

image Jubes_Sprite:
    LiveComposite(
        (500,950),

        (0,0), ConditionSwitch(

            "JubesX.outfit['front_outer_accessory']", "images/JubesSprite/Jubes_Sprite_Jacket_Collar.png",
            "True", Null(),
            ),

        (147,48), "Jubes_Sprite_HairBack",






        (0,0), ConditionSwitch(

            "not JubesX.outfit['bottom'] or not JubesX.upskirt", Null(),
            "JubesX.outfit['bottom'] == '_pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants_Back.png",
            "JubesX.outfit['bottom'] == '_shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.outfit['underwear'] or not JubesX.underwear_pulled_down", Null(),

            "JubesX.outfit['bottom'] and not JubesX.upskirt and JubesX.outfit['bottom'] != '_skirt'", Null(),

            "JubesX.outfit['underwear'] == '_lace_panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace_Back.png",
            "JubesX.outfit['underwear'] == '_tiger_panties'", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Back.png",
            "JubesX.outfit['underwear'] == '_bikini_bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Back.png",
            "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Back.png",
            ),

        (0,0), ConditionSwitch(

            "JubesX.arm_pose != 1", "images/JubesSprite/Jubes_Sprite_Body2.png",
            "True", "images/JubesSprite/Jubes_Sprite_Body1.png",
            ),
        (0,0), ConditionSwitch(

            "JubesX.wet and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Water1.png",
            "JubesX.wet", "images/JubesSprite/Jubes_Sprite_Water2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(







            "not JubesX.outfit['front_outer_accessory']", Null(),
            "(JubesX.top_pulled_up or JubesX.outfit['front_outer_accessory'] == '_open_jacket') and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Open1_Back.png",
            "(JubesX.top_pulled_up or JubesX.outfit['front_outer_accessory'] == '_open_jacket')", "images/JubesSprite/Jubes_Sprite_Jacket_Open2_Back.png",


            "True", "images/JubesSprite/Jubes_Sprite_Jacket_Closed_Back.png",

            ),































        (0,0), ConditionSwitch(

            "JubesX.pubes", "images/JubesSprite/Jubes_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.outfit['front_inner_accessory']", Null(),


            "JubesX.outfit['front_inner_accessory'] == '_barbell'", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Bot.png",
            "JubesX.outfit['front_inner_accessory'] == '_ring'", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Bot.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.outfit['front_inner_accessory']", Null(),



            "JubesX.outfit['front_inner_accessory'] == '_barbell'", ConditionSwitch(


                    "True", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Top.png",
                    ),


            "JubesX.outfit['top'] or JubesX.outfit['bra']", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            "True", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            ),






        (0,0), ConditionSwitch(

            "JubesX.top_pulled_up", ConditionSwitch(

                    "JubesX.outfit['bra'] == '_lace_bra'", "images/JubesSprite/Jubes_Sprite_Chest_Lace_Up.png",
                    "JubesX.outfit['bra'] == '_sports_bra'", "images/JubesSprite/Jubes_Sprite_Chest_Sports_Up.png",
                    "JubesX.outfit['bra'] == '_bikini_top'", "images/JubesSprite/Jubes_Sprite_Chest_Bikini_Up.png",
                    "True", Null(),
                    ),
            "JubesX.outfit['bra'] == '_lace_bra'", "images/JubesSprite/Jubes_Sprite_Chest_Lace.png",
            "JubesX.outfit['bra'] == '_sports_bra'", "images/JubesSprite/Jubes_Sprite_Chest_Sports.png",
            "JubesX.outfit['bra'] == '_bikini_top'", "images/JubesSprite/Jubes_Sprite_Chest_Bikini.png",
            "True", Null(),
            ),















        (0,0), ConditionSwitch(

            "JubesX.outfit['hose'] == '_socks'", "images/JubesSprite/Jubes_Sprite_Hose_Socks.png",
            "JubesX.outfit['hose'] == '_stockings'", "images/JubesSprite/Jubes_Sprite_Hose_Stockings.png",
            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesSprite/Jubes_Sprite_Hose_StockingsandGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesSprite/Jubes_Sprite_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.outfit['underwear']", Null(),
            "JubesX.underwear_pulled_down", ConditionSwitch(

                    "not JubesX.outfit['bottom'] or JubesX.upskirt or JubesX.outfit['bottom'] == '_skirt'", ConditionSwitch(

                            "JubesX.outfit['underwear'] == '_lace_panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace_Down.png",
                            "JubesX.outfit['underwear'] == '_bikini_bottoms' and JubesX.grool", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_DownW.png",
                            "JubesX.outfit['underwear'] == '_bikini_bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Down.png",
                            "JubesX.outfit['underwear'] == '_tiger_panties' and JubesX.grool", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_DownW.png",
                            "JubesX.outfit['underwear'] == '_tiger_panties'", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Down.png",
                            "JubesX.grool", "images/JubesSprite/Jubes_Sprite_Panties_Blue_DownW.png",
                            "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Down.png",
                            ),
                    "True", Null(),
                    ),
            "JubesX.grool", ConditionSwitch(

                "JubesX.outfit['underwear'] == '_lace_panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace.png",
                "JubesX.outfit['underwear'] == '_bikini_bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Wet.png",
                "JubesX.outfit['underwear'] == '_tiger_panties' and JubesX.grool", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Wet.png",
                "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Wet.png",
                ),
            "True", ConditionSwitch(

                "JubesX.outfit['underwear'] == '_lace_panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace.png",
                "JubesX.outfit['underwear'] == '_bikini_bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini.png",
                "JubesX.outfit['underwear'] == '_tiger_panties'", "images/JubesSprite/Jubes_Sprite_Panties_Tiger.png",
                "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue.png",
                ),
            ),
        (0,0), ConditionSwitch(

            "JubesX.outfit['hose'] == '_pantyhose' and (not JubesX.underwear_pulled_down or not JubesX.outfit['underwear'])", "images/JubesSprite/Jubes_Sprite_Hose_Pantyhose.png",
            "JubesX.outfit['hose'] == '_ripped_pantyhose' and (not JubesX.underwear_pulled_down or not JubesX.outfit['underwear'])", "images/JubesSprite/Jubes_Sprite_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.outfit['bottom']", Null(),
            "JubesX.upskirt", ConditionSwitch(

                        "JubesX.outfit['bottom'] == '_pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants_Down.png",
                        "JubesX.outfit['bottom'] == '_shorts' and JubesX.grool > 1", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_DownW.png",
                        "JubesX.outfit['bottom'] == '_shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Down.png",
                        "True", Null(),
                        ),
            "JubesX.grool > 1", ConditionSwitch(

                "JubesX.outfit['bottom'] == '_pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants.png",
                "JubesX.outfit['bottom'] == '_shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Wet.png",

                "True", Null(),
                ),
            "True", ConditionSwitch(

                "JubesX.outfit['bottom'] == '_pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants.png",
                "JubesX.outfit['bottom'] == '_shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts.png",

                "True", Null(),
                ),
            ),
























        (0,0), ConditionSwitch(

            "JubesX.top_pulled_up", ConditionSwitch(

                    "JubesX.outfit['top'] == '_tube_top'", "images/JubesSprite/Jubes_Sprite_Over_Tube_Up.png",
                    "JubesX.outfit['top'] == '_red_shirt'", "images/JubesSprite/Jubes_Sprite_Over_Red_Up.png",
                    "JubesX.outfit['top'] == '_black_shirt'", "images/JubesSprite/Jubes_Sprite_Over_Black_Up.png",

                    "True", Null(),
                    ),


            "JubesX.outfit['top'] == '_tube_top'", "images/JubesSprite/Jubes_Sprite_Over_Tube.png",
            "JubesX.outfit['top'] == '_red_shirt'", "images/JubesSprite/Jubes_Sprite_Over_Red.png",
            "JubesX.outfit['top'] == '_black_shirt'", "images/JubesSprite/Jubes_Sprite_Over_Black.png",
            "JubesX.outfit['top'] == '_towel' and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Over_Towel1.png",
            "JubesX.outfit['top'] == '_towel'", "images/JubesSprite/Jubes_Sprite_Over_Towel2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.outfit['front_outer_accessory']", Null(),
            "JubesX.outfit['front_outer_accessory'] == '_open_jacket' and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Open1.png",
            "JubesX.outfit['front_outer_accessory'] == '_open_jacket'", "images/JubesSprite/Jubes_Sprite_Jacket_Open2.png",
            "JubesX.top_pulled_up", ConditionSwitch(

                    "(JubesX.outfit['front_outer_accessory'] == '_jacket' or JubesX.outfit['front_outer_accessory'] == 'shut jacket') and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Open1.png",
                    "JubesX.outfit['front_outer_accessory'] == '_jacket' or JubesX.outfit['front_outer_accessory'] == 'shut jacket'", "images/JubesSprite/Jubes_Sprite_Jacket_Open2.png",
                    "True", Null(),
                    ),


            "JubesX.outfit['front_outer_accessory'] == '_jacket' and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Closed1.png",
            "JubesX.outfit['front_outer_accessory'] == '_jacket'", "images/JubesSprite/Jubes_Sprite_Jacket_Closed2.png",

            "JubesX.upskirt and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Shut1_Up.png",
            "JubesX.upskirt", "images/JubesSprite/Jubes_Sprite_Jacket_Shut2_Up.png",
            "JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Shut1.png",
            "True", "images/JubesSprite/Jubes_Sprite_Jacket_Shut2.png",
            ),
















        (0,0), ConditionSwitch(

            "JubesX.spunk['belly']", "images/JubesSprite/Jubes_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.spunk['breasts']", "images/JubesSprite/Jubes_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_ArmOver1.png",
            "True", "images/JubesSprite/Jubes_Sprite_ArmOver2.png",
            ),
        (0,0), ConditionSwitch(

            "JubesX.wet and JubesX.arm_pose == 1", "images/JubesSprite/Jubes_Sprite_Water1_Arm.png",
            "True", Null(),
            ),


        (147,48), "Jubes_Sprite_Head",




















        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != JubesX", Null(),


            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_JubesSelf",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck_breasts'", "GirlGropeLeftBreast_Jubes",

                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeRightBreast_Jubes",

                    "True", "GirlGropeBothBreast_Jubes",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Jubes",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Jubes",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Jubes",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_offhand_action or second_girl_primary_action != 'masturbation' or focused_Girl == JubesX", Null(),


            "second_girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and JubesX.lust >= 70", "GirlFingerPussy_Jubes",
            "second_girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Jubes",
            "second_girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Jubes",
            "second_girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(


            "not primary_action or focused_Girl != JubesX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Jubes",
            "primary_action == 'fondle_thighs'", "GropeThigh_Jubes",
            "primary_action == 'fondle_breasts'", "GropeLeftBreast_Jubes",
            "primary_action == 'suck_breasts'", "LickRightBreast_Jubes",
            "primary_action == 'fondle_pussy' and action_speed == 2", "FingerPussy_Jubes",
            "primary_action == 'fondle_pussy'", "GropePussy_Jubes",
            "primary_action == 'eat_pussy'", "Lickpussy_Jubes",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Jubes",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "primary_action == 'vibrator anal'", "VibratorAnal_Jubes",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not offhand_action or focused_Girl != JubesX", Null(),


            "offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' and primary_action == 'suck_breasts'", "GropeLeftBreast_Jubes",

                    "True", "GropeRightBreast_Jubes",

                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck_breasts'", "VibratorLeftBreast_Jubes",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck_breasts'", "LickLeftBreast_Jubes",
            "offhand_action == 'fondle_pussy'", "GropePussy_Jubes",
            "offhand_action == 'eat_pussy'", "Lickpussy_Jubes",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Jubes",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Jubes",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Jubes",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_primary_action or focused_Girl != JubesX", Null(),


            "second_girl_primary_action == 'fondle_pussy' and primary_action != 'sex' and JubesX.lust >= 70", "GirlFingerPussy_Jubes",
            "second_girl_primary_action == 'fondle_pussy'", "GirlGropePussy_Jubes",
            "second_girl_primary_action == 'eat_pussy'", "Lickpussy_Jubes",
            "second_girl_primary_action == 'suck_breasts' and (offhand_action != 'suck_breasts' or primary_action == 'suck_breasts')", "LickLeftBreast_Jubes",
            "second_girl_primary_action == 'suck_breasts'", "LickRightBreast_Jubes",
            "second_girl_primary_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeLeftBreast_Jubes",


                    "True", "GirlGropeRightBreast_Jubes",
                    ),
            "second_girl_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_primary_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action != 'lesbian' or focused_Girl == JubesX or not girl_offhand_action", Null(),


            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and JubesX.lust >= 70", "GirlFingerPussy_Jubes",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Jubes",
            "girl_offhand_action == 'eat_pussy'", "Lickpussy_Jubes",
            "girl_offhand_action == 'suck_breasts' and (offhand_action != 'suck_breasts' or primary_action == 'suck_breasts')", "LickLeftBreast_Jubes",
            "girl_offhand_action == 'suck_breasts'", "LickRightBreast_Jubes",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeLeftBreast_Jubes",

                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck_breasts'", "GirlGropeRightBreast_Jubes",

                    "girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck_breasts'", "GirlGropeLeftBreast_Jubes",

                    "True", "GirlGropeRightBreast_Jubes",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        )
    anchor (0.6, -0.15) zoom 1.1


image Jubes_Sprite_HairBack:
    contains:
        ConditionSwitch(




                "JubesX.outfit['hair'] == '_wet'", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Back.png",
                "JubesX.wet", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Back.png",
                "True", "images/JubesSprite/Jubes_Sprite_Hair_Short_Back.png",
                ),

    anchor (0.5, 0.5)
    zoom .37


