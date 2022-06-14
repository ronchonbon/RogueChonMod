layeredimage Kitty_sprite standing:
    if KittyX.outfit["dress"]:
        "images/Kitty_standing/Kitty_standing_back_outer_accessory[KittyX.outfit[dress]].png"
    elif KittyX.outfit["bottom"] == "_dress":
        "images/Kitty_standing/Kitty_standing_back_outer_accessory[KittyX.outfit[bottom]].png"

    always:
        "Kitty_back_hair" pos (0.12, 0.152) zoom 0.5

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
    elif KittyX.grool > 1:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]]_grool.png"
    else:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]].png"

    if KittyX.outfit["hose"] and not KittyX.underwear_pulled_down:
        "images/Kitty_standing/Kitty_standing_hose[KittyX.outfit[hose]].png"

    if KittyX.outfit["bottom"] and KittyX.grool > 1:
        "images/Kitty_standing/Kitty_standing_grool1.png"
    elif KittyX.grool:
        "images/Kitty_standing/Kitty_standing_grool[KittyX.grool].png"

    always:
        "Kitty_grool_animations"

    if KittyX.spunk["pussy"] or KittyX.spunk["anus"]:
        "images/Kitty_standing/Kitty_standing_spunk_pussy.png"

    always:
        "Kitty_spunk_animations"

    if not KittyX.outfit["bottom"]:
        Null()
    elif KittyX.bottom_pulled_down or KittyX.dress_upskirt or KittyX.upskirt:
        "images/Kitty_standing/Kitty_standing_bottom[KittyX.outfit[bottom]]_down.png"
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

    if KittyX.outfit["piercings"] and KittyX.breasts_covered:
        "images/Kitty_standing/Kitty_standing_piercings_breasts[KittyX.outfit[piercings]]_covered.png"

    if not KittyX.outfit["jacket"]:
        Null()
    elif KittyX.jacket_opened:
        "images/Kitty_standing/Kitty_standing_jacket[KittyX.outfit[jacket]][KittyX.arm_pose]_up.png"
    else:
        "images/Kitty_standing/Kitty_standing_jacket[KittyX.outfit[jacket]][KittyX.arm_pose].png"

    always:
        "Kitty_head" pos (0.12, 0.152) zoom 0.5

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

    # always:
    #     "Kitty_standing_fondling_animations"

    anchor (0.5, 0.0) offset (40, 170) zoom 0.95

layeredimage Kitty_back_hair:
    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_back_hair_wet.png"
    elif KittyX.outfit["hair"] != "_evo":
        "images/Kitty_standing/Kitty_standing_back_hair[KittyX.outfit[hair]].png"

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
        "images/Kitty_standing/Kitty_spunk_standing[KittyX.mouth].png"

    if KittyX.spunk["face"]:
        "images/Kitty_standing/Kitty_standing_face_spunk.png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_hair_wet.png"
    else:
        "images/Kitty_standing/Kitty_standing_hair[KittyX.outfit[hair]].png"

    if KittyX.wet or KittyX.outfit["hair"] == "_wet":
        Null()
    elif KittyX.spunk["hair"]:
        "images/Kitty_standing/Kitty_standing_spunk_hair[KittyX.outfit[hair]].png"

    if KittyX.outfit["face_outer_accessory"]:
        "images/Kitty_standing/Kitty_standing_face_outer_accessory[KittyX.outfit[face_outer_accessory]].png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_water_head.png"

    anchor (0.5, 0.5)

image Kitty_handjob_under:
    "images/Kitty_handjob/Kitty_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Kitty_handjob_over:
    "images/Kitty_handjob/Kitty_handjob_hand_over.png"

    anchor (0.5, 0.5)

