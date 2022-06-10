image Rogue_blinking:
    "images/Rogue_blowjob/Rogue_blowjob_eyes[RogueX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_blowjob/Rogue_blowjob_eyes_squint.png"
    0.05
    "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    0.15
    "images/Rogue_blowjob/Rogue_blowjob_eyes_squint.png"
    0.05
    repeat

layeredimage Rogue_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.129, 0.6) zoom 0.2

    if RogueX.grool > 1 and not RogueX.pussy_covered:
        "grool_dripping_animation" pos (0.129, 0.6) zoom 0.2

    if RogueX.grool > 1 and not RogueX.pussy_covered:
        "grool_dripping_animation" pos (0.129, 0.6) zoom 0.2

    if RogueX.grool > 1 and not RogueX.pussy_covered:
        "grool_dripping_animation" pos (0.129, 0.6) zoom 0.2

layeredimage Rogue_grool_animations:
    if RogueX.grool and RogueX.outfit["bottom"] == "_pants" and RogueX.bottom_pulled_down:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif RogueX.grool and RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif RogueX.grool and not RogueX.pussy_covered:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask.png")

layeredimage Rogue_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.129, 0.6) zoom 0.3

    if not RogueX.pussy_covered:
        "spunk_dripping_animation" pos (0.129, 0.6) zoom 0.3

    if not RogueX.pussy_covered:
        "spunk_dripping_animation" pos (0.129, 0.6) zoom 0.3

    if not RogueX.pussy_covered:
        "spunk_dripping_animation" pos (0.129, 0.6) zoom 0.3

layeredimage Rogue_spunk_animations:
    if (RogueX.spunk["pussy"] or RogueX.spunk["anus"]) and RogueX.outfit["bottom"] == "_pants" and RogueX.bottom_pulled_down:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif (RogueX.spunk["pussy"] or RogueX.spunk["anus"]) and RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif (RogueX.spunk["pussy"] or RogueX.spunk["anus"]) and not RogueX.pussy_covered:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask.png")

# layeredimage Rogue_standing_fondling_animations:
#     if Player.primary_action == "lesbian" or not girl_secondary_action or focused_Girl != RogueX:
#         Null()
#     elif Player.primary_action != "sex" and girl_secondary_action in "finger_pussy" and RogueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif girl_secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == RogueX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and RogueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if not Player.primary_action or focused_Girl != RogueX:
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
#     if not Player.secondary_action or focused_Girl != RogueX:
#         Null()
#     elif Player.secondary_action == "fondle_thighs":
#         "Zero_fondle_thigh_animation" pos (0.11, 0.68)
#     elif Player.primary_action == "fondle_breasts" and not girl_secondary_action and not second_girl_main_action and not second_girl_secondary_action:
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
#     if not second_girl_main_action or focused_Girl != RogueX:
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
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and RogueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and RogueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not second_girl_secondary_action or focused_Girl == RogueX:
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
#     elif second_girl_secondary_action == "fondle_pussy" and Player.primary_action != "sex" and RogueX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)

image Rogue_handjob_under_hand_animation0:
    "Rogue_handjob_under"

image Rogue_handjob_under_hand_animation1:
    "Rogue_handjob_under"

    subpixel True
    block:
        ease 0.5 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_under_hand_animation2:
    "Rogue_handjob_under"

    subpixel True
    block:
        ease 0.2 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

image Rogue_handjob_over_hand_animation0:
    "Rogue_handjob_over"

image Rogue_handjob_over_hand_animation1:
    "Rogue_handjob_over"

    subpixel True
    block:
        ease 0.5 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_over_hand_animation2:
    "Rogue_handjob_over"

    subpixel True
    block:
        ease 0.2 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

layeredimage Rogue_sprite handjob:
    always:
        "Rogue_sprite standing" pos (0.05, 0.0)

    always:
        "Rogue_handjob_under_hand_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    always:
        "Rogue_handjob_cock_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    always:
        "Rogue_handjob_over_hand_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Rogue_titjob_under_tits_animation0:
    "Rogue_titjob_under"

