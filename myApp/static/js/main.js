// let navigation = document.querySelector('.navigation');
// let nav_bar = document.querySelector('.nav--bar');
// document.querySelector('.toggle').onclick = function() {
//     this.classList.toggle('active');
//     navigation.classList.toggle('active');
// }
// document.querySelectorAll('.nav--bar').onclick = function() {
//     this.classList.toggle('active');
//     navigation.classList.toggle('active');
// }


const text = document.querySelector(".auto-type");
const textload = () => {
    setTimeout(() => {
        text.textContent = "Youtube";
    }, 0)
    setTimeout(() => {
        text.textContent = "Developer";

    }, 4000)
    setTimeout(() => {
        text.textContent = "Frontend";

    }, 8000)
}
textload()
setInterval(textload, 12000);

//loading web page

window.addEventListener("load", () => {
    const loader = document.querySelector(".laoding")
    loader.classList.add('loader-hidden');

    loader.addEventListener("transitionend", () => {
        document.body.removeChild("loader");
    })
})