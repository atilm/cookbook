export const FoodService = {
    getAll() {
        return fetch("http://localhost:5000/api/food")
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
    }
};