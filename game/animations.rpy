init python:

    def call_holder(value, Color, XPOS):
        global number_of_holders

        number_of_holders += 1 if number_of_holders < 10 else -9

        renpy.show_screen("stat_holder_" + str(number_of_holders), value, Color, XPOS)

        return

transform stat_animation(Timer, XPOS):
    alpha 0
    pause Timer
    xpos XPOS ypos 0.25 alpha 1
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
    use stat_graphic(value, Color, 0.0, XPOS - 0.015)
    timer 0.6 action Hide("stat_holder_1")

screen stat_holder_2(value, Color, XPOS):
    use stat_graphic(value, Color, 0.1, XPOS)
    timer 0.7 action Hide("stat_holder_2")

screen stat_holder_3(value, Color, XPOS):
    use stat_graphic(value, Color, 0.2, XPOS + 0.015)
    timer 0.8 action Hide("stat_holder_3")

screen stat_holder_4(value, Color, XPOS):
    use stat_graphic(value, Color, 0.3, XPOS - 0.015)
    timer 0.9 action Hide("stat_holder_4")

screen stat_holder_5(value, Color, XPOS):
    use stat_graphic(value, Color, 0.4, XPOS)
    timer 1.0 action Hide("stat_holder_5")

screen stat_holder_6(value, Color, XPOS):
    use stat_graphic(value, Color, 0.5, XPOS + 0.015)
    timer 1.1 action Hide("stat_holder_6")

screen stat_holder_7(value, Color, XPOS):
    use stat_graphic(value, Color, 0.6, XPOS - 0.015)
    timer 1.2 action Hide("stat_holder_7")

screen stat_holder_8(value, Color, XPOS):
    use stat_graphic(value, Color, 0.7, XPOS)
    timer 1.3 action Hide("stat_holder_8")

screen stat_holder_9(value, Color, XPOS):
    use stat_graphic(value, Color, 0.8, XPOS + 0.015)
    timer 1.4 action Hide("stat_holder_9")

screen stat_holder_10(value, Color, XPOS):
    use stat_graphic(value, Color, 0.9, XPOS - 0.015)
    timer 1.5 action Hide("stat_holder_10")

layeredimage Xavier_sprite:
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

    anchor (0.5, 0.0) offset (60, 355) zoom 0.7

image Xavier_blinking:
    "images/NPC/Xavier_eyes[Xavier_eyes].png"
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
    if face == "_psychic":
        $ Xavier_mouth = "_concentrate"
        $ Xavier_brows = "_concentrate"
        $ Xavier_eyes = "_concentrate"
        $ Xavier_psychic = True
    if face == "_hypno":
        $ Xavier_mouth = "_neutral"
        $ Xavier_brows = "_neutral"
        $ Xavier_eyes = "_hypno"
        $ Xavier_psychic = False
    if face == "_shocked":
        $ Xavier_mouth = "_neutral"
        $ Xavier_brows = "_shocked"
        $ Xavier_eyes = "_shocked"
        $ Xavier_psychic = False
    if face == "_happy":
        $ Xavier_mouth = "_smile"
        $ Xavier_brows = "_happy"
        $ Xavier_eyes = "_happy"
        $ Xavier_psychic = False
    if face == "angry":
        $ Xavier_mouth = "_concentrate"
        $ Xavier_brows = "_concentrate"
        $ Xavier_eyes = "_happy"
        $ Xavier_psychic = False

    return

image black_screen:
    Solid("#000000")

    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

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

    if bg_current == "bg_pool":
        AlphaMask("bg_pool", "images/background/bg_pool_mask.png")

    if entering or bg_current != "bg_classroom":
        Null()
    elif EmmaX.location == "bg_teacher" and "frisky" in EmmaX.recent_history:
        "Emma_sprite standing" pos (0.234, 0.176) zoom 0.387
    elif EmmaX.location == "bg_teacher":
        "Emma_sprite standing" pos (0.349, 0.167) zoom 0.387
    elif EmmaX.location == "bg_desk":
        "Emma_sprite standing" pos (0.333, 0.167) zoom 0.387

    if entering or bg_current != "bg_classroom":
        Null()
    elif StormX.location == "bg_teacher" and "frisky" in StormX.recent_history:
        "Storm_sprite standing" pos (0.234, 0.176) zoom 0.387
    elif StormX.location == "bg_teacher":
        "Storm_sprite standing" pos (0.349, 0.167) zoom 0.387
    elif StormX.location == "bg_desk":
        "Storm_sprite standing" pos (0.333, 0.167) zoom 0.387

    if bg_current == "bg_classroom":
        "images/background/bg_classroom_front.png"

    if bg_current == "bg_classroom" and time_index < 2 and weekday < 5:
        "images/background/bg_classroom_pupils.png"