image Jubes_Sprite_Head:
    LiveComposite(
        (900,900),





        (0,0), ConditionSwitch(

                "JubesX.blushing == '_blush2'", "images/JubesSprite/Jubes_Sprite_Head_Blush2.png",
                "JubesX.blushing", "images/JubesSprite/Jubes_Sprite_Head_Blush1.png",
                "True", "images/JubesSprite/Jubes_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "not JubesX.spunk['chin']", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(
            "JubesX.mouth == '_lipbite'", "images/JubesSprite/Jubes_Sprite_mouth_Lipbite.png",
            "JubesX.mouth == '_sucking'", "images/JubesSprite/Jubes_Sprite_mouth_Open.png",
            "JubesX.mouth == '_kiss'", "images/JubesSprite/Jubes_Sprite_mouth_Kiss.png",
            "JubesX.mouth == '_sad'", "images/JubesSprite/Jubes_Sprite_mouth_Sad.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_mouth_Smile.png",
            "JubesX.mouth == '_surprised'", "images/JubesSprite/Jubes_Sprite_mouth_Open.png",
            "JubesX.mouth == '_tongue'", "images/JubesSprite/Jubes_Sprite_mouth_Tongue.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_mouth_Smile.png",
            "JubesX.mouth == '_smirk'", "images/JubesSprite/Jubes_Sprite_mouth_Smirk.png",
            "True", "images/JubesSprite/Jubes_Sprite_mouth_Normal.png",
            ),


        (0,0), ConditionSwitch(
            "not JubesX.spunk['mouth']", Null(),
            "JubesX.mouth == '_sucking'", "images/JubesSprite/Jubes_Sprite_Spunk_Open.png",
            "JubesX.mouth == '_kiss'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.mouth == '_sad'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_Spunk_Lipbite.png",
            "JubesX.mouth == '_surprised'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.mouth == '_tongue'", "images/JubesSprite/Jubes_Sprite_Spunk_Open.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_Spunk_Lipbite.png",
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Smirk.png",
            ),

        (0,0), ConditionSwitch(

            "JubesX.brows == '_angry' and JubesX.blushing == '_blush2'", "images/JubesSprite/Jubes_Sprite_brows_AngryB.png",
            "JubesX.brows == '_angry'", "images/JubesSprite/Jubes_Sprite_brows_Angry.png",
            "JubesX.brows == '_sad' and JubesX.blushing == '_blush2'", "images/JubesSprite/Jubes_Sprite_brows_SadB.png",
            "JubesX.brows == '_sad'", "images/JubesSprite/Jubes_Sprite_brows_Sad.png",
            "JubesX.brows == '_surprised'", "images/JubesSprite/Jubes_Sprite_brows_Surprised.png",
            "JubesX.brows == '_sad' and JubesX.blushing == '_blush2'", "images/JubesSprite/Jubes_Sprite_brows_ConfusedB.png",
            "JubesX.brows == '_confused'", "images/JubesSprite/Jubes_Sprite_brows_Confused.png",
            "True", "images/JubesSprite/Jubes_Sprite_brows_Normal.png",
            ),
        (0,0), "Jubes Blink",





        (0,0), "images/JubesSprite/Jubes_Sprite_Earrings.png",
        (0,0), ConditionSwitch(


            "JubesX.outfit['hair'] == '_wet' or JubesX.wet", "images/JubesSprite/Jubes_Sprite_Hair_Wet.png",
            "JubesX.outfit['hair'] == '_shades'", "images/JubesSprite/Jubes_Sprite_Hair_Shades.png",
            "True", "images/JubesSprite/Jubes_Sprite_Hair_Short.png",
            ),
        (0,0), ConditionSwitch(

            "not JubesX.wet", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Wet_Head.png",
            ),
        (0,0), ConditionSwitch(

            "JubesX.spunk['hair']", "images/JubesSprite/Jubes_Sprite_Spunk_Shades.png",
            "JubesX.spunk['face']", "images/JubesSprite/Jubes_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .37


image Jubes Blink:
    ConditionSwitch(
    "JubesX.eyes == '_sexy'", "images/JubesSprite/Jubes_Sprite_eyes_Sexy.png",
    "JubesX.eyes == '_side'", "images/JubesSprite/Jubes_Sprite_eyes_Side.png",
    "JubesX.eyes == '_surprised'", "images/JubesSprite/Jubes_Sprite_eyes_Surprised.png",
    "JubesX.eyes == '_normal'", "images/JubesSprite/Jubes_Sprite_eyes_Normal.png",
    "JubesX.eyes == '_stunned'", "images/JubesSprite/Jubes_Sprite_eyes_Stunned.png",
    "JubesX.eyes == '_down'", "images/JubesSprite/Jubes_Sprite_eyes_Down.png",
    "JubesX.eyes == '_closed'", "images/JubesSprite/Jubes_Sprite_eyes_Closed.png",
    "JubesX.eyes == '_leftside'", "images/JubesSprite/Jubes_Sprite_eyes_Leftside.png",
    "JubesX.eyes == '_manic'", "images/JubesSprite/Jubes_Sprite_eyes_Squint.png",
    "JubesX.eyes == '_squint'", "Jubes_Squint",
    "True", "images/JubesSprite/Jubes_Sprite_eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JubesSprite/Jubes_Sprite_eyes_Closed.png"
    .25
    repeat

image Jubes_Squint:
    "images/JubesSprite/Jubes_Sprite_eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JubesSprite/Jubes_Sprite_eyes_Squint.png"
    .25
    repeat








image Jubes_Drip_MaskPanties:

    contains:
        "images/JubesSprite/Jubes_Sprite_DripMaskPanties.png"
        offset (-145,-560)

image Jubes_Drip_MaskPants:

    contains:
        "images/JubesSprite/Jubes_Sprite_DripMaskPants.png"
        offset (-145,-560)











image Jubes_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Jubes_Doggy_Body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Top",
                    "action_speed", "Jubes_Doggy_Anal_Head_Top",
                    "True", "Jubes_Doggy_Body",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Top",
                    "True", "Jubes_Doggy_Body",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Jubes_Doggy_Foot2_Top",
                    "action_speed", "Jubes_Doggy_Foot1_Top",
                    "True", "Jubes_Doggy_Foot0_Top",
                    ),
            "True", "Jubes_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Jubes_Doggy_Ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Ass",
                    "action_speed", "Jubes_Doggy_Anal_Head_Ass",
                    "True", "Jubes_Doggy_Ass",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Ass",
                    "True", "Jubes_Doggy_Ass",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Jubes_Doggy_Foot2_Ass",
                    "action_speed", "Jubes_Doggy_Foot1_Ass",
                    "True", "Jubes_Doggy_Foot0_Ass",
                    ),
            "True", "Jubes_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Jubes_Doggy_Feet2",
                    "action_speed", "Jubes_Doggy_Feet1",
                    "True", "Jubes_Doggy_Feet0",
                    ),
            "not Player.sprite and show_feet", "Jubes_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)



image Jubes_Doggy_Body:
    LiveComposite(

        (610,750),

        (0,60), "Jubes_Doggy_Head",



        (0,0), "images/JubesDoggy/Jubes_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "not JubesX.outfit['bra']", Null(),









            "JubesX.outfit['bra'] == '_white_tank'", "images/JubesDoggy/Jubes_Doggy_Chest_Costume.png",
            "JubesX.outfit['bra'] == 'lace corset'", "images/JubesDoggy/Jubes_Doggy_Chest_Corset.png",
            "JubesX.outfit['bra'] == '_corset'", "images/JubesDoggy/Jubes_Doggy_Chest_Corset.png",
            "JubesX.outfit['bra'] == 'wolvie top'", "images/JubesDoggy/Jubes_Doggy_Chest_Wolvie.png",
            "JubesX.outfit['bra'] == '_bikini_top'", "images/JubesDoggy/Jubes_Doggy_Chest_Bikini.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Chest_Tank.png",
            ),





        (0,0), ConditionSwitch(

            "not JubesX.outfit['bottom']", Null(),
            "JubesX.outfit['front_outer_accessory'] == '_suspenders'", "images/JubesDoggy/Jubes_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.outfit['gloves'] == '_gloves'", "images/JubesDoggy/Jubes_Doggy_Gloves.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.outfit['top']", Null(),
            "JubesX.outfit['top'] == '_jacket'", "images/JubesDoggy/Jubes_Doggy_Over_Jacket.png",
            "JubesX.outfit['top'] == '_towel' and not JubesX.top_pulled_up", "images/JubesDoggy/Jubes_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.spunk[back]", "images/JubesDoggy/Jubes_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Jubes_Doggy_GropeBreast",
            "True", Null()
            ),


        )


    offset (-200,0)




