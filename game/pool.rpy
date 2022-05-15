label Pool_Sunbathe(Girl=0,Type=0,Mod=0): #rkeljsv
    # This gets called with a Girl name, and checks
    # line tends to carry the current agreement state, Type tends to carry the item being discussed
    # mod is a modifier, base 0, but +200 if asking for no bottoms

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

    if time_index >= 2: #night/evening time
            $ Girl.change_face("confused")
            call Anyline(Girl,"A bit late in the day for that. . .")
            $ Girl.change_face("normal")
            return
    if not Girl.ClothingCheck():
            #if she's already nude. . .
            $ Girl.change_face("sly")
            call Anyline(Girl,"Little late for that.")
            return
    if "no_tan" in Girl.recent_history:
            $ Girl.change_face("angry")
            call Anyline(Girl,"I just told you \"no.\"")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "no_tan" in Girl.daily_history :
            $ Girl.change_face("angry")
            call Anyline(Girl,"Not today.")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return

    if Girl == EmmaX:
            if "classcaught" not in EmmaX.History:
                        $ Girl.change_face("angry",2)
                        ch_e "That would be entirely inappropriate."
                        return
            if "taboo" not in EmmaX.History:
                        $ Girl.change_face("bemused",2)
                        ch_e "[EmmaX.Petname], we can't be seen like that in public. . ."
                        return
            if "three" not in EmmaX.History:
                if not AloneCheck(EmmaX):
                        $ Girl.change_face("bemused",2)
                        ch_e "Not with this sort of company. . ."
                        return

    if not Girl.Over and not Girl.Chest and not Girl.Legs and not Girl.Panties and (not Girl.Acc or Girl != JubesX): #jubilee could have a coat without that last bit
            #if she's already nude. . .
            $ Girl.change_face("sly")
            if Girl == RogueX:
                    ch_r "I don't think that'll be a problem, [RogueX.Petname]."
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
            $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
            return

    $ line = 0
    while True:
            #loops until you return
            if not line:
                #only asks questions if there's not a play on the table.
                menu:
                    extend ""
                    "take it all off?" if (Girl.Over or Girl.Chest) and (Girl.Legs or Girl.Panties or Girl.Hose):
                            if Girl.Over == "towel" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no_panties"
                            elif (Girl.Legs or Girl.Hose) and not Girl.Panties:
                                $ Type = "no_panties"
                            elif Girl.Over and not Girl.Chest:
                                $ Type = "no_bra"
                            else:
                                $ Type = "both"
                            $ Mod = 200

                    "lose the top?" if Girl.Chest and not Girl.Over:
                            $ Type = "bra"

                    "maybe just lose the jacket?" if Girl.Acc and Girl == JubesX:
                            if Girl.Acc == "shut jacket" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no_panties"
                            elif Girl.Acc == "shut jacket" and not Girl.Over and not Girl.Chest:
                                $ Type = "no_bra"
                            else:
                                $ Type = "jacket"

                    "maybe just lose the [Girl.Over]?" if Girl.Over:
                            if Girl.Over == "towel" and not Girl.Legs and not Girl.Hose and not Girl.Panties:
                                $ Type = "no_panties"
                            elif not Girl.Chest:
                                $ Type = "no_bra"
                            else:
                                $ Type = "over"

                    "maybe just lose the [Girl.Legs]?" if Girl.Legs:
                            if not Girl.Panties:
                                $ Type = "no_panties"
                            else:
                                $ Type = "legs"

                    "maybe just lose the [Girl.Hose]?" if Girl.Hose and not Girl.Legs:
                            if not Girl.Panties:
                                $ Type = "no_panties"
                            else:
                                $ Type = "legs"

                    "maybe just lose the [Girl.Panties]?" if Girl.Panties:
                                $ Type = "panties"
                                $ Mod = 200

                    "never mind.":
                            return
            # end menu

            if Type == "no_panties":
                    $ Mod = 200
                    $ Girl.change_face("bemused",1)
                    call Anyline(Girl,"I don't have bottoms on under this. . .")
            elif Type == "no_bra":
                    $ Girl.change_face("bemused",1)
                    call Anyline(Girl,"I don't have a top on under this. . .")

            if (Girl.SeenPussy and Girl.SeenChest) and AloneCheck(): #makes it easier if you've already seen her
                    $ Mod -= 100

            # This is the primary check to see whether she's into it.
            if "exhibitionist" in Girl.Traits:
                    #if she's an exhibitionist
                    $ line = "sure"
            elif ApprovalCheck(Girl, 700+Mod, "I"):
                    #if she's generally slutty
                    $ line = "sure"
            elif ApprovalCheck(Girl, 1400+Mod) or (Girl == StormX and StormX in Rules):
                    # if she really likes you.
                    $ line = "sure"
            elif ApprovalCheck(Girl, 900):
                    # if she is fairly casual, not not enough
                    $ line = "sorry"
            else:
                    # if she refuses
                    $ line = "no"

            if Type == "no_bra" or Type == "no_panties":
                    #checks to see if she'd lose her jacket/pants if nothing on under
                    menu:
                        extend ""
                        "And?":
                            if line == "sure":
                                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                                        $ Girl.change_stat("inhibition", 70, 1)

                                    $ Girl.change_face("sly",1)
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

                                    $ Girl.change_face("angry",2)
                                    if Girl == RogueX:
                                            ch_r "\"And\" that's all you're getting. . . for now. . ."
                                    elif Girl == KittyX:
                                            ch_k "\"And\". . . AND!"
                                    elif Girl == EmmaX:
                                            ch_e "\"And\". . . you shouldn't push your luck. . ."
                                    elif Girl == LauraX:
                                            ch_l "\"And\" that's all you get."
                                    elif Girl == JeanX:
                                            $ Girl.change_face("bemused",1)
                                            ch_j "\"And\" I'd rather not."
                                    elif Girl == StormX:
                                            ch_s "\"And\" I would prefer to keep it on."
                                    elif Girl == JubesX:
                                            ch_v "Well, I'm keeping it on."
                        "Take it off anyway.":
                            if line == "sure" or (line == "sorry" and Girl != StormX and ApprovalCheck(Girl, 600+Mod, "O")):
                                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                                        $ Girl.change_stat("obedience", 50, 1)
                                        $ Girl.change_stat("obedience", 80, 2)
                                    if line != "sure":
                                            $ Girl.change_face("sad",2)
                                    else:
                                            $ Girl.change_face("normal",1)
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

                                    $ Girl.change_face("angry",1)
                                    if Girl == RogueX:
                                            ch_r "I don't like that tone on you. . ."
                                    elif Girl == KittyX:
                                            ch_k "How about \"no\". . ."
                                    elif Girl == EmmaX:
                                            ch_e "Not with that tone. . ."
                                    elif Girl == LauraX:
                                            ch_l "Don't push me."
                                    elif Girl == JeanX:
                                            $ Girl.change_face("bemused",1)
                                            ch_j "Ha! no."
                                    elif Girl == StormX:
                                            $ Girl.change_stat("love", 80, -2)
                                            ch_s "You presume too much."
                                    elif Girl == JubesX:
                                            ch_v "Nope."

                                    $ Girl.AddWord(1,"no_tan","no_tan") #adds the "no_tan" trait to recent and daily actions
                                    return
                        "Hot.":
                                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                                        $ Girl.change_stat("love", 80, 1)
                                        $ Girl.change_stat("obedience", 70, 2)
                                        $ Girl.change_stat("inhibition", 60, 1)
                                        $ Girl.change_stat("inhibition", 80, 1)

                                    $ Girl.change_face("sly",1)
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

                                    $ Girl.change_face("sly",1)
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

                                    $ Girl.change_face("smile")
                                    if Girl == RogueX:
                                            ch_r "Thanks, [RogueX.Petname]. . ."
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
                            #she agrees
                            $ Girl.Over = 0 # removes Over
                            call first_topless(Girl)
                            if Type == "no_panties":
                                    $ Girl.Legs = 0 # removes Legs
                                    $ Girl.Hose = 0 # removes Hose
                                    call expression Girl.Tag + "_First_Bottomless"
                            $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions
                    else:
                            $ Girl.AddWord(1,"no_tan","no_tan") #adds the "no_tan" trait to recent and daily actions

                    $ line = 0
            # end "nothing on under this. . ."

            if line == "sure":
                    #She agrees. . .
                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 70, 2)
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("inhibition", 70, 2)
                            $ Girl.change_stat("inhibition", 90, 1)
                    $ Girl.change_face("sly",1)
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

                    if Type == "jacket" or Type == "both":
                        if Girl == JubesX:
                            $ Girl.Acc = 0
                    if Type == "over" or Type == "both":
                            $ Girl.Over = 0
                    if Type == "bra" or Type == "both":
                            $ Girl.Chest = 0
                    call first_topless(Girl)

                    if Type == "legs" or Type == "both":
                            $ Girl.Legs = 0 # removes Legs
                            $ Girl.Hose = 0 # removes Hose
                    if Type == "panties" or Type == "both":
                            $ Girl.Panties = 0
                    call expression Girl.Tag + "_First_Bottomless"

                    $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions

            elif line == "sorry" and (Type == "over" or Type == "legs" or Type == "jacket"):
                    #She agrees to just an over-layer. . .
                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("obedience", 80, 1)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_face("bemused",1)
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

                    if Type == "jacket":
                            $ Girl.Acc = 0
                    if Type == "over":
                            $ Girl.Over = 0
                    if Type == "legs":
                            $ Girl.Legs = 0
                            $ Girl.Hose = 0
                    $ Girl.AddWord(1,"tan","tan") #adds the "tan" trait to recent and daily actions

            elif line == "sorry":
                    #She refuses but is not offended. . .
                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("obedience", 80, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("inhibition", 90, 2)
                    $ Girl.change_face("sadside",1)
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
                    $ Girl.AddWord(1,"no_tan","no_tan") #adds the "no_tan" trait to recent and daily actions

            elif line == "no":
                    #She is offended you even asked. . .
                    $ Girl.change_stat("love", 50, -5)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
                    $ Girl.change_face("angry",1)
                    if Girl == RogueX:
                            ch_r "Not interested, [RogueX.Petname]. . ."
                    elif Girl == KittyX:
                            ch_k "Not even."
                    elif Girl == EmmaX:
                            ch_e "You must be dreaming. . ."
                    elif Girl == LauraX:
                            ch_l "Nope. . ."
                    elif Girl == JeanX:
                            ch_j "Ha!"
                    elif Girl == StormX:
                            ch_s "I am afraid not, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "Sure. . ."

                    $ Girl.AddWord(1,"no_tan","no_tan") #adds the "no_tan" trait to recent and daily actions
                    return
            if not Girl.Chest and not Girl.Over and not Girl.Panties and not Girl.Legs and Girl.HoseNum() < 10:
                        $ Girl.OutfitChange("nude") #removes remaining clothing.
            $ Mod = 0
            $ line = 0
            if Girl.ClothingCheck():
                "Anything else?" #loops back to menu
            else:
                return
    return

label Pool_Skinnydip(Girl=0,line=0,Type=0,Mod=0): #rkeljsv
    # This gets called with a Girl name, and checks
    # line tends to carry the current agreement state, Type tends to carry the item being discussed
    # mod is a modifier, base 0, but +200 if asking for no bottoms

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

    if Round <= 10:
            $ Girl.change_face("sad")
            call Anyline(Girl,"No time for that.")
            return
    elif "no_dip" in Girl.recent_history:
            $ Girl.change_face("angry")
            call Anyline(Girl,"I just told you \"no.\"")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "no_dip" in Girl.daily_history:
            $ Girl.change_face("angry")
            call Anyline(Girl,"Not today.")
            $ Girl.AddWord(1,"angry","angry") #makes her angry
            return
    elif "dip" in Girl.recent_history:
            $ Girl.change_face("confused")
            call Anyline(Girl,"We already did that.")
            return

    if Girl == EmmaX:
            if "classcaught" not in EmmaX.History:
                    $ Girl.change_face("angry",2)
                    ch_e "That would be entirely inappropriate."
                    return
            if "taboo" not in EmmaX.History:
                    $ Girl.change_face("bemused",2)
                    ch_e "[EmmaX.Petname], I couldn't risk us getting caught. . ."
                    return
            if "three" not in EmmaX.History:
                    if not AloneCheck(EmmaX):
                            $ Girl.change_face("bemused",2)
                            ch_e "Not with this sort of company. . ."
                            return

    if not Girl.ClothingCheck():
            #if she's already nude. . .
            $ Girl.change_face("sly")
            if Girl == RogueX:
                    ch_r "Sure, let's get wet."
            elif Girl == KittyX:
                    ch_k "Cannonball!"
            elif Girl == EmmaX:
                    ch_e "lovely."
            elif Girl == LauraX:
                    ch_l "I'm in."
            elif Girl == JeanX:
                    ch_j "Heh, sure."
            elif Girl == StormX:
                    ch_s "I would love to."
            elif Girl == JubesX:
                    ch_v "Sure!"

            $ Girl.AddWord(1,"dip","dip") #adds the "dip" trait to recent and daily actions
    else:
            #if she's dressed. . .
            if Girl.SeenPussy and Girl.SeenChest:
                    $ Mod += 100

            if "exhibitionist" in Girl.Traits:
                    #if she's an exhibitionist
                    $ line = "sure"
            elif ApprovalCheck(Girl, 700-Mod, "I"):
                    #if she's generally slutty
                    $ line = "sure"
            elif ApprovalCheck(Girl, 1200-Mod) or (Girl == StormX and StormX in Rules):
                    # if she really likes you.
                    $ line = "sure"
            elif ApprovalCheck(Girl, 800):
                    # if she is fairly casual, not not enough
                    $ line = "sorry"
            else:
                    # if she refuses
                    $ line = "no"

            if line == "sure":
                    #She agrees. . .
                    if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 70, 2)
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("inhibition", 70, 2)
                            $ Girl.change_stat("inhibition", 90, 1)
                    $ Girl.change_face("sly",1)
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


                    $ Girl.Over = 0 # removes Over
                    $ Girl.Chest = 0 # removes Bra
                    call first_topless(Girl)

                    $ Girl.Legs = 0 # removes Legs
                    $ Girl.Hose = 0 # removes Hose
                    $ Girl.Panties = 0 # removes Panties
                    call expression Girl.Tag + "_First_Bottomless"
                    $ Girl.OutfitChange("nude") #removes remaining clothing.
                    $ Girl.AddWord(1,"dip","dip") #adds the "dip" trait to recent and daily actions

            elif line == "sorry":
                    #She refuses but is not offended. . .
                    if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("obedience", 80, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("inhibition", 90, 2)
                    $ Girl.change_face("sadside",1)
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
                            ch_s "I am afraid not, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "Yeah, not right now."
                    menu:
                        extend ""
                        "Ok, we can just use swimsuits.":
                                if Girl.Swim[0]:
                                        #if she has a suit to put on. . .
                                        if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                                                $ Girl.change_stat("love", 80, 2)
                                                $ Girl.change_stat("obedience", 50, 1)
                                                $ Girl.change_stat("inhibition", 60, 2)
                                        $ Girl.change_face("smile")
                                        if Girl == RogueX:
                                                ch_r "Thanks, [RogueX.Petname]."
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

                                        show blackscreen onlayer black
                                        "She goes and changes into her suit. . ."
                                        $ Girl.OutfitChange("swimwear") # puts on her swimsuit
                                        hide blackscreen onlayer black
                                        $ Girl.AddWord(1,"no_dip","no_dip") #adds the "no_tan" trait to recent and daily actions
                                        $ Count = 1
                                else:
                                        if not Girl.OutfitChange("swimwear"):
                                                $ Count = 0
                                if not Count:
                                    #If she has no suit. . .
                                    menu:
                                        extend ""
                                        "Then what about your undies?":
                                                if Girl.ChestNum() > 2 and Girl.PantiesNum() > 2 and ApprovalCheck(Girl, 1000):
                                                        #if she mostly likes you, and is wearing decent undies. . .
                                                        pass
                                                elif Girl.ChestNum() > 1 and Girl.PantiesNum() > 1 and ApprovalCheck(Girl, 1200):
                                                        #if she mostly likes you, and is wearing scandelous undies. . .
                                                        pass
                                                else:
                                                        $ Girl.change_face("sly",1)
                                                        call Anyline(Girl,"That's not going to work either.")
                                                        $ Girl.AddWord(1,"no_dip","no_dip")
                                                        return
                                                $ Girl.change_face("smile",1)
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
                                                call Anyline(Girl,"Thanks.")
                                                $ Girl.AddWord(1,"no_dip","no_dip")
                                                return
                                    $ Girl.Over = 0 # Takes off Over
                                    "She starts to strip down."
                                    $ Girl.Legs = 0 # Takes off Legs
                                    $ Girl.Hose = 0 # Takes off Hose
                                    "And ends up in her underwear."
                                    $ Girl.SeenPanties = 1


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
                                        ch_s "Thank you, [Girl.Petname]."
                                elif Girl == JubesX:
                                        ch_v "Ok."
                                $ Girl.AddWord(1,"no_dip","no_dip") #adds the "no_tan" trait to recent and daily actions
                                return

            elif line == "no":
                    #She is offended you even asked. . .
                    $ Girl.change_stat("love", 50, -5)
                    if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                    $ Girl.change_face("angry",1)
                    if Girl == RogueX:
                            ch_r "Not interested, [RogueX.Petname]. . ."
                    elif Girl == KittyX:
                            ch_k "Not even."
                    elif Girl == EmmaX:
                            ch_e "You must be dreaming. . ."
                    elif Girl == LauraX:
                            ch_l "Nope. . ."
                    elif Girl == JeanX:
                            $ Girl.change_face("bemused",1)
                            ch_j "Ha!"
                    elif Girl == StormX:
                            ch_s "I am afraid not, [Girl.Petname]."
                    elif Girl == JubesX:
                            ch_v "Sorry. . ."

                    $ Girl.AddWord(1,"no_dip","no_dip") #adds the "no_tan" trait to recent and daily actions
                    return

    call ShowPool([Girl]) #displays pool graphics
    $ Girl.Water = 1
    $ Round -= 20 if Round >= 20 else Round
    "You both swim around for a bit."
    hide FullPool
    call set_the_scene(1,0,0)

    return

label Pool_Topless(Girl=focused_Girl,Girls=[]): #rkeljsv
        #the girl is swimming, but ends up topless temporarily
        if Girl.location != bg_current:
                    #if the lead girl isn't in the room for some reason. . .
                    $ Girls = all_Girls[:]
                    $ renpy.random.shuffle(Girls)
                    while Girls:
                            if Girls[0].location == bg_current:
                                    call shift_focus(Girls[0])
                                    $ Girls = [1]
                            $ Girls.remove(Girls[0])

        $ focused_Girl = Girl
        if (Girl.ChestNum() <= 1 and Girl.OverNum() <= 1) or Girl.location != bg_current:
                #if *no* girls are present, ditch or no point, already topless
                $ D20 = renpy.random.randint(1, 14)
                return
        $ Girl.Uptop = 1 #sets uptop
        "[Girl.name] dives into the pool"
        menu:
            "It appears she's had a wardrobe malfunction."
            "Hey, [Girl.name]. . .":
                    ch_p "Looks like you might be missing something there. . ."
                    $ Girl.change_face("confused")
                    if Girl != StormX:
                            $ Girl.change_stat("obedience", 60, 2)
                            $ Girl.change_stat("inhibition", 50, -2)
                            call Anyline(Girl,". . .")
                            $ Girl.change_face("surprised",2,Eyes="down")
                    $ Girl.change_stat("love", 80, 3)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("lust", 50, 2)
                    $ Count = 100
            "Say nothing":
                    $ Girl.change_face("surprised",2,Eyes="down")
                    "After a few moments, [Girl.name] seems to notice that her top rode up."
                    if ApprovalCheck(Girl, 1200):
                            $ Count = 0
                    else:
                            $ Count = -100

        if ApprovalCheck(Girl, 800-Count,"I") or ApprovalCheck(Girl, 1600-Count) or (Girl == StormX and StormX in Rules):
                $ Girl.change_face("sly")
                $ Girl.Chest = 0 #loses top
                $ Girl.Over = 0 #loses top
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 50, 4)
                $ Girl.change_stat("inhibition", 90, 2)
                $ Girl.change_stat("lust", 50, 5)
                "She smiles and tosses her top over her head."
                call first_topless(Girl)
        elif ApprovalCheck(Girl, 500-Count,"I") or ApprovalCheck(Girl, 1200-Count):
                $ Girl.change_face("sly",1)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.change_stat("lust", 50, 3)
                "She smiles, and leaves the top how it is."
                call first_topless(Girl)
        else:
                if ApprovalCheck(Girl, 800-Count) or (Girl == StormX):
                        #she's ok with it
                        $ Girl.change_stat("obedience", 60, 2)
                        $ Girl.change_stat("inhibition", 70, 2)
                        $ Girl.change_stat("lust", 50, 1)
                        $ Girl.change_face("bemused",2)
                else:
                        #she's mad
                        $ Girl.change_stat("love", 70, -2)
                        $ Girl.change_stat("inhibition", 50, 1)
                        $ Girl.change_face("angry",2)
                call first_topless(Girl, silent = 1)
                $ Girl.Uptop = 0 #resets uptop
                "She tugs her top back into place."
                if Count <= 0:
                        $ Girl.change_stat("love", 70, -5)
                        $ Girl.change_stat("obedience", 60, -2)
                        $ Girl.change_stat("inhibition", 60, 2)
                        call Anyline(Girl,"You could have told me.")

        $ Count = 0
        return

