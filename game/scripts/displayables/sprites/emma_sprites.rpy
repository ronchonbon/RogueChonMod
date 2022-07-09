layeredimage Emma_sprite standing normal:
    # always:
    #     "images/Emma_standing/Emma_standing_head_reference.png"

    if EmmaX.Clothes["cloak"].string:
        "images/Emma_standing/Emma_standing_cloak_[EmmaX.Clothes[cloak].string]_back.png"

    if EmmaX.Clothes["jacket"].string:
        "images/Emma_standing/Emma_standing_jacket_[EmmaX.Clothes[jacket].string]_back.png"

    if EmmaX.Clothes["skirt"].string == "Dimitrescu_skirt":
        "images/Emma_standing/Emma_standing_skirt_[EmmaX.Clothes[skirt].string]_back.png"

    if EmmaX.Clothes["bra"].string in ["white_corset", "black_corset"] and not EmmaX.Clothes["bra"].state and not (EmmaX.Clothes["jacket"].string or EmmaX.Clothes["top"].string):
        "images/Emma_standing/Emma_standing_bra[EmmaX.arm_pose]_[EmmaX.Clothes[bra].string]_back.png"

    if EmmaX.Clothes["underwear"].state:
        "images/Emma_standing/Emma_standing_underwear_[EmmaX.Clothes[underwear].string]_back.png"

    always:
        "Emma_hair_back" pos (0.201, 0.31) zoom 0.5

    always:
        "images/Emma_standing/Emma_standing_legs[EmmaX.arm_pose].png"

    if EmmaX.Clothes["body_piercings"].string:
        "images/Emma_standing/Emma_standing_body_piercings_pussy_[EmmaX.Clothes[body_piercings].string].png"

    if EmmaX.pubes:
        "images/Emma_standing/Emma_standing_pubes.png"

    if EmmaX.Clothes["bra"].string and EmmaX.Clothes["bra"].string != "white_lace_bra":
        "images/Emma_standing/Emma_standing_bra_[EmmaX.Clothes[bra].string]_under.png"

    if not EmmaX.Clothes["underwear"].string:
        Null()
    elif EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_underwear_[EmmaX.Clothes[underwear].string]_grool_[EmmaX.Clothes[underwear].state].png"
    else:
        "images/Emma_standing/Emma_standing_underwear_[EmmaX.Clothes[underwear].string]_[EmmaX.Clothes[underwear].state].png"

    if EmmaX.Clothes["hose"].string:
        "images/Emma_standing/Emma_standing_hose_[EmmaX.Clothes[hose].string].png"

    if EmmaX.grool and not EmmaX.Outfit.pussy_covered:
        "images/Emma_standing/Emma_standing_grool.png"

    always:
        "Emma_grool_animations"

    if EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]:
        "images/Emma_standing/Emma_standing_spunk_pussy.png"

    always:
        "Emma_spunk_animations"

    if not EmmaX.Clothes["pants"].string:
        Null()
    elif EmmaX.grool > 1 and EmmaX.Clothes["pants"].string not in ["white_pants", "leather_pants"] and not EmmaX.Clothes["pants"].state:
        "images/Emma_standing/Emma_standing_pants_[EmmaX.Clothes[pants].string]_grool_[EmmaX.Clothes[pants].state].png"
    else:
        "images/Emma_standing/Emma_standing_pants_[EmmaX.Clothes[pants].string]_[EmmaX.Clothes[pants].state].png"

    if EmmaX.Clothes["skirt"].string:
        "images/Emma_standing/Emma_standing_skirt_[EmmaX.Clothes[skirt].string]_[EmmaX.Clothes[skirt].state].png"

    if EmmaX.Clothes["top"].string in ["white_nighty", "white_towel"]:
        "images/Emma_standing/Emma_standing_top_[EmmaX.Clothes[top].string]_waist.png"

    always:
        "images/Emma_standing/Emma_standing_arms[EmmaX.arm_pose].png"

    if EmmaX.Clothes["gloves"].string:
        "images/Emma_standing/Emma_standing_gloves[EmmaX.arm_pose]_[EmmaX.Clothes[gloves].string].png"

    if EmmaX.Clothes["boots"].string:
        "images/Emma_standing/Emma_standing_boots_[EmmaX.Clothes[boots].string].png"

    if EmmaX.Clothes["skirt"].string == "Dimitrescu_skirt" and not EmmaX.Clothes["skirt"].state:
        "images/Emma_standing/Emma_standing_skirt_[EmmaX.Clothes[skirt].string]_front.png"

    if EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_breasts_down.png"

    if not EmmaX.Clothes["body_piercings"].string:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_up.png"
    else:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_down.png"

    if EmmaX.Clothes["jacket"].state:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.arm_pose]_[EmmaX.Clothes[jacket].string]_sleeves.png"

    if EmmaX.Clothes["bra"].string:
        "images/Emma_standing/Emma_standing_bra_[EmmaX.Clothes[bra].string]_[EmmaX.Clothes[bra].state].png"

    if not EmmaX.Clothes["top"].string:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_top[EmmaX.arm_pose]_[EmmaX.Clothes[top].string]_up_[EmmaX.Clothes[top].state].png"
    else:
        "images/Emma_standing/Emma_standing_top[EmmaX.arm_pose]_[EmmaX.Clothes[top].string]_down_[EmmaX.Clothes[top].state].png"

    if EmmaX.Clothes["body_piercings"].string and EmmaX.Outfit.pussy_covered:
        "images/Emma_standing/Emma_standing_body_piercings_pussy_[EmmaX.Clothes[body_piercings].string]_covered.png"

    if not EmmaX.Clothes["body_piercings"].string or not EmmaX.Outfit.breasts_covered:
        Null()
    elif EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_up_covered.png"
    else:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_down_covered.png"

    if EmmaX.Clothes["neck"].string:
        "images/Emma_standing/Emma_standing_neck_[EmmaX.Clothes[neck].string].png"

    if EmmaX.Clothes["top"].string == "Dimitrescu_top":
        "images/Emma_standing/Emma_standing_top[EmmaX.arm_pose]_[EmmaX.Clothes[top].string]_shawl.png"

    if not EmmaX.Clothes["jacket"].string:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.arm_pose]_[EmmaX.Clothes[jacket].string]_up_[EmmaX.Clothes[jacket].state].png"
    else:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.arm_pose]_[EmmaX.Clothes[jacket].string]_down_[EmmaX.Clothes[jacket].state].png"

    if not EmmaX.Clothes["cloak"].string:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_cloak[EmmaX.arm_pose]_[EmmaX.Clothes[cloak].string]_up.png"
    else:
        "images/Emma_standing/Emma_standing_cloak[EmmaX.arm_pose]_[EmmaX.Clothes[cloak].string]_down.png"

    always:
        "Emma_head" pos (0.201, 0.31) zoom 0.5

    if not EmmaX.spunk["breasts"]:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
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
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_water_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_water_breasts_down.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_arms[EmmaX.arm_pose].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_legs.png"

    if EmmaX.Clothes["face_outer_accessory"].string:
        "images/Emma_standing/Emma_standing_face_outer_accessory_[EmmaX.Clothes[face_outer_accessory].string].png" pos (0.0, -0.09) zoom 0.5

    if EmmaX.held_item and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_held_item_[EmmaX.held_item].png"

    always:
        "Emma_standing_fondling_animations"

    anchor (0.5, 0.0) offset (20, 140) zoom 0.5

