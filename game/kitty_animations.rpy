

image Kitty_Sprite:
    LiveComposite(
        (480,960),
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_hairback",
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == 'dress' and KittyX.upskirt", "images/KittySprite/Kitty_Sprite_Legs_Dress_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.ArmPose == 1", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.top == 'pink_top' and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Under_Pink2.png",
            "KittyX.top == 'pink_top'", "images/KittySprite/Kitty_Sprite_Under_Pink1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.ArmPose != 1 and KittyX.pubes", "images/KittySprite/Kitty_Sprite_Body_Hair2.png",
            "KittyX.ArmPose != 1", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",
            "KittyX.pubes", "images/KittySprite/Kitty_Sprite_Body_Hair1.png",
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",
            ),







        (0,0), ConditionSwitch(

            "not KittyX.piercings or (KittyX.underwear and not KittyX.underwear_pulled_down)", Null(),
            "KittyX.piercings == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",
            ),






























        (0,0), ConditionSwitch(

            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittySprite/Kitty_Sprite_Hose_StockingGarter.png",
            "KittyX.hose == 'garterbelt'", "images/KittySprite/Kitty_Sprite_Hose_Garter.png",
            "KittyX.hose == 'stockings'", "images/KittySprite/Kitty_Sprite_Hose_Stockings.png",
            "KittyX.hose == 'knee stockings'", "images/KittySprite/Kitty_Sprite_Hose_Knee.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.underwear_pulled_down or (KittyX.legs and KittyX.legs != 'blue_skirt' and not KittyX.upskirt)", ConditionSwitch(


                    "KittyX.grool", ConditionSwitch(

                            "KittyX.underwear == 'green_panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
                            "KittyX.underwear == 'lace_panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",
                            "KittyX.underwear == 'bikini_bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png",
                            "True", Null(),
                            ),
                    "True", ConditionSwitch(

                            "KittyX.underwear == 'green_panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
                            "KittyX.underwear == 'lace_panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
                            "KittyX.underwear == 'bikini_bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png",
                            "True", Null(),
                            ),
                    ),
            "KittyX.grool", ConditionSwitch(


                    "KittyX.underwear == 'green_panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
                    "KittyX.underwear == 'lace_panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
                    "KittyX.underwear == 'bikini_bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(


                    "KittyX.underwear == 'green_panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
                    "KittyX.underwear == 'lace_panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
                    "KittyX.underwear == 'bikini_bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png",
                    "True", Null(),
                    ),
            ),


        (0,0), ConditionSwitch(

            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'pantyhose'", "images/KittySprite/Kitty_Sprite_Hose_Pantyhose.png",
            "KittyX.hose == 'ripped_pantyhose'", "images/KittySprite/Kitty_Sprite_Hose_RippedPantyhose.png",
            "True", Null(),
            ),
        (225,560), ConditionSwitch(

            "not KittyX.grool", Null(),
            "KittyX.legs and not KittyX.upskirt", Null(),
            "KittyX.underwear and not KittyX.underwear_pulled_down and KittyX.grool <= 1", Null(),
            "KittyX.grool == 1", ConditionSwitch(
                    "KittyX.underwear and KittyX.underwear_pulled_down", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "KittyX.legs", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Kitty_Drip_Mask"),
                    ),
            "True", ConditionSwitch(
                    "KittyX.underwear and KittyX.underwear_pulled_down", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "KittyX.legs", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "KittyX.underwear", AlphaMask("Wet_Drip","Kitty_Drip_Mask"),
                    "True", AlphaMask("Wet_Drip2","Kitty_Drip_Mask"),
                    ),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs or not KittyX.grool", Null(),
            "KittyX.underwear and not KittyX.underwear_pulled_down and KittyX.grool < 2", Null(),
            "KittyX.underwear and not KittyX.underwear_pulled_down", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "KittyX.grool == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),
        (225,560), ConditionSwitch(

            "'in' not in KittyX.spunk and 'anal' not in KittyX.spunk", Null(),
            "KittyX.legs and not KittyX.upskirt", Null(),
            "True", ConditionSwitch(
                    "KittyX.underwear and KittyX.underwear_pulled_down", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "KittyX.legs", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Kitty_Drip_Mask"),
                    ),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == 'blue_skirt' and KittyX.upskirt", "images/KittySprite/Kitty_Sprite_Skirt_Up.png",
            "KittyX.legs == 'blue_skirt'", "images/KittySprite/Kitty_Sprite_Skirt.png",
            "KittyX.legs == 'dress' and KittyX.upskirt", "images/KittySprite/Kitty_Sprite_Legs_Dress_Up.png",
            "KittyX.legs == 'dress'", "images/KittySprite/Kitty_Sprite_Legs_Dress.png",
            "not KittyX.legs or KittyX.upskirt", Null(),
            "KittyX.legs == 'capris'", "images/KittySprite/Kitty_Sprite_Pants_Blue.png",
            "KittyX.legs == 'black jeans'", "images/KittySprite/Kitty_Sprite_Pants_Black.png",
            "KittyX.grool and KittyX.legs == 'yoga_pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png",
            "KittyX.legs == 'yoga_pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png",
            "KittyX.grool and KittyX.legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png",
            "KittyX.legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.ArmPose != 1", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),
            ),

        (0,0), "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
        (0,0), ConditionSwitch(

            "not KittyX.piercings", Null(),
            "KittyX.piercings == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",
            ),














        (0,0), ConditionSwitch(

            "KittyX.neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "KittyX.neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "KittyX.neck == 'flower necklace'", "images/KittySprite/Kitty_Sprite_Necklace3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.bra", Null(),
            "not KittyX.top_pulled_up", ConditionSwitch(

                    "KittyX.ArmPose != 1 and KittyX.bra == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
                    "KittyX.ArmPose != 1 and KittyX.bra == 'bikini_top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
                    "KittyX.ArmPose != 1 and KittyX.bra == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress2.png",
                    "KittyX.bra == 'bikini_top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
                    "KittyX.bra == 'lace_bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
                    "KittyX.bra == 'sports_bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
                    "KittyX.bra == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
                    "KittyX.bra == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
                    "KittyX.bra == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress1.png",
                    "True", Null(),
                    ),
            "KittyX.top and KittyX.top != 'towel'", ConditionSwitch(



                    "KittyX.bra == 'bikini_top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                    "KittyX.bra == 'lace_bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_UpS.png",
                    "KittyX.bra == 'sports_bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_UpS.png",
                    "KittyX.bra == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                    "KittyX.bra == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",
                    "KittyX.bra == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress_UpS.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "KittyX.ArmPose != 1", ConditionSwitch(

                            "KittyX.bra == 'bikini_top'", "images/KittySprite/Kitty_Sprite_Bikini2_Up.png",
                            "KittyX.bra == 'lace_bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace2_Up.png",
                            "KittyX.bra == 'sports_bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport2_Up.png",
                            "KittyX.bra == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic2_Up.png",
                            "KittyX.bra == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2_Up.png",
                            "KittyX.bra == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress_Up.png",
                            "True", Null(),
                            ),
                    "True", ConditionSwitch(

                            "KittyX.bra == 'bikini_top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                            "KittyX.bra == 'lace_bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_Up.png",
                            "KittyX.bra == 'sports_bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_Up.png",
                            "KittyX.bra == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                            "KittyX.bra == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_Up.png",
                            "KittyX.bra == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress_Up.png",
                            "True", Null(),
                            ),
                    "True", Null(),
                    ),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.piercings or not KittyX.bra or KittyX.top_pulled_up", Null(),
            "KittyX.piercings == 'ring' and KittyX.legs", "images/KittySprite/Kitty_Sprite_Piercing_RingOverTop.png",
            "KittyX.piercings == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",
            "KittyX.legs", "images/KittySprite/Kitty_Sprite_Piercing_BallOverTop.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.Water and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Water2.png",
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),













        (0,0), ConditionSwitch(

            "not KittyX.top", Null(),
            "not KittyX.top_pulled_up", ConditionSwitch(

                    "KittyX.ArmPose != 1 and KittyX.top == 'pink_top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
                    "KittyX.ArmPose != 1 and KittyX.top == 'red_shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
                    "KittyX.ArmPose != 1 and KittyX.top == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "KittyX.ArmPose != 1 and KittyX.top == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket2.png",
                    "KittyX.top == 'pink_top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
                    "KittyX.top == 'red_shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
                    "KittyX.top == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
                    "KittyX.top == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket1.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "KittyX.ArmPose != 1 and KittyX.top == 'pink_top'", "images/KittySprite/Kitty_Sprite_Over_Pink2_Up.png",
                    "KittyX.ArmPose != 1 and KittyX.top == 'red_shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2_Up.png",
                    "KittyX.ArmPose != 1 and KittyX.top == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket2_Up.png",

                    "KittyX.top == 'pink_top'", "images/KittySprite/Kitty_Sprite_Over_Pink1_Up.png",
                    "KittyX.top == 'red_shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1_Up.png",

                    "KittyX.top == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket1_Up.png",
                    "True", Null(),
                    ),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.top or not KittyX.bra or not KittyX.top_pulled_up", Null(),
            "KittyX.bra == 'cami'", "images/KittySprite/Kitty_Sprite_Cami_Over.png",
            "KittyX.bra == 'lace_bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace_Over.png",
            "KittyX.bra == 'sports_bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport_Over.png",
            "KittyX.bra == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic_Over.png",
            "KittyX.bra == 'bikini_top'", "images/KittySprite/Kitty_Sprite_Bikini_Over.png",
            "True", Null(),
            ),

        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_Head",
            ),

        (0,0), ConditionSwitch(

            "KittyX.legs and not KittyX.upskirt", Null(),
            "KittyX.underwear and not KittyX.underwear_pulled_down", Null(),
            "'anal' in KittyX.spunk", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs and not KittyX.upskirt", Null(),
            "KittyX.underwear and not KittyX.underwear_pulled_down", Null(),
            "'in' in KittyX.spunk", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'belly' in KittyX.spunk", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' in KittyX.spunk", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != KittyX", Null(),
            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Kitty",
            "girl_offhand_action == 'fondle_breasts' and (offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",
            "girl_offhand_action == 'fondle_breasts' and (primary_action == 'fondle_breasts' or primary_action == 'suck breasts')", "GirlGropeRightBreast_Kitty",
            "girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Kitty",
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Kitty",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Kitty",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Kitty",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_offhand_action or second_girl_primary_action != 'masturbation' or focused_Girl == KittyX", Null(),

            "second_girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "second_girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Kitty",
            "second_girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Kitty",
            "second_girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not primary_action or focused_Girl != KittyX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Kitty",
            "primary_action == 'fondle_thighs'", "GropeThigh_Kitty",
            "primary_action == 'fondle_breasts'", "GropeLeftBreast_Kitty",
            "primary_action == 'suck breasts'", "LickRightBreast_Kitty",
            "primary_action == 'fondle_pussy' and action_speed == 2", "FingerPussy_Kitty",
            "primary_action == 'fondle_pussy'", "GropePussy_Kitty",
            "primary_action == 'eat_pussy'", "Lickpussy_Kitty",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Kitty",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "primary_action == 'vibrator anal'", "VibratorAnal_Kitty",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not offhand_action or focused_Girl != KittyX", Null(),
            "not offhand_action and not second_girl_primary_action and primary_action == 'fondle_breasts'", "GropeRightBreast_Kitty",

            "offhand_action == 'fondle_breasts' and primary_action == 'suck breasts'", "GropeLeftBreast_Kitty",

            "offhand_action == 'fondle_breasts'", "GropeRightBreast_Kitty",
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast_Kitty",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck breasts'", "LickLeftBreast_Kitty",
            "offhand_action == 'fondle_pussy'", "GropePussy_Kitty",
            "offhand_action == 'eat_pussy'", "Lickpussy_Kitty",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Kitty",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Kitty",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Kitty",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not second_girl_primary_action or focused_Girl != KittyX", Null(),
            "second_girl_primary_action == 'fondle_pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "second_girl_primary_action == 'fondle_pussy'", "GirlGropePussy_Kitty",
            "second_girl_primary_action == 'eat_pussy'", "Lickpussy_Kitty",
            "second_girl_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Kitty",
            "second_girl_primary_action == 'suck breasts'", "LickRightBreast_Kitty",
            "second_girl_primary_action == 'fondle_breasts' and (primary_action == 'fondle_breasts' or primary_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",
            "second_girl_primary_action == 'fondle_breasts' and (offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts')", "GirlGropeRightBreast_Kitty",
            "second_girl_primary_action == 'fondle_breasts' and (girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",
            "second_girl_primary_action == 'fondle_breasts'", "GirlGropeRightBreast_Kitty",
            "second_girl_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_primary_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action != 'lesbian' or not girl_offhand_action or focused_Girl == KittyX", Null(),
            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Kitty",
            "girl_offhand_action == 'eat_pussy'", "Lickpussy_Kitty",
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Kitty",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast_Kitty",
            "girl_offhand_action == 'fondle_breasts' and (primary_action == 'fondle_breasts' or primary_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",
            "girl_offhand_action == 'fondle_breasts' and (offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts')", "GirlGropeRightBreast_Kitty",
            "girl_offhand_action == 'fondle_breasts' and (girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",
            "girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Kitty",
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom 0.75
    pos (500,100)


image Kitty_Head:
    LiveComposite(
        (416,610),





        (0,0), ConditionSwitch(
            "KittyX.Water and KittyX.blushing == '_blush1'", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush1.png",
            "KittyX.Water and KittyX.blushing == '_blush2'", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush2.png",
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Head_Wet_Base.png",
            "KittyX.blushing == '_blush1'", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush1.png",
            "KittyX.blushing == '_blush2'", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush2.png",
            "True", "images/KittySprite/Kitty_Sprite_Head_Evo_Base.png",
            ),
        (0,0), ConditionSwitch(
            "KittyX.brows == 'normal'", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            "KittyX.brows == 'angry'", "images/KittySprite/Kitty_Sprite_Brows_Angry.png",
            "KittyX.brows == 'sad'", "images/KittySprite/Kitty_Sprite_Brows_Sad.png",
            "KittyX.brows == 'surprised'", "images/KittySprite/Kitty_Sprite_Brows_Surprised.png",
            "KittyX.brows == 'confused'", "images/KittySprite/Kitty_Sprite_Brows_Confused.png",
            "True", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "KittyX.mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            "KittyX.mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Mouth_Lipbite.png",
            "KittyX.mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Mouth_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Mouth_Sad.png",
            "KittyX.mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Mouth_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Mouth_Surprised.png",
            "KittyX.mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png",
            "KittyX.mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png",
            "True", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "'mouth' not in KittyX.spunk", Null(),
            "KittyX.mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Spunk_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Spunk_Sad.png",
            "KittyX.mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Spunk_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Spunk_Surprised.png",
            "KittyX.mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Spunk_Tongue.png",
            "KittyX.mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Spunk_Sucking.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "'facial' in KittyX.spunk", "images/KittySprite/Kitty_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), "Kitty Blink",
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "KittyX.hair == 'evo'", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            "KittyX.hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long.png",
            "KittyX.hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "True", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            ),
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "KittyX.hair == 'evo' and 'hair' in KittyX.spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "KittyX.hair == 'long' and 'hair' in KittyX.spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",

            "True", Null(),
            ),
        )

    zoom 0.5

