
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
            "(Partner == StormX and Trigger4 == 'hand') or (Ch_Focus == StormX and Trigger3 == 'hand')", "images/Chibi_Hand_S.png",
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
            "'cockout' not in Player.RecentActions", Null(),
            "Trigger2 == 'jackin'", "Chibi_Jackin",
            "Trigger3 == 'hand' or Trigger4 == 'hand'", "Chibi_Handy",
            "Trigger4 == 'blow'", "Chibi_Sucking",
            "True", "Chibi_Null",
            )
#    anchor (0.5,0.5)
#    pos (75,675)
