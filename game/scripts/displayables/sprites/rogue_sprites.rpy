layeredimage Rogue_sprite standing:
    # always:
    #     "images/Rogue_standing/Rogue_standing_head_reference.png"

    if RogueX.Clothes["jacket"].string == "green_hoodie":
        "images/Rogue_standing/Rogue_standing_jacket_[RogueX.Clothes[jacket].string]_back.png"

    if RogueX.Clothes["pants"].string == "jeans" and RogueX.Clothes["pants"].state:
        "images/Rogue_standing/Rogue_standing_pants_[RogueX.Clothes[pants].string]_back.png"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_hair_back" pos (0.314, 0.312) zoom 0.58

    if RogueX.Clothes["body_piercings"].string:
        "images/Rogue_standing/Rogue_standing_body[RogueX.pubes]_[RogueX.Clothes[body_piercings].string].png"
    else:
        "images/Rogue_standing/Rogue_standing_body[RogueX.pubes].png"

    if RogueX.Clothes["neck"].string and RogueX.Clothes["gloves"].string:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[neck].string]_[RogueX.Clothes[gloves].string].png"
    elif RogueX.Clothes["neck"].string:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[neck].string].png"
    elif RogueX.Clothes["gloves"].string:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[gloves].string].png"
    else:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose].png"

    if RogueX.Clothes["body_piercings"].string:
        "images/Rogue_standing/Rogue_standing_breasts_[RogueX.Clothes[body_piercings].string].png"
    else:
        "images/Rogue_standing/Rogue_standing_breasts.png"

    if not RogueX.Clothes["underwear"].string:
        Null()
    elif RogueX.grool > 1 and RogueX.Clothes["underwear"].string in ["green_panties", "yellowgreen_shorts"]:
        "images/Rogue_standing/Rogue_standing_underwear_[RogueX.Clothes[underwear].string]_grool_[RogueX.Clothes[underwear].state].png"
    else:
        "images/Rogue_standing/Rogue_standing_underwear_[RogueX.Clothes[underwear].string]_[RogueX.Clothes[underwear].state].png"

    if not RogueX.Clothes["hose"].string:
        Null()
    elif RogueX.grool > 1 and RogueX.Clothes["hose"].string == "black_tights":
        "images/Rogue_standing/Rogue_standing_hose_[RogueX.Clothes[hose].string]_grool.png"
    else:
        "images/Rogue_standing/Rogue_standing_hose_[RogueX.Clothes[hose].string].png"

    if RogueX.grool and not RogueX.Outfit.pussy_covered:
        "images/Rogue_standing/Rogue_standing_grool[RogueX.grool].png"

    always:
        "Rogue_grool_animations"

    always:
        "Rogue_spunk_animations"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_head" pos (0.314, 0.312) zoom 0.58

    if RogueX.Clothes["bra"].string:
        "images/Rogue_standing/Rogue_standing_bra_[RogueX.Clothes[bra].string]_[RogueX.Clothes[bra].state].png"

    if RogueX.Clothes["pants"].string:
        "images/Rogue_standing/Rogue_standing_pants_[RogueX.Clothes[pants].string]_[RogueX.Clothes[pants].state].png"

    if RogueX.Clothes["skirt"].string:
        "images/Rogue_standing/Rogue_standing_skirt_[RogueX.Clothes[skirt].string]_[RogueX.Clothes[skirt].state].png"

    if RogueX.Clothes["top"].string:
        "images/Rogue_standing/Rogue_standing_top[RogueX.arm_pose]_[RogueX.Clothes[top].string]_[RogueX.Clothes[top].state].png"

    if RogueX.Clothes["belt"].string:
        "images/Rogue_standing/Rogue_standing_belt[RogueX.arm_pose]_[RogueX.Clothes[belt].string].png"

    if RogueX.Clothes["jacket"].string:
        "images/Rogue_standing/Rogue_standing_jacket[RogueX.arm_pose]_[RogueX.Clothes[jacket].string]_[RogueX.Clothes[jacket].state].png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_standing/Rogue_standing_spunk_breasts.png"

    if RogueX.spunk["belly"]:
        "images/Rogue_standing/Rogue_standing_spunk_belly.png"

    if RogueX.spunk["hand"] and RogueX.arm_pose == 2:
        "images/Rogue_standing/Rogue_standing_spunk_hand.png"

    if RogueX.wet:
        "images/Rogue_standing/Rogue_standing_water_body[RogueX.arm_pose].png"

    if RogueX.wet == 3:
        "images/Rogue_standing/Rogue_standing_soap_body.png"

    if RogueX.held_item and RogueX.arm_pose == 2:
        "images/Rogue_standing/Rogue_standing_held_item_[RogueX.held_item].png"

    always:
        "Rogue_standing_fondling_animations" zoom 1.04

    anchor (0.5, 0.0) offset (5, 180) zoom 0.48

