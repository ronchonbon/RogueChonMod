image Storm_blinking:
    "images/Storm_standing/Storm_standing_eyes_[StormX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Storm_standing/Storm_standing_eyes_sexy.png"
    0.05
    "images/Storm_standing/Storm_standing_eyes_closed.png"
    0.15
    "images/Storm_standing/Storm_standing_eyes_sexy.png"
    0.05
    repeat

layeredimage Storm_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.19, 1.05)

    if StormX.grool > 1 and not StormX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.19, 1.05)

    if StormX.grool > 1 and not StormX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.19, 1.05)

    if StormX.grool > 1 and not StormX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.19, 1.05)

layeredimage Storm_grool_animations:
    if not StormX.grool:
        Null()
    elif StormX.Clothes["pants"].state:
        AlphaMask("Storm_grool_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_pants.png")
    elif StormX.Clothes["underwear"].state:
        AlphaMask("Storm_grool_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_underwear.png")
    elif not StormX.Outfit.pussy_covered:
        AlphaMask("Storm_grool_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask.png")

layeredimage Storm_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.19, 1.05)

    if not StormX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.19, 1.05)

    if not StormX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.19, 1.05)

    if not StormX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.19, 1.05)

layeredimage Storm_spunk_animations:
    if not StormX.spunk["pussy"] and not StormX.spunk["anus"]:
        Null()
    elif StormX.Clothes["pants"].state:
        AlphaMask("Storm_spunk_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_pants.png")
    elif StormX.Clothes["underwear"].state:
        AlphaMask("Storm_spunk_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_underwear.png")
    elif not StormX.Outfit.pussy_covered:
        AlphaMask("Storm_spunk_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask.png")

layeredimage Storm_standing_fondling_animations:
    if StormX.primary_Action.Target != StormX:
        Null()
    elif StormX.primary_Action.type == "fondle_breasts":
        "Storm_fondle_breast_right_animation" pos (0.078, 0.675)
    elif StormX.primary_Action.type == "fondle_pussy":
        "Storm_fondle_pussy_animation" pos (0.17, 0.994)
    elif StormX.primary_Action.type in "finger_pussy":
        "Storm_finger_pussy_animation" pos (0.175, 1.05)

    if StormX.secondary_Action.Target != StormX:
        Null()
    elif StormX.secondary_Action.type == "fondle_breasts":
        "Storm_fondle_breast_left_animation" pos (0.24, 0.72)
    elif StormX.secondary_Action.type == "fondle_pussy":
        "Storm_fondle_pussy_animation" pos (0.17, 0.994)
    elif StormX.secondary_Action.type in "finger_pussy":
        "Storm_finger_pussy_animation" pos (0.175, 1.05)

    if Player.primary_Action.Target != StormX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.12, 1.2)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.2, 0.69)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.225, 0.67)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.18, 0.98)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.155, 1.17)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.185, 1.07)

    if Player.secondary_Action.Target != StormX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.12, 1.2)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.135, 0.645)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.07, 0.64)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.18, 0.98)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.155, 1.17)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.185, 1.07)

image Storm_handjob_under_hand_animation0:
    "Storm_handjob_under"

image Storm_handjob_under_hand_animation1:
    animation
    "Storm_handjob_under"

    subpixel True
    rotate -2
    block:
        ease 0.75 yoffset 20 rotate 5
        pause 0.25
        ease 1.0 yoffset -30 rotate -2
        pause 0.1
        repeat

image Storm_handjob_under_hand_animation2:
    animation
    "Storm_handjob_under"

    subpixel True
    rotate 0
    block:
        ease 0.4 yoffset 10 rotate 3
        pause 0.1
        ease 0.4 yoffset -30 rotate 0
        pause 0.1
        repeat

image Storm_handjob_over_hand_animation0:
    "Storm_handjob_over"

image Storm_handjob_over_hand_animation1:
    animation
    "Storm_handjob_over"

    subpixel True
    rotate -2
    block:
        ease 0.75 yoffset 20 rotate 5
        pause 0.25
        ease 1.0 yoffset -30 rotate -2
        pause 0.1
        repeat

image Storm_handjob_over_hand_animation2:
    animation
    "Storm_handjob_over"

    subpixel True
    rotate 0
    block:
        ease 0.4 yoffset 10 rotate 3
        pause 0.1
        ease 0.4 yoffset -30 rotate 0
        pause 0.1
        repeat

