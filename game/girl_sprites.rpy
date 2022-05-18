layeredimage Rogue_sprite:
    if not renpy.showing("Rogue_blowjob_animation") and not renpy.showing("Rogue_TJ_Animation"):
        "Rogue_hairback" pos (185, 38)

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

    if not renpy.showing("Rogue_blowjob_animation") and not renpy.showing("Rogue_TJ_Animation"):
        "Rogue_head" pos (185, 38)

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

    size (480, 960) anchor (0.6, 0.0) zoom 0.75

layeredimage Rogue_hairback:
    always:
        "images/Rogue/Rogue_hairback_standing[RogueX.hair].png"

    size (787, 913) zoom 0.29

layeredimage Rogue_head:
    if not action_speed or not renpy.showing("Rogue_blowjob_animation"):
        "images/Rogue/Rogue_face_standing[RogueX.blushing].png"
    else:
        "images/Rogue/Rogue_face_blowjob[RogueX.blushing].png"

    if renpy.showing("Rogue_blowjob_animation") and action_speed == 1:
        "images/Rogue/Rogue_mouth_blowjob_tongue.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed >= 3:
        "images/Rogue/Rogue_mouth_blowjob_sucking.png"
    elif renpy.showing("Rogue_blowjob_animation") and action_speed:
        Null()
    else:
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
        "Rogue_mouth_blowjob_sucking_spunk" anchor (0.4, 0.65) pos (316, 590)
    elif renpy.showing("Rogue_blowjob_animation") and action_speed == 2:
        "Rogue_mouth_blowjob_sucking" anchor (0.4, 0.65) pos (316, 590)

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

    size (787, 913) zoom 0.29

layeredimage Rogue_eyes:
    always:
        "images/Rogue/Rogue_eyes_standing[RogueX.eyes].png"

layeredimage Rogue_sex_body:
    always:
        "Rogue_hairback_Sex" pos (0.48, 0.1)

    always:
        "images/Rogue_sex/Rogue_body_sex[RogueX.piercings].png"

    if not RogueX.bra:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue_sex/Rogue_bra_sex[RogueX.bra]_up.png"
    else:
        "images/Rogue_sex/Rogue_bra_sex[RogueX.bra].png"

    if RogueX.Water:
        "images/RogueSex/Rogue_Sex_Wet_Body.png"

    if not RogueX.top:
        Null()
    elif RogueX.top_pulled_up:
        "images/Rogue_sex/Rogue_top_sex[RogueX.top]_up.png"
    else:
        "images/Rogue_sex/Rogue_top_sex[RogueX.top].png"

    if RogueX.top_pulled_up or (not RogueX.top and not RogueX.bra):
        Null()
    elif RogueX.piercings:
        "images/Rogue_sex/Rogue_piercings_sex[RogueX.piercings]_breasts.png"

    if RogueX.neck == "_spiked_collar":
        "images/RogueSex/Rogue_Sex_Neck_Stud.png"

    if "belly" in RogueX.spunk:
        "images/KittySex/Kitty_Sex_Spunk_Body.png"

    if "tits" in RogueX.spunk:
        "images/KittySex/Kitty_Sex_Spunk_Tits.png"

    if "suck_breasts" in [primary_action, offhand_action]:
        "Rogue_Sex_Lick_Breasts"

    if "fondle_breasts" in [primary_action, offhand_action]:
        "Rogue_Sex_Fondle_Breasts"

    always:
        "Rogue_head_Sex" pos (0.48, 0.1)

    size (1120, 840) offset (50, 50) zoom 0.9

