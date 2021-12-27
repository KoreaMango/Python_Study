while (True):
    n = input()  # 사용자 입력 받기

    flag = 0
    if n == "0":  # 0을 입력하였으면 종료
        break
    else:  # 아니면 계속 실행
        for i in range(len(n)):  # 길이 만큼 길행
            if int(n[i]) - int(n[-(i+1)]) != 0:  # 다르면 0이 아니기 때문에 실패 플래그 설정
                flag = 1
                break  # 반복문 종료
    if flag == 0:  # 실패 플래그가 0이면 yes
        print("yes")
    else:  # 실패 플래그가 1이면 no
        print("no")
