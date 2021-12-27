while (True):
    n = input()  # 사용자 입력 받기

    flag = 0
    if n == "0":  # 0을 입력하였으면 종료
        break
    else:
        length = len(n)
        for i in range(length):
            if int(n[i]) - int(n[-(i+1)]) != 0:
                flag = 1
                break
    if flag == 0:
        print("yes")
    else:
        print("no")
