layeredimage Rogue_sprite:
    # always:
    #     "images/Rogue_sprite/Rogue_standing_head_reference.png"

    # if RogueX.outfit["back_outer_accessory"]:
    #     "images/Rogue_sprite/Rogue_standing_back_outer_accessory[RogueX.outfit[back_outer_accessory]].png"
    #
    # if RogueX.outfit["back_inner_accessory"]:
    #     "images/Rogue_sprite/Rogue_standing_back_inner_accessory[RogueX.outfit[back_inner_accessory]].png"

    # if RogueX.outfit["dress"]:
    #     "images/Rogue_sprite/Rogue_standing_back_dress[RogueX.outfit[dress]].png"

    # if RogueX.outfit["underwear"]:
    #     "images/Rogue_sprite/Rogue_standing_back_underwear[RogueX.outfit[underwear]].png"

    if RogueX.outfit["back_hair"] and not renpy.showing("Rogue_blowjob_animation"):
        "Rogue_back_hair" pos (0.156, 0.158) zoom 0.29

    always:
        "images/Rogue_sprite/Rogue_standing_body[RogueX.pubes][RogueX.outfit[piercings]].png"

    if not renpy.showing("Rogue_blowjob_animation"):
        "Rogue_head" pos (0.156, 0.158) zoom 0.29

    always:
        "images/Rogue_sprite/Rogue_standing_arms[RogueX.arm_pose][RogueX.outfit[neck]][RogueX.outfit[gloves]].png"

    always:
        "images/Rogue_sprite/Rogue_standing_breasts[RogueX.outfit[piercings]].png"

    # if RogueX.outfit["piercings"]:
    #     "images/Rogue_sprite/Rogue_standing_piercings_breasts[RogueX.outfit[piercings]].png"

    # if RogueX.outfit["piercings"]:
    #     "images/Rogue_sprite/Rogue_standing_piercings_pussy[RogueX.outfit[piercings]].png"

    # if RogueX.outfit["clamps"]:
    #     "images/Rogue_sprite/Rogue_standing_clamps[RogueX.outfit[clamps]].png"

    # if RogueX.outfit["buttplug"]:
    #     "images/Rogue_sprite/Rogue_standing_buttplug[RogueX.outfit[buttplug]].png"

    # if RogueX.outfit["rope"]:
    #     "images/Rogue_sprite/Rogue_standing_rope[RogueX.outfit[rope]].png"

    if RogueX.outfit["bra"] and RogueX.top_pulled_up:
        "images/Rogue_sprite/Rogue_standing_bra[RogueX.outfit[bra]]_up.png"
    elif RogueX.outfit["bra"]:
        "images/Rogue_sprite/Rogue_standing_bra[RogueX.outfit[bra]].png"

    if RogueX.outfit["underwear"] and RogueX.underwear_pulled_down and RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]]_down_grool.png"
    elif RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]]_down.png"
    elif RogueX.outfit["underwear"] and RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]]_grool.png"
    elif RogueX.outfit["underwear"]:
        "images/Rogue_sprite/Rogue_standing_underwear[RogueX.outfit[underwear]].png"

    if RogueX.outfit["hose"] == "_tights" and RogueX.grool:
        "images/Rogue_sprite/Rogue_standing_hose[RogueX.outfit[hose]]_grool.png"
    elif RogueX.outfit["hose"]:
        "images/Rogue_sprite/Rogue_standing_hose[RogueX.outfit[hose]].png"

    if RogueX.outfit["bottom"] and RogueX.grool >= 2:
        "images/Rogue_sprite/Rogue_standing_grool1.png"
    elif RogueX.grool:
        "images/Rogue_sprite/Rogue_standing_grool[RogueX.grool].png"

    # always:
    #     "grool_dripping_animations"
    # if not RogueX.grool:
    #     Null()
    # elif RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt:
    #     Null()
    # elif RogueX.outfit["underwear"] and not RogueX.underwear_pulled_down and RogueX.grool < 2:
    #     Null()
    # elif RogueX.grool == 1 and RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
    #     AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_underwear.png")
    # elif RogueX.grool == 1 and RogueX.outfit["bottom"] == "_pants":
    #     AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    # elif RogueX.grool == 1:
    #     AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")
    # elif RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
    #     AlphaMask("heavy_grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_underwear.png")
    # elif RogueX.outfit["underwear"] and RogueX.outfit["bottom"] == "_pants":
    #     AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    # elif RogueX.outfit["bottom"] == "_pants":
    #     AlphaMask("heavy_grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    # elif RogueX.outfit["underwear"]:
    #     AlphaMask("grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")
    # else:
    #     AlphaMask("heavy_grool_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")

    # if not RogueX.spunk["pussy"] and not RogueX.spunk["anus"]:
    #     Null()
    # elif RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt:
    #     Null()
    # elif RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
    #     AlphaMask("heavy_spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_underwear.png")
    # elif RogueX.outfit["underwear"] and RogueX.outfit["bottom"] == "_pants":
    #     AlphaMask("spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    # elif RogueX.outfit["bottom"] == "_pants":
    #     AlphaMask("heavy_spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask_pants.png")
    # else:
    #     AlphaMask("heavy_spunk_dripping", "images/Rogue_sprite/Rogue_standing_grool_mask.png")

    if RogueX.outfit["bottom"] and RogueX.upskirt:
        "images/Rogue_sprite/Rogue_standing_bottom[RogueX.outfit[bottom]]_up.png"
    elif RogueX.outfit["bottom"]:
        "images/Rogue_sprite/Rogue_standing_bottom[RogueX.outfit[bottom]].png"

    if RogueX.outfit["dress"] and RogueX.top_pulled_up and RogueX.upskirt:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_both.png"
    elif RogueX.outfit["dress"] and RogueX.top_pulled_up:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_top.png"
    elif RogueX.outfit["dress"] and RogueX.upskirt:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_bottom.png"
    elif RogueX.outfit["dress"]:
        "images/Rogue_sprite/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose].png"

    # if RogueX.outfit["loincloth"]:
    #     "images/Rogue_sprite/Rogue_standing_loincloth[RogueX.outfit[loincloth]].png"

    # if RogueX.outfit["boots"]:
    #     "images/Rogue_sprite/Rogue_standing_boots[RogueX.outfit[boots]].png"

    if RogueX.outfit["top"] and RogueX.top_pulled_up:
        "images/Rogue_sprite/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose]_up.png"
    elif RogueX.outfit["top"]:
        "images/Rogue_sprite/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose].png"

    # if RogueX.outfit["piercings"] and (((RogueX.outfit["bottom"] or RogueX.outfit["dress"]) and not RogueX.upskirt) or (RogueX.outfit["underwear"] and not RogueX.underwear_pulled_down)):
    #     "images/Rogue_sprite/Rogue_standing_piercings_pussy[RogueX.outfit[piercings]]_covered.png"

    # if RogueX.outfit["piercings"] and (RogueX.outfit["top"] or RogueX.outfit["bra"] or RogueX.["dress"]) and not RogueX.top_pulled_up:
    #     "images/Rogue_sprite/Rogue_standing_piercings_breasts[RogueX.outfit[piercings]]_covered.png"

    # if RogueX.outfit["neck"]:
    #     "images/Rogue_sprite/Rogue_standing_neck[RogueX.outfit[neck]].png"

    # always:
    #     "images/Rogue_sprite/Rogue_standing_hand[RogueX.arm_pose]_left.png"

    # always:
    #     "images/Rogue_sprite/Rogue_standing_hand[RogueX.arm_pose]_right.png"

    # if RogueX.outfit["gloves"]:
    #     "images/Rogue_sprite/Rogue_standing_gloves[RogueX.outfit[gloves]][RogueX.arm_pose].png"

    # if RogueX.outfit["sleeves"]:
    #     "images/Rogue_sprite/Rogue_standing_sleeves[RogueX.outfit[sleeves]][RogueX.arm_pose].png"

    # if (RogueX.outfit["suspenders"] and RogueX.outfit["bottom"] and not RogueX.upskirt and RogueX.top_pulled_up):
    #     "images/Rogue_sprite/Rogue_standing_suspenders[RogueX.outfit[suspenders]][RogueX.arm_pose]_up.png"
    # elif RogueX.outfit["suspenders"] and RogueX.outfit["bottom"] and not RogueX.upskirt:
    #     "images/Rogue_sprite/Rogue_standing_suspenders[RogueX.outfit[suspenders]][RogueX.arm_pose].png"

    # if RogueX.outfit["scarf"]:
    #     "images/Rogue_sprite/Rogue_standing_scarf[RogueX.outfit[scarf]].png"

    # if RogueX.outfit["jackets"]:
    #     "images/Rogue_sprite/Rogue_standing_jackets[RogueX.outfit[jackets]].png"

    # if RogueX.outfit["cloaks"]:
    #     "images/Rogue_sprite/Rogue_standing_cloaks[RogueX.outfit[cloaks]].png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_sprite/Rogue_standing_spunk_breasts.png"

    if RogueX.spunk["belly"]:
        "images/Rogue_sprite/Rogue_standing_spunk_belly.png"

    if RogueX.spunk["hand"] and RogueX.arm_pose == 2:
        "images/Rogue_sprite/Rogue_standing_spunk_hand.png"

    if RogueX.wet and RogueX.wet < 3:
        "images/Rogue_sprite/Rogue_standing_water_body[RogueX.arm_pose].png"

    if RogueX.wet == 3:
        "images/Rogue_sprite/Rogue_standing_soap_body.png"

    if RogueX.outfit["held_item"] and RogueX.arm_pose == 2:
        "images/Rogue_sprite/Rogue_standing_held[RogueX.outfit[held_item]].png"

    # always:
    #     "Rogue_standing_fondling_animations"

    anchor (0.5, 0.0) offset (0, 180) zoom 0.95

