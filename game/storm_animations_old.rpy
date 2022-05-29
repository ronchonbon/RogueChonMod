

image Storm_sprite standing:
    LiveComposite(
        (450,950),
        (53,-45), "Storm_sprite standing_HairBack",
        (0,0), ConditionSwitch(

            "StormX.outfit['bottom'] == '_skirt'", "images/StormSprite/Storm_Sprite_Legs_SkirtB.png",
            "StormX.upskirt", ConditionSwitch(

                        "StormX.outfit['bottom'] == '_pants'", "images/StormSprite/Storm_Sprite_Legs_Pants_UpB.png",
                        "StormX.outfit['bottom'] == '_yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPants_UpB.png",
                        "True", Null(),
                        ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['top'] == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket_Under.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "not StormX.outfit['underwear']", Null(),
            "StormX.underwear_pulled_down", ConditionSwitch(

                    "not StormX.outfit['bottom'] or StormX.upskirt or StormX.outfit['bottom'] == '_skirt'", ConditionSwitch(

                            "StormX.outfit['underwear'] == '_cosplay_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos_DB.png",
                            "StormX.outfit['underwear'] == '_white_panties'", "images/StormSprite/Storm_Sprite_Panties_White_DB.png",


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
            "StormX.outfit['bottom'] and StormX.outfit['bottom'] != '_skirt' and not StormX.upskirt", Null(),
            "StormX.outfit['underwear'] and not StormX.underwear_pulled_down and StormX.grool <= 1", Null(),
            "StormX.grool == 1", ConditionSwitch(
                    "StormX.outfit['underwear'] and StormX.underwear_pulled_down", AlphaMask("Wet_Drip","Storm_Drip_MaskP"),
                    "StormX.outfit['bottom'] and StormX.outfit['bottom'] != '_skirt'", AlphaMask("Wet_Drip","Storm_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Storm_Drip_Mask"),
                    ),
            "True", ConditionSwitch(
                    "StormX.outfit['underwear'] and StormX.underwear_pulled_down", AlphaMask("Wet_Drip2","Storm_Drip_MaskP"),
                    "StormX.outfit['bottom'] and StormX.outfit['bottom'] != '_skirt'", AlphaMask("Wet_Drip2","Storm_Drip_MaskP"),
                    "StormX.outfit['underwear']", AlphaMask("Wet_Drip","Storm_Drip_Mask"),
                    "True", AlphaMask("Wet_Drip2","Storm_Drip_Mask"),
                    ),
            ),
        (165,560), ConditionSwitch(

            "not StormX.spunk['pussy'] and not StormX.spunk['anus']", Null(),
            "StormX.outfit['bottom'] and StormX.outfit['bottom'] != '_skirt' and not StormX.upskirt", Null(),
            "StormX.outfit['underwear'] and not StormX.underwear_pulled_down and StormX.grool <= 1", Null(),
            "True", ConditionSwitch(
                    "StormX.outfit['underwear'] and StormX.underwear_pulled_down", AlphaMask("Spunk_Drip2","Storm_Drip_MaskP"),

                    "StormX.outfit['underwear']", AlphaMask("Spunk_Drip","Storm_Drip_Mask"),
                    "True", AlphaMask("Spunk_Drip2","Storm_Drip_Mask"),
                    ),
            ),

        (0,0), ConditionSwitch(

            "StormX.pubes", "images/StormSprite/Storm_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['piercings']", Null(),
            "StormX.outfit['underwear'] and not StormX.underwear_pulled_down", Null(),
            "StormX.outfit['bottom'] != '_skirt' and StormX.outfit['bottom'] and not StormX.upskirt", Null(),
            "StormX.outfit['piercings'] == '_barbell'", "images/StormSprite/Storm_Sprite_Barbell_Pussy.png",
            "StormX.outfit['piercings'] == '_ring'", "images/StormSprite/Storm_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['loincloth'] == '_rings' or StormX.outfit['top'] == '_jacket'", Null(),
            "StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_ArmRings1.png",
            "True", "images/StormSprite/Storm_Sprite_ArmRings2.png",
            ),
        (0,0), ConditionSwitch(

            "StormX.top_pulled_up", "images/StormSprite/Storm_Sprite_Tits.png",
            "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Tits_Up.png",
            "True", "images/StormSprite/Storm_Sprite_Tits.png",
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['piercings']", Null(),

            "StormX.top_pulled_up", Null(),

            "StormX.outfit['piercings'] == '_barbell'", ConditionSwitch(

                    "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsU.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsL.png",
                    ),

            "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Ring_TitsUCU.png",
            "StormX.outfit['top'] or StormX.outfit['bra']", "images/StormSprite/Storm_Sprite_Ring_TitsLCU.png",
            "True", "images/StormSprite/Storm_Sprite_Ring_TitsL.png",
            ),


        (0,0), ConditionSwitch(


            "StormX.outfit['neck'] == '_gold_necklace'", "images/StormSprite/Storm_Sprite_Necklace1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.top_pulled_up", ConditionSwitch(

                    "StormX.outfit['bra'] == '_cosplay_bra'", "images/StormSprite/Storm_Sprite_Chest_Cos_Up.png",
                    "StormX.outfit['bra'] == '_black_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_Up.png",
                    "StormX.outfit['bra'] == '_lace_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_Up.png",
                    "StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Chest_Sportsbra_Up.png",
                    "StormX.outfit['bra'] == '_bikini_top'", "images/StormSprite/Storm_Sprite_Chest_Bikini_Up.png",
                    "StormX.outfit['bra'] == '_tube_top'", "images/StormSprite/Storm_Sprite_Chest_Tube_Up.png",
                    "True", Null(),
                    ),
            "StormX.outfit['bra'] == '_cosplay_bra'", "images/StormSprite/Storm_Sprite_Chest_Cos.png",
            "StormX.outfit['bra'] == '_black_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra.png",
            "StormX.outfit['bra'] == '_lace_bra'", "images/StormSprite/Storm_Sprite_Chest_LaceBra.png",
            "StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Chest_Sportsbra.png",
            "StormX.outfit['bra'] == '_bikini_top'", "images/StormSprite/Storm_Sprite_Chest_Bikini.png",
            "StormX.outfit['bra'] == '_tube_top'", "images/StormSprite/Storm_Sprite_Chest_Tube.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not StormX.outfit['piercings'] or (not StormX.outfit['top'] and not StormX.outfit['bra'] and not StormX.top_pulled_up)", Null(),
            "StormX.top_pulled_up", Null(),
            "StormX.outfit['piercings'] == '_barbell'", ConditionSwitch(

                    "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsUC.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsLC.png",
                    ),
            "StormX.outfit['piercings'] == '_ring' and (StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra')", "images/StormSprite/Storm_Sprite_Ring_TitsUC.png",
            "StormX.outfit['piercings'] == '_ring'", "images/StormSprite/Storm_Sprite_Ring_TitsLC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "StormX.outfit['hose'] == '_stockings'", "images/StormSprite/Storm_Sprite_Hose_Stockings.png",
            "StormX.outfit['hose'] == '_stockings_and_garterbelt'", "images/StormSprite/Storm_Sprite_Hose_StockingsandGarter.png",
            "StormX.outfit['hose'] == '_garterbelt'", "images/StormSprite/Storm_Sprite_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['loincloth'] == '_rings' or StormX.outfit['bottom'] == '_pants' or StormX.outfit['bottom'] == '_yoga_pants'", Null(),
            "True", "images/StormSprite/Storm_Sprite_LegRings.png",
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['underwear']", Null(),
            "StormX.underwear_pulled_down", ConditionSwitch(

                    "not StormX.outfit['bottom'] or StormX.upskirt or StormX.outfit['bottom'] == '_skirt'", ConditionSwitch(

                            "StormX.outfit['underwear'] == '_cosplay_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos_D.png",
                            "StormX.outfit['underwear'] == '_white_panties'", "images/StormSprite/Storm_Sprite_Panties_White_D.png",
                            "StormX.outfit['underwear'] == '_lace_panties'", "images/StormSprite/Storm_Sprite_Panties_Lace_D.png",
                            "StormX.outfit['underwear'] == '_bikini_bottoms'", "images/StormSprite/Storm_Sprite_Panties_Bikini_D.png",
                            "True", "images/StormSprite/Storm_Sprite_Panties_Black_D.png",
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "StormX.grool", ConditionSwitch(

                        "StormX.outfit['underwear'] == '_cosplay_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos.png",
                        "StormX.outfit['underwear'] == '_white_panties'", "images/StormSprite/Storm_Sprite_Panties_WhiteW.png",
                        "StormX.outfit['underwear'] == '_lace_panties'", "images/StormSprite/Storm_Sprite_Panties_Lace.png",
                        "StormX.outfit['underwear'] == '_bikini_bottoms' and (StormX.outfit['bra'] != '_bikini_top' or StormX.top_pulled_up)", "images/StormSprite/Storm_Sprite_Panties_BikiniL.png",
                        "StormX.outfit['underwear'] == '_bikini_bottoms'", "images/StormSprite/Storm_Sprite_Panties_Bikini.png",
                        "True", "images/StormSprite/Storm_Sprite_Panties_BlackW.png",
                        ),
                    "True", ConditionSwitch(

                        "StormX.outfit['underwear'] == '_cosplay_panties'", "images/StormSprite/Storm_Sprite_Panties_Cos.png",
                        "StormX.outfit['underwear'] == '_white_panties'", "images/StormSprite/Storm_Sprite_Panties_White.png",
                        "StormX.outfit['underwear'] == '_lace_panties'", "images/StormSprite/Storm_Sprite_Panties_Lace.png",
                        "StormX.outfit['underwear'] == '_bikini_bottoms' and (StormX.outfit['bra'] != '_bikini_top' or StormX.top_pulled_up)", "images/StormSprite/Storm_Sprite_Panties_BikiniL.png",
                        "StormX.outfit['underwear'] == '_bikini_bottoms'", "images/StormSprite/Storm_Sprite_Panties_Bikini.png",
                        "True", "images/StormSprite/Storm_Sprite_Panties_Black.png",
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['hose'] == '_pantyhose' and (not StormX.underwear_pulled_down or not StormX.outfit['underwear'])", "images/StormSprite/Storm_Sprite_Hose_Pantyhose.png",
            "StormX.outfit['hose'] == '_ripped_pantyhose' and (not StormX.underwear_pulled_down or not StormX.outfit['underwear'])", "images/StormSprite/Storm_Sprite_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['bottom']", Null(),
            "StormX.upskirt", ConditionSwitch(

                        "StormX.outfit['bottom'] == '_pants'", "images/StormSprite/Storm_Sprite_Legs_Pants_Up.png",
                        "StormX.outfit['bottom'] == '_yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPants_Up.png",
                        "StormX.outfit['bottom'] == '_skirt'", "images/StormSprite/Storm_Sprite_Legs_Skirt_Up.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(

                    "StormX.grool", ConditionSwitch(

                        "StormX.outfit['bottom'] == '_pants'", "images/StormSprite/Storm_Sprite_Legs_PantsW.png",
                        "StormX.outfit['bottom'] == '_yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPantsW.png",
                        "StormX.outfit['bottom'] == '_skirt'", "images/StormSprite/Storm_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(

                        "StormX.outfit['bottom'] == '_pants'", "images/StormSprite/Storm_Sprite_Legs_Pants.png",
                        "StormX.outfit['bottom'] == '_yoga_pants'", "images/StormSprite/Storm_Sprite_Legs_YogaPants.png",
                        "StormX.outfit['bottom'] == '_skirt'", "images/StormSprite/Storm_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['bottom'] == '_skirt' or StormX.outfit['bottom'] == '_pants'", Null(),
            "StormX.outfit['piercings'] == '_barbell'", ConditionSwitch(

                    "StormX.outfit['bottom'] and not StormX.upskirt", "images/StormSprite/Storm_Sprite_Barbell_PussyC.png",
                    "StormX.outfit['underwear'] and not StormX.underwear_pulled_down", "images/StormSprite/Storm_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "StormX.outfit['piercings'] == '_ring'", ConditionSwitch(

                    "StormX.outfit['bottom'] and not StormX.upskirt", "images/StormSprite/Storm_Sprite_Ring_PussyC.png",
                    "StormX.outfit['underwear'] and not StormX.underwear_pulled_down", "images/StormSprite/Storm_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['bottom'] and not StormX.upskirt", Null(),
            "StormX.spunk['pussy'] or StormX.spunk['anus']", "images/StormSprite/Storm_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.wet", Null(),
            "(StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra') and StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_Water_Tight1.png",
            "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Water_Tight2.png",
            "StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_Water_Loose1.png",
            "True", "images/StormSprite/Storm_Sprite_Water_Loose2.png",
            ),


        (0,0), ConditionSwitch(

            "StormX.outfit['neck'] == '_rings'", "images/StormSprite/Storm_Sprite_Necklace3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.top_pulled_up", ConditionSwitch(

                    "StormX.outfit['top'] == '_white_shirt'", "images/StormSprite/Storm_Sprite_Over_WhiteShirt_Up.png",
                    "StormX.outfit['top'] == '_jacket' and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Over_Jacket2_Up.png",
                    "StormX.outfit['top'] == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket1_Up.png",

                    "True", Null(),
                    ),


            "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra'", ConditionSwitch(

                    "StormX.outfit['top'] == '_white_shirt'", "images/StormSprite/Storm_Sprite_Over_WhiteShirtU.png",
                    "StormX.outfit['top'] == '_jacket' and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Over_Jacket2U.png",
                    "StormX.outfit['top'] == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket1U.png",
                    "True", Null(),
                    ),
            "StormX.outfit['top'] == '_white_shirt'", "images/StormSprite/Storm_Sprite_Over_WhiteShirtL.png",
            "StormX.outfit['top'] == '_jacket' and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Over_Jacket2L.png",
            "StormX.outfit['top'] == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket1L.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.top_pulled_up or StormX.outfit['top'] != '_jacket'", Null(),

            "StormX.outfit['bra'] == '_black_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_UpJ.png",
            "StormX.outfit['bra'] == '_lace_bra'", "images/StormSprite/Storm_Sprite_Chest_Bra_UpJ.png",
            "StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Chest_Sportsbra_UpJ.png",
            "StormX.outfit['bra'] == '_bikini_top'", "images/StormSprite/Storm_Sprite_Chest_Bikini_UpJ.png",
            "StormX.outfit['bra'] == '_tube_top'", "images/StormSprite/Storm_Sprite_Chest_Tube_UpJ.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['piercings'] or (not StormX.outfit['top'] and not StormX.outfit['bra'] and not StormX.top_pulled_up)", Null(),
            "StormX.outfit['top'] == '_jacket' and not StormX.top_pulled_up", Null(),
            "StormX.outfit['piercings'] == '_barbell'", ConditionSwitch(

                    "StormX.top_pulled_up", "images/StormSprite/Storm_Sprite_Barbell_TitsL.png",
                    "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra'", "images/StormSprite/Storm_Sprite_Barbell_TitsUC.png",
                    "True", "images/StormSprite/Storm_Sprite_Barbell_TitsLC.png",
                    ),
            "StormX.top_pulled_up", "images/StormSprite/Storm_Sprite_Ring_TitsL.png",
            "StormX.outfit['piercings'] == '_ring' and (StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra')", "images/StormSprite/Storm_Sprite_Ring_TitsUC.png",
            "StormX.outfit['piercings'] == '_ring'", "images/StormSprite/Storm_Sprite_Ring_TitsLC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.spunk['belly']", "images/StormSprite/Storm_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.spunk['breasts'] and (StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra' or StormX.outfit['bra'] == '_sports_bra')", "images/StormSprite/Storm_Sprite_Spunk_TitsU.png",
            "StormX.spunk['breasts']", "images/StormSprite/Storm_Sprite_Spunk_TitsL.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.arm_pose == 1", "images/StormSprite/Storm_Sprite_Arms1a.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['top'] == '_jacket'", "images/StormSprite/Storm_Sprite_Over_JacketC.png",
            "True", Null(),
            ),
        (53,-45), "Storm_sprite standing_Head",
        (0,0), ConditionSwitch(

            "StormX.arm_pose != 1 and renpy.showing('Storm_sprite handjob')", Null(),
            "StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Arms2a.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.wet and StormX.arm_pose != 1", "images/StormSprite/Storm_Sprite_Water_Arm2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.arm_pose != 1 and StormX.outfit['top'] == '_jacket' and renpy.showing('Storm_sprite handjob')", "images/StormSprite/Storm_Sprite_Over_Jacket2H.png",
            "StormX.arm_pose != 1 and StormX.outfit['top'] == '_jacket'", "images/StormSprite/Storm_Sprite_Over_Jacket2A.png",
            "StormX.arm_pose != 1 and StormX.outfit['loincloth'] == '_rings'", "images/StormSprite/Storm_Sprite_ArmRings2Top.png",
            "True", Null(),
            ),
















        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != StormX", Null(),


            "girl_offhand_action == 'fondle_pussy'", At('GirlGropePussy_StormSelf',GirlGropePussy_Storm1()),
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck_breasts'", "GirlGropeLeftBreast_Storm",

                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeRightBreast_Storm",

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
            "primary_action == 'suck_breasts'", "LickRightBreast_Storm",
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
                    "offhand_action == 'fondle_breasts' and primary_action == 'suck_breasts'", "GropeLeftBreast_Storm",

                    "True", "GropeRightBreast_Storm",

                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck_breasts'", "VibratorLeftBreast_Storm",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck_breasts'", "LickLeftBreast_Storm",
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
            "second_girl_primary_action == 'suck_breasts' and (offhand_action != 'suck_breasts' or primary_action == 'suck_breasts')", "LickLeftBreast_Storm",
            "second_girl_primary_action == 'suck_breasts'", "LickRightBreast_Storm",
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
            "girl_offhand_action == 'suck_breasts' and (offhand_action != 'suck_breasts' or primary_action == 'suck_breasts')", "LickLeftBreast_Storm",
            "girl_offhand_action == 'suck_breasts'", "LickRightBreast_Storm",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeLeftBreast_Storm",

                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck_breasts'", "GirlGropeRightBreast_Storm",

                    "girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck_breasts'", "GirlGropeLeftBreast_Storm",

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
    anchor (0.5, -0.198) zoom 0.95

image Storm_sprite standing_HairBack:
    contains:
        ConditionSwitch(

                "StormX.outfit['top'] == '_towel'", "images/StormSprite/Storm_Sprite_Over_Towel_Under.png",
                "True", Null(),
                ),
    contains:
        ConditionSwitch(




                "StormX.outfit['top'] == '_towel'", Null(),
                "StormX.outfit['hair'] == 'wethawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back_Wet.png",
                "StormX.outfit['hair'] == 'mohawk' and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back_Wet.png",
                "StormX.outfit['hair'] == 'mohawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Back.png",
                "StormX.outfit['hair'] == '_wet'", "images/StormSprite/Storm_Sprite_Hair_Long_Back_Wet.png",
                "StormX.outfit['hair'] and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Long_Back_Wet.png",
                "StormX.outfit['hair'] == 'short'", Null(),
                "StormX.outfit['hair']", "images/StormSprite/Storm_Sprite_Hair_Long_Back.png",
                "True", Null(),
                ),

    anchor (0.5, 0.5)
    zoom .47




























image Storm_sprite standing_Head:
    LiveComposite(
        (900,900),





        (0,0), ConditionSwitch(

                "StormX.blushing == '_blush2'", "images/StormSprite/Storm_Sprite_Head_Blush.png",

                "True", "images/StormSprite/Storm_Sprite_Head_Base.png",
                ),
        (0,0), ConditionSwitch(
            "not StormX.spunk['chin']", Null(),

            "True", "images/StormSprite/Storm_Sprite_Spunk_Chin.png",
            ),














        (0,0), ConditionSwitch(













            "True", ConditionSwitch(
                    "StormX.mouth == '_lipbite'", "images/StormSprite/Storm_Sprite_mouth_Lipbite.png",
                    "StormX.mouth == '_sucking'", "images/StormSprite/Storm_Sprite_mouth_Open.png",
                    "StormX.mouth == '_kiss'", "images/StormSprite/Storm_Sprite_mouth_Kiss.png",
                    "StormX.mouth == '_sad'", "images/StormSprite/Storm_Sprite_mouth_Sad.png",
                    "StormX.mouth == '_smile'", "images/StormSprite/Storm_Sprite_mouth_Smile.png",
                    "StormX.mouth == '_surprised'", "images/StormSprite/Storm_Sprite_mouth_Kiss.png",
                    "StormX.mouth == '_tongue'", "images/StormSprite/Storm_Sprite_mouth_Tongue.png",
                    "StormX.mouth == '_smile'", "images/StormSprite/Storm_Sprite_mouth_Smile.png",
                    "StormX.mouth == '_smirk'", "images/StormSprite/Storm_Sprite_mouth_Smirk.png",
                    "True", "images/StormSprite/Storm_Sprite_mouth_Normal.png",
                    ),
            ),


        (0,0), ConditionSwitch(
            "not StormX.spunk['mouth']", Null(),


            "StormX.mouth == '_sucking'", "images/StormSprite/Storm_Sprite_Spunk_Tongue.png",
            "StormX.mouth == '_kiss'", "images/StormSprite/Storm_Sprite_Spunk_Kiss.png",
            "StormX.mouth == '_sad'", "images/StormSprite/Storm_Sprite_Spunk_Sad.png",
            "StormX.mouth == '_smile'", "images/StormSprite/Storm_Sprite_Spunk_Smile.png",
            "StormX.mouth == '_surprised'", "images/StormSprite/Storm_Sprite_Spunk_Kiss.png",
            "StormX.mouth == '_tongue'", "images/StormSprite/Storm_Sprite_Spunk_Tongue.png",


            "True", "images/StormSprite/Storm_Sprite_Spunk_Smirk.png",
            ),

        (0,0), ConditionSwitch(

            "StormX.brows == '_angry'", "images/StormSprite/Storm_Sprite_brows_Angry.png",
            "StormX.brows == '_sad'", "images/StormSprite/Storm_Sprite_brows_Sad.png",
            "StormX.brows == '_surprised'", "images/StormSprite/Storm_Sprite_brows_Surprised.png",
            "StormX.brows == '_confused'", "images/StormSprite/Storm_Sprite_brows_Confused.png",
            "True", "images/StormSprite/Storm_Sprite_brows_Normal.png",
            ),
        (0,0), "Storm_blinking",
        (0,0), ConditionSwitch(

            "not StormX.wet", Null(),
            "True", "images/StormSprite/Storm_Sprite_Head_Water.png",
            ),
        (0,0), "images/StormSprite/Storm_Sprite_Earrings.png",
        (0,0), ConditionSwitch(


            "StormX.outfit['top'] == '_towel'", Null(),
            "StormX.outfit['hair'] == 'wethawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Wet.png",
            "StormX.outfit['hair'] == 'mohawk' and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Mohawk_Wet.png",
            "StormX.outfit['hair'] == 'mohawk'", "images/StormSprite/Storm_Sprite_Hair_Mohawk.png",
            "StormX.outfit['hair'] == '_wet'", "images/StormSprite/Storm_Sprite_Hair_Long_Wet.png",
            "StormX.outfit['hair'] and StormX.wet", "images/StormSprite/Storm_Sprite_Hair_Long_Wet.png",
            "StormX.outfit['hair'] == 'short'", "images/StormSprite/Storm_Sprite_Hair_Short.png",
            "renpy.showing('Storm_sprite sex')", "images/StormSprite/Storm_Sprite_Hair_Long_Sex.png",
            "StormX.outfit['hair']", "images/StormSprite/Storm_Sprite_Hair_Long.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "StormX.outfit['top'] == '_towel'", "images/StormSprite/Storm_Sprite_Over_Towel.png",
            "True", Null(),
            ),






        (0,0), ConditionSwitch(

            "StormX.spunk['hair'] and StormX.outfit['hair'] == 'short'", "images/StormSprite/Storm_Sprite_Spunk_Hair3.png",
            "StormX.spunk['hair'] and StormX.outfit['hair'] == 'mohawk'", "images/StormSprite/Storm_Sprite_Spunk_Hair2.png",
            "StormX.spunk['hair'] and StormX.outfit['hair'] == 'long'", "images/StormSprite/Storm_Sprite_Spunk_Hair1.png",
            "StormX.spunk['face']", "images/StormSprite/Storm_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['hair'] == 'short'", "images/StormSprite/Storm_Sprite_Earrings.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .47




image Storm_Squint:
    "images/StormSprite/Storm_Sprite_eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/StormSprite/Storm_Sprite_eyes_Sexy.png"
    .25
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































image Storm_sprite sex:
    LiveComposite(
        (1120,960),





        (0,0), ConditionSwitch(


                "Player.cock_position == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Storm_Sex_Fucking_action_speed3",
                        "action_speed >= 2", "Storm_Sex_Fucking_action_speed2",
                        "action_speed", "Storm_Sex_Fucking_action_speed1",
                        "True", "Storm_Sex_Fucking_action_animation0",
                        ),
                "Player.cock_position == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Storm_Sex_Anal_action_speed3",
                        "action_speed >= 2", "Storm_Sex_Anal_action_speed2",
                        "action_speed", "Storm_Sex_Anal_action_speed1",
                        "True", "Storm_Sex_Anal_action_animation0",
                        ),
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 2","Storm_Sex_Hotdog_action_speed2",
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 1","Storm_Sex_Hotdog_action_speed1",
                "Player.cock_position == 'footjob'", ConditionSwitch(

                        "action_speed >= 2", "Storm_Sex_FJ_action_speed2",
                        "action_speed", "Storm_Sex_FJ_action_speed1",
                        "True", "Storm_Sex_FJ_action_animation0",
                        ),

                "True", "Storm_Sex_animation0",
                ),

























        )
    align (0.6,0.0) zoom 0.7




image Storm_Sex_Body:
    LiveComposite(

        (1120,840),
        (245,-225), "Storm_HairBack_Sex",
        (0,0), "images/StormSex/Storm_Sex_Body.png",






        (0,0), ConditionSwitch(

            "not StormX.outfit['loincloth'] == '_rings' or StormX.outfit['top'] == '_jacket'", Null(),
            "True", "images/StormSex/Storm_Sex_Arms_Ring.png",
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['bra']", Null(),
            "StormX.outfit['bra'] == '_cosplay_bra'", "images/StormSex/Storm_Sex_Chest_Cos.png",
            "StormX.outfit['bra'] == '_tube_top'", "images/StormSex/Storm_Sex_Chest_Tube.png",
            "StormX.outfit['bra'] == '_black_bra'", "images/StormSex/Storm_Sex_Chest_Bra.png",
            "StormX.outfit['bra'] == '_lace_bra'", "images/StormSex/Storm_Sex_Chest_Bra.png",
            "not StormX.top_pulled_up", ConditionSwitch(

                    "StormX.outfit['bra'] == '_sports_bra'", "images/StormSex/Storm_Sex_Chest_SportsBra.png",
                    "StormX.outfit['bra'] == '_bikini_top' and StormX.outfit['underwear'] == '_bikini_bottoms'", "images/StormSex/Storm_Sex_Chest_Bikini_Combo.png",
                    "StormX.outfit['bra'] == '_bikini_top'", "images/StormSex/Storm_Sex_Chest_Bikini.png",

                    "True", Null(),
                    ),








            "True", ConditionSwitch(

                    "StormX.outfit['bra'] == '_sports_bra'", "images/StormSex/Storm_Sex_Chest_SportsBra_Up.png",

                    "StormX.outfit['bra'] == '_bikini_top'", "images/StormSex/Storm_Sex_Chest_Bikini_Up.png",

                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.wet", "images/StormSex/Storm_Sex_Wet_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['top'] == '_white_shirt' and StormX.top_pulled_up", "images/StormSex/Storm_Sex_Chest_Shirt_Up.png",
            "StormX.outfit['top'] == '_white_shirt'", "images/StormSex/Storm_Sex_Chest_Shirt.png",
            "StormX.outfit['top'] == '_jacket'", "images/StormSex/Storm_Sex_Chest_Jacket.png",
            "True", Null(),













            ),








        (0,0), ConditionSwitch(

            "StormX.outfit['neck'] == '_rings'", "images/StormSex/Storm_Sex_Neck_Ring.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "StormX.spunk['belly']", "images/StormSex/Storm_Sex_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "StormX.spunk['breasts']", "images/StormSex/Storm_Sex_Spunk_Tits_Back.png",
            "True", Null(),
            ),

        (220,-162), "Storm_Head_Sex",
        )
    yoffset -163



image Storm_Head_Sex:

    "Storm_sprite standing_Head"
    zoom 1.25
    anchor (0.5,0.5)
    rotate -7

image Storm_HairBack_Sex:

    "Storm_sprite standing_HairBack"
    zoom 1.25
    anchor (0.5,0.5)
    rotate -7


image Storm_Sex_Tits:
    LiveComposite(

        (1120,960),



        (0,0), ConditionSwitch(

            "StormX.outfit['bra'] == '_cosplay_bra'", "images/StormSex/Storm_Sex_Tits_Cos.png",
            "True", "images/StormSex/Storm_Sex_Tits.png",
            ),

        (0,0), ConditionSwitch(

            "StormX.outfit['piercings'] == '_barbell'", "images/StormSex/Storm_Sex_Pierce_Tits_Barbell.png",
            "StormX.outfit['piercings'] == '_ring'", "images/StormSex/Storm_Sex_Pierce_Tits_Ring.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['bra']", Null(),
            "StormX.outfit['bra'] == '_cosplay_bra'", Null(),
            "not StormX.top_pulled_up", ConditionSwitch(

                    "StormX.outfit['bra'] == '_tube_top'", "images/StormSex/Storm_Sex_Tits_Tube.png",
                    "StormX.outfit['bra'] == '_black_bra'", "images/StormSex/Storm_Sex_Tits_Bra.png",
                    "StormX.outfit['bra'] == '_lace_bra'", "images/StormSex/Storm_Sex_Tits_LaceBra.png",
                    "StormX.outfit['bra'] == '_sports_bra'", "images/StormSex/Storm_Sex_Tits_SportsBra.png",
                    "StormX.outfit['bra'] == '_bikini_top'", "images/StormSex/Storm_Sex_Tits_Bikini.png",
                    "True", Null(),
                    ),








            "True", ConditionSwitch(

                    "StormX.outfit['bra'] == '_tube_top'", "images/StormSex/Storm_Sex_Tits_Tube_Down.png",


                    "StormX.outfit['bra'] == '_sports_bra'", "images/StormSex/Storm_Sex_Tits_SportsBra_Up.png",
                    "StormX.outfit['bra'] == '_bikini_top'", "images/StormSex/Storm_Sex_Tits_Bikini_Up.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "StormX.wet", "images/StormSex/Storm_Sex_Wet_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['top']", Null(),
            "StormX.outfit['top'] == '_white_shirt' and StormX.top_pulled_up", "images/StormSex/Storm_Sex_Tits_Shirt_Up.png",
            "StormX.outfit['top'] == '_white_shirt'", "images/StormSex/Storm_Sex_Tits_Shirt.png",
            "True", Null(),
            ),




























        (0,0), ConditionSwitch(

            "(not StormX.outfit['bra'] and not StormX.outfit['top']) or StormX.top_pulled_up", Null(),
            "StormX.outfit['piercings'] == '_barbell'", "images/StormSex/Storm_Sex_Pierce_Tits_BarbellC.png",
            "StormX.outfit['piercings'] == '_ring'", "images/StormSex/Storm_Sex_Pierce_Tits_RingC.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "StormX.spunk['breasts']", "images/StormSex/Storm_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'suck_breasts' or offhand_action == 'suck_breasts'", "Storm_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Storm_Sex_Fondle_Breasts",
            "True", Null()
            ),

        )
    yoffset -163


image Storm_Sex_Lick_Breasts:
    "Lick_Anim"
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

            "StormX.outfit['bottom'] == '_skirt'", "images/StormSex/Storm_Sex_Legs_Skirt_Back.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "StormX.spunk['anus']", "images/StormSex/Storm_Sex_Spunk_Anal_Closed.png",
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

                    "StormX.outfit['hose'] == '_stockings_and_garterbelt'", "images/StormSex/Storm_Sex_Hose_StockingsGarter_FJ.png",
                    "StormX.outfit['hose'] == '_garterbelt'", "images/StormSex/Storm_Sex_Hose_Garter_FJ.png",
                    "StormX.outfit['hose'] == '_stockings'", "images/StormSex/Storm_Sex_Hose_Stockings_FJ.png",
                    "True", Null(),
                    ),
            "StormX.outfit['hose'] == '_stockings_and_garterbelt'", "images/StormSex/Storm_Sex_Hose_StockingsGarter.png",
            "StormX.outfit['hose'] == '_garterbelt'", "images/StormSex/Storm_Sex_Hose_Garter.png",
            "StormX.outfit['hose'] == '_stockings'", "images/StormSex/Storm_Sex_Hose_Stockings.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not StormX.outfit['loincloth'] == '_rings' or StormX.outfit['bottom'] == '_pants' or StormX.outfit['bottom'] == '_yoga_pants'", Null(),
            "show_feet", "images/StormSex/Storm_Sex_LegRings_FJ.png",
            "True", "images/StormSex/Storm_Sex_LegRings.png",
            ),
        (0,0), ConditionSwitch(

            "StormX.outfit['bottom'] and StormX.outfit['bottom'] != '_skirt' and not StormX.upskirt", Null(),
            "StormX.underwear_pulled_down",ConditionSwitch(

                    "StormX.outfit['underwear'] == '_cosplay_panties' and show_feet", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Down.png",
                    "StormX.outfit['underwear'] == '_cosplay_panties'", "images/StormSex/Storm_Sex_Panties_Cos_Down.png",
                    "StormX.outfit['underwear'] == '_white_panties' and show_feet", "images/StormSex/Storm_Sex_Panties_White_FJ_Down.png",
                    "StormX.outfit['underwear'] == '_white_panties'", "images/StormSex/Storm_Sex_Panties_White_Down.png",
                    "StormX.outfit['underwear'] and show_feet", "images/StormSex/Storm_Sex_Panties_Black_FJ_Down.png",
                    "StormX.outfit['underwear']", "images/StormSex/Storm_Sex_Panties_Black_Down.png",
                    "True", Null(),
                    ),
            "show_feet",ConditionSwitch(

                    "StormX.outfit['underwear'] == '_cosplay_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_Cos_FJ_Wet.png",
                    "StormX.outfit['underwear'] == '_cosplay_panties'", "images/StormSex/Storm_Sex_Panties_Cos_FJ.png",
                    "StormX.outfit['underwear'] == '_white_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_White_FJ_Wet.png",
                    "StormX.outfit['underwear'] == '_white_panties'", "images/StormSex/Storm_Sex_Panties_White_FJ.png",
                    "StormX.outfit['underwear'] == '_lace_panties'", "images/StormSex/Storm_Sex_Panties_Lace_FJ.png",
                    "StormX.outfit['underwear'] == '_bikini_bottoms' and (StormX.outfit['bra'] != '_bikini_top' or StormX.top_pulled_up)", "images/StormSex/Storm_Sex_Panties_Bikini_FJ_Top.png",
                    "StormX.outfit['underwear'] == '_bikini_bottoms'", "images/StormSex/Storm_Sex_Panties_Bikini_FJ.png",
                    "StormX.outfit['underwear'] and StormX.grool", "images/StormSex/Storm_Sex_Panties_Black_FJ_Wet.png",
                    "StormX.outfit['underwear']", "images/StormSex/Storm_Sex_Panties_Black_FJ.png",
                    "True", Null(),
                    ),
            "StormX.outfit['underwear'] == '_cosplay_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_Cos_Wet.png",
            "StormX.outfit['underwear'] == '_cosplay_panties'", "images/StormSex/Storm_Sex_Panties_Cos.png",
            "StormX.outfit['underwear'] == '_white_panties' and StormX.grool", "images/StormSex/Storm_Sex_Panties_White_Wet.png",
            "StormX.outfit['underwear'] == '_white_panties'", "images/StormSex/Storm_Sex_Panties_White.png",
            "StormX.outfit['underwear'] == '_lace_panties'", "images/StormSex/Storm_Sex_Panties_Lace.png",
            "StormX.outfit['underwear'] == '_bikini_bottoms' and (StormX.outfit['bra'] != '_bikini_top' or StormX.top_pulled_up)", "images/StormSex/Storm_Sex_Panties_Bikini_Top.png",
            "StormX.outfit['underwear'] == '_bikini_bottoms'", "images/StormSex/Storm_Sex_Panties_Bikini.png",
            "StormX.outfit['underwear'] and StormX.grool", "images/StormSex/Storm_Sex_Panties_Black_Wet.png",
            "StormX.outfit['underwear']", "images/StormSex/Storm_Sex_Panties_Black.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(




            "not StormX.outfit['underwear'] and StormX.outfit['hose'] != '_pantyhose'", Null(),
            "((StormX.outfit['underwear'] or StormX.outfit['hose'] == '_pantyhose') and StormX.underwear_pulled_down)", Null(),

            "StormX.outfit['piercings'] == '_barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.outfit['piercings'] == '_ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "StormX.outfit['underwear'] and StormX.underwear_pulled_down", Null(),
            "show_feet",ConditionSwitch(

                    "StormX.outfit['hose'] == '_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png",
                    "StormX.outfit['hose'] == '_ripped_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJHoled.png",
                    "True", Null(),
                    ),
            "StormX.outfit['hose'] == '_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose.png",
            "StormX.outfit['hose'] == '_ripped_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "StormX.outfit['bottom'] == '_skirt' and show_feet", "images/StormSex/Storm_Sex_Legs_Skirt_FJ.png",
            "StormX.upskirt",ConditionSwitch(

                    "StormX.outfit['bottom'] == '_skirt'", "images/StormSex/Storm_Sex_Legs_Skirt_Up.png",
                    "StormX.outfit['bottom'] == '_pants' and show_feet", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Down.png",
                    "StormX.outfit['bottom'] == '_pants'", "images/StormSex/Storm_Sex_Legs_Pants_Down.png",
                    "StormX.outfit['bottom'] == '_yoga_pants' and show_feet", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Down.png",
                    "StormX.outfit['bottom'] == '_yoga_pants'", "images/StormSex/Storm_Sex_Legs_YogaPants_Down.png",
                    "True", Null(),
                    ),
            "show_feet",ConditionSwitch(

                    "StormX.outfit['bottom'] == '_pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_Pants_FJ_Wet.png",
                    "StormX.outfit['bottom'] == '_pants'", "images/StormSex/Storm_Sex_Legs_Pants_FJ.png",
                    "StormX.outfit['bottom'] == '_yoga_pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ_Wet.png",
                    "StormX.outfit['bottom'] == '_yoga_pants'", "images/StormSex/Storm_Sex_Legs_YogaPants_FJ.png",
                    "True", Null(),
                    ),
            "StormX.outfit['bottom'] == '_skirt'", "images/StormSex/Storm_Sex_Legs_Skirt.png",
            "StormX.outfit['bottom'] == '_pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_Pants_Wet.png",
            "StormX.outfit['bottom'] == '_pants'", "images/StormSex/Storm_Sex_Legs_Pants.png",
            "StormX.outfit['bottom'] == '_yoga_pants' and StormX.grool > 1", "images/StormSex/Storm_Sex_Legs_YogaPants_Wet.png",
            "StormX.outfit['bottom'] == '_yoga_pants'", "images/StormSex/Storm_Sex_Legs_YogaPants.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(




            "not StormX.outfit['bottom']", Null(),
            "StormX.outfit['bottom'] and StormX.outfit['bottom'] != '_skirt' and StormX.upskirt", Null(),

            "StormX.outfit['piercings'] == '_barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellC.png",
            "StormX.outfit['piercings'] == '_ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_RingC.png",
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

            "StormX.outfit['hose'] == '_ripped_pantyhose' and (not StormX.outfit['underwear'] or not StormX.underwear_pulled_down)", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJHoled.png",
            "StormX.outfit['hose'] and StormX.outfit['hose'] != '_garterbelt' and StormX.outfit['hose'] != '_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png",
            "StormX.outfit['underwear'] and StormX.underwear_pulled_down", Null(),
            "StormX.outfit['hose'] == '_pantyhose'", "images/StormSex/Storm_Sex_Hose_Pantyhose_FJ.png",
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

                "StormX.spunk['pussy']", "images/StormSex/Storm_Sex_Spunk_Pussy.png",
                "True", Null(),
                )
    contains:















        ConditionSwitch(

                "Player.sprite and Player.cock_position == 'in' and action_speed >= 3", AlphaMask("Storm_Sex_Fucking_Zero_animation3", "Storm_Sex_Fucking_Mask"),
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 2", AlphaMask("Storm_Sex_Fucking_Zero_animation2", "Storm_Sex_Fucking_Mask"),
                "Player.sprite and Player.cock_position == 'in' and action_speed == 1", AlphaMask("Storm_Sex_Fucking_Zero_animation1", "Storm_Sex_Heading_Mask"),
                "Player.sprite and Player.cock_position == 'in'", "Storm_Sex_Fucking_Zero_animation0",
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "StormX.outfit['piercings'] == '_barbell' and Player.sprite and Player.cock_position == 'in' and action_speed", "images/StormSex/Storm_Sex_Pierce_Pussy_BarbellF.png",
                "StormX.outfit['piercings'] == '_ring' and Player.sprite and Player.cock_position == 'in' and action_speed", "images/StormSex/Storm_Sex_Pierce_Pussy_RingF.png",
                "StormX.outfit['piercings'] == '_barbell'", "images/StormSex/Storm_Sex_Pierce_Pussy_Barbell.png",
                "StormX.outfit['piercings'] == '_ring'", "images/StormSex/Storm_Sex_Pierce_Pussy_Ring.png",
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
                "not StormX.spunk['pussy'] or not Player.sprite or Player.cock_position != 'in' or not action_speed", Null(),

                "True", "images/StormSex/Storm_Sex_Spunk_Pussy_Over.png",
                )



image Storm_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.7
    offset (535,500)

image Storm_Sex_Lick_Ass:
    "Lick_Anim"
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
                "Player.sprite", "Zero_blowjob_cock" ,
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



image Storm_Sex_animation0:

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
            ease .5 ypos -130
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
                "Player.sprite", "Zero_blowjob_cock" ,
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
            ease .4 rotate 9
            ease .2 rotate 10
            repeat
    contains:

        subpixel True
        ConditionSwitch(

                "show_feet", AlphaMask("Storm_Sex_Feet", "images/StormSex/Storm_Sex_Mask_Foot2.png"),
                "True", Null(),
                )
        pos (0,-140)
















image Storm_Sex_Fucking_action_animation0:

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

            ease .9 ypos -130
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



image Storm_Sex_Fucking_Zero_animation0:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (0,40)
        block:
            pause 0.2
            easeout 1 ypos 20
            easein .8 ypos 10
            pause 1.4
            easeout 0.6 ypos 10
            easein 1 ypos 40
            repeat






image Storm_Sex_Fucking_action_speed1:

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



image Storm_Sex_Fucking_Zero_animation1:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (0,40)
        block:
            pause 0.2

            ease 2 ypos -10
            pause .8
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
        xzoom .7
        block:
            pause 0.2
            ease 1.2 xzoom 1
            ease .4 xzoom .9
            pause 1.2
            ease .2 xzoom 1
            ease 1.8 xzoom .7
            repeat

image Storm_Pussy_Spunk_Heading:

    contains:
        ConditionSwitch(
                "StormX.spunk['pussy'] and Player.sprite and Player.cock_position == 'in' and action_speed == 1", "images/StormSex/Storm_Sex_Spunk_Pussy_Over.png",
                "True", Null(),
                )
        anchor (0.5,0)
        transform_anchor True
        xoffset 560
        yoffset 5
        xzoom .7
        block:
            pause 0.2
            ease 1.2 xzoom 1
            ease .4 xzoom .9
            pause 1.2
            ease .2 xzoom 1
            ease 1.8 xzoom .7
            repeat





image Storm_Sex_Fucking_action_speed2:

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






image Storm_Sex_Fucking_Zero_animation2:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (0,-10)
        block:
            pause 0.2
            ease 0.95 ypos -145
            ease 0.25 ypos -140
            pause .8
            ease 2 ypos -10
            repeat





image Storm_Sex_Fucking_action_speed3:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-100)
        block:
            ease .5 ypos 0
            pause .4
            ease .9 ypos -100
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




image Storm_Sex_Fucking_Zero_animation3:

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
                "action_speed >= 3",  AlphaMask("Storm_Sex_Anal_Zero_animation3", "Storm_Sex_Anal_Mask"),
                "action_speed >= 2", AlphaMask("Storm_Sex_Anal_Zero_animation2", "Storm_Sex_Anal_Mask"),
                "action_speed", AlphaMask("Storm_Sex_Anal_Zero_animation1", "Storm_Sex_Anal_Mask"),
                "True", AlphaMask("Storm_Sex_Anal_Zero_animation0", "Storm_Sex_Anal_Mask"),
                )
    contains:

        ConditionSwitch(
                "not StormX.spunk['anus'] or not Player.sprite or Player.cock_position != 'anal' or not action_speed", Null(),
                "action_speed == 1", "Storm_Sex_Anal_Spunk_Heading_Over",
                "True", "images/StormSex/Storm_Sex_Spunk_Anal_Over.png",
                )

image Storm_Sex_Anal_Spunk_Heading_Over:
    "images/StormSex/Storm_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease .75 xzoom 1.0
        pause 1.75
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Storm_Sex_Anal_Spunk_Heading_Under:
    "images/StormSex/Storm_Sex_Spunk_Anal_Under.png"
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

image Storm_Sex_Anal_Mask:


    contains:
        "images/StormSex/Storm_Sex_Mask_Anal.png"
        yoffset 3



image Storm_Sex_Anal_action_animation0:

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
            ease .9 xpos 10
            ease .3 xpos 7
            ease .9 xpos -20
            ease .3 xpos -14
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


image Storm_Sex_Anal_Zero_animation0:
    contains:
        subpixel True
        ConditionSwitch(
                "not Player.sprite", Null(),
                "True", "Zero_blowjob_cock" ,
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
            pause .8
            ease 2 ypos 95
            repeat






image Storm_Sex_Anal_action_speed1:

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



image Storm_Sex_Anal_Zero_animation1:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (5,90)
        block:
            pause 0.2

            ease 2 ypos 40
            pause .8
            ease 2 ypos 90
            repeat






image Storm_Sex_Anal_action_speed2:

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






image Storm_Sex_Anal_Zero_animation2:

    contains:
        subpixel True
        "Storm_Sex_Zero_Cock"

        subpixel True
        pos (5,-10)
        block:
            pause 0.2
            ease 0.95 ypos -145
            ease 0.25 ypos -140
            pause .8
            ease 2 ypos -10
            repeat






image Storm_Sex_Anal_action_speed3:

    contains:

        subpixel True
        "Storm_Sex_Body"
        pos (0,-100)
        block:
            ease .5 ypos 0
            pause .4
            ease .9 ypos -100
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



image Storm_Sex_Anal_Zero_animation3:

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









image Storm_Sex_Hotdog_action_speed1:

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
            ease .7 ypos -85
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
            pause .6
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








image Storm_Sex_Hotdog_action_speed2:

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
            ease .9 ypos -70
            ease .5 ypos -80
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











image Storm_Sex_FJ_action_animation0:

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








image Storm_Sex_FJ_action_speed1:

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








image Storm_Sex_FJ_action_speed2:

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









image Storm_Hand_Under:
    "images/StormSprite/handstorm2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

image Storm_Hand_Over:
    "images/StormSprite/handstorm1.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

transform Storm_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5
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
        ease .5 ypos 450 rotate -2
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
        ease .2 ypos 430 rotate -3
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Storm_sprite handjob:
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Storm_Hand_Under"),
            "action_speed == 1", At("Storm_Hand_Under", Storm_Hand_1()),
            "action_speed >= 2", At("Storm_Hand_Under", Storm_Hand_2()),
            "action_speed", Null(),
            ),
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1J()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "action_speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Storm_Hand_Over"),
            "action_speed == 1", At("Storm_Hand_Over", Storm_Hand_1()),
            "action_speed >= 2", At("Storm_Hand_Over", Storm_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4








image Storm_sprite blowjob:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "action_speed == 0", "Storm_BJ_animation0",
            "action_speed == 1", "Storm_BJ_animation1",
            "action_speed == 2", "Storm_BJ_animation2",
            "action_speed == 3", "Storm_BJ_animation3",
            "action_speed == 4", "Storm_BJ_animation4",
            "action_speed == 5", "Storm_BJ_Anim5",
            "action_speed == 6", "Storm_BJ_Anim6",
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Storm_BJ_HairBack:

    ConditionSwitch(
            "(StormX.outfit['hair'] == 'long' and StormX.wet) or StormX.outfit['hair'] == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Under.png",
            "StormX.outfit['hair'] == 'mohawk' or StormX.outfit['hair'] == 'wethawk' or StormX.outfit['hair'] == 'short'", Null(),
            "True", "images/StormBJFace/Storm_BJ_Hair_Long_Under.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Storm_BJ_HairTop:
    contains:
        ConditionSwitch(
                "(StormX.outfit['hair'] == 'mohawk' and StormX.wet) or StormX.outfit['hair'] == 'wethawk'", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png",
                "StormX.wet or StormX.outfit['hair'] == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png",
                "StormX.outfit['hair'] == 'mohawk'", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png",
                "StormX.outfit['hair'] == 'short'", "images/StormBJFace/Storm_BJ_Hair_Short.png",
                "True", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png",
                )
    contains:
        ConditionSwitch(

                "StormX.spunk['hair'] and (StormX.wet or StormX.outfit['hair'] == 'wethawk' or StormX.outfit['hair'] == '_wet')", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
                "StormX.spunk['hair'] and StormX.outfit['hair'] == 'mohawk'", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
                "StormX.spunk['hair']", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
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






            "StormX.blushing == '_blush2'", "images/StormBJFace/Storm_BJ_Head_Blush2.png",

            "True", "images/StormBJFace/Storm_BJ_Head_Blush0.png"
            ),
        (0,0), ConditionSwitch(









            "Speed and renpy.showing('Storm_sprite blowjob')", ConditionSwitch(

                    "action_speed == 1", "images/StormBJFace/Storm_BJ_mouth_Tongue.png",
                    "(action_speed == 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/StormBJFace/Storm_BJ_mouth_Sucking.png",
                    "action_speed == 4", "images/StormBJFace/Storm_BJ_mouth_Sucking.png",
                    "action_speed == 6", "images/StormBJFace/Storm_BJ_mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Storm_sprite titjob')", "images/StormBJFace/Storm_BJ_mouth_Tongue.png",
            "StormX.mouth == '_normal'", "images/StormBJFace/Storm_BJ_mouth_Smile.png",
            "StormX.mouth == '_lipbite'", "images/StormBJFace/Storm_BJ_mouth_Lipbite.png",
            "StormX.mouth == '_sucking'", "images/StormBJFace/Storm_BJ_mouth_Tongue.png",
            "StormX.mouth == '_kiss'", "images/StormBJFace/Storm_BJ_mouth_Kiss.png",
            "StormX.mouth == '_sad'", "images/StormBJFace/Storm_BJ_mouth_Sad.png",
            "StormX.mouth == '_smile'", "images/StormBJFace/Storm_BJ_mouth_Smile.png",
            "StormX.mouth == '_smirk'", "images/StormBJFace/Storm_BJ_mouth_Smirk.png",
            "StormX.mouth == '_smile'", "images/StormBJFace/Storm_BJ_mouth_Smile.png",
            "StormX.mouth == '_surprised'", "images/StormBJFace/Storm_BJ_mouth_Kiss.png",
            "StormX.mouth == '_tongue'", "images/StormBJFace/Storm_BJ_mouth_Tongue.png",
            "True", "images/StormBJFace/Storm_BJ_mouth_Smile.png",
            ),
        (428,555), ConditionSwitch(


            "not renpy.showing('Storm_sprite blowjob')", Null(),
            "action_speed == 2", "Storm_BJ_mouthHeading",
            "action_speed == 5", "Storm_BJ_mouthCumHigh",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not StormX.spunk['mouth']", Null(),
            "Speed and renpy.showing('Storm_sprite blowjob')", ConditionSwitch(

                    "action_speed == 1", "images/StormBJFace/Storm_BJ_Spunk_Tongue.png",
                    "(action_speed == 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 4", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 6", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
                    ),
            "StormX.mouth == '_normal'", "images/StormBJFace/Storm_BJ_Spunk_Smile.png",



            "StormX.mouth == '_smile'", "images/StormBJFace/Storm_BJ_Spunk_Smile.png",


            "StormX.mouth == '_tongue'", "images/StormBJFace/Storm_BJ_Spunk_Tongue.png",
            "StormX.mouth == '_sucking'", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
            "True", "images/StormBJFace/Storm_BJ_Spunk_Kiss.png",
            ),
        (0,0), ConditionSwitch(

            "StormX.brows == '_angry'", "images/StormBJFace/Storm_BJ_brows_Angry.png",
            "StormX.brows == '_sad'", "images/StormBJFace/Storm_BJ_brows_Sad.png",
            "StormX.brows == '_surprised'", "images/StormBJFace/Storm_BJ_brows_Surprised.png",
            "StormX.brows == '_confused'", "images/StormBJFace/Storm_BJ_brows_Confused.png",
            "True", "images/StormBJFace/Storm_BJ_brows_Normal.png",
            ),
        (0,0), "Storm_sprite BJ Blink",

        (0,0), "images/StormBJFace/Storm_BJ_Earring.png",
        (0,0), ConditionSwitch(

            "not StormX.wet", Null(),
            "True", "images/StormBJFace/Storm_BJ_Wet.png",
            ),
        (0,0), ConditionSwitch(

            "(StormX.outfit['hair'] == 'mohawk' and StormX.wet) or StormX.outfit['hair'] == 'wethawk'", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png",
            "StormX.wet or StormX.outfit['hair'] == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png",
            "StormX.outfit['hair'] == 'mohawk'", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png",
            "StormX.outfit['hair'] == 'short'", "images/StormBJFace/Storm_BJ_Hair_Short_Over.png",
            "True", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png",
            ),


        (0,0), ConditionSwitch(

            "StormX.spunk['face']", "images/StormBJFace/Storm_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "StormX.spunk['hair'] and (StormX.wet or StormX.outfit['hair'] == 'wethawk' or StormX.outfit['hair'] == '_wet')", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
            "StormX.spunk['hair'] and StormX.outfit['hair'] == 'short'", "images/StormBJFace/Storm_BJ_Spunk_HairS.png",
            "StormX.spunk['hair'] and StormX.outfit['hair'] == 'mohawk'", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
            "StormX.spunk['hair']", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Storm_Tester:
    "images/StormBJFace/Storm_BJ_tester.jpg"
    alpha 0.5
image Storm_sprite BJ Blink:

    ConditionSwitch(
            "StormX.eyes == '_normal'", "images/StormBJFace/Storm_BJ_eyes_Normal.png",
            "StormX.eyes == '_sexy'", "images/StormBJFace/Storm_BJ_eyes_Sexy.png",
            "StormX.eyes == '_closed'", "images/StormBJFace/Storm_BJ_eyes_Closed.png",
            "StormX.eyes == '_surprised'", "images/StormBJFace/Storm_BJ_eyes_Surprised.png",
            "StormX.eyes == '_side'", "images/StormBJFace/Storm_BJ_eyes_Side.png",
            "StormX.eyes == '_stunned'", "images/StormBJFace/Storm_BJ_eyes_Stunned.png",
            "StormX.eyes == '_down'", "images/StormBJFace/Storm_BJ_eyes_Down.png",
            "StormX.eyes == '_manic'", "images/StormBJFace/Storm_BJ_eyes_Surprised.png",
            "StormX.eyes == '_squint'", "images/StormBJFace/Storm_BJ_eyes_Sexy.png",
            "True", "images/StormBJFace/Storm_BJ_eyes_Normal.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/StormBJFace/Storm_BJ_eyes_Closed.png"
    .25
    repeat

image Storm_BJ_mouthHeading:

    transform_anchor True
    contains:

        "images/StormBJFace/Storm_BJ_mouth_Heading.png"
        zoom 1.4
        anchor (0.50,0.6)
    contains:
        ConditionSwitch(
            "StormX.spunk[mouth]", "images/StormBJFace/Storm_BJ_Spunk_SuckingUnder.png",
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)
    contains:
        ConditionSwitch(
            "StormX.spunk[mouth]", "images/StormBJFace/Storm_BJ_Spunk_SuckingOver.png",
            "True", Null(),
            ),
        zoom 1.4
        anchor (0.50,0.6)
    subpixel True
    zoom 0.58
    block:
        pause .20
        easeout .15 zoom 0.6
        linear .15 zoom 0.60
        easein .25 zoom 0.65
        pause .25

        pause .40
        easeout .40 zoom 0.58
        linear .10 zoom 0.66
        easein .30 zoom 0.45
        pause .30

        repeat

image Storm_BJ_mouthCumHigh:

    contains:
        "images/StormBJFace/Storm_BJ_mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.6)
    subpixel True
    zoom 0.65
    block:
        pause .20
        ease .50 zoom 0.58
        pause .60
        ease .30 zoom 0.62
        pause .10
        ease .30 zoom 0.58
        pause .20
        ease .30 zoom 0.62
        repeat

image Storm_BJ_mouthSuckingMask:

    contains:
        "images/StormBJFace/Storm_BJ_mouth_MaskS.png"
        zoom 1.4














image Storm_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", "Storm_BJ_mouthHeadingComposite",
            "action_speed == 5", "Storm_BJ_mouthCumHighComposite",
            "True", Null(),
            ),
        (300,462), ConditionSwitch(
            "action_speed == 2 and StormX.spunk[mouth]", "StormHeadingSpunk",
            "action_speed == 5 and StormX.spunk[mouth]", "StormCumHighSpunk",
            "True", Null(),
            ),
        )
    zoom 1.8

image Storm_BJ_mouthHeadingComposite:

    transform_anchor True
    contains:

        "images/StormBJFace/Storm_BJ_mouth_MaskH.png"


        anchor (0.50,0.6)
    offset (30,-30)
    subpixel True
    zoom 0.58
    block:
        pause .20
        easeout .15 zoom 0.6
        linear .15 zoom 0.60
        easein .25 zoom 0.65
        pause .25

        pause .40
        easeout .40 zoom 0.58
        linear .10 zoom 0.66
        easein .30 zoom 0.45
        pause .30

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
        pause .20
        easeout .15 zoom 0.6
        linear .15 zoom 0.60
        easein .25 zoom 0.65
        pause .25

        pause .40
        easeout .40 zoom 0.58
        linear .10 zoom 0.66
        easein .30 zoom 0.45
        pause .30

        repeat


image Storm_BJ_mouthCumHighComposite:

    contains:

        "images/StormBJFace/Storm_BJ_mouth_MaskH.png"
        anchor (0.50,0.6)
    subpixel True
    offset (30,-30)
    zoom 0.65
    block:
        pause .20
        ease .50 zoom 0.58
        pause .60
        ease .30 zoom 0.62
        pause .10
        ease .30 zoom 0.58
        pause .20
        ease .30 zoom 0.62
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
        pause .20
        ease .50 zoom 0.58
        pause .60
        ease .30 zoom 0.62
        pause .10
        ease .30 zoom 0.58
        pause .20
        ease .30 zoom 0.62
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



image Storm_BJ_animation0:

    contains:

        "Storm_BJ_HairBack"
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

        "Zero_blowjob_cock"
        anchor (.5,.5)
        rotate -10
        offset (650,370)


image Storm_BJ_animation1:

    contains:

        "Storm_BJ_HairBack"
        subpixel True

        offset (350,175)
        block:
            ease 2.5 offset (375,310)
            ease 2 offset (350,175)
            pause .5
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,-35)
        block:
            ease 2.5 offset (30,90)
            ease 2 offset (0,-35)
            pause .5
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True
        offset (350,175)
        block:
            ease 2.5 offset (375,310)
            ease 2 offset (350,175)
            pause .5
            repeat
    contains:

        "Zero_blowjob_cock"
        subpixel True
        anchor (.5,.5)
        offset (650,370)
        rotate 0
        block:
            ease 2 rotate -5
            pause .5
            ease 2.5 rotate 0
            repeat



image Storm_BJ_animation2:

    contains:

        "Storm_BJ_HairBack"
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

        "Zero_blowjob_cock"
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

















image Storm_BJ_animation3:

    contains:

        "Storm_BJ_HairBack"
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

        "Zero_blowjob_cock"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_mouthSuckingMask")
        subpixel True
        offset (-250,-390)
        block:
            ease 1 yoffset -320
            ease 1.5 yoffset -390
            repeat
    contains:

        ConditionSwitch(

                        "StormX.spunk[mouth]", "StormSuckingSpunk",
                        "True", Null(),
                        )
        subpixel True
        offset (350,260)
        block:
            ease 1 yoffset 330
            ease 1.5 yoffset 260
            repeat


image Storm_BJ_animation4:

    contains:

        "Storm_BJ_HairBack"
        subpixel True

        offset (350,360)
        block:
            subpixel True
            ease 1 yoffset 560
            pause .5
            ease 2 yoffset 360
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,100)
        block:
            subpixel True
            ease 1.2 yoffset 250
            pause .5
            ease 1.8 yoffset 100
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True
        offset (350,360)
        block:
            subpixel True
            ease 1 yoffset 560
            pause .5
            ease 2 yoffset 360
            repeat
    contains:

        "Zero_blowjob_cock"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_mouthSuckingMask")
        subpixel True
        offset (-250,-290)
        block:
            subpixel True
            ease 1 yoffset -90
            pause .5
            ease 2 yoffset -290
            repeat
    contains:








        ConditionSwitch(

                        "StormX.spunk[mouth]", "StormSuckingSpunk",
                        "True", Null(),
                        )
        subpixel True
        offset (350,360)
        block:
            subpixel True
            ease 1 yoffset 560
            pause .5
            ease 2 yoffset 360
            repeat



image Storm_BJ_Anim5:

    contains:

        "Storm_BJ_HairBack"
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

        "Zero_blowjob_cock"
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

        "Storm_BJ_HairBack"
        subpixel True
        offset (350,440)
        block:
            subpixel True
            ease 1 yoffset 460
            pause .5
            ease 2 yoffset 440
            repeat
    contains:

        "Storm_BJ_Backdrop"
        subpixel True
        offset (0,190)
        block:
            subpixel True
            ease 1.2 yoffset 200
            pause .5
            ease 1.8 yoffset 190
            repeat
    contains:

        "Storm_BJ_Head"
        subpixel True

        offset (350,440)
        block:
            subpixel True
            ease 1 yoffset 460
            pause .5
            ease 2 yoffset 440
            repeat
    contains:

        "Zero_blowjob_cock"
        subpixel True
        anchor (.5,.5)
        rotate 0
        alpha 1
        offset (650,370)
    contains:

        AlphaMask("Storm_BJ_Head", "Storm_BJ_mouthSuckingMask")
        subpixel True
        offset (-250,-210)
        block:
            subpixel True
            ease 1 yoffset -190
            pause .5
            ease 2 yoffset -210
            repeat
    contains:

        ConditionSwitch(

                        "StormX.spunk[mouth]", "StormSuckingSpunk",
                        "True", Null(),
                        )
        subpixel True
        offset (350,440)
        block:
            subpixel True
            ease 1 yoffset 460
            pause .5
            ease 2 yoffset 440
            repeat






label Storm_BJ_Launch(Line=primary_action):
    if renpy.showing("Storm_sprite blowjob"):
        return


    if renpy.showing("Storm_sprite titjob"):
        hide Storm_sprite titjob
    else:
        call hide_girl(StormX)
        if Line == "L" or Line == "cum":
            show Storm_sprite standing zorder StormX.sprite_layer at sprite_location(stage_center):
                alpha 1
                ease 1 zoom 2.5 offset (150,80)
            with dissolve
        else:
            show Storm_sprite standing zorder StormX.sprite_layer at sprite_location(stage_center):
                alpha 1
                zoom 2.5 offset (150,80)
            with dissolve
        hide Storm_sprite

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    show Storm_sprite blowjob zorder 150:
        pos (630,650)
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
    if not renpy.showing("Storm_sprite blowjob"):
        return

    call hide_girl(StormX)
    $ action_speed = 0

    show Storm_sprite standing zorder StormX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Storm_sprite standing zorder StormX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Storm_sprite standing zorder StormX.sprite_layer at sprite_location(StormX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return








image Storm_sprite titjob:

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
    zoom .8
    transform_anchor True
    anchor (.5,.5)




image Storm_TJ_HairBack:

    "Storm_BJ_HairBack"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Storm_TJ_Head:

    "Storm_BJ_Head"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Storm_TJ_HairTop:

    contains:
        ConditionSwitch(
                        "(StormX.outfit['hair'] == 'mohawk' and StormX.wet) or StormX.outfit['hair'] == 'wethawk'", "images/StormBJFace/Storm_BJ_Hair_WetM_Over.png",
                        "StormX.wet or StormX.outfit['hair'] == '_wet'", "images/StormBJFace/Storm_BJ_Hair_WetL_Over.png",
                        "StormX.outfit['hair'] == 'mohawk'", "images/StormBJFace/Storm_BJ_Hair_Mohawk_Over.png",
                        "StormX.outfit['hair'] == 'short'", "images/StormBJFace/Storm_BJ_Hair_Short_Over.png",
                        "True", "images/StormBJFace/Storm_BJ_Hair_Long_Over.png",
                        )
        offset (83,-80)
    contains:
        ConditionSwitch(

                        "StormX.spunk['hair'] and (StormX.wet or StormX.outfit['hair'] == 'wethawk' or StormX.outfit['hair'] == '_wet')", "images/StormBJFace/Storm_BJ_Spunk_HairW.png",
                        "StormX.spunk['hair'] and StormX.outfit['hair'] == 'mohawk'", "images/StormBJFace/Storm_BJ_Spunk_HairM.png",
                        "StormX.spunk['hair']", "images/StormBJFace/Storm_BJ_Spunk_HairL.png",
                        "True", Null(),
                        )
        offset (83,-80)




    transform_anchor True
    zoom .98
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Storm_TJ_ZeroCock:

    "Zero_blowjob_cock"
    transform_anchor True
    zoom .6
    anchor (0.5, 0.5)
    offset (30,50)
    rotate 0

image Storm_TJ_Body:

    contains:
        ConditionSwitch(
                        "StormX.outfit['top'] or renpy.showing('Storm_sprite titjob')", Null(),
                        "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra'","images/StormBJFace/Storm_TJ_Chest_Bra_Back.png",
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
                        "not StormX.outfit['loincloth'] == '_rings' or StormX.outfit['top'] == '_jacket'", Null(),
                        "True", "images/StormBJFace/Storm_TJ_Arms_Ring.png",
                        )
    contains:

        ConditionSwitch(

                        "StormX.outfit['bra'] == '_cosplay_bra'","images/StormBJFace/Storm_TJ_Chest_Cos_TopD.png",
                        "StormX.outfit['bra'] == '_sports_bra'","images/StormBJFace/Storm_TJ_Chest_Sportsbra_Body.png",
                        "StormX.outfit['bra'] == '_bikini_top'","images/StormBJFace/Storm_TJ_Chest_Bikini_Body.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.outfit['top'] == '_white_shirt'","images/StormBJFace/Storm_TJ_Over_WhiteShirt_Body.png",
                        "StormX.outfit['top'] == '_jacket'","images/StormBJFace/Storm_TJ_Over_Jacket_Body.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not StormX.spunk['breasts']",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Spunk_Body.png",
                        )
    contains:

        ConditionSwitch(
                        "StormX.outfit['neck'] == '_rings'", "images/StormBJFace/Storm_TJ_Neck_Ring.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.outfit['top']", Null(),
                        "StormX.outfit['hair'] == 'long' and not StormX.wet", "images/StormBJFace/Storm_TJ_Hair_Long_Mid.png",
                        "True",   Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0


image Storm_TJ_Tit_Under:

    contains:

        ConditionSwitch(

                    "StormX.outfit['bra'] == '_cosplay_bra'",Null(),
                    "renpy.showing('Storm_sprite titjob')", "images/StormBJFace/Storm_TJ_TitsUnder.png",
                    "True",  Null(),
                    )





    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Storm_TJ_Braback:

    contains:
        ConditionSwitch(

                        "StormX.outfit['top']",Null(),
                        "StormX.outfit['bra'] == '_black_bra' or StormX.outfit['bra'] == '_lace_bra'","images/StormBJFace/Storm_TJ_Chest_Bra_Back.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Storm_TJ_BraStretch:

    contains:
        ConditionSwitch(

                        "StormX.outfit['bra'] == '_bikini_top'","images/StormBJFace/Storm_TJ_Chest_Bikini_Tent.png",
                        "StormX.outfit['bra'] == '_sports_bra'","images/StormBJFace/Storm_TJ_Chest_Sportsbra_Tent.png",
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
                        "StormX.outfit['piercings'] == '_barbell'","images/StormBJFace/Storm_TJ_Pierce_Barbell.png",
                        "StormX.outfit['top'] == '_white_shirt' and not StormX.top_pulled_up",Null(),
                        "StormX.outfit['bra'] and not StormX.top_pulled_up",Null(),
                        "StormX.outfit['piercings'] == '_ring'","images/StormBJFace/Storm_TJ_Pierce_Ring.png",
                        "True", Null(),
                        )
    contains:
        ConditionSwitch(
                        "not StormX.wet",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Tits_Wet.png",
                        )
    contains:
        ConditionSwitch(
                        "not StormX.spunk['breasts']",Null(),
                        "True",       "images/StormBJFace/Storm_TJ_Spunk_Tits.png",
                        )
    contains:

        ConditionSwitch(
                        "StormX.outfit['top'] == '_jacket'","images/StormBJFace/Storm_TJ_Over_Jacket_Top.png",

                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.outfit['bra'] == '_black_bra' and StormX.top_pulled_up and StormX.outfit['top']","images/StormBJFace/Storm_TJ_Chest_Bra_TopUS.png",
                        "StormX.outfit['bra'] == '_black_bra' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_Bra_TopU.png",
                        "StormX.outfit['bra'] == '_lace_bra' and StormX.top_pulled_up and StormX.outfit['top']","images/StormBJFace/Storm_TJ_Chest_Bra_TopUS.png",
                        "StormX.outfit['bra'] == '_lace_bra' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_Bra_TopU.png",
                        "StormX.outfit['bra'] == '_sports_bra' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_SportsBra_TopU.png",
                        "StormX.outfit['bra'] == '_bikini_top' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_Bikini_TopU.png",

                        "StormX.outfit['bra'] == '_tube_top' and not StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Chest_TubeD.png",
                        "StormX.outfit['bra'] == '_black_bra' and StormX.outfit['top']","images/StormBJFace/Storm_TJ_Chest_Bra_TopDS.png",
                        "StormX.outfit['bra'] == '_black_bra'","images/StormBJFace/Storm_TJ_Chest_Bra_TopD.png",
                        "StormX.outfit['bra'] == '_lace_bra' and StormX.outfit['top']","images/StormBJFace/Storm_TJ_Chest_Lacebra_TopDS.png",
                        "StormX.outfit['bra'] == '_lace_bra'","images/StormBJFace/Storm_TJ_Chest_Lacebra_TopD.png",
                        "StormX.outfit['bra'] == '_sports_bra'","images/StormBJFace/Storm_TJ_Chest_Sportsbra_TopD.png",
                        "StormX.outfit['bra'] == '_bikini_top'","images/StormBJFace/Storm_TJ_Chest_Bikini_TopD.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "StormX.outfit['top'] == '_white_shirt' and StormX.top_pulled_up","images/StormBJFace/Storm_TJ_Over_WhiteShirt_TopU.png",
                        "StormX.outfit['top'] == '_white_shirt'","images/StormBJFace/Storm_TJ_Over_WhiteShirt_TopD.png",

                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not StormX.outfit['loincloth'] == '_rings' or StormX.outfit['top'] == '_jacket'", Null(),
                        "True", "images/StormBJFace/Storm_TJ_Wrists_Ring.png",
                        )
    contains:

        ConditionSwitch(
                        "StormX.top_pulled_up", Null(),
                        "(not StormX.outfit['top']) and (not StormX.outfit['bra'])", Null(),
                        "StormX.outfit['piercings'] == '_ring' and StormX.outfit['top'] == '_white_shirt'","images/StormBJFace/Storm_TJ_Pierce_Ring_Shirt.png",
                        "StormX.outfit['piercings'] == '_barbell' and StormX.outfit['top'] == '_white_shirt'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Shirt.png",
                        "StormX.outfit['bra'] == '_cosplay_bra'",Null(),
                        "StormX.outfit['piercings'] == '_ring' and StormX.outfit['bra'] == '_lace_bra'","images/StormBJFace/Storm_TJ_Pierce_Ring_Lace.png",
                        "StormX.outfit['piercings'] == '_barbell' and StormX.outfit['bra'] == '_lace_bra'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Lace.png",
                        "StormX.outfit['piercings'] == '_ring' and StormX.outfit['bra'] == '_tube_top'","images/StormBJFace/Storm_TJ_Pierce_Ring_Tube.png",
                        "StormX.outfit['piercings'] == '_barbell' and StormX.outfit['bra'] == '_tube_top'","images/StormBJFace/Storm_TJ_Pierce_Barbell_Tube.png",
                        "StormX.outfit['piercings'] == '_ring' and StormX.outfit['bra']","images/StormBJFace/Storm_TJ_Pierce_Ring_Bra.png",
                        "StormX.outfit['piercings'] == '_barbell' and StormX.outfit['bra']","images/StormBJFace/Storm_TJ_Pierce_Barbell_Bra.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not StormX.outfit['loincloth'] == '_rings' or not StormX.outfit['piercings'] == '_ring'", Null(),
                        "StormX.outfit['top'] == '_white_shirt' and not StormX.top_pulled_up", Null(),
                        "StormX.outfit['bra'] and StormX.outfit['bra'] != '_cosplay_bra' and not StormX.top_pulled_up",Null(),
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
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Storm_TJ_HairBack"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos -0
            pause .1
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,0)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 rotate -3
            pause .1
            ease 2 rotate -5
            pause .1
            repeat
    contains:
        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-70,-210)
        transform_anchor True
        xzoom .75
        yzoom .85
        parallel:
            ease 2 yzoom .5
            pause .1
            ease 2 yzoom .85
            pause .1
            repeat
        parallel:
            ease 2 pos (-60,-230)
            pause .1
            ease 2 pos (-70,-210)
            pause .1
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Storm_TJ_HairTop"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat





image Storm_TJ_1:

    contains:

        "Storm_TJ_Braback"
        subpixel True










        pos (0,50)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -60
            pause .4
            ease 1.8 ypos 60
            ease .5 ypos 50
            repeat
    contains:


        "Storm_TJ_HairBack"
        subpixel True
        pos (0,60)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos -40
            pause .2
            ease 2 ypos 60
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,60)
        transform_anchor True
        parallel:
            ease 2 ypos -40
            pause .2
            ease 2 ypos 60
            pause .5
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,60)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos -40
            pause .2
            ease 2 ypos 60
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,60)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -60
            pause .4
            ease 1.8 ypos 60
            ease .5 ypos 50
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,25)
        transform_anchor True
        rotate -6
        parallel:
            ease 2 ypos 0
            pause .4
            ease 1.8 ypos 25
            pause .5
            repeat
    contains:






        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-100,-150)
        transform_anchor True
        xzoom .9
        yzoom 1.3
        parallel:
            pause .1
            ease 1.6 yzoom .3
            pause .9
            ease 1.6 yzoom 1.5
            ease .5 yzoom 1.3
            repeat
        parallel:
            pause .1
            ease 1.9 xzoom .6
            pause .4
            ease 1.8 xzoom .9
            pause .5

            repeat
        parallel:
            pause .1
            ease 1.9 pos (-50,-260)
            pause .4
            ease 1.8 pos (-100,-140)
            ease .5 pos (-100,-150)
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,50)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -60
            pause .4
            ease 1.8 ypos 60
            ease .5 ypos 50
            repeat
    contains:

        "Storm_TJ_HairTop"
        subpixel True
        pos (0,60)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos -40
            pause .2
            ease 2 ypos 60
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat







image Storm_TJ_2:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease .3 ypos 40
            ease .7 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        "Storm_TJ_HairBack"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,80)
        transform_anchor True
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease .3 ypos 40
            ease .7 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,30)
        transform_anchor True
        rotate -4
        parallel:
            ease 1 ypos 0
            pause .2
            ease .4 ypos 30
            repeat
        parallel:
            ease 1 rotate -2
            pause .1
            ease .5 rotate -4
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
            ease .3 yzoom 1.3
            ease .7 yzoom .3
            pause .2
            ease .4 yzoom 1.7
            repeat
        parallel:
            ease .3 pos (-100,-160)
            ease .7 pos (-80,-240)
            pause .2
            ease .4 pos (-100,-120)
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease .3 ypos 40
            ease .7 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:


        "Storm_TJ_HairTop"
        subpixel True
        pos (0,80)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat




image Storm_TJ_3:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,110)
        transform_anchor True
        block:
            ease .3 ypos 100
            ease .7 ypos 60
            pause .2
            ease .4 ypos 110
            repeat
    contains:

        "Storm_TJ_HairBack"
        subpixel True
        pos (0,140)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos 70
            pause .1
            ease .5 ypos 140
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,130)
        transform_anchor True
        parallel:
            ease 1 ypos 100
            pause .1
            ease .5 ypos 130
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,140)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos 70
            pause .1
            ease .5 ypos 140
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,110)
        transform_anchor True
        block:
            ease .3 ypos 100
            ease .7 ypos 60
            pause .2
            ease .4 ypos 110
            repeat
    contains:

        subpixel True
        "Storm_TJ_ZeroCock"
        pos (0,30)
        transform_anchor True
        rotate -4
        parallel:
            ease 1 ypos 0
            pause .2
            ease .4 ypos 30
            repeat
        parallel:
            ease 1 rotate -2
            pause .1
            ease .5 rotate -4
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
            ease .3 yzoom 1.95
            ease .7 yzoom 1.7
            pause .2
            ease .4 yzoom 2
            repeat
        parallel:
            ease .3 pos (-100,-115)
            ease .7 pos (-90,-155)
            pause .2
            ease .4 pos (-100,-105)
            repeat
    contains:

        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,110)
        transform_anchor True
        block:
            ease .3 ypos 100
            ease .7 ypos 60
            pause .2
            ease .4 ypos 110
            repeat
    contains:


        "Storm_TJ_HairTop"
        subpixel True
        pos (0,140)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos 70
            pause .1
            ease .5 ypos 140
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -5
            repeat






