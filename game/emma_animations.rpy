
image Emma_Sprite:
    LiveComposite(
        (402,965),





        (0,0), ConditionSwitch(

            "EmmaX.Uptop or EmmaX.top == 'jacket' or EmmaX.bra != 'corset'", Null(),
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Cape2.png",
            "True", "images/EmmaSprite/EmmaSprite_Cape1.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs == 'dress' and EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Dress_Back.png",
            "EmmaX.legs == 'dress'", "images/EmmaSprite/EmmaSprite_Dress.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png",
            "EmmaX.top and EmmaX.Uptop and EmmaX.top == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet' or EmmaX.Water", "images/EmmaSprite/EmmaSprite_HairbackWet.png",
            "EmmaX.hair", "images/EmmaSprite/EmmaSprite_Hairback.png",
            "True", Null(),
            ),





        (0,0), ConditionSwitch(

            "not EmmaX.underwear or not EmmaX.underwearDown or (EmmaX.legs == 'pants' and not EmmaX.Upskirt)", Null(),
            "EmmaX.underwear == 'sports_panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownBack.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini_DownBack.png",
            "True", "images/EmmaSprite/EmmaSprite_Panties_DownBack.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Legs_Arms2.png",
            "True", "images/EmmaSprite/EmmaSprite_Legs_Arms1.png",
            ),

        (215,540), ConditionSwitch(

            "not EmmaX.Wet", Null(),
            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", Null(),
            "EmmaX.underwear and not EmmaX.underwearDown and EmmaX.Wet <= 1", Null(),
            "EmmaX.Wet == 1", ConditionSwitch(
                    "EmmaX.underwear and EmmaX.underwearDown", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),
                    "EmmaX.legs == 'pants'", AlphaMask("Wet_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Emma_Drip_Mask"),
                    ),
            "True", ConditionSwitch(
                    "EmmaX.underwear and EmmaX.underwearDown", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"),
                    "EmmaX.legs == 'pants'", AlphaMask("Wet_Drip2","Emma_Drip_MaskP"),
                    "EmmaX.underwear", AlphaMask("Wet_Drip","Emma_Drip_Mask"),
                    "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"),
                    ),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.Wet", Null(),
            "EmmaX.legs and EmmaX.Wet <= 1", Null(),
            "EmmaX.legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "EmmaX.Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",
            ),

        (215,540), ConditionSwitch(

            "'in' not in EmmaX.Spunk and 'anal' not in EmmaX.Spunk", Null(),
            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", Null(),
            "True", ConditionSwitch(
                    "EmmaX.underwear and EmmaX.underwearDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "EmmaX.legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Emma_Drip_Mask"),
                    ),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.pubes", "images/EmmaSprite/EmmaSprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.piercings", Null(),
            "EmmaX.underwear and not EmmaX.underwearDown", Null(),
            "EmmaX.legs != 'skirt' and EmmaX.legs and not EmmaX.Upskirt", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Barbell.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_Ring.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.Water", "images/EmmaSprite/EmmaSprite_Water_Legs.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "renpy.showing('Emma_FJ_Animation')", Null(),
            "EmmaX.hose == 'stockings'", "images/EmmaSprite/EmmaSprite_Stockings.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSprite/EmmaSprite_StockingsGarter.png",
            "EmmaX.hose == 'garterbelt'", "images/EmmaSprite/EmmaSprite_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.underwearDown and EmmaX.accessory == 'thigh boots'", "images/EmmaSprite/EmmaSprite_Boots.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.underwear or not EmmaX.underwearDown or (EmmaX.legs == 'pants' and not EmmaX.Upskirt)", Null(),
            "EmmaX.underwear == 'sports_panties' and EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Sports_DownWet.png",
            "EmmaX.underwear == 'sports_panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports_Down.png",
            "EmmaX.underwear == 'lace_panties' and EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Lace_DownWet.png",
            "EmmaX.underwear == 'lace_panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace_Down.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini_Down.png",

            "True", "images/EmmaSprite/EmmaSprite_Panties_Down.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.underwearDown or not EmmaX.underwear", Null(),

            "EmmaX.underwear == 'sports_panties'", "images/EmmaSprite/EmmaSprite_Panties_Sports.png",
            "EmmaX.underwear == 'lace_panties' and EmmaX.Wet", "images/EmmaSprite/EmmaSprite_Panties_Lace_Wet.png",
            "EmmaX.underwear == 'lace_panties'", "images/EmmaSprite/EmmaSprite_Panties_Lace.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaSprite/EmmaSprite_Panties_Bikini.png",

            "True", "images/EmmaSprite/EmmaSprite_Panties.png",
            ),
        (0,0), ConditionSwitch(

            "renpy.showing('Emma_FJ_Animation')", Null(),
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_Hose.png",
            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_HoseHoled.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs and EmmaX.legs != 'skirt' and not EmmaX.Upskirt", Null(),
            "'in' in EmmaX.Spunk or 'anal' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.legs", Null(),
            "EmmaX.Upskirt", ConditionSwitch(

                        "EmmaX.legs == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Up.png",
                        "EmmaX.legs == 'skirt'", "images/EmmaSprite/EmmaSprite_SkirtUp.png",
                        "EmmaX.accessory", Null(),
                        "EmmaX.legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants_Down.png",
                        "EmmaX.legs == 'yoga_pants'", "images/EmmaSprite/EmmaSprite_Pants_Yoga_Down.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(

                    "EmmaX.legs == 'dress' and renpy.showing('Emma_FJ_Animation')","images/EmmaSprite/EmmaSprite_Dress_Up.png",
                    "EmmaX.legs == 'dress'", "images/EmmaSprite/EmmaSprite_Dress.png",
                    "EmmaX.legs == 'skirt'", "images/EmmaSprite/EmmaSprite_Skirt.png",
                    "EmmaX.Wet", ConditionSwitch(

                        "EmmaX.legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants.png",
                        "EmmaX.legs == 'yoga_pants'", "images/EmmaSprite/EmmaSprite_Pants_YogaWet.png",
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(

                        "EmmaX.legs == 'pants'", "images/EmmaSprite/EmmaSprite_Pants.png",
                        "EmmaX.legs == 'yoga_pants'", "images/EmmaSprite/EmmaSprite_Pants_Yoga.png",
                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.underwearDown and EmmaX.accessory == 'thigh boots'", "images/EmmaSprite/EmmaSprite_Boots.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs == 'skirt'", Null(),
            "EmmaX.legs == 'dress'", Null(),
            "EmmaX.piercings == 'barbell'", ConditionSwitch(

                    "EmmaX.legs and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png",
                    "EmmaX.underwear and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_BarOut.png",
                    "True", Null(),
                    ),
            "EmmaX.piercings == 'ring'", ConditionSwitch(

                    "EmmaX.legs and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png",
                    "EmmaX.underwear and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_Pierce_Pussy_RingOut.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.bra == 'sports_bra' and not EmmaX.Uptop", "images/EmmaSprite/EmmaSprite_Bra_Sports_Under.png",
            "EmmaX.bra == 'lace_bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace_Under.png",
            "EmmaX.bra == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetUnder.png",
            "EmmaX.bra == 'bikini_top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Under.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.top == 'dress' and not EmmaX.Upskirt and not renpy.showing('Emma_FJ_Animation')", "images/EmmaSprite/EmmaSprite_Dress_Loincloth.png",
            "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Under.png",
            "EmmaX.top == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Under.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'belly' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Arms2.png",
            "True", "images/EmmaSprite/EmmaSprite_Arms1.png",
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.Water", Null(),
            "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Water_Arms1.png",
            "True", "images/EmmaSprite/EmmaSprite_Water_Arms2.png",
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.arms", Null(),
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Gloves_Arms2.png",
            "True", "images/EmmaSprite/EmmaSprite_Gloves_Arms1.png",
            ),

        (0,0), ConditionSwitch(

            "not EmmaX.Uptop or EmmaX.top != 'jacket'", Null(),
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Jacket_2Arm_Up.png",
            "True", "images/EmmaSprite/EmmaSprite_Jacket_1Arm_Up.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_TitsUp.png",
            "EmmaX.bra in ('corset','lace_bra','sports_bra','bikini_top')", "images/EmmaSprite/EmmaSprite_TitsUp.png",
            "True", "images/EmmaSprite/EmmaSprite_TitsDown.png",
            ),
        (0,0), ConditionSwitch(


            "not EmmaX.piercings", Null(),
            "EmmaX.piercings == 'barbell'", ConditionSwitch(

                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",
                    "EmmaX.bra in ('corset','lace_bra','sports_bra','bikini_top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Barbell.png",


                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Barbell.png",
                    ),
            "EmmaX.piercings == 'ring'", ConditionSwitch(

                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",
                    "EmmaX.bra in ('corset','lace_bra','sports_bra','bikini_top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_Ring.png",


                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_Ring.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.neck == 'choker'", "images/EmmaSprite/EmmaSprite_Neck_Choker.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.Water", Null(),
            "EmmaX.ArmPose == 1 or EmmaX.bra == 'corset'", "images/EmmaSprite/EmmaSprite_Water_TitsUp.png",
            "True", "images/EmmaSprite/EmmaSprite_Water_TitsDown.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.Uptop and EmmaX.bra", ConditionSwitch(

                            "EmmaX.bra == 'sports_bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports_Up.png",
                            "EmmaX.bra == 'lace_bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace_Up.png",
                            "EmmaX.bra == 'bikini_top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini_Up.png",
                            "EmmaX.bra == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits_Up.png",
                            "True", Null(),
                            ),
            "EmmaX.bra == 'sports_bra'", "images/EmmaSprite/EmmaSprite_Bra_Sports.png",
            "EmmaX.bra == 'lace_bra'", "images/EmmaSprite/EmmaSprite_Bra_Lace.png",
            "EmmaX.bra == 'bikini_top'", "images/EmmaSprite/EmmaSprite_Bra_Bikini.png",
            "EmmaX.bra == 'corset' and EmmaX.top", "images/EmmaSprite/EmmaSprite_CorsetTitsX.png",
            "EmmaX.bra == 'corset'", "images/EmmaSprite/EmmaSprite_CorsetTits.png",
            "True", Null(),
            ),




        (0,0), ConditionSwitch(

            "EmmaX.Uptop or EmmaX.top == 'jacket' or EmmaX.bra != 'corset'", Null(),
            "EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Cape2.png",
            "True", "images/EmmaSprite/EmmaSprite_Cape1.png",
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.top", Null(),
            "EmmaX.ArmPose == 2", ConditionSwitch(

                    "EmmaX.Uptop", ConditionSwitch(
                                    "EmmaX.bra in ('corset','lace_bra','sports_bra','bikini_top')", ConditionSwitch(

                                            "EmmaX.top == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Top2U_Up.png",
                                            "EmmaX.top == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Up_Up.png",
                                            "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png",
                                            "True", Null(),
                                            ),

                                    "EmmaX.top == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Top2D_Up.png",
                                    "EmmaX.top == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Down_Up.png",
                                    "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up2_Up.png",
                                    "True", Null(),
                                    ),

                    "EmmaX.bra in ('corset','lace_bra','sports_bra','bikini_top')", ConditionSwitch(

                            "EmmaX.top == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Top2U.png",
                            "EmmaX.top == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Up.png",
                            "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_2Up.png",
                            "EmmaX.top == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up2.png",
                            "True", Null(),
                            ),

                    "EmmaX.top == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Top2D.png",
                    "EmmaX.top == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_2Down.png",
                    "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_2Down.png",
                    "EmmaX.top == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Down2.png",
                    "True", Null(),
                    ),

            "EmmaX.Uptop", ConditionSwitch(

                            "EmmaX.top == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Top1_Up.png",
                            "EmmaX.top == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up_Up.png",
                            "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_Up1_Up.png",
                            "True", Null(),
                            ),

            "EmmaX.top == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Top1.png",
            "EmmaX.top == 'jacket'", "images/EmmaSprite/EmmaSprite_Jacket_1Up.png",
            "EmmaX.top == 'nighty'", "images/EmmaSprite/EmmaSprite_Nighty_1Up.png",
            "EmmaX.top == 'towel'", "images/EmmaSprite/EmmaSprite_Towel_Up1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "not EmmaX.piercings or EmmaX.Uptop or (not EmmaX.top and not EmmaX.bra)", Null(),
            "EmmaX.piercings == 'barbell'", ConditionSwitch(

                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",
                    "EmmaX.bra in ('corset','lace_bra','sports_bra','bikini_top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_BarOut.png",


                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_BarOut.png",
                    ),
            "EmmaX.piercings == 'ring'", ConditionSwitch(

                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",
                    "EmmaX.bra in ('corset','lace_bra','sports_bra','bikini_top')", "images/EmmaSprite/EmmaSprite_Pierce_Up_RingOut.png",


                    "True", "images/EmmaSprite/EmmaSprite_Pierce_Down_RingOut.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'tits' in EmmaX.Spunk", ConditionSwitch(

                    "EmmaX.ArmPose == 1", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "EmmaX.bra == 'corset'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "EmmaX.bra == 'lace_bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "EmmaX.bra == 'sports_bra'", "images/EmmaSprite/EmmaSprite_Spunk_TitsU.png",
                    "True", "images/EmmaSprite/EmmaSprite_Spunk_TitsD.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs == 'dress' and EmmaX.Upskirt and EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Dress_Over2.png",
            "EmmaX.legs == 'dress' and EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_Dress_Over1.png",
            "True", Null(),
            ),
        (55,0), "EmmaSprite_Head",
        (0,0), ConditionSwitch(

            "EmmaX.ArmPose != 2 or 'hand' not in EmmaX.Spunk", Null(),
            "'mouth' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Spunk_HandM.png",
            "True", "images/EmmaSprite/EmmaSprite_Spunk_Hand.png",
            ),








        (0,0), ConditionSwitch(

            "EmmaX.location == 'bg_teacher'", Null(),
            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != EmmaX", Null(),


            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_EmmaSelf",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Emma",

                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeRightBreast_Emma",

                    "True", "GirlGropeBothBreast_Emma",

                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Emma",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Emma",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Emma",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Emma",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.location == 'bg_teacher'", Null(),
            "not second_girl_offhand_action or second_girl_primary_action != 'masturbation' or focused_Girl == EmmaX", Null(),


            "second_girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and EmmaX.lust >= 70", "GirlFingerPussy_Emma",
            "second_girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Emma",
            "second_girl_offhand_action == 'fondle_breasts'", "GirlGropeRightBreast_Emma",
            "second_girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_offhand_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.location == 'bg_teacher'", Null(),
            "not primary_action or focused_Girl != EmmaX", Null(),


            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Emma",
            "primary_action == 'fondle_thighs'", "GropeThigh_Emma",
            "primary_action == 'fondle_breasts'", "GropeLeftBreast_Emma",
            "primary_action == 'suck breasts'", "LickRightBreast_Emma",
            "primary_action == 'fondle_pussy' and action_speed == 2", "FingerPussy_Emma",
            "primary_action == 'fondle_pussy'", "GropePussy_Emma",
            "primary_action == 'eat_pussy'", "Lickpussy_Emma",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Emma",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "primary_action == 'vibrator anal'", "VibratorAnal_Emma",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Emma",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.location == 'bg_teacher'", Null(),
            "not offhand_action or focused_Girl != EmmaX", Null(),


            "offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "offhand_action == 'fondle_breasts' and primary_action == 'suck breasts'", "GropeLeftBreast_Emma",

                    "True", "GropeRightBreast_Emma",

                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast_Emma",

            "offhand_action == primary_action", Null(),

            "offhand_action == 'suck breasts'", "LickLeftBreast_Emma",
            "offhand_action == 'fondle_pussy'", "GropePussy_Emma",
            "offhand_action == 'eat_pussy'", "Lickpussy_Emma",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Emma",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Emma",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Emma",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Emma",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Emma",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.location == 'bg_teacher'", Null(),
            "not second_girl_primary_action or focused_Girl != EmmaX", Null(),


            "second_girl_primary_action == 'fondle_pussy' and primary_action != 'sex' and EmmaX.lust >= 70", "GirlFingerPussy_Emma",
            "second_girl_primary_action == 'fondle_pussy'", "GirlGropePussy_Emma",
            "second_girl_primary_action == 'eat_pussy'", "Lickpussy_Emma",
            "second_girl_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Emma",
            "second_girl_primary_action == 'suck breasts'", "LickRightBreast_Emma",
            "second_girl_primary_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Emma",





                    "True", "GirlGropeRightBreast_Emma",

                    ),
            "second_girl_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "second_girl_primary_action == 'vibrator pussy'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "second_girl_primary_action == 'vibrator anal'", "VibratorAnal",
            "second_girl_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.location == 'bg_teacher'", Null(),
            "primary_action != 'lesbian' or focused_Girl == EmmaX or not girl_offhand_action", Null(),


            "girl_offhand_action == 'fondle_pussy' and primary_action != 'sex' and EmmaX.lust >= 70", "GirlFingerPussy_Emma",
            "girl_offhand_action == 'fondle_pussy'", "GirlGropePussy_Emma",
            "girl_offhand_action == 'eat_pussy'", "Lickpussy_Emma",
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Emma",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast_Emma",
            "girl_offhand_action == 'fondle_breasts'", ConditionSwitch(
                    "primary_action == 'fondle_breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Emma",

                    "offhand_action == 'fondle_breasts' or offhand_action == 'suck breasts'", "GirlGropeRightBreast_Emma",

                    "girl_offhand_action == 'fondle_breasts' or girl_offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Emma",

                    "True", "GirlGropeRightBreast_Emma",

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
    zoom .75

image TempHairBack:
    "images/EmmaSprite/EmmaSprite_Head_HairBackWet.png"
    anchor (0.6, 0.0)
    zoom .5

image EmmaSprite_Head:
    LiveComposite(
        (555,673),























































        (0,0), ConditionSwitch(

                "not EmmaX.blushing", ConditionSwitch(

                    "EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet' or EmmaX.Water", ConditionSwitch(

                            "EmmaX.brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_Angry.png",
                            "EmmaX.brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_Sad.png",
                            "EmmaX.brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_Surprised.png",
                            "EmmaX.brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_Confused.png",
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_Normal.png",
                            ),
                    "True", ConditionSwitch(

                            "EmmaX.brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_Angry.png",
                            "EmmaX.brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_Sad.png",
                            "EmmaX.brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_Surprised.png",
                            "EmmaX.brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_Confused.png",
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_Normal.png",
                            ),
                    ),
                "EmmaX.blushing == 1", ConditionSwitch(

                    "EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet' or EmmaX.Water", ConditionSwitch(

                            "EmmaX.brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB1.png",
                            "EmmaX.brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB1.png",
                            "EmmaX.brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB1.png",
                            "EmmaX.brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB1.png",
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB1.png",
                            ),
                    "True", ConditionSwitch(

                            "EmmaX.brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB1.png",
                            "EmmaX.brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB1.png",
                            "EmmaX.brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB1.png",
                            "EmmaX.brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB1.png",
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB1.png",
                            ),
                    ),
                "True", ConditionSwitch(

                    "EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet' or EmmaX.Water", ConditionSwitch(

                            "EmmaX.brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wet_AngryB2.png",
                            "EmmaX.brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wet_SadB2.png",
                            "EmmaX.brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wet_SurprisedB2.png",
                            "EmmaX.brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wet_ConfusedB2.png",
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wet_NormalB2.png",
                            ),
                    "True", ConditionSwitch(

                            "EmmaX.brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Wave_AngryB2.png",
                            "EmmaX.brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Wave_SadB2.png",
                            "EmmaX.brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Wave_SurprisedB2.png",
                            "EmmaX.brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Wave_ConfusedB2.png",
                            "True", "images/EmmaSprite/EmmaSprite_Head_Wave_NormalB2.png",
                            ),
                    ),
                ),
        (0,0), ConditionSwitch(

            "EmmaX.mouth == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            "EmmaX.mouth == 'lipbite'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Lipbite.png",
            "EmmaX.mouth == 'sucking'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",
            "EmmaX.mouth == 'kiss'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Kiss.png",
            "EmmaX.mouth == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Sad.png",
            "EmmaX.mouth == 'smile'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "EmmaX.mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Surprised.png",
            "EmmaX.mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Tongue.png",
            "EmmaX.mouth == 'grimace'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smile.png",
            "EmmaX.mouth == 'smirk'", "images/EmmaSprite/EmmaSprite_Head_Mouth_Smirk.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Mouth_Normal.png",
            ),

        (0,0), ConditionSwitch(

            "'mouth' not in EmmaX.Spunk", Null(),
            "EmmaX.mouth == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthOpen.png",
            "EmmaX.mouth == 'tongue'", "images/EmmaSprite/EmmaSprite_Head_Spunk_MouthTongue.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Spunk_Mouth.png",
            ),

        (0,0), "Emma Blink",

        (0,0), ConditionSwitch(

            "EmmaX.brows == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            "EmmaX.brows == 'angry'", "images/EmmaSprite/EmmaSprite_Head_Brows_Angry.png",
            "EmmaX.brows == 'sad'", "images/EmmaSprite/EmmaSprite_Head_Brows_Sad.png",
            "EmmaX.brows == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Brows_Surprised.png",
            "EmmaX.brows == 'confused'", "images/EmmaSprite/EmmaSprite_Head_Brows_Confused.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(

            "'facial' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_Face.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet' or EmmaX.Water", "images/EmmaSprite/EmmaSprite_Head_HairWet.png",
            "True", "images/EmmaSprite/EmmaSprite_Head_Hair.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.Water", "images/EmmaSprite/EmmaSprite_Head_Water.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'hair' in EmmaX.Spunk and (EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet' or EmmaX.Water)", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWet.png",
            "'hair' in EmmaX.Spunk", "images/EmmaSprite/EmmaSprite_Head_Spunk_HairWave.png",
            "True", Null(),
            ),
        (-1,0), ConditionSwitch(

            "EmmaX.hair == 'hat wet' or (EmmaX.hair == 'hat' and EmmaX.Water)", "images/EmmaSprite/EmmaSprite_Shadow_Wet.png",
            "EmmaX.hair == 'hat'", "images/EmmaSprite/EmmaSprite_Shadow_Long.png",
            "True", Null(),
            ),
        (-125,-95), ConditionSwitch(

            "EmmaX.hair == 'hat wet' or EmmaX.hair == 'hat'", "images/EmmaSprite/EmmaSprite_Hat.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    zoom .5

image Emma Blink:
    ConditionSwitch(
        "EmmaX.eyes == 'sexy'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png",
        "EmmaX.eyes == 'side'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Side.png",
        "EmmaX.eyes == 'surprised'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
        "EmmaX.eyes == 'normal'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",
        "EmmaX.eyes == 'stunned'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Agao.png",
        "EmmaX.eyes == 'down'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Down.png",
        "EmmaX.eyes == 'closed'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png",
        "EmmaX.eyes == 'manic'", "images/EmmaSprite/EmmaSprite_Head_Eyes_Surprised.png",
        "EmmaX.eyes == 'squint'", "Emma_Squint",
        "True", "images/EmmaSprite/EmmaSprite_Head_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Closed.png"
    .25
    repeat

image Emma_Squint:
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/EmmaSprite/EmmaSprite_Head_Eyes_Squint.png"
    .25
    repeat

image Emma_Drip_Mask:

    contains:
        "images/EmmaSprite/EmmaSprite_WetMask.png"
        offset (-215,-540)

image Emma_Drip_MaskP:

    contains:
        "images/EmmaSprite/EmmaSprite_WetMaskP.png"
        offset (-215,-540)







image Emma_SexSprite:

    contains:
        ConditionSwitch(

            "primary_action == 'eat_pussy' or primary_action == 'eat_ass'", "Emma_Sex_Legs_Lick",
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(

                    "action_speed == 1", "Emma_Sex_Legs_S1",
                    "action_speed == 2", "Emma_Sex_Legs_S2",
                    "action_speed == 3", "Emma_Sex_Legs_S3",
                    "action_speed >= 4", "Emma_Sex_Legs_S4",
                    "True", "Emma_Sex_Legs_S0",
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(

                    "action_speed == 1", "Emma_Sex_Legs_A1",
                    "action_speed == 2", "Emma_Sex_Legs_A2",
                    "action_speed == 3", "Emma_Sex_Legs_A3",
                    "action_speed >= 4", "Emma_Sex_Legs_A4",
                    "True", "Emma_Sex_Legs_A0",
                    ),
            "True", ConditionSwitch(

                    "action_speed == 1", "Emma_Sex_Legs_H1",
                    "action_speed == 4", "Emma_Sex_Legs_H4",
                    "action_speed >= 2", "Emma_Sex_Legs_H2",
                    "True", "Emma_Sex_Legs_H0",
                    ),
            )
    contains:
        ConditionSwitch(

            "primary_action == 'eat_pussy' or primary_action == 'eat_ass'",  "Emma_Sex_Body_Lick",
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(

                    "action_speed == 1", "Emma_Sex_Body_S1",
                    "action_speed == 2", "Emma_Sex_Body_S2",
                    "action_speed == 3", "Emma_Sex_Body_S3",
                    "action_speed >= 4", "Emma_Sex_Body_S4",
                    "True",       "Emma_Sex_Body_S0",
                    ),
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(

                    "action_speed == 1", "Emma_Sex_Body_A1",
                    "action_speed == 2", "Emma_Sex_Body_A2",
                    "action_speed == 3", "Emma_Sex_Body_A3",
                    "action_speed >= 4", "Emma_Sex_Body_A4",
                    "True",       "Emma_Sex_Body_A0",
                    ),
            "True", ConditionSwitch(

                    "action_speed == 1", "Emma_Sex_Body_H1",
                    "action_speed == 4", "Emma_Sex_Body_H4",
                    "action_speed >= 2", "Emma_Sex_Body_H2",
                    "True",       "Emma_Sex_Body_H0",
                    ),
            )
    zoom 0.8
    anchor (.5,.5)

image Emma_Sex_HairBack:

    "Emma_BJ_HairBack"
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)

image Emma_Sex_Head:

    "Emma_BJ_Head"
    zoom 0.48
    anchor (0.5, 0.5)
    pos (505,260)





image Emma_Sex_Torso:




    contains:

        ConditionSwitch(
            "EmmaX.arms and not (EmmaX.top == 'jacket' or EmmaX.top == 'dress')", "images/EmmaSex/Emma_Sex_Body_G.png",
            "True", "images/EmmaSex/Emma_Sex_Body.png",
            )
    contains:

        ConditionSwitch(
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.bra and not EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Tits_Up.png",
            "True", "images/EmmaSex/Emma_Sex_Tits_Down.png",
            )
    contains:

        ConditionSwitch(
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "(EmmaX.top or EmmaX.bra) and not EmmaX.Uptop", Null(),
            "EmmaX.piercings == 'barbell'", ConditionSwitch(

                    "not EmmaX.bra or EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Barbell_Tits_D.png",
                    "True", Null(),
                    ),
            "EmmaX.piercings == 'ring'", ConditionSwitch(

                    "not EmmaX.bra or EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Ring_Tits_D.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "EmmaX.bra == 'sports_bra' and (EmmaX.Uptop or renpy.showing('Emma_TJ_Animation'))", "images/EmmaSex/Emma_Sex_Bra_Sports_Uptop.png",
            "EmmaX.bra == 'bikini_top' and (EmmaX.Uptop or renpy.showing('Emma_TJ_Animation'))", "images/EmmaSex/Emma_Sex_Bra_Bikini_Uptop.png",
            "EmmaX.Uptop or renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.bra == 'corset'", "images/EmmaSex/Emma_Sex_Bra_Corset_Up.png",
            "EmmaX.bra == 'sports_bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_Up.png",
            "EmmaX.bra == 'bikini_top'", "images/EmmaSex/Emma_Sex_Bra_Bikini_Up.png",
            "EmmaX.bra == 'lace_bra'", "images/EmmaSex/Emma_Sex_Bra_Lace_Up.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.top == 'jacket'", ConditionSwitch(


                    "renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Sex_Jacket_TJ.png",
                    "EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Jacket_Down_Uptop.png",
                    "EmmaX.bra and not EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Jacket_Up.png",
                    "True", "images/EmmaSex/Emma_Sex_Jacket_Down.png",
                    ),
            "EmmaX.top == 'nighty'", ConditionSwitch(


                    "EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Nighty_Uptop.png",
                    "EmmaX.bra and not renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Sex_Nighty_Up.png",

                    "True", "images/EmmaSex/Emma_Sex_Nighty_Down.png",
                    ),
            "EmmaX.top == 'dress'", ConditionSwitch(


                    "renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Sex_Dress_TJ.png",
                    "EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Dress_Uptop.png",
                    "EmmaX.bra and not EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Dress_Up.png",
                    "True", "images/EmmaSex/Emma_Sex_Dress_Down.png",
                    ),
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "renpy.showing('Emma_TJ_Animation')", Null(),
            "EmmaX.Uptop or not EmmaX.piercings", Null(),
            "EmmaX.bra and not EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Barbell_Tits_UC.png",
            "EmmaX.top and not EmmaX.Uptop", "images/EmmaSex/Emma_Pierce_Barbell_Tits_DC.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
                "'tits' not in EmmaX.Spunk", Null(),
                "renpy.showing('Emma_TJ_Animation')", "images/EmmaSex/Emma_Spunk_Titjob_Under.png",
                "True", "images/EmmaSex/Emma_Spunk_Tits.png",
                )
    zoom 1

image Emma_Sex_Lick_Breasts_High:
    "Lick_Anim"
    zoom 0.7
    offset (400,590)

image Emma_Sex_Lick_Breasts:
    "Lick_Anim"
    zoom 0.7
    offset (390,620)

image Emma_Sex_Fondle_Breasts:
    "GropeLeftBreast"
    zoom 1.5
    offset (160,-40)

image Emma_Sex_Body:

    contains:
        "Emma_Sex_HairBack"
    contains:

        "Emma_Sex_Torso"
    contains:

        ConditionSwitch(
            "EmmaX.ArmPose == 3", Null(),
            "EmmaX.ArmPose == 4", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask_R.png"),
            "EmmaX.ArmPose == 5", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask_L.png"),
            "True", AlphaMask("Emma_SexArms", "images/EmmaSex/Emma_Sex_ArmsMask.png"),
            )
    contains:
        ConditionSwitch(

            "(primary_action == 'suck breasts' or offhand_action == 'suck breasts') and EmmaX.bra and not EmmaX.Uptop", "Emma_Sex_Lick_Breasts_High",
            "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Emma_Sex_Lick_Breasts",
            "True", Null()
            )
    contains:
        ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Emma_Sex_Fondle_Breasts",
            "True", Null()
            )
    contains:
        "Emma_Sex_Head"
    zoom 1




image Emma_SexArms:
    contains:

        ConditionSwitch(
            "EmmaX.top == 'jacket' or EmmaX.top == 'dress'", Null(),

            "EmmaX.bra and not EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Arms_U.png",




            "True", "images/EmmaSex/Emma_Sex_Arms_D.png",
            )
    contains:

        ConditionSwitch(
            "EmmaX.top == 'jacket' or EmmaX.top == 'dress'", Null(),
            "EmmaX.bra == 'sports_bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_Arms.png",
            "True", Null(),
            )
    contains:







        ConditionSwitch(
            "EmmaX.top == 'jacket' and EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Arms_Jacket_Uptop.png",
            "EmmaX.top == 'jacket'", "images/EmmaSex/Emma_Sex_Arms_Jacket.png",
            "EmmaX.top == 'dress'", "images/EmmaSex/Emma_Sex_Arms_Dress.png",
            "EmmaX.arms", "images/EmmaSex/Emma_Sex_Gloves.png",
            "True", Null(),
            )




image Emma_Sex_Legs_S:

    contains:

        ConditionSwitch(

            "(EmmaX.underwear and EmmaX.underwearDown) and (EmmaX.hose == 'pantyhose' or EmmaX.hose == 'ripped_pantyhose')", "images/EmmaSex/Emma_Sex_Feet.png",
            "EmmaX.hose == 'pantyhose' and Player.Sprite and Player.Cock == 'in'","images/EmmaSex/Emma_Sex_Feet.png",
            "EmmaX.hose == 'garterbelt'", "images/EmmaSex/Emma_Sex_Feet.png",
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaSex/Emma_Sex_Feet_Hose_Holed.png",
            "EmmaX.hose", "images/EmmaSex/Emma_Sex_Feet_Hose.png",
            "True", "images/EmmaSex/Emma_Sex_Feet.png",
            )
    contains:

        ConditionSwitch(
            "(EmmaX.legs == 'pants' or EmmaX.legs == 'yoga_pants') and EmmaX.Upskirt", "images/EmmaSex/Emma_Sex_Pants_Down.png",
            "EmmaX.accessory == 'thigh boots'", "images/EmmaSex/Emma_Sex_Feet_Boots.png",
            "EmmaX.legs == 'pants'", "images/EmmaSex/Emma_Sex_Feet_Pants.png",
            "EmmaX.legs == 'yoga_pants'", "images/EmmaSex/Emma_Sex_Feet_YogaPants.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(EmmaX.legs == 'pants' or EmmaX.legs == 'yoga_pants') and not EmmaX.Upskirt", Null(),
            "not EmmaX.underwearDown", Null(),
            "EmmaX.underwear == 'sports_panties'", "images/EmmaSex/Emma_Sex_Panties_Sport_Down.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaSex/Emma_Sex_Panties_Bikini_Down.png",
            "EmmaX.underwear", "images/EmmaSex/Emma_Sex_Panties_Down.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.legs == 'dress'", "images/EmmaSex/Emma_Sex_Dress_S_Back.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'anal' in EmmaX.Spunk or 'in' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'hotdog'", "images/EmmaSex/Emma_Sex_Legs_Hotdog.png",
            "True", "images/EmmaSex/Emma_Sex_Legs_Sex.png",
            )
    contains:

        ConditionSwitch(
            "EmmaX.hose == 'stockings'", "images/EmmaSex/Emma_Sex_Hose_Stockings_S.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSex/Emma_Sex_Hose_StockingsGarter_S.png",
            "EmmaX.hose == 'garterbelt'", "images/EmmaSex/Emma_Sex_Hose_Garter_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "(EmmaX.legs == 'pants' or EmmaX.legs == 'yoga_pants') and not EmmaX.Upskirt", Null(),
            "EmmaX.underwear and not EmmaX.underwearDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C2.png",
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C2.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.pubes", "images/EmmaSex/Emma_Pubes_Sex.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.underwearDown", Null(),
            "EmmaX.underwear == 'sports_panties' and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_Sport_SW.png",
            "EmmaX.underwear == 'sports_panties'", "images/EmmaSex/Emma_Sex_Panties_Sport_S.png",
            "EmmaX.underwear == 'lace_panties'", "images/EmmaSex/Emma_Sex_Panties_Lace_S.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaSex/Emma_Sex_Panties_Bikini_S.png",
            "EmmaX.underwear and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_SW.png",
            "EmmaX.underwear", "images/EmmaSex/Emma_Sex_Panties_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(EmmaX.underwear and EmmaX.underwearDown)", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaSex/Emma_Sex_Hose_PantyhoseHoled_S.png",
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "EmmaX.hose == 'pantyhose'", "images/EmmaSex/Emma_Sex_Hose_Pantyhose_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(not EmmaX.underwear and EmmaX.hose != 'pantyhose') or EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'pantyhose' and EmmaX.underwearDown", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S_C.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.legs == 'dress' and (EmmaX.Upskirt or Player.Sprite)", "images/EmmaSex/Emma_Sex_Dress_S_Up.png",
            "EmmaX.legs == 'dress'", "images/EmmaSex/Emma_Sex_Dress_S.png",
            "EmmaX.legs == 'skirt'", "images/EmmaSex/Emma_Sex_Skirt_Pussy.png",
            "EmmaX.Upskirt", Null(),
            "EmmaX.legs == 'pants' and EmmaX.Wet >= 2", "images/EmmaSex/Emma_Sex_Pants_SW.png",
            "EmmaX.legs == 'pants'", "images/EmmaSex/Emma_Sex_Pants_S.png",
            "EmmaX.legs == 'yoga_pants' and EmmaX.Wet >= 2", "images/EmmaSex/Emma_Sex_YogaPants_SW.png",
            "EmmaX.legs == 'yoga_pants'", "images/EmmaSex/Emma_Sex_YogaPants_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(EmmaX.legs != 'pants' and EmmaX.legs != 'yoga_pants') or EmmaX.Upskirt", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S_C.png",
            "EmmaX.piercings != 'ring'", Null(),
            "EmmaX.underwear and not EmmaX.underwearDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            "True", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S_C.png",
            )
    contains:

        ConditionSwitch(
            "(EmmaX.legs == 'pants' or EmmaX.legs == 'yoga_pants') and EmmaX.Upskirt", Null(),
            "EmmaX.accessory == 'thigh boots'", "images/EmmaSex/Emma_Sex_Boots_Pussy.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.top == 'nighty'", "images/EmmaSex/Emma_Sex_Nighty_Pussy.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'belly' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Belly.png",
            "True", Null(),
            )
    zoom 1


image Emma_Sex_Legs_A:

    contains:

        ConditionSwitch(
            "EmmaX.legs == 'dress'", "images/EmmaSex/Emma_Sex_Dress_A_Back.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'anal' in EmmaX.Spunk and not action_speed", "images/EmmaSex/Emma_Spunk_Anal_Closed.png",
            "True", Null(),
            )
    contains:

        "images/EmmaSex/Emma_Sex_Legs_Anal.png"
    contains:

        ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and action_speed", ConditionSwitch(

                    "action_speed == 1", "Emma_Sex_Anus_A1",
                    "True", "Emma_Sex_Anus_A2",
                    ),
            "True", "Emma_Sex_Anus_A0",
            )
    contains:

        ConditionSwitch(
            "EmmaX.pubes", "images/EmmaSex/Emma_Pubes_Anal.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.underwear and not EmmaX.underwearDown", Null(),
            "(EmmaX.legs == 'pants' or EmmaX.legs == 'yoga_pants') and not EmmaX.Upskirt", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.hose == 'stockings'", "images/EmmaSex/Emma_Sex_Hose_Stockings_A.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSex/Emma_Sex_Hose_StockingsGarter_A.png",
            "EmmaX.hose == 'garterbelt'", "images/EmmaSex/Emma_Sex_Hose_Garter_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.underwearDown", Null(),
            "EmmaX.underwear == 'sports_panties' and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_Sport_AW.png",
            "EmmaX.underwear == 'sports_panties'", "images/EmmaSex/Emma_Sex_Panties_Sport_A.png",
            "EmmaX.underwear == 'lace_panties'", "images/EmmaSex/Emma_Sex_Panties_Lace_A.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaSex/Emma_Sex_Panties_Bikini_A.png",
            "EmmaX.underwear and EmmaX.Wet", "images/EmmaSex/Emma_Sex_Panties_AW.png",
            "EmmaX.underwear", "images/EmmaSex/Emma_Sex_Panties_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'in' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Pussy.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(EmmaX.underwear and EmmaX.underwearDown)", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaSex/Emma_Sex_Hose_PantyhoseHoled_A.png",
            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "EmmaX.hose == 'pantyhose'", "images/EmmaSex/Emma_Sex_Hose_Pantyhose_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(not EmmaX.underwear and EmmaX.hose != 'pantyhose') or EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'pantyhose' and EmmaX.underwearDown", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A_C.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.legs == 'dress' and (EmmaX.Upskirt or Player.Sprite)", "images/EmmaSex/Emma_Sex_Dress_A_Up.png",
            "EmmaX.legs == 'dress'", "images/EmmaSex/Emma_Sex_Dress_A.png",
            "EmmaX.legs == 'skirt'", "images/EmmaSex/Emma_Sex_Skirt_Anal.png",
            "EmmaX.Upskirt", Null(),
            "EmmaX.legs == 'pants' and EmmaX.Wet >= 2", "images/EmmaSex/Emma_Sex_Pants_AW.png",
            "EmmaX.legs == 'pants'", "images/EmmaSex/Emma_Sex_Pants_A.png",
            "EmmaX.legs == 'yoga_pants' and EmmaX.Wet >= 2", "images/EmmaSex/Emma_Sex_YogaPants_AW.png",
            "EmmaX.legs == 'yoga_pants'", "images/EmmaSex/Emma_Sex_YogaPants_A.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "(EmmaX.legs != 'pants' and EmmaX.legs != 'yoga_pants') or EmmaX.Upskirt", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_A_C.png",
            "EmmaX.piercings != 'ring'", Null(),
            "EmmaX.underwear and not EmmaX.underwearDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            "True", "images/EmmaSex/Emma_Pierce_Ring_Pussy_A_C.png",
            )
    contains:

        ConditionSwitch(
            "EmmaX.accessory == 'thigh boots'", "images/EmmaSex/Emma_Sex_Boots_Anal.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.top == 'nighty'", "images/EmmaSex/Emma_Sex_Nighty_Anal.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "'belly' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Belly.png",
            "True", Null(),
            )
        ypos -40
    contains:
        ConditionSwitch(

            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'eat_pussy'", "Emma_Sex_Lick_Pussy",
            "primary_action == 'eat_ass'", "Emma_Sex_Lick_Ass",
            "True", Null()
            )
    zoom 1


image Emma_Sex_Pussy_Mask:
    contains:
        "images/EmmaSex/Emma_Sex_Pussy_Mask.png"
    contains:

        ConditionSwitch(
            "EmmaX.underwear and not EmmaX.underwearDown", Null(),
            "EmmaX.legs and not EmmaX.Upskirt", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )

image Emma_Sex_Hotdog_Mask:
    contains:
        "images/EmmaSex/Emma_Sex_Legs_HotdogMask.png"
    contains:


        ConditionSwitch(
            "EmmaX.underwear and not EmmaX.underwearDown", Null(),
            "EmmaX.legs and not EmmaX.Upskirt", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.underwear and not EmmaX.underwearDown", Null(),
            "EmmaX.legs and not EmmaX.Upskirt", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaSex/Emma_Pierce_Barbell_Pussy_S.png",
            "EmmaX.piercings == 'ring'", "images/EmmaSex/Emma_Pierce_Ring_Pussy_S.png",
            "True", Null(),
            )







image Emma_Sex_Body_Lick:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-80)
        block:
            ease 1 pos (0,-90)
            ease 1 pos (0,-80)
            repeat

image Emma_Sex_Legs_Lick:

    contains:

        "Emma_Sex_Legs_A"
        subpixel True
        pos (0,-40)
        block:
            ease 1 ypos -45
            ease 1 ypos -40
            repeat


image Emma_Sex_Lick_Pussy:
    "Lick_Anim"
    zoom 0.7
    offset (505,680)

image Emma_Sex_Lick_Ass:
    "Lick_Anim"
    zoom 0.7
    offset (500,740)


image Emma_Sex_Body_H0:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10)
        block:
            ease 2 pos (0,0)
            ease 2 pos (0,-10)
            repeat

image Emma_Sex_Body_H1:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10)
        block:
            ease 1.5 pos (0,0)
            ease 1.5 pos (0,-10)
            repeat

image Emma_Sex_Body_H2:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10)
        block:
            ease .6 pos (0,10)
            ease .4 pos (0,-10)
            repeat

image Emma_Sex_Body_H4:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-80)
        block:
            ease 1.5 pos (0,-70)
            ease 2 pos (0,-80)
            pause .5
            repeat

image Emma_Sex_Body_S0:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-60)
        block:
            ease 1 pos (0,-50)
            ease 1 pos (0,-60)
            repeat

image Emma_Sex_Body_S1:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-20)
        block:
            ease .75 pos (0,0)
            ease 1.5 pos (0,-20)
            pause 0.75
            repeat

image Emma_Sex_Body_S2:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-50)
        block:
            ease 0.5 pos (0,20)
            ease 1.5 pos (0,-50)

            repeat

image Emma_Sex_Body_S3:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-50)
        block:
            ease 0.25 pos (0,0)
            ease 0.5 pos (0,-50)
            repeat

