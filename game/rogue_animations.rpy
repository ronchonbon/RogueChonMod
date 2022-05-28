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

image Rogue_handjob_under_hand_animation0:
    subpixel True
    "Rogue_handjob_under"

image Rogue_handjob_under_hand_animation1:
    subpixel True
    "Rogue_handjob_under"
    block:
        ease 0.5 yoffset -40 rotate 5
        pause 0.25
        ease 1.0 yoffset 10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_under_hand_animation2:
    subpixel True
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
    subpixel True
    "Rogue_handjob_over"

image Rogue_handjob_over_hand_animation1:
    subpixel True
    "Rogue_handjob_over"
    block:
        ease 0.5 yoffset -40 rotate 5
        pause 0.25
        ease 1.0 yoffset 10 rotate -5
        pause 0.1
        repeat

image Rogue_handjob_over_hand_animation2:
    subpixel True
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

layeredimage Rogue_handjob_animation:
    always:
        "Rogue_sprite" pos (0.05, 0.0)

    always:
        "Rogue_handjob_under_hand_animations"

    always:
        "Zero_handjob_cock_animations"

    always:
        "Rogue_handjob_over_hand_animations"

    anchor (0.5, 0.0) offset (550, -200) zoom 2.5

image Rogue_titjob_under_tits_animation0:
    subpixel True
    "Rogue_titjob_under"

image Rogue_titjob_under_tits_animation1:
    subpixel True
    "Rogue_titjob_under"
    block:
        ease 1 yoffset 0
        easeout 0.2 yoffset 0
        easein 1.3 yoffset -50
        repeat

image Rogue_titjob_under_tits_animation2:
    subpixel True
    "Rogue_titjob_under"
    block:
        ease 0.25 yoffset 0
        ease 0.4 yoffset -50
        ease 0.1 yoffset -55
        repeat

layeredimage Rogue_titjob_under_tits_animations:
    always:
        "Rogue_titjob_under_tits_animation[action_speed]" pos (0.2, 0.8)

image Rogue_titjob_over_tits_animation0:
    subpixel True
    "Rogue_titjob_over"

image Rogue_titjob_over_tits_animation1:
    subpixel True
    "Rogue_titjob_over"
    block:
        ease 1.20 yoffset 0
        easeout 0.1 yoffset 0
        easein 1.2 yoffset -50
        repeat

image Rogue_titjob_over_tits_animation2:
    subpixel True
    "Rogue_titjob_over"
    block:
        ease 0.3 yoffset 0
        ease 0.35 yoffset -50
        ease 0.1 yoffset -55
        repeat

layeredimage Rogue_titjob_over_tits_animations:
    always:
        "Rogue_titjob_over_tits_animation[action_speed]" pos (-0.043, 0.8)

layeredimage Rogue_titjob_animation:
    always:
        "Rogue_titjob_under_tits_animations"

    always:
        "Zero_titjob_cock_animations"

    always:
        "Rogue_titjob_over_tits_animations"

    anchor (0.5, 0.0) offset (550, 200) zoom 0.72

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
        "Rogue_blowjob_back_hair_animation[action_speed]" pos (0.1105, 0.3272) zoom 0.2755

image Rogue_blowjob_body_animation0:
    "Rogue_sprite"
    blowjob_starting

image Rogue_blowjob_body_animation1:
    "Rogue_sprite"
    blowjob_licking_body

image Rogue_blowjob_body_animation2:
    "Rogue_sprite"
    blowjob_heading

image Rogue_blowjob_body_animation3:
    "Rogue_sprite"
    blowjob_sucking_body

image Rogue_blowjob_body_animation4:
    "Rogue_sprite"
    blowjob_deepthroat_body

layeredimage Rogue_blowjob_body_animations:
    always:
        "Rogue_blowjob_body_animation[action_speed]" pos (-0.051, -0.01)

image Rogue_blowjob_mask_animation2:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"
    blowjob_face_mask_animation2

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
    blowjob_heading

image Rogue_blowjob_face_mask_animation3:
    AlphaMask("Rogue_head", "images/Rogue_blowjob/Rogue_blowjob_face_mask.png")
    blowjob_sucking

