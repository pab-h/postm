import { Router } from "express";
import Controller from "../controllers/users";
import Authentication from "../middlewares/authentication";

const router = Router();
const controller = new Controller();
const middleware = new Authentication();

router.post("/create", controller.create);

router.post("/login", controller.login);

router.delete("/delete", middleware.auth, controller.delete);

router.put("/update", middleware.auth, controller.update);

export default router;