image Jubes_Doggy_Head:
    LiveComposite(

        (420,525),


        (0,0), ConditionSwitch(

            "JubesX.wet or JubesX.outfit['hair'] == '_wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Wet_Back.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Hair_Long_Back.png",
            ),
        (0,0), ConditionSwitch(


            "JubesX.blushing", "images/JubesDoggy/Jubes_Doggy_Head_Blush.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "JubesX.mouth == '_normal'", "images/JubesDoggy/Jubes_Doggy_mouth_Smile.png",
            "JubesX.mouth == '_lipbite'", "images/JubesDoggy/Jubes_Doggy_mouth_Smile.png",
            "JubesX.mouth == '_sucking'", "images/JubesDoggy/Jubes_Doggy_mouth_Open.png",
            "JubesX.mouth == '_kiss'", "images/JubesDoggy/Jubes_Doggy_mouth_Kiss.png",
            "JubesX.mouth == '_sad'", "images/JubesDoggy/Jubes_Doggy_mouth_Sad.png",
            "JubesX.mouth == '_smile'", "images/JubesDoggy/Jubes_Doggy_mouth_Smile.png",
            "JubesX.mouth == '_smile'", "images/JubesDoggy/Jubes_Doggy_mouth_Smile.png",
            "JubesX.mouth == '_surprised'", "images/JubesDoggy/Jubes_Doggy_mouth_Open.png",
            "JubesX.mouth == '_tongue'", "images/JubesDoggy/Jubes_Doggy_mouth_Tongue.png",
            "True", "images/JubesDoggy/Jubes_Doggy_mouth_Smile.png",
            ),



















        (0,0), ConditionSwitch(


            "JubesX.brows == '_angry'", "images/JubesDoggy/Jubes_Doggy_brows_Angry.png",
            "JubesX.brows == '_sad'", "images/JubesDoggy/Jubes_Doggy_brows_Sad.png",
            "JubesX.brows == '_surprised'", "images/JubesDoggy/Jubes_Doggy_brows_Surprised.png",

            "True", "images/JubesDoggy/Jubes_Doggy_brows_Normal.png",
            ),
        (0,0), "Jubes Doggy Blink",





        (0,0), ConditionSwitch(

            "JubesX.spunk['face']", "images/JubesDoggy/Jubes_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.wet or JubesX.outfit['hair'] == '_wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Wet.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Hair_Long.png",
            ),
        (0,0), ConditionSwitch(

            "JubesX.spunk['hair']", "images/JubesDoggy/Jubes_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )

































image Jubes Doggy Blink:

    ConditionSwitch(
        "JubesX.eyes == '_sexy'", "images/JubesDoggy/Jubes_Doggy_eyes_Sexy.png",
        "JubesX.eyes == '_side'", "images/JubesDoggy/Jubes_Doggy_eyes_Side.png",
        "JubesX.eyes == '_normal'", "images/JubesDoggy/Jubes_Doggy_eyes_Sexy.png",
        "JubesX.eyes == '_closed'", "images/JubesDoggy/Jubes_Doggy_eyes_Closed.png",
        "JubesX.eyes == '_manic'", "images/JubesDoggy/Jubes_Doggy_eyes_Stunned.png",
        "JubesX.eyes == '_down'", "images/JubesDoggy/Jubes_Doggy_eyes_Sexy.png",
        "JubesX.eyes == '_stunned'", "images/JubesDoggy/Jubes_Doggy_eyes_Stunned.png",
        "JubesX.eyes == '_surprised'", "images/JubesDoggy/Jubes_Doggy_eyes_Surprised.png",
        "JubesX.eyes == '_squint'", "images/JubesDoggy/Jubes_Doggy_eyes_Sexy.png",
        "True", "images/JubesDoggy/Jubes_Doggy_eyes_Normal.png",
        ),






    3

    "images/JubesDoggy/Jubes_Doggy_eyes_Closed.png"
    .25
    repeat

image Jubes_Doggy_Ass:
    LiveComposite(

        (420,750),








        (0,0), ConditionSwitch(

            "not JubesX.underwear_pulled_down or (JubesX.outfit['bottom'] == '_pants' and not JubesX.upskirt)", Null(),
            "JubesX.outfit['underwear'] == '_wolvie_panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie_Back.png",
            "JubesX.outfit['underwear'] == '_lace_panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Lace_Back.png",
            "JubesX.outfit['underwear']", "images/JubesDoggy/Jubes_Doggy_Panties_Back.png",
            "True", Null(),
            ),
        (0,0), "images/JubesDoggy/Jubes_Doggy_Ass.png",





        (0,0), ConditionSwitch(

            "JubesX.outfit['hose'] == '_black_stockings'", "images/JubesDoggy/Jubes_Doggy_Stocking.png",
            "JubesX.outfit['hose'] == '_stockings'", "images/JubesDoggy/Jubes_Doggy_Hose.png",
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "Player.sprite and Player.cock_position == 'anal'", Null(),
            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.underwear_pulled_down or (JubesX.outfit['bottom'] == '_pants' and not JubesX.upskirt)", Null(),
            "JubesX.outfit['underwear'] == '_wolvie_panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie_Down.png",
            "JubesX.outfit['underwear'] == '_bikini_bottoms'", "images/JubesDoggy/Jubes_Doggy_Panties_Bikini_Down.png",
            "JubesX.outfit['underwear']", "images/JubesDoggy/Jubes_Doggy_Panties_Black_Down.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Jubes_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Jubes_Pussy_Fucking2",
            "Player.sprite and Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Pussy_Fucking3",
                    "action_speed > 1", "Jubes_Pussy_Fucking2",
                    "action_speed", "Jubes_Pussy_Heading",
                    "True", "Jubes_Pussy_animation0",
                    ),
            "primary_action == 'eat_pussy'", "images/JubesDoggy/Jubes_Doggy_Pussy_Open.png",
            "JubesX.outfit['bottom'] and not JubesX.upskirt", "images/JubesDoggy/Jubes_Doggy_Pussy_Closed.png",
            "JubesX.outfit['underwear'] and not JubesX.underwear_pulled_down", "images/JubesDoggy/Jubes_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Jubes_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Jubes_Pussy_Fucking2",
            "True", "images/JubesDoggy/Jubes_Doggy_Pussy_Closed.png",
            ),


        (0,0), ConditionSwitch(

            "JubesX.spunk['pussy'] and Player.cock_position == 'in'",Null(),
            "JubesX.spunk['pussy'] ", "images/JubesDoggy/Jubes_Doggy_SpunkPussyClosed.png",
            "JubesX.grool and Player.cock_position == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "JubesX.grool", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.pubes", Null(),
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "JubesX.outfit['bottom'] == '_pants' and not JubesX.upskirt", "images/JubesDoggy/Jubes_Doggy_Pubes_Panties.png",
            "JubesX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png",
            "JubesX.underwear_pulled_down", "images/JubesDoggy/Jubes_Doggy_Pubes.png",
            "JubesX.outfit['underwear']", "images/JubesDoggy/Jubes_Doggy_Pubes_Panties.png",
            "JubesX.outfit['hose'] and JubesX.outfit['hose'] != '_stockings'", "images/JubesDoggy/Jubes_Doggy_Pubes_Panties.png",
            "primary_action == 'eat_pussy'", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "JubesX.outfit['front_inner_accessory'] == '_ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "JubesX.outfit['front_inner_accessory'] == '_barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Anal_Fucking2",
                    "action_speed > 1", "Jubes_Anal_Fucking",
                    "action_speed", "Jubes_Anal_Heading",
                    "True", "Jubes_Anal",
                    ),


            "JubesX.outfit['bottom'] and not JubesX.upskirt", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
            "JubesX.outfit['underwear'] and not JubesX.underwear_pulled_down", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Jubes_Anal_Fingering",
            "primary_action == 'dildo anal'", "Jubes_Anal_Fucking",
            "JubesX.used_to_anal", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(

            "not JubesX.spunk['anus'] or Player.sprite", Null(),
            "Player.cock_position == 'anal'", "images/JubesDoggy/Jubes_Doggy_SpunkAnalOpen.png",
            "JubesX.used_to_anal", "images/JubesDoggy/Jubes_Doggy_SpunkAnalLoose.png",
            "True", "images/JubesDoggy/Jubes_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(

            "JubesX.underwear_pulled_down or not JubesX.outfit['underwear']", Null(),
            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),


            "JubesX.outfit['underwear'] == '_wolvie_panties' and JubesX.grool", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie_Wet.png",
            "JubesX.outfit['underwear'] == '_wolvie_panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie.png",
            "JubesX.outfit['underwear'] == '_lace_panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Lace.png",
            "JubesX.outfit['underwear'] == '_bikini_bottoms'", "images/JubesDoggy/Jubes_Doggy_Panties_Bikini.png",
            "JubesX.grool", "images/JubesDoggy/Jubes_Doggy_Panties_Black_Wet.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Panties_Black.png",
            ),














        (0,0), ConditionSwitch(

            "JubesX.outfit['bottom'] == '_leather_pants'", ConditionSwitch(
                    "JubesX.upskirt or JubesX.underwear_pulled_down", Null(),

                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_Pants.png",
                    ),





            "JubesX.outfit['bottom'] == '_other_skirt'", ConditionSwitch(
                    "JubesX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/JubesDoggy/Jubes_Doggy_Legs_SkirtCos_Up.png",
                    "JubesX.upskirt", "images/JubesDoggy/Jubes_Doggy_Legs_SkirtCos_Up.png",
                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_SkirtCos.png",
                    ),
            "JubesX.outfit['bottom'] == '_skirt'", ConditionSwitch(
                    "JubesX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/JubesDoggy/Jubes_Doggy_Legs_Skirt_Up.png",
                    "JubesX.upskirt", "images/JubesDoggy/Jubes_Doggy_Legs_Skirt_Up.png",
                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.outfit['top'] == '_towel' and JubesX.upskirt", "images/JubesDoggy/Jubes_Doggy_Over_TowelAss_Up.png",
            "JubesX.outfit['top'] == '_towel'", "images/JubesDoggy/Jubes_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "JubesX.underwear_pulled_down or (not JubesX.outfit['underwear'] and JubesX.outfit['bottom'] != '_leather_pants')", Null(),
            "JubesX.outfit['front_inner_accessory'] == '_ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC.png",
            "JubesX.outfit['front_inner_accessory'] == '_barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.spunk[back]", "images/JubesDoggy/Jubes_Doggy_Spunk_Ass.png",
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
            "JubesX.outfit['bottom'] == '_skirt' and JubesX.upskirt", "images/JubesDoggy/Jubes_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/JubesDoggy/Jubes_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),
            "JubesX.outfit['bottom'] == '_skirt' and JubesX.upskirt and action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "JubesX.outfit['bottom'] == '_skirt' and JubesX.upskirt", AlphaMask("Zero_Hotdog_animation0", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_animation0", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Jubes_Doggy_Feet:
    contains:
        AlphaMask("Jubes_Doggy_Shins", "images/JubesDoggy/Jubes_Doggy_Feet_Toes.png")

image Jubes_Doggy_Shins:

    contains:
        "images/JubesDoggy/Jubes_Doggy_Feet_Back.png"
    contains:



        ConditionSwitch(
            "not JubesX.outfit['hose']", Null(),
            "JubesX.outfit['hose'] == '_stockings'", "images/JubesDoggy/Jubes_Doggy_Feet_Hose_Back.png",
            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Feet_Hose_Back.png",
            "JubesX.outfit['hose'] == '_black_stockings'", "images/JubesDoggy/Jubes_Doggy_Feet_Stockings_Back.png",
            "JubesX.outfit['hose'] == '_pantyhose'", "images/JubesDoggy/Jubes_Doggy_Feet_Hose_Back.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JubesX.outfit['bottom'] == '_leather_pants'", "images/JubesDoggy/Jubes_Doggy_Feet_Pants.png",
            "True", Null(),
            )












image Jubes_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (270,410)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat

















image Zero_Jubes_Hotdog_animation0:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Jubes_Hotdog_Moving:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Jubes_Doggy_animation0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Jubes_Doggy_Heading:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Jubes_Doggy_Fucking2:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jubes_Doggy_Fucking3:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Jubes_Pussy_Mask:


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

image Jubes_Pussy_Mask_animation0:


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


































image Jubes_Pussy_animation0:

    subpixel True
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
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

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jubes_Doggy_animation0", "Jubes_Pussy_Mask_animation0")
    contains:


        AlphaMask("Jubes_PussyHole_animation0", "Jubes_Pussy_Hole_Mask_animation0")

image Jubes_Pussy_Hole_Mask_animation0:

    contains:

        AlphaMask("images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Jubes_PussyHole_animation0:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Jubes_Pussy_Heading:

    subpixel True
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
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

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jubes_Doggy_Heading", "Jubes_Pussy_Mask")
    contains:


        AlphaMask("Jubes_Pussy_Heading_Flap", "Jubes_Pussy_Hole_Mask")


image Jubes_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Jubes_Pussy_Heading_Flap:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Jubes_Pussy_Fingering:

    subpixel True
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
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











        AlphaMask("Zero_Pussy_Finger", "Rogue_doggy_pussy_mask")
    contains:


        AlphaMask("Jubes_Pussy_Heading_Flap", "Jubes_Pussy_Hole_Mask")



image Jubes_Pussy_Fucking2:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Jubes_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),



image Jubes_Pussy_Fucking3:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jubes_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")





image Jubes_Anal:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        "Zero_Doggy_Insert"
        pos (172,500)




image Jubes_Anal_Fingering:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:











        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")


image Jubes_Anal_Heading:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
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

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jubes_Doggy_Anal_Heading", "Zero_Jubes_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Jubes_Doggy_Anal_Heading", "Jubes_Doggy_Anal_Heading_Mask")

image Zero_Jubes_Doggy_Anal_Heading:

    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jubes_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600
            repeat

image Jubes_Doggy_Anal_Heading_Mask:

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

image Jubes_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Jubes_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat


image Zero_Jubes_Doggy_Anal1:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Jubes_Anal_Fucking:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullCheeks.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
    contains:
        ConditionSwitch(

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "primary_action == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Jubes_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),


image Jubes_Doggy_Anal_FullMask:
    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )

image Jubes_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 15
        pause .4
        block:
            ease .2 ypos 5
            pause .3
            ease 2 ypos 15
            repeat

image Jubes_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15
            ease .1 ypos -5
            pause .2
            ease 1.6 ypos 0
            repeat



image Zero_Jubes_Doggy_Anal2:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Jubes_Anal_Fucking2:

    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
    contains:




        "images/JubesDoggy/Jubes_Doggy_Anal_FullCheeks.png"
    contains:

        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
    contains:
        ConditionSwitch(

            "JubesX.outfit['hose'] == '_stockings_and_garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.outfit['hose'] == '_garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Jubes_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Jubes_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Jubes_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




image Jubes_Doggy_Feet0:

    contains:
        "Jubes_Doggy_Shins"
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
        "Jubes_Doggy_Feet"
        pos (0, 0)
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Jubes_Doggy_Feet1:

    contains:
        "Jubes_Doggy_Shins"
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
        "Jubes_Doggy_Feet"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Jubes_Doggy_Feet2:

    contains:
        "Jubes_Doggy_Shins"
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
        "Jubes_Doggy_Feet"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat



image Jubes_Doggy_Foot0_Top:

    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 10








image Jubes_Doggy_Foot0_Ass:

    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:
            pause 1
            ease 2 ypos 20
            pause .5
            ease 1.5 ypos 0
            repeat

image Jubes_Doggy_Foot1_Top:

    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 70
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 70
            repeat

image Jubes_Doggy_Foot1_Ass:

    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat

image Jubes_Doggy_Foot2_Top:

    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 70
        block:






            pause .05
            ease .6 ypos 90
            ease .3 ypos 70
            repeat

image Jubes_Doggy_Foot2_Ass:

    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 70
        block:
            pause .15
            ease .6 ypos 90
            ease .2 ypos 70
            repeat



label Jubes_Doggy_Launch(Line=primary_action):
    return
    if renpy.showing("Jubes_Doggy_Animation"):
        return
    $ action_speed = 0
    call hide_girl(JubesX, hide_sprite = True)
    show Jubes_Doggy_Animation zorder 150 at sprite_location(stage_center+150)
    with dissolve
    return

label Jubes_Doggy_Reset:
    if not renpy.showing("Jubes_Doggy_Animation"):
        return

    $ JubesX.arm_pose = 2
    $ JubesX.SpriteVer = 0
    hide Jubes_Doggy_Animation
    call hide_girl(JubesX)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return









image Jubes_SexSprite:

    contains:
        ConditionSwitch(

            "Player.cock_position == 'in'", ConditionSwitch(

                    "action_speed == 1", "Jubes_Sex_Body_S1",
                    "action_speed == 2", "Jubes_Sex_Body_S2",
                    "action_speed == 3", "Jubes_Sex_Body_S3",
                    "action_speed >= 4", "Jubes_Sex_Body_S4",
                    "True",       "Jubes_Sex_Body_S0",
                    ),
            "Player.cock_position == 'anal'", ConditionSwitch(

                    "action_speed == 1", "Jubes_Sex_Body_A1",
                    "action_speed == 2", "Jubes_Sex_Body_A2",
                    "action_speed == 3", "Jubes_Sex_Body_A3",
                    "action_speed >= 4", "Jubes_Sex_Body_A4",
                    "True",       "Jubes_Sex_Body_A0",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(

                    "not Player.sprite","Jubes_Sex_Body_F0",
                    "action_speed == 1", "Jubes_Sex_Body_F1",
                    "action_speed >= 4", "Jubes_Sex_Body_F0",
                    "action_speed >= 2", "Jubes_Sex_Body_F2",
                    "True",       "Jubes_Sex_Body_F0",
                    ),

            "True", ConditionSwitch(

                    "not Player.sprite","Jubes_Sex_Body_H0",
                    "action_speed == 1", "Jubes_Sex_Body_H1",
                    "action_speed == 4", "Jubes_Sex_Body_H0",
                    "action_speed >= 2", "Jubes_Sex_Body_H2",
                    "True",       "Jubes_Sex_Body_H0",
                    ),
            )
    contains:
        ConditionSwitch(

            "Player.cock_position == 'in'", ConditionSwitch(

                    "action_speed == 1", "Jubes_Sex_Legs_S1",
                    "action_speed == 2", "Jubes_Sex_Legs_S2",
                    "action_speed == 3", "Jubes_Sex_Legs_S3",
                    "action_speed >= 4", "Jubes_Sex_Legs_S4",
                    "True", "Jubes_Sex_Legs_S0",
                    ),
            "Player.cock_position == 'anal'", ConditionSwitch(

                    "action_speed == 1", "Jubes_Sex_Legs_A1",
                    "action_speed == 2", "Jubes_Sex_Legs_A2",
                    "action_speed == 3", "Jubes_Sex_Legs_A3",
                    "action_speed >= 4", "Jubes_Sex_Legs_A4",
                    "True", "Jubes_Sex_Legs_A0",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(

                    "not Player.sprite","Jubes_Sex_Legs_F0",
                    "action_speed == 1", "Jubes_Sex_Legs_F1",
                    "action_speed >= 4", "Jubes_Sex_Legs_F0",
                    "action_speed >= 2", "Jubes_Sex_Legs_F2",
                    "True",       "Jubes_Sex_Legs_F0",
                    ),
            "True", ConditionSwitch(

                    "not Player.sprite","Jubes_Sex_Legs_H0",
                    "action_speed == 1", "Jubes_Sex_Legs_H1",
                    "action_speed == 4", "Jubes_Sex_Legs_H0",
                    "action_speed >= 2", "Jubes_Sex_Legs_H2",
                    "True", "Jubes_Sex_Legs_H0",
                    ),
            )
    zoom .6
    transform_anchor True
    anchor (.5,.5)


image Jubes_Sex_HairBack:

    "Jubes_Sprite_HairBack"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)

image Jubes_Sex_Head:

    "Jubes_Sprite_Head"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)



image Jubes_Sex_Body:

    contains:
        "Jubes_Sex_HairBack"
    contains:



        ConditionSwitch(
                    "Player.cock_position == 'footjob'", Null(),
                    "JubesX.outfit['gloves'] == '_gloves'", "images/JubesSex/Jubes_Sex_Hand_Gloved.png",
                    "True", "images/JubesSex/Jubes_Sex_Hand.png"
                    )
    contains:

        ConditionSwitch(
            "not JubesX.outfit['top']", Null(),
            "JubesX.top_pulled_up", ConditionSwitch(

                    "JubesX.outfit['top'] == '_jacket'", "images/JubesSex/Jubes_Sex_Jacket_Back_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "JubesX.outfit['top'] == '_jacket'", "images/JubesSex/Jubes_Sex_Jacket_Back.png",
                    "True", Null(),
                    ),
            )
    contains:

        "images/JubesSex/Jubes_Sex_Body.png"
    contains:

        ConditionSwitch(
            "not JubesX.outfit['front_inner_accessory']", Null(),
            "JubesX.outfit['front_inner_accessory'] == '_barbell'", "images/JubesSex/Jubes_Sex_Barbell_Tits.png",
            "JubesX.outfit['front_inner_accessory'] == '_ring'", "images/JubesSex/Jubes_Sex_Ring_Tits.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JubesX.outfit['neck'] == '_leash choker'", "images/JubesSex/Jubes_Sex_Leash.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JubesX.outfit['hose'] == '_stockings_and_garterbelt' or JubesX.outfit['hose'] == '_garterbelt'", "images/JubesSex/Jubes_Sex_Garter.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not JubesX.outfit['bra']", Null(),
            "JubesX.top_pulled_up",ConditionSwitch(

                    "not JubesX.outfit['bra']", Null(),
                    "JubesX.outfit['bra'] == '_white_tank'", "images/JubesSex/Jubes_Sex_WhiteTank_Up.png",
                    "JubesX.outfit['bra'] == 'leather bra'", "images/JubesSex/Jubes_Sex_Bra_Leather_Up.png",
                    "JubesX.outfit['bra'] == 'wolvie top'", "images/JubesSex/Jubes_Sex_Top_Wolvie_Up.png",
                    "JubesX.outfit['bra'] == '_corset'", "images/JubesSex/Jubes_Sex_Corset_Up.png",
                    "JubesX.outfit['bra'] == 'lace corset'", "images/JubesSex/Jubes_Sex_Corset_Lace_Up.png",
                    "JubesX.outfit['bra'] == '_bikini_top'", "images/JubesSex/Jubes_Sex_Top_Bikini_Up.png",


                    "True", Null(),
                    ),

            "JubesX.outfit['bra'] == '_white_tank'", "images/JubesSex/Jubes_Sex_WhiteTank.png",
            "JubesX.outfit['bra'] == 'leather bra'", "images/JubesSex/Jubes_Sex_Bra_Leather.png",
            "JubesX.outfit['bra'] == 'wolvie top'", "images/JubesSex/Jubes_Sex_Top_Wolvie.png",
            "JubesX.outfit['bra'] == '_corset'", "images/JubesSex/Jubes_Sex_Corset.png",
            "JubesX.outfit['bra'] == 'lace corset'", "images/JubesSex/Jubes_Sex_Corset_Lace.png",
            "JubesX.outfit['bra'] == '_bikini_top'", "images/JubesSex/Jubes_Sex_Top_Bikini.png",


            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not JubesX.outfit['front_inner_accessory'] or JubesX.top_pulled_up", Null(),
            "JubesX.outfit['front_inner_accessory'] == '_barbell'", "images/JubesSex/Jubes_Sex_Barbell_Tits_C.png",
            "JubesX.outfit['front_inner_accessory'] == '_ring'", "images/JubesSex/Jubes_Sex_Ring_Tits_C.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not JubesX.outfit['bottom']", Null(),
            "JubesX.outfit['front_outer_accessory'] == '_suspenders' and not JubesX.outfit['bra'] and not JubesX.top_pulled_up", "images/JubesSex/Jubes_Sex_Suspenders.png",
            "JubesX.outfit['front_outer_accessory'] == '_suspenders2'", "images/JubesSex/Jubes_Sex_Suspenders.png",
            "JubesX.outfit['front_outer_accessory'] == '_suspenders'", "images/JubesSex/Jubes_Sex_Suspenders_Up.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not JubesX.outfit['top']", Null(),
            "JubesX.top_pulled_up", ConditionSwitch(

                    "JubesX.outfit['top'] == '_jacket'", "images/JubesSex/Jubes_Sex_Jacket_Up.png",

                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "JubesX.outfit['top'] == '_jacket'", "images/JubesSex/Jubes_Sex_Jacket.png",

                    "True", Null(),
                    ),
            )
    contains:

        ConditionSwitch(
            "JubesX.spunk['belly']", "images/JubesSex/Jubes_Sex_Spunk_Belly.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
                "not JubesX.spunk['breasts']", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Tits.png",
                )
    contains:
        ConditionSwitch(

                "primary_action == 'suck_breasts' or offhand_action == 'suck_breasts'", "Jubes_Sex_Lick_Breasts",
                "True", Null()
                )
    contains:
        ConditionSwitch(

                "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Jubes_Sex_Fondle_Breasts",
                "True", Null()
                )
    contains:
        "Jubes_Sex_Head"
    transform_anchor True
    zoom .9
    offset (55,55)



image Jubes_Sex_Lick_Breasts:
    "Lick_Anim"
    zoom 0.7
    offset (565,290)

image Jubes_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.5
    offset (360,-280)

image Jubes_Sex_Legs:

    contains:

        ConditionSwitch(
            "JubesX.outfit['bottom'] == '_skirt'", "images/JubesSex/Jubes_Sex_Skirt_Back.png",
            "True", Null(),
            )
    contains:







        ConditionSwitch(
            "Player.cock_position == 'footjob'", "images/JubesSex/Jubes_Sex_Legs_Foot.png",
            "True", "images/JubesSex/Jubes_Sex_Legs_High.png",
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'anal' and action_speed > 1", "images/JubesSex/Jubes_Sex_Anus_L.png",
            "Player.cock_position == 'anal' and action_speed > 0", "images/JubesSex/Jubes_Sex_Anus_M.png",
            "JubesX.spunk['anus']", "images/JubesSex/Jubes_Sex_Anus_M.png",
            "True", "images/JubesSex/Jubes_Sex_Anus_S.png",
            )
    contains:

        ConditionSwitch(
            "not JubesX.spunk['anus']", Null(),
            "Player.cock_position == 'anal' and action_speed > 1", "images/JubesSex/Jubes_Sex_Spunk_Anal_U.png",
            "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Pussy_Open.png",
            "Player.cock_position == 'in' and action_speed > 0", "images/JubesSex/Jubes_Sex_Pussy_Mid.png",
            "primary_action == 'eat_pussy'", "images/JubesSex/Jubes_Sex_Pussy_Mid.png",
            "True", "images/JubesSex/Jubes_Sex_Pussy_Closed.png",
            )
    contains:

        ConditionSwitch(
            "not JubesX.grool", Null(),
            "True", "images/JubesSex/Jubes_Sex_Wet.png",
            )
    contains:

        ConditionSwitch(
            "not JubesX.spunk['pussy']", Null(),
            "Player.cock_position == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Open.png",
            "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
            )
    contains:

        ConditionSwitch(
            "not JubesX.pubes", Null(),
            "Player.cock_position == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Pubes_Open.png",
            "Player.cock_position == 'in' and action_speed > 0", "images/JubesSex/Jubes_Sex_Pubes_Mid.png",
            "primary_action == 'eat_pussy'", "images/JubesSex/Jubes_Sex_Pubes_Mid.png",
            "True", "images/JubesSex/Jubes_Sex_Pubes_Closed.png",
            )
    contains:

        ConditionSwitch(
            "JubesX.outfit['front_inner_accessory'] == '_barbell' and Player.cock_position == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Barbell_Pussy_O.png",
            "JubesX.outfit['front_inner_accessory'] == '_barbell'", "images/JubesSex/Jubes_Sex_Barbell_Pussy.png",
            "JubesX.outfit['front_inner_accessory'] == '_ring' and Player.cock_position == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Ring_Pussy_O.png",
            "JubesX.outfit['front_inner_accessory'] == '_ring'", "images/JubesSex/Jubes_Sex_Ring_Pussy.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JubesX.underwear_pulled_down", Null(),

            "JubesX.outfit['underwear'] == '_bikini_bottoms'", "images/JubesSex/Jubes_Sex_Panties_Bikini.png",
            "JubesX.outfit['underwear'] == '_wolvie_panties'", "images/JubesSex/Jubes_Sex_Panties_Wolvie.png",
            "JubesX.outfit['underwear'] == '_lace_panties'", "images/JubesSex/Jubes_Sex_Panties_Lace.png",
            "JubesX.outfit['underwear']", "images/JubesSex/Jubes_Sex_Panties_Black.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'footjob' and (JubesX.outfit['hose'] == '_stockings_and_garterbelt' or JubesX.outfit['hose'] == '_stockings')", "images/JubesSex/Jubes_Sex_Stockings_Base_Foot.png",
            "Player.cock_position == 'footjob' and JubesX.outfit['hose'] == '_black_stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Base_Foot.png",
            "JubesX.outfit['hose'] == '_black_stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Base_Up.png",
            "JubesX.outfit['hose'] == '_stockings_and_garterbelt' or JubesX.outfit['hose'] == '_stockings'", "images/JubesSex/Jubes_Sex_Stockings_Base_Up.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "JubesX.outfit['bottom'] == '_skirt' or JubesX.outfit['bottom'] == '_other_skirt'", "images/JubesSex/Jubes_Sex_Skirt.png",
            "JubesX.upskirt", Null(),
            "JubesX.outfit['bottom'] == '_leather_pants' and Player.cock_position == 'footjob'", "images/JubesSex/Jubes_Sex_Pants_Base_Foot.png",
            "JubesX.outfit['bottom'] == '_leather_pants'", "images/JubesSex/Jubes_Sex_Pants_Base_Up.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Jubes_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Jubes_Sex_Lick_Ass",
            "True", Null()
            ),
    contains:

        ConditionSwitch(


            "JubesX.outfit['front_inner_accessory'] == '_barbell'", "images/JubesSex/Jubes_Sex_Barbell_Pussy_C.png",
            "JubesX.outfit['front_inner_accessory'] == '_ring'", "images/JubesSex/Jubes_Sex_Ring_Pussy_C.png",
            "True", Null(),
            )
    contains:







        ConditionSwitch(
            "Player.cock_position == 'footjob'", "Jubes_Footjob_Foot",
            "True", "Jubes_Sex_Foot",
            )
    transform_anchor True
    zoom 1





image Jubes_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.8
    offset (720,610)

image Jubes_Sex_Lick_Ass:
    "Lick_Anim"
    zoom 0.8
    offset (730,700)


image Jubes_Sex_Foot:




    contains:

        ConditionSwitch(
            "JubesX.outfit['hose'] == '_stockings_and_garterbelt' or JubesX.outfit['hose'] == '_stockings'", "images/JubesSex/Jubes_Sex_Stockings_Up.png",
            "JubesX.outfit['hose'] == '_black_stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Up.png",
            "True", "images/JubesSex/Jubes_Sex_FootHigh.png"
            )
    contains:

        ConditionSwitch(
            "JubesX.upskirt", Null(),
            "JubesX.outfit['bottom'] == '_leather_pants'", "images/JubesSex/Jubes_Sex_Pants_Up.png",
            "True", Null(),
            )
        xoffset -2
    transform_anchor True
    zoom 1

    pos (988,-553)



















image Jubes_CockRef:
    "images/JubesSex/Jubes_Sex_Cocktest.png"
    alpha 0.8






image Jubes_SexMask:
    transform_anchor True
    contains:
        "images/JubesSex/Jubes_Sex_MaskPussyX.png"
        pos (200,303)
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)



image Jubes_Sex_Body_S0:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Jubes_Sex_Legs_S0:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease 0.5 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_S0", "Jubes_SexMask")
        subpixel True
        pos (525,465)
        block:
            pause 0.1
            ease 0.5 ypos 460
            easeout 0.5 ypos 461
            easein 0.9 ypos 465
            repeat


image Jubes_Sex_Zero_Anim_S0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        alpha 0.8
        pos (125,170)
        block:
            ease 2 ypos 115
            easeout .5 ypos 120
            easein 1.5 ypos 170
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True





image Jubes_Sex_Body_S1:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Jubes_Sex_Legs_S1:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease 0.5 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_S1", "Jubes_SexMask")
        subpixel True
        pos (525,485)
        block:
            pause 0.1
            ease 0.5 ypos 480
            easeout 0.5 ypos 481
            easein 0.9 ypos 485
            repeat


image Jubes_Sex_Zero_Anim_S1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,115)
        block:
            ease .5 ypos 90
            easeout .5 ypos 100
            easein 1 ypos 115
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True




image Jubes_Sex_Body_S2:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,10)
        block:
            pause 0.3
            ease 0.3 ypos -10
            pause 0.20
            ease 1.70 ypos 10
            repeat

image Jubes_Sex_Legs_S2:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.25
            ease 0.3 ypos -25
            easeout 0.45 ypos -20
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_S2", "Jubes_SexMask")
        subpixel True
        pos (525,478)
        block:
            pause 0.25
            ease 0.3 ypos 453
            easeout 0.45 ypos 458
            easein 1.5 ypos 478
            repeat
    contains:

        ConditionSwitch(
                "not JubesX.spunk['pussy']", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (-15,-105)
        block:
            pause 0.25
            ease 0.3 ypos -130
            easeout 0.45 ypos -125
            easein 1.5 ypos -105
            repeat


image Jubes_Sex_Zero_Anim_S2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,75)
        block:
            ease .5 ypos -50
            easeout 1.5 ypos 60
            easein .5 ypos 75
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True





image Jubes_Sex_Body_S3:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,10)
        block:
            pause 0.1
            ease 0.2 ypos -50
            pause 0.2
            ease .7 ypos 10
            repeat

