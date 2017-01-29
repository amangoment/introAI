import random as rn

#values of rock, paper, scissors
r,p,s = 0,1,2
#dictionary e.g., rock beats scissors
ws = {r:s, p:r, s:p}

nogames = int(input("Number of games? "))

totgames = 0
compwins = 0
humwins = 0
ties = 0

gamehistory = []

while totgames < nogames:
     compMon = 100
     humMon = int(input("How much do you have?"))
     print("You have " + str(humMon))

     wager = min(compMon, humMon)

     compWag = rn.randrange(wager)
     humWag = int(input("Give a bet below " + str(wager) + ": "))
     print("Computer decides to bet: " + str(compWag))
     

     human = int(input("r=0,p=1,s=2 "))
     comp = rn.randrange(0,3,1)
     gamehistory.append([human, comp])

     print("Human: {0}, Comp: {1}".format(human, comp))


     if ws[comp] == human:
        compwins += 1
        compMon = compMon + humWag
        humMon = humMon - humWag
     elif ws[human] == comp:
        humwins += 1
        compMon = compMon - compWag
        humMon = humMon + compMon
     else:
        ties += 1
        compMon = compMon - compWag + ((compWag + humWag)/2)
        humMon = humMon - humWag + ((compWag+humWag)/2)
     totgames += 1

     print(compMon, humMon)

v = list(map(lambda x: 100*x/totgames, [compwins, humwins, ties]))
print("Stats\ncw% = {0}, hm% = {1}, ties% = {2}".format(*v))


