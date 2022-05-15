# Basic Kitty Sprites

image Kitty_Sprite:
    LiveComposite(
        (480,960),
        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_HairBack",
            ),
        (0,0), ConditionSwitch(
            #back of dress
            "KittyX.Legs == 'dress' and KittyX.Upskirt", "images/KittySprite/Kitty_Sprite_Legs_Dress_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms1
            "KittyX.ArmPose == 1", "images/KittySprite/Kitty_Sprite_Arms1.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #back of the shirt
            "KittyX.Over == 'pink top' and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Under_Pink2.png",       #2
            "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Under_Pink1.png",                  #1
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #body
            "KittyX.ArmPose != 1 and KittyX.Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair2.png",
            "KittyX.ArmPose != 1", "images/KittySprite/Kitty_Sprite_Body_Bare2.png",
            "KittyX.Pubes", "images/KittySprite/Kitty_Sprite_Body_Hair1.png",
            "True", "images/KittySprite/Kitty_Sprite_Body_Bare1.png",
            ),

#        (0,0), ConditionSwitch(
#            #wet look
#            "KittyX.Water and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Water2.png",
#            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Water1.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #piercings bottom
            "not KittyX.Pierce or (KittyX.Panties and not KittyX.PantiesDown)", Null(),
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingB.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallB.png",
            ),

#        (0,0), ConditionSwitch(
#            #panties
#            "not KittyX.Panties or KittyX.PantiesDown", Null(),
#            "KittyX.Legs or KittyX.Upskirt", Null(), #If panties are down, and pants are either off or down, skip this

#            "not KittyX.Panties or not KittyX.PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this