image Emma_Sex_Body_S4:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-20)
        block:
            ease 0.5 pos (0,0)
            ease 1 pos (0,-20)
            repeat

image Emma_Sex_Body_A0:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-115)
        block:
            ease 1 pos (0,-95)
            ease 1 pos (0,-115)
            repeat

image Emma_Sex_Body_A1:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-80)
        block:
            easeout 1 pos (0,-60)
            easein 2 pos (0,-40)
            pause 1
            easeout 1 pos (0,-60)
            easein 2 pos (0,-80)
            pause 1
            repeat

image Emma_Sex_Body_A2:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10)
        block:
            ease .30 pos (0,10)
            ease .50 pos (0,50)
            pause .3
            ease .80 pos (0,-10)
            pause .1
            repeat

image Emma_Sex_Body_A3:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,-10)
        block:
            ease .40 pos (0,50)
            ease .60 pos (0,-10)
            repeat

image Emma_Sex_Body_A4:

    contains:
        "Emma_Sex_Body"
        subpixel True
        pos (0,20)
        block:
            ease 1 pos (0,40)
            ease 1 pos (0,20)
            repeat



image Emma_Sex_Legs_H0:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        anchor (.515,.5)
        pos (528,340)
        zoom .95
        parallel:
            ease 2 zoom .98
            ease 2 zoom .95

            repeat
        parallel:
            ease 2 ypos 360
            ease 2 ypos 340

            repeat
    contains:

        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
        alpha 1
        zoom 1.2
        pos (450,590)
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")
        subpixel True
        anchor (.515,.5)
        pos (528,340)
        zoom .95
        parallel:
            ease 2 zoom .98
            ease 2 zoom .95

            repeat
        parallel:
            ease 2 ypos 360
            ease 2 ypos 340

            repeat


