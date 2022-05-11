image Rogue_Sprite:
    LiveComposite(
        (480,960),

        (185,38),ConditionSwitch(
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "True", "Rogue_HairBack"),

        (0,0), ConditionSwitch(
            "RogueX.Pubes and RogueX.Pierce == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            "RogueX.Pubes and RogueX.Pierce == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueSprite/Rogue_body_ring.png",
            "RogueX.Pierce == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
            "RogueX.Pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",
            "True", "images/RogueSprite/Rogue_body_bare.png"),

        (0,0), ConditionSwitch(
            "RogueX.Hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",
            "RogueX.Legs == 'pants' and RogueX.Upskirt", "images/RogueSprite/Rogue_pantsback.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not RogueX.Panties", Null(),
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", "images/RogueSprite/Rogue_panties.png",
            "RogueX.PantiesDown", ConditionSwitch(
                "RogueX.Wet > 1", ConditionSwitch(
                    "RogueX.Panties == 'shorts'", "images/RogueSprite/Rogue_shorts_down_wet.png",
                    "RogueX.Panties == 'green panties'", "images/RogueSprite/Rogue_undies_down_wet.png",
                    "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",
                    "True", "images/RogueSprite/Rogue_panties_down.png"),
                "True", ConditionSwitch(
                    "RogueX.Panties == 'shorts'", "images/RogueSprite/Rogue_shorts_down.png",
                    "RogueX.Panties == 'green panties'", "images/RogueSprite/Rogue_undies_down.png",
                    "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",
                    "True", "images/RogueSprite/Rogue_panties_down.png")),
            "True", ConditionSwitch(
                    "RogueX.Wet > 1", ConditionSwitch(
                        "RogueX.Panties == 'shorts' and RogueX.Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",
                        "RogueX.Panties == 'green panties' and RogueX.Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",
                        "RogueX.Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",
                        "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",
                        "True", "images/RogueSprite/Rogue_panties.png"),
                    "True", ConditionSwitch(
                        "RogueX.Panties == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
                        "RogueX.Panties == 'green panties'", "images/RogueSprite/Rogue_undies.png",
                        "RogueX.Panties == 'lace panties'", "images/RogueSprite/Rogue_lacepanties.png",
                        "RogueX.Panties == 'bikini bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",
                        "True", "images/RogueSprite/Rogue_panties.png"))),

        (0,0), ConditionSwitch(
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",
            "RogueX.Hose == 'garterbelt'", "images/RogueSprite/Rogue_garters.png",
            "RogueX.Hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",
            "RogueX.Hose == 'tights' and RogueX.Wet", "images/RogueSprite/Rogue_tights_wet.png",
            "RogueX.Hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueSprite/Rogue_hose_holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueSprite/Rogue_tights_holed.png",
            "True", Null()),

        (240,560), ConditionSwitch(
            "not RogueX.Wet", Null(),
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", Null(),
            "RogueX.Panties and not RogueX.PantiesDown and RogueX.Wet <= 1", Null(),
            "RogueX.Wet == 1", ConditionSwitch(
                "RogueX.Panties and RogueX.PantiesDown", AlphaMask("Wet_Drip","Rogue_Drip_MaskP"),
                "RogueX.Legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"),
                "True", AlphaMask("Wet_Drip","Rogue_Drip_Mask")),
            "True", ConditionSwitch( #Wet = 2+
                    "RogueX.Panties and RogueX.PantiesDown", AlphaMask("Wet_Drip2","Rogue_Drip_MaskP"), #"Wet_Drip2",#
                    "RogueX.Panties and RogueX.Legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"), #"Wet_Drip2",#
                    "RogueX.Legs == 'pants'", AlphaMask("Wet_Drip2","Rogue_Drip_MaskPn"),
                    "RogueX.Panties", AlphaMask("Wet_Drip","Rogue_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Wet_Drip2","Rogue_Drip_Mask"))),

        (0,0), ConditionSwitch(
            "not RogueX.Wet", Null(),
            "RogueX.Legs and RogueX.Wet <= 1", Null(),
            "RogueX.Legs", "images/RogueSprite/Rogue_wet.png",
            "RogueX.Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png"),

        (240,560), ConditionSwitch(
            "'in' not in RogueX.Spunk and 'anal' not in RogueX.Spunk", Null(),
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", Null(),
            "True", ConditionSwitch( #Wet = 2+
                "RogueX.Panties and RogueX.PantiesDown", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskP"), #"Wet_Drip2",#
                "RogueX.Panties and RogueX.Legs == 'pants'", AlphaMask("Spunk_Drip","Rogue_Drip_MaskPn"), #"Wet_Drip2",#
                "RogueX.Legs == 'pants'", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskPn"),
                "True", AlphaMask("Spunk_Drip2","Rogue_Drip_Mask"))),

        (0,0), ConditionSwitch(
            "RogueX.Legs == 'pants' and RogueX.Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png",
            "RogueX.Legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",
            "RogueX.Legs == 'skirt' and RogueX.Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            "RogueX.Legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.ArmPose == 1 and RogueX.Arms == 'gloves' and RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_gloved.png",       #Gloves and collar
            "RogueX.ArmPose == 1 and RogueX.Arms == 'gloves'", "images/RogueSprite/Rogue_arms1b_gloved.png",                                     #Gloves, no collar
            "RogueX.ArmPose == 1 and RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms1a_bare.png",                                #No Gloves, collar
            "RogueX.ArmPose == 1", "images/RogueSprite/Rogue_arms1b_bare.png",                                                              #No gloves, no collar
            "RogueX.Arms == 'gloves' and RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_gloved.png",                           #Gloves and collar
            "RogueX.Arms == 'gloves'", "images/RogueSprite/Rogue_arms2b_gloved.png",                                                         #Gloved, no collar
            "RogueX.Neck == 'spiked collar'", "images/RogueSprite/Rogue_arms2a_bare.png",                                                    #No gloves, collar
            "True", "images/RogueSprite/Rogue_arms2b_bare.png"),

        (0,0), ConditionSwitch(
            "RogueX.Pierce == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",
            "True", "images/RogueSprite/Rogue_chest_bare.png"),

        (0,0), ConditionSwitch(
            "not RogueX.Chest", Null(),
            "RogueX.Uptop", ConditionSwitch(
                "RogueX.Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank_Up.png",
                "RogueX.Chest == 'tube top'", "images/RogueSprite/Rogue_chest_tube_Up.png",
                "RogueX.Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2_Up.png",
                "RogueX.Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra_Up.png",
                "RogueX.Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra_Up.png",
                "RogueX.Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra_Up.png",
                "RogueX.Chest == 'bikini top'", "images/RogueSprite/Rogue_chest_bikini_Up.png"),
            "True", ConditionSwitch(
                "RogueX.Chest == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
                "RogueX.Chest == 'tube top'", "images/RogueSprite/Rogue_chest_tube.png",
                "RogueX.Chest == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",
                "RogueX.Chest == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",
                "RogueX.Chest == 'sports bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
                "RogueX.Chest == 'lace bra'", "images/RogueSprite/Rogue_chest_lacebra.png",
                "RogueX.Chest == 'bikini top'", "images/RogueSprite/Rogue_chest_bikini.png",
                "True", Null())),

        (0,0), ConditionSwitch(
            "RogueX.Water and RogueX.ArmPose == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "RogueX.Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not RogueX.Over", Null(),
            "RogueX.Uptop", ConditionSwitch(
                "RogueX.ArmPose == 1", ConditionSwitch(
                    "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",
                    "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1_Up.png",
                    "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1_Up.png",
                    "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
                    "True", Null()),
                "True", ConditionSwitch(
                        "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2_Up.png",
                        "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
                        "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                        "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",
                        "True", Null())),
            "True", ConditionSwitch(
                "RogueX.ArmPose == 1", ConditionSwitch(
                    "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh1.png",
                    "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink1.png",
                    "RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                    "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
                    "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                    "True", Null()),
                "True", ConditionSwitch(
                    "RogueX.Over == 'mesh top'", "images/RogueSprite/Rogue_over_mesh2.png",
                    "RogueX.Over == 'pink top'", "images/RogueSprite/Rogue_over_pink2.png",
                    "RogueX.Over == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                    "RogueX.Over == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
                    "RogueX.Over == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",
                    "True", Null()))),

        (0,0), ConditionSwitch(
            "RogueX.Acc == 'sweater' and RogueX.ArmPose == 2", "images/RogueSprite/Rogue_acc_sweater2.png",
            "RogueX.Acc == 'sweater'", "images/RogueSprite/Rogue_acc_sweater.png",
            "True", Null()),

        (185,38),ConditionSwitch(
            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "True", "Rogue_Head"),

        (0,0), ConditionSwitch(
            "'hand' in RogueX.Spunk and RogueX.ArmPose == 2", "images/RogueSprite/Rogue_spunkhand.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "'belly' in RogueX.Spunk", "images/RogueSprite/Rogue_spunkbelly.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "'tits' in RogueX.Spunk", "images/RogueSprite/Rogue_spunktits.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not RogueX.Held or RogueX.ArmPose != 2", Null(),
            "RogueX.ArmPose == 2 and RogueX.Held == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "RogueX.ArmPose == 2 and RogueX.Held == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",
            "RogueX.ArmPose == 2 and RogueX.Held == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "RogueX.ArmPose == 2 and RogueX.Held == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != RogueX", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == RogueX", Null(),
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not Trigger or Ch_Focus != RogueX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast",
            "Trigger == 'fondle thighs'", "GropeThigh",
            "Trigger == 'fondle breasts'", "GropeRightBreast",
            "Trigger == 'suck breasts'", "LickRightBreast",
            "Trigger == 'vibrator pussy'", "VibratorPussy",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger == 'vibrator anal'", "VibratorAnal",
            "Trigger == 'vibrator anal insert'", "VibratorPussy",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy",
            "Trigger == 'fondle pussy'", "GropePussy",
            "Trigger == 'lick pussy'", "Lickpussy",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not Trigger2 or Ch_Focus != RogueX", Null(),
            "Trigger == 'fondle breasts' and not Trigger3 and not Trigger4 and not Trigger5", "GropeRightBreast",
            "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast",
            "Trigger2 == 'fondle breasts'", "GropeLeftBreast",
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast",
            "Trigger2 == Trigger", Null(),
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger2 == 'suck breasts'", "LickLeftBreast",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger2 == 'vibrator anal'", "VibratorAnal",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger2 == 'fondle pussy'", "GropePussy",
            "Trigger2 == 'lick pussy'", "Lickpussy",
            "Trigger2 == 'fondle thighs'", "GropeThigh",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not Trigger4 or Ch_Focus != RogueX", Null(),
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy",
            "Trigger4 == 'lick pussy'", "Lickpussy",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast",
            "Trigger4 == 'suck breasts'", "LickRightBreast",
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "Trigger4 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger4 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right
            "Trigger4 == 'fondle breasts'", "GirlGropeRightBreast",
            "True", Null()),

        (0,0), ConditionSwitch(
            "Trigger != 'lesbian' or not Trigger3 or Ch_Focus == RogueX", Null(),
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and RogueX.Lust >= 70", "GirlFingerPussy",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy",
            "Trigger3 == 'lick pussy'", "Lickpussy",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast",
            "Trigger3 == 'suck breasts'", "LickRightBreast",
            "Trigger3 == 'fondle breasts' and (Trigger == 'fondle breasts' or Trigger == 'suck breasts')", "GirlGropeLeftBreast",    #When zero is working the right breast, fondle left
            "Trigger3 == 'fondle breasts' and (Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts')", "GirlGropeRightBreast", #When zero is working the left breast, fondle right
            "Trigger3 == 'fondle breasts'", "GirlGropeRightBreast",
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null())
        )

    anchor (0.6, 0.0)
    zoom .75

