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

image Kitty_squinting:
    "images/Kitty_standing/Kitty_standing_eyes_sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_standing/Kitty_standing_eyes_squint.png"
    0.25
    repeat

layeredimage Kitty_standing_fondling:
    if primary_action == "lesbian" or not girl_offhand_action or focused_Girl != KittyX:
        Null()
    elif primary_action != "sex" and girl_offhand_action == "fondle_pussy" and KittyX.lust >= 70:
        "GirlFingerPussy_Kitty"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy_Kitty"
    elif girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "GirlGropeLeftBreast_Kitty"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast_Kitty"

    if second_girl_primary_action != "masturbation" or not second_girl_offhand_action or focused_Girl == KittyX:
        Null()
    elif primary_action != "sex" and second_girl_offhand_action == "fondle_pussy" and KittyX.lust >= 70:
        "GirlFingerPussy_Kitty_Kitty"
    elif second_girl_offhand_action == "fondle_pussy":
        "GirlGropePussy_Kitty"
    elif second_girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "GirlGropeLeftBreast_Kitty"
    elif second_girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast_Kitty"

    if not primary_action or focused_Girl != KittyX:
        Null()
    elif primary_action == "fondle_thighs":
        "GropeThigh_Kitty"
    elif primary_action == "fondle_breasts":
        "GropeRightBreast_Kitty"
    elif primary_action == "suck_breasts":
        "LickRightBreast_Kitty"
    elif primary_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy_Kitty"
    elif primary_action == "fondle_pussy":
        "GropePussy_Kitty"
    elif primary_action == "eat_pussy":
        "Lickpussy_Kitty"

    if not offhand_action or focused_Girl != KittyX:
        Null()
    elif primary_action == "fondle_breasts" and not girl_offhand_action and not second_girl_primary_action and not second_girl_offhand_action:
        "GropeRightBreast_Kitty"
    elif offhand_action == "fondle_thighs":
        "GropeThigh_Kitty"
    elif offhand_action == "fondle_breasts":
        "GropeLeftBreast_Kitty"
    elif offhand_action == "suck_breasts":
        "LickLeftBreast_Kitty"
    elif offhand_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy_Kitty"
    elif offhand_action == "fondle_pussy":
        "GropePussy_Kitty"
    elif offhand_action == "eat_pussy":
        "Lickpussy_Kitty"

    if not second_girl_primary_action or focused_Girl != KittyX:
        Null()
    elif second_girl_primary_action == "fondle_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "GirlGropeLeftBreast_Kitty"
    elif second_girl_primary_action == "fondle_breasts":
        "GirlGropeRightBreast_Kitty"
    elif second_girl_primary_action == "suck_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast_Kitty"
    elif second_girl_primary_action == "suck_breasts" and (offhand_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast_Kitty"
    elif second_girl_primary_action == "suck_breasts":
        "LickRightBreast_Kitty"
    elif second_girl_primary_action == "fondle_pussy" and primary_action != "sex" and KittyX.lust >= 70:
        "GirlFingerPussy_Kitty"
    elif second_girl_primary_action == "fondle_pussy" and offhand_action != "sex" and KittyX.lust >= 70:
        "GirlFingerPussy_Kitty"
    elif second_girl_primary_action == "fondle_pussy":
        "GropePussy_Kitty"
    elif second_girl_primary_action == "eat_pussy":
        "Lickpussy_Kitty"

    if primary_action != "lesbian" or not girl_offhand_action or focused_Girl == KittyX:
        Null()
    elif girl_offhand_action == "fondle_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "GirlGropeLeftBreast_Kitty"
    elif girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck_breasts"]):
        "GirlGropeLeftBreast_Kitty"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast_Kitty"
    elif girl_offhand_action == "suck_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast_Kitty"
    elif girl_offhand_action == "suck_breasts" and (offhand_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast_Kitty"
    elif girl_offhand_action == "suck_breasts":
        "LickRightBreast_Kitty"
    elif girl_offhand_action == "fondle_pussy" and primary_action != "sex" and KittyX.lust >= 70:
        "GirlFingerPussy_Kitty"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy_Kitty"
    elif girl_offhand_action == "eat_pussy":
        "Lickpussy_Kitty"

image Kitty_sprite sex:
    LiveComposite(
        (1120, 840),
        (0, 0), ConditionSwitch(
            "not Player.sprite", "Kitty_sex_body_animation0",
            "Player.cock_position in ['in', 'anal']", "Kitty_sex_body_animation[action_speed]",
            "Player.cock_position == 'footjob'", "Kitty_sex_body_FootAnim[action_speed]",
            "Player.cock_position == 'out' and action_speed >= 2", "Kitty_Hotdog_Body_animation2",
            "True", "Kitty_sex_body_animation0"),
        (0, 0), ConditionSwitch(
            "not Player.sprite", "Kitty_sex_legs_animation0",
            "Player.cock_position in ['in', 'anal']", "Kitty_sex_legs_animation[action_speed]",
            "Player.cock_position == 'footjob'", "Kitty_sex_legs_FootAnim[action_speed]",
            "Player.cock_position == 'out' and action_speed >= 2", "Kitty_Hotdog_legs_animation2",
            "True", "Kitty_sex_legs_animation0"))

    align (0.5, 0.0) zoom 0.7
