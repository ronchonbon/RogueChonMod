layeredimage Emma_sprite standing:
    # always:
    #     "images/Emma_standing/Emma_standing_head_reference.png"

    if EmmaX.top_pulled_up or EmmaX.outfit["top"] == "_jacket" or EmmaX.outfit["bra"] != "_corset":
        Null()
    elif EmmaX.outfit["back_outer_accessory"]:
        "images/Emma_standing/Emma_standing_back_outer_accessory[EmmaX.outfit[back_outer_accessory]][EmmaX.arm_pose].png"

    if EmmaX.outfit["back_inner_accessory"]:
        "images/Emma_standing/Emma_standing_back_inner_accessory[EmmaX.outfit[back_inner_accessory]].png"

    if EmmaX.outfit["bottom"] == "_dress":
        "images/Emma_standing/Emma_standing_back_dress[EmmaX.outfit[bottom]].png"

    if not EmmaX.outfit["underwear"] or not EmmaX.underwear_pulled_down or (EmmaX.outfit["bottom"] == "_pants" and not EmmaX.upskirt):
        Null()
    elif EmmaX.outfit["underwear"]:
        "images/Emma_standing/Emma_standing_back_underwear[EmmaX.outfit[underwear]].png"

    if EmmaX.outfit["back_hair"]:
        "Emma_back_hair" pos (0.1, 0.16) zoom 0.5

    # if EmmaX.outfit["buttplug"]:
    #     "images/Emma_standing/Emma_standing_buttplug[EmmaX.outfit[buttplug]].png"

    if EmmaX.diamond:
        "images/Emma_standing/Emma_standing_legs[EmmaX.arm_pose]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_legs[EmmaX.arm_pose].png"

    if EmmaX.pubes and EmmaX.diamond:
        "images/Emma_standing/Emma_standing_pubes_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_pubes.png"

    if EmmaX.outfit["bra"] == "_sports_bra" and not EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_under.png"
    elif EmmaX.outfit["bra"]:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_under.png"

    if EmmaX.diamond:
        "images/Emma_standing/Emma_standing_arms[EmmaX.arm_pose]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_arms[EmmaX.arm_pose].png"

    if EmmaX.outfit["gloves"]:
        "images/Emma_standing/Emma_standing_gloves[EmmaX.outfit[gloves]][EmmaX.arm_pose].png"

    if EmmaX.outfit["piercings"]:
        "images/Emma_standing/Emma_standing_piercings_pussy[EmmaX.outfit[piercings]].png"

    if EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down and (not EmmaX.outfit["bottom"] == "_pants" or EmmaX.upskirt or EmmaX.wearing_skirt) and EmmaX.grool:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_down_grool.png"
    elif EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down and (not EmmaX.outfit["bottom"] == "_pants" or EmmaX.upskirt or EmmaX.wearing_skirt):
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_down.png"
    elif EmmaX.outfit["underwear"] and EmmaX.grool:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_grool.png"
    elif EmmaX.outfit["underwear"]:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]].png"

    if EmmaX.outfit["hose"]:
        "images/Emma_standing/Emma_standing_hose[EmmaX.outfit[hose]].png"

    if EmmaX.outfit["bottom"] and EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_grool.png"
    elif EmmaX.grool:
        "images/Emma_standing/Emma_standing_grool.png"

    # always:
    #     "grool_dripping_animations"
    # if not EmmaX.grool:
    #     Null()
    # elif EmmaX.outfit["bottom"] == "_pants" and not EmmaX.upskirt:
    #     Null()
    # elif EmmaX.outfit["underwear"] and not EmmaX.underwear_pulled_down and EmmaX.grool < 2:
    #     Null()
    # elif EmmaX.grool == 1 and EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
    #     AlphaMask("grool_dripping", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    # elif EmmaX.grool == 1 and EmmaX.outfit["bottom"] == "_pants":
    #     AlphaMask("grool_dripping", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    # elif EmmaX.grool == 1:
    #     AlphaMask("grool_dripping", "images/Emma_standing/Emma_standing_grool_mask.png")
    # elif EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
    #     AlphaMask("heavy_grool_dripping", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    # elif EmmaX.outfit["underwear"] and EmmaX.outfit["bottom"] == "_pants":
    #     AlphaMask("grool_dripping", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    # elif EmmaX.outfit["bottom"] == "_pants":
    #     AlphaMask("heavy_grool_dripping", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    # elif EmmaX.outfit["underwear"]:
    #     AlphaMask("grool_dripping", "images/Emma_standing/Emma_standing_grool_mask.png")
    # else:
    #     AlphaMask("heavy_grool_dripping", "images/Emma_standing/Emma_standing_grool_mask.png")

    if EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]:
        "images/Emma_standing/Emma_standing_spunk_pussy.png"

    # always:
    #     "spunk_dripping_animations"
    # if not EmmaX.spunk["pussy"] and not EmmaX.spunk["anus"]:
    #     Null()
    # elif EmmaX.outfit["bottom"] == "_pants" and not EmmaX.upskirt:
    #     Null()
    # elif EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
    #     AlphaMask("heavy_spunk_dripping", "images/Emma_standing/Emma_standing_grool_mask_underwear.png")
    # elif EmmaX.outfit["underwear"] and EmmaX.outfit["bottom"] == "_pants":
    #     AlphaMask("spunk_dripping", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    # elif EmmaX.outfit["bottom"] == "_pants":
    #     AlphaMask("heavy_spunk_dripping", "images/Emma_standing/Emma_standing_grool_mask_pants.png")
    # else:
    #     AlphaMask("heavy_spunk_dripping", "images/Emma_standing/Emma_standing_grool_mask.png")

    if EmmaX.outfit["bottom"] and EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_down.png"
    elif EmmaX.outfit["bottom"] == "_yoga_pants" and EmmaX.grool:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_grool.png"
    elif EmmaX.outfit["bottom"]:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]].png"

    if EmmaX.outfit["loincloth"] == "_dress" and not EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_loincloth[EmmaX.outfit[loincloth]].png"
    elif EmmaX.outfit["loincloth"] and not EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_loincloth[EmmaX.outfit[loincloth]].png"

    if EmmaX.diamond and (EmmaX.arm_pose == 1 or EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"]):
        "images/Emma_standing/Emma_standing_breasts_up_diamond.png"
    elif EmmaX.arm_pose == 1 or EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"]:
        "images/Emma_standing/Emma_standing_breasts_up.png"
    elif EmmaX.diamond:
        "images/Emma_standing/Emma_standing_breasts_down_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_breasts_down.png"

    # if EmmaX.outfits["tattoos"]:
    #     "images/Emma_standing/Emma_standing_tattoos[EmmaX.outfit[tattoos]].png"

    if EmmaX.outfit["piercings"] and EmmaX.arm_pose == 1:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_up.png"
    elif EmmaX.outfit["piercings"]:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_down.png"

    # if EmmaX.outfit["clamps"]:
    #     "images/Emma_standing/Emma_standing_clamps[EmmaX.outfit[clamps]].png"

    # if EmmaX.outfit["rope"]:
    #     "images/Emma_standing/Emma_standing_rope[EmmaX.outfit[rope]].png"

    if EmmaX.outfit["sleeves"] and EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_sleeves[EmmaX.outfit[sleeves]][EmmaX.arm_pose]_up.png"

    if EmmaX.outfit["bra"] and EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_up.png"
    elif EmmaX.outfit["bra"] == "_corset" and EmmaX.outfit["top"]:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_top.png"
    elif EmmaX.outfit["bra"]:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]].png"

    # if EmmaX.outfit["dress"] and EmmaX.top_pulled_up and EmmaX.upskirt:
    #     "images/Emma_standing/Emma_standing_dress[EmmaX.outfit[dress]][EmmaX.arm_pose]_both.png"
    # elif EmmaX.outfit["dress"] and EmmaX.top_pulled_up:
    #     "images/Emma_standing/Emma_standing_dress[EmmaX.outfit[dress]][EmmaX.arm_pose]_top.png"
    # elif EmmaX.outfit["dress"] and EmmaX.upskirt:
    #     "images/Emma_standing/Emma_standing_dress[EmmaX.outfit[dress]][EmmaX.arm_pose]_bottom.png"
    if EmmaX.outfit["dress"]:
        "images/Emma_standing/Emma_standing_dress[EmmaX.outfit[dress]][EmmaX.arm_pose].png"

    if EmmaX.outfit["boots"]:
        "images/Emma_standing/Emma_standing_boots[EmmaX.outfit[boots]].png"

    if EmmaX.outfit["top"] and EmmaX.top_pulled_up and EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"]:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up_up.png"
    if EmmaX.outfit["top"] and EmmaX.top_pulled_up and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_down_up.png"
    elif EmmaX.outfit["top"] and EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up.png"
    elif EmmaX.outfit["top"] and (EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"] or (EmmaX.outfit["top"] == "_towel" and EmmaX.arm_pose == 1)):
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up.png"
    elif EmmaX.outfit["top"] and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_down.png"
    elif EmmaX.outfit["top"]:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose].png"

    always:
        "Emma_head" pos (0.1, 0.16) zoom 0.5

    if EmmaX.outfit["piercings"] and (((EmmaX.outfit["bottom"] or EmmaX.outfit["dress"]) and not EmmaX.upskirt) or (EmmaX.outfit["underwear"] and not EmmaX.underwear_pulled_down)):
        "images/Emma_standing/Emma_standing_piercings_pussy[EmmaX.outfit[piercings]]_covered.png"

    if EmmaX.outfit["piercings"] and (EmmaX.arm_pose == 1 or EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"]) and (EmmaX.outfit["top"] or EmmaX.outfit["bra"] or EmmaX.outfit["dress"]) and not EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_up_covered.png"
    elif EmmaX.outfit["piercings"] and (EmmaX.outfit["top"] or EmmaX.outfit["bra"] or EmmaX.outfit["dress"]) and not EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_down_covered.png"

    # if EmmaX.outfit["neck"]:
    #     "images/Emma_standing/Emma_standing_neck[EmmaX.outfit[neck]].png"

    # always:
    #     "images/Emma_standing/Emma_standing_hand[EmmaX.arm_pose]_left.png"

    # always:
    #     "images/Emma_standing/Emma_standing_hand[EmmaX.arm_pose]_right.png"

    # if (EmmaX.outfit["suspenders"] and EmmaX.outfit["bottom"] and not EmmaX.upskirt and EmmaX.top_pulled_up) or EmmaX.outfit["suspenders"] == "_suspenders2":
    #     "images/Emma_standing/Emma_standing_suspenders[EmmaX.outfit[suspenders]][EmmaX.arm_pose]_up.png"
    # elif EmmaX.outfit["suspenders"] and EmmaX.outfit["bottom"] and not EmmaX.upskirt:
    #     "images/Emma_standing/Emma_standing_suspenders[EmmaX.outfit[suspenders]][EmmaX.arm_pose].png"

    if EmmaX.outfit["scarf"] == "_dress" and EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_scarf[EmmaX.outfit[scarf]][EmmaX.arm_pose].png"

    if EmmaX.outfit["jacket"] and EmmaX.top_pulled_up and EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"]:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up_up.png"
    if EmmaX.outfit["jacket"] and EmmaX.top_pulled_up and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_down_up.png"
    elif EmmaX.outfit["jacket"] and EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up.png"
    elif EmmaX.outfit["jacket"] and EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"]:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up.png"
    elif EmmaX.outfit["jacket"] and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_down.png"
    elif EmmaX.outfit["jacket"]:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose].png"

    # if EmmaX.outfit["cloak"]:
    #     "images/Emma_standing/Emma_standing_cloak[EmmaX.outfit[cloak]].png"

    if EmmaX.spunk["breasts"] and EmmaX.arm_pose == 1 and EmmaX.outfit["bra"] in ["_corset", "_lace_bra", "_sports_bra", "_bikini_top"]:
        "images/Emma_standing/Emma_standing_spunk_breasts_up.png"
    elif EmmaX.spunk["breasts"]:
        "images/Emma_standing/Emma_standing_spunk_breasts_down.png"

    if EmmaX.spunk["belly"]:
        "images/Emma_standing/Emma_standing_spunk_belly.png"

    if EmmaX.spunk["hand"] and EmmaX.arm_pose == 2 and EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_hand_mouth.png"
    elif EmmaX.spunk["hand"] and EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_hand.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_body[EmmaX.arm_pose].png"

    if EmmaX.wet and (EmmaX.arm_pose == 1 or EmmaX.outfit["bra"] == "_corset"):
        "images/Emma_standing/Emma_standing_water_breasts_up.png"
    elif EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_breasts_down.png"

    if EmmaX.wet and EmmaX.arm_pose == 1:
        "images/Emma_standing/Emma_standing_water_arm[EmmaX.arm_pose].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_legs.png"

    if EmmaX.outfit["face_outer_accessory"]:
        "images/Emma_standing/Emma_standing_face_outer_accessory[EmmaX.outfit[face_outer_accessory]].png" pos (0.0, -0.043) zoom 0.5

    if EmmaX.outfit["held_item"] and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_held[EmmaX.outfit[held_item]].png"

    # always:
    #     "Emma_standing_fondling_animations"

    anchor (0.5, 0.0) offset (0, 140)

