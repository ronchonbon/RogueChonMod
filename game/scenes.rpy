label Poly_Start(Newbie=0,Round2=0,Asked=0): #rkeljsv
        # This is called prior to any new girls being added to your dating structure
        # If there are already two girls in there, it kicks up to the Harem version.
        # Newbie will be the new girl
        # Asked is passed if you request it from a chat menu
        $ line = 0

        if Newbie in Player.Harem:
            return

        if not Player.Harem:
                return

        if Asked in all_Girls:
                if Asked in Player.Harem and Player.Harem[0] != Asked:
                        #moves Girl "Asked" to the head of the line.
                        $ Player.Harem.remove(Asked)
                        if Player.Harem:
                                $ Player.Harem.insert(0,Asked)
                        else:
                                $ Player.Harem.append(Asked)

        if "polystart" in Player.daily_history:
                if Round2 and Asked:
                        "You pull [Player.Harem[0].name] aside for a moment."
                        ch_p "Hey, have you changed your mind about [Newbie.name] lately?"
                        if Player.Harem[0] == First_Bottomless:
                                ch_r "Getting a little greedy, aren't you."
                        elif Player.Harem[0] == KittyX:
                                ch_k "Wow, um, chill for a bit."
                        elif Player.Harem[0] == EmmaX:
                                ch_e "Take a breather, [Player.Harem[0].Petname]."
                        elif Player.Harem[0] == LauraX:
                                ch_l "Cool your jets."
                        elif Player.Harem[0] == JeanX:
                                ch_j "Not really, no."
                        elif Player.Harem[0] == StormX:
                                ch_s "I am weighing my options, give me time."
                        elif Player.Harem[0] == JubesX:
                                ch_v "Look. . . I have feelings. . ."
                        call Anyline(Asked,"Ask me some time later.")
                return

        $ Player.daily_history.append("polystart")

        if len(Player.Harem) >= 2:
                call Harem_Start(Newbie,Round2)
                return


        $ Party = [Player.Harem[0]]
        call shift_focus(Player.Harem[0])
        call set_the_scene
        call clear_the_room(Player.Harem[0])


        if Round2:
                "You pull [Party[0].name] aside for a moment."
                ch_p "Hey, have you changed your mind about [Newbie.name] lately?"
        else:
                $ Party[0].change_face("bemused")
                "[Party[0].name] pulls you aside and wants to talk about something."

                #line 1
                if Party[0] == First_Bottomless:
                        ch_r "I've seen you were getting pretty cozy with [Newbie.name]."
                elif Party[0] == KittyX:
                        ch_k "You look kinda close with [Newbie.name] lately."
                elif Party[0] == EmmaX:
                        ch_e "I've noticed that [Newbie.name] and yourself have been spending time together."
                elif Party[0] == LauraX:
                        ch_l "You've been all over [Newbie.name] lately."
                elif Party[0] == JeanX:
                        ch_j "I saw you with [Newbie.name] earlier."
                elif Party[0] == StormX:
                        ch_s "I saw you spending time with [Newbie.name] earlier."
                elif Party[0] == JubesX:
                        ch_v "I saw you hanging with [Newbie.name] earlier."
                #end line 1


        if Party[0].GirlLikecheck(Newbie) >= 800:
                $ Party[0].change_face("sly")
        elif Party[0].GirlLikecheck(Newbie) >= 600:
                pass
        else:
                # neither likes her much
                $ Party[0].change_face("angry",Mouth="normal")

        # We like her or not
        if Party[0] == RogueX:
                if Party[0].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "She is pretty sexy, I guess."
                elif Party[0].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "I like her just fine, I was just wondering where it was headed."
                else:
                        # neither likes her much
                        ch_r "I'm not really a fan'a hers."
        elif Party[0] == KittyX:
                if Party[0].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, I get that. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but I'm not sure. . ."
                else:
                        # neither likes her much
                        ch_k "I don't really like her much."
        elif Party[0] == EmmaX:
                if Party[0].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think she's quite the catch."
                elif Party[0].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "I do like her, but have some concerns."
                else:
                        # neither likes her much
                        ch_e "I don't really approve."
        elif Party[0] == LauraX:
                if Party[0].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, I get it."
                elif Party[0].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                else:
                        # neither likes her much
                        ch_l "I don't like her."
        elif Party[0] == JeanX:
                if Party[0].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_j "I get it, she's hot enough."
                elif Party[0].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_j "She's. . . fine."
                else:
                        # neither likes her much
                        ch_j "You probably shouldn't be seen around her."
        elif Party[0] == StormX:
                if Party[0].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_s "She is very beautiful, certainly."
                elif Party[0].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_s "She is a good girl, certainly. . ."
                else:
                        # neither likes her much
                        ch_s "I do not think I like her much."
        elif Party[0] == JubesX:
                if Party[0].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_v "Ok, she's totally hot, but. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_v "She's. . . fine, but. . ."
                else:
                        # neither likes her much
                        ch_v "I'm not there for it."
        #end line 2


        #line 3
        if Party[0] == RogueX:
                ch_r "I don't know how I feel about sharing you with some other girl."
                ch_r "So did you plan to get serious with her?"
        elif Party[0] == KittyX:
                ch_k "I don't know about sharing my boyfriend with somebody else."
                ch_k "So are you[KittyX.like]trying to date her?"
        elif Party[0] == EmmaX:
                ch_e "I can be a bit. . . possessive with my partners."
                ch_e "Is this getting serious with her?"
        elif Party[0] == LauraX:
                ch_l "I don't play well with others."
                ch_l "Are you two getting serious?"
        elif Party[0] == JeanX:
                ch_j "I'm not really interested in sharing with her."
                ch_j "So are you two getting serious?"
        elif Party[0] == StormX:
                ch_s "I am unsure how I feel about this."
                ch_s "What are your intentions with her?"
        elif Party[0] == JubesX:
                ch_v "I don't know. . ."
                ch_v "Are you really into her?"
        #end line 3

        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ line = "y"
            "Maybe, what do you think?":
                $ line = "m"
            "No, not really.":
                $ line = "n"

        if line == "y":
            if Party[0].GirlLikecheck(Newbie) >= 800:
                    # if they like her a lot
                    $ line = "yy"
                    $ Party[0].change_stat("love", 90, 5)
                    $ Party[0].change_stat("obedience", 50, 5)
                    $ Party[0].change_stat("inhibition", 90, 10)
            elif Approvalcheck(Party[0], 1800):
                    # if they really like you enough to put up with it
                    $ line = "ym"
                    $ Party[0].change_stat("obedience", 50, 5)
            elif Approvalcheck(Party[0], 1500) and Party[0].GirlLikecheck(Newbie) >= 500:
                    # if they like her well enough
                    $ line = "ym"
            else:
                    # neither likes her much
                    $ line = "yn"
                    $ Party[0].change_stat("love", 90, -10)
        #end line = y
        if line == "m":
            if Party[0].GirlLikecheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ line = "my"
                    $ Party[0].change_stat("inhibition", 90, 5)
            elif Approvalcheck(Party[0], 1800):
                    # if they both really like you enough to put up with it
                    $ line = "mm"
            elif Approvalcheck(Party[0], 1500) and Party[0].GirlLikecheck(Newbie) >= 600:
                    # if they both like her well enough
                    $ line = "mm"
            else:
                    # neither likes her much
                    $ line = "mn"
        #end line = m
        if line == "n":
            if Party[0].GirlLikecheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ line = "ny"
                    $ Party[0].change_stat("inhibition", 90, 10)
            elif Approvalcheck(Party[0], 1700):
                    # if they both really like you enough to put up with it
                    $ line = "nm"
                    $ Party[0].change_stat("inhibition", 90, 5)
            elif Approvalcheck(Party[0], 1300) and Party[0].GirlLikecheck(Newbie) >= 500:
                    # if they both like her well enough
                    $ line = "nm"
                    $ Party[0].change_stat("love", 90, 5)
            else:
                    # if they don't like her well enough
                    $ line = "nn"
                    $ Party[0].change_stat("love", 90, 10)
        #end line = n


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if line == "yn" or line == "mn" or line == "nn":
                $ Party[0].change_face("angry")
        elif line == "yy" or line == "ny" or line == "my":
                $ Party[0].change_face("sexy")
        else:
                $ Party[0].change_face("bemused")

        #line 5
        if Party[0] == RogueX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess I can live with that."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_r "Hmm, not that I would have minded."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think I'm really cool with that."
                elif line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."

        elif Party[0] == KittyX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with me!"
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, I can[KittyX.like]live with that."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_k "Ok, I would have been ok with it though."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with me."
                elif line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."

        elif Party[0] == EmmaX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "lovely. . ."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose I can make do then."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_e "You could do a lot worse."

                elif line == "yn" or line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."

        elif Party[0] == LauraX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, I can work with that."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_l "Ok. I'm cool with it if you do though."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif line == "nn":
                        # if you said no and agree
                        ch_l "Good."

        elif Party[0] == JeanX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_j "Well, ok, sure."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_j "Well. . . she could be fun. . ."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_j "Really? I mean, she could be fun."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_j "Well, ok, fine. . ."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_j "Ok. I could think about it though."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_j "Well, cut it out."
                elif line == "nn":
                        # if you said no and agree
                        ch_j "Yeah."

        elif Party[0] == StormX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_s "Oh, that will be nice. . ."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_s "Oh, you definitely should!"
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_s "That is too bad. You would go well together."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_s "Well, that should be fine."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_s "You might want to reconsider. . ."

                elif line == "yn" or line == "mn":
                        # neither likes her much
                        ch_s "I do not think I could deal with her."
                elif line == "nn":
                        # if you said no and agree
                        ch_s "Yes, I would agree with that."

        elif Party[0] == JubesX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_v "Ok, cool."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_v "Yeah, sure, I'm down with it."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_v "Ok, but you might be missing out!"

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_v "Ok, yeah, I can deal."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_v "Ok, your call, I guess."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_v "Well. . . I might have some feelings."
                elif line == "nn":
                        # if you said no and agree
                        ch_v "Glad we're on the same page here."

        #end line 5

        if line != "yy" and line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if line in ("my","ny","ym","mm","nm"):
                    #They were generally favorable, so you agreed
                    $ line = "yy"
                    $ Party[0].change_face("smile")
                    $ Party[0].change_stat("love", 90, 10)
                    $ Party[0].change_stat("obedience", 50, 10)
                    if Party[0] == RogueX:
                                    ch_r "Great, sounds fun."
                    elif Party[0] == KittyX:
                                    ch_k "Cool, sounds fun."
                    elif Party[0] == EmmaX:
                                    ch_e "lovely. . ."
                    elif Party[0] == LauraX:
                                    ch_l "Nice."
                    elif Party[0] == JeanX:
                                    ch_j "Ok then."
                    elif Party[0] == StormX:
                                    ch_s "That sounds fantastic."
                    elif Party[0] == JubesX:
                                    ch_v "Sweet!"

                "Well then, I guess I'll stop." if line in ("mn","yn","ym","mm","nm"):
                    #They were unfavorable, so you gave up on it.
                    $ line = "nn"
                    $ Party[0].change_face("smile")
                    $ Party[0].change_stat("love", 90, 10)
                    if Party[0] == RogueX:
                                    ch_r "Good to hear."
                    elif Party[0] == KittyX:
                                    ch_k "Good, that wouldn't have been cool."
                    elif Party[0] == EmmaX:
                                    ch_e "Probably for the best."
                    elif Party[0] == LauraX:
                                    ch_l "Good."
                    elif Party[0] == JeanX:
                                    ch_j "Ok then."
                    elif Party[0] == StormX:
                                    ch_s "That would be a good idea."
                    elif Party[0] == JubesX:
                                    ch_v "Ok, good."

                "I'm asking her in anyway." if line in ("mn","yn"):
                    #if they were unfavorable, but you insist
                    pass

                "Well, I'm going to pass anyway." if line in ("nm","ny","mm"):
                    #if they give you permission, but you aren't into it.
                    $ line = "nn"
                    $ Party[0].change_face("sad")
                    $ Party[0].change_stat("obedience", 70, 5)
                    if Party[0] == RogueX:
                                    ch_r "Oh, ok."
                    elif Party[0] == KittyX:
                                    ch_k "That's fine."
                    elif Party[0] == EmmaX:
                                    ch_e "If you insist."
                    elif Party[0] == LauraX:
                                    ch_l "Ok."
                    elif Party[0] == JeanX:
                                    ch_j "Fine. . ."
                    elif Party[0] == StormX:
                                    ch_s "That is fair."
                    elif Party[0] == JubesX:
                                    ch_v "Yeah, that's fine."

        #end player response to their feedback

        if line == "mn" or line == "yn":
                # if you said yes/maybe and they said no, but you insisted anyway

                if Approvalcheck(Party[0], 1600) and Party[0].GirlLikecheck(Newbie) >= 500:
                            $ Party[0].change_face("sadside")
                            $ Party[0].change_stat("love", 90, -5)
                            $ Party[0].change_stat("obedience", 50, 15)
                            if Party[0] == RogueX:
                                    ch_r "Fine, she's in."
                            elif Party[0] == KittyX:
                                    ch_k "Geeze, ok."
                            elif Party[0] == EmmaX:
                                    ch_e "I suppose we'll make room."
                            elif Party[0] == LauraX:
                                    ch_l "Whatever."
                            elif Party[0] == JeanX:
                                    ch_j "Well. . . ok, fine."
                                    ch_j "But this counts as your Girlistmas present."
                            elif Party[0] == StormX:
                                    ch_s ". . ."
                                    ch_s "I can accept that."
                            elif Party[0] == JubesX:
                                    ch_v "Whatever. Fine."
                            $ line = "yy"
                else:
                            $ Party[0].change_face("angry",Eyes="side")
                            $ Party[0].change_stat("love", 90, -25)
                            $ Party[0].change_stat("inhibition", 90, 10)
                            if Party[0] == RogueX:
                                    ch_r "I just don't like you that much, [RogueX.Petname]."
                                    ch_r "I'm out."
                            elif Party[0] == KittyX:
                                    ch_k "You aren't that cute, [KittyX.Petname]."
                                    ch_k "I'm done."
                            elif Party[0] == EmmaX:
                                    ch_e "Don't overestimate yourself, [EmmaX.Petname]."
                                    ch_e "We're done."
                            elif Party[0] == LauraX:
                                    ch_l "Too far, [LauraX.Petname]."
                                    ch_l "I'm out of here."
                            elif Party[0] == JeanX:
                                    ch_j "I'm more than enough for you."
                                    ch_j "I'm out."
                            elif Party[0] == StormX:
                                    ch_s ". . ."
                                    ch_s "I can't be a part of it then."
                            elif Party[0] == JubesX:
                                    ch_v "Well, I'm out then."
                            $ Party[0].Traits.append("ex")
                            $ Party[0].Break[0] = 5 + Party[0].Break[1] + Party[0].Cheated
                            $ Player.Harem.remove(Party[0])
                            call remove_girl(Party[0])
        #end "she said no but you insisted"

        $ Party = []
        if line == "yy":
                if Newbie.Tag + "No" in Player.Traits:
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                "You should give [Newbie.name] a call."
        else:
                $ Player.Traits.append(Newbie.Tag + "No")
        return

