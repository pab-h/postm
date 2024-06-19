import Repository from "../repositories/users";

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

}