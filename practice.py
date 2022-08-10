#### 자료형 문자 ####

print("Hello")
print("w"*9)  # * 을 이용해 문자를 여러번 출력할 수도 있다.



#### boolean ####

print(5 > 10)
print(5 < 10)
print(True)
print(not True)
print(False)
print(not False)
print(not (5 > 10)) # True



##### 변수 #####

animal = "cat"
age = 3
name = "happy"
hobby = "nap"
is_adult = age >= 3

print("my " + animal + " name is " + name + " and " + str(age) +" years old")
print(name + "'s hobby is " + hobby)
print("name is" ,name, "and" ,age, "years old")
print("is " + name + " adult? " + str(is_adult))

# age 와 같은 숫자 타입과 is_adult 와 같은 boolean 타입을 + + 로 삽입하려면 str로 감싸야한다.
# "+ +" 대신 , , 로 삽입할 수도 있다. , ,을 이용해서 삽입할땐 띄어쓰기가 자동 포함된다.



#### 주석 ####

# 을 이용하면 한줄 주석처리
"""
큰 따움표를 3번씩 앞뒤로 적으면
전체 주석 처리
"""




#### 연산자 ####

print(1 + 1)
print(2 * 3)
print(2 ** 3)  # 2의 3제곱
print(6 % 2)   # 나머지 연산
print(6 // 2)  # 몫 연산

print(5 >= 10)      # False
print(5 <= 10)      # True
print(3 + 4 == 7)   # True

print(1 != 3)
print(not(1 != 3))

print((3 > 2) and (3 > 5)) # 둘다 만족해야 True 
print((3 > 2) & (3> 5)) # 위의 코드와 똑같음
print((3 > 1) or (3 > 5)) # 한쪽만 만족해도 True
print((3 > 1) | (3 > 5)) # 한쪽만 만족해도 True

print(3 < 5 < 7)  # True
print(3 < 6 < 4)  # False



#### 간단한 수식 ####

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4 # 14
print(number)

number += 2 # 16
print(number)

number *= 3 # 48
print(number)

number /= 3 # 16
print(number) # 16.0

number %= 3 
print(number) # 1.0



#### 숫자 처리 함수 ####

print(abs(-5))       # 절댓값 함수
print(abs(5))
print(pow(2,3))      # 2의 3제곱
print(max(2,10))     # 최댓값
print(min(3,8))      # 최솟값
print(round(3.14))   # 반올림
print(round(3.56))   # 4

from ast import Delete
from copyreg import constructor
from http.client import MOVED_PERMANENTLY
from itertools import count
from math import *
from ssl import _PasswordType
print(ceil(3.14))    # 올림 4
print(floor(3.14))   # 내림 3
print(sqrt(16))      # 제곱근 4.0




#### 랜덤 함수 ####

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성  /// int로 둘러싸면 정수로 출력가능
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성   // 46이하가 아닌 미만이다.

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성     // 45 미만이 아닌 이하이다.





#### 문자열 ####

sentence = "나는 소년입니다."
print(sentence)

sentence2 = '파이썬은 쉬워요.'
print(sentence2)

sentence3 = """         # """ """ 으로 감싸면 문장 전체를 출력할수있고 2줄이 아니라 위아래 공백을 한칸씩 추가하여 4줄이 출력된다.
나는 소년이고,
파이썬은 쉬워요
"""    
print(sentence3)    




#### 슬라이싱 ####

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0번째 인덱스부터 2번째 인덱스 전까지를 의미한다. (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # [:6] = 처음부터 6번째 인덱스 전까지를 의미한다.
print("뒤 7자리 : " + jumin[7:]) # [7:] = 7번째 인덱스부터 끝까지를 의미한다.
print("뒤 7자리(뒤에부터) : " + jumin[-7:]) # 맨뒤가 -1 인덱스 왼쪽으로 갈수록 -2,-3,-4,... 을 나타낸다.


#### 문자열 처리함수 ####
python = "Python is Amazing"
print(python.lower())                        # 소문자로 변경
print(python.upper())                        # 대문자로 변경
print(python[0].isupper())                   # 정해진 인덱스가 대문자인지 확인
print(len(python))                           # 문자열의 길이 반환
print(python.replace("Python", "Java"))      # 변경하고자 하는 부분 변경

index = python.index("n")                    # 찾는 문자의 인덱스값 반환
print(index)
index = python.index("n", index + 1)         # 찾고자 하는 문자의 첫번째 인덱스 다음부터 검색
print(index)

print(python.find("java"))                   # find 함수를 이용해서 찾을때 없을경우 -1 반환
print(python.index("java"))                  # index 함수를 이용해서 찾을때 없을경우 에러발생
print("hi")                                  # index 함수를 이용해서 에러가 발생하면 다음코드 실행 불가

print(python.count("n"))                     # 문자열에 찾고자 하는 문자의 개수를 반환




#### 문자열 포맷 ####

print("a" + "b")    # 기본적으로 사용가능한 방법
print("a", "b")     # 띄어쓰기를 포함해서 사용가능한 방법
# 위의 방법들 말고도 여러가지 방법들이 있다.

# 방법 1
print("나는 %d살 입니다." % 20)  # d는 정수값을 의미하므로 항상 정수값만을 넣을수 있다.
print("나는 %s을 좋아해요." % "파이썬") # s는 문자열(string)값을 넣어야한다.
print("Apple 은 %c로 시작해요" % "A") # c는 문자(char)값을 넣어야한다.

# %s 는 숫자, 문자열, 문자 모두 포함해서 사용할수 있다.
print("나는 %s살 입니다." % 20)  
print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))  # ("","")으로 두가지를 표현할 수도 있다.

