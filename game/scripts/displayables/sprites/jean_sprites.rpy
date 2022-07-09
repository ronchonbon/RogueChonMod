layeredimage Jean_sprite standing:
    # always:
    #     "images/Jean_standing/Jean_standing_head_reference.png"

    always:
        "Jean_hair_back" pos (0.32, 0.27) zoom 0.32

    always:
        "images/Jean_standing/Jean_standing_arm[JeanX.arm_pose]_right.png"

    always:
        "images/Jean_standing/Jean_standing_body.png"

    if JeanX.pubes:
        "images/Jean_standing/Jean_standing_pubes.png"

    always:
        "images/Jean_standing/Jean_standing_breasts.png"

    if JeanX.Clothes["body_piercings"].string:
        "images/Jean_standing/Jean_standing_body_piercings_breasts_[JeanX.Clothes[body_piercings].string].png"

    if JeanX.Clothes["body_piercings"].string:
        "images/Jean_standing/Jean_standing_body_piercings_pussy_[JeanX.Clothes[body_piercings].string].png"

    if JeanX.Clothes["underwear"].string:
        "images/Jean_standing/Jean_standing_underwear_[JeanX.Clothes[underwear].string]_[JeanX.Clothes[underwear].state].png"

    if JeanX.Clothes["hose"].string:
        "images/Jean_standing/Jean_standing_hose_[JeanX.Clothes[hose].string].png"

    if JeanX.grool and not JeanX.Outfit.pussy_covered:
        "images/Jean_standing/Jean_standing_grool.png"

    if JeanX.spunk["pussy"] or JeanX.spunk["anus"]:
        "images/Jean_standing/Jean_standing_spunk_pussy.png"

    if JeanX.Clothes["pants"].string:
        "images/Jean_standing/Jean_standing_pants_[JeanX.Clothes[pants].string]_[JeanX.Clothes[pants].state].png"

    if JeanX.Clothes["skirt"].string:
        "images/Jean_standing/Jean_standing_skirt_[JeanX.Clothes[skirt].string]_[JeanX.Clothes[skirt].state].png"

    always:
        "images/Jean_standing/Jean_standing_arm[JeanX.arm_pose]_left.png"

    if JeanX.Clothes["bra"].string:
        "images/Jean_standing/Jean_standing_bra[JeanX.arm_pose]_[JeanX.Clothes[bra].string]_[JeanX.Clothes[bra].state].png"

    if JeanX.Clothes["top"].string:
        "images/Jean_standing/Jean_standing_top[JeanX.arm_pose]_[JeanX.Clothes[top].string]_[JeanX.Clothes[top].state].png"

    if JeanX.Clothes["suspenders"].string:
        "images/Jean_standing/Jean_standing_suspenders_[JeanX.Clothes[suspenders].string]_[JeanX.Clothes[suspenders].state].png"

    always:
        "Jean_head" pos (0.32, 0.27) zoom 0.32

    if JeanX.Clothes["body_piercings"].string and JeanX.Outfit.pussy_covered:
        "images/Jean_standing/Jean_standing_body_piercings_pussy[JeanX.Clothes[body_piercings].string]_covered.png"

    if JeanX.Clothes["body_piercings"].string and JeanX.Outfit.breasts_covered:
        "images/Jean_standing/Jean_standing_body_piercings_breasts_[JeanX.Clothes[body_piercings].string]_covered.png"

    always:
        "images/Jean_standing/Jean_standing_hand[JeanX.arm_pose]_right.png"

    if not renpy.showing("Jean_sprite handjob") and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_hand[JeanX.arm_pose]_left.png"

    if JeanX.Clothes["bra"].string == "blackyellow_sports_bra" and not renpy.showing("Jean_sprite handjob") and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_bra[JeanX.arm_pose]_[JeanX.Clothes[bra].string]_sleeves.png"

    if JeanX.Clothes["top"].string == "pink_shirt" and not renpy.showing("Jean_sprite handjob") and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_top[JeanX.arm_pose]_[JeanX.Clothes[top].string]_sleeves.png"

    if JeanX.spunk["breasts"]:
        "images/Jean_standing/Jean_standing_spunk_breasts.png"

    if JeanX.spunk["belly"]:
        "images/Jean_standing/Jean_standing_spunk_belly.png"

    if JeanX.wet:
        "images/Jean_standing/Jean_standing_water_body[JeanX.arm_pose].png"

    if JeanX.wet and JeanX.arm_pose == 1:
        "images/Jean_standing/Jean_standing_water_arm[JeanX.arm_pose].png"

    if JeanX.held_item and JeanX.arm_pose == 2:
        "images/Jean_standing/Jean_standing_held[JeanX.Clothes[held_item].string].png"

    always:
        "Jean_standing_fondling_animations" zoom 0.96

    anchor (0.5, 0.0) offset (10, 180) zoom 0.52

