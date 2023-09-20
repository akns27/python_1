"""
#문자열 출력포맷
print("a","b")
print("나는 %d살이야"%20)
print("나는 %s색과 %s색을 좋아해"%("파란", "빨강"))
print("나는 %s색 %s색을 좋아해" % ("파란", "빨강"))


print("나는 {}살 입니다".format(20))
print("난 {}색과 {}색을 좋아해요. ".format("파란", "빨강"))
print("난 {0}색과 {1}색을 좋아해요. ".format("파란", "빨강"))
print("난 {0}색과 {1}색을 좋아해요. ".format("파란", "빨강"))

#방법2
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨강"))
age = 20
color="RED"
print(f"나는 {age}살이며, {color}을/를 좋아해요")#format을 앞으로 뽑아내서 앞에 썼기에 f가 앞에 붙음
#_________________________
#함수의 정의

def 함수명():
  return

a =5
def func():
  global a#전체를 3으로 바꿈, 전역변수 a를 3으로 변경
  a =3
  return a

print(func())#func으로 들어가서 global a 적용
print(a)#a=3

def profile(name, age=17, language="python"):
  print("이름: {0}\t나이: {1}\t주사용언어: {2}".format(name,age,language))#\t는 탭을 뜻함

profile("박강원")
"""
def f(*a):#a 몇개를 넣을지 모르니 가변 인자 함수 *을 넣음
  print(type(a))
  return sum(a)
print(f(1,2,3,4,5))#튜플로 전달