image Emma_Sex_Legs_H1:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        anchor (.515,.5)
        pos (528,300)
        zoom .9
        parallel:
            ease 1.5 zoom 1
            ease 1.5 zoom .9
            pause .3
            repeat
        parallel:
            ease 1.5 ypos 390
            ease 1.5 ypos 300
            pause .3
            repeat
    contains:

        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
        alpha 1
        zoom 1.2
        pos (450,590)
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")
        subpixel True
        anchor (.515,.5)
        pos (528,300)
        zoom .9
        parallel:
            ease 1.5 zoom 1
            ease 1.5 zoom .9
            pause .3
            repeat
        parallel:
            ease 1.5 ypos 390
            ease 1.5 ypos 300
            pause .3
            repeat


image Emma_Sex_Legs_H2:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        anchor (.515,.5)
        pos (528,340)
        zoom .95
        parallel:
            ease .6 zoom 1
            ease .4 zoom .95

            repeat
        parallel:
            ease .6 ypos 390
            ease .4 ypos 340

            repeat
    contains:

        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Insert",
                "True", Null(),
                )
        alpha 1
        zoom 1.2
        pos (450,590)
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Hotdog_Mask")
        subpixel True
        anchor (.515,.5)
        pos (528,340)
        zoom .95
        parallel:
            ease .6 zoom 1
            ease .4 zoom .95

            repeat
        parallel:
            ease .6 ypos 390
            ease .4 ypos 340

            repeat


image Emma_Sex_Legs_H4:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True

        pos (0,-80)
        parallel:
            ease 2 ypos -70
            ease 2 ypos -80
            repeat
    contains:


        "Blowcock"
        alpha 1
        zoom 0.5
        pos (680,440)





























image Emma_Sex_Legs_S0:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        pos (0,-140)
        parallel:
            ease 1 ypos -135
            ease 1 ypos -140
            repeat
        parallel:
            ease 2 xpos -8
            ease 2 xpos 8
            repeat
    contains:

        "Blowcock"
        alpha 1
        zoom 0.5
        pos (680,400)
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
        subpixel True
        pos (0,-140)
        parallel:
            ease 1 ypos -135
            ease 1 ypos -140
            repeat
        parallel:
            ease 2 xpos -8
            ease 2 xpos 8
            repeat


image Emma_Sex_Legs_S1:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        pos (0,-120)
        block:
            ease 0.75 ypos -50
            pause 0.75
            ease 1.5 ypos -120
            repeat
    contains:

        "Blowcock"
        subpixel True
        alpha 1
        zoom 0.5
        pos (680,400)
        block:
            ease 0.8 ypos 410
            pause 1
            ease 1.2 ypos 400
            repeat
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
        subpixel True
        pos (0,-120)
        block:
            ease 0.75 ypos -50
            pause 0.75
            ease 1.5 ypos -120
            repeat


