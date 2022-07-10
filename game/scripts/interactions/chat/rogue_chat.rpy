label Rogue_Relationship:
    while True:
        menu:
            ch_r "What did you want to ask me about?"
            "Do you want to be my girlfriend?" if RogueX not in Player.Harem and "ex" not in RogueX.traits:
                $ RogueX.daily_history.append("relationship")
                if "asked boyfriend" in RogueX.daily_history and "angry" in RogueX.daily_history:
                    $ RogueX.change_face("angry", 1)
                    ch_r "Seriously, stop bugging me."
                    return
                elif "asked boyfriend" in RogueX.daily_history:
                    $ RogueX.change_face("angry", 1)
                    ch_r "You already asked about that, the answer's still no."
                    return
                elif RogueX.broken_up[0]:
                    $ RogueX.change_face("angry", 1)
                    ch_r "I already told you, not while you're with her."
                    if Player.Harem:
                        $ RogueX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_p "I'm not anymore."

                $ RogueX.daily_history.append("asked boyfriend")

                if Player.Harem and "RogueYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_r "That wouldn't be fair to the others, [RogueX.player_petname]."
                    else:
                        ch_r "That wouldn't be fair to [Player.Harem[0].name], [RogueX.player_petname]."
                    return

                if RogueX.event_happened[5]:
                    $ RogueX.change_face("bemused", 1)
                    ch_r "I mean, I asked you about this before. . ."
                else:
                    $ RogueX.change_face("surprised", 2)
                    ch_r "Wow, this is unexpected, [RogueX.player_petname]. . ."
                    $ RogueX.change_face("smile", 1)

                call Rogue_OtherWoman

                if RogueX.love >= 800:
                    $ RogueX.change_face("surprised", 1)
                    $ RogueX.mouth = "smile"
                    call change_Girl_stat(RogueX, "love", 40)
                    ch_r "I'd love to!"
                    if "boyfriend" not in RogueX.player_petnames:
                        $ RogueX.player_petnames.append("boyfriend")
                    if "RogueYes" in Player.traits:
                        $ Player.traits.remove("RogueYes")
                    $ Player.Harem.append(RogueX)
                    call Harem_Initiation
                    "[RogueX.name] leaps in and kisses you deeply."
                    $ RogueX.change_face("kiss", 1)
                    $ RogueX.permanent_History["kiss"] += 1
                elif RogueX.obedience >= 500:
                    $ RogueX.change_face("perplexed")
                    ch_r "I'm not sure I'd call what we have \"dating.\""
                elif RogueX.inhibition >= 500:
                    $ RogueX.change_face("smile")
                    ch_r "I don't really want to be tied down like that."
                else:
                    $ RogueX.change_face("perplexed", 1)
                    ch_r "I don't really feel that way about you right now, [RogueX.player_petname]."

            "Do you want to get back together?" if "ex" in RogueX.traits:
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

                if Player.Harem and "RogueYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_r "That wouldn't be fair to the others, [RogueX.player_petname]."
                    else:
                        ch_r "That wouldn't be fair to [Player.Harem[0].name], [RogueX.player_petname]."
                    return

                $ counter = 0
                call Rogue_OtherWoman

                if RogueX.love >= 800:
                    $ RogueX.change_face("surprised", 1)
                    $ RogueX.mouth = "smile"
                    call change_Girl_stat(RogueX, "love", 5)
                    ch_r "If you're in, I'm in!"
                    if "boyfriend" not in RogueX.player_petnames:
                        $ RogueX.player_petnames.append("boyfriend")
                    $ RogueX.traits.remove("ex")
                    if "RogueYes" in Player.traits:
                        $ Player.traits.remove("RogueYes")
                    $ Player.Harem.append(RogueX)
                    call Harem_Initiation
                    "[RogueX.name] leaps in and kisses you deeply."
                    $ RogueX.change_face("kiss", 1)
                    $ RogueX.permanent_History["kiss"] += 1
                elif RogueX.love >= 600 and approval_check(RogueX, 1500):
                    $ RogueX.change_face("smile", 1)
                    $ RogueX.mouth = "smile"
                    call change_Girl_stat(RogueX, "love", 5)
                    ch_r "We can give this another try."
                    if "boyfriend" not in RogueX.player_petnames:
                        $ RogueX.player_petnames.append("boyfriend")
                    $ RogueX.traits.remove("ex")
                    if "RogueYes" in Player.traits:
                        $ Player.traits.remove("RogueYes")
                    $ Player.Harem.append(RogueX)
                    call Harem_Initiation
                    "[RogueX.name] gives you a quick kiss."
                    $ RogueX.change_face("kiss", 1)
                    $ RogueX.permanent_History["kiss"] += 1
                elif RogueX.obedience >= 500:
                    $ RogueX.change_face("sad")
                    ch_r "Whatever we had, whatever we have right now, that's not it."
                elif RogueX.inhibition >= 500:
                    $ RogueX.change_face("perplexed")
                    ch_r "We tried that, it didn't work out."
                else:
                    $ RogueX.change_face("perplexed", 1)
                    ch_r "I'm not ready for more heartbreak, [RogueX.player_petname]."



            "I wanted to ask about [[another girl]" if RogueX in Player.Harem:
                call AskDateOther

            "I think we should break up." if RogueX in Player.Harem:
                if "breakup talk" in RogueX.recent_history:
                    ch_r "We were {i}just{/i} over this, not even funny."
                elif "breakup talk" in RogueX.daily_history:
                    ch_r "Tired of me again that quick?"
                    ch_r "We're not having this talk today, [RogueX.player_petname]."
                else:
                    call Breakup (RogueX)
            "About that talk we had before. . .":

                menu:
                    "You weren't a virgin?" if RogueX.permanent_History["sex"] and not RogueX.had_chat[0]:
                        call Rogue_Not_Virgin

                    "You said you wanted me to be your Master?" if RogueX.event_happened[8] and "master" not in RogueX.player_petnames:
                        menu:
                            ch_r "Yes?"
                            "I'm ok with that now.":
                                if approval_check(RogueX, 800, "O"):
                                    $ RogueX.change_face("sexy", 1)
                                    ch_r "I hope to serve well, Master."
                                    call change_Girl_stat(RogueX, "obedience", 100)
                                    $ RogueX.player_petnames.append("master")
                                    $ RogueX.event_happened[8] = 2
                                else:
                                    ch_r "Well, I'm not really interested in that sort of thing anymore."
                                    ch_r "I mean, maybe later."
                            "Never mind.":
                                $ RogueX.change_face("sad")
                                ch_r "Oh."
                                call change_Girl_stat(RogueX, "obedience", -5)
                                call change_Girl_stat(RogueX, "love", -5)
                    "Never mind":
                        pass
            "Never mind":
                return
        return


