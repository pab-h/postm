import { Request, Response } from "express";
import { z } from "zod";
import { Service } from "../services/users";

const userSchema = z.object({
    username: z.string({ message: "username required "}),
    email: z
        .string({ message: "email required" })
        .email({ message: "email invalid"}),
    password: z.string({ message: "password required" })
});

const loginSchema = z.object({
    email: z
        .string({ message: "email required" })
        .email({ message: "email invalid"}),
    password: z.string({ message: "password required" })
});

const idSchema = z.object({
    userId: z.string({ message: "id required "})
});

export default class Controller {

    private service: Service;

    public constructor() {
        this.service = new Service();

        this.create = this.create.bind(this);
        this.login = this.login.bind(this);
        this.delete = this.delete.bind(this);
        this.update = this.update.bind(this);
    }

    public async create(request: Request, response: Response) {
        try {

            const { 
                email, 
                password, 
                username
            } = userSchema.parse(request.body);

            const user = await this.service.create(
                username,
                email,
                password
            );

            response.status(200).json(user);

        } catch (error: any) {

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

    public async login(request: Request, response: Response) {
        try {

            const { 
                email, 
                password 
            } = loginSchema.parse(request.body);

            const token = await this.service.login(email, password);

            response.status(200).json({ token });

        } catch (error: any) {

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

    public async delete(request: Request, response: Response) {

        const { userId } = idSchema.parse(request);

        if (!await this.service.delete(userId)) {
            response.status(400).json({
                message: `Unable to remove user ${ userId }`
            });
            return;
        }

        response.status(200).json({
            message: `user ${ userId } removed`
        });
    }

    public async update(request: Request, response: Response) {
        try {

            const { 
                email, 
                password, 
                username
            } = userSchema.parse(request.body);

            const { userId } = idSchema.parse(request);

            const user = await this.service.update(
                userId,
                username,
                email,
                password
            );

            response.status(200).json(user);

        } catch (error: any) {

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
    
}