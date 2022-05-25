init python:

    def call_holder(value, Color, XPOS):
        global number_of_holders

        number_of_holders += 1 if number_of_holders < 10 else -9

        renpy.show_screen("stat_holder_" + str(number_of_holders), value, Color, XPOS)

        return

transform stat_animation(Timer, XPOS):
    alpha 0
    pause Timer
    xpos XPOS ypos 0.15 alpha 1
    parallel:
        linear 1 ypos 0.0
    parallel:
        pause 0.3
        linear 0.3 alpha 0

screen stat_graphic(value, Color, Timer, XPOS):
    showif value > 0:
        text "+[value]" size 30 color Color at stat_animation(Timer, XPOS)
    else:
        text "[value]" size 30 color Color at stat_animation(Timer, XPOS)

screen stat_holder_1(value, Color, XPOS):
    use stat_graphic(value, Color, 0.0, XPOS-30)
    timer 0.6 action Hide("stat_holder_1")

screen stat_holder_2(value, Color, XPOS):
    use stat_graphic(value, Color, 0.1, XPOS)
    timer 0.7 action Hide("stat_holder_2")

screen stat_holder_3(value, Color, XPOS):
    use stat_graphic(value, Color, 0.2, XPOS+30)
    timer 0.8 action Hide("stat_holder_3")

screen stat_holder_4(value, Color, XPOS):
    use stat_graphic(value, Color, 0.3, XPOS-30)
    timer 0.9 action Hide("stat_holder_4")

screen stat_holder_5(value, Color, XPOS):
    use stat_graphic(value, Color, 0.4, XPOS)
    timer 1.0 action Hide("stat_holder_5")

screen stat_holder_6(value, Color, XPOS):
    use stat_graphic(value, Color, 0.5, XPOS+30)
    timer 1.1 action Hide("stat_holder_6")

screen stat_holder_7(value, Color, XPOS):
    use stat_graphic(value, Color, 0.6, XPOS-30)
    timer 1.2 action Hide("stat_holder_7")

screen stat_holder_8(value, Color, XPOS):
    use stat_graphic(value, Color, 0.7, XPOS)
    timer 1.3 action Hide("stat_holder_8")

screen stat_holder_9(value, Color, XPOS):
    use stat_graphic(value, Color, 0.8, XPOS+30)
    timer 1.4 action Hide("stat_holder_9")

screen stat_holder_10(value, Color, XPOS):
    use stat_graphic(value, Color, 0.9, XPOS-30)
    timer 1.5 action Hide("stat_holder_10")

layeredimage Xavier_Sprite:
    always:
        "images/NPC/Xavier_body.png"

    always:
        "images/NPC/Xavier_brows[Xavier_brows].png"

    always:
        "images/NPC/Xavier_mouth[Xavier_mouth].png"

    always:
        "Xavier_blinking"

    if Xavier_psychic:
        "images/NPC/Xavier_psychic.png"

    size (429, 521) anchor (0.5, 0) offset (0, 150) zoom 1.1

layeredimage Xavier_eyes:
    always:
        "images/NPC/Xavier_eyes[Xavier_eyes].png"

image Xavier_blinking:
    "Xavier_eyes"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/NPC/Xavier_eyes_closed.png"
    0.25
    repeat

label change_Xavier_face(face = Xavier_emotion):
    if face == "psychic":
        $ Xavier_mouth = "concentrate"
        $ Xavier_brows = "concentrate"
        $ Xavier_eyes = "concentrate"
        $ Xavier_psychic = 1
    if face == "hypno":
        $ Xavier_mouth = "neutral"
        $ Xavier_brows = "neutral"
        $ Xavier_eyes = "hypno"
    if face == "shocked":
        $ Xavier_mouth = "neutral"
        $ Xavier_brows = "shocked"
        $ Xavier_eyes = "shocked"
        $ Xavier_psychic = 0
    if face == "_happy":
        $ Xavier_mouth = "_happy"
        $ Xavier_brows = "_happy"
        $ Xavier_eyes = "_happy"
        $ Xavier_psychic = 0
    if face == "angry":
        $ Xavier_mouth = "concentrate"
        $ Xavier_brows = "concentrate"
        $ Xavier_eyes = "_happy"
        $ Xavier_psychic = 0

    return

