label Kitty_Relationship:
    while True:
        menu:
            ch_k "What did you want to talk about?"
            "Do you want to be my girlfriend?" if KittyX not in Player.Harem and "ex" not in KittyX.traits:
                $ KittyX.daily_history.append("relationship")
                if "asked boyfriend" in KittyX.daily_history and "angry" in KittyX.daily_history:
                    $ KittyX.change_face("angry", 1)
                    ch_k "For real, buzz off."
                    return
                elif "asked boyfriend" in KittyX.daily_history:
                    $ KittyX.change_face("angry", 1)
                    ch_k "Still \"nope.\""
                    return
                elif KittyX.broken_up[0]:
                    $ KittyX.change_face("angry", 1)
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
                    $ KittyX.change_face("bemused", 1)
                    ch_k "I {i}did{/i} ask you about that. . ."
                else:
                    $ KittyX.change_face("surprised", 2)
                    ch_k "I don't know, [KittyX.player_petname]. . ."
                    $ KittyX.change_face("smile", 1)

                call Kitty_OtherWoman

                if KittyX.love >= 800:
                    $ KittyX.change_face("surprised", 1)
                    $ KittyX.mouth = "smile"
                    call change_Girl_stat(KittyX, "love", 40)
                    ch_k "YES!"
                    if "boyfriend" not in KittyX.player_petnames:
                        $ KittyX.player_petnames.append("boyfriend")
                    if "KittyYes" in Player.traits:
                        $ Player.traits.remove("KittyYes")
                    $ Player.Harem.append(KittyX)
                    call Harem_Initiation
                    "[KittyX.name] leaps in and kisses you deeply."
                    $ KittyX.change_face("kiss", 1)
                    $ KittyX.permanent_History["kiss"] += 1
                elif KittyX.obedience >= 500:
                    $ KittyX.change_face("perplexed")
                    ch_k "Maybe not so much \"dating\". . ."
                elif KittyX.inhibition >= 500:
                    $ KittyX.change_face("smile")
                    ch_k "That's not[KittyX.like]where I'm at right now?"
                else:
                    $ KittyX.change_face("perplexed", 1)
                    ch_k "I don't really feel that way about you right now, [KittyX.player_petname]."

            "Do you want to get back together?" if "ex" in KittyX.traits:
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

                if Player.Harem and "KittyYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_k "I don't think they'd be ok with that, [KittyX.player_petname]."
                    else:
                        ch_k "I don't think [Player.Harem[0].name] would be ok with that, [KittyX.player_petname]."
                    return

                $ counter = 0
                call Kitty_OtherWoman

                if KittyX.love >= 800:
                    $ KittyX.change_face("surprised", 1)
                    $ KittyX.mouth = "smile"
                    call change_Girl_stat(KittyX, "love", 5)
                    ch_k "Well, I guess, sure!"
                    if "boyfriend" not in KittyX.player_petnames:
                        $ KittyX.player_petnames.append("boyfriend")
                    $ KittyX.traits.remove("ex")
                    if "KittyYes" in Player.traits:
                        $ Player.traits.remove("KittyYes")
                    $ Player.Harem.append(KittyX)
                    call Harem_Initiation
                    "[KittyX.name] leaps in and kisses you deeply."
                    $ KittyX.change_face("kiss", 1)
                    $ KittyX.permanent_History["kiss"] += 1
                elif KittyX.love >= 600 and approval_check(KittyX, 1500):
                    $ KittyX.change_face("smile", 1)
                    call change_Girl_stat(KittyX, "love", 5)
                    ch_k "Um, ok, I guess."
                    if "boyfriend" not in KittyX.player_petnames:
                        $ KittyX.player_petnames.append("boyfriend")
                    $ KittyX.traits.remove("ex")
                    if "KittyYes" in Player.traits:
                        $ Player.traits.remove("KittyYes")
                    $ Player.Harem.append(KittyX)
                    call Harem_Initiation
                    $ KittyX.change_face("kiss", 1)
                    "[KittyX.name] gives you a quick kiss."
                    $ KittyX.change_face("smile", 1)
                    $ KittyX.permanent_History["kiss"] += 1
                elif KittyX.obedience >= 500:
                    $ KittyX.change_face("sad")
                    ch_k "I think we're better like this."
                elif KittyX.inhibition >= 500:
                    $ KittyX.change_face("perplexed")
                    ch_k "I kind of like what we have right now."
                else:
                    $ KittyX.change_face("perplexed", 1)
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
            "Never mind":
                return
    return

