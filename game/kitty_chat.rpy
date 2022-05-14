label Kitty_Relationship: #rkelj
    while True:
        menu:
            ch_k "What did you want to talk about?"
            "Do you want to be my girlfriend?" if KittyX not in Player.Harem and "ex" not in KittyX.Traits:
                    $ KittyX.daily_history.append("relationship")
                    if "asked boyfriend" in KittyX.daily_history and "angry" in KittyX.daily_history:
                            $ KittyX.change_face("angry", 1)
                            ch_k "For real, buzz off."
                            return
                    elif "asked boyfriend" in KittyX.daily_history:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Still \"nope.\""
                            return
                    elif KittyX.Break[0]:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Not while you're dating her. . ."
                            if Player.Harem:
                                    $ KittyX.daily_history.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "I'm not anymore."

                    $ KittyX.daily_history.append("asked boyfriend")

                    if Player.Harem and "KittyYes" not in Player.Traits:
                        if len(Player.Harem) >= 2:
                            ch_k "I don't think they'd be ok with that, [KittyX.Petname]."
                        else:
                            ch_k "I don't think [Player.Harem[0].name] would be ok with that, [KittyX.Petname]."
                        return

                    if KittyX.Event[5]:
                            $ KittyX.change_face("bemused", 1)
                            ch_k "I {i}did{/i} ask you about that. . ."
                    else:
                            $ KittyX.change_face("surprised", 2)
                            ch_k "I don't know, [KittyX.Petname]. . ."
                            $ KittyX.change_face("smile", 1)

                    call Kitty_OtherWoman

                    if KittyX.love >= 800:
                            $ KittyX.change_face("surprised", 1)
                            $ KittyX.Mouth = "smile"
                            $ KittyX.change_stat("love", 200, 40)
                            ch_k "YES!"
                            if "boyfriend" not in KittyX.Petnames:
                                        $ KittyX.Petnames.append("boyfriend")
                            if "KittyYes" in Player.Traits:
                                    $ Player.Traits.remove("KittyYes")
                            $ Player.Harem.append(KittyX)
                            call Harem_Initiation
                            "[KittyX.name] leaps in and kisses you deeply."
                            $ KittyX.change_face("kiss", 1)
                            $ KittyX.Kissed += 1
                    elif KittyX.obedience >= 500:
                            $ KittyX.change_face("perplexed")
                            ch_k "Maybe not so much \"dating\". . ."
                    elif KittyX.inhibition >= 500:
                            $ KittyX.change_face("smile")
                            ch_k "That's not[KittyX.like]where I'm at right now?"
                    else:
                            $ KittyX.change_face("perplexed", 1)
                            ch_k "I don't really feel that way about you right now, [KittyX.Petname]."

            "Do you want to get back together?" if "ex" in KittyX.Traits:
                    $ KittyX.daily_history.append("relationship")
                    if "asked boyfriend" in KittyX.daily_history and "angry" in KittyX.daily_history:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Seriously, buzz off."
                            return
                    elif "asked boyfriend" in KittyX.daily_history:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Still no."
                            return

                    $ KittyX.daily_history.append("asked boyfriend")

                    if Player.Harem and "KittyYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_k "I don't think they'd be ok with that, [KittyX.Petname]."
                            else:
                                ch_k "I don't think [Player.Harem[0].name] would be ok with that, [KittyX.Petname]."
                            return

                    $ counter = 0
                    call Kitty_OtherWoman

                    if KittyX.love >= 800:
                            $ KittyX.change_face("surprised", 1)
                            $ KittyX.Mouth = "smile"
                            $ KittyX.change_stat("love", 90, 5)
                            ch_k "Well, I guess, sure!"
                            if "boyfriend" not in KittyX.Petnames:
                                        $ KittyX.Petnames.append("boyfriend")
                            $ KittyX.Traits.remove("ex")
                            if "KittyYes" in Player.Traits:
                                    $ Player.Traits.remove("KittyYes")
                            $ Player.Harem.append(KittyX)
                            call Harem_Initiation
                            "[KittyX.name] leaps in and kisses you deeply."
                            $ KittyX.change_face("kiss", 1)
                            $ KittyX.Kissed += 1
                    elif KittyX.love >= 600 and ApprovalCheck(KittyX, 1500):
                            $ KittyX.change_face("smile", 1)
                            $ KittyX.change_stat("love", 90, 5)
                            ch_k "Um, ok, I guess."
                            if "boyfriend" not in KittyX.Petnames:
                                        $ KittyX.Petnames.append("boyfriend")
                            $ KittyX.Traits.remove("ex")
                            if "KittyYes" in Player.Traits:
                                    $ Player.Traits.remove("KittyYes")
                            $ Player.Harem.append(KittyX)
                            call Harem_Initiation
                            $ KittyX.change_face("kiss", 1)
                            "[KittyX.name] gives you a quick kiss."
                            $ KittyX.change_face("smile", 1)
                            $ KittyX.Kissed += 1
                    elif KittyX.obedience >= 500:
                            $ KittyX.change_face("sad")
                            ch_k "I think we're better like this."
                    elif KittyX.inhibition >= 500:
                            $ KittyX.change_face("perplexed")
                            ch_k "I kind of like what we have right now."
                    else:
                            $ KittyX.change_face("perplexed", 1)
                            ch_k "I'm not ready to get burned again."

                    # End Back Together

            "I wanted to ask about [[another girl]" if KittyX in Player.Harem:
                        call AskDateOther

            "I think we should break up." if KittyX in Player.Harem:
                        if "breakup talk" in KittyX.recent_history:
                                ch_k "We were {i}just{/i} over this, not even funny."
                        elif "breakup talk" in KittyX.daily_history:
                                ch_k "I don't want to do this again today, [KittyX.Petname]."
                        else:
                                call Breakup(KittyX)


            "About that talk we had before. . .":
                menu:
                        "When you said you loved me. . ." if "lover" not in KittyX.Traits and KittyX.Event[6] >= 20:
                                call Kitty_love_Redux

                        "You said you wanted me to be more in control?" if "sir" not in KittyX.Petnames and "sir" in KittyX.History:
                                if "asked sub" in KittyX.recent_history:
                                        ch_k "We[KittyX.like]{i}just{/i} went over this."
                                elif "asked sub" in KittyX.daily_history:
                                        ch_k "I think you made yourself {i}perfectly{/i} clear earlier. . ."
                                else:
                                        call Kitty_Sub_Asked
                        "You said you wanted me to be your Master?" if "master" not in KittyX.Petnames and "master" in KittyX.History:
                                if "asked sub" in KittyX.recent_history:
                                        ch_k "We[KittyX.like]{i}just{/i} went over this."
                                elif "asked sub" in KittyX.daily_history:
                                        ch_k "I think you made yourself {i}perfectly{/i} clear earlier. . ."
                                else:
                                        call Kitty_Sub_Asked

                        "About that gift you wanted to get [LauraX.name]. . ." if "dress1" in LauraX.History and "dress2" not in LauraX.History and "dress3" not in LauraX.History:
                                call Laura_Dressup2

                        "Never mind":
                                pass
            "Never Mind":
                return
    return

