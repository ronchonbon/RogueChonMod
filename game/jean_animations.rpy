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

    anchor (0.5, 0.0) offset (220, -220) zoom 2.5
