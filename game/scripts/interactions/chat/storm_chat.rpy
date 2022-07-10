


label Storm_Relationship:
    while True:
        menu:
            ch_s "What did you want to talk about?"
            "Do you want to be my girlfriend?" if StormX not in Player.Harem and "ex" not in StormX.traits and "story" not in Player.history:
                $ StormX.daily_history.append("relationship")
                if "asked boyfriend" in StormX.daily_history and "angry" in StormX.daily_history:
                    $ StormX.change_face("angry", 1)
                    ch_s "Please stop."
                    return
                elif "asked boyfriend" in StormX.daily_history:
                    $ StormX.change_face("sad", 1)
                    ch_s "Oh, [Girl.player_petname], no."
                    return
                elif StormX.broken_up[0]:
                    $ StormX.change_face("angry", 1)
                    ch_s "I. . . do not share."
                    if Player.Harem:
                        $ StormX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_s "It. . . will not work."

                $ StormX.daily_history.append("asked boyfriend")

                if Player.Harem and "StormYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_s "You'd need to clear it with the others first, [StormX.player_petname]."
                    else:
                        ch_s "You'd need to clear it with [Player.Harem[0].name] first, [StormX.player_petname]."
                    return

                if StormX.event_happened[5]:
                    $ StormX.change_face("bemused", 1)
                    ch_s "When I asked, you said \"no\". . ."
                else:
                    $ StormX.change_face("surprised", 2)
                    ch_s "What? . ."
                    $ StormX.change_face("smile", 1)

                call Storm_OtherWoman

                if StormX.love >= 800:
                    $ StormX.change_face("surprised", 1)
                    $ StormX.mouth = "smile"
                    call change_Girl_stat(StormX, "love", 40)
                    ch_s "I would love to!"
                    if "boyfriend" not in StormX.player_petnames:
                        $ StormX.player_petnames.append("boyfriend")
                    if "StormYes" in Player.traits:
                        $ Player.traits.remove("StormYes")
                    $ Player.Harem.append(StormX)
                    call Harem_Initiation
                    "[StormX.name] moves in and kisses you deeply."
                    $ StormX.change_face("kiss", 1)
                    $ StormX.permanent_History["kiss"] += 1
                elif StormX.obedience >= 500:
                    $ StormX.change_face("perplexed")
                    ch_s "I'm unsure, \"dating\". . ."
                elif StormX.inhibition >= 500:
                    $ StormX.change_face("smile")
                    ch_s "Can't we just keep it casual?"
                else:
                    $ StormX.change_face("perplexed", 1)
                    ch_s "I don't know about that, [StormX.player_petname]."

            "Do you want to get back together?" if "ex" in StormX.traits:
                $ StormX.daily_history.append("relationship")
                if "asked boyfriend" in StormX.daily_history and "angry" in StormX.daily_history:
                    $ StormX.change_face("angry", 1)
                    ch_s "Please stop."
                    return
                elif "asked boyfriend" in StormX.daily_history:
                    $ StormX.change_face("sad", 1)
                    ch_s "Oh, [Girl.player_petname], no."
                    return

                $ StormX.daily_history.append("asked boyfriend")

                if Player.Harem and "StormYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_s "You'd need to clear it with the others first, [StormX.player_petname]."
                    else:
                        ch_s "You'd need to clear it with [Player.Harem[0].name] first, [StormX.player_petname]."
                    return

                $ counter = 0
                call Storm_OtherWoman

                if StormX.love >= 800:
                    $ StormX.change_face("surprised", 1)
                    $ StormX.mouth = "smile"
                    call change_Girl_stat(StormX, "love", 5)
                    ch_s "I suppose I could give you another chance."
                    if "boyfriend" not in StormX.player_petnames:
                        $ StormX.player_petnames.append("boyfriend")
                    $ StormX.traits.remove("ex")
                    if "StormYes" in Player.traits:
                        $ Player.traits.remove("StormYes")
                    $ Player.Harem.append(StormX)
                    call Harem_Initiation
                    "[StormX.name] pulls you in and kisses you deeply."
                    $ StormX.change_face("kiss", 1)
                    $ StormX.permanent_History["kiss"] += 1
                elif StormX.love >= 600 and approval_check(StormX, 1500):
                    $ StormX.change_face("smile", 1)
                    call change_Girl_stat(StormX, "love", 5)
                    ch_s "I suppose I could give it another chance."
                    if "boyfriend" not in StormX.player_petnames:
                        $ StormX.player_petnames.append("boyfriend")
                    $ StormX.traits.remove("ex")
                    if "StormYes" in Player.traits:
                        $ Player.traits.remove("StormYes")
                    $ Player.Harem.append(StormX)
                    call Harem_Initiation
                    $ StormX.change_face("kiss", 1)
                    "[StormX.name] gives you a quick kiss."
                    $ StormX.change_face("sly", 1)
                    $ StormX.permanent_History["kiss"] += 1
                elif StormX.obedience >= 500:
                    $ StormX.change_face("sad")
                    ch_s "Perhaps \"relationships\" are beyond us."
                elif StormX.inhibition >= 500:
                    $ StormX.change_face("perplexed")
                    ch_s "Let's keep things casual."
                else:
                    $ StormX.change_face("perplexed", 1)
                    ch_s "You've lost my trust."



            "I wanted to ask about [[another girl]" if StormX in Player.Harem:
                call AskDateOther

            "I think we should break up." if StormX in Player.Harem:
                if "breakup talk" in StormX.recent_history:
                    ch_s "Why do you torment me?"
                elif "breakup talk" in StormX.daily_history:
                    ch_s "Not today, [StormX.player_petname]."
                else:
                    call Breakup (StormX)
            "About that talk we had before. . .":

                menu:
                    "When you said you wanted to tell me a story. . ." if "story" in Player.history and StormX.event_happened[5] == 20:
                        $ Player.history.remove("story")
                        ch_s "Ah, yes, I did have a story to tell you. . ."
                        call Storm_BF_Story
                    "I feel you were trying to tell me something before. . ." if "lover" not in StormX.traits and StormX.event_happened[6] >= 5:
                        if approval_check(StormX, 900, "L"):
                            $ StormX.event_happened[6] = 3
                            ch_s "Yes, I supposed that I did. . ."
                            $ StormX.daily_history.append("relationship")
                            call Storm_Love_Redux
                        else:
                            ch_s "I do not think you understand yet. . ."


                    "You said you wanted me to be more assertive?" if "sir" not in StormX.player_petnames and "sir" in StormX.history:
                        if "asked sub" in StormX.recent_history:
                            ch_s "That was only moments ago."
                        elif "asked sub" in StormX.daily_history:
                            ch_s "We discussed this earlier. . ."
                        else:
                            call Storm_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in StormX.player_petnames and "master" in StormX.history:
                        if "asked sub" in StormX.recent_history:
                            ch_s "That was only moments ago."
                        elif "asked sub" in StormX.daily_history:
                            ch_s "We discussed this earlier. . ."
                        else:
                            call Storm_Sub_Asked
                    "Never mind":
                        pass
            "Never mind":

                return

    return

label Storm_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((StormX.likes[Player.Harem[0].tag] - 500)/2)

    $ StormX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_s "But you are with [Player.Harem[0].name] right now, and others as well."
    else:
        ch_s "But you are with [Player.Harem[0].name], are you not?"
    menu:
        extend ""
        "She said I can be with you too." if "StormYes" in Player.traits:
            if approval_check(StormX, 1800, Bonus = counter):
                $ StormX.change_face("smile", 1)
                if StormX.love >= StormX.obedience:
                    ch_s "I suppose I can share with her."
                elif StormX.obedience >= StormX.inhibition:
                    ch_s "If that's what you want."
                else:
                    ch_s "Fine."
            else:
                $ StormX.change_face("angry", 1)
                ch_s "Yes, I suppose that she would, but I'm unwilling to share."
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "StormYes" not in Player.traits:
            if approval_check(StormX, 1800, Bonus = counter):
                $ StormX.change_face("smile", 1)
                if StormX.love >= StormX.obedience:
                    ch_s "I guess I can share you."
                elif StormX.obedience >= StormX.inhibition:
                    ch_s "If that's what you want."
                else:
                    ch_s "Fine."
                ch_s "Well ask her and tell me in the morning."
            else:
                $ StormX.change_face("angry", 1)
                ch_s "Yeah, I imagine she would, but I'm not sharing."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(StormX, 1800, Bonus = -counter):
                $ StormX.change_face("angry", 1)
                if not approval_check(StormX, 1800):
                    ch_s "It would hurt us both."
                else:
                    ch_s "That sounds beneath you."
                $ renpy.pop_call()
            else:
                $ StormX.change_face("smile", 1)
                if StormX.love >= StormX.obedience:
                    ch_s "I suppose I could get past it. . ."
                elif StormX.obedience >= StormX.inhibition:
                    ch_s "If that's what you want."
                else:
                    ch_s "Fine."
                $ StormX.traits.append("downlow")
        "I can break it off with her.":

            $ StormX.change_face("sad")
            ch_s "Then after you do, we can discuss this again."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ StormX.change_face("sad")
            ch_s "Very."
            $ renpy.pop_call()

    return


