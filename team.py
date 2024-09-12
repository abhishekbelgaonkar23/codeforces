"""
three friends make a team and take aprt in progamming contests. 
if two of them are sure about a solution, then they implement it,
else, they dont.
"""

n = int(input())

count = 0

for _ in range(n):
	opinions = input().split()
	p = int(opinions[0])
	v = int(opinions[1])
	t = int(opinions[2])
	if p + v + t >= 2:
		count += 1
print(count)
