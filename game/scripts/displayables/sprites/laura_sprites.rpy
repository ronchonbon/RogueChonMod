layeredimage Laura_sprite standing:
    # always:
    #     "images/Laura_standing/Laura_standing_head_reference.png"

    if LauraX.Clothes["jacket"].string:
        "images/Laura_standing/Laura_standing_jacket_[LauraX.Clothes[jacket].string]_back_[LauraX.Clothes[jacket].state].png"

    if LauraX.Clothes["underwear"].state:
        "images/Laura_standing/Laura_standing_underwear_[LauraX.Clothes[underwear].string]_back.png"

    always:
        "images/Laura_standing/Laura_standing_arm[LauraX.arm_pose]_right.png"

    if not renpy.showing("Laura_sprite blowjob"):
        "Laura_hair_back" pos (0.209, 0.371) zoom 0.5

    always:
        "images/Laura_standing/Laura_standing_body.png"

    always:
        "images/Laura_standing/Laura_standing_arms[LauraX.arm_pose]_mid.png"

    if LauraX.pubes:
        "images/Laura_standing/Laura_standing_pubes.png"

    always:
        "images/Laura_standing/Laura_standing_breasts.png"

    if not LauraX.Clothes["gloves"].string:
        Null()
    elif LauraX.Clothes["gloves"].string == "Tifa_gloves":
        "images/Laura_standing/Laura_standing_gloves[LauraX.arm_pose]_[LauraX.Clothes[gloves].string]_right.png"
    elif LauraX.Clothes["gloves"].string == "bunny_gloves" and LauraX.arm_pose == 1:
        "images/Laura_standing/Laura_standing_gloves[LauraX.arm_pose]_[LauraX.Clothes[gloves].string].png"
    else:
        "images/Laura_standing/Laura_standing_gloves[LauraX.arm_pose]_[LauraX.Clothes[gloves].string].png"

    if LauraX.Clothes["gloves"].string == "Tifa_gloves":
        "images/Laura_standing/Laura_standing_gloves[LauraX.arm_pose]_[LauraX.Clothes[gloves].string]_mid.png"

    if LauraX.Clothes["body_piercings"].string:
        "images/Laura_standing/Laura_standing_body_piercings_breasts_[LauraX.Clothes[body_piercings].string].png"

    if LauraX.Clothes["body_piercings"].string:
        "images/Laura_standing/Laura_standing_body_piercings_pussy_[LauraX.Clothes[body_piercings].string].png"

    if LauraX.Clothes["nipple_accessories"].string:
        "images/Laura_standing/Laura_standing_nipple_accessories_[LauraX.Clothes[nipple_accessories].string].png"

    if LauraX.Clothes["bra"].string:
        "images/Laura_standing/Laura_standing_bra_[LauraX.Clothes[bra].string]_[LauraX.Clothes[bra].state].png"

    if not LauraX.Clothes["underwear"].string:
        Null()
    elif LauraX.grool > 1 and LauraX.Clothes["underwear"].string not in ["leather_panties", "black_bikini_bottoms"]:
        "images/Laura_standing/Laura_standing_underwear_[LauraX.Clothes[underwear].string]_grool_[LauraX.Clothes[underwear].state].png"
    else:
        "images/Laura_standing/Laura_standing_underwear_[LauraX.Clothes[underwear].string]_[LauraX.Clothes[underwear].state].png"

    if not LauraX.Clothes["hose"].string:
        Null()
    elif LauraX.Clothes["hose"].string == "red_stockings_and_garterbelt":
        "images/Laura_standing/Laura_standing_hose_red_stockings.png"
    else:
        "images/Laura_standing/Laura_standing_hose_[LauraX.Clothes[hose].string].png"

    if LauraX.Clothes["hose"].string == "red_stockings_and_garterbelt":
        "images/Laura_standing/Laura_standing_hose_red_garterbelt.png"

    if LauraX.grool and not LauraX.Outfit.pussy_covered:
        "images/Laura_standing/Laura_standing_grool.png"

    always:
        "Laura_grool_animations"

    if LauraX.spunk["pussy"] or LauraX.spunk["anus"]:
        "images/Laura_standing/Laura_standing_spunk_pussy.png"

    always:
        "Laura_spunk_animations"

    if LauraX.Clothes["bodysuit"].string:
        "images/Laura_standing/Laura_standing_bodysuit_[LauraX.Clothes[bodysuit].string]_[LauraX.Clothes[bodysuit].state].png"

    if LauraX.Clothes["pants"].string:
        "images/Laura_standing/Laura_standing_pants_[LauraX.Clothes[pants].string].png"

    if LauraX.Clothes["skirt"].string:
        "images/Laura_standing/Laura_standing_skirt_[LauraX.Clothes[skirt].string]_[LauraX.Clothes[skirt].state].png"

    if LauraX.Clothes["dress"].string:
        "images/Laura_standing/Laura_standing_dress[LauraX.arm_pose]_[LauraX.Clothes[dress].string]_[LauraX.Clothes[dress].state].png"

    if LauraX.Clothes["top"].string:
        "images/Laura_standing/Laura_standing_top_[LauraX.Clothes[top].string].png"

    if LauraX.Clothes["neck"].string:
        "images/Laura_standing/Laura_standing_neck_[LauraX.Clothes[neck].string].png"

    if not renpy.showing("Laura_sprite blowjob"):
        "Laura_head" pos (0.209, 0.371) zoom 0.5

    if LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_arm[LauraX.arm_pose]_left.png"

    if LauraX.Clothes["gloves"].string == "Tifa_gloves" and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_gloves[LauraX.arm_pose]_[LauraX.Clothes[gloves].string]_left.png"

    if LauraX.Clothes["dress"].string == "Mavis_dress":
        "images/Laura_standing/Laura_standing_dress[LauraX.arm_pose]_[LauraX.Clothes[dress].string]_sleeves.png"

    if LauraX.Clothes["body_piercings"].string and LauraX.Outfit.pussy_covered:
        "images/Laura_standing/Laura_standing_body_piercings_pussy[LauraX.Clothes[body_piercings].string]_covered.png"

    if LauraX.Clothes["body_piercings"].string and LauraX.Outfit.breasts_covered:
        "images/Laura_standing/Laura_standing_body_piercings_breasts_[LauraX.Clothes[body_piercings].string]_covered.png"

    if LauraX.Clothes["jacket"].string and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_jacket[LauraX.arm_pose]_[LauraX.Clothes[jacket].string]_sleeves.png"

    if LauraX.Clothes["suspenders"].string:
        "images/Laura_standing/Laura_standing_suspenders_[LauraX.Clothes[suspenders].string]_[LauraX.Clothes[suspenders].state].png"

    if LauraX.Clothes["jacket"].string:
        "images/Laura_standing/Laura_standing_jacket[LauraX.arm_pose]_[LauraX.Clothes[jacket].string]_[LauraX.Clothes[jacket].state].png"

    if LauraX.claws and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_claws[LauraX.arm_pose].png"

    if LauraX.spunk["breasts"]:
        "images/Laura_standing/Laura_standing_spunk_breasts.png"

    if LauraX.spunk["belly"]:
        "images/Laura_standing/Laura_standing_spunk_belly.png"

    if LauraX.spunk["hand"] and LauraX.arm_pose == 1:
        "images/Laura_standing/Laura_standing_spunk_hand.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_body[LauraX.arm_pose].png"

    if LauraX.wet and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_water_arm[LauraX.arm_pose].png"

    if LauraX.held_item and LauraX.arm_pose == 2:
        "images/Laura_standing/Laura_standing_held_item_[LauraX.Clothes[held_item].string].png"

    always:
        "Laura_standing_fondling_animations"

    anchor (0.5, 0.0) offset (45, 170) zoom 0.535