#            "KittyX.Wet and KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
#            "KittyX.Wet and KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",
#            "KittyX.Wet and KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png",
#            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
#            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
#            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png",
#            "True", Null(),
#            ),
#        (0,0), ConditionSwitch(
#            #panties down
#            "not KittyX.Panties or not KittyX.PantiesDown", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If panties are not down or if  pants are on and up, skip this
#            "KittyX.Wet and KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
#            "KittyX.Wet and KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
#            "KittyX.Wet and KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png",
#            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
#            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
#            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #under hose layer
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittySprite/Kitty_Sprite_Hose_StockingGarter.png",
            "KittyX.Hose == 'garterbelt'", "images/KittySprite/Kitty_Sprite_Hose_Garter.png",
            "KittyX.Hose == 'stockings'", "images/KittySprite/Kitty_Sprite_Hose_Stockings.png",
            "KittyX.Hose == 'knee stockings'", "images/KittySprite/Kitty_Sprite_Hose_Knee.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #panties layer
            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", ConditionSwitch(
                    # if the panties aren't down. . .
                    # and she's not wearing pants that are up
                    "KittyX.Wet", ConditionSwitch(
                            # if they're up and wet. . .
                            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Wet.png",
                            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Wet.png",
                            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Wet.png",
                            "True", Null(),
                            ),
                    "True", ConditionSwitch(
                            #if they're just up. . .
                            "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green.png",
                            "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace.png",
                            "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini.png",
                            "True", Null(),
                            ),
                    ),
            "KittyX.Wet", ConditionSwitch(
                    #if wet and down. . .
#                    "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If nor wearing a skirt, they would be invisible
                    "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down_Wet.png",
                    "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down_Wet.png",
                    "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_DownW.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if not wet, but down
#                    "KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", Null(), #If nor wearing a skirt, they would be invisible
                    "KittyX.Panties == 'green panties'", "images/KittySprite/Kitty_Sprite_Panties_Green_Down.png",
                    "KittyX.Panties == 'lace panties'", "images/KittySprite/Kitty_Sprite_Panties_Lace_Down.png",
                    "KittyX.Panties == 'bikini bottoms'", "images/KittySprite/Kitty_Sprite_Panties_Bikini_Down.png",
                    "True", Null(),
                    ),
            ),


        (0,0), ConditionSwitch(
            #over hose layer
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", "images/KittySprite/Kitty_Sprite_Hose_Pantyhose.png",
            "KittyX.Hose == 'ripped pantyhose'", "images/KittySprite/Kitty_Sprite_Hose_RippedPantyhose.png",
            "True", Null(),
            ),
        (225,560), ConditionSwitch(
            #Personal Wetness
            "not KittyX.Wet", Null(),
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "KittyX.Panties and not KittyX.PantiesDown and KittyX.Wet <= 1", Null(),
            "KittyX.Wet == 1", ConditionSwitch( #Wet = 1
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "KittyX.Legs", AlphaMask("Wet_Drip","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            "True", ConditionSwitch( #Wet = 2+
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",#
                    "KittyX.Legs", AlphaMask("Wet_Drip2","Kitty_Drip_MaskP"),
                    "KittyX.Panties", AlphaMask("Wet_Drip","Kitty_Drip_Mask"), #"Wet_Drip2",#
                    "True", AlphaMask("Wet_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #wetness
            "KittyX.Legs or not KittyX.Wet", Null(),
            "KittyX.Panties and not KittyX.PantiesDown and KittyX.Wet < 2", Null(),
            "KittyX.Panties and not KittyX.PantiesDown", "images/KittySprite/Kitty_Sprite_Wet1.png",
            "KittyX.Wet == 2", "images/KittySprite/Kitty_Sprite_Wet2.png",
            "True", "images/KittySprite/Kitty_Sprite_Wet1.png",
            ),
        (225,560), ConditionSwitch(
            #Spunk nethers
            "'in' not in KittyX.Spunk and 'anal' not in KittyX.Spunk", Null(),
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "True", ConditionSwitch( #Wet = 2+
                    "KittyX.Panties and KittyX.PantiesDown", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"), #"Wet_Drip2",#
                    "KittyX.Legs", AlphaMask("Spunk_Drip2","Kitty_Drip_MaskP"),
                    "True", AlphaMask("Spunk_Drip2","Kitty_Drip_Mask"), #only plays if nothing is in the way
                    ),
            ),
        (0,0), ConditionSwitch(
            #pants
            "KittyX.Legs == 'blue skirt' and KittyX.Upskirt", "images/KittySprite/Kitty_Sprite_Skirt_Up.png",
            "KittyX.Legs == 'blue skirt'", "images/KittySprite/Kitty_Sprite_Skirt.png",
            "KittyX.Legs == 'dress' and KittyX.Upskirt", "images/KittySprite/Kitty_Sprite_Legs_Dress_Up.png",
            "KittyX.Legs == 'dress'", "images/KittySprite/Kitty_Sprite_Legs_Dress.png",
            "not KittyX.Legs or KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris'", "images/KittySprite/Kitty_Sprite_Pants_Blue.png",
            "KittyX.Legs == 'black jeans'", "images/KittySprite/Kitty_Sprite_Pants_Black.png",
            "KittyX.Wet and KittyX.Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga_Wet.png",
            "KittyX.Legs == 'yoga pants'", "images/KittySprite/Kitty_Sprite_Pants_Yoga.png",
            "KittyX.Wet and KittyX.Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts_Wet.png",
            "KittyX.Legs == 'shorts'", "images/KittySprite/Kitty_Sprite_Shorts.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Arms2
            "KittyX.ArmPose != 1", "images/KittySprite/Kitty_Sprite_Arms2.png",
            "True", Null(),
            ),

        (0,0), "images/KittySprite/Kitty_Sprite_Chest_Bare.png",
        (0,0), ConditionSwitch(
            #piercings top
            "not KittyX.Pierce", Null(),
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingT.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallT.png",
            ),
#        (0,0), ConditionSwitch(
#            #Bra
#            "not KittyX.Chest", Null(),
#            "KittyX.ArmPose and KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
#            "KittyX.ArmPose and KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
#            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
#            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
#            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
#            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
#            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
#            "KittyX.Chest == 0 and KittyX.Over == 'pink top'", Null(),   #use for when bra and top clash
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittySprite/Kitty_Sprite_Necklace1.png",
            "KittyX.Neck == 'star necklace'", "images/KittySprite/Kitty_Sprite_Necklace2.png",
            "KittyX.Neck == 'flower necklace'", "images/KittySprite/Kitty_Sprite_Necklace3.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #bra layer
            "not KittyX.Chest", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.ArmPose != 1 and KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2.png",
                    "KittyX.ArmPose != 1 and KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2.png",
                    "KittyX.ArmPose != 1 and KittyX.Chest == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress2.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport.png",
                    "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic.png",
                    "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1.png",
                    "KittyX.Chest == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress1.png",
                    "True", Null(),
                    ),
            "KittyX.Over and KittyX.Over != 'towel'", ConditionSwitch(
                    # If she's wearing a shirt over the bra
#                    "KittyX.ArmPose and KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",
#                    "KittyX.ArmPose and KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_UpS.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_UpS.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_UpS.png",
                    "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                    "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_UpS.png",
                    "KittyX.Chest == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress_UpS.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.ArmPose != 1", ConditionSwitch(
                            # if Arms 2
                            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini2_Up.png",
                            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace2_Up.png",
                            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport2_Up.png",
                            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic2_Up.png",
                            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami2_Up.png",
                            "KittyX.Chest == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress_Up.png",
                            "True", Null(),
                            ),
                    "True", ConditionSwitch(
                            # if Arms 1
                            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini1_Up.png",
                            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace1_Up.png",
                            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport1_Up.png",
                            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic1_Up.png",
                            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami1_Up.png",
                            "KittyX.Chest == 'dress'", "images/KittySprite/Kitty_Sprite_Bra_Dress_Up.png",
                            "True", Null(),
                            ),
                    "True", Null(),
                    ),
            ),

        (0,0), ConditionSwitch(
            #piercings over clothes
            "not KittyX.Pierce or not KittyX.Chest or KittyX.Uptop", Null(),
            "KittyX.Pierce == 'ring' and KittyX.Legs", "images/KittySprite/Kitty_Sprite_Piercing_RingOverTop.png",
            "KittyX.Pierce == 'ring'", "images/KittySprite/Kitty_Sprite_Piercing_RingOver.png",
            "KittyX.Legs", "images/KittySprite/Kitty_Sprite_Piercing_BallOverTop.png",
            "True", "images/KittySprite/Kitty_Sprite_Piercing_BallOver.png",
            ),
        (0,0), ConditionSwitch(
            #wet look
            "KittyX.Water and KittyX.ArmPose", "images/KittySprite/Kitty_Sprite_Water2.png",
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Water1.png",
            "True", Null(),
            ),

#        (0,0), ConditionSwitch(
#            #shirt
#            "not KittyX.Over", Null(),
#            "KittyX.ArmPose and KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
#            "KittyX.ArmPose and KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
#            "KittyX.ArmPose and KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
#            "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
#            "KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
#            "KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
#            "True", Null(),
#            ),

        (0,0), ConditionSwitch(
            #shirt layer
            "not KittyX.Over", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.ArmPose != 1 and KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2.png",
                    "KittyX.ArmPose != 1 and KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2.png",
                    "KittyX.ArmPose != 1 and KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "KittyX.ArmPose != 1 and KittyX.Over == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket2.png",
                    "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1.png",
                    "KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1.png",
                    "KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel1.png",
                    "KittyX.Over == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket1.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.ArmPose != 1 and KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink2_Up.png",
                    "KittyX.ArmPose != 1 and KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew2_Up.png",
                    "KittyX.ArmPose != 1 and KittyX.Over == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket2_Up.png",
#                    "KittyX.ArmPose != 1 and KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sprite_Over_Towel2.png",
                    "KittyX.Over == 'pink top'", "images/KittySprite/Kitty_Sprite_Over_Pink1_Up.png",
                    "KittyX.Over == 'red shirt'", "images/KittySprite/Kitty_Sprite_Over_Crew1_Up.png",
#                    "KittyX.Over == 'towel'", "images/KittySprite/Kitty_Sex_Over_Towel.png",
                    "KittyX.Over == 'jacket'", "images/KittySprite/Kitty_Sprite_Over_Jacket1_Up.png",
                    "True", Null(),
                    ),
            ),

        (0,0), ConditionSwitch(
            #bra over shirt layer
            "not KittyX.Over or not KittyX.Chest or not KittyX.Uptop", Null(),
            "KittyX.Chest == 'cami'", "images/KittySprite/Kitty_Sprite_Cami_Over.png",
            "KittyX.Chest == 'lace bra'", "images/KittySprite/Kitty_Sprite_Bra_Lace_Over.png",
            "KittyX.Chest == 'sports bra'", "images/KittySprite/Kitty_Sprite_Bra_Sport_Over.png",
            "KittyX.Chest == 'bra'", "images/KittySprite/Kitty_Sprite_Bra_Basic_Over.png",
            "KittyX.Chest == 'bikini top'", "images/KittySprite/Kitty_Sprite_Bikini_Over.png",
            "True", Null(),
            ),

        (124,0), ConditionSwitch(
            "renpy.showing('Kitty_BJ_Animation')", Null(),
            "True", "Kitty_Head",
            ),

        (0,0), ConditionSwitch(
            #anal spunk
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "KittyX.Panties and not KittyX.PantiesDown", Null(),
            "'anal' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Anal.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pussy spunk
            "KittyX.Legs and not KittyX.Upskirt", Null(),
            "KittyX.Panties and not KittyX.PantiesDown", Null(),
            "'in' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Pussy.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #belly spunk
            "'belly' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Belly.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #tits spunk
            "'tits' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Tits.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #UI tool for When Kitty is masturbating using girl_offhand_action actions
            "primary_action == 'lesbian' or not girl_offhand_action or focused_Girl != KittyX", Null(),
            "girl_offhand_action == 'fondle pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "girl_offhand_action == 'fondle pussy'", "GirlGropePussy_Kitty",
            "girl_offhand_action == 'fondle breasts' and (offhand_action == 'fondle breasts' or offhand_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "girl_offhand_action == 'fondle breasts' and (primary_action == 'fondle breasts' or primary_action == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right
            "girl_offhand_action == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
            "girl_offhand_action == 'vibrator breasts'", "VibratorRightBreast_Kitty",
            "girl_offhand_action == 'vibrator pussy'", "VibratorPussy_Kitty",
            "girl_offhand_action == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "girl_offhand_action == 'vibrator anal'", "VibratorAnal_Kitty",
            "girl_offhand_action == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Partner_offhand_action(Threesome masutrbation) actions
            "not Partner_offhand_action or Partner_primary_action != 'masturbation' or focused_Girl == KittyX", Null(),
            #this doesn't activate unless Kitty is not primary, and actively masturbating
            "Partner_offhand_action == 'fondle pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "Partner_offhand_action == 'fondle pussy'", "GirlGropePussy_Kitty",
            "Partner_offhand_action == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
            "Partner_offhand_action == 'vibrator breasts'", "VibratorRightBreast",
            "Partner_offhand_action == 'vibrator pussy'", "VibratorPussy",
            "Partner_offhand_action == 'vibrator pussy insert'", "VibratorPussy",
            "Partner_offhand_action == 'vibrator anal'", "VibratorAnal",
            "Partner_offhand_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for primary_action1(primary) actions
            "not primary_action or focused_Girl != KittyX", Null(),
            "primary_action == 'vibrator breasts'", "VibratorLeftBreast_Kitty",
            "primary_action == 'fondle thighs'", "GropeThigh_Kitty",
            "primary_action == 'fondle breasts'", "GropeLeftBreast_Kitty",
            "primary_action == 'suck breasts'", "LickRightBreast_Kitty",
            "primary_action == 'fondle pussy' and action_speed == 2", "FingerPussy_Kitty",
            "primary_action == 'fondle pussy'", "GropePussy_Kitty",
            "primary_action == 'lick pussy'", "Lickpussy_Kitty",
            "primary_action == 'vibrator pussy'", "VibratorPussy_Kitty",
            "primary_action == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "primary_action == 'vibrator anal'", "VibratorAnal_Kitty",
            "primary_action == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for offhand_action(secondary) actions
            "not offhand_action or focused_Girl != KittyX", Null(),
            "not offhand_action and not Partner_primary_action and primary_action == 'fondle breasts'", "GropeRightBreast_Kitty",
            #When doing nothing offhand, use both hands on breasts.
            "offhand_action == 'fondle breasts' and primary_action == 'suck breasts'", "GropeLeftBreast_Kitty",
            #When sucking right breast, fondle left
            "offhand_action == 'fondle breasts'", "GropeRightBreast_Kitty",
            "offhand_action == 'vibrator breasts' and primary_action == 'suck breasts'", "VibratorLeftBreast_Kitty",
            #When sucking right breast, vibrator left
            "offhand_action == primary_action", Null(),
            #When both triggers are the same, do nothing
            "offhand_action == 'suck breasts'", "LickLeftBreast_Kitty",
            "offhand_action == 'fondle pussy'", "GropePussy_Kitty",
            "offhand_action == 'lick pussy'", "Lickpussy_Kitty",
            "offhand_action == 'vibrator breasts'", "VibratorRightBreast_Kitty",
            "offhand_action == 'vibrator pussy'", "VibratorPussy_Kitty",
            "offhand_action == 'vibrator pussy insert'", "VibratorPussy_Kitty",
            "offhand_action == 'vibrator anal'", "VibratorAnal_Kitty",
            "offhand_action == 'vibrator anal insert'", "VibratorPussy_Kitty",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for Partner_primary_action(Threesome) actions (ie Rogue's hand on her)
            "not Partner_primary_action or focused_Girl != KittyX", Null(),
            "Partner_primary_action == 'fondle pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "Partner_primary_action == 'fondle pussy'", "GirlGropePussy_Kitty",
            "Partner_primary_action == 'lick pussy'", "Lickpussy_Kitty",
            "Partner_primary_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Kitty",
            "Partner_primary_action == 'suck breasts'", "LickRightBreast_Kitty",
            "Partner_primary_action == 'fondle breasts' and (primary_action == 'fondle breasts' or primary_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "Partner_primary_action == 'fondle breasts' and (offhand_action == 'fondle breasts' or offhand_action == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right
            "Partner_primary_action == 'fondle breasts' and (girl_offhand_action == 'fondle breasts' or girl_offhand_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty", #When zero is working the left breast, fondle right
            "Partner_primary_action == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
            "Partner_primary_action == 'vibrator breasts'", "VibratorRightBreast",
            "Partner_primary_action == 'vibrator pussy'", "VibratorPussy",
            "Partner_primary_action == 'vibrator pussy insert'", "VibratorPussy",
            "Partner_primary_action == 'vibrator anal'", "VibratorAnal",
            "Partner_primary_action == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #UI tool for girl_offhand_action(lesbian) actions (ie Rogue's hand on her when Kitty is secondary)
            "primary_action != 'lesbian' or not girl_offhand_action or focused_Girl == KittyX", Null(),
            "girl_offhand_action == 'fondle pussy' and primary_action != 'sex' and KittyX.lust >= 70", "GirlFingerPussy_Kitty",
            "girl_offhand_action == 'fondle pussy'", "GirlGropePussy_Kitty",
            "girl_offhand_action == 'lick pussy'", "Lickpussy_Kitty",
            "girl_offhand_action == 'suck breasts' and (offhand_action != 'suck breasts' or primary_action == 'suck breasts')", "LickLeftBreast_Kitty",
            "girl_offhand_action == 'suck breasts'", "LickRightBreast_Kitty",
            "girl_offhand_action == 'fondle breasts' and (primary_action == 'fondle breasts' or primary_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty",    #When zero is working the right breast, fondle left
            "girl_offhand_action == 'fondle breasts' and (offhand_action == 'fondle breasts' or offhand_action == 'suck breasts')", "GirlGropeRightBreast_Kitty", #When zero is working the left breast, fondle right
            "girl_offhand_action == 'fondle breasts' and (girl_offhand_action == 'fondle breasts' or girl_offhand_action == 'suck breasts')", "GirlGropeLeftBreast_Kitty", #When zero is working the left breast, fondle right
            "girl_offhand_action == 'fondle breasts'", "GirlGropeRightBreast_Kitty",
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
    pos (500,100) #fix remove diagnostic


image Kitty_Head:
    LiveComposite(
        (416,610),
#        (0,0), ConditionSwitch(
#            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
#            "KittyX.Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            "KittyX.Water and KittyX.Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush1.png",
            "KittyX.Water and KittyX.Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Wet_Blush2.png",
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Head_Wet_Base.png",
            "KittyX.Blush == 1", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush1.png",
            "KittyX.Blush == 2", "images/KittySprite/Kitty_Sprite_Head_Evo_Blush2.png",
            "True", "images/KittySprite/Kitty_Sprite_Head_Evo_Base.png",
            ),
        (0,0), ConditionSwitch(
            "KittyX.Brows == 'normal'", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittySprite/Kitty_Sprite_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittySprite/Kitty_Sprite_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittySprite/Kitty_Sprite_Brows_Surprised.png",
            "KittyX.Brows == 'confused'", "images/KittySprite/Kitty_Sprite_Brows_Confused.png",
            "True", "images/KittySprite/Kitty_Sprite_Brows_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "KittyX.Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Mouth_Lipbite.png",
            "KittyX.Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Mouth_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Mouth_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Mouth_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Mouth_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Mouth_Tongue.png", #fix add
            "True", "images/KittySprite/Kitty_Sprite_Mouth_Normal.png",
            ),
        (0,0), ConditionSwitch(
            "'mouth' not in KittyX.Spunk", Null(),
            "KittyX.Mouth == 'normal'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittySprite/Kitty_Sprite_Spunk_Normal.png",
            "KittyX.Mouth == 'kiss'", "images/KittySprite/Kitty_Sprite_Spunk_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittySprite/Kitty_Sprite_Spunk_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittySprite/Kitty_Sprite_Spunk_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittySprite/Kitty_Sprite_Spunk_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittySprite/Kitty_Sprite_Spunk_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittySprite/Kitty_Sprite_Spunk_Sucking.png", #fix add
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "'facial' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), "Kitty Blink",
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "KittyX.Hair == 'evo'", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            "KittyX.Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long.png",
            "KittyX.Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet.png",
            "True", "images/KittySprite/Kitty_Sprite_Hair_Evo.png",
            ),
        (0,0), ConditionSwitch(
            "KittyX.Water", "images/KittySprite/Kitty_Sprite_Wet_Head.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "KittyX.Hair == 'evo' and 'hair' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "KittyX.Hair == 'long' and 'hair' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
#            "KittyX.Hair == 'evo' and 'hair' in KittyX.Spunk", "images/KittySprite/Kitty_Sprite_Spunk_Evohair.png",
            "True", Null(),
            ),
        )
#    anchor (0.6, 0.0)
    zoom .5

image Kitty_HairBack:
    LiveComposite(
        (416,610),
        (0,0), ConditionSwitch(
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittySprite/Kitty_Sprite_Hair_Wet_Back.png",
            "KittyX.Hair == 'long'", "images/KittySprite/Kitty_Sprite_Hair_Long_Back.png",
            "True", Null(),
            ),
        )
#    anchor (0.6, 0.0)
    zoom .5

image Kitty Blink:
    ConditionSwitch(
    "KittyX.Eyes == 'sexy'", "images/KittySprite/Kitty_Sprite_Eyes_Sexy.png",
    "KittyX.Eyes == 'side'", "images/KittySprite/Kitty_Sprite_Eyes_Side.png",
    "KittyX.Eyes == 'surprised'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",
    "KittyX.Eyes == 'manic'", "images/KittySprite/Kitty_Sprite_Eyes_Surprised.png",
    "KittyX.Eyes == 'normal'", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",
    "KittyX.Eyes == 'down'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",
    "KittyX.Eyes == 'stunned'", "images/KittySprite/Kitty_Sprite_Eyes_Down.png",
    "KittyX.Eyes == 'squint'", "Kitty_Squint",
    "KittyX.Eyes == 'leftside'", "images/KittySprite/Kitty_Sprite_Eyes_SideLeft.png",
    "KittyX.Eyes == 'closed'", "images/KittySprite/Kitty_Sprite_Eyes_Closed.png",
    "True", "images/KittySprite/Kitty_Sprite_Eyes_Normal.png",
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    # This randomizes the time between blinking.
    "images/KittySprite/Kitty_Sprite_Eyes_Closed.png"
    .25
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
    .25
    repeat


image Kitty_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/KittySprite/Kitty_Sprite_WetMask.png"
        offset (-225,-560)

image Kitty_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/KittySprite/Kitty_Sprite_WetMaskP.png"
        offset (-225,-560)

# End Kitty Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /













# Kitty Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


image Kitty_SexSprite:
    LiveComposite(                                                                                 #Base body
        (1120,840),
        (0,0), ConditionSwitch(
                #Shows different upper body motion depending on events
                "not Player.Sprite", "Kitty_Sex_Body_Static",
                "Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "action_speed >= 3", "Kitty_Sex_Body_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Body_Anim2",
                        "action_speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "action_speed >= 3", "Kitty_Sex_Body_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Body_Anim2",
                        "action_speed", "Kitty_Sex_Body_Anim1",
                        "True", "Kitty_Sex_Body_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "action_speed >= 2", "Kitty_Sex_Body_FootAnim2",
                        "action_speed", "Kitty_Sex_Body_FootAnim1",
                        "True", "Kitty_Sex_Body_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and action_speed >= 2","Kitty_Hotdog_Body_Anim2",
                "True", "Kitty_Sex_Body_Static",
                ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
                "not Player.Sprite", "Kitty_Sex_Legs_Static",
                "Player.Cock == 'anal'", ConditionSwitch(
                        #if the top's down. . .
                        "action_speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "action_speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",
                        ),
                "Player.Cock == 'in'", ConditionSwitch(
                        #if the top's down. . .
                        "action_speed >= 3", "Kitty_Sex_Legs_Anim3",
                        "action_speed >= 2", "Kitty_Sex_Legs_Anim2",
                        "action_speed", "Kitty_Sex_Legs_Anim1",
                        "True", "Kitty_Sex_Legs_Static",
                        ),
                "Player.Cock == 'foot'", ConditionSwitch(
                        #if the top's down. . .
                        "action_speed >= 2", "Kitty_Sex_Legs_FootAnim2",
                        "action_speed", "Kitty_Sex_Legs_FootAnim1",
                        "True", "Kitty_Sex_Legs_FootAnimStatic",
                        ),
                "Player.Cock == 'out' and action_speed >= 2","Kitty_Hotdog_Legs_Anim2",
                "True", "Kitty_Sex_Legs_Static",
                ),
        )
    align (0.6,0.0)
    pos (650,230)#(750,230)
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
        #the torso/head used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (260,-350), "Kitty_HairBack_Sex",
            #Hair underlayer
        (0,0), ConditionSwitch(
            #Body Base
            "KittyX.Pierce == 'barbell'", "images/KittySex/Kitty_Sex_Body_Barbell.png",
            "KittyX.Pierce == 'ring'", "images/KittySex/Kitty_Sex_Body_Ring.png",
            "True", "images/KittySex/Kitty_Sex_Body.png",
            ),
        (260,-350), "Kitty_Head_Sex",  #check positioning (400,-300)
        #Eyes
        (0,0), ConditionSwitch(
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittySex/Kitty_Sex_Neck_Gold.png",
            "KittyX.Neck == 'star necklace'", "images/KittySex/Kitty_Sex_Neck_Star.png",
            "KittyX.Neck == 'flower necklace'", "images/KittySex/Kitty_Sex_Neck_Flower.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #dress base
            "KittyX.Legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Waist.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #bra layer
            "not KittyX.Chest", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.Chest == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress.png",
                    "KittyX.Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra.png",
                    "KittyX.Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra.png",
                    "True", Null(),
                    ),
            "KittyX.Over", ConditionSwitch(
                    # If she's wearing a shirt over the bra
                    "KittyX.Chest == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress_UpS.png",
                    "KittyX.Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_UpS.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.Chest == 'sports bra' and KittyX.Over == 'red shirt'", "images/KittySex/Kitty_Sex_Under_SportsBra_UpS.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.Chest == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress_Up.png",
                    "KittyX.Chest == 'cami'", "images/KittySex/Kitty_Sex_Under_Cami_Up.png",
                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Under_SportsBra_Up.png",
                    "KittyX.Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
                    "KittyX.Chest == 'bikini top'", "images/KittySex/Kitty_Sex_Under_Bikini_Up.png",
                    "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_Up.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Body.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #shirt layer
            "not KittyX.Over", Null(),
            "not KittyX.Uptop", ConditionSwitch(
                    #if the top's down. . .
                    "KittyX.Over == 'jacket'", "images/KittySex/Kitty_Sex_Over_Jacket.png",
                    "KittyX.Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt.png",
                    "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt.png",
                    "KittyX.Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",
                    "True", Null(),
                    ),
            "True", ConditionSwitch(
                    # if she's not wearing a shirt
                    "KittyX.Over == 'jacket'", "images/KittySex/Kitty_Sex_Over_Jacket_Up.png",
                    "KittyX.Over == 'pink top' and KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Over_PinkShirt_UpS.png",
                    "KittyX.Over == 'pink top'", "images/KittySex/Kitty_Sex_Over_PinkShirt_Up.png",
                    "KittyX.Over == 'red shirt'", "images/KittySex/Kitty_Sex_Over_RedShirt_Up.png",
#                    "KittyX.Over == 'towel'", "images/KittySex/Kitty_Sex_Over_Towel.png",
                    "True", Null(),
                    ),
            ),
        (0,0), ConditionSwitch(
            #bra layer over the shirt
            "not KittyX.Chest or not KittyX.Over or not KittyX.Uptop", Null(),
            # if she's not wearing a shirt
            "KittyX.Chest == 'dress'", "images/KittySex/Kitty_Sex_Under_Dress_Up.png",
            "KittyX.Chest == 'bra'", "images/KittySex/Kitty_Sex_Under_Bra_Up.png",
            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Under_LaceBra_UpS.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'belly' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Body.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(
            #Outside Spunk
            "'tits' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Tits.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast licking animation
            "primary_action == 'suck breasts' or offhand_action == 'suck breasts'", "Kitty_Sex_Lick_Breasts",
            "True", Null()
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "primary_action == 'fondle breasts' or offhand_action == 'fondle breasts'", "Kitty_Sex_Fondle_Breasts",
            "True", Null()
            ),
        )

image Kitty_Sex_Lick_Breasts:
        "Lick_Anim"
        zoom 0.6
        offset (450,210)#270)

image Kitty_Sex_Fondle_Breasts:
        "GropeLeftBreast"
        zoom 1.1
        offset (320,-180)#-130)

image Kitty_Head_Sex:
    # The head used for the sex pose, referenced by Kitty_Sex_Body
    "Kitty_Head"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10

image Kitty_HairBack_Sex:
    # The hair behind the head for the sex pose, referenced by Kitty_Sex_Body
    "Kitty_HairBack"
    zoom 1.5
    anchor (0.5,0.5)
    rotate -10

#image Kitty_Sex_Legs = LiveComposite(
image Kitty_Sex_Legs:
    LiveComposite(
        #the legs used in the sex pose, referenced by Kitty_SexSprite
        (1120,840),
        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", "images/KittySex/Kitty_Sex_Legs_Dress_Back_Up.png",
            "KittyX.Legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Back.png",
            "KittyX.Legs == 'blue skirt'", "images/KittySex/Kitty_Sex_Skirt_Back.png",
            "True", Null(),
            ),
        (0,0), "images/KittySex/Kitty_Sex_Legs.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Legs.png",
            "True", Null(),
            ),

        (0,0), "Kitty_Sex_Anus",                                                                          #Anus Composite

        (0,0), "Kitty_Sex_Pussy",                                                                         #Pussy Composite

        (0,0), ConditionSwitch(                                                                                 #Panties if up
            "KittyX.PantiesDown", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", "images/KittySex/Kitty_Sex_Panties_Green_Wet.png",
            "KittyX.Panties == 'green panties'", "images/KittySex/Kitty_Sex_Panties_Green.png",
            "KittyX.Panties == 'lace panties' and KittyX.Wet", "images/KittySex/Kitty_Sex_Panties_Lace_Wet.png",
            "KittyX.Panties == 'lace panties'", "images/KittySex/Kitty_Sex_Panties_Lace.png",
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", "images/KittySex/Kitty_Sex_Panties_Bikini_Wet.png",
            "KittyX.Panties == 'bikini bottoms'", "images/KittySex/Kitty_Sex_Panties_Bikini.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittySex/Kitty_Sex_Hose_StockingGarter_Legs.png",
            "KittyX.Hose == 'garterbelt'", "images/KittySex/Kitty_Sex_Hose_Garter_Legs.png",
            "KittyX.Hose == 'stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_Legs.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", "images/KittySex/Kitty_Sex_Hose_Pantyhose_Legs.png",
#            "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", "images/KittySex/Kitty_Sex_Legs_Dress_Up.png",
            "KittyX.Legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress.png",
            "KittyX.Legs == 'blue skirt'", "images/KittySex/Kitty_Sex_Skirt.png",
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Pants_Blue_Wet.png",
            "KittyX.Legs == 'capris'", "images/KittySex/Kitty_Sex_Pants_Blue.png",
            "KittyX.Legs == 'black jeans' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Pants_Black_Wet.png",
            "KittyX.Legs == 'black jeans'", "images/KittySex/Kitty_Sex_Pants_Black.png",
            "KittyX.Legs == 'shorts' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Shorts_Wet.png",
            "KittyX.Legs == 'shorts'", "images/KittySex/Kitty_Sex_Shorts.png",
            "KittyX.Legs == 'yoga pants' and KittyX.Wet > 1", "images/KittySex/Kitty_Sex_Pants_Yoga_Wet.png",
            "KittyX.Legs == 'yoga pants'", "images/KittySex/Kitty_Sex_Pants_Yoga.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #Over Layer
            "KittyX.Over == 'towel' and not KittyX.Uptop", "images/KittySex/Kitty_Sex_Towel_Legs.png",
            "True", Null(),
            ),
        (0,0),ConditionSwitch(                                                                                  #Outside Spunk
            "'belly' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Pelvis.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                                 #hotdog cock Layer
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            "action_speed >= 2", "Kitty_Hotdog_Zero_Anim2",
            "action_speed", "Kitty_Hotdog_Zero_Anim1",
            "True", "Kitty_Hotdog_Zero_Anim0",
            ),
        (0,0), ConditionSwitch(
            #pussy licking animation
            "Player.Sprite and Player.Cock", Null(),
            "primary_action == 'lick pussy'", "Kitty_Sex_Lick_Pussy",
            "primary_action == 'lick ass'", "Kitty_Sex_Lick_Ass",
            "True", Null()
            ),
        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
            "not Player.Sprite or Player.Cock != 'foot'", Null(),
            "action_speed >= 2", "Kitty_Footcock_Zero_Anim2",
            "action_speed", "Kitty_Footcock_Zero_Anim1",
            "True", "Kitty_Footcock_Static",
            ),
#        (0,0), ConditionSwitch(                                                                                 #footjob cock Layer
#            "not Player.Sprite or Player.Cock != 'foot'", Null(),
#            "action_speed >= 2", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim2A()),
#            "action_speed", At("Kitty_Footcock", Kitty_Footcock_Zero_Anim1A()),
#            "True", At("Kitty_Footcock", Kitty_Footcock_StaticA()),
#            ),
#        (0,0), ConditionSwitch(                                                                                 #UI tool layer
#            "not UI_Tool", Null(),
#            "UI_Tool", "Slap_Ass",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(                                                         #Shows different lower body motion depending on events
            "not action_speed", "Kitty_Sex_Feet",
            "Player.Cock == 'anal' or Player.Cock == 'in' or Player.Cock == 'out'", AlphaMask("Kitty_Sex_Feet", "images/KittySex/Kitty_Sex_FeetMask.png"),
            "True", "Kitty_Sex_Feet",
            ),
        )