image Kitty_hairback:
    LiveComposite(
        (416,610),
        (0,0), ConditionSwitch(
            "KittyX.Water or KittyX.hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
            "KittyX.hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
            "True", Null(),
            ),
        )

    zoom 0.5

image Kitty Blink:
    ConditionSwitch(
    "KittyX.eyes == 'sexy'", "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png",
    "KittyX.eyes == 'side'", "images/KittySprite/Kitty_Sprite_Eyes_Side.png",
    "KittyX.eyes == 'surprised'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",
    "KittyX.eyes == 'manic'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",
    "KittyX.eyes == 'normal'", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",
    "KittyX.eyes == 'down'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",
    "KittyX.eyes == 'stunned'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",
    "KittyX.eyes == 'squint'", "Kitty_Squint",
    "KittyX.eyes == 'leftside'", "images/KittySprite/Kitty_Sprite_Eyes_SideLeft.png",
    "KittyX.eyes == 'closed'", "images/KittySprite/Kitty_Sprite_Eyes_Closed.png",
    "True", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3

    "images/KittySprite/Kitty_Sprite_Eyes_Closed.png"
    0.25
    repeat

image Kitty_Squint:
    "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/KittySprite/Kitty_Sprite_Eyes_Squint.png"
    0.25
    repeat


image Kitty_Drip_Mask:

    contains:
        "images/KittySprite/Kitty_Sprite_WetMask.png"
        offset (-225,-560)

image Kitty_Drip_MaskP:

    contains:
        "images/KittySprite/Kitty_Sprite_WetMaskP.png"
        offset (-225,-560)




















image Kitty_SexSprite:
    LiveComposite(
        (1120,840),
        (0,0), ConditionSwitch(

                "not Player.sprite", "Kitty_Sex_Body_Static",
                "Player.cock_position == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Body_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Body_Anim2",
                        "action_speed ", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",
                        ),
                "Player.cock_position == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Body_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Body_Anim2",
                        "action_speed ", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",
                        ),
                "Player.cock_position == 'foot'", ConditionSwitch(

                        "action_speed >= 2", "Kitty_Sex_Body_FootAnim2",
                        "action_speed ", "Kitty_Sex_Body_FootAnim1",
                        "True", "Kitty_Sex_Body_FootAnimStatic",
                        ),
                "Player.cock_position == 'out' and action_speed >= 2","Kitty_Hotdog_Body_Anim2",
                "True", "Kitty_Sex_Body_Static",
                ),
        (0,0), ConditionSwitch(
                "not Player.sprite", "Kitty_Sex_Legs_Static",
                "Player.cock_position == 'anal'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "action_speed ", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",
                        ),
                "Player.cock_position == 'in'", ConditionSwitch(

                        "action_speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "action_speed ", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",
                        ),
                "Player.cock_position == 'foot'", ConditionSwitch(

                        "action_speed >= 2", "Kitty_Sex_Legs_FootAnim2",
                        "action_speed ", "Kitty_Sex_Legs_FootAnim1",
                        "True", "Kitty_Sex_Legs_FootAnimStatic",
                        ),
                "Player.cock_position == 'out' and action_speed >= 2","Kitty_Hotdog_Legs_Anim2",
                "True", "Kitty_Sex_Legs_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,230)
    zoom 0.7

image Kitty_Sex_Body_Static:
    contains:
        "Kitty_Sex_Body"
    pos (650,230)

image Kitty_Sex_Legs_Static:
    contains:
        "Kitty_Sex_Legs"
    pos (650,230)

