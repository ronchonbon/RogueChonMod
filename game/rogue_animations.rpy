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

image Rogue_squinting:
    "images/Rogue_blowjob/Rogue_blowjob_eyes_sexy.png",
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_blowjob/Rogue_blowjob_eyes_squint.png",
    0.25
    repeat

layeredimage Rogue_standing_fondling:
    if primary_action == "lesbian" or not girl_offhand_action or focused_Girl != RogueX:
            Null()
    elif primary_action != "sex" and girl_offhand_action == "fondle_pussy" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy"
    elif girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "GirlGropeLeftBreast"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast"

    if second_girl_primary_action != "masturbation" or not second_girl_offhand_action or focused_Girl == RogueX:
        Null()
    elif primary_action != "sex" and second_girl_offhand_action == "fondle_pussy" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif second_girl_offhand_action == "fondle_pussy":
        "GirlGropePussy"
    elif second_girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "GirlGropeLeftBreast"
    elif second_girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast"

    if not primary_action or focused_Girl != RogueX:
        Null()
    elif primary_action == "fondle_thighs":
        "GropeThigh"
    elif primary_action == "fondle_breasts":
        "GropeRightBreast"
    elif primary_action == "suck_breasts":
        "LickRightBreast"
    elif primary_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy"
    elif primary_action == "fondle_pussy":
        "GropePussy"
    elif primary_action == "eat_pussy":
        "Lickpussy"

    if not offhand_action or focused_Girl != RogueX:
        Null()
    elif primary_action == "fondle_breasts" and not girl_offhand_action and not second_girl_primary_action and not second_girl_offhand_action:
        "GropeRightBreast"
    elif offhand_action == "fondle_thighs":
        "GropeThigh"
    elif offhand_action == "fondle_breasts":
        "GropeLeftBreast"
    elif offhand_action == "suck_breasts":
        "LickLeftBreast"
    elif offhand_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy"
    elif offhand_action == "fondle_pussy":
        "GropePussy"
    elif offhand_action == "eat_pussy":
        "Lickpussy"

    if not second_girl_primary_action or focused_Girl != RogueX:
        Null()
    elif second_girl_primary_action == "fondle_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "GirlGropeLeftBreast"
    elif second_girl_priamry_action == "fondle_breasts":
        "GirlGropeRightBreast"
    elif second_girl_primary_action == "suck_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast"
    elif second_girl_primary_action == "suck_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast"
    elif second_girl_priamry_action == "suck_breasts":
        "LickRightBreast"
    elif second_girl_primary_action == "fondle_pussy" and primary_action != "sex" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif second_girl_primary_action == "fondle_pussy" and offhand_action != "sex" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif second_girl_primary_action == "fondle_pussy":
        "GropePussy"
    elif second_girl_primary_action == "eat_pussy":
        "Lickpussy"

    if primary_action != "lesbian" or not girl_offhand_action or focused_Girl == RogueX:
        Null()
    elif girl_offhand_action == "fondle_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "GirlGropeLeftBreast"
    elif girl_offhand_action == "fondle_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "GirlGropeLeftBreast"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast"
    elif girl_offhand_action == "suck_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast"
    elif girl_offhand_action == "suck_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast"
    elif girl_offhand_action == "suck_breasts":
        "LickRightBreast"
    elif girl_offhand_action == "fondle_pussy" and primary_action != "sex" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy"
    elif girl_offhand_action == "eat_pussy":
        "Lickpussy"

transform Rogue_handjob_hand_animation1:
    subpixel True
    ease 0.5 yoffset -40 rotate 5
    pause 0.25
    ease 1.0 yoffset 10 rotate -5
    pause 0.1
    repeat

transform Rogue_handjob_hand_animation2:
    subpixel True
    ease 0.2 yoffset -30 rotate 3
    pause 0.1
    ease 0.4 yoffset 10 rotate -3
    pause 0.1
    repeat

