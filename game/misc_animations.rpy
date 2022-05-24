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
