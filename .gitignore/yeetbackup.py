#time to start again

#importing the stuff we need
import sys
import time
import random
import YeetFunctions



#intro
print('FillFire')
time.sleep(.25)
print('        _____________         ____________')
time.sleep(.25)
print('        |                           |            |               |')
time.sleep(.25)
print('        |                           |            |               |')
time.sleep(.25)
print('        |                           |            |               |')
time.sleep(.25)
print('        |_________                  |            |               |')
time.sleep(.25)
print('        |                           |            |               |')
time.sleep(.25)
print('        |                           |            |               |')
time.sleep(.25)
print('        |                           |            |               |')
time.sleep(.25)
print('        |                     ______|_____       |_________      |__________')
time.sleep(.25)
print('')
time.sleep(.25)
print('        _____________         ____________      ___________      ___________')
time.sleep(.25)
print('        |                           |            |         |     |')
time.sleep(.25)
print('        |                           |            |         |     |')
time.sleep(.25)
print('        |_________                  |            |         |     |______')
time.sleep(.25)
print('        |                           |            |_________|     |')
time.sleep(.25)
print('        |                           |            |\              |')
time.sleep(.25)
print('        |                           |            | \             |')
time.sleep(.25)
print('        |                     ______|_____       |  \            |__________')
time.sleep(.5)
      
#defining some functions and variables
enHealth = 10
enType = 'teacher'
enWepDam = 2
turn = 'play'
playHealth = 10
playWepDam = 3
playWepType = ''
healLevel = 1
playChoice = ''
wri = 'Collin Young'
cous = 'Python 3.7.0/3.7.1'
fou1 = 'Dakota Countryman'
fou2 = 'Emmet Ruighainri'

def playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice):
        if playChoice == 'Attack':
                enHealth =  enHealth - playWepDam
                return enHealth
        elif playChoice == 'Heal':
                playHealth = playHealth + 2
                while playHealth > 10:
                        playHealth = playHealth - 1
                return playHealth
        elif playChoice == 'Pass':
                print('You Do Nothing')
        else:
                print('INVALID COMMAND')
        #add more options later

def enChoice(enHealth, enType):
        if enType == 'teacher':
                if enHealth >= 9:
                        mode = 'attack'
                        return mode
                elif enHealth < 9 and enHealth >= 3:
                        a = random.randint(1,10)
                        if a < 4:
                                mode = 'heal'
                                return mode
                        elif a >= 4:
                                mode = 'attack'
                                return mode
                elif enHealth <= 2:
                        mode = 'heal'
                        return mode
        if enType == 'brother/sister':
                if enHealth >= 10:
                        mode = 'attack'
                        return mode
                elif enHealth < 10 and enHealth >=3:
                        x = random.randint(1,100)
                        if x <= 15:
                                mode = 'heal'
                                return mode
                        elif x > 15:
                                mode = 'attack'
                                return mode
                elif enHealth < 3:
                        mode = 'heal'
                        return mode

def turNum(turn):
        if turn == 'play':
                print('It is your turn')
        elif turn == 'en':
                print('It is the enemy\'s turn')

def stats(enHealth, playHealth):
        print('Enemy Health: ' + str(enHealth))
        print('Your Health: ' + str(playHealth))

# now to write the exposition!

input('press enter to continue')
print('You Wake Up...')
time.sleep(1)
print('You look at the faded trees in front of you...')
time.sleep(1)
print('A russle, from the bushes...')
time.sleep(1)
print('Your Brother jumps from the bushes, brandishing a stick!')
time.sleep(1)
print('You grab a sitck of your own...')
input('press enter to continue')






#enHealth = 10
#enType = 'teacher'
#enWepDam = 2
#turn = 'play'
#playHealth = 10
#playWepDam = 3
#playWepType = ''
#healLevel = 1
#playChoice = ''
#Combat time

print('\033[1;31;40mYou Have Entered Combat')

while enHealth > 0:

#------------------------------------------------------------------------------------------------#

        if playHealth <= 0:
                print('You Have Died')
                YeetFunctions.credits(wri, cous, fou1, fou2)

#------------------------------------------------------------------------------------------------#
                
        turNum(turn)
        time.sleep(.5)
        print('What do you wish to do: Attack, Heal, or Pass')
        playChoice = input('>>> ')
        if playChoice == 'Attack':
                enHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
        elif playChoice == 'Heal':
                playHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
        elif playChoice == 'Pass':
                playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
        elif playChoice == 'Exit':
                sys.exit()
        time.sleep(.5)
        stats(enHealth, playHealth)
        time.sleep(.5)

#-------------------------------------------------------------------------------------------------#        

        if enHealth <= 0:
                break

