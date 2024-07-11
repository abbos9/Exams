const colors = ["red", "#56ac3d", "white", "black", "orange", "blue", "green"];

function randColor() {
  const rand = Math.floor(Math.random() * colors.length);
  let changebg = document.querySelector(".press");
  changebg.style = `background-color: ${colors[rand]}`;
}

function randomiser() {
  let randomNum = Math.round(Math.random() * 99 + 1);
  document.querySelector(".result").textContent = randomNum;
}

function background() {
  let changebg = document.querySelector(".press");
  changebg.style = "background-color: red";
}
const a = prompt("Введите число только не буквы!!!");
if (a % 2 == 0) {
  if (a == 0) alert("siz 0 yozdiz");
  else alert("это число четное ");
} else alert("это число нечетное");

function bodybg() {
  document.querySelector(".name").textContent = "Saidabbos";
}
