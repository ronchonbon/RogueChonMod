layeredimage Emma_domme:
    always:
        "images/Emma_domme/Emma_domme_back_hair[EmmaX.outfit[back_hair]].png"

    always:
        "images/Emma_domme/Emma_domme_body.png"

    if EmmaX.outfit["neck"]:
        "images/Emma_domme/Emma_domme_neck[EmmaX.outfit[neck]].png"

    always:
        "Emma_domme_head"

    if EmmaX.outfit["hose"]:
        "images/Emma_domme/Emma_domme_hose[EmmaX.outfit[hose]].png"

    if EmmaX.outfit["dress"]:
        "images/Emma_domme/Emma_domme_dress[EmmaX.outfit[dress]].png"

    if EmmaX.outfit["gloves"]:
        "images/Emma_domme/Emma_domme_gloves[EmmaX.outfit[gloves]].png"

    always:
        "images/Emma_domme/Emma_domme_hair[EmmaX.outfit[hair]].png"

    if EmmaX.outfit["held_item"]:
        "images/Emma_domme/Emma_domme_held_item[EmmaX.outfit[held_item]].png"

    anchor (0.5, -0.16) zoom 0.48

layeredimage Emma_domme_head:
    always:
        "images/Emma_domme/Emma_domme_head.png"

    always:
        "images/Emma_domme/Emma_domme_brows_angry.png"

    always:
        "images/Emma_domme/Emma_domme_mouth[EmmaX.mouth].png"

    always:
        "images/Emma_domme/Emma_domme_eyes[EmmaX.eyes].png"