# 방법 2 {} 와 .format() 이용
print("나는 {} 살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))   # 0 번째와 1번째를 서로 구분해서 알수있다
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))   # 0 번째와 1번째의 순서를 바꿀수 있다.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")





#### 탈출문자 ####

print("백문이 불여일견\n백견이 불여일타")

# 저는 "개발자" 입니다.
print("저는 "개발자" 입니다.") # SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('저는 "개발자" 입니다.') # 저는 "개발자" 입니다.
# \ 는 문자열 안에서 \다음에 오는 문자를 기호가 아닌 그냥 문자로 인식하게 한다.
print("저는 \"개발자\" 입니다.") # 저는 "개발자" 입니다.

# \\ : 문장 내에서 하나의 \ 로 바뀌게 된다.
print("Users\\Desktop\\PythonWorkspace\\tempCodeRunnerFile.py")  # Users\Desktop\PythonWorkspace\tempCodeRunnerFile.py

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple  커서를 맨앞으로 이동해서 'Red ' 부분에 'Pine'을 출력한다.

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red     Apple




# 비밀번호 생성 코드
copyPassWord = "http://naver.com"
index = copyPassWord.index(".")  
copyPassWord = copyPassWord[7:index]
stringNumber = len(copyPassWord)
e_count = copyPassWord.count('e')
copyPassWord = copyPassWord[:3]

print(f"{copyPassWord}{stringNumber}{e_count}" + "!")


# 풀이
url = "http://naver.com"
my_str = url.replace("http://" , "")
my_str = my_str[:my_str.index(".")]  
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))



#### 리스트 ####

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)  # [10, 20, 30]

subway = ['유재석', '조세호', '박명수']
print(subway);

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐 append를 이용해서 배열에 마지막에 추가할 수 있다.
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄  insert 를 하고 첫번째 인수에 삽입할 인덱스를 고르면 그 뒤로는 한칸씩 뒤로 밀리게 된다.
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄  pop 을 이용해서 배열에 맨뒤에 값을 삭제한다.
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인    count 를 이용해 배열에 같은 값이 몇개있는지 확인할 수 있다.
subway.append("유재석")
print(subway)
print(subway.count("유재석"))  


# 정렬도 가능하다.
num_list = [5,3,2,4,1]
num_list.sort()
print(num_list)  # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)  # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list)  # []


# 다양한 자료형 함께 사용
num_list = [5,3,2,4,1]
mix_list = ["조세호" , 20 , True]
print(mix_list)  # ['조세호', 20, True]

# 리스트 확장 서로 다른 리스트들을 합치는것이 가능하다.
num_list.extend(mix_list)
print(num_list)



#### 사전 ####
cabinet = {3:"유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 이때는 대괄호가 아닌 소괄호를 사용해서 구할 수 있다.

# print(cabinet[5])  # KeyError: 5     오류가 나면서 아랫줄에 hi 가 출력되지 않는다.
# print('hi')

print(cabinet.get(5))  # None    위에 대괄호를 이용했을때와는 달리 hi가 실행이 된다.
print('hi')            # hi

print(cabinet.get(5, "사용 가능"))   # 5라는 키값에 결과값이 없으면 "사용 가능" 이라는 값을 할당한다.
print('hi')

print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])    # 유재석
print(cabinet["B-100"])  # 김태호

# 새 손님
print(cabinet)   # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["C-20"] = "조세호"
print(cabinet)   # {'A-3': '유재석', 'B-100': '김태호', 'C-20': '조세호'}
cabinet["A-3"] = "김종국"
print(cabinet)   # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]
print(cabinet)   # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys())  # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 모든 값을 전부 지울때
cabinet.clear()
print(cabinet)  #  {}



#### 튜플 ####
# 튜플에서는 값을 변경 할 수 없다.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

menu.add("생선까스") # AttributeError: 'tuple' object has no attribute 'add' 

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)   # 김종국 20 코딩

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)   # 김종국 20 코딩





##### 세트 #####
# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)  # {'유재석'}
print(java.intersection(python))  # {'유재석'}

# 합집합 (java 나 python 둘중 하나라도 할수 있는 개발자)    순서는 보장되지 않는다.
print(java | python)  # {'박명수', '유재석', '양세형', '김태호'}
print(java.union(python))  # {'박명수', '유재석', '양세형', '김태호'}

