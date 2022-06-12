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

    if JubesX.outfit["bra"] and JubesX.bra_pulled_up:
        "images/Jubes_standing/Jubes_standing_bra[JubesX.outfit[bra]]_up.png"
    elif JubesX.outfit["bra"]:
        "images/Jubes_standing/Jubes_standing_bra[JubesX.outfit[bra]].png"

    if JubesX.outfit["underwear"] and JubesX.underwear_pulled_down and (not JubesX.outfit["bottom"] or JubesX.wearing_skirt) and JubesX.grool > 1:
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]]_down_grool.png"
    elif JubesX.outfit["underwear"] and JubesX.underwear_pulled_down and (not JubesX.outfit["bottom"] or JubesX.wearing_skirt):
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]]_down.png"
    elif JubesX.outfit["underwear"] and JubesX.grool > 1:
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]]_grool.png"
    elif JubesX.outfit["underwear"]:
        "images/Jubes_standing/Jubes_standing_underwear[JubesX.outfit[underwear]].png"

    if JubesX.outfit["hose"]:
        "images/Jubes_standing/Jubes_standing_hose[JubesX.outfit[hose]].png"

    always:
        "Jubes_grool_animations"

    # if JubesX.spunk["pussy"] or JubesX.spunk["anus"]:
    #     "images/Jubes_standing/Jubes_standing_spunk_pussy.png"

    always:
        "Jubes_spunk_animations"

    if JubesX.outfit["bottom"] and (JubesX.bottom_pulled_down or JubesX.upskirt):
        "images/Jubes_standing/Jubes_standing_bottom[JubesX.outfit[bottom]]_down.png"
    elif JubesX.outfit["bottom"]:
        "images/Jubes_standing/Jubes_standing_bottom[JubesX.outfit[bottom]].png"

    if JubesX.outfit["bottom"] and not JubesX.bottom_pulled_down and JubesX.grool > 1:
        "images/Jubes_standing/Jubes_standing_grool.png"
    elif JubesX.grool:
        "images/Jubes_standing/Jubes_standing_grool.png"

    if JubesX.outfit["top"] == "_towel":
        "images/Jubes_standing/Jubes_standing_top[JubesX.outfit[top]][JubesX.arm_pose].png"
    elif JubesX.outfit["top"] and JubesX.top_pulled_up:
        "images/Jubes_standing/Jubes_standing_top[JubesX.outfit[top]]_up.png"
    elif JubesX.outfit["top"]:
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

    if JubesX.outfit["suspenders"] and JubesX.suspenders_aside:
        "images/Jubes_standing/Jubes_standing_suspenders[JubesX.outfit[suspenders]]_aside.png"
    elif JubesX.outfit["suspenders"]:
        "images/Jubes_standing/Jubes_standing_suspenders[JubesX.outfit[suspenders]].png"

    if JubesX.outfit["jacket"] and JubesX.upskirt:
        "images/Jubes_standing/Jubes_standing_jacket[JubesX.outfit[jacket]][JubesX.arm_pose]_up.png"
    elif JubesX.outfit["jacket"]:
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

image Jubes_back_hair:
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

    always:
        "images/Jubes_standing/Jubes_standing_hair[JubesX.outfit[hair]].png"

    if JubesX.spunk["hair"]:
        "images/Jubes_standing/Jubes_standing_spunk_hair.png"

    if JubesX.wet:
        "images/Jubes_standing/Jubes_standing_water_head.png"

    anchor (0.5, 0.5)

image Jubes_handjob_under:
    "images/Jubes_handjob/Jubes_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Jubes_handjob_over:
    "images/Jubes_handjob/Jubes_handjob_hand_over.png"

    anchor (0.5, 0.5)
