layeredimage Storm_sprite standing:
    # always:
    #     "images/Storm_standing/Storm_standing_head_reference.png"

    if StormX.outfit["jacket"]:
        "images/Storm_standing/Storm_standing_back_outer_accessory[StormX.outfit[jacket]].png"

    if StormX.outfit["bra"] in ["_black_bra", "_sports_bra"] and StormX.bra_pulled_up:
        "images/Storm_standing/Storm_standing_back_outer_accessory[StormX.outfit[bra]]_up.png"

    if StormX.outfit["bottom"] == "_skirt":
        "images/Storm_standing/Storm_standing_back_outer_accessory[StormX.outfit[bottom]].png"
    elif StormX.outfit["bottom"] in ["_pants", "_yoga_pants"] and StormX.bottom_pulled_down:
        "images/Storm_standing/Storm_standing_back_outer_accessory[StormX.outfit[bottom]]_down.png"

    if StormX.outfit["underwear"] and StormX.underwear_pulled_down:
        "images/Storm_standing/Storm_standing_back_inner_accessory[StormX.outfit[underwear]]_down.png"

    always:
        "Storm_back_hair" pos (0.1395, 0.158) zoom 0.47

    always:
        "images/Storm_standing/Storm_standing_body[StormX.arm_pose].png"

    if StormX.pubes:
        "images/Storm_standing/Storm_standing_pubes.png"

    if StormX.outfit["sleeves"]:
        "images/Storm_standing/Storm_standing_sleeves[StormX.outfit[sleeves]][StormX.arm_pose].png"

    if StormX.outfit["piercings"]:
        "images/Storm_standing/Storm_standing_piercings_pussy[StormX.outfit[piercings]].png"

    if not StormX.outfit["underwear"]:
        Null()
    elif StormX.outfit["underwear"] == "_bikini_bottoms" and (StormX.outfit["bra"] != "_bikini_top" or StormX.bra_pulled_up):
        "images/Storm_standing/Storm_standing_underwear_bikini_bottoms_unclipped.png"
    elif StormX.underwear_pulled_down and StormX.grool > 1:
        "images/Storm_standing/Storm_standing_underwear[StormX.outfit[underwear]]_down_grool.png"
    elif StormX.underwear_pulled_down:
        "images/Storm_standing/Storm_standing_underwear[StormX.outfit[underwear]]_down.png"
    elif StormX.grool > 1:
        "images/Storm_standing/Storm_standing_underwear[StormX.outfit[underwear]]_grool.png"
    else:
        "images/Storm_standing/Storm_standing_underwear[StormX.outfit[underwear]].png"

    if StormX.outfit["hose"]:
        "images/Storm_standing/Storm_standing_hose[StormX.outfit[hose]].png"

    if StormX.outfit["boots"]:
        "images/Storm_standing/Storm_standing_boots[StormX.outfit[boots]].png"

    if StormX.outfit["bottom"] and StormX.grool > 1:
        "images/Storm_standing/Storm_standing_grool.png"
    elif StormX.grool:
        "images/Storm_standing/Storm_standing_grool.png"

    always:
        "Storm_grool_animations"

    if StormX.spunk["pussy"] or StormX.spunk["anus"]:
        "images/Storm_standing/Storm_standing_spunk_pussy.png"

    always:
        "Storm_spunk_animations"

    if not StormX.outfit["bottom"]:
        Null()
    elif StormX.bottom_pulled_down or StormX.upskirt:
        "images/Storm_standing/Storm_standing_bottom[StormX.outfit[bottom]]_down.png"
    elif StormX.outfit["bottom"] in ["_pants", "_yoga_pants"] and StormX.grool > 1:
        "images/Storm_standing/Storm_standing_bottom[StormX.outfit[bottom]]_grool.png"
    else:
        "images/Storm_standing/Storm_standing_bottom[StormX.outfit[bottom]].png"

    if StormX.arm_pose == 1:
        "images/Storm_standing/Storm_standing_hands[StormX.arm_pose].png"
    elif StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_hand[StormX.arm_pose]_right.png"

    if StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_hand[StormX.arm_pose]_left.png"

    if StormX.breasts_supported:
        "images/Storm_standing/Storm_standing_breasts_up.png"
    else:
        "images/Storm_standing/Storm_standing_breasts_down.png"

    if not StormX.outfit["piercings"]:
        Null()
    elif StormX.breasts_supported:
        "images/Storm_standing/Storm_standing_piercings_breasts[StormX.outfit[piercings]]_up.png"
    else:
        "images/Storm_standing/Storm_standing_piercings_breasts[StormX.outfit[piercings]]_down.png"

    if not StormX.outfit["bra"]:
        Null()
    elif StormX.bra_pulled_up:
        "images/Storm_standing/Storm_standing_bra[StormX.outfit[bra]]_up.png"
    else:
        "images/Storm_standing/Storm_standing_bra[StormX.outfit[bra]].png"

    if StormX.outfit["dress"]:
        "images/Storm_standing/Storm_standing_dress[StormX.outfit[dress]][StormX.arm_pose].png"

    if not StormX.outfit["top"]:
        Null()
    elif StormX.top_pulled_up:
        "images/Storm_standing/Storm_standing_top[StormX.outfit[top]]_up_up.png"
    elif StormX.breasts_supported:
        "images/Storm_standing/Storm_standing_top[StormX.outfit[top]]_up.png"
    else:
        "images/Storm_standing/Storm_standing_top[StormX.outfit[top]]_down.png"

    if StormX.outfit["neck"]:
        "images/Storm_standing/Storm_standing_neck[StormX.outfit[neck]].png"

    if StormX.outfit["jacket"] == "_jacket":
        "images/Storm_standing/Storm_standing_neck[StormX.outfit[jacket]].png"

    if StormX.outfit["piercings"] and StormX.pussy_covered:
        "images/Storm_standing/Storm_standing_piercings_pussy[StormX.outfit[piercings]]_covered.png"

    if not StormX.outfit["piercings"] or not StormX.breasts_covered:
        Null()
    elif StormX.breasts_supported:
        "images/Storm_standing/Storm_standing_piercings_breasts[StormX.outfit[piercings]]_up_covered.png"
    else:
        "images/Storm_standing/Storm_standing_piercings_breasts[StormX.outfit[piercings]]_down_covered.png"

    if not StormX.outfit["jacket"]:
        Null()
    elif StormX.jacket_opened:
        "images/Storm_standing/Storm_standing_jacket[StormX.outfit[jacket]][StormX.arm_pose]_up_up.png"
    elif StormX.breasts_supported:
        "images/Storm_standing/Storm_standing_jacket[StormX.outfit[jacket]][StormX.arm_pose]_up.png"
    else:
        "images/Storm_standing/Storm_standing_jacket[StormX.outfit[jacket]][StormX.arm_pose]_down.png"

    always:
        "Storm_head" pos (0.1395, 0.158) zoom 0.47

    if StormX.outfit["jacket"] == "_jacket" and StormX.arm_pose == 2 and renpy.showing("Storm_sprite handjob"):
        "images/Storm_handjob/Storm_handjob_sleeves[StormX.outfit[jacket]][StormX.arm_pose].png"
    elif StormX.outfit["jacket"] == "_jacket" and StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_sleeves[StormX.outfit[jacket]][StormX.arm_pose].png"
    elif StormX.outfit["sleeves"] == "_rings" and StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_sleeves[StormX.outfit[sleeves]][StormX.arm_pose]_top.png"

    if not StormX.spunk["breasts"]:
        Null()
    elif StormX.breasts_supported:
        "images/Storm_standing/Storm_standing_spunk_breasts_up.png"
    else:
        "images/Storm_standing/Storm_standing_spunk_breasts_down.png"

    if StormX.spunk["belly"]:
        "images/Storm_standing/Storm_standing_spunk_belly.png"

    if not StormX.wet:
        Null()
    elif StormX.breasts_supported:
        "images/Storm_standing/Storm_standing_water_body[StormX.arm_pose]_up.png"
    else:
        "images/Storm_standing/Storm_standing_water_body[StormX.arm_pose]_down.png"

    if StormX.wet and StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_water_arm[StormX.arm_pose].png"

    if StormX.outfit["face_outer_accessory"]:
        "images/Storm_standing/Storm_standing_face_outer_accessory[StormX.outfit[face_outer_accessory]].png" anchor (0.5, 0.5) pos (0.1395, 0.158) zoom 0.47

    if StormX.outfit["held_item"] and StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_held[StormX.outfit[held_item]].png"

    # always:
    #     "Storm_standing_fondling_animations"

    anchor (0.5, 0.0) offset (60, 180) zoom 0.95

