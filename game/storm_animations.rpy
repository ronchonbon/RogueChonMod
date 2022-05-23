

image Storm_Sprite:
    LiveComposite(
        (450,950),
        (53,-45), "Storm_Sprite_hairback",
        (0,0), ConditionSwitch(

            "StormX.legs == 'skirt'", "images/StormSprite/Storm_Sprite_Legs_SkirtB.png",
            "StormX.upskirt", ConditionSwitch(

                        "StormX.legs == 'pants'", "images/StormSprite/Storm_Sprite_Legs_Pants_UpB.png",
                        "StormX.legs == 'yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPants_UpB.png",
                        "True", Null(),
                        ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.top == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket_Under.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "not StormX.underwear", Null(),
            "StormX.underwear_pulled_down", ConditionSwitch(

                    "not StormX.legs or StormX.upskirt or StormX.legs == 'skirt'", ConditionSwitch(

                            "StormX.underwear == 'cos_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos_DB.png",
                            "StormX.underwear == 'white_panties'", "images/StormSprite/Storm_Sprite_Panties_White_DB.png",


                            "True", "images/StormSprite/Storm_Sprite_Panties_Black_DB.png",
                            ),
                    "True", Null(),
                    ),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Body2.png",
            "True", "images/StormSprite/Storm_Sprite_Body1.png",
            ),







        (165,560), ConditionSwitch(

            "not StormX.grool", Null(),
            "StormX.legs and StormX.legs != 'skirt' and not StormX.upskirt", Null(),
            "StormX.underwear and not StormX.underwear_pulled_down and StormX.grool <= 1", Null(),
            "StormX.grool == 1", ConditionSwitch(
                    "StormX.underwear and StormX.underwear_pulled_down", AlphaMask("Wet_Drip","Storm_Drip_MaskP"),
                    "StormX.legs and StormX.legs != 'skirt'", AlphaMask("Wet_Drip","Storm_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Storm_Drip_Mask"),
                    ),
            "True", ConditionSwitch(
                    "StormX.underwear and StormX.underwear_pulled_down", AlphaMask("Wet_Drip2","Storm_Drip_MaskP"),
                    "StormX.legs and StormX.legs != 'skirt'", AlphaMask("Wet_Drip2","Storm_Drip_MaskP"),
                    "StormX.underwear", AlphaMask("Wet_Drip","Storm_Drip_Mask"),
                    "True", AlphaMask("Wet_Drip2","Storm_Drip_Mask"),
                    ),
            ),
        (165,560), ConditionSwitch(

            "'in' not in StormX.spunk and 'anal' not in StormX.spunk", Null(),
            "StormX.legs and StormX.legs != 'skirt' and not StormX.upskirt", Null(),
            "StormX.underwear and not StormX.underwear_pulled_down and StormX.grool <= 1", Null(),
            "True", ConditionSwitch(
                    "StormX.underwear and StormX.underwear_pulled_down", AlphaMask("Spunk_Drip2","Storm_Drip_MaskP"),

                    "StormX.underwear", AlphaMask("Spunk_Drip","Storm_Drip_Mask"),
                    "True", AlphaMask("Spunk_Drip2","Storm_Drip_Mask"),
                    ),
            ),

        (0,0), ConditionSwitch(

            "StormX.pubes", "images/StormSprite/Storm_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.piercings", Null(),
            "StormX.underwear and not StormX.underwear_pulled_down", Null(),
            "StormX.legs != 'skirt' and StormX.legs and not StormX.upskirt", Null(),
            "StormX.piercings == 'barbell'", "images/StormSprite/Storm_Sprite_Barbell_Pussy.png",
            "StormX.piercings == 'ring'", "images/StormSprite/Storm_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.accessory == 'rings' or StormX.top == '_jacket'", Null(),
            "StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_ArmRings1.png",
            "True", "images/StormSprite/Storm_Sprite_ArmRings2.png",
            ),
        (0,0), ConditionSwitch(

            "StormX.top_pulled_up", "images/StormSprite/Storm_Sprite_Tits.png",
            "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Tits_Up.png",
            "True", "images/StormSprite/Storm_Sprite_Tits.png",
            ),
        (0,0), ConditionSwitch(

            "not StormX.piercings", Null(),

            "StormX.top_pulled_up", Null(),

            "StormX.piercings == 'barbell'", ConditionSwitch(

                    "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsU.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsL.png",
                    ),

            "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Ring_TitsUCU.png",
            "StormX.top or StormX.bra", "images/StormSprite/Storm_Sprite_Ring_TitsLCU.png",
            "True", "images/StormSprite/Storm_Sprite_Ring_TitsL.png",
            ),


        (0,0), ConditionSwitch(


            "StormX.neck == 'gold necklace'", "images/StormSprite/Storm_Sprite_Necklace1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.top_pulled_up", ConditionSwitch(

                    "StormX.bra == 'cos_bra'", "images/StormSprite/Storm_Sprite_Chest_Cos_Up.png",
                    "StormX.bra == 'black_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_Up.png",
                    "StormX.bra == 'lace_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_Up.png",
                    "StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Chest_Sportsbra_Up.png",
                    "StormX.bra == 'bikini_top'", "images/StormSprite/Storm_Sprite_Chest_Bikini_Up.png",
                    "StormX.bra == 'tube_top'", "images/StormSprite/Storm_Sprite_Chest_Tube_Up.png",
                    "True", Null(),
                    ),
            "StormX.bra == 'cos_bra'", "images/StormSprite/Storm_Sprite_Chest_Cos.png",
            "StormX.bra == 'black_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra.png",
            "StormX.bra == 'lace_bra'", "images/StormSprite/Storm_Sprite_Chest_LaceBra.png",
            "StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Chest_Sportsbra.png",
            "StormX.bra == 'bikini_top'", "images/StormSprite/Storm_Sprite_Chest_Bikini.png",
            "StormX.bra == 'tube_top'", "images/StormSprite/Storm_Sprite_Chest_Tube.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not StormX.piercings or (not StormX.top and not StormX.bra and not StormX.top_pulled_up)", Null(),
            "StormX.top_pulled_up", Null(),
            "StormX.piercings == 'barbell'", ConditionSwitch(

                    "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsUC.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsLC.png",
                    ),
            "StormX.piercings == 'ring' and (StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra')", "images/StormSprite/Storm_Sprite_Ring_TitsUC.png",
            "StormX.piercings == 'ring'", "images/StormSprite/Storm_Sprite_Ring_TitsLC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "StormX.hose == 'stockings'", "images/StormSprite/Storm_Sprite_Hose_Stockings.png",
            "StormX.hose == 'stockings_and_garterbelt'", "images/StormSprite/Storm_Sprite_Hose_StockingsandGarter.png",
            "StormX.hose == 'garterbelt'", "images/StormSprite/Storm_Sprite_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.accessory == 'rings' or StormX.legs == 'pants' or StormX.legs == 'yoga_pants'", Null(),
            "True", "images/StormSprite/Storm_Sprite_LegRings.png",
            ),
        (0,0), ConditionSwitch(

            "not StormX.underwear", Null(),
            "StormX.underwear_pulled_down", ConditionSwitch(

                    "not StormX.legs or StormX.upskirt or StormX.legs == 'skirt'", ConditionSwitch(

                            "StormX.underwear == 'cos_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos_D.png",
                            "StormX.underwear == 'white_panties'", "images/StormSprite/Storm_Sprite_Panties_White_D.png",
                            "StormX.underwear == 'lace_panties'", "images/StormSprite/Storm_Sprite_Panties_Lace_D.png",
                            "StormX.underwear == 'bikini_bottoms'", "images/StormSprite/Storm_Sprite_Panties_Bikini_D.png",
                            "True", "images/StormSprite/Storm_Sprite_Panties_Black_D.png",
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "StormX.grool", ConditionSwitch(

                        "StormX.underwear == 'cos_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos.png",
                        "StormX.underwear == 'white_panties'", "images/StormSprite/Storm_Sprite_Panties_WhiteW.png",
                        "StormX.underwear == 'lace_panties'", "images/StormSprite/Storm_Sprite_Panties_Lace.png",
                        "StormX.underwear == 'bikini_bottoms' and (StormX.bra != 'bikini_top' or StormX.top_pulled_up)", "images/StormSprite/Storm_Sprite_Panties_BikiniL.png",
                        "StormX.underwear == 'bikini_bottoms'", "images/StormSprite/Storm_Sprite_Panties_Bikini.png",
                        "True", "images/StormSprite/Storm_Sprite_Panties_BlackW.png",
                        ),
                    "True", ConditionSwitch(

                        "StormX.underwear == 'cos_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos.png",
                        "StormX.underwear == 'white_panties'", "images/StormSprite/Storm_Sprite_Panties_White.png",
                        "StormX.underwear == 'lace_panties'", "images/StormSprite/Storm_Sprite_Panties_Lace.png",
                        "StormX.underwear == 'bikini_bottoms' and (StormX.bra != 'bikini_top' or StormX.top_pulled_up)", "images/StormSprite/Storm_Sprite_Panties_BikiniL.png",
                        "StormX.underwear == 'bikini_bottoms'", "images/StormSprite/Storm_Sprite_Panties_Bikini.png",
                        "True", "images/StormSprite/Storm_Sprite_Panties_Black.png",
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.hose == 'pantyhose' and (not StormX.underwear_pulled_down or not StormX.underwear)", "images/StormSprite/Storm_Sprite_Hose_Pantyhose.png",
            "StormX.hose == 'ripped_pantyhose' and (not StormX.underwear_pulled_down or not StormX.underwear)", "images/StormSprite/Storm_Sprite_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.legs", Null(),
            "StormX.upskirt", ConditionSwitch(

                        "StormX.legs == 'pants'", "images/StormSprite/Storm_Sprite_Legs_Pants_Up.png",
                        "StormX.legs == 'yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPants_Up.png",
                        "StormX.legs == 'skirt'", "images/StormSprite/Storm_Sprite_Legs_Skirt_Up.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(

                    "StormX.grool", ConditionSwitch(

                        "StormX.legs == 'pants'", "images/StormSprite/Storm_Sprite_Legs_PantsW.png",
                        "StormX.legs == 'yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPantsW.png",
                        "StormX.legs == 'skirt'", "images/StormSprite/Storm_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(

                        "StormX.legs == 'pants'", "images/StormSprite/Storm_Sprite_Legs_Pants.png",
                        "StormX.legs == 'yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPants.png",
                        "StormX.legs == 'skirt'", "images/StormSprite/Storm_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.legs == 'skirt' or StormX.legs == 'pants'", Null(),
            "StormX.piercings == 'barbell'", ConditionSwitch(

                    "StormX.legs and not StormX.upskirt", "images/StormSprite/Storm_Sprite_Barbell_PussyC.png",
                    "StormX.underwear and not StormX.underwear_pulled_down", "images/StormSprite/Storm_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "StormX.piercings == 'ring'", ConditionSwitch(

                    "StormX.legs and not StormX.upskirt", "images/StormSprite/Storm_Sprite_Ring_PussyC.png",
                    "StormX.underwear and not StormX.underwear_pulled_down", "images/StormSprite/Storm_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.legs and not StormX.upskirt", Null(),
            "'in' in StormX.spunk or 'anal' in StormX.spunk", "images/StormSprite/Storm_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.wet", Null(),
            "(StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra') and StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_Water_Tight1.png",
            "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Water_Tight2.png",
            "StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_Water_Loose1.png",
            "True", "images/StormSprite/Storm_Sprite_Water_Loose2.png",
            ),


        (0,0), ConditionSwitch(

            "StormX.neck == 'rings'", "images/StormSprite/Storm_Sprite_Necklace3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.top_pulled_up", ConditionSwitch(

                    "StormX.top == 'white_shirt'", "images/StormSprite/Storm_Sprite_Over_WhiteShirt_Up.png",
                    "StormX.top == '_jacket' and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Over_Jacket2_Up.png",
                    "StormX.top == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket1_Up.png",

                    "True", Null(),
                    ),


            "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra'", ConditionSwitch(

                    "StormX.top == 'white_shirt'", "images/StormSprite/Storm_Sprite_Over_WhiteShirtU.png",
                    "StormX.top == '_jacket' and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Over_Jacket2U.png",
                    "StormX.top == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket1U.png",
                    "True", Null(),
                    ),
            "StormX.top == 'white_shirt'", "images/StormSprite/Storm_Sprite_Over_WhiteShirtL.png",
            "StormX.top == '_jacket' and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Over_Jacket2L.png",
            "StormX.top == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket1L.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.top_pulled_up or StormX.top != '_jacket'", Null(),

            "StormX.bra == 'black_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_UpJ.png",
            "StormX.bra == 'lace_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_UpJ.png",
            "StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Chest_Sportsbra_UpJ.png",
            "StormX.bra == 'bikini_top'", "images/StormSprite/Storm_Sprite_Chest_Bikini_UpJ.png",
            "StormX.bra == 'tube_top'", "images/StormSprite/Storm_Sprite_Chest_Tube_UpJ.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.piercings or (not StormX.top and not StormX.bra and not StormX.top_pulled_up)", Null(),
            "StormX.top == '_jacket' and not StormX.top_pulled_up", Null(),
            "StormX.piercings == 'barbell'", ConditionSwitch(

                    "StormX.top_pulled_up", "images/StormSprite/Storm_Sprite_Barbell_TitsL.png",
                    "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsUC.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsLC.png",
                    ),
            "StormX.top_pulled_up", "images/StormSprite/Storm_Sprite_Ring_TitsL.png",
            "StormX.piercings == 'ring' and (StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra')", "images/StormSprite/Storm_Sprite_Ring_TitsUC.png",
            "StormX.piercings == 'ring'", "images/StormSprite/Storm_Sprite_Ring_TitsLC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'belly' in StormX.spunk", "images/StormSprite/Storm_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' in StormX.spunk and (StormX.bra == 'black_bra' or StormX.bra == 'lace_bra' or StormX.bra == 'sports_bra')", "images/StormSprite/Storm_Sprite_Spunk_TitsU.png",
            "'tits' in StormX.spunk", "images/StormSprite/Storm_Sprite_Spunk_TitsL.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_Arms1a.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.top == '_jacket'", "images/StormSprite/Storm_Sprite_Over_JacketC.png",
            "True", Null(),
            ),
        (53,-45), "Storm_Sprite_Head",
        (0,0), ConditionSwitch(

            "StormX.arm_pose != 1 and renpy.showing('Storm_HJ_Animation')", Null(),
            "StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Arms2a.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.wet and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Water_Arm2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.arm_pose != 1 and StormX.top == '_jacket' and renpy.showing('Storm_HJ_Animation')", "images/StormSprite/Storm_Sprite_Over_Jacket2H.png",
            "StormX.arm_pose != 1 and StormX.top == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket2A.png",
            "StormX.arm_pose != 1 and StormX.accessory == 'rings'", "images/StormSprite/Storm_Sprite_ArmRings2Top.png",
            "True", Null(),
            ),
















        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != StormX", Null(),


            "girl_offhand_action == 'fondle_pussy'", At('GirlGropePussy_StormSelf',GirlGropePussy_Storm1()),
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Storm",

                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeRightBreast_Storm",

                    "True", "GirlGropeBothBreast_Storm",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Storm",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Storm",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Storm",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Storm",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Storm",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_offhand_action or second_girl_primary_action != 'masturbation' or focused_Girl == StormX", Null(),


            "second_girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and StormX.lust >= 70", "GirlFingerPussy_Storm",
            "second_girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Storm",
            "second_girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Storm",
            "second_girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(


            "not primary_action or focused_Girl != StormX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Storm",
            "primary_action == 'fondle_thighs'", "GropeThigh_Storm",
            "primary_action == 'fondle_breasts'", "GropeLeftBreast_Storm",
            "primary_action == 'suck breasts'", "LickRightBreast_Storm",
            "primary_action == 'fondle_pussy' and action_speed == 2", "FingerPussy_Storm",
            "primary_action == 'fondle_pussy'", "GropePussy_Storm",
            "primary_action == 'eat_pussy'", "Lickpussy_Storm",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Storm",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Storm",
            "primary_action == 'vibrator anal'", "VibratorAnal_Storm",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Storm",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not offhand_action or focused_Girl != StormX", Null(),


            "offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' and primary_action == 'suck breasts'", "GropeLeftBreast_Storm",

                    "True", "GropeRightBreast_Storm",

                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast_Storm",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck breasts'", "LickLeftBreast_Storm",
            "offhand_action == 'fondle_pussy'", "GropePussy_Storm",
            "offhand_action == 'eat_pussy'", "Lickpussy_Storm",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Storm",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Storm",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Storm",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Storm",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Storm",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_primary_action or focused_Girl != StormX", Null(),


            "second_girl_primary_action == 'fondle_pussy'", At('UI_PartnerHand',GirlGropePussy_Storm1()),
            "second_girl_primary_action == 'eat_pussy'", "Lickpussy_Storm",
            "second_girl_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Storm",
            "second_girl_primary_action == 'suck breasts'", "LickRightBreast_Storm",
            "second_girl_primary_action == 'fondle_breasts'", At('UI_PartnerHand',GirlGropeRightBreast_Storm()),






            "second_girl_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_primary_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action != 'lesbian' or focused_Girl == StormX or not girl_offhand_action", Null(),



            "girl_offhand_action == 'fondle_pussy'", At('GirlGropePussy_StormSelf',GirlGropePussy_Storm1()),
            "girl_offhand_action == 'eat_pussy'", "Lickpussy_Storm",
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Storm",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast_Storm",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Storm",

                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeRightBreast_Storm",

                    "girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Storm",

                    "True", "GirlGropeRightBreast_Storm",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    yoffset 15
    zoom 0.75

image Storm_Sprite_hairback:
    contains:
        ConditionSwitch(

                "StormX.top == 'towel'", "images/StormSprite/Storm_Sprite_Over_Towel_Under.png",
                "True", Null(),
                ),
    contains:
        ConditionSwitch(




                "StormX.top == 'towel'", Null(),
                "StormX.hair == 'wethawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back_Wet.png",
                "StormX.hair == 'mohawk' and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back_Wet.png",
                "StormX.hair == 'mohawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back.png",
                "StormX.hair == '_wet'", "images/StormSprite/Storm_Sprite_Hair_Long_Back_Wet.png",
                "StormX.hair and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Long_Back_Wet.png",
                "StormX.hair == 'short'", Null(),
                "StormX.hair", "images/StormSprite/Storm_Sprite_Hair_Long_Back.png",
                "True", Null(),
                ),

    anchor (0.5, 0.5)
    zoom 0.47




























image Storm_Sprite_Head:
    LiveComposite(
        (900,900),





        (0,0), ConditionSwitch(

                "StormX.blushing >= 2", "images/StormSprite/Storm_Sprite_Head_Blush.png",

                "True", "images/StormSprite/Storm_Sprite_Head_Base.png",
                ),
        (0,0), ConditionSwitch(
            "'chin' not in StormX.spunk", Null(),

            "True", "images/StormSprite/Storm_Sprite_Spunk_Chin.png",
            ),














        (0,0), ConditionSwitch(













            "True", ConditionSwitch(
                    "StormX.mouth == 'lipbite'", "images/StormSprite/Storm_Sprite_Mouth_Lipbite.png",
                    "StormX.mouth == 'sucking'", "images/StormSprite/Storm_Sprite_Mouth_Open.png",
                    "StormX.mouth == 'kiss'", "images/StormSprite/Storm_Sprite_Mouth_Kiss.png",
                    "StormX.mouth == 'sad'", "images/StormSprite/Storm_Sprite_Mouth_Sad.png",
                    "StormX.mouth == 'smile'", "images/StormSprite/Storm_Sprite_Mouth_Smile.png",
                    "StormX.mouth == 'surprised'", "images/StormSprite/Storm_Sprite_Mouth_Kiss.png",
                    "StormX.mouth == 'tongue'", "images/StormSprite/Storm_Sprite_Mouth_Tongue.png",
                    "StormX.mouth == 'grimace'", "images/StormSprite/Storm_Sprite_Mouth_Smile.png",
                    "StormX.mouth == 'smirk'", "images/StormSprite/Storm_Sprite_Mouth_Smirk.png",
                    "True", "images/StormSprite/Storm_Sprite_Mouth_Normal.png",
                    ),
            ),


        (0,0), ConditionSwitch(
            "'mouth' not in StormX.spunk", Null(),


            "StormX.mouth == 'sucking'", "images/StormSprite/Storm_Sprite_Spunk_Tongue.png",
            "StormX.mouth == 'kiss'", "images/StormSprite/Storm_Sprite_Spunk_Kiss.png",
            "StormX.mouth == 'sad'", "images/StormSprite/Storm_Sprite_Spunk_Sad.png",
            "StormX.mouth == 'smile'", "images/StormSprite/Storm_Sprite_Spunk_Smile.png",
            "StormX.mouth == 'surprised'", "images/StormSprite/Storm_Sprite_Spunk_Kiss.png",
            "StormX.mouth == 'tongue'", "images/StormSprite/Storm_Sprite_Spunk_Tongue.png",


            "True", "images/StormSprite/Storm_Sprite_Spunk_Smirk.png",
            ),

        (0,0), ConditionSwitch(

            "StormX.brows == 'angry'", "images/StormSprite/Storm_Sprite_Brows_Angry.png",
            "StormX.brows == 'sad'", "images/StormSprite/Storm_Sprite_Brows_Sad.png",
            "StormX.brows == 'surprised'", "images/StormSprite/Storm_Sprite_Brows_Surprised.png",
            "StormX.brows == 'confused'", "images/StormSprite/Storm_Sprite_Brows_Confused.png",
            "True", "images/StormSprite/Storm_Sprite_Brows_Normal.png",
            ),
        (0,0), "Storm Blink",
        (0,0), ConditionSwitch(

            "not StormX.wet", Null(),
            "True", "images/StormSprite/Storm_Sprite_Head_Water.png",
            ),
        (0,0), "images/StormSprite/Storm_Sprite_Earrings.png",
        (0,0), ConditionSwitch(


            "StormX.top == 'towel'", Null(),
            "StormX.hair == 'wethawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Wet.png",
            "StormX.hair == 'mohawk' and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Wet.png",
            "StormX.hair == 'mohawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk.png",
            "StormX.hair == '_wet'", "images/StormSprite/Storm_Sprite_Hair_Long_Wet.png",
            "StormX.hair and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Long_Wet.png",
            "StormX.hair == 'short'", "images/StormSprite/Storm_Sprite_Hair_Short.png",
            "renpy.showing('Storm_SexSprite')", "images/StormSprite/Storm_Sprite_Hair_Long_Sex.png",
            "StormX.hair", "images/StormSprite/Storm_Sprite_Hair_Long.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "StormX.top == 'towel'", "images/StormSprite/Storm_Sprite_Over_Towel.png",
            "True", Null(),
            ),






        (0,0), ConditionSwitch(

            "'hair' in StormX.spunk and StormX.hair == 'short'", "images/StormSprite/Storm_Sprite_Spunk_Hair3.png",
            "'hair' in StormX.spunk and StormX.hair == 'mohawk'", "images/StormSprite/Storm_Sprite_Spunk_Hair2.png",
            "'hair' in StormX.spunk and StormX.hair == 'long'", "images/StormSprite/Storm_Sprite_Spunk_Hair1.png",
            "'facial' in StormX.spunk", "images/StormSprite/Storm_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.hair == 'short'", "images/StormSprite/Storm_Sprite_Earrings.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom 0.47


image Storm Blink:
    ConditionSwitch(
    "StormX.eyes == 'sexy'", "images/StormSprite/Storm_Sprite_Eyes_Sexy.png",
    "StormX.eyes == 'side'", "images/StormSprite/Storm_Sprite_Eyes_Side.png",
    "StormX.eyes == 'surprised'", "images/StormSprite/Storm_Sprite_Eyes_Surprised.png",
    "StormX.eyes == 'normal'", "images/StormSprite/Storm_Sprite_Eyes_Normal.png",
    "StormX.eyes == 'stunned'", "images/StormSprite/Storm_Sprite_Eyes_Stunned.png",
    "StormX.eyes == 'down'", "images/StormSprite/Storm_Sprite_Eyes_Down.png",
    "StormX.eyes == 'closed'", "images/StormSprite/Storm_Sprite_Eyes_Closed.png",
    "StormX.eyes == 'leftside'", "images/StormSprite/Storm_Sprite_Eyes_Leftside.png",
    "StormX.eyes == 'manic'", "images/StormSprite/Storm_Sprite_Eyes_Normal.png",
    "StormX.eyes == 'white'", "images/StormSprite/Storm_Sprite_Eyes_White.png",
    "StormX.eyes == 'squint'", "Storm_Squint",
    "True", "images/StormSprite/Storm_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/StormSprite/Storm_Sprite_Eyes_Closed.png"
    0.25
    repeat

image Storm_Squint:
    "images/StormSprite/Storm_Sprite_Eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/StormSprite/Storm_Sprite_Eyes_Sexy.png"
    0.25
    repeat



image Storm_Photo:
    "images/StormSprite/StormPhoto.png"


image Storm_Drip_Mask:

    contains:
        "images/StormSprite/Storm_Sprite_WetMask.png"
        offset (-145,-560)

image Storm_Drip_MaskP:

    contains:
        "images/StormSprite/Storm_Sprite_WetMaskP.png"
        offset (-145,-560)













label Storm_Doggy_Launch(Line=primary_action):

    return

label Storm_Doggy_Reset:

    return
































image Storm_SexSprite:
    LiveComposite(
        (1120,960),





        (0,0), ConditionSwitch(


                "Player.cock_position == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Storm_Sex_Fucking_Speed3",
                        "action_speed >= 2", "Storm_Sex_Fucking_Speed2",
                        "action_speed ", "Storm_Sex_Fucking_Speed1",
                        "True", "Storm_Sex_Fucking_Speed0",
                        ),
                "Player.cock_position == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Storm_Sex_Anal_Speed3",
                        "action_speed >= 2", "Storm_Sex_Anal_Speed2",
                        "action_speed ", "Storm_Sex_Anal_Speed1",
                        "True", "Storm_Sex_Anal_Speed0",
                        ),
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 2","Storm_Sex_Hotdog_Speed2",
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 1","Storm_Sex_Hotdog_Speed1",
                "Player.cock_position == 'foot'", ConditionSwitch(

                        "action_speed >= 2", "Storm_Sex_FJ_Speed2",
                        "action_speed ", "Storm_Sex_FJ_Speed1",
                        "True", "Storm_Sex_FJ_Speed0",
                        ),

                "True", "Storm_Sex_Static",
                ),

























        )
    align (0.6,0.0)
    pos (650,393)
    zoom 0.7




image Storm_Sex_Body:
    LiveComposite(

        (1120,840),
        (245,-225), "Storm_hairback_Sex",
        (0,0), "images/StormSex/Storm_Sex_Body.png",






        (0,0), ConditionSwitch(

            "not StormX.accessory == 'rings' or StormX.top == '_jacket'", Null(),
            "True", "images/StormSex/Storm_Sex_Arms_Ring.png",
            ),
        (0,0), ConditionSwitch(

            "not StormX.bra", Null(),
            "StormX.bra == 'cos_bra'", "images/StormSex/Storm_Sex_Chest_Cos.png",
            "StormX.bra == 'tube_top'", "images/StormSex/Storm_Sex_Chest_Tube.png",
            "StormX.bra == 'black_bra'", "images/StormSex/Storm_Sex_Chest_Bra.png",
            "StormX.bra == 'lace_bra'", "images/StormSex/Storm_Sex_Chest_Bra.png",
            "not StormX.top_pulled_up", ConditionSwitch(

                    "StormX.bra == 'sports_bra'", "images/StormSex/Storm_Sex_Chest_SportsBra.png",
                    "StormX.bra == 'bikini_top' and StormX.underwear == 'bikini_bottoms'", "images/StormSex/Storm_Sex_Chest_Bikini_Combo.png",
                    "StormX.bra == 'bikini_top'", "images/StormSex/Storm_Sex_Chest_Bikini.png",

                    "True", Null(),
                    ),








            "True", ConditionSwitch(

                    "StormX.bra == 'sports_bra'", "images/StormSex/Storm_Sex_Chest_SportsBra_Up.png",

                    "StormX.bra == 'bikini_top'", "images/StormSex/Storm_Sex_Chest_Bikini_Up.png",

                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.wet", "images/StormSex/Storm_Sex_Wet_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.top == 'white_shirt' and StormX.top_pulled_up", "images/StormSex/Storm_Sex_Chest_Shirt_Up.png",
            "StormX.top == 'white_shirt'", "images/StormSex/Storm_Sex_Chest_Shirt.png",
            "StormX.top == '_jacket'", "images/StormSex/Storm_Sex_Chest_Jacket.png",
            "True", Null(),













            ),








        (0,0), ConditionSwitch(

            "StormX.neck == 'rings'", "images/StormSex/Storm_Sex_Neck_Ring.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "'belly' in StormX.spunk", "images/StormSex/Storm_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "'tits' in StormX.spunk", "images/StormSex/Storm_Sex_Spunk_Tits_Back.png",
            "True", Null(),
            ),

        (220,-162), "Storm_Head_Sex",
        )
    yoffset -163



image Storm_Head_Sex:

    "Storm_Sprite_Head"
    zoom 1.25
    anchor (0.5,0.5)
    rotate -7

image Storm_hairback_Sex:

    "Storm_Sprite_hairback"
    zoom 1.25
    anchor (0.5,0.5)
    rotate -7


image Storm_Sex_Tits:
    LiveComposite(

        (1120,960),



        (0,0), ConditionSwitch(

            "StormX.bra == 'cos_bra'", "images/StormSex/Storm_Sex_Tits_Cos.png",
            "True", "images/StormSex/Storm_Sex_Tits.png",
            ),

        (0,0), ConditionSwitch(

            "StormX.piercings == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Tits_Barbell.png",
            "StormX.piercings == 'ring'", "images/StormSex/Storm_Sex_Pierce_Tits_Ring.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.bra", Null(),
            "StormX.bra == 'cos_bra'", Null(),
            "not StormX.top_pulled_up", ConditionSwitch(

                    "StormX.bra == 'tube_top'", "images/StormSex/Storm_Sex_Tits_Tube.png",
                    "StormX.bra == 'black_bra'", "images/StormSex/Storm_Sex_Tits_Bra.png",
                    "StormX.bra == 'lace_bra'", "images/StormSex/Storm_Sex_Tits_LaceBra.png",
                    "StormX.bra == 'sports_bra'", "images/StormSex/Storm_Sex_Tits_SportsBra.png",
                    "StormX.bra == 'bikini_top'", "images/StormSex/Storm_Sex_Tits_Bikini.png",
                    "True", Null(),
                    ),








            "True", ConditionSwitch(

                    "StormX.bra == 'tube_top'", "images/StormSex/Storm_Sex_Tits_Tube_Down.png",


                    "StormX.bra == 'sports_bra'", "images/StormSex/Storm_Sex_Tits_SportsBra_Up.png",
                    "StormX.bra == 'bikini_top'", "images/StormSex/Storm_Sex_Tits_Bikini_Up.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.wet", "images/StormSex/Storm_Sex_Wet_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.top", Null(),
            "StormX.top == 'white_shirt' and StormX.top_pulled_up", "images/StormSex/Storm_Sex_Tits_Shirt_Up.png",
            "StormX.top == 'white_shirt'", "images/StormSex/Storm_Sex_Tits_Shirt.png",
            "True", Null(),
            ),




























        (0,0), ConditionSwitch(

            "(not StormX.bra and not StormX.top) or StormX.top_pulled_up", Null(),
            "StormX.piercings == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Tits_BarbellC.png",
            "StormX.piercings == 'ring'", "images/StormSex/Storm_Sex_Pierce_Tits_RingC.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "'tits' in StormX.spunk", "images/StormSex/Storm_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Storm_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Storm_Sex_Fondle_Breasts",
            "True", Null()
            ),

        )
    yoffset -163


image Storm_Sex_Lick_Breasts:
    "licking"
    zoom 0.7
    offset (400,350)

image Storm_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.5
    offset (190,-200)


image Storm_Sex_Legs:
    LiveComposite(

        (1120,960),








        (0,0), ConditionSwitch(

            "StormX.legs == 'skirt'", "images/StormSex/Storm_Sex_Legs_Skirt_Back.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "'anal' in StormX.spunk", "images/StormSex/Storm_Sex_Spunk_Anal_Closed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal' and show_feet", "images/StormSex/Storm_Sex_Legs_FJ_Anal.png",
            "show_feet", "images/StormSex/Storm_Sex_Legs_FJ.png",
            "Player.sprite and Player.cock_position == 'anal'", "images/StormSex/Storm_Sex_Legs_Anal.png",
            "True", "images/StormSex/Storm_Sex_Legs.png",
            ),
        (0,0), ConditionSwitch(

            "not StormX.wet", Null(),
            "show_feet", "images/StormSex/Storm_Sex_Wet_Legs_FJ.png",
            "True", "images/StormSex/Storm_Sex_Wet_Legs.png",
            ),

        (0,0), "Storm_Sex_Anus",


        (0,0), "Storm_Sex_Pussy",



        (0,0), ConditionSwitch(

            "show_feet",ConditionSwitch(

                    "StormX.hose == 'stockings_and_garterbelt'", "images/StormSex/Storm_Sex_Hose_StockingsGarter_FJ.png",
                    "StormX.hose == 'garterbelt'", "images/StormSex/Storm_Sex_Hose_Garter_FJ.png",
                    "StormX.hose == 'stockings'", "images/StormSex/Storm_Sex_Hose_Stockings_FJ.png",
                    "True", Null(),
                    ),
            "StormX.hose == 'stockings_and_garterbelt'", "images/StormSex/Storm_Sex_Hose_StockingsGarter.png",
            "StormX.hose == 'garterbelt'", "images/StormSex/Storm_Sex_Hose_Garter.png",
            "StormX.hose == 'stockings'", "images/StormSex/Storm_Sex_Hose_Stockings.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.accessory == 'rings' or StormX.legs == 'pants' or StormX.legs == 'yoga_pants'", Null(),
            "show_feet", "images/StormSex/Storm_Sex_LegRings_FJ.png",
            "True", "images/StormSex/Storm_Sex_LegRings.png",
            ),
        (0,0), ConditionSwitch(

            "StormX.legs and StormX.legs != 'skirt' and not StormX.upskirt", Null(),
            "StormX.underwear_pulled_down",ConditionSwitch(

                    "StormX.underwear == 'cos_panties' and show_feet", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Down.png",
                    "StormX.underwear == 'cos_panties'", "images/StormSex/Storm_Sex_Panties_Cos_Down.png",
                    "StormX.underwear == 'white_panties' and show_feet", "images/StormSex/Storm_Sex_Panties_White_FJ_Down.png",
                    "StormX.underwear == 'white_panties'", "images/StormSex/Storm_Sex_Panties_White_Down.png",
                    "StormX.underwear and show_feet", "images/StormSex/Storm_Sex_Panties_Black_FJ_Down.png",
                    "StormX.underwear", "images/StormSex/Storm_Sex_Panties_Black_Down.png",
                    "True", Null(),
                    ),
            "show_feet",ConditionSwitch(

                    "StormX.underwear == 'cos_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Wet.png",
                    "StormX.underwear == 'cos_panties'", "images/StormSex/Storm_Sex_Panties_Cos_FJ.png",
                    "StormX.underwear == 'white_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_White_FJ_Wet.png",
                    "StormX.underwear == 'white_panties'", "images/StormSex/Storm_Sex_Panties_White_FJ.png",
                    "StormX.underwear == 'lace_panties'", "images/StormSex/Storm_Sex_Panties_Lace_FJ.png",
                    "StormX.underwear == 'bikini_bottoms' and (StormX.bra != 'bikini_top' or StormX.top_pulled_up)", "images/StormSex/Storm_Sex_Panties_Bikini_FJ_Top.png",
                    "StormX.underwear == 'bikini_bottoms'", "images/StormSex/Storm_Sex_Panties_Bikini_FJ.png",
                    "StormX.underwear and StormX.grool", "images/StormSex/Storm_Sex_Panties_Black_FJ_Wet.png",
                    "StormX.underwear", "images/StormSex/Storm_Sex_Panties_Black_FJ.png",
                    "True", Null(),
                    ),
            "StormX.underwear == 'cos_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_Cos_Wet.png",
            "StormX.underwear == 'cos_panties'", "images/StormSex/Storm_Sex_Panties_Cos.png",
            "StormX.underwear == 'white_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_White_Wet.png",
            "StormX.underwear == 'white_panties'", "images/StormSex/Storm_Sex_Panties_White.png",
            "StormX.underwear == 'lace_panties'", "images/StormSex/Storm_Sex_Panties_Lace.png",
            "StormX.underwear == 'bikini_bottoms' and (StormX.bra != 'bikini_top' or StormX.top_pulled_up)", "images/StormSex/Storm_Sex_Panties_Bikini_Top.png",
            "StormX.underwear == 'bikini_bottoms'", "images/StormSex/Storm_Sex_Panties_Bikini.png",
            "StormX.underwear and StormX.grool", "images/StormSex/Storm_Sex_Panties_Black_Wet.png",
            "StormX.underwear", "images/StormSex/Storm_Sex_Panties_Black.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(




            "not StormX.underwear and StormX.hose != 'pantyhose'", Null(),
            "((StormX.underwear or StormX.hose == 'pantyhose') and StormX.underwear_pulled_down)", Null(),

            "StormX.piercings == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.piercings == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "StormX.underwear and StormX.underwear_pulled_down", Null(),
            "show_feet",ConditionSwitch(

                    "StormX.hose == 'pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png",
                    "StormX.hose == 'ripped_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJHoled.png",
                    "True", Null(),
                    ),
            "StormX.hose == 'pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose.png",
            "StormX.hose == 'ripped_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "StormX.legs == 'skirt' and show_feet", "images/StormSex/Storm_Sex_Legs_Skirt_FJ.png",
            "StormX.upskirt",ConditionSwitch(

                    "StormX.legs == 'skirt'", "images/StormSex/Storm_Sex_Legs_Skirt_Up.png",
                    "StormX.legs == 'pants' and show_feet", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Down.png",
                    "StormX.legs == 'pants'", "images/StormSex/Storm_Sex_Legs_Pants_Down.png",
                    "StormX.legs == 'yoga_pants' and show_feet", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Down.png",
                    "StormX.legs == 'yoga_pants'", "images/StormSex/Storm_Sex_Legs_YogaPants_Down.png",
                    "True", Null(),
                    ),
            "show_feet",ConditionSwitch(

                    "StormX.legs == 'pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Wet.png",
                    "StormX.legs == 'pants'", "images/StormSex/Storm_Sex_Legs_Pants_FJ.png",
                    "StormX.legs == 'yoga_pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Wet.png",
                    "StormX.legs == 'yoga_pants'", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ.png",
                    "True", Null(),
                    ),
            "StormX.legs == 'skirt'", "images/StormSex/Storm_Sex_Legs_Skirt.png",
            "StormX.legs == 'pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_Pants_Wet.png",
            "StormX.legs == 'pants'", "images/StormSex/Storm_Sex_Legs_Pants.png",
            "StormX.legs == 'yoga_pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_YogaPants_Wet.png",
            "StormX.legs == 'yoga_pants'", "images/StormSex/Storm_Sex_Legs_YogaPants.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(




            "not StormX.legs", Null(),
            "StormX.legs and StormX.legs != 'skirt' and StormX.upskirt", Null(),

            "StormX.piercings == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.piercings == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
            "True", Null(),
            ),






        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Storm_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Storm_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Storm_Sex_Fondle_Pussy",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),

            "True", Null(),
            ),






















        )


image Storm_Sex_Feet:
    LiveComposite(

        (1120,960),
        (0,0), "images/StormSex/Storm_Sex_Legs_FJ.png",





        (0,0), ConditionSwitch(

            "StormX.hose == 'ripped_pantyhose' and (not StormX.underwear or not StormX.underwear_pulled_down)", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJHoled.png",
            "StormX.hose and StormX.hose != 'garterbelt' and StormX.hose != 'pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png",
            "StormX.underwear and StormX.underwear_pulled_down", Null(),
            "StormX.hose == 'pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png",
            "True", Null(),
            ),








        )


image Storm_Sex_Pussy:


    contains:

        ConditionSwitch(
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 2", "images/StormSex/Storm_Sex_Pussy_Fucking.png",
                "Player.sprite and Player.cock_position == 'in' and action_speed", "Storm_Sex_Heading_Pussy",
                "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'out')", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "primary_action == 'eat_pussy'", "images/StormSex/Storm_Sex_Pussy_Open.png",
                "True", "images/StormSex/Storm_Sex_Pussy_Closed.png",
                )
    contains:








        ConditionSwitch(
                "not StormX.pubes", Null(),

                "Player.sprite and Player.cock_position == 'in' and action_speed and show_feet", "images/StormSex/Storm_Sex_Pubes_Fucking_FJ.png",
                "Player.sprite and Player.cock_position == 'in' and action_speed", "images/StormSex/Storm_Sex_Pubes_Fucking.png",
                "Player.sprite and Player.cock_position == 'in' and show_feet", "images/StormSex/Storm_Sex_Pubes_Open_FJ.png",
                "Player.sprite and Player.cock_position == 'in'", "images/StormSex/Storm_Sex_Pubes_Open.png",
                "primary_action == 'eat_pussy' and show_feet", "images/StormSex/Storm_Sex_Pubes_Open_FJ.png",
                "primary_action == 'eat_pussy'", "images/StormSex/Storm_Sex_Pubes_Open.png",
                "show_feet", "images/StormSex/Storm_Sex_Pubes_Closed_FJ.png",
                "True", "images/StormSex/Storm_Sex_Pubes_Closed.png",
                )
    contains:
        ConditionSwitch(

                "'in' in StormX.spunk", "images/StormSex/Storm_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
    contains:















        ConditionSwitch(

                "Player.sprite and Player.cock_position == 'in' and action_speed >= 3", AlphaMask("Storm_Sex_Fucking_Zero_Anim3", "Storm_Sex_Fucking_Mask"),
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 2", AlphaMask("Storm_Sex_Fucking_Zero_Anim2", "Storm_Sex_Fucking_Mask"),
                "Player.sprite and Player.cock_position == 'in' and action_speed == 1", AlphaMask("Storm_Sex_Fucking_Zero_Anim1", "Storm_Sex_Heading_Mask"),
                "Player.sprite and Player.cock_position == 'in'", "Storm_Sex_Fucking_Zero_Anim0",
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "StormX.piercings == 'barbell' and Player.sprite and Player.cock_position == 'in' and action_speed", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellF.png",
                "StormX.piercings == 'ring' and Player.sprite and Player.cock_position == 'in' and action_speed", "images/StormSex/Storm_Sex_Pierce_Pussy_RingF.png",
                "StormX.piercings == 'barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_Barbell.png",
                "StormX.piercings == 'ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_Ring.png",
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "Player.sprite and Player.cock_position == 'in' and action_speed == 1", "Storm_Pussy_Spunk_Heading",
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "action_speed == 1", Null(),
                "'in' not in StormX.spunk or not Player.sprite or Player.cock_position != 'in' or not action_speed", Null(),

                "True", "images/StormSex/Storm_Sex_Spunk_Pussy_Over.png",
                )



image Storm_Sex_Lick_Pussy:
    "licking"
    zoom 0.7
    offset (535,500)

image Storm_Sex_Lick_Ass:
    "licking"
    zoom 0.7
    offset (535,550)

image Storm_Sex_Fondle_Pussy:
    "GropePussy_Storm"
    xzoom -1.5
    yzoom 1.5
    offset (-890,-300)









image Storm_Sex_Zero_Cock:

    contains:
        subpixel True

        ConditionSwitch(
                "Player.sprite", "Zero_cock_titjob" ,
                "True", Null(),
                )
        subpixel True
        anchor (0.5,1.0)
        transform_anchor True
        offset (546,1007)
        zoom 0.48

image Storm_Sex_Fucking_Mask:


    contains:
        "images/StormSex/Storm_Sex_Mask_Fucking.png"
        yoffset 3



image Storm_Sex_Static:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-140)
        block:
            ease 2 ypos -130
            pause 0.8
            ease 2 ypos -140
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-140)
        block:
            pause 0.6
            ease 1.8 ypos -125
            ease 0.5 ypos -130
            pause 0.3
            ease 1.8 ypos -140
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-140)
    contains:






        subpixel True
        ConditionSwitch(
                "Player.sprite", "Zero_cock_titjob" ,
                "True", Null(),
                )
        subpixel True
        anchor (0.5,1.0)
        transform_anchor True
        offset (506,870)
        zoom 0.48
        rotate 10
        block:
            pause 1
            ease 0.4 rotate 9
            ease 0.2 rotate 10
            repeat
    contains:

        subpixel True
        ConditionSwitch(

                "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
                "True", Null(),
                )
        pos (0,-140)
















image Storm_Sex_Fucking_Speed0:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-180)
        block:
            ease 2 ypos -140
            pause 0.8
            ease 2 ypos -180
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-180)
        block:
            pause 0.2
            ease 2 ypos -120

            ease 0.9 ypos -130
            pause 0.1
            ease 1.8 ypos -180
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-180)
        block:
            pause 0.2
            ease 2 ypos -140
            pause 0.8
            ease 2 ypos -180
            repeat



image Storm_Sex_Fucking_Zero_Anim0:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (0,40)
        block:
            pause 0.2
            easeout 1 ypos 20
            easein 0.8 ypos 10
            pause 1.4
            easeout 0.6 ypos 10
            easein 1 ypos 40
            repeat






image Storm_Sex_Fucking_Speed1:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-180)
        block:
            ease 2 ypos -130
            pause 0.8
            ease 2 ypos -180
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-180)
        block:
            pause 0.2
            ease 1.9 ypos -120
            ease 0.6 ypos -130
            pause 0.3
            ease 2 ypos -180
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-180)
        block:
            pause 0.2
            ease 2 ypos -130
            pause 0.8
            ease 2 ypos -180
            repeat



image Storm_Sex_Fucking_Zero_Anim1:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (0,40)
        block:
            pause 0.2

            ease 2 ypos -10
            pause 0.8
            ease 2 ypos 40
            repeat

image Storm_Sex_Heading_Mask:

    contains:
        "images/StormSex/Storm_Sex_Mask_Fucking.png"
        yoffset 10
        block:
            pause 0.2
            ease 2 yoffset 3
            pause 0.8
            ease 2 yoffset 10
            repeat


image Storm_Sex_Heading_Pussy:

    contains:
        "images/StormSex/Storm_Sex_Pussy_Fucking_Base.png"
    contains:
        "images/StormSex/Storm_Sex_Pussy_Fucking.png"
        anchor (0.5,0)
        transform_anchor True
        xoffset 560
        xzoom 0.7
        block:
            pause 0.2
            ease 1.2 xzoom 1
            ease 0.4 xzoom 0.9
            pause 1.2
            ease 0.2 xzoom 1
            ease 1.8 xzoom 0.7
            repeat

image Storm_Pussy_Spunk_Heading:

    contains:
        ConditionSwitch(
                "'in' in StormX.spunk and Player.sprite and Player.cock_position == 'in' and action_speed == 1", "images/StormSex/Storm_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
        anchor (0.5,0)
        transform_anchor True
        xoffset 560
        yoffset 5
        xzoom 0.7
        block:
            pause 0.2
            ease 1.2 xzoom 1
            ease 0.4 xzoom 0.9
            pause 1.2
            ease 0.2 xzoom 1
            ease 1.8 xzoom 0.7
            repeat





image Storm_Sex_Fucking_Speed2:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-130)
        block:
            ease 1 ypos 0
            pause 1
            ease 2 ypos -130
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-130)
        block:
            pause 0.1
            ease 0.9 ypos 15
            ease 0.5 ypos -5
            ease 0.3 ypos 0
            pause 0.3
            ease 2 ypos -135
            pause 0.1
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-130)
        block:
            pause 0.2
            ease 0.95 ypos 5
            ease 0.25 ypos 0
            pause 0.8
            ease 2 ypos -130
            repeat






