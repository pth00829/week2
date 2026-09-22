const name=document.getElementById('name')
const school=document.getElementById('school')

fetch('/board/profile/get-data')
.then(res=>res.json())
.then(data=>{
    if(data.success){
        name.value=data.data[0]
        school.value=data.data[1]
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
    })
})