image Kitty_Sex_Feet = LiveComposite(
        #the lower legs used in the sex pose, referenced by Kitty_Sex_Legs
        (1120,840),
        (0,0), "images/KittySex/Kitty_Sex_Feet.png",                                                         #Legs Base
        (0,0), ConditionSwitch(                                                                                 #Wet look
            "KittyX.Water", "images/KittySex/Kitty_Sex_Water_Feet.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #hose layer
            "KittyX.Legs and not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'shorts'",ConditionSwitch(
                    #If she has pants on, I need alternate kneesocks to not clip through knees
                    "KittyX.Hose == 'stockings and garterbelt'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.Hose == 'stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.Hose == 'knee stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.Panties and KittyX.PantiesDown", Null(),
                    "KittyX.Hose == 'pantyhose'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
                    "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_FeetP.png",
                    "True", Null(),
                    ),
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'shorts') and KittyX.Hose == 'stockings and garterbelt'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'knee stockings'", "images/KittySex/Kitty_Sex_Hose_Stockings_FeetP.png",
            "KittyX.Hose == 'stockings' or KittyX.Hose == 'stockings and garterbelt'", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png",
            "KittyX.Hose == 'knee stockings'", "images/KittySex/Kitty_Sex_Hose_Kneesocks_Feet.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'pantyhose'", "images/KittySex/Kitty_Sex_Hose_Stockings_Feet.png",
#            "KittyX.Legs and (not KittyX.Upskirt and KittyX.Legs != 'blue skirt' and KittyX.Legs != 'blue skirt') and KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_FeetP.png",
            "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Feet.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(                                                                                 #Legs Layer
            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress'", "images/KittySex/Kitty_Sex_Legs_Dress_Feet.png",
            "KittyX.Legs == 'capris'", "images/KittySex/Kitty_Sex_Feet_Blue.png",
            "KittyX.Legs == 'black jeans'", "images/KittySex/Kitty_Sex_Feet_Black.png",
            "KittyX.Legs == 'yoga pants'", "images/KittySex/Kitty_Sex_Feet_Yoga.png",
            "True", Null(),
            ),
        )

image Kitty_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (530,510)

image Kitty_Sex_Lick_Ass:
        "Lick_Anim"
        zoom 0.7
        offset (535,590)

image GropeBack:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        zoom .7
        pos (300,420)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 90
        block:
            ease 1 rotate 60
            ease 1 rotate 90
            repeat

image TestingSolid:
        #this is a blank solid I use to test things.
        contains:
            Solid("#75d7ec", xysize=(1500,1500))
            alpha 0.2

#Start Animations for Kitty's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Pussy_Fucking0:
    # This is the visual for her pussy during the action_speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking1:
    # This is the visual for her pussy during the action_speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask")

image Kitty_Pussy_Fucking2:
    # This is the visual for her pussy during the action_speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask")
image Kitty_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the action_speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "True", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask")

image Kitty_Pussy_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Pussy_Mask.png"

image Kitty_Pussy_Open_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Pussy_Mask.png"
            yoffset 3

#image TestMask:
#        #This involves a working, shrinking and growing mask for the pussy
#        contains:
#            "images/KittySex/Kitty_Sex_Pussy_Mask.png"
#            subpixel True
#            anchor (0.5,0.63)
#            pos (0.5,0.63)
#            zoom 1
#            block:
#                ease 1 zoom .5
#                pause 1
#                ease 3 zoom 1
#                repeat

image Kitty_Pussy_Spunk_Heading:
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8

image Kitty_Sex_Pussy:
    # This is the visual for her pussy during the action_speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and action_speed", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                "primary_action == 'lick pussy'", "images/KittySex/Kitty_Sex_Pussy_Open.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not KittyX.Wet", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:
            #ring piercing
            ConditionSwitch(
                "KittyX.Pierce != 'ring'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or action_speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Ring.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_RingF.png",
                )
    contains:
            #barbell piercing
            ConditionSwitch(
                "KittyX.Pierce != 'barbell'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or action_speed <= 1", "images/KittySex/Kitty_Sex_Pussy_Barbell.png",
                "True", "images/KittySex/Kitty_Sex_Pussy_BarbellF.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not KittyX.Pubes", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", "images/KittySex/Kitty_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and action_speed", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                "primary_action == 'lick pussy'", "images/KittySex/Kitty_Sex_Pubes_Open.png",
                "True", "images/KittySex/Kitty_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'in' in KittyX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
                "True", Null(),
                )
    contains:
            #hose layer
            ConditionSwitch(
                "KittyX.Panties and KittyX.PantiesDown", Null(),
                "KittyX.Hose == 'ripped pantyhose'", "images/KittySex/Kitty_Sex_Hose_RippedPantyhose_Legs.png",
                "True", Null(),
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
                "not Player.Sprite", Null(),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 3", AlphaMask("Kitty_Sex_Zero_Anim3", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and action_speed >= 2", AlphaMask("Kitty_Sex_Zero_Anim2", "Kitty_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and action_speed", AlphaMask("Kitty_Sex_Zero_Anim1", "Kitty_Pussy_Open_Mask"),
                "Player.Sprite and Player.Cock == 'in'", AlphaMask("Kitty_Sex_Zero_Anim0", "Kitty_Pussy_Open_Mask"),
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'in' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'in' or not action_speed", Null(),
                "action_speed <= 1", "Kitty_Pussy_Spunk_Heading",
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",
                )

    #End Kitty Pussy composite

#End Animations for Kitty's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Zero_Anim0:
        #this is Kitty's sex animation, action_speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.4

image Kitty_Sex_Zero_Anim1:
        #this is Kitty's sex animation, action_speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,525) #X less is left, Y less is up(498,520)
            zoom 1.4
            block:
                ease 1 pos (498,510) #(498,500)
                pause 1
                ease 3 pos (498,525)
                repeat

image Kitty_Sex_Zero_Anim2:
        #this is Kitty's sex animation, action_speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,380) #(500,470)
                pause 1
                ease 3 pos (500,490)
                repeat

image Kitty_Sex_Zero_Anim3:
        #this is Kitty's sex animation, action_speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,490) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,380) #(500,470)
                pause .25
                ease 1.5 pos (500,490)
                repeat
#End Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Legs_Anim1:
        #this is the animation for Kitty's lower body during sex, action_speed 1 (heading)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat

image Kitty_Sex_Legs_Anim2:
        #this is the animation for Kitty's lower body during sex, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat

image Kitty_Sex_Legs_Anim3:
        #this is the animation for Kitty's lower body during sex, action_speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,0)
                repeat
#End Animations for Kitty's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Sex_Body_Anim1:
        #this is the animation for Kitty's upper body during sex, action_speed 1 (heading)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat

image Kitty_Sex_Body_Anim2:
        #this is the animation for Kitty's upper body during sex, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat

image Kitty_Sex_Body_Anim3:
        #this is the animation for Kitty's upper body during sex, action_speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,10)
                repeat
#End Animations for Kitty's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





#Start Animations for Kitty's Ass during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and action_speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and action_speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and action_speed", "Kitty_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Kitty_Sex_Anal_Tip",
            "KittyX.Loose", "images/KittySex/Kitty_Sex_Hole_Loose.png",
            "True", "images/KittySex/Kitty_Sex_Hole_Tight.png",
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in KittyX.Spunk", Null(),
                "Player.Sprite and Player.Cock != 'anal' and action_speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and action_speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",
                )
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
            "not Player.Sprite or Player.Cock != 'anal'", Null(),
            "action_speed >= 3",  AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Sex_Anal_Fucking_Mask"),
            "action_speed >= 2", AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Sex_Anal_Fucking_Mask"),
            "action_speed", AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Sex_Anal_Fucking_Mask"),
            "True", AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Sex_Anal_Fucking_Mask"),
            )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in KittyX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not action_speed", Null(),
                "action_speed == 1", "Kitty_Sex_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",
                )


image Kitty_Sex_Anal_Fucking0:
    # This is the visual for her pussy during the action_speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "Kitty_Sex_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim0", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking1:
    # This is the visual for her pussy during the action_speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "Kitty_Anal_Heading"
#            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim1", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking2:
    # This is the visual for her pussy during the action_speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim2", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking3:
    # This is the visual for her pussy during the action_speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Sex_Anal_Fucking_Mask")

image Kitty_Sex_Anal_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"

image Kitty_Sex_Anal_Open_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 3

image Kitty_Sex_Anal_Heading:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6
    block:
        #total 5 second
        ease .75 xzoom 1.0
        ease .25 xzoom 0.9
        pause 1.50
        ease .25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Kitty_Sex_Anal_Spunk_Heading_Over:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png"
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
image Kitty_Sex_Anal_Spunk_Heading_Under:
    "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png"
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

image Kitty_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6

#End Animations for Kitty's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Anal_Zero_Anim0:
        #this is Kitty's sex animation, action_speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up (498,520)
            zoom 1.4

image Kitty_Anal_Zero_Anim1:
        #this is Kitty's sex animation, action_speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,600) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,570) #(500,470)
                pause 1
                ease 3 pos (500,600)
                repeat

