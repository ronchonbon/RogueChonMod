label hide_girl(character, sprite = False):
    if character != StormX:
        call expression character.Tag + "_Sex_Reset"

    if character != JubesX:
        hide expression character.Tag + "_SexSprite"
        hide expression character.Tag + "_Doggy_Animation"

    hide expression character.Tag + "_HJ_Animation"
    hide expression character.Tag + "_BJ_Animation"
    hide expression character.Tag + "_TJ_Animation"

    if character in [EmmaX]:
        hide expression character.Tag + "_FJ_Animation"

    if character in [JeanX]:
        hide expression character.Tag + "_PJ_Animation"

    if sprite:
        hide expression character.Tag + "_Sprite"

    return

label reset_position(character, trigger = Trigger, set = True):
    if character.Loc != bg_current:
        return

    call hide_girl(character, sprite = True)

    if character == RogueX:
        $ x_anchor = 0.6
    else:
        $ x_anchor = 0.5

    show expression character.Tag + "_Sprite" at sprite_location(character.sprite_location) zorder character.Layer:
        ease 0.5 offset (0,0) anchor (x_anchor, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1

    $ character.Pose = "full" if set else 0
    $ Trigger = trigger

    return

label kissing_launch(character, trigger = Trigger, set = True):
    call hide_girl(character, sprite = True)

    $ Trigger = trigger

    $ character.Pose = "kiss" if set else character.Pose

    show expression character.Tag + "_Sprite" at sprite_location(StageCenter) zorder character.Layer:
        ease 0.5 offset (0, 0) zoom 2 alpha 1

    return

label kissing_smooch(character):
    call hide_girl(character, sprite = True)

    $ character.FaceChange("kiss")

    show expression character.Tag + "_Sprite" at sprite_location(StageCenter) zorder character.Layer:
        offset (0,0)
        alpha 1
        ease 0.5 xpos StageCenter zoom 2
        pause 1
        ease 0.5 xpos character.sprite_location zoom 1

    pause 1

    $ character.FaceChange("sexy")

    return

label breasts_launch(character, trigger = Trigger, set = True):
    call hide_girl(character, sprite = True)

    $ Trigger = trigger

    $ character.Pose = "breasts" if set else character.Pose

    show Rogue_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
        ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1

    return

label pussy_launch(character, trigger = Trigger, set = True):
    call hide_girl(character, sprite = True)

    $ Trigger = trigger

    $ character.Pose = "pussy" if set else character.Pose

    show expression character.Tag + "_Sprite" at sprite_location(character.sprite_location) zorder character.Layer:
        ease 0.5 pos (700, -400) zoom 2 offset (0,0) alpha 1

    return

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

label Close_Launch(GirlA=0,GirlB=0,XLoc=0,YLoc=0,XZoom=0):  #rkelj
    # Launches the girls close to player
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if GirlB:
            $ BO = [GirlA,GirlB]
    elif GirlA:
            $ BO = [GirlA]
    while BO:
            if BO[0] == KittyX or BO[0] == LauraX:
                $ BO[0].ArmPose = 1
            else:
                $ BO[0].ArmPose = 2
            $ YLoc = 100
            if GirlA == BO[0]:
                    #If this girl is lead
                    if BO[0] == KittyX:
                        $ XLoc = 450
                    elif BO[0] == RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500
                    $ BO[0].Layer = 100
                    $ XZoom = -1.3
            elif GirlB == BO[0]:
                    #If the other girl is lead
                    if BO[0] == EmmaX or LauraX:
                        $ XLoc = 700
                    else:
                        $ XLoc = 715
                    $ BO[0].Layer = 75
                    $ XZoom = 1.3

            if BO[0] in [RogueX, StormX, JubesX]:
                $ x_anchor = 0.6
            elif BO[0] in [KittyX, EmmaX, LauraX, JeanX]:
                $ x_anchor = 0.5

            call hide_girl(BO[0])

            show expression BO[0].Tag + "_Sprite" at sprite_location(XLoc,YLoc) zorder BO[0].Layer:
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (x_anchor, 0.0)

            $ BO.remove(BO[0])
    return

#Lesbian action animations.
image GirlGropeLeftBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6#.7
        pos (300,400)#(300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (280,390)
            ease 1 rotate -20 pos (300,400)
            repeat

image GirlGropeRightBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (160,380) #(160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -30 pos (160,410)
            ease 1 rotate -10 pos (160,380)
            repeat

image GirlGropeThigh:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
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

image GirlGropePussy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (230,615)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (225,620)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (225,620)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
            choice: #Fast stroke
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
            repeat

image GirlFingerPussy:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (230,630)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (230,635)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (230,635)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
            choice: #Fast stroke
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
            repeat



label Les_Launch(Girl=0,XLoc=0,YLoc=0,XZoom=0,BO=[]): #rkeljs
    # Launches the lesbian sex positions
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if Partner not in TotalGirls:
            return
    $ BO = [Girl,Partner]
    while BO:
            if "unseen" in BO[0].RecentActions:
                        $ BO[0].Eyes = "closed"
            elif Girl == BO[0]:
                if Girl == RogueX:
                        $ BO[0].Eyes = "side"
                elif Girl == EmmaX:
                        $ BO[0].Eyes = "sly"
                else:
                        $ BO[0].Eyes = "leftside"
            else:
                        $ BO[0].Eyes = "side"

            if BO[0] == KittyX or BO[0] == LauraX:
                $ BO[0].ArmPose = 1
            else:
                $ BO[0].ArmPose = 2
            $ YLoc = 100
            if Girl == BO[0]:
                    #If this girl is lead
                    if BO[0] == KittyX:
                        $ XLoc = 450
                    elif BO[0] == RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500
                    $ BO[0].Layer = 100
                    $ XZoom = -1.3
            else: #Partner == BO[0]:
                    #If the other girl is lead
                    if BO[0] == EmmaX or LauraX:
                        $ XLoc = 700
                    else:
                        $ XLoc = 715
                    if BO[0] == KittyX:
                            if RogueX in (Partner,Girl):
                                    $ KittyX.Layer = 100
                            else:
                                    $ KittyX.Layer = 25
                    else:
                                    $ BO[0].Layer = 75
                    $ XZoom = 1.3

            if BO[0] in [RogueX, StormX, JubesX]:
                $ x_anchor = 0.6
            elif BO[0] in [KittyX, EmmaX, LauraX, JeanX]:
                $ x_anchor = 0.5

            call hide_girl(BO[0])

            show expression BO[0].Tag + "_Sprite" at sprite_location(XLoc,YLoc) zorder BO[0].Layer:
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (x_anchor, 0.0)

            $ BO.remove(BO[0])
    return
