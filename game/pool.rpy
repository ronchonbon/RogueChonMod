label Pool_Sunbathe(Girl=0, Type=0, Mod=0):




    menu:
        "With who?"
        "[RogueX.name]" if bg_current == RogueX.location:
            $ Girl = RogueX
        "[KittyX.name]" if bg_current == KittyX.location:
            $ Girl = KittyX
        "[EmmaX.name]" if bg_current == EmmaX.location:
            $ Girl = EmmaX
        "[LauraX.name]" if bg_current == LauraX.location:
            $ Girl = LauraX
        "[JeanX.name]" if bg_current == JeanX.location:
            $ Girl = JeanX
        "[StormX.name]" if bg_current == StormX.location:
            $ Girl = StormX
        "[JubesX.name]" if bg_current == JubesX.location:
            $ Girl = JubesX
        "Never mind.":
            return

    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
        ch_p "Hey, [Girl.name], why don't you just relax over here?"
        ch_p "You don't want to get tanlines, why don't you. . ."
        ch_p ". . . take off a few layers?"
    else:
        ch_p "Are you sure you don't want to. . ."

    if time_index >= 2:
        $ Girl.change_face("_confused")
        Girl.voice "A bit late in the day for that. . ."
        $ Girl.change_face("_normal")
        return
    if not Girl.clothingCheck():

        $ Girl.change_face("_sly")
        Girl.voice "Little late for that."
        return
    if "no_tan" in Girl.recent_history:
        $ Girl.change_face("_angry")
        Girl.voice "I just told you \"no.\""
        $ Girl.add_word(1,"_angry","_angry")
        return
    elif "no_tan" in Girl.daily_history:
        $ Girl.change_face("_angry")
        Girl.voice "Not today."
        $ Girl.add_word(1,"_angry","_angry")
        return

    if Girl == EmmaX:
        if "classcaught" not in EmmaX.history:
            $ Girl.change_face("_angry",2)
            ch_e "That would be entirely inappropriate."
            return
        if "taboo" not in EmmaX.history:
            $ Girl.change_face("_bemused",2)
            ch_e "[EmmaX.player_petname], we can't be seen like that in public. . ."
            return
        if "threesome" not in EmmaX.history:
            if not AloneCheck(EmmaX):
                $ Girl.change_face("_bemused",2)
                ch_e "Not with this sort of company. . ."
                return

    if not Girl.outfit["top"] and not Girl.outfit["bra"] and not Girl.outfit["bottom"] and not Girl.outfit["underwear"] and (not Girl.outfit["front_outer_accessory"] or Girl != JubesX):

        $ Girl.change_face("_sly")
        if Girl == RogueX:
            ch_r "I don't think that'll be a problem, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "Beat you to it."
        elif Girl == EmmaX:
            ch_e "I plan ahead."
        elif Girl == LauraX:
            ch_l "Yup."
        elif Girl == JeanX:
            ch_j "Seems that's taken care of. . ."
        elif Girl == StormX:
            ch_s "I cannot get much more naked. . ."
        elif Girl == JubesX:
            ch_v "I'm already pretty naked here. . ."
        $ Girl.add_word(1,"tan","tan")
        return

    $ line = 0
    while True:

        if not line:

            menu:
                extend ""
                "take it all off?" if (Girl.outfit["top"] or Girl.outfit["bra"]) and (Girl.outfit["bottom"] or Girl.outfit["underwear"] or Girl.outfit["hose"]):
                    if Girl.outfit["top"] == "_towel" and not Girl.outfit["bottom"] and not Girl.outfit["hose"] and not Girl.outfit["underwear"]:
                        $ Type = "no_panties"
                    elif (Girl.outfit["bottom"] or Girl.outfit["hose"]) and not Girl.outfit["underwear"]:
                        $ Type = "no_panties"
                    elif Girl.outfit["top"] and not Girl.outfit["bra"]:
                        $ Type = "no_bra"
                    else:
                        $ Type = "both"
                    $ Mod = 200

                "lose the top?" if Girl.outfit["bra"] and not Girl.outfit["top"]:
                    $ Type = "_bra"

                "maybe just lose the jacket?" if Girl.outfit["front_outer_accessory"] and Girl == JubesX:
                    if Girl.outfit["front_outer_accessory"] == "_shut_jacket" and not Girl.outfit["bottom"] and not Girl.outfit["hose"] and not Girl.outfit["underwear"]:
                        $ Type = "no_panties"
                    elif Girl.outfit["front_outer_accessory"] == "_shut_jacket" and not Girl.outfit["top"] and not Girl.outfit["bra"]:
                        $ Type = "no_bra"
                    else:
                        $ Type = "_jacket"

                "maybe just lose the [Girl.outfit['top']]?" if Girl.outfit["top"]:
                    if Girl.outfit["top"] == "_towel" and not Girl.outfit["bottom"] and not Girl.outfit["hose"] and not Girl.outfit["underwear"]:
                        $ Type = "no_panties"
                    elif not Girl.outfit["bra"]:
                        $ Type = "no_bra"
                    else:
                        $ Type = "over"

                "maybe just lose the [Girl.outfit['legs']]?" if Girl.outfit["bottom"]:
                    if not Girl.outfit["underwear"]:
                        $ Type = "no_panties"
                    else:
                        $ Type = "legs"

                "maybe just lose the [Girl.outfit['hose']]?" if Girl.outfit["hose"] and not Girl.outfit["bottom"]:
                    if not Girl.outfit["underwear"]:
                        $ Type = "no_panties"
                    else:
                        $ Type = "legs"

                "maybe just lose the [Girl.outfit['underwear']]?" if Girl.outfit["underwear"]:
                    $ Type = "_panties"
                    $ Mod = 200
                "never mind.":

                    return


        if Type == "no_panties":
            $ Mod = 200
            $ Girl.change_face("_bemused",1)
            Girl.voice "I don't have bottoms on under this. . ."
        elif Type == "no_bra":
            $ Girl.change_face("_bemused",1)
            Girl.voice "I don't have a top on under this. . ."

        if (Girl.seen_pussy and Girl.seen_breasts) and AloneCheck():
            $ Mod -= 100


        if "exhibitionist" in Girl.traits:

            $ line = "sure"
        elif approval_check(Girl, 700+Mod, "I"):

            $ line = "sure"
        elif approval_check(Girl, 1400+Mod) or (Girl == StormX and StormX in Rules):

            $ line = "sure"
        elif approval_check(Girl, 900):

            $ line = "sorry"
        else:

            $ line = "no"

        if Type == "no_bra" or Type == "no_panties":

            menu:
                extend ""
                "And?":
                    if line == "sure":
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("inhibition", 70, 1)

                        $ Girl.change_face("_sly",1)
                        if Girl == RogueX:
                            ch_r "Hmm, good point. . ."
                        elif Girl == KittyX:
                            ch_k "\"And\". . . I don't know. . ."
                        elif Girl == EmmaX:
                            ch_e "\"And\". . . you're lucky you're so cute. . ."
                        elif Girl == LauraX:
                            ch_l "I don't know. . ."
                        elif Girl == JeanX:
                            ch_j "Good point."
                        elif Girl == StormX:
                            ch_s "Just giving you fair warning. . ."
                        elif Girl == JubesX:
                            ch_v "Well. . . ok. . ."
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 70, -1)
                            $ Girl.change_stat("obedience", 80, 1)

                        $ Girl.change_face("_angry",2)
                        if Girl == RogueX:
                            ch_r "\"And\" that's all you're getting. . . for now. . ."
                        elif Girl == KittyX:
                            ch_k "\"And\". . . AND!"
                        elif Girl == EmmaX:
                            ch_e "\"And\". . . you shouldn't push your luck. . ."
                        elif Girl == LauraX:
                            ch_l "\"And\" that's all you get."
                        elif Girl == JeanX:
                            $ Girl.change_face("_bemused",1)
                            ch_j "\"And\" I'd rather not."
                        elif Girl == StormX:
                            ch_s "\"And\" I would prefer to keep it on."
                        elif Girl == JubesX:
                            ch_v "Well, I'm keeping it on."
                "Take it off anyway.":
                    if line == "sure" or (line == "sorry" and Girl != StormX and approval_check(Girl, 600+Mod, "O")):
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("obedience", 80, 2)
                        if line != "sure":
                            $ Girl.change_face("_sad",2)
                        else:
                            $ Girl.change_face("_normal",1)
                        if Girl == RogueX:
                            ch_r "Oh, ok. . ."
                        elif Girl == KittyX:
                            ch_k "Yeah, ok. . ."
                        elif Girl == EmmaX:
                            ch_e "If you insist. . ."
                        elif Girl == LauraX:
                            ch_l "Affirmative."
                        elif Girl == JeanX:
                            ch_j ". . . ok."
                        elif Girl == StormX:
                            $ Girl.change_stat("love", 80, -2)
                            ch_s ". . . fine. . ."
                        elif Girl == JubesX:
                            ch_v "Whatever. . ."

                        $ line = "sure"
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, -2)
                            $ Girl.change_stat("obedience", 80, -1)
                            $ Girl.change_stat("inhibition", 60, 1)

                        $ Girl.change_face("_angry",1)
                        if Girl == RogueX:
                            ch_r "I don't like that tone on you. . ."
                        elif Girl == KittyX:
                            ch_k "How about \"no\". . ."
                        elif Girl == EmmaX:
                            ch_e "Not with that tone. . ."
                        elif Girl == LauraX:
                            ch_l "Don't push me."
                        elif Girl == JeanX:
                            $ Girl.change_face("_bemused",1)
                            ch_j "Ha! no."
                        elif Girl == StormX:
                            $ Girl.change_stat("love", 80, -2)
                            ch_s "You presume too much."
                        elif Girl == JubesX:
                            ch_v "Nope."

                        $ Girl.add_word(1,"no_tan","no_tan")
                        return
                "Hot.":
                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                        $ Girl.change_stat("love", 80, 1)
                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                        $ Girl.change_stat("inhibition", 80, 1)

                    $ Girl.change_face("_sly",1)
                    if Girl == RogueX:
                        ch_r "Heh, you're a sweetie. . ."
                    elif Girl == KittyX:
                        ch_k "Hehe. . ."
                    elif Girl == EmmaX:
                        ch_e "How sweet. . ."
                    elif Girl == LauraX:
                        ch_l "True."
                    elif Girl == JeanX:
                        ch_j "You know it."
                    elif Girl == StormX:
                        ch_s ". . . I suppose so."
                    elif Girl == JubesX:
                        ch_v "Hehe. . ."
                "Ok, that's fine.":

                    if line == "sure":
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 80, 1)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("inhibition", 80, 1)

                        $ Girl.change_face("_sly",1)
                        if Girl == RogueX:
                            ch_r "Ready for a nice surprise? . ."
                        elif Girl == KittyX:
                            ch_k "Oh, you bet it is. . ."
                        elif Girl == EmmaX:
                            ch_e "More than you know. . ."
                        elif Girl == LauraX:
                            ch_l "But I can be generous. . ."
                        elif Girl == JeanX:
                            ch_j "But. . . I guess I can make an exception. . ."
                        elif Girl == StormX:
                            ch_s "But you are right about the value in an even tan. . ."
                        elif Girl == JubesX:
                            ch_v "You bet. . ."
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 50, 1)
                            $ Girl.change_stat("love", 80, 1)
                            $ Girl.change_stat("inhibition", 60, 1)

                        $ Girl.change_face("_smile")
                        if Girl == RogueX:
                            ch_r "Thanks, [RogueX.player_petname]. . ."
                        elif Girl == KittyX:
                            ch_k "Thanks. . ."
                        elif Girl == EmmaX:
                            ch_e "Good. . ."
                        elif Girl == LauraX:
                            ch_l "Right."
                        elif Girl == JeanX:
                            ch_j "Good. . ."
                        elif Girl == StormX:
                            ch_s "I am sorry to disappoint."
                        elif Girl == JubesX:
                            ch_v "Thanks. . ."

            if line == "sure":

                $ Girl.outfit["top"] = ""
                call expression Girl.tag + "_First_Topless"
                if Type == "no_panties":
                    $ Girl.outfit["bottom"] = ""
                    $ Girl.outfit["hose"] = ""
                    call expression Girl.tag + "_First_Bottomless"
                $ Girl.add_word(1,"tan","tan")
            else:
                $ Girl.add_word(1,"no_tan","no_tan")

            $ line = 0


        if line == "sure":

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 70, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            $ Girl.change_face("_sly",1)
            if Girl == RogueX:
                ch_r "I suppose I could. . ."
            elif Girl == KittyX:
                ch_k "I guess. . ."
            elif Girl == EmmaX:
                ch_e "Hmmm. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Yeah, ok."
            elif Girl == StormX:
                ch_s "I suppose I could."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            if Type == "_jacket" or Type == "both":
                if Girl == JubesX:
                    $ Girl.outfit["front_outer_accessory"] = ""
            if Type == "over" or Type == "both":
                $ Girl.outfit["top"] = ""
            if Type == "_bra" or Type == "both":
                $ Girl.outfit["bra"] = ""
            call expression Girl.tag + "_First_Topless"

            if Type == "legs" or Type == "both":
                $ Girl.outfit["bottom"] = ""
                $ Girl.outfit["hose"] = ""
            if Type == "_panties" or Type == "both":
                $ Girl.outfit["underwear"] = ""
            call expression Girl.tag + "_First_Bottomless"

            $ Girl.add_word(1,"tan","tan")

        elif line == "sorry" and (Type == "over" or Type == "legs" or Type == "_jacket"):

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("obedience", 80, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_face("_bemused",1)
            if Girl == RogueX:
                ch_r "I suppose I could. . ."
            elif Girl == KittyX:
                ch_k "I guess. . ."
            elif Girl == EmmaX:
                ch_e "Hmmm. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Sure, I guess."
            elif Girl == StormX:
                ch_s "I suppose I could."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            if Type == "_jacket":
                $ Girl.outfit["front_outer_accessory"] = ""
            if Type == "over":
                $ Girl.outfit["top"] = ""
            if Type == "legs":
                $ Girl.outfit["bottom"] = ""
                $ Girl.outfit["hose"] = ""
            $ Girl.add_word(1,"tan","tan")

        elif line == "sorry":

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 90, 2)
            $ Girl.change_face("_sadside",1)
            if Girl == RogueX:
                ch_r "Sorry, I think I can live with the tan lines. . ."
            elif Girl == KittyX:
                ch_k "I just can't. . ."
            elif Girl == EmmaX:
                ch_e "That just wouldn't be appropriate. . ."
            elif Girl == LauraX:
                ch_l "Nah. . ."
            elif Girl == JeanX:
                ch_j "I. . . wouldn't be comfortable with that. . ."
            elif Girl == StormX:
                ch_s "I am sorry to disappoint you."
            elif Girl == JubesX:
                ch_v "Sorry. . ."
            $ Girl.add_word(1,"no_tan","no_tan")

        elif line == "no":

            $ Girl.change_stat("love", 50, -5)
            $ Girl.change_stat("obedience", 50, 2)
            $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_face("_angry",1)
            if Girl == RogueX:
                ch_r "Not interested, [RogueX.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "Not even."
            elif Girl == EmmaX:
                ch_e "You must be dreaming. . ."
            elif Girl == LauraX:
                ch_l "Nope. . ."
            elif Girl == JeanX:
                ch_j "Ha!"
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            $ Girl.add_word(1,"no_tan","no_tan")
            return
        if not Girl.outfit["bra"] and not Girl.outfit["top"] and not Girl.outfit["underwear"] and not Girl.outfit["bottom"] and Girl.hose_number() < 10:
            $ Girl.change_outfit("nude")
        $ Mod = 0
        $ line = 0
        if Girl.clothingCheck():
            "Anything else?"
        else:
            return
    return






