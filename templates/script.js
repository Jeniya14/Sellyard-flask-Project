function search(){
    let input=document.getElementById("search-box").input
    input=input.toLowerCase();
    if(input=="fruits"){
        window.location.href="fruits.html";
    }
    else if(input=="vegetables"){
        window.location.href="vegetables.html";
    }
    else if(input=="homemade"){
        window.location.href="homemade.html";
    }
    else if(input=="handicraft"){
        window.location.href="handicraft.html";
    }
    else if(input=="gifts"){
        window.location.href="gifts.html";
    }
}