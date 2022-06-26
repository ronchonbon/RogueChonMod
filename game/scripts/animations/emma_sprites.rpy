layeredimage Emma_sprite standing normal:
    # always:
    #     "images/Emma_standing/Emma_standing_head_reference.png"

    if EmmaX.outfit["jacket"]:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]]_back.png"

    if EmmaX.outfit["bottom"] == "_dress_skirt":
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_back.png"

    if EmmaX.outfit["bra"] == "_corset" and not EmmaX.bra_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]][EmmaX.arm_pose]_back.png"

    if EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_back_down.png"

    always:
        "Emma_hair_back" pos (0.201, 0.31) zoom 0.5

    always:
        "images/Emma_standing/Emma_standing_legs[EmmaX.arm_pose].png"

    if EmmaX.pubes:
        "images/Emma_standing/Emma_standing_pubes.png"

    if EmmaX.outfit["bra"] in ["_corset", "_sports_bra", "_bikini_top"] and not EmmaX.bra_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_under.png"

    if not EmmaX.outfit["underwear"]:
        Null()
    elif EmmaX.underwear_pulled_down and EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_down_grool.png"
    elif EmmaX.underwear_pulled_down:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_down.png"
    elif EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_grool.png"
    else:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]].png"

    if EmmaX.outfit["hose"] and not EmmaX.hose_pulled_down:
        "images/Emma_standing/Emma_standing_hose[EmmaX.outfit[hose]].png"

    if EmmaX.outfit["bottom"] and EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_grool.png"
    elif EmmaX.grool:
        "images/Emma_standing/Emma_standing_grool.png"

    always:
        "Emma_grool_animations"

    if EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]:
        "images/Emma_standing/Emma_standing_spunk_pussy.png"

    always:
        "Emma_spunk_animations"

    if EmmaX.outfit["bodysuit"]:
        "images/Emma_standing/Emma_standing_bodysuit[EmmaX.outfit[bodysuit]][EmmaX.arm_pose].png"

    if not EmmaX.outfit["bottom"]:
        Null()
    elif EmmaX.bottom_pulled_down or EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_down.png"
    elif EmmaX.outfit["bottom"] == "_yoga_pants" and EmmaX.grool:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_grool.png"
    else:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]].png"

    if EmmaX.outfit["top"] in ["_nighty", "_towel"]:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]]_waist.png"

    always:
        "images/Emma_standing/Emma_standing_arms[EmmaX.arm_pose].png"

    if EmmaX.outfit["gloves"]:
        "images/Emma_standing/Emma_standing_gloves[EmmaX.outfit[gloves]][EmmaX.arm_pose].png"

    if EmmaX.outfit["piercings"]:
        "images/Emma_standing/Emma_standing_piercings_pussy[EmmaX.outfit[piercings]].png"

    if EmmaX.outfit["boots"]:
        "images/Emma_standing/Emma_standing_boots[EmmaX.outfit[boots]].png"

    if EmmaX.outfit["bottom"] == "_dress_skirt" and not EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_front.png"

    if EmmaX.arm_pose == 1 or EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_breasts_down.png"

    if not EmmaX.outfit["piercings"]:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_up.png"
    else:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_down.png"

    if EmmaX.outfit["jacket"] and EmmaX.jacket_opened:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_sleeves_up.png"

    if not EmmaX.outfit["bra"]:
        Null()
    elif EmmaX.bra_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_up.png"
    # elif EmmaX.outfit["bra"] == "_corset" and EmmaX.outfit["top"]:
    #     "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_top.png"
    else:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]].png"

    if not EmmaX.outfit["top"]:
        Null()
    elif EmmaX.top_pulled_up and EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up_up.png"
    elif EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_down_up.png"
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up.png"
    else:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_down.png"

    if EmmaX.outfit["piercings"] and EmmaX.pussy_covered:
        "images/Emma_standing/Emma_standing_piercings_pussy[EmmaX.outfit[piercings]]_covered.png"

    if not EmmaX.outfit["piercings"] or not EmmaX.breasts_covered:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_up_covered.png"
    else:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_down_covered.png"

    if EmmaX.outfit["neck"]:
        "images/Emma_standing/Emma_standing_neck[EmmaX.outfit[neck]].png"

    if EmmaX.outfit["top"] == "_dress_top":
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_shawl.png"

    if not EmmaX.outfit["jacket"]:
        Null()
    elif EmmaX.jacket_opened and EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up_open.png"
    elif EmmaX.jacket_opened:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_down_open.png"
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up.png"
    else:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_down.png"

    always:
        "Emma_head" pos (0.201, 0.31) zoom 0.5

    if not EmmaX.spunk["breasts"]:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_spunk_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_spunk_breasts_down.png"

    if EmmaX.spunk["belly"]:
        "images/Emma_standing/Emma_standing_spunk_belly.png"

    if not EmmaX.spunk["hand"]:
        Null()
    elif EmmaX.arm_pose == 2 and EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_hand_mouth.png"
    else:
        "images/Emma_standing/Emma_standing_spunk_hand.png"

    if not EmmaX.wet:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_water_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_water_breasts_down.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_arms[EmmaX.arm_pose].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_legs.png"

    if EmmaX.outfit["face_outer_accessory"]:
        "images/Emma_standing/Emma_standing_face_outer_accessory[EmmaX.outfit[face_outer_accessory]].png" pos (0.0, -0.09) zoom 0.5

    if EmmaX.outfit["held_item"] and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_held[EmmaX.outfit[held_item]].png"

    always:
        "Emma_standing_fondling_animations"

    anchor (0.5, 0.0) offset (20, 140) zoom 0.5