label Pool_Skinnydip(Girl=0, line=0, Type=0, Mod=0):




    menu:
        "With who?"
        "[RogueX.name]" if bg_current == RogueX.location:
            $ Girl = RogueX
        "[KittyX.name]" if bg_current == KittyX.location:
            $ Girl = KittyX
        "[EmmaX.name]" if bg_current == EmmaX.location:
            $ Girl = EmmaX
        "[LauraX.name]" if bg_current == LauraX.location:
            $ Girl = LauraX
        "[JeanX.name]" if bg_current == JeanX.location:
            $ Girl = JeanX
        "[StormX.name]" if bg_current == StormX.location:
            $ Girl = StormX
        "[JubesX.name]" if bg_current == JubesX.location:
            $ Girl = JubesX
        "Never mind.":
            return

    ch_p "Hey, [Girl.name], why don't we skinny dip?"

    if round <= 10:
        $ Girl.change_face("_sad")
        Girl.voice "No time for that."
        return
    elif "no_dip" in Girl.recent_history:
        $ Girl.change_face("_angry")
        Girl.voice "I just told you \"no.\""
        $ Girl.add_word(1,"_angry","_angry")
        return
    elif "no_dip" in Girl.daily_history:
        $ Girl.change_face("_angry")
        Girl.voice "Not today."
        $ Girl.add_word(1,"_angry","_angry")
        return
    elif "dip" in Girl.recent_history:
        $ Girl.change_face("_confused")
        Girl.voice "We already did that."
        return

    if Girl == EmmaX:
        if "classcaught" not in EmmaX.history:
            $ Girl.change_face("_angry",2)
            ch_e "That would be entirely inappropriate."
            return
        if "taboo" not in EmmaX.history:
            $ Girl.change_face("_bemused",2)
            ch_e "[EmmaX.player_petname], I couldn't risk us getting caught. . ."
            return
        if "threesome" not in EmmaX.history:
            if not AloneCheck(EmmaX):
                $ Girl.change_face("_bemused",2)
                ch_e "Not with this sort of company. . ."
                return

    if not Girl.clothingCheck():

        $ Girl.change_face("_sly")
        if Girl == RogueX:
            ch_r "Sure, let's get wet."
        elif Girl == KittyX:
            ch_k "Cannonball!"
        elif Girl == EmmaX:
            ch_e "Lovely."
        elif Girl == LauraX:
            ch_l "I'm in."
        elif Girl == JeanX:
            ch_j "Heh, sure."
        elif Girl == StormX:
            ch_s "I would love to."
        elif Girl == JubesX:
            ch_v "Sure!"

        $ Girl.add_word(1,"dip","dip")
    else:

        if Girl.seen_pussy and Girl.seen_breasts:
            $ Mod += 100

        if "exhibitionist" in Girl.traits:

            $ line = "sure"
        elif approval_check(Girl, 700-Mod, "I"):

            $ line = "sure"
        elif approval_check(Girl, 1200-Mod) or (Girl == StormX and StormX in Rules):

            $ line = "sure"
        elif approval_check(Girl, 800):

            $ line = "sorry"
        else:

            $ line = "no"

        if line == "sure":

            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 70, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            $ Girl.change_face("_sly",1)
            if Girl == RogueX:
                ch_r "Sounds fun. . ."
            elif Girl == KittyX:
                ch_k "Oooh, naughty. . ."
            elif Girl == EmmaX:
                ch_e "How daring. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Yeah, ok."
            elif Girl == StormX:
                ch_s "I would love to."
            elif Girl == JubesX:
                ch_v "Sure!"


            $ Girl.outfit["top"] = ""
            $ Girl.outfit["bra"] = ""
            call expression Girl.tag + "_First_Topless"

            $ Girl.outfit["bottom"] = ""
            $ Girl.outfit["hose"] = ""
            $ Girl.outfit["underwear"] = ""
            call expression Girl.tag + "_First_Bottomless"
            $ Girl.change_outfit("nude")
            $ Girl.add_word(1,"dip","dip")

        elif line == "sorry":

            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 90, 2)
            $ Girl.change_face("_sadside",1)
            if Girl == RogueX:
                ch_r "Couldn't we just take a normal swim?"
            elif Girl == KittyX:
                ch_k "I don't think so. . ."
            elif Girl == EmmaX:
                ch_e "Perhaps in a tub. . ."
            elif Girl == LauraX:
                ch_l "Nah. . ."
            elif Girl == JeanX:
                ch_j "Um, no, not right now."
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Yeah, not right now."
            menu:
                extend ""
                "Ok, we can just use swimsuits.":
                    if Girl.swimwear["outfit_active"]:

                        if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 60, 2)
                        $ Girl.change_face("_smile")
                        if Girl == RogueX:
                            ch_r "Thanks, [RogueX.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Cool."
                        elif Girl == EmmaX:
                            ch_e "That would be nice."
                        elif Girl == LauraX:
                            ch_l "Whatever."
                        elif Girl == JeanX:
                            ch_j "Yeah, ok."
                        elif Girl == StormX:
                            ch_s "Yes, that would be fine."
                        elif Girl == JubesX:
                            ch_v "Sure!"

                        show black_screen onlayer black
                        "She goes and changes into her suit. . ."
                        $ Girl.change_outfit("swimwear")
                        hide black_screen onlayer black
                        $ Girl.add_word(1,"no_dip","no_dip")
                        $ Count = 1
                    else:
                        if not Girl.change_outfit("swimwear"):
                            $ Count = 0
                    if not Count:

                        menu:
                            extend ""
                            "Then what about your undies?":
                                if Girl.bra_number() > 2 and Girl.underwear_number() > 2 and approval_check(Girl, 1000):

                                    pass
                                elif Girl.bra_number() > 1 and Girl.underwear_number() > 1 and approval_check(Girl, 1200):

                                    pass
                                else:
                                    $ Girl.change_face("_sly",1)
                                    Girl.voice "That's not going to work either."
                                    $ Girl.add_word(1,"no_dip","no_dip")
                                    return
                                $ Girl.change_face("_smile",1)
                                if Girl == RogueX:
                                    ch_r "Ok, fine. . ."
                                elif Girl == KittyX:
                                    ch_k "Fine, geez."
                                elif Girl == EmmaX:
                                    ch_e "I suppose. . ."
                                elif Girl == LauraX:
                                    ch_l "Sure, whatever. . ."
                                elif Girl == JeanX:
                                    ch_j ". . . I guess."
                                elif Girl == StormX:
                                    ch_s "Oh, I suppose so. . ."
                                elif Girl == JubesX:
                                    ch_v "I guess so. . ."
                            "Ok then, never mind.":
                                Girl.voice "Thanks."
                                $ Girl.add_word(1,"no_dip","no_dip")
                                return
                        $ Girl.outfit["top"] = ""
                        "She starts to strip down."
                        $ Girl.outfit["bottom"] = ""
                        $ Girl.outfit["hose"] = ""
                        "And ends up in her underwear."
                        $ Girl.seen_underwear = 1
                "Never mind then.":


                    $ Girl.change_stat("love", 80, -1)
                    if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                    if Girl == RogueX:
                        ch_r "Hmph."
                    elif Girl == KittyX:
                        ch_k "Bummer."
                    elif Girl == EmmaX:
                        ch_e "Disappointing."
                    elif Girl == LauraX:
                        ch_l "K."
                    elif Girl == StormX:
                        ch_s "Thank you, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Ok."
                    $ Girl.add_word(1,"no_dip","no_dip")
                    return

        elif line == "no":

            $ Girl.change_stat("love", 50, -5)
            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_face("_angry",1)
            if Girl == RogueX:
                ch_r "Not interested, [RogueX.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "Not even."
            elif Girl == EmmaX:
                ch_e "You must be dreaming. . ."
            elif Girl == LauraX:
                ch_l "Nope. . ."
            elif Girl == JeanX:
                $ Girl.change_face("_bemused",1)
                ch_j "Ha!"
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Sorry. . ."

            $ Girl.add_word(1,"no_dip","no_dip")
            return

    call ShowPool ([Girl])
    $ Girl.wet = 1
    $ round -= 20 if round >= 20 else round
    "You both swim around for a bit."
    hide FullPool
    call set_the_scene (1, 0, 0)

    return





