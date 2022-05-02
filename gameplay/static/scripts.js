function changeAnimalText() {
    const category = document.getElementById("category");
    category.innerHTML = `Animals
    <br>
    <button class="btn btn-danger" id="refresh">Start Over?</button>`;
}

function changeCityText() {
    const category = document.getElementById("category");
    category.innerHTML = `Cities
    <br>
    <button class="btn btn-danger" id="refresh">Start Over?</button>`;
}

function changeFamousText() {
    const category = document.getElementById("category");
    category.innerHTML = `Famous People
    <br>
    <button class="btn btn-danger" id="refresh">Start Over?</button>`;
}

function resetGame(){
    const cat_section = document.getElementById("category-section");
    cat_section.innerHTML = 
        `<div class="category-box" id="category">
            <button class="btn btn-outline-primary" id="famous_people_btn">Famous People</button>
            <button class="btn btn-outline-primary" id="cities_btn">Cities</button>
            <button class="btn btn-outline-primary" id="animals_btn">Animals</button>
            <p class="category">Choose a category</p>
        </div>`
}

function myFirstAjax(){
    console.log("It's working!")



    // $.ajax({
    //     url : "127"
    //     type : "POST", // http method
    //     data : {
    //       name:"name",
    //       csrfmiddlewaretoken: '{{ csrf_token }}' , //This is must for security in Django
    //     }, // data sent with the post request
    //
    //     // handle a successful response
    //     success : function(response){
    //       alert(response["name"]);
    //     },
    //
    //     // // handle a non-successful response
    //     // error : function() {
    //     // .....
    //     }
    // });
}

/* Event listeners */

document.addEventListener("click", function (event){

    if (event.target.id === "famous_people_btn"){
        changeFamousText();
    }

    if (event.target.id === "cities_btn"){
        changeCityText();
    }

    // if (event.target.id === "animals_btn"){
    //     changeAnimalText();
    // }

    if (event.target.id === "refresh"){
        resetGame();
    }

});

