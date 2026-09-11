document.getElementById('sign_up').addEventListener('submit',function(e) {
    e.preventDefault();
    const formData=new FormData(this)

    fetch('/sign_up',{
        method:"POST",
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success) {
            window.location.href='/'
        }
        else {
            alert(data.message)
        }
    })
    .catch(error=>console.error('에러 : ',error))
})