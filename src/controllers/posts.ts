import { Request, Response } from "express";
import Service from "../services/posts";
import { z } from "zod";
import env from "../env";

const createSchema = z.object({
    title: z.string({ message: "title required" }),
    description: z.string({ message: "title required" })
});

const idSchema = z.object({
    id: z.string({ message: "id required "})
});

const pageSchema = z.object({
    size: z.coerce.number().default(10),
    index: z.coerce.number().default(0)

});

const updateSchema = z.object({
    title: z.string({ message: "title required" }),
    description: z.string({ message: "title required" })
});

export default class Controller {

    private service: Service;

    public constructor() {
        this.service = new Service();
        this.create = this.create.bind(this);
        this.all = this.all.bind(this);
        this.find = this.find.bind(this);
        this.delete = this.delete.bind(this);
        this.allPaged = this.allPaged.bind(this);
        this.update = this.update.bind(this);
    }

    public async update(request: Request, response: Response): Promise<void> {
        try {
            const { id } = idSchema.parse(request.params);
            const { 
                title, 
                description 
            } = updateSchema.parse(request.body);

            let image = null;

            if (request.file) {
                image = request.file.filename;
            }

            const post = await this.service.update(
                id,
                title,
                description,
                image
            );

            response.status(200).json(post);

        } catch(error: any) {

            response.status(500).json({
                message: error.message
            });

        }
    }

    public async allPaged(request: Request, response: Response): Promise<void> {
        try {
            const { index, size } = pageSchema.parse(request.query);

            const hostUrl = `${ env.SERVER_HOST }:${ env.SERVER_PORT }`; 

            const page = await this.service.allPaged(index, size);

            for(const post of page.posts) {
                post.image = `${ hostUrl }/api/images/${ post.image }`;
            }

            response.status(200).json({
                posts: page.posts,
                next: `${ hostUrl }/posts/all/page?size=${ size }&index=${ index + 1}`,
                previous: `${ hostUrl }/posts/all/page?size=${ size }&index=${ index - 1}`
            });

        } catch(error: any) {

            response.status(500).json({
                message: error.message
            });

        }
    }

    public async delete(request: Request, response: Response): Promise<void> {
        try {
            const { id } = idSchema.parse(request.params);

            if (!await this.service.delete(id)) {
                response.status(400).json({
                    message: `Unable to remove post ${ id }`
                })                    
                return;
            }
            
            response.status(200).json({
                message: `post ${ id } removed`
            });

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

    public async find(request: Request, response: Response): Promise<void> {
        try {
            const { id } = idSchema.parse(request.params);

            const post = await this.service.findById(id);

            if (!post) {
                response.status(400).json({
                    message: `post ${ id } not exists`
                })                    
                return;
            }
            
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