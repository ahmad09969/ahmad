// هذه الدالة تقوم بأخفاء وأطهار العناصر
function show_hide_elem(elem){
    const elem1 = document.getElementById(elem);
    if(elem1.style.display == "none"){
        elem1.style.display = "block" ;
    } else {
        elem1.style.display = "none" ;
    }
}
let degre = 0 ;
function rote_180_degre(elem){
    const elem1 = document.getElementById(elem);
    if(degre == 0){
        degre = 1 ;
        elem1.style.transform = "rotate(180deg)" ;
    } else {
        elem1.style.transform = "rotate(0deg)" ;
        degre = 0 ;
    }
}
let shadow = 0 ;
function show_hid_shadow(elem){
    const elem1 = document.getElementById(elem);
    if(shadow == 0){
        shadow = 1 ;
        elem1.style.boxShadow = "1px 1px 18px" ;
    } else {
        elem1.style.boxShadow = "0px 0px 0px" ;
        shadow = 0 ;
    }
}