layeredimage background:
    always:
        "images/background/sky_[current_time].png"

    if entering:
        "images/background/bg_entry.png"

    if entering:
        Null()
    elif bg_current not in ["bg_campus", "bg_study", "bg_storm",  "bg_pool", "bg_mall"]:
        "images/background/[bg_current].png"
    else:
        "images/background/[bg_current]_[current_time].png"

    if entering or bg_current != "bg_classroom":
        Null()
    elif EmmaX.location == "bg_teacher" and "frisky" in EmmaX.recent_history:
        "Emma_Behind_Podium"
    elif EmmaX.location == "bg_teacher":
        "Emma_At_Podium"
    elif EmmaX.location == "bg_desk":
        "Emma_At_Desk"

    if entering or bg_current != "bg_classroom":
        Null()
    elif StormX.location == "bg_teacher" and "frisky" in StormX.recent_history:
        "Storm_Behind_Podium"
    elif StormX.location == "bg_teacher":
        "Storm_At_Podium"
    elif StormX.location == "bg_desk":
        "Storm_At_Desk"

    if not entering and bg_current == "bg_classroom":
        "images/background/bg_classroom_front.png"

    if not entering and bg_current == "bg_classroom" and time_index < 2 and weekday < 5:
        "images/background/bg_classroom_pupils.png"

    size (1024, 768)

image grool_dripping:
    contains:
        "images/Wetdrop.png"
        zoom 0.2 alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                grool_drip (254, 560, 70)
                pause 1
            choice:
                pause 0.2
                grool_drip (249, 560, 75)
                pause 0.4
            choice:
                pause 0.4
                grool_drip (246, 560, 65)
            choice:
                pause 0.8
                grool_drip (252, 560, 60)
            repeat

image heavy_grool_dripping:
    contains:
        "images/Wetdrop.png"
        zoom 0.2
        parallel:
            grool_drip(254, 560, 70)
            pause 1.5
            repeat

    contains:
        "images/Wetdrop.png"
        zoom 0.2
        parallel:
            pause 0.3
            grool_drip(249, 560, 75)
            pause 0.6
            repeat

    contains:
        "images/Wetdrop.png"
        zoom 0.2
        parallel:
            pause 0.6
            grool_drip(246, 560, 65)
            repeat

    contains:
        "images/Wetdrop.png"
        zoom 0.2
        parallel:
            pause 0.8
            grool_drip(252, 560, 60)
            pause 0.2
            repeat

transform grool_drip(x_position, y_position, start):
    pos (x_position, x_position)
    alpha 0.8
    easeout 0.9 ypos y_position + start
    easeout 0.9 ypos y_position + 350
    alpha 0

image spunk_dripping:
    contains:
        "images/SpermdropB.png"
        zoom 0.3 alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                spunk_drip(240, 560, 70)
                pause 1
            choice:
                pause 0.2
                spunk_drip (249, 560, 75)
                pause 0.4
            choice:
                pause 0.4
                spunk_drip (246, 560, 65)
            choice:
                pause 0.8
                spunk_drip (252, 560, 60)
            repeat

image heavy_spunk_dripping:
    contains:
        "images/SpermdropB.png"
        zoom 0.3
        parallel:
            spunk_drip(240, 560, 70)
            pause 1
            repeat
    contains:
        "images/SpermdropB.png"
        zoom 0.3
        parallel:
            pause 0.2
            spunk_drip (249, 560, 75)
            pause 0.4
            repeat
    contains:
        "images/SpermdropB.png"
        zoom 0.3
        parallel:
            pause 0.4
            spunk_drip (246, 560, 65)
            repeat
    contains:
        "images/SpermdropB.png"
        zoom 0.3
        parallel:
            pause 0.8
            spunk_drip (252, 560, 60)
            repeat

transform spunk_drip(x_position, y_position, start):
    pos (x_position, x_position)
    alpha 1
    easeout 2.5 ypos y_position + start
    easeout 0.9 ypos y_position + 350
    alpha 0

image licking:
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



















image cellphone:
    "images/cellphone.png"
    xoffset 0
    yoffset 100


image PhoneSex:

    contains:

        "images/PhoneFrame.png"
    contains:

        AlphaMask("PhoneScreen", "images/PhoneMask.png")
    offset (300,50)

image PhoneRG:

    "bg_rogue"
    xoffset 500