image Kitty_Sex_Body = LiveComposite(

        (1120,840),
        (260,-350), "Kitty_hairback_Sex",

        (0,0), ConditionSwitch(

            "KittyX.piercings == 'barbell'", "images/KittySex/Kitty_Sex_Body_Barbell.png",
            "KittyX.piercings == 'ring'", "images/KittySex/Kitty_Sex_Body_Ring.png",
            "True", "images/KittySex/Kitty_Sex_Body.png",
            ),
        (260,-350), "Kitty_Head_Sex",

        (0,0), ConditionSwitch(

            "KittyX.neck == 'gold necklace'", "images/KittySex/Kitty_Sex_Neck_Gold.png",
            "KittyX.neck == 'star necklace'", "images/KittySex/Kitty_Sex_Neck_Star.png",
            "KittyX.neck == 'flower necklace'", "images/KittySex/Kitty_Sex_Neck_Flower.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Waist.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.bra", Null(),
            "not KittyX.top_pulled_up", ConditionSwitch(

                    "KittyX.bra == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress.png",
                    "KittyX.bra == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami.png",
                    "KittyX.bra == 'sports_bra'", "images/KittySex/Kitty_Sex_Under_SportsBra.png",
                    "KittyX.bra == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra.png",
                    "KittyX.bra == 'bikini_top'", "images/KittySex/Kitty_Sex_Under_Bikini.png",
                    "KittyX.bra == 'lace_bra'", "images/KittySex/Kitty_Sex_Under_LaceBra.png",
                    "True", Null(),
                    ),
            "KittyX.top", ConditionSwitch(

                    "KittyX.bra == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress_UpS.png",
                    "KittyX.bra == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_UpS.png",
                    "KittyX.bra == 'bikini_top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.bra == 'sports_bra' and KittyX.top == 'red_shirt'", "images/KittySex/Kitty_Sex_Under_SportsBra_UpS.png",
                    "KittyX.bra == 'sports_bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "KittyX.bra == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress_Up.png",
                    "KittyX.bra == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_Up.png",
                    "KittyX.bra == 'sports_bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "KittyX.bra == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
                    "KittyX.bra == 'bikini_top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.bra == 'lace_bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_Up.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.top", Null(),
            "not KittyX.top_pulled_up", ConditionSwitch(

                    "KittyX.top == 'jacket'", "images/KittySex/Kitty_Sex_Over_Jacket.png",
                    "KittyX.top == 'pink_top'", "images/KittySex/Kitty_Sex_Over_PinkShirt.png",
                    "KittyX.top == 'red_shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt.png",
                    "KittyX.top == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(

                    "KittyX.top == 'jacket'", "images/KittySex/Kitty_Sex_Over_Jacket_Up.png",
                    "KittyX.top == 'pink_top' and KittyX.bra == 'sports_bra'", "images/KittySex/Kitty_Sex_Over_PinkShirt_UpS.png",
                    "KittyX.top == 'pink_top'", "images/KittySex/Kitty_Sex_Over_PinkShirt_Up.png",
                    "KittyX.top == 'red_shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt_Up.png",

                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.bra or not KittyX.top or not KittyX.top_pulled_up", Null(),

            "KittyX.bra == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress_Up.png",
            "KittyX.bra == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
            "KittyX.bra == 'lace_bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_UpS.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "'belly' in KittyX.spunk", "images/KittySex/Kitty_Sex_Spunk_Body.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(

            "'tits' in KittyX.spunk", "images/KittySex/Kitty_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Kitty_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Kitty_Sex_Fondle_Breasts",
            "True", Null()
            ),
        )

image Kitty_Sex_Lick_Breasts:
    "licking"
    zoom 0.6
    offset (450,210)

image Kitty_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.1
    offset (320,-180)

image Kitty_Head_Sex:

    "Kitty_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10

image Kitty_hairback_Sex:

    "Kitty_hairback"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10


image Kitty_Sex_Legs:
    LiveComposite(

        (1120,840),
        (0,0), ConditionSwitch(
            "KittyX.legs == 'dress' and KittyX.upskirt", "images/KittySex/Kitty_Sex_Legs_Dress_Back_Up.png",
            "KittyX.legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Back.png",
            "KittyX.legs == 'blue_skirt'", "images/KittySex/Kitty_Sex_Skirt_Back.png",
            "True", Null(),
            ),
        (0,0), "images/KittySex/Kitty_Sex_Legs.png",
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Legs.png",
            "True", Null(),
            ),

        (0,0), "Kitty_Sex_Anus",

        (0,0), "Kitty_Sex_Pussy",

        (0,0), ConditionSwitch(
            "KittyX.underwear_pulled_down", Null(),
            "KittyX.underwear == 'green_panties' and KittyX.grool", "images/KittySex/Kitty_Sex_Panties_Green_Wet.png",
            "KittyX.underwear == 'green_panties'", "images/KittySex/Kitty_Sex_Panties_Green.png",
            "KittyX.underwear == 'lace_panties' and KittyX.grool", "images/KittySex/Kitty_Sex_Panties_Lace_Wet.png",
            "KittyX.underwear == 'lace_panties'", "images/KittySex/Kitty_Sex_Panties_Lace.png",
            "KittyX.underwear == 'bikini_bottoms' and KittyX.grool", "images/KittySex/Kitty_Sex_Panties_Bikini_Wet.png",
            "KittyX.underwear == 'bikini_bottoms'", "images/KittySex/Kitty_Sex_Panties_Bikini.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittySex/Kitty_Sex_Hose_StockingGarter_Legs.png",
            "KittyX.hose == 'garterbelt'", "images/KittySex/Kitty_Sex_Hose_Garter_Legs.png",
            "KittyX.hose == 'stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_Legs.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'pantyhose'", "images/KittySex/Kitty_Sex_Hose_Pantyhose_Legs.png",

            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            "KittyX.legs == 'dress' and KittyX.upskirt", "images/KittySex/Kitty_Sex_Legs_Dress_Up.png",
            "KittyX.legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress.png",
            "KittyX.legs == 'blue_skirt'", "images/KittySex/Kitty_Sex_Skirt.png",
            "KittyX.upskirt", Null(),
            "KittyX.legs == 'capris' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Pants_Blue_Wet.png",
            "KittyX.legs == 'capris'", "images/KittySex/Kitty_Sex_Pants_Blue.png",
            "KittyX.legs == 'black jeans' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Pants_Black_Wet.png",
            "KittyX.legs == 'black jeans'", "images/KittySex/Kitty_Sex_Pants_Black.png",
            "KittyX.legs == 'shorts' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Shorts_Wet.png",
            "KittyX.legs == 'shorts'", "images/KittySex/Kitty_Sex_Shorts.png",
            "KittyX.legs == 'yoga_pants' and KittyX.grool > 1", "images/KittySex/Kitty_Sex_Pants_Yoga_Wet.png",
            "KittyX.legs == 'yoga_pants'", "images/KittySex/Kitty_Sex_Pants_Yoga.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "KittyX.top == 'towel' and not KittyX.top_pulled_up", "images/KittySex/Kitty_Sex_Towel_Legs.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            "'belly' in KittyX.spunk", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "not Player.sprite or Player.cock_position != 'out'", Null(),
            "action_speed >= 2", "Kitty_Hotdog_Zero_Anim2",
            "action_speed ", "Kitty_Hotdog_Zero_Anim1",
            "True", "Kitty_Hotdog_Zero_Anim0",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position", Null(),
            "primary_action == 'eat_pussy'", "Kitty_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Kitty_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            "not Player.sprite or Player.cock_position != 'foot'", Null(),
            "action_speed >= 2", "Kitty_Footcock_Zero_Anim2",
            "action_speed ", "Kitty_Footcock_Zero_Anim1",
            "True", "Kitty_Footcock_Static",
            ),











        (0,0), ConditionSwitch(
            "not action_speed", "Kitty_Sex_Feet",
            "Player.cock_position == 'anal' or Player.cock_position == 'in' or Player.cock_position == 'out'", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
            "True", "Kitty_Sex_Feet",
            ),
        )

image Kitty_Sex_Feet = LiveComposite(

        (1120,840),
        (0,0), "images/KittySex/Kitty_Sex_Feet.png",
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Feet.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "KittyX.legs and not KittyX.upskirt and KittyX.legs != 'blue_skirt' and KittyX.legs != 'shorts'",ConditionSwitch(

                    "KittyX.hose == 'stockings_and_garterbelt'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.hose == 'stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.hose == 'knee stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
                    "KittyX.hose == 'pantyhose'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.hose == 'ripped_pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_FeetP.png",
                    "True", Null(),
                    ),



            "KittyX.hose == 'stockings' or KittyX.hose == 'stockings_and_garterbelt'", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png",
            "KittyX.hose == 'knee stockings'", "images/KittySex/Kitty_Sex_Hose_Kneesocks_Feet.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'pantyhose'", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png",

            "KittyX.hose == 'ripped_pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Feet.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            "KittyX.upskirt", Null(),
            "KittyX.legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Feet.png",
            "KittyX.legs == 'capris'", "images/KittySex/Kitty_Sex_Feet_Blue.png",
            "KittyX.legs == 'black jeans'", "images/KittySex/Kitty_Sex_Feet_Black.png",
            "KittyX.legs == 'yoga_pants'", "images/KittySex/Kitty_Sex_Feet_Yoga.png",
            "True", Null(),
            ),
        )

image Kitty_Sex_Lick_Pussy:
    "licking"
    zoom 0.7
    offset (530,510)

image Kitty_Sex_Lick_Ass:
    "licking"
    zoom 0.7
    offset (535,590)

image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom 0.7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image TestingSolid:

    contains:
        Solid("#75d7ec", xysize=(1500,1500))
        alpha 0.2


image Kitty_Pussy_Fucking0:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking1:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking2:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask")
image Kitty_Pussy_Fucking3:

    contains:

        "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                ),
    contains:

        AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask")

image Kitty_Pussy_Fucking_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Pussy_Mask.png"

image Kitty_Pussy_Open_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Pussy_Mask.png"
        yoffset 3















image Kitty_Pussy_Spunk_Heading:
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8

image Kitty_Sex_Pussy:

    contains:

        ConditionSwitch(
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_Pussy_Fucking.png",
                "Player.sprite and Player.cock_position == 'in' and action_speed", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "Player.sprite and Player.cock_position == 'in'", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                "primary_action == 'eat_pussy'", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                )
    contains:

        ConditionSwitch(
                "not KittyX.grool", Null(),
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:

        ConditionSwitch(
                "KittyX.piercings != 'ring'", Null(),
                "not Player.sprite or Player.cock_position != 'in' or action_speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_RingF.png",
                )
    contains:

        ConditionSwitch(
                "KittyX.piercings != 'barbell'", Null(),
                "not Player.sprite or Player.cock_position != 'in' or action_speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",
                )
    contains:

        ConditionSwitch(
                "not KittyX.pubes", Null(),
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                "Player.sprite and Player.cock_position == 'in' and action_speed", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "Player.sprite and Player.cock_position == 'in'", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                "primary_action == 'eat_pussy'", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "True", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                )
    contains:

        ConditionSwitch(
                "'in' in KittyX.spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
                "KittyX.hose == 'ripped_pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png",
                "True", Null(),
                ),
    contains:

        ConditionSwitch(
                "not Player.sprite", Null(),
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "Player.sprite and Player.cock_position == 'in' and action_speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "Player.sprite and Player.cock_position == 'in' and action_speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "Player.sprite and Player.cock_position == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),
                "True", Null(),
                )
    contains:

        ConditionSwitch(
                "'in' not in KittyX.spunk or not Player.sprite or Player.cock_position != 'in' or not action_speed", Null(),
                "action_speed <= 1", "Kitty_Pussy_Spunk_Heading",
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",
                )






image Kitty_Sex_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,530)
        zoom 1.4

image Kitty_Sex_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,525)
        zoom 1.4
        block:
            ease 1 pos (498,510)
            pause 1
            ease 3 pos (498,525)
            repeat

image Kitty_Sex_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,490)
        zoom 1.4
        block:
            ease 1 pos (500,380)
            pause 1
            ease 3 pos (500,490)
            repeat

image Kitty_Sex_Zero_Anim3:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,490)
        zoom 1.4
        block:
            ease 0.25 pos (500,380)
            pause 0.25
            ease 1.5 pos (500,490)
            repeat



