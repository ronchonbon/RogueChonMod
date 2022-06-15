layeredimage Rogue_sprite standing:
    # always:
    #     "images/Rogue_standing/Rogue_standing_head_reference.png"

    if RogueX.outfit["jacket"] == "_hoodie":
        "images/Rogue_standing/Rogue_standing_back_outer_accessory[RogueX.outfit[jacket]].png"
    elif RogueX.outfit["cloak"]:
        "images/Rogue_standing/Rogue_standing_back_outer_accessory[RogueX.outfit[cloak]].png"

    if RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_standing/Rogue_standing_back_outer_accessory[RogueX.outfit[bottom]].png"

    if renpy.showing("Rogue_sprite titjob") or renpy.showing("Rogue_sprite blowjob"):
        Null()
    else:
        "Rogue_back_hair" pos (0.156, 0.158) zoom 0.29

    always:
        "images/Rogue_standing/Rogue_standing_body[RogueX.pubes][RogueX.outfit[piercings]].png"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_head" pos (0.156, 0.158) zoom 0.29

    always:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose][RogueX.outfit[neck]][RogueX.outfit[gloves]].png"

    always:
        "images/Rogue_standing/Rogue_standing_breasts[RogueX.outfit[piercings]].png"

    if not RogueX.outfit["bra"]:
        Null()
    elif RogueX.outfit["bra"] == "_classic":
        "images/Rogue_standing/Rogue_standing_bra[RogueX.outfit[bra]][RogueX.arm_pose].png"
    elif RogueX.bra_pulled_up:
        "images/Rogue_standing/Rogue_standing_bra[RogueX.outfit[bra]]_up.png"
    else:
        "images/Rogue_standing/Rogue_standing_bra[RogueX.outfit[bra]].png"

    if not RogueX.outfit["underwear"]:
        Null()
    elif RogueX.underwear_pulled_down and RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]]_down_grool.png"
    elif RogueX.underwear_pulled_down:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]]_down.png"
    elif RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]]_grool.png"
    else:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]].png"

    if not RogueX.outfit["hose"] or RogueX.underwear_pulled_down:
        Null()
    elif RogueX.outfit["hose"] == "_tights" and RogueX.grool > 1:
        "images/Rogue_standing/Rogue_standing_hose[RogueX.outfit[hose]]_grool.png"
    else:
        "images/Rogue_standing/Rogue_standing_hose[RogueX.outfit[hose]].png"

    if RogueX.outfit["bottom"] and RogueX.grool > 1:
        "images/Rogue_standing/Rogue_standing_grool1.png"
    elif RogueX.grool:
        "images/Rogue_standing/Rogue_standing_grool[RogueX.grool].png"

    always:
        "Rogue_grool_animations"

    always:
        "Rogue_spunk_animations"

    if not RogueX.outfit["bottom"]:
        Null()
    elif RogueX.bottom_pulled_down or RogueX.upskirt:
        "images/Rogue_standing/Rogue_standing_bottom[RogueX.outfit[bottom]]_down.png"
    else:
        "images/Rogue_standing/Rogue_standing_bottom[RogueX.outfit[bottom]].png"

    if not RogueX.outfit["dress"]:
        Null()
    elif RogueX.dress_top_pulled_down and RogueX.dress_upskirt:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_both.png"
    elif RogueX.dress_top_pulled_down:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_top.png"
    elif RogueX.dress_upskirt:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_bottom.png"
    else:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose].png"

    if not RogueX.outfit["top"]:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue_standing/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose]_up.png"
    else:
        "images/Rogue_standing/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose].png"

    if RogueX.outfit["belt"]:
        "images/Rogue_standing/Rogue_standing_belt[RogueX.outfit[belt]][RogueX.arm_pose].png"

    if RogueX.outfit["jacket"]:
        "images/Rogue_standing/Rogue_standing_jacket[RogueX.outfit[jacket]][RogueX.arm_pose].png"

    if RogueX.outfit["cloak"]:
        "images/Rogue_standing/Rogue_standing_cloak[RogueX.outfit[cloak]][RogueX.arm_pose].png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_standing/Rogue_standing_spunk_breasts.png"

    if RogueX.spunk["belly"]:
        "images/Rogue_standing/Rogue_standing_spunk_belly.png"

    if RogueX.spunk["hand"] and RogueX.arm_pose == 2:
        "images/Rogue_standing/Rogue_standing_spunk_hand.png"

    if RogueX.wet:
        "images/Rogue_standing/Rogue_standing_water_body[RogueX.arm_pose].png"

    if RogueX.wet == 3:
        "images/Rogue_standing/Rogue_standing_soap_body.png"

    if RogueX.outfit["held_item"] and RogueX.arm_pose == 2:
        "images/Rogue_standing/Rogue_standing_held[RogueX.outfit[held_item]].png"

    # always:
    #     "Rogue_standing_fondling_animations"

    anchor (0.5, 0.0) offset (5, 180) zoom 0.95

