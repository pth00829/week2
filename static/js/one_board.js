const searchParams=new URLSearchParams(window.location.search)
const board_id=searchParams.get('board_id')
const look_board=document.getElementById('look_board')

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

                    newH2.textContent=data.title
                    newSpan.textContent=data.content
                    look_board.appendChild(newH2)
                    look_board.appendChild(newSpan)
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

            newH2.textContent=data.title
            newSpan.textContent=data.content
            look_board.appendChild(newH2)
            look_board.appendChild(newSpan)
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