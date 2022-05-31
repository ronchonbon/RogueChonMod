layeredimage Rogue_sprite standing:
    # always:
    #     "images/Rogue_standing/Rogue_standing_head_reference.png"

    if RogueX.outfit["jacket"] == "_hoodie":
        "images/Rogue_standing/Rogue_standing_back_outer_accessory[RogueX.outfit[jacket]].png"
    elif RogueX.outfit["cloak"]:
        "images/Rogue_standing/Rogue_standing_back_outer_accessory[RogueX.outfit[cloak]].png"

    if RogueX.outfit["bottom"] == "_pants":
        "images/Rogue_standing/Rogue_standing_back_outer_accessory[RogueX.outfit[bottom]].png"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_back_hair" pos (0.156, 0.158) zoom 0.29

    always:
        "images/Rogue_standing/Rogue_standing_body[RogueX.pubes][RogueX.outfit[piercings]].png"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_head" pos (0.156, 0.158) zoom 0.29

    always:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose][RogueX.outfit[neck]][RogueX.outfit[gloves]].png"

    always:
        "images/Rogue_standing/Rogue_standing_breasts[RogueX.outfit[piercings]].png"

    if RogueX.outfit["bra"] == "_classic":
        "images/Rogue_standing/Rogue_standing_bra[RogueX.outfit[bra]][RogueX.arm_pose].png"
    elif RogueX.outfit["bra"] and RogueX.bra_pulled_up:
        "images/Rogue_standing/Rogue_standing_bra[RogueX.outfit[bra]]_up.png"
    elif RogueX.outfit["bra"]:
        "images/Rogue_standing/Rogue_standing_bra[RogueX.outfit[bra]].png"

    if RogueX.outfit["underwear"] and RogueX.underwear_pulled_down and RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]]_down_grool.png"
    elif RogueX.outfit["underwear"] and RogueX.underwear_pulled_down:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]]_down.png"
    elif RogueX.outfit["underwear"] and RogueX.grool > 1 and RogueX.outfit["underwear"] not in ["_black_panties", "_harness"]:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]]_grool.png"
    elif RogueX.outfit["underwear"]:
        "images/Rogue_standing/Rogue_standing_underwear[RogueX.outfit[underwear]].png"

    if RogueX.outfit["hose"] == "_tights" and RogueX.grool:
        "images/Rogue_standing/Rogue_standing_hose[RogueX.outfit[hose]]_grool.png"
    elif RogueX.outfit["hose"]:
        "images/Rogue_standing/Rogue_standing_hose[RogueX.outfit[hose]].png"

    if RogueX.grool > 1 and RogueX.outfit["bottom"]:
        "images/Rogue_standing/Rogue_standing_grool1.png"
    elif RogueX.grool:
        "images/Rogue_standing/Rogue_standing_grool[RogueX.grool].png"

    always:
        "Rogue_grool_animations"

    always:
        "Rogue_spunk_animations"

    if RogueX.outfit["bottom"] and (RogueX.bottom_pulled_down or RogueX.upskirt):
        "images/Rogue_standing/Rogue_standing_bottom[RogueX.outfit[bottom]]_down.png"
    elif RogueX.outfit["bottom"]:
        "images/Rogue_standing/Rogue_standing_bottom[RogueX.outfit[bottom]].png"

    if RogueX.outfit["dress"] and RogueX.dress_top_pulled_down and RogueX.dress_upskirt:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_both.png"
    elif RogueX.outfit["dress"] and RogueX.dress_top_pulled_down:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_top.png"
    elif RogueX.outfit["dress"] and RogueX.dress_upskirt:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose]_bottom.png"
    elif RogueX.outfit["dress"]:
        "images/Rogue_standing/Rogue_standing_dress[RogueX.outfit[dress]][RogueX.arm_pose].png"

    if RogueX.outfit["top"] and RogueX.top_pulled_up:
        "images/Rogue_standing/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose]_up.png"
    elif RogueX.outfit["top"]:
        "images/Rogue_standing/Rogue_standing_top[RogueX.outfit[top]][RogueX.arm_pose].png"

    if RogueX.outfit["scarf"]:
        "images/Rogue_standing/Rogue_standing_scarf[RogueX.outfit[scarf]][RogueX.arm_pose].png"

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

    if RogueX.wet and RogueX.wet < 3:
        "images/Rogue_standing/Rogue_standing_water_body[RogueX.arm_pose].png"

    if RogueX.wet == 3:
        "images/Rogue_standing/Rogue_standing_soap_body.png"

    if RogueX.outfit["held_item"] and RogueX.arm_pose == 2:
        "images/Rogue_standing/Rogue_standing_held[RogueX.outfit[held_item]].png"

    always:
        "Rogue_standing_fondling_animations"

    anchor (0.5, 0.0) offset (5, 180) zoom 0.95