label Kitty_OtherWoman(counter = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return
    $ counter = int((KittyX.GirlLikeCheck(Player.Harem[0]) - 500)/2)

    $ KittyX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_k "But you're with [Player.Harem[0].name] right now, and and all sorts of other girls!"
    else:
        ch_k "But you're with [Player.Harem[0].name]!"
    menu:
        extend ""
        "She said I can be with you too." if "KittyYes" in Player.Traits:
                if ApprovalCheck(KittyX, 1800, Bonus = counter):
                    $ KittyX.change_face("smile", 1)
                    if KittyX.love >= KittyX.obedience:
                            ch_k "Just so long as we can be together, I can share."
                    elif KittyX.obedience >= KittyX.inhibition:
                            ch_k "I'm ok with that if she is."
                    else:
                            ch_k "Yeah, I mean I guess so."
                else:
                    $ KittyX.change_face("angry", 1)
                    ch_k "Well maybe she did, but I don't want to share."
                    $ renpy.pop_call()
                    #This causes it to jump past the previous menu on the return

        "I could ask if she'd be ok with me dating you both." if "KittyYes" not in Player.Traits:
                if ApprovalCheck(KittyX, 1800, Bonus = counter):
                        $ KittyX.change_face("smile", 1)
                        if KittyX.love >= KittyX.obedience:
                            ch_k "Just so long as we can be together, I can share."
                        elif KittyX.obedience >= KittyX.inhibition:
                            ch_k "I'm ok with that if she is."
                        else:
                            ch_k "Yeah, I mean I guess so."
                        ch_k "Go ask her, and let me know what she thinks in the morning."
                else:
                        $ KittyX.change_face("angry", 1)
                        ch_k "Well maybe she did, but I don't want to share."
                $ renpy.pop_call()

        "What she doesn't know won't hurt her.":
                if not ApprovalCheck(KittyX, 1800, Bonus = -counter): #checks if Kitty likes you more than Kitty
                        $ KittyX.change_face("angry", 1)
                        if not ApprovalCheck(KittyX, 1800):
                                ch_k "Well I don't like you that much either."
                        else:
                                ch_k "Well I'm not cool with that, [Player.Harem[0].name]'s a friend of mine."
                        $ renpy.pop_call()
                else:
                        $ KittyX.change_face("smile", 1)
                        if KittyX.love >= KittyX.obedience:
                                ch_k "I really do want to be together with you."
                        elif KittyX.obedience >= KittyX.inhibition:
                                ch_k "If that's how you want it to be."
                        else:
                                ch_k "I suppose that's true."
                        $ KittyX.Traits.append("downlow")

        "I can break it off with her.":
                    $ KittyX.change_face("sad")
                    ch_k "Well then maybe I'll see you tomorrow after you have."
                    $ renpy.pop_call()

        "You're right, I was dumb to ask.":
                    $ KittyX.change_face("sad")
                    ch_k "You think?"
                    $ renpy.pop_call()

    return

label KittyLike:
    menu:
        ch_k "So[KittyX.like]what would you prefer I say then?"
        "Like":
            $ KittyX.like = ", like, "
            $ KittyX.Like = "Like, "
            ch_k "I guess I do[KittyX.like]say that alot, huh?"
        "Um":
            $ KittyX.like = ", um, "
            $ KittyX.Like = "Um, "
            ch_k "[KittyX.Like]if you say so."
        "So, uh":
            $ KittyX.like = ", uh, "
            $ KittyX.Like = "So, "
            ch_k "[KittyX.Like]I guess I could[KittyX.like]use that more."
        "Nyaa":
            if ApprovalCheck(KittyX, 1400):
                $ KittyX.like = ", nyaa, "
                $ KittyX.Like = "Nyaa, "
                ch_k "[KittyX.Like]you are such a dork."
            elif ApprovalCheck(KittyX, 1000, "LO"):
                $ KittyX.like = ", nyaa, "
                $ KittyX.Like = "Nyaa, "
                ch_k "[KittyX.Like]if that's what you want."
            else:
                ch_k "[KittyX.Like]no way, weirdo."
        "Fucking":
            if ApprovalCheck(KittyX, 400, "I"):
                $ KittyX.like = " fucking "
                $ KittyX.Like = "Fucking "
                ch_k "[KittyX.Like]yeah I will."
            elif ApprovalCheck(KittyX, 1000, "LO"):
                $ KittyX.like = " fucking "
                $ KittyX.Like = "Fucking "
                ch_k "If you[KittyX.like]say so."
            else:
                ch_k "I don't fucking think so."
                ch_k ". . .most of the time."
        "Nothing":
            if ApprovalCheck(KittyX, 900, "LO"):
                $ KittyX.like = " "
                $ KittyX.Like = ". . . "
                ch_k "[KittyX.Like] ok . . ."
            else:
                ch_k "I don't[KittyX.like]think I could do that."

    return

label Kitty_About(Check=0): #rkeljs
    if Check not in all_Girls:
            ch_k "Who?"
            return
    ch_k "What do I think about her? Well. . ."
    if Check == RogueX:
            if "poly Rogue" in KittyX.Traits:
                ch_k "You know we're[KittyX.like]close. . ."
            elif KittyX.LikeRogue >= 900:
                ch_k "She's[KittyX.like]really sexy. . ."
            elif KittyX.LikeRogue >= 800:
                ch_k "She's my bestie, and maybe. . ."
            elif KittyX.LikeRogue >= 700:
                ch_k "She's[KittyX.like]my bestie!"
            elif KittyX.LikeRogue >= 600:
                ch_k "We're[KittyX.like]friends and all."
            elif KittyX.LikeRogue >= 500:
                ch_k "She's not[KittyX.like]a jerk or anything."
            elif KittyX.LikeRogue >= 400:
                ch_k "I'm kinda[KittyX.like]over her."
            elif KittyX.LikeRogue >= 300:
                ch_k "That basic bitch gotta go."
            else:
                ch_k "That slut?"
    elif Check == EmmaX:
            if "poly Emma" in KittyX.Traits:
                ch_k "You know we bang, right?"
            elif KittyX.LikeEmma >= 900:
                ch_k "She's got[KittyX.like]really amazing tits. . ."
            elif KittyX.LikeEmma >= 800:
                ch_k "She's really beautiful. . ."
            elif KittyX.LikeEmma >= 700:
                ch_k "I think we've become good friends."
            elif KittyX.LikeEmma >= 600:
                ch_k "She's[KittyX.like]my favorite teacher."
            elif KittyX.LikeEmma >= 500:
                ch_k "She's[KittyX.like]OK."
            elif KittyX.LikeEmma >= 400:
                ch_k "She gives out[KittyX.like]way too much homework."
            elif KittyX.LikeEmma >= 300:
                ch_k "Ugh, that witch."
            else:
                ch_k "That whore?"
    elif Check == LauraX:
            if "poly Laura" in KittyX.Traits:
                ch_k "You know we[KittyX.like]make out sometimes. . ."
            elif KittyX.LikeLaura >= 900:
                ch_k "She's[KittyX.like]such an animal. . ."
            elif KittyX.LikeLaura >= 800:
                ch_k "We're pretty tight lately. . ."
            elif KittyX.LikeLaura >= 700:
                ch_k "She's[KittyX.like]a really good friend."
            elif KittyX.LikeLaura >= 600:
                ch_k "We're[KittyX.like]teammates."
            elif KittyX.LikeLaura >= 500:
                ch_k "She's not[KittyX.like]a total jerk."
            elif KittyX.LikeLaura >= 400:
                ch_k "I'm kinda[KittyX.like]done with her."
            elif KittyX.LikeLaura >= 300:
                ch_k "Jungle girl?"
            else:
                ch_k "Bitch in heat."
    elif Check == JeanX:
            if "poly Jean" in KittyX.Traits:
                ch_k "You know we're[KittyX.like]close. . ."
            elif KittyX.LikeJean >= 900:
                ch_k "She's[KittyX.like]really sexy. . ."
            elif KittyX.LikeJean >= 800:
                ch_k "She's pretty great. . . I think. . ."
            elif KittyX.LikeJean >= 700:
                ch_k "She's[KittyX.like]my bestie!"
            elif KittyX.LikeJean >= 600:
                ch_k "We're[KittyX.like]friends, I guess."
            elif KittyX.LikeJean >= 500:
                ch_k "She's not[KittyX.like]-so- bad. . ."
            elif KittyX.LikeJean >= 400:
                ch_k "I'm kinda[KittyX.like]done with her drama."
            elif KittyX.LikeJean >= 300:
                ch_k "She is[KittyX.like]-so- dramatic!"
            else:
                ch_k "That bitch?"
    elif Check == StormX:
            if "poly Storm" in KittyX.Traits:
                ch_k "We. . . do kinda have sex?"
            elif KittyX.LikeStorm >= 900:
                ch_k "She's got[KittyX.like]totally thicc. . ."
            elif KittyX.LikeStorm >= 800:
                ch_k "She's really amazing. . ."
            elif KittyX.LikeStorm >= 700:
                ch_k "We're[KittyX.like]close friends."
            elif KittyX.LikeStorm >= 600:
                ch_k "She's[KittyX.like]my favorite teacher."
            elif KittyX.LikeStorm >= 500:
                ch_k "She's[KittyX.like]OK."
            elif KittyX.LikeStorm >= 400:
                ch_k "She gives out[KittyX.like]way too much homework."
            elif KittyX.LikeStorm >= 300:
                ch_k "Ugh, that bitch."
            else:
                ch_k "That whore?"
    elif Check == JubesX:
            if "poly Jubes" in KittyX.Traits:
                ch_k "You know we[KittyX.like]make out sometimes. . ."
            elif KittyX.LikeJubes >= 900:
                ch_k "She's[KittyX.like]such a beast. . ."
            elif KittyX.LikeJubes >= 800:
                ch_k "We're pretty tight lately. . ."
            elif KittyX.LikeJubes >= 700:
                ch_k "She's[KittyX.like]a really good friend."
            elif KittyX.LikeJubes >= 600:
                ch_k "We're[KittyX.like]teammates."
            elif KittyX.LikeJubes >= 500:
                ch_k "She's not[KittyX.like]a total jerk."
            elif KittyX.LikeJubes >= 400:
                ch_k "I'm kinda[KittyX.like]done with her."
            elif KittyX.LikeJubes >= 300:
                ch_k "Bite girl?"
            else:
                ch_k "Bitch in heat."

    return

label Kitty_Monogamy:
        #called from Kitty_Settings to ask her not to hook up wiht other girls
        menu:
            "Could you not hook up with other girls?" if "mono" not in KittyX.Traits:
                    if KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ KittyX.change_face("sly",1)
                            if "mono" not in KittyX.daily_history:
                                    $ KittyX.change_stat("obedience", 90, -2)
                            ch_k "I[KittyX.like]appreciate the interest, but you aren't around enough. . ."
                            return
                    elif ApprovalCheck(KittyX, 1100, "LO", TabM=0) and KittyX.love >= KittyX.obedience:
                            #she cares
                            $ KittyX.change_face("sly",1)
                            if "mono" not in KittyX.daily_history:
                                    $ KittyX.change_stat("love", 90, 1)
                            ch_k "Aw, is someone jellie?"
                            ch_k "I guess I could take care of myself. . ."
                    elif ApprovalCheck(KittyX, 600, "O", TabM=0):
                            #she is obedient
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "If you want. . ."
                    else:
                            #she doesn't care
                            $ KittyX.change_face("sly",1,Brows="confused")
                            ch_k "I'll hook up with who I want!"
                            return
                    if "mono" not in KittyX.daily_history:
                            $ KittyX.change_stat("obedience", 90, 3)
                    $ KittyX.AddWord(1,0,"mono") #Daily
                    $ KittyX.Traits.append("mono")
            "Don't hook up with other girls." if "mono" not in KittyX.Traits:
                    if ApprovalCheck(KittyX, 800, "O", TabM=0):
                            #she is obedient
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "Ok."
                    elif KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ KittyX.change_face("sly",1)
                            if "mono" not in KittyX.daily_history:
                                    $ KittyX.change_stat("obedience", 90, -2)
                            ch_k "I[KittyX.like]appreciate the interest, but you aren't around enough. . ."
                            return
                    elif ApprovalCheck(KittyX, 500, "O", TabM=0):
                            #she is obedient
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "If you want. . ."
                    elif ApprovalCheck(KittyX, 1200, "LO", TabM=0):
                            #she cares
                            $ KittyX.change_face("sly",1)
                            ch_k "Rude much?"
                            ch_k "Fine, I'll do it for you. . ."
                    else:
                            #she doesn't care
                            $ KittyX.change_face("sly",1,Brows="confused")
                            ch_k "I'll hook up with who I want!"
                            return
                    if "mono" not in KittyX.daily_history:
                            $ KittyX.change_stat("obedience", 90, 3)
                    $ KittyX.AddWord(1,0,"mono") #Daily
                    $ KittyX.Traits.append("mono")
            "It's ok if you hook up with other girls." if "mono" in KittyX.Traits:
                    if ApprovalCheck(KittyX, 650, "O", TabM=0):
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "Right, gotcha."
                    elif ApprovalCheck(KittyX, 800, "L", TabM=0):
                            $ KittyX.change_face("sly",1)
                            ch_k "Not like you'd give me the time to do that. . ."
                            ch_k "right?"
                    else:
                            $ KittyX.change_face("sly",1,Brows="confused")
                            if "mono" not in KittyX.daily_history:
                                    $ KittyX.change_stat("love", 90, -2)
                            ch_k "You're not the boss of my pussy!"
                    if "mono" not in KittyX.daily_history:
                            $ KittyX.change_stat("obedience", 90, 3)
                    if "mono" in KittyX.Traits:
                            $ KittyX.Traits.remove("mono")
                    $ KittyX.AddWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return

label Kitty_Jumped:
        #called from Kitty_Settings to ask her not to jump you
        ch_p "Hey, Remember that time you threw yourself at me?"
        $ KittyX.change_face("sly",1,Brows="confused")
        menu:
            ch_k "Um. . . I guess?"
            "Could you maybe just ask instead?" if "chill" not in KittyX.Traits:
                    if KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ KittyX.change_face("surprised",2)
                            if "chill" not in KittyX.daily_history:
                                    $ KittyX.change_stat("obedience", 90, -2)
                            ch_k "Well- Well maybe spend some more time with me!"
                            $ KittyX.change_face("angry",1,Eyes="side")
                            return
                    elif ApprovalCheck(KittyX, 900, "LO", TabM=0) and KittyX.love >= KittyX.obedience:
                            #she cares
                            $ KittyX.change_face("sadside",1)
                            if "chill" not in KittyX.daily_history:
                                    $ KittyX.change_stat("love", 90, 1)
                            ch_k "Sorry, [KittyX.Petname]. . ."
                            ch_k "I can't keep my hands to myself. . ."
                            ch_k "I'll try though. . ."
                    elif ApprovalCheck(KittyX, 400, "O", TabM=0):
                            #she is obedient
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "I guess. . ."
                    else:
                            #she doesn't care
                            $ KittyX.change_face("sly",1)
                            ch_k "I can't keep my hands to myself. . ."
                            return
                    if "chill" not in KittyX.daily_history:
                            $ KittyX.change_stat("obedience", 90, 3)
                    $ KittyX.AddWord(1,0,"chill") #Daily
                    $ KittyX.Traits.append("chill")
            "Don't bother me like that." if "chill" not in KittyX.Traits:
                    if ApprovalCheck(KittyX, 900, "O", TabM=0):
                            #she is obedient
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "Ok."
                    elif KittyX.Thirst >= 60 and not ApprovalCheck(KittyX, 600, "O", TabM=0):
                            #she's too thirsty
                            $ KittyX.change_face("angry",1)
                            if "chill" not in KittyX.daily_history:
                                    $ KittyX.change_stat("obedience", 90, -2)
                            ch_k "Don't keep me waiting then!"
                            return
                    elif ApprovalCheck(KittyX, 400, "O", TabM=0):
                            #she is obedient
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "Fine. . ."
                    elif ApprovalCheck(KittyX, 500, "LO", TabM=0) and not ApprovalCheck(KittyX, 500, "I", TabM=0):
                            #she cares
                            $ KittyX.change_face("sly",1)
                            ch_k "Rude."
                            ch_k ". . . I'll try though. . ."
                    else:
                            #she doesn't care
                            $ KittyX.change_face("sly",1,Brows="confused")
                            ch_k "I don't know. I guess we'll see. . ."
                            return
                    if "chill" not in KittyX.daily_history:
                            $ KittyX.change_stat("obedience", 90, 3)
                    $ KittyX.AddWord(1,0,"chill") #Daily
                    $ KittyX.Traits.append("chill")
            "Knock yourself out.":
                    if ApprovalCheck(KittyX, 800, "L", TabM=0):
                            $ KittyX.change_face("sly",1)
                            ch_k "Roger, roger. . ."
                    elif ApprovalCheck(KittyX, 700, "O", TabM=0):
                            $ KittyX.change_face("sly",1,Eyes="side")
                            ch_k "You bet!"
                    else:
                            $ KittyX.change_face("sly",1,Brows="confused")
                            if "chill" not in KittyX.daily_history:
                                    $ KittyX.change_stat("love", 90, -2)
                            ch_k "I don't know."
                            ch_k "If I've got the time."
                            ch_k "I guess."
                    if "chill" not in KittyX.daily_history:
                            $ KittyX.change_stat("obedience", 90, 3)
                    if "chill" in KittyX.Traits:
                            $ KittyX.Traits.remove("chill")
                    $ KittyX.AddWord(1,0,"chill") #Daily
            "Um, never mind.":
                pass
        return

label Kitty_Hungry:
    if KittyX.Chat[3]:
        ch_k "You know, a kitty does like her milk. . ."
    elif KittyX.Chat[2]:
        ch_k "You know, that serum of yours really has a kick to it. You should market that stuff!"
    else:
        ch_k "You know, a kitty does like her milk. . ."
    $ KittyX.Traits.append("hungry")
    return

label Kitty_SexChat:
    $ line = "Yeah, what did you want to talk about?" if not line else line
    while True:
            menu:
                ch_k "[line]"
                "My favorite thing to do is. . .":
                    if "setfav" in KittyX.daily_history:
                        ch_k "Yeah, I know. You just told me earlier."
                    else:
                        menu:
                            "Sex.":
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "sex":
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "Yeah, I know that. . ."
                                        elif KittyX.Favorite == "sex":
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 10)
                                            ch_k "I really like it too!"
                                        elif KittyX.Sex >= 5:
                                            ch_k "Well I don't mind that."
                                        elif not KittyX.Sex:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who's fucking you? Is it Ms. Frost?!"
                                        else:
                                            $ KittyX.change_face("bemused")
                                            ch_k "Heh, um, yeah, it's nice. . ."
                                        $ KittyX.PlayerFav = "sex"

                            "Anal.":
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "anal":
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "So you've said. . ."
                                        elif KittyX.Favorite == "anal":
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 10)
                                            ch_k "I love it too!"
                                        elif KittyX.Anal >= 10:
                                            ch_k "Yeah, it's. . . nice. . ."
                                        elif not KittyX.Anal:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who's fucking you? Is it Ms. Frost?!"
                                        else:
                                            $ KittyX.change_face("bemused",Eyes="side")
                                            ch_k "Heh, heh, yeah, um, it's ok. . ."
                                        $ KittyX.PlayerFav = "anal"

                            "Blowjobs.":
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "blow":
                                            $ KittyX.change_stat("lust", 80, 3)
                                            ch_k "Yeah, I know."
                                        elif KittyX.Favorite == "blow":
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "I love your dick!"
                                        elif KittyX.Blow >= 10:
                                            ch_k "Yeah, you're pretty tasty."
                                        elif not KittyX.Blow:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who's sucking your dick?! Is it Ms. Frost?!"
                                        else:
                                            $ KittyX.change_face("bemused")
                                            ch_k "I'm. . . getting used to the taste. . ."
                                        $ KittyX.PlayerFav = "blow"

                            "Titjobs.":
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "titjob":
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "Yeah, you've said that before. . ."
                                        elif KittyX.Favorite == "titjob":
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 7)
                                            ch_k "Yeah, I enjoy that too. . ."
                                        elif KittyX.Tit >= 10:
                                            ch_k "It's certainly an interesting experience . . ."
                                        elif not KittyX.Tit:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who's titfucking you? It's Ms. Frost, isn't it!"
                                        else:
                                            $ KittyX.change_face("bemused")
                                            ch_k "That's nice of you to say. . ."
                                            $ KittyX.change_stat("love", 80, 5)
                                            $ KittyX.change_stat("inhibition", 50, 10)
                                        $ KittyX.PlayerFav = "titjob"

                            "Footjobs.":
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "foot":
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "Yeah, you've said that. . ."
                                        elif KittyX.Favorite == "foot":
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 7)
                                            ch_k "You do feel pretty nice. . ."
                                        elif KittyX.Foot >= 10:
                                            ch_k "I like it too . . ."
                                        elif not KittyX.Foot:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who's playing footsie with you? Is it Ms. Frost?!"
                                        else:
                                            $ KittyX.change_face("bemused")
                                            ch_k "Yeah, it's nice. . ."
                                        $ KittyX.PlayerFav = "foot"

                            "Handjobs.":
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "hand":
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "Yeah, you've said that. . ."
                                        elif KittyX.Favorite == "hand":
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 7)
                                            ch_k "You do feel pretty comfy. . ."
                                        elif KittyX.Hand >= 10:
                                            ch_k "I like it too . . ."
                                        elif not KittyX.Hand:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who's jerking you off? Is it Ms. Frost?!"
                                        else:
                                            $ KittyX.change_face("bemused")
                                            ch_k "Yeah, it's nice. . ."
                                        $ KittyX.PlayerFav = "hand"

                            "Feeling you up.":
                                        $ counter = KittyX.FondleB + KittyX.FondleT + KittyX.SuckB + KittyX.Hotdog
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "fondle":
                                            $ KittyX.change_stat("lust", 80, 3)
                                            ch_k "Yeah, I think we're clear on that. . ."
                                        elif KittyX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "I love when you touch me. . ."
                                        elif counter >= 10:
                                            ch_k "Yeah, it's really nice . . ."
                                        elif not counter:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who's letting you feel her up? Is it Ms. Frost?!"
                                        else:
                                            $ KittyX.change_face("bemused")
                                            ch_k "I do like how that feels. . ."
                                        $ KittyX.PlayerFav = "fondle"
                                        $ counter = 0

                            "Kissing you.":
                                        $ KittyX.change_face("sly")
                                        if KittyX.PlayerFav == "kiss you":
                                            $ KittyX.change_stat("love", 90, 3)
                                            ch_k "Such a romantic. . ."
                                        elif KittyX.Favorite == "kiss you":
                                            $ KittyX.change_stat("love", 90, 5)
                                            $ KittyX.change_stat("lust", 80, 5)
                                            ch_k "Hmm, the taste of you on my lips. . ."
                                        elif KittyX.Kissed >= 10:
                                            ch_k "I love kissing you too . . ."
                                        elif not KittyX.Kissed:
                                            $ KittyX.change_face("perplexed")
                                            ch_k "Who are you kissing? Is it Ms. Frost?!"
                                        else:
                                            $ KittyX.change_face("bemused")
                                            ch_k "I like kissing you too. . ."
                                        $ KittyX.PlayerFav = "kiss you"

                        $ KittyX.daily_history.append("setfav")

                "What's your favorite thing to do?":
                                if not ApprovalCheck(KittyX, 800):
                                        $ KittyX.change_face("perplexed")
                                        ch_k "Rude."
                                else:
                                        if KittyX.SEXP >= 50:
                                            $ KittyX.change_face("sly")
                                            ch_k "You should know that. . ."
                                        else:
                                            $ KittyX.change_face("bemused")
                                            $ KittyX.Eyes = "side"
                                            ch_k "Hmm, I don't know. . ."


                                        if not KittyX.Favorite or KittyX.Favorite == "kiss":
                                            ch_k "I do love it when we kiss. . ."
                                        elif KittyX.Favorite == "anal":
                                            if KittyX.Anal >= 10:
                                                ch_k "I like when you. . . fuck my ass."
                                            else:
                                                ch_k "I like it. . . in the butt."
                                        elif KittyX.Favorite == "lick ass":
                                                ch_k "I like when you lick my. . . asshole."
                                        elif KittyX.Favorite == "insert ass":
                                                ch_k "I like when you . . . finger my asshole."
                                        elif KittyX.Favorite == "sex":
                                                ch_k "I like when you fuck me."
                                        elif KittyX.Favorite == "lick pussy":
                                                ch_k "I like when you lick my pussy."
                                        elif KittyX.Favorite == "fondle pussy":
                                                ch_k "I like when you finger me."
                                        elif KittyX.Favorite == "blow":
                                                ch_k "I kinda like to suck your cock."
                                        elif KittyX.Favorite == "tit":
                                                ch_k "I don't mind using my tits."
                                        elif KittyX.Favorite == "foot":
                                                ch_k "I kinda like giving footjobs."
                                        elif KittyX.Favorite == "hand":
                                                ch_k "I like jerking you off."
                                        elif KittyX.Favorite == "hotdog":
                                                ch_k "I like it when you grind against me."
                                        elif KittyX.Favorite == "suck breasts":
                                                ch_k "I like it when you suck on my tits."
                                        elif KittyX.Favorite == "fondle breasts":
                                                ch_k "I like it when you feel up my tits."
                                        elif KittyX.Favorite == "fondle thighs":
                                                ch_k "I like it when you massage my thighs."
                                        else:
                                                ch_k "I don't really know. . ."

                                # End Kitty's favorite things.

                "Don't talk as much during sex." if "vocal" in KittyX.Traits:
                        if "setvocal" in KittyX.daily_history:
                            $ KittyX.change_face("perplexed")
                            ch_k "We've been over this."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                                $ KittyX.change_face("bemused")
                                $ KittyX.change_stat("obedience", 90, 1)
                                ch_k "Well, I guess I can be quieter. . ."
                                $ KittyX.Traits.remove("vocal")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.change_face("sadside")
                                $ KittyX.change_stat("obedience", 90, 1)
                                ch_k "Um, ok, [KittyX.Petname]."
                                $ KittyX.Traits.remove("vocal")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.change_face("sly")
                                $ KittyX.change_stat("love", 90, -3)
                                $ KittyX.change_stat("obedience", 50, -1)
                                $ KittyX.change_stat("inhibition", 90, 5)
                                ch_k "You wish, [KittyX.Petname]."
                            else:
                                $ KittyX.change_face("angry")
                                $ KittyX.change_stat("love", 90, -5)
                                $ KittyX.change_stat("obedience", 60, -3)
                                $ KittyX.change_stat("inhibition", 90, 10)
                                ch_k "Oh, am I too {i}chatty{/i} when I'm getting you off?"

                            $ KittyX.daily_history.append("setvocal")
                "Talk dirty to me during sex." if "vocal" not in KittyX.Traits:
                        if "setvocal" in KittyX.daily_history:
                            $ KittyX.change_face("perplexed")
                            ch_k "We've been over this."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                                $ KittyX.change_face("sly")
                                $ KittyX.change_stat("obedience", 90, 2)
                                ch_k "Hmm, ok. . ."
                                $ KittyX.Traits.append("vocal")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.change_face("sadside")
                                $ KittyX.change_stat("obedience", 90, 2)
                                ch_k "I guess I could try, [KittyX.Petname]."
                                $ KittyX.Traits.append("vocal")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.change_face("sly")
                                $ KittyX.change_stat("obedience", 90, 3)
                                ch_k "I guess I could, [KittyX.Petname]."
                                $ KittyX.Traits.append("vocal")
                            else:
                                $ KittyX.change_face("angry")
                                $ KittyX.change_stat("inhibition", 90, 5)
                                ch_k "Hmm, I don't know about that."

                            $ KittyX.daily_history.append("setvocal")
                        # End Kitty Dirty Talk

                "Don't do your own thing as much during sex." if "passive" not in KittyX.Traits:
                        if "initiative" in KittyX.daily_history:
                            $ KittyX.change_face("perplexed")
                            ch_k "We've been over this."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                                $ KittyX.change_face("bemused")
                                $ KittyX.change_stat("obedience", 90, 1)
                                ch_k "Heh, if you insist. . ."
                                $ KittyX.Traits.append("passive")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.change_face("sadside")
                                $ KittyX.change_stat("obedience", 90, 1)
                                ch_k "I'll try to hold back, [KittyX.Petname]."
                                $ KittyX.Traits.append("passive")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.change_face("sly")
                                $ KittyX.change_stat("love", 90, -3)
                                $ KittyX.change_stat("obedience", 50, -1)
                                $ KittyX.change_stat("inhibition", 90, 5)
                                ch_k "You wish, [KittyX.Petname]."
                            else:
                                $ KittyX.change_face("angry")
                                $ KittyX.change_stat("love", 90, -5)
                                $ KittyX.change_stat("obedience", 60, -3)
                                $ KittyX.change_stat("inhibition", 90, 10)
                                ch_k "If I feel like it."

                            $ KittyX.daily_history.append("initiative")
                "Take more initiative during sex." if "passive" in KittyX.Traits:
                        if "initiative" in KittyX.daily_history:
                                $ KittyX.change_face("perplexed")
                                ch_k "We've been over this."
                        else:
                            if ApprovalCheck(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                                $ KittyX.change_face("bemused")
                                $ KittyX.change_stat("obedience", 90, 1)
                                ch_k "Heh, I'll see what I can do. . ."
                                $ KittyX.Traits.remove("passive")
                            elif ApprovalCheck(KittyX, 700, "O"):
                                $ KittyX.change_face("sadside")
                                $ KittyX.change_stat("obedience", 90, 1)
                                ch_k "I can do that, [KittyX.Petname]."
                                $ KittyX.Traits.remove("passive")
                            elif ApprovalCheck(KittyX, 600):
                                $ KittyX.change_face("sly")
                                $ KittyX.change_stat("obedience", 90, 3)
                                ch_k "I can try, [KittyX.Petname]."
                                $ KittyX.Traits.remove("passive")
                            else:
                                $ KittyX.change_face("angry")
                                $ KittyX.change_stat("inhibition", 90, 5)
                                ch_k "You're not my supervisor!"

                            $ KittyX.daily_history.append("initiative")

                "About getting Jumped" if "jumped" in KittyX.History:
                        call Kitty_Jumped
                "About when you masturbate":
                        call NoFap(KittyX)

                "Never Mind" if line == "Yeah, what did you want to talk about?":
                        return
                "That's all." if line != "Yeah, what did you want to talk about?":
                        return
            if line == "Yeah, what did you want to talk about?":
                $ line = "Anything else?"
    return

label Kitty_Chitchat(O=0, Options = ["default","default","default"]):
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:

        if KittyX not in Digits:
                if ApprovalCheck(KittyX, 500, "L") or ApprovalCheck(KittyX, 250, "I"):
                    ch_k "You know, I never got around to giving you my number, here you go."
                    $ Digits.append(KittyX)
                    return
                elif ApprovalCheck(KittyX, 250, "O"):
                    ch_k "You know, you should probably have my number, here you go."
                    $ Digits.append(KittyX)
                    return

        if "hungry" not in KittyX.Traits and (KittyX.Swallow + KittyX.Chat[2]) >= 10 and KittyX.Loc == bg_current:  #She's swallowed a lot
                    call Kitty_Hungry
                    return
        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not Taboo or ApprovalCheck(KittyX, 800, "I")):
                    if KittyX.Loc == bg_current and KittyX.Thirst >= 30 and "refused" not in KittyX.daily_history and "quicksex" not in KittyX.daily_history:
                            $ Girl.change_face("smile",2,Brows="sad")
                            ch_k "Hey, um . . . did you want to. . ."
                            ch_k ". . . sex?"
                            call Quick_Sex(KittyX)
                            return

        if KittyX.Event[0] and "key" not in KittyX.Chat:
            $ Options.append("key")
        if "lover" in KittyX.Petnames and ApprovalCheck(KittyX, 900, "L"): # luvy dovey
            $ Options.append("luv")
        if "Kate" in KittyX.names and "Katherine" not in KittyX.names:
            #You don't know Kitty's full name
            $ Options.append("Katherine")
        if KittyX.Lvl >= 3 and "Shadowcat" not in KittyX.names:
            #You don't know Kitty's full name
            $ Options.append("Shadowcat")

        if "mandrill" in Player.Traits and "cologne chat" not in KittyX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.Traits and "cologne chat" not in KittyX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.Traits and "cologne chat" not in KittyX.daily_history:
            $ Options.append("corruption")

        if "seenpeen" in KittyX.History:
            $ Options.append("seenpeen")
        if "topless" in KittyX.History:
            $ Options.append("topless")
        if "bottomless" in KittyX.History:
            $ Options.append("bottomless")

        if KittyX.Date >= 1 and bg_current != "bg_restaurant":
            #if you've dated before
            $ Options.append("dated")
        if "cheek" in KittyX.daily_history and "cheek" not in KittyX.Chat:
            #If you've touched her cheek today
            $ Options.append("cheek")
        if KittyX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "kappa" in Player.History:
            $ Options.append("kappa")
        if "dangerroom" in Player.daily_history:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in KittyX.daily_history:
            #If you've caught Kitty showering today
            $ Options.append("showercaught")
        if "fondle breasts" in KittyX.daily_history or "fondle pussy" in KittyX.daily_history or "fondle ass" in KittyX.daily_history:
            #If you've fondled Kitty today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in KittyX.Inventory and "256 Shades of Grey" in KittyX.Inventory and "Avengers Tower Penthouse" in KittyX.Inventory:
            #If you've given Kitty the books
            if "book" not in KittyX.Chat:
                $ Options.append("booked")
        if "lace bra" in KittyX.Inventory or "lace panties" in KittyX.Inventory:
            #If you've given Kitty the lingerie
            if "lingerie" not in KittyX.Chat:
                $ Options.append("lingerie")
        if KittyX.Hand:
            #If Kitty's given a handjob
            $ Options.append("handy")
        if KittyX.Swallow:
            #If Kitty's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in KittyX.daily_history or "painted" in KittyX.daily_history:
            #If Kitty's been facialed
            $ Options.append("facial")
        if KittyX.Sleep:
            #If Kitty's slept over
            $ Options.append("sleep")
        if KittyX.CreamP or KittyX.CreamA:
            #If Kitty's been creampied
            $ Options.append("creampie")
        if KittyX.Sex or KittyX.Anal:
            #If Kitty's been sexed
            $ Options.append("sexed")
        if KittyX.Anal:
            #If Kitty's been analed
            $ Options.append("anal")

        if (bg_current == "bg_kitty" or bg_current == "bg_player") and "relationship" not in KittyX.daily_history:
            if "lover" not in KittyX.Petnames and KittyX.love >= 950 and KittyX.Event[6] != 20: # KittyX.Event[6]
                $ Options.append("lover?")
            elif "sir" not in KittyX.Petnames and KittyX.obedience >= 500 and "sir" not in KittyX.History: # KittyX.Event[7]
                $ Options.append("sir?")
            elif "daddy" not in KittyX.Petnames and ApprovalCheck(KittyX, 750, "L") and ApprovalCheck(KittyX, 500, "O") and ApprovalCheck(KittyX, 500, "I"): # KittyX.Event[5]
                $ Options.append("daddy?")
            elif "master" not in KittyX.Petnames and KittyX.obedience >= 800 and "sir" in KittyX.Petnames and "master" not in KittyX.History: # KittyX.Event[8]
                $ Options.append("master?")
            elif "sex friend" not in KittyX.Petnames and ApprovalCheck(KittyX, 500, "I"): # KittyX.Event[9]
                $ Options.append("sexfriend?")


        if not ApprovalCheck(KittyX, 300):            #She dislikes you
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one

    if Options[0] == "mandrill":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("confused")
        ch_k "(sniff, sniff). . . is that. . . chimp? . . ."
        $ KittyX.change_face("perplexed", 1)
        ch_k ". . . but it's[KittyX.like]. . . {i}sexy{/i} chimp?"
    elif Options[0] == "purple":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("sly",1)
        ch_k "(sniff, sniff). . . huh, what's that smell? . ."
        ch_k ". . . could I get you something?"
    elif Options[0] == "corruption":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("confused")
        ch_k "(sniff, sniff). . . that's pretty overpowering. . ."
        $ KittyX.change_face("sly")
        ch_k ". . . I may not be able to keep my hands to myself. . ."

    elif Options[0] == "caught": # Xavier's caught you
            if "caught chat" in KittyX.Chat:
                    ch_k "We've really got to stop making a habit of getting caught."
                    if not ApprovalCheck(KittyX, 500, "I"):
                         ch_k "Or not. . ."
            else:
                    ch_k "I did not enjoy getting dragged to the Professor's office like that."
                    if not ApprovalCheck(KittyX, 500, "I"):
                        ch_k "I don't know about doing it in public anymore."
                    else:
                        ch_k "It was kind of hot though. . ."
                    $ KittyX.Chat.append("caught chat")
    elif Options[0] == "key": # you have her key
            if KittyX.SEXP <= 15:
                ch_k "I'm glad you have my key now, just don't use it for any funny business. . ."
            else:
                ch_k "I'm glad you have my key now, maybe you could . . . \"surprise\" me sometime. . ."
            $ KittyX.Chat.append("key")

    elif Options[0] == "cheek":
            #Kitty's response to having her cheek touched.
            ch_k "So,[KittyX.Petname]. . .y'know how you[KittyX.like]kinda just brushed my cheek before?"
            ch_p "Yeah?  Was that okay?"
            $ KittyX.change_face("smile",1)
            ch_k "More than just {i}okay{/i}."
            $ KittyX.Chat.append("cheek")

    elif Options[0] == "dated":
            #Kitty's response to having gone on a date with the Player.
            ch_k "Heya,[KittyX.Petname].  I[KittyX.like]had a lot of fun last night.  We should do that again sometime."

    elif Options[0] == "kissed":
            #Kitty's response to having been kissed by the Player.
            $ KittyX.change_face("sly",1)
            ch_k "[KittyX.Like]. . .anybody ever tell you how good a kisser you are, [KittyX.Petname]?"
            menu:
                extend ""
                "Hey. . .when you're good, you're good.":
                        $ KittyX.change_face("smile",1)
                        ch_k "I think maybe you can show me {i}how{/i} good[KittyX.like]whenever you want."
                "No. You think?":
                        ch_k "Yeah.  I do. [KittyX.Like]a {i}lot{/i}."

    elif Options[0] == "dangerroom":
            #Kitty's response to Player working out in the Danger Room while Kitty is present
            $ KittyX.change_face("sly",1)
            ch_k "Hey,[KittyX.Petname].  I watched you working out in the Danger Room, earlier.  You looked[KittyX.like]{i}so{/i} cute in your X-Men uniform!"

    elif Options[0] == "showercaught":
            #Kitty's response to being caught in the shower.
            if "shower" in KittyX.Chat:
                ch_k "Hope you liked the view earlier. . ."
            else:
                ch_k "So, you run into a lot of people in the shower. . .or just[KittyX.like]me?"
                $ KittyX.Chat.append("shower")
                menu:
                    extend ""
                    "It was a total accident!  I promise!":
                            $ KittyX.change_stat("love", 50, 5)
                            $ KittyX.change_stat("love", 90, 2)
                            if ApprovalCheck(KittyX, 1200):
                                $ KittyX.change_face("sly",1)
                                ch_k "Yeah?  {i}Maybe{/i} you should[KittyX.like]have accidents like that more often."
                            $ KittyX.change_face("smile")
                            ch_k "It's cool, [KittyX.Petname]. Eveybody makes mistakes. . . sometimes."
                    "Just you.":
                            $ KittyX.change_stat("obedience", 40, 5)
                            if ApprovalCheck(KittyX, 1000) or ApprovalCheck(KittyX, 700, "L"):
                                    $ KittyX.change_stat("love", 90, 3)
                                    $ KittyX.change_face("sly",1)
                                    ch_k "You know how to make a girl feel special, [KittyX.Petname]."
                            else:
                                    $ KittyX.change_stat("love", 70, -5)
                                    $ KittyX.change_face("angry")
                                    ch_k "You're {i}such{/i} a creep, [Player.name], y'know that?"
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck(KittyX, 1200):
                                    $ KittyX.change_stat("love", 90, 3)
                                    $ KittyX.change_stat("obedience", 70, 10)
                                    $ KittyX.change_stat("inhibition", 50, 5)
                                    $ KittyX.change_face("sly",1)
                                    ch_k "Hmm. . .next time, we'll have to[KittyX.like]take advantage of the moment."
                            elif ApprovalCheck(KittyX, 800):
                                    $ KittyX.change_stat("obedience", 60, 5)
                                    $ KittyX.change_stat("inhibition", 50, 5)
                                    $ KittyX.change_face("perplexed",2)
                                    ch_k "Wha. . . um. . . okay?"
                                    $ KittyX.Blush = 1
                            else:
                                    $ KittyX.change_stat("love", 50, -10)
                                    $ KittyX.change_stat("love", 80, -10)
                                    $ KittyX.change_stat("obedience", 50, 10)
                                    $ KittyX.change_face("angry")
                                    ch_k "You're such a creep, [KittyX.Petname], y'know that?"

    elif Options[0] == "fondled":
            #Kitty's response to being felt up.
            if KittyX.FondleB + KittyX.FondleP + KittyX.FondleA >= 15:
                ch_k "I want your hands on me."
            else:
                ch_k "You know how you felt me up earlier? I could kinda[KittyX.like]get used to having your hands on me."

    elif Options[0] == "booked":
            #Kitty's response after a Player gives her the books from the shop.
            ch_k "So..I[KittyX.like]read the books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        $ KittyX.change_face("sly",2)
                        ch_k "They were[KittyX.like]. . .{i}interesting{/i}."
                "Good.  You looked like you could use to learn a thing or two from them.":
                        $ KittyX.change_stat("love", 90, -3)
                        $ KittyX.change_stat("obedience", 70, 5)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        $ KittyX.change_face("angry")
                        ch_k "Guess {i}you'll{/i} never find out, huh?"
            $ KittyX.Blush = 1
            $ KittyX.Chat.append("book")

    elif Options[0] == "lingerie":
            #Kitty's response to being given lingerie.
            $ KittyX.change_face("sly",2)
            ch_k "[KittyX.Petname], I wanted to thank you again for the. . .{i}stuff{/i} you bought me. They're so cute!"
            $ KittyX.Blush = 1
            $ KittyX.Chat.append("lingerie")

    elif Options[0] == "handy":
            #Kitty's response after giving the Player a handjob.
            $ KittyX.change_face("sly",2)
            ch_k "I was just thinking about how I[KittyX.like]stroked your cock the other day. . ."
            ch_k "I loved the expression on your face. . .knowing I could[KittyX.like]make you {i}feel{/i} like that."
            $ KittyX.Blush = 1

    elif Options[0] == "blow":
            if "blow" not in KittyX.Chat:
                    #Kitty's response after giving the Player a blowjob.
                    $ KittyX.change_face("sly",2)
                    ch_k "So. . .uhm, be honest with me, [KittyX.Petname]?"
                    ch_k "When I gave you head. . . was it any good?"
                    ch_k "I kinda had a hard time getting all of you into my mouth."
                    menu:
                        extend ""
                        "You were totally amazing.":
                                    $ KittyX.change_stat("love", 90, 5)
                                    $ KittyX.change_stat("inhibition", 60, 10)
                                    $ KittyX.change_face("sexy",1)
                                    ch_k "Awesome.  'Cause I can't wait to try again."
                        "Honestly? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck(KittyX, 300, "I") or not ApprovalCheck(KittyX, 800):
                                    $ KittyX.change_stat("love", 90, -5)
                                    $ KittyX.change_stat("obedience", 60, 10)
                                    $ KittyX.change_stat("inhibition", 50, 10)
                                    $ KittyX.change_face("perplexed",1)
                                    ch_k "Yeah? Well then maybe I'll get some practice in before we do it again."
                                else:
                                    $ KittyX.change_stat("obedience", 70, 15)
                                    $ KittyX.change_stat("inhibition", 50, 5)
                                    $ KittyX.change_face("sexy",1)
                                    ch_k "Yeah? Well, I'm[KittyX.Petname]looking forward our next training session, then."
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                                $ KittyX.change_stat("love", 90, -10)
                                $ KittyX.change_stat("obedience", 60, 10)
                                $ KittyX.change_face("angry",2)
                                ch_k "Guess you're gonna have to[KittyX.like]figure out a way to get it to suck itself then from now on. . .{i}jerk{/i}."
                    $ KittyX.Blush = 1
                    $ KittyX.Chat.append("blow")
            else:
                    $ line = renpy.random.choice(["You know, I kinda like how you taste.",
                            "You're a real jaw-breaker.",
                            "Let me know if you want some more lollipop licks.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_k "[line]"

    elif Options[0] == "swallowed":
            #Kitty's response after swallowing the Player's cum.
            if "swallow" in KittyX.Chat:
                ch_k "I'd like another taste sometime."
            else:
                ch_k "So. . .I was[KittyX.like]just thinking about the other day."
                ch_k "Y'know, that was the first time I[KittyX.like]swallowed."
                $ KittyX.change_face("sly",1)
                ch_k "Not bad. . ."
                $ KittyX.Chat.append("swallow")

    elif Options[0] == "facial":
            #Kitty's response after taking a facial from the Player.
            ch_k "Hey. . .this is gonna sound kinda[KittyX.like]weird, but. . ."
            $ KittyX.change_face("sexy",2)
            ch_k "I feel so {i}sexy{/i} when you cum on my face."
            $ KittyX.Blush = 1

    elif Options[0] == "sleepover":
            #Kitty's response after sleeping with the Player.
            ch_k "I[KittyX.like] totally can't stop thinking about the other night."
            ch_k "It was {i}so{/i} perfect."

    elif Options[0] == "creampie":
            #Another of Kitty's responses after having sex with the Player.
            "[KittyX.name] draws close to you so she can whisper into your ear."
            ch_k "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":
            #A final response from Kitty after having sex with the Player.
            ch_k "So. . .I want you to know something. . ."
            $ KittyX.change_face("sexy",2)
            ch_k ". . .[KittyX.Like]every time I masturbate. . ."
            ch_k "I think about how it felt, with you inside of me."
            $ KittyX.Blush = 1

    elif Options[0] == "anal":
            #Kitty's response after getting anal from the Player.
            $ KittyX.change_face("sly",2)
            ch_k "Y'know. . .after the other night, I'm kinda having trouble[KittyX.like]sitting down."
            $ KittyX.change_face("sexy",2)
            ch_k "{i}Totally{/i} worth it, though."
            $ KittyX.Blush = 1
    elif Options[0] == "kappa":
            #Kitty's response to having failed at project Kappa
            ch_k "You know how Xavier[KittyX.like]caught us last time?"
            ch_k "I bet if we had some dirt on him, we could get him to lay off. . ."
            ch_k "Maybe he has something in his office. . ."
    elif Options[0] == "Shadowcat":
            $ KittyX.names.append("Shadowcat")
            ch_k "You know, in the field I go by \"Shadowcat.\""
            menu:
                extend ""
                "Oh, ok then.":
                        $ KittyX.change_face("perplexed", 1)
                        $ KittyX.change_stat("love", 60, 2)
                        ch_k ". . ."
                "Yeah, I know.":
                        $ KittyX.change_stat("love", 90, 5)
                "Huh, why not go by that then?":
                        if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                                $ KittyX.name = "Shadowcat"
                                $ KittyX.change_stat("obedience", 90, 5)
                                ch_k "I guess? . ."
                        else:
                                ch_k "Kind of a silly name to go around with. . ."
                                menu:
                                    extend ""
                                    "Ok, \"[KittyX.name]\" it is then.":
                                            $ KittyX.change_face("smile", 1)
                                    "I insist.":
                                            $ KittyX.change_stat("love", 90, -10)
                                            $ KittyX.change_stat("obedience", 50, 10)
                                            $ KittyX.change_face("angry", 2)
            ch_k ". . ."
            #end "why not Katherine"
    elif Options[0] == "Katherine":
            $ KittyX.names.append("Katherine")
            ch_k "My full name is \"Katherine Pryde.\""
            ch_k "You probably didn't know that."
            menu:
                extend ""
                "Oh, ok then.":
                        $ KittyX.change_face("perplexed", 1)
                        $ KittyX.change_stat("love", 60, 2)
                        ch_k ". . ."
                "I kind of prefer \"[KittyX.name].\"":
                        $ KittyX.change_stat("love", 90, 5)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        if ApprovalCheck(KittyX, 800, "LO"):
                                $ KittyX.change_stat("obedience", 70, 5)
                        ch_k "Yeah, me too. . ."
                "Why not go by \"Katherine\" then?":
                        if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                                $ KittyX.name = "Katherine"
                                $ KittyX.change_stat("obedience", 90, 5)
                                ch_k "I suppose I could. . ."
                        else:
                                ch_k "I don't really like it that much. . ."
                                menu:
                                    extend ""
                                    "Ok, \"[KittyX.name]\" it is then.":
                                            $ KittyX.change_face("smile", 1)
                                    "I insist.":
                                            $ KittyX.change_stat("love", 90, -10)
                                            $ KittyX.change_stat("obedience", 50, 10)
                                            $ KittyX.change_face("angry", 2)
                                            ch_k "!!!"
            #end "why not Katherine"

    elif Options[0] == "seenpeen": # first seen peen skipped
            $ KittyX.change_face("sly",2)
            ch_k "Maybe I didn't mention it before, but. . ."
            ch_k "That cock of yours is. . . impressive."
            $ KittyX.change_face("bemused",1)
            $ KittyX.change_stat("love", 90, 3)
            $ KittyX.History.remove("seenpeen")
    elif Options[0] == "topless": # first seen breasts skipped
            $ KittyX.change_face("bemused",2,Eyes="side")
            ch_k "Hey, when you saw me. . . topless earlier, you didn't have much to say. . ."
            ch_k "What'd you think?"
            call Kitty_First_TMenu
            $ KittyX.History.remove("topless")
    elif Options[0] == "bottomless": # first seen pussy skipped
            $ KittyX.change_face("bemused",2,Eyes="side")
            ch_k "Hey, when you saw my. . . pussy earlier. . ."
            ch_k "You didn't say much. . . "
            ch_k "What'd you think?"
            call Kitty_First_BMenu
            $ KittyX.History.remove("bottomless")

    elif Options[0] == "boyfriend?":
        call Kitty_BF
    elif Options[0] == "lover?":
        call Kitty_love
    elif Options[0] == "sir?":
        call Kitty_Sub
    elif Options[0] == "master?":
        call Kitty_Master
    elif Options[0] == "sexfriend?":
        call Kitty_Sexfriend
    elif Options[0] == "fuckbuddy?":
        call Kitty_Fuckbuddy
    elif Options[0] == "daddy?":
        call Kitty_Daddy

    elif Options[0] == "hate": # trinty lower then 50:
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want to see your face.",
                "Stop bothering me.",
                "Leave me alone."])
        ch_k "[line]"

    else: #all else fell through. . .
            $ D20 = renpy.random.randint(1, 15)
            if D20 == 1:
                    $ KittyX.change_face("smile")
                    ch_k "I'm[KittyX.like]{i}so{/i} excited [KittyX.Petname]! I {i}totally{/i} aced Professor McCoy's Computer Science test!"
            elif D20 == 2:
                    $ KittyX.change_face("sad")
                    ch_k "Ever have[KittyX.like]one of those days where it seems like the whole world's out to get you?"
            elif D20 == 3:
                    $ KittyX.change_face("surprised")
                    ch_k "I can't believe how much stuff I've gotta get done today!"
            elif D20 == 4:
                    $ KittyX.change_face("sad")
                    ch_k "Hey, [KittyX.Petname]. I got[KittyX.like]the world's worst sleep last night. I feel like I could[KittyX.like]curl up and go to bed right here."
            elif D20 == 5:
                    $ KittyX.change_face("smile")
                    ch_k "Wow! Isn't it[KittyX.like]{i}so{/i} nice out right now?"
            elif D20 == 6:
                    $ KittyX.change_face("perplexed")
                    ch_k "I had[KittyX.like]the worst nightmare last night. I dreamed the N'Garai demon was chasing me throught the Mansion!"
            elif D20 == 7:
                    $ KittyX.change_face("smile")
                    ch_k "So awesome. I have[KittyX.like]a lunch date tomorrow with my total bestie!"
            elif D20 == 8:
                    $ KittyX.change_face("sad")
                    ch_k "Y'know, I totally love it here in Salem Center. But I have to admit. . .I kinda miss Deerfield sometimes."
            elif D20 == 9:
                    $ KittyX.change_face("confused")
                    ch_k "So weird. Ever since Professor Xavier telepathically taught me Russian, I kinda find myself[KittyX.like]daydreaming in Cyrillic."
            elif D20 == 10:
                    $ KittyX.change_face("smile")
                    ch_k "{i}So{/i} nerdy, I know. But I[KittyX.like]totally had the best idea for this OS I'm writing for the Mansion's computers in the shower today!"
            elif D20 == 11:
                    $ KittyX.change_face("smile")
                    ch_k "I[KittyX.like]totally can't wait 'til dance class tomorrow! We're starting modern this semester!"
            elif D20 == 12:
                    $ KittyX.change_face("sad")
                    ch_k "I heard a few of the others are going to Harry's Hideaway tomorrow. I have[KittyX.like]{i}so{/i} much homework to do, though!"
            elif D20 == 13:
                    $ KittyX.change_face("smile")
                    ch_k "This probably sounds[KittyX.like]totally random, but, I could {i}so{/i} go for ice cream right now!"
            elif D20 == 14:
                    $ KittyX.change_face("sad")
                    ch_k "I hate thinking about how so many people[KittyX.like]totally hate mutants for no good reason. It's so depressing."
            elif D20 == 15:
                    $ KittyX.change_face("perplexed")
                    ch_k "I think I[KittyX.like]tweaked something in my thigh in the Danger Room, yesterday. It feel like I have a bruise that goes right through it!"
            else:
                    $ KittyX.change_face("perplexed")
                    ch_k "You're fun to hang with."

    $ line = 0
    return

