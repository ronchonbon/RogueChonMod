image Jean_blinking:
    "images/Jean_standing/Jean_standing_eyes[JeanX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jean_standing/Jean_standing_eyes_sexy.png"
    0.05
    "images/Jean_standing/Jean_standing_eyes_closed.png"
    0.15
    "images/Jean_standing/Jean_standing_eyes_sexy.png"
    0.05
    repeat

# layeredimage Jean_standing_fondling_animations:
#     if Player.primary_action == "lesbian" or not JeanX.secondary_action or focused_Girl != JeanX:
#             Null()
#     elif Player.primary_action != "sex" and JeanX.secondary_action in "finger_pussy" and JeanX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif JeanX.secondary_action == "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif JeanX.secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif JeanX.secondary_action == "fondle_breasts":
#         "girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == JeanX:
#         Null()
#     elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and JeanX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_secondary_action in "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif second_girl_secondary_action == "fondle_breasts":
#         "girl_fondle_breast_right_animation" pos (0.083, 0.352)
#
#     if not Player.primary_action or focused_Girl != JeanX:
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
#     if not Player.secondary_action or focused_Girl != JeanX:
#         Null()
#     elif Player.secondary_action == "fondle_thighs":
#         "Zero_fondle_thigh_animation" pos (0.11, 0.68)
#     elif Player.primary_action == "fondle_breasts" and not JeanX.secondary_action and not second_girl_main_action and not second_girl_secondary_action:
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
#     if not second_girl_main_action or focused_Girl != JeanX:
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
#     elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and JeanX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and JeanX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif second_girl_main_action == "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif second_girl_main_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)
#
#     if Player.primary_action != "lesbian" or not JeanX.secondary_action or focused_Girl == JeanX:
#         Null()
#     elif JeanX.secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif JeanX.secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "girl_fondle_breast_left_animation" pos (0.156, 0.37)
#     elif JeanX.secondary_action == "fondle_breasts":
#         "girl_fondle_breast_right_animation" pos (0.083, 0.352)
#     elif JeanX.secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif JeanX.secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
#         "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
#     elif JeanX.secondary_action == "suck_breasts":
#         "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
#     elif JeanX.secondary_action == "fondle_pussy" and Player.primary_action != "sex" and JeanX.lust >= 70:
#         "girl_finger_pussy_animation" pos (0.122, 0.583)
#     elif JeanX.secondary_action == "fondle_pussy":
#         "girl_fondle_pussy_animation" pos (0.122, 0.569)
#     elif JeanX.secondary_action == "eat_pussy":
#         "Zero_eat_pussy_animation" pos (0.13, 0.62)

image Jean_handjob_under_hand_animation0:
    "Jean_handjob_under"

image Jean_handjob_under_hand_animation1:
    animation
    "Jean_handjob_under"

    subpixel True
    rotate 10
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset 0 rotate 10
        pause 0.1
        repeat

image Jean_handjob_under_hand_animation2:
    animation
    "Jean_handjob_under"

    subpixel True
    rotate 8
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset 0 rotate 8
        pause 0.1
        repeat

image Jean_handjob_over_hand_animation0:
    "Jean_handjob_over"

image Jean_handjob_over_hand_animation1:
    animation
    "Jean_handjob_over"

    subpixel True
    rotate 10
    block:
        ease 0.75 yoffset 40 rotate 5
        pause 0.25
        ease 1.0 yoffset 0 rotate 10
        pause 0.1
        repeat

image Jean_handjob_over_hand_animation2:
    animation
    "Jean_handjob_over"

    subpixel True
    rotate 8
    block:
        ease 0.4 yoffset 30 rotate 3
        pause 0.1
        ease 0.4 yoffset 0 rotate 8
        pause 0.1
        repeat

layeredimage Jean_sprite handjob:
    always:
        "Jean_sprite standing"

    always:
        "Jean_handjob_under_hand_animation[action_speed]" pos (0.035, 0.455) zoom 0.28

    always:
        "Zero_cock_Jean"

    always:
        "Jean_handjob_over_hand_animation[action_speed]" pos (0.035, 0.455) zoom 0.28

    anchor (0.5, 0.0) offset (240, -220) zoom 2.5

image Jean_titjob_bra_back_animation0:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_bra_back_animation1:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        pause 0.1
        ease 1.9 ypos -20
        pause 0.4
        ease 1.8 ypos 150
        ease 0.5 ypos 140
        repeat

