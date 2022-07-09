label sex_shop:
    call set_the_scene(location = "bg_shop")

    "You head into \"Spiral's Body Shoppe\". . ."

    while True:
        $ Girl = None

        if round <= 20:
            "It's getting late, you head back into the mall. . ."

            return

        menu:
            "What did you want to purchase?"
            "Buy dildo for $20.":
                if Player.inventory.count("dildo") >= 10:
                    "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
                elif Player.cash >= 20:
                    "You purchase a dildo."

                    $ Player.inventory.append("dildo")
                    $ Player.cash -= 20

                    if Player.Party:
                        if approval_check(Player.Party[0], 800):
                            $ Player.Party[0].change_face("sly")
                            call change_Girl_stat(Player.Party[0], "love", 1)
                            call change_Girl_stat(Player.Party[0], "obedience", 3)
                            call change_Girl_stat(Player.Party[0], "inhibition", 3)

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
                            $ Player.Party[0].change_face("confused", 2)
                            call change_Girl_stat(Player.Party[0], "love", -2)
                            call change_Girl_stat(Player.Party[0], "obedience", 4)
                            call change_Girl_stat(Player.Party[0], "inhibition", 2)

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

                            $ Player.Party[0].change_face("confused", 1)

                        call change_Girl_stat(Player.Party[0], "lust", 5)
                else:
                    "You don't have enough for that."
            "Buy \"Shocker\" vibrator for $25.":
                if Player.inventory.count("vibrator") >= 10:
                    "If you bought one more vibrator, you would risk a geological event."
                elif Player.cash >= 25:
                    "You purchase a vibrator."

                    $ Player.inventory.append("vibrator")
                    $ Player.cash -= 25

                    if Player.Party:
                        if approval_check(Player.Party[0], 800):
                            $ Player.Party[0].change_face("sly")
                            call change_Girl_stat(Player.Party[0], "love", 2)
                            call change_Girl_stat(Player.Party[0], "obedience", 2)
                            call change_Girl_stat(Player.Party[0], "inhibition", 3)

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

                            call change_Girl_stat(Player.Party[0], "lust", 5)
                        else:
                            $ Player.Party[0].change_face("confused", 2)
                            call change_Girl_stat(Player.Party[0], "obedience", 2)
                            call change_Girl_stat(Player.Party[0], "inhibition", 2)

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

                            $ Player.Party[0].change_face("confused", 1)
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

                call set_the_scene(location = "bg_mall")

                return

        if Girl:
            menu:
                "Gift her a dildo" if "dildo" in Player.inventory:
                    if "dildo" not in Girl.inventory:
                        "You give [Girl.name] the dildo."

                        $ Girl.blushing = "_blush1"
                        $ Girl.arm_pose = 2
                        $ Girl.held_item = "dildo"

                        if approval_check(Girl, 800):
                            $ Player.inventory.remove("dildo")

                            $ Girl.inventory.append("dildo")
                            $ Girl.change_face("bemused")
                            call change_Girl_stat(Girl, "love", 30)
                            call change_Girl_stat(Girl, "obedience", 30)
                            call change_Girl_stat(Girl, "inhibition", 30)

                            if Girl == RogueX:
                                ch_r "Well, I've got some ideas in mind for this. . ."
                            elif Girl == LauraX:
                                ch_l "Oh, cool, I've wanted one of these. . ."
                            else:
                                Girl.voice "I'm sure I can find some place to store it. . ."

                            call change_Girl_stat(Girl, "lust", 10)
                        elif approval_check(Girl, 600):
                            $ Player.inventory.remove("dildo")

                            $ Girl.inventory.append("dildo")
                            $ Girl.change_face("confused")

                            if Girl != EmmaX:
                                call change_Girl_stat(Girl, "love", 10)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 10)

                            if Girl == RogueX:
                                ch_r "Huh, well I guess I can find a place for it. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("surprised")

                                ch_r "I- I mean. . . I'll just put it away."
                            elif Girl == KittyX:
                                ch_k "I don't know what. . ."

                                call change_Girl_stat(Girl, "lust", 5)
                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("surprised")

                                ch_k "Oh!"
                                ch_k "Oh. . . I'll just[Girl.like]put it away."
                            elif Girl == EmmaX:
                                ch_e "This is not an appropriate gift from a student. . ."

                                call change_Girl_stat(Girl, "lust", 5)
                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("sadside", 1)

                                ch_e "Hm. . ."

                                call change_Girl_stat(Girl, "love", 10)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 10)
                                $ Girl.change_face("sly")

                                ch_e "I suppose I can find {i}some{/i} use for it. . ."
                            elif Girl == LauraX:
                                ch_l "Huh, you're a weird gift giver."

                                call change_Girl_stat(Girl, "lust", 5)
                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("smile")

                                ch_l "It's very thoughtful though."
                            elif Girl == JeanX:
                                call change_Girl_stat(Girl, "lust", 5)
                                call change_Girl_stat(Girl, "lust", 10)

                                ch_j "Well we know where your mind it at."

                                $ Girl.change_face("smile")

                                ch_j "I guess I should be flattered. . ."
                            elif Girl == StormX:
                                if StormX not in Rules:
                                    $ Girl.change_face("sadside", 1)

                                    ch_s "I don't know that I should accept this from a student. . ."

                                call change_Girl_stat(Girl, "lust", 5)
                                call change_Girl_stat(Girl, "lust", 10)

                                ch_s "Hm. . ."

                                $ Girl.change_face("sly")

                                ch_s "Thank you for the thought. . ."
                            elif Girl == JubesX:
                                ch_v "I guess I have some use for it. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("surprised")

                                ch_v "I- I mean. . . decorative."

                            $ Girl.change_face("bemused")
                        elif "offered gift" in Girl.daily_history:
                            $ Girl.change_face("angry")

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
                            $ Girl.change_face("angry")
                            call change_Girl_stat(Girl, "love", -20)
                            call change_Girl_stat(Girl, "obedience", 10)
                            call change_Girl_stat(Girl, "inhibition", 20)

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

                            call change_Girl_stat(Girl, "lust", 5)

                            "She hands it back to you."

                            $ Girl.daily_history.append("offered gift")
                    elif Girl.inventory.count("dildo") == 1:
                        $ Player.inventory.remove("dildo")

                        $ Girl.inventory.append("dildo")

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

                    $ Girl.held_item = None

                    $ Girl = None
                "Gift her a vibrator" if "vibrator" in Player.inventory:
                    if "vibrator" not in Girl.inventory:
                        "You give [Girl.name] the Shocker Vibrator."

                        $ Girl.blushing = "_blush1"
                        $ Girl.arm_pose = 2
                        $ Girl.held_item = "vibrator"

                        if approval_check(Girl, 700):
                            $ Player.inventory.remove("vibrator")

                            $ Girl.inventory.append("vibrator")
                            $ Girl.change_face("bemused")
                            call change_Girl_stat(Girl, "love", 30)
                            call change_Girl_stat(Girl, "obedience", 30)
                            call change_Girl_stat(Girl, "inhibition", 30)

                            if Girl == RogueX:
                                ch_r "Well, I've got some ideas in mind for this. . ."
                            elif Girl == KittyX:
                                ch_k "Well this is. . . [[bzzzt]- "
                                ch_k "-interesting. . ."
                            elif Girl == EmmaX:
                                ch_e "How very thoughtful of you. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("sly")

                                ch_e "I'm sure I can put this to good use. . ."
                            elif Girl == LauraX:
                                ch_l "This is. . . [[bzzzt]- "

                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("sly")

                                ch_l "-some kind of sex thing, huh. . ."
                            elif Girl == JeanX:
                                ch_j "Oh, nifty."
                            elif Girl == StormX:
                                ch_s "Oh!. . . oooohhh."
                            elif Girl == JubesX:
                                ch_v "Oh, this could be nice. . ."

                            call change_Girl_stat(Girl, "lust", 10)
                        elif approval_check(Girl, 400):
                            $ Player.inventory.remove("vibrator")

                            $ Girl.inventory.append("vibrator")
                            $ Girl.change_face("confused")
                            call change_Girl_stat(Girl, "love", 10)
                            call change_Girl_stat(Girl, "obedience", 10)
                            call change_Girl_stat(Girl, "inhibition", 10)

                            if Girl == RogueX:
                                ch_r "I guess I can use this to work the kinks out. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("surprised")

                                ch_r "Muscle knots, I mean!"
                            elif Girl == KittyX:
                                ch_k "I've heard these are very relaxing. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("surprised")

                                ch_k "-for my back!"
                            elif Girl == EmmaX:
                                ch_e "How very thoughtful of you. . ."

                                call change_Girl_stat(Girl, "lust", 10)
                                $ Girl.change_face("sly")

                                ch_e "A back massager, I assume. . ."
                            elif Girl == LauraX:
                                ch_l "This is. . . [[bzzzt]- "

                                $ Girl.change_face("sly")
                                call change_Girl_stat(Girl, "lust", 10)

                                ch_l "-oooh. . ."
                            elif Girl == JeanX:
                                ch_j "Huh. Ok."
                            elif Girl == StormX:
                                ch_s "Oh, something for exercise purposes. . ."
                            elif Girl == JubesX:
                                ch_v "Thanks, my, uh, back's been killing me. . ."

                            $ Girl.change_face("bemused", 1)
                        elif "offered gift" in Girl.daily_history:
                            $ Girl.change_face("angry")

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
                            $ Girl.change_face("angry")
                            call change_Girl_stat(Girl, "love", -20)
                            call change_Girl_stat(Girl, "obedience", 10)
                            call change_Girl_stat(Girl, "inhibition", 20)

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

                            call change_Girl_stat(Girl, "lust", 5)

                            "She hands it back to you."

                            $ Girl.daily_history.append("offered gift")
                    else:
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname], I only need the one."
                        elif Girl == EmmaX:
                            ch_e "I already have plenty."
                        else:
                            Girl.voice "I already have one of these."

                    $ Girl.held_item = None

                    $ Girl = None
                "Never mind":
                    $ Girl = None

    return