image Kitty_Sex_Legs_Anim1:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause 0.25
            easein 1 pos (0,-5)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Kitty_Sex_Legs_Anim2:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause 0.5
            easein 0.5 pos (0,-15)
            ease 0.25 pos (0,-10)
            pause 1
            ease 2.75 pos (0,0)
            repeat

image Kitty_Sex_Legs_Anim3:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause 0.15
            easein 0.15 pos (0,-20)
            ease 0.10 pos (0,-15)
            pause 0.20
            ease 1.4 pos (0,0)
            repeat



image Kitty_Sex_Body_Anim1:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-5)
            pause 1.25
            ease 2.5 pos (0,0)
            repeat

image Kitty_Sex_Body_Anim2:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause 0.6
            easein 0.4 pos (0,-10)
            ease 0.25 pos (0,-5)
            pause 1
            ease 2.75 pos (0,10)
            repeat

image Kitty_Sex_Body_Anim3:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause 0.17
            easein 0.13 pos (0,-20)
            ease 0.10 pos (0,-15)
            pause 0.20
            ease 1.4 pos (0,10)
            repeat








image Kitty_Sex_Anus:
    contains:

        ConditionSwitch(
            "Player.sprite and Player.cock_position == 'anal' and action_speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.sprite and Player.cock_position == 'anal' and action_speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.sprite and Player.cock_position == 'anal' and action_speed", "Kitty_Sex_Anal_Heading",
            "Player.sprite and Player.cock_position == 'anal'", "Kitty_Sex_Anal_Tip",
            "KittyX.used_to_anal", "images/KittySex/Kitty_Sex_Hole_Loose.png",
            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png",
            )
    contains:

        ConditionSwitch(
                "'anal' not in KittyX.spunk", Null(),
                "Player.sprite and Player.cock_position != 'anal' and action_speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
                "Player.sprite and Player.cock_position != 'anal' and action_speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",
                )
    contains:

        ConditionSwitch(
            "not Player.sprite or Player.cock_position != 'anal'", Null(),
            "action_speed >= 3",  AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Sex_Anal_Fucking_Mask"),
            "action_speed >= 2", AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Sex_Anal_Fucking_Mask"),
            "action_speed ", AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Sex_Anal_Fucking_Mask"),
            "True", AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Sex_Anal_Fucking_Mask"),
            )
    contains:

        ConditionSwitch(
                "'anal' not in KittyX.spunk or not Player.sprite or Player.cock_position != 'anal' or not action_speed", Null(),
                "action_speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",
                )


image Kitty_Sex_Anal_Fucking0:

    contains:

        "Kitty_Sex_Anal_Tip"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking1:

    contains:

        "Kitty_Anal_Heading"
    contains:


        AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking2:

    contains:

        "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking3:

    contains:

        "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:

        AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Hole_Mask.png"

image Kitty_Sex_Anal_Open_Mask:

    contains:
        "images/KittySex/Kitty_Sex_Hole_Mask.png"
        yoffset 3

image Kitty_Sex_Anal_Heading:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:

        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_Sex_Anal_Spunk_Heading_Over:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:

        ease 0.75 xzoom 1.0
        pause 1.75
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.8
        repeat
image Kitty_Sex_Anal_Spunk_Heading_Under:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
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

image Kitty_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6




image Kitty_Anal_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,600)
        zoom 1.4

image Kitty_Anal_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,600)
        zoom 1.4
        block:
            ease 1 pos (500,570)
            pause 1
            ease 3 pos (500,600)
            repeat

image Kitty_Anal_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,570)
        zoom 1.4
        block:
            ease 1 pos (500,450)
            pause 1
            ease 3 pos (500,570)
            repeat

image Kitty_Anal_Zero_Anim3:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,570)
        zoom 1.4
        block:
            ease 0.25 pos (500,450)
            pause 0.25
            ease 1.5 pos (500,570)
            repeat



image Kitty_Hotdog_Zero_Anim0:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,570)
        zoom 1.4

image Kitty_Hotdog_Zero_Anim1:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (498,500)
        zoom 1.4
        block:
            ease 1 pos (498,560)
            pause 0.5
            ease 1.5 pos (498,500)
            repeat

image Kitty_Hotdog_Zero_Anim2:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (500,510)
        zoom 1.4
        block:
            ease 0.5 pos (500,400)
            pause 0.5
            ease 1 pos (500,510)
            repeat

image Kitty_Hotdog_Body_Anim2:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause 0.30
            ease 0.50 pos (0,-10)
            pause 0.20
            ease 1 pos (0,0)
            repeat

image Kitty_Hotdog_Legs_Anim2:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause 0.20
            ease 0.50 pos (0,-10)
            pause 0.20
            ease 1.1 pos (0,0)
            repeat





image Kitty_Footcock:
    contains:
        subpixel True
        "Zero_cock_blowjob"
        alpha 0.8
        zoom 0.7
        anchor (0.5,0.5)
        offset (465,70)
        pos (0,0)
    pos (750,230)

image Kitty_Footcock_Static:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
    pos (750,230)

image Kitty_Footcock_Zero_Anim1:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
        block:

            pause 0.5
            easein 0.75 ypos 360
            ease 0.25 ypos 355
            pause 1
            ease 2.50 ypos 270
            repeat
    pos (750,230)

image Kitty_Footcock_Zero_Anim2:
    contains:
        subpixel True
        "Kitty_Footcock"
        pos (392,295)
        block:

            pause 0.2
            easein 0.4 ypos 360
            ease 0.2 ypos 355
            pause 0.2
            ease 1.00 ypos 270
            repeat
    pos (750,230)

transform Kitty_Footcock_Zero_Anim1A():
    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset 60
        ease 0.25 yoffset 55
        pause 1
        ease 1.50 yoffset -30
        repeat

transform Kitty_Footcock_Zero_Anim2A():
    subpixel True
    offset (0,0)
    block:

        pause 0.2
        easein 0.4 yoffset 60
        ease 0.2 yoffset 55
        pause 0.2
        ease 1.00 yoffset -30
        pause 0.2
        easein 0.4 yoffset 60
        ease 0.2 yoffset 55
        pause 0.2
        ease 1.00 yoffset -30
        repeat

transform Kitty_Footcock_StaticA():
    subpixel True
    offset (0,-5)
    block:

        pause 0.5
        ease 1 yoffset 0
        pause 1
        ease 1.50 yoffset -5
        repeat

image Kitty_Sex_Legs_FootAnim1:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-65)
            ease 0.25 pos (0,-60)
            pause 1
            ease 2.50 pos (0,25)
            repeat
    pos (750,230)

image Kitty_Sex_Legs_FootAnim2:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
        block:

            pause 0.2
            easein 0.4 pos (0,-65)
            ease 0.2 pos (0,-60)
            pause 0.2
            ease 1.0 pos (0,25)
            repeat
    pos (750,230)

image Kitty_Sex_Legs_FootAnimStatic:

    contains:
        subpixel True
        "Kitty_Sex_Legs"
        pos (0,0)
    pos (750,230)

transform Kitty_Sex_Legs_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset -65
        ease 0.25 yoffset -60
        pause 1
        ease 1.50 yoffset 25
        repeat

transform Kitty_Sex_Legs_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause 0.2
        easein 0.4 yoffset -65
        ease 0.2 yoffset -60
        pause 0.2
        ease 1.0 yoffset 25
        pause 0.2
        easein 0.4 yoffset -65
        ease 0.2 yoffset -60
        pause 0.2
        ease 1.0 yoffset 25
        repeat

transform Kitty_Sex_Legs_FootAnimStaticA():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





image Kitty_Sex_Body_FootAnim1:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause 0.5
            easein 0.75 pos (0,-25)
            ease 0.25 pos (0,-15)
            pause 1
            ease 2.50 pos (0,15)
            repeat
    pos (750,230)

image Kitty_Sex_Body_FootAnim2:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
        block:

            pause 0.2
            easein 0.4 pos (0,-25)
            ease 0.2 pos (0,-15)
            pause 0.2
            ease 1.0 pos (0,15)
            repeat
    pos (750,230)

image Kitty_Sex_Body_FootAnimStatic:

    contains:
        subpixel True
        "Kitty_Sex_Body"
        pos (0,0)
    pos (750,230)

transform Kitty_Sex_Body_FootAnim1A():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        easein 0.75 yoffset -25
        ease 0.25 yoffset -15
        pause 1
        ease 1.50 yoffset 15
        repeat

transform Kitty_Sex_Body_FootAnim2A():

    subpixel True
    offset (0,0)
    block:

        pause 0.2
        easein 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        pause 0.2
        easein 0.4 yoffset -25
        ease 0.2 yoffset -15
        pause 0.2
        ease 1.0 yoffset 15
        repeat

transform Kitty_Sex_Body_FootAnimStaticA():

    subpixel True
    offset (0,0)
    block:

        pause 0.5
        ease 1 yoffset -5
        pause 1
        ease 1.50 yoffset 0
        repeat





label Kitty_Sex_Launch(Line=primary_action):
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

    if KittyX.pose == "doggy":
        call Kitty_Doggy_Launch (Line)
        return
    if renpy.showing("Kitty_SexSprite"):
        return
    $ action_speed = 0
    call Kitty_Hide (1)
    show Kitty_SexSprite zorder 150



    with dissolve
    return

label Kitty_Sex_Reset:
    if renpy.showing("Kitty_Doggy_Animation"):
        call Kitty_Doggy_Reset
        return
    if not renpy.showing("Kitty_SexSprite"):
        return
    $ KittyX.ArmPose = 2
    hide Kitty_SexSprite
    call Kitty_Hide

    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return












image Kitty_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Kitty_Doggy_Body",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "action_speed ", "Kitty_Doggy_Anal_Head_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "True", "Kitty_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite", "Kitty_Doggy_Ass",
            "Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "action_speed ", "Kitty_Doggy_Anal_Head_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "True", "Kitty_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.cock_position == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Kitty_Doggy_Feet2",
                    "action_speed ", "Kitty_Doggy_Feet1",
                    "True", "Kitty_Doggy_Feet0",
                    ),
            "not Player.sprite and ShowFeet", "Kitty_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)



