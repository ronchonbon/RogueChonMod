layeredimage Kitty_sprite standing:
    if KittyX.Outfit.Clothes["skirt"].string == "Aerith_skirt":
        "images/Kitty_standing/Kitty_standing_skirt_[KittyX.Outfit.Clothes[skirt].string]_back.png"

    always:
        "Kitty_hair_back" pos (0.24, 0.3) zoom 0.5

    always:
        "images/Kitty_standing/Kitty_standing_arms[KittyX.arm_pose].png"

    always:
        "images/Kitty_standing/Kitty_standing_body[KittyX.arm_pose][KittyX.pubes].png"

    always:
        "images/Kitty_standing/Kitty_standing_breasts.png"

    if KittyX.Outfit.Clothes["body_piercings"]:
        "images/Kitty_standing/Kitty_standing_body_piercings_breasts_[KittyX.Outfit.Clothes[body_piercings].string].png"

    if KittyX.Outfit.Clothes["body_piercings"]:
        "images/Kitty_standing/Kitty_standing_body_piercings_pussy_[KittyX.Outfit.Clothes[body_piercings].string].png"

    if not KittyX.Outfit.Clothes["underwear"]:
        Null()
    elif KittyX.grool > 1:
        "images/Kitty_standing/Kitty_standing_underwear_[KittyX.Outfit.Clothes[underwear].string]_grool_[KittyX.Outfit.Clothes[underwear].state].png"
    else:
        "images/Kitty_standing/Kitty_standing_underwear_[KittyX.Outfit.Clothes[underwear].string]_[KittyX.Outfit.Clothes[underwear].state].png"

    if KittyX.Outfit.Clothes["hose"]:
        "images/Kitty_standing/Kitty_standing_hose_[KittyX.Outfit.Clothes[hose].string].png"

    if KittyX.grool and not KittyX.Outfit.pussy_covered:
        "images/Kitty_standing/Kitty_standing_grool[KittyX.grool].png"

    always:
        "Kitty_grool_animations"

    if KittyX.spunk["pussy"]:
        "images/Kitty_standing/Kitty_standing_spunk_anus.png"

    if KittyX.spunk["anus"]:
        "images/Kitty_standing/Kitty_standing_spunk_pussy.png"

    always:
        "Kitty_spunk_animations"

    if KittyX.Outfit.Clothes["bra"]:
        "images/Kitty_standing/Kitty_standing_bra[KittyX.arm_pose]_[KittyX.Outfit.Clothes[bra].string]_[KittyX.Outfit.Clothes[bra].state].png"

    if KittyX.Outfit.Clothes["neck"]:
        "images/Kitty_standing/Kitty_standing_neck_[KittyX.Outfit.Clothes[neck].string].png"

    if not KittyX.Outfit.Clothes["pants"]:
        Null()
    elif KittyX.grool > 1 and KittyX.Outfit.Clothes["pants"].string == "yellow_shorts":
        "images/Kitty_standing/Kitty_standing_pants_[KittyX.Outfit.Clothes[pants].string]_grool.png"
    else:
        "images/Kitty_standing/Kitty_standing_pants_[KittyX.Outfit.Clothes[pants].string].png"

    if KittyX.Outfit.Clothes["skirt"]:
        "images/Kitty_standing/Kitty_standing_skirt_[KittyX.Outfit.Clothes[skirt].string]_[KittyX.Outfit.Clothes[skirt].state].png"

    if KittyX.Outfit.Clothes["top"]:
        "images/Kitty_standing/Kitty_standing_top[KittyX.arm_pose]_[KittyX.Outfit.Clothes[top].string]_[KittyX.Outfit.Clothes[top].state].png"

    if KittyX.Outfit.Clothes["body_piercings"] and KittyX.Outfit.breasts_covered:
        "images/Kitty_standing/Kitty_standing_body_piercings_breasts_[KittyX.Outfit.Clothes[body_piercings].string]_covered.png"

    if KittyX.Outfit.Clothes["jacket"]:
        "images/Kitty_standing/Kitty_standing_jacket[KittyX.arm_pose]_[KittyX.Outfit.Clothes[jacket].string]_[KittyX.Outfit.Clothes[jacket].state].png"

    always:
        "Kitty_head" pos (0.24, 0.3) zoom 0.5

    if KittyX.spunk["breasts"]:
        "images/Kitty_standing/Kitty_standing_spunk_breasts.png"

    if KittyX.spunk["belly"]:
        "images/Kitty_standing/Kitty_standing_spunk_belly.png"

    if KittyX.spunk["hand"] and KittyX.arm_pose == 2:
        "images/Kitty_standing/Kitty_standing_spunk_hand.png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_water_body[KittyX.arm_pose].png"

    if KittyX.held_item and KittyX.arm_pose == 2:
        "images/Kitty_standing/Kitty_standing_held_item_[KittyX.held_item].png"

    always:
        "Kitty_standing_fondling_animations" pos (-0.002, -0.035) zoom 1.03

    anchor (0.5, 0.0) offset (40, 175) zoom 0.485

