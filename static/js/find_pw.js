document.getElementById('change_pw').addEventListener('submit',function(e){
    e.preventDefault()

    const formData=new FormData(this)

    fetch('/user/find/pw',{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            window.location.href=data.url
        }
        else{
            alert(data.message)
        }
    })
})