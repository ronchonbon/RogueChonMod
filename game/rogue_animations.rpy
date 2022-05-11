

image Rogue_Doggy_Lick_Pussy:
    "Lick_Anim"
    zoom 0.5
    offset (195,540)

image Rogue_Doggy_Lick_Ass:
    "Lick_Anim"
    zoom 0.5
    offset (195,500)

image Rogue_Doggy_GropeBreast:
    contains:
        subpixel True
        "images/UI_HandUnder.png"
        xzoom -.55
        yzoom .55
        offset (150,340)#(100,200)
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0
        block:
            ease 1 rotate 10#60
            ease 1 rotate 0#90
            repeat

image Zero_Doggy_Up:
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_U_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_U_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_U_G.png")
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_U_W.png",
            "True", Null())

image Zero_Hotdog_Static:
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)

image Zero_Hotdog_Moving:
    contains:
        "Zero_Doggy_Up"
        pos (175, 370)
        block:
            ease 1 ypos 330
            ease 1 ypos 420
            repeat

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Insert cock animations
image Zero_Doggy_Insert:
    #Insert cock
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueDoggy/Rogue_Doggy_Cock_In_P.png",
            "Player.Color == 'brown'", "images/RogueDoggy/Rogue_Doggy_Cock_In_B.png",
            "True", "images/RogueDoggy/Rogue_Doggy_Cock_In_G.png",
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueDoggy/Rogue_Doggy_Cock_In_Wet.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Spunk", "images/RogueDoggy/Rogue_Doggy_Cock_In_Spunk.png",
            "True", Null(),
            ),

#image Zero_Doggy_Static:
#    # Sex Speed 2 motions
#    contains:
#        "Zero_Doggy_Insert"
#        pos (169,500)
#        block:
#            ease .5 ypos 540
#            pause .25
#            ease 1.75 ypos 545
#            repeat

image Zero_Doggy_Static:
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

image Zero_Doggy_Heading:
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

image Zero_Doggy_Fucking2:
    # Sex Speed 2 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .5 ypos 440
            pause .25
            ease 1.75 ypos 500
            repeat

image Zero_Doggy_Fucking3:
    # Sex Speed 3 motions
    contains:
        "Zero_Doggy_Insert"
        pos (169,500)
        block:
            ease .2 ypos 440
            pause .1
            ease .6 ypos 500
            repeat

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Pussy fucking animations
#image Rogue_Pussy:
#    #Full Animation for speed 0
#    contains:
#        #Base
#        "images/RogueDoggy/Rogue_Doggy_Pussy_FBase.png"
#    contains:
#        ConditionSwitch(
#            #full hose/tights
#            "RogueX.PantiesDown", Null(),
#            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
#            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
##            "RogueX.Hose == 'tights' and RogueX.Wet", "images/RogueDoggy/Rogue_Doggy_Tights_Wet.png",
##            "RogueX.Hose == 'tights'", "images/RogueDoggy/Rogue_Doggy_Tights.png",
##            "RogueX.Hose == 'pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose.png",
#            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
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

image Zero_Pussy_Finger:
    # Sex Speed 1 motions
    contains:
        subpixel True
        "images/UI_Fingering.png"
        pos (171,545)
        block:
            ease 1 xpos 168 ypos 500 #in stroke
            pause 1
            ease 3 xpos 171 ypos 545 #out stroke
            repeat

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

image Zero_Doggy_Anal_Heading:
        #the cock anal heading animation
    contains:
        "Zero_Doggy_Insert"
        pos (172,500)
        block:
            ease .5 ypos 450
            pause .25
            ease 1.75 ypos 500#505
            repeat

image Zero_Doggy_Anal_HeadingJunk:
    #this is a mask to correct an annoying glitch in the core mask
    contains:
        Solid("#159457", xysize=(150,150))
        pos (152,600)
        block:
            ease .5 ypos 550
            pause .25
            ease 1.75 ypos 600#505
            repeat

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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal1:
    #Animation for speed 2 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .5 ypos 395
            pause .25
            ease 1.75 ypos 460
            repeat