image Jubes_Sex_Legs_S3:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -45
            easeout 0.45 ypos -40
            easein .5 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_S3", "Jubes_SexMask")
        subpixel True
        pos (525,478)
        block:
            pause 0.05
            ease 0.2 ypos 433
            easeout 0.45 ypos 438
            easein .5 ypos 478
            repeat
    contains:







        ConditionSwitch(
                "not JubesX.spunk['pussy']", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (-15,-105)
        block:
            pause 0.05
            ease 0.2 ypos -150
            easeout 0.45 ypos -145
            easein .5 ypos -105
            repeat


image Jubes_Sex_Zero_Anim_S3:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,75)
        block:
            ease .2 ypos -70
            easeout .5 ypos 0
            easein .5 ypos 75
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True




image Jubes_Sex_Body_S4:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,10)
        block:
            pause 0.1
            ease 0.2 ypos 0
            pause 0.2
            ease 1.7 ypos 10
            repeat

image Jubes_Sex_Legs_S4:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -15
            easeout 0.45 ypos -10
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_S4", "Jubes_SexMask")
        subpixel True
        pos (525,475)
        block:
            pause 0.05
            ease 0.2 ypos 460
            easeout 0.45 ypos 465
            easein 1.5 ypos 475
            repeat
    contains:

        ConditionSwitch(
                "not JubesX.spunk['pussy']", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (-15,-105)
        block:
            pause 0.05
            ease 0.2 ypos -120
            easeout 0.45 ypos -115
            easein 1.5 ypos -105
            repeat


image Jubes_Sex_Zero_Anim_S4:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,-60)
        block:
            ease .2 ypos -70
            easeout .5 ypos -68
            easein 1.5 ypos -60
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True







image Jubes_Sex_Body_A0:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Jubes_Sex_Legs_A0:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.6
            easeout 0.8 ypos -2
            easein 0.2 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_A0", "Jubes_AnalMask")
        subpixel True
        pos (533,587)
        block:
            pause 0.6
            easeout 0.8 ypos 585
            easein 0.2 ypos 582
            easeout 0.5 ypos 583
            easein 0.9 ypos 587
            repeat