label Harem_Start(Newbie=0,Round2=0): #rkeljsv
        # This is called prior to any new girls being added to your dating structure
        # If there are aren't two girls in there, it kicks back.
        # Newbie will be the new girl

        $ line = 0

        if len(Player.Harem) < 2:
                #if there aren't enough girls yet, forget about it.
                return

        $ Party = [Player.Harem[0],Player.Harem[1]]
        # Adds first two harem members to party, removed everyone else from the room.
        call Present_check
        $ Party = [Player.Harem[0],Player.Harem[1]]
        call shift_focus(Player.Harem[0])
        call set_the_scene

        $ Party[0].change_face("bemused")
        $ Party[1].change_face("bemused")
        if Round2:
                "You call [Party[0].name] and [Party[1].name] over."
                ch_p "I was wondering if you'd changed your mind about [Newbie.name]."
        else:
                "[Party[0].name] pulls you aside and wants to talk about something."
                #line 1

                if Party[0] == RogueX:
                        ch_r "Hey, so me and [Party[1].name] have been talk'in."
                elif Party[0] == KittyX:
                        ch_k "So[KittyX.like]me and [Party[1].name] had a little chat."
                elif Party[0] == EmmaX:
                        ch_e "[Party[1].name] and I have been discussing a few things."
                elif Party[0] == LauraX:
                        ch_l "I had a little chat with [Party[1].name]. . ."
                elif Party[0] == JeanX:
                        ch_j "Hey, I was talking to. . . this one here. . ."
                elif Party[0] == StormX:
                        ch_s "[Party[1].name] and I were having lunch earlier, and something came up."
                elif Party[0] == JubesX:
                        ch_v "So [Party[1].name] and I were talking earlier, and something came up. . ."
                #end line 1

                #line 2
                if Party[1] == RogueX:
                        ch_r "We hear that you were getting pretty cozy with [Newbie.name]."
                elif Party[1] == KittyX:
                        ch_k "We hear that you're kinda close with [Newbie.name] lately."
                elif Party[1] == EmmaX:
                        ch_e "We've hear that [Newbie.name] and yourself have been spending time together."
                elif Party[1] == LauraX:
                        ch_l "You've been all over [Newbie.name] lately."
                elif Party[1] == JeanX:
                        ch_j "We noticed you were around [Newbie.name] a lot lately."
                elif Party[1] == StormX:
                        ch_s "We have both noticed you spending time with [Newbie.name] lately."
                elif Party[0] == JubesX:
                        ch_v "We totally saw you hanging with [Newbie.name] earlier."
                #end line 2

        # We like her or not line 3

        if Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                pass
        elif Party[0].GirlLikecheck(Newbie) >= 700:
                # only first girl likes her
                $ Party[1].change_face("angry",Mouth="normal")
        elif Party[1].GirlLikecheck(Newbie) >= 700:
                # only second girl likes her
                $ Party[0].change_face("angry",Mouth="normal")
        else:
                # neither likes her much
                $ Party[0].change_face("angry",Mouth="normal")
                $ Party[1].change_face("angry",Mouth="normal")

        if Party[0] == RogueX:
                if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "Now we like her just fine, and we can't say we don't like the idea much."
                elif Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "Now we like her just fine, but we don't know about share'in."
                elif Party[0].GirlLikecheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_r "Now I like her just fine, but [Party[1].name] ain't so sure."
                elif Party[1].GirlLikecheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_r "Now [Party[1].name] seems to like her, but I'm not so sure."
                else:
                        # neither likes her much
                        ch_r "Neither'a us is really cool with that."
        elif Party[0] == KittyX:
                if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, we get that. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but we're not sure. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_k "I like her, but I don't know about [Party[1].name]."
                elif Party[1].GirlLikecheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_k "[Party[1].name] likes her, but I don't know."
                else:
                        # neither likes her much
                        ch_k "We don't really like her much."
        elif Party[0] == EmmaX:
                if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think we agree that she's a nice catch."
                elif Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "We do like her, but we have some concerns."
                elif Party[0].GirlLikecheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_e "[Party[1].name] doesn't really approve."
                elif Party[1].GirlLikecheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_e "[Party[1].name] seems to think she's acceptable."
                else:
                        # neither likes her much
                        ch_e "We don't really approve."
        elif Party[0] == LauraX:
                if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, we get it."
                elif Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                elif Party[0].GirlLikecheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_l "She's fine, but [Party[1].name] doesn't like her."
                elif Party[1].GirlLikecheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_l "[Party[1].name] likes her. I don't."
                else:
                        # neither likes her much
                        ch_l "We don't like her."
        elif Party[0] == JeanX:
                if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_j "I get it, she's hot enough."
                elif Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_j "She's. . . fine."
                elif Party[0].GirlLikecheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_j "I think she's fine, but [Party[1].name] doesn't like her."
                        ch_j "For whatever that's worth. . ."
                elif Party[1].GirlLikecheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_j "[Party[1].name] likes her. I don't."
                        ch_j "So I think you know the right answer to this one. . ."
                else:
                        # neither likes her much
                        ch_j "You probably shouldn't be seen around her."
        elif Party[0] == StormX:
                if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_s "We agree that she is very beautiful. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_s "She is a good girl, but we do have some concerns. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_s "I like her, but [Party[1].name] does not approve."
                elif Party[1].GirlLikecheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_s "[Party[1].name] appears to like her, I am unsure."
                else:
                        # neither likes her much
                        ch_s "We do not like her very much."

        elif Party[0] == JubesX:
                if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_v "Ok, she's totally hot, but. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 600 and Party[1].GirlLikecheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_v "She's. . . fine, but. . ."
                elif Party[0].GirlLikecheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_v "She's. . . fine, but, [Party[1].name]. . ."
                elif Party[1].GirlLikecheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_v "[Party[1].name] likes her, but I don't know."
                else:
                        # neither likes her much
                        ch_v "We're not there for it."

        #end line 3

        #line 4
        if Party[1] == RogueX:
                ch_r "So did you plan to get serious with her?"
        elif Party[1] == KittyX:
                ch_k "So are you[KittyX.like]trying to date her?"
        elif Party[1] == EmmaX:
                ch_e "Is this getting serious with her?"
        elif Party[1] == LauraX:
                ch_l "Are you two getting serious?"
        elif Party[1] == JeanX:
                ch_j "So are you two getting serious?"
        elif Party[1] == StormX:
                ch_s "So where would this relationship be leading?"
        elif Party[1] == JubesX:
                ch_v "I don't know. . ."
                ch_v "Are you really into her?"
        #end line 4

        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ line = "y"
            "Maybe, what do you think?":
                $ line = "m"
            "No, not really.":
                $ line = "n"

        if line == "y":
            if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ line = "yy"
                    $ Party[0].change_stat("love", 90, 5)
                    $ Party[0].change_stat("obedience", 50, 5)
                    $ Party[0].change_stat("inhibition", 90, 10)
                    $ Party[1].change_stat("love", 90, 5)
                    $ Party[1].change_stat("obedience", 50, 5)
                    $ Party[1].change_stat("inhibition", 90, 10)
            elif Approvalcheck(Party[0], 1800) and Approvalcheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ line = "ym"
                    $ Party[0].change_stat("obedience", 50, 10)
                    $ Party[1].change_stat("obedience", 50, 10)
            elif Approvalcheck(Party[0], 1500) and Approvalcheck(Party[1], 1500):
                    if Party[0].GirlLikecheck(Newbie) >= 500 and Party[1].GirlLikecheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ line = "ym"
                            $ Party[0].change_stat("obedience", 80, 15)
                            $ Party[1].change_stat("obedience", 80, 15)
                    else:
                            # if they don't like her well enough
                            $ line = "yn"
                            $ Party[0].change_stat("love", 90, -5)
                            $ Party[0].change_stat("obedience", 50, -5)
                            $ Party[1].change_stat("love", 90, -5)
                            $ Party[1].change_stat("obedience", 50, -5)
            else:
                            # neither likes her much
                            $ line = "yn"
                            $ Party[0].change_stat("love", 90, -10)
                            $ Party[0].change_stat("obedience", 50, -5)
                            $ Party[1].change_stat("love", 90, -10)
                            $ Party[1].change_stat("obedience", 50, -5)
        #end line = y
        if line == "m":
            if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ line = "my"
                    $ Party[0].change_stat("inhibition", 90, 5)
                    $ Party[1].change_stat("inhibition", 90, 5)
            elif Approvalcheck(Party[0], 1800) and Approvalcheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ line = "mm"
            elif Approvalcheck(Party[0], 1500) and Approvalcheck(Party[1], 1500):
                    if Party[0].GirlLikecheck(Newbie) >= 600 or Party[1].GirlLikecheck(Newbie) >= 600:
                            # if they both like her well enough
                            $ line = "mm"
                    else:
                            # if they don't like her well enough
                            $ line = "mn"
            else:
                            # neither likes her much
                            $ line = "mn"
        #end line = m
        if line == "n":
            if Party[0].GirlLikecheck(Newbie) >= 800 and Party[1].GirlLikecheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ line = "ny"
                    $ Party[0].change_stat("inhibition", 90, 10)
                    $ Party[1].change_stat("inhibition", 90, 10)
            elif Approvalcheck(Party[0], 1700) and Approvalcheck(Party[1], 1700):
                    # if they both really like you enough to put up with it
                    $ line = "nm"
                    $ Party[0].change_stat("inhibition", 90, 5)
            elif Approvalcheck(Party[0], 1300) and Approvalcheck(Party[1], 1300):
                    if Party[0].GirlLikecheck(Newbie) >= 500 and Party[1].GirlLikecheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ line = "nm"
                    else:
                            # if they don't like her well enough
                            $ line = "nn"
                            $ Party[0].change_stat("love", 90, 5)
                            $ Party[0].change_stat("inhibition", 90, 5)
                            $ Party[1].change_stat("love", 90, 5)
                            $ Party[1].change_stat("inhibition", 90, 5)
            else:
                            # neither likes her much
                            $ line = "nn"
                            $ Party[0].change_stat("love", 90, 5)
                            $ Party[0].change_stat("inhibition", 90, 5)
                            $ Party[1].change_stat("love", 90, 5)
                            $ Party[1].change_stat("inhibition", 90, 5)
        #end line = n


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if line == "yn" or line == "mn" or line == "nn":
                $ Party[0].change_face("angry")
                $ Party[1].change_face("angry")
        elif line == "yy" or line == "ny" or line == "my":
                $ Party[0].change_face("sexy")
                $ Party[1].change_face("sexy")
        else:
                $ Party[0].change_face("bemused")
                $ Party[1].change_face("bemused")

        #line 5
        if Party[0] == RogueX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess we can live with that."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_r "Hmm, not that we would have minded."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think we're really cool with that."
                elif line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."

        elif Party[0] == KittyX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with us!"
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, we can[KittyX.like]live with that."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_k "Ok, we would have been ok with it though."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with us."
                elif line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."

        elif Party[0] == EmmaX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "lovely. . ."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose we can make do then."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_e "You could do a lot worse."

                elif line == "yn" or line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."

        elif Party[0] == LauraX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, we can work with that."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_l "Ok. We're cool with it if you do though."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif line == "nn":
                        # if you said no and agree
                        ch_l "Good."

        elif Party[0] == JeanX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_j "Well, ok, sure."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_j "Well. . . she could be fun. . ."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_j "Really? I mean, she could be fun."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_j "Well, ok, fine. . ."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_j "Ok. I could think about it though."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_j "Well, cut it out."
                elif line == "nn":
                        # if you said no and agree
                        ch_j "Yeah."

        elif Party[0] == StormX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_s "Oh, that will be nice. . ."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_s "Oh, you definitely should!"
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_s "That is too bad. You would go well together."

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_s "Well, that should be fine."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_s "You might want to reconsider. . ."

                elif line == "yn" or line == "mn":
                        # neither likes her much
                        ch_s "I do not think we could deal with her."
                elif line == "nn":
                        # if you said no and agree
                        ch_s "Yes, we could agree with that."

        elif Party[0] == JubesX:
                if line == "yy":
                        # if you said you did and they both like her a lot
                        ch_v "Ok, cool."
                elif line == "my":
                        # if you said maybe and they both like her a lot
                        ch_v "Yeah, sure, I guess we're down with that down with it."
                elif line == "ny":
                        # if you said no but they both like her a lot
                        ch_v "Ok, but you might be missing out!"

                elif line == "ym" or line == "mm":
                        # if they both really like you enough to put up with it
                        ch_v "Ok, yeah, we can deal."
                elif line == "nm":
                        # if you said no but they both like her well enough
                        ch_v "Ok, your call, I guess."

                elif line == "yn" or line == "mn":
                        # if you said you did they don't like her well enough
                        ch_v "Well. . . we might have some feelings."
                elif line == "nn":
                        # if you said no and agree
                        ch_v "Glad we're on the same page here."

        #end line 5

        if line != "yy" and line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if line in ("my","ny","ym","mm","nm"):
                        #They were generally favorable, so you agreed
                        $ line = "yy"
                        $ Party[0].change_face("smile")
                        $ Party[1].change_face("smile")
                        $ Party[0].change_stat("obedience", 80, 5)
                        $ Party[0].change_stat("inhibition", 90, 10)
                        $ Party[1].change_stat("obedience", 80, 5)
                        $ Party[1].change_stat("inhibition", 90, 10)
                        if Party[0] == RogueX:
                                ch_r "Great, sounds fun."
                        elif Party[0] == KittyX:
                                ch_k "Cool, sounds fun."
                        elif Party[0] == EmmaX:
                                ch_e "lovely. . ."
                        elif Party[0] == LauraX:
                                ch_l "Nice."
                        elif Party[0] == JeanX:
                                ch_j "Good."
                        elif Party[0] == StormX:
                                ch_s "Good."
                        elif Party[0] == JubesX:
                                ch_v "Sweet!"
                "Well then, I guess I'll stop." if line in ("mn","yn"):
                        #They were unfavorable, so you gave up on it.
                        $ line = "nn"
                        $ Party[0].change_face("normal")
                        $ Party[1].change_face("normal")
                        $ Party[0].change_stat("love", 90, 5)
                        $ Party[0].change_stat("inhibition", 90, 5)
                        $ Party[1].change_stat("love", 90, 5)
                        $ Party[1].change_stat("inhibition", 90, 5)
                        if Party[0] == RogueX:
                                ch_r "Good to hear."
                        elif Party[0] == KittyX:
                                ch_k "Good, that wouldn't have been cool."
                        elif Party[0] == EmmaX:
                                ch_e "Probably for the best."
                        elif Party[0] == LauraX:
                                ch_l "Good."
                        elif Party[0] == JeanX:
                                ch_j "Good."
                        elif Party[0] == StormX:
                                ch_s "Good."
                        elif Party[0] == JubesX:
                                ch_v "Ok, good."
                "I'm asking her in anyway." if line in ("mn","yn"):
                        #if they were unfavorable, but you insist
                        pass

                "Well, I'm going to pass anyway." if line in ("ym","my","nm","ny","mm"):
                        #if they give you permission, but you aren't into it.
                        $ line = "nn"
                        $ Party[0].change_face("sad")
                        $ Party[1].change_face("sad")
                        $ Party[0].change_stat("obedience", 50, 5)
                        $ Party[1].change_stat("obedience", 50, 5)
                        if Party[0] == RogueX:
                                ch_r "Oh, ok."
                        elif Party[0] == KittyX:
                                ch_k "That's fine."
                        elif Party[0] == EmmaX:
                                ch_e "If you insist."
                        elif Party[0] == LauraX:
                                ch_l "Ok."
                        elif Party[0] == JeanX:
                                ch_j "Ok, I guess. . ."
                        elif Party[0] == StormX:
                                ch_s "That is unfortunate. . ."
                        elif Party[0] == JubesX:
                                ch_v "Yeah, that's fine."
            #end player response to their feedback

            if line == "yy" or line == "nn":
                                pass
            elif len(Player.Harem) >= 3:
                                $ Party[0].change_face("smile",Eyes="side")
                                $ Party[1].change_face("smile",Eyes="side")
                                $ Party[0].change_stat("obedience", 90, 5)
                                $ Party[0].change_stat("inhibition", 90, 5)
                                if Party[0] == RogueX:
                                        ch_r "Oh, what's one more."
                                elif Party[0] == KittyX:
                                        ch_k "We're building a real \"pride\" here."
                                elif Party[0] == EmmaX:
                                        ch_e "I suppose one more can't hurt."
                                elif Party[0] == LauraX:
                                        ch_l "Whatever."
                                elif Party[0] == JeanX:
                                        ch_j "Oh, fine. . ."
                                        ch_j "But you're not hogging her to yourself."
                                elif Party[0] == StormX:
                                        ch_s "What harm would one more bring?"
                                elif Party[0] == JubesX:
                                        ch_v "Ok, I'll make some room."
                                $ line = "yy"
            elif line == "mn" or line == "yn":
                    # if you said yes/maybe and they said no, but you insisted anyway
                    $Count = 0
                    while Count < 2:
                        if Approvalcheck(Party[Count], 1600) and Party[Count].GirlLikecheck(Newbie) >= 500:
                                # She likes you enough to roll over
                                $ Party[Count].change_face("sadside")
                                $ Party[Count].change_stat("love", 90, -5)
                                $ Party[Count].change_stat("obedience", 90, 10)
                                if Party[Count] == RogueX:
                                        ch_r "Fine, she's in."
                                elif Party[Count] == KittyX:
                                        ch_k "Geeze, ok."
                                elif Party[Count] == EmmaX:
                                        ch_e "I suppose we'll make room."
                                elif Party[Count] == LauraX:
                                        ch_l "Whatever."
                                elif Party[Count] == JeanX:
                                        ch_j "Oh, fine. . ."
                                        ch_j "But you're not hogging her to yourself."
                                elif Party[Count] == StormX:
                                        ch_s "If you insist, I will find room for her. . ."
                                elif Party[0] == JubesX:
                                        ch_v "I guess we can share."
                                $ line = "yy"
                        else:
                                # She doewsn't like you enough to roll over
                                $ Party[Count].change_face("angry",Eyes="side")
                                $ Party[Count].change_stat("love", 90, -25)
                                $ Party[Count].change_stat("inhibition", 90, 10)
                                if Party[Count] == RogueX:
                                        ch_r "I just don't like you that much, [RogueX.Petname]."
                                        ch_r "I'm out."
                                elif Party[Count] == KittyX:
                                        ch_k "You aren't that cute, [KittyX.Petname]."
                                        ch_k "I'm done."
                                elif Party[Count] == EmmaX:
                                        ch_e "Don't overestimate yourself, [EmmaX.Petname]."
                                        ch_e "We're done."
                                elif Party[Count] == LauraX:
                                        ch_l "Too far, [LauraX.Petname]."
                                        ch_l "I'm out of here."
                                elif Party[Count] == JeanX:
                                        ch_j "No way, too much. . ."
                                        ch_j "I'm out of here."
                                elif Party[Count] == StormX:
                                        ch_s "Then I suppose I cannot be a part of this."
                                elif Party[0] == JubesX:
                                        ch_v "Well, I'm out then."
                                $ Party[Count].Traits.append("ex")
                                $ Party[Count].Break[0] = 5 + Party[Count].Break[1] + Party[Count].Cheated

                                $ Player.Harem.remove(Party[Count])
                                call remove_girl(Party[Count])
                        $ Count += 1
            #end "she said no but you insisted"


        if line == "yy":
                if Newbie.Tag + "No" in Player.Traits:
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                $ Count = len(Player.Harem)
                while Count:
                        $ Count -= 1
                        $ Player.Harem[Count].DrainWord("saw with "+Newbie.Tag,0,0,1)      #removes "saw with Kitty" from traits
                "You should give [Newbie.name] a call."
        else:
                $ Player.Traits.append(Newbie.Tag + "No")

        $ Party = []
        $Count = 0
        return

label Harem_Initiation(Girls=[],Girls2=[]):
    # This is called when a new girl is added to the pack
    # it makes them more open to sexing each other.
    $ Girls = Player.Harem[:]
    while Girls:
            $ Girls2 = Player.Harem[:]
            while Girls2:
                    if Girls[0] != Girls2[0] and "poly " + Girls2[0].Tag not in Girls[0].Traits:
                                $ Girls[0].Traits.append("poly " + Girls2[0].Tag)
                    if Girls[0] != Girls2[0] and "saw with " + Girls2[0].Tag in Girls[0].Traits:
                                $ Girls[0].DrainWord("saw with " + Girls2[0].Tag,0,0,1)      #removes "saw with Kitty" from traits
                    $ Girls2.remove(Girls2[0])
            $ Girls.remove(Girls[0])
    return

label Cheatcheck(Girls=[],Girls2=[]):
        # This checks whether any girl saw you with any other girl today.
        # Called by EventCalls
        # If you're in the room with that girl, it launches the cheated scene, otherwise, it has her ask you about it later.
        # Roster[Counter] is the first girl, Roster[Counter2] is the second girl
        # loops through girl 2 options until finished, then next girl 1 option, until done

        # add an aspect to account for hooking up with multiple girls that have not yet been accounted for. . .
        $ Girls = all_Girls[:]
        $ renpy.random.shuffle(Girls)
        while Girls:
                if door_locked and Girls[0].location != bg_current:
                        #exits if the door is locked and she is not in the room with you
                        pass
                else:
                        $ Girls2 = all_Girls[:]
                        while Girls2:
                            if "meet girl" in Player.daily_history:
                                                #skips if you already have an appointment
                                                return
                            elif Girls[0] in Player.Harem:
                                    #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                                    if "saw with " + Girls2[0].Tag in Girls[0].Traits:
                                                #if "saw with Kitty" in RogueX.Traits:
                                                if Girls[0] in Player.Harem and Girls2[0] in Player.Harem:
                                                        #if both girls were in the harem, this shouldn't happen
                                                        $ Girls[0].DrainWord("saw with "+Girls2[0].Tag,0,0,1)      #removes "saw with Kitty" from traits
                                                elif Girls[0] in Player.Harem and Girls2[0].Tag + "Yes" in Player.Traits:
                                                        $ Girls[0].DrainWord("saw with "+Girls2[0].Tag,0,0,1)      #removes "saw with Kitty" from traits
                                                elif bg_current == "bg_player" or bg_current == Girls[0].Home:
                                                        call Cheated(Girls[0],Girls2[0])
                                                        $ renpy.pop_call()
                                                        return
                            $ Girls2.remove(Girls2[0])
                $ Girls.remove(Girls[0])
        return

label Sharecheck(Girls=[],Girls2=[]):
        # This checks whether one of the girls is supposed to ask the other about joining the harem
        # Called by EventCalls
        # Roster[Counter] is the first girl, Roster[Counter2] is the second girl
        # loops through girl 2 options until finished, then next girl 1 option, until done

        $ Girls = all_Girls[:]
        $ Girls.remove(StormX)     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff
        while Girls:
                if Girls[0] in Player.Harem:
                        #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                        $ Girls2 = all_Girls[:]
                        $ Girls2.remove(StormX)     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff
                        while Girls2:
                                if "ask " + Girls2[0].Tag in Girls[0].Traits:
                                        #if "ask Kitty" in RogueX.Traits:
                                        if Girls[0] in Player.Harem and Girls2[0] in Player.Harem:
                                                #if both girls were in the harem, this shouldn't happen
                                                $ Girls[0].DrainWord("ask "+Girls2[0].Tag,0,0,1)      #removes "askKitty" from traits
                                        else:
                                                call Share(Girls[0],Girls2[0])
                                                $ renpy.pop_call() #skips past EventCalls
                                                return
                                $ Girls2.remove(Girls2[0])
                $ Girls.remove(Girls[0])
        return

label Addictcheck(Girls=[]):
        # Called to see if the girl is in an addiction spiral
        # Called by EventCalls
        $ Girls = active_Girls[:]
        $ renpy.random.shuffle(Girls)
        if JubesX in Girls and JubesX.Addict >= 40 and Girls[0].Resistance:
                $ Girls.remove(JubesX)
                if "sunshine" not in JubesX.History or "addiction" in JubesX.daily_history:
                            pass
                elif bg_current == JubesX.Home or bg_current == "bg_player":
                            if not JubesX.Resistance:
                                    #"I'm addicted" event
                                    call First_Addicted(JubesX)
                            else:
                                    call Addiction_Fix(JubesX)
                else:
                    if "asked meet" in JubesX.daily_history:
                            pass
                    elif "asked meet" in JubesX.daily_history and JubesX.Addict >= 60:
                            "[JubesX.name] texts you. . ."
                            call Anyline(JubesX,"I know I asked to meet you in your room earlier, but I really need a fix.")
                            $ Player.AddWord(1,"asked fix",0,0,0)
                            $ JubesX.AddWord(1,"asked meet","asked meet",0,0)
                            call ReturnToRoom
                            return
                    else:
                            "[JubesX.name] texts and asks if you could get her a fix later."
                            $ JubesX.AddWord(1,"asked meet","asked meet",0,0)
                            call ReturnToRoom
                            return
        while Girls:
                if door_locked and Girls[0].location != bg_current:
                        #if the door's locked and she's not in the room, skip it
                        pass
                elif "asked fix" in Player.daily_history and "asked meet" not in Girls[0].daily_history:
                        #this skips any new girls if you've agreed to meet another one
                        pass
                elif Girls[0].Event[3]:
                        #this skips if you've already dealt with her once recently
                        pass
                elif "angry" not in Girls[0].recent_history and "addiction" not in Girls[0].daily_history and Girls[0].Action >= 1:
                        #Activates if she needs her fix
                        if (Girls[0].Addict >= 60 or (Girls[0].Addict >= 40 and Girls[0] == JubesX)) and Girls[0].Resistance:
                                #if addict over 60, and she's completed the event chain
                                if bg_current == Girls[0].Home or bg_current == "bg_player":
                                            call Addiction_Fix(Girls[0])
                                else:
                                    if "asked meet" in Girls[0].recent_history:
                                            pass
                                    elif "asked meet" in Girls[0].daily_history and Girls[0].Addict >= 80:
                                            "[Girls[0].name] texts you. . ."
                                            call Anyline(Girls[0],"I know I asked to meet you in your room earlier, but I'm serious, this is important.")
                                            $ Player.AddWord(1,"asked fix",0,0,0)
                                            $ Girls[0].AddWord(1,"asked meet","asked meet",0,0)
                                            call ReturnToRoom
                                            return
                                    else:
                                            "[Girls[0].name] texts and asks if you could meet her in your room later."
                                            $ Girls[0].AddWord(1,"asked meet","asked meet",0,0)
                                            call ReturnToRoom
                                            return
                        #Activates if you don't need a fix but already have resistance
                        elif Girls[0].Resistance:
                                pass
                        #These are the "first time addict" event chains
                        elif Girls[0] == JubesX and Girls[0].Addict < 50:
                                pass    #she skips until she hits 50%
                        elif Girls[0].Addict >= 35 and not Girls[0].Event[1]:
                                #"I'm addicted" event
                                call First_Addicted(Girls[0])
                        elif Girls[0].Addict >= 60 and Girls[0].Event[1] <= 2:
                                #"I'm super-addicted" event
                                call First_Addicted(Girls[0])
                        elif Girls[0].Addict >= 90:
                                #"I'm crazy-addicted" event
                                call First_Addicted(Girls[0])
                $ Girls.remove(Girls[0])
        return

label Share(Girl=0,Other=0): #rkeljsv
        # This checks when one girl asks another to share you.
        # it is called by Sharecheck

        $ Girl.DrainWord("ask "+Other.Tag,0,0,1) #removes "ask Kitty" from RogueX.Traits

        if Girl.Break[0]:
                #if the girl was only recently broken up with. . .
                "[Girl.name] sends you a text."
                $ Other.change_stat("love", 90, -10)
                $ Other.change_stat("obedience", 80, 10)
                $ Other.change_stat("inhibition", 80, 5)

                if Other == RogueX:
                        call Anyline(Girl,"She said to \"stop bother'in her?\"")
                elif Other == KittyX:
                        call Anyline(Girl,"She said to \"give it a rest?\"")
                elif Other == EmmaX:
                        call Anyline(Girl,"She said \"when hell freezes over?\"")
                elif Other == LauraX:
                        call Anyline(Girl,"She said to \"fuck off?\"")
                elif Other == JeanX:
                        call Anyline(Girl,"She didn't seem to know who I was talking about.")
                elif Other == StormX:
                        call Anyline(Girl,"She said \"I would rather not?\"")
                elif Other == JubesX:
                        call Anyline(Girl,"She said to \"give it a rest?\"")
                call Anyline(Girl,"I guess we can see if she comes around on the idea.")

        else:
                if Other == JeanX or Other.GirlLikecheck(Girl) >= 800 or Approvalcheck(Other, 1800) or (Approvalcheck(Other, 1500) and Other.GirlLikecheck(Girl) >= 500):
                        # if she likes the other girl a lot, or likes you a lot, or sort of likes you both. . .
                        $ Other.AddWord(1,0,0,"poly "+Girl.Tag,0) #adds "poly Kitty" to RogueX.Traits
                        #$ Other.AddWord(1,0,0,"dating?",0) #adds "dating" to KittyX.Traits

                        $ Other.change_stat("obedience", 80, 10)
                        $ Other.change_stat("inhibition", 80, 15)

                        $ Girls = Player.Harem[:]
                        while Girls:
                                $ Girls[0].DrainWord("saw with "+Other.Tag,0,0,1)
                                $ Girls.remove(Girls[0])
                        if Girl.Event[5]:
                                # if you've already done her BF event before. . .
                                $ Player.Harem.append(Other)
                                #$ Other.AddWord(1,0,0,"dating",0)     #adds "dating" to traits
                        elif bg_current in PersonalRooms:
                                #if you're in a Girl room, launch their boyfriend speech
                                if Other.Tag+"Yes" not in Player.Traits:
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call expression Other.Tag + "_BF" #call Rogue_BF
                                $ renpy.pop_call() #skips return to Sharecheck
                                $ renpy.pop_call() #skips return to EventCalls
                        else:
                                # if not in a Girl room, ask later
                                if Other.Tag+"Yes" not in Player.Traits:
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call AskedMeet(Other,"bemused")
                else:
                        #If Girl refuses to share you
                        "[Girl.name] sends you a text."
                        call Anyline(Girl,"I talked to "+Other.name+" about sharing you, and she said she wasn't into that sort of thing,")
                        if not Approvalcheck(Other, 2000):
                                $ Other.change_stat("love", 200, -15)
                                $ Other.change_stat("obedience", 50, -5)
                                $ Other.change_stat("inhibition", 50, 5)
                                call Anyline(Girl,"She's just not into you like that.")
                        else:
                                $ Other.change_stat("love", 200, -5)
                                call Anyline(Girl,"She doesn't really like me that much. . .")

                        #means that she won't be available to ask again for another 7 days
                        $ Other.Break[0] = 7
        return

