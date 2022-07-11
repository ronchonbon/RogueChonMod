image Mystique_blinking:
    "images/Mystique_standing/Mystique_standing_eyes_normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Mystique_standing/Mystique_standing_eyes_half.png"
    0.05
    "images/Mystique_standing/Mystique_standing_eyes_closed.png"
    0.15
    "images/Mystique_standing/Mystique_standing_eyes_half.png"
    0.05
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
        "grool_dripping_animation" pos (0.495, 1.05)

    if MystiqueX.grool > 1 and not MystiqueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.495, 1.05)

    if MystiqueX.grool > 1 and not MystiqueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.495, 1.05)

    if MystiqueX.grool > 1 and not MystiqueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.495, 1.05)

layeredimage Mystique_grool_animations:
    if not MystiqueX.grool:
        Null()
    elif MystiqueX.Clothes["dress"].string:
        AlphaMask("Mystique_grool_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask_dress.png")
    elif not MystiqueX.Outfit.pussy_covered:
        AlphaMask("Mystique_grool_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask.png")

layeredimage Mystique_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.495, 1.05)

    if not MystiqueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.495, 1.05)

    if not MystiqueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.495, 1.05)

    if not MystiqueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.495, 1.05)

layeredimage Mystique_spunk_animations:
    if not MystiqueX.spunk["pussy"] and not MystiqueX.spunk["anus"]:
        Null()
    elif MystiqueX.Clothes["dress"].string:
        AlphaMask("Mystique_grool_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask_dress.png")
    elif not MystiqueX.Outfit.pussy_covered:
        AlphaMask("Mystique_grool_dripping_animation", "images/Mystique_standing/Mystique_standing_grool_mask.png")

layeredimage Mystique_standing_fondling_animations:
    if MystiqueX.primary_Action.Target != MystiqueX:
        Null()
    elif MystiqueX.primary_Action.type == "fondle_breasts":
        "Mystique_fondle_breast_right_animation" pos (0.395, 0.621)
    elif MystiqueX.primary_Action.type == "fondle_pussy":
        "Mystique_fondle_pussy_animation" pos (0.475, 0.995)
    elif MystiqueX.primary_Action.type in "finger_pussy":
        "Mystique_finger_pussy_animation" pos (0.485, 1.06)

    if MystiqueX.secondary_Action.Target != MystiqueX:
        Null()
    elif MystiqueX.secondary_Action.type == "fondle_breasts":
        "Mystique_fondle_breast_left_animation" pos (0.518, 0.633)
    elif MystiqueX.secondary_Action.type == "fondle_pussy":
        "Mystique_fondle_pussy_animation" pos (0.475, 0.995)
    elif MystiqueX.secondary_Action.type in "finger_pussy":
        "Mystique_finger_pussy_animation" pos (0.485, 1.06)

    if Player.primary_Action.Target != MystiqueX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.415, 1.22)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.49, 0.61)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.505, 0.57)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.485, 0.985)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.455, 1.18)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.49, 1.09)

    if Player.secondary_Action.Target != MystiqueX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.415, 1.22)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.44, 0.625)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.38, 0.57)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.485, 0.985)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.455, 1.18)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.49, 1.09)
