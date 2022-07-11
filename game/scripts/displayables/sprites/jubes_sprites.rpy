layeredimage Jubes_sprite standing:
    # always:
    #     "images/Jubes_standing/Jubes_standing_head_reference.png"

    if JubesX.Clothes["jacket"].string:
        "images/Jubes_standing/Jubes_standing_jacket_[JubesX.Clothes[jacket].string]_collar.png"

    if JubesX.Clothes["pants"].state:
        "images/Jubes_standing/Jubes_standing_pants_[JubesX.Clothes[pants].string]_back.png"

    if JubesX.Clothes["underwear"].state:
        "images/Jubes_standing/Jubes_standing_underwear_[JubesX.Clothes[underwear].string]_back.png"

    always:
        "Jubes_hair_back" pos (0.324, 0.406) zoom 0.37

    always:
        "images/Jubes_standing/Jubes_standing_body[JubesX.arm_pose].png"

    if JubesX.pubes:
        "images/Jubes_standing/Jubes_standing_pubes.png"

    if JubesX.Clothes["body_piercings"].string:
        "images/Jubes_standing/Jubes_standing_body_piercings_breasts_[JubesX.Clothes[body_piercings].string].png"

    if JubesX.Clothes["body_piercings"].string:
        "images/Jubes_standing/Jubes_standing_body_piercings_pussy_[JubesX.Clothes[body_piercings].string].png"

    if JubesX.Clothes["jacket"].state:
        "images/Jubes_standing/Jubes_standing_jacket[JubesX.arm_pose]_[JubesX.Clothes[jacket].string]_back.png"

    if JubesX.Clothes["bra"].string:
        "images/Jubes_standing/Jubes_standing_bra_[JubesX.Clothes[bra].string]_[JubesX.Clothes[bra].state].png"

    if not JubesX.Clothes["underwear"].string:
        Null()
    elif JubesX.grool > 1:
        "images/Jubes_standing/Jubes_standing_underwear_[JubesX.Clothes[underwear].string]_grool_[JubesX.Clothes[underwear].state].png"
    else:
        "images/Jubes_standing/Jubes_standing_underwear_[JubesX.Clothes[underwear].string]_[JubesX.Clothes[underwear].state].png"

    if JubesX.Clothes["hose"].string:
        "images/Jubes_standing/Jubes_standing_hose_[JubesX.Clothes[hose].string].png"

    always:
        "Jubes_grool_animations"

    # if JubesX.spunk["pussy"] or JubesX.spunk["anus"]:
    #     "images/Jubes_standing/Jubes_standing_spunk_pussy.png"

    always:
        "Jubes_spunk_animations"

    if JubesX.Clothes["pants"].string:
        "images/Jubes_standing/Jubes_standing_pants_[JubesX.Clothes[pants].string]_[JubesX.Clothes[pants].state].png"

    if JubesX.Clothes["skirt"].string:
        "images/Jubes_standing/Jubes_standing_skirt_[JubesX.Clothes[skirt].string]_[JubesX.Clothes[skirt].state].png"

    if JubesX.grool and not JubesX.Outfit.pussy_covered:
        "images/Jubes_standing/Jubes_standing_grool.png"

    if JubesX.Clothes["top"].string:
        "images/Jubes_standing/Jubes_standing_top[JubesX.arm_pose]_[JubesX.Clothes[top].string]_[JubesX.Clothes[top].state].png"

    if JubesX.Clothes["neck"].string:
        "images/Jubes_standing/Jubes_standing_neck[JubesX.Clothes[neck].string].png"

    always:
        "Jubes_head" pos (0.324, 0.406) zoom 0.37

    if JubesX.Clothes["body_piercings"].string and JubesX.Outfit.pussy_covered:
        "images/Jubes_standing/Jubes_standing_body_piercings_pussy[JubesX.Clothes[body_piercings].string]_covered.png"

    if JubesX.Clothes["body_piercings"].string and JubesX.Outfit.breasts_covered:
        "images/Jubes_standing/Jubes_standing_body_piercings_breasts_[JubesX.Clothes[body_piercings].string]_covered.png"

    if JubesX.Clothes["jacket"].state == -1 and JubesX.arm_pose == 2:
        "images/Jubes_standing/Jubes_standing_jacket[JubesX.arm_pose]_[JubesX.Clothes[jacket].string]_sleeves.png"

    if JubesX.Clothes["suspenders"].string:
        "images/Jubes_standing/Jubes_standing_suspenders_[JubesX.Clothes[suspenders].string]_[JubesX.Clothes[suspenders].state].png"

    if JubesX.Clothes["jacket"].string:
        "images/Jubes_standing/Jubes_standing_jacket[JubesX.arm_pose]_[JubesX.Clothes[jacket].string]_[JubesX.Clothes[jacket].state].png"

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

    if JubesX.held_item and JubesX.arm_pose == 1:
        "images/Jubes_standing/Jubes_standing_held_item_[JubesX.Clothes[held_item].string].png"

    always:
        "Jubes_standing_fondling_animations" zoom 0.91

    anchor (0.5, 0.0) offset (15, 150) zoom 0.54