#image Rogue_Anal_FuckingB:
#    #Animation for speed 2 Ass
#    contains:
#        #Base
#        "images/RogueDoggy/Rogue_Doggy_Anal_FullBase.png"
#    contains:
#        #Hole
#        "images/RogueDoggy/Rogue_Doggy_Anal_FullHole.png"
#    contains:
#        #Cheeks
#        "images/RogueDoggy/Rogue_Doggy_Anal_FullCheeks.png"
#    contains:
#        ConditionSwitch(
#            #full hose/tights
#            "RogueX.Hose == 'garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings_Loose.png",
#            "RogueX.Hose == 'stockings and garterbelt'", "images/RogueDoggy/Rogue_Doggy_Stockings.png",
#            "RogueX.Panties and RogueX.PantiesDown", Null(),
#            "RogueX.Hose == 'ripped pantyhose'", "images/RogueDoggy/Rogue_Doggy_FullHose_Holed.png",
#            "RogueX.Hose == 'ripped tights'", "images/RogueDoggy/Rogue_Doggy_Tights_Holed.png",
#            "True", Null(),
#            ),
#    contains:
#        #Cock
#        AlphaMask("Zero_Doggy_Anal1", "images/RogueDoggy/Rogue_Doggy_Anal_CockMask.png")




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


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
image Zero_Doggy_Anal2:
    #Animation for speed 3 Cock
    contains:
        "Zero_Doggy_Insert"
        pos (172,460)
        block:
            ease .2 ypos 395
            pause .1
            ease .6 ypos 465
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

image Slap_Ass:
    contains:
        "SlapHand"
        pause 1.2
        Null()

image Slap_Ass:
    contains:
        "UI_Hand"
        subpixel True
        zoom 1
        alpha 0.5
        anchor (0.5,0.5)
        pos (600,380)
        rotate 40
        block:
            parallel:
                ease .5 xpos 300 rotate 80
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9

image NotSlap_Ass:
    contains:
        subpixel True
        "UI_Hand"
        zoom 1
        pos (600,380) #follow through  point r-60
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            pos (600,380)
            rotate 40
            parallel:
                ease .5 xpos 300 rotate 80
                ease .1 xpos 310 rotate 80
                pause .5
            parallel:
                ease .2 ypos 520
                pause .9
            repeat


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

image Rogue_Sex_Lick_Pussy:
        "Lick_Anim"
        zoom 0.7
        offset (530,510)

image Rogue_Sex_Lick_Ass:
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

image Rogue_Sex_FingerP_Anim1:
        #this is Rogue's fingering animation
        contains:
            subpixel True
            "images/UI_Fingering.png"
            pos (507,520) #X less is left, Y less is up(498,525)
            zoom 1.2#1.3
            block:
                ease .2 ypos 480 #(498,500)
                pause .2
                ease .6 ypos 520
                repeat

image Rogue_Sex_Dildo_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "images/DildoIn.png"
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease 1 ypos 380 #(500,470)
                pause 1
                ease 3 ypos 490
                repeat

#Start Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Sex_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,530) #X less is left, Y less is up (498,530)
            zoom 1.3#1.4

image Rogue_Sex_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,525) #X less is left, Y less is up(498,525)
            zoom 1.3#1.4
            block:
                ease 1 ypos 510 #(498,500)
                pause 1
                ease 3 ypos 525
                repeat

image Rogue_Sex_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease 1 ypos 380 #(500,470)
                pause 1
                ease 3 ypos 490
                repeat

image Rogue_Sex_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (504,490) #X less is left, Y less is up
            zoom 1.3#1.4
            block:
                ease .25 ypos 380 #(500,470)
                pause .25
                ease 1.5 ypos 490
                repeat
#End Animations for Zero's Cock during Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

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

image Rogue_Sex_FingerA_Anim1:
        #this is Rogue's fingering animation
        contains:
            subpixel True
            "images/UI_Fingering.png"
            pos (507,600) #X less is left, Y less is up(498,525)
            zoom 1.2#1.3
            block:
                ease .4 ypos 550 #480
                pause .4
                ease 1.2 ypos 600#520
                repeat

image Rogue_Anal_Dildo_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "images/DildoIn.png"
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 450 #(500,470)
                pause 1
                ease 3 ypos 570
                repeat

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

image Rogue_Sex_Anal_Fucking2:
    # This is the visual for her pussy during the Speed 2 mode (slow).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Rogue_Anal_Zero_Anim2", "Rogue_Anal_Fucking_Mask")