layeredimage Jean_hair_back:
    if JeanX.wet:
        "images/Jean_standing/Jean_standing_hair_wet_hair_back.png"
    elif JeanX.Clothes["hair"].string != "ponytail":
        "images/Jean_standing/Jean_standing_hair_[JeanX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Jean_head:
    always:
        "images/Jean_standing/Jean_standing_head[JeanX.blushing].png"

    always:
        "images/Jean_standing/Jean_standing_brows_[JeanX.brows][JeanX.blushing].png"

    if JeanX.spunk["mouth"]:
        "images/Jean_standing/Jean_standing_spunk_mouth_[JeanX.mouth].png"
    else:
        "images/Jean_standing/Jean_standing_mouth_[JeanX.mouth].png"

    if JeanX.eyes == "closed":
        "images/Jean_standing/Jean_standing_eyes_closed.png"
    else:
        "Jean_blinking"

    if JeanX.spunk["chin"]:
        "images/Jean_standing/Jean_standing_spunk_chin.png"

    if JeanX.spunk["face"]:
        "images/Jean_standing/Jean_standing_spunk_face.png"

    if JeanX.wet:
        "images/Jean_standing/Jean_standing_hair_wet_hair.png"
    else:
        "images/Jean_standing/Jean_standing_hair_[JeanX.Clothes[hair].string].png"

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

image Jean_titjob_bra_back:
    "images/Jean_titjob/Jean_titjob_bra_back.png"

    anchor (0.5, 0.5)

layeredimage Jean_titjob_body:
    always:
        "images/Jean_titjob/Jean_titjob_body.png"

    anchor (0.5, 0.5)

layeredimage Jean_titjob_right_breast:
    if renpy.showing("Jean_sprite titjob"):
        "images/Jean_titjob/Jean_titjob_right_breast.png"
    else:
        "images/Jean_blowjob/Jean_blowjob_right_breast.png"

    if JeanX.spunk["breasts"]:
        "images/Jean_titjob/Jean_titjob_spunk_breasts_under.png"

    anchor (0.5, 0.5)

image Jean_titjob_bra_stretch:
    "images/Jean_titjob/Jean_titjob_bra_stretch.png"

    anchor (0.5, 0.5)

layeredimage Jean_titjob_breasts:
    always:
        "images/Jean_titjob/Jean_titjob_left_breast.png"

    if renpy.showing("Jean_sprite titjob"):
        "images/Jean_titjob/Jean_titjob_right_breast_over.png"

    if JeanX.spunk["breasts"]:
        "images/Jean_titjob/Jean_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Jean_titjob_hair:
    if JeanX.wet:
        "images/Jean_blowjob/Jean_blowjob_hair_wet.png"
    else:
        "images/Jean_blowjob/Jean_blowjob_hair_[JeanX.Clothes[hair].string].png"

    anchor (0.5, 0.5)

layeredimage Jean_blowjob_hair_back:
    if JeanX.wet:
        "images/Jean_blowjob/Jean_blowjob_hair_wet_hair_back.png"
    elif JeanX.Clothes["hair"].string != "ponytail":
        "images/Jean_blowjob/Jean_blowjob_hair_[JeanX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Jean_blowjob_head:
    if renpy.showing("Jean_sprite sex") and (JeanX.wet or JeanX.Clothes["hair"].string == "wet_hair"):
        "images/Jean_blowjob/Jean_blowjob_hair_mid.png"
    elif JeanX.wet:
        "images/Jean_blowjob/Jean_blowjob_hair_wet_hair_back.png"
    elif JeanX.Clothes["hair"].string != "ponytail":
        "images/Jean_blowjob/Jean_blowjob_hair_[JeanX.Clothes[hair].string]_back.png"

    always:
        "images/Jean_blowjob/Jean_blowjob_head[JeanX.blushing].png"

    if renpy.showing("Jean_sprite titjob") and JeanX.primary_Action.speed > 2:
        "images/Jean_blowjob/Jean_blowjob_mouth_tongue.png"
    elif renpy.showing("Jean_sprite blowjob") and JeanX.primary_Action.speed == 1:
        "images/Jean_blowjob/Jean_blowjob_mouth_tongue.png"
    elif renpy.showing("Jean_sprite blowjob") and JeanX.primary_Action.speed == 2:
        "Jean_blowjob_mouth_animations"
    elif renpy.showing("Jean_sprite blowjob") and JeanX.primary_Action.speed > 2:
        "images/Jean_blowjob/Jean_blowjob_mouth_sucking.png"
    else:
        "images/Jean_blowjob/Jean_blowjob_mouth_[JeanX.mouth].png"

    if not JeanX.spunk["mouth"]:
        Null()
    elif renpy.showing("Jean_sprite titjob") and JeanX.primary_Action.speed > 2:
        "images/Jean_blowjob/Jean_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Jean_sprite blowjob") and JeanX.primary_Action.speed == 1:
        "images/Jean_blowjob/Jean_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Jean_sprite blowjob") and JeanX.primary_Action.speed > 2:
        "images/Jean_blowjob/Jean_blowjob_spunk_mouth_sucking_under.png"
    elif JeanX.mouth == "sucking":
        "images/Jean_blowjob/Jean_blowjob_spunk_mouth_sucking_under.png"
    else:
        "images/Jean_blowjob/Jean_blowjob_spunk_mouth_[JeanX.mouth].png"

    always:
        "images/Jean_blowjob/Jean_blowjob_brows_[JeanX.brows].png"

    if JeanX.eyes == "closed":
        "images/Jean_blowjob/Jean_blowjob_eyes_closed.png"
    else:
        "Jean_blowjob_blinking"

    if JeanX.spunk["face"]:
        "images/Jean_blowjob/Jean_blowjob_spunk_face.png"

    if JeanX.wet:
        "images/Jean_blowjob/Jean_blowjob_hair_wet_hair.png"
    else:
        "images/Jean_blowjob/Jean_blowjob_hair_[JeanX.Clothes[hair].string].png"

    if JeanX.spunk["hair"]:
        "images/Jean_blowjob/Jean_blowjob_spunk_hair.png"

    anchor (0.5, 0.5)
