let url = 'http://localhost:5000/api/food';


var createFoodForm = document.getElementById("createFood");
var nameInput = document.getElementById("foodName");
var caloriesInput = document.getElementById("calories");
var foodList = document.getElementById("foodList");

createFoodForm.addEventListener('submit', createFood);

loadFood();

function createFood(e){
    e.preventDefault();

    let foodObject = {
        "id" : 0,
        "name" : nameInput.value,
        "kcal" : caloriesInput.value
    };

    nameInput.value = null;
    caloriesInput.value = null;

    nameInput.focus();

    sendFood(foodObject);
}

function sendFood(foodObject){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 201) {
            var json = JSON.parse(xhr.responseText);
            addFoodParagraph(json);
        }
    };

    var data = JSON.stringify(foodObject);
    xhr.send(data);
}

function loadFood(){
    fetch(url).then(function(result) {
        console.log('Fetching data');
        return result.json();
    }).then(function(json){
        displayFood(json);
    }).catch(function(e){
        console.log(`Fetch failed: ${ e }`);
    })
}

function displayFood(json){
    let children = foodList.querySelectorAll('p');
    for (let i = 0; i < children.length; i++){
        children[i].remove();
    }

    for(let i = 0; i < json.length; i++){
        let food = json[i];
        addFoodParagraph(food);
    }  
}

function addFoodParagraph(foodObject){
    let paragraph = document.createElement('p');
    paragraph.textContent = `${ foodObject.name } (${ foodObject.kcal })`;
    foodList.appendChild(paragraph);
}