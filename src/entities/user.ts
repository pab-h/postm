export default class User {
    
    readonly id: string;
    public username: string;
    public email: string;
    public password: string;

    public constructor(id: string, username: string, email: string, password: string) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.password = password;
    }

}