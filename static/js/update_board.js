const params = new URLSearchParams(window.location.search)
const boardId = params.get('board_id')  // "5" 문자열로 꺼내짐
const title=document.getElementById('title')
const textarea=document.getElementById('textarea')
const secret=document.getElementById('secret_box')

document.getElementById('secret_box').addEventListener('change',function(){
    if(document.getElementById('secret_box').checked){
        document.getElementById('pw').disabled=false
    }
    else{
        document.getElementById('pw').disabled=true
    }
})


if(boardId){
    fetch(`/board/main/correction/data?board_id=${boardId}`)
    .then(res => res.json())
    .then(data => {
        if(data.success){
            title.value = data.title
            textarea.value = data.content
            if(data.secret===1){
                secret.checked=true
            }
            else{
                secret.checked=false
            }
            
        }
    })
}

document.getElementById('main').addEventListener('submit',function(f){
    f.preventDefault();

    if(document.getElementById('secret_box').value==='true'){
        if(document.getElementById('pw').value===""){
            alert('비밀번호를 입력하세요.')
            return;
        }
    }
    const formData=new FormData(this)

    fetch(`/board/main/correction/update?board_id=${boardId}`,{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            alert(data.message)
            window.location.href=`/board/look?board_id=${boardId}`
        }
        else{
            alert('수정에 실패하였습니다.')
        }
        
    }).catch(err=>console.error(err))
})

document.getElementById('return_main').addEventListener('click',function(){
    window.location.href='/board/main'
})