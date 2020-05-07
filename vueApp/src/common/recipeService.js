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

    get_scaled(id, numberOfPeople) {
        let requestUrl = `${this.apiService.url}/${id}?numberOfPeople=${numberOfPeople}`;
        return fetch(requestUrl)
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
    }

    getRandomlyChosen(number, tags) {
        let tagsString = tags.join(",")
        let requestUrl = `${this.apiService.url}/random?number=${number}&tags=${tagsString}`;
        return fetch(requestUrl)
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
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