label WardrobeEditor(Chr=0): #rkeljs
    while True:
        menu Wardrobe_Menu:
            "View" if True:
                while True:
                    menu:
                        "Default":
                            call expression Chr.Tag + "_Pos_Reset" pass (0)
                        "Face":
                            call expression Chr.Tag + "_Kissing_Launch" pass (0)
                        "Body":
                            call expression Chr.Tag + "_Pussy_Launch" pass (0)
                        "Face Low":
                            call Storm_Hide
                            show Storm_Sprite at sprite_location(StormX.sprite_location) zorder StormX.Layer
                            show Storm_Sprite at sprite_location(StageCenter) zorder StormX.Layer:
                                ease 0.5 offset (100,200) zoom 1.5 alpha 1

                        "BJ":
                            if not renpy.showing(Chr.Tag+"_BJ_Animation"):
                                call expression Chr.Tag + "_BJ_Launch"
                            else:
                                call expression Chr.Tag + "_BJ_Reset"
                        "HJ":
                            if not renpy.showing(Chr.Tag+"_HJ_Animation"):
                                call expression Chr.Tag + "_HJ_Launch"
                            else:
                                call expression Chr.Tag + "_HJ_Reset"
                        "TJ":
                            if not renpy.showing(Chr.Tag+"_TJ_Animation"):
                                call expression Chr.Tag + "_TJ_Launch"
                            else:
                                call expression Chr.Tag + "_TJ_Reset"
                        "Doggy" if Chr == RogueX:
                            $ Chr.Pose = "doggy"
                            if not renpy.showing(Chr.Tag+"_Doggy"):
                                call expression Chr.Tag + "_Sex_Launch" #call expression Chr.Tag + "_Doggy_Launch"
                            else:
                                call expression Chr.Tag + "_Sex_Reset" #call expression Chr.Tag + "_Doggy_Reset"
                        "Sexpose" if Chr != RogueX:
                            if not renpy.showing(Chr.Tag+"_SexSprite"):
                                call expression Chr.Tag + "_Sex_Launch"
                            else:
                                call expression Chr.Tag + "_Sex_Reset"
                        "Back":
                            jump Wardrobe_Menu
            # Outfits
            "First casual outfit":
                $ Chr.OutfitChange("casual1")
            "Second casual outfit":
                $ Chr.OutfitChange("casual2")
            "Nude":
                $ Chr.OutfitChange("nude")
            "Shirts":
                while True:
                    menu:
                        "Remove [Chr.Over]" if Chr.Over:
                            $ Chr.Over = 0
                        "Add mesh top" if Chr == RogueX:
                            $ Chr.Over = "mesh top"
                            $ Chr.Neck = "spiked collar"
                            $ Chr.Arms = "gloves"
                            if Chr.Chest == "buttoned tank":
                                $ Chr.Chest = "tank"
                        "Add pink top" if Chr == RogueX:
                            $ Chr.Over = "pink top"
                            $ Chr.Arms = "gloves"
                        "Add pink top" if Chr == KittyX:
                            $ Chr.Over = "pink top"
                        "Add red top" if Chr == KittyX or Chr == JubesX:
                            $ Chr.Over = "red shirt"
                        "Add black top" if Chr == JubesX:
                            $ Chr.Over = "black shirt"
                        "Add tube top" if Chr == JubesX:
                            $ Chr.Over = "tube top"
                        "Add pink shirt" if Chr == JeanX:
                            $ Chr.Over = "pink shirt"
                        "Add green shirt" if Chr == JeanX:
                            $ Chr.Over = "green shirt"
                        "Add yellow shirt" if Chr == JeanX:
                            $ Chr.Over = "yellow shirt"
                        "Add jacket":
                            if Chr == JubesX:
                                    $ Chr.Acc = "jacket"
                            else:
                                    $ Chr.Acc = "jacket"
                        "Open/shut jacket" if Chr == JubesX:
                            if Chr.Acc == "jacket":
                                    $ Chr.Acc = "shut jacket"
                            else:
                                    $ Chr.Acc = "jacket"
                        "wide open jacket" if Chr == JubesX:
                            if Chr.Acc == "jacket":
                                    $ Chr.Acc = "open jacket"
                            else:
                                    $ Chr.Acc = "jacket"
                        "Remove jacket" if Chr.Acc == "jacket":
                                    $ Chr.Acc = 0

                        "Add white shirt" if Chr == StormX:
                            $ Chr.Over = "white shirt"
                        "Dress" if Chr == EmmaX:
                            $ Chr.Over = "dress"
                        "Add nighty":
                            $ Chr.Over = "nighty"
                            $ Chr.Arms = 0
                        "Add towel":
                            $ Chr.Over = "towel"
                            $ Chr.Arms = 0
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Toggle up-top":
                            if Chr.Uptop:
                                $ Chr.Uptop = 0
                            else:
                                $ Chr.Uptop = 1
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Back":
                            jump Wardrobe_Menu
            "Bra":
                while True:
                    menu:
                        # Tops
                        "Remove [Chr.Chest]" if Chr.Chest:
                            $ Chr.Chest = 0
                        "Add tank top" if Chr == RogueX:
                            $ Chr.Chest = "tank"
                        "Add sports bra":
                            $ Chr.Chest = "sports bra"
                        "Add leather bra" if Chr == LauraX:
                            $ Chr.Chest = "leather bra"
                        "Add white tank" if Chr == LauraX:
                            $ Chr.Chest = "white tank"
                        "Add buttoned tank top" if Chr == RogueX:
                            $ Chr.Chest = "buttoned tank"
                        "Add lace bra":
                            $ Chr.Chest = "lace bra"
                        "Add cami" if Chr == KittyX:
                            $ Chr.Chest = "cami"
                        "Add dress" if Chr == KittyX:
                            $ Chr.Chest = "dress"
                        "Add wolvie top" if Chr == LauraX:
                            $ Chr.Chest = "wolvie top"
                        "Add green bra" if Chr == JeanX:
                            $ Chr.Chest = "green bra"
                        "Add tube top" if Chr == StormX or Chr == RogueX:
                            $ Chr.Chest = "tube top"
                        "Add bra":
                            if Chr == StormX:
                                    $ Chr.Chest = "black bra"
                            else:
                                    $ Chr.Chest = "bra"
                        "Add cosplay bra" if Chr == StormX:
                            $ Chr.Chest = "cos bra"
                        "Add bikini":
                            $ Chr.Chest = "bikini top"
                        "Add corset":
                            $ Chr.Chest = "corset"
                        "Add lace corset":
                            $ Chr.Chest = "lace corset"
                        "Toggle up-top":
                            if Chr.Uptop:
                                $ Chr.Uptop = 0
                            else:
                                $ Chr.Uptop = 1
                        "Toggle Piercings":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Back":
                            jump Wardrobe_Menu

            "Pants":
                while True:
                    menu:
                        # Legs
                        "Remove legs" if Chr.Legs:
                            $ Chr.Legs = 0
                        "Add Skirt" if Chr != KittyX:
                            $ Chr.Legs = "skirt"
                        "Add cosplay Skirt" if Chr == LauraX:
                            $ Chr.Legs = "other skirt"
                        "Add blue Skirt" if Chr == KittyX:
                            $ Chr.Legs = "blue skirt"
                        "Add pants" if Chr != KittyX:
                            $ Chr.Legs = "pants"
                        "Add black jeans" if Chr == KittyX:
                            $ Chr.Legs = "black jeans"
                        "Add capri pants" if Chr == KittyX:
                            $ Chr.Legs = "capris"
                        "Add shorts" if Chr == KittyX or Chr == JeanX or Chr == JubesX:
                            $ Chr.Legs = "shorts"
                        "Add leather pants" if Chr == LauraX:
                            $ Chr.Legs = "leather pants"
                        "Add yoga pants":
                            $ Chr.Legs = "yoga pants"
                        "Dress" if Chr == EmmaX or Chr == KittyX:
                            $ Chr.Legs = "dress"
                        "Boots" if Chr == EmmaX:
                                $ EmmaX.Acc = "thigh boots" if EmmaX.Acc != "thigh boots" else 0
                        "Toggle upskirt":
                            if Chr.Upskirt:
                                $ Chr.Upskirt = 0
                            else:
                                $ Chr.Upskirt = 1
                        "pull down-up panties":
                            if Chr.PantiesDown:
                                $ Chr.PantiesDown = 0
                            else:
                                $ Chr.PantiesDown = 1
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Toggle Wetness":
                            if not Chr.Wet:
                                $ Chr.Wet = 1
                            elif Chr.Wet == 1:
                                $ Chr.Wet = 2
                            else:
                                $ Chr.Wet  = 0
                        "Back":
                            jump Wardrobe_Menu

            "Panties & Hose":
                while True:
                    menu:
                        # Underwear
                        "Hose":
                            menu:
                                "Add hose":
                                    $ Chr.Hose = "stockings"
                                "Add garter":
                                    $ Chr.Hose = "garterbelt"
                                "Add stockings and garter":
                                    $ Chr.Hose = "stockings and garterbelt"
                                "Add pantyhose":
                                    $ Chr.Hose = "pantyhose"
                                "Add tights":
                                    $ Chr.Hose = "tights"
                                "Add ripped hose":
                                    $ Chr.Hose = "ripped pantyhose"
                                "Add ripped tights":
                                    $ Chr.Hose = "ripped tights"
                                "Add tights":
                                    $ Chr.Hose = "tights"
                                "Add knee stockings" if Chr == KittyX:
                                    $ Chr.Hose = "knee stockings"
                                "Add socks" if Chr == JubesX:
                                    $ Chr.Hose = "socks"
                                "Add black stockings" if Chr == LauraX:
                                    $ Chr.Hose = "black stockings"
                                "Remove hose" if Chr.Hose:
                                    $ Chr.Hose = 0
                        "Remove panties" if Chr.Panties:
                            $ Chr.Panties = 0
                        "Add black panties":
                            $ Chr.Panties = "black panties"
                        "Add white panties" if Chr == StormX or Chr == EmmaX:
                            $ Chr.Panties = "white panties"
                        "Add cosplay panties" if Chr == StormX:
                            $ Chr.Panties = "cos panties"
                        "Add bikini":
                            $ Chr.Panties = "bikini bottoms"
                        "Add shorts":
                            $ Chr.Panties = "shorts"
                        "Add green panties":
                            $ Chr.Panties = "green panties"
                        "Add lace panties":
                            $ Chr.Panties = "lace panties"
                        "Add wolvie panties" if Chr == LauraX:
                            $ Chr.Panties = "wolvie panties"
                        "Add sports panties" if Chr == EmmaX:
                            $ Chr.Panties = "sports panties"
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "pull down-up panties":
                            if Chr.PantiesDown:
                                $ Chr.PantiesDown = 0
                            else:
                                $ Chr.PantiesDown = 1
                        "Toggle Wetness":
                            if not Chr.Wet:
                                $ Chr.Wet = 1
                            elif Chr.Wet == 1:
                                $ Chr.Wet = 2
                            else:
                                $ Chr.Wet  = 0
                        "Back":
                            jump Wardrobe_Menu
            "Misc":
                while True:
                    menu:
                        "Emotions":
                            call EmotionEditor(Chr)
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Toggle Wetness":
                            if not Chr.Wet:
                                $ Chr.Wet = 1
                            elif Chr.Wet == 1:
                                $ Chr.Wet = 2
                            else:
                                $ Chr.Wet  = 0
                        "Toggle wet look":
                            if not Chr.Water:
                                $ Chr.Water = 1
                            elif Chr.Water == 1:
                                $ Chr.Water = 3
                            else:
                                $ Chr.Water  = 0
                        "Toggle pubes":
                            if not Chr.Pubes:
                                $ Chr.Pubes = 1
                            else:
                                $ Chr.Pubes = 0
                        "Toggle Short Hair" if Chr == KittyX:
                            if Chr.Hair == "long":
                                $ Chr.Hair = "evo"
                            else:
                                $ Chr.Hair = "long"
                        "Toggle Mohawk" if Chr == StormX:
                            if Chr.Hair == "long":
                                $ Chr.Hair = "mohawk"
                            else:
                                $ Chr.Hair = "long"
                        "Toggle Short Hair" if Chr == StormX:
                            if Chr.Hair == "long":
                                $ Chr.Hair = "short"
                            else:
                                $ Chr.Hair = "long"
                        "Toggle Ponytailr" if Chr == JeanX:
                            if Chr.Hair == "pont":
                                $ Chr.Hair = "short"
                            else:
                                $ Chr.Hair = "pony"
                        "Toggle Hat" if Chr == EmmaX:
                            if Chr.Hair == "wavy":
                                $ Chr.Hair = "hat"
                            elif Chr.Hair == "wet":
                                $ Chr.Hair = "hat wet"
                            elif Chr.Hair == "hat wet":
                                $ Chr.Hair = "wet"
                            else:
                                $ Chr.Hair = "wavy"
                        "Cosplay Hair" if Chr == RogueX:
                            if Chr.Hair == "cosplay":
                                $ Chr.Hair = "evo"
                            else:
                                $ Chr.Hair = "cosplay"
                        "Ponytail Hair" if Chr == JeanX:
                            if Chr.Hair == "pony":
                                $ Chr.Hair = "short"
                            else:
                                $ Chr.Hair = "pony"
                        "Toggle held":
                            if not Chr.Held:
                                $ Chr.Held  = "phone"
                            elif Chr.Held == "phone":
                                $ Chr.Held  = "dildo"
                            elif Chr.Held == "dildo":
                                $ Chr.Held  = "vibrator"
                            elif Chr.Held == "vibrator":
                                $ Chr.Held  = "panties"
                            else:
                                $ Chr.Held  = 0
                        "Toggle gold Necklace" if Chr == StormX:
                            if not Chr.Neck:
                                $ Chr.Neck = 'gold'
                            else:
                                $ Chr.Neck = 0
                        "Toggle flower Necklace":
                            if not Chr.Neck:
                                $ Chr.Neck = 'flower necklace'
                            else:
                                $ Chr.Neck = 0
                        "Toggle ring Necklace" if Chr == StormX:
                            if not Chr.Neck:
                                $ Chr.Neck = 'rings'
                            else:
                                $ Chr.Neck = 0
                        "Toggle Rings" if Chr == StormX:
                            if not Chr.Acc:
                                $ Chr.Acc = 'rings'
                            else:
                                $ Chr.Acc = 0
                        "Toggle choker" if Chr == EmmaX or Chr == RogueX:
                            if Chr.Neck != 'choker':
                                $ Chr.Neck ='choker'
                            else:
                                $ Chr.Neck = 0
                        "Toggle boots" if Chr == EmmaX:
                            if Chr.Acc != "thigh boots":
                                $ Chr.Acc ='thigh boots'
                            else:
                                $ Chr.Acc = 0
                        "Toggle sweater" if Chr == RogueX:
                            if Chr.Acc != "sweater":
                                $ Chr.Acc ='sweater'
                            else:
                                $ Chr.Acc = 0
                        "Toggle suspenders" if Chr == LauraX or Chr == JeanX:
                            if Chr.Acc == "suspenders":
                                $ Chr.Acc = "suspenders2"
                            elif Chr.Acc == "suspenders2":
                                $ Chr.Acc = 0
                            else:
                                $ Chr.Acc = "suspenders"
                        "Spunk Level":
                            menu:
                                "Mouth":
                                    if "mouth" in Chr.Spunk:
                                        $ Chr.Spunk.remove("mouth")
                                    else:
                                        $ Chr.Spunk.append("mouth")
                                "Chin":
                                    if "chin" in Chr.Spunk:
                                        $ Chr.Spunk.remove("chin")
                                    else:
                                        $ Chr.Spunk.append("chin")
                                "Facial":
                                    if "facial" in Chr.Spunk:
                                        $ Chr.Spunk.remove("facial")
                                    else:
                                        $ Chr.Spunk.append("facial")
                                "Hair":
                                    if "hair" in Chr.Spunk:
                                        $ Chr.Spunk.remove("hair")
                                    else:
                                        $ Chr.Spunk.append("hair")
                                "Tits":
                                    if "tits" in Chr.Spunk:
                                        $ Chr.Spunk.remove("tits")
                                    else:
                                        $ Chr.Spunk.append("tits")
                                "Belly":
                                    if "belly" in Chr.Spunk:
                                        $ Chr.Spunk.remove("belly")
                                    else:
                                        $ Chr.Spunk.append("belly")
                                "Back":
                                    if "back" in Chr.Spunk:
                                        $ Chr.Spunk.remove("back")
                                    else:
                                        $ Chr.Spunk.append("back")
                                "Pussy":
                                    if "in" in Chr.Spunk:
                                        $ Chr.Spunk.remove("in")
                                    else:
                                        $ Chr.Spunk.append("in")
                                "Ass":
                                    if "anal" in Chr.Spunk:
                                        $ Chr.Spunk.remove("anal")
                                    else:
                                        $ Chr.Spunk.append("anal")
                                "Return":
                                    pass
                        "Toggle Pierce":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Add Gloves" if not Chr.Arms:
                            $ Chr.Arms = "gloves"
                        "Remove Gloves" if Chr.Arms:
                            $ Chr.Arms = 0
                        "Back":
                            jump Wardrobe_Menu
            "Nothing":
                return
    return

