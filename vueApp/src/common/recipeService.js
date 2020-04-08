import ApiService from "./api.service";

export default class RecipeService {
    constructor() {
        this.apiService = new ApiService("recipe");
    }

    get_all() {
        return this.apiService.getAll();
    }

    get(id) {
        return this.apiService.get(id);
    }

    create(recipe) {
        return this.apiService.create(recipe);
    }

    update(recipe) {
        return this.apiService.update(recipe);
    }

    delete(id) {
        this.apiService.delete(id);
    }
};