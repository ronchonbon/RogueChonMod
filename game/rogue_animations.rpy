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
    
layeredimage Rogue_grool_dripping_animations:
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
        AlphaMask("Rogue_grool_dripping_animations", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif RogueX.grool and RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        AlphaMask("Rogue_grool_dripping_animations", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif RogueX.grool and not RogueX.pussy_covered:
        AlphaMask("Rogue_grool_dripping_animations", "images/Rogue_standing/Rogue_standing_grool_mask.png")

layeredimage Rogue_spunk_dripping_animations:
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
        AlphaMask("Rogue_spunk_dripping_animations", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif (RogueX.spunk["pussy"] or RogueX.spunk["anus"]) and RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        AlphaMask("Rogue_spunk_dripping_animations", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif (RogueX.spunk["pussy"] or RogueX.spunk["anus"]) and not RogueX.pussy_covered:
        AlphaMask("Rogue_spunk_dripping_animations", "images/Rogue_standing/Rogue_standing_grool_mask.png")

layeredimage Rogue_standing_fondling_animations:
    if primary_action == "lesbian" or not girl_offhand_action or focused_Girl != RogueX:
            Null()
    elif primary_action != "sex" and girl_offhand_action in "finger_pussy" and RogueX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif girl_offhand_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif girl_offhand_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if second_girl_primary_action != "masturbation" or not second_girl_offhand_action or focused_Girl == RogueX:
        Null()
    elif primary_action != "sex" and second_girl_offhand_action == "finger_pussy" and RogueX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_offhand_action in "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_offhand_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)

    if not primary_action or focused_Girl != RogueX:
        Null()
    elif primary_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif primary_action == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
    elif primary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif primary_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.115, 0.59)
    elif primary_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.12, 0.66)
    elif primary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if not offhand_action or focused_Girl != RogueX:
        Null()
    elif offhand_action == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.11, 0.68)
    elif primary_action == "fondle_breasts" and not girl_offhand_action and not second_girl_primary_action and not second_girl_offhand_action:
        "Zero_fondle_breasts_right_animation" pos (0.094, 0.38)
    elif offhand_action == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.156, 0.39)
    elif offhand_action == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif offhand_action == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.115, 0.59)
    elif offhand_action == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.12, 0.66)
    elif offhand_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if not second_girl_primary_action or focused_Girl != RogueX:
        Null()
    elif second_girl_primary_action == "fondle_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif second_girl_primary_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif second_girl_primary_action == "suck_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_primary_action == "suck_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif second_girl_primary_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif second_girl_primary_action == "fondle_pussy" and primary_action != "sex" and RogueX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_primary_action == "fondle_pussy" and offhand_action != "sex" and RogueX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif second_girl_primary_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif second_girl_primary_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

    if primary_action != "lesbian" or not girl_offhand_action or focused_Girl == RogueX:
        Null()
    elif girl_offhand_action == "fondle_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif girl_offhand_action == "fondle_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Girl_fondle_breast_left_animation" pos (0.156, 0.37)
    elif girl_offhand_action == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.083, 0.352)
    elif girl_offhand_action == "suck_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif girl_offhand_action == "suck_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "Zero_suck_breasts_left_animation" pos (0.146, 0.38)
    elif girl_offhand_action == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.083, 0.37)
    elif girl_offhand_action == "fondle_pussy" and primary_action != "sex" and RogueX.lust >= 70:
        "Girl_finger_pussy_animation" pos (0.122, 0.583)
    elif girl_offhand_action == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.122, 0.569)
    elif girl_offhand_action == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.13, 0.62)

image Rogue_handjob_under_hand_animation0:
    "Rogue_handjob_under"

image Rogue_handjob_under_hand_animation1:
    "Rogue_handjob_under"
    block:
        ease 0.5 yoffset -40 rotate 5
        pause 0.25
        ease 1.0 yoffset 10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_under_hand_animation2:
    "Rogue_handjob_under"
    block:
        ease 0.2 yoffset -30 rotate 3
        pause 0.1
        ease 0.4 yoffset 10 rotate -3
        pause 0.1
        repeat

layeredimage Rogue_handjob_under_hand_animations:
    always:
        "Rogue_handjob_under_hand_animation[action_speed]" pos (-0.04, 0.455) zoom 0.28

image Rogue_handjob_over_hand_animation0:
    "Rogue_handjob_over"

