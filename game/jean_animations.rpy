

image Jean_Sprite:
    LiveComposite(
        (516,954),
        (160,0), "Jean_Sprite_HairBack",
        (0,0), ConditionSwitch(

            "JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Body2.png",
            "True", "images/JeanSprite/Jean_Sprite_Body1.png",
            ),




































        (0,0), ConditionSwitch(

            "JeanX.pubes", "images/JeanSprite/Jean_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.piercings", Null(),
            "JeanX.underwear and not JeanX.underwear_pulled_down", Null(),
            "JeanX.legs != 'skirt' and JeanX.legs and not JeanX.upskirt", Null(),
            "JeanX.piercings == 'barbell'", "images/JeanSprite/Jean_Sprite_Barbell_Pussy.png",
            "JeanX.piercings == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.hose == 'stockings'", "images/JeanSprite/Jean_Sprite_Hose_Stockings.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanSprite/Jean_Sprite_Hose_StockingsandGarter.png",
            "JeanX.hose == 'garterbelt'", "images/JeanSprite/Jean_Sprite_Hose_Garterbelt.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.Wet", Null(),
            "JeanX.legs and JeanX.Wet <= 1", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Wetness.png",
            ),
        (0,0), ConditionSwitch(

            "not JeanX.underwear", Null(),
            "JeanX.underwear_pulled_down", ConditionSwitch(

                    "not JeanX.legs or JeanX.upskirt or JeanX.legs == 'skirt'", ConditionSwitch(

                            "JeanX.underwear == 'green_panties' and JeanX.Wet", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png",
                            "JeanX.underwear == 'green_panties'", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png",
                            "JeanX.underwear == 'lace_panties'", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png",
                            "JeanX.underwear == 'bikini_bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini_Down.png",
                            "True", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png",
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "JeanX.Wet", ConditionSwitch(

                        "JeanX.underwear == 'green_panties'", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        "JeanX.underwear == 'lace_panties'", "images/JeanSprite/Jean_Sprite_Panties_Lace.png",
                        "JeanX.underwear == 'bikini_bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini.png",
                        "True", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        ),
                    "True", ConditionSwitch(

                        "JeanX.underwear == 'green_panties'", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        "JeanX.underwear == 'lace_panties'", "images/JeanSprite/Jean_Sprite_Panties_Lace.png",
                        "JeanX.underwear == 'bikini_bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini.png",
                        "True", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        ),
                    ),
            ),

        (0,0), ConditionSwitch(

            "JeanX.hose == 'pantyhose' and (not JeanX.underwear_pulled_down or not JeanX.underwear)", "images/JeanSprite/Jean_Sprite_Hose_Pantyhose.png",
            "JeanX.hose == 'ripped_pantyhose' and (not JeanX.underwear_pulled_down or not JeanX.underwear)", "images/JeanSprite/Jean_Sprite_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.legs", Null(),
            "JeanX.upskirt", ConditionSwitch(

                        "JeanX.legs == 'shorts'", "images/JeanSprite/Jean_Sprite_Legs_Shorts_Down.png",
                        "JeanX.legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants_Down.png",
                        "JeanX.legs == 'yoga_pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants_Down.png",
                        "JeanX.legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt_Up.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(

                    "JeanX.Wet", ConditionSwitch(

                        "JeanX.legs == 'shorts'", "images/JeanSprite/Jean_Sprite_Legs_Shorts.png",
                        "JeanX.legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants.png",
                        "JeanX.legs == 'yoga_pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants.png",
                        "JeanX.legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(

                        "JeanX.legs == 'shorts'", "images/JeanSprite/Jean_Sprite_Legs_Shorts.png",
                        "JeanX.legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants.png",
                        "JeanX.legs == 'yoga_pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants.png",
                        "JeanX.legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "JeanX.legs == 'skirt' or JeanX.legs == 'pants'", Null(),
            "JeanX.piercings == 'barbell'", ConditionSwitch(

                    "JeanX.legs and not JeanX.upskirt", "images/JeanSprite/Jean_Sprite_Barbell_PussyC.png",
                    "JeanX.underwear and not JeanX.underwear_pulled_down", "images/JeanSprite/Jean_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "JeanX.piercings == 'ring'", ConditionSwitch(

                    "JeanX.legs and not JeanX.upskirt", "images/JeanSprite/Jean_Sprite_Ring_PussyC.png",
                    "JeanX.underwear and not JeanX.underwear_pulled_down", "images/JeanSprite/Jean_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.legs and not JeanX.upskirt", Null(),
            "'in' in JeanX.spunk or 'anal' in JeanX.spunk", "images/JeanSprite/Jean_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.piercings or ((JeanX.top or JeanX.bra) and not JeanX.top_pulled_up)", Null(),
            "JeanX.piercings == 'barbell'", "images/JeanSprite/Jean_Sprite_Barbell_Tits.png",
            "JeanX.piercings == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_Tits.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_2LeftArm.png",
            "True", "images/JeanSprite/Jean_Sprite_1LeftArm.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1.png",
            "JeanX.Water", "images/JeanSprite/Jean_Sprite_Water2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "JeanX.top_pulled_up", ConditionSwitch(

                    "JeanX.bra == 'green_bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2_Up.png",
                    "JeanX.bra == 'green_bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1_Up.png",
                    "JeanX.bra == 'lace_bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2_Up.png",
                    "JeanX.bra == 'lace_bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1_Up.png",
                    "JeanX.bra == 'corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset_Up.png",
                    "JeanX.bra == 'sports_bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra2_Up.png",
                    "JeanX.bra == 'sports_bra'", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1_Up.png",
                    "JeanX.bra == 'bikini_top' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Bikini2_Up.png",
                    "JeanX.bra == 'bikini_top'", "images/JeanSprite/Jean_Sprite_Chest_Bikini1_Up.png",

                    "True", Null(),
                    ),
            "JeanX.bra == 'green_bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2.png",
            "JeanX.bra == 'green_bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1.png",
            "JeanX.bra == 'lace_bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_LaceBra2.png",
            "JeanX.bra == 'lace_bra'", "images/JeanSprite/Jean_Sprite_Chest_LaceBra1.png",
            "JeanX.bra == 'sports_bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra2.png",
            "JeanX.bra == 'sports_bra'", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1.png",
            "JeanX.bra == 'bikini_top' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Bikini2.png",
            "JeanX.bra == 'bikini_top'", "images/JeanSprite/Jean_Sprite_Chest_Bikini1.png",
            "JeanX.bra == 'corset' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Corset2.png",
            "JeanX.bra == 'corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset1.png",

            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "JeanX.top_pulled_up", ConditionSwitch(

                    "JeanX.top == 'yellow_shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_Tank2_Up.png",
                    "JeanX.top == 'yellow_shirt'", "images/JeanSprite/Jean_Sprite_Over_Tank1_Up.png",
                    "JeanX.top == 'pink_shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_PinkShirt2_Up.png",
                    "JeanX.top == 'pink_shirt'", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1_Up.png",
                    "JeanX.top == 'green_shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_GreenShirt2_Up.png",
                    "JeanX.top == 'green_shirt'", "images/JeanSprite/Jean_Sprite_Over_GreenShirt1_Up.png",

                    "True", Null(),
                    ),
            "JeanX.top == 'yellow_shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_Tank2.png",
            "JeanX.top == 'yellow_shirt'", "images/JeanSprite/Jean_Sprite_Over_Tank1.png",
            "JeanX.top == 'pink_shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_PinkShirt2.png",
            "JeanX.top == 'pink_shirt'", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1.png",
            "JeanX.top == 'green_shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_GreenShirt2.png",
            "JeanX.top == 'green_shirt'", "images/JeanSprite/Jean_Sprite_Over_GreenShirt1.png",
            "JeanX.top == 'towel' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_Towel2.png",
            "JeanX.top == 'towel'", "images/JeanSprite/Jean_Sprite_Over_Towel1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.piercings or (not JeanX.top and not JeanX.bra and not JeanX.top_pulled_up)", Null(),
            "JeanX.piercings == 'barbell'",  "images/JeanSprite/Jean_Sprite_Barbell_TitsC.png",
            "JeanX.piercings == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_TitsC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "'belly' in JeanX.spunk", "images/JeanSprite/Jean_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' in JeanX.spunk", "images/JeanSprite/Jean_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),






        (160,0), ConditionSwitch(


            "True", "Jean_Sprite_Head",
            ),

        (0,0), ConditionSwitch(

            "renpy.showing('Jean_HJ_Animation')", Null(),
            "JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_1LeftHand.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1Arm.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "renpy.showing('Jean_HJ_Animation')", Null(),
            "JeanX.bra == 'sports_bra' and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1_Arm.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "renpy.showing('Jean_HJ_Animation')", Null(),
            "JeanX.top == 'pink_shirt' and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1_Arm.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_2RightHand.png",
            "True", "images/JeanSprite/Jean_Sprite_1RightHand.png",

            ),
        (0,0), ConditionSwitch(

            "not JeanX.legs or JeanX.upskirt", Null(),
            "JeanX.ArmPose != 1 and JeanX.accessory == 'suspenders' and JeanX.top_pulled_up", "images/JeanSprite/Jean_Sprite_Acc_Suspenders2_Up.png",
            "JeanX.ArmPose != 1 and JeanX.accessory == 'suspenders'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders2.png",
            "JeanX.ArmPose != 1 and JeanX.accessory == 'suspenders2'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders2_Up.png",

            "JeanX.accessory == 'suspenders' and JeanX.top_pulled_up", "images/JeanSprite/Jean_Sprite_Acc_Suspenders1_Up.png",
            "JeanX.accessory == 'suspenders'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders1.png",
            "JeanX.accessory == 'suspenders2'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders1_Up.png",
            "True", Null(),
            ),













        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != JeanX", Null(),


            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_JeanSelf",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Jean",

                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeRightBreast_Jean",

                    "True", "GirlGropeBothBreast_Jean",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Jean",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Jean",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Jean",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Jean",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_offhand_action or second_girl_primary_action != 'masturbation' or focused_Girl == JeanX", Null(),


            "second_girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and JeanX.lust >= 70", "GirlFingerPussy_Jean",
            "second_girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Jean",
            "second_girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Jean",
            "second_girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(


            "not primary_action or focused_Girl != JeanX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Jean",
            "primary_action == 'fondle_thighs'", "GropeThigh_Jean",
            "primary_action == 'fondle_breasts'", "GropeLeftBreast_Jean",
            "primary_action == 'suck breasts'", "LickRightBreast_Jean",
            "primary_action == 'fondle_pussy' and action_speed == 2", "FingerPussy_Jean",
            "primary_action == 'fondle_pussy'", "GropePussy_Jean",
            "primary_action == 'eat_pussy'", "Lickpussy_Jean",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Jean",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "primary_action == 'vibrator anal'", "VibratorAnal_Jean",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Jean",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not offhand_action or focused_Girl != JeanX", Null(),


            "offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' and primary_action == 'suck breasts'", "GropeLeftBreast_Jean",

                    "True", "GropeRightBreast_Jean",

                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast_Jean",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck breasts'", "LickLeftBreast_Jean",
            "offhand_action == 'fondle_pussy'", "GropePussy_Jean",
            "offhand_action == 'eat_pussy'", "Lickpussy_Jean",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Jean",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Jean",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Jean",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Jean",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_primary_action or focused_Girl != JeanX", Null(),


            "second_girl_primary_action == 'fondle_pussy' and primary_action != 'sex' and JeanX.lust >= 70", "GirlFingerPussy_Jean",
            "second_girl_primary_action == 'fondle_pussy'", "GirlGropePussy_Jean",
            "second_girl_primary_action == 'eat_pussy'", "Lickpussy_Jean",
            "second_girl_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Jean",
            "second_girl_primary_action == 'suck breasts'", "LickRightBreast_Jean",
            "second_girl_primary_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Jean",


                    "True", "GirlGropeRightBreast_Jean",
                    ),
            "second_girl_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_primary_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action != 'lesbian' or focused_Girl == JeanX or not girl_offhand_action", Null(),


            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and JeanX.lust >= 70", "GirlFingerPussy_Jean",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Jean",
            "girl_offhand_action == 'eat_pussy'", "Lickpussy_Jean",
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Jean",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast_Jean",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Jean",

                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeRightBreast_Jean",

                    "girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Jean",

                    "True", "GirlGropeRightBreast_Jean",

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
    zoom .75

image Jean_Sprite_HairBack:
    ConditionSwitch(

            "not JeanX.hair", Null(),
            "renpy.showing('Jean_BJ_Animation')", Null(),

            "JeanX.hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Under.png",
            "JeanX.hair == 'pony'", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Hair_Short_Under.png",
            ),

    anchor (0.6, 0.0)
    zoom .32

image Jean_Sprite_HairMid:
    ConditionSwitch(

            "not JeanX.hair", Null(),
            "renpy.showing('Jean_BJ_Animation')", Null(),

            "JeanX.hair == 'wet' JeanX.hair == 'pony' or JeanX.Water", Null(),
            "True","images/JeanSprite/Jean_Sprite_Hair_Short_Mid.png",
            ),
    anchor (0.6, 0.0)
    zoom .5

image Jean_Sprite_HairTop:
    ConditionSwitch(

            "not JeanX.hair", Null(),

            "JeanX.hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Over.png",
            "JeanX.hair == 'pony'", "images/JeanSprite/Jean_Sprite_Hair_Pony_Over.png",
            "True", "images/JeanSprite/Jean_Sprite_Hair_Short_Over.png",
            ),

    anchor (0.6, 0.0)
    zoom .5

image Jean_Sprite_Head:
    LiveComposite(
        (900,900),





        (0,0), ConditionSwitch(

                "JeanX.blushing >= 2", "images/JeanSprite/Jean_Sprite_Head_Blush2.png",
                "JeanX.blushing", "images/JeanSprite/Jean_Sprite_Head_Blush.png",
                "True", "images/JeanSprite/Jean_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "'chin' not in JeanX.spunk", Null(),
            "renpy.showing('Jean_BJ_Animation') and action_speed >= 2", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Spunk_Chin.png",
            ),














        (0,0), ConditionSwitch(
            "'mouth' in JeanX.spunk", ConditionSwitch(
                    "JeanX.mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal_Spunk.png",
                    "JeanX.mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite_Spunk.png",
                    "JeanX.mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue_Spunk.png",
                    "JeanX.mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss_Spunk.png",
                    "JeanX.mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad_Spunk.png",
                    "JeanX.mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile_Spunk.png",
                    "JeanX.mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised_Spunk.png",
                    "JeanX.mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue_Spunk.png",
                    "JeanX.mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile_Spunk.png",
                    "JeanX.mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk_Spunk.png",
                    "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal_Spunk.png",
                    ),
            "True", ConditionSwitch(
                    "JeanX.mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
                    "JeanX.mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite.png",
                    "JeanX.mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",
                    "JeanX.mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss.png",
                    "JeanX.mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad.png",
                    "JeanX.mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
                    "JeanX.mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised.png",
                    "JeanX.mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",
                    "JeanX.mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
                    "JeanX.mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk.png",
                    "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
                    ),
            ),
        (0,0), ConditionSwitch(

            "JeanX.blushing >= 2", ConditionSwitch(
                    "JeanX.brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal2.png",
                    "JeanX.brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry2.png",
                    "JeanX.brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad2.png",
                    "JeanX.brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",
                    "JeanX.brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused2.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal2.png",
                    ),
            "JeanX.blushing", ConditionSwitch(
                    "JeanX.brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal1.png",
                    "JeanX.brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry1.png",
                    "JeanX.brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad1.png",
                    "JeanX.brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",
                    "JeanX.brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused1.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal1.png",
                    ),
            "True", ConditionSwitch(
                    "JeanX.brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    "JeanX.brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry.png",
                    "JeanX.brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad.png",
                    "JeanX.brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",
                    "JeanX.brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Jean Blink",





        (0,0), ConditionSwitch(

            "not JeanX.hair", Null(),
            "renpy.showing('Jean_TJ_Animation')", Null(),

            "JeanX.hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Over.png",
            "JeanX.hair == 'pony'", "images/JeanSprite/Jean_Sprite_Hair_Pony_Over.png",
            "JeanX.hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.Water", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Head_Wet.png",

            ),
        (0,0), ConditionSwitch(

            "'hair' in JeanX.spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial2.png",
            "'facial' in JeanX.spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)

    zoom .32

image Jean Blink:
    ConditionSwitch(
    "JeanX.eyes == 'sexy'", "images/JeanSprite/Jean_Sprite_Eyes_Sexy.png",
    "JeanX.eyes == 'side'", "images/JeanSprite/Jean_Sprite_Eyes_Side.png",
    "JeanX.eyes == 'surprised'", "images/JeanSprite/Jean_Sprite_Eyes_Surprised.png",
    "JeanX.eyes == 'normal'", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png",
    "JeanX.eyes == 'stunned'", "images/JeanSprite/Jean_Sprite_Eyes_Stunned.png",
    "JeanX.eyes == 'down'", "images/JeanSprite/Jean_Sprite_Eyes_Down.png",
    "JeanX.eyes == 'closed'", "images/JeanSprite/Jean_Sprite_Eyes_Closed.png",
    "JeanX.eyes == 'leftside'", "images/JeanSprite/Jean_Sprite_Eyes_Leftside.png",
    "JeanX.eyes == 'manic'", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png",
    "JeanX.eyes == 'psychic'", "images/JeanSprite/Jean_Sprite_Eyes_Psychic.png",
    "JeanX.eyes == 'squint'", "Jean_Squint",
    "True", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JeanSprite/Jean_Sprite_Eyes_Closed.png"
    .25
    repeat

image Jean_Squint:
    "images/JeanSprite/Jean_Sprite_Eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JeanSprite/Jean_Sprite_Eyes_Sexy.png"
    .25
    repeat



image Jean_Drip_Mask:

    contains:
        "images/JeanSprite/Jean_Sprite_WetMask.png"
        offset (-145,-560)

image Jean_Drip_MaskP:

    contains:
        "images/JeanSprite/Jean_Sprite_WetMaskP.png"
        offset (-145,-560)











image Jean_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Jean_Doggy_Body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jean_Doggy_Fuck_Top",
                    "action_speed ", "Jean_Doggy_Anal_Head_Top",
                    "True", "Jean_Doggy_Body",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jean_Doggy_Fuck_Top",
                    "True", "Jean_Doggy_Body",
                    ),
            "True", "Jean_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Jean_Doggy_Ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jean_Doggy_Fuck_Ass",
                    "action_speed ", "Jean_Doggy_Anal_Head_Ass",
                    "True", "Jean_Doggy_Ass",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jean_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jean_Doggy_Fuck_Ass",
                    "True", "Jean_Doggy_Ass",
                    ),
            "True", "Jean_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.cock_position == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Jean_Doggy_Feet2",
                    "action_speed ", "Jean_Doggy_Feet1",
                    "True", "Jean_Doggy_Feet0",
                    ),
            "not Player.sprite and ShowFeet", "Jean_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    yoffset 50


image Jean_Doggy_Body:
    LiveComposite(

        (420,750),
        (165,0),"Jean_Doggy_Hair_Under",
        (0,0), ConditionSwitch(

            "JeanX.bra == 'corset' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Chest_Corset_Back.png",
            "True", Null(),
            ),
        (165,0), "Jean_Doggy_Head",

        (0,0), "images/JeanDoggy/Jean_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "not JeanX.bra", Null(),
            "JeanX.top_pulled_up", ConditionSwitch(
                    "JeanX.bra == 'lace_bra' and JeanX.top", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up2.png",
                    "JeanX.bra == 'lace_bra'", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up.png",
                    "JeanX.bra == 'corset'", "images/JeanDoggy/Jean_Doggy_Chest_Corset_Up.png",
                    "JeanX.bra == 'sports_bra'", "images/JeanDoggy/Jean_Doggy_Chest_SportsBra_Up.png",
                    "JeanX.bra == 'bikini_top'", "images/JeanDoggy/Jean_Doggy_Chest_Bikini_Up.png",
                    "JeanX.top", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up2.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up.png",
                    ),
            "JeanX.bra == 'lace_bra'", "images/JeanDoggy/Jean_Doggy_Chest_LaceBra.png",
            "JeanX.bra == 'corset'", "images/JeanDoggy/Jean_Doggy_Chest_Corset.png",
            "JeanX.bra == 'sports_bra'", "images/JeanDoggy/Jean_Doggy_Chest_SportsBra.png",
            "JeanX.bra == 'bikini_top'", "images/JeanDoggy/Jean_Doggy_Chest_Bikini.png",
            "True", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra.png",
            ),





        (0,0), ConditionSwitch(

            "not JeanX.top", Null(),
            "JeanX.top == 'yellow_shirt' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_Tank_Up.png",
            "JeanX.top == 'yellow_shirt'", "images/JeanDoggy/Jean_Doggy_Over_Tank.png",
            "JeanX.top == 'green_shirt' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_GreenShirt_Up.png",
            "JeanX.top == 'green_shirt'", "images/JeanDoggy/Jean_Doggy_Over_GreenShirt.png",
            "JeanX.top == 'pink_shirt' and JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_PinkShirt_Up.png",
            "JeanX.top == 'pink_shirt'", "images/JeanDoggy/Jean_Doggy_Over_PinkShirt.png",
            "JeanX.top == 'towel' and not JeanX.top_pulled_up", "images/JeanDoggy/Jean_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.legs or JeanX.upskirt", Null(),
            "JeanX.accessory == 'suspenders' or JeanX.accessory == 'suspenders2'", "images/JeanDoggy/Jean_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in JeanX.spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Jean_Doggy_GropeBreast",
            "True", Null()
            ),

        (165,0),"Jean_Doggy_Hair_Over",
        (0,0), "images/JeanDoggy/Jean_Doggy_Hand.png",
        )


    offset (-190,-40)




image Jean_Doggy_Head:
    LiveComposite(

        (420,750),


        (0,0), ConditionSwitch(

            "JeanX.blushing > 1", "images/JeanDoggy/Jean_Doggy_Head_Blush2.png",
            "JeanX.blushing", "images/JeanDoggy/Jean_Doggy_Head_Blush1.png",
            "True", "images/JeanDoggy/Jean_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "JeanX.mouth == 'normal'", "images/JeanDoggy/Jean_Doggy_Mouth_Normal.png",
            "JeanX.mouth == 'lipbite'", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            "JeanX.mouth == 'sucking'", "images/JeanDoggy/Jean_Doggy_Mouth_Tongue.png",
            "JeanX.mouth == 'kiss'", "images/JeanDoggy/Jean_Doggy_Mouth_Normal.png",
            "JeanX.mouth == 'sad'", "images/JeanDoggy/Jean_Doggy_Mouth_Sad.png",
            "JeanX.mouth == 'smile'", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            "JeanX.mouth == 'grimace'", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            "JeanX.mouth == 'surprised'", "images/JeanDoggy/Jean_Doggy_Mouth_Open.png",
            "JeanX.mouth == 'tongue'", "images/JeanDoggy/Jean_Doggy_Mouth_Tongue.png",
            "True", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(

            "'chin' in JeanX.spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'mouth' not in JeanX.spunk", Null(),


            "JeanX.mouth == 'lipbite'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.mouth == 'smile'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.mouth == 'grimace'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.mouth == 'sucking'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",

            "JeanX.mouth == 'surprised'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            "JeanX.mouth == 'tongue'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            "True", "images/JeanDoggy/Jean_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(


            "JeanX.brows == 'angry'", "images/JeanDoggy/Jean_Doggy_Brows_Angry.png",
            "JeanX.brows == 'sad'", "images/JeanDoggy/Jean_Doggy_Brows_Sad.png",
            "JeanX.brows == 'surprised'", "images/JeanDoggy/Jean_Doggy_Brows_Surprised.png",

            "True", "images/JeanDoggy/Jean_Doggy_Brows_Normal.png",
            ),
        (0,0), "Jean Doggy Blink",
        (0,0), ConditionSwitch(

            "JeanX.Water or JeanX.hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
            "True", Null(),
            ),




















        )
    zoom 0.9


image Jean_Doggy_Hair_Under:

    ConditionSwitch(
                "JeanX.Water or JeanX.hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
                "JeanX.hair == 'pony'", Null(),
                "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Under.png",
                )
    zoom .9

image Jean_Doggy_Hair_Over:

    contains:
        ConditionSwitch(
                    "JeanX.Water or JeanX.hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Over.png",
                    "JeanX.hair == 'pony'", "images/JeanDoggy/Jean_Doggy_Hair_Pony_Over.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Over.png",
                    )
    contains:
        ConditionSwitch(

                "'facial' in JeanX.spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Facial.png",
                "True", Null(),
                )
    contains:
        ConditionSwitch(

                "'hair' in JeanX.spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Facial2.png",
                "True", Null(),
                )
    zoom .9


image Jean Doggy Blink:

    ConditionSwitch(
        "JeanX.eyes == 'sexy'", "images/JeanDoggy/Jean_Doggy_Eyes_Sexy.png",
        "JeanX.eyes == 'side'", "images/JeanDoggy/Jean_Doggy_Eyes_Normal.png",
        "JeanX.eyes == 'normal'", "images/JeanDoggy/Jean_Doggy_Eyes_Normal.png",
        "JeanX.eyes == 'closed'", "images/JeanDoggy/Jean_Doggy_Eyes_Closed.png",
        "JeanX.eyes == 'manic'", "images/JeanDoggy/Jean_Doggy_Eyes_Surprised.png",
        "JeanX.eyes == 'down'", "images/JeanDoggy/Jean_Doggy_Eyes_Sexy.png",
        "JeanX.eyes == 'stunned'", "images/JeanDoggy/Jean_Doggy_Eyes_Stunned.png",
        "JeanX.eyes == 'surprised'", "images/JeanDoggy/Jean_Doggy_Eyes_Surprised.png",
        "JeanX.eyes == 'squint'", "images/JeanDoggy/Jean_Doggy_Eyes_Sexy.png",
        "True", "images/JeanDoggy/Jean_Doggy_Eyes_Normal.png",
        ),






    3

    "images/JeanDoggy/Jean_Doggy_Eyes_Closed.png"
    .25
    repeat

image Jean_Doggy_Ass:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "JeanX.legs == 'skirt'","images/JeanDoggy/Jean_Doggy_Legs_Skirt_Back.png",
            "not JeanX.upskirt", Null(),
            "JeanX.legs == 'shorts'", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Back.png",
            "JeanX.legs == 'pants'", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Back.png",
            "JeanX.legs == 'yoga_pants'", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.underwear_pulled_down or (JeanX.legs == 'pants' and not JeanX.upskirt)", Null(),
            "JeanX.underwear == 'green_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green_Back.png",
            "JeanX.underwear == 'bikini_bottoms'", Null(),
            "JeanX.underwear", "images/JeanDoggy/Jean_Doggy_Panties_Green_Back.png",
            "True", Null(),
            ),
        (0,0), "images/JeanDoggy/Jean_Doggy_Ass.png",
        (0,0), ConditionSwitch(

            "JeanX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.hose == 'stockings'", "images/JeanDoggy/Jean_Doggy_Hose_Stocking.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.underwear_pulled_down or (JeanX.legs == 'pants' and not JeanX.upskirt)", Null(),
            "JeanX.underwear == 'green_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green_Down.png",
            "JeanX.underwear == 'bikini_bottoms'", Null(),
            "JeanX.underwear", "images/JeanDoggy/Jean_Doggy_Panties_Green_Down.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jean_Pussy_Fucking3",
                    "action_speed > 1", "Jean_Pussy_Fucking2",
                    "action_speed ", "Jean_Pussy_Heading",
                    "True", "Jean_Pussy_Static",
                    ),
            "primary_action == 'eat_pussy'", "images/JeanDoggy/Jean_Doggy_Pussy_Open.png",
            "JeanX.legs and not JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            "JeanX.underwear and not JeanX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Jean_Pussy_Fingering",
            "primary_action == 'dildo_pussy'", "Jean_Pussy_Fucking2",
            "True", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            ),


        (0,0), ConditionSwitch(

            "'in' in JeanX.spunk and Player.cock_position == 'in'",Null(),
            "'in' in JeanX.spunk ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "JeanX.Wet and Player.cock_position == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "JeanX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JeanX.pubes", Null(),
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "JeanX.legs == 'pants' and not JeanX.upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "JeanX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/JeanDoggy/Jean_Doggy_Pubes_Open.png",
            "JeanX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Pubes.png",
            "JeanX.underwear", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "JeanX.hose and JeanX.hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "primary_action == 'eat_pussy'", "images/JeanDoggy/Jean_Doggy_Pubes_Open.png",
            "True", "images/JeanDoggy/Jean_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "JeanX.piercings == 'ring'", "images/JeanDoggy/Jean_Doggy_PussyRing.png",
            "JeanX.piercings == 'barbell'", "images/JeanDoggy/Jean_Doggy_PussyBarbell.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jean_Anal_Fucking2",
                    "action_speed > 1", "Jean_Anal_Fucking",
                    "action_speed ", "Jean_Anal_Heading",
                    "True", "Jean_Anal",
                    ),


            "JeanX.legs and not JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "JeanX.underwear and not JeanX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Jean_Anal_Fingering",
            "primary_action == 'dildo_anal'", "Jean_Anal_Fucking",
            "JeanX.used_to_anal", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(

            "'anal' not in JeanX.spunk or Player.sprite", Null(),
            "Player.cock_position == 'anal'", "images/JeanDoggy/Jean_Doggy_SpunkAnalOpen.png",
            "JeanX.used_to_anal", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(

            "JeanX.underwear_pulled_down or not JeanX.underwear", Null(),
            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),


            "JeanX.underwear == 'green_panties' and JeanX.Wet", "images/JeanDoggy/Jean_Doggy_Panties_Green_Wet.png",
            "JeanX.underwear == 'green_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green.png",
            "JeanX.underwear == 'lace_panties'", "images/JeanDoggy/Jean_Doggy_Panties_Lace.png",
            "JeanX.underwear == 'bikini_bottoms' and JeanX.Wet", "images/JeanDoggy/Jean_Doggy_Panties_Bikini_Wet.png",
            "JeanX.underwear == 'bikini_bottoms'", "images/JeanDoggy/Jean_Doggy_Panties_Bikini.png",
            "True", "images/JeanDoggy/Jean_Doggy_Panties_Green.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),


            "JeanX.hose == 'pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full.png",
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.legs == 'pants'", ConditionSwitch(
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Down.png",
                    "JeanX.Wet > 1", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Pants.png",
                    ),
            "JeanX.legs == 'yoga_pants'", ConditionSwitch(
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Down.png",
                    "JeanX.Wet > 1", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Yoga.png",
                    ),
            "JeanX.legs == 'shorts'", ConditionSwitch(
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Down.png",
                    "JeanX.Wet > 1", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Shorts.png",
                    ),
            "JeanX.legs == 'skirt'", ConditionSwitch(
                    "JeanX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/JeanDoggy/Jean_Doggy_Legs_Skirt_Up.png",
                    "JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Skirt_Up.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JeanX.top == 'towel' and JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Over_TowelAss_Up.png",
            "JeanX.top == 'towel'", "images/JeanDoggy/Jean_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in JeanX.spunk", "images/JeanDoggy/Jean_Doggy_SpunkAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Rogue_Doggy_Lick_Pussy",
            "primary_action == 'eat_ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),
            "JeanX.legs == 'skirt' and JeanX.upskirt", "images/JeanDoggy/Jean_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/JeanDoggy/Jean_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),


            "action_speed ", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Jean_Doggy_Feet:
    contains:
        AlphaMask("Jean_Doggy_Shins", "images/JeanDoggy/Jean_Doggy_Feet_Toes.png")

image Jean_Doggy_Shins:



    contains:

        ConditionSwitch(
            "JeanX.hose == 'stockings'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.hose == 'pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack_Holed.png",
            "True", "images/JeanDoggy/Jean_Doggy_Feet_Legs.png"
            )
    contains:


        ConditionSwitch(
            "JeanX.legs == 'pants'", "images/JeanDoggy/Jean_Doggy_Feet_Pants.png",
            "JeanX.legs == 'yoga_pants'", "images/JeanDoggy/Jean_Doggy_Feet_Yoga.png",
            "True", Null(),
            )
























image Jean_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (280,380)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat

















image Zero_Jean_Hotdog_Static:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Jean_Hotdog_Moving:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Jean_Doggy_Static:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Jean_Doggy_Heading:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Jean_Doggy_Fucking2:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jean_Doggy_Fucking3:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Jean_Pussy_Mask:


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

image Jean_Pussy_Mask_Static:


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


































image Jean_Pussy_Static:

    subpixel True
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
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

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Static", "Jean_Pussy_Mask_Static")
    contains:


        AlphaMask("Jean_PussyHole_Static", "Jean_Pussy_Hole_Mask_Static")

image Jean_Pussy_Hole_Mask_Static:

    contains:

        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Jean_PussyHole_Static:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Jean_Pussy_Heading:

    subpixel True
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
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

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Heading", "Jean_Pussy_Mask")
    contains:


        AlphaMask("Jean_Pussy_Heading_Flap", "Jean_Pussy_Hole_Mask")


image Jean_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Jean_Pussy_Heading_Flap:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Jean_Pussy_Fingering:

    subpixel True
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
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

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
    contains:


        AlphaMask("Jean_Pussy_Heading_Flap", "Jean_Pussy_Hole_Mask")



image Jean_Pussy_Fucking2:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:


        ConditionSwitch(
            "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Jean_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),


image Jean_Pussy_Fucking3:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")





image Jean_Anal:

    contains:

        "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        "Zero_Doggy_Insert"
        pos (172,500)




image Jean_Anal_Fingering:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
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

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")


image Jean_Anal_Heading:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
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

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Anal_Heading", "Zero_Jean_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Jean_Doggy_Anal_Heading", "Jean_Doggy_Anal_Heading_Mask")

image Zero_Jean_Doggy_Anal_Heading:

    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jean_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600
            repeat

image Jean_Doggy_Anal_Heading_Mask:

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

image Jean_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Jean_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Jean_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Jean_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat


image Zero_Jean_Doggy_Anal1:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Jean_Anal_Fucking:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:


        ConditionSwitch(

            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Jean_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),

image Jean_Doggy_Anal_FullMask:
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )

image Jean_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Jean_Doggy_Body"
        ypos 15
        pause .4
        block:
            ease .2 ypos 5
            pause .3
            ease 2 ypos 15
            repeat

image Jean_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Jean_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15
            ease .1 ypos -5
            pause .2
            ease 1.6 ypos 0
            repeat



image Zero_Jean_Doggy_Anal2:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Jean_Anal_Fucking2:

    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:

        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
    contains:




        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "JeanX.hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.underwear and JeanX.underwear_pulled_down", Null(),
            "JeanX.hose == 'ripped_pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jean_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Jean_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Jean_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Jean_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Jean_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




image Jean_Doggy_Feet0:

    contains:
        "Jean_Doggy_Shins"
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
                "Player.sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (160,480)
    contains:
        "Jean_Doggy_Feet"
        pos (0, 0)
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Jean_Doggy_Feet1:

    contains:
        "Jean_Doggy_Shins"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Jean_Doggy_Feet"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Jean_Doggy_Feet2:

    contains:
        "Jean_Doggy_Shins"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (160,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Jean_Doggy_Feet"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat




label Jean_Doggy_Launch(Line=primary_action):
    if renpy.showing("Jean_Doggy_Animation"):
        return
    $ action_speed = 0
    call Jean_Hide (1)
    show Jean_Doggy_Animation zorder 150 at sprite_location(stage_center+50)
    with dissolve
    return

label Jean_Doggy_Reset:
    if not renpy.showing("Jean_Doggy_Animation"):
        return

    $ JeanX.ArmPose = 2
    $ JeanX.spriteVer = 0
    hide Jean_Doggy_Animation
    call Jean_Hide
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return








image Jean_SexSprite:
    LiveComposite(
        (1000,1000),
        (0,0), ConditionSwitch(

                "primary_action == 'eat_pussy'", "Jean_Sex_Lick",
                "not Player.sprite", "Jean_Sex_Static",
                "Player.cock_position == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Jean_Sex_Fucking_Speed3",
                        "action_speed >= 2", "Jean_Sex_Fucking_Speed2",
                        "action_speed ", "Jean_Sex_Fucking_Speed1",
                        "True", "Jean_Sex_Fucking_Speed0",
                        ),
                "Player.cock_position == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Jean_Sex_Anal_Speed3",
                        "action_speed >= 2", "Jean_Sex_Anal_Speed2",
                        "action_speed ", "Jean_Sex_Anal_Speed1",
                        "True", "Jean_Sex_Anal_Speed0",
                        ),
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 2","Jean_Sex_Hotdog_Speed2",
                "Player.sprite and Player.cock_position == 'out' and action_speed >= 1","Jean_Sex_Hotdog_Speed1",







                "True", "Jean_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (750,230)
    zoom 0.8

image Jean_Sex_HairBack:

    "Jean_BJ_HairBack"
    zoom 0.5
    anchor (0.5, 0.5)
    rotate 20
    pos (490,320)

image Jean_Sex_Head:

    "Jean_BJ_Head"
    zoom 0.5
    anchor (0.5, 0.5)
    rotate 20
    pos (490,320)





image Jean_Sex_Torso:

    contains:

        ConditionSwitch(
            "JeanX.bra == 'corset'", "images/JeanSex/Jean_Sex_Over_Back.png",
            "JeanX.top == 'pink_shirt'", "images/JeanSex/Jean_Sex_Over_Back.png",
            "JeanX.top_pulled_up", Null(),
            "JeanX.bra == 'bikini_top' and not JeanX.top", Null(),
            "not JeanX.bra and not JeanX.top", Null(),
            "True", "images/JeanSex/Jean_Sex_Over_Back.png",
            )
    contains:

        "images/JeanSex/Jean_Sex_Body.png"
    contains:

















        ConditionSwitch(
            "JeanX.top_pulled_up", ConditionSwitch(

                    "JeanX.bra == 'sports_bra'", "images/JeanSex/Jean_Sex_Bra_Sports_Up.png",
                    "JeanX.bra == 'bikini_top'", "images/JeanSex/Jean_Sex_Bra_Bikini_Up.png",
                    "JeanX.bra == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Up.png",
                    "JeanX.bra == 'lace_bra'", "images/JeanSex/Jean_Sex_Bra_Green_Up.png",
                    "JeanX.bra", "images/JeanSex/Jean_Sex_Bra_Green_Up.png",
                    "True", Null(),
                    ),
            "JeanX.bra == 'sports_bra'", "images/JeanSex/Jean_Sex_Bra_Sports.png",
            "JeanX.bra == 'bikini_top'", "images/JeanSex/Jean_Sex_Bra_Bikini.png",
            "JeanX.bra == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset.png",
            "JeanX.bra == 'lace_bra'", "images/JeanSex/Jean_Sex_Bra_Lace.png",
            "JeanX.bra", "images/JeanSex/Jean_Sex_Bra_Green.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.top_pulled_up", ConditionSwitch(

                    "JeanX.top == 'green_shirt'", "images/JeanSex/Jean_Sex_Over_Green_Up.png",
                    "JeanX.top == 'pink_shirt'", "images/JeanSex/Jean_Sex_Over_Pink_Up.png",
                    "JeanX.top == 'yellow_shirt'", "images/JeanSex/Jean_Sex_Over_Yellow_Up.png",
                    "True", Null(),
                    ),
            "JeanX.top == 'green_shirt'", "images/JeanSex/Jean_Sex_Over_Green.png",
            "JeanX.top == 'pink_shirt'", "images/JeanSex/Jean_Sex_Over_Pink.png",
            "JeanX.top == 'yellow_shirt'", "images/JeanSex/Jean_Sex_Over_Yellow.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "JeanX.piercings == 'barbell'", ConditionSwitch(

                    "JeanX.top_pulled_up or (not JeanX.bra and not JeanX.top)", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell.png",
                    "JeanX.top == 'green_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Green.png",
                    "JeanX.top == 'pink_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Pink.png",
                    "JeanX.top == 'yellow_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Yellow.png",
                    "JeanX.bra == 'sports_bra'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bikini.png",
                    "JeanX.bra == 'bikini_top'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bikini.png",
                    "JeanX.bra == 'corset'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Corset.png",
                    "JeanX.bra", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bra.png",
                    "True", Null(),
                    ),
            "JeanX.piercings == 'ring'", ConditionSwitch(

                    "JeanX.top_pulled_up or (not JeanX.bra and not JeanX.top)", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Loose.png",
                    "JeanX.top == 'green_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Green.png",
                    "JeanX.top == 'pink_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Pink.png",
                    "JeanX.top == 'yellow_shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Yellow.png",
                    "JeanX.bra == 'sports_bra'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bikini.png",
                    "JeanX.bra == 'bikini_top'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bikini.png",
                    "JeanX.bra == 'corset'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Corset.png",
                    "JeanX.bra", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bra.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(
                "'tits' not in JeanX.spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Tits.png",
                )
    contains:
        ConditionSwitch(


            "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Jean_Sex_Lick_Breasts",
            "True", Null()
            )
    contains:
        ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Jean_Sex_Fondle_Breasts",
            "True", Null()
            )
    zoom 1

image Jean_Sex_Lick_Breasts:
    "Lick_Anim"
    zoom 0.7
    offset (390,600)

image Jean_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.5
    offset (120,-40)

image Jean_Sex_Body:

    contains:
        "Jean_Sex_HairBack"
    contains:






        AlphaMask("Jean_Sex_Torso", "images/JeanSex/Jean_Sex_ArmsMask.png")
    contains:





















        "Jean_Sex_Head"
    zoom 1.1
    offset (-40,-50)











































image Jean_Sex_Legs_S:

    contains:

        "images/JeanSex/Jean_Sex_Legs_Sex.png"
    contains:

        ConditionSwitch(
            "JeanX.Wet", "images/JeanSex/Jean_Sex_Wet_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'anal' in JeanX.spunk or 'in' in JeanX.spunk", "images/JeanSex/Jean_Sex_Spunk_Pussy_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.hose == 'stockings'", "images/JeanSex/Jean_Sex_Hose_Stockings.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanSex/Jean_Sex_Hose_StockingsGarter_S.png",
            "JeanX.hose == 'garterbelt'", "images/JeanSex/Jean_Sex_Hose_Garter_S.png",
            "True", Null(),
            )
    contains:











        ConditionSwitch(
            "JeanX.pubes", "images/JeanSex/Jean_Sex_Pubes_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "JeanX.legs and not JeanX.upskirt and JeanX.piercings == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",
            "JeanX.underwear and not JeanX.underwear_pulled_down and JeanX.piercings == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",
            "JeanX.hose == 'pantyhose' and not JeanX.underwear_pulled_down and JeanX.piercings == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",

            "JeanX.piercings == 'barbell'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Sex.png",
            "JeanX.piercings == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.bra == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Under_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.top == 'green_shirt' and not JeanX.top_pulled_up", "images/JeanSex/Jean_Sex_Over_Green_Under_S.png",
            "JeanX.top == 'pink_shirt'", "images/JeanSex/Jean_Sex_Over_Pink_Under_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.underwear_pulled_down", Null(),
            "JeanX.underwear == 'lace_panties'", "images/JeanSex/Jean_Sex_Panties_Sex_Lace.png",
            "JeanX.underwear == 'bikini_bottoms'", "images/JeanSex/Jean_Sex_Panties_Sex_Bikini.png",
            "JeanX.underwear and JeanX.Wet", "images/JeanSex/Jean_Sex_Panties_Sex_Green_W.png",
            "JeanX.underwear", "images/JeanSex/Jean_Sex_Panties_Sex_Green.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.underwear_pulled_down", Null(),


            "JeanX.hose == 'pantyhose'", "images/JeanSex/Jean_Sex_Hose_Pantyhose_S.png",
            "True", Null(),
            )
    contains:










        ConditionSwitch(
            "JeanX.legs == 'skirt' and JeanX.upskirt", "images/JeanSex/Jean_Sex_Legs_Sex_Skirt_Up.png",
            "JeanX.legs == 'skirt'", "images/JeanSex/Jean_Sex_Legs_Sex_Skirt.png",
            "JeanX.upskirt", Null(),
            "JeanX.legs == 'pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Pants_W.png",
            "JeanX.legs == 'pants'", "images/JeanSex/Jean_Sex_Legs_Sex_Pants.png",
            "JeanX.legs == 'shorts' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Shorts_W.png",
            "JeanX.legs == 'shorts'", "images/JeanSex/Jean_Sex_Legs_Sex_Shorts.png",
            "JeanX.legs == 'yoga_pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Yoga_W.png",
            "JeanX.legs == 'yoga_pants'", "images/JeanSex/Jean_Sex_Legs_Sex_Yoga.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'belly' in JeanX.spunk", "images/JeanSex/Jean_Sex_Spunk_Belly_S.png",
            "True", Null(),
            )
    zoom 1


image Jean_Sex_Legs_A:

    contains:

        ConditionSwitch(
            "primary_action == 'eat_pussy'", "images/JeanSex/Jean_Sex_Legs_Lick.png",
            "True", "images/JeanSex/Jean_Sex_Legs_Anal.png",
            )
    contains:

        ConditionSwitch(
            "JeanX.Wet", "images/JeanSex/Jean_Sex_Wet_Lick.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'anal' in JeanX.spunk and not action_speed", "images/JeanSex/Jean_Sex_Spunk_Pussy_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not JeanX.pubes", Null(),
            "primary_action == 'eat_pussy'", "images/JeanSex/Jean_Sex_Pubes_Lick.png",
            "True", "images/JeanSex/Jean_Sex_Pubes_Anal.png",
            )
    contains:

        ConditionSwitch(
            "JeanX.bra == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Under_A.png",
            "True", Null(),
            )
    contains:








        ConditionSwitch(
            "JeanX.hose == 'stockings'", "images/JeanSex/Jean_Sex_Hose_Stockings.png",
            "JeanX.hose == 'stockings_and_garterbelt'", "images/JeanSex/Jean_Sex_Hose_StockingsGarter_A.png",
            "JeanX.hose == 'garterbelt'", "images/JeanSex/Jean_Sex_Hose_Garter_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'in' in JeanX.spunk", "images/JeanSex/Jean_Sex_Spunk_Pussy_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.underwear_pulled_down", Null(),
            "JeanX.underwear == 'lace_panties'", "images/JeanSex/Jean_Sex_Panties_Anal_Lace.png",
            "JeanX.underwear == 'bikini_bottoms'", "images/JeanSex/Jean_Sex_Panties_Anal_Bikini.png",
            "JeanX.underwear and JeanX.Wet", "images/JeanSex/Jean_Sex_Panties_Anal_Green_W.png",
            "JeanX.underwear", "images/JeanSex/Jean_Sex_Panties_Anal_Green.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.piercings == 'barbell'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.legs and not JeanX.underwear)", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",
                    "JeanX.underwear_pulled_down and not JeanX.legs", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",
                    "JeanX.underwear == 'lace_panties'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Lace.png",
                    "JeanX.underwear == 'bikini_bottoms'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Bikini.png",
                    "JeanX.underwear", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Green.png",
                    "True", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",
                    ),
            "JeanX.piercings == 'ring'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.legs and not JeanX.underwear)", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",
                    "JeanX.underwear_pulled_down and not JeanX.legs", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",
                    "JeanX.underwear == 'lace_panties'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Lace.png",
                    "JeanX.underwear == 'bikini_bottoms'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Bikini.png",
                    "JeanX.underwear", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Green.png",
                    "True", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(JeanX.underwear and JeanX.underwear_pulled_down)", Null(),


            "JeanX.hose == 'pantyhose'", "images/JeanSex/Jean_Sex_Hose_Pantyhose_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.legs == 'skirt' and JeanX.upskirt", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt_Up.png",
            "JeanX.legs == 'skirt' and primary_action == 'hotdog'", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt_Up.png",
            "JeanX.legs == 'skirt'", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt.png",
            "JeanX.upskirt", Null(),
            "JeanX.legs == 'pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Pants_W.png",
            "JeanX.legs == 'pants'", "images/JeanSex/Jean_Sex_Legs_Anal_Pants.png",
            "JeanX.legs == 'shorts' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Shorts_W.png",
            "JeanX.legs == 'shorts'", "images/JeanSex/Jean_Sex_Legs_Anal_Shorts.png",
            "JeanX.legs == 'yoga_pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Yoga_W.png",
            "JeanX.legs == 'yoga_pants'", "images/JeanSex/Jean_Sex_Legs_Anal_Yoga.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JeanX.hose == 'pantyhose' and not JeanX.underwear_pulled_down", Null(),
            "JeanX.legs and not JeanX.upskirt and JeanX.Wet >=2", Null(),
            "JeanX.piercings == 'barbell'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.legs and not JeanX.underwear)", Null(),
                    "JeanX.legs == 'skirt' and not JeanX.upskirt", Null(),
                    "JeanX.legs == 'pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Pants.png",
                    "JeanX.legs == 'shorts'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Shorts.png",
                    "JeanX.legs == 'yoga_pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Yoga.png",
                    "True", Null(),
                    ),
            "JeanX.piercings == 'ring'", ConditionSwitch(

                    "JeanX.upskirt or (not JeanX.legs and not JeanX.underwear)", Null(),
                    "JeanX.legs == 'skirt' and not JeanX.upskirt", Null(),
                    "JeanX.legs == 'pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Pants.png",
                    "JeanX.legs == 'shorts'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Shorts.png",
                    "JeanX.legs == 'yoga_pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Yoga.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'belly' in JeanX.spunk", "images/JeanSex/Jean_Sex_Spunk_Belly_A.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Jean_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Jean_Sex_Lick_Ass",
            "True", Null()
            )
    zoom 1






image Jean_Sex_Body_Lick:

    contains:
        "Jean_Sex_Body"
        subpixel True
        pos (0,-80)
        block:
            ease 1 pos (0,-90)
            ease 1 pos (0,-80)
            repeat

image Jean_Sex_Legs_Lick:

    contains:

        "Jean_Sex_Legs_A"
        subpixel True
        pos (0,-40)
        block:
            ease 1 ypos -45
            ease 1 ypos -40
            repeat


image Jean_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.7
    offset (500,680)

image Jean_Sex_Lick_Ass:
    "Lick_Anim"
    zoom 0.7
    offset (500,740)


image Jean_Sex_Zero_Cock:

    contains:
        subpixel True

        ConditionSwitch(
                "Player.sprite", "Zero_Blowcock" ,
                "True", Null(),
                )
        subpixel True
        anchor (0.5,1.0)
        transform_anchor True
        offset (485,1000)
        zoom 0.48



image Jean_Sex_Static:

    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-190)
        block:
            pause 0.2
            ease 2 ypos -180
            pause 0.8
            ease 2 ypos -190
            repeat
    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat







image Jean_Sex_Lick:






    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-190)
        block:
            pause 0.2
            ease 2 ypos -180
            pause 0.8
            ease 2 ypos -190
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-230)
        block:
            ease 2 ypos -220
            pause 0.8
            ease 2 ypos -230
            pause 0.2
            repeat
    zoom 1.8
    offset (-500,-400)








image Jean_Sex_Fucking_Speed0:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -240
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat







image Jean_Sex_Fucking_Speed1:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 1.2
            ease 1 ypos 20
            pause 1.1
            ease 1.1 ypos -10
            pause 0.1
            ease .5 ypos 0
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -200
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-220)
        block:
            ease 2 ypos -190
            pause 0.8
            ease 2 ypos -220
            pause 0.2
            repeat








image Jean_Sex_Fucking_Speed2:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.7
            ease 1.5 ypos 20
            pause 0.8
            ease 1.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-180)
        block:
            easeout 0.5 ypos -160
            easein 1.5 ypos -80
            pause 0.8
            easeout 1 ypos -130
            easein 1 ypos -180
            pause 0.2
            repeat









