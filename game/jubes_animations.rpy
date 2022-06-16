image Jubes_blinking:
    "images/Jubes_standing/Jubes_standing_eyes[JubesX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jubes_standing/Jubes_standing_eyes_squint.png"
    0.05
    "images/Jubes_standing/Jubes_standing_eyes_closed.png"
    0.15
    "images/Jubes_standing/Jubes_standing_eyes_squint.png"
    0.05
    repeat

layeredimage Jubes_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.145, 0.57) zoom 0.2

    if JubesX.grool > 1 and not JubesX.pussy_covered:
        "grool_dripping_animation" pos (0.145, 0.57) zoom 0.2

    if JubesX.grool > 1 and not JubesX.pussy_covered:
        "grool_dripping_animation" pos (0.145, 0.57) zoom 0.2

    if JubesX.grool > 1 and not JubesX.pussy_covered:
        "grool_dripping_animation" pos (0.145, 0.57) zoom 0.2

layeredimage Jubes_grool_animations:
    if not JubesX.grool:
        Null()
    elif JubesX.outfit["bottom"] == "_pants" and JubesX.bottom_pulled_down:
        AlphaMask("Jubes_grool_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_pants.png")
    elif JubesX.outfit["underwear"] and JubesX.underwear_pulled_down:
        AlphaMask("Jubes_grool_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")
    elif not JubesX.pussy_covered:
        AlphaMask("Jubes_grool_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")

layeredimage Jubes_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.145, 0.57) zoom 0.3

    if not JubesX.pussy_covered:
        "spunk_dripping_animation" pos (0.145, 0.57) zoom 0.3

    if not JubesX.pussy_covered:
        "spunk_dripping_animation" pos (0.145, 0.57) zoom 0.3

    if not JubesX.pussy_covered:
        "spunk_dripping_animation" pos (0.145, 0.57) zoom 0.3

