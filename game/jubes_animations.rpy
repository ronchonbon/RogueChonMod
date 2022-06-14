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
