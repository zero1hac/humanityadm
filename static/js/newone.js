function fcheck(){
    x = document.getElementById("checker").value;
    if(x=="ok"){
    document.getElementById("corres_addr").value = document.getElementById("perma_addr").value;
    }
    else
    {
    if(document.getElementById("corres_addr").value = document.getElementById("perma_addr").value)
    document.getElementById("corres_addr").value = "";
    }
    }

