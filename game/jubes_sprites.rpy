layeredimage Jubes_sprite standing:
    # always:
    #     "images/Jubes_standing/Jubes_standing_head_reference.png"

    if JubesX.outfit["jacket"]:
        "images/Jubes_standing/Jubes_standing_neck[JubesX.outfit[jacket]].png"

    if JubesX.outfit["jacket"] == "_open_jacket":
        "images/Jubes_standing/Jubes_standing_back_outer_accessory[JubesX.outfit[jacket]][JubesX.arm_pose].png"

    if JubesX.outfit["bottom"] and JubesX.bottom_pulled_down:
        "images/Jubes_standing/Jubes_standing_back_outer_accessory[JubesX.outfit[bottom]]_down.png"

    if JubesX.outfit["underwear"] and JubesX.underwear_pulled_down:
        "images/Jubes_standing/Jubes_standing_back_inner_accessory[JubesX.outfit[underwear]]_down.png"

    always:
        "Jubes_back_hair" pos (0.161, 0.198) zoom 0.37

    always:
        "images/Jubes_standing/Jubes_standing_body[JubesX.arm_pose].png"

    if JubesX.pubes:
        "images/Jubes_standing/Jubes_standing_pubes.png"

    if JubesX.outfit["piercings"]:
        "images/Jubes_standing/Jubes_standing_piercings_breasts[JubesX.outfit[piercings]].png"

    if JubesX.outfit["piercings"]:
        "images/Jubes_standing/Jubes_standing_piercings_pussy[JubesX.outfit[piercings]].png"

    if not JubesX.outfit["bra"]:
        Null()
    elif JubesX.bra_pulled_up:
        "images/Jubes_standing/Jubes_standing_bra[JubesX.outfit[bra]]_up.png"
    else:
        "images/Jubes_standing/Jubes_standing_bra[JubesX.outfit[bra]].png"

    if not JubesX.outfit["underwear"]:
        Null()
    elif JubesX.underwear_pulled_down and JubesX.grool > 1:
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]]_down_grool.png"
    elif JubesX.underwear_pulled_down:
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]]_down.png"
    elif JubesX.grool > 1:
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]]_grool.png"
    else:
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]].png"

    if JubesX.outfit["hose"]:
        "images/Jubes_standing/Jubes_standing_hose[JubesX.outfit[hose]].png"

    always:
        "Jubes_grool_animations"

    # if JubesX.spunk["pussy"] or JubesX.spunk["anus"]:
    #     "images/Jubes_standing/Jubes_standing_spunk_pussy.png"

    always:
        "Jubes_spunk_animations"

    if not JubesX.outfit["bottom"]:
        Null()
    elif JubesX.bottom_pulled_down or JubesX.upskirt:
        "images/Jubes_standing/Jubes_standing_bottom[JubesX.outfit[bottom]]_down.png"
    else:
        "images/Jubes_standing/Jubes_standing_bottom[JubesX.outfit[bottom]].png"

    if JubesX.outfit["bottom"] and not JubesX.bottom_pulled_down and JubesX.grool > 1:
        "images/Jubes_standing/Jubes_standing_grool.png"
    elif JubesX.grool:
        "images/Jubes_standing/Jubes_standing_grool.png"

    if not JubesX.outfit["top"]:
        Null()
    elif JubesX.outfit["top"] == "_towel":
        "images/Jubes_standing/Jubes_standing_top[JubesX.outfit[top]][JubesX.arm_pose].png"
    elif JubesX.top_pulled_up:
        "images/Jubes_standing/Jubes_standing_top[JubesX.outfit[top]]_up.png"
    else:
        "images/Jubes_standing/Jubes_standing_top[JubesX.outfit[top]].png"

    if JubesX.outfit["neck"]:
        "images/Jubes_standing/Jubes_standing_neck[JubesX.outfit[neck]].png"

    always:
        "Jubes_head" pos (0.161, 0.198) zoom 0.37

    if JubesX.outfit["piercings"] and JubesX.pussy_covered:
        "images/Jubes_standing/Jubes_standing_piercings_pussy[JubesX.outfit[piercings]]_covered.png"

    if JubesX.outfit["piercings"] and JubesX.breasts_covered:
        "images/Jubes_standing/Jubes_standing_piercings_breasts[JubesX.outfit[piercings]]_covered.png"

    if JubesX.outfit["jacket"] == "_closed_jacket" and JubesX.arm_pose == 2:
        "images/Jubes_standing/Jubes_standing_sleeves[JubesX.outfit[jacket]][JubesX.arm_pose].png"

    if not JubesX.outfit["suspenders"]:
        Null()
    elif JubesX.suspenders_aside:
        "images/Jubes_standing/Jubes_standing_suspenders[JubesX.outfit[suspenders]]_aside.png"
    else:
        "images/Jubes_standing/Jubes_standing_suspenders[JubesX.outfit[suspenders]].png"

    if not JubesX.outfit["jacket"]:
        Null()
    elif JubesX.upskirt:
        "images/Jubes_standing/Jubes_standing_jacket[JubesX.outfit[jacket]][JubesX.arm_pose]_up.png"
    else:
        "images/Jubes_standing/Jubes_standing_jacket[JubesX.outfit[jacket]][JubesX.arm_pose].png"

    always:
        "images/Jubes_standing/Jubes_standing_hand[JubesX.arm_pose]_left.png"

    if JubesX.spunk["breasts"]:
        "images/Jubes_standing/Jubes_standing_spunk_breasts.png"

    if JubesX.spunk["belly"]:
        "images/Jubes_standing/Jubes_standing_spunk_belly.png"

    if JubesX.wet:
        "images/Jubes_standing/Jubes_standing_water_body[JubesX.arm_pose].png"

    if JubesX.wet and JubesX.arm_pose == 1:
        "images/Jubes_standing/Jubes_standing_water_arm[JubesX.arm_pose].png"

    if JubesX.outfit["held_item"] and JubesX.arm_pose == 1:
        "images/Jubes_standing/Jubes_standing_held[JubesX.outfit[held_item]].png"

    # always:
    #     "Jubes_standing_fondling_animations"

    anchor (0.5, 0.0) offset (15, 150) zoom 1.1

