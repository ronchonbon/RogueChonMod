image Rogue_blinking:
    "Rogue_eyes"
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

image Rogue_handjob_animation:
    contains:
        ConditionSwitch(
            "not action_speed", "Rogue_handjob_under",
            "action_speed == 1", At("Rogue_handjob_under", Rogue_Hand_1()),
            "action_speed >= 2", At("Rogue_handjob_under", Rogue_Hand_2()),
            "action_speed ", Null()),

    contains:
        ConditionSwitch(
            "not action_speed", "Zero_handjob_cock",
            "action_speed == 1", At("Zero_handjob_cock", Handcock_1()),
            "action_speed >= 2", At("Zero_handjob_cock", Handcock_2()),
            "action_speed ", Null()),

    contains:
        ConditionSwitch(
            "not action_speed", "Rogue_handjob_over",
            "action_speed == 1", At("Rogue_handjob_over", Rogue_Hand_1()),
            "action_speed >= 2", At("Rogue_handjob_over", Rogue_Hand_2()),
            "action_speed ", Null()),

    anchor (0.5,0.5) offset (200,800) zoom 0.6

image Rogue_titjob_animation:
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Rogue_titjob_under"),
            "action_speed == 1", At("Rogue_titjob_under", Rogue_titjob_under_1()),
            "action_speed >= 2", At("Rogue_titjob_under", Rogue_titjob_under_2()),
            "action_speed ", Null()),

    contains:
        ConditionSwitch(
            "not action_speed", At("Zero_titjob_cock", Zero_TJ_Cock()),
            "action_speed == 1", At("Zero_titjob_cock", Zero_TJ_Cock_1()),
            "action_speed >= 2", At("Zero_titjob_cock", Zero_TJ_Cock_2()),
            "action_speed ", Null()),

    contains:
        ConditionSwitch(
            "not action_speed", Transform("Rogue_titjob_over"),
            "action_speed == 1", At("Rogue_titjob_over", Rogue_titjob_over_1()),
            "action_speed >= 2", At("Rogue_titjob_over", Rogue_titjob_over_2()),
            "action_speed ", Null()),

    anchor (0.6, 0.0) offset (-75, 250) zoom 0.55

transform Rogue_blowjob_mouth_animation:
    subpixel True
    zoom 0.90
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

image Rogue_blowjob_head:
    "Rogue_head"
    zoom 3.45

image Rogue_blowjob_back_hair:
    "Rogue_back_hair"
    zoom 3.45

image Rogue_blowjob_body:
    "Rogue_sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Rogue_blowjob_mask:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"
    anchor (0.4,0.65)

image Rogue_blowjob_mask_heading:
    contains:
        "Rogue_blowjob_mask"
        Rogue_blowjob_mouth_animation

    pos(316, 590)

image Rogue_blowjob_body_animation0:
    "Rogue_blowjob_body"
    blowjob_starting

image Rogue_blowjob_head_animation0:
    "Rogue_blowjob_head"
    blowjob_starting

image Rogue_blowjob_back_hair_animation0:
    "Rogue_blowjob_back_hair"
    blowjob_starting

image Rogue_blowjob_body_animation1:
    "Rogue_blowjob_body"
    blowjob_licking_body

image Rogue_blowjob_head_animation1:
    "Rogue_blowjob_head"
    blowjob_licking

image Rogue_blowjob_back_hair_animation1:
    "Rogue_blowjob_back_hair"
    blowjob_licking

image Rogue_blowjob_body_animation2:
    "Rogue_blowjob_body"
    blowjob_heading

image Rogue_blowjob_head_animation2:
    "Rogue_blowjob_head"
    blowjob_heading

image Rogue_blowjob_back_hair_animation2:
    "Rogue_blowjob_back_hair"
    blowjob_heading

image Rogue_blowjob_face_mask_animation2:
    AlphaMask("Rogue_blowjob_head", "Rogue_blowjob_mask_heading")
    blowjob_heading

