image Kitty_blinking:
    "images/Kitty_standing/Kitty_standing_eyes[KittyX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_standing/Kitty_standing_eyes_half.png"
    0.05
    "images/Kitty_standing/Kitty_standing_eyes_closed.png"
    0.15
    "images/Kitty_standing/Kitty_standing_eyes_half.png"
    0.05
    repeat

layeredimage Kitty_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.25, 1.2)

    if KittyX.grool > 1 and not KittyX.pussy_covered:
        "grool_dripping_animation" pos (0.25, 1.2)

    if KittyX.grool > 1 and not KittyX.pussy_covered:
        "grool_dripping_animation" pos (0.25, 1.2)

    if KittyX.grool > 1 and not KittyX.pussy_covered:
        "grool_dripping_animation" pos (0.25, 1.2)

layeredimage Kitty_grool_animations:
    if not KittyX.grool:
        Null()
    elif KittyX.bottom_pulled_down:
        AlphaMask("Kitty_grool_dripping_animation", "images/Kitty_standing/Kitty_standing_grool_mask_pants.png")
    elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        AlphaMask("Kitty_grool_dripping_animation", "images/Kitty_standing/Kitty_standing_grool_mask_underwear.png")
    elif not KittyX.pussy_covered:
        AlphaMask("Kitty_grool_dripping_animation", "images/Kitty_standing/Kitty_standing_grool_mask.png")

layeredimage Kitty_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.25, 1.2)

    if not KittyX.pussy_covered:
        "spunk_dripping_animation" pos (0.25, 1.2)

    if not KittyX.pussy_covered:
        "spunk_dripping_animation" pos (0.25, 1.2)

    if not KittyX.pussy_covered:
        "spunk_dripping_animation" pos (0.25, 1.2)

layeredimage Kitty_spunk_animations:
    if not KittyX.spunk["pussy"] and not KittyX.spunk["anus"]:
        Null()
    elif KittyX.bottom_pulled_down:
        AlphaMask("Kitty_spunk_dripping_animation", "images/Kitty_standing/Kitty_standing_grool_mask_pants.png")
    elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        AlphaMask("Kitty_spunk_dripping_animation", "images/Kitty_standing/Kitty_standing_grool_mask_underwear.png")
    elif not KittyX.pussy_covered:
        AlphaMask("Kitty_spunk_dripping_animation", "images/Kitty_standing/Kitty_standing_grool_mask.png")

layeredimage Kitty_standing_fondling_animations:
#     if Player.primary_action == "lesbian" or not KittyX.secondary_action or focused_Girl != KittyX:
#             Null()
#     elif Player.primary_action != "sex" and KittyX.secondary_action in "finger_pussy" and KittyX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif KittyX.secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif KittyX.secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif KittyX.secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == KittyX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and KittyX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action in "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
    if not Player.primary_action or focused_Girl != KittyX:
        Null()
    elif Player.primary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.18, 1.38)
    elif Player.primary_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.17, 0.765)
    elif Player.primary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.11, 0.7)
    elif Player.primary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.23, 1.12)
    elif Player.primary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.21, 1.32)
    elif Player.primary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.24, 1.22)

    if not Player.secondary_action or focused_Girl != KittyX:
        Null()
    elif Player.secondary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.18, 1.38)
    elif Player.secondary_action == "fondle_breasts" and not girl_secondary_action and not second_girl_main_action and not second_girl_secondary_action:
        "Zero_fondle_breasts_right_animation" pos (0.17, 0.765)
    elif Player.secondary_action == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.212, 0.765)
    elif Player.secondary_action == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.225, 0.735)
    elif Player.secondary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.23, 1.12)
    elif Player.secondary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.21, 1.32)
    elif Player.secondary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.24, 1.22)
#
#     if not second_girl_main_action or focused_Girl != KittyX:
#         Null()
#     elif second_girl_main_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_main_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif second_girl_main_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif second_girl_main_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif second_girl_main_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and KittyX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and KittyX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not KittyX.secondary_action or focused_Girl == KittyX:
#         Null()
#     elif KittyX.secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif KittyX.secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif KittyX.secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif KittyX.secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif KittyX.secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif KittyX.secondary_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif KittyX.secondary_action == "fondle_pussy" and Player.primary_action != "sex" and KittyX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif KittyX.secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif KittyX.secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)