label Clothing_Schedule_Check(Girl=0,Changed=0,Value=0,Count=0):
        #this clears out clothing items that are out of date.
        #call Clothing_Schedule_Check("Rogue",3,1)

        # Girl is the checked girl, "changed" is the outfit to compare against
        # Value defaults to 0, but if set, it will only check if the value is not 2.
        # (0-6) = Mon-Sun, (7) Datewear, (8) Teach, (9) Private (skips this one)
        # R_Schedule = [0,0,0,0,0,0,0,0,0,0]
        # Custom1=3,Cusotm2=5,Custom3=6,Gym=4,Sleep=7,Swim=10
        while Count < 9:
            if Girl.Clothing[Count] == Changed:
                    if Value:
                        #if the Outfit is custom1, and the outfit is SFW, then leave it alone.
                        if Girl.Clothing[Count] == 3 and Girl.Custom1[0] == 2:
                                pass
                        elif Girl.Clothing[Count] == 5 and Girl.Custom2[0] == 2:
                                pass
                        elif Girl.Clothing[Count] == 6 and Girl.Custom3[0] == 2:
                                pass
                        elif Girl.Clothing[Count] == 4 and Girl.Gym[0] != 1:
                                pass
                        else:
                            $ Girl.Clothing[Count] = 0
                    else:
                            $ Girl.Clothing[Count] = 0
            $ Count += 1
        return