layeredimage Laura_hair_back:
    if LauraX.wet:
        "images/Laura_standing/Laura_standing_hair_wet_back.png"
    else:
        "images/Laura_standing/Laura_standing_hair_[LauraX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Laura_head:
    if not renpy.showing("Laura_sprite sex"):
        Null()
    elif LauraX.wet:
        "images/Laura_sex/Laura_sex_hair_wet_back.png"
    else:
        "images/Laura_sex/Laura_sex_hair_[LauraX.Clothes[hair].string]_back.png"

    always:
        "images/Laura_standing/Laura_standing_head.png"
        # "images/Laura_standing/Laura_standing_head[LauraX.blushing].png"

    if LauraX.blushing == "_blush2":
        "images/Laura_standing/Laura_standing_brows_[LauraX.brows]_blush.png"
    else:
        "images/Laura_standing/Laura_standing_brows_[LauraX.brows].png"

    if renpy.showing("Laura_sprite titjob") and LauraX.primary_Action.speed in [3, 5]:
        "images/Laura_standing/Laura_standing_mouth_tongue.png"
    else:
        "images/Laura_standing/Laura_standing_mouth_[LauraX.mouth].png"

    if not LauraX.spunk["mouth"]:
        Null()
    elif renpy.showing("Laura_sprite titjob") and LauraX.primary_Action.speed in [3, 5]:
        "images/Laura_standing/Laura_standing_spunk_mouth_tongue.png"
    else:
        "images/Laura_standing/Laura_standing_spunk_mouth_[LauraX.mouth].png"

    if LauraX.eyes == "closed":
        "images/Laura_standing/Laura_standing_eyes_closed.png"
    else:
        "Laura_blinking"

    if LauraX.spunk["chin"]:
        "images/Laura_standing/Laura_standing_spunk_chin.png"

    if LauraX.spunk["face"]:
        "images/Laura_standing/Laura_standing_spunk_face.png"

    if renpy.showing("Laura_sprite titjob") or renpy.showing("Laura_sprite sex"):
        Null()
    else:
        "images/Laura_standing/Laura_standing_hair_mid.png"

    if renpy.showing("Laura_sprite sex") and LauraX.wet:
        "images/Laura_sex/Laura_sex_hair_wet.png"
    elif renpy.showing("Laura_sprite sex"):
        "images/Laura_sex/Laura_sex_hair_[LauraX.Clothes[hair].string].png"
    elif LauraX.wet:
        "images/Laura_standing/Laura_standing_hair_wet.png"
    else:
        "images/Laura_standing/Laura_standing_hair_[LauraX.Clothes[hair].string].png"

    if LauraX.spunk["hair"]:
        "images/Laura_standing/Laura_standing_spunk_hair.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_head.png"

    if LauraX.wet:
        "images/Laura_standing/Laura_standing_water_hair.png"

    anchor (0.5, 0.5)

