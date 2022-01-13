a = 254.195   #실수
b = "456"     #문자열
# 형변환 : 특정타입(종류)에서 다른 종류의 타입으로 바뀌는 것
print(a, type(a), int(a),type(int(a)))     #실수 -> 정수
print(b, type(b), int(b),type(int(b)))     #문자열 -> 정수
c = 23     #정수
d = "True" #문자열
print(c, type(c), float(c), type(float(c))) #정수 -> 실수
print(d, type(d), bool(d), type(bool(d)))   #문자열 -> 논리
print(c, type(c), str(c), type(str(c)))     #숫자 -> 문자열
e = "나나나"
# print(e, type(e), int(e), float(e), bool(e))
# e는 데이터가 원래 문자열이며, 다른 형으로 병형이 불가하므로 형변환을 할 수 없음
# 형변환(Casting)