label Emergency_Clothing_Reset: #rkeljsv
        "This resets all customized clothing to their defaults."
        menu:
            "Do you want to continue?"
            "Yes":
                    $ RogueX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Casual1 = [2,"gloves","skirt","mesh top","spiked collar","tank","black panties",0,0,"tights",0]
                    $ RogueX.Casual2 = [2,"gloves","pants","pink top","spiked collar","buttoned tank","black panties",0,0,0,0]
                    $ RogueX.Gym = [0,"gloves",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                    $ RogueX.Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0,0]
                    $ RogueX.Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0]
                    $ RogueX.Costume = [2,"gloves","skirt",0,0,"tube top","black panties","sweater","cosplay",0,0]
                    $ RogueX.Clothing = [0,0,0,0,0,0,0,0,0,0]   #chooses when she wears what
                    $ RogueX.Outfit = "casual1"
                    $ RogueX.OutfitDay = "casual1"

                    $ KittyX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Casual1 = [2,0,"capris","pink top","gold necklace","cami","green panties",0,0,0,0]
                    $ KittyX.Casual2 = [2,0,"black jeans","red shirt",0,"bra","green panties",0,0,0,0]
                    $ KittyX.Gym = [0,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
                    $ KittyX.Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0,0]
                    $ KittyX.Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0]
                    $ KittyX.Costume = [2,0,"dress","jacket","flower necklace","dress","lace panties",0,0,0,0]
                    $ KittyX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Outfit = "casual1"
                    $ KittyX.OutfitDay = "casual1"

                    $ EmmaX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Casual1 = [2,0,"pants","jacket","choker","corset","white panties",0,0,0,0]
                    $ EmmaX.Casual2 = [2,"gloves","pants",0,"choker","corset","white panties",0,0,0,0]
                    $ EmmaX.Gym = [0,0,0,0,0,"sports bra","sports panties",0,0,0,0]
                    $ EmmaX.Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0,0]
                    $ EmmaX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    $ EmmaX.Costume =  [2,"gloves","dress","dress","choker",0,"lace panties",0,"hat","stockings and garterbelt",0]
                    $ EmmaX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Outfit = "casual1"
                    $ EmmaX.OutfitDay = "casual1"

                    $ LauraX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Casual1 = [2,"wrists","leather pants",0,"leash choker","leather bra","black panties",0,0,0,0]
                    $ LauraX.Casual2 = [2,0,"skirt","jacket","leash choker","leather bra","black panties",0,0,0,0]
                    $ LauraX.Gym = [0,"wrists","leather pants",0,0,"leather bra","black panties",0,0,0,0]
                    $ LauraX.Sleepwear = [0,0,0,0,0,"leather bra","leather panties",0,0,0,0]
                    $ LauraX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    $ LauraX.Costume = [2,"gloves","other skirt",0,0,"white tank","black panties","suspenders",0,"black stockings",0]
                    $ LauraX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Outfit = "casual1"
                    $ LauraX.OutfitDay = "casual1"

                    $ JeanX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Casual1 = [2,0,"pants","pink shirt",0,"green bra","green panties",0,0,0,0]
                    $ JeanX.Casual2 = [2,0,"skirt","green shirt",0,"green bra","green panties",0,0,0,0]
                    $ JeanX.Gym = [0,0,"yoga pants",0,0,"sports bra","green panties",0,0,0,0]
                    $ JeanX.Sleepwear = [0,0,0,"pink shirt",0,"green bra","green panties",0,0,0,0]
                    $ JeanX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    $ JeanX.Costume =  [2,0,"shorts","yellow shirt",0,"green bra","green panties","suspenders","pony",0,0]
                    $ JeanX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ JeanX.Outfit = "casual1"
                    $ JeanX.OutfitDay = "casual1"

                    $ StormX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Casual1 = [2,0,"skirt","white shirt",0,"black bra","white panties",0,0,0,0]
                    $ StormX.Casual2 = [2,0,"pants","jacket",0,"tube top","white panties",0,0,0,0]
                    $ StormX.Gym = [0,0,"yoga pants",0,0,"sports bra","white panties",0,0,0,10]
                    $ StormX.Sleepwear = [0,0,0,"white shirt",0,0,"white panties",0,0,0,25]
                    $ StormX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    $ StormX.Costume = [2,0,0,0,"ring necklace","cos bra","cos panties","rings","short",0,0]
                    $ StormX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ StormX.Outfit = "casual1"
                    $ StormX.OutfitDay = "casual1"

                    $ JubesX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Casual1 = [2,0,"shorts","red shirt",0,"sports bra","blue panties","jacket",0,0,0]
                    $ JubesX.Casual2 = [2,0,"pants","black shirt",0,"sports bra","blue panties","jacket",0,0,0]
                    $ JubesX.Gym = [0,0,"pants",0,0,"sports bra","blue panties",0,0,0,10]
                    $ JubesX.Sleepwear = [0,0,0,0,0,"sports bra","blue panties",0,0,0,25]
                    $ JubesX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    $ JubesX.Costume = [0,0,"pants","black shirt",0,"sports bra","blue panties","jacket",0,0,0]
                    $ JubesX.Clothing = [0,0,0,0,0,0,0,0,0,0]
                    $ JubesX.Outfit = "casual1"
                    $ JubesX.OutfitDay = "casual1"

                    "Done."
                    "You will now need to set their custom outfits again."
            "No":
                pass
        return

label Clothes_Schedule(Girl=0,Cnt = 0): #rkeljsv
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        #Schedule 0-6= mon-fri, Schedule 7 is dates, 9 is private
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if Girl == RogueX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_r "So, you'd like to choose what I wear for the week? Ok, shoot."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_r "I guess I could set aside a few schooldays for you."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_r "We can talk about what I wear outside of classes."
                        $ Cnt = 1
                else:
                        ch_r "You know, I don't really need fashion advice from you."
                        return
        elif Girl == KittyX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_k "Let me know what you like."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_k "I could let you pick a few days. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_k "We could talk about weekends, maybe. . ."
                        $ Cnt = 1
                else:
                        ch_k "I think I'll[Girl.like]figure out my own outfits."
                        return
        elif Girl == EmmaX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_e "I'm open to suggestions."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_e "I could let you choose a few days. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_e "Perhaps when I'm off the clock. . ."
                        $ Cnt = 1
                else:
                        ch_e "I'd prefer to handle my own wardrobe."
                        return
        elif Girl == LauraX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_l "Fine, you pick, whatever."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_l "I don't know, you could pick a few days. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_l "Maybe on weekends. . ."
                        $ Cnt = 1
                else:
                        ch_l "Nah, I got it covered."
                        return
        elif Girl == JeanX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_j "Ok, I'm tired of having to pick outfits. . ."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_j "I guess you do have some taste. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_j "I guess my weekends are free. . ."
                        $ Cnt = 1
                else:
                        ch_j "Huh? No."
                        return
        elif Girl == StormX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_s "I'm willing to listen."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_s "I suppose you could choose a few days. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_s "Perhaps when I'm not working. . ."
                        $ Cnt = 1
                else:
                        ch_s "I think I'd rather choose my own clothing."
                        return
        elif Girl == JubesX:
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_v "What're you thinking?"
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_v "You could help with a few days?"
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_v "I don't know, weekends maybe?"
                        $ Cnt = 1
                else:
                        ch_v "Nah, I'll figure it out myself."
                        return
        while True:
            menu:
                    extend ""
                    "Every Day":
                        "This sets her outfit for every day of the week in one go."
                        "This overwrites the default schedule, and any scheduling you've already made."
                        "Any choices you make later will overwrite this choice."
                        menu:
                            "Pick an outfit to wear":
                                call Clothes_ScheduleB
                                if Cnt > 1:
                                        $ Girl.Clothing[0] = _return
                                        $ Girl.Clothing[2] = _return
                                        $ Girl.Clothing[4] = _return
                                if Cnt > 2:
                                        $ Girl.Clothing[1] = _return
                                        $ Girl.Clothing[3] = _return
                                $ Girl.Clothing[5] = _return
                                $ Girl.Clothing[6] = _return
                            "Never mind.":
                                pass
                    "Weekdays":
                        menu:
                            "On Monday you should wear. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[0] = _return
                            "On Monday you should wear. . . (locked)" if Cnt <= 1:
                                pass

                            "On Tuesday you should wear. . ." if Cnt > 2:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[1] = _return
                            "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                                pass

                            "On Wednesday you should wear. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[2] = _return
                            "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                                pass

                            "On Thursday you should wear. . ." if Cnt > 2:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[3] = _return
                            "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                                pass

                            "On Friday you should wear. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[4] = _return
                            "On Friday you should wear. . . (locked)" if Cnt <= 1:
                                pass
                            "Back":
                                pass
                    "Other":
                        menu:
                            "On Saturday you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On Saturday you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[5] = _return

                            "On Sunday you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On Sunday you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[6] = _return

                            "In our rooms you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "In our rooms you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB(Girl,99)
                                $ Girl.Clothing[9] = _return

                            "On dates you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On dates you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[7] = _return

                            "When teaching you should wear. . . (locked)" if Girl in (EmmaX,StormX) and Cnt < 3:
                                pass
                            "When teaching you should wear. . ." if Girl in (EmmaX,StormX) and Cnt >= 3:
                                call Clothes_ScheduleB(Girl,90)
                                $ Girl.Clothing[8] = _return

                            "Back":
                                pass

                    "About Gym clothes":
                        menu:
                            ch_p "You asked me before about your gym clothes?"
                            "Don't ask before changing into gym clothes" if "no ask gym" not in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.append("no ask gym")
                            "Ask me before changing into gym clothes" if "no ask gym" in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.remove("no ask gym")
                            "Never Mind":
                                pass

                    "Private outfit" if Girl.Clothing[9]:
                                #if comfy is in LauraX.Traits, she won't ask before changing
                                ch_p "You know that outfit you wear in private?"
                                if Girl in (EmmaX,StormX):
                                        call AnyLine(Girl,"Yes?")
                                else:
                                        call AnyLine(Girl,"Yeah?")
                                menu:
                                    extend ""
                                    "Just put them on without asking me about it." if "comfy" not in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.append("comfy")
                                    "Ask before changing into that." if "comfy" in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.remove("comfy")
                                    "Never Mind":
                                        pass

                    "Never mind [[Done]":
                        return
        jump Clothes_Schedule

