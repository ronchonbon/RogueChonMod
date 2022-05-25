layeredimage Rogue_sprite:
    if RogueX.outfit["back_outer_accessory"]:
        "images/Rogue_sprite/Rogue_standing_back_outer_accessory[RogueX.outfit[back_outer_accessory]].png"

    if RogueX.outfit["back_inner_accessory"]:
        "images/Rogue_sprite/Rogue_standing_back_inner_accessory[RogueX.outfit[back_inner_accessory]].png"

    if not renpy.showing("Rogue_blowjob_animation") and not renpy.showing("Rogue_TJ_Animation"):
        "Rogue_hair_back" pos (185, 38)

    always:
        "images/Rogue_sprite/Rogue_standing_body[RogueX.pubes][RogueX.outfit[front_inner_accessory]].png"

    always:
        "images/Rogue_sprite/Rogue_standing_arms[RogueX.arm_pose][RogueX.outfit[neck]][RogueX.outfit[gloves]].png"

    always:
        "images/Rogue_sprite/Rogue_standing_chest[RogueX.outfit[front_inner_accessory]].png"

    if not renpy.showing("Rogue_blowjob_animation") and not renpy.showing("Rogue_TJ_Animation"):
        "Rogue_head" pos (185, 38)

    if RogueX.outfit["front_inner_accessory"]:
        "images/Rogue_sprite/Rogue_standing_front_inner_accessory[RogueX.outfit[front_inner_accessory]].png"

    if not RogueX.outfit["bra"]:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue_sprite/Rogue_standing_bra[RogueX.outfit[bra]]_up.png"
    else:
        "images/Rogue_sprite/Rogue_standing_bra[RogueX.outfit[bra]].png"

    if not RogueX.outfit["underwear"]:
        Null()
    elif RogueX.underwear_pulled_down and RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]]_down_grool.png"
    elif RogueX.underwear_pulled_down:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]]_down.png"
    elif RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]]_grool.png"
    else:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]].png"

    if not RogueX.outfit["hose"]:
        Null()
    elif RogueX.grool and RogueX.outfit["hose"] == "_tights":
        "images/Rogue_sprite/Rogue_standing_hose[RogueX.outfit[hose]]_grool.png"
    else:
        "images/Rogue_sprite/Rogue_standing_hose[RogueX.outfit[hose]].png"

    if not RogueX.grool:
        Null()
    elif RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt:
        Null()
    elif RogueX.outfit["underwear"] and not RogueX.underwear_pulled_down and RogueX.grool < 2:
        Null()
    elif RogueX.grool == 1 and RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_underwear.png")
    elif RogueX.grool == 1 and RogueX.outfit["bottom"] == "_pants":
        AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    elif RogueX.grool == 1:
        AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")
    elif RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        AlphaMask("heavy_grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_underwear.png")
    elif RogueX.outfit["underwear"] and RogueX.outfit["bottom"] == "_pants":
        AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    elif RogueX.outfit["bottom"] == "_pants":
        AlphaMask("heavy_grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    elif RogueX.outfit["underwear"]:
        AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")
    else:
        AlphaMask("heavy_grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")

    if not RogueX.grool:
        Null()
    elif RogueX.outfit["bottom"] and RogueX.grool < 2:
        Null()
    elif RogueX.outfit["bottom"]:
        "images/Rogue_sprite/Rogue_standing_grool1.png"
    else:
        "images/Rogue_sprite/Rogue_standing_grool[RogueX.grool].png"

    if "sex" not in RogueX.spunk and "anal" not in RogueX.spunk:
        Null()
    elif RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt:
        Null()
    elif RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        AlphaMask("heavy_spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_underwear.png")
    elif RogueX.outfit["underwear"] and RogueX.outfit["bottom"] == "_pants":
        AlphaMask("spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    elif RogueX.outfit["bottom"] == "_pants":
        AlphaMask("heavy_spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    else:
        AlphaMask("heavy_spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")

    if not RogueX.outfit["bottom"]:
        Null()
    elif RogueX.upskirt:
        "images/Rogue_sprite/Rogue_standing_bottom[RogueX.outfit[bottom]]_up.png"
    else:
        "images/Rogue_sprite/Rogue_standing_bottom[RogueX.outfit[bottom]].png"

    # if RogueX.outfit["neck"]:
    #     "images/Rogue_sprite/Rogue_standing_neck[RogueX.outfit[neck]].png"

    if not RogueX.outfit["dress"]:
        Null()
    elif RogueX.top_pulled_up and RogueX.upskirt:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_both.png"
    elif RogueX.top_pulled_up:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_top.png"
    elif RogueX.upskirt:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_bottom.png"
    else:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose].png"

    if not RogueX.outfit["top"]:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue_sprite/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose]_up.png"
    else:
        "images/Rogue_sprite/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose].png"

    # if RogueX.outfit["gloves"]:
    #     "images/Rogue_sprite/Rogue_standing_gloves[RogueX.outfit[gloves]][RogueX.arm_pose].png"

    if RogueX.outfit["sleeves"]:
        "images/Rogue_sprite/Rogue_standing_sleeves[RogueX.outfit[sleeves]][RogueX.arm_pose].png"

    if RogueX.outfit["front_outer_accessory"]:
        "images/Rogue_sprite/Rogue_standing_front_outer_accessory[RogueX.outfit[front_outer_accessory]][RogueX.arm_pose].png"

    if RogueX.outfit["face_inner_accessory"]:
        "images/Rogue_sprite/Rogue_standing_face_inner_accessory[RogueX.outfit[face_inner_accessory]].png"

    # if not renpy.showing("Rogue_blowjob_animation") and not renpy.showing("Rogue_TJ_Animation"):
    #     "Rogue_hair" pos (185, 38)

    if RogueX.outfit["face_outer_accessory"]:
        "images/Rogue_sprite/Rogue_standing_face_outer_accessory[RogueX.outfit[face_outer_accessory]].png"

    if RogueX.wet and RogueX.wet < 3:
        "images/Rogue_sprite/Rogue_standing_water_body[RogueX.arm_pose].png"

    if RogueX.wet == 3:
        "images/Rogue_sprite/Rogue_standing_water_body3.png"

    if RogueX.spunk["hand"] and RogueX.arm_pose == 2:
        "images/Rogue_sprite/Rogue_standing_spunk_hand.png"

    if RogueX.spunk["belly"]:
        "images/Rogue_sprite/Rogue_standing_spunk_belly.png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_sprite/Rogue_standing_spunk_breasts.png"

    if RogueX.held_item and RogueX.arm_pose == 2:
        "images/Rogue_sprite/Rogue_standing_held[RogueX.held_item].png"

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

    size (480, 960) anchor (0.6, 0.0) zoom 0.75

image Rogue_hair_back:
    contains:
        "images/Rogue_blowjob/Rogue_blowjob_back_hair[RogueX.outfit[back_hair]].png"

    size (787, 913) zoom 0.29

layeredimage Rogue_head:
    if not action_speed or not renpy.showing("Rogue_blowjob_animation"):
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing].png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing]_sucking.png"

    if RogueX.blushing:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows]_blush.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows].png"

    if renpy.showing("Rogue_blowjob_animation") and action_speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed >= 3:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed:
        Null()
    elif RogueX.mouth not in ["_smirk", "_grimace"]:
        "images/Rogue_blowjob/Rogue_blowjob_mouth[RogueX.mouth].png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_smile.png"

    if not RogueX.spunk["mouth"]:
        Null()
    elif renpy.showing("Rogue_blowjob_animation") and action_speed == 2:
        Null()
    elif renpy.showing("Rogue_blowjob_animation") and action_speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_tongue.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_sucking.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_spunk[RogueX.mouth].png"

    if renpy.showing("Rogue_blowjob_animation") and action_speed == 2 and "mouth" in RogueX.spunk:
        "Rogue_blowjob_mouth_sucking_spunk" anchor (0.4, 0.65) pos (316, 590)
    elif renpy.showing("Rogue_blowjob_animation") and action_speed == 2:
        "Rogue_blowjob_mouth_sucking" anchor (0.4, 0.65) pos (316, 590)

    if RogueX.eyes not in ["_closed", "_squint"]:
        "Rogue_blinking"
    elif RogueX.eyes == "_squint":
        "Rogue_squinting"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"

    if RogueX.spunk["chin"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_chin.png"

    if primary_action == "blowjob" and RogueX.spunk["mouth"] and action_speed >= 3:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face_sucking_over.png"

    always:
        "images/Rogue_blowjob/Rogue_blowjob_hair[RogueX.outfit[hair]].png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_water_face.png"

    if RogueX.spunk["hair"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_hair.png"
    elif RogueX.spunk["face"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face.png"

    size (787, 913) zoom 0.29

image Rogue_eyes:
    contains:
        "images/Rogue_blowjob/Rogue_blowjob_eyes[RogueX.eyes].png"

layeredimage Rogue_sex_body:
    always:
        "Rogue_hair_back_Sex" pos (0.48, 0.1)

    always:
        "images/Rogue_sex/Rogue_sex_body[RogueX.outfit[front_inner_accessory]].png"

    if not RogueX.outfit["bra"]:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue_sex/Rogue_sex_bra[RogueX.outfit[bra]]_up.png"
    else:
        "images/Rogue_sex/Rogue_sex_bra[RogueX.outfit[bra]].png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_body.png"

    if not RogueX.outfit["top"]:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue_sex/Rogue_sex_top[RogueX.outfit[top]]_up.png"
    else:
        "images/Rogue_sex/Rogue_sex_top[RogueX.outfit[top]].png"

    if RogueX.top_pulled_up or (not RogueX.outfit["top"] and not RogueX.outfit["bra"]):
        Null()
    elif RogueX.piercings:
        "images/Rogue_sex/Rogue_sex_piercings[RogueX.outfit[front_inner_accessory]]_breasts.png"

    if RogueX.outfit["neck"] == "_spiked_collar":
        "images/Rogue_sex/Rogue_sex_neck_spiked_collar.png"

    if "belly" in RogueX.spunk:
        "images/Kitty_sex/Kitty_sex_spunk_belly.png"

    if "tits" in RogueX.spunk:
        "images/Kitty_sex/Kitty_sex_spunk_breasts.png"

    if "suck_breasts" in [primary_action, offhand_action]:
        "Rogue_sex_Lick_Breasts"

    if "fondle_breasts" in [primary_action, offhand_action]:
        "Rogue_sex_Fondle_Breasts"

    always:
        "Rogue_head_Sex" pos (0.48, 0.1)

    size (1120, 840) offset (50, 50) zoom 0.9

layeredimage Rogue_sex_legs:
    always:
        "images/Rogue_sex/Rogue_sex_legs.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_legs.png"

    always:
        "Rogue_sex_anus"

    always:
        "Rogue_sex_pussy"

    if not RogueX.outfit["underwear"] or RogueX.underwear_pulled_down:
        Null()
    elif Player.sprite and Player.cock_position in ["sex", "anal"]:
        Null()
    elif RogueX.grool and RogueX.outfit["underwear"] not in ["_lace_panties", "_harness"]:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]]_grool.png"
    else:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]].png"

    if RogueX.underwear_pulled_down:
        Null()
    elif RogueX.sprite and Player.cock_position in ["sex", "anal"]:
        Null()
    elif RogueX.outfit["hose"] == "_tights" and RogueX.grool:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]]_grool.png"
    elif RogueX.outfit["hose"]:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]].png"

    if RogueX.upskirt:
        Null()
    elif RogueX.outfit["bottom"] == "_pants" and RogueX.grool:
        "images/Rogue_sex/Rogue_sex_legs[RogueX.outfit[legs]]_grool.png"
    elif RougeX.outfit["bottom"]:
        "images/Rogue_sex/Rogue_sex_legs[RogueX.outfit[legs]].png"

    if RogueX.outfit["front_outer_accessory"] == "_sweater":
        "images/Rogue_sex/Rogue_sex_accessory_sweater.png"

    if "belly" in RogueX.spunk:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if not Player.sprite or Player.cock_position != "out":
        Null()
    else:
        "Rogue_Hotdog_Zero_Anim[action_speed]"

    if primary_action == "eat_pussy":
        "Rogue_sex_Lick_Pussy"
    elif primary_action == "eat_ass":
        "Rogue_sex_Lick_Ass"

    if not Player.sprite or Player.cock_position != "footjob":
        Null()
    else:
        "Rogue_Footcock_Zero_Anim[animation_speed]"

    if not action_speed or Player.cock_position == "footjob" or show_feet:
        "Rogue_sex_feet"
    else:
        AlphaMask("Rogue_sex_feet","images/Rogue_sex/Rogue_sex_feet_mask.png")

    size (1120, 840)