image Storm_Sex_Fucking_Zero_Anim2:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (0,-10)
        block:
            pause 0.2
            ease 0.95 ypos -145
            ease 0.25 ypos -140
            pause 0.8
            ease 2 ypos -10
            repeat





image Storm_Sex_Fucking_Speed3:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-100)
        block:
            ease 0.5 ypos 0
            pause 0.4
            ease 0.9 ypos -100
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-100)
        block:
            pause 0.05
            ease 0.55 ypos 15
            ease 0.2 ypos -5
            ease 0.2 ypos 0
            ease 0.75 ypos -100
            pause 0.05
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-100)
        block:
            pause 0.1
            ease 0.55 ypos 15
            ease 0.15 ypos 0
            pause 0.25
            ease 0.75 ypos -100
            repeat




image Storm_Sex_Fucking_Zero_Anim3:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"
        subpixel True
        pos (0,-40)
        block:
            pause 0.1
            ease 0.55 ypos -155
            ease 0.15 ypos -140
            pause 0.25
            ease 0.75 ypos -40
            repeat








image Storm_Sex_Anus:


















    contains:

        ConditionSwitch(
                "not Player.sprite or Player.cock_position != 'anal'", Null(),
                "action_speed >= 3",  AlphaMask("Storm_Sex_Anal_Zero_Anim3", "Storm_Sex_Anal_Mask"),
                "action_speed >= 2", AlphaMask("Storm_Sex_Anal_Zero_Anim2", "Storm_Sex_Anal_Mask"),
                "action_speed ", AlphaMask("Storm_Sex_Anal_Zero_Anim1", "Storm_Sex_Anal_Mask"),
                "True", AlphaMask("Storm_Sex_Anal_Zero_Anim0", "Storm_Sex_Anal_Mask"),
                )
    contains:

        ConditionSwitch(
                "'anal' not in StormX.spunk or not Player.sprite or Player.cock_position != 'anal' or not action_speed", Null(),
                "action_speed == 1", "Storm_Sex_Anal_Spunk_Heading_Over",
                "True", "images/StormSex/Storm_Sex_Spunk_Anal_Over.png",
                )