image Jubes_Sex_Zero_Anim_A0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,115)
        block:
            ease 1.5 ypos 110
            pause .5
            ease 1.0 ypos 115
            repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True






image Jubes_Sex_Body_A1:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Jubes_Sex_Legs_A1:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.6
            easeout 0.8 ypos -2
            easein 0.2 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_A1", "Jubes_AnalMask")
        subpixel True
        pos (538,583)
        block:
            pause 0.6
            easeout 0.8 ypos 581
            easein 0.2 ypos 578
            easeout 0.5 ypos 579
            easein 0.9 ypos 583
            repeat


image Jubes_Sex_Zero_Anim_A1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,115)
        block:
            easeout 1.2 ypos 100
            easein .3 ypos 90
            easeout .5 ypos 100
            easein 1 ypos 115
            repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True




image Jubes_Sex_Body_A2:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.3
            ease 0.3 ypos -20
            pause 0.20
            ease 1.70 ypos 20
            repeat

image Jubes_Sex_Legs_A2:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.25
            ease 0.3 ypos -35
            easeout 0.45 ypos -30
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_A2", "Jubes_AnalMask")
        subpixel True
        pos (538,580)
        block:
            pause 0.25
            ease 0.3 ypos 545
            easeout 0.45 ypos 550
            easein 1.5 ypos 580
            repeat
    contains:

        ConditionSwitch(
                "not JubesX.spunk['anus']", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (0,0)
        block:
            pause 0.25
            ease 0.3 ypos -35
            easeout 0.45 ypos -30
            easein 1.5 ypos 0
            repeat


image Jubes_Sex_Zero_Anim_A2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,75)
        block:
            ease .5 ypos -50
            easeout 1.5 ypos 60
            easein .5 ypos 75
            repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True




image Jubes_Sex_Body_A3:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease 0.2 ypos -50
            pause 0.2
            ease .7 ypos 00
            repeat

image Jubes_Sex_Legs_A3:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -55
            easeout 0.45 ypos -40
            easein .5 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_A3", "Jubes_AnalMask")
        subpixel True
        pos (538,580)
        block:
            pause 0.05
            ease 0.2 ypos 525
            easeout 0.45 ypos 540
            easein .5 ypos 580
            repeat
    contains:

        ConditionSwitch(
                "not JubesX.spunk['anus']", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -55
            easeout 0.45 ypos -40
            easein .5 ypos 0
            repeat


image Jubes_Sex_Zero_Anim_A3:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,75)
        block:
            ease .2 ypos -70
            easeout .7 ypos 0
            easein .3 ypos 75
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True




image Jubes_Sex_Body_A4:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,20)
        block:
            pause 0.1
            ease 0.2 ypos 00
            pause 0.2
            ease 1.7 ypos 20
            repeat

image Jubes_Sex_Legs_A4:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -15
            easeout 0.45 ypos -10
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Jubes_Sex_Zero_Anim_A4", "Jubes_AnalMask")
        subpixel True
        pos (538,583)
        block:
            pause 0.05
            ease 0.2 ypos 568
            easeout 0.45 ypos 573
            easein 1.5 ypos 583
            repeat
    contains:

        ConditionSwitch(
                "not JubesX.spunk['anus']", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -15
            easeout 0.45 ypos -10
            easein 1.5 ypos 0
            repeat


image Jubes_Sex_Zero_Anim_A4:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        pos (125,-60)
        block:
            ease .2 ypos -70
            easeout .5 ypos -68
            easein 1.5 ypos -60
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True





image Jubes_Sex_Body_H0:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Jubes_Sex_Legs_H0:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.6
            easeout 0.8 ypos -2
            easein 0.2 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        "Jubes_Sex_Zero_Anim_H0"

        subpixel True
        pos (558,580)
        block:
            pause 0.6
            easeout 0.8 ypos 578
            easein 0.2 ypos 575
            easeout 0.5 ypos 576
            easein 0.9 ypos 580
            repeat


image Jubes_Sex_Zero_Anim_H0:

    contains:
        subpixel True
        ConditionSwitch(
            "Player.sprite", "Zero_Doggy_Insert",
            "True", Null(),
            )


        zoom 1.7
        pos (125,115)
        alpha 0.8
        block:
            ease 1.5 ypos 110
            pause .5
            ease 1.0 ypos 115
            repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True





image Jubes_Sex_Body_H1:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Jubes_Sex_Legs_H1:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.6
            ease 1 ypos -10
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        "Jubes_Sex_Zero_Anim_H1"

        subpixel True
        pos (558,580)
        block:
            pause 0.6
            ease 1 ypos 570
            easeout 0.5 ypos 576
            easein 0.9 ypos 580
            repeat


image Jubes_Sex_Zero_Anim_H1:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        alpha 0.8
        pos (125,250)
        block:
            ease 1.5 ypos 90
            pause .5
            ease 1.0 ypos 250
            repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True





image Jubes_Sex_Body_H2:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause .3
            ease .5 ypos -5
            pause 0.3
            ease .4 ypos 0
            repeat

image Jubes_Sex_Legs_H2:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease .25 ypos -20
            easeout 0.15 ypos -18
            easein 0.25 ypos 0
            repeat
    contains:
        "Jubes_Sex_Zero_Anim_H2"

        subpixel True
        pos (558,580)
        block:
            pause 0.1
            ease .25 ypos 560
            easeout 0.15 ypos 562
            easein 0.25 ypos 580
            repeat


image Jubes_Sex_Zero_Anim_H2:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        zoom 1.7
        alpha 0.8
        pos (125,230)
        block:
            ease .25 ypos 150
            easeout 0.25 ypos 170
            easein 0.25 ypos 230
            repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True




image Jubes_AnalMask:
    transform_anchor True
    contains:
        "images/JubesSex/Jubes_Sex_MaskAnalX.png"
        pos (200,366)
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)





image Jubes_Footjob_Foot:

    contains:

        ConditionSwitch(
            "JubesX.outfit['hose'] == '_stockings_and_garterbelt' or JubesX.outfit['hose'] == '_stockings'", "images/JubesSex/Jubes_Sex_Stockings_Foot.png",
            "JubesX.outfit['hose'] == '_black_stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Foot.png",
            "True", "images/JubesSex/Jubes_Sex_Foot.png"
            )
    contains:

        ConditionSwitch(
            "JubesX.upskirt", Null(),
            "JubesX.outfit['bottom'] == '_leather_pants'", "images/JubesSex/Jubes_Sex_Pants_Foot.png",
            "True", Null(),
            )
    offset (1105,140)
    zoom 1

image Jubes_Sex_Zero_Anim_F:

    "Zero_blowjob_cock"
    zoom .7
    anchor (0.5, 0.9)
    offset (270,650)
    rotate 0



image Jubes_Sex_Body_F0:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat
    yoffset -100

image Jubes_Sex_Legs_F0:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.6
            easeout 0.8 ypos -2
            easein 0.2 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:

        "Jubes_Footjob_Foot"
        subpixel True
        anchor (1100,140)
        transform_anchor True
        pos (0,0)
        rotate 0
        parallel:
            pause 0.6
            easeout 0.8 ypos -2
            easein 0.2 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
        parallel:
            ease 2 rotate 5
            ease 2 rotate -5
            pause .5
            repeat
    contains:
        "Jubes_Sex_Zero_Anim_F"
        subpixel True
        transform_anchor True
        pos (558,580)
        rotate -5
        parallel:
            pause 0.6
            easeout 0.8 ypos 578
            easein 0.2 ypos 575
            easeout 0.5 ypos 576
            easein 0.9 ypos 580
            repeat
        parallel:
            easeout 1 rotate -5
            easein 1 rotate -10
            pause .2
            easeout .8 rotate -5
            easein 1 rotate 0
            pause .5
            repeat

    yoffset -100








image Jubes_Sex_Body_F1:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat
    yoffset -100

image Jubes_Sex_Legs_F1:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.6
            easeout 0.8 ypos -2
            easein 0.2 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        "Jubes_Sex_Zero_Anim_F"
        subpixel True
        transform_anchor True
        pos (558,580)
        rotate -5
        parallel:
            pause 0.6
            easeout 0.8 ypos 578
            easein 0.2 ypos 575
            easeout 0.5 ypos 576
            easein 0.9 ypos 580
            repeat
        parallel:
            easeout 1 rotate -20
            easein 1 rotate -28
            pause .2
            easeout .8 rotate -20
            easein 1 rotate -5
            pause .5
            repeat
    contains:

        "Jubes_Footjob_Foot"
        subpixel True
        anchor (1100,140)
        transform_anchor True
        pos (0,0)
        rotate 0
        parallel:
            pause 0.6
            easeout 0.8 ypos -2
            easein 0.2 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
        parallel:
            ease 2 rotate 20
            ease 2 rotate 0
            pause .5
            repeat

    yoffset -100







image Jubes_Sex_Body_F2:

    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            ease .7 ypos -10
            ease .7 ypos 0
            repeat
    rotate 15
    yoffset -250
    xoffset 500
    xzoom -1

image Jubes_Sex_Legs_F2:

    contains:

        "Jubes_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            ease 0.5 ypos -2
            ease 1 ypos -10
            pause .1
            repeat
    contains:
        "Jubes_Sex_Zero_Anim_F"
        subpixel True
        transform_anchor True
        pos (808,380)
        rotate -55
        parallel:
            easeout .25 rotate -58
            easein .25 rotate -60
            pause .1
            easeout .4 rotate -58
            easein .5 rotate -55
            pause .1
            repeat
    contains:

        "Jubes_Footjob_Foot"
        subpixel True
        anchor (1100,140)
        transform_anchor True
        pos (0,0)
        rotate 0
        parallel:
            pause 0.15
            easeout 0.2 ypos -2
            easein 0.05 ypos -5
            easeout 0.25 ypos -4
            easein 0.45 ypos 0
            repeat
        parallel:
            ease .5 rotate 20
            ease 1 rotate 0
            pause .1
            repeat

    yoffset -400
    xoffset 300
    rotate 50










image Jubes_SexMaskX:
    transform_anchor True
    contains:
        "images/JubesSex/Jubes_Sex_MaskPussyX.png"
        pos (200,303)
        anchor (.5,.5)
    zoom 1

    anchor (0.5,0.5)


image Jubes_Sex_Zero_AnimX:

    contains:
        Solid("#159457", xysize=(401,606))
        alpha 0.9
    contains:
        subpixel True

        "Zero_Doggy_Insert"

        zoom 1.6
        alpha 0.5
        pos (130,100)
        block:

            ease 1.25 ypos -50
            ease 1.25 ypos 100
            repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True



image Jubes_Mega_Mask2:

    contains:
        "images/JubesSex/Jubes_Sex_PussyMaskTest2.png"






















    transform_anchor True
    zoom 1
    rotate 30





image Jubes_Mega_Mask:

    contains:
        "images/JubesSex/Jubes_Sex_PussyMaskTestB.png"




        alpha .5









    transform_anchor True
    zoom 1
    rotate 30




label Jubes_Sex_Launch(Line=primary_action):
    return
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action
    $ Player.sprite = 1
    $ Line = "solo" if not Line else Line
    if Line == "sex":
        $ Player.cock_position = "in"
        if offhand_action in ("fondle pussy","dildo pussy","lick pussy"):
            $ offhand_action = 0
    elif Line == "anal":
        $ Player.cock_position = "anal"
        if offhand_action in ("insert ass","dildo anal","lick ass"):
            $ offhand_action = 0
    elif Line == "solo":
        $ Player.sprite = 0
        $ Player.cock_position = "out"
    elif Line == "hotdog":
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

    if JubesX.pose == "doggy":
        call Jubes_Doggy_Launch (Line)
        return
    if renpy.showing("Jubes_SexSprite"):
        return
    call hide_girl(JubesX, hide_sprite = True)
    $ action_speed = 0

    if primary_action == "in" or primary_action == "anal":
        if JubesX.outfit['bottom'] or JubesX.hose_number() >= 5:
            $ JubesX.upskirt = 1
        if JubesX.outfit['underwear']:
            $ JubesX.underwear_pulled_down = 1

    show Jubes_SexSprite zorder 150:
        pos (450,500)
    with dissolve
    return

label Jubes_Sex_Reset:
    if renpy.showing("Jubes_Doggy_Animation"):
        call Jubes_Doggy_Reset
        return
    if not renpy.showing("Jubes_SexSprite"):
        return
    $ JubesX.arm_pose = 2
    hide Jubes_SexSprite
    call hide_girl(JubesX)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return












image Jubes_BJ_Animation:

    contains:
        ConditionSwitch(



            "action_speed == 1", "Jubes_BJ_Body_1",
            "action_speed == 2", "Jubes_BJ_Body_2",
            "action_speed == 3", "Jubes_BJ_Body_3",
            "action_speed == 4", "Jubes_BJ_Body_4",
            "action_speed == 5", "Jubes_BJ_Body_5",
            "action_speed == 6", "Jubes_BJ_Body_6",


            "True","Jubes_BJ_Body_0",
            )
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)














image Jubes_Sprite_BJ_HairBack:


    ConditionSwitch(

            "not JubesX.outfit['hair']", Null(),
            "JubesX.outfit['hair'] == '_wet' or JubesX.wet", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Under.png",
            "JubesX.outfit['hair']", "images/JubesSprite/Jubes_Sprite_Hair_Long_Under.png",
            "True", Null(),
            )