image Rogue_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (787,913),

        (0,0), ConditionSwitch(
            "not Speed or not renpy.showing('Rogue_BJ_Animation')", ConditionSwitch(
                "RogueX.Blush > 1", "images/RogueBJFace/Rogue_bj_face_base_blush2.png",
                "RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_base_blush.png",
                "True", "images/RogueBJFace/Rogue_bj_face_base.png"),
            "RogueX.Blush > 1", "images/RogueBJFace/Rogue_bj_face_base_s_blush2.png",
            "RogueX.Blush", "images/RogueBJFace/Rogue_bj_face_base_s_blush.png",
            "True", "images/RogueBJFace/Rogue_bj_face_base_s.png"),

        (0,0), ConditionSwitch(                                                                                 #Mouth for under layer
            "renpy.showing('Rogue_BJ_Animation') and Speed", ConditionSwitch(
                "Speed == 1", "images/RogueBJFace/Rogue_bj_mouth_licking.png", #licking
                "Speed == 2", Null(),                                               #heading Rogue_BJ_HeadingMouth()
                "Speed == 3", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #sucking
                "Speed >= 4", "images/RogueBJFace/Rogue_bj_mouth_sucking.png", #deepthroat
                "True", Null()),
            "True", ConditionSwitch(
                "RogueX.Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
                "RogueX.Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
                "RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",
                "RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
                "RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
                "RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
                "RogueX.Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
                "RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",
                "RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",
                "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png")),

        (0,0), ConditionSwitch(
            "'chin' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_spunk_chin.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "'mouth' not in RogueX.Spunk", Null(),
            "renpy.showing('Rogue_BJ_Animation') and Speed == 2",  Null(),
            "renpy.showing('Rogue_BJ_Animation') and Speed == 1",  "images/RogueBJFace/Rogue_bj_spunk_licking.png",
            "renpy.showing('Rogue_BJ_Animation') and Speed",  "images/RogueBJFace/Rogue_bj_spunk_sucking.png",
            "True", ConditionSwitch(
                "RogueX.Mouth == 'normal'", "images/RogueBJFace/Rogue_bj_spunk_normal.png",
                "RogueX.Mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_spunk_lipbite.png",
                "RogueX.Mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_spunk_licking.png",
                "RogueX.Mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_spunk_kiss.png",
                "RogueX.Mouth == 'sad'", "images/RogueBJFace/Rogue_bj_spunk_sad.png",
                "RogueX.Mouth == 'smile'", "images/RogueBJFace/Rogue_bj_spunk_smile.png",
                "RogueX.Mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_spunk_smile.png",
                "RogueX.Mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_spunk_licking.png",
                "RogueX.Mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_spunk_licking.png",
                "True", "images/RogueBJFace/Rogue_bj_spunk_normal.png")),

        (316,590), ConditionSwitch(      #600
            "renpy.showing('Rogue_BJ_Animation') and Speed == 2", At("Rogue_BJ_MouthHeading", Rogue_BJ_MouthAnim()),
            "True", Null()),

        (0,0), ConditionSwitch(                                                                 #Brows
            "RogueX.Blush > 1", ConditionSwitch(
                #blushing version
                "RogueX.Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry_b.png",
                "RogueX.Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad_b.png",
                "RogueX.Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised_b.png",
                "RogueX.Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused_b.png",
                "True", "images/RogueBJFace/Rogue_bj_face_brows_normal_b.png"),
            "RogueX.Brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "RogueX.Brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "RogueX.Brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",
            "RogueX.Brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png"),

        (0,0), "Rogue Blink",                                                                #Eyes
        (0,0), ConditionSwitch(
            "not RogueX.Spunk or Trigger != 'blow' or 'mouth' not in RogueX.Spunk", Null(),
            "Speed == 3", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
            "Speed == 4", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
            "True", Null()),

        (0,0), ConditionSwitch(                                                                 #Hair overlay
            "RogueX.Water", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "RogueX.Hair == 'cosplay'", "images/RogueBJFace/Rogue_bj_hair_cos.png",
            "RogueX.Hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "True", "images/RogueBJFace/Rogue_bj_hair_evo.png"),

        (0,0), ConditionSwitch(
            "RogueX.Water", "images/RogueBJFace/Rogue_bj_wet.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "'hair' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_spunk_hair.png",
            "'facial' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_spunk_facial.png",
            "True", Null()),
        )

    zoom 0.29

