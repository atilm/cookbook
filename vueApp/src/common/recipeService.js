import ApiService from "./api.service";

export default class RecipeService {
    constructor() {
        this.apiService = new ApiService("recipe");
    }

    get_all() {
        return this.apiService.getAll();
    }

    get_by_search_term(searchTerm) {
        return this.apiService.getBySearchTerm(searchTerm);
    }

    get(id) {
        return this.apiService.get(id);
    }

    getRandomlyChosen(number) {
        return this.apiService.getRandomlyChosen(number);
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