label Storm_About(Check=0):
    if Check not in all_Girls:
        ch_s "Who?"
        return
    ch_s "What do I think about her? Well. . ."
    if Check == RogueX:
        if "poly Rogue" in StormX.traits:
            ch_s "We have enjoyed each other's company. . ."
        elif StormX.likes[RogueX.tag] >= 900:
            ch_s "She does have a fine figure . ."
        elif StormX.likes[RogueX.tag] >= 800:
            ch_s "She is a lovely person. . ."
        elif StormX.likes[RogueX.tag] >= 700:
            ch_s "She is quite a hard worker."
        elif StormX.likes[RogueX.tag] >= 600:
            ch_s "She is nice."
        elif StormX.likes[RogueX.tag] >= 500:
            ch_s "I have seen her around."
        elif StormX.likes[RogueX.tag] >= 400:
            ch_s "I would rather not talk about it."
        elif StormX.likes[RogueX.tag] >= 300:
            ch_s "I hate her."
        else:
            ch_s "Bitch."
    elif Check == KittyX:
        if "poly Kitty" in StormX.traits:
            ch_s "We have enjoyed each other's company. . ."
        elif StormX.likes[KittyX.tag] >= 900:
            ch_s "She does have a petite figure . ."
        elif StormX.likes[KittyX.tag] >= 800:
            ch_s "She is a lovely person. . ."
        elif StormX.likes[KittyX.tag] >= 700:
            ch_s "She is attentive in class."
        elif StormX.likes[KittyX.tag] >= 600:
            ch_s "She is a hard worker."
        elif StormX.likes[KittyX.tag] >= 500:
            ch_s "She is in our classes, correct?"
        elif StormX.likes[KittyX.tag] >= 400:
            ch_s "I would rather not talk about it."
        elif StormX.likes[KittyX.tag] >= 300:
            ch_s "I stongly dislike her."
        else:
            ch_s "Bitch."
    elif Check == EmmaX:
        if "poly Emma" in StormX.traits:
            ch_s "We have enjoyed each other's company. . ."
        elif StormX.likes[EmmaX.tag] >= 900:
            ch_s "She does have a volumptuous figure . ."
        elif StormX.likes[EmmaX.tag] >= 800:
            ch_s "I have grown to enjoy her company. . ."
        elif StormX.likes[EmmaX.tag] >= 700:
            ch_s "She is an excellent educator."
        elif StormX.likes[EmmaX.tag] >= 600:
            ch_s "I don't mind sharing classes with her."
        elif StormX.likes[EmmaX.tag] >= 500:
            ch_s "She's fine."
        elif StormX.likes[EmmaX.tag] >= 400:
            ch_s "I could do with less of her attitude."
        elif StormX.likes[EmmaX.tag] >= 300:
            ch_s "She needs to stay out of my head."
        else:
            ch_s "Bitch."
    if Check == LauraX:
        if "poly Laura" in StormX.traits:
            ch_s "We have enjoyed each other's company. . ."
        elif StormX.likes[LauraX.tag] >= 900:
            ch_s "She does have a fine figure . ."
        elif StormX.likes[LauraX.tag] >= 800:
            ch_s "She is a lovely person. . . eventually."
        elif StormX.likes[LauraX.tag] >= 700:
            ch_s "She is quite a strong warrior."
        elif StormX.likes[LauraX.tag] >= 600:
            ch_s "She is aggressive."
        elif StormX.likes[LauraX.tag] >= 500:
            ch_s "I have seen her around."
        elif StormX.likes[LauraX.tag] >= 400:
            ch_s "I would rather not talk about it."
        elif StormX.likes[LauraX.tag] >= 300:
            ch_s "I hate her."
        else:
            ch_s "Bitch."
    elif Check == JeanX:
        if "poly Jean" in StormX.traits:
            ch_s "We have enjoyed each other's company. . ."
        elif StormX.likes[JeanX.tag] >= 900:
            ch_s "She does have a fine figure . ."
        elif StormX.likes[JeanX.tag] >= 800:
            ch_s "She is an acquired taste. . ."
        elif StormX.likes[JeanX.tag] >= 700:
            ch_s "She. . . does try."
        elif StormX.likes[JeanX.tag] >= 600:
            ch_s "I've become accustomed to her."
        elif StormX.likes[JeanX.tag] >= 500:
            ch_s "She can be difficult."
        elif StormX.likes[JeanX.tag] >= 400:
            ch_s "She is a chore."
        elif StormX.likes[JeanX.tag] >= 300:
            ch_s "I seriously dislike her."
        else:
            ch_s "Bitch."
    elif Check == JubesX:
        if "poly Jubes" in StormX.traits:
            ch_s "We have enjoyed each other's company. . ."
        elif StormX.likes[JubesX.tag] >= 900:
            ch_s "She does have a wonderful figure . ."
        elif StormX.likes[JubesX.tag] >= 800:
            ch_s "She is a lovely person. . ."
        elif StormX.likes[JubesX.tag] >= 700:
            ch_s "She is attentive in class."
        elif StormX.likes[JubesX.tag] >= 600:
            ch_s "She is a hard worker."
        elif StormX.likes[JubesX.tag] >= 500:
            ch_s "She is in our classes, correct?"
        elif StormX.likes[JubesX.tag] >= 400:
            ch_s "She is a bit of a biter."
        elif StormX.likes[JubesX.tag] >= 300:
            ch_s "I stongly dislike her."
        else:
            ch_s "Bitch."
    return


label Storm_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "monogamous" not in StormX.traits:
            if StormX.thirst >= 60 and not approval_check(StormX, 1700, "LO", taboo_modifier=0):

                $ StormX.change_face("sly", 1)
                if "monogamous" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "obedience", -2)
                ch_s "I do have needs that must be met. . ."
                return
            elif approval_check(StormX, 1200, "LO", taboo_modifier=0) and StormX.love >= StormX.obedience:

                $ StormX.change_face("sly", 1)
                if "monogamous" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "love", 1)
                ch_s "I did not take you for the jealous type."
                ch_s "Very well, for now. . ."
            elif approval_check(StormX, 700, "O", taboo_modifier=0):

                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "Fine."
            else:

                $ StormX.change_face("sly", 1)
                ch_s "I do have needs. No."
                return
            if "monogamous" not in StormX.daily_history:
                call change_Girl_stat(StormX, "obedience", 3)
            $ StormX.add_word(1, 0, "monogamous")
            $ StormX.traits.append("monogamous")
        "Don't hook up with other girls." if "monogamous" not in StormX.traits:
            if approval_check(StormX, 900, "O", taboo_modifier=0):

                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "If that is what you want."
            elif StormX.thirst >= 60 and not approval_check(StormX, 1700, "LO", taboo_modifier=0):

                $ StormX.change_face("sly", 1)
                if "monogamous" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "obedience", -2)
                ch_s "I do have needs that must be met. . ."
                return
            elif approval_check(StormX, 600, "O", taboo_modifier=0):

                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "Fine."
            elif approval_check(StormX, 1400, "LO", taboo_modifier=0):

                $ StormX.change_face("sly", 1)
                ch_s "Take care with your words, but I will consider it."
            else:

                $ StormX.change_face("sly", 1, brows = "confused")
                ch_s "I would watch your tone."
                return
            if "monogamous" not in StormX.daily_history:
                call change_Girl_stat(StormX, "obedience", 3)
            $ StormX.add_word(1, 0, "monogamous")
            $ StormX.traits.append("monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in StormX.traits:
            if approval_check(StormX, 700, "O", taboo_modifier=0):
                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s ". . . ok then."
            elif approval_check(StormX, 800, "L", taboo_modifier=0):
                $ StormX.change_face("sly", 1)
                ch_s "Fine. . ."
            else:
                $ StormX.change_face("sly", 1, brows = "confused")
                if "monogamous" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "love", -2)
                ch_s "It sounds like I have some weekend plans to make then."
            if "monogamous" not in StormX.daily_history:
                call change_Girl_stat(StormX, "obedience", 3)
            if "monogamous" in StormX.traits:
                $ StormX.traits.remove("monogamous")
            $ StormX.add_word(1, 0, "monogamous")
        "Never mind.":
            pass
    return



label Storm_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ StormX.change_face("sly", 1, brows = "confused")
    menu:
        ch_s "Yeah?"
        "Could you maybe just ask instead?" if "chill" not in StormX.traits:
            if StormX.thirst >= 60 and not approval_check(StormX, 1500, "LO", taboo_modifier=0):

                $ StormX.change_face("sly", 1)
                if "chill" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "obedience", -2)
                ch_s "I would if you would come to me more often. . ."
                return
            elif approval_check(StormX, 1000, "LO", taboo_modifier=0) and StormX.love >= StormX.obedience:

                $ StormX.change_face("surprised", 1)
                if "chill" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "love", 1)
                ch_s "I am sorry, but I have needs. . ."
                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "I will -try- to keep them in check. . ."
            elif approval_check(StormX, 500, "O", taboo_modifier=0):

                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "I am sorry about that. . ."
            else:

                $ StormX.change_face("sly", 1)
                ch_s "I will take what I need."
                return
            if "chill" not in StormX.daily_history:
                call change_Girl_stat(StormX, "obedience", 3)
            $ StormX.add_word(1, 0, "chill")
            $ StormX.traits.append("chill")
        "Don't bother me like that." if "chill" not in StormX.traits:
            if approval_check(StormX, 800, "O", taboo_modifier=0):

                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "Very well."
            elif StormX.thirst >= 60 and not approval_check(StormX, 500, "O", taboo_modifier=0):

                $ StormX.change_face("sly", 1)
                if "chill" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "obedience", -2)
                ch_s "I would if you would come to me more often. . ."
                return
            elif approval_check(StormX, 400, "O", taboo_modifier=0):

                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "Fine. . ."
            elif approval_check(StormX, 500, "LO", taboo_modifier=0) and not approval_check(StormX, 500, "I", taboo_modifier=0):

                $ StormX.change_face("sly", 1)
                ch_s "Watch your language."
                ch_s "I will -try- to keep my needs in check. . ."
            else:

                $ StormX.change_face("sly", 1)
                ch_s "I will take what I need."
                return
            if "chill" not in StormX.daily_history:
                call change_Girl_stat(StormX, "obedience", 3)
            $ StormX.add_word(1, 0, "chill")
            $ StormX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(StormX, 800, "L", taboo_modifier=0):
                $ StormX.change_face("sly", 1)
                ch_s "Noted. . ."
            elif approval_check(StormX, 700, "O", taboo_modifier=0):
                $ StormX.change_face("sly", 1, eyes = "side")
                ch_s "Very well. . ."
            else:
                $ StormX.change_face("sly", 1, brows = "confused")
                if "chill" not in StormX.daily_history:
                    call change_Girl_stat(StormX, "love", -2)
                ch_s "If I find myself in need, certainly."
            if "chill" not in StormX.daily_history:
                call change_Girl_stat(StormX, "obedience", 3)
            if "chill" in StormX.traits:
                $ StormX.traits.remove("chill")
            $ StormX.add_word(1, 0, "chill")
        "Um, never mind.":
            pass
    return




