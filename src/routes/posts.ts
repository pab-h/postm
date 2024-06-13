import { Router, Request, Response } from "express";

const router = Router();

router.post("/create", (request: Request, response: Response) => {
    response.send({
        "createdAt": "",
        "description": "",
        "id": "",
        "image": null,
        "title": "",
        "updatedAt": ""
    });
});

router.get("/all", (request: Request, response: Response) => {
    response.send({
        "posts": [
            {
                "createdAt": "",
                "description": "",
                "id": "",
                "image": null,
                "title": "",
                "updatedAt": ""
            },
            {
                "createdAt": "",
                "description": "",
                "id": "",
                "image": null,
                "title": "",
                "updatedAt": ""
            },
            {
                "createdAt": "",
                "description": "",
                "id": "",
                "image": null,
                "title": "",
                "updatedAt": ""
            },
        ]
    });
});

router.get("/find/:id", (request: Request, response: Response) => {
    response.send({
        "createdAt": "",
        "description": "",
        "id": "",
        "image": null,
        "title": "",
        "updatedAt": ""
    });
});

router.delete("/delete/:id", (request: Request, response: Response) => {
    response.send({
        "message": ""
    });
});

router.put("/update/:id", (request: Request, response: Response) => {
    response.send({
        "message": ""
    });
});


router.get("/all/page", (request: Request, response: Response) => {
    response.send({
        "next": "",
        "posts": [
            {
                "createdAt": "",
                "description": "",
                "id": "",
                "image": null,
                "title": "",
                "updatedAt": ""
            },
            {
                "createdAt": "",
                "description": "",
                "id": "",
                "image": null,
                "title": "",
                "updatedAt": ""
            },
            {
                "createdAt": "",
                "description": "",
                "id": "",
                "image": "",
                "title": "",
                "updatedAt": ""
            }
        ],
        "previous": null
    });
});

export default router;
