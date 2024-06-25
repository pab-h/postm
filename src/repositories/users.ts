import { PrismaClient } from "@prisma/client";
import User from "../entities/user";
import bcrypt from "bcrypt";
import env from "../env";

export default class Repository {

    private prisma: PrismaClient;

    public constructor() {
        this.prisma = new PrismaClient();
    }

    public async update(id: string, username: string, email: string, password: string): Promise<User> {
        const hashedPassword = await bcrypt.hash(
            password,
            env.SALT_ROUNDS
        );
        
        const userUpdated = await this.prisma.user.update({
            data: {
                username,
                email,
                password: hashedPassword
            },
            where: { id }
        });

        return new User(
            userUpdated.id,
            userUpdated.username,
            userUpdated.email,
            userUpdated.password
        );
    }

    public async delete(id: string): Promise<boolean> {
        const userDeleted = await this.prisma.user.delete({
            where: { id }
        });

        return Boolean(userDeleted);
    }

    public async findById(id: string): Promise<User | null> {
        const userFound = await this.prisma.user.findUnique({
            where: { id }
        });

        if (!userFound) {
            return null;
        }

        return new User(
            userFound.id,
            userFound.username,
            userFound.email,
            userFound.password
        );
    }

    public async create(username: string, email: string, password: string): Promise<User> {
        
        const hashedPassword = await bcrypt.hash(
            password,
            env.SALT_ROUNDS
        );

        const user = await this.prisma.user.create({
            data: {
                email, 
                password: hashedPassword, 
                username
            }
        });

        return new User(
            user.id,
            user.username,
            user.email,
            user.password
        );
    }

    public async findByEmail(email: string): Promise<User | null> {
        const userFound = await this.prisma.user.findUnique({
            where: { email }
        });

        if (!userFound) {
            return null;
        }

        return new User(
            userFound.id,
            userFound.username,
            userFound.email,
            userFound.password
        );
    }

}