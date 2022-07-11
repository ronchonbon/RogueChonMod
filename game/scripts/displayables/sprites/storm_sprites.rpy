layeredimage Storm_sprite standing:
    # always:
    #     "images/Storm_standing/Storm_standing_head_reference.png"

    if StormX.Clothes["jacket"].string:
        "images/Storm_standing/Storm_standing_jacket_[StormX.Clothes[jacket].string]_back.png"

    if StormX.Clothes["bra"].string in ["black_bra", "black_sports_bra"] and StormX.Clothes["bra"].state:
        "images/Storm_standing/Storm_standing_bra_[StormX.Clothes[bra].string]_back.png"

    if StormX.Clothes["skirt"].string:
        "images/Storm_standing/Storm_standing_skirt_[StormX.Clothes[skirt].string]_back.png"

    if StormX.Clothes["pants"].state:
        "images/Storm_standing/Storm_standing_pants_[StormX.Clothes[pants].string]_back.png"

    if StormX.Clothes["underwear"].state:
        "images/Storm_standing/Storm_standing_underwear_[StormX.Clothes[underwear].string]_back.png"

    always:
        "Storm_hair_back" pos (0.28, 0.318) zoom 0.47

    always:
        "images/Storm_standing/Storm_standing_body[StormX.arm_pose].png"

    if StormX.pubes:
        "images/Storm_standing/Storm_standing_pubes.png"

    if StormX.Clothes["sleeves"].string:
        "images/Storm_standing/Storm_standing_sleeves[StormX.arm_pose]_[StormX.Clothes[sleeves].string].png"

    if StormX.Clothes["body_piercings"].string:
        "images/Storm_standing/Storm_standing_body_piercings_pussy_[StormX.Clothes[body_piercings].string].png"

    if not StormX.Clothes["underwear"].string:
        Null()
    elif StormX.Clothes["underwear"].string == "black_bikini_bottoms" and (StormX.Clothes["bra"].string != "black_bikini_top" or StormX.Clothes["bra"].state):
        "images/Storm_standing/Storm_standing_underwear_[StormX.Clothes[underwear].string]_2.png"
    elif StormX.grool > 1 and StormX.Clothes["underwear"].string != "Elena_panties":
        "images/Storm_standing/Storm_standing_underwear_[StormX.Clothes[underwear].string]_grool_[StormX.Clothes[underwear].state].png"
    else:
        "images/Storm_standing/Storm_standing_underwear_[StormX.Clothes[underwear].string]_[StormX.Clothes[underwear].state].png"

    if StormX.Clothes["hose"].string:
        "images/Storm_standing/Storm_standing_hose_[StormX.Clothes[hose].string].png"

    if StormX.Clothes["boots"].string:
        "images/Storm_standing/Storm_standing_boots_[StormX.Clothes[boots].string].png"

    if StormX.grool and not StormX.Outfit.pussy_covered:
        "images/Storm_standing/Storm_standing_grool.png"

    always:
        "Storm_grool_animations"

    if StormX.spunk["pussy"] or StormX.spunk["anus"]:
        "images/Storm_standing/Storm_standing_spunk_pussy.png"

    always:
        "Storm_spunk_animations"

    if not StormX.Clothes["pants"].string:
        Null()
    elif StormX.grool > 1 and not StormX.Clothes["pants"].state:
        "images/Storm_standing/Storm_standing_pants_[StormX.Clothes[pants].string]_grool.png"
    else:
        "images/Storm_standing/Storm_standing_pants_[StormX.Clothes[pants].string]_[StormX.Clothes[pants].state].png"

    if StormX.Clothes["skirt"].string:
        "images/Storm_standing/Storm_standing_skirt_[StormX.Clothes[skirt].string]_[StormX.Clothes[skirt].state].png"

    if StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_hand[StormX.arm_pose]_right.png"

    if StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_hand[StormX.arm_pose]_left.png"

    if StormX.Outfit.breasts_supported:
        "images/Storm_standing/Storm_standing_breasts_up.png"
    else:
        "images/Storm_standing/Storm_standing_breasts_down.png"

    if StormX.Clothes["body_tattoos"].string:
        "images/Storm_standing/Storm_standing_body_tattoos_[StormX.Clothes[body_tattoos].string].png"

    if not StormX.Clothes["body_piercings"].string:
        Null()
    elif StormX.Outfit.breasts_supported:
        "images/Storm_standing/Storm_standing_body_piercings_breasts_[StormX.Clothes[body_piercings].string]_up.png"
    else:
        "images/Storm_standing/Storm_standing_body_piercings_breasts_[StormX.Clothes[body_piercings].string]_down.png"

    if StormX.Clothes["bra"].string:
        "images/Storm_standing/Storm_standing_bra_[StormX.Clothes[bra].string]_[StormX.Clothes[bra].state].png"

    if not StormX.Clothes["top"].string:
        Null()
    elif StormX.Outfit.breasts_supported or StormX.Clothes["top"].state:
        "images/Storm_standing/Storm_standing_top_[StormX.Clothes[top].string]_up_[StormX.Clothes[top].state].png"
    else:
        "images/Storm_standing/Storm_standing_top_[StormX.Clothes[top].string]_down.png"

    if StormX.Clothes["neck"].string:
        "images/Storm_standing/Storm_standing_neck_[StormX.Clothes[neck].string].png"

    if StormX.Clothes["jacket"].string:
        "images/Storm_standing/Storm_standing_jacket_[StormX.Clothes[jacket].string]_collar.png"

    if StormX.Clothes["body_piercings"].string and StormX.Outfit.pussy_covered:
        "images/Storm_standing/Storm_standing_body_piercings_pussy[StormX.Clothes[body_piercings].string]_covered.png"

    if not StormX.Clothes["body_piercings"].string or not StormX.Outfit.breasts_covered:
        Null()
    elif StormX.Outfit.breasts_supported:
        "images/Storm_standing/Storm_standing_body_piercings_breasts_[StormX.Clothes[body_piercings].string]_up_covered.png"
    else:
        "images/Storm_standing/Storm_standing_body_piercings_breasts_[StormX.Clothes[body_piercings].string]_down_covered.png"

    if not StormX.Clothes["jacket"].string:
        Null()
    elif StormX.Outfit.breasts_supported or StormX.Clothes["jacket"].state:
        "images/Storm_standing/Storm_standing_jacket[StormX.arm_pose]_[StormX.Clothes[jacket].string]_up_[StormX.Clothes[jacket].state].png"
    else:
        "images/Storm_standing/Storm_standing_jacket[StormX.arm_pose]_[StormX.Clothes[jacket].string]_down.png"

    if StormX.arm_pose == 1:
        "images/Storm_standing/Storm_standing_hands[StormX.arm_pose].png"
        
    always:
        "Storm_head" pos (0.28, 0.318) zoom 0.47

    if StormX.Clothes["jacket"].string != "black_jacket" or not StormX.arm_pose == 2:
        Null()
    elif renpy.showing("Storm_sprite handjob"):
        "images/Storm_handjob/Storm_handjob_jacket[StormX.arm_pose]_[StormX.Clothes[jacket].string].png"
    else:
        "images/Storm_standing/Storm_standing_jacket[StormX.arm_pose]_[StormX.Clothes[jacket].string].png"

    if StormX.Clothes["sleeves"].string and StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_sleeves[StormX.arm_pose]_[StormX.Clothes[sleeves].string]_top.png"

    if not StormX.spunk["breasts"]:
        Null()
    elif StormX.Outfit.breasts_supported:
        "images/Storm_standing/Storm_standing_spunk_breasts_up.png"
    else:
        "images/Storm_standing/Storm_standing_spunk_breasts_down.png"

    if StormX.spunk["belly"]:
        "images/Storm_standing/Storm_standing_spunk_belly.png"

    if not StormX.wet:
        Null()
    elif StormX.Outfit.breasts_supported:
        "images/Storm_standing/Storm_standing_water_body[StormX.arm_pose]_up.png"
    else:
        "images/Storm_standing/Storm_standing_water_body[StormX.arm_pose]_down.png"

    if StormX.wet and StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_water_arm[StormX.arm_pose].png"

    if StormX.Clothes["face_outer_accessory"].string:
        "images/Storm_standing/Storm_standing_face_outer_accessory_[StormX.Clothes[face_outer_accessory].string].png" anchor (0.5, 0.5) pos (0.28, 0.318) zoom 0.47

    if StormX.held_item and StormX.arm_pose == 2:
        "images/Storm_standing/Storm_standing_held_item_[StormX.Clothes[held_item].string].png"

    always:
        "Storm_standing_fondling_animations"

    anchor (0.5, 0.0) offset (60, 180) zoom 0.5