image Rogue_HairBack:
    ConditionSwitch(
        "RogueX.Water or RogueX.Hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_wet_back.png",
        "RogueX.Hair == 'cosplay'", "images/RogueBJFace/Rogue_bj_hair_cos_back.png",
        "True", "images/RogueBJFace/Rogue_bj_hair_evo_back.png"),
    zoom 0.29

image Rogue Blink:
    ConditionSwitch(
        "RogueX.Eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",
        "RogueX.Eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",
        "RogueX.Eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "RogueX.Eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "RogueX.Eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "RogueX.Eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "RogueX.Eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "RogueX.Eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_manic.png",
        "RogueX.Eyes == 'squint'", "Rogue_Squint",
        "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png")

    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/RogueBJFace/Rogue_bj_face_eyes_closed.png"
    0.25
    repeat

image Rogue_Squint:
    "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/RogueBJFace/Rogue_bj_face_eyes_squint.png",
    0.25
    repeat

image Rogue_Drip_Mask:
    contains:
        "images/RogueSprite/Rogue_WetMask.png"
        offset (-240,-560)

image Rogue_Drip_MaskP:
    contains:
        "images/RogueSprite/Rogue_WetMaskP.png"
        offset (-240,-560)

image Rogue_Drip_MaskPn:
    contains:
        "images/RogueSprite/Rogue_WetMaskPn.png"
        offset (-240,-560)