image Rogue_back_hair:
    "images/Rogue_blowjob/Rogue_blowjob_back_hair[RogueX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Rogue_head:
    if renpy.showing("Rogue_sprite blowjob") and action_speed:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing]_sucking.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing].png"

    if RogueX.blushing:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows]_blush.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_brows[RogueX.brows].png"

    if RogueX.spunk["mouth"] and not renpy.showing("Rogue_sprite blowjob"):
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth[RogueX.mouth].png"
    elif not renpy.showing("Rogue_sprite blowjob"):
        "images/Rogue_blowjob/Rogue_blowjob_mouth[RogueX.mouth].png"

    if renpy.showing("Rogue_sprite blowjob"):
        "Rogue_blowjob_mouth_animations"

    if RogueX.eyes == "_closed":
        "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    else:
        "Rogue_blinking"

    if RogueX.spunk["chin"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_chin.png"

    if RogueX.spunk["mouth"] and renpy.showing("Rogue_sprite blowjob") and action_speed >= 3:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face_sucking_over.png"

    if RogueX.spunk["face"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face.png"

    always:
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

layeredimage Rogue_titjob_under:
    always:
        "Rogue_back_hair" pos (0.28, -0.09) zoom 0.9

    always:
        "images/Rogue_titjob/Rogue_titjob_body.png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_titjob/Rogue_titjob_spunk_breasts_under.png"

    always:
        "Rogue_head" pos (0.28, -0.09) zoom 0.9

    anchor (0.5, 0.5)

layeredimage Rogue_titjob_over:
    always:
        "images/Rogue_titjob/Rogue_titjob_breasts[RogueX.outfit[piercings]].png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_titjob/Rogue_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Rogue_sex_body:
    always:
        "Rogue_back_hair" pos (0.287, 0.075) rotate -10 zoom 0.37

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

    if "suck_breasts" in [primary_action, offhand_action]:
        "licking" offset (470, 295) zoom 0.6

    if "fondle_breasts" in [primary_action, offhand_action]:
        "Zero_fondle_breasts_left_animation" offset (485, 330) zoom 1.1

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
    elif primary_action == "dildo_ass":
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
        AlphaMask("Rogue_sex_cock_anal_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "finger_ass" in [primary_action, offhand_action]:
        AlphaMask("Rogue_sex_finger_ass_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif primary_action == "dildo_ass":
        AlphaMask("Rogue_dildo_anal_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")

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

    if RogueX.outfit["piercings"] and (Player.sprite or Player.cock_position != "in" or action_speed <= 1):
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
        AlphaMask("Rogue_sex_cock_animations", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif "fondle_pussy" in [primary_action, offhand_action] or "finger_pussy" in [primary_action, offhand_action]:
        AlphaMask("Rogue_sex_finger_pussy_animations", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif primary_action == "dildo_pussy":
        AlphaMask("Rogue_dildo_pussy_animations", "images/Rogue_sex/Rogue_sex_pussy_mask.png")

    if RogueX.spunk["pussy"] and Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

    if not RogueX.outfit["underwear"] or RogueX.underwear_pulled_down:
        Null()
    elif Player.sprite and Player.cock_position in ["in", "anal"]:
        Null()
    elif RogueX.grool and RogueX.outfit["underwear"] not in ["_lace_panties", "_harness"]:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]]_grool.png"
    else:
        "images/Rogue_sex/Rogue_sex_underwear[RogueX.outfit[underwear]].png"

    if RogueX.underwear_pulled_down:
        Null()
    elif Player.sprite and Player.cock_position in ["in", "anal"]:
        Null()
    elif RogueX.outfit["hose"] == "_tights" and RogueX.grool:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]]_grool.png"
    elif RogueX.outfit["hose"]:
        "images/Rogue_sex/Rogue_sex_hose[RogueX.outfit[hose]].png"

    if RogueX.outfit["bottom"] == "_pants" and RogueX.grool and not RogueX.bottom_pulled_down:
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]]_grool.png"
    elif RogueX.outfit["bottom"] and not RogueX.bottom_pulled_down:
        "images/Rogue_sex/Rogue_sex_bottom[RogueX.outfit[bottom]].png"

    if RogueX.outfit["scarf"] == "_sweater":
        "images/Rogue_sex/Rogue_scarf[RogueX.outfit[scarf]].png"

    if RogueX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if Player.sprite and Player.cock_position == "out":
        "Rogue_sex_cock_hotdog_animations"

    if primary_action == "eat_pussy":
        "licking" offset (560, 510) zoom 0.7
    elif primary_action == "eat_ass":
        "licking" offset (560, 590) zoom 0.7

    if Player.sprite and Player.cock_position == "footjob":
        "Rogue_sex_cock_footjob_animations"

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
        "Zero_doggy_fondle_breast_animation"

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
        AlphaMask("Rogue_doggy_cock_animations", "Rogue_doggy_pussy_mask_animations")
    elif "finger_pussy" in [primary_action, offhand_action]:
        AlphaMask("Rogue_doggy_finger_pussy_animations", "Rogue_doggy_pussy_mask_animation1")
    elif primary_action == "dildo_pussy":
        AlphaMask("Rogue_doggy_dildo_pussy_animations", "images/Rogue_doggy/Rogue_doggy_sex_mask.png")

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
        AlphaMask("Rogue_doggy_cock_anal_animations", "Rogue_doggy_anus_mask_animations")
    elif "finger_ass" in [primary_action, offhand_action]:
        AlphaMask("Rogue_doggy_finger_anal_animations", "Rogue_doggy_anus_fingering_mask")
    elif primary_action == "dildo_ass":
        AlphaMask("Rogue_doggy_dildo_anal_animations", "images/Rogue_doggy/Rogue_doggy_anus_mask.png")

    if RogueX.spunk["anus"] and Player.cock_position == "anal":
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    elif RogueX.spunk["anus"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_loose.png"

    if RogueX.outfit["underwear"] and not RogueX.underwear_pulled_down and (not Player.sprite or Player.cock_position not in ["in", "anal"]):
        "images/Rogue_doggy/Rogue_doggy_underwear[RogueX.outfit[underwear]].png"

    if Player.sprite and Player.cock_position in ["in", "anal"]:
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
        AlphaMask("Rogue_doggy_cock_hotdog_animations", "images/Rogue_doggy/Rogue_doggy_hotdog_mask_up.png")

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