layeredimage Emma_back_hair:
    if EmmaX.diamond:
        "images/Emma_standing/Emma_standing_back_hair[EmmaX.outfit[back_hair]]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_back_hair[EmmaX.outfit[back_hair]].png"

    anchor (0.5, 0.5)

layeredimage Emma_head:
    if EmmaX.diamond:
        "images/Emma_standing/Emma_standing_head[EmmaX.brows][EmmaX.outfit[hair]][EmmaX.blushing]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_head[EmmaX.brows][EmmaX.outfit[hair]][EmmaX.blushing].png"

    # if EmmaX.outfit["face_piercings"]:
    #     "images/Emma_standing/Emma_standing_face_piercings[EmmaX.outfit[face_piercings]].png"

    if EmmaX.diamond:
        "images/Emma_standing/Emma_standing_brows[EmmaX.brows]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_brows[EmmaX.brows].png"

    if EmmaX.diamond and EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_mouth[EmmaX.mouth]_diamond.png"
    elif EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_mouth[EmmaX.mouth].png"
    elif EmmaX.diamond:
        "images/Emma_standing/Emma_standing_mouth[EmmaX.mouth]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_mouth[EmmaX.mouth].png"

    if EmmaX.eyes == "_closed" and EmmaX.diamond:
        "images/Emma_standing/Emma_standing_eyes_closed_diamond.png"
    elif EmmaX.eyes == "_closed":
        "images/Emma_standing/Emma_standing_eyes_closed.png"
    elif EmmaX.eyes == "_squint" and EmmaX.diamond:
        "Emma_squinting_diamond"
    elif EmmaX.eyes == "_squint":
        "Emma_squinting"
    elif EmmaX.diamond:
        "Emma_blinking_diamond"
    else:
        "Emma_blinking"

    # if EmmaX.outfit["face_inner_accessory"]:
    #     "images/Emma_standing/Emma_standing_face_inner_accessory[EmmaX.outfit[face_inner_accessory]].png"

    # if EmmaX.spunk["chin"]:
    #     "images/Emma_standing/Emma_standing_spunk_chin.png"

    if EmmaX.spunk["face"]:
        "images/Emma_standing/Emma_standing_spunk_face.png"

    if EmmaX.diamond:
        "images/Emma_standing/Emma_standing_hair[EmmaX.outfit[hair]]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_hair[EmmaX.outfit[hair]].png"

    if EmmaX.spunk["hair"]:
        "images/Emma_standing/Emma_standing_spunk_hair[EmmaX.outfit[hair]].png"

    if EmmaX.outfit["face_outer_accessory"] in ["_hat", "_wet_hat"]:
        "images/Emma_standing/Emma_standing_shadow_head[EmmaX.outfit[hair]].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_head.png"

    anchor (0.5, 0.5)

