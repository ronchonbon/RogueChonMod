layeredimage Laura_sprite standing:
    # always:
    #     "images/Laura_standing/Laura_standing_head_reference.png"

    if not LauraX.outfit["jacket"]:
        Null()
    elif LauraX.jacket_opened:
        "images/Laura_standing/Laura_standing_jacket[LauraX.outfit[jacket]]_back_up.png"
    else:
        "images/Laura_standing/Laura_standing_jacket[LauraX.outfit[jacket]]_back.png"

    if LauraX.outfit["underwear"] and LauraX.underwear_pulled_down:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]]_back_down.png"

    always:
        "images/Laura_standing/Laura_standing_arm[LauraX.arm_pose]_right.png"

    if not renpy.showing("Laura_sprite blowjob"):
        "Laura_hair_back" pos (0.209, 0.371) zoom 0.5

    always:
        "images/Laura_standing/Laura_standing_body.png"

    always:
        "images/Laura_standing/Laura_standing_arms[LauraX.arm_pose]_mid.png"

    if LauraX.pubes:
        "images/Laura_standing/Laura_standing_pubes.png"

    always:
        "images/Laura_standing/Laura_standing_breasts.png"

    if LauraX.outfit["piercings"]:
        "images/Laura_standing/Laura_standing_piercings_breasts[LauraX.outfit[piercings]].png"

    if LauraX.outfit["piercings"]:
        "images/Laura_standing/Laura_standing_piercings_pussy[LauraX.outfit[piercings]].png"

    if LauraX.outfit["nipple_accessories"]:
        "images/Laura_standing/Laura_standing_nipple_accessories[LauraX.outfit[nipple_accessories]].png"

    if not LauraX.outfit["bra"]:
        Null()
    elif LauraX.bra_pulled_up:
        "images/Laura_standing/Laura_standing_bra[LauraX.outfit[bra]]_up.png"
    else:
        "images/Laura_standing/Laura_standing_bra[LauraX.outfit[bra]].png"

    if not LauraX.outfit["underwear"]:
        Null()
    elif LauraX.underwear_pulled_down and LauraX.grool > 1 and LauraX.outfit["underwear"] not in ["leather_panties", "bikini_bottoms"]:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]]_down_grool.png"
    elif LauraX.underwear_pulled_down:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]]_down.png"
    elif LauraX.grool > 1 and LauraX.outfit["underwear"] not in ["leather_panties", "bikini_bottoms"]:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]]_grool.png"
    else:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]].png"

    if LauraX.hose_pulled_down:
        Null()
    elif LauraX.outfit["hose"] == "stockings_and_garterbelt":
        "images/Laura_standing/Laura_standing_hose_stockings.png"
    elif LauraX.outfit["hose"]:
        "images/Laura_standing/Laura_standing_hose[LauraX.outfit[hose]].png"

    if not LauraX.hose_pulled_down and LauraX.outfit["hose"] == "stockings_and_garterbelt":
        "images/Laura_standing/Laura_standing_hose_garterbelt.png"

    if LauraX.outfit["bottom"] and LauraX.grool > 1:
        "images/Laura_standing/Laura_standing_grool.png"
    elif LauraX.grool:
        "images/Laura_standing/Laura_standing_grool.png"

    always:
        "Laura_grool_animations"

    if LauraX.spunk["pussy"] or LauraX.spunk["anus"]:
        "images/Laura_standing/Laura_standing_spunk_pussy.png"

    always:
        "Laura_spunk_animations"

    if LauraX.outfit["bodysuit"]:
        "images/Laura_standing/Laura_standing_bodysuit[LauraX.outfit[bodysuit]].png"

    if not LauraX.outfit["bottom"]:
        Null()
    elif LauraX.bottom_pulled_down or LauraX.upskirt:
        "images/Laura_standing/Laura_standing_bottom[LauraX.outfit[bottom]]_down.png"
    else:
        "images/Laura_standing/Laura_standing_bottom[LauraX.outfit[bottom]].png"

    if LauraX.outfit["dress"]:
        "images/Laura_standing/Laura_standing_dress[LauraX.outfit[dress]][LauraX.arm_pose].png"

    if LauraX.outfit["top"]:
        "images/Laura_standing/Laura_standing_top[LauraX.outfit[top]].png"

    if LauraX.outfit["neck"]:
        "images/Laura_standing/Laura_standing_neck[LauraX.outfit[neck]].png"

    if not renpy.showing("Laura_sprite blowjob"):
        "Laura_head" pos (0.209, 0.371) zoom 0.5

    if LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_arm[LauraX.arm_pose]_left.png"

    if not LauraX.outfit["gloves"]:
        Null()
    elif LauraX.outfit["gloves"] == "gloves":
        "images/Laura_standing/Laura_standing_gloves[LauraX.outfit[gloves]][LauraX.arm_pose]_right.png"
    elif LauraX.outfit["gloves"] == "bunny_gloves" and LauraX.arm_pose == 1:
        "images/Laura_standing/Laura_standing_gloves[LauraX.outfit[gloves]][LauraX.arm_pose].png"
    else:
        "images/Laura_standing/Laura_standing_gloves[LauraX.outfit[gloves]][LauraX.arm_pose].png"

    if LauraX.outfit["gloves"] == "gloves" and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_gloves[LauraX.outfit[gloves]][LauraX.arm_pose]_left.png"

    if LauraX.outfit["dress"] == "Mavis_dress":
        "images/Laura_standing/Laura_standing_sleeves[LauraX.outfit[dress]][LauraX.arm_pose].png"

    if LauraX.outfit["piercings"] and LauraX.pussy_covered:
        "images/Laura_standing/Laura_standing_piercings_pussy[LauraX.outfit[piercings]]_covered.png"

    if LauraX.outfit["piercings"] and LauraX.breasts_covered:
        "images/Laura_standing/Laura_standing_piercings_breasts[LauraX.outfit[piercings]]_covered.png"

    if LauraX.outfit["jacket"] and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_jacket[LauraX.outfit[jacket]][LauraX.arm_pose]_sleeves.png"

    if not LauraX.outfit["suspenders"]:
        Null()
    elif LauraX.suspenders_aside:
        "images/Laura_standing/Laura_standing_suspenders[LauraX.outfit[suspenders]]_aside.png"
    else:
        "images/Laura_standing/Laura_standing_suspenders[LauraX.outfit[suspenders]].png"

    if not LauraX.outfit["jacket"]:
        Null()
    elif LauraX.jacket_opened:
        "images/Laura_standing/Laura_standing_jacket[LauraX.outfit[jacket]][LauraX.arm_pose]_up.png"
    else:
        "images/Laura_standing/Laura_standing_jacket[LauraX.outfit[jacket]][LauraX.arm_pose].png"

    if LauraX.claws and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_claws[LauraX.arm_pose].png"

    if LauraX.spunk["breasts"]:
        "images/Laura_standing/Laura_standing_spunk_breasts.png"

    if LauraX.spunk["belly"]:
        "images/Laura_standing/Laura_standing_spunk_belly.png"

    if LauraX.spunk["hand"] and LauraX.arm_pose == 1:
        "images/Laura_standing/Laura_standing_spunk_hand.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_body[LauraX.arm_pose].png"

    if LauraX.wet and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_water_arm[LauraX.arm_pose].png"

    if LauraX.held_item and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_held[LauraX.outfit[held_item]].png"

    always:
        "Laura_standing_fondling_animations"

    anchor (0.5, 0.0) offset (45, 170) zoom 0.5

