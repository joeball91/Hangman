function alertButton() {
    alert('Clicked');
}

const famous_button = document.getElementById("famous_people_btn");
const cities_button = document.getElementById("cities_btn");
const animals_button = document.getElementById("animals_btn");

/* Event listener */
famous_button.addEventListener("click", alertButton);
cities_button.addEventListener("click", alertButton);
animals_button.addEventListener("click", alertButton);