image Storm_Sex_Anal_Spunk_Heading_Over:
    "images/StormSex/Storm_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease 0.75 xzoom 1.0
        pause 1.75
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Storm_Sex_Anal_Spunk_Heading_Under:
    "images/StormSex/Storm_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.95
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Storm_Sex_Anal_Mask:


    contains:
        "images/StormSex/Storm_Sex_Mask_Anal.png"
        yoffset 3



image Storm_Sex_Anal_Speed0:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-235)
        parallel:
            ease 1 xpos 7
            ease 1 xpos -14
            pause 0.5
            repeat
        parallel:
            ease 2 ypos -230
            pause 0.8
            ease 2 ypos -235
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-235)
        parallel:
            pause 0.1
            ease 0.9 xpos 10
            ease 0.3 xpos 7
            ease 0.9 xpos -20
            ease 0.3 xpos -14
            repeat
    contains:







        subpixel True
        "Storm_Sex_Legs"
        pos (-20,-235)
        parallel:
            ease 1 xpos 10
            ease 1 xpos -20
            pause 0.5
            repeat
        parallel:
            pause 0.2
            ease 2 ypos -230
            pause 0.8
            ease 2 ypos -235
            repeat


image Storm_Sex_Anal_Zero_Anim0:
    contains:
        subpixel True
        ConditionSwitch(
                "not Player.sprite", Null(),
                "True", "Zero_cock_titjob" ,
                )
        subpixel True
        anchor (0.5,1.0)
        transform_anchor True
        offset (545,1007)
        zoom 0.48
        rotate -1
        pos (25,95)
        parallel:
            ease 1 rotate 1
            ease 1 rotate -1
            pause 0.5
            repeat
        parallel:
            ease 1 xpos -5
            ease 1 xpos 25
            pause 0.5
            repeat
        parallel:
            pause 0.2
            ease 2 ypos 90
            pause 0.8
            ease 2 ypos 95
            repeat






