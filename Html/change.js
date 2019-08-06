function startClick() {
    console.log("Start click");
};
startClick();

var btn = document.getElementById("btn");
console.log(btn);
btn.addEventListener('click', function (e) {
    console.log(e);
})

btn.textContent = "Stop";

var s = document.getElementById("search_bar");
console.log(s);
s.style.backgroundColor = "blue";
s.style.color = "white";

var menu = document.getElementById("menu");
var newLi = document.createElement("li") //dang ko co gi ca
newLi.textContent = "Fries";
menu.appendChild(newLi);

var liList = menu.getElementsByTagName("li");
var fli = liList[0];
fli.remove();

// to kill everything
//menu.textcontent = ""