label Cheated(Girl=0,Other=0, Resolution = 0, B = 0): #rkeljsv
        # Called by EventCalls->Cheatcheck if you got caught cheating
        #Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
        $ Girl.AddWord(1,0,"relationship",0,0)
        call shift_focus(Girl)

        $ Girl.change_face("angry")
        if Girl.location != bg_current and Girl not in Party:
                "Suddenly, [Girl.name] shows up and says she needs to talk to you."
        $ Girl.location = bg_current

        $ Girl.DrainWord("asked meet",0,1) #removes "asked meet" from daily
        if "meet girl" in Player.daily_history:
                $ Player.daily_history.remove("meet girl")

        call set_the_scene
        call clear_the_room(Girl)
        call Taboo_Level(1)

        if Girl.GirlLikecheck(Other) >= 900:
                $ Resolution += 2
        elif Girl.GirlLikecheck(Other) >= 800:
                $ Resolution += 1
        $ B = int((Girl.GirlLikecheck(Other) - 500)/2)

        $ Resolution -= Girl.Cheated if Girl.Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating

        if Girl.Cheated:
                $ Girl.change_stat("love", 200, -50)
                $ Girl.change_stat("obedience", 80, -20)
                $ Girl.change_stat("inhibition", 50, -50)
                if Girl == RogueX:
                        ch_r "Why're you screw'in around on me again?"
                elif Girl == KittyX:
                        ch_k "Again with this?!"
                elif Girl == EmmaX:
                        ch_e "I noticed you're back to jumping anything that moves. . ."
                elif Girl == LauraX:
                        ch_l "You were screwing someone else again."
                elif Girl == JeanX:
                        ch_j "You were sneaking around with. . . someone again!"
                elif Girl == StormX:
                        ch_s "You are straying again. . ."
                elif Girl == JubesX:
                        ch_v "You're sleeping around on me again. . ."
        else:
                $ Girl.change_stat("love", 200, -100)
                $ Girl.change_stat("obedience", 80, -30)
                $ Girl.change_stat("inhibition", 50, -20)
                if Girl == RogueX:
                        ch_r "What the hell was that about earlier?"
                elif Girl == KittyX:
                        ch_k "Hello?! What was that?"
                elif Girl == EmmaX:
                        ch_e "Do you mind explaining what I saw earlier?"
                elif Girl == LauraX:
                        ch_l "You were with someone else earlier."
                elif Girl == JeanX:
                        ch_j "Hey! I saw you with. . . "
                        ch_j ". . . I can't remember her name, but I saw you!"
                elif Girl == StormX:
                        ch_s "I see that you've found someone else to occupy your time. . ."
                elif Girl == JubesX:
                        ch_v "I think you've been cheating. . ."

        menu:
                extend ""
                "I'm sorry.":
                        $ Girl.change_stat("love", 90, 30)
                        $ Girl.change_stat("obedience", 80, -10)
                        $ line = "sorry"
                        $ Resolution += 1

                "What do you mean?":
                        $ Girl.change_stat("love", 200, -10)
                        $ Girl.change_stat("obedience", 80, 15)
                        $ Girl.change_stat("inhibition", 80, 5)
                        if Girl == StormX:
                                ch_s "I am talking about you and [Other.name]. . ."
                        else:
                                call Anyline(Girl,"I mean you screwing around with "+Other.name+"!")
                        menu:
                                extend ""
                                "Oh! I'm sorry!":
                                    $ Girl.change_stat("love", 90, 20)
                                    $ Girl.change_stat("obedience", 80, -10)
                                    $ line = "sorry"
                                "Oh, that. Yeah.":
                                    $ Girl.change_stat("love", 200, -20)
                                    $ Girl.change_stat("obedience", 80, 10)
                                    $ line = "yeah"
                                    $ Resolution -= 1

                "You mean with [Other.name]?":
                        $ Girl.change_stat("love", 200, -15)
                        $ Girl.change_stat("obedience", 80, 20)
                        $ Girl.change_stat("inhibition", 80, 10)
                        call Anyline(Girl,"Yes, \"I mean with "+Other.name+".\"")

                        if Girl == RogueX:
                                $ line = "Y'all were screwing around behind my back!"
                        elif Girl == KittyX:
                                $ line = "Why were you all over her like that?!"
                        elif Girl == EmmaX:
                                $ line = "Or didn't you notice who you were fucking?"
                        elif Girl == LauraX:
                                $ line = "I can smell her on you."
                        elif Girl == JeanX:
                                $ line = "I played back her memories of it!"
                        elif Girl == StormX:
                                $ line = "I know that the two of your were together."
                        elif Girl == JubesX:
                                ch_v "I have a sensitive nose. . ."

                        if Girl.Cheated:
                            $ line = line+" Again!"
                        call Anyline(Girl,line)
                        menu:
                                extend ""
                                "Oh! I'm sorry!":
                                    $ Girl.change_stat("love", 90, 15)
                                    $ Girl.change_stat("obedience", 80, -10)
                                    $ line = "sorry"
                                "Oh, yeah.":
                                    $ Girl.change_stat("love", 200, -20)
                                    $ Girl.change_stat("obedience", 80, 10)
                                    $ line = "yeah"
                                    $ Resolution -= 2

        if line == "sorry":
                    $ Girl.change_face("sadside")
                    if Girl == RogueX:
                            ch_r "Well 'course you are, but that don't make it right."
                            ch_r "Screwing around with [Other.name] like that. . ."
                    elif Girl == KittyX:
                            ch_k "Don't you tell me you're sorry, I'll tell you when you're sorry!"
                    elif Girl == EmmaX:
                            ch_e "Very sorry indeed. . ."
                    elif Girl == LauraX:
                            ch_l "You will be."
                    elif Girl == JeanX:
                            ch_j "Of course you are!"
                    elif Girl == StormX:
                            ch_s "I am certain that you are."
                    elif Girl == JubesX:
                            ch_v "Oh, I bet you are."
                    $ Girl.change_face("sad")
        else:
                    $ Girl.change_face("confused")
                    if Girl == RogueX:
                            ch_r "Oh? So what do you have to say for yourself?"
                    elif Girl == KittyX:
                            ch_k "Yeah? Yeah?! What does that even mean?!"
                    elif Girl == EmmaX:
                            ch_e "I'm not sure you understand what trouble you're in here. . ."
                    elif Girl == LauraX:
                            ch_l "So did you have an explanation, or. . ."
                    elif Girl == JeanX:
                            ch_j "So do you have a story to tell me?!"
                    elif Girl == StormX:
                            ch_s "Did you have some explanation?"
                    elif Girl == JubesX:
                            ch_v "Well, did you have some excuse?"
                    $ Girl.change_face("angry")

        menu:
                extend ""
                "I really hurt you, and I'm sorry.":
                        $ Girl.change_stat("love", 90, 25)
                        if Girl == JeanX:
                                $ Girl.change_stat("obedience", 80, 10)
                                $ Resolution += 1
                                ch_j "Yes, we've established that, what else?"
                        else:
                                $ Girl.change_stat("obedience", 80, -5)
                                call Anyline(Girl,"Well at least you're owning up to it.")
                        $ Resolution += 2

                "We were just messing around, nothing serious.":
                        $ Girl.change_stat("obedience", 80, 30)
                        $ Girl.change_stat("inhibition", 80, 10)
                        if Girl == RogueX:
                                ch_r "\"Nothing serious?\" You did {i}not{/i} just tell me that."
                        elif Girl == KittyX:
                                ch_k "I'll \"nothing serious\" you!"
                        elif Girl == EmmaX:
                                ch_e "I'll be the judge of what is or is not \"serious.\""
                        elif Girl == LauraX:
                                if Approvalcheck(Girl, 1500):
                                        ch_l "Ok, that's fair."
                                else:
                                        ch_l "Do you want to try that one again?"
                        elif Girl == JeanX:
                                $ Girl.Eyes = "side"
                                $ Girl.change_stat("love", 80, 10)
                                $ Resolution += 1
                                ch_j "Oh. . . well. . ."
                                $ Girl.change_face("angry",2)
                                ch_j "That's not the point!"
                                $ Girl.Blush = 1
                        elif Girl == StormX:
                                ch_s "Nothing serious to you, but what of me?"
                        elif Girl == JubesX:
                                ch_v "Oh, is that supposed to be an excuse?"
                        $ Girl.change_stat("love", 200, -25)

                        if not Approvalcheck(Girl, 700, "O", Bonus = (B/3)):
                            $ Resolution -= 2

                "I think she's really hot.":
                    if B >= 100 or Approvalcheck(Girl, 500, "I", Bonus = (B/3)):
                            # if Like trait is 700 or more. . .
                            $ Girl.change_face("confused",Eyes="side")
                            if Girl == StormX:
                                    ch_s "She is certainly beautiful, but I do not see why that would be an excuse."
                            elif Other == KittyX:
                                    call Anyline(Girl,"Well. . . yeah, she is cute, but so what?")
                            else:
                                    call Anyline(Girl,"Well. . . yeah, she is hot, but so what?")
                            $ Girl.change_stat("lust", 90, 5)
                            $ line = "threeway"
                    else:
                            $ Girl.change_stat("love", 200, -20)
                            $ Girl.change_stat("obedience", 80, 30)
                            if Girl == RogueX:
                                    ch_r "Well that don't mean shit, [Player.name], you're with me!"
                            elif Girl == KittyX:
                                    ch_k "What does that have to do with anything?!"
                            elif Girl == EmmaX:
                                    ch_e "But I am here. [[gestures to encompass her body]"
                            elif Girl == LauraX:
                                    ch_l "That doesn't make her fair game."
                            elif Girl == JeanX:
                                    ch_j "That doesn't mean you're allowed to fuck her!"
                            elif Girl == StormX:
                                    ch_s "I do not see how that makes it better."
                            elif Girl == JubesX:
                                    ch_v "I don't care how hot she is!"
                            $ Resolution -= 2

                "Don't you like her?":
                    $ Girl.change_stat("obedience", 80, 30)
                    if B >= 100 or Approvalcheck(Girl,500,"I"):
                            # if Like trait is 700 or more. . .
                            $ Girl.change_face("confused",Eyes="side")
                            $ Girl.change_stat("inhibition", 90, 25)
                            $ Girl.change_stat("lust", 90, 5)
                            if Girl == RogueX:
                                    ch_r "I mean, sorta. Not like that really though. . ."
                            elif Girl == KittyX:
                                    ch_k "What, like. . . \"like\" like? Um. . ."
                            elif Girl == EmmaX:
                                    ch_e "She is attractive, yes, but I don't think that's relevant."
                            elif Girl == LauraX:
                                    ch_l "Yeah, but I like you too."
                            elif Girl == JeanX:
                                    ch_j "I mean. . . kinda. . ."
                            elif Girl == StormX:
                                    ch_s "I do, though perhaps not as much as you do. . ."
                            elif Girl == JubesX:
                                    ch_v "Well, yeah, but. . . don't distract me!"
                            $ line = "threeway"
                    elif B >= 50 and Girl != JeanX:
                            # if Like trait is 600 or more. . .
                            $ Girl.change_face("confused")
                            $ Girl.change_stat("love", 200, -10)
                            if Girl == EmmaX and Other != StormX:
                                    ch_e "She's a good student, but that doesn't mean I'm interested in sharing."
                            elif Girl == StormX:
                                    ch_s "I like her well enough, but what difference does that make?"
                            else:
                                    call Anyline(Girl,"We're friends, but so what?")
                    else:
                            $ Girl.change_stat("love", 200, -20)
                            if Girl == RogueX:
                                    ch_r "Whether I like her or not, don't give you rights to hook up with her."
                            elif Girl == KittyX:
                                    ch_k "What does that have to do with anything?!"
                            elif Girl == EmmaX:
                                    ch_e "That's entirely irrelevant!"
                            elif Girl == LauraX:
                                    ch_l "Not enough to share."
                            elif Girl == JeanX:
                                    ch_j "Not enough."
                            elif Girl == StormX:
                                    ch_s "I am afraid not enough."
                            elif Girl == JubesX:
                                    ch_v "I don't care how hot she is!"
                            $ Resolution -= 1

        menu:
                "I won't do it again.":
                    if Girl.Cheated:
                            $ Girl.change_stat("love", 90, 5)
                            call Anyline(Girl,"Like the last time you told me that, you mean?")
                            $ Resolution -= 1
                    else:
                            $ Girl.change_stat("love", 90, 20)
                            $ Girl.change_face("angry")
                            $ Resolution += 2 if Resolution < 3 else 0
                            call Anyline(Girl,"I'll hold you to that.")
                    $ line = 0

                "I can't make any promises, she's pretty hot.":
                            $ Girl.change_face("angry")
                            $ Girl.change_stat("love", 200, -40)
                            $ Girl.change_stat("obedience", 90, 40)
                            $ Girl.change_stat("inhibition", 90, 10)
                            call Anyline(Girl,"Then I don't know what you tell you, I think we're through.")
                            $ Resolution -= 2
                            $ line = 0

                "Have you considered maybe letting her join us?":
                        $ Girl.change_face("confused",Mouth="smile")
                        if Approvalcheck(Girl, 2200, Bonus = B) or Approvalcheck(Girl, 950, "L", Bonus = (B/3)):
                                $ Girl.change_stat("inhibition", 90, 30)
                                $ Girl.change_stat("lust", 89, 10)
                                $ Resolution += 2
                        elif Approvalcheck(Girl, 1500, Bonus = B) or Girl.GirlLikecheck(Other) >= 700:
                                $ Girl.change_stat("inhibition", 90, 10)
                                $ Girl.change_stat("lust", 90, 5)
                        else:
                                $ Resolution -= 3
                                $ Girl.change_stat("love", 200, -25)
                                $ Girl.change_stat("inhibition", 90, 10)

                        $ Girl.change_stat("obedience", 90, 40)
                        if Girl == RogueX:
                                ch_r "I don't know what to do with that, you talk'in a three-way?"
                        elif Girl == KittyX:
                                ch_k "What, like a threeway?"
                        elif Girl == EmmaX:
                                ch_e "I'm not sure how to process that."
                                ch_e "Are you suggesting a threeway?"
                        elif Girl == LauraX:
                                ch_l "You wanna fuck both of us?"
                        elif Girl == JeanX:
                                ch_j "Yeah, maybe. But not like you just randomly fucking around."
                        elif Girl == StormX:
                                ch_s "An interesting proposition. . ."
                        elif Girl == JubesX:
                                ch_v "What? . . I mean. . . "
                                ch_v ". . . what?"
                        $ line = "threeway"

        if Resolution >= 5 and line == "threeway": #she agrees to a threeway
                        if Girl.Cheated:
                                $ Girl.change_stat("love", 90, 25)
                                $ Girl.change_stat("obedience", 90, 30)
                                $ Girl.change_stat("inhibition", 90, 60)
                        else:
                                $ Girl.change_stat("love", 90, 50)
                                $ Girl.change_stat("obedience", 90, 40)
                                $ Girl.change_stat("inhibition", 90, 40)
                        if Girl == RogueX:
                                ch_r "So I catch you fool'in around on me, and you want to make it official?"
                        elif Girl == KittyX:
                                ch_k "So you cheat on me, and then ask for a threeway?"
                        elif Girl == EmmaX:
                                ch_e "Bold move. Boldness should be rewarded. . ."
                        elif Girl == LauraX:
                                ch_l "Cheat on me, and then Ask for a threeway?"
                                ch_l "Risky gamble there."
                        elif Girl == JeanX:
                                ch_j "I was thinking that -I- would be bringing other people in. . ."
                        elif Girl == StormX:
                                ch_s "I suppose it could be. . . mutually beneficial."
                        elif Girl == JubesX:
                                ch_v "I mean, I guess we could. . ."
                        call Anyline(Girl,"Maybe I could live with that, I'll talk to "+Other.name+".")

                        $ line = "poly"

        elif Resolution >= 5: #she suggests a threeway
                        if Girl.Cheated:
                                $ Girl.change_stat("love", 90, 20)
                                $ Girl.change_stat("obedience", 90, 10)
                                $ Girl.change_stat("inhibition", 90, 100)
                        else:
                                $ Girl.change_stat("love", 90, 40)
                                $ Girl.change_stat("obedience", 90, 10)
                                $ Girl.change_stat("inhibition", 90, 60)
                        if Girl == RogueX:
                                ch_r "You're just a regular polecat in heat. I guess I can't tame you."
                                ch_r "Not alone, at least."
                        elif Girl == KittyX:
                                ch_k "What a mess. I guess maybe I could share though. . ."
                        elif Girl == EmmaX:
                                ch_e "Bold move. Boldness should be rewarded. . ."
                        elif Girl == LauraX:
                                ch_l "You're a piece of work, but maybe I could share . . ."
                        elif Girl == JeanX:
                                ch_j "I was thinking that -I- would be bringing other people in. . ."
                        elif Girl == StormX:
                                ch_s "Perhaps there is a way we could both benefit from this."
                        elif Girl == JubesX:
                                ch_v "Maybe we could work together. . ."

                        if Girl in (EmmaX,StormX):
                                call Anyline(Girl,"Perhaps "+Other.name+" and I could work something out.")
                        else:
                                call Anyline(Girl,"Maybe me and "+Other.name+" can work something out.")
                        $ line = "poly"

        elif Resolution >= 2: #she agrees to forgive you
                    if line == "threeway":
                            #you've asked for a threeway, but she knocked it down
                            $ Girl.change_stat("obedience", 80, 10)
                            if Girl == RogueX:
                                    ch_r "Don't try to play cards ya just don't have."
                            elif Girl == KittyX:
                                    ch_k "Way to read the room. . ."
                            elif Girl == EmmaX:
                                    ch_e "I appreciate the initiative, if not the common sense. . ."
                            elif Girl == LauraX:
                                    ch_l "Like that'll happen . . ."
                            elif Girl == JeanX:
                                    ch_j "Nah, you haven't earned it."
                            elif Girl == StormX:
                                    ch_s "I do not think you're prepared for such a relationship."
                            elif Girl == JubesX:
                                    ch_v "I'm not interested in that right now!"
                    $ Girl.change_face("sadside")
                    if Girl.Cheated:
                            $ Girl.change_stat("obedience", 80, 15)
                            if Girl == RogueX:
                                    ch_r "I've given you a chance to do right by me, and you keep screwing it up."
                                    ch_r "I don't know how many more chances I can give you here."
                            elif Girl == KittyX:
                                    ch_k "Too many times, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "At some point I'll have to stop putting up with you. . ."
                            elif Girl == LauraX:
                                    ch_l "This is getting tired . . ."
                            elif Girl == JeanX:
                                    ch_j "I'm not giving you more chances to fuck this up."
                            elif Girl == StormX:
                                    ch_s "You have betrayed my trust too many times."
                            elif Girl == JubesX:
                                    ch_v "You've just played me too many times. . ."
                    else:
                            $ Girl.change_stat("obedience", 80, 30)
                            if Girl == RogueX:
                                    ch_r "You betrayed my trust, [RogueX.Petname]."
                                    ch_r "Don't let it happen again."
                            elif Girl == KittyX:
                                    ch_k "You hurt me here, [KittyX.Petname]. . ."
                                    ch_k "Don't hurt me like this again."
                            elif Girl == EmmaX:
                                    ch_e "I'll let you off with a warning this time, but don't let it happen again."
                            elif Girl == LauraX:
                                    ch_l "You're on thin ice, bub."
                            elif Girl == JeanX:
                                    ch_j "I'll let you off this time, but don't push it."
                            elif Girl == StormX:
                                    ch_s "You have betrayed my trust, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "I don't like these games. . ."

        else:
                    #she doesn't agree to forgive you
                    $ Girl.change_face("angry")
                    if line == "threeway":
                        $ Girl.change_stat("obedience", 80, 10)
                        if Girl == RogueX:
                                ch_r "I can't even believe you would suggest a fucking {i}threeway!{/i}"
                        elif Girl == KittyX:
                                ch_k "Seriously? A threeway?!"
                        elif Girl == EmmaX:
                                ch_e "Bold move. Sometimes boldness will get you hurt. . ."
                        elif Girl == LauraX:
                                ch_l "A threeway?"
                        elif Girl == JeanX:
                                ch_j "You're seriously looking for a prize here?"
                        elif Girl == StormX:
                                ch_s "I do not think you're prepared for such a relationship."
                        elif Girl == JubesX:
                                ch_v "You're pushing it."
                    if Girl.Cheated:
                        $ Girl.change_stat("obedience", 90, -50)
                        $ Girl.change_stat("inhibition", 90, 20)
                        if Girl == RogueX:
                                ch_r "You done this too many times for me to keep let'in you back."
                                ch_r "Sorry, [RogueX.Petname], this is the end."
                        elif Girl == KittyX:
                                ch_k "You aren't even that cute. . ."
                                ch_k "We're over."
                        elif Girl == EmmaX:
                                ch_e "I don't think I'm in the mode for these games."
                                ch_e "We're done."
                        elif Girl == LauraX:
                                ch_l "I hoped I could trust you, but you blew it again. . ."
                        elif Girl == JeanX:
                                ch_j "I gave you a shot, but you blew it."
                        elif Girl == StormX:
                                ch_s "You have betrayed my trust too many times."
                        elif Girl == JubesX:
                                ch_v "You've just played me too many times!"
                    else:
                        $ Girl.change_stat("obedience", 90, -50)
                        $ Girl.change_stat("inhibition", 90, 10)
                        if Girl == RogueX:
                                ch_r "I just don't think I can trust you anymore, [RogueX.Petname]."
                                ch_r "This is it for us."
                        elif Girl == KittyX:
                                ch_k "You hurt me. I just can't even."
                        elif Girl == EmmaX:
                                ch_e "You've lost my trust. We're done here."
                        elif Girl == LauraX:
                                ch_l "I can't trust you. I'm through."
                        elif Girl == JeanX:
                                ch_j "I gave you a shot, but you blew it."
                        elif Girl == StormX:
                                ch_s "You have betrayed my trust, [StormX.Petname]."
                        elif Girl == JubesX:
                                ch_v "I don't like these games!"

                    $ Girl.AddWord(1,0,0,"ex",0) #adds "ex" to traits
                    if Girl in Player.Harem:
                            $ Player.Harem.remove(Girl)
                    $ Girl.AddWord(1,0,"angry",0,0)


        $ Girls = all_Girls[:]
        while Girls:
                #removes "saw with Rogue" from traits
                $ Girl.DrainWord("saw with "+Girls[0].Tag,0,0,1)
                $ Girls.remove(Girls[0])

        if line == "poly":
                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0)    #adds "poly Kitty" to traits
                $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0)     #adds "ask Kitty" to traits
        else:
                $ Girl.GLG(Other,1000,-50,1)   #$ RogueX.LikeKitty -= 50

        if "ex" in Girl.Traits:
            $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
        $ Girl.Cheated += 1

        #aftermath
        menu:
                "I'm glad we could work this out." if Girl in Player.Harem:
                        $ Girl.change_face("sad")
                        if Resolution >= 3:
                                $ Girl.change_stat("love", 90, 10)
                                $ Girl.change_stat("obedience", 90, 5)
                                if Girl == RogueX:
                                        ch_r "I am too, [RogueX.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Me too, [KittyX.Petname]. . ."
                        else:
                                $ Girl.change_stat("love", 90, 5)
                                if Girl == RogueX:
                                        ch_r "Yeah, we'll see, [RogueX.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Sure, [KittyX.Petname]. . ."
                        if Girl == EmmaX:
                                ch_e "Yes, delightful."
                        elif Girl == LauraX:
                                ch_l "Yeah, sure."
                        elif Girl == JeanX:
                                ch_j "Right, sure."
                        elif Girl == StormX:
                                ch_s "We shall see if I made the correct decision, [StormX.Petname]."
                        elif Girl == JubesX:
                                ch_v "Yeah, maybe. . ."

                "Want to fool around a bit?" if Girl in Player.Harem and not Taboo:
                        if Girl.obedience + Girl.inhibition >= (1.5 * Girl.love) or Girl.lust >= 70:
                            #(obedience + inhibition) >= (1.5 * love) or lust >= 70
                            $ Girl.change_face("sly",Eyes="side")
                            $ Girl.change_stat("love", 90, 20)
                            $ Girl.change_stat("obedience", 90, 10)
                            $ Girl.change_stat("inhibition", 90, 10)
                            if Girl == StormX:
                                    ch_s "You are incorrigible, [StormX.Petname]."
                            else:
                                    call Anyline(Girl,"Sure, whatever.")
                            call expression Girl.Tag + "_SMenu" #call Rogue_SexMenu
                        else:
                            $ Girl.change_face("sad")
                            $ Girl.change_stat("love", 90, -10)
                            $ Girl.change_stat("obedience", 90, -10)
                            if Girl == RogueX:
                                    ch_r "It's still too raw, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Don't even, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "Oh, this is rich."
                            elif Girl == LauraX:
                                    ch_l "Yeah, not now."
                            elif Girl == JeanX:
                                    ch_j "Maybe later."
                            elif Girl == StormX:
                                    ch_s "Take some time to reflect on your actions, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Don't even with me right now. . ."

                "I'm sorry it didn't work out." if Girl not in Player.Harem:
                            $ Girl.change_face("sad")
                            $ Girl.change_stat("love", 90, 10)
                            if Girl == RogueX:
                                    ch_r "I am too, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Yeah, me too, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "Yes, you'll get over it. . . eventually."
                            elif Girl == LauraX:
                                    ch_l "Yeah."
                            elif Girl == JeanX:
                                    ch_j "Sure, whatever."
                            elif Girl == StormX:
                                    ch_s "Yes, it is unfortunate. . ."
                            elif Girl == JubesX:
                                    ch_v "Yeah, maybe. . ."

                "Want to have some break-up sex?" if Girl not in Player.Harem and not Taboo:
                        if Girl.obedience + Girl.inhibition >= (1.5 * Girl.love) or Girl.lust >= 70:
                            #(obedience + inhibition) >= (1.5 * love) or lust >= 70
                            $ Girl.change_face("angry",Eyes="side")
                            $ Girl.change_stat("obedience", 90, 10)
                            $ Girl.change_stat("inhibition", 90, 10)
                            if Girl == StormX:
                                    ch_s "You are incorrigible, [StormX.Petname]."
                            else:
                                    call Anyline(Girl,"Sure, whatever.")
                            $ Girl.DrainWord("angry",0,1)
                            call expression Girl.Tag + "_SMenu" #call Rogue_SMenu
                            $ Girl.AddWord(1,0,"angry",0,0) #adds "angry" to daily
                        else:
                            $ Girl.change_face("angry")
                            $ Girl.change_stat("love", 90, -20)
                            $ Girl.change_stat("obedience", 90, -10)
                            if Girl == RogueX:
                                    ch_r "You have got to be kidding me."
                            elif Girl == KittyX:
                                    ch_k "Don't even, [KittyX.Petname]. . ."
                            elif Girl == EmmaX:
                                    ch_e "Oh, this is rich."
                            elif Girl == LauraX:
                                    ch_l "Yeah, not now."
                            elif Girl == JeanX:
                                    ch_j "Maybe later."
                            elif Girl == StormX:
                                    ch_s "Take some time to reflect on your actions, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Don't even with me right now. . ."

                "Let me know if you change your mind." if Girl not in Player.Harem:
                            $ Girl.change_face("angry",Eyes="side")
                            $ Girl.change_stat("love", 90, -5)
                            $ Girl.change_stat("obedience", 90, 10)
                            if Girl == RogueX:
                                    ch_r "Yeah, I'll get right on that."
                            elif Girl == KittyX:
                                    ch_k "Oh, sure, right."
                            elif Girl == EmmaX:
                                    ch_e "Oh, I'm sure you'll be the first I tell."
                            elif Girl == LauraX:
                                    ch_l "Uh-huh."
                            elif Girl == JeanX:
                                    ch_j "Oh, sure."
                            elif Girl == StormX:
                                    ch_s "I am sure that I will, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Sure, whatever. . ."

                "Ok, see you later then.":
                            $ Girl.change_face("confused")

        if Girl == RogueX:
                ch_r "I need some time alone, [RogueX.Petname]. I'll see you later."
        elif Girl == KittyX:
                ch_k "I need some \"me\" time, I'll see you around."
        elif Girl == EmmaX:
                ch_e "Now, I need to be alone for a bit."
        elif Girl == LauraX:
                ch_l "Ok, well, bye."    #no Jean
        elif Girl == StormX:
                ch_s "I'm sure that I will see you later, [StormX.Petname]."
        elif Girl == JubesX:
                ch_v "I'm gonna. . . get out of here. . ."

        $ Round -= 10 if Round > 10 else Round

        if bg_current == Girl.Home:
                #remove Rogue from the scene (or the player)
                $ bg_current = "bg_player"
                jump Misplaced
        else:
                call remove_girl(Girl)
        return