layeredimage Emma_hair_back:
    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet_back.png"
    else:
        "images/Emma_standing/Emma_standing_hair[EmmaX.outfit[hair]]_back.png"

    anchor (0.5, 0.5)

layeredimage Emma_head:
    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_head[EmmaX.brows]_wet[EmmaX.blushing].png"
    else:
        "images/Emma_standing/Emma_standing_head[EmmaX.brows][EmmaX.outfit[hair]][EmmaX.blushing].png"

    always:
        "images/Emma_standing/Emma_standing_brows[EmmaX.brows].png"

    always:
        "images/Emma_standing/Emma_standing_mouth[EmmaX.mouth].png"

    if EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_mouth[EmmaX.mouth].png"

    if EmmaX.eyes == "_closed":
        "images/Emma_standing/Emma_standing_eyes_closed.png"
    else:
        "Emma_blinking"

    if EmmaX.spunk["face"]:
        "images/Emma_standing/Emma_standing_spunk_face.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet.png"
    else:
        "images/Emma_standing/Emma_standing_hair[EmmaX.outfit[hair]].png"

    if EmmaX.spunk["hair"]:
        "images/Emma_standing/Emma_standing_spunk_hair[EmmaX.outfit[hair]].png"

    if EmmaX.outfit["face_outer_accessory"] != "_hat":
        Null()
    elif EmmaX.wet:
        "images/Emma_standing/Emma_standing_shadow_head_wet.png"
    else:
        "images/Emma_standing/Emma_standing_shadow_head[EmmaX.outfit[hair]].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_head.png"

    anchor (0.5, 0.5)

