# Basic character Sprites

image Jean_Sprite:
    LiveComposite(
        (516,954),
        (160,0), "Jean_Sprite_HairBack",
        (0,0), ConditionSwitch(
            #body
            "JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Body2.png",         # right hand up/left down
            "True", "images/JeanSprite/Jean_Sprite_Body1.png", #if JeanX.Arms == 1   # right Hand on hip/left raised
            ),
#        (0,0), ConditionSwitch(
#            #Water effect
#            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1.png",
#            "JeanX.Water", "images/JeanSprite/Jean_Sprite_Water2.png",
#            "True", Null(),
#            ),

#        (145,560), ConditionSwitch(    #(225,560)
#            #Personal Wetness
#            "not JeanX.Wet", Null(),
#            "JeanX.Legs and JeanX.Legs != 'skirt' and not JeanX.Upskirt", Null(),
#            "JeanX.Panties and not JeanX.PantiesDown and JeanX.Wet <= 1", Null(),
#            "JeanX.Wet == 1", ConditionSwitch( #Wet = 1
#                    "JeanX.Panties and JeanX.PantiesDown", AlphaMask("Wet_Drip","Jean_Drip_MaskP"),
#                    "JeanX.Legs and JeanX.Legs != 'skirt'", AlphaMask("Wet_Drip","Jean_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip","Jean_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            "True", ConditionSwitch( #Wet = 2+
#                    "JeanX.Panties and JeanX.PantiesDown", AlphaMask("Wet_Drip2","Jean_Drip_MaskP"),
#                    "JeanX.Legs and JeanX.Legs != 'skirt'", AlphaMask("Wet_Drip2","Jean_Drip_MaskP"),
#                    "JeanX.Panties", AlphaMask("Wet_Drip","Jean_Drip_Mask"), #"Wet_Drip2",#
#                    "True", AlphaMask("Wet_Drip2","Jean_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            ),
#        (145,560), ConditionSwitch(    #(225,560)
#            #dripping spunk
#            "'in' not in JeanX.Spunk and 'anal' not in JeanX.Spunk", Null(),
#            "JeanX.Legs and JeanX.Legs != 'skirt' and not JeanX.Upskirt", Null(),
#            "JeanX.Panties and not JeanX.PantiesDown and JeanX.Wet <= 1", Null(),
#            "True", ConditionSwitch( #Wet = 2+
#                    "JeanX.Panties and JeanX.PantiesDown", AlphaMask("Spunk_Drip2","Jean_Drip_MaskP"),
##                    "JeanX.Legs and JeanX.Legs != 'skirt'", AlphaMask("Spunk_Drip2","Jean_Drip_MaskP"), #add if pantes have down art
#                    "JeanX.Panties", AlphaMask("Spunk_Drip","Jean_Drip_Mask"), #"Wet_Drip2",#
#                    "True", AlphaMask("Spunk_Drip2","Jean_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            ),
        (0,0), ConditionSwitch(
            #pubes
            "JeanX.Pubes", "images/JeanSprite/Jean_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #nude lower piercings
            "not JeanX.Pierce", Null(),
            "JeanX.Panties and not JeanX.PantiesDown", Null(),
            "JeanX.Legs != 'skirt' and JeanX.Legs and not JeanX.Upskirt", Null(), #skirt if wearing a skirt
            "JeanX.Pierce == 'barbell'", "images/JeanSprite/Jean_Sprite_Barbell_Pussy.png",
            "JeanX.Pierce == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #stockings
            "JeanX.Hose == 'stockings'", "images/JeanSprite/Jean_Sprite_Hose_Stockings.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanSprite/Jean_Sprite_Hose_StockingsandGarter.png",
            "JeanX.Hose == 'garterbelt'", "images/JeanSprite/Jean_Sprite_Hose_Garterbelt.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Personal Wetness
            "not JeanX.Wet", Null(),
            "JeanX.Legs and JeanX.Wet <= 1", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Wetness.png",       #JeanX.Wet >1
            ),
        (0,0), ConditionSwitch(
            #panties
            "not JeanX.Panties", Null(),
            "JeanX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not JeanX.Legs or JeanX.Upskirt or JeanX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "JeanX.Panties == 'green panties' and JeanX.Wet", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png", #fix
                            "JeanX.Panties == 'green panties'", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png",
                            "JeanX.Panties == 'lace panties'", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png",
                            "JeanX.Panties == 'bikini bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini_Down.png",
                            "True", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png", #fix
                            ),
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if she's got panties and they are not down
                    "JeanX.Wet", ConditionSwitch(
                        #if she's  wet
                        "JeanX.Panties == 'green panties'", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        "JeanX.Panties == 'lace panties'", "images/JeanSprite/Jean_Sprite_Panties_Lace.png",
                        "JeanX.Panties == 'bikini bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini.png",
                        "True", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        ),
                    "True", ConditionSwitch(
                        #if she's not wet
                        "JeanX.Panties == 'green panties'", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        "JeanX.Panties == 'lace panties'", "images/JeanSprite/Jean_Sprite_Panties_Lace.png",
                        "JeanX.Panties == 'bikini bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini.png",
                        "True", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        ),
                    ),
            ),

        (0,0), ConditionSwitch(
            #pantyhose
            "JeanX.Hose == 'pantyhose' and (not JeanX.PantiesDown or not JeanX.Panties)", "images/JeanSprite/Jean_Sprite_Hose_Pantyhose.png",
            "JeanX.Hose == 'ripped pantyhose' and (not JeanX.PantiesDown or not JeanX.Panties)", "images/JeanSprite/Jean_Sprite_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants
            "not JeanX.Legs", Null(),
            "JeanX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "JeanX.Legs == 'shorts'", "images/JeanSprite/Jean_Sprite_Legs_Shorts_Down.png",
                        "JeanX.Legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants_Down.png",
                        "JeanX.Legs == 'yoga pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants_Down.png",
                        "JeanX.Legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt_Up.png",
                        "True", Null(),
                        ),
            "True", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Wet", ConditionSwitch(
                        #if she's wet
                        "JeanX.Legs == 'shorts'", "images/JeanSprite/Jean_Sprite_Legs_Shorts.png",
                        "JeanX.Legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants.png",
                        "JeanX.Legs == 'yoga pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants.png",
                        "JeanX.Legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    "True", ConditionSwitch(
                        #if not she's wet
                        "JeanX.Legs == 'shorts'", "images/JeanSprite/Jean_Sprite_Legs_Shorts.png",
                        "JeanX.Legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants.png",
                        "JeanX.Legs == 'yoga pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants.png",
                        "JeanX.Legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt.png",
                        "True", Null(),
                        ),
                    ),
            ),
        (0,0), ConditionSwitch(
            #clothed lower piercings
            "JeanX.Legs == 'skirt' or JeanX.Legs == 'pants'", Null(),
            "JeanX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the barbell pericings
                    "JeanX.Legs and not JeanX.Upskirt", "images/JeanSprite/Jean_Sprite_Barbell_PussyC.png",
                    "JeanX.Panties and not JeanX.PantiesDown", "images/JeanSprite/Jean_Sprite_Barbell_PussyC.png",
                    "True", Null(),
                    ),
            "JeanX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Legs and not JeanX.Upskirt", "images/JeanSprite/Jean_Sprite_Ring_PussyC.png",
                    "JeanX.Panties and not JeanX.PantiesDown", "images/JeanSprite/Jean_Sprite_Ring_PussyC.png",
                    "True", Null(),
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy spunk
            "JeanX.Legs and not JeanX.Upskirt", Null(),
            "'in' in JeanX.Spunk or 'anal' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #nude peircings
            "not JeanX.Pierce or ((JeanX.Over or JeanX.Chest) and not JeanX.Uptop)", Null(),
            "JeanX.Pierce == 'barbell'", "images/JeanSprite/Jean_Sprite_Barbell_Tits.png",
            "JeanX.Pierce == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_Tits.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #neck
#            "JeanX.Neck == 'leash choker'", "images/JeanSprite/Jean_Sprite_Neck_Leash.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #left arm
            "JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_2LeftArm.png", # right hand up/left down
            "True", "images/JeanSprite/Jean_Sprite_1LeftArm.png", # right Hand on hip/left raised
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Water effect
            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1.png",
            "JeanX.Water", "images/JeanSprite/Jean_Sprite_Water2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Chest layer
            "JeanX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JeanX.Chest == 'green bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2_Up.png",
                    "JeanX.Chest == 'green bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1_Up.png",
                    "JeanX.Chest == 'lace bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2_Up.png",
                    "JeanX.Chest == 'lace bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1_Up.png",
                    "JeanX.Chest == 'corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset_Up.png",
                    "JeanX.Chest == 'sports bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra2_Up.png",
                    "JeanX.Chest == 'sports bra'", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1_Up.png",
                    "JeanX.Chest == 'bikini top' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Bikini2_Up.png",
                    "JeanX.Chest == 'bikini top'", "images/JeanSprite/Jean_Sprite_Chest_Bikini1_Up.png",
                    #"JeanX.Chest == 'lace corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset_Lace_Up.png",
                    "True", Null(),
                    ),
            "JeanX.Chest == 'green bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2.png",
            "JeanX.Chest == 'green bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1.png",
            "JeanX.Chest == 'lace bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_LaceBra2.png",
            "JeanX.Chest == 'lace bra'", "images/JeanSprite/Jean_Sprite_Chest_LaceBra1.png",
            "JeanX.Chest == 'sports bra' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra2.png",
            "JeanX.Chest == 'sports bra'", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1.png",
            "JeanX.Chest == 'bikini top' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Bikini2.png",
            "JeanX.Chest == 'bikini top'", "images/JeanSprite/Jean_Sprite_Chest_Bikini1.png",
            "JeanX.Chest == 'corset' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Chest_Corset2.png",
            "JeanX.Chest == 'corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset1.png",
            #"JeanX.Chest == 'lace corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset_Lace.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Over
            "JeanX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JeanX.Over == 'yellow shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_Tank2_Up.png",   # right hand up/left down
                    "JeanX.Over == 'yellow shirt'", "images/JeanSprite/Jean_Sprite_Over_Tank1_Up.png",                          # right Hand on hip/left raised
                    "JeanX.Over == 'pink shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_PinkShirt2_Up.png",
                    "JeanX.Over == 'pink shirt'", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1_Up.png",
                    "JeanX.Over == 'green shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_GreenShirt2_Up.png",
                    "JeanX.Over == 'green shirt'", "images/JeanSprite/Jean_Sprite_Over_GreenShirt1_Up.png",
#                    "JeanX.Over == 'towel'", "images/JeanSprite/Jean_Sprite_Towel.png",
                    "True", Null(),
                    ),
            "JeanX.Over == 'yellow shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_Tank2.png",   # right hand up/left down
            "JeanX.Over == 'yellow shirt'", "images/JeanSprite/Jean_Sprite_Over_Tank1.png",                          # right Hand on hip/left raised
            "JeanX.Over == 'pink shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_PinkShirt2.png",   # right hand up/left down
            "JeanX.Over == 'pink shirt'", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1.png",                          # right Hand on hip/left raised
            "JeanX.Over == 'green shirt' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_GreenShirt2.png",   # right hand up/left down
            "JeanX.Over == 'green shirt'", "images/JeanSprite/Jean_Sprite_Over_GreenShirt1.png",                          # right Hand on hip/left raised
            "JeanX.Over == 'towel' and JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_Over_Towel2.png",
            "JeanX.Over == 'towel'", "images/JeanSprite/Jean_Sprite_Over_Towel1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #clothed peircings
            "not JeanX.Pierce or (not JeanX.Over and not JeanX.Chest and not JeanX.Uptop)", Null(),
            "JeanX.Pierce == 'barbell'",  "images/JeanSprite/Jean_Sprite_Barbell_TitsC.png",
            "JeanX.Pierce == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_TitsC.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        #Head
#        (0,0), ConditionSwitch(
#            # head
#            "True", "images/JeanSprite/Jean_Sprite_Headref.png",
#            ),
#        (0,0), "Jean_Sprite_Head", #(55,0)
        (160,0), ConditionSwitch(
            # head
#            "renpy.showing('Jean_BJ_Animation')", Null(),
            "True", "Jean_Sprite_Head",
            ),
    #Left hand stuff
        (0,0), ConditionSwitch(
            #left arms toplayer
            "renpy.showing('Jean_HJ_Animation')", Null(),
            "JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_1LeftHand.png", # right Hand on hip/left raised
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1Arm.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #over left arm toplayer
            "renpy.showing('Jean_HJ_Animation')", Null(),
            "JeanX.Chest == 'sports bra' and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1_Arm.png", # right Hand on hip/left raised
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #over left arm toplayer
            "renpy.showing('Jean_HJ_Animation')", Null(),
            "JeanX.Over == 'pink shirt' and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1_Arm.png", # right Hand on hip/left raised
            "True", Null(),
            ),
    #End Left hand stuff
        (0,0), ConditionSwitch(
            #right arms toplayer
            "JeanX.ArmPose != 1", "images/JeanSprite/Jean_Sprite_2RightHand.png", # right hand up/left down
            "True", "images/JeanSprite/Jean_Sprite_1RightHand.png", # right Hand on hip/left raised
            #"True", Null(),
            ),
        (0,0), ConditionSwitch(
            # suspenders
            "not JeanX.Legs or JeanX.Upskirt", Null(), #hides when no skirt on
            "JeanX.ArmPose != 1 and JeanX.Acc == 'suspenders' and JeanX.Uptop", "images/JeanSprite/Jean_Sprite_Acc_Suspenders2_Up.png", #pulled off
            "JeanX.ArmPose != 1 and JeanX.Acc == 'suspenders'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders2.png", #over nips
            "JeanX.ArmPose != 1 and JeanX.Acc == 'suspenders2'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders2_Up.png", #pulled off

            "JeanX.Acc == 'suspenders' and JeanX.Uptop", "images/JeanSprite/Jean_Sprite_Acc_Suspenders1_Up.png", #pulled off
            "JeanX.Acc == 'suspenders'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders1.png", #over nips
            "JeanX.Acc == 'suspenders2'", "images/JeanSprite/Jean_Sprite_Acc_Suspenders1_Up.png", #pulled off
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #hand spunk
#            "JeanX.ArmPose == 2 or 'hand' not in JeanX.Spunk", Null(),
#            "True", "images/JeanSprite/Jean_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not JeanX.Held or JeanX.ArmPose != 2", Null(),
#            "JeanX.ArmPose == 2 and JeanX.Held == 'phone'", "images/JeanSprite/Jean_held_phone.png",
#            "JeanX.ArmPose == 2 and JeanX.Held == 'dildo'", "images/JeanSprite/Jean_held_dildo.png",
#            "JeanX.ArmPose == 2 and JeanX.Held == 'vibrator'", "images/JeanSprite/Jean_held_vibrator.png",
#            "JeanX.ArmPose == 2 and JeanX.Held == 'panties'", "images/JeanSprite/Jean_held_panties.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #UI tool for When Jean is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != JeanX", Null(),

            #this is not a lesbian thing, and a trigger is set, and Jean is the primary. . .
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_JeanSelf",
            "Trigger3 == 'fondle breasts'", ConditionSwitch(
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_Jean",
                        #When zero is working the right breast, fondle left
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_Jean",
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_Jean",
                        #else, fondle both
                    ),
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_Jean",
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_Jean",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_Jean",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_Jean",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == JeanX", Null(),

            #Jean is not primary, and T4 is masturbation, and a T5 is selected
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and JeanX.Lust >= 70", "GirlFingerPussy_Jean",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_Jean",
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_Jean",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger1(primary) actions
            #Jean is primary and a sex trigger is active
            "not Trigger or Ch_Focus != JeanX", Null(),
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Jean",
            "Trigger == 'fondle thighs'", "GropeThigh_Jean",
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Jean",
            "Trigger == 'suck breasts'", "LickRightBreast_Jean",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Jean",
            "Trigger == 'fondle pussy'", "GropePussy_Jean",
            "Trigger == 'lick pussy'", "Lickpussy_Jean",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Jean",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "Trigger == 'vibrator anal'", "VibratorAnal_Jean",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Jean",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != JeanX", Null(),

            #Jean is primary and an offhand trigger is active
            "Trigger2 == 'fondle breasts'", ConditionSwitch(
                    "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Jean",
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_Jean",
                        #else, fondle right
                    ),
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Jean",
                #When sucking right breast, vibrator left
            "Trigger2 == Trigger", Null(),
                #When both triggers are the same, do nothing
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Jean",
            "Trigger2 == 'fondle pussy'", "GropePussy_Jean",
            "Trigger2 == 'lick pussy'", "Lickpussy_Jean",
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Jean",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Jean",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Jean",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Jean",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != JeanX", Null(),

            # There is a threesome trigger set and Jean is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and JeanX.Lust >= 70", "GirlFingerPussy_Jean",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_Jean",
            "Trigger4 == 'lick pussy'", "Lickpussy_Jean",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Jean",
            "Trigger4 == 'suck breasts'", "LickRightBreast_Jean",
            "Trigger4 == 'fondle breasts'", ConditionSwitch(
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Jean", #When zero is working the right breast, fondle left
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Jean",  #When zero is working the left breast, fondle right
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_Jean", #When zero is working the left breast, fondle right
                    "True", "GirlGropeRightBreast_Jean",#else, fondle right
                    ),
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Jean is secondary)
            "Trigger != 'lesbian' or Ch_Focus == JeanX or not Trigger3", Null(),

            # If there is a Trigger3 and Jean is not the focus
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and JeanX.Lust >= 70", "GirlFingerPussy_Jean",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Jean",
            "Trigger3 == 'lick pussy'", "Lickpussy_Jean",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Jean",
            "Trigger3 == 'suck breasts'", "LickRightBreast_Jean",
            "Trigger3 == 'fondle breasts'", ConditionSwitch(
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Jean",
                        #When zero is working the right breast, fondle left
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Jean",
                        #When zero is working the left breast, fondle right
                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_Jean",
                        #When zero is working the right breast, fondle left
                    "True", "GirlGropeRightBreast_Jean",
                        #else, fondle right
                    ),
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    yoffset 15
    zoom .75