transform dripping(x_offset = 0, start = 0, transparency = 1.0):
    offset (x_offset, start) alpha transparency
    easeout 0.9 yoffset 350 alpha 0.0

image grool_dripping_animation:
    "images/Wetdrop.png"

    subpixel True
    anchor (0.5, 0.5) alpha 0.0
    block:
        choice:
            pause 1
        choice:
            pause 0.5
        choice:
            dripping(8, 10, 0.8)
            pause 1
        choice:
            pause 0.2
            dripping(3, 15, 0.8)
            pause 0.4
        choice:
            pause 0.4
            dripping(0, 5, 0.8)
        choice:
            pause 0.8
            dripping(6, 0, 0.8)
        repeat

image spunk_dripping_animation:
    "images/SpermdropB.png"

    subpixel True
    anchor (0.5, 0.5) alpha 0.0
    block:
        choice:
            pause 1
        choice:
            pause 0.5
        choice:
            dripping(8, 10)
            pause 1
        choice:
            pause 0.2
            dripping(3, 15)
            pause 0.4
        choice:
            pause 0.4
            dripping(0, 5)
        choice:
            pause 0.8
            dripping(6, 0)
        repeat

image licking:
    subpixel True
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

image dildo:
    "images/DildoIn.png"

    anchor (0.5, 0.5)

image Kitty_dildo_pussy_animation:
    "dildo"

    subpixel True
    block:
        ease 1 yoffset -60
        pause 1
        ease 3 yoffset 0
        repeat

layeredimage Kitty_dildo_pussy_animations:
    always:
        "Kitty_dildo_pussy_animation" pos (0.2923, 0.595) zoom 1.22

image Kitty_dildo_anal_animation:
    "dildo"

    subpixel True
    block:
        ease 1 yoffset -60
        pause 1
        ease 3 yoffset 0
        repeat

layeredimage Kitty_dildo_anal_animations:
    always:
        "Kitty_dildo_anal_animation" pos (0.2925, 0.64)




















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

        AlphaMask("images/dress_screen_shadow.png","dress_screen_shadow")
    zoom 1
    offset (375,225)

image dress_screen_shadow:

    contains:

        ConditionSwitch(
            "RogueX.sprite_layer == 100", "Rogue_sprite standing",
            "KittyX.sprite_layer == 100", "Kitty_sprite standing",
            "EmmaX.sprite_layer == 100", "Emma_sprite standing",
            "LauraX.sprite_layer == 100", "Laura_sprite standing",
            "JeanX.sprite_layer == 100", "Jean_sprite standing",
            "StormX.sprite_layer == 100", "Storm_sprite standing",
            "JubesX.sprite_layer == 100", "Jubes_sprite standing",




            "True", Null(),
            )
        offset (210,-170)
        zoom 1
















image CircleTest:
    contains:
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
        "images/Clockface.png"
        anchor (0.5,0.5)

image ClockWhite:
    contains:
        "images/Clockwhite.png"
        anchor (0.5,0.5)
        rotate -(int(round *3.6))

image ClockRed:
    contains:
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

        AlphaMask("SilhouetteBase","Storm_sprite standing")







transform Vibrate():
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










image VibratorRightBreast:
    contains:
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
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert:
    contains:
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0

image TestUIAnimation:
    contains:
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










image Zero_Chibicock:
    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Player.color == 'White'", "images/Chibi_Cock_P.png",
            "Player.color == 'Black'", "images/Chibi_Cock_B.png",
            "Player.color == 'Green'", "images/Chibi_Cock_G.png",
            "True", Null()))

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
        ConditionSwitch(
            "(Partner == StormX and second_girl_main_action == 'hand') or (focused_Girl == StormX and girl_secondary_action == 'hand')", "images/Chibi_Hand_S.png",
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
            "Player.secondary_action == 'jerking_off'", "Chibi_jerking_off",
            "girl_secondary_action == 'hand' or second_girl_main_action == 'hand'", "Chibi_Handy",
            "second_girl_main_action == 'blow'", "Chibi_Sucking",
            "True", "Chibi_Null",
            )

image night_mask = "images/nightmask.png"

image UI_Backpack = "images/UI_Backpack_idle.png"
image UI_Dildo = "images/UI_Dildo.png"
image UI_VibA = "images/UI_VibA.png"
image UI_VibB = "images/UI_VibB.png"

image UI_PartnerHand:
    ConditionSwitch("Partner == StormX", "images/UI_GirlHandS.png",
            "True", "images/UI_GirlHand.png")