#-------------------------------------------------------------------------------------------------#

        turn = 'en'
        turNum(turn)
        time.sleep(.5)
        mode = enChoice(enHealth, enType)
        print('They chose to ' + mode)
        time.sleep(.5)
        if mode == 'attack':
                playHealth = playHealth - enWepDam
        elif mode == 'heal':
                enHealth = enHealth + 2
        stats(enHealth, playHealth)

#-------------------------------------------------------------------------------------------------#

print('You Won')
input('enter to continue...')
print('Your Brother lies before you, bloodied by your savegery...')
print('His stcik is larger than yours')
print('Do you wish to take his stick [Attack], or to take his food [Health]...')
i = input('>>> ')
if i == 'Attack':
        playWepDam = playWepDam + 5
elif i == 'Health':
        while playHealth < 10:
                playHealth = playHealth + 1
        playHealth = playHealth + 5
print('your new stats are ' + str(playHealth) + ' for your health and ' + str(playWepDam) + ' for your damage')
input('enter to continue...')
print('You Walk, fueled by the bloodlust, and you see a helpless newborn, laying apon the ground...')
time.sleep(1)
print('It crys...')
time.sleep(1)
print('What do you wish to do?')
time.sleep(.1)
print('Attack, Give Food, Take, Leave')
baby = input('>>> ')
if baby == 'Attack':
        print('The baby grows, and sprouts horns of  bone...')
        time.sleep(1)
        print('It looks at you...')
        time.sleep(1)
        print('It says: ')
        time.sleep(1)
        print('Goo?')
        time.sleep(1)
        print('GAME OVER')
        time.sleep(2)
        YeetFunctions.credits(wri, cous, fou1, fou2)
elif baby == 'Give Food':
        print('It grows, and a deep voice rumbles:')
        time.sleep(.5)
        print('I thank you, and grant you this weapon')
        time.sleep(.5)
        print('+ 1 Death Blade Of Countrymen')
        time.sleep(.5)
        playWepDam = 100
        print('your new stats are ' + str(playHealth) + ' for your health and ' + str(playWepDam) + ' for your damage')
elif baby == 'Take':
        print('As you walk away, the red tinge arund your eyes grows less...')
        time.sleep(.5)
        print('You are bout 700ft away, when you hear a warbleing cry:')
        time.sleep(.75)
        print('Someone has taken him, our lord... our god!')
        time.sleep(.5)
        print('A man jumps out from the bushes...')
        time.sleep(.5)
        print('He draws his sword...')
        time.sleep(.2)
        print('it is of steel, his armour is leather.')
        input('enter to continue')
        print('You have entered combat!')

        enHealth = 20
        enType = 'brother/sister'
        enWepDam = 6
        turn = 'play'
        healLevel = 1
        playChoice = ''
        enRem = 4

        while enRem > 0:
                while enHealth > 0:

                        if playHealth <= 0:
                                print('You Loose...')
                                time.sleep(.9)
                                print('As you fall to the ground, you close your eyes...')
                                time.sleep(3.25)
                                YeetFunctions.credits(wri, cous, fou1, fou2)

#------------------------------------------------------------------------------------------------#
                
                        turNum(turn)
                        time.sleep(.5)
                        print('What do you wish to do: Attack, Heal, or Pass')
                        playChoice = input('>>> ')
                        if playChoice == 'Attack':
                                enHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Heal':
                                playHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Pass':
                                playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Exit':
                                sys.exit()
                        elif playChoice == 'Escape':
                                enRem = -12.3456789
                                if enRem == -12.3456789:
                                        break
                        time.sleep(.5)
                        stats(enHealth, playHealth)
                        time.sleep(.5)

#-------------------------------------------------------------------------------------------------#        


#-------------------------------------------------------------------------------------------------#

                        turn = 'en'
                        turNum(turn)
                        time.sleep(.5)
                        mode = enChoice(enHealth, enType)
                        print('They chose to ' + mode)
                        time.sleep(.5)
                        if mode == 'attack':
                                playHealth = playHealth - enWepDam
                        elif mode == 'heal':
                                enHealth = enHealth + 2
                        stats(enHealth, playHealth)

#-------------------------------------------------------------------------------------------------#
        
                if enRem == -12.3456789:
                        break
                print('You Won')
                input('enter to continue...')

                print('A woman appears, holding a poison stick...')


                enHealth = 20
                enType = 'brother/sister'
                enWepDam = 6
                turn = 'play'
                healLevel = 1
                playChoice = ''
                enRem = 4

                tN = 0
                while enHealth > 0:

                        if tN > 0:
                                playHealth = playHealth - tN
                                tN = tN + 1
                                print('Poison!!!')
                                stats(enHealth, playHealth)
                        
                        if playHealth <= 0:
                                print('You Loose...')
                                time.sleep(.9)
                                print('As you fall to the ground, you close your eyes...')
                                time.sleep(3.25)
                                YeetFunctions.credits(wri, cous, fou1, fou2)