# 차집합 (java는 할수 있지만 python은 할 수 없는 개발자)
print(java - python)  # {'양세형', '김태호'}
print(java.difference(python))  # {'김태호', '양세형'}

# pythone 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)   # {'박명수', '김태호', '유재석'}

# java를 잊어버림
java.remove("김태호")
print(java)  # {'유재석', '양세형'}




# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))   # {'커피', '우유', '주스'} <class 'set'>

menu = list(menu)
print(menu, type(menu))   # ['커피', '우유', '주스'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu))   # ('우유', '커피', '주스') <class 'tuple'>




# 퀴즈 5-6

import random
candidate = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(candidate)
candidate2 = (random.sample(candidate, 4))
print(candidate2)


print("-- 당첨자 발표 --")
print("치킨 당첨자 :{} " .format(candidate2[0]))
print("커피 당첨자 :[{},{},{}]".format((candidate2[1]), (candidate2[2]), (candidate2[3])))
print("-- 축하합니다 --")


# 풀이
from random import *
users = range(1,21) # 1부터 20까지 숫자를 생성
#print(type(users)) # <class 'range'>
users = list(users) # range 타입이던 user를 list 타입으로 변경시켜준다.
#print(type(users)) # <class 'list'>
shuffle(users)
#print(users) # 랜덤으로 재배치

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 :{0} " .format(winners[0]))
print("커피 당첨자 :{0}".format(winners[1:]))
print(" -- 축하합니다 -- ")






#### if ####
weather = "맑음"
# if 조건:
#     실행 명령문

if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")


# input은 사용자로부터 입력받은 문자를 string 데이터 형태로 변수에 저장한다.
weather = input("오늘 날씨는 어때요? ")   

if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")


temp = int(input("기온은 어때요?"))   # input은 항상 문자로 받기때문에 int로 감싸서 숫자 데이터타입으로 바꿔준다.
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨예요")
elif 0 <= temp < 10:                               # and가 없이 곧바로 비교를 해도 된다.
    print("외투를 챙기세요")
else: 
    print("추워요 나가지 마세요")





#### for ####
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")


# 뒤에 순서대로 처음에는 0이 waiting_no에 들어가고 그다음은 1, 그다음2, 그다음3, ... 차례대로 들어간다.
for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}" .format(waiting_no))


# 일정하게 증가할때는 range를 이용해서 더 편하게 작성할 수 있다.
for waiting_no in range(5):  # 0,1,2,3,4 까지 표현한다.
    print("대기번호 : {0}" .format(waiting_no))
    
# range(1, 6)처럼 시작값을 다르게 조절할 수 있다.
for waiting_no in range(1, 6):  # 1,2,3,4,5 까지 표현한다.
    print("대기번호 : {0}" .format(waiting_no)) 




starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0} , 커피가 준비되었습니다." .format(customer))






#### while ####
customer = "토르"
index = 5
while (index >= 1):
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분되었습니다.")

# 무한루프
customer = "아이언맨"
index = 1
while True :
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회.".format(customer, index))
    index += 1


# 탈출 조건을 포함한 무한루프
customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    



#### continue 와 break
absent = [2, 5]  # 결석
no_book = [7] # 책을 깜박했음
for students in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if students in absent:
        continue   
    elif students in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(students))
        break
    print("{0}, 책을 읽어봐".format(students))




#### 한줄 for ####
# 출석번호가 1 2 3 4 , 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1, 2, 3, 4, 5]
print(students) # [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students) # [101, 102, 103, 104, 105]

# 학생 이름을 길이로 변환
students = ['Iron man', 'Thor', 'I am groot']
students = [len(i) for i in students]
print(students)   # [8, 4, 10]

# 학생 이름을 대문자로 변환
students = ['Iron man', 'Thor', 'I am groot']
students = [i.upper() for i in students]
print(students)  # ['IRON MAN', 'THOR', 'I AM GROOT']



# 퀴즈 5
# 50명의 승객중에 탑승시간이 5분 ~ 15분 사이인 승객을 만날 경우의수 출력

from random import *
count = 0
for passenger in range(1, 51):
        time = randrange(5, 51)
        if 5 <= time <= 15 :
            print("[O] {0}번째 손님 (소요시간 : {1}분)". format(passenger, time))
            count += 1
        else:
            print("[ ] {0}번째 손님 (소요시간 : {1}분)". format(passenger, time))
        
print("총 탑승 승객 : {} 분".format(count))






#### 함수 ####
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


# 전달값과 반환값
def deposit(balance, money): # 입금
    print("임금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금에 실패하였습니다 잔액은 {0} 원입니다.".format(balance))
        return balance
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission # return 을 할때 , 를 이용해서 2개의 값을 반환할 수도 있다.


balance = 0 # 잔액
balance = deposit(balance, 10000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))



