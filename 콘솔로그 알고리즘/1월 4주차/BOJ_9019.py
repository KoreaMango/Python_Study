import sys

# 땅 면적, 인벤토리 개수 입력받기
N, M, B = map(int, sys.stdin.readline().split())

# 2차원 배열로 리스트 입력받기
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 타임 무한으로 설정, 높이 0으로 설정
time, height = 1e9, 0

# 높이 256까지 반복
for h in range(257):
    # bot, top 0 으로 설정
    bot = top = 0
    # 2차원 배열 반복
    for i in range(N):
        for j in range(M):
            # 높이가 낮은 블럭들은
            if li[i][j] < h:
                # 아래에 더해줌, 높이에 해당 블록 높이를 뺌 = 차이
                bot += h-li[i][j]
            else: # 높이가 높거나 같은 블럭은
                # 해당 블록 높이에서 현재 높이를 뺌 = 차이
                top += li[i][j]-h
                
    # 인벤토리에서 꺼내줄 수 없으면 코드 종료하고 다시 반복
    # 아래 코드 실행하지 않음
    if bot > top + B:
        continue

    t = bot + top*2
    
    if t <= time:
        time = t
        height = h
        
print(time, height)
