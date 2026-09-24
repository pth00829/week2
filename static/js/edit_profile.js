const name1=document.getElementById('name')
const school=document.getElementById('school')

fetch('/board/profile/get-data')
.then(res=>res.json())
.then(data=>{
    if(data.success){
        name1.value=data.name
        school.value=data.school
    }
})

document.getElementById('edit_user_data').addEventListener('submit',function(e){
    e.preventDefault()

    const formData=new FormData(this)
    fetch('/board/profile/edit-data',{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            window.location.href='/board/profile'
        }
        else{
            window.location.href='/board/profile'
        }
    })
})