label Pool_Entry:
    call Jubes_Entry_Check
    $ door_locked = False
    $ bg_current = "bg_pool"
    $ Nearby = []
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call Gym_Clothes_Off #call Gym_Clothes
    call SwimSuit #puts girls in swimsuits if already here
    call set_the_scene

label Pool_Room:
    $ bg_current = "bg_pool"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene(Quiet=1,Dress=0)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if time_index >= 3: #night time
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait
                call EventCalls
                call Girls_Location
    call GirlsAngry
    #End Room Set-up

    menu:
        "You're at the pool. What would you like to do?"

        "Chat":
                call Chat

        "Want to sunbathe?" if time_index < 2:
                call Pool_Sunbathe
                $ Round -= 20 if Round >= 20 else Round
                "You just hang out for a little while."
        "Want to swim?":
            if time_index >= 3 and AloneCheck():
                "It's a bit late for a swim."
            else:
                call Pool_Swim
        "Want to skinnydip?":
                call Pool_Skinnydip

        "Wait. (locked)" if time_index >= 3: #night
                pass
        "Wait." if time_index < 3: #not night
                "You hang out for a bit."
                call Wait
                call EventCalls
                call Girls_Location

        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry

        "Go to the showers" if TravelMode:
                jump Shower_Room_Entry
    jump Pool_Room

