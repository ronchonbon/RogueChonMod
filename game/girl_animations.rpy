label hide_girl(character, sprite = False):
    call sex_reset(character)

    if character == RogueX:
        hide Rogue_SexSprite
        hide Rogue_Doggy_Animation
        hide Rogue_HJ_Animation
        hide Rogue_BJ_Animation
        hide Rogue_TJ_Animation

        if sprite:
            hide Rogue_Sprite
    elif character == KittyX:
        hide Kitty_SexSprite
        hide Kitty_Doggy_Animation
        hide Kitty_HJ_Animation
        hide Kitty_BJ_Animation
        hide Kitty_TJ_Animation

        if sprite:
            hide Kitty_Sprite
    elif character == EmmaX:
        hide Emma_SexSprite
        hide Emma_Doggy_Animation
        hide Emma_HJ_Animation
        hide Emma_BJ_Animation
        hide Emma_TJ_Animation
        hide Emma_FJ_Animation

        if sprite:
            hide Emma_Sprite

    return

label reset_position(character, trigger = Trigger, set = True):
    if character.Loc != bg_current:
        return

    call hide_girl(character)

    if character == RogueX:
        $ x_anchor = 0.6
    else:
        $ x_anchor = 0.5

    if character == RogueX:
        show Rogue_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 offset (0,0) anchor (x_anchor, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    elif character == KittyX:
        show Kitty_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 offset (0,0) anchor (x_anchor, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    elif character == EmmaX:
        show Emma_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 offset (0,0) anchor (x_anchor, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1

    $ character.Pose = "full" if set else 0
    $ Trigger = trigger

    return

label kissing_launch(character, trigger = Trigger, set = True):
    call hide_girl(character)

    $ Trigger = trigger

    $ character.Pose = "kiss" if set else character.Pose

    if character == RogueX:
        show Rogue_Sprite at sprite_location(StageCenter) zorder character.Layer:
            ease 0.5 offset (0, 0) zoom 2 alpha 1
    elif character == KittyX:
        show Kitty_Sprite at sprite_location(StageCenter) zorder character.Layer:
            ease 0.5 offset (0, 0) zoom 2 alpha 1
    elif character == EmmaX:
        show Emma_Sprite at sprite_location(StageCenter) zorder character.Layer:
            ease 0.5 offset (0, 0) zoom 2 alpha 1

    return

label kissing_smooch(character):
    call hide_girl(character)

    $ character.FaceChange("kiss")

    if character == RogueX:
        show Rogue_Sprite at sprite_location(StageCenter) zorder character.Layer:
            offset (0,0)
            alpha 1
            ease 0.5 xpos StageCenter zoom 2
            pause 1
            ease 0.5 xpos character.sprite_location zoom 1
    elif character == KittyX:
        show Kitty_Sprite at sprite_location(StageCenter) zorder character.Layer:
            offset (0,0)
            alpha 1
            ease 0.5 xpos StageCenter zoom 2
            pause 1
            ease 0.5 xpos character.sprite_location zoom 1
    elif character == EmmaX:
        show Emma_Sprite at sprite_location(StageCenter) zorder character.Layer:
            offset (0,0)
            alpha 1
            ease 0.5 xpos StageCenter zoom 2
            pause 1
            ease 0.5 xpos character.sprite_location zoom 1

    pause 1

    $ character.FaceChange("sexy")

    return

label breasts_launch(character, trigger = Trigger, set = True):
    call hide_girl(character)

    $ Trigger = trigger

    $ character.Pose = "breasts" if set else character.Pose

    if character == RogueX:
        show Rogue_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1
    elif character == KittyX:
        show Kitty_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1
    elif character == EmmaX:
        show Emma_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1

    return

label pussy_launch(character, trigger = Trigger, set = True):
    call hide_girl(character)

    $ Trigger = trigger

    $ character.Pose = "pussy" if set else character.Pose

    if character == RogueX:
        show Rogue_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 pos (700, -400) zoom 2 offset (0,0) alpha 1
    elif character == KittyX:
        show Kitty_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 pos (700, -400) zoom 2 offset (0,0) alpha 1
    elif character == EmmaX:
        show Emma_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            ease 0.5 pos (700, -400) zoom 2 offset (0,0) alpha 1

    return

label sex_reset(character):
    $ character.ArmPose = 2

    if character == RogueX:
        if renpy.showing("Rogue_Doggy_Animation"):
            call Rogue_Doggy_Reset

            return
        if not renpy.showing("Rogue_SexSprite"):
            return

        hide Rogue_SexSprite

        show Rogue_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            alpha 1
            zoom 1 offset (0,0)
            anchor (0.5, 0.0)
        with dissolve
    elif character == KittyX:
        if renpy.showing("Kitty_Doggy_Animation"):
            call Kitty_Doggy_Reset

            return
        if not renpy.showing("Kitty_SexSprite"):
            return

        hide Kitty_SexSprite

        show Kitty_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            alpha 1
            zoom 1 offset (0,0)
            anchor (0.5, 0.0)
        with dissolve
    elif character == EmmaX:
        if renpy.showing("Emma_Doggy_Animation"):
            call Emma_Doggy_Reset

            return
        if not renpy.showing("Emma_SexSprite"):
            return

        hide Emma_SexSprite

        show Emma_Sprite at sprite_location(character.sprite_location) zorder character.Layer:
            alpha 1
            zoom 1 offset (0,0)
            anchor (0.5, 0.0)
        with dissolve

    $ Speed = 0

    return

transform Rogue_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
    pause 0.1
    repeat

transform Rogue_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat




transform Rogue_Cock_BJ_Starting():
    #The static animation for the cock
    anchor (.5,.5)
    rotate -10

transform Rogue_Cock_BJ_Licking():
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat

transform Rogue_Cock_BJ_Straight():
    #The static animation for the cock
    anchor (.5,.5)
    rotate 0

transform Rogue_BJ_Licking():
    #The licking animation for her face
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform Rogue_BJ_LickingBody():
    #The licking animation for her body
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform Rogue_BJ_Heading():
    #The heading animation for her face
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 35           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat

transform Rogue_BJ_HeadingBody():
    #The heading animation for her body
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 15           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat

transform Rogue_BJ_Sucking():
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50)
        repeat

transform Rogue_BJ_SuckingBody():
    #The sucking animation for her body
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat

transform Rogue_BJ_Deep():
    #The deep animation for her face
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat

transform Rogue_BJ_DeepBody():
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Rogue_BJ_Static():
    #The static animation for her face
    subpixel True
    ease 1.5 offset (0,0)
    repeat

transform Rogue_BJ_StaticBody():
    #The static animation for her face
    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_BJ_Starting():
    #The starting animation for her face
    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_BJ_StartingBody():
    #The starting animation for her face
    subpixel True
    ease 1.5 offset (0,0)
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Rogue_BJ_Launch(Line = Trigger):
    # The sequence to launch the Rogue BJ animations
    if renpy.showing("Rogue_BJ_Animation"):
        return

    call hide_girl(RogueX)
    if Line == "L" or Line == "cum":
        show Rogue_Sprite at sprite_location(StageCenter) zorder RogueX.Layer:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Rogue_Sprite at sprite_location(StageCenter) zorder RogueX.Layer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != RogueX:
                        "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[RogueX.Name] looks around to see if anyone can see her."
    if Line == "L":
            if not RogueX.Blow:
                "[RogueX.Name] hesitantly pulls down your pants and touches her mouth to your cock."
            else:
                "[RogueX.Name] bends down and begins to suck on your cock."

    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    show Rogue_BJ_Animation zorder 150:
        pos (645,510)
    return

label Rogue_BJ_Reset: # The sequence to the Rogue animations from BJ to default
    if not renpy.showing("Rogue_BJ_Animation"):
        return
#    hide Rogue_BJ_Animation
    call hide_girl(RogueX)
    $ Speed = 0

    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        zoom 1 offset (0,0)
    $ RogueX.FaceChange("sexy")
    return

transform Rogue_BJ_MouthAnim():
        #The animation for the heading mouth
        subpixel True
        zoom 0.90     #small
        block: #total time 10 down, 15 back up
            pause .10   #.4
            easeout .55 zoom 0.9 #.25
            linear .10 zoom 0.87
            easein .30 zoom 0.9
            pause .15
            easeout .40 zoom 0.87
            linear .10 zoom 0.9
            easein .45 zoom 0.70
            pause .35
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Rogue_Sex_Launch(Line = Trigger):
    $ Trigger3 = 0 if Trigger3 == "hand" else Trigger3

    $ Line = "solo" if not Line else Line
    $ Player.Sprite = 1
    if Line == "sex":
        $ Player.Cock = "in"
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Cock = "anal"
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Cock = "out"
    elif Line == "foot":
        $ ShowFeet = 1
        $ Player.Cock = "foot"
    elif Line == "massage":
        $ Player.Sprite = 0
        $ Player.Cock = 0
    else: #elif Line == "solo":
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        $ Speed = 0
    $ Trigger = Line

    if RogueX.Pose == "doggy":
            call Rogue_Doggy_Launch(Line)
            return
    if renpy.showing("Rogue_SexSprite"):
        return
    $ Speed = 0
    call hide_girl(RogueX, sprite = True)
    show Rogue_SexSprite zorder 150
#    show Rogue_SexSprite zorder 150:
#        pos (750,230)

    with dissolve
    return

transform Rogue_Sex_Legs_FootAnim1A():
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -65
                ease .25 yoffset -60
                pause 1
                ease 1.50 yoffset 25
                repeat

transform Rogue_Sex_Legs_FootAnim2A():
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                repeat

transform Rogue_Footcock_Zero_Anim1A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset 60#65
                ease .25 yoffset 55#60
                pause 1
                ease 1.50 yoffset -30#285
                repeat

transform Rogue_Footcock_Zero_Anim2A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                repeat


image Rogue_Sex_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask")

image Rogue_Sex_Anal_Fucking3:
    # This is the visual for her pussy during the Speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask")

image Rogue_Anal_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 1#0

image Rogue_Anal_Open_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 3#3

image Rogue_Sex_Anal_Heading:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.9
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_Anal_Spunk_Heading_Over:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:
        #total 5 second
        ease .75 xzoom 1.0   #(1.0)
        pause 1.75
        ease .25 xzoom 1.0  #(1.0)
        ease 2.25 xzoom 0.8   #(0.6)
        repeat
image Rogue_Anal_Spunk_Heading_Under:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.95
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6

transform Rogue_Footcock_StaticA():
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat

transform Rogue_Sex_Legs_FootAnimStaticA():
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat


transform Rogue_Sex_Body_FootAnim1A():
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -25
                ease .25 yoffset -15
                pause 1
                ease 1.50 yoffset 15
                repeat

transform Rogue_Sex_Body_FootAnim2A():
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                repeat

transform Rogue_Sex_Body_FootAnimStaticA():
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat
#End Animations for Rogue's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////



transform Rogue_TJ_Under_1():
    ypos 200
    subpixel True
    block:
        ease 1 ypos 300
        easeout .2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_TJ_Over_1():
    ypos 200
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout .1 ypos 300
        easein 1.2 ypos 120
        repeat

transform Rogue_TJ_Under_2():
    ypos 200
    subpixel True
    block:
        ease .25 ypos 200
        ease .4 ypos 120
        ease .1 ypos 125
        repeat

transform Rogue_TJ_Over_2():
    ypos 200
    subpixel True
    block:
        ease .3 ypos 200
        ease .35 ypos 120
        ease .1 ypos 125          #high point
        repeat


label Rogue_TJ_Launch(Line = Trigger):
    # The sequence to launch the Rogue Titfuck animations
    if renpy.showing("Rogue_TJ_Animation"):
        return
    call hide_girl(RogueX)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 2 xpos 550 offset (0,50)
    if Taboo: # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != RogueX:
                        "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[RogueX.Name] looks around to see if anyone can see her."

    if RogueX.Chest and RogueX.Over:
        "She throws off her [RogueX.Over] and her [RogueX.Chest]."
    elif RogueX.Over:
        "She throws off her [RogueX.Over], baring her breasts underneath."
    elif RogueX.Chest:
        "She tugs off her [RogueX.Chest] and throws it aside."
    $ RogueX.Over = 0
    $ RogueX.Chest = 0
    $ RogueX.Arms = 0

    call first_topless(RogueX)

    if not RogueX.Tit and Line == "L": #first time
        if not RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her [RogueX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her [RogueX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L": #any other time
        if not RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it under her [RogueX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it under her [RogueX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.Name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
            "[RogueX.Name] wraps her tits around your cock."
    show blackscreen onlayer black with dissolve
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Rogue_TJ_Animation at sprite_location(StageRight) zorder 150
    hide blackscreen onlayer black with dissolve
    return

label Rogue_TJ_Reset:
    # The sequence to the Rogue animations from Titfuck to default
    if not renpy.showing("Rogue_TJ_Animation"):
            return
    hide Rogue_TJ_Animation
    call hide_girl(RogueX)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
            zoom 2 xpos 550 offset (0,50)
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos RogueX.sprite_location yoffset 0
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        zoom 1 xpos RogueX.sprite_location yoffset 0

    "[RogueX.Name] pulls back"
    return







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
