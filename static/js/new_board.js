document.getElementById('main').addEventListener('submit',function(e){
    e.preventDefault()
    const formData=new FormData(this)
    
    fetch('/board/main/create',{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            alert('저장 성공하였습니다.')
            window.location.href='/board/main'
        }
        else{
            alert('저장 실패하였습니다.')
        }
    })
})

document.getElementById('return_main').addEventListener('click',function(){
    window.location.href='/board/main'
})