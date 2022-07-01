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
                    for G in [RogueX, KittyX]:
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
            "Unlock all clothes":
                python:
                    import copy

                    for G in all_Girls:
                        for C in all_Clothes:
                            if G.tag in C.Owner_names:
                                if C.name not in G.Wardrobe.Clothes.keys():
                                    G.Wardrobe.Clothes[C.name] = copy.deepcopy(C)

            "Return":
                call checkout

                return

label wardrobe_editor(Girl):
    while True:
        menu wardrobe_menu:
            "View":
                while True:
                    menu:
                        "Default":
                            call show_full_body(Girl)
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
            "Emotions":
                call face_editor(Girl)
            "Wardrobe":
                $ quit = False

                while not quit:
                    call screen Clothing_picker(Girl)

                    if _return != "quit":
                        $ Clothing_name = _return

                        $ currently_wearing = False

                        python:
                            for Clothing in Girl.Wardrobe.current_Outfit.Clothes.values():
                                if Clothing:
                                    if Clothing.name == Clothing_name:
                                        currently_wearing = True

                                        break

                        if currently_wearing:
                            $ Girl.change_out_of(Girl.Wardrobe.Clothes[Clothing_name].type)
                        else:
                            $ Girl.change_into(Clothing_name)
                    else:
                        $ quit = True
            "Misc":
                while True:
                    menu:
                        "Toggle arm pose":
                            if Girl.arm_pose == 1:
                                $ Girl.arm_pose = 2
                            else:
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
                        "Toggle diamond skin" if Girl == EmmaX:
                            if Girl.diamond:
                                $ Girl.diamond = False

                                if renpy.showing("Emma_sprite"):
                                    call show_Girl(EmmaX)
                            else:
                                $ Girl.diamond = True

                                if renpy.showing("Emma_sprite"):
                                    call show_Girl(EmmaX)
                        "Toggle claws" if Girl == LauraX:
                            $ Girl.arm_pose = 2

                            if Girl.claws:
                                $ Girl.claws = False
                            else:
                                $ Girl.claws = True
                        "Toggle psychic" if Girl == JeanX:
                            if Girl.eyes == "psychic":
                                $ Girl.eyes = "normal"
                            else:
                                $ Girl.eyes = "psychic"
                        "Toggle powers" if Girl == StormX:
                            if Girl.eyes == "white":
                                $ Girl.eyes = "normal"
                            else:
                                $ Girl.eyes = "white"
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
                        "Back":
                            jump wardrobe_menu
            "Back":
                return

    return

label face_editor(Girl):
    while True:
        menu:
            "First set":
                menu:
                    "Normal":
                        $ Girl.emotion = "normal"
                    "Angry":
                        $ Girl.emotion = "angry"
                    "Smiling":
                        $ Girl.emotion = "smile"
                    "Sexy":
                        $ Girl.emotion = "sexy"
                    "Suprised":
                        $ Girl.emotion = "surprised"
                    "Bemused":
                        $ Girl.emotion = "bemused"
                    "Manic":
                        $ Girl.emotion = "manic"
            "Second set":
                menu:
                    "Sad":
                        $ Girl.emotion = "sad"
                    "Sucking":
                        $ Girl.emotion = "sucking"
                    "Kiss":
                        $ Girl.emotion = "kiss"
                    "Tongue":
                        $ Girl.emotion = "tongue"
                    "Confused":
                        $ Girl.emotion = "confused"
                    "Closed":
                        $ Girl.emotion = "closed"
                    "Down":
                        $ Girl.emotion = "down"
            "Third set":
                menu:
                    "Sadside":
                        $ Girl.emotion = "sadside"
                    "Startled":
                        $ Girl.emotion = "startled"
                    "Perplexed":
                        $ Girl.emotion = "perplexed"
                    "Sly":
                        $ Girl.emotion = "sly"
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