label Kitty_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((KittyX.likes[Player.Harem[0].tag] - 500)/2)

    $ KittyX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_k "But you're with [Player.Harem[0].name] right now, and and all sorts of other girls!"
    else:
        ch_k "But you're with [Player.Harem[0].name]!"
    menu:
        extend ""
        "She said I can be with you too." if "KittyYes" in Player.traits:
            if approval_check(KittyX, 1800, Bonus = counter):
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


        "I could ask if she'd be ok with me dating you both." if "KittyYes" not in Player.traits:
            if approval_check(KittyX, 1800, Bonus = counter):
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

            if not approval_check(KittyX, 1800, Bonus = -counter):
                $ KittyX.change_face("angry", 1)
                if not approval_check(KittyX, 1800):
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
                $ KittyX.traits.append("downlow")
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
            ch_k "I guess I do[KittyX.like]say that a lot, huh?"
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

                $ KittyX.change_face("sly", 1)
                if "monogamous" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "obedience", -2)
                ch_k "I[KittyX.like]appreciate the interest, but you aren't around enough. . ."
                return
            elif approval_check(KittyX, 1100, "LO", taboo_modifier=0) and KittyX.love >= KittyX.obedience:

                $ KittyX.change_face("sly", 1)
                if "monogamous" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "love", 1)
                ch_k "Aw, is someone jellie?"
                ch_k "I guess I could take care of myself. . ."
            elif approval_check(KittyX, 600, "O", taboo_modifier=0):

                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "If you want. . ."
            else:

                $ KittyX.change_face("sly", 1, brows = "confused")
                ch_k "I'll hook up with who I want!"
                return
            if "monogamous" not in KittyX.daily_history:
                call change_Girl_stat(KittyX, "obedience", 3)
            $ KittyX.add_word(1, 0, "monogamous")
            $ KittyX.traits.append("monogamous")
        "Don't hook up with other girls." if "monogamous" not in KittyX.traits:
            if approval_check(KittyX, 800, "O", taboo_modifier=0):

                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "Ok."
            elif KittyX.thirst >= 60 and not approval_check(KittyX, 1700, "LO", taboo_modifier=0):

                $ KittyX.change_face("sly", 1)
                if "monogamous" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "obedience", -2)
                ch_k "I[KittyX.like]appreciate the interest, but you aren't around enough. . ."
                return
            elif approval_check(KittyX, 500, "O", taboo_modifier=0):

                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "If you want. . ."
            elif approval_check(KittyX, 1200, "LO", taboo_modifier=0):

                $ KittyX.change_face("sly", 1)
                ch_k "Rude much?"
                ch_k "Fine, I'll do it for you. . ."
            else:

                $ KittyX.change_face("sly", 1, brows = "confused")
                ch_k "I'll hook up with who I want!"
                return
            if "monogamous" not in KittyX.daily_history:
                call change_Girl_stat(KittyX, "obedience", 3)
            $ KittyX.add_word(1, 0, "monogamous")
            $ KittyX.traits.append("monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in KittyX.traits:
            if approval_check(KittyX, 650, "O", taboo_modifier=0):
                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "Right, gotcha."
            elif approval_check(KittyX, 800, "L", taboo_modifier=0):
                $ KittyX.change_face("sly", 1)
                ch_k "Not like you'd give me the time to do that. . ."
                ch_k "right?"
            else:
                $ KittyX.change_face("sly", 1, brows = "confused")
                if "monogamous" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "love", -2)
                ch_k "You're not the boss of my pussy!"
            if "monogamous" not in KittyX.daily_history:
                call change_Girl_stat(KittyX, "obedience", 3)
            if "monogamous" in KittyX.traits:
                $ KittyX.traits.remove("monogamous")
            $ KittyX.add_word(1, 0, "monogamous")
        "Never mind.":
            pass
    return



