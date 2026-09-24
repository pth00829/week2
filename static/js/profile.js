const searchParams=new URLSearchParams(window.location.search)
const user_id=searchParams.get('user_id')

const user_data=document.getElementById('user_data')
if(user_id){
    fetch(`/board/profile/get-data?user_id=${user_id}`)
    .then(res=>res.json())
    .then(data=>{
        const newP=document.createElement('p')
        const newH3=document.createElement('h3')
        const newImage=document.createElement('img')

        newImage.alt='USER'
        newImage.height=100
        newImage.width=100
        newImage.id='image_id'
        newH3.textContent='이름 : '+data.name
        newP.textContent='학교 : '+data.school
        user_data.appendChild(newImage)
        user_data.appendChild(newH3)
        user_data.appendChild(newP)
        if(data.success){
            if(data.image_exist){
                newImage.src='/static/uploads/'+data.image
                document.getElementById('edit_profile').style.display='block'
                document.getElementById('image_id').style.display='block'
            }
            else{
                document.getElementById('edit_profile').style.display='block'
                document.getElementById('image_id').style.display='none'
            }
        }
        else{
            if(data.image_exist){
                newImage.src='/static/uploads/'+data.image
                document.getElementById('edit_profile').style.display='none'
                document.getElementById('image_id').style.display='block'
            }
            else{
                document.getElementById('edit_profile').style.display='none'
                document.getElementById('image_id').style.display='none'
            }
        }
    })
}
else{
    fetch('/board/profile/get-data')
    .then(res=>res.json())
    .then(data=>{
        const newP=document.createElement('p')
        const newH3=document.createElement('h3')
        const newImage=document.createElement('img')

        
        newImage.alt='USER'
        newImage.height=100
        newImage.width=100
        newImage.id='image_id'
        newH3.textContent='이름 : '+data.name
        newP.textContent='학교 : '+data.school
        user_data.appendChild(newImage)
        user_data.appendChild(newH3)
        user_data.appendChild(newP)
        if(data.success){
            if(data.image_exist){
                newImage.src='/static/uploads/'+data.image
                document.getElementById('edit_profile').style.display='block'
                document.getElementById('image_id').style.display='block'
            }
            else{
                document.getElementById('edit_profile').style.display='block'
                document.getElementById('image_id').style.display='none'
            }
        }
        else{
            if(data.image_exist){
                newImage.src='/static/uploads/'+data.image
                document.getElementById('edit_profile').style.display='none'
                document.getElementById('image_id').style.display='block'
            }
            else{
                document.getElementById('edit_profile').style.display='none'
                document.getElementById('image_id').style.display='none'
            }
        }
    })
}


document.getElementById('edit_profile').addEventListener('click',function(){
    window.location.href='/board/profile/edit'
})

document.getElementById('')