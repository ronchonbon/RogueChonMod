



label Kitty_Relationship:
    while True:
        menu:
            ch_k "What did you want to talk about?"
            "Do you want to be my girlfriend?" if KittyX not in Player.Harem and "ex" not in KittyX.traits:
                $ KittyX.daily_history.append("relationship")
                if "asked boyfriend" in KittyX.daily_history and "_angry" in KittyX.daily_history:
                    $ KittyX.change_face("_angry", 1)
                    ch_k "For real, buzz off."
                    return
                elif "asked boyfriend" in KittyX.daily_history:
                    $ KittyX.change_face("_angry", 1)
                    ch_k "Still \"nope.\""
                    return
                elif KittyX.broken_up[0]:
                    $ KittyX.change_face("_angry", 1)
                    ch_k "Not while you're dating her. . ."
                    if Player.Harem:
                        $ KittyX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_p "I'm not anymore."

                $ KittyX.daily_history.append("asked boyfriend")

                if Player.Harem and "KittyYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_k "I don't think they'd be ok with that, [KittyX.player_petname]."
                    else:
                        ch_k "I don't think [Player.Harem[0].name] would be ok with that, [KittyX.player_petname]."
                    return

                if KittyX.event_happened[5]:
                    $ KittyX.change_face("_bemused", 1)
                    ch_k "I {i}did{/i} ask you about that. . ."
                else:
                    $ KittyX.change_face("_surprised", 2)
                    ch_k "I don't know, [KittyX.player_petname]. . ."
                    $ KittyX.change_face("_smile", 1)

                call Kitty_OtherWoman

                if KittyX.love >= 800:
                    $ KittyX.change_face("_surprised", 1)
                    $ KittyX.mouth = "_smile"
                    $ KittyX.change_stat("love", 200, 40)
                    ch_k "YES!"
                    if "boyfriend" not in KittyX.player_petnames:
                        $ KittyX.player_petnames.append("boyfriend")
                    if "KittyYes" in Player.traits:
                        $ Player.traits.remove("KittyYes")
                    $ Player.Harem.append(KittyX)
                    call Harem_Initiation
                    "[KittyX.name] leaps in and kisses you deeply."
                    $ KittyX.change_face("_kiss", 1)
                    $ KittyX.action_counter["kiss"] += 1
                elif KittyX.obedience >= 500:
                    $ KittyX.change_face("_perplexed")
                    ch_k "Maybe not so much \"dating\". . ."
                elif KittyX.inhibition >= 500:
                    $ KittyX.change_face("_smile")
                    ch_k "That's not[KittyX.like]where I'm at right now?"
                else:
                    $ KittyX.change_face("_perplexed", 1)
                    ch_k "I don't really feel that way about you right now, [KittyX.player_petname]."

            "Do you want to get back together?" if "ex" in KittyX.traits:
                $ KittyX.daily_history.append("relationship")
                if "asked boyfriend" in KittyX.daily_history and "_angry" in KittyX.daily_history:
                    $ KittyX.change_face("_angry", 1)
                    ch_k "Seriously, buzz off."
                    return
                elif "asked boyfriend" in KittyX.daily_history:
                    $ KittyX.change_face("_angry", 1)
                    ch_k "Still no."
                    return

                $ KittyX.daily_history.append("asked boyfriend")

                if Player.Harem and "KittyYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_k "I don't think they'd be ok with that, [KittyX.player_petname]."
                    else:
                        ch_k "I don't think [Player.Harem[0].name] would be ok with that, [KittyX.player_petname]."
                    return

                $ counter = 0
                call Kitty_OtherWoman

                if KittyX.love >= 800:
                    $ KittyX.change_face("_surprised", 1)
                    $ KittyX.mouth = "_smile"
                    $ KittyX.change_stat("love", 90, 5)
                    ch_k "Well, I guess, sure!"
                    if "boyfriend" not in KittyX.player_petnames:
                        $ KittyX.player_petnames.append("boyfriend")
                    $ KittyX.traits.remove("ex")
                    if "KittyYes" in Player.traits:
                        $ Player.traits.remove("KittyYes")
                    $ Player.Harem.append(KittyX)
                    call Harem_Initiation
                    "[KittyX.name] leaps in and kisses you deeply."
                    $ KittyX.change_face("_kiss", 1)
                    $ KittyX.action_counter["kiss"] += 1
                elif KittyX.love >= 600 and approval_check(KittyX, 1500):
                    $ KittyX.change_face("_smile", 1)
                    $ KittyX.change_stat("love", 90, 5)
                    ch_k "Um, ok, I guess."
                    if "boyfriend" not in KittyX.player_petnames:
                        $ KittyX.player_petnames.append("boyfriend")
                    $ KittyX.traits.remove("ex")
                    if "KittyYes" in Player.traits:
                        $ Player.traits.remove("KittyYes")
                    $ Player.Harem.append(KittyX)
                    call Harem_Initiation
                    $ KittyX.change_face("_kiss", 1)
                    "[KittyX.name] gives you a quick kiss."
                    $ KittyX.change_face("_smile", 1)
                    $ KittyX.action_counter["kiss"] += 1
                elif KittyX.obedience >= 500:
                    $ KittyX.change_face("_sad")
                    ch_k "I think we're better like this."
                elif KittyX.inhibition >= 500:
                    $ KittyX.change_face("_perplexed")
                    ch_k "I kind of like what we have right now."
                else:
                    $ KittyX.change_face("_perplexed", 1)
                    ch_k "I'm not ready to get burned again."



            "I wanted to ask about [[another girl]" if KittyX in Player.Harem:
                call AskDateOther

            "I think we should break up." if KittyX in Player.Harem:
                if "breakup talk" in KittyX.recent_history:
                    ch_k "We were {i}just{/i} over this, not even funny."
                elif "breakup talk" in KittyX.daily_history:
                    ch_k "I don't want to do this again today, [KittyX.player_petname]."
                else:
                    call Breakup (KittyX)
            "About that talk we had before. . .":


                menu:
                    "When you said you loved me. . ." if "lover" not in KittyX.traits and KittyX.event_happened[6] >= 20:
                        call Kitty_Love_Redux

                    "You said you wanted me to be more in control?" if "sir" not in KittyX.player_petnames and "sir" in KittyX.history:
                        if "asked sub" in KittyX.recent_history:
                            ch_k "We[KittyX.like]{i}just{/i} went over this."
                        elif "asked sub" in KittyX.daily_history:
                            ch_k "I think you made yourself {i}perfectly{/i} clear earlier. . ."
                        else:
                            call Kitty_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in KittyX.player_petnames and "master" in KittyX.history:
                        if "asked sub" in KittyX.recent_history:
                            ch_k "We[KittyX.like]{i}just{/i} went over this."
                        elif "asked sub" in KittyX.daily_history:
                            ch_k "I think you made yourself {i}perfectly{/i} clear earlier. . ."
                        else:
                            call Kitty_Sub_Asked

                    "About that gift you wanted to get [LauraX.name]. . ." if "dress1" in LauraX.history and "dress2" not in LauraX.history and "dress3" not in LauraX.history:
                        call Laura_Dressup2
                    "Never mind":

                        pass
            "Never Mind":
                return
    return

label Kitty_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((KittyX.likes[Player.Harem[0].tag] - 500)/2)

    $ KittyX.change_face("_perplexed")
    if len(Player.Harem) >= 2:
        ch_k "But you're with [Player.Harem[0].name] right now, and and all sorts of other girls!"
    else:
        ch_k "But you're with [Player.Harem[0].name]!"
    menu:
        extend ""
        "She said I can be with you too." if "KittyYes" in Player.traits:
            if approval_check(KittyX, 1800, Bonus = counter):
                $ KittyX.change_face("_smile", 1)
                if KittyX.love >= KittyX.obedience:
                    ch_k "Just so long as we can be together, I can share."
                elif KittyX.obedience >= KittyX.inhibition:
                    ch_k "I'm ok with that if she is."
                else:
                    ch_k "Yeah, I mean I guess so."
            else:
                $ KittyX.change_face("_angry", 1)
                ch_k "Well maybe she did, but I don't want to share."
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "KittyYes" not in Player.traits:
            if approval_check(KittyX, 1800, Bonus = counter):
                $ KittyX.change_face("_smile", 1)
                if KittyX.love >= KittyX.obedience:
                    ch_k "Just so long as we can be together, I can share."
                elif KittyX.obedience >= KittyX.inhibition:
                    ch_k "I'm ok with that if she is."
                else:
                    ch_k "Yeah, I mean I guess so."
                ch_k "Go ask her, and let me know what she thinks in the morning."
            else:
                $ KittyX.change_face("_angry", 1)
                ch_k "Well maybe she did, but I don't want to share."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(KittyX, 1800, Bonus = -counter):
                $ KittyX.change_face("_angry", 1)
                if not approval_check(KittyX, 1800):
                    ch_k "Well I don't like you that much either."
                else:
                    ch_k "Well I'm not cool with that, [Player.Harem[0].name]'s a friend of mine."
                $ renpy.pop_call()
            else:
                $ KittyX.change_face("_smile", 1)
                if KittyX.love >= KittyX.obedience:
                    ch_k "I really do want to be together with you."
                elif KittyX.obedience >= KittyX.inhibition:
                    ch_k "If that's how you want it to be."
                else:
                    ch_k "I suppose that's true."
                $ KittyX.traits.append("downlow")
        "I can break it off with her.":

            $ KittyX.change_face("_sad")
            ch_k "Well then maybe I'll see you tomorrow after you have."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ KittyX.change_face("_sad")
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
            if approval_check(KittyX, 1400):
                $ KittyX.like = ", nyaa, "
                $ KittyX.Like = "Nyaa, "
                ch_k "[KittyX.Like]you are such a dork."
            elif approval_check(KittyX, 1000, "LO"):
                $ KittyX.like = ", nyaa, "
                $ KittyX.Like = "Nyaa, "
                ch_k "[KittyX.Like]if that's what you want."
            else:
                ch_k "[KittyX.Like]no way, weirdo."
        "Fucking":
            if approval_check(KittyX, 400, "I"):
                $ KittyX.like = " fucking "
                $ KittyX.Like = "Fucking "
                ch_k "[KittyX.Like]yeah I will."
            elif approval_check(KittyX, 1000, "LO"):
                $ KittyX.like = " fucking "
                $ KittyX.Like = "Fucking "
                ch_k "If you[KittyX.like]say so."
            else:
                ch_k "I don't fucking think so."
                ch_k ". . .most of the time."
        "Nothing":
            if approval_check(KittyX, 900, "LO"):
                $ KittyX.like = " "
                $ KittyX.Like = ". . . "
                ch_k "[KittyX.Like] ok . . ."
            else:
                ch_k "I don't[KittyX.like]think I could do that."

    return


label Kitty_About(Check=0):
    if Check not in all_Girls:
        ch_k "Who?"
        return
    ch_k "What do I think about her? Well. . ."
    if Check == RogueX:
        if "poly Rogue" in KittyX.traits:
            ch_k "You know we're[KittyX.like]close. . ."
        elif KittyX.likes[RogueX.tag] >= 900:
            ch_k "She's[KittyX.like]really sexy. . ."
        elif KittyX.likes[RogueX.tag] >= 800:
            ch_k "She's my bestie, and maybe. . ."
        elif KittyX.likes[RogueX.tag] >= 700:
            ch_k "She's[KittyX.like]my bestie!"
        elif KittyX.likes[RogueX.tag] >= 600:
            ch_k "We're[KittyX.like]friends and all."
        elif KittyX.likes[RogueX.tag] >= 500:
            ch_k "She's not[KittyX.like]a jerk or anything."
        elif KittyX.likes[RogueX.tag] >= 400:
            ch_k "I'm kinda[KittyX.like]over her."
        elif KittyX.likes[RogueX.tag] >= 300:
            ch_k "That basic bitch gotta go."
        else:
            ch_k "That slut?"
    elif Check == EmmaX:
        if "poly Emma" in KittyX.traits:
            ch_k "You know we bang, right?"
        elif KittyX.likes[EmmaX.tag] >= 900:
            ch_k "She's got[KittyX.like]really amazing tits. . ."
        elif KittyX.likes[EmmaX.tag] >= 800:
            ch_k "She's really beautiful. . ."
        elif KittyX.likes[EmmaX.tag] >= 700:
            ch_k "I think we've become good friends."
        elif KittyX.likes[EmmaX.tag] >= 600:
            ch_k "She's[KittyX.like]my favorite teacher."
        elif KittyX.likes[EmmaX.tag] >= 500:
            ch_k "She's[KittyX.like]OK."
        elif KittyX.likes[EmmaX.tag] >= 400:
            ch_k "She gives out[KittyX.like]way too much homework."
        elif KittyX.likes[EmmaX.tag] >= 300:
            ch_k "Ugh, that witch."
        else:
            ch_k "That whore?"
    elif Check == LauraX:
        if "poly Laura" in KittyX.traits:
            ch_k "You know we[KittyX.like]make out sometimes. . ."
        elif KittyX.likes[LauraX.tag] >= 900:
            ch_k "She's[KittyX.like]such an animal. . ."
        elif KittyX.likes[LauraX.tag] >= 800:
            ch_k "We're pretty tight lately. . ."
        elif KittyX.likes[LauraX.tag] >= 700:
            ch_k "She's[KittyX.like]a really good friend."
        elif KittyX.likes[LauraX.tag] >= 600:
            ch_k "We're[KittyX.like]teammates."
        elif KittyX.likes[LauraX.tag] >= 500:
            ch_k "She's not[KittyX.like]a total jerk."
        elif KittyX.likes[LauraX.tag] >= 400:
            ch_k "I'm kinda[KittyX.like]done with her."
        elif KittyX.likes[LauraX.tag] >= 300:
            ch_k "Jungle girl?"
        else:
            ch_k "Bitch in heat."
    elif Check == JeanX:
        if "poly Jean" in KittyX.traits:
            ch_k "You know we're[KittyX.like]close. . ."
        elif KittyX.likes[JeanX.tag] >= 900:
            ch_k "She's[KittyX.like]really sexy. . ."
        elif KittyX.likes[JeanX.tag] >= 800:
            ch_k "She's pretty great. . . I think. . ."
        elif KittyX.likes[JeanX.tag] >= 700:
            ch_k "She's[KittyX.like]my bestie!"
        elif KittyX.likes[JeanX.tag] >= 600:
            ch_k "We're[KittyX.like]friends, I guess."
        elif KittyX.likes[JeanX.tag] >= 500:
            ch_k "She's not[KittyX.like]-so- bad. . ."
        elif KittyX.likes[JeanX.tag] >= 400:
            ch_k "I'm kinda[KittyX.like]done with her drama."
        elif KittyX.likes[JeanX.tag] >= 300:
            ch_k "She is[KittyX.like]-so- dramatic!"
        else:
            ch_k "That bitch?"
    elif Check == StormX:
        if "poly Storm" in KittyX.traits:
            ch_k "We. . . do kinda have sex?"
        elif KittyX.likes[StormX.tag] >= 900:
            ch_k "She's got[KittyX.like]totally thicc. . ."
        elif KittyX.likes[StormX.tag] >= 800:
            ch_k "She's really amazing. . ."
        elif KittyX.likes[StormX.tag] >= 700:
            ch_k "We're[KittyX.like]close friends."
        elif KittyX.likes[StormX.tag] >= 600:
            ch_k "She's[KittyX.like]my favorite teacher."
        elif KittyX.likes[StormX.tag] >= 500:
            ch_k "She's[KittyX.like]OK."
        elif KittyX.likes[StormX.tag] >= 400:
            ch_k "She gives out[KittyX.like]way too much homework."
        elif KittyX.likes[StormX.tag] >= 300:
            ch_k "Ugh, that bitch."
        else:
            ch_k "That whore?"
    elif Check == JubesX:
        if "poly Jubes" in KittyX.traits:
            ch_k "You know we[KittyX.like]make out sometimes. . ."
        elif KittyX.likes[JubesX.tag] >= 900:
            ch_k "She's[KittyX.like]such a beast. . ."
        elif KittyX.likes[JubesX.tag] >= 800:
            ch_k "We're pretty tight lately. . ."
        elif KittyX.likes[JubesX.tag] >= 700:
            ch_k "She's[KittyX.like]a really good friend."
        elif KittyX.likes[JubesX.tag] >= 600:
            ch_k "We're[KittyX.like]teammates."
        elif KittyX.likes[JubesX.tag] >= 500:
            ch_k "She's not[KittyX.like]a total jerk."
        elif KittyX.likes[JubesX.tag] >= 400:
            ch_k "I'm kinda[KittyX.like]done with her."
        elif KittyX.likes[JubesX.tag] >= 300:
            ch_k "Bite girl?"
        else:
            ch_k "Bitch in heat."

    return

