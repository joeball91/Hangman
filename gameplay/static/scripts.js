function changeAnimalText() {
    const category = document.getElementById("category");
    let button = category.innerHTML = 'Animals';
}

function changeCityText() {
    const category = document.getElementById("category");
    let button = category.innerHTML = 'Cities';
}

function changeFamousText() {
    const category = document.getElementById("category");
    let button = category.innerHTML = 'Famous People';
}

const famousButton = document.getElementById("famous_people_btn");
const citiesButton = document.getElementById("cities_btn");
const animalsButton = document.getElementById("animals_btn");

/* Event listener */
famousButton.addEventListener("click", changeFamousText);
citiesButton.addEventListener("click", changeCityText);
animalsButton.addEventListener("click", changeAnimalText);


