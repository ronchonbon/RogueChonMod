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

image Jean_squinting:
    "images/Jean_standing/Jean_standing_eyes_normal.png",
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Jean_standing/Jean_standing_eyes_sexy.png",
    0.25
    repeat

layeredimage Jean_standing_fondling_animations:
    if primary_action == "lesbian" or not girl_offhand_action or focused_Girl != JeanX:
            Null()
    elif primary_action != "sex" and girl_offhand_action == "fondle_pussy" and JeanX.lust >= 70:
        "GirlFingerPussy_Jean"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy_JeanSelf"
    elif girl_offhand_action == "fondle_breasts" and offhand_action in breast_actions:
        "GirlGropeLeftBreast_Jean"
    elif girl_offhand_action == "fondle_breasts" and primary_action in breast_action:
        "GirlGropeRightBreast_Jean"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeBothBreast_Jean"

    if second_girl_primary_action != "masturbation" or not second_girl_offhand_action or focused_Girl == JeanX:
        Null()
    elif primary_action != "sex" and second_girl_offhand_action == "fondle_pussy" and JeanX.lust >= 70:
        "GirlFingerPussy_Jean"
    elif second_girl_offhand_action == "fondle_pussy":
        "GirlGropePussy_Jean"
    elif second_girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "GirlGropeLeftBreast_Jean"
    elif second_girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast_Jean"

    if not primary_action or focused_Girl != JeanX:
        Null()
    elif primary_action == "fondle_thighs":
        "GropeThigh_Jean"
    elif primary_action == "fondle_breasts":
        "GropeRightBreast_Jean"
    elif primary_action == "suck_breasts":
        "LickRightBreast_Jean"
    elif primary_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy_Jean"
    elif primary_action == "fondle_pussy":
        "GropePussy_Jean"
    elif primary_action == "eat_pussy":
        "Lickpussy_Jean"

    if not offhand_action or focused_Girl != JeanX:
        Null()
    elif primary_action == "fondle_breasts" and not girl_offhand_action and not second_girl_primary_action and not second_girl_offhand_action:
        "GropeRightBreast_Jean"
    elif offhand_action == "fondle_thighs":
        "GropeThigh_Jean"
    elif offhand_action == "fondle_breasts":
        "GropeLeftBreast_Jean"
    elif offhand_action == "suck_breasts":
        "LickLeftBreast_Jean"
    elif offhand_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy_Jean"
    elif offhand_action == "fondle_pussy":
        "GropePussy_Jean"
    elif offhand_action == "eat_pussy":
        "Lickpussy_Jean"

    if not second_girl_primary_action or focused_Girl != JeanX:
        Null()
    elif second_girl_primary_action == "fondle_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "GirlGropeLeftBreast_Jean"
    elif second_girl_priamry_action == "fondle_breasts":
        "GirlGropeRightBreast_Jean"
    elif second_girl_primary_action == "suck_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast_Jean"
    elif second_girl_primary_action == "suck_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast_Jean"
    elif second_girl_priamry_action == "suck_breasts":
        "LickRightBreast_Jean"
    elif second_girl_primary_action == "fondle_pussy" and primary_action != "sex" and JeanX.lust >= 70:
        "GirlFingerPussy_Jean"
    elif second_girl_primary_action == "fondle_pussy" and offhand_action != "sex" and JeanX.lust >= 70:
        "GirlFingerPussy_Jean"
    elif second_girl_primary_action == "fondle_pussy":
        "GropePussy_Jean"
    elif second_girl_primary_action == "eat_pussy":
        "Lickpussy_Jean"

    if primary_action != "lesbian" or not girl_offhand_action or focused_Girl == JeanX:
        Null()
    elif girl_offhand_action == "fondle_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "GirlGropeLeftBreast_Jean"
    elif girl_offhand_action == "fondle_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "GirlGropeLeftBreast_Jean"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast_Jean"
    elif girl_offhand_action == "suck_breasts" and primary_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast_Jean"
    elif girl_offhand_action == "suck_breasts" and offhand_action in ["fondle_breasts", "suck_breasts"]:
        "LickLeftBreast_Jean"
    elif girl_offhand_action == "suck_breasts":
        "LickRightBreast_Jean"
    elif girl_offhand_action == "fondle_pussy" and primary_action != "sex" and JeanX.lust >= 70:
        "GirlFingerPussy_Jean"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy_Jean"
    elif girl_offhand_action == "eat_pussy":
        "Lickpussy_Jean"
