import { Router, Request, Response } from "express";
import Controller from "../controllers/users";

const router = Router();
const controller = new Controller();

router.post("/create", controller.create);

router.post("/login", controller.login);

router.delete("/delete", controller.delete);

router.put("/update", controller.update);

export default router;
