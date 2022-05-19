layeredimage Kitty_sprite:
    if not renpy.showing("Kitty_blowjob_animation") and not renpy.showing("Kitty_TJ_Animation"):
        "Kitty_hairback" pos (124, 0)

    if KittyX.legs == "_dress" and KittyX.upskirt:
        "images/Kitty_sprite/Kitty_standing_legs[KittyX.legs]_back.png"

    if KittyX.ArmPose == 1:
        "images/Kitty_sprite/Kitty_standing_arms[KittyX.ArmPose].png"

    if KittyX.top == "_pink_top":
        "images/Kitty_sprite/Kitty_standing_top[KittyX.top][KittyX.ArmPose]_under.png"

    always:
        "images/Kitty_sprite/Kitty_standing_body[KittyX.pubes][KittyX.ArmPose].png"

    if not KittyX.piercings or (KittyX.underwear and not KittyX.underwear_pulled_down):
        Null()
    else:
        "images/Kitty_sprite/Kitty_standing_piercings_breasts[KittyX.piercings].png"

    if KittyX.hose:
        "images/Kitty_sprite/Kitty_standing_hose[KittyX.hose].png"

    if not KittyX.underwear_pulled_down:
        Null()
    elif KittyX.legs and KittyX.legs != "_blue_skirt" and not KittyX.upskirt:
        Null()
    elif KittyX.underwear_pulled_down and KittyX.grool > 1:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.underwear]_down_wet.png"
    elif KittyX.underwear_pulled_down:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.underwear]_down.png"
    elif KittyX.grool > 1:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.underwear]_wet.png"
    elif KittyX.underwear:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.underwear].png"

    if KittyX.underwear and KittyX.underwear_pulled_down:
        Null()
    elif KittyX.hose:
        "images/Kitty_sprite/Kitty_standing_hose[KittyX.hose].png"

    if not KittyX.grool:
        Null()
    elif KittyX.legs and not KittyX.upskirt:
        Null()
    elif KittyX.underwear and not KittyX.underwear_pulled_down and KittyX.grool < 2:
        Null()
    elif KittyX.grool == 1 and KittyX.underwear and KittyX.underwear_pulled_down:
        AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png") pos (225, 560)
    elif KittyX.grool == 1:
        AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (225, 560)
    elif KittyX.underwear and KittyX.underwear_pulled_down:
        AlphaMask("heavy_grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png") pos (225, 560)
    elif KittyX.underwear:
        AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (225, 560)
    else:
        AlphaMask("heavy_grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (225, 560)

    if KittyX.legs or not KittyX.grool:
        Null()
    elif KittyX.underwear and not KittyX.underwear_pulled_down and KittyX.grool < 2:
        Null()
    elif KittyX.underwear or KittyX.underwear_pulled_down == 1:
        "images/Kitty_sprite/Kitty_standing_grool.png"
    else:
        "images/Kitty_sprite/Kitty_standing_grool[KittyX.grool].png"

    if "sex" not in KittyX.spunk and "anal" not in KittyX.spunk:
        Null()
    elif KittyX.legs and not KittyX.upskirt:
        Null()
    elif KittyX.underwear and KittyX.underwear_pulled_down:
        AlphaMask("heavy_spunk_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png") pos (225, 560)
    else:
        AlphaMask("heavy_spunk_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (225, 560)

    if KittyX.upskirt and KittyX.legs in ["_blue_skirt", "_dress"]:
        "images/Kitty_sprite/Kitty_standing_legs[KittyX.legs]_up.png"
    elif not KittyX.legs or KittyX.upskirt:
        Null()
    elif KittyX.grool and KittyX.legs in ["_yoga_pants", "_shorts"]:
        "images/Kitty_sprite/Kitty_standing_legs[KittyX.legs]_wet.png"
    elif KittyX.legs:
        "images/Kitty_sprite/Kitty_standing_legs[KittyX.legs].png"

    if KittyX.ArmPose == 2:
        "images/Kitty_sprite/Kitty_standing_arms[KittyX.ArmPose].png"

    always:
        "images/Kitty_sprite/Kitty_standing_chest.png"

    if KittyX.piercings:
        "images/Kitty_sprite/Kitty_standing_piercings[KittyX.piercings]_breasts.png"

    if KittyX.neck:
        "images/Kitty_sprite/Kitty_standing_neck[KittyX.neck].png"

    if not KittyX.bra:
        Null()
    elif not KittyX.top_pulled_up and KittyX.ArmPose != 1 and KittyX.bra in ["_cami", "_bikini_top", "_dress"]:
        "images/Kitty_sprite/Kitty_standing_bra[KittyX.bra][KittyX.ArmPose].png"
    elif not KittyX.top_pulled_up:
        "images/Kitty_sprite/Kitty_standing_bra[KittyX.bra][KittyX.ArmPose].png"
    elif KittyX.top and KittyX.top != "_towel":
        "images/Kitty_sprite/Kitty_standing_bra[KittyX.bra][KittyX.ArmPose].png"
    elif KittyX.bra:
        "images/Kitty_sprite/Kitty_standing_bra[KittyX.bra][KittyX.ArmPose]_up.png"

    if not KittyX.piercings or not KittyX.bra or KittyX.top_pulled_up:
        Null()
    elif KittyX.legs:
        "images/Kitty_sprite/Kitty_standing_piercings[KittyX.piercings]_top.png"
    else:
        "images/Kitty_sprite/Kitty_standing_piercings[KittyX.piercings].png"

    if KittyX.Water:
        "images/Kitty_sprite/Kitty_standing_wet[KittyX.ArmPose].png"

    if not KittyX.top:
        Null()
    elif KittyX.top_pulled_up:
        "images/Kitty_sprite/Kitty_standing_top[KittyX.top][KittyX.ArmPose]_up.png"
    else:
        "images/Kitty_sprite/Kitty_standing_top[KittyX.top][KittyX.ArmPose].png"

    if not KittyX.top or not KittyX.bra or not KittyX.top_pulled_up:
        Null()
    elif KittyX.bra:
        "images/Kitty_sprite/Kitty_standing_bra[KittyX.bra].png"

    if not renpy.showing("Kitty_blowjob_animation"):
        "Kitty_head" pos (124, 0)

    if KittyX.legs and not KittyX.upskirt:
        Null()
    elif KittyX.underwear and not KittyX.underwear_pulled_down:
        Null()
    elif "anal" in KittyX.spunk:
        "images/Kitty_sprite/Kitty_standing_anal_spunk.png"

    if KittyX.legs and not KittyX.upskirt:
        Null()
    elif KittyX.underwear and not KittyX.underwear_pulled_down:
        Null()
    elif "sex" in KittyX.spunk:
        "images/Kitty_sprite/Kitty_standing_pussy_spunk.png"

    if "belly" in KittyX.spunk:
        "images/Kitty_sprite/Kitty_standing_belly_spunk.png"

    if "tits" in KittyX.spunk:
        "images/Kitty_sprite/Kitty_standing_breasts_spunk.png"

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
    elif second_girl_priamry_action == "fondle_breasts":
        "GirlGropeRightBreast_Kitty"
    elif second_girl_primary_action == "suck_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast_Kitty"
    elif second_girl_primary_action == "suck_breasts" and (offhand_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast_Kitty"
    elif second_girl_priamry_action == "suck_breasts":
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

    size (480, 960) pos (500, 100) anchor (0.6, 0.0) zoom 0.75

layeredimage Kitty_hairback:
    if KittyX.hair != "_evo":
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.hair]_back.png"

    size (416, 610) zoom 0.5

layeredimage Kitty_head:
    if (not action_speed or not renpy.showing("Kitty_blowjob_animation")) and RogueX.Water:
        "images/Kitty_sprite/Kitty_standing_face[KittyX.hair][KittyX.blushing]_wet.png"
    elif not action_speed or not renpy.showing("Kitty_blowjob_animation"):
        "images/Kitty_sprite/Kitty_standing_face[KittyX.hair][KittyX.blushing].png"
    elif RogueX.Water:
        "images/Kitty_sprite/Kitty_face_blowjob[KittyX.blushing]_wet.png"
    else:
        "images/Kitty_sprite/Kitty_face_blowjob[KittyX.blushing].png"

    always:
        "images/Kitty_sprite/Kitty_standing_brows[KittyX.brows].png"

    always:
        "images/Kitty_sprite/Kitty_standing_mouth[KittyX.mouth].png"

    if "mouth" not in KittyX.spunk:
        Null()
    else:
        "images/Kitty_sprite/Kitty_spunk_standing[KittyX.mouth].png"

    if "facial" in KittyX.spunk:
        "images/Kitty_sprite/Kitty_standing_face_spunk.png"

    always:
        "Kitty_blinking"

    if KittyX.Water:
        "images/Kitty_sprite/Kitty_standing_hair_wet.png"
    else:
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.hair].png"

    if KittyX.Water:
        "images/Kitty_sprite/Kitty_standing_head_wet.png"

    if KittyX.hair in ["_evo", "_long"] and "hair" in KittyX.spunk:
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.hair]_spunk.png"

    size (416, 610) zoom 0.5

image Kitty_eyes:
    contains:
        "images/Kitty_sprite/Kitty_standing_eyes[KittyX.eyes].png"
