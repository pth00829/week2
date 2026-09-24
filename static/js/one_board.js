const searchParams=new URLSearchParams(window.location.search)
const board_id=searchParams.get('board_id')
const look_board=document.getElementById('look_board')

const formData=new FormData()
formData.append('board_id',board_id)
fetch('/board/check',{
    method:'post',
    body:formData
})
.then(res=>res.json())
.then(data=>{
    if(data.success){
        document.getElementById('update_btn').style.display='block'
        document.getElementById('delete_btn').style.display='block'
    }
    else{
        document.getElementById('update_btn').style.display='none'
        document.getElementById('delete_btn').style.display='none'
    }
})

fetch(`/board/main/correction/data?board_id=${board_id}`)
.then(res=>res.json())
.then(data=>{
    if(data.success){
        if(data.secret===1){
            document.getElementById('look_board').style.display='none'
            document.getElementById('btn_div').style.display='none'
            document.getElementById('secret_btn').addEventListener('click',function(){
                if(document.getElementById('input_pw').value===data.secret_pw){
                    document.getElementById('look_board').style.display='block'
                    document.getElementById('pw_div').style.display='none'
                    document.getElementById('btn_div').style.display='block'
                    const newH2=document.createElement('h2')
                    const newSpan=document.createElement('span')
                    const newP=document.createElement('p')
                    const newA=document.createElement('a')
                    const text="작성자 : "

                    newP.textContent=text
                    newA.textContent=data.user_id
                    newA.href=`/board/profile?user_id=${data.user_id}`
                    newH2.textContent=data.title
                    newSpan.textContent=data.content
                    newP.appendChild(newA)
                    look_board.appendChild(newP)
                    look_board.appendChild(newH2)
                    look_board.appendChild(newSpan)
                    
                    if(data.file_name){
                        const newA=document.createElement('a')
                        const newBr=document.createElement('br')
                        newA.href='./uploads/'+data.file_name
                        newA.download=data.file_name
                        newA.textContent=data.file_name
                        look_board.appendChild(newBr)
                        look_board.appendChild(newA)
                    }
                }
                else{
                    alert('비밀번호가 틀렸습니다.')
                }
            })
        }
        else{
            document.getElementById('pw_div').style.display='none'
            const newH2=document.createElement('h2')
            const newSpan=document.createElement('span')
            const newP=document.createElement('p')
            const newA=document.createElement('a')
            const text="작성자 : "

            newP.textContent=text
            newA.textContent=data.user_id
            newA.href=`/board/profile?user_id=${data.user_id}`

            newH2.textContent=data.title
            newSpan.textContent=data.content
            newP.appendChild(newA)
            look_board.appendChild(newP)
            look_board.appendChild(newH2)
            look_board.appendChild(newSpan)
            
            if(data.file_name){
                const newA=document.createElement('a')
                const newBr=document.createElement('br')
                newA.href='./uploads/'+data.file_name
                newA.download=data.file_name
                newA.textContent=data.file_name
                look_board.appendChild(newBr)
                look_board.appendChild(newA)
            }
        }
    }
    else{
        alert('데이터 불러오기 실패')
    }
}).catch(err=>console.error(err))

document.getElementById('update_btn').addEventListener('click',function(){
    
    const url=new URL('/board/main/correction',window.location.origin)
    url.searchParams.append('board_id',board_id)
    window.location.href=url
    
})

document.getElementById('delete_btn').addEventListener('click',function(){
    const url=new URL('/board/main/delete',window.location.origin)
    url.searchParams.append('board_id',board_id)

    fetch(url)
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            alert('삭제하였습니다')
            window.location.href='/board/main'
        }
        else{
            alert('삭제에 실패하였습니다.')
        }
    })
})

document.getElementById('return_main').addEventListener('click',function(){
    window.location.href='/board/main'
})

