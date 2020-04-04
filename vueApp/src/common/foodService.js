import ApiService from "./api.service";

export default class FoodService extends ApiService {
    constructor() {
        super("food");
    }

    get_all_names() {
        return this.getAll().then(items => items.map(food => {
            return { "id": food.id, "name": food.name};
         }));
    }
};