layeredimage Storm_sprite handjob:
    always:
        "Storm_sprite standing"

    always:
        "Storm_handjob_under_hand_animation[StormX.primary_Action.speed]" pos (0.08, 0.455) zoom 0.28

    always:
        "Zero_cock_Storm"

    always:
        "Storm_handjob_over_hand_animation[StormX.primary_Action.speed]" pos (0.08, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Storm_titjob_bra_back_animation0:
    animation
    "Storm_titjob_bra_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Storm_titjob_bra_back_animation1:
    animation
    "Storm_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 50
        repeat

image Storm_titjob_bra_back_animation2:
    animation
    "Storm_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Storm_titjob_bra_back_animation3:
    animation
    "Storm_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Storm_titjob_bra_back_animation5:
    animation
    "Storm_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

image Storm_titjob_hair_back_animation0:
    animation
    "Storm_blowjob_hair_back"

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

image Storm_titjob_hair_back_animation1:
    animation
    "Storm_blowjob_hair_back"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -40
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Storm_titjob_hair_back_animation2:
    animation
    "Storm_blowjob_hair_back"

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

image Storm_titjob_hair_back_animation3:
    animation
    "Storm_blowjob_hair_back"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset 70
        pause 0.1
        ease 0.5 yoffset 140
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Storm_titjob_hair_back_animation5:
    animation
    "Storm_blowjob_hair_back"

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

image Storm_titjob_body_animation0:
    animation
    "Storm_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Storm_titjob_body_animation1:
    animation
    "Storm_titjob_body"

    subpixel True
    block:
        ease 2 ypos -40
        pause 0.2
        ease 2 ypos 60
        pause 0.5
        repeat

image Storm_titjob_body_animation2:
    animation
    "Storm_titjob_body"

    subpixel True
    block:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat

image Storm_titjob_body_animation3:
    animation
    "Storm_titjob_body"

    subpixel True
    block:
        ease 1 yoffset 100
        pause 0.1
        ease 0.5 yoffset 130
        repeat

image Storm_titjob_body_animation5:
    animation
    "Storm_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 130
        pause 0.2
        ease 2 yoffset 140
        pause 0.5
        repeat

image Storm_titjob_head_animation0:
    animation
    "Storm_blowjob_head"

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

image Storm_titjob_head_animation1:
    animation
    "Storm_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -40
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Storm_titjob_head_animation2:
    animation
    "Storm_blowjob_head"

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

image Storm_titjob_head_animation3:
    animation
    "Storm_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset 70
        pause 0.1
        ease 0.5 yoffset 140
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Storm_titjob_head_animation5:
    animation
    "Storm_blowjob_head"

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

image Storm_titjob_breasts_under_animation0:
    animation
    "Storm_titjob_breasts_under"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Storm_titjob_breasts_under_animation1:
    animation
    "Storm_titjob_breasts_under"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 50
        repeat

image Storm_titjob_breasts_under_animation2:
    animation
    "Storm_titjob_breasts_under"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Storm_titjob_breasts_under_animation3:
    animation
    "Storm_titjob_breasts_under"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Storm_titjob_breasts_under_animation5:
    animation
    "Storm_titjob_breasts_under"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

image Storm_titjob_bra_stretch_animation0:
    animation
    "Storm_titjob_bra_stretch"

    subpixel True
    zoom (0.75, 0.85)
    parallel:
        ease 2 yzoom 0.5
        pause 0.1
        ease 2 yzoom 0.85
        pause 0.1
        repeat
    parallel:
        ease 2 offset (-60, -230)
        pause 0.1
        ease 2 offset (-70, -210)
        pause 0.1
        repeat

image Storm_titjob_bra_stretch_animation1:
    animation
    "Storm_titjob_bra_stretch"

    subpixel True
    zoom (0.9, 1.3)
    parallel:
        pause 0.1
        ease 1.6 yzoom 0.3
        pause 0.9
        ease 1.6 yzoom 1.5
        ease 0.5 yzoom 1.3
        repeat
    parallel:
        pause 0.1
        ease 1.9 xzoom 0.6
        pause 0.4
        ease 1.8 xzoom 0.9
        pause 0.5
        repeat
    parallel:
        pause 0.1
        ease 1.9 offset (-50, -260)
        pause 0.4
        ease 1.8 offset (-100, -140)
        ease 0.5 offset (-100, -150)
        repeat

image Storm_titjob_bra_stretch_animation2:
    animation
    "Storm_titjob_bra_stretch"

    subpixel True
    zoom (1, 1.7)
    parallel:
        ease 0.3 yzoom 1.3
        ease 0.7 yzoom 0.3
        pause 0.2
        ease 0.4 yzoom 1.7
        repeat
    parallel:
        ease 0.3 offset (-100, -160)
        ease 0.7 offset (-80, -240)
        pause 0.2
        ease 0.4 offset (-100, -120)
        repeat

image Storm_titjob_bra_stretch_animation3:
    animation
    "Storm_titjob_bra_stretch"

    subpixel True
    zoom (1, 2)
    parallel:
        ease 0.3 yzoom 1.95
        ease 0.7 yzoom 1.7
        pause 0.2
        ease 0.4 yzoom 2
        repeat
    parallel:
        ease 0.3 offset (-100, -115)
        ease 0.7 offset (-90, -155)
        pause 0.2
        ease 0.4 offset (-100, -105)
        repeat

image Storm_titjob_bra_stretch_animation5:
    animation
    "Storm_titjob_bra_stretch"

    subpixel True
    zoom (1, 2)
    parallel:
        pause 0.1
        ease 2 yzoom 1.8
        pause 0.2
        ease 2 yzoom 2
        pause 0.4
        repeat
    parallel:
        pause 0.1
        ease 2 offset (-100, -115)
        pause 0.2
        ease 2 offset (-100, -105)
        pause 0.4
        repeat

image Storm_titjob_breasts_animation0:
    animation
    "Storm_titjob_breasts"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Storm_titjob_breasts_animation1:
    animation
    "Storm_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 50
        repeat

image Storm_titjob_breasts_animation2:
    animation
    "Storm_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Storm_titjob_breasts_animation3:
    animation
    "Storm_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Storm_titjob_breasts_animation5:
    animation
    "Storm_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

image Storm_titjob_hair_animation0:
    animation
    "Storm_titjob_hair"

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

image Storm_titjob_hair_animation1:
    animation
    "Storm_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -40
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Storm_titjob_hair_animation2:
    animation
    "Storm_titjob_hair"

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

image Storm_titjob_hair_animation3:
    animation
    "Storm_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset 70
        pause 0.1
        ease 0.5 yoffset 140
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Storm_titjob_hair_animation5:
    animation
    "Storm_titjob_hair"

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

layeredimage Storm_sprite titjob:
    # if StormX.Clothes["bra"].string in ["black_bra", "black_lace_bra"]:
    #     "Storm_titjob_bra_back_animation[StormX.primary_Action.speed]"

    always:
        "Storm_titjob_hair_back_animation[StormX.primary_Action.speed]" pos (0.0, -0.15) zoom 0.9

    always:
        "Storm_titjob_body_animation[StormX.primary_Action.speed]"

    always:
        "Storm_titjob_head_animation[StormX.primary_Action.speed]" pos (0.0, -0.15) zoom 0.9

    # if StormX.Clothes["bra"].string != "Elena_bra":
    #     "Storm_titjob_breasts_under_animation[StormX.primary_Action.speed]"

    always:
        "Zero_cock_Storm"

    # if StormX.Clothes["bra"].string in ["black_sports_bra", "black_bikini_top"]:
    #     "Storm_titjob_bra_stretch_animation[StormX.primary_Action.speed]"

    always:
        "Storm_titjob_breasts_animation[StormX.primary_Action.speed]"

    always:
        "Storm_titjob_hair_animation[StormX.primary_Action.speed]" pos (0.0, -0.15) zoom 0.9

    anchor (0.5, 0.0) offset (320, 700)

image Storm_blowjob_blinking:
    "images/Storm_blowjob/Storm_blowjob_eyes_[StormX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Storm_blowjob/Storm_blowjob_eyes_sexy.png"
    0.05
    "images/Storm_blowjob/Storm_blowjob_eyes_closed.png"
    0.15
    "images/Storm_blowjob/Storm_blowjob_eyes_sexy.png"
    0.05
    repeat
