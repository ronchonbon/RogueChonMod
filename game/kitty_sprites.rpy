layeredimage Kitty_sprite:
    if KittyX.outfit["back_outer_accessory"]:
        "images/Kitty_sprite/Kitty_standing_back_outer_accessory[KittyX.outfit[back_outer_accessory]].png"

    if KittyX.outfit["back_inner_accessory"]:
        "images/Kitty_sprite/Kitty_standing_back_inner_accessory[KittyX.outfit[back_inner_accessory]].png"

    if KittyX.outfit["dress"]:
        "images/Kitty_sprite/Kitty_standing_back_dress[KittyX.outfit[dress]].png"

    # if KittyX.outfit["underwear"]:
    #     "images/Kitty_sprite/Kitty_standing_back_underwear[KittyX.outfit[underwear]].png"

    always:
        "Kitty_back_hair" pos (0.12, 0.152) zoom 0.5

    always:
        "images/Kitty_sprite/Kitty_standing_arms[KittyX.arm_pose][KittyX.outfit[gloves]].png"

    always:
        "images/Kitty_sprite/Kitty_standing_body[KittyX.pubes][KittyX.arm_pose].png"

    always:
        "images/Kitty_sprite/Kitty_standing_breasts.png"

    always:
        "Kitty_head" pos (0.12, 0.152) zoom 0.5

    if KittyX.outfit["piercings"]:
        "images/Kitty_sprite/Kitty_standing_piercings_breasts[KittyX.outfit[piercings]].png"

    if KittyX.outfit["piercings"]:
        "images/Kitty_sprite/Kitty_standing_piercings_pussy[KittyX.outfit[piercings]].png"

    # if KittyX.outfit["clamps"]:
    #     "images/Kitty_sprite/Kitty_standing_clamps[KittyX.outfit[clamps]].png"

    # if KittyX.outfit["buttplug"]:
    #     "images/Kitty_sprite/Kitty_standing_buttplug[KittyX.outfit[buttplug]].png"

    # if KittyX.outfit["rope"]:
    #     "images/Kitty_sprite/Kitty_standing_rope[KittyX.outfit[rope]].png"

    if KittyX.outfit["bra"] and KittyX.top_pulled_up:
        "images/Kitty_sprite/Kitty_standing_bra[KittyX.outfit[bra]][KittyX.arm_pose]_up.png"
    elif KittyX.outfit["bra"]:
        "images/Kitty_sprite/Kitty_standing_bra[KittyX.outfit[bra]][KittyX.arm_pose].png"

    if KittyX.outfit["underwear"] and KittyX.underwear_pulled_down and KittyX.grool > 1:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.outfit[underwear]]_down_grool.png"
    elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.outfit[underwear]]_down.png"
    elif KittyX.outfit["underwear"] and KittyX.grool > 1:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.outfit[underwear]]_grool.png"
    elif KittyX.outfit["underwear"]:
        "images/Kitty_sprite/Kitty_standing_underwear[KittyX.outfit[underwear]].png"

    if KittyX.outfit["hose"]:
        "images/Kitty_sprite/Kitty_standing_hose[KittyX.outfit[hose]].png"

    if KittyX.grool and KittyX.outfit["bottom"] and KittyX.grool < 2:
        Null()
    elif KittyX.grool and KittyX.outfit["bottom"]:
        "images/Kitty_sprite/Kitty_standing_grool1.png"
    elif KittyX.grool:
        "images/Kitty_sprite/Kitty_standing_grool[KittyX.grool].png"

    # always:
    #     "grool_dripping_animations"
    # if not KittyX.grool:
    #     Null()
    # elif KittyX.outfit["bottom"] and not KittyX.upskirt:
    #     Null()
    # elif KittyX.outfit["underwear"] and not KittyX.underwear_pulled_down and KittyX.grool < 2:
    #     Null()
    # elif KittyX.grool == 1 and KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
    #     AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png")
    # elif KittyX.grool == 1:
    #     AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png")
    # elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
    #     AlphaMask("heavy_grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png")
    # elif KittyX.outfit["underwear"]:
    #     AlphaMask("grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png")
    # else:
    #     AlphaMask("heavy_grool_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png")

    # always:
    #     "spunk_dripping_animations"
    # if not KittyX.spunk["pussy"] and not KittyX.spunk["anus"]:
    #     Null()
    # elif KittyX.outfit["bottom"] not in ["_yoga", "_black_jeans", "_capris"] and not KittyX.upskirt:
    #     Null()
    # elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
    #     AlphaMask("heavy_spunk_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask_underwear.png")
    # else:
    #     AlphaMask("heavy_spunk_dripping", "images/Kitty_sprite/Kitty_standing_grool_mask.png")

    if KittyX.outfit["bottom"] and KittyX.upskirt:
        "images/Kitty_sprite/Kitty_standing_bottom[KittyX.outfit[bottom]]_up.png"
    elif KittyX.outfit["bottom"]:
        "images/Kitty_sprite/Kitty_standing_bottom[KittyX.outfit[bottom]].png"

    if KittyX.outfit["dress"] and KittyX.top_pulled_up and KittyX.upskirt:
        "images/Kitty_sprite/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_both.png"
    elif KittyX.outfit["dress"] and KittyX.top_pulled_up:
        "images/Kitty_sprite/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_top.png"
    elif KittyX.outfit["dress"] and KittyX.upskirt:
        "images/Kitty_sprite/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_bottom.png"
    elif KittyX.outfit["dress"]:
        "images/Kitty_sprite/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose].png"

    # if KittyX.outfit["loincloth"]:
    #     "images/Kitty_sprite/Kitty_standing_loincloth[KittyX.outfit[loincloth]].png"

    # if KittyX.outfit["boots"]:
    #     "images/Kitty_sprite/Kitty_standing_boots[KittyX.outfit[boots]].png"

    if KittyX.outfit["top"] and KittyX.top_pulled_up:
        "images/Kitty_sprite/Kitty_standing_top[KittyX.outfit[top]][KittyX.arm_pose]_up.png"
    elif KittyX.outfit["top"]:
        "images/Kitty_sprite/Kitty_standing_top[KittyX.outfit[top]][KittyX.arm_pose].png"

    # if KittyX.outfit["piercings"] and (((KittyX.outfit["bottom"] or KittyX.outfit["dress"]) and not KittyX.upskirt) or (KittyX.outfit["underwear"] and not KittyX.underwear_pulled_down)):
    #     "images/Kitty_sprite/Kitty_standing_piercings_pussy[KittyX.outfit[piercings]]_covered.png"

    # if KittyX.outfit["piercings"] and (KittyX.outfit["top"] or KittyX.outfit["bra"] or KittyX.outfit["dress"]) and not KittyX.top_pulled_up:
    #     "images/Kitty_sprite/Kitty_standing_piercings_breasts[KittyX.outfit[piercings]]_covered.png"

    if KittyX.outfit["neck"]:
        "images/Kitty_sprite/Kitty_standing_neck[KittyX.outfit[neck]].png"

    # if KittyX.outfit["gloves"]:
    #     "images/Kitty_sprite/Kitty_standing_gloves[KittyX.outfit[gloves]][KittyX.arm_pose].png"

    # if KittyX.outfit["sleeves"]:
    #     "images/Kitty_sprite/Kitty_standing_sleeves[KittyX.outfit[sleeves]][KittyX.arm_pose].png"

    # if (KittyX.outfit["suspenders"] and KittyX.outfit["bottom"] and not KittyX.upskirt and KittyX.top_pulled_up) or KittyX.outfit["suspenders"] == "_suspenders2":
    #     "images/Kitty_sprite/Kitty_standing_suspenders[KittyX.outfit[suspenders]][KittyX.arm_pose]_up.png"
    # elif KittyX.outfit["suspenders"] and KittyX.outfit["bottom"] and not KittyX.upskirt:
    #     "images/Kitty_sprite/Kitty_standing_suspenders[KittyX.outfit[suspenders]][KittyX.arm_pose].png"

    # if KittyX.outfit["scarf"]:
    #     "images/Kitty_sprite/Kitty_standing_scarf[KittyX.outfit[scarf]].png"

    # if KittyX.outfit["jacket"]:
    #     "images/Kitty_sprite/Kitty_standing_jacket[KittyX.outfit[jacket]].png"

    # if KittyX.outfit["cloak"]:
    #     "images/Kitty_sprite/Kitty_standing_cloak[KittyX.outfit[cloak]].png"

    if KittyX.spunk["breasts"]:
        "images/Kitty_sprite/Kitty_standing_spunk_breasts.png"

    if KittyX.spunk["belly"]:
        "images/Kitty_sprite/Kitty_standing_spunk_belly.png"

    if KittyX.spunk["hand"] and KittyX.arm_pose == 2:
        "images/Kitty_sprite/Kitty_standing_spunk_hand.png"

    if KittyX.wet and KittyX.wet < 3:
        "images/Kitty_sprite/Kitty_standing_water_body[KittyX.arm_pose].png"

    if KittyX.outfit["held_item"] and KittyX.arm_pose == 2:
        "images/Kitty_sprite/Kitty_standing_held[KittyX.outfit[held_item]].png"

    # always:
    #     "Kitty_standing_fondling_animations"

    anchor (0.5, 0.0) offset (40, 170) zoom 0.95

