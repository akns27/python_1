"""
#파이썬의 형(int, float...)

print("I'm a string")
print(type(28))

#1byte= 8bit, 1byte는 -128~127까지의 수 표현 가능
#b = 2, O = 8, x=10진수, 0x=16진스

print(.4e7)
type(.4e7)
4.2e-4

print(type('true'))
#bin() = int를 2진수로
#float() = 실수형으로
#hex() = 10진수 
#oct() = 8진수
#str() = 문자열




list

변수명 = [값1, 값2...]
변수명 = list(문자형 자료 또는 범위 및 자료)
type에 구애받지 않음

a[2]+str[3]
=> 문자열로 나옴
a[1]*3 + a[2]
a[1] 3개 출력 + a[2]

a[1:3]
3 앞에서 끊김 실제로는 1~ 2까지

list를 수정하려면 a[0] = "hello"
list안에 list를 넣을 수 있음
지울때는 del 사용 ex) a[0], del[0:2]

append를 이용해서 값을 추가할 수 있음
#a.append는 a = []에 삽입할 수 있는 코드

b_list=[]
b_list.append(1)
b_list.append(2)
b_list.append(3)
print(b_list)


c_list=[1,2,"hello",[1,2,3]]
print(c_list)



리스트는 가변이지만 튜플은 불변

#tuple
a = (1,2,3)
print(type(a))
b = 1, 2, 3
print(type(b))

a=[1, "가", 2, "나"]
b= tuple(a)
print(b)

c = tuple(range(1,15,2))
print()

#튜플은 수정, 삭제 안됨

a = (1,2,3,4,5,6)
print(3 in a)#3이 a에 안 들어있음 = > true
print(3 not in a)#3이 a에 안 들어있음 = > false
print(a.count(3))#3이 튜플안에 몇개 들어있는가
print(a.count(5))#5가 튜플안에 몇개 들어있는가




#set, 순서와 중복 없이 저장된 자료형 a= {1, 2, ,7, 4, 3}

#합집합 : a|b => a.union(b)
#교집합 : a&b => a.intersection(b)
#차집합 : a-b => a.difference(b)
#대칭차집합 : a^b =>  a.symmetric_difference(b), 합집합에서 교집합을 뺀 것


#dictionary{key:value}

#key는 변경이 불가능(=튜플), value는 변경가능[list]

#b[(key)], b[(1,"가")]

a = {1: "A"}
print(a[1])
a[2] = "second"
print(a[2])

print(a)
del a[2] 
print(a)

del는 그냥 없애는 거고
pop은 지우고 반환
"""

