"""
if __name__ == "__main__":3 
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        output = []
        for j in range(n):
            output.append(a[(i + j) % n])
        print(*output)
"""
n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    print(*numbers) # 리스트의 원소들을 공백으로 구분하여 출력
    last_number = numbers.pop(0) # 리스트의 첫 번째 원소를 제거하고 그 값을 가져옴
    numbers.append(last_number) # 가져온 값을 리스트의 마지막에 추가