image Jean_Sprite_HairBack:
    ConditionSwitch(
            #hair back
            "not JeanX.Hair", Null(),
            "renpy.showing('Jean_BJ_Animation')", Null(),
#            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_UnderSex.png",
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Under.png",
            "JeanX.Hair == 'pony'", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Hair_Short_Under.png",
            ),
#    "images/JeanSprite/Jean_Sprite_Hair_Long_Under.png"
    anchor (0.6, 0.0)
    zoom .32

image Jean_Sprite_HairMid:
    ConditionSwitch(
            #hair back
            "not JeanX.Hair", Null(),
            "renpy.showing('Jean_BJ_Animation')", Null(),
#            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_UnderSex.png",
            "JeanX.Hair == 'wet' JeanX.Hair == 'pony' or JeanX.Water", Null(),
            "True","images/JeanSprite/Jean_Sprite_Hair_Short_Mid.png",
            ),
    anchor (0.6, 0.0)
    zoom .5

image Jean_Sprite_HairTop:
    ConditionSwitch(
            #hair back
            "not JeanX.Hair", Null(),
#            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Short_OverSex.png",
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Over.png",
            "JeanX.Hair == 'pony'", "images/JeanSprite/Jean_Sprite_Hair_Pony_Over.png",
            "True", "images/JeanSprite/Jean_Sprite_Hair_Short_Over.png",
            ),
#    "images/JeanSprite/Jean_Sprite_Hair_Long_Under.png"
    anchor (0.6, 0.0)
    zoom .5

image Jean_Sprite_Head:
    LiveComposite(
        (900,900),
#        (0,0), ConditionSwitch(
#                # hair behind face
#                "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_UnderSex.png",
#                "True", Null(),
#                ),
        (0,0), ConditionSwitch(
                # Face background plate
                "JeanX.Blush >= 2", "images/JeanSprite/Jean_Sprite_Head_Blush2.png",
                "JeanX.Blush", "images/JeanSprite/Jean_Sprite_Head_Blush.png",
                "True", "images/JeanSprite/Jean_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in JeanX.Spunk", Null(),
            "renpy.showing('Jean_BJ_Animation') and Speed >= 2", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Spunk_Chin.png",
            ),
#        (0,0), ConditionSwitch(#Mouths
#            "renpy.showing('Jean_BJ_Animation')", "images/JeanSprite/Jean_Sprite_Mouth_SuckingBJ.png", #and Speed >= 2
#            "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
#            "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite.png",
#            "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Sucking.png",
#            "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss.png",
#            "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad.png",
#            "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
#            "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised.png",
#            "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",
#            "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
#            "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk.png",
#            "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
#            ),
        (0,0), ConditionSwitch(#Mouths
            "'mouth' in JeanX.Spunk", ConditionSwitch(
                    "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal_Spunk.png",
                    "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite_Spunk.png",
                    "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue_Spunk.png",
                    "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss_Spunk.png",
                    "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad_Spunk.png",
                    "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile_Spunk.png",
                    "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised_Spunk.png",
                    "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue_Spunk.png",
                    "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile_Spunk.png",
                    "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk_Spunk.png",
                    "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal_Spunk.png",
                    ),
            "True", ConditionSwitch(
                    "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
                    "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite.png",
                    "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",
                    "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss.png",
                    "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad.png",
                    "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
                    "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised.png",
                    "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",
                    "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
                    "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk.png",
                    "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
                    ),
            ),
        (0,0), ConditionSwitch(
            #brows
            "JeanX.Blush >= 2", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal2.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry2.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad2.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused2.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal2.png",
                    ),
            "JeanX.Blush", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal1.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry1.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad1.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused1.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal1.png",
                    ),
            "True", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Jean Blink",     #Eyes
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not JeanX.Water", Null(),
#            "True", "images/JeanSprite/Jean_Sprite_Wet_Head.png",
#            ),
        (0,0), ConditionSwitch(
            #Hair over
            "not JeanX.Hair", Null(),
            "renpy.showing('Jean_TJ_Animation')", Null(),
#            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_OverSex.png",
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Over.png",
            "JeanX.Hair == 'pony'", "images/JeanSprite/Jean_Sprite_Hair_Pony_Over.png",
            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "not JeanX.Water", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Head_Wet.png",
#            "True", "images/JeanSprite/Jean_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial2.png",
            "'facial' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    anchor (0.6, 0.0)
    #alpha 0.9
    zoom .32

image Jean Blink:
    ConditionSwitch(
    "JeanX.Eyes == 'sexy'", "images/JeanSprite/Jean_Sprite_Eyes_Sexy.png",
    "JeanX.Eyes == 'side'", "images/JeanSprite/Jean_Sprite_Eyes_Side.png",
    "JeanX.Eyes == 'surprised'", "images/JeanSprite/Jean_Sprite_Eyes_Surprised.png",
    "JeanX.Eyes == 'normal'", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png",
    "JeanX.Eyes == 'stunned'", "images/JeanSprite/Jean_Sprite_Eyes_Stunned.png",
    "JeanX.Eyes == 'down'", "images/JeanSprite/Jean_Sprite_Eyes_Down.png",
    "JeanX.Eyes == 'closed'", "images/JeanSprite/Jean_Sprite_Eyes_Closed.png",
    "JeanX.Eyes == 'leftside'", "images/JeanSprite/Jean_Sprite_Eyes_Leftside.png",
    "JeanX.Eyes == 'manic'", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png",
    "JeanX.Eyes == 'psychic'", "images/JeanSprite/Jean_Sprite_Eyes_Psychic.png",
    "JeanX.Eyes == 'squint'", "Jean_Squint",
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
    #This is the mask for her drip pattern
    contains:
        "images/JeanSprite/Jean_Sprite_WetMask.png"
        offset (-145,-560)#(-225,-560)

image Jean_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/JeanSprite/Jean_Sprite_WetMaskP.png"
        offset (-145,-560)#(-225,-560)

# End Jean Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jean Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Jean_Doggy_Base = LiveComposite(
image Jean_Doggy_Animation: #nee Jean_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Jean_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Jean_Doggy_Fuck2_Top",
                    "Speed > 1", "Jean_Doggy_Fuck_Top",
                    "Speed", "Jean_Doggy_Anal_Head_Top",
                    "True", "Jean_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Jean_Doggy_Fuck2_Top",
                    "Speed > 1", "Jean_Doggy_Fuck_Top",
                    "True", "Jean_Doggy_Body",
                    ),
            "True", "Jean_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Jean_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Jean_Doggy_Fuck2_Ass",
                    "Speed > 1", "Jean_Doggy_Fuck_Ass",
                    "Speed", "Jean_Doggy_Anal_Head_Ass",
                    "True", "Jean_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Jean_Doggy_Fuck2_Ass",
                    "Speed > 1", "Jean_Doggy_Fuck_Ass",
                    "True", "Jean_Doggy_Ass",
                    ),
            "True", "Jean_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "Player.Cock == 'foot'", ConditionSwitch(
                    "Speed > 1", "Jean_Doggy_Feet2",
                    "Speed", "Jean_Doggy_Feet1",
                    "True", "Jean_Doggy_Feet0",
                    ),
            "not Player.Sprite and ShowFeet", "Jean_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    yoffset 50


image Jean_Doggy_Body:
    LiveComposite(
        #Upper body
        (420,750),
        (165,0),"Jean_Doggy_Hair_Under", #back of the hair
        (0,0), ConditionSwitch(
            #Under Corset
            "JeanX.Chest == 'corset' and JeanX.Uptop", "images/JeanDoggy/Jean_Doggy_Chest_Corset_Back.png",
            "True", Null(),
            ),
        (165,0), "Jean_Doggy_Head",               #Head
        #(0,0), "images/JeanDoggy/Jean_Doggy_Breast.png", #Body base
        (0,0), "images/JeanDoggy/Jean_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #tanktop
            "not JeanX.Chest", Null(),
            "JeanX.Uptop", ConditionSwitch(
                    "JeanX.Chest == 'lace bra' and JeanX.Over", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up2.png",
                    "JeanX.Chest == 'lace bra'", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up.png",
                    "JeanX.Chest == 'corset'", "images/JeanDoggy/Jean_Doggy_Chest_Corset_Up.png",
                    "JeanX.Chest == 'sports bra'", "images/JeanDoggy/Jean_Doggy_Chest_SportsBra_Up.png",
                    "JeanX.Chest == 'bikini top'", "images/JeanDoggy/Jean_Doggy_Chest_Bikini_Up.png",
                    "JeanX.Over", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up2.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra_Up.png",
                    ),
            "JeanX.Chest == 'lace bra'", "images/JeanDoggy/Jean_Doggy_Chest_LaceBra.png",
            "JeanX.Chest == 'corset'", "images/JeanDoggy/Jean_Doggy_Chest_Corset.png",
            "JeanX.Chest == 'sports bra'", "images/JeanDoggy/Jean_Doggy_Chest_SportsBra.png",
            "JeanX.Chest == 'bikini top'", "images/JeanDoggy/Jean_Doggy_Chest_Bikini.png",
            "True", "images/JeanDoggy/Jean_Doggy_Chest_GreenBra.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "JeanX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not JeanX.Over", Null(),
            "JeanX.Over == 'yellow shirt' and JeanX.Uptop", "images/JeanDoggy/Jean_Doggy_Over_Tank_Up.png",
            "JeanX.Over == 'yellow shirt'", "images/JeanDoggy/Jean_Doggy_Over_Tank.png",
            "JeanX.Over == 'green shirt' and JeanX.Uptop", "images/JeanDoggy/Jean_Doggy_Over_GreenShirt_Up.png",
            "JeanX.Over == 'green shirt'", "images/JeanDoggy/Jean_Doggy_Over_GreenShirt.png",
            "JeanX.Over == 'pink shirt' and JeanX.Uptop", "images/JeanDoggy/Jean_Doggy_Over_PinkShirt_Up.png",
            "JeanX.Over == 'pink shirt'", "images/JeanDoggy/Jean_Doggy_Over_PinkShirt.png",
            "JeanX.Over == 'towel' and not JeanX.Uptop", "images/JeanDoggy/Jean_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #suspenders
            "not JeanX.Legs or JeanX.Upskirt", Null(), #hides when no skirt on
            "JeanX.Acc == 'suspenders' or JeanX.Acc == 'suspenders2'", "images/JeanDoggy/Jean_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in JeanX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Jean_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Jean_Doggy_Head",               #Head
        (165,0),"Jean_Doggy_Hair_Over", #front of the hair  #(165,0)     (153,0)
        (0,0), "images/JeanDoggy/Jean_Doggy_Hand.png", #hand
        )
#    transform_anchor True
#    anchor (225,1400)
    offset (-190,-40)
#    offset (-350,-180)#(-190,-40)
#    rotate 20