label Clothes_ScheduleB(Girl=0,Count = 0): #rkeljsv
        #This is called by Clothes_Schedule when setting her outfit for a given day
        #If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes, if 90 it's for Emma teaching
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)
        menu:
            "Your green outfit." if Girl == RogueX:
                $ Count = 1
            "That pink outfit, with the jeans." if Girl == RogueX:
                $ Count = 2

            "That pink outfit, with the jeans." if Girl == KittyX:
                $ Count = 1
            "Your red shirt outfit." if Girl == KittyX:
                $ Count = 2

            "That teacher outfit." if Girl == EmmaX:
                $ Count = 1
            "Your superhero outfit." if Girl == EmmaX:
                $ Count = 2

            "That leather combat look." if Girl == LauraX:
                $ Count = 1
            "Your jacket and skirt." if Girl == LauraX:
                $ Count = 2

            "That pink shirt and khakis look." if Girl == JeanX:
                $ Count = 1
            "Your green shirt and skirt." if Girl == JeanX:
                $ Count = 2

            "That white top and skirt look." if Girl == StormX:
                $ Count = 1
            "Your black jacket and pants look." if Girl == StormX:
                $ Count = 2

            "That red and blue look." if Girl == JubesX:
                $ Count = 1
            "Your black top and pants look." if Girl == JubesX:
                $ Count = 2

            "That outfit we put together [[custom]":
                        if Girl == RogueX:
                                ch_r "Which one again?"
                        elif Girl == KittyX:
                                ch_k "[Girl.Like]which?"
                        elif Girl == EmmaX:
                                ch_e "Which were you thinking?"
                        elif Girl == LauraX:
                                ch_l "Which one?"
                        elif Girl == JeanX:
                                ch_j "What outfit?"
                        elif Girl == StormX:
                                ch_s "Which did you mean?"
                        elif Girl == JubesX:
                                ch_v "Which one?"
                        menu:
                            extend ""
                            "The first one. (locked)" if not Girl.Custom1[0]:
                                        pass
                            "The first one." if Girl.Custom1[0]:
                                        if Girl.Custom1[0] == 2 or Count == 99:
                                            $ Count = 3
                                        else:
                                            call AnyLine(Girl,"Well. . .")
                                            call QuickOutfitCheck(Girl,3) #re-checks ot see if it will work
                                            if Girl.Custom1[0] == 2:
                                                    $ Count = 3
                                            else:
                                                    $ Line = "no"
                            "The second one. (locked)" if not Girl.Custom2[0]:
                                        pass
                            "The second one." if Girl.Custom2[0]:
                                        if Girl.Custom2[0] == 2 or Count == 99:
                                            $ Count = 5
                                        else:
                                            call AnyLine(Girl,"Well. . .")
                                            call QuickOutfitCheck(Girl,5)  #re-checks ot see if it will work
                                            if Girl.Custom2[0] == 2:
                                                    $ Count = 5
                                            else:
                                                    $ Line = "no"
                            "The third one. (locked)" if not Girl.Custom3[0]:
                                        pass
                            "The third one." if Girl.Custom3[0]:
                                        if Girl.Custom3[0] == 2 or Count == 99:
                                            $ Count = 6
                                        else:
                                            call AnyLine(Girl,"Well. . .")
                                            call QuickOutfitCheck(Girl,6) #re-checks ot see if it will work
                                            if Girl.Custom3[0] == 2:
                                                    $ Count = 6
                                            else:
                                                    $ Line = "no"
                            "Never mind":
                                        pass
                        if Line == "no":
                                if Girl == RogueX:
                                        ch_r "No, I'm not wearing that outside, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "I'm[Girl.like]definitely not wearing that one out."
                                elif Girl == EmmaX:
                                        ch_e "I'm certainly not wearing that one in public."
                                elif Girl == LauraX:
                                        ch_l "I won't wear that out."
                                elif Girl == JeanX:
                                        ch_j "Yeah, I wouldn't be caught out in that."
                                elif Girl == StormX:
                                        ch_s "I cannot wear that one in public."
                                elif Girl == JubesX:
                                        ch_v "That one's private. . ."
                                $ Line = 0
                        else:
                                call AnyLine(Girl,"Fine. . .")

            "Your gym clothes.":
                if Count == 90:
                    call AnyLine(Girl,"Not in class, "+Girl.Petname+".")
                    $ Count = 0
                else:
                    $ Count = 4
            "Your sleepwear.":
                if Count == 99:
                    $ Count = 7
                else:
                    call AnyLine(Girl,"Well. . .")
                    call QuickOutfitCheck(Girl,7)  #re-checks ot see if it will work
                    if Girl.Custom1[0] == 2:
                            $ Count = 7
                            call AnyLine(Girl,"Fine. . .")
                    else:
                            if Girl == RogueX:
                                    ch_r "I don't know about that, [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "That's not really appropriate, [Girl.Petname]."
                            elif Girl == EmmaX:
                                    ch_e "I don't think that would be appropriate, [Girl.Petname]."
                            elif Girl == LauraX:
                                    ch_l "That's kinda skimpy, [Girl.Petname]."
                            elif Girl == JeanX:
                                    ch_j "I -sleep- in that, I don't wear it out."
                            elif Girl == StormX:
                                    ch_s "That's more sleepwear than casual wear."
                            elif Girl == JubesX:
                                    ch_v "That's for sleeping in, not going out. . ."
                            $ Count = 0
            "Whatever you like.":
                pass

        if Girl == RogueX:
                if Count:
                        ch_r "Ok, sure, I'll wear that."
                else:
                        ch_r "I'll just wear whatever then."
        elif Girl == KittyX:
                if Count:
                        ch_k "Ok, sure, I'll wear that."
                else:
                        ch_k "I'll just wear whatever then."
        elif Girl == EmmaX:
                if Count:
                        ch_e "Very well."
                else:
                        ch_e "I'll wear something else instead."
        elif Girl == LauraX:
                if Count:
                        ch_l "Ok, sure."
                else:
                        ch_l "I'll figure something else out."
        elif Girl == JeanX:
                if Count:
                        ch_j "Ok, fine."
                else:
                        ch_j "I've got my own plans."
        elif Girl == StormX:
                if Count:
                        ch_s "I will wear it."
                else:
                        ch_s "I will choose something else instead. . ."
        elif Girl == JubesX:
                if Count:
                        ch_v "I'd wear it."
                else:
                        ch_v "I'll pick something else. . ."
        return Count

label AltClothes(Girl=0,Outfit=1):
        #1 = "casual1", 2 = "casual2"
        #3 = "custom1", 5 = "custom2", 6 = "custom3", 7 = "sleep", 4 = "gym", 10 = "swimwear"
        #This selects her outfit when teaching if 8
        #This selects her private outfit if 9
        $ Girl = GirlCheck(Girl)

        if Girl.Clothing[Outfit] == 1 or not Girl.Clothing[Outfit]:
                    $ Girl.Outfit = "casual1"
        elif Girl.Clothing[Outfit] == 2:
                    $ Girl.Outfit = "casual2"
        elif Girl.Clothing[Outfit] == 3:
                    $ Girl.Outfit = "custom1"
        elif Girl.Clothing[Outfit] == 5:
                    $ Girl.Outfit = "custom2"
        elif Girl.Clothing[Outfit] == 6:
                    $ Girl.Outfit = "custom3"
        elif Girl.Clothing[Outfit] == 7:
                    $ Girl.Outfit = "sleep"
        elif Girl.Clothing[Outfit] == 4:
                    $ Girl.Outfit = "gym"
        elif Girl.Clothing[Outfit] == 10:
                    $ Girl.Outfit = "swimwear"
        else:
                    $ Girl.Outfit = "casual1"
        return

label Private_Outfit(Girl=0): #rkeljsv
        #sets Girl's private outfit in private
        $ Girl = GirlCheck(Girl)
        if Girl.Break[0] or "angry" in Girl.DailyActions:
                return
        if Girl.Outfit == "temporary" or not Girl.Clothing[9]:
                #if you manually set a different option, keep it
                #if no alternate is set, return
                return
        if "comfy" in Girl.RecentActions or "comfy" in Girl.Traits or Girl.Outfit == Girl.Clothing[9]:
                call AltClothes(Girl,9)
                $ Girl.OutfitChange(Changed=1)
        elif "no comfy" in Girl.RecentActions:
                pass
        elif ApprovalCheck(Girl, 1200, "LI") and (2 * Girl.Inbt) >= (Girl.Love + Girl.Obed +100):
                # if her inhibition is much higher than her obedience to you. . .
                call Shift_Focus(Girl)
                if Girl == RogueX:
                        ch_r "Be right there [Girl.Petname]. . ."
                        ch_r "I'm slippin' inta somethin' more comfortable. . ."
                elif Girl == KittyX:
                        ch_k "Gimme a sec. . ."
                        ch_k "I'm throwing on something a bit more. . . fun."
                elif Girl == EmmaX:
                        ch_e "I'll be just a moment. . ."
                        ch_e "I'll just slip into something more comfortable. . ."
                elif Girl == LauraX:
                        ch_l "One minute. . ."
                        ch_l "I'm getting a bit more comfortable."
                elif Girl == JeanX:
                        ch_j "Let me get changed. . ."
                elif Girl == StormX:
                        ch_s "Give me one moment. . ."
                        ch_s "I need to change into something more comfortable. . ."
                elif Girl == JubesX:
                        ch_v "Gimme a minute. . ."
                        ch_v "I wanna slip something else on. . ."
                call AltClothes(Girl,9)
                $ Girl.OutfitChange(Changed=1)
                $ Girl.RecentActions.append("comfy")
        else:
                call Shift_Focus(Girl)
                if Girl == RogueX:
                        ch_r "Be right there [Girl.Petname]. . ."
                        menu:
                            ch_r "Should I throw on somethin' more comfortable?"
                            "Sure.":
                                    ch_r "Love to. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_r "Suit yourself."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl == KittyX:
                        ch_k "Gimme a sec. . ."
                        menu:
                            ch_k "Want me to wear something more fun?"
                            "Sure.":
                                    ch_k "Hehe. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_k "Oh, ok."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl == EmmaX:
                        ch_e "I'll be just a moment. . ."
                        menu:
                            ch_e "Would you like me to change into something more comfortable?"
                            "Sure.":
                                    ch_e "Lovely. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_e "Very well."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl == LauraX:
                        ch_l "One minute. . ."
                        menu:
                            ch_l "I could throw on something a bit more fun. . ."
                            "Sure.":
                                    ch_l "Cool. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_l "Oh, ok."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl == JeanX:
                        menu:
                            ch_j "I do have a more fun look. . ."
                            "Sure.":
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_j "Huh. Ok. . ."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl == StormX:
                        ch_s "I'll be just a moment. . ."
                        menu:
                            ch_s "Would you like me to change into something more comfortable?"
                            "Sure.":
                                    ch_s "Excellent. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_s "Very well."
                                    $ Girl.RecentActions.append("no comfy")
                elif Girl == JubesX:
                        ch_v "Gimme a minute. . ."
                        menu:
                            ch_v "Hey, how'bout I throw something. . . nice on?"
                            "Sure.":
                                    ch_v "Cool. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_v "Ok, fine."
                                    $ Girl.RecentActions.append("no comfy")
        return