image Storm_TJ_4:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause .2
            ease 1.9 ypos -30
            pause .2
            ease 1.9 ypos 5
            repeat
    contains:

        "Storm_TJ_HairBack"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -20
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause .2
            ease 1.9 ypos -30
            pause .2
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
            pause .1
            ease 2 ypos 20
            pause .1
            repeat
    contains:
        contains:
            "Storm_TJ_BraStretch"
        subpixel True
        pos (-70,-210)
        transform_anchor True
        xzoom .75
        yzoom .5
        parallel:
            pause .2
            ease 1.9 pos (-65,-230)
            pause .2
            ease 1.9 pos (-75,-210)
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,5)
        transform_anchor True
        parallel:
            pause .2
            ease 1.9 ypos -30
            pause .2
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
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
        parallel:
            pause .1
            ease 2 rotate -5
            pause .1
            ease 2 rotate 0
            repeat




image Storm_TJ_5:

    contains:

        "Storm_TJ_Braback"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 100
            pause .2
            ease 2 ypos 110
            pause .4
            repeat
    contains:

        "Storm_TJ_HairBack"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause .2
            ease 2 ypos 130
            pause .5
            repeat
        parallel:
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Storm_TJ_Body"
        subpixel True
        pos (0,140)
        transform_anchor True
        parallel:
            ease 2 ypos 130
            pause .2
            ease 2 ypos 140
            pause .5
            repeat
    contains:

        "Storm_TJ_Head"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause .2
            ease 2 ypos 130
            pause .5
            repeat
        parallel:
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Storm_TJ_Tit_Under"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 100
            pause .2
            ease 2 ypos 110
            pause .4
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
            pause .1
            ease 2 yzoom 1.8
            pause .2
            ease 2 yzoom 2
            pause .4
            repeat
        parallel:
            pause .1
            ease 2 pos (-100,-115)
            pause .2
            ease 2 pos (-100,-105)
            pause .4
            repeat
    contains:
        contains:
            "Storm_TJ_Tits"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 100
            pause .2
            ease 2 ypos 110
            pause .4
            repeat
    contains:

        "Storm_TJ_HairTop"
        subpixel True
        pos (0,130)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 125
            pause .2
            ease 2 ypos 130
            pause .5
            repeat
        parallel:
            ease 2 rotate -5
            pause .5
            repeat