image Jean_Doggy_Head:
    LiveComposite(
        #Head
        (420,750),
        #(0,0), "images/JeanDoggy/Jean_Doggy_Head.png", #Body base
        #(0,0), "images/JeanDoggy/Jean_Doggy_TestArm.png",#Eyes
        (0,0), ConditionSwitch(
            #Head
            "JeanX.Blush > 1", "images/JeanDoggy/Jean_Doggy_Head_Blush2.png",
            "JeanX.Blush", "images/JeanDoggy/Jean_Doggy_Head_Blush1.png",
            "True", "images/JeanDoggy/Jean_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "JeanX.Mouth == 'normal'", "images/JeanDoggy/Jean_Doggy_Mouth_Normal.png",
            "JeanX.Mouth == 'lipbite'", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            "JeanX.Mouth == 'sucking'", "images/JeanDoggy/Jean_Doggy_Mouth_Tongue.png",
            "JeanX.Mouth == 'kiss'", "images/JeanDoggy/Jean_Doggy_Mouth_Normal.png",
            "JeanX.Mouth == 'sad'", "images/JeanDoggy/Jean_Doggy_Mouth_Sad.png",
            "JeanX.Mouth == 'smile'", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            "JeanX.Mouth == 'grimace'", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            "JeanX.Mouth == 'surprised'", "images/JeanDoggy/Jean_Doggy_Mouth_Open.png",
            "JeanX.Mouth == 'tongue'", "images/JeanDoggy/Jean_Doggy_Mouth_Tongue.png",
            "True", "images/JeanDoggy/Jean_Doggy_Mouth_Smile.png",
            ),
        (0,0), ConditionSwitch(
            #chin spunk
            "'chin' in JeanX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in JeanX.Spunk", Null(),
            #"JeanX.Mouth == 'normal'", "images/JeanDoggy/Jean_Doggy_Spunk_Normal.png",
            #"JeanX.Mouth == 'sad'", "images/JeanDoggy/Jean_Doggy_Spunk_Normal.png",
            "JeanX.Mouth == 'lipbite'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.Mouth == 'smile'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.Mouth == 'grimace'", "images/JeanDoggy/Jean_Doggy_Spunk_Smile.png",
            "JeanX.Mouth == 'sucking'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            #"JeanX.Mouth == 'kiss'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            "JeanX.Mouth == 'surprised'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            "JeanX.Mouth == 'tongue'", "images/JeanDoggy/Jean_Doggy_Spunk_Open.png",
            "True", "images/JeanDoggy/Jean_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"JeanX.Brows == 'normal'", "images/JeanDoggy/Jean_Doggy_Brows_Normal.png",
            "JeanX.Brows == 'angry'", "images/JeanDoggy/Jean_Doggy_Brows_Angry.png",
            "JeanX.Brows == 'sad'", "images/JeanDoggy/Jean_Doggy_Brows_Sad.png",
            "JeanX.Brows == 'surprised'", "images/JeanDoggy/Jean_Doggy_Brows_Surprised.png",
            #"JeanX.Brows == 'confused'", "images/JeanDoggy/Jean_Doggy_Brows_Normal.png",
            "True", "images/JeanDoggy/Jean_Doggy_Brows_Normal.png",
            ),
        (0,0), "Jean Doggy Blink",#Eyes
        (0,0), ConditionSwitch(
            #wet hair strand
            "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "JeanX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Hair
#            "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Over.png",
#            "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Over.png",
#            ),
#        (0,0), ConditionSwitch(
#            #face spunk
#            "'facial' in JeanX.Spunk", "images/JeanDoggy/Jean_Doggy_Facial.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #face spunk
#            "'hair' in JeanX.Spunk", "images/JeanDoggy/Jean_Doggy_Facial2.png",
#            "True", Null(),
#            ),
        )
    zoom 0.9#0.9 #.83
    #alpha 0.9

image Jean_Doggy_Hair_Under:
        #hair under body
        ConditionSwitch(
                "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
                "JeanX.Hair == 'pony'", Null(),
                "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Under.png",
                )
        zoom .9#0.9 #.83

image Jean_Doggy_Hair_Over:
        #hair under body
        contains:
            ConditionSwitch(
                    "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Over.png",
                    "JeanX.Hair == 'pony'", "images/JeanDoggy/Jean_Doggy_Hair_Pony_Over.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Over.png",
                    )
        contains:
            ConditionSwitch(
                #face spunk
                "'facial' in JeanX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Facial.png",
                "True", Null(),
                )
        contains:
            ConditionSwitch(
                #face spunk
                "'hair' in JeanX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Facial2.png",
                "True", Null(),
                )
        zoom .9#0.9
#        alpha 0.7

image Jean Doggy Blink:
        #Eyes
        ConditionSwitch(
        "JeanX.Eyes == 'sexy'", "images/JeanDoggy/Jean_Doggy_Eyes_Sexy.png",
        "JeanX.Eyes == 'side'", "images/JeanDoggy/Jean_Doggy_Eyes_Normal.png",
        "JeanX.Eyes == 'normal'", "images/JeanDoggy/Jean_Doggy_Eyes_Normal.png",
        "JeanX.Eyes == 'closed'", "images/JeanDoggy/Jean_Doggy_Eyes_Closed.png",
        "JeanX.Eyes == 'manic'", "images/JeanDoggy/Jean_Doggy_Eyes_Surprised.png",
        "JeanX.Eyes == 'down'", "images/JeanDoggy/Jean_Doggy_Eyes_Sexy.png",
        "JeanX.Eyes == 'stunned'", "images/JeanDoggy/Jean_Doggy_Eyes_Stunned.png",
        "JeanX.Eyes == 'surprised'", "images/JeanDoggy/Jean_Doggy_Eyes_Surprised.png",
        "JeanX.Eyes == 'squint'", "images/JeanDoggy/Jean_Doggy_Eyes_Sexy.png",
        "True", "images/JeanDoggy/Jean_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/JeanDoggy/Jean_Doggy_Eyes_Closed.png"
        .25
        repeat

image Jean_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
        (0,0), ConditionSwitch(
            #Legs backside
            "JeanX.Legs == 'skirt'","images/JeanDoggy/Jean_Doggy_Legs_Skirt_Back.png",
            "not JeanX.Upskirt", Null(),
            "JeanX.Legs == 'shorts'", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Back.png",
            "JeanX.Legs == 'pants'", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Back.png",
            "JeanX.Legs == 'yoga pants'", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties back
            "not JeanX.PantiesDown or (JeanX.Legs == 'pants' and not JeanX.Upskirt)", Null(),
            "JeanX.Panties == 'green panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green_Back.png",
            "JeanX.Panties == 'bikini bottoms'", Null(), #"images/JeanDoggy/Jean_Doggy_Panties_Bikini_Back.png",
            "JeanX.Panties", "images/JeanDoggy/Jean_Doggy_Panties_Green_Back.png",
            "True", Null(),
            ),
        (0,0), "images/JeanDoggy/Jean_Doggy_Ass.png", #Ass Base
        (0,0), ConditionSwitch(
            #Wet look
            "JeanX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "JeanX.Hose == 'stockings'", "images/JeanDoggy/Jean_Doggy_Hose_Stocking.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not JeanX.PantiesDown or (JeanX.Legs == 'pants' and not JeanX.Upskirt)", Null(),
            "JeanX.Panties == 'green panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green_Down.png",
            "JeanX.Panties == 'bikini bottoms'", Null(), #"images/JeanDoggy/Jean_Doggy_Panties_Bikini_Down.png",
            "JeanX.Panties", "images/JeanDoggy/Jean_Doggy_Panties_Green_Down.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Pussy Composite
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "Speed > 2", "Jean_Pussy_Fucking3",#Speed 3
                    "Speed > 1", "Jean_Pussy_Fucking2",#Speed 2
                    "Speed", "Jean_Pussy_Heading",      #Speed 1
                    "True", "Jean_Pussy_Static",              #Speed 0
                    ),
            "Trigger == 'lick pussy'", "images/JeanDoggy/Jean_Doggy_Pussy_Open.png",
            "JeanX.Legs and not JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            "JeanX.Panties and not JeanX.PantiesDown", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "Jean_Pussy_Fingering",
            "Trigger == 'dildo pussy'", "Jean_Pussy_Fucking2",
            "True", "images/JeanDoggy/Jean_Doggy_Pussy_Closed.png",
            ),


        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in JeanX.Spunk and Player.Cock == 'in'",Null(),# "images/JeanDoggy/Jean_Doggy_SpunkPussyOpen.png",  #fix for JeanX.Spunk is used later
            "'in' in JeanX.Spunk ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "JeanX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "JeanX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not JeanX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/JeanDoggy/Jean_Doggy_Pubes_Fucked.png",
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "Trigger == 'dildo pussy'", Null(),
            "JeanX.Legs == 'pants' and not JeanX.Upskirt", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "JeanX.PantiesDown and Trigger == 'lick pussy'", "images/JeanDoggy/Jean_Doggy_Pubes_Open.png",
            "JeanX.PantiesDown", "images/JeanDoggy/Jean_Doggy_Pubes.png",
            "JeanX.Panties", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "JeanX.Hose and JeanX.Hose != 'stockings'", "images/RogueDoggy/Rogue_Doggy_Pubes_Panties.png",
            "Trigger == 'lick pussy'", "images/JeanDoggy/Jean_Doggy_Pubes_Open.png",
            "True", "images/JeanDoggy/Jean_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "JeanX.Pierce == 'ring'", "images/JeanDoggy/Jean_Doggy_PussyRing.png",
            "JeanX.Pierce == 'barbell'", "images/JeanDoggy/Jean_Doggy_PussyBarbell.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Anus Composite
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "Speed > 2", "Jean_Anal_Fucking2", #Speed 3
                    "Speed > 1", "Jean_Anal_Fucking",  #Speed 2
                    "Speed", "Jean_Anal_Heading",      #Speed 1
                    "True", "Jean_Anal",               #Speed 0
                    ),
#            "Action == 'plug'", "Jean_Anal_Plug",
#            "Action == 'plug'", "test_case",
            "JeanX.Legs and not JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "JeanX.Panties and not JeanX.PantiesDown", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "Trigger == 'insert ass' or Trigger2 == 'insert ass'", "Jean_Anal_Fingering",
            "Trigger == 'dildo anal'", "Jean_Anal_Fucking",
            "JeanX.Loose", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in JeanX.Spunk or Player.Sprite", Null(),
            "Player.Cock == 'anal'", "images/JeanDoggy/Jean_Doggy_SpunkAnalOpen.png",
            "JeanX.Loose", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            "True", "images/JeanDoggy/Jean_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "JeanX.PantiesDown or not JeanX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
#            "Trigger == 'dildo pussy'", Null(),
            "JeanX.Panties == 'green panties' and JeanX.Wet", "images/JeanDoggy/Jean_Doggy_Panties_Green_Wet.png",
            "JeanX.Panties == 'green panties'", "images/JeanDoggy/Jean_Doggy_Panties_Green.png",
            "JeanX.Panties == 'lace panties'", "images/JeanDoggy/Jean_Doggy_Panties_Lace.png",
            "JeanX.Panties == 'bikini bottoms' and JeanX.Wet", "images/JeanDoggy/Jean_Doggy_Panties_Bikini_Wet.png",
            "JeanX.Panties == 'bikini bottoms'", "images/JeanDoggy/Jean_Doggy_Panties_Bikini.png",
            "True", "images/JeanDoggy/Jean_Doggy_Panties_Green.png",
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'",Null(),
            "Trigger == 'dildo pussy'", Null(),
#            "JeanX.Panties and JeanX.PantiesDown and JeanX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
#            "JeanX.Hose == 'tights' and JeanX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
#            "JeanX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
            "JeanX.Hose == 'pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full.png",
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "JeanX.Legs == 'pants'", ConditionSwitch(
                    "JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Down.png",
                    "JeanX.Wet > 1", "images/JeanDoggy/Jean_Doggy_Legs_Pants_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Pants.png",
                    ),
            "JeanX.Legs == 'yoga pants'", ConditionSwitch(
                    "JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Down.png",
                    "JeanX.Wet > 1", "images/JeanDoggy/Jean_Doggy_Legs_Yoga_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Yoga.png",
                    ),
            "JeanX.Legs == 'shorts'", ConditionSwitch(
                    "JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Down.png",
                    "JeanX.Wet > 1", "images/JeanDoggy/Jean_Doggy_Legs_Shorts_Wet.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Shorts.png",
                    ),
            "JeanX.Legs == 'skirt'", ConditionSwitch(
                    "JeanX.Upskirt and Player.Sprite and Player.Cock == 'anal' and Speed" , "images/JeanDoggy/Jean_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Legs_Skirt_Up.png",
                    "True", "images/JeanDoggy/Jean_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "JeanX.Over == 'towel' and JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Over_TowelAss_Up.png",
            "JeanX.Over == 'towel'", "images/JeanDoggy/Jean_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in JeanX.Spunk", "images/JeanDoggy/Jean_Doggy_SpunkAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",
            "Trigger == 'lick ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #Hotdogging underlayer
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "JeanX.Legs == 'skirt' and JeanX.Upskirt", "images/JeanDoggy/Jean_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/JeanDoggy/Jean_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            #"JeanX.Legs == 'skirt' and JeanX.Upskirt and Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            #"JeanX.Legs == 'skirt' and JeanX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "Speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),
#        (0,0), ConditionSwitch(
#            #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        )


image Jean_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Jean_Doggy_Shins", "images/JeanDoggy/Jean_Doggy_Feet_Toes.png")

image Jean_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Jean's footjob shins
#    contains:
#        "images/JeanDoggy/Jean_Doggy_Feet_Legs.png"
    contains:
            #hose legs
        ConditionSwitch(
            "JeanX.Hose == 'stockings'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.Hose == 'pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack.png",
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack_Holed.png",
            "True", "images/JeanDoggy/Jean_Doggy_Feet_Legs.png"
            )

    contains:
        #pants
        ConditionSwitch(
            "JeanX.Legs == 'pants'", "images/JeanDoggy/Jean_Doggy_Feet_Pants.png",
            "JeanX.Legs == 'yoga pants'", "images/JeanDoggy/Jean_Doggy_Feet_Yoga.png",
            "True", Null(),
            )
#    contains:
#        "images/JeanDoggy/Jean_Doggy_Feet_Toes.png"
#    contains:
#            #hose toes
#        ConditionSwitch(
#            "not JeanX.Hose", Null(),
#            "JeanX.Hose == 'stockings'", "images/JeanDoggy/Jean_Doggy_Feet_HoseFeet.png",
#            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Feet_HoseFeet.png",
#            "JeanX.Hose == 'pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseFeet.png",
#            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Feet_HoseBack_Holed.png",
#            "True", Null(),
#            )
#    pos (0,0)

#image Jean_Doggy_Lick_Pussy:
#        "Lick_Anim"
#        zoom 0.5
#        offset (195,540)

#image Jean_Doggy_Lick_Ass:
#        "Lick_Anim"
#        zoom 0.5
#        offset (195,500)

image Jean_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (280,380)#(150,340)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

#Hotdogging animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#image Zero_Doggy_Up:
#    #Cock when out (hotdog)
#    contains:
#        ConditionSwitch(
#            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
#            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",
#            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png",
#            ),
#    contains:
#        ConditionSwitch(
#            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
#            "True", Null(),
#            ),

image Zero_Jean_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Jean_Hotdog_Moving:
    # The moving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Insert cock animations
#image Zero_Doggy_Insert:
#    #Insert cock
#    contains:
#        ConditionSwitch(
#            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
#            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",
#            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png",
#            ),
#    contains:
#        ConditionSwitch(
#            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",
#            "True", Null(),
#            ),
#    contains:
#        ConditionSwitch(
#            "Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",
#            "True", Null(),
#            ),

image Zero_Jean_Doggy_Static:
    # Sex Speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 545 #out stroke
            repeat

image Zero_Jean_Doggy_Heading:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat

image Zero_Jean_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jean_Doggy_Fucking3:
    # Sex Speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Jean_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
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
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Jean_Pussy_Moving"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_SexMask.png"
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Pussy fucking animations
#image Jean_Pussy:
#    #Full Animation for speed 0
#    contains:
#        #Base
#        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
#    contains:
#        ConditionSwitch(
#            #full hose/tights
#            "JeanX.PantiesDown", Null(),
#            "JeanX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
#            "JeanX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
##            "JeanX.Hose == 'tights' and JeanX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
##            "JeanX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
##            "JeanX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",
#            "JeanX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
#            "True", Null(),
#            ),
##    contains:
##        #Cock
##        "Zero_Doggy_Insert"
##        pos (169,460) #Out stroke
##    contains:
##        #Masking overlay
##        "images/RogueDoggy/Rogue_Doggy_Pussy_FMask.png"

#    contains:
#        #Cock
#        AlphaMask("Zero_Doggy_Insert", "images/RogueDoggy/Rogue_Doggy_SexMask.png")


image Jean_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:
        #moving hole
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
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jean_Doggy_Static", "Jean_Pussy_Mask_Static")

    contains:
        # expanding pussy flap
        AlphaMask("Jean_PussyHole_Static", "Jean_Pussy_Hole_Mask_Static")

image Jean_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Jean_Pussy_Moving"
    contains:
        #Base
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
    #This is the image impacted by the mask for the pussy flap in "Jean_Pussy_Moving"
    contains:
        #Mask
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
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
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
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jean_Doggy_Heading", "Jean_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Jean_Pussy_Heading_Flap", "Jean_Pussy_Hole_Mask")


image Jean_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Jean_Pussy_Heading"
    contains:
        #Base
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
    #This is the image impacted by the mask for the pussy flap in "Jean_Pussy_Heading"
    contains:
        #Mask
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
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .9#1
            pause 1
            ease 3 xzoom .6
            repeat
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/JeanDoggy/Jean_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Jean_Pussy_Heading_Flap", "Jean_Pussy_Hole_Mask")

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Jean_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
#        AlphaMask("Zero_Jean_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        ConditionSwitch(
            "Trigger == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Jean_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),


image Jean_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jean_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

image Jean_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Jean_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75#1
            pause .5
            ease 1.5 zoom .6
            repeat
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/JeanDoggy/Jean_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock with mask
        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Jean_Anal_Heading:
    #Animation for speed 1
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:
        #Hole
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
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock masking fixer (for when the bottom part tries to cut off)
        AlphaMask("Zero_Jean_Doggy_Anal_Heading", "Zero_Jean_Doggy_Anal_HeadingJunk")
    contains:
        #Cock with mask
        AlphaMask("Zero_Jean_Doggy_Anal_Heading", "Jean_Doggy_Anal_Heading_Mask")

image Zero_Jean_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Jean_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Jean_Doggy_Anal_Heading_Mask:
    #the masking animation for the anal heading
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
#animation for anal fucking top half
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
    #animation for anal fucking ass half
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Jean_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Jean_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
    contains:
        #Cheeks
        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
#        AlphaMask("Zero_Jean_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")
        ConditionSwitch(
            #full hose/tights
            "Trigger == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Jean_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),

image Jean_Doggy_Anal_FullMask:   #unused anymore?
    contains:
        #Mask
        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png" #FullMask?
    contains:
        #Cheeks
        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )

image Jean_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Jean_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Jean_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Jean_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Jean_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Jean_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Base
        "images/JeanDoggy/Jean_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/JeanDoggy/Jean_Doggy_Anal_FullHole.png"
#    contains:
#        #Mask
#        "images/JeanDoggy/Jean_Doggy_Anal_FullMask.png"
    contains:
        #Cheeks
        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JeanX.Hose == 'garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_Garter.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanDoggy/Jean_Doggy_Hose_StockingandGarter.png",
            "JeanX.Panties and JeanX.PantiesDown", Null(),
            "JeanX.Hose == 'ripped pantyhose'", "images/JeanDoggy/Jean_Doggy_Hose_Full_Holed.png",
#            "JeanX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jean_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Jean_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
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
    #animation for anal fucking2 ass half
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


# Footjob animations > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Jean_Doggy_Feet0:
    #static animation
    contains:
        "Jean_Doggy_Shins"
        pos (0, 0) #(0,0) top
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
        pos (160,480)  #(145,480)
    contains:
        "Jean_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Jean_Doggy_Feet1:
    #slow animation
    contains:
        "Jean_Doggy_Shins"
        pos (0, 0) #(0,0) top
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
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Jean_Doggy_Feet2:
    #fast animation
    contains:
        "Jean_Doggy_Shins"
        pos (0, 0) #(0,0) top
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
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Jean_Doggy_Launch(Line = Trigger):
    if renpy.showing("Jean_Doggy_Animation"):
        return
    $ Speed = 0
    call Jean_Hide(1)
    show Jean_Doggy_Animation at sprite_location(StageCenter+50) zorder 150
    with dissolve
    return

label Jean_Doggy_Reset:
    if not renpy.showing("Jean_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ JeanX.ArmPose = 2
    $ JeanX.SpriteVer = 0
    hide Jean_Doggy_Animation
    call Jean_Hide
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return

# End Jean Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jean Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jean Sex element ///////////////////////////////////////////////////////////////////////////

image Jean_SexSprite:
    LiveComposite(
        (1000,1000),
        (0,0), ConditionSwitch(
                #Shows different motion depending on events
                "Trigger == 'lick pussy'", "Jean_Sex_Lick",
                "not Player.Sprite", "Jean_Sex_Static",
                "Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Jean_Sex_Fucking_Speed3",
                        "Speed >= 2", "Jean_Sex_Fucking_Speed2",
                        "Speed", "Jean_Sex_Fucking_Speed1",
                        "True", "Jean_Sex_Fucking_Speed0",
                        ),
                "Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "Speed >= 3", "Jean_Sex_Anal_Speed3",
                        "Speed >= 2", "Jean_Sex_Anal_Speed2",
                        "Speed", "Jean_Sex_Anal_Speed1",
                        "True", "Jean_Sex_Anal_Speed0",
                        ),
                "Player.Sprite and Player.Cock == 'out' and Speed >= 2","Jean_Sex_Hotdog_Speed2",
                "Player.Sprite and Player.Cock == 'out' and Speed >= 1","Jean_Sex_Hotdog_Speed1",
#                "Player.Cock == 'foot'", ConditionSwitch(
#                        #if the top's down. . .
#                        "Speed >= 2", "Jean_Sex_FJ_Speed2",
#                        "Speed", "Jean_Sex_FJ_Speed1",
#                        "True", "Jean_Sex_FJ_Speed0",
#                        ),
#                "Player.Cock == 'out' and Speed >= 2","Jean_Hotdog_Body_Anim2",
                "True", "Jean_Sex_Static",
                ),
        )
    align (0.6,0.0)
    pos (750,230)#(650,393)
    zoom 0.8

