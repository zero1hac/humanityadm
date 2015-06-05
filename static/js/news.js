function check(){
    var r = confirm("You will not be able to change the input data if you submit the form .Are you sure to submit?");
    if(r == true)
    {
    document.getElementById('forms').submit();
    }

    }
