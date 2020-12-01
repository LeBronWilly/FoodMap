


$("#chose_country").change(function () {
    var value = $("#chose_country").val();
    if(value==1){
        document.getElementById('select_city_3').hidden = true;
        document.getElementById('select_city_2').hidden = true;
        document.getElementById('twzipcode').hidden = false;
    }else if((value==2)){
        document.getElementById('twzipcode').hidden = true;
        document.getElementById('select_city_3').hidden = true;
        document.getElementById('select_city_2').hidden = false;
    }
    else {
        document.getElementById('twzipcode').hidden = true;
        document.getElementById('select_city_2').hidden = true;
        document.getElementById('select_city_3').hidden = false;

    }
});