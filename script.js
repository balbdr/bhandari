function validate(){
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
    console.log("प्राबिधिक कारणले यो फारम अहिले पेश हुनसकेन ।")
return true;
}
}
 validate();