image Jean_Sex_Fucking_Speed3:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.3
            ease 0.3 ypos 20
            pause 0.3
            ease 0.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_S"
        pos (0,-200)
        block:
            pause 0.1
            ease 0.5 ypos -100
            pause 0.2
            ease 1.0 ypos -200
            pause 0.1
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-140)
        block:
            ease 0.6 ypos -60
            pause 0.2
            easeout 0.7 ypos -140
            easein 0.4 ypos -150
            repeat









image Jean_Sex_Anal_Spunk_Heading_Over:
    "images/JeanSex/Jean_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease .75 xzoom 1.0
        pause 1.75
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Jean_Sex_Anal_Spunk_Heading_Under:
    "images/JeanSex/Jean_Sex_Spunk_Anal_Under.png"
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

image Jean_Sex_Anal_Mask:


    contains:
        "images/JeanSex/Jean_Sex_Mask_Anal.png"
        yoffset 3



image Jean_Sex_Anal_Speed0:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -240
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-280)
        block:
            ease 2 ypos -270
            pause 0.8
            ease 2 ypos -280
            pause 0.2
            repeat






image Jean_Sex_Anal_Speed1:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 1.2
            ease 1 ypos 20
            pause 1.1
            ease 1.1 ypos -10
            pause 0.1
            ease .5 ypos 0
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-250)
        block:
            pause 0.2
            ease 2 ypos -200
            pause 0.8
            ease 2 ypos -250
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-250)
        block:
            ease 2 ypos -220
            pause 0.8
            ease 2 ypos -250
            pause 0.2
            repeat