image Rogue_titjob_under_tits_animation1:
    "Rogue_titjob_under"

    subpixel True
    block:
        ease 1.0 yoffset 100
        ease 0.2 yoffset 100
        ease 1.3 yoffset -80
        repeat

image Rogue_titjob_under_tits_animation2:
    "Rogue_titjob_under"

    subpixel True
    block:
        ease 0.25 yoffset 0
        ease 0.4 yoffset -80
        ease 0.1 yoffset -75
        repeat

image Rogue_titjob_over_tits_animation0:
    "Rogue_titjob_over"

image Rogue_titjob_over_tits_animation1:
    "Rogue_titjob_over"

    subpixel True
    block:
        ease 1.20 yoffset 100
        ease 0.1 yoffset 100
        ease 1.2 yoffset -80
        repeat

image Rogue_titjob_over_tits_animation2:
    "Rogue_titjob_over"

    subpixel True
    block:
        ease 0.3 yoffset 0
        ease 0.35 yoffset -80
        ease 0.1 yoffset -75
        repeat

layeredimage Rogue_sprite titjob:
    always:
        "Rogue_titjob_under_tits_animation[action_speed]" pos (-0.043, 0.8)

    always:
        "Rogue_titjob_cock_animation[action_speed]" pos (-0.05, 1.0) zoom 0.65

    always:
        "Rogue_titjob_over_tits_animation[action_speed]" pos (-0.043, 0.8)

    anchor (0.5, 0.0) offset (200, 250) zoom 0.72

image Rogue_blowjob_back_hair_animation0:
    "Rogue_back_hair"

    ease 1.5 offset (0, 0)

image Rogue_blowjob_back_hair_animation1:
    "Rogue_back_hair"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (15, 60)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_back_hair_animation2:
    "Rogue_back_hair"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_back_hair_animation3:
    "Rogue_back_hair"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_back_hair_animation4:
    "Rogue_back_hair"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

image Rogue_blowjob_body_animation0:
    "Rogue_sprite standing"

    ease 1.5 offset (0, 0)

image Rogue_blowjob_body_animation1:
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (20, 55)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_body_animation2:
    "Rogue_sprite standing"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_body_animation3:
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 yoffset 45
        ease 1.5 yoffset 30
        repeat

image Rogue_blowjob_body_animation4:
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1.2 yoffset 70
        pause 0.5
        ease 1.8 yoffset 40
        repeat

image Rogue_blowjob_head_animation0:
    "Rogue_head"

    ease 1.5 offset (0, 0)

image Rogue_blowjob_head_animation1:
    "Rogue_head"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (15, 60)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_head_animation2:
    "Rogue_head"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_head_animation3:
    "Rogue_head"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_head_animation4:
    "Rogue_head"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

image Rogue_blowjob_mouth_animation0:
    "Rogue_blowjob_mouth"

image Rogue_blowjob_mouth_animation1:
    "Rogue_blowjob_mouth"

image Rogue_blowjob_mouth_animation2:
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.94
    block:
        pause 0.10
        ease 0.55 zoom 0.94
        linear 0.10 zoom 0.84
        ease 0.30 zoom 0.94
        pause 0.15
        ease 0.40 zoom 0.84
        linear 0.10 zoom 0.94
        ease 0.45 zoom 0.6
        pause 0.35
        repeat

image Rogue_blowjob_mouth_animation3:
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.9
    block:
        ease 0.5 zoom 0.9
        ease 0.5 zoom 0.97
        ease 0.75 zoom 0.94
        ease 0.75 zoom 0.97
        repeat

image Rogue_blowjob_mouth_animation4:
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.94
    block:
        ease 0.25 zoom 0.94
        ease 0.25 zoom 1.0
        pause 0.5
        ease 1.0 zoom 0.96
        ease 1.0 zoom 1.0
        repeat