image PhoneScreen:
    contains:
        ConditionSwitch(
            "focused_Girl.location == 'bg_rogue'","PhoneRG",
            "True", "[focused_Girl.location]")

        offset (-800,-300)
        zoom 1.5

    contains:
        "[focused_Girl.Tag]_sprite"
        pos (0,0)
        offset (290,50)
        anchor (0.6,0)
        zoom 1.1


image dress_screen:

    contains:

        "images/dress_screen.png"
    contains:

        AlphaMask("images/dress_screenShadow.png","DressShadow")
    zoom 1
    offset (375,225)

image DressShadow:

    contains:

        ConditionSwitch(
            "RogueX.sprite_layer == 100", "Rogue_sprite",
            "KittyX.sprite_layer == 100", "Kitty_sprite",
            "EmmaX.sprite_layer == 100", "Emma_Sprite",
            "LauraX.sprite_layer == 100", "Laura_Sprite",
            "JeanX.sprite_layer == 100", "Jean_Sprite",
            "StormX.sprite_layer == 100", "Storm_Sprite",
            "JubesX.sprite_layer == 100", "Jubes_Sprite",




            "True", Null(),
            )
        offset (210,-170)
        zoom 1





image Gwen_Sprite:
    LiveComposite(
        (574,964),

        (0,0), "images/GS_B.png",


        (80,15), "Gwen_Sprite_Head",
        )
    anchor (0.6, 0.0)
    yoffset 15
    zoom 0.75



image Gwen_Sprite_Head:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(

                "G_Blush", "images/NPC/Gwen_Sprite_Head_Blush.png",
                "True", "images/NPC/Gwen_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "G_mouth == 'open'", "images/NPC/Gwen_Sprite_mouth_Open.png",
            "G_mouth == 'kiss'", "images/NPC/Gwen_Sprite_mouth_Kiss.png",
            "G_mouth == 'smile'", "images/NPC/Gwen_Sprite_mouth_Smile.png",
            "G_mouth == 'shocked'", "images/NPC/Gwen_Sprite_mouth_Shocked.png",
            "True", "images/NPC/Gwen_Sprite_mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(

            "G_Blush", ConditionSwitch(
                    "G_brows == 'angry' or G_eyes == 'angry'", "images/NPC/Gwen_Sprite_brows_Angry_B.png",
                    "G_brows == 'sad'", "images/NPC/Gwen_Sprite_brows_Sad_B.png",
                    "True", "images/NPC/Gwen_Sprite_brows_Normal.png",
                    ),
            "True", ConditionSwitch(
                    "G_brows == 'angry' or G_eyes == 'angry'", "images/NPC/Gwen_Sprite_brows_Angry.png",
                    "G_brows == 'sad'", "images/NPC/Gwen_Sprite_brows_Sad.png",
                    "True", "images/NPC/Gwen_Sprite_brows_Normal.png",
                    ),
            ),
        (0,0), "Gwen Blink",
        )
    anchor (0.6, 0.0)
    zoom 0.5