image Rogue_blowjob_face_mask_animation4:
    AlphaMask("Rogue_head", "images/Rogue_blowjob/Rogue_blowjob_face_mask.png")
    blowjob_deepthroat

layeredimage Rogue_blowjob_face_mask_animations:
    if action_speed > 1:
        "Rogue_blowjob_face_mask_animation[action_speed]" pos (-0.0275, 0.1885) zoom 0.2755

image Rogue_blowjob_mouth_animation2:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"
    blowjob_mouth_animation2

image Rogue_blowjob_mouth_animation2_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking_spunk.png"
    blowjob_mouth_animation2

layeredimage Rogue_blowjob_mouth_animations:
    if RogueX.spunk["mouth"]:
        "Rogue_blowjob_mouth_animation[action_speed]_spunk"
    else:
        "Rogue_blowjob_mouth_animation[action_speed]"

layeredimage Rogue_blowjob_animation:
    always:
        "Rogue_blowjob_back_hair_animations"

    always:
        "Rogue_blowjob_body_animations"

    always:
        "Rogue_blowjob_head_animations"

    always:
        "Zero_blowjob_cock_animations"

    always:
        "Rogue_blowjob_face_mask_animations"

    anchor (0.5, 0.0) offset (550, -150) zoom 2.5

image Rogue_sex_body_animation0:
    subpixel True
    "Rogue_sex_body"

image Rogue_sex_body_animation1:
    subpixel True
    "Rogue_sex_body"
    block:
        pause 0.5
        easein 0.75 yoffset -5
        pause 1.25
        ease 2.5 yoffset 0
        repeat

image Rogue_sex_body_animation2:
    subpixel True
    "Rogue_sex_body"
    block:
        pause 0.6
        easein 0.4 yoffset -10
        ease 0.25 yoffset -5
        pause 1
        ease 2.75 yoffset 10
        repeat

image Rogue_sex_body_animation3:
    subpixel True
    "Rogue_sex_body"
    block:
        pause 0.17
        easein 0.13 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 10
        repeat

image Rogue_sex_body_footjob_animation1:
    subpixel True
    "Rogue_sex_body"
    block:
        pause 0.5
        easein 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 2.50 yoffset 15
        repeat

image Rogue_sex_body_footjob_animation2:
    subpixel True
    "Rogue_sex_body"
    block:
        pause 0.2
        easein 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        repeat

image Rogue_sex_body_hotdog_animation1:
    subpixel True
    "Rogue_sex_body"

image Rogue_sex_body_hotdog_animation2:
    subpixel True
    "Rogue_sex_body"
    block:
        pause 0.30
        ease 0.50 yoffset 10
        pause 0.20
        ease 1 yoffset 0
        repeat

image Rogue_sex_body_hotdog_animation3:
    subpixel True
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
    subpixel True
    "Rogue_sex_legs"

image Rogue_sex_legs_animation1:
    subpixel True
    "Rogue_sex_legs"
    block:
        pause 0.25
        easein 1 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation2:
    subpixel True
    "Rogue_sex_legs"
    block:
        pause 0.5
        easein 0.5 yoffset -15
        ease 0.25 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation3:
    subpixel True
    "Rogue_sex_legs"
    block:
        pause 0.15
        easein 0.15 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 0
        repeat

image Rogue_sex_legs_footjob_animation1:
    subpixel True
    "Rogue_sex_legs"
    block:
        pause 0.5
        easein 0.75 yoffset -65
        ease 0.25 yoffset -60
        pause 1
        ease 2.50 yoffset 25
        repeat

image Rogue_sex_legs_footjob_animation2:
    subpixel True
    "Rogue_sex_legs"
    block:
        pause 0.2
        easein 0.4 yoffset -65
        ease 0.2 yoffset -60
        pause 0.2
        ease 1.0 yoffset 25
        repeat

image Rogue_sex_legs_hotdog_animation1:
    subpixel True
    "Rogue_sex_legs"

