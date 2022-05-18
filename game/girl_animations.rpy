layeredimage Rogue_sprite:
    if not renpy.showing("Rogue_TJ_Animation") and not renpy.showing("Rogue_blowjob_animation"):
        "Rogue_hairback" pos (0.2941, 0.1982) anchor (0.5, 0.5) offset (0, 0) zoom 0.2175

    always:
        "Rogue_body" pos (0.25, 0.5) anchor (0.5, 0.5) offset (0, 0) zoom 0.75

    always:
        "Rogue_head" pos (0.2941, 0.1982) anchor (0.5, 0.5) offset (0, 0) zoom 0.2175

layeredimage Rogue_body:
    if RogueX.top == "_hoodie":
        "images/Rogue/Rogue_top_standing[RogueX.top]_back.png"

    if not RogueX.top:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue/Rogue_top_standing[RogueX.top][RogueX.ArmPose]_up.png"
    else:
        "images/Rogue/Rogue_top_standing[RogueX.top][RogueX.ArmPose].png"

    always:
        "images/Rogue/Rogue_body_standing[RogueX.pubes][RogueX.piercings].png"

    if RogueX.hose == "_stockings":
        "images/Rogue/Rogue_hose_standing[RogueX.hose].png"
    elif RogueX.legs == "_pants" and RogueX.upskirt:
        "images/Rogue/Rogue_legs_standing[RogueX.legs]_back.png"

    if not RogueX.underwear:
        Null()
    elif RogueX.legs == "_pants" and not RogueX.upskirt:
        Null()
    elif RogueX.underwear_pulled_down and RogueX.grool > 1:
        "images/Rogue/Rogue_underwear_standing[RogueX.underwear]_down_wet.png"
    elif RogueX.underwear_pulled_down:
        "images/Rogue/Rogue_underwear_standing[RogueX.underwear]_down.png"
    elif RogueX.grool > 1:
        "images/Rogue/Rogue_underwear_standing[RogueX.underwear]_wet.png"
    elif RogueX.underwear:
        "images/Rogue/Rogue_underwear_standing[RogueX.underwear].png"

    if RogueX.underwear and RogueX.underwear_pulled_down:
        Null()
    elif RogueX.grool and RogueX.hose == "_tights":
        "images/Rogue/Rogue_hose_standing[RogueX.hose]_wet.png"
    elif RogueX.hose:
        "images/Rogue/Rogue_hose_standing[RogueX.hose].png"

    if not RogueX.grool:
        Null()
    elif RogueX.legs == "_pants" and not RogueX.upskirt:
        Null()
    elif RogueX.underwear and not RogueX.underwear_pulled_down and RogueX.grool < 2:
        Null()
    elif RogueX.grool == 1 and RogueX.underwear and RogueX.underwear_pulled_down:
        AlphaMask("grool_dripping", "images/Rogue/Rogue_drip_mask_standing_underwear.png")
    elif RogueX.grool == 1 and RogueX.legs == "_pants":
        AlphaMask("grool_dripping", "images/Rogue/Rogue_drip_mask_standing_pants.png")
    elif RogueX.grool == 1:
        AlphaMask("grool_dripping", "images/Rogue/Rogue_drip_mask_standing.png")
    elif RogueX.underwear and RogueX.underwear_pulled_down:
        AlphaMask("heavy_grool_dripping", "images/Rogue/Rogue_drip_mask_standing_underwear.png")
    elif RogueX.underwear and RogueX.legs == "_pants":
        AlphaMask("grool_dripping", "images/Rogue/Rogue_drip_mask_standing_pants.png")
    elif RogueX.legs == "_pants":
        AlphaMask("heavy_grool_dripping", "images/Rogue/Rogue_drip_mask_standing_pants.png")
    elif RogueX.underwear:
        AlphaMask("grool_dripping", "images/Rogue/Rogue_drip_mask_standing.png")
    else:
        AlphaMask("heavy_grool_dripping", "images/Rogue/Rogue_drip_mask_standing.png")

    if not RogueX.grool:
        Null()
    elif RogueX.legs and RogueX.grool < 2:
        Null()
    elif RogueX.legs or RogueX.grool == 1:
        "images/Rogue/Rogue_grool_standing.png"
    else:
        "images/Rogue/Rogue_grool_standing2.png"

    if "in" not in RogueX.spunk and "anal" not in RogueX.spunk:
        Null()
    elif RogueX.legs == "_pants" and not RogueX.upskirt:
        Null()
    elif RogueX.underwear and RogueX.underwear_pulled_down:
        AlphaMask("heavy_spunk_dripping", "images/Rogue/Rogue_drip_mask_standing_underwear.png")
    elif RogueX.underwear and RogueX.legs == "_pants":
        AlphaMask("spunk_dripping", "images/Rogue/Rogue_drip_mask_standing_pants.png")
    elif RogueX.legs == "_pants":
        AlphaMask("heavy_spunk_dripping", "images/Rogue/Rogue_drip_mask_standing_pants.png")
    else:
        AlphaMask("heavy_spunk_dripping", "images/Rogue/Rogue_drip_mask_standing.png")

    if RogueX.legs == "_skirt" and RogueX.upskirt:
        "images/Rogue/Rogue_legs_standing[RogueX.legs]_up.png"
    elif RogueX.legs:
        "images/Rogue/Rogue_legs_standing[RogueX.legs].png"

    always:
        "images/Rogue/Rogue_arms_standing[RogueX.neck][RogueX.arms][RogueX.ArmPose].png"

    always:
        "images/Rogue/Rogue_chest_standing[RogueX.piercings].png"

    if RogueX.bra and RogueX.top_pulled_up:
        "images/Rogue/Rogue_bra_standing[RogueX.bra]_up.png"
    elif RogueX.bra:
        "images/Rogue/Rogue_bra_standing[RogueX.bra].png"

    if RogueX.Water and RogueX.Water < 3:
        "images/Rogue/Rogue_body_standing_wet_overlay[RogueX.ArmPose].png"

    if RogueX.Water == 3:
        "images/Rogue/Rogue_body_standing_wet_overlay3.png"

    if not RogueX.top:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue/Rogue_top_standing[RogueX.top][RogueX.ArmPose]_up.png"
    else:
        "images/Rogue/Rogue_top_standing[RogueX.top][RogueX.ArmPose].png"

    if RogueX.accessory:
        "images/Rogue/Rogue_accessory_standing[RogueX.accessory][RogueX.ArmPose].png"

    if "hand" in RogueX.spunk and RogueX.ArmPose == 2:
        "images/Rogue/Rogue_spunk_standing_hand.png"

    if "belly" in RogueX.spunk:
        "images/Rogue/Rogue_spunk_standing_belly.png"

    if "tits" in RogueX.spunk:
        "images/Rogue/Rogue_spunk_standing_breasts.png"

    if RogueX.held_item and RogueX.ArmPose == 2:
        "images/Rogue/Rogue_held_item_standing[RogueX.held_item].png"

    if primary_action == "lesbian" or not girl_offhand_action or focused_Girl != RogueX:
        Null()
    elif primary_action != "sex" and girl_offhand_action == "fondle_pussy" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy"
    elif girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "GirlGropeLeftBreast"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast"

    if second_girl_primary_action != "masturbation" or not second_girl_offhand_action or focused_Girl == RogueX:
        Null()
    elif primary_action != "sex" and second_girl_offhand_action == "fondle_pussy" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif second_girl_offhand_action == "fondle_pussy":
        "GirlGropePussy"
    elif second_girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck breasts"]):
        "GirlGropeLeftBreast"
    elif second_girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast"

    if not primary_action or focused_Girl != RogueX:
        Null()
    elif primary_action == "fondle_thighs":
        "GropeThigh"
    elif primary_action == "fondle_breasts":
        "GropeRightBreast"
    elif primary_action == "suck_breasts":
        "LickRightBreast"
    elif primary_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy"
    elif primary_action == "fondle_pussy":
        "GropePussy"
    elif primary_action == "eat_pussy":
        "Lickpussy"

    if not offhand_action or focused_Girl != RogueX:
        Null()
    elif primary_action == "fondle_breasts" and not girl_offhand_action and not second_girl_primary_action and not second_girl_offhand_action:
        "GropeRightBreast"
    elif offhand_action == "fondle_thighs":
        "GropeThigh"
    elif offhand_action == "fondle_breasts":
        "GropeLeftBreast"
    elif offhand_action == "suck_breasts":
        "LickLeftBreast"
    elif offhand_action == "fondle_pussy" and action_speed == 2:
        "FingerPussy"
    elif offhand_action == "fondle_pussy":
        "GropePussy"
    elif offhand_action == "eat_pussy":
        "Lickpussy"

    if not second_girl_primary_action or focused_Girl != RogueX:
        Null()
    elif second_girl_primary_action == "fondle_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "GirlGropeLeftBreast"
    elif second_girl_priamry_action == "fondle_breasts":
        "GirlGropeRightBreast"
    elif second_girl_primary_action == "suck_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast"
    elif second_girl_primary_action == "suck_breasts" and (offhand_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast"
    elif second_girl_priamry_action == "suck_breasts":
        "LickRightBreast"
    elif second_girl_primary_action == "fondle_pussy" and primary_action != "sex" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif second_girl_primary_action == "fondle_pussy" and offhand_action != "sex" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif second_girl_primary_action == "fondle_pussy":
        "GropePussy"
    elif second_girl_primary_action == "eat_pussy":
        "Lickpussy"

    if primary_action != "lesbian" or not girl_offhand_action or focused_Girl == RogueX:
        Null()
    elif girl_offhand_action == "fondle_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "GirlGropeLeftBreast"
    elif girl_offhand_action == "fondle_breasts" and (offhand_action in ["fondle_breasts", "suck_breasts"]):
        "GirlGropeLeftBreast"
    elif girl_offhand_action == "fondle_breasts":
        "GirlGropeRightBreast"
    elif girl_offhand_action == "suck_breasts" and (primary_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast"
    elif girl_offhand_action == "suck_breasts" and (offhand_action in ["fondle_breasts", "suck_breasts"]):
        "LickLeftBreast"
    elif girl_offhand_action == "suck_breasts":
        "LickRightBreast"
    elif girl_offhand_action == "fondle_pussy" and primary_action != "sex" and RogueX.lust >= 70:
        "GirlFingerPussy"
    elif girl_offhand_action == "fondle_pussy":
        "GirlGropePussy"
    elif girl_offhand_action == "eat_pussy":
        "Lickpussy"

    # always:
    #     "Rogue_head" pos (185, 38) zoom 0.29

layeredimage Rogue_hairback:
    always:
        "images/Rogue/Rogue_hairback_standing[RogueX.hair].png"

transform Rogue_blowjob_mouth_animation:
    subpixel True
    zoom 0.90

    block:
        pause 0.10
        easeout 0.55 zoom 0.9
        linear 0.10 zoom 0.87
        easein 0.30 zoom 0.9
        pause 0.15
        easeout 0.40 zoom 0.87
        linear 0.10 zoom 0.9
        easein 0.45 zoom 0.70
        pause 0.35
        repeat

layeredimage Rogue_head:
    if not action_speed or not renpy.showing("Rogue_blowjob_animation"):
        "images/Rogue/Rogue_face_standing[RogueX.blushing].png"
    else:
        "images/Rogue/Rogue_face_blowjob[RogueX.blushing].png"

    if renpy.showing("Rogue_blowjob_animation") and action_speed == 1:
        "images/Rogue/Rogue_mouth_blowjob_tongue.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed >= 3:
        "images/Rogue/Rogue_mouth_blowjob_sucking.png"
    elif not action_speed:
        "images/Rogue/Rogue_mouth_standing[RogueX.mouth].png"

    if "chin" in RogueX.spunk:
        "images/Rogue/Rogue_spunk_standing_chin.png"

    if "mouth" not in RogueX.spunk:
        Null()
    elif renpy.showing("Rogue_blowjob_animation") and action_speed == 2:
        Null()
    elif renpy.showing("Rogue_blowjob_animation") and action_speed == 1:
        "images/Rogue/Rogue_spunk_blowjob_tongue.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed:
        "images/Rogue/Rogue_spunk_blowjob_sucking.png"
    else:
        "images/Rogue/Rogue_spunk_standing[RogueX.mouth].png"

    if renpy.showing("Rogue_blowjob_animation") and action_speed == 2 and "mouth" in RogueX.spunk:
        At("images/Rogue/Rogue_mouth_blowjob_sucking_spunk.png", Rogue_blowjob_mouth_animation) anchor (0.4, 0.65) pos (316, 590)
    elif renpy.showing("Rogue_blowjob_animation") and action_speed == 2:
        At("images/Rogue/Rogue_mouth_blowjob_sucking.png", Rogue_blowjob_mouth_animation) anchor (0.4, 0.65) pos (316, 590)

    if RogueX.blushing:
        "images/Rogue/Rogue_brows_standing[RogueX.brows]_blush.png"
    else:
        "images/Rogue/Rogue_brows_standing[RogueX.brows].png"

    if RogueX.eyes != "_closed":
        "Rogue_blinking"
    else:
        "images/Rogue/Rogue_eyes_standing_closed.png"

    if primary_action == "blowjob" and "mouth" in RogueX.spunk and action_speed >= 3:
        "images/Rogue/Rogue_face_blowjob_sucking_cum_over.png"

    always:
        "images/Rogue/Rogue_hair_standing[RogueX.hair].png"

    if RogueX.Water:
        "images/Rogue/Rogue_face_standing_wet_overlay.png"

    if "hair" in RogueX.spunk:
        "images/Rogue/Rogue_spunk_standing_hair.png"
    elif "facial" in RogueX.spunk:
        "images/Rogue/Rogue_spunk_standing_facial.png"

layeredimage Rogue_eyes:
    always:
        "images/Rogue/Rogue_eyes_standing[RogueX.eyes].png"

image Rogue_blinking:
    "Rogue_eyes"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue/Rogue_eyes_standing_squint.png"
    0.05
    "images/Rogue/Rogue_eyes_standing_closed.png"
    0.15
    "images/Rogue/Rogue_eyes_standing_squint.png"
    0.05
    repeat

image Rogue_squinting:
    "images/Rogue/Rogue_eyes_standing_sexy.png",
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue/Rogue_eyes_standing_squint.png",
    0.25
    repeat





transform Rogue_BJ_Starting:
    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_Cock_BJ_Starting:
    anchor (.5,.5)
    rotate -10

transform Rogue_BJ_StartingBody:
    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_Cock_BJ_Licking:
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause .5
        ease 2.5 rotate 0
        repeat

transform Rogue_Cock_BJ_Straight:
    anchor (.5,.5)
    rotate 0

transform Rogue_BJ_Licking:
    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (25,100)
        ease 2 offset (0,-35)
        pause .5
        repeat

transform Rogue_BJ_LickingBody:
    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (30,90)
        ease 2 offset (0,-35)
        pause .5
        repeat

transform Rogue_BJ_Heading:
    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 35
        ease 1.5 offset (0,-40)
        repeat

transform Rogue_BJ_HeadingBody:
    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat

transform Rogue_BJ_Sucking:
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120
        ease 1.5 offset (0,50)
        repeat

transform Rogue_BJ_SuckingBody:
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100
        ease 1.5 offset (0,50)
        repeat

transform Rogue_BJ_Deep:
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat

transform Rogue_BJ_DeepBody:
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

layeredimage Rogue_blowjob_animation:
    if action_speed == 0:
        At("Rogue_BJ_HairBack", Rogue_BJ_Starting) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 1:
        At("Rogue_BJ_HairBack", Rogue_BJ_Licking) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 2:
        At("Rogue_BJ_HairBack", Rogue_BJ_Heading) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 3:
        At("Rogue_BJ_HairBack", Rogue_BJ_Sucking) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 4:
        At("Rogue_BJ_HairBack", Rogue_BJ_Deep) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928

    if action_speed == 0:
        At("Rogue_body", Rogue_BJ_StartingBody) pos (0.37, 0.925) anchor (0.5, 0.0) offset (0, 0) zoom 3.2
    elif action_speed == 1:
        At("Rogue_body", Rogue_BJ_LickingBody) pos (0.37, 0.925) anchor (0.5, 0.0) offset (0, 0) zoom 3.2
    elif action_speed == 2:
        At("Rogue_body", Rogue_BJ_HeadingBody) pos (0.37, 0.925) anchor (0.5, 0.0) offset (0, 0) zoom 3.2
    elif action_speed == 3:
        At("Rogue_body", Rogue_BJ_SuckingBody) pos (0.37, 0.925) anchor (0.5, 0.0) offset (0, 0) zoom 3.2
    elif action_speed == 4:
        At("Rogue_body", Rogue_BJ_DeepBody) pos (0.37, 0.925) anchor (0.5, 0.0) offset (0, 0) zoom 3.2

    if action_speed == 0:
        At("Rogue_head", Rogue_BJ_Starting) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 1:
        At("Rogue_head", Rogue_BJ_Licking) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 2:
        At("Rogue_head", Rogue_BJ_Heading) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 3:
        At("Rogue_head", Rogue_BJ_Sucking) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928
    elif action_speed == 4:
        At("Rogue_head", Rogue_BJ_Deep) pos (0.555, 1.07) anchor (0.5, 0.0) offset (0, 0) zoom 0.928

    if action_speed == 0:
        At("Zero_cock_blowjob", Rogue_Cock_BJ_Starting) pos (0.5, 0.9) anchor (0.5, -0.4) offset (0, 200)
    elif action_speed == 1:
        At("Zero_cock_blowjob", Rogue_Cock_BJ_Licking) pos (0.5, 0.9) anchor (0.5, -0.4) offset (0, 200)
    elif action_speed == 2:
        At("Zero_cock_blowjob", Rogue_Cock_BJ_Straight) pos (0.5, 0.9) anchor (0.5, -0.4) offset (0, 200)
    elif action_speed == 3:
        At("Zero_cock_blowjob", Rogue_Cock_BJ_Straight) pos (0.5, 0.9) anchor (0.5, -0.4) offset (0, 200)
    elif action_speed == 4:
        At("Zero_cock_blowjob", Rogue_Cock_BJ_Straight) pos (0.5, 0.9) anchor (0.5, -0.4) offset (0, 200)

    pos (0.5, 0.5) anchor (0.4, 0.30) offset (0, 0) zoom 0.55
