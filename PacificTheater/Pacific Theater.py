from gamelib import *

game = Game(1600, 825, "Pacific Theater")

usscv = Image("images\\yorktown.png", game)
ijncv = Image("images\\hiryu.png", game)
ijncv.rotateBy(270)
ijncv.resizeBy(-30)
ijncv.moveTo(1470, 420)
Banzai = Sound("sound\\Banzai.wav", 1)
F6F = Image("images\\F6FHellcat.png", game)
JapZero = Image("images\\JapZero.png", game)
Bullet = Animation("images\\Bullet.png", 1, game, 768, 1024)
Bullet.resizeBy(-95)
Bullet.rotateTo(90)
Bullet.visible = False
Explosion = Animation("images\\explosion.png", 22, game, 57, 64)
Explosion.visible = False
StartScreen = Image("images\\Cover.png", game)
StartScreen.resizeTo(1600, 825)
WinScreen = Image("images\\WinScreen.png", game)
WinScreen.resizeTo(1600, 825)
Instruction = Image("images\\Instructions.png", game)
Instruction.resizeTo(1600, 825)
BkSound = Sound("sound\\Samurai.wav", 2)

usscv.moveTo(90, 420)
usscv.rotateBy(90)
usscv.resizeBy(-5)

F6F.resizeBy(-60)
F6F.rotateBy(180)
F6F.moveTo(usscv.x, usscv.y - 250)

bk2 = Image("images\\Ocean.jpg", game)
bk2.resizeTo(game.width, game.height)

game.setBackground(StartScreen)
StartScreen.draw()

game.update()
game.wait(K_SPACE)

game.setBackground(Instruction)
Instruction.draw()
game.update()
game.wait(K_DOWN)
game.update()

game.setBackground(bk2)
bk2.draw()
game.update()

JapZero = []
for times in range(20):
    JapZero.append( Image("images\\JapZero.png", game) )

for j in JapZero:
    x = randint(2000, 3000)
    y = randint(100, 700)
    s = randint(1, 3)
    j.moveTo(x,y)
    j.rotateBy(-90)
    j.setSpeed(s)
    j.resizeBy(-70)

Banzai.play()

KillCount = 0

Bullet.visible = False
    
while not game.over:
    game.processInput()
    game.drawBackground()

    BkSound.play()

    for j in JapZero:
        j.move()

    usscv.draw()
    Bullet.move()
    F6F.move()
    Explosion.draw(False)

    if keys.Pressed[K_UP]:
        F6F.forward(2)
    else:
        F6F.speed *= 0.99

    if keys.Pressed[K_RIGHT]:
        F6F.rotateBy(2, "right")

    if keys.Pressed[K_LEFT]:
        F6F.rotateBy(2, "left")
        
    for j in JapZero:
        if j.collidedWith(F6F):
            F6F.health -= 10
            Explosion.moveTo(j.x, j.y)
            Explosion.visible = True
            j.visible = False
            KillCount += 1

    usscv.draw()
    F6F.move()
    Bullet.draw()
    
    for j in JapZero:
        j.move()

    if F6F.health <1:
        game.over = True

    for j in JapZero:
        if j.collidedWith(usscv,"rectangle"):
            usscv.health -= 10
            Explosion.moveTo(j.x, j.y)
            Explosion.visible = True
            j.visible = False
            KillCount += 1

    if usscv.health <1:
        game.over = True
      
    if keys.Pressed[K_SPACE]:
        Bullet.visible = True
        Bullet.moveTo(F6F.x, F6F.y)
        Bullet.setSpeed(10, F6F.getAngle(180))
        Bullet.rotateTo(F6F.getAngle())
        
    for j in JapZero:
        if Bullet.collidedWith(j):
            Explosion.moveTo(j.x, j.y)
            Explosion.visible = True
            j.visible = False
            KillCount += 1

    if KillCount >19:
        bk2.draw()
        
    if KillCount <20:
        game.drawText("F6F Grumman Health " + str(F6F.health), 200, 5)
        game.drawText("USS Yorktown Health " + str(usscv.health), 200, 30)
        game.drawText("Zero Planes Destroyed " + str(KillCount), 200, 55)
 
    if game.over is True:
        game.quit()

    if KillCount <20 and game.over is False:
        game.over = False
        
    if game.over is False and KillCount >19 and usscv.health >0 and F6F.health >0:
        game.over = True

    game.update(60)

MidScreen = Image("images\\MidScreen.png", game)
MidScreen.resizeTo(1600, 825)
MidScreen.draw()
game.update()
game.wait(K_DOWN)
game.update()
bk2 = Image("images\\Ocean.jpg", game)
bk2.resizeTo(game.width, game.height)
game.setBackground(bk2)
bk2.draw()
game.update()
ijncv.draw()
game.update(60)
game.over = False
KillCount = 0
F6F.health = 125
ijncv.health = 250
F6F.moveTo(100, 420)

for times in range(50):
    JapZero.append( Image("images\\JapZero.png", game) )

for j in JapZero:
    x = randint(1600, 2500)
    y = randint(100, 700)
    s = randint(1, 3)
    j.moveTo(x,y)
    j.rotateBy(-90)
    j.setSpeed(s)
    j.resizeBy(-70)

Bullet.visible = False

while not game.over:
    game.processInput()
    game.drawBackground()

    BkSound.play()

    ijncv.draw()
    F6F.move()
    Bullet.move()

    for j in JapZero:
        j.move()
    
    if keys.Pressed[K_UP]:
        F6F.forward(2)
    else:
        F6F.speed *= 0.99

    if keys.Pressed[K_RIGHT]:
        F6F.rotateBy(1, "right")

    if keys.Pressed[K_LEFT]:
        F6F.rotateBy(1, "left")

    if keys.Pressed[K_SPACE]:
        Bullet.visible = True
        Bullet.moveTo(F6F.x, F6F.y)
        Bullet.setSpeed(5, F6F.getAngle(180))
        Bullet.rotateTo(F6F.getAngle())
 
    if Bullet.isOffScreen():
        Bullet.visible = False
    
    if Bullet.collidedWith(ijncv, "rectangular") or Bullet.x > 1470 and Bullet.visible is True:
        Explosion.moveTo(Bullet.x, Bullet.y)
        Explosion.visible = True
        Bullet.visible = False
        ijncv.health -= 10

    if F6F.collidedWith(ijncv):
        game.over = True

    if F6F.x >1450:
        game.over = True

    if ijncv.health <1:
        game.over = True

    for j in JapZero:
        if j.collidedWith(F6F):
            j.visible = False
            F6F.health -= 10
            KillCount += 1

        if Bullet.collidedWith(j):
            j.visible = False
            KillCount += 1
            Explosion.moveTo(j.x, j.y)
            Explosion.visible = True

        if j.isOffScreen("left"):
            x = randint(1600, 2200)
            y = randint(100, 700)
            s = randint(1, 3)
            j.moveTo(x,y)
            j.setSpeed(s)

        if F6F.health <1:
            game.over = True

        if F6F.health >1 and ijncv.health <1:
            game.update()
            game.wait(K_SPACE)
            game.over = True

    game.drawText("IJN Hiryu Health " + str(ijncv.health), 200, 5)
    game.drawText("F6F Grumman " + str(F6F.health), 200, 30)
    game.drawText("Zero Planes Destroyed " + str(KillCount), 200, 55)
    game.update(120)
game.quit()

#When 1st game loop starts, bullet is auto-fired once
#Start screen, transition screen from game 1 -> game 2, end/credits/controls screen
#Mid-screen transition doesn't work