label NoFap(Girl=0,TabStore=Taboo,counter=0): #rkeljsv
        # called when you ask them not to fap from the romance menu
        # call NoFap(Girl)

        $ Taboo = 0
        ch_p "About when you masturbate on your own time. . ."

        if "askedfap" in Girl.daily_history:
                #if it's not the first time you've asked today. . .
                if "nofap" in Girl.Traits:
                        call Anyline(Girl,"I understand already.")
                else:
                        call Anyline(Girl,"Stop bothering me with this.")

        elif "askedfap" in Girl.History:
                #if it's not the first time you asked. . .
                if not Approvalcheck(Girl, 800):
                        #rude response
                        $ Girl.change_face("angry",2,Eyes="surprised")
                        $ Girl.change_stat("love", 80, -1)
                        $ Girl.change_stat("obedience", 50, 1)
                        $ Girl.change_stat("obedience", 80, 1)
                        $ Girl.change_stat("inhibition", 30, -1)
                        $ Girl.change_stat("inhibition", 30, 3, 1)
                        if Girl == RogueX:
                                ch_r "I really don't want to go over this again. . ."
                        elif Girl == KittyX:
                                ch_k "This isn't really appropriate. . . "
                        elif Girl == EmmaX:
                                ch_e "I'd rather not discuss this again. . ."
                        elif Girl == LauraX:
                                ch_l "Hmm, I don't want to have this conversation again."
                        elif Girl == JeanX:
                                ch_j "We've been over this, and you were insane."
                        elif Girl == StormX:
                                ch_s "This really is none of your business, [StormX.Petname]."
                        elif Girl == JubesX:
                                ch_v "You, um, need to stop asking. . ."
                        $ Girl.change_face("angry",1)
                else:
                        #neutral response
                        $ Girl.change_stat("obedience", 60, 2)
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("inhibition", 60, 1)
                        $ Girl.change_stat("lust", 50, 1)
                        $ Girl.change_face("confused",1)
                        if Girl == EmmaX:
                                ch_e "Oh? This again?"
                        elif Girl == LauraX:
                                ch_l "Yeah?"
                        elif Girl == StormX:
                                ch_s "Oh, what is it, [StormX.Petname]?"
                        else: #Rogue, Kitty, Jean
                                $ Girl.change_face("confused",2)
                                call Anyline(Girl,"Um, yeah, what about it?")

        else:
                #if this is the first time you've asked her. . .
                if not Approvalcheck(Girl, 800):
                        #rude response
                        $ Girl.change_face("angry",2,Eyes="surprised")
                        $ Girl.change_stat("love", 90, -5)
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("obedience", 80, 1)
                        $ Girl.change_stat("inhibition", 30, -1)
                        $ Girl.change_stat("inhibition", 30, 3, 1)
                        if Girl == RogueX:
                                ch_r "Don't go talk'in about a girl's personal time like that."
                        elif Girl == KittyX:
                                ch_k "I, um. . . "
                                extend "hey! That's not any of your business!"
                        elif Girl == EmmaX:
                                ch_e "What I do in the privacy of my own class-"
                                ch_e "Never mind."
                        elif Girl == LauraX:
                                ch_l "Hmm, I don't want to have this conversation."
                        elif Girl == JeanX:
                                ch_j ". . ."
                                ch_j "Why are you talking about my personal habits?"
                        elif Girl == StormX:
                                ch_s ". . ."
                                ch_s "I am not really sure what business that is of yours, [StormX.Petname]."
                        elif Girl == JubesX:
                                ch_v "Do I. . ."
                                ch_v "What? What business is that of yours?!"
                        $ Girl.change_face("angry",1)
                elif not Approvalcheck(Girl, 500, "I"): # or RogueX.SEXP <= 30?
                        #shy response
                        $ Girl.change_stat("love", 90, -5)
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("obedience", 80, 1)
                        $ Girl.change_stat("inhibition", 30, -1)
                        $ Girl.change_stat("inhibition", 30, 3, 1)
                        $ Girl.change_stat("lust", 50, 3)
                        if Girl == RogueX:
                                $ Girl.change_face("surprised",2)
                                ch_r "I. .  um. . I don't really do that. . ."
                        elif Girl == KittyX:
                                $ Girl.change_face("surprised",2)
                                ch_k "Oh, um, that's not really something I. . ."
                        elif Girl == EmmaX:
                                $ Girl.change_face("confused",1)
                                ch_e "I'm not sure why what I do in private is your business. . ."
                        elif Girl == LauraX:
                                $ Girl.change_face("surprised",2)
                                ch_l "Um. . . yeah?"
                        elif Girl == JeanX:
                                ch_j "Well, look. . . that's none of your business."
                        elif Girl == StormX:
                                ch_s ". . ."
                                ch_s "I am not really sure what business that is of yours, [StormX.Petname]."
                        elif Girl == JubesX:
                                ch_v "Do I. . ."
                                ch_v "What? Um. . . I don't wanna talk about it."
                elif Approvalcheck(Girl, 500, "O"):
                        #submissive response
                        $ Girl.change_stat("obedience", 90, 5)
                        $ Girl.change_stat("inhibition", 50, 2)
                        $ Girl.change_stat("inhibition", 80, 1)
                        $ Girl.change_stat("lust", 50, 5)
                        $ Girl.change_face("confused",1)
                        if Girl == EmmaX:
                                ch_e "What of it?"
                        else: #Rogue, Kitty, Laura
                                call Anyline(Girl,"What about it?")
                else:
                        #neutral response
                        $ Girl.change_stat("obedience", 90, 4)
                        $ Girl.change_stat("inhibition", 90, 3)
                        $ Girl.change_stat("lust", 50, 3)
                        $ Girl.change_face("confused",1)
                        if Girl == EmmaX:
                                ch_e "Oh? What about it?"
                        elif Girl in (LauraX,JeanX):
                                call Anyline(Girl,"Yeah?")
                        elif Girl == StormX:
                                ch_s ". . ."
                                ch_s "What did you want to know?"
                        else: #Rogue, Kitty
                                $ Girl.change_face("confused",2)
                                call Anyline(Girl,"Um, yeah, what about it?")
        #end intro check. . .

        menu:
            extend ""
            "I'd rather you not do that." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.daily_history:
                            $ Girl.change_stat("obedience", 200, 2)
                            $ Girl.change_stat("inhibition", 90, 1)
                    if Approvalcheck(Girl, 1400, "LO"):
                            #loving response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, 4)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 90, 3)
                            $ Girl.change_face("bemused",2)
                            if Girl == RogueX:
                                    ch_r "Well, only because it seems to matter to you. . ."
                            elif Girl == KittyX:
                                    ch_k "You really care about something like that?"
                                    ch_k "Ok, fine."
                            elif Girl == EmmaX:
                                    ch_e "[EmmaX.Petname], the idea of it really bothers you?"
                                    ch_e "Fine, I can make do. . ."
                            elif Girl == LauraX:
                                    ch_l "So, that'd really bother you? . ."
                                    ch_l "I guess I could stop. . ."
                            elif Girl == JeanX:
                                    ch_j "Hmm. . ."
                                    ch_j "I guess we could give that a try. . ."
                                    ch_j "But you'd better make it up to me."
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "If you truly believe you can take over my needs, [StormX.Petname]. . ."
                            elif Girl == JubesX:
                                    ch_v "Well, I mean. . ."
                                    ch_v "I do have needs. . ."
                                    ch_v "You would need to make sure they get. . . taken care of."
                            $ Girl.change_face("bemused",1)
                    elif Approvalcheck(Girl, 1600) and not Approvalcheck(Girl, 500, "I") and Girl != JeanX:
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 90, 5)
                                    $ Girl.change_stat("lust", 50, 5)
                            $ Girl.change_face("bemused",2,Eyes="side")
                            if Girl == RogueX:
                                    ch_r "Not that I was, but. . . sure."
                            elif Girl == KittyX:
                                    ch_k "I don't. . . right, I don't."
                            elif Girl == EmmaX:
                                    ch_e "I suppose if it matters to you. . ."
                            elif Girl == LauraX:
                                    ch_l "I guess if it matters to you. . ."
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I am not really sure what business that is of yours, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "I don't really. . ."
                                    ch_v "Ok, we'll see. . ."
                            $ Girl.change_face("bemused",1)
                    elif Approvalcheck(Girl, 700, "O",Alt=[[JeanX],800]):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, 3)
                                    $ Girl.change_stat("obedience", 200, 4)
                                    $ Girl.change_stat("inhibition", 90, 5)
                                    $ Girl.change_stat("lust", 70, 5)
                            $ Girl.change_face("sly",1)
                            call Anyline(Girl,"Yes,"+Girl.Petname+".")
                    elif not Approvalcheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, -5)
                                    $ Girl.change_stat("obedience", 90, -3)
                                    $ Girl.change_stat("inhibition", 90, 3)
                            $ Girl.change_face("angry",2)
                            if Girl == KittyX:
                                    ch_k "I- this whole conversation is inappropriate!"
                            elif Girl in (EmmaX,JeanX):
                                    call Anyline(Girl,"I really don't care what \"you'd rather.\"")
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I am uninterested in your opinions on this, [StormX.Petname]."
                            else: #Rogue, Laura
                                    call Anyline(Girl,"I'd rather you stay out my business.")
                            $ Girl.change_face("angry",1)
                            $ counter = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, -1)
                                    $ Girl.change_stat("obedience", 70, 2)
                                    $ Girl.change_stat("inhibition", 60, 2)
                            $ Girl.change_face("sly",1)
                            if Girl == RogueX:
                                    ch_r "'Fraid not, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Sorry, no. I try to keep busy."
                            elif Girl == EmmaX:
                                    ch_e "No, I think I shall. . . often."
                            elif Girl == LauraX:
                                    ch_l "Sorry, [LauraX.Petname], I've got needs."
                            elif Girl == JeanX:
                                    $ Girl.change_face("confused",1)
                                    ch_j "Um. . . no?"
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I would rather we not discuss this, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Um, that would be very inconvenient for me, so. . ."
                                    ch_v "No."
                            $ counter = 1
                    if not counter:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits
            # end "ask nicely"

            "Don't do that without permission." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.daily_history:
                            $ Girl.change_stat("obedience", 200, 3)
                    if Approvalcheck(Girl, 600, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, 3)
                                    $ Girl.change_stat("obedience", 80, 3)
                                    $ Girl.change_stat("obedience", 200, 4)
                                    $ Girl.change_stat("inhibition", 90, 5)
                                    $ Girl.change_stat("lust", 50, 5)
                                    $ Girl.change_stat("lust", 70, 5)
                            $ Girl.change_face("sly")
                            call Anyline(Girl,"Yes,"+Girl.Petname+".")
                    elif Approvalcheck(Girl, 1200, "LO"):
                            #positive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, 4)
                                    $ Girl.change_stat("obedience", 80, 3)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 90, 3)
                                    $ Girl.change_stat("lust", 50, 5)
                            $ Girl.change_face("bemused",1)
                            if Girl == RogueX:
                                    ch_r "I guess if it means so much to you. . ."
                            elif Girl == KittyX:
                                    ch_k "I guess I could do \"no_fap no-\" what month even is this? . ."
                            elif Girl == EmmaX:
                                    ch_e "Well, aren't you being dominant. . ."
                                    ch_e "I suppose I could restrain myself. . ."
                            elif Girl == LauraX:
                                    ch_l "I guess I could."
                            elif Girl == JeanX:
                                    ch_j "Hmm. . ."
                                    ch_j "I guess we could give that a try. . ."
                                    ch_j "But you'd better make it up to me."
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "Well, I could give that a try, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Well, I mean. . ."
                                    ch_v "I do have needs. . ."
                                    ch_v "You would need to make sure they get. . . taken care of."
                    elif not Approvalcheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 90, 5)
                                    $ Girl.change_stat("lust", 50, 5)
                            $ Girl.change_face("bemused",2,Eyes="side")
                            if Girl == RogueX:
                                    ch_r "It's not like I even do. . ."
                            elif Girl == KittyX:
                                    ch_k "Girls don't do that. But even if I did, you're being rude."
                            elif Girl == EmmaX:
                                    ch_e "I really don't think it's any of your business."
                            elif Girl == LauraX:
                                    ch_l "Not interested."
                            elif Girl == JeanX:
                                    ch_j "I don't like your tone. . ."
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "Do not take this tone with me, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Um, I don't know about that. . ."
                            $ Girl.change_face("normal",1)
                            $ counter = 1
                    elif not Approvalcheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 70, -5)
                                    $ Girl.change_stat("love", 90, -5)
                                    $ Girl.change_stat("obedience", 60, -3)
                                    $ Girl.change_stat("obedience", 90, -3)
                                    $ Girl.change_stat("inhibition", 90, 3)
                            $ Girl.change_face("angry",2)
                            if Girl == RogueX:
                                    ch_r "Fuck you I won't."
                            elif Girl == KittyX:
                                    ch_k "I- this whole conversation is inappropriate!"
                            elif Girl == EmmaX:
                                    ch_e "I really don't think it's any of your business."
                            elif Girl == LauraX:
                                    ch_l "Don't tell me what to do."
                            elif Girl == JeanX:
                                    ch_j "Buzz off."
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I would rather we not discuss this, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Rude. . ."
                            $ Girl.change_face("angry",1)
                            $ counter = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, -2)
                                    $ Girl.change_stat("obedience", 70, -2)
                                    $ Girl.change_stat("inhibition", 60, 2)
                            $ Girl.change_face("bemused",2)
                            if Girl == RogueX:
                                    ch_r "'Fraid not, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Sorry, no. I try to keep busy."
                            elif Girl == EmmaX:
                                    ch_e "No, I think I shall. . . often."
                            elif Girl == LauraX:
                                    ch_l "Sorry, [LauraX.Petname], I've got needs."
                            elif Girl == JeanX:
                                    $ Girl.change_face("confused",1)
                                    ch_j "Um. . . no?"
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I would rather we not discuss this, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "I'm gonna do. . . whatever."
                            $ Girl.change_face("bemused",1)
                            $ counter = 1
                    if not counter:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits
            # end "obedience order"

            "You can do that if you need to." if "nofap" in Girl.Traits:
                    if "askedfap" not in Girl.daily_history:
                            $ Girl.change_stat("love", 90, 1)
                            $ Girl.change_stat("obedience", 90, 1)
                            $ Girl.change_stat("inhibition", 90, 1)
                    if not Approvalcheck(Girl, 500, "I"):
                            #shy response
                            if "okfap" not in Girl.History:
                                    $ Girl.change_stat("love", 60, 1)
                                    $ Girl.change_stat("love", 90, 5)
                                    $ Girl.change_stat("obedience", 60, 3)
                                    $ Girl.change_stat("inhibition", 70, 5)
                                    $ Girl.change_stat("lust", 90, 10)
                            $ Girl.change_face("confused",2)
                            if Girl == RogueX:
                                    ch_r "Right! Not that I ever do that anyway, of course. . ."
                            elif Girl == KittyX:
                                    ch_k "Oh? Um, thanks?"
                            elif Girl == EmmaX:
                                    ch_e "I'm glad that I have your permission. . ."
                            elif Girl == LauraX:
                                    ch_l "Good to know."
                            elif Girl == JeanX:
                                    ch_j "Well. . . good?"
                            elif Girl == StormX:
                                    ch_s "Oh?"
                                    ch_s "Good."
                            elif Girl == JubesX:
                                    ch_v "Huh? Ok then. . ."
                            $ Girl.change_face("smile",1)
                    elif Approvalcheck(Girl, 750, "O"):
                            #submissive response
                            if "okfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, 20)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("obedience", 90, 10)
                                    $ Girl.change_stat("inhibition", 90, 10)
                                    $ Girl.change_stat("lust", 90, 10)
                            $ Girl.change_face("sly",1)
                            call Anyline(Girl,"Yes,"+Girl.Petname+".")
                    else:
                            #positive response
                            if "okfap" not in Girl.History:
                                    $ Girl.change_stat("love", 90, 5)
                                    $ Girl.change_stat("obedience", 60, 3)
                                    $ Girl.change_stat("inhibition", 70, 3)
                                    $ Girl.change_stat("lust", 50, 5)
                            $ Girl.change_face("surprised",2)
                            if Girl == RogueX:
                                    ch_r "Great! I mean, that's cool."
                            elif Girl == KittyX:
                                    ch_k "Nice! I'll, um, yeah."
                            elif Girl == EmmaX:
                                    ch_e "Oh, what a relief. . ."
                            elif Girl == LauraX:
                                    ch_l "Finally."
                            elif Girl == JeanX:
                                    ch_j "Oh! That'll be nice. . ."
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "That would be fantastic, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Oh. . . oh! Nice!"
                            $ Girl.change_face("smile",1)
                    $ Girl.DrainWord("nofap",0,0,1) #removes "nofap" tag from traits
                    $ Girl.AddWord(1,0,0,0,"okfap")  #adds "okfap" tag to History

                    #fix add a potential for the girl to run out now. . .
            #end "return permission"

            "Nevermind":
                    if not Approvalcheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 80, 10)
                                    $ Girl.change_stat("inhibition", 50, 5)
                            $ Girl.change_face("bemused",1)
                            if Girl == EmmaX:
                                    ch_e "Back to more appropriate topics, I hope?"
                            elif Girl == LauraX:
                                    ch_l "Glad we're off this one. . ."
                            elif Girl == JeanX:
                                    $ Girl.change_face("confused",1)
                                    ch_j "Um. . .ok?"
                            elif Girl == StormX:
                                    ch_s ". . . Fine."
                            else: #Rogue, Kitty
                                    $ Girl.change_face("surprised",2)
                                    call Anyline(Girl,"Right! What were we even talking about?")
                                    $ Girl.change_face("smile",1)
                    elif Approvalcheck(Girl, 500, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("obedience", 60, 5)
                                    $ Girl.change_stat("inhibition", 80, 5)
                                    $ Girl.change_stat("lust", 50, 5)
                            $ Girl.change_face("sly",1)
                            if Girl in (EmmaX, StormX):
                                    call Anyline(Girl,"Very Well. . .")
                            else:#Rogue, Kitty, Laura, Jean, Jubuilee
                                    call Anyline(Girl,"Ok.")
                    elif not Approvalcheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("love", 80, 5)
                                    $ Girl.change_stat("obedience", 50, 5)
                            $ Girl.change_face("angry",2,Eyes="side")
                            if Girl == RogueX:
                                    ch_r "Damned straight, \"never mind.\""
                            elif Girl == EmmaX:
                                    ch_e "I should hope so . . ."
                            elif Girl == StormX:
                                    ch_s "Of course."
                            else: #Kitty, Laura, Jean
                                    call Anyline(Girl,"Damned right, \"never mind.\"")
                            $ Girl.change_face("angry",1)
                    else:
                            #neutral response
                            if "askedfap" not in Girl.History:
                                    $ Girl.change_stat("obedience", 50, 3)
                                    $ Girl.change_stat("inhibition", 50, 2)
                            $ Girl.change_face("sly",1)
                            if Girl in (EmmaX,StormX):
                                    call Anyline(Girl,"Very Well. . .")
                            else:#Rogue, Kitty, Laura, Jean
                                    call Anyline(Girl,"Ok.")
            #end "nevermind"

        $ Girl.AddWord(1,0,"askedfap",0,"askedfap")  #adds "askedfap" tag to Daily and History
        $ Taboo = TabStore
        return

label girl_key(Girl):
    call shift_focus(Girl)
    call set_the_scene

    $ Girl.change_face("bemused")

    if Girl not in [LauraX, JeanX, JubesX]:
        $ Girl.ArmPose = 2

    if Girl == RogueX:
        ch_r "Hey, you've been sleeping over a lot, I figured you might want a key?"
    elif Girl == KittyX:
        ch_k "So you've[KittyX.like]been dropping by a lot lately, I figured you might want a key. . ."
    elif Girl == EmmaX:
        ch_e "You've been coming by fairly often. . ."
        ch_e ". . . you might want a key. . ."
    elif Girl == LauraX:
        ch_l "Hey, so. . . this isn't something I usually do but. . ."
        ch_l "Look, you've been sleeping over a lot and I was thinking. . ."
        ch_l "Just take it already."
        "She takes your hand and practically forces a key onto your palm before making your fingers close on it."
    elif Girl == JeanX:
        ch_j "Oh, here, just in case you wanted to drop by."
        "She tossed a key at you, which you manage to catch."
    elif Girl == StormX:
        ch_s "You have been coming up more often. . ."
        ch_s ". . . you might want a key. . ."
    elif Girl == JubesX:
        ch_v "Oh, um. . ."
        ch_v "We've been sleeping together for a bit and. . ."
        ch_v "Here."
        "She takes your hand and hands you her room key."

    ch_p "Thanks."

    if Girl not in [LauraX, JeanX, JubesX]:
        $ Girl.ArmPose = 1

    $ Keys.append(Girl)

    $ Girl.Event[0] = 1

    return

label girl_boyfriend(Girl):
    call shift_focus(Girl)

    $ Player.AddWord(1, "interruption")
    $ Girl.DrainWord("asked meet")

    if Girl.location != bg_current and Girl not in Party:
        $ Girl.location = bg_current

        if Girl == RogueX:
            "Suddenly, [Girl.name] shows up and says she needs to talk to you."
        elif Girl == KittyX:
            "[Girl.name] approaches you and asks if the two of you can talk."
        elif Girl == EmmaX:
            "[Girl.name] approaches you and asks if the two of you can talk."
        elif Girl == LauraX:
            "[Girl.name] approaches you and motions that she wants to speak to you alone."
        elif Girl == StormX:
            "[Girl.name] approaches you and asks if the two of you can talk."
    elif Girl in Party:
        if Girl == RogueX:
            "[Girl.name] turns towards you and asks if the two of you can talk."
        elif Girl  == KittyX:
            "[Girl.name] turns towards you and asks if the two of you can talk."
        elif Girl == EmmaX:
            "[Girl.name] turns towards you and asks if the two of you can talk."
        elif Girl == LauraX:
            "[Girl.name] turns towards you and motions that she wants to speak to you alone."
        elif Girl == StormX:
            "[Girl.name] turns towards you and asks if the two of you can talk."

    call set_the_scene(0)
    call Display_Girl(Girl)

    if Girl == KittyX:
        "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."
    elif Girl == EmmaX:
        "You can tell she's a bit uncomfortable about whatever she has to say."
    elif Girl == LauraX:
        "She looks a bit concerned and you can tell she's a bit anxious about whatever she has to say."

    call Taboo_Level
    call clear_the_room(Girl)

    $ Girl.daily_history.append("relationship")

    if Girl not in [LauraX, StormX]:
        $ Girl.change_face("bemused", 1)

        if Girl == RogueX:
            ch_r "So, [Girl.Petname], we've been hanging out for a while now."
            ch_r ". . ."
        elif Girl == KittyX:
            ch_k "So, [Girl.Petname], we've[Girl.like]been hanging for a while, right?"
            ch_k ". . ."
        elif Girl == EmmaX:
            ch_e "[EmmaX.Petname], we've been. . . enjoying ourselves for a while now."
            ch_e ". . ."

        $ Girl.Eyes = "sexy"

        $ line = None

        if Girl == RogueX:
            $ line = "Right?"
        elif Girl == KittyX:
            $ line = "Right?"
        elif Girl == EmmaX:
            $ line = "You have been enjoying yourself?"

        menu:
            Girl.voice "[line]"
            "Yeah, it's been great." if Girl in [RogueX]:
                $ Girl.change_stat("love", 200, 20)
            "Yeah. And it's been amazing." if Girl in [KittyX, EmmaX]:
                $ Girl.change_stat("love", 200, 20)
            "Yeah, I guess":
                $ Girl.change_stat("love", 200, 10)
            "Um, maybe?" if Girl in [RogueX]:
                $ Girl.change_stat("love", 200, -10)
                $ Girl.change_stat("obedience", 200, 30)
            "Uhm. . . maybe?" if Girl in [KittyX, EmmaX]:
                $ Girl.change_stat("love", 200, -10)
                $ Girl.change_stat("obedience", 200, 30)

        if Girl.SEXP >= 10:
            if Girl == RogueX:
                ch_r "I mean, we've done some stuff. . ."
            elif Girl == KittyX:
                ch_k "I mean, I've gone further with you than I've ever been with anybody before. . ."
            elif Girl == EmmaX:
                ch_e "I think we've been engaging in some rather inappropriate behavior. . ."
        if Girl.SEXP >= 15:
            if Girl == RogueX:
                ch_r "Like {i}sex{/i} stuff. . ."
            elif Girl == KittyX:
                ch_k "You know[Girl.like]. . .in the {i}bedroom{/i}. . ."
            elif Girl == EmmaX:
                ch_e "- for a student and teacher, at least. . ."

        if len(Player.Harem) >= 2:
            if Girl == RogueX:
                ch_r "I know you've been going with those other girls for a while now, but we got talking and . . ."
            elif Girl == KittyX:
                ch_k "I know you[KittyX.like]really get around and all. . ."
            elif Girl == EmmaX:
                ch_e "I understand that this isn't an exclusive deal for you. . ."
        elif Girl == KittyX and RogueX in Player.Harem:
            if "dating?" in KittyX.Traits:
                ch_k "I know you're kinda[Girl.like][RogueX.name]'s boyfriend and all. . . but she and I were talking and[Girl.like]. . ."
            else:
                ch_k "I know you're kinda[Girl.like][RogueX.name]'s boyfriend and all. . ."
        elif Player.Harem:
            if Girl == RogueX:
                ch_r "I know you've been going with [Player.Harem[0].name] for a while now, but we got talking and . . ."
            elif Girl == KittyX:
                ch_k "I know you're kinda[KittyX.like]dating [Player.Harem[0].name] and all. . ."
            elif Girl == EmmaX:
                ch_e "I understand that you've been dating [Player.Harem[0].name]. . ."

        if not Girl.Event[5]:
            if Girl == RogueX:
                ch_r "Right, so I was thinking. . ."
                ch_r "I haven't really been able to have a stable relationship, since I couldn't touch anyone."
                ch_r "This is all very new to me, but I'm feeling my way through it as best I can."
                ch_r "Let's make it official, you want to be my boyfriend?"
            elif Girl == KittyX:
                ch_k "So, uhm. . ."
                ch_k "It’s not like I[KittyX.like]haven’t gone out with guys before."
                ch_k "I just[KittyX.like]..wow, this is so awkward.  I really like you a lot and. . ."
                ch_k "I mean. . . do you wanna[KittyX.like]be my boyfriend?"
                ch_k "[KittyX.Like]maybe we could make it official?"
            elif Girl == EmmaX:
                ch_e "So, that being the case. . ."
                ch_e "I was wondering if you'd like to make this a bit more official."
                ch_e "If I could perhaps consider you my. . ."
                ch_e "Boyfriend?"
                ch_e "- or something to that effect."
        elif Girl == KittyX and "dating?" in Girl.Traits:
            ch_k "[RogueX.name] said it’d totally be cool if we were[Girl.like]dating, too."
        elif Player.Harem:
            if Girl == RogueX:
                ch_r "I'd still like to be your girlfriend too."
            elif Girl == KittyX:
                ch_k "If you were okay with it. . . I’d still like to be your girlfriend, too."
            elif Girl == EmmaX:
                ch_e ". . . but I would still like to also consider you my boyfriend as well."
        else:
            if Girl == RogueX:
                ch_r "You can be a real jerk sometimes, but still. . . I'm serious about this."
                ch_r "I think I want to be your girlfriend. . . officially"
            elif Girl == KittyX:
                ch_k "I wish you weren’t[Girl.like]such a jerk sometimes, but still. . . I’m totally serious about this."
                ch_k "I wanna be your girlfriend[Girl.like]officially."
            elif Girl == EmmaX:
                ch_e "I don't know why I put up with you, but I do still want to be your girlfriend."

        $ Girl.Event[5] += 1

        menu:
            extend ""
            "I'd love to!" if Girl in [RogueX]:
                $ Girl.change_stat("love", 200, 30)

                "[Girl.name] leaps in and kisses you deeply."

                $ Girl.change_face("kiss")
                $ Girl.Kissed += 1
            "Are you kidding? I'd love to!" if Girl in [KittyX, EmmaX]:
                $ Girl.change_stat("love", 200, 30)

                "[Girl.name] wraps her arms around you and starts kissing you passionately."

                $ Girl.change_face("kiss")

                call girl_kissing_launch(Girl, "kiss you")

                $ Girl.Kissed += 1
            "Um, ok." if Girl in [RogueX, EmmaX]:
                $ Girl.Brows = "confused"

                if Girl in [RogueX]:
                    "[Girl.name] is a bit put off by your casual acceptence of reality, but takes it as a positive sign and hugs you."
                elif Girl in [EmmaX]:
                    "[Girl.name] seems a little put off by how casually you’re taking all this."
            "Uhm[Girl.like]okay." if Girl in [KittyX]:
                $ Girl.Brows = "confused"

                "[Girl.name] seems a little put off by how casually you’re taking all this."
                "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."
            "I'm with someone now." if Player.Harem:
                $ Girl.change_face("sad",1)

                if Girl == RogueX:
                    ch_r "I know, I know, I just thought maybe you could go out with me too?"
                elif Girl == KittyX:
                    ch_k "I know.  I just[Girl.like]. . . I thought maybe you could go out with me, too, maybe?"
                elif Girl == EmmaX:
                    ch_e "I understand.  I thought that perhaps you could go out with me as well?"

                menu:
                    extend ""
                    "Sure" if Girl in [RogueX]:
                        $ Girl.change_stat("love", 200, 30)

                        "[Girl.name] leaps in and kisses you deeply."

                        $ Girl.change_face("kiss")
                        $ Girl.Kissed += 1
                    "Yes. Absolutely." if (Girl == KittyX and "KittyYes" in Player.Traits) or (Girl == EmmaX and "EmmaYes" in Player.Traits):
                        $ Girl.change_stat("love", 200, 30)

                        "[Girl.name] wraps her arms around you and starts kissing you passionately."

                        $ Girl.change_face("kiss")

                        call girl_kissing_launch(Girl, "kiss you")

                        $ Girl.Kissed += 1
                    "She wouldn't understand." if len(Player.Harem) == 1:
                        $ line = "no."
                    "They wouldn't be cool with that." if len(Player.Harem) > 1:
                        $ line = "no."
                    "I'm sorry, but. . . no." if Girl.Event[5] != 20:
                        $ line = "no."
                    "No way.":
                        jump girl_boyfriend_jerk_ending

                if line == "no":
                    $ Girl.change_stat("love", 200, -10)

                    if Girl == RogueX:
                        ch_r "I get it. That's fine."
                    elif Girl == KittyX:
                        ch_k "Well. . . okay. I get it."
                    elif Girl == EmmaX:
                        ch_e "Well. . ."
                        ch_e "I suppose I understand."

                    $ Girl.Event[5] = 20

                    call remove_girl(Girl)

                    $ line = 0

                    return
            "Not really.":
                jump girl_boyfriend_jerk_ending

        $ Girl.Petnames.append("boyfriend")
    elif Girl == LauraX:
        $ Girl.change_face("angry", 1, Eyes = "side")

        $ line = 0

        ch_l "Hey. So. [Girl.Petname]. . ."

        $ Girl.change_face("confused",1,Mouth="lipbite")

        ch_l "I don't know- . . . you're pretty fun to hang out with, ya know?"

        menu:
            extend ""
            "I really love hanging out with you too!":
                $ Girl.change_face("surprised",2)

                ch_l "Right, so-"

                $ Girl.change_stat("obedience", 50, -3)
                $ Girl.change_stat("inhibition", 80, 1)

                ch_l ". . ."

                $ Girl.change_stat("love", 200, 5)
                $ Girl.change_face("bemused",1,Eyes="side")

                ch_l "\"love\" is kind of a strong word, [Girl.Petname]."
            "Yeah, sure, it's a lot of fun.":
                $ Girl.change_stat("love", 200, 10)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.change_face("smile",0)

                ch_l "Right?"
            "I mean, it beats math class. . .":
                $ Girl.change_stat("love", 200, 3)
                $ Girl.change_stat("obedience", 80, 3)
                $ Girl.change_stat("inhibition", 80, -3)
                $ Girl.change_face("angry",1)

                ch_l "Um, less enthusiasm than I was expecting. . ."
            "If you say so.":
                $ Girl.change_stat("obedience", 80, 6)
                $ Girl.change_stat("inhibition", 80, -8)
                $ Girl.change_face("confused",1)

                ch_l ". . ."

        ch_l "So like I was saying, I don't exactly have a ton of friends."
        $ Girl.change_face("sadside",1)
        ch_l "I kind of grew up in a rough place, and then spent a lot of time on the road."
        ch_l "I had a life before coming here."

        menu:
            extend ""
            "What was it like?":
                $ Girl.change_stat("love", 200, 7)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_face("sad",1,Mouth="lipbite")
            "Yeah? I know.":
                $ Girl.change_stat("love", 200, 3)
                $ Girl.change_stat("obedience", 80, 4)
                $ Girl.change_stat("inhibition", 80, 1)
                $ Girl.change_face("confused",1,Mouth="lipbite")
            "I don't need a lot of backstory drama.":
                $ Girl.change_stat("love", 200, -5)
                $ Girl.change_stat("obedience", 80, 10)
                $ Girl.change_stat("inhibition", 80, -5)
                $ Girl.change_face("angry",1)

                $ line = "bad"

                ch_l "Fine!"
                ch_l "\"Keep it simple\" it is then."
                ch_l "I don't hate hanging out with you, is all."

        if line != "bad":
            $ Girl.change_face("normal",1,Eyes="side")
            ch_l "Well, you may have guessed I'm related to Wolverine."

            menu:
                extend ""
                "Kinda obvious, yeah.":
                    $ Girl.change_stat("love", 200, 4)
                "I had no idea!":
                    $ Girl.change_stat("love", 200, 3)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_face("confused",1)
                "Duh.":
                    $ Girl.change_stat("love", 200, 1)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_face("angry",1)

            ch_l "Well I'm actually his partial clone."

            $ Girl.change_face("angry",1,Eyes="side")

            ch_l "I was created to be some sort of biological weapon, an assassin."
            ch_l "I did a lot of work for them as a kid, until eventually I escaped."

            $ Girl.change_face("sadside",1)

            ch_l "After that, I had to do a lot of stuff. . . to stay alive."
            ch_l "Stuff I'm not proud of."

            $ Girl.change_face("sad",1)

            ch_l "But I don't know. . . being around you, I think it helps."

            $ Girl.change_face("sad",1,Mouth="smile")

            ch_l "I kind of feel. . . better."

        if Girl.SEXP >= 20:
            $ Girl.change_stat("obedience", 80, 3)
            $ Girl.change_stat("inhibition", 80, 2)
            $ Girl.change_stat("lust", 80, 5)
            $ Girl.change_face("sly",1)

            ch_l "You really are good in bed, after all."

        if len(Player.Harem) >= 2:
            ch_l "And I know that you have your share of other girls. . ."
            ch_l ". . . but I'd still like to be a part of your life."
        elif Player.Harem:
            ch_l "And I know you're with someone else. . ."
            ch_l ". . . but I'd still like to be a part of your life."
        else:
            ch_l "I'd just like to be a part of your life."

        $ Girl.change_face("sad",1,Mouth="smile")

        ch_l "That's it."

        $ Girl.Event[5] += 1

        menu:
            extend ""
            "Yeah! I really love you.":
                $ Girl.change_stat("love", 200, -3)
                $ Girl.change_stat("obedience", 80, -3)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_face("surprised",1)

                ch_l "Whoa!"

                $ Girl.change_face("perplexed")

                ch_l "Maybe cool your jets there, [Girl.Petname]."

                $ Girl.change_face("smile",Eyes="side")

                ch_l "I wasn't. . ."
                ch_l "I don't think we're there. . ."

                $ Girl.change_face("perplexed",1)

                ch_l "Right?"

                menu:
                    extend ""
                    "Maybe you aren't.":
                        $ Girl.change_stat("love", 200, 10)
                        $ Girl.change_stat("obedience", 80, 5)
                        $ Girl.change_stat("inhibition", 80, 5)
                        $ Girl.change_stat("lust", 80, 2)
                        $ Girl.change_face("smile",1,Eyes="side")

                        ch_l "Hehe. . . um."
                    "I guess, sure.":
                        $ Girl.change_stat("love", 200, 6)
                        $ Girl.change_stat("obedience", 80, 3)
                        $ Girl.change_stat("inhibition", 80, 2)
                        $ Girl.change_face("angry",1,Eyes="side",Mouth="lipbite")

                        ch_l "Right, so. . ."
            "Yeah, I think that'd be great.":
                $ Girl.change_stat("love", 200, 6)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_face("smile",1,Eyes="side")

                ch_l "Cool."
            "Hmm? Ok.":
                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("obedience", 80, 5)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_face("confused",1,Eyes="side")

                ch_l "Yeah. . . cool."
            "I'm not really into that.":
                $ Girl.change_stat("love", 200, -5)
                $ Girl.change_stat("obedience", 80, 5)
                $ Girl.change_stat("inhibition", 80, -5)
                $ Girl.change_face("sad",1)

                if len(Player.Harem) >= 2:
                    ch_l "Is it because of [Player.Harem[0].name] and the rest?"
                elif Player.Harem:
                    ch_l "Is it because of [Player.Harem[0].name]?"
                else:
                    ch_l "Why not? What's the deal?"

                menu:
                    extend ""
                    "Yeah, I don't think she'd understand." if len(Player.Harem) == 1:
                        $ Girl.change_stat("love", 200, -5)
                        $ Girl.change_stat("obedience", 80, 7)
                        $ Girl.change_face("angry",1,Eyes="side")
                        $ Girl.GLG(Player.Harem[0],800,-20,1)

                        ch_l "That bitch."
                    "They wouldn't be cool with that." if len(Player.Harem) > 1:
                        $ Girl.change_stat("love", 200, -5)
                        $ Girl.change_stat("obedience", 80, 7)
                        $ Girl.change_face("angry",1,Eyes="side")

                        call Haremchange_stat(Girl,700,-20) #lowers like of all Harem girls by 10

                        ch_l "Bitches."
                    "It's. . . complicated.":
                        $ Girl.change_stat("love", 200, -20)
                        $ Girl.change_stat("obedience", 80, 8)
                        $ Girl.change_stat("inhibition", 80, -5)
                        $ Girl.change_face("angry",1)

                        ch_l "Complicated. Sure. Whatever."

                        $ Girl.change_face("angry",1,Eyes="side")

                        if len(Player.Harem) >= 2:
                            ch_l "Probably those bitches."

                            call Haremchange_stat(Girl,700,-10) #lowers like of all Harem girls by 10
                        elif Player.Harem:
                            ch_l "Probably because of her."

                            $ Girl.GLG(Player.Harem[0],800,-20,1)

                        $ line = "no"
                    "I'm just not into you like that.":
                        $ Girl.change_stat("love", 200, -10)
                        $ Girl.change_face("surprised",1)

                        ch_l "Oh."

                        $ Girl.change_stat("obedience", 80, 10)
                        $ Girl.change_stat("inhibition", 80, 5)
                        $ Girl.change_face("sadside",1)

                        ch_l "Ok, I guess I can respect that."

                $ Girl.change_face("sad",1)

                if line != "no":
                    ch_l "We're still cool though."

                ch_l "I should. . . leave."
                "[Girl.name] wanders off in a bit of a daze."

                $ Girl.Event[5] = 20

                call remove_girl(Girl)
                $ line = 0

                return

        if Player.Harem:
            if not Approvalcheck(Girl, 1400):
                if len(Player.Harem) >= 2:
                    ch_l "So you'll break up with the others?"
                else:
                    ch_l "So you'll break up with [Player.Harem[0].name]?"

                menu:
                    extend ""
                    "Yes, you're worth it.":
                        $ Girl.change_stat("love", 200, 20)
                        $ Girl.change_stat("obedience", 80, 5)
                        $ Girl.change_stat("inhibition", 80, 5)
                        $ Girl.change_face("surprised",2,Mouth="smile")

                        ch_l ". . ."

                        $ Girl.change_face("smile",1)

                        # fix, I need to add code here to initiate breakups with the rest. . .

                        $ Girl.Event[5] = 10
                    "I'd rather you join us.":
                        $ line = 0
                        if Approvalcheck(Girl, 1200):
                            $ Girls = Player.Harem[:]

                            while Girls and line != "no":
                                if Girl.GirlLikecheck(Girls[0]) <= 500:
                                    $ line = "no"

                                $ Girls.remove(Girls[0])
                        else:
                            $ line = "no"

                        if line == "no":
                            $ Girl.change_stat("love", 200, -10)
                            $ Girl.change_stat("obedience", 80, 10)
                            $ Girl.change_face("angry",1)

                            call Haremchange_stat(Girl,700,-10)

                            ch_l "Eh, I'll pass."
                        else:
                            $ Girl.change_stat("love", 200,5)
                            $ Girl.change_stat("obedience", 80, 15)
                            $ Girl.change_stat("inhibition", 80, 10)
                            $ Girl.change_face("bemused",1)

                            ch_l "Well, I s'pose that wouldn't be so terrible."
                    "What? Of course not.":
                        $ Girl.change_stat("love", 200, -25)
                        $ Girl.change_stat("obedience", 80, 5)

                        call Haremchange_stat(Girl,700,-20)

                        $ Girl.change_face("angry",1)

                        ch_l "Well, fine then."

                        $ line = "no"
                if line == "no":
                    $ Girl.Event[5] = 20

                    call remove_girl(Girl)
                    $ line = 0

                    return

            if len(Player.Harem) >= 2:
                ch_l "And you don't think the others would mind?"
            else:
                ch_l "And you don't think [Player.Harem[0].name] would mind?"
            menu:
                extend ""
                "No, actually they're fine with it." if "LauraYes" in Player.Traits:
                    $ Girl.change_stat("love", 200, 5)
                    $ Girl.change_stat("obedience", 80, 10)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_face("surprised",1)

                    ch_l "Oh, cool."
                "Actually. . . I guess we'll need to work on that one." if "LauraYes" not in Player.Traits:
                    $ Girl.change_stat("love", 200, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("lust", 80, 1)
                    $ Girl.change_face("confused",1)

                    ch_l "Hmm, get back to me, I guess?"

                    $ Girl.Event[5] = 20

                    call remove_girl(Girl)

                    $ line = 0

                    return

            call Haremchange_stat(Girl,900,20)
    elif Girl == StormX:
        $ Girl.change_face("smile")

        ch_s "[Girl.Petname]. . . I was hoping that we could talk. . ."

        menu:
            extend ""
            "Yes?":
                pass
            "I'm kinda busy.":
                $ Girl.change_face("sadside")
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 50, 2)

                ch_s "Then I won't take more of your time than is necessary."

                $ Girl.change_face("grimace")

        $ Girl.Event[5] = 20

        ch_s "I have been enjoying the time we've spent together."
        ch_s "I mean to say, I have been enjoying you."

        $ Girl.change_face("smile",Eyes="side")

        ch_s ". . ."

        $ Girl.change_face("smile")

        ch_s "May I tell you a story?"

        menu:
            extend ""
            "Sure.":
                pass
            "Can we not?":
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("inhibition", 70, -2)
                $ Girl.change_face("confused")

                ch_s "I think you will benefit from it."
            "Like I said, I'm really busy here.":
                $ Girl.change_face("sadside")
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 60, 5)
                $ Girl.change_stat("inhibition", 70, -2)

                ch_s "Then I won't take more of your time."
                ch_s "Let me know when your. . . schedule clears up."

                call remove_girl(Girl)

                $ Player.History.append("story")

                return

        $ Girl.change_face("smile")

        ch_s "When I was a child, I spent a lot of my time alone."
        ch_s "I was abandoned on the streets of Cairo, and had to fend for myself. . ."

        $ Girl.change_face("sadside")

        ch_s ". . . as a pickpocket."
        ch_s "Years later, I travelled south to Kenya, but for so much of my time, I had nobody that I could count on."

        $ Girl.change_face("smile")

        ch_s "Since I have come here, I have learned to value the strong bonds that I have with my teammates."

        if Player.Harem:
            if len(Player.Harem) >= 2:
                ch_s "And I know that you have been sharing your time with other girls,"
            else:
                ch_s "And I know that you have been sharing your time with [Player.Harem[0].name],"

            if Approvalcheck(Girl, 1500):
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 70, 2)

                ch_s ". . . but I can accept that."
            else:
                ch_s ". . . and we can discuss that. . ."

        $ Girl.change_face("sly")

        ch_s "I just want to know that you are there for me too."

        menu:
            extend ""
            "Of course I am.":
                $ Girl.change_face("smile")
                $ Girl.change_stat("love", 90, 7)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 70, 2)

                ch_s "That is a relief to hear."
            "I'm not big on commitment. . .":
                $ Girl.change_face("sadside")
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 60, 5)
                $ Girl.change_stat("inhibition", 70, -2)

                ch_s ". . . that is unfortunate."

                $ Girl.change_face("sad")

                ch_s "Let me know if you should reconsider then."

                call remove_girl(Girl)

                $ line = 0

                return
            "Well, I guess. . .":
                $ Girl.change_face("sadside")
                $ Girl.change_stat("love", 90, -3)
                $ Girl.change_stat("obedience", 60, 1)
                $ Girl.change_stat("inhibition", 70, -2)

                ch_s "That is. . . not exactly the answer I was looking for. . ."

        if Player.Harem:
            if Approvalcheck(Girl, 1500):
                $ Girl.change_face("sly",Eyes="side")
                $ Girl.change_stat("obedience", 80, 5)
                $ Girl.change_stat("inhibition", 80, 5)

                ch_s "I would be happy to join your little \"harem.\""

                $ Girl.change_face("sly")

                ch_s "If you'll have me."
            else:
                ch_s "I would prefer to be your one and only. . ."
                menu:
                    extend ""
                    "I could break up with them. . ." if len(Player.Harem) >= 2:
                        $ Girl.change_face("smile")
                        $ Girl.change_stat("love", 90, 10)
                        $ Girl.change_stat("obedience", 60, 5)
                        $ Girl.change_stat("inhibition", 70, 5)

                        ch_s "Excellent!"
                        ch_s "Do let them down gently though. . ."

                        return
                    "I could break up with her. . ." if len(Player.Harem) == 1:
                        $ Girl.change_face("smile")
                        $ Girl.change_stat("love", 90, 10)
                        $ Girl.change_stat("obedience", 60, 5)
                        $ Girl.change_stat("inhibition", 70, 5)

                        ch_s "Excellent!"
                        ch_s "Do let her down gently though. . ."

                        return
                    "I can't do that.":
                        $ Girl.change_face("sadside")
                        $ Girl.change_stat("love", 90, -5)
                        $ Girl.change_stat("obedience", 60, 5)
                        $ Girl.change_stat("obedience", 80, 5)
                        $ Girl.change_stat("inhibition", 70, -3)

                        ch_s ". . .oh."
                        ch_s "Well that is a disappointment."

                        if not Approvalcheck(Girl, 1000):
                            ch_s "I suppose that will be all then."

                            $ Girl.Event[5] = 20

                            call remove_girl(Girl)

                            $ line = 0

                            return
                        else:
                            $ Girl.change_stat("obedience", 80, 5)
                            $ Girl.change_stat("inhibition", 60, 3)
                            $ Girl.change_stat("inhibition", 70, 2)

                            ch_s ". . . I suppose that I could accept this. . . arrangement."
            menu:
                extend ""
                "I would love that!" if "StormYes" in Player.Traits:
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("inhibition", 70, 5)

                    ch_s "Excellent!"
                "I would love that. . . but. . ." if "StormYes" not in Player.Traits:
                    $ Girl.change_face("confused")
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 60, 5)

                    ch_s ". . . but?"

                    if len(Player.Harem) >= 2:
                        ch_p "The others weren't into that. . ."
                    else:
                        ch_p "[Player.Harem[0].name] wasn't into that. . ."

                    $ Girl.change_face("sadside")

                    ch_s ". . .oh."
                    ch_s "Well that is a disappointment."
                    ch_s "Let me know if the situation. . . clears up."

                    $ Girl.Event[5] = 20

                    call remove_girl(Girl)

                    $ line = 0

                    return
                "No thanks.":
                    $ Girl.change_face("sadside")
                    $ Girl.change_stat("love", 90, -25)
                    $ Girl.change_stat("obedience", 60, 10)

                    ch_s ". . .oh."
                    ch_s "Very well then."
                    ch_s "I will take no more of your time."

                    call remove_girl(Girl)

                    $ line = 0

                    return
        else:
            ch_s "So would you mind if I considered you my. . . \"boyfriend?\""
            menu:
                extend ""
                "I'd love that!":
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("inhibition", 70, 5)
                    $ Girl.change_face("smile")
                    ch_s "Excellent!"
                "I'd rather you didn't.":
                    $ Girl.change_stat("love", 90, -20)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("obedience", 70, 5)
                    $ Girl.change_face("sadside")

                    ch_s ". . .oh."
                    ch_s "Well that is a disappointment."

                    call remove_girl(Girl)

                    $ line = 0

                    return
                "Suit yourself.":
                    $ Girl.change_stat("love", 90, -5)

                    if Approvalcheck(Girl, 1000):
                        $ Girl.change_face("confused")
                        $ Girl.change_stat("obedience", 50, 5)
                        $ Girl.change_stat("obedience", 80, 5)

                        ch_s ". . .very well then. I shall do that. . ."
                    else:
                        $ Girl.change_face("sadside")
                        $ Girl.change_stat("obedience", 60, 5)

                        ch_s ". . . that was not the reaction I had expected. . ."
                        ch_s "Perhaps I should give this further consideration. . ."

                        call remove_girl(Girl)

                        $ line = 0

                        return

    if not simulation:
        $ Player.Harem.append(Girl)

        if Girl == RogueX:
            if "RogueYes" in Player.Traits:
                $ Player.Traits.remove("RogueYes")
        elif Girl == KittyX:
            if "KittyYes" in Player.Traits:
                $ Player.Traits.remove("KittyYes")
        elif Girl == EmmaX:
            if "EmmaYes" in Player.Traits:
                $ Player.Traits.remove("EmmaYes")
        elif Girl == LauraX:
            if "LauraYes" in Player.Traits:
                $ Player.Traits.remove("LauraYes")
        elif Girl == StormX:
            if "StormYes" in Player.Traits:
                    $ Player.Traits.remove("StormYes")

        call Harem_Initiation

    $ Girl.change_face("sexy")

    if Girl == RogueX:
        ch_r "Now, . . . boyfriend. . . how would you like to celebrate?"
    elif Girl == KittyX:
        ch_k "Now. . . boyfriend. . . how about you and I[Girl.like]celebrate, huh?"
    elif Girl == EmmaX:
        ch_e "So then. . . how would you like to celebrate?"
    elif Girl == LauraX:
        $ Girl.change_stat("love", 200, 3)
        $ Girl.change_stat("obedience", 80, 3)
        $ Girl.change_stat("inhibition", 80, 1)
        $ Girl.change_stat("lust", 80, 1)
        $ Girl.change_face("sly",1)

        ch_l "So, did you have any plans for the next few minutes? . ."

    if simulation:
        return 1

    $ temp_modifier = 10

    call girl_sex_menu(Girl)

    $ temp_modifier = 0

    return

