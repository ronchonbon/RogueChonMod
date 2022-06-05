image Kitty_blinking:
    "images/Kitty_standing/Kitty_standing_eyes[KittyX.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_standing/Kitty_standing_eyes_squint.png"
    0.05
    "images/Kitty_standing/Kitty_standing_eyes_closed.png"
    0.15
    "images/Kitty_standing/Kitty_standing_eyes_squint.png"
    0.05
    repeat

layeredimage Kitty_grool_dripping_animations:
    always:
        "grool_dripping_animation" pos (0.122, 0.6) zoom 0.2

    if KittyX.grool > 1 and not KittyX.pussy_covered:
        "grool_dripping_animation" pos (0.122, 0.6) zoom 0.2

    if KittyX.grool > 1 and not KittyX.pussy_covered:
        "grool_dripping_animation" pos (0.122, 0.6) zoom 0.2

    if KittyX.grool > 1 and not KittyX.pussy_covered:
        "grool_dripping_animation" pos (0.122, 0.6) zoom 0.2

layeredimage Kitty_grool_animations:
    if KittyX.grool and KittyX.outfit["bottom"] == "_pants" and KittyX.bottom_pulled_down:
        AlphaMask("Kitty_grool_dripping_animations", "images/Kitty_standing/Kitty_standing_grool_mask_pants.png")
    elif KittyX.grool and KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        AlphaMask("Kitty_grool_dripping_animations", "images/Kitty_standing/Kitty_standing_grool_mask_underwear.png")
    elif KittyX.grool and not KittyX.pussy_covered:
        AlphaMask("Kitty_grool_dripping_animations", "images/Kitty_standing/Kitty_standing_grool_mask.png")

layeredimage Kitty_spunk_dripping_animations:
    always:
        "spunk_dripping_animation" pos (0.122, 0.6) zoom 0.3

    if not KittyX.pussy_covered:
        "spunk_dripping_animation" pos (0.122, 0.6) zoom 0.3

    if not KittyX.pussy_covered:
        "spunk_dripping_animation" pos (0.122, 0.6) zoom 0.3

    if not KittyX.pussy_covered:
        "spunk_dripping_animation" pos (0.122, 0.6) zoom 0.3

layeredimage Kitty_spunk_animations:
    if (KittyX.spunk["pussy"] or KittyX.spunk["anus"]) and KittyX.outfit["bottom"] == "_pants" and KittyX.bottom_pulled_down:
        AlphaMask("Kitty_spunk_dripping_animations", "images/Kitty_standing/Kitty_standing_grool_mask_pants.png")
    elif (KittyX.spunk["pussy"] or KittyX.spunk["anus"]) and KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        AlphaMask("Kitty_spunk_dripping_animations", "images/Kitty_standing/Kitty_standing_grool_mask_underwear.png")
    elif (KittyX.spunk["pussy"] or KittyX.spunk["anus"]) and not KittyX.pussy_covered:
        AlphaMask("Kitty_spunk_dripping_animations", "images/Kitty_standing/Kitty_standing_grool_mask.png")