image Jubes_Sprite_BJ_Head:

    LiveComposite(
        (806,806),
        (0,0), ConditionSwitch(

                "JubesX.blushing == '_blush2'", "images/JubesSprite/Jubes_Sprite_Head_Blush2.png",
                "JubesX.blushing", "images/JubesSprite/Jubes_Sprite_Head_Blush.png",
                "True", "images/JubesSprite/Jubes_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "not JubesX.spunk['chin']", Null(),
            "action_speed >= 2", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(
            "action_speed >= 2", "images/JubesSprite/Jubes_Sprite_mouth_SuckingBJ.png",
            "action_speed == 1", "images/JubesSprite/Jubes_Sprite_mouth_Tongue.png",
            "JubesX.mouth == '_normal'", "images/JubesSprite/Jubes_Sprite_mouth_Normal.png",
            "JubesX.mouth == '_lipbite'", "images/JubesSprite/Jubes_Sprite_mouth_Lipbite.png",
            "JubesX.mouth == '_sucking'", "images/JubesSprite/Jubes_Sprite_mouth_Sucking.png",
            "JubesX.mouth == '_kiss'", "images/JubesSprite/Jubes_Sprite_mouth_Kiss.png",
            "JubesX.mouth == '_sad'", "images/JubesSprite/Jubes_Sprite_mouth_Sad.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_mouth_Smile.png",
            "JubesX.mouth == '_surprised'", "images/JubesSprite/Jubes_Sprite_mouth_Surprised.png",
            "JubesX.mouth == '_tongue'", "images/JubesSprite/Jubes_Sprite_mouth_Tongue.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_mouth_Smile.png",
            "JubesX.mouth == '_smirk'", "images/JubesSprite/Jubes_Sprite_mouth_Smirk.png",

            "True", "images/JubesSprite/Jubes_Sprite_mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "not JubesX.spunk['mouth']", Null(),
            "action_speed >= 2", "images/JubesSprite/Jubes_Sprite_Spunk_mouthSuck.png",
            "action_speed == 1", "images/JubesSprite/Jubes_Sprite_Spunk_mouthTongue.png",
            "JubesX.mouth == '_normal'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthNeutral.png",
            "JubesX.mouth == '_lipbite'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthSmirk.png",
            "JubesX.mouth == '_sucking'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthTongue.png",
            "JubesX.mouth == '_kiss'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthKiss.png",
            "JubesX.mouth == '_sad'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthSad.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthSmile.png",
            "JubesX.mouth == '_surprised'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthSad.png",
            "JubesX.mouth == '_tongue'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthTongue.png",
            "JubesX.mouth == '_smile'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthSmile.png",
            "JubesX.mouth == '_smirk'", "images/JubesSprite/Jubes_Sprite_Spunk_mouthSmirk.png",
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_mouthNeutral.png",
            ),
        (0,0), ConditionSwitch(
            "action_speed >= 2 and JubesX.spunk[mouth]", "images/JubesSprite/Jubes_Sprite_SpunkSuckingO.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "action_speed == 1", "images/JubesSprite/Jubes_Sprite_Wet_Tongue.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "JubesX.blushing == '_blush2'", ConditionSwitch(
                    "JubesX.brows == '_normal'", "images/JubesSprite/Jubes_Sprite_brows_Normal_B.png",
                    "JubesX.brows == '_angry'", "images/JubesSprite/Jubes_Sprite_brows_Angry_B.png",
                    "JubesX.brows == '_sad'", "images/JubesSprite/Jubes_Sprite_brows_Sad_B.png",
                    "JubesX.brows == '_surprised'", "images/JubesSprite/Jubes_Sprite_brows_Surprised_B.png",
                    "JubesX.brows == '_confused'", "images/JubesSprite/Jubes_Sprite_brows_Confused_B.png",
                    "True", "images/JubesSprite/Jubes_Sprite_brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "JubesX.brows == '_normal'", "images/JubesSprite/Jubes_Sprite_brows_Normal.png",
                    "JubesX.brows == '_angry'", "images/JubesSprite/Jubes_Sprite_brows_Angry.png",
                    "JubesX.brows == '_sad'", "images/JubesSprite/Jubes_Sprite_brows_Sad.png",
                    "JubesX.brows == '_surprised'", "images/JubesSprite/Jubes_Sprite_brows_Surprised.png",
                    "JubesX.brows == '_confused'", "images/JubesSprite/Jubes_Sprite_brows_Confused.png",
                    "True", "images/JubesSprite/Jubes_Sprite_brows_Normal.png",
                    ),
            ),
        (0,0), "Jubes Blink",
        (0,0), ConditionSwitch(

            "JubesX.outfit['top'] == '_jacket'", Null(),
            "JubesX.outfit['hair'] == '_wet' or JubesX.wet", Null(),
            "JubesX.outfit['hair']", "images/JubesSprite/Jubes_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "not JubesX.outfit['hair']", Null(),
            "JubesX.outfit['hair'] == '_wet' or JubesX.wet", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Over.png",
            "JubesX.outfit['hair']", "images/JubesSprite/Jubes_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not JubesX.wet", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Head_Wet.png",

            ),
        (0,0), ConditionSwitch(

            "JubesX.spunk['hair']", "images/JubesSprite/Jubes_Sprite_Spunk_Facial2.png",
            "JubesX.spunk['face']", "images/JubesSprite/Jubes_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )



image Jubes_BlowCock_Mask:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)





















image Jubes_BJ_Body_0:

    contains:

        "Jubes_Sprite_BJ_HairBack"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (490,400)
        rotate 0
        parallel:
            ease 1.1 ypos 405
            pause 0.2
            ease 1.1 ypos 400
            pause 0.2
            repeat
    contains:

        "Jubes_Sprite"
        subpixel True
        pos (650,800)
        zoom 2.2
        anchor (0.5, 0.5)
        rotate -20
        parallel:
            pause 0.1
            ease 1.1 ypos 810
            pause 0.2
            ease 1 ypos 800
            pause 0.1
            repeat
    contains:

        subpixel True
        "Jubes_Sprite_BJ_Head"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (490,400)
        rotate 0
        parallel:
            ease 1.1 ypos 405
            pause 0.2
            ease 1.1 ypos 400
            pause 0.2
            repeat
    contains:





        AlphaMask("Zero_blowjob_cock", "Jubes_BlowCock_Mask")
        subpixel True
        pos (412,292)
        zoom 0.4
        alpha 1
        rotate 10
        parallel:
            pause 0.1

            ease .15 rotate -5
            pause 0.4
            ease 1.95 rotate 10
            repeat
        parallel:
            pause 0.1

            ease .15 pos (405,255)
            pause 0.4
            ease 1.95 pos (420,292)
            repeat



image Jubes_BJ_Body_1:

    contains:

        "Jubes_Sprite_BJ_HairBack"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (535,340)
        rotate -30
        parallel:
            pause 0.1
            ease 1.4 rotate -50
            pause 0.3
            ease 1.4 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout 1.2 xpos 470
            easein .2 xpos 460
            pause 0.3
            easeout .75 xpos 500
            easein .65 xpos 535
            repeat
        parallel:
            pause 0.1
            ease 1.4 ypos 500
            pause 0.3
            ease 1.4 ypos 340
            repeat
    contains:

        "Jubes_Sprite"
        pos (673,740)
        zoom 2.2
        anchor (0.5, 0.5)
        rotate -20
        subpixel True
        parallel:
            pause 0.15
            ease 1.25 rotate -40
            pause 0.45
            ease 1.35 rotate -20
            repeat
        parallel:
            pause 0.15
            easeout .9 xpos 740
            easein .35 xpos 740
            pause 0.5
            easeout .65 xpos 710
            easein .65 xpos 673
            repeat
        parallel:
            pause 0.15
            ease 1.25 ypos 830
            pause 0.45
            ease 1.35 ypos 740
            repeat
    contains:

        subpixel True
        "Jubes_Sprite_BJ_Head"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (535,340)
        rotate -30
        parallel:
            pause 0.1
            ease 1.4 rotate -50
            pause 0.3
            ease 1.4 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout 1.2 xpos 470
            easein .2 xpos 460
            pause 0.3
            easeout .75 xpos 500
            easein .65 xpos 535
            repeat
        parallel:
            pause 0.1
            ease 1.4 ypos 500
            pause 0.3
            ease 1.4 ypos 340
            repeat
    contains:





        AlphaMask("Zero_blowjob_cock", "Jubes_BlowCock_Mask")
        subpixel True
        pos (412,292)
        zoom 0.4
        alpha 1
        rotate 10
        parallel:
            pause 0.1
            easeout 1.2 rotate 1
            easein .3 rotate -1
            pause 0.4
            ease 1.2 rotate 10
            repeat
        parallel:
            pause 0.1
            easeout 1.2 pos (407,262)
            easein .3 pos (405,255)
            pause 0.4
            ease 1.2 pos (412,292)
            repeat


image Jubes_BJ_Body_2:

    contains:

        "Jubes_Sprite_BJ_HairBack"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (530,355)
        rotate -30
        parallel:
            pause 0.1
            easeout 1.2 rotate -40
            ease .6 rotate -32
            pause 0.1
            ease 1.2 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout 1.2 xpos 510
            ease .7 xpos 520
            pause 0.1
            ease 1.1 xpos 530
            repeat
        parallel:
            pause 0.1
            ease 1.6 ypos 400
            pause 0.1
            ease 1.4 ypos 355
            repeat
    contains:

        "Jubes_Sprite"
        pos (680,755)
        zoom 2.2
        anchor (0.5, 0.5)
        rotate -20
        subpixel True
        parallel:
            pause 0.15
            ease 1.55 rotate -30
            pause 0.15
            ease 1.35 rotate -20
            repeat
        parallel:
            pause 0.15
            ease 1.35 xpos 730
            pause 0.25
            ease 1.45 xpos 680
            repeat
        parallel:
            pause 0.15
            ease 1.55 ypos 780
            pause 0.15
            ease 1.35 ypos 755
            repeat
    contains:

        subpixel True
        "Jubes_Sprite_BJ_Head"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (530,355)
        rotate -30
        parallel:
            pause 0.1
            easeout 1.2 rotate -40
            ease .6 rotate -32
            pause 0.1
            ease 1.2 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout 1.2 xpos 510
            ease .7 xpos 520
            pause 0.1
            ease 1.1 xpos 530
            repeat
        parallel:
            pause 0.1
            ease 1.6 ypos 400
            pause 0.1
            ease 1.4 ypos 355
            repeat
    contains:





        AlphaMask("Zero_blowjob_cock", "Jubes_BlowCock_Mask")
        subpixel True
        pos (412,292)
        zoom 0.4
        alpha 1
        rotate 10
        parallel:
            pause 1.3
            ease .4 rotate 8
            pause .2
            ease 1 rotate 10
            pause .3
            repeat
        parallel:
            pause 1.3
            ease .4 pos (410,285)
            pause .2
            ease 1 pos (412,292)
            pause .3
            repeat
    contains:

        subpixel True
        AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
        zoom 0.81
        anchor (0.5, 0.5)
        pos (530,355)
        rotate -30
        parallel:
            pause 0.1
            easeout 1.2 rotate -40
            ease .6 rotate -32
            pause 0.1
            ease 1.2 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout 1.2 xpos 510
            ease .7 xpos 520
            pause 0.1
            ease 1.1 xpos 530
            repeat
        parallel:
            pause 0.1
            ease 1.6 ypos 400
            pause 0.1
            ease 1.4 ypos 355
            repeat




image Jubes_BlowCock_Mask_3:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,100)







image Jubes_BJ_Body_3:

    contains:

        "Jubes_Sprite_BJ_HairBack"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (523,380)
        rotate -30
        parallel:

            ease .7 rotate -50

            ease 1 rotate -30
            repeat
        parallel:

            easeout .3 xpos 500
            easein .4 xpos 481

            easeout .55 xpos 500
            easein .45 xpos 523
            repeat
        parallel:

            ease .7 ypos 450

            ease 1 ypos 380
            repeat
    contains:

        "Jubes_Sprite"
        pos (673,780)
        zoom 2.2
        anchor (0.5, 0.5)
        rotate -20
        subpixel True
        parallel:

            ease .7 rotate -40

            ease 1.0 rotate -20
            repeat
        parallel:

            easeout .3 xpos 710
            easein .4 xpos 760

            easeout .55 xpos 710
            easein .45 xpos 673
            repeat
        parallel:

            ease .7 ypos 780

            ease 1.0 ypos 780
            repeat
    contains:

        subpixel True
        "Jubes_Sprite_BJ_Head"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (523,380)
        rotate -30
        parallel:

            ease .7 rotate -50

            ease 1 rotate -30
            repeat
        parallel:

            easeout .3 xpos 500
            easein .4 xpos 481

            easeout .55 xpos 500
            easein .45 xpos 523
            repeat
        parallel:

            ease .7 ypos 450

            ease 1 ypos 380
            repeat
    contains:





        AlphaMask("Zero_blowjob_cock", "Jubes_BlowCock_Mask_3")
        subpixel True
        pos (412,292)
        zoom 0.4
        alpha 1
        rotate 10
        parallel:

            ease .7 rotate 0

            ease 1 rotate 10
            repeat
        parallel:

            ease .7 pos (407,262)

            ease 1 pos (412,292)
            repeat
    contains:

        subpixel True
        AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
        zoom 0.81
        anchor (0.5, 0.5)
        pos (523,380)
        rotate -30
        parallel:

            ease .7 rotate -50

            ease 1 rotate -30
            repeat
        parallel:

            easeout .3 xpos 500
            easein .4 xpos 481

            easeout .55 xpos 500
            easein .45 xpos 523
            repeat
        parallel:

            ease .7 ypos 450

            ease 1 ypos 380
            repeat



image Jubes_BlowCock_Mask_4:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)
        block:
            pause 0.1
            ease 1.6 offset (0,300)
            pause 0.1
            ease 1.4 offset (0,0)
            repeat

image Jubes_BJ_Body_4:

    contains:

        "Jubes_Sprite_BJ_HairBack"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (523,380)
        rotate -30
        parallel:
            pause 0.1
            ease 1.6 rotate -50
            pause 0.1
            ease 1.4 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout .7 xpos 500
            easein .9 xpos 481
            pause 0.1
            easeout .75 xpos 500
            easein .65 xpos 523
            repeat
        parallel:
            pause 0.1
            ease 1.6 ypos 500
            pause 0.1
            ease 1.4 ypos 380
            repeat
    contains:

        "Jubes_Sprite"
        pos (673,780)
        zoom 2.2
        anchor (0.5, 0.5)
        rotate -20
        subpixel True
        parallel:
            pause 0.15
            ease 1.55 rotate -40
            pause 0.15
            ease 1.35 rotate -20
            repeat
        parallel:
            pause 0.15
            easeout .65 xpos 710
            easein .9 xpos 760
            pause 0.15
            easeout .70 xpos 710
            easein .65 xpos 673
            repeat
        parallel:
            pause 0.15
            ease 1.55 ypos 830
            pause 0.15
            ease 1.35 ypos 780
            repeat
    contains:

        subpixel True
        "Jubes_Sprite_BJ_Head"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (523,380)
        rotate -30
        parallel:
            pause 0.1
            ease 1.6 rotate -50
            pause 0.1
            ease 1.4 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout .7 xpos 500
            easein .9 xpos 481
            pause 0.1
            easeout .75 xpos 500
            easein .65 xpos 523
            repeat
        parallel:
            pause 0.1
            ease 1.6 ypos 500
            pause 0.1
            ease 1.4 ypos 380
            repeat
    contains:





        AlphaMask("Zero_blowjob_cock", "Jubes_BlowCock_Mask_4")
        subpixel True
        pos (412,292)
        zoom 0.4
        alpha 1
        rotate 10
        parallel:
            pause 0.1
            ease 1.6 rotate 0
            pause 0.1
            ease 1.4 rotate 10
            repeat
        parallel:
            pause 0.1
            ease 1.6 pos (407,262)
            pause 0.1
            ease 1.4 pos (412,292)
            repeat
    contains:

        subpixel True
        AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
        zoom 0.81
        anchor (0.5, 0.5)
        pos (523,380)
        rotate -30
        parallel:
            pause 0.1
            ease 1.6 rotate -50
            pause 0.1
            ease 1.4 rotate -30
            repeat
        parallel:
            pause 0.1
            easeout .7 xpos 500
            easein .9 xpos 481
            pause 0.1
            easeout .75 xpos 500
            easein .65 xpos 523
            repeat
        parallel:
            pause 0.1
            ease 1.6 ypos 500
            pause 0.1
            ease 1.4 ypos 380
            repeat



