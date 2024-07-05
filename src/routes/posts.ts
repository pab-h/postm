import { Router, Request, Response } from "express";
import Controller from "../controllers/posts";

import upload from "../middlewares/upload";
import Authentication from "../middlewares/authentication";

const controller = new Controller();
const router = Router();
const userAuth = new Authentication();

router.post(
    "/create", 
    upload.single("image"), 
    controller.create
);

router.get("/all", userAuth.auth, controller.all);

router.get("/find/:id", userAuth.auth, controller.find);

router.delete("/delete/:id", userAuth.auth, controller.delete);

router.put(
    "/update/:id", 
    userAuth.auth,
    upload.single("image"), 
    controller.update
);

router.get("/all/page", userAuth.auth, controller.allPaged);

export default router;