image Emma_Sex_Legs_S2:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        pos (0,-150)
        block:
            ease 0.5 ypos 0
            pause 0.5
            ease 1 ypos -150
            repeat
    contains:

        "Blowcock"
        subpixel True
        alpha 1
        zoom 0.5
        pos (680,400)
        block:
            ease 0.4 ypos 430
            pause 1
            ease 0.6 ypos 400
            repeat
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
        subpixel True
        pos (0,-150)
        block:
            ease 0.5 ypos 0
            pause 0.5
            ease 1 ypos -150
            repeat


image Emma_Sex_Legs_S3:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        pos (0,-120)
        block:
            ease 0.25 ypos 10
            ease 0.5 ypos -120
            repeat
    contains:

        "Blowcock"
        subpixel True
        alpha 1
        zoom 0.5
        pos (680,400)
        block:
            ease 0.2 ypos 430
            ease 0.55 ypos 400
            repeat
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
        subpixel True
        pos (0,-120)
        block:
            ease 0.25 ypos 10
            ease 0.5 ypos -120
            repeat


image Emma_Sex_Legs_S4:

    contains:

        "Emma_Sex_Legs_S"
        subpixel True
        pos (0,0)
        block:
            ease 0.5 ypos 10
            ease 1 ypos 0
            repeat
    contains:

        "Blowcock"
        subpixel True
        alpha 1
        zoom 0.5
        pos (680,430)
    contains:

        AlphaMask("Emma_Sex_Legs_S", "Emma_Sex_Pussy_Mask")
        subpixel True
        pos (0,0)
        block:
            ease 0.5 ypos 10
            ease 1 ypos 0
            repeat



image Emma_Sex_Legs_A0:

    contains:

        "Emma_Sex_Legs_A"
        subpixel True
        pos (0,-138)
        block:
            ease 1 ypos -134
            ease 1 ypos -138
            repeat
    contains:

        "Blowcock"
        alpha 1
        zoom 0.5
        pos (681,420)


image Emma_Sex_Legs_A1:

    contains:

        "Emma_Sex_Legs_A"
        subpixel True
        pos (0,-130)
        block:
            ease 4 ypos -80
            ease 4 ypos -130
            repeat
    contains:

        "Blowcock"
        alpha 1
        zoom 0.5
        pos (681,420)
    contains:

        AlphaMask("Emma_Sex_Legs_A", "Emma_Sex_Anus_Mask_A1")
        subpixel True
        pos (0,-130)
        block:
            ease 4 ypos -80
            ease 4 ypos -130
            repeat


image Emma_Sex_Anus_Mask_A1:

    contains:
        contains:
            "images/EmmaSex/Emma_Sex_Anus_Mask.png"
        contains:

            ConditionSwitch(
                "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                "True", Null(),
                )
        subpixel True
        xzoom 0.5
        xpos 250
        parallel:

            pause .2
            ease 2.2 xzoom 0.9
            ease 0.6 xzoom 0.85

            ease 0.75 xzoom 0.9
            pause 0.5
            ease 0.75 xzoom 0.85

            ease 0.6 xzoom 0.9
            ease 2.2 xzoom 0.5
            pause .2
            repeat
        parallel:
            pause .2
            ease 2.2 xpos 50
            ease 0.6 xpos 75

            ease 0.75 xpos 50
            pause 0.5
            ease 0.75 xpos 75

            ease 0.6 xpos 50
            ease 2.2 xpos 250
            pause .2
            repeat


image Emma_Sex_Legs_A2:

    contains:

        "Emma_Sex_Legs_A"
        pos (0,-80)
        subpixel True
        block:
            ease 1 ypos 0
            ease 1 ypos -80
            repeat
    contains:

        "Blowcock"
        subpixel True
        alpha 1
        zoom 0.5
        pos (681,420)
        block:
            ease 1 ypos 430
            ease 1 ypos 400
            repeat
    contains:

        contains:
            AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
        contains:

            ConditionSwitch(
                    "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )
        subpixel True
        pos (0,-80)
        block:
            ease 1 ypos 0
            ease 1 ypos -80
            repeat


image Emma_Sex_Legs_A3:

    contains:

        "Emma_Sex_Legs_A"
        subpixel True
        pos (0,-80)
        block:
            ease 0.5 ypos 20
            ease 0.5 ypos -80
            repeat
    contains:

        "Blowcock"
        subpixel True
        alpha 1
        zoom 0.5
        pos (681,420)
        block:
            ease 0.5 ypos 430
            ease 0.5 ypos 400
            repeat
    contains:

        contains:
            AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
        contains:

            ConditionSwitch(
                    "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )
        subpixel True
        pos (0,-80)
        block:
            ease 0.5 ypos 20
            ease 0.5 ypos -80
            repeat


image Emma_Sex_Legs_A4:

    contains:

        "Emma_Sex_Legs_A"
        subpixel True
        pos (0,15)
        block:
            ease 1 ypos 20
            ease 1 ypos 15
            repeat
    contains:

        "Blowcock"
        subpixel True
        alpha 1
        zoom 0.5
        pos (681,430)
    contains:

        contains:
            AlphaMask("Emma_Sex_Legs_A", "images/EmmaSex/Emma_Sex_Anus_Mask.png" )
        contains:

            ConditionSwitch(
                    "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Open.png",
                    "True", Null(),
                    )
        subpixel True
        pos (0,15)
        block:
            ease 1 ypos 20
            ease 1 ypos 15
            repeat


image Emma_Sex_Anus_A0:

    "images/EmmaSex/Emma_Sex_Anus_Tight.png"
    xpos 0

image Emma_Sex_Anus_A1:

    contains:
        "images/EmmaSex/Emma_Sex_Anus_Open.png"
    contains:

        ConditionSwitch(
                "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
    subpixel True
    xzoom 0.5
    xpos 250
    parallel:

        pause .2
        ease 2.2 xzoom 0.9
        ease 0.6 xzoom 0.85

        ease 0.75 xzoom 0.9
        pause 0.5
        ease 0.75 xzoom 0.85

        ease 0.6 xzoom 0.9
        ease 2.2 xzoom 0.5
        pause .2
        repeat
    parallel:
        pause .2
        ease 2.2 xpos 50
        ease 0.6 xpos 75

        ease 0.75 xpos 50
        pause 0.5
        ease 0.75 xpos 75

        ease 0.6 xpos 50
        ease 2.2 xpos 250
        pause .2
        repeat


image Emma_Sex_Anus_A2:

    contains:
        "images/EmmaSex/Emma_Sex_Anus_Open.png"
    contains:

        ConditionSwitch(
                "'anal' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Anal_Under.png",
                "True", Null(),
                )
    xpos 0



label Emma_Sex_Launch(Line=primary_action):
    $ girl_offhand_action = 0 if girl_offhand_action == "handjob" else girl_offhand_action



    $ Player.Sprite = 1
    $ Line = "solo" if not Line else Line
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

    if EmmaX.pose == "doggy":
        call Emma_Doggy_Launch (Line)
        return
    if renpy.showing("Emma_SexSprite"):
        return
    $ action_speed = 0
    call Emma_Hide (1)

    show Emma_SexSprite zorder 150:
        pos (575,470)
    with dissolve
    return

label Emma_Sex_Reset:
    if renpy.showing("Emma_Doggy_Animation"):
        call Emma_Doggy_Reset
        return
    if not renpy.showing("Emma_SexSprite"):
        return
    $ EmmaX.ArmPose = 2
    hide Emma_SexSprite
    call Emma_Hide
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ action_speed = 0
    return








image Emma_Doggy_Animation:
    LiveComposite(

        (420,750),
        (0,0), ConditionSwitch(

            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Emma_Doggy_Boob_Fuck2",
                    "action_speed > 1", "Emma_Doggy_Boob_Fuck",
                    "action_speed ", "Emma_Doggy_Boob",
                    "True", "Emma_Doggy_Boob",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Emma_Doggy_Boob_Fuck2",
                    "action_speed > 1", "Emma_Doggy_Boob_Fuck",
                    "True", "Emma_Doggy_Boob",
                    ),
            "True", "Emma_Doggy_Boob",
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite", "Emma_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Emma_Doggy_Fuck2_Top",
                    "action_speed > 1", "Emma_Doggy_Fuck_Top",
                    "action_speed ", "Emma_Doggy_Anal_Head_Top",
                    "True", "Emma_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Emma_Doggy_Fuck2_Top",
                    "action_speed > 1", "Emma_Doggy_Fuck_Top",
                    "True", "Emma_Doggy_Body",
                    ),
            "True", "Emma_Doggy_Body",
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite", "Emma_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Emma_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Emma_Doggy_Fuck_Ass",
                    "action_speed ", "Emma_Doggy_Anal_Head_Ass",
                    "True", "Emma_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Emma_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Emma_Doggy_Fuck_Ass",
                    "True", "Emma_Doggy_Ass",
                    ),
            "True", "Emma_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(

            "Player.Cock == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Emma_Doggy_Feet2",
                    "action_speed ", "Emma_Doggy_Feet1",
                    "True", "Emma_Doggy_Feet0",
                    ),
            "not Player.Sprite and ShowFeet", "Emma_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)



image Emma_Doggy_Body:
    LiveComposite(

        (420,750),


        (-12,0), "Emma_Doggy_Head",
        (0,0), "images/EmmaDoggy/Emma_Doggy_Body.png",
        (0,0), ConditionSwitch(

            "EmmaX.neck == 'choker'", "images/EmmaDoggy/Emma_Doggy_Choker.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "EmmaX.arms", "images/EmmaDoggy/Emma_Doggy_Gloves.png",
            "True",  Null(),
            ),

        (0,0), ConditionSwitch(

            "EmmaX.top == 'jacket'", Null(),








            "EmmaX.bra == 'corset'", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Sleave.png",
            "EmmaX.bra == 'lace_bra'", "images/EmmaDoggy/Emma_Doggy_Bra_Corset.png",
            "EmmaX.bra == 'sports_bra'", "images/EmmaDoggy/Emma_Doggy_Bra_Sport.png",
            "EmmaX.bra == 'bikini_top'", "images/EmmaDoggy/Emma_Doggy_Bra_Bikini.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Wet_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs == 'dress'", "images/EmmaDoggy/Emma_Doggy_Over_Dress_Under.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.top == 'dress'", "images/EmmaDoggy/Emma_Doggy_Over_Dress.png",
            "EmmaX.top == 'jacket'", "images/EmmaDoggy/Emma_Doggy_Over_Jacket.png",
            "EmmaX.top == 'nighty' and EmmaX.Uptop", "images/EmmaDoggy/Emma_Doggy_Over_Nighty_Down.png",
            "EmmaX.top == 'nighty'", "images/EmmaDoggy/Emma_Doggy_Over_Nighty.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "'back' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "primary_action == 'fondle_breasts' or offhand_action == 'fondle_breasts'", "Emma_Doggy_GropeBreast",
            "True", Null()
            ),
        (-12,0), "Emma_Doggy_Hair_Over",


        )


    offset (0,0)



image Emma_Doggy_Head:
    LiveComposite(

        (420,750),

        (0,0), ConditionSwitch(

                "EmmaX.Water or EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet'", "images/EmmaDoggy/Emma_Doggy_Hair_Wet_Back.png",
                "True", "images/EmmaDoggy/Emma_Doggy_Hair_Long_Back.png",
            ),
        (0,0), ConditionSwitch(


            "EmmaX.blushing", "images/EmmaDoggy/Emma_Doggy_Head_Blush.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.mouth == 'lipbite'", "images/EmmaDoggy/Emma_Doggy_Mouth_Lipbite.png",
            "EmmaX.mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Mouth_Tongue.png",
            "EmmaX.mouth == 'kiss'", "images/EmmaDoggy/Emma_Doggy_Mouth_Kiss.png",
            "EmmaX.mouth == 'sad'", "images/EmmaDoggy/Emma_Doggy_Mouth_Sad.png",
            "EmmaX.mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png",
            "EmmaX.mouth == 'grimace'", "images/EmmaDoggy/Emma_Doggy_Mouth_Smile.png",
            "EmmaX.mouth == 'smirk'", "images/EmmaDoggy/Emma_Doggy_Mouth_Smirk.png",
            "EmmaX.mouth == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Mouth_Kiss.png",
            "EmmaX.mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Mouth_Tongue.png",
            "EmmaX.mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_Mouth_Tongue.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Mouth_Normal.png",
            ),





        (0,0), ConditionSwitch(

            "'mouth' not in EmmaX.Spunk", Null(),



            "EmmaX.mouth == 'smile'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Smile.png",
            "EmmaX.mouth == 'grimace'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Smile.png",
            "EmmaX.mouth == 'sucking'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Tongue.png",


            "EmmaX.mouth == 'tongue'", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Tongue.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(


            "EmmaX.brows == 'angry'", "images/EmmaDoggy/Emma_Doggy_Brows_Angry.png",
            "EmmaX.brows == 'sad'", "images/EmmaDoggy/Emma_Doggy_Brows_Sad.png",
            "EmmaX.brows == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Brows_Surprised.png",

            "True", "images/EmmaDoggy/Emma_Doggy_Brows_Normal.png",
            ),
        (0,0), "Emma Doggy Blink",





        (0,0), ConditionSwitch(

            "EmmaX.Water or EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet'", "images/EmmaDoggy/Emma_Doggy_Hair_Wet.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Hair_Long.png",
            ),












        )
    zoom 0.83










image Emma_Doggy_Hair_Over:

    contains:
        ConditionSwitch(
                    "EmmaX.Water or EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet'", "images/EmmaDoggy/Emma_Doggy_Hair_Wet.png",
                    "True", "images/EmmaDoggy/Emma_Doggy_Hair_Long.png",
                    )
    contains:
        ConditionSwitch(

                "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Head_Wet.png",
                "True", Null(),
                ),
    contains:
        ConditionSwitch(

                "'hair' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Hair.png",
                "'facial' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Head_Spunk_Facial.png",
                "True", Null(),
                )
    contains:
        ConditionSwitch(

                "EmmaX.hair == 'hat wet' or (EmmaX.hair == 'hat' and EmmaX.Water)", "images/EmmaDoggy/Emma_Doggy_Hair_Wet_Shadow.png",
                "EmmaX.hair == 'hat'", "images/EmmaDoggy/Emma_Doggy_Hair_Long_Shadow.png",
                "True", Null(),
                )
    contains:
        ConditionSwitch(

                "EmmaX.hair == 'hat wet' or EmmaX.hair == 'hat'", "Emma_Doggy_Hat",
                "True", Null(),
                )
    zoom 0.83


image Emma_Doggy_Hat:


    "images/EmmaSprite/EmmaSprite_Hat.png"
    xzoom -0.6
    yzoom 0.6

    anchor (0.50,0.65)
    offset (235,300)

    rotate 10


image Emma Doggy Blink:

    ConditionSwitch(
        "EmmaX.eyes == 'sexy'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",
        "EmmaX.eyes == 'side'", "images/EmmaDoggy/Emma_Doggy_Eyes_Side.png",

        "EmmaX.eyes == 'closed'", "images/EmmaDoggy/Emma_Doggy_Eyes_Closed.png",

        "EmmaX.eyes == 'down'", "images/EmmaDoggy/Emma_Doggy_Eyes_Down.png",
        "EmmaX.eyes == 'stunned'", "images/EmmaDoggy/Emma_Doggy_Eyes_Stunned.png",
        "EmmaX.eyes == 'surprised'", "images/EmmaDoggy/Emma_Doggy_Eyes_Surprised.png",
        "EmmaX.eyes == 'squint'", "images/EmmaDoggy/Emma_Doggy_Eyes_Sexy.png",
        "True", "images/EmmaDoggy/Emma_Doggy_Eyes_Normal.png",
        ),






    3

    "images/EmmaDoggy/Emma_Doggy_Eyes_Closed.png"
    .25
    repeat

image Emma_Doggy_Ass:
    LiveComposite(

        (420,750),

        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(


                    "action_speed ", "images/EmmaDoggy/Emma_Doggy_Ass_Base.png",
                    "True", "images/EmmaDoggy/Emma_Doggy_Ass_Base.png",
                    ),
            "primary_action == 'eat_pussy'", "images/EmmaDoggy/Emma_Doggy_Ass_Open.png",
            "EmmaX.legs and not EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Ass_Closed.png",
            "EmmaX.underwear and not EmmaX.underwearDown", "images/EmmaDoggy/Emma_Doggy_Ass_Closed.png",
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "images/EmmaDoggy/Emma_Doggy_Ass_Base.png",
            "primary_action == 'dildo_pussy'", "images/EmmaDoggy/Emma_Doggy_Ass_Base.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Ass_Closed.png",
            ),


        (0,0), ConditionSwitch(

            "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Wet_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.hose == 'stockings'", "images/EmmaDoggy/Emma_Doggy_Hose_Stockings.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.underwearDown or (EmmaX.legs and EmmaX.legs != 'skirt' and not EmmaX.Upskirt)", Null(),
            "EmmaX.underwear == 'sports_panties'", "images/EmmaDoggy/Emma_Doggy_Panties_Sport_Down.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaDoggy/Emma_Doggy_Panties_Bikini_Down.png",
            "EmmaX.underwear == 'lace_panties'","images/EmmaDoggy/Emma_Doggy_Panties_Lace_Down.png",
            "EmmaX.underwear","images/EmmaDoggy/Emma_Doggy_Panties_White_Down.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(

            "EmmaX.legs == 'pants' and EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_Pants_Down.png",
            "EmmaX.legs == 'yoga_pants' and EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_Yoga_Down.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs and EmmaX.legs != 'skirt' and EmmaX.Upskirt",Null(),
            "EmmaX.accessory == 'thigh boots'", "images/EmmaDoggy/Emma_Doggy_Boots.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Emma_Pussy_Fucking3",
                    "action_speed > 1", "Emma_Pussy_Fucking2",
                    "action_speed ", "Emma_Pussy_Heading",
                    "True", "Emma_Pussy_Static",
                    ),



            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'", "Emma_Pussy_Fingering",
            "primary_action == 'dildo_pussy'", "Emma_Pussy_Fucking2",
            "True",Null(),

            ),

        (0,0), ConditionSwitch(

            "'in' in EmmaX.Spunk and Player.Cock == 'in'",Null(),
            "'in' in EmmaX.Spunk ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "EmmaX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "EmmaX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "not EmmaX.pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "(EmmaX.legs and EmmaX.legs != 'skirt') and not EmmaX.Upskirt", Null(),
            "EmmaX.underwearDown and primary_action == 'eat_pussy'", "images/EmmaDoggy/Emma_Doggy_Pubes_Open.png",
            "EmmaX.underwear and EmmaX.underwearDown", "images/EmmaDoggy/Emma_Doggy_Pubes_Closed.png",
            "EmmaX.underwear", "images/EmmaDoggy/Emma_Doggy_Pubes_ClosedC.png",
            "EmmaX.hose == 'pantyhose' and primary_action == 'eat_pussy'", "images/EmmaDoggy/Emma_Doggy_Pubes_OpenC.png",
            "EmmaX.hose == 'pantyhose'", "images/EmmaDoggy/Emma_Doggy_Pubes_ClosedC.png",
            "primary_action == 'eat_pussy'", "images/EmmaDoggy/Emma_Doggy_Pubes_Open.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Pubes_Closed.png",
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "EmmaX.piercings == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_Barbell.png",
            "EmmaX.piercings == 'ring' and EmmaX.underwear and not EmmaX.underwearDown", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC2.png",
            "EmmaX.piercings == 'ring' and EmmaX.hose == 'pantyhose' and not (EmmaX.underwear and EmmaX.underwearDown)", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC2.png",
            "EmmaX.piercings == 'ring' and EmmaX.legs and EmmaX.legs != 'skirt' and not EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC2.png",
            "EmmaX.piercings == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Emma_Anal_Fucking2",
                    "action_speed > 1", "Emma_Anal_Fucking",
                    "action_speed ", "Emma_Anal_Heading",
                    "True", "Emma_Anal",
                    ),




            "primary_action == 'finger_ass' or offhand_action == 'finger_ass'", "Emma_Anal_Fingering",
            "primary_action == 'dildo_anal'", "Emma_Anal_Fucking",


            "True", Null(),
            ),









        (0,0), ConditionSwitch(

            "EmmaX.underwearDown or not EmmaX.underwear", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),


            "EmmaX.underwear == 'sports_panties' and EmmaX.Wet", "images/EmmaDoggy/Emma_Doggy_Panties_Sport_Wet.png",
            "EmmaX.underwear == 'sports_panties'", "images/EmmaDoggy/Emma_Doggy_Panties_Sport.png",
            "EmmaX.underwear == 'lace_panties'", "images/EmmaDoggy/Emma_Doggy_Panties_Lace.png",
            "EmmaX.underwear == 'bikini_bottoms'", "images/EmmaDoggy/Emma_Doggy_Panties_Bikini.png",
            "EmmaX.Wet", "images/EmmaDoggy/Emma_Doggy_Panties_White_Wet.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Panties_White.png",
            ),
        (0,0), ConditionSwitch(

            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_Pantyhose.png",
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "Player.Sprite", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "not EmmaX.underwear and EmmaX.hose != 'pantyhose'", Null(),
            "((EmmaX.underwear or EmmaX.hose == 'pantyhose') and EmmaX.underwearDown)", Null(),

            "EmmaX.piercings == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellC.png",
            "EmmaX.piercings == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs == 'pants'", ConditionSwitch(
                    "EmmaX.Upskirt", Null(),
                    "EmmaX.Wet > 1", "images/EmmaDoggy/Emma_Doggy_Legs_Pants_Wet.png",
                    "True", "images/EmmaDoggy/Emma_Doggy_Legs_Pants.png",
                    ),
            "EmmaX.legs == 'yoga_pants'", ConditionSwitch(
                    "EmmaX.Upskirt", Null(),
                    "EmmaX.Wet > 1", "images/EmmaDoggy/Emma_Doggy_Legs_Yoga_Wet.png",
                    "True", "images/EmmaDoggy/Emma_Doggy_Legs_Yoga.png",
                    ),
            "EmmaX.legs == 'dress'", ConditionSwitch(
                    "EmmaX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/EmmaDoggy/Emma_Doggy_Legs_Dress_Up.png",
                    "EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_Dress_Up.png",
                    "True", "images/EmmaDoggy/Emma_Doggy_Legs_Dress.png",
                    ),
            "EmmaX.legs == 'skirt'", ConditionSwitch(
                    "EmmaX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/EmmaDoggy/Emma_Doggy_Legs_Skirt_Up.png",
                    "EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_Skirt_Up.png",
                    "True", "images/EmmaDoggy/Emma_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "Player.Sprite", Null(),
            "primary_action == 'fondle_pussy' or offhand_action == 'fondle_pussy'",Null(),
            "primary_action == 'dildo_pussy'", Null(),
            "not EmmaX.legs", Null(),
            "EmmaX.legs and EmmaX.legs != 'skirt' and EmmaX.Upskirt", Null(),

            "EmmaX.piercings == 'barbell'", "images/EmmaDoggy/Emma_Doggy_Pierce_BarbellC.png",
            "EmmaX.piercings == 'ring'", "images/EmmaDoggy/Emma_Doggy_Pierce_RingC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.legs and EmmaX.legs != 'skirt' and EmmaX.Upskirt",Null(),
            "Player.Cock == 'in' or Player.Cock == 'anal'",Null(),
            "EmmaX.accessory == 'thigh boots'", "images/EmmaDoggy/Emma_Doggy_Boots.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.top == 'nighty' and EmmaX.Upskirt", "images/EmmaDoggy/Emma_Doggy_Legs_Nighty_Up.png",
            "EmmaX.top == 'nighty'", "images/EmmaDoggy/Emma_Doggy_Legs_Nighty.png",
            "True", Null(),
            ),






        (0,0), ConditionSwitch(

            "'back' in EmmaX.Spunk", "images/EmmaDoggy/Emma_Doggy_Spunk_Ass.png",
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

            "True", "images/KittyDoggy/Kitty_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(

            "not Player.Sprite or Player.Cock != 'out'", Null(),


            "action_speed ", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),






        )


