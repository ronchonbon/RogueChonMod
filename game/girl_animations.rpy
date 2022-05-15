label hide_girl(Girl, sprite = False):
    call sex_reset(Girl)

    $ renpy.hide(Girl.Tag + "_SexSprite")
    $ renpy.hide(Girl.Tag + "_Doggy_Animation")
    $ renpy.hide(Girl.Tag + "_HJ_Animation")
    $ renpy.hide(Girl.Tag + "_BJ_Animation")
    $ renpy.hide(Girl.Tag + "_TJ_Animation")

    if Girl == EmmaX:
        $ renpy.hide(Girl.Tag + "_FJ_Animation")

    if Girl == JeanX:
        $ renpy.hide(Girl.Tag + "_PJ_Animation")

    if sprite:
        $ renpy.hide(Girl.Tag = "_Sprite")

    return

label reset_position(Girl, trigger = primary_action, set = True):
    if Girl.location != bg_current:
        return

    call hide_girl(Girl)

    if Girl == RogueX:
        $ x_anchor = 0.6
    else:
        $ x_anchor = 0.5

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        ease 0.5 offset (0,0) anchor (x_anchor, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1

    $ Girl.Pose = "full" if set else 0
    $ primary_action = trigger

    return

label kissing_launch(Girl, trigger = primary_action, set = True):
    call hide_girl(Girl)

    $ primary_action = trigger

    $ Girl.Pose = "kiss" if set else Girl.Pose

    show expression Girl.Tag + "_Sprite" at sprite_location(StageCenter) zorder Girl.Layer:
        ease 0.5 offset (0, 0) zoom 2 alpha 1

    return

label kissing_smooch(Girl):
    call hide_girl(Girl)

    $ Girl.change_face("kiss")

    show expression Girl.Tag + "_Sprite" at sprite_location(StageCenter) zorder Girl.Layer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos Girl.sprite_location zoom 1

    $ Girl.change_face("sexy")

    return

label breasts_launch(Girl, trigger = primary_action, set = True):
    call hide_girl(Girl)

    $ primary_action = trigger

    $ Girl.Pose = "breasts" if set else Girl.Pose

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1

    return

label pussy_launch(Girl, trigger = primary_action, set = True):
    call hide_girl(Girl)

    $ primary_action = trigger

    $ Girl.Pose = "pussy" if set else Girl.Pose

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        ease 0.5 pos (700, -400) zoom 2 offset (0,0) alpha 1

    return

label handjob_launch(Girl, trigger = primary_action):
    if renpy.showing(Girl.Tag + "_HJ_Animation"):
        $ primary_action = "handjob"

        return

    call hide_girl(Girl)

    if Girl == RogueX:
        $ Girl.Arms = 0

    if Girl in [RogueX, EmmaX, LauraX, JeanX, JubesX]:
        $ Girl.ArmPose = 1
    elif Girl in [StormX]:
        $ Girl.ArmPose = 2

    if Girl in [RogueX, KittyX, EmmaX]:
        $ x_offset = 0
        $ y_offset = 200
    elif Girl in [LauraX, JubesX]:
        $ x_offset = -150
        $ y_offset = 200
    elif Girl in [JeanX, StormX]:
        $ x_offset = -150
        $ y_offset = 350

    if Girl in [RogueX, LauraX]:
        if trigger == "L":
            show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
                alpha 1
                ease 1 zoom 1.7 xpos 700 offset (x_offset, y_offset)
        else:
            show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
                alpha 1
                ease 1 zoom 1.7 xpos 700 offset (x_offset, y_offset)
            with dissolve
    elif Girl in [KittyX, EmmaX, JeanX, StormX]:
        if trigger == "L":
            show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
                alpha 1
                ease 1 zoom 1.7 offset (x_offset, y_offset)
        else:
            show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
                alpha 1
                ease 1 zoom 1.7 offset (x_offset, y_offset)
            with dissolve

    if Taboo and trigger == "L":
        if len(Present) >= 2:
            if Present[0] != Girl:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != Girl:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            $ line = renpy.random.choice(["casually glances around to see if anyone can see her"
                "looks around to see if anyone can see her"])

            "[Girl.name] [line]."

        if Girl == RogueX and not Girl.Hand and Girl.Arms:
            "As you pull out your cock, [Girl.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "She then leans over and grabs your cock."
    elif trigger == "L":
        if Girl == RogueX and not Girl.Hand and Girl.Arms:
            "As you pull out your cock, [Girl.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "[Girl.name] bends down and grabs your cock."
    else:
        "[Girl.name] bends down and grabs your cock."

    $ action_speed = 0

    if trigger != "cum":
        $ primary_action = "handjob"

    pause 0.5

    if Girl in [RogueX]:
        show expression Girl.Tag + "_HJ_Animation" at sprite_location(Girl.sprite_location) zorder 150 with easeinbottom
    elif Girl in [KittyX, EmmaX]:
        show expression Girl.Tag + "_HJ_Animation" at sprite_location(Girl.sprite_location) zorder 150 with easeinbottom:
            offset (100, 250)
    elif Girl in [LauraX, JeanX, StormX, JubesX]:
        show expression Girl.Tag + "_HJ_Animation" at sprite_location(Girl.sprite_location) zorder 150 with easeinbottom:
            offset (250, 250)

    return

label handjob_reset(Girl): # The sequence to the Rogue animations from handjob to default
    if not renpy.showing(Girl.Tag + "_HJ_Animation"):
        return

    $ action_speed = 0

    $ renpy.hide(Girl.Tag + "_HJ_Animation")
    with dissolve

    call hide_girl(Girl)

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        alpha 1
        zoom 1.7 xpos 700 offset (0,200)

    show expression Girl.Tag + "_Sprite" zorder Girl.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos Girl.sprite_location yoffset 0

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        alpha 1
        zoom 1 xpos Girl.sprite_location yoffset 0

    return

label titjob_launch(Girl, trigger = primary_action):
    if renpy.showing(Girl.Tag + "_TJ_Animation"):
        return

    call hide_girl(Girl)

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        alpha 1
        ease 1 zoom 2 xpos 550 offset (0,50)

    if Taboo: # Rogue gets started. . .
        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."

    if Girl.Chest and Girl.Over:
        "She throws off her [Girl.Over] and her [Girl.Chest]."
    elif Girl.Over:
        "She throws off her [Girl.Over], baring her breasts underneath."
    elif Girl.Chest:
        "She tugs off her [Girl.Chest] and throws it aside."

    $ Girl.Over = 0
    $ Girl.Chest = 0
    $ Girl.Arms = 0

    call first_topless(Girl)

    if not Girl.Tit and trigger == "L": #first time
        if not Girl.Chest and not Girl.Over:
            "As you pull out your cock, [Girl.name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif Girl.Chest and not Girl.Over:
            "As you pull out your cock, [Girl.name] hesitantly places it under her [Girl.Chest], between her breasts and starts to rub them up and down the shaft."
        elif Girl.Chest and Girl.Over:
            "As you pull out your cock, [Girl.name] hesitantly places it under her [Girl.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [Girl.name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif trigger == "L": #any other time
        if not Girl.Chest and not Girl.Over:
            "As you pull out your cock, [Girl.name] places it between her breasts and starts to rub them up and down the shaft."
        elif Girl.Chest and not Girl.Over:
            "As you pull out your cock, [Girl.name] places it under her [Girl.Chest], between her breasts and starts to rub them up and down the shaft."
        elif Girl.Chest and Girl.Over:
            "As you pull out your cock, [Girl.name] places it under her [Girl.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [Girl.name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
        "[Girl.name] wraps her tits around your cock."

    show blackscreen onlayer black with dissolve

    show expression Girl.Tag + "_Sprite" zorder Girl.Layer:
        alpha 0

    $ action_speed = 0

    if trigger != "cum":
        $ primary_action = "titjob"

    show expression Girl.Tag + "_TJ_Animation" at sprite_location(StageRight) zorder 150

    hide blackscreen onlayer black with dissolve

    return

label titjob_reset(Girl):
    if not renpy.showing(Girl.Tag + "_TJ_Animation"):
        return

    call hide_girl(Girl)

    $ Player.Sprite = 0

    if Girl in [RogueX, KittyX, EmmaX]:
        $ initial_zoom = 2
        $ initial_y_offset = 50
    elif Girl in [LauraX, JeanX, StormX, JubesX]:
        $ initial_zoom = 2.3
        $ initial_y_offset = -100

    if Girl in [RogueX, KittyX, EmmaX, LauraX, JubesX]:
        $ initial_x_position = 550
    elif Girl in [JeanX, StormX]:
        $ initial_x_position = 750

    if Girl in [RogueX, EmmaX]:
        $ mid_x_position = 500
    elif Girl in [KittyX, LauraX, JeanX, StormX, JubesX]:
        $ mid_x_position = 700

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        zoom initial_zoom xpos initial_x_position yoffset initial_y_offset
    show expression Girl.Tag + "_Sprite" zorder Girl.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos mid_x_position yoffset 50
        pause 0.5
        ease 0.5 zoom 1 xpos Girl.sprite_location yoffset 0
    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        alpha 1
        zoom 1 xpos Girl.sprite_location yoffset 0

    "[Girl.name] pulls back"

    return

label blowjob_launch(Girl, trigger = primary_action):
    if renpy.showing(Girl.Tag + "_BJ_Animation"):
        return

    call hide_girl(Girl)

    if trigger == "L" or trigger == "cum":
        show expression Girl.Tag + "_Sprite" at sprite_location(StageCenter) zorder Girl.Layer:
            alpha 1
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80)
        with dissolve
    else:
        show expression Girl.Tag + "_Sprite" at sprite_location(StageCenter) zorder Girl.Layer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140)
        with dissolve

    if Taboo and trigger == "L":
        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[Girl.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[Girl.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[Girl.name] looks around to see if anyone can see her."
    if trigger == "L":
        if not Girl.Blow:
            "[Girl.name] hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "[Girl.name] bends down and begins to suck on your cock."

    $ action_speed = 0

    if trigger != "cum":
        $ primary_action = "blowjob"

    show expression Girl.Tag + "_Sprite" zorder Girl.Layer:
        alpha 0

    show expression Girl.Tag + "_BJ_Animation" zorder 150:
        pos (645,510)

    return

label blowjob_reset(Girl): # The sequence to the Rogue animations from BJ to default
    if not renpy.showing(Girl.Tag + "_BJ_Animation"):
        return

    call hide_girl(Girl)

    $ action_speed = 0

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        alpha 1
        zoom 1 offset (0,0)

    $ Girl.change_face("sexy")

    return

label sex_launch(Girl, trigger = primary_action):
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action

    $ trigger = "solo" if not trigger else trigger

    $ Player.Sprite = 1

    if trigger == "sex":
        $ Player.Cock = "in"

        if offhand_action in ["fondle_pussy", "eat_pussy", "dildo_pussy"]:
            $ offhand_action = 0
    elif trigger == "anal":
        $ Player.Cock = "anal"

        if offhand_action in ["finger_ass", "eat_ass", "dildo_ass"]:
            $ offhand_action = 0
    elif trigger == "hotdog":
        $ Player.Cock = "out"

        if Girl.wearing_skirt:
            $ Girl.Upskirt = 1
    elif trigger == "footjob":
        $ ShowFeet = 1

        $ Player.Cock = "footjob"
    elif trigger == "massage":
        $ Player.Sprite = 0
        $ Player.Cock = 0
    else: #elif trigger == "solo":
        $ Player.Sprite = 0
        $ Player.Cock = "out"

        $ action_speed = 0

    $ primary_action = trigger

    if Girl.Pose == "doggy":
        call doggy_launch(Girl, trigger)

        return

    if renpy.showing(Girl.Tag + "_SexSprite"):
        return

    $ action_speed = 0

    call hide_girl(Girl, sprite = True)

    if primary_action == "in" or primary_action == "anal":
        if Girl.Legs or Girl.HoseNum() >= 5:
            $ Girl.Upskirt = 1

        if Girl.Panties:
            $ Girl.PantiesDown = 1

    if Girl in [RogueX, KittyX, JeanX, StormX]:
        show expression Girl.Tag + "_SexSprite" zorder 150
    elif Girl in [EmmaX]:
        show expression Girl.Tag + "_SexSprite" zorder 150
            pos (575, 470)
    elif Girl in [LauraX, JubesX]:
        show expression Girl.Tag + "_SexSprite" zorder 150
            pos (450, 500)

    with dissolve

    return

label sex_reset(Girl):
    if renpy.showing(Girl.Tag + "_Doggy_Animation"):
        call doggy_reset(Girl)

        return
    if not renpy.showing(Girl.Tag + "_SexSprite"):
        return

    $ Girl.ArmPose = 2

    hide_girl(Girl)

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve

    $ action_speed = 0

    return

label doggy_launch(Girl, trigger = primary_action):
    if renpy.showing(Girl.Tag + "_Doggy_Animation"):
        return

    $ action_speed = 0

    call hide_girl(Girl, sprite = True)

    show expression Girl.Tag + "_Doggy_Animation" at sprite_location(StageCenter+50) zorder 150
    with dissolve

    return

label doggy_reset(Girl):
    if renpy.showing(Girl.Tag + "_Doggy_Animation"):
        return

    $ Girl.ArmPose = 2
    $ Girl.SpriteVer = 0

    if Girl in [RogueX, KittyX]:
        x_anchor = 0.6
    elif Girl in [EmmaX]:
        x_anchor = 0.5

    $ renpy.hide(expression Girl.Tag + "_Doggy_Animation")

    call hide_girl(Girl)

    show expression Girl.Tag + "_Sprite" at sprite_location(Girl.sprite_location) zorder Girl.Layer:
        alpha 1
        zoom 1
        offset (0,0)
        anchor (x_anchor, 0.0)
    with dissolve

    $ action_speed = 0

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


transform Rogue_BJ_MouthAnim():
        #The animation for the heading mouth
        subpixel True
        zoom 0.90     #small
        block: #total time 10 down, 15 back up
            pause .10   #.4
            easeout .55 zoom 0.9 #.25
            linear 0.10 zoom 0.87
            easein .30 zoom 0.9
            pause .15
            easeout .40 zoom 0.87
            linear .10 zoom 0.9
            easein .45 zoom 0.70
            pause .35
            repeat


transform Rogue_Sex_Legs_FootAnim1A():
        #this is the animation for Rogue's lower body during Footjobs, action_speed 2 (slow)
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
        #this is the animation for Rogue's lower body during Footjobs, action_speed 2 (slow)
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
    # This is the visual for her pussy during the action_speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask")

image Rogue_Sex_Anal_Fucking3:
    # This is the visual for her pussy during the action_speed 3 mode (fast).
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
        #this is the animation for Rogue's lower body during Footjobs, action_speed 2 (slow)
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
        #this is the animation for Rogue's upper body during Footjobs, action_speed 2 (slow)
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
        #this is the animation for Rogue's upper body during Footjobs, action_speed 2 (slow)
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
        #this is the animation for Rogue's upper body during Footjobs, action_speed 2 (slow)
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







label Close_Launch(GirlA=0,GirlB=0,XLoc=0,YLoc=0,XZoom=0):  #rkelj
    # Launches the girls close to player
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if GirlB:
            $ Girls = [GirlA,GirlB]
    elif GirlA:
            $ Girls = [GirlA]
    while Girls:
            if Girls[0] == KittyX or Girls[0] == LauraX:
                $ Girls[0].ArmPose = 1
            else:
                $ Girls[0].ArmPose = 2
            $ YLoc = 100
            if GirlA == Girls[0]:
                    #If this girl is lead
                    if Girls[0] == KittyX:
                        $ XLoc = 450
                    elif Girls[0] == RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500
                    $ Girls[0].Layer = 100
                    $ XZoom = -1.3
            elif GirlB == Girls[0]:
                    #If the other girl is lead
                    if Girls[0] == EmmaX or LauraX:
                        $ XLoc = 700
                    else:
                        $ XLoc = 715
                    $ Girls[0].Layer = 75
                    $ XZoom = 1.3

            if Girls[0] in [RogueX, StormX, JubesX]:
                $ x_anchor = 0.6
            elif Girls[0] in [KittyX, EmmaX, LauraX, JeanX]:
                $ x_anchor = 0.5

            call hide_girl(Girls[0])

            show expression Girls[0].Tag + "_Sprite" at sprite_location(XLoc,YLoc) zorder Girls[0].Layer:
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (x_anchor, 0.0)

            $ Girls.remove(Girls[0])
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



label Les_Launch(Girl=0,XLoc=0,YLoc=0,XZoom=0,Girls=[]): #rkeljs
    # Launches the lesbian sex positions
    # Girl is the lead, Partner is the other girl
    # the Loc and Zoom values are generated based on which is which
    if Partner not in all_Girls:
            return
    $ Girls = [Girl,Partner]
    while Girls:
            if "unseen" in Girls[0].recent_history:
                        $ Girls[0].Eyes = "closed"
            elif Girl == Girls[0]:
                if Girl == RogueX:
                        $ Girls[0].Eyes = "side"
                elif Girl == EmmaX:
                        $ Girls[0].Eyes = "sly"
                else:
                        $ Girls[0].Eyes = "leftside"
            else:
                        $ Girls[0].Eyes = "side"

            if Girls[0] == KittyX or Girls[0] == LauraX:
                $ Girls[0].ArmPose = 1
            else:
                $ Girls[0].ArmPose = 2
            $ YLoc = 100
            if Girl == Girls[0]:
                    #If this girl is lead
                    if Girls[0] == KittyX:
                        $ XLoc = 450
                    elif Girls[0] == RogueX:
                        $ XLoc = 550
                    else:
                        $ XLoc = 500
                    $ Girls[0].Layer = 100
                    $ XZoom = -1.3
            else: #Partner == Girls[0]:
                    #If the other girl is lead
                    if Girls[0] == EmmaX or LauraX:
                        $ XLoc = 700
                    else:
                        $ XLoc = 715
                    if Girls[0] == KittyX:
                            if Girl in (Partner,Girl):
                                    $ KittyX.Layer = 100
                            else:
                                    $ KittyX.Layer = 25
                    else:
                                    $ Girls[0].Layer = 75
                    $ XZoom = 1.3

            if Girls[0] in [RogueX, StormX, JubesX]:
                $ x_anchor = 0.6
            elif Girls[0] in [KittyX, EmmaX, LauraX, JeanX]:
                $ x_anchor = 0.5

            call hide_girl(Girls[0])

            show expression Girls[0].Tag + "_Sprite" at sprite_location(XLoc,YLoc) zorder Girls[0].Layer:
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (x_anchor, 0.0)

            $ Girls.remove(Girls[0])
    return



transform Girl_Dance1(Girl=focused_Girl):
        subpixel True
        pos (Girl.sprite_location, 50)
        xoffset 0
        yoffset 0
        choice:
            parallel:
                ease 2.5 xoffset -40
                ease 2.5 xoffset 0
            parallel:
                easeout 1.0 yoffset 30 # 70 and 80
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0
        choice:
            parallel:
                ease 2.5 xoffset 40
                ease 2.5 xoffset 0
            parallel:
                easeout 1.0 yoffset 30 #1.3
                linear 0.5 yoffset 40
                easein 1.0 yoffset 0
                easeout 1.0 yoffset 40
                linear 0.5 yoffset 50 #1.35
                easein 1.0 yoffset 0
        choice(0.3):
            parallel:
                ease 2.5 xoffset -30
                ease 2.5 xoffset 0
            parallel:
                ease 1.5 yoffset 150
                ease 3.5 yoffset 0
        repeat