layeredimage Kitty_standing_fondling_animations:
    if Player.primary_action == "lesbian" or not KittyX.secondary_action or focused_Girl != KittyX:
            Null()
    elif Player.primary_action != "sex" and KittyX.secondary_action in "finger_pussy" and KittyX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif KittyX.secondary_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif KittyX.secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif KittyX.secondary_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if second_girl_main_action != "masturbation" or not second_girl_secondary_action or focused_Girl == KittyX:
        Null()
    elif Player.primary_action != "sex" and second_girl_secondary_action == "finger_pussy" and KittyX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_secondary_action in "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_secondary_action == "fondle_breasts" and (Player.secondary_action in ["fondle_breasts", "suck breasts"]):
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_secondary_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if not Player.primary_action or focused_Girl != KittyX:
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

    if not Player.secondary_action or focused_Girl != KittyX:
        Null()
    elif Player.secondary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif Player.primary_action == "fondle_breasts" and not KittyX.secondary_action and not second_girl_main_action and not second_girl_secondary_action:
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

    if not second_girl_main_action or focused_Girl != KittyX:
        Null()
    elif second_girl_main_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_main_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif second_girl_main_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_main_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif second_girl_main_action == "fondle_pussy" and Player.primary_action != "sex" and KittyX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy" and Player.secondary_action != "sex" and KittyX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_main_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_main_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if Player.primary_action != "lesbian" or not KittyX.secondary_action or focused_Girl == KittyX:
        Null()
    elif KittyX.secondary_action == "fondle_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif KittyX.secondary_action == "fondle_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif KittyX.secondary_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif KittyX.secondary_action == "suck_breasts" and Player.primary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif KittyX.secondary_action == "suck_breasts" and Player.secondary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif KittyX.secondary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif KittyX.secondary_action == "fondle_pussy" and Player.primary_action != "sex" and KittyX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif KittyX.secondary_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif KittyX.secondary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