layeredimage Rogue_handjob_animation:
    always:
        "Rogue_sprite" pos (0.1, 0.05)

    if not action_speed:
        "Rogue_handjob_under" pos (-0.04, 0.455) zoom 0.28
    elif action_speed == 1:
        At("Rogue_handjob_under", Rogue_handjob_hand_animation1) pos (-0.04, 0.455) zoom 0.28
    elif action_speed >= 2:
        At("Rogue_handjob_under", Rogue_handjob_hand_animation2) pos (-0.04, 0.455) zoom 0.28

    if not action_speed:
        "Zero_handjob_cock" pos (-0.04, 0.455) zoom 0.28
    elif action_speed == 1:
        At("Zero_handjob_cock", Zero_handjob_cock_animation1) pos (-0.04, 0.455) zoom 0.28
    elif action_speed >= 2:
        At("Zero_handjob_cock", Zero_handjob_cock_animation2) pos (-0.04, 0.455) zoom 0.28

    if not action_speed:
        "Rogue_handjob_over" pos (-0.04, 0.455) zoom 0.28
    elif action_speed == 1:
        At("Rogue_handjob_over", Rogue_handjob_hand_animation1) pos (-0.04, 0.455) zoom 0.28
    elif action_speed >= 2:
        At("Rogue_handjob_over", Rogue_handjob_hand_animation2) pos (-0.04, 0.455) zoom 0.28

    anchor (0.0, 0.09) zoom 2.5

transform Zero_titjob_cock_animation0:
    pos (440,1020)

transform Zero_titjob_cock_animation1:
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout 0.2 ypos 1060
        easein 1.3 ypos 1020
        repeat

transform Zero_titjob_cock_animation2:
    pos (440,1020)
    subpixel True
    block:
        ease 0.35 ypos 1030
        ease 0.4 ypos 1020
        repeat

transform Rogue_titjob_under_animation1:
    pos (0, 200)
    subpixel True
    block:
        ease 1 ypos 300
        easeout 0.2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_titjob_over_animation1:
    pos (0, 200)
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout 0.1 ypos 300
        easein 1.2 ypos 120
        repeat

transform Rogue_titjob_under_animation2:
    pos (0, 200)
    subpixel True
    block:
        ease 0.25 ypos 200
        ease 0.4 ypos 120
        ease 0.1 ypos 125
        repeat

transform Rogue_titjob_over_animation2:
    pos (0, 200)
    subpixel True
    block:
        ease 0.3 ypos 200
        ease 0.35 ypos 120
        ease 0.1 ypos 125
        repeat

layeredimage Rogue_titjob_animation:
    if not action_speed:
        "Rogue_titjob_under"
    elif action_speed == 1:
        At("Rogue_titjob_under", Rogue_titjob_under_animation1)
    elif action_speed >= 2:
        At("Rogue_titjob_under", Rogue_titjob_under_animation2)

    if not action_speed:
        At("Zero_handjob_cock", Zero_titjob_cock_animation0) zoom 0.8
    elif action_speed == 1:
        At("Zero_handjob_cock", Zero_titjob_cock_animation1) zoom 0.8
    elif action_speed >= 2:
        At("Zero_handjob_cock", Zero_titjob_cock_animation2) zoom 0.8

    if not action_speed:
        "Rogue_titjob_over"
    elif action_speed == 1:
        At("Rogue_titjob_over", Rogue_titjob_over_animation1)
    elif action_speed >= 2:
        At("Rogue_titjob_over", Rogue_titjob_over_animation2)

    always:
        "Rogue_head"

    anchor (0.5, -0.2) zoom 0.55

transform blowjob_mouth_animation2:
    subpixel True
    pos (0.165, 0.521) anchor (0.4, 0.6) zoom 0.90
    block:
        pause 0.10
        easeout 0.55 zoom 0.9
        linear 0.10 zoom 0.87
        easein 0.30 zoom 0.9
        pause 0.15
        easeout 0.40 zoom 0.87
        linear 0.10 zoom 0.9
        easein 0.45 zoom 0.70
        pause 0.35
        repeat

transform blowjob_face_mask_animation2:
    subpixel True
    pos (0.445, 0.616) anchor (0.45, 0.6) zoom 0.90
    block:
        pause 0.10
        easeout 0.55 zoom 0.9
        linear 0.10 zoom 0.87
        easein 0.30 zoom 0.9
        pause 0.15
        easeout 0.40 zoom 0.87
        linear 0.10 zoom 0.9
        easein 0.45 zoom 0.70
        pause 0.35
        repeat

image Rogue_blowjob_mask_animation2:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"
    blowjob_face_mask_animation2

image Rogue_blowjob_body_animation0:
    "Rogue_sprite"
    blowjob_starting

image Rogue_blowjob_head_animation0:
    "Rogue_head"
    blowjob_starting

image Rogue_blowjob_back_hair_animation0:
    "Rogue_back_hair"
    blowjob_starting

image Rogue_blowjob_body_animation1:
    "Rogue_sprite"
    blowjob_licking_body

image Rogue_blowjob_head_animation1:
    "Rogue_head"
    blowjob_licking

