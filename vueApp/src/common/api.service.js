export default class FoodService {
    constructor() {
        this.url = "http://localhost:5000/api/food";
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
    
    createFood(foodObject) {
        return fetch(this.url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(foodObject),
        })
        .then((response) => response.json())
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    deleteFood(id) {
        return fetch(`${this.url}/${id}`, {
            method: 'DELETE'
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    updateFood(foodObject) {
        return fetch(`${this.url}/${foodObject.id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(foodObject),
            })
            .then((response) => response.json())
            .catch((error) => {
                console.error('Error:', error);
            });
    }
};