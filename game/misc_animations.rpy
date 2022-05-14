image Dildo_Animation:
    contains:
        "UI_Dildo"
        block:
            ease 1 pos (100,300) #pos (0,50)
            ease 1 pos (100,400) #pos (0,0)
            repeat

image AssBase:                  #This is the base image, used in masks
    "images/RogueDoggy/Rogue_Doggy_Ass.png"

image Spunk_Drip:
        #the minor dripping animation
        contains:
            "images/SpermdropB.png"
            zoom 0.3
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (0,0)
                    alpha 1
                    easeout 2.5 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha 1
                    easeout 2.5 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha 1
                    easeout 2.5 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha 1
                    easeout 2.5 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat

image Spunk_Drip2:
        #Dripping spunk
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1
                repeat
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (9,0)
                pause .2
                alpha 1
                easeout 2.5 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .4
                repeat
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (6,0)
                pause .4
                alpha 1
                easeout 2.5 ypos 65
                easeout .9 ypos 350
                alpha 0
                repeat
        contains:
            "images/SpermdropB.png"
            pos (0,0)
            zoom 0.3
            parallel:
                pos (12,0)
                pause .8
                alpha 1
                easeout 2.5 ypos 60
                easeout .9 ypos 350
                alpha 0
                repeat


image Spunk_Dripp:
        #the minor dripping animation
        contains:
            "images/SpermdropP.png"
            zoom 0.3
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (0,0)
                    alpha 1
                    easeout 2.5 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha 1
                    easeout 2.5 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha 1
                    easeout 2.5 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha 1
                    easeout 2.5 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat

image Wet_Drip:
        #the minor dripping animation
        contains:
            "images/Wetdrop.png"
            zoom 0.2
            alpha 0
            block:
                choice:
                    pause 1
                choice:
                    pause .5
                choice:
                    pos (14,0)
                    alpha .8
                    easeout .9 ypos 70
                    easeout .9 ypos 350
                    alpha 0
                    pause 1
                choice:
                    pos (9,0)
                    pause .2
                    alpha .8
                    easeout .9 ypos 75
                    easeout .9 ypos 350
                    alpha 0
                    pause .4
                choice:
                    pos (6,0)
                    pause .4
                    alpha .8
                    easeout .9 ypos 65
                    easeout .9 ypos 350
                    alpha 0
                choice:
                    pos (12,0)
                    pause .8
                    alpha .8
                    easeout .9 ypos 60
                    easeout .9 ypos 350
                    alpha 0
                repeat

image Wet_Drip2:
        #The dripping wetness animation at 2x speed
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (14,0)
                alpha .8
                easeout .9 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1.5
                repeat
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (9,0)
                pause .3
                alpha .8
                easeout .9 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .6
                repeat
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (6,0)
                pause .6
                alpha .8
                easeout .9 ypos 65
                easeout .9 ypos 350
                alpha 0
                repeat
        contains:
            "images/Wetdrop.png"
            pos (0,0)
            zoom 0.2
            parallel:
                pos (12,0)
                pause .8
                alpha .8
                easeout .9 ypos 60
                easeout .9 ypos 350
                alpha 0
                pause .2
                repeat


transform Vibrate():
    subpixel True
    block:
        linear .5 xoffset 2
        linear .5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite(
        (224,224),
        (0,0), ConditionSwitch(
            "not Vibration", "UI_VibA",
            "Vibration", At("UI_VibB", Vibrate()),
            ),
        )



image CircleTest:
    contains:
        subpixel True
        "images/Clockbase.png"
        anchor (0.5,0.5)
#        rotate 180
        yzoom -1

    contains:
         ConditionSwitch(
            "Round>= 50", "ClockWhite",
            "True",Null(),
            ),
    contains:
         ConditionSwitch(
            "Round<= 50", "ClockRed",
            "True",Null(),
            ),
    contains:
        subpixel True
        "images/Clockface.png"
        anchor (0.5,0.5)

