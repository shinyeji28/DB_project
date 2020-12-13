<!DOCTYPE html>
<html>
    <body>
  
        {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul class=flashes>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
        {% endwith %}

        <form method = 'POST'>
        <p>인원수를 선택하세요</p>
        <a>어린이&nbsp;&nbsp;</a><select name = "child" id = "child_p">
            <option value = "0">0명</option>
            <option value = "1">1명</option>
            <option value = "2">2명</option>
            <option value = "3">3명</option>
            <option value = "4">4명</option>
            <option value = "5">5명</option>
            <option value = "6">6명</option>
            <option value = "7">7명</option>
            <option value = "8">8명</option>
            <option value = "9">9명</option>
            <option value = "10">10명</option>
        </select><br><br>
        <a>청소년&nbsp;&nbsp;</a><select name = "teen" id = "teen_p">
            <option value = "0">0명</option>
            <option value = "1">1명</option>
            <option value = "2">2명</option>
            <option value = "3">3명</option>
            <option value = "4">4명</option>
            <option value = "5">5명</option>
            <option value = "6">6명</option>
            <option value = "7">7명</option>
            <option value = "8">8명</option>
            <option value = "9">9명</option>
            <option value = "10">10명</option>
        </select><br><br>
        <a>성인&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a><select name = "adult" id = "adult_p">
            <option value = "0">0명</option>
            <option value = "1">1명</option>
            <option value = "2">2명</option>
            <option value = "3">3명</option>
            <option value = "4">4명</option>
            <option value = "5">5명</option>
            <option value = "6">6명</option>
            <option value = "7">7명</option>
            <option value = "8">8명</option>
            <option value = "9">9명</option>
            <option value = "10">10명</option>
        </select><br><br>
        <p>티켓 수령 방법</p>
        <input type = "radio" name = "ticket" value = "0" checked>현장 수령
        <input type = "radio" name = "ticket" value = "2800">배송(2,800원)
        
        <p>예매자 확인</p>
        {% for i in userInfo %}
        <a>이름 : </a>{{i.uName}}<br>
        생년월일 : <input type = text name = "birth" value = "예) 991111">
        <a>(생년월일이 일치하지 않을 시 예매가 불가합니다.)</a><br>
        <a>연락처 : </a>{{i.phoneNumber}}<br>
        <a>이메일 : </a>{{i.eMail}}<br>
        {% endfor %}

        <input type = 'submit'  value = '조회하기' onkeyup='aa'>        


        <p>총 결제 금액 : </p>{{results}}
        <input type = 'submit'  value = '예매하기' formaction="{{url_for('reserve_accepct',ID8=ID7,e=eID)}}">
        
        

        
        </form>
    </body>
</html>
