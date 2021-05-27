document.getElementById('hablar').addEventListener("click",()=>{
    decir(document.getElementById("mensaje").value);
});

function decir(mensaje){
    speechSynthesis.speak(new SpeechSynthesisUtterance(mensaje));
}