label Kitty_Names:
    menu:
        ch_k "Oh? What would you like me to call you?"
        "Sweetie's fine.":
            $ KittyX.Petname = "sweetie"
            ch_k "You got it, sweetie."
        "My initial's fine.":
            $ KittyX.Petname = Player.name[:1]  #fix test this
            ch_k "You got it, [KittyX.Petname]."
        "Call me by my name.":
            $ KittyX.Petname = Player.name
            ch_k "If you'd rather, [KittyX.Petname]."
        "Call me \"boyfriend\"." if "boyfriend" in KittyX.Petnames:
            $ KittyX.Petname = "boyfriend"
            ch_k "Sure thing, [KittyX.Petname]."
        "Call me \"lover\"." if "lover" in KittyX.Petnames:
            $ KittyX.Petname = "lover"
            ch_k "Oooh, love to, [KittyX.Petname]."
        "Call me \"sir\"." if "sir" in KittyX.Petnames:
            $ KittyX.Petname = "sir"
            ch_k "Yes, [KittyX.Petname]."
        "Call me \"master\"." if "master" in KittyX.Petnames:
            $ KittyX.Petname = "master"
            ch_k "As you wish, [KittyX.Petname]."
        "Call me \"sex friend\"." if "sex friend" in KittyX.Petnames:
            $ KittyX.Petname = "sex friend"
            ch_k "Heh, very cheeky, [KittyX.Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in KittyX.Petnames:
            $ KittyX.Petname = "fuck buddy"
            ch_k "I'm game if you are, [KittyX.Petname]."
        "Call me \"daddy\"." if "daddy" in KittyX.Petnames:
            $ KittyX.Petname = "daddy"
            ch_k "Oh! You bet, [KittyX.Petname]."
        "Nevermind.":
            return
    return

