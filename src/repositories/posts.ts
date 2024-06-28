import { PrismaClient } from "@prisma/client";
import Post from "../entities/post";

export default class Repository {
    
    private prisma: PrismaClient;

    public constructor() {
        this.prisma = new PrismaClient();
    }

    public async create(title: string, description: string, image: string | null): Promise<Post> {

        const post = await this.prisma.post.create({
            data: {
                title, 
                description, 
                image
            }
        });

        return new Post(
            post.id,
            post.image,
            post.title,
            post.description
        );
    }

}