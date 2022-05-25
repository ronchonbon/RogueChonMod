

label Rogue_Relationship:
    while True:
        menu:
            ch_r "What did you want to ask me about?"
            "Do you want to be my girlfriend?" if RogueX not in Player.Harem and "ex" not in RogueX.traits:
                $ RogueX.daily_history.append("relationship")
                if "asked boyfriend" in RogueX.daily_history and "_angry" in RogueX.daily_history:
                    $ RogueX.change_face("_angry", 1)
                    ch_r "Seriously, stop bugging me."
                    return
                elif "asked boyfriend" in RogueX.daily_history:
                    $ RogueX.change_face("_angry", 1)
                    ch_r "You already asked about that, the answer's still no."
                    return
                elif RogueX.broken_up[0]:
                    $ RogueX.change_face("_angry", 1)
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
                    $ RogueX.change_face("_bemused", 1)
                    ch_r "I mean, I asked you about this before. . ."
                else:
                    $ RogueX.change_face("_surprised", 2)
                    ch_r "Wow, this is unexpected, [RogueX.player_petname]. . ."
                    $ RogueX.change_face("_smile", 1)

                call Rogue_OtherWoman

                if RogueX.love >= 800:
                    $ RogueX.change_face("_surprised", 1)
                    $ RogueX.mouth = "_grimace"
                    $ RogueX.change_stat("love", 200, 40)
                    ch_r "I'd love to!"
                    if "boyfriend" not in RogueX.player_petnames:
                        $ RogueX.player_petnames.append("boyfriend")
                    if "RogueYes" in Player.traits:
                        $ Player.traits.remove("RogueYes")
                    $ Player.Harem.append(RogueX)
                    call Harem_Initiation
                    "[RogueX.name] leaps in and kisses you deeply."
                    $ RogueX.change_face("_kiss", 1)
                    $ RogueX.action_counter["kiss"] += 1
                elif RogueX.obedience >= 500:
                    $ RogueX.change_face("_perplexed")
                    ch_r "I'm not sure I'd call what we have \"dating.\""
                elif RogueX.inhibition >= 500:
                    $ RogueX.change_face("_smile")
                    ch_r "I don't really want to be tied down like that."
                else:
                    $ RogueX.change_face("_perplexed", 1)
                    ch_r "I don't really feel that way about you right now, [RogueX.player_petname]."

            "Do you want to get back together?" if "ex" in RogueX.traits:
                $ RogueX.daily_history.append("relationship")
                if "asked boyfriend" in RogueX.daily_history and "_angry" in RogueX.daily_history:
                    $ RogueX.change_face("_angry", 1)
                    ch_r "Seriously, stop bugging me."
                    return
                elif "asked boyfriend" in RogueX.daily_history:
                    $ RogueX.change_face("_angry", 1)
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
                    $ RogueX.change_face("_surprised", 1)
                    $ RogueX.mouth = "_grimace"
                    $ RogueX.change_stat("love", 90, 5)
                    ch_r "If you're in, I'm in!"
                    if "boyfriend" not in RogueX.player_petnames:
                        $ RogueX.player_petnames.append("boyfriend")
                    $ RogueX.traits.remove("ex")
                    if "RogueYes" in Player.traits:
                        $ Player.traits.remove("RogueYes")
                    $ Player.Harem.append(RogueX)
                    call Harem_Initiation
                    "[RogueX.name] leaps in and kisses you deeply."
                    $ RogueX.change_face("_kiss", 1)
                    $ RogueX.action_counter["kiss"] += 1
                elif RogueX.love >= 600 and approval_check(RogueX, 1500):
                    $ RogueX.change_face("_smile", 1)
                    $ RogueX.mouth = "_grimace"
                    $ RogueX.change_stat("love", 90, 5)
                    ch_r "We can give this another try."
                    if "boyfriend" not in RogueX.player_petnames:
                        $ RogueX.player_petnames.append("boyfriend")
                    $ RogueX.traits.remove("ex")
                    if "RogueYes" in Player.traits:
                        $ Player.traits.remove("RogueYes")
                    $ Player.Harem.append(RogueX)
                    call Harem_Initiation
                    "[RogueX.name] gives you a quick kiss."
                    $ RogueX.change_face("_kiss", 1)
                    $ RogueX.action_counter["kiss"] += 1
                elif RogueX.obedience >= 500:
                    $ RogueX.change_face("_sad")
                    ch_r "Whatever we had, whatever we have right now, that's not it."
                elif RogueX.inhibition >= 500:
                    $ RogueX.change_face("_perplexed")
                    ch_r "We tried that, it didn't work out."
                else:
                    $ RogueX.change_face("_perplexed", 1)
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
                    "You weren't a virgin?" if RogueX.action_counter["sex"] and not RogueX.had_chat[0]:
                        call Rogue_Not_Virgin

                    "You said you wanted me to be your Master?" if RogueX.event_happened[8] and "master" not in RogueX.player_petnames:
                        menu:
                            ch_r "Yes?"
                            "I'm ok with that now.":
                                if approval_check(RogueX, 800, "O"):
                                    $ RogueX.change_face("_sexy", 1)
                                    ch_r "I hope to serve well, Master."
                                    $ RogueX.change_stat("obedience", 200, 100)
                                    $ RogueX.player_petnames.append("master")
                                    $ RogueX.event_happened[8] = 2
                                else:
                                    ch_r "Well, I'm not really interested in that sort of thing anymore."
                                    ch_r "I mean, maybe later."
                            "Never mind.":
                                $ RogueX.change_face("_sad")
                                ch_r "Oh."
                                $ RogueX.change_stat("obedience", 200, -5)
                                $ RogueX.change_stat("love", 90, -5)
                    "Never Mind":
                        pass
            "Never Mind":
                return
        return


