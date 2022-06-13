layeredimage Jean_sprite standing:
    # always:
    #     "images/Jean_standing/Jean_standing_head_reference.png"

    if JeanX.outfit["hair"] != "_pony" and not renpy.showing("Jean_sprite blowjob"):
        "Jean_back_hair" pos (0.16, 0.135) zoom 0.32

    always:
        "images/Jean_standing/Jean_standing_body.png"

    if JeanX.pubes:
        "images/Jean_standing/Jean_standing_pubes.png"

    always:
        "images/Jean_standing/Jean_standing_arm[JeanX.arm_pose]_right.png"

    always:
        "images/Jean_standing/Jean_standing_breasts.png"

    always:
        "images/Jean_standing/Jean_standing_arm[JeanX.arm_pose]_left.png"

    if JeanX.outfit["piercings"]:
        "images/Jean_standing/Jean_standing_piercings_breasts[JeanX.outfit[piercings]].png"

    if JeanX.outfit["piercings"]:
        "images/Jean_standing/Jean_standing_piercings_pussy[JeanX.outfit[piercings]].png"

    if JeanX.outfit["clamps"]:
        "images/Jean_standing/Jean_standing_clamps[JeanX.outfit[clamps]].png"

    if JeanX.outfit["rope"]:
        "images/Jean_standing/Jean_standing_rope[JeanX.outfit[rope]].png"

    if not JeanX.outfit["bra"]:
        Null()
    elif JeanX.bra_pulled_up:
        "images/Jean_standing/Jean_standing_bra[JeanX.outfit[bra]][JeanX.arm_pose]_up.png"
    else:
        "images/Jean_standing/Jean_standing_bra[JeanX.outfit[bra]][JeanX.arm_pose].png"

    if not JeanX.outfit["underwear"]:
        Null()
    elif JeanX.underwear_pulled_down:
        "images/Jean_standing/Jean_standing_underwear[JeanX.outfit[underwear]]_down.png"
    else:
        "images/Jean_standing/Jean_standing_underwear[JeanX.outfit[underwear]].png"

    if JeanX.outfit["hose"]:
        "images/Jean_standing/Jean_standing_hose[JeanX.outfit[hose]].png"

    if JeanX.outfit["bottom"] and JeanX.grool > 1:
        "images/Jean_standing/Jean_standing_grool.png"
    elif JeanX.grool:
        "images/Jean_standing/Jean_standing_grool.png"

    if JeanX.spunk["pussy"] or JeanX.spunk["anus"]:
        "images/Jean_standing/Jean_standing_spunk_pussy.png"

    if JeanX.outfit["dress"]:
        "images/Jean_standing/Jean_standing_dress[JeanX.outfit[dress]][JeanX.arm_pose].png"

    if not JeanX.outfit["bottom"]:
        Null()
    elif JeanX.bottom_pulled_down:
        "images/Jean_standing/Jean_standing_bottom[JeanX.outfit[bottom]]_down.png"
    else:
        "images/Jean_standing/Jean_standing_bottom[JeanX.outfit[bottom]].png"

    if not JeanX.outfit["top"]:
        Null()
    elif JeanX.top_pulled_up:
        "images/Jean_standing/Jean_standing_top[JeanX.outfit[top]][JeanX.arm_pose]_up.png"
    else:
        "images/Jean_standing/Jean_standing_top[JeanX.outfit[top]][JeanX.arm_pose].png"

    always:
        "Jean_head" pos (0.16, 0.135) zoom 0.32

    if JeanX.outfit["piercings"] and JeanX.pussy_covered:
        "images/Jean_standing/Jean_standing_piercings_pussy[JeanX.outfit[piercings]]_covered.png"

    if JeanX.outfit["piercings"] and JeanX.breasts_covered:
        "images/Jean_standing/Jean_standing_piercings_breasts[JeanX.outfit[piercings]]_covered.png"

    always:
        "images/Jean_standing/Jean_standing_hand[JeanX.arm_pose]_right.png"

    if not renpy.showing("Jean_sprite handjob") and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_hand[JeanX.arm_pose]_left.png"

    if JeanX.outfit["bra"] == "_sports_bra" and not renpy.showing("Jean_sprite handjob") and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_sleeves[JeanX.outfit[bra]][JeanX.arm_pose].png"

    if JeanX.outfit["top"] == "_pink_shirt" and not renpy.showing("Jean_sprite handjob") and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_sleeves[JeanX.outfit[top]][JeanX.arm_pose].png"

    if not JeanX.outfit["suspenders"]:
        Null()
    elif JeanX.suspenders_aside:
        "images/Jean_standing/Jean_standing_suspenders[JeanX.outfit[suspenders]]_aside.png"
    else:
        "images/Jean_standing/Jean_standing_suspenders[JeanX.outfit[suspenders]].png"

    if JeanX.spunk["breasts"]:
        "images/Jean_standing/Jean_standing_spunk_breasts.png"

    if JeanX.spunk["belly"]:
        "images/Jean_standing/Jean_standing_spunk_belly.png"

    if JeanX.wet:
        "images/Jean_standing/Jean_standing_water_body[JeanX.arm_pose].png"

    if JeanX.wet and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_water_arm[JeanX.arm_pose].png"

    if JeanX.outfit["held_item"] and JeanX.arm_pose == 2:
        "images/Jean_standing/Jean_standing_held[JeanX.outfit[held_item]].png"

    # always:
    #     "Jean_standing_fondling_animations"

    anchor (0.5, 0.0) offset (20, 180)

