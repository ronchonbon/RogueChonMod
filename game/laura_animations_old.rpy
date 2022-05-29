

image Laura_sprite standing:
    LiveComposite(
        (402,965),
        (0,0), "Laura_Sprite_HairBack",
        (0,0), ConditionSwitch(

            "not LauraX.outfit['underwear'] or not LauraX.underwear_pulled_down or (LauraX.outfit['bottom'] and LauraX.outfit['bottom'] != '_skirt' and not LauraX.upskirt)", Null(),
            "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png",
            "LauraX.outfit['underwear'] == '_bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Back.png",
            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['gloves'] == '_gloves' and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Glove_Back2.png",
            "LauraX.outfit['gloves'] == '_gloves'", "images/LauraSprite/Laura_Sprite_Glove_Back1.png",
            "LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",
            "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png",
            ),





        (0,0), ConditionSwitch(

            "LauraX.top_pulled_up and LauraX.outfit['top'] == '_jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back_Up.png",
            "LauraX.outfit['top'] == '_jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png",
            "True", Null(),
            ),

        (0,0), "images/LauraSprite/Laura_Sprite_Body.png",


        (0,0), ConditionSwitch(

            "LauraX.outfit['gloves'] == '_gloves' and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Glove_Mid2.png",
            "LauraX.outfit['gloves'] == '_gloves'", "images/LauraSprite/Laura_Sprite_Glove_Mid1.png",
            "LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",
            "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png",
            ),

        (0,0), "images/LauraSprite/Laura_Sprite_Tits.png",
        (0,0), ConditionSwitch(

            "LauraX.wet and LauraX.arm_pose == 1", "images/LauraSprite/Laura_Sprite_Water1.png",
            "LauraX.wet", "images/LauraSprite/Laura_Sprite_Water2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['gloves'] == '_wrists' and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png",
            "LauraX.outfit['gloves'] == '_wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png",
            "True", Null(),
            ),


        (145,560), ConditionSwitch(

            "not LauraX.grool", Null(),
            "LauraX.outfit['bottom'] and LauraX.outfit['bottom'] != '_skirt' and not LauraX.upskirt", Null(),
            "LauraX.outfit['bottom'] and LauraX.outfit['bottom'] != '_cosplay_skirt' and not LauraX.upskirt", Null(),
            "LauraX.outfit['underwear'] and not LauraX.underwear_pulled_down and LauraX.grool <= 1", Null(),
            "LauraX.grool == 1", ConditionSwitch(
                    "LauraX.outfit['underwear'] and LauraX.underwear_pulled_down", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "LauraX.outfit['bottom'] and LauraX.outfit['bottom'] != '_skirt'", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Laura_Drip_Mask"),
                    ),
            "True", ConditionSwitch(
                    "LauraX.outfit['underwear'] and LauraX.underwear_pulled_down", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.outfit['bottom'] and LauraX.outfit['bottom'] != '_skirt'", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.outfit['underwear']", AlphaMask("Wet_Drip","Laura_Drip_Mask"),
                    "True", AlphaMask("Wet_Drip2","Laura_Drip_Mask"),
                    ),
            ),
        (145,560), ConditionSwitch(

            "not LauraX.spunk['pussy'] and not LauraX.spunk['anus']", Null(),
            "LauraX.outfit['bottom'] and LauraX.outfit['bottom'] != '_skirt' and not LauraX.upskirt", Null(),
            "LauraX.outfit['bottom'] and LauraX.outfit['bottom'] != '_cosplay_skirt' and not LauraX.upskirt", Null(),
            "LauraX.outfit['underwear'] and not LauraX.underwear_pulled_down and LauraX.grool <= 1", Null(),
            "True", ConditionSwitch(
                    "LauraX.outfit['underwear'] and LauraX.underwear_pulled_down", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"),

                    "LauraX.outfit['underwear']", AlphaMask("Spunk_Drip","Laura_Drip_Mask"),
                    "True", AlphaMask("Spunk_Drip2","Laura_Drip_Mask"),
                    ),
            ),
        (0,0), ConditionSwitch(

            "LauraX.pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.outfit['piercings']", Null(),
            "LauraX.outfit['underwear'] and not LauraX.underwear_pulled_down", Null(),
            "LauraX.outfit['bottom'] != '_skirt' and LauraX.outfit['bottom'] and not LauraX.upskirt", Null(),
            "LauraX.outfit['bottom'] != '_cosplay_skirt' and LauraX.outfit['bottom'] and not LauraX.upskirt", Null(),
            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Pussy.png",
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraSprite/Laura_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['hose'] == '_black_stockings'", "images/LauraSprite/Laura_Sprite_BlackStockings.png",
            "LauraX.outfit['hose'] == '_stockings' or LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt' or LauraX.outfit['hose'] == '_garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.outfit['underwear']", Null(),
            "LauraX.underwear_pulled_down", ConditionSwitch(

                    "not LauraX.outfit['bottom'] or LauraX.upskirt or LauraX.outfit['bottom'] == '_skirt'", ConditionSwitch(

                            "LauraX.outfit['underwear'] == '_wolvie_panties' and LauraX.grool", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png",
                            "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",
                            "LauraX.outfit['underwear'] == '_lace_panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png",
                            "LauraX.outfit['underwear'] == '_bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Down.png",
                            "True", "images/LauraSprite/Laura_Sprite_Panties_Leather_Down.png",
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "LauraX.grool", ConditionSwitch(

                        "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
                        "LauraX.outfit['underwear'] == '_lace_panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png",
                        "LauraX.outfit['underwear'] == '_bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png",
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png",
                        ),
                    "True", ConditionSwitch(

                        "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
                        "LauraX.outfit['underwear'] == '_lace_panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png",
                        "LauraX.outfit['underwear'] == '_bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png",
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png",
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.outfit['bottom']", Null(),
            "LauraX.upskirt", ConditionSwitch(

                        "LauraX.outfit['bottom'] == '_cosplay_skirt'", "images/LauraSprite/Laura_Sprite_SkirtCos_Up.png",
                        "LauraX.outfit['bottom'] == '_skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(

                    "LauraX.outfit['bottom'] == '_cosplay_skirt'", "images/LauraSprite/Laura_Sprite_SkirtCos.png",
                    "LauraX.outfit['bottom'] == '_skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png",
                    "LauraX.grool", ConditionSwitch(

                        "LauraX.outfit['bottom'] == '_leather_pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",
                        "LauraX.outfit['bottom'] == '_mesh_pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",

                        "True", Null(),
                        ),
                    "True", ConditionSwitch(

                        "LauraX.outfit['bottom'] == '_leather_pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",
                        "LauraX.outfit['bottom'] == '_mesh_pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",

                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['bottom'] == '_skirt' or LauraX.outfit['bottom'] == '_cosplay_skirt'", Null(),
            "LauraX.outfit['piercings'] == '_barbell'", ConditionSwitch(

                    "LauraX.outfit['bottom'] and not LauraX.upskirt", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",
                    "LauraX.outfit['underwear'] and not LauraX.underwear_pulled_down", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "LauraX.outfit['piercings'] == '_ring'", ConditionSwitch(

                    "LauraX.outfit['bottom'] and not LauraX.upskirt", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",
                    "LauraX.outfit['underwear'] and not LauraX.underwear_pulled_down", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.grool", Null(),
            "LauraX.outfit['bottom'] and LauraX.grool <= 1", Null(),
            "LauraX.outfit['bottom'] == '_cosplay_skirt'", Null(),
            "LauraX.outfit['bottom'] == '_skirt'", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Wetness.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['bottom'] and not LauraX.upskirt", Null(),
            "LauraX.spunk['pussy'] or LauraX.spunk['anus']", "images/LauraSprite/Laura_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not LauraX.outfit['piercings']", Null(),
            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Tits.png",
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraSprite/Laura_Sprite_Ring_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['neck'] == '_leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.outfit['bra'] == '_white_tank'", "images/LauraSprite/Laura_Sprite_Bra_White_Up.png",
                    "LauraX.outfit['bra'] == '_leather_bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather_Up.png",
                    "LauraX.outfit['bra'] == '_wolvie_top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie_Up.png",
                    "LauraX.outfit['bra'] == '_bikini_top'", "images/LauraSprite/Laura_Sprite_Top_Bikini_Up.png",
                    "LauraX.outfit['bra'] == '_corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Up.png",
                    "LauraX.outfit['bra'] == '_lace_corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace_Up.png",
                    "True", Null(),
                    ),
            "LauraX.outfit['bra'] == '_white_tank'", "images/LauraSprite/Laura_Sprite_Bra_White.png",
            "LauraX.outfit['bra'] == '_leather_bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png",
            "LauraX.outfit['bra'] == '_wolvie_top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",
            "LauraX.outfit['bra'] == '_bikini_top'", "images/LauraSprite/Laura_Sprite_Top_Bikini.png",
            "LauraX.outfit['bra'] == '_corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",
            "LauraX.outfit['bra'] == '_lace_corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not LauraX.outfit['bottom'] or LauraX.upskirt", Null(),
            "LauraX.outfit['suspenders'] == '_suspenders' and not LauraX.outfit['bra'] and not LauraX.top_pulled_up", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png",
            "LauraX.outfit['suspenders'] == '_suspenders2'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png",
            "LauraX.outfit['suspenders'] == '_suspenders'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.outfit['top'] == '_jacket' and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2_Up.png",
                    "LauraX.outfit['top'] == '_jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1_Up.png",

                    "True", Null(),
                    ),
            "LauraX.outfit['top'] == '_jacket' and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png",
            "LauraX.outfit['top'] == '_jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png",
            "LauraX.outfit['top'] == '_towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.outfit['piercings'] or (not LauraX.outfit['top'] and not LauraX.outfit['bra'])", Null(),
            "LauraX.outfit['top'] == '_jacket'", Null(),
            "LauraX.outfit['piercings'] == '_barbell'",  "images/LauraSprite/Laura_Sprite_Barbell_TitsC.png",
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraSprite/Laura_Sprite_Ring_TitsC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "LauraX.spunk['belly']", "images/LauraSprite/Laura_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.spunk['breasts']", "images/LauraSprite/Laura_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "renpy.showing('Laura_sprite blowjob')", Null(),
            "True", "Laura_Sprite_Head",
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['gloves'] == '_gloves' and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Glove_Top2.png",
            "LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.wet and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Water2top.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.arm_pose == 2 and LauraX.outfit['gloves'] == '_wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['top'] == '_jacket' and LauraX.arm_pose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.arm_pose == 2 and LauraX.claws", "images/LauraSprite/Laura_Sprite_Claws2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "LauraX.arm_pose == 2 or not LauraX.spunk['hand']", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Hand.png",
            ),








        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != LauraX", Null(),


            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_LauraSelf",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck_breasts'", "GirlGropeLeftBreast_Laura",

                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeRightBreast_Laura",

                    "True", "GirlGropeBothBreast_Laura",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Laura",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Laura",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Laura",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Laura",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_offhand_action or second_girl_primary_action != 'masturbation' or focused_Girl == LauraX", Null(),


            "second_girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and LauraX.lust >= 70", "GirlFingerPussy_Laura",
            "second_girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Laura",
            "second_girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Laura",
            "second_girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(


            "not primary_action or focused_Girl != LauraX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Laura",
            "primary_action == 'fondle_thighs'", "GropeThigh_Laura",
            "primary_action == 'fondle_breasts'", "GropeLeftBreast_Laura",
            "primary_action == 'suck_breasts'", "LickRightBreast_Laura",
            "primary_action == 'fondle_pussy' and action_speed == 2", "FingerPussy_Laura",
            "primary_action == 'fondle_pussy'", "GropePussy_Laura",
            "primary_action == 'eat_pussy'", "Lickpussy_Laura",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Laura",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "primary_action == 'vibrator anal'", "VibratorAnal_Laura",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Laura",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not offhand_action or focused_Girl != LauraX", Null(),


            "offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' and primary_action == 'suck_breasts'", "GropeLeftBreast_Laura",

                    "True", "GropeRightBreast_Laura",

                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck_breasts'", "VibratorLeftBreast_Laura",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck_breasts'", "LickLeftBreast_Laura",
            "offhand_action == 'fondle_pussy'", "GropePussy_Laura",
            "offhand_action == 'eat_pussy'", "Lickpussy_Laura",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Laura",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Laura",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Laura",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Laura",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Laura",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_primary_action or focused_Girl != LauraX", Null(),


            "second_girl_primary_action == 'fondle_pussy' and primary_action != 'sex' and LauraX.lust >= 70", "GirlFingerPussy_Laura",
            "second_girl_primary_action == 'fondle_pussy'", "GirlGropePussy_Laura",
            "second_girl_primary_action == 'eat_pussy'", "Lickpussy_Laura",
            "second_girl_primary_action == 'suck_breasts' and (offhand_action != 'suck_breasts' or primary_action == 'suck_breasts')", "LickLeftBreast_Laura",
            "second_girl_primary_action == 'suck_breasts'", "LickRightBreast_Laura",
            "second_girl_primary_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeLeftBreast_Laura",


                    "True", "GirlGropeRightBreast_Laura",
                    ),
            "second_girl_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_primary_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action != 'lesbian' or focused_Girl == LauraX or not girl_offhand_action", Null(),


            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and LauraX.lust >= 70", "GirlFingerPussy_Laura",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Laura",
            "girl_offhand_action == 'eat_pussy'", "Lickpussy_Laura",
            "girl_offhand_action == 'suck_breasts' and (offhand_action != 'suck_breasts' or primary_action == 'suck_breasts')", "LickLeftBreast_Laura",
            "girl_offhand_action == 'suck_breasts'", "LickRightBreast_Laura",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck_breasts'", "GirlGropeLeftBreast_Laura",

                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck_breasts'", "GirlGropeRightBreast_Laura",

                    "girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck_breasts'", "GirlGropeLeftBreast_Laura",

                    "True", "GirlGropeRightBreast_Laura",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        )
    anchor (0.5, -0.15) zoom 1.0

image Laura_Sprite_HairBack:
    ConditionSwitch(

            "not LauraX.outfit['hair']", Null(),
            "renpy.showing('Laura_sprite blowjob')", Null(),

            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",
            "True", Null(),
            ),

    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_HairMid:
    ConditionSwitch(

            "not LauraX.outfit['hair']", Null(),
            "renpy.showing('Laura_sprite blowjob')", Null(),

            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", Null(),
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),
    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_HairTop:
    ConditionSwitch(

            "not LauraX.outfit['hair']", Null(),
            "renpy.showing('Laura_sprite sex')", "images/LauraSex/Laura_Sprite_Hair_Long_OverSex.png",
            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),

    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_Head:
    LiveComposite(
        (806,806),
        (0,0), ConditionSwitch(

                "renpy.showing('Laura_sprite sex')", "images/LauraSex/Laura_Sprite_Hair_Long_UnderSex.png",
                "True", Null(),
                ),
        (0,0), ConditionSwitch(

                "LauraX.blushing == '_blush2'", "images/LauraSprite/Laura_Sprite_Head_Blush2.png",
                "LauraX.blushing", "images/LauraSprite/Laura_Sprite_Head_Blush.png",
                "True", "images/LauraSprite/Laura_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "not LauraX.spunk['chin']", Null(),
            "renpy.showing('Laura_sprite blowjob') and action_speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(
            "renpy.showing('Laura_sprite blowjob')", "images/LauraSprite/Laura_Sprite_mouth_SuckingBJ.png",
            "LauraX.mouth == '_normal'", "images/LauraSprite/Laura_Sprite_mouth_Normal.png",
            "LauraX.mouth == '_lipbite'", "images/LauraSprite/Laura_Sprite_mouth_Lipbite.png",
            "LauraX.mouth == '_sucking'", "images/LauraSprite/Laura_Sprite_mouth_Sucking.png",
            "LauraX.mouth == '_kiss'", "images/LauraSprite/Laura_Sprite_mouth_Kiss.png",
            "LauraX.mouth == '_sad'", "images/LauraSprite/Laura_Sprite_mouth_Sad.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_mouth_Smile.png",
            "LauraX.mouth == '_surprised'", "images/LauraSprite/Laura_Sprite_mouth_Surprised.png",
            "LauraX.mouth == '_tongue'", "images/LauraSprite/Laura_Sprite_mouth_Tongue.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_mouth_Smile.png",
            "LauraX.mouth == '_smirk'", "images/LauraSprite/Laura_Sprite_mouth_Smirk.png",

            "True", "images/LauraSprite/Laura_Sprite_mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "not LauraX.spunk['mouth']", Null(),
            "renpy.showing('Laura_sprite blowjob')", "images/LauraSprite/Laura_Sprite_Spunk_mouthSuck.png",
            "LauraX.mouth == '_normal'", "images/LauraSprite/Laura_Sprite_Spunk_mouthNeutral.png",
            "LauraX.mouth == '_lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmirk.png",
            "LauraX.mouth == '_sucking'", "images/LauraSprite/Laura_Sprite_Spunk_mouthTongue.png",
            "LauraX.mouth == '_kiss'", "images/LauraSprite/Laura_Sprite_Spunk_mouthKiss.png",
            "LauraX.mouth == '_sad'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSad.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmile.png",
            "LauraX.mouth == '_surprised'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSad.png",
            "LauraX.mouth == '_tongue'", "images/LauraSprite/Laura_Sprite_Spunk_mouthTongue.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmile.png",
            "LauraX.mouth == '_smirk'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmirk.png",
            "True", "images/LauraSprite/Laura_Sprite_Spunk_mouthNeutral.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.blushing == '_blush2'", ConditionSwitch(
                    "LauraX.brows == '_normal'", "images/LauraSprite/Laura_Sprite_brows_Normal_B.png",
                    "LauraX.brows == '_angry'", "images/LauraSprite/Laura_Sprite_brows_Angry_B.png",
                    "LauraX.brows == '_sad'", "images/LauraSprite/Laura_Sprite_brows_Sad_B.png",
                    "LauraX.brows == '_surprised'", "images/LauraSprite/Laura_Sprite_brows_Surprised_B.png",
                    "LauraX.brows == '_confused'", "images/LauraSprite/Laura_Sprite_brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.brows == '_normal'", "images/LauraSprite/Laura_Sprite_brows_Normal.png",
                    "LauraX.brows == '_angry'", "images/LauraSprite/Laura_Sprite_brows_Angry.png",
                    "LauraX.brows == '_sad'", "images/LauraSprite/Laura_Sprite_brows_Sad.png",
                    "LauraX.brows == '_surprised'", "images/LauraSprite/Laura_Sprite_brows_Surprised.png",
                    "LauraX.brows == '_confused'", "images/LauraSprite/Laura_Sprite_brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_brows_Normal.png",
                    ),
            ),
        (0,0), "Laura_blinking",
        (0,0), ConditionSwitch(

            "LauraX.outfit['top'] == '_jacket'", Null(),
            "renpy.showing('Laura_sprite titjob')", Null(),
            "renpy.showing('Laura_Sex_Animation')", Null(),
            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", Null(),
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "not LauraX.outfit['hair']", Null(),
            "renpy.showing('Laura_sprite titjob')", Null(),
            "renpy.showing('Laura_sprite sex')", "images/LauraSex/Laura_Sprite_Hair_Long_OverSex.png",
            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.wet", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",

            ),
        (0,0), ConditionSwitch(

            "LauraX.spunk['hair']", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",
            "LauraX.spunk['face']", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom .5



image Laura_Squint:
    "images/LauraSprite/Laura_Sprite_eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/LauraSprite/Laura_Sprite_eyes_Squint.png"
    .25
    repeat



image Laura_Drip_Mask:

    contains:
        "images/LauraSprite/Laura_Sprite_WetMask.png"
        offset (-145,-560)

image Laura_Drip_MaskP:

    contains:
        "images/LauraSprite/Laura_Sprite_WetMaskP.png"
        offset (-145,-560)











image Laura_sprite doggy:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Laura_Doggy_Body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Top",
                    "action_speed > 1", "Laura_Doggy_Fuck_Top",
                    "action_speed", "Laura_Doggy_Anal_Head_Top",
                    "True", "Laura_Doggy_Body",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Top",
                    "action_speed > 1", "Laura_Doggy_Fuck_Top",
                    "True", "Laura_Doggy_Body",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Laura_Doggy_Foot2_Top",
                    "action_speed", "Laura_Doggy_Foot1_Top",
                    "True", "Laura_Doggy_Foot0_Top",
                    ),
            "True", "Laura_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Laura_Doggy_Ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Laura_Doggy_Fuck_Ass",
                    "action_speed", "Laura_Doggy_Anal_Head_Ass",
                    "True", "Laura_Doggy_Ass",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Laura_Doggy_Fuck_Ass",
                    "True", "Laura_Doggy_Ass",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Laura_Doggy_Foot2_Ass",
                    "action_speed", "Laura_Doggy_Foot1_Ass",
                    "True", "Laura_Doggy_Foot0_Ass",
                    ),
            "True", "Laura_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.cock_position == 'footjob'", ConditionSwitch(
                    "action_speed > 1", "Laura_Doggy_Feet2",
                    "action_speed", "Laura_Doggy_Feet1",
                    "True", "Laura_Doggy_Feet0",
                    ),
            "not Player.sprite and show_feet", "Laura_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)



image Laura_Doggy_Body:
    LiveComposite(

        (610,750),

        (0,60), "Laura_Doggy_Head",



        (0,0), "images/LauraDoggy/Laura_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "not LauraX.outfit['bra']", Null(),









            "LauraX.outfit['bra'] == '_white_tank'", "images/LauraDoggy/Laura_Doggy_Chest_Costume.png",
            "LauraX.outfit['bra'] == '_lace_corset'", "images/LauraDoggy/Laura_Doggy_Chest_Corset.png",
            "LauraX.outfit['bra'] == '_corset'", "images/LauraDoggy/Laura_Doggy_Chest_Corset.png",
            "LauraX.outfit['bra'] == '_wolvie_top'", "images/LauraDoggy/Laura_Doggy_Chest_Wolvie.png",
            "LauraX.outfit['bra'] == '_bikini_top'", "images/LauraDoggy/Laura_Doggy_Chest_Bikini.png",
            "True", "images/LauraDoggy/Laura_Doggy_Chest_Tank.png",
            ),





        (0,0), ConditionSwitch(

            "not LauraX.outfit['bottom']", Null(),
            "LauraX.outfit['suspenders'] == '_suspenders'", "images/LauraDoggy/Laura_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['gloves'] == '_gloves'", "images/LauraDoggy/Laura_Doggy_Gloves.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.outfit['top']", Null(),
            "LauraX.outfit['top'] == '_jacket'", "images/LauraDoggy/Laura_Doggy_Over_Jacket.png",
            "LauraX.outfit['top'] == '_towel' and not LauraX.top_pulled_up", "images/LauraDoggy/Laura_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.spunk['back']", "images/LauraDoggy/Laura_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Laura_Doggy_GropeBreast",
            "True", Null()
            ),


        )


    offset (-200,0)




image Laura_Doggy_Head:
    LiveComposite(

        (420,525),


        (0,0), ConditionSwitch(

            "LauraX.wet or LauraX.outfit['hair'] == '_wet'", "images/LauraDoggy/Laura_Doggy_Hair_Wet_Back.png",
            "True", "images/LauraDoggy/Laura_Doggy_Hair_Long_Back.png",
            ),
        (0,0), ConditionSwitch(


            "LauraX.blushing", "images/LauraDoggy/Laura_Doggy_Head_Blush.png",
            "True", "images/LauraDoggy/Laura_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.mouth == '_normal'", "images/LauraDoggy/Laura_Doggy_mouth_Smile.png",
            "LauraX.mouth == '_lipbite'", "images/LauraDoggy/Laura_Doggy_mouth_Smile.png",
            "LauraX.mouth == '_sucking'", "images/LauraDoggy/Laura_Doggy_mouth_Open.png",
            "LauraX.mouth == '_kiss'", "images/LauraDoggy/Laura_Doggy_mouth_Kiss.png",
            "LauraX.mouth == '_sad'", "images/LauraDoggy/Laura_Doggy_mouth_Sad.png",
            "LauraX.mouth == '_smile'", "images/LauraDoggy/Laura_Doggy_mouth_Smile.png",
            "LauraX.mouth == '_smile'", "images/LauraDoggy/Laura_Doggy_mouth_Smile.png",
            "LauraX.mouth == '_surprised'", "images/LauraDoggy/Laura_Doggy_mouth_Open.png",
            "LauraX.mouth == '_tongue'", "images/LauraDoggy/Laura_Doggy_mouth_Tongue.png",
            "True", "images/LauraDoggy/Laura_Doggy_mouth_Smile.png",
            ),



















        (0,0), ConditionSwitch(


            "LauraX.brows == '_angry'", "images/LauraDoggy/Laura_Doggy_brows_Angry.png",
            "LauraX.brows == '_sad'", "images/LauraDoggy/Laura_Doggy_brows_Sad.png",
            "LauraX.brows == '_surprised'", "images/LauraDoggy/Laura_Doggy_brows_Surprised.png",

            "True", "images/LauraDoggy/Laura_Doggy_brows_Normal.png",
            ),
        (0,0), "Laura_sprite Doggy Blink",





        (0,0), ConditionSwitch(

            "LauraX.spunk['face']", "images/LauraDoggy/Laura_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.wet or LauraX.outfit['hair'] == '_wet'", "images/LauraDoggy/Laura_Doggy_Hair_Wet.png",
            "True", "images/LauraDoggy/Laura_Doggy_Hair_Long.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.spunk['hair']", "images/LauraDoggy/Laura_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )

































image Laura_sprite Doggy Blink:

    ConditionSwitch(
        "LauraX.eyes == '_sexy'", "images/LauraDoggy/Laura_Doggy_eyes_Sexy.png",
        "LauraX.eyes == '_side'", "images/LauraDoggy/Laura_Doggy_eyes_Side.png",
        "LauraX.eyes == '_normal'", "images/LauraDoggy/Laura_Doggy_eyes_Sexy.png",
        "LauraX.eyes == '_closed'", "images/LauraDoggy/Laura_Doggy_eyes_Closed.png",
        "LauraX.eyes == '_manic'", "images/LauraDoggy/Laura_Doggy_eyes_Stunned.png",
        "LauraX.eyes == '_down'", "images/LauraDoggy/Laura_Doggy_eyes_Sexy.png",
        "LauraX.eyes == '_stunned'", "images/LauraDoggy/Laura_Doggy_eyes_Stunned.png",
        "LauraX.eyes == '_surprised'", "images/LauraDoggy/Laura_Doggy_eyes_Surprised.png",
        "LauraX.eyes == '_squint'", "images/LauraDoggy/Laura_Doggy_eyes_Sexy.png",
        "True", "images/LauraDoggy/Laura_Doggy_eyes_Normal.png",
        ),






    3

    "images/LauraDoggy/Laura_Doggy_eyes_Closed.png"
    .25
    repeat

image Laura_Doggy_Ass:
    LiveComposite(

        (420,750),








        (0,0), ConditionSwitch(

            "not LauraX.underwear_pulled_down or (LauraX.outfit['bottom'] == '_pants' and not LauraX.upskirt)", Null(),
            "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Back.png",
            "LauraX.outfit['underwear'] == '_lace_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Lace_Back.png",
            "LauraX.outfit['underwear']", "images/LauraDoggy/Laura_Doggy_Panties_Back.png",
            "True", Null(),
            ),
        (0,0), "images/LauraDoggy/Laura_Doggy_Ass.png",





        (0,0), ConditionSwitch(

            "LauraX.outfit['hose'] == '_black_stockings'", "images/LauraDoggy/Laura_Doggy_Stocking.png",
            "LauraX.outfit['hose'] == '_stockings'", "images/LauraDoggy/Laura_Doggy_Hose.png",
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "Player.sprite and Player.cock_position == 'anal'", Null(),
            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.underwear_pulled_down or (LauraX.outfit['bottom'] == '_pants' and not LauraX.upskirt)", Null(),
            "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Down.png",
            "LauraX.outfit['underwear'] == '_bikini_bottoms'", "images/LauraDoggy/Laura_Doggy_Panties_Bikini_Down.png",
            "LauraX.outfit['underwear']", "images/LauraDoggy/Laura_Doggy_Panties_Black_Down.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Laura_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Laura_Pussy_Fucking2",
            "Player.sprite and Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Laura_Pussy_Fucking3",
                    "action_speed > 1", "Laura_Pussy_Fucking2",
                    "action_speed", "Laura_Pussy_Heading",
                    "True", "Laura_Pussy_animation0",
                    ),
            "primary_action == 'eat_pussy'", "images/LauraDoggy/Laura_Doggy_Pussy_Open.png",
            "LauraX.outfit['bottom'] and not LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Pussy_Closed.png",
            "LauraX.outfit['underwear'] and not LauraX.underwear_pulled_down", "images/LauraDoggy/Laura_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Laura_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Laura_Pussy_Fucking2",
            "True", "images/LauraDoggy/Laura_Doggy_Pussy_Closed.png",
            ),


        (0,0), ConditionSwitch(

            "LauraX.spunk['pussy'] and Player.cock_position == 'in'",Null(),
            "LauraX.spunk['pussy'] ", "images/LauraDoggy/Laura_Doggy_SpunkPussyClosed.png",
            "LauraX.grool and Player.cock_position == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "LauraX.grool", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.pubes", Null(),
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "LauraX.outfit['bottom'] == '_pants' and not LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Pubes_Panties.png",
            "LauraX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/LauraDoggy/Laura_Doggy_Pubes_Open.png",
            "LauraX.underwear_pulled_down", "images/LauraDoggy/Laura_Doggy_Pubes.png",
            "LauraX.outfit['underwear']", "images/LauraDoggy/Laura_Doggy_Pubes_Panties.png",
            "LauraX.outfit['hose'] and LauraX.outfit['hose'] != '_stockings'", "images/LauraDoggy/Laura_Doggy_Pubes_Panties.png",
            "primary_action == 'eat_pussy'", "images/LauraDoggy/Laura_Doggy_Pubes_Open.png",
            "True", "images/LauraDoggy/Laura_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Laura_Anal_Fucking2",
                    "action_speed > 1", "Laura_Anal_Fucking",
                    "action_speed", "Laura_Anal_Heading",
                    "True", "Laura_Anal",
                    ),


            "LauraX.outfit['bottom'] and not LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Asshole_Loose.png",
            "LauraX.outfit['underwear'] and not LauraX.underwear_pulled_down", "images/LauraDoggy/Laura_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Laura_Anal_Fingering",
            "primary_action == 'dildo anal'", "Laura_Anal_Fucking",
            "LauraX.used_to_anal", "images/LauraDoggy/Laura_Doggy_Asshole_Loose.png",
            "True", "images/LauraDoggy/Laura_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(

            "not LauraX.spunk['anus'] or Player.sprite", Null(),
            "Player.cock_position == 'anal'", "images/LauraDoggy/Laura_Doggy_SpunkAnalOpen.png",
            "LauraX.used_to_anal", "images/LauraDoggy/Laura_Doggy_SpunkAnalLoose.png",
            "True", "images/LauraDoggy/Laura_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.underwear_pulled_down or not LauraX.outfit['underwear']", Null(),
            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),


            "LauraX.outfit['underwear'] == '_wolvie_panties' and LauraX.grool", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Wet.png",
            "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie.png",
            "LauraX.outfit['underwear'] == '_lace_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Lace.png",
            "LauraX.outfit['underwear'] == '_bikini_bottoms'", "images/LauraDoggy/Laura_Doggy_Panties_Bikini.png",
            "LauraX.grool", "images/LauraDoggy/Laura_Doggy_Panties_Black_Wet.png",
            "True", "images/LauraDoggy/Laura_Doggy_Panties_Black.png",
            ),














        (0,0), ConditionSwitch(

            "LauraX.outfit['bottom'] == '_leather_pants'", ConditionSwitch(
                    "LauraX.upskirt or LauraX.underwear_pulled_down", Null(),

                    "True", "images/LauraDoggy/Laura_Doggy_Legs_Pants.png",
                    ),





            "LauraX.outfit['bottom'] == '_cosplay_skirt'", ConditionSwitch(
                    "LauraX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png",
                    "LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png",
                    "True", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos.png",
                    ),
            "LauraX.outfit['bottom'] == '_skirt'", ConditionSwitch(
                    "LauraX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/LauraDoggy/Laura_Doggy_Legs_Skirt_Up.png",
                    "LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Legs_Skirt_Up.png",
                    "True", "images/LauraDoggy/Laura_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.outfit['top'] == '_towel' and LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Over_TowelAss_Up.png",
            "LauraX.outfit['top'] == '_towel'", "images/LauraDoggy/Laura_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "LauraX.underwear_pulled_down or (not LauraX.outfit['underwear'] and LauraX.outfit['bottom'] != '_leather_pants')", Null(),
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraDoggy/Laura_Doggy_Pierce_RingC.png",
            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_BarbellC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.spunk['back']", "images/LauraDoggy/Laura_Doggy_Spunk_Ass.png",
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
            "LauraX.outfit['bottom'] == '_skirt' and LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/LauraDoggy/Laura_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),
            "LauraX.outfit['bottom'] == '_skirt' and LauraX.upskirt and action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "LauraX.outfit['bottom'] == '_skirt' and LauraX.upskirt", AlphaMask("Zero_Hotdog_animation0", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_animation0", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Laura_Doggy_Feet:
    contains:
        AlphaMask("Laura_Doggy_Shins", "images/LauraDoggy/Laura_Doggy_Feet_Toes.png")

image Laura_Doggy_Shins:

    contains:
        "images/LauraDoggy/Laura_Doggy_Feet_Back.png"
    contains:



        ConditionSwitch(
            "not LauraX.outfit['hose']", Null(),
            "LauraX.outfit['hose'] == '_stockings'", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png",
            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png",
            "LauraX.outfit['hose'] == '_black_stockings'", "images/LauraDoggy/Laura_Doggy_Feet_Stockings_Back.png",
            "LauraX.outfit['hose'] == '_pantyhose'", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.outfit['bottom'] == '_leather_pants'", "images/LauraDoggy/Laura_Doggy_Feet_Pants.png",
            "True", Null(),
            )












image Laura_Doggy_GropeBreast:
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

















image Zero_Laura_Hotdog_animation0:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Laura_Hotdog_Moving:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Laura_Doggy_animation0:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Laura_Doggy_Heading:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Laura_Doggy_Fucking2:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Laura_Doggy_Fucking3:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Laura_Pussy_Mask:


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

image Laura_Pussy_Mask_animation0:


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


































image Laura_Pussy_animation0:

    subpixel True
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHole.png"
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

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Laura_Doggy_animation0", "Laura_Pussy_Mask_animation0")
    contains:


        AlphaMask("Laura_PussyHole_animation0", "Laura_Pussy_Hole_Mask_animation0")

image Laura_Pussy_Hole_Mask_animation0:

    contains:

        AlphaMask("images/LauraDoggy/Laura_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Laura_PussyHole_animation0:

    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Laura_Pussy_Heading:

    subpixel True
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHole.png"
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

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Laura_Doggy_Heading", "Laura_Pussy_Mask")
    contains:


        AlphaMask("Laura_Pussy_Heading_Flap", "Laura_Pussy_Hole_Mask")


image Laura_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/LauraDoggy/Laura_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Laura_Pussy_Heading_Flap:

    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat

image Laura_Pussy_Fingering:

    subpixel True
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHole.png"
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


        AlphaMask("Laura_Pussy_Heading_Flap", "Laura_Pussy_Hole_Mask")



image Laura_Pussy_Fucking2:

    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FBase.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Laura_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),



image Laura_Pussy_Fucking3:

    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FBase.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Laura_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")





image Laura_Anal:

    contains:

        "images/LauraDoggy/Laura_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        "Zero_Doggy_Insert"
        pos (172,500)




image Laura_Anal_Fingering:

    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullBase.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullHole.png"
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


image Laura_Anal_Heading:

    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullBase.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullHole.png"
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

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Laura_Doggy_Anal_Heading", "Zero_Laura_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Laura_Doggy_Anal_Heading", "Laura_Doggy_Anal_Heading_Mask")

image Zero_Laura_Doggy_Anal_Heading:

    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Laura_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600
            repeat

image Laura_Doggy_Anal_Heading_Mask:

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

image Laura_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Laura_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat


image Zero_Laura_Doggy_Anal1:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Laura_Anal_Fucking:

    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullBase.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullCheeks.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullHole.png"
    contains:
        ConditionSwitch(

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "primary_action == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Laura_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),


image Laura_Doggy_Anal_FullMask:
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullHole.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )

image Laura_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 15
        pause .4
        block:
            ease .2 ypos 5
            pause .3
            ease 2 ypos 15
            repeat

image Laura_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15
            ease .1 ypos -5
            pause .2
            ease 1.6 ypos 0
            repeat



image Zero_Laura_Doggy_Anal2:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Laura_Anal_Fucking2:

    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullBase.png"
    contains:




        "images/LauraDoggy/Laura_Doggy_Anal_FullCheeks.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullHole.png"
    contains:
        ConditionSwitch(

            "LauraX.outfit['hose'] == '_stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.outfit['hose'] == '_garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Laura_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Laura_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Laura_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




image Laura_Doggy_Feet0:

    contains:
        "Laura_Doggy_Shins"
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
        "Laura_Doggy_Feet"
        pos (0, 0)
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Laura_Doggy_Feet1:

    contains:
        "Laura_Doggy_Shins"
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
        "Laura_Doggy_Feet"
        pos (0, 0)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Laura_Doggy_Feet2:

    contains:
        "Laura_Doggy_Shins"
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
        "Laura_Doggy_Feet"
        pos (0, 0)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat



image Laura_Doggy_Foot0_Top:

    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 10








image Laura_Doggy_Foot0_Ass:

    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block:
            pause 1
            ease 2 ypos 20
            pause .5
            ease 1.5 ypos 0
            repeat

image Laura_Doggy_Foot1_Top:

    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 70
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 70
            repeat

image Laura_Doggy_Foot1_Ass:

    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 0
        block:
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat

image Laura_Doggy_Foot2_Top:

    contains:
        subpixel True
        "Laura_Doggy_Body"
        ypos 70
        block:






            pause .05
            ease .6 ypos 90
            ease .3 ypos 70
            repeat

image Laura_Doggy_Foot2_Ass:

    contains:
        subpixel True
        "Laura_Doggy_Ass"
        ypos 70
        block:
            pause .15
            ease .6 ypos 90
            ease .2 ypos 70
            repeat






image Laura_sprite sex:

    contains:
        ConditionSwitch(

            "Player.cock_position == 'in'", ConditionSwitch(

                    "action_speed == 1", "Laura_Sex_Body_S1",
                    "action_speed == 2", "Laura_Sex_Body_S2",
                    "action_speed == 3", "Laura_Sex_Body_S3",
                    "action_speed >= 4", "Laura_Sex_Body_S4",
                    "True",       "Laura_Sex_Body_S0",
                    ),
            "Player.cock_position == 'anal'", ConditionSwitch(

                    "action_speed == 1", "Laura_Sex_Body_A1",
                    "action_speed == 2", "Laura_Sex_Body_A2",
                    "action_speed == 3", "Laura_Sex_Body_A3",
                    "action_speed >= 4", "Laura_Sex_Body_A4",
                    "True",       "Laura_Sex_Body_A0",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(

                    "not Player.sprite","Laura_Sex_Body_F0",
                    "action_speed == 1", "Laura_Sex_Body_F1",
                    "action_speed >= 4", "Laura_Sex_Body_F0",
                    "action_speed >= 2", "Laura_Sex_Body_F2",
                    "True",       "Laura_Sex_Body_F0",
                    ),

            "True", ConditionSwitch(

                    "not Player.sprite","Laura_Sex_Body_H0",
                    "action_speed == 1", "Laura_Sex_Body_H1",
                    "action_speed == 4", "Laura_Sex_Body_H0",
                    "action_speed >= 2", "Laura_Sex_Body_H2",
                    "True",       "Laura_Sex_Body_H0",
                    ),
            )
    contains:
        ConditionSwitch(

            "Player.cock_position == 'in'", ConditionSwitch(

                    "action_speed == 1", "Laura_Sex_Legs_S1",
                    "action_speed == 2", "Laura_Sex_Legs_S2",
                    "action_speed == 3", "Laura_Sex_Legs_S3",
                    "action_speed >= 4", "Laura_Sex_Legs_S4",
                    "True", "Laura_Sex_Legs_S0",
                    ),
            "Player.cock_position == 'anal'", ConditionSwitch(

                    "action_speed == 1", "Laura_Sex_Legs_A1",
                    "action_speed == 2", "Laura_Sex_Legs_A2",
                    "action_speed == 3", "Laura_Sex_Legs_A3",
                    "action_speed >= 4", "Laura_Sex_Legs_A4",
                    "True", "Laura_Sex_Legs_A0",
                    ),
            "Player.cock_position == 'footjob'", ConditionSwitch(

                    "not Player.sprite","Laura_Sex_Legs_F0",
                    "action_speed == 1", "Laura_Sex_Legs_F1",
                    "action_speed >= 4", "Laura_Sex_Legs_F0",
                    "action_speed >= 2", "Laura_Sex_Legs_F2",
                    "True",       "Laura_Sex_Legs_F0",
                    ),
            "True", ConditionSwitch(

                    "not Player.sprite","Laura_Sex_Legs_H0",
                    "action_speed == 1", "Laura_Sex_Legs_H1",
                    "action_speed == 4", "Laura_Sex_Legs_H0",
                    "action_speed >= 2", "Laura_Sex_Legs_H2",
                    "True", "Laura_Sex_Legs_H0",
                    ),
            )
    zoom .6
    transform_anchor True
    anchor (.5, 0.0)


image Laura_Sex_HairBack:

    "Laura_Sprite_HairBack"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)

image Laura_Sex_Head:

    "Laura_Sprite_Head"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)



image Laura_Sex_Body:

    contains:
        "Laura_Sex_HairBack"
    contains:



        ConditionSwitch(
                    "Player.cock_position == 'footjob'", Null(),
                    "LauraX.outfit['gloves'] == '_gloves'", "images/LauraSex/Laura_Sex_Hand_Gloved.png",
                    "True", "images/LauraSex/Laura_Sex_Hand.png"
                    )
    contains:

        ConditionSwitch(
            "not LauraX.outfit['top']", Null(),
            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.outfit['top'] == '_jacket'", "images/LauraSex/Laura_Sex_Jacket_Back_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "LauraX.outfit['top'] == '_jacket'", "images/LauraSex/Laura_Sex_Jacket_Back.png",
                    "True", Null(),
                    ),
            )
    contains:

        "images/LauraSex/Laura_Sex_Body.png"
    contains:

        ConditionSwitch(
            "not LauraX.outfit['piercings']", Null(),
            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits.png",
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraSex/Laura_Sex_Ring_Tits.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.outfit['neck'] == '_leash choker'", "images/LauraSex/Laura_Sex_Leash.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.outfit['hose'] == '_stockings_and_garterbelt' or LauraX.outfit['hose'] == '_garterbelt'", "images/LauraSex/Laura_Sex_Garter.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.outfit['bra']", Null(),
            "LauraX.top_pulled_up",ConditionSwitch(

                    "not LauraX.outfit['bra']", Null(),
                    "LauraX.outfit['bra'] == '_white_tank'", "images/LauraSex/Laura_Sex_WhiteTank_Up.png",
                    "LauraX.outfit['bra'] == '_leather_bra'", "images/LauraSex/Laura_Sex_Bra_Leather_Up.png",
                    "LauraX.outfit['bra'] == '_wolvie_top'", "images/LauraSex/Laura_Sex_Top_Wolvie_Up.png",
                    "LauraX.outfit['bra'] == '_corset'", "images/LauraSex/Laura_Sex_Corset_Up.png",
                    "LauraX.outfit['bra'] == '_lace_corset'", "images/LauraSex/Laura_Sex_Corset_Lace_Up.png",
                    "LauraX.outfit['bra'] == '_bikini_top'", "images/LauraSex/Laura_Sex_Top_Bikini_Up.png",


                    "True", Null(),
                    ),

            "LauraX.outfit['bra'] == '_white_tank'", "images/LauraSex/Laura_Sex_WhiteTank.png",
            "LauraX.outfit['bra'] == '_leather_bra'", "images/LauraSex/Laura_Sex_Bra_Leather.png",
            "LauraX.outfit['bra'] == '_wolvie_top'", "images/LauraSex/Laura_Sex_Top_Wolvie.png",
            "LauraX.outfit['bra'] == '_corset'", "images/LauraSex/Laura_Sex_Corset.png",
            "LauraX.outfit['bra'] == '_lace_corset'", "images/LauraSex/Laura_Sex_Corset_Lace.png",
            "LauraX.outfit['bra'] == '_bikini_top'", "images/LauraSex/Laura_Sex_Top_Bikini.png",


            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.outfit['piercings'] or LauraX.top_pulled_up", Null(),
            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits_C.png",
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraSex/Laura_Sex_Ring_Tits_C.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.outfit['bottom']", Null(),
            "LauraX.outfit['suspenders'] == '_suspenders' and not LauraX.outfit['bra'] and not LauraX.top_pulled_up", "images/LauraSex/Laura_Sex_Suspenders.png",
            "LauraX.outfit['suspenders'] == '_suspenders2'", "images/LauraSex/Laura_Sex_Suspenders.png",
            "LauraX.outfit['suspenders'] == '_suspenders'", "images/LauraSex/Laura_Sex_Suspenders_Up.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.outfit['top']", Null(),
            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.outfit['top'] == '_jacket'", "images/LauraSex/Laura_Sex_Jacket_Up.png",

                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "LauraX.outfit['top'] == '_jacket'", "images/LauraSex/Laura_Sex_Jacket.png",

                    "True", Null(),
                    ),
            )
    contains:

        ConditionSwitch(
            "LauraX.spunk['belly']", "images/LauraSex/Laura_Sex_Spunk_Belly.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
                "not LauraX.spunk['breasts']", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Tits.png",
                )
    contains:
        ConditionSwitch(

                "primary_action == 'suck_breasts' or offhand_action == 'suck_breasts'", "Laura_Sex_Lick_Breasts",
                "True", Null()
                )
    contains:
        ConditionSwitch(

                "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Laura_Sex_Fondle_Breasts",
                "True", Null()
                )
    contains:
        "Laura_Sex_Head"
    transform_anchor True
    zoom .9
    offset (55,55)



image Laura_Sex_Lick_Breasts:
    "Lick_Anim"
    zoom 0.7
    offset (565,290)

image Laura_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.5
    offset (360,-280)

image Laura_Sex_Legs:

    contains:

        ConditionSwitch(
            "LauraX.outfit['bottom'] == '_skirt'", "images/LauraSex/Laura_Sex_Skirt_Back.png",
            "True", Null(),
            )
    contains:







        ConditionSwitch(
            "Player.cock_position == 'footjob'", "images/LauraSex/Laura_Sex_Legs_Foot.png",
            "True", "images/LauraSex/Laura_Sex_Legs_High.png",
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'anal' and action_speed > 1", "images/LauraSex/Laura_Sex_Anus_L.png",
            "Player.cock_position == 'anal' and action_speed > 0", "images/LauraSex/Laura_Sex_Anus_M.png",
            "LauraX.spunk['anus']", "images/LauraSex/Laura_Sex_Anus_M.png",
            "True", "images/LauraSex/Laura_Sex_Anus_S.png",
            )
    contains:

        ConditionSwitch(
            "not LauraX.spunk['anus']", Null(),
            "Player.cock_position == 'anal' and action_speed > 1", "images/LauraSex/Laura_Sex_Spunk_Anal_U.png",
            "True", "images/LauraSex/Laura_Sex_Spunk_Anal.png",
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'in' and action_speed > 1", "images/LauraSex/Laura_Sex_Pussy_Open.png",
            "Player.cock_position == 'in' and action_speed > 0", "images/LauraSex/Laura_Sex_Pussy_Mid.png",
            "primary_action == 'eat_pussy'", "images/LauraSex/Laura_Sex_Pussy_Mid.png",
            "True", "images/LauraSex/Laura_Sex_Pussy_Closed.png",
            )
    contains:

        ConditionSwitch(
            "not LauraX.grool", Null(),
            "True", "images/LauraSex/Laura_Sex_Wet.png",
            )
    contains:

        ConditionSwitch(
            "not LauraX.spunk['pussy']", Null(),
            "Player.cock_position == 'in' and action_speed > 1", "images/LauraSex/Laura_Sex_Spunk_Pussy_Open.png",
            "True", "images/LauraSex/Laura_Sex_Spunk_Pussy.png",
            )
    contains:

        ConditionSwitch(
            "not LauraX.pubes", Null(),
            "Player.cock_position == 'in' and action_speed > 1", "images/LauraSex/Laura_Sex_Pubes_Open.png",
            "Player.cock_position == 'in' and action_speed > 0", "images/LauraSex/Laura_Sex_Pubes_Mid.png",
            "primary_action == 'eat_pussy'", "images/LauraSex/Laura_Sex_Pubes_Mid.png",
            "True", "images/LauraSex/Laura_Sex_Pubes_Closed.png",
            )
    contains:

        ConditionSwitch(
            "LauraX.outfit['piercings'] == '_barbell' and Player.cock_position == 'in' and action_speed > 1", "images/LauraSex/Laura_Sex_Barbell_Pussy_O.png",
            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy.png",
            "LauraX.outfit['piercings'] == '_ring' and Player.cock_position == 'in' and action_speed > 1", "images/LauraSex/Laura_Sex_Ring_Pussy_O.png",
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraSex/Laura_Sex_Ring_Pussy.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.underwear_pulled_down", Null(),

            "LauraX.outfit['underwear'] == '_bikini_bottoms'", "images/LauraSex/Laura_Sex_Panties_Bikini.png",
            "LauraX.outfit['underwear'] == '_wolvie_panties'", "images/LauraSex/Laura_Sex_Panties_Wolvie.png",
            "LauraX.outfit['underwear'] == '_lace_panties'", "images/LauraSex/Laura_Sex_Panties_Lace.png",
            "LauraX.outfit['underwear']", "images/LauraSex/Laura_Sex_Panties_Black.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'footjob' and (LauraX.outfit['hose'] == '_stockings_and_garterbelt' or LauraX.outfit['hose'] == '_stockings')", "images/LauraSex/Laura_Sex_Stockings_Base_Foot.png",
            "Player.cock_position == 'footjob' and LauraX.outfit['hose'] == '_black_stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Base_Foot.png",
            "LauraX.outfit['hose'] == '_black_stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Base_Up.png",
            "LauraX.outfit['hose'] == '_stockings_and_garterbelt' or LauraX.outfit['hose'] == '_stockings'", "images/LauraSex/Laura_Sex_Stockings_Base_Up.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.outfit['bottom'] == '_skirt' or LauraX.outfit['bottom'] == '_cosplay_skirt'", "images/LauraSex/Laura_Sex_Skirt.png",
            "LauraX.upskirt", Null(),
            "LauraX.outfit['bottom'] == '_leather_pants' and Player.cock_position == 'footjob'", "images/LauraSex/Laura_Sex_Pants_Base_Foot.png",
            "LauraX.outfit['bottom'] == '_leather_pants'", "images/LauraSex/Laura_Sex_Pants_Base_Up.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Laura_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Laura_Sex_Lick_Ass",
            "True", Null()
            ),
    contains:

        ConditionSwitch(


            "LauraX.outfit['piercings'] == '_barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy_C.png",
            "LauraX.outfit['piercings'] == '_ring'", "images/LauraSex/Laura_Sex_Ring_Pussy_C.png",
            "True", Null(),
            )
    contains:







        ConditionSwitch(
            "Player.cock_position == 'footjob'", "Laura_Footjob_Foot",
            "True", "Laura_Sex_Foot",
            )
    transform_anchor True
    zoom 1





image Laura_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.8
    offset (720,610)

image Laura_Sex_Lick_Ass:
    "Lick_Anim"
    zoom 0.8
    offset (730,700)


image Laura_Sex_Foot:




    contains:

        ConditionSwitch(
            "LauraX.outfit['hose'] == '_stockings_and_garterbelt' or LauraX.outfit['hose'] == '_stockings'", "images/LauraSex/Laura_Sex_Stockings_Up.png",
            "LauraX.outfit['hose'] == '_black_stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Up.png",
            "True", "images/LauraSex/Laura_Sex_FootHigh.png"
            )
    contains:

        ConditionSwitch(
            "LauraX.upskirt", Null(),
            "LauraX.outfit['bottom'] == '_leather_pants'", "images/LauraSex/Laura_Sex_Pants_Up.png",
            "True", Null(),
            )
        xoffset -2
    transform_anchor True
    zoom 1

    pos (988,-553)



















image Laura_CockRef:
    "images/LauraSex/Laura_Sex_Cocktest.png"
    alpha 0.8






image Laura_SexMask:
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskPussyX.png"
        pos (200,303)
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)



image Laura_Sex_Body_S0:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Laura_Sex_Legs_S0:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease 0.5 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_S0", "Laura_SexMask")
        subpixel True
        pos (525,465)
        block:
            pause 0.1
            ease 0.5 ypos 460
            easeout 0.5 ypos 461
            easein 0.9 ypos 465
            repeat


image Laura_Sex_Zero_Anim_S0:

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





image Laura_Sex_Body_S1:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Laura_Sex_Legs_S1:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease 0.5 ypos -5
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_S1", "Laura_SexMask")
        subpixel True
        pos (525,485)
        block:
            pause 0.1
            ease 0.5 ypos 480
            easeout 0.5 ypos 481
            easein 0.9 ypos 485
            repeat


image Laura_Sex_Zero_Anim_S1:

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




image Laura_Sex_Body_S2:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,10)
        block:
            pause 0.3
            ease 0.3 ypos -10
            pause 0.20
            ease 1.70 ypos 10
            repeat

image Laura_Sex_Legs_S2:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.25
            ease 0.3 ypos -25
            easeout 0.45 ypos -20
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_S2", "Laura_SexMask")
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
                "not LauraX.spunk['pussy']", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (-15,-105)
        block:
            pause 0.25
            ease 0.3 ypos -130
            easeout 0.45 ypos -125
            easein 1.5 ypos -105
            repeat


image Laura_Sex_Zero_Anim_S2:

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





image Laura_Sex_Body_S3:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,10)
        block:
            pause 0.1
            ease 0.2 ypos -50
            pause 0.2
            ease .7 ypos 10
            repeat