image Rogue_Doggy_Animation:
    LiveComposite(
        (420,750),

        (0,0), ConditionSwitch(
            "not Player.Sprite", "Rogue_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                "Speed > 2", "Rogue_Doggy_Fuck2_Top",
                "Speed > 1", "Rogue_Doggy_Fuck_Top",
                "Speed", "Rogue_Doggy_Anal_Head_Top",
                "True", "Rogue_Doggy_Body"),
            "Player.Cock == 'in'", ConditionSwitch(
                "Speed > 2", "Rogue_Doggy_Fuck2_Top",
                "Speed > 1", "Rogue_Doggy_Fuck_Top",
                "True", "Rogue_Doggy_Body"),
            "True", "Rogue_Doggy_Body"),

        (0,0), ConditionSwitch(
            "not Player.Sprite", "Rogue_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                "Speed > 2", "Rogue_Doggy_Fuck2_Ass",
                "Speed > 1", "Rogue_Doggy_Fuck_Ass",
                "Speed", "Rogue_Doggy_Anal_Head_Ass",
                "True", "Rogue_Doggy_Ass"),
            "Player.Cock == 'in'", ConditionSwitch(
                "Speed > 2", "Rogue_Doggy_Fuck2_Ass",
                "Speed > 1", "Rogue_Doggy_Fuck_Ass",
                "True", "Rogue_Doggy_Ass"),
            "True", "Rogue_Doggy_Ass"),

        (0,0), ConditionSwitch(
            "Player.Cock == 'foot'", ConditionSwitch(
                "Speed > 1", "Rogue_Doggy_Feet2",
                "Speed", "Rogue_Doggy_Feet1",
                "True", "Rogue_Doggy_Feet0"),
            "not Player.Sprite and ShowFeet", "Rogue_Doggy_Feet0",
            "True", Null()),
        )

    align (0.6,0.0)

