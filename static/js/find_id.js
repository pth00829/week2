const show_data=document.getElementById('show_data')
document.getElementById('find_user').addEventListener('submit',function(e){
    e.preventDefault()

    const formData=new FormData(this)

    fetch('/user/find/id',{
        method:'post',
        body:formData
    })
    .then(res=>res.json())
    .then(data=>{
        if(data.success){
            show_data.innerHTML=''
            for(let i=0; i<data.data.length; i++){
                const newP=document.createElement('p')

                newP.textContent=data.data[i][0]
                show_data.appendChild(newP)
                alert(data.data[i][0])
            }
        }
    })
})