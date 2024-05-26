import unittest
from unittest.mock import MagicMock

from werkzeug.datastructures import FileStorage
from io import BytesIO
from datetime import datetime

from postm.repositories.posts import PostRepository
from postm.repositories.posts import PostPage
from postm.entities.post import Post
from postm.services.posts import PostsService

class TestPostsService(unittest.TestCase):
    def setUp(self):
        self.postsService = PostsService()
        self.postsService.repository = MagicMock(spec=PostRepository)
    
    def test_create_post_success(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.png")
        self.postsService.repository.create.return_value = Post(
            id='1', title='test', description='test description', image=image,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        post = self.postsService.create('test', 'test description', image)

        self.postsService.repository.create.assert_called_once()
        self.assertEqual(post.title, 'test')
        self.assertEqual(post.description, 'test description')

    def test_create_post_no_title(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.png")
        with self.assertRaises(Exception) as context:
            self.postsService.create('', 'test description', image)
        self.assertEqual(str(context.exception), 'title is not provided')

    def test_create_post_no_description(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.png")
        with self.assertRaises(Exception) as context:
            self.postsService.create('test', '', image)
        self.assertEqual(str(context.exception), 'description is not provided')

    def test_create_post_invalid_image_extension(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.bmp")
        with self.assertRaises(Exception) as context:
            self.postsService.create('test', 'test description', image)
        self.assertEqual(str(context.exception), 'bmp not allowed')

    def test_findAll(self):
        self.postsService.repository.findAll.return_value = [
            Post(id='1', title='test', description='test description', image=None,
                 createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
        ]

        posts = self.postsService.findAll()

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, 'test')

    def test_findById_success(self):
        self.postsService.repository.findById.return_value = Post(
            id='1', title='test', description='test description', image=None,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        post = self.postsService.findById('1')

        self.assertEqual(post.id, '1')

    def test_findById_not_exists(self):
        self.postsService.repository.findById.return_value = None

        with self.assertRaises(Exception) as context:
            self.postsService.findById('1')
        self.assertEqual(str(context.exception), 'post 1 not exists')

    def test_delete_post_success(self):
        self.postsService.repository.findById.return_value = Post(
            id='1', title='test', description='test description', image=None,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )
        self.postsService.repository.delete.return_value = True

        result = self.postsService.delete('1')

        self.assertTrue(result)

    def test_delete_post_not_exists(self):
        self.postsService.repository.findById.return_value = None

        with self.assertRaises(Exception) as context:
            self.postsService.delete('1')
        self.assertEqual(str(context.exception), 'post 1 not exists')

    def test_update_post_success(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.png")
        self.postsService.repository.findById.return_value = Post(
            id='1', title='test', description='test description', image=None,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )
        self.postsService.repository.update.return_value = True

        result = self.postsService.update('1', 'new title', 'new description', image)

        self.assertTrue(result)

    def test_update_post_not_exists(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.png")
        self.postsService.repository.findById.return_value = None

        with self.assertRaises(Exception) as context:
            self.postsService.update('1', 'new title', 'new description', image)
        self.assertEqual(str(context.exception), 'post 1 not exists')

    def test_update_post_no_title(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.png")
        self.postsService.repository.findById.return_value = Post(
            id='1', title='test', description='test description', image=None,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        with self.assertRaises(Exception) as context:
            self.postsService.update('1', '', 'new description', image)
        self.assertEqual(str(context.exception), 'title is not provided')

    def test_update_post_no_description(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.png")
        self.postsService.repository.findById.return_value = Post(
            id='1', title='test', description='test description', image=None,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        with self.assertRaises(Exception) as context:
            self.postsService.update('1', 'new title', '', image)
        self.assertEqual(str(context.exception), 'description is not provided')

    def test_update_post_invalid_image_extension(self):
        image = FileStorage(stream=BytesIO(b"dummy data"), filename="test.bmp")
        self.postsService.repository.findById.return_value = Post(
            id='1', title='test', description='test description', image=None,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        with self.assertRaises(Exception) as context:
            self.postsService.update('1', 'new title', 'new description', image)
        self.assertEqual(str(context.exception), 'bmp not allowed')

    def test_findAllPaged_success(self):
        post_page = PostPage(posts=[
            Post(id='1', title='test', description='test description', image=None,
                 createdAt=str(datetime.now()), updatedAt=str(datetime.now()))
        ], index=0, size=10)
        self.postsService.repository.findAllPaged.return_value = post_page

        paged_posts = self.postsService.findAllPaged(0, 10)

        self.assertEqual(paged_posts.index, 0)
        self.assertEqual(paged_posts.size, 10)
        self.assertEqual(paged_posts.posts[0].title, 'test')

    def test_findAllPaged_invalid_size(self):
        with self.assertRaises(Exception) as context:
            self.postsService.findAllPaged(0, 0)
        self.assertEqual(str(context.exception), 'size must be greater than zero')

    def test_findAllPaged_invalid_index(self):
        with self.assertRaises(Exception) as context:
            self.postsService.findAllPaged(-1, 10)
        self.assertEqual(str(context.exception), 'the index must be positive')

if __name__ == '__main__':
    unittest.main()
