export default class User {
    
    readonly id: string;
    public image: string | null;
    public title: string;
    public description: string;

    public constructor(id: string, image: string | null, title: string, description: string) {
        this.id = id;
        this.image = image;
        this.title = title;
        this.description = description;
    }

}