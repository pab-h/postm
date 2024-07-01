import { Router, Request, Response } from "express";
import Controller from "../controllers/posts";
import upload from "../middlewares/upload";

const controller = new Controller();
const router = Router();

router.post(
    "/create", 
    upload.single("image"), 
    controller.create
);

router.get("/all", controller.all);

router.get("/find/:id", controller.find);

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