layeredimage Storm_back_hair:
    if StormX.outfit["face_outer_accessory"] == "_towel":
        "images/Storm_standing/Storm_standing_face_outer_accessory[StormX.outfit[face_outer_accessory]]_under.png"
    elif StormX.outfit["hair"] in ["_wet_long", "_wet_short", "_wet_mohawk"]:
        "images/Storm_standing/Storm_standing_back_hair[StormX.outfit[hair]].png"
    elif StormX.wet:
        "images/Storm_standing/Storm_standing_back_hair_wet[StormX.outfit[hair]].png"
    else:
        "images/Storm_standing/Storm_standing_back_hair[StormX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Storm_head:
    if StormX.blushing:
        "images/Storm_standing/Storm_standing_head_blush.png"
    else:
        "images/Storm_standing/Storm_standing_head.png"

    always:
        "images/Storm_standing/Storm_standing_brows[StormX.brows].png"

    if StormX.spunk["mouth"]:
        "images/Storm_standing/Storm_standing_spunk_mouth[StormX.mouth].png"
    else:
        "images/Storm_standing/Storm_standing_mouth[StormX.mouth].png"

    if StormX.eyes == "_closed":
        "images/Storm_standing/Storm_standing_eyes_closed.png"
    else:
        "Storm_blinking"

    if StormX.outfit["face_inner_accessory"]:
        "images/Storm_standing/Storm_standing_face_inner_accessory[StormX.outfit[face_inner_accessory]].png"

    if StormX.spunk["chin"]:
        "images/Storm_standing/Storm_standing_spunk_chin.png"

    if StormX.spunk["face"]:
        "images/Storm_standing/Storm_standing_spunk_face.png"

    if StormX.outfit["face_outer_accessory"] == "_towel":
        Null()
    elif renpy.showing("Storm_sprite sex") and StormX.outfit["hair"] == "_long":
        "images/Storm_sex/Storm_sex_hair.png"
    elif StormX.outfit["hair"] in ["_wet_long", "_wet_short", "_wet_mohawk"]:
        "images/Storm_standing/Storm_standing_hair[StormX.outfit[hair]].png"
    elif StormX.wet:
        "images/Storm_standing/Storm_standing_hair_wet[StormX.outfit[hair]].png"
    else:
        "images/Storm_standing/Storm_standing_hair[StormX.outfit[hair]].png"

    if StormX.spunk["hair"]:
        "images/Storm_standing/Storm_standing_spunk_hair[StormX.outfit[hair]].png"

    if StormX.wet:
        "images/Storm_standing/Storm_standing_water_head.png"

    anchor (0.5, 0.5)

image Storm_handjob_under:
    "images/Storm_handjob/Storm_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Storm_handjob_over:
    "images/Storm_handjob/Storm_handjob_hand_over.png"

    anchor (0.5, 0.5)