layeredimage Rogue_doggy_body:
    if not RogueX.Water and RogueX.hair == "_evo":
        "images/RogueDoggy/Rogue_Doggy_HairB.png"

    always:
        "images/RogueDoggy/Rogue_Doggy_Body.png"

    if RogueX.neck == "_spiked_collar":
        "images/RogueDoggy/Rogue_Doggy_Collar.png"

    if "mouth" in RogueX.spunk:
        "images/Rogue_doggy/Rogue_mouth_doggy[RogueX.mouth]_spunk.png"
    else:
        "images/Rogue_doggy/Rogue_mouth_doggy[RogueX.mouth].png"

    if RogueX.blushing:
        "images/RogueDoggy/Rogue_Doggy_Blush.png"

    always:
        "images/Rogue_doggy/Rogue_brows_doggy[RogueX.brows].png"

    if RogueX.eyes != "_closed":
        "Rogue_doggy_blinking"
    else:
        "images/Rogue_doggy/Rogue_eyes_doggy_closed.png"

    if RogueX.bra:
        "images/Rogue_doggy/Rogue_chest_doggy[RogueX.bra].png"

    if RogueX.Water:
        "images/RogueDoggy/Rogue_Doggy_WetTop.png"

    if RogueX.top:
        "images/Rogue_doggy/Rogue_top_doggy[RogueX.top].png"

    if RogueX.Water:
        "images/RogueDoggy/Rogue_Doggy_HairWet.png"
    else:
        "images/Rogue_doggy/Rogue_hair_doggy[RogueX.hair].png"

    if RogueX.top == "hoodie":
        "images/RogueDoggy/Rogue_Doggy_Over_Hood.png"

    if "hair" in RogueX.spunk:
        "images/RogueDoggy/Rogue_Doggy_Spunk_Hair.png"

    if "facial" in RogueX.spunk:
        "images/RogueDoggy/Rogue_Doggy_Spunk_Facial.png"

    if primary_action == "fondle_breasts" or offhand_action == "fondle_breasts":
        "Rogue_Doggy_GropeBreast"

    size (420, 750)

layeredimage Rogue_doggy_eyes:
    always:
        "images/Rogue_doggy/Rogue_eyes_doggy[RogueX.eyes].png"

