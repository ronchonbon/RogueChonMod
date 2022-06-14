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

layeredimage Emma_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if EmmaX.grool > 1 and not EmmaX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if EmmaX.grool > 1 and not EmmaX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

    if EmmaX.grool > 1 and not EmmaX.pussy_covered:
        "grool_dripping_animation" pos (0.115, 0.55) zoom 0.2

layeredimage Emma_grool_animations:
    if not EmmaX.grool:
        Null()
    elif EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
        AlphaMask("Emma_grool_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    elif EmmaX.pussy_covered:
        AlphaMask("Emma_grool_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask.png")

layeredimage Emma_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not EmmaX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not EmmaX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

    if not EmmaX.pussy_covered:
        "spunk_dripping_animation" pos (0.115, 0.55) zoom 0.3

layeredimage Emma_spunk_animations:
    if not EmmaX.spunk["pussy"] and not EmmaX.spunk["anus"]:
        Null()
    elif EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
        AlphaMask("Emma_spunk_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    elif not EmmaX.pussy_covered:
        AlphaMask("Emma_spunk_dripping_animation", "images/Emma_standing/Emma_standing_grool_mask.png")

# layeredimage Emma_standing_fondling_animations:
#     if Player.primary_action == "lesbian" or not EmmaX.secondary_action or focused_Girl != EmmaX:
#             Null()
#     elif Player.primary_action != "sex" and EmmaX.secondary_action in "finger_pussy" and EmmaX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif EmmaX.secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif EmmaX.secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif EmmaX.secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == EmmaX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and EmmaX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action in "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if not Player.primary_action or focused_Girl != EmmaX:
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
#     if not Player.secondary_action or focused_Girl != EmmaX:
#         Null()
#     elif Player.secondary_action == "fondle_thighs":
#         "Zero_fondle_thigh_animation" pos (0.11, 0.68)
#     elif Player.primary_action == "fondle_breasts" and not EmmaX.secondary_action and not second_girl_main_action and not second_girl_secondary_action:
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
#     if not second_girl_main_action or focused_Girl != EmmaX:
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
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and EmmaX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and EmmaX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not EmmaX.secondary_action or focused_Girl == EmmaX:
#         Null()
#     elif EmmaX.secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif EmmaX.secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif EmmaX.secondary_action == "fondle_breasts":
#         "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif EmmaX.secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif EmmaX.secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif EmmaX.secondary_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif EmmaX.secondary_action == "fondle_pussy" and Player.primary_action != "sex" and EmmaX.lust >= 70:
#         "Girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif EmmaX.secondary_action == "fondle_pussy":
#         "Girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif EmmaX.secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)

image Emma_handjob_under_hand_animation0:
    "Emma_handjob_under"

image Emma_handjob_under_hand_animation1:
    animation
    "Emma_handjob_under"

    subpixel True
    rotate 8
    block:
        ease 0.75 yoffset 40 rotate 3
        pause 0.25
        ease 1.0 yoffset -10 rotate 8
        pause 0.1
        repeat

image Emma_handjob_under_hand_animation2:
    animation
    "Emma_handjob_under"

    subpixel True
    rotate 5
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate 5
        pause 0.1
        repeat

image Emma_handjob_over_hand_animation0:
    "Emma_handjob_over"

image Emma_handjob_over_hand_animation1:
    animation
    "Emma_handjob_over"

    subpixel True
    rotate 8
    block:
        ease 0.75 yoffset 40 rotate 3
        pause 0.25
        ease 1.0 yoffset -10 rotate 8
        pause 0.1
        repeat

image Emma_handjob_over_hand_animation2:
    animation
    "Emma_handjob_over"

    subpixel True
    rotate 5
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset -10 rotate 5
        pause 0.1
        repeat

layeredimage Emma_sprite handjob:
    always:
        "Emma_sprite standing" pos (0.05, 0.0)

    always:
        "Emma_handjob_under_hand_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Emma"

    always:
        "Emma_handjob_over_hand_animation[action_speed]" pos (-0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Emma_titjob_back_hair_animation0:
    animation
    "Emma_blowjob_back_hair"

    subpixel True
    block:
        ease 2.4 yoffset -10
        ease 1.6 yoffset 0
        repeat

image Emma_titjob_back_hair_animation1:
    animation
    "Emma_blowjob_back_hair"

    subpixel True
    block:
        pause 0.2
        ease 1.4 yoffset -10
        pause 0.3
        ease 0.6 yoffset 0
        repeat

image Emma_titjob_back_hair_animation2:
    animation
    "Emma_blowjob_back_hair"

    subpixel True
    block:
        pause 0.1
        ease 0.6 yoffset 0
        ease 0.3 yoffset 20
        repeat

image Emma_titjob_back_hair_animation3:
    animation
    "Emma_blowjob_back_hair"

    subpixel True
    block:
        ease 1.5 yoffset 10
        pause 0.7
        ease 0.3 yoffset 40
        pause 0.5
        repeat

image Emma_titjob_body_animation0:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        ease 2 yoffset -5
        ease 2 yoffset 5
        repeat

image Emma_titjob_body_animation1:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        pause 0.2
        ease 1.4 yoffset -20
        pause 0.3
        ease 0.6 yoffset 0
        repeat

image Emma_titjob_body_animation2:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        pause 0.1
        ease 0.5 yoffset -20
        ease 0.3 yoffset 15
        pause 0.1
        repeat

image Emma_titjob_body_animation3:
    animation
    "Emma_sex_body"

    subpixel True
    block:
        ease 1.6 yoffset -20
        pause 0.7
        ease 0.2 yoffset 0
        pause 0.5
        repeat

image Emma_titjob_head_animation0:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        ease 2.4 yoffset -10
        ease 1.6 yoffset 0
        repeat

image Emma_titjob_head_animation1:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        pause 0.2
        ease 1.4 yoffset -10
        pause 0.3
        ease 0.6 yoffset 0
        repeat

image Emma_titjob_head_animation2:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        pause 0.1
        ease 0.6 yoffset 0
        ease 0.3 yoffset 20
        repeat

image Emma_titjob_head_animation3:
    animation
    "Emma_blowjob_head"

    subpixel True
    block:
        ease 1.5 yoffset 10
        pause 0.7
        ease 0.3 yoffset 40
        pause 0.5
        repeat

image Emma_titjob_breasts_animation0:
    animation
    "Emma_titjob_breasts"

    subpixel True
    rotate -3
    block:
        ease 1.5 rotate 4
        pause 0.1
        ease 1.5 rotate -3
        pause 0.1
        repeat

image Emma_titjob_breasts_animation1:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 1.5 yoffset -40
        pause 0.3
        ease 0.7 yoffset 20
        repeat

image Emma_titjob_breasts_animation2:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 0.6 yoffset -50
        ease 0.3 yoffset 10
        pause 0.1
        repeat

image Emma_titjob_breasts_animation3:
    animation
    "Emma_titjob_breasts"

    subpixel True
    block:
        ease 1.8 yoffset -30
        pause 0.3
        ease 0.4 yoffset 20
        pause 0.5
        repeat

layeredimage Emma_sprite titjob:
    always:
        "Emma_titjob_back_hair_animation[action_speed]" pos (0.0, -0.24) zoom 0.56

    always:
        "Emma_titjob_body_animation[action_speed]"

    always:
        "Emma_titjob_head_animation[action_speed]" pos (0.0, -0.24) zoom 0.56

    always:
        "Zero_cock_Emma"

    always:
        "Emma_titjob_breasts_animation[action_speed]" pos (0.0, -0.02)

    anchor (0.5, 0.0) offset (640, 980) zoom 1.7

image Emma_blowjob_blinking:
    "images/Emma_blowjob/Emma_blowjob_eyes[EmmaX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Emma_blowjob/Emma_blowjob_eyes_squint.png"
    0.05
    "images/Emma_blowjob/Emma_blowjob_eyes_closed.png"
    0.15
    "images/Emma_blowjob/Emma_blowjob_eyes_squint.png"
    0.05
    repeat
