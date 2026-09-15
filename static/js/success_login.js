const save=document.getElementById('save')
const delete_data=document.getElementById('delete')
const reset=document.getElementById('reset')
const update=document.getElementById('update')
const p=document.getElementById('p')
const textarea=document.getElementById('textarea')
const title=document.getElementById('title')
const p1=document.getElementById('p1')
const search=document.getElementById('search')

fetch('/board/main/data',{
    method:'get'
})
.then(res=>res.json())
.then(data=>{
    if(data.success){
        p1.textContent=data.title
        p.textContent=data.content
        p.style.display='block' // id가 p인 요소의 style.display를 none에서 block로 변경한다. style.display의 역할은 html을 실행시켰을때 
        save.style.display='none'
        update.style.display='block'
        reset.style.display='none'
        delete_data.style.display='block'
        textarea.style.display='none'
        title.style.display='none'
        p1.style.display='block'
    }
    else{
        p.style.display='none'
        update.style.display='none'
        delete_data.style.display='none'
        p1.style.display='none'
    }
})

document.getElementById('main').addEventListener('submit',function(e){
    e.preventDefault()
    const formData=new FormData(this)
    
    fetch('/board/main',{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            alert('저장 성공하였습니다.')
            p1.textContent=data.title
            p.textContent=data.content
            p.style.display='block'
            save.style.display='none'
            update.style.display='block'
            reset.style.display='none'
            delete_data.style.display='block'
            textarea.style.display='none'
            title.style.display='none'
            p1.style.display='block'
        }
        else{
            alert('저장 실패하였습니다.')
        }
    })
})

document.getElementById('logout_btn').addEventListener('click',function(btn) {
    window.location.href='/user/logout'
})

document.getElementById('secession_btn').addEventListener('click',function(a) {
    window.location.href='/user/secession'
})

update.addEventListener('click',function(){
    p.style.display='none'
    save.style.display='block'
    update.style.display='none'
    reset.style.display='block'
    delete_data.style.display='none'
    textarea.style.display='block'
    title.style.display='block'
    p1.style.display='none'
    fetch('/board/main/data') // 기존 작성했던 코드는 로그아웃 후 재 로그인 시 수정하기를 누르게 되면 기존에 작성된 data들을 불러오지 못했기에 수정
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            title.value=data.title
            textarea.textContent=data.content
        }
        else{
            alert('불러오기 실패')
        }
    })
})

delete_data.addEventListener('click',function(){
    fetch('/board/main/delete')
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            p.style.display='none'
            save.style.display='block'
            update.style.display='none'
            reset.style.display='block'
            delete_data.style.display='none'
            textarea.style.display='block'
            title.style.display='block'
            p1.style.display='none'
            alert('삭제가 완료되었습니다.')
            textarea.value=""
            title.value=""
        }
        else{
            alert('삭제에 실패하였습니다.')
        }
    }).catch(error=>console.error(error))
})

search.addEventListener('click',function(){
    window.location.href='/board/main/search'
})