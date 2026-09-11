document.getElementById('login').addEventListener('submit',function(e) { // document.getElement('login)을 통해 form 태그를 불러오고 addEventListener('submit',function(e) {})를 통해 submit이라는 이벤트가 발생하면 함수 e를 실행한다.
    // e 함수에 대한 정의
    e.preventDefault(); // 이벤트의 기본 동작을 정지시킨다. submit의 경우 새로고침을 하며 데이터를 전송시키는 기본동작이 있는데 이를 멈춘다.
    const formData=new FormData(this) // formData라는 const 변수에 form 태그 속 입력값들을 모두 받아온다. this의 역할이 입력값들을 모두 가져오는 것이다.

    fetch('/login',{ // url은 유지한채로
        method:"POST", // method를 POST로 보내고
        body:formData // 내용은 formData의 전송이다.
    }) // 이후 Promise라는 객체를 받아와 대기하다가(시간이 걸리는 비동기 작업의 결과가 나오면 전달해준다는 약속을 하는 객체)
    .then(res=>res.json()) // 결과가 나오면 받아와서 화살표 함수를 실행한다. json으로 변경 .then은 응답이 오기만 한다면 실행되고 그 응답이 error 코드인 404,500 같은거여도 .then이 받는다
    .then(data=>{ // 위의 .then의 결과를 받아온다. json을 받아서 data에 저장하고
        if(data.success) { // json 속 success의 값을 이용하여 if문 실행
            window.location.href='/login/success' // JavaScript에서 url을 이동할 때 사용
        }
        else { 
            alert(data.message)
        }
    })
    .catch(error=>console.error('에러 : ',error)) // Promise에서 에러가 발생하면 .catch가 에러 객체를 수신해 콘솔에 기록한다. .catch는 네트워크 자체가 끊겨서 응답자체를 못받으면 실행되는것.
})