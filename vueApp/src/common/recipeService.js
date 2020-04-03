import ApiService from "./api.service";

export default class RecipeService {
    constructor() {
        this.apiService = new ApiService("recipe");
    }

    get_all() {
        return this.apiService.getAll();
    }
};