layeredimage Storm_hair_back:
    if StormX.Clothes["face_outer_accessory"].string == "head_towel":
        "images/Storm_standing/Storm_standing_face_outer_accessory_[StormX.Clothes[face_outer_accessory].string]_back.png"
    elif StormX.Clothes["hair"].string in ["wet_long_hair", "wet_short_hair", "wet_mohawk"]:
        "images/Storm_standing/Storm_standing_hair_[StormX.Clothes[hair].string]_back.png"
    elif StormX.wet:
        "images/Storm_standing/Storm_standing_hair_wet_[StormX.Clothes[hair].string]_back.png"
    elif StormX.Clothes["hair"].string != "short_hair":
        "images/Storm_standing/Storm_standing_hair_[StormX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Storm_head:
    if StormX.blushing:
        "images/Storm_standing/Storm_standing_head_blush.png"
    else:
        "images/Storm_standing/Storm_standing_head.png"

    always:
        "images/Storm_standing/Storm_standing_brows_[StormX.brows].png"

    always:
        "images/Storm_standing/Storm_standing_mouth_[StormX.mouth].png"

    if StormX.spunk["mouth"]:
        "images/Storm_standing/Storm_standing_spunk_mouth_[StormX.mouth].png"

    if StormX.eyes == "closed":
        "images/Storm_standing/Storm_standing_eyes_closed.png"
    else:
        "Storm_blinking"

    if StormX.Clothes["face_inner_accessory"].string:
        "images/Storm_standing/Storm_standing_face_inner_accessory_[StormX.Clothes[face_inner_accessory].string].png"

    if StormX.spunk["chin"]:
        "images/Storm_standing/Storm_standing_spunk_chin.png"

    if StormX.spunk["face"]:
        "images/Storm_standing/Storm_standing_spunk_face.png"

    if StormX.Clothes["face_outer_accessory"].string == "head_towel":
        Null()
    elif renpy.showing("Storm_sprite sex") and StormX.Clothes["hair"].string == "long_hair":
        "images/Storm_sex/Storm_sex_hair.png"
    elif StormX.Clothes["hair"].string in ["wet_long_hair", "wet_short_hair", "wet_mohawk"]:
        "images/Storm_standing/Storm_standing_hair_[StormX.Clothes[hair].string].png"
    elif StormX.wet:
        "images/Storm_standing/Storm_standing_hair_wet_[StormX.Clothes[hair].string].png"
    else:
        "images/Storm_standing/Storm_standing_hair_[StormX.Clothes[hair].string].png"

    if StormX.spunk["hair"]:
        "images/Storm_standing/Storm_standing_spunk_hair_[StormX.Clothes[hair].string].png"

    if StormX.wet:
        "images/Storm_standing/Storm_standing_water_head.png"

    anchor (0.5, 0.5)