image Kitty_Anal_Zero_Anim2:
        #this is Kitty's sex animation, action_speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (500,450) #(500,470)
                pause 1
                ease 3 pos (500,570)
                repeat

image Kitty_Anal_Zero_Anim3:
        #this is Kitty's sex animation, action_speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,570) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .25 pos (500,450) #(500,470)
                pause .25
                ease 1.5 pos (500,570)
                repeat
#End Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Kitty_Hotdog_Zero_Anim0:
        #this is Kitty's sex animation, action_speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,570) #X less is left, Y less is up
            zoom 1.4

image Kitty_Hotdog_Zero_Anim1:
        #this is Kitty's sex animation, action_speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (498,500) #X less is left, Y less is up
            zoom 1.4
            block:
                ease 1 pos (498,560) #(500,500)
                pause .5
                ease 1.5 pos (498,500)
                repeat

image Kitty_Hotdog_Zero_Anim2:
        #this is Kitty's sex animation, action_speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (500,510) #X less is left, Y less is up
            zoom 1.4
            block:
                ease .5 pos (500,400) #(500,470)
                pause .5
                ease 1 pos (500,510)
                repeat

image Kitty_Hotdog_Body_Anim2:
        #this is the animation for Kitty's lower body during sex, action_speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat

image Kitty_Hotdog_Legs_Anim2:
        #this is the animation for Kitty's lower body during sex, action_speed 3 (fast)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat

#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Footcock:
    contains:
            subpixel True
            "Blowcock"
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
                #Total time, 4 seconds
                pause .5
                easein .75 ypos 360#65
                ease .25 ypos 355#60
                pause 1
                ease 2.50 ypos 270#285
                repeat
    pos (750,230)

image Kitty_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Kitty_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 ypos 360
                ease .2 ypos 355
                pause .2
                ease 1.00 ypos 270
                repeat
    pos (750,230)

transform Kitty_Footcock_Zero_Anim1A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset 60#65
                ease .25 yoffset 55#60
                pause 1
                ease 1.50 yoffset -30#285
                repeat

transform Kitty_Footcock_Zero_Anim2A():
            subpixel True
            offset (0,0)
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                pause .2
                easein .4 yoffset 60
                ease .2 yoffset 55
                pause .2
                ease 1.00 yoffset -30
                repeat

transform Kitty_Footcock_StaticA():
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat

image Kitty_Sex_Legs_FootAnim1:
        #this is the animation for Kitty's lower body during Footjobs, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-65)
                ease .25 pos (0,-60)
                pause 1
                ease 2.50 pos (0,25)#(0,10)
                repeat
        pos (750,230)

image Kitty_Sex_Legs_FootAnim2:
        #this is the animation for Kitty's lower body during Footjobs, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 pos (0,-65)
                ease .2 pos (0,-60)
                pause .2
                ease 1.0 pos (0,25)#(0,10)
                repeat
        pos (750,230)

image Kitty_Sex_Legs_FootAnimStatic:
        #this is the animation for Kitty's lower body during Footjobs, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)

transform Kitty_Sex_Legs_FootAnim1A():
        #this is the animation for Kitty's lower body during Footjobs, action_speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -65
                ease .25 yoffset -60
                pause 1
                ease 1.50 yoffset 25
                repeat

transform Kitty_Sex_Legs_FootAnim2A():
        #this is the animation for Kitty's lower body during Footjobs, action_speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                pause .2
                easein .4 yoffset -65
                ease .2 yoffset -60
                pause .2
                ease 1.0 yoffset 25
                repeat

transform Kitty_Sex_Legs_FootAnimStaticA():
        #this is the animation for Kitty's lower body during Footjobs, action_speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat

#End Animations for Kitty's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Kitty's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Kitty_Sex_Body_FootAnim1:
        #this is the animation for Kitty's upper body during Footjobs, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-25)#(0,-5)
                ease .25 pos (0,-15)#(0,0)
                pause 1
                ease 2.50 pos (0,15)#(0,5)
                repeat
        pos (750,230)

image Kitty_Sex_Body_FootAnim2:
        #this is the animation for Kitty's upper body during Footjobs, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 pos (0,-25)#(0,-5)
                ease .2 pos (0,-15)#(0,0)
                pause .2
                ease 1.0 pos (0,15)#(0,5)
                repeat
        pos (750,230)

image Kitty_Sex_Body_FootAnimStatic:
        #this is the animation for Kitty's upper body during Footjobs, action_speed 2 (slow)
        contains:
            subpixel True
            "Kitty_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        pos (750,230)

transform Kitty_Sex_Body_FootAnim1A():
        #this is the animation for Kitty's upper body during Footjobs, action_speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 yoffset -25
                ease .25 yoffset -15
                pause 1
                ease 1.50 yoffset 15
                repeat

transform Kitty_Sex_Body_FootAnim2A():
        #this is the animation for Kitty's upper body during Footjobs, action_speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                pause .2
                easein .4 yoffset -25
                ease .2 yoffset -15
                pause .2
                ease 1.0 yoffset 15
                repeat

transform Kitty_Sex_Body_FootAnimStaticA():
        #this is the animation for Kitty's upper body during Footjobs, action_speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat
#End Animations for Kitty's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# End Kitty Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





# Kitty Doggy Compositing ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#image Kitty_Doggy_Base = LiveComposite(
image Kitty_Doggy_Animation: #nee Kitty_Doggy
    LiveComposite(
        #Base body
        (420,750),
        (0,0), ConditionSwitch(
            #Shows different upper body motion depending on events
            "not Player.Sprite", "Kitty_Doggy_Body",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "action_speed", "Kitty_Doggy_Anal_Head_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Top",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Top",
                    "True", "Kitty_Doggy_Body",
                    ),
            "True", "Kitty_Doggy_Body",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "not Player.Sprite", "Kitty_Doggy_Ass",
            "Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "action_speed", "Kitty_Doggy_Anal_Head_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Doggy_Fuck2_Ass",
                    "action_speed > 1", "Kitty_Doggy_Fuck_Ass",
                    "True", "Kitty_Doggy_Ass",
                    ),
            "True", "Kitty_Doggy_Ass",
            ),
        (0,0), ConditionSwitch(
            #Shows different lower body motion depending on events
            "Player.Cock == 'foot'", ConditionSwitch(
                    "action_speed > 1", "Kitty_Doggy_Feet2",
                    "action_speed", "Kitty_Doggy_Feet1",
                    "True", "Kitty_Doggy_Feet0",
                    ),
            "not Player.Sprite and ShowFeet", "Kitty_Doggy_Feet0",
            "True", Null(),
            ),
        )
    align (0.6,0.0)
#    yoffset 0


image Kitty_Doggy_Body:
    LiveComposite(
        #Upper body
        (420,750),
#        (165,0),"Kitty_Doggy_Hair_Under", #back of the hair
        (0,105), "Kitty_Doggy_Head",               #Head(165,0)
        #(0,0), "images/JeanDoggy/Jean_Doggy_Breast.png", #Body base
#        (0,0), "images/KittyDoggy/Kitty_Doggy_HeadRef.png", # reference head
        (0,0), "images/KittyDoggy/Kitty_Doggy_Body.png", #Body base
        (0,0), ConditionSwitch(
            #bra
            "not KittyX.Chest", Null(),
            "KittyX.Uptop", ConditionSwitch(
                    "KittyX.Over and KittyX.Over != 'towel' and KittyX.Over != 'jacket'", Null(),
                    "KittyX.Chest == 'dress' and KittyX.Over and KittyX.Over != 'towel'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_UpC.png",
                    "KittyX.Chest == 'dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress_Up.png",
                    "KittyX.Chest == 'cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami_Up.png",
                    "KittyX.Chest == 'lace bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
                    "KittyX.Chest == 'sports bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports_Up.png",
                    "KittyX.Chest == 'bikini top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
                    ),
            "KittyX.Chest == 'dress'", "images/KittyDoggy/Kitty_Doggy_Bra_Dress.png",
            "KittyX.Chest == 'cami'", "images/KittyDoggy/Kitty_Doggy_Bra_Cami.png",
            "KittyX.Chest == 'lace bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Lace.png",
            "KittyX.Chest == 'sports bra'", "images/KittyDoggy/Kitty_Doggy_Bra_Sports.png",
            "KittyX.Chest == 'bikini top'", "images/KittyDoggy/Kitty_Doggy_Bra_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Bra.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Body_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Overshirt
            "not KittyX.Over", Null(),
            "KittyX.Over == 'jacket'", "images/KittyDoggy/Kitty_Doggy_Over_Jacket.png",
            "KittyX.Over == 'red shirt'", "images/KittyDoggy/Kitty_Doggy_Over_Red.png",
            "KittyX.Over == 'pink top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink.png",
            "KittyX.Over == 'towel' and not KittyX.Uptop", "images/KittyDoggy/Kitty_Doggy_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in KittyX.Spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #breast fondling animation
            "primary_action == 'fondle breasts' or offhand_action == 'fondle breasts'", "Kitty_Doggy_GropeBreast",
            "True", Null()
            ),
        #(161,-1), "Jean_Doggy_Head",               #Head
#        (165,0),"Jean_Doggy_Hair_Over", #front of the hair
        )
#    transform_anchor True
#    anchor (225,1400)
    offset (-30,0)#(-190,-40)
#    rotate 20


image Kitty_Doggy_Head:
    LiveComposite(
        #Head
        (420,750),
        #(0,0), "images/JeanDoggy/Jean_Doggy_Head.png", #Body base
        #(0,0), "images/JeanDoggy/Jean_Doggy_TestArm.png",#Eyes
        (0,0), ConditionSwitch(
            #Head
#            "KittyX.Blush > 1", "images/KittyDoggy/Kitty_Doggy_Head_Blush2.png",
            "KittyX.Blush", "images/KittyDoggy/Kitty_Doggy_Head_Blush.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Head.png",
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "KittyX.Mouth == 'normal'", "images/KittyDoggy/Kitty_Doggy_Mouth_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.Mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Mouth_Tongue.png",
            "KittyX.Mouth == 'kiss'", "images/KittyDoggy/Kitty_Doggy_Mouth_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_Mouth_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.Mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Mouth_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Mouth_Kiss.png",
            "KittyX.Mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Mouth_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Mouth_Normal.png",
            ),
#        (0,0), ConditionSwitch(
#            #chin spunk
#            "'chin' in KittyX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Chin.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #Mouth spunk
            "'mouth' not in KittyX.Spunk", Null(),
            #"KittyX.Mouth == 'normal'", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            #"KittyX.Mouth == 'sad'", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.Mouth == 'smile'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.Mouth == 'grimace'", "images/KittyDoggy/Kitty_Doggy_Spunk_Smile.png",
            "KittyX.Mouth == 'sucking'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",
            #"KittyX.Mouth == 'kiss'", "images/KittyDoggy/Kitty_Doggy_Spunk_Open.png",
#            "KittyX.Mouth == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            "KittyX.Mouth == 'tongue'", "images/KittyDoggy/Kitty_Doggy_Spunk_Tongue.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Spunk_Normal.png",
            ),
        (0,0), ConditionSwitch(
            #Brows
            #"KittyX.Brows == 'normal'", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittyDoggy/Kitty_Doggy_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittyDoggy/Kitty_Doggy_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Brows_Surprised.png",
            #"KittyX.Brows == 'confused'", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Brows_Normal.png",
            ),
        (0,0), "Kitty Doggy Blink",#Eyes
#        (0,0), ConditionSwitch(
#            #wet hair strand
#            "KittyX.Water or KittyX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
#            "True", Null(),
#            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'facial' in KittyX.Spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittyDoggy/Kitty_Doggy_Hair_Wet.png",
            "KittyX.Hair == 'long'", "images/KittyDoggy/Kitty_Doggy_Hair_Long.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Hair_Evo.png",
            ),
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Head_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #face spunk
            "'hair' in KittyX.Spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 0.8 #.83
    #alpha 0.9

#image Kitty_Doggy_Hair_Under:
#        #hair under body
#        ConditionSwitch(
#                "KittyX.Water or KittyX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Under.png",
#                "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Under.png",
#                )
#        zoom 0.83

#image Kitty_Doggy_Hair_Over:
#        #hair under body
#        contains:
#            ConditionSwitch(
#                    "KittyX.Water or KittyX.Hair == 'wet'", "images/JeanDoggy/Jean_Doggy_Hair_Wet_Over.png",
#                    "True", "images/JeanDoggy/Jean_Doggy_Hair_Short_Over.png",
#                    )
#        contains:
#            ConditionSwitch(
#                #face spunk
#                "'facial' in KittyX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Facial.png",
#                "True", Null(),
#                )
#        contains:
#            ConditionSwitch(
#                #face spunk
#                "'hair' in KittyX.Spunk", "images/JeanDoggy/Jean_Doggy_Spunk_Facial2.png",
#                "True", Null(),
#                )
#        zoom 0.83
#        #alpha 0.7

image Kitty Doggy Blink:
        #Eyes
        ConditionSwitch(
        "KittyX.Eyes == 'sexy'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
        "KittyX.Eyes == 'side'", "images/KittyDoggy/Kitty_Doggy_Eyes_Side.png",
#        "KittyX.Eyes == 'normal'", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
        "KittyX.Eyes == 'closed'", "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png",
#        "KittyX.Eyes == 'manic'", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
        "KittyX.Eyes == 'down'", "images/KittyDoggy/Kitty_Doggy_Eyes_Down.png",
        "KittyX.Eyes == 'stunned'", "images/KittyDoggy/Kitty_Doggy_Eyes_Stunned.png",
#        "KittyX.Eyes == 'surprised'", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
        "KittyX.Eyes == 'squint'", "images/KittyDoggy/Kitty_Doggy_Eyes_Sexy.png",
        "True", "images/KittyDoggy/Kitty_Doggy_Eyes_Normal.png",
        ),
    #    choice:
    #        3.5
    #    choice:
    #        3.25
    #    choice:
    #        3
        3
        # This randomizes the time between blinking.
        "images/KittyDoggy/Kitty_Doggy_Eyes_Closed.png"
        .25
        repeat