image Rogue_Sex_Anal_Fucking3:
    # This is the visual for her pussy during the Speed 3 mode (fast).
    contains:
            # The background plate of her pussy
            "images/KittySex/Kitty_Sex_Hole_Open.png"
    contains:
            # The animation of Zero's moving penis, masked by her pussy shape
            AlphaMask("Kitty_Anal_Zero_Anim3", "Kitty_Anal_Fucking_Mask")

image Rogue_Anal_Fucking_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 1#0

image Rogue_Anal_Open_Mask:
        #This is the mask image for Kitty's wide open pussy
        contains:
            "images/KittySex/Kitty_Sex_Hole_Mask.png"
            yoffset 3#3

image Rogue_Sex_Anal_Heading:
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

image Rogue_Anal_Spunk_Heading_Over:
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
image Rogue_Anal_Spunk_Heading_Under:
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

image Rogue_Sex_Anal_Tip:
    "images/KittySex/Kitty_Sex_Hole_Open.png"
    anchor (0.5,0.5)
    pos (0.5,0.5)
    xzoom 0.6

#End Animations for Rogue's Pussy during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Anal_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,600) #X less is left, Y less is up (498,520)
            zoom 1.3

image Rogue_Anal_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,600) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 570 #(500,470)
                pause 1
                ease 3 ypos 600
                repeat

image Rogue_Anal_Zero_Anim2:
        #this is Rogue's sex animation, Speed 2 (slow)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 450 #(500,470)
                pause 1
                ease 3 ypos 570
                repeat

image Rogue_Anal_Zero_Anim3:
        #this is Rogue's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (505,570) #X less is left, Y less is up
            zoom 1.3
            block:
                ease .25 ypos 450 #(500,470)
                pause .25
                ease 1.5 ypos 570
                repeat
#End Animations for Zero's Cock during Anal / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#Start Animations for Zero's Cock during Hotdog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Rogue_Hotdog_Zero_Anim0:
        #this is Rogue's sex animation, Speed 0 (static)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,570) #X less is left, Y less is up
            zoom 1.3

image Rogue_Hotdog_Zero_Anim1:
        #this is Rogue's sex animation, Speed 1 (heading)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,500) #X less is left, Y less is up
            zoom 1.3
            block:
                ease 1 ypos 560 #(500,500)
                pause .5
                ease 1.5 ypos 500
                repeat

image Rogue_Hotdog_Zero_Anim2:
        #this is Rogue's sex animation, Speed 3 (fast)
        contains:
            subpixel True
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
            pos (503,510) #X less is left, Y less is up
            zoom 1.3
            block:
                ease .5 ypos 400 #(500,470)
                pause .5
                ease 1 ypos 510
                repeat

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

transform Rogue_Footcock_Zero_Anim1A():
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

transform Rogue_Footcock_Zero_Anim2A():
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

transform Rogue_Footcock_StaticA():
            subpixel True
            offset (0,-5)
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset 0
                pause 1
                ease 1.50 yoffset -5
                repeat

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

transform Rogue_Sex_Legs_FootAnim1A():
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
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

transform Rogue_Sex_Legs_FootAnim2A():
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
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

transform Rogue_Sex_Legs_FootAnimStaticA():
        #this is the animation for Rogue's lower body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat

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

transform Rogue_Sex_Body_FootAnim1A():
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
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

transform Rogue_Sex_Body_FootAnim2A():
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
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

transform Rogue_Sex_Body_FootAnimStaticA():
        #this is the animation for Rogue's upper body during Footjobs, Speed 2 (slow)
            subpixel True
            offset (0,0) #X less is left, Y less is up
            block:
                #Total time, 4 seconds
                pause .5
                ease 1 yoffset -5
                pause 1
                ease 1.50 yoffset 0
                repeat
#End Animations for Rogue's Body during Footjobs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                                     Sex Launch/Reset
label Rogue_Sex_Launch(Line = Trigger):
    $ Trigger3 = 0 if Trigger3 == "hand" else Trigger3

    $ Line = "solo" if not Line else Line
    $ Player.Sprite = 1
    if Line == "sex":
        $ Player.Cock = "in"
        if Trigger2 in ("fondle pussy","dildo pussy","lick pussy"):
                $ Trigger2 = 0
    elif Line == "anal":
        $ Player.Cock = "anal"
        if Trigger2 in ("insert ass","dildo anal","lick ass"):
                $ Trigger2 = 0
    elif Line == "hotdog":
        $ Player.Cock = "out"
    elif Line == "foot":
        $ ShowFeet = 1
        $ Player.Cock = "foot"
    elif Line == "massage":
        $ Player.Sprite = 0
        $ Player.Cock = 0
    else: #elif Line == "solo":
        $ Player.Sprite = 0
        $ Player.Cock = "out"
        $ Speed = 0
    $ Trigger = Line

    if RogueX.Pose == "doggy":
            call Rogue_Doggy_Launch(Line)
            return
    if renpy.showing("Rogue_SexSprite"):
        return
    $ Speed = 0
    call hide_girl(RogueX, sprite = True)
    show Rogue_SexSprite zorder 150
