layeredimage Laura_sprite standing:
    # always:
    #     "images/Laura_standing/Laura_standing_head_reference.png"

    if LauraX.outfit["jacket"] and LauraX.jacket_opened:
        "images/Laura_standing/Laura_standing_back_outer_accessory[LauraX.outfit[jacket]]_up.png"
    elif LauraX.outfit["jacket"]:
        "images/Laura_standing/Laura_standing_back_outer_accessory[LauraX.outfit[jacket]].png"

    if LauraX.outfit["underwear"] and LauraX.underwear_pulled_down:
        "images/Laura_standing/Laura_standing_back_inner_accessory[LauraX.outfit[underwear]]_down.png"

    if not renpy.showing("Laura_sprite blowjob"):
        "Laura_back_hair" pos (0.102, 0.19) zoom 0.5

    always:
        "images/Laura_standing/Laura_standing_body.png"

    always:
        "images/Laura_standing/Laura_standing_arms[LauraX.arm_pose]_mid.png"

    if LauraX.pubes:
        "images/Laura_standing/Laura_standing_pubes.png"

    always:
        "images/Laura_standing/Laura_standing_arm[LauraX.arm_pose]_right.png"

    always:
        "images/Laura_standing/Laura_standing_breasts.png"

    if LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_arm[LauraX.arm_pose]_left.png"

    if LauraX.outfit["gloves"] == "_gloves":
        "images/Laura_standing/Laura_standing_gloves[LauraX.outfit[gloves]][LauraX.arm_pose]_right.png"
    elif LauraX.outfit["gloves"]:
        "images/Laura_standing/Laura_standing_gloves[LauraX.outfit[gloves]][LauraX.arm_pose].png"

    if LauraX.outfit["gloves"] == "_gloves" and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_gloves[LauraX.outfit[gloves]][LauraX.arm_pose]_left.png"

    if LauraX.outfit["piercings"]:
        "images/Laura_standing/Laura_standing_piercings_breasts[LauraX.outfit[piercings]].png"

    if LauraX.outfit["piercings"]:
        "images/Laura_standing/Laura_standing_piercings_pussy[LauraX.outfit[piercings]].png"

    if LauraX.outfit["bra"] and LauraX.bra_pulled_up:
        "images/Laura_standing/Laura_standing_bra[LauraX.outfit[bra]]_up.png"
    elif LauraX.outfit["bra"]:
        "images/Laura_standing/Laura_standing_bra[LauraX.outfit[bra]].png"

    if LauraX.outfit["underwear"] and LauraX.underwear_pulled_down and (not LauraX.outfit["bottom"] or LauraX.wearing_skirt) and LauraX.grool > 1:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]]_down_grool.png"
    elif LauraX.outfit["underwear"] and LauraX.underwear_pulled_down and (not LauraX.outfit["bottom"] or LauraX.wearing_skirt):
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]]_down.png"
    elif LauraX.outfit["underwear"] and LauraX.grool > 1:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]]_grool.png"
    elif LauraX.outfit["underwear"]:
        "images/Laura_standing/Laura_standing_underwear[LauraX.outfit[underwear]].png"

    if LauraX.outfit["hose"] == "_stockings_and_garterbelt":
        "images/Laura_standing/Laura_standing_hose_stockings.png"
    elif LauraX.outfit["hose"]:
        "images/Laura_standing/Laura_standing_hose[LauraX.outfit[hose]].png"

    if LauraX.outfit["hose"] == "_stockings_and_garterbelt":
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

    if LauraX.outfit["bottom"] and (LauraX.bottom_pulled_down or LauraX.upskirt):
        "images/Laura_standing/Laura_standing_bottom[LauraX.outfit[bottom]]_down.png"
    elif LauraX.outfit["bottom"]:
        "images/Laura_standing/Laura_standing_bottom[LauraX.outfit[bottom]].png"

    if LauraX.outfit["top"]:
        "images/Laura_standing/Laura_standing_top[LauraX.outfit[top]].png"

    if LauraX.outfit["neck"]:
        "images/Laura_standing/Laura_standing_neck[LauraX.outfit[neck]].png"

    if not renpy.showing("Laura_sprite blowjob"):
        "Laura_head" pos (0.102, 0.19) zoom 0.5

    if LauraX.outfit["piercings"] and LauraX.pussy_covered:
        "images/Laura_standing/Laura_standing_piercings_pussy[LauraX.outfit[piercings]]_covered.png"

    if LauraX.outfit["piercings"] and LauraX.breasts_covered:
        "images/Laura_standing/Laura_standing_piercings_breasts[LauraX.outfit[piercings]]_covered.png"

    if LauraX.outfit["jacket"] and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_sleeves[LauraX.outfit[jacket]][LauraX.arm_pose].png"

    if LauraX.outfit["suspenders"] and LauraX.suspenders_aside:
        "images/Laura_standing/Laura_standing_suspenders[LauraX.outfit[suspenders]]_aside.png"
    elif LauraX.outfit["suspenders"]:
        "images/Laura_standing/Laura_standing_suspenders[LauraX.outfit[suspenders]].png"

    if LauraX.outfit["jacket"] and LauraX.jacket_opened:
        "images/Laura_standing/Laura_standing_jacket[LauraX.outfit[jacket]][LauraX.arm_pose]_up.png"
    elif LauraX.outfit["jacket"]:
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

    if LauraX.outfit["held_item"] and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_held[LauraX.outfit[held_item]].png"

    # always:
    #     "Laura_standing_fondling_animations"

    anchor (0.5, 0.0) offset (40, 150)

image Laura_back_hair:
    "images/Laura_standing/Laura_standing_back_hair[LauraX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Laura_head:
    if renpy.showing("Laura_sprite sex"):
        "images/Laura_sex/Laura_sex_back_hair[LauraX.outfit[hair]].png"

    always:
        "images/Laura_standing/Laura_standing_head[LauraX.blushing].png"

    if LauraX.blushing == "_blush2":
        "images/Laura_standing/Laura_standing_brows[LauraX.brows]_blush.png"
    else:
        "images/Laura_standing/Laura_standing_brows[LauraX.brows].png"

    if LauraX.spunk["mouth"]:
        "images/Laura_standing/Laura_standing_spunk_mouth[LauraX.mouth].png"
    else:
        "images/Laura_standing/Laura_standing_mouth[LauraX.mouth].png"

    if LauraX.eyes == "_closed":
        "images/Laura_standing/Laura_standing_eyes_closed.png"
    else:
        "Laura_blinking"

    if LauraX.spunk["chin"]:
        "images/Laura_standing/Laura_standing_spunk_chin.png"

    if LauraX.spunk["face"]:
        "images/Laura_standing/Laura_standing_spunk_face.png"

    if not renpy.showing("Laura_sprite titjob") and not renpy.showing("Laura_sprite sex"):
        "images/Laura_standing/Laura_standing_mid_hair[LauraX.outfit[hair]].png"

    if renpy.showing("Laura_sprite sex"):
        "images/Laura_sex/Laura_sex_hair[LauraX.outfit[hair]].png"
    else:
        "images/Laura_standing/Laura_standing_hair[LauraX.outfit[hair]].png"

    if LauraX.spunk["hair"]:
        "images/Laura_standing/Laura_standing_spunk_hair.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_head.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_hair.png"

    anchor (0.5, 0.5)
