import multer from "multer";
import env from "../env";
import { randomBytes }from "crypto";

const allowedExtensions = ["png", "jpeg", "jpg", "gif"];

const storage = multer.diskStorage({
    destination: (request, file, callback) => {
        callback(null, env.UPLOAD_PATH);
    },
    filename: (request, file, callback) => {
        let fileExtension = file.originalname.split('.').pop();

        if (!fileExtension) {
            fileExtension = "";
        }
        
        const newFilename = randomBytes(16).toString("hex");

        callback(null, `${ newFilename }.${ fileExtension }`);
    }
});

const upload = multer({
    storage,
    fileFilter: (request, file, callback) =>  {
        let fileExtension = file.originalname.split('.').pop();

        if (!fileExtension) {
            fileExtension = "";
        }

        if (!allowedExtensions.includes(fileExtension)) {
            callback(new Error(`extension ${ fileExtension } not allowed`));
        }

        callback(null, true);

    }
});

export default upload;