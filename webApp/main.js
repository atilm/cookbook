let url = 'http://localhost:5000/api/ingredients';

console.log('Starting script.')

var body = document.querySelector('body');

fetch(url).then(function(result) {
    console.log('Fetching data');
    return result.json();
}).then(function(json){
    displayIngredients(json);
}).catch(function(e){
    console.log(`Fetch failed: ${ e }`);
})

function displayIngredients(json){
    for(let i = 0; i < json.length; i++){
        let ingredient = json[i];

        let paragraph = document.createElement('p');
        paragraph.textContent = `${ ingredient.name } (${ ingredient.kcal })`;
        body.appendChild(paragraph);
    }  
}