layeredimage Emma_hair_back:
    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet_back.png"
    else:
        "images/Emma_standing/Emma_standing_hair_[EmmaX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Emma_head:
    if EmmaX.wet or EmmaX.Clothes["hair"].string == "bangs":
        "images/Emma_standing/Emma_standing_head_[EmmaX.brows]_wet[EmmaX.blushing].png"
    else:
        "images/Emma_standing/Emma_standing_head_[EmmaX.brows]_[EmmaX.Clothes[hair].string][EmmaX.blushing].png"

    always:
        "images/Emma_standing/Emma_standing_brows_[EmmaX.brows].png"

    always:
        "images/Emma_standing/Emma_standing_mouth_[EmmaX.mouth].png"

    if EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_mouth_[EmmaX.mouth].png"

    if EmmaX.eyes == "closed":
        "images/Emma_standing/Emma_standing_eyes_closed.png"
    else:
        "Emma_blinking"

    if EmmaX.spunk["face"]:
        "images/Emma_standing/Emma_standing_spunk_face.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet.png"
    else:
        "images/Emma_standing/Emma_standing_hair_[EmmaX.Clothes[hair].string].png"

    if EmmaX.spunk["hair"]:
        "images/Emma_standing/Emma_standing_spunk_hair_[EmmaX.Clothes[hair].string].png"

    if EmmaX.Clothes["face_outer_accessory"].string != "Dimitrescu_hat":
        Null()
    elif EmmaX.wet or EmmaX.Clothes["hair"].string == "bangs":
        "images/Emma_standing/Emma_standing_shadow_head_wet.png"
    else:
        "images/Emma_standing/Emma_standing_shadow_head_[EmmaX.Clothes[hair].string].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_head.png"

    anchor (0.5, 0.5)