image Jean_Sex_HairBack:
    #Hair underlay
    "Jean_BJ_HairBack"
    zoom 0.5#0.48
    anchor (0.5, 0.5)
    rotate 20
    pos (490,320) #(470,380)

image Jean_Sex_Head:
    #Hair underlay
    "Jean_BJ_Head"
    zoom 0.5#0.48
    anchor (0.5, 0.5)
    rotate 20
    pos (490,320) #(470,380)



# Jean's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /

image Jean_Sex_Torso:
    #Her torso for the sex, BJ, and TJ poses
    contains:
            # under tops
        ConditionSwitch(
            "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Over_Back.png",
            "JeanX.Over == 'pink shirt'", "images/JeanSex/Jean_Sex_Over_Back.png",
            "JeanX.Uptop", Null(),
            "JeanX.Chest == 'bikini top' and not JeanX.Over", Null(),
            "not JeanX.Chest and not JeanX.Over", Null(),
            "True", "images/JeanSex/Jean_Sex_Over_Back.png",
            )
    contains:
            # body
            "images/JeanSex/Jean_Sex_Body.png"
#    contains:
#            # piercings tits
#        ConditionSwitch(
#            "(JeanX.Over or JeanX.Chest) and not JeanX.Uptop", Null(),
#            "JeanX.Pierce == 'barbell'", ConditionSwitch(
#                    #if it's the ring pericings
#                    "not JeanX.Chest or JeanX.Uptop", "images/JeanSex/Jean_Pierce_Barbell_Tits_D.png",   # JeanX.TitsUp = 1
#                    "True", Null(),
#                    ),
#            "JeanX.Pierce == 'ring'", ConditionSwitch(
#                    #if it's the ring pericings
#                    "not JeanX.Chest or JeanX.Uptop", "images/JeanSex/Jean_Pierce_Ring_Tits_D.png",   # JeanX.TitsUp = 1
#                    "True", Null(),
#                    ),
#            "True", Null(),
#            )
    contains:
            # bras
        ConditionSwitch(
            "JeanX.Uptop", ConditionSwitch(
                    #if her top's up
                    "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Bra_Sports_Up.png",
                    "JeanX.Chest == 'bikini top'", "images/JeanSex/Jean_Sex_Bra_Bikini_Up.png",
                    "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Up.png",
                    "JeanX.Chest == 'lace bra'", "images/JeanSex/Jean_Sex_Bra_Green_Up.png",
                    "JeanX.Chest", "images/JeanSex/Jean_Sex_Bra_Green_Up.png",
                    "True", Null(),
                    ),
            "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Bra_Sports.png",
            "JeanX.Chest == 'bikini top'", "images/JeanSex/Jean_Sex_Bra_Bikini.png",
            "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset.png",
            "JeanX.Chest == 'lace bra'", "images/JeanSex/Jean_Sex_Bra_Lace.png",
            "JeanX.Chest", "images/JeanSex/Jean_Sex_Bra_Green.png",
            "True", Null(),
            )
    contains:
            # Over clothing layer
        ConditionSwitch(
            "JeanX.Uptop", ConditionSwitch(
                    #if her top's up
                    "JeanX.Over == 'green shirt'", "images/JeanSex/Jean_Sex_Over_Green_Up.png",
                    "JeanX.Over == 'pink shirt'", "images/JeanSex/Jean_Sex_Over_Pink_Up.png",
                    "JeanX.Over == 'yellow shirt'", "images/JeanSex/Jean_Sex_Over_Yellow_Up.png",
                    "True", Null(),
                    ),
            "JeanX.Over == 'green shirt'", "images/JeanSex/Jean_Sex_Over_Green.png",
            "JeanX.Over == 'pink shirt'", "images/JeanSex/Jean_Sex_Over_Pink.png",
            "JeanX.Over == 'yellow shirt'", "images/JeanSex/Jean_Sex_Over_Yellow.png",
            "True", Null(),
            )
    contains:
            # piercings tits over clothes
        ConditionSwitch(
#            "JeanX.Uptop or not JeanX.Pierce", Null(),
            "JeanX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Uptop or (not JeanX.Chest and not JeanX.Over)", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell.png",   # JeanX.TitsUp = 1
                    "JeanX.Over == 'green shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Green.png",
                    "JeanX.Over == 'pink shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Pink.png",
                    "JeanX.Over == 'yellow shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Yellow.png",
                    "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bikini.png",
                    "JeanX.Chest == 'bikini top'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bikini.png",
                    "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Corset.png",
                    "JeanX.Chest", "images/JeanSex/Jean_Sex_Pierce_Tits_Barbell_Bra.png",
                    "True", Null(),
                    ),
            "JeanX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Uptop or (not JeanX.Chest and not JeanX.Over)", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Loose.png",   # JeanX.TitsUp = 1
                    "JeanX.Over == 'green shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Green.png",
                    "JeanX.Over == 'pink shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Pink.png",
                    "JeanX.Over == 'yellow shirt'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Yellow.png",
                    "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bikini.png",
                    "JeanX.Chest == 'bikini top'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bikini.png",
                    "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Corset.png",
                    "JeanX.Chest", "images/JeanSex/Jean_Sex_Pierce_Tits_Ring_Bra.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:
            # spunk on tits
            ConditionSwitch(
                "'tits' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Tits.png",
                )
    contains:
        ConditionSwitch(
            #breast licking animation
#            "(Trigger == 'suck breasts' or Trigger2 == 'suck breasts') and JeanX.Chest and not JeanX.Uptop", "Jean_Sex_Lick_Breasts_High",
            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Jean_Sex_Lick_Breasts",
            "True", Null()
            )
    contains:
        ConditionSwitch(
            #breast fondling animation
            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Jean_Sex_Fondle_Breasts",
            "True", Null()
            )
    zoom 1

image Jean_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (390,600)#(450,270)

image Jean_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (120,-40)#(320,-130)

image Jean_Sex_Body:
    #Her Body in the sex pose
    contains:
            "Jean_Sex_HairBack"
#    contains:
#            # body
#            "Jean_Sex_Torso"
#    contains:
#            # body
#            "images/JeanSex/Jean_Sex_Body.png"
    contains:
            AlphaMask("Jean_Sex_Torso", "images/JeanSex/Jean_Sex_ArmsMask.png")
#    contains:
#            # Arms
#        ConditionSwitch(
#            "JeanX.ArmPose == 3", Null(),   # Neither arms
#            "JeanX.ArmPose == 4", AlphaMask("Jean_SexArms", "images/JeanSex/Jean_Sex_ArmsMask_R.png"),   # Right arm only
#            "JeanX.ArmPose == 5", AlphaMask("Jean_SexArms", "images/JeanSex/Jean_Sex_ArmsMask_L.png"),   # Left arm only
#            "True", AlphaMask("Jean_SexArms", "images/JeanSex/Jean_Sex_ArmsMask.png"),  # Both Arms
#            )
#    contains:
#        ConditionSwitch(
#            #breast licking animation
#            "(Trigger == 'suck breasts' or Trigger2 == 'suck breasts') and JeanX.Chest and not JeanX.Uptop", "Jean_Sex_Lick_Breasts_High",
#            "Trigger == 'suck breasts' or Trigger2 == 'suck breasts'", "Jean_Sex_Lick_Breasts",
#            "True", Null()
#            )
#    contains:
#        ConditionSwitch(
#            #breast fondling animation
#            "Trigger == 'fondle breasts' or Trigger2 == 'fondle breasts'", "Jean_Sex_Fondle_Breasts",
#            "True", Null()
#            )
    contains:
            "Jean_Sex_Head"
    zoom 1.1
    offset (-40,-50) #-100 #(-40,-50)
#    offset (0,0)
# end Jean's sex body torso / / / / / torso / / / / / torso / / / / / torso / / / / / torso / / / / /


#image Jean_SexArms:
#    contains:
#            # Base Arms
#        ConditionSwitch(
#            "JeanX.Over == 'jacket' or JeanX.Over == 'dress'", Null(),
##            "True", "images/JeanSex/Jean_Sex_Arms_Test.png",   # JeanX.TitsUp = 1
#            "JeanX.Chest and not JeanX.Uptop", "images/JeanSex/Jean_Sex_Arms_U.png",   # JeanX.TitsUp = 1
##            "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Arms_U.png",   # JeanX.TitsUp = 1
##            "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Arms_U.png",   # JeanX.TitsUp = 1
##            "JeanX.Chest == 'lace bra'", "images/JeanSex/Jean_Sex_Arms_U.png",   # JeanX.TitsUp = 1
##            "JeanX.Chest == 'bikini top'", "images/JeanSex/Jean_Sex_Arms_U.png",   # JeanX.TitsUp = 1
#            "True", "images/JeanSex/Jean_Sex_Arms_D.png",   # JeanX.TitsUp = 0
#            )
#    contains:
#            # Arm clothing
#        ConditionSwitch(
#            "JeanX.Over == 'jacket' or JeanX.Over == 'dress'", Null(),
#            "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Bra_Sports_Arms.png",   # JeanX.TitsUp = 1
#            "True", Null(),
#            )
##    contains:
##            # Arm clothing
##        ConditionSwitch(
##            "JeanX.Over == 'nighty' and JeanX.Uptop", "images/JeanSex/Jean_Sex_Nighty_Uptop.png",
##            "True", Null(),
##            )
#    contains:
#            # Arm clothing Over
#        ConditionSwitch(
#            "JeanX.Over == 'jacket' and JeanX.Uptop", "images/JeanSex/Jean_Sex_Arms_Jacket_Uptop.png",   # JeanX.TitsUp = 1
#            "JeanX.Over == 'jacket'", "images/JeanSex/Jean_Sex_Arms_Jacket.png",   # JeanX.TitsUp = 1
#            "JeanX.Over == 'dress'", "images/JeanSex/Jean_Sex_Arms_Dress.png",   # JeanX.TitsUp = 1
#            "JeanX.Arms", "images/JeanSex/Jean_Sex_Gloves.png",
#            "True", Null(),
#            )



