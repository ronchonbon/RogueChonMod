image lick_animation:
    anchor (0.5, 0.5)

    parallel:
        "images/Lick1.png"
        0.8
        "images/Lick6.png"
        0.2
        "images/Lick2.png"
        0.2
        "images/Lick3.png"
        0.2
        "images/Lick4.png"
        0.8
        "images/Lick3.png"
        0.1
        "images/Lick2.png"
        0.1
        repeat

    parallel:
        pause 0.6
        easein 0.7 yoffset -15
        pause 0.3
        easein 0.8 yoffset 0
        repeat

image doggy_lick_pussy:
    "eat_animation"
    zoom 0.5
    offset (195,540)

image doggy_lick_Ass:
    "eat_animation"
    zoom 0.5
    offset (195,500)

image doggy_grope_breast:
    contains:
        subpixel True

        "images/UI_HandUnder.png"

        xzoom -.55
        yzoom .55
        offset (150,340)#(100,200)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat



image Zero_Doggy_Up:
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png")
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null())

image Zero_Hotdog_Static:
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Hotdog_Moving:
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat


image Zero_Doggy_Static:
    # Sex action_speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 545 #out stroke
            repeat

image Zero_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Rogue_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (530,510)

image Rogue_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,590)



image Rogue_Sex_Dildo_Anim2:
        #this is Rogue's sex animation, action_speed 2 (slow)
        contains:
            subpixel True
            "images/DildoIn.png"
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease 1 ypos 380 #(500,470)
                pause 1
                ease 3 ypos 490
                repeat


image Rogue_Sex_FingerA_Anim1:
        #this is Rogue's fingering animation
        contains:
            subpixel True
            "images/UI_Fingering.png"
            pos (507,600) #X less is left, Y less is up(498,525)
            zoom 1.2#1.3
            block:
                ease .4 ypos 550 #480
                pause .4
                ease 1.2 ypos 600#520
                repeat


#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Anal_Zero_Anim0:
        #this is Rogue's sex animation, action_speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,600) #X less is left, Y less is up (498,520)
            zoom 1.3

image Rogue_Anal_Zero_Anim1:
        #this is Rogue's sex animation, action_speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,600) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 570 #(500,470)
                pause 1
                ease 3 ypos 600
                repeat

image Rogue_Anal_Zero_Anim2:
        #this is Rogue's sex animation, action_speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 450 #(500,470)
                pause 1
                ease 3 ypos 570
                repeat

image Rogue_Anal_Zero_Anim3:
        #this is Rogue's sex animation, action_speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease .25 ypos 450 #(500,470)
                pause .25
                ease 1.5 ypos 570
                repeat
#End Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Hotdog_Zero_Anim0:
        #this is Rogue's sex animation, action_speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,570) #X less is left, Y less is up
            zoom 1.3

image Rogue_Hotdog_Zero_Anim1:
        #this is Rogue's sex animation, action_speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,500) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 560 #(500,500)
                pause .5
                ease 1.5 ypos 500
                repeat


transform Zero_BJ_Static():                            #The static animation for the cock
    anchor (.5,.5)
#    pos (180,560) #(125,300)
    rotate -10
#    pos (-25,0)

transform Zero_BJ_Sucking():                            #The sucking animation for the cock
    anchor (.5,.5)
    rotate 0

transform Zero_BJ_Licking():                            #The licking animation for the cock
    subpixel True
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat

image Zero_Blowcock:
    LiveComposite(                            #The compositived BJ cock
        (175,946),
        (0,0), ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png",
            "True", Null(),
            ),
        )
    anchor (0.5,0.5)
    zoom 1.2
    xoffset 5



transform Zero_TJ_Cock():
    #The sucking animation for the cock
    anchor (.5,.5)
    pos (440,1020) #220,1000 #(180,560)
    rotate 0

transform Zero_TJ_Cock_1():
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout .2 ypos 1060
        easein 1.3 ypos 1020
        repeat

transform Zero_TJ_Cock_2():
    pos (440,1020)
    subpixel True
    block:
        ease .35 ypos 1030
        ease .4 ypos 1020
#        pause .1
        repeat

image Blowcock:
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png",
            "True", Null(),
            ),
    anchor (0.5,0.5)
    zoom 1.0
    alpha 1.0
    offset (26,350)#(-175,450)


transform Handcock_1():
    subpixel True
    rotate_pad False
    ease .5 ypos 450 rotate -2 #450
    pause 0.25
    ease 1.0 ypos 400 rotate 0 #400
    pause 0.1
    repeat

