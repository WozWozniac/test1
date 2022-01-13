#변수명은 알파벳으로 시작, 대소문자를 구분하며,
#사용할 수 없음 중강에 띄어쓰기 금지
#변수는 데이터를 쉽게 할 수 있도록 해야함
#예약어(Reserved Word) = keyword : print(x)를 사용할 수 없음
#print1(o) printNumber(o)
#printNumber(o) : 카멜 방식, 단어를 읽기 쉽도록 단어부터
# 첫글자를 대문자로 표기하는 방식 -> printNumberCaption
#print_number(o) : 언더스코어 방식, 단어마다 중간 어더스코어를(_)
#를 넣는다
#예약어를 출력
#식별자(Identifiers) : 변수, 클래스, 모듈, 함수
import keyword
print(keyword.kwlist)