# image Kitty_handjob_under_hand_animation0:
#     "Kitty_handjob_under"
#
# image Kitty_handjob_under_hand_animation1:
#     subpixel True
#     "Kitty_handjob_under"
#     block:
#         ease 0.5 yoffset -40 rotate 5
#         pause 0.25
#         ease 1.0 yoffset 10 rotate -5
#         pause 0.1
#         repeat
#
# image Kitty_handjob_under_hand_animation2:
#     subpixel True
#     "Kitty_handjob_under"
#     block:
#         ease 0.2 yoffset -30 rotate 3
#         pause 0.1
#         ease 0.4 yoffset 10 rotate -3
#         pause 0.1
#         repeat
#
# layeredimage Kitty_handjob_under_hand_animations:
#     always:
#         "Kitty_handjob_under_hand_animation[action_speed]" pos (-0.04, 0.455) zoom 0.28
#
# image Kitty_handjob_over_hand_animation0:
#     "Kitty_handjob_over"
#
# image Kitty_handjob_over_hand_animation1:
#     subpixel True
#     "Kitty_handjob_over"
#     block:
#         ease 0.5 yoffset -40 rotate 5
#         pause 0.25
#         ease 1.0 yoffset 10 rotate -5
#         pause 0.1
#         repeat
#
# image Kitty_handjob_over_hand_animation2:
#     subpixel True
#     "Kitty_handjob_over"
#     block:
#         ease 0.2 yoffset -30 rotate 3
#         pause 0.1
#         ease 0.4 yoffset 10 rotate -3
#         pause 0.1
#         repeat
#
# layeredimage Kitty_handjob_over_hand_animations:
#     always:
#         "Kitty_handjob_over_hand_animation[action_speed]" pos (-0.04, 0.455) zoom 0.28
#
# layeredimage Kitty_sprite handjob:
#     always:
#         "Kitty_sprite standing" pos (0.04, 0.0)
#
#     always:
#         "Kitty_handjob_under_hand_animations"
#
#     always:
#         "Kitty_handjob_cock_animations"
#
#     always:
#         "Kitty_handjob_over_hand_animations"
#
#     anchor (0.5, 0.0) offset (280, -300) zoom 2.5
#
# image Kitty_titjob_back_hair_animation0:
#     "Kitty_back_hair"
#     subpixel True
#     block:
#         ease 2.4 yoffset -10
#         ease 1.6 yoffset 0
#         repeat
#
# image Kitty_titjob_back_hair_animation1:
#     "Kitty_back_hair"
#     subpixel True
#     block:
#         ease 3.0 yoffset -50
#         ease 1.0 yoffset 0
#         repeat
#
# image Kitty_titjob_back_hair_animation2:
#     "Kitty_back_hair"
#     subpixel True
#     block:
#         ease 0.7 yoffset -45
#         ease 0.25 yoffset 0
#         pause 0.05
#         repeat
#
# image Kitty_titjob_back_hair_animation3:
#     "Kitty_back_hair"
#     subpixel True
#     parallel:
#         block:
#             ease 2 offset (0, 30)
#             ease 0.6 offset (0, 55)
#             pause 0.4
#             repeat 2
#         block:
#             ease 2.2 offset (0, 30)
#             ease 0.8 offset (20, 60)
#             ease 2.2 offset (10, 30)
#             ease 0.8 offset (20, 60)
#         block:
#             ease 2 offset (0, 30)
#             ease 0.6 offset (0, 55)
#             pause 0.4
#             repeat 2
#         block:
#             ease 2.2 offset (0, 30)
#             ease 0.8 offset (-25, 60)
#             ease 2.2 offset (-10, 30)
#             ease 0.8 offset (-25, 60)
#         repeat
#
# image Kitty_titjob_back_hair_animation4:
#     "Kitty_back_hair"
#     subpixel True
#     block:
#         ease 2 pos (0, 44)
#         ease 1.6 pos (0, 47)
#         pause 0.4
#         repeat
#
# layeredimage Kitty_titjob_back_hair_animations:
#     always:
#         "Kitty_titjob_back_hair_animation[action_speed]" zoom 0.574
#
# image Kitty_titjob_torso_animation0:
#     "Kitty_titjob_torso"
#     subpixel True
#     block:
#         ease 2.4 yoffset -5
#         ease 1.6 yoffset 0
#         repeat
#
# image Kitty_titjob_torso_animation1:
#     "Kitty_titjob_torso"
#     subpixel True
#     block:
#         ease 2.8 yoffset -50
#         ease 1.0 yoffset 0
#         pause 0.2
#         repeat
#
# image Kitty_titjob_torso_animation2:
#     "Kitty_titjob_torso"
#     subpixel True
#     block:
#         ease 0.65 yoffset -45
#         ease 0.25 yoffset 0
#         pause 0.1
#         repeat
#
# image Kitty_titjob_torso_animation3:
#     "Kitty_titjob_torso"
#     subpixel True
#     block:
#         ease 2.2 yoffset -20
#         ease 0.6 yoffset  0
#         pause 0.2
#         repeat
#
# image Kitty_titjob_torso_animation4:
#     "Kitty_titjob_torso"
#     subpixel True
#     block:
#         ease 2.2 pos (0, -10)
#         ease 1.6 pos (0, 0)
#         pause 0.2
#         repeat
#
# layeredimage Kitty_titjob_torso_animations:
#     always:
#         "Kitty_titjob_torso_animation[action_speed]" zoom 0.55
#
# image Kitty_titjob_arms_animation0:
#     "Kitty_titjob_arms"
#
# image Kitty_titjob_arms_animation1:
#     "Kitty_titjob_arms"
#
# image Kitty_titjob_arms_animation2:
#     "Kitty_titjob_arms"
#
# image Kitty_titjob_arms_animation3:
#     "Kitty_titjob_arms"
#
# image Kitty_titjob_arms_animation4:
#     "Kitty_titjob_arms"
#
# layeredimage Kitty_titjob_arms_animations:
#     always:
#         "Kitty_titjob_arms_animation[action_speed]" zoom 0.55
#
# image Kitty_titjob_breasts_animation0:
#     "Kitty_titjob_breasts"
#
# image Kitty_titjob_breasts_animation1:
#     "Kitty_titjob_breasts"
#
# image Kitty_titjob_breasts_animation2:
#     "Kitty_titjob_breasts"
#
# image Kitty_titjob_breasts_animation3:
#     "Kitty_titjob_breasts"
#
# image Kitty_titjob_breasts_animation4:
#     "Kitty_titjob_breasts"
#
# layeredimage Kitty_titjob_breasts_animations:
#     always:
#         "Kitty_titjob_breasts_animation[action_speed]" zoom 0.55
#
# image Kitty_titjob_head_animation0:
#     "Kitty_blowjob_head"
#
# image Kitty_titjob_head_animation1:
#     "Kitty_blowjob_head"
#
# image Kitty_titjob_head_animation2:
#     "Kitty_blowjob_head"
#
# image Kitty_titjob_head_animation3:
#     "Kitty_blowjob_head"
#
# image Kitty_titjob_head_animation4:
#     "Kitty_blowjob_head"
#
# layeredimage Kitty_titjob_head_animations:
#     always:
#         "Kitty_titjob_head_animation[action_speed]" zoom 0.41*1.4
#
# image Kitty_titjob_mask_animation0:
#     "Kitty_titjob_mask"
#
# image Kitty_titjob_mask_animation1:
#     "Kitty_titjob_mask"
#
# image Kitty_titjob_mask_animation2:
#     "Kitty_titjob_mask"
#
# image Kitty_titjob_mask_animation3:
#     "Kitty_titjob_mask"
#
# image Kitty_titjob_mask_animation4:
#     "Kitty_titjob_mask"
#
# layeredimage Kitty_titjob_mask_animations:
#     always:
#         "Kitty_titjob_mask_animation[action_speed]" zoom 0.4*1.4
#
# layeredimage Kitty_sprite titjob:
#     always:
#         "Kitty_titjob_back_hair_animations"
#
#     always:
#         "Kitty_titjob_torso_animations"
#
#     always:
#         "Kitty_titjob_arms_animations"
#
#     always:
#         "Kitty_titjob_breasts_animations"
#
#     always:
#         "Kitty_titjob_head_animations"
#
#     always:
#         "Kitty_titjob_mask_animations"
#
#     always:
#         "Kitty_blowjob_cock" zoom 0.4
#
#     # always:
#     #     AlphaMask("Kitty_blowjob_cock", "Kitty_titjob_mask_animations")
#
#     anchor (0.5, 0.0) offset (0, 200) zoom 1.35
#
# image Kitty_blowjob_blinking:
#     "images/Kitty_blowjob/Kitty_blowjob_eyes[KittyX.eyes].png"
#     choice:
#         3.5
#     choice:
#         3.25
#     choice:
#         3
#     "images/Kitty_blowjob/Kitty_blowjob_eyes_squint.png"
#     0.05
#     "images/Kitty_blowjob/Kitty_blowjob_eyes_closed.png"
#     0.15
#     "images/Kitty_blowjob/Kitty_blowjob_eyes_squint.png"
#     0.05
#     repeat
#
# image Kitty_squinting:
#     "images/Kitty_blowjob/Kitty_blowjob_eyes_sexy.png"
#     choice:
#         3.5
#     choice:
#         3.25
#     choice:
#         3
#     "images/Kitty_blowjob/Kitty_blowjob_eyes_squint.png"
#     0.25
#     repeat
#
#
#
#
#
#
#
#
#
#
#
#
#
# image Kitty_sex_body_animation0:
#     "Kitty_sex_body"
#
# layeredimage Kitty_sex_body_animations:
#     if not action_speed or Player.cock_position in ["in", "anal"]:
#         "Kitty_sex_body_animation[action_speed]"
#     elif Player.cock_position == "footjob":
#         "Kitty_sex_body_footjob_animation[action_speed]"
#     elif Player.cock_position == "out":
#         "Kitty_sex_body_hotdog_animation[action_speed]"
#
# image Kitty_sex_legs_animation0:
#     "Kitty_sex_legs"
#
# layeredimage Kitty_sex_legs_animations:
#     if not action_speed or Player.cock_position in ["in", "anal"]:
#         "Kitty_sex_legs_animation[action_speed]"
#     elif Player.cock_position == "footjob":
#         "Kitty_sex_legs_footjob_animation[action_speed]"
#     elif Player.cock_position == "out":
#         "Kitty_sex_legs_hotdog_animation[action_speed]"
#
# layeredimage Kitty_sprite sex:
#     always:
#         "Kitty_sex_body_animations"
#
#     always:
#         "Kitty_sex_legs_animations"
#
#     anchor (0.5, 0.0) offset (0, 0) zoom 0.7