layeredimage Rogue_back_hair:
    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_back_hair_wet.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_back_hair[RogueX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Rogue_head:
    if renpy.showing("Rogue_sprite blowjob") and action_speed:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing]_sucking.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing].png"

    if renpy.showing("Rogue_sprite titjob") and action_speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and action_speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and action_speed > 1:
        "Rogue_blowjob_mouth_animation[action_speed]" pos (0.164, 0.55)
    elif RogueX.mouth == "_sucking":
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth[RogueX.mouth].png"

    if not RogueX.spunk["mouth"]:
        Null()
    elif renpy.showing("Rogue_sprite titjob") and action_speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and action_speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and action_speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_under.png"
    elif RogueX.mouth == "_sucking":
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth[RogueX.mouth].png"

    if RogueX.spunk["chin"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_chin.png"

    if RogueX.blushing:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows]_blush.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows].png"

    if RogueX.eyes == "_closed":
        "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    else:
        "Rogue_blinking"

    if RogueX.spunk["mouth"] and renpy.showing("Rogue_sprite blowjob") and action_speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_over.png"

    if RogueX.spunk["face"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face.png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_hair_wet.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_hair[RogueX.outfit[hair]].png"

    if RogueX.spunk["hair"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_hair.png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_water_head.png"

    anchor (0.5, 0.5)

image Rogue_handjob_under:
    "images/Rogue_handjob/Rogue_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Rogue_handjob_over:
    "images/Rogue_handjob/Rogue_handjob_hand_over.png"

    anchor (0.5, 0.5)

layeredimage Rogue_titjob_body:
    always:
        "images/Rogue_titjob/Rogue_titjob_body.png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_titjob/Rogue_titjob_spunk_breasts_under.png"

    anchor (0.5, 0.5)

layeredimage Rogue_titjob_breasts:
    always:
        "images/Rogue_titjob/Rogue_titjob_breasts[RogueX.outfit[piercings]].png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_titjob/Rogue_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Rogue_blowjob_mouth:
    if RogueX.spunk["mouth"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_under.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"

    anchor (0.4, 0.65)

image Rogue_blowjob_mask:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"

    anchor (0.4, 0.65) pos (0.402, 0.645)

layeredimage Rogue_sex_body:
    always:
        "Rogue_back_hair" pos (0.287, 0.075) rotate -10 zoom 0.37

    always:
        "images/Rogue_sex/Rogue_sex_body[RogueX.outfit[piercings]].png"

    if not RogueX.outfit["bra"]:
        Null()
    elif RogueX.bra_pulled_up:
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

    if RogueX.outfit["piercings"] and RogueX.breasts_covered:
        "images/Rogue_sex/Rogue_sex_piercings_breasts[RogueX.outfit[piercings]]_covered.png"

    if RogueX.outfit["neck"]:
        "images/Rogue_sex/Rogue_sex_neck[RogueX.outfit[neck]].png"

    if RogueX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly.png"

    if RogueX.spunk["breasts"]:
        "images/Kitty_sex/Kitty_sex_spunk_breasts.png"

    if "suck_breasts" in [Player.primary_action, Player.secondary_action]:
        "licking" offset (0.245, 0.273) zoom 0.6

    if "fondle_breasts" in [Player.primary_action, Player.secondary_action]:
        "Zero_fondle_breasts_left_animation" offset (0.245, 306) zoom 1.1

    always:
        "Rogue_head" pos (0.287, 0.075) rotate -10 zoom 0.37

    anchor (0.5, 0.5)

layeredimage Rogue_sex_legs:
    always:
        "images/Rogue_sex/Rogue_sex_legs.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_legs.png"

    if Player.sprite and Player.cock_position == "anal":
        "Rogue_sex_anus_animation[action_speed]" pos (0.292, 0.386)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_sex_anus" pos (0.292, 0.386) xzoom 0.6
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_sex_anus" pos (0.292, 0.386) xzoom 0.9
    elif RogueX.used_to_anal:
        "images/Rogue_sex/Rogue_sex_anus_loose.png"
    else:
        "images/Rogue_sex/Rogue_sex_anus_tight.png"

    if not RogueX.spunk["anus"]:
        Null()
    elif Player.sprite and Player.cock_position == "anal" and action_speed > 1:
        "Rogue_sex_spunk_anus_under" pos (0.292, 0.386)
    elif Player.sprite and Player.cock_position == "anal" and action_speed == 1:
        "Rogue_sex_spunk_anus_under_animation" pos (0.292, 0.386)
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anus_closed.png"

    if Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"

    if not RogueX.grool:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_grool_fucking.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_grool.png"

    if not RogueX.outfit["piercings"]:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Rogue_sex/Rogue_sex_piercings_pussy[RogueX.outfit[piercings]]_fucking.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_sex/Rogue_sex_piercings_pussy[RogueX.outfit[piercings]]_fucking.png"
    else:
        "images/Rogue_sex/Rogue_sex_piercings_pussy[RogueX.outfit[piercings]].png"

    if not RogueX.pubes:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"

    if RogueX.spunk["pussy"]:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if not RogueX.outfit["underwear"] or RogueX.underwear_pulled_down:
        Null()
    elif RogueX.grool and RogueX.outfit["underwear"] not in ["_lace_panties", "_bikini_bottoms", "_harness"]:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]]_grool.png"
    else:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]].png"

    if not RogueX.outfit["hose"] or RogueX.underwear_pulled_down:
        Null()
    elif RogueX.outfit["hose"] == "_tights" and RogueX.grool > 1:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]]_grool.png"
    else:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]].png"

    if not RogueX.outfit["bottom"] or RogueX.bottom_pulled_down or RogueX.upskirt:
        Null()
    elif RogueX.outfit["bottom"] == "_pants" and RogueX.grool > 1:
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]]_grool.png"
    else:
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]].png"

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_cock_Rogue", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Rogue", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Rogue", "images/Kitty_sex/Kitty_sex_anus_mask.png")

    if not RogueX.spunk["anus"]:
        Null()
    elif not Player.sprite or Player.cock_position != "anal":
        Null()
    elif action_speed == 1:
        "Rogue_sex_spunk_anus_over_animation" pos (0.292, 0.386)
    else:
        "Rogue_sex_spunk_anus_over" pos (0.292, 0.386)

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_cock_Rogue", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif "fondle_pussy" in [Player.primary_action, Player.secondary_action] or "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Rogue", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Rogue", "images/Rogue_sex/Rogue_sex_pussy_mask.png")

    if not RogueX.spunk["pussy"]:
        Null()
    elif not Player.sprite or Player.cock_position != "in":
        Null()
    elif action_speed <= 1:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png" offset (111, 0) xzoom 0.8
    else:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

    if RogueX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if Player.sprite and Player.cock_position == "out":
        "Zero_cock_Rogue"

    if Player.primary_action == "eat_pussy":
        "licking" pos (0.292, 0.474) zoom 0.7
    elif Player.primary_action == "eat_ass":
        "licking" pos (0.292, 0.548) zoom 0.7

    if Player.sprite and Player.cock_position == "footjob":
        "Zero_cock_Rogue"

    if Player.cock_position == "footjob" or show_feet:
        "Rogue_sex_feet" pos (0.291, 0.391)
    else:
        AlphaMask("Rogue_sex_feet", "images/Rogue_sex/Rogue_sex_feet_mask.png")

    anchor (0.5, 0.5)

