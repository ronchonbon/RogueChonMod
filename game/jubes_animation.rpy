# Basic Girl Sprites

image Jubes_Sprite:
    LiveComposite(
        (500,950),

        (0,0), ConditionSwitch(
            #Jacket back of collar
            "JubesX.Acc", "images/JubesSprite/Jubes_Sprite_Jacket_Collar.png",
            "True", Null(),
            ),

        (147,48), "Jubes_Sprite_HairBack",
#        (0,0), ConditionSwitch(
#            #Jacket backplate
#            "JubesX.Over == 'jacket'", "images/JubesSprite/Jubes_Sprite_Over_Jacket_Under.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #pants down back
            "not JubesX.Legs or not JubesX.Upskirt", Null(),
            "JubesX.Legs == 'pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants_Back.png",
            "JubesX.Legs == 'shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties down back
            "not JubesX.Panties or not JubesX.PantiesDown", Null(),
            #if the panties are down
            "JubesX.Legs and not JubesX.Upskirt and JubesX.Legs != 'skirt'", Null(),
            #if she's wearing a skirt or nothing else
            "JubesX.Panties == 'lace panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace_Back.png",
            "JubesX.Panties == 'tiger panties'", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Back.png",
            "JubesX.Panties == 'bikini bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Back.png",
            "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Back.png",
            ),

        (0,0), ConditionSwitch(
            #body
            "JubesX.ArmPose != 1", "images/JubesSprite/Jubes_Sprite_Body2.png",         # right hand up/left down
            "True", "images/JubesSprite/Jubes_Sprite_Body1.png", #if JubesX.Arms == 1   # right Hand on hip/left raised
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "JubesX.Water and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Water1.png",
            "JubesX.Water", "images/JubesSprite/Jubes_Sprite_Water2.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Jacket open, behind torso
#            "JubesX.Uptop", ConditionSwitch(
#                    # if top is up. . .
#                    "(JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket') and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Open1_Back.png",
#                    "JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket'", "images/JubesSprite/Jubes_Sprite_Jacket_Open2_Back.png",
#                    "True", Null(),
#                    ),
            "not JubesX.Acc", Null(),
            "(JubesX.Uptop or JubesX.Acc == 'open jacket') and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Open1_Back.png",
            "(JubesX.Uptop or JubesX.Acc == 'open jacket')", "images/JubesSprite/Jubes_Sprite_Jacket_Open2_Back.png",
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "True", "images/JubesSprite/Jubes_Sprite_Jacket_Closed_Back.png",
#            "True", Null(),
            ),

#        (165,560), ConditionSwitch(    #145,560
#            #Personal Wetness
#            "not JubesX.Wet", Null(),
#            "JubesX.Legs and JubesX.Legs != 'skirt' and not JubesX.Upskirt", Null(),
#            "JubesX.Panties and not JubesX.PantiesDown and JubesX.Wet <= 1", Null(),
#            "JubesX.Wet == 1", ConditionSwitch( #Wet = 1
#                    "JubesX.Panties and JubesX.PantiesDown", AlphaMask("Wet_Drip","Jubes_Drip_MaskP"),
#                    "JubesX.Legs and JubesX.Legs != 'skirt'", AlphaMask("Wet_Drip","Jubes_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip","Jubes_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            "True", ConditionSwitch( #Wet = 2+
#                    "JubesX.Panties and JubesX.PantiesDown", AlphaMask("Wet_Drip2","Jubes_Drip_MaskP"),
#                    "JubesX.Legs and JubesX.Legs != 'skirt'", AlphaMask("Wet_Drip2","Jubes_Drip_MaskP"),
#                    "JubesX.Panties", AlphaMask("Wet_Drip","Jubes_Drip_Mask"), #"Wet_Drip2",#
#                    "True", AlphaMask("Wet_Drip2","Jubes_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            ),
#        (165,560), ConditionSwitch(    #145,560
#            #dripping spunk
#            "'in' not in JubesX.Spunk and 'anal' not in JubesX.Spunk", Null(),
#            "JubesX.Legs and JubesX.Legs != 'skirt' and not JubesX.Upskirt", Null(),
#            "JubesX.Panties and not JubesX.PantiesDown and JubesX.Wet <= 1", Null(),
#            "True", ConditionSwitch( #Wet = 2+
#                    "JubesX.Panties and JubesX.PantiesDown", AlphaMask("Spunk_Drip2","Jubes_Drip_MaskP"),
##                    "JubesX.Legs and JubesX.Legs != 'skirt'", AlphaMask("Spunk_Drip2","Jubes_Drip_MaskP"), #add if pantes have down art
#                    "JubesX.Panties", AlphaMask("Spunk_Drip","Jubes_Drip_Mask"), #"Wet_Drip2",#
#                    "True", AlphaMask("Spunk_Drip2","Jubes_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            ),

        (0,0), ConditionSwitch(
            #pubes
            "JubesX.Pubes", "images/JubesSprite/Jubes_Sprite_Pubes.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #nude lower piercings
            "not JubesX.Pierce", Null(),
#            "JubesX.Panties and not JubesX.PantiesDown", Null(),
#            "JubesX.Legs != 'skirt' and JubesX.Legs and not JubesX.Upskirt", Null(), #skirt if wearing a skirt
            "JubesX.Pierce == 'barbell'", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Bot.png",
            "JubesX.Pierce == 'ring'", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Bot.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #naked tit piercings
            "not JubesX.Pierce", Null(),
#            "not JubesX.Pierce or ((JubesX.Over or JubesX.Chest) and not JubesX.Uptop)", Null(),
#            "JubesX.Uptop", Null(),
            #Only does this if she has piercings, has no tops, or has her top up
            "JubesX.Pierce == 'barbell'", ConditionSwitch(
                    # if top is up. . .
#                    "JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Top.png",
                    "True", "images/JubesSprite/Jubes_Sprite_Pierce_Barbell_Top.png",
                    ),
            # Pierce is "ring"
#            "JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            "JubesX.Over or JubesX.Chest", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            "True", "images/JubesSprite/Jubes_Sprite_Pierce_Ring_Top.png",
            ),
#        (0,0), ConditionSwitch(
#            #Necklaces
##            "JubesX.Neck == 'silver'", "images/JubesSprite/Jubes_Sprite_Necklace2.png",
#            "JubesX.Neck == 'gold necklace'", "images/JubesSprite/Jubes_Sprite_Necklace1.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Chest layer
            "JubesX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JubesX.Chest == 'lace bra'", "images/JubesSprite/Jubes_Sprite_Chest_Lace_Up.png",
                    "JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Chest_Sports_Up.png",
                    "JubesX.Chest == 'bikini top'", "images/JubesSprite/Jubes_Sprite_Chest_Bikini_Up.png",
                    "True", Null(),
                    ),
            "JubesX.Chest == 'lace bra'", "images/JubesSprite/Jubes_Sprite_Chest_Lace.png",
            "JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Chest_Sports.png",
            "JubesX.Chest == 'bikini top'", "images/JubesSprite/Jubes_Sprite_Chest_Bikini.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #clothed tit peircings  under jacket
#            "not JubesX.Pierce or (not JubesX.Over and not JubesX.Chest and not JubesX.Uptop)", Null(),
#            "JubesX.Uptop", Null(),
#            "JubesX.Pierce == 'barbell'", ConditionSwitch(
#                    # if top is up. . .
#                    "JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Barbell_TitsUC.png",
#                    "True", "images/JubesSprite/Jubes_Sprite_Barbell_TitsLC.png",
#                    ),
#            "JubesX.Pierce == 'ring' and (JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra')", "images/JubesSprite/Jubes_Sprite_Ring_TitsUC.png",
#            "JubesX.Pierce == 'ring'", "images/JubesSprite/Jubes_Sprite_Ring_TitsLC.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #stockings
            "JubesX.Hose == 'socks'", "images/JubesSprite/Jubes_Sprite_Hose_Socks.png",
            "JubesX.Hose == 'stockings'", "images/JubesSprite/Jubes_Sprite_Hose_Stockings.png",
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesSprite/Jubes_Sprite_Hose_StockingsandGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesSprite/Jubes_Sprite_Hose_Garter.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties
            "not JubesX.Panties", Null(),
            "JubesX.PantiesDown", ConditionSwitch(
                    #if the panties are down
                    "not JubesX.Legs or JubesX.Upskirt or JubesX.Legs == 'skirt'", ConditionSwitch(
                            #if she's wearing a skirt or nothing else
                            "JubesX.Panties == 'lace panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace_Down.png",
                            "JubesX.Panties == 'bikini bottoms' and JubesX.Wet", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_DownW.png",
                            "JubesX.Panties == 'bikini bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Down.png",
                            "JubesX.Panties == 'tiger panties' and JubesX.Wet", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_DownW.png",
                            "JubesX.Panties == 'tiger panties'", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Down.png",
                            "JubesX.Wet", "images/JubesSprite/Jubes_Sprite_Panties_Blue_DownW.png",
                            "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Down.png",
                            ),
                    "True", Null(),
                    ),
            "JubesX.Wet", ConditionSwitch(
                #if she's  wet
                "JubesX.Panties == 'lace panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace.png",
                "JubesX.Panties == 'bikini bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini_Wet.png",
                "JubesX.Panties == 'tiger panties' and JubesX.Wet", "images/JubesSprite/Jubes_Sprite_Panties_Tiger_Wet.png",
                "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue_Wet.png",
                ),
            "True", ConditionSwitch(
                #if she's not wet
                "JubesX.Panties == 'lace panties'", "images/JubesSprite/Jubes_Sprite_Panties_Lace.png",
                "JubesX.Panties == 'bikini bottoms'", "images/JubesSprite/Jubes_Sprite_Panties_Bikini.png",
                "JubesX.Panties == 'tiger panties'", "images/JubesSprite/Jubes_Sprite_Panties_Tiger.png",
                "True", "images/JubesSprite/Jubes_Sprite_Panties_Blue.png",
                ),
            ),
        (0,0), ConditionSwitch(
            #pantyhose
            "JubesX.Hose == 'pantyhose' and (not JubesX.PantiesDown or not JubesX.Panties)", "images/JubesSprite/Jubes_Sprite_Hose_Pantyhose.png",
            "JubesX.Hose == 'ripped pantyhose' and (not JubesX.PantiesDown or not JubesX.Panties)", "images/JubesSprite/Jubes_Sprite_Hose_Pantyhose_Holed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pants
            "not JubesX.Legs", Null(),
            "JubesX.Upskirt", ConditionSwitch(
                        #if the skirt's up or pants down
                        "JubesX.Legs == 'pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants_Down.png",
                        "JubesX.Legs == 'shorts' and JubesX.Wet > 1", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_DownW.png",
                        "JubesX.Legs == 'shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Down.png",
                        "True", Null(),
                        ),
            "JubesX.Wet > 1", ConditionSwitch(
                #if she's wet
                "JubesX.Legs == 'pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants.png",
                "JubesX.Legs == 'shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts_Wet.png",
#                        "JubesX.Legs == 'skirt'", "images/JubesSprite/Jubes_Sprite_Legs_Skirt.png",
                "True", Null(),
                ),
            "True", ConditionSwitch(
                #if she's not wet
                "JubesX.Legs == 'pants'", "images/JubesSprite/Jubes_Sprite_Legs_Pants.png",
                "JubesX.Legs == 'shorts'", "images/JubesSprite/Jubes_Sprite_Legs_Shorts.png",
#                        "JubesX.Legs == 'skirt'", "images/JubesSprite/Jubes_Sprite_Legs_Skirt.png",
                "True", Null(),
                ),
            ),
#        (0,0), ConditionSwitch(
#            #clothed lower piercings
#            "JubesX.Legs == 'skirt' or JubesX.Legs == 'pants'", Null(),
#            "JubesX.Pierce == 'barbell'", ConditionSwitch(
#                    #if it's the barbell pericings
#                    "JubesX.Legs and not JubesX.Upskirt", "images/JubesSprite/Jubes_Sprite_Barbell_PussyC.png",
#                    "JubesX.Panties and not JubesX.PantiesDown", "images/JubesSprite/Jubes_Sprite_Barbell_PussyC.png",
#                    "True", Null(),
#                    ),
#            "JubesX.Pierce == 'ring'", ConditionSwitch(
#                    #if it's the ring pericings
#                    "JubesX.Legs and not JubesX.Upskirt", "images/JubesSprite/Jubes_Sprite_Ring_PussyC.png",
#                    "JubesX.Panties and not JubesX.PantiesDown", "images/JubesSprite/Jubes_Sprite_Ring_PussyC.png",
#                    "True", Null(),
#                    ),
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #pussy spunk
#            "JubesX.Legs and not JubesX.Upskirt", Null(),
#            "'in' in JubesX.Spunk or 'anal' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Spunk_Pussy.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #Over
            "JubesX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JubesX.Over == 'tube top'", "images/JubesSprite/Jubes_Sprite_Over_Tube_Up.png",
                    "JubesX.Over == 'red shirt'", "images/JubesSprite/Jubes_Sprite_Over_Red_Up.png",
                    "JubesX.Over == 'black shirt'", "images/JubesSprite/Jubes_Sprite_Over_Black_Up.png",
#                    "JubesX.Over == 'towel'", "images/JubesSprite/Jubes_Sprite_Towel.png",
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "JubesX.Over == 'tube top'", "images/JubesSprite/Jubes_Sprite_Over_Tube.png",
            "JubesX.Over == 'red shirt'", "images/JubesSprite/Jubes_Sprite_Over_Red.png",
            "JubesX.Over == 'black shirt'", "images/JubesSprite/Jubes_Sprite_Over_Black.png",
            "JubesX.Over == 'towel' and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Over_Towel1.png",
            "JubesX.Over == 'towel'", "images/JubesSprite/Jubes_Sprite_Over_Towel2.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Jacket as an accessory
            "not JubesX.Acc", Null(),
            "JubesX.Acc == 'open jacket' and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Open1.png",
            "JubesX.Acc == 'open jacket'", "images/JubesSprite/Jubes_Sprite_Jacket_Open2.png",
            "JubesX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "(JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket') and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Open1.png",
                    "JubesX.Acc == 'jacket' or JubesX.Acc == 'shut jacket'", "images/JubesSprite/Jubes_Sprite_Jacket_Open2.png",
                    "True", Null(),
                    ),
            #If she's using arm pose 1, left arm pointing
            #If she's using arm pose 2, Left arm on hip
            "JubesX.Acc == 'jacket' and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Closed1.png",
            "JubesX.Acc == 'jacket'", "images/JubesSprite/Jubes_Sprite_Jacket_Closed2.png",
            #below all assume JubesX.Acc == 'shut jacket'
            "JubesX.Upskirt and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Shut1_Up.png",
            "JubesX.Upskirt", "images/JubesSprite/Jubes_Sprite_Jacket_Shut2_Up.png",
            "JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Jacket_Shut1.png",
            "True", "images/JubesSprite/Jubes_Sprite_Jacket_Shut2.png",
            ),

#        (0,0), ConditionSwitch(
#            #clothed tit peircings
#            "not JubesX.Pierce or (not JubesX.Over and not JubesX.Chest and not JubesX.Uptop)", Null(),
#            "JubesX.Over == 'jacket' and not JubesX.Uptop", Null(),
#            "JubesX.Pierce == 'barbell'", ConditionSwitch(
#                    # if top is up. . .
#                    "JubesX.Uptop", "images/JubesSprite/Jubes_Sprite_Barbell_TitsL.png",
#                    "JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra'", "images/JubesSprite/Jubes_Sprite_Barbell_TitsUC.png",
#                    "True", "images/JubesSprite/Jubes_Sprite_Barbell_TitsLC.png",
#                    ),
#            "JubesX.Uptop", "images/JubesSprite/Jubes_Sprite_Ring_TitsL.png",
#            "JubesX.Pierce == 'ring' and (JubesX.Chest == 'black bra' or JubesX.Chest == 'lace bra' or JubesX.Chest == 'sports bra')", "images/JubesSprite/Jubes_Sprite_Ring_TitsUC.png",
#            "JubesX.Pierce == 'ring'", "images/JubesSprite/Jubes_Sprite_Ring_TitsLC.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast spunk
            "'tits' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms 1 upper layer
            "JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_ArmOver1.png",        #If she's using arm pose 1, right arm high
            "True", "images/JubesSprite/Jubes_Sprite_ArmOver2.png",  #if JubesX.Arms ==2                                        #If she's using arm pose 2, Left arm high
            ),
        (0,0), ConditionSwitch(
            #Water effect
            "JubesX.Water and JubesX.ArmPose == 1", "images/JubesSprite/Jubes_Sprite_Water1_Arm.png",
            "True", Null(),
            ),


        (147,48), "Jubes_Sprite_Head", #(141,45)


