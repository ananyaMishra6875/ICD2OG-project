#imports
import pygame
from pygame import mixer

# initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# load bgm audio and configure
mixer.music.load("ssbMainMenu.mp3")
mixer.music.set_volume(1)

# screen resolution etc.
HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
opacitySurface = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA) # https://youtu.be/8_HVdxBqJmE?feature=shared
pygame.display.set_caption("Brawl Blitz: Arena Mayhem")

# colours
OPACITY = 240
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
LIGHT_YELLOW = (255,242,204)
YELLOW = (255,218,110)
OTHER_YELLOW = (252,227,18)
RED = (136,0,21)
BRIGHTER_RED = (233,30,52)
DARK_GREY = (160,160,160)
LIGHT_GREY = (240,240,240)
GREY_LOW_OPACTITY = (30,30,30,OPACITY)
OTHER_GREY = (210,210,210)
GREEN = (74,215,23)

# sprite variables
SPRITE_Y = 520
spriteS = 128
spriteX1 = WIDTH - (2)*(spriteS)
spriteY1 = HEIGHT - spriteS - 80
spriteX2 = spriteS
spriteY2 = HEIGHT - spriteS - 80
distanceNum = 16
fill = 0
bigS = 300
p1nn = ""
p2nn = ""
winner = p1nn
canType1 = False
canType2 = False
xFlip1 = True
xFlip2 = False
selectedSprite1 = 0
selectedSprite2 = 1
hp1 = 100
hp2 = 100
canPunch1 = False
canPunch2 = False

# other variables
jumping = False
jumping2 = False
GRAVITY = 1
GRAVITY2 = 1
fallGravity = 8
jumpH = 26
jumpH2 = 26
jumpSpeed = jumpH
jumpSpeed2 = jumpH2 # https://youtu.be/ST-Qq3WBZBE?feature=shared
window = 0
windows = [0,1,2,3,4]
xCoord1,yCoord1,xCoord2,yCoord2,xCoord3,xCoord4 = 124,330,259,520,206,606
xCoord,yCoord = xCoord1,yCoord1
x2Coord,y2Coord = xCoord2,yCoord1
x3Coord = xCoord3
coords = [xCoord1,xCoord2,yCoord1,yCoord2,xCoord3,xCoord4]
boxS = 16
boxX1 = WIDTH - (4+10)*(boxS)
boxX2 = (4)*(boxS)
boxY = HEIGHT - (2)*(boxS)
countdown = True
countdownNum = 3

# clock
clock = pygame.time.Clock()
fps = 30

# load graphics 
bg1 = pygame.image.load("titleScreenWithoutFIGHT.png")
bg2 = pygame.image.load("boxingRinkyDink.png")
bg3 = pygame.image.load("coliseumBonk.png")
bg4 = pygame.image.load("otherScreens.png")
bg5 = pygame.image.load("brawlBlitzScreeenWithFire.png")
theLogo = pygame.image.load("brawlBlitzLogo.png")
theFIGHT = pygame.image.load("FIGHT.png")
s1 = pygame.image.load("sprite1.png")
s2 = pygame.image.load("sprite2.png")
s3 = pygame.image.load("sprite3.png")
s4 = pygame.image.load("sprite4.png")
punch1 = pygame.image.load("sprite1punch.png")
punch2 = pygame.image.load("sprite2punch.png")
punch3 = pygame.image.load("sprite3punch.png")
punch4 = pygame.image.load("sprite4punch.png")

# transform graphics 
bg = pygame.transform.scale(bg1,(WIDTH,HEIGHT))
otherBg = pygame.transform.scale(bg4,(WIDTH,HEIGHT))
lastBg = pygame.transform.scale(bg5,(WIDTH,HEIGHT))
boxing = pygame.transform.scale(bg2,(WIDTH,HEIGHT))
smallBoxing = pygame.transform.scale(bg2,(230,173))
coliseum = pygame.transform.scale(bg3,(WIDTH,HEIGHT))
smallColiseum = pygame.transform.scale(bg3,(230,173))
stage = boxing

