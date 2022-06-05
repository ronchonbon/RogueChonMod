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

layeredimage Storm_grool_dripping_animations:
    always:
        "grool_dripping_animation" pos (0.092, 0.5) zoom 0.2

    if StormX.grool > 1 and not StormX.pussy_covered:
        "grool_dripping_animation" pos (0.092, 0.5) zoom 0.2

    if StormX.grool > 1 and not StormX.pussy_covered:
        "grool_dripping_animation" pos (0.092, 0.5) zoom 0.2

    if StormX.grool > 1 and not StormX.pussy_covered:
        "grool_dripping_animation" pos (0.092, 0.5) zoom 0.2

layeredimage Storm_grool_animations:
    if StormX.grool and StormX.outfit["bottom"] == "_pants" and StormX.bottom_pulled_down:
        AlphaMask("Storm_grool_dripping_animations", "images/Storm_standing/Storm_standing_grool_mask_pants.png")
    elif StormX.grool and StormX.outfit["underwear"] and StormX.underwear_pulled_down:
        AlphaMask("Storm_grool_dripping_animations", "images/Storm_standing/Storm_standing_grool_mask_underwear.png")
    elif StormX.grool and not StormX.pussy_covered:
        AlphaMask("Storm_grool_dripping_animations", "images/Storm_standing/Storm_standing_grool_mask.png")

layeredimage Storm_spunk_dripping_animations:
    always:
        "spunk_dripping_animation" pos (0.092, 0.5) zoom 0.3

    if not StormX.pussy_covered:
        "spunk_dripping_animation" pos (0.092, 0.5) zoom 0.3

    if not StormX.pussy_covered:
        "spunk_dripping_animation" pos (0.092, 0.5) zoom 0.3

    if not StormX.pussy_covered:
        "spunk_dripping_animation" pos (0.092, 0.5) zoom 0.3

layeredimage Storm_spunk_animations:
    if (StormX.spunk["pussy"] or StormX.spunk["anus"]) and StormX.outfit["bottom"] == "_pants" and StormX.bottom_pulled_down:
        AlphaMask("Storm_spunk_drippsing_animations", "images/Storm_standing/Storm_standing_grool_mask_pants.png")
    elif (StormX.spunk["pussy"] or StormX.spunk["anus"]) and StormX.outfit["underwear"] and StormX.underwear_pulled_down:
        AlphaMask("Storm_spunk_dripping_animations", "images/Storm_standing/Storm_standing_grool_mask_underwear.png")
    elif (StormX.spunk["pussy"] or StormX.spunk["anus"]) and not StormX.pussy_covered:
        AlphaMask("Storm_spunk_dripping_animations", "images/Storm_standing/Storm_standing_grool_mask.png")

layeredimage Storm_standing_fondling_animations:
    if Player.primary_action == "lesbian" or not StormX.secondary_action or focused_Girl != StormX:
            Null()
    elif Player.primary_action != "sex" and StormX.secondary_action in "finger_pussy" and StormX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif StormX.secondary_action == "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif StormX.secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif StormX.secondary_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == StormX:
        Null()
    elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and StormX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_secondary_action in "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_secondary_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if not Player.primary_action or focused_Girl != StormX:
        Null()
    elif Player.primary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif Player.primary_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
    elif Player.primary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif Player.primary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.115, 0.59)
    elif Player.primary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.12, 0.66)
    elif Player.primary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if not Player.secondary_action or focused_Girl != StormX:
        Null()
    elif Player.secondary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif Player.primary_action == "fondle_breasts" and not StormX.secondary_action and not second_girl_main_action and not second_girl_secondary_action:
        "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
    elif Player.secondary_action == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.156, 0.39)
    elif Player.secondary_action == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif Player.secondary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.115, 0.59)
    elif Player.secondary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.12, 0.66)
    elif Player.secondary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if not second_girl_main_action or focused_Girl != StormX:
        Null()
    elif second_girl_main_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_main_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif second_girl_main_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and StormX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and StormX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_main_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if Player.primary_action != "lesbian" or not StormX.secondary_action or focused_Girl == StormX:
        Null()
    elif StormX.secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif StormX.secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif StormX.secondary_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif StormX.secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif StormX.secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif StormX.secondary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif StormX.secondary_action == "fondle_pussy" and Player.primary_action != "sex" and StormX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif StormX.secondary_action == "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif StormX.secondary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)