layeredimage Emma_domme:
    always:
        "images/Emma_domme/Emma_domme_back_hair[EmmaX.outfit[back_hair]].png"

    always:
        "images/Emma_domme/Emma_domme_body.png"

    if EmmaX.outfit["neck"]:
        "images/Emma_domme/Emma_domme_neck[EmmaX.outfit[neck]].png"

    always:
        "Emma_domme_head"

    if EmmaX.outfit["hose"]:
        "images/Emma_domme/Emma_domme_hose[EmmaX.outfit[hose]].png"

    if EmmaX.outfit["dress"]:
        "images/Emma_domme/Emma_domme_dress[EmmaX.outfit[dress]].png"

    if EmmaX.outfit["gloves"]:
        "images/Emma_domme/Emma_domme_gloves[EmmaX.outfit[gloves]].png"

    always:
        "images/Emma_domme/Emma_domme_hair[EmmaX.outfit[hair]].png"

    if EmmaX.outfit["held_item"]:
        "images/Emma_domme/Emma_domme_held_item[EmmaX.outfit[held_item]].png"

    anchor (0.5, -0.16) zoom 0.48

layeredimage Emma_domme_head:
    always:
        "images/Emma_domme/Emma_domme_head.png"

    always:
        "images/Emma_domme/Emma_domme_brows_angry.png"

    always:
        "images/Emma_domme/Emma_domme_mouth[EmmaX.mouth].png"

    always:
        "images/Emma_domme/Emma_domme_eyes[EmmaX.eyes].png"