layeredimage Rogue_doggy_ass:
    if not RogueX.underwear_pulled_down or (RogueX.legs == "_pants" and not RogueX.upskirt):
        Null()
    elif RogueX.underwear:
        "images/Rogue_doggy/Rogue_underwear_doggy[RogueX.underwear]_back.png"

    always:
        "images/RogueDoggy/Rogue_Doggy_Ass.png"

    if RogueX.Water:
        "images/RogueDoggy/Rogue_Doggy_WetAss.png"

    if RogueX.hose == "_stockings":
        "images/RogueDoggy/Rogue_Doggy_Hose.png"

    if not RogueX.underwear_pulled_down or (RogueX.legs == "_pants" and not RogueX.upskirt):
        Null()
    elif not RogueX.underwear:
        Null()
    elif RogueX.grool > 1 and RogueX.underwear not in ["_panties", "_lace_panties", "_bikini_bottoms"]:
        "images/Rogue_doggy/Rogue_underwear_doggy[RogueX.underwear]_down_wet.png"
    elif RogueX.underwear:
        "images/Rogue_doggy/Rogue_underwear_doggy[RogueX.underwear]_down.png"

    if not RogueX.pubes:
        Null()
    elif RogueX.legs == "_pants" and not RogueX.upskirt:
        "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png"
    elif RogueX.underwear:
        "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png"
    elif RogueX.hose and RogueX.hose != "_stockings":
        "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png"
    else:
        "images/RogueDoggy/Rogue_Doggy_Pubes.png"

    if Player.sprite and Player.cock == "in" and action_speed > 2:
        "Rogue_Pussy_Fucking3"
    elif (Player.sprite and Player.cock == "in" and action_speed > 1) or primary_action == "dildo_pussy":
        "Rogue_Pussy_Fucking2"
    elif Player.sprite and Player.cock == "in" and action_speed:
        "Rogue_Pussy_Heading"
    elif Player.sprite and Player.cock == "in":
        "Rogue_Pussy_Static"
    elif primary_action == "eat_pussy":
        "images/RogueDoggy/Rogue_Doggy_Pussy_Open.png"
    elif primary_action == "fondle_pussy" or offhand_action == "fondle_pussy":
        "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png"
    else:
        "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png"

    if RogueX.piercings == "_ring":
        "images/RogueDoggy/Rogue_Doggy_PussyRing.png"
    elif RogueX.piercings == "_barbell":
        "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png"

    if Player.sprite and Player.cock == "anal" and action_speed > 2:
        "Rogue_Anal_Fucking2"
    elif (Player.sprite and Player.cock == "anal" and action_speed > 1) or primary_action == "dildo_ass":
        "Rogue_Anal_Fucking"
    elif Player.sprite and Player.cock == "anal" and action_speed:
        "Rogue_Anal_Heading"
    elif Player.sprite and Player.cock == "anal":
        "Rogue_Anal"
    elif RogueX.underwear and not RogueX.underwear_pulled_down:
        "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"
    elif primary_action == "finger_ass" or offhand_action == "finger_ass":
        "Rogue_Anal_Fingering"
    elif primary_action == "dildo_anal":
        "Rogue_Anal_Fucking"
    elif RogueX.used_to_anal:
        "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"
    else:
        "images/RogueDoggy/Rogue_Doggy_Asshole_Tight.png"

    if "anal" not in RogueX.spunk:
        Null()
    elif Player.cock == "anal":
        "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png"
    else:
        "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png"

    if RogueX.underwear_pulled_down or not RogueX.underwear:
        Null()
    elif Player.sprite and Player.cock in ["in", "anal"]:
        Null()
    else:
        "images/Rogue_doggy/Rogue_underwear_doggy[RogueX.underwear].png"

    if Player.sprite and Player.cock in ["in", "anal"]:
        Null()
    elif RogueX.hose in ["_garter_belt", "_stockings_and_garterbelt"]:
        "images/Rogue_doggy/Rogue_hose_doggy[RogueX.hose].png"
    elif RogueX.underwear and RogueX.underwear_pulled_down:
        Null()
    elif RogueX.hose == "_tights" and RogueX.grool:
        "images/Rogue_doggy/Rogue_hose_doggy[RogueX.hose]_wet.png"
    elif RogueX.hose:
        "images/Rogue_doggy/Rogue_hose_doggy[RogueX.hose].png"

    if RogueX.legs == "_pants" and RogueX.upskirt:
        "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Down.png"
    elif RogueX.legs == "_pants" and RogueX.grool > 1:
        "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Wet.png"
    elif RogueX.legs == "_pants":
        "images/RogueDoggy/Rogue_Doggy_Legs_Pants.png"
    elif RogueX.legs == "_skirt" and RogueX.upskirt and Player.sprite and Player.cock == "anal" and action_speed:
        "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_UpAnal.png"
    elif RogueX.legs == "_skirt" and RogueX.upskirt:
        "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_Up.png"
    elif RogueX.legs == "_skirt":
        "images/RogueDoggy/Rogue_Doggy_Legs_Skirt.png"

    if RogueX.top in ["_nighty", "_towel"] and RogueX.upskirt:
        "images/Rogue_doggy/Rogue_top_doggy[RogueX.top]_ass_up.png"
    elif RogueX.top in ["_nighty", "_towel"]:
        "images/Rogue_doggy/Rogue_top_doggy[RogueX.top]_ass.png"

    if RogueX.accessory == "_sweater" and (RogueX.upskirt or (Player.sprite and Player.cock == "out")):
        "images/RogueDoggy/Rogue_Doggy_Acc_Sweater_Up.png"
    elif RogueX.accessory == "_sweater":
        "images/RogueDoggy/Rogue_Doggy_Acc_Sweater.png"

    if "back" in RogueX.spunk:
        "images/RogueDoggy/Rogue_Doggy_SpunkAss.png"

    if primary_action == "eat_pussy":
        "Rogue_doggy_licking_pussy"
    elif primary_action == "eat_ass":
        "Rogue_doggy_licking_ass"

    if not Player.sprite or Player.cock != "out":
        Null()
    elif RogueX.legs == "_skirt" and RogueX.upskirt:
        "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png"
    else:
        "images/RogueDoggy/Rogue_Doggy_HotdogBack.png"

    if not Player.sprite or Player.cock != "out":
        Null()
    elif RogueX.legs == "_skirt" and RogueX.upskirt and action_speed:
        AlphaMask("Zero_hotdog_moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png")
    elif RogueX.legs == "_skirt" and RogueX.upskirt:
        AlphaMask("Zero_hotdog_static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png")
    elif action_speed:
        AlphaMask("Zero_hotdog_moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png")
    else:
        AlphaMask("Zero_hotdog_static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png")

    size (420, 750)

layeredimage Rogue_doggy_shins:
    always:
        "images/RogueDoggy/Rogue_doggy_shins.png"

    if RogueX.legs == "_pants":
        "images/Rogue_doggy/Rogue_feet_doggy[RogueX.legs].png"

    always:
        "images/RogueDoggy/Rogue_doggy_feet.png"

    if not RogueX.hose:
        Null()
    else:
        "images/Rogue_doggy/Rogue_feet_doggy[RogueX.hose].png"

image Rogue_doggy_feet:
    contains:
        AlphaMask("Rogue_doggy_shins", "images/RogueDoggy/Rogue_Doggy_Toes.png")