label Rogue_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((RogueX.likes[Player.Harem[0].tag] - 500)/2)

    $ RogueX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_r "But you're with [Player.Harem[0].name] right now, and a whole mess'a other girls!"
    else:
        ch_r "But you're with [Player.Harem[0].name]!"
    menu:
        extend ""
        "She said I can be with you too." if "RogueYes" in Player.traits:
            if approval_check(RogueX, 1800, Bonus = counter):
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


        "I could ask if she'd be ok with me dating you both." if "RogueYes" not in Player.traits:
            if approval_check(RogueX, 1800, Bonus = counter):
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

            if not approval_check(RogueX, 1800, Bonus = -counter):
                $ RogueX.change_face("angry", 1)
                if not approval_check(RogueX, 1800):
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
                $ RogueX.add_word(1, 0, 0, "downlow")
        "I can break it off with her.":

            $ RogueX.change_face("sad")
            ch_r "Well then talk to me after you have."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ RogueX.change_face("sad")
            ch_r "Yeah. . ."
            $ renpy.pop_call()

    return


label Rogue_About(Check=0):
    if Check not in all_Girls:
        ch_r "Who?"
        return
    ch_r "What do I think about her? Well. . ."
    if Check == KittyX:
        if "poly Kitty" in RogueX.traits:
            ch_r "I think you know the answer to that one. . ."
        elif RogueX.likes[KittyX.tag] >= 900:
            ch_r "I think she's really . . . hot?"
        elif RogueX.likes[KittyX.tag] >= 800:
            ch_r "I feel really close to her, best friends, maybe more."
        elif RogueX.likes[KittyX.tag] >= 700:
            ch_r "She's one of my best friends."
        elif RogueX.likes[KittyX.tag] >= 600:
            ch_r "We're good friends."
        elif RogueX.likes[KittyX.tag] >= 500:
            ch_r "I don't know, she's ok."
        elif RogueX.likes[KittyX.tag] >= 400:
            ch_r "We're. . . kind of off right now."
        elif RogueX.likes[KittyX.tag] >= 300:
            ch_r "I don't want to talk about it."
        else:
            ch_r "That ho-bag skank?"
    elif Check == EmmaX:
        if "poly Emma" in RogueX.traits:
            ch_r "Well, I sure don't kick her out of bed. . ."
        elif RogueX.likes[EmmaX.tag] >= 900:
            ch_r "I'm kinda hot for teacher."
        elif RogueX.likes[EmmaX.tag] >= 800:
            ch_r "She's pretty amaz'in, right? Sometimes I wonder. . ."
        elif RogueX.likes[EmmaX.tag] >= 700:
            ch_r "We hang out sometimes after class, she's fun to talk to."
        elif RogueX.likes[EmmaX.tag] >= 600:
            ch_r "She's a really great teach, I love her lectures."
        elif RogueX.likes[EmmaX.tag] >= 500:
            ch_r "I don't know, she's ok."
        elif RogueX.likes[EmmaX.tag] >= 400:
            ch_r "I don't really like the way she looks at you in class."
        elif RogueX.likes[EmmaX.tag] >= 300:
            ch_r "I hate her class."
        else:
            ch_r "Ugh, that WITCH!"
    elif Check == LauraX:
        if "poly Laura" in RogueX.traits:
            ch_r "We hook up from time to time. . ."
        elif RogueX.likes[LauraX.tag] >= 900:
            ch_r "She's got an animal magnetism to her. . ."
        elif RogueX.likes[LauraX.tag] >= 800:
            ch_r "We really seem to get along. . ."
        elif RogueX.likes[LauraX.tag] >= 700:
            ch_r "She's a good friend."
        elif RogueX.likes[LauraX.tag] >= 600:
            ch_r "She's a good teammate."
        elif RogueX.likes[LauraX.tag] >= 500:
            ch_r "I don't know, she's ok in a fight."
        elif RogueX.likes[LauraX.tag] >= 400:
            ch_r "We're. . . not in a good place."
        elif RogueX.likes[LauraX.tag] >= 300:
            ch_r "I don't want to talk about it."
        else:
            ch_r "That ho-bag skank?"
    elif Check == JeanX:
        if "poly Jean" in RogueX.traits:
            ch_r "We hook up from time to time. . ."
        elif RogueX.likes[JeanX.tag] >= 900:
            ch_r "She's got a real charm to her. . ."
        elif RogueX.likes[JeanX.tag] >= 800:
            ch_r "We really seem to get along. . ."
        elif RogueX.likes[JeanX.tag] >= 700:
            ch_r "She's a. . . friend."
        elif RogueX.likes[JeanX.tag] >= 600:
            ch_r "She's a good teammate."
        elif RogueX.likes[JeanX.tag] >= 500:
            ch_r "I don't know, she's ok."
        elif RogueX.likes[JeanX.tag] >= 400:
            ch_r "We're. . . not in a good place."
        elif RogueX.likes[JeanX.tag] >= 300:
            ch_r "I'm tired a' her nonsense."
        else:
            ch_r "That ho-bag witch?!"
    elif Check == StormX:
        if "poly Storm" in RogueX.traits:
            ch_r "Well, she's sure nice to cuddle up to. . ."
        elif RogueX.likes[StormX.tag] >= 900:
            ch_r "I'm kinda into her."
        elif RogueX.likes[StormX.tag] >= 800:
            ch_r "She's pretty great, right? I kinda wonder. . ."
        elif RogueX.likes[StormX.tag] >= 700:
            ch_r "We talk sometimes after class, she's a good listener."
        elif RogueX.likes[StormX.tag] >= 600:
            ch_r "She's a really great teach, I love her lectures."
        elif RogueX.likes[StormX.tag] >= 500:
            ch_r "I don't know, she's ok."
        elif RogueX.likes[StormX.tag] >= 400:
            ch_r "I don't really like the way she looks at you in class."
        elif RogueX.likes[StormX.tag] >= 300:
            ch_r "I hate her class."
        else:
            ch_r "Ugh, that WITCH!"
    elif Check == JubesX:
        if "poly Jubes" in RogueX.traits:
            ch_r "I think you know the answer to that one. . ."
        elif RogueX.likes[JubesX.tag] >= 900:
            ch_r "I think she's really . . . hot?"
        elif RogueX.likes[JubesX.tag] >= 800:
            ch_r "I think we work really great together. . ."
        elif RogueX.likes[JubesX.tag] >= 700:
            ch_r "She's a really good friend."
        elif RogueX.likes[JubesX.tag] >= 600:
            ch_r "We're friends."
        elif RogueX.likes[JubesX.tag] >= 500:
            ch_r "I don't know, she's ok."
        elif RogueX.likes[JubesX.tag] >= 400:
            ch_r "We're. . . kind of off right now."
        elif RogueX.likes[JubesX.tag] >= 300:
            ch_r "I don't want to talk about it."
        else:
            ch_r "That ho-bag skank?"
    return


