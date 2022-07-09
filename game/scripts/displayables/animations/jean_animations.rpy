image Jean_blinking:
    "images/Jean_standing/Jean_standing_eyes_[JeanX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jean_standing/Jean_standing_eyes_sexy.png"
    0.05
    "images/Jean_standing/Jean_standing_eyes_closed.png"
    0.15
    "images/Jean_standing/Jean_standing_eyes_sexy.png"
    0.05
    repeat

layeredimage Jean_standing_fondling_animations:
    if JeanX.primary_Action.Target != JeanX:
        Null()
    elif JeanX.primary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.185, 0.625)
    elif JeanX.primary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.262, 0.985)
    elif JeanX.primary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.27, 1.04)

    if JeanX.secondary_Action.Target != JeanX:
        Null()
    elif JeanX.secondary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_left_animation" pos (0.305, 0.635)
    elif JeanX.secondary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.262, 0.985)
    elif JeanX.secondary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.27, 1.04)

    if Player.primary_Action.Target != JeanX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.225, 1.22)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.282, 0.61)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.295, 0.565)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.26, 0.98)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.245, 1.15)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.275, 1.07)

    if Player.secondary_Action.Target != JeanX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.225, 1.22)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.23, 0.625)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.17, 0.57)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.26, 0.98)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.245, 1.15)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.275, 1.07)

image Jean_handjob_under_hand_animation0:
    "Jean_handjob_under"

image Jean_handjob_under_hand_animation1:
    animation
    "Jean_handjob_under"

    subpixel True
    rotate 10
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset 0 rotate 10
        pause 0.1
        repeat

image Jean_handjob_under_hand_animation2:
    animation
    "Jean_handjob_under"

    subpixel True
    rotate 8
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset 0 rotate 8
        pause 0.1
        repeat

image Jean_handjob_over_hand_animation0:
    "Jean_handjob_over"

image Jean_handjob_over_hand_animation1:
    animation
    "Jean_handjob_over"

    subpixel True
    rotate 10
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset 0 rotate 10
        pause 0.1
        repeat

image Jean_handjob_over_hand_animation2:
    animation
    "Jean_handjob_over"

    subpixel True
    rotate 8
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset 0 rotate 8
        pause 0.1
        repeat

