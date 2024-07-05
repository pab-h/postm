import { PrismaClient } from "@prisma/client";
import fs from "fs";
import Post from "../entities/post";
import env from "../env";
import path from "path";

export default class Repository {
    
    private prisma: PrismaClient;

    public constructor() {
        this.prisma = new PrismaClient();
    }

    public async update(id: string, title: string, description: string, image: string | null): Promise<Post> {
        const oldPost = await this.prisma.post.findUnique({
            where: { id }
        });

        const imageOld = oldPost?.image;

        if (imageOld) {
            fs.unlink(
                path.join(env.UPLOAD_PATH, imageOld), 
                error => {
                    if (error) {
                        throw new Error(`Error removing file: ${ error }`);
                    }
              }
            );
        }
        
        const post = await this.prisma.post.update({
            data: {
                title, 
                description, 
                image
            },
            where: { id }
        });

        return new Post(
            post.id,
            post.image,
            post.title,
            post.description
        );
    }

    public async allPaged(index: number, size: number): Promise<Post[]> {
        const postsFound = await this.prisma.post.findMany({
            skip: size * index,
            take: size
        });

        const posts: Post[] = [];

        for(const post of postsFound) {
            posts.push(new Post(
                post.id,
                post.image,
                post.title,
                post.description
            ));
        }

        return posts;
    }

    public async delete(id: string): Promise<boolean> {
        const postFound = await this.prisma.post.findUnique({ where: { id }})

        if (!postFound) {
            return false;
        }
        
        await this.prisma.post.delete({
            where: { id },
            
        });

        return true;
    }

    public async findById(id: string): Promise<Post | null> {
        const post = await this.prisma.post.findUnique({
            where: { id }
        });

        if (!post) {
            return null
        }

        return new Post(
            post.id,
            post.image,
            post.title,
            post.description
        );
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

    public async all(): Promise<Post[]> {
        const posts = await this.prisma.post.findMany();

        const postsParsed: Post[] = [];

        for(const { id, image, title, description } of posts) {
            const postParsed = new Post(
                id,
                image,
                title,
                description
            );
            postsParsed.push(postParsed);
        }

        return postsParsed;
    }

}