image Storm_handjob_under:
    "images/Storm_handjob/Storm_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Storm_handjob_over:
    "images/Storm_handjob/Storm_handjob_hand_over.png"

    anchor (0.5, 0.5)

image Storm_titjob_bra_back:
    "images/Storm_titjob/Storm_titjob_bra_back.png"

    anchor (0.5, 0.5)

layeredimage Storm_titjob_body:
    always:
        "images/Storm_titjob/Storm_titjob_body.png"

    if StormX.spunk["breasts"]:
        "images/Storm_titjob/Storm_titjob_spunk_breasts_under.png"

    if StormX.wet:
        "images/Storm_titjob/Storm_titjob_water_body.png"

    if StormX.Clothes["hair"].string == "long_hair" and not StormX.wet:
        "images/Storm_titjob/Storm_titjob_hair_mid.png"

    anchor (0.5, 0.5)

image Storm_titjob_breasts_under:
    "images/Storm_titjob/Storm_titjob_breasts_under.png"

    anchor (0.5, 0.5)

image Storm_titjob_bra_stretch:
    "images/Storm_titjob/Storm_titjob_bra_[StormX.Clothes[bra].string]_stretch.png"

    anchor (0.5, 0.5)

layeredimage Storm_titjob_breasts:
    always:
        "images/Storm_titjob/Storm_titjob_breasts.png"

    if StormX.spunk["breasts"]:
        "images/Storm_titjob/Storm_titjob_spunk_breasts.png"

    if StormX.wet:
        "images/Storm_titjob/Storm_titjob_water_breasts.png"

    anchor (0.5, 0.5)

