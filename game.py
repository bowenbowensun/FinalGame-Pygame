import pygame, gamebox

#objects
camera = gamebox.Camera(1400,600)

walkSheet = gamebox.load_sprite_sheet( "Rambo Walk.png", 1,4)
gunSheet = gamebox.load_sprite_sheet("Rambo Gun.png",1,4)
badTankSheet = gamebox.load_sprite_sheet('badTank.png',1,7)
uvaTankSheet = gamebox.load_sprite_sheet('UVATank.png',1,7)
vtVillanSheet = gamebox.load_sprite_sheet('vtBadGuy.png',1,4)
explosionSheet = gamebox.load_sprite_sheet('explosion.png',1,3)
flyRambo = gamebox.from_image(0,0,'flyRambo.png')
flySheet = gamebox.load_sprite_sheet('flySheet.png',1,4)
coverPic = gamebox.from_image(700,300,'CoverPic.png')


wallList = [ gamebox.from_color(3500,600,"black",8000,100),
            gamebox.from_color(350,380,"black",300,25),gamebox.from_color(4900,380,'black',600,25),
             gamebox.from_color(11500,600,"black",6000,100),gamebox.from_color(7870,380,"black",400,25),
             gamebox.from_color(8300,280,"black",300,25),gamebox.from_color(15900,550,'black',2000,200),
             ]

weaponList = [gamebox.from_image(350,340,'MachineGun.png'),gamebox.from_image(10000,460,'unmannedTank.png'),
              gamebox.from_image(16300,420,'flyBoot.png')]

villanList = [gamebox.from_image(2500,468,vtVillanSheet[0]),gamebox.from_image(1500,468,vtVillanSheet[0]),
              gamebox.from_image(2000,468,vtVillanSheet[0]),gamebox.from_image(5000,468,vtVillanSheet[0]),
              gamebox.from_image(5200,468,vtVillanSheet[0]),gamebox.from_image(5400,468,vtVillanSheet[0]),
              gamebox.from_image(8400,0,vtVillanSheet[0]),gamebox.from_image(10500,468,vtVillanSheet[0]),
              gamebox.from_image(10700,468,vtVillanSheet[0]),gamebox.from_image(10900,468,vtVillanSheet[0]),
              gamebox.from_image(16000,368,vtVillanSheet[0]),gamebox.from_image(16200,368,vtVillanSheet[0])]
deadVillan = gamebox.from_image(-500,2000,'deadVillan.png')

badTankList = [gamebox.from_image(4000,468,badTankSheet[0]),gamebox.from_image(6800,468,badTankSheet[0]),
               gamebox.from_image(11200,468,badTankSheet[0]),gamebox.from_image(11800,468,badTankSheet[0]),
               gamebox.from_image(12400,468,badTankSheet[0]),gamebox.from_image(13000,468,badTankSheet[0])]
deadTank = gamebox.from_image(-500,2000,'deadTank.png')

decoList = [gamebox.from_image(-150,480,'signHokie.png'),gamebox.from_image(3050,410,'tree.png'),gamebox.from_image(4380,200,'smallCloud.png')
            ,gamebox.from_image(5800,350,'towerHokie.png'),gamebox.from_image(7200,100,'bigCloud.png'),
            gamebox.from_image(8600,410,'tree.png'),gamebox.from_image(9100,360,'treeTall.png'),
            gamebox.from_image(15100,360,'treeLong.png'),gamebox.from_image(10800,380,'towerBig.png'),
            gamebox.from_image(16000,100,'smallCloud.png'),gamebox.from_image(16300,240,'bootInstruction.png')]

Timmer = 0
Temp = 0

gameActive = False

bulletList = []
for i in range(0,100):
    bullet = gamebox.from_color(-500,2000,'red',12,8)
    bullet.facing = None
    bulletList.append(bullet)
bulletCount = 0

badBulletList = []
for i in range(0,100):
    bullet = gamebox.from_color(-500,2000,'black',12,8)
    bullet.facing = None
    badBulletList.append(bullet)
badBulletCount = 0

tankBulletList = []
for i in range(0,100):
    bullet = gamebox.from_color(-500,2000,'red',48,32)
    bullet.facing = None
    tankBulletList.append(bullet)
tankBulletCount = 0

BadtankBulletList = []
for i in range(0,100):
    bullet = gamebox.from_color(-500,2000,'black',48,32)
    bullet.facing = None
    BadtankBulletList.append(bullet)
BadtankBulletCount = 0


gunFire = gamebox.from_image(0,0,'gunFire.png')
leftGunFire = gamebox.from_image(0,0,'LgunFire.png')
tankFire = gamebox.from_image(0,0,'tankFire.png')
leftTankFire = gamebox.from_image(0,0,'LtankFire.png')