label Kitty_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "monogamous" not in KittyX.traits:
            if KittyX.thirst >= 60 and not approval_check(KittyX, 1700, "LO", taboo_modifier=0):

                $ KittyX.change_face("_sly",1)
                if "monogamous" not in KittyX.daily_history:
                    $ KittyX.change_stat("obedience", 90, -2)
                ch_k "I[KittyX.like]appreciate the interest, but you aren't around enough. . ."
                return
            elif approval_check(KittyX, 1100, "LO", taboo_modifier=0) and KittyX.love >= KittyX.obedience:

                $ KittyX.change_face("_sly",1)
                if "monogamous" not in KittyX.daily_history:
                    $ KittyX.change_stat("love", 90, 1)
                ch_k "Aw, is someone jellie?"
                ch_k "I guess I could take care of myself. . ."
            elif approval_check(KittyX, 600, "O", taboo_modifier=0):

                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "If you want. . ."
            else:

                $ KittyX.change_face("_sly",1,brows="_confused")
                ch_k "I'll hook up with who I want!"
                return
            if "monogamous" not in KittyX.daily_history:
                $ KittyX.change_stat("obedience", 90, 3)
            $ KittyX.add_word(1,0,"monogamous")
            $ KittyX.traits.append("monogamous")
        "Don't hook up with other girls." if "monogamous" not in KittyX.traits:
            if approval_check(KittyX, 800, "O", taboo_modifier=0):

                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "Ok."
            elif KittyX.thirst >= 60 and not approval_check(KittyX, 1700, "LO", taboo_modifier=0):

                $ KittyX.change_face("_sly",1)
                if "monogamous" not in KittyX.daily_history:
                    $ KittyX.change_stat("obedience", 90, -2)
                ch_k "I[KittyX.like]appreciate the interest, but you aren't around enough. . ."
                return
            elif approval_check(KittyX, 500, "O", taboo_modifier=0):

                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "If you want. . ."
            elif approval_check(KittyX, 1200, "LO", taboo_modifier=0):

                $ KittyX.change_face("_sly",1)
                ch_k "Rude much?"
                ch_k "Fine, I'll do it for you. . ."
            else:

                $ KittyX.change_face("_sly",1,brows="_confused")
                ch_k "I'll hook up with who I want!"
                return
            if "monogamous" not in KittyX.daily_history:
                $ KittyX.change_stat("obedience", 90, 3)
            $ KittyX.add_word(1,0,"monogamous")
            $ KittyX.traits.append("monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in KittyX.traits:
            if approval_check(KittyX, 650, "O", taboo_modifier=0):
                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "Right, gotcha."
            elif approval_check(KittyX, 800, "L", taboo_modifier=0):
                $ KittyX.change_face("_sly",1)
                ch_k "Not like you'd give me the time to do that. . ."
                ch_k "right?"
            else:
                $ KittyX.change_face("_sly",1,brows="_confused")
                if "monogamous" not in KittyX.daily_history:
                    $ KittyX.change_stat("love", 90, -2)
                ch_k "You're not the boss of my pussy!"
            if "monogamous" not in KittyX.daily_history:
                $ KittyX.change_stat("obedience", 90, 3)
            if "monogamous" in KittyX.traits:
                $ KittyX.traits.remove("monogamous")
            $ KittyX.add_word(1,0,"monogamous")
        "Never mind.":
            pass
    return



label Kitty_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ KittyX.change_face("_sly",1,brows="_confused")
    menu:
        ch_k "Um. . . I guess?"
        "Could you maybe just ask instead?" if "chill" not in KittyX.traits:
            if KittyX.thirst >= 60 and not approval_check(KittyX, 1500, "LO", taboo_modifier=0):

                $ KittyX.change_face("_surprised",2)
                if "chill" not in KittyX.daily_history:
                    $ KittyX.change_stat("obedience", 90, -2)
                ch_k "Well- Well maybe spend some more time with me!"
                $ KittyX.change_face("_angry",1,eyes="_side")
                return
            elif approval_check(KittyX, 900, "LO", taboo_modifier=0) and KittyX.love >= KittyX.obedience:

                $ KittyX.change_face("_sadside",1)
                if "chill" not in KittyX.daily_history:
                    $ KittyX.change_stat("love", 90, 1)
                ch_k "Sorry, [KittyX.player_petname]. . ."
                ch_k "I can't keep my hands to myself. . ."
                ch_k "I'll try though. . ."
            elif approval_check(KittyX, 400, "O", taboo_modifier=0):

                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "I guess. . ."
            else:

                $ KittyX.change_face("_sly",1)
                ch_k "I can't keep my hands to myself. . ."
                return
            if "chill" not in KittyX.daily_history:
                $ KittyX.change_stat("obedience", 90, 3)
            $ KittyX.add_word(1,0,"chill")
            $ KittyX.traits.append("chill")
        "Don't bother me like that." if "chill" not in KittyX.traits:
            if approval_check(KittyX, 900, "O", taboo_modifier=0):

                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "Ok."
            elif KittyX.thirst >= 60 and not approval_check(KittyX, 600, "O", taboo_modifier=0):

                $ KittyX.change_face("_angry",1)
                if "chill" not in KittyX.daily_history:
                    $ KittyX.change_stat("obedience", 90, -2)
                ch_k "Don't keep me waiting then!"
                return
            elif approval_check(KittyX, 400, "O", taboo_modifier=0):

                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "Fine. . ."
            elif approval_check(KittyX, 500, "LO", taboo_modifier=0) and not approval_check(KittyX, 500, "I", taboo_modifier=0):

                $ KittyX.change_face("_sly",1)
                ch_k "Rude."
                ch_k ". . . I'll try though. . ."
            else:

                $ KittyX.change_face("_sly",1,brows="_confused")
                ch_k "I don't know. I guess we'll see. . ."
                return
            if "chill" not in KittyX.daily_history:
                $ KittyX.change_stat("obedience", 90, 3)
            $ KittyX.add_word(1,0,"chill")
            $ KittyX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(KittyX, 800, "L", taboo_modifier=0):
                $ KittyX.change_face("_sly",1)
                ch_k "Roger, roger. . ."
            elif approval_check(KittyX, 700, "O", taboo_modifier=0):
                $ KittyX.change_face("_sly",1,eyes="_side")
                ch_k "You bet!"
            else:
                $ KittyX.change_face("_sly",1,brows="_confused")
                if "chill" not in KittyX.daily_history:
                    $ KittyX.change_stat("love", 90, -2)
                ch_k "I don't know."
                ch_k "If I've got the time."
                ch_k "I guess."
            if "chill" not in KittyX.daily_history:
                $ KittyX.change_stat("obedience", 90, 3)
            if "chill" in KittyX.traits:
                $ KittyX.traits.remove("chill")
            $ KittyX.add_word(1,0,"chill")
        "Um, never mind.":
            pass
    return




label Kitty_Hungry:
    if KittyX.had_chat[3]:
        ch_k "You know, a kitty does like her milk. . ."
    elif KittyX.had_chat[2]:
        ch_k "You know, that serum of yours really has a kick to it. You should market that stuff!"
    else:
        ch_k "You know, a kitty does like her milk. . ."
    $ KittyX.traits.append("hungry")
return





label Kitty_sexchat:
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
                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "sex":
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "Yeah, I know that. . ."
                            elif KittyX.favorite_action == "sex":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 10)
                                ch_k "I really like it too!"
                            elif KittyX.action_counter["sex"] >= 5:
                                ch_k "Well I don't mind that."
                            elif not KittyX.action_counter["sex"]:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who's fucking you? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("_bemused")
                                ch_k "Heh, um, yeah, it's nice. . ."
                            $ KittyX.player_favorite_action = "sex"
                        "Anal.":

                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "anal":
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "So you've said. . ."
                            elif KittyX.favorite_action == "anal":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 10)
                                ch_k "I love it too!"
                            elif KittyX.action_counter["anal"] >= 10:
                                ch_k "Yeah, it's. . . nice. . ."
                            elif not KittyX.action_counter["anal"]:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who's fucking you? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("_bemused",eyes="_side")
                                ch_k "Heh, heh, yeah, um, it's ok. . ."
                            $ KittyX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "blowjob":
                                $ KittyX.change_stat("lust", 80, 3)
                                ch_k "Yeah, I know."
                            elif KittyX.favorite_action == "blowjob":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "I love your dick!"
                            elif KittyX.action_counter["blowjob"] >= 10:
                                ch_k "Yeah, you're pretty tasty."
                            elif not KittyX.action_counter["blowjob"]:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who's sucking your dick?! Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("_bemused")
                                ch_k "I'm. . . getting used to the taste. . ."
                            $ KittyX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "titjob":
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "Yeah, you've said that before. . ."
                            elif KittyX.favorite_action == "titjob":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 7)
                                ch_k "Yeah, I enjoy that too. . ."
                            elif KittyX.action_counter["titjob"] >= 10:
                                ch_k "It's certainly an interesting experience . . ."
                            elif not KittyX.action_counter["titjob"]:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who's titfucking you? It's Ms. Frost, isn't it!"
                            else:
                                $ KittyX.change_face("_bemused")
                                ch_k "That's nice of you to say. . ."
                                $ KittyX.change_stat("love", 80, 5)
                                $ KittyX.change_stat("inhibition", 50, 10)
                            $ KittyX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "footjob":
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "Yeah, you've said that. . ."
                            elif KittyX.favorite_action == "footjob":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 7)
                                ch_k "You do feel pretty nice. . ."
                            elif KittyX.action_counter["footjob"] >= 10:
                                ch_k "I like it too . . ."
                            elif not KittyX.action_counter["footjob"]:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who's playing footsie with you? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("_bemused")
                                ch_k "Yeah, it's nice. . ."
                            $ KittyX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "handjob":
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "Yeah, you've said that. . ."
                            elif KittyX.favorite_action == "handjob":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 7)
                                ch_k "You do feel pretty comfy. . ."
                            elif KittyX.action_counter["handjob"] >= 10:
                                ch_k "I like it too . . ."
                            elif not KittyX.action_counter["handjob"]:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who's jerking you off? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("_bemused")
                                ch_k "Yeah, it's nice. . ."
                            $ KittyX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = KittyX.action_counter["fondle_breasts"]+ KittyX.action_counter["fondle_thighs"]+ KittyX.action_counter["suck_breasts"] + KittyX.action_counter["hotdog"]
                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "fondle":
                                $ KittyX.change_stat("lust", 80, 3)
                                ch_k "Yeah, I think we're clear on that. . ."
                            elif KittyX.favorite_action in ("hotdog","suck_breasts","fondle_breasts","fondle_thighs"):
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "I love when you touch me. . ."
                            elif counter >= 10:
                                ch_k "Yeah, it's really nice . . ."
                            elif not counter:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who's letting you feel her up? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("_bemused")
                                ch_k "I do like how that feels. . ."
                            $ KittyX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ KittyX.change_face("_sly")
                            if KittyX.player_favorite_action == "kiss":
                                $ KittyX.change_stat("love", 90, 3)
                                ch_k "Such a romantic. . ."
                            elif KittyX.favorite_action == "kiss":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("lust", 80, 5)
                                ch_k "Hmm, the taste of you on my lips. . ."
                            elif KittyX.action_counter["kiss"] >= 10:
                                ch_k "I love kissing you too . . ."
                            elif not KittyX.action_counter["kiss"]:
                                $ KittyX.change_face("_perplexed")
                                ch_k "Who are you kissing? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("_bemused")
                                ch_k "I like kissing you too. . ."
                            $ KittyX.player_favorite_action = "kiss"

                    $ KittyX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(KittyX, 800):
                    $ KittyX.change_face("_perplexed")
                    ch_k "Rude."
                else:
                    if KittyX.SEXP >= 50:
                        $ KittyX.change_face("_sly")
                        ch_k "You should know that. . ."
                    else:
                        $ KittyX.change_face("_bemused")
                        $ KittyX.eyes = "_side"
                        ch_k "Hmm, I don't know. . ."


                    if not KittyX.favorite_action or KittyX.favorite_action == "kiss":
                        ch_k "I do love it when we kiss. . ."
                    elif KittyX.favorite_action == "anal":
                        if KittyX.action_counter["anal"] >= 10:
                            ch_k "I like when you. . . fuck my ass."
                        else:
                            ch_k "I like it. . . in the butt."
                    elif KittyX.favorite_action == "eat_ass":
                        ch_k "I like when you lick my. . . asshole."
                    elif KittyX.favorite_action == "finger_ass":
                        ch_k "I like when you . . . finger my asshole."
                    elif KittyX.favorite_action == "sex":
                        ch_k "I like when you fuck me."
                    elif KittyX.favorite_action == "eat_pussy":
                        ch_k "I like when you lick my pussy."
                    elif KittyX.favorite_action == "fondle_pussy":
                        ch_k "I like when you finger me."
                    elif KittyX.favorite_action == "blowjob":
                        ch_k "I kinda like to suck your cock."
                    elif KittyX.favorite_action == "titjob":
                        ch_k "I don't mind using my tits."
                    elif KittyX.favorite_action == "footjob":
                        ch_k "I kinda like giving footjobs."
                    elif KittyX.favorite_action == "handjob":
                        ch_k "I like jerking you off."
                    elif KittyX.favorite_action == "hotdog":
                        ch_k "I like it when you grind against me."
                    elif KittyX.favorite_action == "suck_breasts":
                        ch_k "I like it when you suck on my tits."
                    elif KittyX.favorite_action == "fondle_breasts":
                        ch_k "I like it when you feel up my tits."
                    elif KittyX.favorite_action == "fondle_thighs":
                        ch_k "I like it when you massage my thighs."
                    else:
                        ch_k "I don't really know. . ."



            "Don't talk as much during sex." if "vocal" in KittyX.traits:
                if "setvocal" in KittyX.daily_history:
                    $ KittyX.change_face("_perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("_bemused")
                        $ KittyX.change_stat("obedience", 90, 1)
                        ch_k "Well, I guess I can be quieter. . ."
                        $ KittyX.traits.remove("vocal")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("_sadside")
                        $ KittyX.change_stat("obedience", 90, 1)
                        ch_k "Um, ok, [KittyX.player_petname]."
                        $ KittyX.traits.remove("vocal")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("_sly")
                        $ KittyX.change_stat("love", 90, -3)
                        $ KittyX.change_stat("obedience", 50, -1)
                        $ KittyX.change_stat("inhibition", 90, 5)
                        ch_k "You wish, [KittyX.player_petname]."
                    else:
                        $ KittyX.change_face("_angry")
                        $ KittyX.change_stat("love", 90, -5)
                        $ KittyX.change_stat("obedience", 60, -3)
                        $ KittyX.change_stat("inhibition", 90, 10)
                        ch_k "Oh, am I too {i}chatty{/i} when I'm getting you off?"

                    $ KittyX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in KittyX.traits:
                if "setvocal" in KittyX.daily_history:
                    $ KittyX.change_face("_perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("_sly")
                        $ KittyX.change_stat("obedience", 90, 2)
                        ch_k "Hmm, ok. . ."
                        $ KittyX.traits.append("vocal")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("_sadside")
                        $ KittyX.change_stat("obedience", 90, 2)
                        ch_k "I guess I could try, [KittyX.player_petname]."
                        $ KittyX.traits.append("vocal")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("_sly")
                        $ KittyX.change_stat("obedience", 90, 3)
                        ch_k "I guess I could, [KittyX.player_petname]."
                        $ KittyX.traits.append("vocal")
                    else:
                        $ KittyX.change_face("_angry")
                        $ KittyX.change_stat("inhibition", 90, 5)
                        ch_k "Hmm, I don't know about that."

                    $ KittyX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in KittyX.traits:
                if "initiative" in KittyX.daily_history:
                    $ KittyX.change_face("_perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("_bemused")
                        $ KittyX.change_stat("obedience", 90, 1)
                        ch_k "Heh, if you insist. . ."
                        $ KittyX.traits.append("passive")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("_sadside")
                        $ KittyX.change_stat("obedience", 90, 1)
                        ch_k "I'll try to hold back, [KittyX.player_petname]."
                        $ KittyX.traits.append("passive")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("_sly")
                        $ KittyX.change_stat("love", 90, -3)
                        $ KittyX.change_stat("obedience", 50, -1)
                        $ KittyX.change_stat("inhibition", 90, 5)
                        ch_k "You wish, [KittyX.player_petname]."
                    else:
                        $ KittyX.change_face("_angry")
                        $ KittyX.change_stat("love", 90, -5)
                        $ KittyX.change_stat("obedience", 60, -3)
                        $ KittyX.change_stat("inhibition", 90, 10)
                        ch_k "If I feel like it."

                    $ KittyX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in KittyX.traits:
                if "initiative" in KittyX.daily_history:
                    $ KittyX.change_face("_perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("_bemused")
                        $ KittyX.change_stat("obedience", 90, 1)
                        ch_k "Heh, I'll see what I can do. . ."
                        $ KittyX.traits.remove("passive")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("_sadside")
                        $ KittyX.change_stat("obedience", 90, 1)
                        ch_k "I can do that, [KittyX.player_petname]."
                        $ KittyX.traits.remove("passive")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("_sly")
                        $ KittyX.change_stat("obedience", 90, 3)
                        ch_k "I can try, [KittyX.player_petname]."
                        $ KittyX.traits.remove("passive")
                    else:
                        $ KittyX.change_face("_angry")
                        $ KittyX.change_stat("inhibition", 90, 5)
                        ch_k "You're not my supervisor!"

                    $ KittyX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in KittyX.history:
                call Kitty_Jumped
            "About when you masturbate":
                call NoFap (KittyX)

            "Never Mind" if line == "Yeah, what did you want to talk about?":
                return
            "That's all." if line != "Yeah, what did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return




label Kitty_Chitchat(O=0, Options=["default","default","default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:

        if KittyX not in phonebook:
            if approval_check(KittyX, 500, "L") or approval_check(KittyX, 250, "I"):
                ch_k "You know, I never got around to giving you my number, here you go."
                $ phonebook.append(KittyX)
                return
            elif approval_check(KittyX, 250, "O"):
                ch_k "You know, you should probably have my number, here you go."
                $ phonebook.append(KittyX)
                return

        if "hungry" not in KittyX.traits and (KittyX.event_counter["swallowed"] + KittyX.had_chat[2]) >= 10 and KittyX.location == bg_current:
            call Kitty_Hungry
            return
        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not taboo or approval_check(KittyX, 800, "I")):
            if KittyX.location == bg_current and KittyX.thirst >= 30 and "refused" not in KittyX.daily_history and "quicksex" not in KittyX.daily_history:
                $ Girl.change_face("_smile",2,brows="_sad")
                ch_k "Hey, um . . . did you want to. . ."
                ch_k ". . . sex?"
                call Quick_Sex (KittyX)
                return





        if KittyX.event_happened[0] and "key" not in KittyX.had_chat:
            $ Options.append("key")
        if "lover" in KittyX.player_petnames and approval_check(KittyX, 900, "L"):
            $ Options.append("luv")
        if "Kate" in KittyX.names and "Katherine" not in KittyX.names:

            $ Options.append("Katherine")
        if KittyX.level >= 3 and "Shadowcat" not in KittyX.names:

            $ Options.append("Shadowcat")

        if "mandrill" in Player.traits and "cologne chat" not in KittyX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in KittyX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in KittyX.daily_history:
            $ Options.append("corruption")

        if "seenpeen" in KittyX.history:
            $ Options.append("seenpeen")
        if "topless" in KittyX.history:
            $ Options.append("topless")
        if "bottomless" in KittyX.history:
            $ Options.append("bottomless")

        if KittyX.went_on_date >= 1 and bg_current != "bg_restaurant":

            $ Options.append("dated")
        if "cheek" in KittyX.daily_history and "cheek" not in KittyX.had_chat:

            $ Options.append("cheek")
        if KittyX.action_counter["kiss"] >= 5:

            $ Options.append("kissed")
        if "kappa" in Player.history:
            $ Options.append("kappa")
        if "dangerroom" in Player.daily_history:

            $ Options.append("dangerroom")
        if "showered" in KittyX.daily_history:

            $ Options.append("showercaught")
        if "fondle_breasts" in KittyX.daily_history or "fondle_pussy" in KittyX.daily_history or "fondle_ass" in KittyX.daily_history:

            $ Options.append("fondled")
        if "Dazzler and Longshot" in KittyX.inventory and "256 Shades of Grey" in KittyX.inventory and "Avengers Tower Penthouse" in KittyX.inventory:

            if "book" not in KittyX.had_chat:
                $ Options.append("booked")
        if "_lace_bra" in KittyX.inventory or "_lace_panties" in KittyX.inventory:

            if "lingerie" not in KittyX.had_chat:
                $ Options.append("lingerie")
        if KittyX.action_counter["handjob"]:

            $ Options.append("handy")
        if KittyX.event_counter["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in KittyX.daily_history or "painted" in KittyX.daily_history:

            $ Options.append("facial")
        if KittyX.event_counter["sleepover"]:

            $ Options.append("sleepwear")
        if KittyX.event_counter["creampied"] or KittyX.event_counter["anal_creampied"]:

            $ Options.append("creampie")
        if KittyX.action_counter["sex"] or KittyX.action_counter["anal"]:

            $ Options.append("sexed")
        if KittyX.action_counter["anal"]:

            $ Options.append("anal")




        if (bg_current == "bg_kitty" or bg_current == "bg_player") and "relationship" not in KittyX.daily_history:
            if "lover" not in KittyX.player_petnames and KittyX.love >= 950 and KittyX.event_happened[6] != 20:
                $ Options.append("lover?")
            elif "sir" not in KittyX.player_petnames and KittyX.obedience >= 500 and "sir" not in KittyX.history:
                $ Options.append("sir?")
            elif "daddy" not in KittyX.player_petnames and approval_check(KittyX, 750, "L") and approval_check(KittyX, 500, "O") and approval_check(KittyX, 500, "I"):
                $ Options.append("daddy?")
            elif "master" not in KittyX.player_petnames and KittyX.obedience >= 800 and "sir" in KittyX.player_petnames and "master" not in KittyX.history:
                $ Options.append("master?")
            elif "sex friend" not in KittyX.player_petnames and approval_check(KittyX, 500, "I"):
                $ Options.append("sexfriend?")


        if not approval_check(KittyX, 300):
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)

    if Options[0] == "mandrill":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("_confused")
        ch_k "(sniff, sniff). . . is that. . . chimp? . . ."
        $ KittyX.change_face("_perplexed", 1)
        ch_k ". . . but it's[KittyX.like]. . . {i}sexy{/i} chimp?"
    elif Options[0] == "purple":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("_sly",1)
        ch_k "(sniff, sniff). . . huh, what's that smell? . ."
        ch_k ". . . could I get you something?"
    elif Options[0] == "corruption":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("_confused")
        ch_k "(sniff, sniff). . . that's pretty overpowering. . ."
        $ KittyX.change_face("_sly")
        ch_k ". . . I may not be able to keep my hands to myself. . ."

    elif Options[0] == "caught":
        if "caught chat" in KittyX.had_chat:
            ch_k "We've really got to stop making a habit of getting caught."
            if not approval_check(KittyX, 500, "I"):
                ch_k "Or not. . ."
        else:
            ch_k "I did not enjoy getting dragged to the Professor's office like that."
            if not approval_check(KittyX, 500, "I"):
                ch_k "I don't know about doing it in public anymore."
            else:
                ch_k "It was kind of hot though. . ."
            $ KittyX.had_chat.append("caught chat")
    elif Options[0] == "key":
        if KittyX.SEXP <= 15:
            ch_k "I'm glad you have my key now, just don't use it for any funny business. . ."
        else:
            ch_k "I'm glad you have my key now, maybe you could . . . \"surprise\" me sometime. . ."
        $ KittyX.had_chat.append("key")

    elif Options[0] == "cheek":

        ch_k "So,[KittyX.player_petname]. . .y'know how you[KittyX.like]kinda just brushed my cheek before?"
        ch_p "Yeah? Was that okay?"
        $ KittyX.change_face("_smile",1)
        ch_k "More than just {i}okay{/i}."
        $ KittyX.had_chat.append("cheek")

    elif Options[0] == "dated":

        ch_k "Heya,[KittyX.player_petname]. I[KittyX.like]had a lot of fun last night. We should do that again sometime."

    elif Options[0] == "kissed":

        $ KittyX.change_face("_sly",1)
        ch_k "[KittyX.Like]. . .anybody ever tell you how good a kisser you are, [KittyX.player_petname]?"
        menu:
            extend ""
            "Hey. . .when you're good, you're good.":
                $ KittyX.change_face("_smile",1)
                ch_k "I think maybe you can show me {i}how{/i} good[KittyX.like]whenever you want."
            "No. You think?":
                ch_k "Yeah. I do. [KittyX.Like]a {i}lot{/i}."

    elif Options[0] == "dangerroom":

        $ KittyX.change_face("_sly",1)
        ch_k "Hey,[KittyX.player_petname]. I watched you working out in the Danger Room, earlier. You looked[KittyX.like]{i}so{/i} cute in your X-Men uniform!"

    elif Options[0] == "showercaught":

        if "shower" in KittyX.had_chat:
            ch_k "Hope you liked the view earlier. . ."
        else:
            ch_k "So, you run into a lot of people in the shower. . .or just[KittyX.like]me?"
            $ KittyX.had_chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    $ KittyX.change_stat("love", 50, 5)
                    $ KittyX.change_stat("love", 90, 2)
                    if approval_check(KittyX, 1200):
                        $ KittyX.change_face("_sly",1)
                        ch_k "Yeah? {i}Maybe{/i} you should[KittyX.like]have accidents like that more often."
                    $ KittyX.change_face("_smile")
                    ch_k "It's cool, [KittyX.player_petname]. Eveybody makes mistakes. . . sometimes."
                "Just you.":
                    $ KittyX.change_stat("obedience", 40, 5)
                    if approval_check(KittyX, 1000) or approval_check(KittyX, 700, "L"):
                        $ KittyX.change_stat("love", 90, 3)
                        $ KittyX.change_face("_sly",1)
                        ch_k "You know how to make a girl feel special, [KittyX.player_petname]."
                    else:
                        $ KittyX.change_stat("love", 70, -5)
                        $ KittyX.change_face("_angry")
                        ch_k "You're {i}such{/i} a creep, [Player.name], y'know that?"
                "Totally on purpose. I regret nothing.":
                    if approval_check(KittyX, 1200):
                        $ KittyX.change_stat("love", 90, 3)
                        $ KittyX.change_stat("obedience", 70, 10)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        $ KittyX.change_face("_sly",1)
                        ch_k "Hmm. . .next time, we'll have to[KittyX.like]take advantage of the moment."
                    elif approval_check(KittyX, 800):
                        $ KittyX.change_stat("obedience", 60, 5)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        $ KittyX.change_face("_perplexed",2)
                        ch_k "Wha. . . um. . . okay?"
                        $ KittyX.blushing = "_blush1"
                    else:
                        $ KittyX.change_stat("love", 50, -10)
                        $ KittyX.change_stat("love", 80, -10)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_face("_angry")
                        ch_k "You're such a creep, [KittyX.player_petname], y'know that?"

    elif Options[0] == "fondled":

        if KittyX.action_counter["fondle_breasts"]+ KittyX.action_counter["fondle_pussy"] + KittyX.action_counter["fondle_ass"] >= 15:
            ch_k "I want your hands on me."
        else:
            ch_k "You know how you felt me up earlier? I could kinda[KittyX.like]get used to having your hands on me."

    elif Options[0] == "booked":

        ch_k "So.I[KittyX.like]read the books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ KittyX.change_face("_sly",2)
                ch_k "They were[KittyX.like]. . .{i}interesting{/i}."
            "Good. You looked like you could use to learn a thing or two from them.":
                $ KittyX.change_stat("love", 90, -3)
                $ KittyX.change_stat("obedience", 70, 5)
                $ KittyX.change_stat("inhibition", 50, 5)
                $ KittyX.change_face("_angry")
                ch_k "Guess {i}you'll{/i} never find out, huh?"
        $ KittyX.blushing = "_blush1"
        $ KittyX.had_chat.append("book")

    elif Options[0] == "lingerie":

        $ KittyX.change_face("_sly",2)
        ch_k "[KittyX.player_petname], I wanted to thank you again for the. . .{i}stuff{/i} you bought me. They're so cute!"
        $ KittyX.blushing = "_blush1"
        $ KittyX.had_chat.append("lingerie")

    elif Options[0] == "handy":

        $ KittyX.change_face("_sly",2)
        ch_k "I was just thinking about how I[KittyX.like]stroked your cock the other day. . ."
        ch_k "I loved the expression on your face. . .knowing I could[KittyX.like]make you {i}feel{/i} like that."
        $ KittyX.blushing = "_blush1"

    elif Options[0] == "blowjob":
        if "blowjob" not in KittyX.had_chat:

            $ KittyX.change_face("_sly",2)
            ch_k "So. . .uhm, be honest with me, [KittyX.player_petname]?"
            ch_k "When I gave you head. . . was it any good?"
            ch_k "I kinda had a hard time getting all of you into my mouth."
            menu:
                extend ""
                "You were totally amazing.":
                    $ KittyX.change_stat("love", 90, 5)
                    $ KittyX.change_stat("inhibition", 60, 10)
                    $ KittyX.change_face("_sexy",1)
                    ch_k "Awesome. 'Cause I can't wait to try again."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(KittyX, 300, "I") or not approval_check(KittyX, 800):
                        $ KittyX.change_stat("love", 90, -5)
                        $ KittyX.change_stat("obedience", 60, 10)
                        $ KittyX.change_stat("inhibition", 50, 10)
                        $ KittyX.change_face("_perplexed",1)
                        ch_k "Yeah? Well then maybe I'll get some practice in before we do it again."
                    else:
                        $ KittyX.change_stat("obedience", 70, 15)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        $ KittyX.change_face("_sexy",1)
                        ch_k "Yeah? Well, I'm[KittyX.player_petname]looking forward our next training session, then."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 60, 10)
                    $ KittyX.change_face("_angry",2)
                    ch_k "Guess you're gonna have to[KittyX.like]figure out a way to get it to suck itself then from now on. . .{i}jerk{/i}."
            $ KittyX.blushing = "_blush1"
            $ KittyX.had_chat.append("blowjob")
        else:
            $ line = renpy.random.choice(["You know, I kinda like how you taste.",
                            "You're a real jaw-breaker.",
                            "Let me know if you want some more lollipop licks.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_k "[line]"

    elif Options[0] == "swallowed":

        if "swallow" in KittyX.had_chat:
            ch_k "I'd like another taste sometime."
        else:
            ch_k "So. . .I was[KittyX.like]just thinking about the other day."
            ch_k "Y'know, that was the first time I[KittyX.like]swallowed."
            $ KittyX.change_face("_sly",1)
            ch_k "Not bad. . ."
            $ KittyX.had_chat.append("swallow")

    elif Options[0] == "facial":

        ch_k "Hey. . .this is gonna sound kinda[KittyX.like]weird, but. . ."
        $ KittyX.change_face("_sexy",2)
        ch_k "I feel so {i}sexy{/i} when you cum on my face."
        $ KittyX.blushing = "_blush1"

    elif Options[0] == "sleepover":

        ch_k "I[KittyX.like] totally can't stop thinking about the other night."
        ch_k "It was {i}so{/i} perfect."

    elif Options[0] == "creampie":

        "[KittyX.name] draws close to you so she can whisper into your ear."
        ch_k "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":

        ch_k "So. . .I want you to know something. . ."
        $ KittyX.change_face("_sexy",2)
        ch_k ". . .[KittyX.Like]every time I masturbate. . ."
        ch_k "I think about how it felt, with you inside of me."
        $ KittyX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ KittyX.change_face("_sly",2)
        ch_k "Y'know. . .after the other night, I'm kinda having trouble[KittyX.like]sitting down."
        $ KittyX.change_face("_sexy",2)
        ch_k "{i}Totally{/i} worth it, though."
        $ KittyX.blushing = "_blush1"
    elif Options[0] == "kappa":

        ch_k "You know how Xavier[KittyX.like]caught us last time?"
        ch_k "I bet if we had some dirt on him, we could get him to lay off. . ."
        ch_k "Maybe he has something in his office. . ."
    elif Options[0] == "Shadowcat":
        $ KittyX.names.append("Shadowcat")
        ch_k "You know, in the field I go by \"Shadowcat.\""
        menu:
            extend ""
            "Oh, ok then.":
                $ KittyX.change_face("_perplexed", 1)
                $ KittyX.change_stat("love", 60, 2)
                ch_k ". . ."
            "Yeah, I know.":
                $ KittyX.change_stat("love", 90, 5)
            "Huh, why not go by that then?":
                if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                    $ KittyX.name = "Shadowcat"
                    $ KittyX.change_stat("obedience", 90, 5)
                    ch_k "I guess? . ."
                else:
                    ch_k "Kind of a silly name to go around with. . ."
                    menu:
                        extend ""
                        "Ok, \"[KittyX.name]\" it is then.":
                            $ KittyX.change_face("_smile", 1)
                        "I insist.":
                            $ KittyX.change_stat("love", 90, -10)
                            $ KittyX.change_stat("obedience", 50, 10)
                            $ KittyX.change_face("_angry", 2)
        ch_k ". . ."

    elif Options[0] == "Katherine":
        $ KittyX.names.append("Katherine")
        ch_k "My full name is \"Katherine Pryde.\""
        ch_k "You probably didn't know that."
        menu:
            extend ""
            "Oh, ok then.":
                $ KittyX.change_face("_perplexed", 1)
                $ KittyX.change_stat("love", 60, 2)
                ch_k ". . ."
            "I kind of prefer \"[KittyX.name].\"":
                $ KittyX.change_stat("love", 90, 5)
                $ KittyX.change_stat("inhibition", 50, 5)
                if approval_check(KittyX, 800, "LO"):
                    $ KittyX.change_stat("obedience", 70, 5)
                ch_k "Yeah, me too. . ."
            "Why not go by \"Katherine\" then?":
                if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                    $ KittyX.name = "Katherine"
                    $ KittyX.change_stat("obedience", 90, 5)
                    ch_k "I suppose I could. . ."
                else:
                    ch_k "I don't really like it that much. . ."
                    menu:
                        extend ""
                        "Ok, \"[KittyX.name]\" it is then.":
                            $ KittyX.change_face("_smile", 1)
                        "I insist.":
                            $ KittyX.change_stat("love", 90, -10)
                            $ KittyX.change_stat("obedience", 50, 10)
                            $ KittyX.change_face("_angry", 2)
                            ch_k "!!!"


    elif Options[0] == "seenpeen":
        $ KittyX.change_face("_sly",2)
        ch_k "Maybe I didn't mention it before, but. . ."
        ch_k "That cock of yours is. . . impressive."
        $ KittyX.change_face("_bemused",1)
        $ KittyX.change_stat("love", 90, 3)
        $ KittyX.history.remove("seenpeen")
    elif Options[0] == "topless":
        $ KittyX.change_face("_bemused",2,eyes="_side")
        ch_k "Hey, when you saw me. . . topless earlier, you didn't have much to say. . ."
        ch_k "What'd you think?"
        call Kitty_First_TMenu
        $ KittyX.history.remove("topless")
    elif Options[0] == "bottomless":
        $ KittyX.change_face("_bemused",2,eyes="_side")
        ch_k "Hey, when you saw my. . . pussy earlier. . ."
        ch_k "You didn't say much. . . "
        ch_k "What'd you think?"
        call Kitty_First_BMenu
        $ KittyX.history.remove("bottomless")

    elif Options[0] == "boyfriend?":
        call Kitty_BF
    elif Options[0] == "lover?":
        call Kitty_Love
    elif Options[0] == "sir?":
        call Kitty_Sub
    elif Options[0] == "master?":
        call Kitty_Master
    elif Options[0] == "sexfriend?":
        call Kitty_sexfriend
    elif Options[0] == "fuckbuddy?":
        call Kitty_Fuckbuddy
    elif Options[0] == "daddy?":
        call Kitty_Daddy

    elif Options[0] == "hate":
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want to see your face.",
                "Stop bothering me.",
                "Leave me alone."])
        ch_k "[line]"
    else:

        $ D20 = renpy.random.randint(1, 15)
        if D20 == 1:
            $ KittyX.change_face("_smile")
            ch_k "I'm[KittyX.like]{i}so{/i} excited [KittyX.player_petname]! I {i}totally{/i} aced Professor McCoy's Computer Science test!"
        elif D20 == 2:
            $ KittyX.change_face("_sad")
            ch_k "Ever have[KittyX.like]one of those days where it seems like the whole world's out to get you?"
        elif D20 == 3:
            $ KittyX.change_face("_surprised")
            ch_k "I can't believe how much stuff I've gotta get done today!"
        elif D20 == 4:
            $ KittyX.change_face("_sad")
            ch_k "Hey, [KittyX.player_petname]. I got[KittyX.like]the world's worst sleep last night. I feel like I could[KittyX.like]curl up and go to bed right here."
        elif D20 == 5:
            $ KittyX.change_face("_smile")
            ch_k "Wow! Isn't it[KittyX.like]{i}so{/i} nice out right now?"
        elif D20 == 6:
            $ KittyX.change_face("_perplexed")
            ch_k "I had[KittyX.like]the worst nightmare last night. I dreamed the N'Garai demon was chasing me throught the Mansion!"
        elif D20 == 7:
            $ KittyX.change_face("_smile")
            ch_k "So awesome. I have[KittyX.like]a lunch date tomorrow with my total bestie!"
        elif D20 == 8:
            $ KittyX.change_face("_sad")
            ch_k "Y'know, I totally love it here in Salem Center. But I have to admit. . .I kinda miss Deerfield sometimes."
        elif D20 == 9:
            $ KittyX.change_face("_confused")
            ch_k "So weird. Ever since Professor Xavier telepathically taught me Russian, I kinda find myself[KittyX.like]daydreaming in Cyrillic."
        elif D20 == 10:
            $ KittyX.change_face("_smile")
            ch_k "{i}So{/i} nerdy, I know. But I[KittyX.like]totally had the best idea for this OS I'm writing for the Mansion's computers in the shower today!"
        elif D20 == 11:
            $ KittyX.change_face("_smile")
            ch_k "I[KittyX.like]totally can't wait 'til dance class tomorrow! We're starting modern this semester!"
        elif D20 == 12:
            $ KittyX.change_face("_sad")
            ch_k "I heard a few of the others are going to Harry's Hideaway tomorrow. I have[KittyX.like]{i}so{/i} much homework to do, though!"
        elif D20 == 13:
            $ KittyX.change_face("_smile")
            ch_k "This probably sounds[KittyX.like]totally random, but, I could {i}so{/i} go for ice cream right now!"
        elif D20 == 14:
            $ KittyX.change_face("_sad")
            ch_k "I hate thinking about how so many people[KittyX.like]totally hate mutants for no good reason. It's so depressing."
        elif D20 == 15:
            $ KittyX.change_face("_perplexed")
            ch_k "I think I[KittyX.like]tweaked something in my thigh in the Danger Room, yesterday. It feel like I have a bruise that goes right through it!"
        else:
            $ KittyX.change_face("_perplexed")
            ch_k "You're fun to hang with."

    $ line = 0
    return



label Kitty_names:
    menu:
        ch_k "Oh? What would you like me to call you?"
        "Sweetie's fine.":
            $ KittyX.player_petname = "sweetie"
            ch_k "You got it, sweetie."
        "My initial's fine.":
            $ KittyX.player_petname = Player.name[:1]
            ch_k "You got it, [KittyX.player_petname]."
        "Call me by my name.":
            $ KittyX.player_petname = Player.name
            ch_k "If you'd rather, [KittyX.player_petname]."
        "Call me \"boyfriend\"." if "boyfriend" in KittyX.player_petnames:
            $ KittyX.player_petname = "boyfriend"
            ch_k "Sure thing, [KittyX.player_petname]."
        "Call me \"lover\"." if "lover" in KittyX.player_petnames:
            $ KittyX.player_petname = "lover"
            ch_k "Oooh, love to, [KittyX.player_petname]."
        "Call me \"sir\"." if "sir" in KittyX.player_petnames:
            $ KittyX.player_petname = "sir"
            ch_k "Yes, [KittyX.player_petname]."
        "Call me \"master\"." if "master" in KittyX.player_petnames:
            $ KittyX.player_petname = "master"
            ch_k "As you wish, [KittyX.player_petname]."
        "Call me \"sex friend\"." if "sex friend" in KittyX.player_petnames:
            $ KittyX.player_petname = "sex friend"
            ch_k "Heh, very cheeky, [KittyX.player_petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in KittyX.player_petnames:
            $ KittyX.player_petname = "fuck buddy"
            ch_k "I'm game if you are, [KittyX.player_petname]."
        "Call me \"daddy\"." if "daddy" in KittyX.player_petnames:
            $ KittyX.player_petname = "daddy"
            ch_k "Oh! You bet, [KittyX.player_petname]."
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
                        $ KittyX.petname = "Kitty"
                        ch_k "I don't see why not, [KittyX.player_petname]."
                    "I think I'll call you \"girl\".":

                        $ KittyX.petname = "girl"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("_sexy", 1)
                            ch_k "I'm totally your girl, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry")
                            ch_k "I'm NOT your girl, [KittyX.player_petname]."
                    "I think I'll call you \"boo\".":

                        $ KittyX.petname = "boo"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("_sexy", 1)
                            ch_k "Aw, I am your boo, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry")
                            ch_k "I'm NOT your boo, [KittyX.player_petname]."
                    "I think I'll call you \"bae\".":

                        $ KittyX.petname = "bae"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("_sexy", 1)
                            ch_k "Aw, I am your bae, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry")
                            ch_k "I'm NOT your bae, [KittyX.player_petname]."
                    "I think I'll call you \"baby\".":

                        $ KittyX.petname = "baby"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("_sexy", 1)
                            ch_k "Aw, cute, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry")
                            ch_k "I'm not a baby!"
                    "I think I'll call you \"sweetie\".":


                        $ KittyX.petname = "sweetie"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            ch_k "Aw, that's sweet, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "Too saccharine, [KittyX.player_petname]."
                    "I think I'll call you \"sexy\".":

                        $ KittyX.petname = "_sexy"
                        if "lover" in KittyX.player_petnames or approval_check(KittyX, 900):
                            $ KittyX.change_face("_sexy", 1)
                            ch_k "Mreow, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "Not in public, [KittyX.player_petname]."
                    "I think I'll call you \"lover\".":

                        $ KittyX.petname = "lover"
                        if "lover" in KittyX.player_petnames or approval_check(KittyX, 900, "L") or approval_check(KittyX, 1400):
                            $ KittyX.change_face("_sexy", 1)
                            ch_k "Love you too, [KittyX.player_petname]!"
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "Not in this lifetime, [KittyX.player_petname]."
                    "I think I'll call you \"kitten\".":

                        $ KittyX.petname = "baby"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("_sexy", 1)
                            ch_k "Purrr, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry")
                            ch_k "Not really that cute, [KittyX.player_petname]"
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you \"slave\".":
                        $ KittyX.petname = "slave"
                        if "master" in KittyX.player_petnames or approval_check(KittyX, 700, "O"):
                            $ KittyX.change_face("_bemused", 1)
                            ch_k "As you wish, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "I'm not a slave, [KittyX.player_petname]."
                    "I think I'll call you \"pet\".":

                        $ KittyX.petname = "pet"
                        if "master" in KittyX.player_petnames or approval_check(KittyX, 600, "O"):
                            $ KittyX.change_face("_bemused", 1)
                            ch_k "Hmm, make sure to pet me, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "I'm no house cat, [KittyX.player_petname]."
                    "I think I'll call you \"slut\".":

                        $ KittyX.petname = "slut"
                        if "sex friend" in KittyX.player_petnames or approval_check(KittyX, 1000, "OI"):
                            $ KittyX.change_face("_sexy")
                            ch_k "If the name fits, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            $ KittyX.mouth = "_surprised"
                            ch_k "Not unless you want to lose some teeth!"
                    "I think I'll call you \"whore\".":

                        $ KittyX.petname = "whore"
                        if "fuckbuddy" in KittyX.player_petnames or approval_check(KittyX, 1100, "OI"):
                            $ KittyX.change_face("_sly")
                            ch_k "Only for you though. . ."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "Can you say that with a fat lip, [KittyX.player_petname]?"
                    "I think I'll call you \"sugartits\".":

                        $ KittyX.petname = "sugartits"
                        if "sex friend" in KittyX.player_petnames or approval_check(KittyX, 1400):
                            $ KittyX.change_face("_sly", 1)
                            ch_k "These little things?"
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "I would hope not, [KittyX.player_petname]."
                    "I think I'll call you \"sex friend\".":

                        $ KittyX.petname = "sex friend"
                        if "sex friend" in KittyX.player_petnames or approval_check(KittyX, 600, "I"):
                            $ KittyX.change_face("_sly")
                            ch_k "Rreow. . ."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "Not out loud, [KittyX.player_petname]."
                    "I think I'll call you \"fuckbuddy\".":

                        $ KittyX.petname = "fuckbuddy"
                        if "fuckbuddy" in KittyX.player_petnames or approval_check(KittyX, 700, "I"):
                            $ KittyX.change_face("_sly")
                            ch_k "Yup."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            $ KittyX.mouth = "_surprised"
                            ch_k "Don't even joke, [KittyX.player_petname]."
                    "I think I'll call you \"baby girl\".":

                        $ KittyX.petname = "baby girl"
                        if "daddy" in KittyX.player_petnames or approval_check(KittyX, 1200):
                            $ KittyX.change_face("_smile", 1)
                            ch_k "You know it, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("_angry", 1)
                            ch_k "I'm no kid!"
                    "Back":

                        pass
            "Nevermind.":

                return
    return