label Custom_Out(Girl=0,Custom = 3, Shame = 0, Agree = 0): #rkeljsv
        #If Custom1 = 3, if custom2 = 5, if custom3 = 6
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)
        $ Girl.FaceChange("sexy", 1)

        if Custom == 3:
                $ Shame = Girl.Custom1[10]
                if Girl.Custom1[0] == 2 or "exhibitionist" in Girl.Traits: #if custom 1:
                        $ Girl.Outfit = "custom1"
                        $ Agree = 1
                else:
                        call QuickOutfitCheck(Girl,3) #re-checks ot see if it will work
                        if Girl.Custom1[0] == 2:
                                $ Girl.Outfit = "custom1"
                                $ Agree = 1
        elif Custom == 5:
                $ Shame = Girl.Custom2[10]
                if Girl.Custom2[0] == 2 or "exhibitionist" in Girl.Traits:
                        $ Girl.Outfit = "custom2"
                        $ Agree = 1
                else:
                        call QuickOutfitCheck(Girl,5) #re-checks ot see if it will work
                        if Girl.Custom2[0] == 2:
                                $ Girl.Outfit = "custom2"
                                $ Agree = 1
        else: #if Custom == 6:
                $ Shame = Girl.Custom3[10]
                if Girl.Custom3[0] == 2 or "exhibitionist" in Girl.Traits:
                        $ Girl.Outfit = "custom3"
                        $ Agree = 1
                else:
                        call QuickOutfitCheck(Girl,6) #re-checks ot see if it will work
                        if Girl.Custom3[0] == 2:
                                $ Girl.Outfit = "custom3"
                                $ Agree = 1

        if Girl == RogueX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_r "Ooo, momma likes."
                        elif Shame >= 50:
                            ch_r "You realize I'm pretty much naked here, right?"
                        elif Shame >= 25:
                            ch_r "This is pretty shameless. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_r "I don't know, I guess I could try it. . ."
                        else:
                            ch_r "Sure, [Girl.Petname], that one's nice."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_r "Come on, I'd be totally nude!"
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_r "You're lucky I show {i}you{/i} this."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_r "It's kind of daring for me, sorry."
        elif Girl == KittyX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_k "Hmm, I'm getting excited. . ."
                        elif Shame >= 50:
                            ch_k "This is. . . kinda slutty. . . but. . ."
                        elif Shame >= 25:
                            ch_k "I'm not really comfortable with this one. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_k "I'll give it a shot. . ."
                        else:
                            ch_k "Yeah, I like that one too."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_k "You have GOT to be kidding me here."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_k "This is just between us."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_k "I can't wear this out!"
        elif Girl == EmmaX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_e "Hmm, I'm getting excited. . ."
                        elif Shame >= 50:
                            ch_e "This is rather. . . shameless. . ."
                        elif Shame >= 25:
                            ch_e "I'm a bit uncomfortable with this one. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_e "I'll try it. . ."
                        else:
                            ch_e "Yeah, I like that one too."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "You have GOT to be kidding me here."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "This is just between us."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_e "I can't wear this out!"
        elif Girl == LauraX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_l "Mmmmmm. . ."
                        elif Shame >= 50:
                            ch_l "This is. . . really brave. . ."
                        elif Shame >= 25:
                            ch_l "This one's pretty skimpy. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_l "Yeah, ok. . ."
                        else:
                            ch_l "Yup."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_l "Perv."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_l "Yeah, not in public."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_l "Nah."
        elif Girl == JeanX:
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_j ". . ."
                        elif Shame >= 50:
                            ch_j "Pretty daring. . ."
                        elif Shame >= 25:
                            ch_j "Kinda skimpy. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_j "Sure, whatever. . ."
                        else:
                            ch_j "Sure."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_j "Gross."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_j "You wish."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_j "No way."
        elif Girl == StormX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_s "Oooh. . ."
                        elif Shame >= 25:
                            ch_s "You are going to get me into trouble. . ."
                        else:
                            ch_s "Yes, this will do nicely."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_s "I am afraid cannot wear this out."
        elif Girl == JubesX:
                $ Girl.FaceChange("bemused", 1)
                if Agree:
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame
                        if "exhibitionist" in Girl.Traits:
                            ch_s "Oooh. . ."
                        elif Shame >= 25:
                            ch_s "Whew, this is flat out pornographic. . ."
                        else:
                            ch_s "Oh, yeah, this'll do. . ."
                else:
                        #She's decided not to wear this out
                        $ Girl.FaceChange("bemused", 1)
                        ch_s "I really can't wear this one out. . ."
        return

