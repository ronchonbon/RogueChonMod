label Emma_chat_Minimal:
    $ EmmaX.change_face()
    $ shift_focus (EmmaX)
    if EmmaX.location != Player.location:
        show cellphone at sprite_location(EmmaX.sprite_location)
    else:
        hide cellphone
    if "caught" in EmmaX.recent_history:
        ch_e "I don't think we should be seen together, if you don't mind."
        return
    if "angry" in EmmaX.recent_history:
        ch_e "I would not press my luck if I were you."
        return
    menu:
        ch_e "What was it you wished to discuss, [EmmaX.player_petname]?"
        "Come on over." if EmmaX.location != Player.location:
            ch_e "I don't think I should be visiting students at their whim."
            ch_e "You know my office hours."
        "Ask [EmmaX.name] to leave" if EmmaX.location == Player.location:
            ch_e "I'll come and go as I see fit, thank you."
        "Romance her":
            menu:
                "Flirt with her (locked)" if EmmaX.had_chat[5]:
                    pass
                "Flirt with her" if not EmmaX.had_chat[5]:
                    call Emma_Flirt_Minimal
                "Sex Menu" if EmmaX.location == Player.location:
                    ch_p "Did you want to fool around?"
                    ch_e "With a student? You should know better than that, [EmmaX.player_petname]."
                "Date":
                    ch_p "Do you want to go on a date tonight?"
                    ch_e "Well that certainly doesn't seem appropriate."
                "Gifts" if EmmaX.location == Player.location:
                    ch_p "I'd like to give you something."
                    ch_e "I'm not sure that would be appropriate at the moment."
                "Back":
                    pass
        "Talk to her":
            menu:
                "I just wanted to talk. . .":
                    call Emma_Chitchat
                "Relationship status":
                    ch_p "Could we talk about us?"
                    ch_e "I'm not sure that's an appropriate discussion at the moment."
                "Could I get your number?" if EmmaX not in Player.Phonebook:
                    if approval_check(EmmaX, 800, "LI"):
                        ch_e "I don't see why not."
                        $ Player.Phonebook.append(EmmaX)
                    elif approval_check(EmmaX, 500, "OI"):
                        ch_e "Hmm. . . fine, hand me your phone."
                        $ Player.Phonebook.append(EmmaX)
                    else:
                        ch_e "I don't think it's appropriate to give my number out to a student like that."
                "Back":
                    pass
        "Change [EmmaX.name]":
            ch_p "Let's talk about you."
            ch_e "I doubt that's any of your business."
        "Player.Party up" if EmmaX not in Player.Party and EmmaX.location == Player.location:
            ch_p "Could you follow me for a bit?"
            ch_e "I don't think I should."
        "Disband party" if EmmaX in Player.Party:
            ch_p "Ok, you can leave if you prefer."
            $ Player.Party.remove(EmmaX)
        "Never mind.":
            if time_index == 2:
                ch_e "Now if that will be all, please clear out of here."
                $ EmmaX.change_face("bemused", 2)
                ch_e "I have some. . . business to attend to."
            else:
                "She seems a bit reserved. Maybe you need something to break the ice."
                "Maybe you should check in on her after classes are over and the students leave."
            return
    jump Emma_chat_Minimal

label Emma_Flirt_Minimal:
    menu:
        "Compliment her":
            call Compliment (Girl)
        "Say you love her":
            if EmmaX.love >= 500:
                call change_Girl_stat(EmmaX, "love", 2)
            call change_Girl_stat(EmmaX, "obedience", 1)
            ch_e "Don't even joke, [EmmaX.player_petname]."
        "Touch her cheek":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Hold hands":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Pat her head":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Kiss her cheek":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Hug her":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Slap her ass":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Pinch her ass":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Grab her tit":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Rub her shoulders":
            "You begin to approach her, but she cuts you off with a firm hand out."
            ch_e "Don't get too close to me, [EmmaX.player_petname]."
        "Never mind":
            return
    $ EmmaX.had_chat[5] = 1
    return


label Emma_Relationship:
    while True:
        menu:
            ch_e "What did you want to talk about?"
            "Do you want to be my girlfriend?" if EmmaX not in Player.Harem and "ex" not in EmmaX.traits:
                $ EmmaX.daily_history.append("relationship")
                if "asked boyfriend" in EmmaX.daily_history and "angry" in EmmaX.daily_history:
                    $ EmmaX.change_face("angry", 1)
                    ch_e "Pest."
                    return
                elif "asked boyfriend" in EmmaX.daily_history:
                    $ EmmaX.change_face("angry", 1)
                    ch_e "Not today, little fly."
                    return
                elif EmmaX.broken_up[0]:
                    $ EmmaX.change_face("angry", 1)
                    ch_e "I don't share."
                    if Player.Harem:
                        $ EmmaX.daily_history.append("asked boyfriend")
                        return
                    else:
                        ch_p "I'm not anymore."

                $ EmmaX.daily_history.append("asked boyfriend")

                if Player.Harem and "EmmaYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_e "I doubt they would understand, [EmmaX.player_petname]."
                    else:
                        ch_e "I doubt [Player.Harem[0].name] would understand, [EmmaX.player_petname]."
                    return

                if EmmaX.event_happened[5]:
                    $ EmmaX.change_face("bemused", 1)
                    ch_e "I believe I asked you first."
                else:
                    $ EmmaX.change_face("surprised", 2)
                    ch_e "Don't you think that might be inappropriate, [EmmaX.player_petname]. . ."
                    $ EmmaX.change_face("smile", 1)

                call Emma_OtherWoman

                if EmmaX.love >= 800:
                    $ EmmaX.change_face("surprised", 1)
                    $ EmmaX.mouth = "smile"
                    call change_Girl_stat(EmmaX, "love", 40)
                    ch_e "I suppose I've become accustomed to you. . ."
                    if "boyfriend" not in EmmaX.player_petnames:
                        $ EmmaX.player_petnames.append("boyfriend")
                    if "EmmaYes" in Player.traits:
                        $ Player.traits.remove("EmmaYes")
                    $ Player.Harem.append(EmmaX)
                    call Harem_Initiation
                    "[EmmaX.name] draws you in and kisses you deeply."
                    $ EmmaX.change_face("kiss", 1)
                    $ EmmaX.permanent_History["kiss"] += 1
                elif EmmaX.obedience >= 500:
                    $ EmmaX.change_face("perplexed")
                    ch_e "I don't believe \"dating\" would be the right term for it."
                elif EmmaX.inhibition >= 500:
                    $ EmmaX.change_face("smile")
                    ch_e "I don't think we should be \"exclusive.\""
                else:
                    $ EmmaX.change_face("perplexed", 1)
                    ch_e "I really couldn't get serious about a student, [EmmaX.player_petname]."

            "Do you want to get back together?" if "ex" in EmmaX.traits:
                $ EmmaX.daily_history.append("relationship")
                if "asked boyfriend" in EmmaX.daily_history and "angry" in EmmaX.daily_history:
                    $ EmmaX.change_face("angry", 1)
                    ch_e "Do I have to demonstrate how unlikely that is?"
                    return
                elif "asked boyfriend" in EmmaX.daily_history:
                    $ EmmaX.change_face("angry", 1)
                    ch_e "Now you're just embarrassing yourself."
                    return

                $ EmmaX.daily_history.append("asked boyfriend")

                if Player.Harem and "EmmaYes" not in Player.traits:
                    if len(Player.Harem) >= 2:
                        ch_e "I doubt they would understand, [EmmaX.player_petname]."
                    else:
                        ch_e "I doubt [Player.Harem[0].name] would understand, [EmmaX.player_petname]."
                    return

                $ counter = 0
                call Emma_OtherWoman

                if EmmaX.love >= 800:
                    $ EmmaX.change_face("sly", 1)
                    call change_Girl_stat(EmmaX, "love", 5)
                    ch_e "Try as I might, I can't stay mad at you."
                    if "boyfriend" not in EmmaX.player_petnames:
                        $ EmmaX.player_petnames.append("boyfriend")
                    $ EmmaX.traits.remove("ex")
                    if "EmmaYes" in Player.traits:
                        $ Player.traits.remove("EmmaYes")
                    $ Player.Harem.append(EmmaX)
                    call Harem_Initiation
                    "[EmmaX.name] leans in and kisses you deeply."
                    $ EmmaX.change_face("kiss", 1)
                    $ EmmaX.permanent_History["kiss"] += 1
                elif EmmaX.love >= 600 and approval_check(EmmaX, 1500):
                    $ EmmaX.change_face("smile", 1)
                    call change_Girl_stat(EmmaX, "love", 5)
                    ch_e "Hrm, very well."
                    if "boyfriend" not in EmmaX.player_petnames:
                        $ EmmaX.player_petnames.append("boyfriend")
                    $ EmmaX.traits.remove("ex")
                    if "EmmaYes" in Player.traits:
                        $ Player.traits.remove("EmmaYes")
                    $ Player.Harem.append(EmmaX)
                    call Harem_Initiation
                    $ EmmaX.change_face("kiss", 1)
                    "[EmmaX.name] gives you a quick kiss."
                    $ EmmaX.change_face("sly", 1)
                    $ EmmaX.permanent_History["kiss"] += 1
                elif EmmaX.obedience >= 500:
                    $ EmmaX.change_face("sad")
                    ch_e "Let's keep things as they are, for now."
                elif EmmaX.inhibition >= 500:
                    $ EmmaX.change_face("perplexed")
                    ch_e "No, \"casual\" works better for the time being."
                else:
                    $ EmmaX.change_face("perplexed", 1)
                    ch_e "I can't be bothered with second chances."



            "I wanted to ask about [[another girl]" if EmmaX in Player.Harem:
                call AskDateOther

            "I think we should break up." if EmmaX in Player.Harem:
                if "breakup talk" in EmmaX.daily_history:
                    ch_e "You must be joking. Again?"
                else:
                    call Breakup (EmmaX)
            "About that talk we had before. . .":

                menu:
                    "When you said you loved me. . ." if "lover" not in EmmaX.traits and EmmaX.event_happened[6] >= 20:
                        call Emma_Love_Redux
                    "You said you wanted me to be more in control?" if "sir" not in EmmaX.player_petnames and "sir" in EmmaX.history:
                        if "asked sub" in EmmaX.daily_history:
                            ch_e "I did, you didn't."
                        else:
                            call Emma_Sub_Asked
                    "You said you wanted me to be your Master?" if "master" not in EmmaX.player_petnames and "master" in EmmaX.history:
                        if "asked sub" in EmmaX.daily_history:
                            ch_e "I seem to recall something about that. . ."
                        else:
                            call Emma_Sub_Asked
                    "Never mind":
                        pass
            "Never mind":
                return

    return