label Kitty_Rename:

    $ KittyX.mouth = "_smile"
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
            if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                $ KittyX.name = "Katherine"
                if "namechange" not in KittyX.daily_history:
                    $ KittyX.change_stat("obedience", 70, 2)
                ch_k "I guess. . . I could?"
            else:
                ch_k "I don't really like that one. . ."
        "Do you go by \"Shadowcat?\"" if KittyX.name != "Shadowcat" and "Shadowcat" in KittyX.names:
            if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                $ KittyX.change_face("_confused")
                $ KittyX.name = "Shadowcat"
                ch_k "I guess. . . I could?"
            else:
                $ KittyX.change_face("_perplexed")
                ch_k "People don't exactly call me that out of the field!"
            $ KittyX.change_face()
        "Nevermind.":
            pass
    $ KittyX.add_word(1,0,"namechange")
    return




label Kitty_Personality(counter=0):
    if not KittyX.had_chat[4] or counter:
        "Since you're doing well in one area, you can convince [KittyX.name] to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_k "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if KittyX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_k "If[KittyX.like]that's what you want, I could be a bit more obedient."
            $ KittyX.had_chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if KittyX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_k "I could always be a bit more wild if that's what you want."
            $ KittyX.had_chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if KittyX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_k "Ok, I could open up more."
            $ KittyX.had_chat[4] = 3
        "More Loving. [[Obedience to Love]" if KittyX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_k "I'll try to."
            $ KittyX.had_chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if KittyX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_k "Oooh, kinky. . ."
            $ KittyX.had_chat[4] = 5

        "More Loving. [[Inhibition to Love]" if KittyX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_k "We do have fun together. . ."
            $ KittyX.had_chat[4] = 6

        "I guess just do what you like. . .[[reset]" if KittyX.had_chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_k "Um, ok."
            $ KittyX.had_chat[4] = 0
        "Repeat the rules":
            call Kitty_Personality (1)
            return
        "Nevermind.":
            return
    return