label OutfitShame(Girl=0, Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1): #rkeljsv
        #Custom determines which custom outfit is being checked against.
        #If Custom1 = 3, if gym = 4, if custom2 = 5, if custom3 = 6,  if sleepwear 7, if classwear 8, if private = 9, if swimsuit = 10
        #if not a check, then it is only applied if it's in a taboo area
        # Custom = 20 means it is just re-setting the current Shame level to be accurate.
        # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
        # call OutfitShame(RogueX,20)
        $ Girl = GirlCheck(Girl)

        if not Check and not Taboo and not Girl.Taboo and Custom != 20:
                #if this is not a custom check and you're in a safe space,
                if Girl.Clothing[9] and bg_current in PersonalRooms:
                        #if there is a "private outfit" set, ask to change. (skips if halloween)
                        if "halloween" not in Player.DailyActions:
                                call Private_Outfit
                return

        if Girl.ChestNum() >= 5:   #Outerwear
                $ Count = 20
        elif Girl.ChestNum() >= 4: #Semi-Outerwear
                $ Count = 15
        elif Girl.ChestNum() >= 3: #Opaque Underwear
                $ Count = 10
        elif Girl.ChestNum() >= 2: #Lace
                $ Count = 5
        else:
                $ Count = 0

        #If she's wearing an overshirt

        if Custom == 20 and Girl.Uptop:
                $ Count = 0
        elif Girl.OverNum() >= 5: #Outerwear
                $ Count += 20
        elif Girl.OverNum() >= 4: #Open-Outerwear
                $ Count += 15
        elif Girl.OverNum() >= 3: #Opaque Underwear
                $ Count += 10
        elif Girl.OverNum() >= 2: #Lace/mesh
                $ Count += 5
        #else:
                #nothing

        if Girl.Pierce and Count <= 10:
                $ Count = -5

        $ Girl.FaceChange("sexy", 0)
        if Custom == 9 or Custom == 7:
            pass
        elif Count >= 20:
            $ Count = 20
            if Check:
                if Girl == RogueX:
                        ch_r "Oh, I think this top combination works."
                elif Girl == KittyX:
                        ch_k "This is[Girl.like]totally a cute top."
                elif Girl == EmmaX:
                        ch_e "This is a fashionable top."
                elif Girl == LauraX:
                        ch_l "This top works."
                elif Girl == JeanX:
                        ch_j "The top is fine."
                elif Girl == StormX:
                        ch_s "The top is fine."
                elif Girl == JubesX:
                        ch_v "Yeah, the top'll work. . ."
        elif not Check:
            pass
        elif Girl == RogueX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                        ch_r "This top is pretty sexy. . ."
                elif Count >= 10:
                        ch_r "This top might be a bit daring to wear outside."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_r "Not leaving much to the imagination. . ."
                elif Count >= 5:
                        $ Girl.FaceChange("startled", 1)
                        ch_r "I really think this is a bit scandalous to wear out. . ."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                        ch_r "Oooh, I'm getting turned on already. . ."
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_r "This is just for in private, right. . ."
        elif Girl == KittyX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                        ch_k "Kinda hot top."
                elif Count >= 10:
                        ch_k "I wouldn't[Girl.like]feel comfortable in this top."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_k "This top is is[Girl.like]kinda breezy. . ."
                elif Count >= 5:
                        $ Girl.FaceChange("startled", 1)
                        ch_k "This top is[Girl.like]way too slutty."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                        ch_k "Is it hot in here? Whew. . ."
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_k "I wouldn't wear this out, but maybe indoors."
        elif Girl == EmmaX:
                if Count >= 10:
                        if ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_e "A bit daring. . ."
                        else:
                                ch_e "I'm not sure about this top."
                elif Count >= 5:
                        if ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0):
                                ch_e "I typically cover a {i}bit{/i} more than this."
                        else:
                                $ Girl.FaceChange("startled", 1)
                                ch_e "This is a bit more cleavage than even I'm comforable with."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                        ch_e "Aren't my assets a bit. . . exposed here?"
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_e "This is considerably more cleavage than even I'm comforable with."
        elif Girl == LauraX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_l "This top works."
                elif Count >= 10:
                    ch_l "The top's not really a good look."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_l "I don't know, the top's a little light."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_l "I can't really wear this top out."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_l ". . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_l "I wouldn't go out with my tits out."
        elif Girl == JeanX:
                if Count >= 10:# and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                    ch_j "You must really enjoy these tits. . ."
                #elif Count >= 10:
                    #ch_j "The top's not really a good look."
                elif Count >= 5:# and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_j "I've kinda got my tits out here. . ."
                #elif Count >= 5:
                    #$ Girl.FaceChange("startled", 1)
                    #ch_j "I can't really wear this top out."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_j ". . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_j "You think I'd go out with my tits on display?"
        elif Girl == StormX:
                if Count >= 10:
                                ch_s "A lovely choice for the top."
                elif Count >= 5:
                        if StormX not in Rules:
                                ch_s "I do typically cover more than this around the school."
                        else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "I'm not sure Charles would approve of this top."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                                ch_s "Aren't my assets a bit. . . exposed here?"
                else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "I'm not sure Charles would approve of this top."
        elif Girl == JubesX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                        ch_v "Yeah, the top'll work. . ."
                elif Count >= 10:
                    ch_v "I don't know about this top. . ."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_v "I don't know, the top's a little skimpy."
                elif Count >= 5:
                    $ Girl.FaceChange("startled", 1)
                    ch_v "I can't really wear this top out."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):
                    ch_v "I don't know. . ."
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_v "Well, I wouldn't go anywhere with my tits out like this. . ."
        #end top check dialog

        $ Tempshame -= Count                  #Set Outfit shame for the upper half
        $ Count = 0

        if Girl.Legs and Girl.Panties: #If wearing both legs and panties
                    $ Count = 30
        else: #If she's missing something on her legs
                    if Girl.PantsNum() > 5:
                        #If wearing pants commando
                        $ Count = 25
                    elif Girl.PantsNum() == 5:
                        #If wearing a skirt commando
                        $ Count = 20
                    elif Girl.PantiesNum() >= 8:
                        #If wearing shorts
                        $ Count = 25
                    elif Girl.PantiesNum() >= 6:
                        #If wearing only bikini bottoms
                        $ Count = 15
                    elif Girl.PantiesNum() >= 4:
                        #If wearing only panties
                        $ Count = 10
                    elif Girl.PantiesNum() >= 2:
                        #If wearing only lace panties
                        $ Count = 5
                    #else: 0

                    if Girl.HoseNum() >= 10:
                        #Factors in tights and hose
                        $ Count = 25 if Count < 25 else Count

                    if Girl.Over == "towel" and Count:
                        #If wearing a Towel and anything else
                        $ Count = 25
                    elif Girl.Over == "towel":
                        #If just wearing a Towel
                        $ Count = 15
        if not Check:
                    #If this isn't a custom check, skip this dialog stuff
                    pass
        elif Custom == 9 or Custom == 7:
                    pass
        elif Girl == RogueX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_r "Oh, I think these pants will work fine."
                            elif Girl.PantsNum() == 5:
                                ch_r "Oh, I think this skirt will work fine."
                            elif Girl.HoseNum() >= 10:
                                ch_r "Oh, these [Girl.Hose] will work."
                            elif Girl.Panties == "shorts":
                                ch_r "Oh, I think these shorts will work fine."
                            elif Girl.Over == "towel":
                                ch_r "The towel's an odd choice. . ."
                            else:
                                ch_r "Kinda breezy across my nethers, [Girl.Petname]. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_r "I kinda like going commando."
                            elif not Girl.Panties:
                                ch_r "Don't know about going commando though."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                    ch_r "These don't really leave much to the imagination. . ."
                elif Count >= 10:
                    $ Girl.FaceChange("angry", 1)
                    ch_r "I'm warning you, I'm not running around in my panties. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                    ch_r "Hmm, Breezy. . ."
                else:
                    ch_r "So long as we stay inside. . ."
        elif Girl == KittyX:
                if Count >= 20:
                            if Girl.PantsNum() >= 5:
                                ch_k "and these pants look cute on me."
                            elif Girl.Legs == "shorts":
                                ch_k "and these are cute shorts."
                            elif Girl.HoseNum() >= 10:
                                ch_k "I guess these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_k "The towel's an odd choice. . ."
                            else:
                                ch_k "This is kinda breezy."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_k "I like going without panties."
                            elif not Girl.Panties:
                                ch_k "It's a little uncomfortable without panties."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_k "I'm not sure about the coverage down here. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_k "I'm barely covered down here. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_k "kinda chilly. . ."
                else:
                        ch_k "if it's just[Girl.like]you and me. . ."
        elif Girl == EmmaX:
                if Count >= 20:
                            if Girl.PantsNum() > 5:
                                ch_e "and these pants always did suit me."
                            elif Girl.PantsNum() >= 5:
                                ch_e "and this skirt always did suit me."
                            elif Girl.HoseNum() >= 10:
                                ch_e "I guess these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_e "I'm unsure about wearing a towel out, [Girl.Petname]. . ."
                            else:
                                ch_e "I probably could wear something more downstairs, [Girl.Petname]. . ."
                            if not Girl.Panties:
                                if ApprovalCheck(Girl, 500, "I", TabM=0):
                                    ch_e "I do enjoy going without panties."
                                else:
                                    ch_e "I don't know about going without panties in this situation."
                elif Count >= 10:
                    if ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0):
                            ch_e "I hope you don't expect me to wear this out. . ."
                    else:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "I don't know about wearing this outside. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                            ch_e "This really tests my limits."
                else:
                            ch_e "I'll need to put something else on to leave the room though."
        elif Girl == LauraX:
                if Count >= 20:
                            if Girl.PantsNum() > 5:
                                ch_l "and these pants work."
                            elif Girl.PantsNum() >= 5:
                                ch_l "and this skirt works."
                            elif Girl.HoseNum() >= 10:
                                ch_l "and these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_l "The towel's an odd choice. . ."
                            else:
                                ch_l "but there's a draft."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_l "Commando's cool."
                            elif not Girl.Panties:
                                ch_l "I might accidentally flash some people like this though."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_l "I don't think I'm fully covered. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_l "I'm not covered like this. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_l "It's pretty minimal. . ."
                else:
                        ch_l "I wouldn't show off my cooch either. . ."
        elif Girl == JeanX:
                if Count >= 20:
                            if Girl.PantsNum() > 5:
                                ch_j "I do like these pants. . ."
                            elif Girl.PantsNum() >= 5:
                                ch_j "I do like this skirt. . ."
                            elif Girl.HoseNum() >= 10:
                                ch_j "these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_j "A towel though? . ."
                            else:
                                ch_j "kinda exposed here. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_j "I don't mind doing without the panties. . ."
                            elif not Girl.Panties:
                                ch_j "I'd kinda need panties with this. . ."
                #elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        #ch_j "I don't think I'm fully covered. . ."
                elif Count >= 10:
                        if (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                                $ Girl.FaceChange("sly", 1)
                        else:
                                $ Girl.FaceChange("angry", 1)
                        ch_j "So you want my puss on display? . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_j "This is basically \"nothing\". . ."
                else:
                        ch_j "I'm not interested in showing off the goods. . ."
        elif Girl == StormX:
                if Girl.PantsNum() > 5:
                            ch_s "and these pants always did suit me."
                elif Girl.PantsNum() >= 5:
                            ch_s "and this skirt always did suit me."
                elif Girl.HoseNum() >= 10:
                            ch_s "I supposed that these [Girl.Hose] will work fine."
                elif Girl.Over == "towel":
                            ch_s "I'm unsure about wearing a towel out, [Girl.Petname]. . ."
                else:
                            ch_s "A rather breezy ensemble, [Girl.Petname]. . ."
                if not Girl.Panties:
                    if ApprovalCheck(Girl, 500, "I", TabM=0):
                            ch_s "I do enjoy doing without panties."
                    else:
                            ch_s "Certainly quite exposed without panties. . ."
                if Count >= 10 and StormX not in Rules:
                            $ Girl.FaceChange("bemused", 1)
                            ch_s "I don't know that Charles would let me roam the halls in such an exposed state."
                elif StormX in Rules and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):
                            ch_s "This is quite the daring look you've put together."
                else:
                            ch_s "I doubt Charles would let me roam the halls in such an exposed state."
        elif Girl == JubesX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_v "and these pants work."
                            elif Girl.PantsNum() >= 6:
                                ch_v "and these shorts work."
                            elif Girl.PantsNum() >= 5:
                                ch_v "and this skirt works."
                            elif Girl.HoseNum() >= 10:
                                ch_v "and these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_v "The towel's an odd choice. . ."
                            else:
                                ch_v "but I don't know about this. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_v "I guess we're not doing panties now?"
                            elif not Girl.Panties:
                                ch_v "I don't think I'd want to go without panties. . ."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_v "This is pretty skimpy. . ."
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_v "This is pretty skimpy. . ."
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):
                        ch_v "Wow, this look is. . . a lot. . ."
                else:
                        ch_v "I don't really go around showing the goods. . ."
        # End Panties check dialog

        $ Tempshame -= Count                  #Set Outfit shame for the lower half

        if Check:
                #if this is a custom outfit check
                if Check == 2:
                    ch_p "So can I see it then?"
                elif Custom == 4:
                    ch_p "So would you work out in that?"
                elif Custom == 7:
                    ch_p "So would you sleep in that?"
                else:
                    ch_p "So would you wear that outside?"

                $ Girl.FaceChange("sexy", 0)
                if Girl.PantsNum() > 2:
                    pass        #if she's wearing pants
                elif Girl == StormX and StormX in Rules:
                    pass
                elif Girl.PantiesNum() > 2 and (Girl.SeenPanties or ApprovalCheck(Girl, 900, TabM=0)):
                    pass        #no pants, but panties
                elif Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=0):
                    pass        #no panties, but she's fine with that
                else:
                    $ Agree = 0 #not fine with it

                if not Agree:
                    pass
                elif Girl == StormX and StormX in Rules:
                    pass
                elif Girl.OverNum() > 2:
                    pass        #if she's wearing a top
                elif Girl.ChestNum() > 2 and (Girl.SeenChest or ApprovalCheck(Girl, 900, TabM=0)):
                    pass        #no top, but bra
                elif Girl.SeenChest or ApprovalCheck(Girl, 1200, TabM=0):
                    pass        #no bra, but she's fine with that
                else:
                    $ Agree = 0 #not fine with it

                if Check == 2 and Agree:
                            #if checking to see if she'll drop the dressing screen. . .
                            $ Girl.Shame = Tempshame
                            $ Girl.FaceChange("sly")
                            if Girl == RogueX:
                                    ch_r "This ain't a bad look, I guess. . ."
                            elif Girl == KittyX:
                                    ch_k "I suppose you've put together a cute little outfit. . ."
                            elif Girl == EmmaX:
                                    ch_e "I suppose I could pull this off. . ."
                            elif Girl == LauraX:
                                    ch_l "Huh, this'll work. . ."
                            elif Girl == JeanX:
                                    ch_j "It does look good on me. . ."
                            elif Girl == StormX:
                                    ch_s "I don't see why not. . ."
                            elif Girl == JubesX:
                                    ch_v "Sure, take a look. . ."
                            hide DressScreen
                            return 1
                if not Agree:
                            #she isn't even comfortable with you seeing it
                            $ Girl.FaceChange("bemused", 2,Eyes="side")
                            if Girl == RogueX:
                                    ch_r "I don't really feel comfortable in this. . ."
                            elif Girl == KittyX:
                                    ch_k "I don't think I'd be comfortable with you seeing me like this. . ."
                            elif Girl == EmmaX:
                                    ch_e "I wouldn't want to blind you. . ."
                            elif Girl == LauraX:
                                    ch_l "You'll have to earn it."
                            elif Girl == JeanX:
                                    ch_j "It's cute, yeah, but I can't go out in it."
                            elif Girl == StormX:
                                    ch_s "I think you're making fun of me. . ."
                            elif Girl == JubesX:
                                    ch_v "I really can't let you see this. . ."
                            menu:
                                extend ""
                                "Ok then, you can put your normal clothes back on.":
                                            $ Girl.OutfitChange(Changed=1)
                                            hide DressScreen
                                "Ok, we can keep tweaking it.":
                                            pass
                            $ Girl.FaceChange("smile", 1)
                            if Girl == RogueX:
                                    ch_r "Thanks, [Girl.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Thanks."
                            elif Girl == EmmaX:
                                    ch_e "Appreciated."
                            elif Girl == LauraX:
                                    ch_l "Thanks."
                            elif Girl == JeanX:
                                    ch_j ". . . that's what I said."
                            elif Girl == StormX:
                                    ch_s "Very well. . ."
                            elif Girl == JubesX:
                                    ch_v "Cool, cool. . ."
                            return
                if Girl == RogueX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_r "It's a little late to worry about that, right?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_r "Hmm. . . yeah, I'd love to. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Custom == 7:
                                #Sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                        ch_r "A bit scandalous, but yeah."
                                elif Tempshame >= 15:
                                        ch_r "Yeah, you're worth it."
                                else:
                                        ch_r "Sure, it's cute."
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_r "Yeah, I think I like this style, I'd wear this."
                        elif Tempshame <= 15:
                            if ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0):
                                ch_r "It's pretty skimpy, but I can make it work."
                            else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "I think this looks is a bit daring to wear."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "Sure, I can swim in this. . ."
                        elif Tempshame <= 25:
                            if ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0):
                                ch_r "Kinky, but I can rock this."
                            else:
                                $ Girl.FaceChange("angry", 1)
                                ch_r "I'm definitely not going out in this."
                                $ Agree = 0
                        elif ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0):
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "I can't believe it. . . but yeah."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_r "You have got to be kidding."
                                $ Agree = 0
                elif Girl == KittyX:
                        if Girl.Taboo >= 40: #Girl.Loc != "bg player" and Girl.Loc != "bg kitty":
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_k "Kinda late to ask, right?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_k "I'm getting wet just thinking about it. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_k "Sure, it's a cute look!"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_k "It's pretty hot, right?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_k "This is[Girl.like]pretty exposed, but ok."
                                elif Tempshame >= 15:
                                    ch_k "It's kinda naughty, I like it."
                                else:
                                    ch_k "Yeah, these are fine."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "It's too slutty to wear out."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "This is a cute swimsuit. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_k "So sexy, but I can handle it."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_k "{i}Way{/i} too sexy for outside."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "OMG, I can't believe I'm doing this."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_k "I - can't - even."
                                $ Agree = 0
                elif Girl == EmmaX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                "She glances around."
                                ch_e "Is that a trick question?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_e "The thought of it gets me moist. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_e "Yes, it's a fine choice."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_e "Rather daring, how could I resist?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_e "You understand I only wear this sort of thing in private."
                                else:
                                    ch_e "It is a comfortable outfit."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "Rather too daring, don't you think?"
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "Fine, this is decent swimwear. . ."
                        elif Tempshame >= 15 and "public" not in Girl.History:
                                ch_e "I doubt I could get away with this in public, [Girl.Petname]."
                                $ Agree = 0
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_e "This is particularly inappropriate. . . in the best ways."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_e "I don't believe even I could pull off this look, [Girl.Petname]."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "This look certainly pushes the boundaries."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_e "Even I can't pull this off."
                                $ Agree = 0
                elif Girl == LauraX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_l "Well a bit late for that, I guess."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_l ". . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_l "I don't see why not."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_l "It looks good, right?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_l "Sure, perv."
                                elif Tempshame >= 15:
                                    ch_l "Sure, why not."
                                else:
                                    ch_l "Yeah, I guess."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "I can't move freely in this without showing off the goods."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "Yeah, I can swim in this. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_l "I can handle this."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_l "Nah, too slutty."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "Pretty daring, eh?"
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_l "As if."
                                $ Agree = 0
                elif Girl == JeanX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_j "Well, I guess so, right?"
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_j ". . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_j "Sure, whatever."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_j "I almost have to. . ."
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_j "If it'll keep you hard. . ."
                                elif Tempshame >= 15:
                                    ch_j "Yeah, sure."
                                else:
                                    ch_j "Why not."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_j "I can pull this one off. . ."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_j "Yeah, sure."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_j "This'll turn some heads. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_j "I wouldn't want to break anyone. . ."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_j "Kinky, but sure."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_j "You have to be joking."
                                $ Agree = 0
                elif Girl == StormX:
                        #Storm will approve anything if you clear it with Xavier, and is more likely to be fine with risky looks
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                "She glances around."
                                ch_s "It seems a bit late for that question. . ."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                ch_s "I do find the idea. . . exciting. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 10:
                                $ Girl.FaceChange("smile")
                                ch_s "Yes, it's a fine choice."
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 20:
                                    ch_s "This is a fine outfit."
                                else:
                                    ch_s "It may be a bit more than I'm used to. . ."
                        elif StormX in Rules:
                                ch_s "I don't see why not. . ."
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "I suppose I could swim well like this. . ."
                        elif Tempshame <= 20 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_s "This certainly does push the limits of good taste. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "I doubt Charles would approve, but so what?"
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "I'm afraid that Charles would never approve."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "I doubt Charles would approve, but so what?"
                        else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_s "I'm afraid that Charles would never approve."
                                $ Agree = 0
                elif Girl == JubesX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_v "I guess that ship has sailed. . ."
                        if "exhibitionist" in Girl.Traits and Tempshame >= 20:
                                $ Girl.Statup("Lust", 80, 10)
                                $ Girl.FaceChange("sexy", 2)
                                ch_v ". . ."
                                $ Girl.FaceChange("sexy", 1)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_v "I guess?"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                                ch_v "It looks totally hot, right?"
                        elif Custom == 7:
                                #if it's sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_v "Whatever, perv."
                                elif Tempshame >= 15:
                                    ch_v "Sure, why not."
                                else:
                                    ch_v "Sure, I guess."
                        elif Tempshame <= 15:
                                $ Girl.FaceChange("bemused", 1)
                                ch_v "I think this is too breezy."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_v "I could swim in this. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_v "I guess this is fine. . ."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_v "I really couldn't wear this out."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_v "It's pretty hot, right?"
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_v "As if."
                                $ Agree = 0
                #End check dialog

                #$ Girl.OutfitShame[Custom] = Tempshame
                if Custom == 5:
                        $ Girl.Custom2 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                        $ Girl.Custom2[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,5,1) #checks to make sure it's still SFW
                elif Custom == 6:
                        $ Girl.Custom3 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                        $ Girl.Custom3[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,6,1)
                elif Custom == 4:
                    if Agree:
                        $ Girl.Gym = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                        call Clothing_Schedule_Check(Girl,4,1)
                elif Custom == 7:
                        $ Girl.Sleepwear = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                        $ Girl.Sleepwear[0] = 2 if Agree else 1
                elif Custom == 10:
                    if Agree:
                        $ Girl.Swim = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                elif Custom == 3:
                        $ Girl.Custom1 = [2,Girl.Arms,Girl.Legs,Girl.Over,Girl.Neck,Girl.Chest,Girl.Panties,Girl.Acc,Girl.Hair,Girl.Hose,Tempshame]
                        $ Girl.Custom1[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,3,1)
                else:
                        "Tell Oni Custom Outfit was [Custom]"
                        $ RogueX.gibberish = 5
        elif Girl.Taboo <= 20:
                # halves shame level if she's comfortable
                $ Tempshame /= 2

        $ Girl.Shame = Tempshame

        if Custom == 20:
                # This returns the scene if it's a check Shame adjustment
                return

        if Check:
                pass
        elif bg_current == "HW Party" or (bg_current == "bg player" and "halloween" in Player.DailyActions):
                #skips because it's at the party and they should be in costume only
                pass
        elif "exhibitionist" in Girl.Traits and Tempshame <= 20:
                #If she's an exhibitionist
                pass
        elif Girl == StormX and StormX in Rules:
                pass
        elif Tempshame <= 12:
                #If the outfit is tame
                pass
        elif Girl.Over == "towel" and Girl.Loc == "bg showerroom":
                #If she's in a towel but it's appropriate
                pass
        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1500) or ApprovalCheck(Girl, 500, "I")):
                #If the outfit is hot but she's ok
                pass
        elif Tempshame <= 20 and (Girl.Loc == "bg dangerroom" or Girl.Loc == "bg pool"):
                #If the outfit is light but she's in the gym or pool
                pass
        elif Tempshame <= 20 and (ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 650, "I")):
                #If the outfit is sexy but she's cool with that
                pass
        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2000) or ApprovalCheck(Girl, 700, "I")):
                #If the outfit is sexy but she's cool with that
                pass
        elif (ApprovalCheck(Girl, 2500) or ApprovalCheck(Girl, 800, "I")):
                #If the outfit is very scandalous but she's ok with that
                pass
        elif Girl.Loc == "bg dangerroom" and Girl.Outfit == "gym":
                $ Girl.OutfitChange("gym",Changed = 1)
        elif not Girl.Taboo:
                pass
        elif Girl.Outfit == "swimwear" and bg_current == "bg pool":
                pass
        elif bg_current == "bg pool" and Girl.ChestNum() >= 3 and Girl.PantiesNum() >= 6:
                pass
        elif Girl.Outfit == "gym" and bg_current == "bg dangerroom":
                pass
        else:
                #if this is a called outfit modesty check. . .
                if Girl.Loc == bg_current:
                        if Girl == RogueX:
                                ch_r "I'll be right back, I've got to change out of this."
                        elif Girl == KittyX:
                                ch_k "One sec, I gotta change real quick."
                        elif Girl == EmmaX:
                                ch_e "I'm afraid I'll have to change, one moment."
                        elif Girl == LauraX:
                                ch_l "One sec, I gotta change real quick."
                        elif Girl == JeanX:
                                ch_j "Wait while I get changed."
                        elif Girl == StormX:
                                ch_s "I'll need to change into something more substantial."
                        elif Girl == JubesX:
                                ch_v "I need to throw something on real quick. . ."
                if Girl.Loc == "bg dangerroom":
                        $ Girl.Outfit =  "gym"
                elif Girl.Loc == "bg pool" and Girl.Swim[0]:
                        $ Girl.Outfit =  "swimwear"
                else:
                        $ Girl.Outfit = renpy.random.choice(["casual1", "casual2"])

                $ Girl.AddWord(1,"modesty","modesty")  #sets a flag that this has happened before
                $ Girl.Water = 0
                $ Girl.OutfitChange(Changed=1)
                if Girl == RogueX:
                        ch_r "That wasn't really \"outdoor ready\"."
                elif Girl == KittyX:
                        ch_k "I just needed to throw some more on."
                elif Girl == EmmaX:
                        ch_e "I wouldn't want to be \"inappropriate\"."
                elif Girl == LauraX:
                        ch_l "That wasn't really \"outdoors\" wear."
                elif Girl == JeanX:
                        ch_j "Couldn't really be out in that."
                elif Girl == StormX:
                        ch_s "I'm afraid Charles would not approve of that look around students."
                elif Girl == JubesX:
                        ch_v "That was kinda. . . private. . ."
        return