image Storm_At_Desk:
    contains:
        subpixel True
        "Storm_sprite standing"
        zoom 0.29
        pos (450,190)

image Storm_At_Podium:
    contains:
        subpixel True
        "Storm_sprite standing"
        zoom 0.29
        pos (670,180)

image Storm_Behind_Podium:
    contains:
        subpixel True
        "Storm_sprite standing"
        zoom 0.29
        pos (640,180)
        block:
            subpixel True
            ease .5 ypos 183
            ease .5 ypos 180
            pause .5
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
            ease .5 rotate -40 pos (55,310)
            pause .5
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
            ease .5 rotate -40 pos (185,330)
            pause .5
            ease 1.5 rotate 30 pos (205,350)
            repeat

image GropeThigh_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (145,630)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (145,700)
            ease 1 rotate 100 pos (145,630)
            repeat

image GropePussy_Storm:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (145,560)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (145,545)
                ease .75 rotate 170 pos (145,560)
            choice:
                ease .5 rotate 190 pos (145,545)
                pause .25
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
                pause .5
                ease 1 rotate 50 pos (165,640)
            choice:
                ease .5 rotate 40 pos (175,615)
                pause .5
                ease 1.75 rotate 50 pos (165,640)
            choice:
                ease 2 rotate 40 pos (175,615)
                pause .5
                ease 1 rotate 50 pos (165,640)
            choice:
                ease .25 rotate 40 pos (175,615)
                ease .25 rotate 50 pos (165,640)
                ease .25 rotate 40 pos (175,615)
                ease .25 rotate 50 pos (165,640)
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
            easeout .5 rotate -50 pos (165,575)
            linear .5 rotate -60 pos (155,585)
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
            ease .9 rotate 35 ypos 310
            pause .25
            ease .7 rotate 55 ypos 320
            pause .25
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
            pause .25
            ease .9 rotate 55 ypos 350
            pause .25
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
            pause .25
            ease 1 rotate 70 xpos 170
            pause .25
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
            pause .25
            ease 1 rotate 10 xpos 200
            pause .25
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
        zoom .6
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
        zoom .6
        anchor (0.5,0.5)
        pos (0,0)
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
    zoom .6
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
            ease .75 rotate 210 yoffset 465
            ease .5 rotate 195
            ease .75 rotate 210
            ease .5 rotate 195
        choice:
            ease .5 rotate 210 yoffset 465
            ease 1 rotate 195
            pause .25
            ease .5 rotate 210
            ease 1 rotate 195
            pause .25
        choice:
            ease .5 rotate 205 yoffset 465
            ease .75 rotate 200 yoffset 470
            ease .5 rotate 205 yoffset 465
            ease .75 rotate 200 yoffset 470
        choice:
            ease .3 rotate 205 yoffset 465
            ease .3 rotate 200 yoffset 475
            ease .3 rotate 205 yoffset 465
            ease .3 rotate 200 yoffset 475
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
                ease .75 rotate 210 pos (150,545)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (150,545)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (150,545)
                ease .75 rotate 200 pos (150,550)
                ease .5 rotate 205 pos (150,545)
                ease .75 rotate 200 pos (150,550)
            choice:
                ease .3 rotate 205 pos (150,545)
                ease .3 rotate 200 pos (150,555)
                ease .3 rotate 205 pos (150,545)
                ease .3 rotate 200 pos (150,555)
            repeat

image GirlFingerPussy_Storm:
    contains:
        subpixel True
        "images/UI_GirlFingerS.png"
        zoom .6
        pos (250,550)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (250,555)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (250,555)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 ypos 565
                ease .75 rotate 200 ypos 570
                ease .5 rotate 205 ypos 565
                ease .75 rotate 200 ypos 570
            choice:
                ease .3 rotate 205 ypos 565
                ease .3 rotate 200 ypos 575
                ease .3 rotate 205 ypos 565
                ease .3 rotate 200 ypos 575
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
