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

layeredimage Jubes_grool_dripping_animations:
    always:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if JubesX.grool > 1 and not JubesX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if JubesX.grool > 1 and not JubesX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if JubesX.grool > 1 and not JubesX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

layeredimage Jubes_grool_animations:
    if JubesX.grool and JubesX.outfit["bottom"] == "_pants" and JubesX.bottom_pulled_down:
        AlphaMask("Jubes_grool_dripping_animations", "images/Jubes_standing/Jubes_standing_grool_mask_pants.png")
    elif JubesX.grool and JubesX.outfit["underwear"] and JubesX.underwear_pulled_down:
        AlphaMask("Jubes_grool_dripping_animations", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")
    elif JubesX.grool and not JubesX.pussy_covered:
        AlphaMask("Jubes_grool_dripping_animations", "images/Jubes_standing/Jubes_standing_grool_mask.png")

layeredimage Jubes_spunk_dripping_animations:
    always:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not JubesX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not JubesX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not JubesX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

layeredimage Jubes_spunk_animations:
    if (JubesX.spunk["pussy"] or JubesX.spunk["anus"]) and JubesX.outfit["bottom"] == "_pants" and JubesX.bottom_pulled_down:
        AlphaMask("Jubes_spunk_dripping_animations", "images/Jubes_standing/Jubes_standing_grool_mask_pants.png")
    elif (JubesX.spunk["pussy"] or JubesX.spunk["anus"]) and JubesX.outfit["underwear"] and JubesX.underwear_pulled_down:
        AlphaMask("Jubes_spunk_dripping_animations", "images/Jubes_standing/Jubes_standing_grool_mask_underwear.png")
    elif (JubesX.spunk["pussy"] or JubesX.spunk["anus"]) and not JubesX.pussy_covered:
        AlphaMask("Jubes_spunk_dripping_animations", "images/Jubes_standing/Jubes_standing_grool_mask.png")

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