#        (0,0), "images/JubesSprite/Jubes_Sprite_Headref.png", #53,-45


#        (0,0), ConditionSwitch(
#            #hand spunk
#            "JubesX.ArmPose == 2 or 'hand' not in JubesX.Spunk", Null(),
#            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Hand.png",
#            ),
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not JubesX.Held or JubesX.ArmPose != 2", Null(),
#            "JubesX.ArmPose == 2 and JubesX.Held == 'phone'", "images/JubesSprite/Jubes_held_phone.png",
#            "JubesX.ArmPose == 2 and JubesX.Held == 'dildo'", "images/JubesSprite/Jubes_held_dildo.png",
#            "JubesX.ArmPose == 2 and JubesX.Held == 'vibrator'", "images/JubesSprite/Jubes_held_vibrator.png",
#            "JubesX.ArmPose == 2 and JubesX.Held == 'panties'", "images/JubesSprite/Jubes_held_panties.png",
#            "True", Null(),
#            ),


        (0,0), ConditionSwitch(
            #UI tool for When Jubes is masturbating using girl_offhand_action actions
            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != JubesX", Null(),

            #this is not a lesbian thing, and a trigger is set, and Jubes is the primary. . .
            "girl_offhand_action == 'fondle pussy'", "GirlGropePussy_JubesSelf",
            "girl_offhand_action == 'fondle breasts'", ConditionSwitch(
                    "offhand_action == 'fondle breasts' or offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Jubes",
                        #When zero is working the right breast, fondle left
                    "primary_action == 'fondle breasts' or primary_action == 'suck breasts'", "GirlGropeRightBreast_Jubes",
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_Jubes",
                        #else, fondle both
                    ),
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Jubes",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Jubes",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Jubes",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Partner_offhand_action(Threesome masutrbation) actions
            "not Partner_offhand_action or Partner_primary_action != 'masturbation' or focused_Girl == JubesX", Null(),

            #Jubes is not primary, and T4 is masturbation, and a T5 is selected
            "Partner_offhand_action == 'fondle pussy' and primary_action != 'sex' and JubesX.lust >= 70", "GirlFingerPussy_Jubes",
            "Partner_offhand_action == 'fondle pussy'", "GirlGropePussy_Jubes",
            "Partner_offhand_action == 'fondle breasts'", "GirlGropeRightBreast_Jubes",
            "Partner_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "Partner_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "Partner_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "Partner_offhand_action == 'vibrator anal'", "VibratorAnal",
            "Partner_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for primary_action1(primary) actions
            #Jubes is primary and a sex trigger is active
            "not primary_action or focused_Girl != JubesX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Jubes",
            "primary_action == 'fondle thighs'", "GropeThigh_Jubes",
            "primary_action == 'fondle breasts'", "GropeLeftBreast_Jubes",
            "primary_action == 'suck breasts'", "LickRightBreast_Jubes",
            "primary_action == 'fondle pussy' and action_speed == 2", "FingerPussy_Jubes",
            "primary_action == 'fondle pussy'", "GropePussy_Jubes",
            "primary_action == 'lick pussy'", "Lickpussy_Jubes",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Jubes",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "primary_action == 'vibrator anal'", "VibratorAnal_Jubes",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for offhand_action(secondary) actions
            "not offhand_action or focused_Girl != JubesX", Null(),

            #Jubes is primary and an offhand trigger is active
            "offhand_action == 'fondle breasts'", ConditionSwitch(
                    "offhand_action == 'fondle breasts' and primary_action == 'suck breasts'", "GropeLeftBreast_Jubes",
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_Jubes",
                        #else, fondle right
                    ),
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast_Jubes",
                #When sucking right breast, vibrator left
            "offhand_action == primary_action", Null(),
                #When both triggers are the same, do nothing
            "offhand_action == 'suck breasts'", "LickLeftBreast_Jubes",
            "offhand_action == 'fondle pussy'", "GropePussy_Jubes",
            "offhand_action == 'lick pussy'", "Lickpussy_Jubes",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Jubes",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Jubes",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Jubes",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Jubes",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Jubes",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Partner_primary_action(Threesome) actions (ie Rogue's hand on her)
            "not Partner_primary_action or focused_Girl != JubesX", Null(),

            # There is a threesome trigger set and Jubes is the target of it
            "Partner_primary_action == 'fondle pussy' and primary_action != 'sex' and JubesX.lust >= 70", "GirlFingerPussy_Jubes",
            "Partner_primary_action == 'fondle pussy'", "GirlGropePussy_Jubes",
            "Partner_primary_action == 'lick pussy'", "Lickpussy_Jubes",
            "Partner_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Jubes",
            "Partner_primary_action == 'suck breasts'", "LickRightBreast_Jubes",
            "Partner_primary_action == 'fondle breasts'", ConditionSwitch(
                    "primary_action == 'fondle breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Jubes", #When zero is working the right breast, fondle left
#                    "offhand_action == 'fondle breasts' or offhand_action == 'suck breasts'", "GirlGropeRightBreast_Jubes",  #When zero is working the left breast, fondle right
#                    "girl_offhand_action == 'fondle breasts' or girl_offhand_action == 'suck breasts'", "GirlGropeRightBreast_Jubes", #When zero is working the left breast, fondle right
                    "True", "GirlGropeRightBreast_Jubes",#else, fondle right
                    ),
            "Partner_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "Partner_primary_action == 'vibrator pussy'", "VibratorPussy",
            "Partner_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "Partner_primary_action == 'vibrator anal'", "VibratorAnal",
            "Partner_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for girl_offhand_action(lesbian) actions (ie Rogue's hand on her when Jubes is secondary)
            "primary_action != 'lesbian' or focused_Girl == JubesX or not girl_offhand_action", Null(),

            # If there is a girl_offhand_action and Jubes is not the focus
            "girl_offhand_action == 'fondle pussy' and primary_action != 'sex' and JubesX.lust >= 70", "GirlFingerPussy_Jubes",
            "girl_offhand_action == 'fondle pussy'", "GirlGropePussy_Jubes",
            "girl_offhand_action == 'lick pussy'", "Lickpussy_Jubes",
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Jubes",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast_Jubes",
            "girl_offhand_action == 'fondle breasts'", ConditionSwitch(
                    "primary_action == 'fondle breasts' or primary_action == 'suck breasts'", "GirlGropeLeftBreast_Jubes",
                        #When zero is working the right breast, fondle left
                    "offhand_action == 'fondle breasts' or offhand_action == 'suck breasts'", "GirlGropeRightBreast_Jubes",
                        #When zero is working the left breast, fondle right
                    "girl_offhand_action == 'fondle breasts' or girl_offhand_action == 'suck breasts'", "GirlGropeLeftBreast_Jubes",
                        #When zero is working the right breast, fondle left
                    "True", "GirlGropeRightBreast_Jubes",
                        #else, fondle right
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
    yoffset 0
    zoom .85


image Jubes_Sprite_HairBack:
    contains:
        ConditionSwitch(
                #hair back
    #            "renpy.showing('Jubes_BJ_Animation')", Null(),
    #            "renpy.showing('Jubes_SexSprite')", "images/JubesSex/Jubes_Sprite_Hair_Long_UnderSex.png",
    #            "JubesX.Hair == 'wet' or JubesX.Water", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Under.png",
                "JubesX.Hair == 'wet'", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Back.png",
                "JubesX.Water", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Back.png",
                "True", "images/JubesSprite/Jubes_Sprite_Hair_Short_Back.png",
                ),
#    "images/JubesSprite/Jubes_Sprite_Hair_Long_Under.png"
    anchor (0.5, 0.5)
    zoom .37#.47


image Jubes_Sprite_Head:
    LiveComposite(
        (900,900),
#        (0,0), ConditionSwitch(
#                # hair behind face
#                "renpy.showing('Jubes_SexSprite')", "images/JubesSex/Jubes_Sprite_Hair_Long_UnderSex.png",
#                "True", Null(),
#                ),
        (0,0), ConditionSwitch(
                # Face background plate
                "JubesX.Blush >= 2", "images/JubesSprite/Jubes_Sprite_Head_Blush2.png",
                "JubesX.Blush", "images/JubesSprite/Jubes_Sprite_Head_Blush1.png",
                "True", "images/JubesSprite/Jubes_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in JubesX.Spunk", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(#Mouths
            "JubesX.Mouth == 'lipbite'", "images/JubesSprite/Jubes_Sprite_Mouth_Lipbite.png",
            "JubesX.Mouth == 'sucking'", "images/JubesSprite/Jubes_Sprite_Mouth_Open.png",
            "JubesX.Mouth == 'kiss'", "images/JubesSprite/Jubes_Sprite_Mouth_Kiss.png",
            "JubesX.Mouth == 'sad'", "images/JubesSprite/Jubes_Sprite_Mouth_Sad.png",
            "JubesX.Mouth == 'smile'", "images/JubesSprite/Jubes_Sprite_Mouth_Smile.png",
            "JubesX.Mouth == 'surprised'", "images/JubesSprite/Jubes_Sprite_Mouth_Open.png",
            "JubesX.Mouth == 'tongue'", "images/JubesSprite/Jubes_Sprite_Mouth_Tongue.png",
            "JubesX.Mouth == 'grimace'", "images/JubesSprite/Jubes_Sprite_Mouth_Smile.png",
            "JubesX.Mouth == 'smirk'", "images/JubesSprite/Jubes_Sprite_Mouth_Smirk.png",
            "True", "images/JubesSprite/Jubes_Sprite_Mouth_Normal.png",
            ),


        (0,0), ConditionSwitch(#Mouths spunk
            "'mouth' not in JubesX.Spunk", Null(),
            "JubesX.Mouth == 'sucking'", "images/JubesSprite/Jubes_Sprite_Spunk_Open.png",
            "JubesX.Mouth == 'kiss'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.Mouth == 'sad'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.Mouth == 'smile'", "images/JubesSprite/Jubes_Sprite_Spunk_Lipbite.png",
            "JubesX.Mouth == 'surprised'", "images/JubesSprite/Jubes_Sprite_Spunk_Kiss.png",
            "JubesX.Mouth == 'tongue'", "images/JubesSprite/Jubes_Sprite_Spunk_Open.png",
            "JubesX.Mouth == 'grimace'", "images/JubesSprite/Jubes_Sprite_Spunk_Lipbite.png",
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Smirk.png",
            ),

        (0,0), ConditionSwitch(
            #brows
            "JubesX.Brows == 'angry' and JubesX.Blush >= 2", "images/JubesSprite/Jubes_Sprite_Brows_AngryB.png",
            "JubesX.Brows == 'angry'", "images/JubesSprite/Jubes_Sprite_Brows_Angry.png",
            "JubesX.Brows == 'sad' and JubesX.Blush >= 2", "images/JubesSprite/Jubes_Sprite_Brows_SadB.png",
            "JubesX.Brows == 'sad'", "images/JubesSprite/Jubes_Sprite_Brows_Sad.png",
            "JubesX.Brows == 'surprised'", "images/JubesSprite/Jubes_Sprite_Brows_Surprised.png",
            "JubesX.Brows == 'sad' and JubesX.Blush >= 2", "images/JubesSprite/Jubes_Sprite_Brows_ConfusedB.png",
            "JubesX.Brows == 'confused'", "images/JubesSprite/Jubes_Sprite_Brows_Confused.png",
            "True", "images/JubesSprite/Jubes_Sprite_Brows_Normal.png",
            ),
        (0,0), "Jubes Blink",     #Eyes
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not JubesX.Water", Null(),
#            "True", "images/JubesSprite/Jubes_Sprite_Head_Water.png",
#            ),
        (0,0), "images/JubesSprite/Jubes_Sprite_Earrings.png",     #Eyes
        (0,0), ConditionSwitch(
            #Hair over
#            "renpy.showing('Jubes_TJ_Animation')", Null(),
            "JubesX.Hair == 'wet' or JubesX.Water", "images/JubesSprite/Jubes_Sprite_Hair_Wet.png",
            "JubesX.Hair == 'shades'", "images/JubesSprite/Jubes_Sprite_Hair_Shades.png",
            "True", "images/JubesSprite/Jubes_Sprite_Hair_Short.png",
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "not JubesX.Water", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Wet_Head.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Spunk_Shades.png",
            "'facial' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        )
    anchor (0.5, 0.5)
    zoom .37#.38
#    alpha 0.9

image Jubes Blink:
    ConditionSwitch(
    "JubesX.Eyes == 'sexy'", "images/JubesSprite/Jubes_Sprite_Eyes_Sexy.png",
    "JubesX.Eyes == 'side'", "images/JubesSprite/Jubes_Sprite_Eyes_Side.png",
    "JubesX.Eyes == 'surprised'", "images/JubesSprite/Jubes_Sprite_Eyes_Surprised.png",
    "JubesX.Eyes == 'normal'", "images/JubesSprite/Jubes_Sprite_Eyes_Normal.png",
    "JubesX.Eyes == 'stunned'", "images/JubesSprite/Jubes_Sprite_Eyes_Stunned.png",
    "JubesX.Eyes == 'down'", "images/JubesSprite/Jubes_Sprite_Eyes_Down.png",
    "JubesX.Eyes == 'closed'", "images/JubesSprite/Jubes_Sprite_Eyes_Closed.png",
    "JubesX.Eyes == 'leftside'", "images/JubesSprite/Jubes_Sprite_Eyes_Leftside.png",
    "JubesX.Eyes == 'manic'", "images/JubesSprite/Jubes_Sprite_Eyes_Squint.png",
    "JubesX.Eyes == 'squint'", "Jubes_Squint",
    "True", "images/JubesSprite/Jubes_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JubesSprite/Jubes_Sprite_Eyes_Closed.png"
    .25
    repeat

image Jubes_Squint:
    "images/JubesSprite/Jubes_Sprite_Eyes_Sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/JubesSprite/Jubes_Sprite_Eyes_Squint.png"
    .25
    repeat


#image Jubes_Drip_Mask:
#    #This is the mask for her drip pattern
#    contains:
#        "images/JubesSprite/Jubes_Sprite_WetMask.png"
#        offset (-145,-560)#(-225,-560)

image Jubes_Drip_MaskPanties:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/JubesSprite/Jubes_Sprite_DripMaskPanties.png"
        offset (-145,-560)#(-225,-560)

image Jubes_Drip_MaskPants:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/JubesSprite/Jubes_Sprite_DripMaskPants.png"
        offset (-145,-560)#(-225,-560)

# End Jubes Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#if there is a problem, remove Doggy form here and put it at the bottom.

# Jubes Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Jubes_Doggy_Base = LiveComposite(
image Jubes_Doggy_Animation: #nee Jubes_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Jubes_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Top",
                    "action_speed", "Jubes_Doggy_Anal_Head_Top",
                    "True", "Jubes_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Top",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Top",
                    "True", "Jubes_Doggy_Body",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Jubes_Doggy_Foot2_Top",
                    "action_speed", "Jubes_Doggy_Foot1_Top",
                    "True", "Jubes_Doggy_Foot0_Top",
                    ),
            "True", "Jubes_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Jubes_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Ass",
                    "action_speed", "Jubes_Doggy_Anal_Head_Ass",
                    "True", "Jubes_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Jubes_Doggy_Fuck_Ass",
                    "True", "Jubes_Doggy_Ass",
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Jubes_Doggy_Foot2_Ass",
                    "action_speed", "Jubes_Doggy_Foot1_Ass",
                    "True", "Jubes_Doggy_Foot0_Ass",
                    ),
            "True", "Jubes_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            "Player.Cock == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Jubes_Doggy_Feet2",
                    "action_speed", "Jubes_Doggy_Feet1",
                    "True", "Jubes_Doggy_Feet0",
                    ),
            "not Player.Sprite and ShowFeet", "Jubes_Doggy_Shins",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
    #yoffset 50


image Jubes_Doggy_Body:
    LiveComposite(
        #Upper body
        (610,750),
        #(165,0),"Jubes_Doggy_Hair_Under", #back of the hair
        (0,60), "Jubes_Doggy_Head",               #Head

        #(0,0), "images/JubesDoggy/Jubes_Doggy_HeadRef.png",               #Head

        (0,0), "images/JubesDoggy/Jubes_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #tanktop
            "not JubesX.Chest", Null(),
#            "JubesX.Uptop", ConditionSwitch(
#                    "JubesX.Chest == 'lace bra' and JubesX.Over", "images/JubesDoggy/Jubes_Doggy_Chest_GreenBra_Up2.png",
#                    "JubesX.Chest == 'lace bra'", "images/JubesDoggy/Jubes_Doggy_Chest_GreenBra_Up.png",
#                    "JubesX.Chest == 'corset'", "images/JubesDoggy/Jubes_Doggy_Chest_Corset_Up.png",
#                    "JubesX.Chest == 'sports bra'", "images/JubesDoggy/Jubes_Doggy_Chest_SportsBra_Up.png",
#                    "JubesX.Chest == 'bikini top'", "images/JubesDoggy/Jubes_Doggy_Chest_Bikini_Up.png",
#                    "JubesX.Over", "images/JubesDoggy/Jubes_Doggy_Chest_GreenBra_Up2.png",
#                    "True", "images/JubesDoggy/Jubes_Doggy_Chest_GreenBra_Up.png",
#                    ),
            "JubesX.Chest == 'white tank'", "images/JubesDoggy/Jubes_Doggy_Chest_Costume.png",
            "JubesX.Chest == 'lace corset'", "images/JubesDoggy/Jubes_Doggy_Chest_Corset.png",
            "JubesX.Chest == 'corset'", "images/JubesDoggy/Jubes_Doggy_Chest_Corset.png",
            "JubesX.Chest == 'wolvie top'", "images/JubesDoggy/Jubes_Doggy_Chest_Wolvie.png",
            "JubesX.Chest == 'bikini top'", "images/JubesDoggy/Jubes_Doggy_Chest_Bikini.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Chest_Tank.png",
            ),
#        (0,0), ConditionSwitch(
#            #Wet look
#            "JubesX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #suspenders
            "not JubesX.Legs", Null(), #hides when no skirt on
            "JubesX.Acc == 'suspenders'", "images/JubesDoggy/Jubes_Doggy_Suspenders.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #gloves
            "JubesX.Arms == 'gloves'", "images/JubesDoggy/Jubes_Doggy_Gloves.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not JubesX.Over", Null(),
            "JubesX.Over == 'jacket'", "images/JubesDoggy/Jubes_Doggy_Over_Jacket.png",
            "JubesX.Over == 'towel' and not JubesX.Uptop", "images/JubesDoggy/Jubes_Doggy_Over_TowelTop.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #spunk back Layer
            "'back' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "primary_action == 'fondle breasts' or offhand_action == 'fondle breasts'", "Jubes_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Jubes_Doggy_Head",               #Head
        #(165,0),"Jubes_Doggy_Hair_Over", #front of the hair
        )
#    transform_anchor True
#    anchor (225,1400)
    offset (-200,0)#(-190,-40)
#    offset (-350,-180)#(-190,-40)
#    rotate 20


image Jubes_Doggy_Head:
    LiveComposite(
        #Head
        (420,525),
        #(0,0), "images/JubesDoggy/Jubes_Doggy_Head.png", #Body base
        #(0,0), "images/JubesDoggy/Jubes_Doggy_TestArm.png",#Eyes
        (0,0), ConditionSwitch(
            #Hair
            "JubesX.Water or JubesX.Hair == 'wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Wet_Back.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Hair_Long_Back.png",
            ),
        (0,0), ConditionSwitch(
            #Head
            #"JubesX.Blush > 1", "images/JubesDoggy/Jubes_Doggy_Head_Blush2.png",
            "JubesX.Blush", "images/JubesDoggy/Jubes_Doggy_Head_Blush.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "JubesX.Mouth == 'normal'", "images/JubesDoggy/Jubes_Doggy_Mouth_Smile.png",
            "JubesX.Mouth == 'lipbite'", "images/JubesDoggy/Jubes_Doggy_Mouth_Smile.png",
            "JubesX.Mouth == 'sucking'", "images/JubesDoggy/Jubes_Doggy_Mouth_Open.png",
            "JubesX.Mouth == 'kiss'", "images/JubesDoggy/Jubes_Doggy_Mouth_Kiss.png",
            "JubesX.Mouth == 'sad'", "images/JubesDoggy/Jubes_Doggy_Mouth_Sad.png",
            "JubesX.Mouth == 'smile'", "images/JubesDoggy/Jubes_Doggy_Mouth_Smile.png",
            "JubesX.Mouth == 'grimace'", "images/JubesDoggy/Jubes_Doggy_Mouth_Smile.png",
            "JubesX.Mouth == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Mouth_Open.png",
            "JubesX.Mouth == 'tongue'", "images/JubesDoggy/Jubes_Doggy_Mouth_Tongue.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Mouth_Smile.png",
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #Mouth spunk
#            "'mouth' not in JubesX.Spunk", Null(),
#            #"JubesX.Mouth == 'normal'", "images/JubesDoggy/Jubes_Doggy_Spunk_Normal.png",
#            #"JubesX.Mouth == 'sad'", "images/JubesDoggy/Jubes_Doggy_Spunk_Normal.png",
#            "JubesX.Mouth == 'lipbite'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
#            "JubesX.Mouth == 'smile'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
#            "JubesX.Mouth == 'grimace'", "images/JubesDoggy/Jubes_Doggy_Spunk_Smile.png",
#            "JubesX.Mouth == 'sucking'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
#            #"JubesX.Mouth == 'kiss'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
#            "JubesX.Mouth == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
#            "JubesX.Mouth == 'tongue'", "images/JubesDoggy/Jubes_Doggy_Spunk_Open.png",
#            "True", "images/JubesDoggy/Jubes_Doggy_Spunk_Normal.png",
#            ),
        (0,0), ConditionSwitch(
            #Brows
            #"JubesX.Brows == 'normal'", "images/JubesDoggy/Jubes_Doggy_Brows_Normal.png",
            "JubesX.Brows == 'angry'", "images/JubesDoggy/Jubes_Doggy_Brows_Angry.png",
            "JubesX.Brows == 'sad'", "images/JubesDoggy/Jubes_Doggy_Brows_Sad.png",
            "JubesX.Brows == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Brows_Surprised.png",
            #"JubesX.Brows == 'confused'", "images/JubesDoggy/Jubes_Doggy_Brows_Normal.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Brows_Normal.png",
            ),
        (0,0), "Jubes Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #Wet look
#            "JubesX.Water", "images/RogueDoggy/Rogue_Doggy_WetTop.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'facial' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair
            "JubesX.Water or JubesX.Hair == 'wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Wet.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Hair_Long.png",
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    #zoom 0.95
    #alpha 0.5

#image Jubes_Doggy_Hair_Under:
#        #hair under body
#        ConditionSwitch(
#                "JubesX.Water or JubesX.Hair == 'wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Wet_Under.png",
#                "True", "images/JubesDoggy/Jubes_Doggy_Hair_Short_Under.png",
#                )
#        zoom 0.83

#image Jubes_Doggy_Hair_Over:
#        #hair under body
#        contains:
#            ConditionSwitch(
#                    "JubesX.Water or JubesX.Hair == 'wet'", "images/JubesDoggy/Jubes_Doggy_Hair_Wet_Over.png",
#                    "True", "images/JubesDoggy/Jubes_Doggy_Hair_Short_Over.png",
#                    )
#        contains:
#            ConditionSwitch(
#                #face spunk
#                "'facial' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Facial.png",
#                "True", Null(),
#                )
#        contains:
#            ConditionSwitch(
#                #face spunk
#                "'hair' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Facial2.png",
#                "True", Null(),
#                )
#        zoom 0.83
#        #alpha 0.7

image Jubes Doggy Blink:
        #Eyes
        ConditionSwitch(
        "JubesX.Eyes == 'sexy'", "images/JubesDoggy/Jubes_Doggy_Eyes_Sexy.png",
        "JubesX.Eyes == 'side'", "images/JubesDoggy/Jubes_Doggy_Eyes_Side.png",
        "JubesX.Eyes == 'normal'", "images/JubesDoggy/Jubes_Doggy_Eyes_Sexy.png",
        "JubesX.Eyes == 'closed'", "images/JubesDoggy/Jubes_Doggy_Eyes_Closed.png",
        "JubesX.Eyes == 'manic'", "images/JubesDoggy/Jubes_Doggy_Eyes_Stunned.png",
        "JubesX.Eyes == 'down'", "images/JubesDoggy/Jubes_Doggy_Eyes_Sexy.png",
        "JubesX.Eyes == 'stunned'", "images/JubesDoggy/Jubes_Doggy_Eyes_Stunned.png",
        "JubesX.Eyes == 'surprised'", "images/JubesDoggy/Jubes_Doggy_Eyes_Surprised.png",
        "JubesX.Eyes == 'squint'", "images/JubesDoggy/Jubes_Doggy_Eyes_Sexy.png",
        "True", "images/JubesDoggy/Jubes_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/JubesDoggy/Jubes_Doggy_Eyes_Closed.png"
        .25
        repeat

image Jubes_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
#        (0,0), ConditionSwitch(
#            #Legs backside
#            "JubesX.Legs == 'skirt'","images/JubesDoggy/Jubes_Doggy_Legs_Skirt_Back.png",
#            "not JubesX.Upskirt", Null(),
#            "JubesX.Legs == 'pants'", "images/JubesDoggy/Jubes_Doggy_Legs_Pants_Back.png",
#            "JubesX.Legs == 'yoga pants'", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga_Back.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Panties back
            "not JubesX.PantiesDown or (JubesX.Legs == 'pants' and not JubesX.Upskirt)", Null(),
            "JubesX.Panties == 'wolvie panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie_Back.png",
            "JubesX.Panties == 'lace panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Lace_Back.png",
            "JubesX.Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Back.png",
            "True", Null(),
            ),
        (0,0), "images/JubesDoggy/Jubes_Doggy_Ass.png", #Ass Base
#        (0,0), ConditionSwitch(
#            #Wet look
#            "JubesX.Water", "images/RogueDoggy/Rogue_Doggy_WetAss.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "JubesX.Hose == 'black stockings'", "images/JubesDoggy/Jubes_Doggy_Stocking.png",
            "JubesX.Hose == 'stockings'", "images/JubesDoggy/Jubes_Doggy_Hose.png",
            "Player.Sprite and Player.Cock == 'in'", Null(),
            "Player.Sprite and Player.Cock == 'anal'", Null(),
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties if Down
            "not JubesX.PantiesDown or (JubesX.Legs == 'pants' and not JubesX.Upskirt)", Null(),
            "JubesX.Panties == 'wolvie panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie_Down.png",
            "JubesX.Panties == 'bikini bottoms'", "images/JubesDoggy/Jubes_Doggy_Panties_Bikini_Down.png",
            "JubesX.Panties", "images/JubesDoggy/Jubes_Doggy_Panties_Black_Down.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Composite
            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'", "Jubes_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Jubes_Pussy_Fucking2",
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Pussy_Fucking3",#action_speed 3
                    "action_speed > 1", "Jubes_Pussy_Fucking2",#action_speed 2
                    "action_speed", "Jubes_Pussy_Heading",      #action_speed 1
                    "True", "Jubes_Pussy_Static",              #action_speed 0
                    ),
            "primary_action == 'lick pussy'", "images/JubesDoggy/Jubes_Doggy_Pussy_Open.png",
            "JubesX.Legs and not JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Pussy_Closed.png",
            "JubesX.Panties and not JubesX.PantiesDown", "images/JubesDoggy/Jubes_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'", "Jubes_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Jubes_Pussy_Fucking2",
            "True", "images/JubesDoggy/Jubes_Doggy_Pussy_Closed.png",
            ),


        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in JubesX.Spunk and Player.Cock == 'in'",Null(),# "images/JubesDoggy/Jubes_Doggy_SpunkPussyOpen.png",  #fix for JubesX.Spunk is used later
            "'in' in JubesX.Spunk ", "images/JubesDoggy/Jubes_Doggy_SpunkPussyClosed.png",
            "JubesX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "JubesX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not JubesX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/JubesDoggy/Jubes_Doggy_Pubes_Fucked.png",
            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "JubesX.Legs == 'pants' and not JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Pubes_Panties.png",
            "JubesX.PantiesDown and primary_action == 'lick pussy'", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png",
            "JubesX.PantiesDown", "images/JubesDoggy/Jubes_Doggy_Pubes.png",
            "JubesX.Panties", "images/JubesDoggy/Jubes_Doggy_Pubes_Panties.png",
            "JubesX.Hose and JubesX.Hose != 'stockings'", "images/JubesDoggy/Jubes_Doggy_Pubes_Panties.png",
            "primary_action == 'lick pussy'", "images/JubesDoggy/Jubes_Doggy_Pubes_Open.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_Ring.png",
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_Barbell.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Anus Composite
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Jubes_Anal_Fucking2", #action_speed 3
                    "action_speed > 1", "Jubes_Anal_Fucking",  #action_speed 2
                    "action_speed", "Jubes_Anal_Heading",      #action_speed 1
                    "True", "Jubes_Anal",               #action_speed 0
                    ),
#            "Action == 'plug'", "Jubes_Anal_Plug",
#            "Action == 'plug'", "test_case",
            "JubesX.Legs and not JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
            "JubesX.Panties and not JubesX.PantiesDown", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
            "primary_action == 'insert ass' or offhand_action == 'insert ass'", "Jubes_Anal_Fingering",
            "primary_action == 'dildo anal'", "Jubes_Anal_Fucking",
            "JubesX.Loose", "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Asshole_Tight.png",
            ),


        (0,0), ConditionSwitch(
            #spunkanal Layer
            "'anal' not in JubesX.Spunk or Player.Sprite", Null(),
            "Player.Cock == 'anal'", "images/JubesDoggy/Jubes_Doggy_SpunkAnalOpen.png",
            "JubesX.Loose", "images/JubesDoggy/Jubes_Doggy_SpunkAnalLoose.png",
            "True", "images/JubesDoggy/Jubes_Doggy_SpunkAnalLoose.png",
            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "JubesX.PantiesDown or not JubesX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'",Null(),
#            "primary_action == 'dildo pussy'", Null(),
            "JubesX.Panties == 'wolvie panties' and JubesX.Wet", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie_Wet.png",
            "JubesX.Panties == 'wolvie panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Wolvie.png",
            "JubesX.Panties == 'lace panties'", "images/JubesDoggy/Jubes_Doggy_Panties_Lace.png",
            "JubesX.Panties == 'bikini bottoms'", "images/JubesDoggy/Jubes_Doggy_Panties_Bikini.png",
            "JubesX.Wet", "images/JubesDoggy/Jubes_Doggy_Panties_Black_Wet.png",
            "True", "images/JubesDoggy/Jubes_Doggy_Panties_Black.png",
            ),