image Storm_Sex_Anal_Speed1:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-230)
        block:
            ease 2 ypos -180
            pause 0.8
            ease 2 ypos -230
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-230)
        block:














            pause 0.2
            ease 2 ypos -170
            ease 0.6 ypos -180
            pause 0.2
            ease 2 ypos -230
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-230)
        block:
            pause 0.2
            ease 2 ypos -180
            pause 0.8
            ease 2 ypos -230
            repeat



image Storm_Sex_Anal_Zero_Anim1:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (5,90)
        block:
            pause 0.2

            ease 2 ypos 40
            pause 0.8
            ease 2 ypos 90
            repeat






image Storm_Sex_Anal_Speed2:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-130)
        block:
            ease 1 ypos 0
            pause 1
            ease 2 ypos -130
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-130)
        block:
            pause 0.1
            ease 0.9 ypos 15
            ease 0.5 ypos -5
            ease 0.3 ypos 0
            pause 0.3
            ease 2 ypos -135
            pause 0.1
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-130)
        block:
            pause 0.2
            ease 0.95 ypos 5
            ease 0.25 ypos 0
            pause 0.8
            ease 2 ypos -130
            repeat






image Storm_Sex_Anal_Zero_Anim2:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (5,-10)
        block:
            pause 0.2
            ease 0.95 ypos -145
            ease 0.25 ypos -140
            pause 0.8
            ease 2 ypos -10
            repeat






image Storm_Sex_Anal_Speed3:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-100)
        block:
            ease 0.5 ypos 0
            pause 0.4
            ease 0.9 ypos -100
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-100)
        block:
            pause 0.05
            ease 0.55 ypos 15
            ease 0.2 ypos -5
            ease 0.2 ypos 0
            ease 0.75 ypos -100
            pause 0.05
            repeat
    contains:


        subpixel True
        "Storm_Sex_Legs"
        pos (0,-100)
        block:
            pause 0.1
            ease 0.55 ypos 15
            ease 0.15 ypos 0
            pause 0.25
            ease 0.75 ypos -100
            repeat