image Rogue_handjob_over_hand_animation1:
    "Rogue_handjob_over"
    block:
        ease 0.5 yoffset -40 rotate 5
        pause 0.25
        ease 1.0 yoffset 10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_over_hand_animation2:
    "Rogue_handjob_over"
    block:
        ease 0.2 yoffset -30 rotate 3
        pause 0.1
        ease 0.4 yoffset 10 rotate -3
        pause 0.1
        repeat

layeredimage Rogue_handjob_over_hand_animations:
    always:
        "Rogue_handjob_over_hand_animation[action_speed]" pos (-0.04, 0.455) zoom 0.28

layeredimage Rogue_sprite handjob:
    always:
        "Rogue_sprite standing" pos (0.05, 0.0)

    always:
        "Rogue_handjob_under_hand_animations"

    always:
        "Rogue_handjob_cock_animations"

    always:
        "Rogue_handjob_over_hand_animations"

    anchor (0.5, 0.0) offset (220, -200) zoom 2.5

image Rogue_titjob_under_tits_animation0:
    "Rogue_titjob_under"

image Rogue_titjob_under_tits_animation1:
    "Rogue_titjob_under"
    block:
        ease 1 yoffset 0
        easeout 0.2 yoffset 0
        easein 1.3 yoffset -50
        repeat

image Rogue_titjob_under_tits_animation2:
    "Rogue_titjob_under"
    block:
        ease 0.25 yoffset 0
        ease 0.4 yoffset -50
        ease 0.1 yoffset -55
        repeat

layeredimage Rogue_titjob_under_tits_animations:
    always:
        "Rogue_titjob_under_tits_animation[action_speed]" pos (-0.043, 0.8)

image Rogue_titjob_over_tits_animation0:
    "Rogue_titjob_over"

image Rogue_titjob_over_tits_animation1:
    "Rogue_titjob_over"
    block:
        ease 1.20 yoffset 0
        easeout 0.1 yoffset 0
        easein 1.2 yoffset -50
        repeat

image Rogue_titjob_over_tits_animation2:
    "Rogue_titjob_over"
    block:
        ease 0.3 yoffset 0
        ease 0.35 yoffset -50
        ease 0.1 yoffset -55
        repeat

layeredimage Rogue_titjob_over_tits_animations:
    always:
        "Rogue_titjob_over_tits_animation[action_speed]" pos (-0.043, 0.8)

layeredimage Rogue_sprite titjob:
    always:
        "Rogue_titjob_under_tits_animations"

    always:
        "Rogue_titjob_cock_animations"

    always:
        "Rogue_titjob_over_tits_animations"

    anchor (0.5, 0.0) offset (200, 200) zoom 0.72

image Rogue_blowjob_back_hair_animation0:
    "Rogue_back_hair"
    blowjob_starting

image Rogue_blowjob_back_hair_animation1:
    "Rogue_back_hair"
    blowjob_licking

image Rogue_blowjob_back_hair_animation2:
    "Rogue_back_hair"
    blowjob_heading

image Rogue_blowjob_back_hair_animation3:
    "Rogue_back_hair"
    blowjob_sucking

image Rogue_blowjob_back_hair_animation4:
    "Rogue_back_hair"
    blowjob_deepthroat

layeredimage Rogue_blowjob_back_hair_animations:
    always:
        "Rogue_blowjob_back_hair_animation[action_speed]" pos (0.029, 0.305) zoom 0.2755

image Rogue_blowjob_body_animation0:
    "Rogue_sprite standing"
    blowjob_starting

image Rogue_blowjob_body_animation1:
    "Rogue_sprite standing"
    blowjob_licking_body

image Rogue_blowjob_body_animation2:
    "Rogue_sprite standing"
    blowjob_heading

image Rogue_blowjob_body_animation3:
    "Rogue_sprite standing"
    blowjob_sucking_body

image Rogue_blowjob_body_animation4:
    "Rogue_sprite standing"
    blowjob_deepthroat_body

layeredimage Rogue_blowjob_body_animations:
    always:
        "Rogue_blowjob_body_animation[action_speed]"

image Rogue_blowjob_mask_animation2:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"
    blowjob_face_mask_animation2

image Rogue_blowjob_mask_animation3:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"

image Rogue_blowjob_mask_animation4:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"

image Rogue_blowjob_head_animation0:
    "Rogue_head"
    blowjob_starting

image Rogue_blowjob_head_animation1:
    "Rogue_head"
    blowjob_licking

image Rogue_blowjob_head_animation2:
    "Rogue_head"
    blowjob_heading

image Rogue_blowjob_head_animation3:
    "Rogue_head"
    blowjob_sucking

image Rogue_blowjob_head_animation4:
    "Rogue_head"
    blowjob_deepthroat