image Rogue_blowjob_body_animation3:
    "Rogue_blowjob_body"
    blowjob_sucking_body

image Rogue_blowjob_head_animation3:
    "Rogue_blowjob_head"
    blowjob_sucking

image Rogue_blowjob_back_hair_animation3:
    "Rogue_blowjob_back_hair"
    blowjob_sucking

image Rogue_blowjob_face_mask_animation3:
    AlphaMask("Rogue_blowjob_head", "images/Rogue_blowjob/Rogue_blowjob_face_mask.png")
    blowjob_sucking

image Rogue_blowjob_body_animation4:
    "Rogue_blowjob_body"
    blowjob_deepthroat_body

image Rogue_blowjob_head_animation4:
    "Rogue_blowjob_head"
    blowjob_deepthroat

image Rogue_blowjob_back_hair_animation4:
    "Rogue_blowjob_back_hair"
    blowjob_deepthroat

image Rogue_blowjob_face_mask_animation4:
    AlphaMask("Rogue_blowjob_head", "images/Rogue_blowjob/Rogue_blowjob_face_mask.png")
    blowjob_deepthroat

image Rogue_blowjob_mouth_sucking:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"
    Rogue_blowjob_mouth_animation

image Rogue_blowjob_mouth_sucking_spunk:
    "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking_spunk.png"
    Rogue_blowjob_mouth_animation

image Rogue_blowjob_animation:
    LiveComposite(
        (787, 913),
        (0, 0), "Rogue_blowjob_back_hair_animation[action_speed]",
        (0, 0), "Rogue_blowjob_body_animation[action_speed]",
        (0, 0), "Rogue_blowjob_head_animation[action_speed]",
        (-0.224, 0.15), "Zero_blowjob_cock_animation[action_speed]",
        (0, 0), ConditionSwitch(
            "action_speed > 1", "Rogue_blowjob_face_mask_animation[action_speed]",
            "True", Null()),
        )
    zoom 0.55
    anchor (0.5, 0.5)

image Rogue_sex_animation:
    LiveComposite(
        (1120,840),

        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_sex_body_animation0",
            "Player.cock_position in ['sex', 'anal']", "Rogue_sex_body_animation[action_speed]",
            "Player.cock_position == 'footjob'", "Rogue_sex_body_FootAnim[action_speed]",
            "Player.cock_position == 'out' and action_speed >= 2","Rogue_Hotdog_Body_animation[action_speed]",
            "True", "Rogue_sex_body_animation0"),
        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_sex_legs_animation0",
            "Player.cock_position in ['sex', 'anal']", "Rogue_sex_legs_animation[action_speed]",
            "Player.cock_position == 'footjob'", "Rogue_sex_legs_FootAnim[action_speed]",
            "Player.cock_position == 'out' and action_speed >= 2","Rogue_Hotdog_Legs_animation[action_speed]",
            "True", "Rogue_sex_legs_animation0"))

    align (2.5, 2.5) zoom 0.85

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

image Rogue_doggy_animation:
    LiveComposite(
        (420,750),
        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_doggy_body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Top",
                    "action_speed ", "Rogue_Doggy_Anal_Head_Top",
                    "True", "Rogue_doggy_body"),
            "Player.cock_position == 'sex'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Top",
                    "True", "Rogue_doggy_body"),
            "True", "Rogue_doggy_body"),
        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_doggy_ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "action_speed ", "Rogue_Doggy_Anal_Head_Ass",
                    "True", "Rogue_doggy_ass"),
            "Player.cock_position == 'sex'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "True", "Rogue_doggy_ass"),
            "True", "Rogue_doggy_ass"),
        (0,0), ConditionSwitch(
            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Rogue_doggy_feet2",
                    "action_speed ", "Rogue_doggy_feet1",
                    "True", "Rogue_doggy_feet0"),
            "not Player.sprite and show_feet", "Rogue_doggy_feet0",
            "True", Null()))

    align (0.6,0.0)

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
