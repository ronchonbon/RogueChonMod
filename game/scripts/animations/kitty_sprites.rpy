layeredimage Kitty_sprite standing:
    if KittyX.outfit["bottom"] == "_dress_skirt":
        "images/Kitty_standing/Kitty_standing_bottom[KittyX.outfit[bottom]]_back.png"

    always:
        "Kitty_hair_back" pos (0.24, 0.3) zoom 0.5

    if KittyX.outfit["buttplug"]:
        "images/Kitty_standing/Kitty_standing_buttplug[KittyX.outfit[buttplug]].png"

    always:
        "images/Kitty_standing/Kitty_standing_arms[KittyX.arm_pose][KittyX.outfit[gloves]].png"

    always:
        "images/Kitty_standing/Kitty_standing_body[KittyX.pubes][KittyX.arm_pose].png"

    always:
        "images/Kitty_standing/Kitty_standing_breasts.png"

    if KittyX.outfit["piercings"]:
        "images/Kitty_standing/Kitty_standing_piercings_breasts[KittyX.outfit[piercings]].png"

    if KittyX.outfit["piercings"]:
        "images/Kitty_standing/Kitty_standing_piercings_pussy[KittyX.outfit[piercings]].png"

    if not KittyX.outfit["bra"]:
        Null()
    # elif KittyX.outfit["top"] and KittyX.bra_pulled_up:
    #     "images/Kitty_standing/Kitty_standing_bra[KittyX.outfit[bra]][KittyX.arm_pose]_strapless_up.png"
    elif KittyX.bra_pulled_up:
        "images/Kitty_standing/Kitty_standing_bra[KittyX.outfit[bra]][KittyX.arm_pose]_up.png"
    else:
        "images/Kitty_standing/Kitty_standing_bra[KittyX.outfit[bra]][KittyX.arm_pose].png"

    if not KittyX.outfit["underwear"]:
        Null()
    elif KittyX.underwear_pulled_down and KittyX.grool > 1:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]]_down_grool.png"
    elif KittyX.underwear_pulled_down:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]]_down.png"
    elif KittyX.grool:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]]_grool.png"
    else:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]].png"

    if KittyX.outfit["hose"] and not KittyX.hose_pulled_down:
        "images/Kitty_standing/Kitty_standing_hose[KittyX.outfit[hose]].png"

    if KittyX.outfit["bottom"] and KittyX.grool > 1:
        "images/Kitty_standing/Kitty_standing_grool1.png"
    elif KittyX.grool:
        "images/Kitty_standing/Kitty_standing_grool[KittyX.grool].png"

    always:
        "Kitty_grool_animations"

    if KittyX.spunk["pussy"]:
        "images/Kitty_standing/Kitty_standing_spunk_anus.png"

    if KittyX.spunk["anus"]:
        "images/Kitty_standing/Kitty_standing_spunk_pussy.png"

    always:
        "Kitty_spunk_animations"

    if not KittyX.outfit["bottom"]:
        Null()
    elif KittyX.bottom_pulled_down and KittyX.outfit["bottom"] == "_capris":
        Null()
    elif KittyX.bottom_pulled_down or KittyX.upskirt:
        "images/Kitty_standing/Kitty_standing_bottom[KittyX.outfit[bottom]]_down.png"
    elif KittyX.grool > 1 and KittyX.outfit["bottom"] in ["_shorts", "_yoga_pants", "_black_and_blue_pants"]:
        "images/Kitty_standing/Kitty_standing_bottom[KittyX.outfit[bottom]]_grool.png"
    else:
        "images/Kitty_standing/Kitty_standing_bottom[KittyX.outfit[bottom]].png"

    if KittyX.outfit["neck"]:
        "images/Kitty_standing/Kitty_standing_neck[KittyX.outfit[neck]].png"

    if not KittyX.outfit["dress"]:
        Null()
    elif KittyX.dress_top_pulled_down and KittyX.dress_upskirt:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_both.png"
    elif KittyX.dress_top_pulled_down:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_top.png"
    elif KittyX.dress_upskirt:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_bottom.png"
    else:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose].png"

    if not KittyX.outfit["top"]:
        Null()
    elif KittyX.top_pulled_up:
        "images/Kitty_standing/Kitty_standing_top[KittyX.outfit[top]][KittyX.arm_pose]_up.png"
    else:
        "images/Kitty_standing/Kitty_standing_top[KittyX.outfit[top]][KittyX.arm_pose].png"

    # if KittyX.outfit["bra"] and KittyX.outfit["top"] and KittyX.top_pulled_up:
    #     "images/Kitty_standing/Kitty_standing_bra[KittyX.outfit[bra]]_over.png"

    if KittyX.outfit["piercings"] and KittyX.breasts_covered:
        "images/Kitty_standing/Kitty_standing_piercings_breasts[KittyX.outfit[piercings]]_covered.png"

    if not KittyX.outfit["jacket"]:
        Null()
    elif KittyX.jacket_opened:
        "images/Kitty_standing/Kitty_standing_jacket[KittyX.outfit[jacket]][KittyX.arm_pose]_open.png"
    else:
        "images/Kitty_standing/Kitty_standing_jacket[KittyX.outfit[jacket]][KittyX.arm_pose].png"

    always:
        "Kitty_head" pos (0.24, 0.3) zoom 0.5

    if KittyX.spunk["breasts"]:
        "images/Kitty_standing/Kitty_standing_spunk_breasts.png"

    if KittyX.spunk["belly"]:
        "images/Kitty_standing/Kitty_standing_spunk_belly.png"

    if KittyX.spunk["hand"] and KittyX.arm_pose == 2:
        "images/Kitty_standing/Kitty_standing_spunk_hand.png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_water_body[KittyX.arm_pose].png"

    if KittyX.outfit["held_item"] and KittyX.arm_pose == 2:
        "images/Kitty_standing/Kitty_standing_held[KittyX.outfit[held_item]].png"

    always:
        "Kitty_standing_fondling_animations" pos (-0.002, -0.035) zoom 1.03

    anchor (0.5, 0.0) offset (40, 175) zoom 0.485