label swimsuit_shop:
    call set_the_scene(location = "bg_shop")

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

                call set_the_scene(location = "bg_mall")

                return

        if Girl:
            $ shift_focus(Girl)

            $ Girl.change_face("smile", 1)

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
                    "Stay out here.":
                        Player.Party[0].voice "Fine, we'll wait out here."

                        $ Player.Party = [Girl]
            elif len(Player.Party) == 2:
                menu:
                    Player.Party[0].voice "Should I come in too?"
                    "Sure.":
                        "[Player.Party[0].name] follows you in."
                    "Stay out here.":
                        Player.Party[0].voice "Fine, I'll just wait here then."

                        $ Player.Party = [Girl]

            $ door_locked = True

            call set_the_scene(location = "bg_dressing")
            call set_Character_taboos

            $ cart = []
            $ leave = False

            while Girl:
                $ item = None

                menu:
                    "What did you want to try on here?"
                    "Bikini top" if Girl.Clothes["bra"] != "bikini_top":
                        $ item = "bikini_top"
                    "Bikini top (locked)" if Girl.Clothes["bra"] == "bikini_top":
                        pass
                    "Bikini bottoms" if Girl.Clothes["underwear"] != "bikini_bottoms":
                        $ item = "bikini_bottoms"
                    "Bikini bottoms (locked)" if Girl.Clothes["underwear"] == "bikini_bottoms":
                        pass
                    "Blue swimskirt" if Girl == KittyX and Girl.Clothes["bottom"] != "blue_skirt":
                        $ item = "blue_skirt"
                    "Blue swimskirt (locked)" if Girl == KittyX and Girl.Clothes["bottom"] == "blue_skirt":
                        pass
                    "Leave dressing area.":
                        $ leave = True

                if item:
                    if item in bras:
                        if Girl.seen_breasts or approval_check(Girl, 1100, taboo_modifier = 2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_bra(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.take_off("jacket")
                            $ Girl.take_off("top")
                            $ Girl.take_off("dress")
                            $ Girl.take_off("bodysuit")
                            $ Girl.Clothes["bra"] = item

                            hide black_screen onlayer black
                    elif item in underwears:
                        if Girl.seen_pussy or approval_check(Girl, 1200, taboo_modifier = 2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_underwear(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.take_off("bodysuit")
                            $ Girl.take_off("dress")
                            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
                            $ Girl.take_off("hose")
                            $ Girl.Clothes["underwear"] = item

                            hide black_screen onlayer black
                    elif item in skirts:
                        $ Girl.change_face("smile")

                        if Girl.seen_pussy or (Girl.Clothes["underwear"] and Girl.seen_underwear) or (Girl.Clothes["underwear"] and approval_check(Girl, 900, taboo_modifier = 2)) or approval_check(Girl, 1200, taboo_modifier = 2):

                            Girl.voice "Sure. . ."

                            call change_bottom(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["bottom"] = item

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

                        if Girl == StormX and item in ["bikini_top", "bikini_bottoms"] and (Girl.Clothes["bra"] == "bikini_top" or Girl.Clothes["underwear"] == "bikini_bottoms"):
                            ch_s "Oh! I understand the purpose of the flap now!"
                elif leave:
                    if cart and len(Player.Party) > 1:
                        if Player.Party[0].location == Player.location and Player.Party[0] not in [LauraX, JeanX] and Player.Party[0].likes[Girl.tag] >= 500:
                            $ Player.Party[0].change_face("smile")

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

                            $ Girl.change_face("smile")

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

                            $ Girl.likes[Player.Party[0].tag] += 5

                            $ Player.Party[0].likes[Girl.tag] += 3

                    $ Girl.change_Outfit()

                    $ door_locked = False

                    call set_the_scene(location = "bg_shop")

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
                            "The top." if "bikini_top" in cart:
                                $ item = "bikini_top"
                            "The bottoms." if "bikini_bottoms" in cart:
                                $ item = "bikini_bottoms"
                            "The skirt." if "blue_skirt" in cart:
                                $ item = "blue_skirt"
                            "Nothing." if "purchased" not in Player.recent_history:
                                $ Girl.change_face("sad")

                                if "shopblock" not in Girl.daily_history:
                                    $ Girl.add_word(1, "shopblock", "shopblock")
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "obedience", 3)
                                    call change_Girl_stat(Girl, "obedience", 3)

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
                                if item == "bikini_top":
                                    if Girl in [KittyX, EmmaX, StormX]:
                                        $ cost = 50
                                    else:
                                        $ cost = 60
                                elif item == "bikini_bottoms":
                                    if Girl in [KittyX, EmmaX, StormX]:
                                        $ cost = 60
                                    else:
                                        $ cost = 50
                                elif item == "blue_skirt":
                                    $ cost = 50

                                if Player.cash < cost:
                                    "You look at the tag - it's $[cost]. You can't afford it."

                                    $ cart.remove(item)
                                else:
                                    $ Player.cash -= cost

                            if item in cart:
                                $ cart.remove(item)

                                $ Player.add_word(1, "purchased")

                                $ Girl.inventory.append(item)
                                $ Girl.change_face("bemused", 1)
                                call change_Girl_stat(Girl, "love", 20)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "inhibition", 5)

                                if item == "bikini_top":
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
                                elif item == "bikini_bottoms":
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
                                elif item == "blue_skirt":
                                    ch_k "This is a cute skirt. . ."

                    $ Player.drain_word("purchased")

                    if Girl == KittyX and ("blue_skirt" in Girl.inventory or Girl.inhibition >= 400) and "bikini_top" in Girl.inventory and "bikini_bottoms" in Girl.inventory:
                        $ Girl.swimwear["outfit_active"] = 1
                    elif "bikini_top" in Girl.inventory and "bikini_bottoms" in Girl.inventory:
                        $ Girl.swimwear["outfit_active"] = 1

                    $ Girl = None

    return

label lingerie_shop:
    call set_the_scene(location = "bg_shop")

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

                call set_the_scene(location = "bg_mall")

                return

        if Girl:
            $ shift_focus(Girl)

            $ Girl.change_face("smile", 1)

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
                    "Stay out here.":
                        Player.Party[0].voice "Fine, we'll wait out here."

                        $ Player.Party = [Girl]
            elif len(Player.Party) == 2:
                menu:
                    Player.Party[0].voice "Should I come in too?"
                    "Sure.":
                        "[Player.Party[0].name] follows you in."
                    "Stay out here.":
                        Player.Party[0].voice "Fine, I'll just wait here then."

                        $ Player.Party = [Girl]

            $ door_locked = True

            call set_the_scene(location = "bg_dressing")
            call set_Character_taboos

            $ cart = []
            $ leave = False

            while Girl:
                $ item = None

                menu:
                    "What did you want to try on here?"
                    "Lace bra" if Girl != LauraX and Girl.Clothes["bra"] != "lace_bra":
                        $ item = "lace_bra"
                    "Lace bra (locked)" if Girl.Clothes["bra"] == "lace_bra":
                        pass
                    "Corset" if Girl in [LauraX, JeanX] and Girl.Clothes["bra"] != "corset":
                        $ item = "corset"
                    "Corset (locked)" if Girl in [LauraX, JeanX] and Girl.Clothes["bra"] == "corset":
                        pass
                    "Lace corset" if Girl == LauraX and Girl.Clothes["bra"] != "lace_corset":
                        $ item = "lace_corset"
                    "Lace corset (locked)" if Girl.Clothes["bra"] == "lace_corset":
                        pass
                    "Lace panties" if Girl.Clothes["underwear"] != "lace_panties":
                        $ item = "lace_panties"
                    "Lace panties (locked)" if Girl.Clothes["underwear"] == "lace_panties":
                        pass
                    "Tiger-striped panties" if Girl == JubesX and Girl.Clothes["underwear"] != "tiger_panties":
                        $ item = "tiger_panties"
                    "Tiger-striped panties (locked)" if Girl.Clothes["underwear"] == "tiger_panties":
                        pass
                    "Pantyhose" if Girl.Clothes["hose"] != "pantyhose":
                        $ item = "pantyhose"
                    "Pantyhose (locked)" if Girl.Clothes["hose"] == "pantyhose":
                        pass
                    "Stockings and garterbelt" if Girl.Clothes["hose"] != "stockings_and_garterbelt":
                        $ item = "stockings_and_garterbelt"
                    "Stockings and garterbelt (locked)" if Girl.Clothes["hose"] == "stockings_and_garterbelt":
                        pass
                    "Knee stockings" if Girl == KittyX and Girl.Clothes["hose"] != "knee_stockings":
                        $ item = "knee_stockings"
                    "Knee stockings (locked)" if Girl.Clothes["hose"] == "knee_stockings":
                        pass
                    "High socks" if Girl == JubesX and Girl.Clothes["hose"] != "socks":
                        $ item = "socks"
                    "High socks (locked)" if Girl.Clothes["hose"] == "socks":
                        pass
                    "Nighty" if Girl in [RogueX, KittyX] and Girl.Clothes["top"] != "nighty":
                        $ item = "nighty"
                    "Nighty (locked)" if Girl.Clothes["top"] == "nighty":
                        pass
                    "Harness bra" if Girl == RogueX and Girl.Clothes["bra"] != "harness_bra":
                        $ item = "harness_bra"
                    "Harness bra (locked)" if Girl.Clothes["bra"] == "harness_bra":
                        pass
                    "Kitty bra" if Girl == KittyX and Girl.Clothes["bra"] != "kitty_bra":
                        $ item = "kitty_bra"
                    "Kitty bra (locked)" if Girl.Clothes["bra"] == "kitty_bra":
                        pass
                    "Orange top" if Girl == KittyX and Girl.Clothes["bra"] != "orange_top":
                        $ item = "orange_top"
                    "Orange top (locked)" if Girl.Clothes["bra"] == "orange_top":
                        pass
                    "Harness panties" if Girl == RogueX and Girl.Clothes["underwear"] != "harness_panties":
                        $ item = "harness_panties"
                    "Harness panties (locked)" if Girl.Clothes["underwear"] == "harness_panties":
                        pass
                    "Kitty panties" if Girl == KittyX and Girl.Clothes["underwear"] != "kitty_panties":
                        $ item = "kitty_panties"
                    "Kitty panties (locked)" if Girl.Clothes["underwear"] == "kitty_panties":
                        pass
                    "Nighty panties" if Girl == KittyX and Girl.Clothes["underwear"] != "nighty_panties":
                        $ item = "nighty_panties"
                    "Nighty panties (locked)" if Girl.Clothes["underwear"] == "nighty_panties":
                        pass
                    "Take off the [Girl.Clothes[hose].name]." if Girl.Clothes["hose"]:
                        if Girl.Clothes["hose"] != "pantyhose" or approval_check(Girl, 900, taboo_modifier = 2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            if Girl.Clothes["hose"] in hoses:
                                call change_hose(Girl, "")
                            elif Girl.Clothes["hose"] in socks:
                                call change_socks(Girl, "")
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Leave dressing area.":
                        $ leave = True

                if item:
                    if item in bras or item == "nighty":
                        if "no_gift_bra" in Girl.recent_history:
                            Girl.voice "I said no. . ."

                            $ item = None
                        elif not Girl.seen_breasts and not approval_check(Girl, 900):
                            $ Girl.change_face("angry", 2)

                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in [JeanX, LauraX]:
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, definitely not. . ."

                            $ Girl.recent_history.append("no_gift_bra")
                            $ Girl.change_face("angry", 1)

                            $ item = None
                    elif item in underwears or item in hoses:
                        if "no_gift_panties" in Girl.recent_history:
                            Girl.voice "I said no. . ."

                            $ item = None
                        elif "no_gift_bra" in Girl.recent_history:
                            Girl.voice "Why would this be okay instead?"

                            $ item = None
                        elif not Girl.seen_pussy and not approval_check(Girl, 1000):
                            $ Girl.change_face("angry", 2)

                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I don't think that would be appropriate."
                            elif Girl in [JeanX, LauraX]:
                                Girl.voice "No thanks. . ."
                            else:
                                Girl.voice "Um, no, not really interested. . ."

                            $ Girl.recent_history.append("no_gift_panties")
                            $ Girl.change_face("angry", 1)

                if item:
                    if item in bras:
                        if Girl.seen_breasts or approval_check(Girl, 1000, taboo_modifier=2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_bra(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.take_off("jacket")
                            $ Girl.take_off("top")
                            $ Girl.take_off("dress")
                            $ Girl.take_off("bodysuit")
                            $ Girl.Clothes["bra"] = item

                            hide black_screen onlayer black
                    elif item in underwears:
                        if Girl.seen_pussy or approval_check(Girl, 1200, taboo_modifier=2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_underwear(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.take_off("dress")
                            $ Girl.take_off("bodysuit")
                            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
                            $ Girl.Clothes["underwear"] = item

                            hide black_screen onlayer black
                    elif item in hoses:
                        if Girl.seen_pussy or approval_check(Girl, 900, taboo_modifier = 2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_hose(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.take_off("dress")
                            $ Girl.take_off("bodysuit")
                            $ Girl.Outfit.remove_Clothing(["pants", "skirt"])
                            $ Girl.Clothes["hose"] = item

                            hide black_screen onlayer black
                    elif item in socks:
                        $ Girl.change_face("sexy")

                        Girl.voice "Sure. . ."

                        call change_socks(Girl, item, redress = False)

                        $ Girl.Clothes["hose"] = item
                    elif item in tops:
                        if Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_top(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["top"] = item

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
                            $ Player.Party[0].change_face("smile")

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

                            $ Girl.change_face("smile")

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

                            $ Girl.likes[Player.Party[0].tag] += 5

                            $ Player.Party[0].likes[Girl.tag] += 3

                    $ Girl.change_Outfit()

                    $ door_locked = False

                    call set_the_scene(location = "bg_shop")

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
                            "The lace bra." if "lace_bra" in cart:
                                $ item = "lace_bra"
                            "The corset." if "corset" in cart:
                                $ item = "corset"
                            "The lace corset." if "lace_corset" in cart:
                                $ item = "lace_corset"
                            "The lace panties." if "lace_panties" in cart:
                                $ item = "lace_panties"
                            "The tiger-striped panties." if "tiger_panties" in cart:
                                $ item = "tiger_panties"
                            "The pantyhose." if "pantyhose" in cart:
                                $ item = "pantyhose"
                            "The stockings and garterbelt." if "stockings_and_garterbelt" in cart:
                                $ item = "stockings_and_garterbelt"
                            "The knee stockings." if "knee_stockings" in cart:
                                $ item = "knee_stockings"
                            "The high socks." if "socks" in cart:
                                $ item = "socks"
                            "The nighty." if "nighty" in cart:
                                $ item = "nighty"
                            "The harness bra." if "harness_bra" in cart:
                                $ item = "harness_bra"
                            "The kitty bra." if "kitty_bra" in cart:
                                $ item = "kitty_bra"
                            "The orange top." if "orange_top" in cart:
                                $ item = "orange_top"
                            "The harness panties." if "harness_panties" in cart:
                                $ item = "harness_panties"
                            "The kitty panties." if "kitty_panties" in cart:
                                $ item = "kitty_panties"
                            "The nighty panties." if "nighty_panties" in cart:
                                $ item = "nighty_panties"
                            "Nothing." if "purchased" not in Player.recent_history:
                                $ Girl.change_face("sad")

                                if "shopblock" not in Girl.daily_history:
                                    $ Girl.add_word(1, "shopblock", "shopblock")
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "obedience", 3)
                                    call change_Girl_stat(Girl, "obedience", 3)

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
                                if item in ["lace_bra", "lace_corset"]:
                                    $ cost = 90
                                elif item == ["corset", "kitty_panties"]:
                                    $ cost = 70
                                elif item in ["lace_panties"]:
                                    $ cost = 110
                                elif item in ["tiger_panties", "stockings_and_garterbelt"]:
                                    $ cost = 100
                                elif item in ["pantyhose", "knee_stockings", "socks", "orange_top", "nighty_panties"]:
                                    $ cost = 50
                                elif item == ["nighty", "kitty_bra"]:
                                    $ cost = 75

                                if Player.cash < cost:
                                    "You look at the tag - it's $[cost]. You can't afford it."

                                    $ cart.remove(item)
                                else:
                                    $ Player.cash -= cost

                            if item in cart:
                                $ cart.remove(item)

                                $ Player.add_word(1, "purchased")

                                $ Girl.inventory.append(item)
                                $ Girl.change_face("bemused", 1)

                                if item == "lace_bra":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)

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
                                elif item == "corset":
                                    call change_Girl_stat(Girl, "love", 15)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 10)

                                    if Girl == LauraX:
                                        ch_l "This is. . . kinda cool. . ."
                                    elif Girl == JeanX:
                                        ch_j "Thanks?"
                                elif item == "lace_corset":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 30)
                                    call change_Girl_stat(Girl, "inhibition", 20)

                                    ch_l "You think this'd look good on me?"
                                elif item == "harness_bra":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 30)
                                    call change_Girl_stat(Girl, "inhibition", 20)

                                    ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                    $ Girl.mouth = "lipbite"

                                    ch_r "But never did mind a wardrobe change."
                                elif item == "lace_panties":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)

                                    if Girl == RogueX:
                                        ch_r "These are a bit flimsy. . ."
                                    elif Girl == KittyX:
                                        ch_k "These don't leave much to the imagination. . ."
                                    elif Girl == EmmaX:
                                        ch_e "This is an. . . unsual gift."

                                        $ EmmaX.change_face("sly", 1)

                                        ch_e "But I'll hold on to them. . ."
                                    elif Girl == LauraX:
                                        ch_l "These are pretty hot. . ."
                                    elif Girl == JeanX:
                                        ch_j "Oh, these are nice. . ."
                                    elif Girl == StormX:
                                        ch_s "I suppose I could always use another pair. . ."
                                    elif Girl == JubesX:
                                        ch_v "A little. . . intimate. . ."
                                elif item == "tiger_panties":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)

                                    ch_v "These are stink'in cute. . ."
                                elif item == "harness_panties":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)

                                    ch_r "Not exactly my usual gear, [Girl.player_petname]. . ."

                                    $ Girl.mouth = "lipbite"

                                    ch_r "But never did mind a wardrobe change."
                                elif item == "pantyhose":
                                    call change_Girl_stat(Girl, "love", 5)
                                    call change_Girl_stat(Girl, "obedience", 5)
                                    call change_Girl_stat(Girl, "inhibition", 5)

                                    Girl.voice "These are lovely. . ."
                                elif item == "stockings_and_garterbelt":
                                    call change_Girl_stat(Girl, "love", 5)
                                    call change_Girl_stat(Girl, "obedience", 5)
                                    call change_Girl_stat(Girl, "inhibition", 5)

                                    if Girl == EmmaX:
                                        ch_e "These are lovely. . ."
                                    elif Girl == StormX:
                                        ch_s "You think I could pull these off?"
                                    else:
                                        Girl.voice "These are pretty nice. . ."
                                elif item == "knee_stockings":
                                    call change_Girl_stat(Girl, "love", 5)
                                    call change_Girl_stat(Girl, "obedience", 5)
                                    call change_Girl_stat(Girl, "inhibition", 5)

                                    Girl.voice "These are pretty nice. . ."
                                elif item == "socks":
                                    call change_Girl_stat(Girl, "love", 5)
                                    call change_Girl_stat(Girl, "obedience", 5)
                                    call change_Girl_stat(Girl, "inhibition", 5)

                                    Girl.voice "These are pretty nice. . ."
                                elif item == "nighty":
                                    call change_Girl_stat(Girl, "love", 40)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 30)

                                    if Girl == RogueX:
                                        ch_r "Well, it's a little revealing, but still pretty cute."

                                    call change_Girl_stat(Girl, "lust", 10)

                    $ Player.drain_word("purchased")

                    $ Girl = None

    return

label clothing_shop:
    call set_the_scene(location = "bg_shop")

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

                call set_the_scene(location = "bg_mall")

                return

        if Girl:
            $ shift_focus(Girl)

            $ Girl.change_face("smile", 1)

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
                    "Stay out here.":
                        Player.Party[0].voice "Fine, we'll wait out here."

                        $ Player.Party = [Girl]
            elif len(Player.Party) == 2:
                menu:
                    Player.Party[0].voice "Should I come in too?"
                    "Sure.":
                        "[Player.Party[0].name] follows you in."
                    "Stay out here.":
                        Player.Party[0].voice "Fine, I'll just wait here then."

                        $ Player.Party = [Girl]

            $ door_locked = True

            call set_the_scene(location = "bg_dressing")
            call set_Character_taboos

            $ cart = []
            $ leave = False

            while Girl:
                $ item = None

                menu:
                    "What did you want to try on here?"
                    "Raven cloak" if Girl == RogueX and Girl.Clothes["cloak"] != "Raven_cloak":
                        $ item = "Raven_cloak"
                    "Raven cloak (locked)" if Girl.Clothes["cloak"] == "Raven_cloak":
                        pass
                    "Classic jacket" if Girl == RogueX and Girl.Clothes["jacket"] != "classic_jacket":
                        $ item = "classic_jacket"
                    "Classic jacket (locked)" if Girl.Clothes["jacket"] == "classic_jacket":
                        pass
                    "Opaque fetish top" if Girl == RogueX and Girl.Clothes["top"] != "opaque_fetish_top":
                        $ item = "opaque_fetish_top"
                    "Opaque fetish top (locked)" if Girl.Clothes["top"] == "opaque_fetish_top":
                        pass
                    "Sheer fetish top" if Girl == RogueX and Girl.Clothes["top"] != "sheer_fetish_top":
                        $ item = "sheer_fetish_top"
                    "Sheer fetish top (locked)" if Girl.Clothes["top"] == "sheer_fetish_top":
                        pass
                    "Opaque fetish pants" if Girl == RogueX and Girl.Clothes["bottom"] != "opaque_fetish_pants":
                        $ item = "opaque_fetish_pants"
                    "Opaque fetish pants (locked)" if Girl.Clothes["bottom"] == "opaque_fetish_pants":
                        pass
                    "Sheer fetish pants" if Girl == RogueX and Girl.Clothes["bottom"] != "sheer_fetish_pants":
                        $ item = "sheer_fetish_pants"
                    "Sheer fetish pants (locked)" if Girl.Clothes["bottom"] == "sheer_fetish_pants":
                        pass
                    "Red dress" if Girl == RogueX and Girl.Clothes["dress"] != "red_dress":
                        $ item = "red_dress"
                    "Red dress (locked)" if Girl.Clothes["dress"] == "red_dress":
                        pass
                    "Blue dress" if Girl == RogueX and Girl.Clothes["dress"] != "blue_dress":
                        $ item = "blue_dress"
                    "Blue dress (locked)" if Girl.Clothes["dress"] == "blue_dress":
                        pass
                    "Raven suit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "Raven_suit":
                        $ item = "Raven_suit"
                    "Raven suit (locked)" if Girl.Clothes["bodysuit"] == "Raven_suit":
                        pass
                    "Swimsuit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "swimsuit":
                        $ item = "swimsuit"
                    "Swimsuit (locked)" if Girl.Clothes["bodysuit"] == "swimsuit":
                        pass
                    "Sexy swimsuit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "sexy_swimsuit":
                        $ item = "sexy_swimsuit"
                    "Sexy swimsuit (locked)" if Girl.Clothes["bodysuit"] == "sexy_swimsuit":
                        pass
                    "Classic catsuit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "catsuit":
                        $ item = "catsuit"
                    "Classic catsuit (locked)" if Girl.Clothes["bodysuit"] == "catsuit":
                        pass
                    "Violet shirt" if Girl == KittyX and Girl.Clothes["top"] != "violet_shirt":
                        $ item = "violet_shirt"
                    "Violet shirt (locked)" if Girl.Clothes["top"] == "violet_shirt":
                        pass
                    "Black and blue pants" if Girl == KittyX and Girl.Clothes["bottom"] != "black_and_blue_pants":
                        $ item = "black_and_blue_pants"
                    "Black and blue pants (locked)" if Girl.Clothes["bottom"] == "black_and_blue_pants":
                        pass
                    "Qipao" if Girl == KittyX and Girl.Clothes["dress"] != "qipao":
                        $ item = "qipao"
                    "Qipao (locked)" if Girl.Clothes["dress"] == "qipao":
                        pass
                    "Domme outfit" if Girl == EmmaX and Girl.Clothes["bodysuit"] != "domme_suit":
                        $ item = "domme_suit"
                    "Domme outfit (locked)" if Girl.Clothes["bodysuit"] == "domme_suit":
                        pass
                    "Spiked collar" if Girl == EmmaX and Girl.Clothes["neck"] != "spiked_collar":
                        $ item = "spiked_collar"
                    "Spiked collar (locked)" if Girl.Clothes["neck"] == "spiked_collar":
                        pass
                    "Domme boots" if Girl == EmmaX and Girl.Clothes["boots"] != "domme_boots":
                        $ item = "domme_boots"
                    "Domme boots (locked)" if Girl.Clothes["boots"] == "domme_boots":
                        pass
                    "Bunny suit" if Girl == LauraX and Girl.Clothes["bodysuit"] != "bunny_suit":
                        $ item = "bunny_suit"
                    "Bunny suit (locked)" if Girl.Clothes["bodysuit"] == "bunny_suit":
                        pass
                    "Bunny ears" if Girl == LauraX and Girl.Clothes["face_outer_accessory"] != "bunny_ears":
                        $ item = "bunny_ears"
                    "Bunny ears (locked)" if Girl.Clothes["face_outer_accessory"] == "bunny_ears":
                        pass
                    "Bunny cuffs" if Girl == LauraX and Girl.Clothes["gloves"] != "bunny_gloves":
                        $ item = "bunny_gloves"
                    "Bunny cuffs (locked)" if Girl.Clothes["gloves"] == "bunny_gloves":
                        pass
                    "Sci-fi suit" if Girl == JeanX and Girl.Clothes["bodysuit"] != "sci_fi_suit":
                        $ item = "sci_fi_suit"
                    "Sci-fi suit (locked)" if Girl.Clothes["bodysuit"] == "sci_fi_suit":
                        pass
                    "Take off the [Girl.Clothes[cloak].name]." if Girl.Clothes["cloak"]:
                        $ Girl.take_off("cloak")
                    "Take off the [Girl.Clothes[top].name]." if Girl.Clothes["top"]:
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
                    "Take off the [Girl.Clothes[dress].name]." if Girl.Clothes["dress"]:
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
                    "Take off the [Girl.Clothes[bottom].name]." if Girl.Clothes["bottom"]:
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
                    "Take off the [Girl.Clothes[bodysuit].name]." if Girl.Clothes["bodysuit"]:
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
                    "Take off the [Girl.Clothes[face_outer_accessory].name]." if Girl.Clothes["face_outer_accessory"]:
                        $ Girl.take_off("face_outer_accessory")
                    "Take off the [Girl.Clothes[neck].name]." if Girl.Clothes["neck"]:
                        $ Girl.take_off("neck")
                    "Take off the [Girl.Clothes[gloves].name]." if Girl.Clothes["gloves"]:
                        $ Girl.take_off("gloves")
                    "Take off the [Girl.Clothes[boots].name]." if Girl.Clothes["boots"]:
                        $ Girl.take_off("boots")
                    "Leave dressing area.":
                        $ leave = True

                if item:
                    if item in jackets:
                        if Girl.Clothes["top"] or Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            Girl.voice "Sure. . ."

                            call change_jacket(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["jacket"] = item

                            hide black_screen onlayer black
                    elif item in tops:
                        if Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_top(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["top"] = item

                            hide black_screen onlayer black
                    elif item in dresses or item in bodysuits:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            $ Girl.change_face("sexy")

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
                                $ Girl.Clothes["dress"] = item
                            elif item in bodysuits:
                                $ Girl.Clothes["bodysuit"] = item

                            hide black_screen onlayer black
                    elif item in bras:
                        if Girl.seen_breasts or approval_check(Girl, 1000, taboo_modifier=2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_bra(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.take_off("jacket")
                            $ Girl.take_off("top")
                            $ Girl.take_off("dress")
                            $ Girl.take_off("bodysuit")
                            $ Girl.Clothes["bra"] = item

                            hide black_screen onlayer black
                    elif item in pants or item in skirts or item in shorts:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_bottom(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["bottom"] = item

                            hide black_screen onlayer black
                    elif item in cloaks:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("cloak")

                        pause 0.2

                        $ Girl.Clothes["cloak"] = item
                    elif item in face_outer_accessories:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("face_outer_accessory")

                        pause 0.2

                        $ Girl.Clothes["face_outer_accessory"] = item
                    elif item in necks:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("neck")

                        pause 0.2

                        $ Girl.Clothes["neck"] = item
                    elif item in gloves:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("gloves")

                        pause 0.2

                        $ Girl.Clothes["gloves"] = item
                    elif item in boots:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("boots")

                        pause 0.2

                        $ Girl.Clothes["boots"] = item

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
                            $ Player.Party[0].change_face("smile")

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

                            $ Girl.change_face("smile")

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

                            $ Girl.likes[Player.Party[0].tag] += 5

                            $ Player.Party[0].likes[Girl.tag] += 3

                    $ Girl.change_Outfit()

                    $ door_locked = False

                    $ Player.Party = Present[:]
                    $ Player.Party.remove(Girl)
                    $ Player.Party.append(Girl)

                    call set_the_scene(location = "bg_shop")
                    call set_Character_taboos

                    if not cart:
                        "That was fun, but since there wasn't anything she was interested in, she put it all back."

                    while cart:
                        $ item = None

                        menu:
                            "So what did you want to buy?"
                            "The Raven cloak." if "Raven_cloak" in cart:
                                $ item = "Raven_cloak"
                            "Rogue's classic jacket." if "classic_jacket" in cart:
                                $ item = "classic_jacket"
                            "The opaque fetish top." if "opaque_fetish_top" in cart:
                                $ item = "opaque_fetish_top"
                            "The sheer fetish top." if "sheer_fetish_top" in cart:
                                $ item = "sheer_fetish_top"
                            "The opaque fetish pants." if "opaque_fetish_pants" in cart:
                                $ item = "opaque_fetish_pants"
                            "The sheer fetish pants." if "sheer_fetish_pants" in cart:
                                $ item = "sheer_fetish_pants"
                            "The red dress." if "red_dress" in cart:
                                $ item = "red_dress"
                            "The blue dress." if "blue_dress" in cart:
                                $ item = "blue_dress"
                            "The Raven suit." if "Raven_suit" in cart:
                                $ item = "Raven_suit"
                            "The swimsuit." if "swimsuit" in cart:
                                $ item = "swimsuit"
                            "The sexy swimsuit." if "sexy_swimsuit" in cart:
                                $ item = "sexy_swimsuit"
                            "Rogue's classic outfit." if "catsuit" in cart:
                                $ item = "catsuit"
                            "The violet shirt." if "violet_shirt" in cart:
                                $ item = "violet_shirt"
                            "The qipao." if "qipao" in cart:
                                $ item = "qipao"
                            "The black and blue pants." if "black_and_blue_pants" in cart:
                                $ item = "black_and_blue_pants"
                            "The domme outfit." if "domme_suit" in cart:
                                $ item = "domme_suit"
                            "The spiked collar." if "spiked_collar" in cart:
                                $ item = "spiked_collar"
                            "The domme boots." if "domme_boots" in cart:
                                $ item = "domme_boots"
                            "The bunny suit." if "bunny_suit" in cart:
                                $ item = "bunny_suit"
                            "The bunny ears." if "bunny_ears" in cart:
                                $ item = "bunny_ears"
                            "The bunny cuffs." if "bunny_cuffs" in cart:
                                $ item = "bunny_cuffs"
                            "The sci-fi suit." if "sci_fi_suit" in cart:
                                $ item = "sci_fi_suit"
                            "Nothing." if "purchased" not in Player.recent_history:
                                $ Girl.change_face("sad")

                                if "shopblock" not in Girl.daily_history:
                                    $ Girl.add_word(1, "shopblock", "shopblock")
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "obedience", 3)
                                    call change_Girl_stat(Girl, "obedience", 3)

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
                                if item in ["Raven_suit", "catsuit", "domme_suit"]:
                                    $ cost = 200
                                elif item in ["Raven_cloak", "opaque_fetish_top", "sheer_fetish_top", "opaque_fetish_pants", "sheer_fetish_pants", "red_dress", "blue_dress"]:
                                    $ cost = 100
                                elif item in ["classic_jacket", "swimsuit", "sexy_swimsuit", "violet_shirt", "black_and_blue_pants", "domme_boots"]:
                                    $ cost = 75
                                elif item in ["qipao", "sci_fi_suit"]:
                                    $ cost = 300
                                elif item == "bunny_suit":
                                    $ cost = 150
                                elif item == ["spiked_collar", "bunny_cuffs"]:
                                    $ cost = 25
                                elif item == "bunny_ears":
                                    $ cost = 15

                                if Player.cash < cost:
                                    "You look at the tag - it's $[cost]. You can't afford it."

                                    $ cart.remove(item)
                                else:
                                    $ Player.cash -= cost

                            if item in cart:
                                $ cart.remove(item)

                                $ Player.add_word(1, "purchased")

                                $ Girl.inventory.append(item)
                                $ Girl.change_face("bemused", 1)

                                if item == "Raven_suit":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)
                                elif item == "Raven_cloak":
                                    call change_Girl_stat(Girl, "love", 15)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 10)
                                elif item in ["opaque_fetish_top", "opaque_fetish_pants"]:
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 30)
                                    call change_Girl_stat(Girl, "inhibition", 20)

                                    ch_r "Always did like mesh."

                                    $ Girl.change_face("smile")

                                    ch_r "Thanks, [Girl.player_petname]."
                                elif item in ["sheer_fetish_top", "sheer_fetish_pants"]:
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 30)
                                    call change_Girl_stat(Girl, "inhibition", 20)

                                    ch_r "Always did like mesh."

                                    $ Girl.change_face("smile")

                                    ch_r "Thanks, [Girl.player_petname]."
                                elif item == "qipao":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)
                                elif item == "bunny_suit":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)
                                elif item == "bunny_cuffs":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "obedience", 20)
                                    call change_Girl_stat(Girl, "inhibition", 20)
                                elif item == "bunny_ears":
                                    call change_Girl_stat(Girl, "love", 5)
                                    call change_Girl_stat(Girl, "obedience", 5)
                                    call change_Girl_stat(Girl, "inhibition", 5)

                    $ Player.drain_word("purchased")

                    $ Girl = None

    return
