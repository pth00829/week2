const board=document.getElementById('board')
const value=document.getElementById('value')

fetch('/board/')
.then(res=>res.json())
.then(data=>{
    if(data.success){
        for(let i=0; i<data.data.length; i++){
            const myLabel=document.createElement('label')
            const myH2=document.createElement('h2')
            const myRadio=document.createElement('input')

            myRadio.type='radio'
            myRadio.value=data.data[i][0]
            myRadio.name='boardId'
            myRadio.id='radio_id'

            myH2.textContent=data.data[i][1]
            myLabel.appendChild(myRadio)
            myLabel.appendChild(myH2)
            board.appendChild(myLabel)
        }
    }
    else{
        board.textContent="저장된 게시글이 없습니다."
    }
}).catch(err=>console.error(err))

document.getElementById('new_board').addEventListener('click',function(){
    window.location.href='/board/main/create'
})

const search=document.getElementById('search')

search.addEventListener('submit',function(a){
    a.preventDefault()

    const formData=new FormData(this)

    fetch('/board/main/search',{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            value.innerHTML=''
            board.innerHTML=''
            for(let i=0; i<data.data.length; i++){
                const newSpan=document.createElement('Span')
                const newH1=document.createElement('h1')
                const newLabel=document.createElement('label')
                const newRadio=document.createElement('input')
                const newBr=document.createElement('br')
                newRadio.type='radio'
                newRadio.name='boardId'
                newRadio.id='board_id'
                newRadio.value=data.data[i][0]

                newH1.textContent=data.data[i][1]
                newSpan.textContent=data.data[i][2]

                newLabel.appendChild(newRadio)
                newLabel.appendChild(newH1)
                newLabel.appendChild(newSpan)
                newLabel.appendChild(newBr)
                value.appendChild(newLabel)
            }
        }
        else{
            value.innerHTML=''
            alert(data.message)
        }
    }).catch(err=>console.error(err))
})

document.getElementById('finish').addEventListener('click',function(f){
    value.innerHTML=''
    board.innerHTML=''
    fetch('/board/')
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            for(let i=0; i<data.data.length; i++){
                const myLabel=document.createElement('label')
                const myH2=document.createElement('h2')
                const myRadio=document.createElement('input')

                myRadio.type='radio'
                myRadio.value=data.data[i][0]
                myRadio.name='boardId'
                myRadio.id='radio_id'

                myH2.textContent=data.data[i][1]
                myLabel.appendChild(myRadio)
                myLabel.appendChild(myH2)
                board.appendChild(myLabel)
            }
        }
        else{
            board.textContent="저장된 게시글이 없습니다."
        }
    }).catch(err=>console.error(err))
})

document.getElementById('look').addEventListener('click',function(a){
    a.preventDefault()

    const checked=document.querySelector('input[name="boardId"]:checked')

    if(checked){
        const board_id=checked.value
        const url=new URL('/board/look',window.location.origin)

        url.searchParams.append('board_id',board_id)
        window.location.href=url
    }
    else{
        alert('게시글을 선택해주세요.')
    }
})

document.getElementById('logout_btn').addEventListener('click',function(){
    window.location.href='/user/logout'
})

document.getElementById('delete_user').addEventListener('click',function(a) {
    window.location.href='/user/secession'
})

document.getElementById('profile').addEventListener('click',function(){
    window.location.href='/board/profile'
})