image Laura_Sex_Legs_S3:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -45
            easeout 0.45 ypos -40
            easein .5 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_S3", "Laura_SexMask")
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
                "not LauraX.spunk['pussy']", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (-15,-105)
        block:
            pause 0.05
            ease 0.2 ypos -150
            easeout 0.45 ypos -145
            easein .5 ypos -105
            repeat


image Laura_Sex_Zero_Anim_S3:

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




image Laura_Sex_Body_S4:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,10)
        block:
            pause 0.1
            ease 0.2 ypos 0
            pause 0.2
            ease 1.7 ypos 10
            repeat

image Laura_Sex_Legs_S4:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -15
            easeout 0.45 ypos -10
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_S4", "Laura_SexMask")
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
                "not LauraX.spunk['pussy']", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (-15,-105)
        block:
            pause 0.05
            ease 0.2 ypos -120
            easeout 0.45 ypos -115
            easein 1.5 ypos -105
            repeat


image Laura_Sex_Zero_Anim_S4:

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







image Laura_Sex_Body_A0:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Laura_Sex_Legs_A0:

    contains:

        "Laura_Sex_Legs"
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
        AlphaMask("Laura_Sex_Zero_Anim_A0", "Laura_AnalMask")
        subpixel True
        pos (533,587)
        block:
            pause 0.6
            easeout 0.8 ypos 585
            easein 0.2 ypos 582
            easeout 0.5 ypos 583
            easein 0.9 ypos 587
            repeat


