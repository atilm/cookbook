import ApiService from "./api.service";

export default class RecipeCollectionService {
    constructor() {
        this.apiService = new ApiService("recipeCollection");
    }

    get_all() {
        return this.apiService.getAll();
    }

    get(id){
        return this.apiService.get(id);
    }

    create(recipeCollection) {
        return this.apiService.create(recipeCollection);
    }

    update(recipeCollection) {
        return this.apiService.update(recipeCollection);
    }

    delete(id) {
        return this.apiService.delete(id);
    }
}