image Storm_Sex_Anal_Zero_Anim3:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"
        subpixel True
        pos (5,-40)
        block:
            pause 0.1
            ease 0.55 ypos -155
            ease 0.15 ypos -140
            pause 0.25
            ease 0.75 ypos -40
            repeat









image Storm_Sex_Hotdog_Speed1:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-160)
        block:
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -160
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-160)
        block:
            pause 0.2
            ease 2 ypos -75
            ease 0.7 ypos -85
            pause 0.1
            ease 2 ypos -160
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-160)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -160
            repeat
    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"
        subpixel True
        pos (0,-140)
        block:
            pause 1.5
            ease 0.7 ypos -120
            pause 1
            ease 1 ypos -145
            ease 0.2 ypos -140
            pause 0.6
            repeat
    contains:

        subpixel True
        ConditionSwitch(

                "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
                "True", Null(),
                )
        pos (0,-160)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -160
            repeat








image Storm_Sex_Hotdog_Speed2:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-160)
        block:
            ease 1 ypos -80
            pause 0.4
            ease 1 ypos -160
            pause 0.1
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-160)
        block:
            pause 0.1
            ease 0.9 ypos -70
            ease 0.5 ypos -80
            ease 1 ypos -160
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-160)
        block:
            pause 0.1
            ease 1 ypos -80
            pause 0.4
            ease 1 ypos -160
            repeat
    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"
        subpixel True
        pos (0,-140)
        block:
            pause 0.8
            ease 0.3 ypos -120
            pause 0.5
            ease 0.5 ypos -145
            ease 0.1 ypos -140
            pause 0.3
            repeat
    contains:

        subpixel True
        ConditionSwitch(

                "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
                "True", Null(),
                )
        pos (0,-160)
        block:
            pause 0.1
            ease 1 ypos -80
            pause 0.4
            ease 1 ypos -160
            repeat











image Storm_Sex_FJ_Speed0:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-160)
        block:
            ease 2 ypos -140
            pause 0.8
            ease 2 ypos -160
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-160)
        block:
            pause 0.2
            ease 2 ypos -140

            ease 0.7 ypos -145
            pause 0.1
            ease 2 ypos -160
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"
        subpixel True
        pos (0,-140)
    contains:

        subpixel True
        ConditionSwitch(

                "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
                "True", Null(),
                )
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -200
            repeat








image Storm_Sex_FJ_Speed1:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-160)
        block:
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -160
            pause 0.2
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-160)
        block:
            pause 0.2
            ease 2 ypos -75
            ease 0.7 ypos -85
            pause 0.1
            ease 2 ypos -160
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"
        subpixel True
        pos (0,-140)
        block:
            pause 1.5
            ease 0.7 ypos -120
            pause 1
            ease 1 ypos -140
            pause 0.8
            repeat
    contains:

        subpixel True
        ConditionSwitch(

                "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
                "True", Null(),
                )
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat








image Storm_Sex_FJ_Speed2:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-160)
        block:
            ease 0.9 ypos -80
            pause 0.1
            ease 1 ypos -160
            pause 0.1
            repeat
    contains:

        subpixel True
        "Storm_Sex_Tits"
        pos (0,-160)
        block:
            pause 0.1
            ease 0.8 ypos -75
            ease 0.2 ypos -85

            ease 1 ypos -160
            repeat
    contains:

        subpixel True
        "Storm_Sex_Legs"
        pos (0,-200)
        block:
            pause 0.1
            ease 0.9 ypos -150
            pause 0.1
            ease 1 ypos -250
            repeat
    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"
        subpixel True
        pos (0,-140)
        block:
            pause 0.6
            ease 0.4 ypos -120
            pause 0.2
            ease 0.5 ypos -140
            pause 0.4
            repeat
    contains:

        subpixel True
        ConditionSwitch(

                "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot.png"),
                "True", Null(),
                )
        pos (0,-200)
        block:
            pause 0.1
            ease 0.9 ypos -150
            pause 0.1
            ease 1 ypos -250
            repeat






label Storm_Sex_Launch(Line=primary_action):
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action


    $ StormX.pose = "sex"


    $ Player.sprite = 1
    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.cock_position = "sex"
        if offhand_action in ("fondle_pussy","dildo_pussy","eat_pussy"):
            $ offhand_action = 0
    elif Line == "anal":
        $ Player.cock_position = "anal"
        if offhand_action in ("finger_ass","dildo_anal","eat_ass"):
            $ offhand_action = 0
    elif Line == "hotdog":
        if StormX.PantsNum() == 5:
            $ StormX.upskirt = 1
        $ Player.cock_position = "out"
    elif Line == "footjob":
        $ show_feet = 1
        $ Player.cock_position = "footjob"
    elif Line == "massage":
        $ Player.sprite = 0
        $ Player.cock_position = 0
    else:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        $ action_speed = 0
    $ primary_action = Line

    if StormX.pose == "doggy":
        call Storm_Doggy_Launch (Line)
        return
    if renpy.showing("Storm_SexSprite"):
        return
    $ action_speed = 0
    call Storm_Hide (1)
    show Storm_SexSprite zorder 150
    with dissolve
    return

label Storm_Sex_Reset:
    if renpy.showing("Storm_Doggy_Animation"):
        call Storm_Doggy_Reset
        return
    if not renpy.showing("Storm_SexSprite"):
        return
    $ StormX.arm_pose = 2
    hide Storm_SexSprite
    call Storm_Hide

    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return








image Storm_handjob_under:
    "images/StormSprite/handstorm2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

image Storm_handjob_over:
    "images/StormSprite/handstorm1.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

transform Storm_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease 0.5 pos (0,150) rotate -5
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5
        pause 0.1
        repeat

transform Storm_Hand_2():
    subpixel True
    pos (-15,-120)
    rotate 10
    block:
        ease 0.2 pos (-15,0) rotate 0
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10
        pause 0.1
        repeat
























transform Handcock_1J():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease 0.5 ypos 450 rotate -2
        pause 0.25
        ease 1.0 ypos 400 rotate 0
        pause 0.1
        repeat

transform Handcock_2J():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease 0.2 ypos 430 rotate -3
        ease 0.5 ypos 400 rotate 0
        pause 0.1
        repeat

image Storm_HJ_Animation:
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Storm_handjob_under"),
            "action_speed == 1", At("Storm_handjob_under", Storm_Hand_1()),
            "action_speed >= 2", At("Storm_handjob_under", Storm_Hand_2()),
            "action_speed ", Null(),
            ),
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Zero_cock_handjob"),
            "action_speed == 1", At("Zero_cock_handjob", Handcock_1J()),
            "action_speed >= 2", At("Zero_cock_handjob", Handcock_2J()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Storm_handjob_over"),
            "action_speed == 1", At("Storm_handjob_over", Storm_Hand_1()),
            "action_speed >= 2", At("Storm_handjob_over", Storm_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Storm_HJ_Launch(Line=primary_action):
    $ StormX.arm_pose = 2
    if renpy.showing("Storm_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call Storm_Hide
    if Line == "L":
        show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)
    else:
        show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)
        with dissolve

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause 0.5
    # show Storm_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:
    #
    #     offset (250,250)
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_right):
        alpha 1
        ease 0.5 zoom 1.7 offset (-150,200)
    return

label Storm_HJ_Reset:
    if not renpy.showing("Storm_HJ_Animation"):
        return
    $ action_speed = 0
    $ StormX.arm_pose = 1
    hide Storm_HJ_Animation with easeoutbottom
    call Storm_Hide
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        alpha 1
        zoom 1.7 offset (-150,200)
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause 0.5
        ease 0.5 zoom 1 offset (0,0)
        pause 0.5
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return









image Storm_BJ_Animation:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "action_speed == 0", "Storm_BJ_Anim0",
            "action_speed == 1", "Storm_BJ_Anim1",
            "action_speed == 2", "Storm_BJ_Anim2",
            "action_speed == 3", "Storm_BJ_Anim3",
            "action_speed == 4", "Storm_BJ_Anim4",
            "action_speed == 5", "Storm_BJ_Anim5",
            "action_speed == 6", "Storm_BJ_Anim6",
            "True", Null(),
            ),
        )
    zoom 0.55
    anchor (.5,.5)