image Laura_handjob_under:
    "images/Laura_handjob/Laura_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Laura_handjob_over:
    "images/Laura_handjob/Laura_handjob_hand_over.png"

    anchor (0.5, 0.5)

image Laura_titjob_hair_mid:
    "images/Laura_standing/Laura_standing_hair_mid.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_hair:
    if LauraX.wet:
        "images/Laura_standing/Laura_standing_hair_wet.png"
    else:
        "images/Laura_standing/Laura_standing_hair_[LauraX.Clothes[hair].string].png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_body:
    always:
        "images/Laura_titjob/Laura_titjob_body.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_left_arm:
    always:
        "images/Laura_titjob/Laura_titjob_left_hand.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_right_arm:
    always:
        "images/Laura_titjob/Laura_titjob_right_hand.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_right_arm_back:
    always:
        "images/Laura_titjob/Laura_titjob_right_hand_back.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_left_breast:
    always:
        "images/Laura_titjob/Laura_titjob_left_breast.png"

    if LauraX.spunk["breasts"]:
        "images/Laura_titjob/Laura_titjob_spunk_left_breast.png"

    anchor (0.5, 0.5)

layeredimage Laura_titjob_right_breast:
    always:
        "images/Laura_titjob/Laura_titjob_right_breast.png"

    if LauraX.spunk["breasts"]:
        "images/Laura_titjob/Laura_titjob_spunk_right_breast.png"

    anchor (0.5, 0.5)
