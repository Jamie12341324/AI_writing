document.addEventListener("DOMContentLoaded", function(){
    let form=document.getElementById("train_form");
    form.addEventListener("submit", function(event){
        let text=document.getElementById("train_AI").value;
        if (text.length>0){
            let char=text[text.length-1];
            if (char!="." && char!="?" && char!="!"){
                alert("Training texts must finish with a punctuation mark like a full stop, question mark or exclamation.");
                event.preventDefault();
            }
        }else{
            alert("Training text must have a value to be used as training.");
            event.preventDefault();
        }
    });
});