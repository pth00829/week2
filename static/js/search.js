const search=document.getElementById('search')
search.addEventListener('submit',function(e){
    e.preventDefault();
    const formData=new FormData(this)

    fetch('/board/main/search',{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            const value=document.getElementById('value')
            value.innerHTML=''
            for(let i=0; i<data.data.length; i++){
                const myP = document.createElement('p')
                const myH1 = document.createElement('h1')
                const mySpan = document.createElement('span')

                myH1.textContent = 'Title : '+data.data[i][0]
                mySpan.textContent = 'Content : '+data.data[i][1]

                myP.appendChild(myH1)
                myP.appendChild(mySpan)
                value.appendChild(myP)
            }
        }
        else{
            const value=document.getElementById('value')
            value.innerHTML=''
            alert(data.message)
        }
    })
})

document.getElementById('finish').addEventListener('click',function(){
    window.location.href='/board/main'
})