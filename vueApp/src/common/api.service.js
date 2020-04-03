export default class ApiService {
    constructor(endpoint) {
        this.url = `http://localhost:5000/api/${endpoint}`;
    }

    getAll() {
        return fetch(this.url)
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
    }

    getBySearchTerm(searchTerm) {
        let requestUrl = `${this.url}?searchTerm=${searchTerm}`;
        return fetch(requestUrl)
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
    }

    getRandomlyChosen(number) {
        let requestUrl = `${this.url}/random?number=${number}`;
        return fetch(requestUrl)
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
    }
    
    create(object) {
        return fetch(this.url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(object),
        })
        .then((response) => response.json())
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    delete(id) {
        return fetch(`${this.url}/${id}`, {
            method: 'DELETE'
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    update(object) {
        return fetch(`${this.url}/${object.id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(object),
            })
            .then((response) => response.json())
            .catch((error) => {
                console.error('Error:', error);
            });
    }
};

export default class FoodService extends ApiService {
    constructor() {
        super("Food");
    }
};

export default class RecipeService {
    constructor() {
        this.apiService = new ApiService("Recipe");
    }

    get_all() {
        return this.apiService.getAll();
    }
};