layeredimage Emma_sprite standing diamond:
    # always:
    #     "images/Emma_standing/Emma_standing_head_reference.png"

    if EmmaX.Clothes["jacket"].string:
        "images/Emma_standing/Emma_standing_jacket_[EmmaX.Clothes[jacket].string]_back.png"

    if EmmaX.Clothes["skirt"].string == "Dimitrescu_skirt":
        "images/Emma_standing/Emma_standing_skirt_[EmmaX.Clothes[skirt].string]_back.png"

    if EmmaX.Clothes["bra"].string in ["white_corset", "black_corset"] and not EmmaX.Clothes["bra"].state and not (EmmaX.Clothes["jacket"].string or EmmaX.Clothes["top"].string):
        "images/Emma_standing/Emma_standing_bra[EmmaX.arm_pose]_[EmmaX.Clothes[bra].string]_back.png"

    if EmmaX.Clothes["underwear"].state:
        "images/Emma_standing/Emma_standing_underwear_[EmmaX.Clothes[underwear].string]_back.png"

    always:
        "Emma_hair_back_diamond" pos (0.201, 0.31) zoom 0.5

    always:
        "images/Emma_standing/Emma_standing_legs[EmmaX.arm_pose]_diamond.png"

    if EmmaX.pubes:
        "images/Emma_standing/Emma_standing_pubes_diamond.png"

    if EmmaX.Clothes["bra"].string != "white_lace_bra":
        "images/Emma_standing/Emma_standing_bra_[EmmaX.Clothes[bra].string]_under.png"

    if not EmmaX.Clothes["underwear"].string:
        Null()
    elif EmmaX.grool > 1:
        "images/Emma_standing/Emma_standing_underwear_[EmmaX.Clothes[underwear].string]_grool_[EmmaX.Clothes[underwear].state].png"
    else:
        "images/Emma_standing/Emma_standing_underwear_[EmmaX.Clothes[underwear].string]_[EmmaX.Clothes[underwear].state].png"

    if EmmaX.Clothes["hose"].string:
        "images/Emma_standing/Emma_standing_hose_[EmmaX.Clothes[hose].string].png"

    if EmmaX.grool and not EmmaX.Outfit.pussy_covered:
        "images/Emma_standing/Emma_standing_grool.png"

    always:
        "Emma_grool_animations"

    if EmmaX.spunk["pussy"] or EmmaX.spunk["anus"]:
        "images/Emma_standing/Emma_standing_spunk_pussy.png"

    always:
        "Emma_spunk_animations"

    if not EmmaX.Clothes["pants"].string:
        Null()
    elif EmmaX.grool > 1 and EmmaX.Clothes["pants"].string and EmmaX.grool > 1 and EmmaX.Clothes["pants"].string not in ["white_pants", "leather_pants"]:
        "images/Emma_standing/Emma_standing_pants_[EmmaX.Clothes[pants].string]_grool.png"
    else:
        "images/Emma_standing/Emma_standing_pants_[EmmaX.Clothes[pants].string]_[EmmaX.Clothes[pants].state].png"

    if EmmaX.Clothes["skirt"].string:
        "images/Emma_standing/Emma_standing_pants_[EmmaX.Clothes[skirt].string]_[EmmaX.Clothes[skirt].state].png"

    if EmmaX.Clothes["top"].string in ["white_nighty", "white_towel"]:
        "images/Emma_standing/Emma_standing_top_[EmmaX.Clothes[top].string]_waist.png"

    always:
        "images/Emma_standing/Emma_standing_arms[EmmaX.arm_pose]_diamond.png"

    if EmmaX.Clothes["gloves"].string:
        "images/Emma_standing/Emma_standing_gloves[EmmaX.arm_pose]_[EmmaX.Clothes[gloves].string].png"

    if EmmaX.Clothes["body_piercings"].string:
        "images/Emma_standing/Emma_standing_body_piercings_pussy_[EmmaX.Clothes[body_piercings].string].png"

    if EmmaX.Clothes["boots"].string:
        "images/Emma_standing/Emma_standing_boots_[EmmaX.Clothes[boots].string].png"

    if EmmaX.Clothes["skirt"].string == "Dimitrescu_skirt" and not EmmaX.Clothes["skirt"].state:
        "images/Emma_standing/Emma_standing_skirt_[EmmaX.Clothes[skirt].string]_front.png"

    if EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_breasts_up_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_breasts_down_diamond.png"

    if not EmmaX.Clothes["body_piercings"].string:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_up.png"
    else:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_down.png"

    if EmmaX.Clothes["jacket"].state:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.arm_pose]_[EmmaX.Clothes[jacket].string]_sleeves.png"

    if not EmmaX.Clothes["bra"].string:
        "images/Emma_standing/Emma_standing_bra_[EmmaX.Clothes[bra].string]_[EmmaX.Clothes[bra].state].png"

    if not EmmaX.Clothes["top"].string:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_top[EmmaX.arm_pose]_[EmmaX.Clothes[top].string]_up_[EmmaX.Clothes[top].state].png"
    else:
        "images/Emma_standing/Emma_standing_top[EmmaX.arm_pose]_[EmmaX.Clothes[top].string]_down_[EmmaX.Clothes[top].state].png"

    if EmmaX.Clothes["body_piercings"].string and EmmaX.Outfit.pussy_covered:
        "images/Emma_standing/Emma_standing_body_piercings_pussy_[EmmaX.Clothes[body_piercings].string]_covered.png"

    if not EmmaX.Clothes["body_piercings"].string or not EmmaX.Outfit.breasts_covered:
        Null()
    elif EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_up_covered.png"
    else:
        "images/Emma_standing/Emma_standing_body_piercings_breasts_[EmmaX.Clothes[body_piercings].string]_down_covered.png"

    if EmmaX.Clothes["neck"].string:
        "images/Emma_standing/Emma_standing_neck_[EmmaX.Clothes[neck].string].png"

    if EmmaX.Clothes["top"].string == "Dimitrescu_top":
        "images/Emma_standing/Emma_standing_top[EmmaX.arm_pose]_[EmmaX.Clothes[top].string]_shawl.png"

    if not EmmaX.Clothes["jacket"].string:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.arm_pose]_[EmmaX.Clothes[jacket].string]_up_[EmmaX.Clothes[jacket].state].png"
    else:
        "images/Emma_standing/Emma_standing_jacket[EmmaX.arm_pose]_[EmmaX.Clothes[jacket].string]_down_[EmmaX.Clothes[jacket].state].png"

    always:
        "Emma_head_diamond" pos (0.201, 0.31) zoom 0.5

    if not EmmaX.spunk["breasts"]:
        Null()
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
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
    elif EmmaX.arm_pose == 1 or EmmaX.Outfit.breasts_supported:
        "images/Emma_standing/Emma_standing_water_breasts_up.png"
    else:
        "images/Emma_standing/Emma_standing_water_breasts_down.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_arms[EmmaX.arm_pose].png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_water_legs.png"

    if EmmaX.Clothes["face_outer_accessory"].string:
        "images/Emma_standing/Emma_standing_face_outer_accessory_[EmmaX.Clothes[face_outer_accessory].string].png" pos (0.0, -0.09) zoom 0.5

    if EmmaX.held_item and EmmaX.arm_pose == 2:
        "images/Emma_standing/Emma_standing_held_item_[EmmaX.held_item].png"

    always:
        "Emma_standing_fondling_animations"

    anchor (0.5, 0.0) offset (20, 140) zoom 0.5

