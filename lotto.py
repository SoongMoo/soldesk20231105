import random
lotto = []
cnt = int(input("원하는 수량을 입력하세요. :"))
start = 1
while start <= cnt:
    i = 1   # 리스트와 반복문을 이용해서 로또프로그램
    while i <= 45:
        lotto.append(i)
        i += 1
    #print(lotto)
    size = len(lotto) # 45
    y = 1
    while y <= 6:
        size -= 1 # 44 , 43, 42, 41, 40, 39
        idx = random.randint(0, size)
        lottoNum = lotto.pop(idx)
        print(lottoNum, end=" ")
        y += 1
    print()
    lotto.clear()
    start += 1