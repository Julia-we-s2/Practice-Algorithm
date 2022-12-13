n = int(input())
round = 1
nums_pileup = 1

while n > nums_pileup:
    nums_pileup += 6 * round
    round += 1

print(round)
