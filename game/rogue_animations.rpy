image Rogue_Pussy_Mask:
    #AlphaMask used to prevent the cock from moving past the pussy
    #Called in "Rogue_Pussy_Moving"
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

image Rogue_Pussy_Mask_Static:
    #AlphaMask used to prevent the cock from moving past the pussy in static pose
    #Called in "Rogue_Pussy_Moving"
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

image Rogue_Pussy_Static:
    #Full Animation for speed 0
    subpixel True
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518)
        xzoom 1
    contains:
        #moving hole
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
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
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:
        #Cock
        AlphaMask("Zero_Doggy_Static", "Rogue_Pussy_Mask_Static")

    contains:
        # expanding pussy flap
        AlphaMask("Rogue_PussyHole_Static", "Rogue_Pussy_Hole_Mask_Static")

image Rogue_Pussy_Hole_Mask_Static:
    # This is the alpha used for the little flap in the heading animation "Rogue_Pussy_Moving"
    contains:
        #Base
        AlphaMask("images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom .65
            pause 1
            ease 3 xzoom .6
            repeat

image Rogue_PussyHole_Static:
    #This is the image impacted by the mask for the pussy flap in "Rogue_Pussy_Moving"
    contains:
        #Mask
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 512
            pause 1
            ease 3 ypos 515
            repeat


image Rogue_Pussy_Heading:
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
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
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:
        #Cock
        AlphaMask("Zero_Doggy_Heading", "Rogue_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")


image Rogue_Pussy_Hole_Mask:
    # This is the alpha used for the little flap in the heading animation "Rogue_Pussy_Heading"
    contains:
        #Base
        AlphaMask("images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png", "images/RogueDoggy/Rogue_Doggy_SexMask.png")
        subpixel True
        anchor (0.52,0.69)
        pos (217,518)
        xzoom .6
        block:
            ease 1 xzoom 1
            pause 1
            ease 3 xzoom .6
            repeat

image Rogue_Pussy_Heading_Flap:
    #This is the image impacted by the mask for the pussy flap in "Rogue_Pussy_Heading"
    contains:
        #Mask
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHeading.png"
        anchor (0.52,0.69)
        pos (217,515)
        zoom 1
        alpha .9
        block:
            ease 1 ypos 505
            pause 1
            ease 3 ypos 515
            repeat


image Rogue_Pussy_Fingering:
    #Full Animation for speed 1
    subpixel True
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
        anchor (0.52,0.69)
        pos (220,518) # fix this back once re-exported(217,518)
        xzoom 1
    contains:
        #moving hole
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
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
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:
        #Cock
        AlphaMask("Zero_Pussy_Finger", "Rogue_Pussy_Mask")

    contains:
        # expanding pussy flap
        AlphaMask("Rogue_Pussy_Heading_Flap", "Rogue_Pussy_Hole_Mask")

# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

image Rogue_Pussy_Fucking2:
    #Full Animation for speed 2
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:
        #Cock
#        AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png")

        #Cock
        ConditionSwitch(
            "Trigger == 'dildo pussy'", AlphaMask("Rogue_Doggy_Fucking_Dildo", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            "True",AlphaMask("Zero_Doggy_Fucking2", "images/RogueDoggy/Rogue_Doggy_SexMask.png"),
            ),


image Rogue_Pussy_Fucking3:
    #Full Animation for speed 3
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Pussy_FHole.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:
        #Cock
        AlphaMask("Zero_Doggy_Fucking3", "images/RogueDoggy/Rogue_Doggy_SexMask.png")

image Rogue_Doggy_Fucking_Dildo:
    #Animation for speed 2 Cock
    contains:
        "images/DildoIn.png"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

image Rogue_Anal:
    #Anal static Loose
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Asshole_Loose.png"
        anchor (0.50,0.69)
        pos (208,500)
        zoom 1.25
    contains:
        ConditionSwitch(
            #full hose/tights
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        "Zero_Doggy_Insert"
        pos (172,500)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Rogue_Anal_Fingering:
    #Animation for speed 1
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
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
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
#    contains:
#        #Cock masking fixer (for when the bottom part tries to cut off)
#        AlphaMask("Zero_Doggy_Anal_Finger", "Zero_Doggy_Anal_HeadingJunk")
    contains:
        #Cock with mask
        AlphaMask("Zero_Doggy_Anal_Finger", "Rogue_Doggy_Anal_Fingering_Mask")

image Zero_Doggy_Anal_Finger:
        #the cock anal heading animation
    contains:
        "images/UI_Fingering.png",
        pos (172,480)#500
        block:
            ease .5 ypos 460#450
            pause .25
            ease 1.75 ypos 480#500
            repeat

image Rogue_Doggy_Anal_Fingering_Mask:
    #the masking animation for the anal heading
    contains:
        "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"
#        yoffset 10
        anchor (0.52,0.69)
        pos (218,518)
        zoom .6
        block:
            ease .5 zoom .75
            pause .5
            ease 1.5 zoom .6
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Rogue_Anal_Heading:
    #Animation for speed 1
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
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
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock masking fixer (for when the bottom part tries to cut off)
        AlphaMask("Zero_Doggy_Anal_Heading", "Zero_Doggy_Anal_HeadingJunk")
    contains:
        #Cock with mask
        AlphaMask("Zero_Doggy_Anal_Heading", "Rogue_Doggy_Anal_Heading_Mask")

image Rogue_Doggy_Anal_Heading_Mask:
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

image Rogue_Doggy_Anal_Head_Top:
#animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 0
        block:
            pause .4
            ease .3 ypos -5
            easeout 1 ypos 0
            pause .8
            repeat

image Rogue_Doggy_Anal_Head_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -10
            easeout .1 ypos -7
            easein .9 ypos 0
            pause .9
            repeat

image Rogue_Anal_Fucking:
    #Animation for speed 2 Ass
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
    contains:
        #Cheeks
        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            ),
    contains:
        #Cock
        ConditionSwitch(
            #full hose/tights
            "Trigger == 'dildo anal'", AlphaMask("Rogue_Doggy_Anal_Dildo", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            "True", AlphaMask("Zero_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png"),
            ),

image Rogue_Doggy_Anal_Dildo:
    #Animation for speed 2 Cock
    contains:
        "images/DildoIn.png"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat


image Rogue_Doggy_Anal_FullMask:
    contains:
        #Mask
        "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png"
    contains:
        #Cheeks
        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )

image Rogue_Doggy_Fuck_Top:
    #animation for anal fucking top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 15#28
        pause .4
        block:
            ease .2 ypos 5#10
            pause .3
            ease 2 ypos 15#28
            repeat

image Rogue_Doggy_Fuck_Ass:
    #animation for anal fucking ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
        ypos 0
        block:
            pause .4
            ease .2 ypos -15#-25
            ease .1 ypos -5#-15
            pause .2
            ease 1.6 ypos 0
            repeat

image Rogue_Anal_Fucking2:
    #Animation for speed 3 Ass
    contains:
        #Base
        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
    contains:
        #Hole
        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
#    contains:
#        #Mask
#        "images/RogueDoggy/Rogue_Doggy_Anal_FullMask.png"
    contains:
        #Cheeks
        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
    contains:
        ConditionSwitch(
            #full hose/tights
            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
            "RogueX.Panties and RogueX.PantiesDown", Null(),
            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
            "True", Null(),
            )
    contains:
        #Cock
        AlphaMask("Zero_Doggy_Anal2", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")

image Rogue_Doggy_Fuck2_Top:
    #animation for anal fucking2 top half
    contains:
        subpixel True
        "Rogue_Doggy_Body"
        ypos 20
        block:
            pause .15
            ease .1 ypos 0
            pause .1
            easein .5 ypos 20
            pause .05
            repeat

image Rogue_Doggy_Fuck2_Ass:
    #animation for anal fucking2 ass half
    contains:
        subpixel True
        "Rogue_Doggy_Ass"
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

image Rogue_Doggy_Feet0:
    #static animation
    contains:
        "Rogue_Doggy_Shins"
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
        pos (145,480)
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            subpixel True
            pause .5
            ease 2 ypos 20
            pause .5
            ease 2 ypos 0
            repeat

image Rogue_Doggy_Feet1:
    #slow animation
    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .4
            ease 1.7 ypos 500
            ease .9 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .3
            ease 1.7 ypos 100
            ease 1 ypos 0
            repeat

image Rogue_Doggy_Feet2:
    #fast animation
    contains:
        "Rogue_Doggy_Shins"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
    contains:
        "Zero_Doggy_Up"
        zoom 1.2
        pos (145,480)
        block:
            pause .07
            ease .6 ypos 500
            ease .28 ypos 480
            repeat
    contains:
        "Rogue_Doggy_Feet"
        pos (0, 0) #(0,0) top
        block:
            pause .05
            ease .6 ypos 110
            ease .3 ypos 0
            repeat
# Footjob animations end > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>             UI Tool animations



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Doggy Launch/Reset
label Rogue_Doggy_Launch(Line = Trigger):
    if renpy.showing("Rogue_Doggy_Animation"):
        return
    $ Speed = 0
    call hide_girl(RogueX, sprite = True)
    show Rogue_Doggy_Animation at sprite_location(StageCenter+50) zorder 150
    with dissolve
    return

label Rogue_Doggy_Reset:
    if not renpy.showing("Rogue_Doggy_Animation"):
        return
#    $ Trigger = 0               #fix, not sure this is a good idea
    $ RogueX.ArmPose = 2
    $ RogueX.SpriteVer = 0
    hide Rogue_Doggy_Animation
    call hide_girl(RogueX)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
                    alpha 1
                    zoom 1
                    offset (0,0)
                    anchor (0.6, 0.0)
    with dissolve
    $ Speed = 0
    return





# Rogue Sex Sprite ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#Start Animations for Rogue's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Rogue_Sex_Pussy_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "images/RogueSex/Rogue_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim0", "Rogue_Pussy_Open_Mask")

image Rogue_Sex_Pussy_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "images/RogueSex/Rogue_Sex_Pussy_Open.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim1", "Rogue_Pussy_Open_Mask")

image Rogue_Sex_Pussy_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/RogueSex/Rogue_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim2", "Rogue_Pussy_Fucking_Mask")

image Rogue_Sex_Pussy_Fucking3:  #rename this to 3
    # This is the visual for her pussy during the Speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/RogueSex/Rogue_Sex_Pussy_Fucking.png"
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "True", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                ),
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Sex_Zero_Anim3", "Rogue_Pussy_Fucking_Mask")

image Rogue_Pussy_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Pussy_Mask.png"

image Rogue_Pussy_Open_Mask:
        #This is the mask image for Rogue's wide open pussy
        contains:
            "images/RogueSex/Rogue_Sex_Pussy_Mask.png"
            yoffset 3

image Rogue_Sex_Pussy_Spunk_Heading:
    "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.8

image Rogue_Sex_Pussy:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                "Trigger == 'dildo pussy'", "images/RogueSex/Rogue_Sex_Pussy_Fucking.png",
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "images/RogueSex/Rogue_Sex_Pussy_Open.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_Closed.png",
                )
    contains:
            # The background plate of her pussy
            ConditionSwitch(
                "not RogueX.Wet", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/KittySex/Kitty_Sex_WetPussy_F.png",
                "True", "images/KittySex/Kitty_Sex_WetPussy_C.png",
                )
    contains:
            #ring piercing
            ConditionSwitch(
                "RogueX.Pierce != 'ring'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Ring.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_RingF.png",
                )
    contains:
            #barbell piercing
            ConditionSwitch(
                "RogueX.Pierce != 'barbell'", Null(),
                "not Player.Sprite or Player.Cock != 'in' or Speed <= 1", "images/RogueSex/Rogue_Sex_Pussy_Barbell.png",
                "True", "images/RogueSex/Rogue_Sex_Pussy_BarbellF.png",
                )
    contains:
            # pubes
            ConditionSwitch(
                "not RogueX.Pubes", Null(),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                "Player.Sprite and Player.Cock == 'in' and Speed", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                "Player.Sprite and Player.Cock == 'in'", "images/RogueSex/Rogue_Sex_Pubes_Closed.png",
                "Trigger == 'lick pussy' or Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", "images/RogueSex/Rogue_Sex_Pubes_Open.png",
                "Trigger == 'dildo pussy'", "images/RogueSex/Rogue_Sex_Pubes_Fucking.png",
                "True", "images/RogueSex/Rogue_Sex_Pubes_Closed.png",
                )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'in' in RogueX.Spunk", "images/KittySex/Kitty_Sex_Spunk_Puss_Under.png",
                "True", Null(),
                )
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            ConditionSwitch(
                "Player.Sprite and Player.Cock == 'in' and Speed >= 3", AlphaMask("Rogue_Sex_Zero_Anim3", "Rogue_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed >= 2", AlphaMask("Rogue_Sex_Zero_Anim2", "Rogue_Pussy_Fucking_Mask"),
                "Player.Sprite and Player.Cock == 'in' and Speed", AlphaMask("Rogue_Sex_Zero_Anim1", "Rogue_Pussy_Open_Mask"),
                "Player.Sprite and Player.Cock == 'in'", AlphaMask("Rogue_Sex_Zero_Anim0", "Rogue_Pussy_Open_Mask"),
                "Trigger == 'fondle pussy' or Trigger2 == 'fondle pussy'", AlphaMask("Rogue_Sex_FingerP_Anim1", "Rogue_Pussy_Open_Mask"),
                "Trigger == 'dildo pussy'", AlphaMask("Rogue_Sex_Dildo_Anim2", "Rogue_Pussy_Fucking_Mask"),
                "True", Null(),
                )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'in' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'in' or not Speed", Null(),
                "Speed <= 1", "Rogue_Sex_Pussy_Spunk_Heading",
                "True", "images/KittySex/Kitty_Sex_Spunk_Puss_Over.png",
                )

    #End Rogue Pussy composite