label Pool_Topless(Girl=focused_Girl, temp_Girls=[]):

    if Girl.location != bg_current:

        $ temp_Girls = all_Girls[:]
        $ renpy.random.shuffle(temp_Girls)
        while temp_Girls:
            if temp_Girls[0].location == bg_current:
                call shift_focus (temp_Girls[0])
                $ temp_Girls = [1]
            $ temp_Girls.remove(temp_Girls[0])

    $ focused_Girl = Girl
    if (Girl.bra_number() <= 1 and Girl.top_number() <= 1) or Girl.location != bg_current:

        $ D20 = renpy.random.randint(1, 14)
        return
    $ Girl.top_pulled_up = 1
    "[Girl.name] dives into the pool"
    menu:
        "It appears she's had a wardrobe malfunction."
        "Hey, [Girl.name]. . .":
            ch_p "Looks like you might be missing something there. . ."
            $ Girl.change_face("_confused")
            if Girl != StormX:
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 50, -2)
                Girl.voice ". . ."
                $ Girl.change_face("_surprised",2,eyes="_down")
            $ Girl.change_stat("love", 80, 3)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("lust", 50, 2)
            $ Count = 100
        "Say nothing":
            $ Girl.change_face("_surprised",2,eyes="_down")
            "After a few moments, [Girl.name] seems to notice that her top rode up."
            if approval_check(Girl, 1200):
                $ Count = 0
            else:
                $ Count = -100

    if approval_check(Girl, 800-Count,"I") or approval_check(Girl, 1600-Count) or (Girl == StormX and StormX in Rules):
        $ Girl.change_face("_sly")
        $ Girl.outfit["bra"] = ""
        $ Girl.outfit["top"] = ""
        $ Girl.change_stat("obedience", 60, 2)
        $ Girl.change_stat("inhibition", 50, 4)
        $ Girl.change_stat("inhibition", 90, 2)
        $ Girl.change_stat("lust", 50, 5)
        "She smiles and tosses her top over her head."
        call expression Girl.tag + "_First_Topless"
    elif approval_check(Girl, 500-Count,"I") or approval_check(Girl, 1200-Count):
        $ Girl.change_face("_sly",1)
        $ Girl.change_stat("obedience", 60, 2)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("inhibition", 80, 2)
        $ Girl.change_stat("lust", 50, 3)
        "She smiles, and leaves the top how it is."
        call expression Girl.tag + "_First_Topless"
    else:
        if approval_check(Girl, 800-Count) or (Girl == StormX):

            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("inhibition", 70, 2)
            $ Girl.change_stat("lust", 50, 1)
            $ Girl.change_face("_bemused",2)
        else:

            $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_face("_angry",2)
        call expression Girl.tag + "_First_Topless" pass (1)
        $ Girl.top_pulled_up = 0
        "She tugs her top back into place."
        if Count <= 0:
            $ Girl.change_stat("love", 70, -5)
            $ Girl.change_stat("obedience", 60, -2)
            $ Girl.change_stat("inhibition", 60, 2)
            Girl.voice "You could have told me."

    $ Count = 0
    return



