import Repository from "../repositories/users";
import bcrypt from "bcrypt";
import env from "../env";
import jwt from "jsonwebtoken";
import User from "../entities/user";

export class Service {

    private repository: Repository;

    public constructor() {
        this.repository = new Repository();
    }

    public async create(username: string, email: string, password: string): Promise<User> {

        if (await this.repository.findByEmail(email)) {
            throw new Error(`email ${ email } already exists`);
        }
        
        const user = await this.repository.create(
            username,
            email,
            password
        ); 

        user.password = "";

        return user;
    }

    public async login(email: string, password: string): Promise<string> {

        const user = await this.repository.findByEmail(email);

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

    public async delete(id: string): Promise<boolean> {

        if (!await this.repository.findById(id)) {
            throw new Error(`id ${ id } not exists`);
        }

        return await this.repository.delete(id);
    }

    public async update(id: string, username: string, email: string, password: string): Promise<User> {

        const userFound = await this.repository.findById(id);

        if(!userFound) {
            throw new Error(`user ${ id } not exists`);
        }

        const hasEmailChanged = userFound.email != email; 
        const hasAvailableEmail = await this.repository.findByEmail(email);

        if (hasEmailChanged && hasAvailableEmail) {
            throw new Error (`email ${ email } already exists`);
        }

        const userUpdated = await this.repository.update(
            id,
            username,
            email,
            password
        );

        userUpdated.password = "";

        return userUpdated;
    }

}