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

    if KittyX.outfit["bra"] and KittyX.bra_pulled_up:
        "images/Kitty_standing/Kitty_standing_bra[KittyX.outfit[bra]][KittyX.arm_pose]_up.png"
    elif KittyX.outfit["bra"]:
        "images/Kitty_standing/Kitty_standing_bra[KittyX.outfit[bra]][KittyX.arm_pose].png"

    if KittyX.outfit["underwear"] and KittyX.underwear_pulled_down and (not KittyX.outfit["bottom"] or KittyX.wearing_skirt) and KittyX.grool > 1:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]]_down_grool.png"
    elif KittyX.outfit["underwear"] and KittyX.underwear_pulled_down and (not KittyX.outfit["bottom"] or KittyX.wearing_skirt):
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]]_down.png"
    elif KittyX.outfit["underwear"] and KittyX.grool > 1:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]]_grool.png"
    elif KittyX.outfit["underwear"]:
        "images/Kitty_standing/Kitty_standing_underwear[KittyX.outfit[underwear]].png"

    if KittyX.outfit["hose"]:
        "images/Kitty_standing/Kitty_standing_hose[KittyX.outfit[hose]].png"

    elif KittyX.grool > 1and KittyX.outfit["bottom"]:
        "images/Kitty_standing/Kitty_standing_grool1.png"
    elif KittyX.grool:
        "images/Kitty_standing/Kitty_standing_grool[KittyX.grool].png"

    always:
        "Kitty_grool_animations"

    always:
        "Kitty_spunk_animations"

    if KittyX.outfit["bottom"] and (KittyX.bottom_pulled_down or KittyX.upskirt):
        "images/Kitty_standing/Kitty_standing_bottom[KittyX.outfit[bottom]]_down.png"
    elif KittyX.outfit["bottom"]:
        "images/Kitty_standing/Kitty_standing_bottom[KittyX.outfit[bottom]].png"

    if KittyX.outfit["neck"]:
        "images/Kitty_standing/Kitty_standing_neck[KittyX.outfit[neck]].png"

    if KittyX.outfit["dress"] and KittyX.dress_top_pulled_down and KittyX.dress_upskirt:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_both.png"
    elif KittyX.outfit["dress"] and KittyX.dress_top_pulled_down:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_top.png"
    elif KittyX.outfit["dress"] and KittyX.dress_upskirt:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose]_bottom.png"
    elif KittyX.outfit["dress"]:
        "images/Kitty_standing/Kitty_standing_dress[KittyX.outfit[dress]][KittyX.arm_pose].png"

    if KittyX.outfit["top"] and KittyX.top_pulled_up:
        "images/Kitty_standing/Kitty_standing_top[KittyX.outfit[top]][KittyX.arm_pose]_up.png"
    elif KittyX.outfit["top"]:
        "images/Kitty_standing/Kitty_standing_top[KittyX.outfit[top]][KittyX.arm_pose].png"

    if KittyX.outfit["piercings"] and KittyX.breasts_covered:
        "images/Kitty_standing/Kitty_standing_piercings_breasts[KittyX.outfit[piercings]]_covered.png"

    if KittyX.outfit["jacket"]:
        "images/Kitty_standing/Kitty_standing_jacket[KittyX.outfit[jacket]].png"

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

    always:
        "Kitty_standing_fondling_animations"

    anchor (0.5, 0.0) offset (40, 170) zoom 0.95

layeredimage Kitty_back_hair:
    if KittyX.outfit["hair"] != "_evo":
        "images/Kitty_standing/Kitty_standing_back_hair[KittyX.outfit[hair]].png"

    anchor (0.5, 0.5)

