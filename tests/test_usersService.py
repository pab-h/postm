import unittest

from unittest.mock import MagicMock
from unittest.mock import patch

from postm.repositories.users import UserRepository
from postm.entities.user import User

from hashlib import sha256

from datetime import datetime

from postm.services.users import UsersService

class TestUsersService(unittest.TestCase):
    def setUp(self):
        self.userService = UsersService()
        self.userService.repository = MagicMock(spec=UserRepository)

    def test_create_user_success(self):
        self.userService.repository.findByEmail.return_value = None
        self.userService.repository.create.return_value = User(
            id='1', username='test', email='test@example.com', password='hashedpassword',
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        user = self.userService.create('test', 'test@example.com', 'password')

        self.userService.repository.create.assert_called_once()
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_user_no_username(self):
        with self.assertRaises(Exception) as context:
            self.userService.create('', 'test@example.com', 'password')
        self.assertEqual(str(context.exception), 'username is not provided')

    def test_create_user_existing_email(self):
        self.userService.repository.findByEmail.return_value = User(
            id='1', username='test', email='test@example.com', password='hashedpassword',
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        with self.assertRaises(Exception) as context:
            self.userService.create('test', 'test@example.com', 'password')
        self.assertEqual(str(context.exception), 'email test@example.com already exists')

    def test_login_success(self):
        password = 'password'
        password_hash = sha256(password.encode()).hexdigest()
        user = User(
            id='1', username='test', email='test@example.com', password=password_hash,
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )
        self.userService.repository.findByEmail.return_value = user

        with patch('postm.services.users.getenv') as mock_getenv:
            mock_getenv.side_effect = lambda key, default=None: 'secret' if key == 'JWT_KEY' else default
            token = self.userService.login('test@example.com', password)

        self.assertIsInstance(token, str)

    def test_login_wrong_password(self):
        self.userService.repository.findByEmail.return_value = User(
            id='1', username='test', email='test@example.com', password='differenthashedpassword',
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        with self.assertRaises(Exception) as context:
            self.userService.login('test@example.com', 'password')
        self.assertEqual(str(context.exception), "('wrong password for test@example.com', 403)")

    def test_findByEmail(self):
        self.userService.repository.findByEmail.return_value = User(
            id='1', username='test', email='test@example.com', password='hashedpassword',
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        user = self.userService.findByEmail('test@example.com')

        self.assertEqual(user.email, 'test@example.com')

    def test_findById(self):
        self.userService.repository.findById.return_value = User(
            id='1', username='test', email='test@example.com', password='hashedpassword',
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        user = self.userService.findById('1')

        self.assertEqual(user.id, '1')

    def test_delete(self):
        self.userService.repository.delete.return_value = True

        result = self.userService.delete('1')

        self.assertTrue(result)

    def test_update_user_success(self):
        self.userService.repository.findById.return_value = User(
            id='1', username='test', email='test@example.com', password='hashedpassword',
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )
        self.userService.repository.findByEmail.return_value = None  # Ensure email does not exist
        self.userService.repository.update.return_value = User(
            id='1', username='newusername', email='newemail@example.com', password='newhashedpassword',
            createdAt=str(datetime.now()), updatedAt=str(datetime.now())
        )

        user = self.userService.update('1', 'newusername', 'newemail@example.com', 'newpassword')

        self.assertEqual(user.username, 'newusername')
        self.assertEqual(user.email, 'newemail@example.com')

if __name__ == '__main__':
    unittest.main()