#    show Rogue_SexSprite zorder 150:
#        pos (750,230)

    with dissolve
    return

label Rogue_Sex_Reset:
    if renpy.showing("Rogue_Doggy_Animation"):
        call Rogue_Doggy_Reset
        return
    if not renpy.showing("Rogue_SexSprite"):
        return
    $ RogueX.ArmPose = 2
    hide Rogue_SexSprite
    call hide_girl(RogueX)
#    call Set_The_Scene(Dress = 0)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        zoom 1 offset (0,0)
        anchor (0.5, 0.0)
    with dissolve
    $ Speed = 0
    return


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

transform Rogue_BJ_MouthAnim():
        #The animation for the heading mouth
        subpixel True
        zoom 0.90     #small
        block: #total time 10 down, 15 back up
            pause .10   #.4
            easeout .55 zoom 0.9 #.25
            linear .10 zoom 0.87
            easein .30 zoom 0.9
            pause .15
            easeout .40 zoom 0.87
            linear .10 zoom 0.9
            easein .45 zoom 0.70
            pause .35
            repeat

image Blowcock:
    contains:
        ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
    contains:
        ConditionSwitch(
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png",
            "True", Null(),
            ),
    anchor (0.5,0.5)
    zoom 1.0
    alpha 1.0
    offset (26,350)#(-175,450)

transform Rogue_Cock_BJ_Starting():
    #The static animation for the cock
    anchor (.5,.5)
    rotate -10

transform Rogue_Cock_BJ_Licking():
    #The licking animation for the cock
    subpixel True
    anchor (.5,.5)
    ease 0.5 rotate 0
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat

transform Rogue_Cock_BJ_Straight():
    #The static animation for the cock
    anchor (.5,.5)
    rotate 0

transform Rogue_BJ_Licking():
    #The licking animation for her face
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (25,100) #bottom
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform Rogue_BJ_LickingBody():
    #The licking animation for her body
    subpixel True
    ease 0.5 offset (0,-35)  #top
    block:
        ease 2.5 offset (30,90) #bottom 25,50
        ease 2 offset (0,-35)  #top
        pause .5
        repeat

transform Rogue_BJ_Heading():
    #The heading animation for her face
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 35           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat

transform Rogue_BJ_HeadingBody():
    #The heading animation for her body
    subpixel True
    offset (0,-40)     #top
    block:
        ease 1 yoffset 15           #bottom
        ease 1.5 offset (0,-40)     #top
        repeat

transform Rogue_BJ_Sucking():
    #The sucking animation for her face
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 120 #100
        ease 1.5 offset (0,50)
        repeat

transform Rogue_BJ_SuckingBody():
    #The sucking animation for her body
    subpixel True
    ease 0.5 offset (0,50)
    block:
        ease 1 yoffset 100 #80      #bottom
        ease 1.5 offset (0,50) #top
        repeat

transform Rogue_BJ_Deep():
    #The deep animation for her face
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1 yoffset 300
        pause .5
        ease 2 yoffset 100
        repeat

transform Rogue_BJ_DeepBody():
    #The deep animation for her body
    ease .5 offset (0,100)
    block:
        subpixel True
        ease 1.2 yoffset 250
        pause .5
        ease 1.8 yoffset 100
        repeat

transform Rogue_BJ_Static():
    #The static animation for her face
    subpixel True
    ease 1.5 offset (0,0)
    repeat

transform Rogue_BJ_StaticBody():
    #The static animation for her face
    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_BJ_Starting():
    #The starting animation for her face
    subpixel True
    ease 1.5 offset (0,0)

transform Rogue_BJ_StartingBody():
    #The starting animation for her face
    subpixel True
    ease 1.5 offset (0,0)
                                                               #BJ Launchers
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Rogue_BJ_Launch(Line = Trigger):
    # The sequence to launch the Rogue BJ animations
    if renpy.showing("Rogue_BJ_Animation"):
        return

    call hide_girl(RogueX)
    if Line == "L" or Line == "cum":
        show Rogue_Sprite at sprite_location(StageCenter) zorder RogueX.Layer:
            alpha 1