image Kitty_Doggy_Body:
    LiveComposite(

        (420,750),

        (0,105), "Kitty_Doggy_Head",


        (0,0), "images/KittyDoggy/Kitty_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "not KittyX.bra", Null(),
            "KittyX.top_pulled_up", ConditionSwitch(
                    "KittyX.top and KittyX.top != 'towel' and KittyX.top != 'jacket'", Null(),
                    "KittyX.bra == 'dress' and KittyX.top and KittyX.top != 'towel'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_UpC.png",
                    "KittyX.bra == 'dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_Up.png",
                    "KittyX.bra == 'cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami_Up.png",
                    "KittyX.bra == 'lace_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
                    "KittyX.bra == 'sports_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports_Up.png",
                    "KittyX.bra == 'bikini_top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
                    ),
            "KittyX.bra == 'dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress.png",
            "KittyX.bra == 'cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami.png",
            "KittyX.bra == 'lace_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
            "KittyX.bra == 'sports_bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports.png",
            "KittyX.bra == 'bikini_top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Body_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.top", Null(),
            "KittyX.top == 'jacket'", "images/KittyDoggy/Kitty_Doggy_Over_Jacket.png",
            "KittyX.top == 'red_shirt'", "images/KittyDoggy/Kitty_Doggy_Over_Red.png",
            "KittyX.top == 'pink_top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink.png",
            "KittyX.top == 'towel' and not KittyX.top_pulled_up", "images/KittyDoggy/Kitty_Doggy_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Kitty_Doggy_GropeBreast",
            "True", Null()
            ),


        )


    offset (-30,0)



image Kitty_Doggy_Head:
    LiveComposite(

        (420,750),


        (0,0), ConditionSwitch(


            "KittyX.blushing", "images/KittyDoggy/Kitty_Doggy_Head_Blush.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.mouth == 'normal'", "images/KittyDoggy/Kitty_Doggy_Mouth_Normal.png",
            "KittyX.mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Mouth_Tongue.png",
            "KittyX.mouth == 'kiss'", "images/KittyDoggy/Kitty_Doggy_Mouth_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_Mouth_Sad.png",
            "KittyX.mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Mouth_Kiss.png",
            "KittyX.mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Mouth_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Mouth_Normal.png",
            ),





        (0,0), ConditionSwitch(

            "'mouth' not in KittyX.spunk", Null(),


            "KittyX.mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",


            "KittyX.mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(


            "KittyX.brows == 'angry'", "images/KittyDoggy/Kitty_Doggy_Brows_Angry.png",
            "KittyX.brows == 'sad'", "images/KittyDoggy/Kitty_Doggy_Brows_Sad.png",
            "KittyX.brows == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Brows_Surprised.png",

            "True", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            ),
        (0,0), "Kitty Doggy Blink",





        (0,0), ConditionSwitch(

            "'facial' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.Water or KittyX.hair == 'wet'", "images/KittyDoggy/Kitty_Doggy_Hair_Wet.png",
            "KittyX.hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Long.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Hair_Evo.png",
            ),
        (0,0), ConditionSwitch(

            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'hair' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 0.8
































image Kitty Doggy Blink:

    ConditionSwitch(
        "KittyX.eyes == 'sexy'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
        "KittyX.eyes == 'side'", "images/KittyDoggy/Kitty_Doggy_Eyes_Side.png",

        "KittyX.eyes == 'closed'", "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png",

        "KittyX.eyes == 'down'", "images/KittyDoggy/Kitty_Doggy_Eyes_Down.png",
        "KittyX.eyes == 'stunned'", "images/KittyDoggy/Kitty_Doggy_Eyes_Stunned.png",

        "KittyX.eyes == 'squint'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
        ),






    3

    "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png"
    0.25
    repeat

image Kitty_Doggy_Ass:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "not KittyX.upskirt", Null(),
            "KittyX.legs == 'dress'", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Back.png",
            "KittyX.legs == 'shorts' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_BackW.png",
            "KittyX.legs == 'shorts'", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Back.png",
            "KittyX.legs == 'yoga_pants'", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.underwear_pulled_down or (KittyX.legs and KittyX.legs != 'blue_skirt' and not KittyX.upskirt)", Null(),
            "KittyX.underwear == 'green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Green_BackW.png",
            "KittyX.underwear == 'green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Back.png",
            "KittyX.underwear == 'bikini_bottoms' and KittyX.grool","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_BackW.png",
            "KittyX.underwear == 'bikini_bottoms'","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Back.png",
            "KittyX.underwear == 'lace_panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Back.png",
            "True", Null(),
            ),
        (0,0), "images/KittyDoggy/Kitty_Doggy_Ass.png",
        (0,0), ConditionSwitch(

            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Ass_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.hose == 'stockings'", "images/KittyDoggy/Kitty_Doggy_Hose_Stockings.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "(KittyX.legs and KittyX.legs != 'blue_skirt') and not KittyX.upskirt", Null(),
            "KittyX.hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.underwear_pulled_down or (KittyX.legs and KittyX.legs != 'blue_skirt' and not KittyX.upskirt)", Null(),
            "KittyX.underwear == 'green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Green_DownW.png",
            "KittyX.underwear == 'green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Down.png",
            "KittyX.underwear == 'bikini_bottoms' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_DownW.png",
            "KittyX.underwear == 'bikini_bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Down.png",
            "KittyX.underwear == 'lace_panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "KittyX.hose and KittyX.hose != 'garterbelt'", Null(),
            "KittyX.legs == 'capris' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png",
            "KittyX.legs == 'black jeans' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png",
            "KittyX.legs == 'yoga_pants' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png",
            "KittyX.legs == 'shorts' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Pussy_Fucking3",
                    "action_speed > 1", "Kitty_Pussy_Fucking2",
                    "action_speed ", "Kitty_Pussy_Heading",
                    "True", "Kitty_Pussy_Static",
                    ),
            "primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pussy_Open.png",
            "KittyX.legs and not KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "KittyX.underwear and not KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Kitty_Pussy_Fingering",
            "primary_action == 'dildo_pussy'", "Kitty_Pussy_Fucking2",
            "True", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            ),

        (0,0), ConditionSwitch(

            "'in' in KittyX.spunk and Player.cock_position == 'in'",Null(),
            "'in' in KittyX.spunk ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "KittyX.grool and Player.cock_position == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "KittyX.grool", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.pubes", Null(),
            "Player.sprite and Player.cock_position == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "(KittyX.legs and KittyX.legs != 'blue_skirt') and not KittyX.upskirt", Null(),
            "KittyX.underwear_pulled_down and primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            "KittyX.underwear", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "KittyX.hose == 'pantyhose' and primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_OpenC.png",
            "KittyX.hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "primary_action == 'eat_pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "KittyX.piercings == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.piercings == 'ring' and KittyX.underwear and not KittyX.underwear_pulled_down", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.piercings == 'ring' and KittyX.hose == 'pantyhose' and not (KittyX.underwear and KittyX.underwear_pulled_down)", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.piercings == 'ring' and KittyX.legs and KittyX.legs != 'blue_skirt' and not KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.piercings == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "Player.sprite and Player.cock_position == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Anal_Fucking2",
                    "action_speed > 1", "Kitty_Anal_Fucking",
                    "action_speed ", "Kitty_Anal_Heading",
                    "True", "Kitty_Anal",
                    ),


            "KittyX.legs and not KittyX.upskirt", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "KittyX.underwear and not KittyX.underwear_pulled_down", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Kitty_Anal_Fingering",
            "primary_action == 'dildo_anal'", "Kitty_Anal_Fucking",
            "KittyX.used_to_anal", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),









        (0,0), ConditionSwitch(

            "KittyX.underwear_pulled_down or not KittyX.underwear", Null(),
            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),


            "KittyX.underwear == 'green_panties' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_GreenW.png",
            "KittyX.underwear == 'green_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            "KittyX.underwear == 'lace_panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Lace.png",
            "KittyX.underwear == 'bikini_bottoms' and KittyX.grool", "images/KittyDoggy/Kitty_Doggy_Panties_BikiniW.png",
            "KittyX.underwear == 'bikini_bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            ),
        (0,0), ConditionSwitch(

            "Player.sprite and (Player.cock_position == 'in' or Player.cock_position == 'anal')", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "(KittyX.legs or KittyX.legs == 'blue_skirt') or not KittyX.upskirt", Null(),
            "KittyX.hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == 'dress'", ConditionSwitch(
                    "KittyX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Dress.png",
                    ),
            "KittyX.legs == 'blue_skirt'", ConditionSwitch(
                    "KittyX.upskirt and Player.sprite and Player.cock_position == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",
                    "KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt.png",
                    ),

            "KittyX.upskirt", Null(),
            "KittyX.legs == 'capris'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlueW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Blue.png",
                    ),
            "KittyX.legs == 'black jeans'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlackW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Black.png",
                    ),
            "KittyX.legs == 'yoga_pants'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_YogaW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga.png",
                    ),
            "KittyX.legs == 'shorts'", ConditionSwitch(

                    "KittyX.grool > 1", "images/KittyDoggy/Kitty_Doggy_Legs_ShortsW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts.png",
                    ),





            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == 'blue_skirt' and KittyX.upskirt", Null(),
            "KittyX.legs == 'dress' and KittyX.upskirt", Null(),
            "KittyX.top == 'pink_top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink_Tail.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.legs == 'dress' and KittyX.upskirt", Null(),
            "KittyX.top == 'towel' and KittyX.top_pulled_up", Null(),
            "KittyX.top == 'towel' and KittyX.upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Towel_Up.png",
            "KittyX.top == 'towel'", "images/KittyDoggy/Kitty_Doggy_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in KittyX.spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Ass.png",
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

            "True", "images/KittyDoggy/Kitty_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.sprite or Player.cock_position != 'out'", Null(),


            "action_speed ", AlphaMask("Zero_hotdog_moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_hotdog_static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Kitty_Doggy_Feet:
    contains:
        AlphaMask("Kitty_Doggy_Shins", "images/KittyDoggy/Kitty_Doggy_Feet_Mask.png")

image Kitty_Doggy_Shins:



    contains:

        ConditionSwitch(
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hole.png",
            "KittyX.hose and KittyX.hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet_Legs.png"
            )
    contains:

        ConditionSwitch(
            "KittyX.legs == 'capris'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Blue.png",
            "KittyX.legs == 'black jeans'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Black.png",
            "KittyX.legs == 'yoga_pants'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Yoga.png",
            "True", Null(),
            )
    contains:



        ConditionSwitch(
            "not Player.sprite or Player.cock_position == 'foot'", ConditionSwitch(
                    "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_HoleF.png",
                    "KittyX.hose and KittyX.hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_HoseF.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_FeetF.png"
                    ),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_Hole.png",
            "KittyX.hose and KittyX.hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet.png"
            )












image Kitty_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom 0.55
        offset (110,420)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat

















image Zero_Kitty_Hotdog_Static:


    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)