image ClockWhite:
    contains:
        subpixel True
        "images/Clockwhite.png"
        anchor (0.5,0.5)
        rotate -(int(Round *3.6))

image ClockRed:
    contains:
        subpixel True
        "images/Clockred.png"
        anchor (0.5,0.5)
        rotate -(int(Round *3.6-180))

image BlueScreen:
    #used by Historia
    alpha .1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))

image SilhouetteBase:
    #used by silhouettes
    alpha .95
    contains:
        Solid("#14142d", xysize=(1024, 768))


image Silhouettes:
    #this is dressing screen displayed during wardrobe

#    contains:
##        #screen
#        "SilhouetteBase"
    contains:
#        #screen
        AlphaMask("SilhouetteBase","Storm_Sprite") #tried to use master layer as a mask?



image Cellphone:
    "images/Cellphone.png"
    xoffset 0 #-250
    yoffset 100


image PhoneSex: #rkeljsv
    #this is the phone displayed during phone sex
    contains:
        #base
        "images/PhoneFrame.png"
    contains:
        #screen
        AlphaMask("PhoneScreen", "images/PhoneMask.png")
    offset (300,50)

image PhoneRG:
    #Rogue's room for the phone (to make sure the bed is framed properly)
    "bg_rogue"
    xoffset 500

image PhoneScreen:
    #this is the screen displayed on "PhoneSex", alpha-masked
    contains:
        #backdrop
        ConditionSwitch(
            "focused_Girl.Loc == 'bg rogue'","PhoneRG",
            "focused_Girl.Loc == 'bg kitty'", "bg_kitty",
            "focused_Girl.Loc == 'bg emma'", "bg_emma",
            "focused_Girl.Loc == 'bg laura'", "bg_laura",
            "focused_Girl.Loc == 'bg jean'", "bg_jean",
            "focused_Girl.Loc == 'bg storm'", "bg_storm",
            "focused_Girl.Loc == 'bg jubes'", "bg_jubes",
            "focused_Girl.Loc == 'bg classroom'", "bg_class",
            "focused_Girl.Loc == 'bg teacher'", "bg_class",
            "True", "bg_shower",
            )
        offset (-800,-300)
        zoom 1.5
    contains:
        #girl
        ConditionSwitch(
            "focused_Girl.Tag == 'Rogue'", "Rogue_Sprite",
            "focused_Girl.Tag == 'Kitty'", "Kitty_Sprite",
            "focused_Girl.Tag == 'Emma'", "Emma_Sprite",
            "focused_Girl.Tag == 'Laura'", "Laura_Sprite",
            "focused_Girl.Tag == 'Jean'", "Jean_Sprite",
            "focused_Girl.Tag == 'Storm'", "Storm_Sprite",
            "focused_Girl.Tag == 'Jubes'", "Jubes_Sprite",
            "True", Null(),
            )
        pos (0,0)
        offset (290,50)
        anchor (0.6,0)
        zoom 1.1


image DressScreen:
    #this is dressing screen displayed during wardrobe
    contains:
        #base
        "images/DressScreen.png"
    contains:
        #screen
        AlphaMask("images/DressScreenShadow.png","DressShadow")
    zoom 1
    offset (375,225)

image DressShadow:
    #this is the shadow projected on that screen
    contains:
        #girl
        ConditionSwitch(
            "RogueX.Layer == 100", "Rogue_Sprite",
            "KittyX.Layer == 100", "Kitty_Sprite",
            "EmmaX.Layer == 100", "Emma_Sprite",
            "LauraX.Layer == 100", "Laura_Sprite",
            "JeanX.Layer == 100", "Jean_Sprite",
            "StormX.Layer == 100", "Storm_Sprite",
            "JubesX.Layer == 100", "Jubes_Sprite",
#            "focused_Girl == RogueX", "Rogue_Sprite",
#            "focused_Girl == 'Kitty'", "Kitty_Sprite",
#            "focused_Girl == 'Emma'", "Emma_Sprite",
#            "focused_Girl == 'Laura'", "Laura_Sprite",
            "True", Null(),
            )
        offset (210,-170)
        zoom 1