image Storm_BJ_hairback:

    ConditionSwitch(
            "(StormX.hair == 'long' and StormX.wet) or StormX.hair == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Under.png",
            "StormX.hair == 'mohawk' or StormX.hair == 'wethawk' or StormX.hair == 'short'", Null(),
            "True", "images/StormBJFace/Storm_BJ_Hair_Long_Under.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Storm_BJ_HairTop:
    contains:
        ConditionSwitch(
                "(StormX.hair == 'mohawk' and StormX.wet) or StormX.hair == 'wethawk'", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png",
                "StormX.wet or StormX.hair == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png",
                "StormX.hair == 'mohawk'", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png",
                "StormX.hair == 'short'", "images/StormBJFace/Storm_BJ_Hair_Short.png",
                "True", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png",
                )
    contains:
        ConditionSwitch(

                "'hair' in StormX.spunk and (StormX.wet or StormX.hair == 'wethawk' or StormX.hair == '_wet')", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
                "'hair' in StormX.spunk and StormX.hair == 'mohawk'", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
                "'hair' in StormX.spunk", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
                "True", Null(),
                )
    zoom 1.4
    anchor (0.5, 0.5)


image Storm_BJ_Backdrop1:
    contains:

        ConditionSwitch(
                "'blanket' in StormX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),
        zoom 2
        anchor (.5,.5)
        pos (350,600)









image Storm_BJ_Head:
    LiveComposite(
        (858,928),






        (0,0), ConditionSwitch(






            "StormX.blushing > 1", "images/StormBJFace/Storm_BJ_Head_Blush2.png",

            "True", "images/StormBJFace/Storm_BJ_Head_Blush0.png"
            ),
        (0,0), ConditionSwitch(









            "action_speed and renpy.showing('Storm_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png",
                    "action_speed == 4", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png",
                    "action_speed == 6", "images/StormBJFace/Storm_BJ_Mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Storm_TJ_Animation')", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png",
            "StormX.mouth == 'normal'", "images/StormBJFace/Storm_BJ_Mouth_Smile.png",
            "StormX.mouth == 'lipbite'", "images/StormBJFace/Storm_BJ_Mouth_Lipbite.png",
            "StormX.mouth == 'sucking'", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png",
            "StormX.mouth == 'kiss'", "images/StormBJFace/Storm_BJ_Mouth_Kiss.png",
            "StormX.mouth == 'sad'", "images/StormBJFace/Storm_BJ_Mouth_Sad.png",
            "StormX.mouth == 'smile'", "images/StormBJFace/Storm_BJ_Mouth_Smile.png",
            "StormX.mouth == 'smirk'", "images/StormBJFace/Storm_BJ_Mouth_Smirk.png",
            "StormX.mouth == 'grimace'", "images/StormBJFace/Storm_BJ_Mouth_Smile.png",
            "StormX.mouth == 'surprised'", "images/StormBJFace/Storm_BJ_Mouth_Kiss.png",
            "StormX.mouth == 'tongue'", "images/StormBJFace/Storm_BJ_Mouth_Tongue.png",
            "True", "images/StormBJFace/Storm_BJ_Mouth_Smile.png",
            ),
        (428,555), ConditionSwitch(


            "not renpy.showing('Storm_BJ_Animation')", Null(),
            "action_speed == 2", "Storm_BJ_MouthHeading",
            "action_speed == 5", "Storm_BJ_MouthCumHigh",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "'mouth' not in StormX.spunk", Null(),
            "action_speed and renpy.showing('Storm_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/StormBJFace/Storm_BJ_Spunk_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 4", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 6", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
                    ),
            "StormX.mouth == 'normal'", "images/StormBJFace/Storm_BJ_Spunk_Smile.png",



            "StormX.mouth == 'smile'", "images/StormBJFace/Storm_BJ_Spunk_Smile.png",


            "StormX.mouth == 'tongue'", "images/StormBJFace/Storm_BJ_Spunk_Tongue.png",
            "StormX.mouth == 'sucking'", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
            "True", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
            ),
        (0,0), ConditionSwitch(

            "StormX.brows == 'angry'", "images/StormBJFace/Storm_BJ_Brows_Angry.png",
            "StormX.brows == 'sad'", "images/StormBJFace/Storm_BJ_Brows_Sad.png",
            "StormX.brows == 'surprised'", "images/StormBJFace/Storm_BJ_Brows_Surprised.png",
            "StormX.brows == 'confused'", "images/StormBJFace/Storm_BJ_Brows_Confused.png",
            "True", "images/StormBJFace/Storm_BJ_Brows_Normal.png",
            ),
        (0,0), "Storm BJ Blink",

        (0,0), "images/StormBJFace/Storm_BJ_Earring.png",
        (0,0), ConditionSwitch(

            "not StormX.wet", Null(),
            "True", "images/StormBJFace/Storm_BJ_Wet.png",
            ),
        (0,0), ConditionSwitch(

            "(StormX.hair == 'mohawk' and StormX.wet) or StormX.hair == 'wethawk'", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png",
            "StormX.wet or StormX.hair == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png",
            "StormX.hair == 'mohawk'", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png",
            "StormX.hair == 'short'", "images/StormBJFace/Storm_BJ_Hair_Short_Over.png",
            "True", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png",
            ),


        (0,0), ConditionSwitch(

            "'facial' in StormX.spunk", "images/StormBJFace/Storm_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'hair' in StormX.spunk and (StormX.wet or StormX.hair == 'wethawk' or StormX.hair == '_wet')", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
            "'hair' in StormX.spunk and StormX.hair == 'short'", "images/StormBJFace/Storm_BJ_Spunk_HairS.png",
            "'hair' in StormX.spunk and StormX.hair == 'mohawk'", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
            "'hair' in StormX.spunk", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Storm_Tester:
    "images/StormBJFace/Storm_BJ_tester.jpg"
    alpha 0.5
image Storm BJ Blink:

    ConditionSwitch(
            "StormX.eyes == 'normal'", "images/StormBJFace/Storm_BJ_Eyes_Normal.png",
            "StormX.eyes == 'sexy'", "images/StormBJFace/Storm_BJ_Eyes_Sexy.png",
            "StormX.eyes == 'closed'", "images/StormBJFace/Storm_BJ_Eyes_Closed.png",
            "StormX.eyes == 'surprised'", "images/StormBJFace/Storm_BJ_Eyes_Surprised.png",
            "StormX.eyes == 'side'", "images/StormBJFace/Storm_BJ_Eyes_Side.png",
            "StormX.eyes == 'stunned'", "images/StormBJFace/Storm_BJ_Eyes_Stunned.png",
            "StormX.eyes == 'down'", "images/StormBJFace/Storm_BJ_Eyes_Down.png",
            "StormX.eyes == 'manic'", "images/StormBJFace/Storm_BJ_Eyes_Surprised.png",
            "StormX.eyes == 'squint'", "images/StormBJFace/Storm_BJ_Eyes_Sexy.png",
            "True", "images/StormBJFace/Storm_BJ_Eyes_Normal.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/StormBJFace/Storm_BJ_Eyes_Closed.png"
    0.25
    repeat

image Storm_BJ_MouthHeading:

    transform_anchor True
    contains:

        "images/StormBJFace/Storm_BJ_Mouth_Heading.png"
        zoom 1.4
        anchor (0.50,0.6)
    contains:
        ConditionSwitch(
            "'mouth' in StormX.spunk", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)
    contains:
        ConditionSwitch(
            "'mouth' in StormX.spunk", "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png",
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)
    subpixel True
    zoom 0.58
    block:
        pause 0.20
        easeout 0.15 zoom 0.6
        linear 0.15 zoom 0.60
        easein 0.25 zoom 0.65
        pause 0.25

        pause 0.40
        easeout 0.40 zoom 0.58
        linear 0.10 zoom 0.66
        easein 0.30 zoom 0.45
        pause 0.30

        repeat

image Storm_BJ_MouthCumHigh:

    contains:
        "images/StormBJFace/Storm_BJ_Mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.6)
    subpixel True
    zoom 0.65
    block:
        pause 0.20
        ease 0.50 zoom 0.58
        pause 0.60
        ease 0.30 zoom 0.62
        pause 0.10
        ease 0.30 zoom 0.58
        pause 0.20
        ease 0.30 zoom 0.62
        repeat

image Storm_BJ_MouthSuckingMask:

    contains:
        "images/StormBJFace/Storm_BJ_Mouth_MaskS.png"
        zoom 1.4














image Storm_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", "Storm_BJ_MouthHeadingComposite",
            "action_speed == 5", "Storm_BJ_MouthCumHighComposite",
            "True", Null(),
            ),
        (300,462), ConditionSwitch(
            "action_speed == 2 and 'mouth' in StormX.spunk", "StormHeadingSpunk",
            "action_speed == 5 and 'mouth' in StormX.spunk", "StormCumHighSpunk",
            "True", Null(),
            ),
        )
    zoom 1.8

image Storm_BJ_MouthHeadingComposite:

    transform_anchor True
    contains:

        "images/StormBJFace/Storm_BJ_Mouth_MaskH.png"


        anchor (0.50,0.6)
    offset (30,-30)
    subpixel True
    zoom 0.58
    block:
        pause 0.20
        easeout 0.15 zoom 0.6
        linear 0.15 zoom 0.60
        easein 0.25 zoom 0.65
        pause 0.25

        pause 0.40
        easeout 0.40 zoom 0.58
        linear 0.10 zoom 0.66
        easein 0.30 zoom 0.45
        pause 0.30

        repeat

image StormHeadingSpunk:

    transform_anchor True
    contains:

        "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png"


        anchor (0.50,0.6)
    offset (30,-30)
    subpixel True
    zoom 0.58
    block:
        pause 0.20
        easeout 0.15 zoom 0.6
        linear 0.15 zoom 0.60
        easein 0.25 zoom 0.65
        pause 0.25

        pause 0.40
        easeout 0.40 zoom 0.58
        linear 0.10 zoom 0.66
        easein 0.30 zoom 0.45
        pause 0.30

        repeat


image Storm_BJ_MouthCumHighComposite:

    contains:

        "images/StormBJFace/Storm_BJ_Mouth_MaskH.png"
        anchor (0.50,0.6)
    subpixel True
    offset (30,-30)
    zoom 0.65
    block:
        pause 0.20
        ease 0.50 zoom 0.58
        pause 0.60
        ease 0.30 zoom 0.62
        pause 0.10
        ease 0.30 zoom 0.58
        pause 0.20
        ease 0.30 zoom 0.62
        repeat

image StormCumHighSpunk:

    transform_anchor True
    contains:
        "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png"
        anchor (0.50,0.6)
    offset (30,-30)
    subpixel True
    zoom 0.65
    block:
        pause 0.20
        ease 0.50 zoom 0.58
        pause 0.60
        ease 0.30 zoom 0.62
        pause 0.10
        ease 0.30 zoom 0.58
        pause 0.20
        ease 0.30 zoom 0.62
        repeat

image StormSuckingSpunk:

    contains:
        "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)


image Storm_BJ_Backdrop:

    contains:

        ConditionSwitch(
                "'blanket' in StormX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                )
        zoom 1.2
        anchor (.5,.5)
        pos (180,-400)
    contains:



















        "Storm_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
    contains:


















        "Storm_TJ_Tits"
        subpixel True
        pos (0,0)
        transform_anchor True






    zoom 1.4
    offset (225,1100)



image Storm_BJ_Anim0:

    contains:

        "Storm_BJ_hairback"
        subpixel True
        offset (350,210)
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,0)
    contains:

        "Storm_BJ_Head"
        subpixel True
        offset (350,210)
    contains:

        "Zero_cock_blowjob"
        anchor (.5,.5)
        rotate -10
        offset (650,370)


image Storm_BJ_Anim1:

    contains:

        "Storm_BJ_hairback"
        subpixel True

        offset (350,175)
        block:
            ease 2.5 offset (375,310)
            ease 2 offset (350,175)
            pause 0.5
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,-35)
        block:
            ease 2.5 offset (30,90)
            ease 2 offset (0,-35)
            pause 0.5
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True
        offset (350,175)
        block:
            ease 2.5 offset (375,310)
            ease 2 offset (350,175)
            pause 0.5
            repeat
    contains:

        "Zero_cock_blowjob"
        subpixel True
        anchor (.5,.5)
        offset (650,370)
        rotate 0
        block:
            ease 2 rotate -5
            pause 0.5
            ease 2.5 rotate 0
            repeat



image Storm_BJ_Anim2:

    contains:

        "Storm_BJ_hairback"
        subpixel True

        offset (350,190)
        block:
            ease 1 yoffset 270
            ease 1.5 yoffset 190
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,-40)
        block:
            ease 1 yoffset 15
            ease 1.5 offset (0,-40)
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True
        offset (350,190)
        block:
            ease 1 yoffset 270
            ease 1.5 yoffset 190
            repeat
    contains:

        "Zero_cock_blowjob"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_MaskHeadingComposite")
        subpixel True

        offset (-250,-460)
        block:
            ease 1 yoffset -380
            ease 1.5 yoffset -460
            repeat

















image Storm_BJ_Anim3:

    contains:

        "Storm_BJ_hairback"
        subpixel True
        offset (350,260)
        block:
            ease 1 yoffset 330
            ease 1.5 yoffset 260
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,50)
        block:
            ease 1 yoffset 100
            ease 1.5 yoffset 50
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True

        offset (350,260)
        block:
            ease 1 yoffset 330
            ease 1.5 yoffset 260
            repeat
    contains:

        "Zero_cock_blowjob"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_MouthSuckingMask")
        subpixel True
        offset (-250,-390)
        block:
            ease 1 yoffset -320
            ease 1.5 yoffset -390
            repeat
    contains:

        ConditionSwitch(

                        "'mouth' in StormX.spunk", "StormSuckingSpunk",
                        "True", Null(),
                        )
        subpixel True
        offset (350,260)
        block:
            ease 1 yoffset 330
            ease 1.5 yoffset 260
            repeat


image Storm_BJ_Anim4:

    contains:

        "Storm_BJ_hairback"
        subpixel True

        offset (350,360)
        block:
            subpixel True
            ease 1 yoffset 560
            pause 0.5
            ease 2 yoffset 360
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,100)
        block:
            subpixel True
            ease 1.2 yoffset 250
            pause 0.5
            ease 1.8 yoffset 100
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True
        offset (350,360)
        block:
            subpixel True
            ease 1 yoffset 560
            pause 0.5
            ease 2 yoffset 360
            repeat
    contains:

        "Zero_cock_blowjob"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_MouthSuckingMask")
        subpixel True
        offset (-250,-290)
        block:
            subpixel True
            ease 1 yoffset -90
            pause 0.5
            ease 2 yoffset -290
            repeat
    contains:








        ConditionSwitch(

                        "'mouth' in StormX.spunk", "StormSuckingSpunk",
                        "True", Null(),
                        )
        subpixel True
        offset (350,360)
        block:
            subpixel True
            ease 1 yoffset 560
            pause 0.5
            ease 2 yoffset 360
            repeat



image Storm_BJ_Anim5:

    contains:

        "Storm_BJ_hairback"
        subpixel True
        offset (350,200)
        block:
            ease 1 yoffset 210
            ease 1.5 yoffset 200
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,-30)
        block:
            ease 1 yoffset -20
            ease 1.5 yoffset -30
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True

        offset (350,200)
        block:
            ease 1 yoffset 210
            ease 1.5 yoffset 200
            repeat
    contains:

        "Zero_cock_blowjob"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_MaskHeadingComposite")
        subpixel True
        offset (-250,-450)
        block:
            ease 1 yoffset -440
            ease 1.5 yoffset -450
            repeat









image Storm_BJ_Anim6:

    contains:

        "Storm_BJ_hairback"
        subpixel True
        offset (350,440)
        block:
            subpixel True
            ease 1 yoffset 460
            pause 0.5
            ease 2 yoffset 440
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,190)
        block:
            subpixel True
            ease 1.2 yoffset 200
            pause 0.5
            ease 1.8 yoffset 190
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True

        offset (350,440)
        block:
            subpixel True
            ease 1 yoffset 460
            pause 0.5
            ease 2 yoffset 440
            repeat
    contains:

        "Zero_cock_blowjob"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_MouthSuckingMask")
        subpixel True
        offset (-250,-210)
        block:
            subpixel True
            ease 1 yoffset -190
            pause 0.5
            ease 2 yoffset -210
            repeat
    contains:

        ConditionSwitch(

                        "'mouth' in StormX.spunk", "StormSuckingSpunk",
                        "True", Null(),
                        )
        subpixel True
        offset (350,440)
        block:
            subpixel True
            ease 1 yoffset 460
            pause 0.5
            ease 2 yoffset 440
            repeat






label Storm_BJ_Launch(Line=primary_action):
    if renpy.showing("Storm_BJ_Animation"):
        return


    if renpy.showing("Storm_TJ_Animation"):
        hide Storm_TJ_Animation
    else:
        call Storm_Hide
        if Line == "L" or Line == "cum":
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_center):
                alpha 1
                ease 1 zoom 2.5 offset (150,80)
            with dissolve
        else:
            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_center):
                alpha 1
                zoom 2.5 offset (150,80)
            with dissolve
        hide Storm_Sprite

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    # show Storm_BJ_Animation zorder 150:
    #     pos (630,650)
    if taboo and Line == "L":
        if len(Present) >= 2:
            if Present[0] != StormX:
                "[StormX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != StormX:
                "[StormX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[StormX.name] looks around to see if anyone can see her."
        "She then bends down and puts your cock to her mouth."
    elif Line == "L":
        "[StormX.name] smoothly bends down and places your cock against her cheek."

    return

label Storm_BJ_Reset:
    if not renpy.showing("Storm_BJ_Animation"):
        return

    call Storm_Hide
    $ action_speed = 0

    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Storm_Sprite zorder StormX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause 0.2
        ease 0.3 zoom 1 offset (0,0)
    pause 1.5
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return








image Storm_TJ_Animation:

    contains:
        ConditionSwitch(

                    "not Player.sprite","Storm_TJ_0",
                    "action_speed == 1", "Storm_TJ_1",
                    "action_speed == 3", "Storm_TJ_3",
                    "action_speed == 4", "Storm_TJ_4",
                    "action_speed == 5", "Storm_TJ_5",
                    "action_speed >= 2", "Storm_TJ_2",
                    "True",       "Storm_TJ_0",
                    )
    zoom 0.8
    transform_anchor True
    anchor (.5,.5)