image Zero_Kitty_Hotdog_Moving:


    contains:
        "Zero_cock_doggy_out"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat






















image Zero_Kitty_Doggy_Static:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (169,545)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 545
            repeat

image Zero_Kitty_Doggy_Heading:

    contains:
        subpixel True
        "Zero_cock_doggy_in"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500
            pause 1
            ease 3 xpos 171 ypos 545
            repeat

image Zero_Kitty_Doggy_Fucking2:

    contains:
        "Zero_cock_doggy_in"
        pos (169,500)
        block:
            ease 0.5 ypos 440
            pause 0.25
            ease 1.75 ypos 500
            repeat

image Zero_Kitty_Doggy_Fucking3:

    contains:
        "Zero_cock_doggy_in"
        pos (169,500)
        block:
            ease 0.2 ypos 440
            pause 0.1
            ease 0.6 ypos 500
            repeat

image Kitty_Pussy_Mask:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Kitty_Pussy_Mask_Static:


    contains:

        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat


































image Kitty_Pussy_Static:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Static", "Kitty_Pussy_Mask_Static")
    contains:


        AlphaMask("Kitty_PussyHole_Static", "Kitty_Pussy_Hole_Mask_Static")

image Kitty_Pussy_Hole_Mask_Static:

    contains:

        AlphaMask("images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.65
            pause 1
            ease 3 xzoom 0.6
            repeat

image Kitty_PussyHole_Static:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha 0.9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Heading:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Heading", "Kitty_Pussy_Mask")
    contains:


        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")


image Kitty_Pussy_Hole_Mask:

    contains:

        AlphaMask("images/JeanDoggy/Jean_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom 0.6
            repeat

image Kitty_Pussy_Heading_Flap:

    contains:

        "images/JeanDoggy/Jean_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha 0.9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat


image Kitty_Pussy_Fingering:

    subpixel True
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom 0.6
        block:
            ease 1 xzoom 0.9
            pause 1
            ease 3 xzoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")
    contains:



        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")



image Kitty_Pussy_Fucking2:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Kitty_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),



image Kitty_Pussy_Fucking3:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")





image Kitty_Anal:

    contains:

        "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        "Zero_cock_doggy_in"
        pos (172,500)

image Kitty_Anal_Fingering:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.6
        block:
            ease 0.5 zoom 0.75
            pause 0.5
            ease 1.5 zoom 0.6
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")


image Kitty_Anal_Heading:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            ease 0.5 zoom 1
            pause 0.5
            ease 1.5 zoom 0.5
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Zero_Kitty_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Kitty_Doggy_Anal_Heading_Mask")

image Zero_Kitty_Doggy_Anal_Heading:

    contains:
        "Zero_cock_doggy_in"
        pos (172,500)
        block:
            ease 0.5 ypos 450
            pause 0.25
            ease 1.75 ypos 500
            repeat

image Zero_Kitty_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease 0.5 ypos 550
            pause 0.25
            ease 1.75 ypos 600
            repeat

image Kitty_Doggy_Anal_Heading_Mask:

    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            ease 0.5 zoom 1
            pause 0.5
            ease 1.5 zoom 0.5
            repeat

image Kitty_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause 0.4
            ease 0.3 ypos -5
            easeout 1 ypos 0
            pause 0.8
            repeat

image Kitty_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause 0.4
            ease 0.2 ypos -10
            easeout 0.1 ypos -7
            easein 0.9 ypos 0
            pause 0.9
            repeat


image Zero_Kitty_Doggy_Anal1:

    contains:
        "Zero_cock_doggy_in"
        pos (172,460)
        block:
            ease 0.5 ypos 395
            pause 0.25
            ease 1.75 ypos 460
            repeat

image Kitty_Anal_Fucking:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            pause 0.25
            ease 0.25 zoom 1
            pause 0.75
            ease 1 zoom 0.95
            pause 0.25
            repeat
    contains:
        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Kitty_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),


image Kitty_Doggy_Anal_FullMask:
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
    contains:



        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )

image Kitty_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        pause 0.4
        block:
            ease 0.2 ypos -10
            pause 0.3
            ease 2 ypos 0
            repeat

image Kitty_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause 0.4
            ease 0.2 ypos -15
            ease 0.1 ypos -5
            pause 0.2
            ease 1.6 ypos 0
            repeat



image Zero_Kitty_Doggy_Anal2:

    contains:
        "Zero_cock_doggy_in"
        pos (172,460)
        block:
            ease 0.2 ypos 395
            pause 0.1
            ease 0.6 ypos 465
            repeat

image Kitty_Anal_Fucking2:

    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:

        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom 0.5
        block:
            pause 0.1
            ease 0.1 zoom 1
            pause 0.3
            ease 0.3 zoom 0.95
            pause 0.1
            repeat
    contains:






        ConditionSwitch(

            "KittyX.hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.hose == 'stockings_and_garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.underwear and KittyX.underwear_pulled_down", Null(),
            "KittyX.hose == 'ripped_pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Kitty_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Kitty_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause 0.15
            ease 0.1 ypos -20
            pause 0.1
            easein 0.5 ypos 0
            pause 0.05
            repeat

image Kitty_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 5
        block:
            pause 0.15
            ease 0.1 ypos -25
            ease 0.1 ypos -15
            pause 0.1
            ease 0.4 ypos 5
            pause 0.05
            repeat




image Kitty_Doggy_Feet0:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            subpixel True
            pause 0.5
            ease 2 ypos 0
            pause 0.5
            ease 2 ypos -20
            repeat
    contains:
        ConditionSwitch(
                "Player.sprite", "Zero_cock_doggy_out",
                "True", Null(),
                )
        zoom 1.2
        pos (158,520)
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            subpixel True
            pause 0.5
            ease 2 ypos 0
            pause 0.5
            ease 2 ypos -20
            repeat

image Kitty_Doggy_Feet1:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            pause 0.3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat
    contains:
        "Zero_cock_doggy_out"
        zoom 1.2
        pos (158,520)
        block:
            pause 0.4
            ease 1.7 ypos 540
            ease 0.9 ypos 520
            repeat
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            pause 0.3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat

image Kitty_Doggy_Feet2:

    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20)
        block:
            pause 0.05
            ease 0.6 ypos 110
            ease 0.3 ypos -20
            repeat
    contains:
        "Zero_cock_doggy_out"
        zoom 1.2
        pos (158,520)
        block:
            pause 0.07
            ease 0.6 ypos 540
            ease 0.28 ypos 520
            repeat
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20)
        block:
            pause 0.05
            ease 0.6 ypos 110
            ease 0.3 ypos -20
            repeat




label Kitty_Doggy_Launch(Line=primary_action):
    if renpy.showing("Kitty_Doggy_Animation"):
        return
    $ action_speed = 0
    call Kitty_Hide (1)
    show Kitty_Doggy_Animation zorder 150 at sprite_location(stage_center+50)
    with dissolve
    return

label Kitty_Doggy_Reset:
    if not renpy.showing("Kitty_Doggy_Animation"):
        return

    $ KittyX.ArmPose = 2
    $ KittyX.spriteVer = 0
    hide Kitty_Doggy_Animation
    call Kitty_Hide
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return













image Kitty_BJ_Animation:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Kitty_BJ_Backdrop", blowjob_starting()),
            "action_speed == 1", At("Kitty_BJ_Backdrop", blowjob_licking_body()),
            "action_speed == 2", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_2()),
            "action_speed == 3", At("Kitty_BJ_Backdrop", blowjob_sucking_body()),
            "action_speed == 4", At("Kitty_BJ_Backdrop", blowjob_deepthroat_body()),
            "action_speed == 5", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_5()),
            "action_speed == 6", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Kitty_BJ_Head", blowjob_starting()),
            "action_speed == 1", At("Kitty_BJ_Head", blowjob_licking()),
            "action_speed == 2", At("Kitty_BJ_Head", blowjob_heading()),
            "action_speed == 3", At("Kitty_BJ_Head", blowjob_sucking()),
            "action_speed == 4", At("Kitty_BJ_Head", blowjob_deepthroat()),
            "action_speed == 5", At("Kitty_BJ_Head", Kitty_BJ_Head_5()),
            "action_speed == 6", At("Kitty_BJ_Head", Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Zero_cock_blowjob", blowjob_starting_cock()),
            "action_speed == 1", At("Zero_cock_blowjob", blowjob_licking_cock()),
            "action_speed >= 2", At("Zero_cock_blowjob", blowjob_straight_cock()),



            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), blowjob_sucking()),
            "action_speed == 4", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), blowjob_deepthroat()),
            "action_speed == 6", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 2", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), blowjob_heading()),
            "action_speed == 5", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_5()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed < 3 or 'mouth' not in KittyX.spunk", Null(),
            "action_speed == 3", At("KittySuckingSpunk", blowjob_sucking()),
            "action_speed == 4", At("KittySuckingSpunk", blowjob_deepthroat()),
            "action_speed == 6", At("KittySuckingSpunk", Kitty_BJ_Head_6()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed == 2 and 'mouth' in KittyX.spunk", At("Kitty_BJ_MaskHeadingSpunk", blowjob_heading()),
            "action_speed == 5 and 'mouth' in KittyX.spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_5()),
            "True", Null(),
            ),
        )
    zoom 0.55
    anchor (.5,.5)

