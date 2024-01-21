const passwd = document.getElementById("passwd");
const btnPasswd = document.getElementById("buttonRemovePasswd");

if(btn.addEventListener("click",()=>{
    btn.style.display = "none";
    btnPasswd.style.display = "block";
    passwd.style.display = "block";
})); else {
    btnPasswd.style.display = "none";
    passwd.style.display = "none";
};

if(btnPasswd.addEventListener("click",()=>{
    btn.style.display = "block";
    btnPasswd.style.display = "none";
    passwd.style.display = "none";
}));

const btn = document.getElementById("kirim");
const myForm = document.getElementById("form");

btn.addEventListener("click", () => {
    myForm.reset()
});

document.getElementById("back").addEventListener("click",() => {
    window.location.href = "index.html";
});