image Jean_Sex_Anal_Speed2:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.7
            ease 1.5 ypos 20
            pause 0.8
            ease 1.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:
            ease 2 ypos -100
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat






image Jean_Sex_Anal_Speed3:

    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        block:
            pause 0.3
            ease 0.3 ypos 20
            pause 0.3
            ease 0.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.1
            ease 0.5 ypos -100
            pause 0.2
            ease 1.0 ypos -200
            pause 0.1
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-190)
        block:
            ease 0.6 ypos -120
            pause 0.1

            ease 1.2 ypos -190



            repeat











image Jean_Sex_Hotdog_Speed1:

    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.2
            ease 2 ypos -80
            pause 0.8
            ease 2 ypos -200
            repeat
    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        alpha 0.8
        block:
            pause 0.7
            ease 1.5 ypos 20
            pause 0.8
            ease 1.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-200)
        block:







            ease 2 ypos -100
            pause 0.8
            ease 2 ypos -200
            pause 0.2
            repeat






image Jean_Sex_Hotdog_Speed2:

    contains:

        subpixel True
        "Jean_Sex_Legs_A"
        pos (0,-200)
        block:
            pause 0.1
            ease 0.5 ypos -100
            pause 0.2
            ease 1.0 ypos -200
            pause 0.1
            repeat
    contains:

        subpixel True
        "Jean_Sex_Zero_Cock"
        pos (0,0)
        alpha 0.8
        block:
            pause 0.3
            ease 0.3 ypos 20
            pause 0.3
            ease 0.5 ypos 0
            pause 0.5
            repeat
    contains:

        subpixel True
        "Jean_Sex_Body"
        pos (0,-190)
        block:
            ease 0.6 ypos -120
            pause 0.1
            ease 1.2 ypos -190



            repeat