layeredimage Kitty_hair_back:
    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_hair_wet_hair_back.png"
    elif KittyX.Outfit.Clothes["hair"].string != "Evolutions_hair":
        "images/Kitty_standing/Kitty_standing_hair_[KittyX.Outfit.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Kitty_head:
    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_face_wet_hair_[KittyX.blushing].png"
    else:
        "images/Kitty_standing/Kitty_standing_face_[KittyX.Outfit.Clothes[hair].string][KittyX.blushing].png"

    always:
        "images/Kitty_standing/Kitty_standing_brows_[KittyX.brows].png"

    always:
        "images/Kitty_standing/Kitty_standing_mouth_[KittyX.mouth].png"

    if KittyX.eyes == "closed":
        "images/Kitty_standing/Kitty_standing_eyes_closed.png"
    else:
        "Kitty_blinking"

    if KittyX.spunk["mouth"]:
        "images/Kitty_standing/Kitty_standing_spunk_mouth_[KittyX.mouth].png"

    if KittyX.spunk["face"]:
        "images/Kitty_standing/Kitty_standing_spunk_face.png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_hair_wet_hair.png"
    else:
        "images/Kitty_standing/Kitty_standing_hair_[KittyX.Outfit.Clothes[hair].string].png"

    if KittyX.spunk["hair"]:
        "images/Kitty_standing/Kitty_standing_spunk_hair.png"

    if KittyX.wet:
        "images/Kitty_standing/Kitty_standing_water_head.png"

    anchor (0.5, 0.5)

image Kitty_handjob_under:
    "images/Kitty_handjob/Kitty_handjob_hand_under.png"

    anchor (0.5, 0.5)

image Kitty_handjob_over:
    "images/Kitty_handjob/Kitty_handjob_hand_over.png"

    anchor (0.5, 0.5)

layeredimage Kitty_titjob_hair_back:
    if KittyX.wet or KittyX.Outfit.Clothes["hair"].string == "wet_hair":
        "images/Kitty_blowjob/Kitty_blowjob_hair_back.png"

    anchor (0.5, 0.5)

image Kitty_titjob_body:
    "images/Kitty_titjob/Kitty_titjob_body.png"

    anchor (0.5, 0.5)

image Kitty_titjob_arms:
    "images/Kitty_titjob/Kitty_titjob_arms.png"

    anchor (0.5, 0.5)

layeredimage Kitty_titjob_breasts:
    if action_speed:
        "images/Kitty_titjob/Kitty_titjob_breasts_smooshed.png"
    else:
        "images/Kitty_titjob/Kitty_titjob_breasts.png"

    anchor (0.5, 0.5)

image Kitty_titjob_mask:
    "images/Kitty_titjob/Kitty_titjob_mask.png"

    anchor (0.5, 0.5)