label Storm_Hungry:
    if StormX.had_chat[3]:
        ch_s "[[licks her lips] could use another taste. . ."
    elif StormX.had_chat[2]:
        ch_s "I have really acquired a taste for that serum of yours."
    else:
        ch_s "[[licks her lips] I really love your taste. . ."
    $ StormX.traits.append("hungry")
return





label Storm_SexChat:
    $ line = "Yes? What did you want to discuss?" if not line else line
    while True:
        menu:
            ch_s "[line]"
            "My favorite thing to do is. . .":
                if "setfav" in StormX.daily_history:
                    ch_s "We've been over this."
                else:
                    menu:
                        "Sex.":
                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "sex":
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action == "sex":
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 10)
                                ch_s "I also enjoy that. . ."
                            elif StormX.permanent_History["sex"] >= 5:
                                ch_s "It certainly is enjoyable. . ."
                            elif not StormX.permanent_History["sex"]:
                                $ StormX.change_face("perplexed")
                                ch_s "And who is fucking you?"
                            else:
                                $ StormX.change_face("bemused")
                                ch_s "Yes. . . um. . . it is fine. . ."
                            $ StormX.player_favorite_action = "sex"
                        "Anal.":

                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "anal":
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action == "anal":
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 10)
                                ch_s "I also enjoy that. . ."
                            elif StormX.permanent_History["anal"] >= 10:
                                ch_s "It certainly is enjoyable. . ."
                            elif not StormX.permanent_History["anal"]:
                                $ StormX.change_face("perplexed")
                                ch_s "And who is fucking you?"
                            else:
                                $ StormX.change_face("bemused", eyes = "side")
                                ch_s "Yes. . . um. . . it is fine. . ."
                            $ StormX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "blowjob":
                                call change_Girl_stat(StormX, "lust", 3)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action == "blowjob":
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "I would have to agree. . ."
                            elif StormX.permanent_History["blowjob"] >= 10:
                                ch_s "You are quite delicious. . ."
                            elif not StormX.permanent_History["blowjob"]:
                                $ StormX.change_face("perplexed")
                                ch_s "Who's sucking your dick?!"
                            else:
                                $ StormX.change_face("bemused")
                                ch_s "I'm. . . getting used to the taste. . ."
                            $ StormX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "titjob":
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action == "titjob":
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 7)
                                ch_s "I also enjoy that. . ."
                            elif StormX.permanent_History["titjob"] >= 10:
                                ch_s "It certainly is enjoyable. . ."
                            elif not StormX.permanent_History["titjob"]:
                                $ StormX.change_face("perplexed")
                                ch_s "And who is titfucking you?"
                            else:
                                $ StormX.change_face("bemused")
                                ch_s "Yes. . . um. . . it is fine. . ."
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "inhibition", 10)
                            $ StormX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "footjob":
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action == "footjob":
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 7)
                                ch_s "I also enjoy that. . ."
                            elif StormX.permanent_History["footjob"] >= 10:
                                ch_s "I like it too . . ."
                            elif not StormX.permanent_History["footjob"]:
                                $ StormX.change_face("perplexed")
                                ch_s "And who is playing footsie with you?"
                            else:
                                $ StormX.change_face("bemused")
                                ch_s "Yes. . . um. . . it is fine. . ."
                            $ StormX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "handjob":
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action == "handjob":
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 7)
                                ch_s "I also enjoy that. . ."
                            elif StormX.permanent_History["handjob"] >= 10:
                                ch_s "I like it too . . ."
                            elif not StormX.permanent_History["handjob"]:
                                $ StormX.change_face("perplexed")
                                ch_s "And who is jerking you off?"
                            else:
                                $ StormX.change_face("bemused")
                                ch_s "Yes. . . um. . . it is fine. . ."
                            $ StormX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = StormX.permanent_History["fondle_breasts"]+ StormX.permanent_History["fondle_thighs"]+ StormX.permanent_History["suck_breasts"] + StormX.permanent_History["hotdog"]
                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "fondle":
                                call change_Girl_stat(StormX, "lust", 3)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action in ("hotdog", "suck_breasts", "fondle_breasts", "fondle_thighs"):
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "I do not mind that myself. . ."
                            elif counter >= 10:
                                ch_s "It certainly is enjoyable. . ."
                            elif not counter:
                                $ StormX.change_face("perplexed")
                                ch_s "And who is letting you feel her up?"
                            else:
                                $ StormX.change_face("bemused")
                                ch_s "I do enjoy how that feels. . ."
                            $ StormX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ StormX.change_face("sly")
                            if StormX.player_favorite_action == "kiss":
                                call change_Girl_stat(StormX, "love", 3)
                                ch_s "Yes, so you've said."
                            elif StormX.favorite_action == "kiss":
                                call change_Girl_stat(StormX, "love", 5)
                                call change_Girl_stat(StormX, "lust", 5)
                                ch_s "I also enjoy that. . ."
                            elif StormX.permanent_History["kiss"] >= 10:
                                ch_s "It certainly is enjoyable. . ."
                            elif not StormX.permanent_History["kiss"]:
                                $ StormX.change_face("perplexed")
                                ch_s "And who are you kissing?"
                            else:
                                $ StormX.change_face("bemused")
                                ch_s "I enjoy kissing you as well. . ."
                            $ StormX.player_favorite_action = "kiss"

                    $ StormX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(StormX, 800):
                    $ StormX.change_face("perplexed")
                    ch_s ". . . I would rather not say."
                else:
                    if StormX.SEXP >= 50:
                        $ StormX.change_face("sly")
                        ch_s "You should be aware. . ."
                    else:
                        $ StormX.change_face("bemused")
                        $ StormX.eyes = "side"
                        ch_s "Well. . ."


                    if not StormX.favorite_action or StormX.favorite_action == "kiss":
                        ch_s "Kissing?"
                    elif StormX.favorite_action == "anal":
                        ch_s "Probably anal."
                    elif StormX.favorite_action == "eat_ass":
                        ch_s "When you lick my ass."
                    elif StormX.favorite_action == "finger_ass":
                        ch_s "Fingering my asshole, probably."
                    elif StormX.favorite_action == "sex":
                        ch_s "I enjoy sex the most."
                    elif StormX.favorite_action == "eat_pussy":
                        ch_s "When you lick my pussy."
                    elif StormX.favorite_action == "fondle_pussy":
                        ch_s "When you finger me."
                    elif StormX.favorite_action == "blowjob":
                        ch_s "I enjoy the taste of your cock."
                    elif StormX.favorite_action == "titjob":
                        ch_s "When I use my breasts."
                    elif StormX.favorite_action == "footjob":
                        ch_s "Footjobs are quite fun."
                    elif StormX.favorite_action == "handjob":
                        ch_s "I enjoy jerking you off."
                    elif StormX.favorite_action == "hotdog":
                        ch_s "When you grind against me."
                    elif StormX.favorite_action == "suck_breasts":
                        ch_s "When you suck my breasts."
                    elif StormX.favorite_action == "fondle_breasts":
                        ch_s "When you grab my breasts."
                    elif StormX.favorite_action == "fondle_thighs":
                        ch_s "When you rub my thighs."
                    else:
                        ch_s "I'm unsure, actually."



            "Don't talk as much during sex." if "vocal" in StormX.traits:
                if "setvocal" in StormX.daily_history:
                    $ StormX.change_face("perplexed")
                    ch_s "I do wish you would make up your mind."
                else:
                    if approval_check(StormX, 1000) and StormX.obedience <= StormX.love:
                        $ StormX.change_face("bemused")
                        call change_Girl_stat(StormX, "obedience", 1)
                        ch_s "I can be silent if you wish."
                        $ StormX.traits.remove("vocal")
                    elif approval_check(StormX, 700, "O"):
                        $ StormX.change_face("sadside")
                        call change_Girl_stat(StormX, "obedience", 1)
                        ch_s ". . ."
                        $ StormX.traits.remove("vocal")
                    elif approval_check(StormX, 600):
                        $ StormX.change_face("sly")
                        call change_Girl_stat(StormX, "love", -3)
                        call change_Girl_stat(StormX, "obedience", -1)
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s "Do not presume to control me, [StormX.player_petname]."
                    else:
                        $ StormX.change_face("angry")
                        call change_Girl_stat(StormX, "love", -5)
                        call change_Girl_stat(StormX, "obedience", -3)
                        call change_Girl_stat(StormX, "inhibition", 10)
                        ch_s "I do not take orders from you, [StormX.player_petname]."

                    $ StormX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in StormX.traits:
                if "setvocal" in StormX.daily_history:
                    $ StormX.change_face("perplexed")
                    ch_s "I do wish you would make up your mind."
                else:
                    if approval_check(StormX, 1000) and StormX.obedience <= StormX.love:
                        $ StormX.change_face("sly")
                        call change_Girl_stat(StormX, "obedience", 2)
                        ch_s "I believe I can make myself known. . ."
                        $ StormX.traits.append("vocal")
                    elif approval_check(StormX, 700, "O"):
                        $ StormX.change_face("sadside")
                        call change_Girl_stat(StormX, "obedience", 2)
                        ch_s "If that is what you want, [StormX.player_petname]."
                        $ StormX.traits.append("vocal")
                    elif approval_check(StormX, 600):
                        $ StormX.change_face("sly")
                        call change_Girl_stat(StormX, "obedience", 3)
                        ch_s "I suppose that I could. . ."
                        $ StormX.traits.append("vocal")
                    else:
                        $ StormX.change_face("angry")
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s ". . . I would rather not."

                    $ StormX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in StormX.traits:
                if "initiative" in StormX.daily_history:
                    $ StormX.change_face("perplexed")
                    ch_s "I do wish you would make up your mind."
                else:
                    if approval_check(StormX, 1200) and StormX.obedience <= StormX.love:
                        $ StormX.change_face("bemused")
                        call change_Girl_stat(StormX, "obedience", 1)
                        ch_s "Allow you to take the lead? Fine."
                        $ StormX.traits.append("passive")
                    elif approval_check(StormX, 700, "O"):
                        $ StormX.change_face("sadside")
                        call change_Girl_stat(StormX, "obedience", 1)
                        ch_s "I will try to restrain myself."
                        $ StormX.traits.append("passive")
                    elif approval_check(StormX, 600):
                        $ StormX.change_face("sly")
                        call change_Girl_stat(StormX, "love", -3)
                        call change_Girl_stat(StormX, "obedience", -1)
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s "We shall see."
                    else:
                        $ StormX.change_face("angry")
                        call change_Girl_stat(StormX, "love", -5)
                        call change_Girl_stat(StormX, "obedience", -3)
                        call change_Girl_stat(StormX, "inhibition", 10)
                        ch_s "I don't think that I shall."

                    $ StormX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in StormX.traits:
                if "initiative" in StormX.daily_history:
                    $ StormX.change_face("perplexed")
                    ch_s "I do wish you would make up your mind."
                else:
                    if approval_check(StormX, 1000) and StormX.obedience <= StormX.love:
                        $ StormX.change_face("bemused")
                        call change_Girl_stat(StormX, "obedience", 1)
                        ch_s "You would prefer I choose? Very Well."
                        $ StormX.traits.remove("passive")
                    elif approval_check(StormX, 700, "O"):
                        $ StormX.change_face("sadside")
                        call change_Girl_stat(StormX, "obedience", 1)
                        ch_s "If you insist."
                        $ StormX.traits.remove("passive")
                    elif approval_check(StormX, 600):
                        $ StormX.change_face("sly")
                        call change_Girl_stat(StormX, "obedience", 3)
                        ch_s "We shall see."
                        $ StormX.traits.remove("passive")
                    else:
                        $ StormX.change_face("angry")
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s "I would rather not."

                    $ StormX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in StormX.history:
                call Storm_Jumped
            "About when you masturbate":
                call NoFap (StormX)

            "Never mind" if line == "Yes? What did you want to discuss?":
                return
            "That's all." if line != "Yes? What did you want to discuss?":
                return
        if line == "Yes? What did you want to discuss?":
            $ line = "Anything else?"
    return