image Jubes_BJ_Body_5:

    contains:

        "Jubes_Sprite_BJ_HairBack"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (520,375)
        rotate -50
        parallel:
            pause 1
            ease .3 rotate -30
            easeout .3 rotate -32
            easein .5 rotate -35
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 530
            easeout .3 xpos 525
            easein .5 xpos 520
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 355
            easeout .3 ypos 365
            easein .5 ypos 375
            pause .5
            repeat
    contains:

        "Jubes_Sprite"
        subpixel True
        zoom 2.2
        anchor (0.5, 0.5)
        rotate -30
        pos (730,760)
        parallel:
            pause 1
            ease .3 rotate -26
            easeout .3 rotate -28
            easein .5 rotate -30
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 710
            easeout .3 xpos 720
            easein .5 xpos 730
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 750
            easeout .3 ypos 755
            easein .5 ypos 760
            pause .5
            repeat
    contains:

        subpixel True
        "Jubes_Sprite_BJ_Head"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (520,375)
        rotate -35
        parallel:
            pause 1
            ease .3 rotate -30
            easeout .3 rotate -32
            easein .5 rotate -35
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 530
            easeout .3 xpos 525
            easein .5 xpos 520
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 355
            easeout .3 ypos 365
            easein .5 ypos 375
            pause .5
            repeat
    contains:





        AlphaMask("Zero_blowjob_cock", "Jubes_BlowCock_Mask")
        subpixel True
        pos (410,292)
        zoom 0.4
        alpha 1
        rotate 12
        parallel:
            pause 1
            ease .3 rotate 10
            ease .3 rotate 12
            pause 1
            repeat
        parallel:
            pause 1
            ease .3 pos (412,285)
            ease .3 pos (410,292)
            pause 1
            repeat
    contains:

        subpixel True
        AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
        zoom 0.81
        anchor (0.5, 0.5)
        pos (520,375)
        rotate -35
        parallel:
            pause 1
            ease .3 rotate -30
            easeout .3 rotate -32
            easein .5 rotate -35
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 530
            easeout .3 xpos 525
            easein .5 xpos 520
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 355
            easeout .3 ypos 365
            easein .5 ypos 375
            pause .5
            repeat


image Jubes_BlowCock_Mask_6:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,300)







image Jubes_BJ_Body_6:

    contains:

        "Jubes_Sprite_BJ_HairBack"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (481,500)
        rotate -50
        parallel:
            pause 1
            ease .3 rotate -45
            easeout .3 rotate -48
            easein .5 rotate -50
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 490
            easeout .3 xpos 485
            easein .5 xpos 481
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 490
            easeout .3 ypos 496
            easein .5 ypos 500
            pause .5
            repeat
    contains:

        "Jubes_Sprite"
        subpixel True
        zoom 2.2
        anchor (0.5, 0.5)
        rotate -40
        pos (760,830)
        parallel:
            pause 1
            ease .3 rotate -38
            easeout .3 rotate -39
            easein .5 rotate -40
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 750
            easeout .3 xpos 756
            easein .5 xpos 760
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 835
            easeout .3 ypos 830
            easein .5 ypos 830
            pause .5
            repeat
    contains:

        subpixel True
        "Jubes_Sprite_BJ_Head"
        zoom 0.81
        anchor (0.5, 0.5)
        pos (481,500)
        rotate -50
        parallel:
            pause 1
            ease .3 rotate -45
            easeout .3 rotate -48
            easein .5 rotate -50
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 490
            easeout .3 xpos 485
            easein .5 xpos 481
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 490
            easeout .3 ypos 496
            easein .5 ypos 500
            pause .5
            repeat
    contains:





        AlphaMask("Zero_blowjob_cock", "Jubes_BlowCock_Mask_6")
        subpixel True
        pos (407,262)
        zoom 0.4
        alpha 1
        rotate 0
        parallel:
            pause 1
            ease .3 rotate 2
            ease .3 rotate 0
            pause 1
            repeat
        parallel:
            pause 1
            ease .3 pos (409,268)
            ease .3 pos (407,262)
            pause 1
            repeat
    contains:

        subpixel True
        AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
        zoom 0.81
        anchor (0.5, 0.5)
        pos (481,500)
        rotate -50
        parallel:
            pause 1
            ease .3 rotate -45
            easeout .3 rotate -48
            easein .5 rotate -50
            pause .5
            repeat
        parallel:
            pause 1
            easein .3 xpos 490
            easeout .3 xpos 485
            easein .5 xpos 481
            pause .5
            repeat
        parallel:
            pause 1
            ease .3 ypos 490
            easeout .3 ypos 496
            easein .5 ypos 500
            pause .5
            repeat







label Jubes_BJ_Launch(Line=primary_action):
    return

    $ JubesX.arm_pose = 1
    if renpy.showing("Jubes_BJ_Animation"):
        return

    call hide_girl(JubesX)
    if Line == "L" or Line == "cum":
        show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_center):
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    $ action_speed = 0
    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != JubesX:
                    "[JubesX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != JubesX:
                    "[JubesX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[JubesX.name] casually glances around to see if anyone can see her."
        "[JubesX.name] smoothly bends down and places your cock against her cheek."

    if Line != "cum":
        $ primary_action = "blowjob"

    show Jubes_Sprite zorder JubesX.sprite_layer:
        alpha 0
    show Jubes_BJ_Animation zorder 150:
        pos (645,510)
    return

label Jubes_BJ_Reset:
    if not renpy.showing("Jubes_BJ_Animation"):
        return

    call hide_girl(JubesX)
    $ action_speed = 0

    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Jubes_Sprite zorder JubesX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return








image Jubes_Hand_Under:
    "images/JubesSprite/handjubes2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Jubes_Hand_Over:
    "images/JubesSprite/handjubes1.png"
    anchor (0.5,0.5)
    pos (-10,0)

transform Jubes_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5
        pause 0.1
        repeat

transform Jubes_Hand_2():
    subpixel True
    pos (-15,-120)
    rotate 10
    block:
        ease 0.2 pos (-15,0) rotate 0
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10
        pause 0.1
        repeat

transform Handcock_3():
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

transform Handcock_4():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

transform Handcock_1L():
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

transform Handcock_2L():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Jubes_HJ_Animation:
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jubes_Hand_Under"),
            "action_speed == 1", At("Jubes_Hand_Under", Jubes_Hand_1()),
            "action_speed >= 2", At("Jubes_Hand_Under", Jubes_Hand_2()),
            "action_speed", Null(),
            ),
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1L()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2L()),
            "action_speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Jubes_Hand_Over"),
            "action_speed == 1", At("Jubes_Hand_Over", Jubes_Hand_1()),
            "action_speed >= 2", At("Jubes_Hand_Over", Jubes_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Jubes_HJ_Launch(Line=primary_action):
    return
    if renpy.showing("Jubes_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call hide_girl(JubesX)
    if Line == "L":
        show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)
    else:
        show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)
        with dissolve

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause .5
    $ JubesX.arm_pose = 1
    show Jubes_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:

        offset (250,250)
    return

label Jubes_HJ_Reset:
    if not renpy.showing("Jubes_HJ_Animation"):
        return
    $ action_speed = 0
    $ JubesX.arm_pose = 1
    hide Jubes_HJ_Animation with easeoutbottom
    call hide_girl(JubesX)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        zoom 1.7 offset (-50,200)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return










image Jubes_TJ_Animation:

    contains:
        ConditionSwitch(

                    "not Player.sprite","Jubes_TJ_0",
                    "action_speed == 1", "Jubes_TJ_1",
                    "action_speed == 4", "Jubes_TJ_4",
                    "action_speed == 5", "Jubes_TJ_5",
                    "action_speed >= 2", "Jubes_TJ_2",
                    "True",       "Jubes_TJ_0",
                    )
    zoom .7
    transform_anchor True
    anchor (.5,.5)




image Jubes_TJ_HairBack:

    "Jubes_Sprite_HairBack"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    offset (320,100)
    rotate 0

image Jubes_TJ_Head:

    "Jubes_Sprite_Head"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    offset (320,100)
    rotate 0

image Jubes_TJ_HairMid:

    "Jubes_Sprite_HairMid"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    rotate 20
    offset (320,100)
    rotate 0

image Jubes_TJ_HairTop:

    "Jubes_Sprite_HairTop"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    offset (320,100)
    rotate 0

image Jubes_TJ_ZeroCock:

    "Zero_blowjob_cock"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (220,670)
    rotate 0

image Jubes_TJ_Body:

    contains:
        "images/JubesSex/Jubes_Titjob_Body.png"
    contains:
        ConditionSwitch(
                        "not JubesX.outfit['neck']",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Neck_[JubesX.outfit['neck']].png",
                        )
    contains:
        ConditionSwitch(
                        "not JubesX.spunk['breasts']",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Spunk_Chest.png",
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)
    offset (410,770)
    rotate 0


image Jubes_TJ_LeftArm:

    contains:
        "images/JubesSex/Jubes_Titjob_LeftHand.png"
    contains:
        ConditionSwitch(
                        "not JubesX.outfit['gloves']",Null(),
                        "JubesX.outfit['gloves'] == '_gloves'",       "images/JubesSex/Jubes_Titjob_LeftGlove.png",
                        "True",       "images/JubesSex/Jubes_Titjob_wrists.png",
                        )
    contains:

        ConditionSwitch(
                        "not JubesX.outfit['front_inner_accessory']",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Left_[JubesX.outfit['front_inner_accessory']].png",
                        )

image Jubes_TJ_RightArm:

    contains:
        "images/JubesSex/Jubes_Titjob_RightHand.png"
    contains:
        ConditionSwitch(
                        "JubesX.outfit['gloves'] == '_gloves'",       "images/JubesSex/Jubes_Titjob_RightGlove.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not JubesX.outfit['front_inner_accessory']",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Right_[JubesX.outfit['front_inner_accessory']].png",
                        )

image Jubes_TJ_RightArmBack:

    contains:
        "images/JubesSex/Jubes_Titjob_RightHandBack.png"
    contains:
        ConditionSwitch(
                        "JubesX.outfit['gloves'] == '_gloves'",       "images/JubesSex/Jubes_Titjob_RightGloveBack.png",
                        "True", Null(),
                        )




image Jubes_TJ_0:

    contains:

        "Jubes_TJ_HairBack"
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

        "Jubes_TJ_Body"
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

        "Jubes_TJ_RightArmBack"
        subpixel True
        pos (0,-15)
        transform_anchor True
        parallel:
            ease 2 ypos -5
            pause .1
            ease 2 ypos -15
            pause .1
            repeat
    contains:
        contains:
            "images/JubesSex/Jubes_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
        subpixel True
        pos (0,-15)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos -5
            pause .1
            ease 2 ypos -15
            repeat
    contains:









        "Jubes_TJ_RightArm"
        subpixel True
        pos (0,-15)
        transform_anchor True
        parallel:
            ease 2 ypos -5
            pause .1
            ease 2 ypos -15
            pause .1
            repeat
    contains:

        "Jubes_TJ_Head"
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

        subpixel True
        "Jubes_TJ_ZeroCock"
        pos (0,30)
        transform_anchor True
        rotate -2
        parallel:
            ease 2 rotate -2
            pause .1
            ease 2 rotate 3
            pause .1
            repeat
    contains:

        contains:
            "images/JubesSex/Jubes_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            pause .1
            ease 2 ypos -40
            pause .1
            ease 2 ypos 0
            repeat
    contains:

        "Jubes_TJ_LeftArm"








        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -40
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Jubes_TJ_HairMid"
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

        "Jubes_TJ_HairTop"
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




image Jubes_TJ_1:

    contains:

        "Jubes_TJ_HairBack"
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

        "Jubes_TJ_Body"
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

        "Jubes_TJ_RightArmBack"
        subpixel True
        pos (0,150)
        transform_anchor True
        block:
            ease 2 ypos -20
            pause .4
            ease 1.8 ypos 150
            pause .5
            repeat
    contains:
        contains:
            "images/JubesSex/Jubes_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
        subpixel True
        pos (0,150)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:









        "Jubes_TJ_RightArm"
        subpixel True
        pos (0,150)
        transform_anchor True
        block:
            ease 2 ypos -20
            pause .4
            ease 1.8 ypos 150
            pause .5
            repeat
    contains:

        "Jubes_TJ_Head"
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

        subpixel True
        "Jubes_TJ_ZeroCock"
        pos (0,25)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos 0
            pause .4
            ease 1.8 ypos 25
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        contains:
            "images/JubesSex/Jubes_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
        subpixel True
        pos (0,150)
        transform_anchor True
        block:
            pause .1
            ease 1.9 ypos -20
            pause .4
            ease 1.8 ypos 150
            ease .5 ypos 140
            repeat
    contains:

        "Jubes_TJ_LeftArm"
        subpixel True
        pos (0,150)
        transform_anchor True
        block:
            ease 2 ypos -20
            pause .4
            ease 1.8 ypos 150
            pause .5
            repeat
    contains:

        "Jubes_TJ_HairMid"
        subpixel True
        pos (0,160)
        transform_anchor True
        rotate -5
        parallel:
            ease 2 ypos -20
            pause .4
            ease 1.8 ypos 160
            pause .5
            repeat
        parallel:
            ease 2 rotate 0
            pause .2
            ease 2 rotate -5
            pause .5
            repeat
    contains:

        "Jubes_TJ_HairTop"
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




