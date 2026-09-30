document.addEventListener("DOMContentLoaded", function(){
    let form=document.getElementById("Name_AI_form");
    form.addEventListener("submit", function(event){
        let text=document.getElementById("AI_name").value;
        let existing_names=document.getElementsByClassName("AI_names");
        let c=0;
        let L=existing_names.length;
        while (c<L){
            if (existing_names[c].value==text){
                alert("You can't have two AIs with the same name.");
                event.preventDefault();
            }
            c=c+1;
        }
    })
});