image Laura_Sex_Zero_Anim_A0:

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






image Laura_Sex_Body_A1:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Laura_Sex_Legs_A1:

    contains:

        "Laura_Sex_Legs"
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
        AlphaMask("Laura_Sex_Zero_Anim_A1", "Laura_AnalMask")
        subpixel True
        pos (538,583)
        block:
            pause 0.6
            easeout 0.8 ypos 581
            easein 0.2 ypos 578
            easeout 0.5 ypos 579
            easein 0.9 ypos 583
            repeat


image Laura_Sex_Zero_Anim_A1:

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




image Laura_Sex_Body_A2:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.3
            ease 0.3 ypos -20
            pause 0.20
            ease 1.70 ypos 20
            repeat

image Laura_Sex_Legs_A2:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.25
            ease 0.3 ypos -35
            easeout 0.45 ypos -30
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_A2", "Laura_AnalMask")
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
                "not LauraX.spunk['anus']", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (0,0)
        block:
            pause 0.25
            ease 0.3 ypos -35
            easeout 0.45 ypos -30
            easein 1.5 ypos 0
            repeat


image Laura_Sex_Zero_Anim_A2:

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




image Laura_Sex_Body_A3:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease 0.2 ypos -50
            pause 0.2
            ease .7 ypos 00
            repeat