label Rogue_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((RogueX.likes[Player.Harem[0].tag] - 500)/2)

    $ RogueX.change_face("_perplexed")
    if len(Player.Harem) >= 2:
        ch_r "But you're with [Player.Harem[0].name] right now, and a whole mess'a other girls!"
    else:
        ch_r "But you're with [Player.Harem[0].name]!"
    menu:
        extend ""
        "She said I can be with you too." if "RogueYes" in Player.traits:
            if approval_check(RogueX, 1800, Bonus = counter):
                $ RogueX.change_face("_smile", 1)
                if RogueX.love >= RogueX.obedience:
                    ch_r "I s'pose I can learn ta share."
                elif RogueX.obedience >= RogueX.inhibition:
                    ch_r "Well I won't be the one to get in the way a this."
                else:
                    ch_r "Ok, sure."
            else:
                $ RogueX.change_face("_angry", 1)
                ch_r "Well that harlot!"
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "RogueYes" not in Player.traits:
            if approval_check(RogueX, 1800, Bonus = counter):
                $ RogueX.change_face("_smile", 1)
                if RogueX.love >= RogueX.obedience:
                    ch_r "I s'pose I can learn ta share."
                elif RogueX.obedience >= RogueX.inhibition:
                    ch_r "Well I won't be the one to get in the way a this."
                else:
                    ch_r "Ok, sure."
                ch_r "You go ask her if she's inta that, then get back to me tomorrow."
            else:
                $ RogueX.change_face("_angry", 1)
                ch_r "Well that harlot!"
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(RogueX, 1800, Bonus = -counter):
                $ RogueX.change_face("_angry", 1)
                if not approval_check(RogueX, 1800):
                    ch_r "Well now I don't wantcha."
                else:
                    ch_r "I ain't in a sharin mood."
                $ renpy.pop_call()
            else:
                $ RogueX.change_face("_smile", 1)
                if RogueX.love >= RogueX.obedience:
                    ch_r "I s'pose somethin could be arranged. . ."
                elif RogueX.obedience >= RogueX.inhibition:
                    ch_r "If you insist."
                else:
                    ch_r "Don't see why not."
                $ RogueX.add_word(1,0,0,"downlow")
        "I can break it off with her.":

            $ RogueX.change_face("_sad")
            ch_r "Well then talk to me after you have."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ RogueX.change_face("_sad")
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

                $ RogueX.change_face("_sly",1)
                if "monogamous" not in RogueX.daily_history:
                    $ RogueX.change_stat("obedience", 90, -2)
                ch_r "I might consider that, but you don't exactly make yourself available. . ."
                return
            elif approval_check(RogueX, 1200, "LO", taboo_modifier=0) and RogueX.love >= RogueX.obedience:

                $ RogueX.change_face("_sly",1)
                if "monogamous" not in RogueX.daily_history:
                    $ RogueX.change_stat("love", 90, 1)
                ch_r "Aw, would that make you jealous?"
                ch_r "I suppose I could restain myself. . ."
            elif approval_check(RogueX, 700, "O", taboo_modifier=0):

                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "If that's what you really want. . ."
            else:

                $ RogueX.change_face("_sly",1,brows="_confused")
                ch_r "Who I \"hook up\" with is my own damned business."
                return
            if "monogamous" not in RogueX.daily_history:
                $ RogueX.change_stat("obedience", 90, 3)
            $ RogueX.add_word(1,0,"monogamous","monogamous")
        "Don't hook up with other girls." if "monogamous" not in RogueX.traits:
            if approval_check(RogueX, 900, "O", taboo_modifier=0):

                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "Ok."
            elif RogueX.thirst >= 60 and not approval_check(RogueX, 1700, "LO", taboo_modifier=0):

                $ RogueX.change_face("_sly",1)
                if "monogamous" not in RogueX.daily_history:
                    $ RogueX.change_stat("obedience", 90, -2)
                ch_r "I might consider that, but you don't exactly make yourself available. . ."
                return
            elif approval_check(RogueX, 550, "O", taboo_modifier=0):

                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "If that's what you really want. . ."
            elif approval_check(RogueX, 1400, "LO", taboo_modifier=0):

                $ RogueX.change_face("_sly",1)
                ch_r "Is that any way to ask a girl?"
                ch_r "Still, I'll do it for you. . ."
            else:

                $ RogueX.change_face("_sly",1,brows="_confused")
                ch_r "Who I \"hook up\" with is my own damned business."
                return
            if "monogamous" not in RogueX.daily_history:
                $ RogueX.change_stat("obedience", 90, 3)
            $ RogueX.add_word(1,0,"monogamous","monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in RogueX.traits:
            if approval_check(RogueX, 700, "O", taboo_modifier=0):
                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "As you wish."
            elif approval_check(RogueX, 800, "L", taboo_modifier=0):
                $ RogueX.change_face("_sly",1)
                ch_r "I hope you don't give me any reasons to want to. . ."
            else:
                $ RogueX.change_face("_sly",1,brows="_confused")
                if "monogamous" not in RogueX.daily_history:
                    $ RogueX.change_stat("love", 90, -2)
                ch_r "Oh? Well, glad I got your permission there."
            if "monogamous" not in RogueX.daily_history:
                $ RogueX.change_stat("obedience", 90, 3)
            if "monogamous" in RogueX.traits:
                $ RogueX.traits.remove("monogamous")
            $ RogueX.add_word(1,0,"monogamous")
        "Never mind.":
            pass
    return




label Rogue_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ RogueX.change_face("_sly",1,brows="_confused")
    menu:
        ch_r "Yeah?"
        "Could you maybe just ask instead?" if "chill" not in RogueX.traits:
            if RogueX.thirst >= 60 and not approval_check(RogueX, 1500, "LO", taboo_modifier=0):

                $ RogueX.change_face("_sly",1)
                if "chill" not in RogueX.daily_history:
                    $ RogueX.change_stat("obedience", 90, -2)
                ch_r "Maybe don't keep me waiting then. . ."
                return
            elif approval_check(RogueX, 1000, "LO", taboo_modifier=0) and RogueX.love >= RogueX.obedience:

                $ RogueX.change_face("_sly",1)
                if "chill" not in RogueX.daily_history:
                    $ RogueX.change_stat("love", 90, 1)
                ch_r "Sorry, [RogueX.player_petname], I just got a little lonely. . ."
                ch_r "I'll be good. . ."
            elif approval_check(RogueX, 500, "O", taboo_modifier=0):

                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "If that's what you really want. . ."
            else:

                $ RogueX.change_face("_sly",1,brows="_confused")
                ch_r "I can't make any promises."
                return
            if "chill" not in RogueX.daily_history:
                $ RogueX.change_stat("obedience", 90, 3)
            $ RogueX.add_word(1,0,"chill","chill")
        "Don't bother me like that." if "chill" not in RogueX.traits:
            if approval_check(RogueX, 900, "O", taboo_modifier=0):

                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "Ok."
            elif RogueX.thirst >= 60 and not approval_check(RogueX, 600, "O", taboo_modifier=0):

                $ RogueX.change_face("_sly",1)
                if "chill" not in RogueX.daily_history:
                    $ RogueX.change_stat("obedience", 90, -2)
                ch_r "Maybe don't keep me waiting then. . ."
                return
            elif approval_check(RogueX, 450, "O", taboo_modifier=0):

                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "If that's what you really want. . ."
            elif approval_check(RogueX, 500, "LO", taboo_modifier=0) and not approval_check(RogueX, 500, "I", taboo_modifier=0):

                $ RogueX.change_face("_sly",1)
                ch_r "You might want to watch your mouth."
                ch_r "Still, I'll try to keep to myself. . ."
            else:

                $ RogueX.change_face("_sly",1,brows="_confused")
                ch_r "No promises."
                return
            if "chill" not in RogueX.daily_history:
                $ RogueX.change_stat("obedience", 90, 3)
            $ RogueX.add_word(1,0,"chill","chill")
        "Knock yourself out.":
            if approval_check(RogueX, 800, "L", taboo_modifier=0):
                $ RogueX.change_face("_sly",1)
                ch_r "Will do. . ."
            elif approval_check(RogueX, 700, "O", taboo_modifier=0):
                $ RogueX.change_face("_sly",1,eyes="_side")
                ch_r "Yes sir."
            else:
                $ RogueX.change_face("_sly",1,brows="_confused")
                if "chill" not in RogueX.daily_history:
                    $ RogueX.change_stat("love", 90, -2)
                ch_r "Maybe. If I've got nothing better to do."
            if "chill" not in RogueX.daily_history:
                $ RogueX.change_stat("obedience", 90, 3)
            if "chill" in RogueX.traits:
                $ RogueX.traits.remove("chill")
            $ RogueX.add_word(1,0,"chill")
        "Um, never mind.":
            pass
    return





label Rogue_Not_Virgin:
    menu:
        "I noticed that when we had sex, you didn't seem to be a virgin."
        "Wasn't I your first time?":
            $ RogueX.change_face("_bemused", 1)
            $ RogueX.change_stat("love", 60, 5)
            $ RogueX.change_stat("obedience", 20, 15)
            ch_r "Oh, no! You definitely were, it's just. . . you know,"
            ch_r "I lead a pretty active lifestyle, so I lost that physical barrier years ago."
        "So you get around?":
            $ RogueX.change_face("_sexy", 1)
            $ RogueX.brows = "_angry"
            $ RogueX.change_stat("obedience", 30, 15)
            $ RogueX.change_stat("obedience", 60, 5)
            $ RogueX.change_stat("inhibition", 30, 15)
            $ RogueX.change_stat("inhibition", 60, 5)
            ch_r "Jerk, not like that. I tore it years ago in combat training."
        "Are you a slut?":
            $ RogueX.change_face("_angry", 1)
            $ RogueX.change_stat("love", 30, -20, 1)
            $ RogueX.change_stat("love", 60, -40, 1)
            $ RogueX.change_stat("obedience", 30, 30)
            $ RogueX.change_stat("obedience", 60, 20)
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





label Rogue_sexchat:
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
                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "sex":
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "Yeah, I know that. . ."
                            elif RogueX.favorite_action == "sex":
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 10)
                                ch_r "Oooh, I love a good pipe cleaning too. . ."
                            elif RogueX.action_counter["sex"] >= 5:
                                ch_r "Can't say as I mind a good roll in the hay."
                            elif not RogueX.action_counter["sex"]:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} are y'all having sex {i}with?{/i}"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "Heh, [RogueX.player_petname], flithy mouth on you. . ."
                            $ RogueX.player_favorite_action = "sex"
                        "Anal.":

                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "anal":
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "So I hear. . ."
                            elif RogueX.favorite_action == "anal":
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 10)
                                ch_r "I can't say as I mind that. . ."
                            elif RogueX.action_counter["anal"] >= 10:
                                ch_r "It's not a bad way to spend some time. . ."
                            elif not RogueX.action_counter["anal"]:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} are y'all fucking {i}with?{/i}"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "Heh, heh, I . . . I don't {i}mind{/i} it. . ."
                            $ RogueX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "blowjob":
                                $ RogueX.change_stat("lust", 80, 3)
                                ch_r "I'm not surprised. . ."
                            elif RogueX.favorite_action == "blowjob":
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "I guess I have developed a real taste for you. . ."
                            elif RogueX.action_counter["blowjob"] >= 10:
                                ch_r "I'm getting to enjoy it too . . ."
                            elif not RogueX.action_counter["blowjob"]:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} is sucking you off?"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "I'm. . . getting used to the taste. . ."
                            $ RogueX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "titjob":
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "So I hear. . ."
                            elif RogueX.favorite_action == "titjob":
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 7)
                                ch_r "I really enjoy it too. . ."
                            elif RogueX.action_counter["titjob"] >= 10:
                                ch_r "It's certainly an interesting experience . . ."
                            elif not RogueX.action_counter["titjob"]:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} is tit fucking you?"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "I can't say as I blame you. . ."
                            $ RogueX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "footjob":
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "Yeah, you've said that before. . ."
                            elif RogueX.favorite_action == "footjob":
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 7)
                                ch_r "I do enjoy that sensation. . ."
                            elif RogueX.action_counter["footjob"] >= 10:
                                ch_r "It is pretty nice to touch someone like that . . ."
                            elif not RogueX.action_counter["footjob"]:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} is jerking you off?"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "I do like the sensation. . ."
                            $ RogueX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "handjob":
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "Yeah, you've said that before. . ."
                            elif RogueX.favorite_action == "handjob":
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 7)
                                ch_r "I love how you feel in my hand. . ."
                            elif RogueX.action_counter["handjob"] >= 10:
                                ch_r "It is pretty nice to touch someone like that . . ."
                            elif not RogueX.action_counter["handjob"]:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} is jerking you off?"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "I do like the sensation. . ."
                            $ RogueX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = RogueX.action_counter["fondle_breasts"]+ RogueX.action_counter["fondle_thighs"]+ RogueX.action_counter["suck_breasts"] + RogueX.action_counter["hotdog"]
                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "fondle":
                                $ RogueX.change_stat("lust", 80, 3)
                                ch_r "Yeah, I think we've established that. . ."
                            elif RogueX.favorite_action in ("hotdog","suck_breasts","fondle_breasts","fondle_thighs"):
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "I love how you touch me. . ."
                            elif counter >= 10:
                                ch_r "It's nice to have someone who can really touch me . . ."
                            elif not counter:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} are you feeling up?"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "I do like how that feels. . ."
                            $ RogueX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ RogueX.change_face("_sly")
                            if RogueX.player_favorite_action == "kiss":
                                $ RogueX.change_stat("love", 90, 3)
                                ch_r "I've heard it before, but don't mind hearing it again. . ."
                            elif RogueX.favorite_action == "kiss":
                                $ RogueX.change_stat("love", 90, 5)
                                $ RogueX.change_stat("lust", 80, 5)
                                ch_r "I can't get over your lips either. . ."
                            elif RogueX.action_counter["kiss"] >= 10:
                                ch_r "I love kissing you too . . ."
                            elif not RogueX.action_counter["kiss"]:
                                $ RogueX.change_face("_perplexed")
                                ch_r "Who {i}exactly{/i} are you smooch'in?"
                            else:
                                $ RogueX.change_face("_bemused")
                                ch_r "It's nice being able to kiss someone without hurting them. . ."
                            $ RogueX.player_favorite_action = "kiss"

                    $ RogueX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(RogueX, 800):
                    $ RogueX.change_face("_perplexed")
                    ch_r "I don't think that's any of your business. . ."
                else:
                    if RogueX.SEXP >= 50:
                        $ RogueX.change_face("_sly")
                        ch_r "If you can't tell. . ."
                    else:
                        $ RogueX.change_face("_bemused")
                        $ RogueX.eyes = "_side"
                        ch_r "I don't know, I guess maybe. . ."


                    if not RogueX.favorite_action or RogueX.favorite_action == "kiss":
                        ch_r "I guess I love it when we kiss. . ."
                    elif RogueX.favorite_action == "anal":
                        if RogueX.action_counter["anal"] >= 10:
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
                    $ RogueX.change_face("_perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("_bemused")
                        $ RogueX.change_stat("obedience", 90, 1)
                        ch_r "Heh, ok, if that's what you want. . ."
                        $ RogueX.traits.remove("vocal")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("_sadside")
                        $ RogueX.change_stat("obedience", 90, 1)
                        ch_r "If that's what you want, [RogueX.player_petname]."
                        $ RogueX.traits.remove("vocal")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("_sly")
                        $ RogueX.change_stat("love", 90, -3)
                        $ RogueX.change_stat("obedience", 50, -1)
                        $ RogueX.change_stat("inhibition", 90, 5)
                        ch_r "I'll say what I want, and you'll like it, [RogueX.player_petname]."
                    else:
                        $ RogueX.change_face("_angry")
                        $ RogueX.change_stat("love", 90, -5)
                        $ RogueX.change_stat("obedience", 60, -3)
                        $ RogueX.change_stat("inhibition", 90, 10)
                        ch_r "Fuck you, I'll talk as much as I want."

                    $ RogueX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in RogueX.traits:
                if "setvocal" in RogueX.daily_history:
                    $ RogueX.change_face("_perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("_sly")
                        $ RogueX.change_stat("obedience", 90, 2)
                        ch_r "Heh, ok, if that's what you want. . ."
                        $ RogueX.traits.append("vocal")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("_sadside")
                        $ RogueX.change_stat("obedience", 90, 2)
                        ch_r "If that's what you want, [RogueX.player_petname]."
                        $ RogueX.traits.append("vocal")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("_sly")
                        $ RogueX.change_stat("obedience", 90, 3)
                        ch_r "I can give it a shot, [RogueX.player_petname]."
                        $ RogueX.traits.append("vocal")
                    else:
                        $ RogueX.change_face("_angry")
                        $ RogueX.change_stat("inhibition", 90, 5)
                        ch_r "I'll say what I want, when I want."

                    $ RogueX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in RogueX.traits:
                if "initiative" in RogueX.daily_history:
                    $ RogueX.change_face("_perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("_bemused")
                        $ RogueX.change_stat("obedience", 90, 1)
                        ch_r "Heh, ok, lead the way. . ."
                        $ RogueX.traits.append("passive")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("_sadside")
                        $ RogueX.change_stat("obedience", 90, 1)
                        ch_r "I'll restrain myself then, [RogueX.player_petname]."
                        $ RogueX.traits.append("passive")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("_sly")
                        $ RogueX.change_stat("love", 90, -3)
                        $ RogueX.change_stat("obedience", 50, -1)
                        $ RogueX.change_stat("inhibition", 90, 5)
                        ch_r "You know you don't want that, [RogueX.player_petname]."
                    else:
                        $ RogueX.change_face("_angry")
                        $ RogueX.change_stat("love", 90, -5)
                        $ RogueX.change_stat("obedience", 60, -3)
                        $ RogueX.change_stat("inhibition", 90, 10)
                        ch_r "I'll do what I want, prick."

                    $ RogueX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in RogueX.traits:
                if "initiative" in RogueX.daily_history:
                    $ RogueX.change_face("_perplexed")
                    ch_r "We've been over this already."
                else:
                    if approval_check(RogueX, 1000) and RogueX.obedience <= RogueX.love:
                        $ RogueX.change_face("_bemused")
                        $ RogueX.change_stat("obedience", 90, 1)
                        ch_r "Heh, I think I can handle that. . ."
                        $ RogueX.traits.remove("passive")
                    elif approval_check(RogueX, 700, "O"):
                        $ RogueX.change_face("_sadside")
                        $ RogueX.change_stat("obedience", 90, 1)
                        ch_r "I can do that, [RogueX.player_petname]."
                        $ RogueX.traits.remove("passive")
                    elif approval_check(RogueX, 600):
                        $ RogueX.change_face("_sly")
                        $ RogueX.change_stat("obedience", 90, 3)
                        ch_r "I can certainly try, [RogueX.player_petname]."
                        $ RogueX.traits.remove("passive")
                    else:
                        $ RogueX.change_face("_angry")
                        $ RogueX.change_stat("inhibition", 90, 5)
                        ch_r "If I want to, I will, but not because you say so."

                    $ RogueX.daily_history.append("initiative")

            "About getting Jumped" if "jumped" in RogueX.history:
                call Rogue_Jumped
            "About when you masturbate":
                call NoFap (RogueX)

            "Never Mind" if line == "Yeah, what did you want to talk about?":
                return
            "That's all." if line != "Yeah, what did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return





label Rogue_Chitchat(O=0, Options=["default","default","default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:
        if RogueX not in phonebook:
            if approval_check(RogueX, 500, "L") or approval_check(RogueX, 250, "I"):
                ch_r "You know, I never got around to giving you my number, here you go."
                $ phonebook.append(RogueX)
                return
            elif approval_check(RogueX, 250, "O"):
                ch_r "You know, you should probably have my number, here you go."
                $ phonebook.append(RogueX)
                return
        if "hungry" not in RogueX.traits and (RogueX.event_counter["swallowed"] + RogueX.had_chat[2]) >= 10 and RogueX.location == bg_current:
            call Rogue_Hungry
            return
        if bg_current != "bg_restaurant" and bg_current != "HW Party" and (not taboo or approval_check(RogueX, 800, "I")):
            if RogueX.location == bg_current and RogueX.thirst >= 30 and "refused" not in RogueX.daily_history and "quicksex" not in RogueX.daily_history:
                $ RogueX.change_face("_sly",1)
                ch_r "Hey, do you want to get a little frisky?"
                call Quick_Sex (RogueX)
                return


        if approval_check(RogueX, 1200) and bg_current == RogueX.location and bg_current != "bg_restaurant":
            $ Options.append("dance")
        if approval_check(RogueX, 800, "L") and "nametag chat" not in RogueX.daily_history:
            $ Options.append("close")
        if RogueX.action_counter["blowjob"] >= 2:
            $ Options.append("blowjob")
        if "steal" in RogueX.traits:
            $ Options.append("steal")
        if being_punished and "caught chat" not in RogueX.daily_history:
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

        if not RogueX.had_chat[0] and RogueX.action_counter["sex"]:
            $ Options.append("virgin")

        if "seenpeen" in RogueX.history:
            $ Options.append("seenpeen")
        if "topless" in RogueX.history:
            $ Options.append("topless")
        if "bottomless" in RogueX.history:
            $ Options.append("bottomless")

        if "lover" in RogueX.player_petnames and "Anna" not in RogueX.names:

            $ Options.append("annamarie")

        if (bg_current == "bg_rogue" or bg_current == "bg_player") and "nametag chat" not in RogueX.daily_history:
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
        $ RogueX.change_face("_confused")
        ch_r "(sniff, sniff). . . something kind of smells like monkey butt in here. . ."
        $ RogueX.change_face("_sly", 1)
        ch_r ". . . but you're looking pretty handsome today, [RogueX.player_petname]."
    elif Options[0] == "purple":
        $ RogueX.daily_history.append("cologne chat")
        $ RogueX.change_face("_sly",1)
        ch_r "(sniff, sniff). . . hmm, you're smelling good today. . ."
        ch_r ". . . was there anything I could do to make you happy?"
    elif Options[0] == "corruption":
        $ RogueX.daily_history.append("cologne chat")
        $ RogueX.change_face("_confused")
        ch_r "(sniff, sniff). . . that's a pretty strong scent you've got there. . ."
        $ RogueX.change_face("_sly")
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
        call Rogue_Sex_Launch ("massage")
        if RogueX.outfit["bottom"] == "_skirt":
            $ RogueX.upskirt = 1
            if RogueX.outfit["underwear"] and RogueX.seen_underwear and approval_check(RogueX, 800, taboo_modifier = 3):
                pass
            elif RogueX.outfit["underwear"] and approval_check(RogueX, 800, taboo_modifier = 3):
                $ RogueX.seen_underwear = 1
            elif RogueX.outfit["underwear"]:
                $ RogueX.upskirt = 0
            elif RogueX.seen_pussy and approval_check(RogueX, 1000, taboo_modifier = 4):
                pass
            elif approval_check(RogueX, 1400, taboo_modifier = 3):
                call Rogue_First_Bottomless (1)
            else:
                $ RogueX.upskirt = 0
            pause 0.5
            $ RogueX.upskirt = 0
        ch_r "Y'know what I'm sayin', [RogueX.player_petname]?"
        $ RogueX.upskirt = 0
        call Rogue_Doggy_Reset

    elif Options[0] == "seenpeen":
        $ RogueX.change_face("_sly",1)
        ch_r "You really did surprise me when you whipped that cock out."
        ch_r "I didn't know they looked so big up close."
        $ RogueX.change_face("_bemused",1)
        $ RogueX.change_stat("love", 90, 5)
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
        $ RogueX.change_face("_bemused", 1)
        ch_r ". . ."
        ch_r "You know, time was, I really thought I'd end up alone, unable to touch anyone. . ."
        $ RogueX.change_face("_smile")
        ch_r "I'm really glad that I was able to find you."
        ch_r "I love you, [RogueX.player_petname]."
        menu:
            extend ""
            "I love you too.":
                $ RogueX.change_stat("love", 200, 10)
                $ RogueX.change_stat("obedience", 80, 4)
                $ RogueX.change_stat("inhibition", 80, 4)
            "I love you too, [RogueX.petname].":
                $ RogueX.name_check()
                if _return:
                    $ RogueX.change_face("_angry")
                    $ RogueX.change_stat("love", 90, -1)
                    $ RogueX.change_stat("obedience", 80, 10)
                    $ RogueX.change_stat("inhibition", 80, 4)
                else:
                    $ RogueX.change_stat("love", 200, 10)
                    $ RogueX.change_stat("obedience", 80, 4)
                    $ RogueX.change_stat("inhibition", 80, 4)
            "Yeah, same here.":
                $ RogueX.change_face("_perplexed")
                $ RogueX.change_stat("love", 90, -1)
                $ RogueX.change_stat("obedience", 80, 10)
                $ RogueX.change_stat("inhibition", 80, 4)
            "Whatever.":
                $ RogueX.change_face("_angry")
                $ RogueX.change_stat("love", 200, -10)
                $ RogueX.change_stat("obedience", 80, 4)
                $ RogueX.change_stat("inhibition", 80, 10)

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
        call Rogue_sexfriend
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
            $ RogueX.change_face("_confused")
            ch_r "I'm so nervous about this Genetics test with Professor McCoy. I don't get this stuff at all."
        elif D20 == 2:
            $ RogueX.change_face("_sad")
            ch_r "Feeling kinda down today, [RogueX.player_petname]. Family problems. It's. . .kinda complicated."
        elif D20 == 3:
            $ RogueX.change_face("_sly")
            ch_r "So, um. . .maybe you heard about the friends I used to hang out with? They're not all as bad as they seem. Mostly."
        elif D20 == 4:
            $ RogueX.change_face("_smile")
            ch_r "I had the best workout earlier in the Danger Room today! Wish you coulda seen me!"
        elif D20 == 5:
            $ RogueX.change_face("_smile")
            ch_r "Ever wonder what it would be like to be able to fly? That's gotta be the coolest power, right?"
        elif D20 == 6:
            $ RogueX.change_face("_smile")
            ch_r "Ever been out to Breakstone Lake, behind the Mansion? It's so nice and peaceful. Kinda reminds me of back home in Mississippi, during the summer. Just a little chillier."
        elif D20 == 7:
            $ RogueX.change_face("_smile")
            $ RogueX.eyes = "_surprised"
            ch_r "I just saw the coolest thing, when I was walking through the courtyard! A bunch of deer, in the woods, just over by the fence!"
            $ RogueX.eyes = "_side"
            ch_r "Their fur looked so. . .{i}soft{/i}. I wonder what they actually feel like?"
        elif D20 == 8:
            $ RogueX.change_face("_smile")
            ch_r "Hey, did you see the Avengers on the news this morning? Those guys make everything look {i}so{/i} easy!"
        elif D20 == 9:
            $ RogueX.change_face("_smile")
            ch_r "A couple of us are gonna get together and go for a jog around one of the Mansion's sub-basements tomorrow. You should come with us!"
        elif D20 == 10:
            $ RogueX.change_face("_down")
            ch_r "I have {i}so{/i} much homework this week! And I {i}so{/i} don't feel like doing any of it!"
        elif D20 == 11:
            $ RogueX.change_face("startled")
            ch_r "Y'know, I {i}really{/i} hate my powers. But could you imagine having Professor Xavier's?"
            ch_r "I don't know if I could handle that kind of responsibility."
            ch_r "Might be even worse than mine, in their own way."
        elif D20 == 12:
            $ RogueX.change_face("_sad")
            ch_r "The Mansion's a great place to live. . .but sometimes I get weirded out when I think how we could get attacked by some super-maniac any given second."
        elif D20 == 13:
            $ RogueX.change_face("_smile")
            ch_r "I love it when you get a really good night's sleep. Feels amazing!"
        elif D20 == 14:
            $ RogueX.change_face("_bemused")
            ch_r "I heard they're thinking about maybe having a school dance this year. That could be. . .{i}interesting{/i}."
        elif D20 == 15:
            $ RogueX.change_face("_smile")
            ch_r "You been outside today? Wow, is it gorgeous!"
        elif D20 == 16:
            $ RogueX.change_face("_smile")
            ch_r "You know, I tagged Wolverine once,"
            $ RogueX.change_face("_sadside")
            $ RogueX.brows = "_confused"
            ch_r "I still catch myself calling people \"bub\" from time to time."
        else:
            $ RogueX.change_face("_smile")
            ch_r "I like hanging out with you like this!"
    $ line = 0
    return


label Rogue_names:

    if approval_check(RogueX, 600, "L", taboo_modifier=0) or approval_check(RogueX, 300, "O", taboo_modifier=0):
        pass
    else:
        $ RogueX.mouth = "_smile"
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
                            $ RogueX.change_face("_sexy", 1)
                            ch_r "I sure am your girl, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry")
                            ch_r "I ain't your girl, [RogueX.player_petname]."
                    "I think I'll call you \"boo\".":

                        $ RogueX.petname = "boo"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            $ RogueX.change_face("_sexy", 1)
                            ch_r "Aw, I am your boo, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry")
                            ch_r "I ain't your boo, [RogueX.player_petname]."
                    "I think I'll call you \"bae\".":

                        $ RogueX.petname = "bae"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            $ RogueX.change_face("_sexy", 1)
                            ch_r "Aw, I am your bae, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry")
                            ch_r "I ain't your bae, [RogueX.player_petname]."
                    "I think I'll call you \"baby\".":

                        $ RogueX.petname = "baby"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            $ RogueX.change_face("_sexy", 1)
                            ch_r "Aw, cute, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry")
                            ch_r "I ain't your baby, [RogueX.player_petname]."
                    "I think I'll call you \"chere\".":

                        $ RogueX.petname = "chere"
                        if "lover" in RogueX.player_petnames or approval_check(RogueX, 600, "L"):
                            $ RogueX.change_face("_sexy", 1)
                            ch_r "Oh, tre romantic, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            $ RogueX.eyes = "_side"
                            ch_r "That has some. . . bad memories, [RogueX.player_petname]."
                    "I think I'll call you \"sweetie\".":

                        $ RogueX.petname = "sweetie"
                        if "boyfriend" in RogueX.player_petnames or approval_check(RogueX, 500, "L"):
                            ch_r "Aw, that's sweet, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "That's a bit much, [RogueX.player_petname]."
                    "I think I'll call you \"sexy\".":

                        $ RogueX.petname = "_sexy"
                        if "lover" in RogueX.player_petnames or approval_check(RogueX, 900):
                            $ RogueX.change_face("_sexy", 1)
                            ch_r "You're not so bad yourself, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "Inappropriate, [RogueX.player_petname]."
                    "I think I'll call you \"lover\".":

                        $ RogueX.petname = "lover"
                        if "lover" in RogueX.player_petnames or approval_check(RogueX, 900):
                            $ RogueX.change_face("_sexy", 1)
                            ch_r "Oh, I love you too, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "Not any time soon, [RogueX.player_petname]."
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you \"slave\".":
                        $ RogueX.petname = "slave"
                        if "master" in RogueX.player_petnames or approval_check(RogueX, 700, "O"):
                            $ RogueX.change_face("_bemused", 1)
                            ch_r "As you wish, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "I ain't anyone's slave, [RogueX.player_petname]."
                    "I think I'll call you \"pet\".":

                        $ RogueX.petname = "pet"
                        if "master" in RogueX.player_petnames or approval_check(RogueX, 600, "O"):
                            $ RogueX.change_face("_bemused", 1)
                            ch_r "Hmm, make sure to pet me, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "I ain't your pet, [RogueX.player_petname]."
                    "I think I'll call you \"slut\".":

                        $ RogueX.petname = "slut"
                        if "sex friend" in RogueX.player_petnames or approval_check(RogueX, 1000, "OI"):
                            $ RogueX.change_face("_sexy")
                            ch_r "You know me too well, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            $ RogueX.mouth = "_surprised"
                            ch_r "Well I never!"
                    "I think I'll call you \"whore\".":

                        $ RogueX.petname = "whore"
                        if "fuckbuddy" in RogueX.player_petnames or approval_check(RogueX, 1100, "OI"):
                            $ RogueX.change_face("_sly")
                            ch_r "I guess I am. . ."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "You look'in to start something, [RogueX.player_petname]?"
                    "I think I'll call you \"sugartits\".":

                        $ RogueX.petname = "sugartits"
                        if "sex friend" in RogueX.player_petnames or approval_check(RogueX, 1500):
                            $ RogueX.change_face("_sly", 1)
                            ch_r "Heh."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "Better not to my face, [RogueX.player_petname]."
                    "I think I'll call you \"sex friend\".":

                        $ RogueX.petname = "sex friend"
                        if "sex friend" in RogueX.player_petnames or approval_check(RogueX, 600, "I"):
                            $ RogueX.change_face("_sly")
                            ch_r "Rreow. . ."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "Hey, no need to advertise, [RogueX.player_petname]."
                    "I think I'll call you \"fuckbuddy\".":

                        $ RogueX.petname = "fuckbuddy"
                        if "fuckbuddy" in RogueX.player_petnames or approval_check(RogueX, 700, "I"):
                            $ RogueX.change_face("_sly")
                            ch_r "That sounds about right, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            $ RogueX.mouth = "_surprised"
                            ch_r "Inappropriate, [RogueX.player_petname]."
                    "I think I'll call you \"baby girl\".":

                        $ RogueX.petname = "baby girl"
                        if "daddy" in RogueX.player_petnames or approval_check(RogueX, 1200):
                            $ RogueX.change_face("_smile", 1)
                            ch_r "You know it, [RogueX.player_petname]."
                        else:
                            $ RogueX.change_face("_angry", 1)
                            ch_r "I ain't your baby girl, [RogueX.player_petname]."
                    "Back":

                        pass
            "Nevermind.":

                return
    return




label Rogue_Rename:

    $ RogueX.mouth = "_smile"
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





label Rogue_Summon(approval_bonus=approval_bonus):
    $ RogueX.change_outfit()
    if "no_summon" in RogueX.recent_history:

        if "_angry" in RogueX.recent_history:
            ch_r "What part of \"no\" don't you understand?"
        elif RogueX.recent_history.count("no_summon") > 1:
            ch_r "I already told you no, take a hint."
            $ RogueX.recent_history.append("_angry")
        elif time_index >= 3:
            ch_r "I told you it was too late for that tonight."
        else:
            ch_r "I told you I was busy."
        $ RogueX.recent_history.append("no_summon")
        return

    $ D20 = renpy.random.randint(1, 20)
    $ line = 0
    if RogueX.location == "bg_classroom":
        $ approval_bonus = -10
    elif RogueX.location == "bg_dangerroom":
        $ approval_bonus = -20
    elif RogueX.location == "bg_showerroom":
        $ approval_bonus = -40

    if D20 <= 3:

        $ line = "no"
    elif "lesbian" in RogueX.recent_history:

        if approval_check(RogueX, 2000):
            ch_r "I'm enjoying some company right now, [RogueX.player_petname], care to join us?"
            menu:
                extend ""
                "Sure":
                    $ line = "go to"
                "No thanks.":
                    ch_r "Suit yourself."
                    return
        else:
            ch_r "What? Um, no, um, not right now."
            ch_r "Maybe we could touch base later."
            $ RogueX.recent_history.append("no_summon")
            return
    elif time_index >= 3:
        if approval_check(RogueX, 700, "L") or approval_check(RogueX, 300, "O"):

            ch_r "Ok, it's getting late but I can hang out for a bit."
            $ RogueX.location = bg_current
            call set_the_scene
        else:

            ch_r "It's a bit late, [RogueX.player_petname], maybe tomorrow."
            $ RogueX.recent_history.append("no_summon")
        return
    elif not approval_check(RogueX, 700, "L") or not approval_check(RogueX, 600, "O"):

        if not approval_check(RogueX, 300):
            ch_r "Not really interested, [RogueX.player_petname]."
            $ RogueX.recent_history.append("no_summon")
            return


        if "summoned" in RogueX.recent_history:
            pass
        elif "goto" in RogueX.recent_history:
            ch_r "You were just over here and then you took off. Why not just head back?"
        elif RogueX.location == "bg_classroom":
            ch_r "I'm kinda in class right now, [RogueX.player_petname], you could join me."
        elif RogueX.location == "bg_dangerroom":
            ch_r "I'm training at the moment, [RogueX.player_petname], care to join me?"
        elif RogueX.location == "bg_campus":
            ch_r "I'm hanging out on campus, [RogueX.player_petname], want to hang with me?"
        elif RogueX.location == "bg_rogue":
            ch_r "I'm in my room, [RogueX.player_petname], want to swing by?"
        elif RogueX.location == "bg_player":
            ch_r "I happen to be in your room, [RogueX.player_petname], I'm waiting for you. . ."
        elif RogueX.location == "bg_showerroom":
            if approval_check(RogueX, 1600):
                ch_r "I'm kinda in the shower right now, [RogueX.player_petname], care to join me?"
            else:
                ch_r "I'm kinda in the shower right now, [RogueX.player_petname], maybe we could touch base later."
                $ RogueX.recent_history.append("no_summon")
                return
        elif RogueX.location == "hold":
            ch_r "I'm not really around right now, see you later?"
            $ RogueX.recent_history.append("no_summon")
            return
        else:

            ch_r "Why don't you come over here, [RogueX.player_petname]?"

        if "summoned" in RogueX.recent_history:
            ch_r "Ok, fine, but why are you leading me on a merry chase?"
            $ line = "yes"

        elif "goto" in RogueX.recent_history:
            menu:
                extend ""
                "You're right, be right back.":
                    ch_r "See you then!"
                    $ line = "go to"
                "Nah, it's better here.":
                    ch_r "Fine by me."
                "But I'd {i}really{/i} like to see you over here.":
                    if approval_check(RogueX, 600, "L") or approval_check(RogueX, 1400):
                        $ line = "lonely"
                    else:
                        $ line = "no"
                "I said come over here.":
                    if approval_check(RogueX, 600, "O"):

                        $ line = "command"
                    elif D20 >= 7 and approval_check(RogueX, 1400):

                        ch_r "I suppose I can, [RogueX.player_petname]."
                        $ line = "yes"
                    elif approval_check(RogueX, 200, "O"):

                        ch_r "I don't think so."
                        ch_r "If you want to see me, you know where to find me."
                    else:

                        $ line = "no"
        else:
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ RogueX.change_stat("love", 55, 1)
                    $ RogueX.change_stat("inhibition", 30, 1)
                    ch_r "See you then!"
                    $ line = "go to"
                "Nah, we can talk later.":

                    $ RogueX.change_stat("obedience", 50, 1)
                    $ RogueX.change_stat("obedience", 30, 2)
                    ch_r "Oh, ok. Talk to you later then."
                "Could you please come visit me? I'm lonely.":

                    if approval_check(RogueX, 600, "L") or approval_check(RogueX, 1400):
                        $ RogueX.change_stat("love", 70, 1)
                        $ RogueX.change_stat("obedience", 50, 1)
                        $ line = "lonely"
                    else:
                        $ RogueX.change_stat("inhibition", 30, 1)
                        $ line = "no"
                "I said come over here.":

                    if approval_check(RogueX, 600, "O"):

                        $ RogueX.change_stat("love", 50, 1, 1)
                        $ RogueX.change_stat("love", 40, -1)
                        $ RogueX.change_stat("obedience", 90, 1)
                        $ line = "command"

                    elif D20 >= 7 and approval_check(RogueX, 1400):

                        $ RogueX.change_stat("love", 70, -2)
                        $ RogueX.change_stat("love", 90, -1)
                        $ RogueX.change_stat("obedience", 50, 2)
                        $ RogueX.change_stat("obedience", 90, 1)
                        ch_r "I suppose I can, [RogueX.player_petname]."
                        $ line = "yes"

                    elif approval_check(RogueX, 200, "O"):

                        $ RogueX.change_stat("love", 70, -4)
                        $ RogueX.change_stat("love", 90, -2)
                        ch_r "I don't know who you think you are, boss'in me around like that."
                        $ RogueX.change_stat("inhibition", 40, 2)
                        $ RogueX.change_stat("inhibition", 60, 1)
                        $ RogueX.change_stat("obedience", 70, -2)
                        ch_r "If you want to see me, you know where to find me."
                    else:

                        $ RogueX.change_stat("inhibition", 30, 1)
                        $ RogueX.change_stat("inhibition", 50, 1)
                        $ RogueX.change_stat("love", 50, -1, 1)
                        $ RogueX.change_stat("obedience", 70, -1)
                        $ line = "no"
    else:


        if RogueX.love > RogueX.obedience:
            ch_r "I'd love to, [RogueX.player_petname]."
        else:
            ch_r "Ok, I'll be right over, [RogueX.player_petname]."
        $ line = "yes"

    $ approval_bonus = 0

    if not line:

        $ RogueX.recent_history.append("no_summon")
        return

    if line == "no":

        if RogueX.location == "bg_classroom":
            ch_r "I seriously can't, [RogueX.player_petname], big test coming up."
        elif RogueX.location == "bg_dangerroom":
            ch_r "Wish I could, [RogueX.player_petname], but I need to get some hours in."
        else:
            ch_r "I'm sorry, [RogueX.player_petname], but I'm kinda busy right now."
        $ RogueX.recent_history.append("no_summon")
        return

    elif line == "go to":

        $ renpy.pop_call()
        $ approval_bonus = 0
        $ line = 0
        $ RogueX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        if RogueX.location == "bg_classroom":
            ch_r "See you then!"
            jump classroom
        elif RogueX.location == "bg_dangerroom":
            ch_r "I'll be warming up!"
            jump danger_room
        elif RogueX.location == "bg_rogue":
            ch_r "I'll get tidied up."

            $ Girl = RogueX
            jump girls_room
        elif RogueX.location == "bg_player":
            ch_r "I'll be waiting."
            jump player_room
        elif RogueX.location == "bg_showerroom":
            ch_r "I guess I'll be here."
            jump shower_room
        elif RogueX.location == "bg_campus":
            ch_r "I'll keep an eye out for you."
            jump campus
        elif RogueX.location in personal_rooms:
            ch_r "I'll see you there."
            $ bg_current = RogueX.location
            jump Misplaced
        else:
            ch_r "You know, I'll just meet you in my room."
            $ RogueX.location = "bg_rogue"

            $ Girl = RogueX
            jump girls_room


    elif line == "lonely":
        ch_r "Oh, how could I say \"no\" to you, [RogueX.player_petname]?"
    elif line == "command":
        ch_r "Fine, if you insist, [RogueX.player_petname]."

    $ RogueX.recent_history.append("summoned")
    $ line = 0
    if "locked" in Player.traits:
        call locked_door (RogueX)
        return
    call taboo_level(taboo_location = False)
    $ RogueX.change_outfit()
    $ RogueX.location = bg_current
    call set_the_scene
    return




label Rogue_Leave(approval_bonus=approval_bonus):
    if "leaving" in RogueX.recent_history:
        $ RogueX.drain_word("leaving")
    else:
        return

    if bg_current == "bg_dangerroom":
        call exit_gym ([RogueX])

    if RogueX.location == "hold":

        ch_r "I'm heading out for a while, see you later."
        return

    if RogueX in Party or "lockedtravels" in RogueX.traits:


        $ RogueX.location = bg_current
        return

    elif "freetravels" in RogueX.traits or not approval_check(RogueX, 700):

        $ RogueX.change_outfit()
        if not approval_check(RogueX, 600, "LO"):
            ch_r "I'm headed out, see you later."
        elif RogueX.location == "bg_classroom":
            ch_r "I'm headed to class right now, [RogueX.player_petname]."
        elif RogueX.location == "bg_dangerroom":
            ch_r "I'm hitting the danger room, [RogueX.player_petname]."
        elif RogueX.location == "bg_campus":
            ch_r "I'm going to hang out on campus, [RogueX.player_petname]."
        elif RogueX.location == "bg_rogue":
            ch_r "I'm heading back to my room, [RogueX.player_petname]."
        elif RogueX.location == "bg_player":
            ch_r "I'll be heading to your room, [RogueX.player_petname]."
        elif RogueX.location == "bg_pool":
            ch_r "I'm headed for the pool."
        elif RogueX.location == "bg_showerroom":
            if approval_check(RogueX, 1400):
                ch_r "I'm hitting the showers, later."
            else:
                ch_r "I'm . . . headed out, see you later."
        else:
            ch_r "I'm headed out, see you later."
        hide Rogue_sprite
        return


    $ RogueX.change_outfit()

    if "follow" not in RogueX.traits:

        $ RogueX.traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ line = 0

    if RogueX.location == "bg_classroom":
        $ approval_bonus = 10
    elif RogueX.location == "bg_dangerroom":
        $ approval_bonus = 20
    elif RogueX.location == "bg_showerroom":
        $ approval_bonus = 40


    if RogueX.location == "bg_classroom":
        ch_r "I'm headed to class right now, [RogueX.player_petname], you could join me."
    elif RogueX.location == "bg_dangerroom":
        ch_r "I'm hitting the danger room, [RogueX.player_petname], care to join me?"
    elif RogueX.location == "bg_campus":
        ch_r "I'm going to hang out on campus, [RogueX.player_petname], want to hang with me?"
    elif RogueX.location == "bg_rogue":
        ch_r "I'm heading back to my room, [RogueX.player_petname], want to swing by?"
    elif RogueX.location == "bg_player":
        ch_r "I'll be heading to your room, [RogueX.player_petname]."
    elif RogueX.location == "bg_showerroom":
        if approval_check(RogueX, 1600):
            ch_r "I'm hitting the showers, [RogueX.player_petname], care to join me?"
        else:
            ch_r "I'm hitting the showers, [RogueX.player_petname], maybe we could touch base later."
            return
    elif RogueX.location == "bg_pool":
        ch_r "I'm headed for the pool. Wanna come?"
    else:
        ch_r "Why don't you come with me, [RogueX.player_petname]?"

    menu:
        extend ""
        "Sure, I'll catch up.":
            if "followed" not in RogueX.recent_history:
                $ RogueX.change_stat("love", 55, 1)
                $ RogueX.change_stat("inhibition", 30, 1)
            $ line = "go to"
        "Nah, we can talk later.":

            if "followed" not in RogueX.recent_history:
                $ RogueX.change_stat("obedience", 50, 1)
                $ RogueX.change_stat("obedience", 30, 2)
            ch_r "Oh, ok. Talk to you later then."
        "Could you please stay with me? I'll get lonely.":

            if approval_check(RogueX, 600, "L") or approval_check(RogueX, 1400):
                if "followed" not in RogueX.recent_history:
                    $ RogueX.change_stat("love", 70, 1)
                    $ RogueX.change_stat("obedience", 50, 1)
                $ line = "lonely"
            else:
                if "followed" not in RogueX.recent_history:
                    $ RogueX.change_stat("inhibition", 30, 1)
                $ line = "no"
        "No, stay here.":

            if approval_check(RogueX, 600, "O"):

                if "followed" not in RogueX.recent_history:
                    $ RogueX.change_stat("love", 50, 1, 1)
                    $ RogueX.change_stat("love", 40, -1)
                    $ RogueX.change_stat("obedience", 90, 1)
                $ line = "command"

            elif D20 >= 7 and approval_check(RogueX, 1400):

                if "followed" not in RogueX.recent_history:
                    $ RogueX.change_stat("love", 70, -2)
                    $ RogueX.change_stat("love", 90, -1)
                    $ RogueX.change_stat("obedience", 50, 2)
                    $ RogueX.change_stat("obedience", 90, 1)
                ch_r "I suppose I can, [RogueX.player_petname]."
                $ line = "yes"

            elif approval_check(RogueX, 200, "O"):

                if "followed" not in RogueX.recent_history:
                    $ RogueX.change_stat("love", 70, -4)
                    $ RogueX.change_stat("love", 90, -2)
                ch_r "I don't know who you think you are, boss'in me around like that."
                if "followed" not in RogueX.recent_history:
                    $ RogueX.change_stat("inhibition", 40, 2)
                    $ RogueX.change_stat("inhibition", 60, 1)
                    $ RogueX.change_stat("obedience", 70, -2)
                ch_r "If you want to see me, you know where to find me."
            else:

                if "followed" not in RogueX.recent_history:
                    $ RogueX.change_stat("inhibition", 30, 1)
                    $ RogueX.change_stat("inhibition", 50, 1)
                    $ RogueX.change_stat("love", 50, -1, 1)
                    $ RogueX.change_stat("obedience", 70, -1)
                $ line = "no"


    $ RogueX.recent_history.append("followed")
    if not line:

        hide Rogue_sprite
        call change_out_of_gym_clothes ([RogueX])
        return

    if line == "no":

        if RogueX.location == "bg_classroom":
            ch_r "I seriously can't, [RogueX.player_petname], big test coming up."
        elif RogueX.location == "bg_dangerroom":
            ch_r "Wish I could, [RogueX.player_petname], but I need to get some hours in."
        else:
            ch_r "I'm sorry, [RogueX.player_petname], but I'm kinda busy right now."
        hide Rogue_sprite
        call change_out_of_gym_clothes ([RogueX])
        return

    elif line == "go to":


        $ approval_bonus = 0
        $ line = 0
        call drain_all_words ("leaving")
        call drain_all_words ("arriving")
        $ RogueX.recent_history.append("goto")
        $ Player.recent_history.append("goto")
        hide Rogue_sprite
        call change_out_of_gym_clothes ([RogueX])

        $ renpy.pop_call()
        $ renpy.pop_call()
        $ renpy.pop_call()

        if RogueX.location == "bg_classroom":
            ch_r "See you then!"
            jump classroom_entry
        elif RogueX.location == "bg_dangerroom":
            ch_r "I'll be warming up!"
            jump danger_room_entry
        elif RogueX.location == "bg_rogue":
            ch_r "I'll meet you there."

            $ Girl = RogueX

            jump girls_room
        elif RogueX.location == "bg_player":
            ch_r "I'll be waiting."
            jump player_room
        elif RogueX.location == "bg_showerroom":
            ch_r "I guess I'll see you there."
            jump shower_entry
        elif RogueX.location == "bg_campus":
            ch_r "Let's head over there."
            jump campus_entry
        elif RogueX.location == "bg_pool":
            ch_r "Let's head over there."
            jump pool_entry
        else:
            ch_r "You know, I'll just meet you in my room."
            $ RogueX.location = "bg_rogue"

            $ Girl = RogueX
            jump girls_room



    elif line == "lonely":
        ch_r "Oh, how could I say \"no\" to you, [RogueX.player_petname]?"
    elif line == "command":
        ch_r "Fine, if you insist, [RogueX.player_petname]."

    $ line = 0
    ch_r "I can stay for a bit."
    $ RogueX.location = bg_current
    call taboo_level(taboo_location = False)
    return
























































































































label Rogue_Clothes:
    if RogueX.taboo:
        if "exhibitionist" in RogueX.traits:
            ch_r "Oooh, naughty. . ."
        elif approval_check(RogueX, 900, taboo_modifier=4) or approval_check(RogueX, 400, "I", taboo_modifier=3):
            ch_r "Well, I mean, it's pretty public here, but I guess I could. . ."
        else:
            ch_r "This is a pretty public place for that, don't you think?"
            ch_r "We can talk about that back in our rooms."

            return
    elif approval_check(RogueX, 900, taboo_modifier=4) or approval_check(RogueX, 600, "L") or approval_check(RogueX, 300, "O"):
        ch_r "Ok, what did you want?"
    else:
        ch_r "I'm not really interested in your fashion opinions."

        return
    if Girl != RogueX or line == "giftstore":
        $ renpy.pop_call()

    $ line = 0

    $ Girl = RogueX
    call shift_focus(Girl)

label Rogue_Wardrobe_Menu:
    while True:
        $ trigger = True

        $ RogueX.change_face()

        menu:
            ch_r "What did you want to tell me about my clothes?"
            "Overshirts":
                call Rogue_Clothes_Over
            "Legwear":
                call Rogue_Clothes_Legs
            "Underwear":
                call Rogue_Clothes_Under
            "Accessories":
                call Rogue_Clothes_Misc
            "Outfit Management":
                call Rogue_Clothes_outfits
            "Let's talk about what you wear around.":
                call Clothes_Schedule (RogueX)
            "Could I get a look at it?" if RogueX.location != bg_current:
                call outfitShame (RogueX, 0, 2)

                if _return:
                    show PhoneSex zorder 150
                    ch_r "How's that? . ."

                hide PhoneSex
            "Could I get a look at it?" if renpy.showing('dress_screen'):
                call outfitShame (RogueX, 0, 2)

                if _return:
                    hide dress_screen
            "Would you be more comfortable behind a screen? (locked)" if RogueX.taboo:
                pass
            "Would you be more comfortable behind a screen?" if RogueX.location == bg_current and not RogueX.taboo and not renpy.showing('dress_screen'):
                if approval_check(RogueX, 1500) or (RogueX.seen_breasts and RogueX.seen_pussy):
                    ch_r "Don't really need that, thanks."
                else:
                    show dress_screen zorder 150

                    ch_r "This is more comfortable, thanks."
            "Gift for you (locked)" if Girl.location != bg_current:
                pass
            "Gift for you" if Girl.location == bg_current:
                ch_p "I'd like to give you something."

                call gifts
            "Switch to. . .":
                if renpy.showing('dress_screen'):
                    call outfitShame (RogueX, 0, 2)

                    if _return:
                        hide dress_screen
                    else:
                        $ RogueX.change_outfit()

                $ RogueX.set_temp_outfit()

                $ trigger = None

                call Switch_chat

                if Girl != RogueX:
                    ch_p "I wanted to talk about your clothes."

                    call expression Girl.tag +"_Clothes"

                $ Girl = RogueX

                call shift_focus(Girl)
            "Never mind, you look good like that. [[return]":
                if "wardrobe" not in RogueX.recent_history:
                    if RogueX.had_chat[1] <= 1:
                        $ RogueX.change_stat("love", 70, 10)
                        $ RogueX.change_stat("obedience", 20, 10)

                        ch_r "Aw, that's sweet."
                    elif RogueX.had_chat[1] <= 10:
                        $ RogueX.change_stat("love", 70, 5)
                        $ RogueX.change_stat("obedience", 20, 5)

                        ch_r "Thanks."
                    elif RogueX.had_chat[1] <= 50:
                        $ RogueX.change_stat("love", 70, 1)
                        $ RogueX.change_stat("obedience", 20, 1)

                        ch_r "Ok."
                    else:
                        ch_r "Ok."

                    $ RogueX.recent_history.append("wardrobe")

                if renpy.showing('dress_screen'):
                    call outfitShame (RogueX, 0, 2)

                    if _return:
                        hide dress_screen
                    else:
                        $ RogueX.change_outfit()

                $ RogueX.set_temp_outfit()
                $ RogueX.had_chat[1] += 1

                $ trigger = None

                return

    menu Rogue_Clothes_outfits:
        "That looks really good on you, you should remember that one. [[Set Custom]":

            menu:
                "Which slot would you like this saved in?"
                "Custom 1":
                    call outfitShame (RogueX, 3, 1)
                "Custom 2":
                    call outfitShame (RogueX, 5, 1)
                "Custom 3":
                    call outfitShame (RogueX, 6, 1)
                "Gym Clothes":
                    call outfitShame (RogueX, 4, 1)
                "Sleepwear":
                    call outfitShame (RogueX, 7, 1)
                "Swimwear":
                    call outfitShame (RogueX, 10, 1)
                "Never mind":
                    pass
        "I really like that green top and skirt outfit you have.":


            $ RogueX.change_outfit("casual1")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ RogueX.outfit_name = "casual1"
                    $ RogueX.outfit["shame"] = 0
                    ch_r "Ok, [RogueX.player_petname], I like this one too."
                "Let's try something else though.":
                    ch_r "Sure."
        "That pink top and pants look really nice on you.":


            $ RogueX.change_outfit("casual2")
            menu:
                "You should wear this one out. [[set current outfit]":
                    $ RogueX.outfit_name = "casual2"
                    $ RogueX.outfit["shame"] = 0
                    ch_r "Sure, [RogueX.player_petname], that one's nice."
                "Let's try something else though.":
                    ch_r "Ok."

        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not RogueX.first_custom_outfit[0] and not RogueX.second_custom_outfit[0] and not RogueX.third_custom_outfit[0]:
            pass

        "Remember that outfit we put together?" if RogueX.first_custom_outfit[0] or RogueX.second_custom_outfit[0] or RogueX.third_custom_outfit[0]:
            $ counter = 0
            while 1:
                menu:
                    "Throw on Custom 1 (locked)" if not RogueX.first_custom_outfit[0]:
                        pass
                    "Throw on Custom 1" if RogueX.first_custom_outfit[0]:
                        $ RogueX.change_outfit("custom1")
                        $ counter = 3
                    "Throw on Custom 2 (locked)" if not RogueX.second_custom_outfit[0]:
                        pass
                    "Throw on Custom 2" if RogueX.second_custom_outfit[0]:
                        $ RogueX.change_outfit("custom2")
                        $ counter = 5
                    "Throw on Custom 3 (locked)" if not RogueX.third_custom_outfit[0]:
                        pass
                    "Throw on Custom 3" if RogueX.third_custom_outfit[0]:
                        $ RogueX.change_outfit("custom3")
                        $ counter = 6

                    "You should wear this one in private. (locked)" if not counter:
                        pass
                    "You should wear this one in private." if counter:
                        if counter == 5:
                            $ RogueX.clothing[9] = "custom2"
                        elif counter == 6:
                            $ RogueX.clothing[9] = "custom3"
                        else:
                            $ RogueX.clothing[9] = "custom1"
                        ch_r "Ok, sure."
                    "On second thought, forget about that one outfit. . .":

                        menu:
                            ch_r "Which one did you mean?"
                            "Custom 1 [[clear custom 1]" if RogueX.first_custom_outfit[0]:
                                ch_r "Ok, no problem."
                                $ RogueX.first_custom_outfit[0] = 0
                            "Custom 1 [[clear custom 1] (locked)" if not RogueX.first_custom_outfit[0]:
                                pass
                            "Custom 2 [[clear custom 2]" if RogueX.second_custom_outfit[0]:
                                ch_r "Ok, no problem."
                                $ RogueX.second_custom_outfit[0] = 0
                            "Custom 2 [[clear custom 2] (locked)" if not RogueX.second_custom_outfit[0]:
                                pass
                            "Custom 3 [[clear custom 3]" if RogueX.third_custom_outfit[0]:
                                ch_r "Ok, no problem."
                                $ RogueX.third_custom_outfit[0] = 0
                            "Custom 3 [[clear custom 3] (locked)" if not RogueX.third_custom_outfit[0]:
                                pass
                            "Never mind, [[back].":
                                pass

                    "You should wear this one out. [[choose outfit first](locked)" if not counter:
                        pass
                    "You should wear this one out." if counter:
                        call Custom_Out (RogueX, counter)
                    "Ok, back to what we were talking about. . .":
                        $ counter = 0
                        return


        "Gym Clothes?" if not RogueX.taboo or bg_current == "bg_dangerroom":
            $ RogueX.change_outfit("gym")

        "Sleepwear?" if not RogueX.taboo:
            if approval_check(RogueX, 1200):
                $ RogueX.change_outfit("sleep")
            else:
                call Display_dress_screen (RogueX)
                if _return:
                    $ RogueX.change_outfit("sleep")

        "Swimwear? (locked)" if (RogueX.taboo and bg_current != "bg_pool") or not RogueX.swimwear[0]:
            $ RogueX.change_outfit("swimwear")
        "Swimwear?" if (not RogueX.taboo or bg_current == "bg_pool") and RogueX.swimwear[0]:
            $ RogueX.change_outfit("swimwear")

        "Halloween Costume?" if "halloween" in RogueX.history:
            ch_r "Sure."
            $ RogueX.change_outfit("costume")
        "Your birthday suit looks really great. . .":


            $ RogueX.change_face("_sexy", 1)
            $ line = 0
            if not RogueX.outfit["bra"] and not RogueX.outfit["underwear"] and not RogueX.outfit["top"] and not RogueX.outfit["bottom"] and not RogueX.outfit["hose"]:
                ch_r "Can't get much more naked than this."
            elif RogueX.seen_breasts and RogueX.seen_pussy and approval_check(RogueX, 1000, taboo_modifier=5):
                ch_r "Naughty boy. . ."
                $ line = 1
            elif approval_check(RogueX, 2000, taboo_modifier=5):
                ch_r "Hmm. . . you move fast, but I suppose for you. . ."
                $ line = 1
            elif RogueX.seen_breasts and RogueX.seen_pussy and approval_check(RogueX, 1000, taboo_modifier=0):
                ch_r "Well, maybe if it weren't quite so. . . public here."
            elif approval_check(RogueX, 2000, taboo_modifier=0):
                ch_r "I might consider it if we had some privacy. . ."
            elif approval_check(RogueX, 1000, taboo_modifier=0):
                $ RogueX.change_face("_surprised", 1)
                ch_r "Hmm. . . you're getting a bit ahead of yourself, [RogueX.player_petname]."
            else:
                $ RogueX.change_face("_angry", 1)
                ch_r "What sort of common strumpet do you take me for?"

            if line:
                $ RogueX.change_outfit("nude")
                "She pulls all her clothes off and throws them in a heap on the floor."
                call Rogue_First_Topless
                call Rogue_First_Bottomless (1)
                $ RogueX.change_face("_sexy")
                menu:
                    "You know, you should wear this one out. [[set current outfit]":
                        if "exhibitionist" in RogueX.traits:
                            ch_r "You sure know how to rev my engines. . ."
                            $ RogueX.outfit_name = "nude"
                            $ RogueX.outfit["shame"] = 50
                        elif approval_check(RogueX, 750, "I") or approval_check(RogueX, 2500, taboo_modifier=0):
                            ch_r "Heh, all right [RogueX.player_petname]."
                            $ RogueX.outfit_name = "nude"
                            $ RogueX.outfit["shame"] = 50
                        else:
                            $ RogueX.change_face("_sexy", 1)
                            $ RogueX.eyes = "_surprised"
                            ch_r "I'm afraid not, [RogueX.player_petname], this is just for between you and me."
                    "Let's try something else though.":
                        if "exhibitionist" in RogueX.traits:
                            ch_r "Hmm, too bad you didn't want me to wear this out. . ."
                        elif approval_check(RogueX, 750, "I") or approval_check(RogueX, 2500, taboo_modifier=0):
                            $ RogueX.change_face("_bemused", 1)
                            ch_r "You know, for a second there I thought you might want me to wear this out. . ."
                            ch_r "Hehe, um. . ."
                        else:
                            $ RogueX.change_face("_confused", 1)
                            ch_r "Well obviously. It's not like I'd ever go out like this."
            $ line = 0
        "Never mind":

            return

    return





    menu Rogue_Clothes_Over:

        "Why don't you go with no [RogueX.outfit['top']]?" if RogueX.outfit["top"]:
            $ RogueX.change_face("_bemused", 1)
            if RogueX.outfit["bra"] or (RogueX.seen_breasts and approval_check(RogueX, 600)):
                ch_r "Sure."
            elif approval_check(RogueX, 600, taboo_modifier=0):
                call Rogue_NoBra
                if not _return:
                    if not approval_check(RogueX, 1200):
                        call Display_dress_screen (RogueX)
                        if not _return:
                            return
                    else:

                        return
            else:

                call Display_dress_screen (RogueX)
                if not _return:
                    ch_r "I'd rather not. . ."
                    if not RogueX.outfit["bra"]:
                        ch_r "I'm afraid I don't have anything on under this."
                    return

            $ RogueX.outfit["top"] = ""
            if not RogueX.outfit["bra"] and not renpy.showing('dress_screen'):
                call Rogue_First_Topless

        "Try on the green mesh top." if RogueX.outfit["top"] != "_mesh_top":
            $ RogueX.change_face("_bemused", 1)
            if RogueX.outfit["bra"] or (RogueX.seen_breasts and approval_check(RogueX, 500, taboo_modifier=2)):
                ch_r "Sure."
            elif approval_check(RogueX, 600, taboo_modifier=0):
                call Rogue_NoBra
                if not _return:
                    if not approval_check(RogueX, 1200):
                        call Display_dress_screen (RogueX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_dress_screen (RogueX)
                if not _return:
                    ch_r "I'm afraid that top is a bit sheer to have nothing under it."
                    if not RogueX.outfit["bra"]:
                        ch_r "I don't have anything on under this."
                    return

            $ RogueX.outfit["top"] = "_mesh_top"
            menu:
                ch_r "With the collar?"
                "Yes":
                    $ RogueX.outfit["neck"] = "_spiked_collar"
                "No":
                    $ RogueX.outfit["neck"] = ""


            if not RogueX.outfit["bra"] and not renpy.showing('dress_screen'):
                call Rogue_First_Topless

        "How about that pink top?" if RogueX.outfit["top"] != "_pink_top":
            $ RogueX.outfit["top"] = "_pink_top"
            $ RogueX.outfit["neck"] = ""

        "How about that green hoodie?" if RogueX.outfit["top"] != "_hoodie":
            $ RogueX.outfit["top"] = "_hoodie"

        "Maybe just throw on a towel?" if RogueX.outfit["top"] != "_towel":
            $ RogueX.change_face("_bemused", 1)
            if RogueX.outfit["bra"] or RogueX.seen_breasts:
                ch_r "Fresh."
            elif approval_check(RogueX, 900, taboo_modifier=0):
                $ RogueX.change_face("_perplexed", 1)
                ch_r "I suppose? . ."
            else:
                call Display_dress_screen (RogueX)
                if not _return:
                    ch_r "That don't leave much to the imagination. . ."
                    return
            $ RogueX.outfit["top"] = "_towel"

        "How about that green nighty I got you?" if RogueX.outfit["top"] != "_nighty" and "_nighty" in RogueX.inventory:
            if RogueX.outfit["bottom"]:
                ch_r "I can't really wear that with my [RogueX.outfit['legs']] on."
            elif not approval_check(RogueX, 1100, taboo_modifier=3):
                call Display_dress_screen (RogueX)
                if not _return:
                    ch_r "That's a bit . . . revealing."
                    return
            else:
                ch_r "Sure. . ."
            if "_lace_bra" in RogueX.inventory:
                $ RogueX.outfit["bra"] = "_lace_bra"
            else:
                $ RogueX.outfit["bra"] = "_bra"
            if "_lace_panties" in RogueX.inventory:
                $ RogueX.outfit["underwear"] = "_lace_panties"
            else:
                $ RogueX.outfit["underwear"] = "_black_panties"
            $ RogueX.outfit["top"] = "_nighty"
            menu:
                extend ""
                "Nice.":
                    pass
                "I meant {i}just{/i} the nighty.":
                    if approval_check(RogueX, 1400, taboo_modifier=3):
                        "She shrugs off her bra and then pulls the nighty back up."
                        $ RogueX.outfit["underwear"] = ""
                        $ RogueX.outfit["bra"] = ""
                        ch_r "Hmmm, alright. . ."
                    elif approval_check(RogueX, 1200, taboo_modifier=3):
                        $ RogueX.outfit["bra"] = ""
                        ch_r "I'll keep my panties on, thanks."
                    else:
                        ch_r "Be happy with what you get."
            if not RogueX.outfit["bra"] and not renpy.showing('dress_screen'):
                call Rogue_First_Topless
        "What about the opaque fetish top?" if RogueX.outfit["top"] != "_opaque_fetish" and "_fetish" in RogueX.inventory:
            ch_p "Try on that opaque fetish top I bought you."
            $ RogueX.outfit["top"] = "_opaque_fetish"
        "What about the sheer fetish top?" if RogueX.outfit["top"] != "_sheer_fetish" and "_fetish" in RogueX.inventory:
            ch_p "Try on that sheer fetish top I bought you."
            $ RogueX.outfit["top"] = "_sheer_fetish"
        "Never mind":

            pass
    return




    label Rogue_NoBra:
        menu:
            ch_r "I don't have anything under this. . ."
            "Then you could slip something on under it. . .":
                if RogueX.seen_breasts and approval_check(RogueX, 1000, taboo_modifier=3) or approval_check(RogueX, 1200, taboo_modifier=4):
                    $ RogueX.blushing = "_blush2"
                    ch_r "'course, I don't exactly need something under it either. . ."
                    $ RogueX.blushing = "_blush1"
                elif approval_check(RogueX, 900, taboo_modifier=2) and "_lace_bra" in RogueX.inventory:
                    ch_r "I suppose this would work. . ."
                    $ RogueX.outfit["bra"]  = "_lace_bra"
                    "She pulls out her lace bra and slips it on under her [RogueX.outfit['top']]."
                elif approval_check(RogueX, 800, taboo_modifier=2):
                    ch_r "Yeah, I guess."
                    $ RogueX.outfit["bra"] = "_bra"
                    "She pulls out her bra and slips it on under her [RogueX.outfit['top']]."
                elif approval_check(RogueX, 600, taboo_modifier=2):
                    ch_r "Yeah, I guess."
                    $ RogueX.outfit["bra"] = "_tank"
                    "She pulls out her tanktop and slips it on under her [RogueX.outfit['top']]."
                else:
                    ch_r "Yeah, I don't think so."
                    return False
            "You could always just wear nothing at all. . .":

                if approval_check(RogueX, 1100, "LI", taboo_modifier=2) and RogueX.love > RogueX.inhibition:
                    ch_r "I suppose I could. . ."
                elif approval_check(RogueX, 700, "OI", taboo_modifier=2) and RogueX.obedience > RogueX.inhibition:
                    ch_r "Sure. . ."
                elif approval_check(RogueX, 600, "I", taboo_modifier=2):
                    ch_r "Yeah. . ."
                elif approval_check(RogueX, 1300, taboo_modifier=2):
                    ch_r "Okay, fine."
                else:
                    $ RogueX.change_face("_surprised")
                    $ RogueX.brows = "_angry"
                    if RogueX.taboo > 20:
                        ch_r "Not in public, [RogueX.player_petname]!"
                    else:
                        ch_r "Don't push it, [RogueX.player_petname]."
                    return False
            "Never mind.":

                ch_r "Ok. . ."
                return False
        return True




    menu Rogue_Clothes_Legs:

        "Maybe go without the [RogueX.outfit['legs']]." if RogueX.outfit["bottom"]:
            $ RogueX.change_face("_sexy", 1)
            if RogueX.seen_underwear and RogueX.outfit["underwear"] and approval_check(RogueX, 500, taboo_modifier=5):
                ch_r "Sure."
            elif RogueX.seen_pussy and approval_check(RogueX, 900, taboo_modifier=4):
                ch_r "Sure, why not?"
            elif approval_check(RogueX, 1300, taboo_modifier=2) and RogueX.outfit["underwear"]:
                ch_r "Well, I suppose if it's for you. . ."
            elif approval_check(RogueX, 700) and not RogueX.outfit["underwear"]:
                call Rogue_NoPantiesOn
                if not _return and not RogueX.outfit["underwear"]:
                    if not approval_check(RogueX, 1500):
                        call Display_dress_screen (RogueX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_dress_screen (RogueX)
                if not _return:
                    ch_r "Not in front of you, [RogueX.player_petname]."
                    if not RogueX.outfit["underwear"]:
                        ch_r "Maybe if I put some panties on first. . ."
                    return
            if RogueX.bottom_number() > 6:
                $ RogueX.outfit["bottom"] = ""
                "She tugs her pants off and drops them to the ground."
            else:
                $ RogueX.outfit["bottom"] = ""
                "She tugs her skirt off and drops it to the ground."
            if renpy.showing('dress_screen'):
                pass
            elif RogueX.outfit["underwear"]:
                $ RogueX.seen_underwear = 1
            else:
                call Rogue_First_Bottomless

        "How about that skirt?" if RogueX.outfit["bottom"] != "_skirt":
            $ RogueX.outfit["bottom"] = "_skirt"
            $ RogueX.upskirt = 0

        "Your ass looks tight in those jeans." if RogueX.outfit["bottom"] != "_pants":
            $ RogueX.outfit["bottom"] = "_pants"
            $ RogueX.outfit["hose"] = ""

        "The tights would look good with that." if RogueX.outfit["hose"] != '_tights' and RogueX.outfit["bottom"] != "_pants":
            $ RogueX.outfit["hose"] = "_tights"
        "Your ripped tights would look good with that." if RogueX.outfit["hose"] != 'ripped_tights' and "_ripped_tights" in RogueX.inventory and RogueX.outfit["bottom"] != "_pants":
            $ RogueX.outfit["hose"] = "_ripped_tights"
        "You could lose the tights." if RogueX.outfit["hose"] == 'ripped_tights' or RogueX.outfit["hose"] == '_tights':
            $ RogueX.outfit["hose"] = ""

        "What about wearing your shorts?" if RogueX.outfit["underwear"] != "_shorts":
            ch_r "Alright."
            $ RogueX.outfit["underwear"] = "_shorts"
        "Why don't you lose the shorts?" if RogueX.outfit["underwear"] == "_shorts":
            $ RogueX.change_face("_sexy", 1)
            if RogueX.seen_underwear and RogueX.outfit["underwear"] and approval_check(RogueX, 500, taboo_modifier=5):
                ch_r "Sure."
            elif RogueX.seen_pussy and approval_check(RogueX, 900, taboo_modifier=4):
                ch_r "Sure, why not?"
            elif approval_check(RogueX, 1300, taboo_modifier=2) and RogueX.outfit["underwear"]:
                ch_r "Well, I suppose if it's for you. . ."
            elif approval_check(RogueX, 700) and not RogueX.outfit["underwear"]:
                call Rogue_NoPantiesOn
                if not _return and not RogueX.outfit["underwear"]:
                    if not approval_check(RogueX, 1500):
                        call Display_dress_screen (RogueX)
                        if not _return:
                            return
                    else:
                        return
            else:
                call Display_dress_screen (RogueX)
                if not _return:
                    ch_r "Not in front of you, [RogueX.player_petname]."
                    if not RogueX.outfit["underwear"]:
                        ch_r "Maybe if I put some panties on first. . ."
                    return
            if RogueX.outfit["underwear"] == "_shorts":
                $ RogueX.outfit["underwear"] = ""
            "She tugs her shorts off and drops them to the ground."
            if renpy.showing('dress_screen'):
                pass
            elif RogueX.outfit["underwear"]:
                $ RogueX.seen_underwear = 1
            else:
                call Rogue_First_Bottomless

        "What about those opaque fetish pants?" if RogueX.outfit["bottom"] != "_opaque_fetish" and "_fetish" in RogueX.inventory:
            ch_p "Try on those opaque fetish pants I bought you."
            $ RogueX.outfit["bottom"] = "_opaque_fetish"
        "What about those sheer fetish pants?" if RogueX.outfit["bottom"] != "_sheer_fetish" and "_fetish" in RogueX.inventory:
            ch_p "Try on those sheer fetish pants I bought you."
            $ RogueX.outfit["bottom"] = "_sheer_fetish"

        "How about that sweater?" if RogueX.outfit["front_outer_accessory"] != "_sweater" and "halloween" in RogueX.history:
            ch_p "What about that sweater you wore at the party?"
            $ RogueX.outfit["front_outer_accessory"] = "_sweater"
        "Lose the sweater?" if RogueX.outfit["front_outer_accessory"] == "_sweater" and "halloween" in RogueX.history:
            ch_p "You can do without the sweater."
            $ RogueX.outfit["front_outer_accessory"] = ""
        "Never mind":

            pass
    return




    label Rogue_NoPantiesOn:
        menu:
            ch_r "I'm not wearing anything under these, you know. . ."
            "Then you could slip on a pair of panties. . .":
                if RogueX.seen_pussy and approval_check(RogueX, 1100, taboo_modifier=4):
                    $ RogueX.blushing = "_blush1"
                    ch_r "Alright."
                    $ RogueX.blushing = ""
                elif approval_check(RogueX, 1500, taboo_modifier=4):
                    $ RogueX.blushing = "_blush1"
                    ch_r "Alright."
                    $ RogueX.blushing = ""
                elif approval_check(RogueX, 700, taboo_modifier=4):
                    ch_r "I like how you think."
                    if "_lace_panties" in RogueX.inventory:
                        $ RogueX.outfit["underwear"]  = "_lace_panties"
                    else:
                        $ RogueX.outfit["underwear"] = "_black_panties"
                    if approval_check(RogueX, 1200, taboo_modifier=4) and RogueX.outfit["bottom"]:
                        $ line = RogueX.outfit["bottom"]
                        $ RogueX.outfit["bottom"] = ""
                        "She pulls off her [line] and slips on the [RogueX.outfit['underwear']]."
                    elif RogueX.outfit["bottom"] == "_skirt":
                        "She pulls out her [RogueX.outfit['underwear']] and pulls them up under her skirt."
                        $ RogueX.outfit["bottom"] = ""
                        "Then she drops the skirt to the floor."
                    else:
                        $ line = RogueX.outfit["bottom"]
                        $ RogueX.outfit["bottom"] = ""
                        "She steps away a moment and then comes back wearing only the [RogueX.outfit['underwear']]."
                    return
                else:
                    ch_r "Nope."
                    return False
            "You could always just wear nothing at all. . .":

                if approval_check(RogueX, 1100, "LI", taboo_modifier=3) and RogueX.love > RogueX.inhibition:
                    ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                elif approval_check(RogueX, 750, "OI", taboo_modifier=3) and RogueX.obedience > RogueX.inhibition:
                    ch_r "If that's what you want."
                elif approval_check(RogueX, 500, "I", taboo_modifier=3):
                    ch_r "Oooh, naughty."
                elif approval_check(RogueX, 1400, taboo_modifier=3):
                    ch_r "Oh, fine. You've been a good boy."
                else:
                    $ RogueX.change_face("_surprised")
                    $ RogueX.brows = "_angry"
                    if RogueX.taboo:
                        ch_r "Not here,[RogueX.player_petname]!"
                    else:
                        ch_r "Not with you around,[RogueX.player_petname]!"
                    return False
            "Never mind.":

                ch_r "Ok. . ."
                return False
        return True



    menu Rogue_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [RogueX.outfit['bra']]?" if RogueX.outfit["bra"]:
                    $ RogueX.change_face("_bemused", 1)
                    if RogueX.seen_breasts and approval_check(RogueX, 1100, taboo_modifier=2):
                        ch_r "Sure."
                    elif approval_check(RogueX, 1100, taboo_modifier=2):
                        ch_r "I guess I don't really mind if you see them. . ."
                    elif RogueX.outfit["top"] == "_hoodie" and approval_check(RogueX, 500, taboo_modifier=2):
                        ch_r "I guess this covers enough. . ."
                    elif not RogueX.seen_breasts and not approval_check(RogueX, 1100):
                        call Display_dress_screen (RogueX)
                        if not _return:
                            if RogueX.outfit["top"] == "_pink_top" and approval_check(RogueX, 950, taboo_modifier=2):
                                ch_r "This look is a bit revealing. . ."
                            elif RogueX.outfit["top"] == "_mesh_top":
                                ch_r "In this top? That would leave nothing to the imagination!"
                            elif not RogueX.outfit["top"]:
                                ch_r "Not without a little coverage, for modesty."
                            else:
                                ch_r "I don't think so, [RogueX.player_petname]."
                            return
                    $ line = RogueX.outfit["bra"]
                    $ RogueX.outfit["bra"] = ""
                    if RogueX.outfit["top"]:
                        "She reaches into her [RogueX.outfit['top']] grabs her [line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [line] fall to the ground."
                    if (not RogueX.outfit["top"] or RogueX.outfit["top"] == "_mesh_top") and not renpy.showing('dress_screen'):
                        call Rogue_First_Topless

                "Try on that black tank top." if RogueX.outfit["bra"] != "_tank":
                    $ RogueX.outfit["bra"] = "_tank"
                "I like that buttoned tank top." if RogueX.outfit["bra"] != "_buttoned_tank":
                    $ RogueX.outfit["bra"] = "_buttoned_tank"

                "I like that sports bra." if RogueX.outfit["bra"] != "_sports_bra":
                    if (RogueX.seen_breasts and approval_check(RogueX, 600)) or approval_check(RogueX, 900, taboo_modifier=2):
                        ch_r "Sure."
                    else:
                        call Display_dress_screen (RogueX)
                        if not _return:
                            ch_r "I don't know about wearing it with this. . ."
                            return
                    $ RogueX.outfit["bra"] = "_sports_bra"

                "I like that black bra." if RogueX.outfit["bra"] != "_bra":
                    if (RogueX.seen_breasts and approval_check(RogueX, 600)) or approval_check(RogueX, 1100, taboo_modifier=2):
                        ch_r "Sure."
                    else:
                        call Display_dress_screen (RogueX)
                        if not _return:
                            ch_r "That's a bit too revealing. . ."
                            return
                    $ RogueX.outfit["bra"] = "_bra"

                "I like that blue tube top." if RogueX.outfit["bra"] != "_tube_top" and "halloween" in RogueX.history:
                    if (RogueX.seen_breasts and approval_check(RogueX, 600)) or approval_check(RogueX, 900, taboo_modifier=2):
                        ch_r "Sure."
                    else:
                        call Display_dress_screen (RogueX)
                        if not _return:
                            ch_r "I don't know about wearing it with this. . ."
                            return
                    $ RogueX.outfit["bra"] = "_tube_top"

                "I like that lace bra." if "_lace_bra" in RogueX.inventory and RogueX.outfit["bra"] != "_lace_bra":
                    if (RogueX.seen_breasts and approval_check(RogueX, 800)) or approval_check(RogueX, 1100, taboo_modifier=2):
                        ch_r "Sure."
                    else:
                        call Display_dress_screen (RogueX)
                        if not _return:
                            ch_r "That's a bit too revealing. . ."
                            return
                    $ RogueX.outfit["bra"] = "_lace_bra"

                "I like that bikini top." if RogueX.outfit["bra"] != "_bikini_top" and "_bikini_top" in RogueX.inventory:
                    if bg_current == "bg_pool":
                        ch_r "Sure."
                    else:
                        if RogueX.seen_breasts or approval_check(RogueX, 1000, taboo_modifier=2):
                            ch_r "Sure."
                        else:
                            call Display_dress_screen (RogueX)
                            if not _return:
                                ch_r "I kinda don't feel right about that. . ."
                                return
                    $ RogueX.outfit["bra"] = "_bikini_top"

                "I like that harness bra." if "_harness" in RogueX.inventory and RogueX.outfit["bra"] != "_harness":
                    if (RogueX.seen_breasts and approval_check(RogueX, 800)) or approval_check(RogueX, 1100, taboo_modifier=2):
                        ch_r "Sure."
                    else:
                        call Display_dress_screen (RogueX)

                        if not _return:
                            ch_r "That's a bit too revealing. . ."

                            return
                    $ RogueX.outfit["bra"] = "_harness"
                "Never mind":

                    pass
            jump Rogue_Clothes_Under
        "Hose and stockings options":


            menu:
                "You could lose the hose." if RogueX.outfit["hose"] and RogueX.outfit["hose"] != 'ripped_tights' and RogueX.outfit["hose"] != '_tights':
                    $ RogueX.outfit["hose"] = ""
                "The thigh-high hose would look good with that." if RogueX.outfit["hose"] != "_stockings" and RogueX.outfit["bottom"] != "_pants":
                    $ RogueX.outfit["hose"] = "_stockings"
                "The pantyhose would look good with that." if RogueX.outfit["hose"] != "_pantyhose" and RogueX.outfit["bottom"] != "_pants":
                    $ RogueX.outfit["hose"] = "_pantyhose"
                "The stockings would look good with that." if RogueX.outfit["hose"] != "_stockings_and_garterbelt" and "_stockings_and_garterbelt" in RogueX.inventory and RogueX.outfit["bottom"] != "_pants":
                    $ RogueX.outfit["hose"] = "_stockings_and_garterbelt"
                "Maybe just the garterbelt?" if RogueX.outfit["hose"] != "garterbelt" and "_stockings_and_garterbelt" in RogueX.inventory and RogueX.outfit["bottom"] != "_pants":
                    $ RogueX.outfit["hose"] = "garterbelt"
                "Your ripped pantyhose would look good with that." if RogueX.outfit["hose"] != "_ripped_pantyhose" and "_ripped_pantyhose" in RogueX.inventory and RogueX.outfit["bottom"] != "_pants":
                    $ RogueX.outfit["hose"] = "_ripped_pantyhose"
                "Never mind":
                    pass
            jump Rogue_Clothes_Under
        "Panties":

            menu:

                "You could lose those panties. . ." if RogueX.outfit["underwear"] and RogueX.outfit["underwear"] != "_shorts":
                    $ RogueX.change_face("_bemused", 1)
                    if (RogueX.seen_pussy and approval_check(RogueX, 900)) and not RogueX.taboo:
                        if approval_check(RogueX, 850, "L", taboo_modifier=2):
                            ch_r "Well aren't you cheeky. . ."
                        elif approval_check(RogueX, 500, "O", taboo_modifier=2):
                            ch_r "Fine by me."
                        elif approval_check(RogueX, 350, "I", taboo_modifier=2):
                            ch_r "Oooh, naughty."
                        else:
                            ch_r "Oh, I guess I could."
                    else:
                        if approval_check(RogueX, 1100, "LI", taboo_modifier=2):
                            ch_r "Well aren't you cheeky. . . I suppose I could give you a show. . ."
                        elif approval_check(RogueX, 750, "OI", taboo_modifier=2):
                            ch_r "If that's what you want."
                        elif approval_check(RogueX, 500, "I", taboo_modifier=2):
                            ch_r "Oooh, naughty."
                        elif approval_check(RogueX, 1400, taboo_modifier=3):
                            ch_r "Oh, fine. You've been a good boy."
                        else:
                            call Display_dress_screen (RogueX)
                            if not _return:
                                $ RogueX.change_face("_surprised")
                                $ RogueX.brows = "_angry"
                                if RogueX.taboo > 20:
                                    ch_r "Not in public, [RogueX.player_petname]!"
                                else:
                                    ch_r "Not with you around,[RogueX.player_petname]!"
                                jump Rogue_Clothes
                    $ line = RogueX.outfit["underwear"]
                    $ RogueX.outfit["underwear"] = ""
                    if not RogueX.outfit["bottom"]:
                        "She pulls off her [line], then drops them to the ground."
                        if not renpy.showing('dress_screen'):
                            call Rogue_First_Bottomless
                    elif approval_check(RogueX, 1200, taboo_modifier=4):
                        $ trigger = RogueX.outfit["bottom"]
                        $ RogueX.outfit["bottom"] = ""
                        pause 0.5
                        $ RogueX.outfit["bottom"] = trigger
                        "She pulls off her [RogueX.outfit['legs']] and [line], then pulls the [RogueX.outfit['legs']] back on."
                        $ trigger = 1
                        call Rogue_First_Bottomless (1)
                    elif RogueX.outfit["bottom"] == "_skirt":
                        "She reaches under her skirt and pulls her [line] off."
                    else:
                        $ RogueX.blushing = "_blush1"
                        "She steps away a moment and then comes back."
                        $ RogueX.blushing = ""
                    $ line = 0

                "Why don't you wear the green panties instead?" if RogueX.outfit["underwear"] and RogueX.outfit["underwear"] != "_green_panties":
                    if approval_check(RogueX, 1000, taboo_modifier=3):
                        ch_r "Sure, ok."
                        $ RogueX.outfit["underwear"] = "_green_panties"
                    elif RogueX.outfit["underwear"] == "_shorts":
                        ch_r "Heh, no, I think I'll stick with these, thanks."
                    else:
                        call Display_dress_screen (RogueX)
                        if not _return:
                            ch_r "I think I'll choose my own underwear, thank you."
                        else:
                            $ RogueX.outfit["underwear"] = "_green_panties"

                "Why don't you wear the black panties instead?" if RogueX.outfit["underwear"] and RogueX.outfit["underwear"] != "_black_panties":
                    if approval_check(RogueX, 1100, taboo_modifier=3):
                        ch_r "Sure."
                        $ RogueX.outfit["underwear"] = "_black_panties"
                    elif RogueX.outfit["underwear"] == "_shorts":
                        ch_r "Heh, no, I think I'll stick with these, thanks."
                    else:
                        call Display_dress_screen (RogueX)
                        if not _return:
                            ch_r "I don't see how that's any business of yours, [RogueX.player_petname]."
                        else:
                            $ RogueX.outfit["underwear"] = "_black_panties"

                "Why don't you wear the lace panties instead?" if "_lace_panties" in RogueX.inventory and RogueX.outfit["underwear"] and RogueX.outfit["underwear"] != "_lace_panties":
                    if approval_check(RogueX, 1200, taboo_modifier=3):
                        ch_r "Sure."
                        $ RogueX.outfit["underwear"] = "_lace_panties"
                    elif RogueX.outfit["underwear"] == "_shorts":
                        ch_r "Heh, no, I think I'll stick with these, thanks."
                    else:
                        call Display_dress_screen (RogueX)
                        if not _return:
                            ch_r "I don't see how that's any business of yours, [RogueX.player_petname]."
                        else:
                            $ RogueX.outfit["underwear"] = "_lace_panties"

                "I like those bikini bottoms." if RogueX.outfit["underwear"] != "_bikini_bottoms" and "_bikini_bottoms" in RogueX.inventory:
                    if bg_current == "bg_pool":
                        ch_r "Sure."
                        $ RogueX.outfit["underwear"] = "_bikini_bottoms"
                    else:
                        if approval_check(RogueX, 1000, taboo_modifier=2):
                            ch_r "Sure."
                            $ RogueX.outfit["underwear"] = "_bikini_bottoms"
                        else:
                            call Display_dress_screen (RogueX)
                            if not _return:
                                ch_r "I kinda don't feel right about that. . ."
                            else:
                                $ RogueX.outfit["underwear"] = "_bikini_bottoms"

                "What about those harness panties I bought you?" if "_harness" in RogueX.inventory and RogueX.outfit["underwear"] and RogueX.outfit["underwear"] != "_harness":
                    if approval_check(RogueX, 1200, taboo_modifier=3):
                        ch_r "Sure."

                        $ RogueX.outfit["underwear"] = "_harness"
                    elif RogueX.outfit["underwear"] == "_shorts":
                        ch_r "Heh, no, I think I'll stick with these, thanks."
                    else:
                        call Display_dress_screen (RogueX)

                        if not _return:
                            ch_r "I don't see how that's any business of yours, [RogueX.player_petname]."
                        else:
                            $ RogueX.outfit["underwear"] = "_harness"

                "You know, you could wear some panties with that. . ." if not RogueX.outfit["underwear"]:
                    $ RogueX.change_face("_bemused", 1)
                    if RogueX.outfit["bottom"] and (RogueX.love+RogueX.obedience) <= (1.5*RogueX.inhibition):
                        $ RogueX.mouth = "_smile"
                        ch_r "No thanks, [RogueX.player_petname]."
                        menu:
                            "Fine by me":
                                jump Rogue_Clothes
                            "I insist, put some on.":
                                if (RogueX.love+RogueX.obedience) <= RogueX.inhibition:
                                    $ RogueX.change_face("_angry")
                                    ch_r "Well too bad."
                                    jump Rogue_Clothes
                                else:
                                    $ RogueX.change_face("_sadside")
                                    ch_r "Well! Fine."
                    menu:
                        extend ""
                        "How about the green ones?":
                            ch_r "Sure, ok."
                            $ RogueX.outfit["underwear"] = "_green_panties"
                        "How about the black ones?":
                            ch_r "Alright."
                            $ RogueX.outfit["underwear"]  = "_black_panties"
                        "How about the lace ones?" if "_lace_panties" in RogueX.inventory:
                            ch_r "Alright."
                            $ RogueX.outfit["underwear"]  = "_lace_panties"
                        "How about the harness panties?" if "_harness" in RogueX.inventory:
                            ch_r "Alright."

                            $ RogueX.outfit["underwear"] = "_harness"
                "Never mind":

                    pass
            jump Rogue_Clothes_Under
        "Never mind":
            return
    return






    menu Rogue_Clothes_Misc:
        "Dry hair." if RogueX.outfit["hair"] == "_wet":
            ch_p "Maybe dry out your hair."
            if approval_check(RogueX, 600):
                ch_r "Ok."
                $ RogueX.outfit["hair"] = "_evo"
            else:
                ch_r "I kinda prefer this look."

        "Wet Look hair." if RogueX.outfit["hair"] != "_wet":
            ch_p "You should go for that wet look with your hair."
            if approval_check(RogueX, 800):
                ch_r "Hmm?"
                $ RogueX.outfit["hair"] = "_wet"
                "She wanders off for a minute and comes back."
                ch_r "Like this?"
            else:
                ch_r "Not really into that."

        "Party hair style." if RogueX.outfit["hair"] != "_cosplay" and "halloween" in RogueX.history:
            ch_p "I liked the hair you had at the party."
            if approval_check(RogueX, 600):
                ch_r "Oh, ok."
                $ RogueX.outfit["hair"] = "_cosplay"
            else:
                ch_r "I kinda prefer this look."
        "Original hair style." if RogueX.outfit["hair"] == "_cosplay":
            ch_p "I liked your original hair style."
            if approval_check(RogueX, 600):
                ch_r "Oh, ok."
                $ RogueX.outfit["hair"] = "_evo"
            else:
                ch_r "I kinda prefer this look."

        "Grow pubes" if not RogueX.pubes:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in RogueX.to_do:
                $ RogueX.change_face("_bemused", 1)
                ch_r "Yeah, I know, [RogueX.player_petname]. It doesn't grow out overnight!"
            else:
                $ RogueX.change_face("_bemused", 1)
                $ approval = approval_check(RogueX, 1150, taboo_modifier=0)

                if approval_check(RogueX, 850, "L", taboo_modifier=0) or (approval and RogueX.love > RogueX.obedience):
                    ch_r "Well. . . if that's how you like it. . ."
                elif approval_check(RogueX, 500, "O", taboo_modifier=0) or (approval and RogueX.obedience > RogueX.inhibition):
                    ch_r "If that's what you want."
                elif approval_check(RogueX, 500, "I", taboo_modifier=0) or approval:
                    ch_r "Heh, I like a man knows what he wants, [RogueX.player_petname]."
                else:
                    $ RogueX.change_face("_surprised")
                    $ RogueX.brows = "_angry"
                    ch_r "Well I don't see how that's any of your business, [RogueX.player_petname]."
                    return
                $ RogueX.to_do.append("pubes")
                $ RogueX.pubes_counter = 6


        "Shave pubes" if RogueX.pubes == "_hairy":
            ch_p "I like it waxed clean down there."

            $ RogueX.change_face("_bemused", 1)

            if "shave" in RogueX.to_do:
                ch_r "I know, I'll get on that. Not right this second, obviously."
            else:
                $ approval = approval_check(RogueX, 1150, taboo_modifier=0)

                if approval_check(RogueX, 850, "L", taboo_modifier=0) or (approval and RogueX.love > RogueX.obedience):
                    ch_r "I can keep it tidy if you like. . ."
                elif approval_check(RogueX, 500, "O", taboo_modifier=0) or (approval and RogueX.obedience > RogueX.inhibition):
                    ch_r "I'll take care of it."
                elif approval_check(RogueX, 500, "I", taboo_modifier=0) or approval:
                    ch_r "You better earn it, [RogueX.player_petname]."
                else:
                    $ RogueX.change_face("_surprised")
                    $ RogueX.brows = "_angry"

                    ch_r "I don't see how that's any of your beeswax, [RogueX.player_petname]."

                    return
                $ RogueX.to_do.append("shave")
        "Add ring piercings." if RogueX.piercings != "_ring" and (RogueX.seen_pussy or RogueX.seen_breasts):
            ch_p "You know, you'd look really nice with some ring body piercings."

            if "_ring" in RogueX.to_do:
                ch_r "Yeah, I know, I'll get to it."
            else:
                $ RogueX.change_face("_bemused", 1)

                $ approval = approval_check(RogueX, 1350, taboo_modifier=0)

                if approval_check(RogueX, 950, "L", taboo_modifier=0) or (approval and RogueX.love > RogueX.obedience):
                    ch_r "You really like those? Well, I suppose. . ."
                elif approval_check(RogueX, 600, "O", taboo_modifier=0) or (approval and RogueX.obedience > RogueX.inhibition):
                    ch_r "I'll go get that taken care of."
                elif approval_check(RogueX, 600, "I", taboo_modifier=0) or approval:
                    ch_r "I've always kind of liked the look of those. . ."
                else:
                    $ RogueX.change_face("_surprised")
                    $ RogueX.brows = "_angry"

                    ch_r "I don't see how that's any of your beeswax, [RogueX.player_petname]."

                    return

                $ RogueX.to_do.append("_ring")
        "Add barbell piercings." if RogueX.piercings != "_barbell" and (RogueX.seen_pussy or RogueX.seen_breasts):
            ch_p "You know, you'd look really nice with some barbell body piercings."

            if "_barbell" in RogueX.to_do:
                ch_r "Yeah, I know, I'll get to it."
            else:
                $ RogueX.change_face("_bemused", 1)

                $ approval = approval_check(RogueX, 1350, taboo_modifier=0)

                if approval_check(RogueX, 900, "L", taboo_modifier=0) or (approval and RogueX.love > RogueX.obedience):
                    ch_r "You really like those? Well, I suppose. . ."
                elif approval_check(RogueX, 600, "O", taboo_modifier=0) or (approval and RogueX.obedience > RogueX.inhibition):
                    ch_r "I'll go get that taken care of."
                elif approval_check(RogueX, 600, "I", taboo_modifier=0) or approval:
                    ch_r "I've always kind of liked the look of those. . ."
                else:
                    $ RogueX.change_face("_surprised")
                    $ RogueX.brows = "_angry"

                    ch_r "I don't see how that's any of your beeswax, [RogueX.player_petname]."

                    return

                $ RogueX.to_do.append("_barbell")
                $ RogueX.piercings = "_barbell"
        "Remove piercings." if RogueX.piercings:
            ch_p "You know, you'd look better without those piercings."

            $ RogueX.change_face("_bemused", 1)

            $ approval = approval_check(RogueX, 1350, taboo_modifier=0)

            if approval_check(RogueX, 950, "L", taboo_modifier=0) or (approval and RogueX.love > RogueX.obedience):
                ch_r "You really think so? I guess I could lose them. . ."
            elif approval_check(RogueX, 600, "O", taboo_modifier=0) or (approval and RogueX.obedience > RogueX.inhibition):
                ch_r "I'll take them out then."
            elif approval_check(RogueX, 600, "I", taboo_modifier=0) or approval:
                ch_r "I guess I prefered not having them in. . ."
            else:
                $ RogueX.change_face("_surprised")
                $ RogueX.brows = "_angry"

                ch_r "I'll keep them, if you don't mind."

                return
            $ RogueX.piercings = ""
        "Add spiked collar." if RogueX.outfit["neck"] != "_spiked_collar":
            $ RogueX.outfit["neck"] = "_spiked_collar"
        "Remove spiked collar." if RogueX.outfit["neck"] == "_spiked_collar":
            $ RogueX.outfit["neck"] = ""
        "Gloves on." if not RogueX.outfit["gloves"]:
            $ RogueX.outfit["gloves"] = "_gloves"
        "Gloves off." if RogueX.outfit["gloves"]:
            $ RogueX.outfit["gloves"] = ""
        "Never mind":
            pass

    return