#        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
#            #full hose/tights
#            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
##            "JubesX.Panties and JubesX.PantiesDown and JubesX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
#            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Hose_Garter.png",
#            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_Hose_StockingandGarter.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
##            "JubesX.Hose == 'tights' and JubesX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
##            "JubesX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
#            "JubesX.Hose == 'pantyhose'", "images/JubesDoggy/Jubes_Doggy_Hose_Full.png",
##            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
##            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "JubesX.Legs == 'leather pants'", ConditionSwitch(
                    "JubesX.Upskirt or JubesX.PantiesDown", Null(), #"images/JubesDoggy/Jubes_Doggy_Legs_Pants_Down.png",
                    #"JubesX.Wet > 1", "images/JubesDoggy/Jubes_Doggy_Legs_Pants_Wet.png",
                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_Pants.png",
                    ),
#            "JubesX.Legs == 'yoga pants'", ConditionSwitch(
#                    "JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga_Down.png",
#                    "JubesX.Wet > 1", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga_Wet.png",
#                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_Yoga.png",
#                    ),
            "JubesX.Legs == 'other skirt'", ConditionSwitch(
                    "JubesX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/JubesDoggy/Jubes_Doggy_Legs_SkirtCos_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Legs_SkirtCos_Up.png",
                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_SkirtCos.png",
                    ),
            "JubesX.Legs == 'skirt'", ConditionSwitch(
                    "JubesX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/JubesDoggy/Jubes_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Legs_Skirt_Up.png",
                    "True", "images/JubesDoggy/Jubes_Doggy_Legs_Skirt.png",
                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Over Layer
            "JubesX.Over == 'towel' and JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Over_TowelAss_Up.png",
            "JubesX.Over == 'towel'", "images/JubesDoggy/Jubes_Doggy_Over_TowelAss.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings clothed
            "Player.Sprite", Null(),
            "JubesX.PantiesDown or (not JubesX.Panties and JubesX.Legs != 'leather pants')", Null(), #if not panties or legs, skip this
            "JubesX.Pierce == 'ring'", "images/JubesDoggy/Jubes_Doggy_Pierce_RingC.png",
            "JubesX.Pierce == 'barbell'", "images/JubesDoggy/Jubes_Doggy_Pierce_BarbellC.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in JubesX.Spunk", "images/JubesDoggy/Jubes_Doggy_Spunk_Ass.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'lick pussy'", "Rogue_Doggy_Lick_Pussy",
            "primary_action == 'lick ass'", "Rogue_Doggy_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #Hotdogging underlayer
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "JubesX.Legs == 'skirt' and JubesX.Upskirt", "images/JubesDoggy/Jubes_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/JubesDoggy/Jubes_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "JubesX.Legs == 'skirt' and JubesX.Upskirt and action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "JubesX.Legs == 'skirt' and JubesX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            "action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            "True", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask.png"),
            ),
