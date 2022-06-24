layeredimage Mystique_sprite standing normal:
    always:
        "Mystique_hair_back" pos (0.54, 0.32) zoom 0.43

    always:
        "images/Mystique_standing/Mystique_standing_body.png"

    always:
        "Mystique_grool_animations"

    always:
        "Mystique_spunk_animations"

    if not MystiqueX.outfit["underwear"]:
        Null()
    elif MystiqueX.underwear_pulled_down:
        "images/Mystique_standing/Mystique_standing_underwear[MystiqueX.outfit[underwear]]_down.png"
    else:
        "images/Mystique_standing/Mystique_standing_underwear[MystiqueX.outfit[underwear]].png"

    if not MystiqueX.outfit["bottom"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_bottom[MystiqueX.outfit[bottom]].png"

    always:
        "images/Mystique_standing/Mystique_standing_arms1.png"

    always:
        "images/Mystique_standing/Mystique_standing_breasts.png"

    if not MystiqueX.outfit["bra"]:
        Null()
    elif MystiqueX.bra_pulled_up:
        "images/Mystique_standing/Mystique_standing_bra[MystiqueX.outfit[bra]]_up.png"
    else:
        "images/Mystique_standing/Mystique_standing_bra[MystiqueX.outfit[bra]].png"

    if MystiqueX.outfit["boots"]:
        "images/Mystique_standing/Mystique_standing_boots[MystiqueX.outfit[boots]].png"

    if MystiqueX.outfit["dress"]:
        "images/Mystique_standing/Mystique_standing_dress[MystiqueX.outfit[dress]].png"

    if MystiqueX.outfit["belt"]:
        "images/Mystique_standing/Mystique_standing_belt[MystiqueX.outfit[belt]].png"

    if not MystiqueX.outfit["top"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_top[MystiqueX.outfit[top]].png"

    if MystiqueX.outfit["jacket"]:
        "images/Mystique_standing/Mystique_standing_jacket[MystiqueX.outfit[jacket]]1.png"

    if MystiqueX.outfit["gloves"]:
        "images/Mystique_standing/Mystique_standing_gloves[MystiqueX.outfit[gloves]]1.png"

    always:
        "Mystique_head" pos (0.54, 0.32) zoom 0.43

    always:
        "Mystique_standing_fondling_animations"

    anchor (0.5, 0.0) offset (0, 180) zoom 0.55

image Mystique_hair_back:
    "images/Mystique_standing/Mystique_standing_hair_long_back.png"

    anchor (0.5, 0.5)

layeredimage Mystique_head:
    always:
        "images/Mystique_standing/Mystique_standing_head.png"

    always:
        "images/Mystique_standing/Mystique_standing_brows[MystiqueX.brows].png"

    always:
        "images/Mystique_standing/Mystique_standing_mouth[MystiqueX.mouth].png"

    if MystiqueX.spunk["mouth"]:
        "images/Mystique_standing/Mystique_standing_spunk_mouth[MystiqueX.mouth].png"

    if MystiqueX.eyes == "_closed":
        "images/Mystique_standing/Mystique_standing_eyes_closed.png"
    else:
        "Mystique_blinking"

    always:
        "images/Mystique_standing/Mystique_standing_hair_long.png"

    if MystiqueX.outfit["face_outer_accessory"]:
        "images/Mystique_standing/Mystique_standing_face_outer_accessory[MystiqueX.outfit[face_outer_accessory]].png"

    anchor (0.5, 0.5)

layeredimage Mystique_sprite standing Raven:
    always:
        "images/Raven_standing/Raven_standing_body.png"

    if not MystiqueX.outfit["underwear"]:
        Null()
    elif MystiqueX.underwear_pulled_down:
        "images/Mystique_standing/Mystique_standing_underwear[MystiqueX.outfit[underwear]]_down.png"
    else:
        "images/Mystique_standing/Mystique_standing_underwear[MystiqueX.outfit[underwear]].png"

    if not MystiqueX.outfit["bottom"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_bottom[MystiqueX.outfit[bottom]].png"

    always:
        "images/Raven_standing/Raven_standing_arms1.png"

    always:
        "images/Raven_standing/Raven_standing_breasts.png"

    if not MystiqueX.outfit["bra"]:
        Null()
    elif MystiqueX.bra_pulled_up:
        "images/Mystique_standing/Mystique_standing_bra[MystiqueX.outfit[bra]]_up.png"
    else:
        "images/Mystique_standing/Mystique_standing_bra[MystiqueX.outfit[bra]].png"

    if MystiqueX.outfit["boots"]:
        "images/Mystique_standing/Mystique_standing_boots[MystiqueX.outfit[boots]].png"

    if MystiqueX.outfit["dress"]:
        "images/Mystique_standing/Mystique_standing_dress[MystiqueX.outfit[dress]].png"

    if MystiqueX.outfit["belt"]:
        "images/Mystique_standing/Mystique_standing_belt[MystiqueX.outfit[belt]].png"

    if not MystiqueX.outfit["top"]:
        Null()
    else:
        "images/Mystique_standing/Mystique_standing_top[MystiqueX.outfit[top]].png"

    if MystiqueX.outfit["jacket"]:
        "images/Mystique_standing/Mystique_standing_jacket[MystiqueX.outfit[jacket]]1.png"

    if MystiqueX.outfit["gloves"]:
        "images/Mystique_standing/Mystique_standing_gloves[MystiqueX.outfit[gloves]]1.png"

    always:
        "Raven_head" pos (0.54, 0.32) zoom 0.43

    anchor (0.5, 0.0) offset (0, 180) zoom 0.55

layeredimage Raven_head:
    always:
        "images/Raven_standing/Raven_standing_head.png"

    always:
        "images/Raven_standing/Raven_standing_brows[MystiqueX.brows].png"

    always:
        "images/Raven_standing/Raven_standing_mouth[MystiqueX.mouth].png"

    if MystiqueX.eyes == "_closed":
        "images/Raven_standing/Raven_standing_eyes_closed.png"
    else:
        "Raven_blinking"

    always:
        "images/Raven_standing/Raven_standing_hair_short.png"

    if MystiqueX.outfit["face_outer_accessory"]:
        "images/Mystique_standing/Mystique_standing_face_outer_accessory[MystiqueX.outfit[face_outer_accessory]].png"

    anchor (0.5, 0.5)