#End Animations for Rogue's Pussy during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Legs_Anim1:
        #this is the animation for Rogue's lower body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .25
                easein 1 pos (0,-5)
                pause 1
                ease 2.75 pos (0,0)
                repeat

image Rogue_Sex_Legs_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .5 pos (0,-15)
                ease .25 pos (0,-10)
                pause 1
                ease 2.75 pos (0,0)
                repeat

image Rogue_Sex_Legs_Anim3:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .15
                easein .15 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,0)
                repeat
#End Animations for Rogue's Legs during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Body_Anim1:
        #this is the animation for Rogue's upper body during sex, Speed 1 (heading)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-5)
                pause 1.25
                ease 2.5 pos (0,0)
                repeat

image Rogue_Sex_Body_Anim2:
        #this is the animation for Rogue's upper body during sex, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .6
                easein .4 pos (0,-10)
                ease .25 pos (0,-5)
                pause 1
                ease 2.75 pos (0,10)
                repeat

image Rogue_Sex_Body_Anim3:
        #this is the animation for Rogue's upper body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .17
                easein .13 pos (0,-20)
                ease .10 pos (0,-15)
                pause .20
                ease 1.4 pos (0,10)
                repeat
#End Animations for Rogue's Body during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /





#Start Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Rogue_Sex_Anus:
    contains:
            #Anus background plate
            ConditionSwitch(
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 3", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed >= 2", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "Player.Sprite and Player.Cock == 'anal' and Speed", "Rogue_Sex_Anal_Heading",
            "Player.Sprite and Player.Cock == 'anal'", "Rogue_Sex_Anal_Tip",
            "Trigger == 'insert ass' or Trigger2 == 'insert ass'", "Rogue_Sex_Anal_Tip",
            "Trigger == 'dildo anal'", "images/KittySex/Kitty_Sex_Hole_Open.png",
            "RogueX.Loose", "images/RogueSex/Rogue_Sex_Hole_Loose.png",
            "True", "images/RogueSex/Rogue_Sex_Hole_Tight.png",
            )
    contains:
            #Spunk under penis
            ConditionSwitch(
                "'anal' not in RogueX.Spunk", Null(),
                "Player.Sprite and Player.Cock != 'anal' and Speed >= 1", "images/KittySex/Kitty_Sex_Spunk_Anal_Under.png",
                "Player.Sprite and Player.Cock != 'anal' and Speed == 1", "Rogue_Anal_Spunk_Heading_Under",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Closed.png",
                )
    contains:
            # The animation of Zero's moving penis, masked by her anus shape
            ConditionSwitch(
            "Trigger == 'insert ass' or Trigger2 == 'insert ass'", AlphaMask("Rogue_Sex_FingerA_Anim1", "Rogue_Anal_Fucking_Mask"),
            "Trigger == 'dildo anal'", AlphaMask("Rogue_Anal_Dildo_Anim2", "Rogue_Anal_Fucking_Mask"),
            "not Player.Sprite or Player.Cock != 'anal'", Null(),
            "Speed >= 3",  AlphaMask("Rogue_Anal_Zero_Anim3", "Rogue_Anal_Fucking_Mask"),
            "Speed >= 2", AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask"),
            "Speed", AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask"),
            "True", AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask"),
            )
    contains:
            #Spunk over penis
            ConditionSwitch(
                "'anal' not in RogueX.Spunk or not Player.Sprite or Player.Cock != 'anal' or not Speed", Null(),
                "Speed == 1", "Rogue_Anal_Spunk_Heading_Over",
                "True", "images/KittySex/Kitty_Sex_Spunk_Anal_Over.png",
                )