image Rogue_sex_legs_hotdog_animation2:
    subpixel True
    "Rogue_sex_legs"
    block:
        pause 0.20
        ease 0.50 yoffset -10
        pause 0.20
        ease 1.1 yoffset 0
        repeat

image Rogue_sex_legs_hotdog_animation3:
    subpixel True
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

image Rogue_sex_anus_animation1:
    "images/Kitty_sex/Kitty_sex_anus_open.png"
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_sex_anus_animation2:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

image Rogue_sex_anus_animation3:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

layeredimage Rogue_sex_anus_animations:
    always:
        "Rogue_sex_anus_animation[action_speed]" anchor (0.5, 0.5) pos (0.292, 0.386) xzoom 0.6

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

layeredimage Rogue_sex_animation:
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
    subpixel True
    "Rogue_doggy_body"

image Rogue_doggy_body_animation1:
    subpixel True
    "Rogue_doggy_body"
    block:
        pause 0.4
        ease 0.3 yoffset -5
        easeout 1 yoffset 0
        pause 0.8
        repeat

image Rogue_doggy_body_animation2:
    subpixel True
    "Rogue_doggy_body"
    block:
        pause 0.4
        ease 0.2 yoffset -10
        pause 0.3
        ease 2 yoffset 0
        repeat

image Rogue_doggy_body_animation3:
    subpixel True
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
    subpixel True
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation1:
    subpixel True
    "Rogue_doggy_ass"
    block:
        pause 0.4
        ease 0.2 yoffset -10
        easeout 0.1 yoffset -7
        easein 0.9 yoffset 0
        pause 0.9
        repeat

image Rogue_doggy_ass_animation2:
    subpixel True
    "Rogue_doggy_ass"
    block:
        pause 0.4
        ease 0.2 yoffset -15
        ease 0.1 yoffset -5
        pause 0.2
        ease 1.6 yoffset 0
        repeat

image Rogue_doggy_ass_animation3:
    subpixel True
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
    subpixel True
    anchor (0.52, 0.69) offset (217, 513) xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation1:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"
    subpixel True
    anchor (0.52, 0.69) offset (217, 513) xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation2:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"

image Rogue_doggy_pussy_hole_animation3:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"

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

image Rogue_doggy_pussy_mask_animation3:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"

layeredimage Rogue_doggy_pussy_mask_animations:
    always:
        "Rogue_doggy_pussy_mask_animation[action_speed]"

image Rogue_doggy_pussy_hole_mask_animation0:
    AlphaMask("images/Rogue_doggy/Rogue_doggy_pussy_hole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
    subpixel True
    anchor (0.52, 0.69) xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_mask_animation1:
    AlphaMask("images/Rogue_doggy/Rogue_doggy_pussy_hole.png", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")
    subpixel True
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
    subpixel True
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

image Rogue_doggy_anus_anal_animation3:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"

layeredimage Rogue_doggy_anus_anal_animations:
    always:
        "Rogue_doggy_anus_anal_animation[action_speed]"

image Rogue_doggy_anus_mask_animation0:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

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

image Rogue_doggy_anus_mask_animation3:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

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
        subpixel True
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
        subpixel True
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
        "Rogue_doggy_feet_animation[action_speed]" pos (-0.1095, -0.347)

layeredimage Rogue_doggy_animation:
    always:
        "Rogue_doggy_body_animations"

    always:
        "Rogue_doggy_ass_animations"

    if Player.sprite and Player.cock_position == "footjob":
        "Rogue_doggy_shin_animations"
    elif not Player.sprite or show_feet:
        "Rogue_doggy_shins"
    else:
        "Rogue_doggy_shins" alpha 0.0

    if Player.sprite and Player.cock_position == "footjob":
        "Zero_doggy_cock_footjob_animations"

    if Player.cock_position == "footjob":
        "Rogue_doggy_feet_animations"
    elif not Player.sprite or show_feet:
        "Rogue_doggy_feet" pos (-0.1095, -0.347)
    else:
        "Rogue_doggy_feet" pos (-0.1095, -0.347) alpha 0.0

    anchor (0.5, 0.0) offset (1050, 650) zoom 1.2