layeredimage Emma_sprite standing diamond:
    # always:
    #     "images/Emma_standing/Emma_standing_head_reference.png"

    if EmmaX.outfit["jacket"]:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]]_back.png"

    if EmmaX.outfit["bottom"] == "_dress_skirt":
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_back.png"

    if EmmaX.outfit["bra"] == "_corset" and not EmmaX.bra_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]][EmmaX.arm_pose]_back.png"

    if EmmaX.outfit["underwear"] and EmmaX.underwear_pulled_down:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_back_down.png"

    always:
        "Emma_hair_back_diamond" pos (0.201, 0.31) zoom 0.5

    always:
        "images/Emma_standing/Emma_standing_legs[EmmaX.arm_pose]_diamond.png"

    if EmmaX.pubes:
        "images/Emma_standing/Emma_standing_pubes_diamond.png"

    if EmmaX.outfit["bra"] in ["_corset", "_sports_bra", "_bikini_top"] and not EmmaX.bra_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_under.png"

    always:
        "images/Emma_standing/Emma_standing_arms[EmmaX.arm_pose]_diamond.png"

    if EmmaX.outfit["gloves"]:
        "images/Emma_standing/Emma_standing_gloves[EmmaX.outfit[gloves]][EmmaX.arm_pose].png"

    if EmmaX.outfit["piercings"]:
        "images/Emma_standing/Emma_standing_piercings_pussy[EmmaX.outfit[piercings]].png"

    if not EmmaX.outfit["underwear"]:
        Null()
    elif EmmaX.underwear_pulled_down and EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_down_grool.png"
    elif EmmaX.underwear_pulled_down:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_down.png"
    elif EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]]_grool.png"
    else:
        "images/Emma_standing/Emma_standing_underwear[EmmaX.outfit[underwear]].png"

    if EmmaX.outfit["hose"] and not EmmaX.hose_pulled_down:
        "images/Emma_standing/Emma_standing_hose[EmmaX.outfit[hose]].png"

    if EmmaX.outfit["bottom"] and EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_grool.png"
    elif EmmaX.grool:
        "images/Emma_standing/Emma_standing_grool.png"

    always:
        "Emma_grool_animations"

    if EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]:
        "images/Emma_standing/Emma_standing_spunk_pussy.png"

    always:
        "Emma_spunk_animations"

    if EmmaX.outfit["bodysuit"]:
        "images/Emma_standing/Emma_standing_bodysuit[EmmaX.outfit[bodysuit]][EmmaX.arm_pose].png"

    if not EmmaX.outfit["bottom"]:
        Null()
    elif EmmaX.bottom_pulled_down or EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_down.png"
    elif EmmaX.outfit["bottom"] == "_yoga_pants" and EmmaX.grool:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_grool.png"
    else:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]].png"

    if EmmaX.outfit["top"] in ["_nighty", "_towel"]:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]]_waist.png"

    if EmmaX.outfit["bottom"] == "_dress_skirt" and not EmmaX.upskirt:
        "images/Emma_standing/Emma_standing_bottom[EmmaX.outfit[bottom]]_front.png"

    if EmmaX.arm_pose == 1 or EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_breasts_up_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_breasts_down_diamond.png"

    if not EmmaX.outfit["piercings"]:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_up.png"
    else:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_down.png"

    if EmmaX.outfit["jacket"] and EmmaX.jacket_opened:
        "images/Emma_standing/Emma_standing_sleeves[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up.png"

    if not EmmaX.outfit["bra"]:
        Null()
    elif EmmaX.bra_pulled_up:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_up.png"
    # elif EmmaX.outfit["bra"] == "_corset" and EmmaX.outfit["top"]:
    #     "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]]_top.png"
    else:
        "images/Emma_standing/Emma_standing_bra[EmmaX.outfit[bra]].png"

    if EmmaX.outfit["boots"]:
        "images/Emma_standing/Emma_standing_boots[EmmaX.outfit[boots]].png"

    if not EmmaX.outfit["top"]:
        Null()
    elif EmmaX.top_pulled_up and EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up_up.png"
    elif EmmaX.top_pulled_up and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_down_up.png"
    elif EmmaX.top_pulled_up:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up.png"
    elif EmmaX.breasts_supported or EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_up.png"
    elif EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_down.png"
    else:
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose].png"

    if EmmaX.outfit["piercings"] and EmmaX.pussy_covered:
        "images/Emma_standing/Emma_standing_piercings_pussy[EmmaX.outfit[piercings]]_covered.png"

    if not EmmaX.outfit["piercings"] or not EmmaX.breasts_covered:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_up_covered.png"
    else:
        "images/Emma_standing/Emma_standing_piercings_breasts[EmmaX.outfit[piercings]]_down_covered.png"

    if EmmaX.outfit["neck"]:
        "images/Emma_standing/Emma_standing_neck[EmmaX.outfit[neck]].png"

    if EmmaX.outfit["top"] == "_dress_top":
        "images/Emma_standing/Emma_standing_top[EmmaX.outfit[top]][EmmaX.arm_pose]_shawl.png"

    if not EmmaX.outfit["jacket"]:
        Null()
    elif EmmaX.jacket_opened and EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up_up.png"
    elif EmmaX.jacket_opened:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_down_up.png"
    elif EmmaX.jacket_opened or EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_up.png"
    else:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.outfit[jacket]][EmmaX.arm_pose]_down.png"

    always:
        "Emma_head_diamond" pos (0.201, 0.31) zoom 0.5

    if not EmmaX.spunk["breasts"]:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_spunk_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_spunk_breasts_down.png"

    if EmmaX.spunk["belly"]:
        "images/Emma_standing/Emma_standing_spunk_belly.png"

    if not EmmaX.spunk["hand"]:
        Null()
    elif EmmaX.arm_pose == 2 and EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_hand_mouth.png"
    else:
        "images/Emma_standing/Emma_standing_spunk_hand.png"

    if not EmmaX.wet:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_standing/Emma_standing_water_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_water_breasts_down.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_arms[EmmaX.arm_pose].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_legs.png"

    if EmmaX.outfit["face_outer_accessory"]:
        "images/Emma_standing/Emma_standing_face_outer_accessory[EmmaX.outfit[face_outer_accessory]].png" pos (0.0, -0.09) zoom 0.5

    if EmmaX.outfit["held_item"] and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_held[EmmaX.outfit[held_item]].png"

    # always:
    #     "Emma_standing_fondling_animations"

    anchor (0.5, 0.0) offset (20, 140) zoom 0.5

