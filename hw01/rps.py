import random as rn

#values of rock, paper, scissors
r,p,s = 0,1,2
#dictionary e.g., rock beats scissors
ws = {r:s, p:r, s:p}

nogames = int(input("Number of games? "))

totgames = 0
compwins = 0
robbywins = 0
ties = 0

gamehistory = []

while totgames < nogames:
     robby = rn.randrange(0,2)
     comp = rn.randrange(0,3,1)
     gamehistory.append([robby, comp])

     print("Robby: {0}, Comp: {1}".format(robby, comp))

     if ws[comp] == robby:
        compwins += 1
     elif ws[robby] == comp:
        robbywins += 1
     else:
        ties += 1
     totgames += 1

v = list(map(lambda x: 100*x/totgames, [compwins, robbywins, ties]))
print("Stats\ncw% = {0}, rm% = {1}, ties% = {2}".format(*v))