layeredimage Jubes_hair_back:
    if JubesX.wet:
        "images/Jubes_standing/Jubes_standing_hair_wet_hair_back.png"
    else:
        "images/Jubes_standing/Jubes_standing_hair_[JubesX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Jubes_head:
    always:
        "images/Jubes_standing/Jubes_standing_head[JubesX.blushing].png"

    always:
        "images/Jubes_standing/Jubes_standing_brows_[JubesX.brows].png"

    always:
        "images/Jubes_standing/Jubes_standing_mouth_[JubesX.mouth].png"

    if JubesX.spunk["mouth"]:
        "images/Jubes_standing/Jubes_standing_spunk_mouth_[JubesX.mouth].png"

    if JubesX.eyes == "closed":
        "images/Jubes_standing/Jubes_standing_eyes_closed.png"
    else:
        "Jubes_blinking"

    if JubesX.Clothes["face_inner_accessory"].string:
        "images/Jubes_standing/Jubes_standing_face_inner_accessory_[JubesX.Clothes[face_inner_accessory].string].png"

    if JubesX.spunk["chin"]:
        "images/Jubes_standing/Jubes_standing_spunk_chin.png"

    if JubesX.spunk["face"]:
        "images/Jubes_standing/Jubes_standing_spunk_face.png"

    if JubesX.wet:
        "images/Jubes_standing/Jubes_standing_hair_wet_hair.png"
    else:
        "images/Jubes_standing/Jubes_standing_hair_[JubesX.Clothes[hair].string].png"

    if JubesX.Clothes["face_outer_accessory"].string:
        "images/Jubes_standing/Jubes_standing_face_outer_accessory_[JubesX.Clothes[face_outer_accessory].string].png"

    if JubesX.spunk["hair"]:
        "images/Jubes_standing/Jubes_standing_spunk_hair_[JubesX.Clothes[hair].string].png"

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
    "images/Jubes_titjob/Jubes_titjob_jacket_[JubesX.Clothes[jacket].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Jubes_titjob_bra_back:
    if JubesX.Clothes["bra"].string not in ["blue_sports_bra", "pink_bikini_top"]:
        Null()
    elif JubesX.Clothes["bra"].state:
        "images/Jubes_titjob/Jubes_titjob_bra_[JubesX.Clothes[bra].string]_back_[JubesX.Clothes[bra].state].png"
    else:
        "images/Jubes_titjob/Jubes_titjob_bra_[JubesX.Clothes[bra].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Jubes_titjob_body:
    always:
        "images/Jubes_titjob/Jubes_titjob_body.png"

    if JubesX.spunk["breasts"]:
        "images/Jubes_titjob/Jubes_titjob_spunk_breasts_under.png"

    anchor (0.5, 0.5)

image Jubes_titjob_breasts_under:
    "images/Jubes_titjob/Jubes_titjob_breasts_under.png"

    anchor (0.5, 0.5)

layeredimage Jubes_titjob_breasts:
    always:
        "images/Jubes_titjob/Jubes_titjob_breasts.png"

    if JubesX.spunk["breasts"]:
        "images/Jubes_titjob/Jubes_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Jubes_blowjob_head:
    if JubesX.blushing == "_blush2":
        "images/Jubes_blowjob/Jubes_blowjob_head_blush.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_head.png"

    if renpy.showing("Jubes_sprite titjob") and JubesX.primary_Action.speed > 2:
        "images/Jubes_blowjob/Jubes_blowjob_mouth_tongue.png"
    elif renpy.showing("Jubes_sprite blowjob") and JubesX.primary_Action.speed == 1:
        "images/Jubes_blowjob/Jubes_blowjob_mouth_tongue.png"
    elif renpy.showing("Jubes_sprite blowjob") and JubesX.primary_Action.speed > 2:
        "images/Jubes_blowjob/Jubes_blowjob_mouth_sucking.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_mouth_[JubesX.mouth].png"

    if renpy.showing("Jubes_sprite blowjob") and JubesX.primary_Action.speed == 2:
        "Jubes_blowjob_mouth_animations"

    if not JubesX.spunk["mouth"]:
        Null()
    elif renpy.showing("Jubes_sprite blowjob") and JubesX.primary_Action.speed == 1:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Jubes_sprite blowjob") and JubesX.primary_Action.speed > 2:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth_sucking_under.png"
    elif JubesX.mouth == "sucking":
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth_[JubesX.mouth]_under.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_mouth_[JubesX.mouth].png"

    always:
        "images/Jubes_blowjob/Jubes_blowjob_brows_[JubesX.brows].png"

    if JubesX.eyes == "closed":
        "images/Jubes_blowjob/Jubes_blowjob_eyes_closed.png"
    else:
        "Jubes_blowjob_blinking"

    if JubesX.spunk["face"]:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_face.png"

    if JubesX.wet:
        "images/Jubes_blowjob/Jubes_blowjob_water_head.png"

    if JubesX.wet:
        "images/Jubes_blowjob/Jubes_blowjob_hair_wet_hair.png"
    else:
        "images/Jubes_blowjob/Jubes_blowjob_hair_[JubesX.Clothes[hair].string].png"

    if JubesX.spunk["hair"]:
        "images/Jubes_blowjob/Jubes_blowjob_spunk_hair.png"

    anchor (0.5, 0.5)
