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

layeredimage Laura_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

    if LauraX.grool > 1 and not LauraX.pussy_covered:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

    if LauraX.grool > 1 and not LauraX.pussy_covered:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

    if LauraX.grool > 1 and not LauraX.pussy_covered:
        "grool_dripping_animation" pos (0.078, 0.58) zoom 0.2

layeredimage Laura_grool_animations:
    if not LauraX.grool:
        Null()
    elif LauraX.outfit["bottom"] == "_pants" and LauraX.bottom_pulled_down:
        AlphaMask("Laura_grool_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_pants.png")
    elif LauraX.outfit["underwear"] and LauraX.underwear_pulled_down:
        AlphaMask("Laura_grool_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_underwear.png")
    elif not LauraX.pussy_covered:
        AlphaMask("Laura_grool_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask.png")

layeredimage Laura_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

    if not LauraX.pussy_covered:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

    if not LauraX.pussy_covered:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

    if not LauraX.pussy_covered:
        "spunk_dripping_animation" pos (0.078, 0.58) zoom 0.3

layeredimage Laura_spunk_animations:
    if not LauraX.spunk["pussy"] and not LauraX.spunk["anus"]:
        Null()
    elif LauraX.outfit["bottom"] == "_pants" and LauraX.bottom_pulled_down:
        AlphaMask("Laura_spunk_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_pants.png")
    elif LauraX.outfit["underwear"] and LauraX.underwear_pulled_down:
        AlphaMask("Laura_spunk_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask_underwear.png")
    elif not LauraX.pussy_covered:
        AlphaMask("Laura_spunk_dripping_animation", "images/Laura_standing/Laura_standing_grool_mask.png")

# layeredimage Laura_standing_fondling_animations:
#     if Player.primary_action == "lesbian" or not LauraX.secondary_action or focused_Girl != LauraX:
#             Null()
#     elif Player.primary_action != "sex" and LauraX.secondary_action in "finger_pussy" and LauraX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif LauraX.secondary_action == "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif LauraX.secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif LauraX.secondary_action == "fondle_breasts":
#         "girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == LauraX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and LauraX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action in "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if not Player.primary_action or focused_Girl != LauraX:
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
#     if not Player.secondary_action or focused_Girl != LauraX:
#         Null()
#     elif Player.secondary_action == "fondle_thighs":
#         "Zero_fondle_thigh_animation" pos (0.11, 0.68)
#     elif Player.primary_action == "fondle_breasts" and not LauraX.secondary_action and not second_girl_main_action and not second_girl_secondary_action:
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
#     if not second_girl_main_action or focused_Girl != LauraX:
#         Null()
#     elif second_girl_main_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_main_action == "fondle_breasts":
#         "girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif second_girl_main_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif second_girl_main_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif second_girl_main_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and LauraX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and LauraX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not LauraX.secondary_action or focused_Girl == LauraX:
#         Null()
#     elif LauraX.secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif LauraX.secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif LauraX.secondary_action == "fondle_breasts":
#         "girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif LauraX.secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif LauraX.secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif LauraX.secondary_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif LauraX.secondary_action == "fondle_pussy" and Player.primary_action != "sex" and LauraX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif LauraX.secondary_action == "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif LauraX.secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)

image Laura_handjob_under_hand_animation0:
    "Laura_handjob_under"

image Laura_handjob_under_hand_animation1:
    animation
    "Laura_handjob_under"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 1
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Laura_handjob_under_hand_animation2:
    animation
    "Laura_handjob_under"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 0
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

image Laura_handjob_over_hand_animation0:
    "Laura_handjob_over"

image Laura_handjob_over_hand_animation1:
    animation
    "Laura_handjob_over"

    subpixel True
    rotate -5
    block:
        ease 0.75 yoffset 40 rotate 1
        pause 0.25
        ease 1.0 yoffset -10 rotate -5
        pause 0.1
        repeat

image Laura_handjob_over_hand_animation2:
    animation
    "Laura_handjob_over"

    subpixel True
    rotate -3
    block:
        ease 0.4 yoffset 30 rotate 0
        pause 0.1
        ease 0.4 yoffset -10 rotate -3
        pause 0.1
        repeat

