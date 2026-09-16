document.addEventListener("DOMContentLoaded", function(){
let form2=document.getElementById("input_form");
alert("hi");
    form2.addEventListener("submit", function(event){
        alert("hello");
        const button = event.submitter;
        alert(button);
        console.log(button);
        let text="";
        if (button.id=="talk_AI_button"){
            text=document.getElementById("talk_AI").value;
        }
        else if (button.id=="talk_AI_button2"){
            text=document.getElementById("response_AI").value;
        }
        else if (button.id=="talk_AI_button2a"){
            text=document.getElementById("response_AI1").value;
        }
        else if (button.id=="talk_AI_button2b"){
            text=document.getElementById("response_AI2").value;
        }
        else if (button.id=="talk_AI_button2c"){
            text=document.getElementById("response_AI3").value;
        }
        if (text.length<2){
            alert("Starting texts or response texts used as a start must have a value to be used to make a response text.");
            event.preventDefault();
        }
    });
});