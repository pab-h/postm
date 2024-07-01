import { Request, Response } from "express";
import Service from "../services/posts";
import { z } from "zod";
import env from "../env";

const createSchema = z.object({
    title: z.string({ message: "title required" }),
    description: z.string({ message: "title required" })
});

export default class Controller {

    private service: Service;

    public constructor() {
        this.service = new Service();
        this.create = this.create.bind(this);
        this.all = this.all.bind(this);
    }

    public async create(request: Request, response: Response): Promise<void> {
        try {
            const { 
                title, 
                description 
            } = createSchema.parse(request.body);

            let image = null;

            if (request.file) {
                image = request.file.filename;
            }

            const post = await this.service.create(
                title, 
                description, 
                image
            );

            const hostUrl = `${ env.SERVER_HOST }:${ env.SERVER_PORT }`; 

            post.image = `${ hostUrl}/api/images/${ post.image }`;

            response.status(200).json(post);

        } catch(error: any) {

            if (error instanceof z.ZodError) {
                response.status(400).json({
                    message: error.issues[0].message
                });
                return;
            }

            response.status(500).json({
                message: error.message
            });

        }
    }

    public async all(request: Request, response: Response): Promise<void> {
        try {

            const hostUrl = `${ env.SERVER_HOST }:${ env.SERVER_PORT }`; 

            const posts = await this.service.all();

            for(const post of posts) {
                post.image = `${ hostUrl}/api/images/${ post.image }`;
            }

            response.status(200).json({ posts });

        } catch(error: any) {

            response.status(500).json({
                message: error.message
            });

        }
    }

}