image Kitty_handjob_under_hand_animation0:
    "Kitty_handjob_under"

image Kitty_handjob_under_hand_animation1:
    animation
    "Kitty_handjob_under"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Kitty_handjob_under_hand_animation2:
    animation
    "Kitty_handjob_under"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

image Kitty_handjob_over_hand_animation0:
    "Kitty_handjob_over"

image Kitty_handjob_over_hand_animation1:
    animation
    "Kitty_handjob_over"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Kitty_handjob_over_hand_animation2:
    animation
    "Kitty_handjob_over"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

layeredimage Kitty_sprite handjob:
    always:
        "Kitty_sprite standing" pos (0.05, 0.0)

    always:
        "Kitty_handjob_under_hand_animation[action_speed]" pos (-0.01, 0.455) zoom 0.28

    always:
        "Zero_cock_Kitty"

    always:
        "Kitty_handjob_over_hand_animation[action_speed]" pos (-0.01, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Kitty_titjob_hair_back_animation0:
    animation
    "Kitty_titjob_hair_back"

    subpixel True
    block:
        ease 2.4 yoffset -10
        ease 1.6 yoffset 0
        repeat

image Kitty_titjob_hair_back_animation1:
    animation
    "Kitty_titjob_hair_back"

    subpixel True
    block:
        ease 3.0 yoffset -50
        ease 1.0 yoffset 0
        repeat

image Kitty_titjob_hair_back_animation2:
    animation
    "Kitty_titjob_hair_back"

    subpixel True
    block:
        ease 0.7 yoffset -45
        ease 0.25 yoffset 0
        pause 0.05
        repeat

image Kitty_titjob_hair_back_animation3:
    animation
    "Kitty_titjob_hair_back"

    subpixel True
    parallel:
        block:
            ease 2 offset (-5, 30)
            ease 0.6 offset (-5, 55)
            pause 0.4
            repeat 2
        block:
            ease 2.2 offset (-5, 30)
            ease 0.8 offset (15, 60)
            ease 2.2 offset (5, 30)
            ease 0.8 offset (15, 60)
        block:
            ease 2 offset (-5, 30)
            ease 0.6 offset (-5, 55)
            pause 0.4
            repeat 2
        block:
            ease 2.2 offset (-5, 30)
            ease 0.8 offset (-30, 60)
            ease 2.2 offset (-15, 30)
            ease 0.8 offset (-30, 60)
        repeat
    parallel:
        block:
            ease 2.2 rotate 0
            pause 3.8
        block:
            ease 2.2 rotate 0
            ease 0.8 rotate 10
            ease 2.2 rotate 0
            ease 0.8 rotate 5
        block:
            ease 2.2 rotate 0
            pause 3.8
        block:
            ease 2.2 rotate 0
            ease 0.8 rotate -10
            ease 2.2 rotate 0
            ease 0.8 rotate -5
        repeat

image Kitty_titjob_hair_back_animation5:
    animation
    "Kitty_titjob_hair_back"

    subpixel True
    block:
        ease 2 yoffset 4
        ease 1.6 yoffset 7
        pause 0.4
        repeat

image Kitty_titjob_body_animation0:
    animation
    "Kitty_titjob_body"

    subpixel True
    block:
        ease 2.4 yoffset -5
        ease 1.6 yoffset 0
        repeat

image Kitty_titjob_body_animation1:
    animation
    "Kitty_titjob_body"

    subpixel True
    block:
        ease 2.8 yoffset -50
        ease 1.0 yoffset 0
        pause 0.2
        repeat

image Kitty_titjob_body_animation2:
    animation
    "Kitty_titjob_body"

    subpixel True
    block:
        ease 0.65 yoffset -45
        ease 0.25 yoffset 0
        pause 0.1
        repeat

image Kitty_titjob_body_animation3:
    animation
    "Kitty_titjob_body"

    subpixel True
    block:
        ease 2.2 yoffset -20
        ease 0.6 yoffset 0
        pause 0.2
        repeat

image Kitty_titjob_body_animation5:
    animation
    "Kitty_titjob_body"

    subpixel True
    block:
        ease 2.2 yoffset -20
        ease 1.6 yoffset 0
        pause 0.2
        repeat

image Kitty_titjob_arms_animation0:
    animation
    "Kitty_titjob_arms"

    subpixel True
    block:
        ease 2.4 yoffset -5
        ease 1.6 yoffset 0
        repeat

image Kitty_titjob_arms_animation1:
    animation
    "Kitty_titjob_arms"

    subpixel True
    block:
        ease 2.85 yoffset -50
        ease 1.0 yoffset 0
        pause 0.15
        repeat

image Kitty_titjob_arms_animation2:
    animation
    "Kitty_titjob_arms"

    subpixel True
    block:
        ease 0.68 yoffset -45
        ease 0.25 yoffset 0
        pause 0.07
        repeat

image Kitty_titjob_arms_animation3:
    animation
    "Kitty_titjob_arms"

    subpixel True
    block:
        ease 2.2 yoffset -20
        ease 0.6 yoffset 0
        pause 0.2
        repeat

image Kitty_titjob_arms_animation5:
    animation
    "Kitty_titjob_arms"

    subpixel True
    block:
        ease 2.2 yoffset -20
        ease 1.6 yoffset 0
        pause 0.2
        repeat

image Kitty_titjob_head_animation0:
    animation
    "Kitty_blowjob_head"

    subpixel True
    block:
        ease 2.4 yoffset -10
        ease 1.6 yoffset 0
        repeat

image Kitty_titjob_head_animation1:
    animation
    "Kitty_blowjob_head"

    subpixel True
    block:
        ease 2.9 yoffset -50
        ease 1.0 yoffset 0
        pause 0.1
        repeat

image Kitty_titjob_head_animation2:
    animation
    "Kitty_blowjob_head"

    subpixel True
    block:
        ease 0.68 yoffset -45
        ease 0.25 yoffset 0
        pause 0.07
        repeat

image Kitty_titjob_head_animation3:
    animation
    "Kitty_blowjob_head"

    subpixel True
    parallel:
        block:
            ease 2 offset (-5, 30)
            ease 0.6 offset (-5, 55)
            pause 0.4
            repeat 2
        block:
            ease 2.2 offset (-5, 30)
            ease 0.8 offset (15, 60)
            ease 2.2 offset (5, 30)
            ease 0.8 offset (15, 60)
        block:
            ease 2 offset (-5, 30)
            ease 0.6 offset (-5, 55)
            pause 0.4
            repeat 2
        block:
            ease 2.2 offset (-5, 30)
            ease 0.8 offset (-30, 60)
            ease 2.2 offset (-15, 30)
            ease 0.8 offset (-30, 60)
        repeat
    parallel:
        block:
            ease 2.2 rotate 0
            pause 3.8
        block:
            ease 2.2 rotate 0
            ease 0.8 rotate 10
            ease 2.2 rotate 0
            ease 0.8 rotate 5
        block:
            ease 2.2 rotate 0
            pause 3.8
        block:
            ease 2.2 rotate 0
            ease 0.8 rotate -10
            ease 2.2 rotate 0
            ease 0.8 rotate -5
        repeat

image Kitty_titjob_head_animation5:
    animation
    "Kitty_blowjob_head"

    subpixel True
    block:
        ease 2 offset (-5, 0)
        ease 1.6 offset (-5, 3)
        pause 0.4
        repeat

image Kitty_titjob_breasts_animation0:
    animation
    "Kitty_titjob_breasts"

    subpixel True
    block:
        ease 2.4 yoffset -5
        ease 1.6 yoffset 0
        repeat

image Kitty_titjob_breasts_animation1:
    animation
    "Kitty_titjob_breasts"

    subpixel True
    block:
        ease 2.9 yoffset -50
        ease 1.0 yoffset 0
        pause 0.1
        repeat

image Kitty_titjob_breasts_animation2:
    animation
    "Kitty_titjob_breasts"

    subpixel True
    block:
        ease 0.71 yoffset -40
        ease 0.27 yoffset 0
        pause 0.02
        repeat

image Kitty_titjob_breasts_animation3:
    animation
    "Kitty_titjob_breasts"

    subpixel True
    block:
        ease 2.2 yoffset -20
        ease 0.6 yoffset 0
        pause 0.2
        repeat

image Kitty_titjob_breasts_animation5:
    animation
    "Kitty_titjob_breasts"

    subpixel True
    block:
        ease 2.2 yoffset -20
        ease 1.6 yoffset 0
        pause 0.2
        repeat

layeredimage Kitty_sprite titjob:
    always:
        "Kitty_titjob_hair_back_animation[action_speed]" pos (0.0, -0.2) zoom 0.9

    always:
        "Kitty_titjob_body_animation[action_speed]"

    always:
        "Kitty_titjob_arms_animation[action_speed]"

    always:
        "Kitty_titjob_head_animation[action_speed]" pos (0.0, -0.2) zoom 0.9

    always:
        "Kitty_titjob_breasts_animation[action_speed]"

    if action_speed:
        AlphaMask("Zero_cock_Kitty", "Zero_cock_Kitty_mask") offset (-100, -100)
    else:
        "Zero_cock_Kitty" offset (-100, -100)

    anchor (0.5, 0.0) offset (280, 800)

image Kitty_blowjob_blinking:
    "images/Kitty_blowjob/Kitty_blowjob_eyes[KittyX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_blowjob/Kitty_blowjob_eyes_squint.png"
    0.05
    "images/Kitty_blowjob/Kitty_blowjob_eyes_closed.png"
    0.15
    "images/Kitty_blowjob/Kitty_blowjob_eyes_squint.png"
    0.05
    repeat

image Kitty_blowjob_body_animation0:
    "Kitty_blowjob_body"

image Kitty_blowjob_body_animation1:
    animation
    "Kitty_blowjob_body"

    subpixel True
    ease 0.5 offset (0, -35)
    block:
        ease 2.5 offset (30, 90)
        ease 2 offset (0, -35)
        pause 0.5
        repeat

image Kitty_blowjob_body_animation2:
    animation
    "Kitty_blowjob_body"

    subpixel True
    block:
        ease 1 yoffset 15
        ease 1.5 yoffset -40
        repeat

image Kitty_blowjob_body_animation3:
    animation
    "Kitty_blowjob_body"

    subpixel True
    ease 0.5 yoffset 50
    block:
        ease 1 yoffset 100
        ease 1.5 yoffset 50
        repeat

image Kitty_blowjob_body_animation4:
    animation
    "Kitty_blowjob_body"

    subpixel True
    ease 0.5 yoffset 100
    block:
        ease 1.2 yoffset 160
        pause 0.5
        ease 1.8 yoffset 80
        repeat

image Kitty_blowjob_head_animation0:
    "Kitty_blowjob_head"

image Kitty_blowjob_head_animation1:
    animation
    "Kitty_blowjob_head"

    subpixel True
    ease 0.5 offset (0, -35)
    block:
        ease 2.5 offset (25, 100)
        ease 2 offset (0, -35)
        pause 0.5
        repeat

image Kitty_blowjob_head_animation2:
    animation
    "Kitty_blowjob_head"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset -40
        repeat

image Kitty_blowjob_head_animation3:
    animation
    "Kitty_blowjob_head"

    subpixel True
    ease 0.5 yoffset 50
    block:
        ease 1 yoffset 120
        ease 1.5 yoffset 50
        repeat

image Kitty_blowjob_head_animation4:
    animation
    "Kitty_blowjob_head"

    subpixel True
    ease 0.5 yoffset 100
    block:
        ease 1 yoffset 210
        pause 0.5
        ease 2 yoffset 80
        repeat

image Kitty_blowjob_mouth_animation2:
    animation
    "Kitty_blowjob_mouth"

    subpixel True
    zoom 0.7
    block:
        pause 0.40
        easeout 0.40 zoom 0.69
        linear 0.10 zoom 0.7
        easein 0.45 zoom 0.65
        pause 0.15
        easeout 0.25 zoom 0.7
        linear 0.10 zoom 0.69
        easein 0.30 zoom 0.7
        pause 0.35
        repeat

image Kitty_blowjob_mask_animation2:
    animation
    "Kitty_blowjob_mask"

    subpixel True
    zoom 0.7
    block:
        pause 0.40
        easeout 0.40 zoom 0.69
        linear 0.10 zoom 0.7
        easein 0.45 zoom 0.65
        pause 0.15
        easeout 0.25 zoom 0.7
        linear 0.10 zoom 0.69
        easein 0.30 zoom 0.7
        pause 0.35
        repeat

image Kitty_blowjob_face_mask_animation2:
    animation
    AlphaMask("Kitty_blowjob_head", "Kitty_blowjob_mask_animation2")

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset -40
        repeat

image Kitty_blowjob_face_mask_animation3:
    animation
    AlphaMask("Kitty_blowjob_head", "Kitty_blowjob_mask")

    subpixel True
    ease 0.5 yoffset 50
    block:
        ease 1 yoffset 120
        ease 1.5 yoffset 50
        repeat

image Kitty_blowjob_face_mask_animation4:
    animation
    AlphaMask("Kitty_blowjob_head", "Kitty_blowjob_mask")

    subpixel True
    ease 0.5 yoffset 100
    block:
        ease 1 yoffset 210
        pause 0.5
        ease 2 yoffset 80
        repeat

image Kitty_blowjob_spunk_mouth_animation2:
    animation
    "Kitty_blowjob_spunk_mouth_over"

    subpixel True
    zoom 0.7
    block:
        pause 0.40
        easeout 0.40 zoom 0.69
        linear 0.10 zoom 0.7
        easein 0.45 zoom 0.65
        pause 0.15
        easeout 0.25 zoom 0.7
        linear 0.10 zoom 0.69
        easein 0.30 zoom 0.7
        pause 0.35
        repeat

image Kitty_blowjob_spunk_mouth_over_animation2:
    animation
    "Kitty_blowjob_spunk_mouth_animation2"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset -40
        repeat

image Kitty_blowjob_spunk_mouth_over_animation3:
    animation
    "Kitty_blowjob_spunk_mouth_over"

    subpixel True
    ease 0.5 yoffset 50
    block:
        ease 1 yoffset 120
        ease 1.5 yoffset 50
        repeat

image Kitty_blowjob_spunk_mouth_over_animation4:
    animation
    "Kitty_blowjob_spunk_mouth_over"

    subpixel True
    ease 0.5 yoffset 100
    block:
        ease 1 yoffset 210
        pause 0.5
        ease 2 yoffset 80
        repeat

layeredimage Kitty_sprite blowjob:
    always:
        "Kitty_blowjob_body_animation[action_speed]"

    always:
        "Kitty_blowjob_head_animation[action_speed]" pos (0.0, -0.05) zoom 0.9

    always:
        "Zero_cock_Kitty"

    if action_speed > 1:
        "Kitty_blowjob_face_mask_animation[action_speed]" anchor (0.5, 0.5) pos (0.0, -0.05) zoom 0.9

    if KittyX.spunk["mouth"] and action_speed > 1:
        "Kitty_blowjob_spunk_mouth_over_animation[action_speed]" pos (0.0, -0.05) zoom 0.9

    anchor (0.5, 0.0) offset (250, 750) zoom 1.1

image Kitty_sex_body_animation0:
    "Kitty_sex_body"

image Kitty_sex_body_animation1:
    animation
    "Kitty_sex_body"

    subpixel True
    block:
        pause 0.5
        easein 0.75 yoffset -5
        pause 1.25
        ease 2.5 yoffset 0
        repeat

image Kitty_sex_body_animation2:
    animation
    "Kitty_sex_body"

    subpixel True
    block:
        pause 0.6
        easein 0.4 yoffset -10
        ease 0.25 yoffset -5
        pause 1
        ease 2.75 yoffset 10
        repeat

image Kitty_sex_body_animation3:
    animation
    "Kitty_sex_body"

    subpixel True
    block:
        pause 0.17
        easein 0.13 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 10
        repeat

image Kitty_sex_body_footjob_animation0:
    "Kitty_sex_body"

image Kitty_sex_body_footjob_animation1:
    animation
    "Kitty_sex_body"

    subpixel True
    block:
        pause 0.5
        ease 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 2.50 yoffset 15
        repeat

image Kitty_sex_body_footjob_animation2:
    animation
    "Kitty_sex_body"

    subpixel True
    block:
        pause 0.2
        ease 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        repeat

image Kitty_sex_body_hotdog_animation0:
    "Kitty_sex_body"

image Kitty_sex_body_hotdog_animation1:
    "Kitty_sex_body"

image Kitty_sex_body_hotdog_animation2:
    animation
    "Kitty_sex_body"

    subpixel True
    block:
        pause 0.30
        ease 0.50 yoffset -10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Kitty_sex_body_hotdog_animation3:
    animation
    "Kitty_sex_body"

    subpixel True
    block:
        pause 0.30
        ease 0.50 yoffset -10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Kitty_sex_legs_animation0:
    "Kitty_sex_legs"

image Kitty_sex_legs_animation1:
    animation
    "Kitty_sex_legs"

    subpixel True
    block:
        pause 0.25
        easein 1 yoffset -5
        pause 1
        ease 2.75 yoffset 0
        repeat

image Kitty_sex_legs_animation2:
    animation
    "Kitty_sex_legs"

    subpixel True
    block:
        pause 0.5
        easein 0.5 yoffset -15
        ease 0.25 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Kitty_sex_legs_animation3:
    animation
    "Kitty_sex_legs"

    subpixel True
    block:
        pause 0.15
        easein 0.15 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 0
        repeat

image Kitty_sex_legs_footjob_animation0:
    "Kitty_sex_legs"

image Kitty_sex_legs_footjob_animation1:
    animation
    "Kitty_sex_legs"

    subpixel True
    block:
        pause 0.5
        ease 1.0 yoffset -15
        ease 0.5 yoffset -10
        pause 1
        ease 2. yoffset 45
        repeat

image Kitty_sex_legs_footjob_animation2:
    animation
    "Kitty_sex_legs"

    subpixel True
    block:
        pause 0.2
        ease 0.5 yoffset -15
        ease 0.3 yoffset -10
        pause 0.2
        ease 0.8 yoffset 45
        repeat

image Kitty_sex_legs_hotdog_animation0:
    "Kitty_sex_legs"

image Kitty_sex_legs_hotdog_animation1:
    "Kitty_sex_legs"

image Kitty_sex_legs_hotdog_animation2:
    animation
    "Kitty_sex_legs"

    subpixel True
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Kitty_sex_legs_hotdog_animation3:
    animation
    "Kitty_sex_legs"

    subpixel True
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Kitty_sex_anus_animation0:
    "Kitty_sex_anus"

    xzoom 0.6

image Kitty_sex_anus_animation1:
    animation
    "Kitty_sex_anus"

    subpixel True
    xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_sex_anus_animation2:
    "Kitty_sex_anus"

image Kitty_sex_anus_animation3:
    "Kitty_sex_anus"

image Kitty_sex_spunk_anus_under_animation:
    animation
    "Kitty_sex_spunk_anus_under"

    subpixel True
    xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.95
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_sex_spunk_anus_over_animation:
    animation
    "Kitty_sex_spunk_anus_over"

    subpixel True
    xzoom 0.8
    block:
        ease 0.75 xzoom 1.0
        pause 1.75
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat

layeredimage Kitty_sprite sex:
    if Player.cock_position in ["in", "anal"]:
        "Kitty_sex_body_animation[action_speed]"
    elif Player.cock_position == "footjob":
        "Kitty_sex_body_footjob_animation[action_speed]"
    elif Player.cock_position == "out":
        "Kitty_sex_body_hotdog_animation[action_speed]"

    if Player.cock_position in ["in", "anal"]:
        "Kitty_sex_legs_animation[action_speed]"
    elif Player.cock_position == "footjob":
        "Kitty_sex_legs_footjob_animation[action_speed]"
    elif Player.cock_position == "out":
        "Kitty_sex_legs_hotdog_animation[action_speed]"

    anchor (0.5, 0.0) offset (230, 785) zoom 0.9

image Kitty_doggy_blinking:
    "images/Kitty_doggy/Kitty_doggy_eyes[KittyX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_doggy/Kitty_doggy_eyes_sexy.png"
    0.05
    "images/Kitty_doggy/Kitty_doggy_eyes_closed.png"
    0.15
    "images/Kitty_doggy/Kitty_doggy_eyes_sexy.png"
    0.05
    repeat

image Kitty_doggy_body_animation0:
    "Kitty_doggy_body"

image Kitty_doggy_body_animation1:
    animation
    "Kitty_doggy_body"

    subpixel True
    block:
        pause 0.4
        ease 0.3 yoffset -5
        ease 1 yoffset 0
        pause 0.8
        repeat

image Kitty_doggy_body_animation2:
    animation
    "Kitty_doggy_body"

    subpixel True
    pause 0.4
    block:
        ease 0.2 yoffset -10
        pause 0.3
        ease 2 yoffset 0
        repeat

image Kitty_doggy_body_animation3:
    animation
    "Kitty_doggy_body"

    subpixel True
    block:
        pause 0.15
        ease 0.1 yoffset 0
        pause 0.1
        ease 0.5 yoffset 20
        pause 0.05
        repeat

image Kitty_doggy_ass_animation0:
    "Kitty_doggy_ass"

image Kitty_doggy_ass_animation1:
    animation
    "Kitty_doggy_ass"

    subpixel True
    block:
        pause 0.4
        ease 0.2 yoffset -10
        ease 0.1 yoffset -7
        ease 0.9 yoffset 0
        pause 0.9
        repeat

image Kitty_doggy_ass_animation2:
    animation
    "Kitty_doggy_ass"

    subpixel True
    block:
        pause 0.4
        ease 0.2 yoffset -15
        ease 0.1 yoffset -5
        pause 0.2
        ease 1.6 yoffset 0
        repeat

image Kitty_doggy_ass_animation3:
    animation
    "Kitty_doggy_ass"

    subpixel True
    block:
        pause 0.15
        ease 0.1 yoffset -25
        ease 0.1 yoffset -15
        pause 0.1
        ease 0.4 yoffset 5
        pause 0.05
        repeat

image Kitty_doggy_pussy_hole_animation0:
    animation
    "Kitty_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Kitty_doggy_pussy_hole_animation1:
    animation
    "Kitty_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Kitty_doggy_pussy_hole_animation2:
    "Kitty_doggy_pussy_hole"

image Kitty_doggy_pussy_hole_animation3:
    "Kitty_doggy_pussy_hole"

image Kitty_doggy_pussy_fingering_animation:
    animation
    "Kitty_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.67
        pause 1
        ease 3 xzoom 0.6
        repeat

image Kitty_doggy_anus_anal_animation1:
    animation
    "Kitty_doggy_anus_hole"

    subpixel True
    zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Kitty_doggy_anus_anal_animation2:
    "Kitty_doggy_anus_hole"

    zoom 0.9

image Kitty_doggy_anus_anal_animation3:
    "Kitty_doggy_anus_hole"

    zoom 0.9

image Kitty_doggy_anus_fingering_animation:
    animation
    "Kitty_doggy_anus_hole"

    subpixel True
    zoom 0.6
    block:
        ease 0.5 zoom 0.67
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

image Kitty_doggy_shin_animation0:
    animation
    "Kitty_doggy_shins"

    subpixel True
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Kitty_doggy_shin_animation1:
    animation
    "Kitty_doggy_shins"

    subpixel True
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Kitty_doggy_shin_animation2:
    animation
    "Kitty_doggy_shins"

    subpixel True
    block:
        pause 0.05
        ease 0.6 yoffset 110
        ease 0.3 yoffset 0
        repeat

image Kitty_doggy_feet_animation0:
    animation
    "Kitty_doggy_feet"

    subpixel True
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Kitty_doggy_feet_animation1:
    animation
    "Kitty_doggy_feet"

    subpixel True
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Kitty_doggy_feet_animation2:
    animation
    "Kitty_doggy_feet"

    subpixel True
    block:
        pause 0.05
        ease 0.6 yoffset 110
        ease 0.3 yoffset 0
        repeat

layeredimage Kitty_sprite doggy:
    if Player.cock_position == "anal":
        "Kitty_doggy_body_animation[action_speed]"
    elif Player.cock_position == "in" and action_speed > 1:
        "Kitty_doggy_body_animation[action_speed]"
    else:
        "Kitty_doggy_body"

    if Player.cock_position == "anal":
        "Kitty_doggy_ass_animation[action_speed]"
    elif Player.cock_position == "in" and action_speed > 1:
        "Kitty_doggy_ass_animation[action_speed]"
    else:
        "Kitty_doggy_ass"

    if Player.sprite and Player.cock_position == "footjob":
        "Kitty_doggy_shin_animation[action_speed]"
    elif not Player.sprite and show_feet:
        "Kitty_doggy_shins"

    if Player.sprite and Player.cock_position == "footjob":
        "Kitty_doggy_cock_footjob_animation[action_speed]" pos (-0.005, 0.24) zoom 1.1

    if Player.cock_position == "footjob":
        "Kitty_doggy_feet_animation[action_speed]"
    elif not Player.sprite and show_feet:
        "Kitty_doggy_feet"

    anchor (0.5, 0.0) offset (190, 650) zoom 1.15
