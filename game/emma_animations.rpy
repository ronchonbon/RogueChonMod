image Emma_blinking:
    "images/Emma_standing/Emma_standing_eyes[EmmaX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Emma_standing/Emma_standing_eyes_squint.png"
    0.05
    "images/Emma_standing/Emma_standing_eyes_closed.png"
    0.15
    "images/Emma_standing/Emma_standing_eyes_squint.png"
    0.05
    repeat

image Emma_blinking_diamond:
    "images/Emma_standing/Emma_standing_eyes[EmmaX.eyes]_diamond.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Emma_standing/Emma_standing_eyes_squint_diamond.png"
    0.05
    "images/Emma_standing/Emma_standing_eyes_closed_diamond.png"
    0.15
    "images/Emma_standing/Emma_standing_eyes_squint_diamond.png"
    0.05
    repeat

layeredimage Emma_grool_dripping_animations:
    always:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if EmmaX.grool > 1 and not EmmaX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if EmmaX.grool > 1 and not EmmaX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if EmmaX.grool > 1 and not EmmaX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

layeredimage Emma_grool_animations:
    if EmmaX.grool and EmmaX.outfit["bottom"] == "_pants" and EmmaX.bottom_pulled_down:
        AlphaMask("Emma_grool_dripping_animations", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    elif EmmaX.grool and EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
        AlphaMask("Emma_grool_dripping_animations", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    elif EmmaX.grool and not EmmaX.pussy_covered:
        AlphaMask("Emma_grool_dripping_animations", "images/Emma_standing/Emma_standing_grool_mask.png")

layeredimage Emma_spunk_dripping_animations:
    always:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not EmmaX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not EmmaX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not EmmaX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

layeredimage Emma_spunk_animations:
    if (EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]) and EmmaX.outfit["bottom"] == "_pants" and EmmaX.bottom_pulled_down:
        AlphaMask("Emma_spunk_dripping_animations", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    elif (EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]) and EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
        AlphaMask("Emma_spunk_dripping_animations", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    elif (EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]) and not EmmaX.pussy_covered:
        AlphaMask("Emma_spunk_dripping_animations", "images/Emma_standing/Emma_standing_grool_mask.png")

layeredimage Emma_standing_fondling_animations:
    if main_action == "lesbian" or not girl_offhand_action or focused_Girl != EmmaX:
            Null()
    elif main_action != "sex" and girl_offhand_action in "finger_pussy" and EmmaX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif girl_offhand_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif girl_offhand_action == "fondle_breasts" and (Player.offhand_action in ["fondle_breasts", "suck breasts"]):
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif girl_offhand_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if second_girl_main_action != "masturbation" or not second_girl_offhand_action or focused_Girl == EmmaX:
        Null()
    elif main_action != "sex" and second_girl_offhand_action == "finger_pussy" and EmmaX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_offhand_action in "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_offhand_action == "fondle_breasts" and (Player.offhand_action in ["fondle_breasts", "suck breasts"]):
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_offhand_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if not main_action or focused_Girl != EmmaX:
        Null()
    elif main_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif main_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
    elif main_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif main_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.115, 0.59)
    elif main_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.12, 0.66)
    elif main_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if not Player.offhand_action or focused_Girl != EmmaX:
        Null()
    elif Player.offhand_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif main_action == "fondle_breasts" and not girl_offhand_action and not second_girl_main_action and not second_girl_offhand_action:
        "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
    elif Player.offhand_action == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.156, 0.39)
    elif Player.offhand_action == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif Player.offhand_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.115, 0.59)
    elif Player.offhand_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.12, 0.66)
    elif Player.offhand_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if not second_girl_main_action or focused_Girl != EmmaX:
        Null()
    elif second_girl_main_action == "fondle_breasts" and main_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_main_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif second_girl_main_action == "suck_breasts" and main_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts" and Player.offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif second_girl_main_action == "fondle_pussy" and main_action != "sex" and EmmaX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy" and Player.offhand_action != "sex" and EmmaX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_main_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if main_action != "lesbian" or not girl_offhand_action or focused_Girl == EmmaX:
        Null()
    elif girl_offhand_action == "fondle_breasts" and main_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif girl_offhand_action == "fondle_breasts" and Player.offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif girl_offhand_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif girl_offhand_action == "suck_breasts" and main_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif girl_offhand_action == "suck_breasts" and Player.offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif girl_offhand_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif girl_offhand_action == "fondle_pussy" and main_action != "sex" and EmmaX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif girl_offhand_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif girl_offhand_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)