# Jean's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /
image Jean_Sex_Legs_S:
    #Her Legs during sex
    contains:
            # body
            "images/JeanSex/Jean_Sex_Legs_Sex.png"
    contains:
            # wetness
        ConditionSwitch(
            "JeanX.Wet", "images/JeanSex/Jean_Sex_Wet_Sex.png",
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(
            "'anal' in JeanX.Spunk or 'in' in JeanX.Spunk", "images/JeanSex/Jean_Sex_Spunk_Pussy_S.png",
            "True", Null(),
            )
    contains:
            # stockings
        ConditionSwitch(
            "JeanX.Hose == 'stockings'", "images/JeanSex/Jean_Sex_Hose_Stockings.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanSex/Jean_Sex_Hose_StockingsGarter_S.png",
            "JeanX.Hose == 'garterbelt'", "images/JeanSex/Jean_Sex_Hose_Garter_S.png",
            "True", Null(),
            )
#    contains:
#            # piercings
#        ConditionSwitch(
#            "JeanX.Pierce == 'barbell'", "images/JeanSex/Jean_Pierce_Barbell_Pussy_S.png",
#            "(JeanX.Legs == 'pants' or JeanX.Legs == 'yoga pants') and not JeanX.Upskirt", Null(),
#            "JeanX.Panties and not JeanX.PantiesDown", "images/JeanSex/Jean_Pierce_Ring_Pussy_S_C2.png",
#            "JeanX.Hose == 'pantyhose' and not JeanX.PantiesDown", "images/JeanSex/Jean_Pierce_Ring_Pussy_S_C2.png",
#            "JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Pierce_Ring_Pussy_S.png",
#            "True", Null(),
#            )
    contains:
            # pubes
        ConditionSwitch(
            "JeanX.Pubes", "images/JeanSex/Jean_Sex_Pubes_Sex.png",
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(
#            "JeanX.Hose == 'pantyhose' and not JeanX.PantiesDown", Null(),
            "JeanX.Legs and not JeanX.Upskirt and JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",
            "JeanX.Panties and not JeanX.PantiesDown and JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",
            "JeanX.Hose == 'pantyhose' and not JeanX.PantiesDown and JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex_Clothed.png",
#            "JeanX.Legs or JeanX.Panties or JeanX.Upskirt", Null(),
            "JeanX.Pierce == 'barbell'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Sex.png",
            "JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Sex.png",
            "True", Null(),
            )
    contains:
            # Bra clothing layer
        ConditionSwitch(
            "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Under_S.png",
            "True", Null(),
            )
    contains:
            # Over clothing layer
        ConditionSwitch(
            "JeanX.Over == 'green shirt' and not JeanX.Uptop", "images/JeanSex/Jean_Sex_Over_Green_Under_S.png",
            "JeanX.Over == 'pink shirt'", "images/JeanSex/Jean_Sex_Over_Pink_Under_S.png",
            "True", Null(),
            )
    contains:
            # panties
        ConditionSwitch(
            "JeanX.PantiesDown", Null(),
            "JeanX.Panties == 'lace panties'", "images/JeanSex/Jean_Sex_Panties_Sex_Lace.png",
            "JeanX.Panties == 'bikini bottoms'", "images/JeanSex/Jean_Sex_Panties_Sex_Bikini.png",
            "JeanX.Panties and JeanX.Wet", "images/JeanSex/Jean_Sex_Panties_Sex_Green_W.png",
            "JeanX.Panties", "images/JeanSex/Jean_Sex_Panties_Sex_Green.png",
            "True", Null(),
            )
    contains:
            # pantyhose
        ConditionSwitch(
            "JeanX.PantiesDown", Null(),
#            "JeanX.Hose == 'ripped pantyhose'", "images/JeanSex/Jean_Sex_Hose_PantyhoseHoled_S.png",
#            "Player.Sprite and Player.Cock == 'in'", Null(),
            "JeanX.Hose == 'pantyhose'", "images/JeanSex/Jean_Sex_Hose_Pantyhose_S.png",
            "True", Null(),
            )
#    contains:
#            # piercings
#        ConditionSwitch(
#            "(not JeanX.Panties and JeanX.Hose != 'pantyhose') or JeanX.PantiesDown", Null(),
#            "JeanX.Hose == 'pantyhose' and JeanX.PantiesDown", Null(),
#            "JeanX.Pierce == 'barbell'", "images/JeanSex/Jean_Pierce_Barbell_Pussy_S_C.png",
#            "JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Pierce_Ring_Pussy_S_C.png",
#            "True", Null(),
#            )
    contains:
            # legs
        ConditionSwitch(
            "JeanX.Legs == 'skirt' and JeanX.Upskirt", "images/JeanSex/Jean_Sex_Legs_Sex_Skirt_Up.png",
            "JeanX.Legs == 'skirt'", "images/JeanSex/Jean_Sex_Legs_Sex_Skirt.png",
            "JeanX.Upskirt", Null(),
            "JeanX.Legs == 'pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Pants_W.png",
            "JeanX.Legs == 'pants'", "images/JeanSex/Jean_Sex_Legs_Sex_Pants.png",
            "JeanX.Legs == 'shorts' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Shorts_W.png",
            "JeanX.Legs == 'shorts'", "images/JeanSex/Jean_Sex_Legs_Sex_Shorts.png",
            "JeanX.Legs == 'yoga pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Sex_Yoga_W.png",
            "JeanX.Legs == 'yoga pants'", "images/JeanSex/Jean_Sex_Legs_Sex_Yoga.png",
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(
            "'belly' in JeanX.Spunk", "images/JeanSex/Jean_Sex_Spunk_Belly_S.png",
            "True", Null(),
            )
    zoom 1
#    offset (0,0)

image Jean_Sex_Legs_A:
    #Her Legs during anal
    contains:
            # body
        ConditionSwitch(
            "Trigger == 'lick pussy'", "images/JeanSex/Jean_Sex_Legs_Lick.png",
            "True", "images/JeanSex/Jean_Sex_Legs_Anal.png",
            )
    contains:
            # wetness
        ConditionSwitch(
            "JeanX.Wet", "images/JeanSex/Jean_Sex_Wet_Lick.png",
            "True", Null(),
            )
    contains:
            # anal spunk
        ConditionSwitch(
            "'anal' in JeanX.Spunk and not Speed", "images/JeanSex/Jean_Sex_Spunk_Pussy_S.png",
            "True", Null(),
            )
    contains:
            # pubes
        ConditionSwitch(
            "not JeanX.Pubes", Null(),
            "Trigger == 'lick pussy'", "images/JeanSex/Jean_Sex_Pubes_Lick.png",
            "True", "images/JeanSex/Jean_Sex_Pubes_Anal.png",
            )
    contains:
            # Bra clothing layer
        ConditionSwitch(
            "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Bra_Corset_Under_A.png",
            "True", Null(),
            )
#    contains:
#            # Over clothing layer
#        ConditionSwitch(
#            "JeanX.Over == 'green shirt' and not JeanX.Uptop", "images/JeanSex/Jean_Sex_Over_Green_Under_S.png",
#            "JeanX.Over == 'pink shirt'", "images/JeanSex/Jean_Sex_Over_Pink_Under_S.png",
#            "True", Null(),
#            )
    contains:
            # stockings
        ConditionSwitch(
            "JeanX.Hose == 'stockings'", "images/JeanSex/Jean_Sex_Hose_Stockings.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanSex/Jean_Sex_Hose_StockingsGarter_A.png",
            "JeanX.Hose == 'garterbelt'", "images/JeanSex/Jean_Sex_Hose_Garter_A.png",
            "True", Null(),
            )
    contains:
            # pussy spunk
        ConditionSwitch(
            "'in' in JeanX.Spunk", "images/JeanSex/Jean_Sex_Spunk_Pussy_A.png",
            "True", Null(),
            )
    contains:
            # panties
        ConditionSwitch(
            "JeanX.PantiesDown", Null(),
            "JeanX.Panties == 'lace panties'", "images/JeanSex/Jean_Sex_Panties_Anal_Lace.png",
            "JeanX.Panties == 'bikini bottoms'", "images/JeanSex/Jean_Sex_Panties_Anal_Bikini.png",
            "JeanX.Panties and JeanX.Wet", "images/JeanSex/Jean_Sex_Panties_Anal_Green_W.png",
            "JeanX.Panties", "images/JeanSex/Jean_Sex_Panties_Anal_Green.png",
            "True", Null(),
            )
    contains:
            # piercings over pants
        ConditionSwitch(
            "JeanX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Upskirt or (not JeanX.Legs and not JeanX.Panties)", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",   # JeanX.TitsUp = 1
                    "JeanX.PantiesDown and not JeanX.Legs", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",   # JeanX.TitsUp = 1
                    "JeanX.Panties == 'lace panties'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Lace.png",
                    "JeanX.Panties == 'bikini bottoms'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Bikini.png",
                    "JeanX.Panties", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Green.png",
                    "True", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Anal.png",
                    ),
            "JeanX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Upskirt or (not JeanX.Legs and not JeanX.Panties)", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",   # JeanX.TitsUp = 1
                    "JeanX.PantiesDown and not JeanX.Legs", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",   # JeanX.TitsUp = 1
                    "JeanX.Panties == 'lace panties'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Lace.png",
                    "JeanX.Panties == 'bikini bottoms'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Bikini.png",
                    "JeanX.Panties", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Green.png",
                    "True", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Anal.png",
                    ),
            "True", Null(),
            )
    contains:
            # pantyhose
        ConditionSwitch(
            "(JeanX.Panties and JeanX.PantiesDown)", Null(),
#            "JeanX.Hose == 'ripped pantyhose'", "images/JeanSex/Jean_Sex_Hose_PantyhoseHoled_A.png",
#            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "JeanX.Hose == 'pantyhose'", "images/JeanSex/Jean_Sex_Hose_Pantyhose_A.png",
            "True", Null(),
            )
    contains:
            # legs
        ConditionSwitch(
            "JeanX.Legs == 'skirt' and JeanX.Upskirt", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt_Up.png",
            "JeanX.Legs == 'skirt' and Trigger == 'hotdog'", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt_Up.png",
            "JeanX.Legs == 'skirt'", "images/JeanSex/Jean_Sex_Legs_Anal_Skirt.png",
            "JeanX.Upskirt", Null(),
            "JeanX.Legs == 'pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Pants_W.png",
            "JeanX.Legs == 'pants'", "images/JeanSex/Jean_Sex_Legs_Anal_Pants.png",
            "JeanX.Legs == 'shorts' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Shorts_W.png",
            "JeanX.Legs == 'shorts'", "images/JeanSex/Jean_Sex_Legs_Anal_Shorts.png",
            "JeanX.Legs == 'yoga pants' and JeanX.Wet >=2", "images/JeanSex/Jean_Sex_Legs_Anal_Yoga_W.png",
            "JeanX.Legs == 'yoga pants'", "images/JeanSex/Jean_Sex_Legs_Anal_Yoga.png",
            "True", Null(),
            )
    contains:
            # piercings over pants
        ConditionSwitch(
            "JeanX.Hose == 'pantyhose' and not JeanX.PantiesDown", Null(),
            "JeanX.Legs and not JeanX.Upskirt and JeanX.Wet >=2", Null(),
            "JeanX.Pierce == 'barbell'", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Upskirt or (not JeanX.Legs and not JeanX.Panties)", Null(),   # JeanX.TitsUp = 1
                    "JeanX.Legs == 'skirt' and not JeanX.Upskirt", Null(),
                    "JeanX.Legs == 'pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Pants.png",
                    "JeanX.Legs == 'shorts'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Shorts.png",
                    "JeanX.Legs == 'yoga pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Barbell_Yoga.png",
                    "True", Null(),
                    ),
            "JeanX.Pierce == 'ring'", ConditionSwitch(
                    #if it's the ring pericings
                    "JeanX.Upskirt or (not JeanX.Legs and not JeanX.Panties)", Null(),   # JeanX.TitsUp = 1
                    "JeanX.Legs == 'skirt' and not JeanX.Upskirt", Null(),
                    "JeanX.Legs == 'pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Pants.png",
                    "JeanX.Legs == 'shorts'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Shorts.png",
                    "JeanX.Legs == 'yoga pants'", "images/JeanSex/Jean_Sex_Pierce_Pussy_Ring_Yoga.png",
                    "True", Null(),
                    ),
            "True", Null(),
            )
    contains:
            # spunk
        ConditionSwitch(
            "'belly' in JeanX.Spunk", "images/JeanSex/Jean_Sex_Spunk_Belly_A.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "Trigger == 'lick pussy'", "Jean_Sex_Lick_Pussy",
            "Trigger == 'lick ass'", "Jean_Sex_Lick_Ass",
            "True", Null()
            )
    zoom 1
#    offset (0,0)

# Jean's sex body legs / / / / / legs / / / / / legs / / / / / legs / / / / / legs / / / / /

#  Sex animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Body_Lick:
    #Her Body in the licking pose
    contains:
        "Jean_Sex_Body"
        subpixel True
        pos (0,-80) #top (0,-40)
        block:
            ease 1 pos (0,-90) #bottom   (0,-20)
            ease 1 pos (0,-80) #top
            repeat

image Jean_Sex_Legs_Lick:
    # Her Legs in the anal pose, idle
    contains:
            #Base Legs
            "Jean_Sex_Legs_A"
            subpixel True
            pos (0,-40) #top (0,-138)
            block:
                ease 1 ypos -45 #bottom -15
                ease 1 ypos -40 #top -10
                repeat
    # End Sex Legs Anal Idle

image Jean_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (500,680) #(505,680)

image Jean_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (500,740) # (535,590)


image Jean_Sex_Zero_Cock:
        #this is the cock generally used by Jean's sex pose
        contains:
            subpixel True
#            "Zero_Blowcock"
            ConditionSwitch(
                "Player.Sprite", "Zero_Blowcock" ,
                "True", Null(),
                )
            subpixel True
            anchor (0.5,1.0)
            transform_anchor True
            offset (485,1000) #(546,1007)
            zoom 0.48

# Start Jean Sex Pose Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Static:
    # Pose for Jean's Sex Pose in which she is static
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_S"
            pos (0,-190) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -180 #0 240
                pause 0.8
                ease 2 ypos -190 #top 250
                repeat
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -190 #0
                pause 0.8
                ease 2 ypos -200 #-130
                pause 0.2
                repeat
# End main animation for Sex Pose Static

# End Jean Sex Pose Speed Static / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jean Sex Pose Lick / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Lick:
    # Pose for Jean's Sex Pose in which she is being licked
#    contains:
#            #Zero's cock
#            subpixel True
#            "Jean_Sex_Zero_Cock"
#            pos (0,0) #X less is left, Y less is up
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_A"
            pos (0,-190) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -180 #0 240
                pause 0.8
                ease 2 ypos -190 #top 250
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-230) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -220 #-190
                pause 0.8
                ease 2 ypos -230 #-200
                pause 0.2
                repeat
    zoom 1.8
    offset (-500,-400)#(-600,-550)#(-300,-300)
# End main animation for Sex Pose Lick

# End Jean Sex Pose Speed Lick / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jean Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jean Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Fucking_Speed0:
    # Pose for Jean's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_S"
            pos (0,-250) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -240 #0
                pause 0.8
                ease 2 ypos -250 #top
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -190 #0
                pause 0.8
                ease 2 ypos -200 #-130
                pause 0.2
                repeat

# End Jean Sex Pose Speed 0 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jean Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jean Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Fucking_Speed1:
    # Pose for Jean's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            block: #adds to 5
                pause 1.2
                ease 1 ypos 20 #0
                pause 1.1
                ease 1.1 ypos -10 #-130
                pause 0.1
                ease .5 ypos 0 #-130
                repeat
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_S"
            pos (0,-250) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -200 #0
                pause 0.8
                ease 2 ypos -250 #top
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-220) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -190 #0
                pause 0.8
                ease 2 ypos -220 #-200
                pause 0.2
                repeat

# End Jean Sex Pose Speed 1 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jean Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jean Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Fucking_Speed2:
    # Pose for Jean's Sex Pose in which she is fucking at speed 2 (deep)
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos 20 #0
                pause 0.8
                ease 1.5 ypos 0 #-130
                pause 0.5
                repeat
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_S"
            pos (0,-200) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -80 #bottom
                pause 0.8
                ease 2 ypos -200 #top
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-180) #X less is left, Y less is up
            block: #adds to 5
                easeout 0.5 ypos -160 #bottom -160
                easein 1.5 ypos -80 #bottom -100
                pause 0.8
                easeout 1 ypos -130 #top -130
                easein 1 ypos -180 #top -180
                pause 0.2
                repeat


# End Jean Sex Pose Speed 2 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jean Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jean Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Fucking_Speed3:
    # Pose for Jean's Sex Pose in which she is fucking at speed 3 (fast)
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            block: #adds to 5
                pause 0.3
                ease 0.3 ypos 20 #0
                pause 0.3
                ease 0.5 ypos 0 #-130
                pause 0.5
                repeat
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_S"
            pos (0,-200) #X less is left, Y more is up
            block: #adds to 5
                pause 0.1
                ease 0.5 ypos -100 #bottom
                pause 0.2
                ease 1.0 ypos -200 #top
                pause 0.1
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-140) #X less is left, Y less is up
            block: #adds to 5
                ease 0.6 ypos -60 #bottom -190
                pause 0.2
                easeout 0.7 ypos -140 #top
                easein 0.4 ypos -150 #top
                repeat


# End Jean Sex Pose Speed 3 Fucking / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Start Animations for Jean's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Jean's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Anal_Spunk_Heading_Over:
    "images/JeanSex/Jean_Sex_Spunk_Anal_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8
    block:
        #total 5 second
        ease .75 xzoom 1.0   #(1.0)
        pause 1.75
        ease .25 xzoom 1.0  #(1.0)
        ease 2.25 xzoom 0.8   #(0.6)
        repeat
image Jean_Sex_Anal_Spunk_Heading_Under:
    "images/JeanSex/Jean_Sex_Spunk_Anal_Under.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.95
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Jean_Sex_Anal_Mask:
        #This is the mask image for Kitty's wide open pussy
        # Used in "Jean_Sex_Speed2" and "Jean_Sex_Speed3"
        contains:
            "images/JeanSex/Jean_Sex_Mask_Anal.png"
            yoffset 3

# Start Jean Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Anal_Speed0:
    # Pose for Jean's Sex Pose in which she is fucking at speed 0 (static)
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_A"
            pos (0,-250) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -240 #0
                pause 0.8
                ease 2 ypos -250 #top
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-280) #X less is left, Y less is down
            block: #adds to 5
                ease 2 ypos -270 #-240
                pause 0.8
                ease 2 ypos -280 #-250
                pause 0.2
                repeat

# End Jean Sex Pose Speed 0 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jean Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Anal_Speed1:
    # Pose for Jean's Sex Pose in which she is fucking at speed 1 (heading)
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            block: #adds to 5
                pause 1.2
                ease 1 ypos 20 #0
                pause 1.1
                ease 1.1 ypos -10 #-130
                pause 0.1
                ease .5 ypos 0 #-130
                repeat
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_A"
            pos (0,-250) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -200 #0
                pause 0.8
                ease 2 ypos -250 #top
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-250) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -220 #-190
                pause 0.8
                ease 2 ypos -250 #-200
                pause 0.2
                repeat

# End Jean Sex Pose Speed 1 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jean Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Anal_Speed2:
    # Pose for Jean's Sex Pose in which she is doing anal at speed 2
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos 20 #0
                pause 0.8
                ease 1.5 ypos 0 #-130
                pause 0.5
                repeat
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_A"
            pos (0,-200) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -80 #bottom
                pause 0.8
                ease 2 ypos -200 #top
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
                ease 2 ypos -100 #bottom -100
                pause 0.8
                ease 2 ypos -200 #top -180
                pause 0.2
                repeat

# End Jean Sex Pose Speed 2 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jean Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Anal_Speed3:
    # Pose for Jean's Sex Pose in which she is Anal at speed 3
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            block: #adds to 5
                pause 0.3
                ease 0.3 ypos 20 #0
                pause 0.3
                ease 0.5 ypos 0 #-130
                pause 0.5
                repeat
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_A"
            pos (0,-200) #X less is left, Y more is up
            block: #adds to 5
                pause 0.1
                ease 0.5 ypos -100 #bottom
                pause 0.2
                ease 1.0 ypos -200 #top
                pause 0.1
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-190) #X less is left, Y less is up
            block: #adds to 5
                ease 0.6 ypos -120 #bottom -60
                pause 0.1

                ease 1.2 ypos -190 #top -180

#                easeout 0.7 ypos -180 #top -170
#                easein 0.4 ypos -190 #top -180
                repeat

# End Jean Sex Pose Speed 3 Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Start Jean Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Jean Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Hotdog_Speed1:
    # Pose for Jean's Sex Pose in which she is doing Hotdog at speed 1
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_A"
            pos (0,-200) #X less is left, Y more is up
            block: #adds to 5
                pause 0.2
                ease 2 ypos -80 #bottom
                pause 0.8
                ease 2 ypos -200 #top
                repeat
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            alpha 0.8
            block: #adds to 5
                pause 0.7
                ease 1.5 ypos 20#0
                pause 0.8
                ease 1.5 ypos 0#-130
                pause 0.5
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-200) #X less is left, Y less is up
            block: #adds to 5
