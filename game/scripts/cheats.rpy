label cheat_editor(Girl):
    $ counter = 0

    while True:
        menu:
            "[Girl.name]: Love: [Girl.love], Obedience: [Girl.obedience], Inhibition: [Girl.inhibition], Lust: [Girl.lust], Taboo: [taboo], Location: [Girl.location]"
            "Activities":
                menu:
                    "Recent Actions":
                        "[Girl.recent_history]"
                    "Daily Actions":
                        "[Girl.daily_history]"
                    "Traits":
                        "[Girl.traits]"
                    "History":
                        "[Girl.history]"
            "Raise love":
                $ Girl.love += 100
            "Lower love":
                $ Girl.love -= 100
            "Raise obedience":
                $ Girl.obedience += 100
            "Lower obedience":
                $ Girl.obedience -= 100
            "Raise inhibition":
                $ Girl.inhibition += 100
            "Lower inhibition":
                $ Girl.inhibition -= 100
            "Taboo toggle":
                $ taboo = 40 if taboo != 40 else 0

                "[taboo]"
            "Small changes":
                $ counter = 1

                while counter:
                    menu:
                        "Raise love":
                            $ Girl.love += 10
                        "Lower love":
                            $ Girl.love -= 10
                        "Raise obedience":
                            $ Girl.obedience += 10
                        "Lower obedience":
                            $ Girl.obedience -= 10
                        "Raise inhibition":
                            $ Girl.inhibition += 10
                        "Lower inhibition":
                            $ Girl.inhibition -= 10
                        "Back":
                            $ counter = 0
            "Other":
                menu:
                    "Raise lust":
                        $ Girl.lust += 10
                    "Lower lust":
                        $ Girl.lust -= 10
                    "Raise addiction":
                        $ Girl.addiction += 10
                    "Lower addiction":
                        $ Girl.addiction -= 10
                    "Back":
                        pass
            "Wardrobe":
                call wardrobe_editor(Girl)
            "Unlock all Girls":
                python:
                    for G in all_Girls:
                        active_Girls.append(G)

                        Player.Phonebook.append(G)

                        G.history.append("met")

                        if G == EmmaX:
                            EmmaX.name = "Emma"
                            EmmaX.names.append("Emma")
                            G.history.append("classcaught")
                        elif G == LauraX:
                            LauraX.name = "Laura"
                            LauraX.names.append("X-23")
                            LauraX.names.append("Laura")
                            G.history.append("dress0")
                        elif G == StormX:
                            StormX.names.append("Ororo")
                            StormX.names.append("Ms. Munroe")

                        if G.location == "hold":
                            G.location = G.home
            "Maximize all Girls' stats":
                python:
                    for G in all_Girls:
                        G.love = 1000
                        G.obedience = 1000
                        G.inhibition = 1000
            "Add all Girls to Harem":
                python:
                    for G in all_Girls:
                        Player.Harem.append(G)
            "Unlock all outfits":
                python:
                    for G in all_Girls:
                        for item in face_inner_accessories:
                            G.inventory.append(item)

                        for item in face_outer_accessories:
                            G.inventory.append(item)

                        for item in bras:
                            G.inventory.append(item)

                        for item in underwears:
                            G.inventory.append(item)

                        for item in hoses:
                            G.inventory.append(item)

                        for item in socks:
                            G.inventory.append(item)

                        for item in bodysuits:
                            G.inventory.append(item)

                        for item in pants:
                            G.inventory.append(item)

                        for item in skirts:
                            G.inventory.append(item)

                        for item in shorts:
                            G.inventory.append(item)

                        for item in dresses:
                            G.inventory.append(item)

                        for item in boots:
                            G.inventory.append(item)

                        for item in tops:
                            G.inventory.append(item)

                        for item in necks:
                            G.inventory.append(item)

                        for item in gloves:
                            G.inventory.append(item)

                        for item in sleeves:
                            G.inventory.append(item)

                        for item in suspenders:
                            G.inventory.append(item)

                        for item in belts:
                            G.inventory.append(item)

                        for item in jackets:
                            G.inventory.append(item)

                        for item in cloaks:
                            G.inventory.append(item)

                        Girl.swimwear["outfit_active"]

            "Return":
                call checkout

                return

