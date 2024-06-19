import Repository from "../repositories/users";
import bcrypt from "bcrypt";
import env from "../env";
import jwt from "jsonwebtoken";

export class Service {

    private repository: Repository;

    public constructor() {

        this.repository = new Repository();
        
    }

    public create(username: string, email: string, password: string) {

        if (this.repository.findByEmail(email)) {
            throw new Error(`email ${ email } already exists`);
        }
        
        return this.repository.create(
            username,
            email,
            password
        );
    }

    public async login(email: string, password: string): Promise<string> {

        const user = this.repository.findByEmail(email);

        if (!user) {
            throw new Error(`email ${ email } already exists`);
        }

        if (!await bcrypt.compare(password, user.password)) {
            throw new Error(`wrong password for ${ email }`);
        }

        return jwt.sign(
            { id: user.id }, 
            env.JWT_KEY, 
            { expiresIn: "1h" }
        );
    }

    public delete(id: string) {

        if (!this.repository.findById(id)) {
            throw new Error(`id ${ id } not exists`);
        }

        return this.repository.delete(id);
    }

    public update(id: string, username: string, email: string, password: string) {

        const userFound = this.repository.findById(id);

        const hasEmailChanged = userFound.email != email; 
        const hasAvailableEmail = this.repository.findByEmail(email);

        if (hasEmailChanged && hasAvailableEmail) {
            throw new Error (`email ${ email } already exists`);
        }

        return this.repository.update(
            id,
            username,
            email,
            password
        );
    }

}