image Rogue_Sex_Anal_Fucking0:
    # This is the visual for her pussy during the Speed 0 mode (static).
    contains:
            # The background plate of her pussy
            "Rogue_Anal_Tip"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim0", "Rogue_Anal_Fucking_Mask")

image Rogue_Sex_Anal_Fucking1:
    # This is the visual for her pussy during the Speed 1 mode (heading).
    contains:
            # The background plate of her pussy
            "Rogue_Anal_Heading"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim1", "Rogue_Anal_Fucking_Mask")


#End Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Rogue_Hotdog_Body_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .30
                ease .50 pos (0,-10)
                pause .20
                ease 1 pos (0,0)
                repeat

image Rogue_Hotdog_Legs_Anim2:
        #this is the animation for Rogue's lower body during sex, Speed 3 (fast)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .20
                ease .50 pos (0,-10)
                pause .20
                ease 1.1 pos (0,0)
                repeat

#End Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Rogue_Footcock:
    contains:
            subpixel True
            "Blowcock"
            alpha 0.8
            zoom 0.7
            anchor (0.5,0.5)
            offset (465,70)
            pos (0,0)
    pos (750,230)

image Rogue_Footcock_Static:
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
    #pos (750,230)
    offset (0,-100)

image Rogue_Footcock_Zero_Anim1:
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 ypos 360#65
                ease .25 ypos 355#60
                pause 1
                ease 2.50 ypos 270#285
                repeat
    offset (0,-100)