image Storm_TJ_hairback:

    "Storm_BJ_hairback"
    transform_anchor True
    zoom 0.7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Storm_TJ_Head:

    "Storm_BJ_Head"
    transform_anchor True
    zoom 0.7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Storm_TJ_HairTop:

    contains:
        ConditionSwitch(
                        "(StormX.hair == 'mohawk' and StormX.wet) or StormX.hair == 'wethawk'", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png",
                        "StormX.wet or StormX.hair == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png",
                        "StormX.hair == 'mohawk'", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png",
                        "StormX.hair == 'short'", "images/StormBJFace/Storm_BJ_Hair_Short_Over.png",
                        "True", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png",
                        )
        offset (83,-80)
    contains:
        ConditionSwitch(

                        "'hair' in StormX.spunk and (StormX.wet or StormX.hair == 'wethawk' or StormX.hair == '_wet')", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
                        "'hair' in StormX.spunk and StormX.hair == 'mohawk'", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
                        "'hair' in StormX.spunk", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
                        "True", Null(),
                        )
        offset (83,-80)




    transform_anchor True
    zoom 0.98
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Storm_TJ_ZeroCock:

    "Zero_cock_titjob"
    transform_anchor True
    zoom 0.6
    anchor (0.5, 0.5)
    offset (30,50)
    rotate 0

image Storm_TJ_Body:

    contains:
        ConditionSwitch(
                        "StormX.top or renpy.showing('Storm_TJ_Animation')", Null(),
                        "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra'","images/StormBJFace/Storm_TJ_Chest_Bra_Back.png",
                        "True", Null(),
                        )
    contains:
        "images/StormBJFace/Storm_TJ_Body.png"
    contains:
        ConditionSwitch(
                        "not StormX.wet",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Body_Wet.png",
                        )
    contains:

        ConditionSwitch(
                        "not StormX.accessory == 'rings' or StormX.top == '_jacket'", Null(),
                        "True", "images/StormBJFace/Storm_TJ_Arms_Ring.png",
                        )
    contains:

        ConditionSwitch(

                        "StormX.bra == 'cos_bra'","images/StormBJFace/Storm_TJ_Chest_Cos_TopD.png",
                        "StormX.bra == 'sports_bra'","images/StormBJFace/Storm_TJ_Chest_Sportsbra_Body.png",
                        "StormX.bra == 'bikini_top'","images/StormBJFace/Storm_TJ_Chest_Bikini_Body.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.top == 'white_shirt'","images/StormBJFace/Storm_titjob_over_WhiteShirt_Body.png",
                        "StormX.top == '_jacket'","images/StormBJFace/Storm_titjob_over_Jacket_Body.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "'tits' not in StormX.spunk",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Spunk_Body.png",
                        )
    contains:

        ConditionSwitch(
                        "StormX.neck == 'rings'", "images/StormBJFace/Storm_TJ_Neck_Ring.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.top", Null(),
                        "StormX.hair == 'long' and not StormX.wet", "images/StormBJFace/Storm_TJ_Hair_Long_Mid.png",
                        "True",   Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0


image Storm_TJ_Tit_Under:

    contains:

        ConditionSwitch(

                    "StormX.bra == 'cos_bra'",Null(),
                    "renpy.showing('Storm_TJ_Animation')", "images/StormBJFace/Storm_TJ_TitsUnder.png",
                    "True",  Null(),
                    )





    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Storm_TJ_Braback:

    contains:
        ConditionSwitch(

                        "StormX.top",Null(),
                        "StormX.bra == 'black_bra' or StormX.bra == 'lace_bra'","images/StormBJFace/Storm_TJ_Chest_Bra_Back.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Storm_TJ_BraStretch:

    contains:
        ConditionSwitch(

                        "StormX.bra == 'bikini_top'","images/StormBJFace/Storm_TJ_Chest_Bikini_Tent.png",
                        "StormX.bra == 'sports_bra'","images/StormBJFace/Storm_TJ_Chest_Sportsbra_Tent.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    offset (50,0)
    anchor (.1,.1)
    rotate 0


image Storm_TJ_Tits:

    contains:
        "images/StormBJFace/Storm_TJ_Tits.png"
    contains:

        ConditionSwitch(
                        "StormX.piercings == 'barbell'","images/StormBJFace/Storm_TJ_Pierce_Barbell.png",
                        "StormX.top == 'white_shirt' and not StormX.top_pulled_up",Null(),
                        "StormX.bra and not StormX.top_pulled_up",Null(),
                        "StormX.piercings == 'ring'","images/StormBJFace/Storm_TJ_Pierce_Ring.png",
                        "True", Null(),
                        )
    contains:
        ConditionSwitch(
                        "not StormX.wet",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Tits_Wet.png",
                        )
    contains:
        ConditionSwitch(
                        "'tits' not in StormX.spunk",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Spunk_Tits.png",
                        )
    contains:

        ConditionSwitch(
                        "StormX.top == '_jacket'","images/StormBJFace/Storm_titjob_over_Jacket_Top.png",

                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.bra == 'black_bra' and StormX.top_pulled_up and StormX.top","images/StormBJFace/Storm_TJ_Chest_Bra_TopUS.png",
                        "StormX.bra == 'black_bra' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_Bra_TopU.png",
                        "StormX.bra == 'lace_bra' and StormX.top_pulled_up and StormX.top","images/StormBJFace/Storm_TJ_Chest_Bra_TopUS.png",
                        "StormX.bra == 'lace_bra' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_Bra_TopU.png",
                        "StormX.bra == 'sports_bra' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_SportsBra_TopU.png",
                        "StormX.bra == 'bikini_top' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_Bikini_TopU.png",

                        "StormX.bra == 'tube_top' and not StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_TubeD.png",
                        "StormX.bra == 'black_bra' and StormX.top","images/StormBJFace/Storm_TJ_Chest_Bra_TopDS.png",
                        "StormX.bra == 'black_bra'","images/StormBJFace/Storm_TJ_Chest_Bra_TopD.png",
                        "StormX.bra == 'lace_bra' and StormX.top","images/StormBJFace/Storm_TJ_Chest_Lacebra_TopDS.png",
                        "StormX.bra == 'lace_bra'","images/StormBJFace/Storm_TJ_Chest_Lacebra_TopD.png",
                        "StormX.bra == 'sports_bra'","images/StormBJFace/Storm_TJ_Chest_Sportsbra_TopD.png",
                        "StormX.bra == 'bikini_top'","images/StormBJFace/Storm_TJ_Chest_Bikini_TopD.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.top == 'white_shirt' and StormX.top_pulled_up","images/StormBJFace/Storm_titjob_over_WhiteShirt_TopU.png",
                        "StormX.top == 'white_shirt'","images/StormBJFace/Storm_titjob_over_WhiteShirt_TopD.png",

                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not StormX.accessory == 'rings' or StormX.top == '_jacket'", Null(),
                        "True", "images/StormBJFace/Storm_TJ_Wrists_Ring.png",
                        )
    contains:

        ConditionSwitch(
                        "StormX.top_pulled_up", Null(),
                        "(not StormX.top) and (not StormX.bra)", Null(),
                        "StormX.piercings == 'ring' and StormX.top == 'white_shirt'","images/StormBJFace/Storm_TJ_Pierce_Ring_Shirt.png",
                        "StormX.piercings == 'barbell' and StormX.top == 'white_shirt'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Shirt.png",
                        "StormX.bra == 'cos_bra'",Null(),
                        "StormX.piercings == 'ring' and StormX.bra == 'lace_bra'","images/StormBJFace/Storm_TJ_Pierce_Ring_Lace.png",
                        "StormX.piercings == 'barbell' and StormX.bra == 'lace_bra'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Lace.png",
                        "StormX.piercings == 'ring' and StormX.bra == 'tube_top'","images/StormBJFace/Storm_TJ_Pierce_Ring_Tube.png",
                        "StormX.piercings == 'barbell' and StormX.bra == 'tube_top'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Tube.png",
                        "StormX.piercings == 'ring' and StormX.bra","images/StormBJFace/Storm_TJ_Pierce_Ring_Bra.png",
                        "StormX.piercings == 'barbell' and StormX.bra","images/StormBJFace/Storm_TJ_Pierce_Barbell_Bra.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not StormX.accessory == 'rings' or not StormX.piercings == 'ring'", Null(),
                        "StormX.top == 'white_shirt' and not StormX.top_pulled_up", Null(),
                        "StormX.bra and StormX.bra != 'cos_bra' and not StormX.top_pulled_up",Null(),
                        "True","images/StormBJFace/Storm_TJ_Pierce_Ring.png",








                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0





image Storm_TJ_0:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
    contains:

        "Storm_TJ_hairback"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
        parallel:
            pause 0.1
            ease 2 rotate -5
            pause 0.1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
        parallel:
            pause 0.1
            ease 2 rotate -5
            pause 0.1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos -0
            pause 0.1
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,0)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 rotate -3
            pause 0.1
            ease 2 rotate -5
            pause 0.1
            repeat
    contains:
        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-70,-210)
        transform_anchor True
        xzoom 0.75
        yzoom 0.85
        parallel:
            ease 2 yzoom 0.5
            pause 0.1
            ease 2 yzoom 0.85
            pause 0.1
            repeat
        parallel:
            ease 2 pos (-60,-230)
            pause 0.1
            ease 2 pos (-70,-210)
            pause 0.1
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
    contains:

        "Storm_TJ_HairTop"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
        parallel:
            pause 0.1
            ease 2 rotate -5
            pause 0.1
            ease 2 rotate 0
            repeat





image Storm_TJ_1:

    contains:

        "Storm_TJ_Braback"
        subpixel True










        pos (0,50)
        transform_anchor True
        block:
            pause 0.1
            ease 1.9 ypos -60
            pause 0.4
            ease 1.8 ypos 60
            ease 0.5 ypos 50
            repeat
    contains:


        "Storm_TJ_hairback"
        subpixel True
        pos (0,60)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos -40
            pause 0.2
            ease 2 ypos 60
            pause 0.5
            repeat
        parallel:
            ease 2 rotate 0
            pause 0.2
            ease 2 rotate -5
            pause 0.5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,60)
        transform_anchor True
        parallel:
            ease 2 ypos -40
            pause 0.2
            ease 2 ypos 60
            pause 0.5
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,60)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos -40
            pause 0.2
            ease 2 ypos 60
            pause 0.5
            repeat
        parallel:
            ease 2 rotate 0
            pause 0.2
            ease 2 rotate -5
            pause 0.5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,60)
        transform_anchor True
        block:
            pause 0.1
            ease 1.9 ypos -60
            pause 0.4
            ease 1.8 ypos 60
            ease 0.5 ypos 50
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,25)
        transform_anchor True
        rotate -6
        parallel:
            ease 2 ypos 0
            pause 0.4
            ease 1.8 ypos 25
            pause 0.5
            repeat
    contains:






        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-100,-150)
        transform_anchor True
        xzoom 0.9
        yzoom 1.3
        parallel:
            pause 0.1
            ease 1.6 yzoom 0.3
            pause 0.9
            ease 1.6 yzoom 1.5
            ease 0.5 yzoom 1.3
            repeat
        parallel:
            pause 0.1
            ease 1.9 xzoom 0.6
            pause 0.4
            ease 1.8 xzoom 0.9
            pause 0.5

            repeat
        parallel:
            pause 0.1
            ease 1.9 pos (-50,-260)
            pause 0.4
            ease 1.8 pos (-100,-140)
            ease 0.5 pos (-100,-150)
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,50)
        transform_anchor True
        block:
            pause 0.1
            ease 1.9 ypos -60
            pause 0.4
            ease 1.8 ypos 60
            ease 0.5 ypos 50
            repeat
    contains:

        "Storm_TJ_HairTop"
        subpixel True
        pos (0,60)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos -40
            pause 0.2
            ease 2 ypos 60
            pause 0.5
            repeat
        parallel:
            ease 2 rotate 0
            pause 0.2
            ease 2 rotate -5
            pause 0.5
            repeat







image Storm_TJ_2:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 0.3 ypos 40
            ease 0.7 ypos -40
            pause 0.2
            ease 0.4 ypos 80
            repeat
    contains:

        "Storm_TJ_hairback"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause 0.1
            ease 0.5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause 0.1
            ease 0.5 rotate -5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,80)
        transform_anchor True
        parallel:
            ease 1 ypos -20
            pause 0.1
            ease 0.5 ypos 80
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause 0.1
            ease 0.5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause 0.1
            ease 0.5 rotate -5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 0.3 ypos 40
            ease 0.7 ypos -40
            pause 0.2
            ease 0.4 ypos 80
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,30)
        transform_anchor True
        rotate -4
        parallel:
            ease 1 ypos 0
            pause 0.2
            ease 0.4 ypos 30
            repeat
        parallel:
            ease 1 rotate -2
            pause 0.1
            ease 0.5 rotate -4
            repeat
    contains:
        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-100,-120)
        transform_anchor True
        yzoom 1.7
        xzoom 1
        parallel:
            ease 0.3 yzoom 1.3
            ease 0.7 yzoom 0.3
            pause 0.2
            ease 0.4 yzoom 1.7
            repeat
        parallel:
            ease 0.3 pos (-100,-160)
            ease 0.7 pos (-80,-240)
            pause 0.2
            ease 0.4 pos (-100,-120)
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 0.3 ypos 40
            ease 0.7 ypos -40
            pause 0.2
            ease 0.4 ypos 80
            repeat
    contains:


        "Storm_TJ_HairTop"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause 0.1
            ease 0.5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause 0.1
            ease 0.5 rotate -5
            repeat