layeredimage Rogue_blowjob_head_animations:
    always:
        "Rogue_blowjob_head_animation[action_speed]" pos (0.029, 0.305) zoom 0.2755

image Rogue_blowjob_face_mask_animation2:
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation2")
    anchor (0.5, 0.5)
    blowjob_heading

image Rogue_blowjob_face_mask_animation3:
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation3")
    anchor (0.5, 0.5)
    blowjob_sucking

image Rogue_blowjob_face_mask_animation4:
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation4")
    anchor (0.5, 0.5)
    blowjob_deepthroat

layeredimage Rogue_blowjob_face_mask_animations:
    if action_speed > 1:
        "Rogue_blowjob_face_mask_animation[action_speed]" pos (0.029, 0.305) zoom 0.2755

image Rogue_blowjob_mouth_animation0:
    "images/Rogue_blowjob/Rogue_blowjob_mouth[RogueX.mouth].png"

image Rogue_blowjob_mouth_animation1:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"

image Rogue_blowjob_mouth_animation2:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"
    blowjob_mouth_animation2

image Rogue_blowjob_mouth_animation3:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"

image Rogue_blowjob_mouth_animation4:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"

image Rogue_blowjob_mouth_animation0_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth[RogueX.mouth].png"

image Rogue_blowjob_mouth_animation1_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"

image Rogue_blowjob_mouth_animation2_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking.png"
    blowjob_mouth_animation2

image Rogue_blowjob_mouth_animation3_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking.png"

image Rogue_blowjob_mouth_animation4_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking_spunk.png"

layeredimage Rogue_blowjob_mouth_animations:
    if RogueX.spunk["mouth"]:
        "Rogue_blowjob_mouth_animation[action_speed]_spunk"
    else:
        "Rogue_blowjob_mouth_animation[action_speed]"

layeredimage Rogue_sprite blowjob:
    always:
        "Rogue_blowjob_back_hair_animations"

    always:
        "Rogue_blowjob_body_animations"

    always:
        "Rogue_blowjob_head_animations"

    always:
        "Rogue_blowjob_cock_animations"

    always:
        "Rogue_blowjob_face_mask_animations"

    anchor (0.5, 0.0) offset (220, -150) zoom 2.5

image Rogue_sex_body_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_animation1:
    "Rogue_sex_body"
    block:
        pause 0.5
        easein 0.75 yoffset -5
        pause 1.25
        ease 2.5 yoffset 0
        repeat

image Rogue_sex_body_animation2:
    "Rogue_sex_body"
    block:
        pause 0.6
        easein 0.4 yoffset -10
        ease 0.25 yoffset -5
        pause 1
        ease 2.75 yoffset 10
        repeat

image Rogue_sex_body_animation3:
    "Rogue_sex_body"
    block:
        pause 0.17
        easein 0.13 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 10
        repeat

image Rogue_sex_body_footjob_animation1:
    "Rogue_sex_body"
    block:
        pause 0.5
        easein 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 2.50 yoffset 15
        repeat

image Rogue_sex_body_footjob_animation2:
    "Rogue_sex_body"
    block:
        pause 0.2
        easein 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        repeat

image Rogue_sex_body_hotdog_animation1:
    "Rogue_sex_body"

image Rogue_sex_body_hotdog_animation2:
    "Rogue_sex_body"
    block:
        pause 0.30
        ease 0.50 yoffset 10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Rogue_sex_body_hotdog_animation3:
    "Rogue_sex_body"
    block:
        pause 0.30
        ease 0.50 yoffset 10
        pause 0.20
        ease 1 yoffset 0
        repeat

layeredimage Rogue_sex_body_animations:
    if not action_speed or Player.cock_position in ["in", "anal"]:
        "Rogue_sex_body_animation[action_speed]"
    elif Player.cock_position == "footjob":
        "Rogue_sex_body_footjob_animation[action_speed]"
    elif Player.cock_position == "out":
        "Rogue_sex_body_hotdog_animation[action_speed]"

image Rogue_sex_legs_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_animation1:
    "Rogue_sex_legs"
    block:
        pause 0.25
        easein 1 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation2:
    "Rogue_sex_legs"
    block:
        pause 0.5
        easein 0.5 yoffset -15
        ease 0.25 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation3:
    "Rogue_sex_legs"
    block:
        pause 0.15
        easein 0.15 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 0
        repeat

image Rogue_sex_legs_footjob_animation1:
    "Rogue_sex_legs"
    block:
        pause 0.5
        easein 0.75 yoffset -65
        ease 0.25 yoffset -60
        pause 1
        ease 2.50 yoffset 25
        repeat

