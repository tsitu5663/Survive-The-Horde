from gamelib import *

game=Game(1000,800,"SURVIVE THE HORDE")
startscreen=Image("Game_Project//start_screen.jpg",game)
startscreen.resizeTo(game.width,game.height)
startscreen.draw()
game.drawText("SURVIVE THE HORDE",100,100,Font(red,100,green,))
game.drawText("PRESS SPACE TO SEE THE TUTORIAL",500,500,Font(yellow,25,green,))
game.update()
game.wait(K_SPACE)
game.drawText("HOW TO PLAY:",100,300)
game.drawText("A to move LEFT   D to move RIGHT   SPACE to JUMP",100,350)
game.drawText("U to use MELEE ATTACK   I to use CRESENT SLASH",100,400)
game.drawText("O to clear the screen   P to FIRE THE LAZER!!!!",100,450)
game.drawText("SURVIVE UNTIL THE TIME REACH 10000",100,500)
game.drawText("PRESS UP TO START",100,550)
game.drawText("MADE BY WEEB KINGDOM",100,650,Font(yellow,100,green,))
game.update()
game.wait(K_UP)
game.setMusic("Game_project_sound//background_music.wav")
endscreen=Animation("Game_Project//endscreen.png",103,game,3675/7,3300/15,1)
endscreen.resizeTo(game.width,game.height)
victory_end=Animation("Game_Project//victory_end.png",10,game,780/2,1100/5,2)
victory_end.resizeTo(game.width,game.height)
platform=Image("Game_Project//platform2.png",game)
platform.resizeBy(100)
platform.moveTo(500,625)
hero=Animation("Game_Project//hero.png",4,game,384/2,464/2,3)
hero.resizeBy(-10)
hero.moveTo(300,450)
hero.stop()
finisher=Animation("Game_Project//finisher.png",10,game,884/2,1200/5,3)
finisher.resizeTo(game.width,game.height)
bk=Animation("Game_Project//sky.png",25,game,2000/4,2016/7,150)
bk.resizeTo(game.width,game.height)


zambie=[]
for times in range(250):
    zambie.append( Animation("Game_Project\\zambie.png",19,game,200,200,) )

for z in zambie:
    x = randint(1000,4000)
    s = randint(2,5)
    z.moveTo(x,500)
    z.setSpeed(s,90)
    
giantzambie=[]
for times in range(25):
    giantzambie.append( Animation("Game_Project\\giantzambie.png",12,game,2000/4,1761/3,5) )

for g in giantzambie:
    b = randint(1500,3000)
    a = randint(1,2)
    g.moveTo(x,300)
    g.setSpeed(a,90)
    
victory=Sound("Game_project_sound\\epic_sax_guy.wav",1)
energy=Sound("Game_project_sound\\energy.wav",2)
bite=Sound("Game_project_sound\\Bite-Sound.wav",3)
failure=Sound("Game_project_sound\\hell.wav",4)
delete=Sound("Game_project_sound\\yasuo-ult-sound-1.wav",5)
boom=Sound("Game_project_sound\\boom.wav",6)
victorylogo=Image("Game_Project//victory.png",game)
victorylogo.resizeBy(-30)
castle=Image("Game_Project\\castle.png",game)
castle.moveTo(100,400)
castle.resizeBy(10)
heroattack1=Animation("Game_Project//hero_swipeattack.png",7,game,560/2,752/4,2)
heroattack1.resizeBy(-10)
heroattack1.stop
heroattack2=Animation("Game_Project//hero_slashattack.png",7,game,560/2,848/4,2)
heroattack2.resizeBy(-10)
heroattack2.stop
rangedslash=Image("Game_Project//rangedslash.png",game)
rangedslash.resizeBy(-35)
rangedslash.visible=False
srangedslash=Image("Game_Project//superrangedslash.png",game)
srangedslash.resizeBy(-35)
srangedslash.visible=False
archer=Animation("Game_Project//archer.png",30,game,640/5,768/6,2)
archer.resizeBy(150)
archer.moveTo(150,250)
archer.stop()
energywave=Animation("Game_Project//energywave.png",10,game,705/1,840/10,2)
energywave.resizeTo(game.width,game.height-200)
energywave.stop()
jumping = False #Used to check to see if you are jumping
landed = False #Used to check to see if you have landed on the ground
factor = 1 #Used for a slowing effect of the jumping

