
class FishCakeMaker:
  def __init__(self, **kwargs):#어떤 parameter값이 들어갈 줄 모르니 가변인자 매개변수를 씀
    self.size=10
    self.flavor="팥"
    self.price=100

    if "size" in kwargs:
      self.size=kwargs.get("size")#keyword arguments 딕셔니리 안에 size라는 key값이 있나? 있다면 가져와서 size변수에 대임
    if "flavor" in kwargs:
      self.flavor=kwargs.get("flavor")
    if "price" in kwargs:
      self.price=kwargs.get("price")
    
  def show(self):
    print("붕어빵 크기 {}".format(self.size))
    print("붕어빵 종류 {}".format(self.flavor))
    print("붕어빵 가격 {}".format(self.price))
    print("*"*30)

fish1 = FishCakeMaker()
fish2 = FishCakeMaker(size = 20, price = 300)#**는 ** 형식으로 key: value값을 전달해줘서 딕셔너리
fish3 = FishCakeMaker(flavor = "초콜렛", size = "15", price = 400)

fish1.show()
fish2.show()
fish3.show()