layeredimage Storm_titjob_hair:
    if StormX.Clothes["hair"].string in ["wet_long_hair", "wet_short_hair", "wet_mohawk"]:
        "images/Storm_blowjob/Storm_blowjob_hair_[StormX.Clothes[hair].string].png"
    elif StormX.wet:
        "images/Storm_blowjob/Storm_blowjob_hair_wet_[StormX.Clothes[hair].string].png"
    else:
        "images/Storm_blowjob/Storm_blowjob_hair_[StormX.Clothes[hair].string].png"

    if not StormX.spunk["hair"]:
        Null()
    elif StormX.Clothes["hair"].string in ["wet_long_hair", "wet_short_hair", "wet_mohawk"]:
        "images/Storm_blowjob/Storm_blowjob_spunk_hair_[StormX.Clothes[hair].string].png"
    elif StormX.wet:
        "images/Storm_blowjob/Storm_blowjob_spunk_hair_wet_[StormX.Clothes[hair].string].png"
    else:
        "images/Storm_blowjob/Storm_blowjob_spunk_hair_[StormX.Clothes[hair].string].png"

    anchor (0.5, 0.5)

layeredimage Storm_blowjob_hair_back:
    if StormX.wet or StormX.Clothes["hair"].string == "wet_long_hair":
        "images/Storm_blowjob/Storm_blowjob_hair_wet_back.png"
    elif StormX.Clothes["hair"].string == "long_hair":
        "images/Storm_blowjob/Storm_blowjob_hair_back.png"

    anchor (0.5, 0.5)

layeredimage Storm_blowjob_head:
    if StormX.blushing == "_blush2":
        "images/Storm_blowjob/Storm_blowjob_head_blush.png"
    else:
        "images/Storm_blowjob/Storm_blowjob_head.png"

    if renpy.showing("Storm_sprite titjob") and StormX.primary_Action.speed > 2:
        "images/Storm_blowjob/Storm_blowjob_mouth_tongue.png"
    elif renpy.showing("Storm_sprite blowjob") and StormX.primary_Action.speed == 1:
        "images/Storm_blowjob/Storm_blowjob_mouth_tongue.png"
    elif renpy.showing("Storm_sprite blowjob") and StormX.primary_Action.speed > 2:
        "images/Storm_blowjob/Storm_blowjob_mouth_sucking.png"
    else:
        "images/Storm_blowjob/Storm_blowjob_mouth_[StormX.mouth].png"

    if renpy.showing("Storm_sprite blowjob") and StormX.primary_Action.speed == 2:
        "Storm_blowjob_mouth_animations"

    if not StormX.spunk["mouth"]:
        Null()
    elif renpy.showing("Storm_sprite blowjob") and StormX.primary_Action.speed == 1:
        "images/Storm_blowjob/Storm_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Storm_sprite blowjob") and StormX.primary_Action.speed > 2:
        "images/Storm_blowjob/Storm_blowjob_spunk_mouth_sucking_under.png"
    elif StormX.mouth == "sucking":
        "images/Storm_blowjob/Storm_blowjob_spunk_mouth_[StormX.mouth]_under.png"
    else:
        "images/Storm_blowjob/Storm_blowjob_spunk_mouth_[StormX.mouth].png"

    if StormX.spunk["chin"]:
        "images/Storm_blowjob/Storm_blowjob_spunk_chin.png"

    always:
        "images/Storm_blowjob/Storm_blowjob_brows_[StormX.brows].png"

    if StormX.eyes == "closed":
        "images/Storm_blowjob/Storm_blowjob_eyes_closed.png"
    else:
        "Storm_blowjob_blinking"

    if StormX.wet:
        "images/Storm_blowjob/Storm_blowjob_water_head.png"

    if StormX.spunk["face"]:
        "images/Storm_blowjob/Storm_blowjob_spunk_face.png"

    if StormX.Clothes["hair"].string in ["wet_long_hair", "wet_short_hair", "wet_mohawk"]:
        "images/Storm_blowjob/Storm_blowjob_hair_[StormX.Clothes[hair].string].png"
    elif StormX.wet:
        "images/Storm_blowjob/Storm_blowjob_hair_wet_[StormX.Clothes[hair].string].png"
    else:
        "images/Storm_blowjob/Storm_blowjob_hair_[StormX.Clothes[hair].string].png"

    if not StormX.spunk["hair"]:
        Null()
    elif StormX.Clothes["hair"].string in ["wet_long_hair", "wet_short_hair", "wet_mohawk"]:
        "images/Storm_blowjob/Storm_blowjob_spunk_hair_[StormX.Clothes[hair].string].png"
    elif StormX.wet:
        "images/Storm_blowjob/Storm_blowjob_spunk_hair_wet_[StormX.Clothes[hair].string].png"
    else:
        "images/Storm_blowjob/Storm_blowjob_spunk_hair_[StormX.Clothes[hair].string].png"

    anchor (0.5, 0.5)