image Emma_Doggy_Feet:
    contains:
        AlphaMask("Emma_Doggy_Shins", "images/EmmaDoggy/Emma_Doggy_Feet_Mask.png")

image Emma_Doggy_Shins:

    contains:

        ConditionSwitch(
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Feet_StockingsHoled.png",
            "EmmaX.hose and EmmaX.hose != 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Feet_Stockings.png",
            "True", "images/EmmaDoggy/Emma_Doggy_Feet.png"
            )
    contains:

        ConditionSwitch(
            "EmmaX.legs == 'pants'", "images/EmmaDoggy/Emma_Doggy_Feet_Pants.png",
            "EmmaX.legs == 'yoga_pants'", "images/EmmaDoggy/Emma_Doggy_Feet_YogaPants.png",
            "True", Null(),
            )

image Emma_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (110,420)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10
            ease 1 rotate 0
            repeat

image Emma_Doggy_Boob:
    contains:
        "images/EmmaDoggy/Emma_Doggy_Boob.png"
    contains:


        ConditionSwitch(
            "EmmaX.Uptop", ConditionSwitch(


                    "EmmaX.bra == 'sports_bra'", "images/EmmaDoggy/Emma_Doggy_Bra_Sport_Boob_Down.png",

                    "EmmaX.bra", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob_Down.png",
                    "True", Null(),
                    ),
            "EmmaX.top == 'jacket'", Null(),
            "EmmaX.bra == 'corset'", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob.png",
            "EmmaX.bra == 'lace_bra'", "images/EmmaDoggy/Emma_Doggy_Bra_Lace_Boob.png",
            "EmmaX.bra == 'sports_bra'", "images/EmmaDoggy/Emma_Doggy_Bra_Sport_Boob.png",
            "EmmaX.bra == 'bikini_top'", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "EmmaX.Water", "images/EmmaDoggy/Emma_Doggy_Wet_Boob.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "not EmmaX.top", Null(),
            "EmmaX.top == 'dress' and EmmaX.Uptop", "images/EmmaDoggy/Emma_Doggy_Over_Dress_Boob_Down.png",
            "EmmaX.top == 'dress'", "images/EmmaDoggy/Emma_Doggy_Over_Dress_Boob.png",
            "EmmaX.top == 'jacket' and EmmaX.Uptop", Null(),
            "EmmaX.top == 'jacket'", "images/EmmaDoggy/Emma_Doggy_Over_Jacket_Boob.png",
            "EmmaX.top == 'nighty' and EmmaX.Uptop", "images/EmmaDoggy/Emma_Doggy_Bra_Corset_Boob_Down.png",
            "EmmaX.top == 'nighty'", "images/EmmaDoggy/Emma_Doggy_Over_Nighty_Boob.png",
            "True", Null(),
            )



image Emma_Doggy_Boob_Fuck:

    contains:
        subpixel True
        "Emma_Doggy_Boob"
        ypos 0
        pause .4
        block:
            pause .05
            ease .25 ypos -20
            pause .2
            ease .3 ypos -5
            ease .2 ypos -10
            easein 1.5 ypos 0
            repeat






image Emma_Doggy_Boob_Fuck2:

    contains:
        subpixel True
        "Emma_Doggy_Boob"
        ypos 0
        block:
            pause .15
            ease .1 ypos -30
            pause .1
            ease .55 ypos 5

            repeat




image Zero_Emma_Hotdog_Static:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Emma_Hotdog_Moving:


    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat


image Emma_Pussy_Static:

    subpixel True
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom .8
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_Heading.png"
        subpixel True
        anchor (0.52,0.69)
        pos (220,518)
        xzoom .9
        block:
            ease 1 xzoom 1.1
            pause 1
            ease 3 xzoom .9
            repeat
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (218,540)
        xzoom .1
        yzoom .8
        parallel:
            ease 1 xzoom .6
            pause 1
            ease 3 xzoom .1
            repeat
        parallel:
            ease 1 yzoom .6
            pause 1
            ease 3 yzoom .8
            repeat
        parallel:
            ease 1 ypos 533
            pause 1
            ease 3 ypos 540
            repeat
    contains:
        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Emma_Doggy_Static", "Emma_Pussy_Mask_Static")

image Zero_Emma_Doggy_Static:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (173,550)
        block:
            ease 1 ypos 540
            pause 1
            ease 3 ypos 550
            repeat

image Emma_Pussy_Mask_Static:


    contains:

        subpixel True

        "images/EmmaDoggy/Emma_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (220,525)
        xzoom 1
        parallel:
            ease .9 ypos 526
            pause 2.1
            ease 2 ypos 525
            repeat





image Emma_Pussy_Heading:

    subpixel True
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (220,518)
        xzoom .6
        block:
            ease .9 xzoom 1
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Emma_Doggy_Heading", "Emma_Pussy_Mask")

image Zero_Emma_Doggy_Heading:

    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:

            ease 1 ypos 500
            pause 1
            ease 3 ypos 545
            repeat

image Emma_Pussy_Mask:


    contains:



        "images/EmmaDoggy/Emma_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom .8
        parallel:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .8
            repeat
        parallel:
            ease 1 ypos 520
            pause 1
            ease 3 ypos 528
            repeat


image Emma_Pussy_Fingering:

    subpixel True
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (220,518)
        xzoom .6
        block:
            ease .9 xzoom .85
            pause 1.6
            ease 2.5 xzoom .6
            repeat
    contains:
        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            ),
    contains:

        AlphaMask("Zero_Pussy_Finger", "Emma_Pussy_Mask_Finger")
        xoffset 3




image Emma_Pussy_Mask_Finger:


    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_MaskHeading.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom .8
        parallel:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .8
            repeat
        parallel:
            ease 1 ypos 518
            pause 1
            ease 3 ypos 528
            repeat



image Emma_Pussy_Fucking2:

    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png"
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(
            "primary_action == 'dildo_pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Emma_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),


image Zero_Emma_Doggy_Fucking2:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat


image Emma_Pussy_Fucking3:

    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FBase.png"
    contains:

        "images/EmmaDoggy/Emma_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Emma_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")

image Zero_Emma_Doggy_Fucking3:

    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat




image Emma_Anal:







    contains:
        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        "Zero_Doggy_Insert"
        pos (172,500)

image Emma_Anal_Fingering:

    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png"
    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png"
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

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",

            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")


image Emma_Anal_Heading:

    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png"
    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png"
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

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Emma_Doggy_Anal_Heading", "Zero_Emma_Doggy_Anal_HeadingJunk")
    contains:

        AlphaMask("Zero_Emma_Doggy_Anal_Heading", "Emma_Doggy_Anal_Heading_Mask")

image Zero_Emma_Doggy_Anal_Heading:

    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Emma_Doggy_Anal_HeadingJunk:

    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600
            repeat

image Emma_Doggy_Anal_Heading_Mask:

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

image Emma_Doggy_Anal_Head_Top:

    contains:
        subpixel True
        "Emma_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Emma_Doggy_Anal_Head_Ass:

    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat


image Zero_Emma_Doggy_Anal1:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Emma_Anal_Fucking:

    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png"
    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            pause .25
            ease .25 zoom 1
            pause .75
            ease 1 zoom .95
            pause .25
            repeat
    contains:
        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        ConditionSwitch(

            "primary_action == 'dildo_anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Emma_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),


image Emma_Doggy_Anal_FullMask:
    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png"
    contains:



        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )

image Emma_Doggy_Fuck_Top:

    contains:
        subpixel True
        "Emma_Doggy_Body"
        ypos 0
        pause .4
        block:
            ease .2 ypos -10
            pause .3
            ease 2 ypos 0
            repeat

image Emma_Doggy_Fuck_Ass:

    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15
            ease .1 ypos -5
            pause .2
            ease 1.6 ypos 0
            repeat