image Rogue_Doggy_Body:
    LiveComposite(                                                                                         #Upper body
        (420,750),

        (0,0), ConditionSwitch(
            #Hair underlayer
            "RogueX.Water", Null(),
            "RogueX.Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairB.png",
            "True", Null()),

        (0,0), "images/RogueDoggy/Rogue_Doggy_Body.png",

        (0,0), ConditionSwitch(
            "RogueX.Neck == 'spiked collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "'mouth' in RogueX.Spunk", ConditionSwitch(
                "RogueX.Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_LipbiteW.png",
                "RogueX.Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_SurprisedW.png",
                "RogueX.Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
                "RogueX.Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_SadW.png",
                "RogueX.Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_SmileW.png",
                "RogueX.Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_TongueW.png",
                "True", "images/RogueDoggy/Rogue_Doggy_Mouth_NormalW.png"),
            "RogueX.Mouth == 'normal'", "images/RogueDoggy/Rogue_Doggy_Mouth_Normal.png",
            "RogueX.Mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_Lipbite.png",
            "RogueX.Mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            "RogueX.Mouth == 'kiss'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",
            "RogueX.Mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_Sad.png",
            "RogueX.Mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "RogueX.Mouth == 'grimace'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "RogueX.Mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",
            "RogueX.Mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_Tongue.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png"),

        (0,0), ConditionSwitch(
            "RogueX.Blush", "images/RogueDoggy/Rogue_Doggy_Blush.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Brows == 'normal'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "RogueX.Brows == 'angry'", "images/RogueDoggy/Rogue_Doggy_Brows_Angry.png",
            "RogueX.Brows == 'sad'", "images/RogueDoggy/Rogue_Doggy_Brows_Sad.png",
            "RogueX.Brows == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Brows_Surprised.png",
            "RogueX.Brows == 'confused'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png"),

        (0,0), "Rogue Doggy Blink",

        (0,0), ConditionSwitch(
            "not RogueX.Chest", Null(),
            "RogueX.Chest == 'tube top'", "images/RogueDoggy/Rogue_Doggy_Chest_Tube.png",
            "RogueX.Chest == 'tank'", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png",
            "RogueX.Chest == 'buttoned tank'", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png",
            "RogueX.Chest == 'sports bra'", "images/RogueDoggy/Rogue_Doggy_Chest_SportsBra.png",
            "RogueX.Chest == 'bikini top'", "images/RogueDoggy/Rogue_Doggy_Chest_Bikini.png",
            "RogueX.Chest", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not RogueX.Over", Null(),
            "RogueX.Over == 'mesh top'", "images/RogueDoggy/Rogue_Doggy_Over_Mesh.png",
            "RogueX.Over == 'pink top'", "images/RogueDoggy/Rogue_Doggy_Over_Pink.png",
            "RogueX.Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hoodie.png",
            "RogueX.Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyTop.png",
            "RogueX.Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelTop.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_HairWet.png",
            "RogueX.Hair == 'cosplay'", "images/RogueDoggy/Rogue_Doggy_Hair_Cos.png",
            "RogueX.Hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairF.png",
            "True", "images/RogueDoggy/Rogue_Doggy_HairF.png"),

        (0,0), ConditionSwitch(
            "RogueX.Over == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not RogueX.Spunk", Null(),
            "'hair' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_Spunk_Hair.png",
            "'facial' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_Spunk_Facial.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Rogue_Doggy_GropeBreast",
            "True", Null()),
        )