image Rogue_blowjob_mask_animation2:
    "Rogue_blowjob_mask"

    subpixel True
    zoom 0.94
    block:
        pause 0.10
        ease 0.55 zoom 0.94
        linear 0.10 zoom 0.84
        ease 0.30 zoom 0.94
        pause 0.15
        ease 0.40 zoom 0.84
        linear 0.10 zoom 0.94
        ease 0.45 zoom 0.6
        pause 0.35
        repeat

image Rogue_blowjob_mask_animation3:
    "Rogue_blowjob_mask"

    subpixel True
    zoom 0.9
    block:
        ease 0.5 zoom 0.9
        ease 0.5 zoom 0.97
        ease 0.75 zoom 0.94
        ease 0.75 zoom 0.97
        repeat

image Rogue_blowjob_mask_animation4:
    "Rogue_blowjob_mask"

    subpixel True
    zoom 0.94
    block:
        ease 0.25 zoom 0.94
        ease 0.25 zoom 1.0
        pause 0.5
        ease 1.0 zoom 0.96
        ease 1.0 zoom 1.0
        repeat

image Rogue_blowjob_face_mask_animation2:
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation2")

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_face_mask_animation3:
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation3")

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_face_mask_animation4:
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation4")

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

layeredimage Rogue_sprite blowjob:
    always:
        "Rogue_blowjob_back_hair_animation[action_speed]" pos (0.031, 0.317) zoom 0.2755

    always:
        "Rogue_blowjob_body_animation[action_speed]"

    always:
        "Rogue_blowjob_head_animation[action_speed]" pos (0.031, 0.317) zoom 0.2755

    always:
        "Rogue_blowjob_cock_animation[action_speed]" pos (0.02272, 0.462) zoom 0.2755

    if action_speed > 1:
        "Rogue_blowjob_face_mask_animation[action_speed]" anchor (0.5, 0.5) pos (0.031, 0.317) zoom 0.2755

    anchor (0.5, 0.0) offset (220, -320) zoom 2.75

image Rogue_sex_body_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_animation1:
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.5
        ease 0.75 yoffset -5
        pause 1.25
        ease 2.5 yoffset 0
        repeat

image Rogue_sex_body_animation2:
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.6
        ease 0.4 yoffset -10
        ease 0.25 yoffset -5
        pause 1
        ease 2.75 yoffset 10
        repeat

image Rogue_sex_body_animation3:
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.17
        ease 0.13 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 10
        repeat

image Rogue_sex_body_footjob_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_footjob_animation1:
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.5
        ease 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 2.50 yoffset 15
        repeat

image Rogue_sex_body_footjob_animation2:
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.2
        ease 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        repeat

image Rogue_sex_body_hotdog_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_hotdog_animation1:
    "Rogue_sex_body"

image Rogue_sex_body_hotdog_animation2:
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.30
        ease 0.50 yoffset -10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Rogue_sex_body_hotdog_animation3:
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.30
        ease 0.50 yoffset -10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Rogue_sex_legs_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_animation1:
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.25
        ease 1 yoffset -5
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation2:
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.5
        ease 0.5 yoffset -15
        ease 0.25 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation3:
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.15
        ease 0.15 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 0
        repeat

image Rogue_sex_legs_footjob_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_footjob_animation1:
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.5
        ease 1.0 yoffset -25
        ease 0.5 yoffset -20
        pause 1
        ease 2. yoffset 25
        repeat

image Rogue_sex_legs_footjob_animation2:
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.2
        ease 0.5 yoffset -25
        ease 0.3 yoffset -20
        pause 0.2
        ease 0.8 yoffset 25
        repeat

image Rogue_sex_legs_hotdog_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_hotdog_animation1:
    "Rogue_sex_legs"

image Rogue_sex_legs_hotdog_animation2:
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Rogue_sex_legs_hotdog_animation3:
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Rogue_sex_anus_animation0:
    "Rogue_sex_anus"

    xzoom 0.6

image Rogue_sex_anus_animation1:
    "Rogue_sex_anus"

    subpixel True
    xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_sex_anus_animation2:
    "Rogue_sex_anus"

image Rogue_sex_anus_animation3:
    "Rogue_sex_anus"