image Kitty_BJ_hairback:

    ConditionSwitch(
            "KittyX.Water and KittyX.hair == 'evo'", "images/KittyBJFace/Kitty_BJ_hairbackWet.png",
            "KittyX.hair == 'long'", "images/KittyBJFace/Kitty_BJ_hairbackWet.png",
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    yoffset 50







image Kitty_BJ_Backdrop:

    LiveComposite(
        (858,928),
        (-375,250), ConditionSwitch(

            "'blanket' in KittyX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.top == 'red_shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
            "True", Null(),
            ),
        (0,0),"images/KittyBJFace/Kitty_BJ_Body.png",

        (0,0), ConditionSwitch(

            "KittyX.neck == 'gold necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Gold.png",
            "KittyX.neck == 'star necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Star.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.piercings", Null(),
            "KittyX.piercings == 'ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",
            ),
        (0,0), ConditionSwitch(

            "not KittyX.Water", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Wet_Body.png",
            ),

        (0,0), ConditionSwitch(

            "not KittyX.bra", Null(),
            "KittyX.bra == 'lace_bra'", "images/KittyBJFace/Kitty_BJ_Bra_Lace.png",
            "KittyX.bra == 'sports_bra'", "images/KittyBJFace/Kitty_BJ_Bra_Sport.png",
            "KittyX.bra == 'bra'", "images/KittyBJFace/Kitty_BJ_Bra.png",
            "KittyX.bra == 'cami'", "images/KittyBJFace/Kitty_BJ_Bra_Cami.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "not KittyX.top", Null(),
            "KittyX.top == 'pink_top'", "images/KittyBJFace/Kitty_BJ_Over_PinkShirt.png",
            "KittyX.top == 'red_shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedShirt.png",
            "KittyX.top == 'towel'", "images/KittyBJFace/Kitty_BJ_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' not in KittyX.spunk", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_Body.png",
            ),
        )
    zoom 1.5
    offset (-300,-200)

image Kitty_BJ_Head:
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(

            "KittyX.Water or KittyX.hair == 'wet'", "images/KittyBJFace/Kitty_BJ_hairbackWet.png",
            "True", Null(),
            ),
















        (0,0), ConditionSwitch(

            "action_speed <= 2 or action_speed == 5 or not renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(

                    "KittyX.Water", ConditionSwitch(

                            "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",
                            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png",
                            ),
                    "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
                    ),

            "KittyX.Water", ConditionSwitch(

                    "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png",
                    ),
            "KittyX.blushing", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",
            "True",  "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
            ),
        (0,0), ConditionSwitch(

            "action_speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    "action_speed == 6", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    "True", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Mouth_Lipbite.png",
            "KittyX.mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
            "KittyX.mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Mouth_Sad.png",
            "KittyX.mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.mouth == 'grimace'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Mouth_Surprised.png",
            "KittyX.mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
            "True", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(


            "not renpy.showing('Kitty_BJ_Animation')", Null(),
            "action_speed == 2", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnim()),
            "action_speed == 5", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnimC()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'mouth' not in KittyX.spunk", Null(),
            "action_speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
                    ),
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "KittyX.mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "KittyX.mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "KittyX.mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.brows == 'normal'", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            "KittyX.brows == 'angry'", "images/KittyBJFace/Kitty_BJ_Brows_Angry.png",
            "KittyX.brows == 'sad'", "images/KittyBJFace/Kitty_BJ_Brows_Sad.png",
            "KittyX.brows == 'surprised'", "images/KittyBJFace/Kitty_BJ_Brows_Surprised.png",
            "KittyX.brows == 'confused'", "images/KittyBJFace/Kitty_BJ_Brows_Confused.png",
            "True", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            ),
        (0,0), "Kitty BJ Blink",

        (0,0), ConditionSwitch(

            "'facial' in KittyX.spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "KittyX.Water or KittyX.hair == 'wet'", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png",
            "KittyX.hair == 'long'", "images/KittyBJFace/Kitty_BJ_Hair_Long.png",
            "KittyX.hair == 'evo'", "images/KittyBJFace/Kitty_BJ_Hair_Evo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not KittyX.Water", Null(),
            "action_speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),
        (0,0), ConditionSwitch(

            "'hair' in KittyX.spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Kitty BJ Blink:

    ConditionSwitch(
            "KittyX.eyes == 'normal'", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",
            "KittyX.eyes == 'sexy'", "images/KittyBJFace/Kitty_BJ_Eyes_Sexy.png",
            "KittyX.eyes == 'closed'", "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png",
            "KittyX.eyes == 'surprised'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.eyes == 'side'", "images/KittyBJFace/Kitty_BJ_Eyes_Side.png",
            "KittyX.eyes == 'stunned'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.eyes == 'down'", "images/KittyBJFace/Kitty_BJ_Eyes_Down.png",
            "KittyX.eyes == 'manic'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.eyes == 'squint'", "images/KittyBJFace/Kitty_BJ_Eyes_Squint.png",
            "True", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png"
    0.25
    repeat

image Kitty_BJ_MouthHeading:

    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)

image Kitty_BJ_MouthSuckingMask:

    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        zoom 1.4
    contains:
        ConditionSwitch(
            "'mouth' not in KittyX.spunk", Null(),
            "action_speed != 2 and action_speed != 5", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            )
        zoom 1.4

image Kitty_BJ_MaskHeading:

    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Kitty_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", At("Kitty_BJ_MaskHeading", Kitty_BJ_MouthAnim()),
            "action_speed == 5", At("Kitty_BJ_MaskHeading", Kitty_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Kitty_BJ_MaskHeadingSpunk:

    At("KittySuckingSpunk", Kitty_BJ_MouthAnim())
    zoom 1.8

image KittySuckingSpunk:
    contains:
        "images/KittyBJFace/Kitty_BJ_Spunk_SuckingO.png"
        zoom 1.4
        anchor (0.5, 0.5)

transform Kitty_BJ_MouthAnim():

    subpixel True
    zoom 0.7
    block:
        pause 0.40
        easeout 0.40 zoom 0.69
        linear 0.10 zoom 0.7
        easein 0.45 zoom 0.65
        pause 0.15

        easeout 0.25 zoom 0.7
        linear 0.10 zoom 0.69
        easein 0.30 zoom 0.7
        pause 0.35

        repeat
transform Kitty_BJ_MouthAnimC():

    subpixel True
    zoom 0.7
    block:
        pause 0.20
        ease 0.50 zoom 0.65
        pause 0.60
        ease 0.30 zoom 0.7
        pause 0.10
        ease 0.30 zoom 0.65
        pause 0.20
        ease 0.30 zoom 0.7
        repeat

image Blanket:
    contains:
        "images/KittyBJFace/Kitty_BJFace_Blanket.png"
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image Blanket = LiveComposite(
    (858,928),
    (0, 0), "images/KittyBJFace/Kitty_BJFace_Blanket.png"
    )




transform Kitty_BJ_Body_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat



transform Kitty_BJ_Head_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat
transform Kitty_BJ_Body_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat

transform Kitty_BJ_Head_6():

    ease 0.5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause 0.5
        ease 2 yoffset 230
        repeat
transform Kitty_BJ_Body_6():

    ease 0.5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause 0.5
        ease 1.8 yoffset 190
        repeat






label Kitty_BJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_BJ_Animation"):
        return

    call Kitty_Hide
    if Line == "L" or Line == "cum":
        show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    if Line == "L":
        if Taboo:
            if len(Present) >= 2:
                if Present[0] != KittyX:
                    "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != KittyX:
                    "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[KittyX.name] casually glances around to see if anyone can see her."
        if not KittyX.action_counter["blowjob"]:
            "[KittyX.name] hesitantly kneels down and touches her mouth to your cock."
        else:
            "[KittyX.name] kneels down and begins to suck on your cock."

    $ action_speed = 0

    if Line != "cum":
        $ primary_action = "blowjob"

    show Kitty_Sprite zorder KittyX.sprite_layer:
        alpha 0
    show Kitty_BJ_Animation zorder 150:
        pos (645,510)
    return

label Kitty_BJ_Reset:
    if not renpy.showing("Kitty_BJ_Animation"):
        return
    call Kitty_Hide
    $ action_speed = 0

    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Kitty_Sprite zorder KittyX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause 0.5
        ease 0.5 zoom 1 offset (0,0)
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)

    return









image Kitty_TJ_Animation:

    contains:
        ConditionSwitch(

            "Player.sprite", ConditionSwitch(

                    "action_speed == 1", "Kitty_TJ_Body_1",
                    "action_speed == 2", "Kitty_TJ_Body_2",
                    "action_speed == 3", "Kitty_TJ_Body_3",
                    "action_speed >= 5", "Kitty_TJ_Body_5",
                    "True",       "Kitty_TJ_Body_0",
                    ),
            "True","Kitty_TJ_Body_0",
            ),
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)


image Kitty_TJ_Torso:

    contains:

        "images/KittyBJFace/Kitty_TJ_Body.png"












































image Kitty_TJ_Arms:

    contains:

        "images/KittyBJFace/Kitty_TJ_Arms.png"

image Kitty_TJ_Tits:

    contains:


        ConditionSwitch(
            "Player.sprite and action_speed", "images/KittyBJFace/Kitty_TJ_Tits_Smooshed.png",
            "True", "images/KittyBJFace/Kitty_TJ_Tits.png",
            )






















































image Kitty_Mega_Mask:

    contains:
        Solid("#159457", xysize=(1750,1750))
        alpha 0.5





image Kitty_TJ_Body_0:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.4 ypos 325
            ease 1.6 ypos 330
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", "Zero_cock_blowjob",
                    "True", Null(),
                    )
        subpixel True
        pos (640,150)
        anchor (0.5,0.5)
        zoom 0.4



image Kitty_TJ_Mask_1:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,60)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.9 ypos -40
            ease 1 ypos 60
            pause 0.1
            repeat

image Kitty_TJ_Body_1:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 3 ypos 210
            ease 1 ypos 260
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.8 ypos 280
            ease 1 ypos 330
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.85 ypos 280
            ease 1 ypos 330
            pause 0.15
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.9 ypos 210
            ease 1 ypos 260
            pause 0.1
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.9 ypos 280
            ease 1 ypos 330
            pause 0.1
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_1"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            ease 2.8 ypos 490
            ease 0.8 ypos 500
            pause 0.4
            repeat



image Kitty_TJ_Mask_2:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,60)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 0.71 ypos -15
            ease 0.27 ypos 60
            pause 0.02
            repeat

image Kitty_TJ_Body_2:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 0.7 ypos 215
            ease 0.25 ypos 260
            pause 0.05
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 0.65 ypos 285
            ease 0.25 ypos 330
            pause 0.1
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 0.68 ypos 285
            ease 0.25 ypos 330
            pause 0.07
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,330)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 0.71 ypos 290
            ease 0.27 ypos 330
            pause 0.02
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 0.68 ypos 215
            ease 0.25 ypos 260
            pause 0.07
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_2"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            ease 0.72 ypos 490
            ease 0.27 ypos 500
            pause 0.01
            repeat



image Kitty_TJ_Mask_3:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,140)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.2 ypos 90
            ease 0.6 ypos 140
            pause 0.2
            repeat

