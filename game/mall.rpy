label sex_shop:
    $ Player.location = "bg_shop"

    python:
        for G in Player.Party:
            G.location = "bg_shop"

    call set_the_scene

    "You head into \"Spiral's Body Shoppe\". . ."

    while True:
        $ Girl = None

        if round <= 20:
            "It's getting late, you head back into the mall. . ."

            return

        menu:
            "What did you want to purchase?"
            "Buy dildo for $20.":
                if Player.inventory.count("_dildo") >= 10:
                    "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
                elif Player.cash >= 20:
                    "You purchase a dildo."

                    $ Player.inventory.append("_dildo")
                    $ Player.cash -= 20

                    if Player.Party:
                        if approval_check(Player.Party[0], 800):
                            $ Player.Party[0].change_face("_sly")
                            $ Player.Party[0].change_stat("love", 80, 1)
                            $ Player.Party[0].change_stat("obedience", 50, 3)
                            $ Player.Party[0].change_stat("inhibition", 50, 3)

                            if Player.Party[0] == RogueX:
                                ch_r "Oh, what's that for, [Player.Party[0].player_petname]?"
                            elif Player.Party[0] == KittyX:
                                ch_k "Is that for. . ."
                            elif Player.Party[0] == EmmaX:
                                ch_e "Hmm. . ."
                            elif Player.Party[0] == LauraX:
                                ch_l ". . ."
                            elif Player.Party[0] == JeanX:
                                pass
                            elif Player.Party[0] == StormX:
                                ch_s "Well that's certainly interesting. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "What're you gonna do with that. . ."
                        else:
                            $ Player.Party[0].change_face("_confused",2)
                            $ Player.Party[0].change_stat("love", 60, -2)
                            $ Player.Party[0].change_stat("obedience", 70, 4)
                            $ Player.Party[0].change_stat("inhibition", 50, 2)

                            if Player.Party[0] == RogueX:
                                ch_r "Is that. . . oh. . ."
                            elif Player.Party[0] == KittyX:
                                ch_k "Um, what's that about. . ."
                            elif Player.Party[0] == EmmaX:
                                ch_e "This is certainly an unusual trip. . ."
                            elif Player.Party[0] == LauraX:
                                ch_l ". . ."
                            elif Player.Party[0] == JeanX:
                                pass
                            elif Player.Party[0] == StormX:
                                ch_s "Interesting choice. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "What're you gonna do with that. . ."

                            $ Player.Party[0].change_face("_confused", 1)

                        $ Player.Party[0].change_stat("lust", 60, 5)
                else:
                    "You don't have enough for that."
            "Buy \"Shocker\" vibrator for $25.":
                if Player.inventory.count("_vibrator") >= 10:
                    "If you bought one more vibrator, you would risk a geological event."
                elif Player.cash >= 25:
                    "You purchase a vibrator."

                    $ Player.inventory.append("_vibrator")
                    $ Player.cash -= 25

                    if Player.Party:
                        if approval_check(Player.Party[0], 800):
                            $ Player.Party[0].change_face("_sly")
                            $ Player.Party[0].change_stat("love", 80, 2)
                            $ Player.Party[0].change_stat("obedience", 50, 2)
                            $ Player.Party[0].change_stat("inhibition", 50, 3)

                            if Player.Party[0] == RogueX:
                                ch_r "Oh, what's that for, [Player.Party[0].player_petname]?"
                            elif Player.Party[0] == KittyX:
                                ch_k "Is that for. . ."
                            elif Player.Party[0] == EmmaX:
                                ch_e "Hmm. . ."
                            elif Player.Party[0] == LauraX:
                                ch_l ". . ."
                            elif Player.Party[0] == JeanX:
                                pass
                            elif Player.Party[0] == StormX:
                                ch_s "Well that's certainly interesting. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "What're you gonna do with that. . ."

                            $ Player.Party[0].change_stat("lust", 60, 5)
                        else:
                            $ Player.Party[0].change_face("_confused",2)
                            $ Player.Party[0].change_stat("obedience", 70, 2)
                            $ Player.Party[0].change_stat("inhibition", 50, 2)

                            if Player.Party[0] == RogueX:
                                ch_r "Is that. . . oh. . ."
                            elif Player.Party[0] == KittyX:
                                ch_k "Um, what's that about. . ."
                            elif Player.Party[0] == EmmaX:
                                ch_e "This is certainly an unusual trip. . ."
                            elif Player.Party[0] == LauraX:
                                ch_l ". . ."
                            elif Player.Party[0] == JeanX:
                                pass
                            elif Player.Party[0] == StormX:
                                ch_s "Interesting choice. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "What're you gonna do with that. . ."

                            $ Player.Party[0].change_face("_confused", 1)
                else:
                    "You don't have enough for that."
            "Give a gift to [RogueX.name]." if RogueX in Player.Party:
                $ Girl = RogueX
            "Give a gift to [KittyX.name]." if KittyX in Player.Party:
                $ Girl = KittyX
            "Give a gift to [EmmaX.name]." if EmmaX in Player.Party:
                $ Girl = EmmaX
            "Give a gift to [LauraX.name]." if LauraX in Player.Party:
                $ Girl = LauraX
            "Give a gift to [JeanX.name]." if JeanX in Player.Party:
                $ Girl = JeanX
            "Give a gift to [StormX.name]." if StormX in Player.Party:
                $ Girl = StormX
            "Give a gift to [JubesX.name]." if JubesX in Player.Party:
                $ Girl = JubesX
            "Exit.":
                "You head back into the mall. . ."

                $ round -= 10 if round > 20 else round - 10

                $ Player.location = "bg_mall"

                python:
                    for G in Player.Party:
                        G.location = "bg_mall"

                call set_the_scene

                return

        if Girl:
            menu:
                "Gift her a dildo" if "_dildo" in Player.inventory:
                    if "_dildo" not in Girl.inventory:
                        "You give [Girl.name] the dildo."

                        $ Girl.blushing = "_blush1"
                        $ Girl.arm_pose = 2
                        $ Girl.outfit["held_item"] = "_dildo"

                        if approval_check(Girl, 800):
                            $ Player.inventory.remove("_dildo")

                            $ Girl.inventory.append("_dildo")
                            $ Girl.change_face("_bemused")
                            $ Girl.change_stat("love", 200, 30)
                            $ Girl.change_stat("obedience", 200, 30)
                            $ Girl.change_stat("inhibition", 200, 30)

                            if Girl == RogueX:
                                ch_r "Well, I've got some ideas in mind for this. . ."
                            elif Girl == LauraX:
                                ch_l "Oh, cool, I've wanted one of these. . ."
                            else:
                                Girl.voice "I'm sure I can find some place to store it. . ."

                            $ Girl.change_stat("lust", 89, 10)
                        elif approval_check(Girl, 600):
                            $ Player.inventory.remove("_dildo")

                            $ Girl.inventory.append("_dildo")
                            $ Girl.change_face("_confused")

                            if Girl != EmmaX:
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)

                            if Girl == RogueX:
                                ch_r "Huh, well I guess I can find a place for it. . ."

                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_surprised")

                                ch_r "I- I mean. . . I'll just put it away."
                            elif Girl == KittyX:
                                ch_k "I don't know what. . ."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_surprised")

                                ch_k "Oh!"
                                ch_k "Oh. . . I'll just[Girl.like]put it away."
                            elif Girl == EmmaX:
                                ch_e "This is not an appropriate gift from a student. . ."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_sadside", 1)

                                ch_e "Hm. . ."

                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                $ Girl.change_face("_sly")

                                ch_e "I suppose I can find {i}some{/i} use for it. . ."
                            elif Girl == LauraX:
                                ch_l "Huh, you're a weird gift giver."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_smile")

                                ch_l "It's very thoughtful though."
                            elif Girl == JeanX:
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)

                                ch_j "Well we know where your mind it at."

                                $ Girl.change_face("_smile")

                                ch_j "I guess I should be flattered. . ."
                            elif Girl == StormX:
                                if StormX not in Rules:
                                    $ Girl.change_face("_sadside", 1)

                                    ch_s "I don't know that I should accept this from a student. . ."

                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.change_stat("lust", 89, 10)

                                ch_s "Hm. . ."

                                $ Girl.change_face("_sly")

                                ch_s "Thank you for the thought. . ."
                            elif Girl == JubesX:
                                ch_v "I guess I have some use for it. . ."

                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_surprised")

                                ch_v "I- I mean. . . decorative."

                            $ Girl.change_face("_bemused")
                        elif "offered gift" in Girl.daily_history:
                            $ Girl.change_face("_angry")

                            "She hands it back to you."

                            if Girl == RogueX:
                                ch_r "Look, maybe you should just rethink your gift-giving choices?"
                            elif Girl == KittyX:
                                ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                            elif Girl == EmmaX:
                                ch_e "I think I have made myself clear about inappropriate gifts?"
                            elif Girl == LauraX:
                                ch_l "I said I can't take something like this."
                            elif Girl == JeanX:
                                ch_j "I really don't need this."
                            elif Girl == StormX:
                                ch_s "I repeat, this is not something I need."
                            elif Girl == JubesX:
                                ch_v "This really isn't something I need. . ."
                        else:
                            $ Girl.change_face("_angry")
                            $ Girl.change_stat("love", 50, -20)
                            $ Girl.change_stat("obedience", 20, 10)
                            $ Girl.change_stat("inhibition", 20, 20)

                            if Girl == RogueX:
                                ch_r "That's a pretty forward gift to be giving a lady. . ."
                            elif Girl == KittyX:
                                ch_k "I- you shouldn't be giving girls stuff like this!"
                            elif Girl == EmmaX:
                                ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                            elif Girl == LauraX:
                                ch_l "I don't think you should just be handing these out to random chicks."
                            elif Girl == JeanX:
                                ch_j "So you just go around handing out sex toys?"
                            elif Girl == StormX:
                                ch_s "I do not appreciate the implication here."
                            elif Girl == JubesX:
                                ch_v "This is an odd design for a. . . wait."

                            $ Girl.change_stat("lust", 89, 5)

                            "She hands it back to you."

                            $ Girl.daily_history.append("offered gift")
                    elif Girl.inventory.count("_dildo") == 1:
                        $ Player.inventory.remove("_dildo")

                        $ Girl.inventory.append("_dildo")

                        if Girl == RogueX:
                            ch_r "Well, I suppose I could always use another. . ."
                        elif Girl == KittyX:
                            ch_k "Why stop with one. . ."
                        elif Girl == EmmaX:
                            ch_e "I suppose I always have room for one more. . ."
                        elif Girl == LauraX:
                            ch_l "I don't know if I need another. . ."
                        elif Girl == JeanX:
                            ch_j "Oh look, another rubber cock. . ."
                        elif Girl == StormX:
                            ch_s "Oh, another one. . ."
                        elif Girl == JubesX:
                            ch_v "I don't need more. . ."
                    else:
                        if Girl == RogueX:
                            ch_r "Honestly, [Girl.player_petname], I already have enough of those."
                        elif Girl == KittyX:
                            ch_k "I only have so many places to store these."
                        elif Girl == EmmaX:
                            ch_e "How many places do you think I could put these?"
                        elif Girl == LauraX:
                            ch_l "I'm running out of space at this point."
                        elif Girl == JeanX:
                            ch_j "How many holes do you think a girl has?"
                        elif Girl == StormX:
                            ch_s "I doubt I can find a place for this one."
                        elif Girl == JubesX:
                            ch_v "This is way too many. . ."

                    $ Girl.outfit["held_item"] = None

                    $ Girl = None
                "Gift her a vibrator" if "_vibrator" in Player.inventory:
                    if "_vibrator" not in Girl.inventory:
                        "You give [Girl.name] the Shocker Vibrator."

                        $ Girl.blushing = "_blush1"
                        $ Girl.arm_pose = 2
                        $ Girl.outfit["held_item"] = "_vibrator"

                        if approval_check(Girl, 700):
                            $ Player.inventory.remove("_vibrator")

                            $ Girl.inventory.append("_vibrator")
                            $ Girl.change_face("_bemused")
                            $ Girl.change_stat("love", 200, 30)
                            $ Girl.change_stat("obedience", 200, 30)
                            $ Girl.change_stat("inhibition", 200, 30)

                            if Girl == RogueX:
                                ch_r "Well, I've got some ideas in mind for this. . ."
                            elif Girl == KittyX:
                                ch_k "Well this is. . . [[bzzzt]- "
                                ch_k "-interesting. . ."
                            elif Girl == EmmaX:
                                ch_e "How very thoughtful of you. . ."

                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_sly")

                                ch_e "I'm sure I can put this to good use. . ."
                            elif Girl == LauraX:
                                ch_l "This is. . . [[bzzzt]- "

                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_sly")

                                ch_l "-some kind of sex thing, huh. . ."
                            elif Girl == JeanX:
                                ch_j "Oh, nifty."
                            elif Girl == StormX:
                                ch_s "Oh!. . . oooohhh."
                            elif Girl == JubesX:
                                ch_v "Oh, this could be nice. . ."

                            $ Girl.change_stat("lust", 89, 10)
                        elif approval_check(Girl, 400):
                            $ Player.inventory.remove("_vibrator")

                            $ Girl.inventory.append("_vibrator")
                            $ Girl.change_face("_confused")
                            $ Girl.change_stat("love", 200, 10)
                            $ Girl.change_stat("obedience", 200, 10)
                            $ Girl.change_stat("inhibition", 200, 10)

                            if Girl == RogueX:
                                ch_r "I guess I can use this to work the kinks out. . ."

                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_surprised")

                                ch_r "Muscle knots, I mean!"
                            elif Girl == KittyX:
                                ch_k "I've heard these are very relaxing. . ."

                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_surprised")

                                ch_k "-for my back!"
                            elif Girl == EmmaX:
                                ch_e "How very thoughtful of you. . ."

                                $ Girl.change_stat("lust", 89, 10)
                                $ Girl.change_face("_sly")

                                ch_e "A back massager, I assume. . ."
                            elif Girl == LauraX:
                                ch_l "This is. . . [[bzzzt]- "

                                $ Girl.change_face("_sly")
                                $ Girl.change_stat("lust", 89, 10)

                                ch_l "-oooh. . ."
                            elif Girl == JeanX:
                                ch_j "Huh. Ok."
                            elif Girl == StormX:
                                ch_s "Oh, something for exercise purposes. . ."
                            elif Girl == JubesX:
                                ch_v "Thanks, my, uh, back's been killing me. . ."

                            $ Girl.change_face("_bemused", 1)
                        elif "offered gift" in Girl.daily_history:
                            $ Girl.change_face("_angry")

                            "She hands it back to you."

                            if Girl == RogueX:
                                ch_r "Look, maybe you should just rethink your gift-giving choices?"
                            elif Girl == KittyX:
                                ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                            elif Girl == EmmaX:
                                ch_e "I think I have made myself clear about inappropriate gifts?"
                            elif Girl == LauraX:
                                ch_l "I don't want it."
                            elif Girl == JeanX:
                                ch_j "I really don't need this."
                            elif Girl == StormX:
                                ch_s "I repeat, this is not something I need."
                            elif Girl == JubesX:
                                ch_v "I don't need this. . ."
                        else:
                            $ Girl.change_face("_angry")
                            $ Girl.change_stat("love", 50, -20)
                            $ Girl.change_stat("obedience", 20, 10)
                            $ Girl.change_stat("inhibition", 20, 20)

                            if Girl == RogueX:
                                ch_r "I don't think I have much use for that."
                            elif Girl == KittyX:
                                ch_k "I can't really see the point."
                            elif Girl == EmmaX:
                                ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                            elif Girl == LauraX:
                                ch_l "I don't need it."
                            elif Girl == JeanX:
                                ch_j "Huh. No, I don't need this."
                            elif Girl == StormX:
                                ch_s "I have no use for this."
                            elif Girl == JubesX:
                                ch_v "Put that away. . ."

                            $ Girl.change_stat("lust", 89, 5)

                            "She hands it back to you."

                            $ Girl.daily_history.append("offered gift")
                    else:
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname], I only need the one."
                        elif Girl == EmmaX:
                            ch_e "I already have plenty."
                        else:
                            Girl.voice "I already have one of these."

                    $ Girl.outfit["held_item"] = None

                    $ Girl = None
                "Never mind":
                    $ Girl = None

    return