layeredimage Rogue_sex_feet:
    always:
        "images/Rogue_sex/Rogue_sex_feet.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_feet.png"

    if RogueX.outfit["hose"] and RogueX.outfit["hose"] != "_garterbelt" and not RogueX.underwear_pulled_down:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]]_feet.png"

    if RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]]_down.png"

    if RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]]_feet.png"

    anchor (0.5, 0.5)

image Rogue_sex_anus:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

image Rogue_sex_spunk_anus_under:
    "images/Kitty_sex/Kitty_sex_spunk_anus_under.png"

    anchor (0.5, 0.5)

image Rogue_sex_spunk_anus_over:
    "images/Kitty_sex/Kitty_sex_spunk_anus_over.png"

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_body:
    if RogueX.outfit["hair"] == "_evo":
        "images/Rogue_doggy/Rogue_doggy_back_hair.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_body.png"

    if RogueX.outfit["neck"]:
        "images/Rogue_doggy/Rogue_doggy_neck[RogueX.outfit[neck]].png"

    if RogueX.spunk["mouth"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_mouth[RogueX.mouth].png"
    else:
        "images/Rogue_doggy/Rogue_doggy_mouth[RogueX.mouth].png"

    if RogueX.blushing:
        "images/Rogue_doggy/Rogue_doggy_blush.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_brows[RogueX.brows].png"

    if RogueX.eyes == "_closed":
        "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"
    else:
        "Rogue_doggy_blinking"

    if RogueX.outfit["bra"]:
        "images/Rogue_doggy/Rogue_doggy_bra[RogueX.outfit[bra]].png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_water_top.png"

    if RogueX.outfit["top"]:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]].png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_hair_wet.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_hair[RogueX.outfit[hair]].png"

    if RogueX.outfit["jacket"] == "_hoodie":
        "images/Rogue_doggy/Rogue_doggy_jacket_hood.png"

    if RogueX.spunk["hair"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_hair.png"

    if RogueX.spunk["face"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_face.png"

    if "fondle_breasts" in [Player.primary_action, Player.secondary_action]:
        "Zero_doggy_fondle_breast_animation"

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_ass:
    if RogueX.outfit["underwear"] and RogueX.underwear_pulled_down and RogueX.outfit["underwear"] != "_harness":
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]]_back.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_ass.png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_water_ass.png"

    if RogueX.outfit["hose"] == "_stockings":
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]].png"

    if not RogueX.outfit["underwear"] or not RogueX.underwear_pulled_down:
        Null()
    elif RogueX.grool > 1 and RogueX.outfit["underwear"] == "_green_panties":
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]]_down_grool.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]]_down.png"

    if not RogueX.pubes:
        Null()
    elif RogueX.outfit["bottom"] == "_pants" and not RogueX.bottom_pulled_down:
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    elif RogueX.outfit["underwear"]:
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    elif RogueX.outfit["hose"] and RogueX.outfit["hose"] != "_stockings":
        "images/Rogue_doggy/Rogue_doggy_pubes_underwear.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_pubes.png"

    if Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Rogue_doggy/Rogue_doggy_pussy_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_pussy_closed.png"

    if Player.sprite and Player.cock_position == "in":
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"

    if Player.sprite and Player.cock_position == "in":
        "Rogue_doggy_pussy_hole_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_pussy_hole_fingering" pos (0.113, 0.475)
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_pussy_hole_animation1" pos (0.113, 0.475)

    if RogueX.outfit["piercings"]:
        "images/Rogue_doggy/Rogue_doggy_piercings_pussy[RogueX.outfit[piercings]].png"

    if RogueX.used_to_anal:
        "images/Rogue_doggy/Rogue_doggy_anus_loose.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_anus_tight.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "Rogue_doggy_anus_anal_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_anus_fingering_animation" pos (0.113, 0.475)
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "Rogue_doggy_anus_anal_animation1" pos (0.113, 0.475)

    if Player.sprite and Player.cock_position == "anal" and action_speed > 1:
        "images/Rogue_doggy/Rogue_doggy_anus_full_cheeks.png"

    if RogueX.outfit["hose"] and not RogueX.underwear_pulled_down:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]].png"

    if not RogueX.spunk["anus"]:
        Null()
    elif Player.cock_position == "anal" and action_speed:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_loose.png"

    if RogueX.outfit["underwear"] and not RogueX.underwear_pulled_down:
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]].png"

    if not RogueX.outfit["hose"] or RogueX.underwear_pulled_down:
        Null()
    elif RogueX.outfit["hose"] == "_tights" and RogueX.grool > 1:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]]_grool.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]].png"

    if RogueX.outfit["bottom"] not in ["_pants", "_skirt"]:
        Null()
    elif RogueX.outfit["bottom"] == "_pants" and RogueX.bottom_pulled_down:
        "images/Rogue_doggy/Rogue_doggy_bottom_pants_down.png"
    elif RogueX.outfit["bottom"] == "_pants" and RogueX.grool > 1:
        "images/Rogue_doggy/Rogue_doggy_bottom_pants_grool.png"
    elif RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_doggy/Rogue_doggy_bottom_pants.png"
    elif RogueX.upskirt and Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Rogue_doggy/Rogue_doggy_bottom_skirt_anal_down.png"
    elif RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_bottom_skirt_down.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_bottom_skirt.png"

    if RogueX.outfit["top"] not in ["_nighty", "_towel"]:
        Null()
    elif RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]]_ass_up.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_top[RogueX.outfit[top]]_ass.png"

    if not RogueX.outfit["belt"]:
        Null()
    elif RogueX.upskirt or (Player.sprite and Player.cock_position == "out"):
        "images/Rogue_doggy/Rogue_doggy_belt[RogueX.outfit[belt]]_up.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_belt[RogueX.outfit[belt]].png"

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_cock_Rogue", "Zero_cock_Rogue_mask")
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Rogue", "Zero_finger_Rogue_mask")
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Rogue", "dildo_Rogue_mask")

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_cock_Rogue", "Zero_cock_Rogue_mask")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Rogue", "Zero_finger_Rogue_mask")
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Rogue", "dildo_Rogue_mask")

    if RogueX.spunk["back"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_ass.png"

    if Player.primary_action == "eat_pussy":
        "licking" offset (195, 540) zoom 0.5
    elif Player.primary_action == "eat_ass":
        "licking" offset (195, 500) zoom 0.5

    if not Player.sprite or Player.cock_position != "out":
        Null()
    elif RogueX.upskirt:
        "images/Rogue_doggy/Rogue_doggy_hotdog_back_up.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_hotdog_back.png"

    if not Player.sprite or Player.cock_position != "out":
        Null()
    elif RogueX.upskirt:
        AlphaMask("Zero_cock_Rogue", "images/Rogue_doggy/Rogue_doggy_hotdog_mask_up.png")
    else:
        AlphaMask("Zero_cock_Rogue", "images/Rogue_doggy/Rogue_doggy_hotdog_mask.png")

    anchor (0.5, 0.5)

image Rogue_doggy_pussy_hole:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_hole:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"

    anchor (0.515, 0.69)

image Rogue_doggy_pussy_mask:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_mask:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    anchor (0.52, 0.69)

layeredimage Rogue_doggy_shins:
    always:
        "images/Rogue_doggy/Rogue_doggy_shins.png"

    if RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_doggy/Rogue_doggy_bottom[RogueX.outfit[bottom]]_feet.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_feet.png"

    if RogueX.outfit["hose"] and RogueX.outfit["hose"] != "_garterbelt":
        "images/Rogue_doggy/Rogue_doggy_hose[RogueX.outfit[hose]]_feet.png"

    anchor (0.5, 0.5)

image Rogue_doggy_feet:
    AlphaMask("Rogue_doggy_shins", "images/Rogue_doggy/Rogue_doggy_toes.png")

    anchor (0.5, 0.5)
