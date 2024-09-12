x = int(input().strip())
complete_steps = x // 5
remainder = x % 5

if remainder > 0:
    complete_steps += 1

print(complete_steps)