image Laura_Sex_Legs_A3:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -55
            easeout 0.45 ypos -40
            easein .5 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_A3", "Laura_AnalMask")
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
                "not LauraX.spunk['anus']", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -55
            easeout 0.45 ypos -40
            easein .5 ypos 0
            repeat


image Laura_Sex_Zero_Anim_A3:

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




image Laura_Sex_Body_A4:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,20)
        block:
            pause 0.1
            ease 0.2 ypos 00
            pause 0.2
            ease 1.7 ypos 20
            repeat

image Laura_Sex_Legs_A4:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -15
            easeout 0.45 ypos -10
            easein 1.5 ypos 0
            repeat
    contains:
        AlphaMask("Laura_Sex_Zero_Anim_A4", "Laura_AnalMask")
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
                "not LauraX.spunk['anus']", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Anal_O.png",
                )
        subpixel True
        pos (0,0)
        block:
            pause 0.05
            ease 0.2 ypos -15
            easeout 0.45 ypos -10
            easein 1.5 ypos 0
            repeat


image Laura_Sex_Zero_Anim_A4:

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





image Laura_Sex_Body_H0:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Laura_Sex_Legs_H0:

    contains:

        "Laura_Sex_Legs"
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
        "Laura_Sex_Zero_Anim_H0"

        subpixel True
        pos (558,580)
        block:
            pause 0.6
            easeout 0.8 ypos 578
            easein 0.2 ypos 575
            easeout 0.5 ypos 576
            easein 0.9 ypos 580
            repeat