#------------------------------------------------------------------------------------------------#
                
                        turNum(turn)
                        time.sleep(.5)
                        print('What do you wish to do: Attack, Heal, or Pass')
                        playChoice = input('>>> ')
                        if playChoice == 'Attack':
                                enHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Heal':
                                playHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Pass':
                                playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Exit':
                                sys.exit()
                        time.sleep(.5)
                        stats(enHealth, playHealth)
                        time.sleep(.5)

#-------------------------------------------------------------------------------------------------#        


#-------------------------------------------------------------------------------------------------#

                        turn = 'en'
                        turNum(turn)
                        time.sleep(.5)
                        mode = enChoice(enHealth, enType)
                        print('They chose to ' + mode)
                        time.sleep(.5)
                        if mode == 'attack':
                                playHealth = playHealth - enWepDam
                        elif mode == 'heal':
                                enHealth = enHealth + 2
                        stats(enHealth, playHealth)
                print('You Won!')
                input('enter to continue...')
                print('She lies on th ground...')
                time.sleep(.5)
                print('You look down and see an amulet...')
                time.sleep(.5)
                print('You cannot tell what it does...')
                w = input('Do you take it...\nYes [Y] or No [N]\n>>> ')
                if w.lower() == 'y':
                        amu = 'y'
                        print('You pick it up...')
                elif w.lower() == 'n':
                        amu = 'n'
                        print('You pass by...')
                time.sleep(.5)
                print('running, you see another man step out of the bushes...')
                time.sleep(.5)
                print('He draws his sword...')
                time.sleep(.2)
                print('it is of steel, his armour is leather.')
                input('enter to continue')
                print('You have entered combat!')

                while enHealth > 0:

                        if playHealth <= 0:
                                print('You Loose...')
                                time.sleep(.9)
                                print('As you fall to the ground, you close your eyes...')
                                time.sleep(3.25)
                                YeetFunctions.credits(wri, cous, fou1, fou2)

#------------------------------------------------------------------------------------------------#
                
                        turNum(turn)
                        time.sleep(.5)
                        print('What do you wish to do: Attack, Heal, or Pass')
                        playChoice = input('>>> ')
                        if playChoice == 'Attack':
                                enHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Heal':
                                playHealth = playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Pass':
                                playTurn(playHealth, playWepType, playWepDam, enHealth, enWepDam, playChoice)
                        elif playChoice == 'Exit':
                                sys.exit()
                        time.sleep(.5)
                        stats(enHealth, playHealth)
                        time.sleep(.5)        


#-------------------------------------------------------------------------------------------------#

                        turn = 'en'
                        turNum(turn)
                        time.sleep(.5)
                        mode = enChoice(enHealth, enType)
                        print('They chose to ' + mode)
                        time.sleep(.5)
                        if mode == 'attack':
                                playHealth = playHealth - enWepDam
                        elif mode == 'heal':
                                enHealth = enHealth + 2
                        stats(enHealth, playHealth)

                print('You Won!')
                input('enter to continue...')
                break
                
                

        if enRem == -12.3456789:
                print('You Dodge His blade and push your way into the bushes...')
                time.sleep(.5)
                print('You run, and he trips over a log...')
                time.sleep(.5)
                print('You slip, and tumble into a creek...')
                time.sleep(.25)
                c = input('A log...\nOver [O] or Under [U]\n')
                if c.upper() == 'U':
                        print('you shred your back')
                        print('GAME OVER')
                        time.sleep(4)
                        YeetFunctions.credits(wri, cous, fou1, fou2)
                elif c.upper == 'O':
                        print('You Vault the log...')
                        time.sleep(.5)
                        print('A fork in the path...')
                        time.sleep(.25)
                        print('Which Way? Left [L] or right [R]')
                        c = input('>>> ')
                        if c.upper() == 'L':
                                print('you fell off a cliff...')
                                print('GAME OVER')
                                time.sleep(4)
                                YeetFunctions.credits(wri, cous, fou1, fou2)
                        elif c.upper() == 'R':
                                pritn('i')
        elif enRem != -12.3456789:
                print('You Are A Hacker If You Survived That!')
                time.sleep(1)
                print('die')
                sys.exit()

elif baby == 'Leave':
        print('You leave the baby, and walk away...')























        

        
