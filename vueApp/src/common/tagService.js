import ApiService from "./api.service";

export default class TagService {
    constructor() {
        this.apiService = new ApiService("tag");
    }

    get_all() {
        return this.apiService.getAll();
    }
};