layeredimage Kitty_back_hair:
    if KittyX.outfit["hair"] != "_evo":
        "images/Kitty_sprite/Kitty_standing_back_hair[KittyX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Kitty_head:
    always:
        "images/Kitty_sprite/Kitty_standing_face[KittyX.outfit[hair]][KittyX.blushing].png"

    # if KittyX.outfit["face_piercings"]:
    #     "images/Kitty_sprite/Kitty_standing_face_piercings[KittyX.outfit[face_piercings]].png"

    always:
        "images/Kitty_sprite/Kitty_standing_brows[KittyX.brows].png"

    always:
        "images/Kitty_sprite/Kitty_standing_mouth[KittyX.mouth].png"

    if KittyX.eyes == "_closed":
        "images/Kitty_sprite/Kitty_standing_eyes_closed.png"
    elif KittyX.eyes == "_squint":
        "Kitty_squinting"
    else:
        "Kitty_blinking"

    # if KittyX.outfit["face_inner_accessory"]:
    #     "images/Kitty_sprite/Kitty_standing_face_inner_accessory[KittyX.outfit[face_inner_accessory]].png"

    if KittyX.spunk["mouth"]:
        "images/Kitty_sprite/Kitty_spunk_standing[KittyX.mouth].png"

    if KittyX.spunk["face"]:
        "images/Kitty_sprite/Kitty_standing_face_spunk.png"

    always:
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.outfit[hair]].png"

    if KittyX.spunk["hair"] and KittyX.outfit["hair"] != "_wet":
        "images/Kitty_sprite/Kitty_standing_hair[KittyX.outfit[hair]]_spunk.png"

    # if KittyX.outfit["face_outer_accessory"]:
    #     "images/Kitty_sprite/Kitty_standing_face_outer_accessory[KittyX.outfit[face_outer_accessory]].png"

    if KittyX.wet:
        "images/Kitty_sprite/Kitty_standing_water_head.png"

    anchor (0.5, 0.5)