image Rogue_Footcock_Zero_Anim2:
    contains:
            subpixel True
            "Rogue_Footcock"
            pos (392,295)
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 ypos 360
                ease .2 ypos 355
                pause .2
                ease 1.00 ypos 270
                repeat
    offset (0,-100)

image Rogue_Sex_Legs_FootAnim1:
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 5 seconds
                pause .5
                easein .75 pos (0,-65)
                ease .25 pos (0,-60)
                pause 1
                ease 2.50 pos (0,25)#(0,10)
                repeat
        #pos (750,230)
        offset (0,100)

image Rogue_Sex_Legs_FootAnim2:
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 2 seconds
                pause .2
                easein .4 pos (0,-65)
                ease .2 pos (0,-60)
                pause .2
                ease 1.0 pos (0,25)#(0,10)
                repeat
        offset (0,100)

image Rogue_Sex_Legs_FootAnimStatic:
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Legs"
            pos (0,0) #X less is left, Y less is up
        offset (0,100)

#End Animations for Rogue's Legs during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Rogue's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Rogue_Sex_Body_FootAnim1:
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                easein .75 pos (0,-25)#(0,-5)
                ease .25 pos (0,-15)#(0,0)
                pause 1
                ease 2.50 pos (0,15)#(0,5)
                repeat
        #pos (750,230)
        offset (0,100)