image Jubes_TJ_2:

    contains:

        "Jubes_TJ_HairBack"
        subpixel True
        pos (0,80)
        transform_anchor True
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

        "Jubes_TJ_Body"
        subpixel True
        pos (0,80)
        transform_anchor True
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
    contains:

        "Jubes_TJ_RightArmBack"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 1 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:
        contains:
            "images/JubesSex/Jubes_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
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









        "Jubes_TJ_RightArm"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 1 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        "Jubes_TJ_Head"
        subpixel True
        pos (0,80)
        transform_anchor True
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

        subpixel True
        "Jubes_TJ_ZeroCock"
        pos (0,30)
        transform_anchor True
        rotate -2
        parallel:
            ease 1 ypos 0
            pause .2
            ease .4 ypos 30
            repeat
        parallel:
            ease 1 rotate 0
            pause .1
            ease .5 rotate -2
            repeat
    contains:

        contains:
            "images/JubesSex/Jubes_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
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

        "Jubes_TJ_LeftArm"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 1 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        "Jubes_TJ_HairMid"
        subpixel True
        pos (0,90)
        transform_anchor True
        rotate -5
        parallel:
            ease 1 ypos -40
            pause .2
            ease .4 ypos 90
            repeat
        parallel:
            ease 1 rotate 0
            pause .2
            ease .4 rotate -5
            repeat
    contains:

        "Jubes_TJ_HairTop"
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




image Jubes_TJ_4:

    contains:

        "Jubes_TJ_HairBack"
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

        "Jubes_TJ_Body"
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

        "Jubes_TJ_RightArmBack"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -30
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:
        contains:
            "images/JubesSex/Jubes_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
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









        "Jubes_TJ_RightArm"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -30
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Jubes_TJ_Head"
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

        subpixel True
        "Jubes_TJ_ZeroCock"
        pos (0,20)
        transform_anchor True
        rotate 2
        parallel:
            ease 2 ypos 0
            pause .1
            ease 2 ypos 20
            pause .1
            repeat
    contains:

        contains:
            "images/JubesSex/Jubes_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
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

        "Jubes_TJ_LeftArm"
        subpixel True
        pos (0,0)
        transform_anchor True
        parallel:
            ease 2 ypos -30
            pause .1
            ease 2 ypos 0
            pause .1
            repeat
    contains:

        "Jubes_TJ_HairMid"
        subpixel True
        pos (0,0)
        transform_anchor True
        rotate 0
        parallel:
            ease 2 ypos -15
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

        "Jubes_TJ_HairTop"
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




image Jubes_TJ_5:

    contains:

        "Jubes_TJ_HairBack"
        subpixel True
        pos (-30,155)
        transform_anchor True
        rotate -20
        parallel:
            ease 2 ypos 140
            pause .1
            ease 2 ypos 155
            pause .1
            repeat
    contains:















        "Jubes_TJ_Body"
        subpixel True
        pos (185,70)
        transform_anchor True
        rotate -20
        parallel:
            ease 2 ypos 50
            pause .1
            ease 2 ypos 70
            pause .1
            repeat
    contains:

        contains:
            "Jubes_TJ_RightArmBack"
        subpixel True
        pos (-80,-180)
        transform_anchor True
        rotate -10
        parallel:
            ease 2 ypos -200
            pause .1
            ease 2 ypos -180
            pause .1
            repeat
    contains:

        contains:
            "images/JubesSex/Jubes_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
        subpixel True
        pos (-80,-160)
        transform_anchor True
        rotate -10
        parallel:
            ease .4 ypos -170
            ease 1.7 ypos -190
            pause .1
            ease 2 ypos -160
            repeat
    contains:









        "Jubes_TJ_RightArm"
        subpixel True
        pos (-80,-180)
        transform_anchor True
        rotate -10
        parallel:
            ease 2 ypos -200
            pause .1
            ease 2 ypos -180
            pause .1
            repeat
    contains:

        "Jubes_TJ_Head"
        subpixel True
        pos (-30,155)
        transform_anchor True
        rotate -20
        parallel:
            ease 2 ypos 140
            pause .1
            ease 2 ypos 155
            pause .1
            repeat
    contains:

        subpixel True
        "Jubes_TJ_ZeroCock"
        pos (0,20)
        transform_anchor True
        rotate 2
        parallel:
            ease 2 ypos 0
            pause .1
            ease 2 ypos 20
            pause .1
            repeat
    contains:

        contains:
            "images/JubesSex/Jubes_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not JubesX.spunk['breasts']",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
        subpixel True
        pos (-80,-160)
        transform_anchor True
        rotate -10
        parallel:
            ease .4 ypos -170
            ease 1.7 ypos -190
            pause .1
            ease 2 ypos -160
            repeat
    contains:

        "Jubes_TJ_LeftArm"
        subpixel True
        pos (-80,-180)
        transform_anchor True
        rotate -10
        parallel:
            ease 2 ypos -200
            pause .1
            ease 2 ypos -180
            pause .1
            repeat
    contains:

        "Jubes_TJ_HairMid"
        subpixel True
        pos (-30,115)
        transform_anchor True
        rotate -10
        parallel:
            ease 2 ypos 95
            pause .1
            ease 2 ypos 115
            pause .1
            repeat
    contains:

        "Jubes_TJ_HairTop"
        subpixel True
        pos (-30,155)
        transform_anchor True
        rotate -20
        parallel:
            ease 2 ypos 140
            pause .1
            ease 2 ypos 155
            pause .1
            repeat




label Jubes_TJ_Launch(Line=primary_action):
    return
    if renpy.showing("Jubes_TJ_Animation"):
        return
    call hide_girl(JubesX)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        ease 1 zoom 2.3 xpos 750 yoffset -100
    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != JubesX:
                    "[JubesX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != JubesX:
                    "[JubesX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[JubesX.name] casually glances around to see if anyone can see her."
        "[JubesX.name] bends over and places your cock between her breasts."

    if JubesX.outfit['bra'] and JubesX.outfit['top']:
        "She throws off her [JubesX.outfit['top']] and her [JubesX.outfit['bra']]."
    elif JubesX.outfit['top']:
        "She throws off her [JubesX.outfit['top']], baring her breasts underneath."
    elif JubesX.outfit['bra']:
        "She tugs off her [JubesX.outfit['bra']] and throws it aside."
    $ JubesX.outfit['top'] = 0
    $ JubesX.outfit['bra'] = 0
    $ JubesX.arm_pose = 0

    call Jubes_First_Topless

    show blackscreen onlayer black with dissolve
    show Jubes_Sprite zorder JubesX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Jubes_TJ_Animation zorder 150:
        pos (700,520)
    $ Player.sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Jubes_TJ_Reset:

    if not renpy.showing("Jubes_TJ_Animation"):
        return

    call hide_girl(JubesX)
    $ Player.sprite = 0

    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        zoom 2.3 xpos 750 yoffset -100
    show Jubes_Sprite zorder JubesX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos JubesX.sprite_location yoffset 0
    "[JubesX.name] pulls back"
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos JubesX.sprite_location
    return













label Jubes_Kissing_Launch(T=primary_action, Set=1):
    call hide_girl(JubesX)
    $ primary_action = T
    $ JubesX.pose = "kiss" if Set else JubesX.pose
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Jubes_Kissing_Smooch:
    $ JubesX.change_face("kiss")
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos JubesX.sprite_location zoom 1
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        zoom 1
    $ JubesX.change_face("_sexy")
    return

label Jubes_Breasts_Launch(T=primary_action, Set=1):
    call hide_girl(JubesX)
    $ primary_action = T
    $ JubesX.pose = "breasts" if Set else JubesX.pose
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Jubes_Middle_Launch(T=primary_action, Set=1):
    call hide_girl(JubesX)
    $ primary_action = T
    $ JubesX.pose = "mid" if Set else JubesX.pose
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Jubes_Pussy_Launch(T=primary_action, Set=1):
    call hide_girl(JubesX)
    $ primary_action = T
    $ JubesX.pose = "pussy" if Set else JubesX.pose
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Jubes_Pos_Reset(T=0, Set=0):
    if JubesX.location != bg_current:
        return
    call hide_girl(JubesX)
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location):
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Jubes_Sprite zorder JubesX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (JubesX.sprite_location,50)
    $ JubesX.pose = "full" if Set else 0
    $ primary_action = T
    return



image GropeLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (290,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (190,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat

image LickRightBreast_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (290,350)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (270,330)
            pause .5
            ease 1.5 rotate 30 pos (290,350)
            repeat

image LickLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (175,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (170,320)
            pause .5
            ease 1.5 rotate 30 pos (175,340)
            repeat

image GropeThigh_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (235,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (195,740)
            ease 1 rotate 100 pos (235,640)
            repeat

image GropePussy_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (260,580)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 ypos 565
                ease .75 rotate 170 ypos 580
            choice:
                ease .5 rotate 190 ypos 565
                pause .25
                ease 1 rotate 170 ypos 580
            repeat

image FingerPussy_Jubes:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (275,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (285,625)
                pause .5
                ease 1 rotate 50 pos (275,650)
            choice:
                ease .5 rotate 40 pos (285,625)
                pause .5
                ease 1.75 rotate 50 pos (275,650)
            choice:
                ease 2 rotate 40 pos (285,625)
                pause .5
                ease 1 rotate 50 pos (275,650)
            choice:
                ease .25 rotate 40 pos (285,625)
                ease .25 rotate 50 pos (275,650)
                ease .25 rotate 40 pos (285,625)
                ease .25 rotate 50 pos (275,650)
            repeat

image Lickpussy_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (285,610)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (275,590)
            linear .5 rotate -60 pos (265,600)
            easein 1 rotate 10 pos (285,610)
            repeat

image VibratorRightBreast_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (180,330)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            pause .25
            ease 1 rotate 35 ypos 320
            pause .25
            ease 1 rotate 55 ypos 330
            repeat

image VibratorLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (285,340)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1 rotate 35 ypos 330
            pause .25
            ease 1 rotate 55 ypos 340
            pause .25
            repeat

image VibratorPussy_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (285,600)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 pos (275,590)
            pause .25
            ease 1 rotate 70 pos (285,600)
            pause .25
            repeat

image VibratorAnal_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (305,590)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:






            ease 1 rotate 0 pos (295,580)
            pause .25
            ease 1 rotate 10 pos (305,590)
            pause .25
            repeat

image VibratorPussyInsert_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Jubes:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeBothBreast_Jubes:
    contains:
        "GirlGropeLeftBreast_Jubes"
    contains:
        "GirlGropeRightBreast_Jubes"

image GirlGropeLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 ypos 350
            ease 1 rotate -10 ypos 340
            repeat

image GirlGropeRightBreast_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (190,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -40 ypos 350
            ease 1 rotate -10 ypos 340
            repeat

image GirlGropeThigh_Jubes:
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

image GirlGropePussy_JubesSelf:
    contains:
        "GirlGropePussy_Jubes"
        anchor (0.5,0.5)
        rotate -40

        pos (180,525)

image GirlGropePussy_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (265,575)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 ypos 570
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 ypos 570
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 ypos 570
                ease .75 rotate 200 ypos 575
                ease .5 rotate 205 ypos 570
                ease .75 rotate 200 ypos 575
            choice:
                ease .3 rotate 205 ypos 570
                ease .3 rotate 200 ypos 580
                ease .3 rotate 205 ypos 570
                ease .3 rotate 200 ypos 580
            repeat

image GirlFingerPussy_Jubes:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (265,570)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 ypos 575
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 ypos 575
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 ypos 575
                ease .75 rotate 200 ypos 580
                ease .5 rotate 205 ypos 575
                ease .75 rotate 200 ypos 580
            choice:
                ease .3 rotate 205 ypos 575
                ease .3 rotate 200 ypos 585
                ease .3 rotate 205 ypos 575
                ease .3 rotate 200 ypos 585
            repeat



image Star1:
    "images/JubesSprite/Star_P.png"
    block:
        rotate 0
        ease 1 rotate 360
        repeat

image Star2:
    "images/JubesSprite/Star_B.png"
    block:
        rotate 0
        ease 1 rotate 360
        repeat

image Star3:
    "images/JubesSprite/Star_Y.png"
    block:
        rotate 0
        ease 1 rotate 360
        repeat

image Fireworks:

    contains:
        alpha 1
        anchor (0.5,0.5)
        transform_anchor True

        offset (0,0)
        pause .2
        choice:
            "Star1"
        choice:
            "Star2"
        choice:
            "Star3"
        parallel:

            pause 0.7
            ease 0.3 alpha 0
        parallel:
            offset (0,0)
            choice:
                parallel:

                    ease .5 offset (50,-100)
                    ease .5 offset (100,150)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1
            choice:
                parallel:

                    ease .5 offset (-25,-120)
                    ease .5 offset (-50,130)
                parallel:

                    zoom 0.2
                    ease 1 zoom .9
            choice:
                parallel:

                    ease .5 offset (25,-130)
                    ease .5 offset (50,140)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1.2
            choice:
                parallel:

                    ease .5 offset (10,-150)
                    ease .5 offset (20,140)
                parallel:

                    zoom 0.3
                    ease 1 zoom .9
            choice:
                parallel:

                    ease .5 offset (100,-100)
                    ease .5 offset (150,150)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1.2
    contains:

        alpha 1
        anchor (0.5,0.5)

        transform_anchor True
        pause .1
        choice:
            "Star1"
        choice:
            "Star2"
        choice:
            "Star3"
        parallel:

            pause 0.7
            ease 0.3 alpha 0
        parallel:
            offset (0,0)
            choice:
                parallel:

                    ease .5 offset (50,-100)
                    ease .5 offset (100,150)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1
            choice:
                parallel:

                    ease .5 offset (-25,-120)
                    ease .5 offset (-50,130)
                parallel:

                    zoom 0.2
                    ease 1 zoom .9
            choice:
                parallel:

                    ease .5 offset (25,-130)
                    ease .5 offset (50,140)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1.2
            choice:
                parallel:

                    ease .5 offset (10,-150)
                    ease .5 offset (20,140)
                parallel:

                    zoom 0.3
                    ease 1 zoom .9
            choice:
                parallel:

                    ease .5 offset (100,-100)
                    ease .5 offset (150,150)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1.2
    contains:

        alpha 1
        anchor (0.5,0.5)

        transform_anchor True
        choice:
            "Star1"
        choice:
            "Star2"
        choice:
            "Star3"
        parallel:

            pause 0.7
            ease 0.3 alpha 0
        parallel:
            offset (0,0)
            choice:
                parallel:

                    ease .5 offset (50,-100)
                    ease .5 offset (100,150)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1
            choice:
                parallel:

                    ease .5 offset (-25,-120)
                    ease .5 offset (-50,130)
                parallel:

                    zoom 0.2
                    ease 1 zoom .9
            choice:
                parallel:

                    ease .5 offset (25,-130)
                    ease .5 offset (50,140)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1.2
            choice:
                parallel:

                    ease .5 offset (10,-150)
                    ease .5 offset (20,140)
                parallel:

                    zoom 0.3
                    ease 1 zoom .9
            choice:
                parallel:

                    ease .5 offset (100,-100)
                    ease .5 offset (150,150)
                parallel:

                    zoom 0.3
                    ease 1 zoom 1.2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
