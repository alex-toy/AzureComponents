
with open('data/us_accidents_short.csv', 'w') as output:
    fp = open("data/us_accidents.csv")
    for i, line in enumerate(fp):
        if i in range(0, 100000) : output.write(line)   
    fp.close()