#                easeout 1 ypos -160 #bottom -160
#                easein 1 ypos -100 #bottom -100
#                pause 0.8
#                easeout 1 ypos -130 #top -130
#                easein 1 ypos -180 #top -180
#                pause 0.2

                ease 2 ypos -100 #bottom -100
                pause 0.8
                ease 2 ypos -200 #top -180
                pause 0.2
                repeat

# End Jean Sex Pose Speed 1 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Jean Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Sex_Hotdog_Speed2:
    # Pose for Jean's Sex Pose in which she is Hotdog at speed 2
    contains:
            #Jean's Legs
            subpixel True
            "Jean_Sex_Legs_A"
            pos (0,-200) #X less is left, Y more is up
            block: #adds to 5
                pause 0.1
                ease 0.5 ypos -100 #bottom
                pause 0.2
                ease 1.0 ypos -200 #top
                pause 0.1
                repeat
    contains:
            #Zero's cock
            subpixel True
            "Jean_Sex_Zero_Cock"
            pos (0,0) #X less is left, Y less is up
            alpha 0.8
            block: #adds to 5
                pause 0.3
                ease 0.3 ypos 20 #0
                pause 0.3
                ease 0.5 ypos 0 #-130
                pause 0.5
                repeat
    contains:
            #Jean's underlying body
            subpixel True
            "Jean_Sex_Body"
            pos (0,-190) #X less is left, Y less is up
            block: #adds to 5
                ease 0.6 ypos -120 #bottom -60
                pause 0.1
                ease 1.2 ypos -190 #top -180

#                easeout 0.7 ypos -170 #top -140
#                easein 0.4 ypos -180 #top -150
                repeat

# End Jean Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# End Jean Sex Pose Speed 2 Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jean_Sex_Launch(Line = Trigger):
        $ Trigger3 = 0 if Trigger3 == "hand" else Trigger3
#        #temporary      #temporary      #temporary      #temporary      #temporary      #temporary
#        $ JeanX.Pose = "doggy"
#        #temporary      #temporary      #temporary      #temporary      #temporary      #temporary

        $ Player.Sprite = 1
        $ Line = "solo" if not Line else Line
        if Line == "sex":
            $ Player.Cock = "in"
            if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                    $ Trigger2 = 0
        elif Line == "anal":
            $ Player.Cock = "anal"
            if Trigger2 in ("insert ass","dildo anal","lick ass"):
                    $ Trigger2 = 0
        elif Line == "hotdog":
            if JeanX.PantsNum() == 5: #upskirts her if she's in a skirt
                    $ JeanX.Upskirt = 1
            $ Player.Cock = "out"
        elif Line == "foot":
            $ ShowFeet = 1
            $ Player.Cock = "foot"
            $ JeanX.Pose = "doggy"
        elif Line == "massage":
            $ Player.Sprite = 0
            $ Player.Cock = 0
        else: #elif Line == "solo":
            $ Player.Sprite = 0
            $ Player.Cock = "out"
            $ Speed = 0
        $ Trigger = Line

        if JeanX.Pose == "doggy":
                call Jean_Doggy_Launch(Line)
                return
        if renpy.showing("Jean_SexSprite"):
                return
        $ Speed = 0
        call Jean_Hide(1)
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
        show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
            alpha 1
            zoom 1 offset (0,0)
            anchor (0.5, 0.0)
        with dissolve
        $ Speed = 0
        return




# Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jean_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (-270,-160), ConditionSwitch( #-270,-160
            # Jean's hair backside
            "Speed == 0", At("Jean_BJ_HairBack", Jean_BJ_Head_0()),               #Static
            "Speed == 1", At("Jean_BJ_HairBack", Jean_BJ_Head_1()),               #Licking
            "Speed == 2", At("Jean_BJ_HairBack", Jean_BJ_Head_2()),               #Heading
            "Speed == 3", At("Jean_BJ_HairBack", Jean_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Jean_BJ_HairBack", Jean_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Jean_BJ_HairBack", Jean_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Jean_BJ_HairBack", Jean_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),
        (-20,270), ConditionSwitch(
            # Jean's body, everything below the chin
            "Speed == 0", At("Jean_BJ_Backdrop", Jean_BJ_Body_0()),           #Static
            "Speed == 1", At("Jean_BJ_Backdrop", Jean_BJ_Body_1()),           #Licking
            "Speed == 2", At("Jean_BJ_Backdrop", Jean_BJ_Body_2()),           #Heading
            "Speed == 3", At("Jean_BJ_Backdrop", Jean_BJ_Body_3()),           #Sucking
            "Speed == 4", At("Jean_BJ_Backdrop", Jean_BJ_Body_4()),           #Deepthroat
            "Speed == 5", At("Jean_BJ_Backdrop", Jean_BJ_Body_5()),           #Cumming High
            "Speed == 6", At("Jean_BJ_Backdrop", Jean_BJ_Body_6()),           #Cumming Deep
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # Jean's head Underlay
            "Speed == 0", At("Jean_BJ_Head", Jean_BJ_Head_0()),               #Static
            "Speed == 1", At("Jean_BJ_Head", Jean_BJ_Head_1()),               #Licking
            "Speed == 2", At("Jean_BJ_Head", Jean_BJ_Head_2()),               #Heading
            "Speed == 3", At("Jean_BJ_Head", Jean_BJ_Head_3()),               #Sucking
            "Speed == 4", At("Jean_BJ_Head", Jean_BJ_Head_4()),               #Deepthroat
            "Speed == 5", At("Jean_BJ_Head", Jean_BJ_Head_5()),               #Cumming High
            "Speed == 6", At("Jean_BJ_Head", Jean_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # Cock
            "Speed == 0", At("Blowcock", Jean_BJ_Cock_0()),                    #Static
            "Speed == 1", At("Blowcock", Jean_BJ_Cock_1()),                    #Licking
            "Speed >= 2", At("Blowcock", Jean_BJ_Cock_2()),                    #Heading+
#            "Speed == 2", At("Blowcock", Jean_BJ_Cock_2()),                    #Heading
#            "Speed == 3", At("Blowcock", Jean_BJ_Cock_2()),                    #Sucking
#            "Speed == 4", At("Blowcock", Jean_BJ_Cock_2()),                    #Deepthroat
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(),
            "Speed == 3", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MouthSuckingMask"), Jean_BJ_Head_3()), #Sucking
            "Speed == 4", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MouthSuckingMask"), Jean_BJ_Head_4()), #Deepthroat
            "Speed == 6", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MouthSuckingMask"), Jean_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MaskHeadingComposite"), Jean_BJ_Head_2()), #Heading
            "Speed == 5", At(AlphaMask("Jean_BJ_Head", "Jean_BJ_MaskHeadingComposite"), Jean_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),
        (325,490), ConditionSwitch(
            # the over part of spunk
            "Speed < 3 or 'mouth' not in JeanX.Spunk", Null(),
            "Speed == 3", At("JeanSuckingSpunk", Jean_BJ_Head_3()), #Sucking
            "Speed == 4", At("JeanSuckingSpunk", Jean_BJ_Head_4()), #Deepthroat
            "Speed == 6", At("JeanSuckingSpunk", Jean_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),
#        (325,490), ConditionSwitch(         #(325,490)
#            # same as above, but for the heading animation
#            "True", At("Jean_BJ_MaskHeadingSpunk", Jean_BJ_Head_2()), #Heading
#            "Speed == 2 and 'mouth' in JeanX.Spunk", At("Jean_BJ_MaskHeadingSpunk", Jean_BJ_Head_2()), #Heading
##            "Speed == 5 and 'mouth' in JeanX.Spunk", At("Jean_BJ_MaskHeadingSpunkB", Jean_BJ_Head_5()), #Cumming High
#            "True", Null(),
#            ),
        )
    zoom .55
    anchor (.5,.5)

image Jean_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(
            "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Under.png",
            "JeanX.Hair == 'pony'", Null(),
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Under.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Jean_BJ_HairTop:
    #Hair underlay
    ConditionSwitch(
            "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
            "True", Null(), #"images/JeanBJFace/Jean_BJ_Hair_Short_Over.png",
            ),
    zoom 1.4
    anchor (0.5, 0.5)

image Jean_BJ_Backdrop1: #delete if other works better. . .
    contains:
            #blanket
            ConditionSwitch(
                "'blanket' in JeanX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                ),
            zoom 2
            anchor (.5,.5)
            pos (350,600)
#    contains:
#            #body backdrop
#            "Jean_Sex_Torso"
#            zoom 2.5
#            anchor (.5,.5)
#            pos (160,750)
#    zoom 1.5
#    offset (-300,-200)

image Jean_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            # hair underlayer in normal mode
            "(JeanX.Water or JeanX.Hair == 'wet') and renpy.showing('Jean_SexSprite')", "images/JeanBJFace/Jean_BJ_Hair_Wet_Mid.png",
            "JeanX.Water or JeanX.Hair == 'wet'", Null(),
            "JeanX.Hair == 'pony'", Null(),
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Under.png",
            ),




        (0,0), ConditionSwitch(
            # Basic Face layer
#            "Speed <= 2 or Speed == 5 or not renpy.showing('Jean_BJ_Animation')", ConditionSwitch(
#                    # If the animation isn't sucking, or if not in BJ pose
#                    "JeanX.Blush", "images/JeanBJFace/Jean_BJ_FaceClosed_Blush.png",
#                    "True", "images/JeanBJFace/Jean_BJ_FaceClosed.png",
#                    ),
            "JeanX.Blush > 1", "images/JeanBJFace/Jean_BJ_Head_Blush2.png",
            "JeanX.Blush", "images/JeanBJFace/Jean_BJ_Head_Blush1.png",
            "True", "images/JeanBJFace/Jean_BJ_Head_Blush0.png"
            ),
        (0,0), ConditionSwitch(
            #Mouth
#            "(Speed == 2 or Speed == 5) and renpy.showing('Jean_BJ_Animation')", ConditionSwitch(
#                    # If the Heading animation is active
##                    "JeanX.Blush", "images/JeanBJFace/Jean_BJ_FaceClosed_Blush.png",
##                    "True", "images/JeanBJFace/Jean_BJ_FaceClosed.png"
#                    ),
            "Speed and renpy.showing('Jean_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png", #sucking
                    "Speed == 4", "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png", #deepthroat
                    "Speed == 6", "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png", #cumming
                    ),
            "Speed == 3 and renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",
            "JeanX.Mouth == 'normal'", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            "JeanX.Mouth == 'lipbite'", "images/JeanBJFace/Jean_BJ_Mouth_Lipbite.png",
            "JeanX.Mouth == 'sucking'", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",
            "JeanX.Mouth == 'kiss'", "images/JeanBJFace/Jean_BJ_Mouth_Kiss.png",
            "JeanX.Mouth == 'sad'", "images/JeanBJFace/Jean_BJ_Mouth_Sad.png",
            "JeanX.Mouth == 'smile'", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            "JeanX.Mouth == 'smirk'", "images/JeanBJFace/Jean_BJ_Mouth_Smirk.png",
            "JeanX.Mouth == 'grimace'", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            "JeanX.Mouth == 'surprised'", "images/JeanBJFace/Jean_BJ_Mouth_Kiss.png",
            "JeanX.Mouth == 'tongue'", "images/JeanBJFace/Jean_BJ_Mouth_Tongue.png",
            "True", "images/JeanBJFace/Jean_BJ_Mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(
            # Heading Mouth
#            "Speed == 2 and Trigger == 'blow'", At("Jean_BJ_MouthHeading", Jean_BJ_MouthAnim()),  #heading
            "not renpy.showing('Jean_BJ_Animation')", Null(),                       #heading
            "Speed == 2", At("Jean_BJ_MouthHeading", Jean_BJ_MouthAnim()),  #heading
            "Speed == 5", At("Jean_BJ_MouthHeading", Jean_BJ_MouthAnimC()), #cumming high
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in JeanX.Spunk", Null(),
            "Speed and renpy.showing('Jean_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "Speed == 1", "images/JeanBJFace/Jean_BJ_Spunk_Tongue.png",  #licking
                    "(Speed == 2 or Speed == 5)", Null(),                          #heading
                    "Speed == 3", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png", #sucking
                    "Speed == 4", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png", #deepthroat
                    "Speed == 6", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png", #cumming
                    ),
            "JeanX.Mouth == 'normal'", "images/JeanBJFace/Jean_BJ_Spunk_Smile.png",
#            "JeanX.Mouth == 'lipbite'", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
#            "JeanX.Mouth == 'kiss'", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
#            "JeanX.Mouth == 'sad'", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
            "JeanX.Mouth == 'smile'", "images/JeanBJFace/Jean_BJ_Spunk_Smile.png",
#            "JeanX.Mouth == 'smirk'", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
#            "JeanX.Mouth == 'surprised'", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
            "JeanX.Mouth == 'tongue'", "images/JeanBJFace/Jean_BJ_Spunk_Tongue.png",
            "JeanX.Mouth == 'sucking'", "images/JeanBJFace/Jean_BJ_Spunk_SuckingUnder.png",
            "True", "images/JeanBJFace/Jean_BJ_Spunk_Kiss.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            "JeanX.Brows == 'normal'", "images/JeanBJFace/Jean_BJ_Brows_Normal.png",
            "JeanX.Brows == 'angry'", "images/JeanBJFace/Jean_BJ_Brows_Angry.png",
            "JeanX.Brows == 'sad'", "images/JeanBJFace/Jean_BJ_Brows_Sad.png",
            "JeanX.Brows == 'surprised'", "images/JeanBJFace/Jean_BJ_Brows_Surprised.png",
            "JeanX.Brows == 'confused'", "images/JeanBJFace/Jean_BJ_Brows_Confused.png",
            "True", "images/JeanBJFace/Jean_BJ_Brows_Normal.png",
            ),
        (0,0), "Jean BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #Hair overlay
            "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
            "JeanX.Hair == 'pony'", "images/JeanBJFace/Jean_BJ_Hair_Pony_Over.png",
            "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Over.png",
            ),
#        (0,0), ConditionSwitch(
#            #Hair water overlay
#            "not JeanX.Water", Null(),
#            "Speed > 2", "images/JeanBJFace/Jean_BJ_Wet_HeadOpen.png",
#            "True", "images/JeanBJFace/Jean_BJ_Wet_HeadClosed.png",
#            ),
#        (0,0), ConditionSwitch(
#            #cum on the hair
#            "'hair' in JeanX.Spunk", "images/JeanBJFace/Jean_BJ_Spunk_Hair.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #cum on the face
            "'hair' in JeanX.Spunk", "images/JeanBJFace/Jean_BJ_Spunk_Facial2.png",
            "'facial' in JeanX.Spunk", "images/JeanBJFace/Jean_BJ_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)


image Jean BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "JeanX.Eyes == 'normal'", "images/JeanBJFace/Jean_BJ_Eyes_Normal.png",
            "JeanX.Eyes == 'sexy'", "images/JeanBJFace/Jean_BJ_Eyes_Sexy.png",
            "JeanX.Eyes == 'closed'", "images/JeanBJFace/Jean_BJ_Eyes_Closed.png",
            "JeanX.Eyes == 'surprised'", "images/JeanBJFace/Jean_BJ_Eyes_Surprised.png",
            "JeanX.Eyes == 'side'", "images/JeanBJFace/Jean_BJ_Eyes_Side.png",
            "JeanX.Eyes == 'stunned'", "images/JeanBJFace/Jean_BJ_Eyes_Stunned.png",
            "JeanX.Eyes == 'down'", "images/JeanBJFace/Jean_BJ_Eyes_Down.png",
            "JeanX.Eyes == 'manic'", "images/JeanBJFace/Jean_BJ_Eyes_Surprised.png",
            "JeanX.Eyes == 'squint'", "images/JeanBJFace/Jean_BJ_Eyes_Sexy.png",
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
    #the mouth used for the heading animations
    contains:
        "images/JeanBJFace/Jean_BJ_Mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)  #(0.50,0.65)

image Jean_BJ_MouthSuckingMask:
    #the mask used for sucking animations
    contains:
        "images/JeanBJFace/Jean_BJ_Mouth_MaskS.png"
        zoom 1.4
#    contains: #see if this works, if not remove it
#        ConditionSwitch(
#            "'mouth' not in JeanX.Spunk", Null(),
#            "Speed != 2 and Speed != 5", Null(),
#            "True", "images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png",
#            )
#        zoom 1.4

image Jean_BJ_MaskHeading:
    #the mask used for the heading image
    contains:
        "images/JeanBJFace/Jean_BJ_Mouth_MaskH.png"
        offset (-380,-595)

