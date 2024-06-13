import express from "express";
import { Express, Request, Response } from "express";

export default class App {

    private express: Express;
    private host: string;
    private port: number;

    constructor(host: string, port: number) {
        this.express = express();
        this.host = host; 
        this.port = port;

        this.express.get("/api/hi", (request: Request, response: Response) => {
            response.send({
                "hello": "world"
            });
        });

    }

    public run(): void {
        this.express.listen(this.port, () => {
            console.log(
                `Server listen on ${ this.host }:${ this.port }`
            );
        });

    }

}