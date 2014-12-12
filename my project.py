print "The Most Amazing Story Ever"
print "You are a young man traveling to meet someone in Massachussets"
print "right as you start walking away from your home, you come to a fork in the road. One path is littered with lollipops and reeks of happiness. The other has mud and smells of onions. Which path do you take? Press Q for candy path. Press W for muddy path."
userchoice = raw_input()
userchoice2 = ""
if userchoice == "q":
    print "You decide to play it safe and take the candy path. You find a mountain of lollipops and gorge yourself on lollipops. Congragulations: You have achieved diabetes. Play again?"
if userchoice == "w":
    print "You little risk taker you. You embark down the path. After a while, you realize you have in fact ventured into a swamp."
    print "The ground begins to rumble. The pungent smell of onions fills the air. You hear a mighty roar as the ground begins to rumble. Press E to stay and fight the unknown being or R to run."
userchoice2 = raw_input()
if userchoice2 == "r":
    print "You do the smart thing and run away. You trip over an... onion? You can barely see as a green hand covers your face and you get your last glimpse of sunlight. Play again?"
if userchoice2 == "e":
    print "You decide to be a little cheeky bloke and stay to fight whatever being you are up against."
print "The trees in front of you are crumbling. Suddenly a being pops out. You make eye contact and he screams 'WHAT ARE YE DOIN IN MAH SWAMP??!!! That's right. It's Shrek."
print "ENGAGE BOSS BATTLE" 
print "sponsored by mountain dew"
import random
shrekhealth = 100
playerhealth = 100   
magic = random.randint(1,30)
shrekattack = random.randint(1,20)
while(playerhealth > 0 and shrekhealth > 0):
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Press 1 to punch"
    print "Press 2 for a running kick"
    print "Press 3 for Magic Gamble"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    attack = raw_input()
    if attack == "1":
        print "Shrek's health is now"
        shrekhealth = shrekhealth - 10
        print shrekhealth
    elif attack == "2":
        print "Shrek's health is now"
        shrekhealth = shrekhealth - 10 
        print shrekhealth
    elif attack == "3":
        print "Shrek's health is now"
        shrekhealth = shrekhealth - magic
        print shrekhealth
    print "Shrek uses his mighty fists to attack! Your health is now"
    playerhealth = playerhealth - shrekattack
    print playerhealth
    if playerhealth < 1:
        print "Your time here is ogre. Play again?"
    if shrekhealth < 1:
        print "You have defeated Shrek! This is your swamp now!"
        print "You walk for 10 more minutes until you venture out of that wretched swamp."
        print "You find a car that looks like it has been there for years. You really need to get Massachussets, so you decide to give the car a try, although there can't possibly be any gasa left."
        print "You get in the car and start it. The engine runs 'WHAT??!!' you think. 'This isn't The Walking Dead' but you ignore the oddity and begin driving."
        print "You have been driving for about an hour and two signs appear. You can turn left to go through Pennsylvania or right to go through Washington D.C. Where do you turn?"
        print "Press T to take a left or press Y to take a right."
userchoice3 = raw_input()
if userchoice3 == "t":
    print "You decide to drive through Pennsylvania. You drive and drive and drive. You've been driving for hours now, and you're wondering how you're still in the state"
    print "You pass the same sign you passed an hour ago. What's going on? Suddenly it strikes you. Pennsylvania has captured you with how boring it is. There is no escape. Play Again?"
if userchoice3 == "y":
    print "You decide to drive through Washington D.C. After about an hour you begin to drive by majestic monuments such as the Lincoln Memorial and the Washington Monument"
    print "As you are passing the White House, your car decides that it is time to be cliche and randomly run out of gas. Amazing."
    print "You notice as you look around that nobody is on the streets. Peculiar for such a city."
    print "You hear music coming from the White House. You recognize it instantly. Its the Cory In The House theme song."
    print "Cory himself blasts out of the White House straight towards you. Time for another fight!"
    print "BOSS BATTLE 2 ENGAGE"
    print "Sponsored by FaZe clan and Doritos"
