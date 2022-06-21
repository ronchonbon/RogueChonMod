image Storm_blinking:
    "images/Storm_standing/Storm_standing_eyes[StormX.eyes].png"
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

    if StormX.grool > 1 and not StormX.pussy_covered:
        "grool_dripping_animation" pos (0.19, 1.05)

    if StormX.grool > 1 and not StormX.pussy_covered:
        "grool_dripping_animation" pos (0.19, 1.05)

    if StormX.grool > 1 and not StormX.pussy_covered:
        "grool_dripping_animation" pos (0.19, 1.05)

layeredimage Storm_grool_animations:
    if not StormX.grool:
        Null()
    elif StormX.bottom_pulled_down:
        AlphaMask("Storm_grool_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_pants.png")
    elif StormX.underwear_pulled_down:
        AlphaMask("Storm_grool_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_underwear.png")
    elif not StormX.pussy_covered:
        AlphaMask("Storm_grool_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask.png")

layeredimage Storm_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.19, 1.05)

    if not StormX.pussy_covered:
        "spunk_dripping_animation" pos (0.19, 1.05)

    if not StormX.pussy_covered:
        "spunk_dripping_animation" pos (0.19, 1.05)

    if not StormX.pussy_covered:
        "spunk_dripping_animation" pos (0.19, 1.05)

layeredimage Storm_spunk_animations:
    if not StormX.spunk["pussy"] and not StormX.spunk["anus"]:
        Null()
    elif StormX.bottom_pulled_down:
        AlphaMask("Storm_spunk_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_pants.png")
    elif StormX.underwear_pulled_down:
        AlphaMask("Storm_spunk_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask_underwear.png")
    elif not StormX.pussy_covered:
        AlphaMask("Storm_spunk_dripping_animation", "images/Storm_standing/Storm_standing_grool_mask.png")

layeredimage Storm_standing_fondling_animations:
    # if Player.primary_action == "lesbian" or not girl_secondary_action or focused_Girl != StormX:
    #     Null()
    # elif Player.primary_action != "sex" and girl_secondary_action in "finger_pussy" and StormX.lust >= 70:
    #     "Girl_finger_pussy_animation" pos (0.122, 0.583)
    # elif girl_secondary_action == "fondle_pussy":
    #     "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    # elif girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
    #     "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    # elif girl_secondary_action == "fondle_breasts":
    #     "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == StormX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and StormX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
    if not Player.primary_action or focused_Girl != StormX:
        Null()
    elif Player.primary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.12, 1.2)
    elif Player.primary_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.135, 0.645)
    elif Player.primary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.07, 0.64)
    elif Player.primary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.18, 0.98)
    elif Player.primary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.155, 1.17)
    elif Player.primary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.185, 1.07)

    if not Player.secondary_action or focused_Girl != StormX:
        Null()
    elif Player.secondary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.12, 1.2)
    elif Player.secondary_action == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.2, 0.69)
    elif Player.secondary_action == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.225, 0.67)
    elif Player.secondary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.18, 0.98)
    elif Player.secondary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.155, 1.17)
    elif Player.secondary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.185, 1.07)
#
#     if not second_girl_main_action or focused_Girl != StormX:
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
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and StormX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and StormX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not second_girl_secondary_action or focused_Girl == StormX:
#         Null()
#     elif second_girl_secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif second_girl_secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif second_girl_secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif second_girl_secondary_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif second_girl_secondary_action == "fondle_pussy" and Player.primary_action != "sex" and StormX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)

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
        "Storm_handjob_under_hand_animation[action_speed]" pos (0.08, 0.455) zoom 0.28

    always:
        "Zero_cock_Storm"

    always:
        "Storm_handjob_over_hand_animation[action_speed]" pos (0.08, 0.455) zoom 0.28

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
        ease 0.3 offset (-100,-115)
        ease 0.7 offset (-90,-155)
        pause 0.2
        ease 0.4 offset (-100,-105)
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
    if StormX.outfit["bra"] in ["_black_bra", "_lace_bra"]:
        "Storm_titjob_bra_back_animation[action_speed]"

    always:
        "Storm_titjob_hair_back_animation[action_speed]" pos (0.0, -0.15) zoom 0.9

    always:
        "Storm_titjob_body_animation[action_speed]"

    always:
        "Storm_titjob_head_animation[action_speed]" pos (0.0, -0.15) zoom 0.9

    if not StormX.outfit["bra"] == "_cosplay_bra":
        "Storm_titjob_breasts_under_animation[action_speed]"

    always:
        "Zero_cock_Storm"

    if StormX.outfit["bra"] in ["_sports_bra", "_bikini_top"]:
        "Storm_titjob_bra_stretch_animation[action_speed]"

    always:
        "Storm_titjob_breasts_animation[action_speed]"

    always:
        "Storm_titjob_hair_animation[action_speed]" pos (0.0, -0.15) zoom 0.9

    anchor (0.5, 0.0) offset (320, 700)

image Storm_blowjob_blinking:
    "images/Storm_blowjob/Storm_blowjob_eyes[StormX.eyes].png"
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