image Rogue_sex_legs_footjob_animation2:
    "Rogue_sex_legs"
    block:
        pause 0.2
        easein 0.4 yoffset -65
        ease 0.2 yoffset -60
        pause 0.2
        ease 1.0 yoffset 25
        repeat

image Rogue_sex_legs_hotdog_animation1:
    "Rogue_sex_legs"

image Rogue_sex_legs_hotdog_animation2:
    "Rogue_sex_legs"
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Rogue_sex_legs_hotdog_animation3:
    "Rogue_sex_legs"
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

layeredimage Rogue_sex_legs_animations:
    if not action_speed or Player.cock_position in ["in", "anal"]:
        "Rogue_sex_legs_animation[action_speed]"
    elif Player.cock_position == "footjob":
        "Rogue_sex_legs_footjob_animation[action_speed]"
    elif Player.cock_position == "out":
        "Rogue_sex_legs_hotdog_animation[action_speed]"

image Rogue_sex_anus_animation0:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

image Rogue_sex_anus_animation1:
    "images/Kitty_sex/Kitty_sex_anus_open.png"
    anchor (0.5, 0.5) pos (0.292, 0.386)
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_sex_anus_animation2:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

image Rogue_sex_anus_animation3:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

layeredimage Rogue_sex_anus_animations:
    always:
        "Rogue_sex_anus_animation[action_speed]" pos (0.292, 0.386) xzoom 0.6

image Rogue_sex_spunk_anus_under:
    "images/Kitty_sex/Kitty_sex_spunk_anus_under.png"
    anchor (0.5, 0.5) pos (0.5, 0.5) xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.95
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

layeredimage Rogue_sprite sex:
    always:
        "Rogue_sex_body_animations"

    always:
        "Rogue_sex_legs_animations"

    anchor (0.5, 0.0) offset (370, 800) zoom 1.1

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
    block:
        pause 0.4
        ease 0.3 yoffset -5
        easeout 1 yoffset 0
        pause 0.8
        repeat

image Rogue_doggy_body_animation2:
    "Rogue_doggy_body"
    block:
        pause 0.4
        ease 0.2 yoffset -10
        pause 0.3
        ease 2 yoffset 0
        repeat

image Rogue_doggy_body_animation3:
    "Rogue_doggy_body"
    block:
        pause 0.15
        ease 0.1 yoffset -20
        pause 0.1
        easein 0.5 yoffset 0
        pause 0.05
        repeat

layeredimage Rogue_doggy_body_animations:
    if Player.cock_position == "anal":
        "Rogue_doggy_body_animation[action_speed]"
    elif Player.cock_position == "in" and action_speed > 1:
        "Rogue_doggy_body_animation[action_speed]"
    else:
        "Rogue_doggy_body_animation0"

image Rogue_doggy_ass_animation0:
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation1:
    "Rogue_doggy_ass"
    block:
        pause 0.4
        ease 0.2 yoffset -10
        easeout 0.1 yoffset -7
        easein 0.9 yoffset 0
        pause 0.9
        repeat

image Rogue_doggy_ass_animation2:
    "Rogue_doggy_ass"
    block:
        pause 0.4
        ease 0.2 yoffset -15
        ease 0.1 yoffset -5
        pause 0.2
        ease 1.6 yoffset 0
        repeat

image Rogue_doggy_ass_animation3:
    "Rogue_doggy_ass"
    block:
        pause 0.15
        ease 0.1 yoffset -20
        ease 0.1 yoffset -10
        pause 0.1
        ease 0.4 yoffset 0
        pause 0.05
        repeat

image Rogue_doggy_pussy_hole_animation0:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"
    anchor (0.52, 0.69) offset (217, 513) xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation1:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"
    anchor (0.52, 0.69) offset (217, 513) xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation2:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"

    anchor (0.52, 0.69)

image Rogue_doggy_pussy_hole_animation3:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"

    anchor (0.52, 0.69)

layeredimage Rogue_doggy_pussy_hole_animations:
    always:
        "Rogue_doggy_pussy_hole_animation[action_speed]"

image Rogue_doggy_pussy_mask_animation0:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"
    anchor (0.52, 0.69) offset (217, 513) xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_mask_animation1:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"
    anchor (0.52, 0.69) offset (217, 513) xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_mask_animation2:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"

    anchor (0.52, 0.69)

image Rogue_doggy_pussy_mask_animation3:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"

    anchor (0.52, 0.69)