layeredimage Laura_hair_back:
    if LauraX.wet:
        "images/Laura_standing/Laura_standing_hair_wet_back.png"
    else:
        "images/Laura_standing/Laura_standing_hair[LauraX.outfit[hair]]_back.png"

    anchor (0.5, 0.5)

layeredimage Laura_head:
    if not renpy.showing("Laura_sprite sex"):
        Null()
    elif LauraX.wet:
        "images/Laura_sex/Laura_sex_hair_wet_back.png"
    else:
        "images/Laura_sex/Laura_sex_hair[LauraX.outfit[hair]]_back.png"

    always:
        "images/Laura_standing/Laura_standing_head.png"
        # "images/Laura_standing/Laura_standing_head[LauraX.blushing].png"

    if LauraX.blushing == "_blush2":
        "images/Laura_standing/Laura_standing_brows_[LauraX.brows]_blush.png"
    else:
        "images/Laura_standing/Laura_standing_brows_[LauraX.brows].png"

    if renpy.showing("Laura_sprite titjob") and action_speed in [3, 5]:
        "images/Laura_standing/Laura_standing_mouth_tongue.png"
    else:
        "images/Laura_standing/Laura_standing_mouth_[LauraX.mouth].png"

    if not LauraX.spunk["mouth"]:
        Null()
    elif renpy.showing("Laura_sprite titjob") and action_speed in [3, 5]:
        "images/Laura_standing/Laura_standing_spunk_mouth_tongue.png"
    else:
        "images/Laura_standing/Laura_standing_spunk_mouth_[LauraX.mouth].png"

    if LauraX.eyes == "closed":
        "images/Laura_standing/Laura_standing_eyes_closed.png"
    else:
        "Laura_blinking"

    if LauraX.spunk["chin"]:
        "images/Laura_standing/Laura_standing_spunk_chin.png"

    if LauraX.spunk["face"]:
        "images/Laura_standing/Laura_standing_spunk_face.png"

    if renpy.showing("Laura_sprite titjob") or renpy.showing("Laura_sprite sex"):
        Null()
    else:
        "images/Laura_standing/Laura_standing_hair_mid.png"

    if renpy.showing("Laura_sprite sex") and LauraX.wet:
        "images/Laura_sex/Laura_sex_hair_wet.png"
    elif renpy.showing("Laura_sprite sex"):
        "images/Laura_sex/Laura_sex_hair[LauraX.outfit[hair]].png"
    elif LauraX.wet:
        "images/Laura_standing/Laura_standing_hair_wet.png"
    else:
        "images/Laura_standing/Laura_standing_hair[LauraX.outfit[hair]].png"

    if LauraX.spunk["hair"]:
        "images/Laura_standing/Laura_standing_spunk_hair.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_head.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_hair.png"

    if LauraX.outfit["face_outer_accessory"]:
        "images/Laura_standing/Laura_standing_face_outer_accessory[LauraX.outfit[face_outer_accessory]].png"

    anchor (0.5, 0.5)