layeredimage Kitty_titjob_back_hair:
    if KittyX.wet or KittyX.outfit["hair"] == "_wet":
        "images/Kitty_blowjob/Kitty_blowjob_back_hair.png"

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
        "images/Kitty_blowjob/Kitty_blowjob_back_hair.png"

    if renpy.showing("Kitty_sprite_blowjob") and action_speed > 2 and KittyX.wet and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet_blush.png"
    elif renpy.showing("Kitty_sprite_blowjob") and action_speed > 2 and KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet.png"
    elif renpy.showing("Kitty_sprite_blowjob") and action_speed > 2 and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_blush.png"
    elif renpy.showing("Kitty_sprite_blowjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_face_open.png"
    elif KittyX.wet and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet_blush.png"
    elif KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet.png"
    elif KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_blush.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed.png"

    if renpy.showing("Kitty_sprite titjob") and action_speed == 3:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 1:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_sucking.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_mouth[KittyX.mouth].png"

    if renpy.showing("Kitty_sprite blowjob") and action_speed == 2:
        "Kitty_blowjob_mouth_animations"

    if not KittyX.spunk["mouth"]:
        Null()
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 1:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed > 2:
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


















layeredimage Kitty_blowjob_body:
    if "blanket" in KittyX.recent_history:
        "images/Kitty_blowjob/Kitty_blowjob_blanket.png"

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
        "Kitty_back_hair" pos (0.28, -0.065) rotate -10 zoom 0.75

    always:
        "images/Kitty_sex/Kitty_sex_body[KittyX.outfit[piercings]].png"

    if KittyX.outfit["neck"]:
        "images/Kitty_sex/Kitty_sex_neck[KittyX.outfit[neck]].png"

    if KittyX.outfit["bottom"] == "_dress":
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_waist.png"

    if KittyX.outfit["bra"] and KittyX.bra_pulled_up:
        "images/Kitty_sex/Kitty_sex_bra[KittyX.outfit[bra]]_up.png"
    elif KittyX.outfit["bra"]:
        "images/Kitty_sex/Kitty_sex_bra[KittyX.outfit[bra]].png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_body.png"

    if KittyX.outfit["top"] and KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_top[KittyX.outfit[top]]_up.png"
    elif KittyX.outfit["top"]:
        "images/Kitty_sex/Kitty_sex_top[KittyX.outfit[top]].png"

    if KittyX.outfit["jacket"] and KittyX.jacket_opened:
        "images/Kitty_sex/Kitty_sex_jacket[KittyX.outfit[jacket]]_up.png"
    elif KittyX.outfit["jacket"]:
        "images/Kitty_sex/Kitty_sex_jacket[KittyX.outfit[jacket]].png"

    if KittyX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly.png"

    if KittyX.spunk["breasts"]:
        "images/Kitty_sex/Kitty_sex_spunk_breasts.png"

    if "suck_breasts" in [Player.primary_action, Player.secondary_action]:
        "licking" offset (0.245, 0.273) zoom 0.6

    if "fondle_breasts" in [Player.primary_action, Player.secondary_action]:
        "Zero_fondle_breasts_left_animation" offset (0.245, 306) zoom 1.1

    always:
        "Kitty_head" pos (0.28, -0.065) rotate -10 zoom 0.75

    anchor (0.5, 0.5)

layeredimage Kitty_sex_legs:
    if KittyX.outfit["bottom"] == "_dress" and KittyX.dress_upskirt:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_back_up.png"
    elif KittyX.outfit["bottom"] in ["_dress", "_skirt"]:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_back.png"

    always:
        "images/Kitty_sex/Kitty_sex_legs.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_legs.png"

    if Player.sprite and Player.cock_position == "anal":
        "Kitty_sex_anus_animation[action_speed]" pos (0.292, 0.386)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_sex_anus" pos (0.292, 0.386) xzoom 0.6
    elif Player.primary_action == "dildo_ass":
        "Kitty_sex_anus" pos (0.292, 0.386) xzoom 0.9
    elif KittyX.used_to_anal:
        "images/Kitty_sex/Kitty_sex_anus_loose.png"
    else:
        "images/Kitty_sex/Kitty_sex_anus_tight.png"

    if KittyX.spunk["anus"]:
        "Kitty_sex_spunk_anus_under_animations"

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Kitty_sex_cock_anal_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Kitty_sex_finger_ass_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif Player.primary_action == "dildo_ass":
        AlphaMask("Kitty_dildo_anal_animations", "images/Kitty_sex/Kitty_sex_anus_mask.png")

    if KittyX.spunk["anus"] and Player.sprite and Player.cock_position == "anal" and action_speed == 1:
        "Kitty_sex_spunk_anus_over_animation" pos (0.292, 0.386)
    elif KittyX.spunk["anus"] and Player.sprite and Player.cock_position == "anal":
        "Kitty_sex_spunk_anus_over" pos (0.292, 0.386)

    if Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"
    elif Player.primary_action == "dildo_pussy":
        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"

    if KittyX.grool and Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_grool_fucking.png"
    elif KittyX.grool:
        "images/Kitty_sex/Kitty_sex_pussy_grool.png"

    if KittyX.outfit["piercings"] and (Player.sprite or Player.cock_position != "in" or action_speed <= 1):
        "images/Kitty_sex/Kitty_sex_piercings_pussy[KittyX.outfit[piercings]].png"
    elif KittyX.outfit["piercings"]:
        "images/Kitty_sex/Kitty_sex_piercings_pussy[KittyX.outfit[piercings]]_fucking.png"

    if KittyX.pubes and Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
    elif KittyX.pubes and Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    elif KittyX.pubes and Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"
    elif KittyX.pubes and Player.primary_action == "dildo_pussy":
        "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
    elif KittyX.pubes and Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    elif KittyX.pubes:
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"

    if KittyX.spunk["pussy"]:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Kitty_sex_cock_animations", "images/Kitty_sex/Kitty_sex_pussy_mask.png")
    elif "fondle_pussy" in [Player.primary_action, Player.secondary_action] or "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Kitty_sex_finger_pussy_animations", "images/Kitty_sex/Kitty_sex_pussy_mask.png")
    elif Player.primary_action == "dildo_pussy":
        AlphaMask("Kitty_dildo_pussy_animations", "images/Kitty_sex/Kitty_sex_pussy_mask.png")

    if KittyX.spunk["pussy"] and Player.sprite and Player.cock_position == "in" and action_speed <= 1:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png" anchor (0.5, 0.5) pos (0.5, 0.5) xzoom 0.8
    elif KittyX.spunk["pussy"] and Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png" anchor (0.5, 0.5) pos (0.5, 0.5)

    if not KittyX.outfit["underwear"] or KittyX.underwear_pulled_down:
        Null()
    elif KittyX.grool:
        "images/Kitty_sex/Kitty_sex_underwear[KittyX.outfit[underwear]]_grool.png"
    else:
        "images/Kitty_sex/Kitty_sex_underwear[KittyX.outfit[underwear]].png"

    if KittyX.outfit["hose"] and not KittyX.underwear_pulled_down:
        "images/Kitty_sex/Kitty_sex_hose[KittyX.outfit[hose]].png"

    if KittyX.outfit["bottom"] in ["_capris", "_black_jeans", "_shorts", "_yoga_pants"] and KittyX.grool > 1 and (not KittyX.bottom_pulled_down and not KittyX.upskirt and not KittyX.dress_upskirt):
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_grool.png"
    if KittyX.outfit["bottom"] and (KittyX.bottom_pulled_down or KittyX.upskirt or KittyX.dress_upskirt):
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_down.png"
    elif KittyX.outfit["bottom"]:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]].png"

    if KittyX.outfit["top"] == "_towel" and not KittyX.top_pulled_up:
        "images/Kitty_sex/Kitty_sex_top[KittyX.outfit[top]]_legs.png"

    if KittyX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if Player.sprite and Player.cock_position == "out":
        "Kitty_sex_cock_hotdog_animation[action_speed]" pos (0.29175, 0.65) zoom 1.18

    if Player.primary_action == "eat_pussy":
        "licking" pos (0.292, 0.474) zoom 0.7
    elif Player.primary_action == "eat_ass":
        "licking" pos (0.292, 0.548) zoom 0.7

    if Player.sprite and Player.cock_position == "footjob":
        "Kitty_sex_cock_footjob_animation[action_speed]" pos (0.29, 0.7) alpha 0.8 zoom 0.6

    if not action_speed or Player.cock_position == "footjob" or show_feet:
        "Kitty_sex_feet" pos (0.291, 0.391)
    else:
        AlphaMask("Kitty_sex_feet", "images/Kitty_sex/Kitty_sex_feet_mask.png")

    anchor (0.5, 0.5)