image Storm_TJ_3:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,110)
        transform_anchor True
        block:
            ease 0.3 ypos 100
            ease 0.7 ypos 60
            pause 0.2
            ease 0.4 ypos 110
            repeat
    contains:

        "Storm_TJ_hairback"
        subpixel True
        pos (0,140)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos 70
            pause 0.1
            ease 0.5 ypos 140
            repeat
        parallel:
            ease 1 rotate 0
            pause 0.1
            ease 0.5 rotate -5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,130)
        transform_anchor True
        parallel:
            ease 1 ypos 100
            pause 0.1
            ease 0.5 ypos 130
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,140)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos 70
            pause 0.1
            ease 0.5 ypos 140
            repeat
        parallel:
            ease 1 rotate 0
            pause 0.1
            ease 0.5 rotate -5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,110)
        transform_anchor True
        block:
            ease 0.3 ypos 100
            ease 0.7 ypos 60
            pause 0.2
            ease 0.4 ypos 110
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,30)
        transform_anchor True
        rotate -4
        parallel:
            ease 1 ypos 0
            pause 0.2
            ease 0.4 ypos 30
            repeat
        parallel:
            ease 1 rotate -2
            pause 0.1
            ease 0.5 rotate -4
            repeat
    contains:
        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-100,-105)
        transform_anchor True
        yzoom 2
        xzoom 1
        parallel:
            ease 0.3 yzoom 1.95
            ease 0.7 yzoom 1.7
            pause 0.2
            ease 0.4 yzoom 2
            repeat
        parallel:
            ease 0.3 pos (-100,-115)
            ease 0.7 pos (-90,-155)
            pause 0.2
            ease 0.4 pos (-100,-105)
            repeat
    contains:

        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,110)
        transform_anchor True
        block:
            ease 0.3 ypos 100
            ease 0.7 ypos 60
            pause 0.2
            ease 0.4 ypos 110
            repeat
    contains:


        "Storm_TJ_HairTop"
        subpixel True
        pos (0,140)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos 70
            pause 0.1
            ease 0.5 ypos 140
            repeat
        parallel:
            ease 1 rotate 0
            pause 0.1
            ease 0.5 rotate -5
            repeat






image Storm_TJ_4:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause 0.2
            ease 1.9 ypos -30
            pause 0.2
            ease 1.9 ypos 5
            repeat
    contains:

        "Storm_TJ_hairback"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
        parallel:
            pause 0.1
            ease 2 rotate -5
            pause 0.1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
        parallel:
            pause 0.1
            ease 2 rotate -5
            pause 0.1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause 0.2
            ease 1.9 ypos -30
            pause 0.2
            ease 1.9 ypos 5
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,20)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause 0.1
            ease 2 ypos 20
            pause 0.1
            repeat
    contains:
        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-70,-210)
        transform_anchor True
        xzoom 0.75
        yzoom 0.5
        parallel:
            pause 0.2
            ease 1.9 pos (-65,-230)
            pause 0.2
            ease 1.9 pos (-75,-210)
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause 0.2
            ease 1.9 ypos -30
            pause 0.2
            ease 1.9 ypos 5
            repeat
    contains:

        "Storm_TJ_HairTop"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause 0.1
            ease 2 ypos 0
            pause 0.1
            repeat
        parallel:
            pause 0.1
            ease 2 rotate -5
            pause 0.1
            ease 2 rotate 0
            repeat




image Storm_TJ_5:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause 0.1
            ease 2 ypos 100
            pause 0.2
            ease 2 ypos 110
            pause 0.4
            repeat
    contains:

        "Storm_TJ_hairback"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause 0.2
            ease 2 ypos 130
            pause 0.5
            repeat
        parallel:
            ease 2 rotate -5
            pause 0.5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,140)
        transform_anchor True
        parallel:
            ease 2 ypos 130
            pause 0.2
            ease 2 ypos 140
            pause 0.5
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause 0.2
            ease 2 ypos 130
            pause 0.5
            repeat
        parallel:
            ease 2 rotate -5
            pause 0.5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause 0.1
            ease 2 ypos 100
            pause 0.2
            ease 2 ypos 110
            pause 0.4
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,25)
        transform_anchor True
        rotate -5
    contains:
        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-100,-105)
        transform_anchor True
        xzoom 1
        yzoom 2
        parallel:
            pause 0.1
            ease 2 yzoom 1.8
            pause 0.2
            ease 2 yzoom 2
            pause 0.4
            repeat
        parallel:
            pause 0.1
            ease 2 pos (-100,-115)
            pause 0.2
            ease 2 pos (-100,-105)
            pause 0.4
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause 0.1
            ease 2 ypos 100
            pause 0.2
            ease 2 ypos 110
            pause 0.4
            repeat
    contains:

        "Storm_TJ_HairTop"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause 0.2
            ease 2 ypos 130
            pause 0.5
            repeat
        parallel:
            ease 2 rotate -5
            pause 0.5
            repeat





label Storm_TJ_Launch(Line=primary_action):
    if renpy.showing("Storm_TJ_Animation"):
        return
























    show blackscreen onlayer black with dissolve

    if renpy.showing("Storm_BJ_Animation"):
        hide Storm_BJ_Animation
    else:
        call Storm_Hide
        show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
            alpha 1
            ease 1 zoom 2.3 xpos 750 yoffset -100
        show Storm_Sprite zorder StormX.sprite_layer:
            alpha 0




    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    # show Storm_TJ_Animation zorder 150:
    #     pos (1000,1050)
    $ Player.sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Storm_TJ_Reset:

    if not renpy.showing("Storm_TJ_Animation"):
        return

    call Storm_Hide
    $ Player.sprite = 0

    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        zoom 2.3 xpos 750 yoffset -100
    show Storm_Sprite zorder StormX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause 0.5
        ease 0.5 zoom 1 xpos StormX.sprite_location yoffset 0
    "[StormX.name] pulls back"
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos StormX.sprite_location
    return








label Storm_Kissing_Launch(T=primary_action, Set=1):
    call Storm_Hide
    $ primary_action = T
    $ StormX.pose = "kiss" if Set else StormX.pose
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location)
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Storm_Kissing_Smooch:
    $ StormX.change_face("_kiss")
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos StormX.sprite_location zoom 1
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        zoom 1
    $ StormX.change_face("_sexy")
    return

label Storm_Breasts_Launch(T=primary_action, Set=1):
    call Storm_Hide
    $ primary_action = T
    $ StormX.pose = "breasts" if Set else StormX.pose
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Storm_Middle_Launch(T=primary_action, Set=1):
    call Storm_Hide
    $ primary_action = T
    $ StormX.pose = "mid" if Set else StormX.pose
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Storm_Pussy_Launch(T=primary_action, Set=1):
    call Storm_Hide
    $ primary_action = T
    $ StormX.pose = "pussy" if Set else StormX.pose
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Storm_Pos_Reset(T=0, Set=0):
    if StormX.location != bg_current:
        return
    call Storm_Hide
    show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        ease 0.5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Storm_Sprite zorder StormX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (StormX.sprite_location,50)
    $ StormX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Storm_Hide(Sprite=0):

    hide Storm_SexSprite
    hide Storm_Doggy_Animation
    hide Storm_HJ_Animation
    hide Storm_BJ_Animation
    hide Storm_TJ_Animation
    if Sprite:
        hide Storm_Sprite
    return



image Storm_At_Desk:
    contains:
        subpixel True
        "Storm_Sprite"
        zoom 0.29
        pos (450,190)

image Storm_At_Podium:
    contains:
        subpixel True
        "Storm_Sprite"
        zoom 0.29
        pos (670,180)

image Storm_Behind_Podium:
    contains:
        subpixel True
        "Storm_Sprite"
        zoom 0.29
        pos (640,180)
        block:
            subpixel True
            ease 0.5 ypos 183
            ease 0.5 ypos 180
            pause 0.5
            repeat


image GropeRightBreast_Storm:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (95,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat

image GropeLeftBreast_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (220,350)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image LickRightBreast_Storm:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (80,335)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -40 pos (55,310)
            pause 0.5
            ease 1.5 rotate 30 pos (80,335)
            repeat


image LickLeftBreast_Storm:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (205,350)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -40 pos (185,330)
            pause 0.5
            ease 1.5 rotate 30 pos (205,350)
            repeat

image GropeThigh_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (145,630)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause 0.5
            ease 1 rotate 110 pos (145,700)
            ease 1 rotate 100 pos (145,630)
            repeat

image GropePussy_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (145,560)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease 0.5 rotate 190 pos (145,545)
                ease 0.75 rotate 170 pos (145,560)
            choice:
                ease 0.5 rotate 190 pos (145,545)
                pause 0.25
                ease 1 rotate 170 pos (145,560)
            repeat

image FingerPussy_Storm:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (165,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (175,615)
                pause 0.5
                ease 1 rotate 50 pos (165,640)
            choice:
                ease 0.5 rotate 40 pos (175,615)
                pause 0.5
                ease 1.75 rotate 50 pos (165,640)
            choice:
                ease 2 rotate 40 pos (175,615)
                pause 0.5
                ease 1 rotate 50 pos (165,640)
            choice:
                ease 0.25 rotate 40 pos (175,615)
                ease 0.25 rotate 50 pos (165,640)
                ease 0.25 rotate 40 pos (175,615)
                ease 0.25 rotate 50 pos (165,640)
            repeat

image Lickpussy_Storm:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (175,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout 0.5 rotate -50 pos (165,575)
            linear 0.5 rotate -60 pos (155,585)
            easein 1 rotate 10 pos (175,595)
            repeat

image VibratorRightBreast_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (75,320)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 0.9 rotate 35 ypos 310
            pause 0.25
            ease 0.7 rotate 55 ypos 320
            pause 0.25
            repeat

image VibratorLeftBreast_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (200,350)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1.1 rotate 35 ypos 340
            pause 0.25
            ease 0.9 rotate 55 ypos 350
            pause 0.25
            repeat

image VibratorPussy_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (170,580)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 160
            pause 0.25
            ease 1 rotate 70 xpos 170
            pause 0.25
            repeat

image VibratorAnal_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (195,570)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 190
            pause 0.25
            ease 1 rotate 10 xpos 200
            pause 0.25
            repeat

image VibratorPussyInsert_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Storm:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeBothBreast_Storm:
    contains:
        "GirlGropeLeftBreast_Storm"
    contains:
        "GirlGropeRightBreast_Storm"

image GirlGropeLeftBreast_Storm:
    contains:
        subpixel True
        "images/UI_GirlHandS.png"
        zoom 0.6
        pos (220,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 pos (220,350)
            ease 1 rotate -10 pos (220,340)
            repeat

image GirlGropeRightBreast_Storm:
    contains:
        subpixel True
        "images/UI_GirlHandS.png"
        yzoom 0.6
        xzoom -0.6
        pos (70,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -40 pos (70,350)
            ease 1 rotate -10 pos (70,340)
            repeat

image GirlGropeThigh_Storm:
    contains:
        subpixel True
        "images/UI_GirlHandS.png"
        zoom 0.6
        anchor (0.5,0.5)
        pos (0,0)
        alpha 0.5
        rotate 100
        parallel:
            pause 0.5
            ease 1 ypos 780
            ease 1 ypos 730
            repeat
        parallel:
            pause 0.5
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            ease 0.5 xpos 213
            ease 0.5 xpos 210
            repeat









image GirlGropePussy_StormSelf:
    "images/UI_GirlHandS.png"
    offset (-40,-20)
    anchor (0.5,0.5)
    rotate 320

transform GirlGropeRightBreast_Storm():
    subpixel True
    yzoom 0.6
    xzoom -0.6
    offset (-30,240)
    anchor (0.5,0.5)
    alpha 0.5
    rotate -10
    block:
        ease 1 rotate -40 yoffset 250
        ease 1 rotate -10 yoffset 240
        repeat

transform GirlGropeLeftBreast_Storm():
    subpixel True
    zoom 0.6
    offset (120,240)
    anchor (0.5,0.5)
    alpha 0.5
    rotate -10
    block:
        ease 1 rotate 10 yoffset 250
        ease 1 rotate -10 yoffset 240
        repeat

transform GirlGropePussy_Storm1():
    subpixel True
    zoom 0.6
    offset (60,470)
    anchor (0.5,0.5)
    alpha 0.5
    rotate 200
    block:
        choice:
            ease 0.75 rotate 210 yoffset 465
            ease 0.5 rotate 195
            ease 0.75 rotate 210
            ease 0.5 rotate 195
        choice:
            ease 0.5 rotate 210 yoffset 465
            ease 1 rotate 195
            pause 0.25
            ease 0.5 rotate 210
            ease 1 rotate 195
            pause 0.25
        choice:
            ease 0.5 rotate 205 yoffset 465
            ease 0.75 rotate 200 yoffset 470
            ease 0.5 rotate 205 yoffset 465
            ease 0.75 rotate 200 yoffset 470
        choice:
            ease 0.3 rotate 205 yoffset 465
            ease 0.3 rotate 200 yoffset 475
            ease 0.3 rotate 205 yoffset 465
            ease 0.3 rotate 200 yoffset 475
        repeat

image GirlGropePussy_Storm:
    contains:
        subpixel True
        "UI_PartnerHand"
        zoom 0.6
        pos (150,550)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (150,545)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (150,545)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 pos (150,545)
                ease 0.75 rotate 200 pos (150,550)
                ease 0.5 rotate 205 pos (150,545)
                ease 0.75 rotate 200 pos (150,550)
            choice:
                ease 0.3 rotate 205 pos (150,545)
                ease 0.3 rotate 200 pos (150,555)
                ease 0.3 rotate 205 pos (150,545)
                ease 0.3 rotate 200 pos (150,555)
            repeat

image GirlFingerPussy_Storm:
    contains:
        subpixel True
        "images/UI_GirlFingerS.png"
        zoom 0.6
        pos (250,550)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (250,555)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (250,555)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 ypos 565
                ease 0.75 rotate 200 ypos 570
                ease 0.5 rotate 205 ypos 565
                ease 0.75 rotate 200 ypos 570
            choice:
                ease 0.3 rotate 205 ypos 565
                ease 0.3 rotate 200 ypos 575
                ease 0.3 rotate 205 ypos 565
                ease 0.3 rotate 200 ypos 575
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