image Rogue_sex_spunk_anus_under_animation:
    "Rogue_sex_spunk_anus"

    subpixel True
    xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.95
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

layeredimage Rogue_sex_spunk_anus_animations:
    if Player.sprite and Player.cock_position == "anal" and action_speed > 1:
        "Rogue_sex_spunk_anus" pos (0.292, 0.386)
    elif Player.sprite and Player.cock_position == "anal" and action_speed == 1:
        "Rogue_sex_spunk_anus_under_animation" pos (0.292, 0.386)
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anus_closed.png"

layeredimage Rogue_sprite sex:
    if Player.cock_position in ["in", "anal"]:
        "Rogue_sex_body_animation[action_speed]"
    elif Player.cock_position == "footjob":
        "Rogue_sex_body_footjob_animation[action_speed]"
    elif Player.cock_position == "out":
        "Rogue_sex_body_hotdog_animation[action_speed]"

    if Player.cock_position in ["in", "anal"]:
        "Rogue_sex_legs_animation[action_speed]"
    elif Player.cock_position == "footjob":
        "Rogue_sex_legs_footjob_animation[action_speed]"
    elif Player.cock_position == "out":
        "Rogue_sex_legs_hotdog_animation[action_speed]"

    anchor (0.5, 0.0) offset (370, 770) zoom 1.1

image Rogue_doggy_blinking:
    "images/Rogue_doggy/Rogue_doggy_eyes[RogueX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_doggy/Rogue_doggy_eyes_sexy.png"
    0.05
    "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"
    0.15
    "images/Rogue_doggy/Rogue_doggy_eyes_sexy.png"
    0.05
    repeat

image Rogue_doggy_body_animation0:
    "Rogue_doggy_body"

image Rogue_doggy_body_animation1:
    "Rogue_doggy_body"

    subpixel True
    block:
        pause 0.4
        ease 0.3 yoffset -5
        ease 1 yoffset 0
        pause 0.8
        repeat

image Rogue_doggy_body_animation2:
    "Rogue_doggy_body"

    subpixel True
    offset (0, 15)
    block:
        pause 0.4
        ease 0.2 yoffset 5
        pause 0.3
        ease 2 yoffset 15
        repeat

image Rogue_doggy_body_animation3:
    "Rogue_doggy_body"

    subpixel True
    offset (0, 20)
    block:
        pause 0.15
        ease 0.1 yoffset 0
        pause 0.1
        ease 0.5 yoffset 20
        pause 0.05
        repeat

image Rogue_doggy_ass_animation0:
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation1:
    "Rogue_doggy_ass"

    subpixel True
    block:
        pause 0.4
        ease 0.2 yoffset -10
        ease 0.1 yoffset -7
        ease 0.9 yoffset 0
        pause 0.9
        repeat

image Rogue_doggy_ass_animation2:
    "Rogue_doggy_ass"

    subpixel True
    block:
        pause 0.4
        ease 0.2 yoffset -15
        ease 0.1 yoffset -5
        pause 0.2
        ease 1.6 yoffset 0
        repeat

image Rogue_doggy_ass_animation3:
    "Rogue_doggy_ass"

    subpixel True
    offset (0, 5)
    block:
        pause 0.15
        ease 0.1 yoffset -25
        ease 0.1 yoffset -15
        pause 0.1
        ease 0.4 yoffset 5
        pause 0.05
        repeat

image Rogue_doggy_pussy_hole_animation0:
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation1:
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation2:
    "Rogue_doggy_pussy_hole"

image Rogue_doggy_pussy_hole_animation3:
    "Rogue_doggy_pussy_hole"

image Rogue_doggy_pussy_mask_animation0:
    "Rogue_doggy_pussy_mask"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_mask_animation1:
    "Rogue_doggy_pussy_mask"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_mask_animation2:
    "Rogue_doggy_pussy_mask"

image Rogue_doggy_pussy_mask_animation3:
    "Rogue_doggy_pussy_mask"

layeredimage Rogue_doggy_pussy_mask_animations:
    always:
        "Rogue_doggy_pussy_mask_animation[action_speed]" offset (217, 514)