character = gamebox.from_image(0,200,walkSheet[0])

#background
backGround = gamebox.from_image(0,460,'background.png')






#Sound Effects
loadSound = gamebox.load_sound('gunUp.wav')
shotSound = gamebox.load_sound('Shot.wav')
tankFireSound = gamebox.load_sound('tankFire.wav')
tankSound = gamebox.load_sound('tankRide.wav')
explosionSound = gamebox.load_sound('explosion.wav')
flySound = gamebox.load_sound('flySound.wav')


wahoowa = gamebox.from_image(0,0,'wahoowa.png')
wahoowa.temp = 0

Rounds = 0

#initialSetup ------ Run Once
def initialSetup():
    character.facing = None
    character.image = walkSheet[0]
    character.yspeed = 0
    character.full_size()
    character.facing = 'R'
    character.center = [0,200]
    character.steps = 0
    character.frame = 0
    character.facing = 'R'
    character.grounded = False
    character.walled = False
    character.weapon = None
    character.health = 100
    backGround.center = [0,460]
    for v in villanList: #use range to configure different health for villans
        v.facing = None
        v.image = vtVillanSheet[0]
        if Rounds != 0:
            v.flip()
        v.full_size()
        v.facing = 'R'
        v.health = 7
        v.frame = 0
        v.speedx = 7
        v.dead = False
    for tank in badTankList: #use range to configure different health for villans
        tank.facing = None
        tank.image = badTankSheet[0]
        tank.full_size()
        if Rounds != 0:
            tank.flip()
        tank.facing = 'R'
        tank.health = 25
        tank.frame = 0
        tank.speedx = 7
        tank.dead = False

    for weapon in weaponList:
        weapon.taken = False


    for tBullet in tankBulletList:
        tBullet.explosion = -1


#Functions
def change_frame_at(noOfFrame):
    character.frame += 1
    if character.frame == noOfFrame:
        character.frame = 0

def configureBadguys(CharacList,BulList,Count,Sheet,noOfFrame,Image):
    for villan in CharacList:

        if villan.dead == False:

            villan.y += 10
            #the facing of villan
            if character.x < villan.x and villan.facing == 'R':
                villan.flip()
                villan.facing = 'L'
            elif character.x > villan.x and villan.facing == 'L':
                villan.flip()
                villan.facing = 'R'

            if character.x - villan.x > -700 and character.x - villan.x < -15:
                villan.x -= villan.speedx
                if Timmer % 2 == 0:
                    villan.image = Sheet[villan.frame]
                    villan.frame += 1
                if villan.frame == noOfFrame:
                    villan.frame = 0
                if Timmer % 30 == 0:
                    tempBullet = BulList[Count]
                    tempBullet.facing = villan.facing
                    if noOfFrame == 7:
                        tempBullet.center = [villan.x - 200,villan.y - 100]
                    elif noOfFrame == 4:
                        tempBullet.center = [villan.x,villan.y -15]
                    Count += 1
                    if Count == 100:
                        Count = 0

            elif character.x - villan.x >15:
                villan.x += villan.speedx
                if Timmer % 2 == 0:
                    villan.image = Sheet[villan.frame]
                    villan.frame += 1
                if villan.frame == noOfFrame:
                    villan.frame = 0
            elif character.x - villan.x > -15 and character.x - villan.x < 15:
                villan.image = Sheet[0]

            if villan.touches(character):
                if character.weapon != 'Tank':
                    character.health -= 1
                else:
                    villan.health -= 2

                if villan.facing == 'L':
                    villan.x += 100
                else:
                    villan.x -= 100

            if villan.health < 0:

                villan.image = Image
                villan.y += 60
                villan.full_size()
                villan.speedx = 0
                villan.dead = True

            camera.draw(villan)
        else:
            camera.draw(villan)
    return Count