image Laura_Sex_Zero_Anim_H0:

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





image Laura_Sex_Body_H1:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat

image Laura_Sex_Legs_H1:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.6
            ease 1 ypos -10
            easeout 0.5 ypos -4
            easein 0.9 ypos 0
            repeat
    contains:
        "Laura_Sex_Zero_Anim_H1"

        subpixel True
        pos (558,580)
        block:
            pause 0.6
            ease 1 ypos 570
            easeout 0.5 ypos 576
            easein 0.9 ypos 580
            repeat


image Laura_Sex_Zero_Anim_H1:

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





image Laura_Sex_Body_H2:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause .3
            ease .5 ypos -5
            pause 0.3
            ease .4 ypos 0
            repeat

image Laura_Sex_Legs_H2:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            pause 0.1
            ease .25 ypos -20
            easeout 0.15 ypos -18
            easein 0.25 ypos 0
            repeat
    contains:
        "Laura_Sex_Zero_Anim_H2"

        subpixel True
        pos (558,580)
        block:
            pause 0.1
            ease .25 ypos 560
            easeout 0.15 ypos 562
            easein 0.25 ypos 580
            repeat


image Laura_Sex_Zero_Anim_H2:

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




image Laura_AnalMask:
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskAnalX.png"
        pos (200,366)
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)