image Rogue_Doggy_Ass:
    LiveComposite(                                                                                          #Lower body
        (420,750),

        (0,0), ConditionSwitch(
            "not RogueX.PantiesDown or (RogueX.Legs == 'pants' and not RogueX.Upskirt)", Null(),
            "RogueX.Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            "RogueX.Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Back.png",
            "RogueX.Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Back.png",
            "RogueX.Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png",
            "True", Null()),

        (0,0), "images/RogueDoggy/Rogue_Doggy_Ass.png",

        (0,0), ConditionSwitch(
            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not RogueX.PantiesDown or (RogueX.Legs == 'pants' and not RogueX.Upskirt)", Null(),
            "RogueX.Panties == 'shorts' and RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png", #fix turn this on when graphics fixed
            "RogueX.Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png",
            "RogueX.Panties == 'green panties' and RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "RogueX.Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Down.png",
            "RogueX.Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Down.png",
            "RogueX.Panties", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                "Speed > 2", "Rogue_Pussy_Fucking3",#Speed 3
                "Speed > 1", "Rogue_Pussy_Fucking2",#Speed 2
                "Speed", "Rogue_Pussy_Heading",      #Speed 1
                "True", "Rogue_Pussy_Static"),
            "Trigger == 'lick pussy'", "images/RogueDoggy/Rogue_Doggy_Pussy_Open.png",
            "RogueX.Legs and not RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png",
            "RogueX.Panties and not RogueX.PantiesDown", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png",
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Rogue_Pussy_Fingering",
            "Trigger == 'dildo pussy'", "Rogue_Pussy_Fucking2",
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png"),

        (0,0), ConditionSwitch(
            "not RogueX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "Trigger == 'dildo pussy'", Null(),
            "RogueX.Legs == 'pants' and not RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "RogueX.PantiesDown", "images/RogueDoggy/Rogue_Doggy_Pubes.png",
            "RogueX.Panties", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "RogueX.Hose and RogueX.Hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Pubes.png"),

        (0,0), ConditionSwitch(
            "Player.Sprite", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "Trigger == 'dildo pussy'", Null(),
            "RogueX.Pierce == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",
            "RogueX.Pierce == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                "Speed > 2", "Rogue_Anal_Fucking2", #Speed 3
                "Speed > 1", "Rogue_Anal_Fucking",  #Speed 2
                "Speed", "Rogue_Anal_Heading",      #Speed 1
                "True", "Rogue_Anal"),
            "RogueX.Legs and not RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",
            "RogueX.Panties and not RogueX.PantiesDown", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",
            "Trigger == 'insert ass' or Trigger2 == 'insert ass'", "Rogue_Anal_Fingering",
            "Trigger == 'dildo anal'", "Rogue_Anal_Fucking",
            "RogueX.Loose", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Asshole_Tight.png"),

        (0,0), ConditionSwitch(
            "'anal' not in RogueX.Spunk or Player.Sprite", Null(),
            "Player.Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",
            "RogueX.Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            "True", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png"),

        (0,0), ConditionSwitch(
            "RogueX.PantiesDown or not RogueX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "RogueX.Panties == 'shorts' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",
            "RogueX.Panties == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
            "RogueX.Panties == 'green panties' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",
            "RogueX.Panties == 'green panties'", "images/RogueDoggy/Rogue_Doggy_Undies.png",
            "RogueX.Panties == 'lace panties'", "images/RogueDoggy/Rogue_Doggy_PantiesLace.png",
            "RogueX.Panties == 'bikini bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Panties.png"),

        (0,0), ConditionSwitch(
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "Trigger == 'dildo pussy'", Null(),
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'tights' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
            "RogueX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
            "RogueX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Legs == 'pants'", ConditionSwitch(
                "RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Down.png",
                "RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Wet.png",
                "True", "images/RogueDoggy/Rogue_Doggy_Legs_Pants.png"),
            "RogueX.Legs == 'skirt'", ConditionSwitch(
                    "RogueX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_Up.png",
                    "True", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt.png"),
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Over == 'nighty' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",
            "RogueX.Over == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png",
            "RogueX.Over == 'towel' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss_Up.png",
            "RogueX.Over == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "RogueX.Acc == 'sweater' and (RogueX.Upskirt or (Player.Sprite and Player.Cock == 'out'))", "images/RogueDoggy/Rogue_Doggy_Acc_Sweater_Up.png",
            "RogueX.Acc == 'sweater'", "images/RogueDoggy/Rogue_Doggy_Acc_Sweater.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "'back' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",
            "True", Null()),

        (0,0), ConditionSwitch(
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",
            "Trigger == 'lick ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()),

        (0,0), ConditionSwitch(
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "RogueX.Legs == 'skirt' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png",
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png"),

        (0,0), ConditionSwitch(
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "RogueX.Legs == 'skirt' and RogueX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "RogueX.Legs == 'skirt' and RogueX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png")),
        )

image Rogue Doggy Blink:                                                                                        #Eyes
    ConditionSwitch(
        "RogueX.Eyes == 'sexy'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
        "RogueX.Eyes == 'side'", "images/RogueDoggy/Rogue_Doggy_Eyes_Side.png",
        "RogueX.Eyes == 'normal'", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
        "RogueX.Eyes == 'closed'", "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png",
        "RogueX.Eyes == 'manic'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
        "RogueX.Eyes == 'down'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
        "RogueX.Eyes == 'stunned'", "images/RogueDoggy/Rogue_Doggy_Eyes_Stunned.png",
        "RogueX.Eyes == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
        "RogueX.Eyes == 'squint'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
        "True", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png"),

    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png"
    0.25
    repeat

image Rogue_Doggy_Feet:
    contains:
        AlphaMask("Rogue_Doggy_Shins", "images/RogueDoggy/Rogue_Doggy_Toes.png")

image Rogue_Doggy_Shins:
    contains:
        "images/RogueDoggy/Rogue_Doggy_Shins.png"
    contains:
        ConditionSwitch(
            "RogueX.Legs == 'pants'", "images/RogueDoggy/Rogue_Doggy_Feet_Pants.png",
            "True", Null())
    contains:
        "images/RogueDoggy/Rogue_Doggy_Feet.png"
    contains:
        ConditionSwitch(
            "not RogueX.Hose", Null(),
            "RogueX.Hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",
            "RogueX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights.png",
            "RogueX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights_Holed.png",
            "True", Null())

image Rogue_SexSprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
                "not Player.Sprite", "Rogue_Sex_Body_Static",
                "Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Body_Anim3",
                        "Speed >= 2", "Rogue_Sex_Body_Anim2",
                        "Speed", "Rogue_Sex_Body_Anim1",
                        "True", "Rogue_Sex_Body_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Body_Anim3",
                        "Speed >= 2", "Rogue_Sex_Body_Anim2",
                        "Speed", "Rogue_Sex_Body_Anim1",
                        "True", "Rogue_Sex_Body_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Rogue_Sex_Body_FootAnim2",
                        "Speed", "Rogue_Sex_Body_FootAnim1",
                        "True", "Rogue_Sex_Body_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and Speed >= 2","Rogue_Hotdog_Body_Anim2",
                "True", "Rogue_Sex_Body_Static",
                ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
                "not Player.Sprite", "Rogue_Sex_Legs_Static",
                "Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Legs_Anim3",
                        "Speed >= 2", "Rogue_Sex_Legs_Anim2",
                        "Speed", "Rogue_Sex_Legs_Anim1",
                        "True", "Rogue_Sex_Legs_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Rogue_Sex_Legs_Anim3",
                        "Speed >= 2", "Rogue_Sex_Legs_Anim2",
                        "Speed", "Rogue_Sex_Legs_Anim1",
                        "True", "Rogue_Sex_Legs_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 2", "Rogue_Sex_Legs_FootAnim2",
                        "Speed", "Rogue_Sex_Legs_FootAnim1",
                        "True", "Rogue_Sex_Legs_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and Speed >= 2","Rogue_Hotdog_Legs_Anim2",
                "True", "Rogue_Sex_Legs_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,200)#(650,230)
    zoom 0.85#0.8

image Rogue_Sex_Body_Static:
    contains:
            "Rogue_Sex_Body"
    pos (650,230)

image Rogue_Sex_Legs_Static:
    contains:
            "Rogue_Sex_Legs"
    pos (650,230)

image Rogue_Sex_Body:
    LiveComposite(
        #the torso/head used in the sex pose, referenced by Rogue_SexSprite
        (1120,840),

        (320,-135), "Rogue_HairBack_Sex",                                                                                      #Hair underlayer
        (0,0), ConditionSwitch(
            #Body Base
            "RogueX.Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Body_Barbell.png",
            "RogueX.Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Body_Ring.png",
            "True", "images/RogueSex/Rogue_Sex_Body.png",
            ),
        #(260,-350), "Rogue_Head_Sex",  #check positioning (400,-300)
        (0,0), ConditionSwitch(
            #bra layer
            "not RogueX.Chest", Null(),
            "RogueX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "RogueX.Chest == 'tank'", "images/RogueSex/Rogue_Sex_Chest_Tank_Up.png",
                    "RogueX.Chest == 'tube top'", "images/RogueSex/Rogue_Sex_Chest_Tube_Up.png",
                    "RogueX.Chest == 'buttoned tank'", "images/RogueSex/Rogue_Sex_Chest_ButtonTank_Up.png",
                    "RogueX.Chest == 'sports bra'", "images/RogueSex/Rogue_Sex_Chest_SportsBra_Up.png",
                    "RogueX.Chest == 'bra'", "images/RogueSex/Rogue_Sex_Chest_Bra_Up.png",
                    "RogueX.Chest == 'bikini top'", "images/RogueSex/Rogue_Sex_Chest_Bikini_Up.png",
                    "RogueX.Chest == 'lace bra'", "images/RogueSex/Rogue_Sex_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "RogueX.Chest == 'tank'", "images/RogueSex/Rogue_Sex_Chest_Tank.png",
                    "RogueX.Chest == 'tube top'", "images/RogueSex/Rogue_Sex_Chest_Tube.png",
                    "RogueX.Chest == 'buttoned tank'", "images/RogueSex/Rogue_Sex_Chest_ButtonTank.png",
                    "RogueX.Chest == 'sports bra'", "images/RogueSex/Rogue_Sex_Chest_SportsBra.png",
                    "RogueX.Chest == 'bra'", "images/RogueSex/Rogue_Sex_Chest_Bra.png",
                    "RogueX.Chest == 'bikini top'", "images/RogueSex/Rogue_Sex_Chest_Bikini.png",
                    "RogueX.Chest == 'lace bra'", "images/RogueSex/Rogue_Sex_Chest_LaceBra.png",
                    "True", Null(),
                    ),
            ),
        (0,0),ConditionSwitch(
            #Wet look
            "RogueX.Water", "images/RogueSex/Rogue_Sex_Wet_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "not RogueX.Over", Null(),
            "RogueX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "RogueX.Over == 'pink top'", "images/RogueSex/Rogue_Sex_Over_Pink_Up.png",
                    "RogueX.Over == 'mesh top'", "images/RogueSex/Rogue_Sex_Over_Mesh_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    "RogueX.Over == 'pink top'", "images/RogueSex/Rogue_Sex_Over_Pink.png",
                    "RogueX.Over == 'mesh top'", "images/RogueSex/Rogue_Sex_Over_Mesh.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #Body Base
            "RogueX.Uptop or (not RogueX.Over and not RogueX.Chest)", Null(),
            "RogueX.Pierce == 'barbell'", "images/RogueSex/Rogue_Sex_Pierce_BarbellC.png",
            "RogueX.Pierce == 'ring'", "images/RogueSex/Rogue_Sex_Pierce_RingC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #necklace
            "RogueX.Neck == 'spiked collar'", "images/RogueSex/Rogue_Sex_Neck_Stud.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Body.png",
            "True", Null(),
            ),
        (0,80),ConditionSwitch(
            #Outside Spunk
            "'tits' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast licking animation
            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Rogue_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Rogue_Sex_Fondle_Breasts",
            "True", Null()
            ),
        (320,-135), "Rogue_Head_Sex",  #check positioning (260,-350)
        )
    zoom 0.9
    offset (50,50)

image Rogue_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.6
        offset (450,270)

image Rogue_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.1
        offset (320,-130)

image Rogue_Head_Sex:
    # The head used for the sex pose, referenced by Rogue_Sex_Body
    "Rogue_Head"#"Rogue_Head"
    zoom 1.28 #0.37
    anchor (0.5,0.5)
    rotate -10

image Rogue_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Rogue_Sex_Body
    "Rogue_HairBack"
    zoom 1.28 # 0.37
    anchor (0.5,0.5)
    rotate -10

image Rogue_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), "images/RogueSex/Rogue_Sex_Legs.png",
        #Legs Base
        (0,0),ConditionSwitch(
            #wet look
            "RogueX.Water", "images/RogueSex/Rogue_Sex_Wet_Legs.png",
            "True", Null(),
            ),
        (0,0), "Rogue_Sex_Anus",
        #Anus Composite

        (0,0), "Rogue_Sex_Pussy",
        #Pussy Composite

        (0,0), ConditionSwitch(
            #Panties if up
            "not RogueX.Panties or RogueX.PantiesDown", Null(),
            "Player.Sprite and (Player.Cock == 'sex' or Player.Cock == 'anal')", Null(),  #hide if sexing
            "RogueX.Panties == 'lace panties'", "images/RogueSex/Rogue_Sex_Panties_Lace.png",
            "RogueX.Panties == 'green panties' and RogueX.Wet", "images/RogueSex/Rogue_Sex_Panties_Green_Wet.png",
            "RogueX.Panties == 'green panties' or RogueX.Panties == 'bikini bottoms'", "images/RogueSex/Rogue_Sex_Panties_Green.png",
            "RogueX.Panties == 'shorts' and RogueX.Wet", "images/RogueSex/Rogue_Sex_Panties_Shorts_Wet.png",
            "RogueX.Panties == 'shorts'", "images/RogueSex/Rogue_Sex_Panties_Shorts.png",
            "RogueX.Wet", "images/RogueSex/Rogue_Sex_Panties_Black_Wet.png",
            "True", "images/RogueSex/Rogue_Sex_Panties_Black.png",
            ),

        (0,0), ConditionSwitch(
            #Hose layer (add panties up dependencies)
            #"RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueSex/Rogue_Sex_Hose_Legs_Full_Hole.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Hole.png",
            "RogueX.Hose == 'stockings'", "images/RogueSex/Rogue_Sex_Hose_Legs_Stockings.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueSex/Rogue_Sex_Hose_Legs_StockingGarter.png",
            "RogueX.Hose == 'garterbelt'", "images/RogueSex/Rogue_Sex_Hose_Legs_Garter.png",
            "RogueX.PantiesDown", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),  #hide if sexing
            "RogueX.Hose == 'pantyhose'", "images/RogueSex/Rogue_Sex_Hose_Legs_Full.png",
            "RogueX.Hose == 'tights' and RogueX.Wet", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Wet.png",
            "RogueX.Hose == 'tights'", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "RogueX.Legs == 'skirt'", "images/RogueSex/Rogue_Sex_Legs_Skirt.png",
            "RogueX.Upskirt", Null(),
            "RogueX.Legs == 'pants' and RogueX.Wet > 1", "images/RogueSex/Rogue_Sex_Legs_Pants_Wet.png",
            "RogueX.Legs == 'pants'","images/RogueSex/Rogue_Sex_Legs_Pants.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Sweater
            "RogueX.Acc == 'sweater'", "images/RogueSex/Rogue_Sex_Sweater.png",
            "True", Null(),
            ),

        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #hotdog cock Layer
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "Speed >= 2", "Rogue_Hotdog_Zero_Anim2",
            "Speed", "Rogue_Hotdog_Zero_Anim1",
            "True", "Rogue_Hotdog_Zero_Anim0",
            ),

        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Rogue_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Rogue_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #footjob cock Layer
            "not Player.Sprite or Player.Cock != 'foot'", Null(),
            "Speed >= 2", "Rogue_Footcock_Zero_Anim2",
            "Speed", "Rogue_Footcock_Zero_Anim1",
            "True", "Rogue_Footcock_Static",
            ),

        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Speed or Player.Cock == 'foot' or ShowFeet", "Rogue_Sex_Feet",
            #"Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Rogue_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
            "True", AlphaMask("Rogue_Sex_Feet","images/RogueSex/Rogue_Sex_FeetMask2.png")
            ),
        )