layeredimage Rogue_sex_feet:
    always:
        "images/Rogue_sex/Rogue_sex_feet.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_feet.png"

    if not RogueX.outfit["hose"] or RogueX.underwear_pulled_down or RogueX.outfit["hose"] == "_garterbelt":
        Null()
    elif Player.sprite and Playercock in ["sex", "anal"]:
        Null()
    else:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]]_feet.png"

    if not RogueX.outfit["underwear"] or not RogueX.underwear_pulled_down:
        Null()
    elif RogueX.outfit["bottom"] == "pants":
        Null()
    else:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]]_down.png"

    if RogueX.outfit["bottom"] == "pants" and RogueX.upskirt:
        "images/Rogue_sex/Rogue_sex_legs[RogueX.outfit[legs]].png"
    elif RogueX.outfit["bottom"] == "pants":
        "images/Rogue_sex/Rogue_sex_legs[RogueX.outfit[legs]]_feet.png"

    size (1120, 840)

layeredimage Rogue_sex_pussy:
    if Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif Player.sprite and Player.cock_position == "sex" and action_speed:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    elif Player.sprite and Player.cock_position == "sex":
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"
    elif primary_action == "dildo_pussy":
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif primary_action in ["fondle_pussy", "eat_pussy"] or offhand_action == "fondle_pussy":
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"

    if not RogueX.grool:
        Null()
    elif Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_grool_fucking.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_grool.png"

    if not RogueX.piercings:
        Null()
    elif Player.sprite or Player.cock_position != "sex" or action_speed <= 1:
        "images/Rogue_sex/Rogue_sex_piercings[RogueX.outfit[front_inner_accessory]].png"
    else:
        "images/Rogue_sex/Rogue_sex_piercings[RogueX.outfit[front_inner_accessory]]_fucking.png"

    if not RogueX.pubes:
        Null()
    elif Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif Player.sprite and Player.cock_position == "sex" and action_speed:
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    elif Player.sprite and Player.cock_position == "sex":
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"
    elif primary_action == "dildo_pussy":
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif primary_action in ["fondle_pussy", "eat_pussy"] or offhand_action == "fondle_pussy":
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"

    if "in" in RogueX.spunk:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
        AlphaMask("Rogue_sex_Zero_Anim[action_speed]", "Rogue_Pussy_Fucking_Mask")
    elif Player.sprite and Player.cock_position == "sex":
        AlphaMask("Rogue_sex_Zero_Anim[action_speed]", "Rogue_Pussy_Open_Mask")
    elif primary_action == "dildo_pussy":
        AlphaMask("Rogue_sex_Dildo_Anim2", "Rogue_Pussy_Fucking_Mask")
    elif primary_action == "fondle_pussy" or offhand_action == "fondle_pussy":
        AlphaMask("Rogue_sex_FingerP_Anim1", "Rogue_Pussy_Open_Mask")

    if "in" not in RogueX.spunk or not Player.sprite or Player.cock_position != "sex" or not action_speed:
        Null()
    elif action_speed <= 1:
        "Rogue_sex_pussy_Spunk_Heading"
    else:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