label Emma_OtherWoman(counter=0):

    if not Player.Harem:
        return
    $ counter = int((EmmaX.likes[Player.Harem[0].tag] - 500)/2)

    $ EmmaX.change_face("perplexed")
    if len(Player.Harem) >= 2:
        ch_e "But you're with [Player.Harem[0].name] right now, among others, apparently."
    else:
        ch_e "But you're with [Player.Harem[0].name] right now."
    menu:
        extend ""
        "She said I can be with you too." if "EmmaYes" in Player.traits:
            if approval_check(EmmaX, 1800, Bonus = counter):
                $ EmmaX.change_face("smile", 1)
                if EmmaX.love >= EmmaX.obedience:
                    ch_e "I suppose you're worth sharing."
                elif EmmaX.obedience >= EmmaX.inhibition:
                    ch_e "If she can share then I can."
                else:
                    ch_e "Sure, why not."
            else:
                $ EmmaX.change_face("angry", 1)
                ch_e "I really don't care what that little slut does."
                $ renpy.pop_call()


        "I could ask if she'd be ok with me dating you both." if "EmmaYes" not in Player.traits:
            if approval_check(EmmaX, 1800, Bonus = counter):
                $ EmmaX.change_face("smile", 1)
                if EmmaX.love >= EmmaX.obedience:
                    ch_e "I suppose you're worth sharing."
                elif EmmaX.obedience >= EmmaX.inhibition:
                    ch_e "If she can share then I can."
                else:
                    ch_e "Sure, why not."
                ch_e "Go ask her, give me the night to think about it, and then come back tomorrow with her answer."
            else:
                $ EmmaX.change_face("angry", 1)
                ch_e "I really don't care what that little slut does."
            $ renpy.pop_call()
        "What she doesn't know won't hurt her.":

            if not approval_check(EmmaX, 1800, Bonus = -counter):
                $ EmmaX.change_face("angry", 1)
                if not approval_check(EmmaX, 1800):
                    ch_e "I don't want you either."
                else:
                    ch_e "I don't want to share you."
                $ renpy.pop_call()
            else:
                $ EmmaX.change_face("smile", 1)
                if EmmaX.love >= EmmaX.obedience:
                    ch_e "I suppose we could arrange something."
                elif EmmaX.obedience >= EmmaX.inhibition:
                    ch_e "If you insist."
                else:
                    ch_e "I don't see why not."
                $ EmmaX.traits.append("downlow")
        "I can break it off with her.":

            $ EmmaX.change_face("sad")
            ch_e "Then we can talk after you have."
            $ renpy.pop_call()
        "You're right, I was dumb to ask.":

            $ EmmaX.change_face("sad")
            ch_e "Obviously. . ."
            $ renpy.pop_call()
    return


label Emma_About(Check=0):
    if Check not in all_Girls:
        ch_e "Who?"
        return
    ch_e "What do I think about her? Well. . ."
    if Check == RogueX:
        if "poly Rogue" in EmmaX.traits:
            ch_e "As you're aware, we've shared a great deal. . ."
        elif EmmaX.likes[RogueX.tag] >= 900:
            ch_e "I do find her rather mesmerizing. . ."
        elif EmmaX.likes[RogueX.tag] >= 800:
            ch_e "That accent certainly did grow on me. . ."
        elif EmmaX.likes[RogueX.tag] >= 700:
            ch_e "We've become quite close."
        elif EmmaX.likes[RogueX.tag] >= 600:
            ch_e "I'm rather fond of her."
        elif EmmaX.likes[RogueX.tag] >= 500:
            ch_e "She's an adequate student."
        elif EmmaX.likes[RogueX.tag] >= 400:
            ch_e "She can be a bit of a handful."
        elif EmmaX.likes[RogueX.tag] >= 300:
            ch_e "I can barely tolerate her disrespectful nature."
        else:
            ch_e "That swamp rat? What about her?"
    elif Check == KittyX:
        if "poly Kitty" in EmmaX.traits:
            ch_e "As you're aware, we do get along quite well. . ."
        elif EmmaX.likes[KittyX.tag] >= 900:
            ch_e "She is rather. . . flexible. . ."
        elif EmmaX.likes[KittyX.tag] >= 800:
            ch_e "She is rather adorable. . ."
        elif EmmaX.likes[KittyX.tag] >= 700:
            ch_e "She's something of a friend at this point."
        elif EmmaX.likes[KittyX.tag] >= 600:
            ch_e "Once you get to know her, she's not bad."
        elif EmmaX.likes[KittyX.tag] >= 500:
            ch_e "She's an adequate student."
        elif EmmaX.likes[KittyX.tag] >= 400:
            ch_e "She can be a bit of a know it all."
        elif EmmaX.likes[KittyX.tag] >= 300:
            ch_e "I can't stand her constant questions."
        else:
            ch_e "That little bitch?"
    elif Check == LauraX:
        if "poly Laura" in EmmaX.traits:
            ch_e "She is quite. . . energetic. . ."
        elif EmmaX.likes[LauraX.tag] >= 900:
            ch_e "She's very durable. . ."
        elif EmmaX.likes[LauraX.tag] >= 800:
            ch_e "She has a rough quality that is quite exciting. . ."
        elif EmmaX.likes[LauraX.tag] >= 700:
            ch_e "She's something of a friend at this point."
        elif EmmaX.likes[LauraX.tag] >= 600:
            ch_e "Once you get to know her, she's not bad."
        elif EmmaX.likes[LauraX.tag] >= 500:
            ch_e "She's an adequate student."
        elif EmmaX.likes[LauraX.tag] >= 400:
            ch_e "She is a bit rough around the edges."
        elif EmmaX.likes[LauraX.tag] >= 300:
            ch_e "Yes, a bit feral, that one."
        else:
            ch_e "I'd put her down myself if I didn't have responsibilites."
    elif Check == JeanX:
        if "poly Jean" in EmmaX.traits:
            ch_e "As you're aware, we've shared a great deal. . ."
        elif EmmaX.likes[JeanX.tag] >= 900:
            ch_e "I do find her rather mesmerizing. . ."
        elif EmmaX.likes[JeanX.tag] >= 800:
            ch_e "She really is lovely, when you give her a chance. . ."
        elif EmmaX.likes[JeanX.tag] >= 700:
            ch_e "I have grown to like her. . ."
        elif EmmaX.likes[JeanX.tag] >= 600:
            ch_e "I'm rather fond of her."
        elif EmmaX.likes[JeanX.tag] >= 500:
            ch_e "She's an adequate student."
        elif EmmaX.likes[JeanX.tag] >= 400:
            ch_e "She can be a bit of a pill."
        elif EmmaX.likes[JeanX.tag] >= 300:
            ch_e "I can barely tollerate her arrogance."
        else:
            ch_e "That bitch? What about her?"
    elif Check == StormX:
        if "poly Storm" in EmmaX.traits:
            ch_e "She is marvelously experienced. . ."
        elif EmmaX.likes[StormX.tag] >= 900:
            ch_e "She complements me well. . ."
        elif EmmaX.likes[StormX.tag] >= 800:
            ch_e "She has a lovely figure. . ."
        elif EmmaX.likes[StormX.tag] >= 700:
            ch_e "She's something of a friend."
        elif EmmaX.likes[StormX.tag] >= 600:
            ch_e "She's an excellent colleague."
        elif EmmaX.likes[StormX.tag] >= 500:
            ch_e "She's an adequate colleague."
        elif EmmaX.likes[StormX.tag] >= 400:
            ch_e "She is a bit rough around the edges"
        elif EmmaX.likes[StormX.tag] >= 300:
            ch_e "The carpet matches the drapes, you know. Of course you would."
        else:
            ch_e "I wish I could convince Charles to fire her."
    elif Check == JubesX:
        if "poly Jubes" in EmmaX.traits:
            ch_e "As you're aware, we do get along quite well. . ."
        elif EmmaX.likes[JubesX.tag] >= 900:
            ch_e "She is rather. . . flexible. . ."
        elif EmmaX.likes[JubesX.tag] >= 800:
            ch_e "She is rather lovely. . ."
        elif EmmaX.likes[JubesX.tag] >= 700:
            ch_e "She's something of a friend at this point."
        elif EmmaX.likes[JubesX.tag] >= 600:
            ch_e "Once you get to know her, she's not bad."
        elif EmmaX.likes[JubesX.tag] >= 500:
            ch_e "She's an adequate student."
        elif EmmaX.likes[JubesX.tag] >= 400:
            ch_e "She can be a bit of a biter"
        elif EmmaX.likes[JubesX.tag] >= 300:
            ch_e "She is very disruptive."
        else:
            ch_e "That little bitch?"
    return


