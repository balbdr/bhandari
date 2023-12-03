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
   document.write (" यो फारम अहिले  पेश हुन सकेन ।
             ( This form could not be submitted now  )")
        return true;

}
}
 validate();
