export default class ApiService {
    constructor(endpoint) {
        this.url = `${SERVICE_URL}/${endpoint}`;
    }

    getAll() {
        return fetch(this.url)
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
    }

    get(id) {
        return fetch(`${this.url}/${id}`)
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