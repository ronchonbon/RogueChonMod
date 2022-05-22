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
        AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png") pos (-0.03, 0)
    elif KittyX.grool == 1:
        AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (-0.03, 0)
    elif KittyX.underwear and KittyX.underwear_pulled_down:
        AlphaMask("heavy_grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png") pos (-0.03, 0)
    elif KittyX.underwear:
        AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (-0.03, 0)
    else:
        AlphaMask("heavy_grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (-0.03, 0)

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
        AlphaMask("heavy_spunk_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png") pos (-0.03, 0)
    else:
        AlphaMask("heavy_spunk_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png") pos (-0.03, 0)

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

    if KittyX.wet:
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

    size (480, 960) pos (500, 100) anchor (0.6, 0.0) zoom 0.75

layeredimage Kitty_hairback:
    if KittyX.hair != "_evo":
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.hair]_back.png"

    size (416, 610) zoom 0.5

layeredimage Kitty_head:
    if (not action_speed or not renpy.showing("Kitty_blowjob_animation")) and RogueX.wet:
        "images/Kitty_sprite/Kitty_standing_face[KittyX.hair][KittyX.blushing]_wet.png"
    elif not action_speed or not renpy.showing("Kitty_blowjob_animation"):
        "images/Kitty_sprite/Kitty_standing_face[KittyX.hair][KittyX.blushing].png"
    elif RogueX.wet:
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

    if KittyX.wet:
        "images/Kitty_sprite/Kitty_standing_hair_wet.png"
    else:
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.hair].png"

    if KittyX.wet:
        "images/Kitty_sprite/Kitty_standing_head_wet.png"

    if KittyX.hair in ["_evo", "_long"] and "hair" in KittyX.spunk:
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.hair]_spunk.png"

    size (416, 610) zoom 0.5

image Kitty_eyes:
    contains:
        "images/Kitty_sprite/Kitty_standing_eyes[KittyX.eyes].png"

layeredimage Kitty_sex_body:
    always:
        "Kitty_hairback" pos (0.49, -0.07) anchor (0.5, 0.5) rotate -10 zoom 1.5

    always:
        "images/Kitty_sex/Kitty_sex_body[KittyX.piercings].png"

    always:
        "Kitty_head" pos (0.49, -0.07) anchor (0.5, 0.5) rotate -10 zoom 1.5

    if KittyX.neck:
        "images/Kitty_sex/Kitty_sex_neck[KittyX.neck].png"

    if KittyX.legs:
        "images/Kitty_sex/Kitty_sex_legs_dress_waist.png"

    if not KittyX.bra:
        Null()
    elif KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_bra[KittyX.bra]_up.png"
    elif KittyX.top == "_red_shirt" and KittyX.bra == "_sports_bra":
        "images/Kitty_sex/Kitty_sex_bra[KittyX.bra][KittyX.bra]_top_up.png"
    elif KittyX.top and KittyX.bra != "_cami":
        "images/Kitty_sex/Kitty_sex_bra[KittyX.bra]_top.png"
    else:
        "images/Kitty_sex/Kitty_sex_bra[KittyX.bra].png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_body_wet.png"

    if not KittyX.top:
        Null()
    elif not KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_top[KittyX.top].png"
    elif KittyX.top == "_pink_top" and KittyX.bra == "_sports_bra":
        "images/Kitty_sex/Kitty_sex_top[KittyX.top][KittyX.bra].png"
    elif KittyX.top:
        "images/Kitty_sex/Kitty_sex_top[KittyX.top]_up.png"

    if KittyX.bra and KittyX.top and KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_bra[KittyX.bra]_up.png"

    if "belly" in KittyX.spunk:
        "images/Kitty_sex_Kitty_sex_spunk_belly_body.png"

    if "tits" in KittyX.spunk:
        "images/Kitty_sex/Kitty_sex_spunk_tits.png"

    if "suck_breasts" in [primary_action, offhand_action]:
        "Kitty_Sex_Lick_Breasts"

    if "fondle_breasts" in [primary_action, offhand_action]:
        "Kitty_Sex_Fondle_Breasts"

    size (1120, 840)