#            zoom 1 offset (0,0)
            ease 1 zoom 2.5 offset (70,140) #(-90,140) offset (150,80)
        with dissolve
    else:
        show Rogue_Sprite at sprite_location(StageCenter) zorder RogueX.Layer:
            alpha 1
            zoom 2.5 offset (70,140) #(-90,140)
        with dissolve

    if Taboo and Line == "L":
            # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != RogueX:
                        "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[RogueX.Name] looks around to see if anyone can see her."
    if Line == "L":
            if not RogueX.Blow:
                "[RogueX.Name] hesitantly pulls down your pants and touches her mouth to your cock."
            else:
                "[RogueX.Name] bends down and begins to suck on your cock."

    $ Speed = 0

    if Line != "cum":
        $ Trigger = "blow"

    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    show Rogue_BJ_Animation zorder 150:
        pos (645,510)
    return

label Rogue_BJ_Reset: # The sequence to the Rogue animations from BJ to default
    if not renpy.showing("Rogue_BJ_Animation"):
        return
#    hide Rogue_BJ_Animation
    call hide_girl(RogueX)
    $ Speed = 0

    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        zoom 2 offset (70,140)
        alpha 1
        block:
            pause .5
            ease 1 zoom 1.5 offset (-50,50)
            pause .5
            ease .5 zoom 1 offset (0,0)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        zoom 1 offset (0,0)
    $ RogueX.FaceChange("sexy")
    return

# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////
# ////////////////////////////////                                                                                      ///////////////////////////////


transform Zero_BJ_Static():                            #The static animation for the cock
    anchor (.5,.5)
#    pos (180,560) #(125,300)
    rotate -10
#    pos (-25,0)

transform Zero_BJ_Sucking():                            #The sucking animation for the cock
    anchor (.5,.5)
    rotate 0

transform Zero_BJ_Licking():                            #The licking animation for the cock
    subpixel True
    block:
        ease 2 rotate -5 #410
        pause .5
        ease 2.5 rotate 0
        repeat

image Zero_Blowcock:
    LiveComposite(                            #The compositived BJ cock
        (175,946),
        (0,0), ConditionSwitch(
            "Player.Color == 'pink'", "images/RogueBJFace/Zero_Cock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/Zero_Cock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/Zero_Cock_G.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "Player.Wet", "images/RogueBJFace/Zero_Cock_Wet.png",
            "True", Null(),
            ),
        (0,0), ConditionSwitch(
            "Player.Spunk", "images/RogueBJFace/Zero_Cock_S.png",
            "True", Null(),
            ),
        )
    anchor (0.5,0.5)
    zoom 1.2
    xoffset 5



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


transform Rogue_TJ_Under_1():
    ypos 200
    subpixel True
    block:
        ease 1 ypos 300
        easeout .2 ypos 300
        easein 1.3 ypos 120
        repeat

transform Rogue_TJ_Over_1():
    ypos 200
    subpixel True
    block:
        ease 1.20 ypos 300
        easeout .1 ypos 300
        easein 1.2 ypos 120
        repeat

transform Rogue_TJ_Under_2():
    ypos 200
    subpixel True
    block:
        ease .25 ypos 200
        ease .4 ypos 120
        ease .1 ypos 125
        repeat

transform Rogue_TJ_Over_2():
    ypos 200
    subpixel True
    block:
        ease .3 ypos 200
        ease .35 ypos 120
        ease .1 ypos 125          #high point
        repeat


transform Zero_TJ_Cock():
    #The sucking animation for the cock
    anchor (.5,.5)
    pos (440,1020) #220,1000 #(180,560)
    rotate 0

transform Zero_TJ_Cock_1():
    pos (440,1020)
    subpixel True
    block:
        ease 1 ypos 1050
        easeout .2 ypos 1060
        easein 1.3 ypos 1020
        repeat

transform Zero_TJ_Cock_2():
    pos (440,1020)
    subpixel True
    block:
        ease .35 ypos 1030
        ease .4 ypos 1020
#        pause .1
        repeat



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