label Kitty_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Kitty.":
                        $ KittyX.Pet = "Kitty"
                        ch_k "I don't see why not, [KittyX.Petname]."

                    "I think I'll call you \"girl\".":
                        $ KittyX.Pet = "girl"
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "I'm totally your girl, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm NOT your girl, [KittyX.Petname]."

                    "I think I'll call you \"boo\".":
                        $ KittyX.Pet = "boo"
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Aw, I am your boo, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm NOT your boo,  [KittyX.Petname]."

                    "I think I'll call you \"bae\".":
                        $ KittyX.Pet = "bae"
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Aw, I am your bae, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm NOT your bae,  [KittyX.Petname]."

                    "I think I'll call you \"baby\".":
                        $ KittyX.Pet = "baby"
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Aw, cute, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm not a baby!"


                    "I think I'll call you \"sweetie\".":
                        $ KittyX.Pet = "sweetie"
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            ch_k "Aw, that's sweet, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Too saccharine, [KittyX.Petname]."

                    "I think I'll call you \"sexy\".":
                        $ KittyX.Pet = "sexy"
                        if "lover" in KittyX.Petnames or ApprovalCheck(KittyX, 900):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Mreow, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Not in public, [KittyX.Petname]."

                    "I think I'll call you \"lover\".":
                        $ KittyX.Pet = "lover"
                        if "lover" in KittyX.Petnames or ApprovalCheck(KittyX, 900, "L") or ApprovalCheck(KittyX, 1400):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "love you too, [KittyX.Petname]!"
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Not in this lifetime, [KittyX.Petname]."

                    "I think I'll call you \"kitten\".":
                        $ KittyX.Pet = "baby"
                        if "boyfriend" in KittyX.Petnames or ApprovalCheck(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Purrr, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "Not really that cute, [KittyX.Petname]"

                    "Back":
                        pass

            "Risky":
                menu:
                    "I think I'll call you \"slave\".":
                        $ KittyX.Pet = "slave"
                        if "master" in KittyX.Petnames or ApprovalCheck(KittyX, 700, "O"):
                            $ KittyX.change_face("bemused", 1)
                            ch_k "As you wish, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I'm not a slave, [KittyX.Petname]."

                    "I think I'll call you \"pet\".":
                        $ KittyX.Pet = "pet"
                        if "master" in KittyX.Petnames or ApprovalCheck(KittyX, 600, "O"):
                            $ KittyX.change_face("bemused", 1)
                            ch_k "Hmm, make sure to pet me, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I'm no house cat, [KittyX.Petname]."

                    "I think I'll call you \"slut\".":
                        $ KittyX.Pet = "slut"
                        if "sex friend" in KittyX.Petnames or ApprovalCheck(KittyX, 1000, "OI"):
                            $ KittyX.change_face("sexy")
                            ch_k "If the name fits, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            $ KittyX.Mouth = "surprised"
                            ch_k "Not unless you want to lose some teeth!"

                    "I think I'll call you \"whore\".":
                        $ KittyX.Pet = "whore"
                        if "fuckbuddy" in KittyX.Petnames or ApprovalCheck(KittyX, 1100, "OI"):
                            $ KittyX.change_face("sly")
                            ch_k "Only for you though. . ."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Can you say that with a fat lip, [KittyX.Petname]?"

                    "I think I'll call you \"sugartits\".":
                        $ KittyX.Pet = "sugartits"
                        if "sex friend" in KittyX.Petnames or ApprovalCheck(KittyX, 1400):
                            $ KittyX.change_face("sly", 1)
                            ch_k "These little things?"
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I would hope not, [KittyX.Petname]."

                    "I think I'll call you \"sex friend\".":
                        $ KittyX.Pet = "sex friend"
                        if "sex friend" in KittyX.Petnames or ApprovalCheck(KittyX, 600, "I"):
                            $ KittyX.change_face("sly")
                            ch_k "Rreow. . ."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Not out loud, [KittyX.Petname]."

                    "I think I'll call you \"fuckbuddy\".":
                        $ KittyX.Pet = "fuckbuddy"
                        if "fuckbuddy" in KittyX.Petnames or ApprovalCheck(KittyX, 700, "I"):
                            $ KittyX.change_face("sly")
                            ch_k "Yup."
                        else:
                            $ KittyX.change_face("angry", 1)
                            $ KittyX.Mouth = "surprised"
                            ch_k "Don't even joke, [KittyX.Petname]."

                    "I think I'll call you \"baby girl\".":
                        $ KittyX.Pet = "baby girl"
                        if "daddy" in KittyX.Petnames or ApprovalCheck(KittyX, 1200):
                            $ KittyX.change_face("smile", 1)
                            ch_k "You know it, [KittyX.Petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I'm no kid!"

                    "Back":
                        pass

            "Nevermind.":
                return
    return

label Kitty_Rename:
        #Sets alternate names from Kitty
        $ KittyX.Mouth = "smile"
        ch_k "Yeah?"
        menu:
            extend ""
            "I think \"Kitty's\" a pretty name." if KittyX.name != "Kitty" and "Kitty" in KittyX.names:
                            $ KittyX.name = "Kitty"
                            ch_k "Me too!"
            "I thought \"Kate\" sounded cool." if KittyX.name != "Kate" and "Kate" in KittyX.names:
                            if "namechange" not in KittyX.daily_history:
                                    $ KittyX.change_stat("love", 70, 1)
                                    $ KittyX.change_stat("inhibition", 60, 2)
                                    $ KittyX.change_stat("inhibition", 80, 1)
                            $ KittyX.name = "Kate"
                            ch_k "Yeah, I thought so too. . ."
            "Do you go by \"Katherine?\"" if KittyX.name != "Katherine" and "Katherine" in KittyX.names:
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                            $ KittyX.name = "Katherine"
                            if "namechange" not in KittyX.daily_history:
                                    $ KittyX.change_stat("obedience", 70, 2)
                            ch_k "I guess. . . I could?"
                    else:
                            ch_k "I don't really like that one. . ."
            "Do you go by \"Shadowcat?\"" if KittyX.name != "Shadowcat" and "Shadowcat" in KittyX.names:
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                            $ KittyX.change_face("confused")
                            $ KittyX.name = "Shadowcat"
                            ch_k "I guess. . . I could?"
                    else:
                            $ KittyX.change_face("perplexed")
                            ch_k "People don't exactly call me that out of the field!"
                    $ KittyX.change_face()
            "Nevermind.":
                    pass
        $ KittyX.AddWord(1,0,"namechange")
        return

label Kitty_Personality(counter = 0):
    if not KittyX.Chat[4] or counter:
        "Since you're doing well in one area, you can convince [KittyX.name] to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_k "Sure, what's up?"
        "More obedienceient. [[love to obedienceience]" if KittyX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_k "If[KittyX.like]that's what you want, I could be a bit more obedient."
            $ KittyX.Chat[4] = 1
        "Less Inhibited. [[love to Inhibition]" if KittyX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_k "I could always be a bit more wild if that's what you want."
            $ KittyX.Chat[4] = 2

        "Less Inhibited. [[obedienceience to Inhibition]" if KittyX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_k "Ok, I could open up more."
            $ KittyX.Chat[4] = 3
        "More Loving. [[obedienceience to love]" if KittyX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_k "I'll try to."
            $ KittyX.Chat[4] = 4

        "More obedienceient. [[Inhibition to obedienceience]" if KittyX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_k "Oooh, kinky. . ."
            $ KittyX.Chat[4] = 5

        "More Loving. [[Inhibition to love]" if KittyX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_k "We do have fun together. . ."
            $ KittyX.Chat[4] = 6

        "I guess just do what you like. . .[[reset]" if KittyX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_k "Um, ok."
            $ KittyX.Chat[4] = 0
        "Repeat the rules":
            call Kitty_Personality(1)
            return
        "Nevermind.":
            return
    return

label Kitty_Clothes:
    if KittyX.Taboo:
            if "exhibitionist" in KittyX.Traits:
                ch_k "Mmmmm. . ."
            elif ApprovalCheck(KittyX, 900, TabM=4) or ApprovalCheck(KittyX, 400, "I", TabM=3):
                ch_k "This is[KittyX.like]pretty. . . exposed. . ."
            else:
                ch_k "This is[KittyX.like]pretty exposed, right?"
                ch_k "Can't we talk about this in our rooms?"
                return
    elif ApprovalCheck(KittyX, 900, TabM=4) or ApprovalCheck(KittyX, 600, "L") or ApprovalCheck(KittyX, 300, "O"):
                ch_k "[KittyX.Like]what were you thinking here?"
    else:
                ch_k "I'll let you know when I care what you think."
                return

    if Girl != KittyX or line == "Giftstore":
            #This culls returns if sent from another girl
            $ renpy.pop_call()
    $ line = 0
    $ Girl = KittyX
    call Shift_Focus(Girl)

label Kitty_Wardrobe_Menu:
    $ primary_action = 1 # to prevent Focus swapping. . .
    $ KittyX.change_face()
    while True:
        menu:
            ch_k "So[KittyX.like]you wanted to talk about my clothes?"
            "Overshirts":
                        call Kitty_Clothes_Over
            "Legwear":
                        call Kitty_Clothes_Legs
            "Underwear":
                        call Kitty_Clothes_Under
            "Accessories":
                        call Kitty_Clothes_Misc
            "Outfits":
                        call Kitty_Clothes_Outfits
            "Let's talk about what you wear around.":
                        call Clothes_Schedule(KittyX)

            "Could I get a look at it?" if KittyX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(KittyX,0,2)
                    if _return:
                        show PhoneSex zorder 150
                        ch_k "Cute? . ."
                    hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(KittyX,0,2)
                    if _return:
                        hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if KittyX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if KittyX.Loc == bg_current and not KittyX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    if ApprovalCheck(KittyX, 1500) or (KittyX.SeenChest and KittyX.SeenPussy):
                            ch_k "Probably won't need it, thanks."
                    else:
                            show DressScreen zorder 150
                            ch_k "Yeah, this is a bit more comfortable, thanks."

            "Gift for you (locked)" if Girl.Loc != bg_current:
                            pass
            "Gift for you" if Girl.Loc == bg_current:
                            ch_p "I'd like to give you something."
                            call Gifts #(Girl)

            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(KittyX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ KittyX.OutfitChange()
                    $ KittyX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ primary_action = 0
                    call Switch_Chat
                    if Girl != KittyX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = KittyX
                    call Shift_Focus(Girl)

            "Never mind, you look good like that.":
                    if "wardrobe" not in KittyX.recent_history:
                            #Apply stat boosts only if it's the first time this turn
                            if KittyX.Chat[1] <= 1:
                                    $ KittyX.change_stat("love", 70, 15)
                                    $ KittyX.change_stat("obedience", 40, 20)
                                    ch_k "That's[KittyX.like]really nice of you to say."
                            elif KittyX.Chat[1] <= 10:
                                    $ KittyX.change_stat("love", 70, 5)
                                    $ KittyX.change_stat("obedience", 40, 7)
                                    ch_k "I like it too."
                            elif KittyX.Chat[1] <= 50:
                                    $ KittyX.change_stat("love", 70, 1)
                                    $ KittyX.change_stat("obedience", 40, 1)
                                    ch_k "Yeah."
                            else:
                                    ch_k "Sure."
                            $ KittyX.recent_history.append("wardrobe")
                    if renpy.showing('DressScreen'):
                            call OutfitShame(KittyX,0,2)
                            if _return:
                                hide DressScreen
                            else:
                                $ KittyX.OutfitChange()
                    #sets up a temporary outfit
                    $ KittyX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ KittyX.Chat[1] += 1
                    $ primary_action = 0
                    return

        #Loops back up
        #jump Kitty_Clothes
        #End of Kitty Wardrobe Main Menu

    menu Kitty_Clothes_Outfits:
        # Outfits
        "You should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(KittyX,3,1)
                    "Custom 2":
                                call OutfitShame(KittyX,5,1)
                    "Custom 3":
                                call OutfitShame(KittyX,6,1)
                    "Gym Clothes":
                                call OutfitShame(KittyX,4,1)
                    "Sleepwear":
                                call OutfitShame(KittyX,7,1)
                    "Swimwear":
                                call OutfitShame(KittyX,10,1)
                    "Never mind":
                                pass

        "I really like that pink shirt and capris outfit you wear.":
                #pink shirt
                $ KittyX.OutfitChange("casual1")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ KittyX.Outfit = "casual1"
                        $ KittyX.Shame = 0
                        ch_k "I used to wear that one[KittyX.like]every day!"
                    "Let's try something else though.":
                        ch_k "K."

        "That red shirt and black jeans look really nice on you.":
                #red shirt
                $ KittyX.OutfitChange("casual2")
                menu:
                    "You should wear this one out. [[set current outfit]":
                        $ KittyX.Outfit = "casual2"
                        $ KittyX.Shame = 0
                        ch_k "That one[KittyX.like]used to be my favorite too!"
                    "Let's try something else though.":
                        ch_k "K."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not KittyX.Custom1[0] and not KittyX.Custom2[0] and not KittyX.Custom3[0]:
                        pass

        "Remember that outfit we put together?" if KittyX.Custom1[0] or KittyX.Custom2[0] or KittyX.Custom3[0]:
                $ counter = 0
                while 1:
                    menu:
                        "Throw on Custom 1 (locked)" if not KittyX.Custom1[0]:
                                pass
                        "Throw on Custom 1" if KittyX.Custom1[0]:
                                $ KittyX.OutfitChange("custom1")
                                $ counter = 3
                        "Throw on Custom 2 (locked)" if not KittyX.Custom2[0]:
                                pass
                        "Throw on Custom 2" if KittyX.Custom2[0]:
                                $ KittyX.OutfitChange("custom2")
                                $ counter = 5
                        "Throw on Custom 3 (locked)" if not KittyX.Custom3[0]:
                                pass
                        "Throw on Custom 3" if KittyX.Custom3[0]:
                                $ KittyX.OutfitChange("custom3")
                                $ counter = 6

                        "You should wear this one in private. (locked)" if not counter:
                                pass
                        "You should wear this one in private." if counter:
                                if counter == 5:
                                    $ KittyX.Clothing[9] = "custom2"
                                elif counter == 6:
                                    $ KittyX.Clothing[9] = "custom3"
                                else:
                                    $ KittyX.Clothing[9] = "custom1"
                                ch_k "Ok, sure."

                        "On second thought, forget about that one outfit. . .":
                                menu:
                                    "Custom 1 [[clear custom 1]" if KittyX.Custom1[0]:
                                        ch_k "Ok, no problem."
                                        $ KittyX.Custom1[0] = 0
                                    "Custom 1 [[clear custom 1] (locked)" if not KittyX.Custom1[0]:
                                        pass
                                    "Custom 2 [[clear custom 2]" if KittyX.Custom2[0]:
                                        ch_k "Ok, no problem."
                                        $ KittyX.Custom2[0] = 0
                                    "Custom 2 [[clear custom 2] (locked)" if not KittyX.Custom2[0]:
                                        pass
                                    "Custom 3 [[clear custom 3]" if KittyX.Custom3[0]:
                                        ch_k "Ok, no problem."
                                        $ KittyX.Custom3[0] = 0
                                    "Custom 3 [[clear custom 3] (locked)" if not KittyX.Custom3[0]:
                                        pass
                                    "Never mind, [[back].":
                                        pass

                        "You should wear this one out. [[choose outfit first](locked)" if not counter:
                                pass
                        "You should wear this one out." if counter:
                            call Custom_Out(KittyX,counter)
                        "Ok, back to what we were talking about. . .":
                            $ counter = 0
                            return

        "Gym Clothes?" if not KittyX.Taboo or bg_current == "bg_dangerroom":
                $ KittyX.OutfitChange("gym")

        "Sleepwear?" if not KittyX.Taboo:
                if ApprovalCheck(KittyX, 1200):
                        $ KittyX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(KittyX)
                        if _return:
                            $ KittyX.OutfitChange("sleep")

        "Swimwear? (locked)" if (KittyX.Taboo and bg_current != "bg_pool") or not KittyX.Swim[0]:
                $ KittyX.OutfitChange("swimwear")
        "Swimwear?" if (not KittyX.Taboo or bg_current == "bg_pool") and KittyX.Swim[0]:
                $ KittyX.OutfitChange("swimwear")

        "Halloween Costume?" if "halloween" in KittyX.History:
                ch_k "Sure."
                $ KittyX.OutfitChange("costume")

        "Your birthday suit looks really great. . .":
                #Nude
                $ KittyX.change_face("sexy", 1)
                $ line = 0
                if not KittyX.Chest and not KittyX.Panties and not KittyX.Over and not KittyX.Legs and not KittyX.Hose:
                    ch_k "You're kidding, right?"
                elif KittyX.SeenChest and KittyX.SeenPussy and ApprovalCheck(KittyX, 1200, TabM=4):
                    ch_k "[KittyX.Like]Reow. . ."
                    $ line = 1
                elif ApprovalCheck(KittyX, 2000, TabM=4):
                    ch_k "You don't[KittyX.like]mess around, huh."
                    $ line = 1
                elif KittyX.SeenChest and KittyX.SeenPussy and ApprovalCheck(KittyX, 1200, TabM=0):
                    ch_k "[KittyX.Like]this is a little exposed. . ."
                elif ApprovalCheck(KittyX, 2000, TabM=0):
                    ch_k "Maybe if we were alone?"
                elif ApprovalCheck(KittyX, 1000, TabM=0):
                    $ KittyX.change_face("surprised", 2)
                    ch_k "[KittyX.Like]get to know a girl first, [KittyX.Petname]."
                    $ KittyX.Blush = 1
                else:
                    $ KittyX.change_face("angry", 1)
                    ch_k "Yeah[KittyX.like]it does."

                if line:                                                            #If she got nude. . .
                    $ KittyX.OutfitChange("nude")
                    "She lets all her clothes drop into a pile at her feet."
                    call Kitty_First_Topless
                    call Kitty_First_Bottomless(1)
                    $ KittyX.change_face("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in KittyX.Traits:
                                ch_k "I'm[KittyX.like]getting a little wet just thinking about it."
                                $ KittyX.Outfit = "nude"
                                $ KittyX.change_stat("lust", 50, 10)
                                $ KittyX.change_stat("lust", 70, 5)
                                $ KittyX.Shame = 50
                            elif ApprovalCheck(KittyX, 800, "I") or ApprovalCheck(KittyX, 2800, TabM=0):
                                ch_k "I guess we could. . ."
                                $ KittyX.Outfit = "nude"
                                $ KittyX.Shame = 50
                            else:
                                $ KittyX.change_face("sexy", 1)
                                $ KittyX.Eyes = "surprised"
                                ch_k "No way! That'd be[KittyX.like]totally embarrassing!"

                        "Let's try something else though.":
                            if "exhibitionist" in KittyX.Traits:
                                ch_k "Aw, do I have to?"
                            elif ApprovalCheck(KittyX, 800, "I") or ApprovalCheck(KittyX, 2800, TabM=0):
                                $ KittyX.change_face("bemused", 1)
                                ch_k "It's a good thing you didn't[KittyX.like]ask me to wear this outside."
                                ch_k "A good thing. . ."
                            else:
                                $ KittyX.change_face("confused", 1)
                                ch_k "I[KittyX.like]don't mind this around the room, but definitely not outside."
                $ line = 0

        "Never mind":
            return #jump Kitty_Clothes

    return #jump Kitty_Clothes
    #End of Kitty Outfits

    menu Kitty_Clothes_Over:
        # Overshirts
        "Why don't you go with no [KittyX.Over]?" if KittyX.Over:
                $ KittyX.change_face("bemused", 1)
                if ApprovalCheck(KittyX, 800, TabM=3) and (KittyX.Chest or KittyX.SeenChest):
                    ch_k "Why not?"
                elif ApprovalCheck(KittyX, 600, TabM=0):
                    call Kitty_NoBra
                    if not _return:
                        if not ApprovalCheck(KittyX, 1200):
                            call Display_DressScreen(KittyX)
                            if not _return:
                                return #jump Kitty_Clothes
                        else:
                                return #jump Kitty_Clothes
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                            ch_k "Lol, not around you."
                            if not KittyX.Chest:
                                ch_k "I don't have anything under this. . ."
                            return #jump Kitty_Clothes
                $ line = KittyX.Over
                $ KittyX.Over = 0
                "She lets her [line] drop to her feet."
                if not KittyX.Chest and not renpy.showing('DressScreen'):
                        call Kitty_First_Topless

        "Try on that pink shirt you have." if KittyX.Over != "pink top":
                $ KittyX.change_face("bemused")
                if KittyX.Chest or KittyX.SeenChest:
                    ch_k "K."
                elif ApprovalCheck(KittyX, 800, TabM=0):
                    ch_k "Yeah, ok."
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                            $ KittyX.change_face("bemused", 1)
                            ch_k "This top is a little skimpy for what I have on under it."
                            return #jump Kitty_Clothes
                $ KittyX.Over = "pink top"

        "How about that red t-shirt you have?" if KittyX.Over != "red shirt":
                $ KittyX.Over = "red shirt"
                ch_k "This one?"

        "Try on that red jacket." if KittyX.Over != "jacket" and "halloween" in KittyX.History:
                $ KittyX.change_face("bemused")
                if KittyX.Chest or KittyX.SeenChest:
                    ch_k "K."
                elif ApprovalCheck(KittyX, 900, TabM=0):
                    ch_k "Yeah, ok."
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                            $ KittyX.change_face("bemused", 1)
                            ch_k "This top is a little skimpy for what I have on under it."
                            return #jump Kitty_Clothes
                $ KittyX.Over = "jacket"

        "Maybe just throw on a towel?" if KittyX.Over != "towel":
                $ KittyX.change_face("bemused", 1)
                if KittyX.Chest or KittyX.SeenChest:
                    ch_k "Weirdo."
                elif ApprovalCheck(KittyX, 1000, TabM=0): #or showing screen
                    $ KittyX.change_face("perplexed", 1)
                    ch_k "I guess? . ."
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                            ch_k "I don't think so with what I have on under it."
                            return #jump Kitty_Clothes
                $ KittyX.Over = "towel"

        "Never mind":
            pass
    return #jump Kitty_Clothes
    #End of Kitty Top

    label Kitty_NoBra: #fix test this
        menu:
            ch_k "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":
                        if KittyX.SeenChest and ApprovalCheck(KittyX, 1000, TabM=3):
                                $ KittyX.Blush = 2
                                ch_k "-not that that's a problem. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 1200, TabM=4):
                                $ KittyX.Blush = 2
                                ch_k "-not that that's a problem. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 900, TabM=2) and "lace bra" in KittyX.Inventory:
                                ch_k "I could find {i}something{/i} to wear."
                                $ KittyX.Chest  = "lace bra"
                                "She pulls out her lace bra and passes it through her [KittyX.Over]."
                        elif ApprovalCheck(KittyX, 800, TabM=2):
                                ch_k "Yeah, I guess."
                                $ KittyX.Chest = "bra"
                                "She pulls out her bra and passes it through her [KittyX.Over]."
                        elif ApprovalCheck(KittyX, 700, TabM=2):
                                ch_k "Yeah, I guess."
                                $ KittyX.Chest = "cami"
                                "She pulls out her camisole and passes it through her [KittyX.Over]."
                        elif ApprovalCheck(KittyX, 600, TabM=2):
                                ch_k "Yeah, I guess."
                                $ KittyX.Chest = "sports bra"
                                "She pulls out her sports bra and passes it through her [KittyX.Over]."
                        else:
                                ch_k "Yeah, I don't think so."
                                return 0

            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(KittyX, 1100, "LI", TabM=2) and KittyX.love > KittyX.inhibition:
                                ch_k "I guess for you. . ."
                        elif ApprovalCheck(KittyX, 700, "OI", TabM=2) and KittyX.obedience > KittyX.inhibition:
                                ch_k "Sure. . ."
                        elif ApprovalCheck(KittyX, 600, "I", TabM=2):
                                ch_k "Yeah. . ."
                        elif ApprovalCheck(KittyX, 1300, TabM=2):
                                ch_k "Okay, fine."
                        else:
                                $ KittyX.change_face("surprised")
                                $ KittyX.Brows = "angry"
                                if KittyX.Taboo > 20:
                                    ch_k "Not in public, [KittyX.Petname]!"
                                else:
                                    ch_k "I don't like you {i}that{/i} much, [KittyX.Petname]!"
                                return 0


            "Never mind.":
                        ch_k "Ok. . ."
                        return 0
        return 1
        #End of Kitty bra check

    menu Kitty_Clothes_Legs:
        # Leggings
        "Maybe go without the [KittyX.Legs]." if KittyX.Legs:
                $ KittyX.change_face("sexy", 1)
                if KittyX.SeenPanties and KittyX.Panties and ApprovalCheck(KittyX, 500, TabM=5):
                    ch_k "K."
                elif KittyX.SeenPussy and ApprovalCheck(KittyX, 900, TabM=4):
                    ch_k "Yeah, ok."
                elif ApprovalCheck(KittyX, 1300, TabM=2) and KittyX.Panties:
                    ch_k "For you, I guess. . ."
                elif ApprovalCheck(KittyX, 700) and not KittyX.Panties:
                    call Kitty_NoPantiesOn
                    if not _return and not KittyX.Panties:
                        if not ApprovalCheck(KittyX, 1500):
                            call Display_DressScreen(KittyX)
                            if not _return:
                                return #jump Kitty_Clothes
                        else:
                                return #jump Kitty_Clothes
                else:
                    call Display_DressScreen(KittyX)
                    if not _return:
                        ch_k "Lol, not around you."
                        if not KittyX.Panties:
                            ch_k "I'm not {i}wearing any panties{/i}. . ."
                        return #jump Kitty_Clothes
                $ line = KittyX.Legs
                $ KittyX.Legs = 0
                "She lets her [line] drop through her to the ground."
                $ line = 0
                if renpy.showing('DressScreen'):
                    pass
                elif KittyX.Panties:
                    $ KittyX.SeenPanties = 1
                else:
                    call Kitty_First_Bottomless

        "You look great in those capris." if KittyX.Legs != "capris":
                ch_k "Yeah, ok."
                $ KittyX.Legs = "capris"

        "You look great in those black jeans." if KittyX.Legs != "black jeans":
                ch_k "K, no problem."
                $ KittyX.Legs = "black jeans"

        "You look great in yoga pants." if KittyX.Legs != "yoga pants":
                ch_k "Yeah, ok."
                $ KittyX.Legs = "yoga pants"

        "What about wearing your yellow shorts?" if KittyX.Legs != "shorts":
                ch_k "K, no problem."
                $ KittyX.Legs = "shorts"

        "How about the blue skirt?" if KittyX.Legs != "blue skirt" and "blue skirt" in KittyX.Inventory:
                if KittyX.Panties or ApprovalCheck(KittyX,500,"I",TabM=2):
                        ch_k "Yeah, ok."
                        $ KittyX.Legs = "blue skirt"
                else:
                        ch_k "That's a little revealing. . ."

        "Try on that pink dress you have." if KittyX.Legs != "dress" and "halloween" in KittyX.History:
                menu:
                    ch_k "The whole thing, or just the skirt?"
                    "The whole dress.":
                            $ KittyX.Chest = "dress"
                    "Just the skirt.":
                            pass
                $ KittyX.Legs = "dress"

        "Never mind":
                pass
    return #jump Kitty_Clothes
    #End of Kitty Pants

    label Kitty_NoPantiesOn: #fix test this
        menu:
            ch_k "These are[KittyX.like]all I have on."
            "Then you could slip on a pair of panties. . .":
                        if KittyX.SeenPussy and ApprovalCheck(KittyX, 1100, TabM=4):
                                $ KittyX.Blush = 2
                                ch_k "I didn't say that bothered me. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 1500, TabM=4):
                                $ KittyX.Blush = 2
                                ch_k "I didn't say that bothered me. . ."
                                $ KittyX.Blush = 1
                        elif ApprovalCheck(KittyX, 800, TabM=4) and "lace panties" in KittyX.Inventory:
                                ch_k "I like how you think."
                                $ KittyX.Panties  = "lace panties"
                                "She pulls out her lace panties and pulls them up through her [KittyX.Legs]."
                        elif ApprovalCheck(KittyX, 700, TabM=4):
                                ch_k "Yeah, I guess."
                                $ KittyX.Panties = "green panties"
                                "She pulls out her green panties and pulls them up through her [KittyX.Legs]."
                        else:
                                ch_k "Yeah, I don't think so."
                                return 0

            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(KittyX, 1100, "LI", TabM=3) and KittyX.love > KittyX.inhibition:
                                ch_k "Well, not that I mind you seeing it. . ."
                        elif ApprovalCheck(KittyX, 700, "OI", TabM=3) and KittyX.obedience > KittyX.inhibition:
                                ch_k "I guess. . ."
                        elif ApprovalCheck(KittyX, 600, "I", TabM=3):
                                ch_k "Hrmm. . ."
                        elif ApprovalCheck(KittyX, 1300, TabM=3):
                                ch_k "Okay, okay."
                        else:
                                $ KittyX.change_face("surprised")
                                $ KittyX.Brows = "angry"
                                if KittyX.Taboo > 20:
                                    ch_k "Not in public, [KittyX.Petname]!"
                                else:
                                    ch_k "I don't like you {i}that{/i} much, [KittyX.Petname]!"
                                return 0

            "Never mind.":
                ch_k "Ok. . ."
                return 0
        return 1
        #End of Kitty Panties check

    menu Kitty_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [KittyX.Chest]?" if KittyX.Chest:
                        $ KittyX.change_face("bemused", 1)
                        if KittyX.SeenChest and ApprovalCheck(KittyX, 900, TabM=2.7):
                            ch_k "Sure."
                        elif ApprovalCheck(KittyX, 1100, TabM=2):
                            if KittyX.Taboo:
                                ch_k "I'm kind of nervous. . ."
                            else:
                                ch_k "If it's just you. . ."
                        elif KittyX.Over == "pink top" and ApprovalCheck(KittyX, 600, TabM=2):
                            ch_k "This look is a bit revealing. . ."
                        elif KittyX.Over == "red shirt" and ApprovalCheck(KittyX, 500, TabM=2):
                            ch_k "I guess I could. . ."
                        elif not KittyX.Over:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "Not without a little coverage, for modesty."
                                return #jump Kitty_Clothes
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "I don't think so, [KittyX.Petname]."
                                return #jump Kitty_Clothes
                        $ line = KittyX.Chest
                        $ KittyX.Chest = 0
                        if KittyX.Over:
                            "She reaches into her [KittyX.Over] grabs her [line], and pulls it out, dropping it to the ground."
                        else:
                            "She lets her [line] fall to the ground."
                            if not renpy.showing('DressScreen'):
                                call Kitty_First_Topless

                "Try on that yellow camisole." if KittyX.Chest != "cami":
                        ch_k "Ok."
                        $ KittyX.Chest = "cami"

                "I like that strapless bra." if KittyX.Chest != "bra":
                        if KittyX.SeenChest or ApprovalCheck(KittyX, 1200, TabM=2):
                            ch_k "K."
                            $ KittyX.Chest = "bra"
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "I'm not really comfortable with that. . ."
                            else:
                                $ KittyX.Chest = "bra"

                "I like that lace bra." if "lace bra" in KittyX.Inventory and KittyX.Chest != "lace bra":
                        if KittyX.SeenChest or ApprovalCheck(KittyX, 1300, TabM=2):
                            ch_k "K."
                            $ KittyX.Chest = "lace bra"
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "It's pretty skimpy. . ."
                            else:
                                $ KittyX.Chest = "lace bra"

                "I like that sports bra." if KittyX.Chest != "sports bra":
                        if KittyX.SeenChest or ApprovalCheck(KittyX, 1000, TabM=2):
                            ch_k "K."
                            $ KittyX.Chest = "sports bra"
                        else:
                            call Display_DressScreen(KittyX)
                            if not _return:
                                ch_k "I'm not sure about that. . ."
                            else:
                                $ KittyX.Chest = "sports bra"

                "I like that bikini top." if KittyX.Chest != "bikini top" and "bikini top" in KittyX.Inventory:
                        if bg_current == "bg_pool":
                                ch_k "K."
                                $ KittyX.Chest = "bikini top"
                        else:
                                if KittyX.SeenChest or ApprovalCheck(KittyX, 1000, TabM=2):
                                    ch_k "K."
                                    $ KittyX.Chest = "bikini top"
                                else:
                                    call Display_DressScreen(KittyX)
                                    if not _return:
                                            ch_k "Geez, not here!"
                                    else:
                                            $ KittyX.Chest = "bikini top"

                "Try on that pink dress you have." if KittyX.Chest != "dress" and "halloween" in KittyX.History:
                    if KittyX.SeenChest or ApprovalCheck(KittyX, 1000, TabM=2):
                            ch_k "K."
                    else:
                        call Display_DressScreen(KittyX)
                        if not _return:
                            ch_k "I'm not sure about that. . ."
                            jump Kitty_Clothes_Under
                    menu:
                        ch_k "The whole thing, or just the top?"
                        "The whole dress.":
                                $ KittyX.Legs = "dress"
                        "Just the top.":
                                pass
                    $ KittyX.Chest = "dress"

                "Never mind":
                        pass
            jump Kitty_Clothes_Under

        "Hose and stockings options":
                menu:
                    "You could lose the hose." if KittyX.Hose:
                            $ KittyX.Hose = 0
                    "The thigh-high hose would look good with that." if KittyX.Hose != "stockings":
                            $ KittyX.Hose = "stockings"
                    "The knee-high hose would look good with that." if KittyX.Hose != "knee stockings" and "knee" in KittyX.Inventory:
                            $ KittyX.Hose = "knee stockings"
                    "The pantyhose would look good with that." if KittyX.Hose != "pantyhose" and "pantyhose" in KittyX.Inventory:
                            $ KittyX.Hose = "pantyhose"
                    "The stockings would look good with that." if KittyX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in KittyX.Inventory:
                            $ KittyX.Hose = "stockings and garterbelt"
                    "Maybe just the garterbelt?" if KittyX.Hose != "garterbelt" and "stockings and garterbelt" in KittyX.Inventory:
                            $ KittyX.Hose = "garterbelt"
                    "Your ripped pantyhose would look good with that." if KittyX.Hose != "ripped pantyhose" and "ripped pantyhose" in KittyX.Inventory:
                            $ KittyX.Hose = "ripped pantyhose"
                    "Never mind":
                            pass
                jump Kitty_Clothes_Under

        #Panties
        "Panties":
            menu:
                "You could lose those panties. . ." if KittyX.Panties:
                        $ KittyX.change_face("bemused", 1)
                        if ApprovalCheck(KittyX, 900) and (KittyX.Legs or (KittyX.SeenPussy and not KittyX.Taboo)):
                            #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public
                            if ApprovalCheck(KittyX, 850, "L"):
                                    ch_k "Well, if you ask me nicely. . ."
                            elif ApprovalCheck(KittyX, 500, "O"):
                                    ch_k "For you, ok."
                            elif ApprovalCheck(KittyX, 350, "I"):
                                    ch_k "[[snort]."
                            else:
                                    ch_k "Yeah, I guess."
                        else:                       #low approval or not wearing pants or in public
                            if ApprovalCheck(KittyX, 1100, "LI", TabM=3) and KittyX.love > KittyX.inhibition:
                                    ch_k "Well, not that I mind you seeing it. . ."
                            elif ApprovalCheck(KittyX, 700, "OI", TabM=3) and KittyX.obedience > KittyX.inhibition:
                                    ch_k "I guess. . ."
                            elif ApprovalCheck(KittyX, 600, "I", TabM=3):
                                    ch_k "Hrmm. . ."
                            elif ApprovalCheck(KittyX, 1300, TabM=3):
                                    ch_k "Okay, okay."
                            else:
                                call Display_DressScreen(KittyX)
                                if not _return:
                                    $ KittyX.change_face("surprised")
                                    $ KittyX.Brows = "angry"
                                    if KittyX.Taboo > 20:
                                        ch_k "Not in public, [KittyX.Petname]!"
                                    else:
                                        ch_k "I don't like you that much, [KittyX.Petname]!"
                                    return #jump Kitty_Clothes

                        $ line = KittyX.Panties
                        $ KittyX.Panties = 0
                        if KittyX.Legs:
                            "She reaches into her pocket, grabs hold of something, and then pulls her [line] out, droping them to the ground."
                        else:
                            "She lets her [line] drop to the ground."
                            if  not renpy.showing('DressScreen'):
                                call Kitty_First_Bottomless
                                $ KittyX.change_stat("inhibition", 50, 2)

                "Why don't you wear the green panties instead?" if KittyX.Panties and KittyX.Panties != "green panties":
                        if ApprovalCheck(KittyX, 1100, TabM=3):
                                ch_k "K."
                                $ KittyX.Panties = "green panties"
                        else:
                                call Display_DressScreen(KittyX)
                                if not _return:
                                    ch_k "I don't think that's any of your beeswax."
                                else:
                                    $ KittyX.Panties = "green panties"

                "Why don't you wear the lace panties instead?" if "lace panties" in KittyX.Inventory and KittyX.Panties and KittyX.Panties != "lace panties":
                        if ApprovalCheck(KittyX, 1300, TabM=3):
                                ch_k "I guess."
                                $ KittyX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(KittyX)
                                if not _return:
                                    ch_k "That's[KittyX.like]none of your business."
                                else:
                                    $ KittyX.Panties = "lace panties"

                "I like those bikini bottoms." if KittyX.Panties != "bikini bottoms" and "bikini bottoms" in KittyX.Inventory:
                        if bg_current == "bg_pool":
                                ch_k "K."
                                $ KittyX.Panties = "bikini bottoms"
                        else:
                                if ApprovalCheck(KittyX, 1000, TabM=2):
                                    ch_k "K."
                                    $ KittyX.Panties = "bikini bottoms"
                                else:
                                    call Display_DressScreen(KittyX)
                                    if not _return:
                                        ch_k "Geez, not here!"
                                    else:
                                        $ KittyX.Panties = "bikini bottoms"

                "You know, you could wear some panties with that. . ." if not KittyX.Panties:
                        $ KittyX.change_face("bemused", 1)
                        if KittyX.Legs and (KittyX.love+KittyX.obedience) <= (2 * KittyX.inhibition):
                            $ KittyX.Mouth = "smile"
                            ch_k "I think I'd. . . rather not."
                            menu:
                                "Fine by me":
                                    return #jump Kitty_Clothes
                                "I insist, put some on.":
                                    if (KittyX.love+KittyX.obedience) <= (1.5 * KittyX.inhibition):
                                        $ KittyX.change_face("angry", Eyes="side")
                                        ch_k "Well that's too bad."
                                        return #jump Kitty_Clothes
                                    else:
                                        $ KittyX.change_face("sadside")
                                        ch_k "Ok, FINE."
                        menu:
                            ch_k "I guess. . ."
                            "How about the green ones?":
                                ch_k "Sure, ok."
                                $ KittyX.Panties = "green panties"
                            "How about the lace ones?" if "lace panties" in KittyX.Inventory:
                                ch_k "Alright."
                                $ KittyX.Panties  = "lace panties"
                "Never mind":
                        pass
            jump Kitty_Clothes_Under
        "Never mind":
                pass
    return #jump Kitty_Clothes
    #End of Kitty Underwear

    menu Kitty_Clothes_Misc:
        #Misc
        "Ponytail style" if KittyX.Hair != "evo":
                ch_p "You look good with your hair up."
                if ApprovalCheck(KittyX, 600):
                    ch_k "Like this?"
                    $ KittyX.Hair = "evo"
                else:
                    ch_k "Yeah, I know that."

        "Loose Hair Style" if KittyX.Hair != "long":
                ch_p "Maybe let your hair down."
                if ApprovalCheck(KittyX, 600):
                    ch_k "You think?"
                    $ KittyX.Hair = "long"
                else:
                    ch_k "I[KittyX.like]kinda prefer to keep it up."

        "Wet hair style." if KittyX.Hair != "wet":
                ch_p "You should go for that wet look with your hair."
                if ApprovalCheck(KittyX, 800):
                    ch_k "You think so?"
                    "She rummages in her bag and grabs some gel, running it through her hair."
                    ch_k "Like this?"
                    $ KittyX.Hair = "wet"
                else:
                    ch_k "It's too high maintenance."

        "Grow pubes" if not KittyX.Pubes:
                ch_p "You know, I like some nice hair down there. Maybe grow it out."
                if "pubes" in KittyX.Todo:
                    ch_k "[[snort] You've got to give it some time!"
                else:
                    $ KittyX.change_face("bemused", 1)
                    $ Approval = ApprovalCheck(KittyX, 1150, TabM=0)
                    if ApprovalCheck(KittyX, 850, "L", TabM=0) or (Approval and KittyX.love > 2 * KittyX.obedience):
                        ch_k "I guess I could. . ."
                    elif ApprovalCheck(KittyX, 500, "I", TabM=0) or (Approval and KittyX.inhibition > KittyX.obedience):
                        ch_k "You want a furry kitty to pet?"
                    elif ApprovalCheck(KittyX, 400, "O", TabM=0) or Approval:
                        ch_k "If you want me to. . ."
                    else:
                        $ KittyX.change_face("surprised")
                        $ KittyX.Brows = "angry"
                        ch_k "Not that it's any of your business, [KittyX.Petname]."
                        return #jump Kitty_Clothes
                    $ KittyX.Todo.append("pubes")
                    $ KittyX.PubeC = 6

        "Shave pubes" if KittyX.Pubes:
                ch_p "I like it waxed clean down there."
                $ KittyX.change_face("bemused", 1)
                if "shave" in KittyX.Todo:
                        ch_k "I know, I know. I'll take care of it later."
                else:
                        $ Approval = ApprovalCheck(KittyX, 1150, TabM=0)

                        if ApprovalCheck(KittyX, 850, "L", TabM=0) or (Approval and KittyX.love > 2 * KittyX.obedience):
                            ch_k "I guess I could tidy up a bit. . ."
                        elif ApprovalCheck(KittyX, 500, "I", TabM=0) or (Approval and KittyX.inhibition > KittyX.obedience):
                            ch_k "I'll keep it smooth."
                        elif ApprovalCheck(KittyX, 400, "O", TabM=0) or Approval:
                            ch_k "I'll get it done."
                        else:
                            $ KittyX.change_face("surprised")
                            $ KittyX.Brows = "angry"
                            ch_k "Not that it's any of your business, [KittyX.Petname]."
                            return #jump Kitty_Clothes
                        $ KittyX.Todo.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not KittyX.SeenPussy and not KittyX.SeenChest:
            pass

        "Add ring piercings" if KittyX.Pierce != "ring" and (KittyX.SeenPussy or KittyX.SeenChest):
                ch_p "You know, you'd look really nice with some ring body piercings."
                if "ring" in KittyX.Todo:
                    ch_k "I know, I know. I'll take care of it later."
                else:
                    $ KittyX.change_face("bemused", 1)
                    $ Approval = ApprovalCheck(KittyX, 1350, TabM=0)
                    if ApprovalCheck(KittyX, 900, "L", TabM=0) or (Approval and KittyX.love > 2* KittyX.obedience):
                        ch_k "If you think they'd look good on me. . ."
                    elif ApprovalCheck(KittyX, 600, "I", TabM=0) or (Approval and KittyX.inhibition > KittyX.obedience):
                        ch_k "I think they'd look great too!"
                    elif ApprovalCheck(KittyX, 500, "O", TabM=0) or Approval:
                        ch_k "K, I'll take care of it."
                    else:
                        $ KittyX.change_face("surprised")
                        $ KittyX.Brows = "angry"
                        ch_k "Not that it's any of your business, [KittyX.Petname]."
                        return #jump Kitty_Clothes
                    $ KittyX.Todo.append("ring")

        "Add barbell piercings" if KittyX.Pierce != "barbell" and (KittyX.SeenPussy or KittyX.SeenChest):
                ch_p "You know, you'd look really nice with some barbell body piercings."
                if "barbell" in KittyX.Todo:
                    ch_k "I know, I know. I'll take care of it later."
                else:
                    $ KittyX.change_face("bemused", 1)
                    $ Approval = ApprovalCheck(KittyX, 1350, TabM=0)
                    if ApprovalCheck(KittyX, 900, "L", TabM=0) or (Approval and KittyX.love > 2 * KittyX.obedience):
                        ch_k "If you think they'd look good on me. . ."
                    elif ApprovalCheck(KittyX, 600, "I", TabM=0) or (Approval and KittyX.inhibition > KittyX.obedience):
                        ch_k "I think they'd look great too!"
                    elif ApprovalCheck(KittyX, 500, "O", TabM=0) or Approval:
                        ch_k "K, I'll take care of it."
                    else:
                        $ KittyX.change_face("surprised")
                        $ KittyX.Brows = "angry"
                        ch_k "Not that it's any of your business, [KittyX.Petname]."
                        return #jump Kitty_Clothes
                    $ KittyX.Todo.append("barbell")
                    $ KittyX.Pierce = "barbell"

        "Remove Piercings" if KittyX.Pierce:
                ch_p "You know, you'd look better without those piercings."
                $ KittyX.change_face("bemused", 1)
                $ Approval = ApprovalCheck(KittyX, 1350, TabM=0)
                if ApprovalCheck(KittyX, 950, "L", TabM=0) or (Approval and KittyX.love > KittyX.obedience):
                    ch_k "I guess if they're getting in the way . ."
                elif ApprovalCheck(KittyX, 700, "I", TabM=0) or (Approval and KittyX.inhibition > KittyX.obedience):
                    ch_k "They were getting a little annoying."
                elif ApprovalCheck(KittyX, 600, "O", TabM=0) or Approval:
                    ch_k "I'll take them out then."
                else:
                    $ KittyX.change_face("surprised")
                    $ KittyX.Brows = "angry"
                    ch_k "Well {i}I{/i} kinda like'em."
                    return #jump Kitty_Clothes
                $ KittyX.Pierce = 0

        "Add gold necklace" if KittyX.Neck != "gold necklace":
                ch_p "Why don't you try on that gold necklace?"
                ch_k "Ok. . ."
                $ KittyX.Neck = "gold necklace"
        "Add star necklace" if KittyX.Neck != "star necklace":
                ch_p "Why don't you try on that star necklace?"
                ch_k "Ok. . ."
                $ KittyX.Neck = "star necklace"
        "Add flower necklace" if KittyX.Neck != "flower necklac" and "halloween" in KittyX.History:
                ch_p "Why don't you try on that flower necklace?"
                ch_k "Ok. . ."
                $ KittyX.Neck = "flower necklace"

        "Maybe go without a necklace." if KittyX.Neck:
                ch_k "Ok. . ."
                $ KittyX.Neck = 0


        "Never mind":
            pass
    return #jump Kitty_Clothes
    #End of Kitty Misc Wardrobe

    return