layeredimage Kitty_head:
    always:
        "images/Kitty_standing/Kitty_standing_face[KittyX.outfit[hair]][KittyX.blushing].png"

    always:
        "images/Kitty_standing/Kitty_standing_brows[KittyX.brows].png"

    always:
        "images/Kitty_standing/Kitty_standing_mouth[KittyX.mouth].png"

    if KittyX.eyes == "_closed":
        "images/Kitty_standing/Kitty_standing_eyes_closed.png"
    elif KittyX.eyes == "_squint":
        "Kitty_squinting"
    else:
        "Kitty_blinking"

    if KittyX.spunk["mouth"]:
        "images/Kitty_standing/Kitty_spunk_standing[KittyX.mouth].png"

    if KittyX.spunk["face"]:
        "images/Kitty_standing/Kitty_standing_face_spunk.png"

    always:
        "images/Kitty_standing/Kitty_standing_hair[KittyX.outfit[hair]].png"

    if KittyX.spunk["hair"] and KittyX.outfit["hair"] != "_wet":
        "images/Kitty_standing/Kitty_standing_hair[KittyX.outfit[hair]]_spunk.png"

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

image Kitty_titjob_torso:
    "images/Kitty_titjob/Kitty_titjob_body.png"

    anchor (0.5, 0.5)

image Kitty_titjob_arms:
    "images/Kitty_titjob/Kitty_titjob_arms.png"

    anchor (0.5, 0.5)

image Kitty_titjob_mask:
    "images/Kitty_titjob/Kitty_titjob_mask.png"

    anchor (0.5, 0.5)

layeredimage Kitty_titjob_breasts:
    if Player.sprite and action_speed:
        "images/Kitty_titjob/Kitty_titjob_breasts_smooshed.png"
    else:
        "images/Kitty_titjob/Kitty_titjob_breasts.png"

    anchor (0.5, 0.5)

layeredimage Kitty_blowjob_head:
    if KittyX.wet or KittyX.outfit["hair"] == "_wet":
        "images/Kitty_blowjob/Kitty_blowjob_back_hair_wet.png"

    if action_speed in [0, 1, 2, 5] or not renpy.showing("Kitty_sprite blowjob") and KittyX.wet and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet_blush.png"
    elif action_speed in [0, 1, 2, 5] or not renpy.showing("Kitty_sprite blowjob") and KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet.png"
    elif action_speed in [0, 1, 2, 5] or not renpy.showing("Kitty_sprite blowjob") and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_blush.png"
    elif action_speed in [0, 1, 2, 5] or not renpy.showing("Kitty_sprite blowjob"):
        "images/Kitty_blowjob/Kitty_blowjob_face_closed.png"
    elif KittyX.wet and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet_blush.png"
    elif KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet.png"
    elif KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_blush.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_face_open.png"

    if action_speed == 1 and renpy.showing("Kitty_sprite blowjob"):
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif action_speed not in [2, 5] and renpy.showing("Kitty_sprite blowjob"):
        "images/Kitty_blowjob/Kitty_blowjob_mouth_sucking.png"
    elif action_speed == 3 and renpy.showing("Kitty_sprite titjob"):
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif action_speed in [5, 6] and renpy.showing("Kitty_sprite titjob"):
        "images/Kitty_blowjob/Kitty_blowjob_mouth_kiss.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_mouth[KittyX.mouth].png"

    if renpy.showing("Kitty_sprite blowjob") and action_speed in [2, 5]:
        "Kitty_blowjob_mouth_animations"

    if KittyX.spunk["mouth"] and action_speed == 1 and renpy.showing("Kitty_sprite blowjob"):
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_tongue.png"
    elif KittyX.spunk["mouth"] and action_speed not in [2, 5] and renpy.showing("Kitty_sprite blowjob"):
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"
    elif KittyX.spunk["mouth"] and action_speed in [5, 6] and renpy.showing("Kitty_sprite titjob"):
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_kiss.png"
    elif KittyX.spunk["mouth"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth[KittyX.mouth].png"

    always:
        "images/Kitty_blowjob/Kitty_blowjob_brows[KittyX.brows].png"

    if KittyX.eyes == "_closed":
        "images/Kitty_blowjob/Kitty_blowjob_eyes_closed.png"
    elif KittyX.eyes == "_squint":
        "Kitty_blowjob_squinting"
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

    if KittyX.wet and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_head_open_wet.png"
    elif KittyX.wet:
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