layeredimage Jubes_back_hair:
    if JubesX.wet:
        "images/Jubes_standing/Jubes_standing_back_hair_wet.png"
    else:
        "images/Jubes_standing/Jubes_standing_back_hair[JubesX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Jubes_head:
    always:
        "images/Jubes_standing/Jubes_standing_head[JubesX.blushing].png"

    always:
        "images/Jubes_standing/Jubes_standing_brows[JubesX.brows].png"

    if JubesX.spunk["mouth"]:
        "images/Jubes_standing/Jubes_standing_spunk_mouth[JubesX.mouth].png"
    else:
        "images/Jubes_standing/Jubes_standing_mouth[JubesX.mouth].png"

    if JubesX.eyes == "_closed":
        "images/Jubes_standing/Jubes_standing_eyes_closed.png"
    else:
        "Jubes_blinking"

    if JubesX.outfit["face_inner_accessory"]:
        "images/Jubes_standing/Jubes_standing_face_inner_accessory[JubesX.outfit[face_inner_accessory]].png"

    if JubesX.spunk["chin"]:
        "images/Jubes_standing/Jubes_standing_spunk_chin.png"

    if JubesX.spunk["face"]:
        "images/Jubes_standing/Jubes_standing_spunk_face.png"

    if JubesX.wet:
        "images/Jubes_standing/Jubes_standing_hair_wet.png"
    else:
        "images/Jubes_standing/Jubes_standing_hair[JubesX.outfit[hair]].png"

    if JubesX.spunk["hair"]:
        "images/Jubes_standing/Jubes_standing_spunk_hair[JubesX.outfit[hair]].png"

    if JubesX.wet:
        "images/Jubes_standing/Jubes_standing_water_head.png"

    anchor (0.5, 0.5)

image Jubes_handjob_under:
    "images/Jubes_handjob/Jubes_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Jubes_handjob_over:
    "images/Jubes_handjob/Jubes_handjob_hand_over.png"

    anchor (0.5, 0.5)

image Jubes_titjob_jacket_back:
    "images/Jubes_titjob/Jubes_titjob_jacket[JubesX.outfit[jacket]]_back.png"

    anchor (0.5, 0.5)

layeredimage Jubes_titjob_bra_back:
    if JubesX.outfit["bra"] not in ["_sports_bra", "_bikini_top"]:
        Null()
    elif JubesX.outfit["bra"] == "_bikini_top" and JubesX.bra_pulled_up:
        "images/Jubes_titjob/Jubes_titjob_bra[JubesX.outfit[bra]]_back_up.png"
    else:
        "images/Jubes_titjob/Jubes_titjob_bra[JubesX.outfit[bra]]_back.png"

    anchor (0.5, 0.5)