label girl_boyfriend_jerk_ending:
    $ Girl.change_face("angry", 1)

    if Player.focused_Girl == RogueX:
        ch_r "Well fine!"

        $ Count = (20*Player.focused_Girl.Event[5])
    elif Player.focused_Girl == KittyX:
        ch_k "Fine![KittyX.Like]. . .be that way!"
    elif Player.focused_Girl == EmmaX:
        ch_e "Well! Suit yourself."

    $ Player.focused_Girl.change_stat("obedience", 50, 40)

    if Player.focused_Girl.Event[5] != 20:
        $ Player.focused_Girl.change_stat("obedience", 200, (20*Player.focused_Girl.Event[5]))
    if 20 > Player.focused_Girl.Event[5] >= 3:
        $ Player.focused_Girl.change_face("sad")

        if Player.focused_Girl == RogueX:
            ch_r "Hrmph. I don't care what you want, we're dating. Deal with it."
            ch_r "Now I need some alone time though."
        elif Player.focused_Girl == KittyX:
            ch_k "Yeah? Well. . .[Player.focused_Girl.like]I don’t care what you want! We’re dating! Deal."
            ch_k "I. . .uhm. . .think I need to[Player.focused_Girl.like]be alone for a little while."
        elif Player.focused_Girl == EmmaX:
            ch_e "You know, I'm tired of caring what you think about the matter."
            ch_e "I'm doing to consider us a couple whether you approve or not."
            ch_e "And with that, adieu."

        if simulation:
            return 1

        $ Player.focused_Girl.Petnames.append("boyfriend")

        $ Achievements.append("I am not your Boyfriend!")

        $ bg_current = "bg_player"

        call remove_girl(Player.focused_Girl)
        call set_the_scene
        $ renpy.pop_call()
        jump Player_Room

        return

    if Player.focused_Girl.Event[5] > 1:
        if Player.focused_Girl == RogueX:
            ch_r "I don't know why I keep asking, I should know you haven't changed."
        elif Player.focused_Girl == KittyX:
            ch_k "It was such a mistake asking you again.  You’re[KittyX.like]still such a jerk!"
        elif Player.focused_Girl == EmmaX:
            ch_e "It was such a mistake asking you again.  You still need to mature."

    if Player.focused_Girl.Event[5] != 20:
        $ Player.focused_Girl.change_stat("love", 200, -(50*Player.focused_Girl.Event[5]))
    else:
        $ Player.focused_Girl.change_stat("love", 200, -50)

    if bg_current == Player.focused_Girl.Home:
        if Player.focused_Girl == RogueX:
            ch_r "Jerk! Out!"
        elif Player.focused_Girl == KittyX:
            ch_k "Get out, you big jerk!"
        elif Player.focused_Girl == EmmaX:
            ch_e "Get away from me."

        $ bg_current = "bg_player"
        call remove_girl(Player.focused_Girl)
        call set_the_scene
        $ renpy.pop_call()
        jump Player_Room
    else:
        "[Player.focused_Girl.name] storms off."

        call remove_girl(Player.focused_Girl)
        call set_the_scene
        $ renpy.pop_call()

    if simulation:
        return 1