#        (0,0), ConditionSwitch(
#            #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        )


image Jubes_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Jubes_Doggy_Shins", "images/JubesDoggy/Jubes_Doggy_Feet_Toes.png")

image Jubes_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Jubes's footjob shins
    contains:
        "images/JubesDoggy/Jubes_Doggy_Feet_Back.png"
#    contains:
#        "images/JubesDoggy/Jubes_Doggy_Feet_Toes.png"
    contains:
            #hose legs
        ConditionSwitch(
            "not JubesX.Hose", Null(),
            "JubesX.Hose == 'stockings'", "images/JubesDoggy/Jubes_Doggy_Feet_Hose_Back.png",
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_Feet_Hose_Back.png",
            "JubesX.Hose == 'black stockings'", "images/JubesDoggy/Jubes_Doggy_Feet_Stockings_Back.png",
            "JubesX.Hose == 'pantyhose'", "images/JubesDoggy/Jubes_Doggy_Feet_Hose_Back.png",
            "True", Null(),
            )
    contains:
        #pants
        ConditionSwitch(
            "JubesX.Legs == 'leather pants'", "images/JubesDoggy/Jubes_Doggy_Feet_Pants.png",
            "True", Null(),
            )
#    pos (0,0)

#image Jubes_Doggy_Lick_Pussy:
#        "Lick_Anim"
#        zoom 0.5
#        offset (195,540)

#image Jubes_Doggy_Lick_Ass:
#        "Lick_Anim"
#        zoom 0.5
#        offset (195,500)

image Jubes_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (270,410)#(150,340)
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

image Zero_Jubes_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Jubes_Hotdog_Moving:
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

image Zero_Jubes_Doggy_Static:
    # Sex action_speed 0 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (169,545)
        block:
            ease 1 ypos 540 #in stroke
            pause 1
            ease 3 ypos 545 #out stroke
            repeat

image Zero_Jubes_Doggy_Heading:
    # Sex action_speed 1 motions
    contains:
        subpixel True
        "Zero_Doggy_Insert"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat

image Zero_Jubes_Doggy_Fucking2:
    # Sex action_speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Jubes_Doggy_Fucking3:
    # Sex action_speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Jubes_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Jubes_Pussy_Moving"
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

image Jubes_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Jubes_Pussy_Moving"
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
#image Jubes_Pussy:
#    #Full Animation for speed 0
#    contains:
#        #Base
#        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
#    contains:
#        ConditionSwitch(
#            #full hose/tights
#            "JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
#            "JubesX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
##            "JubesX.Hose == 'tights' and JubesX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
##            "JubesX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
##            "JubesX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
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


image Jubes_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:
        #moving hole
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
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jubes_Doggy_Static", "Jubes_Pussy_Mask_Static")

    contains:
        # expanding pussy flap
        AlphaMask("Jubes_PussyHole_Static", "Jubes_Pussy_Hole_Mask_Static")

image Jubes_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Jubes_Pussy_Moving"
    contains:
        #Base
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

image Jubes_PussyHole_Static:
    #This is the image impacted by the mask for the pussy flap in "Jubes_Pussy_Moving"
    contains:
        #Mask
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
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
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
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jubes_Doggy_Heading", "Jubes_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Jubes_Pussy_Heading_Flap", "Jubes_Pussy_Hole_Mask")


image Jubes_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Jubes_Pussy_Heading"
    contains:
        #Base
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
    #This is the image impacted by the mask for the pussy flap in "Jubes_Pussy_Heading"
    contains:
        #Mask
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
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .9#1
            pause 1
            ease 3 xzoom .6
            repeat
#    contains:
#        ConditionSwitch(
#            #full hose/tights
#            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Stockings_Loose.png",
#            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_Stockings.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/JubesDoggy/Jubes_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/JubesDoggy/Jubes_Doggy_Tights_Holed.png",
#            "True", Null(),
#            ),
    contains:
        #Cock
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Jubes_Pussy_Heading_Flap", "Jubes_Pussy_Hole_Mask")

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Jubes_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "primary_action == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Jubes_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
#        AlphaMask("Zero_Jubes_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")


image Jubes_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jubes_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

image Jubes_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Jubes_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75#1
            pause .5
            ease 1.5 zoom .6
            repeat
#    contains:
#        ConditionSwitch(
#            #full hose/tights
#            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Stockings_Loose.png",
#            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_Stockings.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/JubesDoggy/Jubes_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/JubesDoggy/Jubes_Doggy_Tights_Holed.png",
#            "True", Null(),
#            )
    contains:
        #Cock with mask
        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Jubes_Anal_Heading:
    #Animation for speed 1
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
    contains:
        #Hole
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
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock masking fixer (for when the bottom part tries to cut off)
        AlphaMask("Zero_Jubes_Doggy_Anal_Heading", "Zero_Jubes_Doggy_Anal_HeadingJunk")
    contains:
        #Cock with mask
        AlphaMask("Zero_Jubes_Doggy_Anal_Heading", "Jubes_Doggy_Anal_Heading_Mask")

image Zero_Jubes_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Jubes_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Jubes_Doggy_Anal_Heading_Mask:
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

image Jubes_Doggy_Anal_Head_Top:
#animation for anal fucking top half
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
    #animation for anal fucking ass half
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Jubes_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Jubes_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
    contains:
        #Cheeks
        "images/JubesDoggy/Jubes_Doggy_Anal_FullCheeks.png"
    contains:
        #Hole
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "primary_action == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Jubes_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),
#        AlphaMask("Zero_Jubes_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Jubes_Doggy_Anal_FullMask:   #unused anymore?
    contains:
        #Mask
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png" #FullMask?
    contains:
        #Cheeks
        "images/JubesDoggy/Jubes_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )

image Jubes_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Jubes_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Jubes_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Jubes_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Base
        "images/JubesDoggy/Jubes_Doggy_Anal_FullBase.png"
#    contains:
#        #Mask
#        "images/JubesDoggy/Jubes_Doggy_Anal_FullMask.png"
    contains:
        #Cheeks
        "images/JubesDoggy/Jubes_Doggy_Anal_FullCheeks.png"
    contains:
        #Hole
        "images/JubesDoggy/Jubes_Doggy_Anal_FullHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "JubesX.Hose == 'stockings and garterbelt'", "images/JubesDoggy/Jubes_Doggy_StockingsGarter.png",
            "JubesX.Hose == 'garterbelt'", "images/JubesDoggy/Jubes_Doggy_Garters.png",
#            "JubesX.Panties and JubesX.PantiesDown", Null(),
#            "JubesX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "JubesX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Jubes_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Jubes_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
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
    #animation for anal fucking2 ass half
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


# Footjob animations > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Jubes_Doggy_Feet0:
    #static animation
    contains:
        "Jubes_Doggy_Shins"
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
        "Jubes_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Jubes_Doggy_Feet1:
    #slow animation
    contains:
        "Jubes_Doggy_Shins"
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
        "Jubes_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Jubes_Doggy_Feet2:
    #fast animation
    contains:
        "Jubes_Doggy_Shins"
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
        "Jubes_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >


image Jubes_Doggy_Foot0_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 10#28
        #pause .4
#        block:
#            pause .5
#            ease 2 ypos 20
#            pause .5
#            ease 2 ypos 10
#            repeat

image Jubes_Doggy_Foot0_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block:     #total 3
            pause 1 #.5
            ease 2 ypos 20
            pause .5
            ease 1.5 ypos 0
            repeat

image Jubes_Doggy_Foot1_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 70#28
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 70
            repeat

image Jubes_Doggy_Foot1_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 0
        block: #total 3
            pause .3
            ease 2 ypos 80
            ease .7 ypos 0
            repeat

image Jubes_Doggy_Foot2_Top:
    #animation for footjob top half
    contains:
        subpixel True
        "Jubes_Doggy_Body"
        ypos 70#28
#        pause .4
#        block:
#            ease .2 ypos 5#10
#            pause .3
#            ease 2 ypos 15#28
#            repeat
        block:
            pause .05
            ease .6 ypos 90#90#110
            ease .3 ypos 70#70
            repeat

image Jubes_Doggy_Foot2_Ass:
    #animation for footjob ass half
    contains:
        subpixel True
        "Jubes_Doggy_Ass"
        ypos 70
        block: #total .95
            pause .15#.05
            ease .6 ypos 90#110
            ease .2 ypos 70
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Jubes_Doggy_Launch(line = primary_action):
    return #fix, temporary
    if renpy.showing("Jubes_Doggy_Animation"):
        return
    $ action_speed = 0
    call Jubes_Hide(1)
    show Jubes_Doggy_Animation at sprite_location(StageCenter+150) zorder 150
    with dissolve
    return

label Jubes_Doggy_Reset:
    if not renpy.showing("Jubes_Doggy_Animation"):
        return
#    $ primary_action = 0               #fix, not sure this is a good idea
    $ JubesX.ArmPose = 2
    $ JubesX.SpriteVer = 0
    hide Jubes_Doggy_Animation
    call Jubes_Hide
    show Jubes_Sprite at sprite_location(JubesX.sprite_location) zorder JubesX.Layer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    with dissolve
    $ action_speed = 0
    return

# End Jubes Doggy Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Jubes Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jubes Sex element //////////////////////////////////////////////////////////////////////////// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_SexSprite:
    #core sex animation
    contains:
        ConditionSwitch(
            # Jubes's upper body
            "Player.Cock == 'in'", ConditionSwitch(
                    # If during sex
                    "action_speed == 1", "Jubes_Sex_Body_S1",#heading
                    "action_speed == 2", "Jubes_Sex_Body_S2",#slow
                    "action_speed == 3", "Jubes_Sex_Body_S3",#fast
                    "action_speed >= 4", "Jubes_Sex_Body_S4",#cumming
                    "True",       "Jubes_Sex_Body_S0",#Static
                    ),
            "Player.Cock == 'anal'", ConditionSwitch(
#                    # If during Anal
                    "action_speed == 1", "Jubes_Sex_Body_A1",#heading
                    "action_speed == 2", "Jubes_Sex_Body_A2",#slow
                    "action_speed == 3", "Jubes_Sex_Body_A3",#fast
                    "action_speed >= 4", "Jubes_Sex_Body_A4",#cumming
                    "True",       "Jubes_Sex_Body_A0",#Static
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    # If during Footjob
                    "not Player.Sprite","Jubes_Sex_Body_F0",#Static
                    "action_speed == 1", "Jubes_Sex_Body_F1",#heading
                    "action_speed >= 4", "Jubes_Sex_Body_F0",#cumming
                    "action_speed >= 2", "Jubes_Sex_Body_F2",#slow
                    "True",       "Jubes_Sex_Body_F0",#Static
                    ),

            "True", ConditionSwitch(
                    # If neither
                    "not Player.Sprite","Jubes_Sex_Body_H0",#Static
                    "action_speed == 1", "Jubes_Sex_Body_H1",#slow
                    "action_speed == 4", "Jubes_Sex_Body_H0",#cumming
                    "action_speed >= 2", "Jubes_Sex_Body_H2",#fast
                    "True",       "Jubes_Sex_Body_H0",#Static
                    ),
            )
    contains:
        ConditionSwitch(
            # Jubes's lower body
            "Player.Cock == 'in'", ConditionSwitch(
                    # If during sex
                    "action_speed == 1", "Jubes_Sex_Legs_S1",#heading
                    "action_speed == 2", "Jubes_Sex_Legs_S2",#slow
                    "action_speed == 3", "Jubes_Sex_Legs_S3",#fast
                    "action_speed >= 4", "Jubes_Sex_Legs_S4",#cumming
                    "True", "Jubes_Sex_Legs_S0",#Static
                    ),
            "Player.Cock == 'anal'", ConditionSwitch(
                    # If during Anal
                    "action_speed == 1", "Jubes_Sex_Legs_A1",#heading
                    "action_speed == 2", "Jubes_Sex_Legs_A2",#slow
                    "action_speed == 3", "Jubes_Sex_Legs_A3",#fast
                    "action_speed >= 4", "Jubes_Sex_Legs_A4",#cumming
                    "True", "Jubes_Sex_Legs_A0",#Static
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(
                    # If during Footjob
                    "not Player.Sprite","Jubes_Sex_Legs_F0",#Static
                    "action_speed == 1", "Jubes_Sex_Legs_F1",#heading
                    "action_speed >= 4", "Jubes_Sex_Legs_F0",#cumming
                    "action_speed >= 2", "Jubes_Sex_Legs_F2",#slow
                    "True",       "Jubes_Sex_Legs_F0",#Static
                    ),
            "True", ConditionSwitch(
                    # If neither
                    "not Player.Sprite","Jubes_Sex_Legs_H0",#Static
                    "action_speed == 1", "Jubes_Sex_Legs_H1",#heading
                    "action_speed == 4", "Jubes_Sex_Legs_H0",#cumming
                    "action_speed >= 2", "Jubes_Sex_Legs_H2",#slow
                    "True", "Jubes_Sex_Legs_H0",#Static
                    ),
            )
    zoom .6 #0.6
    transform_anchor True
    anchor (.5,.5)
#    rotate -30

image Jubes_Sex_HairBack:
    #Hair underlay
    "Jubes_Sprite_HairBack"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)

image Jubes_Sex_Head:
    #Hair underlay
    "Jubes_Sprite_Head"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)



image Jubes_Sex_Body:
    #Her torso for the sex pose
    contains:
            "Jubes_Sex_HairBack"
    contains:
            # hand