image Jean_titjob_bra_back_animation2:
    animation
    "Jean_titjob_bra_back"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jean_titjob_back_hair_animation0:
    animation
    "Jean_blowjob_back_hair"

    subpixel True
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

image Jean_titjob_back_hair_animation1:
    animation
    "Jean_blowjob_back_hair"

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

image Jean_titjob_back_hair_animation2:
    animation
    "Jean_blowjob_back_hair"

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

image Jean_titjob_body_animation0:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_body_animation1:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 2 yoffset 0
        pause 0.2
        ease 2 yoffset 150
        pause 0.5
        repeat

image Jean_titjob_body_animation2:
    animation
    "Jean_titjob_body"

    subpixel True
    block:
        ease 1 yoffset -20
        pause 0.1
        ease 0.5 yoffset 80
        repeat

image Jean_titjob_head_animation0:
    animation
    "Jean_blowjob_head"

    subpixel True
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

image Jean_titjob_head_animation1:
    animation
    "Jean_blowjob_head"

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

image Jean_titjob_head_animation2:
    animation
    "Jean_blowjob_head"

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

image Jean_titjob_right_breast_animation0:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_right_breast_animation1:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Jean_titjob_right_breast_animation2:
    animation
    "Jean_titjob_right_breast"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jean_titjob_bra_stretch_animation0:
    "Jean_titjob_bra_stretch"

    yzoom 0.75

image Jean_titjob_bra_stretch_animation1:
    animation
    "Jean_titjob_bra_stretch"

    subpixel True
    parallel:
        pause 0.1
        ease 1.9 ypos -70
        pause 0.4
        ease 2.3 ypos 145
        repeat
    parallel:
        pause 0.1
        ease 1.9 yzoom 0.5
        pause 0.4
        ease 1.8 yzoom 1
        pause 0.5
        repeat

image Jean_titjob_bra_stretch_animation2:
    animation
    "Jean_titjob_bra_stretch"

    subpixel True
    yzoom 0.75
    block:
        pause 0.2
        ease 0.8 yoffset 0
        pause 0.3
        ease 0.3 yoffset 50
        repeat

image Jean_titjob_breasts_animation0:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        ease 2 yoffset -20
        pause 0.1
        ease 2 yoffset 0
        pause 0.1
        repeat

image Jean_titjob_breasts_animation1:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        pause 0.1
        ease 1.9 yoffset -20
        pause 0.4
        ease 1.8 yoffset 150
        ease 0.5 yoffset 140
        repeat

image Jean_titjob_breasts_animation2:
    animation
    "Jean_titjob_breasts"

    subpixel True
    block:
        ease 0.3 yoffset 40
        ease 0.7 yoffset -40
        pause 0.2
        ease 0.4 yoffset 80
        repeat

image Jean_titjob_hair_animation0:
    animation
    "Jean_titjob_hair"

    subpixel True
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

image Jean_titjob_hair_animation1:
    animation
    "Jean_titjob_hair"

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

image Jean_titjob_hair_animation2:
    animation
    "Jean_titjob_hair"

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

layeredimage Jean_sprite titjob:
    if JeanX.outfit["bra"] in ["_green_bra", "_lace_bra"]:
        "Jean_titjob_bra_back_animation[action_speed]"

    always:
        "Jean_titjob_back_hair_animation[action_speed]" pos (0.0, -0.15) zoom 0.9

    always:
        "Jean_titjob_body_animation[action_speed]"

    always:
        "Jean_titjob_head_animation[action_speed]" pos (0.0, -0.15) zoom 0.9

    always:
        "Jean_titjob_right_breast_animation[action_speed]"

    always:
        "Zero_cock_Jean"

    if JeanX.outfit["bra"] in ["_sports_bra", "_bikini_top"]:
        "Jean_titjob_bra_stretch_animation[action_speed]"

    always:
        "Jean_titjob_breasts_animation[action_speed]"

    always:
        "Jean_titjob_hair_animation[action_speed]" pos (0.0, -0.15) zoom 0.9

    anchor (0.5, 0.0) offset (300, 750)

image Jean_blowjob_blinking:
    "images/Jean_blowjob/Jean_blowjob_eyes[JeanX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jean_blowjob/Jean_blowjob_eyes_sexy.png"
    0.05
    "images/Jean_blowjob/Jean_blowjob_eyes_closed.png"
    0.15
    "images/Jean_blowjob/Jean_blowjob_eyes_sexy.png"
    0.05
    repeat
