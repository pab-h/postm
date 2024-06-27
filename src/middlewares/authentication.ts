import { Request, Response, NextFunction } from "express";
import { z } from "zod";
import jwt from "jsonwebtoken";
import env from "../env";

const headerSchema = z.object({
    authorization: z.string({ message: "Authorization header required" })
});

const payloadSchema = z.object({
    id: z.string({ message: "id required" })
});

export default class Authentication {

    public auth(request: Request, response: Response, next: NextFunction) {

        try {
            const { authorization } = headerSchema.parse(request.headers);
    
            const parts = authorization.split(" ");
    
            if (parts.length < 2 || parts[0] != "Bearer") {
                response.status(403).json({
                    error: "authentication token needs to be a jwt"
                });
    
                return;
            }
            const tokenEncoded = parts[1];
    
            const { id } = payloadSchema.parse(
                jwt.verify(tokenEncoded, env.JWT_KEY)
            );

            (request as any).userId = id;

            next();

        } catch (error: any) {

            if (error instanceof z.ZodError) {
                response.status(403).json({
                    message: "token bad formated"
                });
                return;
            }

            response.status(500).json({
                message: error.message
            });

        }

    }


}