layeredimage Rogue_doggy_pussy_mask_animations:
    always:
        "Rogue_doggy_pussy_mask_animation[action_speed]"

image Rogue_doggy_pussy_hole_mask_animation0:
    AlphaMask("images/Rogue_doggy/Rogue_doggy_pussy_hole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
    anchor (0.52, 0.69) xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_mask_animation1:
    AlphaMask("images/Rogue_doggy/Rogue_doggy_pussy_hole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
    anchor (0.52, 0.69) xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

layeredimage Rogue_doggy_pussy_hole_mask_animations:
    always:
        "Rogue_doggy_pussy_hole_mask_animation[action_speed]"

image Rogue_doggy_pussy_outer_animation0:
    "images/Rogue_doggy/Rogue_doggy_pussy_heading.png"
    anchor (0.52, 0.69) alpha 0.9
    block:
        ease 1 ypos 512
        pause 1
        ease 3 ypos 515
        repeat

image Rogue_doggy_pussy_outer_animation1:
    "images/Rogue_doggy/Rogue_doggy_pussy_heading.png"
    anchor (0.52, 0.69) alpha 0.9
    block:
        ease 1 ypos 505
        pause 1
        ease 3 ypos 515
        repeat

layeredimage Rogue_doggy_pussy_outer_animations:
    always:
        "Rogue_doggy_pussy_outer_animation[action_speed]"

image Rogue_doggy_pussy_fingering:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"
    anchor (0.52, 0.69) offset (217, 513) xzoom 0.6
    block:
        ease 1 xzoom 0.9
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_anus_anal_animation1:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"
    anchor (0.52, 0.69) offset (217, 513) zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Rogue_doggy_anus_anal_animation2:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_anal_animation3:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"

    anchor (0.52, 0.69)

layeredimage Rogue_doggy_anus_anal_animations:
    always:
        "Rogue_doggy_anus_anal_animation[action_speed]"

image Rogue_doggy_anus_mask_animation0:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_mask_animation1:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"
    anchor (0.52, 0.69) offset (217, 513) zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Rogue_doggy_anus_mask_animation2:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_mask_animation3:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    anchor (0.52, 0.69)

layeredimage Rogue_doggy_anus_mask_animations:
    always:
        "Rogue_doggy_anus_mask_animation[action_speed]"

image Rogue_doggy_anus_fingering:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"
    anchor (0.52, 0.69) offset (217, 513) zoom 0.6
    block:
        ease 0.5 zoom 0.75
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

image Rogue_doggy_anus_fingering_mask:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"
    anchor (0.52, 0.69) offset (217, 513) zoom 0.6
    block:
        ease 0.5 zoom 0.75
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

layeredimage Rogue_doggy_ass_animations:
    if Player.cock_position == "anal":
        "Rogue_doggy_ass_animation[action_speed]"
    elif Player.cock_position == "in" and action_speed > 1:
        "Rogue_doggy_ass_animation[action_speed]"
    else:
        "Rogue_doggy_ass_animation0"

image Rogue_doggy_shin_animation0:
    "Rogue_doggy_shins"
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Rogue_doggy_shin_animation1:
    "Rogue_doggy_shins"
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Rogue_doggy_shin_animation2:
    "Rogue_doggy_shins"
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
    block:
        pause 0.5
        ease 2 yoffset 20
        pause 0.5
        ease 2 yoffset 0
        repeat

image Rogue_doggy_feet_animation1:
    "Rogue_doggy_feet"
    block:
        pause 0.3
        ease 1.7 yoffset 100
        ease 1 yoffset 0
        repeat

image Rogue_doggy_feet_animation2:
    "Rogue_doggy_feet"
    block:
        pause 0.05
        ease 0.6 yoffset 110
        ease 0.3 yoffset 0
        repeat

layeredimage Rogue_doggy_feet_animations:
    always:
        "Rogue_doggy_feet_animation[action_speed]"

layeredimage Rogue_sprite doggy:
    always:
        "Rogue_doggy_body_animations"

    always:
        "Rogue_doggy_ass_animations"

    if Player.sprite and Player.cock_position == "footjob":
        "Rogue_doggy_shin_animations"
    elif not Player.sprite or show_feet:
        "Rogue_doggy_shins"

    if Player.sprite and Player.cock_position == "footjob":
        "Rogue_doggy_cock_footjob_animations"

    if Player.cock_position == "footjob":
        "Rogue_doggy_feet_animations"
    elif not Player.sprite or show_feet:
        "Rogue_doggy_feet"

    anchor (0.5, 0.0) offset (150, 700) zoom 1.2