image Kitty_Doggy_Ass:
    LiveComposite(
        #Lower body
        (420,750),
        (0,0), ConditionSwitch(
            #Legs backside
            "not KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress'", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Back.png",
            "KittyX.Legs == 'shorts' and KittyX.Wet", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_BackW.png",
            "KittyX.Legs == 'shorts'", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Back.png",
            "KittyX.Legs == 'yoga pants'", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Back.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Panties back
            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", "images/KittyDoggy/Kitty_Doggy_Panties_Green_BackW.png",
            "KittyX.Panties == 'green panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Back.png",
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_BackW.png",
            "KittyX.Panties == 'bikini bottoms'","images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Back.png",
            "KittyX.Panties == 'lace panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Back.png",
            "True", Null(),
            ),
        (0,0), "images/KittyDoggy/Kitty_Doggy_Ass.png", #Ass Base
        (0,0), ConditionSwitch(
            #Wet look
            "KittyX.Water", "images/KittyDoggy/Kitty_Doggy_Ass_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #Hose
            "KittyX.Hose == 'stockings'", "images/KittyDoggy/Kitty_Doggy_Hose_Stockings.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "(KittyX.Legs and KittyX.Legs != 'blue skirt') and not KittyX.Upskirt", Null(),
            "KittyX.Hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Panties if Down
            "not KittyX.PantiesDown or (KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt)", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", "images/KittyDoggy/Kitty_Doggy_Panties_Green_DownW.png",
            "KittyX.Panties == 'green panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green_Down.png",
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_DownW.png",
            "KittyX.Panties == 'bikini bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini_Down.png",
            "KittyX.Panties == 'lace panties'","images/KittyDoggy/Kitty_Doggy_Panties_Lace_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Legs Layer if down
            "KittyX.Hose and KittyX.Hose != 'garterbelt'", Null(),
            "KittyX.Legs == 'capris' and KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png",
            "KittyX.Legs == 'black jeans' and KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png",
            "KittyX.Legs == 'yoga pants' and KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png",
            "KittyX.Legs == 'shorts' and KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Pussy Composite
            "Player.Sprite and Player.Cock == 'in'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Pussy_Fucking3",#action_speed 3
                    "action_speed > 1", "Kitty_Pussy_Fucking2",#action_speed 2
                    "action_speed", "Kitty_Pussy_Heading",      #action_speed 1
                    "True", "Kitty_Pussy_Static",              #action_speed 0
                    ),
            "primary_action == 'lick pussy'", "images/KittyDoggy/Kitty_Doggy_Pussy_Open.png",
            "KittyX.Legs and not KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "KittyX.Panties and not KittyX.PantiesDown", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'", "Kitty_Pussy_Fingering",
            "primary_action == 'dildo pussy'", "Kitty_Pussy_Fucking2",
            "True", "images/KittyDoggy/Kitty_Doggy_Pussy_Closed.png",
            ),

        (0,0), ConditionSwitch(
            #spunkpussy Layer
            "'in' in KittyX.Spunk and Player.Cock == 'in'",Null(),# "images/JeanDoggy/Jean_Doggy_SpunkPussyOpen.png",  #fix for KittyX.Spunk is used later
            "'in' in KittyX.Spunk ", "images/JeanDoggy/Jean_Doggy_SpunkPussyClosed.png",
            "KittyX.Wet and Player.Cock == 'in'", "images/RogueDoggy/Rogue_Doggy_WetPussyOpen.png",
            "KittyX.Wet", "images/RogueDoggy/Rogue_Doggy_WetPussyClosed.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #pubes
            "not KittyX.Pubes", Null(),
            "Player.Sprite and Player.Cock == 'in'", Null(), # "images/KittyDoggy/Kitty_Doggy_Pubes_Fucked.png",
            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "(KittyX.Legs and KittyX.Legs != 'blue skirt') and not KittyX.Upskirt", Null(),
            "KittyX.PantiesDown and primary_action == 'lick pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "KittyX.Panties and KittyX.PantiesDown", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            "KittyX.Panties", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "KittyX.Hose == 'pantyhose' and primary_action == 'lick pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_OpenC.png",
            "KittyX.Hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_PubesC.png",
            "primary_action == 'lick pussy'", "images/KittyDoggy/Kitty_Doggy_Pubes_Open.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Pubes.png",
            ),
        (0,0), ConditionSwitch(
            #Pussy Piercings
            "Player.Sprite", Null(),
            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
            "KittyX.Pierce == 'barbell'", "images/KittyDoggy/Kitty_Doggy_Pierce_Barbell.png",
            "KittyX.Pierce == 'ring' and KittyX.Panties and not KittyX.PantiesDown", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.Pierce == 'ring' and KittyX.Hose == 'pantyhose' and not (KittyX.Panties and KittyX.PantiesDown)", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.Pierce == 'ring' and KittyX.Legs and KittyX.Legs != 'blue skirt' and not KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Pierce_RingC.png",
            "KittyX.Pierce == 'ring'", "images/KittyDoggy/Kitty_Doggy_Pierce_Ring.png",
            "True", Null(),
            ),


        (0,0), ConditionSwitch(
            #Anus Composite
            "Player.Sprite and Player.Cock == 'anal'", ConditionSwitch(
                    "action_speed > 2", "Kitty_Anal_Fucking2", #action_speed 3
                    "action_speed > 1", "Kitty_Anal_Fucking",  #action_speed 2
                    "action_speed", "Kitty_Anal_Heading",      #action_speed 1
                    "True", "Kitty_Anal",               #action_speed 0
                    ),
#            "Action == 'plug'", "Jean_Anal_Plug",
#            "Action == 'plug'", "test_case",
            "KittyX.Legs and not KittyX.Upskirt", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "KittyX.Panties and not KittyX.PantiesDown", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "primary_action == 'insert ass' or offhand_action == 'insert ass'", "Kitty_Anal_Fingering",
            "primary_action == 'dildo anal'", "Kitty_Anal_Fucking",
            "KittyX.Loose", "images/JeanDoggy/Jean_Doggy_Asshole_Loose.png",
            "True", "images/JeanDoggy/Jean_Doggy_Asshole_Tight.png",
            ),


#        (0,0), ConditionSwitch(
#            #spunkanal Layer
#            "'anal' not in KittyX.Spunk or Player.Sprite", Null(),
#            "Player.Cock == 'anal'", "images/RogueDoggy/Rogue_Doggy_SpunkAnalOpen.png",
#            "KittyX.Loose", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
#            "True", "images/RogueDoggy/Rogue_Doggy_SpunkAnalLoose.png",
#            ),
        (0,0), ConditionSwitch(
            #Panties if up
            "KittyX.PantiesDown or not KittyX.Panties", Null(),
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
#            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'",Null(),
#            "primary_action == 'dildo pussy'", Null(),
            "KittyX.Panties == 'green panties' and KittyX.Wet", "images/KittyDoggy/Kitty_Doggy_Panties_GreenW.png",
            "KittyX.Panties == 'green panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            "KittyX.Panties == 'lace panties'", "images/KittyDoggy/Kitty_Doggy_Panties_Lace.png",
            "KittyX.Panties == 'bikini bottoms' and KittyX.Wet", "images/KittyDoggy/Kitty_Doggy_Panties_BikiniW.png",
            "KittyX.Panties == 'bikini bottoms'", "images/KittyDoggy/Kitty_Doggy_Panties_Bikini.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Panties_Green.png",
            ),
        (0,0), ConditionSwitch(        #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
            #full hose/tights
            "Player.Sprite and (Player.Cock == 'in' or Player.Cock == 'anal')", Null(),
            "primary_action == 'fondle pussy' or offhand_action == 'fondle pussy'",Null(),
            "primary_action == 'dildo pussy'", Null(),
#            "KittyX.Panties and KittyX.PantiesDown and KittyX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "(KittyX.Legs or KittyX.Legs == 'blue skirt') or not KittyX.Upskirt", Null(),   #maybe?
            "KittyX.Hose == 'pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_Pantyhose.png",
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Legs Layer
            "KittyX.Legs == 'dress'", ConditionSwitch(
                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Dress_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Dress.png",
                    ),
            "KittyX.Legs == 'blue skirt'", ConditionSwitch(
                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt_Up.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_BlueSkirt.png",
                    ),

            "KittyX.Upskirt", Null(),
            "KittyX.Legs == 'capris'", ConditionSwitch(
#                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Blue_Down.png",
                    "KittyX.Wet > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlueW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Blue.png",
                    ),
            "KittyX.Legs == 'black jeans'", ConditionSwitch(
#                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Black_Down.png",
                    "KittyX.Wet > 1", "images/KittyDoggy/Kitty_Doggy_Legs_BlackW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Black.png",
                    ),
            "KittyX.Legs == 'yoga pants'", ConditionSwitch(
#                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga_Down.png",
                    "KittyX.Wet > 1", "images/KittyDoggy/Kitty_Doggy_Legs_YogaW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Yoga.png",
                    ),
            "KittyX.Legs == 'shorts'", ConditionSwitch(
#                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts_Down.png",
                    "KittyX.Wet > 1", "images/KittyDoggy/Kitty_Doggy_Legs_ShortsW.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Shorts.png",
                    ),
#            "KittyX.Legs == 'skirt'", ConditionSwitch(
#                    "KittyX.Upskirt and Player.Sprite and Player.Cock == 'anal' and action_speed" , "images/KittyDoggy/Kitty_Doggy_Legs_Skirt_Up.png",   #Rogue_Doggy_Legs_Skirt_UpAnal.png",
#                    "KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Skirt_Up.png",
#                    "True", "images/KittyDoggy/Kitty_Doggy_Legs_Skirt.png",
#                    ),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over Layer
            "KittyX.Legs == 'blue skirt' and KittyX.Upskirt", Null(),
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Null(),
            "KittyX.Over == 'pink top'", "images/KittyDoggy/Kitty_Doggy_Over_Pink_Tail.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Over Layer
            "KittyX.Legs == 'dress' and KittyX.Upskirt", Null(),
            "KittyX.Over == 'towel' and KittyX.Uptop", Null(),
            "KittyX.Over == 'towel' and KittyX.Upskirt", "images/KittyDoggy/Kitty_Doggy_Legs_Towel_Up.png",
            "KittyX.Over == 'towel'", "images/KittyDoggy/Kitty_Doggy_Legs_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #spunk back Layer
            "'back' in KittyX.Spunk", "images/KittyDoggy/Kitty_Doggy_Spunk_Ass.png",
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
#            "KittyX.Legs == 'skirt' and KittyX.Upskirt", "images/JeanDoggy/Jean_Doggy_Hotdog_Upskirt_Back.png",
            "True", "images/KittyDoggy/Kitty_Doggy_HotdogBack.png",
            ),
        (0,0), ConditionSwitch(
            #Hotdogging Cock w/ alpha
            "not Player.Sprite or Player.Cock != 'out'", Null(),
            #"KittyX.Legs == 'skirt' and KittyX.Upskirt and action_speed", AlphaMask("Zero_Hotdog_Moving", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
            #"KittyX.Legs == 'skirt' and KittyX.Upskirt", AlphaMask("Zero_Hotdog_Static", "images/RogueDoggy/Rogue_Doggy_HotdogMask_Upskirt.png"),
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


image Kitty_Doggy_Feet:         #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    contains:
            AlphaMask("Kitty_Doggy_Shins", "images/KittyDoggy/Kitty_Doggy_Feet_Mask.png")

image Kitty_Doggy_Shins:             #fix // // // // // // fix // // // // // // fix // // // // // // fix // // // // // //
    #Kitty's footjob shins
#    contains:
#            "images/KittyDoggy/Kitty_Doggy_Feet_Legs.png"
    contains:
            #hose legs
        ConditionSwitch(
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hole.png",
            "KittyX.Hose and KittyX.Hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet_Legs.png"
            )
    contains:
        #pants
        ConditionSwitch(
            "KittyX.Legs == 'capris'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Blue.png",
            "KittyX.Legs == 'black jeans'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Black.png",
            "KittyX.Legs == 'yoga pants'", "images/KittyDoggy/Kitty_Doggy_Feet_Legs_Yoga.png",
            "True", Null(),
            )
#    contains:
#        "images/KittyDoggy/Kitty_Doggy_Feet.png"
    contains:
            #hose toes
        ConditionSwitch(
            "not Player.Sprite or Player.Cock == 'foot'", ConditionSwitch(
                    "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_HoleF.png",
                    "KittyX.Hose and KittyX.Hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_HoseF.png",
                    "True", "images/KittyDoggy/Kitty_Doggy_FeetF.png"  #If you're doing the footjob
                    ),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose_Hole.png",
            "KittyX.Hose and KittyX.Hose != 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Feet_Hose.png",
            "True", "images/KittyDoggy/Kitty_Doggy_Feet.png"
            )
#    pos (0,0)

#image Kitty_Doggy_Lick_Pussy:
#        "Lick_Anim"
#        zoom 0.5
#        offset (195,540)

#image Kitty_Doggy_Lick_Ass:
#        "Lick_Anim"
#        zoom 0.5
#        offset (195,500)

image Kitty_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (110,420)#(150,340)
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

image Zero_Kitty_Hotdog_Static:
    # The unmoving version of the hotdog cock
    # called in Doggy Ass LC
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Kitty_Hotdog_Moving:
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

image Zero_Kitty_Doggy_Static:
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

image Zero_Kitty_Doggy_Heading:
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

image Zero_Kitty_Doggy_Fucking2:
    # Sex action_speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Kitty_Doggy_Fucking3:
    # Sex action_speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

image Kitty_Pussy_Mask:
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

image Kitty_Pussy_Mask_Static:
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
#            "KittyX.PantiesDown", Null(),
#            "KittyX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
#            "KittyX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
##            "KittyX.Hose == 'tights' and KittyX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
##            "KittyX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
##            "KittyX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",
#            "KittyX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "KittyX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
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


image Kitty_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:
        #moving hole
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
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
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Kitty_Doggy_Static", "Kitty_Pussy_Mask_Static")

    contains:
        # expanding pussy flap
        AlphaMask("Kitty_PussyHole_Static", "Kitty_Pussy_Hole_Mask_Static")

image Kitty_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Kitty_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Kitty_PussyHole_Static:
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


image Kitty_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
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
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Kitty_Doggy_Heading", "Kitty_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")


image Kitty_Pussy_Hole_Mask:
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

image Kitty_Pussy_Heading_Flap:
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


image Kitty_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
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
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
#            "KittyX.Hose == 'ripped tights'", "images/KittyDoggy/Kitty_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:
        #Cock
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")


    contains:
        # expanding pussy flap
        AlphaMask("Kitty_Pussy_Heading_Flap", "Kitty_Pussy_Hole_Mask")

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Kitty_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            "primary_action == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Kitty_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),
#        AlphaMask("Zero_Kitty_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")


image Kitty_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Kitty_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

image Kitty_Anal:
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
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)

image Kitty_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
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
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
#            "KittyX.Hose == 'ripped tights'", "images/KittyDoggy/Kitty_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock with mask
        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Kitty_Anal_Heading:
    #Animation for speed 1
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
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
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock masking fixer (for when the bottom part tries to cut off)
        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Zero_Kitty_Doggy_Anal_HeadingJunk")
    contains:
        #Cock with mask
        AlphaMask("Zero_Kitty_Doggy_Anal_Heading", "Kitty_Doggy_Anal_Heading_Mask")

image Zero_Kitty_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Kitty_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

image Kitty_Doggy_Anal_Heading_Mask:
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

image Kitty_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Kitty_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Kitty_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

image Kitty_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
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
            #full hose/tights
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "primary_action == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Kitty_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),
#        AlphaMask("Zero_Kitty_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Kitty_Doggy_Anal_FullMask:   #unused anymore?
    contains:
        #Mask
        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png" #FullMask?
#    contains:
#        #Cheeks
#        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )

image Kitty_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0#15
        pause .4
        block:
            ease .2 ypos -10#5
            pause .3
            ease 2 ypos 0#15
            repeat

image Kitty_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Kitty_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
            repeat

image Kitty_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Base
        "images/KittyDoggy/Kitty_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/KittyDoggy/Kitty_Doggy_Anal_FullHole.png"
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
#    contains:
#        #Mask
#        "images/JeanDoggy/Jean_Doggy_Anal_FullMask.png"
#    contains:
#        #Cheeks
#        "images/JeanDoggy/Jean_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "KittyX.Hose == 'garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_Garter.png",
            "KittyX.Hose == 'stockings and garterbelt'", "images/KittyDoggy/Kitty_Doggy_Hose_StockingGarter.png",
            "KittyX.Panties and KittyX.PantiesDown", Null(),
            "KittyX.Hose == 'ripped pantyhose'", "images/KittyDoggy/Kitty_Doggy_Hose_PantyhoseHoled.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Kitty_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Kitty_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Kitty_Doggy_Body"
        ypos 0#20
        block:
            pause .15
            ease .1 ypos -20#0
            pause .1
            easein .5 ypos 0#20
            pause .05
            repeat

image Kitty_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Kitty_Doggy_Ass"
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

image Kitty_Doggy_Feet0:
    #static animation
    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 0#20
            pause .5
            ease 2 ypos -20#0
            repeat
    contains:
        ConditionSwitch(
                "Player.Sprite", "Zero_Doggy_Up",
                "True", Null(),
                )
        zoom 1.2
        pos (158,520)  #(160,480)
    contains:
        "Kitty_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 0#20
            pause .5
            ease 2 ypos -20#0
            repeat

image Kitty_Doggy_Feet1:
    #slow animation
    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20) #(0,0) top
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
        "Kitty_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos -20
            repeat

image Kitty_Doggy_Feet2:
    #fast animation
    contains:
        "Kitty_Doggy_Shins"
        pos (0, -20) #(0,0) top
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
        "Kitty_Doggy_Feet"
        pos (0, -20) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos -20
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Kitty_Doggy_Launch(line = primary_action):
    if renpy.showing("Kitty_Doggy_Animation"):
        return
    $ action_speed = 0
    call Kitty_Hide(1)
    show Kitty_Doggy_Animation at sprite_location(StageCenter+50) zorder 150
    with dissolve
    return




# Start Kitty Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Kitty BJ element
#Kitty BJ Over Sprite Compositing


image Kitty_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            # Kitty's body, everything below the chin
            "action_speed == 0", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_0()),           #Static
            "action_speed == 1", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_1()),           #Licking
            "action_speed == 2", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_2()),           #Heading
            "action_speed == 3", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_3()),           #Sucking
            "action_speed == 4", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_4()),           #Deepthroat
            "action_speed == 5", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_5()),           #Cumming High
            "action_speed == 6", At("Kitty_BJ_Backdrop", Kitty_BJ_Body_6()),           #Cumming Deep
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # Kitty's head Underlay
            "action_speed == 0", At("Kitty_BJ_Head", Kitty_BJ_Head_0()),               #Static
            "action_speed == 1", At("Kitty_BJ_Head", Kitty_BJ_Head_1()),               #Licking
            "action_speed == 2", At("Kitty_BJ_Head", Kitty_BJ_Head_2()),               #Heading
            "action_speed == 3", At("Kitty_BJ_Head", Kitty_BJ_Head_3()),               #Sucking
            "action_speed == 4", At("Kitty_BJ_Head", Kitty_BJ_Head_4()),               #Deepthroat
            "action_speed == 5", At("Kitty_BJ_Head", Kitty_BJ_Head_5()),               #Cumming High
            "action_speed == 6", At("Kitty_BJ_Head", Kitty_BJ_Head_6()),               #Cumming Deep
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # Cock
            "action_speed == 0", At("Blowcock", Kitty_BJ_Cock_0()),                    #Static
            "action_speed == 1", At("Blowcock", Kitty_BJ_Cock_1()),                    #Licking
            "action_speed >= 2", At("Blowcock", Kitty_BJ_Cock_2()),                    #Heading+
#            "action_speed == 2", At("Blowcock", Kitty_BJ_Cock_2()),                    #Heading
#            "action_speed == 3", At("Blowcock", Kitty_BJ_Cock_2()),                    #Sucking
#            "action_speed == 4", At("Blowcock", Kitty_BJ_Cock_2()),                    #Deepthroat
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # the masked overlay for when her head overlaps the cock
            "action_speed < 3", Null(),
            "action_speed == 3", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_3()), #Sucking
            "action_speed == 4", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_4()), #Deepthroat
            "action_speed == 6", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MouthSuckingMask"), Kitty_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),
        (-270,-160), ConditionSwitch(
            # same as above, but for the heading animation
            "action_speed == 2", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_2()), #Heading
            "action_speed == 5", At(AlphaMask("Kitty_BJ_Head", "Kitty_BJ_MaskHeadingComposite"), Kitty_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),
        (325,490), ConditionSwitch(
            # the over part of spunk
            "action_speed < 3 or 'mouth' not in KittyX.Spunk", Null(),
            "action_speed == 3", At("KittySuckingSpunk", Kitty_BJ_Head_3()), #Sucking
            "action_speed == 4", At("KittySuckingSpunk", Kitty_BJ_Head_4()), #Deepthroat
            "action_speed == 6", At("KittySuckingSpunk", Kitty_BJ_Head_6()), #Cumming Deep
            "True", Null(),
            ),
        (325,490), ConditionSwitch(
            # same as above, but for the heading animation
            "action_speed == 2 and 'mouth' in KittyX.Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_2()), #Heading
            "action_speed == 5 and 'mouth' in KittyX.Spunk", At("Kitty_BJ_MaskHeadingSpunk", Kitty_BJ_Head_5()), #Cumming High
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Kitty_BJ_HairBack:
    #Hair underlay
    ConditionSwitch(
            "KittyX.Water and KittyX.Hair == 'evo'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png",
            "KittyX.Hair == 'long'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png",
            "True", Null(),
            ),
    zoom 1.4
    anchor (0.5, 0.5)
    yoffset 50

#image Kitty_BJ_Backdrop:                                                                        #Her Body under the head
#    "Kitty_Sprite"
#    zoom 4.8 #4.5
#    pos (175,-110)
#    offset (-500,-280)#(-450,-200) #(-615, -125)

image Kitty_BJ_Backdrop:
    #Her Body under the head
    LiveComposite(
        (858,928),
        (-375,250), ConditionSwitch(
            #blanket
            "'blanket' in KittyX.recent_history", "images/KittyBJFace/Kitty_BJFace_Blanket.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #red shirt under
            "KittyX.Over == 'red shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedUnder.png",
            "True", Null(),
            ),
        (0,0),"images/KittyBJFace/Kitty_BJ_Body.png",
            #body
        (0,0), ConditionSwitch(
            #necklace
            "KittyX.Neck == 'gold necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Gold.png",
            "KittyX.Neck == 'star necklace'", "images/KittyBJFace/Kitty_BJ_Neck_Star.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # piercings
            "not KittyX.Pierce", Null(),
            "KittyX.Pierce == 'ring'", "images/KittyBJFace/Kitty_BJ_PierceRing.png",
            "True", "images/KittyBJFace/Kitty_BJ_PierceBall.png",
            ),
        (0,0), ConditionSwitch(
            # wet body
            "not KittyX.Water", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Wet_Body.png",
            ),

        (0,0), ConditionSwitch(
            #Bra
            "not KittyX.Chest", Null(),
            "KittyX.Chest == 'lace bra'", "images/KittyBJFace/Kitty_BJ_Bra_Lace.png",
            "KittyX.Chest == 'sports bra'", "images/KittyBJFace/Kitty_BJ_Bra_Sport.png",
            "KittyX.Chest == 'bra'", "images/KittyBJFace/Kitty_BJ_Bra.png",
            "KittyX.Chest == 'cami'", "images/KittyBJFace/Kitty_BJ_Bra_Cami.png",
            "True", Null(),
            ),

        (0,0), ConditionSwitch(
            #Shirt
            "not KittyX.Over", Null(),
            "KittyX.Over == 'pink top'", "images/KittyBJFace/Kitty_BJ_Over_PinkShirt.png",
            "KittyX.Over == 'red shirt'", "images/KittyBJFace/Kitty_BJ_Over_RedShirt.png",
            "KittyX.Over == 'towel'", "images/KittyBJFace/Kitty_BJ_Over_Towel.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Spunk
            "'tits' not in KittyX.Spunk", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_Body.png",
            ),
        )
    zoom 1.5
    offset (-300,-200)

image Kitty_BJ_Head:                                                                            #These are all the details of the face
    LiveComposite(
        (858,928),
        (0,0), ConditionSwitch(
            #Hair back
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittyBJFace/Kitty_BJ_HairBackWet.png", #AlphaMask("images/KittyBJFace/Kitty_BJ_HairBackWet.png", "Kitty_BJ_Backdrop"),
            "True", Null(),
            ),
#        (0,0), ConditionSwitch(       #Legacy, the bellow version should do the same role
#            # Underface for sucking
#            "action_speed > 2 and action_speed != 5", Null(),
#            "KittyX.Water and KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",
#            "KittyX.Water", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png",
#            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",
#            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
#            ),
#        (0,0), ConditionSwitch(
#            # Underface for not sucking
#            "action_speed <= 2 or action_speed == 5", Null(),   #"action_speed <= 2 or primary_action != 'blow' or action_speed == 5", Null(),
#            "KittyX.Water and KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",
#            "KittyX.Water", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png",
#            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",
#            "True", "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
#            ),
        (0,0), ConditionSwitch(
            # Basic Face layer
            "action_speed <= 2 or action_speed == 5 or not renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(
                    # If the animation isn't sucking, or if not in BJ pose
                    "KittyX.Water", ConditionSwitch(
                            # If she's wet
                            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet_Blush.png",
                            "True", "images/KittyBJFace/Kitty_BJ_FaceClosed_Wet.png",
                            ),
                    "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceClosed_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceClosed.png"
                    ),
            #if it is in the open, sucking position
            "KittyX.Water", ConditionSwitch(
                    # If she's wet
                    "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet_Blush.png",
                    "True", "images/KittyBJFace/Kitty_BJ_FaceOpen_Wet.png",
                    ),
            "KittyX.Blush", "images/KittyBJFace/Kitty_BJ_FaceOpen_Blush.png",
            "True",  "images/KittyBJFace/Kitty_BJ_FaceOpen.png"
            ),
        (0,0), ConditionSwitch(
            #Mouth
            "action_speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",  #licking
                    "(action_speed == 2 or action_speed == 5)", Null(),                          #heading
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #sucking
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #deepthroat
                    "action_speed == 6", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #cumming
                    "True", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png", #cumming
                    ),
            "action_speed == 3 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Mouth_Lipbite.png",
            "KittyX.Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png",
            "KittyX.Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Mouth_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Mouth_Sad.png",
            "KittyX.Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.Mouth == 'grimace'", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Mouth_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Mouth_Tongue.png",
            "True", "images/KittyBJFace/Kitty_BJ_Mouth_Smile.png",
            ),
        (428,605), ConditionSwitch(
            # Heading Mouth
#            "action_speed == 2 and primary_action == 'blow'", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnim()),  #heading
            "not renpy.showing('Kitty_BJ_Animation')", Null(),
            "action_speed == 2", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnim()),  #heading
            "action_speed == 5", At("Kitty_BJ_MouthHeading", Kitty_BJ_MouthAnimC()), #cumming high
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Spunk layer
            "'mouth' not in KittyX.Spunk", Null(),
            "action_speed and renpy.showing('Kitty_BJ_Animation')", ConditionSwitch(
                    # If in sucking position
                    "action_speed == 1", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",  #licking
                    "(action_speed == 2 or action_speed == 5)", Null(),                          #heading
                    "action_speed == 3", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #sucking
                    "action_speed == 4", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #deepthroat
                    "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #cumming
                    ),
            "action_speed >= 5 and renpy.showing('Kitty_TJ_Animation')", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'normal'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.Mouth == 'lipbite'", "images/KittyBJFace/Kitty_BJ_Spunk_Lipbite.png",
            "KittyX.Mouth == 'kiss'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'sad'", "images/KittyBJFace/Kitty_BJ_Spunk_Kiss.png",
            "KittyX.Mouth == 'smile'", "images/KittyBJFace/Kitty_BJ_Spunk_Smile.png",
            "KittyX.Mouth == 'surprised'", "images/KittyBJFace/Kitty_BJ_Spunk_Surprised.png",
            "KittyX.Mouth == 'tongue'", "images/KittyBJFace/Kitty_BJ_Spunk_Tongue.png",
            "KittyX.Mouth == 'sucking'", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png", #fix add
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Brows
            "KittyX.Brows == 'normal'", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            "KittyX.Brows == 'angry'", "images/KittyBJFace/Kitty_BJ_Brows_Angry.png",
            "KittyX.Brows == 'sad'", "images/KittyBJFace/Kitty_BJ_Brows_Sad.png",
            "KittyX.Brows == 'surprised'", "images/KittyBJFace/Kitty_BJ_Brows_Surprised.png",
            "KittyX.Brows == 'confused'", "images/KittyBJFace/Kitty_BJ_Brows_Confused.png",
            "True", "images/KittyBJFace/Kitty_BJ_Brows_Normal.png",
            ),
        (0,0), "Kitty BJ Blink",
            #Eyes
        (0,0), ConditionSwitch(
            #cum on the face
            "'facial' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Facial.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair overlay
            "KittyX.Water or KittyX.Hair == 'wet'", "images/KittyBJFace/Kitty_BJ_Hair_Wet.png",
            "KittyX.Hair == 'long'", "images/KittyBJFace/Kitty_BJ_Hair_Long.png",
            "KittyX.Hair == 'evo'", "images/KittyBJFace/Kitty_BJ_Hair_Evo.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            #Hair water overlay
            "not KittyX.Water", Null(),
            "action_speed > 2", "images/KittyBJFace/Kitty_BJ_Wet_HeadOpen.png",
            "True", "images/KittyBJFace/Kitty_BJ_Wet_HeadClosed.png",
            ),
        (0,0), ConditionSwitch(
            #cum on the hair
            "'hair' in KittyX.Spunk", "images/KittyBJFace/Kitty_BJ_Spunk_Hair.png",
            "True", Null(),
            ),
        )
    zoom 1.4
    anchor (0.5, 0.5)

image Kitty BJ Blink:
        #eyeblinks
        ConditionSwitch(
            "KittyX.Eyes == 'normal'", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",
            "KittyX.Eyes == 'sexy'", "images/KittyBJFace/Kitty_BJ_Eyes_Sexy.png",
            "KittyX.Eyes == 'closed'", "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png",
            "KittyX.Eyes == 'surprised'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'side'", "images/KittyBJFace/Kitty_BJ_Eyes_Side.png",
            "KittyX.Eyes == 'stunned'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'down'", "images/KittyBJFace/Kitty_BJ_Eyes_Down.png",
            "KittyX.Eyes == 'manic'", "images/KittyBJFace/Kitty_BJ_Eyes_Surprised.png",
            "KittyX.Eyes == 'squint'", "images/KittyBJFace/Kitty_BJ_Eyes_Squint.png",
            "True", "images/KittyBJFace/Kitty_BJ_Eyes_Normal.png",
            ),
        choice:
            3.5
        choice:
            3.25
        choice:
            3
        "images/KittyBJFace/Kitty_BJ_Eyes_Closed.png"
        .25
        repeat