image Laura_handjob_under:
    "images/Laura_handjob/Laura_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Laura_handjob_over:
    "images/Laura_handjob/Laura_handjob_hand_over.png"

    anchor (0.5, 0.5)

image Laura_titjob_hair_mid:
    "images/Laura_standing/Laura_standing_hair_mid.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_hair:
    if LauraX.wet:
        "images/Laura_standing/Laura_standing_hair_wet.png"
    else:
        "images/Laura_standing/Laura_standing_hair[LauraX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_body:
    always:
        "images/Laura_titjob/Laura_titjob_body.png"

    if LauraX.outfit["neck"]:
        "images/Laura_titjob/Laura_titjob_neck[LauraX.outfit[neck]].png"

    if LauraX.spunk["breasts"]:
        "images/Laura_titjob/Laura_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_left_arm:
    always:
        "images/Laura_titjob/Laura_titjob_left_hand.png"

    if LauraX.outfit["gloves"] == "gloves":
        "images/Laura_titjob/Laura_titjob_gloves[LauraX.outfit[gloves]]_left.png"

    if LauraX.outfit["piercings"]:
        "images/Laura_titjob/Laura_titjob_piercings[LauraX.outfit[piercings]]_left.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_right_arm:
    always:
        "images/Laura_titjob/Laura_titjob_right_hand.png"

    if LauraX.outfit["gloves"] == "gloves":
        "images/Laura_titjob/Laura_titjob_gloves[LauraX.outfit[gloves]]_right.png"

    if LauraX.outfit["piercings"]:
        "images/Laura_titjob/Laura_titjob_piercings[LauraX.outfit[piercings]]_right.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_right_arm_back:
    always:
        "images/Laura_titjob/Laura_titjob_right_hand_back.png"

    if LauraX.outfit["gloves"] == "gloves":
        "images/Laura_titjob/Laura_titjob_gloves[LauraX.outfit[gloves]]_right_back.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_left_breast:
    always:
        "images/Laura_titjob/Laura_titjob_left_breast.png"

    if LauraX.spunk["breasts"]:
        "images/Laura_titjob/Laura_titjob_spunk_left_breast.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_right_breast:
    always:
        "images/Laura_titjob/Laura_titjob_right_breast.png"

    if LauraX.spunk["breasts"]:
        "images/Laura_titjob/Laura_titjob_spunk_right_breast.png"

    anchor (0.5, 0.5)