layeredimage Rogue_sex_anus:
    if Player.sprite and Player.cock_position == "anal" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_anus_open.png"
    elif Player.sprite and Player.cock_position == "anal" and action_speed:
        "Rogue_sex_Anal_Heading"
    elif Player.sprite and Player.cock_position == "anal":
        "Rogue_sex_Anal_Tip"
    elif "finger_ass" in [primary_action, offhand_action]:
        "Rogue_sex_Anal_Tip"
    elif primary_action == "dildo_anal":
        "images/Kitty_sex/Kitty_sex_anus_open.png"
    elif RogueX.used_to_anal:
        "images/Rogue_sex/Rogue_sex_anus_loose.png"
    else:
        "images/Rogue_sex/Rogue_sex_anus_tight.png"

    if "anal" not in RogueX.spunk:
        Null()
    elif Player.sprite and Player.cock_position != "anal" and action_speed > 1:
        "images/Kitty_sex/Kitty_sex_spunk_anus_under.png"
    elif Player.sprite and Player.cock_position != "anal" and action_speed == 1:
        "Rogue_Anal_Spunk_Heading_Under"
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anus_closed.png"

    if "finger_ass" in [primary_action, offhand_action]:
        AlphaMask("Rogue_sex_FingerA_Anim1", "Rogue_Anal_Fucking_Mask")
    elif primary_action == "dildo_anal":
        AlphaMask("Rogue_Anal_Dildo_Anim2", "Rogue_Anal_Fucking_Mask")
    elif not Player.sprite or Player.cock_position != "anal":
        Null()
    else:
        AlphaMask("Rogue_Anal_Zero_Anim[action_speed]", "Rogue_Anal_Fucking_Mask")

