/*function validate(){
    let comments=document.getElementById('c');
    let name=document.getElementById('n');
if(comments==""){
        alert("comments");
        return false;
    }
if(name==""){
        alert("name");
        return false;
}
else{
   document.write (" यो फारम अहिले  पेश हुन सकेन ।
             ( This form could not be submitted now  )")
        return true;

}
}
 validate();*/

var btn= document.getElementById("but");
var input = document.getElementById("inp");
var list = document.getElementById("uli");

btn.addEventListener("click",function(){
    var inputValue = input.value;
    list.insertAdjacentHTML("beforeend", `<li>${inputValue}</li>`);
});