rangedslash.setSpeed(20,-90)
srangedslash.setSpeed(30,-90)
heroattack1.visible=False
heroattack2.visible=False
g.health=500
castle.health=1000

game.playMusic()
while not game.over:
    
    
    game.processInput()
    bk.nextFrame()
    game.displayTime(600,5,)
    game.time+=1
    rangedslash.move()
    platform.draw()
    castle.draw()
        
  
    #Player Controls
    if keys.Pressed[K_a]:
        hero.nextFrame()
        hero.x -= 10
    elif keys.Pressed[K_d]:
        hero.prevFrame()
        hero.x+=10
    else:
        hero.draw()
        
    if keys.Pressed[K_u]:
        heroattack1.visible=True
        hero.visible=False
        heroattack1.moveTo(hero.x,hero.y)
       
    elif keys.Pressed[K_i]:
        heroattack2.visible=True
        hero.visible=False
        heroattack2.moveTo(hero.x,hero.y)
        hero.nextFrame()
        rangedslash.moveTo(hero.x+50,hero.y)
        rangedslash.visible=True
        game.score-=25
        
    else:
        hero.visible=True
        
    if keys.Pressed[K_p]:
        game.score-=10
        archer.visible=True
        energywave.moveTo(archer.x+700,archer.y)
        archer.nextFrame()
        energywave.nextFrame()
        energy.play()
    else:
        archer.draw()
   
    rangedslash.move()
    srangedslash.move()
    for g in giantzambie:
            g.move()
            if g.collidedWith(hero):
                hero.health-=20
                g.moveTo(b,300)
            if g.collidedWith(energywave) and g.x<900:
               g.moveTo(b,300)
            if g.health<100:
                g.moveTo(b,300)
            if g.collidedWith(castle):
                castle.health-=150
                g.moveTo(b,300)
                
    for z in zambie:
        z.move()
        if z.collidedWith(hero):
            hero.health-=5
            bite.play()
            z.moveTo(x,500)
        if rangedslash.collidedWith(z):
            z.damage+=100
        if srangedslash.collidedWith(z):
            z.moveTo(x,500)
        if z.damage>200:
            z.moveTo(x,500)
            z.move()
        if heroattack1.collidedWith(z):
            z.damage+=5
            game.score+=5
        if z.collidedWith(castle):
            castle.health-=100
            z.moveTo(x,500)
       
           
        
    if hero.collidedWith(castle) and hero.x<100: 
        hero.moveTo(150,350)
    if rangedslash.isOffScreen("right"):
        rangedslash.visible=False
    if srangedslash.isOffScreen("right"):
        srangedslash.visible=False
    if game.score>500:
        z.health+=100
    
   
    
    heroattack1.visible=False
    heroattack2.visible=False
     
     
    if keys.Pressed[K_o]:
        game.score-25
        srangedslash.moveTo(hero.x+50,hero.y)
        srangedslash.visible=True
        finisher.nextFrame()
        delete.play()
        boom.play()
        
  
        

    #Jumping Logic    
    if hero.y < 500:
        landed = False
        if hero.collidedWith(castle) and hero.y<450:
            landed=True
        #300 is the floor.  Decision can be replaced with a more complex condition based on game
    else:
        landed = True
        
    if jumping:
        hero.y -= 30 * factor
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor *= .95
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if keys.Pressed[K_SPACE] and landed and not jumping:
            #If you landed on the floor and are not jumping and press the SpaceBar then jump
            jumping = True
            
    if not landed:
        hero.y += 9
        #If you haven't landed then you are in the air, so you should fall.
    if castle.health<100 or hero.health<10:
        game.stopMusic()
        failure.play()
        endscreen.nextFrame()
    if game.time>10000:
        game.stopMusic()
        victory_end.nextFrame()
        victory.play()
        victorylogo.draw()
    game.displayScore()
    game.displayTime(600,5,)    
    game.drawText("Health: " + str(hero.health),200,5)
    game.drawText("Castle Health: " + str(castle.health),400,5)
    
    
    game.update(100)
game.quit()