image Gwen Blink:
    ConditionSwitch(
    "G_eyes == 'angry'", "images/NPC/Gwen_Sprite_eyes_Angry.png",
    "G_eyes == 'surprised'", "images/NPC/Gwen_Sprite_eyes_Surprised.png",
    "G_eyes == 'closed'", "images/NPC/Gwen_Sprite_eyes_Closed.png",
    "True", "images/NPC/Gwen_Sprite_eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/NPC/Gwen_Sprite_eyes_Closed.png"
    0.20
    repeat

default G_mouth = "normal"
default G_brows = "normal"
default G_eyes = "normal"
default G_Blush = 0

label GwenFace(emotion="normal", B=G_Blush, M=0, mouth=0, eyes=0, brows=0):


    $ B = G_Blush if B == 5 else B

    if emotion == "normal":
        $ G_mouth = "normal"
        $ G_brows = "normal"
        $ G_eyes = "normal"
    elif emotion == "angry":
        $ G_mouth = "_kiss"
        $ G_brows = "angry"
        $ G_eyes = "angry"
    elif emotion == "closed":
        $ G_mouth = "normal"
        $ G_brows = "_sad"
        $ G_eyes = "closed"
    elif emotion == "_sad":
        $ G_mouth = "_kiss"
        $ G_brows = "_sad"
        $ G_eyes = "normal"
    elif emotion == "smile":
        $ G_mouth = "smile"
        $ G_brows = "normal"
        $ G_eyes = "normal"
    elif emotion == "surprised":
        $ G_mouth = "open"
        $ G_brows = "normal"
        $ G_eyes = "surprised"
    elif emotion == "shocked":
        $ G_mouth = "shocked"
        $ G_brows = "normal"
        $ G_eyes = "surprised"

    if B > 1:
        $ G_Blush = 2
    elif B:
        $ G_Blush = 1
    else:
        $ G_Blush = 0

    if mouth:
        $ G_mouth = mouth
    if eyes:
        $ G_eyes = eyes
    if brows:
        $ G_brows = brows

    return

label Gwen_FaceEditor:
    while True:
        menu:
            "brows=[G_brows], eyes=[G_eyes], mouth=[G_mouth]"
            "Toggle brows":
                if G_brows == "normal":
                    $ G_brows = "angry"
                elif G_brows == "angry":
                    $ G_brows = "_confused"
                elif G_brows == "_confused":
                    $ G_brows = "_sad"
                elif G_brows == "_sad":
                    $ G_brows = "surprised"
                else:
                    $ G_brows = "normal"
            "Toggle eyes Emotions":
                if G_eyes == "normal":
                    $ G_eyes = "surprised"
                elif G_eyes == "surprised":
                    $ G_eyes = "sexy"
                elif G_eyes == "sexy":
                    $ G_eyes = "squint"
                elif G_eyes == "squint":
                    $ G_eyes = "closed"
                else:
                    $ G_eyes = "normal"
            "Toggle eyes Directions":
                if G_eyes == "normal":
                    $ G_eyes = "side"
                elif G_eyes == "side":
                    $ G_eyes = "down"
                elif G_eyes == "down":
                    $ G_eyes = "leftside"
                elif G_eyes == "leftside":
                    $ G_eyes = "stunned"
                else:
                    $ G_eyes = "normal"
            "Toggle mouth Normal":
                if G_mouth  == "normal":
                    $ G_mouth = "_sad"
                elif G_mouth == "_sad":
                    $ G_mouth = "smile"
                elif G_mouth == "smile":
                    $ G_mouth = "surprised"
                else:
                    $ G_mouth = "normal"
            "Toggle mouth Sexy":
                if G_mouth  == "normal":
                    $ G_mouth = "_kiss"
                elif G_mouth == "kiss":
                    $ G_mouth = "_sucking"
                elif G_mouth == "_sucking":
                    $ G_mouth = "_tongue"
                elif G_mouth == "_tongue":
                    $ G_mouth = "_lipbite"
                else:
                    $ G_mouth = "normal"
            "Toggle Blush":
                if G_Blush == 1:
                    $ G_Blush = 2
                elif G_Blush:
                    $ G_Blush = 0
                else:
                    $ G_Blush = 1
            "Back":

                return














label Display_Gwen(GwLoc=350, YLoc=50):



    show Gwen_Sprite:
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.5, 0.0)
        easeout 0.5 pos (GwLoc,YLoc)
    show Gwen_Sprite:
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.5, 0.0)
        pos (GwLoc,YLoc)
    return


label Close_Launch(GirlA=0, GirlB=0, XLoc=0, YLoc=0, XZoom=0):



    if GirlB:
        $ temp_Girls = [GirlA,GirlB]
    elif GirlA:
        $ temp_Girls = [GirlA]
    while temp_Girls:
        if temp_Girls[0] == KittyX or temp_Girls[0] == LauraX:
            $ temp_Girls[0].arm_pose = 1
        else:
            $ temp_Girls[0].arm_pose = 2
        $ YLoc = 100
        if GirlA == temp_Girls[0]:

            if temp_Girls[0] == KittyX:
                $ XLoc = 450
            elif temp_Girls[0] == RogueX:
                $ XLoc = 550
            else:
                $ XLoc = 500
            $ temp_Girls[0].sprite_layer = 100
            $ XZoom = -1.3
        elif GirlB == temp_Girls[0]:

            if temp_Girls[0] == EmmaX or LauraX:
                $ XLoc = 700
            else:
                $ XLoc = 715
            $ temp_Girls[0].sprite_layer = 75
            $ XZoom = 1.3

        if temp_Girls[0] == RogueX:
            call hide_girl(RogueX)
            show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == KittyX:
            call hide_girl(KittyX)
            show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == EmmaX:
            call Emma_Hide
            show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == LauraX:
            call Laura_Hide
            show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == JeanX:
            call Jean_Hide
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == StormX:
            call Storm_Hide
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == JubesX:
            call Jubes_Hide
            show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        $ temp_Girls.remove(temp_Girls[0])
    return
