image Kitty_BJ_MouthHeading:
    #the mouth used for the heading animations
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_Sucking.png"
        zoom 1.4
        anchor (0.50,0.65)  #(0.40,0.65)

image Kitty_BJ_MouthSuckingMask:
    #the mask used for sucking animations
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        zoom 1.4
    contains: #see if this works, if not remove it
        ConditionSwitch(
            "'mouth' not in KittyX.Spunk", Null(),
            "action_speed != 2 and action_speed != 5", Null(),
            "True", "images/KittyBJFace/Kitty_BJ_Spunk_SuckingU.png",
            )
        zoom 1.4

image Kitty_BJ_MaskHeading:
    #the mask used for the heading image
    contains:
        "images/KittyBJFace/Kitty_BJ_Mouth_SuckingMask.png"
        offset (-380,-595)

image Kitty_BJ_MaskHeadingComposite:
    #The composite for the heading mask that goes over the face
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
    #The composite for the heading mask that goes over the face
    At("KittySuckingSpunk", Kitty_BJ_MouthAnim())
    zoom 1.8

image KittySuckingSpunk:
    contains:
        "images/KittyBJFace/Kitty_BJ_Spunk_SuckingO.png"
        zoom 1.4
        anchor (0.5, 0.5)

transform Kitty_BJ_MouthAnim():
        #The animation for the heading mouth
        subpixel True
        zoom 0.7 #0.90
        block: #total time 1.0 down, 1.5 back up 2.5 total
            pause .40
            easeout .40 zoom 0.69 #0.87
            linear .10 zoom 0.7 #0.9
            easein .45 zoom 0.65 #0.70
            pause .15
            #1.5s to this point
            easeout .25 zoom 0.7#0.9
            linear .10 zoom 0.69#0.87
            easein .30 zoom 0.7#0.9
            pause .35
            #1.0s to this point
            repeat
transform Kitty_BJ_MouthAnimC():
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

#Cock Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Kitty_BJ_Cock_0():
    #The angled static animation for the cock for starting
    anchor (.5,.5)
    rotate -10
transform Kitty_BJ_Cock_1():
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat
transform Kitty_BJ_Cock_2():
    #The vertical static animation for the cock used in most sucking
    anchor (.5,.5)
    rotate 0
#    alpha 0.9
#End Cock Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Head and Body Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
transform Kitty_BJ_Head_0():
    #The starting animation for her face
    subpixel True
    ease 1.5 offset (0,0)
transform Kitty_BJ_Body_0():
    #The starting animation for her body
    subpixel True
    ease 1.5 offset (0,0)


transform Kitty_BJ_Head_1():
    #The licking animation for her face
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat
transform Kitty_BJ_Body_1():
    #The licking animation for her body
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform Kitty_BJ_Head_2():
    #The heading animation for her face
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 35           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat
transform Kitty_BJ_Body_2():
    #The heading animation for her body
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 15           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat

transform Kitty_BJ_Head_3():
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50)
        repeat
transform Kitty_BJ_Body_3():
    #The sucking animation for her body
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat

transform Kitty_BJ_Head_4():
    #The deep animation for her face
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat
transform Kitty_BJ_Body_4():
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Kitty_BJ_Head_5():
    #The heading cumming animation for her face
    subpixel True
    offset (0,-30)     #top
    block:
        ease 1 yoffset -20           #bottom
        ease 1.5 offset (0,-30)     #top
        repeat
transform Kitty_BJ_Body_5():
    #The heading cumming animation for her body
    subpixel True
    offset (0,-30)     #top
    block:
        ease 1 yoffset -20           #bottom
        ease 1.5 offset (0,-30)     #top
        repeat

transform Kitty_BJ_Head_6():
    #The deep cumming animation for her face
    ease .5 offset (0,230)
    block:
        subpixel True
        ease 1 yoffset 250
        pause .5
        ease 2 yoffset 230
        repeat
transform Kitty_BJ_Body_6():
    #The deep cumming animation for her body
    ease .5 offset (0,190)
    block:
        subpixel True
        ease 1.2 yoffset 200
        pause .5
        ease 1.8 yoffset 190
        repeat


#Head and Body Animations for Kitty's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Kitty_BJ_Launch(line = primary_action):    # The sequence to launch the Kitty BJ animations
    if renpy.showing("Kitty_BJ_Animation"):
            return

    call Kitty_Hide
    if line == "L" or line == "cum":
        show Kitty_Sprite at sprite_location(StageCenter) zorder KittyX.Layer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80)
        with dissolve
    else:
        show Kitty_Sprite at sprite_location(StageCenter) zorder KittyX.Layer:
            alpha 1
            zoom 2.5 offset (150,80)
        with dissolve

    if line == "L":
            if Taboo:
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                    elif Present[1] != KittyX:
                            "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
                else:
                            "[KittyX.name] casually glances around to see if anyone can see her."
            if not KittyX.Blow:
                "[KittyX.name] hesitantly kneels down and touches her mouth to your cock."
            else:
                "[KittyX.name] kneels down and begins to suck on your cock."

    $ action_speed = 0

    if line != "cum":
        $ primary_action = "blowjob"

    show Kitty_Sprite zorder KittyX.Layer:
        alpha 0
    show Kitty_BJ_Animation zorder 150:
        pos (645,510)
    return

label Kitty_BJ_Reset: # The sequence to the Kitty animations from BJ to default
    if not renpy.showing("Kitty_BJ_Animation"):
            return
    call Kitty_Hide
    $ action_speed = 0

    show Kitty_Sprite at sprite_location(StageCenter) zorder KittyX.Layer:
        alpha 1
        zoom 2.5 offset (150,80)
    with dissolve

    show Kitty_Sprite zorder KittyX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)
    show Kitty_Sprite at sprite_location(KittyX.sprite_location) zorder KittyX.Layer:
        alpha 1
        zoom 1 offset (0,0)

    return

# End Kitty Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Kitty TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty TJ annimation element ///////////////////////////////////////////////////////////////////////////                                     Core Kitty BJ element

image Kitty_TJ_Animation:
    #core titjob animation
    contains:
        ConditionSwitch(
            # Kitty's upper body
            "Player.Sprite", ConditionSwitch(
                    # If during sex
                    "action_speed == 1", "Kitty_TJ_Body_1",#slow
                    "action_speed == 2", "Kitty_TJ_Body_2",#fast
                    "action_speed == 3", "Kitty_TJ_Body_3",#licking
                    "action_speed >= 5", "Kitty_TJ_Body_5",#cumming
                    "True",       "Kitty_TJ_Body_0",#Static
                    ),
            "True","Kitty_TJ_Body_0",#Static
            )
    zoom 1.35 #0.8
    anchor (.5,.5)
    pos (600,605) #(600,705)#height for bj


image Kitty_TJ_Torso:
    # Her torso for the sex, BJ, and TJ poses
    contains:
            #body
            "images/KittyBJFace/Kitty_TJ_Body.png"
#    contains:
#            #chest clothing under layer for TJs
#            ConditionSwitch(
#                "not renpy.showing('Kitty_TJ_Animation')", Null(),   # KittyX.TitsUp = 0
#                "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_TJU.png",
#                "True", Null(),
#                )
#    contains:
#            # Chest clothing layer
#        ConditionSwitch(
#            "not KittyX.Chest or renpy.showing('Kitty_TJ_Animation')", Null(),   # KittyX.TitsUp = 0
#            "KittyX.Chest == 'corset'", "images/KittySex/Kitty_Sex_Bra_Corset_Up.png",   # KittyX.TitsUp = 1
#            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_Up.png",   # KittyX.TitsUp = 1
#            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Bra_Lace_Up.png",   # KittyX.TitsUp = 1
#            "True", Null(),   # KittyX.TitsUp = 0
#            )
#    contains:
#            # Over clothing layer
#        ConditionSwitch(
#            "KittyX.Over == 'jacket'", ConditionSwitch(
#                    #if it's the ring pericings
#                    "renpy.showing('Kitty_TJ_Animation')", Null(),
##                    "renpy.showing('Kitty_TJ_Animation')", "images/KittySex/Kitty_Sex_Jacket_Down.png",
#                    "KittyX.Chest == 'corset'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # KittyX.TitsUp = 1
#                    "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # KittyX.TitsUp = 1
#                    "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Jacket_Up.png",   # KittyX.TitsUp = 1
#                    "True", "images/KittySex/Kitty_Sex_Jacket_Down.png",   # KittyX.TitsUp = 0
#                    ),
#            "KittyX.Over == 'nighty'", ConditionSwitch(
#                    #if she has the nighty on
#                    "renpy.showing('Kitty_TJ_Animation')", Null(),
#                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Sex_Nighty_Up.png",
#                    "True", "images/KittySex/Kitty_Sex_Nighty_Down.png",
#                    ),
#            "True", Null(),
#            )
#    contains:
#            # spunk on tits
#            ConditionSwitch(
#                "'tits' not in KittyX.Spunk", Null(),
#                "renpy.showing('Kitty_TJ_Animation')", "images/KittySex/Kitty_Spunk_Titjob_Under.png",
#                "True", "images/KittySex/Kitty_Spunk_Tits.png",
#                )

image Kitty_TJ_Arms:
    # Her arms for the TJ poses
    contains:
            #body
            "images/KittyBJFace/Kitty_TJ_Arms.png"

image Kitty_TJ_Tits:
    #core titjob breasts
    contains:
            #base layer
#            "images/KittyBJFace/Kitty_TJ_Tits.png"
        ConditionSwitch(
            "Player.Sprite and action_speed", "images/KittyBJFace/Kitty_TJ_Tits_Smooshed.png",
            "True", "images/KittyBJFace/Kitty_TJ_Tits.png",
            )
#    contains:
#            # piercings
#        ConditionSwitch(
#            "not KittyX.Pierce", Null(),
#            "KittyX.Pierce == 'barbell'", ConditionSwitch(
#                    #if it's the ring pericings
##                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),
#                    "True", "images/KittySex/Kitty_Pierce_Barbell_Tits_T.png",
#                    ),
#            "KittyX.Pierce == 'ring'", ConditionSwitch(
#                    #if it's the ring pericings
##                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", Null(),
#                    "True", "images/KittySex/Kitty_Pierce_Ring_Tits_T.png",
#                    ),
#            "True", Null(),
#            )
#    contains:
#            #chest clothing layer
#        ConditionSwitch(
#            "not KittyX.Chest", Null(),   # KittyX.TitsUp = 0
#            "KittyX.Chest == 'sports bra'", "images/KittySex/Kitty_Sex_Bra_Sports_TJ.png",   # KittyX.TitsUp = 1
#            "KittyX.Chest == 'lace bra'", "images/KittySex/Kitty_Sex_Bra_Lace_TJ.png",   # KittyX.TitsUp = 1
#            "True", Null(),   # KittyX.TitsUp = 0
#            )
#    contains:
#            # piercings over clothes
#        ConditionSwitch(
#            "not KittyX.Pierce or not KittyX.Chest", Null(),
#            "KittyX.Pierce == 'barbell'", ConditionSwitch(
#                    #if it's the ring pericings
#                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Pierce_Barbell_Tits_TC.png",
#                    "True", Null(),
#                    ),
#            "KittyX.Pierce == 'ring'", ConditionSwitch(
#                    #if it's the ring pericings
#                    "KittyX.Chest in ('corset', 'lace bra', 'sports bra')", "images/KittySex/Kitty_Pierce_Ring_Tits_TC.png",
#                    "True", Null(),
#                    ),
#            "True", Null(),
#            )
#    contains:
#            # spunk on tits
#        ConditionSwitch(
#                "'tits' in KittyX.Spunk", "images/KittySex/Kitty_Spunk_Titjob_Over.png",
#                "True", Null(),
#                )


#image Kitty_TJ_MaskA:
#    #Test mask for showing her moving chest
#    contains:
##        Solid("#159457", xysize=(750,750))
#        "images/KittyBJFace/Kitty_TJ_Mask.png"

image Kitty_Mega_Mask:
    # giant green brick for use in finding where a mask is
    contains:
        Solid("#159457", xysize=(1750,1750))
        alpha .5


#  TJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Kitty_TJ_Body_0:
        #Her Body in the TJ pose, idle
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease 2.4 ypos 250 #top
                    ease 1.6 ypos 260 #bottom
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"
                pos (545,330)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat
        contains:
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease 2.4 ypos 250 #top
                    ease 1.6 ypos 260 #bottom
                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.4 ypos 325 #top
                    ease 1.6 ypos 330 #bottom
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
                    "Player.Sprite", "Blowcock",
                    "True", Null(),
                    )
                subpixel True
                pos (640,150) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4
#End TJ animation action_speed 0


image Kitty_TJ_Mask_1:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,60) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.9 ypos -40 #top 280
                ease 1 ypos 60 #bottom 330
                pause .1
                repeat

image Kitty_TJ_Body_1:
        #Her Body in the TJ pose, slow 1
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease 3 ypos 210 #top
                    ease 1 ypos 260 #bottom
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"
                pos (545,330)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.8 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .2
                    repeat
        contains:
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.85 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .15
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease 2.9 ypos 210 #top
                    ease 1 ypos 260 #bottom
                    pause .1
                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.9 ypos 280 #top
                    ease 1 ypos 330 #bottom
                    pause .1
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_1"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4
                block:
                    ease 2.8 ypos 490 #top
                    ease .8 ypos 500 #bottom
                    pause .4
                    repeat
#End TJ animation action_speed 1


image Kitty_TJ_Mask_2:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,60) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease .71 ypos -15 #top 280
                ease .27 ypos 60 #bottom 330
                pause .02
                repeat

image Kitty_TJ_Body_2:
        #Her Body in the TJ pose, fast 2
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #505
                subpixel True
                block:
                    ease .7 ypos 215 #top
                    ease .25 ypos 260 #bottom
                    pause .05
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"
                pos (545,330)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .65 ypos 285 #top
                    ease .25 ypos 330 #bottom
                    pause .1
                    repeat
        contains:
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .68 ypos 285 #top
                    ease .25 ypos 330 #bottom
                    pause .07
                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,330)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease .71 ypos 290 #top
                    ease .27 ypos 330 #bottom
                    pause .02
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (505,260) #bottom  #280
                subpixel True
                block:
                    ease .68 ypos 215 #top
                    ease .25 ypos 260 #bottom
                    pause .07
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_2"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4
                block:
                    ease .72 ypos 490 #top
                    ease .27 ypos 500 #bottom
                    pause .01
                    repeat
#End TJ animation action_speed 2


