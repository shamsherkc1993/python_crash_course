console.log("hi")

let fefaultColor = "red";

function changeColor(newColor){
    let greenLight = document.querySelector(".green");
    let redLight = document.querySelector(".red");
    let yellowLight = document.querySelector(".yellow");

    if(newColor === "green"){
        greenLight.style.backgroundColor = "green";
        redLight.style.backgroundColor = "grey";
        yellowLight.style.backgroundColor = "grey";
    } else if(newColor === "red"){
        greenLight.style.backgroundColor = "grey";
        redLight.style.backgroundColor = "red";
        yellowLight.style.backgroundColor = "grey";
    } else if(newColor === "yellow"){
        greenLight.style.backgroundColor = "grey";
        redLight.style.backgroundColor = "grey";
        yellowLight.style.backgroundColor = "yellow";
    }
}

let button = document.querySelector("button");
button.addEventListener("click", function(){
    if(fefaultColor === "red"){
        changeColor("green");
        fefaultColor = "green";
    } else if(fefaultColor === "green"){
        changeColor("yellow");
        fefaultColor = "yellow";
    } else if(fefaultColor === "yellow"){
        changeColor("red");
        fefaultColor = "red";
    }
})          