logo = pygame.transform.scale(theLogo,(550,425))
fight = pygame.transform.scale(theFIGHT,(150,78))

sprite1 = pygame.transform.scale(s1,(spriteS,spriteS))
sprite1big = pygame.transform.scale(sprite1,(bigS,bigS))
sprite1punch = pygame.transform.scale(punch1,(spriteS,spriteS))
sprite2 = pygame.transform.scale(s2,(spriteS,spriteS))
sprite2big = pygame.transform.scale(sprite2,(bigS,bigS))
sprite2punch = pygame.transform.scale(punch2,(spriteS,spriteS))
sprite3 = pygame.transform.scale(s3,(spriteS,spriteS))
sprite3big = pygame.transform.scale(sprite3,(bigS,bigS))
sprite3punch = pygame.transform.scale(punch3,(spriteS,spriteS))
sprite4 = pygame.transform.scale(s4,(spriteS,spriteS))
sprite4big = pygame.transform.scale(sprite4,(bigS,bigS))
sprite4punch = pygame.transform.scale(punch4,(spriteS,spriteS))
bigSprites = [sprite1big,sprite2big,sprite3big,sprite4big]
selected1 = bigSprites[0]
selected2 = bigSprites[1]

# text etc. 
enterName1 = "click to enter a name"
enterName2 = "click to enter a name"
titleFont = pygame.font.Font("Silkscreen-Regular.ttf",35)
otherFont = pygame.font.Font("Silkscreen-Regular.ttf",15)
otherFont2 = pygame.font.Font("Silkscreen-Regular.ttf",30)
text1 = titleFont.render("Choose your fighter: (1)",True,LIGHT_YELLOW)
text2 = titleFont.render("Choose your fighter: (2)",True,LIGHT_YELLOW)
text3 = titleFont.render("Choose the fighting stage:",True,LIGHT_YELLOW)
text4 = otherFont.render(enterName1,True,BLACK)
text5 = otherFont.render(enterName2,True,BLACK)
text7 = otherFont.render("Return to title screen",True,WHITE)
text8 = otherFont.render("Return to fighter selection screen",True,WHITE)
text9 = otherFont.render("Return to stage selection screen",True,WHITE)
text10 = otherFont2.render("FIGHT!",True,LIGHT_YELLOW)

# functions ---------------------------------------------------------------------------------------
def xSpriteCollision():
  if (abs(spriteX1 - spriteX2) <= spriteS-30) and (abs(spriteY1 - spriteY2) <= spriteS):
    return True
  else:
    return False

def ySpriteCollision():
  if (abs(spriteX1 - spriteX2) <= spriteS-30) and (abs(spriteY1 - spriteY2) <= spriteS):
    return True
  else:
    return False

def spriteStuffs():
  sprite1facing1 = pygame.transform.flip(sprite1,xFlip1,False)
  sprite1facing2 = pygame.transform.flip(sprite1,xFlip2,False)
  sprite1punchfacing1 = pygame.transform.flip(sprite1punch,xFlip1,False)
  sprite1punchfacing2 = pygame.transform.flip(sprite1punch,xFlip2,False)
  sprite2facing1 = pygame.transform.flip(sprite2,xFlip1,False)
  sprite2facing2 = pygame.transform.flip(sprite2,xFlip2,False)
  sprite2punchfacing1 = pygame.transform.flip(sprite2punch,xFlip1,False)
  sprite2punchfacing2 = pygame.transform.flip(sprite2punch,xFlip2,False)
  sprite3facing1 = pygame.transform.flip(sprite3,xFlip1,False)
  sprite3facing2 = pygame.transform.flip(sprite3,xFlip2,False)
  sprite3punchfacing1 = pygame.transform.flip(sprite3punch,xFlip1,False)
  sprite3punchfacing2 = pygame.transform.flip(sprite3punch,xFlip2,False)
  sprite4facing1 = pygame.transform.flip(sprite4,xFlip1,False)
  sprite4facing2 = pygame.transform.flip(sprite4,xFlip2,False)
  sprite4punchfacing1 = pygame.transform.flip(sprite4punch,xFlip1,False)
  sprite4punchfacing2 = pygame.transform.flip(sprite4punch,xFlip2,False)
  global sprites1,sprites2,sprites1punch,sprites2punch,chosenPunch1,chosenPunch2
  sprites1 = [sprite1facing1,sprite2facing1,sprite3facing1,sprite4facing1]
  sprites2 = [sprite1facing2,sprite2facing2,sprite3facing2,sprite4facing2]
  sprites1punch = [sprite1punchfacing1,sprite2punchfacing1,sprite3punchfacing1,sprite4punchfacing1]
  sprites2punch = [sprite1punchfacing2,sprite2punchfacing2,sprite3punchfacing2,sprite4punchfacing2]
  chosenPunch1 = sprites1punch[selectedSprite1]
  chosenPunch2 = sprites2punch[selectedSprite2]

