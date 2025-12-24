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

let btn= document.getElementById("but");
let input = document.getElementById("inp");
let list = document.getElementById("uli");

btn.addEventListener("click",function(){
    let inputValue = input.value;
    list.insertAdjacentHTML("beforeend", `<li>${inputValue}</li>`);
});