def tick(keys):
    global Timmer,Temp,bulletCount,tankBulletCount,badBulletCount,BadtankBulletCount,BadtankBulletList,gameActive,Rounds
    if gameActive == False:
        camera.clear('black')
        camera.draw(coverPic)
        if pygame.K_SPACE in keys:
            gameActive = True
            initialSetup()

    else:
    #Universal Properties
        camera.clear('cyan2')
        camera.center = [character.x,300]
        if character.y < 100:
            camera.y -= abs(character.y-100)
        #Gravity
        character.yspeed += 1
        character.y = character.y + character.yspeed
        #Timmer
        Timmer += 1

    #Configure Backgrounds  #Based on x, change position of background picture
        camera.draw(backGround)

    #draw Decorations
        for deco in decoList:
            camera.draw(deco)

    #Configure Walls
        for wall in wallList:
            camera.draw(wall)
            if character.touches(wall):
                character.move_to_stop_overlapping(wall)
                if wall.y != 600 and character.bottom_touches(wall) == False:
                    character.walled = True
                else:
                    character.walled = False

            if character.bottom_touches(wall):
                character.grounded = True
                character.move_to_stop_overlapping(wall)
            else:
                character.grounded = False

            for v in villanList:
                if v.touches(wall):
                    v.move_to_stop_overlapping(wall)
            for tank in badTankList:
                if tank.touches(wall):
                    tank.move_to_stop_overlapping(wall)

      #EXCEPTION: Charactor Jumping Configuration
                if pygame.K_SPACE in keys and character.grounded:
                    if character.weapon != 'Tank':
                        character.yspeed = -25

    #Configure Weapons
        for weapon in weaponList:
            if weapon.taken == False:
                camera.draw(weapon)

            if character.touches(weapon):
                if weapon.x == weaponList[0].x:
                    weapon.taken = True
                    if character.weapon != 'MachineGun':
                        loadSound.play()
                        character.weapon = 'MachineGun'
                        character.image = gunSheet[0]
                        character.full_size()
                elif weapon.x == weaponList[1].x:
                    weapon.taken = True
                    if character.weapon != 'Tank':
                        character.weapon = 'Tank'
                        character.image = uvaTankSheet[0]
                        character.full_size()
                elif weapon.x == weaponList[2].x:
                    weapon.taken = True
                    if character.weapon != 'FlyBoot':
                        character.weapon = 'FlyBoot'
                        character.image = flyRambo.image
                        character.full_size()
                        character.frame = 0

        if character.weapon == 'Tank' and pygame.K_f in keys:
            loadSound.play()
            weaponList[1].center = [character.x-400,460]
            weaponList[1].taken = False
            character.weapon = 'MachineGun'
            character.image = gunSheet[0]
            character.full_size()
            character.frame = 0


    #Configure Charactor Motion
        if pygame.K_LEFT in keys:
            character.x -= 10
            if character.walled == False:
                backGround.x -= 9.5
            if character.facing == 'R':
                character.flip()
                character.facing = 'L'

            if Timmer % 2 == 0:
                if character.weapon == None:
                    character.image = walkSheet[character.frame]
                    change_frame_at(4)
                elif character.weapon == 'MachineGun':
                    character.image = gunSheet[character.frame]
                    change_frame_at(4)
                elif character.weapon == 'Tank':
                    change_frame_at(7)
                    character.image = uvaTankSheet[character.frame]
                    tankSound.play()


        if pygame.K_RIGHT in keys:
            character.x += 10
            if character.walled == False:
                backGround.x += 9.5
            if character.facing == 'L':
                character.flip()
                character.facing = 'R'

            if Timmer % 2 == 0:
                if character.weapon == None:
                    character.image = walkSheet[character.frame]
                    change_frame_at(4)
                elif character.weapon == 'MachineGun':
                    character.image = gunSheet[character.frame]
                    change_frame_at(4)
                elif character.weapon == 'Tank':
                    character.image = uvaTankSheet[character.frame]
                    change_frame_at(7)
                    tankSound.play()
    #Configure Fly
        if character.weapon == 'FlyBoot':
            if pygame.K_SPACE in keys:
                character.image = flySheet[character.frame]
                character.frame += 1
                if character.frame == 4:
                    character.frame = 0
                character.full_size()
                character.yspeed = -10
                flySound.play()
            else:
                character.image = flyRambo.image
                character.full_size()


        #Jumping Configured at the Wall Loop

    #Configure Shooting
        if character.weapon == 'MachineGun':
            #Configure Fire Rate
            if pygame.K_s in keys and Timmer - Temp > 2:
                shotSound.play()
                Temp = Timmer
                if character.facing == 'R':
                    tempBullet = bulletList[bulletCount]
                    tempBullet.x = (character.x + 100)
                    tempBullet.y = character.y - 14
                    gunFire.center = [character.x+110,character.y-18]
                    camera.draw(gunFire)


                if character.facing == 'L':
                    tempBullet = bulletList[bulletCount]
                    tempBullet.x = (character.x - 100)
                    tempBullet.y = character.y - 14
                    leftGunFire.center = [character.x-105,character.y-18]
                    camera.draw(leftGunFire)


                tempBullet.facing = character.facing
                bulletCount += 1
                if bulletCount == 99:
                    bulletCount = 0
        elif character.weapon == 'Tank':
            if pygame.K_s in keys and Timmer - Temp > 20:
                tankFireSound.play()
                Temp = Timmer
                if character.facing == 'R':
                    tempBullet = tankBulletList[tankBulletCount]
                    tempBullet.x = (character.x + 200)
                    tempBullet.y = character.y - 50
                    tankFire.center = [character.x+250,character.y-50]
                    camera.draw(tankFire)


                if character.facing == 'L':
                    tempBullet = tankBulletList[tankBulletCount]
                    tempBullet.x = (character.x - 200)
                    tempBullet.y = character.y - 50
                    leftTankFire.center = [character.x-250,character.y-50]
                    camera.draw(leftTankFire)


                tempBullet.facing = character.facing
                tankBulletCount += 1
                if bulletCount == 99:
                    bulletCount = 0

    #draw WAHOOWA
        if character.x > 13000 and wahoowa.temp < 60:
            wahoowa.center = [character.x,character.y-200]
            camera.draw(wahoowa)
            wahoowa.temp += 1



    #Health Info
        healthBar = gamebox.from_color(camera.x - (100-character.health) - 498,camera.y + 280,'red',character.health*2,10)
        healthBottom = gamebox.from_color(camera.x - 498,camera.y + 280,'white',200,10)
        camera.draw(healthBottom)
        camera.draw(healthBar)

    #Configure Character Health
        if character.health < 0:
            camera.center = [700,300]
            gameActive = False
            Rounds += 1
            if character.facing == 'L':
                character.facing = 'R'
                character.flip()

        if character.y > 700:
            character.health -= 1

    #Configure Villans
        badBulletCount = configureBadguys(villanList,badBulletList,badBulletCount,vtVillanSheet,4,deadVillan.image)

    #Configure BadTanks
        BadtankBulletCount = configureBadguys(badTankList,BadtankBulletList,BadtankBulletCount,badTankSheet,7,deadTank.image)

    #Configure MachineGun Bullet
        for abullet in bulletList:
            if abullet.facing == 'R':
                abullet.x += 20
            elif abullet.facing == 'L':
                abullet.x -= 20

            for v in villanList:
                if v.touches(abullet):
                    v.health -= 1
                    abullet.center = [-500,2000]

                    if v.facing == 'L':
                        v.x += 10
                    else:
                        v.x -= 10
            for tank in badTankList:
                if tank.touches(abullet) and tank.dead == False:
                    tank.health -= 1
                    abullet.center = [-500,2000]

                    if tank.facing == 'L':
                        tank.x += 5
                    else:
                        tank.x -= 5


            if abs(camera.x - abullet.x) > 700:
                abullet.center = [-500,2000]
            camera.draw(abullet)

    #Configure Tank Bullet
        for abullet in tankBulletList:
            if abullet.explosion == -1:
                if abullet.facing == 'R':
                    abullet.x += 20
                elif abullet.facing == 'L':
                    abullet.x -= 20

                for v in villanList:
                    if v.touches(abullet):
                        v.health -= 5
                        abullet.explosion = 0

                        if v.facing == 'L':
                            v.x += 70
                        else:
                            v.x -= 70
                for tank in badTankList:
                    if tank.touches(abullet) and tank.dead == False:
                        tank.health -= 10
                        abullet.explosion = 0

                        if tank.facing == 'L':
                            tank.x += 70
                        else:
                            tank.x -= 70
            elif abullet.explosion == 0:
                explosionSound.play()
                abullet.image = explosionSheet[0]
                abullet.full_size()
                abullet.explosion = 1
            elif abullet.explosion == 1:
                abullet.image = explosionSheet[1]
                abullet.explosion = 2
            elif abullet.explosion == 2:
                abullet.image = explosionSheet[2]
                abullet.explosion == -1
                abullet.center = [-500,2000]


            if abs(camera.x - abullet.x) > 700:
                abullet.center = [-500,2000]
            camera.draw(abullet)

    #Configure Bad Bullet
        for abullet in badBulletList:
            if abullet.facing == 'R':
                abullet.x += 20
            elif abullet.facing == 'L':
                abullet.x -= 20

            if abullet.touches(character):
                character.health -= 3
                abullet.center = [-500,2000]

                if character.facing == 'L':
                    character.x += 35
                else:
                    character.x -= 35

            if abs(camera.x - abullet.x) > 700:
                abullet.center = [-500,2000]
            camera.draw(abullet)

    #Configure Bad Tank Bullet
        for abullet in BadtankBulletList:
            if abullet.facing == 'R':
                abullet.x += 20
            elif abullet.facing == 'L':
                abullet.x -= 20

            if abullet.touches(character):
                character.health -= 3
                abullet.center = [-500,2000]

                if character.facing == 'L':
                    character.x += 70
                else:
                    character.x -= 70

            if abs(camera.x - abullet.x) > 700:
                abullet.center = [-500,2000]
            camera.draw(abullet)


        camera.draw(character)
    camera.display()

    #Test Key 7
    if pygame.K_7 in keys:
        character.health = 100
        print(character.center)





ticks_per_second = 30
gamebox.timer_loop(ticks_per_second,tick)