label Emma_Monogamy:

    menu:
        "Could you not hook up with other girls?" if "monogamous" not in EmmaX.traits:
            if EmmaX.thirst >= 50 and not approval_check(EmmaX, 1800, "LO", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1)
                if "monogamous" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "obedience", -2)
                ch_e "You know, it's not like you leave me any alternatives. . ."
                return
            elif approval_check(EmmaX, 1300, "LO", taboo_modifier=0) and EmmaX.love >= EmmaX.obedience:

                $ EmmaX.change_face("sly", 1)
                if "monogamous" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "love", 1)
                ch_e "Jealousy is an adorable look on you. . ."
                ch_e "I suppose I could restain myself. . ."
            elif approval_check(EmmaX, 750, "O", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "If you insist. . ."
            else:

                $ EmmaX.change_face("sly", 1, brows = "confused")
                ch_e "I'm afraid my affairs are my own business."
                ch_e "Don't leave me wanting. . ."
                return
            if "monogamous" not in EmmaX.daily_history:
                call change_Girl_stat(EmmaX, "obedience", 3)
            $ EmmaX.add_word(1, 0, "monogamous")
            $ EmmaX.traits.append("monogamous")
        "Don't hook up with other girls." if "monogamous" not in EmmaX.traits:
            if approval_check(EmmaX, 900, "O", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "Oh very well."
            elif EmmaX.thirst >= 60 and not approval_check(EmmaX, 1700, "LO", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1)
                if "monogamous" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "obedience", -2)
                ch_e "You know, it's not like you leave me any alternatives. . ."
                return
            elif approval_check(EmmaX, 600, "O", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "If I must. . ."
            elif approval_check(EmmaX, 1500, "LO", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1)
                ch_e "You shouldn't take that tone with me."
                ch_e "But I suppose I could let it slide. . ."
            else:

                $ EmmaX.change_face("sly", 1, brows = "confused")
                ch_e "My affairs are my own business."
                return
            if "monogamous" not in EmmaX.daily_history:
                call change_Girl_stat(EmmaX, "obedience", 3)
            $ EmmaX.add_word(1, 0, "monogamous")
            $ EmmaX.traits.append("monogamous")
        "It's ok if you hook up with other girls." if "monogamous" in EmmaX.traits:
            if approval_check(EmmaX, 700, "O", taboo_modifier=0):
                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "Of course."
            elif approval_check(EmmaX, 800, "L", taboo_modifier=0):
                $ EmmaX.change_face("sly", 1)
                ch_e "Only if I find myself. . . available. . ."
            else:
                $ EmmaX.change_face("sly", 1, brows = "confused")
                if "monogamous" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "love", -2)
                ch_e "I wasn't aware that I needed your permission."
            if "monogamous" not in EmmaX.daily_history:
                call change_Girl_stat(EmmaX, "obedience", 3)
            if "monogamous" in EmmaX.traits:
                $ EmmaX.traits.remove("monogamous")
            $ EmmaX.add_word(1, 0, "monogamous")
        "Never mind.":
            pass
    return



label Emma_Jumped:

    ch_p "Hey, Remember that time you threw yourself at me?"
    $ EmmaX.change_face("sly", 1, brows = "confused")
    ch_e "I believe I recall something like that."
    menu:
        ch_e "What of it?"
        "Could you maybe just ask instead?" if "chill" not in EmmaX.traits:
            if EmmaX.thirst >= 60 and not approval_check(EmmaX, 1600, "LO", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1)
                if "chill" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "obedience", -2)
                ch_e "I do have certain. . . needs that must be met."
                ch_e "Stay on your toes."
                return
            elif approval_check(EmmaX, 1100, "LO", taboo_modifier=0) and EmmaX.love >= EmmaX.obedience:

                $ EmmaX.change_face("sly", 1)
                if "chill" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "love", 1)
                ch_e "I didn't intend to upset you, [EmmaX.player_petname]. . ."
                ch_e "I'll try to keep control. . ."
            elif approval_check(EmmaX, 600, "O", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "If that's what would make you comfortable. . ."
            else:

                $ EmmaX.change_face("sly", 1, brows = "confused")
                ch_e "I'll see what I can do about that."
                ch_e "Stay on your toes."
                return
            if "chill" not in EmmaX.daily_history:
                call change_Girl_stat(EmmaX, "obedience", 3)
            $ EmmaX.add_word(1, 0, "chill")
            $ EmmaX.traits.append("chill")
        "Don't bother me like that." if "chill" not in EmmaX.traits:
            if approval_check(EmmaX, 900, "O", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "Oh, very well."
            elif EmmaX.thirst >= 60 and not approval_check(EmmaX, 600, "O", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1)
                if "chill" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "obedience", -2)
                ch_e "I do have certain. . . needs that must be met."
                ch_e "Stay on your toes."
                return
            elif approval_check(EmmaX, 450, "O", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "Well, I wouldn't want to be a \"bother\". . ."
            elif approval_check(EmmaX, 500, "LO", taboo_modifier=0) and not approval_check(EmmaX, 500, "I", taboo_modifier=0):

                $ EmmaX.change_face("sly", 1)
                ch_e "Don't press your luck, [EmmaX.player_petname]."
                ch_e "I will try to give you some space, however. . ."
            else:

                $ EmmaX.change_face("sly", 1, brows = "confused")
                ch_e "I'll see what I can do about that."
                ch_e "Stay on your toes."
                return
            if "chill" not in EmmaX.daily_history:
                call change_Girl_stat(EmmaX, "obedience", 3)
            $ EmmaX.add_word(1, 0, "chill")
            $ EmmaX.traits.append("chill")
        "Knock yourself out.":
            if approval_check(EmmaX, 800, "L", taboo_modifier=0):
                $ EmmaX.change_face("sly", 1)
                ch_e "You can count on it. . ."
            elif approval_check(EmmaX, 700, "O", taboo_modifier=0):
                $ EmmaX.change_face("sly", 1, eyes = "side")
                ch_e "Very well."
            else:
                $ EmmaX.change_face("sly", 1, brows = "confused")
                if "chill" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "love", -2)
                ch_e "We'll see. . ."
            if "chill" not in EmmaX.daily_history:
                call change_Girl_stat(EmmaX, "obedience", 3)
            if "chill" in EmmaX.traits:
                $ EmmaX.traits.remove("chill")
            $ EmmaX.add_word(1, 0, "chill")
        "Um, never mind.":
            pass
    return




label Emma_Hungry:
    if EmmaX.had_chat[3]:
        ch_e "I do enjoy your taste. . ."
    elif EmmaX.had_chat[2]:
        ch_e "You know, that serum of yours has a rather. . . familiar taste to it."
    else:
        ch_e "I do enjoy your taste. . ."
    $ EmmaX.traits.append("hungry")
return





label Emma_SexChat:
    $ line = "Hmm? What did you want to talk about?" if not line else line
    while True:
        menu:
            ch_e "[line]"
            "My favorite thing to do is. . .":
                if "setfav" in EmmaX.daily_history:
                    ch_e "I'm aware. You just told me earlier."
                else:
                    menu:
                        "Sex.":
                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "sex":
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "I'm well aware. . ."
                            elif EmmaX.favorite_action == "sex":
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 10)
                                ch_e "Oh. . . as chance would have it. . ."
                            elif EmmaX.permanent_History["sex"]:
                                ch_e "I can see why."
                            else:
                                $ EmmaX.change_face("perplexed")
                                ch_e "And exactly {i}who{/i} are you having sex {i}with?{/i}"
                            $ EmmaX.player_favorite_action = "sex"
                        "Anal.":

                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "anal":
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "So you've told me. . ."
                            elif EmmaX.favorite_action == "anal":
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 10)
                                ch_e "{i}Mine too{/i}. . ."
                            elif EmmaX.permanent_History["anal"] >= 10:
                                ch_e "It certainly is a workout. . ."
                            elif not EmmaX.permanent_History["anal"]:
                                $ EmmaX.change_face("perplexed")
                                ch_e "Who's ass {i}are{/i} you fucking?"
                            else:
                                $ EmmaX.change_face("bemused")
                                ch_e "Yes, you did seem enthusiastic. . ."
                            $ EmmaX.player_favorite_action = "anal"
                        "Blowjobs.":

                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "blowjob":
                                call change_Girl_stat(EmmaX, "lust", 3)
                                ch_e "Yes, so you've said. . ."
                            elif EmmaX.favorite_action == "blowjob":
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "Hmm, you are delicious. . ."
                            elif EmmaX.permanent_History["blowjob"] >= 10:
                                ch_e "I certainly can't complain . . ."
                            elif not EmmaX.permanent_History["blowjob"]:
                                $ EmmaX.change_face("perplexed")
                                ch_e "Oh? Is some little whore sucking you off?"
                            else:
                                $ EmmaX.change_face("bemused")
                                ch_e "Yes, I enjoy it as well. . . ."
                            $ EmmaX.player_favorite_action = "blowjob"
                        "Titjobs.":

                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "titjob":
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "So you're said. . ."
                            elif EmmaX.favorite_action == "titjob":
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 7)
                                ch_e "I really enjoy it too. . ."
                            elif EmmaX.permanent_History["titjob"] >= 10:
                                ch_e "I can't imagine why . . ."
                            elif not EmmaX.permanent_History["titjob"]:
                                $ EmmaX.change_face("perplexed")
                                ch_e "Oh, is someone else providing that service?"
                            else:
                                $ EmmaX.change_face("bemused")
                                ch_e "I can understand why. . ."
                            $ EmmaX.player_favorite_action = "titjob"
                        "Footjobs.":

                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "footjob":
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "Yes, so you've said. . ."
                            elif EmmaX.favorite_action == "footjob":
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 7)
                                ch_e "It certainly is a diversion. . ."
                            elif EmmaX.permanent_History["footjob"] >= 10:
                                ch_e "Yes, it certainly is a workout . . ."
                            elif not EmmaX.permanent_History["footjob"]:
                                $ EmmaX.change_face("perplexed")
                                ch_e "Oh, is some little skank offering footsies now?"
                            else:
                                $ EmmaX.change_face("bemused")
                                ch_e "It certainly is a diversion. . ."
                            $ EmmaX.player_favorite_action = "footjob"
                        "Handjobs.":

                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "handjob":
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "Yes, so you've said. . ."
                            if EmmaX.favorite_action == "handjob":
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 7)
                                ch_e "It certainly is a diversion. . ."
                            elif EmmaX.permanent_History["handjob"] >= 10:
                                ch_e "Yes, it certainly is a workout . . ."
                            elif not EmmaX.permanent_History["handjob"]:
                                $ EmmaX.change_face("perplexed")
                                ch_e "Oh, is some little skank offering handies now?"
                            else:
                                $ EmmaX.change_face("bemused")
                                ch_e "It certainly is a diversion. . ."
                            $ EmmaX.player_favorite_action = "handjob"
                        "Feeling you up.":

                            $ counter = EmmaX.permanent_History["fondle_breasts"]+ EmmaX.permanent_History["fondle_thighs"]+ EmmaX.permanent_History["suck_breasts"] + EmmaX.permanent_History["hotdog"]
                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "fondle":
                                call change_Girl_stat(EmmaX, "lust", 3)
                                ch_e "I've heard that before. . ."
                            elif EmmaX.favorite_action in ("hotdog", "suck_breasts", "fondle_breasts", "fondle_thighs"):
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "You do have a way with my body . ."
                            elif not counter:
                                $ EmmaX.change_face("perplexed")
                                ch_e "I can't imagine who youre feeling up. Yet."
                            else:
                                $ EmmaX.change_face("bemused")
                                ch_e "You have a very deft hand . . ."
                            $ EmmaX.player_favorite_action = "fondle"
                            $ counter = 0
                        "Kissing you.":

                            $ EmmaX.change_face("sly")
                            if EmmaX.player_favorite_action == "kiss":
                                call change_Girl_stat(EmmaX, "love", 3)
                                ch_e "I'm well aware. . ."
                            elif EmmaX.favorite_action == "kiss":
                                call change_Girl_stat(EmmaX, "love", 5)
                                call change_Girl_stat(EmmaX, "lust", 5)
                                ch_e "For some reason, the romantic in me agrees. . ."
                            elif EmmaX.permanent_History["kiss"] >= 10:
                                ch_e "I love kissing you too . . ."
                            elif not EmmaX.permanent_History["kiss"]:
                                $ EmmaX.change_face("perplexed")
                                ch_e "Who {i}are{/i} you kissing, [EmmaX.player_petname]?"
                            else:
                                $ EmmaX.change_face("bemused")
                                ch_e "How romantic."
                            $ EmmaX.player_favorite_action = "kiss"

                    $ EmmaX.daily_history.append("setfav")
            "What's your favorite thing to do?":

                if not approval_check(EmmaX, 800):
                    $ EmmaX.change_face("perplexed")
                    ch_e "I don't believe that's an appropriate question. . ."
                else:
                    if EmmaX.SEXP >= 50:
                        $ EmmaX.change_face("sly")
                        ch_e "You really should know already . ."
                    else:
                        $ EmmaX.change_face("bemused")
                        $ EmmaX.eyes = "side"
                        ch_e "Hmm, I suppose I could tell you. . ."


                    if not EmmaX.favorite_action or EmmaX.favorite_action == "kiss":
                        ch_e "Call me a romantic, but I enjoy kissing you. . ."
                    elif EmmaX.favorite_action == "anal":
                        ch_e "I really enjoy anal."
                    elif EmmaX.favorite_action == "eat_ass":
                        ch_e "I enjoy it when you lick my asshole."
                    elif EmmaX.favorite_action == "finger_ass":
                        ch_e "I enjoy it when you stick a finger in my ass."
                    elif EmmaX.favorite_action == "sex":
                        ch_e "I like when you fuck me hard."
                    elif EmmaX.favorite_action == "eat_pussy":
                        ch_e "I like when you lick my pussy."
                    elif EmmaX.favorite_action == "fondle_pussy":
                        ch_e "I like when you finger me."
                    elif EmmaX.favorite_action == "blowjob":
                        ch_e "I quite enjoy sucking you, is that a problem?"
                    elif EmmaX.favorite_action == "titjob":
                        ch_e "I enjoy using my tits."
                    elif EmmaX.favorite_action == "footjob":
                        ch_e "I do enjoy using my feet."
                    elif EmmaX.favorite_action == "handjob":
                        ch_e "I enjoy stroking you off."
                    elif EmmaX.favorite_action == "hotdog":
                        ch_e "I enjoy it when you grind against me."
                    elif EmmaX.favorite_action == "suck_breasts":
                        ch_e "You are good at sucking my tits."
                    elif EmmaX.favorite_action == "fondle_breasts":
                        ch_e "You are good at fondling my tits."
                    elif EmmaX.favorite_action == "fondle_thighs":
                        ch_e "I enjoy when you massage my thighs."
                    else:
                        ch_e "I'm really not sure. . ."



            "Don't talk as much during sex." if "vocal" in EmmaX.traits:
                if "setvocal" in EmmaX.daily_history:
                    $ EmmaX.change_face("perplexed")
                    ch_e "You've made yourself clear on the matter."
                else:
                    if approval_check(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                        $ EmmaX.change_face("bemused")
                        call change_Girl_stat(EmmaX, "obedience", 1)
                        ch_e "Oh, very well. . ."
                        $ EmmaX.traits.remove("vocal")
                    elif approval_check(EmmaX, 700, "O"):
                        $ EmmaX.change_face("sadside")
                        call change_Girl_stat(EmmaX, "obedience", 1)
                        ch_e "I suppose I could, [EmmaX.player_petname]."
                        $ EmmaX.traits.remove("vocal")
                    elif approval_check(EmmaX, 600):
                        $ EmmaX.change_face("sly")
                        call change_Girl_stat(EmmaX, "love", -3)
                        call change_Girl_stat(EmmaX, "obedience", -1)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "Don't presume to tell me what to say, [EmmaX.player_petname]."
                    else:
                        $ EmmaX.change_face("angry")
                        call change_Girl_stat(EmmaX, "love", -5)
                        call change_Girl_stat(EmmaX, "obedience", -3)
                        call change_Girl_stat(EmmaX, "inhibition", 10)
                        ch_e "I'll say what I wish, and you'll enjoy it."

                    $ EmmaX.daily_history.append("setvocal")
            "Talk dirty to me during sex." if "vocal" not in EmmaX.traits:
                if "setvocal" in EmmaX.daily_history:
                    $ EmmaX.change_face("perplexed")
                    ch_e "We've discussed this already."
                else:
                    if approval_check(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                        $ EmmaX.change_face("sly")
                        call change_Girl_stat(EmmaX, "obedience", 2)
                        ch_e "Mmmm, I believe I can do that. . ."
                        $ EmmaX.traits.append("vocal")
                    elif approval_check(EmmaX, 700, "O"):
                        $ EmmaX.change_face("sadside")
                        call change_Girl_stat(EmmaX, "obedience", 2)
                        ch_e "If that's what you wish, [EmmaX.player_petname]."
                        $ EmmaX.traits.append("vocal")
                    elif approval_check(EmmaX, 600):
                        $ EmmaX.change_face("sly")
                        call change_Girl_stat(EmmaX, "obedience", 3)
                        ch_e "I suppose I could, [EmmaX.player_petname]."
                        $ EmmaX.traits.append("vocal")
                    else:
                        $ EmmaX.change_face("angry")
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "If I feel like it."

                    $ EmmaX.daily_history.append("setvocal")


            "Don't do your own thing as much during sex." if "passive" not in EmmaX.traits:
                if "initiative" in EmmaX.daily_history:
                    $ EmmaX.change_face("perplexed")
                    ch_e "I believe we've discussed this."
                else:
                    if approval_check(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                        $ EmmaX.change_face("bemused")
                        call change_Girl_stat(EmmaX, "obedience", 1)
                        ch_e "Oh, so you want to take charge? . ."
                        $ EmmaX.traits.append("passive")
                    elif approval_check(EmmaX, 700, "O"):
                        $ EmmaX.change_face("sadside")
                        call change_Girl_stat(EmmaX, "obedience", 1)
                        ch_e "I'll await your instruction, [EmmaX.player_petname]."
                        $ EmmaX.traits.append("passive")
                    elif approval_check(EmmaX, 600):
                        $ EmmaX.change_face("sly")
                        call change_Girl_stat(EmmaX, "love", -3)
                        call change_Girl_stat(EmmaX, "obedience", -1)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "Oh, you don't mean that, [EmmaX.player_petname]."
                    else:
                        $ EmmaX.change_face("angry")
                        call change_Girl_stat(EmmaX, "love", -5)
                        call change_Girl_stat(EmmaX, "obedience", -3)
                        call change_Girl_stat(EmmaX, "inhibition", 10)
                        ch_e "You wish."

                    $ EmmaX.daily_history.append("initiative")
            "Take more initiative during sex." if "passive" in EmmaX.traits:
                if "initiative" in EmmaX.daily_history:
                    $ EmmaX.change_face("perplexed")
                    ch_e "I believe we've discussed this."
                else:
                    if approval_check(EmmaX, 1000) and EmmaX.obedience <= EmmaX.love:
                        $ EmmaX.change_face("bemused")
                        call change_Girl_stat(EmmaX, "obedience", 1)
                        ch_e "Oh, you know that I will. . ."
                        $ EmmaX.traits.remove("passive")
                    elif approval_check(EmmaX, 700, "O"):
                        $ EmmaX.change_face("sadside")
                        call change_Girl_stat(EmmaX, "obedience", 1)
                        ch_e "I can do that, [EmmaX.player_petname]."
                        $ EmmaX.traits.remove("passive")
                    elif approval_check(EmmaX, 600):
                        $ EmmaX.change_face("sly")
                        call change_Girl_stat(EmmaX, "obedience", 3)
                        ch_e "I suppose I might, [EmmaX.player_petname]."
                        $ EmmaX.traits.remove("passive")
                    else:
                        $ EmmaX.change_face("angry")
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "We'll see."

                    $ EmmaX.daily_history.append("initiative")


            "About getting Jumped" if "jumped" in EmmaX.history:
                call Emma_Jumped

            "About that \"mind screen\"" if "screen" in EmmaX.traits or "noscreen" in EmmaX.traits:
                ch_e "You mean how I can make Charles ignore us sometimes?"
                menu:
                    extend ""
                    "Yeah, do that." if "noscreen" in EmmaX.traits:
                        ch_e "Lovely. . ."
                        $ EmmaX.traits.append("screen")
                    "Don't do that anymore, I want him to know." if "screen" in EmmaX.traits:
                        ch_e "Oh, you are a naughty one."
                        if approval_check(EmmaX, 900, "OI"):
                            $ EmmaX.change_face("sad")
                            ch_e "Very well, we won't do that."
                            $ EmmaX.change_face("bemused")
                            $ EmmaX.traits.append("noscreen")
                        else:
                            ch_e "However, I still don't appreciate his interference."
                            ch_e "I'll use the screen anyway."
                    "Never mind.":
                        pass
            "About when you masturbate":

                call NoFap (EmmaX)

            "Have you considered maybe having some fun in public?" if "taboocheck" not in EmmaX.history and "taboo" not in EmmaX.history:
                call Emma_taboo_Talk
            "We talked about maybe having some fun in public?" if "taboocheck" in EmmaX.history and "taboo" not in EmmaX.history:
                call Emma_taboo_Talk

            "Have you considered maybe having a threesome?" if "threecheck" not in EmmaX.history and "threesome" not in EmmaX.history:
                call Emma_ThreeCheck
            "We talked about maybe having a threesome?" if "threecheck" in EmmaX.history and "threesome" not in EmmaX.history:
                call Emma_ThreeCheck

            "Never mind" if line == "Hmm? What did you want to talk about?":
                return
            "That's all." if line != "Hmm? What did you want to talk about?":
                return
        if line == "Yeah, what did you want to talk about?":
            $ line = "Anything else?"
    return



label Emma_Chitchat(O=0, Options = ["default", "default", "default"]):
    $ round -= 3 if round > 3 else (round-1)
    if O:
        $ Options = [O]
    else:
        if EmmaX not in Player.Phonebook:
            if approval_check(EmmaX, 850, "LI"):
                ch_e "If you'd like to reach me. . . after hours, here's my number."
                $ Player.Phonebook.append(EmmaX)
                return
            elif approval_check(EmmaX, 500, "OI"):
                ch_e "I should let you know how to contact me."
                $ Player.Phonebook.append(EmmaX)
                return

        if "hungry" not in EmmaX.traits and (EmmaX.permanent_History["swallowed"] + EmmaX.had_chat[2]) >= 10 and EmmaX.location == Player.location:
            call Emma_Hungry
            return
        if Player.location != "bg_restaurant" and Player.location != "bg_halloween" and (not taboo or approval_check(EmmaX, 800, "I")):
            if EmmaX.location == Player.location and EmmaX.thirst >= 30 and "refused" not in EmmaX.daily_history and "quicksex" not in EmmaX.daily_history:
                $ Girl.change_face("sly", 1, eyes = "down")
                ch_e "I've got an itch. . . "
                "[EmmaX.name] draws her hand down her body and grazes her pussy."
                $ Girl.change_face("sly", 1)
                ch_e ". . think you can scratch it?"
                call Quick_Sex (EmmaX)
                return



        if "classcaught" in EmmaX.traits:
            if "caught" in EmmaX.daily_history and "caught chat" not in EmmaX.daily_history:
                $ Options.append("caught")
            if "screen" not in EmmaX.traits and "noscreen" not in EmmaX.traits and "screen" in JeanX.traits:
                $ Options.append("screen")
            if EmmaX.event_happened[0] and "key" not in EmmaX.had_chat:
                $ Options.append("key")
            if "lover" in EmmaX.player_petnames and approval_check(EmmaX, 900, "L"):
                $ Options.append("luv")

            if "mandrill" in Player.traits and "cologne chat" not in EmmaX.daily_history:
                $ Options.append("mandrill")
            if "purple" in Player.traits and "cologne chat" not in EmmaX.daily_history:
                $ Options.append("purple")
            if "corruption" in Player.traits and "cologne chat" not in EmmaX.daily_history:
                $ Options.append("corruption")

            if EmmaX.went_on_date >= 1 and Player.location != "bg_restaurant":

                $ Options.append("dated")
            if "cheek" in EmmaX.daily_history and "cheek" not in EmmaX.had_chat:

                $ Options.append("cheek")
            if EmmaX.permanent_History["kiss"] >= 5:

                $ Options.append("kissed")
            if "dangerroom" in Player.daily_history:

                $ Options.append("dangerroom")
            if "showered" in EmmaX.daily_history:

                $ Options.append("showercaught")
            if "fondle_breasts" in EmmaX.daily_history or "fondle_pussy" in EmmaX.daily_history or "fondle_ass" in EmmaX.daily_history:

                $ Options.append("fondled")
            if "Dazzler and Longshot" in EmmaX.inventory and "256 Shades of Grey" in EmmaX.inventory and "Avengers Tower Penthouse" in EmmaX.inventory:

                if "book" not in EmmaX.had_chat:
                    $ Options.append("booked")
            if "lace_bra" in EmmaX.inventory or "lace_panties" in EmmaX.inventory:

                if "lingerie" not in EmmaX.had_chat:
                    $ Options.append("lingerie")

            if "seenpeen" in EmmaX.history:
                $ Options.append("seenpeen")
            if "topless" in EmmaX.history:
                $ Options.append("topless")
            if "bottomless" in EmmaX.history:
                $ Options.append("bottomless")

            if EmmaX.permanent_History["handjob"]:

                $ Options.append("handy")
            if EmmaX.permanent_History["swallowed"]:

                $ Options.append("swallowed")
            if "cleaned" in EmmaX.daily_history or "painted" in EmmaX.daily_history:

                $ Options.append("facial")
            if EmmaX.permanent_History["sleepover"]:

                $ Options.append("sleepwear")
            if EmmaX.permanent_History["creampied"] or EmmaX.permanent_History["anal_creampied"]:

                $ Options.append("creampie")
            if EmmaX.permanent_History["sex"] or EmmaX.permanent_History["anal"]:

                $ Options.append("sexed")
            if EmmaX.permanent_History["anal"]:

                $ Options.append("anal")
            if "public" in EmmaX.history and "public" not in EmmaX.had_chat:
                $ Options.append("public")

            if (Player.location == "bg_emma" or Player.location == "bg_player") and "relationship" not in EmmaX.daily_history:
                if "lover" not in EmmaX.player_petnames and EmmaX.love >= 950 and EmmaX.event_happened[6] != 20:
                    $ Options.append("lover?")
                elif "sir" not in EmmaX.history and EmmaX.obedience >= 500:
                    $ Options.append("sir?")
                elif "daddy" not in EmmaX.player_petnames and approval_check(EmmaX, 750, "L") and approval_check(EmmaX, 500, "O") and approval_check(EmmaX, 500, "I"):
                    $ Options.append("daddy?")
                elif "master" not in EmmaX.history and EmmaX.obedience >= 800 and "sir" in EmmaX.player_petnames:
                    $ Options.append("master?")
                elif "sex friend" not in EmmaX.player_petnames and EmmaX.inhibition >= 500 and Player.location == "bg_classroom" and time_index == 2:
                    $ Options.append("sexfriend?")
                elif "fuck buddy" not in EmmaX.player_petnames and EmmaX.inhibition >= 800 and Player.location != EmmaX.location:
                    $ Options.append("fuckbuddy?")


        if not approval_check(EmmaX, 300):
            $ Options.append("hate")

    $ renpy.random.shuffle(Options)

    if Options[0] == "mandrill":
        $ EmmaX.daily_history.append("cologne chat")
        $ EmmaX.change_face("confused")
        ch_e "(sniff, sniff). . . you aren't using that cheap baboon musk, are you? . ."
        $ EmmaX.change_face("perplexed", 1)
        ch_e ". . . though I suppose. . . he wasn't that bad. . ."
    elif Options[0] == "purple":
        $ EmmaX.daily_history.append("cologne chat")
        $ EmmaX.change_face("sly", 1)
        ch_e "(sniff, sniff). . . huh, what's that smell? . ."
        ch_e ". . . was there anything I could do for you?"
    elif Options[0] == "corruption":
        $ EmmaX.daily_history.append("cologne chat")
        $ EmmaX.change_face("confused")
        ch_e "(sniff, sniff). . . that's. . . ripe. . ."
        $ EmmaX.change_face("sly")
        ch_e ". . . I may have some. . . purpose for you later. . ."

    elif Options[0] == "caught":
        $ EmmaX.change_face("angry", eyes = "side")
        if "caught chat" in EmmaX.had_chat:
            ch_e "I'm getting rather tired of getting dragged into Charles' office."
            ch_e "Perhaps we ought to be more. . . discrete."
            if not approval_check(EmmaX, 500, "I"):
                $ EmmaX.change_face("sly", eyes = "side")
                ch_e "Sometimes. . ."
        else:
            ch_e "Well that was certainly unpleasant."
            ch_e "Xavier talked my ear off for at least an hour."
            ch_e "Some nonsense about \"the responsibilities of an educator.\""
            ch_e "I'll have you know, I take my responsibilities to my students. . ."
            $ EmmaX.change_face("sly")
            ch_e "{i}very{/i} seriously. . ."
            if not approval_check(EmmaX, 500, "I"):
                ch_e "I don't thing we should be so forward in public anymore."
            else:
                ch_e "I did enjoy seeing the old buzzard so worked up though. . ."
            $ EmmaX.had_chat.append("caught chat")

    elif Options[0] == "screen":
        $ EmmaX.change_face("angry")
        ch_e "Charles!"
        ch_e "I'm tired of him interfering in our business!"
        $ EmmaX.change_face("surprised")
        ch_e "Oh!"
        $ EmmaX.change_face("sly")
        ch_e "I've had an idea."
        ch_e "I -could- use my own powers to neutralize his, make it more likely that he'll ignore us."
        menu:
            "Sure, that sounds good.":
                ch_e "Lovely. . ."
                $ EmmaX.traits.append("screen")
            "Nah, I want him to know.":
                ch_e "Oh, you are a naughty one."
                if approval_check(EmmaX, 900, "OI"):
                    $ EmmaX.change_face("sad")
                    ch_e "Very well, we won't do that."
                    $ EmmaX.change_face("bemused")
                    $ EmmaX.traits.append("noscreen")
                else:
                    ch_e "Even so, I don't appreciate his interference."
                    ch_e "I'll use the screen anyway."
                    $ EmmaX.traits.append("screen")
    elif Options[0] == "key":
        if EmmaX.SEXP <= 15:
            ch_e "Now just because I gave you my room key, doesn't mean you shouldn't knock. . ."
        else:
            ch_e "I gave you that key for a reason, you might want to use it sometime. . ."
        $ EmmaX.had_chat.append("key")

    elif Options[0] == "cheek":

        ch_e "Earlier, you brushed my cheek. . ."
        ch_p "Yeah? Was that okay?"
        if approval_check(EmmaX, 600, "L"):
            $ EmmaX.change_face("smile", 1)
            ch_e "Yes, it was. . . intimate."
            $ EmmaX.had_chat.append("cheek")
        elif approval_check(EmmaX, 800):
            $ EmmaX.change_face("normal", 1, eyes = "side")
            ch_e "I. . . suppose so, [EmmaX.player_petname]."
        else:
            $ EmmaX.change_face("confused", 1, eyes = "side")
            ch_e "I just found it to be a bit. . . forward."


    elif Options[0] == "dated":

        ch_e "You should know, I enjoyed our last date. We should do that again sometime."

    elif Options[0] == "kissed":

        $ EmmaX.change_face("sly", 1)
        ch_e "You have some remarkably skilled lips, [EmmaX.player_petname]."
        menu:
            extend ""
            "Hey. . .when you're good, you're good.":
                $ EmmaX.change_face("smile", 1)
                ch_e "Oh, don't let it get to your head."
                ch_e "-unless you're interested in sharing."
            "No. You think?":
                ch_e "Oh, learn to take a compliment, [EmmaX.player_petname]."

    elif Options[0] == "dangerroom":

        $ EmmaX.change_face("sly", 1)
        ch_e "I caught your last Danger Room session,[EmmaX.player_petname]."
        ch_e "You certainly do. . . fill out that uniform."

    elif Options[0] == "showercaught":

        if "shower" in EmmaX.had_chat:
            ch_e "Enjoy the show earlier?"
        else:
            ch_e "I do hope that my appearance in the shower earlier wasn't too distracting."
            $ EmmaX.had_chat.append("shower")
            menu:
                extend ""
                "It was a total accident! I promise!":
                    call change_Girl_stat(EmmaX, "love", 5)
                    call change_Girl_stat(EmmaX, "love", 2)
                    if approval_check(EmmaX, 1000):
                        $ EmmaX.change_face("sly", 1)
                        ch_e "Oh? so I can't count on a repeat performance?"
                    else:
                        $ EmmaX.change_face("smile")
                        ch_e "It happens, just don't make a habit of it."
                "I only have eyes for you.":
                    call change_Girl_stat(EmmaX, "obedience", 5)
                    if approval_check(EmmaX, 1000) or approval_check(EmmaX, 700, "L"):
                        call change_Girl_stat(EmmaX, "love", 3)
                        $ EmmaX.change_face("sly", 1)
                        ch_e "Oh, I'm sure that's true. . ."
                        ch_e "It is nice to hear though."
                    else:
                        call change_Girl_stat(EmmaX, "love", -5)
                        $ EmmaX.change_face("angry", eyes = "side")
                        ch_e "I suppose it's better than being stalked by one-eye over there."
                "Totally on purpose. I regret nothing.":
                    if approval_check(EmmaX, 1200):
                        call change_Girl_stat(EmmaX, "love", 3)
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        $ EmmaX.change_face("sly", 1)
                        ch_e "Welll. . . I suppose I can appreciate your honesty."
                        $ EmmaX.change_face("sly", 1, eyes = "side")
                        ch_e ". . .if not for your lack of follow-through."
                    elif approval_check(EmmaX, 800):
                        call change_Girl_stat(EmmaX, "obedience", 5)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        $ EmmaX.change_face("perplexed", 2)
                        ch_e "Hmm? I suppose I can't blame you for that."
                    else:
                        call change_Girl_stat(EmmaX, "love", -10)
                        call change_Girl_stat(EmmaX, "love", -10)
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        $ EmmaX.change_face("angry")
                        ch_e "Unexpectedly honest, but still unacceptable."

    elif Options[0] == "fondled":

        if EmmaX.permanent_History["fondle_breasts"]+ EmmaX.permanent_History["fondle_pussy"] + EmmaX.permanent_History["fondle_ass"] >= 10:
            ch_e "I'll need a helping hand later."
        else:
            ch_e "You've displayed some rather significant talents in. . . massage."
            ch_e "We may need to explore that further. . ."

    elif Options[0] == "booked":

        ch_e "I read the. . . books you gave me."
        menu:
            extend ""
            "Yeah? Did you like them?":
                $ EmmaX.change_face("sly", 2)
                ch_e "They were a bit simplistic, but certainly inspirational."
            "Good. You looked like you could use to learn a thing or two from them.":
                call change_Girl_stat(EmmaX, "love", 3)
                call change_Girl_stat(EmmaX, "inhibition", 10)
                $ EmmaX.change_face("sly")
                ch_e "Oh, [EmmaX.player_petname], the things I could teach those authors would leave them in the hospital."
        $ EmmaX.blushing = "_blush1"
        $ EmmaX.had_chat.append("book")

    elif Options[0] == "lingerie":

        $ EmmaX.change_face("sly")
        ch_e "[EmmaX.player_petname], I wanted to thank you again for the. . .{i}clothing{/i} you bought me."
        ch_e "They look wonderful."
        $ EmmaX.had_chat.append("lingerie")

    elif Options[0] == "handy":

        $ EmmaX.change_face("sly", eyes = "side")
        ch_e "You know, I was thinking about my hand, "
        $ EmmaX.change_face("sly")
        ch_e "on your cock. . ."
        ch_e "Oh, that expression is priceless. . ."
        ch_e "I suppose I'll have to repeat that service sometime. . ."

    elif Options[0] == "blowjob":
        if "blowjob" not in EmmaX.had_chat:

            $ EmmaX.change_face("sly", 2)
            ch_e "You know, [EmmaX.player_petname], you have a very unique flavor to you."
            ch_p "Oh?"
            ch_e "Your cock, I mean."
            ch_e "Very. . . satisfying."
            menu:
                extend ""
                "Well, there's always more where that came from.":
                    call change_Girl_stat(EmmaX, "love", 5)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    $ EmmaX.change_face("sly")
                    ch_e "I'll have to take you up on that."
                "I'm glad it measured up to all those other guys.":
                    if approval_check(EmmaX, 300, "I") or not approval_check(EmmaX, 800):
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        call change_Girl_stat(EmmaX, "inhibition", 10)
                        $ EmmaX.change_face("smile", 1)
                        ch_e "Oh, it certainly managed that."
                    else:
                        call change_Girl_stat(EmmaX, "love", -2)
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        $ EmmaX.change_face("sly")
                        ch_e "Are you trying to imply something about my. . . experience?"
            $ EmmaX.blushing = "_blush1"
            $ EmmaX.had_chat.append("blowjob")
        else:
            $ line = renpy.random.choice(["You've a taste that's easy to acquire.",
                            "My jaw is a bit sore lately.",
                            "If you need some. . . attention, let me know.",
                            "Mmmm. . . [she mimes her tongue knocking against her cheek.]"])
            ch_e "[line]"

    elif Options[0] == "swallowed":

        if "swallow" in EmmaX.had_chat:
            ch_e "I think I'd like another taste of your. . . essence."
        else:
            ch_e "You certainly have a unique flavor to your semen, [EmmaX.player_petname]."
            $ EmmaX.change_face("sly", 1)
            ch_e "Very. . . envigorating. . ."
            $ EmmaX.had_chat.append("swallow")

    elif Options[0] == "facial":

        $ EmmaX.change_face("sexy")
        ch_e "You know, perhaps you could try to keep it away from my eyes next time?"

    elif Options[0] == "sleepover":

        ch_e "You're so restless in your sleep, it gives me. . . ideas."

    elif Options[0] == "creampie":

        "[EmmaX.name] draws close to you so she can whisper into your ear."
        ch_e "I can still feel you. . .running down the inside of my thigh."

    elif Options[0] == "sexed":

        $ EmmaX.change_face("sexy", 2)
        ch_e "Since being with you, I have a lot more to think about, after class. . ."

    elif Options[0] == "anal":

        $ EmmaX.change_face("sly", 1)
        ch_e "It's been a while since I've had anyone use the back door."
        $ EmmaX.change_face("sexy")
        ch_e "I'm glad you \"went there.\""

    elif Options[0] == "seenpeen":
        $ EmmaX.change_face("sly", 1)
        ch_e "Perhaps I should have mentioned it earlier, "
        $ EmmaX.change_face("sly", 1, eyes = "down")
        ch_e "That cock you've got is certainly an interesting specimen."
        $ EmmaX.change_face("bemused", 1)
        call change_Girl_stat(EmmaX, "love", 5)
        call change_Girl_stat(EmmaX, "love", 10)
        $ EmmaX.history.remove("seenpeen")
    elif Options[0] == "topless":
        $ EmmaX.change_face("sly", 1)
        ch_e "Out of curiosity, when you saw my breasts earlier. . ."
        ch_e "Was it everything you dreamed?"
        call Emma_First_TMenu
        $ EmmaX.history.remove("topless")
    elif Options[0] == "bottomless":
        $ EmmaX.change_face("sly", 1)
        ch_e "I was wondering, when you saw me bottomless before. . ."
        ch_e "What did you think?"
        call Emma_First_BMenu
        $ EmmaX.history.remove("bottomless")

    elif Options[0] == "boyfriend?":
        call Emma_BF
    elif Options[0] == "lover?":
        call Emma_Love
    elif Options[0] == "sir?":
        call Emma_Sub
    elif Options[0] == "master?":
        call Emma_Master
    elif Options[0] == "sexfriend?":
        call Emma_Sexfriend
    elif Options[0] == "fuckbuddy?":
        call Emma_Fuckbuddy
    elif Options[0] == "daddy?":
        call Emma_Daddy

    elif Options[0] == "public":
        $ EmmaX.change_face("sly")
        ch_e "Hmm, well I suppose the cat's out of the bag now."
        $ EmmaX.change_face("sly", eyes = "side", brows = "angry")
        if "spotted" in EmmaX.daily_history:
            ch_e "With that show we put on earlier, I doubt we can keep rumors from spreading."
        else:
            ch_e "With that show we put on the other day, I doubt we can keep rumors from spreading."
        ch_e ". . ."
        $ EmmaX.change_face("sly")
        call change_Girl_stat(EmmaX, "obedience", 10)
        call change_Girl_stat(EmmaX, "inhibition", 10)
        call change_Girl_stat(EmmaX, "inhibition", 10)
        ch_e "I suppose we'll just have to spread some more. . ."
        $ EmmaX.had_chat.append("public")

    elif Options[0] == "hate":
        $ line = renpy.random.choice(["I'd rather keep this professional.",
                "If you have something to say, put it in writing.",
                "Back off.",
                "Leave me alone."])
        ch_e "[line]"
    else:

        $ D20 = renpy.random.randint(1, 15)
        if D20 == 1:
            $ EmmaX.change_face("smile")
            ch_e "You did lovely job on the quiz the other day."
        elif D20 == 2:
            $ EmmaX.change_face("sad")
            ch_e "I've had a miserable amount of paperwork lately."
            $ EmmaX.change_face("bemused")
            ch_e "Perhaps come by after class to help?"
        elif D20 == 3:
            $ EmmaX.change_face("surprised")
            ch_e "You should have seen what Miss Pryde was wearing earlier!"
        elif D20 == 4:
            $ EmmaX.change_face("sad")
            ch_e "Preparing for next week's test has been exhausting!"
        elif D20 == 5:
            $ EmmaX.change_face("smile")
            ch_e "It really is a lovely day for a walk. . ."
        elif D20 == 6:
            $ EmmaX.change_face("startled")
            ch_e "There have been some serious issues lately with Sentinel attacks."
        elif D20 == 7:
            $ EmmaX.change_face("smile")
            ch_e "I've just had a positive progress report on my work so far."
        elif D20 == 8:
            $ EmmaX.change_face("sad")
            ch_e "This is a lovely school, but I do miss the amenities of the big city."
        elif D20 == 9:
            $ EmmaX.change_face("confused")
            ch_e "Do you pick up that weird humming of Xavier's in your head, or is that just me?"
        elif D20 == 10:
            $ EmmaX.change_face("smile")
            ch_e "I think the class is picking up the recent study sessions."
        elif D20 == 11:
            $ EmmaX.change_face("smile")
            ch_e "I've been looking forward to my next workout session."
        elif D20 == 12:
            $ EmmaX.change_face("sad")
            ch_e "I'm not sure what to do with Rogue's grades, they're starting to slip."
        elif D20 == 13:
            $ EmmaX.change_face("smile")
            ch_e "Not that I'm a lush or anything, but I could really do for a drink."
        elif D20 == 14:
            $ EmmaX.change_face("sad")
            ch_e "There's been another attack on the news, deplorable."
        elif D20 == 15:
            $ EmmaX.change_face("sadside")
            ch_e "I think I must have pulled something during my workout yesterday."
            $ EmmaX.change_face("sly", mouth = "normal")
            ch_e "Perhaps you could work it out for me?"
        else:
            $ EmmaX.change_face("startled")
            ch_e "As students go, you're not intollerable."

    $ line = 0
    return


label Emma_names:
    $ last_name = get_last_name(Player)
    menu:
        ch_e "Oh? What would you like me to call you?"
        "[last_name]'s fine.":
            $ EmmaX.player_petname = Tempname
            ch_e "I assumed it was, [EmmaX.player_petname]."
        "Call me by my name.":
            $ EmmaX.player_petname = Player.name
            ch_e "If you'd rather, [EmmaX.player_petname]."
        "Call me \"dear\"." if "dear" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "dear"
            ch_e "Certainly, [EmmaX.player_petname]."
        "Call me \"darling\"." if "darling" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "darling"
            ch_e "Certainly, [EmmaX.player_petname]."
        "Call me \"boyfriend\"." if "boyfriend" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "boyfriend"
            ch_e "How pedestrian, but fine, [EmmaX.player_petname]."
        "Call me \"lover\"." if "lover" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "lover"
            ch_e "Certainly, [EmmaX.player_petname]."
        "Call me \"sir\"." if "sir" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "sir"
            ch_e "Yes, [EmmaX.player_petname]."
        "Call me \"master\"." if "master" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "master"
            ch_e "As you wish, [EmmaX.player_petname]."
        "Call me \"sex friend\"." if "sex friend" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "sex friend"
            ch_e "You naughty boy. Very well, [EmmaX.player_petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "fuck buddy"
            ch_e "How nasty, \"[EmmaX.player_petname]\"."
        "Call me \"daddy\"." if "daddy" in EmmaX.player_petnames:
            $ EmmaX.player_petname = "daddy"
            ch_e "Mmm, ok, [EmmaX.player_petname]."
        "Nevermind.":
            return
    return


label Emma_Pet:
    while 1:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Ms. Frost.":
                        $ EmmaX.petname = "Ms. Frost"
                        $ EmmaX.name = "Ms. Frost"
                        ch_e "I don't see why not, [EmmaX.player_petname]."
                    "I think I'll just call you Emma.":

                        if approval_check(EmmaX, 700) or "classcaught" in EmmaX.history:
                            ch_e "I don't see why not, [EmmaX.player_petname]."
                            $ EmmaX.petname = "Emma"
                            $ EmmaX.name = "Emma"
                        else:
                            ch_e "I'd rather you didn't, [EmmaX.player_petname]."
                    "I think I'll call you \"girl\".":

                        $ EmmaX.petname = "girl"
                        if "boyfriend" in EmmaX.player_petnames or approval_check(EmmaX, 600, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "How droll, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "I wouldn't, [EmmaX.player_petname]."
                    "I think I'll call you \"boo\".":

                        $ EmmaX.petname = "boo"
                        if "boyfriend" in EmmaX.player_petnames or approval_check(EmmaX, 800, "L"):
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "How adorable, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "I'm no such thing, [EmmaX.player_petname]."
                    "I think I'll call you \"bae\".":

                        $ EmmaX.petname = "bae"
                        if "boyfriend" in EmmaX.player_petnames or approval_check(EmmaX, 800, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "I suppose I am your. . . \"bae?\""
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "What does that even mean?."
                    "I think I'll call you \"baby\".":

                        $ EmmaX.petname = "baby"
                        if "boyfriend" in EmmaX.player_petnames or approval_check(EmmaX, 500, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "How precious."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "I think I'm a bit. . . mature for that."
                    "I think I'll call you \"darling\".":

                        $ EmmaX.petname = "darling"
                        if "boyfriend" in EmmaX.player_petnames or approval_check(EmmaX, 600, "L"):
                            ch_e "I do adore you, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "A bit premature, [EmmaX.player_petname]."
                    "I think I'll call you \"sweetie\".":

                        $ EmmaX.petname = "sweetie"
                        if "boyfriend" in EmmaX.player_petnames or approval_check(EmmaX, 500, "L"):
                            ch_e "Really, [EmmaX.player_petname]?"
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Too saccharine, [EmmaX.player_petname]."
                    "I think I'll call you \"sexy\".":

                        $ EmmaX.petname = "sexy"
                        if "lover" in EmmaX.player_petnames or approval_check(EmmaX, 900):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "I can't argue there, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "That may be a bit much, [EmmaX.player_petname]."
                    "I think I'll call you \"lover\".":

                        $ EmmaX.petname = "lover"
                        if "lover" in EmmaX.player_petnames or approval_check(EmmaX, 900, "L"):
                            $ EmmaX.change_face("sexy", 1)
                            ch_e "I do love you, [EmmaX.player_petname]!"
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Not in this lifetime, [EmmaX.player_petname]."
                    "Back":

                        pass
            "Risky":

                menu:
                    "I think I'll call you \"slave\".":
                        $ EmmaX.petname = "slave"
                        if "master" in EmmaX.player_petnames or approval_check(EmmaX, 900, "O"):
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "As you wish, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "I'm no man's slave, [EmmaX.player_petname]."
                    "I think I'll call you \"pet\".":

                        $ EmmaX.petname = "pet"
                        if "master" in EmmaX.player_petnames or approval_check(EmmaX, 600, "O"):
                            $ EmmaX.change_face("bemused", 1)
                            ch_e "So long as you make sure to pet me, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "I doubt you'd want me for a pet, [EmmaX.player_petname]."
                    "I think I'll call you \"slut\".":

                        $ EmmaX.petname = "slut"
                        if "sex friend" in EmmaX.player_petnames or approval_check(EmmaX, 1000, "OI"):
                            $ EmmaX.change_face("sexy")
                            ch_e "I cant exactly disagree, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            $ EmmaX.mouth = "surprised"
                            ch_e "I would strongly reconsider that."
                    "I think I'll call you \"whore\".":

                        $ EmmaX.petname = "whore"
                        if "fuckbuddy" in EmmaX.player_petnames or approval_check(EmmaX, 1100, "OI"):
                            $ EmmaX.change_face("sly")
                            ch_e "Only for you though. . ."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "The last man to call me that no longer remembers his own name."
                    "I think I'll call you \"sugartits\".":

                        $ EmmaX.petname = "sugartits"
                        if "sex friend" in EmmaX.player_petnames or approval_check(EmmaX, 1400):
                            $ EmmaX.change_face("sly", 1)
                            ch_e "They certainly are sweet. . ."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "I expect you're better than that, [EmmaX.player_petname]."
                    "I think I'll call you \"sex friend\".":

                        $ EmmaX.petname = "sex friend"
                        if "sex friend" in EmmaX.player_petnames or approval_check(EmmaX, 600, "I"):
                            $ EmmaX.change_face("sly")
                            ch_e "Hm?"
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "Hopefully not in public, [EmmaX.player_petname]."
                    "I think I'll call you \"fuckbuddy\".":

                        $ EmmaX.petname = "fuckbuddy"
                        if "fuckbuddy" in EmmaX.player_petnames or approval_check(EmmaX, 700, "I"):
                            $ EmmaX.change_face("bemused")
                            ch_e "Well. . . alright."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            $ EmmaX.mouth = "surprised"
                            ch_e "How crass."
                    "I think I'll call you \"baby girl\".":

                        $ EmmaX.petname = "baby girl"
                        if "daddy" in EmmaX.player_petnames or approval_check(EmmaX, 1200):
                            $ EmmaX.change_face("smile", 1)
                            ch_e "Adorable."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            ch_e "A bit inappropriate."
                    "I think I'll call you \"mommy\".":

                        $ EmmaX.petname = "mommy"
                        if "mommy" in EmmaX.petnames or approval_check(EmmaX, 1500):
                            $ EmmaX.change_face("sly", 1, mouth = "kiss")
                            ch_e "Oooh, [EmmaX.player_petname]."
                        else:
                            $ EmmaX.change_face("angry")
                            ch_e "That's a bit much, [EmmaX.player_petname]"
                    "Back":

                        pass
            "Nevermind.":

                return
    return




label Emma_Rename:

    $ EmmaX.mouth = "smile"
    ch_e "Yes, and?"
    menu:
        extend ""
        "I think \"Emma's\" a pretty name." if EmmaX.name != "Emma" and "Emma" in EmmaX.names:
            $ EmmaX.name = "Emma"
            ch_e "I've always been fond of it. . ."
        "I thought \"Ms. Frost\" sounded cool." if EmmaX.name != "Ms. Frost" and "Ms. Frost" in EmmaX.names:
            $ EmmaX.name = "Ms. Frost"
            if approval_check(EmmaX, 1000, "LI"):
                $ EmmaX.change_face("sly", 1)
                if "namechange" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "obedience", 2)
                    call change_Girl_stat(EmmaX, "inhibition", 3)
                ch_e "Naughty boy. . ."
            else:
                ch_e "I suppose we could keep things professional. . ."
        "I liked the sound of \"White Queen.\"" if EmmaX.name != "White Queen" and "White Queen" in EmmaX.names:
            $ EmmaX.name = "White Queen"
            if not approval_check(EmmaX, 500, "I"):
                $ EmmaX.change_face("confused")
                ch_e "Where have you heard that-"
                $ EmmaX.change_face("sly", 2)
                if "namechange" not in EmmaX.daily_history:
                    call change_Girl_stat(EmmaX, "love", 2)
                    call change_Girl_stat(EmmaX, "obedience", 2)
                    call change_Girl_stat(EmmaX, "inhibition", 3)
                ch_e "Oh, you dirty, dirty boy. . ."
            else:
                $ EmmaX.change_face("confused")
                ch_e "Oh, well, I suppose. . ."
            $ EmmaX.change_face()
        "Nevermind.":
            pass
    $ EmmaX.add_word(1, 0, "namechange")
    return



label Emma_Personality(counter=0):
    if not EmmaX.had_chat[4] or counter:
        "Since you're doing well in one area, you can convince Emma to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_e "Sure, what's up?"
        "More Obedient. [[Love to Obedience]" if EmmaX.love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_e "Anything to humor you, [EmmaX.player_petname]."
            $ EmmaX.had_chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if EmmaX.love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_e "I don't see how I could be {i}less{/i} inhibited, but I can certainly try."
            $ EmmaX.had_chat[4] = 2

        "Less Inhibited. [[Obedience to Inhibition]" if EmmaX.obedience > 900:
            ch_p "I want you to be less inhibited."
            ch_e "If you say so."
            $ EmmaX.had_chat[4] = 3
        "More Loving. [[Obedience to Love]" if EmmaX.obedience > 900:
            ch_p "I'd like you to learn to love me."
            ch_e "I'll try to."
            $ EmmaX.had_chat[4] = 4

        "More Obedient. [[Inhibition to Obedience]" if EmmaX.inhibition > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_e "Does that get you off?"
            $ EmmaX.had_chat[4] = 5

        "More Loving. [[Inhibition to Love]" if EmmaX.inhibition > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_e "We do have fun. . ."
            $ EmmaX.had_chat[4] = 6

        "I guess just do what you like. . .[[reset]" if EmmaX.had_chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_e "As if I ever do anything else?"
            $ EmmaX.had_chat[4] = 0
        "Repeat the rules":
            call Emma_Personality (1)
            return
        "Nevermind.":
            return
    return












    label Emma_NoPantiesOn:
        $ EmmaX.change_face("sexy", eyes = "side")
        ch_e "You should be aware. . ."
        $ EmmaX.change_face("sly")
        menu:
            ch_e "I'm not wearing any panties at the moment. . ."
            "Then you could slip on a pair. . .":
                if (EmmaX.seen_pussy and approval_check(EmmaX, 1100, taboo_modifier=(5-Public))) or approval_check(EmmaX, 1500, taboo_modifier=(5-Public)):
                    $ EmmaX.blushing = "_blush1"
                    ch_e "I didn't say that bothered me. . ."
                    $ EmmaX.blushing = ""
                elif approval_check(EmmaX, 700, taboo_modifier=5):
                    ch_e "I suppose that I could. . ."
                    if "lace_panties" in EmmaX.inventory:
                        $ EmmaX.Clothes["underwear"]  = "lace_panties"
                    else:
                        $ EmmaX.Clothes["underwear"] = "green_panties"
                    if approval_check(EmmaX, 1200, taboo_modifier=4):
                        $ line = EmmaX.Clothes["bottom"]
                        $ EmmaX.Outfit.remove_Clothing(["pants", "skirt"])
                        "She pulls off her [line] and slips on the [EmmaX.Clothes[underwear].name]."
                    elif EmmaX.Clothes["bottom"] == "skirt":
                        "She pulls out her [EmmaX.Clothes[underwear].name] and pulls them up under her skirt."
                        $ EmmaX.Outfit.remove_Clothing(["pants", "skirt"])
                        "Then she drops the skirt to the floor."
                    else:
                        $ line = EmmaX.Clothes["bottom"]
                        $ EmmaX.Outfit.remove_Clothing(["pants", "skirt"])
                        "She steps away a moment and then comes back wearing only the [EmmaX.Clothes[underwear].name]."
                    return
                elif EmmaX.taboo and approval_check(EmmaX, 800, taboo_modifier=0):
                    ch_e "I like how you think, but not in public like this."
                    return False
                else:
                    ch_e "I could, but I'd rather not."
                    return False
            "You could always just wear nothing at all. . .":

                if approval_check(EmmaX, 1100, "LI", taboo_modifier=(5-Public)) and EmmaX.love > EmmaX.inhibition:
                    ch_e "I suppose I could. . ."
                elif approval_check(EmmaX, 700, "OI", taboo_modifier=(5-Public)) and EmmaX.obedience > EmmaX.inhibition:
                    ch_e "If you'd like. . ."
                elif approval_check(EmmaX, 600, "I", taboo_modifier=(5-Public)):
                    ch_e "I certainly could. . ."
                elif approval_check(EmmaX, 1300, taboo_modifier=(5-Public)):
                    ch_e "Very well."
                else:
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.brows = "angry"
                    if EmmaX.taboo > 20:
                        ch_e "I'm afraid not out here, [EmmaX.player_petname]!"
                    else:
                        ch_e "You wish, [EmmaX.player_petname]!"
                    return False
            "Never mind.":

                ch_e "Ok. . ."
                return False
        return True




    menu Emma_Clothes_Under:
        "Tops":
            menu:
                "How about you lose the [EmmaX.Clothes[bra].name]?" if EmmaX.Clothes["bra"]:
                    $ EmmaX.change_face("bemused", 1)
                    if EmmaX.seen_breasts and approval_check(EmmaX, 900, taboo_modifier=(4-Public)):
                        ch_e "Of course."
                    elif approval_check(EmmaX, 1100, taboo_modifier=2):
                        if EmmaX.taboo:
                            ch_e "I'd rather not out here. . ."
                        else:
                            ch_e "I suppose for you. . ."
                    elif EmmaX.Clothes["jacket"] == "jacket" and approval_check(EmmaX, 700, taboo_modifier=(3-Public)):
                        ch_e "This is a bit daring without anything under it. . ."
                    elif not EmmaX.Clothes["top"]:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "I don't think that would be appropriate."
                            return
                    else:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "I'm afraid not, [EmmaX.player_petname]."
                            return
                    $ line = EmmaX.Clothes["bra"]
                    $ EmmaX.take_off("bra")
                    if EmmaX.Clothes["top"]:
                        "She reaches under her [EmmaX.Clothes[top].name] grabs her [line], and pulls it out, dropping it to the ground."
                    else:
                        "She lets her [line] fall to the ground."
                        if not renpy.showing('dress_screen'):
                            call Emma_First_Topless

                "I like that corset you have." if EmmaX.Clothes["bra"] != "corset":
                    if EmmaX.seen_breasts or approval_check(EmmaX, 1000, taboo_modifier=(3-Public)):
                        ch_e "So do I."
                        $ EmmaX.Clothes["bra"] = "corset"
                        $ EmmaX.top_pulled_up = 1
                    else:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "I don't think that would be appropriate. . ."
                        else:
                            $ EmmaX.Clothes["bra"] = "corset"

                "I like that lace bra." if "lace_bra" in EmmaX.inventory and EmmaX.Clothes["bra"] != "lace_bra":
                    if EmmaX.seen_breasts or approval_check(EmmaX, 1300, taboo_modifier=(3-Public)):
                        ch_e "Fine."
                        $ EmmaX.Clothes["bra"] = "lace_bra"
                    else:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "It's a bit revealing. . ."
                        else:
                            $ EmmaX.Clothes["bra"] = "lace_bra"

                "I like that sports bra." if EmmaX.Clothes["bra"] != "sports_bra":
                    if EmmaX.seen_breasts or approval_check(EmmaX, 1000, taboo_modifier=(3-Public)):
                        ch_e "Fine."
                        $ EmmaX.Clothes["bra"] = "sports_bra"
                    else:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "I'm not sure about that. . ."
                        else:
                            $ EmmaX.Clothes["bra"] = "sports_bra"

                "I like that bikini top." if EmmaX.Clothes["bra"] != "bikini_top" and "bikini_top" in EmmaX.inventory:
                    if Player.location == "bg_pool":
                        ch_e "Fine."
                        $ EmmaX.Clothes["bra"] = "bikini_top"
                    else:
                        if EmmaX.seen_breasts or approval_check(EmmaX, 800, taboo_modifier=2):
                            ch_e "Fine."
                            $ EmmaX.Clothes["bra"] = "bikini_top"
                        else:
                            call ask_for_dress_screen (EmmaX)
                            if not _return:
                                ch_e "I don't know about wearing that here. . ."
                            else:
                                $ EmmaX.Clothes["bra"] = "bikini_top"
                "Never mind":
                    pass
            return
        "Hose and stockings options":


            menu:
                "You could lose the hose." if EmmaX.Clothes["hose"]:
                    $ EmmaX.take_off("hose")
                "The thigh-high hose would look good with that." if EmmaX.Clothes["hose"] != "stockings" and "stockings_and_garterbelt" in EmmaX.inventory:
                    $ EmmaX.Clothes["hose"] = "stockings"
                "The pantyhose would look good with that." if EmmaX.Clothes["hose"] != "pantyhose" and "pantyhose" in EmmaX.inventory:
                    $ EmmaX.Clothes["hose"] = "pantyhose"
                "The ripped pantyhose would look good with that." if EmmaX.Clothes["hose"] != "ripped_pantyhose" and "ripped_pantyhose" in EmmaX.inventory:
                    $ EmmaX.Clothes["hose"] = "ripped_pantyhose"
                "The stockings and garterbelt would look good with that." if EmmaX.Clothes["hose"] != "stockings_and_garterbelt" and "stockings_and_garterbelt" in EmmaX.inventory:
                    $ EmmaX.Clothes["hose"] = "stockings_and_garterbelt"
                "Maybe just the garterbelt?" if EmmaX.Clothes["hose"] != "garterbelt" and "stockings_and_garterbelt" in EmmaX.inventory:
                    $ EmmaX.Clothes["hose"] = "garterbelt"
                "Never mind":
                    pass
            return
        "Panties":


            menu:
                "You could lose those panties. . ." if EmmaX.Clothes["underwear"]:
                    $ EmmaX.change_face("bemused", 1)
                    if (approval_check(EmmaX, 900) or EmmaX.seen_pussy) and not EmmaX.taboo:


                        if approval_check(EmmaX, 850, "L"):
                            ch_e "You like the view?"
                        elif approval_check(EmmaX, 500, "O"):
                            ch_e "If you'd like."
                        elif approval_check(EmmaX, 350, "I"):
                            ch_e "I do enjoy going without them. . ."
                        else:
                            ch_e "Very well."
                    else:

                        if approval_check(EmmaX, 1100, "LI", taboo_modifier=(4-Public)) and EmmaX.love > EmmaX.inhibition:
                            ch_e "I don't exactly mind you seeing. . ."
                        elif approval_check(EmmaX, 700, "OI", taboo_modifier=(4-Public)) and EmmaX.obedience > EmmaX.inhibition:
                            ch_e "I suppose I could. . ."
                        elif approval_check(EmmaX, 600, "I", taboo_modifier=(4-Public)):
                            ch_e "Why not."
                        elif approval_check(EmmaX, 1300, taboo_modifier=(4-Public)):
                            ch_e "Fine."
                        else:
                            call ask_for_dress_screen (EmmaX)
                            if not _return:
                                $ EmmaX.change_face("surprised")
                                $ EmmaX.brows = "angry"
                                if EmmaX.taboo > 20:
                                    ch_e "I don't think I could out here, [EmmaX.player_petname]!"
                                else:
                                    ch_e "I could, but I won't, [EmmaX.player_petname]!"
                                return
                    $ line = EmmaX.Clothes["underwear"]
                    $ EmmaX.take_off("underwear")
                    if not EmmaX.Clothes["bottom"]:
                        "She pulls off her [line], then drops them to the ground."
                        if not renpy.showing('dress_screen'):
                            call Emma_First_Bottomless
                    elif approval_check(EmmaX, 1200, taboo_modifier=4):
                        $ temp_bottom = EmmaX.Clothes["bottom"]
                        $ EmmaX.Outfit.remove_Clothing(["pants", "skirt"])
                        pause 0.5
                        $ EmmaX.Clothes["bottom"] = temp_bottom
                        "She pulls off her [EmmaX.Clothes[bottom]] and [line], then pulls the [EmmaX.Clothes[bottom].name] back on."
                        call Emma_First_Bottomless (1)
                    elif EmmaX.Clothes["bottom"] == "skirt":
                        "She reaches under her skirt and pulls her [line] off."
                    else:
                        $ EmmaX.blushing = "_blush1"
                        "She steps away a moment and then comes back."
                        $ EmmaX.blushing = ""
                    $ line = 0

                "Why don't you wear the white panties instead?" if EmmaX.Clothes["underwear"] and EmmaX.Clothes["underwear"] != "white_panties":
                    if approval_check(EmmaX, 1100, taboo_modifier=(4-Public)):
                        ch_e "Ok."
                        $ EmmaX.Clothes["underwear"] = "white_panties"
                    else:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "I really don't see how that's any of your concern."
                        else:
                            $ EmmaX.Clothes["underwear"] = "white_panties"

                "Why don't you wear the sporty panties instead?" if EmmaX.Clothes["underwear"] and EmmaX.Clothes["underwear"] != "sports_panties":
                    if approval_check(EmmaX, 1200, taboo_modifier=(4-Public)):
                        ch_e "Fine."
                        $ EmmaX.Clothes["underwear"] = "sports_panties"
                    else:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "I really don't see how that's any of your concern."
                        else:
                            $ EmmaX.Clothes["underwear"] = "sports_panties"

                "Why don't you wear the lace panties instead?" if "lace_panties" in EmmaX.inventory and EmmaX.Clothes["underwear"] and EmmaX.Clothes["underwear"] != "lace_panties":
                    if approval_check(EmmaX, 1300, taboo_modifier=(4-Public)):
                        ch_e "Fine."
                        $ EmmaX.Clothes["underwear"] = "lace_panties"
                    else:
                        call ask_for_dress_screen (EmmaX)
                        if not _return:
                            ch_e "I really don't see how that's any of your concern."
                        else:
                            $ EmmaX.Clothes["underwear"] = "lace_panties"

                "I like those bikini bottoms." if EmmaX.Clothes["underwear"] != "bikini_bottoms" and "bikini_bottoms" in EmmaX.inventory:
                    if Player.location == "bg_pool":
                        ch_e "Fine."
                        $ EmmaX.Clothes["underwear"] = "bikini_bottoms"
                    else:
                        if approval_check(EmmaX, 800, taboo_modifier=2):
                            ch_e "Fine."
                            $ EmmaX.Clothes["underwear"] = "bikini_bottoms"
                        else:
                            call ask_for_dress_screen (EmmaX)
                            if not _return:
                                ch_e "I don't know about wearing those here. . ."
                            else:
                                $ EmmaX.Clothes["underwear"] = "bikini_bottoms"

                "You know, you could wear some panties with that. . ." if not EmmaX.Clothes["underwear"]:
                    $ EmmaX.change_face("bemused", 1)
                    if EmmaX.Clothes["bottom"] and (EmmaX.love+EmmaX.obedience) <= (2* EmmaX.inhibition):
                        $ EmmaX.mouth = "smile"
                        ch_e "I could, but won't."
                        menu:
                            "Fine by me":
                                return
                            "I insist, put some on.":
                                if (EmmaX.love+EmmaX.obedience) <= EmmaX.inhibition:
                                    $ EmmaX.change_face("angry", eyes = "side")
                                    ch_e "How disappointing that must be for you."
                                    return
                                else:
                                    $ EmmaX.change_face("sadside")
                                    ch_e "If you insist."
                    menu:
                        ch_e "If you insist. . ."
                        "How about the white ones?":
                            ch_e "Fine."
                            $ EmmaX.Clothes["underwear"] = "white_panties"
                        "How about the sporty ones?":
                            ch_e "Fine."
                            $ EmmaX.Clothes["underwear"] = "sports_panties"
                        "How about the lace ones?" if "lace_panties" in EmmaX.inventory:
                            ch_e "Fine."
                            $ EmmaX.Clothes["underwear"]  = "lace_panties"
                "Never mind":
                    pass
            return
        "Never mind":
            pass
    return




    menu Emma_Clothes_Misc:

        "You look good with your hair flowing." if EmmaX.Clothes["hair"] != "wavy":
            if approval_check(EmmaX, 600):
                $ EmmaX.Clothes["hair"] = "wavy"

                ch_e "Like this?"
            else:
                ch_e "Yes, I do."

        "Maybe keep your hair straight." if EmmaX.Clothes["hair"] != "wet":
            if approval_check(EmmaX, 600):
                $ EmmaX.Clothes["hair"] = "wet"
                ch_e "You think?"
            else:
                ch_e "I tend to prefer it a bit more loose."

        "Add hat" if EmmaX.Clothes["face_outer_accessory"] != "hat" and "halloween" in EmmaX.history:
            ch_p "That hat you wore to the party was nice."

            $ EmmaX.Clothes["face_outer_accessory"] = "hat"
        "Remove hat" if EmmaX.Clothes["face_outer_accessory"] == "hat":
            ch_p "You could probably lose the hat."

            $ EmmaX.take_off("face_outer_accessory")

        "Grow Pubes." if not EmmaX.pubes and "pubes" not in EmmaX.to_do:
            ch_p "You know, I like some nice hair down there. Maybe grow it out."
            if "pubes" in EmmaX.to_do:
                $ EmmaX.change_face("bemused", 1)
                ch_e "Rome wasn't built in a day. . ."
            else:
                $ EmmaX.change_face("bemused", 1)
                $ approval = approval_check(EmmaX, 1150, taboo_modifier=0)
                if approval_check(EmmaX, 850, "L", taboo_modifier=0) or (approval and EmmaX.love > 2*EmmaX.obedience):
                    ch_e "If you like that sort of thing. . ."
                elif approval_check(EmmaX, 500, "I", taboo_modifier=0) or (approval and EmmaX.inhibition > EmmaX.obedience):
                    ch_e "I could go a bit more. . . wild."
                elif approval_check(EmmaX, 400, "O", taboo_modifier=0) or approval:
                    ch_e "If you insist. . ."
                else:
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.brows = "angry"
                    ch_e "I don't see how that's your concern, [EmmaX.player_petname]."
                    return
                $ EmmaX.to_do.append("pubes")
                $ EmmaX.pubes_counter = 6

        "Shave pubes" if EmmaX.pubes == "_hairy":
            ch_p "I like it waxed clean down there."
            $ EmmaX.change_face("bemused", 1)
            if "shave" in EmmaX.to_do:
                ch_e "Yes, yes, it's on my schedule."
            else:
                $ approval = approval_check(EmmaX, 1150, taboo_modifier=0)

                if approval_check(EmmaX, 850, "L", taboo_modifier=0) or (approval and EmmaX.love > 2*EmmaX.obedience):
                    ch_e "I know you love it."
                elif approval_check(EmmaX, 500, "I", taboo_modifier=0) or (approval and EmmaX.inhibition > EmmaX.obedience):
                    ch_e "I like it kept tidy."
                elif approval_check(EmmaX, 400, "O", taboo_modifier=0) or approval:
                    ch_e "If you insist."
                else:
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.brows = "angry"
                    ch_e "I don't see how that's your concern, [EmmaX.player_petname]."
                    return
                $ EmmaX.to_do.append("shave")
        "Piercings. [[See what she looks like without them first] (locked)" if not EmmaX.seen_pussy and not EmmaX.seen_breasts:
            pass

        "Add ring piercings" if EmmaX.Clothes["piercings"] != "ring" and (EmmaX.seen_pussy or EmmaX.seen_breasts):
            ch_p "You know, you'd look really nice with some ring body piercings."
            if "ring" in EmmaX.to_do:
                ch_e "Yes, yes, it's on my schedule."
            else:
                $ EmmaX.change_face("bemused", 1)
                $ approval = approval_check(EmmaX, 1350, taboo_modifier=0)
                if approval_check(EmmaX, 900, "L", taboo_modifier=0) or (approval and EmmaX.love > 2* EmmaX.obedience):
                    ch_e "A little handhold, I assume?"
                elif approval_check(EmmaX, 600, "I", taboo_modifier=0) or (approval and EmmaX.inhibition > EmmaX.obedience):
                    ch_e "I do like a nice ring. . ."
                elif approval_check(EmmaX, 500, "O", taboo_modifier=0) or approval:
                    ch_e "I didn't know you were into that sort of thing."
                else:
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.brows = "angry"
                    ch_e "Well, I'm just not ready for that sort of thing, [EmmaX.player_petname]."
                    return
                $ EmmaX.to_do.append("ring")

        "Add barbell piercings." if EmmaX.Clothes["piercings"] != "barbell" and (EmmaX.seen_pussy or EmmaX.seen_breasts):
            ch_p "You know, you'd look really nice with some barbell body piercings."
            if "barbell" in EmmaX.to_do:
                ch_e "Yes, yes, it's on my schedule."
            else:
                $ EmmaX.change_face("bemused", 1)
                $ approval = approval_check(EmmaX, 1350, taboo_modifier=0)
                if approval_check(EmmaX, 900, "L", taboo_modifier=0) or (approval and EmmaX.love > 2*EmmaX.obedience):
                    ch_e "A little handhold, I assume?"
                elif approval_check(EmmaX, 600, "I", taboo_modifier=0) or (approval and EmmaX.inhibition > EmmaX.obedience):
                    ch_e "They might look nice on these. . ."
                elif approval_check(EmmaX, 500, "O", taboo_modifier=0) or approval:
                    ch_e "I didn't know you were into that sort of thing."
                else:
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.brows = "angry"
                    ch_e "Well, I'm just not ready for that sort of thing, [EmmaX.player_petname]."
                    return
                $ EmmaX.to_do.append("barbell")
                $ EmmaX.Clothes["piercings"] = "barbell"

        "Remove piercings" if EmmaX.Clothes["piercings"]:
            ch_p "You know, you'd look better without those piercings."
            $ EmmaX.change_face("bemused", 1)
            $ approval = approval_check(EmmaX, 1350, taboo_modifier=0)
            if approval_check(EmmaX, 950, "L", taboo_modifier=0) or (approval and EmmaX.love > EmmaX.obedience):
                ch_e "If they aren't working for you. . ."
            elif approval_check(EmmaX, 700, "I", taboo_modifier=0) or (approval and EmmaX.inhibition > EmmaX.obedience):
                ch_e "They were being a nuisance."
            elif approval_check(EmmaX, 600, "O", taboo_modifier=0) or approval:
                ch_e "I'll remove them then."
            else:
                $ EmmaX.change_face("surprised")
                $ EmmaX.brows = "angry"
                ch_e "Well {i}I{/i} enjoy them."
                return
            $ EmmaX.take_off("piercings")

        "Add_choker" if EmmaX.Clothes["neck"] != "choker":
            ch_e "Why don't you try on that white choker."
            ch_e "Ok. . ."
            $ EmmaX.Clothes["neck"] = "choker"
        "Remove_choker" if EmmaX.Clothes["neck"]:
            ch_e "WMaybe go without a collar."
            ch_e "Ok. . ."
            $ EmmaX.take_off("neck")

        "Maybe lose the gloves." if EmmaX.Clothes["gloves"]:
            $ EmmaX.take_off("gloves")
            ch_e "Ok."
        "Put your gloves on." if not EmmaX.Clothes["gloves"]:
            $ EmmaX.Clothes["gloves"] = "gloves"
            ch_e "Ok."
        "Never mind":
            pass
    return


return
