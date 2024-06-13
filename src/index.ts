import "dotenv/config";
import App from "./app";

const app = new App(
    process.env.SERVER_HOST as string,
    Number(process.env.SERVER_PORT)
);

app.run();

