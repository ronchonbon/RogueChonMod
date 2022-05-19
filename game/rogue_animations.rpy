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

image Rogue_HJ_Animation:
    contains:
        ConditionSwitch(
            "not action_speed", "Rogue_handjob_under",
            "action_speed == 1", At("Rogue_handjob_under", Rogue_Hand_1()),
            "action_speed >= 2", At("Rogue_handjob_under", Rogue_Hand_2()),
            "action_speed ", Null()),

    contains:
        ConditionSwitch(
            "not action_speed", "Zero_cock_handjob",
            "action_speed == 1", At("Zero_cock_handjob", Handcock_1()),
            "action_speed >= 2", At("Zero_cock_handjob", Handcock_2()),
            "action_speed ", Null()),

    contains:
        ConditionSwitch(
            "not action_speed", "Rogue_handjob_over",
            "action_speed == 1", At("Rogue_handjob_over", Rogue_Hand_1()),
            "action_speed >= 2", At("Rogue_handjob_over", Rogue_Hand_2()),
            "action_speed ", Null()),

    anchor (0.5,0.5) offset (200,800) zoom 0.6

image Rogue_TJ_Animation:
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Rogue_titjob_under"),
            "action_speed == 1", At("Rogue_titjob_under", Rogue_titjob_under_1()),
            "action_speed >= 2", At("Rogue_titjob_under", Rogue_titjob_under_2()),
            "action_speed ", Null()),

    contains:
        ConditionSwitch(
            "not action_speed", At("Zero_cock_titjob", Zero_TJ_Cock()),
            "action_speed == 1", At("Zero_cock_titjob", Zero_TJ_Cock_1()),
            "action_speed >= 2", At("Zero_cock_titjob", Zero_TJ_Cock_2()),
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

image Rogue_blowjob_hairback:
    "Rogue_hairback"
    zoom 3.45

image Rogue_blowjob_body:
    "Rogue_sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)

image Rogue_blowjob_mask:
    "images/Rogue_blowjob/Rogue_facemask_blowjob.png"
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

image Rogue_blowjob_hairback_animation0:
    "Rogue_blowjob_hairback"
    blowjob_starting

image Rogue_blowjob_body_animation1:
    "Rogue_blowjob_body"
    blowjob_licking_body

image Rogue_blowjob_head_animation1:
    "Rogue_blowjob_head"
    blowjob_licking

image Rogue_blowjob_hairback_animation1:
    "Rogue_blowjob_hairback"
    blowjob_licking

image Rogue_blowjob_body_animation2:
    "Rogue_blowjob_body"
    blowjob_heading

image Rogue_blowjob_head_animation2:
    "Rogue_blowjob_head"
    blowjob_heading

image Rogue_blowjob_hairback_animation2:
    "Rogue_blowjob_hairback"
    blowjob_heading

image Rogue_blowjob_facemask_animation2:
    AlphaMask("Rogue_blowjob_head", "Rogue_blowjob_mask_heading")
    blowjob_heading

image Rogue_blowjob_body_animation3:
    "Rogue_blowjob_body"
    blowjob_sucking_body

image Rogue_blowjob_head_animation3:
    "Rogue_blowjob_head"
    blowjob_sucking

image Rogue_blowjob_hairback_animation3:
    "Rogue_blowjob_hairback"
    blowjob_sucking

image Rogue_blowjob_facemask_animation3:
    AlphaMask("Rogue_blowjob_head", "images/Rogue_blowjob/Rogue_facemask_blowjob.png")
    blowjob_sucking

image Rogue_blowjob_body_animation4:
    "Rogue_blowjob_body"
    blowjob_deepthroat_body

image Rogue_blowjob_head_animation4:
    "Rogue_blowjob_head"
    blowjob_deepthroat

image Rogue_blowjob_hairback_animation4:
    "Rogue_blowjob_hairback"
    blowjob_deepthroat

image Rogue_blowjob_facemask_animation4:
    AlphaMask("Rogue_blowjob_head", "images/Rogue_blowjob/Rogue_facemask_blowjob.png")
    blowjob_deepthroat

image Rogue_mouth_blowjob_sucking:
    "images/Rogue_blowjob/Rogue_mouth_blowjob_sucking.png"
    Rogue_blowjob_mouth_animation

image Rogue_mouth_blowjob_sucking_spunk:
    "images/Rogue_blowjob/Rogue_mouth_blowjob_sucking_spunk.png"
    Rogue_blowjob_mouth_animation

image Rogue_blowjob_animation:
    LiveComposite(
        (787, 913),
        (0, 0), "Rogue_blowjob_hairback_animation[action_speed]",
        (0, 0), "Rogue_blowjob_body_animation[action_speed]",
        (0, 0), "Rogue_blowjob_head_animation[action_speed]",
        (-0.224, 0.15), "Zero_blowjob_cock_animation[action_speed]",
        (0, 0), ConditionSwitch(
            "action_speed > 1", "Rogue_blowjob_facemask_animation[action_speed]",
            "True", Null()),
        )
    zoom 0.55
    anchor (0.5, 0.5)

image Rogue_sex_animation:
    LiveComposite(
        (1120,840),
        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_sex_body_Anim0",
            "Player.cock in ['sex', 'anal']", "Rogue_sex_body_Anim[action_speed]",
            "Player.cock == 'footjob'", "Rogue_sex_body_FootAnim[action_speed]",
            "Player.cock == 'out' and action_speed >= 2","Rogue_Hotdog_Body_Anim[action_speed]",
            "True", "Rogue_sex_body_Anim0"),
        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_sex_legs_Anim0",
            "Player.cock in ['sex', 'anal']", "Rogue_sex_legs_Anim[action_speed]",
            "Player.cock == 'footjob'", "Rogue_sex_legs_FootAnim[action_speed]",
            "Player.cock == 'out' and action_speed >= 2","Rogue_Hotdog_Legs_Anim[action_speed]",
            "True", "Rogue_sex_legs_Anim0"))

    align (0.6, 0.0)
    pos (650, 200)
    zoom 0.85

image Rogue_doggy_blinking:
    "Rogue_doggy_eyes"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_doggy/Rogue_eyes_doggy_squint.png"
    0.05
    "images/Rogue_doggy/Rogue_eyes_doggy_closed.png"
    0.15
    "images/Rogue_doggy/Rogue_eyes_doggy_squint.png"
    0.05
    repeat

image Rogue_doggy_animation:
    LiveComposite(
        (420,750),
        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_doggy_body",
            "Player.cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Top",
                    "action_speed ", "Rogue_Doggy_Anal_Head_Top",
                    "True", "Rogue_doggy_body"),
            "Player.cock == 'sex'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Top",
                    "True", "Rogue_doggy_body"),
            "True", "Rogue_doggy_body"),
        (0,0), ConditionSwitch(
            "not Player.sprite", "Rogue_doggy_ass",
            "Player.cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "action_speed ", "Rogue_Doggy_Anal_Head_Ass",
                    "True", "Rogue_doggy_ass"),
            "Player.cock == 'sex'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "True", "Rogue_doggy_ass"),
            "True", "Rogue_doggy_ass"),
        (0,0), ConditionSwitch(
            "Player.cock == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Rogue_doggy_feet2",
                    "action_speed ", "Rogue_doggy_feet1",
                    "True", "Rogue_doggy_feet0"),
            "not Player.sprite and ShowFeet", "Rogue_doggy_feet0",
            "True", Null()))

    align (0.6,0.0)

image doggy_licking_pussy:
    "licking"
    zoom 0.5
    offset (195, 540)

image doggy_licking_ass:
    "licking"
    zoom 0.5
    offset (195, 500)