layeredimage Laura_sprite handjob:
    always:
        "Laura_sprite standing"

    always:
        "Laura_handjob_under_hand_animation[action_speed]" pos (0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Laura"

    always:
        "Laura_handjob_over_hand_animation[action_speed]" pos (0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5

image Laura_titjob_back_hair_animation0:
    animation
    "Laura_back_hair"

    subpixel True
    rotate 0
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_back_hair_animation1:
    animation
    "Laura_back_hair"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_back_hair_animation2:
    animation
    "Laura_back_hair"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Laura_titjob_body_animation0:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Laura_titjob_body_animation1:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_body_animation2:
    animation
    "Laura_titjob_body"

    subpixel True
    block:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat

image Laura_titjob_right_arm_back_animation0:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 2 yoffset -5
        pause 0.1
        ease 2 yoffset -15
        pause 0.1
        repeat

image Laura_titjob_right_arm_back_animation1:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_right_arm_back_animation2:
    animation
    "Laura_titjob_right_arm_back"

    subpixel True
    block:
        ease 1 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_right_breast_animation0:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset -5
        pause 0.1
        ease 2 yoffset -15
        repeat

image Laura_titjob_right_breast_animation1:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Laura_titjob_right_breast_animation2:
    animation
    "Laura_titjob_right_breast"

    subpixel True
    block:
        ease 0.3 yoffset 50
        ease 0.7 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_right_arm_animation0:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 2 yoffset 10
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Laura_titjob_right_arm_animation1:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_right_arm_animation2:
    animation
    "Laura_titjob_right_arm"

    subpixel True
    block:
        ease 1 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_head_animation0:
    animation
    "Laura_head"

    subpixel True
    rotate 0
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_head_animation1:
    animation
    "Laura_head"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_head_animation2:
    animation
    "Laura_head"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

image Laura_titjob_left_breast_animation0:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    block:
        pause 0.1
        ease 2 yoffset -40
        pause 0.1
        ease 2 yoffset 0
        repeat

image Laura_titjob_left_breast_animation1:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Laura_titjob_left_breast_animation2:
    animation
    "Laura_titjob_left_breast"

    subpixel True
    block:
        ease 0.3 yoffset 50
        ease 0.7 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_left_arm_animation0:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    block:
        ease 2 yoffset -40
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Laura_titjob_left_arm_animation1:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        pause 0.5
        repeat

image Laura_titjob_left_arm_animation2:
    animation
    "Laura_titjob_left_arm"

    subpixel True
    block:
        ease 1 yoffset 0
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Laura_titjob_mid_hair_animation0:
    animation
    "Laura_titjob_mid_hair"

    subpixel True
    rotate 0
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_mid_hair_animation1:
    animation
    "Laura_titjob_mid_hair"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset -20
        pause 0.4
        ease 1.8 yoffset 160
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_mid_hair_animation2:
    animation
    "Laura_titjob_mid_hair"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -40
        pause 0.2
        ease 0.4 yoffset 90
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.2
        ease 0.4 rotate -5
        repeat

image Laura_titjob_hair_animation0:
    animation
    "Laura_titjob_hair"

    subpixel True
    rotate 0
    parallel:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat
    parallel:
        pause 0.1
        ease 2 rotate -5
        pause 0.1
        ease 2 rotate 0
        repeat

image Laura_titjob_hair_animation1:
    animation
    "Laura_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat
    parallel:
        ease 2 rotate 0
        pause 0.2
        ease 2 rotate -5
        pause 0.5
        repeat

image Laura_titjob_hair_animation2:
    animation
    "Laura_titjob_hair"

    subpixel True
    rotate -5
    parallel:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat
    parallel:
        ease 1 rotate 0
        pause 0.1
        ease 0.5 rotate -5
        repeat

layeredimage Laura_sprite titjob:
    always:
        "Laura_titjob_back_hair_animation[action_speed]" pos (-0.035, -0.26) zoom 1.1

    always:
        "Laura_titjob_body_animation[action_speed]"

    always:
        "Laura_titjob_right_arm_back_animation[action_speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_right_breast_animation[action_speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_right_arm_animation[action_speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_head_animation[action_speed]" pos (-0.035, -0.26) zoom 1.1

    always:
        "Zero_cock_Laura"

    always:
        "Laura_titjob_left_breast_animation[action_speed]"

    always:
        "Laura_titjob_left_arm_animation[action_speed]" pos (0.0, 0.01)

    always:
        "Laura_titjob_mid_hair_animation[action_speed]" pos (-0.035, -0.26) zoom 1.1

    always:
        "Laura_titjob_hair_animation[action_speed]" pos (-0.035, -0.26) zoom 1.1

    anchor (0.5, 0.0) offset (400, 850) zoom 1.05