#            "images/JubesSex/Jubes_Sex_Hand.png"

            ConditionSwitch(
                    "Player.Cock == 'foot'", Null(),
                    "JubesX.Arms == 'gloves'", "images/JubesSex/Jubes_Sex_Hand_Gloved.png",
                    "True", "images/JubesSex/Jubes_Sex_Hand.png"
                    )
    contains:
            # Over under layer
        ConditionSwitch(
            "not JubesX.Over", Null(),
            "JubesX.Uptop", ConditionSwitch(
                    #if uptop
                    "JubesX.Over == 'jacket'", "images/JubesSex/Jubes_Sex_Jacket_Back_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if not uptop
                    "JubesX.Over == 'jacket'", "images/JubesSex/Jubes_Sex_Jacket_Back.png",
                    "True", Null(),
                    ),
            )
    contains:
            # body
            "images/JubesSex/Jubes_Sex_Body.png"
    contains:
            # piercings tits
        ConditionSwitch(
            "not JubesX.Pierce", Null(),
            "JubesX.Pierce == 'barbell'", "images/JubesSex/Jubes_Sex_Barbell_Tits.png",
            "JubesX.Pierce == 'ring'", "images/JubesSex/Jubes_Sex_Ring_Tits.png",
            "True", Null(),
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(
            "JubesX.Neck == 'leash choker'", "images/JubesSex/Jubes_Sex_Leash.png",
            "True", Null(),
            )
    contains:
            # garters
        ConditionSwitch(
            "JubesX.Hose == 'stockings and garterbelt' or JubesX.Hose == 'garterbelt'", "images/JubesSex/Jubes_Sex_Garter.png",
            "True", Null(),
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(
            "not JubesX.Chest", Null(),
            "JubesX.Uptop",ConditionSwitch(
                    #if the top is up. . .
                    "not JubesX.Chest", Null(),
                    "JubesX.Chest == 'white tank'", "images/JubesSex/Jubes_Sex_WhiteTank_Up.png",
                    "JubesX.Chest == 'leather bra'", "images/JubesSex/Jubes_Sex_Bra_Leather_Up.png",
                    "JubesX.Chest == 'wolvie top'", "images/JubesSex/Jubes_Sex_Top_Wolvie_Up.png",
                    "JubesX.Chest == 'corset'", "images/JubesSex/Jubes_Sex_Corset_Up.png",
                    "JubesX.Chest == 'lace corset'", "images/JubesSex/Jubes_Sex_Corset_Lace_Up.png",
                    "JubesX.Chest == 'bikini top'", "images/JubesSex/Jubes_Sex_Top_Bikini_Up.png",
#                    "JubesX.Chest == 'sports bra'", "images/JubesSex/Jubes_Sex_Bra_Sports_Up.png",
#                    "JubesX.Chest == 'lace bra'", "images/JubesSex/Jubes_Sex_Bra_Lace_Up.png",
                    "True", Null(),
                    ),
            # else. . .
            "JubesX.Chest == 'white tank'", "images/JubesSex/Jubes_Sex_WhiteTank.png",
            "JubesX.Chest == 'leather bra'", "images/JubesSex/Jubes_Sex_Bra_Leather.png",
            "JubesX.Chest == 'wolvie top'", "images/JubesSex/Jubes_Sex_Top_Wolvie.png",
            "JubesX.Chest == 'corset'", "images/JubesSex/Jubes_Sex_Corset.png",
            "JubesX.Chest == 'lace corset'", "images/JubesSex/Jubes_Sex_Corset_Lace.png",
            "JubesX.Chest == 'bikini top'", "images/JubesSex/Jubes_Sex_Top_Bikini.png",
#            "JubesX.Chest == 'sports bra'", "images/JubesSex/Jubes_Sex_Bra_Sports.png",
#            "JubesX.Chest == 'lace bra'", "images/JubesSex/Jubes_Sex_Bra_Lace.png",
            "True", Null(),
            )
    contains:
            # piercings tits over clothes
        ConditionSwitch(
            "not JubesX.Pierce or JubesX.Uptop", Null(),
            "JubesX.Pierce == 'barbell'", "images/JubesSex/Jubes_Sex_Barbell_Tits_C.png",
            "JubesX.Pierce == 'ring'", "images/JubesSex/Jubes_Sex_Ring_Tits_C.png",
            "True", Null(),
            )
    contains:
            # suspenders
        ConditionSwitch(
            "not JubesX.Legs", Null(), #hides when no skirt on
            "JubesX.Acc == 'suspenders' and not JubesX.Chest and not JubesX.Uptop", "images/JubesSex/Jubes_Sex_Suspenders.png",
            "JubesX.Acc == 'suspenders2'", "images/JubesSex/Jubes_Sex_Suspenders.png",
            "JubesX.Acc == 'suspenders'", "images/JubesSex/Jubes_Sex_Suspenders_Up.png",
            "True", Null(),
            )
    contains:
            # Over clothing layer
        ConditionSwitch(
            "not JubesX.Over", Null(),
            "JubesX.Uptop", ConditionSwitch(
                    #if uptop
                    "JubesX.Over == 'jacket'", "images/JubesSex/Jubes_Sex_Jacket_Up.png",
#                    "JubesX.Over == 'towel'", "images/JubesSex/Jubes_Sex_Towel_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    #if not uptop
                    "JubesX.Over == 'jacket'", "images/JubesSex/Jubes_Sex_Jacket.png",
#                    "JubesX.Over == 'towel'", "images/JubesSex/Jubes_Sex_Towel.png",
                    "True", Null(),
                    ),
            )
    contains:
            # spunk
        ConditionSwitch(
            "'belly' in JubesX.Spunk", "images/JubesSex/Jubes_Sex_Spunk_Belly.png",
            "True", Null(),
            )
    contains:
            # spunk on tits
            ConditionSwitch(
                "'tits' not in JubesX.Spunk", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Tits.png",
                )
    contains:
            ConditionSwitch(
                #breast licking animation
                "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Jubes_Sex_Lick_Breasts",
                "True", Null()
                )
    contains:
            ConditionSwitch(
                #breast fondling animation
                "primary_action == 'fondle breasts' or offhand_action == 'fondle breasts'", "Jubes_Sex_Fondle_Breasts",
                "True", Null()
                )
    contains:
            "Jubes_Sex_Head"
    transform_anchor True
    zoom .9 #1
    offset (55,55)
#    rotate 30
#end Jubes Body base

image Jubes_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.7
        offset (565,290)#(450,270)

image Jubes_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.5
        offset (360,-280)#(320,-130)

image Jubes_Sex_Legs:
    #Her Legs during sex
    contains:
            # legs under
        ConditionSwitch(
            "JubesX.Legs == 'skirt'", "images/JubesSex/Jubes_Sex_Skirt_Back.png",
            "True", Null(),
            )
#    contains:
#            # spunk
#        ConditionSwitch(
#            "'anal' in JubesX.Spunk or 'in' in JubesX.Spunk", "images/JubesSex/Jubes_Spunk_Sex.png",
#            "True", Null(),
#            )
    contains:
            # Legs base
        ConditionSwitch(
            "Player.Cock == 'foot'", "images/JubesSex/Jubes_Sex_Legs_Foot.png",
            "True", "images/JubesSex/Jubes_Sex_Legs_High.png",
            )
    contains:
            # anus
        ConditionSwitch(
            "Player.Cock == 'anal' and action_speed > 1", "images/JubesSex/Jubes_Sex_Anus_L.png", #and speed above heading?
            "Player.Cock == 'anal' and action_speed > 0", "images/JubesSex/Jubes_Sex_Anus_M.png", #and speed above heading?
            "'anal' in JubesX.Spunk", "images/JubesSex/Jubes_Sex_Anus_M.png", # If it's full. . .
            "True", "images/JubesSex/Jubes_Sex_Anus_S.png",
            )
    contains:
            # anal spunk
        ConditionSwitch(
            "'anal' not in JubesX.Spunk", Null(),
            "Player.Cock == 'anal' and action_speed > 1", "images/JubesSex/Jubes_Sex_Spunk_Anal_U.png", #speed above heading?
            "True", "images/JubesSex/Jubes_Sex_Spunk_Anal.png",
            )
    contains:
            # pussy
        ConditionSwitch(
            "Player.Cock == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Pussy_Open.png", #and speed above heading?
            "Player.Cock == 'in' and action_speed > 0", "images/JubesSex/Jubes_Sex_Pussy_Mid.png", #and speed heading?
            "primary_action == 'lick pussy'", "images/JubesSex/Jubes_Sex_Pussy_Mid.png", #pussy licking
            "True", "images/JubesSex/Jubes_Sex_Pussy_Closed.png",
            )
    contains:
            # pussy wetness
        ConditionSwitch(
            "not JubesX.Wet", Null(),
            "True", "images/JubesSex/Jubes_Sex_Wet.png",
            )
    contains:
            # pussy spunk
        ConditionSwitch(
            "'in' not in JubesX.Spunk", Null(),
            "Player.Cock == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Spunk_Pussy_Open.png", #and speed above heading?
            "True", "images/JubesSex/Jubes_Sex_Spunk_Pussy.png",
            )
    contains:
            # pubes
        ConditionSwitch(
            "not JubesX.Pubes", Null(),
            "Player.Cock == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Pubes_Open.png", #and speed above heading?
            "Player.Cock == 'in' and action_speed > 0", "images/JubesSex/Jubes_Sex_Pubes_Mid.png", #and speed heading?
            "primary_action == 'lick pussy'", "images/JubesSex/Jubes_Sex_Pubes_Mid.png", #pussy licking
            "True", "images/JubesSex/Jubes_Sex_Pubes_Closed.png",
            )
    contains:
            # piercings
        ConditionSwitch(
            "JubesX.Pierce == 'barbell' and Player.Cock == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Barbell_Pussy_O.png", #and speed above heading?
            "JubesX.Pierce == 'barbell'", "images/JubesSex/Jubes_Sex_Barbell_Pussy.png",
            "JubesX.Pierce == 'ring' and Player.Cock == 'in' and action_speed > 1", "images/JubesSex/Jubes_Sex_Ring_Pussy_O.png", #and speed above heading?
            "JubesX.Pierce == 'ring'", "images/JubesSex/Jubes_Sex_Ring_Pussy.png",
            "True", Null(),
            )
    contains:
            # panties
        ConditionSwitch(
            "JubesX.PantiesDown", Null(),
#            "JubesX.Panties == 'wolvie panties' and JubesX.Wet", "images/JubesSex/Jubes_Sex_Panties_Sport_SW.png",
            "JubesX.Panties == 'bikini bottoms'", "images/JubesSex/Jubes_Sex_Panties_Bikini.png",
            "JubesX.Panties == 'wolvie panties'", "images/JubesSex/Jubes_Sex_Panties_Wolvie.png",
            "JubesX.Panties == 'lace panties'", "images/JubesSex/Jubes_Sex_Panties_Lace.png",
            "JubesX.Panties", "images/JubesSex/Jubes_Sex_Panties_Black.png",
            "True", Null(),
            )
    contains:
            # hose base layer
        ConditionSwitch(
            "Player.Cock == 'foot' and (JubesX.Hose == 'stockings and garterbelt' or JubesX.Hose == 'stockings')", "images/JubesSex/Jubes_Sex_Stockings_Base_Foot.png",
            "Player.Cock == 'foot' and JubesX.Hose == 'black stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Base_Foot.png",
            "JubesX.Hose == 'black stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Base_Up.png",
            "JubesX.Hose == 'stockings and garterbelt' or JubesX.Hose == 'stockings'", "images/JubesSex/Jubes_Sex_Stockings_Base_Up.png",
            "True", Null(),
            )
    contains:
            # legs
        ConditionSwitch(
            "JubesX.Legs == 'skirt' or JubesX.Legs == 'other skirt'", "images/JubesSex/Jubes_Sex_Skirt.png",
            "JubesX.Upskirt", Null(),
            "JubesX.Legs == 'leather pants' and Player.Cock == 'foot'", "images/JubesSex/Jubes_Sex_Pants_Base_Foot.png",
            "JubesX.Legs == 'leather pants'", "images/JubesSex/Jubes_Sex_Pants_Base_Up.png",
            "True", Null(),
            )
    contains:
        ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'lick pussy'", "Jubes_Sex_Lick_Pussy",
            "primary_action == 'lick ass'", "Jubes_Sex_Lick_Ass",
            "True", Null()
            ),
    contains:
            # piercings
        ConditionSwitch(
#            "JubesX.Panties and JubesX.PantiesDown", Null(), #don't show if panties are down
#            "JubesX.Legs == 'skirt' or (JubesX.Legs and JubesX.Upskirt)", Null(), #don't show if pants are down
            "JubesX.Pierce == 'barbell'", "images/JubesSex/Jubes_Sex_Barbell_Pussy_C.png",
            "JubesX.Pierce == 'ring'", "images/JubesSex/Jubes_Sex_Ring_Pussy_C.png",
            "True", Null(),
            )
#    contains:
#            # Over
#        ConditionSwitch(
#            "JubesX.Over == 'nighty'", "images/JubesSex/Jubes_Sex_Nighty_Pussy.png",
#            "True", Null(),
#            )
    contains:
            # Feet
        ConditionSwitch(
            "Player.Cock == 'foot'", "Jubes_Footjob_Foot",
            "True", "Jubes_Sex_Foot",
            )
    transform_anchor True
    zoom 1
#    rotate 30
#    offset (0,0)
# End Jubes Legs base


image Jubes_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.8
        offset (720,610)#(530,510)

image Jubes_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.8
        offset (730,700)#(535,590)


image Jubes_Sex_Foot:
    #her vertical foot in the sex poses
#    contains:
#            # base
#            "images/JubesSex/Jubes_Sex_FootHigh.png"
    contains:
            # hose/foot
        ConditionSwitch(
            "JubesX.Hose == 'stockings and garterbelt' or JubesX.Hose == 'stockings'", "images/JubesSex/Jubes_Sex_Stockings_Up.png",
            "JubesX.Hose == 'black stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Up.png",
            "True", "images/JubesSex/Jubes_Sex_FootHigh.png" #base
            )
    contains:
            # legs
        ConditionSwitch(
            "JubesX.Upskirt", Null(),
            "JubesX.Legs == 'leather pants'", "images/JubesSex/Jubes_Sex_Pants_Up.png",
            "True", Null(),
            )
        xoffset  -2 #this shouldn't be needed, but otherwise there's a gap between the knee and leg.
    transform_anchor True
    zoom 1
#    alpha 0.2
    pos (988,-553)#(988,-553)

#image Jubes_Footjob_Foot:
#    #her movable foot in the footjob poses
#    contains:
#            # hose/base
#        ConditionSwitch(
#            "JubesX.Hose == 'stockings and garterbelt' or JubesX.Hose == 'stockings'", "images/JubesSex/Jubes_Sex_Stockings_Foot.png",
#            "True", "images/JubesSex/Jubes_Sex_Foot.png"
#            )
#    contains:
#            # legs
#        ConditionSwitch(
#            "JubesX.Upskirt", Null(),
#            "JubesX.Legs == 'leather pants'", "images/JubesSex/Jubes_Sex_Pants_Foot.png",
#            "True", Null(),
#            )
#    transform_anchor True
#    zoom 1

image Jubes_CockRef:
    "images/JubesSex/Jubes_Sex_Cocktest.png"
    alpha 0.8


# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_SexMask:
    transform_anchor True
    contains:
        "images/JubesSex/Jubes_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #303
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)

# Start S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_S0:
    #Her Body in the sex pose, static
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jubes_Sex_Legs_S0:
    # Her Legs in the Sex pose, static
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_S0", "Jubes_SexMask")
            subpixel True
            pos (525,465)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 460 #in 470
                easeout 0.5 ypos 461 #471
                easein 0.9 ypos 465 #out 475
                repeat
    # End Legs Sex static

image Jubes_Sex_Zero_Anim_S0:
    #this is the cock for Jubes's sex animation, action_speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,170)#125,75
        block: #total 4s
                ease 2 ypos 115#-50
                easeout .5 ypos 120#60
                easein 1.5 ypos 170
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_S1:
    #Her Body in the sex pose, heading
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jubes_Sex_Legs_S1:
    # Her Legs in the Sex pose, heading
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_S1", "Jubes_SexMask")
            subpixel True
            pos (525,485)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 480 #in 450
                easeout 0.5 ypos 481 #455
                easein 0.9 ypos 485 #out    #475
                repeat
    # End Legs Sex heading

image Jubes_Sex_Zero_Anim_S1:
    #this is the cock for Jubes's sex animation, action_speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 2s
                ease .5 ypos 90#-50
                easeout .5 ypos 100#60
                easein 1 ypos 115
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_Sex_Body_S2:
    #Her Body in the sex pose, slow
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,10) #top (0,-10)
        block:
            pause 0.3
            ease 0.3 ypos -10 #in
            pause 0.20
            ease 1.70 ypos 10 #out
            repeat

image Jubes_Sex_Legs_S2:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:
                pause 0.25
                ease 0.3 ypos -25 #in
                easeout 0.45 ypos -20
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_S2", "Jubes_SexMask")
            subpixel True
            pos (525,478)
            block:
                pause 0.25
                ease 0.3 ypos 453 #in
                easeout 0.45 ypos 458
                easein 1.5 ypos 478 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'in' not in JubesX.Spunk", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
            subpixel True
            pos (-15,-105) #top
            block:
                pause 0.25
                ease 0.3 ypos -130 #in
                easeout 0.45 ypos -125
                easein 1.5 ypos -105 #out
                repeat
    # End Legs Sex slow

image Jubes_Sex_Zero_Anim_S2:
    #this is the cock for Jubes's sex animation, action_speed 1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#100
                easein .5 ypos 75
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_S3:
    #Her Body in the sex pose, fast
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,10) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in -10
            pause 0.2
            ease .7 ypos 10 #out
            repeat

image Jubes_Sex_Legs_S3:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -45 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_S3", "Jubes_SexMask")
            subpixel True
            pos (525,478) #(525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 433 #in 450
                easeout 0.45 ypos 438 #455
                easein .5 ypos 478 #out
                repeat
#            block:#total 2.5s > 1.75 > 1.2
#                pause 0.05
#                ease 0.2 ypos 430 #in 450
#                easeout 0.45 ypos 435 #455
#                easein .5 ypos 475 #out
#                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'in' not in JubesX.Spunk", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
            subpixel True
            pos (-15,-105) #top(-15,-105)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -150 #in -45
                easeout 0.45 ypos -145 #-40
                easein .5 ypos -105 #out
                repeat
    # End Legs Sex fast

image Jubes_Sex_Zero_Anim_S3:
    #this is the cock for Jubes's sex animation, action_speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .5 ypos 0#60
                easein .5 ypos 75
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_S4:
    #Her Body in the sex pose, cumming
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,10) #top (0,10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 0 #in
            pause 0.2
            ease 1.7 ypos 10 #out
            repeat

