image Laura_blinking:
    "images/Laura_standing/Laura_standing_eyes[LauraX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Laura_standing/Laura_standing_eyes_squint.png"
    0.05
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.15
    "images/Laura_standing/Laura_standing_eyes_squint.png"
    0.05
    repeat

layeredimage Laura_grool_dripping_animations:
    always:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

    if LauraX.grool > 1 and not LauraX.pussy_covered:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

    if LauraX.grool > 1 and not LauraX.pussy_covered:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

    if LauraX.grool > 1 and not LauraX.pussy_covered:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

layeredimage Laura_grool_animations:
    if LauraX.grool and LauraX.outfit["bottom"] == "_pants" and LauraX.bottom_pulled_down:
        AlphaMask("Laura_grool_dripping_animations", "images/Laura_standing/Laura_standing_grool_mask_pants.png")
    elif LauraX.grool and LauraX.outfit["underwear"] and LauraX.underwear_pulled_down:
        AlphaMask("Laura_grool_dripping_animations", "images/Laura_standing/Laura_standing_grool_mask_underwear.png")
    elif LauraX.grool and not LauraX.pussy_covered:
        AlphaMask("Laura_grool_dripping_animations", "images/Laura_standing/Laura_standing_grool_mask.png")

layeredimage Laura_spunk_dripping_animations:
    always:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

    if not LauraX.pussy_covered:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

    if not LauraX.pussy_covered:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

    if not LauraX.pussy_covered:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

layeredimage Laura_spunk_animations:
    if (LauraX.spunk["pussy"] or LauraX.spunk["anus"]) and LauraX.outfit["bottom"] == "_pants" and LauraX.bottom_pulled_down:
        AlphaMask("Laura_spunk_dripping_animations", "images/Laura_standing/Laura_standing_grool_mask_pants.png")
    elif (LauraX.spunk["pussy"] or LauraX.spunk["anus"]) and LauraX.outfit["underwear"] and LauraX.underwear_pulled_down:
        AlphaMask("Laura_spunk_dripping_animations", "images/Laura_standing/Laura_standing_grool_mask_underwear.png")
    elif (LauraX.spunk["pussy"] or LauraX.spunk["anus"]) and not LauraX.pussy_covered:
        AlphaMask("Laura_spunk_dripping_animations", "images/Laura_standing/Laura_standing_grool_mask.png")

layeredimage Laura_standing_fondling_animations:
    if Player.main_action == "lesbian" or not LauraX.offhand_action or focused_Girl != LauraX:
            Null()
    elif Player.main_action != "sex" and LauraX.offhand_action in "finger_pussy" and LauraX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif LauraX.offhand_action == "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif LauraX.offhand_action == "fondle_breasts" and (Player.offhand_action in ["fondle_breasts", "suck breasts"]):
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif LauraX.offhand_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if second_girl_main_action != "masturbation" or not second_girl_offhand_action or focused_Girl == LauraX:
        Null()
    elif Player.main_action != "sex" and second_girl_offhand_action == "finger_pussy" and LauraX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_offhand_action in "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_offhand_action == "fondle_breasts" and (Player.offhand_action in ["fondle_breasts", "suck breasts"]):
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_offhand_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if not Player.main_action or focused_Girl != LauraX:
        Null()
    elif Player.main_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif Player.main_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
    elif Player.main_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif Player.main_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.115, 0.59)
    elif Player.main_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.12, 0.66)
    elif Player.main_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if not Player.offhand_action or focused_Girl != LauraX:
        Null()
    elif Player.offhand_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif Player.main_action == "fondle_breasts" and not LauraX.offhand_action and not second_girl_main_action and not second_girl_offhand_action:
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

    if not second_girl_main_action or focused_Girl != LauraX:
        Null()
    elif second_girl_main_action == "fondle_breasts" and Player.main_action in ["fondle_breasts", "suck_breasts"]:
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_main_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif second_girl_main_action == "suck_breasts" and Player.main_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts" and Player.offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif second_girl_main_action == "fondle_pussy" and Player.main_action != "sex" and LauraX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy" and Player.offhand_action != "sex" and LauraX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_main_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if Player.main_action != "lesbian" or not LauraX.offhand_action or focused_Girl == LauraX:
        Null()
    elif LauraX.offhand_action == "fondle_breasts" and Player.main_action in ["fondle_breasts", "suck_breasts"]:
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif LauraX.offhand_action == "fondle_breasts" and Player.offhand_action in ["fondle_breasts", "suck_breasts"]:
        "girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif LauraX.offhand_action == "fondle_breasts":
        "girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif LauraX.offhand_action == "suck_breasts" and Player.main_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif LauraX.offhand_action == "suck_breasts" and Player.offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif LauraX.offhand_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif LauraX.offhand_action == "fondle_pussy" and Player.main_action != "sex" and LauraX.lust >= 70:
        "girl_finger_pussy_animation" pos (0.122, 0.583)
    elif LauraX.offhand_action == "fondle_pussy":
        "girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif LauraX.offhand_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)