image Rogue_doggy_pussy_fingering:
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.9
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_anus_anal_animation1:
    "Rogue_doggy_anus_hole"

    subpixel True
    zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Rogue_doggy_anus_anal_animation2:
    "Rogue_doggy_anus_hole"

    zoom 0.9

image Rogue_doggy_anus_anal_animation3:
    "Rogue_doggy_anus_hole"

    zoom 0.9

image Rogue_doggy_anus_mask_animation0:
    "Rogue_doggy_anus_mask"

image Rogue_doggy_anus_mask_animation1:
    "Rogue_doggy_anus_mask"

    subpixel True
    zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Rogue_doggy_anus_mask_animation2:
    "Rogue_doggy_anus_mask"

    zoom 0.9

image Rogue_doggy_anus_mask_animation3:
    "Rogue_doggy_anus_mask"

    zoom 0.9

layeredimage Rogue_doggy_anus_mask_animations:
    if Player.sprite and Player.cock_position == "anal":
        "Rogue_doggy_anus_mask_animation[action_speed]" offset (217, 514)
    elif Player.primary_action == "dildo_ass":
        "Rogue_doggy_anus_mask_animation1" offset (217, 514)

image Rogue_doggy_anus_fingering:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"

    subpixel True
    anchor (0.52, 0.69) zoom 0.6
    block:
        ease 0.5 zoom 0.75
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

image Rogue_doggy_anus_fingering_mask_animation:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    subpixel True
    anchor (0.52, 0.69) zoom 0.6
    block:
        ease 0.5 zoom 0.75
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

layeredimage Rogue_doggy_anus_fingering_mask_animations:
    always:
        "Rogue_doggy_anus_fingering_mask_animation" offset (217, 514)

image Rogue_doggy_shin_animation0:
    "Rogue_doggy_shins"

    subpixel True
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Rogue_doggy_shin_animation1:
    "Rogue_doggy_shins"

    subpixel True
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Rogue_doggy_shin_animation2:
    "Rogue_doggy_shins"

    subpixel True
    block:
        pause 0.05
        ease 0.6 yoffset 110
        ease 0.3 yoffset 0
        repeat

layeredimage Rogue_doggy_shin_animations:
    always:
        "Rogue_doggy_shin_animation[action_speed]"

image Rogue_doggy_feet_animation0:
    "Rogue_doggy_feet"

    subpixel True
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Rogue_doggy_feet_animation1:
    "Rogue_doggy_feet"

    subpixel True
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Rogue_doggy_feet_animation2:
    "Rogue_doggy_feet"

    subpixel True
    block:
        pause 0.05
        ease 0.6 yoffset 110
        ease 0.3 yoffset 0
        repeat

layeredimage Rogue_doggy_feet_animations:
    always:
        "Rogue_doggy_feet_animation[action_speed]"

layeredimage Rogue_sprite doggy:
    if Player.cock_position == "anal":
        "Rogue_doggy_body_animation[action_speed]"
    elif Player.cock_position == "in" and action_speed > 1:
        "Rogue_doggy_body_animation[action_speed]"
    else:
        "Rogue_doggy_body"

    if Player.cock_position == "anal":
        "Rogue_doggy_ass_animation[action_speed]"
    elif Player.cock_position == "in" and action_speed > 1:
        "Rogue_doggy_ass_animation[action_speed]"
    else:
        "Rogue_doggy_ass"

    if Player.sprite and Player.cock_position == "footjob":
        "Rogue_doggy_shin_animation[action_speed]"
    elif not Player.sprite or show_feet:
        "Rogue_doggy_shins"

    if Player.sprite and Player.cock_position == "footjob":
        "Rogue_doggy_cock_footjob_animation[action_speed]" pos (-0.005, 0.24) zoom 1.1

    if Player.cock_position == "footjob":
        "Rogue_doggy_feet_animation[action_speed]"
    elif not Player.sprite or show_feet:
        "Rogue_doggy_feet"

    anchor (0.5, 0.0) offset (150, 700) zoom 1.2
