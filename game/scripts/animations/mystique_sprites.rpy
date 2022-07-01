layeredimage Mystique_sprite standing normal:
    always:
        "Mystique_hair_back" pos (0.54, 0.32) zoom 0.43

    always:
        "images/Mystique_standing/Mystique_standing_body.png"

    always:
        "Mystique_grool_animations"

    always:
        "Mystique_spunk_animations"

    if not MystiqueX.Clothes["underwear"]:
        Null()
    elif MystiqueX.Clothes["underwear"].state:
        "images/Mystique_standing/Mystique_standing_underwear_[MystiqueX.Clothes[underwear]]_down.png"
    else:
        "images/Mystique_standing/Mystique_standing_underwear_[MystiqueX.Clothes[underwear]].png"

    if not MystiqueX.Clothes["bottom"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_bottom[MystiqueX.Clothes[bottom]].png"

    always:
        "images/Mystique_standing/Mystique_standing_arms1.png"

    always:
        "images/Mystique_standing/Mystique_standing_breasts.png"

    if not MystiqueX.Clothes["bra"]:
        Null()
    elif MystiqueX.Clothes["bra"].state:
        "images/Mystique_standing/Mystique_standing_bra_[MystiqueX.Clothes[bra]]_up.png"
    else:
        "images/Mystique_standing/Mystique_standing_bra_[MystiqueX.Clothes[bra]].png"

    if MystiqueX.Clothes["boots"]:
        "images/Mystique_standing/Mystique_standing_boots[MystiqueX.Clothes[boots]].png"

    if MystiqueX.Clothes["dress"]:
        "images/Mystique_standing/Mystique_standing_dress[MystiqueX.Clothes[dress]].png"

    if MystiqueX.Clothes["belt"]:
        "images/Mystique_standing/Mystique_standing_belt[MystiqueX.Clothes[belt]].png"

    if not MystiqueX.Clothes["top"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_top_[MystiqueX.Clothes[top]].png"

    if MystiqueX.Clothes["jacket"]:
        "images/Mystique_standing/Mystique_standing_jacket_[MystiqueX.Clothes[jacket]]1.png"

    if MystiqueX.Clothes["gloves"]:
        "images/Mystique_standing/Mystique_standing_gloves[MystiqueX.Clothes[gloves]]1.png"

    always:
        "Mystique_head" pos (0.54, 0.32) zoom 0.43

    always:
        "Mystique_standing_fondling_animations" zoom 0.91

    anchor (0.5, 0.0) offset (0, 180) zoom 0.55

image Mystique_hair_back:
    "images/Mystique_standing/Mystique_standing_hair_long_back.png"

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
        "images/Mystique_standing/Mystique_standing_hair_long.png"

    if MystiqueX.Clothes["face_outer_accessory"]:
        "images/Mystique_standing/Mystique_standing_face_outer_accessory[MystiqueX.Clothes[face_outer_accessory]].png"

    anchor (0.5, 0.5)

layeredimage Mystique_sprite standing Raven:
    always:
        "images/Raven_standing/Raven_standing_body.png"

    if not MystiqueX.disguise_outfit["underwear"]:
        Null()
    elif MystiqueX.Clothes["underwear"].state:
        "images/Mystique_standing/Mystique_standing_underwear_[MystiqueX.disguise_outfit[underwear]]_down.png"
    else:
        "images/Mystique_standing/Mystique_standing_underwear_[MystiqueX.disguise_outfit[underwear]].png"

    if not MystiqueX.disguise_outfit["bottom"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_bottom[MystiqueX.disguise_outfit[bottom]].png"

    always:
        "images/Raven_standing/Raven_standing_arms1.png"

    always:
        "images/Raven_standing/Raven_standing_breasts.png"

    if not MystiqueX.disguise_outfit["bra"]:
        Null()
    elif MystiqueX.Clothes["bra"].state:
        "images/Mystique_standing/Mystique_standing_bra_[MystiqueX.disguise_outfit[bra]]_up.png"
    else:
        "images/Mystique_standing/Mystique_standing_bra_[MystiqueX.disguise_outfit[bra]].png"

    if MystiqueX.disguise_outfit["boots"]:
        "images/Mystique_standing/Mystique_standing_boots[MystiqueX.disguise_outfit[boots]].png"

    if MystiqueX.disguise_outfit["dress"]:
        "images/Mystique_standing/Mystique_standing_dress[MystiqueX.disguise_outfit[dress]].png"

    if MystiqueX.disguise_outfit["belt"]:
        "images/Mystique_standing/Mystique_standing_belt[MystiqueX.disguise_outfit[belt]].png"

    if not MystiqueX.disguise_outfit["top"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_top_[MystiqueX.disguise_outfit[top]].png"

    if MystiqueX.disguise_outfit["jacket"]:
        "images/Mystique_standing/Mystique_standing_jacket_[MystiqueX.disguise_outfit[jacket]]1.png"

    if MystiqueX.disguise_outfit["gloves"]:
        "images/Mystique_standing/Mystique_standing_gloves[MystiqueX.disguise_outfit[gloves]]1.png"

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
        "images/Raven_standing/Raven_standing_hair_short.png"

    if MystiqueX.disguise_outfit["face_outer_accessory"]:
        "images/Mystique_standing/Mystique_standing_face_outer_accessory[MystiqueX.disguise_outfit[face_outer_accessory]].png"

    anchor (0.5, 0.5)
