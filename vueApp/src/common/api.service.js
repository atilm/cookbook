export const FoodService = {
    getAll() {
        return fetch("http://localhost:5000/api/food")
            .then(result => result.json())
            .catch(function(e){
                console.log(`Fetch failed: ${ e }`);
            });
    },
    createFood(foodObject) {
        return fetch("http://localhost:5000/api/food", {
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
};