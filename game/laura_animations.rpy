

image Laura_Sprite:
    LiveComposite(
        (402,965),
        (0,0), "Laura_Sprite_hairback",
        (0,0), ConditionSwitch(

            "not LauraX.underwear or not LauraX.underwear_pulled_down or (LauraX.legs and LauraX.legs != 'skirt' and not LauraX.upskirt)", Null(),
            "LauraX.underwear == 'wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Back.png",
            "LauraX.underwear == 'bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Back.png",
            "True", "images/LauraSprite/Laura_Sprite_Panties_Lace_Back.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.arms == 'gloves' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Glove_Back2.png",
            "LauraX.arms == 'gloves'", "images/LauraSprite/Laura_Sprite_Glove_Back1.png",
            "LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Arm_Back2.png",
            "True", "images/LauraSprite/Laura_Sprite_Arm_Back1.png",
            ),





        (0,0), ConditionSwitch(

            "LauraX.top_pulled_up and LauraX.top == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back_Up.png",
            "LauraX.top == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_Back.png",
            "True", Null(),
            ),

        (0,0), "images/LauraSprite/Laura_Sprite_Body.png",


        (0,0), ConditionSwitch(

            "LauraX.arms == 'gloves' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Glove_Mid2.png",
            "LauraX.arms == 'gloves'", "images/LauraSprite/Laura_Sprite_Glove_Mid1.png",
            "LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Arm_Mid2.png",
            "True", "images/LauraSprite/Laura_Sprite_Arm_Mid1.png",
            ),

        (0,0), "images/LauraSprite/Laura_Sprite_Tits.png",
        (0,0), ConditionSwitch(

            "LauraX.Water and LauraX.ArmPose == 1", "images/LauraSprite/Laura_Sprite_Water1.png",
            "LauraX.Water", "images/LauraSprite/Laura_Sprite_Water2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.arms == 'wrists' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Wrist2.png",
            "LauraX.arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist1.png",
            "True", Null(),
            ),


        (145,560), ConditionSwitch(

            "not LauraX.grool", Null(),
            "LauraX.legs and LauraX.legs != 'skirt' and not LauraX.upskirt", Null(),
            "LauraX.legs and LauraX.legs != 'other_skirt' and not LauraX.upskirt", Null(),
            "LauraX.underwear and not LauraX.underwear_pulled_down and LauraX.grool <= 1", Null(),
            "LauraX.grool == 1", ConditionSwitch(
                    "LauraX.underwear and LauraX.underwear_pulled_down", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "LauraX.legs and LauraX.legs != 'skirt'", AlphaMask("Wet_Drip","Laura_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Laura_Drip_Mask"),
                    ),
            "True", ConditionSwitch(
                    "LauraX.underwear and LauraX.underwear_pulled_down", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.legs and LauraX.legs != 'skirt'", AlphaMask("Wet_Drip2","Laura_Drip_MaskP"),
                    "LauraX.underwear", AlphaMask("Wet_Drip","Laura_Drip_Mask"),
                    "True", AlphaMask("Wet_Drip2","Laura_Drip_Mask"),
                    ),
            ),
        (145,560), ConditionSwitch(

            "'in' not in LauraX.spunk and 'anal' not in LauraX.spunk", Null(),
            "LauraX.legs and LauraX.legs != 'skirt' and not LauraX.upskirt", Null(),
            "LauraX.legs and LauraX.legs != 'other_skirt' and not LauraX.upskirt", Null(),
            "LauraX.underwear and not LauraX.underwear_pulled_down and LauraX.grool <= 1", Null(),
            "True", ConditionSwitch(
                    "LauraX.underwear and LauraX.underwear_pulled_down", AlphaMask("Spunk_Drip2","Laura_Drip_MaskP"),

                    "LauraX.underwear", AlphaMask("Spunk_Drip","Laura_Drip_Mask"),
                    "True", AlphaMask("Spunk_Drip2","Laura_Drip_Mask"),
                    ),
            ),
        (0,0), ConditionSwitch(

            "LauraX.pubes", "images/LauraSprite/Laura_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.piercings", Null(),
            "LauraX.underwear and not LauraX.underwear_pulled_down", Null(),
            "LauraX.legs != 'skirt' and LauraX.legs and not LauraX.upskirt", Null(),
            "LauraX.legs != 'other_skirt' and LauraX.legs and not LauraX.upskirt", Null(),
            "LauraX.piercings == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Pussy.png",
            "LauraX.piercings == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.hose == 'black stockings'", "images/LauraSprite/Laura_Sprite_BlackStockings.png",
            "LauraX.hose == 'stockings' or LauraX.hose == 'stockings_and_garterbelt'", "images/LauraSprite/Laura_Sprite_Stockings.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.hose == 'stockings_and_garterbelt' or LauraX.hose == 'garterbelt'", "images/LauraSprite/Laura_Sprite_Garters.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.underwear", Null(),
            "LauraX.underwear_pulled_down", ConditionSwitch(

                    "not LauraX.legs or LauraX.upskirt or LauraX.legs == 'skirt'", ConditionSwitch(

                            "LauraX.underwear == 'wolvie_panties' and LauraX.grool", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down_W.png",
                            "LauraX.underwear == 'wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_Down.png",
                            "LauraX.underwear == 'lace_panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace_Down.png",
                            "LauraX.underwear == 'bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini_Down.png",
                            "True", "images/LauraSprite/Laura_Sprite_Panties_Leather_Down.png",
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "LauraX.grool", ConditionSwitch(

                        "LauraX.underwear == 'wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie_W.png",
                        "LauraX.underwear == 'lace_panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png",
                        "LauraX.underwear == 'bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png",
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png",
                        ),
                    "True", ConditionSwitch(

                        "LauraX.underwear == 'wolvie_panties'", "images/LauraSprite/Laura_Sprite_Panties_Wolvie.png",
                        "LauraX.underwear == 'lace_panties'", "images/LauraSprite/Laura_Sprite_Panties_Lace.png",
                        "LauraX.underwear == 'bikini_bottoms'", "images/LauraSprite/Laura_Sprite_Panties_Bikini.png",
                        "True", "images/LauraSprite/Laura_Sprite_Panties_Leather.png",
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.legs", Null(),
            "LauraX.upskirt", ConditionSwitch(

                        "LauraX.legs == 'other_skirt'", "images/LauraSprite/Laura_Sprite_SkirtCos_Up.png",
                        "LauraX.legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt_Up.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(

                    "LauraX.legs == 'other_skirt'", "images/LauraSprite/Laura_Sprite_SkirtCos.png",
                    "LauraX.legs == 'skirt'", "images/LauraSprite/Laura_Sprite_Skirt.png",
                    "LauraX.grool", ConditionSwitch(

                        "LauraX.legs == 'leather_pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",
                        "LauraX.legs == 'mesh_pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",

                        "True", Null(),
                        ),
                    "True", ConditionSwitch(

                        "LauraX.legs == 'leather_pants'", "images/LauraSprite/Laura_Sprite_Pants_Leather.png",
                        "LauraX.legs == 'mesh_pants'", "images/LauraSprite/Laura_Sprite_Pants_Mesh.png",

                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "LauraX.legs == 'skirt' or LauraX.legs == 'other_skirt'", Null(),
            "LauraX.piercings == 'barbell'", ConditionSwitch(

                    "LauraX.legs and not LauraX.upskirt", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",
                    "LauraX.underwear and not LauraX.underwear_pulled_down", "images/LauraSprite/Laura_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "LauraX.piercings == 'ring'", ConditionSwitch(

                    "LauraX.legs and not LauraX.upskirt", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",
                    "LauraX.underwear and not LauraX.underwear_pulled_down", "images/LauraSprite/Laura_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.grool", Null(),
            "LauraX.legs and LauraX.grool <= 1", Null(),
            "LauraX.legs == 'other_skirt'", Null(),
            "LauraX.legs == 'skirt'", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Wetness.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.legs and not LauraX.upskirt", Null(),
            "'in' in LauraX.spunk or 'anal' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not LauraX.piercings", Null(),
            "LauraX.piercings == 'barbell'", "images/LauraSprite/Laura_Sprite_Barbell_Tits.png",
            "LauraX.piercings == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.neck == 'leash choker'", "images/LauraSprite/Laura_Sprite_Neck_Leash.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.bra == 'white tank'", "images/LauraSprite/Laura_Sprite_Bra_White_Up.png",
                    "LauraX.bra == 'leather_bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather_Up.png",
                    "LauraX.bra == 'wolvie_top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie_Up.png",
                    "LauraX.bra == 'bikini_top'", "images/LauraSprite/Laura_Sprite_Top_Bikini_Up.png",
                    "LauraX.bra == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Up.png",
                    "LauraX.bra == 'lace corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace_Up.png",
                    "True", Null(),
                    ),
            "LauraX.bra == 'white tank'", "images/LauraSprite/Laura_Sprite_Bra_White.png",
            "LauraX.bra == 'leather_bra'", "images/LauraSprite/Laura_Sprite_Bra_Leather.png",
            "LauraX.bra == 'wolvie_top'", "images/LauraSprite/Laura_Sprite_Top_Wolvie.png",
            "LauraX.bra == 'bikini_top'", "images/LauraSprite/Laura_Sprite_Top_Bikini.png",
            "LauraX.bra == 'corset'", "images/LauraSprite/Laura_Sprite_Top_Corset.png",
            "LauraX.bra == 'lace corset'", "images/LauraSprite/Laura_Sprite_Top_Corset_Lace.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not LauraX.legs or LauraX.upskirt", Null(),
            "LauraX.accessory == 'suspenders' and not LauraX.bra and not LauraX.top_pulled_up", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png",
            "LauraX.accessory == 'suspenders2'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders2.png",
            "LauraX.accessory == 'suspenders'", "images/LauraSprite/Laura_Sprite_Acc_Suspenders1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.top == 'jacket' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2_Up.png",
                    "LauraX.top == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1_Up.png",

                    "True", Null(),
                    ),
            "LauraX.top == 'jacket' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2.png",
            "LauraX.top == 'jacket'", "images/LauraSprite/Laura_Sprite_Jacket_A1.png",
            "LauraX.top == 'towel'", "images/LauraSprite/Laura_Sprite_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.piercings or (not LauraX.top and not LauraX.bra)", Null(),
            "LauraX.top == 'jacket'", Null(),
            "LauraX.piercings == 'barbell'",  "images/LauraSprite/Laura_Sprite_Barbell_TitsC.png",
            "LauraX.piercings == 'ring'", "images/LauraSprite/Laura_Sprite_Ring_TitsC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "'belly' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "renpy.showing('Laura_BJ_Animation')", Null(),
            "True", "Laura_Sprite_Head",
            ),
        (0,0), ConditionSwitch(

            "LauraX.arms == 'gloves' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Glove_Top2.png",
            "LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Arm_Left2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.Water and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Water2top.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.ArmPose == 2 and LauraX.arms == 'wrists'", "images/LauraSprite/Laura_Sprite_Wrist_Left2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.top == 'jacket' and LauraX.ArmPose == 2", "images/LauraSprite/Laura_Sprite_Jacket_A2Top.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.ArmPose == 2 and LauraX.Claws", "images/LauraSprite/Laura_Sprite_Claws2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "LauraX.ArmPose == 2 or 'hand' not in LauraX.spunk", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Hand.png",
            ),








        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != LauraX", Null(),


            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_LauraSelf",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Laura",

                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeRightBreast_Laura",

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
            "primary_action == 'suck breasts'", "LickRightBreast_Laura",
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
                    "offhand_action == 'fondle_breasts' and primary_action == 'suck breasts'", "GropeLeftBreast_Laura",

                    "True", "GropeRightBreast_Laura",

                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast_Laura",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck breasts'", "LickLeftBreast_Laura",
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
            "second_girl_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Laura",
            "second_girl_primary_action == 'suck breasts'", "LickRightBreast_Laura",
            "second_girl_primary_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Laura",


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
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Laura",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast_Laura",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Laura",

                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeRightBreast_Laura",

                    "girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Laura",

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
    anchor (0.6, 0.0)
    yoffset 15
    zoom .75

image Laura_Sprite_hairback:
    ConditionSwitch(

            "not LauraX.hair", Null(),
            "renpy.showing('Laura_BJ_Animation')", Null(),

            "LauraX.hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",
            "True", Null(),
            ),

    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_HairMid:
    ConditionSwitch(

            "not LauraX.hair", Null(),
            "renpy.showing('Laura_BJ_Animation')", Null(),

            "LauraX.hair == 'wet' or LauraX.Water", Null(),
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),
    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_HairTop:
    ConditionSwitch(

            "not LauraX.hair", Null(),
            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_OverSex.png",
            "LauraX.hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),

    anchor (0.6, 0.0)
    zoom .5

image Laura_Sprite_Head:
    LiveComposite(
        (806,806),
        (0,0), ConditionSwitch(

                "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_UnderSex.png",
                "True", Null(),
                ),
        (0,0), ConditionSwitch(

                "LauraX.blushing == '_blush2'", "images/LauraSprite/Laura_Sprite_Head_Blush2.png",
                "LauraX.blushing", "images/LauraSprite/Laura_Sprite_Head_Blush.png",
                "True", "images/LauraSprite/Laura_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(
            "'chin' not in LauraX.spunk", Null(),
            "renpy.showing('Laura_BJ_Animation') and action_speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png",
            "LauraX.mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            "LauraX.mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
            "LauraX.mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",
            "LauraX.mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
            "LauraX.mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
            "LauraX.mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "LauraX.mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",
            "LauraX.mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",
            "LauraX.mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "LauraX.mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",

            "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "'mouth' not in LauraX.spunk", Null(),
            "renpy.showing('Laura_BJ_Animation')", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png",
            "LauraX.mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "LauraX.mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "LauraX.mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "LauraX.mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.blushing >= 2", ConditionSwitch(
                    "LauraX.brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "LauraX.brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "LauraX.brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "LauraX.brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",
                    "LauraX.brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "LauraX.brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "LauraX.brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "LauraX.brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",
                    "LauraX.brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Laura Blink",
        (0,0), ConditionSwitch(

            "LauraX.top == 'jacket'", Null(),
            "renpy.showing('Laura_TJ_Animation')", Null(),
            "renpy.showing('Laura_Sex_Animation')", Null(),
            "LauraX.hair == 'wet' or LauraX.Water", Null(),
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "not LauraX.hair", Null(),
            "renpy.showing('Laura_TJ_Animation')", Null(),
            "renpy.showing('Laura_SexSprite')", "images/LauraSex/Laura_Sprite_Hair_Long_OverSex.png",
            "LauraX.hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.Water", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",

            ),
        (0,0), ConditionSwitch(

            "'hair' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",
            "'facial' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom .5

image Laura Blink:
    ConditionSwitch(
    "LauraX.eyes == 'sexy'", "images/LauraSprite/Laura_Sprite_Eyes_Squint.png",
    "LauraX.eyes == 'side'", "images/LauraSprite/Laura_Sprite_Eyes_Side.png",
    "LauraX.eyes == 'surprised'", "images/LauraSprite/Laura_Sprite_Eyes_Surprised.png",
    "LauraX.eyes == 'normal'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "LauraX.eyes == 'stunned'", "images/LauraSprite/Laura_Sprite_Eyes_Stunned.png",
    "LauraX.eyes == 'down'", "images/LauraSprite/Laura_Sprite_Eyes_Down.png",
    "LauraX.eyes == 'closed'", "images/LauraSprite/Laura_Sprite_Eyes_Closed.png",
    "LauraX.eyes == 'leftside'", "images/LauraSprite/Laura_Sprite_Eyes_Leftside.png",
    "LauraX.eyes == 'manic'", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    "LauraX.eyes == 'squint'", "Laura_Squint",
    "True", "images/LauraSprite/Laura_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/LauraSprite/Laura_Sprite_Eyes_Closed.png"
    .25
    repeat

image Laura_Squint:
    "images/LauraSprite/Laura_Sprite_Eyes_Normal.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/LauraSprite/Laura_Sprite_Eyes_Squint.png"
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











image Laura_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Laura_Doggy_Body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Top",
                    "action_speed > 1", "Laura_Doggy_Fuck_Top",
                    "action_speed ", "Laura_Doggy_Anal_Head_Top",
                    "True", "Laura_Doggy_Body",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Top",
                    "action_speed > 1", "Laura_Doggy_Fuck_Top",
                    "True", "Laura_Doggy_Body",
                    ),
            "Player.cock_position == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Laura_Doggy_Foot2_Top",
                    "action_speed ", "Laura_Doggy_Foot1_Top",
                    "True", "Laura_Doggy_Foot0_Top",
                    ),
            "True", "Laura_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Laura_Doggy_Ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Laura_Doggy_Fuck_Ass",
                    "action_speed ", "Laura_Doggy_Anal_Head_Ass",
                    "True", "Laura_Doggy_Ass",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Laura_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Laura_Doggy_Fuck_Ass",
                    "True", "Laura_Doggy_Ass",
                    ),
            "Player.cock_position == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Laura_Doggy_Foot2_Ass",
                    "action_speed ", "Laura_Doggy_Foot1_Ass",
                    "True", "Laura_Doggy_Foot0_Ass",
                    ),
            "True", "Laura_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.cock_position == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Laura_Doggy_Feet2",
                    "action_speed ", "Laura_Doggy_Feet1",
                    "True", "Laura_Doggy_Feet0",
                    ),
            "not Player.sprite and ShowFeet", "Laura_Doggy_Shins",
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

            "not LauraX.bra", Null(),









            "LauraX.bra == 'white tank'", "images/LauraDoggy/Laura_Doggy_Chest_Costume.png",
            "LauraX.bra == 'lace corset'", "images/LauraDoggy/Laura_Doggy_Chest_Corset.png",
            "LauraX.bra == 'corset'", "images/LauraDoggy/Laura_Doggy_Chest_Corset.png",
            "LauraX.bra == 'wolvie_top'", "images/LauraDoggy/Laura_Doggy_Chest_Wolvie.png",
            "LauraX.bra == 'bikini_top'", "images/LauraDoggy/Laura_Doggy_Chest_Bikini.png",
            "True", "images/LauraDoggy/Laura_Doggy_Chest_Tank.png",
            ),





        (0,0), ConditionSwitch(

            "not LauraX.legs", Null(),
            "LauraX.accessory == 'suspenders'", "images/LauraDoggy/Laura_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.arms == 'gloves'", "images/LauraDoggy/Laura_Doggy_Gloves.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.top", Null(),
            "LauraX.top == 'jacket'", "images/LauraDoggy/Laura_Doggy_Over_Jacket.png",
            "LauraX.top == 'towel' and not LauraX.top_pulled_up", "images/LauraDoggy/Laura_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in LauraX.spunk", "images/LauraDoggy/Laura_Doggy_Spunk_Back.png",
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

            "LauraX.Water or LauraX.hair == 'wet'", "images/LauraDoggy/Laura_Doggy_Hair_Wet_Back.png",
            "True", "images/LauraDoggy/Laura_Doggy_Hair_Long_Back.png",
            ),
        (0,0), ConditionSwitch(


            "LauraX.blushing", "images/LauraDoggy/Laura_Doggy_Head_Blush.png",
            "True", "images/LauraDoggy/Laura_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.mouth == 'normal'", "images/LauraDoggy/Laura_Doggy_Mouth_Smile.png",
            "LauraX.mouth == 'lipbite'", "images/LauraDoggy/Laura_Doggy_Mouth_Smile.png",
            "LauraX.mouth == 'sucking'", "images/LauraDoggy/Laura_Doggy_Mouth_Open.png",
            "LauraX.mouth == 'kiss'", "images/LauraDoggy/Laura_Doggy_Mouth_Kiss.png",
            "LauraX.mouth == 'sad'", "images/LauraDoggy/Laura_Doggy_Mouth_Sad.png",
            "LauraX.mouth == 'smile'", "images/LauraDoggy/Laura_Doggy_Mouth_Smile.png",
            "LauraX.mouth == 'grimace'", "images/LauraDoggy/Laura_Doggy_Mouth_Smile.png",
            "LauraX.mouth == 'surprised'", "images/LauraDoggy/Laura_Doggy_Mouth_Open.png",
            "LauraX.mouth == 'tongue'", "images/LauraDoggy/Laura_Doggy_Mouth_Tongue.png",
            "True", "images/LauraDoggy/Laura_Doggy_Mouth_Smile.png",
            ),



















        (0,0), ConditionSwitch(


            "LauraX.brows == 'angry'", "images/LauraDoggy/Laura_Doggy_Brows_Angry.png",
            "LauraX.brows == 'sad'", "images/LauraDoggy/Laura_Doggy_Brows_Sad.png",
            "LauraX.brows == 'surprised'", "images/LauraDoggy/Laura_Doggy_Brows_Surprised.png",

            "True", "images/LauraDoggy/Laura_Doggy_Brows_Normal.png",
            ),
        (0,0), "Laura Doggy Blink",





        (0,0), ConditionSwitch(

            "'facial' in LauraX.spunk", "images/LauraDoggy/Laura_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.Water or LauraX.hair == 'wet'", "images/LauraDoggy/Laura_Doggy_Hair_Wet.png",
            "True", "images/LauraDoggy/Laura_Doggy_Hair_Long.png",
            ),
        (0,0), ConditionSwitch(

            "'hair' in LauraX.spunk", "images/LauraDoggy/Laura_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )

































image Laura Doggy Blink:

    ConditionSwitch(
        "LauraX.eyes == 'sexy'", "images/LauraDoggy/Laura_Doggy_Eyes_Sexy.png",
        "LauraX.eyes == 'side'", "images/LauraDoggy/Laura_Doggy_Eyes_Side.png",
        "LauraX.eyes == 'normal'", "images/LauraDoggy/Laura_Doggy_Eyes_Sexy.png",
        "LauraX.eyes == 'closed'", "images/LauraDoggy/Laura_Doggy_Eyes_Closed.png",
        "LauraX.eyes == 'manic'", "images/LauraDoggy/Laura_Doggy_Eyes_Stunned.png",
        "LauraX.eyes == 'down'", "images/LauraDoggy/Laura_Doggy_Eyes_Sexy.png",
        "LauraX.eyes == 'stunned'", "images/LauraDoggy/Laura_Doggy_Eyes_Stunned.png",
        "LauraX.eyes == 'surprised'", "images/LauraDoggy/Laura_Doggy_Eyes_Surprised.png",
        "LauraX.eyes == 'squint'", "images/LauraDoggy/Laura_Doggy_Eyes_Sexy.png",
        "True", "images/LauraDoggy/Laura_Doggy_Eyes_Normal.png",
        ),






    3

    "images/LauraDoggy/Laura_Doggy_Eyes_Closed.png"
    .25
    repeat

image Laura_Doggy_Ass:
    LiveComposite(

        (420,750),








        (0,0), ConditionSwitch(

            "not LauraX.underwear_pulled_down or (LauraX.legs == 'pants' and not LauraX.upskirt)", Null(),
            "LauraX.underwear == 'wolvie_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Back.png",
            "LauraX.underwear == 'lace_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Lace_Back.png",
            "LauraX.underwear", "images/LauraDoggy/Laura_Doggy_Panties_Back.png",
            "True", Null(),
            ),
        (0,0), "images/LauraDoggy/Laura_Doggy_Ass.png",





        (0,0), ConditionSwitch(

            "LauraX.hose == 'black stockings'", "images/LauraDoggy/Laura_Doggy_Stocking.png",
            "LauraX.hose == 'stockings'", "images/LauraDoggy/Laura_Doggy_Hose.png",
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "Player.sprite and Player.cock_position == 'anal'", Null(),
            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.underwear_pulled_down or (LauraX.legs == 'pants' and not LauraX.upskirt)", Null(),
            "LauraX.underwear == 'wolvie_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Down.png",
            "LauraX.underwear == 'bikini_bottoms'", "images/LauraDoggy/Laura_Doggy_Panties_Bikini_Down.png",
            "LauraX.underwear", "images/LauraDoggy/Laura_Doggy_Panties_Black_Down.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Laura_Pussy_Fingering",
            "primary_action == 'dildo_pussy'", "Laura_Pussy_Fucking2",
            "Player.sprite and Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Laura_Pussy_Fucking3",
                    "action_speed > 1", "Laura_Pussy_Fucking2",
                    "action_speed ", "Laura_Pussy_Heading",
                    "True", "Laura_Pussy_Static",
                    ),
            "primary_action == 'eat_pussy'", "images/LauraDoggy/Laura_Doggy_Pussy_Open.png",
            "LauraX.legs and not LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Pussy_Closed.png",
            "LauraX.underwear and not LauraX.underwear_pulled_down", "images/LauraDoggy/Laura_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Laura_Pussy_Fingering",
            "primary_action == 'dildo_pussy'", "Laura_Pussy_Fucking2",
            "True", "images/LauraDoggy/Laura_Doggy_Pussy_Closed.png",
            ),


        (0,0), ConditionSwitch(

            "'in' in LauraX.spunk and Player.cock_position == 'in'",Null(),
            "'in' in LauraX.spunk ", "images/LauraDoggy/Laura_Doggy_SpunkPussyClosed.png",
            "LauraX.grool and Player.cock_position == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "LauraX.grool", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.pubes", Null(),
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "LauraX.legs == 'pants' and not LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Pubes_Panties.png",
            "LauraX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/LauraDoggy/Laura_Doggy_Pubes_Open.png",
            "LauraX.underwear_pulled_down", "images/LauraDoggy/Laura_Doggy_Pubes.png",
            "LauraX.underwear", "images/LauraDoggy/Laura_Doggy_Pubes_Panties.png",
            "LauraX.hose and LauraX.hose != 'stockings'", "images/LauraDoggy/Laura_Doggy_Pubes_Panties.png",
            "primary_action == 'eat_pussy'", "images/LauraDoggy/Laura_Doggy_Pubes_Open.png",
            "True", "images/LauraDoggy/Laura_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "LauraX.piercings == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_Ring.png",
            "LauraX.piercings == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Laura_Anal_Fucking2",
                    "action_speed > 1", "Laura_Anal_Fucking",
                    "action_speed ", "Laura_Anal_Heading",
                    "True", "Laura_Anal",
                    ),


            "LauraX.legs and not LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Asshole_Loose.png",
            "LauraX.underwear and not LauraX.underwear_pulled_down", "images/LauraDoggy/Laura_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Laura_Anal_Fingering",
            "primary_action == 'dildo_anal'", "Laura_Anal_Fucking",
            "LauraX.used_to_anal", "images/LauraDoggy/Laura_Doggy_Asshole_Loose.png",
            "True", "images/LauraDoggy/Laura_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(

            "'anal' not in LauraX.spunk or Player.sprite", Null(),
            "Player.cock_position == 'anal'", "images/LauraDoggy/Laura_Doggy_SpunkAnalOpen.png",
            "LauraX.used_to_anal", "images/LauraDoggy/Laura_Doggy_SpunkAnalLoose.png",
            "True", "images/LauraDoggy/Laura_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(

            "LauraX.underwear_pulled_down or not LauraX.underwear", Null(),
            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),


            "LauraX.underwear == 'wolvie_panties' and LauraX.grool", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie_Wet.png",
            "LauraX.underwear == 'wolvie_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Wolvie.png",
            "LauraX.underwear == 'lace_panties'", "images/LauraDoggy/Laura_Doggy_Panties_Lace.png",
            "LauraX.underwear == 'bikini_bottoms'", "images/LauraDoggy/Laura_Doggy_Panties_Bikini.png",
            "LauraX.grool", "images/LauraDoggy/Laura_Doggy_Panties_Black_Wet.png",
            "True", "images/LauraDoggy/Laura_Doggy_Panties_Black.png",
            ),














        (0,0), ConditionSwitch(

            "LauraX.legs == 'leather_pants'", ConditionSwitch(
                    "LauraX.upskirt or LauraX.underwear_pulled_down", Null(),

                    "True", "images/LauraDoggy/Laura_Doggy_Legs_Pants.png",
                    ),





            "LauraX.legs == 'other_skirt'", ConditionSwitch(
                    "LauraX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png",
                    "LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos_Up.png",
                    "True", "images/LauraDoggy/Laura_Doggy_Legs_SkirtCos.png",
                    ),
            "LauraX.legs == 'skirt'", ConditionSwitch(
                    "LauraX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/LauraDoggy/Laura_Doggy_Legs_Skirt_Up.png",
                    "LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Legs_Skirt_Up.png",
                    "True", "images/LauraDoggy/Laura_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.top == 'towel' and LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Over_TowelAss_Up.png",
            "LauraX.top == 'towel'", "images/LauraDoggy/Laura_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "LauraX.underwear_pulled_down or (not LauraX.underwear and LauraX.legs != 'leather_pants')", Null(),
            "LauraX.piercings == 'ring'", "images/LauraDoggy/Laura_Doggy_Pierce_RingC.png",
            "LauraX.piercings == 'barbell'", "images/LauraDoggy/Laura_Doggy_Pierce_BarbellC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in LauraX.spunk", "images/LauraDoggy/Laura_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "licking_pussy",
            "primary_action == 'eat_ass'", "licking_ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),
            "LauraX.legs == 'skirt' and LauraX.upskirt", "images/LauraDoggy/Laura_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/LauraDoggy/Laura_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),
            "LauraX.legs == 'skirt' and LauraX.upskirt and action_speed", AlphaMask("Zero_hotdog_moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "LauraX.legs == 'skirt' and LauraX.upskirt", AlphaMask("Zero_hotdog_static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "action_speed ", AlphaMask("Zero_hotdog_moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_hotdog_static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
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
            "not LauraX.hose", Null(),
            "LauraX.hose == 'stockings'", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png",
            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png",
            "LauraX.hose == 'black stockings'", "images/LauraDoggy/Laura_Doggy_Feet_Stockings_Back.png",
            "LauraX.hose == 'pantyhose'", "images/LauraDoggy/Laura_Doggy_Feet_Hose_Back.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.legs == 'leather_pants'", "images/LauraDoggy/Laura_Doggy_Feet_Pants.png",
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

















image Zero_Laura_Hotdog_Static:


    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)

image Zero_Laura_Hotdog_Moving:


    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Laura_Doggy_Static:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Laura_Doggy_Heading:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Laura_Doggy_Fucking2:

    contains:
        "Zero_cock_doggy_in"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Laura_Doggy_Fucking3:

    contains:
        "Zero_cock_doggy_in"
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

image Laura_Pussy_Mask_Static:


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


































image Laura_Pussy_Static:

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

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Laura_Doggy_Static", "Laura_Pussy_Mask_Static")
    contains:


        AlphaMask("Laura_PussyHole_Static", "Laura_Pussy_Hole_Mask_Static")

image Laura_Pussy_Hole_Mask_Static:

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

image Laura_PussyHole_Static:

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

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



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











        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
    contains:


        AlphaMask("Laura_Pussy_Heading_Flap", "Laura_Pussy_Hole_Mask")



image Laura_Pussy_Fucking2:

    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FBase.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Laura_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),



image Laura_Pussy_Fucking3:

    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FBase.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



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

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        "Zero_cock_doggy_in"
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

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Laura_Doggy_Anal_Heading", "Zero_Laura_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Laura_Doggy_Anal_Heading", "Laura_Doggy_Anal_Heading_Mask")

image Zero_Laura_Doggy_Anal_Heading:

    contains:
        "Zero_cock_doggy_in"
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
        "Zero_cock_doggy_in"
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

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Laura_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),


image Laura_Doggy_Anal_FullMask:
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullHole.png"
    contains:

        "images/LauraDoggy/Laura_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



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
        "Zero_cock_doggy_in"
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

            "LauraX.hose == 'stockings_and_garterbelt'", "images/LauraDoggy/Laura_Doggy_StockingsGarter.png",
            "LauraX.hose == 'garterbelt'", "images/LauraDoggy/Laura_Doggy_Garters.png",



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
                "Player.sprite", "Zero_cock_doggy_out",
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
        "Zero_cock_doggy_out"
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
        "Zero_cock_doggy_out"
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



label Laura_Doggy_Launch(Line=primary_action):
    if renpy.showing("Laura_Doggy_Animation"):
        return
    $ action_speed = 0
    call Laura_Hide (1)
    show Laura_Doggy_Animation zorder 150 at sprite_location(stage_center+150)
    with dissolve
    return

label Laura_Doggy_Reset:
    if not renpy.showing("Laura_Doggy_Animation"):
        return

    $ LauraX.ArmPose = 2
    $ LauraX.spriteVer = 0
    hide Laura_Doggy_Animation
    call Laura_Hide
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return









image Laura_SexSprite:

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
            "Player.cock_position == 'foot'", ConditionSwitch(

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
            "Player.cock_position == 'foot'", ConditionSwitch(

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
    anchor (.5,.5)


image Laura_Sex_hairback:

    "Laura_Sprite_hairback"
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
        "Laura_Sex_hairback"
    contains:



        ConditionSwitch(
                    "Player.cock_position == 'foot'", Null(),
                    "LauraX.arms == 'gloves'", "images/LauraSex/Laura_Sex_Hand_Gloved.png",
                    "True", "images/LauraSex/Laura_Sex_Hand.png"
                    )
    contains:

        ConditionSwitch(
            "not LauraX.top", Null(),
            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.top == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Back_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "LauraX.top == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Back.png",
                    "True", Null(),
                    ),
            )
    contains:

        "images/LauraSex/Laura_Sex_Body.png"
    contains:

        ConditionSwitch(
            "not LauraX.piercings", Null(),
            "LauraX.piercings == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits.png",
            "LauraX.piercings == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.neck == 'leash choker'", "images/LauraSex/Laura_Sex_Leash.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.hose == 'stockings_and_garterbelt' or LauraX.hose == 'garterbelt'", "images/LauraSex/Laura_Sex_Garter.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.bra", Null(),
            "LauraX.top_pulled_up",ConditionSwitch(

                    "not LauraX.bra", Null(),
                    "LauraX.bra == 'white tank'", "images/LauraSex/Laura_Sex_WhiteTank_Up.png",
                    "LauraX.bra == 'leather_bra'", "images/LauraSex/Laura_Sex_Bra_Leather_Up.png",
                    "LauraX.bra == 'wolvie_top'", "images/LauraSex/Laura_Sex_Top_Wolvie_Up.png",
                    "LauraX.bra == 'corset'", "images/LauraSex/Laura_Sex_Corset_Up.png",
                    "LauraX.bra == 'lace corset'", "images/LauraSex/Laura_Sex_Corset_Lace_Up.png",
                    "LauraX.bra == 'bikini_top'", "images/LauraSex/Laura_Sex_Top_Bikini_Up.png",


                    "True", Null(),
                    ),

            "LauraX.bra == 'white tank'", "images/LauraSex/Laura_Sex_WhiteTank.png",
            "LauraX.bra == 'leather_bra'", "images/LauraSex/Laura_Sex_Bra_Leather.png",
            "LauraX.bra == 'wolvie_top'", "images/LauraSex/Laura_Sex_Top_Wolvie.png",
            "LauraX.bra == 'corset'", "images/LauraSex/Laura_Sex_Corset.png",
            "LauraX.bra == 'lace corset'", "images/LauraSex/Laura_Sex_Corset_Lace.png",
            "LauraX.bra == 'bikini_top'", "images/LauraSex/Laura_Sex_Top_Bikini.png",


            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.piercings or LauraX.top_pulled_up", Null(),
            "LauraX.piercings == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Tits_C.png",
            "LauraX.piercings == 'ring'", "images/LauraSex/Laura_Sex_Ring_Tits_C.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.legs", Null(),
            "LauraX.accessory == 'suspenders' and not LauraX.bra and not LauraX.top_pulled_up", "images/LauraSex/Laura_Sex_Suspenders.png",
            "LauraX.accessory == 'suspenders2'", "images/LauraSex/Laura_Sex_Suspenders.png",
            "LauraX.accessory == 'suspenders'", "images/LauraSex/Laura_Sex_Suspenders_Up.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not LauraX.top", Null(),
            "LauraX.top_pulled_up", ConditionSwitch(

                    "LauraX.top == 'jacket'", "images/LauraSex/Laura_Sex_Jacket_Up.png",

                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "LauraX.top == 'jacket'", "images/LauraSex/Laura_Sex_Jacket.png",

                    "True", Null(),
                    ),
            )
    contains:

        ConditionSwitch(
            "'belly' in LauraX.spunk", "images/LauraSex/Laura_Sex_Spunk_Belly.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
                "'tits' not in LauraX.spunk", Null(),
                "True", "images/LauraSex/Laura_Sex_Spunk_Tits.png",
                )
    contains:
        ConditionSwitch(

                "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Laura_Sex_Lick_Breasts",
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
    "licking"
    zoom 0.7
    offset (565,290)

image Laura_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.5
    offset (360,-280)

image Laura_Sex_Legs:

    contains:

        ConditionSwitch(
            "LauraX.legs == 'skirt'", "images/LauraSex/Laura_Sex_Skirt_Back.png",
            "True", Null(),
            )
    contains:







        ConditionSwitch(
            "Player.cock_position == 'foot'", "images/LauraSex/Laura_Sex_Legs_Foot.png",
            "True", "images/LauraSex/Laura_Sex_Legs_High.png",
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'anal' and action_speed > 1", "images/LauraSex/Laura_Sex_Anus_L.png",
            "Player.cock_position == 'anal' and action_speed > 0", "images/LauraSex/Laura_Sex_Anus_M.png",
            "'anal' in LauraX.spunk", "images/LauraSex/Laura_Sex_Anus_M.png",
            "True", "images/LauraSex/Laura_Sex_Anus_S.png",
            )
    contains:

        ConditionSwitch(
            "'anal' not in LauraX.spunk", Null(),
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
            "'in' not in LauraX.spunk", Null(),
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
            "LauraX.piercings == 'barbell' and Player.cock_position == 'in' and action_speed > 1", "images/LauraSex/Laura_Sex_Barbell_Pussy_O.png",
            "LauraX.piercings == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy.png",
            "LauraX.piercings == 'ring' and Player.cock_position == 'in' and action_speed > 1", "images/LauraSex/Laura_Sex_Ring_Pussy_O.png",
            "LauraX.piercings == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.underwear_pulled_down", Null(),

            "LauraX.underwear == 'bikini_bottoms'", "images/LauraSex/Laura_Sex_Panties_Bikini.png",
            "LauraX.underwear == 'wolvie_panties'", "images/LauraSex/Laura_Sex_Panties_Wolvie.png",
            "LauraX.underwear == 'lace_panties'", "images/LauraSex/Laura_Sex_Panties_Lace.png",
            "LauraX.underwear", "images/LauraSex/Laura_Sex_Panties_Black.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "Player.cock_position == 'foot' and (LauraX.hose == 'stockings_and_garterbelt' or LauraX.hose == 'stockings')", "images/LauraSex/Laura_Sex_Stockings_Base_Foot.png",
            "Player.cock_position == 'foot' and LauraX.hose == 'black stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Base_Foot.png",
            "LauraX.hose == 'black stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Base_Up.png",
            "LauraX.hose == 'stockings_and_garterbelt' or LauraX.hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Base_Up.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "LauraX.legs == 'skirt' or LauraX.legs == 'other_skirt'", "images/LauraSex/Laura_Sex_Skirt.png",
            "LauraX.upskirt", Null(),
            "LauraX.legs == 'leather_pants' and Player.cock_position == 'foot'", "images/LauraSex/Laura_Sex_Pants_Base_Foot.png",
            "LauraX.legs == 'leather_pants'", "images/LauraSex/Laura_Sex_Pants_Base_Up.png",
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


            "LauraX.piercings == 'barbell'", "images/LauraSex/Laura_Sex_Barbell_Pussy_C.png",
            "LauraX.piercings == 'ring'", "images/LauraSex/Laura_Sex_Ring_Pussy_C.png",
            "True", Null(),
            )
    contains:







        ConditionSwitch(
            "Player.cock_position == 'foot'", "Laura_Footjob_Foot",
            "True", "Laura_Sex_Foot",
            )
    transform_anchor True
    zoom 1





image Laura_Sex_Lick_Pussy:
    "licking"
    zoom 0.8
    offset (720,610)

image Laura_Sex_Lick_Ass:
    "licking"
    zoom 0.8
    offset (730,700)


image Laura_Sex_Foot:




    contains:

        ConditionSwitch(
            "LauraX.hose == 'stockings_and_garterbelt' or LauraX.hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Up.png",
            "LauraX.hose == 'black stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Up.png",
            "True", "images/LauraSex/Laura_Sex_FootHigh.png"
            )
    contains:

        ConditionSwitch(
            "LauraX.upskirt", Null(),
            "LauraX.legs == 'leather_pants'", "images/LauraSex/Laura_Sex_Pants_Up.png",
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
        "Zero_cock_doggy_in"
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
        "Zero_cock_doggy_in"
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
                "'in' not in LauraX.spunk", Null(),
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
        "Zero_cock_doggy_in"
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
                "'in' not in LauraX.spunk", Null(),
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
        "Zero_cock_doggy_in"
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
                "'in' not in LauraX.spunk", Null(),
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
        "Zero_cock_doggy_in"
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
        "Zero_cock_doggy_in"
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
        "Zero_cock_doggy_in"
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
                "'anal' not in LauraX.spunk", Null(),
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
        "Zero_cock_doggy_in"
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
                "'anal' not in LauraX.spunk", Null(),
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
        "Zero_cock_doggy_in"
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
                "'anal' not in LauraX.spunk", Null(),
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
        "Zero_cock_doggy_in"
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
            "Player.sprite", "Zero_cock_doggy_in",
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
        "Zero_cock_doggy_in"
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
        "Zero_cock_doggy_in"
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
            "LauraX.hose == 'stockings_and_garterbelt' or LauraX.hose == 'stockings'", "images/LauraSex/Laura_Sex_Stockings_Foot.png",
            "LauraX.hose == 'black stockings'", "images/LauraSex/Laura_Sex_BlackStockings_Foot.png",
            "True", "images/LauraSex/Laura_Sex_Foot.png"
            )
    contains:

        ConditionSwitch(
            "LauraX.upskirt", Null(),
            "LauraX.legs == 'leather_pants'", "images/LauraSex/Laura_Sex_Pants_Foot.png",
            "True", Null(),
            )
    offset (1105,140)
    zoom 1

image Laura_Sex_Zero_Anim_F:

    "Zero_Zero_cock_blowjob"
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

        "Zero_cock_doggy_in"

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




label Laura_Sex_Launch(Line=primary_action):
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
    elif Line == "solo":
        $ Player.sprite = 0
        $ Player.cock_position = "out"
    elif Line == "hotdog":
        $ Player.cock_position = "out"
    elif Line == "footjob":
        $ ShowFeet = 1
        $ Player.cock_position = "footjob"
    elif Line == "massage":
        $ Player.sprite = 0
        $ Player.cock_position = 0
    else:
        $ Player.sprite = 0
        $ Player.cock_position = "out"
        $ action_speed = 0
    $ primary_action = Line

    if LauraX.pose == "doggy":
        call Laura_Doggy_Launch (Line)
        return
    if renpy.showing("Laura_SexSprite"):
        return
    call Laura_Hide (1)
    $ action_speed = 0

    if primary_action == "in" or primary_action == "anal":
        if LauraX.legs or LauraX.HoseNum() >= 5:
            $ LauraX.upskirt = 1
        if LauraX.underwear:
            $ LauraX.underwear_pulled_down = 1

    show Laura_SexSprite zorder 150:
        pos (450,500)
    with dissolve
    return

label Laura_Sex_Reset:
    if renpy.showing("Laura_Doggy_Animation"):
        call Laura_Doggy_Reset
        return
    if not renpy.showing("Laura_SexSprite"):
        return
    $ LauraX.ArmPose = 2
    hide Laura_SexSprite
    call Laura_Hide
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return












image Laura_BJ_Animation:

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














image Laura_Sprite_BJ_hairback:


    ConditionSwitch(

            "not LauraX.hair", Null(),
            "LauraX.hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Under.png",
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Under.png",
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
            "'chin' not in LauraX.spunk", Null(),
            "action_speed >= 2", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(
            "action_speed >= 2", "images/LauraSprite/Laura_Sprite_Mouth_SuckingBJ.png",
            "action_speed == 1", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",
            "LauraX.mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            "LauraX.mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Mouth_Lipbite.png",
            "LauraX.mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Mouth_Sucking.png",
            "LauraX.mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Mouth_Kiss.png",
            "LauraX.mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Mouth_Sad.png",
            "LauraX.mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "LauraX.mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Mouth_Surprised.png",
            "LauraX.mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Mouth_Tongue.png",
            "LauraX.mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Mouth_Smile.png",
            "LauraX.mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Mouth_Smirk.png",

            "True", "images/LauraSprite/Laura_Sprite_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "'mouth' not in LauraX.spunk", Null(),
            "action_speed >= 2", "images/LauraSprite/Laura_Sprite_Spunk_MouthSuck.png",
            "action_speed == 1", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.mouth == 'normal'", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            "LauraX.mouth == 'lipbite'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "LauraX.mouth == 'sucking'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.mouth == 'kiss'", "images/LauraSprite/Laura_Sprite_Spunk_MouthKiss.png",
            "LauraX.mouth == 'sad'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.mouth == 'smile'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.mouth == 'surprised'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSad.png",
            "LauraX.mouth == 'tongue'", "images/LauraSprite/Laura_Sprite_Spunk_MouthTongue.png",
            "LauraX.mouth == 'grimace'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmile.png",
            "LauraX.mouth == 'smirk'", "images/LauraSprite/Laura_Sprite_Spunk_MouthSmirk.png",
            "True", "images/LauraSprite/Laura_Sprite_Spunk_MouthNeutral.png",
            ),
        (0,0), ConditionSwitch(
            "action_speed >= 2 and 'mouth' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_SpunkSuckingO.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "action_speed == 1", "images/LauraSprite/Laura_Sprite_Wet_Tongue.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "LauraX.blushing >= 2", ConditionSwitch(
                    "LauraX.brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    "LauraX.brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry_B.png",
                    "LauraX.brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad_B.png",
                    "LauraX.brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised_B.png",
                    "LauraX.brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused_B.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "LauraX.brows == 'normal'", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    "LauraX.brows == 'angry'", "images/LauraSprite/Laura_Sprite_Brows_Angry.png",
                    "LauraX.brows == 'sad'", "images/LauraSprite/Laura_Sprite_Brows_Sad.png",
                    "LauraX.brows == 'surprised'", "images/LauraSprite/Laura_Sprite_Brows_Surprised.png",
                    "LauraX.brows == 'confused'", "images/LauraSprite/Laura_Sprite_Brows_Confused.png",
                    "True", "images/LauraSprite/Laura_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Laura Blink",
        (0,0), ConditionSwitch(

            "LauraX.top == 'jacket'", Null(),
            "LauraX.hair == 'wet' or LauraX.Water", Null(),
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "not LauraX.hair", Null(),
            "LauraX.hair == 'wet' or LauraX.Water", "images/LauraSprite/Laura_Sprite_Hair_Wet_Over.png",
            "LauraX.hair", "images/LauraSprite/Laura_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not LauraX.Water", Null(),
            "True", "images/LauraSprite/Laura_Sprite_Head_Wet.png",

            ),
        (0,0), ConditionSwitch(

            "'hair' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial2.png",
            "'facial' in LauraX.spunk", "images/LauraSprite/Laura_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )



image Laura_BlowCock_Mask:


    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)





















image Laura_BJ_Body_0:

    contains:

        "Laura_Sprite_BJ_hairback"
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

        "Laura_Sprite"
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





        AlphaMask("Zero_cock_blowjob", "Laura_BlowCock_Mask")
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

        "Laura_Sprite_BJ_hairback"
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

        "Laura_Sprite"
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





        AlphaMask("Zero_cock_blowjob", "Laura_BlowCock_Mask")
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

        "Laura_Sprite_BJ_hairback"
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

        "Laura_Sprite"
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





        AlphaMask("Zero_cock_blowjob", "Laura_BlowCock_Mask")
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

        "Laura_Sprite_BJ_hairback"
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

        "Laura_Sprite"
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





        AlphaMask("Zero_cock_blowjob", "Laura_BlowCock_Mask_3")
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

        "Laura_Sprite_BJ_hairback"
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

        "Laura_Sprite"
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





        AlphaMask("Zero_cock_blowjob", "Laura_BlowCock_Mask_4")
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

        "Laura_Sprite_BJ_hairback"
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

        "Laura_Sprite"
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





        AlphaMask("Zero_cock_blowjob", "Laura_BlowCock_Mask")
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

        "Laura_Sprite_BJ_hairback"
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

        "Laura_Sprite"
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





        AlphaMask("Zero_cock_blowjob", "Laura_BlowCock_Mask_6")
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

    $ LauraX.ArmPose = 1
    if renpy.showing("Laura_BJ_Animation"):
        return

    call Laura_Hide
    if Line == "L" or Line == "cum":
        show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(stage_center):
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    $ action_speed = 0
    if Line == "L":
        if Taboo:
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

    show Laura_Sprite zorder LauraX.sprite_layer:
        alpha 0
    show Laura_BJ_Animation zorder 150:
        pos (645,510)
    return

label Laura_BJ_Reset:
    if not renpy.showing("Laura_BJ_Animation"):
        return

    call Laura_Hide
    $ action_speed = 0

    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Laura_Sprite zorder LauraX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
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

image Laura_HJ_Animation:
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Laura_Hand_Under"),
            "action_speed == 1", At("Laura_Hand_Under", Laura_Hand_1()),
            "action_speed >= 2", At("Laura_Hand_Under", Laura_Hand_2()),
            "action_speed ", Null(),
            ),
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1L()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2L()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(

            "not action_speed", Transform("Laura_Hand_Over"),
            "action_speed == 1", At("Laura_Hand_Over", Laura_Hand_1()),
            "action_speed >= 2", At("Laura_Hand_Over", Laura_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Laura_HJ_Launch(Line=primary_action):
    if renpy.showing("Laura_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call Laura_Hide
    if Line == "L":
        show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)
    else:
        show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-150,200)
        with dissolve

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause .5
    $ LauraX.ArmPose = 1
    show Laura_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:

        offset (250,250)
    return

label Laura_HJ_Reset:
    if not renpy.showing("Laura_HJ_Animation"):
        return
    $ action_speed = 0
    $ LauraX.ArmPose = 1
    hide Laura_HJ_Animation with easeoutbottom
    call Laura_Hide
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        zoom 1.7 offset (-50,200)
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return










image Laura_TJ_Animation:

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




image Laura_TJ_hairback:

    "Laura_Sprite_hairback"
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

    "Zero_Zero_cock_blowjob"
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
                        "not LauraX.neck",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Neck_[LauraX.neck].png",
                        )
    contains:
        ConditionSwitch(
                        "'tits' not in LauraX.spunk",Null(),
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
                        "not LauraX.arms",Null(),
                        "LauraX.arms == 'gloves'",       "images/LauraSex/Laura_Titjob_LeftGlove.png",
                        "True",       "images/LauraSex/Laura_Titjob_wrists.png",
                        )
    contains:

        ConditionSwitch(
                        "not LauraX.piercings",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Left_[LauraX.piercings].png",
                        )

image Laura_TJ_RightArm:

    contains:
        "images/LauraSex/Laura_Titjob_RightHand.png"
    contains:
        ConditionSwitch(
                        "LauraX.arms == 'gloves'",       "images/LauraSex/Laura_Titjob_RightGlove.png",
                        "True", Null(),
                        )
    contains:

        ConditionSwitch(
                        "not LauraX.piercings",Null(),
                        "True",       "images/LauraSex/Laura_Titjob_Right_[LauraX.piercings].png",
                        )

image Laura_TJ_RightArmBack:

    contains:
        "images/LauraSex/Laura_Titjob_RightHandBack.png"
    contains:
        ConditionSwitch(
                        "LauraX.arms == 'gloves'",       "images/LauraSex/Laura_Titjob_RightGloveBack.png",
                        "True", Null(),
                        )




image Laura_TJ_0:

    contains:

        "Laura_TJ_hairback"
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
                            "'tits' not in LauraX.spunk",Null(),
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
                            "'tits' not in LauraX.spunk",Null(),
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

        "Laura_TJ_hairback"
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
                            "'tits' not in LauraX.spunk",Null(),
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
                            "'tits' not in LauraX.spunk",Null(),
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

        "Laura_TJ_hairback"
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
                            "'tits' not in LauraX.spunk",Null(),
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
                            "'tits' not in LauraX.spunk",Null(),
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

        "Laura_TJ_hairback"
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
                            "'tits' not in LauraX.spunk",Null(),
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
                            "'tits' not in LauraX.spunk",Null(),
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

        "Laura_TJ_hairback"
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
                            "'tits' not in LauraX.spunk",Null(),
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
                            "'tits' not in LauraX.spunk",Null(),
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
    if renpy.showing("Laura_TJ_Animation"):
        return
    call Laura_Hide
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        ease 1 zoom 2.3 xpos 750 yoffset -100
    if Line == "L":
        if Taboo:
            if len(Present) >= 2:
                if Present[0] != LauraX:
                    "[LauraX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != LauraX:
                    "[LauraX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[LauraX.name] casually glances around to see if anyone can see her."
        "[LauraX.name] bends over and places your cock between her breasts."

    if LauraX.bra and LauraX.top:
        "She throws off her [LauraX.top] and her [LauraX.bra]."
    elif LauraX.top:
        "She throws off her [LauraX.top], baring her breasts underneath."
    elif LauraX.bra:
        "She tugs off her [LauraX.bra] and throws it aside."
    $ LauraX.top = ""
    $ LauraX.bra = ""
    $ LauraX.ArmPose = 0

    call Laura_First_Topless

    show blackscreen onlayer black with dissolve
    show Laura_Sprite zorder LauraX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Laura_TJ_Animation zorder 150:
        pos (700,520)
    $ Player.sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Laura_TJ_Reset:

    if not renpy.showing("Laura_TJ_Animation"):
        return

    call Laura_Hide
    $ Player.sprite = 0

    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        zoom 2.3 xpos 750 yoffset -100
    show Laura_Sprite zorder LauraX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos LauraX.sprite_location yoffset 0
    "[LauraX.name] pulls back"
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos LauraX.sprite_location
    return













label Laura_Kissing_Launch(T=primary_action, Set=1):
    call Laura_Hide
    $ primary_action = T
    $ LauraX.pose = "kiss" if Set else LauraX.pose
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location)
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Laura_Kissing_Smooch:
    $ LauraX.change_face("_kiss")
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos LauraX.sprite_location zoom 1
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        zoom 1
    $ LauraX.change_face("_sexy")
    return

label Laura_Breasts_Launch(T=primary_action, Set=1):
    call Laura_Hide
    $ primary_action = T
    $ LauraX.pose = "breasts" if Set else LauraX.pose
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Laura_Middle_Launch(T=primary_action, Set=1):
    call Laura_Hide
    $ primary_action = T
    $ LauraX.pose = "mid" if Set else LauraX.pose
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Laura_Pussy_Launch(T=primary_action, Set=1):
    call Laura_Hide
    $ primary_action = T
    $ LauraX.pose = "pussy" if Set else LauraX.pose
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Laura_Pos_Reset(T=0, Set=0):
    if LauraX.location != bg_current:
        return
    call Laura_Hide
    show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location):
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Laura_Sprite zorder LauraX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (LauraX.sprite_location,50)
    $ LauraX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Laura_Hide(Sprite=0):
    call Laura_Sex_Reset




    hide Laura_SexSprite
    hide Laura_Doggy_Animation
    hide Laura_HJ_Animation
    hide Laura_BJ_Animation
    hide Laura_TJ_Animation
    if Sprite:
        hide Laura_Sprite
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