label Rogue_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "monogamous" not in RogueX.traits:
            if RogueX.thirst >= 60 and not approval_check(RogueX, 1700, "LO", taboo_modifier=0):

                $ RogueX.change_face("sly", 1)
                if "monogamous" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "obedience", -2)
                ch_r "I might consider that, but you don't exactly make yourself available. . ."
                return
            elif approval_check(RogueX, 1200, "LO", taboo_modifier=0) and RogueX.love >= RogueX.obedience:

                $ RogueX.change_face("sly", 1)
                if "monogamous" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "love", 1)
                ch_r "Aw, would that make you jealous?"
                ch_r "I suppose I could restain myself. . ."
            elif approval_check(RogueX, 700, "O", taboo_modifier=0):

                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "If that's what you really want. . ."
            else:

                $ RogueX.change_face("sly", 1, brows = "confused")
                ch_r "Who I \"hook up\" with is my own damned business."
                return
            if "monogamous" not in RogueX.daily_history:
                call change_Girl_stat(RogueX, "obedience", 3)
            $ RogueX.add_word(1, 0, "monogamous", "monogamous")
        "Don't hook up with other girls." if "monogamous" not in RogueX.traits:
            if approval_check(RogueX, 900, "O", taboo_modifier=0):

                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "Ok."
            elif RogueX.thirst >= 60 and not approval_check(RogueX, 1700, "LO", taboo_modifier=0):

                $ RogueX.change_face("sly", 1)
                if "monogamous" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "obedience", -2)
                ch_r "I might consider that, but you don't exactly make yourself available. . ."
                return
            elif approval_check(RogueX, 550, "O", taboo_modifier=0):

                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "If that's what you really want. . ."
            elif approval_check(RogueX, 1400, "LO", taboo_modifier=0):

                $ RogueX.change_face("sly", 1)
                ch_r "Is that any way to ask a girl?"
                ch_r "Still, I'll do it for you. . ."
            else:

                $ RogueX.change_face("sly", 1, brows = "confused")
                ch_r "Who I \"hook up\" with is my own damned business."
                return
            if "monogamous" not in RogueX.daily_history:
                call change_Girl_stat(RogueX, "obedience", 3)
            $ RogueX.add_word(1, 0, "monogamous", "monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in RogueX.traits:
            if approval_check(RogueX, 700, "O", taboo_modifier=0):
                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "As you wish."
            elif approval_check(RogueX, 800, "L", taboo_modifier=0):
                $ RogueX.change_face("sly", 1)
                ch_r "I hope you don't give me any reasons to want to. . ."
            else:
                $ RogueX.change_face("sly", 1, brows = "confused")
                if "monogamous" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "love", -2)
                ch_r "Oh? Well, glad I got your permission there."
            if "monogamous" not in RogueX.daily_history:
                call change_Girl_stat(RogueX, "obedience", 3)
            if "monogamous" in RogueX.traits:
                $ RogueX.traits.remove("monogamous")
            $ RogueX.add_word(1, 0, "monogamous")
        "Never mind.":
            pass
    return




label Rogue_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ RogueX.change_face("sly", 1, brows = "confused")
    menu:
        ch_r "Yeah?"
        "Could you maybe just ask instead?" if "chill" not in RogueX.traits:
            if RogueX.thirst >= 60 and not approval_check(RogueX, 1500, "LO", taboo_modifier=0):

                $ RogueX.change_face("sly", 1)
                if "chill" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "obedience", -2)
                ch_r "Maybe don't keep me waiting then. . ."
                return
            elif approval_check(RogueX, 1000, "LO", taboo_modifier=0) and RogueX.love >= RogueX.obedience:

                $ RogueX.change_face("sly", 1)
                if "chill" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "love", 1)
                ch_r "Sorry, [RogueX.player_petname], I just got a little lonely. . ."
                ch_r "I'll be good. . ."
            elif approval_check(RogueX, 500, "O", taboo_modifier=0):

                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "If that's what you really want. . ."
            else:

                $ RogueX.change_face("sly", 1, brows = "confused")
                ch_r "I can't make any promises."
                return
            if "chill" not in RogueX.daily_history:
                call change_Girl_stat(RogueX, "obedience", 3)
            $ RogueX.add_word(1, 0, "chill", "chill")
        "Don't bother me like that." if "chill" not in RogueX.traits:
            if approval_check(RogueX, 900, "O", taboo_modifier=0):

                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "Ok."
            elif RogueX.thirst >= 60 and not approval_check(RogueX, 600, "O", taboo_modifier=0):

                $ RogueX.change_face("sly", 1)
                if "chill" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "obedience", -2)
                ch_r "Maybe don't keep me waiting then. . ."
                return
            elif approval_check(RogueX, 450, "O", taboo_modifier=0):

                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "If that's what you really want. . ."
            elif approval_check(RogueX, 500, "LO", taboo_modifier=0) and not approval_check(RogueX, 500, "I", taboo_modifier=0):

                $ RogueX.change_face("sly", 1)
                ch_r "You might want to watch your mouth."
                ch_r "Still, I'll try to keep to myself. . ."
            else:

                $ RogueX.change_face("sly", 1, brows = "confused")
                ch_r "No promises."
                return
            if "chill" not in RogueX.daily_history:
                call change_Girl_stat(RogueX, "obedience", 3)
            $ RogueX.add_word(1, 0, "chill", "chill")
        "Knock yourself out.":
            if approval_check(RogueX, 800, "L", taboo_modifier=0):
                $ RogueX.change_face("sly", 1)
                ch_r "Will do. . ."
            elif approval_check(RogueX, 700, "O", taboo_modifier=0):
                $ RogueX.change_face("sly", 1, eyes = "side")
                ch_r "Yes sir."
            else:
                $ RogueX.change_face("sly", 1, brows = "confused")
                if "chill" not in RogueX.daily_history:
                    call change_Girl_stat(RogueX, "love", -2)
                ch_r "Maybe. If I've got nothing better to do."
            if "chill" not in RogueX.daily_history:
                call change_Girl_stat(RogueX, "obedience", 3)
            if "chill" in RogueX.traits:
                $ RogueX.traits.remove("chill")
            $ RogueX.add_word(1, 0, "chill")
        "Um, never mind.":
            pass
    return