label QuickOutfitCheck(Girl=0, Custom = 3, Count = 0, Tempshame = 50, Agree = 1, HolderOutfit =[]): #rkeljsv
        #Custom determines which custom outfit is being checked against.
        #If Custom1 = 3, if gym = 4, if custom2 = 5, if custom3 = 6,  if sleepwear 7, if classwear 8, if private = 9, if swimsuit = 10
        # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you.
        # call QuickOutfitCheck(RogueX,20)

        $ Girl = GirlCheck(Girl)

        if Custom == 3:
                $ HolderOutfit = Girl.Custom1[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 5:
                $ HolderOutfit = Girl.Custom2[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 6:
                $ HolderOutfit = Girl.Custom3[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 7:
                $ HolderOutfit = Girl.Sleepwear[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 4:
                $ HolderOutfit = Girl.Gym[:] #fills Holder with the values of the sent uni. . .
        elif Custom == 10:
                $ HolderOutfit = Girl.Swim[:] #fills Holder with the values of the sent uni. . .
        else:
                "Tell Oni, Outfit check, [Custom]."
                return

        #end Holder setting. . .

        #Chests
        while len(HolderOutfit) < 11:
                $ HolderOutfit.append(0)

        if HolderOutfit[5] in ("tank","white tank","button tank","sports bra","tube top","corset"):
                $ Count = 20
        elif HolderOutfit[5] == "wolvie top":
                $ Count = 10
        elif HolderOutfit[5] in ("lace bra","lace corset"):
                $ Count = 5
        elif HolderOutfit[5]:
                #any other bra
                $ Count = 10
        elif HolderOutfit[7] == "suspenders" or HolderOutfit[7] == "suspenders2":
                $ Count = 5
        else:
                $ Count = 0

        #Overs
        if HolderOutfit[3] in ("nighty","mesh top"):
                $ Count += 5
        elif HolderOutfit[3] == "towel":
            if Girl == EmmaX:
                $ Count += 5
            elif Girl == StormX:
                pass
            else:
                $ Count += 10
        elif HolderOutfit[3] in ("jacket","dress","pink top") or HolderOutfit[7] == "jacket":
                $ Count += 15
        elif HolderOutfit[3] or HolderOutfit[7] == "shut jacket":
                $ Count += 20

        if Girl.Pierce and Count <= 10:
                $ Count = -5

        $ Count = 20 if Count >= 20 else Count

        $ Tempshame -= Count                  #Set Outfit shame for the upper half
        $ Count = 0

        if HolderOutfit[2] and HolderOutfit[6]: #If wearing both legs and panties
                    $ Count = 30
        elif HolderOutfit[2] in ("blue skirt","skirt","other skirt"):
                    $ Count = 20
        elif HolderOutfit[2] or HolderOutfit[7] == "shut jacket": #any pants
                    $ Count = 25
        elif HolderOutfit[6] == "shorts": #Rogue's shorts as panties
                    $ Count = 25
        elif HolderOutfit[6] in ("bikini bottoms","sports panties","shorts"):
                    $ Count = 15
        elif HolderOutfit[6] == "lace panties":
                    $ Count = 5
        elif HolderOutfit[6]: #any panties
                    $ Count = 10

        if HolderOutfit[9] == "tights":
                    #Factors in tights and hose
                    $ Count = 25 if Count < 25 else Count

        if HolderOutfit[3] == "towel" and Girl not in (EmmaX,StormX):
                    #25 if wearing anything else, 15 if not
                    $ Count = 25 if Count else 15

        $ Tempshame -= Count                  #Set Outfit shame for the lower half

        if "exhibitionist" in Girl.Traits:
                    pass
        elif Tempshame <= 5:
                    pass
        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):
                    pass
        elif Custom == 10 and Tempshame <= 20:
                    #swimsuit
                    pass
        elif Girl == EmmaX and Tempshame >= 15 and "public" not in Girl.History:
                    $ Agree = 0
        elif Girl == StormX and StormX in Rules:
                    pass
        elif Tempshame <= 25:
                if ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0):
                    pass
                else:
                    $ Agree = 0
        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                    pass
        else:
                    $ Agree = 0

        #End check dialog

        #$ Girl.OutfitShame[Custom] = Tempshame
        if Custom == 3:
                $ Girl.Custom1[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,3,1)
        elif Custom == 5:
                $ Girl.Custom2[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,5,1) #checks to make sure it's still SFW
        elif Custom == 6:
                $ Girl.Custom3[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,6,1)
        elif Custom == 4:

                $ Girl.Gym[0] = 2 if Agree else 1
                call Clothing_Schedule_Check(Girl,4,1)
        elif Custom == 7:
                $ Girl.Sleepwear[0] = 2 if Agree else 1
        elif Custom == 10:
                $ Girl.Swim[0] = 2 if Agree else 1
        else:
                "Tell Oni Custom Outfit was [Custom]"
                $ RogueX.gibberish = 5
        return

label Display_DressScreen(Girl=Ch_Focus): #rkeljsv
        #asks if you're willing to put up a protective dressing screen, XTaboo is the girl's local taboo
        # call Display_DressScreen(Girl)
        if renpy.showing('DressScreen'):
                return 1

        if Girl == StormX:
            if not Girl.Taboo or StormX in Rules: #Storm skips this if not in public
                return 1
            else:
                ch_s "I'm afraid rules are rules."

        if Girl.Taboo:
                return 0

        $ Girl.FaceChange("bemused",1,Eyes="side")
        if "screen" in Girl.DailyActions:
                pass
        elif Girl == RogueX:
                ch_r "I'm not really comfortable like this."
        elif Girl == KittyX:
                ch_k "I'm getting kinda exposed here."
        elif Girl == EmmaX:
                ch_e "I'm feeling a bit exposed here. . ."
        elif Girl == LauraX:
                ch_l "I don't know about showing this much skin."
        elif Girl == JeanX:
                ch_j "I don't think you're ready for this. . ."
        elif Girl == JeanX:
                ch_j "I don't think you're ready for this. . ."
        elif Girl == JubesX:
                ch_v "I don't know, this is moving a little fast. . ."
        $ Girl.AddWord(1,0,"screen") #adds screen to daily
        $ Girl.FaceChange("bemused",1)
        call AnyLine(Girl,"Mind if I get behind a dressing screen?")
        menu:
            extend ""
            "Go ahead":
                    show DressScreen zorder 150
                    if Girl == RogueX:
                            ch_r "Thanks."
                    elif Girl == KittyX:
                            ch_k "Great."
                    elif Girl == EmmaX:
                            ch_e "Thank you."
                    elif Girl == LauraX:
                            ch_l "K."
                    elif Girl == JeanX:
                            ch_j "Good."
                    elif Girl == JubesX:
                            ch_v "Oh, thanks. . ."
                    return 1
            "No, don't":
                    if Girl == RogueX:
                            ch_r "Fine then. . ."
                    elif Girl == KittyX:
                            ch_k "Ok then. . ."
                    elif Girl == EmmaX:
                            ch_e "Fair enough. . ."
                    elif Girl == LauraX:
                            ch_l "Ok. . ."
                    elif Girl == JeanX:
                            ch_j "Ok then."
                    elif Girl == JubesX:
                            ch_v "Well, fine. . ."

        return 0