layeredimage Jubes_titjob_body:
    always:
        "images/Jubes_titjob/Jubes_titjob_body.png"

    if JubesX.outfit["jacket"]:
        "images/Jubes_titjob/Jubes_titjob_jacket[JubesX.outfit[jacket]].png"

    if JubesX.outfit["top"]:
        "images/Jubes_titjob/Jubes_titjob_top[JubesX.outfit[top]]_base.png"

    if JubesX.spunk["breasts"]:
        "images/Jubes_titjob/Jubes_titjob_spunk_breasts_under.png"

    anchor (0.5, 0.5)

image Jubes_titjob_breasts_under:
    "images/Jubes_titjob/Jubes_titjob_breasts_under.png"

    anchor (0.5, 0.5)

layeredimage Jubes_titjob_breasts:
    always:
        "images/Jubes_titjob/Jubes_titjob_breasts.png"

    if not JubesX.outfit["bra"]:
        Null()
    elif JubesX.bra_pulled_up:
        "images/Jubes_titjob/Jubes_titjob_bra[JubesX.outfit[bra]]_up.png"
    else:
        "images/Jubes_titjob/Jubes_titjob_bra[JubesX.outfit[bra]].png"

    if JubesX.outfit["top"] != "_tube_top":
        Null()
    elif JubesX.top_pulled_up:
        "images/Jubes_titjob/Jubes_titjob_top[JubesX.outfit[top]]_up.png"
    else:
        "images/Jubes_titjob/Jubes_titjob_top[JubesX.outfit[top]].png"

    if JubesX.outfit["piercings"]:
        "images/Jubes_titjob/Jubes_titjob_piercings[JubesX.outfit[piercings]].png"

    if not JubesX.outfit["piercings"] or not JubesX.breasts_covered:
        Null()
    elif JubesX.outfit["top"] in ["_pink_shirt", "_tube_top"]:
        "images/Jubes_titjob/Jubes_titjob_piercings[JubesX.outfit[piercings]][JubesX.outfit[top]]_covered.png"
    elif JubesX.outfit["bra"]:
        "images/Jubes_titjob/Jubes_titjob_piercings[JubesX.outfit[piercings]][JubesX.outfit[bra]]_covered.png"

    if JubesX.spunk["breasts"]:
        "images/Jubes_titjob/Jubes_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Jubes_blowjob_head:
    if JubesX.blushing == "_blush2":
        "images/Jubes_blowjob/Jubes_blowjob_head_blush.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_head.png"

    if renpy.showing("Jubes_sprite titjob") and action_speed == 3:
        "images/Jubes_blowjob/Jubes_blowjob_mouth_tongue.png"
    elif renpy.showing("Jubes_sprite blowjob") and action_speed == 1:
        "images/Jubes_blowjob/Jubes_blowjob_mouth_tongue.png"
    elif renpy.showing("Jubes_sprite blowjob") and action_speed > 2:
        "images/Jubes_blowjob/Jubes_blowjob_mouth_sucking.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_mouth[JubesX.mouth].png"

    if renpy.showing("Jubes_sprite blowjob") and action_speed == 2:
        "Jubes_blowjob_mouth_animations"

    if not JubesX.spunk["mouth"]:
        Null()
    elif renpy.showing("Jubes_sprite blowjob") and action_speed == 1:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Jubes_sprite blowjob") and action_speed > 2:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth_sucking_under.png"
    elif JubesX.mouth == "_sucking":
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth[JubesX.mouth]_under.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth[JubesX.mouth].png"

    always:
        "images/Jubes_blowjob/Jubes_blowjob_brows[JubesX.brows].png"

    if JubesX.eyes == "_closed":
        "images/Jubes_blowjob/Jubes_blowjob_eyes_closed.png"
    else:
        "Jubes_blowjob_blinking"

    if JubesX.outfit["face_inner_accessory"]:
        "images/Jubes_blowjob/Jubes_blowjob_face_inner_accessory[JubesX.outfit[face_inner_accessory]].png"

    if JubesX.spunk["face"]:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_face.png"

    if JubesX.wet:
        "images/Jubes_blowjob/Jubes_blowjob_water_head.png"

    if JubesX.wet:
        "images/Jubes_blowjob/Jubes_blowjob_hair_wet.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_hair[JubesX.outfit[hair]].png"

    if JubesX.spunk["hair"]:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_hair.png"

    anchor (0.5, 0.5)