layeredimage Kitty_hair_back:
    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_hair_wet_back.png"
    elif KittyX.outfit["hair"] != "_evo":
        "images/Kitty_standing/Kitty_standing_hair[KittyX.outfit[hair]]_back.png"

    anchor (0.5, 0.5)

layeredimage Kitty_head:
    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_face_wet[KittyX.blushing].png"
    else:
        "images/Kitty_standing/Kitty_standing_face[KittyX.outfit[hair]][KittyX.blushing].png"

    always:
        "images/Kitty_standing/Kitty_standing_brows[KittyX.brows].png"

    always:
        "images/Kitty_standing/Kitty_standing_mouth[KittyX.mouth].png"

    if KittyX.eyes == "_closed":
        "images/Kitty_standing/Kitty_standing_eyes_closed.png"
    else:
        "Kitty_blinking"

    if KittyX.spunk["mouth"]:
        "images/Kitty_standing/Kitty_standing_spunk_mouth[KittyX.mouth].png"

    if KittyX.spunk["face"]:
        "images/Kitty_standing/Kitty_standing_spunk_face.png"

    if KittyX.outfit["face_outer_accessory"]:
        "images/Kitty_standing/Kitty_standing_face_outer_accessory[KittyX.outfit[face_outer_accessory]].png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_hair_wet.png"
    else:
        "images/Kitty_standing/Kitty_standing_hair[KittyX.outfit[hair]].png"

    if KittyX.wet or KittyX.outfit["hair"] == "_wet":
        Null()
    elif KittyX.spunk["hair"]:
        "images/Kitty_standing/Kitty_standing_spunk_hair.png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_water_head.png"

    anchor (0.5, 0.5)

image Kitty_handjob_under:
    "images/Kitty_handjob/Kitty_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Kitty_handjob_over:
    "images/Kitty_handjob/Kitty_handjob_hand_over.png"

    anchor (0.5, 0.5)

layeredimage Kitty_titjob_hair_back:
    if KittyX.wet or KittyX.outfit["hair"] == "_wet":
        "images/Kitty_blowjob/Kitty_blowjob_hair_back.png"

    anchor (0.5, 0.5)

image Kitty_titjob_body:
    "images/Kitty_titjob/Kitty_titjob_body.png"

    anchor (0.5, 0.5)

image Kitty_titjob_arms:
    "images/Kitty_titjob/Kitty_titjob_arms.png"

    anchor (0.5, 0.5)

