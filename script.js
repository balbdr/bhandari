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
    document.write("केही प्राबधिक कारणले गर्दा यो फारम अहिले  पेशहुन सकेन ");
    return true;
}
}
 validate();
