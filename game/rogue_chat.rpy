label Rogue_Relationship: #rkelj
    while True:
        menu:
            ch_r "What did you want to ask me about?"
            "Do you want to be my girlfriend?" if RogueX not in Player.Harem and "ex" not in RogueX.Traits:
                    $ RogueX.daily_history.append("relationship")
                    if "asked boyfriend" in RogueX.daily_history and "angry" in RogueX.daily_history:
                            $ RogueX.change_face("angry", 1)
                            ch_r "Seriously, stop bugging me."
                            return
                    elif "asked boyfriend" in RogueX.daily_history:
                            $ RogueX.change_face("angry", 1)
                            ch_r "You already asked about that, the answer's still no."
                            return
                    elif RogueX.Break[0]:
                            $ RogueX.change_face("angry", 1)
                            ch_r "I already told you, not while you're with her."
                            if Player.Harem:
                                    $ RogueX.daily_history.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "I'm not anymore."

                    $ RogueX.daily_history.append("asked boyfriend")

                    if Player.Harem and "RogueYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_r "That wouldn't be fair to the others, [RogueX.Petname]."
                        else:
                            ch_r "That wouldn't be fair to [Player.Harem[0].name], [RogueX.Petname]."
                        return

                    if RogueX.Event[5]:
                            $ RogueX.change_face("bemused", 1)
                            ch_r "I mean, I asked you about this before. . ."
                    else:
                            $ RogueX.change_face("surprised", 2)
                            ch_r "Wow, this is unexpected, [RogueX.Petname]. . ."
                            $ RogueX.change_face("smile", 1)

                    call Rogue_OtherWoman

                    if RogueX.love >= 800:
                            $ RogueX.change_face("surprised", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.change_stat("love", 200, 40)
                            ch_r "I'd love to!"
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")
                            if "RogueYes" in Player.Traits:
                                    $ Player.Traits.remove("RogueYes")
                            $ Player.Harem.append(RogueX)
                            call Harem_Initiation
                            "[RogueX.name] leaps in and kisses you deeply."
                            $ RogueX.change_face("kiss", 1)
                            $ RogueX.action_counter["kiss"] += 1
                    elif RogueX.obedience >= 500:
                            $ RogueX.change_face("perplexed")
                            ch_r "I'm not sure I'd call what we have \"dating.\""
                    elif RogueX.inhibition >= 500:
                            $ RogueX.change_face("smile")
                            ch_r "I don't really want to be tied down like that."
                    else:
                            $ RogueX.change_face("perplexed", 1)
                            ch_r "I don't really feel that way about you right now, [RogueX.Petname]."

            "Do you want to get back together?" if "ex" in RogueX.Traits:
                    $ RogueX.daily_history.append("relationship")
                    if "asked boyfriend" in RogueX.daily_history and "angry" in RogueX.daily_history:
                            $ RogueX.change_face("angry", 1)
                            ch_r "Seriously, stop bugging me."
                            return
                    elif "asked boyfriend" in RogueX.daily_history:
                            $ RogueX.change_face("angry", 1)
                            ch_r "You already asked about that, the answer's still no."
                            return

                    $ RogueX.daily_history.append("asked boyfriend")

                    if Player.Harem and "RogueYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_r "That wouldn't be fair to the others, [RogueX.Petname]."
                            else:
                                ch_r "That wouldn't be fair to [Player.Harem[0].name], [RogueX.Petname]."
                            return

                    $ counter = 0
                    call Rogue_OtherWoman

                    if RogueX.love >= 800:
                            $ RogueX.change_face("surprised", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.change_stat("love", 90, 5)
                            ch_r "If you're in, I'm in!"
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")
                            $ RogueX.Traits.remove("ex")
                            if "RogueYes" in Player.Traits:
                                    $ Player.Traits.remove("RogueYes")
                            $ Player.Harem.append(RogueX)
                            call Harem_Initiation
                            "[RogueX.name] leaps in and kisses you deeply."
                            $ RogueX.change_face("kiss", 1)
                            $ RogueX.action_counter["kiss"] += 1
                    elif RogueX.love >= 600 and Approvalcheck(RogueX, 1500):
                            $ RogueX.change_face("smile", 1)
                            $ RogueX.Mouth = "grimace"
                            $ RogueX.change_stat("love", 90, 5)
                            ch_r "We can give this another try."
                            if "boyfriend" not in RogueX.Petnames:
                                        $ RogueX.Petnames.append("boyfriend")
                            $ RogueX.Traits.remove("ex")
                            if "RogueYes" in Player.Traits:
                                    $ Player.Traits.remove("RogueYes")
                            $ Player.Harem.append(RogueX)
                            call Harem_Initiation
                            "[RogueX.name] gives you a quick kiss."
                            $ RogueX.change_face("kiss", 1)
                            $ RogueX.action_counter["kiss"] += 1
                    elif RogueX.obedience >= 500:
                            $ RogueX.change_face("sad")
                            ch_r "Whatever we had, whatever we have right now, that's not it."
                    elif RogueX.inhibition >= 500:
                            $ RogueX.change_face("perplexed")
                            ch_r "We tried that, it didn't work out."
                    else:
                            $ RogueX.change_face("perplexed", 1)
                            ch_r "I'm not ready for more heartbreak, [RogueX.Petname]."

                    # End Back Together

            "I wanted to ask about [[another girl]" if RogueX in Player.Harem:
                        call AskDateOther

            "I think we should break up." if RogueX in Player.Harem:
                        if "breakup talk" in RogueX.recent_history:
                                ch_r "We were {i}just{/i} over this, not even funny."
                        elif "breakup talk" in RogueX.daily_history:
                                ch_r "Tired of me again that quick?"
                                ch_r "We're not having this talk today, [RogueX.Petname]."
                        else:
                                call Breakup(RogueX)

            "About that talk we had before. . .":
                menu:
                    "You weren't a virgin?" if RogueX.action_counter["sex"] and not RogueX.Chat[0]:
                        call Rogue_Not_Virgin

                    "You said you wanted me to be your Master?" if RogueX.Event[8] and "master" not in RogueX.Petnames:
                        menu:
                            ch_r "Yes?"
                            "I'm ok with that now.":
                                        if Approvalcheck(RogueX, 800, "O"):
                                            $ RogueX.change_face("sexy", 1)
                                            ch_r "I hope to serve well, Master."
                                            $ RogueX.change_stat("obedience", 200, 100)
                                            $ RogueX.Petnames.append("master")
                                            $ RogueX.Event[8] = 2
                                        else:
                                            ch_r "Well, I'm not really interested in that sort of thing anymore."
                                            ch_r "I mean, maybe later."
                            "Never mind.":
                                        $ RogueX.change_face("sad")
                                        ch_r "Oh."
                                        $ RogueX.change_stat("obedience", 200, -5)
                                        $ RogueX.change_stat("love", 90, -5)
                    "Never Mind":
                        pass
            "Never Mind":
                return
        return

label Rogue_OtherWoman(counter = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ counter = int((RogueX.GirlLikecheck(Player.Harem[0]) - 500)/2)

    $ RogueX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_r "But you're with [Player.Harem[0].name] right now, and a whole mess'a other girls!"
    else:
        ch_r "But you're with [Player.Harem[0].name]!"
    menu:
        extend ""
        "She said I can be with you too." if "RogueYes" in Player.Traits:
                if Approvalcheck(RogueX, 1800, Bonus = counter):
                    $ RogueX.change_face("smile", 1)
                    if RogueX.love >= RogueX.obedience:
                            ch_r "I s'pose I can learn ta share."
                    elif RogueX.obedience >= RogueX.inhibition:
                            ch_r "Well I won't be the one to get in the way a this."
                    else:
                            ch_r "Ok, sure."
                else:
                    $ RogueX.change_face("angry", 1)
                    ch_r "Well that harlot!"
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "I could ask if she'd be ok with me dating you both." if "RogueYes" not in Player.Traits:
                if Approvalcheck(RogueX, 1800, Bonus = counter):
                        $ RogueX.change_face("smile", 1)
                        if RogueX.love >= RogueX.obedience:
                            ch_r "I s'pose I can learn ta share."
                        elif RogueX.obedience >= RogueX.inhibition:
                            ch_r "Well I won't be the one to get in the way a this."
                        else:
                            ch_r "Ok, sure."
                        ch_r "You go ask her if she's inta that, then get back to me tomorrow."
                else:
                        $ RogueX.change_face("angry", 1)
                        ch_r "Well that harlot!"
                $ renpy.pop_call()

        "What she doesn't know won't hurt her.":
                if not Approvalcheck(RogueX, 1800, Bonus = -counter): #checks if She likes you more than the other girl
                        $ RogueX.change_face("angry", 1)
                        if not Approvalcheck(RogueX, 1800):
                                ch_r "Well now I don't wantcha."
                        else:
                                ch_r "I ain't in a sharin mood."
                        $ renpy.pop_call()
                else:
                        $ RogueX.change_face("smile", 1)
                        if RogueX.love >= RogueX.obedience:
                                ch_r "I s'pose somethin could be arranged. . ."
                        elif RogueX.obedience >= RogueX.inhibition:
                                ch_r "If you insist."
                        else:
                                ch_r "Don't see why not."
                        $ RogueX.AddWord(1,0,0,"downlow")

        "I can break it off with her.":
                    $ RogueX.change_face("sad")
                    ch_r "Well then talk to me after you have."
                    $ renpy.pop_call()

        "You're right, I was dumb to ask.":
                    $ RogueX.change_face("sad")
                    ch_r "Yeah. . ."
                    $ renpy.pop_call()

    return

label Rogue_About(check=0): #rkeljsv
    if check not in all_Girls:
            ch_r "Who?"
            return
    ch_r "What do I think about her? Well. . ."
    if check == KittyX:
            if "poly Kitty" in RogueX.Traits:
                ch_r "I think you know the answer to that one. . ."
            elif RogueX.LikeKitty >= 900:
                ch_r "I think she's really . . . hot?"
            elif RogueX.LikeKitty >= 800:
                ch_r "I feel really close to her, best friends, maybe more."
            elif RogueX.LikeKitty >= 700:
                ch_r "She's one of my best friends."
            elif RogueX.LikeKitty >= 600:
                ch_r "We're good friends."
            elif RogueX.LikeKitty >= 500:
                ch_r "I don't know, she's ok."
            elif RogueX.LikeKitty >= 400:
                ch_r "We're. . . kind of off right now."
            elif RogueX.LikeKitty >= 300:
                ch_r "I don't want to talk about it."
            else:
                ch_r "That ho-bag skank?"
    elif check == EmmaX:
            if "poly Emma" in RogueX.Traits:
                ch_r "Well, I sure don't kick her out of bed. . ."
            elif RogueX.LikeEmma >= 900:
                ch_r "I'm kinda hot for teacher."
            elif RogueX.LikeEmma >= 800:
                ch_r "She's pretty amaz'in, right? Sometimes I wonder. . ."
            elif RogueX.LikeEmma >= 700:
                ch_r "We hang out sometimes after class, she's fun to talk to."
            elif RogueX.LikeEmma >= 600:
                ch_r "She's a really great teach, I love her lectures."
            elif RogueX.LikeEmma >= 500:
                ch_r "I don't know, she's ok."
            elif RogueX.LikeEmma >= 400:
                ch_r "I don't really like the way she looks at you in class."
            elif RogueX.LikeEmma >= 300:
                ch_r "I hate her class."
            else:
                ch_r "Ugh, that WITCH!"
    elif check == LauraX:
            if "poly Laura" in RogueX.Traits:
                ch_r "We hook up from time to time. . ."
            elif RogueX.LikeLaura >= 900:
                ch_r "She's got an animal magnetism to her. . ."
            elif RogueX.LikeLaura >= 800:
                ch_r "We really seem to get along. . ."
            elif RogueX.LikeLaura >= 700:
                ch_r "She's a good friend."
            elif RogueX.LikeLaura >= 600:
                ch_r "She's a good teammate."
            elif RogueX.LikeLaura >= 500:
                ch_r "I don't know, she's ok in a fight."
            elif RogueX.LikeLaura >= 400:
                ch_r "We're. . . not in a good place."
            elif RogueX.LikeLaura >= 300:
                ch_r "I don't want to talk about it."
            else:
                ch_r "That ho-bag skank?"
    elif check == JeanX:
            if "poly Jean" in RogueX.Traits:
                ch_r "We hook up from time to time. . ."
            elif RogueX.LikeJean >= 900:
                ch_r "She's got a real charm to her. . ."
            elif RogueX.LikeJean >= 800:
                ch_r "We really seem to get along. . ."
            elif RogueX.LikeJean >= 700:
                ch_r "She's a. . . friend."
            elif RogueX.LikeJean >= 600:
                ch_r "She's a good teammate."
            elif RogueX.LikeJean >= 500:
                ch_r "I don't know, she's ok."
            elif RogueX.LikeJean >= 400:
                ch_r "We're. . . not in a good place."
            elif RogueX.LikeJean >= 300:
                ch_r "I'm tired a' her nonsense."
            else:
                ch_r "That ho-bag witch?!"
    elif check == StormX:
            if "poly Storm" in RogueX.Traits:
                ch_r "Well, she's sure nice to cuddle up to. . ."
            elif RogueX.LikeStorm >= 900:
                ch_r "I'm kinda into her."
            elif RogueX.LikeStorm >= 800:
                ch_r "She's pretty great, right? I kinda wonder. . ."
            elif RogueX.LikeStorm >= 700:
                ch_r "We talk sometimes after class, she's a good listener."
            elif RogueX.LikeStorm >= 600:
                ch_r "She's a really great teach, I love her lectures."
            elif RogueX.LikeStorm >= 500:
                ch_r "I don't know, she's ok."
            elif RogueX.LikeStorm >= 400:
                ch_r "I don't really like the way she looks at you in class."
            elif RogueX.LikeStorm >= 300:
                ch_r "I hate her class."
            else:
                ch_r "Ugh, that WITCH!"
    elif check == JubesX:
            if "poly Jubes" in RogueX.Traits:
                ch_r "I think you know the answer to that one. . ."
            elif RogueX.LikeJubes >= 900:
                ch_r "I think she's really . . . hot?"
            elif RogueX.LikeJubes >= 800:
                ch_r "I think we work really great together. . ."
            elif RogueX.LikeJubes >= 700:
                ch_r "She's a really good friend."
            elif RogueX.LikeJubes >= 600:
                ch_r "We're friends."
            elif RogueX.LikeJubes >= 500:
                ch_r "I don't know, she's ok."
            elif RogueX.LikeJubes >= 400:
                ch_r "We're. . . kind of off right now."
            elif RogueX.LikeJubes >= 300:
                ch_r "I don't want to talk about it."
            else:
                ch_r "That ho-bag skank?"
    return

label Rogue_Monogamy:
        #called from Rogue_Settings to ask her not to hook up wiht other girls
        menu:
            "Could you not hook up with other girls?" if "mono" not in RogueX.Traits:
                    if RogueX.Thirst >= 60 and not Approvalcheck(RogueX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.change_face("sly",1)
                            if "mono" not in RogueX.daily_history:
                                    $ RogueX.change_stat("obedience", 90, -2)
                            ch_r "I might consider that, but you don't exactly make yourself available. . ."
                            return
                    elif Approvalcheck(RogueX, 1200, "LO", TabM=0) and RogueX.love >= RogueX.obedience:
                            #she cares
                            $ RogueX.change_face("sly",1)
                            if "mono" not in RogueX.daily_history:
                                    $ RogueX.change_stat("love", 90, 1)
                            ch_r "Aw, would that make you jealous?"
                            ch_r "I suppose I could restain myself. . ."
                    elif Approvalcheck(RogueX, 700, "O", TabM=0):
                            #she is obedient
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "If that's what you really want. . ."
                    else:
                            #she doesn't care
                            $ RogueX.change_face("sly",1,Brows="confused")
                            ch_r "Who I \"hook up\" with is my own damned business."
                            return
                    if "mono" not in RogueX.daily_history:
                            $ RogueX.change_stat("obedience", 90, 3)
                    $ RogueX.AddWord(1,0,"mono","mono") #Daily
            "Don't hook up with other girls." if "mono" not in RogueX.Traits:
                    if Approvalcheck(RogueX, 900, "O", TabM=0):
                            #she is obedient
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "Ok."
                    elif RogueX.Thirst >= 60 and not Approvalcheck(RogueX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.change_face("sly",1)
                            if "mono" not in RogueX.daily_history:
                                    $ RogueX.change_stat("obedience", 90, -2)
                            ch_r "I might consider that, but you don't exactly make yourself available. . ."
                            return
                    elif Approvalcheck(RogueX, 550, "O", TabM=0):
                            #she is obedient
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "If that's what you really want. . ."
                    elif Approvalcheck(RogueX, 1400, "LO", TabM=0):
                            #she cares
                            $ RogueX.change_face("sly",1)
                            ch_r "Is that any way to ask a girl?"
                            ch_r "Still, I'll do it for you. . ."
                    else:
                            #she doesn't care
                            $ RogueX.change_face("sly",1,Brows="confused")
                            ch_r "Who I \"hook up\" with is my own damned business."
                            return
                    if "mono" not in RogueX.daily_history:
                            $ RogueX.change_stat("obedience", 90, 3)
                    $ RogueX.AddWord(1,0,"mono","mono") #Daily
            "It's ok if you hook up with other girls." if "mono" in RogueX.Traits:
                    if Approvalcheck(RogueX, 700, "O", TabM=0):
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "As you wish."
                    elif Approvalcheck(RogueX, 800, "L", TabM=0):
                            $ RogueX.change_face("sly",1)
                            ch_r "I hope you don't give me any reasons to want to. . ."
                    else:
                            $ RogueX.change_face("sly",1,Brows="confused")
                            if "mono" not in RogueX.daily_history:
                                    $ RogueX.change_stat("love", 90, -2)
                            ch_r "Oh? Well, glad I got your permission there."
                    if "mono" not in RogueX.daily_history:
                            $ RogueX.change_stat("obedience", 90, 3)
                    if "mono" in RogueX.Traits:
                            $ RogueX.Traits.remove("mono")
                    $ RogueX.AddWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return

label Rogue_Jumped:
        #called from Rogue_Settings to ask her not to jump you
        ch_p "Hey, Remember that time you threw yourself at me?"
        $ RogueX.change_face("sly",1,Brows="confused")
        menu:
            ch_r "Yeah?"
            "Could you maybe just ask instead?" if "chill" not in RogueX.Traits:
                    if RogueX.Thirst >= 60 and not Approvalcheck(RogueX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ RogueX.change_face("sly",1)
                            if "chill" not in RogueX.daily_history:
                                    $ RogueX.change_stat("obedience", 90, -2)
                            ch_r "Maybe don't keep me waiting then. . ."
                            return
                    elif Approvalcheck(RogueX, 1000, "LO", TabM=0) and RogueX.love >= RogueX.obedience:
                            #she cares
                            $ RogueX.change_face("sly",1)
                            if "chill" not in RogueX.daily_history:
                                    $ RogueX.change_stat("love", 90, 1)
                            ch_r "Sorry, [RogueX.Petname], I just got a little lonely. . ."
                            ch_r "I'll be good. . ."
                    elif Approvalcheck(RogueX, 500, "O", TabM=0):
                            #she is obedient
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "If that's what you really want. . ."
                    else:
                            #she doesn't care
                            $ RogueX.change_face("sly",1,Brows="confused")
                            ch_r "I can't make any promises."
                            return
                    if "chill" not in RogueX.daily_history:
                            $ RogueX.change_stat("obedience", 90, 3)
                    $ RogueX.AddWord(1,0,"chill","chill") #Daily
            "Don't bother me like that." if "chill" not in RogueX.Traits:
                    if Approvalcheck(RogueX, 900, "O", TabM=0):
                            #she is obedient
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "Ok."
                    elif RogueX.Thirst >= 60 and not Approvalcheck(RogueX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ RogueX.change_face("sly",1)
                            if "chill" not in RogueX.daily_history:
                                    $ RogueX.change_stat("obedience", 90, -2)
                            ch_r "Maybe don't keep me waiting then. . ."
                            return
                    elif Approvalcheck(RogueX, 450, "O", TabM=0):
                            #she is obedient
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "If that's what you really want. . ."
                    elif Approvalcheck(RogueX, 500, "LO", TabM=0) and not Approvalcheck(RogueX, 500, "I", TabM=0):
                            #she cares
                            $ RogueX.change_face("sly",1)
                            ch_r "You might want to watch your mouth."
                            ch_r "Still, I'll try to keep to myself. . ."
                    else:
                            #she doesn't care
                            $ RogueX.change_face("sly",1,Brows="confused")
                            ch_r "No promises."
                            return
                    if "chill" not in RogueX.daily_history:
                            $ RogueX.change_stat("obedience", 90, 3)
                    $ RogueX.AddWord(1,0,"chill","chill") #Daily
            "Knock yourself out.":
                    if Approvalcheck(RogueX, 800, "L", TabM=0):
                            $ RogueX.change_face("sly",1)
                            ch_r "Will do. . ."
                    elif Approvalcheck(RogueX, 700, "O", TabM=0):
                            $ RogueX.change_face("sly",1,Eyes="side")
                            ch_r "Yes sir."
                    else:
                            $ RogueX.change_face("sly",1,Brows="confused")
                            if "chill" not in RogueX.daily_history:
                                    $ RogueX.change_stat("love", 90, -2)
                            ch_r "Maybe. If I've got nothing better to do."
                    if "chill" not in RogueX.daily_history:
                            $ RogueX.change_stat("obedience", 90, 3)
                    if "chill" in RogueX.Traits:
                            $ RogueX.Traits.remove("chill")
                    $ RogueX.AddWord(1,0,"chill") #Daily
            "Um, never mind.":
                pass
        return

label Rogue_Not_Virgin:
    menu:
        "I noticed that when we had sex, you didn't seem to be a virgin."
        "Wasn't I your first time?":
            $ RogueX.change_face("bemused", 1)
            $ RogueX.change_stat("love", 60, 5)
            $ RogueX.change_stat("obedience", 20, 15)
            ch_r "Oh, no! You definitely were, it's just. . . you know,"
            ch_r "I lead a pretty active lifestyle, so I lost that physical barrier years ago."
        "So you get around?":
            $ RogueX.change_face("sexy", 1)
            $ RogueX.Brows = "angry"
            $ RogueX.change_stat("obedience", 30, 15)
            $ RogueX.change_stat("obedience", 60, 5)
            $ RogueX.change_stat("inhibition", 30, 15)
            $ RogueX.change_stat("inhibition", 60, 5)
            ch_r "Jerk, not like that. I tore it years ago in combat training."
        "Are you a slut?":
            $ RogueX.change_face("angry", 1)
            $ RogueX.change_stat("love", 30, -20, 1)
            $ RogueX.change_stat("love", 60, -40, 1)
            $ RogueX.change_stat("obedience", 30, 30)
            $ RogueX.change_stat("obedience", 60, 20)
            ch_r "If you'd like to find that out, you might want to rethink how you talk to me, [RogueX.Petname]."
    $ RogueX.Chat[0] = 1
    return

label Rogue_Hungry:
    if RogueX.Chat[3]:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    elif RogueX.Chat[2]:
        ch_r "You know, I've really come to enjoy the taste of your, serum. It's like my favorite drink!"
    else:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    $ RogueX.Traits.append("hungry")
    return

label Rogue_SexChat:
    $ line = "Yeah, what did you want to talk about?" if not line else line
    while True:
            menu:
                ch_r "[line]"
                "My favorite thing to do is. . .":
                    if "setfav" in RogueX.daily_history:
                        ch_r "Yeah, I know. You just told me earlier."
                    else:
                        menu:
                            "Sex.":
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "sex":
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "Yeah, I know that. . ."
                                        elif RogueX.Favorite == "sex":
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 10)
                                            ch_r "Oooh, I love a good pipe cleaning too. . ."
                                        elif RogueX.action_counter["sex"] >= 5:
                                            ch_r "Can't say as I mind a good roll in the hay."
                                        elif not RogueX.action_counter["sex"]:
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} are y'all having sex {i}with?{/i}"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "Heh, [RogueX.Petname], flithy mouth on you. . ."
                                        $ RogueX.PlayerFav = "sex"

                            "Anal.":
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "anal":
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "So I hear. . ."
                                        elif RogueX.Favorite == "anal":
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 10)
                                            ch_r "I can't say as I mind that. . ."
                                        elif RogueX.action_counter["anal"]  >= 10:
                                            ch_r "It's not a bad way to spend some time. . ."
                                        elif not RogueX.action_counter["anal"] :
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} are y'all fucking {i}with?{/i}"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "Heh, heh, I . . . I don't {i}mind{/i} it. . ."
                                        $ RogueX.PlayerFav = "anal"

                            "Blowjobs.":
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "blowjob":
                                            $ RogueX.change_stat("lust", 80, 3)
                                            ch_r "I'm not surprised. . ."
                                        elif RogueX.Favorite == "blowjob":
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "I guess I have developed a real taste for you. . ."
                                        elif RogueX.Blow >= 10:
                                            ch_r "I'm getting to enjoy it too . . ."
                                        elif not RogueX.Blow:
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} is sucking you off?"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "I'm. . . getting used to the taste. . ."
                                        $ RogueX.PlayerFav = "blowjob"

                            "Titjobs.":
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "titjob":
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "So I hear. . ."
                                        elif RogueX.Favorite == "titjob":
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 7)
                                            ch_r "I really enjoy it too. . ."
                                        elif RogueX.Tit >= 10:
                                            ch_r "It's certainly an interesting experience . . ."
                                        elif not RogueX.Tit:
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} is tit fucking you?"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "I can't say as I blame you. . ."
                                        $ RogueX.PlayerFav = "titjob"

                            "Footjobs.":
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "footjob":
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "Yeah, you've said that before. . ."
                                        elif RogueX.Favorite == "footjob":
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 7)
                                            ch_r "I do enjoy that sensation. . ."
                                        elif RogueX.Foot >= 10:
                                            ch_r "It is pretty nice to touch someone like that . . ."
                                        elif not RogueX.Foot:
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} is jerking you off?"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "I do like the sensation. . ."
                                        $ RogueX.PlayerFav = "footjob"

                            "Handjobs.":
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "handjob":
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "Yeah, you've said that before. . ."
                                        elif RogueX.Favorite == "handjob":
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 7)
                                            ch_r "I love how you feel in my hand. . ."
                                        elif RogueX.Hand >= 10:
                                            ch_r "It is pretty nice to touch someone like that . . ."
                                        elif not RogueX.Hand:
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} is jerking you off?"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "I do like the sensation. . ."
                                        $ RogueX.PlayerFav = "handjob"

                            "Feeling you up.":
                                        $ counter = RogueX.action_counter["fondle_breasts"] + RogueX.action_counter["fondle_thighs"] + RogueX.SuckB + RogueX.Hotdog
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "fondle":
                                            $ RogueX.change_stat("lust", 80, 3)
                                            ch_r "Yeah, I think we've established that. . ."
                                        elif RogueX.Favorite in ("hotdog","suck_breasts","fondle_breasts","fondle_thighs"):
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "I love how you touch me. . ."
                                        elif counter >= 10:
                                            ch_r "It's nice to have someone who can really touch me . . ."
                                        elif not counter:
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} are you feeling up?"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "I do like how that feels. . ."
                                        $ RogueX.PlayerFav = "fondle"
                                        $ counter = 0

                            "Kissing you.":
                                        $ RogueX.change_face("sly")
                                        if RogueX.PlayerFav == "kiss":
                                            $ RogueX.change_stat("love", 90, 3)
                                            ch_r "I've heard it before, but don't mind hearing it again. . ."
                                        elif RogueX.Favorite == "kiss":
                                            $ RogueX.change_stat("love", 90, 5)
                                            $ RogueX.change_stat("lust", 80, 5)
                                            ch_r "I can't get over your lips either. . ."
                                        elif RogueX.action_counter["kiss"] >= 10:
                                            ch_r "I love kissing you too . . ."
                                        elif not RogueX.action_counter["kiss"]:
                                            $ RogueX.change_face("perplexed")
                                            ch_r "Who {i}exactly{/i} are you smooch'in?"
                                        else:
                                            $ RogueX.change_face("bemused")
                                            ch_r "It's nice being able to kiss someone without hurting them. . ."
                                        $ RogueX.PlayerFav = "kiss"

                        $ RogueX.daily_history.append("setfav")

                "What's your favorite thing to do?":
                                if not Approvalcheck(RogueX, 800):
                                        $ RogueX.change_face("perplexed")
                                        ch_r "I don't think that's any of your business. . ."
                                else:
                                        if RogueX.SEXP >= 50:
                                            $ RogueX.change_face("sly")
                                            ch_r "If you can't tell. . ."
                                        else:
                                            $ RogueX.change_face("bemused")
                                            $ RogueX.Eyes = "side"
                                            ch_r "I don't know, I guess maybe. . ."


                                        if not RogueX.Favorite or RogueX.Favorite == "kiss":
                                            ch_r "I guess I love it when we kiss. . ."
                                        elif RogueX.Favorite == "anal":
                                            if RogueX.action_counter["anal"]  >= 10:
                                                ch_r "I like when you fuck my ass."
                                            else:
                                                ch_r "I like when you stick it in my. . . butt."
                                        elif RogueX.Favorite == "eat_ass":
                                                ch_r "I like when you lick my. . . asshole."
                                        elif RogueX.Favorite == "finger_ass":
                                                ch_r "I like when you . . . finger my asshole."
                                        elif RogueX.Favorite == "sex":
                                                ch_r "I like when you fuck me hard."
                                        elif RogueX.Favorite == "eat_pussy":
                                                ch_r "I like when you lick my pussy."
                                        elif RogueX.Favorite == "fondle_pussy":
                                                ch_r "I like when you fingerblast me."
                                        elif RogueX.Favorite == "blowjob":
                                                ch_r "I kind of like to suck your cock."
                                        elif RogueX.Favorite == "titjob":
                                                ch_r "I like to work your cock with my tits."
                                        elif RogueX.Favorite == "handjob":
                                                ch_r "I like the feel of your cock in my hand."
                                        elif RogueX.Favorite == "footjob":
                                                ch_r "I kinda like to use my feet."
                                        elif RogueX.Favorite == "hotdog":
                                                ch_r "I like it when you grind against me."
                                        elif RogueX.Favorite == "suck_breasts":
                                                ch_r "I like it when you suck on my tits."
                                        elif RogueX.Favorite == "fondle_breasts":
                                                ch_r "I like it when you feel up my tits."
                                        elif RogueX.Favorite == "fondle_thighs":
                                                ch_r "I like it when you massage my thighs."
                                        else:
                                                ch_r "I don't really know. . ."

                                # End Rogue's favorite things.

                "Don't talk as much during sex." if "vocal" in RogueX.Traits:
                        if "setvocal" in RogueX.daily_history:
                            $ RogueX.change_face("perplexed")
                            ch_r "We've been over this already."
                        else:
                            if Approvalcheck(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                                $ RogueX.change_face("bemused")
                                $ RogueX.change_stat("obedience", 90, 1)
                                ch_r "Heh, ok, if that's what you want. . ."
                                $ RogueX.Traits.remove("vocal")
                            elif Approvalcheck(RogueX, 700, "O"):
                                $ RogueX.change_face("sadside")
                                $ RogueX.change_stat("obedience", 90, 1)
                                ch_r "If that's what you want, [RogueX.Petname]."
                                $ RogueX.Traits.remove("vocal")
                            elif Approvalcheck(RogueX, 600):
                                $ RogueX.change_face("sly")
                                $ RogueX.change_stat("love", 90, -3)
                                $ RogueX.change_stat("obedience", 50, -1)
                                $ RogueX.change_stat("inhibition", 90, 5)
                                ch_r "I'll say what I want, and you'll like it, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry")
                                $ RogueX.change_stat("love", 90, -5)
                                $ RogueX.change_stat("obedience", 60, -3)
                                $ RogueX.change_stat("inhibition", 90, 10)
                                ch_r "Fuck you, I'll talk as much as I want."

                            $ RogueX.daily_history.append("setvocal")
                "Talk dirty to me during sex." if "vocal" not in RogueX.Traits:
                        if "setvocal" in RogueX.daily_history:
                            $ RogueX.change_face("perplexed")
                            ch_r "We've been over this already."
                        else:
                            if Approvalcheck(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                                $ RogueX.change_face("sly")
                                $ RogueX.change_stat("obedience", 90, 2)
                                ch_r "Heh, ok, if that's what you want. . ."
                                $ RogueX.Traits.append("vocal")
                            elif Approvalcheck(RogueX, 700, "O"):
                                $ RogueX.change_face("sadside")
                                $ RogueX.change_stat("obedience", 90, 2)
                                ch_r "If that's what you want, [RogueX.Petname]."
                                $ RogueX.Traits.append("vocal")
                            elif Approvalcheck(RogueX, 600):
                                $ RogueX.change_face("sly")
                                $ RogueX.change_stat("obedience", 90, 3)
                                ch_r "I can give it a shot, [RogueX.Petname]."
                                $ RogueX.Traits.append("vocal")
                            else:
                                $ RogueX.change_face("angry")
                                $ RogueX.change_stat("inhibition", 90, 5)
                                ch_r "I'll say what I want, when I want."

                            $ RogueX.daily_history.append("setvocal")
                        # End Rogue Dirty Talk

                "Don't do your own thing as much during sex." if "passive" not in RogueX.Traits:
                        if "initiative" in RogueX.daily_history:
                                $ RogueX.change_face("perplexed")
                                ch_r "We've been over this already."
                        else:
                            if Approvalcheck(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                                $ RogueX.change_face("bemused")
                                $ RogueX.change_stat("obedience", 90, 1)
                                ch_r "Heh, ok, lead the way. . ."
                                $ RogueX.Traits.append("passive")
                            elif Approvalcheck(RogueX, 700, "O"):
                                $ RogueX.change_face("sadside")
                                $ RogueX.change_stat("obedience", 90, 1)
                                ch_r "I'll restrain myself then, [RogueX.Petname]."
                                $ RogueX.Traits.append("passive")
                            elif Approvalcheck(RogueX, 600):
                                $ RogueX.change_face("sly")
                                $ RogueX.change_stat("love", 90, -3)
                                $ RogueX.change_stat("obedience", 50, -1)
                                $ RogueX.change_stat("inhibition", 90, 5)
                                ch_r "You know you don't want that, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry")
                                $ RogueX.change_stat("love", 90, -5)
                                $ RogueX.change_stat("obedience", 60, -3)
                                $ RogueX.change_stat("inhibition", 90, 10)
                                ch_r "I'll do what I want, prick."

                            $ RogueX.daily_history.append("initiative")
                "Take more initiative during sex." if "passive" in RogueX.Traits:
                        if "initiative" in RogueX.daily_history:
                                $ RogueX.change_face("perplexed")
                                ch_r "We've been over this already."
                        else:
                            if Approvalcheck(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                                $ RogueX.change_face("bemused")
                                $ RogueX.change_stat("obedience", 90, 1)
                                ch_r "Heh, I think I can handle that. . ."
                                $ RogueX.Traits.remove("passive")
                            elif Approvalcheck(RogueX, 700, "O"):
                                $ RogueX.change_face("sadside")
                                $ RogueX.change_stat("obedience", 90, 1)
                                ch_r "I can do that, [RogueX.Petname]."
                                $ RogueX.Traits.remove("passive")
                            elif Approvalcheck(RogueX, 600):
                                $ RogueX.change_face("sly")
                                $ RogueX.change_stat("obedience", 90, 3)
                                ch_r "I can certainly try, [RogueX.Petname]."
                                $ RogueX.Traits.remove("passive")
                            else:
                                $ RogueX.change_face("angry")
                                $ RogueX.change_stat("inhibition", 90, 5)
                                ch_r "If I want to, I will, but not because you say so."

                            $ RogueX.daily_history.append("initiative")

                "About getting Jumped" if "jumped" in RogueX.History:
                        call Rogue_Jumped
                "About when you masturbate":
                        call NoFap(RogueX)

                "Never Mind" if line == "Yeah, what did you want to talk about?":
                        return
                "That's all." if line != "Yeah, what did you want to talk about?":
                        return
            if line == "Yeah, what did you want to talk about?":
                $ line = "Anything else?"
    return

label Rogue_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        if RogueX not in Digits:
            if Approvalcheck(RogueX, 500, "L") or Approvalcheck(RogueX, 250, "I"):
                    ch_r "You know, I never got around to giving you my number, here you go."
                    $ Digits.append(RogueX)
                    return
            elif Approvalcheck(RogueX, 250, "O"):
                    ch_r "You know, you should probably have my number, here you go."
                    $ Digits.append(RogueX)
                    return
        if "hungry" not in RogueX.Traits and (RogueX.event_counter["swallowed"] + RogueX.Chat[2]) >= 10 and RogueX.location == bg_current:  #She's swallowed a lot
                    call Rogue_Hungry
                    return
        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not Taboo or Approvalcheck(RogueX, 800, "I")):
                    if RogueX.location == bg_current and RogueX.Thirst >= 30 and "refused" not in RogueX.daily_history and "quicksex" not in RogueX.daily_history:
                            $ RogueX.change_face("sly",1)
                            ch_r "Hey, do you want to get a little frisky?"
                            call Quick_Sex(RogueX)
                            return

        #adds options based on accomplishments
        if Approvalcheck(RogueX, 1200) and bg_current == RogueX.location and bg_current != "bg_restaurant":
            $ Options.append("dance")
        if Approvalcheck(RogueX, 800, "L") and "nametag chat" not in RogueX.daily_history:
            $ Options.append("close")
        if RogueX.Blow >= 2:
            $ Options.append("blowjob")
        if "steal" in RogueX.Traits:
            $ Options.append("steal")
        if PunishmentX and "caught chat" not in RogueX.daily_history:
            $ Options.append("caught")
        if RogueX.Event[0] and "key chat" not in RogueX.daily_history:
            $ Options.append("key")
        if "lover" in RogueX.Petnames and Approvalcheck(RogueX, 900, "L"): # luvy dovey
            $ Options.append("luv")

        if Player.cologne and "cologne_chat" not in RogueX.daily_history:
            $ Options.append(Player.cologne)

        if not RogueX.Chat[0] and RogueX.action_counter["sex"]:
            $ Options.append("virgin")

        if "seenpeen" in RogueX.History:
            $ Options.append("seenpeen")
        if "topless" in RogueX.History:
            $ Options.append("topless")
        if "bottomless" in RogueX.History:
            $ Options.append("bottomless")

        if "lover" in RogueX.Petnames and "Anna" not in RogueX.names:
            #if you've done the love scene, but never got Rogue's other name, second chance
            $ Options.append("annamarie")

        if (bg_current == "bg_rogue" or bg_current == "bg_player") and "nametag chat" not in RogueX.daily_history:
            if "lover" not in RogueX.Petnames and Approvalcheck(RogueX, 900, "L"): # RogueX.Event[6]
                $ Options.append("lover?")
            elif "sir" not in RogueX.Petnames and Approvalcheck(RogueX, 500, "O"): # RogueX.Event[7]
                $ Options.append("sir?")
            elif "daddy" not in RogueX.Petnames and Approvalcheck(RogueX, 750, "L") and Approvalcheck(RogueX, 500, "O") and Approvalcheck(RogueX, 500, "I"): # RogueX.Event[5]
                $ Options.append("daddy?")
            elif "master" not in RogueX.Petnames and Approvalcheck(RogueX, 900, "O"): # RogueX.Event[8]
                $ Options.append("master?")
            elif "sex friend" not in RogueX.Petnames and Approvalcheck(RogueX, 500, "I"): # RogueX.Event[9]
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in RogueX.Petnames and Approvalcheck(RogueX, 900, "I"): # RogueX.Event[10]
                $ Options.append("fuckbuddy?")

        if not Approvalcheck(RogueX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "virgin": # "virgin line" not yet triggered:
        call Rogue_Not_Virgin

    elif Options[0] == "mandrill":
        $ RogueX.daily_history.append("cologne_chat")
        $ RogueX.change_face("confused")
        ch_r "(sniff, sniff). . . something kind of smells like monkey butt in here. . ."
        $ RogueX.change_face("sly", 1)
        ch_r ". . . but you're looking pretty handsome today, [RogueX.Petname]."
    elif Options[0] == "purple":
        $ RogueX.daily_history.append("cologne_chat")
        $ RogueX.change_face("sly",1)
        ch_r "(sniff, sniff). . . hmm, you're smelling good today. . ."
        ch_r ". . . was there anything I could do to make you happy?"
    elif Options[0] == "corruption":
        $ RogueX.daily_history.append("cologne_chat")
        $ RogueX.change_face("confused")
        ch_r "(sniff, sniff). . . that's a pretty strong scent you've got there. . ."
        $ RogueX.change_face("sly")
        ch_r ". . . I'm gettin some pretty naughty thoughts over here, [RogueX.Petname]. . ."

    elif Options[0] == "blowjob":
        $ line = renpy.random.choice(["You know, you taste better than I thought.",
                "You're making my jaw a bit sore there.",
                "Let me know if you want a little mouth attention.",
                "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
        ch_r "[line]"

    elif Options[0] == "close": # RogueX.love >= 800
        ch_r "It's always been hard for me to get close to people, since I could never. . ."
        ch_r "get {i}close{/i} to them, you know?"
        ch_r "It's been real good for me to be able to get close to you like this."
        $ RogueX.daily_history.append("close chat")
    elif Options[0] == "caught": # Xavier's caught you
        ch_r "Wow, that was scary getting dragged into the Professor's office."
        if not Approvalcheck(RogueX, 500, "I"):
            ch_r "Maybe we should be more careful about where we. . . you know."
        else:
            ch_r "Maybe we should be more careful about where we fuck."
        $ RogueX.daily_history.append("caught chat")
    elif Options[0] == "key": # you have her key
        if RogueX.SEXP <= 15:
            ch_r "I'm glad you have my key now, just don't use it for any funny business. . ."
        else:
            ch_r "I'm glad you have my key now, maybe you could . . . \"surprise\" me sometime. . ."
        $ RogueX.daily_history.append("key chat")
    elif Options[0] == "touch": # "touch" in RogueX.Traits:
        ch_r "It's only because I've been working with you so much that I've been able to learn to control my abilities."
        ch_r "If it weren't for you, I wouldn't have been able to touch anyone!"
    elif Options[0] == "steal": # "steal" in RogueX.Traits:
        ch_r "It's only because of having worked with you and your powers that I've learned to permanently copy other mutant powers."
    elif Options[0] == "dance": # dancing comes up
        ch_r "Can't wait for the next big party."
        ch_r "I love to dance, and I've got the best partner to grind with-"
        $ RogueX.Pose = "doggy"
        call Rogue_Sex_Launch("massage")
        if RogueX.Legs == "skirt":
            $ RogueX.Upskirt = 1
            if RogueX.Panties and RogueX.SeenPanties and Approvalcheck(RogueX, 800, TabM = 3):
                pass
            elif RogueX.Panties and Approvalcheck(RogueX, 800, TabM = 3):
                $ RogueX.SeenPanties = 1
            elif RogueX.Panties:
                $ RogueX.Upskirt = 0
            elif RogueX.SeenPussy and Approvalcheck(RogueX, 1000, TabM = 4):
                pass
            elif Approvalcheck(RogueX, 1400, TabM = 3):
                call Rogue_First_Bottomless(1)
            else:
                $ RogueX.Upskirt = 0
            pause 0.5
            $ RogueX.Upskirt = 0
        ch_r "Y'know what I'm sayin', [RogueX.Petname]?"
        $ RogueX.Upskirt = 0
        call Rogue_Doggy_Reset

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ RogueX.change_face("sly",1)
            ch_r "You really did surprise me when you whipped that cock out."
            ch_r "I didn't know they looked so big up close."
            $ RogueX.change_face("bemused",1)
            $ RogueX.change_stat("love", 90, 5)
            $ RogueX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            ch_r "Hey, when you got a look at my tits earlier, you didn't have much to say. . ."
            ch_r "Did you like what you saw?"
            call Rogue_First_TMenu
            $ RogueX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            ch_r "Hey, when you saw me bottomless earlier, you didn't have much to say. . ."
            call Rogue_First_BMenu
            $ RogueX.History.remove("bottomless")

    elif Options[0] == "luv": # love maxed out
        $ RogueX.change_face("bemused", 1)
        ch_r ". . ."
        ch_r "You know, time was, I really thought I'd end up alone, unable to touch anyone. . ."
        $ RogueX.change_face("smile")
        ch_r "I'm really glad that I was able to find you."
        ch_r "I love you, [RogueX.Petname]."
        menu:
            extend ""
            "I love you too.":
                $ RogueX.change_stat("love", 200, 10)
                $ RogueX.change_stat("obedience", 80, 4)
                $ RogueX.change_stat("inhibition", 80, 4)
            "I love you too, [RogueX.Pet].":
                $ RogueX.namecheck()
                if _return:
                    $ RogueX.change_face("angry")
                    $ RogueX.change_stat("love", 90, -1)
                    $ RogueX.change_stat("obedience", 80, 10)
                    $ RogueX.change_stat("inhibition", 80, 4)
                else:
                    $ RogueX.change_stat("love", 200, 10)
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 80, 4)
            "Yeah, same here.":
                $ RogueX.change_face("perplexed")
                $ RogueX.change_stat("love", 90, -1)
                $ RogueX.change_stat("obedience", 80, 10)
                $ RogueX.change_stat("inhibition", 80, 4)
            "Whatever.":
                $ RogueX.change_face("angry")
                $ RogueX.change_stat("love", 200, -10)
                $ RogueX.change_stat("obedience", 80, 4)
                $ RogueX.change_stat("inhibition", 80, 10)

    elif Options[0] == "boyfriend?":
        call Rogue_BF
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "lover?":
        call Rogue_love
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "sir?":
        call Rogue_Sub
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "master?":
        call Rogue_Master
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "sexfriend?":
        call Rogue_Sexfriend
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "fuckbuddy?":
        call Rogue_Fuckbuddy
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "daddy?":
        call Rogue_Daddy
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "annamarie":
        call Rogue_AnnaMarie #adds new names to list
    elif Options[0] == "hate": # trinty lower then 50:
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want to see your face.",
                "Stop bothering me.",
                "Leave me alone."])
        ch_r "[line]"

    else: #all else fell through. . .
        $ D20 = renpy.random.randint(1, 16)
        if D20 == 1:
                $ RogueX.change_face("confused")
                ch_r "I'm so nervous about this Genetics test with Professor McCoy. I don't get this stuff at all."
        elif D20 == 2:
                $ RogueX.change_face("sad")
                ch_r "Feeling kinda down today, [RogueX.Petname]. Family problems. It's. . .kinda complicated."
        elif D20 == 3:
                $ RogueX.change_face("sly")
                ch_r "So, um. . .maybe you heard about the friends I used to hang out with? They're not all as bad as they seem. Mostly."
        elif D20 == 4:
                $ RogueX.change_face("smile")
                ch_r "I had the best workout earlier in the Danger Room today! Wish you coulda seen me!"
        elif D20 == 5:
                $ RogueX.change_face("smile")
                ch_r "Ever wonder what it would be like to be able to fly? That's gotta be the coolest power, right?"
        elif D20 == 6:
                $ RogueX.change_face("smile")
                ch_r "Ever been out to Breakstone Lake, behind the Mansion? It's so nice and peaceful. Kinda reminds me of back home in Mississippi, during the summer. Just a little chillier."
        elif D20 == 7:
                $ RogueX.change_face("smile")
                $ RogueX.Eyes = "surprised"
                ch_r "I just saw the coolest thing, when I was walking through the courtyard! A bunch of deer, in the woods, just over by the fence!"
                $ RogueX.Eyes = "side"
                ch_r "Their fur looked so. . .{i}soft{/i}. I wonder what they actually feel like?"
        elif D20 == 8:
                $ RogueX.change_face("smile")
                ch_r "Hey, did you see the Avengers on the news this morning?  Those guys make everything look {i}so{/i} easy!"
        elif D20 == 9:
                $ RogueX.change_face("smile")
                ch_r "A couple of us are gonna get together and go for a jog around one of the Mansion's sub-basements tomorrow. You should come with us!"
        elif D20 == 10:
                $ RogueX.change_face("down")
                ch_r "I have {i}so{/i} much homework this week! And I {i}so{/i} don't feel like doing any of it!"
        elif D20 == 11:
                $ RogueX.change_face("startled")
                ch_r "Y'know, I {i}really{/i} hate my powers. But could you imagine having Professor Xavier's?"
                ch_r "I don't know if I could handle that kind of responsibility."
                ch_r "Might be even worse than mine, in their own way."
        elif D20 == 12:
                $ RogueX.change_face("sad")
                ch_r "The Mansion's a great place to live. . .but sometimes I get weirded out when I think how we could get attacked by some super-maniac any given second."
        elif D20 == 13:
                $ RogueX.change_face("smile")
                ch_r "I love it when you get a really good night's sleep. Feels amazing!"
        elif D20 == 14:
                $ RogueX.change_face("bemused")
                ch_r "I heard they're thinking about maybe having a school dance this year. That could be. . .{i}interesting{/i}."
        elif D20 == 15:
                $ RogueX.change_face("smile")
                ch_r "You been outside today? Wow, is it gorgeous!"
        elif D20 == 16:
                $ RogueX.change_face("smile")
                ch_r "You know, I tagged Wolverine once,"
                $ RogueX.change_face("sadside")
                $ RogueX.Brows = "confused"
                ch_r "I still catch myself calling people \"bub\" from time to time."
        else:
                $ RogueX.change_face("smile")
                ch_r "I like hanging out with you like this!"
    $ line = 0
    return

label Rogue_Names:
        #Sets pet names from Rogue
        if Approvalcheck(RogueX, 600, "L", TabM=0) or Approvalcheck(RogueX, 300, "O", TabM=0):
            pass
        else:
            $ RogueX.Mouth = "smile"
            ch_r "I'll call you what I like, [RogueX.Petname], and you'll like it."
            return
        menu:
            ch_r "Oh? What would you like me to call you?"
            "Sugar's fine.":
                    $ RogueX.Petname = "sugar"
                    ch_r "You got it, sugar."
            "Call me by my name.":
                    $ RogueX.Petname = Player.name
                    ch_r "If you'd rather, [RogueX.Petname]."
            "Call me \"boyfriend\"." if "boyfriend" in RogueX.Petnames:
                    $ RogueX.Petname = "boyfriend"
                    ch_r "Sure thing, [RogueX.Petname]."
            "Call me \"lover\"." if "lover" in RogueX.Petnames:
                    $ RogueX.Petname = "lover"
                    ch_r "Oooh, love to, [RogueX.Petname]."
            "Call me \"sir\"." if "sir" in RogueX.Petnames:
                    $ RogueX.Petname = "sir"
                    ch_r "Yes, [RogueX.Petname]."
            "Call me \"master\"." if "master" in RogueX.Petnames:
                    $ RogueX.Petname = "master"
                    ch_r "As you wish, [RogueX.Petname]."
            "Call me \"sex friend\"." if "sex friend" in RogueX.Petnames:
                    $ RogueX.Petname = "sex friend"
                    ch_r "Heh, very cheeky, [RogueX.Petname]."
            "Call me \"fuck buddy\"." if "fuck buddy" in RogueX.Petnames:
                    $ RogueX.Petname = "fuck buddy"
                    ch_r "I'm game if you are, [RogueX.Petname]."
            "Call me \"daddy\"." if "daddy" in RogueX.Petnames:
                    $ RogueX.Petname = "daddy"
                    ch_r "Oh! You bet, [RogueX.Petname]."
            "Nevermind.":
                return
        return

label Rogue_Pet:
        #sets what you call Rogue
        if Approvalcheck(RogueX, 600, "L", TabM=0):
            ch_r "Oh? What is it?"
        elif Approvalcheck(RogueX, 300, "O", TabM=0):
            ch_r "What did you want to call me?"
        else:
            ch_r "Oh, this should be good. . ."
        while 1:
            menu:
                extend ""
                "Polite":
                    menu:
                        extend ""
                        "I think I'll just call you Rogue.":
                            $ RogueX.Pet = "Rogue"
                            ch_r "I don't see why not, [RogueX.Petname]."

                        "I think I'll call you \"girl\".":
                            $ RogueX.Pet = "girl"
                            if "boyfriend" in RogueX.Petnames or Approvalcheck(RogueX, 500, "L"):
                                $ RogueX.change_face("sexy", 1)
                                ch_r "I sure am your girl, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry")
                                ch_r "I ain't your girl, [RogueX.Petname]."

                        "I think I'll call you \"boo\".":
                            $ RogueX.Pet = "boo"
                            if "boyfriend" in RogueX.Petnames or Approvalcheck(RogueX, 500, "L"):
                                $ RogueX.change_face("sexy", 1)
                                ch_r "Aw, I am your boo, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry")
                                ch_r "I ain't your boo,  [RogueX.Petname]."

                        "I think I'll call you \"bae\".":
                            $ RogueX.Pet = "bae"
                            if "boyfriend" in RogueX.Petnames or Approvalcheck(RogueX, 500, "L"):
                                $ RogueX.change_face("sexy", 1)
                                ch_r "Aw, I am your bae, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry")
                                ch_r "I ain't your bae,  [RogueX.Petname]."

                        "I think I'll call you \"baby\".":
                            $ RogueX.Pet = "baby"
                            if "boyfriend" in RogueX.Petnames or Approvalcheck(RogueX, 500, "L"):
                                $ RogueX.change_face("sexy", 1)
                                ch_r "Aw, cute, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry")
                                ch_r "I ain't your baby, [RogueX.Petname]."

                        "I think I'll call you \"chere\".":
                            $ RogueX.Pet = "chere"
                            if "lover" in RogueX.Petnames or Approvalcheck(RogueX, 600, "L"):
                                $ RogueX.change_face("sexy", 1)
                                ch_r "Oh, tre romantic, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                $ RogueX.Eyes = "side"
                                ch_r "That has some. . . bad memories, [RogueX.Petname]."

                        "I think I'll call you \"sweetie\".":
                            $ RogueX.Pet = "sweetie"
                            if "boyfriend" in RogueX.Petnames or Approvalcheck(RogueX, 500, "L"):
                                ch_r "Aw, that's sweet, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "That's a bit much, [RogueX.Petname]."

                        "I think I'll call you \"sexy\".":
                            $ RogueX.Pet = "sexy"
                            if "lover" in RogueX.Petnames or Approvalcheck(RogueX, 900):
                                $ RogueX.change_face("sexy", 1)
                                ch_r "You're not so bad yourself, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "Inappropriate, [RogueX.Petname]."

                        "I think I'll call you \"lover\".":
                            $ RogueX.Pet = "lover"
                            if "lover" in RogueX.Petnames or Approvalcheck(RogueX, 900):
                                $ RogueX.change_face("sexy", 1)
                                ch_r "Oh, I love you too, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "Not any time soon, [RogueX.Petname]."

                        "Back":
                            pass

                "Risky":
                    menu:
                        "I think I'll call you \"slave\".":
                            $ RogueX.Pet = "slave"
                            if "master" in RogueX.Petnames or Approvalcheck(RogueX, 700, "O"):
                                $ RogueX.change_face("bemused", 1)
                                ch_r "As you wish, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "I ain't anyone's slave, [RogueX.Petname]."

                        "I think I'll call you \"pet\".":
                            $ RogueX.Pet = "pet"
                            if "master" in RogueX.Petnames or Approvalcheck(RogueX, 600, "O"):
                                $ RogueX.change_face("bemused", 1)
                                ch_r "Hmm, make sure to pet me, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "I ain't your pet, [RogueX.Petname]."

                        "I think I'll call you \"slut\".":
                            $ RogueX.Pet = "slut"
                            if "sex friend" in RogueX.Petnames or Approvalcheck(RogueX, 1000, "OI"):
                                $ RogueX.change_face("sexy")
                                ch_r "You know me too well, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                $ RogueX.Mouth = "surprised"
                                ch_r "Well I never!"

                        "I think I'll call you \"whore\".":
                            $ RogueX.Pet = "whore"
                            if "fuckbuddy" in RogueX.Petnames or Approvalcheck(RogueX, 1100, "OI"):
                                $ RogueX.change_face("sly")
                                ch_r "I guess I am. . ."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "You look'in to start something, [RogueX.Petname]?"

                        "I think I'll call you \"sugartits\".":
                            $ RogueX.Pet = "sugartits"
                            if "sex friend" in RogueX.Petnames or Approvalcheck(RogueX, 1500):
                                $ RogueX.change_face("sly", 1)
                                ch_r "Heh."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "Better not to my face, [RogueX.Petname]."

                        "I think I'll call you \"sex friend\".":
                            $ RogueX.Pet = "sex friend"
                            if "sex friend" in RogueX.Petnames or Approvalcheck(RogueX, 600, "I"):
                                $ RogueX.change_face("sly")
                                ch_r "Rreow. . ."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "Hey, no need to advertise, [RogueX.Petname]."

                        "I think I'll call you \"fuckbuddy\".":
                            $ RogueX.Pet = "fuckbuddy"
                            if "fuckbuddy" in RogueX.Petnames or Approvalcheck(RogueX, 700, "I"):
                                $ RogueX.change_face("sly")
                                ch_r "That sounds about right, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                $ RogueX.Mouth = "surprised"
                                ch_r "Inappropriate, [RogueX.Petname]."

                        "I think I'll call you \"baby girl\".":
                            $ RogueX.Pet = "baby girl"
                            if "daddy" in RogueX.Petnames or Approvalcheck(RogueX, 1200):
                                $ RogueX.change_face("smile", 1)
                                ch_r "You know it, [RogueX.Petname]."
                            else:
                                $ RogueX.change_face("angry", 1)
                                ch_r "I ain't your baby girl, [RogueX.Petname]."

                        "Back":
                            pass

                "Nevermind.":
                    return
        return