layeredimage Emma_hair_back_diamond:
    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet_back_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_hair[EmmaX.outfit[hair]]_back_diamond.png"

    anchor (0.5, 0.5)

layeredimage Emma_head_diamond:
    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_head[EmmaX.brows]_wet[EmmaX.blushing]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_head[EmmaX.brows][EmmaX.outfit[hair]][EmmaX.blushing]_diamond.png"

    always:
        "images/Emma_standing/Emma_standing_brows[EmmaX.brows]_diamond.png"

    if EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_mouth[EmmaX.mouth]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_mouth[EmmaX.mouth]_diamond.png"

    if EmmaX.eyes == "_closed":
        "images/Emma_standing/Emma_standing_eyes_closed_diamond.png"
    else:
        "Emma_blinking_diamond"

    if EmmaX.spunk["face"]:
        "images/Emma_standing/Emma_standing_spunk_face.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_hair[EmmaX.outfit[hair]]_diamond.png"

    if EmmaX.spunk["hair"]:
        "images/Emma_standing/Emma_standing_spunk_hair[EmmaX.outfit[hair]].png"

    if EmmaX.outfit["face_outer_accessory"] != "_hat":
        Null()
    elif EmmaX.wet:
        "images/Emma_standing/Emma_standing_shadow_head_wet.png"
    else:
        "images/Emma_standing/Emma_standing_shadow_head[EmmaX.outfit[hair]].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_head.png"

    anchor (0.5, 0.5)

image Emma_handjob_under:
    "images/Emma_handjob/Emma_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Emma_handjob_over:
    "images/Emma_handjob/Emma_handjob_hand_over.png"

    anchor (0.5, 0.5)