image Zero_Emma_Doggy_Anal2:

    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Emma_Anal_Fucking2:

    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullBase.png"
    contains:

        "images/EmmaDoggy/Emma_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .5
        block:
            pause .1
            ease .1 zoom 1
            pause .3
            ease .3 zoom .95
            pause .1
            repeat
    contains:






        ConditionSwitch(

            "EmmaX.hose == 'garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_Garter.png",
            "EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaDoggy/Emma_Doggy_Hose_StockingGarter.png",
            "EmmaX.underwear and EmmaX.underwearDown", Null(),
            "EmmaX.hose == 'ripped_pantyhose'", "images/EmmaDoggy/Emma_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:

        AlphaMask("Zero_Emma_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Emma_Doggy_Fuck2_Top:

    contains:
        subpixel True
        "Emma_Doggy_Body"
        ypos 0
        block:
            pause .15
            ease .1 ypos -20
            pause .1
            easein .5 ypos 0
            pause .05
            repeat

image Emma_Doggy_Fuck2_Ass:

    contains:
        subpixel True
        "Emma_Doggy_Ass"
        ypos 5
        block:
            pause .15
            ease .1 ypos -25
            ease .1 ypos -15
            pause .1
            ease .4 ypos 5
            pause .05
            repeat




image Emma_Doggy_Feet0:

    contains:
        "Emma_Doggy_Shins"
        pos (0, -20)
        block:
            subpixel True
            pause .5
            ease 2 ypos 0
            pause .5
            ease 2 ypos -20
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (158,520)
    contains:
        "Emma_Doggy_Feet"
        pos (0, -20)
        block:
            subpixel True
            pause .5
            ease 2 ypos 0
            pause .5
            ease 2 ypos -20
            repeat

image Emma_Doggy_Feet1:

    contains:
        "Emma_Doggy_Shins"
        pos (0, -20)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (158,520)
        block:
            pause .4
            ease 1.7 ypos 540
            ease .9 ypos 520
            repeat
    contains:
        "Emma_Doggy_Feet"
        pos (0, -20)
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat

image Emma_Doggy_Feet2:

    contains:
        "Emma_Doggy_Shins"
        pos (0, -20)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (158,520)
        block:
            pause .07
            ease .6 ypos 540
            ease .28 ypos 520
            repeat
    contains:
        "Emma_Doggy_Feet"
        pos (0, -20)
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
            repeat




label Emma_Doggy_Launch(Line=primary_action):
    if renpy.showing("Emma_Doggy_Animation"):
        return
    $ action_speed = 0
    call Emma_Hide (1)
    show Emma_Doggy_Animation zorder 150 at sprite_location(stage_center+50)
    with dissolve
    return

label Emma_Doggy_Reset:
    if not renpy.showing("Emma_Doggy_Animation"):
        return

    $ EmmaX.ArmPose = 2
    $ EmmaX.SpriteVer = 0
    hide Emma_Doggy_Animation
    call Emma_Hide
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        zoom 1
        offset (0,0)
        anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return














image Emma_TJ_Animation:

    contains:
        ConditionSwitch(

            "Player.Sprite", ConditionSwitch(

                    "action_speed == 1", "Emma_TJ_Body_1",
                    "action_speed == 2", "Emma_TJ_Body_2",
                    "action_speed == 3", "Emma_TJ_Body_3",
                    "action_speed == 5", "Emma_TJ_Body_5",
                    "True",       "Emma_TJ_Body_0",
                    ),
            "True","Emma_TJ_Body_0",
            )
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)

image Emma_TJ_Tits:

    contains:

        ConditionSwitch(
            "EmmaX.arms or EmmaX.top == 'jacket' or EmmaX.top == 'dress'", "images/EmmaSex/Emma_Sex_Forearms_W.png",
            "True", "images/EmmaSex/Emma_Sex_Forearms.png",
            )
        zoom 0.9
    contains:

        ConditionSwitch(
            "EmmaX.arms", "images/EmmaSex/Emma_Sex_Tits_TJ_Gloved.png",
            "True", "images/EmmaSex/Emma_Sex_Tits_TJ.png",
            )
        zoom 0.9
    contains:

        ConditionSwitch(
            "not EmmaX.piercings", Null(),
            "EmmaX.piercings == 'barbell'", ConditionSwitch(


                    "True", "images/EmmaSex/Emma_Pierce_Barbell_Tits_T.png",
                    ),
            "EmmaX.piercings == 'ring'", ConditionSwitch(


                    "True", "images/EmmaSex/Emma_Pierce_Ring_Tits_T.png",
                    ),
            "True", Null(),
            )
        zoom 0.9
    contains:

        ConditionSwitch(
            "not EmmaX.bra", Null(),
            "EmmaX.bra == 'sports_bra' and EmmaX.Uptop", "images/EmmaSex/Emma_Sex_Bra_Sports_TJ_Uptop.png",
            "EmmaX.bra == 'sports_bra'", "images/EmmaSex/Emma_Sex_Bra_Sports_TJ.png",
            "EmmaX.Uptop", Null(),
            "EmmaX.bra == 'bikini_top'", "images/EmmaSex/Emma_Sex_Bra_Bikini_TJ.png",
            "EmmaX.bra == 'lace_bra'", "images/EmmaSex/Emma_Sex_Bra_Lace_TJ.png",

            "True", Null(),
            )
        zoom 0.9
    contains:

        ConditionSwitch(
            "not EmmaX.piercings or not EmmaX.bra", Null(),
            "EmmaX.piercings == 'barbell'", ConditionSwitch(

                    "EmmaX.bra in ('corset', 'lace_bra', 'sports_bra')", "images/EmmaSex/Emma_Pierce_Barbell_Tits_TC.png",
                    "True", Null(),
                    ),
            "EmmaX.piercings == 'ring'", ConditionSwitch(

                    "EmmaX.bra in ('corset', 'lace_bra', 'sports_bra')", "images/EmmaSex/Emma_Pierce_Ring_Tits_TC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
        zoom 0.9
    contains:

        ConditionSwitch(
                "'tits' in EmmaX.Spunk", "images/EmmaSex/Emma_Spunk_Titjob_Over.png",
                "True", Null(),
                )
        zoom 0.9
    offset (50,50)
















image Emma_TJ_Body_0:

    contains:

        "Emma_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        "Emma_Sex_Torso"
        pos (0,0)
        subpixel True
        block:
            ease 2 ypos -5
            ease 2 ypos 5
            repeat
    contains:


        "Emma_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,260)
        subpixel True
        block:
            ease 2.4 ypos 250
            ease 1.6 ypos 260
            repeat
    contains:

        ConditionSwitch(
                "Player.Sprite", "Blowcock",
                "True", Null(),
                )
        subpixel True
        pos (640,150)
        anchor (0.5,0.5)
        zoom 0.4
        rotate -3
        parallel:
            pause 0.1
            ease 1.6 ypos 170
            pause 0.1
            ease 1.4 ypos 150
            repeat
        parallel:
            pause 0.1
            ease 1.6 rotate 4
            pause 0.1
            ease 1.4 rotate -3
            repeat
    contains:

        "Emma_TJ_Tits"
        pos (290,270)
        rotate -3
        subpixel True
        size (1000,1000)
        anchor (500,500)
        parallel:
            ease 1.5 rotate 4
            pause 0.1
            ease 1.5 rotate -3
            pause 0.1
            repeat



image Emma_TJ_Body_1:

    contains:

        "Emma_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,250)
        subpixel True
        block:
            pause 0.2
            ease 1.4 ypos 240
            pause 0.3
            ease 0.6 ypos 250
            repeat
    contains:

        "Emma_Sex_Torso"
        pos (0,0)
        subpixel True
        block:
            pause 0.2
            ease 1.4 ypos -20
            pause 0.3
            ease 0.6 ypos 0
            repeat
    contains:

        "Blowcock"
        subpixel True
        pos (640,150)

        anchor (0.5,0.5)
        zoom 0.4
        block:
            pause 0.2
            ease 1.4 ypos 140
            pause 0.3
            ease 0.6 ypos 150
            repeat
    contains:

        "Emma_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,250)
        subpixel True
        block:
            pause 0.2
            ease 1.4 ypos 240
            pause 0.3
            ease 0.6 ypos 250
            repeat
    contains:

        "Emma_TJ_Tits"
        pos (290,290)
        rotate 0
        subpixel True
        size (1000,1000)
        anchor (500,500)
        parallel:
            ease 1.5 ypos 230
            pause 0.3
            ease 0.7 ypos 290
            repeat









image Emma_TJ_Body_2:

    contains:

        "Emma_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,250)
        subpixel True
        block:
            pause 0.1
            ease .6 ypos 250
            ease .3 ypos 270
            repeat
    contains:

        "Emma_Sex_Torso"
        pos (0,0)
        subpixel True
        block:
            pause .1
            ease .5 ypos -20
            ease .3 ypos 15
            pause .1
            repeat
    contains:

        "Blowcock"
        subpixel True
        pos (640,150)

        anchor (0.5,0.5)
        zoom 0.4
        block:
            pause .05
            ease .65 ypos 140
            ease .3 ypos 150
            repeat
    contains:

        "Emma_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (505,250)
        subpixel True
        block:
            pause 0.1
            ease .6 ypos 250
            ease 0.3 ypos 270
            repeat
    contains:

        "Emma_TJ_Tits"
        pos (290,290)
        rotate 0
        subpixel True
        size (1000,1000)
        anchor (500,500)
        parallel:
            ease .6 ypos 220
            ease .3 ypos 300
            pause .1
            repeat


image Emma_TJ_Body_3:

    contains:

        "Emma_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,290)
        subpixel True
        block:
            ease 1.5 ypos 260
            pause .7
            ease .3 ypos 290
            pause .5
            repeat
    contains:

        "Emma_Sex_Torso"
        pos (0,0)
        subpixel True
        block:
            ease 1.6 ypos -20
            pause .7
            ease .2 ypos 0
            pause .5
            repeat
    contains:

        "Emma_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,290)
        subpixel True
        block:
            ease 1.5 ypos 260
            pause .7
            ease .3 ypos 290
            pause .5
            repeat
    contains:

        "Blowcock"
        subpixel True
        pos (640,130)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            pause .2
            ease 1.6 ypos 120
            pause .4
            ease .3 ypos 130
            pause .5
            repeat
    contains:

        "Emma_TJ_Tits"
        pos (290,290)
        rotate 0
        subpixel True
        size (1000,1000)
        anchor (500,500)
        parallel:
            ease 1.8 ypos 240
            pause .3
            ease .4 ypos 290
            pause .5
            repeat




image Emma_TJ_Body_5:

    contains:

        "Emma_BJ_HairBack"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,290)
        subpixel True
        block:
            ease 1.5 ypos 288
            pause .7
            ease .3 ypos 290
            pause .5
            repeat
    contains:

        "Emma_Sex_Torso"
        pos (0,0)
        subpixel True
        block:
            ease 1.3 ypos -5
            pause .7
            ease .5 ypos 0
            pause .5
            repeat
    contains:

        "Emma_BJ_Head"
        zoom 0.41
        anchor (0.5, 0.5)
        pos (500,290)
        subpixel True
        block:
            ease 1.5 ypos 288
            pause .7
            ease .3 ypos 290
            pause .5
            repeat
    contains:

        "Blowcock"
        subpixel True
        pos (640,130)
        anchor (0.5,0.5)
        zoom 0.4
        block:
            pause .2
            ease 1.6 ypos 128
            pause .4
            ease .3 ypos 130
            pause .5
            repeat
    contains:

        "Emma_TJ_Tits"
        pos (290,290)
        rotate 0
        subpixel True
        size (1000,1000)
        anchor (500,500)
        parallel:
            ease 1.3 ypos 270
            pause .3
            ease .9 ypos 290
            pause .5
            repeat



label Emma_TJ_Launch(Line=primary_action):
    if renpy.showing("Emma_TJ_Animation"):
        return
    call Emma_Hide
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        ease 1 zoom 2 xpos 550 yoffset 50
    if Taboo:
        if len(Present) >= 2:
            if Present[0] != EmmaX:
                "[EmmaX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != EmmaX:
                "[EmmaX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[EmmaX.name] looks around to see if anyone can see her."









    $ EmmaX.ArmPose = 0

    call Emma_First_Topless

    if not EmmaX.action_counter["titjob"] and Line == "L":
        if not EmmaX.bra and not EmmaX.top:
            "As you pull out your cock, [EmmaX.name] cautiously places it between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.bra and not EmmaX.top:
            "As you pull out your cock, [EmmaX.name] cautiously places it under her [EmmaX.bra], between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.bra and EmmaX.top:
            "As you pull out your cock, [EmmaX.name] cautiously places it under her [EmmaX.top], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [EmmaX.name] cautiously places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L":
        if not EmmaX.bra and not EmmaX.top:
            "As you pull out your cock, [EmmaX.name] places it between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.bra and not EmmaX.top:
            "As you pull out your cock, [EmmaX.name] places it under her [EmmaX.bra], between her breasts and starts to rub them up and down the shaft."
        elif EmmaX.bra and EmmaX.top:
            "As you pull out your cock, [EmmaX.name] places it under her [EmmaX.top], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [EmmaX.name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
        "[EmmaX.name] wraps her tits around your cock."

    show blackscreen onlayer black with dissolve
    show Emma_Sprite zorder EmmaX.sprite_layer:
        alpha 0
    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "titjob"
    show Emma_TJ_Animation zorder 150
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Emma_TJ_Reset:
    if not renpy.showing("Emma_TJ_Animation"):
        return

    call Emma_Hide
    $ Player.Sprite = 0

    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        zoom 2 xpos 550 yoffset 50
    show Emma_Sprite zorder EmmaX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 yoffset 50
        pause .5
        ease .5 zoom 1 xpos EmmaX.sprite_location yoffset 0
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos EmmaX.sprite_location

    "[EmmaX.name] pulls back"
    return












image Emma_BJ_Animation:
    LiveComposite(
        (858,928),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Emma_BJ_HairBack", Emma_BJ_Head_0()),
            "action_speed == 1", At("Emma_BJ_HairBack", Emma_BJ_Head_1()),
            "action_speed == 2", At("Emma_BJ_HairBack", Emma_BJ_Head_2()),
            "action_speed == 3", At("Emma_BJ_HairBack", Emma_BJ_Head_3()),
            "action_speed == 4", At("Emma_BJ_HairBack", Emma_BJ_Head_4()),
            "action_speed == 5", At("Emma_BJ_HairBack", Emma_BJ_Head_5()),
            "action_speed == 6", At("Emma_BJ_HairBack", Emma_BJ_Head_6()),
            "True", Null(),
            ),
        (-20,270), ConditionSwitch(

            "action_speed == 0", At("Emma_BJ_Backdrop", Emma_BJ_Body_0()),
            "action_speed == 1", At("Emma_BJ_Backdrop", Emma_BJ_Body_1()),
            "action_speed == 2", At("Emma_BJ_Backdrop", Emma_BJ_Body_2()),
            "action_speed == 3", At("Emma_BJ_Backdrop", Emma_BJ_Body_3()),
            "action_speed == 4", At("Emma_BJ_Backdrop", Emma_BJ_Body_4()),
            "action_speed == 5", At("Emma_BJ_Backdrop", Emma_BJ_Body_5()),
            "action_speed == 6", At("Emma_BJ_Backdrop", Emma_BJ_Body_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 0", At("Emma_BJ_Head", Emma_BJ_Head_0()),
            "action_speed == 1", At("Emma_BJ_Head", Emma_BJ_Head_1()),
            "action_speed == 2", At("Emma_BJ_Head", Emma_BJ_Head_2()),
            "action_speed == 3", At("Emma_BJ_Head", Emma_BJ_Head_3()),
            "action_speed == 4", At("Emma_BJ_Head", Emma_BJ_Head_4()),
            "action_speed == 5", At("Emma_BJ_Head", Emma_BJ_Head_5()),
            "action_speed == 6", At("Emma_BJ_Head", Emma_BJ_Head_6()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "action_speed == 0", At("Blowcock", Emma_BJ_Cock_0()),
            "action_speed == 1", At("Blowcock", Emma_BJ_Cock_1()),
            "action_speed >= 2", At("Blowcock", Emma_BJ_Cock_2()),



            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_3()),
            "action_speed == 4", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_4()),
            "action_speed == 6", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MouthSuckingMask"), Emma_BJ_Head_6()),
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(

            "action_speed == 2", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MaskHeadingComposite"), Emma_BJ_Head_2()),
            "action_speed == 5", At(AlphaMask("Emma_BJ_Head", "Emma_BJ_MaskHeadingComposite"), Emma_BJ_Head_5()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed < 3 or 'mouth' not in EmmaX.Spunk", Null(),
            "action_speed == 3", At("EmmaSuckingSpunk", Emma_BJ_Head_3()),
            "action_speed == 4", At("EmmaSuckingSpunk", Emma_BJ_Head_4()),
            "action_speed == 6", At("EmmaSuckingSpunk", Emma_BJ_Head_6()),
            "True", Null(),
            ),
        (325,490), ConditionSwitch(

            "action_speed == 2 and 'mouth' in EmmaX.Spunk", At("Emma_BJ_MaskHeadingSpunk", Emma_BJ_Head_2()),

            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Emma_BJ_HairBack:

    ConditionSwitch(
            "EmmaX.Water or EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet'", Null(),
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Back.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Emma_BJ_Backdrop:
    contains:

        ConditionSwitch(
                "'blanket' in EmmaX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),
        zoom 2
        anchor (.5,.5)
        pos (350,600)
    contains:

        "Emma_Sex_Torso"
        zoom 2.5
        anchor (.5,.5)
        pos (160,750)



image Emma_BJ_Head:
    LiveComposite(
        (858,928),
         (0,0), ConditionSwitch(

            "EmmaX.Water or EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet'", "images/EmmaBJFace/Emma_BJ_Hair_Wet_Mid.png",
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Mid.png",
            ),
        (0,0), ConditionSwitch(

            "action_speed <= 2 or action_speed == 5 or not renpy.showing('Emma_BJ_Animation')", ConditionSwitch(

                    "EmmaX.blushing", "images/EmmaBJFace/Emma_BJ_FaceClosed_Blush.png",
                    "True", "images/EmmaBJFace/Emma_BJ_FaceClosed.png",
                    ),
            "EmmaX.blushing", "images/EmmaBJFace/Emma_BJ_FaceOpen_Blush.png",
            "True", "images/EmmaBJFace/Emma_BJ_FaceOpen.png"
            ),
        (0,0), ConditionSwitch(






            "action_speed and renpy.showing('Emma_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/EmmaBJFace/Emma_BJ_Mouth_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png",
                    "action_speed == 4", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png",
                    "action_speed == 6", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png",
                    ),
            "action_speed == 3 and renpy.showing('Emma_TJ_Animation')", "images/EmmaBJFace/Emma_BJ_Mouth_Tongue.png",
            "EmmaX.mouth == 'normal'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            "EmmaX.mouth == 'lipbite'", "images/EmmaBJFace/Emma_BJ_Mouth_Lipbite.png",
            "EmmaX.mouth == 'sucking'", "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png",
            "EmmaX.mouth == 'kiss'", "images/EmmaBJFace/Emma_BJ_Mouth_Kiss.png",
            "EmmaX.mouth == 'sad'", "images/EmmaBJFace/Emma_BJ_Mouth_Sad.png",
            "EmmaX.mouth == 'smile'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            "EmmaX.mouth == 'smirk'", "images/EmmaBJFace/Emma_BJ_Mouth_Smirk.png",
            "EmmaX.mouth == 'grimace'", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            "EmmaX.mouth == 'surprised'", "images/EmmaBJFace/Emma_BJ_Mouth_Surprised.png",
            "EmmaX.mouth == 'tongue'", "images/EmmaBJFace/Emma_BJ_Mouth_Tongue.png",
            "True", "images/EmmaBJFace/Emma_BJ_Mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(


            "not renpy.showing('Emma_BJ_Animation')", Null(),
            "action_speed == 2", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnim()),
            "action_speed == 5", At("Emma_BJ_MouthHeading", Emma_BJ_MouthAnimC()),
            "True", Null(),
            ),

        (0,0), ConditionSwitch(

            "'mouth' not in EmmaX.Spunk", Null(),
            "action_speed and renpy.showing('Emma_BJ_Animation')", ConditionSwitch(

                    "action_speed == 1", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",
                    "(action_speed== 2 or action_speed == 5)", Null(),
                    "action_speed == 3", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 4", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png",
                    "action_speed == 6", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png",
                    ),
            "EmmaX.mouth == 'normal'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            "EmmaX.mouth == 'lipbite'", "images/EmmaBJFace/Emma_BJ_Spunk_Lipbite.png",
            "EmmaX.mouth == 'kiss'", "images/EmmaBJFace/Emma_BJ_Spunk_Kiss.png",
            "EmmaX.mouth == 'sad'", "images/EmmaBJFace/Emma_BJ_Spunk_Sad.png",
            "EmmaX.mouth == 'smile'", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            "EmmaX.mouth == 'smirk'", "images/EmmaBJFace/Emma_BJ_Spunk_Smirk.png",
            "EmmaX.mouth == 'surprised'", "images/EmmaBJFace/Emma_BJ_Spunk_Surprised.png",
            "EmmaX.mouth == 'tongue'", "images/EmmaBJFace/Emma_BJ_Spunk_Tongue.png",
            "EmmaX.mouth == 'sucking'", "images/EmmaBJFace/Emma_BJ_Spunk_SuckingUnder.png",
            "True", "images/EmmaBJFace/Emma_BJ_Spunk_Smile.png",
            ),
        (0,0), ConditionSwitch(

            "EmmaX.brows == 'normal'", "images/EmmaBJFace/Emma_BJ_Brows_Normal.png",
            "EmmaX.brows == 'angry'", "images/EmmaBJFace/Emma_BJ_Brows_Angry.png",
            "EmmaX.brows == 'sad'", "images/EmmaBJFace/Emma_BJ_Brows_Sad.png",
            "EmmaX.brows == 'surprised'", "images/EmmaBJFace/Emma_BJ_Brows_Surprised.png",
            "EmmaX.brows == 'confused'", "images/EmmaBJFace/Emma_BJ_Brows_Confused.png",
            "True", "images/EmmaBJFace/Emma_BJ_Brows_Normal.png",
            ),
        (0,0), "Emma BJ Blink",

        (0,0), ConditionSwitch(

            "'facial' in EmmaX.Spunk", "images/EmmaBJFace/Emma_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(

            "EmmaX.Water or EmmaX.hair == 'wet' or EmmaX.hair == 'hat wet'", "images/EmmaBJFace/Emma_BJ_Hair_Wet_Top.png",
            "True", "images/EmmaBJFace/Emma_BJ_Hair_Wave_Top.png",
            ),











        (-80,-95), ConditionSwitch(

            "EmmaX.hair == 'hat' or EmmaX.hair == 'hat wet'", "Emma_BJ_Hat",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Emma BJ Blink:

    ConditionSwitch(
            "EmmaX.eyes == 'normal'", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",
            "EmmaX.eyes == 'sexy'", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",
            "EmmaX.eyes == 'closed'", "images/EmmaBJFace/Emma_BJ_Eyes_Closed.png",
            "EmmaX.eyes == 'surprised'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "EmmaX.eyes == 'side'", "images/EmmaBJFace/Emma_BJ_Eyes_Side.png",
            "EmmaX.eyes == 'stunned'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "EmmaX.eyes == 'down'", "images/EmmaBJFace/Emma_BJ_Eyes_Down.png",
            "EmmaX.eyes == 'manic'", "images/EmmaBJFace/Emma_BJ_Eyes_Surprised.png",
            "EmmaX.eyes == 'squint'", "images/EmmaBJFace/Emma_BJ_Eyes_Squint.png",
            "True", "images/EmmaBJFace/Emma_BJ_Eyes_Sexy.png",
            ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/EmmaBJFace/Emma_BJ_Eyes_Closed.png"
    .25
    repeat

image Emma_BJ_Hat:


    "images/EmmaSprite/EmmaSprite_Hat.png"
    zoom 1.3
    anchor (0.50,0.65)

image Emma_BJ_MouthHeading:

    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)

image Emma_BJ_MouthSuckingMask:

    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_SuckingMask.png"
        zoom 1.4








image Emma_BJ_MaskHeading:

    contains:
        "images/EmmaBJFace/Emma_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Emma_BJ_MaskHeadingComposite:

    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "action_speed == 2", At("Emma_BJ_MaskHeading", Emma_BJ_MouthAnim()),
            "action_speed == 5", At("Emma_BJ_MaskHeading", Emma_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Emma_BJ_MaskHeadingSpunk:

    contains:

        "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png"
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


    zoom 2.5
    yoffset 210

image EmmaSuckingSpunk:
    contains:
        "images/EmmaBJFace/Emma_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)


transform Emma_BJ_MouthAnim():

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















transform Emma_BJ_Head_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 40
        ease 1.5 offset (0,-40)
        repeat






transform Emma_BJ_MouthAnimC():

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



transform Emma_BJ_Cock_0():

    anchor (.5,.5)
    rotate -10
transform Emma_BJ_Cock_1():

    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5
        pause .5
        ease 2.5 rotate 0
        repeat
transform Emma_BJ_Cock_2():

    anchor (.5,.5)
    rotate 0
    alpha 1




transform Emma_BJ_Head_0():

    subpixel True
    ease 1.5 offset (0,0)
transform Emma_BJ_Body_0():

    subpixel True
    ease 1.5 offset (0,0)


transform Emma_BJ_Head_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (25,100)
        ease 2 offset (0,-35)
        pause .5
        repeat
transform Emma_BJ_Body_1():

    subpixel True
    ease 0.5 offset (0,-35)
    block:
        ease 2.5 offset (30,90)
        ease 2 offset (0,-35)
        pause .5
        repeat













transform Emma_BJ_Body_2():

    subpixel True
    offset (0,-40)
    block:
        ease 1 yoffset 15
        ease 1.5 offset (0,-40)
        repeat

transform Emma_BJ_Head_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120
        ease 1.5 offset (0,50)
        repeat
transform Emma_BJ_Body_3():

    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100
        ease 1.5 offset (0,50)
        repeat

transform Emma_BJ_Head_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat
transform Emma_BJ_Body_4():

    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Emma_BJ_Head_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat
transform Emma_BJ_Body_5():

    subpixel True
    offset (0,-30)
    block:
        ease 1 yoffset -20
        ease 1.5 offset (0,-30)
        repeat

transform Emma_BJ_Head_6():

    ease .5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230
        repeat
transform Emma_BJ_Body_6():

    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190
        repeat


















label Emma_BJ_Launch(Line=primary_action):
    if renpy.showing("Emma_BJ_Animation"):
        return

    call Emma_Hide
    if Line == "L" or Line == "cum":
        show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(stage_center):
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(stage_center):
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    $ action_speed = 0
    if Taboo and Line == "L":
        if len(Present) >= 2:
            if Present[0] != EmmaX:
                "[EmmaX.name] looks back at [Present[0].name] to see if she's watching."
            elif Present[1] != EmmaX:
                "[EmmaX.name] looks back at [Present[1].name] to see if she's watching."
        else:
            "[EmmaX.name] looks around to see if anyone can see her."
        "She then bends down and puts your cock to her mouth."
    elif Line == "L":
        "[EmmaX.name] smoothly bends down and places your cock against her cheek."


    if Line != "cum":
        $ primary_action = "blowjob"

    show Emma_Sprite zorder EmmaX.sprite_layer:
        alpha 0
    show Emma_BJ_Animation zorder 150:
        pos (645,510)
    return

label Emma_BJ_Reset:
    if not renpy.showing("Emma_BJ_Animation"):
        return

    call Emma_Hide
    $ action_speed = 0

    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(stage_center):
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Emma_Sprite zorder EmmaX.sprite_layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return









image Emma_Hand_Under:
    "images/EmmaSprite/handemma2.png"
    anchor (0.5,0.5)
    pos (-10,0)


image Emma_Hand_Over:
    "images/EmmaSprite/handemma1.png"
    anchor (0.5,0.5)
    pos (-10,0)

transform Emma_Hand_1():
    subpixel True
    pos (-20,-100)
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5
        pause 0.1
        repeat

transform Emma_Hand_2():
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

transform Handcock_1E():
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

transform Handcock_2E():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Emma_HJ_Animation:
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Emma_Hand_Under"),
            "action_speed == 1", At("Emma_Hand_Under", Emma_Hand_1()),
            "action_speed >= 2", At("Emma_Hand_Under", Emma_Hand_2()),
            "action_speed ", Null(),
            ),
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1E()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2E()),
            "action_speed ", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            "not action_speed", Transform("Emma_Hand_Over"),
            "action_speed == 1", At("Emma_Hand_Over", Emma_Hand_1()),
            "action_speed >= 2", At("Emma_Hand_Over", Emma_Hand_2()),
            "action_speed ", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4


label Emma_HJ_Launch(Line=primary_action):
    if renpy.showing("Emma_HJ_Animation"):
        $ primary_action = "handjob"
        return
    call Emma_Hide
    if Line == "L":
        show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (0,200)
    else:
        show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(stage_right):
            alpha 1
            ease 1 zoom 1.7 offset (0,200)
        with dissolve

    if Line == "L":
        if Taboo:
            if len(Present) >= 2:
                if Present[0] != EmmaX:
                    "[EmmaX.name] looks back at [Present[0].name] to see if she's watching."
                elif Present[1] != EmmaX:
                    "[EmmaX.name] looks back at [Present[1].name] to see if she's watching."
            else:
                "[EmmaX.name] looks around to see if anyone can see her."
            "She then bends down and grabs your cock."
        else:
            "[EmmaX.name] bends down and grabs your cock."

    $ action_speed = 0
    if Line != "cum":
        $ primary_action = "handjob"
    else:
        $ action_speed = 1
    pause .5
    $ EmmaX.ArmPose = 1
    show Emma_HJ_Animation zorder 150 at sprite_location(stage_center) with easeinbottom:

        offset (100,250)
    return

label Emma_HJ_Reset:
    if not renpy.showing("Emma_HJ_Animation"):
        return
    $ action_speed = 0
    $ EmmaX.ArmPose = 1
    hide Emma_HJ_Animation with easeoutbottom
    call Emma_Hide
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        zoom 1.7 offset (-50,200)
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        zoom 1 offset (0,0)
    return







image Emma_FJ_Chair:

    contains:
        ConditionSwitch(

            "not renpy.showing('Emma_FJ_Animation')", Null(),
            "True", "images/EmmaSprite/EmmaSprite_Chair.png"
            )
        anchor (0.6, 0.05)
        zoom 0.75

image Emma_FJ_Mask:

    contains:
        "images/EmmaSprite/EmmaSprite_FJMask.png"
        anchor (0.6, 0.0)
        zoom 0.75
        pos (200,0)

image Emma_FJ_Animation:

    contains:

        ConditionSwitch(

            "EmmaX.legs == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Back_FJ.png",
            "True", Null(),
            )
        zoom 0.75
    contains:
        ConditionSwitch(

            "not EmmaX.Wet", Null(),
            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", Null(),
            "EmmaX.underwear and not EmmaX.underwearDown and EmmaX.Wet <= 1", Null(),
            "EmmaX.Wet == 1", AlphaMask("Wet_Drip","Emma_Drip_Mask"),
            "True", AlphaMask("Wet_Drip2","Emma_Drip_Mask"),
            )
        pos (160,400)
    contains:
        ConditionSwitch(

            "'in' not in EmmaX.Spunk and 'anal' not in EmmaX.Spunk", Null(),
            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", Null(),
            "True", ConditionSwitch(
                    "EmmaX.underwear and EmmaX.underwearDown", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "EmmaX.legs == 'pants'", AlphaMask("Spunk_Drip","Emma_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip","Emma_Drip_Mask"),
                    ),
            )
        pos (160,400)
    contains:

        AlphaMask("Emma_Sprite", "Emma_FJ_Mask")
    contains:


        "images/EmmaSprite/EmmaSprite_FJRight.png"
        zoom 0.75
    contains:

        ConditionSwitch(
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJRight_Pantyhose.png",
            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJRight_PantyhoseHoled.png",
            "EmmaX.hose == 'stockings' or EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSprite/EmmaSprite_FJRight_Stocking.png",
            "True", Null(),
            )
        zoom 0.75
    contains:
        ConditionSwitch(

            "not EmmaX.Wet", Null(),
            "EmmaX.legs and EmmaX.Wet <= 1", Null(),
            "EmmaX.legs", "images/EmmaSprite/EmmaSprite_Wet.png",
            "EmmaX.Wet == 1", "images/EmmaSprite/EmmaSprite_Wet.png",
            "True", "images/EmmaSprite/EmmaSprite_Wet.png",
            )
        zoom .75
    contains:

        ConditionSwitch(
            "EmmaX.hose == 'garterbelt' or EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSprite/EmmaSprite_FJRight_Garter.png",
            "True", Null(),
            )
        zoom 0.75
    contains:

        ConditionSwitch(

            "not EmmaX.legs", Null(),
            "EmmaX.legs == 'dress' and EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Dress_FJ2.png",
            "EmmaX.legs == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_FJ1.png",
            "EmmaX.Upskirt", ConditionSwitch(

                        "EmmaX.legs == 'skirt'", "images/EmmaSprite/EmmaSprite_SkirtUp.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(
                        "EmmaX.legs == 'pants'", "images/EmmaSprite/EmmaSprite_FJRight_Pants.png",
                        "EmmaX.legs == 'yoga_pants'", "images/EmmaSprite/EmmaSprite_FJRight_Yoga.png",
                        "EmmaX.legs == 'skirt'", "images/EmmaSprite/EmmaSprite_FJRight_Skirt.png",
                        "True", Null(),
                        ),
            )
        zoom 0.75
    contains:

        ConditionSwitch(
            "EmmaX.Upskirt and EmmaX.legs and EmmaX.legs != 'skirt'", Null(),
            "EmmaX.accessory", "images/EmmaSprite/EmmaSprite_FJRight_Boot.png",
            "True", Null(),
            )
        zoom 0.75
    contains:


        ConditionSwitch(
            "EmmaX.legs == 'dress' and EmmaX.ArmPose == 2", "images/EmmaSprite/EmmaSprite_Dress_Over2.png",
            "EmmaX.legs == 'dress'", "images/EmmaSprite/EmmaSprite_Dress_Over1.png",
            "True", Null(),
            )
        zoom 0.75
    contains:
        ConditionSwitch(



            "action_speed == 1", "Emma_FJ_Legs_1",
            "action_speed == 4", "Emma_FJ_Legs_4",
            "action_speed >= 2", "Emma_FJ_Legs_2",
            "True", "Emma_FJ_Legs_0",
            )
        pos (450,20)
        zoom 0.7
    contains:

        ConditionSwitch(
            "EmmaX.hair == 'hat' or EmmaX.hair == 'hat wet'", "images/EmmaSprite/EmmaSprite_Hat.png",
            "True", Null(),
            )
        zoom 0.4
        pos (-17,-45)
    anchor (0.6, 0.0)
    zoom .85
    subpixel True
    block:
        ease 1 yoffset -2
        ease 1 yoffset 0
        repeat




image Emma_FJ_Legs_0:

    contains:

        ConditionSwitch(

            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.legs == 'yoga_pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_PantyhoseHoled.png",
            "EmmaX.hose == 'stockings' or EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png",
            )
        subpixel True
        transform_anchor True
        anchor (.70,.63)
        pos (290,630)
        rotate 12
        parallel:
            ease 2.5 ypos 610
            ease 2.5 ypos 630
            repeat
        parallel:
            ease 2.5 rotate 10
            ease 2.5 rotate 12
            repeat
    contains:
        "Emma_FJ_Calf"
        subpixel True
        transform_anchor True
        pos (340,510)
        rotate 20
        parallel:
            ease 2.5 ypos 490
            ease 2.5 ypos 510
            repeat
        parallel:
            ease 2.5 rotate 15
            ease 2.5 rotate 20
            repeat
    contains:

        ConditionSwitch(

            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.hose == 'ripped_pantyhose' or EmmaX.hose == 'pantyhose') and EmmaX.underwearDown", Null(),
            "EmmaX.hose and EmmaX.hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (200,680)
        rotate 25
        parallel:
            easeout 2 rotate -5
            easein .5 rotate -10
            easeout 2 rotate 20
            easein .5 rotate 25
            repeat
    contains:

        "Zero_Emma_FootCock"
        transform_anchor True
        rotate 0
        block:
            pause .5
            easeout 1.5 rotate -5
            easein .5 rotate -7
            pause .5
            easeout 1 rotate -3
            easein 1 rotate 0
            repeat
    anchor (0.6, 0.0)


image Emma_FJ_Legs_1:

    contains:

        ConditionSwitch(

            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.legs == 'yoga_pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_PantyhoseHoled.png",
            "EmmaX.hose == 'stockings' or EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png",
            )
        transform_anchor True
        anchor (.70,.63)
        pos (280,615)
        rotate 10
        parallel:
            pause 1.3
            ease 2.2 ypos 630
            ease 1 ypos 615
            repeat
        parallel:
            easein .5 rotate 12
            pause 1
            ease 1.5 rotate 18
            pause .5
            easeout 1 rotate 14
            repeat
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (350,475)
        rotate 15
        parallel:
            pause 1.5
            ease 2 ypos 515
            ease 1 ypos 475
            repeat
        parallel:
            ease 1 rotate 8
            ease 1 rotate 18
            ease 2 rotate 20
            ease .5 rotate 18
            repeat
    contains:

        ConditionSwitch(

            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.hose == 'ripped_pantyhose' or EmmaX.hose == 'pantyhose') and EmmaX.underwearDown", Null(),
            "EmmaX.hose and EmmaX.hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (200,680)
        rotate 25
        parallel:
            ease 1 xpos 240
            ease 1 xpos 200
            pause 2.5
            repeat
        parallel:
            pause 1.5
            ease 2 ypos 730
            ease 1 ypos 680
            repeat
        parallel:
            easein 1 rotate 0
            easeout 1 rotate 25
            easein 2 rotate 35
            easeout .5 rotate 25
            repeat
    contains:

        "Zero_Emma_FootCock"
        transform_anchor True
        block:
            easein 1 rotate 0
            ease 2.5 rotate -5
            easeout 1 rotate 2
            repeat
    anchor (0.6, 0.0)


image Emma_FJ_Legs_2:

    contains:

        ConditionSwitch(

            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.legs == 'yoga_pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_PantyhoseHoled.png",
            "EmmaX.hose == 'stockings' or EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png",
            )
        transform_anchor True
        anchor (.70,.63)
        pos (290,610)
        rotate 10
        parallel:
            ease .5 ypos 630
            ease 1 ypos 610
            repeat
        parallel:
            ease .5 rotate 0
            ease 1 rotate 10
            repeat
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (380,450)
        rotate 15
        parallel:
            ease .5 pos (320,500)
            ease 1 pos (380,460)
            repeat
        parallel:
            ease .5 rotate -5
            ease 1 rotate 15
            repeat
    contains:

        ConditionSwitch(

            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.hose == 'ripped_pantyhose' or EmmaX.hose == 'pantyhose') and EmmaX.underwearDown", Null(),
            "EmmaX.hose and EmmaX.hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (240,670)
        rotate 30
        parallel:
            ease .5 pos (240,870)
            ease 1 pos (240,670)
            repeat
        parallel:
            ease .5 rotate 20
            ease 1 rotate 30
            repeat
    contains:

        "Zero_Emma_FootCock"
        transform_anchor True
        block:
            ease .5 rotate -8
            ease 1 rotate 0
            repeat
    anchor (0.6, 0.0)



image Emma_FJ_Legs_4:

    contains:

        ConditionSwitch(

            "EmmaX.legs == 'pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.legs == 'yoga_pants' and not EmmaX.Upskirt", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Yoga.png",
            "EmmaX.hose == 'pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Pantyhose.png",
            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftThigh_PantyhoseHoled.png",
            "EmmaX.hose == 'stockings' or EmmaX.hose == 'stockings_and_garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftThigh_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftThigh.png",
            )
        transform_anchor True
        anchor (.70,.63)
        pos (290,610)
        rotate 10
        parallel:
            ease 1 rotate 0
            ease 1.3 rotate 23
            pause .5
            repeat
    contains:
        "Emma_FJ_Calf"
        transform_anchor True
        pos (380,450)
        rotate 15

        parallel:
            ease 1 pos (320,480)
            ease 1.3 pos (380,450)
            pause .5
            repeat
        parallel:
            ease 1 rotate 5
            ease 1.3 rotate 15
            pause .5
            repeat
    contains:

        ConditionSwitch(

            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJFoot_StockingHoled.png",
            "(EmmaX.hose == 'ripped_pantyhose' or EmmaX.hose == 'pantyhose') and EmmaX.underwearDown", Null(),
            "EmmaX.hose and EmmaX.hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJFoot_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJFoot.png",
            )
        transform_anchor True
        anchor (.6,.8)
        pos (240,670)
        rotate 40
        parallel:
            ease 1 pos (200,750)
            ease 1.3 pos (220,670)
            pause .5
            repeat
        parallel:
            ease 1 rotate 30
            ease 1.3 rotate 40
            pause .5
            repeat
    contains:


        "Zero_Emma_FootCock"
        transform_anchor True
        block:
            pause .1
            ease .9 rotate -8
            ease 1.3 rotate 0
            pause .5
            repeat
    anchor (0.6, 0.0)



image Zero_Emma_FootCock:

    contains:
        ConditionSwitch(
                "Player.Sprite", "Blowcock",
                "True", Null(),
                )
    pos (200,1000)
    zoom .9
    anchor (-.4,0.7)


image Emma_FJ_Calf:

    contains:
        ConditionSwitch(

            "EmmaX.hose == 'ripped_pantyhose' and not EmmaX.underwearDown", "images/EmmaSprite/EmmaSprite_FJLeftCalf_StockingHoled.png",
            "(EmmaX.hose == 'ripped_pantyhose' or EmmaX.hose == 'pantyhose') and EmmaX.underwearDown", Null(),
            "EmmaX.hose and EmmaX.hose != 'garterbelt'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Stocking.png",
            "True", "images/EmmaSprite/EmmaSprite_FJLeftCalf.png",
            )
    contains:

        ConditionSwitch(

            "not EmmaX.legs or EmmaX.Upskirt", Null(),
            "EmmaX.legs == 'pants'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Pants.png",
            "EmmaX.legs == 'yoga_pants'", "images/EmmaSprite/EmmaSprite_FJLeftCalf_Yoga.png",
            "True", Null(),
            )
    anchor (.31,.63)



label Emma_FJ_Launch(Line=primary_action):
    $ primary_action = "foot"
    $ Player.Sprite = 1
    $ ShowFeet = 1
    if EmmaX.pose == "doggy":
        call Emma_Sex_Launch ("foot")
        return

    if renpy.showing("Emma_FJ_Animation"):
        return
    call Emma_Hide
    show Emma_FJ_Chair zorder 10:
        xpos 1580
        yoffset 170
        alpha 1
        ease .5 xpos 590
    show Emma_FJ_Animation zorder 150:
        alpha 0
        pos (950,200)
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        ease 1 zoom .8 xpos 580 yoffset 150
    pause 1

    show Emma_FJ_Chair zorder 10:
        alpha 1
        xpos 590
    show Emma_Sprite zorder EmmaX.sprite_layer:
        alpha 0
    $ action_speed = 0
    show Emma_FJ_Animation zorder 150:
        ease .5 alpha 1
    pause 0.5
    show Emma_FJ_Animation zorder 150:
        alpha 1
    return

label Emma_FJ_Reset:
    if renpy.showing("Emma_Doggy_Animation"):
        call Emma_Doggy_Reset
        return

    if not renpy.showing("Emma_FJ_Animation"):
        return
    call Emma_Hide
    $ Player.Sprite = 0

    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        zoom .8 xpos 580 yoffset 150
    show Emma_Sprite zorder EmmaX.sprite_layer:
        alpha 1
        ease .5 zoom 1 xpos EmmaX.sprite_location yoffset 0 alpha 1
    pause .5

    hide Emma_FJ_Chair zorder 10
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        alpha 1
        zoom 1 offset (0,0) xpos EmmaX.sprite_location

    "[EmmaX.name] stands back up."
    return












































image Emma_At_Desk:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (450,190)

image Emma_At_Podium:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (670,180)


image Emma_Behind_Podium:
    contains:
        subpixel True
        "Emma_Sprite"
        zoom 0.29
        pos (640,180)
        block:
            subpixel True
            ease .5 ypos 183
            ease .5 ypos 180
            pause .5
            repeat



label Emma_Kissing_Launch(T=primary_action, Set=1):
    call Emma_Hide
    $ primary_action = T
    $ EmmaX.pose = "kiss" if Set else EmmaX.pose
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location)
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(stage_center):
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return

label Emma_Kissing_Smooch:
    $ EmmaX.change_face("kiss")
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(stage_center):
        ease 0.5 xpos stage_center offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos EmmaX.sprite_location zoom 1
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        zoom 1
    $ EmmaX.change_face("sexy")
    return

label Emma_Breasts_Launch(T=primary_action, Set=1):
    call Emma_Hide
    $ primary_action = T
    $ EmmaX.pose = "breasts" if Set else EmmaX.pose
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return

label Emma_Middle_Launch(T=primary_action, Set=1):
    call Emma_Hide
    $ primary_action = T
    $ EmmaX.pose = "mid" if Set else EmmaX.pose
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):

        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Emma_Pussy_Launch(T=primary_action, Set=1):
    call Emma_Hide
    $ primary_action = T
    $ EmmaX.pose = "pussy" if Set else EmmaX.pose
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return

label Emma_Pos_Reset(T=0, Set=0):
    if EmmaX.location != bg_current:
        return
    call Emma_Hide
    show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location):
        ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Emma_Sprite zorder EmmaX.sprite_layer:
        offset (0,0)
        anchor (0.5, 0.0)
        zoom 1
        xzoom 1
        yzoom 1
        alpha 1
        pos (EmmaX.sprite_location,50)
    $ EmmaX.pose = "full" if Set else 0
    $ primary_action = T
    return

label Emma_Hide(Sprite=0):
    call Emma_Sex_Reset
    hide Emma_SexSprite
    hide Emma_Doggy_Animation
    hide Emma_HJ_Animation
    hide Emma_BJ_Animation
    hide Emma_TJ_Animation
    hide Emma_FJ_Animation
    if Sprite:
        hide Emma_Sprite
    return



image GropeLeftBreast_Emma:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65
        pos (215,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image GropeRightBreast_Emma:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (110,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -90
        block:
            ease 1 rotate -60
            ease 1 rotate -90
            repeat


image LickRightBreast_Emma:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (105,375)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (85,345)
            pause .5
            ease 1.5 rotate 30 pos (105,375)
            repeat

image LickLeftBreast_Emma:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (205,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (190,350)
            pause .5
            ease 1.5 rotate 30 pos (205,370)
            repeat

image GropeThigh_Emma:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (150,750)
            ease 1 rotate 100 pos (180,670)
            repeat

image GropePussy_Emma:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,600)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (200,585)
                ease .75 rotate 170 pos (200,600)
            choice:
                ease .5 rotate 190 pos (200,585)
                pause .25
                ease 1 rotate 170 pos (200,600)
            repeat

image FingerPussy_Emma:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (210,665)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (220,640)
                pause .5
                ease 1 rotate 50 pos (210,665)
            choice:
                ease .5 rotate 40 pos (220,640)
                pause .5
                ease 1.75 rotate 50 pos (210,665)
            choice:
                ease 2 rotate 40 pos (220,640)
                pause .5
                ease 1 rotate 50 pos (210,665)
            choice:
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665)
                ease .25 rotate 40 pos (220,640)
                ease .25 rotate 50 pos (210,665)
            repeat

image Lickpussy_Emma:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (230,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (210,605)
            linear .5 rotate -60 pos (200,615)
            easein 1 rotate 10 pos (230,625)
            repeat

image VibratorRightBreast_Emma:
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

image VibratorLeftBreast_Emma:
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

image VibratorPussy_Emma:
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

image VibratorAnal_Emma:
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

image VibratorPussyInsert_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Emma:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0




image GirlGropeBothBreast_Emma:
    contains:
        "GirlGropeLeftBreast_Emma"
    contains:
        "GirlGropeRightBreast_Emma"

image GirlGropeLeftBreast_Emma:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (230,360)
            ease 1 rotate -20 pos (240,370)
            repeat

image GirlGropeRightBreast_Emma:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (90,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate -30 pos (90,410)
            ease 1 rotate -10 pos (90,380)
            repeat

image GirlGropeThigh_Emma:
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

image GirlGropePussy_EmmaSelf:
    contains:
        "GirlGropePussy_Emma"
        anchor (0.5,0.5)
        rotate -40

        pos (120,530)

image GirlGropePussy_Emma:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (200,575)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (205,590)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (205,590)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
                ease .5 rotate 205 pos (205,590)
                ease .75 rotate 200 pos (205,595)
            choice:
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
                ease .3 rotate 205 pos (205,590)
                ease .3 rotate 200 pos (205,600)
            repeat

image GirlFingerPussy_Emma:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice:
                ease .75 rotate 210 pos (220,645)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice:
                ease .5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice:
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
            choice:
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
            repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