image Rogue_blowjob_back_hair_animation1:
    "Rogue_back_hair"
    blowjob_licking

image Rogue_blowjob_body_animation2:
    "Rogue_sprite"
    blowjob_heading

image Rogue_blowjob_head_animation2:
    "Rogue_head"
    blowjob_heading

image Rogue_blowjob_back_hair_animation2:
    "Rogue_back_hair"
    blowjob_heading

image Rogue_blowjob_face_mask_animation2:
    AlphaMask("Rogue_head", "Rogue_blowjob_mask_animation2")
    blowjob_heading

image Rogue_blowjob_body_animation3:
    "Rogue_sprite"
    blowjob_sucking_body

image Rogue_blowjob_head_animation3:
    "Rogue_head"
    blowjob_sucking

image Rogue_blowjob_back_hair_animation3:
    "Rogue_back_hair"
    blowjob_sucking

image Rogue_blowjob_face_mask_animation3:
    AlphaMask("Rogue_head", "images/Rogue_blowjob/Rogue_blowjob_face_mask.png")
    blowjob_sucking

image Rogue_blowjob_body_animation4:
    "Rogue_sprite"
    blowjob_deepthroat_body

image Rogue_blowjob_head_animation4:
    "Rogue_head"
    blowjob_deepthroat

image Rogue_blowjob_back_hair_animation4:
    "Rogue_back_hair"
    blowjob_deepthroat

image Rogue_blowjob_face_mask_animation4:
    AlphaMask("Rogue_head", "images/Rogue_blowjob/Rogue_blowjob_face_mask.png")
    blowjob_deepthroat

image Rogue_blowjob_mouth_animation2:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"
    blowjob_mouth_animation2

image Rogue_blowjob_mouth_animation2_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking_spunk.png"
    blowjob_mouth_animation2

layeredimage Rogue_blowjob_animation:
    always:
        "Rogue_blowjob_back_hair_animation[action_speed]" pos (0.1105, 0.3272) zoom 0.2755

    always:
        "Rogue_blowjob_body_animation[action_speed]"

    always:
        "Rogue_blowjob_head_animation[action_speed]" pos (0.029, 0.305) zoom 0.2755

    always:
        "Zero_blowjob_cock_animation[action_speed]" pos (0.021, 0.455) zoom 0.28

    if action_speed > 1:
        "Rogue_blowjob_face_mask_animation[action_speed]" pos (-0.0275, 0.1885) zoom 0.2755

    anchor (0.0, 0.075) zoom 2.5

layeredimage Rogue_sex_animation:
    if not Player.sprite:
        "Rogue_sex_body_animation0"
    elif Player.cock_position in ['in', 'anal']:
        "Rogue_sex_body_animation[action_speed]"
    elif Player.cock_position == 'footjob':
        "Rogue_sex_body_FootAnim[action_speed]"
    else:
        "Rogue_sex_body_animation0"

    if not Player.sprite:
        "Rogue_sex_legs_animation0"
    elif Player.cock_position in ['in', 'anal']:
        "Rogue_sex_legs_animation[action_speed]"
    elif Player.cock_position == 'footjob':
        "Rogue_sex_legs_FootAnim[action_speed]"
    elif Player.cock_position == 'out' and action_speed >= 2:
        "Rogue_Hotdog_Legs_animation[action_speed]"
    else:
        "Rogue_sex_legs_animation0"

    anchor (0.5, -0.5) zoom 0.85

image Rogue_doggy_blinking:
    "Rogue_doggy_eyes"
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

layeredimage Rogue_doggy_animation:
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

    if Player.cock_position == "footjob":
        "Rogue_doggy_feet_animation[action_speed]"
    elif not Player.sprite and show_feet:
        "Rogue_doggy_feet_animation0"

    anchor (0.5, -0.2)

image Rogue_doggy_pussy_mask:
    contains:
        "images/Rogue_doggy/Rogue_doggy_sex_mask.png"
        pos (217, 518) anchor (0.52, 0.69) xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Rogue_doggy_pussy_mask_animation0:
    contains:
        "images/Rogue_doggy/Rogue_doggy_sex_mask.png"
        pos (217, 518) anchor (0.52, 0.69) xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat

image Rogue_doggy_pussy_animation0:
    subpixel True
    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
        pos (220, 518) anchor (0.52, 0.69)

    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"
        subpixel True
        pos (217, 518) anchor (0.52, 0.69) xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat

    contains:
        ConditionSwitch(
            "RogueX.outfit['hose'] == '_garterbelt'", "images/Rogue_doggy/Rogue_doggy_hose_garterbelt.png",
            "RogueX.outfit['hose'] == '_stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_doggy_hose_stockings_and_garterbelt.png",
            "RogueX.outfit['underwear'] and RogueX.underwear_pulled_down", Null(),
            "RogueX.outfit['hose'] == '_ripped_pantyhose'", "images/Rogue_doggy/Rogue_doggy_hose_ripped_pantyhose.png",
            "RogueX.outfit['hose'] == '_ripped_tights'", "images/Rogue_doggy/Rogue_doggy_hose_ripped_tights.png",
            "True", Null())

    contains:
        AlphaMask("Zero_doggy_static", "Rogue_doggy_pussy_mask_animation0")

    contains:
        AlphaMask("Rogue_doggy_pussy_hole_animation0", "Rogue_doggy_pussy_hole_mask_animation0")

image Rogue_doggy_pussy_hole_mask_animation0:
    contains:
        AlphaMask("images/Rogue_doggy/Rogue_doggy_pussy_hole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
        subpixel True
        pos (217, 518) anchor (0.52, 0.69) xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat

image Rogue_doggy_pussy_hole_animation0:
    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_heading.png"
        pos (217, 515)anchor (0.52, 0.69) alpha 0.9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat

image Rogue_doggy_pussy_heading:
    subpixel True
    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
        pos (220, 518)anchor (0.52, 0.69)

    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"
        subpixel True
        pos (217, 518) anchor (0.52, 0.69) xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

    contains:
        ConditionSwitch(
            "RogueX.outfit['hose'] == '_garterbelt'", "images/Rogue_doggy/Rogue_doggy_hose_garterbelt.png",
            "RogueX.outfit['hose'] == '_stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_doggy_hose_stockings_and_garterbelt.png",
            "RogueX.outfit['underwear'] and RogueX.underwear_pulled_down", Null(),
            "RogueX.outfit['hose'] == '_ripped_pantyhose'", "images/Rogue_doggy/Rogue_doggy_hose_ripped_pantyhose.png",
            "RogueX.outfit['hose'] == '_ripped_tights'", "images/Rogue_doggy/Rogue_doggy_hose_ripped_tights.png",
            "True", Null())

    contains:
        AlphaMask("Zero_doggy_heading", "Rogue_doggy_pussy_mask")

    contains:
        AlphaMask("Rogue_doggy_pussy_flap_heading", "Rogue_doggy_pussy_hole_mask")

image Rogue_doggy_pussy_hole_mask:
    contains:
        AlphaMask("images/Rogue_doggy/Rogue_doggy_pussy_hole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
        subpixel True
        pos (217, 518) anchor (0.52, 0.69) xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Rogue_doggy_pussy_flap_heading:
    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_heading.png"
        pos (217, 515) anchor (0.52, 0.69)
        alpha 0.9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Rogue_doggy_pussy_fingering:
    subpixel True
    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
        pos (220,518) anchor (0.52,0.69)

    contains:
        "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"
        subpixel True
        pos (217,518) anchor (0.52, 0.69) xzoom 0.6
        block:
            ease 1 xzoom 0.9
            pause 1
            ease 3 xzoom 0.6
            repeat

    contains:
        ConditionSwitch(
            "RogueX.outfit['hose'] == '_garterbelt'", "images/Rogue_doggy/Rogue_doggy_hose_garterbelt.png",
            "RogueX.outfit['hose'] == '_stockings_and_garterbelt'", "images/Rogue_doggy/Rogue_doggy_hose_stockings_and_garterbelt.png",
            "RogueX.outfit['underwear'] and RogueX.underwear_pulled_down", Null(),
            "RogueX.outfit['hose'] == '_ripped_pantyhose'", "images/Rogue_doggy/Rogue_doggy_hose_ripped_pantyhose.png",
            "RogueX.outfit['hose'] == '_ripped_tights'", "images/Rogue_doggy/Rogue_doggy_hose_ripped_tights.png",
            "True", Null())

    contains:
        AlphaMask("Zero_Pussy_Finger", "Rogue_doggy_pussy_mask")

    contains:
        AlphaMask("Rogue_doggy_pussy_flap_heading", "Rogue_doggy_pussy_hole_mask")

image doggy_licking_pussy:
    "licking"
    zoom 0.5
    offset (195, 540)

image doggy_licking_ass:
    "licking"
    zoom 0.5
    offset (195, 500)