label girl_daddy(Girl):
    $ Girl.daily_history.append("relationship")

    if Girl != JeanX:
        $ Girl.DrainWord("asked meet")

    call shift_focus(Girl)
    call set_the_scene

    if Girl == RogueX:
        ch_r ". . ."
    elif Girl == KittyX:
        ch_k ". . ."
    elif Girl == EmmaX:
        ch_e ". . ."
    elif Girl == LauraX:
        ch_l ". . ."
    elif Girl == JeanX:
        ch_j ". . ."
    elif Girl == StormX:
        ch_s ". . ."

        $ line = 0
        $ Options = all_Girls[:]

        while Options:
            if "daddy" == Options[0].Petname:
                $ line = 2
            elif "daddy" in Options[0].Petnames:
                $ line = 1 if not line else line

            $ Options.remove(Options[0])
    elif Girl == JubesX:
        ch_v ". . ."

    if Girl in Player.Harem:
        if Girl == RogueX:
            ch_r "You know, even though we've been dating,"
        elif Girl == KittyX:
            ch_k "Hey, so[KittyX.like]we've been dating,"
        elif Girl == EmmaX:
            ch_e "We have been dating a while, [EmmaX.Petname],"
        elif Girl == LauraX:
            ch_l "So we've been dating a while yeah?"
        elif Girl == JeanX:
            ch_j "Ok, so I know we're dating. . ."
        elif Girl == StormX:
            ch_s "I have been talking with the other girls. . ."
        elif Girl == JubesX:
            ch_v "So we've been dating a while yeah?"
    else:
        if Girl == RogueX:
            ch_r "Even though we've been hanging out,"
        elif Girl == KittyX:
            ch_k "Hey, so[KittyX.like]we've been hanging out,"
        elif Girl == EmmaX:
            ch_e "We have been enjoying ourselves,"
        elif Girl == LauraX:
            ch_l "This thing we've got, pretty fun, right?"
        elif Girl == JeanX:
            ch_j "You. . . like me, right?"
        elif Girl == StormX:
            ch_s "I have heard something among the students. . ."
        elif Girl == JubesX:
            ch_v "This thing we've got, pretty fun, right?"

    if Girl != StormX:
        if Girl.love > Girl.obedience and Girl.love > Girl.inhibition:
            if Girl == RogueX:
                ch_r "and you're really sweet to me. . ."
            elif Girl == KittyX:
                ch_k "and you're so sweet. . ."
            elif Girl == EmmaX:
                ch_e "and you certainly are sweet. . ."
            elif Girl == LauraX:
                ch_l "and you've been really kind to me. . ."
            elif Girl == JeanX:
                ch_j "and I've really been warming up to this. . ."
            elif Girl == JubesX:
                ch_v "and you've been really kind to me. . ."
        elif Girl.obedience > Girl.inhibition:
            if Girl == RogueX:
                ch_r "and you know what I need. . ."
            elif Girl == KittyX:
                ch_k "and you give me what I need. . ."
            elif Girl == EmmaX:
                ch_e "and you know how to keep me interested. . ."
            elif Girl == LauraX:
                ch_l "and you've been a good influence. . ."
            elif Girl == JeanX:
                ch_j "I. . . \"respect\" you? . ."
            elif Girl == JubesX:
                ch_v "and you've been a good influence. . ."
        else:
            if Girl == RogueX:
                ch_r "and I've really been spreading my wings. . ."
            elif Girl == KittyX:
                ch_k "and I've been trying out new things. . ."
            elif Girl == EmmaX:
                ch_e "and I've been. . . exploring. . ."
            elif Girl == LauraX:
                ch_l "like, really fun. . ."
            elif Girl == JeanX:
                ch_j "and this is fun. . ."
            elif Girl == JubesX:
                ch_v "like, really fun. . ."

        if Girl == RogueX:
            ch_r "So I was thinking, could I call you \"daddy?\""
        elif Girl == KittyX:
            ch_k "So[KittyX.like]I was thinking, could I call you. . . \"daddy?\""
        elif Girl == EmmaX:
            ch_e "I was thinking, would you mind if I call you \"daddy?\""
        elif Girl == LauraX:
            ch_l "So I've been thinking, would you want to be called. . ."
            ch_l "\"daddy?\""
        elif Girl == JeanX:
            ch_j "I've been thinking, you know what would be totally hot? . ."
            ch_j "What if I called you. . . \"daddy?\""
        elif Girl == JubesX:
            ch_v "So I've been thinking, would you want to be called. . ."
            ch_v "\"daddy?\""

        menu:
            extend ""
            "Ok, go right ahead?":
                $ Girl.change_face("smile")
                $ Girl.change_stat("obedience", 60, 10)
                $ Girl.change_stat("inhibition", 80, 30)

                if Girl in [RogueX, EmmaX, LauraX, JeanX, JubesX]:
                    $ Girl.change_stat("love", 90, 20)
                elif Girl in [KittyX]:
                    $ Girl.change_stat("love", 90, 25)

                if Girl == RogueX:
                    ch_r "Squee!"
                elif Girl == KittyX:
                    ch_r "Great!"
                elif Girl == EmmaX:
                    ch_e "Excellent."
                elif Girl == LauraX:
                    ch_l "Cool."
                elif Girl == JeanX:
                    ch_j "Cool."
                elif Girl == JubesX:
                    ch_v "Cool."

                $ Girl.Petname = "daddy"
            "What do you mean by that?":
                $ Girl.change_face("bemused")

                if Girl == RogueX:
                    ch_r "I just sort of get turned on by it, you know, being your baby girl. . ."
                    ch_r "I'd like to call you that."
                elif Girl == KittyX:
                    ch_k "I don't know, it'd kinda be hot, being your baby girl. . ."
                    ch_k "Could'ya call me that?"
                elif Girl == EmmaX:
                    ch_e "I just find it to be a turn-on, being your baby girl. . ."
                    ch_e "I'd prefer to call you that sometimes."
                elif Girl == LauraX:
                    ch_l "I don't know, I've had some shitty father figures. . ."
                    ch_l "I just. . ."
                    if Girl.love > Girl.obedience and Girl.love > Girl.inhibition:
                        ch_l "I think you could do better. . ."
                    elif Girl.obedience > Girl.inhibition:
                        ch_l "you've really been assertive. . ."
                    else:
                        ch_l "wouldn't it be kinky?"
                elif Girl == JeanX:
                    ch_j "It's just kinda kinky, right. . ."
                    ch_j "\"Daddy?\""
                elif Girl == JubesX:
                    ch_v "I don't know, I've had some shitty father figures. . ."
                    ch_v "I just. . ."
                    if Girl.love > Girl.obedience and Girl.love > Girl.inhibition:
                        ch_v "I think you could do better. . ."
                    elif Girl.obedience > Girl.inhibition:
                        ch_v "you've really been assertive. . ."
                    else:
                        ch_v "wouldn't it be kinky?"

                menu:
                    extend ""
                    "Sounds interesting, fine by me.":
                        $ Girl.change_face("smile")
                        $ Girl.change_stat("obedience", 60, 20)
                        $ Girl.change_stat("inhibition", 80, 25)

                        if Girl != KittyX:
                            $ Girl.change_stat("love", 90, 15)

                        if Girl == RogueX:
                            ch_r "Great! . . daddy."
                        elif Girl == KittyX:
                            $ Girl.change_stat("love", 90, 17)

                            ch_k "Nice! . . daddy."
                        elif Girl == EmmaX:
                            ch_e "Great!"

                            $ Girl.change_face("sly",2)

                            ch_e " . . . daddy."

                            $ Girl.change_face("sly",1)
                        elif Girl == LauraX:
                            ch_l "Great!"

                            $ Girl.change_face("sly",2)

                            ch_l " . . . daddy."

                            $ Girl.change_face("sly",1)
                        elif Girl == JeanX:
                            ch_j "Nice."

                            $ Girl.change_face("sly",2)

                            ch_j " . . . daddy."

                            $ Girl.change_face("sly",1)
                        elif Girl == JubesX:
                            ch_v "Great!"

                            $ Girl.change_face("sly",2)

                            ch_v " . . . daddy."

                            $ Girl.change_face("sly",1)

                        $ Girl.Petname = "daddy"
                    "Could you not, please?":
                        $ Girl.change_stat("obedience", 80, 40)
                        $ Girl.change_stat("inhibition", 80, 20)

                        if Girl != JeanX:
                            $ Girl.change_face("sad")

                        if Girl != KittyX:
                            $ Girl.change_stat("love", 90, 5)

                        if Girl == RogueX:
                            ch_r "   . . .   "
                            ch_r "Well, ok."
                        elif Girl == KittyX:
                            ch_k "   . . .   "
                            ch_k "Huh. K."
                        elif Girl == EmmaX:
                            ch_e "   . . .   "
                            ch_e "Well, ok."
                        elif Girl == LauraX:
                            ch_l "   . . .   "
                            ch_l "Well, ok."
                        elif Girl == JeanX:
                            $ Girl.change_face("angry", 2)

                            ch_j "   . . .   "
                            ch_j "Fine, be that way!"

                            $ Girl.change_face("angry", 1, Eyes = "side")
                        elif Girl == JubesX:
                            ch_v "   . . .   "
                            ch_v "Well, ok."
                    "No, that creeps me out." if Girl in [RogueX, KittyX]:
                        $ Girl.change_stat("obedience", 80, 45)
                        $ Girl.change_stat("inhibition", 70, 5)
                        $ Girl.change_face("angry")

                        if Girl in [RogueX]:
                            $ Girl.change_stat("love", 90, -10)
                        elif Girl in [KittyX]:
                            $ Girl.change_stat("love", 90, -15)

                        if Girl == RogueX:
                            ch_r "Hrmph."
                        elif Girl == KittyX:
                            ch_r "Booo."
                    "You've got some real daddy issues, huh?" if Girl in [EmmaX, LauraX, JeanX, JubesX]:
                        $ Girl.change_stat("love", 90, -15)
                        $ Girl.change_stat("obedience", 80, 45)
                        $ Girl.change_stat("inhibition", 70, 5)

                        if Girl != JeanX:
                            $ Girl.change_face("angry")

                        if Girl == EmmaX:
                            ch_e "Let's not get into it."
                        elif Girl == LauraX:
                            ch_l "Yes. . . I said that."
                        elif Girl == JeanX:
                            $ Girl.change_face("angry",2)

                            ch_j "Oh, whatever, like you know!"

                            $ Girl.change_face("angry",1,Eyes="side")
                        elif Girl == JubesX:
                            ch_j "Yes. . . I said that."
            "No, that creeps me out." if Girl in [RogueX, KittyX]:
                $ Girl.change_stat("obedience", 80, 40)
                $ Girl.change_stat("inhibition", 70, 10)
                $ Girl.change_face("angry")

                if Girl == RogueX:
                    $ Girl.change_stat("love", 90, -5)

                    ch_r "Hrmph."
                elif Girl == KittyX:
                    $ Girl.change_stat("love", 90, -10)

                    ch_r "Hrmph."
            "Aren't you a bit old for that?" if Girl in [EmmaX]:
                $ Girl.change_stat("love", 90, -15)
                $ Girl.change_stat("obedience", 80, 40)
                $ Girl.change_stat("inhibition", 70, 10)
                $ Girl.change_face("angry")

                if Girl == EmmaX:
                    ch_e "Perhaps this was a bad idea."
            "You've got some real daddy issues, uh?" if Girl in [LauraX, JeanX, JubesX]:
                $ Girl.change_stat("love", 90, -15)
                $ Girl.change_stat("obedience", 80, 45)
                $ Girl.change_stat("inhibition", 70, 5)

                if Girl != JeanX:
                    $ Girl.change_face("angry")

                if Girl == LauraX:
                    ch_l ". . . Probably."
                    ch_l "Never mind."
                elif Girl == JeanX:
                    $ Girl.change_face("angry",2)

                    ch_j "Oh, whatever, like you know!"

                    $ Girl.change_face("angry",1,Eyes="side")
                elif Girl == JubesX:
                    ch_v ". . . Probably."
                    ch_v "Never mind."
    else:
        if line:
            ch_s "Apparently you have some of them call you. . . \"daddy?\""
        else:
            ch_s "Apparently sometimes the woman in a relationship. . ."
            ch_s ". . . calls her partner. . . \"daddy?\""

        menu:
            extend ""
            "Yes?":
                ch_s "I thought as much. . ."
            "I don't know what you're talking about.":
                ch_s "I think it is just a term of endearment. . ."
                ch_s "Affectionate, but. . . submissive?"
            "Not really.":
                ch_s "Oh. Perhaps I misunderstood."

        $ line = 1

        while line:
            menu:
                extend ""
                "Did you want me to call you that?" if "callyouthat" not in Girl.recent_history:
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("inhibition", 90, 2)

                    ch_s ". . ."

                    $ Girl.change_stat("love", 95, 2)
                    $ Girl.change_stat("inhibition", 70, 1)

                    ch_s "I suppose that I did. . ."

                    $ Girl.recent_history.append("callyouthat")
                "I guess you could. . ." if "callyouthat" in Girl.recent_history or "whycare" in Girl.recent_history:
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 70, 1)

                    ch_s ". . ."

                    $ Girl.change_stat("love", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 3)

                    ch_s "Certainly. . . Daddy."

                    $ line = 0
                "Call me \"Daddy.\"":
                    $ Girl.change_stat("love", 90, 2)
                    $ Girl.change_stat("obedience", 80, 3)

                    ch_s ". . ."

                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("inhibition", 90, 2)
                    $ Girl.change_stat("lust", 90, 3)

                    ch_s "Certainly. . . Daddy."

                    $ line = 0
                "Why do you care?" if "whycare" not in Girl.recent_history:
                    $ Girl.change_stat("love", 90, 2)
                    $ Girl.change_stat("obedience", 80, -1)
                    $ Girl.change_stat("inhibition", 90, -1)

                    ch_s "Oh, well, I was thinking that I could. . ."

                    $ Girl.recent_history.append("whycare")
                "It's weird, right?":
                    $ Girl.change_stat("love", 90, -3)
                    $ Girl.change_stat("obedience", 90, -5)
                    $ Girl.change_stat("inhibition", 90, -15)

                    ch_s "Oh. . . "
                    ch_s ". . . I suppose that it is."
                    ch_s "Never mind. . ."

                    call remove_girl(Girl)

                    $ line = 0
                "I'd rather not." if "callyouthat" in Girl.recent_history or "whycare" in Girl.recent_history:
                    $ Girl.change_stat("love", 90, -2)
                    $ Girl.change_stat("obedience", 90, 3)
                    $ Girl.change_stat("inhibition", 90, -5)

                    ch_s "Oh. . . "
                    ch_s ". . . I suppose that is fine."
                    ch_s "Never mind. . ."

                    call remove_girl(Girl)

                    $ line = 0

    $ Girl.Petnames.append("daddy")

    return