label Rogue_Rename:
        #Sets alternate names from Rogue
        $ RogueX.Mouth = "smile"
        ch_r "Yeah? What of it?"
        menu:
            extend ""
            "I guess \"Rogue\" suits you." if RogueX.name != "Rogue":
                    $ RogueX.name = "Rogue"
                    ch_r "You bet."
            "I liked the sound of \"Marie.\"" if RogueX.name != "Marie" and "Marie" in RogueX.names:
                    $ RogueX.name = "Marie"
                    ch_r "Yeah, I could go by that again. . ."
            "I liked the sound of \"Anna.\"" if RogueX.name != "Anna" and "Anna" in RogueX.names:
                    $ RogueX.name = "Anna"
                    ch_r "Yeah, I could go by that again. . ."
            "I liked the sound of \"Anna-Marie.\"" if RogueX.name != "Anna-Marie" and "Anna-Marie" in RogueX.names:
                    $ RogueX.name = "Anna-Marie"
                    ch_r "Yeah, I could go by that again. . ."
            "Nevermind.":
                return
        return

label Rogue_Personality(counter = 0):
        if not RogueX.Chat[4] or counter:
            "Since you're doing well in one area, you can convince [RogueX.name] to focus on one of the others."
            "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
            "This will also impact which personality trait takes priority in dialog."
        menu:
            ch_r "Sure, what's up?"
            "More obedienceient. [[love to obedience]" if RogueX.love > 900:
                ch_p "If you really love me, could you please just do what I say?"
                ch_r "Well, I suppose for you I could be a bit more obedient."
                $ RogueX.Chat[4] = 1
            "Less Inhibited. [[love to Inhibition]" if RogueX.love > 900:
                ch_p "If you really love me, could lighten up a bit, just have some fun?"
                ch_r "Well, I suppose for you I could be a bit less inhibited."
                $ RogueX.Chat[4] = 2

            "Less Inhibited. [[obedience to Inhibition]" if RogueX.obedience > 900:
                ch_p "I want you to be less inhibited."
                ch_r "Very well, I'll try to take more initiative."
                $ RogueX.Chat[4] = 3
            "More Loving. [[obedience to love]" if RogueX.obedience > 900:
                ch_p "I'd like you to learn to love me."
                ch_r "If I must, I'll try to come around."
                $ RogueX.Chat[4] = 4

            "More obedienceient. [[Inhibition to obedience]" if RogueX.inhibition > 900:
                ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
                ch_r "Well, I guess it can be fun to try what you want too. . ."
                $ RogueX.Chat[4] = 5

            "More Loving. [[Inhibition to love]" if RogueX.inhibition > 900:
                ch_p "I know we're having fun, but do you even care about me?"
                ch_r "Well, I guess I am getting pretty attached. . ."
                $ RogueX.Chat[4] = 6

            "I guess just do what you like. . .[[reset]" if RogueX.Chat[4]:
                ch_p "You know what we talked about before? Nevermind that stuff."
                ch_r "Um, ok."
                $ RogueX.Chat[4] = 0
            "Repeat the rules":
                call Rogue_Personality(1)
                return
            "Nevermind.":
                return
        return