label Pool_Swim(Swimmers=[], temp_Girls=[]):
    $ D20 = renpy.random.randint(1, 20)

    $ Player.daily_history.append("swim")
    call set_the_scene

    $ line = ""
    $ Passline = 0
    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if bg_current == temp_Girls[0].location and approval_check(temp_Girls[0], 700):
            if temp_Girls[0].outfit["bra"] == temp_Girls[0].swimwear[5] and temp_Girls[0].outfit["underwear"] == temp_Girls[0].swimwear[6]:

                $ Swimmers.append(temp_Girls[0])
            elif not temp_Girls[0].bra_number() and not temp_Girls[0].top_number() and not temp_Girls[0].underwear_number() and not temp_Girls[0].bottom_number() and not temp_Girls[0].hose_number():

                $ Swimmers.append(temp_Girls[0])
            else:
                if line or Passline:

                    call display_girl (temp_Girls[0], 0, 0, 950, 150)
                else:
                    call display_girl (temp_Girls[0], 0, 0, 800, 150)
                if temp_Girls[0].change_outfit("swimwear"):

                    $ line = "" if Swimmers and not Passline else "s"
                    $ Swimmers.append(temp_Girls[0])
                else:

                    $ line = "" if Passline and not Swimmers else "s"
                    $ Passline = Passline + " and " + temp_Girls[0].name if Passline else temp_Girls[0].name
        $ temp_Girls.remove(temp_Girls[0])

    if len(Swimmers) >= 2:
        "The girls get[line] changed and join you."
    elif Swimmers:
        "[Swimmers[0].name] get[line] changed and joins you."
    if Passline:
        "[Passline] chill[line] out poolside."
    $ Passline = 0
    $ line = 0

    call ShowPool (Swimmers[:])

    if D20 >= 15 and Swimmers:
        call Pool_Topless (Swimmers[0])
    if D20 >= 11:
        "You take a nice, refreshing swim."
    elif D20 == 2:
        "You join some of the others in a rousing game of Marco Polo."
    elif D20 == 3:
        "You manage to snag one of the floating chairs and drift lazily on the water."
    elif D20 == 4:
        "You manage to snag one of the floating chairs and drift lazily on the water."
        "Until, that is, Kurt teleports up in the air nearby and performs an admittedly awesome cannonball."
        "Too bad it capsizes your chair."
    elif D20 == 5:
        "You test yourself by swimming from one end of the pool to the other."
    elif D20 == 6:
        "You try to impress some of the girls by doing a running jump into the pool."
        "You wind up triggering a cannonball competition that’s ironically NOT won by Cannonball, much to his shock."
    elif D20 == 7:
        "You are about to get into the pool when you hear annoyed cries and shouts of, \"Bobby!\""
        "Looks like Iceman made himself a floating chair again."
        "You stick to the far end of the pool, where it isn’t freezing cold."
    elif D20 == 8:
        "You relax on one of the poolside chairs instead."
    elif D20 == 9:
        "Cyclops is instructing some of the other students in water rescues."
        "You listen in as he talks about approaching a drowning victim from behind so that their panicked flailing won’t cause you injury."
    elif D20 == 10:
        "You decide to make use of the diving board. You do a couple of dives before taking it easy and just swimming around."

    call who_likes_who (80, 3)
    call RoomStatboost ("love", 80, 3)
    call RoomStatboost ("lust", 30, 5)
    $ round -= 20 if round >= 20 else round
    hide FullPool
    call set_the_scene (1, 0, 0)
    "You all get out of the pool and rest for a bit."

    return