label Rogue_Not_Virgin:
    menu:
        "I noticed that when we had sex, you didn't seem to be a virgin."
        "Wasn't I your first time?":
            $ RogueX.change_face("bemused", 1)
            call change_Girl_stat(RogueX, "love", 5)
            call change_Girl_stat(RogueX, "obedience", 15)
            ch_r "Oh, no! You definitely were, it's just. . . you know, "
            ch_r "I lead a pretty active lifestyle, so I lost that physical barrier years ago."
        "So you get around?":
            $ RogueX.change_face("sexy", 1)
            $ RogueX.brows = "angry"
            call change_Girl_stat(RogueX, "obedience", 15)
            call change_Girl_stat(RogueX, "obedience", 5)
            call change_Girl_stat(RogueX, "inhibition", 15)
            call change_Girl_stat(RogueX, "inhibition", 5)
            ch_r "Jerk, not like that. I tore it years ago in combat training."
        "Are you a slut?":
            $ RogueX.change_face("angry", 1)
            call change_Girl_stat(RogueX, "love", 1)
            call change_Girl_stat(RogueX, "love", 1)
            call change_Girl_stat(RogueX, "obedience", 30)
            call change_Girl_stat(RogueX, "obedience", 20)
            ch_r "If you'd like to find that out, you might want to rethink how you talk to me, [RogueX.player_petname]."
    $ RogueX.had_chat[0] = 1
    return