image Jean_back_hair:
    "images/Jean_standing/Jean_standing_back_hair[JeanX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Jean_head:
    always:
        "images/Jean_standing/Jean_standing_head[JeanX.blushing].png"

    always:
        "images/Jean_standing/Jean_standing_brows[JeanX.brows][JeanX.blushing].png"

    if JeanX.spunk["mouth"]:
        "images/Jean_standing/Jean_standing_spunk_mouth[JeanX.mouth].png"
    else:
        "images/Jean_standing/Jean_standing_mouth[JeanX.mouth].png"

    if JeanX.eyes == "_closed":
        "images/Jean_standing/Jean_standing_eyes_closed.png"
    else:
        "Jean_blinking"

    if JeanX.spunk["chin"]:
        "images/Jean_standing/Jean_standing_spunk_chin.png"

    if JeanX.spunk["face"]:
        "images/Jean_standing/Jean_standing_spunk_face.png"

    always:
        "images/Jean_standing/Jean_standing_hair[JeanX.outfit[hair]].png"

    if JeanX.spunk["hair"]:
        "images/Jean_standing/Jean_standing_spunk_hair.png"

    if JeanX.wet:
        "images/Jean_standing/Jean_standing_water_head.png"

    anchor (0.5, 0.5)

image Jean_handjob_under:
    "images/Jean_handjob/Jean_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Jean_handjob_over:
    "images/Jean_handjob/Jean_handjob_hand_over.png"

    anchor (0.5, 0.5)












# layeredimage Jean_kneeling:
#     # always:
#     #     "images/Jean_kneeling/Jean_kneeling_head_reference.png"
#
#     always:
#         "images/Jean_kneeling/Jean_kneeling_back_hair[JeanX.outfit[hair]].png"
#
#     if JeanX.outfit["rope"]:
#         "images/Jean_kneeling/Jean_kneeling_right_arm_bound.png"
#     else:
#         "images/Jean_kneeling/Jean_kneeling_right_arm.png"
#
#     if JeanX.whipped:
#         "images/Jean_kneeling/Jean_kneeling_body_whipped.png"
#     else:
#         "images/Jean_kneeling/Jean_kneeling_body.png"
#
#     if JeanX.whipped:
#         "images/Jean_kneeling/Jean_kneeling_legs_whipped.png"
#     else:
#         "images/Jean_kneeling/Jean_kneeling_legs.png"
#
#     if JeanX.outfit["rope"]:
#         "images/Jean_kneeling/Jean_kneeling_left_arm_bound.png"
#     else:
#         "images/Jean_kneeling/Jean_kneeling_left_arm.png"
#
#     always:
#         "Jean_head" pos (0.31, 0.4) rotate -18.0 zoom 0.6304
#
#     if JeanX.outfit["makeup"]:
#         "images/Jean_kneeling/Jean_kneeling_makeup[JeanX.outfit[makeup]].png"
#
#     if JeanX.outfit["gag"]:
#         "images/Jean_kneeling/Jean_kneeling_gag[JeanX.outfit[gag]].png"
#
#     if JeanX.outfit["clamps"]:
#         "images/Jean_kneeling/Jean_kneeling_clamps[JeanX.outfit[clamps]].png"
#
#     if JeanX.outfit["rope"]:
#         "images/Jean_kneeling/Jean_kneeling_rope[JeanX.outfit[rope]].png"
#
#     if JeanX.outfit["held_item"]:
#         "images/Jean_kneeling/Jean_kneeling_held_item[JeanX.outfit[held_item]].png"
#
#     anchor (0.5, 0.0) offset (0, 320) zoom 0.45