label face_editor(Girl):
    while True:
        menu:
            "First set":
                menu:
                    "Normal":
                        $ Girl.emotion = "_normal"
                    "Angry":
                        $ Girl.emotion = "_angry"
                    "Smiling":
                        $ Girl.emotion = "_smile"
                    "Sexy":
                        $ Girl.emotion = "_sexy"
                    "Suprised":
                        $ Girl.emotion = "_surprised"
                    "Bemused":
                        $ Girl.emotion = "_bemused"
                    "Manic":
                        $ Girl.emotion = "_manic"
            "Second set":
                menu:
                    "Sad":
                        $ Girl.emotion = "_sad"
                    "Sucking":
                        $ Girl.emotion = "_sucking"
                    "Kiss":
                        $ Girl.emotion = "_kiss"
                    "Tongue":
                        $ Girl.emotion = "_tongue"
                    "Confused":
                        $ Girl.emotion = "_confused"
                    "Closed":
                        $ Girl.emotion = "_closed"
                    "Down":
                        $ Girl.emotion = "_down"
            "Third set":
                menu:
                    "Sadside":
                        $ Girl.emotion = "_sadside"
                    "Startled":
                        $ Girl.emotion = "startled"
                    "Perplexed":
                        $ Girl.emotion = "_perplexed"
                    "Sly":
                        $ Girl.emotion = "_sly"
            "Toggle blushing":
                if Girl.blushing == "":
                    $ Girl.blushing = "_blush1"
                elif Girl.blushing == "_blush1":
                    $ Girl.blushing = "_blush2"
                else:
                    $ Girl.blushing = ""
            "Back":
                return

        $ Girl.change_face()