layeredimage Emma_hair_back_diamond:
    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet_back_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_hair_[EmmaX.Clothes[hair].string]_back_diamond.png"

    anchor (0.5, 0.5)

layeredimage Emma_head_diamond:
    if EmmaX.wet or EmmaX.Clothes["hair"].string == "bangs":
        "images/Emma_standing/Emma_standing_head_[EmmaX.brows]_wet[EmmaX.blushing]_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_head_[EmmaX.brows]_[EmmaX.Clothes[hair].string][EmmaX.blushing]_diamond.png"

    always:
        "images/Emma_standing/Emma_standing_brows_[EmmaX.brows]_diamond.png"

    always:
        "images/Emma_standing/Emma_standing_mouth_[EmmaX.mouth]_diamond.png"

    if EmmaX.spunk["mouth"]:
        "images/Emma_standing/Emma_standing_spunk_mouth_[EmmaX.mouth].png"

    if EmmaX.eyes == "closed":
        "images/Emma_standing/Emma_standing_eyes_closed_diamond.png"
    else:
        "Emma_blinking_diamond"

    if EmmaX.spunk["face"]:
        "images/Emma_standing/Emma_standing_spunk_face.png"

    if EmmaX.wet:
        "images/Emma_standing/Emma_standing_hair_wet_hair_diamond.png"
    else:
        "images/Emma_standing/Emma_standing_hair_[EmmaX.Clothes[hair].string]_diamond.png"

    if EmmaX.spunk["hair"]:
        "images/Emma_standing/Emma_standing_spunk_hair_[EmmaX.Clothes[hair].string].png"

    if EmmaX.Clothes["face_outer_accessory"].string != "Dimitrescu_hat":
        Null()
    elif EmmaX.wet or EmmaX.Clothes["hair"].string == "bangs":
        "images/Emma_standing/Emma_standing_shadow_head_wet.png"
    else:
        "images/Emma_standing/Emma_standing_shadow_head_[EmmaX.Clothes[hair].string].png"

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
    if EmmaX.Clothes["gloves"].string or EmmaX.Clothes["top"].string == "Dimitrescu_top" or EmmaX.Clothes["jacket"].string == "white_jacket":
        "images/Emma_titjob/Emma_titjob_forearms_covered.png"
    else:
        "images/Emma_titjob/Emma_titjob_forearms.png"

    if EmmaX.Clothes["gloves"].string:
        "images/Emma_titjob/Emma_titjob_breasts_gloved.png"
    else:
        "images/Emma_titjob/Emma_titjob_breasts.png"

    if EmmaX.spunk["breasts"]:
        "images/Emma_titjob/Emma_titjob_spunk_breasts_over.png"

    anchor (0.5, 0.5)