layeredimage Jubes_spunk_animations:
    if not JubesX.spunk["pussy"] and not JubesX.spunk["anus"]:
        Null()
    elif JubesX.outfit["bottom"] == "_pants" and JubesX.bottom_pulled_down:
        AlphaMask("Jubes_spunk_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_pants.png")
    elif JubesX.outfit["underwear"] and JubesX.underwear_pulled_down:
        AlphaMask("Jubes_spunk_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")
    elif not JubesX.pussy_covered:
        AlphaMask("Jubes_spunk_dripping_animation", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")

# layeredimage Jubes_standing_fondling_animations:
#     if Player.primary_action == "lesbian" or not JubesX.secondary_action or focused_Girl != JubesX:
#             Null()
#     elif Player.primary_action != "sex" and JubesX.secondary_action in "finger_pussy" and JubesX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif JubesX.secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif JubesX.secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif JubesX.secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == JubesX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and JubesX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action in "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if not Player.primary_action or focused_Girl != JubesX:
#         Null()
#     elif Player.primary_action == "fondle_thighs":
#         "Zero_fondle_thigh_animation" pos (0.11, 0.68)
#     elif Player.primary_action == "fondle_breasts":
#         "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
#     elif Player.primary_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif Player.primary_action == "fondle_pussy":
#         "Zero_fondle_pussy_animation" pos (0.115, 0.59)
#     elif Player.primary_action == "finger_pussy":
#         "Zero_finger_pussy_animation" pos (0.12, 0.66)
#     elif Player.primary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if not Player.secondary_action or focused_Girl != JubesX:
#         Null()
#     elif Player.secondary_action == "fondle_thighs":
#         "Zero_fondle_thigh_animation" pos (0.11, 0.68)
#     elif Player.primary_action == "fondle_breasts" and not JubesX.secondary_action and not second_girl_main_action and not second_girl_secondary_action:
#         "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
#     elif Player.secondary_action == "fondle_breasts":
#         "Zero_fondle_breasts_left_animation" pos (0.156, 0.39)
#     elif Player.secondary_action == "suck_breasts":
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif Player.secondary_action == "fondle_pussy":
#         "Zero_fondle_pussy_animation" pos (0.115, 0.59)
#     elif Player.secondary_action == "finger_pussy":
#         "Zero_finger_pussy_animation" pos (0.12, 0.66)
#     elif Player.secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if not second_girl_main_action or focused_Girl != JubesX:
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
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and JubesX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and JubesX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not JubesX.secondary_action or focused_Girl == JubesX:
#         Null()
#     elif JubesX.secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif JubesX.secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif JubesX.secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif JubesX.secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif JubesX.secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif JubesX.secondary_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif JubesX.secondary_action == "fondle_pussy" and Player.primary_action != "sex" and JubesX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif JubesX.secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif JubesX.secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)

image Jubes_handjob_under_hand_animation0:
    "Jubes_handjob_under"

image Jubes_handjob_under_hand_animation1:
    animation
    "Jubes_handjob_under"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate -10
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Jubes_handjob_under_hand_animation2:
    animation
    "Jubes_handjob_under"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate -7
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

image Jubes_handjob_over_hand_animation0:
    "Jubes_handjob_over"

image Jubes_handjob_over_hand_animation1:
    animation
    "Jubes_handjob_over"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate -10
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Jubes_handjob_over_hand_animation2:
    animation
    "Jubes_handjob_over"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate -7
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

layeredimage Jubes_sprite handjob:
    always:
        "Jubes_sprite standing" pos (0.05, 0.0)

    always:
        "Jubes_handjob_under_hand_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Jubes"

    always:
        "Jubes_handjob_over_hand_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Jubes_titjob_jacket_back_animation0:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_jacket_back_animation1:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 2 yoffset -50
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat

image Jubes_titjob_jacket_back_animation2:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 1 yoffset -5
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_jacket_back_animation3:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 1 yoffset 60
        pause 0.15
        ease 0.45 yoffset 110
        repeat

image Jubes_titjob_jacket_back_animation5:
    animation
    "Jubes_titjob_jacket_back"

    subpixel True
    block:
        ease 2 yoffset 130
        pause 0.2
        ease 2 yoffset 140
        pause 0.5
        repeat

image Jubes_titjob_bra_back_animation0:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_bra_back_animation1:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 50
        repeat

image Jubes_titjob_bra_back_animation2:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 60
        ease 0.7 yoffset -20
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_bra_back_animation3:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Jubes_titjob_bra_back_animation5:
    animation
    "Jubes_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

image Jubes_titjob_body_animation0:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_body_animation1:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 2 ypos -50
        pause 0.2
        ease 2 ypos 60
        pause 0.5
        repeat

image Jubes_titjob_body_animation2:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 1 yoffset -5
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_body_animation3:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 1 yoffset 60
        pause 0.15
        ease 0.45 yoffset 110
        repeat

image Jubes_titjob_body_animation5:
    animation
    "Jubes_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 130
        pause 0.2
        ease 2 yoffset 140
        pause 0.5
        repeat

image Jubes_titjob_head_animation0:
    animation
    "Jubes_blowjob_head"

    subpixel True
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -0.5
        pause 0.1
        ease 2 rotate 0
        repeat

image Jubes_titjob_head_animation1:
    animation
    "Jubes_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -40
        pause 0.2
        ease 2 yoffset 60
        pause 0.5
        repeat
    parallel:
        ease 2.3 rotate 0
        pause 0.2
        ease 2.2 rotate -5
        pause 0.5
        repeat

image Jubes_titjob_head_animation2:
    animation
    "Jubes_blowjob_head"

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

image Jubes_titjob_head_animation3:
    animation
    "Jubes_blowjob_head"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset 80
        pause 0.1
        ease 0.5 yoffset 140
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Jubes_titjob_head_animation5:
    animation
    "Jubes_blowjob_head"

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

image Jubes_titjob_breasts_under_animation0:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_breasts_under_animation1:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 50
        repeat

image Jubes_titjob_breasts_under_animation2:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        ease 0.3 yoffset 60
        ease 0.7 yoffset -20
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_breasts_under_animation3:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Jubes_titjob_breasts_under_animation5:
    animation
    "Jubes_titjob_breasts_under"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

image Jubes_titjob_breasts_animation0:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jubes_titjob_breasts_animation1:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -60
        pause 0.4
        ease 1.8 yoffset 60
        ease 0.5 yoffset 50
        repeat

image Jubes_titjob_breasts_animation2:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 60
        ease 0.7 yoffset -20
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jubes_titjob_breasts_animation3:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 100
        ease 0.7 yoffset 60
        pause 0.2
        ease 0.4 yoffset 110
        repeat

image Jubes_titjob_breasts_animation5:
    animation
    "Jubes_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset 100
        pause 0.2
        ease 2 yoffset 110
        pause 0.4
        repeat

layeredimage Jubes_sprite titjob:
    if JubesX.outfit["jacket"]:
        "Jubes_titjob_jacket_back_animation[action_speed]"

    if JubesX.outfit["bra"] in ["_sports_bra", "_bikini_top"]:
        "Jubes_titjob_bra_back_animation[action_speed]" pos (0.0, -0.06)

    always:
        "Jubes_titjob_body_animation[action_speed]"

    always:
        "Jubes_titjob_head_animation[action_speed]" pos (0.0, -0.19) zoom 0.9

    always:
        "Jubes_titjob_breasts_under_animation[action_speed]" pos (0.0, -0.06)

    always:
        "Zero_cock_Jubes"

    always:
        "Jubes_titjob_breasts_animation[action_speed]" pos (0.0, -0.06)

    anchor (0.5, 0.0) offset (360, 800) zoom 1.15

image Jubes_blowjob_blinking:
    "images/Jubes_blowjob/Jubes_blowjob_eyes[JubesX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jubes_blowjob/Jubes_blowjob_eyes_squint.png"
    0.05
    "images/Jubes_blowjob/Jubes_blowjob_eyes_closed.png"
    0.15
    "images/Jubes_blowjob/Jubes_blowjob_eyes_squint.png"
    0.05
    repeat
