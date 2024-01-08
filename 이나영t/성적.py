class grade:
   def __init__(self, name, score):#틀만 만들어 주기/__init__ 초기화, 생성자 역활
    self.name = name
    self.score = score
   def s_grade(self):
      if self.score >= 90:#꼭 self 붙여주기
         self.grade="A"

      elif self.score >= 80:
         self.grade="B"

      else:
         self.grade="C"

   def __str__(self):
      return "%s: %c등급" %(self.name, self.grade)
   
a1 = grade("박강원", 88)#이 매개변수들을 넣어줌
a1.s_grade()#메서드 호출
print(a1)#프린트