label wardrobe_editor(Girl):
    while True:
        menu wardrobe_menu:
            "View":
                while True:
                    menu:
                        "Default":
                            call show_full_body(Girl)
                        # "Face":
                        #     call kiss_launch(Girl)
                        # "Body":
                        #     call pussy_launch(Girl)
                        "Handjob":
                            if not renpy.showing(Girl.tag + " handjob"):
                                call show_handjob(Girl)
                            else:
                                call show_full_body(Girl)
                        "Titjob":
                            if not renpy.showing(Girl.tag + " titjob"):
                                call show_titjob(Girl)
                            else:
                                call show_full_body(Girl)
                        "Blowjob":
                            if not renpy.showing(Girl.tag + " blowjob"):
                                call show_blowjob(Girl)
                            else:
                                call show_full_body(Girl)
                        "Missionary":
                            $ Girl.pose = "sex"

                            if not renpy.showing(Girl.tag + " sex"):
                                call show_sex(Girl, "sex")
                            else:
                                call show_full_body(Girl)
                        "Doggy":
                            $ Girl.pose = "doggy"

                            if not renpy.showing(Girl.tag + " doggy"):
                                call show_sex(Girl, "anal")
                            else:
                                call show_full_body(Girl)
                        "Back":
                            jump wardrobe_menu
            "First casual outfit":
                $ Girl.outfit = Girl.first_casual_outfit
            "Second casual outfit":
                $ Girl.outfit = Girl.second_casual_outfit
            "Halloween costume":
                $ Girl.outfit = Girl.halloween_costume
            "Domme outfit" if Girl == EmmaX:
                $ Girl.arm_pose = 2
                $ Girl.outfit = Girl.domme_outfit
            "Nude":
                $ Girl.outfit = Girl.nude
            "Dress/Suit":
                while True:
                    menu:
                        "Remove [Girl.outfit[dress]]" if Girl.outfit["dress"]:
                            $ Girl.outfit["dress"] = ""
                            $ Girl.dress_top_pulled_down = False
                            $ Girl.dress_upskirt = False
                        "Remove [Girl.outfit[bodysuit]]" if Girl.outfit["bodysuit"]:
                            $ Girl.outfit["bodysuit"] = ""
                            $ Girl.bodysuit_top_pulled_aside = False
                            $ Girl.bodysuit_bottom_pulled_aside = False
                        "Add catsuit" if Girl == RogueX:
                            $ Girl.outfit["bodysuit"] = "_catsuit"
                        "Add Raven suit" if Girl == RogueX:
                            $ Girl.outfit["bodysuit"] = "_Raven_suit"
                        "Toggle Raven cloak" if Girl == RogueX:
                            if Girl.outfit["cloak"] == "_Raven_cloak":
                                $ Girl.outfit["cloak"] = ""
                            else:
                                $ Girl.outfit["cloak"] = "_Raven_cloak"
                        "Add blue dress" if Girl == RogueX:
                            $ Girl.outfit["dress"] = "_blue_dress"
                        "Add one-piece swimsuit" if Girl == RogueX:
                            $ Girl.outfit["bodysuit"] = "_swimsuit"
                        "Add sexy swimsuit" if Girl == RogueX:
                            $ Girl.outfit["bodysuit"] = "_sexy_swimsuit"
                        "Add red dress" if Girl == RogueX:
                            $ Girl.outfit["dress"] = "_red_dress"
                        "Add qipao" if Girl == KittyX:
                            $ Girl.outfit["dress"] = "_qipao"
                        "Add sci-fi suit" if Girl == JeanX:
                            $ Girl.arm_pose = 1
                            $ Girl.outfit["bodysuit"] = "_sci_fi"
                        "Pull top up/down" if Girl.outfit["dress"]:
                            if Girl.dress_top_pulled_down:
                                $ Girl.dress_top_pulled_down = False
                            else:
                                $ Girl.dress_top_pulled_down = True
                        "Pull skirt up/down" if Girl.outfit["dress"]:
                            if Girl.dress_upskirt:
                                $ Girl.dress_upskirt = False
                            else:
                                $ Girl.dress_upskirt = True
                        "Pull top aside" if Girl.outfit["bodysuit"]:
                            if Girl.bodysuit_top_pulled_aside:
                                $ Girl.bodysuit_top_pulled_aside = False
                            else:
                                $ Girl.bodysuit_top_pulled_aside = True
                        "Pull bottom aside" if Girl.outfit["bodysuit"]:
                            if Girl.bodysuit_bottom_pulled_aside:
                                $ Girl.bodysuit_bottom_pulled_aside = False
                            else:
                                $ Girl.bodysuit_bottom_pulled_aside = True
                        "Back":
                            jump wardrobe_menu

                    $ Girl.set_outfit_flags()
            "Top":
                while True:
                    menu:
                        "Remove [Girl.outfit[top]]" if Girl.outfit["top"]:
                            $ Girl.outfit["top"] = ""
                            $ Girl.top_pulled_up = False
                        "Remove [Girl.outfit[jacket]]" if Girl.outfit["jacket"]:
                            $ Girl.outfit["jacket"] = ""
                            $ Girl.jacket_opened = False
                        "Add mesh top" if Girl == RogueX:
                            $ Girl.outfit["top"] = "_mesh_top"
                        "Add pink top" if Girl in [RogueX, KittyX]:
                            $ Girl.outfit["top"] = "_pink_top"
                        "Add tube top" if Girl in [RogueX, StormX]:
                            $ Girl.outfit["top"] = "_tube_top"
                        "Add red top" if Girl in [KittyX, JubesX]:
                            $ Girl.outfit["top"] = "_red_shirt"
                        "Add pink shirt" if Girl == JeanX:
                            $ Girl.outfit["top"] = "_pink_shirt"
                        "Add green shirt" if Girl == JeanX:
                            $ Girl.outfit["top"] = "_green_shirt"
                        "Add yellow shirt" if Girl == JeanX:
                            $ Girl.outfit["top"] = "_yellow_shirt"
                        "Add black top" if Girl == JubesX:
                            $ Girl.outfit["top"] = "_black_shirt"
                        "Add tube top" if Girl == JubesX:
                            $ Girl.outfit["top"] = "_tube_top"
                        "Add classic jacket" if Girl == RogueX:
                            $ Girl.outfit["jacket"] = "_classic_jacket"
                        "Add jacket" if Girl == JubesX:
                            $ Girl.outfit["jacket"] = "_jacket"
                        "Close jacket" if Girl == JubesX and Girl.outfit["jacket"] in ["_jacket", "_closed_jacket"]:
                            if Girl.outfit["jacket"] == "_jacket":
                                $ Girl.outfit["jacket"] = "_closed_jacket"
                            else:
                                $ Girl.outfit["jacket"] = "_jacket"
                        "Open jacket" if Girl == JubesX and Girl.outfit["jacket"] in ["_jacket", "_open_jacket"]:
                            if Girl.outfit["jacket"] == "_jacket":
                                $ Girl.outfit["jacket"] = "_open_jacket"
                            else:
                                $ Girl.outfit["jacket"] = "_jacket"
                        "Add white shirt" if Girl == StormX:
                            $ Girl.outfit["top"] = "_white_shirt"
                        "Add dress" if Girl == EmmaX:
                            $ Girl.outfit["top"] = "_dress"
                        "Add opaque fetish top" if Girl == RogueX:
                            $ Girl.outfit["top"] = "_opaque_fetish"
                        "Add sheer fetish top" if Girl == RogueX:
                            $ Girl.outfit["top"] = "_sheer_fetish"
                        "Add violet shirt" if Girl == KittyX:
                            $ Girl.outfit["top"] = "_violet_shirt"
                        "Add nighty" if Girl == KittyX:
                            $ Girl.outfit["top"] = "_nighty"
                        "Add towel":
                            if Girl == StormX:
                                $ Girl.outfit["face_outer_accessory"] = "_towel"
                            else:
                                $ Girl.outfit["top"] = "_towel"
                        "Pull top up/down":
                            if Girl.top_pulled_up:
                                $ Girl.top_pulled_up = False
                            else:
                                $ Girl.top_pulled_up = True
                        "Back":
                            jump wardrobe_menu

                    $ Girl.set_outfit_flags()
            "Bra":
                while True:
                    menu:
                        "Remove [Girl.outfit[bra]]" if Girl.outfit["bra"]:
                            $ Girl.outfit["bra"] = ""
                            $ Girl.bra_pulled_up = False
                        "Add bikini":
                            $ Girl.outfit["bra"] = "_bikini_top"
                        "Add lace bra" if Girl not in [KittyX, LauraX]:
                            $ Girl.outfit["bra"] = "_lace_bra"
                        "Add sports bra" if Girl != LauraX:
                            $ Girl.outfit["bra"] = "_sports_bra"
                        "Add tank top" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_tank"
                        "Add buttoned tank top" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_buttoned_tank"
                        "Add basic bra" if Girl in [RogueX, KittyX]:
                            $ Girl.outfit["bra"] = "_bra"
                        "Add cami" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_cami"
                        "Add dress top" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_dress"
                        "Add corset" if Girl in [EmmaX, LauraX]:
                            $ Girl.outfit["bra"] = "_corset"
                        "Add lace corset" if Girl == LauraX:
                            $ Girl.outfit["bra"] = "_lace_corset"
                        "Add leather bra" if Girl == LauraX:
                            $ Girl.outfit["bra"] = "_leather_bra"
                        "Add white tank" if Girl == LauraX:
                            $ Girl.outfit["bra"] = "_white_tank"
                        "Add wolvie bra" if Girl == LauraX:
                            $ Girl.outfit["bra"] = "_wolvie_bra"
                        "Add green bra" if Girl == JeanX:
                            $ Girl.outfit["bra"] = "_green_bra"
                        "Add black bra" if Girl == StormX:
                            $ Girl.outfit["bra"] = "_black_bra"
                        "Add cosplay bra" if Girl == StormX:
                            $ Girl.outfit["bra"] = "_cosplay_bra"
                        "Add classic top" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_classic"
                        "Add harness" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_harness"
                        "Add kitty lingerie" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_kitty_lingerie"
                        "Add orange top" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_orange_top"
                        "Pull bra up/down":
                            if Girl.bra_pulled_up:
                                $ Girl.bra_pulled_up = False
                            else:
                                $ Girl.bra_pulled_up = True
                        "Back":
                            jump wardrobe_menu

                    $ Girl.set_outfit_flags()
            "Bottom":
                while True:
                    menu:
                        "Remove [Girl.outfit[bottom]]" if Girl.outfit["bottom"]:
                            $ Girl.outfit["bottom"] = ""
                            $ Girl.bottom_pulled_down = False
                            $ Girl.upskirt = False
                        "Add skirt" if Girl not in [KittyX, JubesX]:
                            $ Girl.outfit["bottom"] = "_skirt"
                        "Add cosplay skirt" if Girl == LauraX:
                            $ Girl.outfit["bottom"] = "_cosplay_skirt"
                        "Add blue skirt" if Girl == KittyX:
                            $ Girl.outfit["bottom"] = "_blue_skirt"
                        "Add pants" if Girl != KittyX:
                            $ Girl.outfit["bottom"] = "_pants"
                        "Add black jeans" if Girl == KittyX:
                            $ Girl.outfit["bottom"] = "_black_jeans"
                        "Add capri pants" if Girl == KittyX:
                            $ Girl.outfit["bottom"] = "_capris"
                        "Add shorts" if Girl in [KittyX, JeanX, JubesX]:
                            $ Girl.outfit["bottom"] = "_shorts"
                        "Add leather pants" if Girl == LauraX:
                            $ Girl.outfit["bottom"] = "_leather_pants"
                        "Add yoga pants" if Girl in [EmmaX, JeanX, StormX]:
                            $ Girl.outfit["bottom"] = "_yoga_pants"
                        "Add dress" if Girl in [KittyX, EmmaX]:
                            $ Girl.outfit["bottom"] = "_dress"
                        "Add cheerleader skirt" if Girl == RogueX:
                            $ Girl.outfit["bottom"] = "_cheerleader_skirt"
                        "Add classic outfit bottom" if Girl == RogueX:
                            $ Girl.outfit["bottom"] = "_classic"
                        "Add opaque fetish bottom" if Girl == RogueX:
                            $ Girl.outfit["bottom"] = "_opaque_fetish"
                        "Add sheer fetish bottom" if Girl == RogueX:
                            $ Girl.outfit["bottom"] = "_sheer_fetish"
                        "Add black and blue pants" if Girl == KittyX:
                            $ Girl.outfit["bottom"] = "_black_and_blue_pants"
                        "Add boots" if Girl == EmmaX:
                            $ EmmaX.outfit["boots"] = "_thigh_boots"
                        "Pull bottom up/down" if Girl.wearing_pants or Girl.wearing_shorts:
                            if Girl.bottom_pulled_down:
                                $ Girl.bottom_pulled_down = False
                            else:
                                $ Girl.bottom_pulled_down = True
                        "Pull skirt up/down" if Girl.wearing_skirt:
                            if Girl.upskirt:
                                $ Girl.upskirt = False
                            else:
                                $ Girl.upskirt = True
                        "Pull dress up/down" if Girl.wearing_dress:
                            if Girl.dress_upskirt:
                                $ Girl.dress_upskirt = False
                            else:
                                $ Girl.dress_upskirt = True
                        "Pull bottom aside" if Girl.wearing_bodysuit:
                            if Girl.bodysuit_bottom_pulled_aside:
                                $ Girl.bodysuit_bottom_pulled_aside = False
                            else:
                                $ Girl.bodysuit_bottom_pulled_aside = True
                        "Toggle grool":
                            if not Girl.grool:
                                $ Girl.grool = 1
                            elif Girl.grool == 1:
                                $ Girl.grool = 2
                            else:
                                $ Girl.grool  = 0
                        "Back":
                            jump wardrobe_menu

                    $ Girl.set_outfit_flags()
            "Panties & Hose":
                while True:
                    menu:
                        "Hose":
                            menu:
                                "Remove [Girl.outfit[hose]]" if Girl.outfit["hose"]:
                                    $ Girl.outfit["hose"] = ""
                                "Add stockings":
                                    $ Girl.outfit["hose"] = "_stockings"
                                "Add garterbelt":
                                    $ Girl.outfit["hose"] = "_garterbelt"
                                "Add stockings and garterbelt":
                                    $ Girl.outfit["hose"] = "_stockings_and_garterbelt"
                                "Add pantyhose":
                                    $ Girl.outfit["hose"] = "_pantyhose"
                                "Add ripped pantyhose":
                                    $ Girl.outfit["hose"] = "_ripped_pantyhose"
                                "Add tights" if Girl == RogueX:
                                    $ Girl.outfit["hose"] = "_tights"
                                "Add ripped tights" if Girl == RogueX:
                                    $ Girl.outfit["hose"] = "_ripped_tights"
                                "Add knee stockings" if Girl == KittyX:
                                    $ Girl.outfit["hose"] = "_knee_stockings"
                                "Add socks" if Girl == JubesX:
                                    $ Girl.outfit["hose"] = "_socks"
                                "Add black stockings" if Girl == LauraX:
                                    $ Girl.outfit["hose"] = "_black_stockings"
                        "Remove [Girl.outfit[underwear]]" if Girl.outfit["underwear"]:
                            $ Girl.outfit["underwear"] = ""
                            $ Girl.underwear_pulled_down = False
                        "Add lace panties":
                            $ Girl.outfit["underwear"] = "_lace_panties"
                        "Add bikini bottoms":
                            $ Girl.outfit["underwear"] = "_bikini_bottoms"
                        "Add green panties" if Girl != JubesX:
                            $ Girl.outfit["underwear"] = "_green_panties"
                        "Add black panties" if Girl not in [KittyX, JeanX, JubesX]:
                            $ Girl.outfit["underwear"] = "_black_panties"
                        "Add shorts" if Girl == RogueX:
                            $ Girl.outfit["underwear"] = "_shorts"
                        "Add white panties" if Girl in [EmmaX, StormX]:
                            $ Girl.outfit["underwear"] = "_white_panties"
                        "Add sports panties" if Girl == EmmaX:
                            $ Girl.outfit["underwear"] = "_sports_panties"
                        "Add wolvie panties" if Girl == LauraX:
                            $ Girl.outfit["underwear"] = "_wolvie_panties"
                        "Add cosplay panties" if Girl == StormX:
                            $ Girl.outfit["underwear"] = "_cosplay_panties"
                        "Add blue panties" if Girl == JubesX:
                            $ Girl.outfit["underwear"] = "_blue_panties"
                        "Add tiger panties" if Girl == JubesX:
                            $ Girl.outfit["underwear"] = "_tiger_panties"
                        "Add harness" if Girl == RogueX:
                            $ Girl.outfit["underwear"] = "_harness"
                        "Add kitty lingerie" if Girl == KittyX:
                            $ Girl.outfit["underwear"] = "_kitty_lingerie"
                        "Add nighty underwear" if Girl == KittyX:
                            $ Girl.outfit["underwear"] = "_nighty"
                        "Pull underwear up/down" if not Girl.outfit["bottom"]:
                            if Girl.underwear_pulled_down:
                                $ Girl.underwear_pulled_down = False
                            else:
                                $ Girl.underwear_pulled_down = True
                        "Toggle grool":
                            if not Girl.grool:
                                $ Girl.grool = 1
                            elif Girl.grool == 1:
                                $ Girl.grool = 2
                            else:
                                $ Girl.grool  = 0
                        "Back":
                            jump wardrobe_menu

                    $ Girl.set_outfit_flags()
            "Misc":
                while True:
                    menu:
                        "Emotions":
                            call face_editor(Girl)
                        "Toggle arm pose":
                            if Girl.arm_pose == 1:
                                if Girl == JeanX and Girl.outfit["bodysuit"] == "_sci_fi":
                                    $ Girl.outfit["bodysuit"] = ""

                                $ Girl.arm_pose = 2
                            else:
                                if Girl == EmmaX and Girl.outfit["bodysuit"] == "_domme_suit":
                                    $ Girl.outfit["bodysuit"] = ""
                                elif Girl == EmmaX and Girl.outfit["gloves"] == "_spiked_bracelets":
                                    $ Girl.outfit["gloves"] = ""

                                $ Girl.arm_pose = 1
                        "Toggle wet look":
                            if not Girl.wet:
                                $ Girl.wet = 1
                            elif Girl.wet == 1:
                                $ Girl.wet = 3
                            else:
                                $ Girl.wet  = 0
                        "Toggle pubes":
                            if not Girl.pubes:
                                $ Girl.pubes = "_hairy"
                            else:
                                $ Girl.pubes = ""
                        "Toggle hair" if Girl == RogueX:
                            if Girl.outfit["hair"] == "_cosplay":
                                $ Girl.outfit["hair"] = "_evo"
                            elif Girl.outfit["hair"] == "_evo":
                                $ Girl.outfit["hair"] = "_wet"
                            elif Girl.outfit["hair"] == "_wet":
                                $ Girl.outfit["hair"] = "_cosplay"

                            $ Girl.outfit["hair_back"] = Girl.outfit["hair"]
                        "Toggle hair" if Girl == KittyX:
                            if Girl.outfit["hair"] == "_long":
                                $ Girl.outfit["hair"] = "_evo"
                            elif Girl.outfit["hair"] == "_evo":
                                $ Girl.outfit["hair"] = "_wet"
                            elif Girl.outfit["hair"] == "_wet":
                                $ Girl.outfit["hair"] = "_long"

                            $ Girl.outfit["hair_back"] = Girl.outfit["hair"]
                        "Toggle hair" if Girl == JeanX:
                            if Girl.outfit["hair"] == "_pony":
                                $ Girl.outfit["hair"] = "_short"
                            elif Girl.outfit["hair"] == "_short":
                                $ Girl.outfit["hair"] = "_wet"
                            elif Girl.outfit["hair"] == "_wet":
                                $ Girl.outfit["hair"] = "_pony"

                            $ Girl.outfit["hair_back"] = Girl.outfit["hair"]
                        "Toggle hair" if Girl == StormX:
                            if Girl.outfit["hair"] == "_long":
                                $ Girl.outfit["hair"] = "_mohawk"
                            elif Girl.outfit["hair"] == "_mohawk":
                                $ Girl.outfit["hair"] = "_short"
                            elif Girl.outfit["hair"] == "_short":
                                $ Girl.outfit["hair"] = "_wet_long"
                            elif Girl.outfit["hair"] == "_wet_long":
                                $ Girl.outfit["hair"] = "_wet_mohawk"
                            elif Girl.outfit["hair"] == "_wet_mohawk":
                                $ Girl.outfit["hair"] = "_wet_short"
                            elif Girl.outfit["hair"] == "_wet_short":
                                $ Girl.outfit["hair"] = "_long"

                            $ Girl.outfit["hair_back"] = Girl.outfit["hair"]
                        "Toggle hat" if Girl == EmmaX:
                            if Girl.outfit["face_outer_accessory"] == "_hat":
                                $ Girl.outfit["face_outer_accessory"] = "_hat"
                            else:
                                $ Girl.outfit["face_outer_accessory"] = ""
                        "Toggle held item":
                            if not Girl.outfit["held_item"]:
                                $ Girl.outfit["held_item"]  = "_phone"
                            elif Girl.outfit["held_item"] == "_phone":
                                $ Girl.outfit["held_item"]  = "_dildo"
                            elif Girl.outfit["held_item"] == "_dildo":
                                $ Girl.outfit["held_item"]  = "_vibrator"
                            elif Girl.outfit["held_item"] == "_vibrator":
                                $ Girl.outfit["held_item"]  = "_panties"
                            else:
                                $ Girl.outfit["held_item"]  = ""
                        "Toggle gold necklace" if Girl in [KittyX, StormX]:
                            if not Girl.outfit["neck"]:
                                $ Girl.outfit["neck"] = "_gold_necklace"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle flower necklace" if Girl in [KittyX, StormX]:
                            if not Girl.outfit["neck"]:
                                $ Girl.outfit["neck"] = "_flower_necklace"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle ring necklace" if Girl == StormX:
                            if not Girl.outfit["neck"]:
                                $ Girl.outfit["neck"] = "_rings"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle arm rings" if Girl == StormX:
                            if not Girl.outfit["sleeves"]:
                                $ Girl.outfit["sleeves"] = "_rings"
                            else:
                                $ Girl.outfit["sleeves"] = ""
                        "Toggle leg rings" if Girl == StormX:
                            if not Girl.outfit["boots"]:
                                $ Girl.outfit["boots"] = "_rings"
                            else:
                                $ Girl.outfit["boots"] = ""
                        "Toggle sweater" if Girl == RogueX:
                            if Girl.outfit["belt"] != "_sweater":
                                $ Girl.outfit["belt"] = "_sweater"
                            else:
                                $ Girl.outfit["belt"] = ""
                        "Toggle spiked collar" if Girl in [RogueX, EmmaX]:
                            if Girl.outfit["neck"] != "_spiked_collar":
                                $ Girl.outfit["neck"] = "_spiked_collar"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle choker" if Girl == EmmaX:
                            if Girl.outfit["neck"] != "_choker":
                                $ Girl.outfit["neck"] = "_choker"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle leash" if Girl == LauraX:
                            if Girl.outfit["neck"] != "_leash_choker":
                                $ Girl.outfit["neck"] = "_leash_choker"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle boots" if Girl == EmmaX:
                            if Girl.outfit["boots"] != "_thigh_boots":
                                $ Girl.outfit["boots"] = "_thigh_boots"
                            else:
                                $ Girl.outfit["boots"] = ""
                        "Toggle suspenders" if Girl in [LauraX, JeanX]:
                            if Girl.outfit["suspenders"] == "_suspenders" and not Girl.suspenders_aside:
                                $ Girl.suspenders_aside = True
                            elif Girl.outfit["suspenders"] == "_suspenders" and Girl.suspenders_aside:
                                $ Girl.outfit["suspenders"] = ""
                            else:
                                $ Girl.outfit["suspenders"] = "_suspenders"
                        "Toggle diamond skin" if Girl == EmmaX:
                            if Girl.diamond:
                                $ Girl.diamond = False
                            else:
                                $ Girl.diamond = True
                        "Toggle claws" if Girl == LauraX:
                            $ Girl.arm_pose = 2

                            if Girl.claws:
                                $ Girl.claws = False
                            else:
                                $ Girl.claws = True
                        "Toggle psychic" if Girl == JeanX:
                            if Girl.eyes == "_psychic":
                                $ Girl.eyes = "_normal"
                            else:
                                $ Girl.eyes = "_psychic"
                        "Toggle powers" if Girl == StormX:
                            if Girl.eyes == "_white":
                                $ Girl.eyes = "_normal"
                            else:
                                $ Girl.eyes = "_white"
                        "Spunk locations":
                            menu:
                                "Mouth":
                                    if Girl.spunk["mouth"]:
                                        $ Girl.spunk["mouth"] = False
                                    else:
                                        $ Girl.spunk["mouth"] = True
                                "Chin":
                                    if Girl.spunk["chin"]:
                                        $ Girl.spunk["chin"] = False
                                    else:
                                        $ Girl.spunk["chin"] = True
                                "Face":
                                    if Girl.spunk["face"]:
                                        $ Girl.spunk["face"] = False
                                    else:
                                        $ Girl.spunk["face"] = True
                                "Hair":
                                    if Girl.spunk["hair"]:
                                        $ Girl.spunk["hair"] = False
                                    else:
                                        $ Girl.spunk["hair"] = True
                                "Tits":
                                    if Girl.spunk["breasts"]:
                                        $ Girl.spunk["breasts"] = False
                                    else:
                                        $ Girl.spunk["breasts"] = True
                                "Belly":
                                    if Girl.spunk["belly"]:
                                        $ Girl.spunk["belly"] = False
                                    else:
                                        $ Girl.spunk["belly"] = True
                                "Back":
                                    if Girl.spunk["back"]:
                                        $ Girl.spunk["back"] = False
                                    else:
                                        $ Girl.spunk["back"] = True
                                "Pussy":
                                    if Girl.spunk["pussy"]:
                                        $ Girl.spunk["pussy"] = False
                                    else:
                                        $ Girl.spunk["pussy"] = True
                                "Ass":
                                    if Girl.spunk["anus"]:
                                        $ Girl.spunk["anus"] = False
                                    else:
                                        $ Girl.spunk["anus"] = True
                                "Return":
                                    pass
                        "Toggle piercings":
                            if Girl.outfit["piercings"] == "_ring":
                                $ Girl.outfit["piercings"] = "_barbell"
                            elif Girl.outfit["piercings"] == "_barbell":
                                $ Girl.outfit["piercings"] = ""
                            else:
                                $ Girl.outfit["piercings"] = "_ring"
                        "Toggle gloves" if Girl in [RogueX, EmmaX]:
                            if Girl.outfit["gloves"]:
                                $ Girl.outfit["gloves"] = ""
                            else:
                                $ Girl.outfit["gloves"] = "_gloves"
                        "Toggle spiked bracelets" if Girl == EmmaX:
                            if Girl.outfit["gloves"]:
                                $ Girl.outfit["gloves"] = ""
                            else:
                                $ Girl.outfit["gloves"] = "_spiked_bracelets"
                        "Toggle wristbands" if Girl == LauraX:
                            if Girl.outfit["gloves"]:
                                $ Girl.outfit["gloves"] = ""
                            else:
                                $ Girl.outfit["gloves"] = "_wrists"
                        "Back":
                            jump wardrobe_menu
            "Nothing":
                return

        $ Girl.set_outfit_flags()

    return