image Rogue_back_hair:
    "images/Rogue_blowjob/Rogue_blowjob_back_hair[RogueX.outfit[back_hair]].png"

    anchor (0.5, 0.5)

layeredimage Rogue_head:
    if action_speed and renpy.showing("Rogue_blowjob_animation"):
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing]_sucking.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing].png"

    # if RogueX.outfit["face_piercings"]:
    #     "images/Rogue_sprite/Rogue_standing_face_piercings[RogueX.outfit[face_piercings]].png"

    if RogueX.blushing:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows]_blush.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows].png"

    if renpy.showing("Rogue_blowjob_animation") and action_speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_licking.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed >= 3:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed:
        Null()
    elif RogueX.mouth == "_smirk":
        "images/Rogue_blowjob/Rogue_blowjob_mouth_smile.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth[RogueX.mouth].png"

    if RogueX.spunk["mouth"] and renpy.showing("Rogue_blowjob_animation") and action_speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_tongue.png"
    elif RogueX.spunk["mouth"] and renpy.showing("Rogue_blowjob_animation") and action_speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_sucking.png"
    elif RogueX.spunk["mouth"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk[RogueX.mouth].png"

    if renpy.showing("Rogue_blowjob_animation") and action_speed == 2:
        "Rogue_blowjob_mouth_animations"

    if RogueX.eyes == "_closed":
        "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    elif RogueX.eyes == "_squint":
        "Rogue_squinting"
    else:
        "Rogue_blinking"

    # if RogueX.outfit["face_inner_accessory"]:
    #     "images/Rogue_sprite/Rogue_standing_face_inner_accessory[RogueX.outfit[face_inner_accessory]].png"

    if RogueX.spunk["chin"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_chin.png"

    if RogueX.spunk["mouth"] and renpy.showing("Rogue_blowjob_animation") and action_speed >= 3:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face_sucking_over.png"

    if RogueX.spunk["face"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face.png"

    always:
        "images/Rogue_blowjob/Rogue_blowjob_hair[RogueX.outfit[hair]].png"

    if RogueX.spunk["hair"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_hair.png"

    # if RogueX.outfit["face_outer_accessory"]:
    #     "images/Rogue_sprite/Rogue_standing_face_outer_accessory[RogueX.outfit[face_outer_accessory]].png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_water_head.png"

    anchor (0.5, 0.5)

image Rogue_handjob_under:
    "images/Rogue_handjob/Rogue_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Rogue_handjob_over:
    "images/Rogue_handjob/Rogue_handjob_hand_over.png"

    anchor (0.5, 0.5)

layeredimage Rogue_titjob_under:
    always:
        "Rogue_back_hair" pos (0.545, -0.02) zoom 0.9

    always:
        "images/Rogue_blowjob/Rogue_titjob_body.png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_blowjob/Rogue_titjob_spunk_breasts_under.png"

    always:
        "Rogue_head" pos (0.28, -0.09) zoom 0.9

    anchor (0.5, 0.5)

layeredimage Rogue_titjob_over:
    always:
        "images/Rogue_blowjob/Rogue_titjob_breasts[RogueX.outfit[piercings]].png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_blowjob/Rogue_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Rogue_sex_body:
    always:
        "Rogue_back_hair" pos (0.397, 0.07) rotate -10 zoom 0.37

    always:
        "images/Rogue_sex/Rogue_sex_body[RogueX.outfit[piercings]].png"

    if RogueX.outfit["bra"] and RogueX.top_pulled_up:
        "images/Rogue_sex/Rogue_sex_bra[RogueX.outfit[bra]]_up.png"
    elif RogueX.outfit["bra"]:
        "images/Rogue_sex/Rogue_sex_bra[RogueX.outfit[bra]].png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_body.png"

    if RogueX.outfit["top"] and RogueX.top_pulled_up:
        "images/Rogue_sex/Rogue_sex_top[RogueX.outfit[top]]_up.png"
    elif RogueX.outfit["top"]:
        "images/Rogue_sex/Rogue_sex_top[RogueX.outfit[top]].png"

    if RogueX.outfit["piercings"] and (RogueX.outfit["top"] or RogueX.outfit["bra"]) and not RogueX.top_pulled_up:
        "images/Rogue_sex/Rogue_sex_piercings_breasts[RogueX.outfit[piercings]]_covered.png"

    if RogueX.outfit["neck"]:
        "images/Rogue_sex/Rogue_sex_neck[RogueX.outfit[neck]].png"

    if RogueX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly.png"

    if RogueX.spunk["breasts"]:
        "images/Kitty_sex/Kitty_sex_spunk_breasts.png"

    # if "suck_breasts" in [primary_action, offhand_action]:
    #     "licking" offset (450, 270) zoom 0.6
    #
    # if "fondle_breasts" in [primary_action, offhand_action]:
    #     "GropeLeftBreast" offset (320, -130) zoom 1.1

    always:
        "Rogue_head" pos (0.287, 0.075) rotate -10 zoom 0.37

    anchor (0.5, 0.5)

layeredimage Rogue_sex_legs:
    always:
        "images/Rogue_sex/Rogue_sex_legs.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_legs.png"

    if Player.sprite and Player.cock_position == "anal":
        "Rogue_sex_anus_animation[action_speed]"
    elif "finger_ass" in [primary_action, offhand_action]:
        "Rogue_sex_anus_animation0"
    elif primary_action == "dildo_anal":
        "images/Kitty_sex/Kitty_sex_anus_open.png"
    elif RogueX.used_to_anal:
        "images/Rogue_sex/Rogue_sex_anus_loose.png"
    else:
        "images/Rogue_sex/Rogue_sex_anus_tight.png"

    if RogueX.spunk["anus"] and Player.sprite and Player.cock_position != "anal" and action_speed > 1:
        "images/Kitty_sex/Kitty_sex_spunk_anus_under.png"
    elif RogueX.spunk["anus"] and Player.sprite and Player.cock_position != "anal" and action_speed == 1:
        "Rogue_sex_spunk_anus_under"
    elif RogueX.spunk["anus"]:
        "images/Kitty_sex/Kitty_sex_spunk_anus_closed.png"

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_sex_cock_anal_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "finger_ass" in [primary_action, offhand_action]:
        AlphaMask("Zero_sex_finger_ass_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif primary_action == "dildo_anal":
        AlphaMask("dildo_anal_animation", "images/Kitty_sex/Kitty_sex_anus_mask.png")

    if Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"
    elif primary_action == "dildo_pussy":
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif primary_action in pussy_actions or offhand_action in pussy_actions:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"

    if RogueX.grool and Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_grool_fucking.png"
    elif RogueX.grool:
        "images/Kitty_sex/Kitty_sex_pussy_grool.png"

    if RogueX.outfit["piercings"] and Player.sprite or Player.cock_position != "sex" or action_speed <= 1:
        "images/Rogue_sex/Rogue_sex_piercings_pussy[RogueX.outfit[piercings]].png"
    elif RogueX.outfit["piercings"]:
        "images/Rogue_sex/Rogue_sex_piercings_pussy[RogueX.outfit[piercings]]_fucking.png"

    if RogueX.pubes and Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif RogueX.pubes and Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    elif RogueX.pubes and Player.sprite and Player.cock_position == "in":
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"
    elif RogueX.pubes and primary_action == "dildo_pussy":
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif RogueX.pubes and primary_action in pussy_actions or offhand_action in pussy_actions:
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    elif RogueX.pubes:
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"

    if RogueX.spunk["pussy"]:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_sex_cock_animations", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif "fondle_pussy" in [primary_action, offhand_action] or "finger_pussy" in [primary_action, offhand_action]:
        AlphaMask("Zero_sex_finger_pussy_animations", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif primary_action == "dildo_pussy":
        AlphaMask("dildo_pussy_animation", "images/Rogue_sex/Rogue_sex_pussy_mask.png")

    if RogueX.spunk and Player.sprite and Player.cock_position == "sex" and action_speed <= 1:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png" anchor (0.5, 0.5) pos (0.5, 0.5) xzoom 0.8
    elif RogueX.spunk and Player.sprite and Player.cock_position == "sex":
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

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
    elif Player.sprite and Player.cock_position in ["sex", "anal"]:
        Null()
    elif RogueX.outfit["hose"] == "_tights" and RogueX.grool:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]]_grool.png"
    elif RogueX.outfit["hose"]:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]].png"

    if RogueX.outfit["bottom"] == "_pants" and RogueX.grool and not RogueX.upskirt:
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]]_grool.png"
    elif RogueX.outfit["bottom"] and not RogueX.upskirt:
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]].png"

    if RogueX.outfit["scarf"] == "_sweater":
        "images/Rogue_sex/Rogue_scarf[RogueX.outfit[scarf]].png"

    if RogueX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if Player.sprite and Player.cock_position == "out":
        "Zero_sex_cock_hotdog_animations"

    if primary_action == "eat_pussy":
        "licking" offset (530, 510) zoom 0.7
    elif primary_action == "eat_ass":
        "licking" offset (535, 590) zoom 0.7

    if Player.sprite and Player.cock_position == "footjob":
        "Zero_sex_cock_footjob_animations"

    if not action_speed or Player.cock_position == "footjob" or show_feet:
        "Rogue_sex_feet" pos (0.291, 0.391)
    else:
        AlphaMask("Rogue_sex_feet", "images/Rogue_sex/Rogue_sex_feet_mask.png")

    anchor (0.5, 0.5)