image Jean_BJ_MaskHeadingComposite:
    #The composite for the heading mask that goes over the face
    LiveComposite(
        (858,928),
        (300,462), ConditionSwitch(
            "Speed == 2", At("Jean_BJ_MaskHeading", Jean_BJ_MouthAnim()),
            "Speed == 5", At("Jean_BJ_MaskHeading", Jean_BJ_MouthAnimC()),
            "True", Null(),
            ),
        )
    zoom 1.8

image Jean_BJ_MaskHeadingSpunk:
    #The composite for the heading mask that goes over the face
    contains:
#            "JeanSuckingSpunk"
            ConditionSwitch(
                    "Speed == 2", "images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png",
                    "True", Null(),
                    )

            #"images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png"
            subpixel True
            anchor (0.5, 0.65)
            zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
            block: #total time 1.0 down, 1.5 back up 2.5 total
                pause .20
                easeout .15 zoom 0.66
                linear .15 zoom 0.60
                easein .25 zoom 0.68
                pause .25
                #1.0s to this point
                pause .40
                easeout .40 zoom 0.60
                linear .10 zoom 0.66
                easein .30 zoom 0.58
                pause .30
                #1.5s to this point
                repeat
#    contains:
#            At("JeanSuckingSpunk", Jean_BJ_MouthAnim())
    zoom 1.8 #2.5 #1.8
    yoffset 180#210#130

image JeanSuckingSpunk:
    contains:
        "images/JeanBJFace/Jean_BJ_Spunk_SuckingOver.png"
        zoom 1.4
        anchor (0.5, 0.5)

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_BJ_Backdrop:
        #Her Body in the BJ pose
        contains:
            #blanket
            ConditionSwitch(
                "'blanket' in JeanX.RecentActions", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
                "True", Null(),
                )
            zoom 1.2
            anchor (.5,.5)
            pos (180,-400)
#            block:
#                ease 1 pos (0,-600)
#                ease 1 pos (-350,0)
#                ease 1 pos (-350,0)
#                ease 1 pos (-350,-600)
#                repeat
        contains:
                #bra strap backing
                "Jean_TJ_Braback"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos -0
#                    pause .1
#                    repeat
        contains:
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jean_TJ_Body"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos 0
#                    pause .1
#                    repeat
        contains:
                #right hand backside
                "Jean_TJ_TitR"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos -0
#                    pause .1
#                    repeat
        contains:
                "Jean_TJ_Tits"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
#                parallel:
#                    ease 2 ypos -20
#                    pause .1
#                    ease 2 ypos -0
#                    pause .1
#                    repeat
        zoom 1.4
        offset (225,1100)

# End Jean BJ Body / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


transform Jean_BJ_MouthAnim():
        #The animation for the heading mouth
        subpixel True
        zoom 0.58 #0.58 = top of heading, 0.66 = crown, 0.60 = valley, 0.68 = base
        block: #total time 1.0 down, 1.5 back up 2.5 total
            pause .20
            easeout .15 zoom 0.66
            linear .15 zoom 0.60
            easein .25 zoom 0.68
            pause .25
            #1.0s to this point
            pause .40
            easeout .40 zoom 0.60
            linear .10 zoom 0.66
            easein .30 zoom 0.58
            pause .30
            #1.5s to this point
            repeat


#            pause .40
#            easein .40 zoom 0.69 #0.87
#            linear .10 zoom 0.7 #0.9
#            easeout .45 zoom 0.65 #0.70
#            pause .15
#            #1.5s to this point
#            easein .25 zoom 0.7#0.9
#            linear .10 zoom 0.69#0.87
#            easeout .30 zoom 0.7#0.9
#            pause .35
#            #1.0s to this point
#            repeat

transform Jean_BJ_Head_2():
    #The heading animation for her face
    subpixel True
    offset (0,-40)     #top (0,-40), -20 is crown, 0 is mid
    block:
        ease 1 yoffset 40           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat


#        ease 1 yoffset 35           #bottom
#        ease 1.5 offset (0,-40)     #top
#        repeat

transform Jean_BJ_MouthAnimC():
        #The animation for the heading mouth
        subpixel True
        zoom 0.7 #0.90
        block: #total time 10 down, 15 back up
            pause .20
            ease .50 zoom 0.65 #0.87
            pause .60
            ease .30 zoom 0.7#0.9
            pause .10
            ease .30 zoom 0.65#0.9
            pause .20
            ease .30 zoom 0.7#0.9
            repeat


#Cock Animations for Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Jean_BJ_Cock_0():
    #The angled static animation for the cock for starting
    anchor (.5,.5)
    rotate -10
transform Jean_BJ_Cock_1():
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat
transform Jean_BJ_Cock_2():
    #The vertical static animation for the cock used in most sucking
    anchor (.5,.5)
    rotate 0
    alpha 1
#End Cock Animations for Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Head and Body Animations for Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Jean_BJ_Head_0():
    #The starting animation for her face
    subpixel True
    ease 1.5 offset (0,0)
transform Jean_BJ_Body_0():
    #The starting animation for her body
    subpixel True
    ease 1.5 offset (0,0)


transform Jean_BJ_Head_1():
    #The licking animation for her face
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
transform Jean_BJ_Body_1():
    #The licking animation for her body
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

#transform Jean_BJ_Head_2():
#    #The heading animation for her face
#    subpixel True
#    offset (0,-40)     #top
#    block:
#        ease 1 yoffset 35           #bottom
#        ease 1.5 offset (0,-40)     #top
#        repeat
##        ease 1 yoffset 35           #bottom
##        ease 1.5 offset (0,-40)     #top
##        repeat

transform Jean_BJ_Body_2():
    #The heading animation for her body
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 15           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat

transform Jean_BJ_Head_3():
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50)
        repeat
transform Jean_BJ_Body_3():
    #The sucking animation for her body
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat

transform Jean_BJ_Head_4():
    #The deep animation for her face
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat
transform Jean_BJ_Body_4():
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Jean_BJ_Head_5():
    #The heading cumming animation for her face
    subpixel True
    offset (0,-30)     #top
    block:
        ease 1 yoffset -20           #bottom
        ease 1.5 offset (0,-30)     #top
        repeat
transform Jean_BJ_Body_5():
    #The heading cumming animation for her body
    subpixel True
    offset (0,-30)     #top
    block:
        ease 1 yoffset -20           #bottom
        ease 1.5 offset (0,-30)     #top
        repeat

transform Jean_BJ_Head_6():
    #The deep cumming animation for her face
    ease .5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230
        repeat
transform Jean_BJ_Body_6():
    #The deep cumming animation for her body
    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190
        repeat


#transform Jean_BJ_Static():
#    #The static animation for her face
#    subpixel True
#    ease 1.5 offset (0,0)
#    repeat

#transform Jean_BJ_StaticBody():
#    #The static animation for her face
#    subpixel True
#    ease 1.5 offset (0,0)


#Head and Body Animations for Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jean_BJ_Launch(Line = Trigger):    # The sequence to launch the Jean BJ animations
    if renpy.showing("Jean_BJ_Animation"):
        return


    if renpy.showing("Jean_TJ_Animation"):
            hide Jean_TJ_Animation
    else:
            call Jean_Hide
            if Line == "L" or Line == "cum":
                show Jean_Sprite at sprite_location(StageCenter) zorder JeanX.Layer:
                    alpha 1
                    ease 1 zoom 2.5 offset (150,80)
                with dissolve
            else:
                show Jean_Sprite at sprite_location(StageCenter) zorder JeanX.Layer:
                    alpha 1
                    zoom 2.5 offset (150,80)
                with dissolve
            hide Jean_Sprite
    #". . ."
    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

    show Jean_BJ_Animation zorder 150:
        pos (645,510)
    if Taboo and Line == "L": # Jean gets started. . .
            if len(Present) >= 2:
                if Present[0] != JeanX:
                        "[JeanX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != JeanX:
                        "[JeanX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[JeanX.Name] looks around to see if anyone can see her."
            "She then bends down and puts your cock to her mouth."
    elif Line == "L":
            "[JeanX.Name] smoothly bends down and places your cock against her cheek."

    return

label Jean_BJ_Reset: # The sequence to the Jean animations from BJ to default
    if not renpy.showing("Jean_BJ_Animation"):
        return
#    hide Jean_BJ_Animation
    call Jean_Hide
    $ Speed = 0

    show Jean_Sprite at sprite_location(StageCenter) zorder JeanX.Layer:
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Jean_Sprite zorder JeanX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .2
        ease .3 zoom 1 offset (0,0)
    pause 1.5
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
        alpha 1
        zoom 1 offset (0,0)
    return

# End Jean Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# End Jean Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jean Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jean Handjob element //////////////////////////////////////////////////////////////////////

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
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
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

#transform Handcock_3():
#    subpixel True
#    rotate_pad False
#    ypos 400
#    rotate 0 #400
#    block:
#        ease .5 ypos 450 rotate -2 #450
#        pause 0.25
#        ease 1.0 ypos 400 rotate 0 #400
#        pause 0.1
#        repeat

#transform Handcock_4():
#    subpixel True
#    rotate_pad False
#    ypos 400
#    rotate 0
#    block:
#        ease .2 ypos 430 rotate -3 #410
#        ease .5 ypos 400 rotate 0
#        pause 0.1
#        repeat

