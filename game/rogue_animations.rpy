
image Rogue_Sprite:
    LiveComposite(
        (480,960),









        (185,38),ConditionSwitch(

            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "True", "Rogue_HairBack",
            ),

        (0,0), ConditionSwitch(

            "not RogueX.top", Null(),
            "RogueX.top == 'hoodie'", "images/RogueSprite/Rogue_over_hoodieB.png",
            "RogueX.Uptop", ConditionSwitch(

                    "RogueX.ArmPose == 1", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",


                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",

                            "True", Null(),
                            ),
                    "True", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh2_Up.png",


                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",

                            "True", Null(),
                            ),
                    ),
            "True", ConditionSwitch(

                    "RogueX.ArmPose == 1", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh1.png",


                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",

                            "True", Null(),
                            ),
                    "True", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh2.png",


                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",

                            "True", Null(),
                            ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "RogueX.pubes and RogueX.piercings == 'ring'", "images/RogueSprite/Rogue_bodyhaired_ring.png",
            "RogueX.pubes and RogueX.piercings == 'barbell'", "images/RogueSprite/Rogue_bodyhaired_barbell.png",
            "RogueX.piercings == 'ring'", "images/RogueSprite/Rogue_body_ring.png",
            "RogueX.piercings == 'barbell'", "images/RogueSprite/Rogue_body_barbell.png",
            "RogueX.pubes", "images/RogueSprite/Rogue_bodyhaired_bare.png",
            "True", "images/RogueSprite/Rogue_body_bare.png",
            ),











        (0,0), ConditionSwitch(

            "RogueX.hose == 'stockings'", "images/RogueSprite/Rogue_hose.png",
            "RogueX.legs == 'pants' and RogueX.Upskirt", "images/RogueSprite/Rogue_pantsback.png",
            "True", Null(),
            ),
















        (0,0), ConditionSwitch(

            "not RogueX.underwear", Null(),
            "RogueX.legs == 'pants' and not RogueX.Upskirt", "images/RogueSprite/Rogue_panties.png",
            "RogueX.underwearDown", ConditionSwitch(

                    "RogueX.Wet > 1", ConditionSwitch(

                            "RogueX.underwear == 'shorts'", "images/RogueSprite/Rogue_shorts_down_wet.png",
                            "RogueX.underwear == 'green_panties'", "images/RogueSprite/Rogue_undies_down_wet.png",
                            "RogueX.underwear == 'bikini_bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",
                            "True", "images/RogueSprite/Rogue_panties_down.png",
                            ),
                    "True", ConditionSwitch(

                            "RogueX.underwear == 'shorts'", "images/RogueSprite/Rogue_shorts_down.png",
                            "RogueX.underwear == 'green_panties'", "images/RogueSprite/Rogue_undies_down.png",
                            "RogueX.underwear == 'bikini_bottoms'", "images/RogueSprite/Rogue_panties_bikini_down.png",
                            "True", "images/RogueSprite/Rogue_panties_down.png",
                            ),
                    ),
            "True", ConditionSwitch(

                    "RogueX.Wet > 1", ConditionSwitch(

                            "RogueX.underwear == 'shorts' and RogueX.Wet > 1", "images/RogueSprite/Rogue_shorts_wet.png",
                            "RogueX.underwear == 'green_panties' and RogueX.Wet > 1", "images/RogueSprite/Rogue_undies_wet.png",
                            "RogueX.underwear == 'lace_panties'", "images/RogueSprite/Rogue_lacepanties.png",
                            "RogueX.underwear == 'bikini_bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",
                            "True", "images/RogueSprite/Rogue_panties.png",
                            ),
                    "True", ConditionSwitch(

                            "RogueX.underwear == 'shorts'", "images/RogueSprite/Rogue_shorts.png",
                            "RogueX.underwear == 'green_panties'", "images/RogueSprite/Rogue_undies.png",
                            "RogueX.underwear == 'lace_panties'", "images/RogueSprite/Rogue_lacepanties.png",
                            "RogueX.underwear == 'bikini_bottoms'", "images/RogueSprite/Rogue_panties_bikini.png",
                            "True", "images/RogueSprite/Rogue_panties.png",
                            ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueSprite/Rogue_hose_garter.png",
            "RogueX.hose == 'garterbelt'", "images/RogueSprite/Rogue_garters.png",
            "RogueX.hose == 'pantyhose'", "images/RogueSprite/Rogue_hosefull.png",
            "RogueX.hose == 'tights' and RogueX.Wet", "images/RogueSprite/Rogue_tights_wet.png",
            "RogueX.hose == 'tights'", "images/RogueSprite/Rogue_tights.png",
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueSprite/Rogue_hose_holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueSprite/Rogue_tights_holed.png",
            "True", Null(),
            ),
        (240,560), ConditionSwitch(

            "not RogueX.Wet", Null(),
            "RogueX.legs == 'pants' and not RogueX.Upskirt", Null(),
            "RogueX.underwear and not RogueX.underwearDown and RogueX.Wet <= 1", Null(),
            "RogueX.Wet == 1", ConditionSwitch(
                    "RogueX.underwear and RogueX.underwearDown", AlphaMask("Wet_Drip","Rogue_Drip_MaskP"),
                    "RogueX.legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"),
                    "True", AlphaMask("Wet_Drip","Rogue_Drip_Mask"),
                    ),
            "True", ConditionSwitch(
                    "RogueX.underwear and RogueX.underwearDown", AlphaMask("Wet_Drip2","Rogue_Drip_MaskP"),
                    "RogueX.underwear and RogueX.legs == 'pants'", AlphaMask("Wet_Drip","Rogue_Drip_MaskPn"),
                    "RogueX.legs == 'pants'", AlphaMask("Wet_Drip2","Rogue_Drip_MaskPn"),
                    "RogueX.underwear", AlphaMask("Wet_Drip","Rogue_Drip_Mask"),
                    "True", AlphaMask("Wet_Drip2","Rogue_Drip_Mask"),
                    ),
            ),
        (0,0), ConditionSwitch(

            "not RogueX.Wet", Null(),
            "RogueX.legs and RogueX.Wet <= 1", Null(),
            "RogueX.legs", "images/RogueSprite/Rogue_wet.png",
            "RogueX.Wet == 1", "images/RogueSprite/Rogue_wet.png",
            "True", "images/RogueSprite/Rogue_wet2.png",
            ),
        (240,560), ConditionSwitch(

            "'in' not in RogueX.Spunk and 'anal' not in RogueX.Spunk", Null(),
            "RogueX.legs == 'pants' and not RogueX.Upskirt", Null(),
            "True", ConditionSwitch(
                    "RogueX.underwear and RogueX.underwearDown", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskP"),
                    "RogueX.underwear and RogueX.legs == 'pants'", AlphaMask("Spunk_Drip","Rogue_Drip_MaskPn"),
                    "RogueX.legs == 'pants'", AlphaMask("Spunk_Drip2","Rogue_Drip_MaskPn"),
                    "True", AlphaMask("Spunk_Drip2","Rogue_Drip_Mask"),
                    ),
            ),

















































        (0,0), ConditionSwitch(

            "RogueX.legs == 'pants' and RogueX.Upskirt", "images/RogueSprite/Rogue_legs_pants_down.png",
            "RogueX.legs == 'pants'", "images/RogueSprite/Rogue_legs_pants.png",
            "RogueX.legs == 'skirt' and RogueX.Upskirt", "images/RogueSprite/Rogue_legs_skirt_up.png",
            "RogueX.legs == 'skirt'", "images/RogueSprite/Rogue_legs_skirt.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.ArmPose == 1 and RogueX.arms == 'gloves' and RogueX.neck == 'spiked_collar'", "images/RogueSprite/Rogue_arms1a_gloved.png",
            "RogueX.ArmPose == 1 and RogueX.arms == 'gloves'", "images/RogueSprite/Rogue_arms1b_gloved.png",
            "RogueX.ArmPose == 1 and RogueX.neck == 'spiked_collar'", "images/RogueSprite/Rogue_arms1a_bare.png",
            "RogueX.ArmPose == 1", "images/RogueSprite/Rogue_arms1b_bare.png",
            "RogueX.arms == 'gloves' and RogueX.neck == 'spiked_collar'", "images/RogueSprite/Rogue_arms2a_gloved.png",
            "RogueX.arms == 'gloves'", "images/RogueSprite/Rogue_arms2b_gloved.png",
            "RogueX.neck == 'spiked_collar'", "images/RogueSprite/Rogue_arms2a_bare.png",
            "True", "images/RogueSprite/Rogue_arms2b_bare.png",
            ),
        (0,0), ConditionSwitch(

            "RogueX.piercings == 'barbell'", "images/RogueSprite/Rogue_chest_barbell.png",
            "RogueX.piercings == 'ring'", "images/RogueSprite/Rogue_chest_rings.png",
            "True", "images/RogueSprite/Rogue_chest_bare.png",
            ),









        (0,0), ConditionSwitch(

            "not RogueX.bra", Null(),
            "RogueX.Uptop", ConditionSwitch(

                    "RogueX.bra == 'tank'", "images/RogueSprite/Rogue_chest_tank_Up.png",
                    "RogueX.bra == 'tube_top'", "images/RogueSprite/Rogue_chest_tube_Up.png",
                    "RogueX.bra == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2_Up.png",
                    "RogueX.bra == 'bra'", "images/RogueSprite/Rogue_chest_bra_Up.png",
                    "RogueX.bra == 'sports_bra'", "images/RogueSprite/Rogue_chest_sportsbra_Up.png",
                    "RogueX.bra == 'lace_bra'", "images/RogueSprite/Rogue_chest_lacebra_Up.png",
                    "RogueX.bra == 'bikini_top'", "images/RogueSprite/Rogue_chest_bikini_Up.png",
                    ),
            "True", ConditionSwitch(

                    "RogueX.bra == 'tank'", "images/RogueSprite/Rogue_chest_tank.png",
                    "RogueX.bra == 'tube_top'", "images/RogueSprite/Rogue_chest_tube.png",
                    "RogueX.bra == 'buttoned tank'", "images/RogueSprite/Rogue_chest_tank2.png",
                    "RogueX.bra == 'bra'", "images/RogueSprite/Rogue_chest_bra.png",
                    "RogueX.bra == 'sports_bra'", "images/RogueSprite/Rogue_chest_sportsbra.png",
                    "RogueX.bra == 'lace_bra'", "images/RogueSprite/Rogue_chest_lacebra.png",
                    "RogueX.bra == 'bikini_top'", "images/RogueSprite/Rogue_chest_bikini.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "RogueX.Water and RogueX.ArmPose == 1", "images/RogueSprite/Rogue_body_wet1.png",
            "RogueX.Water", "images/RogueSprite/Rogue_body_wet2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.Water == 3", "images/RogueSprite/Rogue_body_wet3.png",
            "True", Null(),
            ),















        (0,0), ConditionSwitch(

            "not RogueX.top", Null(),
            "RogueX.Uptop", ConditionSwitch(

                    "RogueX.ArmPose == 1", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh1_Up.png",
                            "RogueX.top == 'pink_top'", "images/RogueSprite/Rogue_over_pink1_Up.png",
                            "RogueX.top == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1_Up.png",
                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",

                            "True", Null(),
                            ),
                    "True", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh2_Up.png",
                            "RogueX.top == 'pink_top'", "images/RogueSprite/Rogue_over_pink2_Up.png",
                            "RogueX.top == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2_Up.png",
                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty_Up.png",

                            "True", Null(),
                            ),
                    ),
            "True", ConditionSwitch(

                    "RogueX.ArmPose == 1", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh1.png",
                            "RogueX.top == 'pink_top'", "images/RogueSprite/Rogue_over_pink1.png",
                            "RogueX.top == 'towel'", "images/RogueSprite/Rogue_over_towel1.png",
                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty1.png",
                            "RogueX.top == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie1.png",
                            "True", Null(),
                            ),
                    "True", ConditionSwitch(

                            "RogueX.top == 'mesh_top'", "images/RogueSprite/Rogue_over_mesh2.png",
                            "RogueX.top == 'pink_top'", "images/RogueSprite/Rogue_over_pink2.png",
                            "RogueX.top == 'hoodie'", "images/RogueSprite/Rogue_over_hoodie2.png",
                            "RogueX.top == 'nighty'", "images/RogueSprite/Rogue_over_nighty2.png",
                            "RogueX.top == 'towel'", "images/RogueSprite/Rogue_over_towel2.png",
                            "True", Null(),
                            ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "RogueX.accessory == 'sweater' and RogueX.ArmPose == 2", "images/RogueSprite/Rogue_acc_sweater2.png",
            "RogueX.accessory == 'sweater'", "images/RogueSprite/Rogue_acc_sweater.png",
            "True", Null(),
            ),








        (185,38),ConditionSwitch(

            "renpy.showing('Rogue_BJ_Animation') or renpy.showing('Rogue_TJ_Animation')", Null(),
            "True", "Rogue_Head",
            ),

        (0,0), ConditionSwitch(

            "'hand' in RogueX.Spunk and RogueX.ArmPose == 2", "images/RogueSprite/Rogue_spunkhand.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'belly' in RogueX.Spunk", "images/RogueSprite/Rogue_spunkbelly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' in RogueX.Spunk", "images/RogueSprite/Rogue_spunktits.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "not RogueX.held_item or RogueX.ArmPose != 2", Null(),
            "RogueX.ArmPose == 2 and RogueX.held_item == 'phone'", "images/RogueSprite/Rogue_held_phone.png",
            "RogueX.ArmPose == 2 and RogueX.held_item == 'dildo'", "images/RogueSprite/Rogue_held_dildo.png",
            "RogueX.ArmPose == 2 and RogueX.held_item == 'vibrator'", "images/RogueSprite/Rogue_held_vibrator.png",
            "RogueX.ArmPose == 2 and RogueX.held_item == 'panties'", "images/RogueSprite/Rogue_held_panties.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != RogueX", Null(),
            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and RogueX.lust >= 70", "GirlFingerPussy",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy",
            "girl_offhand_action == 'fondle_breasts' and (offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts')", "GirlGropeLeftBreast",
            "girl_offhand_action == 'fondle_breasts' and (primary_action == 'fondle_breasts' or primary_action == 'suck breasts')", "GirlGropeRightBreast",
            "girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast",
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_offhand_action or second_girl_primary_action != 'masturbation' or focused_Girl == RogueX", Null(),

            "second_girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and RogueX.lust >= 70", "GirlFingerPussy",
            "second_girl_offhand_action == 'fondle_pussy'", "GirlGropePussy",
            "second_girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast",
            "second_girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not primary_action or focused_Girl != RogueX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast",
            "primary_action == 'fondle_thighs'", "GropeThigh",
            "primary_action == 'fondle_breasts'", "GropeRightBreast",
            "primary_action == 'suck breasts'", "LickRightBreast",
            "primary_action == 'vibrator pussy'", "VibratorPussy",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "primary_action == 'vibrator anal'", "VibratorAnal",
            "primary_action == 'vibrator anal insert'", "VibratorPussy",
            "primary_action == 'fondle_pussy' and action_speed == 2", "FingerPussy",
            "primary_action == 'fondle_pussy'", "GropePussy",
            "primary_action == 'eat_pussy'", "Lickpussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not offhand_action or focused_Girl != RogueX", Null(),
            "primary_action == 'fondle_breasts' and not girl_offhand_action and not second_girl_primary_action and not second_girl_offhand_action", "GropeRightBreast",

            "offhand_action == 'fondle_breasts' and primary_action == 'suck breasts'", "GropeLeftBreast",

            "offhand_action == 'fondle_breasts'", "GropeLeftBreast",
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "offhand_action == 'suck breasts'", "LickLeftBreast",
            "offhand_action == 'vibrator pussy'", "VibratorPussy",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "offhand_action == 'vibrator anal'", "VibratorAnal",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "offhand_action == 'fondle_pussy'", "GropePussy",
            "offhand_action == 'eat_pussy'", "Lickpussy",
            "offhand_action == 'fondle_thighs'", "GropeThigh",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_primary_action or focused_Girl != RogueX", Null(),
            "second_girl_primary_action == 'fondle_pussy' and primary_action != 'sex' and RogueX.lust >= 70", "GirlFingerPussy",
            "second_girl_primary_action == 'fondle_pussy'", "GirlGropePussy",
            "second_girl_primary_action == 'eat_pussy'", "Lickpussy",
            "second_girl_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast",
            "second_girl_primary_action == 'suck breasts'", "LickRightBreast",
            "second_girl_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_primary_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "second_girl_primary_action == 'fondle_breasts' and (primary_action == 'fondle_breasts' or primary_action == 'suck breasts')", "GirlGropeLeftBreast",
            "second_girl_primary_action == 'fondle_breasts' and (offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts')", "GirlGropeRightBreast",
            "second_girl_primary_action == 'fondle_breasts'", "GirlGropeRightBreast",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action != 'lesbian' or not girl_offhand_action or focused_Girl == RogueX", Null(),
            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and RogueX.lust >= 70", "GirlFingerPussy",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy",
            "girl_offhand_action == 'eat_pussy'", "Lickpussy",
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast",
            "girl_offhand_action == 'fondle_breasts' and (primary_action == 'fondle_breasts' or primary_action == 'suck breasts')", "GirlGropeLeftBreast",
            "girl_offhand_action == 'fondle_breasts' and (offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts')", "GirlGropeRightBreast",
            "girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast",
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom .75


image Rogue_Head:
    LiveComposite(
        (787,913),




        (0,0), ConditionSwitch(

            "not action_speed or not renpy.showing('Rogue_BJ_Animation')", ConditionSwitch(

                    "RogueX.blushing > 1", "images/RogueBJFace/Rogue_bj_face_base_blush2.png",
                    "RogueX.blushing", "images/RogueBJFace/Rogue_bj_face_base_blush.png",
                    "True", "images/RogueBJFace/Rogue_bj_face_base.png",
                    ),
            "RogueX.blushing > 1", "images/RogueBJFace/Rogue_bj_face_base_s_blush2.png",
            "RogueX.blushing", "images/RogueBJFace/Rogue_bj_face_base_s_blush.png",
            "True", "images/RogueBJFace/Rogue_bj_face_base_s.png"
            ),
        (0,0), ConditionSwitch(
            "renpy.showing('Rogue_BJ_Animation') and action_speed", ConditionSwitch(


                    "action_speed == 1", "images/RogueBJFace/Rogue_bj_mouth_licking.png",
                    "action_speed == 2", Null(),
                    "action_speed == 3", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
                    "action_speed >= 4", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
                    "True", Null(),
                    ),










            "True", ConditionSwitch(

                    "RogueX.mouth == 'normal'", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
                    "RogueX.mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_mouth_lipbite.png",
                    "RogueX.mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",
                    "RogueX.mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_mouth_kiss.png",
                    "RogueX.mouth == 'sad'", "images/RogueBJFace/Rogue_bj_mouth_sad.png",
                    "RogueX.mouth == 'smile'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
                    "RogueX.mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_mouth_smile.png",
                    "RogueX.mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_mouth_surprised.png",
                    "RogueX.mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_mouth_licking.png",
                    "True", "images/RogueBJFace/Rogue_bj_mouth_normal.png",
                    ),
            ),
        (0,0), ConditionSwitch(

                "'chin' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_spunk_chin.png",
                "True", Null(),
                ),
        (0,0), ConditionSwitch(

            "'mouth' not in RogueX.Spunk", Null(),
            "renpy.showing('Rogue_BJ_Animation') and action_speed == 2",  Null(),
            "renpy.showing('Rogue_BJ_Animation') and action_speed == 1",  "images/RogueBJFace/Rogue_bj_spunk_licking.png",
            "renpy.showing('Rogue_BJ_Animation') and action_speed",  "images/RogueBJFace/Rogue_bj_spunk_sucking.png",
            "True", ConditionSwitch(

                    "RogueX.mouth == 'normal'", "images/RogueBJFace/Rogue_bj_spunk_normal.png",
                    "RogueX.mouth == 'lipbite'", "images/RogueBJFace/Rogue_bj_spunk_lipbite.png",
                    "RogueX.mouth == 'sucking'", "images/RogueBJFace/Rogue_bj_spunk_licking.png",
                    "RogueX.mouth == 'kiss'", "images/RogueBJFace/Rogue_bj_spunk_kiss.png",
                    "RogueX.mouth == 'sad'", "images/RogueBJFace/Rogue_bj_spunk_sad.png",
                    "RogueX.mouth == 'smile'", "images/RogueBJFace/Rogue_bj_spunk_smile.png",
                    "RogueX.mouth == 'grimace'", "images/RogueBJFace/Rogue_bj_spunk_smile.png",
                    "RogueX.mouth == 'surprised'", "images/RogueBJFace/Rogue_bj_spunk_licking.png",
                    "RogueX.mouth == 'tongue'", "images/RogueBJFace/Rogue_bj_spunk_licking.png",
                    "True", "images/RogueBJFace/Rogue_bj_spunk_normal.png",
                    ),
            ),
        (316,590), ConditionSwitch(
            "renpy.showing('Rogue_BJ_Animation') and action_speed == 2", At("Rogue_BJ_MouthHeading", Rogue_BJ_MouthAnim()),
            "True", Null(),
            ),








        (0,0), ConditionSwitch(
            "RogueX.blushing > 1", ConditionSwitch(

                    "RogueX.brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry_b.png",
                    "RogueX.brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad_b.png",
                    "RogueX.brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised_b.png",
                    "RogueX.brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused_b.png",
                    "True", "images/RogueBJFace/Rogue_bj_face_brows_normal_b.png",
                    ),
            "RogueX.brows == 'angry'", "images/RogueBJFace/Rogue_bj_face_brows_angry.png",
            "RogueX.brows == 'sad'", "images/RogueBJFace/Rogue_bj_face_brows_sad.png",
            "RogueX.brows == 'surprised'", "images/RogueBJFace/Rogue_bj_face_brows_surprised.png",
            "RogueX.brows == 'confused'", "images/RogueBJFace/Rogue_bj_face_brows_confused.png",
            "True", "images/RogueBJFace/Rogue_bj_face_brows_normal.png",
            ),
        (0,0), "Rogue Blink",
        (0,0), ConditionSwitch(

                "not RogueX.Spunk or primary_action != 'blow' or 'mouth' not in RogueX.Spunk", Null(),

                "action_speed == 3", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "action_speed == 4", "images/RogueBJFace/Rogue_bj_face_over_sucking_cum.png",
                "True", Null(),
                ),
        (0,0), ConditionSwitch(
            "RogueX.Water", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "RogueX.hair == 'cosplay'", "images/RogueBJFace/Rogue_bj_hair_cos.png",
            "RogueX.hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_wet.png",
            "True", "images/RogueBJFace/Rogue_bj_hair_evo.png",
            ),
        (0,0), ConditionSwitch(

            "RogueX.Water", "images/RogueBJFace/Rogue_bj_wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

                "'hair' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_spunk_hair.png",
                "'facial' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_spunk_facial.png",
                "True", Null(),
                ),
        )
    zoom .29

image Rogue_HairBack:
    ConditionSwitch(

            "RogueX.Water or RogueX.hair == 'wet'", "images/RogueBJFace/Rogue_bj_hair_wet_back.png",
            "RogueX.hair == 'cosplay'", "images/RogueBJFace/Rogue_bj_hair_cos_back.png",
            "True", "images/RogueBJFace/Rogue_bj_hair_evo_back.png",
            ),
    zoom .29

image Rogue Blink:

    ConditionSwitch(
        "RogueX.eyes == 'normal'", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",
        "RogueX.eyes == 'sexy'", "images/RogueBJFace/Rogue_bj_face_eyes_sexy.png",
        "RogueX.eyes == 'closed'", "images/RogueBJFace/Rogue_bj_face_eyes_closed.png",
        "RogueX.eyes == 'surprised'", "images/RogueBJFace/Rogue_bj_face_eyes_surprised.png",
        "RogueX.eyes == 'side'", "images/RogueBJFace/Rogue_bj_face_eyes_side.png",
        "RogueX.eyes == 'stunned'", "images/RogueBJFace/Rogue_bj_face_eyes_stunned.png",
        "RogueX.eyes == 'down'", "images/RogueBJFace/Rogue_bj_face_eyes_down.png",
        "RogueX.eyes == 'manic'", "images/RogueBJFace/Rogue_bj_face_eyes_manic.png",
        "RogueX.eyes == 'squint'", "Rogue_Squint",
        "True", "images/RogueBJFace/Rogue_bj_face_eyes_normal.png",
        )
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/RogueBJFace/Rogue_bj_face_eyes_closed.png"
    .25
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
    .25
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


image Professor:
    LiveComposite(
        (429,521),
        (0,0), "images/NPC/Xavier_body.png",
        (0,0), ConditionSwitch(
            "X_Brows == 'concentrate'", "images/NPC/Xavier_brows_concentrate.png",
            "X_Brows == 'happy'", "images/NPC/Xavier_brows_happy.png",
            "X_Brows == 'shocked'", "images/NPC/Xavier_brows_shocked.png",
            "X_Brows == 'neutral'", "images/NPC/Xavier_brows_neutral.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "X_Mouth == 'concentrate'", "images/NPC/Xavier_mouth_stern.png",
            "X_Mouth == 'happy'", "images/NPC/Xavier_mouth_smile.png",
            "X_Mouth == 'neutral'", "images/NPC/Xavier_mouth_neutral.png",
            "True", Null(),
            ),
        (0,0), "Xavier Blink",
        (0,0), ConditionSwitch(
            "X_Psychic == 1", "images/NPC/Xavier_psychic.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.0)
    offset (0,150)
    zoom 1.1

image Xavier Blink:
    ConditionSwitch(
    "X_Eyes == 'concentrate'", "images/NPC/Xavier_eyes_closed.png",
    "X_Eyes == 'hypno'", "images/NPC/Xavier_eyes_hypno.png",
    "X_Eyes == 'shocked'", "images/NPC/Xavier_eyes_shocked.png",
    "True", "images/NPC/Xavier_eyes_happy.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3

    "images/NPC/Xavier_eyes_closed.png"
    .25
    repeat



image setting = LiveComposite(
    (1024,768),
    (0, 0), ConditionSwitch(
        "time_index >= 3", "images/sky_night.jpg",
        "time_index == 2", "images/sky_sunset.jpg",
        "True", "images/sky_day.jpg",
        ),
    (0, 0), ConditionSwitch(
        "bg_current == 'bg_study'", "images/study.jpg",
        "bg_current == 'bg_player'", "images/playerroom.png",
        "bg_current == 'bg_dangerroom'", "images/dangerroom.jpg",
        "bg_current == 'bg_showerroom'", "images/Shower.jpg",
        "bg_current == 'bg_rogue'", "images/Rogueroom.png",
        "bg_current == 'bg_movies'", "images/Movies.jpg",
        "bg_current == 'bg_restaurant'", "images/Restaurant.jpg",
        "bg_current == 'bg_kitty'", "images/kittyroom.png",
        "bg_current == 'bg_emma'", "images/emmaroom.png",


        "time_index >= 3",      "images/Crossroads_Night.jpg",
        "time_index == 2",    "images/Crossroads_Evening.jpg",
        "True",                         "images/Crossroads_Day.jpg",
        ),
    )

label Display_Background(Entry=0):


    if Entry:
        scene bg_entry onlayer backdrop
    elif bg_current == "bg_player":
        scene bg_player onlayer backdrop
    elif bg_current == "bg_rogue":
        scene bg_rogue onlayer backdrop
    elif bg_current == "bg_kitty":
        scene bg_kitty onlayer backdrop
    elif bg_current == "bg_emma":
        scene bg_emma onlayer backdrop
    elif bg_current == "bg_laura":
        scene bg_laura onlayer backdrop
    elif bg_current == "bg_jean":
        scene bg_jean onlayer backdrop
    elif bg_current == "bg_storm":
        scene bg_storm onlayer backdrop
    elif bg_current == "bg_jubes":
        scene bg_jubes onlayer backdrop
    elif bg_current == "bg_classroom":
        scene bg_class onlayer backdrop
    elif bg_current == "bg_dangerroom":
        scene bg_danger onlayer backdrop
    elif bg_current == "bg_showerroom":
        scene bg_shower onlayer backdrop
    elif bg_current == "bg_study":
        scene bg_study onlayer backdrop
    elif bg_current == "bg_movies":
        scene bg_movies onlayer backdrop
    elif bg_current == "bg_restaurant":
        scene bg_rest onlayer backdrop
    elif bg_current == "bg_pool":
        scene bg_pool onlayer backdrop
    elif bg_current == "bg_mall":
        scene bg_mall onlayer backdrop
    elif bg_current == "bg_shop":
        scene bg_shop onlayer backdrop
    elif bg_current == "bg_dressing":
        scene bg_dressing onlayer backdrop
    elif bg_current == "HW Party":
        scene bg_halloween onlayer backdrop
    else:
        scene bg_campus onlayer backdrop

    scene
    
    return

image bg_entry = "images/Door.jpg"
image bg_player:
    contains:
        ConditionSwitch(
                "time_index >= 3", "images/sky_night.jpg",
                "time_index == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
    contains:
        "images/playerroom.png"











image bg_rogue:
    LiveComposite(
            (1024,768),
            (0,0), ConditionSwitch(

                "time_index >= 3", "images/sky_night.jpg",
                "time_index == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                ),
            (0,0), "images/rogueroom.png"
            )

image bg_kitty:
    contains:
        ConditionSwitch(
                "time_index >= 3", "images/sky_night.jpg",
                "time_index == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
    contains:
        "images/kittyroom.png"

image bg_emma:
    contains:
        ConditionSwitch(
                "time_index >= 3", "images/sky_night.jpg",
                "time_index == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
    contains:
        "images/emmaroom.png"

image bg_laura:
    contains:
        ConditionSwitch(
                "time_index >= 3", "images/sky_night.jpg",
                "time_index == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
    contains:
        "images/lauraroom.png"

image bg_jean:
    contains:
        ConditionSwitch(
                "time_index >= 3", "images/sky_night.jpg",
                "time_index == 2", "images/sky_sunset.jpg",
                "True", "images/sky_day.jpg",
                )
    contains:
        "images/jeanroom.png"

image bg_storm:
    contains:
        ConditionSwitch(
                "time_index >= 3", "images/stormroom_night.png",
                "time_index == 2", "images/stormroom_evening.png",
                "True", "images/stormroom_day.png",
                )

image bg_jubes:
    contains:
        "images/jubesroom.png",

image bg_campus:
    contains:
        ConditionSwitch(
                "time_index >= 3",      "images/Campus_Night.png",
                "time_index == 2",    "images/Campus_Evening.png",
                "True",                         "images/Campus_Day.png",
                )

image bg_pool:
    contains:
        ConditionSwitch(
                "time_index >= 3",      "images/pool_night.png",
                "time_index == 2",    "images/pool_evening.png",
                "True",                         "images/pool_day.png",
                )

image bg_class:
    contains:
        "images/Classroom.jpg"
    contains:
        ConditionSwitch(
                "EmmaX.location == 'bg_teacher' and 'frisky' in EmmaX.recent_history", "Emma_Behind_Podium",
                "EmmaX.location == 'bg_teacher'", "Emma_At_Podium",
                "EmmaX.location == 'bg_desk'", "Emma_At_Desk",
                "StormX.location == 'bg_teacher' and 'frisky' in StormX.recent_history", "Storm_Behind_Podium",
                "StormX.location == 'bg_teacher'", "Storm_At_Podium",
                "StormX.location == 'bg_desk'", "Storm_At_Desk",
                "True", Null(),
                )
    contains:

        "images/ClassroomFront.png"
    contains:
        ConditionSwitch(
                "bg_current != 'bg_classroom' or time_index >= 2 or Weekday >= 5", Null(),
                "True", "images/ClassroomPupils.png",
                )

image empty_class:
    contains:
        "images/Classroom.jpg"

image bg_study:
    contains:
        ConditionSwitch(
                "time_index > 2",      "images/StudyNight.jpg",
                "True",                         "images/StudyDay.jpg",
                )
image bg_mall:
    contains:
        ConditionSwitch(
                "time_index > 1",      "images/mall_night.png",
                "True",                         "images/mall_day.png",
                )



image bg_halloween = "images/HalloweenParty.jpg"
image bg_danger = "images/dangerroom.jpg"
image bg_shower = "images/Shower.jpg"

image bg_movies = "images/Movies.jpg"
image bg_rest = "images/Restaurant.jpg"
image bg_shop = "images/Shop.jpg"
image bg_dressing = "images/Dressingroom.jpg"


label RoomMask:
    if bg_current == "bg_player":
        show bg_playermask onlayer black:
            alpha .2
    elif bg_current == "bg_rogue":
        show bg_roguemask onlayer black:
            alpha .2
    elif bg_current == "bg_kitty":
        show bg_kittymask onlayer black:
            alpha .2
    elif bg_current == "bg_emma":
        show bg_emmamask onlayer black:
            alpha .2
    elif bg_current == "bg_laura":
        show bg_lauramask onlayer black:
            alpha .2
    elif bg_current == "bg_jean":
        show bg_jeanmask onlayer black:
            alpha .2
    elif bg_current == "bg_storm":
        show bg_stormmask onlayer black:
            alpha .2
    elif bg_current == "bg_jubes":
        show bg_jubesmask onlayer black:
            alpha .2
    return

image bg_playermask = "images/playerroom.png"

image bg_roguemask = "images/Rogueroom.png"

image bg_kittymask = "images/kittyroom.png"

image bg_emmamask = "images/emmaroom.png"

image bg_lauramask = "images/lauraroom.png"

image bg_jeanmask = "images/jeanroom.png"

image bg_stormmask = "images/stormroom_day.png"

image bg_jubesmask = "images/jubesroom.png"

image bg_classmask = "images/Classroom.jpg"







image Rogue_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.Sprite", "Rogue_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Top",
                    "action_speed ", "Rogue_Doggy_Anal_Head_Top",
                    "True", "Rogue_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Top",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Top",
                    "True", "Rogue_Doggy_Body",
                    ),
            "True", "Rogue_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite", "Rogue_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "action_speed ", "Rogue_Doggy_Anal_Head_Ass",
                    "True", "Rogue_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Rogue_Doggy_Fuck_Ass",
                    "True", "Rogue_Doggy_Ass",
                    ),
            "True", "Rogue_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.Cock == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Rogue_Doggy_Feet2",
                    "action_speed ", "Rogue_Doggy_Feet1",
                    "True", "Rogue_Doggy_Feet0",
                    ),
            "not Player.Sprite and ShowFeet", "Rogue_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)


image Rogue_Doggy_Body = LiveComposite(
        (420,750),
        (0,0), ConditionSwitch(

            "RogueX.Water", Null(),
            "RogueX.hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairB.png",
            "True", Null(),
            ),
        (0,0), "images/RogueDoggy/Rogue_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "RogueX.neck == 'spiked_collar'", "images/RogueDoggy/Rogue_Doggy_Collar.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'mouth' in RogueX.Spunk", ConditionSwitch(
                    "RogueX.mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_LipbiteW.png",
                    "RogueX.mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_SurprisedW.png",
                    "RogueX.mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_BlowW.png",
                    "RogueX.mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_SadW.png",
                    "RogueX.mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_SmileW.png",
                    "RogueX.mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_TongueW.png",
                    "True", "images/RogueDoggy/Rogue_Doggy_Mouth_NormalW.png",
                    ),
            "RogueX.mouth == 'normal'", "images/RogueDoggy/Rogue_Doggy_Mouth_Normal.png",
            "RogueX.mouth == 'lipbite'", "images/RogueDoggy/Rogue_Doggy_Mouth_Lipbite.png",
            "RogueX.mouth == 'sucking'", "images/RogueDoggy/Rogue_Doggy_Mouth_Blow.png",
            "RogueX.mouth == 'kiss'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",
            "RogueX.mouth == 'sad'", "images/RogueDoggy/Rogue_Doggy_Mouth_Sad.png",
            "RogueX.mouth == 'smile'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "RogueX.mouth == 'grimace'", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            "RogueX.mouth == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Mouth_Surprised.png",
            "RogueX.mouth == 'tongue'", "images/RogueDoggy/Rogue_Doggy_Mouth_Tongue.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(

            "RogueX.blushing", "images/RogueDoggy/Rogue_Doggy_Blush.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.brows == 'normal'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "RogueX.brows == 'angry'", "images/RogueDoggy/Rogue_Doggy_Brows_Angry.png",
            "RogueX.brows == 'sad'", "images/RogueDoggy/Rogue_Doggy_Brows_Sad.png",
            "RogueX.brows == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Brows_Surprised.png",
            "RogueX.brows == 'confused'", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Brows_Normal.png",
            ),
        (0,0), "Rogue Doggy Blink",
        (0,0), ConditionSwitch(

            "not RogueX.bra", Null(),
            "RogueX.bra == 'tube_top'", "images/RogueDoggy/Rogue_Doggy_Chest_Tube.png",
            "RogueX.bra == 'tank'", "images/RogueDoggy/Rogue_Doggy_Chest_Tank.png",
            "RogueX.bra == 'buttoned tank'", "images/RogueDoggy/Rogue_Doggy_Chest_ButtonTank.png",
            "RogueX.bra == 'sports_bra'", "images/RogueDoggy/Rogue_Doggy_Chest_SportsBra.png",
            "RogueX.bra == 'bikini_top'", "images/RogueDoggy/Rogue_Doggy_Chest_Bikini.png",
            "RogueX.bra", "images/RogueDoggy/Rogue_Doggy_Chest_Bra.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not RogueX.top", Null(),
            "RogueX.top == 'mesh_top'", "images/RogueDoggy/Rogue_Doggy_Over_Mesh.png",
            "RogueX.top == 'pink_top'", "images/RogueDoggy/Rogue_Doggy_Over_Pink.png",
            "RogueX.top == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hoodie.png",
            "RogueX.top == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyTop.png",
            "RogueX.top == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_HairWet.png",
            "RogueX.hair == 'cosplay'", "images/RogueDoggy/Rogue_Doggy_Hair_Cos.png",
            "RogueX.hair == 'evo'", "images/RogueDoggy/Rogue_Doggy_HairF.png",
            "True", "images/RogueDoggy/Rogue_Doggy_HairF.png",
            ),
        (0,0), ConditionSwitch(

            "RogueX.top == 'hoodie'", "images/RogueDoggy/Rogue_Doggy_Over_Hood.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not RogueX.Spunk", Null(),
            "'hair' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_Spunk_Hair.png",
            "'facial' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Rogue_Doggy_GropeBreast",
            "True", Null()
            ),
        )

image Rogue_Doggy_Ass = LiveComposite(
        (420,750),
        (0,0), ConditionSwitch(

            "not RogueX.underwearDown or (RogueX.legs == 'pants' and not RogueX.Upskirt)", Null(),
            "RogueX.underwear == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Back.png",
            "RogueX.underwear == 'green_panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Back.png",
            "RogueX.underwear == 'bikini_bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Back.png",
            "RogueX.underwear", "images/RogueDoggy/Rogue_Doggy_Panties_Back.png",
            "True", Null(),
            ),
        (0,0), "images/RogueDoggy/Rogue_Doggy_Ass.png",
        (0,0), ConditionSwitch(

            "RogueX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Hose.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not RogueX.underwearDown or (RogueX.legs == 'pants' and not RogueX.Upskirt)", Null(),
            "RogueX.underwear == 'shorts' and RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Shorts_Down_Wet.png",
            "RogueX.underwear == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts_Down.png",
            "RogueX.underwear == 'green_panties' and RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Undies_Down_Wet.png",
            "RogueX.underwear == 'green_panties'", "images/RogueDoggy/Rogue_Doggy_Undies_Down.png",
            "RogueX.underwear == 'bikini_bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini_Down.png",
            "RogueX.underwear", "images/RogueDoggy/Rogue_Doggy_Panties_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Pussy_Fucking3",
                    "action_speed > 1", "Rogue_Pussy_Fucking2",
                    "action_speed ", "Rogue_Pussy_Heading",
                    "True", "Rogue_Pussy_Static",
                    ),
            "primary_action == 'eat_pussy'", "images/RogueDoggy/Rogue_Doggy_Pussy_Open.png",
            "RogueX.legs and not RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png",
            "RogueX.underwear and not RogueX.underwearDown", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Rogue_Pussy_Fingering",
            "primary_action == 'dildo_pussy'", "Rogue_Pussy_Fucking2",
            "True", "images/RogueDoggy/Rogue_Doggy_Pussy_Closed.png",
            ),









        (0,0), ConditionSwitch(

            "not RogueX.pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "RogueX.legs == 'pants' and not RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "RogueX.underwearDown", "images/RogueDoggy/Rogue_Doggy_Pubes.png",
            "RogueX.underwear", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "RogueX.hose and RogueX.hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "RogueX.piercings == 'ring'", "images/RogueDoggy/Rogue_Doggy_PussyRing.png",
            "RogueX.piercings == 'barbell'", "images/RogueDoggy/Rogue_Doggy_PussyBarbell.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Rogue_Anal_Fucking2",
                    "action_speed > 1", "Rogue_Anal_Fucking",
                    "action_speed ", "Rogue_Anal_Heading",
                    "True", "Rogue_Anal",
                    ),


            "RogueX.legs and not RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",
            "RogueX.underwear and not RogueX.underwearDown", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Rogue_Anal_Fingering",
            "primary_action == 'dildo_anal'", "Rogue_Anal_Fucking",
            "RogueX.used_to_anal", "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(

            "'anal' not in RogueX.Spunk or Player.Sprite", Null(),
            "Player.Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",
            "RogueX.used_to_anal", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            "True", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(

            "RogueX.underwearDown or not RogueX.underwear", Null(),


            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "RogueX.underwear == 'shorts' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Shorts_Wet.png",
            "RogueX.underwear == 'shorts'", "images/RogueDoggy/Rogue_Doggy_Shorts.png",
            "RogueX.underwear == 'green_panties' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Undies_Wet.png",
            "RogueX.underwear == 'green_panties'", "images/RogueDoggy/Rogue_Doggy_Undies.png",
            "RogueX.underwear == 'lace_panties'", "images/RogueDoggy/Rogue_Doggy_PantiesLace.png",
            "RogueX.underwear == 'bikini_bottoms'", "images/RogueDoggy/Rogue_Doggy_Panties_Bikini.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Panties.png",
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'tights' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
            "RogueX.hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
            "RogueX.hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.legs == 'pants'", ConditionSwitch(
                    "RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Down.png",
                    "RogueX.Wet > 1", "images/RogueDoggy/Rogue_Doggy_Legs_Pants_Wet.png",
                    "True", "images/RogueDoggy/Rogue_Doggy_Legs_Pants.png",
                    ),
            "RogueX.legs == 'skirt'", ConditionSwitch(
                    "RogueX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt_Up.png",
                    "True", "images/RogueDoggy/Rogue_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.top == 'nighty' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss_Up.png",
            "RogueX.top == 'nighty'", "images/RogueDoggy/Rogue_Doggy_Over_NightyAss.png",
            "RogueX.top == 'towel' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss_Up.png",
            "RogueX.top == 'towel'", "images/RogueDoggy/Rogue_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "RogueX.accessory == 'sweater' and (RogueX.Upskirt or (Player.Sprite and Player.Cock == 'out'))", "images/RogueDoggy/Rogue_Doggy_Acc_Sweater_Up.png",
            "RogueX.accessory == 'sweater'", "images/RogueDoggy/Rogue_Doggy_Acc_Sweater.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in RogueX.Spunk", "images/RogueDoggy/Rogue_Doggy_SpunkAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'eat_pussy'", "Rogue_Doggy_Lick_Pussy",
            "primary_action == 'eat_ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "RogueX.legs == 'skirt' and RogueX.Upskirt", "images/RogueDoggy/Rogue_Doggy_HotdogUpskirtBack.png",
            "True", "images/RogueDoggy/Rogue_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "RogueX.legs == 'skirt' and RogueX.Upskirt and action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "RogueX.legs == 'skirt' and RogueX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "action_speed ", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )

image Rogue Doggy Blink:
    ConditionSwitch(
    "RogueX.eyes == 'sexy'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "RogueX.eyes == 'side'", "images/RogueDoggy/Rogue_Doggy_Eyes_Side.png",
    "RogueX.eyes == 'normal'", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
    "RogueX.eyes == 'closed'", "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png",
    "RogueX.eyes == 'manic'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "RogueX.eyes == 'down'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "RogueX.eyes == 'stunned'", "images/RogueDoggy/Rogue_Doggy_Eyes_Stunned.png",
    "RogueX.eyes == 'surprised'", "images/RogueDoggy/Rogue_Doggy_Eyes_Surprised.png",
    "RogueX.eyes == 'squint'", "images/RogueDoggy/Rogue_Doggy_Eyes_Sexy.png",
    "True", "images/RogueDoggy/Rogue_Doggy_Eyes_Normal.png",
    ),






    3

    "images/RogueDoggy/Rogue_Doggy_Eyes_Closed.png"
    .25
    repeat


image Rogue_Doggy_Feet:
    contains:
        AlphaMask("Rogue_Doggy_Shins", "images/RogueDoggy/Rogue_Doggy_Toes.png")

image Rogue_Doggy_Shins:

    contains:
        "images/RogueDoggy/Rogue_Doggy_Shins.png"
    contains:

        ConditionSwitch(
            "RogueX.legs == 'pants'", "images/RogueDoggy/Rogue_Doggy_Feet_Pants.png",
            "True", Null(),
            )
    contains:
        "images/RogueDoggy/Rogue_Doggy_Feet.png"
    contains:

        ConditionSwitch(
            "not RogueX.hose", Null(),
            "RogueX.hose == 'stockings'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",
            "RogueX.hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights.png",
            "RogueX.hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose.png",
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_Feet_Hose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Feet_Tights_Holed.png",
            "True", Null(),
            )


image Rogue_Doggy_Lick_Pussy:
    "Lick_Anim"
    zoom 0.5
    offset (195,540)

image Rogue_Doggy_Lick_Ass:
    "Lick_Anim"
    zoom 0.5
    offset (195,500)

image Rogue_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (150,340)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat


image Zero_Doggy_Up:

    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png",
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null(),
            ),

image Zero_Hotdog_Static:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Hotdog_Moving:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat



image Zero_Doggy_Insert:

    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png",
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",
            "True", Null(),
            ),












image Zero_Doggy_Static:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Doggy_Heading:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Doggy_Fucking2:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Doggy_Fucking3:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Rogue_Pussy_Mask:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Rogue_Pussy_Mask_Static:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat


































image Rogue_Pussy_Static:

    subpixel True
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Doggy_Static", "Rogue_Pussy_Mask_Static")
    contains:


        AlphaMask("Rogue_PussyHole_Static", "Rogue_Pussy_Hole_Mask_Static")

image Rogue_Pussy_Hole_Mask_Static:

    contains:

        AlphaMask("images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Rogue_PussyHole_Static:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Rogue_Pussy_Heading:

    subpixel True
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Doggy_Heading", "Rogue_Pussy_Mask")
    contains:


        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")


image Rogue_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Rogue_Pussy_Heading_Flap:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat


image Rogue_Pussy_Fingering:

    subpixel True
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .9
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
    contains:


        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")

image Zero_Pussy_Finger:

    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat



image Rogue_Pussy_Fucking2:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:




        ConditionSwitch(
            "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),


image Rogue_Pussy_Fucking3:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")

image Rogue_Doggy_Fucking_Dildo:

    contains:
        "images/DildoIn.png"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat





image Rogue_Anal:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:

        "Zero_Doggy_Insert"
        pos (172,500)



image Rogue_Anal_Fingering:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:




        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")

image Zero_Doggy_Anal_Finger:

    contains:
        "images/UI_Fingering.png",
        pos (172,480)
        block:
            ease .5 ypos 460
            pause .25
            ease 1.75 ypos 480
            repeat

image Rogue_Doggy_Anal_Fingering_Mask:

    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"

        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat


image Rogue_Anal_Heading:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal_Heading", "Zero_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Doggy_Anal_Heading", "Rogue_Doggy_Anal_Heading_Mask")

image Zero_Doggy_Anal_Heading:

    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600
            repeat

image Rogue_Doggy_Anal_Heading_Mask:

    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            ease .5 zoom 1
            pause .5
            ease 1.5 zoom .5
            repeat

image Rogue_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Rogue_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat


image Zero_Doggy_Anal1:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat





























image Rogue_Anal_Fucking:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:

        ConditionSwitch(

            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),

image Rogue_Doggy_Anal_Dildo:

    contains:
        "images/DildoIn.png"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat


image Rogue_Doggy_Anal_FullMask:
    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )

image Rogue_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 15
        pause .4
        block:
            ease .2 ypos 5
            pause .3
            ease 2 ypos 15
            repeat

image Rogue_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15
            ease .1 ypos -5
            pause .2
            ease 1.6 ypos 0
            repeat



image Zero_Doggy_Anal2:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Rogue_Anal_Fucking2:

    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:

        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
    contains:




        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "RogueX.hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.underwear and RogueX.underwearDown", Null(),
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Rogue_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Rogue_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




image Rogue_Doggy_Feet0:

    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0)
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (145,480)
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0)
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Rogue_Doggy_Feet1:

    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Rogue_Doggy_Feet2:

    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat




image Slap_Ass:
    contains:
        "SlapHand"
        pause 1.2
        Null()

image Slap_Ass:
    contains:
        "UI_Hand"
        subpixel True
        zoom 1
        alpha 0.5
        anchor (0.5,0.5)
        pos (600,380)
        rotate 40
        block:
            parallel:
                ease .5 xpos 300 rotate 80
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9

image NotSlap_Ass:
    contains:
        subpixel True
        "UI_Hand"
        zoom 1
        pos (600,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            pos (600,380)
            rotate 40
            parallel:
                ease .5 xpos 300 rotate 80
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9
            repeat




label Rogue_Doggy_Launch(Line=primary_action):
    if renpy.showing("Rogue_Doggy_Animation"):
        return
    $ action_speed = 0
    call Rogue_Hide (1)
    show Rogue_Doggy_Animation zorder 150 at sprite_location(stage_center+50)
    with dissolve
    return

label Rogue_Doggy_Reset:
    if not renpy.showing("Rogue_Doggy_Animation"):
        return

    $ RogueX.ArmPose = 2
    $ RogueX.SpriteVer = 0
    hide Rogue_Doggy_Animation
    call Rogue_Hide
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return










image Rogue_SexSprite:
    LiveComposite(
        (1120,840),
        (0,0), ConditionSwitch(

                "not Player.Sprite", "Rogue_Sex_Body_Static",
                "Player.Cock == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Rogue_Sex_Body_Anim3",
                        "action_speed >= 2", "Rogue_Sex_Body_Anim2",
                        "action_speed ", "Rogue_Sex_Body_Anim1",
                        "True", "Rogue_Sex_Body_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Rogue_Sex_Body_Anim3",
                        "action_speed >= 2", "Rogue_Sex_Body_Anim2",
                        "action_speed ", "Rogue_Sex_Body_Anim1",
                        "True", "Rogue_Sex_Body_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(

                        "action_speed >= 2", "Rogue_Sex_Body_FootAnim2",
                        "action_speed ", "Rogue_Sex_Body_FootAnim1",
                        "True", "Rogue_Sex_Body_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and action_speed >= 2","Rogue_Hotdog_Body_Anim2",
                "True", "Rogue_Sex_Body_Static",
                ),
        (0,0), ConditionSwitch(
                "not Player.Sprite", "Rogue_Sex_Legs_Static",
                "Player.Cock == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Rogue_Sex_Legs_Anim3",
                        "action_speed >= 2", "Rogue_Sex_Legs_Anim2",
                        "action_speed ", "Rogue_Sex_Legs_Anim1",
                        "True", "Rogue_Sex_Legs_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Rogue_Sex_Legs_Anim3",
                        "action_speed >= 2", "Rogue_Sex_Legs_Anim2",
                        "action_speed ", "Rogue_Sex_Legs_Anim1",
                        "True", "Rogue_Sex_Legs_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(

                        "action_speed >= 2", "Rogue_Sex_Legs_FootAnim2",
                        "action_speed ", "Rogue_Sex_Legs_FootAnim1",
                        "True", "Rogue_Sex_Legs_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and action_speed >= 2","Rogue_Hotdog_Legs_Anim2",
                "True", "Rogue_Sex_Legs_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,200)
    zoom 0.85

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

        (1120,840),





        (320,-135), "Rogue_HairBack_Sex",
        (0,0), ConditionSwitch(

            "RogueX.piercings == 'barbell'", "images/RogueSex/Rogue_Sex_Body_Barbell.png",
            "RogueX.piercings == 'ring'", "images/RogueSex/Rogue_Sex_Body_Ring.png",
            "True", "images/RogueSex/Rogue_Sex_Body.png",
            ),

        (0,0), ConditionSwitch(

            "not RogueX.bra", Null(),
            "RogueX.Uptop", ConditionSwitch(

                    "RogueX.bra == 'tank'", "images/RogueSex/Rogue_Sex_Chest_Tank_Up.png",
                    "RogueX.bra == 'tube_top'", "images/RogueSex/Rogue_Sex_Chest_Tube_Up.png",
                    "RogueX.bra == 'buttoned tank'", "images/RogueSex/Rogue_Sex_Chest_ButtonTank_Up.png",
                    "RogueX.bra == 'sports_bra'", "images/RogueSex/Rogue_Sex_Chest_SportsBra_Up.png",
                    "RogueX.bra == 'bra'", "images/RogueSex/Rogue_Sex_Chest_Bra_Up.png",
                    "RogueX.bra == 'bikini_top'", "images/RogueSex/Rogue_Sex_Chest_Bikini_Up.png",
                    "RogueX.bra == 'lace_bra'", "images/RogueSex/Rogue_Sex_Chest_Bra_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "RogueX.bra == 'tank'", "images/RogueSex/Rogue_Sex_Chest_Tank.png",
                    "RogueX.bra == 'tube_top'", "images/RogueSex/Rogue_Sex_Chest_Tube.png",
                    "RogueX.bra == 'buttoned tank'", "images/RogueSex/Rogue_Sex_Chest_ButtonTank.png",
                    "RogueX.bra == 'sports_bra'", "images/RogueSex/Rogue_Sex_Chest_SportsBra.png",
                    "RogueX.bra == 'bra'", "images/RogueSex/Rogue_Sex_Chest_Bra.png",
                    "RogueX.bra == 'bikini_top'", "images/RogueSex/Rogue_Sex_Chest_Bikini.png",
                    "RogueX.bra == 'lace_bra'", "images/RogueSex/Rogue_Sex_Chest_LaceBra.png",
                    "True", Null(),
                    ),
            ),
        (0,0),ConditionSwitch(

            "RogueX.Water", "images/RogueSex/Rogue_Sex_Wet_Body.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not RogueX.top", Null(),
            "RogueX.Uptop", ConditionSwitch(

                    "RogueX.top == 'pink_top'", "images/RogueSex/Rogue_Sex_Over_Pink_Up.png",
                    "RogueX.top == 'mesh_top'", "images/RogueSex/Rogue_Sex_Over_Mesh_Up.png",

                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "RogueX.top == 'pink_top'", "images/RogueSex/Rogue_Sex_Over_Pink.png",
                    "RogueX.top == 'mesh_top'", "images/RogueSex/Rogue_Sex_Over_Mesh.png",

                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "RogueX.Uptop or (not RogueX.top and not RogueX.bra)", Null(),
            "RogueX.piercings == 'barbell'", "images/RogueSex/Rogue_Sex_Pierce_BarbellC.png",
            "RogueX.piercings == 'ring'", "images/RogueSex/Rogue_Sex_Pierce_RingC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.neck == 'spiked_collar'", "images/RogueSex/Rogue_Sex_Neck_Stud.png",
            "True", Null(),
            ),








        (0,0),ConditionSwitch(

            "'belly' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Body.png",
            "True", Null(),
            ),
        (0,80),ConditionSwitch(

            "'tits' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Rogue_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Rogue_Sex_Fondle_Breasts",
            "True", Null()
            ),
        (320,-135), "Rogue_Head_Sex",
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

    "Rogue_Head"
    zoom 1.28
    anchor (0.5,0.5)
    rotate -10

image Rogue_HairBack_Sex:

    "Rogue_HairBack"
    zoom 1.28
    anchor (0.5,0.5)
    rotate -10



image Rogue_Sex_Legs:
    LiveComposite(

        (1120,840),
        (0,0), "images/RogueSex/Rogue_Sex_Legs.png",

        (0,0),ConditionSwitch(

            "RogueX.Water", "images/RogueSex/Rogue_Sex_Wet_Legs.png",
            "True", Null(),
            ),
        (0,0), "Rogue_Sex_Anus",


        (0,0), "Rogue_Sex_Pussy",


        (0,0), ConditionSwitch(

            "not RogueX.underwear or RogueX.underwearDown", Null(),
            "Player.Sprite and (Player.Cock == 'sex' or Player.Cock == 'anal')", Null(),
            "RogueX.underwear == 'lace_panties'", "images/RogueSex/Rogue_Sex_Panties_Lace.png",
            "RogueX.underwear == 'green_panties' and RogueX.Wet", "images/RogueSex/Rogue_Sex_Panties_Green_Wet.png",
            "RogueX.underwear == 'green_panties' or RogueX.underwear == 'bikini_bottoms'", "images/RogueSex/Rogue_Sex_Panties_Green.png",
            "RogueX.underwear == 'shorts' and RogueX.Wet", "images/RogueSex/Rogue_Sex_Panties_Shorts_Wet.png",
            "RogueX.underwear == 'shorts'", "images/RogueSex/Rogue_Sex_Panties_Shorts.png",
            "RogueX.Wet", "images/RogueSex/Rogue_Sex_Panties_Black_Wet.png",
            "True", "images/RogueSex/Rogue_Sex_Panties_Black.png",
            ),

        (0,0), ConditionSwitch(


            "RogueX.hose == 'ripped_pantyhose'", "images/RogueSex/Rogue_Sex_Hose_Legs_Full_Hole.png",
            "RogueX.hose == 'ripped_tights'", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Hole.png",
            "RogueX.hose == 'stockings'", "images/RogueSex/Rogue_Sex_Hose_Legs_Stockings.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueSex/Rogue_Sex_Hose_Legs_StockingGarter.png",
            "RogueX.hose == 'garterbelt'", "images/RogueSex/Rogue_Sex_Hose_Legs_Garter.png",
            "RogueX.underwearDown", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "RogueX.hose == 'pantyhose'", "images/RogueSex/Rogue_Sex_Hose_Legs_Full.png",
            "RogueX.hose == 'tights' and RogueX.Wet", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights_Wet.png",
            "RogueX.hose == 'tights'", "images/RogueSex/Rogue_Sex_Hose_Legs_Tights.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.legs == 'skirt'", "images/RogueSex/Rogue_Sex_Legs_Skirt.png",
            "RogueX.Upskirt", Null(),
            "RogueX.legs == 'pants' and RogueX.Wet > 1", "images/RogueSex/Rogue_Sex_Legs_Pants_Wet.png",
            "RogueX.legs == 'pants'","images/RogueSex/Rogue_Sex_Legs_Pants.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "RogueX.accessory == 'sweater'", "images/RogueSex/Rogue_Sex_Sweater.png",
            "True", Null(),
            ),





        (0,0),ConditionSwitch(

            "'belly' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "action_speed >= 2", "Rogue_Hotdog_Zero_Anim2",
            "action_speed ", "Rogue_Hotdog_Zero_Anim1",
            "True", "Rogue_Hotdog_Zero_Anim0",
            ),

        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'eat_pussy'", "Rogue_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Rogue_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite or Player.Cock != 'foot'", Null(),
            "action_speed >= 2", "Rogue_Footcock_Zero_Anim2",
            "action_speed ", "Rogue_Footcock_Zero_Anim1",
            "True", "Rogue_Footcock_Static",
            ),













        (0,0), ConditionSwitch(

            "not action_speed or Player.Cock == 'foot' or ShowFeet", "Rogue_Sex_Feet",

            "True", AlphaMask("Rogue_Sex_Feet","images/RogueSex/Rogue_Sex_FeetMask2.png")
            ),
        )


image Rogue_Sex_Feet = LiveComposite(

        (1120,840),
        (0,0), "images/RogueSex/Rogue_Sex_Feet.png",
        (0,0),ConditionSwitch(

            "RogueX.Water", "images/RogueSex/Rogue_Sex_Wet_Feet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not RogueX.hose", Null(),
            "RogueX.hose == 'ripped_tights'", "images/RogueSex/Rogue_Sex_Hose_Feet_Tights_Hole.png",
            "RogueX.hose == 'ripped_pantyhose'", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking_Hole.png",
            "RogueX.hose == 'stockings_and_garterbelt'", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png",
            "RogueX.hose == 'stockings'", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png",
            "RogueX.underwearDown", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "RogueX.hose == 'tights'", "images/RogueSex/Rogue_Sex_Hose_Feet_Tights.png",
            "RogueX.hose == 'garterbelt'", Null(),
            "True", "images/RogueSex/Rogue_Sex_Hose_Feet_Stocking.png",
            ),
        (0,0), ConditionSwitch(

            "not RogueX.underwear or not RogueX.underwearDown", Null(),
            "RogueX.legs == 'pants'", Null(),

            "RogueX.underwear == 'lace_panties'", "images/RogueSex/Rogue_Sex_Panties_Lace_Down.png",
            "RogueX.underwear == 'green_panties'", "images/RogueSex/Rogue_Sex_Panties_Green_Down.png",
            "RogueX.underwear == 'bikini_bottoms'", "images/RogueSex/Rogue_Sex_Panties_Bikini_Down.png",
            "RogueX.underwear == 'shorts'", "images/RogueSex/Rogue_Sex_Panties_Shorts_Down.png",
            "True", "images/RogueSex/Rogue_Sex_Panties_Black_Down.png",
            ),

        (0,0), ConditionSwitch(

            "RogueX.legs == 'pants' and RogueX.Upskirt", "images/RogueSex/Rogue_Sex_Legs_Pants_Down.png",
            "RogueX.legs == 'pants'", "images/RogueSex/Rogue_Sex_Legs_Pants_Feet.png",
            "True", Null(),
            ),
        )



image Rogue_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.7
    offset (530,510)

image Rogue_Sex_Lick_Ass:
    "Lick_Anim"
    zoom 0.7
    offset (535,590)

image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image Rogue_Sex_Pussy_Fucking0:

    contains:

        "images/RogueSex/Rogue_Sex_Pussy_Open.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Rogue_Sex_Zero_Anim0", "Rogue_Pussy_Open_Mask")

image Rogue_Sex_Pussy_Fucking1:

    contains:

        "images/RogueSex/Rogue_Sex_Pussy_Open.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Rogue_Sex_Zero_Anim1", "Rogue_Pussy_Open_Mask")

image Rogue_Sex_Pussy_Fucking2:

    contains:

        "images/RogueSex/Rogue_Sex_Pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Rogue_Sex_Zero_Anim2", "Rogue_Pussy_Fucking_Mask")

image Rogue_Sex_Pussy_Fucking3:

    contains:

        "images/RogueSex/Rogue_Sex_Pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Rogue_Sex_Zero_Anim3", "Rogue_Pussy_Fucking_Mask")

image Rogue_Pussy_Fucking_Mask:

    contains:
        "images/RogueSex/Rogue_Sex_Pussy_Mask.png"

image Rogue_Pussy_Open_Mask:

    contains:
        "images/RogueSex/Rogue_Sex_Pussy_Mask.png"
        yoffset 3

image Rogue_Sex_Pussy_Spunk_Heading:
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8

image Rogue_Sex_Pussy:

    contains:

        ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and action_speed", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                "primary_action == 'dildo_pussy'", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                "primary_action == 'eat_pussy' or primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                )
    contains:

        ConditionSwitch(
                "not RogueX.Wet", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:

        ConditionSwitch(
                "RogueX.piercings != 'ring'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or action_speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Ring.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_RingF.png",
                )
    contains:

        ConditionSwitch(
                "RogueX.piercings != 'barbell'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or action_speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Barbell.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png",
                )
    contains:

        ConditionSwitch(
                "not RogueX.pubes", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and action_speed", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/RogueSex/Rogue_Sex_Pubes_Closed.png",
                "primary_action == 'eat_pussy' or primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                "primary_action == 'dildo_pussy'", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                "True", "images/RogueSex/Rogue_Sex_Pubes_Closed.png",
                )
    contains:

        ConditionSwitch(
                "'in' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 3", AlphaMask("Rogue_Sex_Zero_Anim3", "Rogue_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", AlphaMask("Rogue_Sex_Zero_Anim2", "Rogue_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and action_speed", AlphaMask("Rogue_Sex_Zero_Anim1", "Rogue_Pussy_Open_Mask"),
                "Player.Sprite and Player.Cock == 'in'", AlphaMask("Rogue_Sex_Zero_Anim0", "Rogue_Pussy_Open_Mask"),
                "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", AlphaMask("Rogue_Sex_FingerP_Anim1", "Rogue_Pussy_Open_Mask"),
                "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Sex_Dildo_Anim2", "Rogue_Pussy_Fucking_Mask"),
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "'in' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'in' or not action_speed", Null(),
                "action_speed <= 1", "Rogue_Sex_Pussy_Spunk_Heading",
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",
                )





image Rogue_Sex_FingerP_Anim1:

    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (507,520)
        zoom 1.2
        block:
            ease .2 ypos 480
            pause .2
            ease .6 ypos 520
            repeat

image Rogue_Sex_Dildo_Anim2:

    contains:
        subpixel True
        "images/DildoIn.png"
        pos (504,490)
        zoom 1.3
        block:
            ease 1 ypos 380
            pause 1
            ease 3 ypos 490
            repeat


image Rogue_Sex_Zero_Anim0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (503,530)
        zoom 1.3

image Rogue_Sex_Zero_Anim1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (503,525)
        zoom 1.3
        block:
            ease 1 ypos 510
            pause 1
            ease 3 ypos 525
            repeat

image Rogue_Sex_Zero_Anim2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (504,490)
        zoom 1.3
        block:
            ease 1 ypos 380
            pause 1
            ease 3 ypos 490
            repeat

image Rogue_Sex_Zero_Anim3:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (504,490)
        zoom 1.3
        block:
            ease .25 ypos 380
            pause .25
            ease 1.5 ypos 490
            repeat



image Rogue_Sex_Legs_Anim1:

    contains:
        subpixel True
        "Rogue_Sex_Legs"
        pos (0,0)
        block:

            pause .25
            easein 1 pos (0,-5)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Rogue_Sex_Legs_Anim2:

    contains:
        subpixel True
        "Rogue_Sex_Legs"
        pos (0,0)
        block:

            pause .5
            easein .5 pos (0,-15)
            ease .25 pos (0,-10)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Rogue_Sex_Legs_Anim3:

    contains:
        subpixel True
        "Rogue_Sex_Legs"
        pos (0,0)
        block:

            pause .15
            easein .15 pos (0,-20)
            ease .10 pos (0,-15)
            pause .20
            ease 1.4 pos (0,0)
            repeat



image Rogue_Sex_Body_Anim1:

    contains:
        subpixel True
        "Rogue_Sex_Body"
        pos (0,0)
        block:

            pause .5
            easein .75 pos (0,-5)
            pause 1.25
            ease 2.5 pos (0,0)
            repeat

image Rogue_Sex_Body_Anim2:

    contains:
        subpixel True
        "Rogue_Sex_Body"
        pos (0,0)
        block:

            pause .6
            easein .4 pos (0,-10)
            ease .25 pos (0,-5)
            pause 1
            ease 2.75 pos (0,10)
            repeat

image Rogue_Sex_Body_Anim3:

    contains:
        subpixel True
        "Rogue_Sex_Body"
        pos (0,0)
        block:

            pause .17
            easein .13 pos (0,-20)
            ease .10 pos (0,-15)
            pause .20
            ease 1.4 pos (0,10)
            repeat








image Rogue_Sex_Anus:
    contains:

        ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and action_speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and action_speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and action_speed", "Rogue_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Rogue_Sex_Anal_Tip",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Rogue_Sex_Anal_Tip",
            "primary_action == 'dildo_anal'", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "RogueX.used_to_anal", "images/RogueSex/Rogue_Sex_Hole_Loose.png",
            "True", "images/RogueSex/Rogue_Sex_Hole_Tight.png",
            )
    contains:

        ConditionSwitch(
                "'anal' not in RogueX.Spunk", Null(),
                "Player.Sprite and Player.Cock != 'anal' and action_speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and action_speed == 1", "Rogue_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",
                )
    contains:

        ConditionSwitch(
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", AlphaMask("Rogue_Sex_FingerA_Anim1", "Rogue_Anal_Fucking_Mask"),
            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Anal_Dildo_Anim2", "Rogue_Anal_Fucking_Mask"),
            "not Player.Sprite or Player.Cock != 'anal'", Null(),
            "action_speed >= 3",  AlphaMask("Rogue_Anal_Zero_Anim3", "Rogue_Anal_Fucking_Mask"),
            "action_speed >= 2", AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask"),
            "action_speed ", AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask"),
            "True", AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask"),
            )
    contains:

        ConditionSwitch(
                "'anal' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not action_speed", Null(),
                "action_speed == 1", "Rogue_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",
                )

image Rogue_Sex_FingerA_Anim1:

    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (507,600)
        zoom 1.2
        block:
            ease .4 ypos 550
            pause .4
            ease 1.2 ypos 600
            repeat

image Rogue_Anal_Dildo_Anim2:

    contains:
        subpixel True
        "images/DildoIn.png"
        pos (505,570)
        zoom 1.3
        block:
            ease 1 ypos 450
            pause 1
            ease 3 ypos 570
            repeat

image Rogue_Sex_Anal_Fucking0:

    contains:

        "Rogue_Anal_Tip"
    contains:

        AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask")

image Rogue_Sex_Anal_Fucking1:

    contains:

        "Rogue_Anal_Heading"
    contains:

        AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask")

image Rogue_Sex_Anal_Fucking2:

    contains:

        "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:

        AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask")

image Rogue_Sex_Anal_Fucking3:

    contains:

        "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask")

image Rogue_Anal_Fucking_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Hole_Mask.png"
        yoffset 1

image Rogue_Anal_Open_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Hole_Mask.png"
        yoffset 3

image Rogue_Sex_Anal_Heading:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease .75 xzoom 1.0
        ease .25 xzoom 0.9
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_Anal_Spunk_Heading_Over:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease .75 xzoom 1.0
        pause 1.75
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Rogue_Anal_Spunk_Heading_Under:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease .75 xzoom 1.0
        ease .25 xzoom 0.95
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6




image Rogue_Anal_Zero_Anim0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (505,600)
        zoom 1.3

image Rogue_Anal_Zero_Anim1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (505,600)
        zoom 1.3
        block:
            ease 1 ypos 570
            pause 1
            ease 3 ypos 600
            repeat

image Rogue_Anal_Zero_Anim2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (505,570)
        zoom 1.3
        block:
            ease 1 ypos 450
            pause 1
            ease 3 ypos 570
            repeat

image Rogue_Anal_Zero_Anim3:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (505,570)
        zoom 1.3
        block:
            ease .25 ypos 450
            pause .25
            ease 1.5 ypos 570
            repeat



image Rogue_Hotdog_Zero_Anim0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (503,570)
        zoom 1.3

image Rogue_Hotdog_Zero_Anim1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (503,500)
        zoom 1.3
        block:
            ease 1 ypos 560
            pause .5
            ease 1.5 ypos 500
            repeat

image Rogue_Hotdog_Zero_Anim2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (503,510)
        zoom 1.3
        block:
            ease .5 ypos 400
            pause .5
            ease 1 ypos 510
            repeat

image Rogue_Hotdog_Body_Anim2:

    contains:
        subpixel True
        "Rogue_Sex_Body"
        pos (0,0)
        block:

            pause .30
            ease .50 pos (0,-10)
            pause .20
            ease 1 pos (0,0)
            repeat

image Rogue_Hotdog_Legs_Anim2:

    contains:
        subpixel True
        "Rogue_Sex_Legs"
        pos (0,0)
        block:

            pause .20
            ease .50 pos (0,-10)
            pause .20
            ease 1.1 pos (0,0)
            repeat





image Rogue_Footcock:
    contains:
        subpixel True
        "Blowcock"
        alpha 0.8
        zoom 0.7
        anchor (0.5,0.5)
        offset (465,70)
        pos (0,0)
    pos (750,230)

image Rogue_Footcock_Static:
    contains:
        subpixel True
        "Rogue_Footcock"
        pos (392,295)

    offset (0,-100)

image Rogue_Footcock_Zero_Anim1:
    contains:
        subpixel True
        "Rogue_Footcock"
        pos (392,295)
        block:

            pause .5
            easein .75 ypos 360
            ease .25 ypos 355
            pause 1
            ease 2.50 ypos 270
            repeat
    offset (0,-100)

image Rogue_Footcock_Zero_Anim2:
    contains:
        subpixel True
        "Rogue_Footcock"
        pos (392,295)
        block:

            pause .2
            easein .4 ypos 360
            ease .2 ypos 355
            pause .2
            ease 1.00 ypos 270
            repeat
    offset (0,-100)

transform Rogue_Footcock_Zero_Anim1A():
    subpixel True
    offset (0,0)
    block:

        pause .5
        easein .75 yoffset 60
        ease .25 yoffset 55
        pause 1
        ease 1.50 yoffset -30
        repeat

transform Rogue_Footcock_Zero_Anim2A():
    subpixel True
    offset (0,0)
    block:

        pause .2
        easein .4 yoffset 60
        ease .2 yoffset 55
        pause .2
        ease 1.00 yoffset -30
        pause .2
        easein .4 yoffset 60
        ease .2 yoffset 55
        pause .2
        ease 1.00 yoffset -30
        repeat

transform Rogue_Footcock_StaticA():
    subpixel True
    offset (0,-5)
    block:

        pause .5
        ease 1 yoffset 0
        pause 1
        ease 1.50 yoffset -5
        repeat

image Rogue_Sex_Legs_FootAnim1:

    contains:
        subpixel True
        "Rogue_Sex_Legs"
        pos (0,0)
        block:

            pause .5
            easein .75 pos (0,-65)
            ease .25 pos (0,-60)
            pause 1
            ease 2.50 pos (0,25)
            repeat

    offset (0,100)

image Rogue_Sex_Legs_FootAnim2:

    contains:
        subpixel True
        "Rogue_Sex_Legs"
        pos (0,0)
        block:

            pause .2
            easein .4 pos (0,-65)
            ease .2 pos (0,-60)
            pause .2
            ease 1.0 pos (0,25)
            repeat
    offset (0,100)

image Rogue_Sex_Legs_FootAnimStatic:

    contains:
        subpixel True
        "Rogue_Sex_Legs"
        pos (0,0)
    offset (0,100)

transform Rogue_Sex_Legs_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause .5
        easein .75 yoffset -65
        ease .25 yoffset -60
        pause 1
        ease 1.50 yoffset 25
        repeat

transform Rogue_Sex_Legs_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause .2
        easein .4 yoffset -65
        ease .2 yoffset -60
        pause .2
        ease 1.0 yoffset 25
        pause .2
        easein .4 yoffset -65
        ease .2 yoffset -60
        pause .2
        ease 1.0 yoffset 25
        repeat

transform Rogue_Sex_Legs_FootAnimStaticA():

    subpixel True
    offset (0,0)
    block:

        pause .5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





image Rogue_Sex_Body_FootAnim1:

    contains:
        subpixel True
        "Rogue_Sex_Body"
        pos (0,0)
        block:

            pause .5
            easein .75 pos (0,-25)
            ease .25 pos (0,-15)
            pause 1
            ease 2.50 pos (0,15)
            repeat

    offset (0,100)

image Rogue_Sex_Body_FootAnim2:

    contains:
        subpixel True
        "Rogue_Sex_Body"
        pos (0,0)
        block:

            pause .2
            easein .4 pos (0,-25)
            ease .2 pos (0,-15)
            pause .2
            ease 1.0 pos (0,15)
            repeat
    offset (0,100)

image Rogue_Sex_Body_FootAnimStatic:

    contains:
        subpixel True
        "Rogue_Sex_Body"
        pos (0,0)
    offset (0,100)

transform Rogue_Sex_Body_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause .5
        easein .75 yoffset -25
        ease .25 yoffset -15
        pause 1
        ease 1.50 yoffset 15
        repeat

transform Rogue_Sex_Body_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause .2
        easein .4 yoffset -25
        ease .2 yoffset -15
        pause .2
        ease 1.0 yoffset 15
        pause .2
        easein .4 yoffset -25
        ease .2 yoffset -15
        pause .2
        ease 1.0 yoffset 15
        repeat

transform Rogue_Sex_Body_FootAnimStaticA():

    subpixel True
    offset (0,0)
    block:

        pause .5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





label Rogue_Sex_Launch(Line=primary_action):
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action

    $ Line = "solo" if not Line else Line
    $ Player.Sprite = 1
    if Line == "sex":
        $ Player.Cock = "in"
        if offhand_action in ("fondle_pussy","dildo_pussy","eat_pussy"):
            $ offhand_action = 0
    elif Line == "anal":
        $ Player.Cock = "anal"
        if offhand_action in ("finger_ass","dildo_anal","eat_ass"):
            $ offhand_action = 0
    elif Line == "hotdog":
        $ Player.Cock = "out"
    elif Line == "foot":
        $ ShowFeet = 1
        $ Player.Cock = "foot"
    elif Line == "massage":
        $ Player.Sprite = 0
        $ Player.Cock = 0
    else:
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        $ action_speed = 0
    $ primary_action = Line

    if RogueX.pose == "doggy":
        call Rogue_Doggy_Launch (Line)
        return
    if renpy.showing("Rogue_SexSprite"):
        return
    $ action_speed = 0
    call Rogue_Hide (1)
    show Rogue_SexSprite zorder 150



    with dissolve
    return

label Rogue_Sex_Reset:
    if renpy.showing("Rogue_Doggy_Animation"):
        call Rogue_Doggy_Reset
        return
    if not renpy.showing("Rogue_SexSprite"):
        return
    $ RogueX.ArmPose = 2
    hide Rogue_SexSprite
    call Rogue_Hide

    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return











image Rogue_BJ_Animation:
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Rogue_BJ_HairBack", Rogue_BJ_Starting()),
            "action_speed == 1", At("Rogue_BJ_HairBack", Rogue_BJ_Licking()),
            "action_speed == 2", At("Rogue_BJ_HairBack", Rogue_BJ_Heading()),
            "action_speed == 3", At("Rogue_BJ_HairBack", Rogue_BJ_Sucking()),
            "action_speed >= 4", At("Rogue_BJ_HairBack", Rogue_BJ_Deep()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Rogue_BJ_Backdrop", Rogue_BJ_StartingBody()),
            "action_speed == 1", At("Rogue_BJ_Backdrop", Rogue_BJ_LickingBody()),
            "action_speed == 2", At("Rogue_BJ_Backdrop", Rogue_BJ_HeadingBody()),
            "action_speed == 3", At("Rogue_BJ_Backdrop", Rogue_BJ_SuckingBody()),
            "action_speed >= 4", At("Rogue_BJ_Backdrop", Rogue_BJ_DeepBody()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Rogue_BJ_Head", Rogue_BJ_Starting()),
            "action_speed == 1", At("Rogue_BJ_Head", Rogue_BJ_Licking()),
            "action_speed == 2", At("Rogue_BJ_Head", Rogue_BJ_Heading()),
            "action_speed == 3", At("Rogue_BJ_Head", Rogue_BJ_Sucking()),
            "action_speed >= 4", At("Rogue_BJ_Head", Rogue_BJ_Deep()),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "action_speed == 0", At("Blowcock", Rogue_Cock_BJ_Starting()),
            "action_speed == 1", At("Blowcock", Rogue_Cock_BJ_Licking()),
            "action_speed == 2", At("Blowcock", Rogue_Cock_BJ_Straight()),
            "action_speed == 3", At("Blowcock", Rogue_Cock_BJ_Straight()),
            "action_speed >= 4", At("Blowcock", Rogue_Cock_BJ_Straight()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Rogue_BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), Rogue_BJ_Sucking()),
            "action_speed >= 4", At(AlphaMask("Rogue_BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), Rogue_BJ_Deep()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "action_speed == 2", At(AlphaMask("Rogue_BJ_Head", "Rogue_BJ_MaskHeadingComposite"), Rogue_BJ_Heading()),
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Rogue_BJ_Head:
    "Rogue_Head"
    zoom 3.45


image Rogue_BJ_HairBack:
    "Rogue_HairBack"
    zoom 3.45

image Rogue_BJ_Backdrop:
    "Rogue_Sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)


image Rogue_BJ_MouthHeading:

    contains:
        ConditionSwitch(

            "'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_suckingS.png",
            "True", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
            )

        anchor (0.40,0.65)

image Rogue_BJ_MaskHeading:

    contains:
        "images/RogueBJFace/Rogue_bj_facemask.png"
        anchor (0.4,0.65)

image Rogue_BJ_MaskHeadingComposite:

    LiveComposite(
        (787,913),
        (316,590), ConditionSwitch(
            "action_speed == 2", At("Rogue_BJ_MaskHeading", Rogue_BJ_MouthAnim()),
            "True", Null(),
            ),
        )

transform Rogue_BJ_MouthAnim():

    subpixel True
    zoom 0.90
    block:
        pause .10
        easeout .55 zoom 0.9
        linear .10 zoom 0.87
        easein .30 zoom 0.9
        pause .15
        easeout .40 zoom 0.87
        linear .10 zoom 0.9
        easein .45 zoom 0.70
        pause .35
        repeat

image Blowcock:
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png",
            "True", Null(),
            ),
    anchor (0.5,0.5)
    zoom 1.0
    alpha 1.0
    offset (26,350)

transform Rogue_Cock_BJ_Starting():

    anchor (.5,.5)
    rotate -10

transform Rogue_Cock_BJ_Licking():

    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause .5
        ease 2.5 rotate 0
        repeat

transform Rogue_Cock_BJ_Straight():

    anchor (.5,.5)
    rotate 0

transform Rogue_BJ_Licking():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (25,100)
        ease 2 offset (0,-35)
        pause .5
        repeat

transform Rogue_BJ_LickingBody():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (30,90)
        ease 2 offset (0,-35)
        pause .5
        repeat

transform Rogue_BJ_Heading():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 35
        ease 1.5 offset (0,-40)
        repeat

transform Rogue_BJ_HeadingBody():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat

transform Rogue_BJ_Sucking():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120
        ease 1.5 offset (0,50)
        repeat

transform Rogue_BJ_SuckingBody():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100
        ease 1.5 offset (0,50)
        repeat

transform Rogue_BJ_Deep():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat

transform Rogue_BJ_DeepBody():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Rogue_BJ_Static():

    subpixel True
    ease 1.5 offset (0,0)
    repeat

transform Rogue_BJ_StaticBody():

    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_BJ_Starting():

    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_BJ_StartingBody():

    subpixel True
    ease 1.5 offset (0,0)



label Rogue_BJ_Launch(Line=primary_action):

    if renpy.showing("Rogue_BJ_Animation"):
        return

    call Rogue_Hide
    if Line == "L" or Line == "cum":
        show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
            alpha 1

            ease 1 zoom 2.5 offset (70,140)
        with dissolve
    else:
        show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (70,140)
        with dissolve

    if Taboo and Line == "L":

        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[RogueX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[RogueX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[RogueX.name] looks around to see if anyone can see her."
    if Line == "L":
        if not RogueX.action_counter["blowjob"]:
            "[RogueX.name] hesitantly pulls down your pants and touches her mouth to your cock."
        else:
            "[RogueX.name] bends down and begins to suck on your cock."

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    show Rogue_Sprite zorder RogueX.sprite_layer:
        alpha 0
    show Rogue_BJ_Animation zorder 150:
        pos (645,510)
    return

label Rogue_BJ_Reset:
    if not renpy.showing("Rogue_BJ_Animation"):
        return

    call Rogue_Hide
    $ action_speed = 0

    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    $ RogueX.change_face("sexy")
    return






transform Zero_BJ_Static():
    anchor (.5,.5)

    rotate -10


transform Zero_BJ_Sucking():
    anchor (.5,.5)
    rotate 0

transform Zero_BJ_Licking():
    subpixel True
    block:
        ease 2 rotate -5
        pause .5
        ease 2.5 rotate 0
        repeat

image Zero_Blowcock:
    LiveComposite(
        (175,946),
        (0,0), ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png",
            "True", Null(),
            ),
        )
    anchor (0.5,0.5)
    zoom 1.2
    xoffset 5





image Rogue_TJ_Under:
    contains:
        "Rogue_BJ_HairBack"
        pos (150, -560)
        zoom .95
    contains:
        "images/RogueBJFace/Rogue_tj_base.png"
    contains:
        ConditionSwitch(
            "'tits' in RogueX.Spunk", "images/RogueBJFace/Rogue_tj_spunkU.png",
            "True", Null(),
            ),
    contains:
        "Rogue_BJ_Head"
        pos (150, -560)
        zoom .95
    pos (-60, 200)

image Rogue_TJ_Over:
    contains:
        ConditionSwitch(
            "RogueX.piercings == 'barbell'", "images/RogueBJFace/Rogue_tj_tits_b.png",
            "RogueX.piercings == 'ring'", "images/RogueBJFace/Rogue_tj_tits_r.png",
            "RogueX.piercings != 'barbell'", "images/RogueBJFace/Rogue_tj_tits.png",
            ),
    contains:
        ConditionSwitch(
            "'tits' in RogueX.Spunk", "images/RogueBJFace/Rogue_tj_spunk.png",
            "True", Null(),
            ),
    pos (-60, 200)


transform Rogue_TJ_Under_1():
    ypos 200
    subpixel True
    block:
        ease 1 ypos 300
        easeout .2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_TJ_Over_1():
    ypos 200
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout .1 ypos 300
        easein 1.2 ypos 120
        repeat

transform Rogue_TJ_Under_2():
    ypos 200
    subpixel True
    block:
        ease .25 ypos 200
        ease .4 ypos 120
        ease .1 ypos 125
        repeat

transform Rogue_TJ_Over_2():
    ypos 200
    subpixel True
    block:
        ease .3 ypos 200
        ease .35 ypos 120
        ease .1 ypos 125
        repeat


transform Zero_TJ_Cock():

    anchor (.5,.5)
    pos (440,1020)
    rotate 0

transform Zero_TJ_Cock_1():
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout .2 ypos 1060
        easein 1.3 ypos 1020
        repeat

transform Zero_TJ_Cock_2():
    pos (440,1020)
    subpixel True
    block:
        ease .35 ypos 1030
        ease .4 ypos 1020

        repeat



image Rogue_TJ_Animation:

    contains:
        ConditionSwitch(
            "not action_speed", Transform("Rogue_TJ_Under"),
            "action_speed == 1", At("Rogue_TJ_Under", Rogue_TJ_Under_1()),
            "action_speed >= 2", At("Rogue_TJ_Under", Rogue_TJ_Under_2()),
            "action_speed ", Null(),
            ),
    contains:

        ConditionSwitch(
            "not action_speed", At("Zero_Blowcock", Zero_TJ_Cock()),
            "action_speed == 1", At("Zero_Blowcock", Zero_TJ_Cock_1()),
            "action_speed >= 2", At("Zero_Blowcock", Zero_TJ_Cock_2()),
            "action_speed ", Null(),
            ),
    contains:

        ConditionSwitch(
            "not action_speed", Transform("Rogue_TJ_Over"),
            "action_speed == 1", At("Rogue_TJ_Over", Rogue_TJ_Over_1()),
            "action_speed >= 2", At("Rogue_TJ_Over", Rogue_TJ_Over_2()),
            "action_speed ", Null(),
            ),
    anchor (0.6, 0.0)
    offset (-75, 250)
    zoom .55

label Rogue_TJ_Launch(Line=primary_action):

    if renpy.showing("Rogue_TJ_Animation"):
        return
    call Rogue_Hide
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        ease 1 zoom 2 xpos 550 offset (0,50)
    if Taboo:
        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[RogueX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[RogueX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[RogueX.name] looks around to see if anyone can see her."

    if RogueX.bra and RogueX.top:
        "She throws off her [RogueX.top] and her [RogueX.bra]."
    elif RogueX.top:
        "She throws off her [RogueX.top], baring her breasts underneath."
    elif RogueX.bra:
        "She tugs off her [RogueX.bra] and throws it aside."
    $ RogueX.top = 0
    $ RogueX.bra = 0
    $ RogueX.arms = 0

    call Rogue_First_Topless

    if not RogueX.action_counter["titjob"] and Line == "L":
        if not RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] hesitantly places it under her [RogueX.bra], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and RogueX.top:
            "As you pull out your cock, [RogueX.name] hesitantly places it under her [RogueX.top], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L":
        if not RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and not RogueX.top:
            "As you pull out your cock, [RogueX.name] places it under her [RogueX.bra], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.bra and RogueX.top:
            "As you pull out your cock, [RogueX.name] places it under her [RogueX.top], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
        "[RogueX.name] wraps her tits around your cock."
    show blackscreen onlayer black with dissolve
    show Rogue_Sprite zorder RogueX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Rogue_TJ_Animation zorder 150 at sprite_location(stage_right)
    hide blackscreen onlayer black with dissolve
    return

label Rogue_TJ_Reset:

    if not renpy.showing("Rogue_TJ_Animation"):
        return
    hide Rogue_TJ_Animation
    call Rogue_Hide
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        zoom 2 xpos 550 offset (0,50)
    show Rogue_Sprite zorder RogueX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos RogueX.sprite_location yoffset 0
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 xpos RogueX.sprite_location yoffset 0

    "[RogueX.name] pulls back"
    return




image Zero_Handcock:
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/handcock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/handcock_G.png",
            "Player.Color != 'pink'", Null(),
            ),
    anchor (0.5,1.0)
    pos (200,400)

image Rogue_Hand_Under:
    "images/RogueBJFace/hand2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Rogue_Hand_Over:
    "images/RogueBJFace/hand1.png"
    anchor (0.5,0.5)
    pos (0,0)

transform Handcock_1():
    subpixel True
    rotate_pad False
    ease .5 ypos 450 rotate -2
    pause 0.25
    ease 1.0 ypos 400 rotate 0
    pause 0.1
    repeat

transform Handcock_2():
    subpixel True
    rotate_pad False
    ease .2 ypos 430 rotate -3
    ease .5 ypos 400 rotate 0
    pause 0.1
    repeat

transform Rogue_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5
    pause 0.25
    ease 1.0 ypos -100 rotate -5
    pause 0.1
    repeat

transform Rogue_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat

image Rogue_HJ_Animation:
    contains:
        ConditionSwitch(
            "not action_speed", "Rogue_Hand_Under",
            "action_speed == 1", At("Rogue_Hand_Under", Rogue_Hand_1()),
            "action_speed >= 2", At("Rogue_Hand_Under", Rogue_Hand_2()),
            "action_speed ", Null(),
            ),
    contains:
        ConditionSwitch(
            "not action_speed", "Zero_Handcock",
            "action_speed == 1", At("Zero_Handcock", Handcock_1()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            "not action_speed", "Rogue_Hand_Over",
            "action_speed == 1", At("Rogue_Hand_Over", Rogue_Hand_1()),
            "action_speed >= 2", At("Rogue_Hand_Over", Rogue_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.5,0.5)
    offset (200,800)
    zoom 0.6

label Rogue_HJ_Launch(Line=primary_action):
    if renpy.showing("Rogue_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call Rogue_Hide
    $ RogueX.arms = 0
    $ RogueX.ArmPose = 1
    if not renpy.showing("Rogue_Sprite"):
        show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
            alpha 1
            zoom 1.7 xpos 700 offset (0,200)
        with dissolve
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        ease 1 zoom 1.7 xpos 700 offset (0,200)

    if Taboo and Line == "L":

        if len(Present) >= 2:
            if Present[0] != RogueX:
                "[RogueX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != RogueX:
                "[RogueX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[RogueX.name] looks around to see if anyone can see her."
        if not RogueX.action_counter["handjob"] and RogueX.arms:
            "As you pull out your cock, [RogueX.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "She then leans over and grabs your cock."
    elif Line == "L":
        if not RogueX.action_counter["handjob"] and RogueX.arms:
            "As you pull out your cock, [RogueX.name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "[RogueX.name] bends down and grabs your cock."
    else:
        "[RogueX.name] bends down and grabs your cock."

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    show Rogue_HJ_Animation zorder 150 at sprite_location(RogueX.sprite_location) with easeinbottom
    return

label Rogue_HJ_Reset:
    if not renpy.showing("Rogue_HJ_Animation"):
        return
    $ action_speed = 0
    hide Rogue_HJ_Animation
    with dissolve
    call Rogue_Hide
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1.7 xpos 700 offset (0,200)
    show Rogue_Sprite zorder RogueX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos RogueX.sprite_location yoffset 0
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        alpha 1
        zoom 1 xpos RogueX.sprite_location yoffset 0
    return




transform Vibrate():
    subpixel True
    block:
        linear .5 xoffset 2
        linear .5 xoffset -2
        repeat


image UI_Vibrator = LiveComposite(
        (224,224),
        (0,0), ConditionSwitch(
            "not Vibration", "UI_VibA",
            "Vibration", At("UI_VibB", Vibrate()),
            ),
        )

image GropeLeftBreast:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.7
        xzoom -0.7
        pos (180,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat


image LickRightBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (160,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -45 pos (150,370)
            pause .5
            ease 1.5 rotate 30 pos (160,400)
            repeat

image LickLeftBreast:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (280,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -45 pos (260,380)
            pause .5
            ease 1.5 rotate 30 pos (280,410)
            repeat

image GropeThigh:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GropePussy:
    contains:
        subpixel True
        "UI_Hand"
        zoom .7
        pos (220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (220,620)
                ease .75 rotate 170 pos (220,635)
            choice:
                ease .5 rotate 190 pos (220,620)
                pause .25
                ease 1 rotate 170 pos (220,635)
            repeat

image FingerPussy:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.7
        pos (230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease .5 rotate 40 pos (240,685)
                pause .5
                ease 1.75 rotate 50 pos (230,720)
            choice:
                ease 2 rotate 40 pos (240,685)
                pause .5
                ease 1 rotate 50 pos (230,720)
            choice:
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
                ease .25 rotate 40 pos (240,685)
                ease .25 rotate 50 pos (230,720)
            repeat

image Lickpussy:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.5
        xzoom -0.5
        pos (250,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (230,650)
            linear .5 rotate -60 pos (220,660)
            easein 1 rotate 10 pos (250,670)
            repeat

image VibratorRightBreast:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 370
            pause .25
            ease 1 rotate 55 ypos 380
            pause .25
            repeat

image VibratorLeftBreast:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 390
            pause .25
            ease 1 rotate 55 ypos 400
            pause .25
            repeat

image VibratorPussy:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 230 ypos 655
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665
            pause .25
            repeat

image VibratorAnal:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat

image VibratorPussyInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0

image TestUIAnimation:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            ease 1 rotate 0 xpos 260 ypos 655
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
            repeat


image GirlGropeLeftBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (300,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (280,390)
            ease 1 rotate -20 pos (300,400)
            repeat

image GirlGropeRightBreast:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (160,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -30 pos (160,410)
            ease 1 rotate -10 pos (160,380)
            repeat

image GirlGropeThigh:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause .5
            ease .5 xpos 213
            ease .5 xpos 210
            ease .5 xpos 213
            ease .5 xpos 210
            repeat

image GirlGropePussy:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (230,615)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (225,620)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (225,620)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (225,620)
                ease .75 rotate 200 pos (225,625)
            choice:
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
                ease .3 rotate 205 pos (225,620)
                ease .3 rotate 200 pos (225,630)
            repeat

image GirlFingerPussy:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (230,630)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (230,635)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (230,635)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
                ease .5 rotate 205 pos (230,635)
                ease .75 rotate 200 pos (230,640)
            choice:
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
                ease .3 rotate 205 pos (230,635)
                ease .3 rotate 200 pos (230,645)
            repeat





image Spunk_Drip:

    contains:
        "images/SpermdropB.png"
        zoom 0.3
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause .5
            choice:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause .2
                alpha 1
                easeout 2.5 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .4
            choice:
                pos (6,0)
                pause .4
                alpha 1
                easeout 2.5 ypos 65
                easeout .9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause .8
                alpha 1
                easeout 2.5 ypos 60
                easeout .9 ypos 350
                alpha 0
            repeat

image Spunk_Drip2:

    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (0,0)
            alpha 1
            easeout 2.5 ypos 70
            easeout .9 ypos 350
            alpha 0
            pause 1
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (9,0)
            pause .2
            alpha 1
            easeout 2.5 ypos 75
            easeout .9 ypos 350
            alpha 0
            pause .4
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (6,0)
            pause .4
            alpha 1
            easeout 2.5 ypos 65
            easeout .9 ypos 350
            alpha 0
            repeat
    contains:
        "images/SpermdropB.png"
        pos (0,0)
        zoom 0.3
        parallel:
            pos (12,0)
            pause .8
            alpha 1
            easeout 2.5 ypos 60
            easeout .9 ypos 350
            alpha 0
            repeat


image Spunk_Dripp:

    contains:
        "images/SpermdropP.png"
        zoom 0.3
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause .5
            choice:
                pos (0,0)
                alpha 1
                easeout 2.5 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause .2
                alpha 1
                easeout 2.5 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .4
            choice:
                pos (6,0)
                pause .4
                alpha 1
                easeout 2.5 ypos 65
                easeout .9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause .8
                alpha 1
                easeout 2.5 ypos 60
                easeout .9 ypos 350
                alpha 0
            repeat

image Wet_Drip:

    contains:
        "images/Wetdrop.png"
        zoom 0.2
        alpha 0
        block:
            choice:
                pause 1
            choice:
                pause .5
            choice:
                pos (14,0)
                alpha .8
                easeout .9 ypos 70
                easeout .9 ypos 350
                alpha 0
                pause 1
            choice:
                pos (9,0)
                pause .2
                alpha .8
                easeout .9 ypos 75
                easeout .9 ypos 350
                alpha 0
                pause .4
            choice:
                pos (6,0)
                pause .4
                alpha .8
                easeout .9 ypos 65
                easeout .9 ypos 350
                alpha 0
            choice:
                pos (12,0)
                pause .8
                alpha .8
                easeout .9 ypos 60
                easeout .9 ypos 350
                alpha 0
            repeat

image Wet_Drip2:

    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (14,0)
            alpha .8
            easeout .9 ypos 70
            easeout .9 ypos 350
            alpha 0
            pause 1.5
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (9,0)
            pause .3
            alpha .8
            easeout .9 ypos 75
            easeout .9 ypos 350
            alpha 0
            pause .6
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (6,0)
            pause .6
            alpha .8
            easeout .9 ypos 65
            easeout .9 ypos 350
            alpha 0
            repeat
    contains:
        "images/Wetdrop.png"
        pos (0,0)
        zoom 0.2
        parallel:
            pos (12,0)
            pause .8
            alpha .8
            easeout .9 ypos 60
            easeout .9 ypos 350
            alpha 0
            pause .2
            repeat


image Zero_Chibicock:
    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Player.Color == 'pink'", "images/Chibi_Cock_P.png",
            "Player.Color == 'brown'", "images/Chibi_Cock_B.png",
            "Player.Color == 'green'", "images/Chibi_Cock_G.png",
            "True", Null(),
            ),








        )
    anchor (0.5,0.5)



image Chibi_Null:

    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    pos (75,675)
    zoom 0.5

image Chibi_Jackin:

    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        "images/Chibi_Hand_M.png"
        pos (-10,-80)
        anchor (0.5,0.5)
        rotate 20
        block:
            ease .3 rotate -10 pos (0,50)
            ease .7 rotate 20 pos (-10,-80)
            repeat
    pos (75,675)
    zoom 0.5

image Chibi_Handy:

    contains:
        "Zero_Chibicock"
        anchor (0.5,0.5)
        pos (0,0)
        rotate 0
        xzoom 1
    contains:
        subpixel True
        ConditionSwitch(
            "(Partner == StormX and second_girl_primary_action == 'hand') or (focused_Girl == StormX and girl_offhand_action == 'hand')", "images/Chibi_Hand_S.png",
            "True", "images/Chibi_Hand_G.png"
            )

        pos (0,-110)
        anchor (0.5,0.5)
        rotate -10
        block:
            ease .3 rotate 0 pos (10,10)
            ease .7 rotate -10 pos (0,-130)
            repeat
    pos (75,675)
    zoom 0.5

image Chibi_Mouth_Mask:
    "images/Chibi_Mouth_Mask.png"
    anchor (0.5,0.5)

image Chibi_Mouth_Rogue:
    "images/Chibi_Mouth_R.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Kitty:
    "images/Chibi_Mouth_K.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Emma:
    "images/Chibi_Mouth_E.png"
    anchor (0.5,0.5)
image Chibi_Mouth_Storm:
    "images/Chibi_Mouth_S.png"
    anchor (0.5,0.5)

image Chibi_Sucking:

    contains:
        "Chibi_SuckingB"
    pos (75,675)

image Chibi_SuckingB:

    LiveComposite(
        (225,350),
        (0,0), ConditionSwitch(
            "Partner == RogueX", "Chibi_Mouth_Rogue",
            "Partner == EmmaX", "Chibi_Mouth_Emma",
            "Partner == StormX", "Chibi_Mouth_Storm",
            "True", "Chibi_Mouth_Kitty"
            ),
        (0,0), AlphaMask("Chibi_Sucking_Cock", "Chibi_Mouth_Mask")
        )
    subpixel True
    pos (7,0)
    anchor (0.5,0.5)
    zoom 0.5
    xzoom 0.71
    block:
        easeout .25 rotate 0 pos (2,48) xzoom 1
        easein .25 rotate 0 pos (6,92) xzoom 1
        easeout .5 rotate 0 pos (2,48) xzoom 1
        easein .5 rotate 0 pos (5,0) xzoom 0.71
        repeat

image Chibi_Sucking_Cock:

    contains:
        subpixel True
        "Zero_Chibicock"
        pos (100,175)
        xzoom 1.5
        anchor (0.5,0.5)

        rotate 0
        block:
            easeout .25 rotate 0 pos (110,80) xzoom 1
            easein .25 rotate 0 pos (100,-10) xzoom 1
            easeout .5 rotate 0 pos (110,80) xzoom 1
            easein .5 rotate 0 pos (100,175) xzoom 1.5
            repeat




image Chibi_UI:

    contains:
        ConditionSwitch(
            "'cockout' not in Player.recent_history", Null(),
            "offhand_action == 'jackin'", "Chibi_Jackin",
            "girl_offhand_action == 'hand' or second_girl_primary_action == 'hand'", "Chibi_Handy",
            "second_girl_primary_action == 'blow'", "Chibi_Sucking",
            "True", "Chibi_Null",
            )



label Rogue_Kissing_Launch(T=primary_action, Set=1):
    call Rogue_Hide
    $ primary_action = T
    $ RogueX.pose = "kiss" if Set else RogueX.pose
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location)
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Rogue_Kissing_Smooch:
    $ RogueX.change_face("kiss")
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(stage_center):
        offset (0,0)
        alpha 1
        ease 0.5 xpos stage_center zoom 2
        pause 1
        ease 0.5 xpos RogueX.sprite_location zoom 1
    pause 1
    $ RogueX.change_face("sexy")
    return

label Rogue_Breasts_Launch(T=primary_action, Set=1):
    call Rogue_Hide
    $ primary_action = T
    $ RogueX.pose = "breasts" if Set else RogueX.pose
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        ease 0.5 pos (700,-50) zoom 2 offset (0,0) alpha 1
    return

label Rogue_Middle_Launch(T=primary_action, Set=1):
    call Rogue_Hide
    $ primary_action = T
    $ RogueX.pose = "mid" if Set else RogueX.pose
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Rogue_Pussy_Launch(T=primary_action, Set=1):
    call Rogue_Hide
    $ primary_action = T
    $ RogueX.pose = "pussy" if Set else RogueX.pose
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        ease 0.5 pos (700,-400) zoom 2 offset (0,0) alpha 1
    return

label Rogue_Pos_Reset(T=0, Set=0):
    if RogueX.location != bg_current:
        return
    call Rogue_Hide
    show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location):
        ease .5 offset (0,0) anchor (0.6, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Rogue_Sprite zorder RogueX.sprite_layer:
        offset (0,0)
        anchor (0.6, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (RogueX.sprite_location,50)
    $ RogueX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Rogue_Hide(Sprite=0):
    call Rogue_Sex_Reset
    hide Rogue_SexSprite
    hide Rogue_Doggy_Animation
    hide Rogue_HJ_Animation
    hide Rogue_BJ_Animation
    hide Rogue_TJ_Animation
    if Sprite:
        hide Rogue_Sprite
    return

image Cellphone:
    "images/Cellphone.png"
    xoffset 0
    yoffset 100


image PhoneSex:

    contains:

        "images/PhoneFrame.png"
    contains:

        AlphaMask("PhoneScreen", "images/PhoneMask.png")
    offset (300,50)

image PhoneRG:

    "bg_rogue"
    xoffset 500

image PhoneScreen:

    contains:

        ConditionSwitch(
            "focused_Girl.location == 'bg_rogue'","PhoneRG",
            "focused_Girl.location == 'bg_kitty'", "bg_kitty",
            "focused_Girl.location == 'bg_emma'", "bg_emma",
            "focused_Girl.location == 'bg_laura'", "bg_laura",
            "focused_Girl.location == 'bg_jean'", "bg_jean",
            "focused_Girl.location == 'bg_storm'", "bg_storm",
            "focused_Girl.location == 'bg_jubes'", "bg_jubes",
            "focused_Girl.location == 'bg_classroom'", "bg_class",
            "focused_Girl.location == 'bg_teacher'", "bg_class",
            "True", "bg_shower",
            )
        offset (-800,-300)
        zoom 1.5
    contains:

        ConditionSwitch(
            "focused_Girl.Tag == 'Rogue'", "Rogue_Sprite",
            "focused_Girl.Tag == 'Kitty'", "Kitty_Sprite",
            "focused_Girl.Tag == 'Emma'", "Emma_Sprite",
            "focused_Girl.Tag == 'Laura'", "Laura_Sprite",
            "focused_Girl.Tag == 'Jean'", "Jean_Sprite",
            "focused_Girl.Tag == 'Storm'", "Storm_Sprite",
            "focused_Girl.Tag == 'Jubes'", "Jubes_Sprite",
            "True", Null(),
            )
        pos (0,0)
        offset (290,50)
        anchor (0.6,0)
        zoom 1.1


image DressScreen:

    contains:

        "images/DressScreen.png"
    contains:

        AlphaMask("images/DressScreenShadow.png","DressShadow")
    zoom 1
    offset (375,225)

image DressShadow:

    contains:

        ConditionSwitch(
            "RogueX.sprite_layer == 100", "Rogue_Sprite",
            "KittyX.sprite_layer == 100", "Kitty_Sprite",
            "EmmaX.sprite_layer == 100", "Emma_Sprite",
            "LauraX.sprite_layer == 100", "Laura_Sprite",
            "JeanX.sprite_layer == 100", "Jean_Sprite",
            "StormX.sprite_layer == 100", "Storm_Sprite",
            "JubesX.sprite_layer == 100", "Jubes_Sprite",




            "True", Null(),
            )
        offset (210,-170)
        zoom 1




label XavierFace(Face=X_emotion):
    if Face == "psychic":
        $ X_Mouth = "concentrate"
        $ X_Brows = "concentrate"
        $ X_Eyes = "concentrate"
        $ X_Psychic = 1
    if Face == "hypno":
        $ X_Mouth = "neutral"
        $ X_Brows = "neutral"
        $ X_Eyes = "hypno"
    if Face == "shocked":
        $ X_Mouth = "neutral"
        $ X_Brows = "shocked"
        $ X_Eyes = "shocked"
        $ X_Psychic = 0
    if Face == "happy":
        $ X_Mouth = "happy"
        $ X_Brows = "happy"
        $ X_Eyes = "happy"
        $ X_Psychic = 0
    if Face == "angry":
        $ X_Mouth = "concentrate"
        $ X_Brows = "concentrate"
        $ X_Eyes = "happy"
        $ X_Psychic = 0
    return


image Gwen_Sprite:
    LiveComposite(
        (574,964),

        (0,0), "images/GS_B.png",


        (80,15), "Gwen_Sprite_Head",
        )
    anchor (0.6, 0.0)
    yoffset 15
    zoom .75



image Gwen_Sprite_Head:
    LiveComposite(
        (820,820),
        (0,0), ConditionSwitch(

                "G_Blush", "images/NPC/Gwen_Sprite_Head_Blush.png",
                "True", "images/NPC/Gwen_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "G_Mouth == 'open'", "images/NPC/Gwen_Sprite_Mouth_Open.png",
            "G_Mouth == 'kiss'", "images/NPC/Gwen_Sprite_Mouth_Kiss.png",
            "G_Mouth == 'smile'", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            "G_Mouth == 'shocked'", "images/NPC/Gwen_Sprite_Mouth_Shocked.png",
            "True", "images/NPC/Gwen_Sprite_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(

            "G_Blush", ConditionSwitch(
                    "G_Brows == 'angry' or G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Brows_Angry_B.png",
                    "G_Brows == 'sad'", "images/NPC/Gwen_Sprite_Brows_Sad_B.png",
                    "True", "images/NPC/Gwen_Sprite_Brows_Normal.png",
                    ),
            "True", ConditionSwitch(
                    "G_Brows == 'angry' or G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Brows_Angry.png",
                    "G_Brows == 'sad'", "images/NPC/Gwen_Sprite_Brows_Sad.png",
                    "True", "images/NPC/Gwen_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Gwen Blink",
        )
    anchor (0.6, 0.0)
    zoom .5

image Gwen Blink:
    ConditionSwitch(
    "G_Eyes == 'angry'", "images/NPC/Gwen_Sprite_Eyes_Angry.png",
    "G_Eyes == 'surprised'", "images/NPC/Gwen_Sprite_Eyes_Surprised.png",
    "G_Eyes == 'closed'", "images/NPC/Gwen_Sprite_Eyes_Closed.png",
    "True", "images/NPC/Gwen_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/NPC/Gwen_Sprite_Eyes_Closed.png"
    .20
    repeat

default G_Mouth = "normal"
default G_Brows = "normal"
default G_Eyes = "normal"
default G_Blush = 0

label GwenFace(emotion="normal", B=G_Blush, M=0, Mouth=0, Eyes=0, Brows=0):


    $ B = G_Blush if B == 5 else B

    if emotion == "normal":
        $ G_Mouth = "normal"
        $ G_Brows = "normal"
        $ G_Eyes = "normal"
    elif emotion == "angry":
        $ G_Mouth = "kiss"
        $ G_Brows = "angry"
        $ G_Eyes = "angry"
    elif emotion == "closed":
        $ G_Mouth = "normal"
        $ G_Brows = "sad"
        $ G_Eyes = "closed"
    elif emotion == "sad":
        $ G_Mouth = "kiss"
        $ G_Brows = "sad"
        $ G_Eyes = "normal"
    elif emotion == "smile":
        $ G_Mouth = "smile"
        $ G_Brows = "normal"
        $ G_Eyes = "normal"
    elif emotion == "surprised":
        $ G_Mouth = "open"
        $ G_Brows = "normal"
        $ G_Eyes = "surprised"
    elif emotion == "shocked":
        $ G_Mouth = "shocked"
        $ G_Brows = "normal"
        $ G_Eyes = "surprised"

    if B > 1:
        $ G_Blush = 2
    elif B:
        $ G_Blush = 1
    else:
        $ G_Blush = 0

    if Mouth:
        $ G_Mouth = Mouth
    if Eyes:
        $ G_Eyes = Eyes
    if Brows:
        $ G_Brows = Brows

    return

label Gwen_FaceEditor:
    while True:
        menu:
            "Brows=[G_Brows], Eyes=[G_Eyes], Mouth=[G_Mouth]"
            "Toggle Brows":
                if G_Brows == "normal":
                    $ G_Brows = "angry"
                elif G_Brows == "angry":
                    $ G_Brows = "confused"
                elif G_Brows == "confused":
                    $ G_Brows = "sad"
                elif G_Brows == "sad":
                    $ G_Brows = "surprised"
                else:
                    $ G_Brows = "normal"
            "Toggle Eyes Emotions":
                if G_Eyes == "normal":
                    $ G_Eyes = "surprised"
                elif G_Eyes == "surprised":
                    $ G_Eyes = "sexy"
                elif G_Eyes == "sexy":
                    $ G_Eyes = "squint"
                elif G_Eyes == "squint":
                    $ G_Eyes = "closed"
                else:
                    $ G_Eyes = "normal"
            "Toggle Eyes Directions":
                if G_Eyes == "normal":
                    $ G_Eyes = "side"
                elif G_Eyes == "side":
                    $ G_Eyes = "down"
                elif G_Eyes == "down":
                    $ G_Eyes = "leftside"
                elif G_Eyes == "leftside":
                    $ G_Eyes = "stunned"
                else:
                    $ G_Eyes = "normal"
            "Toggle Mouth Normal":
                if G_Mouth  == "normal":
                    $ G_Mouth = "sad"
                elif G_Mouth == "sad":
                    $ G_Mouth = "smile"
                elif G_Mouth == "smile":
                    $ G_Mouth = "surprised"
                else:
                    $ G_Mouth = "normal"
            "Toggle Mouth Sexy":
                if G_Mouth  == "normal":
                    $ G_Mouth = "kiss"
                elif G_Mouth == "kiss":
                    $ G_Mouth = "sucking"
                elif G_Mouth == "sucking":
                    $ G_Mouth = "tongue"
                elif G_Mouth == "tongue":
                    $ G_Mouth = "lipbite"
                else:
                    $ G_Mouth = "normal"
            "Toggle Blush":
                if G_Blush == 1:
                    $ G_Blush = 2
                elif G_Blush:
                    $ G_Blush = 0
                else:
                    $ G_Blush = 1
            "Back":

                return














label Display_Gwen(GwLoc=350, YLoc=50):



    show Gwen_Sprite:
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.5, 0.0)
        easeout .5 pos (GwLoc,YLoc)
    show Gwen_Sprite:
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.5, 0.0)
        pos (GwLoc,YLoc)
    return


label Close_Launch(GirlA=0, GirlB=0, XLoc=0, YLoc=0, XZoom=0):



    if GirlB:
        $ BO = [GirlA,GirlB]
    elif GirlA:
        $ BO = [GirlA]
    while BO:
        if BO[0] == KittyX or BO[0] == LauraX:
            $ BO[0].ArmPose = 1
        else:
            $ BO[0].ArmPose = 2
        $ YLoc = 100
        if GirlA == BO[0]:

            if BO[0] == KittyX:
                $ XLoc = 450
            elif BO[0] == RogueX:
                $ XLoc = 550
            else:
                $ XLoc = 500
            $ BO[0].sprite_layer = 100
            $ XZoom = -1.3
        elif GirlB == BO[0]:

            if BO[0] == EmmaX or LauraX:
                $ XLoc = 700
            else:
                $ XLoc = 715
            $ BO[0].sprite_layer = 75
            $ XZoom = 1.3

        if BO[0] == RogueX:
            call Rogue_Hide
            show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif BO[0] == KittyX:
            call Kitty_Hide
            show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == EmmaX:
            call Emma_Hide
            show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == LauraX:
            call Laura_Hide
            show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == JeanX:
            call Jean_Hide
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == StormX:
            call Storm_Hide
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif BO[0] == JubesX:
            call Jubes_Hide
            show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        $ BO.remove(BO[0])
    return
















label Les_Launch(Girl=0, XLoc=0, YLoc=0, XZoom=0, BO=[]):



    if Partner not in all_Girls:
        return
    $ BO = [Girl,Partner]
    while BO:
        if "unseen" in BO[0].recent_history:
            $ BO[0].eyes = "closed"
        elif Girl == BO[0]:
            if Girl == RogueX:
                $ BO[0].eyes = "side"
            elif Girl == EmmaX:
                $ BO[0].eyes = "sly"
            else:
                $ BO[0].eyes = "leftside"
        else:
            $ BO[0].eyes = "side"

        if BO[0] == KittyX or BO[0] == LauraX:
            $ BO[0].ArmPose = 1
        else:
            $ BO[0].ArmPose = 2
        $ YLoc = 100
        if Girl == BO[0]:

            if BO[0] == KittyX:
                $ XLoc = 450
            elif BO[0] == RogueX:
                $ XLoc = 550
            else:
                $ XLoc = 500
            $ BO[0].sprite_layer = 100
            $ XZoom = -1.3
        else:

            if BO[0] == EmmaX or LauraX:
                $ XLoc = 700
            else:
                $ XLoc = 715
            if BO[0] == KittyX:
                if RogueX in (Partner,Girl):
                    $ KittyX.sprite_layer = 100
                else:
                    $ KittyX.sprite_layer = 25
            else:
                $ BO[0].sprite_layer = 75
            $ XZoom = 1.3

        if BO[0] == RogueX:
            call Rogue_Hide
            show Rogue_Sprite zorder RogueX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif BO[0] == KittyX:
            call Kitty_Hide
            show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == EmmaX:
            call Emma_Hide
            show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == LauraX:
            call Laura_Hide
            show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == JeanX:
            call Jean_Hide
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.5, 0.0)
        elif BO[0] == StormX:
            call Storm_Hide
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        elif BO[0] == JubesX:
            call Jubes_Hide
            show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(XLoc,YLoc):
                alpha 1
                zoom 1
                xzoom XZoom
                yzoom 1.3
                offset (0,0)
                anchor (0.6, 0.0)
        $ BO.remove(BO[0])
    return

image CircleTest:
    contains:
        subpixel True
        "images/Clockbase.png"
        anchor (0.5,0.5)

        yzoom -1
    contains:

        ConditionSwitch(
            "Round>= 50", "ClockWhite",
            "True",Null(),
            ),
    contains:
        ConditionSwitch(
            "Round<= 50", "ClockRed",
            "True",Null(),
            ),
    contains:
        subpixel True
        "images/Clockface.png"
        anchor (0.5,0.5)

image ClockWhite:
    contains:
        subpixel True
        "images/Clockwhite.png"
        anchor (0.5,0.5)
        rotate -(int(Round *3.6))

image ClockRed:
    contains:
        subpixel True
        "images/Clockred.png"
        anchor (0.5,0.5)
        rotate -(int(Round *3.6-180))

image BlueScreen:

    alpha .1
    contains:
        Solid("#00B3D6", xysize=(1024, 768))

image SilhouetteBase:

    alpha .95
    contains:
        Solid("#14142d", xysize=(1024, 768))


image Silhouettes:





    contains:

        AlphaMask("SilhouetteBase","Storm_Sprite")


image Lick_Anim:
    anchor (0.5, 0.5)
    parallel:
        "images/Lick1.png"
        .8
        "images/Lick6.png"
        .2
        "images/Lick2.png"
        .2
        "images/Lick3.png"
        .2
        "images/Lick4.png"
        .8
        "images/Lick3.png"
        .1
        "images/Lick2.png"
        .1
        repeat
    parallel:
        pause .6
        easein .7 yoffset -15
        pause .3
        easein .8 yoffset 0
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