layeredimage Rogue_doggy_body:
    if not RogueX.wet and RogueX.outfit["hair"] == "_evo":
        "images/Rogue_doggy/Rogue_doggy_hair_evo_back.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_body.png"

    if RogueX.outfit["neck"] == "_spiked_collar":
        "images/Rogue_doggy/Rogue_doggy_neck_spiked_collar.png"

    if "mouth" in RogueX.spunk:
        "images/Rogue_doggy/Rogue_doggy_spunk_mouth[RogueX.mouth].png"
    elif RogueX.mouth not in ["_smirk", "_kiss"]:
        "images/Rogue_doggy/Rogue_doggy_mouth[RogueX.mouth].png"
    elif RogueX.mouth == "_kiss":
        "images/Rogue_doggy/Rogue_doggy_mouth_surprised.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_mouth_smile.png"

    if RogueX.blushing:
        "images/Rogue_doggy/Rogue_doggy_blush.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_brows[RogueX.brows].png"

    if RogueX.eyes != "_closed":
        "Rogue_doggy_blinking"
    else:
        "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"

    if RogueX.outfit["bra"]:
        "images/Rogue_doggy/Rogue_doggy_bra[RogueX.outfit[bra]].png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_water_top.png"

    if RogueX.outfit["top"] and RogueX.outfit["top"] not in ["_nighty", "_towel"]:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]].png"
    elif RogueX.outfit["top"]:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]]_top.png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_hair_wet.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_hair[RogueX.outfit[hair]].png"

    if RogueX.outfit["top"] == "hoodie":
        "images/Rogue_doggy/Rogue_doggy_top_hood.png"

    if "hair" in RogueX.spunk:
        "images/Rogue_doggy/Rogue_doggy_spunk_hair.png"

    if "facial" in RogueX.spunk:
        "images/Rogue_doggy/Rogue_doggy_spunk_face.png"

    if primary_action == "fondle_breasts" or offhand_action == "fondle_breasts":
        "Rogue_Doggy_GropeBreast"

    size (420, 750)