image Laura_Footjob_Foot:

    contains:

        ConditionSwitch(
            "LauraX.outfit['hose'] == '_stockings_and_garterbelt' or LauraX.outfit['hose'] == '_stockings'", "images/LauraSex/Laura_Sex_Stockings_Foot.png",
            "LauraX.outfit['hose'] == '_black_stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Foot.png",
            "True", "images/LauraSex/Laura_Sex_Foot.png"
            )
    contains:

        ConditionSwitch(
            "LauraX.upskirt", Null(),
            "LauraX.outfit['bottom'] == '_leather_pants'", "images/LauraSex/Laura_Sex_Pants_Foot.png",
            "True", Null(),
            )
    offset (1105,140)
    zoom 1

image Laura_Sex_Zero_Anim_F:

    "Zero_blowjob_cock"
    zoom .7
    anchor (0.5, 0.9)
    offset (270,650)
    rotate 0



image Laura_Sex_Body_F0:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat
    yoffset -100

image Laura_Sex_Legs_F0:

    contains:

        "Laura_Sex_Legs"
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

        "Laura_Footjob_Foot"
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
        "Laura_Sex_Zero_Anim_F"
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








image Laura_Sex_Body_F1:

    contains:
        "Laura_Sex_Body"
        subpixel True
        pos (0,0)
        block:
            pause 1.15
            ease 0.6 ypos -5
            pause 0.65
            ease .6 ypos 0
            repeat
    yoffset -100

image Laura_Sex_Legs_F1:

    contains:

        "Laura_Sex_Legs"
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
        "Laura_Sex_Zero_Anim_F"
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

        "Laura_Footjob_Foot"
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







image Laura_Sex_Body_F2:

    contains:
        "Laura_Sex_Body"
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

image Laura_Sex_Legs_F2:

    contains:

        "Laura_Sex_Legs"
        subpixel True
        pos (0,0)
        block:
            ease 0.5 ypos -2
            ease 1 ypos -10
            pause .1
            repeat
    contains:
        "Laura_Sex_Zero_Anim_F"
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

        "Laura_Footjob_Foot"
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










image Laura_SexMaskX:
    transform_anchor True
    contains:
        "images/LauraSex/Laura_Sex_MaskPussyX.png"
        pos (200,303)
        anchor (.5,.5)
    zoom 1

    anchor (0.5,0.5)


image Laura_Sex_Zero_AnimX:

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



image Laura_Mega_Mask2:

    contains:
        "images/LauraSex/Laura_Sex_PussyMaskTest2.png"






















    transform_anchor True
    zoom 1
    rotate 30





image Laura_Mega_Mask:

    contains:
        "images/LauraSex/Laura_Sex_PussyMaskTestB.png"




        alpha .5









    transform_anchor True
    zoom 1
    rotate 30