coryhealth = 105
playerhealth2 = 100
randomnumber2 = random.randint(1,30)
while(playerhealth > 0 and coryhealth > 0):
  print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
  print "Press 4 for upgraded punch"
  print "Press 5 for Steel Sword"
  print "Press 6 for Magic Gamble"
  print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
  attack2 = raw_input()
  if attack2 == "4":
    coryhealth = coryhealth - 10
    print "Cory's health is now"
    print coryhealth
    print "Your health is now"
    playerhealth2 = playerhealth2 - shrekattack
    print playerhealth
  if attack2 == "5":
     coryhealth = coryhealth - 15
     print "Cory's health is now"
     coryhealth = coryhealth - 20
     print coryhealth
     print "Your health is now"
     playerhealth2 = playerhealth2 - shrekattack
     print playerhealth2
  if attack2 == "6":
    coryhealth = coryhealth - magic
    playerhealth2 = playerhealth2 - shrekattack
    print "Cory's health is now"
    print coryhealth
    print "Your health is now"
    print playerhealth2
  if playerhealth2 < 1:
    print "Of course, you were no match for almighty Cory. Cory smirks as he walks away from your body. Play Again?"
  if coryhealth < 1:
    print "Somehow you defeated Cory. That should be impossible, but you're just glad you made it out alive."
print "After finding another car, you finally arrive in Massachussets. The man you are meeting is waiting with other shady men. You get out of the car."
print "You walk over to the man... It is none other than Supa Hot Fire! The men hanging around him are his hype gang."
print "This is it. The moment you've been waiting for. Supa Hot challenges you to a rap battle. Press u to stay and rap. Press I to run away."
playerchoice = raw_input()
if playerchoice == "i":
    print "You're not yet ready to battle such a big figure as Supa Hot. You turn around and leave, as Supa Hot claims his 300000000001st victory."
    print "You get in your car and drive home. You are disappointed you could not bring pride back to your town. A tear streams down your face as you drive home."
    print "The End"
    print "Battle Supa Hot for a better ending."
if playerchoice == "u":
    print "Of course you stay to rap. You are ready. Supa Hot is ready. Lets go!"
supahealth = 150
playerhealth3 = 110
while(playerhealth > 0 and supahealth > 0):
  print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
  print "Press 7 for Thunderpunch"
  print "Press 8 for Steel Sword"
  print "Press 9 for Max Magic"
  print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
  attack3 = raw_input()  
  if attack3 == "7":
     print "You punch supa hot (how dare you) His health is now"
     supahealth = supahealth - 15
     print supahealth
     print "Supa Hot spits some mad verses. Your health is now"
     playerhealth3 = playerhealth3 - shrekattack
  if attack3 == "8":
     print "You swing your sword at Supa Hot. His health is now"
     supahealth = supahealth - 20
     print supahealth
     print "Supa Hot spits some mad verses. Your health is now"
     playerhealth3 = playerhealth3 - shrekattack
     print playerhealth
  if attack3 == "9":
     print "You charge your intense magic and fire at Supa Hot. His health is now."
     supahealth = supahealth - magic
     print supahealth
     print "Supa Hot spits some mad verses. Your health is now"
     playerhealth3 = playerhealth3 - shrekattack
     print playerhealth3
  if playerhealth3 < 1:
     print "It was obvious you couldn't beat Supa Hot from the beginning. Your eyes slowly close as your journey comes to its end."
     print "The End"
     print "Defeat Supa Hot for a better ending."
  if supahealth < 1:
     print "It is done. You are unbelievable. You have just broken Supa Hot's 3000000 winning streak. His hype gang is in awe. Supa Hot falls. You are the victor."
     print "You get back in your car and drive back home. You know you have brought pride back to your city. You drive past Corys body. You pass by Shreks body. You smile. You drive into the sunset, back to your home."
     print "The End"
     print "Congragulations. You found the best ending."
    
    
    
  