label Pool_Swim(Swimmers=[],Girls=[]):
    $ D20 = renpy.random.randint(1, 20)

    $ Player.daily_history.append("swim")
    call set_the_scene

    $ line = ""
    $ Passline = 0
    $ Girls = all_Girls[:]
    while Girls:
            if bg_current == Girls[0].location and ApprovalCheck(Girls[0], 700):
                    if Girls[0].Chest == Girls[0].Swim[5] and Girls[0].Panties == Girls[0].Swim[6]:
                                # if she's already in swimwear . . .
                                $ Swimmers.append(Girls[0])
                    elif not Girls[0].ChestNum() and not Girls[0].OverNum() and not Girls[0].PantiesNum() and not Girls[0].PantsNum() and not Girls[0].HoseNum():
                                # or is nude. . .
                                $ Swimmers.append(Girls[0])
                    else:
                        if line or Passline:
                                #if it's second time through
                                call Display_Girl(Girls[0],0,0,950,150)
                        else:
                                call Display_Girl(Girls[0],0,0,800,150)
                        if Girls[0].OutfitChange("swimwear"):
                                #if changed into swimsuit. . .
                                $ line = "" if Swimmers and not Passline else "s" #whole point of this is to change the plaurals
                                $ Swimmers.append(Girls[0])
                        else:
                                #If she doesn't swim. . .
                                $ line = "" if Passline and not Swimmers else "s"
                                $ Passline = Passline + " and " + Girls[0].name if Passline else Girls[0].name
            $ Girls.remove(Girls[0])

    if len(Swimmers) >= 2:
            "The girls get[line] changed and join you."
    elif Swimmers:
            "[Swimmers[0].name] get[line] changed and joins you."
    if Passline:
            "[Passline] chill[line] out poolside."
    $ Passline = 0
    $ line = 0

    call ShowPool(Swimmers[:]) #displays pool graphics

    if D20 >= 15 and Swimmers:
            call Pool_Topless(Swimmers[0])
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

    call GirlWaitUp(1,80,3) #makes any girls in the room like each other a bit more.
    call RoomStatboost("love",80,3)
    call RoomStatboost("lust",30,5)
    $ Round -= 20 if Round >= 20 else Round
    hide FullPool
    call set_the_scene(1,0,0)
    "You all get out of the pool and rest for a bit."
    return