image Laura_sprite blowjob:

    contains:
        ConditionSwitch(



            "action_speed == 1", "Laura_BJ_Body_1",
            "action_speed == 2", "Laura_BJ_Body_2",
            "action_speed == 3", "Laura_BJ_Body_3",
            "action_speed == 4", "Laura_BJ_Body_4",
            "action_speed == 5", "Laura_BJ_Body_5",
            "action_speed == 6", "Laura_BJ_Body_6",


            "True","Laura_BJ_Body_0",
            )
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)














image Laura_Sprite_BJ_HairBack:


    ConditionSwitch(

            "not LauraX.outfit['hair']", Null(),
            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",
            "True", Null(),
            )

image Laura_Sprite_BJ_Head:

    LiveComposite(
        (806,806),
        (0,0), ConditionSwitch(

                "LauraX.blushing == '_blush2'", "images/LauraSprite/Laura_Sprite_Head_Blush2.png",
                "LauraX.blushing", "images/LauraSprite/Laura_Sprite_Head_Blush.png",
                "True", "images/LauraSprite/Laura_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "not LauraX.spunk['chin']", Null(),
            "action_speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(
            "action_speed >= 2", "images/LauraSprite/Laura_Sprite_mouth_SuckingBJ.png",
            "action_speed == 1", "images/LauraSprite/Laura_Sprite_mouth_Tongue.png",
            "LauraX.mouth == '_normal'", "images/LauraSprite/Laura_Sprite_mouth_Normal.png",
            "LauraX.mouth == '_lipbite'", "images/LauraSprite/Laura_Sprite_mouth_Lipbite.png",
            "LauraX.mouth == '_sucking'", "images/LauraSprite/Laura_Sprite_mouth_Sucking.png",
            "LauraX.mouth == '_kiss'", "images/LauraSprite/Laura_Sprite_mouth_Kiss.png",
            "LauraX.mouth == '_sad'", "images/LauraSprite/Laura_Sprite_mouth_Sad.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_mouth_Smile.png",
            "LauraX.mouth == '_surprised'", "images/LauraSprite/Laura_Sprite_mouth_Surprised.png",
            "LauraX.mouth == '_tongue'", "images/LauraSprite/Laura_Sprite_mouth_Tongue.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_mouth_Smile.png",
            "LauraX.mouth == '_smirk'", "images/LauraSprite/Laura_Sprite_mouth_Smirk.png",

            "True", "images/LauraSprite/Laura_Sprite_mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "not LauraX.spunk['mouth']", Null(),
            "action_speed >= 2", "images/LauraSprite/Laura_Sprite_Spunk_mouthSuck.png",
            "action_speed == 1", "images/LauraSprite/Laura_Sprite_Spunk_mouthTongue.png",
            "LauraX.mouth == '_normal'", "images/LauraSprite/Laura_Sprite_Spunk_mouthNeutral.png",
            "LauraX.mouth == '_lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmirk.png",
            "LauraX.mouth == '_sucking'", "images/LauraSprite/Laura_Sprite_Spunk_mouthTongue.png",
            "LauraX.mouth == '_kiss'", "images/LauraSprite/Laura_Sprite_Spunk_mouthKiss.png",
            "LauraX.mouth == '_sad'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSad.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmile.png",
            "LauraX.mouth == '_surprised'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSad.png",
            "LauraX.mouth == '_tongue'", "images/LauraSprite/Laura_Sprite_Spunk_mouthTongue.png",
            "LauraX.mouth == '_smile'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmile.png",
            "LauraX.mouth == '_smirk'", "images/LauraSprite/Laura_Sprite_Spunk_mouthSmirk.png",
            "True", "images/LauraSprite/Laura_Sprite_Spunk_mouthNeutral.png",
            ),
        (0,0), ConditionSwitch(
            "action_speed >= 2 and LauraX.spunk[mouth]", "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "action_speed == 1", "images/LauraSprite/Laura_Sprite_Wet_Tongue.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.blushing == '_blush2'", ConditionSwitch(
                    "LauraX.brows == '_normal'", "images/LauraSprite/Laura_Sprite_brows_Normal_B.png",
                    "LauraX.brows == '_angry'", "images/LauraSprite/Laura_Sprite_brows_Angry_B.png",
                    "LauraX.brows == '_sad'", "images/LauraSprite/Laura_Sprite_brows_Sad_B.png",
                    "LauraX.brows == '_surprised'", "images/LauraSprite/Laura_Sprite_brows_Surprised_B.png",
                    "LauraX.brows == '_confused'", "images/LauraSprite/Laura_Sprite_brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.brows == '_normal'", "images/LauraSprite/Laura_Sprite_brows_Normal.png",
                    "LauraX.brows == '_angry'", "images/LauraSprite/Laura_Sprite_brows_Angry.png",
                    "LauraX.brows == '_sad'", "images/LauraSprite/Laura_Sprite_brows_Sad.png",
                    "LauraX.brows == '_surprised'", "images/LauraSprite/Laura_Sprite_brows_Surprised.png",
                    "LauraX.brows == '_confused'", "images/LauraSprite/Laura_Sprite_brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_brows_Normal.png",
                    ),
            ),
        (0,0), "Laura_blinking",
        (0,0), ConditionSwitch(

            "LauraX.outfit['top'] == '_jacket'", Null(),
            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", Null(),
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "not LauraX.outfit['hair']", Null(),
            "LauraX.outfit['hair'] == '_wet' or LauraX.wet", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.outfit['hair']", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.wet", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",

            ),
        (0,0), ConditionSwitch(

            "LauraX.spunk['hair']", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",
            "LauraX.spunk['face']", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )



image Laura_BlowCock_Mask:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)





















image Laura_BJ_Body_0:

    contains:

        "Laura_Sprite_BJ_HairBack"
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

        "Laura_sprite standing"
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
        "Laura_Sprite_BJ_Head"
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





        AlphaMask("Zero_blowjob_cock", "Laura_BlowCock_Mask")
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



image Laura_BJ_Body_1:

    contains:

        "Laura_Sprite_BJ_HairBack"
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

        "Laura_sprite standing"
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
        "Laura_Sprite_BJ_Head"
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





        AlphaMask("Zero_blowjob_cock", "Laura_BlowCock_Mask")
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


image Laura_BJ_Body_2:

    contains:

        "Laura_Sprite_BJ_HairBack"
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

        "Laura_sprite standing"
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
        "Laura_Sprite_BJ_Head"
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





        AlphaMask("Zero_blowjob_cock", "Laura_BlowCock_Mask")
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
        AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
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




image Laura_BlowCock_Mask_3:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,100)







image Laura_BJ_Body_3:

    contains:

        "Laura_Sprite_BJ_HairBack"
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

        "Laura_sprite standing"
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
        "Laura_Sprite_BJ_Head"
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





        AlphaMask("Zero_blowjob_cock", "Laura_BlowCock_Mask_3")
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
        AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
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



image Laura_BlowCock_Mask_4:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)
        block:
            pause 0.1
            ease 1.6 offset (0,300)
            pause 0.1
            ease 1.4 offset (0,0)
            repeat

image Laura_BJ_Body_4:

    contains:

        "Laura_Sprite_BJ_HairBack"
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

        "Laura_sprite standing"
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
        "Laura_Sprite_BJ_Head"
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





        AlphaMask("Zero_blowjob_cock", "Laura_BlowCock_Mask_4")
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
        AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
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



image Laura_BJ_Body_5:

    contains:

        "Laura_Sprite_BJ_HairBack"
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

        "Laura_sprite standing"
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
        "Laura_Sprite_BJ_Head"
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





        AlphaMask("Zero_blowjob_cock", "Laura_BlowCock_Mask")
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
        AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
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


image Laura_BlowCock_Mask_6:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,300)







image Laura_BJ_Body_6:

    contains:

        "Laura_Sprite_BJ_HairBack"
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

        "Laura_sprite standing"
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
        "Laura_Sprite_BJ_Head"
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





        AlphaMask("Zero_blowjob_cock", "Laura_BlowCock_Mask_6")
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
        AlphaMask("Laura_Sprite_BJ_Head", "images/LauraSprite/Laura_Sprite_SuckingMask.png")
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







label Laura_BJ_Launch(Line=primary_action):

    $ LauraX.arm_pose = 1
    if renpy.showing("Laura_sprite blowjob"):
        return

    call hide_girl(LauraX)
    if Line == "L" or Line == "cum":
        show Laura_sprite standing zorder LauraX.sprite_layer at sprite_location(stage_center):
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Laura_sprite standing zorder LauraX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    $ action_speed = 0
    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != LauraX:
                    "[LauraX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != LauraX:
                    "[LauraX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[LauraX.name] casually glances around to see if anyone can see her."
        "[LauraX.name] smoothly bends down and places your cock against her cheek."

    if Line != "cum":
        $ primary_action = "blowjob"

    show Laura_sprite standing zorder LauraX.sprite_layer:
        alpha 0
    show Laura_sprite blowjob zorder 150:
        pos (645,510)
    return

label Laura_BJ_Reset:
    if not renpy.showing("Laura_sprite blowjob"):
        return

    call hide_girl(LauraX)
    $ action_speed = 0

    show Laura_sprite standing zorder LauraX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Laura_sprite standing zorder LauraX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Laura_sprite standing zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return








image Laura_Hand_Under:
    "images/LauraSprite/handlaura2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Laura_Hand_Over:
    "images/LauraSprite/handlaura1.png"
    anchor (0.5,0.5)
    pos (-10,0)

transform Laura_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5
        pause 0.1
        repeat

transform Laura_Hand_2():
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