image Kitty_TJ_Body_3:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,260)
        rotate 0
        subpixel True
        parallel:
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (520,320)
                ease 2.2 pos (510,290)
                ease 0.8 pos (520,320)
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (475,320)
                ease 2.2 pos (490,290)
                ease 0.8 pos (475,320)
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease 0.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease 0.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 340
            ease 0.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,310)
        subpixel True
        rotate 0
        parallel:
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (520,320)
                ease 2.2 pos (510,290)
                ease 0.8 pos (520,320)
            block:

                ease 2 pos (500,290)
                ease 0.6 pos (500,315)
                pause 0.4
                repeat 2
            block:

                ease 2.2 pos (500,290)
                ease 0.8 pos (475,320)
                ease 2.2 pos (490,290)
                ease 0.8 pos (475,320)
            repeat
        parallel:
            block:

                ease 2.2 rotate 0
                pause 3.8
            block:

                ease 2.2 rotate 0
                ease 0.8 rotate 10
                ease 2.2 rotate 0
                ease 0.8 rotate 5
            block:

                ease 2.2 rotate 0
                pause 3.8
            block:

                ease 2.2 rotate 0
                ease 0.8 rotate -10
                ease 2.2 rotate 0
                ease 0.8 rotate -5
            repeat
    contains:

        ConditionSwitch(
                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_3"),
                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4



image Kitty_TJ_Mask_5:
    contains:
        "images/KittyBJFace/Kitty_TJ_Mask.png"
        pos (100,140)
        anchor (0.5, 0.5)
        zoom 1.4
        subpixel True
        block:
            ease 2.2 ypos 120
            ease 1.6 ypos 140
            pause 0.2
            repeat

image Kitty_TJ_Body_5:

    contains:

        "Kitty_BJ_hairback"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,260)
        rotate 0
        subpixel True
        block:

            ease 2 pos (500,304)
            ease 1.6 pos (500,307)
            pause 0.4
            repeat
    contains:

        "Kitty_TJ_Torso"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_TJ_Arms"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause 0.2
            repeat
    contains:

        "Kitty_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,307)
        subpixel True
        rotate 0
        block:

            ease 2 pos (500,304)
            ease 1.6 pos (500,307)
            pause 0.4
            repeat
    contains:

        "Kitty_TJ_Tits"
        pos (545,360)
        anchor (0.5, 0.5)
        zoom 0.55
        subpixel True
        block:
            ease 2.2 ypos 350
            ease 1.6 ypos 360
            pause 0.2
            repeat
    contains:













        ConditionSwitch(

                    "Player.sprite", AlphaMask("Zero_cock_blowjob", "Kitty_TJ_Mask_5"),

                    "True", Null(),
                    )
        subpixel True
        pos (665,500)
        anchor (0.5,0.5)
        zoom 0.4





























label Kitty_TJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_TJ_Animation"):
        return
    call Kitty_Hide
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        ease 1 zoom 2 xpos 700 yoffset 50
    if Line == "L" and Taboo:
        if len(Present) >= 2:
            if Present[0] != KittyX:
                "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != KittyX:
                "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[KittyX.name] casually glances around to see if anyone can see her."
    if KittyX.bra and KittyX.top:
        "She throws off her [KittyX.top] and her [KittyX.bra]."
    elif KittyX.top:
        "She throws off her [KittyX.top], baring her breasts underneath."
    elif KittyX.bra:
        "She tugs off her [KittyX.bra] and throws it aside."
    $ KittyX.top = ""
    $ KittyX.bra = ""
    $ KittyX.ArmPose = 0
    call Kitty_First_Topless
    if Line == "L":
        if not KittyX.action_counter["titjob"]:
            "She hesitantly presses your cock against her chest."
        else:
            "She squeezes her breasts around your cock."


    show blackscreen onlayer black with dissolve
    show Kitty_Sprite zorder KittyX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Kitty_TJ_Animation zorder 150
    $ Player.sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Kitty_TJ_Reset:
    if not renpy.showing("Kitty_TJ_Animation"):
        return
    call Kitty_Hide
    $ Player.sprite = 0

    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        zoom 2 xpos 550 yoffset 50
    show Kitty_Sprite zorder KittyX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause 0.5
        ease 0.5 zoom 1 xpos KittyX.sprite_location yoffset 0
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos KittyX.sprite_location

    return






















image Kitty_Hand_Under:
    "images/KittySprite/handkitty2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Kitty_Hand_Over:
    "images/KittySprite/handkitty1.png"
    anchor (0.5,0.5)
    pos (0,0)


















transform Kitty_Hand_1():
    subpixel True
    ease 0.5 ypos 150 rotate 5
    pause 0.25
    ease 1.0 ypos -100 rotate -5
    pause 0.1
    repeat

transform Kitty_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat

image Kitty_HJ_Animation:
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Kitty_Hand_Under"),
            "action_speed == 1", At("Kitty_Hand_Under", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_Hand_Under", Kitty_Hand_2()),
            "action_speed ", Null(),
            ),
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Kitty_Hand_Over"),
            "action_speed == 1", At("Kitty_Hand_Over", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_Hand_Over", Kitty_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Kitty_HJ_Launch(Line=primary_action):
    if renpy.showing("Kitty_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call Kitty_Hide
    if Line == "L":
        show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
    else:
        show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (-50,200)
        with dissolve

    if Line == "L":
        if Taboo:
            if len(Present) >= 2:
                if Present[0] != KittyX:
                    "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != KittyX:
                    "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[KittyX.name] casually glances around to see if anyone can see her."

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause 0.5
    show Kitty_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:

        offset (100,250)
    return

label Kitty_HJ_Reset:
    if not renpy.showing("Kitty_HJ_Animation"):
        return
    $ action_speed = 0
    hide Kitty_HJ_Animation with easeoutbottom
    call Kitty_Hide
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1.7 offset (-50,200)
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause 0.5
        ease 0.5 zoom 1 offset (0,0)
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return


label Kitty_Kissing_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "kiss" if Set else KittyX.pose
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location)
    show Kitty_Sprite at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Kitty_Kissing_Smooch:
    $ KittyX.change_face("_kiss")
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos KittyX.sprite_location zoom 1
    $ KittyX.change_face("_sexy")
    return

label Kitty_Breasts_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "breasts" if Set else KittyX.pose
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Kitty_Middle_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "mid" if Set else KittyX.pose
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Kitty_Pussy_Launch(T=primary_action, Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.pose = "pussy" if Set else KittyX.pose
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Kitty_Pos_Reset(T=0, Set=0):
    if KittyX.location != bg_current:
        return
    call Kitty_Hide
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):
        ease 0.5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Kitty_Sprite zorder KittyX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (KittyX.sprite_location,50)
    $ KittyX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Kitty_Hide(Sprite=0):
    call Kitty_Sex_Reset
    hide Kitty_SexSprite
    hide Kitty_Doggy_Animation
    hide Kitty_HJ_Animation
    hide Kitty_BJ_Animation
    hide Kitty_TJ_Animation
    if Sprite:
        hide Kitty_Sprite
    return

label Kitty_ThreewayBreasts_Launch:
    show Kitty_Sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location):

        ease 0.5 pos (700,200) xzoom -1.5 yzoom 1.5
    $ KittyX.ArmPose = 1
    return













image GropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (215,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (120,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat


image LickRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -40 pos (95,370)
            pause 0.5
            ease 1.5 rotate 30 pos (115,400)
            repeat

image LickLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease 0.5 rotate -40 pos (190,380)
            pause 0.5
            ease 1.5 rotate 30 pos (200,410)
            repeat

image GropeThigh_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause 0.5
            ease 1 ypos 780
            ease 1 ypos 720
            repeat
        parallel:
            pause 0.5
            ease 1 rotate 110 xpos 180
            ease 1 rotate 100 xpos 200
            repeat

image GropePussy_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (210,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease 0.5 rotate 190 pos (210,625)
                ease 0.75 rotate 170 pos (210,640)
            choice:
                ease 0.5 rotate 190 pos (210,625)
                pause 0.25
                ease 1 rotate 170 pos (210,640)
            repeat

image FingerPussy_Kitty:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (220,730)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (230,695)
                pause 0.5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease 0.5 rotate 40 pos (230,695)
                pause 0.5
                ease 1.75 rotate 50 pos (220,730)
            choice:
                ease 2 rotate 40 pos (230,695)
                pause 0.5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease 0.25 rotate 40 pos (230,695)
                ease 0.25 rotate 50 pos (220,730)
                ease 0.25 rotate 40 pos (230,695)
                ease 0.25 rotate 50 pos (220,730)
            repeat

image Lickpussy_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (240,680)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout 0.5 rotate -50 pos (220,660)
            linear 0.5 rotate -60 pos (210,670)
            easein 1 rotate 10 pos (240,680)
            repeat

image VibratorRightBreast_Kitty:
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
            pause 0.25
            ease 1 rotate 55 ypos 380
            pause 0.25
            repeat

image VibratorLeftBreast_Kitty:
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
            pause 0.25
            ease 1 rotate 55 ypos 400
            pause 0.25
            repeat

image VibratorPussy_Kitty:
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
            pause 0.25
            ease 1 rotate 70 xpos 240 ypos 665
            pause 0.25
            repeat

image VibratorAnal_Kitty:
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
            pause 0.25
            ease 1 rotate 10 xpos 270 ypos 665
            pause 0.25
            repeat

image VibratorPussyInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Kitty:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (240,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (230,390)
            ease 1 rotate -20 pos (240,400)
            repeat

image GirlGropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -30 pos (110,410)
            ease 1 rotate -10 pos (110,380)
            repeat

image GirlGropeThigh_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (210,730)
        anchor (0.5,0.5)
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

image GirlGropePussy_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (210,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (215,640)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (215,640)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:


                ease 0.5 rotate 205 pos (215,640)
                ease 0.75 rotate 200 pos (215,645)
                ease 0.5 rotate 205 pos (215,640)
                ease 0.75 rotate 200 pos (215,645)
            choice:
                ease 0.3 rotate 205 pos (215,640)
                ease 0.3 rotate 200 pos (215,650)
                ease 0.3 rotate 205 pos (215,640)
                ease 0.3 rotate 200 pos (215,650)
            repeat

image GirlFingerPussy_Kitty:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom 0.6
        pos (220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease 0.75 rotate 210 pos (220,645)
                ease 0.5 rotate 195
                ease 0.75 rotate 210
                ease 0.5 rotate 195
            choice:
                ease 0.5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause 0.25
                ease 0.5 rotate 210
                ease 1 rotate 195
                pause 0.25
            choice:
                ease 0.5 rotate 205 pos (220,655)
                ease 0.75 rotate 200 pos (220,660)
                ease 0.5 rotate 205 pos (220,655)
                ease 0.75 rotate 200 pos (220,660)
            choice:
                ease 0.3 rotate 205 pos (220,655)
                ease 0.3 rotate 200 pos (220,665)
                ease 0.3 rotate 205 pos (220,655)
                ease 0.3 rotate 200 pos (220,665)
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
