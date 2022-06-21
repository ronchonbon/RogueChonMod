image Mystique_blinking:
    "images/Mystique_standing/Mystique_standing_eyes_normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Mystique_standing/Mystique_standing_eyes_closed.png"
    0.25
    repeat

image Raven_blinking:
    "images/Raven_standing/Raven_standing_eyes_normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Raven_standing/Raven_standing_eyes_closed.png"
    0.25
    repeat

layeredimage Mystique_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.295, 1.05)

    if MystiqueX.grool > 1 and not MystiqueX.pussy_covered:
        "grool_dripping_animation" pos (0.295, 1.05)

    if MystiqueX.grool > 1 and not MystiqueX.pussy_covered:
        "grool_dripping_animation" pos (0.295, 1.05)

    if MystiqueX.grool > 1 and not MystiqueX.pussy_covered:
        "grool_dripping_animation" pos (0.295, 1.05)

layeredimage Mystique_grool_animations:
    if not MystiqueX.grool:
        Null()
    elif MystiqueX.bottom_pulled_down:
        AlphaMask("Mystique_grool_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask_pants.png")
    elif MystiqueX.underwear_pulled_down:
        AlphaMask("Mystique_grool_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask_underwear.png")
    elif not MystiqueX.pussy_covered:
        AlphaMask("Mystique_grool_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask.png")

layeredimage Mystique_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.295, 1.05)

    if not MystiqueX.pussy_covered:
        "spunk_dripping_animation" pos (0.295, 1.05)

    if not MystiqueX.pussy_covered:
        "spunk_dripping_animation" pos (0.295, 1.05)

    if not MystiqueX.pussy_covered:
        "spunk_dripping_animation" pos (0.295, 1.05)

layeredimage Mystique_spunk_animations:
    if not MystiqueX.spunk["pussy"] and not MystiqueX.spunk["anus"]:
        Null()
    elif MystiqueX.bottom_pulled_down:
        AlphaMask("Mystique_spunk_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask_pants.png")
    elif MystiqueX.underwear_pulled_down:
        AlphaMask("Mystique_spunk_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask_underwear.png")
    elif not MystiqueX.pussy_covered:
        AlphaMask("Mystique_spunk_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask.png")

layeredimage Mystique_standing_fondling_animations:
    # if Player.primary_action == "lesbian" or not girl_secondary_action or focused_Girl != MystiqueX:
    #     Null()
    # elif Player.primary_action != "sex" and girl_secondary_action in "finger_pussy" and MystiqueX.lust >= 70:
    #     "Girl_finger_pussy_animation" pos (0.122, 0.583)
    # elif girl_secondary_action == "fondle_pussy":
    #     "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    # elif girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
    #     "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    # elif girl_secondary_action == "fondle_breasts":
    #     "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == MystiqueX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and MystiqueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
    if not Player.primary_action or focused_Girl != MystiqueX:
        Null()
    elif Player.primary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.215, 1.22)
    elif Player.primary_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.24, 0.675)
    elif Player.primary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.175, 0.605)
    elif Player.primary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.28, 1.0)
    elif Player.primary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.255, 1.17)
    elif Player.primary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.287, 1.1)

    if not Player.secondary_action or focused_Girl != MystiqueX:
        Null()
    elif Player.secondary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.215, 1.22)
    elif Player.secondary_action == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.29, 0.655)
    elif Player.secondary_action == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.315, 0.615)
    elif Player.secondary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.28, 1.0)
    elif Player.secondary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.255, 1.17)
    elif Player.secondary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.287, 1.1)
#
#     if not second_girl_main_action or focused_Girl != MystiqueX:
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
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and MystiqueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and MystiqueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not second_girl_secondary_action or focused_Girl == MystiqueX:
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
#     elif second_girl_secondary_action == "fondle_pussy" and Player.primary_action != "sex" and MystiqueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