label cheat_menu(Girl):
    while True:
        menu:
            "Level up":
                $ Girl.action_counter["handjob"] += 5
                $ Girl.action_counter["blowjob"] += 5
                $ Girl.event_counter["swallowed"] += 5
                $ Girl.action_counter["handjob"] += 5
                $ Girl.event_counter["ass_slapped"] += 5
                $ Girl.action_counter["titjob"] += 5
                $ Girl.action_counter["sex"] += 5
                $ Girl.action_counter["anal"] += 5
                $ Girl.action_counter["hotdog"] += 5
                $ Girl.action_counter["masturbation"] += 5
                $ Girl.event_counter["orgasmed"] += 5
                $ Girl.action_counter["fondle_breasts"] += 5
                $ Girl.action_counter["fondle_thighs"] += 5
                $ Girl.action_counter["fondle_pussy"] += 5
                $ Girl.action_counter["fondle_ass"] += 5
                $ Girl.action_counter["dildo_pussy"] += 5
                $ Girl.action_counter["dildo_ass"] += 5
                $ Girl.action_counter["suck_breasts"] += 5
                $ Girl.action_counter["finger_pussy"] += 5
                $ Girl.action_counter["finger_ass"] += 5
                $ Girl.action_counter["eat_pussy"] += 5
                $ Girl.action_counter["eat_ass"] += 5
                $ Girl.action_counter["blowjob"] += 5
                $ Girl.event_counter["swallowed"] += 5
                $ Girl.event_counter["creampied"] += 5
                $ Girl.event_counter["anal_creampied"] += 5
                $ Girl.seen_breasts = True
                $ Girl.seen_underwear = True
                $ Girl.seen_pussy = True
            "Level reset":
                $ Girl.action_counter["handjob"] = 0
                $ Girl.action_counter["blowjob"] = 0
                $ Girl.event_counter["swallowed"] = 0
            "Toggle taboo":
                if not taboo:
                    $ taboo = 40
                else:
                    $ taboo = 0
            "Maxed":
                $ Girl.love = 1000
                $ Girl.inhibition = 1000
                $ Girl.obedience = 1000
                $ Girl.lust = 50
                $ Girl.addiction = 0
                $ Girl.addiction_rate = 0
                $ Girl.action_counter["kiss"] = 1
                $ Girl.event_counter["swallowed"] = 0
            "50%%":
                $ Girl.love = 500
                $ Girl.inhibition = 500
                $ Girl.obedience = 500
                $ Girl.lust = 65
                $ Girl.addiction = 0
                $ Girl.addiction_rate = 10
                $ Girl.action_counter["kiss"] = 10
                $ Girl.event_counter["swallowed"] = 0
            "25%%":
                $ Girl.love = 250
                $ Girl.inhibition = 250
                $ Girl.obedience = 250
                $ Girl.lust = 85
                $ Girl.addiction = 10
                $ Girl.addiction_rate = 50
                $ Girl.action_counter["kiss"] = 10
                $ Girl.event_counter["swallowed"] = 0
            "Juice up":
                $ Player.semen = Player.max_semen
                $ Girl.remaining_actions = 10
            "Cold Shower":
                $ Player.focus = 0
            "Exit":
                return