layeredimage Rogue_hair_back:
    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_hair_wet_hair_back.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_hair_[RogueX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Rogue_head:
    if renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing]_sucking.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing].png"

    if renpy.showing("Rogue_sprite titjob") and RogueX.primary_Action.speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed > 1:
        "Rogue_blowjob_mouth_animation[RogueX.primary_Action.speed]" pos (0.164, 0.55)
    elif RogueX.mouth == "sucking":
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_[RogueX.mouth].png"

    if not RogueX.spunk["mouth"]:
        Null()
    elif renpy.showing("Rogue_sprite titjob") and RogueX.primary_Action.speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed > 1:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_under.png"
    elif RogueX.mouth == "sucking":
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_[RogueX.mouth].png"

    if RogueX.spunk["chin"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_chin.png"

    if RogueX.blushing:
        "images/Rogue_blowjob/Rogue_blowjob_brows_[RogueX.brows]_blush.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_brows_[RogueX.brows].png"

    if RogueX.eyes == "closed":
        "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    else:
        "Rogue_blinking"

    if RogueX.spunk["mouth"] and renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_over.png"

    if RogueX.spunk["face"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face.png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_hair_wet_hair.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_hair_[RogueX.Clothes[hair].string].png"

    if RogueX.spunk["hair"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_hair.png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_water_head.png"

    anchor (0.5, 0.5)

image Rogue_handjob_under:
    "images/Rogue_handjob/Rogue_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Rogue_handjob_over:
    "images/Rogue_handjob/Rogue_handjob_hand_over.png"

    anchor (0.5, 0.5)

layeredimage Rogue_titjob_body:
    always:
        "images/Rogue_titjob/Rogue_titjob_body.png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_titjob/Rogue_titjob_spunk_breasts_under.png"

    anchor (0.5, 0.5)

layeredimage Rogue_titjob_breasts:
    if RogueX.Clothes["body_piercings"].string:
        "images/Rogue_titjob/Rogue_titjob_breasts_[RogueX.Clothes[body_piercings].string].png"
    else:
        "images/Rogue_titjob/Rogue_titjob_breasts.png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_titjob/Rogue_titjob_spunk_breasts.png"

    anchor (0.5, 0.5)

layeredimage Rogue_blowjob_mouth:
    if RogueX.spunk["mouth"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_under.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"

    anchor (0.4, 0.65)

image Rogue_blowjob_mask:
    "images/Rogue_blowjob/Rogue_blowjob_face_mask.png"

    anchor (0.4, 0.65) pos (0.402, 0.645)

layeredimage Rogue_sex_body:
    always:
        "Rogue_hair_back" pos (0.287, 0.075) rotate -10 zoom 0.37

    if RogueX.Clothes["body_piercings"].string:
        "images/Rogue_sex/Rogue_sex_body_[RogueX.Clothes[body_piercings].string].png"
    else:
        "images/Rogue_sex/Rogue_sex_body.png"

    if RogueX.spunk["breasts"]:
        "images/Kitty_sex/Kitty_sex_spunk_breasts.png"

    if RogueX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_body.png"

    if "suck_breasts" in [Player.primary_Action, Player.secondary_Action]:
        "licking" pos (0.245, 0.273) zoom 0.3

    if "fondle_breasts" in [Player.primary_Action, Player.secondary_Action]:
        "Zero_fondle_breasts_left_animation" pos (0.248, 0.31) zoom 0.55

    always:
        "Rogue_head" pos (0.287, 0.075) rotate -10 zoom 0.37

    anchor (0.5, 0.5)

layeredimage Rogue_sex_legs:
    always:
        "images/Rogue_sex/Rogue_sex_legs.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_legs.png"

    if Player.sprite and Player.primary_Action.type == "anal":
        "Rogue_sex_anus_animation[Player.primary_Action.speed]" pos (0.292, 0.386)
    elif "finger_ass" in [Player.primary_Action, Player.secondary_Action]:
        "Rogue_sex_anus" pos (0.292, 0.386) xzoom 0.6
    elif "dildo_ass" in [Player.primary_Action, Player.secondary_Action]:
        "Rogue_sex_anus" pos (0.292, 0.386) xzoom 0.9
    elif RogueX.used_to_anal:
        "images/Rogue_sex/Rogue_sex_anus_loose.png"
    else:
        "images/Rogue_sex/Rogue_sex_anus_tight.png"

    if not RogueX.spunk["anus"]:
        Null()
    elif Player.sprite and Player.primary_Action.type == "anal" and Player.primary_Action.speed > 1:
        "Rogue_sex_spunk_anus_under" pos (0.292, 0.386)
    elif Player.sprite and Player.primary_Action.type == "anal" and Player.primary_Action.speed == 1:
        "Rogue_sex_spunk_anus_under_animation" pos (0.292, 0.386)
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anus_closed.png"

    if Player.sprite and Player.primary_Action.type == "sex" and Player.primary_Action.speed >= 2:
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif Player.sprite and Player.primary_Action.type == "sex" and Player.primary_Action.speed:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    elif Player.sprite and Player.primary_Action.type == "sex":
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"
    elif "dildo_pussy" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif Player.primary_Action in pussy_Action_types or Player.secondary_Action in pussy_Action_types:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"

    if not RogueX.grool:
        Null()
    elif Player.sprite and Player.primary_Action.type == "sex" and Player.primary_Action.speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_grool_fucking.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_grool.png"

    if not RogueX.pubes:
        Null()
    elif Player.sprite and Player.primary_Action.type == "sex" and Player.primary_Action.speed >= 2:
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif Player.sprite and Player.primary_Action.type == "sex" and Player.primary_Action.speed:
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    elif Player.sprite and Player.primary_Action.type == "sex":
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"
    elif "dildo_pussy" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_sex/Rogue_sex_pubes_fucking.png"
    elif Player.primary_Action in pussy_Action_types or Player.secondary_Action in pussy_Action_types:
        "images/Rogue_sex/Rogue_sex_pubes_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pubes_closed.png"

    if RogueX.spunk["pussy"]:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if Player.sprite and Player.primary_Action.type == "anal":
        AlphaMask("Zero_cock_Rogue", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "finger_ass" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("Zero_finger_Rogue", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "dildo_ass" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("dildo_Rogue", "images/Kitty_sex/Kitty_sex_anus_mask.png")

    if not RogueX.spunk["anus"]:
        Null()
    elif not Player.sprite or Player.primary_Action.type != "anal":
        Null()
    elif Player.primary_Action.speed == 1:
        "Rogue_sex_spunk_anus_over_animation" pos (0.292, 0.386)
    else:
        "Rogue_sex_spunk_anus_over" pos (0.292, 0.386)

    if Player.sprite and Player.primary_Action.type == "sex":
        AlphaMask("Zero_cock_Rogue", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif "finger_pussy" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("Zero_finger_Rogue", "images/Rogue_sex/Rogue_sex_pussy_mask.png")
    elif "dildo_pussy" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("dildo_Rogue", "images/Rogue_sex/Rogue_sex_pussy_mask.png")

    if not RogueX.spunk["pussy"]:
        Null()
    elif not Player.sprite or Player.primary_Action.type != "sex":
        Null()
    elif Player.primary_Action.speed <= 1:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png" offset (111, 0) xzoom 0.8
    else:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

    if RogueX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if Player.sprite and Player.primary_Action.type == "out":
        "Zero_cock_Rogue"

    if Player.primary_Action == "eat_pussy":
        "licking" pos (0.292, 0.474) zoom 0.35
    elif Player.primary_Action == "eat_ass":
        "licking" pos (0.292, 0.548) zoom 0.35

    if Player.sprite and RogueX.primary_Action.type == "footjob":
        "Zero_cock_Rogue"

    if RogueX.primary_Action.type == "footjob" or show_feet:
        "Rogue_sex_feet" pos (0.291, 0.391)
    else:
        AlphaMask("Rogue_sex_feet", "images/Rogue_sex/Rogue_sex_feet_mask.png")

    anchor (0.5, 0.5)

layeredimage Rogue_sex_feet:
    always:
        "images/Rogue_sex/Rogue_sex_feet.png"

    if RogueX.wet:
        "images/Rogue_sex/Rogue_sex_water_feet.png"

    anchor (0.5, 0.5)

image Rogue_sex_anus:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

image Rogue_sex_spunk_anus_under:
    "images/Kitty_sex/Kitty_sex_spunk_anus_under.png"

    anchor (0.5, 0.5)

image Rogue_sex_spunk_anus_over:
    "images/Kitty_sex/Kitty_sex_spunk_anus_over.png"

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_body:
    if RogueX.Clothes["hair"].string == "Evolutions_hair":
        "images/Rogue_doggy/Rogue_doggy_hair_back.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_body.png"

    if RogueX.spunk["mouth"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_mouth_[RogueX.mouth].png"
    else:
        "images/Rogue_doggy/Rogue_doggy_mouth_[RogueX.mouth].png"

    if RogueX.blushing:
        "images/Rogue_doggy/Rogue_doggy_blush.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_brows_[RogueX.brows].png"

    if RogueX.eyes == "closed":
        "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"
    else:
        "Rogue_doggy_blinking"

    if RogueX.spunk["face"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_face.png"

    if RogueX.spunk["hair"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_hair.png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_water_top.png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_hair_wet.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_hair_[RogueX.Clothes[hair].string].png"

    if "fondle_breasts" in [Player.primary_Action, Player.secondary_Action]:
        "Zero_doggy_fondle_breast_animation" pos (0.12, 0.32)

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_ass:
    always:
        "images/Rogue_doggy/Rogue_doggy_ass.png"

    if Player.primary_Action in pussy_Action_types or Player.secondary_Action in pussy_Action_types:
        "images/Rogue_doggy/Rogue_doggy_pussy_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_pussy_closed.png"

    if Player.sprite and Player.primary_Action.type == "sex":
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
    elif "finger_pussy" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"
    elif "dildo_pussy" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"

    if Player.sprite and Player.primary_Action.type == "sex":
        "Rogue_doggy_pussy_hole_animation[Player.primary_Action.speed]" pos (0.113, 0.475)
    elif "finger_pussy" in [Player.primary_Action, Player.secondary_Action]:
        "Rogue_doggy_pussy_hole_fingering" pos (0.113, 0.475)
    elif "dildo_pussy" in [Player.primary_Action, Player.secondary_Action]:
        "Rogue_doggy_pussy_hole_animation1" pos (0.113, 0.475)

    if RogueX.used_to_anal:
        "images/Rogue_doggy/Rogue_doggy_anus_loose.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_anus_tight.png"

    if Player.sprite and Player.primary_Action.type == "anal" and Player.primary_Action.speed:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"
    elif "finger_ass" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"
    elif "dildo_ass" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"

    if Player.sprite and Player.primary_Action.type == "anal" and Player.primary_Action.speed:
        "Rogue_doggy_anus_anal_animation[Player.primary_Action.speed]" pos (0.113, 0.475)
    elif "finger_ass" in [Player.primary_Action, Player.secondary_Action]:
        "Rogue_doggy_anus_fingering_animation" pos (0.113, 0.475)
    elif "dildo_ass" in [Player.primary_Action, Player.secondary_Action]:
        "Rogue_doggy_anus_anal_animation1" pos (0.113, 0.475)

    if Player.sprite and Player.primary_Action.type == "anal" and Player.primary_Action.speed > 1:
        "images/Rogue_doggy/Rogue_doggy_anus_full_cheeks.png"

    if not RogueX.spunk["anus"]:
        Null()
    elif Player.primary_Action.type == "anal" and Player.primary_Action.speed:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    elif "finger_ass" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    elif "dildo_ass" in [Player.primary_Action, Player.secondary_Action]:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_spunk_anus_loose.png"

    if RogueX.wet:
        "images/Rogue_doggy/Rogue_doggy_water_ass.png"

    if Player.sprite and Player.primary_Action.type == "sex":
        AlphaMask("Zero_cock_Rogue", "Zero_cock_Rogue_mask")
    elif "finger_pussy" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("Zero_finger_Rogue", "Zero_finger_Rogue_mask")
    elif "dildo_pussy" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("dildo_Rogue", "dildo_Rogue_mask")

    if Player.sprite and Player.primary_Action.type == "anal":
        AlphaMask("Zero_cock_Rogue", "Zero_cock_Rogue_mask")
    elif "finger_ass" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("Zero_finger_Rogue", "Zero_finger_Rogue_mask")
    elif "dildo_ass" in [Player.primary_Action, Player.secondary_Action]:
        AlphaMask("dildo_Rogue", "dildo_Rogue_mask")

    if RogueX.spunk["back"]:
        "images/Rogue_doggy/Rogue_doggy_spunk_ass.png"

    if Player.primary_Action == "eat_pussy":
        "licking" pos (0.112, 0.53) zoom 0.28
    elif Player.primary_Action == "eat_ass":
        "licking" pos (0.112, 0.48) zoom 0.28

    if not Player.sprite or Player.primary_Action.type != "out":
        Null()
    else:
        "images/Rogue_doggy/Rogue_doggy_hotdog_back.png"

    if not Player.sprite or Player.primary_Action.type != "out":
        Null()
    else:
        AlphaMask("Zero_cock_Rogue", "images/Rogue_doggy/Rogue_doggy_hotdog_mask.png")

    anchor (0.5, 0.5)

image Rogue_doggy_pussy_hole:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_hole:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"

    anchor (0.515, 0.69)

image Rogue_doggy_pussy_mask:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_mask:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    anchor (0.52, 0.69)

layeredimage Rogue_doggy_shins:
    always:
        "images/Rogue_doggy/Rogue_doggy_shins.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_feet.png"

    anchor (0.5, 0.5)

image Rogue_doggy_feet:
    AlphaMask("Rogue_doggy_shins", "images/Rogue_doggy/Rogue_doggy_toes.png")

    anchor (0.5, 0.5)