label SwimSuit(Girls=[]):
        # puts girls in swimsuit if applicable
        $ Girls = all_Girls[:]
        while Girls:
                if Girls[0].location == bg_current and Girls[0].Swim[0] and Girls[0] not in Party and Girls[0].Schedule[Weekday][time_index] == "bg_pool":
                        #if she has a suit, is not in the party, is at this location, and is scehduled to be there, put her in a swimsuit.
                        $ Girls[0].OutfitChange("swimwear") # puts on her swimsuit
                $ Girls.remove(Girls[0])
        return

image FullPool:
        #water
        AlphaMask("bg_pool", "images/PoolMask.png")

label ShowPool(Girls=[],PoolLoc=0): #rkeljsv
        #displays the pool with girls in it
        #if not Girls:
                #$ Girls = active_Girls[:]
        while Girls:
                if Girls[0].location == bg_current:
                            $ Girls[0].AddWord(0,"swim","swim",0,0) #adds "swim" tag to recent and daily actions
                            $ Girls[0].Water = 1
                            $ Girls[0].Spunk = []
                            $ PoolLoc = 500 if len(Girls) > 1 else 650
                            if Girls[0] == RogueX:
                                    show Rogue_Sprite at Pool_Bob(PoolLoc) zorder 50  #Girls[0].Layer
                            elif Girls[0] == KittyX:
                                    show Kitty_Sprite at Pool_Bob(PoolLoc) zorder 50
                            elif Girls[0] == EmmaX:
                                    show Emma_Sprite at Pool_Bob(PoolLoc) zorder 50
                            elif Girls[0] == LauraX:
                                    show Laura_Sprite at Pool_Bob(PoolLoc) zorder 50
                            elif Girls[0] == JeanX:
                                    show Jean_Sprite at Pool_Bob(PoolLoc) zorder 50
                            elif Girls[0] == StormX:
                                    show Storm_Sprite at Pool_Bob(PoolLoc) zorder 50
                            elif Girls[0] == JubesX:
                                    show Jubes_Sprite at Pool_Bob(PoolLoc) zorder 50
                $ Girls.remove(Girls[0])
        show FullPool zorder 60        #should put masked pool above girls #175?
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