label SwimSuit(temp_Girls=[]):

    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current and temp_Girls[0].swimwear["outfit_active"] and temp_Girls[0] not in Party and temp_Girls[0].weekly_schedule[weekday][time_index] == "bg_pool":


            $ temp_Girls[0].change_outfit("swimwear")
        $ temp_Girls.remove(temp_Girls[0])
    return

image FullPool:

    AlphaMask("bg_pool", "images/background/bg_pool_mask.png")

label ShowPool(temp_Girls=[], PoolLoc=0):



    while temp_Girls:
        if temp_Girls[0].location == bg_current:
            $ temp_Girls[0].add_word(0,"swim","swim",0,0)
            $ temp_Girls[0].wet = 1
            $ temp_Girls[0].spunk = []
            $ PoolLoc = 500 if len(temp_Girls) > 1 else 650
            if temp_Girls[0] == RogueX:
                show Rogue_sprite zorder 50 at Pool_Bob(PoolLoc)
            elif temp_Girls[0] == KittyX:
                show Kitty_sprite zorder 50 at Pool_Bob(PoolLoc)
            elif temp_Girls[0] == EmmaX:
                show Emma_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif temp_Girls[0] == LauraX:
                show Laura_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif temp_Girls[0] == JeanX:
                show Jean_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif temp_Girls[0] == StormX:
                show Storm_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif temp_Girls[0] == JubesX:
                show Jubes_Sprite zorder 50 at Pool_Bob(PoolLoc)
        $ temp_Girls.remove(temp_Girls[0])
    show FullPool zorder 60
    return










transform Pool_Bob(PoolLoc=500):
    subpixel True
    pos (PoolLoc,450)
    alpha 1
    zoom .45
    offset (0,0)
    anchor (0.5, 0.0)
    xoffset 0
    yoffset 0
    choice:
        yoffset 0
    choice:
        pause .3
    choice:
        pause .5
    block:
        ease 1 yoffset 10
        ease 1.5 yoffset 0
        repeat
