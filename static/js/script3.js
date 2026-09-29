document.addEventListener("DOMContentLoaded", function(){
    let form=document.getElementById("text_rename_form");
    form.addEventListener("submit", function(event){
        let text=document.getElementById("text_name").value;
        let existing_names=document.getElementsByClassName("text_names");
        let c=0;
        let L=existing_names.length;
        while (c<L){
            if (existing_names[c].value==text){
                alert("You can't have two texts with the same name.");
                event.preventDefault();
            }
            c=c+1;
        }
    })
});