layeredimage Mystique_sprite standing normal:
    always:
        "Mystique_hair_back" pos (0.54, 0.32) zoom 0.43

    always:
        "images/Mystique_standing/Mystique_standing_body.png"

    always:
        "Mystique_grool_animations"

    always:
        "Mystique_spunk_animations"

    if MystiqueX.Clothes["underwear"].string:
        "images/Mystique_standing/Mystique_standing_underwear_[MystiqueX.Clothes[underwear].string]_[MystiqueX.Clothes[underwear].state].png"

    if MystiqueX.Clothes["skirt"].string:
        "images/Mystique_standing/Mystique_standing_skirt_[MystiqueX.Clothes[skirt].string].png"

    always:
        "images/Mystique_standing/Mystique_standing_arms[MystiqueX.arm_pose].png"

    always:
        "images/Mystique_standing/Mystique_standing_breasts.png"

    if MystiqueX.Clothes["bra"].string:
        "images/Mystique_standing/Mystique_standing_bra_[MystiqueX.Clothes[bra].string]_[MystiqueX.Clothes[bra].state].png"

    if MystiqueX.Clothes["boots"].string:
        "images/Mystique_standing/Mystique_standing_boots_[MystiqueX.Clothes[boots].string].png"

    if MystiqueX.Clothes["dress"].string:
        "images/Mystique_standing/Mystique_standing_dress_[MystiqueX.Clothes[dress].string].png"

    if MystiqueX.Clothes["belt"].string:
        "images/Mystique_standing/Mystique_standing_belt_[MystiqueX.Clothes[belt].string].png"

    if MystiqueX.Clothes["top"].string:
        "images/Mystique_standing/Mystique_standing_top_[MystiqueX.Clothes[top].string].png"

    if MystiqueX.Clothes["jacket"].string:
        "images/Mystique_standing/Mystique_standing_jacket_[MystiqueX.Clothes[jacket].string].png"

    if MystiqueX.Clothes["gloves"].string:
        "images/Mystique_standing/Mystique_standing_gloves[MystiqueX.Clothes[gloves].string].png"

    always:
        "Mystique_head" pos (0.54, 0.32) zoom 0.43

    always:
        "Mystique_standing_fondling_animations" zoom 0.91

    anchor (0.5, 0.0) offset (0, 180) zoom 0.55

image Mystique_hair_back:
    "images/Mystique_standing/Mystique_standing_hair_[MystiqueX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Mystique_head:
    always:
        "images/Mystique_standing/Mystique_standing_head.png"

    always:
        "images/Mystique_standing/Mystique_standing_brows_[MystiqueX.brows].png"

    always:
        "images/Mystique_standing/Mystique_standing_mouth_[MystiqueX.mouth].png"

    if MystiqueX.spunk["mouth"]:
        "images/Mystique_standing/Mystique_standing_spunk_mouth_[MystiqueX.mouth].png"

    if MystiqueX.eyes == "closed":
        "images/Mystique_standing/Mystique_standing_eyes_closed.png"
    else:
        "Mystique_blinking"

    always:
        "images/Mystique_standing/Mystique_standing_hair_long_hair.png"

    if MystiqueX.Clothes["face_outer_accessory"].string:
        "images/Mystique_standing/Mystique_standing_face_outer_accessory_[MystiqueX.Clothes[face_outer_accessory].string].png"

    anchor (0.5, 0.5)

layeredimage Mystique_sprite standing Raven:
    always:
        "images/Raven_standing/Raven_standing_body.png"

    if MystiqueX.disguise_Clothes["underwear"].string:
        "images/Mystique_standing/Mystique_standing_underwear_[MystiqueX.disguise_Clothes[underwear].string]_[MystiqueX.disguise_Clothes[underwear].state].png"

    if MystiqueX.disguise_Clothes["skirt"].string:
        "images/Mystique_standing/Mystique_standing_skirt_[MystiqueX.disguise_Clothes[skirt].string].png"

    always:
        "images/Raven_standing/Raven_standing_arms[MystiqueX.arm_pose].png"

    always:
        "images/Raven_standing/Raven_standing_breasts.png"

    if MystiqueX.disguise_Clothes["bra"].string:
        "images/Mystique_standing/Mystique_standing_bra_[MystiqueX.disguise_Clothes[bra].string]_[MystiqueX.disguise_Clothes[bra].state].png"

    if MystiqueX.disguise_Clothes["boots"].string:
        "images/Mystique_standing/Mystique_standing_boots_[MystiqueX.disguise_Clothes[boots].string].png"

    if MystiqueX.disguise_Clothes["dress"].string:
        "images/Mystique_standing/Mystique_standing_dress_[MystiqueX.disguise_Clothes[dress].string].png"

    if MystiqueX.disguise_Clothes["belt"].string:
        "images/Mystique_standing/Mystique_standing_belt_[MystiqueX.disguise_Clothes[belt].string].png"

    if MystiqueX.disguise_Clothes["top"].string:
        "images/Mystique_standing/Mystique_standing_top_[MystiqueX.disguise_Clothes[top].string].png"

    if MystiqueX.disguise_Clothes["jacket"].string:
        "images/Mystique_standing/Mystique_standing_jacket_[MystiqueX.disguise_Clothes[jacket].string].png"

    if MystiqueX.disguise_Clothes["gloves"].string:
        "images/Mystique_standing/Mystique_standing_gloves_[MystiqueX.disguise_Clothes[gloves].string].png"

    always:
        "Raven_head" pos (0.54, 0.32) zoom 0.43

    anchor (0.5, 0.0) offset (0, 180) zoom 0.55

layeredimage Raven_head:
    always:
        "images/Raven_standing/Raven_standing_head.png"

    always:
        "images/Raven_standing/Raven_standing_brows_[MystiqueX.brows].png"

    always:
        "images/Raven_standing/Raven_standing_mouth_[MystiqueX.mouth].png"

    if MystiqueX.eyes == "closed":
        "images/Raven_standing/Raven_standing_eyes_closed.png"
    else:
        "Raven_blinking"

    always:
        "images/Raven_standing/Raven_standing_hair_[MystiqueX.disguise_Clothes[hair].string].png"

    if MystiqueX.disguise_Clothes["face_outer_accessory"].string:
        "images/Mystique_standing/Mystique_standing_face_outer_accessory_[MystiqueX.disguise_Clothes[face_outer_accessory].string].png"

    anchor (0.5, 0.5)