transform Handcock_2():
    subpixel True
    rotate_pad False
    ease .2 ypos 430 rotate -3 #410
    ease .5 ypos 400 rotate 0
    pause 0.1
    repeat


image Zero_Handcock:
    contains:
        ConditionSwitch(    # Zero cock sucking
            "Player.Color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/handcock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/handcock_G.png",
            "Player.Color != 'pink'", Null(),
            ),
    anchor (0.5,1.0)  #1.0
    pos (200,400)#(200,400)

image Rogue_Hotdog_Zero_Anim2:
        #this is Rogue's sex animation, action_speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,510) #X less is left, Y less is up
            zoom 1.3
            block:
                ease .5 ypos 400 #(500,470)
                pause .5
                ease 1 ypos 510
                repeat

image Rogue_Anal_Dildo_Anim2:
        #this is Rogue's sex animation, action_speed 2 (slow)
        contains:
            subpixel True
            "images/DildoIn.png"
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 450 #(500,470)
                pause 1
                ease 3 ypos 570
                repeat

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Zero_Anim0:
        #this is Rogue's sex animation, action_speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,530) #X less is left, Y less is up (498,530)
            zoom 1.3#1.4

image Rogue_Sex_Zero_Anim1:
        #this is Rogue's sex animation, action_speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,525) #X less is left, Y less is up(498,525)
            zoom 1.3#1.4
            block:
                ease 1 ypos 510 #(498,500)
                pause 1
                ease 3 ypos 525
                repeat

image Rogue_Sex_Zero_Anim2:
        #this is Rogue's sex animation, action_speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease 1 ypos 380 #(500,470)
                pause 1
                ease 3 ypos 490
                repeat

image Rogue_Sex_Zero_Anim3:
        #this is Rogue's sex animation, action_speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease .25 ypos 380 #(500,470)
                pause .25
                ease 1.5 ypos 490
                repeat
#End Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Rogue_Sex_FingerP_Anim1:
        #this is Rogue's fingering animation
        contains:
            subpixel True
            "images/UI_Fingering.png"
            pos (507,520) #X less is left, Y less is up(498,525)
            zoom 1.2#1.3
            block:
                ease .2 ypos 480 #(498,500)
                pause .2
                ease .6 ypos 520
                repeat

image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat


image Slap_Ass:
    contains:
        "SlapHand"
        pause 1.2
        Null()

image Slap_Ass:
    contains:
        "UI_Hand"
        subpixel True
        zoom 1
        alpha 0.5
        anchor (0.5,0.5)
        pos (600,380)
        rotate 40
        block:
            parallel:
                ease .5 xpos 300 rotate 80
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9

image NotSlap_Ass:
    contains:
        subpixel True
        "UI_Hand"
        zoom 1
        pos (600,380) #follow through  point r-60
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            pos (600,380)
            rotate 40
            parallel:
                ease .5 xpos 300 rotate 80
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Zero_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Zero_Pussy_Finger:
    # Sex action_speed 1 motions
    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat

image Zero_Doggy_Heading:
    # Sex action_speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat

image Zero_Doggy_Fucking2:
    # Sex action_speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Doggy_Fucking3:
    # Sex action_speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Insert cock animations
image Zero_Doggy_Insert:
    #Insert cock
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png",
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",
            "True", Null(),
            ),


