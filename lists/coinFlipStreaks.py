import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            results.append('H')
        else: 
            results.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    coinString = ''.join(results)
    if 'HHHHHH' in coinString or 'TTTTTT' in coinString:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))