label Kitty_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ KittyX.change_face("sly", 1, brows = "confused")
    menu:
        ch_k "Um. . . I guess?"
        "Could you maybe just ask instead?" if "chill" not in KittyX.traits:
            if KittyX.thirst >= 60 and not approval_check(KittyX, 1500, "LO", taboo_modifier=0):

                $ KittyX.change_face("surprised", 2)
                if "chill" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "obedience", -2)
                ch_k "Well- Well maybe spend some more time with me!"
                $ KittyX.change_face("angry", 1, eyes = "side")
                return
            elif approval_check(KittyX, 900, "LO", taboo_modifier=0) and KittyX.love >= KittyX.obedience:

                $ KittyX.change_face("sadside", 1)
                if "chill" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "love", 1)
                ch_k "Sorry, [KittyX.player_petname]. . ."
                ch_k "I can't keep my hands to myself. . ."
                ch_k "I'll try though. . ."
            elif approval_check(KittyX, 400, "O", taboo_modifier=0):

                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "I guess. . ."
            else:

                $ KittyX.change_face("sly", 1)
                ch_k "I can't keep my hands to myself. . ."
                return
            if "chill" not in KittyX.daily_history:
                call change_Girl_stat(KittyX, "obedience", 3)
            $ KittyX.add_word(1, 0, "chill")
            $ KittyX.traits.append("chill")
        "Don't bother me like that." if "chill" not in KittyX.traits:
            if approval_check(KittyX, 900, "O", taboo_modifier=0):

                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "Ok."
            elif KittyX.thirst >= 60 and not approval_check(KittyX, 600, "O", taboo_modifier=0):

                $ KittyX.change_face("angry", 1)
                if "chill" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "obedience", -2)
                ch_k "Don't keep me waiting then!"
                return
            elif approval_check(KittyX, 400, "O", taboo_modifier=0):

                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "Fine. . ."
            elif approval_check(KittyX, 500, "LO", taboo_modifier=0) and not approval_check(KittyX, 500, "I", taboo_modifier=0):

                $ KittyX.change_face("sly", 1)
                ch_k "Rude."
                ch_k ". . . I'll try though. . ."
            else:

                $ KittyX.change_face("sly", 1, brows = "confused")
                ch_k "I don't know. I guess we'll see. . ."
                return
            if "chill" not in KittyX.daily_history:
                call change_Girl_stat(KittyX, "obedience", 3)
            $ KittyX.add_word(1, 0, "chill")
            $ KittyX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(KittyX, 800, "L", taboo_modifier=0):
                $ KittyX.change_face("sly", 1)
                ch_k "Roger, roger. . ."
            elif approval_check(KittyX, 700, "O", taboo_modifier=0):
                $ KittyX.change_face("sly", 1, eyes = "side")
                ch_k "You bet!"
            else:
                $ KittyX.change_face("sly", 1, brows = "confused")
                if "chill" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "love", -2)
                ch_k "I don't know."
                ch_k "If I've got the time."
                ch_k "I guess."
            if "chill" not in KittyX.daily_history:
                call change_Girl_stat(KittyX, "obedience", 3)
            if "chill" in KittyX.traits:
                $ KittyX.traits.remove("chill")
            $ KittyX.add_word(1, 0, "chill")
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
                            if KittyX.player_favorite_action == "sex":
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "Yeah, I know that. . ."
                            elif KittyX.favorite_action == "sex":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 10)
                                ch_k "I really like it too!"
                            elif KittyX.permanent_History["sex"] >= 5:
                                ch_k "Well I don't mind that."
                            elif not KittyX.permanent_History["sex"]:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who's fucking you? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("bemused")
                                ch_k "Heh, um, yeah, it's nice. . ."
                            $ KittyX.player_favorite_action = "sex"
                        "Anal.":

                            $ KittyX.change_face("sly")
                            if KittyX.player_favorite_action == "anal":
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "So you've said. . ."
                            elif KittyX.favorite_action == "anal":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 10)
                                ch_k "I love it too!"
                            elif KittyX.permanent_History["anal"] >= 10:
                                ch_k "Yeah, it's. . . nice. . ."
                            elif not KittyX.permanent_History["anal"]:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who's fucking you? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("bemused", eyes = "side")
                                ch_k "Heh, heh, yeah, um, it's ok. . ."
                            $ KittyX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ KittyX.change_face("sly")
                            if KittyX.player_favorite_action == "blowjob":
                                call change_Girl_stat(KittyX, "lust", 3)
                                ch_k "Yeah, I know."
                            elif KittyX.favorite_action == "blowjob":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "I love your dick!"
                            elif KittyX.permanent_History["blowjob"] >= 10:
                                ch_k "Yeah, you're pretty tasty."
                            elif not KittyX.permanent_History["blowjob"]:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who's sucking your dick?! Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("bemused")
                                ch_k "I'm. . . getting used to the taste. . ."
                            $ KittyX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ KittyX.change_face("sly")
                            if KittyX.player_favorite_action == "titjob":
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "Yeah, you've said that before. . ."
                            elif KittyX.favorite_action == "titjob":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 7)
                                ch_k "Yeah, I enjoy that too. . ."
                            elif KittyX.permanent_History["titjob"] >= 10:
                                ch_k "It's certainly an interesting experience . . ."
                            elif not KittyX.permanent_History["titjob"]:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who's titfucking you? It's Ms. Frost, isn't it!"
                            else:
                                $ KittyX.change_face("bemused")
                                ch_k "That's nice of you to say. . ."
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "inhibition", 10)
                            $ KittyX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ KittyX.change_face("sly")
                            if KittyX.player_favorite_action == "footjob":
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "Yeah, you've said that. . ."
                            elif KittyX.favorite_action == "footjob":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 7)
                                ch_k "You do feel pretty nice. . ."
                            elif KittyX.permanent_History["footjob"] >= 10:
                                ch_k "I like it too . . ."
                            elif not KittyX.permanent_History["footjob"]:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who's playing footsie with you? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("bemused")
                                ch_k "Yeah, it's nice. . ."
                            $ KittyX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ KittyX.change_face("sly")
                            if KittyX.player_favorite_action == "handjob":
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "Yeah, you've said that. . ."
                            elif KittyX.favorite_action == "handjob":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 7)
                                ch_k "You do feel pretty comfy. . ."
                            elif KittyX.permanent_History["handjob"] >= 10:
                                ch_k "I like it too . . ."
                            elif not KittyX.permanent_History["handjob"]:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who's jerking you off? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("bemused")
                                ch_k "Yeah, it's nice. . ."
                            $ KittyX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = KittyX.permanent_History["fondle_breasts"]+ KittyX.permanent_History["fondle_thighs"]+ KittyX.permanent_History["suck_breasts"] + KittyX.permanent_History["hotdog"]
                            $ KittyX.change_face("sly")
                            if KittyX.player_favorite_action == "fondle":
                                call change_Girl_stat(KittyX, "lust", 3)
                                ch_k "Yeah, I think we're clear on that. . ."
                            elif KittyX.favorite_action in ("hotdog", "suck_breasts", "fondle_breasts", "fondle_thighs"):
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "I love when you touch me. . ."
                            elif counter >= 10:
                                ch_k "Yeah, it's really nice . . ."
                            elif not counter:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who's letting you feel her up? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("bemused")
                                ch_k "I do like how that feels. . ."
                            $ KittyX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ KittyX.change_face("sly")
                            if KittyX.player_favorite_action == "kiss":
                                call change_Girl_stat(KittyX, "love", 3)
                                ch_k "Such a romantic. . ."
                            elif KittyX.favorite_action == "kiss":
                                call change_Girl_stat(KittyX, "love", 5)
                                call change_Girl_stat(KittyX, "lust", 5)
                                ch_k "Hmm, the taste of you on my lips. . ."
                            elif KittyX.permanent_History["kiss"] >= 10:
                                ch_k "I love kissing you too . . ."
                            elif not KittyX.permanent_History["kiss"]:
                                $ KittyX.change_face("perplexed")
                                ch_k "Who are you kissing? Is it Ms. Frost?!"
                            else:
                                $ KittyX.change_face("bemused")
                                ch_k "I like kissing you too. . ."
                            $ KittyX.player_favorite_action = "kiss"

                    $ KittyX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(KittyX, 800):
                    $ KittyX.change_face("perplexed")
                    ch_k "Rude."
                else:
                    if KittyX.SEXP >= 50:
                        $ KittyX.change_face("sly")
                        ch_k "You should know that. . ."
                    else:
                        $ KittyX.change_face("bemused")
                        $ KittyX.eyes = "side"
                        ch_k "Hmm, I don't know. . ."


                    if not KittyX.favorite_action or KittyX.favorite_action == "kiss":
                        ch_k "I do love it when we kiss. . ."
                    elif KittyX.favorite_action == "anal":
                        if KittyX.permanent_History["anal"] >= 10:
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
                    $ KittyX.change_face("perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("bemused")
                        call change_Girl_stat(KittyX, "obedience", 1)
                        ch_k "Well, I guess I can be quieter. . ."
                        $ KittyX.traits.remove("vocal")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("sadside")
                        call change_Girl_stat(KittyX, "obedience", 1)
                        ch_k "Um, ok, [KittyX.player_petname]."
                        $ KittyX.traits.remove("vocal")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("sly")
                        call change_Girl_stat(KittyX, "love", -3)
                        call change_Girl_stat(KittyX, "obedience", -1)
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        ch_k "You wish, [KittyX.player_petname]."
                    else:
                        $ KittyX.change_face("angry")
                        call change_Girl_stat(KittyX, "love", -5)
                        call change_Girl_stat(KittyX, "obedience", -3)
                        call change_Girl_stat(KittyX, "inhibition", 10)
                        ch_k "Oh, am I too {i}chatty{/i} when I'm getting you off?"

                    $ KittyX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in KittyX.traits:
                if "setvocal" in KittyX.daily_history:
                    $ KittyX.change_face("perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("sly")
                        call change_Girl_stat(KittyX, "obedience", 2)
                        ch_k "Hmm, ok. . ."
                        $ KittyX.traits.append("vocal")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("sadside")
                        call change_Girl_stat(KittyX, "obedience", 2)
                        ch_k "I guess I could try, [KittyX.player_petname]."
                        $ KittyX.traits.append("vocal")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("sly")
                        call change_Girl_stat(KittyX, "obedience", 3)
                        ch_k "I guess I could, [KittyX.player_petname]."
                        $ KittyX.traits.append("vocal")
                    else:
                        $ KittyX.change_face("angry")
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        ch_k "Hmm, I don't know about that."

                    $ KittyX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in KittyX.traits:
                if "initiative" in KittyX.daily_history:
                    $ KittyX.change_face("perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("bemused")
                        call change_Girl_stat(KittyX, "obedience", 1)
                        ch_k "Heh, if you insist. . ."
                        $ KittyX.traits.append("passive")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("sadside")
                        call change_Girl_stat(KittyX, "obedience", 1)
                        ch_k "I'll try to hold back, [KittyX.player_petname]."
                        $ KittyX.traits.append("passive")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("sly")
                        call change_Girl_stat(KittyX, "love", -3)
                        call change_Girl_stat(KittyX, "obedience", -1)
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        ch_k "You wish, [KittyX.player_petname]."
                    else:
                        $ KittyX.change_face("angry")
                        call change_Girl_stat(KittyX, "love", -5)
                        call change_Girl_stat(KittyX, "obedience", -3)
                        call change_Girl_stat(KittyX, "inhibition", 10)
                        ch_k "If I feel like it."

                    $ KittyX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in KittyX.traits:
                if "initiative" in KittyX.daily_history:
                    $ KittyX.change_face("perplexed")
                    ch_k "We've been over this."
                else:
                    if approval_check(KittyX, 1000) and KittyX.obedience <= KittyX.love:
                        $ KittyX.change_face("bemused")
                        call change_Girl_stat(KittyX, "obedience", 1)
                        ch_k "Heh, I'll see what I can do. . ."
                        $ KittyX.traits.remove("passive")
                    elif approval_check(KittyX, 700, "O"):
                        $ KittyX.change_face("sadside")
                        call change_Girl_stat(KittyX, "obedience", 1)
                        ch_k "I can do that, [KittyX.player_petname]."
                        $ KittyX.traits.remove("passive")
                    elif approval_check(KittyX, 600):
                        $ KittyX.change_face("sly")
                        call change_Girl_stat(KittyX, "obedience", 3)
                        ch_k "I can try, [KittyX.player_petname]."
                        $ KittyX.traits.remove("passive")
                    else:
                        $ KittyX.change_face("angry")
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        ch_k "You're not my supervisor!"

                    $ KittyX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in KittyX.history:
                call Kitty_Jumped
            "About when you masturbate":
                call NoFap (KittyX)

            "Never mind" if line == "Yeah, what did you want to talk about?":
                return
            "That's all." if line != "Yeah, what did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return




label Kitty_Chitchat(O=0, Options = ["default", "default", "default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:

        if KittyX not in Player.Phonebook:
            if approval_check(KittyX, 500, "L") or approval_check(KittyX, 250, "I"):
                ch_k "You know, I never got around to giving you my number, here you go."
                $ Player.Phonebook.append(KittyX)
                return
            elif approval_check(KittyX, 250, "O"):
                ch_k "You know, you should probably have my number, here you go."
                $ Player.Phonebook.append(KittyX)
                return

        if "hungry" not in KittyX.traits and (KittyX.permanent_History["swallowed"] + KittyX.had_chat[2]) >= 10 and KittyX.location == Player.location:
            call Kitty_Hungry
            return
        if Player.location != "bg_restaurant" and Player.location != "bg_halloween" and (not taboo or approval_check(KittyX, 800, "I")):
            if KittyX.location == Player.location and KittyX.thirst >= 30 and "refused" not in KittyX.daily_history and "quicksex" not in KittyX.daily_history:
                $ Girl.change_face("smile", 2, brows = "sad")
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

        if KittyX.went_on_date >= 1 and Player.location != "bg_restaurant":

            $ Options.append("dated")
        if "cheek" in KittyX.daily_history and "cheek" not in KittyX.had_chat:

            $ Options.append("cheek")
        if KittyX.permanent_History["kiss"] >= 5:

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
        if "lace_bra" in KittyX.inventory or "lace_panties" in KittyX.inventory:

            if "lingerie" not in KittyX.had_chat:
                $ Options.append("lingerie")
        if KittyX.permanent_History["handjob"]:

            $ Options.append("handy")
        if KittyX.permanent_History["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in KittyX.daily_history or "painted" in KittyX.daily_history:

            $ Options.append("facial")
        if KittyX.permanent_History["sleepover"]:

            $ Options.append("sleepwear")
        if KittyX.permanent_History["creampied"] or KittyX.permanent_History["anal_creampied"]:

            $ Options.append("creampie")
        if KittyX.permanent_History["sex"] or KittyX.permanent_History["anal"]:

            $ Options.append("sexed")
        if KittyX.permanent_History["anal"]:

            $ Options.append("anal")




        if (Player.location == "bg_kitty" or Player.location == "bg_player") and "relationship" not in KittyX.daily_history:
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
        $ KittyX.change_face("confused")
        ch_k "(sniff, sniff). . . is that. . . chimp? . . ."
        $ KittyX.change_face("perplexed", 1)
        ch_k ". . . but it's[KittyX.like]. . . {i}sexy{/i} chimp?"
    elif Options[0] == "purple":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("sly", 1)
        ch_k "(sniff, sniff). . . huh, what's that smell? . ."
        ch_k ". . . could I get you something?"
    elif Options[0] == "corruption":
        $ KittyX.daily_history.append("cologne chat")
        $ KittyX.change_face("confused")
        ch_k "(sniff, sniff). . . that's pretty overpowering. . ."
        $ KittyX.change_face("sly")
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
        $ KittyX.change_face("smile", 1)
        ch_k "More than just {i}okay{/i}."
        $ KittyX.had_chat.append("cheek")

    elif Options[0] == "dated":

        ch_k "Heya,[KittyX.player_petname]. I[KittyX.like]had a lot of fun last night. We should do that again sometime."

    elif Options[0] == "kissed":

        $ KittyX.change_face("sly", 1)
        ch_k "[KittyX.Like]. . .anybody ever tell you how good a kisser you are, [KittyX.player_petname]?"
        menu:
            extend ""
            "Hey. . .when you're good, you're good.":
                $ KittyX.change_face("smile", 1)
                ch_k "I think maybe you can show me {i}how{/i} good[KittyX.like]whenever you want."
            "No. You think?":
                ch_k "Yeah. I do. [KittyX.Like]a {i}lot{/i}."

    elif Options[0] == "dangerroom":

        $ KittyX.change_face("sly", 1)
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
                    call change_Girl_stat(KittyX, "love", 5)
                    call change_Girl_stat(KittyX, "love", 2)
                    if approval_check(KittyX, 1200):
                        $ KittyX.change_face("sly", 1)
                        ch_k "Yeah? {i}Maybe{/i} you should[KittyX.like]have accidents like that more often."
                    $ KittyX.change_face("smile")
                    ch_k "It's cool, [KittyX.player_petname]. Eveybody makes mistakes. . . sometimes."
                "Just you.":
                    call change_Girl_stat(KittyX, "obedience", 5)
                    if approval_check(KittyX, 1000) or approval_check(KittyX, 700, "L"):
                        call change_Girl_stat(KittyX, "love", 3)
                        $ KittyX.change_face("sly", 1)
                        ch_k "You know how to make a girl feel special, [KittyX.player_petname]."
                    else:
                        call change_Girl_stat(KittyX, "love", -5)
                        $ KittyX.change_face("angry")
                        ch_k "You're {i}such{/i} a creep, [Player.name], y'know that?"
                "Totally on purpose. I regret nothing.":
                    if approval_check(KittyX, 1200):
                        call change_Girl_stat(KittyX, "love", 3)
                        call change_Girl_stat(KittyX, "obedience", 10)
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        $ KittyX.change_face("sly", 1)
                        ch_k "Hmm. . .next time, we'll have to[KittyX.like]take advantage of the moment."
                    elif approval_check(KittyX, 800):
                        call change_Girl_stat(KittyX, "obedience", 5)
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        $ KittyX.change_face("perplexed", 2)
                        ch_k "Wha. . . um. . . okay?"
                        $ KittyX.blushing = "_blush1"
                    else:
                        call change_Girl_stat(KittyX, "love", -10)
                        call change_Girl_stat(KittyX, "love", -10)
                        call change_Girl_stat(KittyX, "obedience", 10)
                        $ KittyX.change_face("angry")
                        ch_k "You're such a creep, [KittyX.player_petname], y'know that?"

    elif Options[0] == "fondled":

        if KittyX.permanent_History["fondle_breasts"]+ KittyX.permanent_History["fondle_pussy"] + KittyX.permanent_History["fondle_ass"] >= 15:
            ch_k "I want your hands on me."
        else:
            ch_k "You know how you felt me up earlier? I could kinda[KittyX.like]get used to having your hands on me."

    elif Options[0] == "booked":

        ch_k "So.I[KittyX.like]read the books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ KittyX.change_face("sly", 2)
                ch_k "They were[KittyX.like]. . .{i}interesting{/i}."
            "Good. You looked like you could use to learn a thing or two from them.":
                call change_Girl_stat(KittyX, "love", -3)
                call change_Girl_stat(KittyX, "obedience", 5)
                call change_Girl_stat(KittyX, "inhibition", 5)
                $ KittyX.change_face("angry")
                ch_k "Guess {i}you'll{/i} never find out, huh?"
        $ KittyX.blushing = "_blush1"
        $ KittyX.had_chat.append("book")

    elif Options[0] == "lingerie":

        $ KittyX.change_face("sly", 2)
        ch_k "[KittyX.player_petname], I wanted to thank you again for the. . .{i}stuff{/i} you bought me. They're so cute!"
        $ KittyX.blushing = "_blush1"
        $ KittyX.had_chat.append("lingerie")

    elif Options[0] == "handy":

        $ KittyX.change_face("sly", 2)
        ch_k "I was just thinking about how I[KittyX.like]stroked your cock the other day. . ."
        ch_k "I loved the expression on your face. . .knowing I could[KittyX.like]make you {i}feel{/i} like that."
        $ KittyX.blushing = "_blush1"

    elif Options[0] == "blowjob":
        if "blowjob" not in KittyX.had_chat:

            $ KittyX.change_face("sly", 2)
            ch_k "So. . .uhm, be honest with me, [KittyX.player_petname]?"
            ch_k "When I gave you head. . . was it any good?"
            ch_k "I kinda had a hard time getting all of you into my mouth."
            menu:
                extend ""
                "You were totally amazing.":
                    call change_Girl_stat(KittyX, "love", 5)
                    call change_Girl_stat(KittyX, "inhibition", 10)
                    $ KittyX.change_face("sexy", 1)
                    ch_k "Awesome. 'Cause I can't wait to try again."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(KittyX, 300, "I") or not approval_check(KittyX, 800):
                        call change_Girl_stat(KittyX, "love", -5)
                        call change_Girl_stat(KittyX, "obedience", 10)
                        call change_Girl_stat(KittyX, "inhibition", 10)
                        $ KittyX.change_face("perplexed", 1)
                        ch_k "Yeah? Well then maybe I'll get some practice in before we do it again."
                    else:
                        call change_Girl_stat(KittyX, "obedience", 15)
                        call change_Girl_stat(KittyX, "inhibition", 5)
                        $ KittyX.change_face("sexy", 1)
                        ch_k "Yeah? Well, I'm[KittyX.player_petname]looking forward our next training session, then."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    call change_Girl_stat(KittyX, "love", -10)
                    call change_Girl_stat(KittyX, "obedience", 10)
                    $ KittyX.change_face("angry", 2)
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
            $ KittyX.change_face("sly", 1)
            ch_k "Not bad. . ."
            $ KittyX.had_chat.append("swallow")

    elif Options[0] == "facial":

        ch_k "Hey. . .this is gonna sound kinda[KittyX.like]weird, but. . ."
        $ KittyX.change_face("sexy", 2)
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
        $ KittyX.change_face("sexy", 2)
        ch_k ". . .[KittyX.Like]every time I masturbate. . ."
        ch_k "I think about how it felt, with you inside of me."
        $ KittyX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ KittyX.change_face("sly", 2)
        ch_k "Y'know. . .after the other night, I'm kinda having trouble[KittyX.like]sitting down."
        $ KittyX.change_face("sexy", 2)
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
                $ KittyX.change_face("perplexed", 1)
                call change_Girl_stat(KittyX, "love", 2)
                ch_k ". . ."
            "Yeah, I know.":
                call change_Girl_stat(KittyX, "love", 5)
            "Huh, why not go by that then?":
                if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                    $ KittyX.name = "Shadowcat"
                    call change_Girl_stat(KittyX, "obedience", 5)
                    ch_k "I guess? . ."
                else:
                    ch_k "Kind of a silly name to go around with. . ."
                    menu:
                        extend ""
                        "Ok, \"[KittyX.name]\" it is then.":
                            $ KittyX.change_face("smile", 1)
                        "I insist.":
                            call change_Girl_stat(KittyX, "love", -10)
                            call change_Girl_stat(KittyX, "obedience", 10)
                            $ KittyX.change_face("angry", 2)
        ch_k ". . ."

    elif Options[0] == "Katherine":
        $ KittyX.names.append("Katherine")
        ch_k "My full name is \"Katherine Pryde.\""
        ch_k "You probably didn't know that."
        menu:
            extend ""
            "Oh, ok then.":
                $ KittyX.change_face("perplexed", 1)
                call change_Girl_stat(KittyX, "love", 2)
                ch_k ". . ."
            "I kind of prefer \"[KittyX.name].\"":
                call change_Girl_stat(KittyX, "love", 5)
                call change_Girl_stat(KittyX, "inhibition", 5)
                if approval_check(KittyX, 800, "LO"):
                    call change_Girl_stat(KittyX, "obedience", 5)
                ch_k "Yeah, me too. . ."
            "Why not go by \"Katherine\" then?":
                if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                    $ KittyX.name = "Katherine"
                    call change_Girl_stat(KittyX, "obedience", 5)
                    ch_k "I suppose I could. . ."
                else:
                    ch_k "I don't really like it that much. . ."
                    menu:
                        extend ""
                        "Ok, \"[KittyX.name]\" it is then.":
                            $ KittyX.change_face("smile", 1)
                        "I insist.":
                            call change_Girl_stat(KittyX, "love", -10)
                            call change_Girl_stat(KittyX, "obedience", 10)
                            $ KittyX.change_face("angry", 2)
                            ch_k "!!!"


    elif Options[0] == "seenpeen":
        $ KittyX.change_face("sly", 2)
        ch_k "Maybe I didn't mention it before, but. . ."
        ch_k "That cock of yours is. . . impressive."
        $ KittyX.change_face("bemused", 1)
        call change_Girl_stat(KittyX, "love", 3)
        $ KittyX.history.remove("seenpeen")
    elif Options[0] == "topless":
        $ KittyX.change_face("bemused", 2, eyes = "side")
        ch_k "Hey, when you saw me. . . topless earlier, you didn't have much to say. . ."
        ch_k "What'd you think?"
        call Kitty_First_TMenu
        $ KittyX.history.remove("topless")
    elif Options[0] == "bottomless":
        $ KittyX.change_face("bemused", 2, eyes = "side")
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
        call Kitty_Sexfriend
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
            $ KittyX.change_face("smile")
            ch_k "I'm[KittyX.like]{i}so{/i} excited [KittyX.player_petname]! I {i}totally{/i} aced Professor McCoy's Computer Science test!"
        elif D20 == 2:
            $ KittyX.change_face("sad")
            ch_k "Ever have[KittyX.like]one of those days where it seems like the whole world's out to get you?"
        elif D20 == 3:
            $ KittyX.change_face("surprised")
            ch_k "I can't believe how much stuff I've gotta get done today!"
        elif D20 == 4:
            $ KittyX.change_face("sad")
            ch_k "Hey, [KittyX.player_petname]. I got[KittyX.like]the world's worst sleep last night. I feel like I could[KittyX.like]curl up and go to bed right here."
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
                            $ KittyX.change_face("sexy", 1)
                            ch_k "I'm totally your girl, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm NOT your girl, [KittyX.player_petname]."
                    "I think I'll call you \"boo\".":

                        $ KittyX.petname = "boo"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Aw, I am your boo, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm NOT your boo, [KittyX.player_petname]."
                    "I think I'll call you \"bae\".":

                        $ KittyX.petname = "bae"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Aw, I am your bae, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm NOT your bae, [KittyX.player_petname]."
                    "I think I'll call you \"baby\".":

                        $ KittyX.petname = "baby"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Aw, cute, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "I'm not a baby!"
                    "I think I'll call you \"sweetie\".":


                        $ KittyX.petname = "sweetie"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            ch_k "Aw, that's sweet, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Too saccharine, [KittyX.player_petname]."
                    "I think I'll call you \"sexy\".":

                        $ KittyX.petname = "sexy"
                        if "lover" in KittyX.player_petnames or approval_check(KittyX, 900):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Mreow, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Not in public, [KittyX.player_petname]."
                    "I think I'll call you \"lover\".":

                        $ KittyX.petname = "lover"
                        if "lover" in KittyX.player_petnames or approval_check(KittyX, 900, "L") or approval_check(KittyX, 1400):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Love you too, [KittyX.player_petname]!"
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Not in this lifetime, [KittyX.player_petname]."
                    "I think I'll call you \"kitten\".":

                        $ KittyX.petname = "baby"
                        if "boyfriend" in KittyX.player_petnames or approval_check(KittyX, 500, "L"):
                            $ KittyX.change_face("sexy", 1)
                            ch_k "Purrr, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry")
                            ch_k "Not really that cute, [KittyX.player_petname]"
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you \"slave\".":
                        $ KittyX.petname = "slave"
                        if "master" in KittyX.player_petnames or approval_check(KittyX, 700, "O"):
                            $ KittyX.change_face("bemused", 1)
                            ch_k "As you wish, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I'm not a slave, [KittyX.player_petname]."
                    "I think I'll call you \"pet\".":

                        $ KittyX.petname = "pet"
                        if "master" in KittyX.player_petnames or approval_check(KittyX, 600, "O"):
                            $ KittyX.change_face("bemused", 1)
                            ch_k "Hmm, make sure to pet me, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I'm no house cat, [KittyX.player_petname]."
                    "I think I'll call you \"slut\".":

                        $ KittyX.petname = "slut"
                        if "sex friend" in KittyX.player_petnames or approval_check(KittyX, 1000, "OI"):
                            $ KittyX.change_face("sexy")
                            ch_k "If the name fits, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            $ KittyX.mouth = "surprised"
                            ch_k "Not unless you want to lose some teeth!"
                    "I think I'll call you \"whore\".":

                        $ KittyX.petname = "whore"
                        if "fuckbuddy" in KittyX.player_petnames or approval_check(KittyX, 1100, "OI"):
                            $ KittyX.change_face("sly")
                            ch_k "Only for you though. . ."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Can you say that with a fat lip, [KittyX.player_petname]?"
                    "I think I'll call you \"sugartits\".":

                        $ KittyX.petname = "sugartits"
                        if "sex friend" in KittyX.player_petnames or approval_check(KittyX, 1400):
                            $ KittyX.change_face("sly", 1)
                            ch_k "These little things?"
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I would hope not, [KittyX.player_petname]."
                    "I think I'll call you \"sex friend\".":

                        $ KittyX.petname = "sex friend"
                        if "sex friend" in KittyX.player_petnames or approval_check(KittyX, 600, "I"):
                            $ KittyX.change_face("sly")
                            ch_k "Rreow. . ."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "Not out loud, [KittyX.player_petname]."
                    "I think I'll call you \"fuckbuddy\".":

                        $ KittyX.petname = "fuckbuddy"
                        if "fuckbuddy" in KittyX.player_petnames or approval_check(KittyX, 700, "I"):
                            $ KittyX.change_face("sly")
                            ch_k "Yup."
                        else:
                            $ KittyX.change_face("angry", 1)
                            $ KittyX.mouth = "surprised"
                            ch_k "Don't even joke, [KittyX.player_petname]."
                    "I think I'll call you \"baby girl\".":

                        $ KittyX.petname = "baby girl"
                        if "daddy" in KittyX.player_petnames or approval_check(KittyX, 1200):
                            $ KittyX.change_face("smile", 1)
                            ch_k "You know it, [KittyX.player_petname]."
                        else:
                            $ KittyX.change_face("angry", 1)
                            ch_k "I'm no kid!"
                    "Back":

                        pass
            "Nevermind.":

                return
    return




label Kitty_Rename:

    $ KittyX.mouth = "smile"
    ch_k "Yeah?"
    menu:
        extend ""
        "I think \"Kitty's\" a pretty name." if KittyX.name != "Kitty" and "Kitty" in KittyX.names:
            $ KittyX.name = "Kitty"
            ch_k "Me too!"
        "I thought \"Kate\" sounded cool." if KittyX.name != "Kate" and "Kate" in KittyX.names:
            if "namechange" not in KittyX.daily_history:
                call change_Girl_stat(KittyX, "love", 1)
                call change_Girl_stat(KittyX, "inhibition", 2)
                call change_Girl_stat(KittyX, "inhibition", 1)
            $ KittyX.name = "Kate"
            ch_k "Yeah, I thought so too. . ."
        "Do you go by \"Katherine?\"" if KittyX.name != "Katherine" and "Katherine" in KittyX.names:
            if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                $ KittyX.name = "Katherine"
                if "namechange" not in KittyX.daily_history:
                    call change_Girl_stat(KittyX, "obedience", 2)
                ch_k "I guess. . . I could?"
            else:
                ch_k "I don't really like that one. . ."
        "Do you go by \"Shadowcat?\"" if KittyX.name != "Shadowcat" and "Shadowcat" in KittyX.names:
            if approval_check(KittyX, 1200, "LO") or approval_check(KittyX, 500, "0"):
                $ KittyX.change_face("confused")
                $ KittyX.name = "Shadowcat"
                ch_k "I guess. . . I could?"
            else:
                $ KittyX.change_face("perplexed")
                ch_k "People don't exactly call me that out of the field!"
            $ KittyX.change_face()
        "Nevermind.":
            pass
    $ KittyX.add_word(1, 0, "namechange")
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