layeredimage Kitty_blowjob_head:
    if KittyX.wet or KittyX.Outfit.Clothes["hair"].string == "wet_hair":
        "images/Kitty_blowjob/Kitty_blowjob_hair_back.png"

    if not renpy.showing("Kitty_sprite blowjob"):
        Null()
    elif action_speed > 1 and (KittyX.wet or KittyX.Outfit.Clothes["hair"].string == "wet_hair") and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet_blush.png"
    elif action_speed > 1 and (KittyX.wet or KittyX.Outfit.Clothes["hair"].string == "wet_hair"):
        "images/Kitty_blowjob/Kitty_blowjob_face_open_wet.png"
    elif action_speed > 1 and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_open_blush.png"
    elif action_speed > 1:
        "images/Kitty_blowjob/Kitty_blowjob_face_open.png"

    if renpy.showing("Kitty_sprite blowjob") and action_speed > 1:
        Null()
    elif (KittyX.wet or KittyX.Outfit.Clothes["hair"].string == "wet_hair") and KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet_blush.png"
    elif (KittyX.wet or KittyX.Outfit.Clothes["hair"].string == "wet_hair"):
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_wet.png"
    elif KittyX.blushing:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed_blush.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_face_closed.png"

    if renpy.showing("Kitty_sprite titjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 1:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 2:
        "Kitty_blowjob_mouth_animation[action_speed]" pos (0.225, 0.555)
    elif renpy.showing("Kitty_sprite blowjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_sucking.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_[KittyX.mouth].png"

    if not KittyX.spunk["mouth"]:
        Null()
    elif renpy.showing("Kitty_sprite titjob") and action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed == 1:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Kitty_sprite blowjob") and action_speed > 1:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"
    elif KittyX.mouth == "sucking":
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_[KittyX.mouth].png"

    always:
        "images/Kitty_blowjob/Kitty_blowjob_brows_[KittyX.brows].png"

    if KittyX.eyes == "closed":
        "images/Kitty_blowjob/Kitty_blowjob_eyes_closed.png"
    else:
        "Kitty_blowjob_blinking"

    if KittyX.spunk["face"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_face.png"

    if KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_hair_wet_hair.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_hair_[KittyX.Outfit.Clothes[hair].string].png"

    if KittyX.spunk["hair"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_hair.png"

    if not (KittyX.wet or KittyX.Outfit.Clothes["hair"].string == "wet_hair"):
        Null()
    elif action_speed > 2:
        "images/Kitty_blowjob/Kitty_blowjob_head_open_wet.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_head_closed_wet.png"

    anchor (0.5, 0.5)

layeredimage Kitty_blowjob_mouth:
    if KittyX.spunk["mouth"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"
    else:
        "images/Kitty_blowjob/Kitty_blowjob_mouth_sucking.png"

    anchor (0.5, 0.65)

layeredimage Kitty_blowjob_mask:
    always:
        "images/Kitty_blowjob/Kitty_blowjob_face_mask.png"

    if KittyX.spunk["mouth"] and action_speed == 2:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_under.png"

    anchor (0.5, 0.5) pos (0.5, 0.5)

image Kitty_blowjob_spunk_mouth_over:
    "images/Kitty_blowjob/Kitty_blowjob_spunk_mouth_sucking_over.png"

    anchor (0.5, 0.5)

layeredimage Kitty_blowjob_body:
    # if "blanket" in KittyX.recent_history:
    #     "images/Kitty_blowjob/Kitty_blowjob_blanket.png"

    always:
        "images/Kitty_blowjob/Kitty_blowjob_body.png"

    if KittyX.spunk["breasts"]:
        "images/Kitty_blowjob/Kitty_blowjob_spunk_body.png"

    if KittyX.wet:
        "images/Kitty_blowjob/Kitty_blowjob_water_body.png"

    anchor (0.5, 0.5)

layeredimage Kitty_sex_body:
    always:
        "Kitty_hair_back" pos (0.28, -0.065) rotate -10 zoom 0.75

    if KittyX.Outfit.Clothes["body_piercings"]:
        "images/Kitty_sex/Kitty_sex_body_[KittyX.Outfit.Clothes[body_piercings].string].png"
    else:
        "images/Kitty_sex/Kitty_sex_body.png"

    if KittyX.spunk["breasts"]:
        "images/Kitty_sex/Kitty_sex_spunk_breasts.png"

    if KittyX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_body.png"

    if "suck_breasts" in [Player.primary_action, Player.secondary_action]:
        "licking" pos (0.245, 0.22) zoom 0.33

    if "fondle_breasts" in [Player.primary_action, Player.secondary_action]:
        "Zero_fondle_breasts_left_animation" pos (0.245, 0.25) zoom 0.61

    always:
        "Kitty_head" pos (0.28, -0.065) rotate -10 zoom 0.375

    anchor (0.5, 0.5)

layeredimage Kitty_sex_legs:
    always:
        "images/Kitty_sex/Kitty_sex_legs.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_legs.png"

    if Player.sprite and Player.cock_position == "anal":
        "Kitty_sex_anus_animation[action_speed]" pos (0.292, 0.386)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_sex_anus" pos (0.292, 0.386) xzoom 0.6
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_sex_anus" pos (0.292, 0.386) xzoom 0.9
    elif KittyX.used_to_anal:
        "images/Kitty_sex/Kitty_sex_anus_loose.png"
    else:
        "images/Kitty_sex/Kitty_sex_anus_tight.png"

    if not KittyX.spunk["anus"]:
        Null()
    elif Player.sprite and Player.cock_position == "anal" and action_speed > 1:
        "Kitty_sex_spunk_anus_under" pos (0.292, 0.386)
    elif Player.sprite and Player.cock_position == "anal" and action_speed == 1:
        "Kitty_sex_spunk_anus_under_animation" pos (0.292, 0.386)
    else:
        "images/Kitty_sex/Kitty_sex_spunk_anus_closed.png"

    if Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_sex/Kitty_sex_pussy_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_sex/Kitty_sex_pussy_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_closed.png"

    if not KittyX.grool:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pussy_grool_fucking.png"
    else:
        "images/Kitty_sex/Kitty_sex_pussy_grool.png"

    if not KittyX.pubes:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_sex/Kitty_sex_pubes_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_sex/Kitty_sex_pubes_open.png"
    else:
        "images/Kitty_sex/Kitty_sex_pubes_closed.png"

    if KittyX.spunk["pussy"]:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_under.png"

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_cock_Kitty", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "images/Kitty_sex/Kitty_sex_anus_mask.png")
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Kitty", "images/Kitty_sex/Kitty_sex_anus_mask.png")

    if not KittyX.spunk["anus"]:
        Null()
    elif not Player.sprite or Player.cock_position != "anal":
        Null()
    elif action_speed == 1:
        "Kitty_sex_spunk_anus_over_animation" pos (0.292, 0.386)
    else:
        "Kitty_sex_spunk_anus_over" pos (0.292, 0.386)

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_cock_Kitty", "images/Kitty_sex/Kitty_sex_pussy_mask.png")
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "images/Kitty_sex/Kitty_sex_pussy_mask.png")
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Kitty", "images/Kitty_sex/Kitty_sex_pussy_mask.png")

    if not KittyX.spunk["pussy"]:
        Null()
    elif not Player.sprite or Player.cock_position != "in":
        Null()
    elif action_speed <= 1:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png" offset (111, 0) xzoom 0.8
    else:
        "images/Kitty_sex/Kitty_sex_spunk_pussy_over.png"

    if KittyX.spunk["belly"]:
        "images/Kitty_sex/Kitty_sex_spunk_belly_legs.png"

    if Player.sprite and Player.cock_position == "out":
        "Zero_cock_Kitty"

    if Player.primary_action == "eat_pussy":
        "licking" pos (0.292, 0.474) zoom 0.39
    elif Player.primary_action == "eat_ass":
        "licking" pos (0.292, 0.548) zoom 0.39

    if Player.sprite and Player.cock_position == "footjob":
        "Zero_cock_Kitty"

    if Player.cock_position == "footjob" or show_feet:
        "Kitty_sex_feet" pos (0.291, 0.391)
    else:
        AlphaMask("Kitty_sex_feet", "images/Kitty_sex/Kitty_sex_feet_mask.png")

    anchor (0.5, 0.5)

layeredimage Kitty_sex_feet:
    always:
        "images/Kitty_sex/Kitty_sex_feet.png"

    if KittyX.wet:
        "images/Kitty_sex/Kitty_sex_water_feet.png"

    anchor (0.5, 0.5)

image Kitty_sex_anus:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

image Kitty_sex_spunk_anus_under:
    "images/Kitty_sex/Kitty_sex_spunk_anus_under.png"

    anchor (0.5, 0.5)

image Kitty_sex_spunk_anus_over:
    "images/Kitty_sex/Kitty_sex_spunk_anus_over.png"

    anchor (0.5, 0.5)

layeredimage Kitty_doggy_body:
    # always:
    #     "images/Kitty_doggy/Kitty_doggy_head_reference.png"

    always:
        "Kitty_doggy_head" pos (0.095, 0.265) zoom 0.8

    always:
        "images/Kitty_doggy/Kitty_doggy_body.png"

    if KittyX.spunk["back"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_back.png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_water_body.png"

    if "fondle_breasts" in [Player.primary_action, Player.secondary_action]:
        "Zero_doggy_fondle_breast_animation" pos (0.1, 0.36)

    anchor (0.5, 0.5)

layeredimage Kitty_doggy_head:
    if KittyX.blushing:
        "images/Kitty_doggy/Kitty_doggy_head_blush.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_head.png"

    always:
        "images/Kitty_doggy/Kitty_doggy_mouth_[KittyX.mouth].png"

    if KittyX.spunk["mouth"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_mouth_[KittyX.mouth].png"

    always:
        "images/Kitty_doggy/Kitty_doggy_brows_[KittyX.brows].png"

    if KittyX.eyes == "closed":
        "images/Kitty_doggy/Kitty_doggy_eyes_closed.png"
    else:
        "Kitty_doggy_blinking"

    if KittyX.spunk["face"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_face.png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_hair_wet.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_hair_[KittyX.Outfit.Clothes[hair].string].png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_water_hair.png"

    if KittyX.spunk["hair"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_hair.png"

    anchor (0.5, 0.5)

layeredimage Kitty_doggy_ass:
    always:
        "images/Kitty_doggy/Kitty_doggy_ass.png"

    if KittyX.wet:
        "images/Kitty_doggy/Kitty_doggy_water_ass.png"

    if Player.primary_action == "eat_pussy":
        "images/Kitty_doggy/Kitty_doggy_pussy_open.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_pussy_closed.png"

    if Player.sprite and Player.cock_position == "in":
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_pussy_base.png"

    if Player.sprite and Player.cock_position == "in":
        "Kitty_doggy_pussy_hole_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_pussy_fingering_animation" pos (0.113, 0.475)
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_pussy_hole_animation1" pos (0.113, 0.475)

    if KittyX.spunk["pussy"] and Player.cock_position != "in":
        "images/Jean_doggy/Jean_doggy_spunk_pussy_closed.png"

    if not KittyX.grool:
        Null()
    elif Player.cock_position == "in":
        "images/Rogue_doggy/Rogue_doggy_grool_open.png"
    else:
        "images/Rogue_doggy/Rogue_doggy_grool_closed.png"

    if not KittyX.pubes:
        Null()
    elif Player.sprite and Player.cock_position == "in" and action_speed >= 2:
        "images/Kitty_doggy/Kitty_doggy_pubes_fucking.png"
    elif Player.sprite and Player.cock_position == "in" and action_speed:
        "images/Kitty_doggy/Kitty_doggy_pubes_open.png"
    elif Player.sprite and Player.cock_position == "in":
        "images/Kitty_doggy/Kitty_doggy_pubes.png"
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_pubes_fucking.png"
    elif Player.primary_action in pussy_actions or Player.secondary_action in pussy_actions:
        "images/Kitty_doggy/Kitty_doggy_pubes_open.png"
    else:
        "images/Kitty_doggy/Kitty_doggy_pubes.png"

    if KittyX.used_to_anal:
        "images/Jean_doggy/Jean_doggy_anus_loose.png"
    else:
        "images/Jean_doggy/Jean_doggy_anus_tight.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Kitty_doggy/Kitty_doggy_anus_full_base.png"

    if Player.sprite and Player.cock_position == "anal" and action_speed:
        "Kitty_doggy_anus_anal_animation[action_speed]" pos (0.113, 0.475)
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_anus_fingering_animation" pos (0.113, 0.475)
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "Kitty_doggy_anus_anal_animation1" pos (0.113, 0.475)

    if not KittyX.spunk["anus"]:
        Null()
    elif Player.cock_position == "anal" and action_speed:
        "images/Jean_doggy/Jean_doggy_spunk_anus_open.png"
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Jean_doggy/Jean_doggy_spunk_anus_open.png"
    elif "dildo_ass" in [Player.primary_action, Player.secondary_action]:
        "images/Jean_doggy/Jean_doggy_spunk_anus_open.png"
    else:
        "images/Jean_doggy/Jean_doggy_spunk_anus_loose.png"

    if Player.sprite and Player.cock_position == "in":
        AlphaMask("Zero_cock_Kitty", "Zero_cock_Kitty_mask")
    elif "finger_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "Zero_finger_Kitty_mask")
    elif "dildo_pussy" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("dildo_Kitty", "dildo_Kitty_mask")

    if Player.sprite and Player.cock_position == "anal":
        AlphaMask("Zero_cock_Kitty", "Zero_cock_Kitty_mask")
    elif "finger_ass" in [Player.primary_action, Player.secondary_action]:
        AlphaMask("Zero_finger_Kitty", "Zero_finger_Kitty_mask")
    elif Player.primary_action == "dildo_ass":
        AlphaMask("dildo_Kitty", "dildo_Kitty_mask")

    if KittyX.spunk["back"]:
        "images/Kitty_doggy/Kitty_doggy_spunk_back.png"

    if Player.primary_action == "eat_pussy":
        "licking" pos (0.112, 0.53) zoom 0.28
    elif Player.primary_action == "eat_ass":
        "licking" pos (0.112, 0.48) zoom 0.28

    if Player.sprite and Player.cock_position == "out":
        "images/Kitty_doggy/Kitty_doggy_hotdog_back.png"

    if Player.sprite and Player.cock_position == "out":
        AlphaMask("Zero_cock_Kitty", "images/Rogue_doggy/Rogue_doggy_hotdog_mask.png")

    anchor (0.5, 0.5)

image Kitty_doggy_pussy_hole:
    "images/Kitty_doggy/Kitty_doggy_pussy_hole.png"

    anchor (0.52, 0.69)

image Kitty_doggy_anus_hole:
    "images/Kitty_doggy/Kitty_doggy_anus_full_hole.png"

    anchor (0.52, 0.69)

image Kitty_doggy_pussy_mask:
    "images/Rogue_doggy/Rogue_doggy_sex_mask.png"

    anchor (0.52, 0.69)

image Kitty_doggy_anus_mask:
    "images/Rogue_doggy/Rogue_doggy_anus_mask.png"

    anchor (0.52, 0.69)

layeredimage Kitty_doggy_shins:
    always:
        "images/Kitty_doggy/Kitty_doggy_shins.png"

    always:
        "images/Kitty_doggy/Kitty_doggy_feet.png"

    anchor (0.5, 0.5)

image Kitty_doggy_feet:
    AlphaMask("Kitty_doggy_shins", "images/Kitty_doggy/Kitty_doggy_feet_mask.png")

    anchor (0.5, 0.5)