layeredimage Emma_titjob_breasts:
    if EmmaX.outfit["gloves"] or EmmaX.outfit["top"] == "_dress_top" or EmmaX.outfit["jacket"] == "_jacket":
        "images/Emma_titjob/Emma_titjob_forearms_covered.png"
    else:
        "images/Emma_titjob/Emma_titjob_forearms.png"

    if EmmaX.outfit["gloves"]:
        "images/Emma_titjob/Emma_titjob_breasts_gloved.png"
    else:
        "images/Emma_titjob/Emma_titjob_breasts.png"

    if EmmaX.outfit["piercings"]:
        "images/Emma_titjob/Emma_titjob_piercings[EmmaX.outfit[piercings]].png"

    if not EmmaX.outfit["bra"]:
        Null()
    elif EmmaX.outfit["bra"] == "_sports_bra" and EmmaX.bra_pulled_up:
        "images/Emma_titjob/Emma_titjob_bra[EmmaX.outfit[bra]]_up.png"
    elif EmmaX.outfit["bra"] != "_corset":
        "images/Emma_titjob/Emma_titjob_bra[EmmaX.outfit[bra]].png"

    if EmmaX.outfit["piercings"] and EmmaX.breasts_covered:
        "images/Emma_titjob/Emma_titjob_piercings[EmmaX.outfit[piercings]]_covered.png"

    if EmmaX.spunk["breasts"]:
        "images/Emma_titjob/Emma_titjob_spunk_breasts_over.png"

    anchor (0.5, 0.5)

layeredimage Emma_blowjob_hair_back:
    if EmmaX.wet or EmmaX.outfit["hair"] != "_wavy":
        Null()
    else:
        "images/Emma_blowjob/Emma_blowjob_hair_back.png"

    anchor (0.5, 0.5)

layeredimage Emma_blowjob_body:
    # if "blanket" in EmmaX.recent_history:
    #     "images/Kitty_blowjob/Kitty_blowjob_blanket.png" pos (0.0, 0.0) zoom 0.8

    always:
        "Emma_sex_body"

    anchor (0.5, 0.5)

layeredimage Emma_blowjob_head:
    if EmmaX.wet:
        "images/Emma_blowjob/Emma_blowjob_hair_wet_mid.png"
    else:
        "images/Emma_blowjob/Emma_blowjob_hair[EmmaX.outfit[hair]]_mid.png"

    always:
        "images/Emma_blowjob/Emma_blowjob_face.png"
    # if renpy.showing("Emma_sprite blowjob") and action_speed > 2 and EmmaX.blushing:
    #     "images/Emma_blowjob/Emma_blowjob_face_open_blush.png"
    # elif renpy.showing("Emma_sprite blowjob") and action_speed > 2:
    #     "images/Emma_blowjob/Emma_blowjob_face_open.png"
    # elif EmmaX.blushing:
    #     "images/Emma_blowjob/Emma_blowjob_face_closed_blush.png"
    # else:
    #     "images/Emma_blowjob/Emma_blowjob_face_closed.png"

    if renpy.showing("Emma_sprite titjob") and action_speed > 2:
        "images/Emma_blowjob/Emma_blowjob_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and action_speed == 1:
        "images/Emma_blowjob/Emma_blowjob_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and action_speed == 2:
        "Emma_blowjob_mouth_animations"
    elif renpy.showing("Emma_sprite blowjob") and action_speed > 2:
        "images/Emma_blowjob/Emma_blowjob_mouth_sucking.png"
    else:
        "images/Emma_blowjob/Emma_blowjob_mouth[EmmaX.mouth].png"

    if not EmmaX.spunk["mouth"]:
        Null()
    elif renpy.showing("Emma_sprite titjob") and action_speed > 2:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and action_speed == 1:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and action_speed > 2:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_sucking_under.png"
    elif EmmaX.mouth == "_sucking":
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth[EmmaX.mouth]_under.png"
    else:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth[EmmaX.mouth].png"

    always:
        "images/Emma_blowjob/Emma_blowjob_brows[EmmaX.brows].png"

    if EmmaX.eyes == "_closed":
        "images/Emma_blowjob/Emma_blowjob_eyes_closed.png"
    else:
        "Emma_blowjob_blinking"

    if EmmaX.spunk["face"]:
        "images/Emma_blowjob/Emma_blowjob_spunk_face.png"

    if EmmaX.wet:
        "images/Emma_blowjob/Emma_blowjob_hair_wet.png"
    else:
        "images/Emma_blowjob/Emma_blowjob_hair[EmmaX.outfit[hair]].png"

    # always:
    #     "images/Emma_blowjob/Emma_blowjob_hat_reference.png"

    # if EmmaX.outfit["face_outer_accessory"]:
    #     "images/Emma_standing/Emma_standing_face_outer_accessory[EmmaX.outfit[face_outer_accessory]].png" pos (-0.044, -0.095) zoom 1.3

    anchor (0.5, 0.5)