image Kitty_TJ_Mask_3:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,140) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.2 ypos 90 #top 280
                ease .6 ypos 140 #bottom 330
                pause .2
                repeat

image Kitty_TJ_Body_3:
        #Her Body in the TJ pose, licking 3
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,260) #bottom  #505
                rotate 0
                subpixel True
                parallel:
                    block:
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom
                        pause .4
                        repeat 2
                    block:
                        #left tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (520,320) #bottom
                        ease 2.2 pos (510,290) #top
                        ease .8 pos (520,320) #bottom
                    block:
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom
                        pause .4
                        repeat 2
                    block:
                        #right tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (475,320) #bottom
                        ease 2.2 pos (490,290) #top
                        ease .8 pos (475,320) #bottom
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"
                pos (545,360)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat
        contains:
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"
                pos (545,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 340 #top
                    ease .6 ypos 360 #bottom
                    pause .2
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,310) #bottom  #505
                subpixel True
                rotate 0
                parallel:
                    block:
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom
                        pause .4
                        repeat 2
                    block:
                        #left tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (520,320) #bottom
                        ease 2.2 pos (510,290) #top
                        ease .8 pos (520,320) #bottom
                    block:
                        #un tilted loop
                        ease 2 pos (500,290) #top
                        ease .6 pos (500,315) #bottom
                        pause .4
                        repeat 2
                    block:
                        #right tilted loop
                        ease 2.2 pos (500,290) #top
                        ease .8 pos (475,320) #bottom
                        ease 2.2 pos (490,290) #top
                        ease .8 pos (475,320) #bottom
                    repeat
                parallel:
                    block:
                        #un tilted loop
                        ease 2.2 rotate 0  #top
                        pause 3.8 #bottom
                    block:
                        #left tilted loop
                        ease 2.2 rotate 0   #top
                        ease .8 rotate 10   #bottom
                        ease 2.2 rotate 0   #top
                        ease .8 rotate 5   #bottom
                    block:
                        #un tilted loop
                        ease 2.2 rotate 0  #top
                        pause 3.8 #bottom
                    block:
                        #right tilted loop
                        ease 2.2 rotate 0   #top
                        ease .8 rotate -10   #bottom
                        ease 2.2 rotate 0   #top
                        ease .8 rotate -5   #bottom
                    repeat
        contains:
                #zero's cock
                ConditionSwitch(
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_3"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4
#End TJ animation action_speed 3


image Kitty_TJ_Mask_5:
        contains:
            "images/KittyBJFace/Kitty_TJ_Mask.png"
            pos (100,140) #bottom #pos (545,330)
            anchor (0.5, 0.5)
            zoom 1.4           #temp
            subpixel True
            block:
                ease 2.2 ypos 120 #top 280 #90
                ease 1.6 ypos 140 #bottom 330
                pause .2
                repeat

image Kitty_TJ_Body_5:
        #Her Body in the TJ pose, cumming 5
        contains:
                #Hair underlay
                "Kitty_BJ_HairBack"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,260) #bottom  #505
                rotate 0
                subpixel True
                block:
                    #un tilted loop
                    ease 2 pos (500,304) #top 280
                    ease 1.6 pos (500,307) #bottom 315
                    pause .4
                    repeat
        contains:
                #base body
                "Kitty_TJ_Torso"#"images/KittyBJFace/Kitty_TJ_Body.png"
                pos (545,360)#(500,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat
        contains:
                #arms
                "Kitty_TJ_Arms"#"images/KittyBJFace/Kitty_TJ_Arms.png"
                pos (545,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat
        contains:
                #head
                "Kitty_BJ_Head"
                zoom 0.41
                anchor (0.5, 0.5)
                pos (500,307) #bottom  #505
                subpixel True
                rotate 0
                block:
                    #un tilted loop
                    ease 2 pos (500,304) #top 280
                    ease 1.6 pos (500,307) #bottom 315
                    pause .4
                    repeat
        contains:
                #tits underlayer
                "Kitty_TJ_Tits"
                pos (545,360)#pos (0,0) #bottom
                anchor (0.5, 0.5)
                zoom 0.55           #temp
                subpixel True
                block:
                    ease 2.2 ypos 350 #top
                    ease 1.6 ypos 360 #bottom
                    pause .2
                    repeat
    #    contains:
    #            #tits underlayer
    #            "Kitty_TJ_MaskA"
    #            pos (545,360)#pos (0,0) #bottom
    #            anchor (0.5, 0.5)
    #            zoom 0.55           #temp
    #            subpixel True
    #            block:
    #                ease 2.2 ypos 350 #top
    #                ease 1.6 ypos 360 #bottom
    #                pause .2
    #                repeat
        contains:
                #zero's cock
                ConditionSwitch(
    #                "Player.Sprite", AlphaMask("Kitty_Mega_Mask", "Kitty_TJ_Mask_5"),
                    "Player.Sprite", AlphaMask("Blowcock", "Kitty_TJ_Mask_5"),
    #                "Player.Sprite", AlphaMask("Blowcock", "Kitty_Mega_Mask"),
                    "True", Null(),
                    )
                subpixel True
                pos (665,500) #bottom #150
                anchor (0.5,0.5)
                zoom 0.4

    #    contains:
    #            #zero's cock
    #            ConditionSwitch(
    #                "Player.Sprite", "Blowcock",
    #                "True", Null(),
    #                )
    #            subpixel True
    #            alpha 0.2
    #            pos (640,150) #bottom #150
    #            anchor (0.5,0.5)
    #            zoom 0.4
    #    contains:
    #            #tits
    #            "Kitty_Tits_Mask"
    #            pos (545,360)#pos (0,0) #bottom
    #            anchor (0.5, 0.5)
    #            zoom 0.55           #temp
    #            subpixel True
    #            block:
    #                ease 2.2 ypos 340 #top
    #                ease .6 ypos 360 #bottom
    #                pause .2
    #                repeat
#End TJ animation action_speed 5 (cumming)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


label Kitty_TJ_Launch(line = primary_action):    # The sequence to launch the Kitty Titfuck animations
    if renpy.showing("Kitty_TJ_Animation"):
        return
    call Kitty_Hide
    show Kitty_Sprite at sprite_location(KittyX.sprite_location) zorder KittyX.Layer:
        alpha 1
        ease 1 zoom 2 xpos 700 yoffset 50 #offset (-100,50)
    if line == "L" and Taboo:
                if len(Present) >= 2:
                    if Present[0] != KittyX:
                            "[KittyX.name] looks back at [Present[0].name] to see if she's watching."
                    elif Present[1] != KittyX:
                            "[KittyX.name] looks back at [Present[1].name] to see if she's watching."
                else:
                            "[KittyX.name] casually glances around to see if anyone can see her."
    if KittyX.Chest and KittyX.Over:
        "She throws off her [KittyX.Over] and her [KittyX.Chest]."
    elif KittyX.Over:
        "She throws off her [KittyX.Over], baring her breasts underneath."
    elif KittyX.Chest:
        "She tugs off her [KittyX.Chest] and throws it aside."
    $ KittyX.Over = 0
    $ KittyX.Chest = 0
    $ KittyX.ArmPose = 0
    call Kitty_First_Topless      #restore if topless
    if line == "L":
            if not KittyX.Tit:
                "She hesitantly presses your cock against her chest."
            else:
                "She squeezes her breasts around your cock."


    show blackscreen onlayer black with dissolve
    show Kitty_Sprite zorder KittyX.Layer:
        alpha 0
    $ action_speed = 0
    if line != "cum":
        $ primary_action = "titjob"
    show Kitty_TJ_Animation zorder 150
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return

# End Kitty TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






# Start Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Kitty Handjob element //////////////////////////////////////////////////////////////////////                                         Core Kitty HJ element

#image Zero_Handcock:
#    contains:
#        ConditionSwitch(    # Zero cock sucking
#            "Player.Color == 'pink'", "images/RogueBJFace/handcock_P.png",
#            "Player.Color == 'brown'", "images/RogueBJFace/handcock_B.png",
#            "Player.Color == 'green'", "images/RogueBJFace/handcock_G.png",
#            "Player.Color != 'pink'", Null(),
#            ),
#    anchor (0.5,1.0)  #1.0
#    pos (200,400)#(200,400)

image Kitty_Hand_Under:
    "images/KittySprite/handkitty2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Kitty_Hand_Over:
    "images/KittySprite/handkitty1.png"
    anchor (0.5,0.5)
    pos (0,0)

#transform Handcock_1():
#    subpixel True
#    rotate_pad False
#    ease .5 ypos 450 rotate -2 #450
#    pause 0.25
#    ease 1.0 ypos 400 rotate 0 #400
#    pause 0.1
#    repeat

#transform Handcock_2():
#    subpixel True
#    rotate_pad False
#    ease .2 ypos 430 rotate -3 #410
#    ease .5 ypos 400 rotate 0
#    pause 0.1
#    repeat

transform Kitty_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
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
        ConditionSwitch(                                                # backside of the hand
            "not action_speed", Transform("Kitty_Hand_Under"),
            "action_speed == 1", At("Kitty_Hand_Under", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_Hand_Under", Kitty_Hand_2()),
            "action_speed", Null(),
            ),
    contains:
        ConditionSwitch(                                                # cock
            "not action_speed", Transform("Zero_Handcock"),
            "action_speed == 1", At("Zero_Handcock", Handcock_1()),
            "action_speed >= 2", At("Zero_Handcock", Handcock_2()),
            "action_speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not action_speed", Transform("Kitty_Hand_Over"),
            "action_speed == 1", At("Kitty_Hand_Over", Kitty_Hand_1()),
            "action_speed >= 2", At("Kitty_Hand_Over", Kitty_Hand_2()),
            "action_speed", Null(),
            ),
    anchor (0.51, -1.3)
    zoom 0.4#0.6


label Kitty_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Kitty_HJ_Animation"):
            return
    $ action_speed = 0
    hide Kitty_HJ_Animation with easeoutbottom
    call Kitty_Hide
    show Kitty_Sprite at sprite_location(KittyX.sprite_location) zorder KittyX.Layer:
            alpha 1
            zoom 1.7 offset (-50,200)
    show Kitty_Sprite at sprite_location(KittyX.sprite_location) zorder KittyX.Layer:
            alpha 1
            ease 1 zoom 1.5 offset (-150,50)
            pause .5
            ease .5 zoom 1 offset (0,0)
    show Kitty_Sprite at sprite_location(KittyX.sprite_location) zorder KittyX.Layer:
            alpha 1
            zoom 1 offset (0,0)
    return

label Kitty_Middle_Launch(T = primary_action,Set=1):
    call Kitty_Hide
    $ primary_action = T
    $ KittyX.Pose = "mid" if Set else KittyX.Pose
    show Kitty_Sprite at sprite_location(KittyX.sprite_location) zorder KittyX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return

label Kitty_ThreewayBreasts_Launch:
        show Kitty_Sprite at sprite_location(KittyX.sprite_location) zorder KittyX.Layer:
    #      ease 0.5 pos (800,200) zoom 1.3
            ease 0.5 pos (700,200) xzoom -1.5 yzoom 1.5
        $ KittyX.ArmPose = 1
        return


# End Kitty Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






# Start Kitty Fondling Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (215,420)#(300,420)230
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
        pos (120,410)#(180,410) 150
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block:
            ease 1 rotate -30
            ease 1 rotate -60
            repeat

#image GropeBreast:
image LickRightBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (95,370)
            pause .5
            ease 1.5 rotate 30 pos (115,400)
            repeat

image LickLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5
        xzoom -0.45
        pos (200,410) #(115,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block:
            ease .5 rotate -40 pos (190,380)#(95,370)
            pause .5
            ease 1.5 rotate 30 pos (200,410)#(115,400)
            repeat

image GropeThigh_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (200,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        parallel:
            pause .5
            ease 1 ypos 780
            ease 1 ypos 720
            repeat
        parallel:
            pause .5
            ease 1 rotate 110 xpos 180
            ease 1 rotate 100 xpos 200
            repeat

image GropePussy_Kitty:
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (210,640)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice:
                ease .5 rotate 190 pos (210,625)
                ease .75 rotate 170 pos (210,640)
            choice:
                ease .5 rotate 190 pos (210,625)
                pause .25
                ease 1 rotate 170 pos (210,640)
            repeat

image FingerPussy_Kitty:
    contains:
        subpixel True
        "UI_Finger"
        zoom 0.65
        pos (220,730)#(230,720)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice:
                ease 1 rotate 40 pos (230,695)#(240,685)
                pause .5
                ease 1 rotate 50 pos (220,730)  #(230,720)
            choice:
                ease .5 rotate 40 pos (230,695)
                pause .5
                ease 1.75 rotate 50 pos (220,730)
            choice:
                ease 2 rotate 40 pos (230,695)
                pause .5
                ease 1 rotate 50 pos (220,730)
            choice:
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730)
                ease .25 rotate 40 pos (230,695)
                ease .25 rotate 50 pos (220,730)
            repeat

image Lickpussy_Kitty:
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45
        xzoom -0.45
        pos (240,680)#(250,670)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block:
            easeout .5 rotate -50 pos (220,660) #(230,650)
            linear .5 rotate -60 pos (210,670) #(220,660)
            easein 1 rotate 10 pos (240,680) #(250,670)
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
            pause .25
            ease 1 rotate 55 ypos 380
            pause .25
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
            pause .25
            ease 1 rotate 55 ypos 400
            pause .25
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
            pause .25
            ease 1 rotate 70 xpos 240 ypos 665
            pause .25
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
            pause .25
            ease 1 rotate 10 xpos 270 ypos 665
            pause .25
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



#Lesbian action animations.
image GirlGropeLeftBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (240,400)#(300,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -20
        block:
            ease 1 rotate -40 pos (230,390)#(280,390)
            ease 1 rotate -20 pos (240,400)
            repeat

image GirlGropeRightBreast_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (110,380) #(160,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block:
            ease 1 rotate -30 pos (110,410)#(160,410)
            ease 1 rotate -10 pos (110,380)
            repeat

image GirlGropeThigh_Kitty:
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

image GirlGropePussy_Kitty:
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (210,625)#(230,615)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (215,640)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (215,640)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
#                ease .5 rotate 205 pos (225,620)
#                ease .75 rotate 200 pos (225,625)
                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
                ease .5 rotate 205 pos (215,640)
                ease .75 rotate 200 pos (215,645)
            choice: #Fast stroke
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
                ease .3 rotate 205 pos (215,640)
                ease .3 rotate 200 pos (215,650)
            repeat

image GirlFingerPussy_Kitty:
    contains:
        subpixel True
        "UI_GirlFinger"
        zoom .6
        pos (220,640)#(220,635)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (220,645)
                ease .5 rotate 195
                ease .75 rotate 210
                ease .5 rotate 195
            choice: #slow rub
                ease .5 rotate 210 pos (220,645)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
                ease .5 rotate 205 pos (220,655)
                ease .75 rotate 200 pos (220,660)
            choice: #Fast stroke
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
                ease .3 rotate 205 pos (220,655)
                ease .3 rotate 200 pos (220,665)
            repeat
