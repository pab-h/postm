import { Router, Request, Response } from "express";

const router = Router();

router.post("/create", (request: Request, response: Response) => {
    response.send({
        "createdAt": "",
        "email": "",
        "id": "",
        "password": null,
        "updatedAt": "",
        "username": ""
    });
});

router.post("/login", (request: Request, response: Response) => {
    response.send({
        "token": ""
    });
});

router.delete("/delete", (request: Request, response: Response) => {
    response.send({
        "message": ""
    });
});

router.put("/update", (request: Request, response: Response) => {
    response.send({
        "createdAt": "",
        "email": "",
        "id": "",
        "password": null,
        "updatedAt": "",
        "username": ""
    });
});


export default router;
