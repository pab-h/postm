import { Request, Response } from "express";
import { z } from "zod";

const userSchema = z.object({
    username: z.string(),
    email: z.string().email(),
    password: z.string()
});

const loginSchema = z.object({
    email: z.string().email(),
    password: z.string()
});

export default class Controller {
    public create(request: Request, response: Response) {
        try {

            const { 
                email, 
                password, 
                username
            } = userSchema.parse(request.body);

            console.log(email, password, username);

            response.json({
                "createdAt": "",
                "email": "",
                "id": "",
                "password": null,
                "updatedAt": "",
                "username": ""
            });

        } catch (error) {

            if (error instanceof z.ZodError) {
                response.status(400).json(error);
                return;
            }

            response.status(500).json({
                message: "something unexpected happened"
            });

        }
    }

    public login(request: Request, response: Response) {
        try {

            const { 
                email, 
                password 
            } = loginSchema.parse(request.body);

            console.log(email, password);

            response.json({
                "token": ""
            });

        } catch (error) {

            if (error instanceof z.ZodError) {
                response.status(400).json(error);
                return;
            }

            response.status(500).json({
                message: "something unexpected happened"
            });

        }
    }

    public delete(request: Request, response: Response) {
        response.json({
            "message": ""
        });
    }

    public update(request: Request, response: Response) {
        try {

            const { 
                email, 
                password, 
                username
            } = userSchema.parse(request.body);

            console.log(email, password, username);

            response.json({
                "createdAt": "",
                "email": "",
                "id": "",
                "password": null,
                "updatedAt": "",
                "username": ""
            });

        } catch (error) {

            if (error instanceof z.ZodError) {
                response.status(400).json(error);
                return;
            }

            response.status(500).json({
                message: "something unexpected happened"
            });

        }
    }
    
}