layeredimage Jean_sprite handjob:
    always:
        "Jean_sprite standing"

    always:
        "Jean_handjob_under_hand_animation[JeanX.primary_Action.speed]" pos (0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Jean"

    always:
        "Jean_handjob_over_hand_animation[JeanX.primary_Action.speed]" pos (0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (240, -220) zoom 2.5

image Jean_titjob_bra_back_animation0:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_bra_back_animation1:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 1.9 ypos -20
        pause 0.4
        ease 1.8 ypos 150
        ease 0.5 ypos 140
        repeat

image Jean_titjob_bra_back_animation2:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jean_titjob_bra_back_animation3:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        pause 0.2
        ease 1.9 yoffset 80
        pause 0.2
        ease 1.9 yoffset 90
        repeat

image Jean_titjob_bra_back_animation5:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 80
        pause 0.2
        ease 2 yoffset 90
        pause 0.4
        repeat

image Jean_titjob_hair_back_animation0:
    animation
    "Jean_blowjob_hair_back"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jean_titjob_hair_back_animation1:
    animation
    "Jean_blowjob_hair_back"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Jean_titjob_hair_back_animation2:
    animation
    "Jean_blowjob_hair_back"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Jean_titjob_hair_back_animation3:
    animation
    "Jean_blowjob_hair_back"

    subpixel True
    rotate 0
    parallel:
        ease 2 yoffset 125
        pause 0.1
        ease 2 yoffset 130
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jean_titjob_hair_back_animation5:
    animation
    "Jean_blowjob_hair_back"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 125
        pause 0.2
        ease 2 yoffset 130
        pause 0.5
        repeat
    parallel:
        ease 2 rotate -5
        pause 0.5
        repeat

image Jean_titjob_body_animation0:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_body_animation1:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat

image Jean_titjob_body_animation2:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat

image Jean_titjob_body_animation3:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 130
        pause 0.1
        ease 2 yoffset 140
        pause 0.1
        repeat

image Jean_titjob_body_animation5:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 130
        pause 0.2
        ease 2 yoffset 140
        pause 0.5
        repeat

image Jean_titjob_head_animation0:
    animation
    "Jean_blowjob_head"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jean_titjob_head_animation1:
    animation
    "Jean_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Jean_titjob_head_animation2:
    animation
    "Jean_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Jean_titjob_head_animation3:
    animation
    "Jean_blowjob_head"

    subpixel True
    parallel:
        ease 2 yoffset 125
        pause 0.1
        ease 2 yoffset 130
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jean_titjob_head_animation5:
    animation
    "Jean_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 125
        pause 0.2
        ease 2 yoffset 130
        pause 0.5
        repeat
    parallel:
        ease 2 rotate -5
        pause 0.5
        repeat

image Jean_titjob_right_breast_animation0:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_right_breast_animation1:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Jean_titjob_right_breast_animation2:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jean_titjob_right_breast_animation3:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        pause 0.2
        ease 1.9 yoffset 80
        pause 0.2
        ease 1.9 yoffset 90
        repeat

image Jean_titjob_right_breast_animation5:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 80
        pause 0.2
        ease 2 yoffset 90
        pause 0.4
        repeat

image Jean_titjob_bra_stretch_animation0:
    "Jean_titjob_bra_stretch"

    yzoom 0.75

image Jean_titjob_bra_stretch_animation1:
    animation
    "Jean_titjob_bra_stretch"

    subpixel True
    parallel:
        pause 0.1
        ease 1.9 ypos -70
        pause 0.4
        ease 2.3 ypos 145
        repeat
    parallel:
        pause 0.1
        ease 1.9 yzoom 0.5
        pause 0.4
        ease 1.8 yzoom 1
        pause 0.5
        repeat

image Jean_titjob_bra_stretch_animation2:
    animation
    "Jean_titjob_bra_stretch"

    subpixel True
    yzoom 0.75
    block:
        pause 0.2
        ease 0.8 yoffset 0
        pause 0.3
        ease 0.3 yoffset 50
        repeat

image Jean_titjob_bra_stretch_animation3:
    animation
    "Jean_titjob_bra_stretch"

    offset (-20, 145)

image Jean_titjob_bra_stretch_animation5:
    "Jean_titjob_bra_stretch"

    offset (-20, 145)

image Jean_titjob_breasts_animation0:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_breasts_animation1:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Jean_titjob_breasts_animation2:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jean_titjob_breasts_animation3:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        pause 0.2
        ease 1.9 yoffset 80
        pause 0.2
        ease 1.9 yoffset 90
        repeat

image Jean_titjob_breasts_animation5:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 80
        pause 0.2
        ease 2 yoffset 90
        pause 0.4
        repeat

image Jean_titjob_hair_animation0:
    animation
    "Jean_titjob_hair"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jean_titjob_hair_animation1:
    animation
    "Jean_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Jean_titjob_hair_animation2:
    animation
    "Jean_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Jean_titjob_hair_animation3:
    animation
    "Jean_titjob_hair"

    subpixel True
    parallel:
        ease 2 yoffset 125
        pause 0.1
        ease 2 yoffset 130
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jean_titjob_hair_animation5:
    animation
    "Jean_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 125
        pause 0.2
        ease 2 yoffset 130
        pause 0.5
        repeat
    parallel:
        ease 2 rotate -5
        pause 0.5
        repeat

layeredimage Jean_sprite titjob:
    # if JeanX.Clothes["bra"].string in ["green_bra", "green_lace_bra"]:
    #     "Jean_titjob_bra_back_animation[JeanX.primary_Action.speed]" pos (0.0, -0.025)

    always:
        "Jean_titjob_hair_back_animation[JeanX.primary_Action.speed]" pos (0.0, -0.15) zoom 0.9

    always:
        "Jean_titjob_body_animation[JeanX.primary_Action.speed]"

    always:
        "Jean_titjob_head_animation[JeanX.primary_Action.speed]" pos (0.0, -0.15) zoom 0.9

    always:
        "Jean_titjob_right_breast_animation[JeanX.primary_Action.speed]" pos (0.0, -0.025)

    always:
        "Zero_cock_Jean"

    # if JeanX.Outfit["bra"].name in ["sports bra", "bikini top"]:
    #     "Jean_titjob_bra_stretch_animation[JeanX.primary_Action.speed]"

    always:
        "Jean_titjob_breasts_animation[JeanX.primary_Action.speed]" pos (0.0, -0.025)

    always:
        "Jean_titjob_hair_animation[JeanX.primary_Action.speed]" pos (0.0, -0.15) zoom 0.9

    anchor (0.5, 0.0) offset (300, 750) zoom 1.1

image Jean_blowjob_blinking:
    "images/Jean_blowjob/Jean_blowjob_eyes_[JeanX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jean_blowjob/Jean_blowjob_eyes_sexy.png"
    0.05
    "images/Jean_blowjob/Jean_blowjob_eyes_closed.png"
    0.15
    "images/Jean_blowjob/Jean_blowjob_eyes_sexy.png"
    0.05
    repeat