label Rogue_Hungry:
    if RogueX.had_chat[3]:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    elif RogueX.had_chat[2]:
        ch_r "You know, I've really come to enjoy the taste of your, serum. It's like my favorite drink!"
    else:
        ch_r "You know, I've really come to enjoy the taste of your. . . cum. I think I'd like some more of that."
    $ RogueX.traits.append("hungry")
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
                            if RogueX.player_favorite_action == "sex":
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "Yeah, I know that. . ."
                            elif RogueX.favorite_action == "sex":
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 10)
                                ch_r "Oooh, I love a good pipe cleaning too. . ."
                            elif RogueX.permanent_History["sex"] >= 5:
                                ch_r "Can't say as I mind a good roll in the hay."
                            elif not RogueX.permanent_History["sex"]:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} are y'all having sex {i}with?{/i}"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "Heh, [RogueX.player_petname], flithy mouth on you. . ."
                            $ RogueX.player_favorite_action = "sex"
                        "Anal.":

                            $ RogueX.change_face("sly")
                            if RogueX.player_favorite_action == "anal":
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "So I hear. . ."
                            elif RogueX.favorite_action == "anal":
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 10)
                                ch_r "I can't say as I mind that. . ."
                            elif RogueX.permanent_History["anal"] >= 10:
                                ch_r "It's not a bad way to spend some time. . ."
                            elif not RogueX.permanent_History["anal"]:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} are y'all fucking {i}with?{/i}"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "Heh, heh, I . . . I don't {i}mind{/i} it. . ."
                            $ RogueX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ RogueX.change_face("sly")
                            if RogueX.player_favorite_action == "blowjob":
                                call change_Girl_stat(RogueX, "lust", 3)
                                ch_r "I'm not surprised. . ."
                            elif RogueX.favorite_action == "blowjob":
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "I guess I have developed a real taste for you. . ."
                            elif RogueX.permanent_History["blowjob"] >= 10:
                                ch_r "I'm getting to enjoy it too . . ."
                            elif not RogueX.permanent_History["blowjob"]:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} is sucking you off?"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "I'm. . . getting used to the taste. . ."
                            $ RogueX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ RogueX.change_face("sly")
                            if RogueX.player_favorite_action == "titjob":
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "So I hear. . ."
                            elif RogueX.favorite_action == "titjob":
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 7)
                                ch_r "I really enjoy it too. . ."
                            elif RogueX.permanent_History["titjob"] >= 10:
                                ch_r "It's certainly an interesting experience . . ."
                            elif not RogueX.permanent_History["titjob"]:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} is tit fucking you?"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "I can't say as I blame you. . ."
                            $ RogueX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ RogueX.change_face("sly")
                            if RogueX.player_favorite_action == "footjob":
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "Yeah, you've said that before. . ."
                            elif RogueX.favorite_action == "footjob":
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 7)
                                ch_r "I do enjoy that sensation. . ."
                            elif RogueX.permanent_History["footjob"] >= 10:
                                ch_r "It is pretty nice to touch someone like that . . ."
                            elif not RogueX.permanent_History["footjob"]:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} is jerking you off?"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "I do like the sensation. . ."
                            $ RogueX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ RogueX.change_face("sly")
                            if RogueX.player_favorite_action == "handjob":
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "Yeah, you've said that before. . ."
                            elif RogueX.favorite_action == "handjob":
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 7)
                                ch_r "I love how you feel in my hand. . ."
                            elif RogueX.permanent_History["handjob"] >= 10:
                                ch_r "It is pretty nice to touch someone like that . . ."
                            elif not RogueX.permanent_History["handjob"]:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} is jerking you off?"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "I do like the sensation. . ."
                            $ RogueX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = RogueX.permanent_History["fondle_breasts"]+ RogueX.permanent_History["fondle_thighs"]+ RogueX.permanent_History["suck_breasts"] + RogueX.permanent_History["hotdog"]
                            $ RogueX.change_face("sly")
                            if RogueX.player_favorite_action == "fondle":
                                call change_Girl_stat(RogueX, "lust", 3)
                                ch_r "Yeah, I think we've established that. . ."
                            elif RogueX.favorite_action in ("hotdog", "suck_breasts", "fondle_breasts", "fondle_thighs"):
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "I love how you touch me. . ."
                            elif counter >= 10:
                                ch_r "It's nice to have someone who can really touch me . . ."
                            elif not counter:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} are you feeling up?"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "I do like how that feels. . ."
                            $ RogueX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ RogueX.change_face("sly")
                            if RogueX.player_favorite_action == "kiss":
                                call change_Girl_stat(RogueX, "love", 3)
                                ch_r "I've heard it before, but don't mind hearing it again. . ."
                            elif RogueX.favorite_action == "kiss":
                                call change_Girl_stat(RogueX, "love", 5)
                                call change_Girl_stat(RogueX, "lust", 5)
                                ch_r "I can't get over your lips either. . ."
                            elif RogueX.permanent_History["kiss"] >= 10:
                                ch_r "I love kissing you too . . ."
                            elif not RogueX.permanent_History["kiss"]:
                                $ RogueX.change_face("perplexed")
                                ch_r "Who {i}exactly{/i} are you smooch'in?"
                            else:
                                $ RogueX.change_face("bemused")
                                ch_r "It's nice being able to kiss someone without hurting them. . ."
                            $ RogueX.player_favorite_action = "kiss"

                    $ RogueX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(RogueX, 800):
                    $ RogueX.change_face("perplexed")
                    ch_r "I don't think that's any of your business. . ."
                else:
                    if RogueX.SEXP >= 50:
                        $ RogueX.change_face("sly")
                        ch_r "If you can't tell. . ."
                    else:
                        $ RogueX.change_face("bemused")
                        $ RogueX.eyes = "side"
                        ch_r "I don't know, I guess maybe. . ."


                    if not RogueX.favorite_action or RogueX.favorite_action == "kiss":
                        ch_r "I guess I love it when we kiss. . ."
                    elif RogueX.favorite_action == "anal":
                        if RogueX.permanent_History["anal"] >= 10:
                            ch_r "I like when you fuck my ass."
                        else:
                            ch_r "I like when you stick it in my. . . butt."
                    elif RogueX.favorite_action == "eat_ass":
                        ch_r "I like when you lick my. . . asshole."
                    elif RogueX.favorite_action == "finger_ass":
                        ch_r "I like when you . . . finger my asshole."
                    elif RogueX.favorite_action == "sex":
                        ch_r "I like when you fuck me hard."
                    elif RogueX.favorite_action == "eat_pussy":
                        ch_r "I like when you lick my pussy."
                    elif RogueX.favorite_action == "fondle_pussy":
                        ch_r "I like when you fingerblast me."
                    elif RogueX.favorite_action == "blowjob":
                        ch_r "I kind of like to suck your cock."
                    elif RogueX.favorite_action == "titjob":
                        ch_r "I like to work your cock with my tits."
                    elif RogueX.favorite_action == "handjob":
                        ch_r "I like the feel of your cock in my hand."
                    elif RogueX.favorite_action == "footjob":
                        ch_r "I kinda like to use my feet."
                    elif RogueX.favorite_action == "hotdog":
                        ch_r "I like it when you grind against me."
                    elif RogueX.favorite_action == "suck_breasts":
                        ch_r "I like it when you suck on my tits."
                    elif RogueX.favorite_action == "fondle_breasts":
                        ch_r "I like it when you feel up my tits."
                    elif RogueX.favorite_action == "fondle_thighs":
                        ch_r "I like it when you massage my thighs."
                    else:
                        ch_r "I don't really know. . ."



            "Don't talk as much during sex." if "vocal" in RogueX.traits:
                if "setvocal" in RogueX.daily_history:
                    $ RogueX.change_face("perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("bemused")
                        call change_Girl_stat(RogueX, "obedience", 1)
                        ch_r "Heh, ok, if that's what you want. . ."
                        $ RogueX.traits.remove("vocal")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("sadside")
                        call change_Girl_stat(RogueX, "obedience", 1)
                        ch_r "If that's what you want, [RogueX.player_petname]."
                        $ RogueX.traits.remove("vocal")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("sly")
                        call change_Girl_stat(RogueX, "love", -3)
                        call change_Girl_stat(RogueX, "obedience", -1)
                        call change_Girl_stat(RogueX, "inhibition", 5)
                        ch_r "I'll say what I want, and you'll like it, [RogueX.player_petname]."
                    else:
                        $ RogueX.change_face("angry")
                        call change_Girl_stat(RogueX, "love", -5)
                        call change_Girl_stat(RogueX, "obedience", -3)
                        call change_Girl_stat(RogueX, "inhibition", 10)
                        ch_r "Fuck you, I'll talk as much as I want."

                    $ RogueX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in RogueX.traits:
                if "setvocal" in RogueX.daily_history:
                    $ RogueX.change_face("perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("sly")
                        call change_Girl_stat(RogueX, "obedience", 2)
                        ch_r "Heh, ok, if that's what you want. . ."
                        $ RogueX.traits.append("vocal")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("sadside")
                        call change_Girl_stat(RogueX, "obedience", 2)
                        ch_r "If that's what you want, [RogueX.player_petname]."
                        $ RogueX.traits.append("vocal")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("sly")
                        call change_Girl_stat(RogueX, "obedience", 3)
                        ch_r "I can give it a shot, [RogueX.player_petname]."
                        $ RogueX.traits.append("vocal")
                    else:
                        $ RogueX.change_face("angry")
                        call change_Girl_stat(RogueX, "inhibition", 5)
                        ch_r "I'll say what I want, when I want."

                    $ RogueX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in RogueX.traits:
                if "initiative" in RogueX.daily_history:
                    $ RogueX.change_face("perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("bemused")
                        call change_Girl_stat(RogueX, "obedience", 1)
                        ch_r "Heh, ok, lead the way. . ."
                        $ RogueX.traits.append("passive")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("sadside")
                        call change_Girl_stat(RogueX, "obedience", 1)
                        ch_r "I'll restrain myself then, [RogueX.player_petname]."
                        $ RogueX.traits.append("passive")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("sly")
                        call change_Girl_stat(RogueX, "love", -3)
                        call change_Girl_stat(RogueX, "obedience", -1)
                        call change_Girl_stat(RogueX, "inhibition", 5)
                        ch_r "You know you don't want that, [RogueX.player_petname]."
                    else:
                        $ RogueX.change_face("angry")
                        call change_Girl_stat(RogueX, "love", -5)
                        call change_Girl_stat(RogueX, "obedience", -3)
                        call change_Girl_stat(RogueX, "inhibition", 10)
                        ch_r "I'll do what I want, prick."

                    $ RogueX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in RogueX.traits:
                if "initiative" in RogueX.daily_history:
                    $ RogueX.change_face("perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("bemused")
                        call change_Girl_stat(RogueX, "obedience", 1)
                        ch_r "Heh, I think I can handle that. . ."
                        $ RogueX.traits.remove("passive")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("sadside")
                        call change_Girl_stat(RogueX, "obedience", 1)
                        ch_r "I can do that, [RogueX.player_petname]."
                        $ RogueX.traits.remove("passive")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("sly")
                        call change_Girl_stat(RogueX, "obedience", 3)
                        ch_r "I can certainly try, [RogueX.player_petname]."
                        $ RogueX.traits.remove("passive")
                    else:
                        $ RogueX.change_face("angry")
                        call change_Girl_stat(RogueX, "inhibition", 5)
                        ch_r "If I want to, I will, but not because you say so."

                    $ RogueX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in RogueX.history:
                call Rogue_Jumped
            "About when you masturbate":
                call NoFap (RogueX)

            "Never mind" if line == "Yeah, what did you want to talk about?":
                return
            "That's all." if line != "Yeah, what did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return





label Rogue_Chitchat(O=0, Options = ["default", "default", "default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:
        if RogueX not in Player.Phonebook:
            if approval_check(RogueX, 500, "L") or approval_check(RogueX, 250, "I"):
                ch_r "You know, I never got around to giving you my number, here you go."
                $ Player.Phonebook.append(RogueX)
                return
            elif approval_check(RogueX, 250, "O"):
                ch_r "You know, you should probably have my number, here you go."
                $ Player.Phonebook.append(RogueX)
                return
        if "hungry" not in RogueX.traits and (RogueX.permanent_History["swallowed"] + RogueX.had_chat[2]) >= 10 and RogueX.location == Player.location:
            call Rogue_Hungry
            return
        if Player.location != "bg_restaurant" and Player.location != "bg_halloween" and (not taboo or approval_check(RogueX, 800, "I")):
            if RogueX.location == Player.location and RogueX.thirst >= 30 and "refused" not in RogueX.daily_history and "quicksex" not in RogueX.daily_history:
                $ RogueX.change_face("sly", 1)
                ch_r "Hey, do you want to get a little frisky?"
                call Quick_Sex (RogueX)
                return


        if approval_check(RogueX, 1200) and Player.location == RogueX.location and Player.location != "bg_restaurant":
            $ Options.append("dance")
        if approval_check(RogueX, 800, "L") and "nametag chat" not in RogueX.daily_history:
            $ Options.append("close")
        if RogueX.permanent_History["blowjob"] >= 2:
            $ Options.append("blowjob")
        if "steal" in RogueX.traits:
            $ Options.append("steal")
        if Player.being_punished and "caught chat" not in RogueX.daily_history:
            $ Options.append("caught")
        if RogueX.event_happened[0] and "key chat" not in RogueX.daily_history:
            $ Options.append("key")
        if "lover" in RogueX.player_petnames and approval_check(RogueX, 900, "L"):
            $ Options.append("luv")

        if "mandrill" in Player.traits and "cologne chat" not in RogueX.daily_history:
            $ Options.append("mandrill")
        if "purple" in Player.traits and "cologne chat" not in RogueX.daily_history:
            $ Options.append("purple")
        if "corruption" in Player.traits and "cologne chat" not in RogueX.daily_history:
            $ Options.append("corruption")

        if not RogueX.had_chat[0] and RogueX.permanent_History["sex"]:
            $ Options.append("virgin")

        if "seenpeen" in RogueX.history:
            $ Options.append("seenpeen")
        if "topless" in RogueX.history:
            $ Options.append("topless")
        if "bottomless" in RogueX.history:
            $ Options.append("bottomless")

        if "lover" in RogueX.player_petnames and "Anna" not in RogueX.names:

            $ Options.append("annamarie")

        if (Player.location == "bg_rogue" or Player.location == "bg_player") and "nametag chat" not in RogueX.daily_history:
            if "lover" not in RogueX.player_petnames and approval_check(RogueX, 900, "L"):
                $ Options.append("lover?")
            elif "sir" not in RogueX.player_petnames and approval_check(RogueX, 500, "O"):
                $ Options.append("sir?")
            elif "daddy" not in RogueX.player_petnames and approval_check(RogueX, 750, "L") and approval_check(RogueX, 500, "O") and approval_check(RogueX, 500, "I"):
                $ Options.append("daddy?")
            elif "master" not in RogueX.player_petnames and approval_check(RogueX, 900, "O"):
                $ Options.append("master?")
            elif "sex friend" not in RogueX.player_petnames and approval_check(RogueX, 500, "I"):
                $ Options.append("sexfriend?")
            elif "fuck buddy" not in RogueX.player_petnames and approval_check(RogueX, 900, "I"):
                $ Options.append("fuckbuddy?")

        if not approval_check(RogueX, 300):
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)

    if Options[0] == "virgin":
        call Rogue_Not_Virgin

    elif Options[0] == "mandrill":
        $ RogueX.daily_history.append("cologne chat")
        $ RogueX.change_face("confused")
        ch_r "(sniff, sniff). . . something kind of smells like monkey butt in here. . ."
        $ RogueX.change_face("sly", 1)
        ch_r ". . . but you're looking pretty handsome today, [RogueX.player_petname]."
    elif Options[0] == "purple":
        $ RogueX.daily_history.append("cologne chat")
        $ RogueX.change_face("sly", 1)
        ch_r "(sniff, sniff). . . hmm, you're smelling good today. . ."
        ch_r ". . . was there anything I could do to make you happy?"
    elif Options[0] == "corruption":
        $ RogueX.daily_history.append("cologne chat")
        $ RogueX.change_face("confused")
        ch_r "(sniff, sniff). . . that's a pretty strong scent you've got there. . ."
        $ RogueX.change_face("sly")
        ch_r ". . . I'm gettin some pretty naughty thoughts over here, [RogueX.player_petname]. . ."

    elif Options[0] == "blowjob":
        $ line = renpy.random.choice(["You know, you taste better than I thought.",
                "You're making my jaw a bit sore there.",
                "Let me know if you want a little mouth attention.",
                "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
        ch_r "[line]"

    elif Options[0] == "close":
        ch_r "It's always been hard for me to get close to people, since I could never. . ."
        ch_r "get {i}close{/i} to them, you know?"
        ch_r "It's been real good for me to be able to get close to you like this."
        $ RogueX.daily_history.append("close chat")
    elif Options[0] == "caught":
        ch_r "Wow, that was scary getting dragged into the Professor's office."
        if not approval_check(RogueX, 500, "I"):
            ch_r "Maybe we should be more careful about where we. . . you know."
        else:
            ch_r "Maybe we should be more careful about where we fuck."
        $ RogueX.daily_history.append("caught chat")
    elif Options[0] == "key":
        if RogueX.SEXP <= 15:
            ch_r "I'm glad you have my key now, just don't use it for any funny business. . ."
        else:
            ch_r "I'm glad you have my key now, maybe you could . . . \"surprise\" me sometime. . ."
        $ RogueX.daily_history.append("key chat")
    elif Options[0] == "touch":
        ch_r "It's only because I've been working with you so much that I've been able to learn to control my abilities."
        ch_r "If it weren't for you, I wouldn't have been able to touch anyone!"
    elif Options[0] == "steal":
        ch_r "It's only because of having worked with you and your powers that I've learned to permanently copy other mutant powers."
    elif Options[0] == "dance":
        ch_r "Can't wait for the next big party."
        ch_r "I love to dance, and I've got the best partner to grind with-"
        $ RogueX.pose = "doggy"
        call show_sex(RogueX, "massage")
        if RogueX.wearing_skirt:
            $ RogueX.upskirt = True
            if RogueX.Clothes["underwear"] and RogueX.seen_underwear and approval_check(RogueX, 800, taboo_modifier = 3):
                pass
            elif RogueX.Clothes["underwear"] and approval_check(RogueX, 800, taboo_modifier = 3):
                $ RogueX.seen_underwear = True
            elif RogueX.Clothes["underwear"]:
                $ RogueX.upskirt = True
            elif RogueX.seen_pussy and approval_check(RogueX, 1000, taboo_modifier = 4):
                pass
            elif approval_check(RogueX, 1400, taboo_modifier = 3):
                call Rogue_First_Bottomless (1)
            else:
                $ RogueX.upskirt = False
            pause 0.5
            $ RogueX.upskirt = False
        ch_r "Y'know what I'm sayin', [RogueX.player_petname]?"
        $ RogueX.upskirt = False
        call show_full_body(Girl)

    elif Options[0] == "seenpeen":
        $ RogueX.change_face("sly", 1)
        ch_r "You really did surprise me when you whipped that cock out."
        ch_r "I didn't know they looked so big up close."
        $ RogueX.change_face("bemused", 1)
        call change_Girl_stat(RogueX, "love", 5)
        $ RogueX.history.remove("seenpeen")
    elif Options[0] == "topless":
        ch_r "Hey, when you got a look at my tits earlier, you didn't have much to say. . ."
        ch_r "Did you like what you saw?"
        call Rogue_First_TMenu
        $ RogueX.history.remove("topless")
    elif Options[0] == "bottomless":
        ch_r "Hey, when you saw me bottomless earlier, you didn't have much to say. . ."
        call Rogue_First_BMenu
        $ RogueX.history.remove("bottomless")

    elif Options[0] == "luv":
        $ RogueX.change_face("bemused", 1)
        ch_r ". . ."
        ch_r "You know, time was, I really thought I'd end up alone, unable to touch anyone. . ."
        $ RogueX.change_face("smile")
        ch_r "I'm really glad that I was able to find you."
        ch_r "I love you, [RogueX.player_petname]."
        menu:
            extend ""
            "I love you too.":
                call change_Girl_stat(RogueX, "love", 10)
                call change_Girl_stat(RogueX, "obedience", 4)
                call change_Girl_stat(RogueX, "inhibition", 4)
            "I love you too, [RogueX.petname].":
                $ RogueX.name_check()
                if _return:
                    $ RogueX.change_face("angry")
                    call change_Girl_stat(RogueX, "love", -1)
                    call change_Girl_stat(RogueX, "obedience", 10)
                    call change_Girl_stat(RogueX, "inhibition", 4)
                else:
                    call change_Girl_stat(RogueX, "love", 10)
                    call change_Girl_stat(RogueX, "obedience", 4)
                    call change_Girl_stat(RogueX, "inhibition", 4)
            "Yeah, same here.":
                $ RogueX.change_face("perplexed")
                call change_Girl_stat(RogueX, "love", -1)
                call change_Girl_stat(RogueX, "obedience", 10)
                call change_Girl_stat(RogueX, "inhibition", 4)
            "Whatever.":
                $ RogueX.change_face("angry")
                call change_Girl_stat(RogueX, "love", -10)
                call change_Girl_stat(RogueX, "obedience", 4)
                call change_Girl_stat(RogueX, "inhibition", 10)

    elif Options[0] == "boyfriend?":
        call Rogue_BF
        $ RogueX.daily_history.append("nametag chat")
    elif Options[0] == "lover?":
        call Rogue_Love
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
        call Rogue_AnnaMarie
    elif Options[0] == "hate":
        $ line = renpy.random.choice(["Get away from me.",
                "I don't want to see your face.",
                "Stop bothering me.",
                "Leave me alone."])
        ch_r "[line]"
    else:

        $ D20 = renpy.random.randint(1, 16)
        if D20 == 1:
            $ RogueX.change_face("confused")
            ch_r "I'm so nervous about this Genetics test with Professor McCoy. I don't get this stuff at all."
        elif D20 == 2:
            $ RogueX.change_face("sad")
            ch_r "Feeling kinda down today, [RogueX.player_petname]. Family problems. It's. . .kinda complicated."
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
            $ RogueX.eyes = "surprised"
            ch_r "I just saw the coolest thing, when I was walking through the courtyard! A bunch of deer, in the woods, just over by the fence!"
            $ RogueX.eyes = "side"
            ch_r "Their fur looked so. . .{i}soft{/i}. I wonder what they actually feel like?"
        elif D20 == 8:
            $ RogueX.change_face("smile")
            ch_r "Hey, did you see the Avengers on the news this morning? Those guys make everything look {i}so{/i} easy!"
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
            ch_r "You know, I tagged Wolverine once, "
            $ RogueX.change_face("sadside")
            $ RogueX.brows = "confused"
            ch_r "I still catch myself calling people \"bub\" from time to time."
        else:
            $ RogueX.change_face("smile")
            ch_r "I like hanging out with you like this!"
    $ line = 0
    return


label Rogue_names:

    if approval_check(RogueX, 600, "L", taboo_modifier=0) or approval_check(RogueX, 300, "O", taboo_modifier=0):
        pass
    else:
        $ RogueX.mouth = "smile"
        ch_r "I'll call you what I like, [RogueX.player_petname], and you'll like it."
        return
    menu:
        ch_r "Oh? What would you like me to call you?"
        "Sugar's fine.":
            $ RogueX.player_petname = "sugar"
            ch_r "You got it, sugar."
        "Call me by my name.":
            $ RogueX.player_petname = Player.name
            ch_r "If you'd rather, [RogueX.player_petname]."
        "Call me \"boyfriend\"." if "boyfriend" in RogueX.player_petnames:
            $ RogueX.player_petname = "boyfriend"
            ch_r "Sure thing, [RogueX.player_petname]."
        "Call me \"lover\"." if "lover" in RogueX.player_petnames:
            $ RogueX.player_petname = "lover"
            ch_r "Oooh, love to, [RogueX.player_petname]."
        "Call me \"sir\"." if "sir" in RogueX.player_petnames:
            $ RogueX.player_petname = "sir"
            ch_r "Yes, [RogueX.player_petname]."
        "Call me \"master\"." if "master" in RogueX.player_petnames:
            $ RogueX.player_petname = "master"
            ch_r "As you wish, [RogueX.player_petname]."
        "Call me \"sex friend\"." if "sex friend" in RogueX.player_petnames:
            $ RogueX.player_petname = "sex friend"
            ch_r "Heh, very cheeky, [RogueX.player_petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in RogueX.player_petnames:
            $ RogueX.player_petname = "fuck buddy"
            ch_r "I'm game if you are, [RogueX.player_petname]."
        "Call me \"daddy\"." if "daddy" in RogueX.player_petnames:
            $ RogueX.player_petname = "daddy"
            ch_r "Oh! You bet, [RogueX.player_petname]."
        "Nevermind.":
            return
    return


label Rogue_Pet:

    if approval_check(RogueX, 600, "L", taboo_modifier=0):
        ch_r "Oh? What is it?"
    elif approval_check(RogueX, 300, "O", taboo_modifier=0):
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
                        $ RogueX.petname = "Rogue"
                        ch_r "I don't see why not, [RogueX.player_petname]."
                    "I think I'll call you \"girl\".":

                        $ RogueX.petname = "girl"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            $ RogueX.change_face("sexy", 1)
                            ch_r "I sure am your girl, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry")
                            ch_r "I ain't your girl, [RogueX.player_petname]."
                    "I think I'll call you \"boo\".":

                        $ RogueX.petname = "boo"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            $ RogueX.change_face("sexy", 1)
                            ch_r "Aw, I am your boo, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry")
                            ch_r "I ain't your boo, [RogueX.player_petname]."
                    "I think I'll call you \"bae\".":

                        $ RogueX.petname = "bae"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            $ RogueX.change_face("sexy", 1)
                            ch_r "Aw, I am your bae, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry")
                            ch_r "I ain't your bae, [RogueX.player_petname]."
                    "I think I'll call you \"baby\".":

                        $ RogueX.petname = "baby"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            $ RogueX.change_face("sexy", 1)
                            ch_r "Aw, cute, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry")
                            ch_r "I ain't your baby, [RogueX.player_petname]."
                    "I think I'll call you \"chere\".":

                        $ RogueX.petname = "chere"
                        if "lover" in RogueX.player_petnames or approval_check(RogueX, 600, "L"):
                            $ RogueX.change_face("sexy", 1)
                            ch_r "Oh, tre romantic, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            $ RogueX.eyes = "side"
                            ch_r "That has some. . . bad memories, [RogueX.player_petname]."
                    "I think I'll call you \"sweetie\".":

                        $ RogueX.petname = "sweetie"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            ch_r "Aw, that's sweet, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "That's a bit much, [RogueX.player_petname]."
                    "I think I'll call you \"sexy\".":

                        $ RogueX.petname = "sexy"
                        if "lover" in RogueX.player_petnames or approval_check(RogueX, 900):
                            $ RogueX.change_face("sexy", 1)
                            ch_r "You're not so bad yourself, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "Inappropriate, [RogueX.player_petname]."
                    "I think I'll call you \"lover\".":

                        $ RogueX.petname = "lover"
                        if "lover" in RogueX.player_petnames or approval_check(RogueX, 900):
                            $ RogueX.change_face("sexy", 1)
                            ch_r "Oh, I love you too, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "Not any time soon, [RogueX.player_petname]."
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you \"slave\".":
                        $ RogueX.petname = "slave"
                        if "master" in RogueX.player_petnames or approval_check(RogueX, 700, "O"):
                            $ RogueX.change_face("bemused", 1)
                            ch_r "As you wish, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "I ain't anyone's slave, [RogueX.player_petname]."
                    "I think I'll call you \"pet\".":

                        $ RogueX.petname = "pet"
                        if "master" in RogueX.player_petnames or approval_check(RogueX, 600, "O"):
                            $ RogueX.change_face("bemused", 1)
                            ch_r "Hmm, make sure to pet me, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "I ain't your pet, [RogueX.player_petname]."
                    "I think I'll call you \"slut\".":

                        $ RogueX.petname = "slut"
                        if "sex friend" in RogueX.player_petnames or approval_check(RogueX, 1000, "OI"):
                            $ RogueX.change_face("sexy")
                            ch_r "You know me too well, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            $ RogueX.mouth = "surprised"
                            ch_r "Well I never!"
                    "I think I'll call you \"whore\".":

                        $ RogueX.petname = "whore"
                        if "fuckbuddy" in RogueX.player_petnames or approval_check(RogueX, 1100, "OI"):
                            $ RogueX.change_face("sly")
                            ch_r "I guess I am. . ."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "You look'in to start something, [RogueX.player_petname]?"
                    "I think I'll call you \"sugartits\".":

                        $ RogueX.petname = "sugartits"
                        if "sex friend" in RogueX.player_petnames or approval_check(RogueX, 1500):
                            $ RogueX.change_face("sly", 1)
                            ch_r "Heh."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "Better not to my face, [RogueX.player_petname]."
                    "I think I'll call you \"sex friend\".":

                        $ RogueX.petname = "sex friend"
                        if "sex friend" in RogueX.player_petnames or approval_check(RogueX, 600, "I"):
                            $ RogueX.change_face("sly")
                            ch_r "Rreow. . ."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "Hey, no need to advertise, [RogueX.player_petname]."
                    "I think I'll call you \"fuckbuddy\".":

                        $ RogueX.petname = "fuckbuddy"
                        if "fuckbuddy" in RogueX.player_petnames or approval_check(RogueX, 700, "I"):
                            $ RogueX.change_face("sly")
                            ch_r "That sounds about right, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            $ RogueX.mouth = "surprised"
                            ch_r "Inappropriate, [RogueX.player_petname]."
                    "I think I'll call you \"baby girl\".":

                        $ RogueX.petname = "baby girl"
                        if "daddy" in RogueX.player_petnames or approval_check(RogueX, 1200):
                            $ RogueX.change_face("smile", 1)
                            ch_r "You know it, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("angry", 1)
                            ch_r "I ain't your baby girl, [RogueX.player_petname]."
                    "Back":

                        pass
            "Nevermind.":

                return
    return




label Rogue_Rename:

    $ RogueX.mouth = "smile"
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



label Rogue_Personality(counter=0):
    if not RogueX.had_chat[4] or counter:
        "Since you're doing well in one area, you can convince [RogueX.name] to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_r "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if RogueX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_r "Well, I suppose for you I could be a bit more obedient."
            $ RogueX.had_chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if RogueX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_r "Well, I suppose for you I could be a bit less inhibited."
            $ RogueX.had_chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if RogueX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_r "Very well, I'll try to take more initiative."
            $ RogueX.had_chat[4] = 3
        "More Loving. [[Obedience to Love]" if RogueX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_r "If I must, I'll try to come around."
            $ RogueX.had_chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if RogueX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_r "Well, I guess it can be fun to try what you want too. . ."
            $ RogueX.had_chat[4] = 5

        "More Loving. [[Inhibition to Love]" if RogueX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_r "Well, I guess I am getting pretty attached. . ."
            $ RogueX.had_chat[4] = 6

        "I guess just do what you like. . .[[reset]" if RogueX.had_chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_r "Um, ok."
            $ RogueX.had_chat[4] = 0
        "Repeat the rules":
            call Rogue_Personality (1)
            return
        "Nevermind.":
            return
    return