label swimsuit_shop:
    $ Player.location = "bg_shop"

    python:
        for G in Player.Party:
            G.location = "bg_shop"

    call set_the_scene

    "You head into \"The Swimsuit Issue\". . ."

    while True:
        $ Girl = None

        if round <= 20:
            "It's getting late, you head back into the mall. . ."

            return

        menu:
            "What did you want to do?"
            "Have [RogueX.name] try something on." if RogueX in Player.Party:
                $ Girl = RogueX
            "Have [KittyX.name] try something on." if KittyX in Player.Party:
                $ Girl = KittyX
            "Have [EmmaX.name] try something on." if EmmaX in Player.Party:
                $ Girl = EmmaX
            "Have [LauraX.name] try something on." if LauraX in Player.Party:
                $ Girl = LauraX
            "Have [JeanX.name] try something on." if JeanX in Player.Party:
                $ Girl = JeanX
            "Have [StormX.name] try something on." if StormX in Player.Party:
                $ Girl = StormX
            "Have [JubesX.name] try something on." if JubesX in Player.Party:
                $ Girl = JubesX
            "Exit.":
                "You head back into the mall. . ."

                $ round -= 10 if round > 20 else round - 10

                $ Player.location = "bg_mall"

                python:
                    for G in Player.Party:
                        G.location = "bg_mall"

                call set_the_scene

                return

        if Girl:
            call shift_focus(Girl)

            $ Girl.change_face("_smile", 1)

            if Girl.swimwear["outfit_active"]:
                if Girl == RogueX:
                    ch_r "I'm already set on that. . ."
                elif Girl == KittyX:
                    ch_k "I[KittyX.like]don't think I really need -another- one. . ."
                elif Girl == EmmaX:
                    ch_e "I don't really need more of those. . ."
                elif Girl == LauraX:
                    ch_l "I already have a suit. . ."
                elif Girl == JeanX:
                    ch_j "Oh, I don't need one of those."
                elif Girl == StormX:
                    ch_s "I have plenty of those. . ."
                elif Girl == JubesX:
                    ch_v "I already got one!"

                $ Girl = None
            elif approval_check(Girl, 800) or approval_check(Girl, 600, "L") or approval_check(Girl, 300, "O"):
                if Girl == RogueX:
                    ch_r "Oh, we're looking for a nice suit?"
                elif Girl == KittyX:
                    ch_k "Oh, um, I guess we could shop for suits. . ."
                elif Girl == EmmaX:
                    ch_e "I suppose we could pick something out. . ."
                elif Girl == LauraX:
                    ch_l "Oh, I guess I do need a suit. . ."
                elif Girl == JeanX:
                    ch_j "Oh, what're you getting?"
                elif Girl == StormX:
                    ch_s "I suppose I should get something for the pool area. . ."
                elif Girl == JubesX:
                    ch_v "I guess I do need a new suit now. . ."
            else:
                if Girl == RogueX:
                    ch_r "Oh, no thank you."
                elif Girl == KittyX:
                    ch_k "Oh, um, I don't really need one. . ."
                elif Girl == EmmaX:
                    ch_e "I think that's a bit inappropriate. . ."
                elif Girl == LauraX:
                    ch_l "Not interested. . ."
                elif Girl == JeanX:
                    ch_j "No, I'm good."
                elif Girl == StormX:
                    ch_s "I don't think that I should. . ."
                elif Girl == JubesX:
                    ch_v "I don't really want to shop for that. . ."

                $ Girl = None

        if Girl:
            $ Player.Party.remove(Girl)
            $ Player.Party.append(Girl)

            "You grab some things and head into one of the dressing rooms with [Girl.name]."

            if len(Player.Party) > 2:
                menu:
                    Player.Party[0].voice "Should we come in too?"
                    "Sure.":
                        "The rest follow you in."

                        python:
                            for G in Player.Party:
                                G.location = "bg_dressing"
                    "Stay out here.":
                        Player.Party[0].voice "Fine, we'll wait out here."

                        $ Player.Party = [Girl]

                        $ Girl.location = "bg_dressing"
            elif len(Player.Party) == 2:
                menu:
                    Player.Party[0].voice "Should I come in too?"
                    "Sure.":
                        "[Player.Party[0].name] follows you in."

                        python:
                            for G in Player.Party:
                                G.location = "bg_dressing"
                    "Stay out here.":
                        Player.Party[0].voice "Fine, I'll just wait here then."

                        $ Player.Party = [Girl]

                        $ Girl.location = "bg_dressing"

            $ Player.location = "bg_dressing"

            $ door_locked = True

            call set_the_scene
            call set_Character_taboos

            $ cart = []
            $ leave = False

            while Girl:
                $ item = None

                menu:
                    "What did you want to try on here?"
                    "Bikini top" if Girl.outfit["bra"] != "_bikini_top":
                        $ item = "_bikini_top"
                    "Bikini top (locked)" if Girl.outfit["bra"] == "_bikini_top":
                        pass
                    "Bikini bottoms" if Girl.outfit["underwear"] != "_bikini_bottoms":
                        $ item = "_bikini_bottoms"
                    "Bikini bottoms (locked)" if Girl.outfit["underwear"] == "_bikini_bottoms":
                        pass
                    "Blue swimskirt" if Girl == KittyX and Girl.outfit["bottom"] != "_blue_skirt":
                        $ item = "_blue_skirt"
                    "Blue swimskirt (locked)" if Girl == KittyX and Girl.outfit["bottom"] == "_blue_skirt":
                        pass
                    "Leave dressing area.":
                        $ leave = True

                if item:
                    if item in bras:
                        if Girl.seen_breasts or approval_check(Girl, 1100, taboo_modifier = 2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_bra(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["jacket"] = ""
                            $ Girl.outfit["top"] = ""
                            $ Girl.outfit["dress"] = ""
                            $ Girl.outfit["bodysuit"] = ""
                            $ Girl.outfit["bra"] = item

                            hide black_screen onlayer black
                    elif item in underwears:
                        if Girl.seen_pussy or approval_check(Girl, 1200, taboo_modifier = 2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_underwear(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["bodysuit"] = ""
                            $ Girl.outfit["dress"] = ""
                            $ Girl.outfit["bottom"] = ""
                            $ Girl.outfit["hose"] = ""
                            $ Girl.outfit["underwear"] = item

                            hide black_screen onlayer black
                    elif item in skirts:
                        $ Girl.change_face("_smile")

                        if Girl.seen_pussy or (Girl.outfit["underwear"] and Girl.seen_underwear) or (Girl.outfit["underwear"] and approval_check(Girl, 900, taboo_modifier = 2)) or approval_check(Girl, 1200, taboo_modifier = 2):

                            Girl.voice "Sure. . ."

                            call change_bottom(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["bottom"] = item

                            hide black_screen onlayer black

                    if item in cart:
                        pass
                    elif item in Girl.inventory:
                        if item in bras or item in skirts:
                            Girl.voice "I do already have one of these though."
                        elif item in underwears:
                            Girl.voice "I do already have some of these though."
                    else:
                        $ cart.append(item)

                        if Girl == StormX and item in ["_bikini_top", "_bikini_bottoms"] and (Girl.outfit["bra"] == "_bikini_top" or Girl.outfit["underwear"] == "_bikini_bottoms"):
                            ch_s "Oh! I understand the purpose of the flap now!"
                elif leave:
                    if cart and len(Player.Party) > 1:
                        if Player.Party[0].location == Player.location and Player.Party[0] not in [LauraX, JeanX] and Player.Party[0].likes[Girl.tag] >= 500:
                            $ Player.Party[0].change_face("_smile")

                            if Player.Party[0] == RogueX:
                                ch_r "Look'in good there. . ."
                            elif Player.Party[0] == KittyX:
                                ch_k "Oh, that looks cute on you!"
                            elif Player.Party[0] == EmmaX:
                                ch_e "You really do wear that well. . ."
                            elif Player.Party[0] == StormX:
                                ch_s "That really does suit you. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "So cute!"

                            $ Girl.change_face("_smile")

                            if Girl == RogueX:
                                ch_r "Aw, thanks. . ."
                            elif Girl == KittyX:
                                ch_k "Right?"
                            elif Girl == EmmaX:
                                ch_e "Obviously. . ."
                            elif Girl == LauraX:
                                ch_l "Ok, cool. . ."
                            elif Girl == JeanX:
                                ch_j "Of course it does. . ."
                            elif Girl == StormX:
                                ch_s "Oh, thank you. . ."
                            elif Girl == JubesX:
                                ch_v "I know, right?"

                            $ Girl.change_likes(Player.Party[0],5)

                            $ Player.Party[0].change_likes(Girl,3)

                    $ Girl.change_outfit()

                    $ door_locked = False

                    $ Player.location = "bg_shop"

                    call check_who_is_present

                    $ Player.Party = Present[:]
                    $ Player.Party.remove(Girl)
                    $ Player.Party.append(Girl)

                    call set_the_scene
                    call set_Character_taboos

                    if not cart:
                        "That was fun, but since there wasn't anything she was interested in, she put it all back."

                    while cart:
                        $ item = None

                        menu:
                            "So what did you want to buy?"
                            "The top." if "_bikini_top" in cart:
                                $ item = "_bikini_top"
                            "The bottoms." if "_bikini_bottoms" in cart:
                                $ item = "_bikini_bottoms"
                            "The skirt." if "_blue_skirt" in cart:
                                $ item = "_blue_skirt"
                            "Nothing." if "purchased" not in Player.recent_history:
                                $ Girl.change_face("_sad")

                                if "shopblock" not in Girl.daily_history:
                                    $ Girl.add_word(1,"shopblock","shopblock")
                                    $ Girl.change_stat("love", 50, -2)
                                    $ Girl.change_stat("love", 90, -2)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 3)

                                "You put all the stuff back."

                                if Girl in [EmmaX, StormX]:
                                    Girl.voice "How disappointing."
                                elif Girl in [LauraX, JeanX]:
                                    pass
                                else:
                                    Girl.voice "Aw. . ."

                                $ cart = []
                            "Done." if "purchased" in Player.recent_history:
                                "You put all the remaining stuff back."

                                $ cart = []

                        if item:
                            if Girl.tag + item in Player.inventory:
                                if item in bras or item in skirts:
                                    "Wait, you already have one of those."
                                    "You pull out the one in your bag and give it to [Girl.name]."
                                elif item in underwears:
                                    "Wait, you already have a pair of these."
                                    "You pull out the pair in your bag and give them to [Girl.name]."

                                $ Player.inventory.remove(Girl.tag + item)
                            else:
                                if item == "_bikini_top":
                                    if Girl in [KittyX, EmmaX, StormX]:
                                        $ cost = 50
                                    else:
                                        $ cost = 60
                                elif item == "_bikini_bottoms":
                                    if Girl in [KittyX, EmmaX, StormX]:
                                        $ cost = 60
                                    else:
                                        $ cost = 50
                                elif item == "_blue_skirt":
                                    $ cost = 50

                                if Player.cash < cost:
                                    "You look at the tag - it's $[cost]. You can't afford it."

                                    $ cart.remove(item)
                                else:
                                    $ Player.cash -= cost

                            if item in cart:
                                $ cart.remove(item)

                                $ Player.add_word(1,"purchased")

                                $ Girl.inventory.append(item)
                                $ Girl.change_face("_bemused", 1)
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)

                                if item == "_bikini_top":
                                    if Girl == RogueX:
                                        ch_r "A little skimpy. . ."
                                    elif Girl == KittyX:
                                        ch_k "Aw, a cute Kitty. . . hole. . ."
                                    elif Girl == EmmaX:
                                        ch_e "This does show off my assets, doesn't it. . ."
                                    elif Girl == LauraX:
                                        ch_l "\"X\", cute. . ."
                                    elif Girl == JeanX:
                                        ch_j "Yeah, this'll work. . ."
                                    elif Girl == StormX:
                                        ch_s "I think I can recognize the design. . ."
                                    elif Girl == JubesX:
                                        ch_v "Ooo, so Cal. . ."
                                elif item == "_bikini_bottoms":
                                    if Girl == RogueX:
                                        ch_r "I was thinking about a tan. . ."
                                    elif Girl == KittyX:
                                        ch_k "A little snug, maybe. . ."
                                    elif Girl == EmmaX:
                                        ch_e "I don't know that a student should be buying me swimwear. . ."
                                    elif Girl == LauraX:
                                        ch_l "Ok, cool. . ."
                                    elif Girl == JeanX:
                                        ch_j "Ooo, these are nice. . ."
                                    elif Girl == StormX:
                                        ch_s "Where have I seen this cut before. . ."
                                    elif Girl == JubesX:
                                        ch_v "Maybe a little small. . ."
                                elif item == "_blue_skirt":
                                    ch_k "This is a cute skirt. . ."

                    $ Player.drain_word("purchased")

                    if Girl == KittyX and ("_blue_skirt" in Girl.inventory or Girl.inhibition >= 400) and "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                        $ Girl.swimwear["outfit_active"] = 1
                    elif "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                        $ Girl.swimwear["outfit_active"] = 1

                    $ Girl = None

    return

label lingerie_shop:
    $ Player.location = "bg_shop"

    python:
        for G in Player.Party:
            G.location = "bg_shop"

    call set_the_scene

    "You head into \"Stacy's\". . ."

    while True:
        $ Girl = None

        if round <= 20:
            "It's getting late, you head back into the mall. . ."

            return

        menu:
            "What did you want to do?"
            "Have [RogueX.name] try something on." if RogueX in Player.Party:
                $ Girl = RogueX
            "Have [KittyX.name] try something on." if KittyX in Player.Party:
                $ Girl = KittyX
            "Have [EmmaX.name] try something on." if EmmaX in Player.Party:
                $ Girl = EmmaX
            "Have [LauraX.name] try something on." if LauraX in Player.Party:
                $ Girl = LauraX
            "Have [JeanX.name] try something on." if JeanX in Player.Party:
                $ Girl = JeanX
            "Have [StormX.name] try something on." if StormX in Player.Party:
                $ Girl = StormX
            "Have [JubesX.name] try something on." if JubesX in Player.Party:
                $ Girl = JubesX
            "Exit.":
                "You head back into the mall. . ."

                $ round -= 10 if round > 20 else round - 10

                $ Player.location = "bg_mall"

                python:
                    for G in Player.Party:
                        G.location = "bg_mall"

                call set_the_scene

                return

        if Girl:
            call shift_focus(Girl)

            $ Girl.change_face("_smile", 1)

            if approval_check(Girl, 800) or approval_check(Girl, 600, "L") or approval_check(Girl, 300, "O"):
                if Girl == RogueX:
                    ch_r "Oh, this looks spicy. . ."
                elif Girl == KittyX:
                    ch_k "Um, I don't know. . ."
                elif Girl == EmmaX:
                    ch_e "I'm not sure where this is heading. . ."
                elif Girl == LauraX:
                    ch_l "Oh?"
                elif Girl == JeanX:
                    ch_j "Oh, what're you getting?"
                elif Girl == StormX:
                    ch_s "I will see where you are heading with this. . ."
                elif Girl == JubesX:
                    ch_v "Ok, interesting play here. . ."
            else:
                if Girl == RogueX:
                    ch_r "Oh, no thank you."
                elif Girl == KittyX:
                    ch_k "Oh, um, I don't really need anything from here. . ."
                elif Girl == EmmaX:
                    ch_e "I think that's a bit inappropriate. . ."
                elif Girl == LauraX:
                    ch_l "Not interested. . ."
                elif Girl == JeanX:
                    ch_j "No, I'm good."
                elif Girl == StormX:
                    ch_s "I don't think that I should. . ."
                elif Girl == JubesX:
                    ch_v "I don't really want to shop for that. . ."

                $ Girl = None

        if Girl:
            $ Player.Party.remove(Girl)
            $ Player.Party.append(Girl)

            "You grab some things and head into one of the dressing rooms with [Girl.name]."

            if len(Player.Party) > 2:
                menu:
                    Player.Party[0].voice "Should we come in too?"
                    "Sure.":
                        "The rest follow you in."

                        python:
                            for G in Player.Party:
                                G.location = "bg_dressing"
                    "Stay out here.":
                        Player.Party[0].voice "Fine, we'll wait out here."

                        $ Player.Party = [Girl]

                        $ Girl.location = "bg_dressing"
            elif len(Player.Party) == 2:
                menu:
                    Player.Party[0].voice "Should I come in too?"
                    "Sure.":
                        "[Player.Party[0].name] follows you in."

                        python:
                            for G in Player.Party:
                                G.location = "bg_dressing"
                    "Stay out here.":
                        Player.Party[0].voice "Fine, I'll just wait here then."

                        $ Player.Party = [Girl]

                        $ Girl.location = "bg_dressing"

            $ Player.location = "bg_dressing"

            $ door_locked = True

            call set_the_scene
            call set_Character_taboos

            $ cart = []
            $ leave = False

            while Girl:
                $ item = None

                menu:
                    "What did you want to try on here?"
                    "Lace bra" if Girl != LauraX and Girl.outfit["bra"] != "_lace_bra":
                        $ item = "_lace_bra"
                    "Lace bra (locked)" if Girl.outfit["bra"] == "_lace_bra":
                        pass
                    "Corset" if Girl in [LauraX, JeanX] and Girl.outfit["bra"] != "_corset":
                        $ item = "_corset"
                    "Corset (locked)" if Girl in [LauraX, JeanX] and Girl.outfit["bra"] == "_corset":
                        pass
                    "Lace corset" if Girl == LauraX and Girl.outfit["bra"] != "_lace_corset":
                        $ item = "_lace_corset"
                    "Lace corset (locked)" if Girl.outfit["bra"] == "_lace_corset":
                        pass
                    "Lace panties" if Girl.outfit["underwear"] != "_lace_panties":
                        $ item = "_lace_panties"
                    "Lace panties (locked)" if Girl.outfit["underwear"] == "_lace_panties":
                        pass
                    "Tiger-striped panties" if Girl == JubesX and Girl.outfit["underwear"] != "_tiger_panties":
                        $ item = "_tiger_panties"
                    "Tiger-striped panties (locked)" if Girl.outfit["underwear"] == "_tiger_panties":
                        pass
                    "Pantyhose" if Girl.outfit["hose"] != "_pantyhose":
                        $ item = "_pantyhose"
                    "Pantyhose (locked)" if Girl.outfit["hose"] == "_pantyhose":
                        pass
                    "Stockings and garterbelt" if Girl.outfit["hose"] != "_stockings_and_garterbelt":
                        $ item = "_stockings_and_garterbelt"
                    "Stockings and garterbelt (locked)" if Girl.outfit["hose"] == "_stockings_and_garterbelt":
                        pass
                    "Knee stockings" if Girl == KittyX and Girl.outfit["hose"] != "_knee_stockings":
                        $ item = "_knee_stockings"
                    "Knee stockings (locked)" if Girl.outfit["hose"] == "_knee_stockings":
                        pass
                    "High socks" if Girl == JubesX and Girl.outfit["hose"] != "_socks":
                        $ item = "_socks"
                    "High socks (locked)" if Girl.outfit["hose"] == "_socks":
                        pass
                    "Nighty" if Girl in [RogueX, KittyX] and Girl.outfit["top"] != "_nighty":
                        $ item = "_nighty"
                    "Nighty (locked)" if Girl.outfit["top"] == "_nighty":
                        pass
                    "Harness bra" if Girl == RogueX and Girl.outfit["bra"] != "_harness_bra":
                        $ item = "_harness_bra"
                    "Harness bra (locked)" if Girl.outfit["bra"] == "_harness_bra":
                        pass
                    "Kitty bra" if Girl == KittyX and Girl.outfit["bra"] != "_kitty_bra":
                        $ item = "_kitty_bra"
                    "Kitty bra (locked)" if Girl.outfit["bra"] == "_kitty_bra":
                        pass
                    "Orange top" if Girl == KittyX and Girl.outfit["bra"] != "_orange_top":
                        $ item = "_orange_top"
                    "Orange top (locked)" if Girl.outfit["bra"] == "_orange_top":
                        pass
                    "Harness panties" if Girl == RogueX and Girl.outfit["underwear"] != "_harness_panties":
                        $ item = "_harness_panties"
                    "Harness panties (locked)" if Girl.outfit["underwear"] == "_harness_panties":
                        pass
                    "Kitty panties" if Girl == KittyX and Girl.outfit["underwear"] != "_kitty_panties":
                        $ item = "_kitty_panties"
                    "Kitty panties (locked)" if Girl.outfit["underwear"] == "_kitty_panties":
                        pass
                    "Nighty panties" if Girl == KittyX and Girl.outfit["underwear"] != "_nighty_panties":
                        $ item = "_nighty_panties"
                    "Nighty panties (locked)" if Girl.outfit["underwear"] == "_nighty_panties":
                        pass
                    "Take off the [Girl.outfit[hose]]." if Girl.outfit["hose"]:
                        if Girl.outfit["hose"] != "_pantyhose" or approval_check(Girl, 900, taboo_modifier = 2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            if Girl.outfit["hose"] in hoses:
                                call change_hose(Girl, "")
                            elif Girl.outfit["hose"] in socks:
                                call change_socks(Girl, "")
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Leave dressing area.":
                        $ leave = True

                if item:
                    if item in bras or item == "_nighty":
                        if "no_gift_bra" in Girl.recent_history:
                            Girl.voice "I said no. . ."

                            $ item = None
                        elif not Girl.seen_breasts and not approval_check(Girl, 900):
                            $ Girl.change_face("_angry",2)

                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in [JeanX, LauraX]:
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, definitely not. . ."

                            $ Girl.recent_history.append("no_gift_bra")
                            $ Girl.change_face("_angry", 1)

                            $ item = None
                    elif item in underwears or item in hoses:
                        if "no_gift_panties" in Girl.recent_history:
                            Girl.voice "I said no. . ."

                            $ item = None
                        elif "no_gift_bra" in Girl.recent_history:
                            Girl.voice "Why would this be okay instead?"

                            $ item = None
                        elif not Girl.seen_pussy and not approval_check(Girl, 1000):
                            $ Girl.change_face("_angry",2)

                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in [JeanX, LauraX]:
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, not really interested. . ."

                            $ Girl.recent_history.append("no_gift_panties")
                            $ Girl.change_face("_angry", 1)

                if item:
                    if item in bras:
                        if Girl.seen_breasts or approval_check(Girl, 1000, taboo_modifier=2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_bra(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["jacket"] = ""
                            $ Girl.outfit["top"] = ""
                            $ Girl.outfit["dress"] = ""
                            $ Girl.outfit["bodysuit"] = ""
                            $ Girl.outfit["bra"] = item

                            hide black_screen onlayer black
                    elif item in underwears:
                        if Girl.seen_pussy or approval_check(Girl, 1200, taboo_modifier=2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_underwear(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["dress"] = ""
                            $ Girl.outfit["bodysuit"] = ""
                            $ Girl.outfit["bottom"] = ""
                            $ Girl.outfit["underwear"] = item

                            hide black_screen onlayer black
                    elif item in hoses:
                        if Girl.seen_pussy or approval_check(Girl, 900, taboo_modifier = 2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_hose(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["dress"] = ""
                            $ Girl.outfit["bodysuit"] = ""
                            $ Girl.outfit["bottom"] = ""
                            $ Girl.outfit["hose"] = item

                            hide black_screen onlayer black
                    elif item in socks:
                        $ Girl.change_face("_sexy")

                        Girl.voice "Sure. . ."

                        call change_socks(Girl, item, redress = False)

                        $ Girl.outfit["hose"] = item
                    elif item in tops:
                        if Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_top(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["top"] = item

                            hide black_screen onlayer black

                    if item in cart:
                        pass
                    elif item in Girl.inventory:
                        if item in bras or item in tops:
                            Girl.voice "I do already have one of these though."
                        elif item in underwears or item in hoses or item in socks:
                            Girl.voice "I do already have some of these though."
                    else:
                        $ cart.append(item)
                elif leave:
                    if cart and len(Player.Party) > 1:
                        if Player.Party[0].location == Player.location and Player.Party[0] not in [LauraX, JeanX] and Player.Party[0].likes[Girl.tag] >= 500:
                            $ Player.Party[0].change_face("_smile")

                            if Player.Party[0] == RogueX:
                                ch_r "Look'in good there. . ."
                            elif Player.Party[0] == KittyX:
                                ch_k "Oh, that looks cute on you!"
                            elif Player.Party[0] == EmmaX:
                                ch_e "You really do wear that well. . ."
                            elif Player.Party[0] == StormX:
                                ch_s "That really does suit you. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "So cute!"

                            $ Girl.change_face("_smile")

                            if Girl == RogueX:
                                ch_r "Aw, thanks. . ."
                            elif Girl == KittyX:
                                ch_k "Right?"
                            elif Girl == EmmaX:
                                ch_e "Obviously. . ."
                            elif Girl == LauraX:
                                ch_l "Ok, cool. . ."
                            elif Girl == JeanX:
                                ch_j "Of course it does. . ."
                            elif Girl == StormX:
                                ch_s "Oh, thank you. . ."
                            elif Girl == JubesX:
                                ch_v "I know, right?"

                            $ Girl.change_likes(Player.Party[0],5)

                            $ Player.Party[0].change_likes(Girl,3)

                    $ Girl.change_outfit()

                    $ door_locked = False

                    $ Player.location = "bg_shop"

                    call check_who_is_present

                    $ Player.Party = Present[:]
                    $ Player.Party.remove(Girl)
                    $ Player.Party.append(Girl)

                    call set_the_scene
                    call set_Character_taboos

                    if not cart:
                        "That was fun, but since there wasn't anything she was interested in, she put it all back."

                    while cart:
                        $ item = None

                        menu:
                            "So what did you want to buy?"
                            "The lace bra." if "_lace_bra" in cart:
                                $ item = "_lace_bra"
                            "The corset." if "_corset" in cart:
                                $ item = "_corset"
                            "The lace corset." if "_lace_corset" in cart:
                                $ item = "_lace_corset"
                            "The lace panties." if "_lace_panties" in cart:
                                $ item = "_lace_panties"
                            "The tiger-striped panties." if "_tiger_panties" in cart:
                                $ item = "_tiger_panties"
                            "The pantyhose." if "_pantyhose" in cart:
                                $ item = "_pantyhose"
                            "The stockings and garterbelt." if "_stockings_and_garterbelt" in cart:
                                $ item = "_stockings_and_garterbelt"
                            "The knee stockings." if "_knee_stockings" in cart:
                                $ item = "_knee_stockings"
                            "The high socks." if "_socks" in cart:
                                $ item = "_socks"
                            "The nighty." if "_nighty" in cart:
                                $ item = "_nighty"
                            "The harness bra." if "_harness_bra" in cart:
                                $ item = "_harness_bra"
                            "The kitty bra." if "_kitty_bra" in cart:
                                $ item = "_kitty_bra"
                            "The orange top." if "_orange_top" in cart:
                                $ item = "_orange_top"
                            "The harness panties." if "_harness_panties" in cart:
                                $ item = "_harness_panties"
                            "The kitty panties." if "_kitty_panties" in cart:
                                $ item = "_kitty_panties"
                            "The nighty panties." if "_nighty_panties" in cart:
                                $ item = "_nighty_panties"
                            "Nothing." if "purchased" not in Player.recent_history:
                                $ Girl.change_face("_sad")

                                if "shopblock" not in Girl.daily_history:
                                    $ Girl.add_word(1,"shopblock","shopblock")
                                    $ Girl.change_stat("love", 50, -2)
                                    $ Girl.change_stat("love", 90, -2)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 3)

                                "You put all the stuff back."

                                if Girl in [EmmaX, StormX]:
                                    Girl.voice "How disappointing."
                                elif Girl in [LauraX, JeanX]:
                                    pass
                                else:
                                    Girl.voice "Aw. . ."

                                $ cart = []
                            "Done." if "purchased" in Player.recent_history:
                                "You put all the remaining stuff back."

                                $ cart = []

                        if item:
                            if Girl.tag + item in Player.inventory:
                                if item in bras or item in tops:
                                    "Wait, you already have one of those."
                                    "You pull out the one in your bag and give it to [Girl.name]."
                                elif item in underwears or item in hoses or item in socks:
                                    "Wait, you already have a pair of these."
                                    "You pull out the pair in your bag and give them to [Girl.name]."
                            else:
                                if item in ["_lace_bra", "_lace_corset"]:
                                    $ cost = 90
                                elif item == ["_corset", "_kitty_panties"]:
                                    $ cost = 70
                                elif item in ["_lace_panties"]:
                                    $ cost = 110
                                elif item in ["_tiger_panties", "_stockings_and_garterbelt"]:
                                    $ cost = 100
                                elif item in ["_pantyhose", "_knee_stockings", "_socks", "_orange_top", "_nighty_panties"]:
                                    $ cost = 50
                                elif item == ["_nighty", "_kitty_bra"]:
                                    $ cost = 75

                                if Player.cash < cost:
                                    "You look at the tag - it's $[cost]. You can't afford it."

                                    $ cart.remove(item)
                                else:
                                    $ Player.cash -= cost

                            if item in cart:
                                $ cart.remove(item)

                                $ Player.add_word(1,"purchased")

                                $ Girl.inventory.append(item)
                                $ Girl.change_face("_bemused", 1)

                                if item == "_lace_bra":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    if Girl == RogueX:
                                        ch_r "I don't know that I'd wear this out, but maybe in private."
                                    elif Girl == KittyX:
                                        ch_k "At least you appreciate what I've got."
                                    elif Girl == EmmaX:
                                        ch_e "I'm not exactly running low on this sort of thing. . ."
                                    elif Girl == StormX:
                                        ch_s "It is not that I do not appreciate it, but. . ."
                                    elif Girl == JeanX:
                                        ch_j "Good tastes. . ."
                                    elif Girl == JubesX:
                                        ch_v "It's not my usual style. . ."
                                elif item == "_corset":
                                    $ Girl.change_stat("love", 200, 15)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 10)

                                    if Girl == LauraX:
                                        ch_l "This is. . . kinda cool. . ."
                                    elif Girl == JeanX:
                                        ch_j "Thanks?"
                                elif item == "_lace_corset":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 30)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    ch_l "You think this'd look good on me?"
                                elif item == "_harness_bra":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 30)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                    $ Girl.mouth = "_lipbite"

                                    ch_r "But never did mind a wardrobe change."
                                elif item == "_lace_panties":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    if Girl == RogueX:
                                        ch_r "These are a bit flimsy. . ."
                                    elif Girl == KittyX:
                                        ch_k "These don't leave much to the imagination. . ."
                                    elif Girl == EmmaX:
                                        ch_e "This is an. . . unsual gift."

                                        $ EmmaX.change_face("_sly", 1)

                                        ch_e "But I'll hold on to them. . ."
                                    elif Girl == LauraX:
                                        ch_l "These are pretty hot. . ."
                                    elif Girl == JeanX:
                                        ch_j "Oh, these are nice. . ."
                                    elif Girl == StormX:
                                        ch_s "I suppose I could always use another pair. . ."
                                    elif Girl == JubesX:
                                        ch_v "A little. . . intimate. . ."
                                elif item == "_tiger_panties":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    ch_v "These are stink'in cute. . ."
                                elif item == "_harness_panties":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                    $ Girl.mouth = "_lipbite"

                                    ch_r "But never did mind a wardrobe change."
                                elif item == "_pantyhose":
                                    $ Girl.change_stat("love", 200, 5)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 200, 5)

                                    Girl.voice "These are lovely. . ."
                                elif item == "_stockings_and_garterbelt":
                                    $ Girl.change_stat("love", 200, 5)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 200, 5)

                                    if Girl == EmmaX:
                                        ch_e "These are lovely. . ."
                                    elif Girl == StormX:
                                        ch_s "You think I could pull these off?"
                                    else:
                                        Girl.voice "These are pretty nice. . ."
                                elif item == "_knee_stockings":
                                    $ Girl.change_stat("love", 200, 5)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 200, 5)

                                    Girl.voice "These are pretty nice. . ."
                                elif item == "_socks":
                                    $ Girl.change_stat("love", 200, 5)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 200, 5)

                                    Girl.voice "These are pretty nice. . ."
                                elif item == "_nighty":
                                    $ Girl.change_stat("love", 200, 40)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 30)

                                    if Girl == RogueX:
                                        ch_r "Well, it's a little revealing, but still pretty cute."

                                    $ Girl.change_stat("lust", 89, 10)

                    $ Player.drain_word("purchased")

                    $ Girl = None

    return

label clothing_shop:
    $ Player.location = "bg_shop"

    python:
        for G in Player.Party:
            G.location = "bg_shop"

    call set_the_scene

    "You head into \"Urban Big-Titter's\". . ."

    while True:
        $ Girl = None

        if round <= 20:
            "It's getting late, you head back into the mall. . ."

            return

        menu:
            "What did you want to do?"
            "Have [RogueX.name] try something on." if RogueX in Player.Party:
                $ Girl = RogueX
            "Have [KittyX.name] try something on." if KittyX in Player.Party:
                $ Girl = KittyX
            "Have [EmmaX.name] try something on." if EmmaX in Player.Party:
                $ Girl = EmmaX
            "Have [LauraX.name] try something on." if LauraX in Player.Party:
                $ Girl = LauraX
            "Have [JeanX.name] try something on." if JeanX in Player.Party:
                $ Girl = JeanX
            "Have [StormX.name] try something on." if StormX in Player.Party:
                $ Girl = StormX
            "Have [JubesX.name] try something on." if JubesX in Player.Party:
                $ Girl = JubesX
            "Exit.":
                "You head back into the mall. . ."

                $ round -= 10 if round > 20 else round - 10

                $ Player.location = "bg_mall"

                python:
                    for G in Player.Party:
                        G.location = "bg_mall"

                call set_the_scene

                return

        if Girl:
            call shift_focus(Girl)

            $ Girl.change_face("_smile", 1)

            # if approval_check(Girl, 800) or approval_check(Girl, 600, "L") or approval_check(Girl, 300, "O"):
            "This is placeholder dialogue."

        if Girl:
            $ Player.Party.remove(Girl)
            $ Player.Party.append(Girl)

            "You grab some things and head into one of the dressing rooms with [Girl.name]."

            if len(Player.Party) > 2:
                menu:
                    Player.Party[0].voice "Should we come in too?"
                    "Sure.":
                        "The rest follow you in."

                        python:
                            for G in Player.Party:
                                G.location = "bg_dressing"
                    "Stay out here.":
                        Player.Party[0].voice "Fine, we'll wait out here."

                        $ Player.Party = [Girl]

                        $ Girl.location = "bg_dressing"
            elif len(Player.Party) == 2:
                menu:
                    Player.Party[0].voice "Should I come in too?"
                    "Sure.":
                        "[Player.Party[0].name] follows you in."

                        python:
                            for G in Player.Party:
                                G.location = "bg_dressing"
                    "Stay out here.":
                        Player.Party[0].voice "Fine, I'll just wait here then."

                        $ Player.Party = [Girl]

                        $ Girl.location = "bg_dressing"

            $ Player.location = "bg_dressing"

            $ door_locked = True

            call set_the_scene
            call set_Character_taboos

            $ cart = []
            $ leave = False

            while Girl:
                $ item = None

                menu:
                    "What did you want to try on here?"
                    "Raven cloak" if Girl == RogueX and Girl.outfit["cloak"] != "_raven_cloak":
                        $ item = "_raven_cloak"
                    "Raven cloak (locked)" if Girl.outfit["cloak"] == "_raven_cloak":
                        pass
                    "Classic jacket" if Girl == RogueX and Girl.outfit["jacket"] != "_classic_jacket":
                        $ item = "_classic_jacket"
                    "Classic jacket (locked)" if Girl.outfit["jacket"] == "_classic_jacket":
                        pass
                    "Opaque fetish top" if Girl == RogueX and Girl.outfit["top"] != "_opaque_fetish_top":
                        $ item = "_opaque_fetish_top"
                    "Opaque fetish top (locked)" if Girl.outfit["top"] == "_opaque_fetish_top":
                        pass
                    "Sheer fetish top" if Girl == RogueX and Girl.outfit["top"] != "_sheer_fetish_top":
                        $ item = "_sheer_fetish_top"
                    "Sheer fetish top (locked)" if Girl.outfit["top"] == "_sheer_fetish_top":
                        pass
                    "Opaque fetish pants" if Girl == RogueX and Girl.outfit["bottom"] != "_opaque_fetish_pants":
                        $ item = "_opaque_fetish_pants"
                    "Opaque fetish pants (locked)" if Girl.outfit["bottom"] == "_opaque_fetish_pants":
                        pass
                    "Sheer fetish pants" if Girl == RogueX and Girl.outfit["bottom"] != "_sheer_fetish_pants":
                        $ item = "_sheer_fetish_pants"
                    "Sheer fetish pants (locked)" if Girl.outfit["bottom"] == "_sheer_fetish_pants":
                        pass
                    "Classic outfit pants" if Girl == RogueX and Girl.outfit["bottom"] != "_classic_pants":
                        $ item = "_classic_pants"
                    "Classic outfit pants (locked)" if Girl.outfit["bottom"] == "_classic_pants":
                        pass
                    "Red dress" if Girl == RogueX and Girl.outfit["dress"] != "_red_dress":
                        $ item = "_red_dress"
                    "Red dress (locked)" if Girl.outfit["dress"] == "_red_dress":
                        pass
                    "Blue dress" if Girl == RogueX and Girl.outfit["dress"] != "_blue_dress":
                        $ item = "_blue_dress"
                    "Blue dress (locked)" if Girl.outfit["dress"] == "_blue_dress":
                        pass
                    "Classic outfit bra" if Girl == RogueX and Girl.outfit["bra"] != "_classic_bra":
                        $ item = "_classic_bra"
                    "Classic outfit bra (locked)" if Girl.outfit["bra"] == "_classic_bra":
                        pass
                    "Raven suit" if Girl == RogueX and Girl.outfit["bodysuit"] != "_raven_suit":
                        $ item = "_raven_suit"
                    "Raven suit (locked)" if Girl.outfit["bodysuit"] == "_raven_suit":
                        pass
                    "Swimsuit" if Girl == RogueX and Girl.outfit["bodysuit"] != "_swimsuit":
                        $ item = "_swimsuit"
                    "Swimsuit (locked)" if Girl.outfit["bodysuit"] == "_swimsuit":
                        pass
                    "Sexy swimsuit" if Girl == RogueX and Girl.outfit["bodysuit"] != "_sexy_swimsuit":
                        $ item = "_sexy_swimsuit"
                    "Sexy swimsuit (locked)" if Girl.outfit["bodysuit"] == "_sexy_swimsuit":
                        pass
                    "Classic catsuit" if Girl == RogueX and Girl.outfit["bodysuit"] != "_catsuit":
                        $ item = "_catsuit"
                    "Classic catsuit (locked)" if Girl.outfit["bodysuit"] == "_catsuit":
                        pass
                    "Violet shirt" if Girl == KittyX and Girl.outfit["top"] != "_violet_shirt":
                        $ item = "_violet_shirt"
                    "Violet shirt (locked)" if Girl.outfit["top"] == "_violet_shirt":
                        pass
                    "Black and blue pants" if Girl == KittyX and Girl.outfit["bottom"] != "_black_and_blue_pants":
                        $ item = "_black_and_blue_pants"
                    "Black and blue pants (locked)" if Girl.outfit["bottom"] == "_black_and_blue_pants":
                        pass
                    "Chinese dress" if Girl == KittyX and Girl.outfit["dress"] != "_chinese_dress":
                        $ item = "_chinese_dress"
                    "Chinese dress (locked)" if Girl.outfit["dress"] == "_chinese_dress":
                        pass
                    "Domme outfit" if Girl == EmmaX and Girl.outfit["bodysuit"] != "_domme_suit":
                        $ item = "_domme_suit"
                    "Domme outfit (locked)" if Girl.outfit["bodysuit"] == "_domme_suit":
                        pass
                    "Spiked collar" if Girl == EmmaX and Girl.outfit["neck"] != "_spiked_collar":
                        $ item = "_spiked_collar"
                    "Spiked collar (locked)" if Girl.outfit["neck"] == "_spiked_collar":
                        pass
                    "Domme boots" if Girl == EmmaX and Girl.outfit["boots"] != "_domme_boots":
                        $ item = "_domme_boots"
                    "Domme boots (locked)" if Girl.outfit["boots"] == "_domme_boots":
                        pass
                    "Bunny suit" if Girl == LauraX and Girl.outfit["bodysuit"] != "_bunny_suit":
                        $ item = "_bunny_suit"
                    "Bunny suit (locked)" if Girl.outfit["bodysuit"] == "_bunny_suit":
                        pass
                    "Bunny ears" if Girl == LauraX and Girl.outfit["face_outer_accessory"] != "_bunny_ears":
                        $ item = "_bunny_ears"
                    "Bunny ears (locked)" if Girl.outfit["face_outer_accessory"] == "_bunny_ears":
                        pass
                    "Bunny cuffs" if Girl == LauraX and Girl.outfit["gloves"] != "_bunny_gloves":
                        $ item = "_bunny_gloves"
                    "Bunny cuffs (locked)" if Girl.outfit["gloves"] == "_bunny_gloves":
                        pass
                    "Sci-fi suit" if Girl == JeanX and Girl.outfit["bodysuit"] != "_sci_fi_suit":
                        $ item = "_sci_fi_suit"
                    "Sci-fi suit (locked)" if Girl.outfit["bodysuit"] == "_sci_fi_suit":
                        pass
                    "Take off the [Girl.outfit[cloak]]." if Girl.outfit["cloak"]:
                        $ Girl.outfit["cloak"] = ""
                    "Take off the [Girl.outfit[top]]." if Girl.outfit["top"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_top(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.outfit[dress]]." if Girl.outfit["dress"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_dress(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.outfit[bottom]]." if Girl.outfit["bottom"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_bottom(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.outfit[bodysuit]]." if Girl.outfit["bodysuit"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_bodysuit(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.outfit[face_outer_accessory]]." if Girl.outfit["face_outer_accessory"]:
                        $ Girl.outfit["face_outer_accessory"] = ""
                    "Take off the [Girl.outfit[neck]]." if Girl.outfit["neck"]:
                        $ Girl.outfit["neck"] = ""
                    "Take off the [Girl.outfit[gloves]]." if Girl.outfit["gloves"]:
                        $ Girl.outfit["gloves"] = ""
                    "Take off the [Girl.outfit[boots]]." if Girl.outfit["boots"]:
                        $ Girl.outfit["boots"] = ""
                    "Leave dressing area.":
                        $ leave = True

                if item:
                    if item in jackets:
                        if Girl.outfit["top"] or Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            Girl.voice "Sure. . ."

                            call change_jacket(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["jacket"] = item

                            hide black_screen onlayer black
                    elif item in tops:
                        if Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_top(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["top"] = item

                            hide black_screen onlayer black
                    elif item in dresses or item in bodysuits:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            if item in dresses:
                                call change_dress(Girl, item, redress = False)
                            elif item in bodysuits:
                                call change_bodysuit(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            if item in dresses:
                                $ Girl.outfit["dress"] = item
                            elif item in bodysuits:
                                $ Girl.outfit["bodysuit"] = item

                            hide black_screen onlayer black
                    elif item in bras:
                        if Girl.seen_breasts or approval_check(Girl, 1000, taboo_modifier=2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_bra(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["jacket"] = ""
                            $ Girl.outfit["top"] = ""
                            $ Girl.outfit["dress"] = ""
                            $ Girl.outfit["bodysuit"] = ""
                            $ Girl.outfit["bra"] = item

                            hide black_screen onlayer black
                    elif item in pants or item in skirts or item in shorts:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            $ Girl.change_face("_sexy")

                            Girl.voice "Sure. . ."

                            call change_bottom(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.outfit["bottom"] = item

                            hide black_screen onlayer black
                    elif item in cloaks:
                        Girl.voice "Sure. . ."

                        $ Girl.outfit["cloak"] = ""

                        pause 0.2

                        $ Girl.outfit["cloak"] = item
                    elif item in face_outer_accessories:
                        Girl.voice "Sure. . ."

                        $ Girl.outfit["face_outer_accessory"] = ""

                        pause 0.2

                        $ Girl.outfit["face_outer_accessory"] = item
                    elif item in necks:
                        Girl.voice "Sure. . ."

                        $ Girl.outfit["neck"] = ""

                        pause 0.2

                        $ Girl.outfit["neck"] = item
                    elif item in gloves:
                        Girl.voice "Sure. . ."

                        $ Girl.outfit["gloves"] = ""

                        pause 0.2

                        $ Girl.outfit["gloves"] = item
                    elif item in boots:
                        Girl.voice "Sure. . ."

                        $ Girl.outfit["boots"] = ""

                        pause 0.2

                        $ Girl.outfit["boots"] = item

                    if item in cart:
                        pass
                    elif item in Girl.inventory:
                        if item in bras or item in tops:
                            Girl.voice "I do already have one of these though."
                        elif item in underwears or item in hoses or item in socks or item in boots:
                            Girl.voice "I do already have some of these though."
                    else:
                        $ cart.append(item)
                elif leave:
                    if cart and len(Player.Party) > 1:
                        if Player.Party[0].location == Player.location and Player.Party[0] not in [LauraX, JeanX] and Player.Party[0].likes[Girl.tag] >= 500:
                            $ Player.Party[0].change_face("_smile")

                            if Player.Party[0] == RogueX:
                                ch_r "Look'in good there. . ."
                            elif Player.Party[0] == KittyX:
                                ch_k "Oh, that looks cute on you!"
                            elif Player.Party[0] == EmmaX:
                                ch_e "You really do wear that well. . ."
                            elif Player.Party[0] == StormX:
                                ch_s "That really does suit you. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "So cute!"

                            $ Girl.change_face("_smile")

                            if Girl == RogueX:
                                ch_r "Aw, thanks. . ."
                            elif Girl == KittyX:
                                ch_k "Right?"
                            elif Girl == EmmaX:
                                ch_e "Obviously. . ."
                            elif Girl == LauraX:
                                ch_l "Ok, cool. . ."
                            elif Girl == JeanX:
                                ch_j "Of course it does. . ."
                            elif Girl == StormX:
                                ch_s "Oh, thank you. . ."
                            elif Girl == JubesX:
                                ch_v "I know, right?"

                            $ Girl.change_likes(Player.Party[0],5)

                            $ Player.Party[0].change_likes(Girl,3)

                    $ Girl.change_outfit()

                    $ door_locked = False

                    $ Player.location = "bg_shop"

                    call check_who_is_present

                    $ Player.Party = Present[:]
                    $ Player.Party.remove(Girl)
                    $ Player.Party.append(Girl)

                    call set_the_scene
                    call set_Character_taboos

                    if not cart:
                        "That was fun, but since there wasn't anything she was interested in, she put it all back."

                    while cart:
                        $ item = None

                        menu:
                            "So what did you want to buy?"
                            "The Raven cloak." if "_raven_cloak" in cart:
                                $ item = "_raven_cloak"
                            "Rogue's classic jacket." if "_classic_jacket" in cart:
                                $ item = "_classic_jacket"
                            "The opaque fetish top." if "_opaque_fetish_top" in cart:
                                $ item = "_opaque_fetish_top"
                            "The sheer fetish top." if "_sheer_fetish_top" in cart:
                                $ item = "_sheer_fetish_top"
                            "The opaque fetish pants." if "_opaque_fetish_pants" in cart:
                                $ item = "_opaque_fetish_pants"
                            "The sheer fetish pants." if "_sheer_fetish_pants" in cart:
                                $ item = "_sheer_fetish_pants"
                            "Rogue's classic outfit pants." if "_classic_pants" in cart:
                                $ item = "_classic_pants"
                            "The red dress." if "_red_dress" in cart:
                                $ item = "_red_dress"
                            "The blue dress." if "_blue_dress" in cart:
                                $ item = "_blue_dress"
                            "Rogue's classic outfit top." if "_classic_bra" in cart:
                                $ item = "_classic_bra"
                            "The Raven suit." if "_raven_suit" in cart:
                                $ item = "_raven_suit"
                            "The swimsuit." if "_swimsuit" in cart:
                                $ item = "_swimsuit"
                            "The sexy swimsuit." if "_sexy_swimsuit" in cart:
                                $ item = "_sexy_swimsuit"
                            "Rogue's classic outfit." if "_catsuit" in cart:
                                $ item = "_catsuit"
                            "The violet shirt." if "_violet_shirt" in cart:
                                $ item = "_violet_shirt"
                            "The Chinese dress." if "_chinese_dress" in cart:
                                $ item = "_chinese_dress"
                            "The black and blue pants." if "_black_and_blue_pants" in cart:
                                $ item = "_black_and_blue_pants"
                            "The domme outfit." if "_domme_suit" in cart:
                                $ item = "_domme_suit"
                            "The spiked collar." if "_spiked_collar" in cart:
                                $ item = "_spiked_collar"
                            "The domme boots." if "_domme_boots" in cart:
                                $ item = "_domme_boots"
                            "The bunny suit." if "_bunny_suit" in cart:
                                $ item = "_bunny_suit"
                            "The bunny ears." if "_bunny_ears" in cart:
                                $ item = "_bunny_ears"
                            "The bunny cuffs." if "_bunny_cuffs" in cart:
                                $ item = "_bunny_cuffs"
                            "The sci-fi suit." if "_sci_fi_suit" in cart:
                                $ item = "_sci_fi_suit"
                            "Nothing." if "purchased" not in Player.recent_history:
                                $ Girl.change_face("_sad")

                                if "shopblock" not in Girl.daily_history:
                                    $ Girl.add_word(1,"shopblock","shopblock")
                                    $ Girl.change_stat("love", 50, -2)
                                    $ Girl.change_stat("love", 90, -2)
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("obedience", 80, 3)

                                "You put all the stuff back."

                                if Girl in [EmmaX, StormX]:
                                    Girl.voice "How disappointing."
                                elif Girl in [LauraX, JeanX]:
                                    pass
                                else:
                                    Girl.voice "Aw. . ."

                                $ cart = []
                            "Done." if "purchased" in Player.recent_history:
                                "You put all the remaining stuff back."

                                $ cart = []

                        if item:
                            if Girl.tag + item in Player.inventory:
                                if item in dresses or item in bodysuits or item in tops or item in skirts or item in cloaks:
                                    "Wait, you already have one of those."
                                    "You pull out the one in your bag and give it to [Girl.name]."
                                elif item in pants or item in shorts or item in gloves or item in face_outer_accessories:
                                    "Wait, you already have a pair of these."
                                    "You pull out the pair in your bag and give them to [Girl.name]."
                            else:
                                if item in ["_raven_suit", "_catsuit", "_domme_suit"]:
                                    $ cost = 200
                                elif item in ["_raven_cloak", "_opaque_fetish_top", "_sheer_fetish_top", "_opaque_fetish_pants", "_sheer_fetish_pants", "_red_dress", "_blue_dress", "_classic_bra"]:
                                    $ cost = 100
                                elif item in ["_classic_jacket", "_classic_pants", "_swimsuit", "_sexy_swimsuit", "_violet_shirt", "_black_and_blue_pants", "_domme_boots"]:
                                    $ cost = 75
                                elif item in ["_chinese_dress", "_sci_fi_suit"]:
                                    $ cost = 300
                                elif item == "_bunny_suit":
                                    $ cost = 150
                                elif item == ["_spiked_collar", "_bunny_cuffs"]:
                                    $ cost = 25
                                elif item == "_bunny_ears":
                                    $ cost = 15

                                if Player.cash < cost:
                                    "You look at the tag - it's $[cost]. You can't afford it."

                                    $ cart.remove(item)
                                else:
                                    $ Player.cash -= cost

                            if item in cart:
                                $ cart.remove(item)

                                $ Player.add_word(1,"purchased")

                                $ Girl.inventory.append(item)
                                $ Girl.change_face("_bemused", 1)

                                if item == "_raven_suit":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)
                                elif item == "_raven_cloak":
                                    $ Girl.change_stat("love", 200, 15)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 10)
                                elif item in ["_opaque_fetish_top", "_opaque_fetish_pants"]:
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 30)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    ch_r "Always did like mesh."

                                    $ Girl.change_face("_smile")

                                    ch_r "Thanks, [Girl.player_petname]."
                                elif item in ["_sheer_fetish_top", "_sheer_fetish_pants"]:
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 30)
                                    $ Girl.change_stat("inhibition", 200, 20)

                                    ch_r "Always did like mesh."

                                    $ Girl.change_face("_smile")

                                    ch_r "Thanks, [Girl.player_petname]."
                                elif item == "_chinese_dress":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)
                                elif item == "_bunny_suit":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)
                                elif item == "_bunny_cuffs":
                                    $ Girl.change_stat("love", 200, 25)
                                    $ Girl.change_stat("obedience", 200, 20)
                                    $ Girl.change_stat("inhibition", 200, 20)
                                elif item == "_bunny_ears":
                                    $ Girl.change_stat("love", 200, 5)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 200, 5)

                    $ Player.drain_word("purchased")

                    $ Girl = None

    return