label Jean_Sex_Launch(Line=primary_action):
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action




    $ Player.sprite = 1
    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.cock_position = "in"
        if offhand_action in ("fondle_pussy","dildo_pussy","eat_pussy"):
            $ offhand_action = 0
    elif Line == "anal":
        $ Player.cock_position = "anal"
        if offhand_action in ("finger_ass","dildo_anal","eat_ass"):
            $ offhand_action = 0
    elif Line == "hotdog":
        if JeanX.PantsNum() == 5:
            $ JeanX.upskirt = 1
        $ Player.cock_position = "out"
    elif Line == "foot":
        $ ShowFeet = 1
        $ Player.cock_position = "foot"
        $ JeanX.pose = "doggy"
    elif Line == "massage":
        $ Player.sprite = 0
        $ Player.cock_position = 0
    else:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        $ action_speed = 0
    $ primary_action = Line

    if JeanX.pose == "doggy":
        call Jean_Doggy_Launch (Line)
        return
    if renpy.showing("Jean_SexSprite"):
        return
    $ action_speed = 0
    call Jean_Hide (1)
    show Jean_SexSprite zorder 150
    with dissolve
    return

label Jean_Sex_Reset:
    if renpy.showing("Jean_Doggy_Animation"):
        call Jean_Doggy_Reset
        return
    if not renpy.showing("Jean_SexSprite"):
        return
    $ JeanX.ArmPose = 2
    hide Jean_SexSprite
    call Jean_Hide
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return











