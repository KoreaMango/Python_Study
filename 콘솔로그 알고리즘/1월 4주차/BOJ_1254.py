s = input()

# 문자열의 길이만큼 반복함
for i in range(len(s)):
    # 문자열과 뒤집은 문자열이 같으면 문자열의 길이 + 앞으로 이동한 인덱스를 더함
    # 앞에 사라진 문자만큼 뒤에 붙여주면 되니까 그 수만큼 붙임
    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break