layeredimage Kitty_titjob_breasts:
    if action_speed:
        "images/Kitty_titjob/Kitty_titjob_breasts_smooshed.png"
    else:
        "images/Kitty_titjob/Kitty_titjob_breasts.png"

    anchor (0.5, 0.5)

image Kitty_titjob_mask:
    "images/Kitty_titjob/Kitty_titjob_mask.png"

    anchor (0.5, 0.5)

layeredimage Kitty_blowjob_head:
    if KittyX.wet or KittyX.outfit["hair"] == "_wet":
        "images/Kitty_blowjob/Kitty_blowjob_hair_back.png"

    if not renpy.showing("Kitty_sprite blowjob"):
        Null()
    elif action_speed > 1 and KittyX.wet and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet_blush.png"
    elif action_speed > 1 and KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet.png"
    elif action_speed > 1 and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_blush.png"
    elif action_speed > 1:
        "images/Kitty_blowjob/Kitty_blowjob_face_open.png"

    if renpy.showing("Kitty_sprite blowjob") and action_speed > 1:
        Null()
    elif KittyX.wet and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet_blush.png"
    elif KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet.png"
    elif KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_blush.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed.png"

    if renpy.showing("Kitty_sprite titjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 1:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 2:
        "Kitty_blowjob_mouth_animation[action_speed]" pos (0.225, 0.555)
    elif renpy.showing("Kitty_sprite blowjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_sucking.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_mouth[KittyX.mouth].png"

    if not KittyX.spunk["mouth"]:
        Null()
    elif renpy.showing("Kitty_sprite titjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 1:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed > 1:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"
    elif KittyX.mouth == "_sucking":
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth[KittyX.mouth]_under.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth[KittyX.mouth].png"

    always:
        "images/Kitty_blowjob/Kitty_blowjob_brows[KittyX.brows].png"

    if KittyX.eyes == "_closed":
        "images/Kitty_blowjob/Kitty_blowjob_eyes_closed.png"
    else:
        "Kitty_blowjob_blinking"

    if KittyX.spunk["face"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_face.png"

    if KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_hair_wet.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_hair[KittyX.outfit[hair]].png"

    if KittyX.spunk["hair"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_hair.png"

    if not KittyX.wet:
        Null()
    elif action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_head_open_wet.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_head_closed_wet.png"

    anchor (0.5, 0.5)

layeredimage Kitty_blowjob_mouth:
    if KittyX.spunk["mouth"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_sucking.png"

    anchor (0.5, 0.65)

layeredimage Kitty_blowjob_mask:
    always:
        "images/Kitty_blowjob/Kitty_blowjob_face_mask.png"

    if KittyX.spunk["mouth"] and action_speed == 2:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"

    anchor (0.5, 0.5) pos (0.5, 0.5)

image Kitty_blowjob_spunk_mouth_over:
    "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_over.png"

    anchor (0.5, 0.5)

layeredimage Kitty_blowjob_body:
    # if "blanket" in KittyX.recent_history:
    #     "images/Kitty_blowjob/Kitty_blowjob_blanket.png"

    if KittyX.outfit["top"] == "_red_shirt":
        "images/Kitty_blowjob/Kitty_blowjob_top[KittyX.outfit[top]]_under.png"

    always:
        "images/Kitty_blowjob/Kitty_blowjob_body.png"

    if KittyX.outfit["neck"]:
        "images/Kitty_blowjob/Kitty_blowjob_neck[KittyX.outfit[neck]].png"

    if KittyX.outfit["piercings"]:
        "images/Kitty_blowjob/Kitty_blowjob_piercings[KittyX.outfit[piercings]].png"

    if KittyX.outfit["bra"]:
        "images/Kitty_blowjob/Kitty_blowjob_bra[KittyX.outfit[bra]].png"

    if KittyX.outfit["dress"]:
        "images/Kitty_blowjob/Kitty_blowjob_dress[KittyX.outfit[dress]].png"

    if KittyX.outfit["top"]:
        "images/Kitty_blowjob/Kitty_blowjob_top[KittyX.outfit[top]].png"

    if KittyX.spunk["breasts"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_body.png"

    if KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_water_body.png"

    anchor (0.5, 0.5)

layeredimage Kitty_sex_body:
    always:
        "Kitty_hair_back" pos (0.28, -0.065) rotate -10 zoom 0.75

    always:
        "images/Kitty_sex/Kitty_sex_body[KittyX.outfit[piercings]].png"

    if KittyX.outfit["neck"]:
        "images/Kitty_sex/Kitty_sex_neck[KittyX.outfit[neck]].png"

    if KittyX.outfit["bottom"] == "_dress_skirt":
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_waist.png"

    if not KittyX.outfit["bra"]:
        Null()
    elif not KittyX.bra_pulled_up:
        "images/Kitty_sex/Kitty_sex_bra[KittyX.outfit[bra]].png"
    # elif KittyX.outfit["top"] == "_red_shirt" and KittyX.outfit["bra"] == "_sports_bra":
    #     "images/Kitty_sex/Kitty_sex_bra[KittyX.outfit[bra]]_top_up.png"
    # elif KittyX.outfit["bra"] == "_sports_bra":
    #     "images/Kitty_sex/Kitty_sex_bra[KittyX.outfit[bra]]_top.png"
    # elif KittyX.outfit["top"] and KittyX.outfit["bra"] != "_bikini_top":
    #     "images/Kitty_sex/Kitty_sex_bra[KittyX.outfit[bra]]_top_up.png"
    else:
        "images/Kitty_sex/Kitty_sex_bra[KittyX.outfit[bra]]_up.png"

    if not KittyX.outfit["top"]:
        Null()
    # elif KittyX.top_pulled_up and KittyX.outfit["top"] == "_pink_top" and KittyX.outfit["bra"] == "_sports_bra":
    #     "images/Kitty_sex/Kitty_sex_top_pink_top_sports_bra_up.png"
    elif KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_top[KittyX.outfit[top]]_up.png"
    else:
        "images/Kitty_sex/Kitty_sex_top[KittyX.outfit[top]].png"

    if not KittyX.outfit["jacket"]:
        Null()
    elif KittyX.jacket_opened:
        "images/Kitty_sex/Kitty_sex_jacket[KittyX.outfit[jacket]]_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_jacket[KittyX.outfit[jacket]].png"

    if KittyX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly.png"

    if KittyX.spunk["breasts"]:
        "images/Kitty_sex/Kitty_sex_spunk_breasts.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_body.png"

    if "suck_breasts" in [Player.primary_action, Player.secondary_action]:
        "licking" pos (0.245, 0.22) zoom 0.33

    if "fondle_breasts" in [Player.primary_action, Player.secondary_action]:
        "Zero_fondle_breasts_left_animation" pos (0.245, 0.25) zoom 0.61

    always:
        "Kitty_head" pos (0.28, -0.065) rotate -10 zoom 0.375

    anchor (0.5, 0.5)

layeredimage Kitty_sex_legs:
    if KittyX.outfit["bottom"] not in skirts:
        Null()
    elif KittyX.outfit["bottom"] == "_dress_skirt" and KittyX.upskirt:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_back_up.png"
    else:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_back.png"

    always:
        "images/Kitty_sex/Kitty_sex_legs.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_legs.png"

    if Player.sprite and Player.cock_position == "anal":
        "Kitty_sex_anus_animation[action_speed]" pos (0.292, 0.386)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_sex_anus" pos (0.292, 0.386) xzoom 0.6
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_sex_anus" pos (0.292, 0.386) xzoom 0.9
    elif KittyX.used_to_anal:
        "images/Kitty_sex/Kitty_sex_anus_loose.png"
    else:
        "images/Kitty_sex/Kitty_sex_anus_tight.png"

    if not KittyX.spunk["anus"]:
        Null()
    elif Player.sprite and Player.cock_position == "anal" and action_speed > 1:
        "Kitty_sex_spunk_anus_under" pos (0.292, 0.386)
    elif Player.sprite and Player.cock_position == "anal" and action_speed == 1:
        "Kitty_sex_spunk_anus_under_animation" pos (0.292, 0.386)
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anus_closed.png"

    if Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"

    if not KittyX.grool:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_grool_fucking.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_grool.png"

    if not KittyX.outfit["piercings"]:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_piercings_pussy[KittyX.outfit[piercings]]_fucking.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_sex/Kitty_sex_piercings_pussy[KittyX.outfit[piercings]]_fucking.png"
    else:
        "images/Kitty_sex/Kitty_sex_piercings_pussy[KittyX.outfit[piercings]].png"

    if not KittyX.pubes:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"

    if KittyX.spunk["pussy"]:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if not KittyX.outfit["underwear"] or KittyX.underwear_pulled_down:
        Null()
    elif KittyX.grool:
        "images/Kitty_sex/Kitty_sex_underwear[KittyX.outfit[underwear]]_grool.png"
    else:
        "images/Kitty_sex/Kitty_sex_underwear[KittyX.outfit[underwear]].png"

    if KittyX.outfit["hose"] and not KittyX.hose_pulled_down:
        "images/Kitty_sex/Kitty_sex_hose[KittyX.outfit[hose]].png"

    if not KittyX.outfit["bottom"]:
        Null()
    elif KittyX.outfit["bottom"] not in skirts and KittyX.grool > 1 and not KittyX.bottom_pulled_down:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_grool.png"
    elif KittyX.bottom_pulled_down and KittyX.outfit["bottom"] == "_capris":
        Null()
    elif KittyX.bottom_pulled_down or KittyX.upskirt:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_down.png"
    else:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]].png"

    if KittyX.outfit["top"] == "_towel" and not KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_top[KittyX.outfit[top]]_legs.png"

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_cock_Kitty", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Kitty", "images/Kitty_sex/Kitty_sex_anus_mask.png")

    if not KittyX.spunk["anus"]:
        Null()
    elif not Player.sprite or Player.cock_position != "anal":
        Null()
    elif action_speed == 1:
        "Kitty_sex_spunk_anus_over_animation" pos (0.292, 0.386)
    else:
        "Kitty_sex_spunk_anus_over" pos (0.292, 0.386)

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_cock_Kitty", "images/Kitty_sex/Kitty_sex_pussy_mask.png")
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "images/Kitty_sex/Kitty_sex_pussy_mask.png")
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Kitty", "images/Kitty_sex/Kitty_sex_pussy_mask.png")

    if not KittyX.spunk["pussy"]:
        Null()
    elif not Player.sprite or Player.cock_position != "in":
        Null()
    elif action_speed <= 1:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png" offset (111, 0) xzoom 0.8
    else:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

    if KittyX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if Player.sprite and Player.cock_position == "out":
        "Zero_cock_Kitty"

    if Player.primary_action == "eat_pussy":
        "licking" pos (0.292, 0.474) zoom 0.39
    elif Player.primary_action == "eat_ass":
        "licking" pos (0.292, 0.548) zoom 0.39

    if Player.sprite and Player.cock_position == "footjob":
        "Zero_cock_Kitty"

    if Player.cock_position == "footjob" or show_feet:
        "Kitty_sex_feet" pos (0.291, 0.391)
    else:
        AlphaMask("Kitty_sex_feet", "images/Kitty_sex/Kitty_sex_feet_mask.png")

    anchor (0.5, 0.5)

layeredimage Kitty_sex_feet:
    always:
        "images/Kitty_sex/Kitty_sex_feet.png"

    if KittyX.outfit["hose"] and KittyX.outfit["hose"] != "_garterbelt" and KittyX.hose_pulled_down:
        "images/Kitty_sex/Kitty_sex_hose[KittyX.outfit[hose]]_feet.png"

    if KittyX.outfit["bottom"] in pants and not KittyX.bottom_pulled_down:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_feet.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_feet.png"

    anchor (0.5, 0.5)

image Kitty_sex_anus:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

image Kitty_sex_spunk_anus_under:
    "images/Kitty_sex/Kitty_sex_spunk_anus_under.png"

    anchor (0.5, 0.5)

image Kitty_sex_spunk_anus_over:
    "images/Kitty_sex/Kitty_sex_spunk_anus_over.png"

    anchor (0.5, 0.5)

layeredimage Kitty_doggy_body:
    # always:
    #     "images/Kitty_doggy/Kitty_doggy_head_reference.png"

    always:
        "Kitty_doggy_head" pos (0.095, 0.265) zoom 0.8

    always:
        "images/Kitty_doggy/Kitty_doggy_body.png"

    if not KittyX.outfit["bra"]:
        Null()
    elif KittyX.bra_pulled_up:
        "images/Kitty_doggy/Kitty_doggy_bra[KittyX.outfit[bra]]_up.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_bra[KittyX.outfit[bra]].png"

    if KittyX.outfit["top"]:
        "images/Kitty_doggy/Kitty_doggy_top[KittyX.outfit[top]].png"

    if KittyX.outfit["jacket"]:
        "images/Kitty_doggy/Kitty_doggy_jacket[KittyX.outfit[jacket]].png"

    if KittyX.spunk["back"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_back.png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_water_body.png"

    if "fondle_breasts" in [Player.primary_action, Player.secondary_action]:
        "Zero_doggy_fondle_breast_animation" pos (0.1, 0.36)

    anchor (0.5, 0.5)

layeredimage Kitty_doggy_head:
    if KittyX.blushing:
        "images/Kitty_doggy/Kitty_doggy_head_blush.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_head.png"

    always:
        "images/Kitty_doggy/Kitty_doggy_mouth[KittyX.mouth].png"

    if KittyX.spunk["mouth"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_mouth[KittyX.mouth].png"

    always:
        "images/Kitty_doggy/Kitty_doggy_brows[KittyX.brows].png"

    if KittyX.eyes == "_closed":
        "images/Kitty_doggy/Kitty_doggy_eyes_closed.png"
    else:
        "Kitty_doggy_blinking"

    if KittyX.spunk["face"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_face.png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_hair_wet.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_hair[KittyX.outfit[hair]].png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_water_hair.png"

    if KittyX.spunk["hair"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_hair.png"

    anchor (0.5, 0.5)

layeredimage Kitty_doggy_ass:
    if KittyX.outfit["bottom"] and KittyX.outfit["bottom"] != "_capris" and (KittyX.bottom_pulled_down or KittyX.upskirt):
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_back_down.png"

    if not KittyX.outfit["underwear"] or not KittyX.underwear_pulled_down:
        Null()
    elif KittyX.grool > 1:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_back_down_grool.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_back_down.png"

    always:
        "images/Kitty_doggy/Kitty_doggy_ass.png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_water_ass.png"

    if KittyX.outfit["hose"]:
        "images/Kitty_doggy/Kitty_doggy_hose[KittyX.outfit[hose]].png"

    if not KittyX.outfit["underwear"] or not KittyX.underwear_pulled_down:
        Null()
    elif KittyX.grool > 1:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_down_grool.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_down.png"

    if KittyX.outfit["bottom"] and (KittyX.bottom_pulled_down or KittyX.upskirt):
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_down.png"

    if Player.primary_action == "eat_pussy":
        "images/Kitty_doggy/Kitty_doggy_pussy_open.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_pussy_closed.png"

    if Player.sprite and Player.cock_position == "in":
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"

    if Player.sprite and Player.cock_position == "in":
        "Kitty_doggy_pussy_hole_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_pussy_fingering_animation" pos (0.113, 0.475)
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_pussy_hole_animation1" pos (0.113, 0.475)

    if KittyX.spunk["pussy"] and Player.cock_position != "in":
        "images/Jean_doggy/Jean_doggy_spunk_pussy_closed.png"

    if not KittyX.grool:
        Null()
    elif Player.cock_position == "in":
        "images/Rogue_doggy/Rogue_doggy_grool_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_grool_closed.png"

    if not KittyX.pubes:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_doggy/Kitty_doggy_pubes_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_doggy/Kitty_doggy_pubes_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Kitty_doggy/Kitty_doggy_pubes.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_pubes_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_doggy/Kitty_doggy_pubes_open.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_pubes.png"

    if KittyX.outfit["piercings"]:
        "images/Kitty_doggy/Kitty_doggy_piercings_pussy[KittyX.outfit[piercings]].png"

    if KittyX.used_to_anal:
        "images/Jean_doggy/Jean_doggy_anus_loose.png"
    else:
        "images/Jean_doggy/Jean_doggy_anus_tight.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "Kitty_doggy_anus_anal_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_anus_fingering_animation" pos (0.113, 0.475)
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_anus_anal_animation1" pos (0.113, 0.475)

    if KittyX.outfit["hose"] and not KittyX.hose_pulled_down:
        "images/Kitty_doggy/Kitty_doggy_hose[KittyX.outfit[hose]].png"

    if not KittyX.spunk["anus"]:
        Null()
    elif Player.cock_position == "anal" and action_speed:
        "images/Jean_doggy/Jean_doggy_spunk_anus_open.png"
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Jean_doggy/Jean_doggy_spunk_anus_open.png"
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Jean_doggy/Jean_doggy_spunk_anus_open.png"
    else:
        "images/Jean_doggy/Jean_doggy_spunk_anus_loose.png"

    if not KittyX.outfit["underwear"] or KittyX.underwear_pulled_down:
        Null()
    elif Player.sprite and Player.cock_position in ["in", "anal"]:
        Null()
    elif KittyX.grool > 1:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_grool.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]].png"

    if KittyX.outfit["hose"]:
        "images/Kitty_doggy/Kitty_doggy_hose[KittyX.outfit[hose]].png"

    if not KittyX.outfit["bottom"]:
        Null()
    elif KittyX.outfit["bottom"] in skirts and KittyX.upskirt:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_down.png"
    elif KittyX.outfit["bottom"] not in skirts and KittyX.grool > 1:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_grool.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]].png"

    if KittyX.outfit["top"] == "_pink_top" and not (KittyX.bottom_pulled_down or KittyX.upskirt):
        "images/Kitty_doggy/Kitty_doggy_top[KittyX.outfit[top]]_tail.png"

    if KittyX.outfit["bra"] != "_towel":
        Null()
    elif KittyX.upskirt:
        "images/Kitty_doggy/Kitty_doggy_bra[KittyX.outfit[bra]]_legs_down.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_bra[KittyX.outfit[bra]]_legs.png"

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_cock_Kitty", "Zero_cock_Kitty_mask")
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "Zero_finger_Kitty_mask")
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Kitty", "dildo_Kitty_mask")

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_cock_Kitty", "Zero_cock_Kitty_mask")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "Zero_finger_Kitty_mask")
    elif Player.primary_action == "dildo_ass":
        AlphaMask("dildo_Kitty", "dildo_Kitty_mask")

    if KittyX.spunk["back"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_back.png"

    if Player.primary_action == "eat_pussy":
        "licking" pos (0.112, 0.53) zoom 0.28
    elif Player.primary_action == "eat_ass":
        "licking" pos (0.112, 0.48) zoom 0.28

    if Player.sprite and Player.cock_position == "out":
        "images/Kitty_doggy/Kitty_doggy_hotdog_back.png"

    if Player.sprite and Player.cock_position == "out":
        AlphaMask("Zero_cock_Kitty", "images/Rogue_doggy/Rogue_doggy_hotdog_mask.png")

    anchor (0.5, 0.5)

image Kitty_doggy_pussy_hole:
    "images/Kitty_doggy/Kitty_doggy_pussy_hole.png"

    anchor (0.52, 0.69)

image Kitty_doggy_anus_hole:
    "images/Kitty_doggy/Kitty_doggy_anus_full_hole.png"

    anchor (0.52, 0.69)

image Kitty_doggy_pussy_mask:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"

    anchor (0.52, 0.69)

image Kitty_doggy_anus_mask:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    anchor (0.52, 0.69)

layeredimage Kitty_doggy_shins:
    if not KittyX.outfit["hose"] or KittyX.outfit["hose"] == "_garterbelt" or KittyX.hose_pulled_down:
        "images/Kitty_doggy/Kitty_doggy_shins.png"
    elif KittyX.outfit["hose"] in ["_ripped_pantyhose", "_ripped_tights"]:
        "images/Kitty_doggy/Kitty_doggy_hose_ripped_shins.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_hose_shins.png"

    if KittyX.outfit["bottom"] in pants:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_shins.png"

    if not KittyX.outfit["hose"] or KittyX.outfit["hose"] == "_garterbelt" and (not Player.sprite or Player.cock_position == "footjob"):
        "images/Kitty_doggy/Kitty_doggy_feet_footjob.png"
    elif not KittyX.outfit["hose"] or KittyX.outfit["hose"] == "_garterbelt":
        "images/Kitty_doggy/Kitty_doggy_feet.png"
    elif KittyX.outfit["hose"] in ["_ripped_pantyhose", "_ripped_tights"] and (not Player.sprite or Player.cock_position == "footjob"):
        "images/Kitty_doggy/Kitty_doggy_hose_ripped_feet_footjob.png"
    elif KittyX.outfit["hose"] in ["_ripped_pantyhose", "_ripped_tights"]:
        "images/Kitty_doggy/Kitty_doggy_hose_ripped_feet.png"

    anchor (0.5, 0.5)

image Kitty_doggy_feet:
    AlphaMask("Kitty_doggy_shins", "images/Kitty_doggy/Kitty_doggy_feet_mask.png")

    anchor (0.5, 0.5)