image Jean_BJ_Animation:
    LiveComposite(
        (858,928),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Jean_BJ_HairBack", Jean_BJ_Head_0()),
            "action_speed == 1", At("Jean_BJ_HairBack", Jean_BJ_Head_1()),
            "action_speed == 2", At("Jean_BJ_HairBack", Jean_BJ_Head_2()),
            "action_speed == 3", At("Jean_BJ_HairBack", Jean_BJ_Head_3()),
            "action_speed == 4", At("Jean_BJ_HairBack", Jean_BJ_Head_4()),
            "action_speed == 5", At("Jean_BJ_HairBack", Jean_BJ_Head_5()),
            "action_speed == 6", At("Jean_BJ_HairBack", Jean_BJ_Head_6()),
            "True", Null(),
            ),
        (-20,270), ConditionSwitch(

            "action_speed == 0", At("Jean_BJ_Backdrop", Jean_BJ_Body_0()),
            "action_speed == 1", At("Jean_BJ_Backdrop", Jean_BJ_Body_1()),
            "action_speed == 2", At("Jean_BJ_Backdrop", Jean_BJ_Body_2()),
            "action_speed == 3", At("Jean_BJ_Backdrop", Jean_BJ_Body_3()),
            "action_speed == 4", At("Jean_BJ_Backdrop", Jean_BJ_Body_4()),
            "action_speed == 5", At("Jean_BJ_Backdrop", Jean_BJ_Body_5()),
            "action_speed == 6", At("Jean_BJ_Backdrop", Jean_BJ_Body_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Jean_BJ_Head", Jean_BJ_Head_0()),
            "action_speed == 1", At("Jean_BJ_Head", Jean_BJ_Head_1()),
            "action_speed == 2", At("Jean_BJ_Head", Jean_BJ_Head_2()),
            "action_speed == 3", At("Jean_BJ_Head", Jean_BJ_Head_3()),
            "action_speed == 4", At("Jean_BJ_Head", Jean_BJ_Head_4()),
            "action_speed == 5", At("Jean_BJ_Head", Jean_BJ_Head_5()),
            "action_speed == 6", At("Jean_BJ_Head", Jean_BJ_Head_6()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Blowcock", Jean_BJ_Cock_0()),
            "action_speed == 1", At("Blowcock", Jean_BJ_Cock_1()),
            "action_speed >= 2", At("Blowcock", Jean_BJ_Cock_2()),



            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MouthSuckingMask"), Jean_BJ_Head_3()),
            "action_speed == 4", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MouthSuckingMask"), Jean_BJ_Head_4()),
            "action_speed == 6", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MouthSuckingMask"), Jean_BJ_Head_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 2", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MaskHeadingComposite"), Jean_BJ_Head_2()),
            "action_speed == 5", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MaskHeadingComposite"), Jean_BJ_Head_5()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed < 3 or 'mouth' not in JeanX.spunk", Null(),
            "action_speed == 3", At("JeanSuckingSpunk", Jean_BJ_Head_3()),
            "action_speed == 4", At("JeanSuckingSpunk", Jean_BJ_Head_4()),
            "action_speed == 6", At("JeanSuckingSpunk", Jean_BJ_Head_6()),
            "True", Null(),
            ),







        )
    zoom .55
    anchor (.5,.5)

image Jean_BJ_HairBack:

    ConditionSwitch(
            "JeanX.Water or JeanX.hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Under.png",
            "JeanX.hair == 'pony'", Null(),
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Under.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Jean_BJ_HairTop:

    ConditionSwitch(
            "JeanX.Water or JeanX.hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Jean_BJ_Backdrop1:
    contains:

        ConditionSwitch(
                "'blanket' in JeanX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),
        zoom 2
        anchor (.5,.5)
        pos (350,600)









image Jean_BJ_Head:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "(JeanX.Water or JeanX.hair == 'wet') and renpy.showing('Jean_SexSprite')", "images/JeanBJFace/Jean_BJ_Hair_Wet_Mid.png",
            "JeanX.Water or JeanX.hair == 'wet'", Null(),
            "JeanX.hair == 'pony'", Null(),
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Under.png",
            ),




        (0,0), ConditionSwitch(






            "JeanX.blushing > 1", "images/JeanBJFace/Jean_BJ_Head_Blush2.png",
            "JeanX.blushing", "images/JeanBJFace/Jean_BJ_Head_Blush1.png",
            "True", "images/JeanBJFace/Jean_BJ_Head_Blush0.png"
            ),
        (0,0), ConditionSwitch(






            "action_speed and renpy.showing('Jean_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png",
                    "action_speed == 4", "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png",
                    "action_speed == 6", "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",
            "JeanX.mouth == 'normal'", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            "JeanX.mouth == 'lipbite'", "images/JeanBJFace/Jean_BJ_Mouth_Lipbite.png",
            "JeanX.mouth == 'sucking'", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",
            "JeanX.mouth == 'kiss'", "images/JeanBJFace/Jean_BJ_Mouth_Kiss.png",
            "JeanX.mouth == 'sad'", "images/JeanBJFace/Jean_BJ_Mouth_Sad.png",
            "JeanX.mouth == 'smile'", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            "JeanX.mouth == 'smirk'", "images/JeanBJFace/Jean_BJ_Mouth_Smirk.png",
            "JeanX.mouth == 'grimace'", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            "JeanX.mouth == 'surprised'", "images/JeanBJFace/Jean_BJ_Mouth_Kiss.png",
            "JeanX.mouth == 'tongue'", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",
            "True", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(


            "not renpy.showing('Jean_BJ_Animation')", Null(),
            "action_speed == 2", At("Jean_BJ_MouthHeading", Jean_BJ_MouthAnim()),
            "action_speed == 5", At("Jean_BJ_MouthHeading", Jean_BJ_MouthAnimC()),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "'mouth' not in JeanX.spunk", Null(),
            "action_speed and renpy.showing('Jean_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/JeanBJFace/Jean_BJ_Spunk_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 4", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 6", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
                    ),
            "JeanX.mouth == 'normal'", "images/JeanBJFace/Jean_BJ_Spunk_Smile.png",



            "JeanX.mouth == 'smile'", "images/JeanBJFace/Jean_BJ_Spunk_Smile.png",


            "JeanX.mouth == 'tongue'", "images/JeanBJFace/Jean_BJ_Spunk_Tongue.png",
            "JeanX.mouth == 'sucking'", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
            "True", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
            ),
        (0,0), ConditionSwitch(

            "JeanX.brows == 'normal'", "images/JeanBJFace/Jean_BJ_Brows_Normal.png",
            "JeanX.brows == 'angry'", "images/JeanBJFace/Jean_BJ_Brows_Angry.png",
            "JeanX.brows == 'sad'", "images/JeanBJFace/Jean_BJ_Brows_Sad.png",
            "JeanX.brows == 'surprised'", "images/JeanBJFace/Jean_BJ_Brows_Surprised.png",
            "JeanX.brows == 'confused'", "images/JeanBJFace/Jean_BJ_Brows_Confused.png",
            "True", "images/JeanBJFace/Jean_BJ_Brows_Normal.png",
            ),
        (0,0), "Jean BJ Blink",

        (0,0), ConditionSwitch(

            "JeanX.Water or JeanX.hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
            "JeanX.hair == 'pony'", "images/JeanBJFace/Jean_BJ_Hair_Pony_Over.png",
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Over.png",
            ),











        (0,0), ConditionSwitch(

            "'hair' in JeanX.spunk", "images/JeanBJFace/Jean_BJ_Spunk_Facial2.png",
            "'facial' in JeanX.spunk", "images/JeanBJFace/Jean_BJ_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)


image Jean BJ Blink:

    ConditionSwitch(
            "JeanX.eyes == 'normal'", "images/JeanBJFace/Jean_BJ_Eyes_Normal.png",
            "JeanX.eyes == 'sexy'", "images/JeanBJFace/Jean_BJ_Eyes_Sexy.png",
            "JeanX.eyes == 'closed'", "images/JeanBJFace/Jean_BJ_Eyes_Closed.png",
            "JeanX.eyes == 'surprised'", "images/JeanBJFace/Jean_BJ_Eyes_Surprised.png",
            "JeanX.eyes == 'side'", "images/JeanBJFace/Jean_BJ_Eyes_Side.png",
            "JeanX.eyes == 'stunned'", "images/JeanBJFace/Jean_BJ_Eyes_Stunned.png",
            "JeanX.eyes == 'down'", "images/JeanBJFace/Jean_BJ_Eyes_Down.png",
            "JeanX.eyes == 'manic'", "images/JeanBJFace/Jean_BJ_Eyes_Surprised.png",
            "JeanX.eyes == 'squint'", "images/JeanBJFace/Jean_BJ_Eyes_Sexy.png",
            "True", "images/JeanBJFace/Jean_BJ_Eyes_Normal.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JeanBJFace/Jean_BJ_Eyes_Closed.png"
    .25
    repeat

image Jean_BJ_MouthHeading:

    contains:
        "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)

image Jean_BJ_MouthSuckingMask:

    contains:
        "images/JeanBJFace/Jean_BJ_Mouth_MaskS.png"
        zoom 1.4








image Jean_BJ_MaskHeading:

    contains:
        "images/JeanBJFace/Jean_BJ_Mouth_MaskH.png"
        offset (-380,-595)

image Jean_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", At("Jean_BJ_MaskHeading", Jean_BJ_MouthAnim()),
            "action_speed == 5", At("Jean_BJ_MaskHeading", Jean_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Jean_BJ_MaskHeadingSpunk:

    contains:

        ConditionSwitch(
                    "action_speed == 2", "images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png",
                    "True", Null(),
                    )


        subpixel True
        anchor (0.5, 0.65)
        zoom 0.58
        block:
            pause .20
            easeout .15 zoom 0.66
            linear .15 zoom 0.60
            easein .25 zoom 0.68
            pause .25

            pause .40
            easeout .40 zoom 0.60
            linear .10 zoom 0.66
            easein .30 zoom 0.58
            pause .30

            repeat


    zoom 1.8
    yoffset 180

image JeanSuckingSpunk:
    contains:
        "images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)


image Jean_BJ_Backdrop:

    contains:

        ConditionSwitch(
                "'blanket' in JeanX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                )
        zoom 1.2
        anchor (.5,.5)
        pos (180,-400)
    contains:







        "Jean_TJ_Braback"
        subpixel True
        pos (0,0)
        transform_anchor True
    contains:







        "Jean_TJ_Body"
        subpixel True
        pos (0,0)
        transform_anchor True
    contains:







        "Jean_TJ_TitR"
        subpixel True
        pos (0,0)
        transform_anchor True
    contains:






        "Jean_TJ_Tits"
        subpixel True
        pos (0,0)
        transform_anchor True






    zoom 1.4
    offset (225,1100)




transform Jean_BJ_MouthAnim():

    subpixel True
    zoom 0.58
    block:
        pause .20
        easeout .15 zoom 0.66
        linear .15 zoom 0.60
        easein .25 zoom 0.68
        pause .25

        pause .40
        easeout .40 zoom 0.60
        linear .10 zoom 0.66
        easein .30 zoom 0.58
        pause .30

        repeat















transform Jean_BJ_Head_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 40
        ease 1.5 offset (0,-40)
        repeat






transform Jean_BJ_MouthAnimC():

    subpixel True
    zoom 0.7
    block:
        pause .20
        ease .50 zoom 0.65
        pause .60
        ease .30 zoom 0.7
        pause .10
        ease .30 zoom 0.65
        pause .20
        ease .30 zoom 0.7
        repeat



transform Jean_BJ_Cock_0():

    anchor (.5,.5)
    rotate -10
transform Jean_BJ_Cock_1():

    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause .5
        ease 2.5 rotate 0
        repeat
transform Jean_BJ_Cock_2():

    anchor (.5,.5)
    rotate 0
    alpha 1




transform Jean_BJ_Head_0():

    subpixel True
    ease 1.5 offset (0,0)
transform Jean_BJ_Body_0():

    subpixel True
    ease 1.5 offset (0,0)


transform Jean_BJ_Head_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (25,100)
        ease 2 offset (0,-35)
        pause .5
        repeat
transform Jean_BJ_Body_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (30,90)
        ease 2 offset (0,-35)
        pause .5
        repeat













transform Jean_BJ_Body_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat

transform Jean_BJ_Head_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120
        ease 1.5 offset (0,50)
        repeat
transform Jean_BJ_Body_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100
        ease 1.5 offset (0,50)
        repeat

transform Jean_BJ_Head_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat
transform Jean_BJ_Body_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Jean_BJ_Head_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat
transform Jean_BJ_Body_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat

transform Jean_BJ_Head_6():

    ease .5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230
        repeat
transform Jean_BJ_Body_6():

    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190
        repeat


















label Jean_BJ_Launch(Line=primary_action):
    if renpy.showing("Jean_BJ_Animation"):
        return


    if renpy.showing("Jean_TJ_Animation"):
        hide Jean_TJ_Animation
    else:
        call Jean_Hide
        if Line == "L" or Line == "cum":
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_center):
                alpha 1
                ease 1 zoom 2.5 offset (150,80)
            with dissolve
        else:
            show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_center):
                alpha 1
                zoom 2.5 offset (150,80)
            with dissolve
        hide Jean_Sprite

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    show Jean_BJ_Animation zorder 150:
        pos (645,510)
    if Taboo and Line == "L":
        if len(Present) >= 2:
            if Present[0] != JeanX:
                "[JeanX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != JeanX:
                "[JeanX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[JeanX.name] looks around to see if anyone can see her."
        "She then bends down and puts your cock to her mouth."
    elif Line == "L":
        "[JeanX.name] smoothly bends down and places your cock against her cheek."

    return

label Jean_BJ_Reset:
    if not renpy.showing("Jean_BJ_Animation"):
        return

    call Jean_Hide
    $ action_speed = 0

    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Jean_Sprite zorder JeanX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return













image Jean_Hand_Under:
    "images/JeanSprite/handjean2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

image Jean_Hand_Over:
    "images/JeanSprite/handjean1.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)

transform Jean_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5
        pause 0.1
        repeat

transform Jean_Hand_2():
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

image Jean_HJ_Animation:
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jean_Hand_Under"),
            "action_speed == 1", At("Jean_Hand_Under", Jean_Hand_1()),
            "action_speed >= 2", At("Jean_Hand_Under", Jean_Hand_2()),
            "action_speed ", Null(),
            ),
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1J()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jean_Hand_Over"),
            "action_speed == 1", At("Jean_Hand_Over", Jean_Hand_1()),
            "action_speed >= 2", At("Jean_Hand_Over", Jean_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Jean_HJ_Launch(Line=primary_action):
    if renpy.showing("Jean_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call Jean_Hide
    $ JeanX.ArmPose = 1
    if Line == "L":
        show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)
    else:
        show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)
        with dissolve

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause .5
    show Jean_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:

        offset (250,250)
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_right):
        alpha 1
        ease .5 zoom 1.7 offset (-150,200)
    return

label Jean_HJ_Reset:
    if not renpy.showing("Jean_HJ_Animation"):
        return
    $ action_speed = 0
    $ JeanX.ArmPose = 1
    hide Jean_HJ_Animation with easeoutbottom
    call Jean_Hide
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        zoom 1.7 offset (-150,200)
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
        pause .5
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return








image Jean_Hand_Psychic:
    ConditionSwitch(
        "Psychic == 'mouth'", "images/JeanSprite/PsyMouth.png",
        "Psychic == 'pussy'", "images/JeanSprite/PsyPussy.png",
        "Psychic == 'anal'", "images/JeanSprite/PsyAss.png",
        "Psychic == 'tits'", "images/JeanSprite/PsyTits.png",
        "True", "images/JeanSprite/handjeanP.png",
        )


    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)
    block:
        ease 3 alpha 0.7
        ease 3 alpha 1
        repeat

image Jean_PJ_Animation:








    contains:
        ConditionSwitch(


            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1J()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jean_Hand_Psychic"),
            "action_speed == 1", At("Jean_Hand_Psychic", Jean_Hand_1()),
            "action_speed >= 2", At("Jean_Hand_Psychic", Jean_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Jean_PJ_Launch(Line=primary_action):
    if renpy.showing("Jean_PJ_Animation"):
        $ primary_action = "psy"
        return

    call Jean_Hide
    if JeanX.location == bg_current:

        show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
            alpha 1
            zoom 1 offset (0,0) xpos JeanX.sprite_location

    show Jean_PJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:

        offset (250,250)
    return

label Jean_PJ_Reset:
    if not renpy.showing("Jean_PJ_Animation"):
        return
    $ action_speed = 0
    $ JeanX.ArmPose = 1
    hide Jean_PJ_Animation with easeoutbottom
    return








image Jean_TJ_Animation:

    contains:
        ConditionSwitch(

                    "not Player.sprite","Jean_TJ_0",
                    "action_speed == 1", "Jean_TJ_1",
                    "action_speed == 4", "Jean_TJ_4",
                    "action_speed == 5", "Jean_TJ_5",
                    "action_speed >= 2", "Jean_TJ_2",
                    "True",       "Jean_TJ_0",
                    )
    zoom .8
    transform_anchor True
    anchor (.5,.5)




image Jean_TJ_HairBack:

    "Jean_BJ_HairBack"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Jean_TJ_Head:

    "Jean_BJ_Head"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image Jean_TJ_HairTop:

    ConditionSwitch(
                    "JeanX.Water or JeanX.hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
                    "JeanX.hair == 'pony'", "images/JeanBJFace/Jean_BJ_Hair_Pony_Over.png",
                    "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Over.png",
                    )




    transform_anchor True
    zoom .98
    anchor (0.5, 0.5)
    offset (30,-450)
    rotate 0

image JeanScreen:
    "images/JeanBJFace/screenshot0115.png"
    alpha 0.2

image Jean_TJ_ZeroCock:

    "Zero_Blowcock"
    transform_anchor True
    zoom .6
    anchor (0.5, 0.5)
    offset (70,50)
    rotate 0

image Jean_TJ_Body:

    contains:
        "images/JeanBJFace/Jean_TJ_Body.png"
    contains:

        ConditionSwitch(

                        "JeanX.bra == 'sports_bra'","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Base.png",
                        "JeanX.bra == 'bikini_top'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Base.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(

                        "JeanX.top == 'yellow_shirt'","images/JeanBJFace/Jean_TJ_Over_Tank_Base.png",
                        "JeanX.top == 'green_shirt'","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Base.png",
                        "JeanX.top == 'pink_shirt'","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Base.png",
                        "True", Null(),
                        )





    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0


image Jean_TJ_TitR:

    contains:

        ConditionSwitch(

                    "not renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_TJ_TitR.png",
                    "True",  "images/JeanBJFace/Jean_TJ_TitRTJ.png",
                    )
    contains:

        ConditionSwitch(
                        "'tits' not in JeanX.spunk",Null(),
                        "True",       "images/JeanBJFace/Jean_TJ_Spunk_TitsUnder.png",
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Jean_TJ_Braback:






    contains:
        ConditionSwitch(
                        "JeanX.top == 'green_shirt'",Null(),
                        "JeanX.bra == 'green_bra' or JeanX.bra == 'lace_bra'","images/JeanBJFace/Jean_TJ_Chest_Bra_Base.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0

image Jean_TJ_BraStretch:

    contains:
        ConditionSwitch(

                        "JeanX.bra == 'bikini_top' or JeanX.bra == 'sports_bra'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Stretch.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0


image Jean_TJ_Tits:

    contains:
        "images/JeanBJFace/Jean_TJ_TitL.png"
    contains:

        ConditionSwitch(
                        "JeanX.piercings == 'ring'","images/JeanBJFace/Jean_TJ_Pierce_Ring.png",
                        "JeanX.piercings == 'barbell'","images/JeanBJFace/Jean_TJ_Pierce_Barbell.png",
                        "True", Null(),
                        )
    contains:
        ConditionSwitch(

                    "not renpy.showing('Jean_TJ_Animation')", Null(),
                    "True",  "images/JeanBJFace/Jean_TJ_TitRO.png",
                    )
    contains:
        ConditionSwitch(
                        "'tits' not in JeanX.spunk",Null(),
                        "True",       "images/JeanBJFace/Jean_TJ_Spunk_Tits.png",
                        )
    contains:

        ConditionSwitch(
                        "JeanX.bra == 'green_bra' and JeanX.top_pulled_up and JeanX.top == 'green_shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_UpS.png",
                        "JeanX.bra == 'green_bra' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_Bra_Up.png",
                        "JeanX.bra == 'lace_bra' and JeanX.top_pulled_up and JeanX.top == 'green_shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_UpS.png",
                        "JeanX.bra == 'lace_bra' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_Bra_Up.png",
                        "JeanX.bra == 'sports_bra' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Up.png",
                        "JeanX.bra == 'bikini_top' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Chest_Bikini_Up.png",
                        "JeanX.bra == 'green_bra' and JeanX.top == 'green_shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_Strapless.png",
                        "JeanX.bra == 'green_bra'","images/JeanBJFace/Jean_TJ_Chest_Bra_Top.png",
                        "JeanX.bra == 'lace_bra' and JeanX.top == 'green_shirt'","images/JeanBJFace/Jean_TJ_Chest_LaceBra_Strapless.png",
                        "JeanX.bra == 'lace_bra'","images/JeanBJFace/Jean_TJ_Chest_LaceBra_Top.png",
                        "JeanX.bra == 'sports_bra'","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Top.png",
                        "JeanX.bra == 'bikini_top'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Top.png",
                        "JeanX.bra == 'corset' and not JeanX.top_pulled_up and not renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_TJ_Chest_Corset.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(

                        "JeanX.top == 'yellow_shirt' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Over_Tank_Up.png",
                        "JeanX.top == 'yellow_shirt'","images/JeanBJFace/Jean_TJ_Over_Tank_Top.png",
                        "JeanX.top == 'green_shirt' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Up.png",
                        "JeanX.top == 'pink_shirt' and JeanX.top_pulled_up","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Up.png",
                        "JeanX.top == 'green_shirt'","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Top.png",
                        "JeanX.top == 'pink_shirt'","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Top.png",
                        "JeanX.top == 'towel' and not renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_TJ_Over_Towel.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "JeanX.top_pulled_up", Null(),
                        "(not JeanX.top or JeanX.top == 'towel') and (not JeanX.bra or JeanX.bra == 'corset')", Null(),
                        "JeanX.piercings == 'ring'","images/JeanBJFace/Jean_TJ_Pierce_RingC.png",
                        "JeanX.piercings == 'barbell'","images/JeanBJFace/Jean_TJ_Pierce_BarbellC.png",
                        "True", Null(),
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)

    rotate 0





image Jean_TJ_0:

    contains:

        "Jean_TJ_Braback"
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

        "Jean_TJ_HairBack"
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

        "Jean_TJ_Body"
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

        "Jean_TJ_Head"
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

        "Jean_TJ_TitR"
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
        "Jean_TJ_ZeroCock"
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
            "Jean_TJ_BraStretch"
        subpixel True
        pos (0,20)
        transform_anchor True
        yzoom .75
    contains:
        contains:
            "Jean_TJ_Tits"
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

        "Jean_TJ_HairTop"
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





image Jean_TJ_1:

    contains:

        "Jean_TJ_Braback"
        subpixel True
        pos (0,140)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:

        "Jean_TJ_HairBack"
        subpixel True
        pos (0,150)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Jean_TJ_Body"
        subpixel True
        pos (0,150)
        transform_anchor True
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
    contains:

        "Jean_TJ_Head"
        subpixel True
        pos (0,150)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Jean_TJ_TitR"
        subpixel True
        pos (0,140)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:

        subpixel True
        "Jean_TJ_ZeroCock"
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
            "Jean_TJ_BraStretch"
        subpixel True
        pos (0,145)
        transform_anchor True
        yzoom 1
        parallel:
            pause .1
            ease 1.9 ypos -70
            pause .4
            ease 2.3 ypos 145
            repeat
        parallel:
            pause .1
            ease 1.9 yzoom .5
            pause .4
            ease 1.8 yzoom 1
            pause .5
            repeat
    contains:
        contains:
            "Jean_TJ_Tits"
        subpixel True
        pos (0,140)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:

        "Jean_TJ_HairTop"
        subpixel True
        pos (0,150)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .2
            ease 2 ypos 150
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat







image Jean_TJ_2:

    contains:

        "Jean_TJ_Braback"
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

        "Jean_TJ_HairBack"
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

        "Jean_TJ_Body"
        subpixel True
        pos (0,80)
        transform_anchor True
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
    contains:

        "Jean_TJ_Head"
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

        "Jean_TJ_TitR"
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
        "Jean_TJ_ZeroCock"
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
            "Jean_TJ_BraStretch"
        subpixel True
        pos (0,50)
        transform_anchor True
        yzoom .75
        parallel:
            pause .2
            ease .8 ypos 0
            pause .3
            ease .3 ypos 50
            repeat
    contains:
        contains:
            "Jean_TJ_Tits"
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

        "Jean_TJ_HairTop"
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






image Jean_TJ_4:

    contains:

        "Jean_TJ_Braback"
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

        "Jean_TJ_HairBack"
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

        "Jean_TJ_Body"
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

        "Jean_TJ_Head"
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

        "Jean_TJ_TitR"
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
        "Jean_TJ_ZeroCock"
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
            "Jean_TJ_Tits"
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

        "Jean_TJ_HairTop"
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




image Jean_TJ_5:

    contains:

        "Jean_TJ_Braback"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 80
            pause .2
            ease 2 ypos 90
            pause .4
            repeat
    contains:

        "Jean_TJ_HairBack"
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

        "Jean_TJ_Body"
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

        "Jean_TJ_Head"
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

        "Jean_TJ_TitR"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 80
            pause .2
            ease 2 ypos 90
            pause .4
            repeat
    contains:

        subpixel True
        "Jean_TJ_ZeroCock"
        pos (0,25)
        transform_anchor True
        rotate -10
    contains:
        contains:
            "Jean_TJ_BraStretch"
        subpixel True
        pos (-20,145)
        transform_anchor True
        yzoom 1
    contains:
        contains:
            "Jean_TJ_Tits"
        subpixel True
        pos (0,90)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos 80
            pause .2
            ease 2 ypos 90
            pause .4
            repeat
    contains:

        "Jean_TJ_HairTop"
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





label Jean_TJ_Launch(Line=primary_action):
    if renpy.showing("Jean_TJ_Animation"):
        return
























    show blackscreen onlayer black with dissolve

    if renpy.showing("Jean_BJ_Animation"):
        hide Jean_BJ_Animation
    else:
        call Jean_Hide
        show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
            alpha 1
            ease 1 zoom 2.3 xpos 750 yoffset -100
        show Jean_Sprite zorder JeanX.sprite_layer:
            alpha 0

    if JeanX.top == "towel" or JeanX.bra == "corset":
        $ JeanX.top_pulled_up = 1

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Jean_TJ_Animation zorder 150:
        pos (1000,1050)
    $ Player.sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Jean_TJ_Reset:

    if not renpy.showing("Jean_TJ_Animation"):
        return

    call Jean_Hide
    $ Player.sprite = 0

    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        zoom 2.3 xpos 750 yoffset -100
    show Jean_Sprite zorder JeanX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos JeanX.sprite_location yoffset 0
    "[JeanX.name] pulls back"
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos JeanX.sprite_location
    return













label Jean_Kissing_Launch(T=primary_action, Set=1):
    call Jean_Hide
    $ primary_action = T
    $ JeanX.pose = "kiss" if Set else JeanX.pose
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location)
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Jean_Kissing_Smooch:
    $ JeanX.change_face("kiss")
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos JeanX.sprite_location zoom 1
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        zoom 1
    $ JeanX.change_face("sexy")
    return

label Jean_Breasts_Launch(T=primary_action, Set=1):
    call Jean_Hide
    $ primary_action = T
    $ JeanX.pose = "breasts" if Set else JeanX.pose
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Jean_Middle_Launch(T=primary_action, Set=1):
    call Jean_Hide
    $ primary_action = T
    $ JeanX.pose = "mid" if Set else JeanX.pose
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Jean_Pussy_Launch(T=primary_action, Set=1):
    call Jean_Hide
    $ primary_action = T
    $ JeanX.pose = "pussy" if Set else JeanX.pose
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Jean_Pos_Reset(T=0, Set=0):
    if JeanX.location != bg_current:
        return
    call Jean_Hide
    show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location):
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Jean_Sprite zorder JeanX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (JeanX.sprite_location,50)
    $ JeanX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Jean_Hide(Sprite=0):
    call Jean_Sex_Reset
    hide Jean_SexSprite
    hide Jean_Doggy_Animation
    hide Jean_HJ_Animation
    hide Jean_BJ_Animation
    hide Jean_TJ_Animation
    hide Jean_PJ_Animation
    if Sprite:
        hide Jean_Sprite
    return



image GropeRightBreast_Jean:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (185,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat

image GropeLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image LickRightBreast_Jean:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (175,325)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (150,300)
            pause .5
            ease 1.5 rotate 30 pos (175,325)
            repeat


image LickLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (275,330)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (255,310)
            pause .5
            ease 1.5 rotate 30 pos (275,330)
            repeat

image GropeThigh_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,630)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (255,700)
            ease 1 rotate 100 pos (245,630)
            repeat

image GropePussy_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,560)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (245,545)
                ease .75 rotate 170 pos (245,560)
            choice:
                ease .5 rotate 190 pos (245,545)
                pause .25
                ease 1 rotate 170 pos (245,560)
            repeat

image FingerPussy_Jean:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (265,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (275,615)
                pause .5
                ease 1 rotate 50 pos (265,640)
            choice:
                ease .5 rotate 40 pos (275,615)
                pause .5
                ease 1.75 rotate 50 pos (265,640)
            choice:
                ease 2 rotate 40 pos (275,615)
                pause .5
                ease 1 rotate 50 pos (265,640)
            choice:
                ease .25 rotate 40 pos (275,615)
                ease .25 rotate 50 pos (265,640)
                ease .25 rotate 40 pos (275,615)
                ease .25 rotate 50 pos (265,640)
            repeat

image Lickpussy_Jean:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (275,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (265,575)
            linear .5 rotate -60 pos (255,585)
            easein 1 rotate 10 pos (275,595)
            repeat

image VibratorRightBreast_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (165,310)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease .9 rotate 35 ypos 300
            pause .25
            ease .7 rotate 55 ypos 310
            pause .25
            repeat

image VibratorLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (270,310)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1.1 rotate 35 ypos 300
            pause .25
            ease .9 rotate 55 ypos 310
            pause .25
            repeat

image VibratorPussy_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (265,580)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 250
            pause .25
            ease 1 rotate 70 xpos 265
            pause .25
            repeat

image VibratorAnal_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (295,570)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 290
            pause .25
            ease 1 rotate 10 xpos 300
            pause .25
            repeat

image VibratorPussyInsert_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeBothBreast_Jean:
    contains:
        "GirlGropeLeftBreast_Jean"
    contains:
        "GirlGropeRightBreast_Jean"

image GirlGropeLeftBreast_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 pos (290,350)
            ease 1 rotate -10 pos (290,340)
            repeat

image GirlGropeRightBreast_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (170,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -40 pos (170,350)
            ease 1 rotate -10 pos (170,340)
            repeat

image GirlGropeThigh_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        anchor (0.5,0.5)
        pos (0,0)
        alpha 0.5
        rotate 100













image GirlGropePussy_JeanSelf:
    contains:
        "GirlGropePussy_Jean"
        anchor (0.5,0.5)
        rotate -40

        pos (200,510)

image GirlGropePussy_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (240,540)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (240,535)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (240,535)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (240,535)
                ease .75 rotate 200 pos (240,540)
                ease .5 rotate 205 pos (240,535)
                ease .75 rotate 200 pos (240,540)
            choice:
                ease .3 rotate 205 pos (240,535)
                ease .3 rotate 200 pos (240,545)
                ease .3 rotate 205 pos (240,535)
                ease .3 rotate 200 pos (240,545)
            repeat

image GirlFingerPussy_Jean:
    contains:
        subpixel True
        "UI_GirlFinger"
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