layeredimage Rogue_doggy_eyes:
    if RogueX.eyes != "_squint":
        "images/Rogue_doggy/Rogue_doggy_eyes[RogueX.eyes].png"
    else:
        "images/Rogue_doggy/Rogue_doggy_eyes_sexy.png"

layeredimage Rogue_doggy_ass:
    if not RogueX.underwear_pulled_down or (RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt):
        Null()
    elif RogueX.outfit["underwear"] and RogueX.outfit["underwear"] != "_harness":
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]]_back.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_ass.png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_water_ass.png"

    if RogueX.outfit["hose"] == "_stockings":
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]].png"

    if not RogueX.underwear_pulled_down or (RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt):
        Null()
    elif not RogueX.outfit["underwear"]:
        Null()
    elif RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_lace_panties", "_bikini_bottoms", "_harness"]:
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]]_down_grool.png"
    elif RogueX.outfit["underwear"]:
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]]_down.png"

    if not RogueX.pubes:
        Null()
    elif RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    elif RogueX.outfit["underwear"]:
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    elif RogueX.outfit["hose"] and RogueX.outfit["hose"] != "_stockings":
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_pubes.png"

    if Player.sprite and Player.cock_position == "sex" and action_speed > 2:
        "Rogue_Pussy_Fucking3"
    elif (Player.sprite and Player.cock_position == "sex" and action_speed > 1) or primary_action == "dildo_pussy":
        "Rogue_Pussy_Fucking2"
    elif Player.sprite and Player.cock_position == "sex" and action_speed:
        "Rogue_Pussy_Heading"
    elif Player.sprite and Player.cock_position == "sex":
        "Rogue_Pussy_Static"
    elif primary_action == "eat_pussy":
        "images/Rogue_doggy/Rogue_doggy_pussy_open.png"
    elif primary_action == "fondle_pussy" or offhand_action == "fondle_pussy":
        "images/Rogue_doggy/Rogue_doggy_pussy_closed.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_pussy_closed.png"

    if RogueX.piercings:
        "images/Rogue_doggy/Rogue_doggy_piercings_pussy[RogueX.outfit[front_inner_accessory]].png"

    if Player.sprite and Player.cock_position == "anal" and action_speed > 2:
        "Rogue_Anal_Fucking2"
    elif (Player.sprite and Player.cock_position == "anal" and action_speed > 1) or primary_action == "dildo_ass":
        "Rogue_Anal_Fucking"
    elif Player.sprite and Player.cock_position == "anal" and action_speed:
        "Rogue_Anal_Heading"
    elif Player.sprite and Player.cock_position == "anal":
        "Rogue_Anal"
    elif RogueX.outfit["underwear"] and not RogueX.underwear_pulled_down:
        "images/Rogue_doggy/Rogue_doggy_anus_loose.png"
    elif primary_action == "finger_ass" or offhand_action == "finger_ass":
        "Rogue_Anal_Fingering"
    elif primary_action == "dildo_anal":
        "Rogue_Anal_Fucking"
    elif RogueX.used_to_anal:
        "images/Rogue_doggy/Rogue_doggy_anus_loose.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_anus_tight.png"

    if "anal" not in RogueX.spunk:
        Null()
    elif Player.cock_position == "anal":
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_loose.png"

    if RogueX.underwear_pulled_down or not RogueX.outfit["underwear"]:
        Null()
    elif Player.sprite and Player.cock_position in ["sex", "anal"]:
        Null()
    else:
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]].png"

    if Player.sprite and Player.cock_position in ["sex", "anal"]:
        Null()
    elif RogueX.outfit["hose"] in ["_garter_belt", "_stockings_and_garterbelt"]:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]].png"
    elif RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        Null()
    elif RogueX.outfit["hose"] == "_tights" and RogueX.grool:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]]_grool.png"
    elif RogueX.outfit["hose"]:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]].png"

    if RogueX.outfit["bottom"] == "_pants" and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_legs_pants_down.png"
    elif RogueX.outfit["bottom"] == "_pants" and RogueX.grool > 1:
        "images/Rogue_doggy/Rogue_doggy_legs_pants_grool.png"
    elif RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_doggy/Rogue_doggy_legs_pants.png"
    elif RogueX.outfit["bottom"] == "_skirt" and RogueX.upskirt and Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Rogue_doggy/Rogue_doggy_legs_skirt_anal_up.png"
    elif RogueX.outfit["bottom"] == "_skirt" and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_legs_skirt_up.png"
    elif RogueX.outfit["bottom"] == "_skirt":
        "images/Rogue_doggy/Rogue_doggy_legs_skirt.png"

    if RogueX.outfit["top"] in ["_nighty", "_towel"] and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]]_ass_up.png"
    elif RogueX.outfit["top"] in ["_nighty", "_towel"]:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]]_ass.png"

    if RogueX.outfit["front_outer_accessory"] == "_sweater" and (RogueX.upskirt or (Player.sprite and Player.cock_position == "out")):
        "images/Rogue_doggy/Rogue_doggy_accessory_sweater_up.png"
    elif RogueX.outfit["front_outer_accessory"] == "_sweater":
        "images/Rogue_doggy/Rogue_doggy_accessory_sweater.png"

    if "back" in RogueX.spunk:
        "images/Rogue_doggy/Rogue_doggy_spunk_ass.png"

    if primary_action == "eat_pussy":
        "doggy_licking_pussy"
    elif primary_action == "eat_ass":
        "doggy_licking_ass"

    if not Player.sprite or Player.cock_position != "out":
        Null()
    elif RogueX.outfit["bottom"] == "_skirt" and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_hotdog_back_up.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_hotdog_back.png"

    if not Player.sprite or Player.cock_position != "out":
        Null()
    elif RogueX.outfit["bottom"] == "_skirt" and RogueX.upskirt and action_speed:
        AlphaMask("Zero_hotdog_moving", "images/Rogue_doggy/Rogue_doggy_hotdog_mask_up.png")
    elif RogueX.outfit["bottom"] == "_skirt" and RogueX.upskirt:
        AlphaMask("Zero_hotdog_static", "images/Rogue_doggy/Rogue_doggy_hotdog_mask_up.png")
    elif action_speed:
        AlphaMask("Zero_hotdog_moving", "images/Rogue_doggy/Rogue_doggy_hotdog_mask.png")
    else:
        AlphaMask("Zero_hotdog_static", "images/Rogue_doggy/Rogue_doggy_hotdog_mask.png")

    size (420, 750)

layeredimage Rogue_doggy_shins:
    always:
        "images/Rogue_doggy/Rogue_doggy_shins.png"

    if RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_doggy/Rogue_doggy[RogueX.outfit[legs]]_feet.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_feet.png"

    if not RogueX.outfit["hose"]:
        Null()
    else:
        "images/Rogue_doggy/Rogue_doggy[RogueX.outfit[hose]]_feet.png"

image Rogue_doggy_feet:
    contains:
        AlphaMask("Rogue_doggy_shins", "images/Rogue_doggy/Rogue_doggy_toes.png")
