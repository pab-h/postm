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

router.delete("/delete/:id", controller.delete);

router.put(
    "/update/:id", 
    upload.single("image"), 
    controller.update
);

router.get("/all/page", controller.allPaged);

export default router;