image GropeLeftBreast:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.7
        xzoom -0.7
        pos (180,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat

#image GropeBreast:
image LickRightBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -45 pos (150,370)
            pause .5
            ease 1.5 rotate 30 pos (160,400)
            repeat

image LickLeftBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (280,410)#(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -45 pos (260,380)#(150,370)
            pause .5
            ease 1.5 rotate 30 pos (280,410)#(160,400)
            repeat

image GropeThigh:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GropePussy:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (220,620)
                ease .75 rotate 170 pos (220,635)
            choice:
                ease .5 rotate 190 pos (220,620)
                pause .25
                ease 1 rotate 170 pos (220,635)
            repeat

image FingerPussy:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.7
        pos (230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease .5 rotate 40 pos (240,685)
                pause .5
                ease 1.75 rotate 50 pos (230,720)
            choice:
                ease 2 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
            repeat

image Lickpussy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (250,670)#(0.5,0.5)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (230,650)
            linear .5 rotate -60 pos (220,660)
            easein 1 rotate 10 pos (250,670)
            repeat

image VibratorRightBreast:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380
            pause .25
            repeat

image VibratorLeftBreast:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400
            pause .25
            repeat

image VibratorPussy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665
            pause .25
            repeat

image VibratorAnal:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat

image VibratorPussyInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0

image TestUIAnimation:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat




image Zero_Chibicock:
    LiveComposite(                            #The compositived Chibi UI cock
        (225,350),
        (0,0), ConditionSwitch(
            "Player.Color == 'pink'", "images/Chibi_Cock_P.png",
            "Player.Color == 'brown'", "images/Chibi_Cock_B.png",
            "Player.Color == 'green'", "images/Chibi_Cock_G.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            "Player.Spunk", "images/RogueBJFace/Zero_Cock_Spunk.png",
#            "True", Null(),
#            ),
        )
    anchor (0.5,0.5)



image Chibi_Null:
    #The Blank Chibi-cock
    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    pos (75,675)
    zoom 0.5

image Chibi_Jackin:
    #the jackin it chibi cock
    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        "images/Chibi_Hand_M.png"
        pos (-10,-80)
        anchor (0.5,0.5)
        rotate 20
        block:
                ease .3 rotate -10 pos (0,50)
                ease .7 rotate 20 pos (-10,-80)
                repeat
    pos (75,675)
    zoom 0.5

image Chibi_Handy:
    #the girl handy chibicock
    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        ConditionSwitch(
            "(Partner == StormX and second_girl_primary_action == 'hand') or (focused_Girl == StormX and girl_offhand_action == 'hand')", "images/Chibi_Hand_S.png",
            "True", "images/Chibi_Hand_G.png"
            )
#        "images/Chibi_Hand_G.png"
        pos (0,-110)
        anchor (0.5,0.5)
        rotate -10
        block:
                ease .3 rotate 0 pos (10,10)
                ease .7 rotate -10 pos (0,-130)
                repeat
    pos (75,675)
    zoom 0.5

image Chibi_Mouth_Mask:
    "images/Chibi_Mouth_Mask.png"
    anchor (0.5,0.5)

image Chibi_Mouth_Rogue:
    "images/Chibi_Mouth_R.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Kitty:
    "images/Chibi_Mouth_K.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Emma:
    "images/Chibi_Mouth_E.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Storm:
    "images/Chibi_Mouth_S.png"
    anchor (0.5,0.5)

image Chibi_Sucking:
    # The core sucking image
    contains:
        "Chibi_SuckingB"
    pos (75,675)

image Chibi_SuckingB:
    #The composited Chibi UI cock
    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Partner == RogueX", "Chibi_Mouth_Rogue",
            "Partner == EmmaX", "Chibi_Mouth_Emma",
            "Partner == StormX", "Chibi_Mouth_Storm",
            "True", "Chibi_Mouth_Kitty"
            ),
        (0,0), AlphaMask("Chibi_Sucking_Cock", "Chibi_Mouth_Mask")
        )
    subpixel True
    pos (7,0) #top
    anchor (0.5,0.5)
    zoom 0.5
    xzoom 0.71
    block:
        easeout .25 rotate 0 pos (2,48) xzoom 1 #middle
        easein .25 rotate 0 pos (6,92) xzoom 1 #bottom
        easeout .5 rotate 0 pos (2,48) xzoom 1 #middle
        easein .5 rotate 0 pos (5,0) xzoom 0.71 #top
        repeat

image Chibi_Sucking_Cock:
    #The animation for the cock used in the sucking cock animation
    contains:
        subpixel True
        "Zero_Chibicock"
        pos (100,175) #top
        xzoom 1.5
        anchor (0.5,0.5)
#        alpha 0.5
        rotate 0
        block:
            easeout .25 rotate 0 pos (110,80) xzoom 1 #middle
            easein .25 rotate 0 pos (100,-10) xzoom 1 #bottom
            easeout .5 rotate 0 pos (110,80) xzoom 1 #middle
            easein .5 rotate 0 pos (100,175) xzoom 1.5 #top
            repeat


#>>>>>>>>>>

image Chibi_UI:
    # The basic chibi-UI image that is called
    contains:
        ConditionSwitch(
            "'cockout' not in Player.recent_history", Null(),
            "offhand_action == 'jackin'", "Chibi_Jackin",
            "girl_offhand_action == 'hand' or second_girl_primary_action == 'hand'", "Chibi_Handy",
            "second_girl_primary_action == 'blow'", "Chibi_Sucking",
            "True", "Chibi_Null",
            )
#    anchor (0.5,0.5)
#    pos (75,675)