layeredimage Emma_blowjob_hair_back:
    if EmmaX.wet or EmmaX.Clothes["hair"].string != "wavy_hair":
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
        "images/Emma_blowjob/Emma_blowjob_hair_[EmmaX.Clothes[hair].string]_mid.png"

    always:
        "images/Emma_blowjob/Emma_blowjob_face.png"
    # if renpy.showing("Emma_sprite blowjob") and EmmaX.primary_Action.speed > 2 and EmmaX.blushing:
    #     "images/Emma_blowjob/Emma_blowjob_face_open_blush.png"
    # elif renpy.showing("Emma_sprite blowjob") and EmmaX.primary_Action.speed > 2:
    #     "images/Emma_blowjob/Emma_blowjob_face_open.png"
    # elif EmmaX.blushing:
    #     "images/Emma_blowjob/Emma_blowjob_face_closed_blush.png"
    # else:
    #     "images/Emma_blowjob/Emma_blowjob_face_closed.png"

    if renpy.showing("Emma_sprite titjob") and EmmaX.primary_Action.speed > 2:
        "images/Emma_blowjob/Emma_blowjob_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and EmmaX.primary_Action.speed == 1:
        "images/Emma_blowjob/Emma_blowjob_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and EmmaX.primary_Action.speed == 2:
        "Emma_blowjob_mouth_animations"
    elif renpy.showing("Emma_sprite blowjob") and EmmaX.primary_Action.speed > 2:
        "images/Emma_blowjob/Emma_blowjob_mouth_sucking.png"
    else:
        "images/Emma_blowjob/Emma_blowjob_mouth_[EmmaX.mouth].png"

    if not EmmaX.spunk["mouth"]:
        Null()
    elif renpy.showing("Emma_sprite titjob") and EmmaX.primary_Action.speed > 2:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and EmmaX.primary_Action.speed == 1:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Emma_sprite blowjob") and EmmaX.primary_Action.speed > 2:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_sucking_under.png"
    elif EmmaX.mouth == "sucking":
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_[EmmaX.mouth]_under.png"
    else:
        "images/Emma_blowjob/Emma_blowjob_spunk_mouth_[EmmaX.mouth].png"

    always:
        "images/Emma_blowjob/Emma_blowjob_brows_[EmmaX.brows].png"

    if EmmaX.eyes == "closed":
        "images/Emma_blowjob/Emma_blowjob_eyes_closed.png"
    else:
        "Emma_blowjob_blinking"

    if EmmaX.spunk["face"]:
        "images/Emma_blowjob/Emma_blowjob_spunk_face.png"

    if EmmaX.wet:
        "images/Emma_blowjob/Emma_blowjob_hair_wet.png"
    else:
        "images/Emma_blowjob/Emma_blowjob_hair_[EmmaX.Clothes[hair].string].png"

    # always:
    #     "images/Emma_blowjob/Emma_blowjob_hat_reference.png"

    # if EmmaX.Clothes["face_outer_accessory"].string:
    #     "images/Emma_standing/Emma_standing_face_outer_accessory_[EmmaX.Clothes[face_outer_accessory].string].png" pos (-0.044, -0.095) zoom 1.3

    anchor (0.5, 0.5)

layeredimage Emma_sex_body:
    if EmmaX.Clothes["gloves"].string:
        "images/Emma_sex/Emma_sex_body_[EmmaX.Clothes[gloves].string].png"
    else:
        "images/Emma_sex/Emma_sex_body.png"

    if renpy.showing("Emma_sprite titjob"):
        Null()
    elif EmmaX.Outfit.breasts_supported:
        "images/Emma_sex/Emma_sex_breasts_up.png"
    else:
        "images/Emma_sex/Emma_sex_breasts_down.png"

    if not EmmaX.spunk["breasts"]:
        Null()
    elif renpy.showing("Emma_sprite titjob"):
        "images/Emma_titjob/Emma_titjob_spunk_breasts_under.png"
    else:
        "images/Emma_sex/Emma_sex_spunk_breasts.png"

    anchor (0.5, 0.5)
