import Repository from "../repositories/posts";
import Post from "../entities/post";

export default class Service {

    private repository: Repository;

    public constructor() {
        this.repository = new Repository();
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