label Les_Launch(Girl=0, XLoc=0, YLoc=0, XZoom=0, temp_Girls=[]):



    if Partner not in all_Girls:
        return
    $ temp_Girls = [Girl,Partner]
    while temp_Girls:
        if "unseen" in temp_Girls[0].recent_history:
            $ temp_Girls[0].eyes = "closed"
        elif Girl == temp_Girls[0]:
            if Girl == RogueX:
                $ temp_Girls[0].eyes = "side"
            elif Girl == EmmaX:
                $ temp_Girls[0].eyes = "_sly"
            else:
                $ temp_Girls[0].eyes = "leftside"
        else:
            $ temp_Girls[0].eyes = "side"

        if temp_Girls[0] == KittyX or temp_Girls[0] == LauraX:
            $ temp_Girls[0].arm_pose = 1
        else:
            $ temp_Girls[0].arm_pose = 2
        $ YLoc = 100
        if Girl == temp_Girls[0]:

            if temp_Girls[0] == KittyX:
                $ XLoc = 450
            elif temp_Girls[0] == RogueX:
                $ XLoc = 550
            else:
                $ XLoc = 500
            $ temp_Girls[0].sprite_layer = 100
            $ XZoom = -1.3
        else:

            if temp_Girls[0] == EmmaX or LauraX:
                $ XLoc = 700
            else:
                $ XLoc = 715
            if temp_Girls[0] == KittyX:
                if RogueX in (Partner,Girl):
                    $ KittyX.sprite_layer = 100
                else:
                    $ KittyX.sprite_layer = 25
            else:
                $ temp_Girls[0].sprite_layer = 75
            $ XZoom = 1.3

        if temp_Girls[0] == RogueX:
            call hide_girl(RogueX)
            show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == KittyX:
            call hide_girl(KittyX)
            show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == EmmaX:
            call Emma_Hide
            show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == LauraX:
            call Laura_Hide
            show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == JeanX:
            call Jean_Hide
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif temp_Girls[0] == StormX:
            call Storm_Hide
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif temp_Girls[0] == JubesX:
            call Jubes_Hide
            show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        $ temp_Girls.remove(temp_Girls[0])
    return

image CircleTest:
    contains:
        subpixel True
        "images/Clockbase.png"
        anchor (0.5,0.5)

        yzoom -1
    contains:

        ConditionSwitch(
            "round>= 50", "ClockWhite",
            "True",Null(),
            ),
    contains:
        ConditionSwitch(
            "round<= 50", "ClockRed",
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
        rotate -(int(round *3.6))

image ClockRed:
    contains:
        subpixel True
        "images/Clockred.png"
        anchor (0.5,0.5)
        rotate -(int(round *3.6-180))

image blue_screen:

    alpha 0.1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))

image SilhouetteBase:

    alpha 0.95
    contains:
        Solid("#14142d", xysize=(1024, 768))


image Silhouettes:





    contains:

        AlphaMask("SilhouetteBase","Storm_Sprite")







transform Vibrate():
    subpixel True
    block:
        linear 0.5 xoffset 2
        linear 0.5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite(
        (224,224),
        (0,0), ConditionSwitch(
            "not Vibration", "UI_VibA",
            "Vibration", At("UI_VibB", Vibrate()),
            ),
        )

image GropeLeftBreast:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.7
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
            ease 0.5 rotate -45 pos (150,370)
            pause 0.5
            ease 1.5 rotate 30 pos (160,400)
            repeat

image LickLeftBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (280,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -45 pos (260,380)
            pause 0.5
            ease 1.5 rotate 30 pos (280,410)
            repeat

image GropeThigh:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.7
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause 0.5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause 0.5
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            repeat

image GropePussy:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.7
        pos (220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease 0.5 rotate 190 pos (220,620)
                ease 0.75 rotate 170 pos (220,635)
            choice:
                ease 0.5 rotate 190 pos (220,620)
                pause 0.25
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
                pause 0.5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease 0.5 rotate 40 pos (240,685)
                pause 0.5
                ease 1.75 rotate 50 pos (230,720)
            choice:
                ease 2 rotate 40 pos (240,685)
                pause 0.5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease 0.25 rotate 40 pos (240,685)
                ease 0.25 rotate 50 pos (230,720)
                ease 0.25 rotate 40 pos (240,685)
                ease 0.25 rotate 50 pos (230,720)
            repeat

image Lickpussy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (250,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout 0.5 rotate -50 pos (230,650)
            linear 0.5 rotate -60 pos (220,660)
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
            pause 0.25
            ease 1 rotate 55 ypos 380
            pause 0.25
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
            pause 0.25
            ease 1 rotate 55 ypos 400
            pause 0.25
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
            pause 0.25
            ease 1 rotate 70 xpos 240 ypos 665
            pause 0.25
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
            pause 0.25
            ease 1 rotate 10 xpos 270 ypos 665
            pause 0.25
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
            pause 0.25
            ease 1 rotate 10 xpos 270 ypos 665
            pause 0.25
            repeat


image GirlGropeLeftBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (300,400)
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
        pos (160,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -30 pos (160,410)
            ease 1 rotate -10 pos (160,380)
            repeat

image GirlGropeThigh:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause 0.5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause 0.5
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            repeat

image GirlGropePussy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (230,615)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (225,620)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (225,620)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 pos (225,620)
                ease 0.75 rotate 200 pos (225,625)
                ease 0.5 rotate 205 pos (225,620)
                ease 0.75 rotate 200 pos (225,625)
            choice:
                ease 0.3 rotate 205 pos (225,620)
                ease 0.3 rotate 200 pos (225,630)
                ease 0.3 rotate 205 pos (225,620)
                ease 0.3 rotate 200 pos (225,630)
            repeat

image GirlFingerPussy:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom 0.6
        pos (230,630)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (230,635)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (230,635)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 pos (230,635)
                ease 0.75 rotate 200 pos (230,640)
                ease 0.5 rotate 205 pos (230,635)
                ease 0.75 rotate 200 pos (230,640)
            choice:
                ease 0.3 rotate 205 pos (230,635)
                ease 0.3 rotate 200 pos (230,645)
                ease 0.3 rotate 205 pos (230,635)
                ease 0.3 rotate 200 pos (230,645)
            repeat





image Spunk_Drip:

    contains:
        "images/SpermdropB.png"
        zoom 0.3
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout 0.9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause 0.2
                alpha 1
                easeout 2.5 ypos 75
                easeout 0.9 ypos 350
                alpha 0
                pause 0.4
            choice:
                pos (6,0)
                pause 0.4
                alpha 1
                easeout 2.5 ypos 65
                easeout 0.9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause 0.8
                alpha 1
                easeout 2.5 ypos 60
                easeout 0.9 ypos 350
                alpha 0
            repeat

image Spunk_Drip2:

    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (0,0)
            alpha 1
            easeout 2.5 ypos 70
            easeout 0.9 ypos 350
            alpha 0
            pause 1
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (9,0)
            pause 0.2
            alpha 1
            easeout 2.5 ypos 75
            easeout 0.9 ypos 350
            alpha 0
            pause 0.4
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (6,0)
            pause 0.4
            alpha 1
            easeout 2.5 ypos 65
            easeout 0.9 ypos 350
            alpha 0
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (12,0)
            pause 0.8
            alpha 1
            easeout 2.5 ypos 60
            easeout 0.9 ypos 350
            alpha 0
            repeat


image Spunk_Dripp:

    contains:
        "images/SpermdropP.png"
        zoom 0.3
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout 0.9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause 0.2
                alpha 1
                easeout 2.5 ypos 75
                easeout 0.9 ypos 350
                alpha 0
                pause 0.4
            choice:
                pos (6,0)
                pause 0.4
                alpha 1
                easeout 2.5 ypos 65
                easeout 0.9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause 0.8
                alpha 1
                easeout 2.5 ypos 60
                easeout 0.9 ypos 350
                alpha 0
            repeat

image Wet_Drip:

    contains:
        "images/Wetdrop.png"
        zoom 0.2
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause 0.5
            choice:
                pos (14,0)
                alpha 0.8
                easeout 0.9 ypos 70
                easeout 0.9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause 0.2
                alpha 0.8
                easeout 0.9 ypos 75
                easeout 0.9 ypos 350
                alpha 0
                pause 0.4
            choice:
                pos (6,0)
                pause 0.4
                alpha 0.8
                easeout 0.9 ypos 65
                easeout 0.9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause 0.8
                alpha 0.8
                easeout 0.9 ypos 60
                easeout 0.9 ypos 350
                alpha 0
            repeat

image Wet_Drip2:

    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (14,0)
            alpha 0.8
            easeout 0.9 ypos 70
            easeout 0.9 ypos 350
            alpha 0
            pause 1.5
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (9,0)
            pause 0.3
            alpha 0.8
            easeout 0.9 ypos 75
            easeout 0.9 ypos 350
            alpha 0
            pause 0.6
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (6,0)
            pause 0.6
            alpha 0.8
            easeout 0.9 ypos 65
            easeout 0.9 ypos 350
            alpha 0
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (12,0)
            pause 0.8
            alpha 0.8
            easeout 0.9 ypos 60
            easeout 0.9 ypos 350
            alpha 0
            pause 0.2
            repeat


image Zero_Chibicock:
    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Player.color == 'White'", "images/Chibi_Cock_P.png",
            "Player.color == 'Black'", "images/Chibi_Cock_B.png",
            "Player.color == 'Green'", "images/Chibi_Cock_G.png",
            "True", Null(),
            ),








        )
    anchor (0.5,0.5)



image Chibi_Null:

    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    pos (75,675)
    zoom 0.5

image Chibi_jerking_off:

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
            ease 0.3 rotate -10 pos (0,50)
            ease 0.7 rotate 20 pos (-10,-80)
            repeat
    pos (75,675)
    zoom 0.5

image Chibi_Handy:

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

        pos (0,-110)
        anchor (0.5,0.5)
        rotate -10
        block:
            ease 0.3 rotate 0 pos (10,10)
            ease 0.7 rotate -10 pos (0,-130)
            repeat
    pos (75,675)
    zoom 0.5

image Chibi_mouth_Mask:
    "images/Chibi_mouth_Mask.png"
    anchor (0.5,0.5)

image Chibi_mouth_Rogue:
    "images/Chibi_mouth_R.png"
    anchor (0.5,0.5)
image Chibi_mouth_Kitty:
    "images/Chibi_mouth_K.png"
    anchor (0.5,0.5)
image Chibi_mouth_Emma:
    "images/Chibi_mouth_E.png"
    anchor (0.5,0.5)
image Chibi_mouth_Storm:
    "images/Chibi_mouth_S.png"
    anchor (0.5,0.5)

image Chibi_Sucking:

    contains:
        "Chibi_SuckingB"
    pos (75,675)

image Chibi_SuckingB:

    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Partner == RogueX", "Chibi_mouth_Rogue",
            "Partner == EmmaX", "Chibi_mouth_Emma",
            "Partner == StormX", "Chibi_mouth_Storm",
            "True", "Chibi_mouth_Kitty"
            ),
        (0,0), AlphaMask("Chibi_Sucking_Cock", "Chibi_mouth_Mask")
        )
    subpixel True
    pos (7,0)
    anchor (0.5,0.5)
    zoom 0.5
    xzoom 0.71
    block:
        easeout 0.25 rotate 0 pos (2,48) xzoom 1
        easein 0.25 rotate 0 pos (6,92) xzoom 1
        easeout 0.5 rotate 0 pos (2,48) xzoom 1
        easein 0.5 rotate 0 pos (5,0) xzoom 0.71
        repeat

image Chibi_Sucking_Cock:

    contains:
        subpixel True
        "Zero_Chibicock"
        pos (100,175)
        xzoom 1.5
        anchor (0.5,0.5)

        rotate 0
        block:
            easeout 0.25 rotate 0 pos (110,80) xzoom 1
            easein 0.25 rotate 0 pos (100,-10) xzoom 1
            easeout 0.5 rotate 0 pos (110,80) xzoom 1
            easein 0.5 rotate 0 pos (100,175) xzoom 1.5
            repeat




image Chibi_UI:

    contains:
        ConditionSwitch(
            "'cockout' not in Player.recent_history", Null(),
            "offhand_action == 'jerking_off'", "Chibi_jerking_off",
            "girl_offhand_action == 'hand' or second_girl_primary_action == 'hand'", "Chibi_Handy",
            "second_girl_primary_action == 'blow'", "Chibi_Sucking",
            "True", "Chibi_Null",
            )