# layeredimage Kitty_sex_body:
#     always:
#         "Kitty_back_hair" pos (0.49, -0.07) anchor (0.5, 0.5) rotate -10 zoom 1.5
#
#     always:
#         "images/Kitty_sex/Kitty_sex_body[KittyX.outfit[front_inner_accessory]].png"
#
#     always:
#         "Kitty_head" pos (0.49, -0.07) anchor (0.5, 0.5) rotate -10 zoom 1.5
#
#     if KittyX.neck:
#         "images/Kitty_sex/Kitty_sex_neck[KittyX.neck].png"
#
#     if KittyX.legs:
#         "images/Kitty_sex/Kitty_sex_legs_dress_waist.png"
#
#     if not KittyX.bra:
#         Null()
#     elif KittyX.top_pulled_up:
#         "images/Kitty_sex/Kitty_sex_bra[KittyX.bra]_up.png"
#     elif KittyX.top == "_red_shirt" and KittyX.bra == "_sports_bra":
#         "images/Kitty_sex/Kitty_sex_bra[KittyX.bra][KittyX.bra]_top_up.png"
#     elif KittyX.top and KittyX.bra != "_cami":
#         "images/Kitty_sex/Kitty_sex_bra[KittyX.bra]_top.png"
#     else:
#         "images/Kitty_sex/Kitty_sex_bra[KittyX.bra].png"
#
#     if KittyX.wet:
#         "images/Kitty_sex/Kitty_sex_body_wet.png"
#
#     if not KittyX.top:
#         Null()
#     elif not KittyX.top_pulled_up:
#         "images/Kitty_sex/Kitty_sex_top[KittyX.top].png"
#     elif KittyX.top == "_pink_top" and KittyX.bra == "_sports_bra":
#         "images/Kitty_sex/Kitty_sex_top[KittyX.top][KittyX.bra].png"
#     elif KittyX.top:
#         "images/Kitty_sex/Kitty_sex_top[KittyX.top]_up.png"
#
#     if KittyX.bra and KittyX.top and KittyX.top_pulled_up:
#         "images/Kitty_sex/Kitty_sex_bra[KittyX.bra]_up.png"
#
#     if KittyX.spunk["belly"]:
#         "images/Kitty_sex_Kitty_sex_spunk_belly_body.png"
#
#     if KittyX.spunk["breasts"]:
#         "images/Kitty_sex/Kitty_sex_spunk_tits.png"
#
#     if "suck_breasts" in [primary_action, offhand_action]:
#         "Kitty_sex_Lick_Breasts"
#
#     if "fondle_breasts" in [primary_action, offhand_action]:
#         "Kitty_sex_Fondle_Breasts"
#
#     size (1120, 840)
#
# layeredimage Kitty_sex_legs:
#     if KittyX.legs == "_dress" and KittyX.upskirt:
#         "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_back_up.png"
#     elif KittyX.legs in ["_dress", "_blue_skirt"]:
#         "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_back.png"
#
#     always:
#         "images/Kitty_sex/Kitty_sex_legs.png"
#
#     if KittyX.wet:
#         "images/Kitty_sex/Kitty_sex_legs_wet.png"
#
#     always:
#         "Kitty_sex_anus"
#
#     always:
#         "Kitty_sex_pussy"
#
#     if KittyX.underwear_pulled_down:
#         Null()
#     elif KittyX.underwear and KittyX.grool:
#         "images/Kitty_sex/Kitty_sex_underwear[KittyX.underwear]_wet.png"
#     elif KittyX.underwear:
#         "images/Kitty_sex/Kitty_sex_underwear[KittyX.underwear].png"
#
#     if KittyX.underwear and KittyX.underwear_pulled_down:
#         Null()
#     elif KittyX.hose:
#         "images/Kitty_sex/Kitty_sex_hose[KittyX.hose].png"
#
#     if KittyX.legs == "_dress" and KittyX.upskirt:
#         "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_up.png"
#     elif KittyX.legs in ["_dress", "_blue_skirt"]:
#         "images/Kitty_sex/Kitty_sex_legs[KittyX.legs].png"
#     elif KittyX.upskirt:
#         Null()
#     elif KittyX.legs and KittyX.grool == 2:
#         "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_wet.png"
#     elif KittyX.legs:
#         "images/Kitty_sex/Kitty_sex_legs[KittyX.legs].png"
#
#     if KittyX.top == "_towel" and not KittyX.top_pulled_up:
#         "images/Kitty_sex/Kitty_sex_top[KittyX.top]_legs.png"
#
#     if KittyX.spunk["belly"]:
#         "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"
#
#     if not Player.sprite or Player.cock_position != "out":
#         Null()
#     else:
#         "Kitty_Hotdog_Zero_Anim[action_speed]"
#
#     if Player.sprite and Player.cock_position:
#         Null()
#     elif primary_action == "eat_pussy":
#         "Kitty_sex_Lick_Pussy"
#     elif primary_action == "eat_ass":
#         "Kitty_sex_Lick_Ass"
#
#     if not Player.sprite or Player.cock_position != "footjob":
#         Null()
#     else:
#         "Kitty_Footcock_Zero_Anim[action_speed]"
#
#     if not action_speed:
#         "Kitty_sex_feet"
#     elif Player.cock_position:
#         AlphaMask("Kitty_sex_feet", "images/Kitty_sex/Kitty_sex_feet_mask.png")
#     else:
#         "Kitty_sex_feet"
#
#     size (1120, 840)
#
# layeredimage Kitty_sex_feet:
#     always:
#         "images/Kitty_sex/Kitty_sex_feet.png"
#
#     if KittyX.wet:
#         "images/Kitty_sex/Kitty_sex_feet_wet.png"
#
#     if KittyX.legs and not KittyX.upskirt and KittyX.legs not in ["_blue_skirt", "_shorts"] and KittyX.hose:
#         "images/Kitty_sex/Kitty_sex_hose[KittyX.hose]_feet_under.png"
#     elif KittyX.hose:
#         "images/Kitty_sex/Kitty_sex_hose[KittyX.hose]_feet.png"
#
#     if not KittyX.upskirt:
#         "images/Kitty_sex/Kitty_sex_legs[KittyX.legs]_feet.png"
#
#     size (1120, 840)
#
# layeredimage Kitty_sex_pussy:
#     if Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
#         "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
#     elif Player.sprite and Player.cock_position == "sex" and action_speed:
#         "images/Kitty_sex/Kitty_sex_pussy_open.png"
#     elif Player.sprite and Player.cock_position == "sex":
#         "images/Kitty_sex/Kitty_sex_pussy_closed.png"
#     elif primary_action == "eat_pussy":
#         "images/Kitty_sex/Kitty_sex_pussy_open.png"
#     else:
#         "images/Kitty_sex/Kitty_sex_pussy_closed.png"
#
#     if not KittyX.grool:
#         Null()
#     elif Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
#         "images/Kitty_sex/Kitty_sex_pussy_wet_fucking.png"
#     else:
#         "images/Kitty_sex/Kitty_sex_pussy_wet.png"
#
#     if not KittyX.outfit["front_inner_accessory"]:
#         Null()
#     elif not Player.sprite or Player.cock_position != "sex" or action_speed <= 1:
#         "images/Kitty_sex/Kitty_sex_piercings[KittyX.outfit[front_inner_accessory]]_pussy.png"
#     else:
#         "images/Kitty_sex/Kitty_sex_piercings[KittyX.outfit[front_inner_accessory]]_pussy_fucking.png"
#
#     if not KittyX.pubes:
#         Null()
#     elif Player.sprite and Player.cock_position == "sex" and action_speed >= 2:
#         "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
#     elif Player.sprite and Player.cock_position == "sex" and action_speed:
#         "images/Kitty_sex/Kitty_sex_pubes_open.png"
#     elif Player.sprite and Player.cock_position == "sex":
#         "images/Kitty_sex/Kitty_sex_pubes_closed.png"
#     elif primary_action == "eat_pussy":
#         "images/Kitty_sex/Kitty_sex_pubes_open.png"
#     else:
#         "images/Kitty_sex/Kitty_sex_pubes_closed.png"
#
#     if KittyX.spunk["sex"]:
#         "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"
#
#     if KittyX.underwear and KittyX.underwear_pulled_down:
#         Null()
#     elif KittyX.hose == "_ripped_pantyhose":
#         "images/Kitty_sex/Kitty_sex_hose[KittyX.hose].png"
#
#     if not Player.sprite or Player.cock_position != "sex":
#         Null()
#     else:
#         AlphaMask("Kitty_sex_Zero_Anim[action_speed]", "Kitty_Pussy_Fucking_Mask")
#
#     if not KittyX.spunk["pussy"] or not Player.sprite or Player.cock_position != "sex" or not action_speed:
#         Null()
#     elif action_speed == 1:
#         "Kitty_Pussy_Spunk_Heading"
#     else:
#         "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"
#
# layeredimage Kitty_sex_anus:
#     if Player.sprite and Player.cock_position == "anal" and action_speed < 2:
#         "Kitty_sex_Anal[action_speed]"
#     elif Player.sprite and Player.cock_position == "anal":
#         "images/Kitty_sex/Kitty_sex_anus_open.png"
#     elif KittyX.used_to_anal:
#         "images/Kitty_sex/Kitty_sex_anus_loose.png"
#     else:
#         "images/Kitty_sex/Kitty_sex_anus_tight.png"
#
#     if not KittyX.spunk["anus"]:
#         Null()
#     elif Player.sprite and Player.cock_position != "anal" and action_speed >= 1:
#         "images/Kitty_sex/Kitty_sex_spunk_anal_under.png"
#     elif Player.sprite and Player.cock_position != "anal" and action_speed:
#         "Kitty_sex_Anal_Spunk_Heading_Under"
#     else:
#         "images/Kitty_sex/Kitty_sex_spunk_anal_closed.png"
#
#     if not Player.sprite or Player.cock_position != "anal":
#         Null()
#     else:
#         AlphaMask("Kitty_Anal_Zero_Anim[action_speed]", "Kitty_sex_Anal_Fucking_Mask")
#
#     if not KittyX.spunk["anus"] or not Player.sprite or Player.cock_position != "anal" or not action_speed:
#         Null()
#     elif action_speed == 1:
#         "Kitty_sex_Anal_Spunk_Heading_Over"
#     else:
#         "images/Kitty_sex/Kitty_sex_spunk_anal_over.png"