def resetVariables():
  global hp1,hp2,spriteX1,spriteY1,spriteX2,spriteY2,xFlip1,xFlip2,p1nn,p2nn,canPunch1,canPunch2,countdown,countdownNum
  hp1 = 100
  hp2 = 100
  spriteX1 = WIDTH - (2)*(spriteS)
  spriteY1 = HEIGHT - spriteS - 80
  spriteX2 = spriteS
  spriteY2 = HEIGHT - spriteS - 80
  xFlip1 = True
  xFlip2 = False
  p1nn = ""
  p2nn = ""
  canPunch1 = False
  canPunch2 = False
  countdown = True
  countdownNum = 3

spriteStuffs()
sprite1Character = sprites1[selectedSprite1]
sprite2Character = sprites2[selectedSprite2]

mixer.music.play()
# game loop ---------------------------------------------------------------------------------------
while True:
  mixer.music.unpause()
  # determine facing which side and punching 
  spriteStuffs()

  # determine punching sprites
  if canPunch1:
    sprite1Character = sprites1punch[selectedSprite1]
  else:
    sprite1Character = sprites1[selectedSprite1]
  if canPunch2:
    sprite2Character = sprites2punch[selectedSprite2]
  else:
    sprite2Character = sprites2[selectedSprite2]
  
  # home screen -----------------------------------------------------------------------------------
  if window == windows[0]:
    screen.blit(bg,(0,0))
    screen.blit(logo,(125,20))
    screen.blit(fight,(325,370))
    pygame.draw.polygon(screen,LIGHT_YELLOW,((308,409),(320,414),(320,404)),fill)
    pygame.draw.polygon(screen,LIGHT_YELLOW,((496,409),(484,414),(484,404)),fill)
    pygame.display.update()

    # get mouse coordinates
    mouseX,mouseY = pygame.mouse.get_pos()

    # game button ("FIGHT" text on title screen)
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if (mouseX >= 325 and mouseX <= 475) and (mouseY >= 370 and mouseY <= 448):
            window = windows[1]

  # choose your fighter screen --------------------------------------------------------------------
  elif window == windows[1]:
    screen.blit(otherBg,(0,0)) 
    screen.blit(text1,(40,70))
    screen.blit(selected1,(450,170))
    pygame.draw.polygon(screen,LIGHT_YELLOW,((xCoord,yCoord),(xCoord+10,yCoord+10),(xCoord-10,yCoord+10)),fill)
    screen.blit(sprite1,(60,190))
    screen.blit(sprite2,(195,190))
    screen.blit(sprite3,(60,380))
    screen.blit(sprite4,(195,380))
    # player name box
    pygame.draw.rect(screen,LIGHT_GREY,(430,524,230,30),fill,4)
    pygame.draw.rect(screen,DARK_GREY,(430,524,230,30),4,4)
    if p1nn == "" and canType1 == False:
      enterName1 = "click to enter a name"
      screen.blit(text4,(435,529))
    else:
      enterName1 = p1nn
      screen.blit(otherFont.render(enterName1,True,BLACK),(435,529))
    # draw buttons to coordinate between pages
    pygame.draw.polygon(screen,YELLOW,((34,539),(66,554),(66,524)),fill)
    pygame.draw.polygon(screen,YELLOW,((766,539),(734,554),(734,524)),fill)
    pygame.display.update()

    # get mouse coordinates
    mouseX,mouseY = pygame.mouse.get_pos()

    # click on selected fighter
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          # select fighter
          if (mouseX >= 60 and mouseX <= 188) and (mouseY >= 190 and mouseY <= 318):
            if selected2 != bigSprites[0]:
              selectedSprite1 = 0
              selected1 = bigSprites[selectedSprite1]
              xCoord = coords[0]
              yCoord = coords[2]
              sprite1Character = sprites1[selectedSprite1]
              chosenPunch1 = sprites1punch[selectedSprite1]
          elif (mouseX >= 195 and mouseX <= 323) and (mouseY >= 190 and mouseY <= 318):
            if selected2 != bigSprites[1]:
              selectedSprite1 = 1
              selected1 = bigSprites[selectedSprite1]
              xCoord = coords[1]
              yCoord = coords[2]
              sprite1Character = sprites1[selectedSprite1]
              chosenPunch1 = sprites1punch[selectedSprite1]
          elif (mouseX >= 60 and mouseX <= 188) and (mouseY >= 380 and mouseY <= 508):
            if selected2 != bigSprites[2]:
              selectedSprite1 = 2
              selected1 = bigSprites[selectedSprite1]
              xCoord = coords[0]
              yCoord = coords[3]
              sprite1Character = sprites1[selectedSprite1]
              chosenPunch1 = sprites1punch[selectedSprite1]
          elif (mouseX >= 195 and mouseX <= 323) and (mouseY >= 380 and mouseY <= 508):
            if selected2 != bigSprites[3]:
              selectedSprite1 = 3
              selected1 = bigSprites[selectedSprite1]
              xCoord = coords[1]
              yCoord = coords[3]
              sprite1Character = sprites1[selectedSprite1]
              chosenPunch1 = sprites1punch[selectedSprite1]
          # buttons coordinating pages
          if (mouseX >= 34 and mouseX <= 66) and (mouseY >= 524 and mouseY <= 554):
            window = windows[0]
          elif (mouseX >= 734 and mouseX <= 766) and (mouseY >= 524 and mouseY <= 554):
            window = windows[2]
          # add a player name
          if (mouseX >= 430 and mouseX <= 660) and (mouseY >= 524 and mouseY <= 554):
            canType1 = True
            screen.blit(otherFont.render("",True,BLACK),(435,529))
          if not(mouseX >= 430 and mouseX <= 660) and not(mouseY >= 524 and mouseY <= 554):
            canType1 = False
      if event.type == pygame.KEYDOWN and canType1:
        if event.key >= pygame.K_EXCLAIM and event.key <= pygame.K_z:
          if len(p1nn) < 15:
            p1nn = p1nn + pygame.key.name(event.key)
        if event.key == pygame.K_BACKSPACE:
          p1nn = p1nn[:-1]
        if event.key == pygame.K_SPACE:
          p1nn = p1nn + " "
        print(p1nn)

  # choose your fighter (2) screen ----------------------------------------------------------------
  elif window == windows[2]:
    screen.blit(otherBg,(0,0)) 
    screen.blit(text2,(40,70))
    if selected2 == bigSprites[0]:
      x2Coord = coords[0]
      y2Coord = coords[2]
    elif selected2 == bigSprites[1]:
      x2Coord = coords[1]
      y2Coord = coords[2]
    elif selected2 == bigSprites[2]:
      x2Coord = coords[0]
      y2Coord = coords[3]
    else:
      x2Coord = coords[1]
      y2Coord = coords[3]

    screen.blit(selected2,(450,170))
    pygame.draw.polygon(screen,LIGHT_YELLOW,((x2Coord,y2Coord),(x2Coord+10,y2Coord+10),(x2Coord-10,y2Coord+10)),fill)
    screen.blit(sprite1,(60,190))
    screen.blit(sprite2,(195,190))
    screen.blit(sprite3,(60,380))
    screen.blit(sprite4,(195,380))
    # player name box
    pygame.draw.rect(screen,LIGHT_GREY,(430,524,230,30),fill,4)
    pygame.draw.rect(screen,DARK_GREY,(430,524,230,30),4,4)
    if p2nn == "" and canType2 == False:
      enterName2 = "click to enter a name"
      screen.blit(text4,(435,529))
    else:
      enterName2 = p2nn
      screen.blit(otherFont.render(enterName2,True,BLACK),(435,529))
    # draw buttons to coordinate between pages
    pygame.draw.polygon(screen,YELLOW,((34,539),(66,554),(66,524)),fill)
    pygame.draw.polygon(screen,YELLOW,((766,539),(734,554),(734,524)),fill)
    pygame.display.update()

    # get mouse coordinates
    mouseX,mouseY = pygame.mouse.get_pos()

    # click on selected fighter
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          # select fighter
          if (mouseX >= 60 and mouseX <= 188) and (mouseY >= 190 and mouseY <= 318):
            if selected1 != bigSprites[0]:
              selectedSprite2 = 0
              selected2 = bigSprites[selectedSprite2]
              x2Coord = coords[0]
              y2Coord = coords[2]
              sprite2Character = sprites2[selectedSprite2]
              chosenPunch2 = sprites2punch[selectedSprite2]
          elif (mouseX >= 195 and mouseX <= 323) and (mouseY >= 190 and mouseY <= 318):
            if selected1 != bigSprites[1]:
              selectedSprite2 = 1
              selected2 = bigSprites[selectedSprite2]
              x2Coord = coords[1]
              y2Coord = coords[2]
              sprite2Character = sprites2[selectedSprite2]
              chosenPunch2 = sprites2punch[selectedSprite2]
          elif (mouseX >= 60 and mouseX <= 188) and (mouseY >= 380 and mouseY <= 508):
            if selected1 != bigSprites[2]:
              selectedSprite2 = 2
              selected2 = bigSprites[selectedSprite2]
              x2Coord = coords[0]
              y2Coord = coords[3]
              sprite2Character = sprites2[selectedSprite2]
              chosenPunch2 = sprites2punch[selectedSprite2]
          elif (mouseX >= 195 and mouseX <= 323) and (mouseY >= 380 and mouseY <= 508):
            if selected1 != bigSprites[3]:
              selectedSprite2 = 3
              selected2 = bigSprites[selectedSprite2]
              x2Coord = coords[1]
              y2Coord = coords[3]
              sprite2Character = sprites2[selectedSprite2]
              chosenPunch2 = sprites2punch[selectedSprite2]
          # buttons coordinating pages
          if (mouseX >= 34 and mouseX <= 66) and (mouseY >= 524 and mouseY <= 554):
            window = windows[1]
          elif (mouseX >= 734 and mouseX <= 766) and (mouseY >= 524 and mouseY <= 554):
            window = windows[3]
          # add a player name
          if (mouseX >= 430 and mouseX <= 660) and (mouseY >= 524 and mouseY <= 554):
            canType2 = True
            screen.blit(otherFont.render("",True,BLACK),(435,529))
          if not(mouseX >= 430 and mouseX <= 660) and not(mouseY >= 524 and mouseY <= 554):
            canType2 = False
      if event.type == pygame.KEYDOWN and canType2:
        if event.key >= pygame.K_EXCLAIM and event.key <= pygame.K_z:
          if len(p2nn) < 15:
            p2nn = p2nn + pygame.key.name(event.key)
        if event.key == pygame.K_BACKSPACE:
          p2nn = p2nn[:-1]
        if event.key == pygame.K_SPACE:
          p2nn = p2nn + " "
        print(p2nn)

  # choose game stage screen ----------------------------------------------------------------------
  elif window == windows[3]:
    screen.blit(lastBg,(0,0))
    screen.blit(text10,(655,480))
    screen.blit(text3,(40,70))
    screen.blit(smallBoxing,(85,220))
    pygame.draw.rect(screen,RED,(85,220,230,173),5)
    screen.blit(smallColiseum,(485,220))
    pygame.draw.rect(screen,RED,(485,220,230,173),5)
    pygame.draw.polygon(screen,LIGHT_YELLOW,((x3Coord,405),(x3Coord+10,405+10),(x3Coord-10,405+10)),fill)
    # draw button to coordinate between pages
    pygame.draw.polygon(screen,YELLOW,((34,539),(66,554),(66,524)),fill)
    pygame.display.update()

    # get mouse coordinates
    mouseX,mouseY = pygame.mouse.get_pos()

    # click on selected stage
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          # choose stage
          if (mouseX >= 85 and mouseX <= 315) and (mouseY >= 220 and mouseY <= 393):
            stage = boxing
            x3Coord = coords[4]
          if (mouseX >= 485 and mouseX <= 715) and (mouseY >= 220 and mouseY <= 393):
            stage = coliseum
            x3Coord = coords[5]
          # buttons coordinating pages
          if (mouseX >= 34 and mouseX <= 66) and (mouseY >= 524 and mouseY <= 554):
            window = windows[2]
          elif (mouseX >= 410 and mouseX <= 800) and (mouseY >= 470 and mouseY <= 600):
            window = windows[4]

  # game screen -----------------------------------------------------------------------------------
  elif window == windows[4]:
    # draw sprites on screen
    screen.blit(stage,(0,0))
    screen.blit(sprite1Character,(spriteX1,spriteY1))
    screen.blit(sprite2Character,(spriteX2,spriteY2))
    # if someone won the game
    if ((hp1 <= 0) or (hp2 <= 0)):
      screen.blit(opacitySurface,(0,0))
      pygame.draw.rect(opacitySurface,GREY_LOW_OPACTITY,(65,185,670,230),fill)
      # the winner is [winner]
      text6 = titleFont.render("The winner is "+winner+"!",True,LIGHT_YELLOW)
      screen.blit(text6,(80,225))
      # home screen
      pygame.draw.polygon(screen,WHITE,((85,291),(97,296),(97,286)),fill)
      screen.blit(text7,(111,280))
      pygame.draw.polygon(screen,WHITE,((351,291),(339,296),(339,286)),fill)
      # fighter selection
      pygame.draw.polygon(screen,WHITE,((85,316),(97,321),(97,311)),fill)
      screen.blit(text8,(111,305))
      pygame.draw.polygon(screen,WHITE,((468,316),(457,321),(457,311)),fill)
      # stage selection
      pygame.draw.polygon(screen,WHITE,((85,341),(97,346),(97,336)),fill)
      screen.blit(text9,(111,330))
      pygame.draw.polygon(screen,WHITE,((453,341),(442,346),(442,336)),fill)
    # display hp bars
    pygame.draw.rect(screen,WHITE,(boxX1,(boxY-boxS-5),(10)*(boxS),(boxS+boxS+5)),fill,5)
    pygame.draw.rect(screen,WHITE,(boxX2,(boxY-boxS-5),(10)*(boxS),(boxS+boxS+5)),fill,5)
    pygame.draw.rect(screen,OTHER_GREY,(boxX1,(boxY),(10)*(boxS),(boxS)),fill,5)
    pygame.draw.rect(screen,OTHER_GREY,(boxX2,(boxY),(10)*(boxS),(boxS)),fill,5)
    pygame.draw.rect(screen,BLACK,(boxX2,(boxY-boxS-5),(10)*(boxS),(boxS+boxS+5)),2,5)
    pygame.draw.rect(screen,BLACK,(boxX1,(boxY-boxS-5),(10)*(boxS),(boxS+boxS+5)),2,5)
    if hp1 <= 30:
      colour = BRIGHTER_RED
    elif hp1 <= 50:
      colour = OTHER_YELLOW
    else:
      colour = GREEN
    pygame.draw.rect(screen,colour,(boxX1,boxY,(boxS)*(hp1/10),boxS),fill,5)
    if hp2 <= 30:
      colour = BRIGHTER_RED
    elif hp2 <= 50:
      colour = OTHER_YELLOW
    else:
      colour = GREEN
    pygame.draw.rect(screen,colour,(boxX2,boxY,(boxS)*(hp2/10),boxS),fill,5)
    pygame.draw.rect(screen,BLACK,((WIDTH - (4+10)*(boxS)),boxY,(10)*(boxS),boxS),2,5)
    pygame.draw.rect(screen,BLACK,(((4)*(boxS)),boxY,(10)*(boxS),boxS),2,5)
    if p1nn == "":
      playerName1 = "Player One"
    else:
      playerName1 = p1nn
    if p2nn == "":
      playerName2 = "Player Two"
    else:
      playerName2 = p2nn
    screen.blit(otherFont.render(playerName1,True,BLACK),((boxX1+5),(boxY-boxS-4)))
    screen.blit(otherFont.render(playerName2,True,BLACK),((boxX2+5),(boxY-boxS-4)))
    # countdown screen
    if countdown:
      screen.blit(opacitySurface,(0,0))
      pygame.draw.rect(opacitySurface,GREY_LOW_OPACTITY,(0,250,800,80),fill)
      opacitySurface.blit(titleFont.render("game starts in "+str(countdownNum),True,LIGHT_YELLOW),(187,265))
      pygame.display.update()
      if countdownNum == 3:
        MOVE = 3000
        START = pygame.time.get_ticks()
      countdownNum-=1
      elapsedTime = pygame.time.get_ticks() - START
      print(elapsedTime)
      pygame.display.update()
      pygame.time.delay(1050)
      if elapsedTime >= MOVE:
        # remove the countdown screen
        countdown = False
    
    pygame.display.update()
    clock.tick(fps)

    # attack -------------------------------------------------------------

    # get mouse coordinates
    mouseX,mouseY = pygame.mouse.get_pos()

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        # player 1
        if (event.key == pygame.K_RCTRL):
          if xSpriteCollision():
            if not((hp1 <= 0) or (hp2 <= 0)):
              # when sprite1 is in front and facing sprite2 OR when sprite1 isnt in front and facing sprite2
              if ((spriteX1 > spriteX2) and (xFlip1 == True)) or ((spriteX1 < spriteX2) and (xFlip1 == False)):
                sprite1Character = chosenPunch1
                canPunch1 = True
                if hp2 > 0:
                  hp2 -= 10
        else:
          canPunch1 = False
          sprite1Character = sprites1[selectedSprite1]

        # player 2
        if (event.key == pygame.K_f):
          if xSpriteCollision():
            if not((hp1 <= 0) or (hp2 <= 0)):
              # when sprite2 is in front and facing sprite2 OR when sprite2 isnt in front and facing sprite1
              if ((spriteX2 > spriteX1) and (xFlip2 == True)) or ((spriteX2 < spriteX1) and (xFlip2 == False)):
                sprite2Character = chosenPunch2
                canPunch2 = True
                if hp1 > 0:
                  hp1 -= 10
        else:
          canPunch2 = False
          sprite2Character = sprites2[selectedSprite2]
      # if a button is clicked
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          # if a player won
          if ((hp1 <= 0) or (hp2 <= 0)):
            resetVariables()
            # home screen button
            if (mouseX >= 111 and mouseX <= 351) and (mouseY >= 280 and mouseY <= 305):
              window = windows[0]
            # fighter selection button
            if (mouseX >= 111 and mouseX <= 468) and (mouseY >= 305 and mouseY <= 330):
              window = windows[1]
            # stage selection button
            if (mouseX >= 111 and mouseX <= 453) and (mouseY >= 330 and mouseY <= 355):
              window = windows[3]

    if not((hp1 <= 0) or (hp2 <= 0)):        
      keys = pygame.key.get_pressed()
      
      # player one -------------------------------------------------------

      # player one's sprite moving left
      if keys[pygame.K_LEFT]:
        # collision against walls
        if spriteX1 <= 0:
          spriteX1 -= 0 
        else:
          # normally moving left
          if not xSpriteCollision():
            spriteX1 -= distanceNum
            xFlip1 = True
          # if colliding and sprite1 is in front of sprite2, it can still move left
          elif xSpriteCollision() and (spriteX1 < spriteX2):
            spriteX1 -= distanceNum
            xFlip1 = True
          # if colliding and sprite2 is in front of sprite1, it cant move left
          elif xSpriteCollision() and (spriteX1 > spriteX2):
            spriteX1 -= 0
      
      # player one's sprite moving right
      if keys[pygame.K_RIGHT]:
        # collision against walls
        if spriteX1 >= WIDTH-spriteS:
          spriteX1 -= 0
        else:
          # normally moving right
          if not xSpriteCollision():
            spriteX1 += distanceNum
            xFlip1 = False
          # if colliding and sprite1 is in front of sprite2, it can still move right
          elif xSpriteCollision() and (spriteX1 > spriteX2):
            spriteX1 += distanceNum
            xFlip1 = False
          # if colliding and sprite1 is in front of sprite2, it cant move right
          elif xSpriteCollision() and (spriteX1 < spriteX2):
            spriteX1 += 0

      # player one's sprite jumping
      if spriteY1 < SPRITE_Y-spriteS and not ySpriteCollision():
        spriteY1 += fallGravity
      if keys[pygame.K_UP] and (ySpriteCollision() or spriteY1 >= SPRITE_Y-spriteS):
        jumping = True
      if jumping:
        spriteY1 -= jumpSpeed
        jumpSpeed -= GRAVITY
        if jumpSpeed == 0:
          jumping = False
          jumpSpeed = jumpH
        screen.blit(sprite1Character,(spriteX1,spriteY1))
      else:
        screen.blit(sprite1Character,(spriteX1,spriteY1))

      # player two -------------------------------------------------------
        
      # player two's sprite moving left
      if keys[pygame.K_a]:
        # collision against walls
        if spriteX2 <= 0:
          spriteX2 -= 0 
        else:
          # normally moving left
          if not xSpriteCollision():
            spriteX2 -= distanceNum
            xFlip2 = True
          # if colliding and sprite2 is in front of sprite1, it can still move left
          elif xSpriteCollision() and (spriteX2 < spriteX1):
            spriteX2 -= distanceNum
            xFlip2 = True
          # if colliding and sprite2 is in front of sprite1, it cant move left
          elif xSpriteCollision() and (spriteX2 > spriteX1):
            spriteX2 -= 0

      # player two's sprite moving right
      if keys[pygame.K_d]:
        # collision against walls
        if spriteX2 >= WIDTH-spriteS:
          spriteX2 -= 0
        else:
          # normally moving right
          if not xSpriteCollision():
            spriteX2 += distanceNum
            xFlip2 = False
          # if colliding and sprite1 is in front of sprite2, it can still move right
          elif xSpriteCollision() and (spriteX2 > spriteX1):
            spriteX2 += distanceNum
            xFlip2 = False
          # if colliding and sprite2 is in front of sprite1, it cant move right
          elif xSpriteCollision() and (spriteX2 < spriteX1):
            spriteX2 += 0
      # player two's sprite jumping
      if spriteY2 < SPRITE_Y-spriteS and not ySpriteCollision():
        spriteY2 += fallGravity
      if keys[pygame.K_w] and (ySpriteCollision() or spriteY2 >= SPRITE_Y-spriteS):
        jumping2 = True
      if jumping2:
        spriteY2 -= jumpSpeed2
        jumpSpeed2 -= GRAVITY2
        if jumpSpeed2 == 0:
          jumping2 = False
          jumpSpeed2 = jumpH2
        screen.blit(sprite2Character,(spriteX2,spriteY2))
      else:
        screen.blit(sprite2Character,(spriteX2,spriteY2))
      pygame.event.clear()
    else:
      if hp1 > 0:
        if p1nn == "":
          winner = "Player One"
        else:
          winner = p1nn
      elif hp2 > 0:
        if p1nn == "":
          winner = "Player Two"
        else:
          winner = p2nn