transform Handcock_1J():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_2J():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Jean_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not Speed", Transform("Jean_Hand_Under"),
            "Speed == 1", At("Jean_Hand_Under", Jean_Hand_1()),
            "Speed >= 2", At("Jean_Hand_Under", Jean_Hand_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # cock
            "not Speed", Transform("Zero_Handcock"),
            "Speed == 1", At("Zero_Handcock", Handcock_1J()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            # fingers of the hand
            "not Speed", Transform("Jean_Hand_Over"),
            "Speed == 1", At("Jean_Hand_Over", Jean_Hand_1()),
            "Speed >= 2", At("Jean_Hand_Over", Jean_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Jean_HJ_Launch(Line = Trigger):
    if renpy.showing("Jean_HJ_Animation"):
        $ Trigger = "hand"
        return
    call Jean_Hide
    $ JeanX.ArmPose = 1
    if Line == "L":
        show Jean_Sprite at sprite_location(StageRight) zorder JeanX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)#(-180,350)
    else:
        show Jean_Sprite at sprite_location(StageRight) zorder JeanX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)#(-180,350)
        with dissolve

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Jean_HJ_Animation at sprite_location(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (250,250)#(100,250)
    show Jean_Sprite at sprite_location(StageRight) zorder JeanX.Layer:
        alpha 1
        ease .5 zoom 1.7 offset (-150,200)#(-180,200)
    return

label Jean_HJ_Reset: # The sequence to the Jean animations from handjob to default
    if not renpy.showing("Jean_HJ_Animation"):
        return
    $ Speed = 0
    $ JeanX.ArmPose = 1
    hide Jean_HJ_Animation with easeoutbottom
    call Jean_Hide
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
        alpha 1
        zoom 1.7 offset (-150,200)
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
        pause.5
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
        alpha 1
        zoom 1 offset (0,0)
    return

# End Jean Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jean Psychic Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jean Psychic Handjob element //////////////////////////////////////////////////////////////////////

image Jean_Hand_Psychic:
    ConditionSwitch(
        "Psychic == 'mouth'", "images/JeanSprite/PsyMouth.png",
        "Psychic == 'pussy'", "images/JeanSprite/PsyPussy.png",
        "Psychic == 'anal'", "images/JeanSprite/PsyAss.png",
        "Psychic == 'tits'", "images/JeanSprite/PsyTits.png",
        "True", "images/JeanSprite/handjeanP.png",
        )

#    "images/JeanSprite/handjeanP.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)
    block:
        ease 3 alpha 0.7
        ease 3 alpha 1
        repeat

image Jean_PJ_Animation:
#    contains:
#        ConditionSwitch(
#            # backside of the hand
#            "not Speed", Transform("Jean_Hand_Under"),
#            "Speed == 1", At("Jean_Hand_Under", Jean_Hand_1()),
#            "Speed >= 2", At("Jean_Hand_Under", Jean_Hand_2()),
#            "Speed", Null(),
#            ),
    contains:
        ConditionSwitch(
            # cock
#            "True", Transform("Zero_Handcock"), #remove?
            "not Speed", Transform("Zero_Handcock"),
            "Speed == 1", At("Zero_Handcock", Handcock_1J()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2J()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            # fingers of the hand
            "not Speed", Transform("Jean_Hand_Psychic"),
            "Speed == 1", At("Jean_Hand_Psychic", Jean_Hand_1()),
            "Speed >= 2", At("Jean_Hand_Psychic", Jean_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Jean_PJ_Launch(Line = Trigger):
    if renpy.showing("Jean_PJ_Animation"):
        $ Trigger = "psy"
        return

    call Jean_Hide
    if JeanX.Loc == bg_current:
            #hides alternate sex poses and displays Jean again
            show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
                alpha 1
                zoom 1 offset (0,0) xpos JeanX.sprite_location

    show Jean_PJ_Animation at sprite_location(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (250,250)#(100,250)
    return

label Jean_PJ_Reset: # The sequence to the Jean animations from handjob to default
    if not renpy.showing("Jean_PJ_Animation"):
        return
    $ Speed = 0
    $ JeanX.ArmPose = 1
    hide Jean_PJ_Animation with easeoutbottom
    return

# End Jean Psychic Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Jean's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jean_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Jean's upper body
                    "not Player.Sprite","Jean_TJ_0",#Static
                    "Speed == 1", "Jean_TJ_1",#slow
                    "Speed == 4", "Jean_TJ_4",#cumming high
                    "Speed == 5", "Jean_TJ_5",#cumming low
                    "Speed >= 2", "Jean_TJ_2",#fast
                    "True",       "Jean_TJ_0",#Static
                    )
            zoom .8 #.7
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Jean_TJ_HairBack:
            #Hair underlay
            "Jean_BJ_HairBack"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (30,-450)#(320,100)
            rotate 0

image Jean_TJ_Head:
            #Hair underlay
            "Jean_BJ_Head"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (30,-450)
            rotate 0

image Jean_TJ_HairTop:
            #Hair overlay
            ConditionSwitch(
                    "JeanX.Water or JeanX.Hair == 'wet'", "images/JeanBJFace/Jean_BJ_Hair_Wet_Over.png",
                    "JeanX.Hair == 'pony'", "images/JeanBJFace/Jean_BJ_Hair_Pony_Over.png",
                    "True", "images/JeanBJFace/Jean_BJ_Hair_Short_Over.png",
                    )
#            zoom 1.4
#            anchor (0.5, 0.5)

            #"Jean_BJ_HairBack"
            transform_anchor True
            zoom .98
            anchor (0.5, 0.5)
            offset (30,-450)#(120,-500)
            rotate 0

image JeanScreen:
    "images/JeanBJFace/screenshot0115.png"
    alpha 0.2

image Jean_TJ_ZeroCock:
            #cock used in laura's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .6
            anchor (0.5, 0.5)
            offset (70,50)#(220,670)
            rotate 0

image Jean_TJ_Body:
            #body underlay
            contains:
                "images/JeanBJFace/Jean_TJ_Body.png"
            contains:
                #Chest
                ConditionSwitch(
                        #"JeanX.Chest == 'bra'","images/JeanBJFace/Jean_TJ_Chest_Bra_Base.png",
                        "JeanX.Chest == 'sports bra'","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Base.png",
                        "JeanX.Chest == 'bikini top'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Base.png",
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
#                        "JeanX.Over == 'yellow shirt' and JeanX.Uptop",Null(),
                        "JeanX.Over == 'yellow shirt'","images/JeanBJFace/Jean_TJ_Over_Tank_Base.png",
                        "JeanX.Over == 'green shirt'","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Base.png",
                        "JeanX.Over == 'pink shirt'","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Base.png",
                        "True", Null(),
                        )
#            contains:
#                ConditionSwitch(
#                        "'tits' not in JeanX.Spunk",Null(),
#                        "True",       "images/JeanBJFace/Jean_Titjob_Spunk_Chest.png",
#                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0


image Jean_TJ_TitR:
            #body underlay
            contains:

                ConditionSwitch(
                    # right breast overlay
                    "not renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_TJ_TitR.png",
                    "True",  "images/JeanBJFace/Jean_TJ_TitRTJ.png",
                    )

            contains:
                ConditionSwitch(
                        "'tits' not in JeanX.Spunk",Null(),
                        "True",       "images/JeanBJFace/Jean_TJ_Spunk_TitsUnder.png",
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0

image Jean_TJ_Braback:
            #back fo the bra straps
#            contains:
#                ConditionSwitch(
#                        "JeanX.Over == 'yellow shirt' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Over_Tank_Back.png",
#                        "True", Null(),
#                        )
            contains:
                ConditionSwitch(
                        "JeanX.Over == 'green shirt'",Null(),
                        "JeanX.Chest == 'green bra' or JeanX.Chest == 'lace bra'","images/JeanBJFace/Jean_TJ_Chest_Bra_Base.png",
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0

image Jean_TJ_BraStretch:
            #bra streching effect
            contains:
                ConditionSwitch(
                        #"JeanX.Chest == 'corset' and not JeanX.Uptop","images/JeanBJFace/Jean_TJ_Chest_Corset.png",
                        "JeanX.Chest == 'bikini top' or JeanX.Chest == 'sports bra'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Stretch.png",
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0
            #alpha 0.9

image Jean_TJ_Tits:
            #layer with left tit and all clothing
            contains:
                "images/JeanBJFace/Jean_TJ_TitL.png"
            contains:
                #Piercings
                ConditionSwitch(
                        "JeanX.Pierce == 'ring'","images/JeanBJFace/Jean_TJ_Pierce_Ring.png",
                        "JeanX.Pierce == 'barbell'","images/JeanBJFace/Jean_TJ_Pierce_Barbell.png",
                        "True", Null(),
                        )
            contains:
                ConditionSwitch(
                    # right breast overlay
                    "not renpy.showing('Jean_TJ_Animation')", Null(),
                    "True",  "images/JeanBJFace/Jean_TJ_TitRO.png",
                    )
            contains:
                ConditionSwitch(
                        "'tits' not in JeanX.Spunk",Null(),
                        "True",       "images/JeanBJFace/Jean_TJ_Spunk_Tits.png",
                        )
            contains:
                #Chest
                ConditionSwitch(
                        "JeanX.Chest == 'green bra' and JeanX.Uptop and JeanX.Over == 'green shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_UpS.png",  #fix, add "no straps" version here
                        "JeanX.Chest == 'green bra' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Chest_Bra_Up.png",
                        "JeanX.Chest == 'lace bra' and JeanX.Uptop and JeanX.Over == 'green shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_UpS.png",    #fix, add "no straps" version here
                        "JeanX.Chest == 'lace bra' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Chest_Bra_Up.png",
                        "JeanX.Chest == 'sports bra' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Up.png",
                        "JeanX.Chest == 'bikini top' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Chest_Bikini_Up.png",
                        "JeanX.Chest == 'green bra' and JeanX.Over == 'green shirt'","images/JeanBJFace/Jean_TJ_Chest_Bra_Strapless.png",  #fix, add "no straps" version here
                        "JeanX.Chest == 'green bra'","images/JeanBJFace/Jean_TJ_Chest_Bra_Top.png",
                        "JeanX.Chest == 'lace bra' and JeanX.Over == 'green shirt'","images/JeanBJFace/Jean_TJ_Chest_LaceBra_Strapless.png",  #fix, add "no straps" version here
                        "JeanX.Chest == 'lace bra'","images/JeanBJFace/Jean_TJ_Chest_LaceBra_Top.png",
                        "JeanX.Chest == 'sports bra'","images/JeanBJFace/Jean_TJ_Chest_SportsBra_Top.png",
                        "JeanX.Chest == 'bikini top'","images/JeanBJFace/Jean_TJ_Chest_Bikini_Top.png",
                        "JeanX.Chest == 'corset' and not JeanX.Uptop and not renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_TJ_Chest_Corset.png",
                        "True", Null(),
                        )
            contains:
                #Over
                ConditionSwitch(
#                        "JeanX.Over == 'yellow shirt' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Up.png",
                        "JeanX.Over == 'yellow shirt' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Over_Tank_Up.png",
                        "JeanX.Over == 'yellow shirt'","images/JeanBJFace/Jean_TJ_Over_Tank_Top.png",
                        "JeanX.Over == 'green shirt' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Up.png",
                        "JeanX.Over == 'pink shirt' and JeanX.Uptop","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Up.png",
                        "JeanX.Over == 'green shirt'","images/JeanBJFace/Jean_TJ_Over_GreenShirt_Top.png",
                        "JeanX.Over == 'pink shirt'","images/JeanBJFace/Jean_TJ_Over_PinkShirt_Top.png",
                        "JeanX.Over == 'towel' and not renpy.showing('Jean_TJ_Animation')", "images/JeanBJFace/Jean_TJ_Over_Towel.png",
                        "True", Null(),
                        )
            contains:
                #Piercings clothing
                ConditionSwitch(
                        "JeanX.Uptop", Null(),
                        "(not JeanX.Over or JeanX.Over == 'towel') and (not JeanX.Chest or JeanX.Chest == 'corset')", Null(),
                        "JeanX.Pierce == 'ring'","images/JeanBJFace/Jean_TJ_Pierce_RingC.png",
                        "JeanX.Pierce == 'barbell'","images/JeanBJFace/Jean_TJ_Pierce_BarbellC.png",
                        "True", Null(),
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            #offset (410,770) # (300,275)
            rotate 0


# Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_0:
        #Her Body in the TJ pose, static
        contains:
                #bra strap backing
                "Jean_TJ_Braback"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #hairbelow the body
                "Jean_TJ_HairBack"
                subpixel True
                pos (0,0) #top (0,-10)
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jean_TJ_Body"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #head
                "Jean_TJ_Head"
                subpixel True
                pos (0,0) #top (0,-10)
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
                #right hand backside
                "Jean_TJ_TitR"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos -0
                    pause .1
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,0) #top (0,30)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 rotate -3#3
                    pause .1
                    ease 2 rotate -5#-2
                    pause .1
                    repeat
        contains:
                contains:
                    "Jean_TJ_BraStretch"
                subpixel True
                pos (0,20) #top (0,-10)
                transform_anchor True
                yzoom .75
        contains:
                contains:
                    "Jean_TJ_Tits"
                subpixel True
                pos (0,0) #top (0,-15)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #hairback
                "Jean_TJ_HairTop"
                subpixel True
                pos (0,0) #top (0,-10)
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

# End Jean TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_1:
        #Her Body in the TJ pose, slow
        contains:
                #bra strap backing
                "Jean_TJ_Braback"
                subpixel True
                pos (0,140) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140
                    repeat
        contains:
                #hairbelow the body
                "Jean_TJ_HairBack"
                subpixel True
                pos (0,150) #top (0,-10)
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jean_TJ_Body"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat
        contains:
                #head
                "Jean_TJ_Head"
                subpixel True
                pos (0,150) #top (0,-10)
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
                #right hand backside
                "Jean_TJ_TitR"
                subpixel True
                pos (0,140) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate -6
                parallel:
                    ease 2 ypos 0
                    pause .4
                    ease 1.8 ypos 25
                    pause .5
                    repeat
#                parallel:
#                    ease 2 rotate 0
#                    pause .2
#                    ease 2 rotate -5
#                    pause .5
#                    repeat
        contains:
                contains:
                    "Jean_TJ_BraStretch"
                subpixel True
                pos (0,145) #top (0,-10)
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
                pos (0,140) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140
                    repeat
        contains:
                #hairback
                "Jean_TJ_HairTop"
                subpixel True
                pos (0,150) #top (0,-10)
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

# End Jean TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_2:
        #Her Body in the TJ pose, fast
        contains:
                #bra strap backing
                "Jean_TJ_Braback"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #hairbelow the body
                "Jean_TJ_HairBack"
                subpixel True
                pos (0,80) #top (0,-10)
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jean_TJ_Body"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat
        contains:
                #head
                "Jean_TJ_Head"
                subpixel True
                pos (0,80) #top (0,-10)
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
                #right hand backside
                "Jean_TJ_TitR"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
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
                pos (0,50) #top (0,-10)
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
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #hairback
                "Jean_TJ_HairTop"
                subpixel True
                pos (0,80) #top (0,-10)
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

# End Jean TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_4:
        #Her Body in the TJ pose, cummming high
        contains:
                #bra strap backing
                "Jean_TJ_Braback"
                subpixel True
                pos (0,5) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat
        contains:
                #hairbelow the body
                "Jean_TJ_HairBack"
                subpixel True
                pos (0,0) #top (0,-10)
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jean_TJ_Body"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #head
                "Jean_TJ_Head"
                subpixel True
                pos (0,0) #top (0,-10)
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
                #right hand backside
                "Jean_TJ_TitR"
                subpixel True
                pos (0,5) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
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
                pos (0,5) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat
        contains:
                #hairback
                "Jean_TJ_HairTop"
                subpixel True
                pos (0,0) #top (0,-10)
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
# End Jean TJ Pose 4 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_5:
        #Her Body in the TJ pose, cumming low
        contains:
                #bra strap backing
                "Jean_TJ_Braback"
                subpixel True
                pos (0,90) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos 80
                    pause .2
                    ease 2 ypos 90
                    pause .4
                    repeat
        contains:
                #hairbelow the body
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
                #base body test / / / / / / / / / / / / / / / / / / / /
                "Jean_TJ_Body"
                subpixel True
                pos (0,140) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 130
                    pause .2
                    ease 2 ypos 140
                    pause .5
                    repeat
        contains:
                #head
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
                #right hand backside
                "Jean_TJ_TitR"
                subpixel True
                pos (0,90) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos 80
                    pause .2
                    ease 2 ypos 90
                    pause .4
                    repeat
        contains:
                #zero cock / / / / / / / / / / / / / / / / / / / /
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate -10
        contains:
                contains:
                    "Jean_TJ_BraStretch"
                subpixel True
                pos (-20,145) #top (0,-10)
                transform_anchor True
                yzoom 1
        contains:
                contains:
                    "Jean_TJ_Tits"
                subpixel True
                pos (0,90) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos 80
                    pause .2
                    ease 2 ypos 90
                    pause .4
                    repeat
        contains:
                #hairback
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

# End Jean TJ Pose 5 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Jean's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_TJ_Launch(Line = Trigger):    # The sequence to launch the Jean Titfuck animations
    if renpy.showing("Jean_TJ_Animation"):
        return

#    if Line == "L": # Jean gets started. . .
#            if Taboo:
#                if len(Present) >= 2:
#                    if Present[0] != JeanX:
#                            "[JeanX.Name] looks back at [Present[0].Name] to see if she's watching."
#                    elif Present[1] != JeanX:
#                            "[JeanX.Name] looks back at [Present[1].Name] to see if she's watching."
#                else:
#                            "[JeanX.Name] casually glances around to see if anyone can see her."
#            "[JeanX.Name] bends over and places your cock between her breasts."

#    if JeanX.Chest and JeanX.Over:
#        "She throws off her [JeanX.Over] and her [JeanX.Chest]."
#    elif JeanX.Over:
#        "She throws off her [JeanX.Over], baring her breasts underneath."
#    elif JeanX.Chest:
#        "She tugs off her [JeanX.Chest] and throws it aside."
#    $ JeanX.Over = 0
#    $ JeanX.Chest = 0
#    $ JeanX.ArmPose = 0

#    call Jean_First_Topless

    show blackscreen onlayer black with dissolve

    if renpy.showing("Jean_BJ_Animation"):
            hide Jean_BJ_Animation
    else:
            call Jean_Hide
            show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
                alpha 1
                ease 1 zoom 2.3 xpos 750 yoffset -100
            show Jean_Sprite zorder JeanX.Layer:
                alpha 0

    if JeanX.Over == "towel" or JeanX.Chest == "corset": #pulls top down because these tops are incompatible with TJ.
        $ JeanX.Uptop = 1

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Jean_TJ_Animation zorder 150:
        pos (1000,1050)#(1000,1000)#(700,520)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

label Jean_TJ_Reset:
    # The sequence to the Jean animations from Titfuck to default
    if not renpy.showing("Jean_TJ_Animation"):
        return
#    hide Jean_TJ_Animation
    call Jean_Hide
    $ Player.Sprite = 0

    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
        zoom 2.3 xpos 750 yoffset -100
    show Jean_Sprite zorder JeanX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos JeanX.sprite_location yoffset 0
    "[JeanX.Name] pulls back"
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
        alpha 1
        zoom 1 offset (0,0) xpos JeanX.sprite_location
    return


label Jean_Kissing_Smooch:
    $ JeanX.FaceChange("kiss")
    show Jean_Sprite at sprite_location(StageCenter) zorder JeanX.Layer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos JeanX.sprite_location zoom 1
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
        zoom 1
    $ JeanX.FaceChange("sexy")
    return
    

label Jean_Middle_Launch(T = Trigger,Set=1):
    call Jean_Hide
    $ Trigger = T
    $ JeanX.Pose = "mid" if Set else JeanX.Pose
    show Jean_Sprite at sprite_location(JeanX.sprite_location) zorder JeanX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeRightBreast_Jean:
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (185,340)#(110,380)#(120,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

image GropeLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (290,340)#(195,380)#(215,400)
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
        yzoom 0.45#0.5
        xzoom -0.45
        pos (175,325)#(195,360) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (150,300)#(190,380)
            pause .5
            ease 1.5 rotate 30 pos (175,325)#(200,410)
            repeat

#image GropeBreast:
image LickLeftBreast_Jean:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (275,330)#(95,355)#(105,375)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (255,310)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (275,330)#(105,375) bottom
            repeat

image GropeThigh_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,630)#(115,690)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (255,700) #(150,750) bottom
            ease 1 rotate 100 pos (245,630)
            repeat

image GropePussy_Jean:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,560)#(120,620)#(200,600) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (245,545)#pos (120,605) #(200,585)
                ease .75 rotate 170 pos (245,560)#pos (120,620)
            choice:
                ease .5 rotate 190 pos (245,545)#pos (120,605)
                pause .25
                ease 1 rotate 170 pos (245,560)#pos (120,620)
            repeat

image FingerPussy_Jean:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (265,640)#(140,700)#(210,665)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (275,615)#(150,665)#(220,640)
                pause .5
                ease 1 rotate 50 pos (265,640)#(140,700)  #(210,665)
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
        pos (275,595)#(155,650)#(230,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (265,575)#(145,630) #(210,605)
            linear .5 rotate -60 pos (255,585)#(135,640) #(200,615)
            easein 1 rotate 10 pos (275,595)#(155,650) #(230,625)
            repeat

image VibratorRightBreast_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (165,310)#(150,380)
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
        pos (270,310)#(270,400)
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
        pos (265,580)#(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 250 #230
            pause .25
            ease 1 rotate 70 xpos 265 #240
            pause .25
            repeat

image VibratorAnal_Jean:
    contains:
        subpixel True
        "UI_Vibrator"
        pos (295,570)#(270,640)
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



#Lesbian action animations.
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
            ease 1 rotate 10 pos (290,350)#(220,380)
            ease 1 rotate -10 pos (290,340)#(220,370)
            repeat
#(185,340)(290,340)
image GirlGropeRightBreast_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (170,340)#(90,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 pos (170,350)#(90,380)
            ease 1 rotate -10 pos (170,340)#(90,370)
            repeat

image GirlGropeThigh_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        anchor (0.5,0.5)
        pos (0,0)#(240,540)#(210,730)
        alpha 0.5
        rotate 100
#        parallel:
#            pause .5
#            ease 1 ypos 780
#            ease 1 ypos 730
#            repeat
#        parallel:
#            pause .5
#            ease .5 xpos 213
#            ease .5 xpos 210
#            ease .5 xpos 213
#            ease .5 xpos 210
#            repeat

image GirlGropePussy_JeanSelf:
    contains:
        "GirlGropePussy_Jean"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (200,510)#(100,500)

image GirlGropePussy_Jean:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (240,540)#(130,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (240,535)#(130,590)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (240,535)#(130,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (240,535)#(130,590)
                ease .75 rotate 200 pos (240,540)#(130,595)
                ease .5 rotate 205 pos (240,535)
                ease .75 rotate 200 pos (240,540)
            choice: #Fast stroke
                ease .3 rotate 205 pos (240,535)#(130,590)
                ease .3 rotate 200 pos (240,545)#(130,600)
                ease .3 rotate 205 pos (240,535)
                ease .3 rotate 200 pos (240,545)
            repeat

image GirlFingerPussy_Jean:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (250,550)#(140,605)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (250,555)#(140,610)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (250,555)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 565#620
                ease .75 rotate 200 ypos 570#625
                ease .5 rotate 205 ypos 565
                ease .75 rotate 200 ypos 570
            choice: #Fast stroke
                ease .3 rotate 205 ypos 565#620
                ease .3 rotate 200 ypos 575#630
                ease .3 rotate 205 ypos 565
                ease .3 rotate 200 ypos 575
            repeat
