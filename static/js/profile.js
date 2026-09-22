const user_data=document.getElementById('user_data')
fetch('/board/profile/get-data')
.then(res=>res.json())
.then(data=>{
    if(data.success){
        const newP=document.createElement('p')
        const newH3=document.createElement('h3')
        newH3.textContent='이름 : '+data.data[0]
        newP.textContent='학교 : '+data.data[1]
        user_data.appendChild(newH3)
        user_data.appendChild(newP)
    }
})

document.getElementById('edit_profile').addEventListener('click',function(){
    window.location.href='/board/profile/edit'
})