layeredimage Rogue_sex_feet:
    always:
        "images/Rogue_sex/Rogue_sex_feet.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_feet.png"

    if RogueX.outfit["hose"] and RogueX.outfit["hose"] != "_garterbelt" and RogueX.underwear_pulled_down:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]]_feet.png"

    if RogueX.outfit["underwear"] and RogueX.underwear_pulled_down and RogueX.outfit["bottom"] != "_pants":
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]]_down.png"

    if RogueX.outfit["bottom"] == "_pants" and RogueX.upskirt:
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]].png"
    elif RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]]_feet.png"

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_body:
    if not RogueX.wet and RogueX.outfit["hair"] == "_evo":
        "images/Rogue_doggy/Rogue_doggy_hair_evo_back.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_body.png"

    if RogueX.outfit["neck"]:
        "images/Rogue_doggy/Rogue_doggy_neck[RogueX.outfit[neck]].png"

    if RogueX.spunk["mouth"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_mouth[RogueX.mouth].png"
    elif RogueX.mouth == "_kiss":
        "images/Rogue_doggy/Rogue_doggy_mouth_surprised.png"
    elif RogueX.mouth == "_smirk":
        "images/Rogue_doggy/Rogue_doggy_mouth_smile.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_mouth[RogueX.mouth].png"

    if RogueX.blushing:
        "images/Rogue_doggy/Rogue_doggy_blush.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_brows[RogueX.brows].png"

    if RogueX.eyes in ["_squint", "_closed"]:
        "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"
    else:
        "Rogue_doggy_blinking"

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

    if RogueX.spunk["hair"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_hair.png"

    if RogueX.spunk["face"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_face.png"

    if primary_action == "fondle_breasts" or offhand_action == "fondle_breasts":
        "Zero_doggy_grope_breast_animation"

    anchor (0.5, 0.5)

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

    if RogueX.pubes and RogueX.outfit["bottom"] == "_pants" and not RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    elif RogueX.pubes and RogueX.outfit["underwear"]:
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    elif RogueX.pubes and RogueX.outfit["hose"] and RogueX.outfit["hose"] != "_stockings":
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    elif RogueX.pubes:
        "images/Rogue_doggy/Rogue_doggy_pubes.png"

    if primary_action == "eat_pussy":
        "images/Rogue_doggy/Rogue_doggy_pussy_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_pussy_closed.png"

    if Player.sprite and Player.cock_position == "in":
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
    elif "finger_pussy" in [primary_action, offhand_action]:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"

    if Player.sprite and Player.cock_position == "in":
        "Rogue_doggy_pussy_hole_animations"
    elif "finger_pussy" in [primary_action, offhand_action]:
        "Rogue_doggy_pussy_fingering"

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_doggy_cock_animations", "Rogue_doggy_pussy_mask_animations")
    elif "finger_pussy" in [primary_action, offhand_action]:
        AlphaMask("Zero_doggy_finger_pussy_animations", "Rogue_doggy_pussy_mask_animation1")
    elif primary_action == "dildo_pussy":
        AlphaMask("doggy_dildo_pussy_animation", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")

    if Player.sprite and Player.cock_position == "in" and action_speed < 2:
        AlphaMask("Rogue_doggy_pussy_outer_animations", "Rogue_doggy_pussy_hole_mask_animations")
    elif "finger_pussy" in [primary_action, offhand_action]:
        AlphaMask("Rogue_doggy_pussy_outer_animation1", "Rogue_doggy_pussy_hole_mask_animation1")

    if RogueX.outfit["piercings"]:
        "images/Rogue_doggy/Rogue_doggy_piercings_pussy[RogueX.outfit[piercings]].png"

    if RogueX.used_to_anal:
        "images/Rogue_doggy/Rogue_doggy_anus_loose.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_anus_tight.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"
    elif "finger_ass" in [primary_action, offhand_action]:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "Rogue_doggy_anus_anal_animations"
    elif "finger_ass" in [primary_action, offhand_action]:
        "Rogue_doggy_anus_fingering"

    if Player.sprite and Player.cock_position == "anal" and action_speed > 1:
        "images/Rogue_doggy/Rogue_doggy_anus_full_cheeks.png"

    if RogueX.outfit["hose"] and not RogueX.underwear_pulled_down:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]].png"

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_doggy_cock_anal_animations", "Rogue_doggy_anus_mask_animations")
    elif "finger_ass" in [primary_action, offhand_action]:
        AlphaMask("Zero_doggy_finger_anal_animations", "Rogue_doggy_anus_fingering_mask")
    elif primary_action == "dildo_anal":
        AlphaMask("doggy_dildo_anal_animation", "images/Rogue_doggy/Rogue_doggy_anus_mask.png")

    if RogueX.spunk["anus"] and Player.cock_position == "anal":
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    elif RogueX.spunk["anus"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_loose.png"

    if RogueX.outfit["underwear"] and not RogueX.underwear_pulled_down and (not Player.sprite or Player.cock_position not in ["sex", "anal"]):
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
        "images/Rogue_doggy/Rogue_doggy_bottom_pants_down.png"
    elif RogueX.outfit["bottom"] == "_pants" and RogueX.grool > 1:
        "images/Rogue_doggy/Rogue_doggy_bottom_pants_grool.png"
    elif RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_doggy/Rogue_doggy_bottom_pants.png"
    elif RogueX.outfit["bottom"] == "_skirt" and RogueX.upskirt and Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Rogue_doggy/Rogue_doggy_bottom_skirt_anal_up.png"
    elif RogueX.outfit["bottom"] == "_skirt" and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_bottom_skirt_up.png"
    elif RogueX.outfit["bottom"] == "_skirt":
        "images/Rogue_doggy/Rogue_doggy_bottom_skirt.png"

    if RogueX.outfit["top"] in ["_nighty", "_towel"] and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]]_ass_up.png"
    elif RogueX.outfit["top"] in ["_nighty", "_towel"]:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]]_ass.png"

    if RogueX.outfit["back_outer_accessory"] and (RogueX.upskirt or (Player.sprite and Player.cock_position == "out")):
        "images/Rogue_doggy/Rogue_doggy_back_outer_accessory[RogueX.outfit[back_outer_accessory]]_up.png"
    elif RogueX.outfit["back_outer_accessory"]:
        "images/Rogue_doggy/Rogue_doggy_back_outer_accessory[RogueX.outfit[back_outer_accessory]].png"

    if RogueX.spunk["back"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_ass.png"

    if primary_action == "eat_pussy":
        "licking" offset (195, 540) zoom 0.5
    elif primary_action == "eat_ass":
        "licking" offset (195, 500) zoom 0.5

    if Player.sprite and Player.cock_position == "out" and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_hotdog_back_up.png"
    elif Player.sprite and Player.cock_position == "out":
        "images/Rogue_doggy/Rogue_doggy_hotdog_back.png"

    if Player.sprite and Player.cock_position == "out":
        AlphaMask("Zero_doggy_cock_hotdog_animations", "images/Rogue_doggy/Rogue_doggy_hotdog_mask_up.png")

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_shins:
    always:
        "images/Rogue_doggy/Rogue_doggy_shins.png"

    if RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_doggy/Rogue_doggy_bottom[RogueX.outfit[bottom]]_feet.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_feet.png"

    if RogueX.outfit["hose"]:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]]_feet.png"

    anchor (0.5, 0.5)

image Rogue_doggy_feet:
    AlphaMask("Rogue_doggy_shins", "images/Rogue_doggy/Rogue_doggy_toes.png")

    anchor (0.5, 0.5)