label Kitty_Summon(approval_bonus=approval_bonus):
    $ KittyX.change_outfit()
    if "no_summon" in KittyX.recent_history:
        if "_angry" in KittyX.recent_history:
            ch_k "Get a clue, [KittyX.player_petname]!"
        elif KittyX.recent_history.count("no_summon") > 1:
            ch_k "I'm telling you to give it a rest!"
            $ KittyX.recent_history.append("_angry")
        elif time_index >= 3:
            ch_k "Like I said, it's too late for that."
        else:
            ch_k "Like I told you, I'm busy."
        $ KittyX.recent_history.append("no_summon")
        return

    $ D20 = renpy.random.randint(1, 20)
    $ line = 0
    if KittyX.location == "bg_classroom":
        $ approval_bonus = -10
    elif KittyX.location == "bg_dangerroom":
        $ approval_bonus = -10
    elif KittyX.location == "bg_showerroom":
        $ approval_bonus = -30

    if D20 <= 3:

        $ line = "no"

    elif time_index >= 3:
        if approval_check(KittyX, 700, "L") or approval_check(KittyX, 300, "O"):

            ch_k "It's[KittyX.like]getting kinda late, but we can hang out for a bit."
            $ KittyX.location = bg_current
            call set_the_scene
        else:

            ch_k "It's kinda late? Maybe tomorrow."
            $ KittyX.recent_history.append("no_summon")
        return
    elif "lesbian" in KittyX.recent_history:

        if approval_check(KittyX, 2000):
            ch_k "I'm sorta with someone right now, [KittyX.player_petname], wanna join us?"
            menu:
                extend ""
                "Sure":
                    $ line = "go to"
                "No thanks.":
                    ch_k "K' then."
                    return
        else:
            ch_k "Um, no, everything's fine here, we're all good here."
            ch_k "Maybe I could see you in a bit?"
            $ KittyX.recent_history.append("no_summon")
            return
    elif not approval_check(KittyX, 700, "L") or not approval_check(KittyX, 600, "O"):

        if not approval_check(KittyX, 300):
            ch_k "I'm kinda busy, [KittyX.player_petname]."
            $ KittyX.recent_history.append("no_summon")
            return


        if "summoned" in KittyX.recent_history:
            pass
        elif "goto" in KittyX.recent_history:
            ch_k "You {i}just{/i} left here, why not come back?"
        elif KittyX.location == "bg_classroom":
            ch_k "I'm[KittyX.like]in class right now, [KittyX.player_petname], you up for it?"
        elif KittyX.location == "bg_dangerroom":
            ch_k "I'm in the Danger Room, [KittyX.player_petname], want in?"
        elif KittyX.location == "bg_campus":
            ch_k "I'm chillin in the quad, [KittyX.player_petname], want to come?"
        elif KittyX.location == "bg_kitty":
            ch_k "I'm in my room, [KittyX.player_petname], want to hang?"
        elif KittyX.location == "bg_player":
            ch_k "I'm in your room, [KittyX.player_petname],come home. . ."
        elif KittyX.location == "bg_showerroom":
            if approval_check(KittyX, 1600):
                ch_k "I'm[KittyX.like]in the shower right now, [KittyX.player_petname], want to get wet?"
            else:
                ch_k "I'm[KittyX.like]in the shower right now, [KittyX.player_petname], maybe we could touch base later."
                $ KittyX.recent_history.append("no_summon")
                return
        elif KittyX.location == "hold":
            ch_k "I'm[KittyX.like]kinda off the grid right now. Sorry?"
            $ KittyX.recent_history.append("no_summon")
            return
        else:
            ch_k "Why don't you come over here, [KittyX.player_petname]?"


        if "summoned" in KittyX.recent_history:
            ch_k "Ok, fiiiiine, but why are you dragging me all over?"
            $ line = "yes"
        elif "goto" in KittyX.recent_history:
            menu:
                extend ""
                "You're right, be right back.":
                    ch_k "KK, Cya!"
                    $ line = "go to"
                "Nah, it's better here.":
                    ch_k "OK."
                "But I'd {i}really{/i} like to see you over here.":
                    if approval_check(KittyX, 600, "L") or approval_check(KittyX, 1400):
                        $ line = "lonely"
                    else:
                        $ line = "no"
                "I said come over here.":
                    if approval_check(KittyX, 600, "O"):

                        $ line = "command"
                    elif D20 >= 7 and approval_check(KittyX, 1400):

                        ch_k "Ok, fine."
                        $ line = "yes"
                    elif approval_check(KittyX, 200, "O"):

                        ch_k "Whatever."
                        ch_k "Here I am if you want me."
                    else:

                        $ line = "no"
        else:
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ KittyX.change_stat("love", 55, 1)
                    $ KittyX.change_stat("inhibition", 30, 1)
                    ch_k "See ya!"
                    $ line = "go to"
                "Nah, we can talk later.":

                    $ KittyX.change_stat("obedience", 50, 1)
                    $ KittyX.change_stat("obedience", 30, 2)
                    ch_k "Oh, ok. Later then."
                "Could you please come visit me? I'm lonely.":

                    if approval_check(KittyX, 600, "L") or approval_check(KittyX, 1400):
                        $ KittyX.change_stat("love", 70, 1)
                        $ KittyX.change_stat("obedience", 50, 1)
                        $ line = "lonely"
                    else:
                        $ KittyX.change_stat("inhibition", 30, 1)
                        $ line = "no"
                "I said come over here.":

                    if approval_check(KittyX, 600, "O"):

                        $ KittyX.change_stat("love", 50, 1, 1)
                        $ KittyX.change_stat("love", 40, -1)
                        $ KittyX.change_stat("obedience", 90, 1)
                        $ line = "command"

                    elif D20 >= 7 and approval_check(KittyX, 1400):

                        $ KittyX.change_stat("love", 70, -2)
                        $ KittyX.change_stat("love", 90, -1)
                        $ KittyX.change_stat("obedience", 50, 2)
                        $ KittyX.change_stat("obedience", 90, 1)
                        ch_k "Ok, fine, [KittyX.player_petname]."
                        $ line = "yes"

                    elif approval_check(KittyX, 200, "O"):

                        $ KittyX.change_stat("love", 70, -4)
                        $ KittyX.change_stat("love", 90, -2)
                        ch_k "You're not my supervisor!"
                        $ KittyX.change_stat("inhibition", 40, 2)
                        $ KittyX.change_stat("inhibition", 60, 1)
                        $ KittyX.change_stat("obedience", 70, -2)
                        ch_k "You know where to find me."
                    else:

                        $ KittyX.change_stat("inhibition", 30, 1)
                        $ KittyX.change_stat("inhibition", 50, 1)
                        $ KittyX.change_stat("love", 50, -1, 1)
                        $ KittyX.change_stat("obedience", 70, -1)
                        $ line = "no"
    else:


        if KittyX.love > KittyX.obedience:
            ch_k "Sure!"
        else:
            ch_k "Ok, be there in a gif, [KittyX.player_petname]."
        $ line = "yes"

    $ approval_bonus = 0

    if not line:

        $ KittyX.recent_history.append("no_summon")
        return

    if line == "no":

        if KittyX.location == "bg_classroom":
            ch_k "I[KittyX.like]really need to study, [KittyX.player_petname]."
        elif KittyX.location == "bg_dangerroom":
            ch_k "I'm just getting a workout in."
        else:
            ch_k "I'm sorry, [KittyX.player_petname], but I'm kinda busy."
        $ KittyX.recent_history.append("no_summon")
        return

    elif line == "go to":

        $ renpy.pop_call()
        $ KittyX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        $ line = 0
        if KittyX.location == "bg_classroom":
            ch_k "I'll hold a seat for you!"
            jump classroom
        elif KittyX.location == "bg_dangerroom":
            ch_k "I'll be warming up!"
            jump danger_room
        elif KittyX.location == "bg_kitty":
            ch_k "I'll clean up a few things."
            $ Girl = KittyX
            jump girls_room
        elif KittyX.location == "bg_player":
            ch_k "I'll be here for you."
            jump player_room
        elif KittyX.location == "bg_showerroom":
            ch_k "I guess I'll be lathering up."
            jump shower_room
        elif KittyX.location == "bg_campus":
            ch_k "I've got a nice spot in the shade."
            jump campus
        elif KittyX.location in personal_rooms:
            ch_k "See ya' in a bit. . ."
            $ bg_current = KittyX.location
            jump reset_location
        else:
            ch_k "You know, I'll just meet you in my room."
            $ KittyX.location = "bg_kitty"
            $ Girl = KittyX
            jump girls_room


    elif line == "lonely":
        ch_k "Awwww, how sweet!"
    elif line == "command":
        ch_k "Very well, [KittyX.player_petname]."

    $ KittyX.recent_history.append("summoned")
    $ line = 0
    if "locked" in Player.traits:
        call locked_door (KittyX)
        return
    call taboo_level(taboo_location = False)
    $ KittyX.location = bg_current
    $ KittyX.change_outfit()
    call taboo_level(taboo_location = False)
    call set_the_scene
    return