image Jubes_Sex_Legs_S4:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_S4", "Jubes_SexMask")
            subpixel True
            pos (525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 460 #in 450
                easeout 0.45 ypos 465 #455
                easein 1.5 ypos 475 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'in' not in JubesX.Spunk", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
            subpixel True
            pos (-15,-105) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -120 #in -15
                easeout 0.45 ypos -115 #-10
                easein 1.5 ypos -105 #out
                repeat
    # End Legs Sex fast

image Jubes_Sex_Zero_Anim_S4:
    #this is the cock for Jubes's sex animation, action_speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Anal Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_A0:
    #Her Body in the anal pose, static
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jubes_Sex_Legs_A0:
    # Her Legs in the anal pose, static
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_A0", "Jubes_AnalMask")
            subpixel True
            pos (533,587) #538,580
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 585 #578
                easein 0.2 ypos 582 #out  575
                easeout 0.5 ypos 583 #576
                easein 0.9 ypos 587 #out  580
                repeat
    # End Legs anal static

image Jubes_Sex_Zero_Anim_A0:
    #this is the cock for Jubes's anal animation, action_speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,115
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


image Jubes_Sex_Body_A1:
    #Her Body in the anal pose, heading
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jubes_Sex_Legs_A1:
    # Her Legs in the anal pose, heading
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_A1", "Jubes_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 581 #455
                easein 0.2 ypos 578 #out
                easeout 0.5 ypos 579 #455
                easein 0.9 ypos 583 #out
                repeat
    # End Legs anal heading

image Jubes_Sex_Zero_Anim_A1:
    #this is the cock for Jubes's anal animation, action_speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 3s
                easeout 1.2 ypos 100
                easein .3 ypos 90
                easeout .5 ypos 100
                easein 1 ypos 115
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_A2:
    #Her Body in the anal pose, slow
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.3
            ease 0.3 ypos -20 #in
            pause 0.20
            ease 1.70 ypos 20 #out
            repeat

image Jubes_Sex_Legs_A2:
    # Her Legs in the anal pose, slow
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_A2", "Jubes_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos 545 #in 450
                easeout 0.45 ypos 550 #455
                easein 1.5 ypos 580 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'anal' not in JubesX.Spunk", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat
    # End Legs anal slow

image Jubes_Sex_Zero_Anim_A2:
    #this is the cock for Jubes's anal animation, action_speed2 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#60
                easein .5 ypos 75
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_A3:
    #Her Body in the anal pose, fast
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in
            pause 0.2
            ease .7 ypos 00 #out
            repeat

image Jubes_Sex_Legs_A3:
    # Her Legs in the anal pose, fast
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_A3", "Jubes_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 525 #in 450
                easeout 0.45 ypos 540 #455
                easein .5 ypos 580 #out
                repeat
    contains:
            # Spunk
            ConditionSwitch(
                "'anal' not in JubesX.Spunk", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat
    # End Legs Anal fast

image Jubes_Sex_Zero_Anim_A3:
    #this is the cock for Jubes's anal animation, action_speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .7 ypos 0#60
                easein .3 ypos 75
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_A4:
    #Her Body in the anal pose, cumming
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,20) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 00 #in
            pause 0.2
            ease 1.7 ypos 20 #out
            repeat

image Jubes_Sex_Legs_A4:
    # Her Legs in the anal pose, cumming
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat
    contains:
            AlphaMask("Jubes_Sex_Zero_Anim_A4", "Jubes_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 568 #in 450
                easeout 0.45 ypos 573 #455
                easein 1.5 ypos 583 #out
                repeat
    contains:
            # spunk
            ConditionSwitch(
                "'anal' not in JubesX.Spunk", Null(),
                "True", "images/JubesSex/Jubes_Sex_Spunk_Anal_O.png",
                )
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat
    # End Legs Anal cumming

image Jubes_Sex_Zero_Anim_A4:
    #this is the cock for Jubes's anal animation, action_speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat

    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_H0:
    #Her Body in the hotdogging pose, static
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jubes_Sex_Legs_H0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            "Jubes_Sex_Zero_Anim_H0"
#            AlphaMask("Jubes_Sex_Zero_Anim_H0", "Jubes_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out
                repeat
    # End Legs hotdogging static

image Jubes_Sex_Zero_Anim_H0:
    #this is the cock for Jubes's hotdogging animation, action_speed0 (static)
    contains:
        subpixel True
        ConditionSwitch(
            "Player.Sprite", "Zero_Doggy_Insert",# Zero's cock, changes color and properties
            "True", Null(),
            )

#        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        alpha 0.8
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_H1:
    #Her Body in the hotdogging pose, slow
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jubes_Sex_Legs_H1:
    # Her Legs in the hotdogging pose, slow
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                ease 1 ypos -10 #-50
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            "Jubes_Sex_Zero_Anim_H1"
#            AlphaMask("Jubes_Sex_Zero_Anim_H0", "Jubes_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                ease 1 ypos 570 #-50
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out
                repeat
    # End Legs hotdogging slow

image Jubes_Sex_Zero_Anim_H1:
    #this is the cock for Jubes's hotdogging animation, action_speed1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,250)#125,75
        block: #total 3s
                ease 1.5 ypos 90 #110
                pause .5
                ease 1.0 ypos 250
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_H2:
    #Her Body in the hotdogging pose, fast
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total .75s
            pause .3
            ease .5 ypos -5 #in
            pause 0.3
            ease .4 ypos 0 #out
            repeat

image Jubes_Sex_Legs_H2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total .75s
                pause 0.1
                ease .25 ypos -20 #-50
                easeout 0.15 ypos -18 #-50
                easein 0.25 ypos 0 #out
                repeat
    contains:
            "Jubes_Sex_Zero_Anim_H2"
#            AlphaMask("Jubes_Sex_Zero_Anim_H0", "Jubes_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.1
                ease .25 ypos 560 #-50
                easeout 0.15 ypos 562 #455
                easein 0.25 ypos 580 #out
                repeat
    # End Legs anal fast

image Jubes_Sex_Zero_Anim_H2:
    #this is the cock for Jubes's hotdogging animation, action_speed1 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,230)#125,75
        block: #total .75s
                ease .25 ypos 150 #110
                easeout 0.25 ypos 170
                easein 0.25 ypos 230
                repeat
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True

# End H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


image Jubes_AnalMask:
    transform_anchor True
    contains:
        "images/JubesSex/Jubes_Sex_MaskAnalX.png"
        pos (200,366)#(0,0)#(-300,-300) #323 -70
        anchor (.5,.5)
    zoom 1
    anchor (0.5,0.5)



# Jubes Footjob  Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jubes_Footjob_Foot:
    #her movable foot in the footjob poses
    contains:
            # hose/base
        ConditionSwitch(
            "JubesX.Hose == 'stockings and garterbelt' or JubesX.Hose == 'stockings'", "images/JubesSex/Jubes_Sex_Stockings_Foot.png",
            "JubesX.Hose == 'black stockings'", "images/JubesSex/Jubes_Sex_BlackStockings_Foot.png",
            "True", "images/JubesSex/Jubes_Sex_Foot.png"
            )
    contains:
            # legs
        ConditionSwitch(
            "JubesX.Upskirt", Null(),
            "JubesX.Legs == 'leather pants'", "images/JubesSex/Jubes_Sex_Pants_Foot.png",
            "True", Null(),
            )
    offset (1105,140) #
    zoom 1

image Jubes_Sex_Zero_Anim_F:
            #cock used in jubes's sex pose
            "Zero_Blowcock"
            zoom .7
            anchor (0.5, 0.9)
            offset (270,650)#(220,350)
            rotate 0

# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_F0:
    #Her Body in the hotdogging pose, static
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
    yoffset -100

image Jubes_Sex_Legs_F0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            #Foot
            "Jubes_Footjob_Foot"
            subpixel True
            anchor (1100,140)
            transform_anchor True
            pos (0,0) #top
            rotate 0
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-2
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-4
                easein 0.9 ypos 0 #out
                repeat
            parallel:#total 3s
                ease 2 rotate 5 #20
                ease 2 rotate -5 #0
                pause .5
                repeat
    contains:
            "Jubes_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True
            pos (558,580) #538,475
            rotate -5
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos 578 #578
                easein 0.2 ypos 575 #out 575
                easeout 0.5 ypos 576 #575
                easein 0.9 ypos 580 #out  580
                repeat
            parallel:#total 3s
                easeout 1 rotate -5 #-20
                easein 1 rotate -10 #-28
                pause .2
                easeout .8 rotate -5 #-20
                easein 1 rotate 0 #-5
                pause .5
                repeat

    yoffset -100
    # End Legs hotdogging static


# End F0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_F1:
    #Her Body in the hotdogging pose, static
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
    yoffset -100

image Jubes_Sex_Legs_F1:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
    contains:
            "Jubes_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True
            pos (558,580) #538,475
            rotate -5
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out
                repeat
            parallel:#total 3s
                easeout 1 rotate -20 #-50
                easein 1 rotate -28 #-50
                pause .2
                easeout .8 rotate -20 #-50
                easein 1 rotate -5 #-50
                pause .5
                repeat
    contains:
            #Foot
            "Jubes_Footjob_Foot"
            subpixel True
            anchor (1100,140)
            transform_anchor True
            pos (0,0) #top
            rotate 0
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat
            parallel:#total 3s
                ease 2 rotate 20 #-50
                ease 2 rotate 0 #-50
                pause .5
                repeat

    yoffset -100
    # End Legs hotdogging static

# End F1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jubes_Sex_Body_F2:
    #Her Body in the hotdogging pose, fast
    contains:
        "Jubes_Sex_Body"
        subpixel True
        pos (0,0) #top (0,-10)
        block:#total 2s
            ease .7 ypos -10 #in
            ease .7 ypos 0 #out
            repeat
    rotate 15
    yoffset -250
    xoffset 500#400
    xzoom -1

image Jubes_Sex_Legs_F2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Jubes_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3
                ease 0.5 ypos -2 #-50
                ease 1 ypos -10 #-50
                pause .1
                repeat
    contains:
            "Jubes_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True
            pos (808,380) #(558,580)
            rotate -55
            parallel:#total 3s
                easeout .25 rotate -58 #-20
                easein .25 rotate -60 #-28
                pause .1
                easeout .4 rotate -58 #-20
                easein .5 rotate -55 #-5
                pause .1#.25
                repeat
    contains:
            #Foot
            "Jubes_Footjob_Foot"
            subpixel True
            anchor (1100,140)
            transform_anchor True
            pos (0,0) #top
            rotate 0
            parallel:#total 3s
                pause 0.15
                easeout 0.2 ypos -2 #-50
                easein 0.05 ypos -5 #out
                easeout 0.25 ypos -4 #-50
                easein 0.45 ypos 0 #out
                repeat
            parallel:#total 3s
                ease .5 rotate 20 #-50  top
                ease 1 rotate 0 #-50
                pause .1#.25
                repeat

    yoffset -400
    xoffset 300#200
    rotate 50
    # End Legs hotdogging fast


# End F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

#End Footjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jubes_SexMaskX:
    transform_anchor True
    contains:
        "images/JubesSex/Jubes_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #
        anchor (.5,.5)
    zoom 1
#    transform_anchor True
    anchor (0.5,0.5)
#    rotate 30

image Jubes_Sex_Zero_AnimX:
        #this is the cock for Jubes's sex animation, action_speed 0 (static)
        contains:
            Solid("#159457", xysize=(401,606))#(1264,1061))
            alpha 0.9
        contains:
            subpixel True
#            anchor (0.5,0)
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
#            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.6
            alpha 0.5
            pos (130,100)#(390,550)#(350,250) #466
#            rotate -30
            block:
                    ease 1.25 ypos -50#630
                    ease 1.25 ypos 100#480
                    repeat

        size (401,606)#(88,266)(1264,1061)#(1119,1186)
        anchor (0.1,0.5)
        transform_anchor True
#        rotate 30


image Jubes_Mega_Mask2:
    # giant green brick for use in finding where a mask is
    contains:
        "images/JubesSex/Jubes_Sex_PussyMaskTest2.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
#        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease .25 offset(0,-500)
#                    ease .25 offset(0,1000)
#                    ease .25 offset(200,-500)
#                    ease .25 offset(200,1000)
#                    ease .25 offset(400,-500)
#                    ease .25 offset(400,1000)
#                    ease .25 offset(600,-500)
#                    ease .25 offset(600,1000)
#                    ease 1.5 offset(-800,-1000)
#                    ease 1.5 offset(-200,-100)
#                    ease .25 offset(-400,-500)
#                    ease .25 offset(-400,1000)
#                    ease .25 offset(-200,-500)
#                    ease .25 offset(-200,1000)
#                    repeat
    transform_anchor True
    zoom 1
    rotate 30
#    block:
#                    ease 1 rotate 0
#                    ease 1 rotate 30
#                    repeat

image Jubes_Mega_Mask:
    # giant green brick for use in finding where a mask is
    contains:
        "images/JubesSex/Jubes_Sex_PussyMaskTestB.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease 1.5 offset(-800,-1200)
#                    ease 1.5 offset(-200,-100)
#                    ease 1.5 offset(-600,-1200)
#                    ease 1.5 offset(-600,-600)
#                    ease 1.5 offset(-200,-1200)
#                    ease 1.5 offset(-200,-600)
#                    repeat
    transform_anchor True
    zoom 1
    rotate 30

# end Jubes's Sex Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Jubes's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jubes's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Jubes_BJ_Animation:
    #core blowjob animation
    contains:
        ConditionSwitch(
            # Jubes's upper body
#            "Player.Sprite", ConditionSwitch(
#                    # If during sex
            "action_speed == 1", "Jubes_BJ_Body_1",#Licking
            "action_speed == 2", "Jubes_BJ_Body_2",#Heading
            "action_speed == 3", "Jubes_BJ_Body_3",#Sucking
            "action_speed == 4", "Jubes_BJ_Body_4",#Deepthroat
            "action_speed == 5", "Jubes_BJ_Body_5",#Cumming high
            "action_speed == 6", "Jubes_BJ_Body_6",#Cumming deep
#                    "True",     "Jubes_BJ_Body_0",#Static
#                    ),
            "True","Jubes_BJ_Body_0",#Static
            )
    zoom 1.35
    anchor (.5,.5)
    pos (600,605)


#  BJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#image Jubes_Sprite_BJ_SuckingMask:
#    contains:
#            "images/JubesSprite/Jubes_Sprite_SuckingMask.png"
##            pos (200,50)
#    contains:
#            "images/JubesSprite/Jubes_Sprite_SpunkSuckingO.png"
#    pos (100,150)
#    alpha .8

image Jubes_Sprite_BJ_HairBack:
    #This is the version of the hair back used in the BJ pose
#    "images/JubesSprite/Jubes_Sprite_Hair_Long_Under.png"
    ConditionSwitch(
            #Hair over
            "not JubesX.Hair", Null(),
            "JubesX.Hair == 'wet' or JubesX.Water", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Under.png",
            "JubesX.Hair", "images/JubesSprite/Jubes_Sprite_Hair_Long_Under.png",
            "True", Null(),
            )

image Jubes_Sprite_BJ_Head:
    #This is the version of the head used in the BJ pose
    LiveComposite(
        (806,806),
        (0,0), ConditionSwitch(
                # Face background plate
                "JubesX.Blush == 2", "images/JubesSprite/Jubes_Sprite_Head_Blush2.png",
                "JubesX.Blush", "images/JubesSprite/Jubes_Sprite_Head_Blush.png",
                "True", "images/JubesSprite/Jubes_Sprite_Head.png",
                ),
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in JubesX.Spunk", Null(),
            "action_speed >= 2", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_Chin.png",
            ),
        (0,0), ConditionSwitch(#Mouths
            "action_speed >= 2", "images/JubesSprite/Jubes_Sprite_Mouth_SuckingBJ.png",   #sucking
            "action_speed == 1", "images/JubesSprite/Jubes_Sprite_Mouth_Tongue.png",     #licking
            "JubesX.Mouth == 'normal'", "images/JubesSprite/Jubes_Sprite_Mouth_Normal.png",
            "JubesX.Mouth == 'lipbite'", "images/JubesSprite/Jubes_Sprite_Mouth_Lipbite.png",
            "JubesX.Mouth == 'sucking'", "images/JubesSprite/Jubes_Sprite_Mouth_Sucking.png",
            "JubesX.Mouth == 'kiss'", "images/JubesSprite/Jubes_Sprite_Mouth_Kiss.png",
            "JubesX.Mouth == 'sad'", "images/JubesSprite/Jubes_Sprite_Mouth_Sad.png",
            "JubesX.Mouth == 'smile'", "images/JubesSprite/Jubes_Sprite_Mouth_Smile.png",
            "JubesX.Mouth == 'surprised'", "images/JubesSprite/Jubes_Sprite_Mouth_Surprised.png",
            "JubesX.Mouth == 'tongue'", "images/JubesSprite/Jubes_Sprite_Mouth_Tongue.png",
            "JubesX.Mouth == 'grimace'", "images/JubesSprite/Jubes_Sprite_Mouth_Smile.png",
            "JubesX.Mouth == 'smirk'", "images/JubesSprite/Jubes_Sprite_Mouth_Smirk.png",
#            "JubesX.Mouth == 'smirk'", "images/JubesSprite/Jubes_Sprite_Mouth_Normal.png",
            "True", "images/JubesSprite/Jubes_Sprite_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(#Mouth spunk
            "'mouth' not in JubesX.Spunk", Null(),
            "action_speed >= 2", "images/JubesSprite/Jubes_Sprite_Spunk_MouthSuck.png",   #sucking
            "action_speed == 1", "images/JubesSprite/Jubes_Sprite_Spunk_MouthTongue.png",     #licking
            "JubesX.Mouth == 'normal'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthNeutral.png",
            "JubesX.Mouth == 'lipbite'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthSmirk.png",
            "JubesX.Mouth == 'sucking'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthTongue.png",
            "JubesX.Mouth == 'kiss'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthKiss.png",
            "JubesX.Mouth == 'sad'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthSad.png",
            "JubesX.Mouth == 'smile'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthSmile.png",
            "JubesX.Mouth == 'surprised'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthSad.png",
            "JubesX.Mouth == 'tongue'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthTongue.png",
            "JubesX.Mouth == 'grimace'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthSmile.png",
            "JubesX.Mouth == 'smirk'", "images/JubesSprite/Jubes_Sprite_Spunk_MouthSmirk.png",
            "True", "images/JubesSprite/Jubes_Sprite_Spunk_MouthNeutral.png",
            ),
        (0,0), ConditionSwitch(#Mouth spunk over
            "action_speed >= 2 and 'mouth' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_SpunkSuckingO.png",   #sucking
            "True", Null(),
            ),
        (0,0), ConditionSwitch(#wet tongue
            "action_speed == 1", "images/JubesSprite/Jubes_Sprite_Wet_Tongue.png",     #licking
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #brows
            "JubesX.Blush >= 2", ConditionSwitch(
                    "JubesX.Brows == 'normal'", "images/JubesSprite/Jubes_Sprite_Brows_Normal_B.png",
                    "JubesX.Brows == 'angry'", "images/JubesSprite/Jubes_Sprite_Brows_Angry_B.png",
                    "JubesX.Brows == 'sad'", "images/JubesSprite/Jubes_Sprite_Brows_Sad_B.png",
                    "JubesX.Brows == 'surprised'", "images/JubesSprite/Jubes_Sprite_Brows_Surprised_B.png",
                    "JubesX.Brows == 'confused'", "images/JubesSprite/Jubes_Sprite_Brows_Confused_B.png",
                    "True", "images/JubesSprite/Jubes_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "JubesX.Brows == 'normal'", "images/JubesSprite/Jubes_Sprite_Brows_Normal.png",
                    "JubesX.Brows == 'angry'", "images/JubesSprite/Jubes_Sprite_Brows_Angry.png",
                    "JubesX.Brows == 'sad'", "images/JubesSprite/Jubes_Sprite_Brows_Sad.png",
                    "JubesX.Brows == 'surprised'", "images/JubesSprite/Jubes_Sprite_Brows_Surprised.png",
                    "JubesX.Brows == 'confused'", "images/JubesSprite/Jubes_Sprite_Brows_Confused.png",
                    "True", "images/JubesSprite/Jubes_Sprite_Brows_Normal.png",
                    ),
            ),
        (0,0), "Jubes Blink",     #Eyes
        (0,0), ConditionSwitch(
            #Hair mid
            "JubesX.Over == 'jacket'", Null(),
            "JubesX.Hair == 'wet' or JubesX.Water", Null(),
            "JubesX.Hair", "images/JubesSprite/Jubes_Sprite_Hair_Long_Mid.png",
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not JubesX.Water", Null(),
#            "True", "images/JubesSprite/Jubes_Sprite_Wet_Head.png",
#            ),
        (0,0), ConditionSwitch(
            #Hair over
            "not JubesX.Hair", Null(),
            "JubesX.Hair == 'wet' or JubesX.Water", "images/JubesSprite/Jubes_Sprite_Hair_Wet_Over.png",
            "JubesX.Hair", "images/JubesSprite/Jubes_Sprite_Hair_Long_Over.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair Water
            "not JubesX.Water", Null(),
            "True", "images/JubesSprite/Jubes_Sprite_Head_Wet.png",
#            "True", "images/JubesSprite/Jubes_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk
            "'hair' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Spunk_Facial2.png",
            "'facial' in JubesX.Spunk", "images/JubesSprite/Jubes_Sprite_Spunk_Facial1.png",
            "True", Null(),
            ),
        )
#    anchor (0.6, 0.0)
#    zoom .5

image Jubes_BlowCock_Mask:
    #This is a mask used by the blockcock during the action_speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat


#image Jubes_BlowCock_Mask_3:
#    This is a mask used by the blockcock during the action_speed 4 deep throat animation
#    it is a block moving in and out to prevent the cock sticking out the back.
#    contains:
#        Solid("#159457", xysize=(190,950))
#        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat

image Jubes_BJ_Body_0:
    #Her Body in the BJ pose, static
    contains:
            #Hair underlay
            "Jubes_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat
    contains:
            #base body
            "Jubes_Sprite"
            subpixel True
            pos (650,800)#(673,740) #top
            zoom 2.2 #.75
            anchor (0.5, 0.5)
            rotate -20
            parallel:
                pause 0.1
                ease 1.1 ypos 810 #bottom
                pause 0.2
                ease 1 ypos 800 #top
                pause 0.1
                repeat
    contains:
            #base head under cock
            subpixel True
            "Jubes_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jubes_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Jubes_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
                pause 0.1
#                easeout .1 rotate 1 #bottom .6
                ease .15 rotate -5 #bottom
                pause 0.4
                ease 1.95 rotate 10 #top
                repeat
            parallel:
                pause 0.1
#                easeout .1 pos (407,262) #bottom(637,168)
                ease .15 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.95 pos (420,292) #top 412
                repeat
    #End BJ animation action_speed 0


image Jubes_BJ_Body_1:
    #Her Body in the BJ pose, licking
    contains:
            #Hair underlay
            "Jubes_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat
    contains:
            #base body
            "Jubes_Sprite"
            pos (673,740)#(680,755) #top
            zoom 2.2 #.75
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.25 rotate -40 #bottom
                pause 0.45
                ease 1.35 rotate -20 #top
                repeat
            parallel:
                pause 0.15
                easeout .9 xpos 740 #bottom
                easein .35 xpos 740 #bottom 481
                pause 0.5
                easeout .65 xpos 710 #top
                easein .65 xpos 673 #top
                repeat
            parallel:
                pause 0.15
                ease 1.25 ypos 830 #bottom
                pause 0.45
                ease 1.35 ypos 740 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Jubes_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jubes_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Jubes_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
                pause 0.1
                easeout 1.2 rotate 1 #bottom
                easein .3 rotate -1 #bottom
                pause 0.4
                ease 1.2 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 pos (407,262) #bottom(637,168)
                easein .3 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.2 pos (412,292) #top
                repeat
    #End BJ animation action_speed 1

image Jubes_BJ_Body_2:
    #Her Body in the BJ pose, heading
    contains:
            #Hair underlay
            "Jubes_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat
    contains:
            #base body
            "Jubes_Sprite"
            pos (680,755)#(680,755) #top
            zoom 2.2 #.75
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -30 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat
            parallel:
                pause 0.15
                ease 1.35 xpos 730 #bottom 760
                pause 0.25
                ease 1.45 xpos 680 #top
                repeat
            parallel:
                pause 0.15
                ease 1.55 ypos 780 #bottom
                pause 0.15
                ease 1.35 ypos 755 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Jubes_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jubes_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Jubes_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
                pause 1.3
                ease .4 rotate 8 #bottom
                pause .2
                ease 1 rotate 10 #top
                pause .3
                repeat
            parallel:
                pause 1.3
                ease .4 pos (410,285) #bottom(407,262)
                pause .2
                ease 1 pos (412,292) #top
                pause .3
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat
    #End BJ animation action_speed 2



image Jubes_BlowCock_Mask_3:
    #This is a mask used by the blockcock during the action_speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,100)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat

image Jubes_BJ_Body_3:
    #Her Body in the BJ pose, sucking
    contains:
            #Hair underlay
            "Jubes_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat
    contains:
            #base body
            "Jubes_Sprite"
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
#                pause 0.15
                ease .7 rotate -40 #bottom
#                pause 0.15
                ease 1.0 rotate -20 #top
                repeat
            parallel:
#                pause 0.15
                easeout .3 xpos 710 #bottom
                easein .4 xpos 760 #bottom
#                pause 0.15
                easeout .55 xpos 710 #top
                easein .45 xpos 673 #top
                repeat
            parallel:
#                pause 0.15
                ease .7 ypos 780 #bottom 830
#                pause 0.15
                ease 1.0 ypos 780 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Jubes_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jubes_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Jubes_BlowCock_Mask_3")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
#                pause 0.2
                ease .7 rotate 0 #bottom
#                pause 0.1
                ease 1 rotate 10 #top
                repeat
            parallel:
#                pause 0.2
                ease .7 pos (407,262) #bottom(637,168)
#                pause 0.1
                ease 1 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat
    #End BJ animation action_speed 3


image Jubes_BlowCock_Mask_4:
    #This is a mask used by the blockcock during the action_speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
        block:
                pause 0.1
                ease 1.6 offset (0,300)# bottom
                pause 0.1
                ease 1.4 offset (0,0)# top
                repeat

image Jubes_BJ_Body_4:
    #Her Body in the BJ pose, deep throat
    contains:
            #Hair underlay
            "Jubes_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat
    contains:
            #base body
            "Jubes_Sprite"
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -40 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat
            parallel:
                pause 0.15
                easeout .65 xpos 710 #bottom
                easein .9 xpos 760 #bottom
                pause 0.15
                easeout .70 xpos 710 #top
                easein .65 xpos 673 #top
                repeat
            parallel:
                pause 0.15
                ease 1.55 ypos 830 #bottom
                pause 0.15
                ease 1.35 ypos 780 #top
                repeat
    contains:
            #base head under cock
            subpixel True
            "Jubes_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jubes_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Jubes_BlowCock_Mask_4")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4
            alpha 1
            rotate 10
            parallel:
                pause 0.1
                ease 1.6 rotate 0 #bottom
                pause 0.1
                ease 1.4 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 pos (407,262) #bottom(637,168)
                pause 0.1
                ease 1.4 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat
    #End BJ animation action_speed 4


image Jubes_BJ_Body_5:
    #Her Body in the BJ pose, high cumming
    contains:
            #Hair underlay
            "Jubes_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat
    contains:
            #base body
            "Jubes_Sprite"
            subpixel True
            zoom 2.2 #.75
            anchor (0.5, 0.5)
            rotate -30
            pos (730,760)#(680,755) #bottom
            parallel:
                pause 1
                ease .3 rotate -26 #top
                easeout .3 rotate -28 #bottom
                easein .5 rotate -30 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 710 #top 680
                easeout .3 xpos 720 #bottom
                easein .5 xpos 730 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 750 #top 755
                easeout .3 ypos 755 #bottom
                easein .5 ypos 760 #bottom
                pause .5
                repeat
    contains:
            #base head under cock
            subpixel True
            "Jubes_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jubes_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Jubes_BlowCock_Mask")
            subpixel True
            pos (410,292) #bottom
            zoom 0.4
            alpha 1
            rotate 12
            parallel:
                pause 1
                ease .3 rotate 10 #top
                ease .3 rotate 12 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (412,285) #top
                ease .3 pos (410,292) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat
    #End BJ animation action_speed 5