image Laura_sprite handjob:
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Laura_Hand_Under"),
            "action_speed == 1", At("Laura_Hand_Under", Laura_Hand_1()),
            "action_speed >= 2", At("Laura_Hand_Under", Laura_Hand_2()),
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

            "not action_speed", Transform("Laura_Hand_Over"),
            "action_speed == 1", At("Laura_Hand_Over", Laura_Hand_1()),
            "action_speed >= 2", At("Laura_Hand_Over", Laura_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4






image Laura_sprite titjob:

    contains:
        ConditionSwitch(

                    "not Player.sprite","Laura_TJ_0",
                    "action_speed == 1", "Laura_TJ_1",
                    "action_speed == 4", "Laura_TJ_4",
                    "action_speed == 5", "Laura_TJ_5",
                    "action_speed >= 2", "Laura_TJ_2",
                    "True",       "Laura_TJ_0",
                    )
    zoom .7
    transform_anchor True
    anchor (.5,.5)




image Laura_TJ_HairBack:

    "Laura_Sprite_HairBack"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    offset (320,100)
    rotate 0

image Laura_TJ_Head:

    "Laura_Sprite_Head"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    offset (320,100)
    rotate 0

image Laura_TJ_HairMid:

    "Laura_Sprite_HairMid"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    rotate 20
    offset (320,100)
    rotate 0

image Laura_TJ_HairTop:

    "Laura_Sprite_HairTop"
    transform_anchor True
    zoom 2.5
    anchor (0.5, 0.5)
    offset (320,100)
    rotate 0

image Laura_TJ_ZeroCock:

    "Zero_blowjob_cock"
    transform_anchor True
    zoom .7
    anchor (0.5, 0.5)
    offset (220,670)
    rotate 0

image Laura_TJ_Body:

    contains:
        "images/LauraSex/Laura_Titjob_Body.png"
    contains:
        ConditionSwitch(
                        "not LauraX.outfit['neck']",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Neck_[LauraX.outfit['neck']].png",
                        )
    contains:
        ConditionSwitch(
                        "not LauraX.spunk['breasts']",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Spunk_Chest.png",
                        )
    transform_anchor True
    zoom 1
    anchor (0.4, 1.0)
    offset (410,770)
    rotate 0


image Laura_TJ_LeftArm:

    contains:
        "images/LauraSex/Laura_Titjob_LeftHand.png"
    contains:
        ConditionSwitch(
                        "not LauraX.outfit['gloves']",Null(),
                        "LauraX.outfit['gloves'] == '_gloves'",       "images/LauraSex/Laura_Titjob_LeftGlove.png",
                        "True",       "images/LauraSex/Laura_Titjob_wrists.png",
                        )
    contains:

        ConditionSwitch(
                        "not LauraX.outfit['piercings']",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Left_[LauraX.outfit['piercings']].png",
                        )

image Laura_TJ_RightArm:

    contains:
        "images/LauraSex/Laura_Titjob_RightHand.png"
    contains:
        ConditionSwitch(
                        "LauraX.outfit['gloves'] == '_gloves'",       "images/LauraSex/Laura_Titjob_RightGlove.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not LauraX.outfit['piercings']",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.outfit['piercings']].png",
                        )

image Laura_TJ_RightArmBack:

    contains:
        "images/LauraSex/Laura_Titjob_RightHandBack.png"
    contains:
        ConditionSwitch(
                        "LauraX.outfit['gloves'] == '_gloves'",       "images/LauraSex/Laura_Titjob_RightGloveBack.png",
                        "True", Null(),
                        )




image Laura_TJ_0:

    contains:

        "Laura_TJ_HairBack"
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

        "Laura_TJ_Body"
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

        "Laura_TJ_RightArmBack"
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
            "images/LauraSex/Laura_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
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









        "Laura_TJ_RightArm"
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

        "Laura_TJ_Head"
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
        "Laura_TJ_ZeroCock"
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
            "images/LauraSex/Laura_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
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

        "Laura_TJ_LeftArm"








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

        "Laura_TJ_HairMid"
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

        "Laura_TJ_HairTop"
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




image Laura_TJ_1:

    contains:

        "Laura_TJ_HairBack"
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

        "Laura_TJ_Body"
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

        "Laura_TJ_RightArmBack"
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
            "images/LauraSex/Laura_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
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









        "Laura_TJ_RightArm"
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

        "Laura_TJ_Head"
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
        "Laura_TJ_ZeroCock"
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
            "images/LauraSex/Laura_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
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

        "Laura_TJ_LeftArm"
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

        "Laura_TJ_HairMid"
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

        "Laura_TJ_HairTop"
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




image Laura_TJ_2:

    contains:

        "Laura_TJ_HairBack"
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

        "Laura_TJ_Body"
        subpixel True
        pos (0,80)
        transform_anchor True
        parallel:
            ease 1 ypos -20
            pause .1
            ease .5 ypos 80
            repeat
    contains:

        "Laura_TJ_RightArmBack"
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
            "images/LauraSex/Laura_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
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









        "Laura_TJ_RightArm"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 1 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        "Laura_TJ_Head"
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
        "Laura_TJ_ZeroCock"
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
            "images/LauraSex/Laura_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
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

        "Laura_TJ_LeftArm"
        subpixel True
        pos (0,80)
        transform_anchor True
        block:
            ease 1 ypos -40
            pause .2
            ease .4 ypos 80
            repeat
    contains:

        "Laura_TJ_HairMid"
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

        "Laura_TJ_HairTop"
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




image Laura_TJ_4:

    contains:

        "Laura_TJ_HairBack"
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

        "Laura_TJ_Body"
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

        "Laura_TJ_RightArmBack"
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
            "images/LauraSex/Laura_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
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









        "Laura_TJ_RightArm"
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

        "Laura_TJ_Head"
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
        "Laura_TJ_ZeroCock"
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
            "images/LauraSex/Laura_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
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

        "Laura_TJ_LeftArm"
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

        "Laura_TJ_HairMid"
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

        "Laura_TJ_HairTop"
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




image Laura_TJ_5:

    contains:

        "Laura_TJ_HairBack"
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















        "Laura_TJ_Body"
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
            "Laura_TJ_RightArmBack"
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
            "images/LauraSex/Laura_Titjob_RightTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Right.png",
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









        "Laura_TJ_RightArm"
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

        "Laura_TJ_Head"
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
        "Laura_TJ_ZeroCock"
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
            "images/LauraSex/Laura_Titjob_LeftTit.png"
        contains:
            ConditionSwitch(
                            "not LauraX.spunk['breasts']",Null(),
                            "True",       "images/LauraSex/Laura_Titjob_Spunk_Left.png",
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

        "Laura_TJ_LeftArm"
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

        "Laura_TJ_HairMid"
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

        "Laura_TJ_HairTop"
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




label Laura_TJ_Launch(Line=primary_action):
    if renpy.showing("Laura_sprite titjob"):
        return
    call hide_girl(LauraX)
    show Laura_sprite standing zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        ease 1 zoom 2.3 xpos 750 yoffset -100
    if Line == "L":
        if taboo:
            if len(Present) >= 2:
                if Present[0] != LauraX:
                    "[LauraX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != LauraX:
                    "[LauraX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[LauraX.name] casually glances around to see if anyone can see her."
        "[LauraX.name] bends over and places your cock between her breasts."

    if LauraX.outfit['bra'] and LauraX.outfit['top']:
        "She throws off her [LauraX.outfit['top']] and her [LauraX.outfit['bra']]."
    elif LauraX.outfit['top']:
        "She throws off her [LauraX.outfit['top']], baring her breasts underneath."
    elif LauraX.outfit['bra']:
        "She tugs off her [LauraX.outfit['bra']] and throws it aside."
    $ LauraX.outfit['top'] = 0
    $ LauraX.outfit['bra'] = 0
    $ LauraX.arm_pose = 0

    call Laura_First_Topless

    show blackscreen onlayer black with dissolve
    show Laura_sprite standing zorder LauraX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Laura_sprite titjob zorder 150:
        pos (700,520)
    $ Player.sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Laura_TJ_Reset:

    if not renpy.showing("Laura_sprite titjob"):
        return

    call hide_girl(LauraX)
    $ Player.sprite = 0

    show Laura_sprite standing zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        zoom 2.3 xpos 750 yoffset -100
    show Laura_sprite standing zorder LauraX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos LauraX.sprite_location yoffset 0
    "[LauraX.name] pulls back"
    show Laura_sprite standing zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos LauraX.sprite_location
    return











image GropeLeftBreast_Laura:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (195,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block:
            ease 1 rotate 30
            ease 1 rotate 60
            repeat

image GropeRightBreast_Laura:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat


image LickRightBreast_Laura:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (95,355)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (75,330)
            pause .5
            ease 1.5 rotate 30 pos (95,355)
            repeat

image LickLeftBreast_Laura:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (195,360)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (190,340)
            pause .5
            ease 1.5 rotate 30 pos (195,360)
            repeat

image GropeThigh_Laura:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (115,690)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (105,780)
            ease 1 rotate 100 pos (115,690)
            repeat

image GropePussy_Laura:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (120,620)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (120,605)
                ease .75 rotate 170 pos (120,620)
            choice:
                ease .5 rotate 190 pos (120,605)
                pause .25
                ease 1 rotate 170 pos (120,620)
            repeat

image FingerPussy_Laura:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (140,700)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (150,665)
                pause .5
                ease 1 rotate 50 pos (140,700)
            choice:
                ease .5 rotate 40 pos (150,665)
                pause .5
                ease 1.75 rotate 50 pos (140,700)
            choice:
                ease 2 rotate 40 pos (150,665)
                pause .5
                ease 1 rotate 50 pos (140,700)
            choice:
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
                ease .25 rotate 40 pos (150,665)
                ease .25 rotate 50 pos (140,700)
            repeat

image Lickpussy_Laura:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (155,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (145,630)
            linear .5 rotate -60 pos (135,640)
            easein 1 rotate 10 pos (155,650)
            repeat

image VibratorRightBreast_Laura:
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

image VibratorLeftBreast_Laura:
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

image VibratorPussy_Laura:
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

image VibratorAnal_Laura:
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

image VibratorPussyInsert_Laura:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Laura:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeBothBreast_Laura:
    contains:
        "GirlGropeLeftBreast_Laura"
    contains:
        "GirlGropeRightBreast_Laura"

image GirlGropeLeftBreast_Laura:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (220,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 pos (220,380)
            ease 1 rotate -10 pos (220,370)
            repeat

image GirlGropeRightBreast_Laura:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -40 pos (90,380)
            ease 1 rotate -10 pos (90,370)
            repeat

image GirlGropeThigh_Laura:
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

image GirlGropePussy_LauraSelf:
    contains:
        "GirlGropePussy_Laura"
        anchor (0.5,0.5)
        rotate -40

        pos (100,500)

image GirlGropePussy_Laura:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (130,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (130,590)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (130,590)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (130,590)
                ease .75 rotate 200 pos (130,595)
                ease .5 rotate 205 pos (130,590)
                ease .75 rotate 200 pos (130,595)
            choice:
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
                ease .3 rotate 205 pos (130,590)
                ease .3 rotate 200 pos (130,600)
            repeat

image GirlFingerPussy_Laura:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (140,605)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (140,610)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (140,610)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 ypos 620
                ease .75 rotate 200 ypos 625
                ease .5 rotate 205 ypos 620
                ease .75 rotate 200 ypos 625
            choice:
                ease .3 rotate 205 ypos 620
                ease .3 rotate 200 ypos 630
                ease .3 rotate 205 ypos 620
                ease .3 rotate 200 ypos 630
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