label Kitty_Leave(approval_bonus=approval_bonus, GirlsNum=0):
    if "leaving" in KittyX.recent_history:
        $ KittyX.drain_word("leaving")
    else:
        return

    if KittyX.location == "hold":

        ch_k "I'm[KittyX.like]going off the grid, see you later."
        return

    if KittyX in Party or "lockedtravels" in KittyX.traits:


        $ KittyX.location = bg_current
        return

    elif "freetravels" in KittyX.traits or not approval_check(KittyX, 700):

        $ KittyX.change_outfit()
        if GirlsNum:
            ch_k "Yeah, I'm headed out too."

        if KittyX.location == "bg_classroom":
            ch_k "I'm[KittyX.like]headed to class right now."
        elif KittyX.location == "bg_dangerroom":
            ch_k "I'm[KittyX.like]hitting the danger room."
        elif KittyX.location == "bg_campus":
            ch_k "I'm[KittyX.like]going to hang out on campus."
        elif KittyX.location == "bg_kitty":
            ch_k "I'm[KittyX.like]heading back to my room."
        elif KittyX.location == "bg_player":
            ch_k "I'll[KittyX.like]be heading to your room."
        elif KittyX.location == "bg_pool":
            ch_k "I'm[KittyX.like]hitting up the pool."
        elif KittyX.location == "bg_showerroom":
            if approval_check(KittyX, 1400):
                ch_k "I'm catching a shower, later!"
            else:
                ch_k "I'm outta here, later!"
        else:
            ch_k "I'm headed out, see you later."
        hide Kitty_sprite
        return


    if bg_current == "bg_dangerroom":
        call exit_gym ([KittyX])

    $ KittyX.change_outfit()

    if "follow" not in KittyX.traits:

        $ KittyX.traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ line = 0

    if KittyX.location == "bg_classroom":
        $ approval_bonus = 10
    elif KittyX.location == "bg_dangerroom":
        $ approval_bonus = 20
    elif KittyX.location == "bg_showerroom":
        $ approval_bonus = 40


    if GirlsNum:
        ch_k "Yeah, I'm headed out too."

    if KittyX.location == "bg_classroom":
        ch_k "I'm headed to class right now, you could[KittyX.like]join me."
    elif KittyX.location == "bg_dangerroom":
        ch_k "I'm hitting the danger room, care to[KittyX.like]join me?"
    elif KittyX.location == "bg_campus":
        ch_k "I'm going to[KittyX.like]hang out on campus, want to chill with me?"
    elif KittyX.location == "bg_kitty":
        ch_k "I'm heading back to my room, want to[KittyX.like]hang out?"
    elif KittyX.location == "bg_player":
        ch_k "I'll[KittyX.like]be heading to your room."
    elif KittyX.location == "bg_showerroom":
        if approval_check(KittyX, 1600):
            ch_k "I'm[KittyX.like]hitting the showers, want to join me?"
        else:
            ch_k "I'm hitting the showers, maybe we could[KittyX.like]touch base later."
            return
    elif KittyX.location == "bg_pool":
        ch_k "I'm[KittyX.like]hitting up the pool. You coming?"
    else:
        ch_k "Wanna[KittyX.like]come with me, [KittyX.player_petname]?"

    menu:
        extend ""
        "Sure, I'll catch up.":
            if "followed" not in KittyX.recent_history:
                $ KittyX.change_stat("love", 55, 1)
                $ KittyX.change_stat("inhibition", 30, 1)
            $ line = "go to"
        "Nah, we can talk later.":

            if "followed" not in KittyX.recent_history:
                $ KittyX.change_stat("obedience", 50, 1)
                $ KittyX.change_stat("obedience", 30, 2)
            ch_k "Ok, cool. Talk to you later then."
        "Could you please stay with me? I'll get lonely.":

            if approval_check(KittyX, 600, "L") or approval_check(KittyX, 1400):
                if "followed" not in KittyX.recent_history:
                    $ KittyX.change_stat("love", 70, 1)
                    $ KittyX.change_stat("obedience", 50, 1)
                $ line = "lonely"
            else:
                if "followed" not in KittyX.recent_history:
                    $ KittyX.change_stat("inhibition", 30, 1)
                $ line = "no"
        "No, stay here.":

            if approval_check(KittyX, 600, "O"):

                if "followed" not in KittyX.recent_history:
                    if KittyX.love >= 50:
                        $ KittyX.change_stat("love", 90, 1)
                    $ KittyX.change_stat("love", 40, -1)
                    $ KittyX.change_stat("obedience", 90, 1)
                $ line = "command"

            elif D20 >= 7 and approval_check(KittyX, 1400):

                if "followed" not in KittyX.recent_history:
                    $ KittyX.change_stat("love", 70, -2)
                    $ KittyX.change_stat("love", 90, -1)
                    $ KittyX.change_stat("obedience", 50, 2)
                    $ KittyX.change_stat("obedience", 90, 1)
                ch_k "Uh, sure, I guess."
                $ line = "yes"

            elif approval_check(KittyX, 200, "O"):

                if "followed" not in KittyX.recent_history:
                    $ KittyX.change_stat("love", 70, -4)
                    $ KittyX.change_stat("love", 90, -2)
                ch_k "[KittyX.Like]in your dreams, [KittyX.player_petname]."
                if "followed" not in KittyX.recent_history:
                    $ KittyX.change_stat("inhibition", 40, 2)
                    $ KittyX.change_stat("inhibition", 60, 1)
                    $ KittyX.change_stat("obedience", 70, -2)
                ch_k "I'm gone."
            else:

                if "followed" not in KittyX.recent_history:
                    $ KittyX.change_stat("inhibition", 30, 1)
                    $ KittyX.change_stat("inhibition", 50, 1)
                    $ KittyX.change_stat("love", 50, -1, 1)
                    $ KittyX.change_stat("obedience", 70, -1)
                $ line = "no"


    $ KittyX.recent_history.append("followed")
    if not line:

        hide Kitty_sprite
        call change_out_of_gym_clothes ([KittyX])
        return

    if line == "no":

        if KittyX.location == "bg_classroom":
            ch_k "Totally can't, [KittyX.player_petname], Gotta study for the test."
        elif KittyX.location == "bg_dangerroom":
            ch_k "Sorry [KittyX.player_petname], but I[KittyX.like]need the practice?"
        else:
            ch_k "I'm[KittyX.like]sorry, [KittyX.player_petname], I've got things to do."
        hide Kitty_sprite
        call change_out_of_gym_clothes ([KittyX])
        return

    elif line == "go to":


        $ approval_bonus = 0
        $ line = 0
        call drain_all_words ("leaving")
        call drain_all_words ("arriving")
        $ KittyX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        hide Kitty_sprite
        call change_out_of_gym_clothes ([KittyX])
        if KittyX.location == "bg_classroom":
            ch_k "Cool, study buddy!"
            jump classroom_entry
        elif KittyX.location == "bg_dangerroom":
            ch_k "I'll be ready and waiting!"
            jump danger_room_entry
        elif KittyX.location == "bg_kitty":
            ch_k "I'll meet you there."
            $ Girl = KittyX
            jump girls_room
        elif KittyX.location == "bg_player":
            ch_k "I'll be waiting."
            jump player_room
        elif KittyX.location == "bg_showerroom":
            ch_k "I guess I'll see you there."
            jump shower_entry
        elif KittyX.location == "bg_campus":
            ch_k "Let's head over there."
            jump campus_entry
        elif KittyX.location == "bg_pool":
            ch_k "Ok, let's go."
            jump pool_entry
        else:
            ch_k "You know, I'll just meet you in my room."
            $ KittyX.location = "bg_kitty"
            $ Girl = KittyX
            jump girls_room



    elif line == "lonely":
        ch_k "I guess[KittyX.like]I couldn't leave you lonely. . ."
    elif line == "command":
        ch_k "Humph, ok."

    $ line = 0
    ch_k "I guess I can stick around."
    $ KittyX.location = bg_current
    call taboo_level(taboo_location = False)
    return