label Rogue_TJ_Launch(Line = Trigger):
    # The sequence to launch the Rogue Titfuck animations
    if renpy.showing("Rogue_TJ_Animation"):
        return
    call hide_girl(RogueX)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 2 xpos 550 offset (0,50)
    if Taboo: # Rogue gets started. . .
            if len(Present) >= 2:
                if Present[0] != RogueX:
                        "[RogueX.Name] looks back at [Present[0].Name] to see if she's watching."
                elif Present[1] != RogueX:
                        "[RogueX.Name] looks back at [Present[1].Name] to see if she's watching."
            else:
                        "[RogueX.Name] looks around to see if anyone can see her."

    if RogueX.Chest and RogueX.Over:
        "She throws off her [RogueX.Over] and her [RogueX.Chest]."
    elif RogueX.Over:
        "She throws off her [RogueX.Over], baring her breasts underneath."
    elif RogueX.Chest:
        "She tugs off her [RogueX.Chest] and throws it aside."
    $ RogueX.Over = 0
    $ RogueX.Chest = 0
    $ RogueX.Arms = 0

    call first_topless(RogueX)

    if not RogueX.Tit and Line == "L": #first time
        if not RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her [RogueX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and RogueX.Over:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her [RogueX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.Name] hesitantly places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    elif Line == "L": #any other time
        if not RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and not RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it under her [RogueX.Chest], between her breasts and starts to rub them up and down the shaft."
        elif RogueX.Chest and RogueX.Over:
            "As you pull out your cock, [RogueX.Name] places it under her [RogueX.Over], between her breasts and starts to rub them up and down the shaft."
        else:
            "As you pull out your cock, [RogueX.Name] places it under her clothes, between her breasts and starts to rub them up and down the shaft."
    else:
            "[RogueX.Name] wraps her tits around your cock."
    show blackscreen onlayer black with dissolve
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Rogue_TJ_Animation at sprite_location(StageRight) zorder 150
    hide blackscreen onlayer black with dissolve
    return

label Rogue_TJ_Reset:
    # The sequence to the Rogue animations from Titfuck to default
    if not renpy.showing("Rogue_TJ_Animation"):
            return
    hide Rogue_TJ_Animation
    call hide_girl(RogueX)
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
            zoom 2 xpos 550 offset (0,50)
    show Rogue_Sprite zorder RogueX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 500 offset (0,50)
        pause .5
        ease .5 zoom 1 xpos RogueX.sprite_location yoffset 0
    show Rogue_Sprite at sprite_location(RogueX.sprite_location) zorder RogueX.Layer:
        alpha 1
        zoom 1 xpos RogueX.sprite_location yoffset 0

    "[RogueX.Name] pulls back"
    return


# Core Rogue Handjob element //////////////////////////////////////////////////////////////////////                                         Core Rogue HJ element

image Zero_Handcock:
    contains:
        ConditionSwitch(    # Zero cock sucking
            "Player.Color == 'pink'", "images/RogueBJFace/handcock_P.png",
            "Player.Color == 'brown'", "images/RogueBJFace/handcock_B.png",
            "Player.Color == 'green'", "images/RogueBJFace/handcock_G.png",
            "Player.Color != 'pink'", Null(),
            ),
    anchor (0.5,1.0)  #1.0
    pos (200,400)#(200,400)

image Rogue_Hand_Under:
    "images/RogueBJFace/hand2.png"
    anchor (0.5,0.5)
    pos (0,0)


image Rogue_Hand_Over:
    "images/RogueBJFace/hand1.png"
    anchor (0.5,0.5)
    pos (0,0)

transform Handcock_1():
    subpixel True
    rotate_pad False
    ease .5 ypos 450 rotate -2 #450
    pause 0.25
    ease 1.0 ypos 400 rotate 0 #400
    pause 0.1
    repeat

transform Handcock_2():
    subpixel True
    rotate_pad False
    ease .2 ypos 430 rotate -3 #410
    ease .5 ypos 400 rotate 0
    pause 0.1
    repeat

transform Rogue_Hand_1():
    subpixel True
    ease .5 ypos 150 rotate 5 #500 #100 #rotate 10#   Bottom
    pause 0.25
    ease 1.0 ypos -100 rotate -5 #250#-150 #rotate -10#  Top
    pause 0.1
    repeat

transform Rogue_Hand_2():
    subpixel True
    ease 0.2 ypos 0 rotate 3
    pause 0.1
    ease 0.4 ypos -100 rotate -3
    pause 0.1
    repeat

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
