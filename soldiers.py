"""
a soldier wants to buy 'w' bananas in the shop. 
he has to pay 'k' for the first banana, 2k for the second one and so on.
he has 'n' dollars, how many dollars does he have to borrow from his friend
to buy w bananas?
"""

k, n, w = map(int, input().strip().split())

total_cost = 0

for i in range(1, w + 1):
	total_cost += i * k
	
borrow = total_cost - n
if borrow < 0:
	borrow = 0

print(borrow)