layeredimage Kitty_sex_feet:
    always:
        "images/Kitty_sex/Kitty_sex_feet.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_feet.png"

    if KittyX.outfit["hose"] and KittyX.outfit["hose"] != "_garterbelt" and KittyX.underwear_pulled_down:
        "images/Kitty_sex/Kitty_sex_hose[KittyX.outfit[hose]]_feet.png"

    if KittyX.outfit["bottom"] and KittyX.outfit["bottom"] != "_skirt" and not KittyX.bottom_pulled_down and not KittyX.dress_upskirt:
        "images/Kitty_sex/Kitty_sex_bottom[KittyX.outfit[bottom]]_feet.png"

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

    if KittyX.outfit["bra"] and KittyX.bra_pulled_up:
        "images/Kitty_doggy/Kitty_doggy_bra[KittyX.outfit[bra]]_up.png"
    elif KittyX.outfit["bra"]:
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
        "Zero_doggy_fondle_breast_animation"

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
    if KittyX.outfit["bottom"] and (KittyX.bottom_pulled_down or KittyX.upskirt or KittyX.dress_upskirt):
        "images/Kitty_doggy/Kitty_doggy_back_outer_accessory[KittyX.outfit[bottom]]_down.png"

    if KittyX.outfit["underwear"] and KittyX.underwear_pulled_down and KittyX.grool:
        "images/Kitty_doggy/Kitty_doggy_back_inner_accessory[KittyX.outfit[underwear]]_down_grool.png"
    elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        "images/Kitty_doggy/Kitty_doggy_back_inner_accessory[KittyX.outfit[underwear]]_down.png"

    always:
        "images/Kitty_doggy/Kitty_doggy_ass.png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_water_ass.png"

    if KittyX.outfit["hose"]:
        "images/Kitty_doggy/Kitty_doggy_hose[KittyX.outfit[hose]].png"

    if KittyX.outfit["underwear"] and KittyX.underwear_pulled_down and KittyX.grool:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_down_grool.png"
    elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_down.png"

    if KittyX.outfit["bottom"] and (KittyX.bottom_pulled_down or KittyX.upskirt or KittyX.dress_upskirt):
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_down.png"

    if Player.primary_action == "eat_pussy":
        "images/Kitty_doggy/Kitty_doggy_pussy_open.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_pussy_closed.png"

    if Player.sprite and Player.cock_position == "in":
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"

    if Player.sprite and Player.cock_position == "in":
        "Kitty_doggy_pussy_hole_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_pussy_fingering" pos (0.113, 0.475)
    elif Player.primary_action == "dildo_pussy":
        "Kitty_doggy_pussy_hole_animation1" pos (0.113, 0.475)

    if KittyX.spunk["pussy"] and Player.cock_position != "in":
        "images/Jean_doggy/Jean_doggy_spunk_pussy_closed.png"
    elif KittyX.grool and Player.cock_position == "in":
        "images/Rogue_doggy/Rogue_doggy_grool_open.png"
    elif KittyX.grool:
        "images/Rogue_doggy/Rogue_doggy_grool_closed.png"

    if KittyX.pubes and Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_doggy/Kitty_doggy_pubes_fucking.png"
    elif KittyX.pubes and Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_doggy/Kitty_doggy_pubes_open.png"
    elif KittyX.pubes and Player.sprite and Player.cock_position == "in":
        "images/Kitty_doggy/Kitty_doggy_pubes.png"
    elif KittyX.pubes and Player.primary_action == "dildo_pussy":
        "images/Kitty_doggy/Kitty_doggy_pubes_fucking.png"
    elif KittyX.pubes and Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_doggy/Kitty_doggy_pubes_open.png"
    elif KittyX.pubes:
        "images/Kitty_doggy/Kitty_doggy_pubes.png"

    if KittyX.outfit["piercings"]:
        "images/Kitty_doggy/Kitty_doggy_piercings_pussy[KittyX.outfit[piercings]].png"

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Kitty_doggy_cock_animations", "Kitty_doggy_pussy_mask_animations")
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Kitty_doggy_finger_pussy_animations", "Kitty_doggy_pussy_mask_animations")
    elif Player.primary_action == "dildo_pussy":
        AlphaMask("Kitty_doggy_dildo_pussy_animations", "Kitty_doggy_pussy_mask_animations")

    if KittyX.used_to_anal:
        "images/Jean_doggy/Jean_doggy_anus_loose.png"
    else:
        "images/Jean_doggy/Jean_doggy_anus_tight.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "Kitty_doggy_anus_anal_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_anus_fingering" pos (0.113, 0.475)
    elif Player.primary_action == "dildo_ass":
        "Kitty_doggy_anus_anal_animation1" pos (0.113, 0.475)

    if KittyX.outfit["hose"] and not KittyX.underwear_pulled_down:
        "images/Kitty_doggy/Kitty_doggy_hose[KittyX.outfit[hose]].png"

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Kitty_doggy_cock_anal_animations", "Kitty_doggy_anus_mask_animations")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Kitty_doggy_finger_anal_animations", "Kitty_doggy_anus_fingering_mask_animations")
    elif Player.primary_action == "dildo_ass":
        AlphaMask("Kitty_doggy_dildo_anal_animations", "Kitty_doggy_anus_mask_animations")

    if KittyX.spunk["anus"] and Player.cock_position == "anal" and Player.primary_action not in ["finger_ass", "dildo_ass"]:
        "images/Jean_doggy/Jean_doggy_spunk_anus_open.png"
    elif KittyX.spunk["anus"] and Player.primary_action not in ["finger_ass", "dildo_ass"]:
        "images/Jean_doggy/Jean_doggy_spunk_anus_loose.png"

    if KittyX.outfit["underwear"] and KittyX.grool and not KittyX.underwear_pulled_down and (not Player.sprite or Player.cock_position not in ["in", "anal"]):
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]]_grool.png"
    elif KittyX.outfit["underwear"] and not KittyX.underwear_pulled_down and (not Player.sprite or Player.cock_position not in ["in", "anal"]):
        "images/Kitty_doggy/Kitty_doggy_underwear[KittyX.outfit[underwear]].png"

    if Player.sprite and Player.cock_position in ["in", "anal"]:
        Null()
    elif KittyX.outfit["hose"] in ["_garter_belt", "_stockings_and_garterbelt"]:
        "images/Kitty_doggy/Kitty_doggy_hose[KittyX.outfit[hose]].png"
    elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down:
        Null()
    elif KittyX.outfit["hose"]:
        "images/Kitty_doggy/Kitty_doggy_hose[KittyX.outfit[hose]].png"

    if KittyX.outfit["bottom"] in ["_blue_skirt", "_dress"] and KittyX.upskirt and Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_down.png"
    elif KittyX.outfit["bottom"] in ["_blue_skirt", "_dress"] and KittyX.upskirt:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_down.png"
    elif KittyX.outfit["bottom"] in ["_blue_skirt", "_dress"]:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]].png"
    elif KittyX.outfit["bottom"] and KittyX.grool > 1:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_grool.png"
    elif KittyX.outfit["bottom"]:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]].png"

    if KittyX.outfit["top"] == "_pink_top" and (not KittyX.upskirt and not KittyX.dress_upskirt):
        "images/Kitty_doggy/Kitty_doggy_top_pink_top_tail.png"

    if KittyX.outfit["top"] == "_towel" and KittyX.upskirt:
        "images/Kitty_doggy/Kitty_doggy_top_towel_down_legs.png"
    elif KittyX.outfit["top"] == "_towel":
        "images/Kitty_doggy/Kitty_doggy_top_towel_legs.png"

    if KittyX.spunk["back"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_back.png"

    if Player.primary_action == "eat_pussy":
        "licking" offset (195, 540) zoom 0.5
    elif Player.primary_action == "eat_ass":
        "licking" offset (195, 500) zoom 0.5

    if Player.sprite and Player.cock_position == "out":
        "images/Kitty_doggy/Kitty_doggy_hotdog_back.png"

    if Player.sprite and Player.cock_position == "out":
        AlphaMask("Kitty_doggy_cock_hotdog_animations", "images/Rogue_doggy/Rogue_doggy_hotdog_mask.png")

    anchor (0.5, 0.5)

image Kitty_doggy_pussy_hole:
    "images/Jean_doggy/Jean_doggy_pussy_hole.png"

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
    if KittyX.outfit["hose"] in ["_ripped_pantyhose", "_ripped_tights"]:
        "images/Kitty_doggy/Kitty_doggy_hose_ripped_shins.png"
    elif KittyX.outfit["hose"] and KittyX.outfit["hose"] != "_garterbelt":
        "images/Kitty_doggy/Kitty_doggy_hose_shins.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_shins.png"

    if KittyX.outfit["bottom"] in ["_capris", "_black_jeans", "_yoga_pants"]:
        "images/Kitty_doggy/Kitty_doggy_bottom[KittyX.outfit[bottom]]_shins.png"

    if (not Player.sprite or Player.cock_position == "footjob") and KittyX.outfit["hose"] in ["_ripped_pantyhose", "_ripped_tights"]:
        "images/Kitty_doggy/Kitty_doggy_hose_ripped_feet.png"
    elif (not Player.sprite or Player.cock_position == "footjob") and KittyX.outfit["hose"] and KittyX.outfit["hose"] != "_garterbelt":
        "images/Kitty_doggy/Kitty_doggy_hose_feet.png"
    elif not Player.sprite or Player.cock_position == "footjob":
        "images/Kitty_doggy/Kitty_doggy_feet.png"
    elif KittyX.outfit["hose"] in ["_ripped_pantyhose", "_ripped_tights"]:
        "images/Kitty_doggy/Kitty_doggy_hose_ripped_feet_footjob.png"
    elif KittyX.outfit["hose"] and KittyX.outfit["hose"] != "_garterbelt":
        "images/Kitty_doggy/Kitty_doggy_hose_feet_footjob.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_feet_footjob.png"

    anchor (0.5, 0.5)

image Kitty_doggy_feet:
    AlphaMask("Kitty_doggy_shins", "images/Kitty_doggy/Kitty_doggy_feet_mask.png")

    anchor (0.5, 0.5)