label first_topless(Girl, silent = 0, temporary_line = 0): #rkeljsv
    if Girl.ChestNum() > 1 or Girl.OverNum() > 2 and not temporary_line:
        return

    if Girl.location != bg_current and "phonesex" not in Player.recent_history:
        return

    $ Girl.recent_history.append("topless")
    $ Girl.daily_history.append("topless")
    $ Girl.DrainWord("no_topless")
    $ Girl.SeenChest += 1

    if Girl.SeenChest > 1:
        return

    if Girl == RogueX:
        $ Girl.change_stat("inhibition", 70, 20)
    elif Girl in [KittyX, EmmaX, LauraX, JeanX]:
        $ Girl.change_stat("inhibition", 70, 15)

    if not silent:
        if Girl == RogueX:
            $ Girl.change_face("bemused", 1)

            "[Girl.name] looks a bit shy, and slowly lowers her hands from her chest."
            Girl.voice "Well, [Girl.Petname]? Like what you see?"

            $ disappointed_line = "Well, they aren't that bad. . ."
        elif Girl == KittyX:
            $ Girl.change_face("bemused", 2)

            "[Girl.name] looks a bit shy, and slowly lowers her hands from her chest."
            Girl.voice "[Girl.Like]what do you think?"

            $Girl.Blush = 1

            $ disapointed_line = "That's it?"
        elif Girl in [EmmaX, LauraX, JeanX, JubesX]:
            $ Girl.change_face("sly")

            "You get your first look at [Girl.name]'s bare chest."

            if Girl == EmmaX:
                Girl.voice "Well, [Girl.Petname]? Is it everything you dreamed?"
            elif Girl == LauraX:
                ch_l "So? What are you looking at?"
            elif Girl == JeanX:
                ch_j "So, pretty spectacular, right?"
            elif Girl == JubesX:
                ch_v "So. . . um. . . like what you see?"

            $ Girl.Blush = 1

            $ disappointed_line = "Huh, not what I was expecting. . ."

        menu:
            extend ""
            "Nod" if Girl in [RogueX]:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("inhibition", 70, 20)

                if Girl == RogueX:
                    $ Girl.change_face("smile")

                Girl.voice ". . ."

                $ Girl.change_stat("love", 40, 20)
            "lovely." if Girl in [KittyX]:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("inhibition", 70, 20)

                if Girl == KittyX:
                    $ Girl.change_face("smile", 2)

                Girl.voice ". . ."

                $ Girl.change_stat("love", 40, 20)

                if Girl == KittyX:
                    $ Girl.Blush = 1
            "Whatever." if Girl in [RogueX]:
                $ Girl.change_stat("love", 90, -30)
                $ Girl.change_stat("obedience", 50, 20)
                $ Girl.change_stat("inhibition", 70, -10)
                $ Girl.change_face("angry")

                if Girl == RogueX:
                    ch_r "Hmph!"

                $ Girl.change_stat("obedience", 70, 20)
            "Definitely, and more." if Girl in [EmmaX]:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("inhibition", 70, 20)
                $ Girl.change_face("smile",1)

                ch_e "I do aim to impress."

                $ Girl.change_stat("love", 40, 20)
                $ Girl.Blush = 0
            "Your tits? They look great." if Girl in [LauraX, JubesX]:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("inhibition", 70, 20)

                if Girl == LauraX:
                    $ Girl.change_face("sexy",1,Eyes="down")

                    ch_l "Huh. I mean I guess so. . ."

                    $ Girl.change_face("smile",0)
                elif Girl == JubesX:
                    $ Girl.change_face("smile",2)

                    pause 0.5

                    $ Girl.change_face("sexy",1,Eyes="down")

                    ch_v "Ah! Um. . . yeah, I guess. . ."

                    $ Girl.change_face("smile")

                $ Girl.change_stat("love", 40, 20)
            "Yeah, they look amazing." if Girl in [JeanX]:
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("inhibition", 200, 20)
                $ JeanX.change_face("sexy",1,Eyes="down")

                ch_j "Yeah, they are pretty tight. . ."

                $ JeanX.change_face("smile",0)
                $ JeanX.change_stat("obedience", 40, 20)
            ". . . [[stunned]]" if Girl in [EmmaX, LauraX, JeanX, JubesX]:
                if Girl == EmmaX:
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("inhibition", 70, 30)

                    ch_e "Yes, that would be the usual reaction."
                elif Girl in [LauraX, JubesX]:
                    $ Girl.change_stat("love", 90, 10)
                    $ Girl.change_stat("inhibition", 70, 10)

                    if Girl == LauraX:
                        ch_l "Cat got your tongue?"
                    elif Girl == JubesX:
                        ch_v "Oh, that's a \"hit.\""
                elif Girl == JeanX:
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("inhibition", 200, 10)

                    ch_j "Stunning, I know."

                $ Girl.change_stat("love", 40, 10)
            "[disappointed_line]":
                if Girl != JeanX:
                    $ Girl.change_stat("love", 90, -30)
                    $ Girl.change_stat("obedience", 60, 25)
                    $ Girl.change_stat("inhibition", 70, -15)
                    $ Girl.change_face("confused", 2)

                    if Girl == RogueX:
                        Girl.voice "Say what now?"
                    elif Girl == KittyX:
                        Girl.voice "What?"
                    elif Girl == EmmaX:
                        Girl.voice "What?"
                    elif Girl == LauraX:
                        ch_l "Huh?"
                    elif Girl == JubesX:
                        ch_v "Wha?"
                else:
                    $ Girl.change_stat("love", 90, 10)
                    $ Girl.change_stat("obedience", 40, 20)
                    $ Girl.change_stat("inhibition", 200, 20)
                    $ Girl.change_face("smile",0)

                    ch_j "Exactl-{w=0.3}{nw}"

                    $ Girl.change_stat("love", 90, -40)
                    $ Girl.change_stat("obedience", 60, 10)
                    $ Girl.change_stat("inhibition", 200, -15)
                    $ Girl.change_face("confused",2)

                    ch_j "Exactl- wait, what?"

                    $ temporary_line = 0

                menu:
                    "They're even better than I imagined!" if Girl in [EmmaX]:
                        $ Girl.change_stat("love", 90, 20)
                        $ Girl.change_stat("obedience", 60, -20)
                        $ Girl.change_stat("inhibition", 70, 20)
                        $ Girl.change_face("perplexed",1)

                        ch_e "Well, I suppose you managed to salvage that one. . ."
                    "They're really perky!" if Girl in [LauraX, JeanX, JubesX]:
                        if Girl in [LauraX, JubesX]:
                            $ Girl.change_stat("love", 90, 20)
                            $ Girl.change_stat("obedience", 60, -20)
                            $ Girl.change_stat("inhibition", 70, 20)
                            $ Girl.change_face("perplexed",1)

                            Girl.voice "Oh. Right. . ."
                        elif Girl == JeanX:
                            $ Girl.change_stat("love", 90, 10)
                            $ Girl.change_stat("obedience", 60, 10)
                            $ Girl.change_stat("inhibition", 200, 20)
                            $ Girl.change_face("perplexed",1)

                            ch_j "Oh. Of course. . ."
                    "I, um, no, they're great!":
                        $ Girl.change_face("angry", 2, Mouth = "smile")

                        if Girl != JeanX:
                            $ Girl.change_stat("inhibition", 70, 10)

                        if Girl == RogueX:
                            ch_r "Of couse they are!"
                        elif Girl == KittyX:
                            ch_k "Obviously!"
                        elif Girl == EmmaX:
                            ch_r "Of couse they are!"
                        elif Girl == LauraX:
                            ch_l "Why wouldn't they be?"
                        elif Girl == JeanX:
                            $ Girl.change_stat("obedience", 80, 20)

                            ch_j "Of course they are!"
                        elif Girl == JubesX:
                            ch_v ". . ."
                            ch_v "I -know- that, that's why I was confused?"
                    "[EmmaX.name]'s were a lot bigger, that's all." if Girl in [KittyX] and EmmaX.SeenChest:
                        $ temporary_line = EmmaX
                    "[StormX.name]'s were a lot bigger, that's all." if Girl in [RogueX, KittyX, LauraX, JeanX, JubesX] and StormX.SeenChest:
                        $ temporary_line = StormX
                    "[RogueX.name]'s were bigger, that's all." if Girl in [KittyX] and RogueX.SeenChest:
                        $ temporary_line = RogueX
                    "[EmmaX.name]'s were bigger, that's all." if Girl in [RogueX, KittyX, LauraX, JeanX, JubesX] and EmmaX.SeenChest:
                        $ temporary_line = EmmaX
                    "[LauraX.name]'s were bigger, that's all." if Girl in [KittyX] and LauraX.SeenChest:
                        $ temporary_line = LauraX
                    "[JeanX.name]'s were bigger, that's all." if Girl in [KittyX] and JeanX.SeenChest:
                        $ temporary_line = JeanX
                    "[StormX.name]'s were bigger, that's all." if Girl in [RogueX, KittyX, EmmaX, LauraX, JeanX, JubesX] and StormX.SeenChest:
                        $ temporary_line = StormX
                    "[RogueX.name]'s were nicer, that's all." if Girl in [LauraX, JeanX, JubesX] and RogueX.SeenChest:
                        $ temporary_line = RogueX
                    "[LauraX.name]'s were nicer, that's all." if Girl in [RogueX, JeanX, JubesX] and LauraX.SeenChest:
                        $ temporary_line = LauraX
                    "[JeanX.name]'s were nicer, that's all." if Girl in [RogueX, LauraX, JubesX] and JeanX.SeenChest:
                        $ temporary_line = JeanX
                    "[RogueX.name]'s were tighter, that's all." if Girl in [EmmaX, StormX] and RogueX.SeenChest:
                        $ temporary_line = RogueX
                    "[KittyX.name]'s were tighter, that's all." if Girl in [RogueX, EmmaX, LauraX, JeanX, StormX, JubesX] and KittyX.SeenChest:
                        $ temporary_line = KittyX
                    "[EmmaX.name]'s were tighter, that's all." if Girl in [StormX] and EmmaX.SeenChest:
                        $ temporary_line = EmmaX
                    "[LauraX.name]'s were tighter, that's all." if Girl in [RogueX, EmmaX, StormX] and LauraX.SeenChest:
                        $ temporary_line = LauraX
                    "[JeanX.name]'s were tighter, that's all." if Girl in [EmmaX, StormX] and JeanX.SeenChest:
                        $ temporary_line = JeanX

                if temporary_line:
                    $ Girl.change_face("angry")
                    $ Girl.Mouth = "surprised"

                    if Girl != JeanX:
                        $ Girl.change_stat("love", 90, -10)
                        $ Girl.change_stat("obedience", 80, 30)
                        $ Girl.change_stat("inhibition", 70, -25)
                    else:
                        $ Girl.change_stat("love", 50, -10)
                        $ Girl.change_stat("love", 90, -10)
                        $ Girl.change_stat("obedience", 50, 10)
                        $ Girl.change_stat("obedience", 80, 30)
                        $ Girl.change_stat("inhibition", 200, -15)

                    Girl.voice ". . ."

                    $ Girl.Mouth = "sad"

                    if temporary_line in [EmmaX, StormX]:
                        if Girl.GirlLikecheck(temporary_line) >= 800:
                            $ Girl.change_face("sly", 2, Eyes="side")
                            $ Girl.change_stat("obedience", 80, 5)

                            if Girl == RogueX:
                                ch_r "Well, I mean they would be quite the handful. . ."
                            elif Girl == KittyX:
                                ch_k "Yeah, like you just wanna shove your head into there. . ."
                            elif Girl == EmmaX:
                                ch_e "They are lovely, but. . ."
                            elif Girl == LauraX:
                                ch_l "They are kinda huge. . ."
                            elif Girl == JeanX:
                                ch_j "Well, they are. . . heavy. . ."
                            elif Girl == JubesX:
                                ch_v "Well they are really ginormous. . ."

                            $ Girl.GirlLikeUp(temporary_line, 20) # +20
                        elif Girl.GirlLikecheck(temporary_line) >= 700:
                            $ Girl.Eyes = "side"
                            $ Girl.change_stat("obedience", 80, 5)

                            if Girl == RogueX:
                                ch_r "I mean, I guess, if you like that kind of thing. . ."
                            elif Girl == KittyX:
                                ch_k "I mean, I guess, if you like that kind of thing. . ."
                            elif Girl == EmmaX:
                                ch_e "I don't know about that. . ."
                            elif Girl == LauraX:
                                ch_l "I guess that's true. . ."
                            elif Girl == JeanX:
                                ch_j "If you have a thing for udders. . ."
                            elif Girl == JubesX:
                                ch_v "Oh. Well I can't compete there. . ."
                        else:
                            $ Girl.GirlLikeUp(temporary_line, -50) # +20

                            $ temporary_line = "bad"
                    elif temporary_line == KittyX:
                        if Girl.GirlLikecheck(temporary_line) >= 800:
                            $ Girl.change_face("sly",2,Eyes="side")
                            $ Girl.change_stat("obedience", 80, 5)

                            if Girl = RogueX:
                                ch_r "They are kind of adorable. . ."
                            elif Girl == EmmaX:
                                ch_e "They are rather . . . pert. . ."
                            elif Girl == LauraX:
                                ch_l "She is very. . . streamlined. . ."
                            elif Girl == JeanX:
                                ch_j "She is very. . . cute. . ."
                            elif Girl == JubesX:
                                ch_v ". . . I guess they are really cute. . ."

                            $ Girl.GirlLikeUp(temporary_line, 20)
                        elif Girl.GirlLikecheck(temporary_line) >= 700:
                            $ Girl.Eyes = "side"
                            $ Girl.change_stat("obedience", 80, 5)

                            if Girl == RogueX:
                                ch_r "I mean, yeah, I guess. . ."
                            elif Girl == EmmaX:
                                ch_e "Well, for a child. . ."
                            elif Girl == LauraX:
                                ch_l "They are kinda. . . pointy. . ."
                            elif Girl == JeanX:
                                ch_j "If you have a thing for surf boards. . ."
                            elif Girl == JubesX:
                                ch_v "Ok, into that, uh? . ."
                        else:
                            $ Girl.GirlLikeUp(temporary_line, -50)

                            $ temporary_line = "bad"

                    if temporary_line == "bad":
                        $ Girl.change_stat("love", 90, -20)

                        if Girl == RogueX:
                            ch_r "Yeah, that's enough outta you, [Girl.Petname]."
                        elif Girl == KittyX:
                            ch_k "Well you sure know how to ruin a mood."
                        elif Girl == EmmaX:
                            ch_e "I think you've seen enough for now, [EmmaX.Petname]."
                        elif Girl == LauraX:
                            ch_l "Still kinda rude though."
                        elif Girl == JeanX:
                            ch_j "Still, inappropriate on your part!"
                        elif Girl == JubesX:
                            ch_v "Still, you don't just -say- something like that!"

                        $ Girl.OutfitChange()

                        $ Girl.recent_history.append("no_topless")
                        $ Girl.daily_history.append("no_topless")
                        $ Girl.recent_history.append("angry")
                        $ Girl.daily_history.append("angry")
    else:
        $ Girl.AddWord(1,0,0,0,"topless") #$ Girl.History.append("topless")

        if Approvalcheck(Girl, 800) and not Girl.Forced:
            $ Girl.change_stat("inhibition", 70, 5)

            if Girl in [RogueX, EmmaX]:
                $ Girl.change_stat("obedience", 70, 5)
            elif Girl in [KittyX, LauraX, JubesX]:
                $ Girl.change_stat("obedience", 70, 10)
            elif Girl == JeanX:
                $ Girl.change_stat("love", 70, 5)
                $ Girl.change_stat("obedience", 70, 25)
                $ Girl.change_stat("inhibition", 70, 15)
        else:
            if Girl == EmmaX:
                $ Girl.change_stat("love", 90, -5)

            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("inhibition", 70, -5)
            $ Girl.change_face("angry")

            if Girl in [RogueX, EmmaX]:
                $ Girl.change_stat("obedience", 70, 15)
            elif Girl in [KittyX, LauraX]:
                $ Girl.change_stat("obedience", 70, 20)
            elif Girl == JeanX:
                $ Girl.change_stat("love", 90, -35)
                $ Girl.change_stat("inhibition", 200, -15)
                $ Girl.change_stat("obedience", 70, 40)
            elif Girl == JubesX:
                $ Girl.change_stat("obedience", 70, 10)
    return