image Jubes_BlowCock_Mask_6:
    #This is a mask used by the blockcock during the action_speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back.
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,300)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat

image Jubes_BJ_Body_6:
    #Her Body in the BJ pose, deep throat cumming
    contains:
            #Hair underlay
            "Jubes_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat
    contains:
            #base body
            "Jubes_Sprite"
            subpixel True
            zoom 2.2 #.75
            anchor (0.5, 0.5)
            rotate -40
            pos (760,830)#(680,755) #bottom
            parallel:
                pause 1
                ease .3 rotate -38 #top
                easeout .3 rotate -39 #bottom
                easein .5 rotate -40 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 750 #top
                easeout .3 xpos 756 #bottom
                easein .5 xpos 760 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 835 #top
                easeout .3 ypos 830 #bottom
                easein .5 ypos 830 #bottom
                pause .5
                repeat
    contains:
            #base head under cock
            subpixel True
            "Jubes_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat
    contains:
            #zero's cock
#            ConditionSwitch(
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jubes_BlowCock_Mask"), #Null(),
#                )
            AlphaMask("Blowcock", "Jubes_BlowCock_Mask_6")
            subpixel True
            pos (407,262) #bottom
            zoom 0.4
            alpha 1
            rotate 0
            parallel:
                pause 1
                ease .3 rotate 2 #top
                ease .3 rotate 0 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (409,268) #top
                ease .3 pos (407,262) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jubes_Sprite_BJ_Head", "images/JubesSprite/Jubes_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat
    #End BJ animation action_speed 6
#Head and Body Animations for Jubes's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jubes_BJ_Launch(line = primary_action):
    return #fix, temporary
    # The sequence to launch the Jubes BJ animations
    $ JubesX.ArmPose = 1
    if renpy.showing("Jubes_BJ_Animation"):
        return

    call Jubes_Hide
    if line == "L" or line == "cum":
        show Jubes_Sprite at sprite_location(StageCenter) zorder JubesX.Layer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Jubes_Sprite at sprite_location(StageCenter) zorder JubesX.Layer:
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    $ action_speed = 0
    if line == "L": # Jubes gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != JubesX:
                            "[JubesX.name] looks back at [Present[0].name] to see if she's watching."
                    elif Present[1] != JubesX:
                            "[JubesX.name] looks back at [Present[1].name] to see if she's watching."
                else:
                            "[JubesX.name] casually glances around to see if anyone can see her."
            "[JubesX.name] smoothly bends down and places your cock against her cheek."

    if line != "cum":
        $ primary_action = "blowjob"

    show Jubes_Sprite zorder JubesX.Layer:
        alpha 0
    show Jubes_BJ_Animation zorder 150:
        pos (645,510)
    return

label Jubes_BJ_Reset: # The sequence to the Jubes animations from BJ to default
    if not renpy.showing("Jubes_BJ_Animation"):
        return
#    hide Jubes_BJ_Animation
    call Jubes_Hide
    $ action_speed = 0

    show Jubes_Sprite at sprite_location(StageCenter) zorder JubesX.Layer:
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Jubes_Sprite zorder JubesX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Jubes_Sprite at sprite_location(JubesX.sprite_location) zorder JubesX.Layer:
        alpha 1
        zoom 1 offset (0,0)
    return

# End Jubes Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jubes Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jubes Handjob element //////////////////////////////////////////////////////////////////////

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
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
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
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_4():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

transform Handcock_1L():
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

transform Handcock_2L():
    subpixel True
    rotate_pad False
    ypos 400
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat

image Jubes_HJ_Animation:
    contains:
        ConditionSwitch(
            # backside of the hand
            "not action_speed", Transform("Jubes_Hand_Under"),
            "action_speed == 1", At("Jubes_Hand_Under", Jubes_Hand_1()),
            "action_speed >= 2", At("Jubes_Hand_Under", Jubes_Hand_2()),
            "action_speed", Null(),
            ),
    contains:
        ConditionSwitch(
            # cock
            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1L()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2L()),
            "action_speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(
            # fingers of the hand
            "not action_speed", Transform("Jubes_Hand_Over"),
            "action_speed == 1", At("Jubes_Hand_Over", Jubes_Hand_1()),
            "action_speed >= 2", At("Jubes_Hand_Over", Jubes_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Jubes_HJ_Reset: # The sequence to the Jubes animations from handjob to default
    if not renpy.showing("Jubes_HJ_Animation"):
        return
    $ action_speed = 0
    $ JubesX.ArmPose = 1
    hide Jubes_HJ_Animation with easeoutbottom
    call Jubes_Hide
    show Jubes_Sprite at sprite_location(JubesX.sprite_location) zorder JubesX.Layer:
        alpha 1
        zoom 1.7 offset (-50,200)
    show Jubes_Sprite at sprite_location(JubesX.sprite_location) zorder JubesX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Jubes_Sprite at sprite_location(JubesX.sprite_location) zorder JubesX.Layer:
        alpha 1
        zoom 1 offset (0,0)
    return

# End Jubes Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Jubes's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jubes_TJ_Animation:
            #core TJ animation
            contains:
                ConditionSwitch(
                    # Jubes's upper body
                    "not Player.Sprite","Jubes_TJ_0",#Static
                    "action_speed == 1", "Jubes_TJ_1",#slow
                    "action_speed == 4", "Jubes_TJ_4",#cumming high
                    "action_speed == 5", "Jubes_TJ_5",#cumming low
                    "action_speed >= 2", "Jubes_TJ_2",#fast
                    "True",       "Jubes_TJ_0",#Static
                    )
            zoom .7 #0.6
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



image Jubes_TJ_HairBack:
            #Hair underlay
            "Jubes_Sprite_HairBack"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0

image Jubes_TJ_Head:
            #Hair underlay
            "Jubes_Sprite_Head"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0

image Jubes_TJ_HairMid:
            #Hair midlayer
            "Jubes_Sprite_HairMid"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            rotate 20
            offset (320,100)
            rotate 0

image Jubes_TJ_HairTop:
            #Hair overlay
            "Jubes_Sprite_HairTop"
            transform_anchor True
            zoom 2.5 #2.1
            anchor (0.5, 0.5)
            offset (320,100) # (300,275)
            rotate 0

image Jubes_TJ_ZeroCock:
            #cock used in jubes's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (220,670)#(300,750)
            rotate 0

image Jubes_TJ_Body:
            #body underlay
            contains:
                "images/JubesSex/Jubes_Titjob_Body.png"
            contains:
                ConditionSwitch(
                        "not JubesX.Neck",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Neck_[JubesX.Neck].png",
                        )
            contains:
                ConditionSwitch(
                        "'tits' not in JubesX.Spunk",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Spunk_Chest.png",
                        )
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            offset (410,770) # (300,275)
            rotate 0


image Jubes_TJ_LeftArm:
            #left arm
            contains:
                "images/JubesSex/Jubes_Titjob_LeftHand.png"
            contains:
                ConditionSwitch(
                        "not JubesX.Arms",Null(),
                        "JubesX.Arms == 'gloves'",       "images/JubesSex/Jubes_Titjob_LeftGlove.png",
                        "True",       "images/JubesSex/Jubes_Titjob_wrists.png",
                        )
            contains:
                # Left Piercings
                ConditionSwitch(
                        "not JubesX.Pierce",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Left_[JubesX.Pierce].png",
                        )

image Jubes_TJ_RightArm:
            #left arm
            contains:
                "images/JubesSex/Jubes_Titjob_RightHand.png"
            contains:
                ConditionSwitch(
                        "JubesX.Arms == 'gloves'",       "images/JubesSex/Jubes_Titjob_RightGlove.png",
                        "True", Null(),
                        )
            contains:
                # Right Piercings
                ConditionSwitch(
                        "not JubesX.Pierce",Null(),
                        "True",       "images/JubesSex/Jubes_Titjob_Right_[JubesX.Pierce].png",
                        )

image Jubes_TJ_RightArmBack:
            #left arm
            contains:
                "images/JubesSex/Jubes_Titjob_RightHandBack.png"
            contains:
                ConditionSwitch(
                        "JubesX.Arms == 'gloves'",       "images/JubesSex/Jubes_Titjob_RightGloveBack.png",
                        "True", Null(),
                        )

# Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_0:
        #Her Body in the TJ pose, static
        contains:
                #hairback
                "Jubes_TJ_HairBack"
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
                #base body test
                "Jubes_TJ_Body"
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
                #right hand backside
                "Jubes_TJ_RightArmBack" #"images/JubesSex/Jubes_Titjob_RightHandBack.png"
                subpixel True
                pos (0,-15) #top (0,-10)
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
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
                subpixel True
                pos (0,-15) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    repeat
        contains:
                #right hand
#                contains:
#                    "images/JubesSex/Jubes_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not JubesX.Pierce",Null(),
#                            "True",       "images/JubesSex/Jubes_Titjob_Right_[JubesX.Pierce].png",
#                            )
                "Jubes_TJ_RightArm"
                subpixel True
                pos (0,-15) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    pause .1
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
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
                #zero cock
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -2
                parallel:
                    ease 2 rotate -2
                    pause .1
                    ease 2 rotate 3
                    pause .1
                    repeat
        contains:
                #left tit
                contains:
                    "images/JubesSex/Jubes_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    repeat
        contains:
                #left hand
                "Jubes_TJ_LeftArm"
#                contains:
#                    "images/JubesSex/Jubes_Titjob_LeftHand.png"
#                contains:
#                    # Left Piercings
#                    ConditionSwitch(
#                            "not JubesX.Pierce",Null(),
#                            "True",       "images/JubesSex/Jubes_Titjob_Left_[JubesX.Pierce].png",
#                            )
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #mid hair
                "Jubes_TJ_HairMid"
                subpixel True
                pos (0,0) #top (0,+10)
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
                #head
                "Jubes_TJ_HairTop"
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
# End Jubes TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_1:
        #Her Body in the TJ pose, slow
        contains:
                #hairback
                "Jubes_TJ_HairBack"
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
                #base body
                "Jubes_TJ_Body"
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
                #right hand backside
                "Jubes_TJ_RightArmBack"
                subpixel True
                pos (0,150) #top (0,-10)
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
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140
                    repeat
        contains:
                #right hand
#                contains:
#                    "images/JubesSex/Jubes_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not JubesX.Pierce",Null(),
#                            "True",       "images/JubesSex/Jubes_Titjob_Right_[JubesX.Pierce].png",
#                            )
                "Jubes_TJ_RightArm"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
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
                #zero cock
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
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
                #left tit
                contains:
                    "images/JubesSex/Jubes_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140
                    repeat
        contains:
                #left hand
                "Jubes_TJ_LeftArm"
                subpixel True
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat
        contains:
                #mid hair
                "Jubes_TJ_HairMid"
                subpixel True
                pos (0,160) #top (0,150)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos -20#-20
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
                #head
                "Jubes_TJ_HairTop"
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
# End Jubes TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_2:
        #Her Body in the TJ pose, fast
        contains:
                #hairback
                "Jubes_TJ_HairBack"
                subpixel True
                pos (0,80) #top (0,-10)
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
                #base body
                "Jubes_TJ_Body"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat
        contains:
                #right hand backside
                "Jubes_TJ_RightArmBack"
                subpixel True
                pos (0,80) #top (0,-10)
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
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
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
                #right hand
#                contains:
#                    "images/JubesSex/Jubes_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not JubesX.Pierce",Null(),
#                            "True",       "images/JubesSex/Jubes_Titjob_Right_[JubesX.Pierce].png",
#                            )
                "Jubes_TJ_RightArm"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
                subpixel True
                pos (0,80) #top (0,-10)
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
                #zero cock
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
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
                #left tit
                contains:
                    "images/JubesSex/Jubes_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
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
                #left hand
                "Jubes_TJ_LeftArm"
                subpixel True
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #mid hair
                "Jubes_TJ_HairMid"
                subpixel True
                pos (0,90) #top (0,+10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos -40#-20
                    pause .2
                    ease .4 ypos 90
                    repeat
                parallel:
                    ease 1 rotate 0
                    pause .2
                    ease .4 rotate -5
                    repeat
        contains:
                #head
                "Jubes_TJ_HairTop"
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
# End Jubes TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_4:
        #Her Body in the TJ pose, cumming
        contains:
                #hairback
                "Jubes_TJ_HairBack"
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
                #base body
                "Jubes_TJ_Body"
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
                #right hand backside
                "Jubes_TJ_RightArmBack"
                subpixel True
                pos (0,0) #top (0,-10)
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
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Right.png",
                            )
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
                #right hand
#                contains:
#                    "images/JubesSex/Jubes_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not JubesX.Pierce",Null(),
#                            "True",       "images/JubesSex/Jubes_Titjob_Right_[JubesX.Pierce].png",
#                            )
                "Jubes_TJ_RightArm"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #head
                "Jubes_TJ_Head"
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
                #zero cock
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2
                parallel:
                    ease 2 ypos 0
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat
        contains:
                #left tit
                contains:
                    "images/JubesSex/Jubes_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' not in JubesX.Spunk",Null(),
                            "True",       "images/JubesSex/Jubes_Titjob_Spunk_Left.png",
                            )
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
                #left hand
                "Jubes_TJ_LeftArm"
                subpixel True
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat
        contains:
                #mid hair
                "Jubes_TJ_HairMid"
                subpixel True
                pos (0,0) #top (0,+10)
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
                #head
                "Jubes_TJ_HairTop"
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
# End Jubes TJ Pose 4 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jubes_TJ_5:
        #Her Body in the TJ pose, cumming low
        contains:
                #hairback
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
#        contains:
#                #base body
#                contains:
#                    "images/JubesSex/Jubes_Titjob_Body.png"
#                subpixel True
#                pos (-80,-200)
#                transform_anchor True
#                rotate -20
#                parallel:
#                    ease 2 ypos -220
#                    pause .1
#                    ease 2 ypos -200
#                    pause .1
#                    repeat
        contains:
                #base body
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
                #right hand backside
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
                #right tit
                contains:
                    "images/JubesSex/Jubes_Titjob_RightTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' not in JubesX.Spunk",Null(),
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
                #right hand
#                contains:
#                    "images/JubesSex/Jubes_Titjob_RightHand.png"
#                contains:
#                    # Right Piercings
#                    ConditionSwitch(
#                            "not JubesX.Pierce",Null(),
#                            "True",       "images/JubesSex/Jubes_Titjob_Right_[JubesX.Pierce].png",
#                            )
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
                #head
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
                #zero cock
                subpixel True
                "Jubes_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2
                parallel:
                    ease 2 ypos 0
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat
        contains:
                #left tit
                contains:
                    "images/JubesSex/Jubes_Titjob_LeftTit.png"
                contains:
                    ConditionSwitch(
                            "'tits' not in JubesX.Spunk",Null(),
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
                #left hand
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
                #mid hair
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
                #head
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
# End Jubes TJ Pose 5 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Jubes's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jubes_TJ_Launch(line = primary_action):    # The sequence to launch the Jubes Titfuck animations
    return #fix, temporary
    if renpy.showing("Jubes_TJ_Animation"):
        return
    call Jubes_Hide
    show Jubes_Sprite at sprite_location(JubesX.sprite_location) zorder JubesX.Layer:
        alpha 1
        ease 1 zoom 2.3 xpos 750 yoffset -100
    if line == "L": # Jubes gets started. . .
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != JubesX:
                            "[JubesX.name] looks back at [Present[0].name] to see if she's watching."
                    elif Present[1] != JubesX:
                            "[JubesX.name] looks back at [Present[1].name] to see if she's watching."
                else:
                            "[JubesX.name] casually glances around to see if anyone can see her."
            "[JubesX.name] bends over and places your cock between her breasts."

    if JubesX.Chest and JubesX.Over:
        "She throws off her [JubesX.Over] and her [JubesX.Chest]."
    elif JubesX.Over:
        "She throws off her [JubesX.Over], baring her breasts underneath."
    elif JubesX.Chest:
        "She tugs off her [JubesX.Chest] and throws it aside."
    $ JubesX.Over = 0
    $ JubesX.Chest = 0
    $ JubesX.ArmPose = 0

    call Jubes_First_Topless

    show blackscreen onlayer black with dissolve
    show Jubes_Sprite zorder JubesX.Layer:
        alpha 0
    $ action_speed = 0
    if line != "cum":
        $ primary_action = "titjob"
    show Jubes_TJ_Animation zorder 150:
        pos (700,520) #700,420)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return



label Jubes_Middle_Launch(T = primary_action,Set=1):
    call Jubes_Hide
    $ primary_action = T
    $ JubesX.Pose = "mid" if Set else JubesX.Pose
    show Jubes_Sprite at sprite_location(JubesX.sprite_location) zorder JubesX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return


# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (290,370)#(195,380)
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
        pos (190,370)#(110,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60
            repeat

image LickRightBreast_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (290,350)#(95,355)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (270,330)#(85,345)  top
            pause .5
            ease 1.5 rotate 30 pos (290,350)#(105,375) bottom
            repeat

image LickLeftBreast_Jubes:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (175,340) #(195,360)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (170,320)#(190,380)
            pause .5
            ease 1.5 rotate 30 pos (175,340)#(200,410)
            repeat

image GropeThigh_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (235,640)#(180,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (195,740) #(205,750) bottom
            ease 1 rotate 100 pos (235,640)   #215
            repeat

image GropePussy_Jubes:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (260,580)#(120,620) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 ypos 565 #(200,585)
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
        pos (275,650)#(140,700)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (285,625)#(150,665)
                pause .5
                ease 1 rotate 50 pos (275,650)  #(140,700)
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
        pos (285,610)#(155,650)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (275,590) #(210,605)
            linear .5 rotate -60 pos (265,600) #(200,615)
            easein 1 rotate 10 pos (285,610) #(230,625)
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
        pos (285,340) #(270,400)
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
        pos (285,600) #(240,665)
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
#        block:
#            ease 1 rotate 0 xpos 260 ypos 655
#            pause .25
#            ease 1 rotate 10 xpos 270 ypos 665
#            pause .25
#            repeat
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



#Lesbian action animations.
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
        pos (290,340) #(220,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block:
            ease 1 rotate 10 ypos 350#(280,390)
            ease 1 rotate -10 ypos 340
            repeat

image GirlGropeRightBreast_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (190,340) #(90,370)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -40 ypos 350#(90,410)
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
#        yzoom -1
        pos (180,525)

image GirlGropePussy_Jubes:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (265,575) #(130,595
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 570
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 570#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 570 #(205,590)
                ease .75 rotate 200 ypos 575 #(205,595)
                ease .5 rotate 205 ypos 570
                ease .75 rotate 200 ypos 575
            choice: #Fast stroke
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
        pos (265,570)#(220,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 ypos 575
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 ypos 575
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 575
                ease .75 rotate 200 ypos 580
                ease .5 rotate 205 ypos 575
                ease .75 rotate 200 ypos 580
            choice: #Fast stroke
                ease .3 rotate 205 ypos 575
                ease .3 rotate 200 ypos 585
                ease .3 rotate 205 ypos 575
                ease .3 rotate 200 ypos 585
            repeat


#Start of fireworks animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
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
        #Jubilee's firework
        contains:
            alpha 1
            anchor (0.5,0.5)
            transform_anchor True
#            pos (0.5,0.5)
            offset (0,0)
            pause .2
            choice:
                "Star1"
            choice:
                "Star2"
            choice:
                "Star3"
            parallel:
                #hides image over last .3 seconds
                pause 0.7
                ease 0.3 alpha 0
            parallel:
                offset (0,0)
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (50,-100)
                        ease .5 offset (100,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (-25,-120)
                        ease .5 offset (-50,130)
                    parallel:
                        #grows it
                        zoom 0.2
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (25,-130)
                        ease .5 offset (50,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (10,-150)
                        ease .5 offset (20,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (100,-100)
                        ease .5 offset (150,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
        #End Star 1
        contains:
            alpha 1
            anchor (0.5,0.5)
#            pos (0.5,0.5)
            transform_anchor True
            pause .1
            choice:
                "Star1"
            choice:
                "Star2"
            choice:
                "Star3"
            parallel:
                #hides image over last .3 seconds
                pause 0.7
                ease 0.3 alpha 0
            parallel:
                offset (0,0)
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (50,-100)
                        ease .5 offset (100,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (-25,-120)
                        ease .5 offset (-50,130)
                    parallel:
                        #grows it
                        zoom 0.2
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (25,-130)
                        ease .5 offset (50,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (10,-150)
                        ease .5 offset (20,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (100,-100)
                        ease .5 offset (150,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
        #End Star 2
        contains:
            alpha 1
            anchor (0.5,0.5)
#            pos (0.5,0.5)
            transform_anchor True
            choice:
                "Star1"
            choice:
                "Star2"
            choice:
                "Star3"
            parallel:
                #hides image over last .3 seconds
                pause 0.7
                ease 0.3 alpha 0
            parallel:
                offset (0,0)
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (50,-100)
                        ease .5 offset (100,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (-25,-120)
                        ease .5 offset (-50,130)
                    parallel:
                        #grows it
                        zoom 0.2
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (25,-130)
                        ease .5 offset (50,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (10,-150)
                        ease .5 offset (20,140)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom .9
                choice:
                    parallel:
                        #arcs it
                        ease .5 offset (100,-100)
                        ease .5 offset (150,150)
                    parallel:
                        #grows it
                        zoom 0.3
                        ease 1 zoom 1.2
        #End Star 3
#end of fireworks animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