image Rogue_Sex_Body_FootAnim2:
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .2
                easein .4 pos (0,-25)#(0,-5)
                ease .2 pos (0,-15)#(0,0)
                pause .2
                ease 1.0 pos (0,15)#(0,5)
                repeat
        offset (0,100)

image Rogue_Sex_Body_FootAnimStatic:
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
        contains:
            subpixel True
            "Rogue_Sex_Body"
            pos (0,0) #X less is left, Y less is up
        offset (0,100)


# End Rogue Sex pose Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# Core Rogue BJ element ///////////////////////////////////////////////////////////////////////////                                     Core Rogue BJ element
#Rogue BJ Over Sprite Compositing


image Rogue_BJ_Animation:#BJ_NewTest:                                                                #core BJ animation
    LiveComposite(
        (787,913),
        (0,0), ConditionSwitch(
            # back of the hair, which needs to go behind the body
            "Speed == 0", At("Rogue_BJ_HairBack", Rogue_BJ_Starting()),
            "Speed == 1", At("Rogue_BJ_HairBack", Rogue_BJ_Licking()),
            "Speed == 2", At("Rogue_BJ_HairBack", Rogue_BJ_Heading()),
            "Speed == 3", At("Rogue_BJ_HairBack", Rogue_BJ_Sucking()),
            "Speed >= 4", At("Rogue_BJ_HairBack", Rogue_BJ_Deep()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # body, everything below the chin
            "Speed == 0", At("Rogue_BJ_Backdrop", Rogue_BJ_StartingBody()),
            "Speed == 1", At("Rogue_BJ_Backdrop", Rogue_BJ_LickingBody()),
            "Speed == 2", At("Rogue_BJ_Backdrop", Rogue_BJ_HeadingBody()),
            "Speed == 3", At("Rogue_BJ_Backdrop", Rogue_BJ_SuckingBody()),
            "Speed >= 4", At("Rogue_BJ_Backdrop", Rogue_BJ_DeepBody()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            # her head
            "Speed == 0", At("Rogue_BJ_Head", Rogue_BJ_Starting()),
            "Speed == 1", At("Rogue_BJ_Head", Rogue_BJ_Licking()),
            "Speed == 2", At("Rogue_BJ_Head", Rogue_BJ_Heading()),
            "Speed == 3", At("Rogue_BJ_Head", Rogue_BJ_Sucking()),
            "Speed >= 4", At("Rogue_BJ_Head", Rogue_BJ_Deep()),
            "True", Null(),
            ),
#        (0,0), Transform("images/RogueBJFace/Rogue_bj_markercard.png", alpha=(.2)),
        (0,0), ConditionSwitch(
            # cock
            "Speed == 0", At("Blowcock", Rogue_Cock_BJ_Starting()),
            "Speed == 1", At("Blowcock", Rogue_Cock_BJ_Licking()),
            "Speed == 2", At("Blowcock", Rogue_Cock_BJ_Straight()),
            "Speed == 3", At("Blowcock", Rogue_Cock_BJ_Straight()),
            "Speed >= 4", At("Blowcock", Rogue_Cock_BJ_Straight()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 # the masked overlay for when her head overlaps the cock
            "Speed < 3", Null(),
            "Speed == 3", At(AlphaMask("Rogue_BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), Rogue_BJ_Sucking()),
            "Speed >= 4", At(AlphaMask("Rogue_BJ_Head", "images/RogueBJFace/Rogue_bj_facemask.png"), Rogue_BJ_Deep()),
            "True", Null(),
            ),
        (0,0), ConditionSwitch(                                                                 # same as above, but for the heading animation
            "Speed == 2", At(AlphaMask("Rogue_BJ_Head", "Rogue_BJ_MaskHeadingComposite"), Rogue_BJ_Heading()),
            "True", Null(),
            ),
        )
    zoom .55
    anchor (.5,.5)

image Rogue_BJ_Head:
    "Rogue_Head"
    zoom 3.45


image Rogue_BJ_HairBack:
    "Rogue_HairBack"
    zoom 3.45

image Rogue_BJ_Backdrop:                                                                        #Her Body under the head
    "Rogue_Sprite"
    zoom 4.5
    pos (175,-110)
    offset (-615, -125)


image Rogue_BJ_MouthHeading:
    #the mouth used for the heading animations
    contains:
        ConditionSwitch(
            #if spunk in mouth
            "'mouth' in RogueX.Spunk", "images/RogueBJFace/Rogue_bj_mouth_suckingS.png",
            "True", "images/RogueBJFace/Rogue_bj_mouth_sucking.png",
            )
#        "images/RogueBJFace/Rogue_bj_mouth_sucking.png"
        anchor (0.40,0.65)

image Rogue_BJ_MaskHeading:
    #the mask used for the heading image
    contains:
        "images/RogueBJFace/Rogue_bj_facemask.png"
        anchor (0.4,0.65)

image Rogue_BJ_MaskHeadingComposite:
    #The composite for the heading mask that goes over the face
    LiveComposite(
        (787,913),
        (316,590), ConditionSwitch(      #600
            "Speed == 2", At("Rogue_BJ_MaskHeading", Rogue_BJ_MouthAnim()),
            "True", Null(),
            ),
        )


# Core Rogue Titfucking element //////////////////////////////////////////////////////////////////////                                         Core Rogue TJ element

image Rogue_TJ_Under:
    contains:
        "Rogue_BJ_HairBack"
        pos (150, -560)
        zoom .95
    contains:
        "images/RogueBJFace/Rogue_tj_base.png"
    contains:
        ConditionSwitch(
            "'tits' in RogueX.Spunk", "images/RogueBJFace/Rogue_tj_spunkU.png",
            "True", Null(),
            ),
    contains:
        "Rogue_BJ_Head"
        pos (150, -560)
        zoom .95
    pos (-60, 200)

image Rogue_TJ_Over:
    contains:
        ConditionSwitch(
            "RogueX.Pierce == 'barbell'", "images/RogueBJFace/Rogue_tj_tits_b.png",
            "RogueX.Pierce == 'ring'", "images/RogueBJFace/Rogue_tj_tits_r.png",
            "RogueX.Pierce != 'barbell'", "images/RogueBJFace/Rogue_tj_tits.png",
            ),
    contains:
        ConditionSwitch(
            "'tits' in RogueX.Spunk", "images/RogueBJFace/Rogue_tj_spunk.png",
            "True", Null(),
            ),
    pos (-60, 200)




image Rogue_TJ_Animation:
    #core TJ animation
    contains:
        ConditionSwitch(
            "not Speed", Transform("Rogue_TJ_Under"),
            "Speed == 1", At("Rogue_TJ_Under", Rogue_TJ_Under_1()),
            "Speed >= 2", At("Rogue_TJ_Under", Rogue_TJ_Under_2()),
            "Speed", Null(),
            ),

    contains:
        ConditionSwitch(
            "not Speed", At("Zero_Blowcock", Zero_TJ_Cock()),
            "Speed == 1", At("Zero_Blowcock", Zero_TJ_Cock_1()),
            "Speed >= 2", At("Zero_Blowcock", Zero_TJ_Cock_2()),
            "Speed", Null(),
            ),

    contains:
        ConditionSwitch(
            "not Speed", Transform("Rogue_TJ_Over"),
            "Speed == 1", At("Rogue_TJ_Over", Rogue_TJ_Over_1()),
            "Speed >= 2", At("Rogue_TJ_Over", Rogue_TJ_Over_2()),
            "Speed", Null(),
            ),
    anchor (0.6, 0.0)
    offset (-75, 250)
    zoom .55


# Core Rogue Handjob element //////////////////////////////////////////////////////////////////////                                         Core Rogue HJ element


image Rogue_Hand_Under:
    "images/RogueBJFace/hand2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Rogue_Hand_Over:
    "images/RogueBJFace/hand1.png"
    anchor (0.5,0.5)
    pos (0,0)

image Rogue_HJ_Animation:
    contains:
        ConditionSwitch(                                                # backside of the hand
            "not Speed", "Rogue_Hand_Under",
            "Speed == 1", At("Rogue_Hand_Under", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Under", Rogue_Hand_2()),
            "Speed", Null(),
            ),
    contains:
        ConditionSwitch(                                                # cock
            "not Speed", "Zero_Handcock",
            "Speed == 1", At("Zero_Handcock", Handcock_1()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2()),
            "Speed", Null(),
            ),
        offset (0,0)
    contains:
        ConditionSwitch(                                                # fingers of the hand
            "not Speed", "Rogue_Hand_Over",
            "Speed == 1", At("Rogue_Hand_Over", Rogue_Hand_1()),
            "Speed >= 2", At("Rogue_Hand_Over", Rogue_Hand_2()),
            "Speed", Null(),
            ),
    anchor (0.5,0.5)#anchor (0.51, -1.3)
    offset (200,800)
    zoom 0.6

label Rogue_HJ_Launch(Line = Trigger):
    if renpy.showing("Rogue_HJ_Animation"):
        $ Trigger = "hand"
        return
    call hide_girl(RogueX)
    $ RogueX.Arms = 0
    $ RogueX.ArmPose = 1
    if not renpy.showing("Rogue_Sprite"):
        show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
            alpha 1
            zoom 1.7 xpos 700 offset (0,200)
        with dissolve
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 1.7  xpos 700 offset (0,200)

    if Taboo and Line == "L":
        # Rogue gets started. . .
        if len(Present) >= 2:
            if Present[0] != RogueX:
                    "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
            elif Present[1] != RogueX:
                    "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
        else:
                    "[RogueX.Name] looks around to see if anyone can see her."
        if not RogueX.Hand and RogueX.Arms:
            "As you pull out your cock, [RogueX.Name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "She then leans over and grabs your cock."
    elif Line == "L":
        if not RogueX.Hand and RogueX.Arms:
            "As you pull out your cock, [RogueX.Name] pulls off her gloves, and hesitantly reaches for it. She starts to roughly stroke on it."
        else:
            "[RogueX.Name] bends down and grabs your cock."
    else:
            "[RogueX.Name] bends down and grabs your cock."

    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    show Rogue_HJ_Animation at sprite_location(RogueX.sprite_location) zorder 150 with easeinbottom
    return

label Rogue_HJ_Reset: # The sequence to the Rogue animations from handjob to default
    if not renpy.showing("Rogue_HJ_Animation"):
        return
    $ Speed = 0
    hide Rogue_HJ_Animation
    with dissolve
    call hide_girl(RogueX)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        zoom 1.7  xpos 700 offset (0,200)
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos RogueX.sprite_location yoffset 0
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        zoom 1  xpos RogueX.sprite_location yoffset 0
    return

label Rogue_Middle_Launch(T = Trigger,Set=1):
    call hide_girl(RogueX)
    $ Trigger = T
    $ RogueX.Pose = "mid" if Set else RogueX.Pose
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return