label Rogue_Clothes:
    if RogueX.Taboo:
            if "exhibitionist" in RogueX.Traits:
                ch_r "Oooh, naughty. . ."
            elif Approvalcheck(RogueX, 900, TabM=4) or Approvalcheck(RogueX, 400, "I", TabM=3):
                ch_r "Well, I mean, it's pretty public here, but I guess I could. . ."
            else:
                ch_r "This is a pretty public place for that, don't you think?"
                ch_r "We can talk about that back in our rooms."
                return
    elif Approvalcheck(RogueX, 900, TabM=4) or Approvalcheck(RogueX, 600, "L") or Approvalcheck(RogueX, 300, "O"):
                ch_r "Ok, what did you want?"
    else:
                ch_r "I'm not really interested in your fashion opinions."
                return
    if Girl != RogueX or line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ line = 0
    $ Girl = RogueX
    call shift_focus(Girl)

label Rogue_Wardrobe_Menu:
    while True:
        $ primary_action = 1 # to prevent Focus swapping. . .
        $ RogueX.change_face()
        menu:
            ch_r "So what did you want to tell me about my clothes again?"
            "Overshirts":
                    call Rogue_Clothes_Over
            "Legwear":
                    call Rogue_Clothes_Legs
            "Underwear":
                    call Rogue_Clothes_Under
            "Accessories":
                    call Rogue_Clothes_Misc
            "Outfit Management":
                    call Rogue_Clothes_Outfits
            "Let's talk about what you wear around.":
                    call Clothes_Schedule(RogueX)

            "Could I get a look at it?" if RogueX.location != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(RogueX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_r "How's that? . ."
                    hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(RogueX,0,2)
                    if _return:
                        hide DressScreen

            "Would you be more comfortable behind a screen? (locked)" if RogueX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if RogueX.location == bg_current and not RogueX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if Approvalcheck(RogueX, 1500) or (RogueX.SeenChest and RogueX.SeenPussy):
                            ch_r "Don't really need that, thanks."
                    else:
                            show DressScreen zorder 150
                            ch_r "This is more comfortable, thanks."

            "Gift for you (locked)" if Girl.location != bg_current:
                            pass
            "Gift for you" if Girl.location == bg_current:
                            ch_p "I'd like to give you something."
                            call Gifts #(Girl)

            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(RogueX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ RogueX.OutfitChange()
                    $ RogueX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ primary_action = 0
                    call Switch_Chat
                    if Girl != RogueX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = RogueX
                    call shift_focus(Girl)

            "Never mind, you look good like that. [[return]":
                    if "wardrobe" not in RogueX.recent_history:
                            #Apply stat boosts only if it's the first time this turn
                            if RogueX.Chat[1] <= 1:
                                    $ RogueX.change_stat("love", 70, 10)
                                    $ RogueX.change_stat("obedience", 20, 10)
                                    ch_r "Aw, that's sweet."
                            elif RogueX.Chat[1] <= 10:
                                    $ RogueX.change_stat("love", 70, 5)
                                    $ RogueX.change_stat("obedience", 20, 5)
                                    ch_r "Thanks."
                            elif RogueX.Chat[1] <= 50:
                                    $ RogueX.change_stat("love", 70, 1)
                                    $ RogueX.change_stat("obedience", 20, 1)
                                    ch_r "Ok."
                            else:
                                    ch_r "Ok."
                            $ RogueX.recent_history.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(RogueX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ RogueX.OutfitChange()
                    #sets up a temporary outfit
                    $ RogueX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ RogueX.Chat[1] += 1
                    $ primary_action = 0
                    return
        #Loops back up

    menu Rogue_Clothes_Outfits:
        # Outfits
        "That looks really good on you, you should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(RogueX,3,1)
                    "Custom 2":
                                call OutfitShame(RogueX,5,1)
                    "Custom 3":
                                call OutfitShame(RogueX,6,1)
                    "Gym Clothes":
                                call OutfitShame(RogueX,4,1)
                    "Sleepwear":
                                call OutfitShame(RogueX,7,1)
                    "Swimwear":
                                call OutfitShame(RogueX,10,1)
                    "Never mind":
                                pass

        "I really like that green top and skirt outfit you have.":
                #Green
                $ RogueX.OutfitChange("casual1")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ RogueX.Outfit = "casual1"
                        $ RogueX.Shame = 0
                        ch_r "Ok, [RogueX.Petname], I like this one too."
                    "Let's try something else though.":
                        ch_r "Sure."

        "That pink top and pants look really nice on you.":
                #Pink
                $ RogueX.OutfitChange("casual2")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ RogueX.Outfit = "casual2"
                        $ RogueX.Shame = 0
                        ch_r "Sure, [RogueX.Petname], that one's nice."
                    "Let's try something else though.":
                        ch_r "Ok."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not RogueX.Custom1[0] and not RogueX.Custom2[0] and not RogueX.Custom3[0]:
                        pass

        "Remember that outfit we put together?" if RogueX.Custom1[0] or RogueX.Custom2[0] or RogueX.Custom3[0]:
                        $ counter = 0
                        while 1:
                            menu:
                                "Throw on Custom 1 (locked)" if not RogueX.Custom1[0]:
                                        pass
                                "Throw on Custom 1" if RogueX.Custom1[0]:
                                        $ RogueX.OutfitChange("custom1")
                                        $ counter = 3
                                "Throw on Custom 2 (locked)" if not RogueX.Custom2[0]:
                                        pass
                                "Throw on Custom 2" if RogueX.Custom2[0]:
                                        $ RogueX.OutfitChange("custom2")
                                        $ counter = 5
                                "Throw on Custom 3 (locked)" if not RogueX.Custom3[0]:
                                        pass
                                "Throw on Custom 3" if RogueX.Custom3[0]:
                                        $ RogueX.OutfitChange("custom3")
                                        $ counter = 6

                                "You should wear this one in private. (locked)" if not counter:
                                        pass
                                "You should wear this one in private." if counter:
                                        if counter == 5:
                                            $ RogueX.Clothing[9] = "custom2"
                                        elif counter == 6:
                                            $ RogueX.Clothing[9] = "custom3"
                                        else:
                                            $ RogueX.Clothing[9] = "custom1"
                                        ch_r "Ok, sure."

                                "On second thought, forget about that one outfit. . .":
                                        menu:
                                            ch_r "Which one did you mean?"
                                            "Custom 1 [[clear custom 1]" if RogueX.Custom1[0]:
                                                ch_r "Ok, no problem."
                                                $ RogueX.Custom1[0] = 0
                                            "Custom 1 [[clear custom 1] (locked)" if not RogueX.Custom1[0]:
                                                pass
                                            "Custom 2 [[clear custom 2]" if RogueX.Custom2[0]:
                                                ch_r "Ok, no problem."
                                                $ RogueX.Custom2[0] = 0
                                            "Custom 2 [[clear custom 2] (locked)" if not RogueX.Custom2[0]:
                                                pass
                                            "Custom 3 [[clear custom 3]" if RogueX.Custom3[0]:
                                                ch_r "Ok, no problem."
                                                $ RogueX.Custom3[0] = 0
                                            "Custom 3 [[clear custom 3] (locked)" if not RogueX.Custom3[0]:
                                                pass
                                            "Never mind, [[back].":
                                                pass

                                "You should wear this one out. [[choose outfit first](locked)" if not counter:
                                                pass
                                "You should wear this one out." if counter:
                                                call Custom_Out(RogueX,counter)
                                "Ok, back to what we were talking about. . .":
                                                $ counter = 0
                                                return
                                                #jump Rogue_Clothes

        "Gym Clothes?" if not RogueX.Taboo or bg_current == "bg_dangerroom":
                $ RogueX.OutfitChange("gym")

        "Sleepwear?" if not RogueX.Taboo:
                if Approvalcheck(RogueX, 1200):
                        $ RogueX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(RogueX)
                        if _return:
                            $ RogueX.OutfitChange("sleep")

        "Swimwear? (locked)" if (RogueX.Taboo and bg_current != "bg_pool") or not RogueX.Swim[0]:
                $ RogueX.OutfitChange("swimwear")
        "Swimwear?" if (not RogueX.Taboo or bg_current == "bg_pool") and RogueX.Swim[0]:
                $ RogueX.OutfitChange("swimwear")

        "Halloween Costume?" if "halloween" in RogueX.History:
                ch_r "Sure."
                $ RogueX.OutfitChange("costume")

        "Your birthday suit looks really great. . .":
                #Nude
                $ RogueX.change_face("sexy", 1)
                $ line = 0
                if not RogueX.Chest and not RogueX.Panties and not RogueX.Over and not RogueX.Legs and not RogueX.Hose:
                        ch_r "Can't get much more naked than this."
                elif RogueX.SeenChest and RogueX.SeenPussy and Approvalcheck(RogueX, 1000, TabM=5):
                        ch_r "Naughty boy. . ."
                        $ line = 1
                elif Approvalcheck(RogueX, 2000, TabM=5):
                        ch_r "Hmm. . . you move fast, but I suppose for you. . ."
                        $ line = 1
                elif RogueX.SeenChest and RogueX.SeenPussy and Approvalcheck(RogueX, 1000, TabM=0):
                        ch_r "Well, maybe if it weren't quite so. . . public here."
                elif Approvalcheck(RogueX, 2000, TabM=0):
                        ch_r "I might consider it if we had some privacy. . ."
                elif Approvalcheck(RogueX, 1000, TabM=0):
                        $ RogueX.change_face("surprised", 1)
                        ch_r "Hmm. . . you're getting a bit ahead of yourself, [RogueX.Petname]."
                else:
                        $ RogueX.change_face("angry", 1)
                        ch_r "What sort of common strumpet do you take me for?"

                if line:                                                            #If she got nude. . .
                        $ RogueX.OutfitChange("nude")
                        "She pulls all her clothes off and throws them in a heap on the floor."
                        call first_topless(RogueX)
                        call Rogue_First_Bottomless(1)
                        $ RogueX.change_face("sexy")
                        menu:
                            "You know, you should wear this one out. [[set current outfit]":
                                if "exhibitionist" in RogueX.Traits:
                                        ch_r "You sure know how to rev my engines. . ."
                                        $ RogueX.Outfit = "nude"
                                        $ RogueX.Shame = 50
                                elif Approvalcheck(RogueX, 750, "I") or Approvalcheck(RogueX, 2500, TabM=0):
                                        ch_r "Heh, all right [RogueX.Petname]."
                                        $ RogueX.Outfit = "nude"
                                        $ RogueX.Shame = 50
                                else:
                                        $ RogueX.change_face("sexy", 1)
                                        $ RogueX.Eyes = "surprised"
                                        ch_r "I'm afraid not, [RogueX.Petname], this is just for between you and me."
                            "Let's try something else though.":
                                if "exhibitionist" in RogueX.Traits:
                                        ch_r "Hmm, too bad you didn't want me to wear this out. . ."
                                elif Approvalcheck(RogueX, 750, "I") or Approvalcheck(RogueX, 2500, TabM=0):
                                        $ RogueX.change_face("bemused", 1)
                                        ch_r "You know, for a second there I thought you might want me to wear this out. . ."
                                        ch_r "Hehe, um. . ."
                                else:
                                        $ RogueX.change_face("confused", 1)
                                        ch_r "Well obviously. It's not like I'd ever go out like this."
                $ line = 0

        "Never mind":
                        return
                        #jump Rogue_Clothes
    return
    #jump Rogue_Clothes
    #End of Rogue Outfits

    menu Rogue_Clothes_Over:
        # Overshirts
        "Why don't you go with no [RogueX.Over]?" if RogueX.Over:
                $ RogueX.change_face("bemused", 1)
                if RogueX.Chest or (RogueX.SeenChest and Approvalcheck(RogueX, 600)):
                    ch_r "Sure."
                elif Approvalcheck(RogueX, 600, TabM=0):
                    call Rogue_NoBra
                    if not _return:
                            if not Approvalcheck(RogueX, 1200):
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    return
                                    #jump Rogue_Clothes
                            else:
                                    return
                                    #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "I'd rather not. . ."
                            if not RogueX.Chest:
                                    ch_r "I'm afraid I don't have anything on under this."
                            return
                            #jump Rogue_Clothes
                $ RogueX.Over = 0
                if not RogueX.Chest and not renpy.showing('DressScreen'):
                            call first_topless(RogueX)

        "Try on the green mesh top." if RogueX.Over != "mesh top":
                $ RogueX.change_face("bemused", 1)
                if RogueX.Chest or (RogueX.SeenChest and Approvalcheck(RogueX, 500, TabM=2)):
                    ch_r "Sure."
                elif Approvalcheck(RogueX, 600, TabM=0):
                    call Rogue_NoBra
                    if not _return:
                        if not Approvalcheck(RogueX, 1200):
                            call Display_DressScreen(RogueX)
                            if not _return:
                                return  #jump Rogue_Clothes
                        else:
                                return  #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "I'm afraid that top is a bit sheer to have nothing under it."
                            if not RogueX.Chest:
                                ch_r "I don't have anything on under this."
                            return  #jump Rogue_Clothes

                $ RogueX.Over = "mesh top"
                menu:
                    ch_r "With the collar?"
                    "Yes":
                        $ RogueX.Neck = "spiked collar"
                    "No":
                        $ RogueX.Neck = 0

                if not RogueX.Chest and not renpy.showing('DressScreen'):
                    call first_topless(RogueX)

        "How about that pink top?" if RogueX.Over != "pink top":
                $ RogueX.Over = "pink top"
                $ RogueX.Neck = 0

        "How about that green hoodie?" if RogueX.Over != "hoodie":
                $ RogueX.Over = "hoodie"

        "Maybe just throw on a towel?" if RogueX.Over != "towel":
                $ RogueX.change_face("bemused", 1)
                if RogueX.Chest or RogueX.SeenChest:
                    ch_r "Fresh."
                elif Approvalcheck(RogueX, 900, TabM=0):
                    $ RogueX.change_face("perplexed", 1)
                    ch_r "I suppose? . ."
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                            ch_r "That don't leave much to the imagination. . ."
                            return  #jump Rogue_Clothes
                $ RogueX.Over = "towel"

        "How about that green nighty I got you?" if RogueX.Over != "nighty" and "nighty" in RogueX.Inventory:
                if RogueX.Legs:
                        ch_r "I can't really wear that with my [RogueX.Legs] on."
                elif not Approvalcheck(RogueX, 1100, TabM=3):
                        call Display_DressScreen(RogueX)
                        if not _return:
                                ch_r "That's a bit . . . revealing."
                                return  #jump Rogue_Clothes
                else:
                        ch_r "Sure. . ."
                if "lace bra" in RogueX.Inventory:
                    $ RogueX.Chest = "lace bra"
                else:
                    $ RogueX.Chest = "bra"
                if "lace panties" in RogueX.Inventory:
                    $ RogueX.Panties = "lace panties"
                else:
                    $ RogueX.Panties = "black panties"
                $ RogueX.Over = "nighty"
                menu:
                    extend ""
                    "Nice.":
                        pass
                    "I meant {i}just{/i} the nighty.":
                        if Approvalcheck(RogueX, 1400, TabM=3):
                            "She shrugs off her bra and then pulls the nighty back up."
                            $ RogueX.Panties = 0
                            $ RogueX.Chest = 0
                            ch_r "Hmmm, alright. . ."
                        elif Approvalcheck(RogueX, 1200, TabM=3):
                            $ RogueX.Chest = 0
                            ch_r "I'll keep my panties on, thanks."
                        else:
                            ch_r "Be happy with what you get."
                if not RogueX.Chest and not renpy.showing('DressScreen'):
                    call first_topless(RogueX)

        "Never mind":
            pass
    return  #jump Rogue_Clothes
    #End of Rogue Top

    label Rogue_NoBra:
        menu:
            ch_r "I don't have anything under this. . ."
            "Then you could slip something on under it. . .":
                        if RogueX.SeenChest and Approvalcheck(RogueX, 1000, TabM=3) or Approvalcheck(RogueX, 1200, TabM=4):
                                $ RogueX.Blush = 2
                                ch_r "'course, I don't exactly need something under it either. . ."
                                $ RogueX.Blush = 1
                        elif Approvalcheck(RogueX, 900, TabM=2) and "lace bra" in RogueX.Inventory:
                                ch_r "I suppose this would work. . ."
                                $ RogueX.Chest  = "lace bra"
                                "She pulls out her lace bra and slips it on under her [RogueX.Over]."
                        elif Approvalcheck(RogueX, 800, TabM=2):
                                ch_r "Yeah, I guess."
                                $ RogueX.Chest = "bra"
                                "She pulls out her bra and slips it on under her [RogueX.Over]."
                        elif Approvalcheck(RogueX, 600, TabM=2):
                                ch_r "Yeah, I guess."
                                $ RogueX.Chest = "tank"
                                "She pulls out her tanktop and slips it on under her [RogueX.Over]."
                        else:
                                ch_r "Yeah, I don't think so."
                                return 0

            "You could always just wear nothing at all. . .":
                        if Approvalcheck(RogueX, 1100, "LI", TabM=2) and RogueX.love > RogueX.inhibition:
                                ch_r "I suppose I could. . ."
                        elif Approvalcheck(RogueX, 700, "OI", TabM=2) and RogueX.obedience > RogueX.inhibition:
                                ch_r "Sure. . ."
                        elif Approvalcheck(RogueX, 600, "I", TabM=2):
                                ch_r "Yeah. . ."
                        elif Approvalcheck(RogueX, 1300, TabM=2):
                                ch_r "Okay, fine."
                        else:
                                $ RogueX.change_face("surprised")
                                $ RogueX.Brows = "angry"
                                if RogueX.Taboo > 20:
                                    ch_r "Not in public, [RogueX.Petname]!"
                                else:
                                    ch_r "Don't push it, [RogueX.Petname]."
                                return 0

            "Never mind.":
                        ch_r "Ok. . ."
                        return 0
        return 1
        #End of Rogue bra check

    menu Rogue_Clothes_Legs:
        # Leggings
        "Maybe go without the [RogueX.Legs]." if RogueX.Legs:
                $ RogueX.change_face("sexy", 1)
                if RogueX.SeenPanties and RogueX.Panties and Approvalcheck(RogueX, 500, TabM=5):
                        ch_r "Sure."
                elif RogueX.SeenPussy and Approvalcheck(RogueX, 900, TabM=4):
                        ch_r "Sure, why not?"
                elif Approvalcheck(RogueX, 1300, TabM=2) and RogueX.Panties:
                        ch_r "Well, I suppose if it's for you. . ."
                elif Approvalcheck(RogueX, 700) and not RogueX.Panties:
                        call Rogue_NoPantiesOn
                        if not _return and not RogueX.Panties:
                            if not Approvalcheck(RogueX, 1500):
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    return  #jump Rogue_Clothes
                            else:
                                    return  #jump Rogue_Clothes
                else:
                        call Display_DressScreen(RogueX)
                        if not _return:
                            ch_r "Not in front of you, [RogueX.Petname]."
                            if not RogueX.Panties:
                                ch_r "Maybe if I put some panties on first. . ."
                            return  #jump Rogue_Clothes
                if RogueX.PantsNum() > 6:
                        $ RogueX.Legs = 0
                        "She tugs her pants off and drops them to the ground."
                else:
                        $ RogueX.Legs = 0
                        "She tugs her skirt off and drops it to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif RogueX.Panties:
                    $ RogueX.SeenPanties = 1
                else:
                    call Rogue_First_Bottomless

        "How about that skirt?" if RogueX.Legs != "skirt":
                $ RogueX.Legs = "skirt"
                $ RogueX.Upskirt = 0

        "Your ass looks tight in those jeans." if RogueX.Legs != "pants":
                $ RogueX.Legs = "pants"
                $ RogueX.Hose = 0

        "The tights would look good with that." if RogueX.Hose != 'tights' and RogueX.Legs != "pants":
                $ RogueX.Hose = "tights"
        "Your ripped tights would look good with that." if RogueX.Hose != 'ripped tights' and "ripped tights" in RogueX.Inventory and RogueX.Legs != "pants":
                $ RogueX.Hose = "ripped tights"
        "You could lose the tights." if RogueX.Hose == 'ripped tights' or RogueX.Hose == 'tights':
                $ RogueX.Hose = 0

        "What about wearing your shorts?" if RogueX.Panties != "shorts":
                ch_r "Alright."
                $ RogueX.Panties = "shorts"
        "Why don't you lose the shorts?" if RogueX.Panties == "shorts":
                $ RogueX.change_face("sexy", 1)
                if RogueX.SeenPanties and RogueX.Panties and Approvalcheck(RogueX, 500, TabM=5):
                    ch_r "Sure."
                elif RogueX.SeenPussy and Approvalcheck(RogueX, 900, TabM=4):
                    ch_r "Sure, why not?"
                elif Approvalcheck(RogueX, 1300, TabM=2) and RogueX.Panties:
                    ch_r "Well, I suppose if it's for you. . ."
                elif Approvalcheck(RogueX, 700) and not RogueX.Panties:
                    call Rogue_NoPantiesOn
                    if not _return and not RogueX.Panties:
                        if not Approvalcheck(RogueX, 1500):
                            call Display_DressScreen(RogueX)
                            if not _return:
                                return  #jump Rogue_Clothes
                        else:
                                return  #jump Rogue_Clothes
                else:
                    call Display_DressScreen(RogueX)
                    if not _return:
                        ch_r "Not in front of you, [RogueX.Petname]."
                        if not RogueX.Panties:
                            ch_r "Maybe if I put some panties on first. . ."
                        return  #jump Rogue_Clothes
                if RogueX.Panties == "shorts":
                        $ RogueX.Panties = 0
                "She tugs her shorts off and drops them to the ground."
                if renpy.showing('DressScreen'):
                    pass
                elif RogueX.Panties:
                    $ RogueX.SeenPanties = 1
                else:
                    call Rogue_First_Bottomless

        "How about that sweater?" if RogueX.Acc != "sweater" and "halloween" in RogueX.History:
                ch_p "What about that sweater you wore at the party?"
                $ RogueX.Acc = "sweater"
        "Lose the sweater?" if RogueX.Acc == "sweater" and "halloween" in RogueX.History:
                ch_p "You can do without the sweater."
                $ RogueX.Acc = 0

        "Never mind":
            pass
    return  #jump Rogue_Clothes
    #End of Rogue Pants

    label Rogue_NoPantiesOn:
        menu:
            ch_r "I'm not wearing anything under these, you know. . ."
            "Then you could slip on a pair of panties. . .":
                        if RogueX.SeenPussy and Approvalcheck(RogueX, 1100, TabM=4):
                                $ RogueX.Blush = 1
                                ch_r "Alright."
                                $ RogueX.Blush = 0
                        elif Approvalcheck(RogueX, 1500, TabM=4):
                                $ RogueX.Blush = 1
                                ch_r "Alright."
                                $ RogueX.Blush = 0
                        elif Approvalcheck(RogueX, 700, TabM=4):
                                ch_r "I like how you think."
                                if "lace panties" in RogueX.Inventory:
                                        $ RogueX.Panties  = "lace panties"
                                else:
                                        $ RogueX.Panties = "black panties"
                                if Approvalcheck(RogueX, 1200, TabM=4) and RogueX.Legs:
                                        $ line = RogueX.Legs
                                        $ RogueX.Legs = 0
                                        "She pulls off her [line] and slips on the [RogueX.Panties]."
                                elif RogueX.Legs == "skirt":
                                        "She pulls out her [RogueX.Panties] and pulls them up under her skirt."
                                        $ RogueX.Legs = 0
                                        "Then she drops the skirt to the floor."
                                else:
                                        $ line = RogueX.Legs
                                        $ RogueX.Legs = 0
                                        "She steps away a moment and then comes back wearing only the [RogueX.Panties]."
                                return  #jump Rogue_Clothes
                        else:
                                ch_r "Nope."
                                return 0

            "You could always just wear nothing at all. . .":
                    if Approvalcheck(RogueX, 1100, "LI", TabM=3) and RogueX.love > RogueX.inhibition:
                            ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                    elif Approvalcheck(RogueX, 750, "OI", TabM=3) and RogueX.obedience > RogueX.inhibition:
                            ch_r "If that's what you want."
                    elif Approvalcheck(RogueX, 500, "I", TabM=3):
                            ch_r "Oooh, naughty."
                    elif Approvalcheck(RogueX, 1400, TabM=3):
                            ch_r "Oh, fine. You've been a good boy."
                    else:
                            $ RogueX.change_face("surprised")
                            $ RogueX.Brows = "angry"
                            if RogueX.Taboo:
                                ch_r "Not here,[RogueX.Petname]!"
                            else:
                                ch_r "Not with you around,[RogueX.Petname]!"
                            return 0

            "Never mind.":
                ch_r "Ok. . ."
                return 0
        return 1
        #End of Rogue Panties check

    menu Rogue_Clothes_Under:
            "Tops":
                menu:
                    "How about you lose the [RogueX.Chest]?" if RogueX.Chest:
                            $ RogueX.change_face("bemused", 1)
                            if RogueX.SeenChest and Approvalcheck(RogueX, 1100, TabM=2):
                                ch_r "Sure."
                            elif Approvalcheck(RogueX, 1100, TabM=2):
                                ch_r "I guess I don't really mind if you see them. . ."
                            elif RogueX.Over == "hoodie" and Approvalcheck(RogueX, 500, TabM=2):
                                ch_r "I guess this covers enough. . ."
                            elif not RogueX.SeenChest and not Approvalcheck(RogueX, 1100):
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                        if RogueX.Over == "pink top" and Approvalcheck(RogueX, 950, TabM=2):
                                                ch_r "This look is a bit revealing. . ."
                                        elif RogueX.Over == "mesh top":
                                                ch_r "In this top? That would leave nothing to the imagination!"
                                        elif not RogueX.Over:
                                                ch_r "Not without a little coverage, for modesty."
                                        else:
                                                ch_r "I don't think so, [RogueX.Petname]."
                                        return  #jump Rogue_Clothes
                            $ line = RogueX.Chest
                            $ RogueX.Chest = 0
                            if RogueX.Over:
                                "She reaches into her [RogueX.Over] grabs her [line], and pulls it out, dropping it to the ground."
                            else:
                                "She lets her [line] fall to the ground."
                            if (not RogueX.Over or RogueX.Over == "mesh top") and not renpy.showing('DressScreen'):
                                call first_topless(RogueX)

                    "Try on that black tank top." if RogueX.Chest != "tank":
                            $ RogueX.Chest = "tank"
                    "I like that buttoned tank top." if RogueX.Chest != "buttoned tank":# and RogueX.Over != "mesh top":
                            $ RogueX.Chest = "buttoned tank"

                    "I like that sports bra." if RogueX.Chest != "sports bra":
                            if (RogueX.SeenChest and Approvalcheck(RogueX, 600)) or Approvalcheck(RogueX, 900, TabM=2):
                                ch_r "Sure."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "I don't know about wearing it with this. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "sports bra"

                    "I like that black bra." if RogueX.Chest != "bra":
                            if (RogueX.SeenChest and Approvalcheck(RogueX, 600)) or Approvalcheck(RogueX, 1100, TabM=2):
                                ch_r "Sure."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "That's a bit too revealing. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "bra"

                    "I like that blue tube top." if RogueX.Chest != "tube top" and "halloween" in RogueX.History:
                            if (RogueX.SeenChest and Approvalcheck(RogueX, 600)) or Approvalcheck(RogueX, 900, TabM=2):
                                ch_r "Sure."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "I don't know about wearing it with this. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "tube top"

                    "I like that lace bra." if "lace bra" in RogueX.Inventory and RogueX.Chest != "lace bra":
                            if (RogueX.SeenChest and Approvalcheck(RogueX, 800)) or Approvalcheck(RogueX, 1100, TabM=2):
                                ch_r "Sure."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "That's a bit too revealing. . ."
                                    return  #jump Rogue_Clothes
                            $ RogueX.Chest = "lace bra"

                    "I like that bikini top." if RogueX.Chest != "bikini top" and "bikini top" in RogueX.Inventory:
                            if bg_current == "bg_pool":
                                    ch_r "Sure."
                            else:
                                    if RogueX.SeenChest or Approvalcheck(RogueX, 1000, TabM=2):
                                        ch_r "Sure."
                                    else:
                                        call Display_DressScreen(RogueX)
                                        if not _return:
                                            ch_r "I kinda don't feel right about that. . ."
                                            return  #jump Rogue_Clothes
                            $ RogueX.Chest = "bikini top"

                    "Never mind":
                                pass
                jump Rogue_Clothes_Under


            "Hose and stockings options":
                menu:
                    "You could lose the hose." if RogueX.Hose and RogueX.Hose != 'ripped tights' and RogueX.Hose != 'tights':
                            $ RogueX.Hose = 0
                    "The thigh-high hose would look good with that." if RogueX.Hose != "stockings" and RogueX.Legs != "pants":
                            $ RogueX.Hose = "stockings"
                    "The pantyhose would look good with that." if RogueX.Hose != "pantyhose" and RogueX.Legs != "pants":
                            $ RogueX.Hose = "pantyhose"
                    "The stockings would look good with that." if RogueX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in RogueX.Inventory and RogueX.Legs != "pants":
                            $ RogueX.Hose = "stockings and garterbelt"
                    "Maybe just the garterbelt?" if RogueX.Hose != "garterbelt" and "stockings and garterbelt" in RogueX.Inventory and RogueX.Legs != "pants":
                            $ RogueX.Hose = "garterbelt"
                    "Your ripped pantyhose would look good with that." if RogueX.Hose != "ripped pantyhose" and "ripped pantyhose" in RogueX.Inventory and RogueX.Legs != "pants":
                            $ RogueX.Hose = "ripped pantyhose"
                    "Never mind":
                            pass
                jump Rogue_Clothes_Under

            "Panties":
                menu:

                    "You could lose those panties. . ." if RogueX.Panties and RogueX.Panties != "shorts":
                            $ RogueX.change_face("bemused", 1)
                            if (RogueX.SeenPussy and Approvalcheck(RogueX, 900)) and not RogueX.Taboo: # You've seen her pussy
                                if Approvalcheck(RogueX, 850, "L", TabM=2):
                                    ch_r "Well aren't you cheeky. . ."
                                elif Approvalcheck(RogueX, 500, "O", TabM=2):
                                    ch_r "Fine by me."
                                elif Approvalcheck(RogueX, 350, "I", TabM=2):
                                    ch_r "Oooh, naughty."
                                else:
                                    ch_r "Oh, I guess I could."
                            else:                       #You've never seen it
                                if Approvalcheck(RogueX, 1100, "LI", TabM=2):
                                    ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                                elif Approvalcheck(RogueX, 750, "OI", TabM=2):
                                    ch_r "If that's what you want."
                                elif Approvalcheck(RogueX, 500, "I", TabM=2):
                                    ch_r "Oooh, naughty."
                                elif Approvalcheck(RogueX, 1400, TabM=3):
                                    ch_r "Oh, fine. You've been a good boy."
                                else:
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                        $ RogueX.change_face("surprised")
                                        $ RogueX.Brows = "angry"
                                        if RogueX.Taboo > 20:
                                            ch_r "Not in public, [RogueX.Petname]!"
                                        else:
                                            ch_r "Not with you around,[RogueX.Petname]!"
                                        jump Rogue_Clothes
                            $ line = RogueX.Panties
                            $ RogueX.Panties = 0
                            if not RogueX.Legs:
                                "She pulls off her [line], then drops them to the ground."
                                if not renpy.showing('DressScreen'):
                                        call Rogue_First_Bottomless
                            elif Approvalcheck(RogueX, 1200, TabM=4):
                                $ temp = RogueX.Legs
                                $ RogueX.Legs = 0
                                pause 0.5
                                $ RogueX.Legs = temp
                                "She pulls off her [RogueX.Legs] and [line], then pulls the [RogueX.Legs] back on."
                                $ primary_action = 1
                                call Rogue_First_Bottomless(1)
                            elif RogueX.Legs == "skirt":
                                "She reaches under her skirt and pulls her [line] off."
                            else:
                                $ RogueX.Blush = 1
                                "She steps away a moment and then comes back."
                                $ RogueX.Blush = 0
                            $ line = 0

                    "Why don't you wear the green panties instead?" if RogueX.Panties and RogueX.Panties != "green panties":
                            if Approvalcheck(RogueX, 1000, TabM=3):
                                ch_r "Sure, ok."
                                $ RogueX.Panties = "green panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Heh, no, I think I'll stick with these, thanks."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                    ch_r "I think I'll choose my own underwear, thank you."
                                else:
                                        $ RogueX.Panties = "green panties"

                    "Why don't you wear the black panties instead?" if RogueX.Panties and RogueX.Panties != "black panties":
                            if Approvalcheck(RogueX, 1100, TabM=3):
                                ch_r "Sure."
                                $ RogueX.Panties = "black panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Heh, no, I think I'll stick with these, thanks."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                        ch_r "I don't see how that's any business of yours, [RogueX.Petname]."
                                else:
                                        $ RogueX.Panties = "black panties"

                    "Why don't you wear the lace panties instead?" if "lace panties" in RogueX.Inventory and RogueX.Panties and RogueX.Panties != "lace panties":
                            if Approvalcheck(RogueX, 1200, TabM=3):
                                ch_r "Sure."
                                $ RogueX.Panties = "lace panties"
                            elif RogueX.Panties == "shorts":
                                ch_r "Heh, no, I think I'll stick with these, thanks."
                            else:
                                call Display_DressScreen(RogueX)
                                if not _return:
                                        ch_r "I don't see how that's any business of yours, [RogueX.Petname]."
                                else:
                                        $ RogueX.Panties = "lace panties"

                    "I like those bikini bottoms." if RogueX.Panties != "bikini bottoms" and "bikini bottoms" in RogueX.Inventory:
                            if bg_current == "bg_pool":
                                ch_r "Sure."
                                $ RogueX.Panties = "bikini bottoms"
                            else:
                                if Approvalcheck(RogueX, 1000, TabM=2):
                                    ch_r "Sure."
                                    $ RogueX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(RogueX)
                                    if not _return:
                                            ch_r "I kinda don't feel right about that. . ."
                                    else:
                                            $ RogueX.Panties = "bikini bottoms"
                    "You know, you could wear some panties with that. . ." if not RogueX.Panties:
                            $ RogueX.change_face("bemused", 1)
                            if RogueX.Legs and (RogueX.love+RogueX.obedience) <= (1.5 * RogueX.inhibition):
                                $ RogueX.Mouth = "smile"
                                ch_r "No thanks, [RogueX.Petname]."
                                menu:
                                    "Fine by me":
                                        jump Rogue_Clothes
                                    "I insist, put some on.":
                                        if (RogueX.love+RogueX.obedience) <= RogueX.inhibition:
                                            $ RogueX.change_face("angry")
                                            ch_r "Well too bad."
                                            jump Rogue_Clothes
                                        else:
                                            $ RogueX.change_face("sadside")
                                            ch_r "Well! Fine."
                            menu:
                                extend ""
                                "How about the green ones?":
                                    ch_r "Sure, ok."
                                    $ RogueX.Panties = "green panties"
                                "How about the black ones?":
                                    ch_r "Alright."
                                    $ RogueX.Panties  = "black panties"
                                "How about the lace ones?" if "lace panties" in RogueX.Inventory:
                                    ch_r "Alright."
                                    $ RogueX.Panties  = "lace panties"

                    "Never mind":
                            pass
                jump Rogue_Clothes_Under
            "Never mind":
                            return
    return
    #end loop
    #jump Rogue_Clothes
    #End of Rogue Underwear

    menu Rogue_Clothes_Misc:
        #Misc
        "Dry hair." if RogueX.Hair == "wet":
                ch_p "Maybe dry out your hair."
                if Approvalcheck(RogueX, 600):
                        ch_r "Ok."
                        $ RogueX.Hair = "evo"
                else:
                        ch_r "I kinda prefer this look."

        "Wet Look hair." if RogueX.Hair != "wet":
                ch_p "You should go for that wet look with your hair."
                if Approvalcheck(RogueX, 800):
                        ch_r "Hmm?"
                        $ RogueX.Hair = "wet"
                        "She wanders off for a minute and comes back."
                        ch_r "Like this?"
                else:
                        ch_r "Not really into that."

        "Party hair style." if RogueX.Hair != "cosplay" and "halloween" in RogueX.History:
                ch_p "I liked the hair you had at the party."
                if Approvalcheck(RogueX, 600):
                        ch_r "Oh, ok."
                        $ RogueX.Hair = "cosplay"
                else:
                        ch_r "I kinda prefer this look."
        "Original hair style." if RogueX.Hair == "cosplay":
                ch_p "I liked your original hair style."
                if Approvalcheck(RogueX, 600):
                        ch_r "Oh, ok."
                        $ RogueX.Hair = "evo"
                else:
                        ch_r "I kinda prefer this look."

        "Grow pubes" if not RogueX.Pubes:
                ch_p "You know, I like some nice hair down there. Maybe grow it out."
                if "pubes" in RogueX.Todo:
                        $ RogueX.change_face("bemused", 1)
                        ch_r "Yeah, I know, [RogueX.Petname]. It doesn't grow out overnight!"
                else:
                        $ RogueX.change_face("bemused", 1)
                        $ Approval = Approvalcheck(RogueX, 1150, TabM=0)

                        if Approvalcheck(RogueX, 850, "L", TabM=0) or (Approval and RogueX.love > RogueX.obedience):
                            ch_r "Well. . . if that's how you like it. . ."
                        elif Approvalcheck(RogueX, 500, "O", TabM=0) or (Approval and RogueX.obedience > RogueX.inhibition):
                            ch_r "If that's what you want."
                        elif Approvalcheck(RogueX, 500, "I", TabM=0) or Approval:
                            ch_r "Heh, I like a man knows what he wants, [RogueX.Petname]."
                        else:
                            $ RogueX.change_face("surprised")
                            $ RogueX.Brows = "angry"
                            ch_r "Well I don't see how that's any of your business, [RogueX.Petname]."
                            return  #jump Rogue_Clothes
                        $ RogueX.Todo.append("pubes")
                        $ RogueX.PubeC = 6

        "Shave pubes" if RogueX.Pubes == 1:
                ch_p "I like it waxed clean down there."
                $ RogueX.change_face("bemused", 1)
                if "shave" in RogueX.Todo:
                        ch_r "I know, I'll get on that. Not right this second, obviously."
                else:
                        $ Approval = Approvalcheck(RogueX, 1150, TabM=0)
                        if Approvalcheck(RogueX, 850, "L", TabM=0) or (Approval and RogueX.love > RogueX.obedience):
                            ch_r "I can keep it tidy if you like. . ."
                        elif Approvalcheck(RogueX, 500, "O", TabM=0) or (Approval and RogueX.obedience > RogueX.inhibition):
                            ch_r "I'll take care of it."
                        elif Approvalcheck(RogueX, 500, "I", TabM=0) or Approval:
                            ch_r "You better earn it, [RogueX.Petname]."
                        else:
                            $ RogueX.change_face("surprised")
                            $ RogueX.Brows = "angry"
                            ch_r "I don't see how that's any of your beeswax, [RogueX.Petname]."
                            return  #jump Rogue_Clothes
                        $ RogueX.Todo.append("shave")
        "Piercings. [[See what she looks like without them first] (locked)" if not RogueX.SeenPussy and not RogueX.SeenChest:
                        pass

        "Add ring piercings." if RogueX.Pierce != "ring" and (RogueX.SeenPussy or RogueX.SeenChest):
                ch_p "You know, you'd look really nice with some ring body piercings."
                if "ring" in RogueX.Todo:
                    ch_r "Yeah, I know, I'll get to it."
                else:
                    $ RogueX.change_face("bemused", 1)
                    $ Approval = Approvalcheck(RogueX, 1350, TabM=0)
                    if Approvalcheck(RogueX, 950, "L", TabM=0) or (Approval and RogueX.love > RogueX.obedience):
                        ch_r "You really like those? Well, I suppose. . ."
                    elif Approvalcheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.obedience > RogueX.inhibition):
                        ch_r "I'll go get that taken care of."
                    elif Approvalcheck(RogueX, 600, "I", TabM=0) or Approval:
                        ch_r "I've always kind of liked the look of those. . ."
                    else:
                        $ RogueX.change_face("surprised")
                        $ RogueX.Brows = "angry"
                        ch_r "I don't see how that's any of your beeswax, [RogueX.Petname]."
                        return  #jump Rogue_Clothes
                    $ RogueX.Todo.append("ring")

        "Add barbell piercings." if RogueX.Pierce != "barbell" and (RogueX.SeenPussy or RogueX.SeenChest):
                ch_p "You know, you'd look really nice with some barbell body piercings."
                if "barbell" in RogueX.Todo:
                    ch_r "Yeah, I know, I'll get to it."
                else:
                    $ RogueX.change_face("bemused", 1)
                    $ Approval = Approvalcheck(RogueX, 1350, TabM=0)
                    if Approvalcheck(RogueX, 900, "L", TabM=0) or (Approval and RogueX.love > RogueX.obedience):
                        ch_r "You really like those? Well, I suppose. . ."
                    elif Approvalcheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.obedience > RogueX.inhibition):
                        ch_r "I'll go get that taken care of."
                    elif Approvalcheck(RogueX, 600, "I", TabM=0) or Approval:
                        ch_r "I've always kind of liked the look of those. . ."
                    else:
                        $ RogueX.change_face("surprised")
                        $ RogueX.Brows = "angry"
                        ch_r "I don't see how that's any of your beeswax, [RogueX.Petname]."
                        return  #jump Rogue_Clothes
                    $ RogueX.Todo.append("barbell")
                    $ RogueX.Pierce = "barbell"

        "Remove piercings." if RogueX.Pierce:
                ch_p "You know, you'd look better without those piercings."
                $ RogueX.change_face("bemused", 1)
                $ Approval = Approvalcheck(RogueX, 1350, TabM=0)
                if Approvalcheck(RogueX, 950, "L", TabM=0) or (Approval and RogueX.love > RogueX.obedience):
                    ch_r "You really think so? I guess I could lose them. . ."
                elif Approvalcheck(RogueX, 600, "O", TabM=0) or (Approval and RogueX.obedience > RogueX.inhibition):
                    ch_r "I'll take them out then."
                elif Approvalcheck(RogueX, 600, "I", TabM=0) or Approval:
                    ch_r "I guess I prefered not having them in. . ."
                else:
                    $ RogueX.change_face("surprised")
                    $ RogueX.Brows = "angry"
                    ch_r "I'll keep them, if you don't mind."
                    return  #jump Rogue_Clothes
                $ RogueX.Pierce = 0

        "Add spiked collar." if RogueX.Neck != "spiked collar":
                        $ RogueX.Neck = "spiked collar"
        "Remove spiked collar." if RogueX.Neck == "spiked collar":
                        $ RogueX.Neck = 0

        "Gloves on." if not RogueX.Arms:
                        $ RogueX.Arms = "gloves"
        "Gloves off." if RogueX.Arms:
                        $ RogueX.Arms = 0

        "Never mind":
                pass
    return
    #jump Rogue_Clothes
    #End of Rogue Misc Wardrobe

    return