label first_bottomless(Girl, silent = 0): #rkeljsv
    if Girl.PantiesNum() > 1 or Girl.PantsNum() > 2 or Girl.HoseNum() > 9:
        return

    if Girl.location != bg_current and "phonesex" not in Player.recent_history:
        return

    $ Girl.recent_history.append("bottomless")
    $ Girl.daily_history.append("bottomless")
    $ Girl.DrainWord("no_bottomless")

    $ Girl.SeenPussy += 1

    if Girl.SeenPussy > 1:
        return

    $ Girl.change_stat("inhibition", 80, 40)

    if not silent:
        $ Girl.change_face("bemused", 1)

        "[Girl.name] shyly moves her hands aside, revealing her pussy."

        menu:
            ch_r "Well, [Girl.Petname]? Was it worth the wait?"
            "lovely. . .":
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("inhibition", 60, 30)
                    $ Girl.change_face("smile")

                    ch_r ". . ."

                    $ Girl.change_stat("love", 40, 20)
            "I suppose.":
                    $ Girl.change_stat("love", 90, -30)
                    $ Girl.change_stat("obedience", 50, 20)
                    $ Girl.change_stat("inhibition", 70, -20)
                    $ Girl.change_face("angry")

                    ch_r ". . ."

                    $ Girl.change_stat("obedience", 70, 30)
    else:
        $ Girl.AddWord(1,0,0,0,"bottomless") #$ Girl.History.append("bottomless")

        if Approvalcheck(Girl, 500):
            $ Girl.change_stat("inhibition", 60, 30)
        else:
            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("inhibition", 70, -5)
            $ Girl.change_face("angry")
            $ Girl.change_stat("obedience", 70, 15)
    return

label Kitty_First_Bottomless(Silent = 0):
    if KittyX.PantiesNum() > 1 or KittyX.PantsNum() > 2 or KittyX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if KittyX.location != bg_current and "phonesex" not in Player.recent_history:
            return
    $ KittyX.recent_history.append("bottomless")
    $ KittyX.daily_history.append("bottomless")
    $ KittyX.DrainWord("no_bottomless")
    $ KittyX.SeenPussy += 1
    if KittyX.SeenPussy > 1:
            return                  #ends portion if you've already seen them

    $ KittyX.change_stat("inhibition", 80, 30)
    $ KittyX.change_stat("obedience", 70, 10)
    if not Silent:
        $ KittyX.change_face("bemused", 1)
        "[KittyX.name] shyly moves her hands aside, revealing her pussy."
        menu Kitty_First_BMenu:
            extend ""
            "lovely. . .":
                    $ KittyX.change_stat("love", 90, 20)
                    $ KittyX.change_stat("inhibition", 60, 25)
                    $ KittyX.change_face("smile")
                    ch_k ". . ."
                    $ KittyX.change_stat("love", 40, 20)
            "Now {i}that's{/i} the \"Kitty\" I wanted to see.":
                    $ KittyX.change_stat("love", 40, 25)
                    $ KittyX.change_stat("inhibition", 60, 30)
                    $ KittyX.change_face("perplexed", 2)
                    ch_k "[[snort]"
                    $ KittyX.change_stat("love", 90, 25)
                    $ KittyX.Blush = 1
            "Pretty messy down there." if KittyX.Pubes:
                    $ KittyX.change_face("surprised",2)
                    ch_k "!"
                    if Approvalcheck(KittyX, 800, "LO"):
                            $ KittyX.change_face("bemused",1)
                            $ KittyX.change_stat("obedience", 50, 30)
                            $ KittyX.change_stat("inhibition", 60, 25)
                            ch_k "I guess I could trim it up a bit. . ."
                            $ KittyX.Todo.append("shave")
                    else:
                            $ KittyX.change_face("angry",1)
                            $ KittyX.change_stat("love", 40, -20)
                            $ KittyX.change_stat("obedience", 50, 25)
                            $ KittyX.change_stat("inhibition", 60, -5)
                            ch_k "Well[KittyX.like]sorry I don't keep it baby soft!"
            "I've seen better.":
                    $ KittyX.change_stat("love", 90, -30)
                    $ KittyX.change_stat("obedience", 50, 25)
                    $ KittyX.change_stat("inhibition", 70, -30)
                    $ KittyX.change_face("angry")
                    ch_k ". . ."
                    $ KittyX.change_stat("obedience", 70, 35)
    else:
            $ KittyX.AddWord(1,0,0,0,"bottomless") #$ KittyX.History.append("bottomless")
            if Approvalcheck(KittyX, 800) and not KittyX.Forced:
                    $ KittyX.change_stat("inhibition", 60, 15)
                    $ KittyX.change_stat("obedience", 70, 10)
            else:
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("inhibition", 70, -5)
                    $ KittyX.change_face("angry")
                    $ KittyX.change_stat("obedience", 70, 20)
    return

label Emma_First_Bottomless(Silent = 0):
    if EmmaX.PantiesNum() > 1 or EmmaX.PantsNum() > 2 or EmmaX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if EmmaX.location != bg_current and "phonesex" not in Player.recent_history:
            return
    $ EmmaX.recent_history.append("bottomless")
    $ EmmaX.daily_history.append("bottomless")
    $ EmmaX.DrainWord("no_bottomless")
    $ EmmaX.SeenPussy += 1
    if EmmaX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ EmmaX.change_stat("inhibition", 80, 30)
    $ EmmaX.change_stat("obedience", 70, 10)
    if not Silent:
        $ EmmaX.change_face("sly")
        "You find yourself staring at [EmmaX.name]'s bare pussy."
        menu Emma_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ EmmaX.change_stat("love", 90, 20)
                    $ EmmaX.change_stat("inhibition", 60, 25)
                    $ EmmaX.change_face("smile")
                    ch_e "I'm aware. . . "
                    $ EmmaX.change_stat("love", 40, 20)
            "I see you keep it smooth down there." if not EmmaX.Pubes:
                $ EmmaX.change_face("confused",1)
                ch_e "Yes?"
                if Approvalcheck(EmmaX, 700, "LO"):
                        $ EmmaX.change_face("bemused")
                        menu:
                            ch_e "Do you prefer more fuzz?"
                            "Yes":
                                if Approvalcheck(EmmaX, 900, "LO"):
                                        $ EmmaX.change_stat("obedience", 50, 30)
                                        $ EmmaX.change_stat("inhibition", 60, 25)
                                        ch_e "I suppose I could let it go. . ."
                                        $ EmmaX.Todo.append("pubes")
                                else:
                                        $ EmmaX.change_face("normal")
                                        ch_e "Well that's a pity."
                            "Up to you, I guess.":
                                        $ EmmaX.change_stat("love", 80, 10)
                                        ch_e "I'm glad you agree."
                            "No, leave it that way.":
                                        if Approvalcheck(EmmaX, 900, "LO"):
                                                $ EmmaX.change_face("sly")
                                                $ EmmaX.change_stat("love", 80, 10)
                                        else:
                                                $ EmmaX.change_face("angry",Mouth="normal")
                                        $ EmmaX.change_stat("inhibition", 60, 25)
                                        ch_e "I'm glad I have your. . . permission."
                                        $ EmmaX.Brows = "normal"
                else:
                        $ EmmaX.change_face("angry",1)
                        $ EmmaX.change_stat("love", 40, -20)
                        $ EmmaX.change_stat("obedience", 50, 25)
                        $ EmmaX.change_stat("inhibition", 60, -5)
                        ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":
                $ EmmaX.change_stat("love", 90, -30)
                $ EmmaX.change_stat("obedience", 50, 25)
                $ EmmaX.change_stat("inhibition", 70, -30)
                $ EmmaX.change_face("angry",2)
                if not EmmaX.Forced and not Approvalcheck(EmmaX, 900, "LO"):
                        $ EmmaX.recent_history.append("angry")
                        $ EmmaX.daily_history.append("angry")
                        $ EmmaX.change_stat("obedience", 70, 25)
                ch_e "You will regret that remark. . ."
    else:

        $ EmmaX.AddWord(1,0,0,0,"bottomless") #$ EmmaX.History.append("bottomless")
        if Approvalcheck(EmmaX, 800) and not EmmaX.Forced:
                $ EmmaX.change_stat("inhibition", 60, 5)
                $ EmmaX.change_stat("obedience", 70, 10)
        else:
                $ EmmaX.change_stat("love", 90, -10)
                $ EmmaX.change_stat("inhibition", 70, -5)
                $ EmmaX.change_face("angry")
                $ EmmaX.change_stat("obedience", 70, 15)
    return

label Laura_First_Bottomless(Silent = 0):
    if LauraX.PantiesNum() > 1 or LauraX.PantsNum() > 2 or LauraX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if LauraX.location != bg_current and "phonesex" not in Player.recent_history:
            return
    $ LauraX.recent_history.append("bottomless")
    $ LauraX.daily_history.append("bottomless")
    $ LauraX.DrainWord("no_bottomless")
    $ LauraX.SeenPussy += 1
    if LauraX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ LauraX.change_stat("inhibition", 80, 30)
    $ LauraX.change_stat("obedience", 70, 10)
    if not Silent:
        $ LauraX.change_face("sly")
        if LauraX.Pubes:
                "You find yourself staring at [LauraX.name]'s furry pussy."
        else:
                "You find yourself staring at [LauraX.name]'s bare pussy."
        menu Laura_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ LauraX.change_stat("love", 90, 20)
                    $ LauraX.change_stat("inhibition", 60, 25)
                    $ LauraX.change_face("smile")
                    ch_l "You think?"
                    ch_l "Yeah, I like it too. . . "
                    $ LauraX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if LauraX.Pubes:
                $ LauraX.change_face("confused",1)
                ch_l "Well. . . yeah."
                if Approvalcheck(LauraX, 700, "LO"):
                    $ LauraX.change_face("bemused")
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if Approvalcheck(LauraX, 900, "LO"):
                                    $ LauraX.change_stat("obedience", 50, 30)
                                    $ LauraX.change_stat("inhibition", 60, 25)
                                    ch_l "I guess I could. . ."
                                    $ LauraX.Todo.append("pubes")
                            else:
                                    $ LauraX.change_face("normal")
                                    ch_l "Seems like a waste of time."
                                    ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                                    $ LauraX.change_stat("love", 80, 10)
                                    ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":
                                    if Approvalcheck(LauraX, 900, "LO"):
                                            $ LauraX.change_face("sly")
                                            $ LauraX.change_stat("love", 80, 10)
                                    else:
                                            $ LauraX.change_face("angry",Mouth="normal")
                                    $ LauraX.change_stat("inhibition", 60, 25)
                                    ch_l "Right."
                                    $ LauraX.Brows = "normal"
                else:
                        $ LauraX.change_face("angry",1)
                        $ LauraX.change_stat("love", 40, -20)
                        $ LauraX.change_stat("obedience", 50, 25)
                        $ LauraX.change_stat("inhibition", 60, -5)
                        ch_l "I mean, what else would I do?"
            "What a mess.":
                    $ LauraX.change_stat("love", 90, -30)
                    $ LauraX.change_stat("obedience", 50, 25)
                    $ LauraX.change_stat("inhibition", 70, -30)
                    $ LauraX.change_face("angry",2)
                    if not LauraX.Forced and not Approvalcheck(LauraX, 900, "LO"):
                            $ LauraX.recent_history.append("angry")
                            $ LauraX.daily_history.append("angry")
                            $ LauraX.change_stat("obedience", 70, 25)
                    ch_l "I'll make you a mess. . ."
    else:
        $ LauraX.AddWord(1,0,0,0,"bottomless") #$ LauraX.History.append("bottomless")
        if Approvalcheck(LauraX, 800) and not LauraX.Forced:
                $ LauraX.change_stat("inhibition", 60, 5)
                $ LauraX.change_stat("obedience", 70, 10)
        else:
                $ LauraX.change_stat("love", 90, -5)
                $ LauraX.change_stat("inhibition", 70, -5)
                $ LauraX.change_face("angry")
                $ LauraX.change_stat("obedience", 70, 15)
    return

label Jean_First_Bottomless(Silent = 0):
    if JeanX.PantiesNum() > 1 or JeanX.PantsNum() > 2 or JeanX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if JeanX.location != bg_current and "phonesex" not in Player.recent_history:
            return
    $ JeanX.recent_history.append("bottomless")
    $ JeanX.daily_history.append("bottomless")
    $ JeanX.DrainWord("no_bottomless")
    $ JeanX.SeenPussy += 1
    if JeanX.SeenPussy > 1:
            return                  #ends portion if you've already seen them

    $ JeanX.change_stat("inhibition", 200, 30)
    $ JeanX.change_stat("obedience", 90, 10)
    if not Silent:
        $ JeanX.change_face("sly")
        if JeanX.Pubes:
                "You find yourself staring at [JeanX.name]'s fuzzy pussy."
        else:
                "You find yourself staring at [JeanX.name]'s bare pussy."
        menu Jean_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ JeanX.change_stat("love", 90, 20)
                    $ JeanX.change_stat("inhibition", 200, 25)
                    $ JeanX.change_face("smile")
                    ch_j "Right?"
                    $ JeanX.change_stat("love", 40, 20)
            "I see you got a fire crotch down there." if JeanX.Pubes:
                $ JeanX.change_face("confused",1)
                ch_j "Well. . . yeah."
                if Approvalcheck(JeanX, 700, "LO"):
                    $ JeanX.change_face("bemused")
                    menu:
                        ch_j "Do you prefer it smooth?"
                        "Yes":
                            if Approvalcheck(JeanX, 900, "LO"):
                                    $ JeanX.change_stat("obedience", 90, 30)
                                    $ JeanX.change_stat("inhibition", 200, 25)
                                    ch_j "Hmm, I guess. . ."
                                    $ JeanX.Todo.append("pubes")
                            else:
                                    $ JeanX.change_face("normal")
                                    ch_j "Not worth the hassle."
                        "Up to you, I guess.":
                                    $ JeanX.change_stat("love", 80, 10)
                                    ch_j "Of course it is."
                        "No, leave it that way.":
                                    if Approvalcheck(JeanX, 900, "LO"):
                                            $ JeanX.change_face("sly")
                                            $ JeanX.change_stat("love", 80, 10)
                                    else:
                                            $ JeanX.change_face("angry",Mouth="normal")
                                    $ JeanX.change_stat("inhibition", 200, 25)
                                    ch_j "Of course."
                                    $ JeanX.Brows = "normal"
                else:
                        $ JeanX.change_face("angry",1)
                        $ JeanX.change_stat("love", 40, -20)
                        $ JeanX.change_stat("obedience", 90, 25)
                        $ JeanX.change_stat("inhibition", 200, -5)
                        ch_j "I didn't really feel like waxing it."
            "What a mess." if JeanX.Pubes:
                    $ JeanX.change_stat("love", 90, -30)
                    $ JeanX.change_stat("obedience", 90, 25)
                    $ JeanX.change_stat("inhibition", 200, -30)
                    $ JeanX.change_face("angry",2)
                    if not JeanX.Forced and not Approvalcheck(JeanX, 900, "LO"):
                            $ JeanX.recent_history.append("angry")
                            $ JeanX.daily_history.append("angry")
                            $ JeanX.change_stat("obedience", 90, 25)
                    ch_j "Oh, so it's not baby-smooth like [EmmaX.name]'s?"
            "Eh, I've seen better" if not JeanX.Pubes:
                    $ JeanX.change_stat("love", 90, -30)
                    $ JeanX.change_stat("obedience", 90, 25)
                    $ JeanX.change_stat("inhibition", 200, -30)
                    $ JeanX.change_face("angry",2)
                    if not JeanX.Forced and not Approvalcheck(JeanX, 900, "LO"):
                            $ JeanX.recent_history.append("angry")
                            $ JeanX.daily_history.append("angry")
                            $ JeanX.change_stat("obedience", 90, 25)
                    ch_j "Oh, so it's not saggy like [EmmaX.name]'s?"
    else:
        $ JeanX.AddWord(1,0,0,0,"bottomless") #$ JeanX.History.append("bottomless")
        if Approvalcheck(JeanX, 800) and not JeanX.Forced:
                $ JeanX.change_stat("inhibition", 60, 5)
                $ JeanX.change_stat("obedience", 90, 10)
        else:
                $ JeanX.change_stat("love", 90, -5)
                $ JeanX.change_stat("inhibition", 200, -5)
                $ JeanX.change_face("angry")
                $ JeanX.change_stat("obedience", 90, 15)
    return

label Jubes_First_Bottomless(Silent = 0):
    if JubesX.PantiesNum() > 1 or JubesX.PantsNum() > 2 or JubesX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if JubesX.location != bg_current and "phonesex" not in Player.recent_history:
            return
    $ JubesX.recent_history.append("bottomless")
    $ JubesX.daily_history.append("bottomless")
    $ JubesX.DrainWord("no_bottomless")
    $ JubesX.SeenPussy += 1
    if JubesX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ JubesX.change_stat("inhibition", 80, 30)
    $ JubesX.change_stat("obedience", 70, 10)
    if not Silent:
        $ JubesX.change_face("sly")
        if JubesX.Pubes:
                "You find yourself staring at [JubesX.name]'s furry pussy."
        else:
                "You find yourself staring at [JubesX.name]'s bare pussy."
        menu Jubes_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ JubesX.change_stat("love", 90, 20)
                    $ JubesX.change_stat("inhibition", 60, 25)
                    $ JubesX.change_face("surprised",2)
                    ch_v "!!"
                    $ JubesX.change_face("smile",1)
                    ch_v "Oh, um, yeah, I. . . also. . . "
                    $ JubesX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if JubesX.Pubes:
                $ JubesX.change_face("confused",2)
                ch_v "Well. . . yeah."
                if Approvalcheck(JubesX, 700, "LO"):
                    $ JubesX.change_face("bemused",1)
                    menu:
                        ch_v "Did you. . . prefer it shaved?"
                        "Yes":
                            if Approvalcheck(JubesX, 900, "LO"):
                                    $ JubesX.change_stat("obedience", 50, 30)
                                    $ JubesX.change_stat("inhibition", 60, 25)
                                    ch_v "I guess I could. . ."
                                    $ JubesX.Todo.append("pubes")
                            else:
                                    $ JubesX.change_face("normal")
                                    ch_v "I dunno, seems like a lot of hassle."
                        "Up to you, I guess.":
                                    $ JubesX.change_stat("love", 80, 10)
                                    ch_v "Well, yeah, right? Of course."
                                    if Approvalcheck(JubesX, 900, "LO"):
                                            $ JubesX.change_stat("inhibition", 60, 10)
                                            $ JubesX.Todo.append("pubes")
                        "No, leave it that way.":
                                    if Approvalcheck(JubesX, 900, "LO"):
                                            $ JubesX.change_face("sly")
                                            $ JubesX.change_stat("love", 80, 10)
                                    else:
                                            $ JubesX.change_face("angry",Mouth="normal")
                                    $ JubesX.change_stat("inhibition", 60, 25)
                                    ch_v "Oh, I guess that's your call?"
                                    $ JubesX.Brows = "normal"
                else:
                        $ JubesX.change_face("angry",1)
                        $ JubesX.change_stat("love", 40, -20)
                        $ JubesX.change_stat("obedience", 50, 25)
                        $ JubesX.change_stat("inhibition", 60, -5)
                        ch_v "Well, of course!"
            "What a mess.":
                    $ JubesX.change_stat("love", 90, -30)
                    $ JubesX.change_stat("obedience", 50, 25)
                    $ JubesX.change_stat("inhibition", 70, -30)
                    $ JubesX.change_face("angry",2)
                    if not JubesX.Forced and not Approvalcheck(JubesX, 900, "LO"):
                            $ JubesX.recent_history.append("angry")
                            $ JubesX.daily_history.append("angry")
                            $ JubesX.change_stat("obedience", 70, 25)
                    ch_v "Oh, them's fighting words. . ."
    else:
        $ JubesX.AddWord(1,0,0,0,"bottomless") #$ JubesX.History.append("bottomless")
        if Approvalcheck(JubesX, 800) and not JubesX.Forced:
                $ JubesX.change_stat("inhibition", 60, 5)
                $ JubesX.change_stat("obedience", 70, 10)
        else:
                $ JubesX.change_stat("love", 90, -5)
                $ JubesX.change_stat("inhibition", 70, -5)
                $ JubesX.change_face("angry")
                $ JubesX.change_stat("obedience", 70, 15)
    return
