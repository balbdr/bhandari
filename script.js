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
    document.write(" फारम पेश भयो (your form is submitted)");
    return true;
}
}
document.write validate();