image Rogue_Sex_Feet = LiveComposite(
        #the lower legs used in the sex pose, referenced by Kitty_Sex_Legs
        (1120,840),
        (0,0), "images/RogueSex/Rogue_Sex_Feet.png",                                                         #Legs Base
        (0,0),ConditionSwitch(
            #Wet look
            "RogueX.Water", "images/RogueSex/Rogue_Sex_Wet_Feet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hose Layer
            "not RogueX.Hose", Null(),
            "RogueX.Hose == 'ripped tights'", "images/RogueSex/Rogue_Sex_Hose_Feet_Tights_Hole.png",
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking_Hole.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png",
            "RogueX.Hose == 'stockings'", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png",
            "RogueX.PantiesDown", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),  #hide if sexing
            "RogueX.Hose == 'tights'", "images/RogueSex/Rogue_Sex_Hose_Feet_Tights.png",
            "RogueX.Hose == 'garterbelt'", Null(),
            "True", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "not RogueX.Panties or not RogueX.PantiesDown", Null(),
            "RogueX.Legs == 'pants'", Null(),
            #"Player.Sprite and (Player.Cock == 'sex' or Player.Cock == 'anal')", Null(),  #hide if sexing
            "RogueX.Panties == 'lace panties'", "images/RogueSex/Rogue_Sex_Panties_Lace_Down.png",
            "RogueX.Panties == 'green panties'", "images/RogueSex/Rogue_Sex_Panties_Green_Down.png",
            "RogueX.Panties == 'bikini bottoms'", "images/RogueSex/Rogue_Sex_Panties_Bikini_Down.png",
            "RogueX.Panties == 'shorts'", "images/RogueSex/Rogue_Sex_Panties_Shorts_Down.png",
            "True", "images/RogueSex/Rogue_Sex_Panties_Black_Down.png",
            ),

        (0,0), ConditionSwitch(
            #Legs Layer
            "RogueX.Legs == 'pants' and RogueX.Upskirt", "images/RogueSex/Rogue_Sex_Legs_Pants_Down.png",
            "RogueX.Legs == 'pants'", "images/RogueSex/Rogue_Sex_Legs_Pants_Feet.png",
            "True", Null(),
            ),
        )