label Kitty_Clothes:
    if KittyX.taboo:
        if "exhibitionist" in KittyX.traits:
            ch_k "Mmmmm. . ."
        elif approval_check(KittyX, 900, taboo_modifier=4) or approval_check(KittyX, 400, "I", taboo_modifier=3):
            ch_k "This is[KittyX.like]pretty. . . exposed. . ."
        else:
            ch_k "This is[KittyX.like]pretty exposed, right?"
            ch_k "Can't we talk about this in our rooms?"
            return
    elif approval_check(KittyX, 900, taboo_modifier=4) or approval_check(KittyX, 600, "L") or approval_check(KittyX, 300, "O"):
        ch_k "[KittyX.Like]what were you thinking here?"
    else:
        ch_k "I'll let you know when I care what you think."
        return

    if Girl != KittyX or line == "giftstore":

        $ renpy.pop_call()
    $ line = 0
    $ Girl = KittyX
    call shift_focus (Girl)

label Kitty_wardrobe_menu:
    $ primary_action = 1
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
            "outfits":
                call Kitty_Clothes_outfits
            "Let's talk about what you wear around.":
                call set_clothes_schedule (KittyX)

            "Could I get a look at it?" if KittyX.location != bg_current:

                call outfitShame (KittyX, 0, 2)
                if _return:
                    show PhoneSex zorder 150
                    ch_k "Cute? . ."
                hide PhoneSex
            "Could I get a look at it?" if renpy.showing('dress_screen'):

                call outfitShame (KittyX, 0, 2)
                if _return:
                    hide dress_screen
            "Would you be more comfortable behind a screen? (locked)" if KittyX.taboo:
                pass
            "Would you be more comfortable behind a screen?" if KittyX.location == bg_current and not KittyX.taboo and not renpy.showing('dress_screen'):

                if approval_check(KittyX, 1500) or (KittyX.seen_breasts and KittyX.seen_pussy):
                    ch_k "Probably won't need it, thanks."
                else:
                    show dress_screen zorder 150
                    ch_k "Yeah, this is a bit more comfortable, thanks."

            "Gift for you (locked)" if Girl.location != bg_current:
                pass
            "Gift for you" if Girl.location == bg_current:
                ch_p "I'd like to give you something."
                call gifts
            "Switch to. . .":

                if renpy.showing('dress_screen'):
                    call outfitShame (KittyX, 0, 2)
                    if _return:
                        hide dress_screen
                    else:
                        $ KittyX.change_outfit()
                $ KittyX.set_temp_outfit()
                $ primary_action = None
                call Switch_chat
                if Girl != KittyX:
                    ch_p "I wanted to talk about your clothes."
                    call expression Girl.tag +"_Clothes"
                $ Girl = KittyX
                call shift_focus (Girl)
            "Never mind, you look good like that.":

                if "wardrobe" not in KittyX.recent_history:

                    if KittyX.had_chat[1] <= 1:
                        $ KittyX.change_stat("love", 70, 15)
                        $ KittyX.change_stat("obedience", 40, 20)
                        ch_k "That's[KittyX.like]really nice of you to say."
                    elif KittyX.had_chat[1] <= 10:
                        $ KittyX.change_stat("love", 70, 5)
                        $ KittyX.change_stat("obedience", 40, 7)
                        ch_k "I like it too."
                    elif KittyX.had_chat[1] <= 50:
                        $ KittyX.change_stat("love", 70, 1)
                        $ KittyX.change_stat("obedience", 40, 1)
                        ch_k "Yeah."
                    else:
                        ch_k "Sure."
                    $ KittyX.recent_history.append("wardrobe")
                if renpy.showing('dress_screen'):
                    call outfitShame (KittyX, 0, 2)
                    if _return:
                        hide dress_screen
                    else:
                        $ KittyX.change_outfit()

                $ KittyX.set_temp_outfit()
                $ KittyX.had_chat[1] += 1
                $ primary_action = None
                return







    menu Kitty_Clothes_outfits:
        "You should remember that one. [[Set Custom]":

            menu:
                "Which slot would you like this saved in?"
                "Custom 1":
                    call outfitShame (KittyX, 3, 1)
                "Custom 2":
                    call outfitShame (KittyX, 5, 1)
                "Custom 3":
                    call outfitShame (KittyX, 6, 1)
                "Gym Clothes":
                    call outfitShame (KittyX, 4, 1)
                "Sleepwear":
                    call outfitShame (KittyX, 7, 1)
                "Swimwear":
                    call outfitShame (KittyX, 10, 1)
                "Never mind":
                    pass
        "I really like that pink shirt and capris outfit you wear.":


            $ KittyX.change_outfit("casual1")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ KittyX.outfit_name = "casual1"
                    $ KittyX.outfit["shame"] = 0
                    ch_k "I used to wear that one[KittyX.like]every day!"
                "Let's try something else though.":
                    ch_k "K."
        "That red shirt and black jeans look really nice on you.":


            $ KittyX.change_outfit("casual2")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ KittyX.outfit_name = "casual2"
                    $ KittyX.outfit["shame"] = 0
                    ch_k "That one[KittyX.like]used to be my favorite too!"
                "Let's try something else though.":
                    ch_k "K."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not KittyX.first_custom_outfit["outfit_active"] and not KittyX.second_custom_outfit["outfit_active"] and not KittyX.third_custom_outfit["outfit_active"]:
            pass

        "Remember that outfit we put together?" if KittyX.first_custom_outfit["outfit_active"] or KittyX.second_custom_outfit["outfit_active"] or KittyX.third_custom_outfit["outfit_active"]:
            $ counter = 0
            while 1:
                menu:
                    "Throw on Custom 1 (locked)" if not KittyX.first_custom_outfit["outfit_active"]:
                        pass
                    "Throw on Custom 1" if KittyX.first_custom_outfit["outfit_active"]:
                        $ KittyX.change_outfit("custom1")
                        $ counter = 3
                    "Throw on Custom 2 (locked)" if not KittyX.second_custom_outfit["outfit_active"]:
                        pass
                    "Throw on Custom 2" if KittyX.second_custom_outfit["outfit_active"]:
                        $ KittyX.change_outfit("custom2")
                        $ counter = 5
                    "Throw on Custom 3 (locked)" if not KittyX.third_custom_outfit["outfit_active"]:
                        pass
                    "Throw on Custom 3" if KittyX.third_custom_outfit["outfit_active"]:
                        $ KittyX.change_outfit("custom3")
                        $ counter = 6

                    "You should wear this one in private. (locked)" if not counter:
                        pass
                    "You should wear this one in private." if counter:
                        if counter == 5:
                            $ KittyX.clothing[9] = 5
                        elif counter == 6:
                            $ KittyX.clothing[9] = 6
                        else:
                            $ KittyX.clothing[9] = 3
                        ch_k "Ok, sure."
                    "On second thought, forget about that one outfit. . .":

                        menu:
                            "Custom 1 [[clear custom 1]" if KittyX.first_custom_outfit["outfit_active"]:
                                ch_k "Ok, no problem."
                                $ KittyX.first_custom_outfit["outfit_active"] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not KittyX.first_custom_outfit["outfit_active"]:
                                pass
                            "Custom 2 [[clear custom 2]" if KittyX.second_custom_outfit["outfit_active"]:
                                ch_k "Ok, no problem."
                                $ KittyX.second_custom_outfit["outfit_active"] = 0
                            "Custom 2 [[clear custom 2] (locked)" if not KittyX.second_custom_outfit["outfit_active"]:
                                pass
                            "Custom 3 [[clear custom 3]" if KittyX.third_custom_outfit["outfit_active"]:
                                ch_k "Ok, no problem."
                                $ KittyX.third_custom_outfit["outfit_active"] = 0
                            "Custom 3 [[clear custom 3] (locked)" if not KittyX.third_custom_outfit["outfit_active"]:
                                pass
                            "Never mind, [[back].":
                                pass

                    "You should wear this one out. [[choose outfit first](locked)" if not counter:
                        pass
                    "You should wear this one out." if counter:
                        call Custom_Out (KittyX, counter)
                    "Ok, back to what we were talking about. . .":
                        $ counter = 0
                        return

        "Gym Clothes?" if not KittyX.taboo or bg_current == "bg_dangerroom":
            $ KittyX.change_outfit("gym_clothes")

        "Sleepwear?" if not KittyX.taboo:
            if approval_check(KittyX, 1200):
                $ KittyX.change_outfit("sleepwear")
            else:
                call Display_dress_screen (KittyX)
                if _return:
                    $ KittyX.change_outfit("sleepwear")

        "Swimwear? (locked)" if (KittyX.taboo and bg_current != "bg_pool") or not KittyX.swimwear["outfit_active"]:
            $ KittyX.change_outfit("swimwear")
        "Swimwear?" if (not KittyX.taboo or bg_current == "bg_pool") and KittyX.swimwear["outfit_active"]:
            $ KittyX.change_outfit("swimwear")

        "Halloween Costume?" if "halloween" in KittyX.history:
            ch_k "Sure."
            $ KittyX.change_outfit("costume")
        "Your birthday suit looks really great. . .":


            $ KittyX.change_face("_sexy", 1)
            $ line = 0
            if not KittyX.outfit["bra"] and not KittyX.outfit["underwear"] and not KittyX.outfit["top"] and not KittyX.outfit["bottom"] and not KittyX.outfit["hose"]:
                ch_k "You're kidding, right?"
            elif KittyX.seen_breasts and KittyX.seen_pussy and approval_check(KittyX, 1200, taboo_modifier=4):
                ch_k "[KittyX.Like]Reow. . ."
                $ line = 1
            elif approval_check(KittyX, 2000, taboo_modifier=4):
                ch_k "You don't[KittyX.like]mess around, huh."
                $ line = 1
            elif KittyX.seen_breasts and KittyX.seen_pussy and approval_check(KittyX, 1200, taboo_modifier=0):
                ch_k "[KittyX.Like]this is a little exposed. . ."
            elif approval_check(KittyX, 2000, taboo_modifier=0):
                ch_k "Maybe if we were alone?"
            elif approval_check(KittyX, 1000, taboo_modifier=0):
                $ KittyX.change_face("_surprised", 2)
                ch_k "[KittyX.Like]get to know a girl first, [KittyX.player_petname]."
                $ KittyX.blushing = "_blush1"
            else:
                $ KittyX.change_face("_angry", 1)
                ch_k "Yeah[KittyX.like]it does."

            if line:
                $ KittyX.change_outfit("nude")
                "She lets all her clothes drop into a pile at her feet."
                call Kitty_First_Topless
                call Kitty_First_Bottomless (1)
                $ KittyX.change_face("_sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in KittyX.traits:
                            ch_k "I'm[KittyX.like]getting a little wet just thinking about it."
                            $ KittyX.outfit_name = "nude"
                            $ KittyX.change_stat("lust", 50, 10)
                            $ KittyX.change_stat("lust", 70, 5)
                            $ KittyX.outfit["shame"] = 50
                        elif approval_check(KittyX, 800, "I") or approval_check(KittyX, 2800, taboo_modifier=0):
                            ch_k "I guess we could. . ."
                            $ KittyX.outfit_name = "nude"
                            $ KittyX.outfit["shame"] = 50
                        else:
                            $ KittyX.change_face("_sexy", 1)
                            $ KittyX.eyes = "_surprised"
                            ch_k "No way! That'd be[KittyX.like]totally embarrassing!"
                    "Let's try something else though.":

                        if "exhibitionist" in KittyX.traits:
                            ch_k "Aw, do I have to?"
                        elif approval_check(KittyX, 800, "I") or approval_check(KittyX, 2800, taboo_modifier=0):
                            $ KittyX.change_face("_bemused", 1)
                            ch_k "It's a good thing you didn't[KittyX.like]ask me to wear this outside."
                            ch_k "A good thing. . ."
                        else:
                            $ KittyX.change_face("_confused", 1)
                            ch_k "I[KittyX.like]don't mind this around the room, but definitely not outside."
            $ line = 0
        "Never mind":

            return

    return




    menu Kitty_Clothes_Over:

        "Why don't you go with no [KittyX.outfit['top']]?" if KittyX.outfit["top"]:
            $ KittyX.change_face("_bemused", 1)
            if approval_check(KittyX, 800, taboo_modifier=3) and (KittyX.outfit["bra"] or KittyX.seen_breasts):
                ch_k "Why not?"
            elif approval_check(KittyX, 600, taboo_modifier=0):
                call Kitty_NoBra
                if not _return:
                    if not approval_check(KittyX, 1200):
                        call Display_dress_screen (KittyX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_dress_screen (KittyX)
                if not _return:
                    ch_k "Lol, not around you."
                    if not KittyX.outfit["bra"]:
                        ch_k "I don't have anything under this. . ."
                    return
            $ line = KittyX.outfit["top"]
            $ KittyX.outfit["top"] = ""
            "She lets her [line] drop to her feet."
            if not KittyX.outfit["bra"] and not renpy.showing('dress_screen'):
                call Kitty_First_Topless

        "Try on that pink shirt you have." if KittyX.outfit["top"] != "_pink_top":
            $ KittyX.change_face("_bemused")
            if KittyX.outfit["bra"] or KittyX.seen_breasts:
                ch_k "K."
            elif approval_check(KittyX, 800, taboo_modifier=0):
                ch_k "Yeah, ok."
            else:
                call Display_dress_screen (KittyX)
                if not _return:
                    $ KittyX.change_face("_bemused", 1)
                    ch_k "This top is a little skimpy for what I have on under it."
                    return
            $ KittyX.outfit["top"] = "_pink_top"

        "How about that red t-shirt you have?" if KittyX.outfit["top"] != "_red_shirt":
            $ KittyX.outfit["top"] = "_red_shirt"
            ch_k "This one?"

        "Try on that red jacket." if KittyX.outfit["top"] != "_jacket" and "halloween" in KittyX.history:
            $ KittyX.change_face("_bemused")
            if KittyX.outfit["bra"] or KittyX.seen_breasts:
                ch_k "K."
            elif approval_check(KittyX, 900, taboo_modifier=0):
                ch_k "Yeah, ok."
            else:
                call Display_dress_screen (KittyX)
                if not _return:
                    $ KittyX.change_face("_bemused", 1)
                    ch_k "This top is a little skimpy for what I have on under it."
                    return
            $ KittyX.outfit["top"] = "_jacket"

        "Maybe just throw on a towel?" if KittyX.outfit["top"] != "_towel":
            $ KittyX.change_face("_bemused", 1)
            if KittyX.outfit["bra"] or KittyX.seen_breasts:
                ch_k "Weirdo."
            elif approval_check(KittyX, 1000, taboo_modifier=0):
                $ KittyX.change_face("_perplexed", 1)
                ch_k "I guess? . ."
            else:
                call Display_dress_screen (KittyX)
                if not _return:
                    ch_k "I don't think so with what I have on under it."
                    return
            $ KittyX.outfit["top"] = "_towel"
        "Never mind":

            pass
    return




    label Kitty_NoBra:
        menu:
            ch_k "I don't exactly have anything on under this. . ."
            "Then you could slip something on under it. . .":
                if KittyX.seen_breasts and approval_check(KittyX, 1000, taboo_modifier=3):
                    $ KittyX.blushing = "_blush2"
                    ch_k "-not that that's a problem. . ."
                    $ KittyX.blushing = "_blush1"
                elif approval_check(KittyX, 1200, taboo_modifier=4):
                    $ KittyX.blushing = "_blush2"
                    ch_k "-not that that's a problem. . ."
                    $ KittyX.blushing = "_blush1"
                elif approval_check(KittyX, 900, taboo_modifier=2) and "_lace_bra" in KittyX.inventory:
                    ch_k "I could find {i}something{/i} to wear."
                    $ KittyX.outfit["bra"]  = "_lace_bra"
                    "She pulls out her lace bra and passes it through her [KittyX.outfit['top']]."
                elif approval_check(KittyX, 800, taboo_modifier=2):
                    ch_k "Yeah, I guess."
                    $ KittyX.outfit["bra"] = "_bra"
                    "She pulls out her bra and passes it through her [KittyX.outfit['top']]."
                elif approval_check(KittyX, 700, taboo_modifier=2):
                    ch_k "Yeah, I guess."
                    $ KittyX.outfit["bra"] = "_cami"
                    "She pulls out her camisole and passes it through her [KittyX.outfit['top']]."
                elif approval_check(KittyX, 600, taboo_modifier=2):
                    ch_k "Yeah, I guess."
                    $ KittyX.outfit["bra"] = "_sports_bra"
                    "She pulls out her sports bra and passes it through her [KittyX.outfit['top']]."
                else:
                    ch_k "Yeah, I don't think so."
                    return False
            "You could always just wear nothing at all. . .":

                if approval_check(KittyX, 1100, "LI", taboo_modifier=2) and KittyX.love > KittyX.inhibition:
                    ch_k "I guess for you. . ."
                elif approval_check(KittyX, 700, "OI", taboo_modifier=2) and KittyX.obedience > KittyX.inhibition:
                    ch_k "Sure. . ."
                elif approval_check(KittyX, 600, "I", taboo_modifier=2):
                    ch_k "Yeah. . ."
                elif approval_check(KittyX, 1300, taboo_modifier=2):
                    ch_k "Okay, fine."
                else:
                    $ KittyX.change_face("_surprised")
                    $ KittyX.brows = "_angry"
                    if KittyX.taboo > 20:
                        ch_k "Not in public, [KittyX.player_petname]!"
                    else:
                        ch_k "I don't like you {i}that{/i} much, [KittyX.player_petname]!"
                    return False
            "Never mind.":


                ch_k "Ok. . ."
                return False
        return True




    menu Kitty_Clothes_Legs:

        "Maybe go without the [KittyX.outfit['legs']]." if KittyX.outfit["bottom"]:
            $ KittyX.change_face("_sexy", 1)
            if KittyX.seen_underwear and KittyX.outfit["underwear"] and approval_check(KittyX, 500, taboo_modifier=5):
                ch_k "K."
            elif KittyX.seen_pussy and approval_check(KittyX, 900, taboo_modifier=4):
                ch_k "Yeah, ok."
            elif approval_check(KittyX, 1300, taboo_modifier=2) and KittyX.outfit["underwear"]:
                ch_k "For you, I guess. . ."
            elif approval_check(KittyX, 700) and not KittyX.outfit["underwear"]:
                call Kitty_NoPantiesOn
                if not _return and not KittyX.outfit["underwear"]:
                    if not approval_check(KittyX, 1500):
                        call Display_dress_screen (KittyX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_dress_screen (KittyX)
                if not _return:
                    ch_k "Lol, not around you."
                    if not KittyX.outfit["underwear"]:
                        ch_k "I'm not {i}wearing any panties{/i}. . ."
                    return
            $ line = KittyX.outfit["bottom"]
            $ KittyX.outfit["bottom"] = ""
            "She lets her [line] drop through her to the ground."
            $ line = 0
            if renpy.showing('dress_screen'):
                pass
            elif KittyX.outfit["underwear"]:
                $ KittyX.seen_underwear = 1
            else:
                call Kitty_First_Bottomless

        "You look great in those capris." if KittyX.outfit["bottom"] != "_capris":
            ch_k "Yeah, ok."
            $ KittyX.outfit["bottom"] = "_capris"

        "You look great in those black jeans." if KittyX.outfit["bottom"] != "_black_jeans":
            ch_k "K, no problem."
            $ KittyX.outfit["bottom"] = "_black_jeans"

        "You look great in yoga pants." if KittyX.outfit["bottom"] != "_yoga_pants":
            ch_k "Yeah, ok."
            $ KittyX.outfit["bottom"] = "_yoga_pants"

        "What about wearing your yellow shorts?" if KittyX.outfit["bottom"] != "_shorts":
            ch_k "K, no problem."
            $ KittyX.outfit["bottom"] = "_shorts"

        "How about the blue skirt?" if KittyX.outfit["bottom"] != "_blue_skirt" and "_blue_skirt" in KittyX.inventory:
            if KittyX.outfit["underwear"] or approval_check(KittyX,500,"I",taboo_modifier=2):
                ch_k "Yeah, ok."
                $ KittyX.outfit["bottom"] = "_blue_skirt"
            else:
                ch_k "That's a little revealing. . ."

        "Try on that pink dress you have." if KittyX.outfit["bottom"] != "_dress" and "halloween" in KittyX.history:
            menu:
                ch_k "The whole thing, or just the skirt?"
                "The whole dress.":
                    $ KittyX.outfit["bra"] = "_dress"
                "Just the skirt.":
                    pass
            $ KittyX.outfit["bottom"] = "_dress"
        "Never mind":

            pass
    return




    label Kitty_NoPantiesOn:
        menu:
            ch_k "These are[KittyX.like]all I have on."
            "Then you could slip on a pair of panties. . .":
                if KittyX.seen_pussy and approval_check(KittyX, 1100, taboo_modifier=4):
                    $ KittyX.blushing = "_blush2"
                    ch_k "I didn't say that bothered me. . ."
                    $ KittyX.blushing = "_blush1"
                elif approval_check(KittyX, 1500, taboo_modifier=4):
                    $ KittyX.blushing = "_blush2"
                    ch_k "I didn't say that bothered me. . ."
                    $ KittyX.blushing = "_blush1"
                elif approval_check(KittyX, 800, taboo_modifier=4) and "_lace_panties" in KittyX.inventory:
                    ch_k "I like how you think."
                    $ KittyX.outfit["underwear"]  = "_lace_panties"
                    "She pulls out her lace panties and pulls them up through her [KittyX.outfit['legs']]."
                elif approval_check(KittyX, 700, taboo_modifier=4):
                    ch_k "Yeah, I guess."
                    $ KittyX.outfit["underwear"] = "_green_panties"
                    "She pulls out her green panties and pulls them up through her [KittyX.outfit['legs']]."
                else:
                    ch_k "Yeah, I don't think so."
                    return False
            "You could always just wear nothing at all. . .":

                if approval_check(KittyX, 1100, "LI", taboo_modifier=3) and KittyX.love > KittyX.inhibition:
                    ch_k "Well, not that I mind you seeing it. . ."
                elif approval_check(KittyX, 700, "OI", taboo_modifier=3) and KittyX.obedience > KittyX.inhibition:
                    ch_k "I guess. . ."
                elif approval_check(KittyX, 600, "I", taboo_modifier=3):
                    ch_k "Hrmm. . ."
                elif approval_check(KittyX, 1300, taboo_modifier=3):
                    ch_k "Okay, okay."
                else:
                    $ KittyX.change_face("_surprised")
                    $ KittyX.brows = "_angry"
                    if KittyX.taboo > 20:
                        ch_k "Not in public, [KittyX.player_petname]!"
                    else:
                        ch_k "I don't like you {i}that{/i} much, [KittyX.player_petname]!"
                    return False
            "Never mind.":

                ch_k "Ok. . ."
                return False
        return True




    menu Kitty_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [KittyX.outfit['bra']]?" if KittyX.outfit["bra"]:
                    $ KittyX.change_face("_bemused", 1)
                    if KittyX.seen_breasts and approval_check(KittyX, 900, taboo_modifier=2.7):
                        ch_k "Sure."
                    elif approval_check(KittyX, 1100, taboo_modifier=2):
                        if KittyX.taboo:
                            ch_k "I'm kind of nervous. . ."
                        else:
                            ch_k "If it's just you. . ."
                    elif KittyX.outfit["top"] == "_pink_top" and approval_check(KittyX, 600, taboo_modifier=2):
                        ch_k "This look is a bit revealing. . ."
                    elif KittyX.outfit["top"] == "_red_shirt" and approval_check(KittyX, 500, taboo_modifier=2):
                        ch_k "I guess I could. . ."
                    elif not KittyX.outfit["top"]:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "Not without a little coverage, for modesty."
                            return
                    else:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "I don't think so, [KittyX.player_petname]."
                            return
                    $ line = KittyX.outfit["bra"]
                    $ KittyX.outfit["bra"] = ""
                    if KittyX.outfit["top"]:
                        "She reaches into her [KittyX.outfit['top']] grabs her [line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [line] fall to the ground."
                        if not renpy.showing('dress_screen'):
                            call Kitty_First_Topless

                "Try on that yellow camisole." if KittyX.outfit["bra"] != "_cami":
                    ch_k "Ok."
                    $ KittyX.outfit["bra"] = "_cami"

                "I like that strapless bra." if KittyX.outfit["bra"] != "_bra":
                    if KittyX.seen_breasts or approval_check(KittyX, 1200, taboo_modifier=2):
                        ch_k "K."
                        $ KittyX.outfit["bra"] = "_bra"
                    else:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "I'm not really comfortable with that. . ."
                        else:
                            $ KittyX.outfit["bra"] = "_bra"

                "I like that lace bra." if "_lace_bra" in KittyX.inventory and KittyX.outfit["bra"] != "_lace_bra":
                    if KittyX.seen_breasts or approval_check(KittyX, 1300, taboo_modifier=2):
                        ch_k "K."
                        $ KittyX.outfit["bra"] = "_lace_bra"
                    else:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "It's pretty skimpy. . ."
                        else:
                            $ KittyX.outfit["bra"] = "_lace_bra"

                "I like that sports bra." if KittyX.outfit["bra"] != "_sports_bra":
                    if KittyX.seen_breasts or approval_check(KittyX, 1000, taboo_modifier=2):
                        ch_k "K."
                        $ KittyX.outfit["bra"] = "_sports_bra"
                    else:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "I'm not sure about that. . ."
                        else:
                            $ KittyX.outfit["bra"] = "_sports_bra"

                "I like that bikini top." if KittyX.outfit["bra"] != "_bikini_top" and "_bikini_top" in KittyX.inventory:
                    if bg_current == "bg_pool":
                        ch_k "K."
                        $ KittyX.outfit["bra"] = "_bikini_top"
                    else:
                        if KittyX.seen_breasts or approval_check(KittyX, 1000, taboo_modifier=2):
                            ch_k "K."
                            $ KittyX.outfit["bra"] = "_bikini_top"
                        else:
                            call Display_dress_screen (KittyX)
                            if not _return:
                                ch_k "Geez, not here!"
                            else:
                                $ KittyX.outfit["bra"] = "_bikini_top"

                "Try on that pink dress you have." if KittyX.outfit["bra"] != "_dress" and "halloween" in KittyX.history:
                    if KittyX.seen_breasts or approval_check(KittyX, 1000, taboo_modifier=2):
                        ch_k "K."
                    else:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "I'm not sure about that. . ."
                            jump Kitty_Clothes_Under
                    menu:
                        ch_k "The whole thing, or just the top?"
                        "The whole dress.":
                            $ KittyX.outfit["bottom"] = "_dress"
                        "Just the top.":
                            pass
                    $ KittyX.outfit["bra"] = "_dress"
                "Never mind":

                    pass
            jump Kitty_Clothes_Under
        "Hose and stockings options":

            menu:
                "You could lose the hose." if KittyX.outfit["hose"]:
                    $ KittyX.outfit["hose"] = ""
                "The thigh-high hose would look good with that." if KittyX.outfit["hose"] != "_stockings":
                    $ KittyX.outfit["hose"] = "_stockings"
                "The knee-high hose would look good with that." if KittyX.outfit["hose"] != "_knee_stockings" and "_knee_stockings" in KittyX.inventory:
                    $ KittyX.outfit["hose"] = "_knee_stockings"
                "The pantyhose would look good with that." if KittyX.outfit["hose"] != "_pantyhose" and "_pantyhose" in KittyX.inventory:
                    $ KittyX.outfit["hose"] = "_pantyhose"
                "The stockings would look good with that." if KittyX.outfit["hose"] != "_stockings_and_garterbelt" and "_stockings_and_garterbelt" in KittyX.inventory:
                    $ KittyX.outfit["hose"] = "_stockings_and_garterbelt"
                "Maybe just the garterbelt?" if KittyX.outfit["hose"] != "_garterbelt" and "_stockings_and_garterbelt" in KittyX.inventory:
                    $ KittyX.outfit["hose"] = "_garterbelt"
                "Your ripped pantyhose would look good with that." if KittyX.outfit["hose"] != "_ripped_pantyhose" and "_ripped_pantyhose" in KittyX.inventory:
                    $ KittyX.outfit["hose"] = "_ripped_pantyhose"
                "Never mind":
                    pass
            jump Kitty_Clothes_Under
        "Panties":


            menu:
                "You could lose those panties. . ." if KittyX.outfit["underwear"]:
                    $ KittyX.change_face("_bemused", 1)
                    if approval_check(KittyX, 900) and (KittyX.outfit["bottom"] or (KittyX.seen_pussy and not KittyX.taboo)):

                        if approval_check(KittyX, 850, "L"):
                            ch_k "Well, if you ask me nicely. . ."
                        elif approval_check(KittyX, 500, "O"):
                            ch_k "For you, ok."
                        elif approval_check(KittyX, 350, "I"):
                            ch_k "[[snort]."
                        else:
                            ch_k "Yeah, I guess."
                    else:
                        if approval_check(KittyX, 1100, "LI", taboo_modifier=3) and KittyX.love > KittyX.inhibition:
                            ch_k "Well, not that I mind you seeing it. . ."
                        elif approval_check(KittyX, 700, "OI", taboo_modifier=3) and KittyX.obedience > KittyX.inhibition:
                            ch_k "I guess. . ."
                        elif approval_check(KittyX, 600, "I", taboo_modifier=3):
                            ch_k "Hrmm. . ."
                        elif approval_check(KittyX, 1300, taboo_modifier=3):
                            ch_k "Okay, okay."
                        else:
                            call Display_dress_screen (KittyX)
                            if not _return:
                                $ KittyX.change_face("_surprised")
                                $ KittyX.brows = "_angry"
                                if KittyX.taboo > 20:
                                    ch_k "Not in public, [KittyX.player_petname]!"
                                else:
                                    ch_k "I don't like you that much, [KittyX.player_petname]!"
                                return

                    $ line = KittyX.outfit["underwear"]
                    $ KittyX.outfit["underwear"] = ""
                    if KittyX.outfit["bottom"]:
                        "She reaches into her pocket, grabs hold of something, and then pulls her [line] out, droping them to the ground."
                    else:
                        "She lets her [line] drop to the ground."
                        if not renpy.showing('dress_screen'):
                            call Kitty_First_Bottomless
                            $ KittyX.change_stat("inhibition", 50, 2)

                "Why don't you wear the green panties instead?" if KittyX.outfit["underwear"] and KittyX.outfit["underwear"] != "_green_panties":
                    if approval_check(KittyX, 1100, taboo_modifier=3):
                        ch_k "K."
                        $ KittyX.outfit["underwear"] = "_green_panties"
                    else:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "I don't think that's any of your beeswax."
                        else:
                            $ KittyX.outfit["underwear"] = "_green_panties"

                "Why don't you wear the lace panties instead?" if "_lace_panties" in KittyX.inventory and KittyX.outfit["underwear"] and KittyX.outfit["underwear"] != "_lace_panties":
                    if approval_check(KittyX, 1300, taboo_modifier=3):
                        ch_k "I guess."
                        $ KittyX.outfit["underwear"] = "_lace_panties"
                    else:
                        call Display_dress_screen (KittyX)
                        if not _return:
                            ch_k "That's[KittyX.like]none of your business."
                        else:
                            $ KittyX.outfit["underwear"] = "_lace_panties"

                "I like those bikini bottoms." if KittyX.outfit["underwear"] != "_bikini_bottoms" and "_bikini_bottoms" in KittyX.inventory:
                    if bg_current == "bg_pool":
                        ch_k "K."
                        $ KittyX.outfit["underwear"] = "_bikini_bottoms"
                    else:
                        if approval_check(KittyX, 1000, taboo_modifier=2):
                            ch_k "K."
                            $ KittyX.outfit["underwear"] = "_bikini_bottoms"
                        else:
                            call Display_dress_screen (KittyX)
                            if not _return:
                                ch_k "Geez, not here!"
                            else:
                                $ KittyX.outfit["underwear"] = "_bikini_bottoms"

                "You know, you could wear some panties with that. . ." if not KittyX.outfit["underwear"]:
                    $ KittyX.change_face("_bemused", 1)
                    if KittyX.outfit["bottom"] and (KittyX.love+KittyX.obedience) <= (2*KittyX.inhibition):
                        $ KittyX.mouth = "_smile"
                        ch_k "I think I'd. . . rather not."
                        menu:
                            "Fine by me":
                                return
                            "I insist, put some on.":
                                if (KittyX.love+KittyX.obedience) <= (1.5*KittyX.inhibition):
                                    $ KittyX.change_face("_angry", eyes="_side")
                                    ch_k "Well that's too bad."
                                    return
                                else:
                                    $ KittyX.change_face("_sadside")
                                    ch_k "Ok, FINE."
                    menu:
                        ch_k "I guess. . ."
                        "How about the green ones?":
                            ch_k "Sure, ok."
                            $ KittyX.outfit["underwear"] = "_green_panties"
                        "How about the lace ones?" if "_lace_panties" in KittyX.inventory:
                            ch_k "Alright."
                            $ KittyX.outfit["underwear"]  = "_lace_panties"
                "Never mind":
                    pass
            jump Kitty_Clothes_Under
        "Never mind":
            pass
    return




    menu Kitty_Clothes_Misc:

        "Ponytail style" if KittyX.outfit["hair"] != "_evo":
            ch_p "You look good with your hair up."
            if approval_check(KittyX, 600):
                ch_k "Like this?"
                $ KittyX.outfit["hair"] = "_evo"
            else:
                ch_k "Yeah, I know that."

        "Loose Hair Style" if KittyX.outfit["hair"] != "_long":
            ch_p "Maybe let your hair down."
            if approval_check(KittyX, 600):
                ch_k "You think?"
                $ KittyX.outfit["hair"] = "_long"
            else:
                ch_k "I[KittyX.like]kinda prefer to keep it up."

        "Wet hair style." if KittyX.outfit["hair"] != "_wet":
            ch_p "You should go for that wet look with your hair."
            if approval_check(KittyX, 800):
                ch_k "You think so?"
                "She rummages in her bag and grabs some gel, running it through her hair."
                ch_k "Like this?"
                $ KittyX.outfit["hair"] = "_wet"
            else:
                ch_k "It's too high maintenance."

        "Grow pubes" if not KittyX.pubes:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in KittyX.to_do:
                ch_k "[[snort] You've got to give it some time!"
            else:
                $ KittyX.change_face("_bemused", 1)
                $ approval = approval_check(KittyX, 1150, taboo_modifier=0)
                if approval_check(KittyX, 850, "L", taboo_modifier=0) or (approval and KittyX.love > 2*KittyX.obedience):
                    ch_k "I guess I could. . ."
                elif approval_check(KittyX, 500, "I", taboo_modifier=0) or (approval and KittyX.inhibition > KittyX.obedience):
                    ch_k "You want a furry kitty to pet?"
                elif approval_check(KittyX, 400, "O", taboo_modifier=0) or approval:
                    ch_k "If you want me to. . ."
                else:
                    $ KittyX.change_face("_surprised")
                    $ KittyX.brows = "_angry"
                    ch_k "Not that it's any of your business, [KittyX.player_petname]."
                    return
                $ KittyX.to_do.append("pubes")
                $ KittyX.pubes_counter = 6

        "Shave pubes" if KittyX.pubes:
            ch_p "I like it waxed clean down there."
            $ KittyX.change_face("_bemused", 1)
            if "shave" in KittyX.to_do:
                ch_k "I know, I know. I'll take care of it later."
            else:
                $ approval = approval_check(KittyX, 1150, taboo_modifier=0)

                if approval_check(KittyX, 850, "L", taboo_modifier=0) or (approval and KittyX.love > 2*KittyX.obedience):
                    ch_k "I guess I could tidy up a bit. . ."
                elif approval_check(KittyX, 500, "I", taboo_modifier=0) or (approval and KittyX.inhibition > KittyX.obedience):
                    ch_k "I'll keep it smooth."
                elif approval_check(KittyX, 400, "O", taboo_modifier=0) or approval:
                    ch_k "I'll get it done."
                else:
                    $ KittyX.change_face("_surprised")
                    $ KittyX.brows = "_angry"
                    ch_k "Not that it's any of your business, [KittyX.player_petname]."
                    return
                $ KittyX.to_do.append("shave")

        "Piercings. [[See what she looks like without them first] (locked)" if not KittyX.seen_pussy and not KittyX.seen_breasts:
            pass

        "Add ring piercings" if KittyX.outfit["piercings"] != "_ring" and (KittyX.seen_pussy or KittyX.seen_breasts):
            ch_p "You know, you'd look really nice with some ring body piercings."
            if "_ring" in KittyX.to_do:
                ch_k "I know, I know. I'll take care of it later."
            else:
                $ KittyX.change_face("_bemused", 1)
                $ approval = approval_check(KittyX, 1350, taboo_modifier=0)
                if approval_check(KittyX, 900, "L", taboo_modifier=0) or (approval and KittyX.love > 2* KittyX.obedience):
                    ch_k "If you think they'd look good on me. . ."
                elif approval_check(KittyX, 600, "I", taboo_modifier=0) or (approval and KittyX.inhibition > KittyX.obedience):
                    ch_k "I think they'd look great too!"
                elif approval_check(KittyX, 500, "O", taboo_modifier=0) or approval:
                    ch_k "K, I'll take care of it."
                else:
                    $ KittyX.change_face("_surprised")
                    $ KittyX.brows = "_angry"
                    ch_k "Not that it's any of your business, [KittyX.player_petname]."
                    return
                $ KittyX.to_do.append("_ring")

        "Add barbell piercings" if KittyX.outfit["piercings"] != "_barbell" and (KittyX.seen_pussy or KittyX.seen_breasts):
            ch_p "You know, you'd look really nice with some barbell body piercings."
            if "_barbell" in KittyX.to_do:
                ch_k "I know, I know. I'll take care of it later."
            else:
                $ KittyX.change_face("_bemused", 1)
                $ approval = approval_check(KittyX, 1350, taboo_modifier=0)
                if approval_check(KittyX, 900, "L", taboo_modifier=0) or (approval and KittyX.love > 2*KittyX.obedience):
                    ch_k "If you think they'd look good on me. . ."
                elif approval_check(KittyX, 600, "I", taboo_modifier=0) or (approval and KittyX.inhibition > KittyX.obedience):
                    ch_k "I think they'd look great too!"
                elif approval_check(KittyX, 500, "O", taboo_modifier=0) or approval:
                    ch_k "K, I'll take care of it."
                else:
                    $ KittyX.change_face("_surprised")
                    $ KittyX.brows = "_angry"
                    ch_k "Not that it's any of your business, [KittyX.player_petname]."
                    return
                $ KittyX.to_do.append("_barbell")
                $ KittyX.outfit["piercings"] = "_barbell"

        "Remove Piercings" if KittyX.outfit["piercings"]:
            ch_p "You know, you'd look better without those piercings."
            $ KittyX.change_face("_bemused", 1)
            $ approval = approval_check(KittyX, 1350, taboo_modifier=0)
            if approval_check(KittyX, 950, "L", taboo_modifier=0) or (approval and KittyX.love > KittyX.obedience):
                ch_k "I guess if they're getting in the way . ."
            elif approval_check(KittyX, 700, "I", taboo_modifier=0) or (approval and KittyX.inhibition > KittyX.obedience):
                ch_k "They were getting a little annoying."
            elif approval_check(KittyX, 600, "O", taboo_modifier=0) or approval:
                ch_k "I'll take them out then."
            else:
                $ KittyX.change_face("_surprised")
                $ KittyX.brows = "_angry"
                ch_k "Well {i}I{/i} kinda like'em."
                return
            $ KittyX.outfit["piercings"] = ""

        "Add gold_necklace" if KittyX.outfit["neck"] != "_gold_necklace":
            ch_p "Why don't you try on that gold necklace?"
            ch_k "Ok. . ."
            $ KittyX.outfit["neck"] = "_gold_necklace"
        "Add star_necklace" if KittyX.outfit["neck"] != "_star_necklace":
            ch_p "Why don't you try on that star necklace?"
            ch_k "Ok. . ."
            $ KittyX.outfit["neck"] = "_star_necklace"
        "Add flower_necklace" if KittyX.outfit["neck"] != "flower necklac" and "halloween" in KittyX.history:
            ch_p "Why don't you try on that flower necklace?"
            ch_k "Ok. . ."
            $ KittyX.outfit["neck"] = "_flower_necklace"

        "Maybe go without a necklace." if KittyX.outfit["neck"]:
            ch_k "Ok. . ."
            $ KittyX.outfit["neck"] = ""
        "Never mind":


            pass
    return


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
