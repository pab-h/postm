import Repository from "../repositories/posts";
import Post from "../entities/post";

type Page = {
    posts: Post[],
    size: number,
    index: number
}

export default class Service {

    private repository: Repository;

    public constructor() {
        this.repository = new Repository();
    }

    public async allPaged(index: number, size: number): Promise<Page> {
        const page: Page = {
            posts: await this.repository.allPaged(index, size),
            size,
            index
        }

        return page;
    }

    public async delete(id: string): Promise<boolean> {
        return await this.repository.delete(id);
    }

    public async findById(id: string): Promise<Post | null> {
        return await this.repository.findById(id);
    }

    public async create(title: string, description: string, image: string | null) : Promise<Post>{
        return await this.repository.create(
            title,
            description,
            image
        );
    }

    public async all(): Promise<Post[]> {
        return await this.repository.all();
    }

}