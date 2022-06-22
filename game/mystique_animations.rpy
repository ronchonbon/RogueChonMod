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
    if not girl_secondary_action:
        Null()
    elif girl_secondary_action == "fondle_breasts":
        "Girl_fondle_breast_left_animation" pos (0.518, 0.633)
    elif girl_secondary_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.395, 0.621)
    elif girl_secondary_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.475, 0.995)
    elif girl_secondary_action in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.485, 1.06)

    if not Player.primary_action:
        Null()
    elif Player.primary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.415, 1.22)
    elif Player.primary_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.44, 0.625)
    elif Player.primary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.38, 0.57)
    elif Player.primary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.485, 0.985)
    elif Player.primary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.455, 1.18)
    elif Player.primary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.49, 1.09)

    if not Player.secondary_action:
        Null()
    elif Player.secondary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.415, 1.22)
    elif Player.secondary_action == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.49, 0.61)
    elif Player.secondary_action == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.505, 0.57)
    elif Player.secondary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.485, 0.985)
    elif Player.secondary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.455, 1.18)
    elif Player.secondary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.49, 1.09)