layeredimage Emma_sex_body:
    always:
        "images/Emma_sex/Emma_sex_body[EmmaX.outfit[gloves]].png"

    if renpy.showing("Emma_sprite titjob"):
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_sex/Emma_sex_breasts_up.png"
    else:
        "images/Emma_sex/Emma_sex_breasts_down.png"

    if renpy.showing("Emma_sprite titjob"):
        Null()
    elif EmmaX.outfit["piercings"] and not EmmaX.breasts_supported:
        "images/Emma_sex/Emma_sex_piercings_breasts[EmmaX.outfit[piercings]]_down.png"

    if EmmaX.outfit["bra"] in ["_sports_bra", "_bikini_top"] and (EmmaX.top_pulled_up or renpy.showing("Emma_sprite titjob")):
        "images/Emma_sex/Emma_sex_bra[EmmaX.outfit[bra]]_up.png"
    elif EmmaX.outfit["bra"]:
        "images/Emma_sex/Emma_sex_bra[EmmaX.outfit[bra]].png"

    if not EmmaX.outfit["jacket"]:
        Null()
    elif renpy.showing("Emma_sprite titjob"):
        "images/Emma_titjob/Emma_titjob_jacket[EmmaX.outfit[jacket]].png"
    elif EmmaX.breasts_supported and EmmaX.jacket_opened:
        "images/Emma_sex/Emma_sex_jacket[EmmaX.outfit[jacket]]_up_open.png"
    elif EmmaX.jacket_opened:
        "images/Emma_sex/Emma_sex_jacket[EmmaX.outfit[jacket]]_down_open.png"
    elif EmmaX.breasts_supported:
        "images/Emma_sex/Emma_sex_jacket[EmmaX.outfit[jacket]]_up.png"
    else:
        "images/Emma_sex/Emma_sex_jacket[EmmaX.outfit[jacket]]_down.png"

    if not EmmaX.outfit["top"]:
        Null()
    elif EmmaX.outfit["top"] == "_dress_top" and renpy.showing("Emma_sprite titjob"):
        "images/Emma_titjob/Emma_titjob_top[EmmaX.outfit[top]].png"
    elif EmmaX.top_pulled_up:
        "images/Emma_sex/Emma_sex_top[EmmaX.outfit[top]]_up_up.png"
    elif EmmaX.breasts_supported:
        "images/Emma_sex/Emma_sex_top[EmmaX.outfit[top]]_up.png"
    else:
        "images/Emma_sex/Emma_sex_top[EmmaX.outfit[top]]_down.png"

    if renpy.showing("Emma_sprite titjob"):
        Null()
    elif not EmmaX.outfit["piercings"] or not EmmaX.breasts_covered:
        Null()
    elif EmmaX.breasts_supported:
        "images/Emma_sex/Emma_sex_piercings_breasts[EmmaX.outfit[piercings]]_up_covered.png"
    else:
        "images/Emma_sex/Emma_sex_piercings_breasts[EmmaX.outfit[piercings]]_down_covered.png"

    if not EmmaX.spunk["breasts"]:
        Null()
    elif renpy.showing("Emma_sprite titjob"):
        "images/Emma_titjob/Emma_titjob_spunk_breasts_under.png"
    else:
        "images/Emma_sex/Emma_sex_spunk_breasts.png"

    anchor (0.5, 0.5)
