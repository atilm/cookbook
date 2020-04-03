import ApiService from "./api.service";

export default class FoodService extends ApiService {
    constructor() {
        super("food");
    }
};