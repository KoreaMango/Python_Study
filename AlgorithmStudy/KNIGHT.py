s = input()
# 'UUR', 'UUL', 'LLU', 'LLD', 'DDL', 'DDR', 'RRU', 'RRD'
# (x, y)
move_type = [(1, -2), (-1, -2), (-2, -1), (-2, 1),
             (-1, 2), (1, 2), (2, -1), (2, 1)]

row = int(ord(s[0]) - 96)
col = int(s[1])
count = 0

for i in range(len(move_type)):
    nx = move_type[i][0]
    ny = move_type[i][1]
    if row + nx > 0 and col + ny > 0 and row + nx <= 8 and col + ny <= 8:
        count += 1

print(count)