layeredimage Kitty_sex_legs:
    if KittyX.legs == "_dress" and KittyX.upskirt:
        "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_back_up.png"
    elif KittyX.legs in ["_dress", "_blue_skirt"]:
        "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_back.png"

    always:
        "images/Kitty_sex/Kitty_sex_legs.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_legs_wet.png"

    always:
        "Kitty_sex_anus"

    always:
        "Kitty_sex_pussy"

    if KittyX.underwear_pulled_down:
        Null()
    elif KittyX.underwear and KittyX.grool:
        "images/Kitty_sex/Kitty_sex_underwear[KittyX.underwear]_wet.png"
    elif KittyX.underwear:
        "images/Kitty_sex/Kitty_sex_underwear[KittyX.underwear].png"

    if KittyX.underwear and KittyX.underwear_pulled_down:
        Null()
    elif KittyX.hose:
        "images/Kitty_sex/Kitty_sex_hose[KittyX.hose].png"

    if KittyX.legs == "_dress" and KittyX.upskirt:
        "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_up.png"
    elif KittyX.legs in ["_dress", "_blue_skirt"]:
        "images/Kitty_sex/Kitty_sex_legs[KittyX.legs].png"
    elif KittyX.upskirt:
        Null()
    elif KittyX.legs and KittyX.grool == 2:
        "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_wet.png"
    elif KittyX.legs:
        "images/Kitty_sex/Kitty_sex_legs[KittyX.legs].png"

    if KittyX.top == "_towel" and not KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_top[KittyX.top]_legs.png"

    if "belly" in KittyX.spunk:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if not Player.sprite or Player.cock_position != "out":
        Null()
    else:
        "Kitty_Hotdog_Zero_Anim[action_speed]"

    if Player.sprite and Player.cock_position:
        Null()
    elif primary_action == "eat_pussy":
        "Kitty_Sex_Lick_Pussy"
    elif primary_action == "eat_ass":
        "Kitty_Sex_Lick_Ass"

    if not Player.sprite or Player.cock_position != "footjob":
        Null()
    else:
        "Kitty_Footcock_Zero_Anim[action_speed]"

    if not action_speed:
        "Kitty_sex_feet"
    elif Player.cock_position:
        AlphaMask("Kitty_sex_feet", "images/Kitty_sex/Kitty_sex_feet_mask.png")
    else:
        "Kitty_sex_feet"

    size (1120, 840)

layeredimage Kitty_sex_feet:
    always:
        "images/Kitty_sex/Kitty_sex_feet.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_feet_wet.png"

    if KittyX.legs and not KittyX.upskirt and KittyX.legs not in ["_blue_skirt", "_shorts"] and KittyX.hose:
        "images/Kitty_sex/Kitty_sex_hose[KittyX.hose]_feet_under.png"
    elif KittyX.hose:
        "images/Kitty_sex/Kitty_sex_hose[KittyX.hose]_feet.png"

    if not KittyX.upskirt:
        "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_feet.png"

    size (1120, 840)

layeredimage Kitty_sex_pussy:
    if Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    elif Player.sprite and Player.cock_position == "sex" and action_speed:
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    elif Player.sprite and Player.cock_position == "sex":
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"
    elif primary_action == "eat_pussy":
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"

    if not KittyX.grool:
        Null()
    elif Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_wet_fucking.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_wet.png"

    if not KittyX.piercings:
        Null()
    elif not Player.sprite or Player.cock_position != "sex" or action_speed <= 1:
        "images/Kitty_sex/Kitty_sex_piercings[KittyX.piercings]_pussy.png"
    else:
        "images/Kitty_sex/Kitty_sex_piercings[KittyX.piercings]_pussy_fucking.png"

    if not KittyX.pubes:
        Null()
    elif Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
    elif Player.sprite and Player.cock_position == "sex" and action_speed:
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    elif Player.sprite and Player.cock_position == "sex":
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"
    elif primary_action == "eat_pussy":
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"

    if "sex" in KittyX.spunk:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if KittyX.underwear and KittyX.underwear_pulled_down:
        Null()
    elif KittyX.hose == "_ripped_pantyhose":
        "images/Kitty_sex/Kitty_sex_hose[KittyX.hose].png"

    if not Player.sprite or Player.cock_position != "sex":
        Null()
    else:
        AlphaMask("Kitty_Sex_Zero_Anim[action_speed]", "Kitty_Pussy_Fucking_Mask")

    if "in" not in KittyX.spunk or not Player.sprite or Player.cock_position != "sex" or not action_speed:
        Null()
    elif action_speed == 1:
        "Kitty_Pussy_Spunk_Heading"
    else:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

layeredimage Kitty_sex_anus:
    if Player.sprite and Player.cock_position == "anal" and action_speed < 2:
        "Kitty_Sex_Anal[action_speed]"
    elif Player.sprite and Player.cock_position == "anal":
        "images/Kitty_sex/Kitty_sex_anus_open.png"
    elif KittyX.used_to_anal:
        "images/Kitty_sex/Kitty_sex_anus_loose.png"
    else:
        "images/Kitty_sex/Kitty_sex_anus_tight.png"

    if "anal" not in KittyX.spunk:
        Null()
    elif Player.sprite and Player.cock_position != "anal" and action_speed >= 1:
        "images/Kitty_sex/Kitty_sex_spunk_anal_under.png"
    elif Player.sprite and Player.cock_position != "anal" and action_speed:
        "Kitty_Sex_Anal_Spunk_Heading_Under"
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anal_closed.png"

    if not Player.sprite or Player.cock_position != "anal":
        Null()
    else:
        AlphaMask("Kitty_Anal_Zero_Anim[action_speed]", "Kitty_Sex_Anal_Fucking_Mask")

    if "anal" not in KittyX.spunk or not Player.sprite or Player.cock_position != "anal" or not action_speed:
        Null()
    elif action_speed == 1:
        "Kitty_Sex_Anal_Spunk_Heading_Over"
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anal_over.png"