label Storm_Chitchat(O=0, Options = ["default", "default", "default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:

        if StormX not in Player.Phonebook:
            if approval_check(StormX, 500, "L") or approval_check(StormX, 250, "I"):
                ch_s "Oh, here's my number, in case you need back-up."
                $ Player.Phonebook.append(StormX)
                return
            elif approval_check(StormX, 250, "O"):
                ch_s "If you need to contact me, here's my number."
                $ Player.Phonebook.append(StormX)
                return

        if "hungry" not in StormX.traits and (StormX.permanent_History["swallowed"] + StormX.had_chat[2]) >= 10 and StormX.location == Player.location:
            call Storm_Hungry
            return

        if Player.location != "bg_restaurant" and Player.location != "bg_halloween" and (not taboo or approval_check(StormX, 800, "I")):
            if StormX.location == Player.location and StormX.thirst >= 30 and "refused" not in StormX.daily_history and "quicksex" not in StormX.daily_history:
                $ StormX.change_face("sly", 1)
                ch_s "I was wondering if you wanted to. . ."
                ch_s "\"get intimate\" with me?"
                call Quick_Sex (StormX)
                return




        if StormX.event_happened[0] and "key" not in StormX.had_chat:
            $ Options.append("key")

        if "mandrill" in Player.traits and "cologne chat" not in StormX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in StormX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in StormX.daily_history:
            $ Options.append("corruption")

        if StormX.went_on_date >= 1 and Player.location != "bg_restaurant":

            $ Options.append("dated")



        if StormX.permanent_History["kiss"] >= 5:

            $ Options.append("kissed")
        if "dangerroom" in Player.daily_history:

            $ Options.append("dangerroom")


            $ Options.append("showercaught")
        if "fondle_breasts" in StormX.daily_history or "fondle_pussy" in StormX.daily_history or "fondle_ass" in StormX.daily_history:

            $ Options.append("fondled")
        if "Dazzler and Longshot" in StormX.inventory and "256 Shades of Grey" in StormX.inventory and "Avengers Tower Penthouse" in StormX.inventory:

            if "book" not in StormX.had_chat:
                $ Options.append("booked")
        if "lace_bra" in StormX.inventory or "lace_panties" in StormX.inventory:

            if "lingerie" not in StormX.had_chat:
                $ Options.append("lingerie")
        if StormX.permanent_History["handjob"]:

            $ Options.append("handy")
        if StormX.permanent_History["swallowed"]:

            $ Options.append("swallowed")
        if "cleaned" in StormX.daily_history or "painted" in StormX.daily_history:

            $ Options.append("facial")
        if StormX.permanent_History["sleepover"]:

            $ Options.append("sleepwear")
        if StormX.permanent_History["creampied"] or StormX.permanent_History["anal_creampied"]:

            $ Options.append("creampie")
        if StormX.permanent_History["sex"] or StormX.permanent_History["anal"]:

            $ Options.append("sexed")
        if StormX.permanent_History["anal"]:

            $ Options.append("anal")

        if "seenpeen" in StormX.history:
            $ Options.append("seenpeen")
        if "nudity" not in StormX.history:
            $ Options.append("nudity")























        if not approval_check(StormX, 300):
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)

    if Options[0] == "mandrill":
        $ StormX.daily_history.append("cologne chat")
        $ StormX.change_face("confused")
        ch_s "(sniff, sniff). . . I can smell. . . some type of ape . . ."
        $ StormX.change_face("sexy", 2)
        ch_s ". . . you are looking quite fetching though. . ."
    elif Options[0] == "purple":
        $ StormX.daily_history.append("cologne chat")
        $ StormX.change_face("sly", 1)
        ch_s "(sniff, sniff). . . what is that odor? . ."
        $ StormX.change_face("normal", 0)
        ch_s ". . . was there anything that you wanted?"
    elif Options[0] == "corruption":
        $ StormX.daily_history.append("cologne chat")
        $ StormX.change_face("confused")
        ch_s "(sniff, sniff). . . that's a strong odor. . ."
        $ StormX.change_face("angry")
        ch_s ". . . I'm feeling quite dangerous. . ."
        $ StormX.change_face("sly")

    elif Options[0] == "caught":
        if "caught chat" in StormX.had_chat:
            ch_s "We should be more careful where we're seen together. . ."
            if not approval_check(StormX, 500, "I"):
                ch_s "Not that this should stop us. . ."
        else:
            ch_s "I am sorry for that unforunate business with Charles."
            if not approval_check(StormX, 500, "I"):
                ch_s "I suppose we should avoid activities in public."
            else:
                ch_s "I did enjoy the thrill though. . ."
            $ StormX.had_chat.append("caught chat")
    elif Options[0] == "key":
        if StormX.SEXP <= 15:
            ch_s "I gave you that key for convenience, do not abuse it . ."
        else:
            ch_s "I gave you a key, but you never come up to visit me. . ."
        $ StormX.had_chat.append("key")










    elif Options[0] == "dated":

        ch_s "I enjoyed our date, we should definitely do that again sometime."

    elif Options[0] == "kissed":

        $ StormX.change_face("normal", 1)
        ch_s "You know, [StormX.player_petname], you are a quite good kisser."
        menu:
            extend ""
            "Hey. . .I'm the best there is at what I do.":
                $ StormX.change_face("bemused", 1, eyes = "leftside")
                ch_s "Well, one of the best, perhaps."
                $ StormX.change_face("smile", 1)
                ch_s "But we'll get you there. . ."
            "No. You think?":
                ch_s "I'm quie certain. . ."
                ch_s "But we could experiment. . ."

    elif Options[0] == "dangerroom":

        $ StormX.change_face("sly", 1)
        ch_s "Hey,[StormX.player_petname]. I saw your work in the Danger Room."
        ch_s "You might want to stay close to a \"tank\" to avoid damage. . ."
    elif Options[0] == "nudity":

        ch_p "I've noticed you walk around naked more than the others."
        call Storm_Nudity
















































    elif Options[0] == "fondled":

        if StormX.permanent_History["fondle_breasts"]+ StormX.permanent_History["fondle_pussy"] + StormX.permanent_History["fondle_ass"] >= 15:
            ch_s "Please touch me. . . sometime. . ."
        else:
            ch_s "You know, you could touch me. . . if you wanted."

    elif Options[0] == "booked":

        ch_s "I read those books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ StormX.change_face("sly", 2)
                ch_s "They were. . .{i}interesting{/i}."
            "Good. You looked like you could use to learn a thing or two from them.":
                call change_Girl_stat(StormX, "love", -3)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", 5)
                $ StormX.change_face("angry")
                ch_s "Well, I cannot say they I din't learn a thing or so."
        $ StormX.blushing = "_blush1"
        $ StormX.had_chat.append("book")

    elif Options[0] == "lingerie":

        $ StormX.change_face("sly", 2)
        ch_s "I have enjoyed that lingerie you purchased for me."
        $ StormX.blushing = "_blush1"
        $ StormX.had_chat.append("lingerie")

    elif Options[0] == "handy":

        $ StormX.change_face("sly", 1)
        ch_s "I was thinking about having your cock in my hand the other day. . ."
        ch_s "Were you?"
        $ StormX.blushing = ""

    elif Options[0] == "blowjob":
        if "blowjob" not in StormX.had_chat:

            $ StormX.change_face("sly", 2)
            ch_s "I was curious, did you enjoy that blowjob earlier?"
            menu:
                extend ""
                "You were totally amazing.":
                    call change_Girl_stat(StormX, "love", 5)
                    call change_Girl_stat(StormX, "inhibition", 10)
                    $ StormX.change_face("normal", 1)
                    ch_s ". . . "
                    $ StormX.change_face("sexy", 1)
                    ch_s "As I had hoped. . ."
                    ch_s "Let me know if you're like a repeat. . ."
                "Honestly? It was good. . .but you could use a little practice, I think.":
                    if approval_check(StormX, 300, "I") or not approval_check(StormX, 800):
                        call change_Girl_stat(StormX, "love", -5)
                        call change_Girl_stat(StormX, "obedience", 10)
                        call change_Girl_stat(StormX, "inhibition", 10)
                        $ StormX.change_face("perplexed", 1)
                        ch_s "Oh? Well I am sorry I was not up to your usual standards. . ."
                    else:
                        call change_Girl_stat(StormX, "obedience", 15)
                        call change_Girl_stat(StormX, "inhibition", 5)
                        $ StormX.change_face("sexy", 1)
                        ch_s "Oh? I'm certain that I can improve on the experience. . ."
                "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":
                    call change_Girl_stat(StormX, "love", -10)
                    call change_Girl_stat(StormX, "obedience", 10)
                    $ StormX.change_face("angry", 2)
                    ch_s "Oh, then I suppose you will not miss it."
            $ StormX.blushing = "_blush1"
            $ StormX.had_chat.append("blowjob")
        else:
            $ line = renpy.random.choice(["You know, I really do enjoy the taste of your cock.",
                            "I think I nearly dislocated my jaw last time.",
                            "Let me know if you would enjoy another blowjob.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_s "[line]"

    elif Options[0] == "swallowed":

        if "swallow" in StormX.had_chat:
            ch_s "I would like to taste you again sometime."
        else:
            ch_s "So. . . the other day. . ."
            ch_s "I really enjoyed the taste of your semen."
            $ StormX.change_face("sly", 1)
            ch_s "Fairly surpirsing, all things considered."
            $ StormX.had_chat.append("swallow")

    elif Options[0] == "facial":

        ch_s ". . .I know this is a bit unusual, but. . ."
        $ StormX.change_face("sexy", 2)
        ch_s "I do so enjoy when you cum on my face. . ."
        $ StormX.blushing = "_blush1"

    elif Options[0] == "sleepover":

        ch_s "I really enjoyed the other night."
        ch_s "I don't often get to sleep with someone else around. . ."

    elif Options[0] == "creampie":

        "[StormX.name] draws close to you so she can whisper into your ear."
        ch_s "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":

        ch_s "So. . . you should know. . ."
        $ StormX.change_face("sexy", 2)
        ch_s ". . .when I. . . care for my own needs. . ."
        ch_s "It is you that I imagine with me. . ."
        $ StormX.blushing = "_blush1"

    elif Options[0] == "anal":

        $ StormX.change_face("sly")
        ch_s "I never much cared for anal sex."
        $ StormX.change_face("sexy", 1)
        ch_s ". . . but you have turned me around on the idea."

    elif Options[0] == "seenpeen":
        $ StormX.change_face("sly", 1, eyes = "leftside")
        ch_s "Oh, just so you are aware, I was impressed by your. . ."
        $ StormX.change_face("sly", 2, eyes = "down")
        ch_s ". . . manhood. . ."
        $ StormX.change_face("bemused", 1)
        call change_Girl_stat(StormX, "love", 5)
        $ StormX.history.remove("seenpeen")

























    elif Options[0] == "hate":
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want you in my sight.",
                "Stay away.",
                "Leave me."])
        ch_s "[line]"
    else:




































































        $ StormX.change_face("smile")
        ch_s "I do enjoy being with you. . ."

    $ line = 0
    return


label Storm_names:
    menu:
        ch_s "Oh? What would you prefer I call you?"
        "My initial's fine.":
            $ StormX.player_petname = Player.name[:1]
            ch_s "You got it, [StormX.player_petname]."
        "Call me by my name.":
            $ StormX.player_petname = Player.name
            ch_s "If you'd rather, [StormX.player_petname]."
        "Call me \"boyfriend\"." if "boyfriend" in StormX.player_petnames:
            $ StormX.player_petname = "boyfriend"
            ch_s "Very well, [StormX.player_petname]."
        "Call me \"lover\"." if "lover" in StormX.player_petnames:
            $ StormX.player_petname = "lover"
            ch_s "I would love to, [StormX.player_petname]."
        "Call me \"beloved\"." if "lover" in StormX.player_petnames:
            $ StormX.player_petname = "beloved"
            ch_s "I would love to, [StormX.player_petname]."
        "Call me \"sir\"." if "sir" in StormX.player_petnames:
            $ StormX.player_petname = "sir"
            ch_s "Yes, [StormX.player_petname]."
        "Call me \"master\"." if "master" in StormX.player_petnames:
            $ StormX.player_petname = "master"
            ch_s "As you wish, [StormX.player_petname]."
        "Call me \"sex friend\"." if "sex friend" in StormX.player_petnames:
            $ StormX.player_petname = "sex friend"
            ch_s "Quite cheeky, [StormX.player_petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in StormX.player_petnames:
            $ StormX.player_petname = "fuck buddy"
            ch_s "Fine, [StormX.player_petname]."
        "Call me \"daddy\"." if "daddy" in StormX.player_petnames:
            $ StormX.player_petname = "daddy"
            ch_s "Ok, [StormX.player_petname]."
        "Nevermind.":
            return
    return


label Storm_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    "I think I'll call you. . ."
                    "Ororo.":
                        $ StormX.petname = "Ororo"
                        ch_s "I don't see why not, [StormX.player_petname]."
                    "Storm.":
                        $ StormX.petname = "Storm"
                        ch_s "I don't see why not, [StormX.player_petname]."
                    "Stormy.":
                        $ StormX.petname = "Stormy"
                        if approval_check(StormX, 600):
                            $ StormX.change_face("smile", 1)
                            ch_s "I don't see why not, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("normal", 1)
                            ch_s "I would rather you weren't so familiar, [StormX.player_petname]."
                    "'Ro.":
                        $ StormX.petname = "'Ro"
                        if approval_check(StormX, 700):
                            $ StormX.change_face("smile", 1)
                            ch_s "I don't see why not, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("normal", 1)
                            ch_s "I would rather you weren't so familiar, [StormX.player_petname]."

                    "Ms. Munroe." if "Ms. Munroe" in StormX.names:
                        $ StormX.petname = "Ms. Munroe"
                        if approval_check(StormX, 700):
                            $ StormX.change_face("bemused", 1)
                            ch_s "I don't see why not, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("normal", 1)
                            ch_s "That would be a bit much, [StormX.player_petname]."
                    "\"girl\".":


                        $ StormX.petname = "girl"
                        if "boyfriend" in StormX.player_petnames or approval_check(StormX, 600, "L"):
                            $ StormX.change_face("sexy", 1)
                            ch_s "I can be your girl, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry")
                            ch_s "I'm NOT your girl, [StormX.player_petname]."
                    "\"boo\".":

                        $ StormX.petname = "boo"
                        if "boyfriend" in StormX.player_petnames or approval_check(StormX, 700, "L"):
                            $ StormX.change_face("sexy", 1)
                            ch_s "I can be your boo, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry")
                            ch_s "I'm NOT your boo, [StormX.player_petname]."
                    "\"bae\".":

                        $ StormX.petname = "bae"
                        if "boyfriend" in StormX.player_petnames or approval_check(StormX, 600, "L"):
                            $ StormX.change_face("sexy", 1)
                            ch_s "I can be your bae, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry")
                            ch_s "I'm NOT your bae, [StormX.player_petname]."
                    "\"baby\".":

                        $ StormX.petname = "baby"
                        if "boyfriend" in StormX.player_petnames or approval_check(StormX, 500, "L"):
                            $ StormX.change_face("sexy", 1)
                            ch_s "Cute, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry")
                            ch_s "I am not your baby."
                    "\"sweetie\".":


                        $ StormX.petname = "sweetie"
                        if "boyfriend" in StormX.player_petnames or approval_check(StormX, 600, "L"):
                            ch_s "That is so sweet, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "Perhaps too sweet, [StormX.player_petname]."
                    "\"sexy\".":

                        $ StormX.petname = "sexy"
                        if "lover" in StormX.player_petnames or approval_check(StormX, 800):
                            $ StormX.change_face("sexy", 1)
                            ch_s "I suppose that I am, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "Crossing a line there, [StormX.player_petname]."
                    "\"lover\".":

                        $ StormX.petname = "lover"
                        if "lover" in StormX.player_petnames or approval_check(StormX, 1200):
                            $ StormX.change_face("sexy", 1)
                            ch_s "I am, I suppose."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "I do not think so, [StormX.player_petname]."
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you. . ."
                    "\"slave\".":
                        $ StormX.petname = "slave"
                        if "master" in StormX.player_petnames or approval_check(StormX, 850, "O"):
                            $ StormX.change_face("bemused", 1)
                            ch_s "As you wish, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "I am no one's slave, [StormX.player_petname]."
                    "\"pet\".":

                        $ StormX.petname = "pet"
                        if "master" in StormX.player_petnames or approval_check(StormX, 700, "O"):
                            $ StormX.change_face("bemused", 1)
                            ch_s "You can pet me if you want, [StormX.player_petname]."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "I am no one's pet, [StormX.player_petname]."
                    "\"slut\".":

                        $ StormX.petname = "slut"
                        if "sex friend" in StormX.player_petnames or approval_check(StormX, 900, "OI"):
                            $ StormX.change_face("sexy")
                            ch_s "Fair enough."
                        else:
                            $ StormX.change_face("angry", 1)
                            $ StormX.mouth = "surprised"
                            ch_s "You would do well to avoid that."
                    "\"whore\".":

                        $ StormX.petname = "whore"
                        if "fuckbuddy" in StormX.player_petnames or approval_check(StormX, 1000, "OI"):
                            $ StormX.change_face("sly")
                            ch_s ". . ."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "Do not tempt me to harm you. . ."
                    "\"sugartits\".":

                        $ StormX.petname = "sugartits"
                        if "sex friend" in StormX.player_petnames or approval_check(StormX, 1400):
                            $ StormX.change_face("sly", 1)
                            ch_s "I suppose. . ."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "Why would you even-."
                    "\"sex friend\".":

                        $ StormX.petname = "sex friend"
                        if "sex friend" in StormX.player_petnames or approval_check(StormX, 600, "I"):
                            $ StormX.change_face("sly")
                            ch_s "Yes. . ."
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "Keep it quiet, [StormX.player_petname]."
                    "\"fuckbuddy\".":

                        $ StormX.petname = "fuckbuddy"
                        if "fuckbuddy" in StormX.player_petnames or approval_check(StormX, 700, "I"):
                            $ StormX.change_face("sly")
                            ch_s "Sure."
                        else:
                            $ StormX.change_face("angry", 1)
                            $ StormX.mouth = "surprised"
                            ch_s "That is not even funny, [StormX.player_petname]."
                    "\"baby girl\".":

                        $ StormX.petname = "baby girl"
                        if "daddy" in StormX.player_petnames or approval_check(StormX, 1200):
                            $ StormX.change_face("smile", 1)
                            ch_s "I suppose?"
                        else:
                            $ StormX.change_face("angry", 1)
                            ch_s "How odd. . ."
                    "Back":

                        pass
            "Nevermind.":

                return
    return





