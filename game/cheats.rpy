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
                            call reset_position(Girl)
                        # "Face":
                        #     call kiss_launch(Girl)
                        # "Body":
                        #     call pussy_launch(Girl)
                        "Handjob":
                            if not renpy.showing(Girl.tag + " handjob"):
                                call handjob_launch(Girl)
                            else:
                                call reset_position(Girl)
                        "Titjob":
                            if not renpy.showing(Girl.tag + " titjob"):
                                call titjob_launch(Girl)
                            else:
                                call reset_position(Girl)
                        "Blowjob":
                            if not renpy.showing(Girl.tag + " blowjob"):
                                call blowjob_launch(Girl)
                            else:
                                call reset_position(Girl)
                        "Missionary":
                            $ Girl.pose = "sex"

                            if not renpy.showing(Girl.tag + " sex"):
                                call sex_launch(Girl, "sex")
                            else:
                                call reset_position(Girl)
                        "Doggy":
                            $ Girl.pose = "doggy"

                            if not renpy.showing(Girl.tag + " doggy"):
                                call sex_launch(Girl, "anal")
                            else:
                                call reset_position(Girl)
                        "Back":
                            jump wardrobe_menu
            "First casual outfit":
                $ Girl.change_outfit("casual1")
            "Second casual outfit":
                $ Girl.change_outfit("casual2")
            "Halloween costume":
                $ Girl.change_outfit("costume")
            "Domme outfit" if Girl == EmmaX:
                $ Girl.arm_pose = 2
                $ Girl.change_outfit("domme_outfit")
            "Nude":
                $ Girl.change_outfit("nude")
            "Dress/Suit":
                while True:
                    menu:
                        "Remove [Girl.outfit[dress]]" if Girl.outfit["dress"]:
                            $ Girl.outfit["dress"] = ""
                        "Add catsuit" if Girl == RogueX:
                            $ Girl.outfit["dress"] = "_catsuit"
                        "Add Raven outfit" if Girl == RogueX:
                            $ Girl.outfit["back_outer_accessory"] = "_raven_cloak"
                            $ Girl.outfit["dress"] = "_raven"
                            $ Girl.outfit["cloak"] = "_raven_cloak"
                        "Add blue dress" if Girl == RogueX:
                            $ Girl.outfit["dress"] = "_blue_dress"
                        "Add one-piece swimsuit" if Girl == RogueX:
                            $ Girl.outfit["dress"] = "_onepiece_swimsuit"
                        "Add sexy swimsuit" if Girl == RogueX:
                            $ Girl.outfit["dress"] = "_sexy_swimsuit"
                        "Add red dress" if Girl == RogueX:
                            $ Girl.outfit["dress"] = "_red_dress"
                        "Add Chinese dress" if Girl == KittyX:
                            $ Girl.outfit["dress"] = "_chinese"
                        "Add sci-fi suit" if Girl == JeanX:
                            $ Girl.arm_pose = 1
                            $ Girl.outfit["bottom"] = ""
                            $ Girl.outfit["dress"] = "_sci_fi"
                        "Back":
                            jump wardrobe_menu
            "Top":
                while True:
                    menu:
                        "Remove [Girl.outfit[top]]" if Girl.outfit["top"]:
                            $ Girl.outfit["top"] = ""
                        "Remove [Girl.outfit[jacket]]" if Girl.outfit["jacket"]:
                            $ Girl.outfit["jacket"] = ""
                        "Add mesh top" if Girl == RogueX:
                            $ Girl.outfit["top"] = "_mesh_top"
                        "Add pink top" if Girl in [RogueX, KittyX]:
                            $ Girl.outfit["top"] = "_pink_top"
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
                        "Open/close jacket" if Girl == JubesX and Girl.outfit["jacket"] in ["_jacket", "_shut_jacket"]:
                            if Girl.outfit["jacket"] == "_jacket":
                                $ Girl.outfit["jacket"] = "_shut_jacket"
                            else:
                                $ Girl.outfit["jacket"] = "_jacket"
                        "Wide open jacket" if Girl == JubesX and Girl.outfit["jacket"] in ["_jacket", "_open_jacket"]:
                            if Girl.outfit["jacket"] == "_jacket":
                                $ Girl.outfit["jacket"] = "_open_jacket"
                            else:
                                $ Girl.outfit["jacket"] = "_jacket"
                        "Add white_shirt" if Girl == StormX:
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
                            $ Girl.outfit["top"] = "_towel"
                        "Back":
                            jump wardrobe_menu
            "Bra":
                while True:
                    menu:
                        "Remove [Girl.outfit[bra]]" if Girl.outfit["bra"]:
                            $ Girl.outfit["bra"] = ""
                        "Add sports bra":
                            $ Girl.outfit["bra"] = "_sports_bra"
                        "Add bikini":
                            $ Girl.outfit["bra"] = "_bikini_top"
                        "Add lace bra" if Girl != KittyX:
                            $ Girl.outfit["bra"] = "_lace_bra"
                        "Add tank top" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_tank"
                        "Add buttoned tank top" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_buttoned_tank"
                        "Add tube top" if Girl in [RogueX, StormX]:
                            $ Girl.outfit["bra"] = "_tube_top"
                        "Add basic bra" if Girl in [RogueX, KittyX, EmmaX, LauraX, JubesX]:
                            $ Girl.outfit["bra"] = "_bra"
                        "Add cami" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_cami"
                        "Add dress top" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_dress"
                        "Add leather bra" if Girl == LauraX:
                            $ Girl.outfit["bra"] = "_leather_bra"
                        "Add white tank" if Girl == LauraX:
                            $ Girl.outfit["bra"] = "_white_tank"
                        "Add wolvie panties" if Girl == LauraX:
                            $ Girl.outfit["bra"] = "_wolvie_bra"
                        "Add green bra" if Girl == JeanX:
                            $ Girl.outfit["bra"] = "_green_bra"
                        "Add black bra" if Girl == StormX:
                            $ Girl.outfit["bra"] = "_black_bra"
                        "Add cosplay bra" if Girl == StormX:
                            $ Girl.outfit["bra"] = "_cosplay_bra"
                        "Add corset" if Girl == EmmaX:
                            $ Girl.outfit["bra"] = "_corset"
                        "Add lace corset" if Girl == EmmaX:
                            $ Girl.outfit["bra"] = "_lace_corset"
                        "Add classic top" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_classic"
                        "Add harness" if Girl == RogueX:
                            $ Girl.outfit["bra"] = "_harness"
                        "Add kitty lingerie" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_kitty_lingerie"
                        "Add orange top" if Girl == KittyX:
                            $ Girl.outfit["bra"] = "_orange_top"
                        "Toggle up-top":
                            if Girl.top_pulled_up:
                                $ Girl.top_pulled_up = False
                            else:
                                $ Girl.top_pulled_up = True
                        "Back":
                            jump wardrobe_menu
            "Bottom":
                while True:
                    menu:
                        "Remove [Girl.outfit[bottom]]" if Girl.outfit["bottom"]:
                            $ Girl.outfit["bottom"] = ""
                        "Add skirt" if Girl != KittyX:
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
                        "Toggle upskirt":
                            if Girl.upskirt:
                                $ Girl.upskirt = False
                            else:
                                $ Girl.upskirt = True
                        "Back":
                            jump wardrobe_menu
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
                                "Add tights":
                                    $ Girl.outfit["hose"] = "_tights"
                                "Add ripped pantyhose":
                                    $ Girl.outfit["hose"] = "_ripped_pantyhose"
                                "Add ripped tights":
                                    $ Girl.outfit["hose"] = "_ripped_tights"
                                "Add knee stockings" if Girl == KittyX:
                                    $ Girl.outfit["hose"] = "_knee_stockings"
                                "Add socks" if Girl == JubesX:
                                    $ Girl.outfit["hose"] = "_socks"
                                "Add black stockings" if Girl == LauraX:
                                    $ Girl.outfit["hose"] = "_black_stockings"
                        "Remove [Girl.outfit[underwear]]" if Girl.outfit["underwear"]:
                            $ Girl.outfit["underwear"] = ""
                        "Add green panties":
                            $ Girl.outfit["underwear"] = "_green_panties"
                        "Add lace panties":
                            $ Girl.outfit["underwear"] = "_lace_panties"
                        "Add bikini bottoms":
                            $ Girl.outfit["underwear"] = "_bikini_bottoms"
                        "Add black panties" if Girl != JeanX:
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
                        "Add harness" if Girl == RogueX:
                            $ Girl.outfit["underwear"] = "_harness"
                        "Add kitty lingerie" if Girl == KittyX:
                            $ Girl.outfit["underwear"] = "_kitty_lingerie"
                        "Add nighty underwear" if Girl == KittyX:
                            $ Girl.outfit["underwear"] = "_nighty"
                        "Toggle underwear up/down":
                            if Girl.underwear_pulled_down:
                                $ Girl.underwear_pulled_down = 0
                            else:
                                $ Girl.underwear_pulled_down = 1
                        "Toggle grool":
                            if not Girl.grool:
                                $ Girl.grool = 1
                            elif Girl.grool == 1:
                                $ Girl.grool = 2
                            else:
                                $ Girl.grool  = 0
                        "Back":
                            jump wardrobe_menu
            "Misc":
                while True:
                    menu:
                        "Emotions":
                            call face_editor(Girl)
                        "Toggle arm pose":
                            if Girl.arm_pose == 1:
                                if Girl == JeanX and Girl.outfit["dress"] == "_sci_fi":
                                    $ Girl.outfit["dress"] = ""

                                $ Girl.arm_pose = 2
                            else:
                                if Girl == EmmaX and Girl.outfit["dress"] == "_dommef":
                                    $ Girl.outfit["dress"] = ""
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

                            $ Girl.outfit["back_hair"] = Girl.outfit["hair"]
                        "Toggle hair" if Girl == KittyX:
                            if Girl.outfit["hair"] == "_long":
                                $ Girl.outfit["hair"] = "_evo"
                            elif Girl.outfit["hair"] == "_evo":
                                $ Girl.outfit["hair"] = "_wet"
                            elif Girl.outfit["hair"] == "_wet":
                                $ Girl.outfit["hair"] = "_long"

                            $ Girl.outfit["back_hair"] = Girl.outfit["hair"]
                        "Toggle hair" if Girl == JeanX:
                            if Girl.outfit["hair"] == "_pony":
                                $ Girl.outfit["hair"] = "_short"
                            elif Girl.outfit["hair"] == "_short":
                                $ Girl.outfit["hair"] = "_wet"
                            elif Girl.outfit["hair"] == "_wet":
                                $ Girl.outfit["hair"] = "_pony"

                            $ Girl.outfit["back_hair"] = Girl.outfit["hair"]
                        "Toggle hair" if Girl == StormX:
                            if Girl.outfit["hair"] == "_long":
                                $ Girl.outfit["hair"] = "_mohawk"
                            elif Girl.outfit["hair"] == "_mohawk":
                                $ Girl.outfit["hair"] = "_short"
                            elif Girl.outfit["hair"] == "_short":
                                $ Girl.outfit["hair"] = "_wet"
                            elif Girl.outfit["hair"] = "_wet":
                                $ Girl.outfit["hair"] = "_long"

                            $ Girl.outfit["back_hair"] = Girl.outfit["hair"]
                        "Toggle hat" if Girl == EmmaX:
                            if Girl.outfit["hair"] == "_wavy":
                                $ Girl.outfit["face_outer_accessory"] = "_hat"
                            elif Girl.outfit["hair"] == "_wet":
                                $ Girl.outfit["face_outer_accessory"] = "_wet_hat"
                            elif Girl.outfit["hair"] in ["_hat", "_wet_hat"]:
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
                        "Toggle rings" if Girl == StormX:
                            if not Girl.outfit["front_outer_accessory"]:
                                $ Girl.outfit["front_outer_accessory"] = "_rings"
                            else:
                                $ Girl.outfit["front_outer_accessory"] = ""
                        "Toggle sweater" if Girl == RogueX:
                            if Girl.outfit["scarf"] != "_sweater":
                                $ Girl.outfit["scarf"] = "_sweater"
                            else:
                                $ Girl.outfit["scarf"] = ""
                        "Toggle spiked collar" if Girl in [RogueX, LauraX]:
                            if Girl.outfit["neck"] != "_spiked_collar":
                                $ Girl.outfit["neck"] = "_spiked_collar"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle choker" if Girl == EmmaX:
                            if Girl.outfit["neck"] != "_choker":
                                $ Girl.outfit["neck"] = "_choker"
                            else:
                                $ Girl.outfit["neck"] = ""
                        "Toggle boots" if Girl == EmmaX:
                            if Girl.outfit["boots"] != "_thigh_boots":
                                $ Girl.outfit["boots"] = "_thigh_boots"
                            else:
                                $ Girl.outfit["boots"] = ""
                        "Toggle suspenders" if Girl in [LauraX, JeanX]:
                            if Girl.outfit["suspenders"] == "_suspenders":
                                $ Girl.outfit["suspenders"] = "_suspenders2"
                            elif Girl.outfit["suspenders"] == "_suspenders2":
                                $ Girl.outfit["suspenders"] = ""
                            else:
                                $ Girl.outfit["suspenders"] = "_suspenders"
                        "Toggle Raven cloak" if Girl == RogueX:
                            if Girl.outfit["cloak"] == "_raven_cloak":
                                $ Girl.outfit["back_outer_accessory"] = ""
                                $ Girl.outfit["cloak"] = ""
                            else:
                                $ Girl.outfit["back_outer_accessory"] = "_raven_cloak"
                                $ Girl.outfit["cloak"] = "_raven_cloak"
                        "Toggle diamond mode" if Girl == EmmaX:
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
                        "Back":
                            jump wardrobe_menu
            "Nothing":
                return
    return

label cheat_menu(Girl):
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

    jump cheat_menu