label Storm_Rename:

    $ StormX.mouth = "smile"
    ch_s "Yeah?"
    menu:
        extend ""
        "I think \"Storm's\" a cool name." if StormX.name != "Storm" and "Storm" in StormX.names:
            $ StormX.name = "Storm"
            ch_s "Sounds good."
        "I think \"Ororo's\" a pretty name." if StormX.name != "Ororo" and "Ororo" in StormX.names:
            $ StormX.name = "Ororo"
            ch_s "Sounds good."
        "I think \"Ms. Munroe's\" a pretty name." if StormX.name != "Ms. Munroe" and "Ms. Munroe" in StormX.names:
            $ StormX.name = "Ms. Munroe"
            ch_s "Sounds good."
        "Nevermind.":
            pass
    $ StormX.add_word(1, 0, "namechange")
    return




label Storm_Personality(counter=0):
    if not StormX.had_chat[4] or counter:
        "Since you're doing well in one area, you can convince Storm to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_s "Yes? What was it you wanted?"
        "More Obedient. [[Love to Obedience]" if StormX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_s "I suppose that I could try."
            $ StormX.had_chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if StormX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_s "I can try to be more open."
            $ StormX.had_chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if StormX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_s "I can try to be more open."
            $ StormX.had_chat[4] = 3
        "More Loving. [[Obedience to Love]" if StormX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_s "I can try."
            $ StormX.had_chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if StormX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_s "I suppose that I could try."
            $ StormX.had_chat[4] = 5

        "More Loving. [[Inhibition to Love]" if StormX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_s "I will try."
            $ StormX.had_chat[4] = 6

        "I guess just do what you like. . .[[reset]" if StormX.had_chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_s ". . . very well."
            $ StormX.had_chat[4] = 0
        "Repeat the rules":
            call Storm_Personality (1)
            return
        "Nevermind.":
            return
    return







    label Storm_NoPantiesOn:
        menu:
            ch_s "I am not wearing panties today."
            "Then you could slip on a pair of panties. . .":
                if StormX.taboo <= 20 or StormX.Clothes["hose"] in ["tights", "pantyhose"] or StormX in Rules:
                    ch_s "No, it's fine."
                elif StormX.seen_pussy and approval_check(StormX, 1100, taboo_modifier=4):
                    $ StormX.blushing = "_blush1"
                    ch_s "No, commando's fine. . ."
                    $ StormX.blushing = ""




                elif approval_check(StormX, 700, taboo_modifier=4):
                    ch_s "Fine."
                    if "lace_panties" in StormX.inventory:
                        $ StormX.Clothes["underwear"]  = "lace_panties"
                    else:
                        $ StormX.Clothes["underwear"] = "black_panties"
                    if approval_check(StormX, 1200, taboo_modifier=4):
                        $ line = StormX.Clothes["bottom"]
                        $ StormX.Outfit.remove_Clothing(["pants", "skirt"])
                        "She pulls off her [line] and slips on the [StormX.Clothes[underwear].name]."
                    elif StormX.Clothes["bottom"] == "skirt":
                        "She pulls out her [StormX.Clothes[underwear].name] and pulls them up under her skirt."
                        $ StormX.Outfit.remove_Clothing(["pants", "skirt"])
                        "Then she drops the skirt to the floor."
                    else:
                        $ line = StormX.Clothes["bottom"]
                        $ StormX.Outfit.remove_Clothing(["pants", "skirt"])
                        "She steps away a moment and then comes back wearing only the [StormX.Clothes[underwear].name]."
                    return
                else:
                    ch_s "No, thank you."
                    return False
            "You could always just wear nothing at all. . .":

                if StormX.taboo <= 20 or StormX.Clothes["hose"] in ["tights", "pantyhose"] or StormX in Rules:
                    ch_s "True."
                elif approval_check(StormX, 1100, "LI", taboo_modifier = 3) and StormX.love > StormX.inhibition:
                    ch_s "True. . ."
                elif approval_check(StormX, 700, "OI", taboo_modifier = 3) and StormX.obedience > StormX.inhibition:
                    ch_s "Yes. . ."
                elif approval_check(StormX, 600, "I", taboo_modifier = 3):
                    ch_s "Hrmm. . ."
                elif approval_check(StormX, 1300, taboo_modifier = 3):
                    ch_s "Fine."
                else:
                    $ StormX.change_face("bemused")
                    if StormX.taboo > 20:
                        ch_s "Obviously, but not in public, [StormX.player_petname]."
                    else:
                        ch_s "I'm afraid not, [StormX.player_petname]!"
                    return False
            "Never mind.":

                ch_s "Ok. . ."
                return False
        return True




    menu Storm_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [StormX.Clothes[bra].name]?" if StormX.Clothes["bra"]:
                    $ StormX.change_face("bemused", 1)

                    if StormX.taboo <= 20 or StormX in Rules or StormX.top_number() >= 5:
                        ch_s "Fine."
                    elif StormX.seen_breasts and approval_check(StormX, 900, taboo_modifier=2.7):
                        ch_s "Fine."





                    elif StormX.Clothes["jacket"] == "jacket" and approval_check(StormX, 600, taboo_modifier=2):
                        ch_s "This jacket is a bit revealing. . ."


                    elif not StormX.Clothes["top"]:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "I'd have to wear something else over it."
                            return
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "I'm afraid not."
                            return
                    $ line = StormX.Clothes["bra"]
                    $ StormX.take_off("bra")
                    if StormX.Clothes["top"]:
                        "She reaches under her [StormX.Clothes[top].name] grabs her [line], and pulls it off, dropping it to the ground."
                    else:
                        "She pulls off her [line] and drops it to the ground."
                        if not renpy.showing('dress_screen'):
                            call Storm_First_Topless


                "Try on that tube top." if StormX.Clothes["bra"] != "tube_top":
                    ch_s "Fine."
                    $ StormX.Clothes["bra"] = "tube_top"

                "Try on that sports bra." if StormX.Clothes["bra"] != "sports_bra":
                    ch_s "Fine."
                    $ StormX.Clothes["bra"] = "sports_bra"

                "I like that black bra." if StormX.Clothes["bra"] != "black_bra":
                    if StormX.taboo <= 20 or StormX in Rules or StormX.top_number() >= 5:
                        ch_s "Fine."
                        $ StormX.Clothes["bra"] = "black_bra"
                    elif StormX.seen_breasts or approval_check(StormX, 1100, taboo_modifier=2):
                        ch_s "Fine."
                        $ StormX.Clothes["bra"] = "black_bra"
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "It's a bit minimal. . ."
                        else:
                            $ StormX.Clothes["bra"] = "black_bra"

                "I like that lace bra." if StormX.Clothes["bra"] != "lace_bra" and "lace_bra" in StormX.inventory:
                    if StormX.taboo <= 20 or StormX in Rules or StormX.top_number() >= 5:
                        ch_s "Fine."
                        $ StormX.Clothes["bra"] = "lace_bra"
                    elif StormX.seen_breasts or approval_check(StormX, 1300, taboo_modifier=2):
                        ch_s "Fine."
                        $ StormX.Clothes["bra"] = "lace_bra"
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "It's a bit sheer. . ."
                        else:
                            $ StormX.Clothes["bra"] = "lace_bra"

                "I like that bikini top." if StormX.Clothes["bra"] != "bikini_top" and "bikini_top" in StormX.inventory:
                    if Player.location == "bg_pool":
                        ch_s "Fine."
                        $ StormX.Clothes["bra"] = "bikini_top"
                    else:
                        if StormX.taboo <= 20 or StormX in Rules or StormX.top_number() >= 5:
                            ch_s "Fine."
                            $ StormX.Clothes["bra"] = "bikini_top"
                        elif StormX.seen_breasts or approval_check(StormX, 1000, taboo_modifier=2):
                            ch_s "Fine."
                            $ StormX.Clothes["bra"] = "bikini_top"
                        else:
                            call ask_for_dress_screen (StormX)
                            if not _return:
                                ch_s "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ StormX.Clothes["bra"] = "bikini_top"

                "I like that top you had at the party." if StormX.Clothes["bra"] != "cosplay_bra" and "halloween" in StormX.history:
                    if StormX.taboo <= 20 or StormX in Rules or StormX.top_number() >= 5:
                        ch_s "Fine."
                        $ StormX.Clothes["bra"] = "cosplay_bra"
                    elif StormX.seen_breasts or approval_check(StormX, 1100, taboo_modifier=2):
                        ch_s "Fine."
                        $ StormX.Clothes["bra"] = "cosplay_bra"
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "It's a bit minimal. . ."
                        else:
                            $ StormX.Clothes["bra"] = "cosplay_bra"
                "Never mind":

                    pass
            return
        "Hose and stockings options":

            menu:
                "You could lose the hose." if StormX.Clothes["hose"] and StormX.Clothes["hose"] != 'ripped_tights' and StormX.Clothes["hose"] != '_tights':
                    $ StormX.take_off("hose")
                "The thigh-high hose would look good with that." if StormX.Clothes["hose"] != "stockings":
                    $ StormX.Clothes["hose"] = "stockings"
                "The pantyhose would look good with that." if StormX.Clothes["hose"] != "pantyhose":
                    $ StormX.Clothes["hose"] = "pantyhose"
                "The ripped pantyhose would look good with that." if StormX.Clothes["hose"] != "ripped_pantyhose" and "ripped_pantyhose" in StormX.inventory:
                    $ StormX.Clothes["hose"] = "ripped_pantyhose"
                "The stockings and garterbelt would look good with that." if StormX.Clothes["hose"] != "stockings_and_garterbelt" and "stockings_and_garterbelt" in StormX.inventory:
                    $ StormX.Clothes["hose"] = "stockings_and_garterbelt"
                "Just the garterbelt would look good with that." if StormX.Clothes["hose"] != "garterbelt" and "stockings_and_garterbelt" in StormX.inventory:
                    $ StormX.Clothes["hose"] = "garterbelt"
                "Never mind":
                    pass
            return
        "Panties":


            menu:
                "You could lose those panties. . ." if StormX.Clothes["underwear"]:
                    $ StormX.change_face("bemused", 1)
                    if StormX.taboo <= 20 or StormX.Clothes["hose"] in ["tights", "pantyhose"] or StormX.bottom_number() >= 5 or StormX in Rules:
                        ch_s "Sure."
                    else:










                        if approval_check(StormX, 1100, "LI", taboo_modifier = 3) and StormX.love > StormX.inhibition:
                            ch_s "I suppose I could, but. . ."
                        elif approval_check(StormX, 700, "OI", taboo_modifier = 3) and StormX.obedience > StormX.inhibition:
                            ch_s "Well. . ."
                        elif approval_check(StormX, 600, "I", taboo_modifier = 3):
                            ch_s "Hrmm. . ."
                        elif approval_check(StormX, 1300, taboo_modifier = 3):
                            ch_s "Okay, okay."
                        else:
                            call ask_for_dress_screen (StormX)
                            if not _return:
                                $ StormX.change_face("bemused")
                                if StormX.taboo >= 20:
                                    ch_s "Obviously, but not in public, [StormX.player_petname]."
                                else:
                                    ch_s "I'm afraid not, [StormX.player_petname]!"
                                return
                    $ line = StormX.Clothes["underwear"]
                    $ StormX.take_off("underwear")
                    if not StormX.Clothes["bottom"]:
                        "She pulls off her [line], then drops them to the ground."
                        if not renpy.showing('dress_screen'):
                            call Storm_First_Bottomless
                    elif approval_check(StormX, 1200, taboo_modifier=4):
                        $ temp_bottom = StormX.Clothes["bottom"]
                        $ StormX.Outfit.remove_Clothing(["pants", "skirt"])
                        pause 0.5
                        $ StormX.Clothes["bottom"] = temp_bottom
                        "She pulls off her [StormX.Clothes[bottom]] and [line], then pulls the [StormX.Clothes[bottom].name] back on."
                        call Storm_First_Bottomless (1)
                    elif StormX.Clothes["bottom"] == "skirt":
                        "She reaches under her skirt and pulls her [line] off."
                    else:
                        $ StormX.blushing = "_blush1"
                        "She steps away a moment and then comes back."
                        $ StormX.blushing = ""
                    $ line = 0

                "Why don't you wear the white panties instead?" if StormX.Clothes["underwear"] and StormX.Clothes["underwear"] != "white_panties":
                    if StormX.taboo <= 20 or StormX in Rules or StormX.bottom_number() >= 5:
                        ch_s "Fine."
                        $ StormX.Clothes["underwear"] = "white_panties"
                    elif approval_check(StormX, 1100, taboo_modifier = 3):
                        ch_s "Ok."
                        $ StormX.Clothes["underwear"] = "white_panties"
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "That's really none of your busines."
                        else:
                            $ StormX.Clothes["underwear"] = "white_panties"

                "Why don't you wear the black panties instead?" if StormX.Clothes["underwear"] and StormX.Clothes["underwear"] != "black_panties":
                    if StormX.taboo <= 20 or StormX in Rules or StormX.bottom_number() >= 5:
                        ch_s "Fine."
                        $ StormX.Clothes["underwear"] = "black_panties"
                    elif approval_check(StormX, 1100, taboo_modifier = 3):
                        ch_s "Ok."
                        $ StormX.Clothes["underwear"] = "black_panties"
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "That's really none of your busines."
                        else:
                            $ StormX.Clothes["underwear"] = "black_panties"

                "Why don't you wear the lace panties instead?" if "lace_panties" in StormX.inventory and StormX.Clothes["underwear"] and StormX.Clothes["underwear"] != "lace_panties":
                    if StormX.taboo <= 20 or StormX in Rules or StormX.bottom_number() >= 5:
                        ch_s "Fine."
                        $ StormX.Clothes["underwear"] = "lace_panties"
                    elif approval_check(StormX, 1300, taboo_modifier = 3):
                        ch_s "I guess."
                        $ StormX.Clothes["underwear"] = "lace_panties"
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "That's really none of your busines."
                        else:
                            $ StormX.Clothes["underwear"] = "lace_panties"

                "I like those bikini bottoms." if "bikini_bottoms" in StormX.inventory and StormX.Clothes["underwear"] != "bikini_bottoms":
                    if Player.location == "bg_pool":
                        ch_s "Fine."
                        $ StormX.Clothes["underwear"] = "bikini_bottoms"
                    else:
                        if StormX.taboo <= 20 or StormX in Rules or StormX.bottom_number() >= 5:
                            ch_s "Fine."
                            $ StormX.Clothes["underwear"] = "bikini_bottoms"
                        elif approval_check(StormX, 1000, taboo_modifier=2):
                            ch_s "Fine."
                            $ StormX.Clothes["underwear"] = "bikini_bottoms"
                        else:
                            call ask_for_dress_screen (StormX)
                            if not _return:
                                ch_s "This is not really a \"bikini\" sort of place. . ."
                            else:
                                $ StormX.Clothes["underwear"] = "bikini_bottoms"

                "Why don't you wear those panties from the party?" if StormX.Clothes["underwear"] and "halloween" in StormX.history and StormX.Clothes["underwear"] != "cosplay_panties":
                    if StormX.taboo <= 20 or StormX in Rules or StormX.bottom_number() >= 5:
                        ch_s "Fine."
                        $ StormX.Clothes["underwear"] = "cosplay_panties"
                    elif approval_check(StormX, 1100, taboo_modifier = 3):
                        ch_s "Ok."
                        $ StormX.Clothes["underwear"] = "cosplay_panties"
                    else:
                        call ask_for_dress_screen (StormX)
                        if not _return:
                            ch_s "That's really none of your busines."
                        else:
                            $ StormX.Clothes["underwear"] = "cosplay_panties"

                "You know, you could wear some panties with that. . ." if not StormX.Clothes["underwear"]:
                    $ StormX.change_face("bemused", 1)
                    if StormX.Clothes["bottom"] and (StormX.love+StormX.obedience) <= (2*StormX.inhibition):
                        $ StormX.mouth = "smile"
                        ch_s "I don't know about that."
                        menu:
                            "Fine by me":
                                return
                            "I insist, put some on.":
                                if (StormX.love+StormX.obedience) <= (1.5*StormX.inhibition):
                                    $ StormX.change_face("angry", eyes = "side")
                                    ch_s "Well I insist otherwise."
                                    return
                                else:
                                    $ StormX.change_face("sadside")
                                    ch_s "Oh, fine. . ."
                    else:
                        ch_s "Which?"
                    menu:
                        extend ""
                        "How about the white ones?":
                            ch_s "Fine."
                            $ StormX.Clothes["underwear"] = "white_panties"
                        "How about the black ones?":
                            ch_s "Fine."
                            $ StormX.Clothes["underwear"] = "black_panties"
                        "How about the lace ones?" if "lace_panties" in StormX.inventory:
                            ch_s "Fine."
                            $ StormX.Clothes["underwear"]  = "lace_panties"
                        "How about the bikini bottoms?" if "bikini_bottoms" in StormX.inventory:
                            ch_s "Fine."
                            $ StormX.Clothes["underwear"] = "bikini_bottoms"
                        "How about the costume ones?" if "halloween" in StormX.history:
                            ch_s "Fine."
                            $ StormX.Clothes["underwear"] = "cosplay_panties"
                "Never mind":
                    pass
            return
        "Never mind":
            pass
    return




    menu Storm_Clothes_Misc:

        "Long hair style" if StormX.Clothes["hair"] not in ["long", "wet_long"]:
            ch_p "You looked good with long hair."
            if "hair" in StormX.recent_history:
                ch_s "I have already messed with it too much today."
            elif approval_check(StormX, 900):
                ch_s "Oh, you did?"
                ch_s "I suppose I could speak to Hank about that. . ."
                show black_screen onlayer black
                $ round -5 if round >= 10 else 0
                "She steps away for a few minutes."
                hide black_screen onlayer black
                if StormX.Clothes["hair"] == "wet_mohawk":
                    $ StormX.Clothes["hair"] = "wet_long"
                else:
                    $ StormX.Clothes["hair"] = "long"
                $ StormX.add_word(1, "hair", "hair", 0, 0)
                ch_s "Like this?"
            else:
                ch_s "Thank you, but I'm not interested in that style right now."

        "Mohawk hair style" if "mohawk" in StormX.history and StormX.Clothes["hair"] not in ["mohawk", "wet_mohawk"]:
            ch_p "You looked good with a mohawk."
            if "hair" in StormX.recent_history:
                ch_s "I have already messed with it too much today."
            elif approval_check(StormX, 900):
                ch_s "You liked it?"
                show black_screen onlayer black
                $ round -5 if round >= 10 else 0
                "She steps away for a few minutes."
                hide black_screen onlayer black
                if StormX.Clothes["hair"] == "wet_long":
                    $ StormX.Clothes["hair"] = "wet_mohawk"
                else:
                    $ StormX.Clothes["hair"] = "mohawk"
                $ StormX.add_word(1, "hair", "hair", 0, 0)
                ch_s "Like this?"
            else:
                ch_s "Thank you, but I'm not interested in that style right now."

        "Short hair style" if StormX.Clothes["hair"] != "short" and "halloween" in StormX.history:
            ch_p "You looked good with short hair."
            if "hair" in StormX.recent_history:
                ch_s "I have already messed with it too much today."
            elif approval_check(StormX, 900):
                ch_s "Oh, you did?"
                ch_s "I suppose I could speak to Hank about that. . ."
                show black_screen onlayer black
                $ round -5 if round >= 10 else 0
                "She steps away for a few minutes."
                hide black_screen onlayer black
                $ StormX.Clothes["hair"] = "short"
                $ StormX.add_word(1, "hair", "hair", 0, 0)
                ch_s "Like this?"
            else:
                ch_s "Thank you, but I'm not interested in that style right now."

        "Wet look hairstyle" if StormX.Clothes["hair"] != "wet_long" and StormX.Clothes["hair"] != "wet_mohawk":
            ch_p "You should go for that wet look with your hair."
            if approval_check(StormX, 800):
                ch_s "Really?"
                if StormX.Clothes["hair"] == "mohawk":
                    $ StormX.Clothes["hair"] = "wet_mohawk"
                else:
                    $ StormX.Clothes["hair"] = "wet_long"
                "A concentrated hurricane swirls around her head for a moment, leaving her hair limp."
                ch_s "Like this?"
            else:
                ch_s "I'd rather not."

        "Dry out hair" if StormX.Clothes["hair"] == "wet_long" or StormX.Clothes["hair"] == "wet_mohawk":
            ch_p "Maybe dry out your hair."
            if approval_check(StormX, 600):
                ch_s "Fine."
                "A gust of wind swirls around her hair."
                if StormX.Clothes["hair"] == "wet_mohawk":
                    $ StormX.Clothes["hair"] = "mohawk"
                else:
                    $ StormX.Clothes["hair"] = "long"
            else:
                ch_s "I'm unsure, I think this is fine."

        "Grow pubes" if not StormX.pubes:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in StormX.to_do:
                $ StormX.change_face("bemused", 1)
                ch_s "It's not as though it grows instantly!"
            else:
                $ StormX.change_face("bemused", 1)
                if approval_check(StormX, 500, taboo_modifier=0):
                    ch_s "I do prefer it that way. . ."
                else:
                    $ StormX.change_face("surprised")
                    $ StormX.brows = "angry"
                    ch_s "I do not need your advice."
                    return
                $ StormX.to_do.append("pubes")
                $ StormX.pubes_counter = 6
        "Shave pubes" if StormX.pubes == "_hairy":
            ch_p "I like it waxed clean down there."
            $ StormX.change_face("bemused", 1)
            if "shave" in StormX.to_do:
                ch_s "Yes, I will get around to it."
            else:
                if approval_check(StormX, 1100, taboo_modifier=0):
                    ch_s "You do? I suppose I could shave. . ."
                else:
                    $ StormX.change_face("surprised")
                    $ StormX.brows = "angry"
                    ch_s "I think I will do what I want down there."
                    return
                $ StormX.to_do.append("shave")




        "Add Ring Piercings" if StormX.Clothes["piercings"] != "ring":
            ch_p "You know, you'd look really nice with some ring body piercings."
            if "ring" in StormX.to_do:
                ch_s "I know, I will do it."
            else:
                $ StormX.change_face("bemused", 1)
                $ approval = approval_check(StormX, 1150, taboo_modifier=0)
                if approval_check(StormX, 900, "L", taboo_modifier=0) or (approval and StormX.love > 2* StormX.obedience):
                    ch_s "You like the way they'd look on me?"
                elif approval_check(StormX, 600, "I", taboo_modifier=0) or (approval and StormX.inhibition > StormX.obedience):
                    ch_s "I have been considering that for a while."
                elif approval_check(StormX, 500, "O", taboo_modifier=0) or approval:
                    ch_s "Yes, [StormX.player_petname]."
                else:
                    $ StormX.change_face("bemused")
                    ch_s "I would rather not, [StormX.player_petname]."
                    return
                $ StormX.to_do.append("ring")

        "Add barbell piercings." if StormX.Clothes["piercings"] != "barbell":
            ch_p "You know, you'd look really nice with some barbell body piercings."
            if "barbell" in StormX.to_do:
                ch_s "I know, I will do it."
            else:
                $ StormX.change_face("bemused", 1)
                $ approval = approval_check(StormX, 1150, taboo_modifier=0)
                if approval_check(StormX, 900, "L", taboo_modifier=0) or (approval and StormX.love > 2*StormX.obedience):
                    ch_s "You like the way they'd look on me?"
                elif approval_check(StormX, 600, "I", taboo_modifier=0) or (approval and StormX.inhibition > StormX.obedience):
                    ch_s "I have been considering that for a while."
                elif approval_check(StormX, 500, "O", taboo_modifier=0) or approval:
                    ch_s "Yes, [StormX.player_petname]."
                else:
                    $ StormX.change_face("bemused")
                    ch_s "I would rather not, [StormX.player_petname]."
                    return
                $ StormX.to_do.append("barbell")

        "Remove Piercings" if StormX.Clothes["piercings"]:
            ch_p "You know, you'd look better without those piercings."
            $ StormX.change_face("bemused", 1)
            $ approval = approval_check(StormX, 1350, taboo_modifier=0)
            if approval_check(StormX, 950, "L", taboo_modifier=0) or (approval and StormX.love > StormX.obedience):
                ch_s "Really? Very well . ."
            elif approval_check(StormX, 700, "I", taboo_modifier=0) or (approval and StormX.inhibition > StormX.obedience):
                ch_s "Oh, I was growing rather attached. . ."
            elif approval_check(StormX, 600, "O", taboo_modifier=0) or approval:
                ch_s "Fine."
            else:
                $ StormX.change_face("surprised")
                $ StormX.brows = "angry"
                ch_s "I grown rather attached."
                return
            $ StormX.take_off("piercings")

        "Add gold_necklace" if StormX.Clothes["neck"] != "gold_necklace":
            ch_p "Why don't you try on that gold necklace?"
            ch_s "Ok. . ."
            $ StormX.Clothes["neck"] = "gold_necklace"
        "Add ring_necklace" if StormX.Clothes["neck"] != "rings" and "halloween" in StormX.history:
            ch_p "Why don't you try on that ring necklace?"
            ch_s "Ok. . ."
            $ StormX.Clothes["neck"] = "rings"
        "Remove Necklace" if StormX.Clothes["neck"]:
            ch_p "Maybe go without a necklace."
            ch_s "Ok. . ."
            $ StormX.take_off("neck")

        "Add Arm and Leg hoops." if StormX.Clothes["loincloth"] != "rings" and "halloween" in StormX.history:
            ch_p "Why don't you wear those body hoops?"
            ch_s "Ok. . ."
            $ StormX.Clothes["loincloth"] = "rings"
        "Remove Arm and Leg hoops." if StormX.Clothes["loincloth"] == "rings":
            ch_p "Why don't you take off those body hoops?"
            ch_s "Ok. . ."
            $ StormX.take_off("loincloth")
        "Never mind":








            pass
    return


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
