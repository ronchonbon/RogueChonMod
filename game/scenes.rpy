label Poly_Start(Newbie=0,Round2=0,Asked=0): #rkeljsv
        # This is called prior to any new girls being added to your dating structure
        # If there are already two girls in there, it kicks up to the Harem version.
        # Newbie will be the new girl
        # Asked is passed if you request it from a chat menu
        $ Line = 0

        if Newbie in Player.Harem:
            return

        if not Player.Harem:
                return

        if Asked in TotalGirls:
                if Asked in Player.Harem and Player.Harem[0] != Asked:
                        #moves character "Asked" to the head of the line.
                        $ Player.Harem.remove(Asked)
                        if Player.Harem:
                                $ Player.Harem.insert(0,Asked)
                        else:
                                $ Player.Harem.append(Asked)

        if "polystart" in Player.DailyActions:
                if Round2 and Asked:
                        "You pull [Player.Harem[0].Name] aside for a moment."
                        ch_p "Hey, have you changed your mind about [Newbie.Name] lately?"
                        if Player.Harem[0] == RogueX:
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
                        call AnyLine(Asked,"Ask me some time later.")
                return

        $ Player.DailyActions.append("polystart")

        if len(Player.Harem) >= 2:
                call Harem_Start(Newbie,Round2)
                return


        $ Party = [Player.Harem[0]]
        call Shift_Focus(Player.Harem[0])
        call Set_The_Scene
        call CleartheRoom(Player.Harem[0])


        if Round2:
                "You pull [Party[0].Name] aside for a moment."
                ch_p "Hey, have you changed your mind about [Newbie.Name] lately?"
        else:
                $ Party[0].FaceChange("bemused")
                "[Party[0].Name] pulls you aside and wants to talk about something."

                #Line 1
                if Party[0] == RogueX:
                        ch_r "I've seen you were getting pretty cozy with [Newbie.Name]."
                elif Party[0] == KittyX:
                        ch_k "You look kinda close with [Newbie.Name] lately."
                elif Party[0] == EmmaX:
                        ch_e "I've noticed that [Newbie.Name] and yourself have been spending time together."
                elif Party[0] == LauraX:
                        ch_l "You've been all over [Newbie.Name] lately."
                elif Party[0] == JeanX:
                        ch_j "I saw you with [Newbie.Name] earlier."
                elif Party[0] == StormX:
                        ch_s "I saw you spending time with [Newbie.Name] earlier."
                elif Party[0] == JubesX:
                        ch_v "I saw you hanging with [Newbie.Name] earlier."
                #end Line 1


        if Party[0].GirlLikeCheck(Newbie) >= 800:
                $ Party[0].FaceChange("sly")
        elif Party[0].GirlLikeCheck(Newbie) >= 600:
                pass
        else:
                # neither likes her much
                $ Party[0].FaceChange("angry",Mouth="normal")

        # We like her or not
        if Party[0] == RogueX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "She is pretty sexy, I guess."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "I like her just fine, I was just wondering where it was headed."
                else:
                        # neither likes her much
                        ch_r "I'm not really a fan'a hers."
        elif Party[0] == KittyX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, I get that. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but I'm not sure. . ."
                else:
                        # neither likes her much
                        ch_k "I don't really like her much."
        elif Party[0] == EmmaX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think she's quite the catch."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "I do like her, but have some concerns."
                else:
                        # neither likes her much
                        ch_e "I don't really approve."
        elif Party[0] == LauraX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, I get it."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                else:
                        # neither likes her much
                        ch_l "I don't like her."
        elif Party[0] == JeanX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_j "I get it, she's hot enough."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_j "She's. . . fine."
                else:
                        # neither likes her much
                        ch_j "You probably shouldn't be seen around her."
        elif Party[0] == StormX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_s "She is very beautiful, certainly."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_s "She is a good girl, certainly. . ."
                else:
                        # neither likes her much
                        ch_s "I do not think I like her much."
        elif Party[0] == JubesX:
                if Party[0].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_v "Ok, she's totally hot, but. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_v "She's. . . fine, but. . ."
                else:
                        # neither likes her much
                        ch_v "I'm not there for it."
        #end line 2


        #Line 3
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
        #end Line 3

        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ Line = "y"
            "Maybe, what do you think?":
                $ Line = "m"
            "No, not really.":
                $ Line = "n"

        if Line == "y":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they like her a lot
                    $ Line = "yy"
                    $ Party[0].Statup("Love", 90, 5)
                    $ Party[0].Statup("Obed", 50, 5)
                    $ Party[0].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1800):
                    # if they really like you enough to put up with it
                    $ Line = "ym"
                    $ Party[0].Statup("Obed", 50, 5)
            elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 500:
                    # if they like her well enough
                    $ Line = "ym"
            else:
                    # neither likes her much
                    $ Line = "yn"
                    $ Party[0].Statup("Love", 90, -10)
        #end Line = y
        if Line == "m":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    $ Party[0].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 600:
                    # if they both like her well enough
                    $ Line = "mm"
            else:
                    # neither likes her much
                    $ Line = "mn"
        #end Line = m
        if Line == "n":
            if Party[0].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    $ Party[0].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    $ Party[0].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1300) and Party[0].GirlLikeCheck(Newbie) >= 500:
                    # if they both like her well enough
                    $ Line = "nm"
                    $ Party[0].Statup("Love", 90, 5)
            else:
                    # if they don't like her well enough
                    $ Line = "nn"
                    $ Party[0].Statup("Love", 90, 10)
        #end Line = n


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if Line == "yn" or Line == "mn" or Line == "nn":
                $ Party[0].FaceChange("angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                $ Party[0].FaceChange("sexy")
        else:
                $ Party[0].FaceChange("bemused")

        #Line 5
        if Party[0] == RogueX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess I can live with that."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_r "Hmm, not that I would have minded."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think I'm really cool with that."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."

        elif Party[0] == KittyX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with me!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, I can[KittyX.like]live with that."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_k "Ok, I would have been ok with it though."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with me."
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."

        elif Party[0] == EmmaX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Lovely. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose I can make do then."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_e "You could do a lot worse."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."

        elif Party[0] == LauraX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, I can work with that."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_l "Ok. I'm cool with it if you do though."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Good."

        elif Party[0] == JeanX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_j "Well, ok, sure."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_j "Well. . . she could be fun. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_j "Really? I mean, she could be fun."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_j "Well, ok, fine. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_j "Ok. I could think about it though."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_j "Well, cut it out."
                elif Line == "nn":
                        # if you said no and agree
                        ch_j "Yeah."

        elif Party[0] == StormX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_s "Oh, that will be nice. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_s "Oh, you definitely should!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_s "That is too bad. You would go well together."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_s "Well, that should be fine."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_s "You might want to reconsider. . ."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_s "I do not think I could deal with her."
                elif Line == "nn":
                        # if you said no and agree
                        ch_s "Yes, I would agree with that."

        elif Party[0] == JubesX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_v "Ok, cool."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_v "Yeah, sure, I'm down with it."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_v "Ok, but you might be missing out!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_v "Ok, yeah, I can deal."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_v "Ok, your call, I guess."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_v "Well. . . I might have some feelings."
                elif Line == "nn":
                        # if you said no and agree
                        ch_v "Glad we're on the same page here."

        #end Line 5

        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):
                    #They were generally favorable, so you agreed
                    $ Line = "yy"
                    $ Party[0].FaceChange("smile")
                    $ Party[0].Statup("Love", 90, 10)
                    $ Party[0].Statup("Obed", 50, 10)
                    if Party[0] == RogueX:
                                    ch_r "Great, sounds fun."
                    elif Party[0] == KittyX:
                                    ch_k "Cool, sounds fun."
                    elif Party[0] == EmmaX:
                                    ch_e "Lovely. . ."
                    elif Party[0] == LauraX:
                                    ch_l "Nice."
                    elif Party[0] == JeanX:
                                    ch_j "Ok then."
                    elif Party[0] == StormX:
                                    ch_s "That sounds fantastic."
                    elif Party[0] == JubesX:
                                    ch_v "Sweet!"

                "Well then, I guess I'll stop." if Line in ("mn","yn","ym","mm","nm"):
                    #They were unfavorable, so you gave up on it.
                    $ Line = "nn"
                    $ Party[0].FaceChange("smile")
                    $ Party[0].Statup("Love", 90, 10)
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

                "I'm asking her in anyway." if Line in ("mn","yn"):
                    #if they were unfavorable, but you insist
                    pass

                "Well, I'm going to pass anyway." if Line in ("nm","ny","mm"):
                    #if they give you permission, but you aren't into it.
                    $ Line = "nn"
                    $ Party[0].FaceChange("sad")
                    $ Party[0].Statup("Obed", 70, 5)
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

        if Line == "mn" or Line == "yn":
                # if you said yes/maybe and they said no, but you insisted anyway

                if ApprovalCheck(Party[0], 1600) and Party[0].GirlLikeCheck(Newbie) >= 500:
                            $ Party[0].FaceChange("sadside")
                            $ Party[0].Statup("Love", 90, -5)
                            $ Party[0].Statup("Obed", 50, 15)
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
                                    ch_j "But this counts as your Christmas present."
                            elif Party[0] == StormX:
                                    ch_s ". . ."
                                    ch_s "I can accept that."
                            elif Party[0] == JubesX:
                                    ch_v "Whatever. Fine."
                            $ Line = "yy"
                else:
                            $ Party[0].FaceChange("angry",Eyes="side")
                            $ Party[0].Statup("Love", 90, -25)
                            $ Party[0].Statup("Inbt", 90, 10)
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
                            call Remove_Girl(Party[0])
        #end "she said no but you insisted"

        $ Party = []
        if Line == "yy":
                if Newbie.Tag + "No" in Player.Traits:
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                "You should give [Newbie.Name] a call."
        else:
                $ Player.Traits.append(Newbie.Tag + "No")
        return

label Harem_Start(Newbie=0,Round2=0): #rkeljsv
        # This is called prior to any new girls being added to your dating structure
        # If there are aren't two girls in there, it kicks back.
        # Newbie will be the new girl

        $ Line = 0

        if len(Player.Harem) < 2:
                #if there aren't enough girls yet, forget about it.
                return

        $ Party = [Player.Harem[0],Player.Harem[1]]
        # Adds first two harem members to party, removed everyone else from the room.
        call Present_Check
        $ Party = [Player.Harem[0],Player.Harem[1]]
        call Shift_Focus(Player.Harem[0])
        call Set_The_Scene

        $ Party[0].FaceChange("bemused")
        $ Party[1].FaceChange("bemused")
        if Round2:
                "You call [Party[0].Name] and [Party[1].Name] over."
                ch_p "I was wondering if you'd changed your mind about [Newbie.Name]."
        else:
                "[Party[0].Name] pulls you aside and wants to talk about something."
                #Line 1

                if Party[0] == RogueX:
                        ch_r "Hey, so me and [Party[1].Name] have been talk'in."
                elif Party[0] == KittyX:
                        ch_k "So[KittyX.like]me and [Party[1].Name] had a little chat."
                elif Party[0] == EmmaX:
                        ch_e "[Party[1].Name] and I have been discussing a few things."
                elif Party[0] == LauraX:
                        ch_l "I had a little chat with [Party[1].Name]. . ."
                elif Party[0] == JeanX:
                        ch_j "Hey, I was talking to. . . this one here. . ."
                elif Party[0] == StormX:
                        ch_s "[Party[1].Name] and I were having lunch earlier, and something came up."
                elif Party[0] == JubesX:
                        ch_v "So [Party[1].Name] and I were talking earlier, and something came up. . ."
                #end Line 1

                #Line 2
                if Party[1] == RogueX:
                        ch_r "We hear that you were getting pretty cozy with [Newbie.Name]."
                elif Party[1] == KittyX:
                        ch_k "We hear that you're kinda close with [Newbie.Name] lately."
                elif Party[1] == EmmaX:
                        ch_e "We've hear that [Newbie.Name] and yourself have been spending time together."
                elif Party[1] == LauraX:
                        ch_l "You've been all over [Newbie.Name] lately."
                elif Party[1] == JeanX:
                        ch_j "We noticed you were around [Newbie.Name] a lot lately."
                elif Party[1] == StormX:
                        ch_s "We have both noticed you spending time with [Newbie.Name] lately."
                elif Party[0] == JubesX:
                        ch_v "We totally saw you hanging with [Newbie.Name] earlier."
                #end Line 2

        # We like her or not Line 3

        if Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                pass
        elif Party[0].GirlLikeCheck(Newbie) >= 700:
                # only first girl likes her
                $ Party[1].FaceChange("angry",Mouth="normal")
        elif Party[1].GirlLikeCheck(Newbie) >= 700:
                # only second girl likes her
                $ Party[0].FaceChange("angry",Mouth="normal")
        else:
                # neither likes her much
                $ Party[0].FaceChange("angry",Mouth="normal")
                $ Party[1].FaceChange("angry",Mouth="normal")

        if Party[0] == RogueX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_r "Now we like her just fine, and we can't say we don't like the idea much."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_r "Now we like her just fine, but we don't know about share'in."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_r "Now I like her just fine, but [Party[1].Name] ain't so sure."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_r "Now [Party[1].Name] seems to like her, but I'm not so sure."
                else:
                        # neither likes her much
                        ch_r "Neither'a us is really cool with that."
        elif Party[0] == KittyX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_k "She's kinda hot, we get that. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_k "She's ok, sure, but we're not sure. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_k "I like her, but I don't know about [Party[1].Name]."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_k "[Party[1].Name] likes her, but I don't know."
                else:
                        # neither likes her much
                        ch_k "We don't really like her much."
        elif Party[0] == EmmaX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_e "I think we agree that she's a nice catch."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_e "We do like her, but we have some concerns."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_e "[Party[1].Name] doesn't really approve."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_e "[Party[1].Name] seems to think she's acceptable."
                else:
                        # neither likes her much
                        ch_e "We don't really approve."
        elif Party[0] == LauraX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_l "She's pretty hot, we get it."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_l "She's ok, I guess."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_l "She's fine, but [Party[1].Name] doesn't like her."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_l "[Party[1].Name] likes her. I don't."
                else:
                        # neither likes her much
                        ch_l "We don't like her."
        elif Party[0] == JeanX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_j "I get it, she's hot enough."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_j "She's. . . fine."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_j "I think she's fine, but [Party[1].Name] doesn't like her."
                        ch_j "For whatever that's worth. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_j "[Party[1].Name] likes her. I don't."
                        ch_j "So I think you know the right answer to this one. . ."
                else:
                        # neither likes her much
                        ch_j "You probably shouldn't be seen around her."
        elif Party[0] == StormX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_s "We agree that she is very beautiful. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_s "She is a good girl, but we do have some concerns. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_s "I like her, but [Party[1].Name] does not approve."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_s "[Party[1].Name] appears to like her, I am unsure."
                else:
                        # neither likes her much
                        ch_s "We do not like her very much."

        elif Party[0] == JubesX:
                if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                        # if they both like her a lot
                        ch_v "Ok, she's totally hot, but. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
                        # if they both like her well enough
                        ch_v "She's. . . fine, but. . ."
                elif Party[0].GirlLikeCheck(Newbie) >= 700:
                        # only first girl likes her
                        ch_v "She's. . . fine, but, [Party[1].Name]. . ."
                elif Party[1].GirlLikeCheck(Newbie) >= 700:
                        # only second girl likes her
                        ch_v "[Party[1].Name] likes her, but I don't know."
                else:
                        # neither likes her much
                        ch_v "We're not there for it."

        #end line 3

        #Line 4
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
        #end Line 4

        menu:
            extend ""
            "Yeah, I'd like to date her too.":
                $ Line = "y"
            "Maybe, what do you think?":
                $ Line = "m"
            "No, not really.":
                $ Line = "n"

        if Line == "y":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "yy"
                    $ Party[0].Statup("Love", 90, 5)
                    $ Party[0].Statup("Obed", 50, 5)
                    $ Party[0].Statup("Inbt", 90, 10)
                    $ Party[1].Statup("Love", 90, 5)
                    $ Party[1].Statup("Obed", 50, 5)
                    $ Party[1].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "ym"
                    $ Party[0].Statup("Obed", 50, 10)
                    $ Party[1].Statup("Obed", 50, 10)
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "ym"
                            $ Party[0].Statup("Obed", 80, 15)
                            $ Party[1].Statup("Obed", 80, 15)
                    else:
                            # if they don't like her well enough
                            $ Line = "yn"
                            $ Party[0].Statup("Love", 90, -5)
                            $ Party[0].Statup("Obed", 50, -5)
                            $ Party[1].Statup("Love", 90, -5)
                            $ Party[1].Statup("Obed", 50, -5)
            else:
                            # neither likes her much
                            $ Line = "yn"
                            $ Party[0].Statup("Love", 90, -10)
                            $ Party[0].Statup("Obed", 50, -5)
                            $ Party[1].Statup("Love", 90, -10)
                            $ Party[1].Statup("Obed", 50, -5)
        #end Line = y
        if Line == "m":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "my"
                    $ Party[0].Statup("Inbt", 90, 5)
                    $ Party[1].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):
                    # if they both really like you enough to put up with it
                    $ Line = "mm"
            elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
                    if Party[0].GirlLikeCheck(Newbie) >= 600 or Party[1].GirlLikeCheck(Newbie) >= 600:
                            # if they both like her well enough
                            $ Line = "mm"
                    else:
                            # if they don't like her well enough
                            $ Line = "mn"
            else:
                            # neither likes her much
                            $ Line = "mn"
        #end Line = m
        if Line == "n":
            if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:
                    # if they both like her a lot
                    $ Line = "ny"
                    $ Party[0].Statup("Inbt", 90, 10)
                    $ Party[1].Statup("Inbt", 90, 10)
            elif ApprovalCheck(Party[0], 1700) and ApprovalCheck(Party[1], 1700):
                    # if they both really like you enough to put up with it
                    $ Line = "nm"
                    $ Party[0].Statup("Inbt", 90, 5)
            elif ApprovalCheck(Party[0], 1300) and ApprovalCheck(Party[1], 1300):
                    if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:
                            # if they both like her well enough
                            $ Line = "nm"
                    else:
                            # if they don't like her well enough
                            $ Line = "nn"
                            $ Party[0].Statup("Love", 90, 5)
                            $ Party[0].Statup("Inbt", 90, 5)
                            $ Party[1].Statup("Love", 90, 5)
                            $ Party[1].Statup("Inbt", 90, 5)
            else:
                            # neither likes her much
                            $ Line = "nn"
                            $ Party[0].Statup("Love", 90, 5)
                            $ Party[0].Statup("Inbt", 90, 5)
                            $ Party[1].Statup("Love", 90, 5)
                            $ Party[1].Statup("Inbt", 90, 5)
        #end Line = n


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if Line == "yn" or Line == "mn" or Line == "nn":
                $ Party[0].FaceChange("angry")
                $ Party[1].FaceChange("angry")
        elif Line == "yy" or Line == "ny" or Line == "my":
                $ Party[0].FaceChange("sexy")
                $ Party[1].FaceChange("sexy")
        else:
                $ Party[0].FaceChange("bemused")
                $ Party[1].FaceChange("bemused")

        #Line 5
        if Party[0] == RogueX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_r "Great, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_r "Oh, don't let me stop you."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_r "Oh. Well maybe you should!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_r "Yeah, I guess we can live with that."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_r "Hmm, not that we would have minded."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_r "I don't think we're really cool with that."
                elif Line == "nn":
                        # if you said no and agree
                        ch_r "Good to hear."

        elif Party[0] == KittyX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_k "Cool, sounds fun."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_k "Oh, seriously, it's fine with us!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_k "You might want to, she's hot!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_k "Yeah, we can[KittyX.like]live with that."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_k "Ok, we would have been ok with it though."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_k "That's not really cool with us."
                elif Line == "nn":
                        # if you said no and agree
                        ch_k "Good, that wouldn't have been cool."

        elif Party[0] == EmmaX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_e "Lovely. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_e "Oh, please do, she's lovely."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_e "Pity, I rather like her."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_e "I suppose we can make do then."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_e "You could do a lot worse."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_e "I don't think that will be acceptable."
                elif Line == "nn":
                        # if you said no and agree
                        ch_e "Probably for the best."

        elif Party[0] == LauraX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_l "Nice."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_l "Come on, she's pretty great."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_l "You sure? She's hot."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_l "Fine, we can work with that."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_l "Ok. We're cool with it if you do though."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_l "Nope."
                elif Line == "nn":
                        # if you said no and agree
                        ch_l "Good."

        elif Party[0] == JeanX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_j "Well, ok, sure."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_j "Well. . . she could be fun. . ."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_j "Really? I mean, she could be fun."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_j "Well, ok, fine. . ."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_j "Ok. I could think about it though."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_j "Well, cut it out."
                elif Line == "nn":
                        # if you said no and agree
                        ch_j "Yeah."

        elif Party[0] == StormX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_s "Oh, that will be nice. . ."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_s "Oh, you definitely should!"
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_s "That is too bad. You would go well together."

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_s "Well, that should be fine."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_s "You might want to reconsider. . ."

                elif Line == "yn" or Line == "mn":
                        # neither likes her much
                        ch_s "I do not think we could deal with her."
                elif Line == "nn":
                        # if you said no and agree
                        ch_s "Yes, we could agree with that."

        elif Party[0] == JubesX:
                if Line == "yy":
                        # if you said you did and they both like her a lot
                        ch_v "Ok, cool."
                elif Line == "my":
                        # if you said maybe and they both like her a lot
                        ch_v "Yeah, sure, I guess we're down with that down with it."
                elif Line == "ny":
                        # if you said no but they both like her a lot
                        ch_v "Ok, but you might be missing out!"

                elif Line == "ym" or Line == "mm":
                        # if they both really like you enough to put up with it
                        ch_v "Ok, yeah, we can deal."
                elif Line == "nm":
                        # if you said no but they both like her well enough
                        ch_v "Ok, your call, I guess."

                elif Line == "yn" or Line == "mn":
                        # if you said you did they don't like her well enough
                        ch_v "Well. . . we might have some feelings."
                elif Line == "nn":
                        # if you said no and agree
                        ch_v "Glad we're on the same page here."

        #end Line 5

        if Line != "yy" and Line != "nn":
            #if there was some doubt to it
            menu:
                extend ""
                "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):
                        #They were generally favorable, so you agreed
                        $ Line = "yy"
                        $ Party[0].FaceChange("smile")
                        $ Party[1].FaceChange("smile")
                        $ Party[0].Statup("Obed", 80, 5)
                        $ Party[0].Statup("Inbt", 90, 10)
                        $ Party[1].Statup("Obed", 80, 5)
                        $ Party[1].Statup("Inbt", 90, 10)
                        if Party[0] == RogueX:
                                ch_r "Great, sounds fun."
                        elif Party[0] == KittyX:
                                ch_k "Cool, sounds fun."
                        elif Party[0] == EmmaX:
                                ch_e "Lovely. . ."
                        elif Party[0] == LauraX:
                                ch_l "Nice."
                        elif Party[0] == JeanX:
                                ch_j "Good."
                        elif Party[0] == StormX:
                                ch_s "Good."
                        elif Party[0] == JubesX:
                                ch_v "Sweet!"
                "Well then, I guess I'll stop." if Line in ("mn","yn"):
                        #They were unfavorable, so you gave up on it.
                        $ Line = "nn"
                        $ Party[0].FaceChange("normal")
                        $ Party[1].FaceChange("normal")
                        $ Party[0].Statup("Love", 90, 5)
                        $ Party[0].Statup("Inbt", 90, 5)
                        $ Party[1].Statup("Love", 90, 5)
                        $ Party[1].Statup("Inbt", 90, 5)
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
                "I'm asking her in anyway." if Line in ("mn","yn"):
                        #if they were unfavorable, but you insist
                        pass

                "Well, I'm going to pass anyway." if Line in ("ym","my","nm","ny","mm"):
                        #if they give you permission, but you aren't into it.
                        $ Line = "nn"
                        $ Party[0].FaceChange("sad")
                        $ Party[1].FaceChange("sad")
                        $ Party[0].Statup("Obed", 50, 5)
                        $ Party[1].Statup("Obed", 50, 5)
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

            if Line == "yy" or Line == "nn":
                                pass
            elif len(Player.Harem) >= 3:
                                $ Party[0].FaceChange("smile",Eyes="side")
                                $ Party[1].FaceChange("smile",Eyes="side")
                                $ Party[0].Statup("Obed", 90, 5)
                                $ Party[0].Statup("Inbt", 90, 5)
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
                                $ Line = "yy"
            elif Line == "mn" or Line == "yn":
                    # if you said yes/maybe and they said no, but you insisted anyway
                    $Count = 0
                    while Count < 2:
                        if ApprovalCheck(Party[Count], 1600) and Party[Count].GirlLikeCheck(Newbie) >= 500:
                                # She likes you enough to roll over
                                $ Party[Count].FaceChange("sadside")
                                $ Party[Count].Statup("Love", 90, -5)
                                $ Party[Count].Statup("Obed", 90, 10)
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
                                $ Line = "yy"
                        else:
                                # She doewsn't like you enough to roll over
                                $ Party[Count].FaceChange("angry",Eyes="side")
                                $ Party[Count].Statup("Love", 90, -25)
                                $ Party[Count].Statup("Inbt", 90, 10)
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
                                call Remove_Girl(Party[Count])
                        $ Count += 1
            #end "she said no but you insisted"


        if Line == "yy":
                if Newbie.Tag + "No" in Player.Traits:
                        $ Player.Traits.remove(Newbie.Tag + "No")
                $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
                $ Player.Traits.append(Newbie.Tag + "Yes")
                $ Count = len(Player.Harem)
                while Count:
                        $ Count -= 1
                        $ Player.Harem[Count].DrainWord("saw with "+Newbie.Tag,0,0,1)      #removes "saw with Kitty" from traits
                "You should give [Newbie.Name] a call."
        else:
                $ Player.Traits.append(Newbie.Tag + "No")

        $ Party = []
        $Count = 0
        return

label Harem_Initiation(BO=[],BO2=[]):
    # This is called when a new girl is added to the pack
    # it makes them more open to sexing each other.
    $ BO = Player.Harem[:]
    while BO:
            $ BO2 = Player.Harem[:]
            while BO2:
                    if BO[0] != BO2[0] and "poly " + BO2[0].Tag not in BO[0].Traits:
                                $ BO[0].Traits.append("poly " + BO2[0].Tag)
                    if BO[0] != BO2[0] and "saw with " + BO2[0].Tag in BO[0].Traits:
                                $ BO[0].DrainWord("saw with " + BO2[0].Tag,0,0,1)      #removes "saw with Kitty" from traits
                    $ BO2.remove(BO2[0])
            $ BO.remove(BO[0])
    return

label CheatCheck(BO=[],BO2=[]):
        # This checks whether any girl saw you with any other girl today.
        # Called by EventCalls
        # If you're in the room with that girl, it launches the cheated scene, otherwise, it has her ask you about it later.
        # Roster[Counter] is the first girl, Roster[Counter2] is the second girl
        # loops through girl 2 options until finished, then next girl 1 option, until done

        # add an aspect to account for hooking up with multiple girls that have not yet been accounted for. . .
        $ BO = TotalGirls[:]
        $ renpy.random.shuffle(BO)
        while BO:
                if "locked" in Player.Traits and BO[0].Loc != bg_current:
                        #exits if the door is locked and she is not in the room with you
                        pass
                else:
                        $ BO2 = TotalGirls[:]
                        while BO2:
                            if "meet girl" in Player.DailyActions:
                                                #skips if you already have an appointment
                                                return
                            elif BO[0] in Player.Harem:
                                    #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                                    if "saw with " + BO2[0].Tag in BO[0].Traits:
                                                #if "saw with Kitty" in RogueX.Traits:
                                                if BO[0] in Player.Harem and BO2[0] in Player.Harem:
                                                        #if both girls were in the harem, this shouldn't happen
                                                        $ BO[0].DrainWord("saw with "+BO2[0].Tag,0,0,1)      #removes "saw with Kitty" from traits
                                                elif BO[0] in Player.Harem and BO2[0].Tag + "Yes" in Player.Traits:
                                                        $ BO[0].DrainWord("saw with "+BO2[0].Tag,0,0,1)      #removes "saw with Kitty" from traits
                                                elif bg_current == "bg player" or bg_current == BO[0].Home:
                                                        call Cheated(BO[0],BO2[0])
                                                        $ renpy.pop_call()
                                                        return
                            $ BO2.remove(BO2[0])
                $ BO.remove(BO[0])
        return

label ShareCheck(BO=[],BO2=[]):
        # This checks whether one of the girls is supposed to ask the other about joining the harem
        # Called by EventCalls
        # Roster[Counter] is the first girl, Roster[Counter2] is the second girl
        # loops through girl 2 options until finished, then next girl 1 option, until done

        $ BO = TotalGirls[:]
        $ BO.remove(StormX)     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff
        while BO:
                if BO[0] in Player.Harem:
                        #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                        $ BO2 = TotalGirls[:]
                        $ BO2.remove(StormX)     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff     #fix, temporary until Storm gets relationship stuff
                        while BO2:
                                if "ask " + BO2[0].Tag in BO[0].Traits:
                                        #if "ask Kitty" in RogueX.Traits:
                                        if BO[0] in Player.Harem and BO2[0] in Player.Harem:
                                                #if both girls were in the harem, this shouldn't happen
                                                $ BO[0].DrainWord("ask "+BO2[0].Tag,0,0,1)      #removes "askKitty" from traits
                                        else:
                                                call Share(BO[0],BO2[0])
                                                $ renpy.pop_call() #skips past EventCalls
                                                return
                                $ BO2.remove(BO2[0])
                $ BO.remove(BO[0])
        return

label AddictCheck(BO=[]):
        # Called to see if the girl is in an addiction spiral
        # Called by EventCalls
        $ BO = ActiveGirls[:]
        $ renpy.random.shuffle(BO)
        if JubesX in BO and JubesX.Addict >= 40 and BO[0].Resistance:
                $ BO.remove(JubesX)
                if "sunshine" not in JubesX.History or "addiction" in JubesX.DailyActions:
                            pass
                elif bg_current == JubesX.Home or bg_current == "bg player":
                            if not JubesX.Resistance:
                                    #"I'm addicted" event
                                    call First_Addicted(JubesX)
                            else:
                                    call Addiction_Fix(JubesX)
                else:
                    if "asked meet" in JubesX.DailyActions:
                            pass
                    elif "asked meet" in JubesX.DailyActions and JubesX.Addict >= 60:
                            "[JubesX.Name] texts you. . ."
                            call AnyLine(JubesX,"I know I asked to meet you in your room earlier, but I really need a fix.")
                            $ Player.AddWord(1,"asked fix",0,0,0)
                            $ JubesX.AddWord(1,"asked meet","asked meet",0,0)
                            call ReturnToRoom
                            return
                    else:
                            "[JubesX.Name] texts and asks if you could get her a fix later."
                            $ JubesX.AddWord(1,"asked meet","asked meet",0,0)
                            call ReturnToRoom
                            return
        while BO:
                if "locked" in Player.Traits and BO[0].Loc != bg_current:
                        #if the door's locked and she's not in the room, skip it
                        pass
                elif "asked fix" in Player.DailyActions and "asked meet" not in BO[0].DailyActions:
                        #this skips any new girls if you've agreed to meet another one
                        pass
                elif BO[0].Event[3]:
                        #this skips if you've already dealt with her once recently
                        pass
                elif "angry" not in BO[0].RecentActions and "addiction" not in BO[0].DailyActions and BO[0].Action >= 1:
                        #Activates if she needs her fix
                        if (BO[0].Addict >= 60 or (BO[0].Addict >= 40 and BO[0] == JubesX)) and BO[0].Resistance:
                                #if addict over 60, and she's completed the event chain
                                if bg_current == BO[0].Home or bg_current == "bg player":
                                            call Addiction_Fix(BO[0])
                                else:
                                    if "asked meet" in BO[0].RecentActions:
                                            pass
                                    elif "asked meet" in BO[0].DailyActions and BO[0].Addict >= 80:
                                            "[BO[0].Name] texts you. . ."
                                            call AnyLine(BO[0],"I know I asked to meet you in your room earlier, but I'm serious, this is important.")
                                            $ Player.AddWord(1,"asked fix",0,0,0)
                                            $ BO[0].AddWord(1,"asked meet","asked meet",0,0)
                                            call ReturnToRoom
                                            return
                                    else:
                                            "[BO[0].Name] texts and asks if you could meet her in your room later."
                                            $ BO[0].AddWord(1,"asked meet","asked meet",0,0)
                                            call ReturnToRoom
                                            return
                        #Activates if you don't need a fix but already have resistance
                        elif BO[0].Resistance:
                                pass
                        #These are the "first time addict" event chains
                        elif BO[0] == JubesX and BO[0].Addict < 50:
                                pass    #she skips until she hits 50%
                        elif BO[0].Addict >= 35 and not BO[0].Event[1]:
                                #"I'm addicted" event
                                call First_Addicted(BO[0])
                        elif BO[0].Addict >= 60 and BO[0].Event[1] <= 2:
                                #"I'm super-addicted" event
                                call First_Addicted(BO[0])
                        elif BO[0].Addict >= 90:
                                #"I'm crazy-addicted" event
                                call First_Addicted(BO[0])
                $ BO.remove(BO[0])
        return

label Share(Girl=0,Other=0): #rkeljsv
        # This checks when one girl asks another to share you.
        # it is called by Sharecheck

        $ Girl.DrainWord("ask "+Other.Tag,0,0,1) #removes "ask Kitty" from RogueX.Traits

        if Girl.Break[0]:
                #if the girl was only recently broken up with. . .
                "[Girl.Name] sends you a text."
                $ Other.Statup("Love", 90, -10)
                $ Other.Statup("Obed", 80, 10)
                $ Other.Statup("Inbt", 80, 5)

                if Other == RogueX:
                        call AnyLine(Girl,"She said to \"stop bother'in her?\"")
                elif Other == KittyX:
                        call AnyLine(Girl,"She said to \"give it a rest?\"")
                elif Other == EmmaX:
                        call AnyLine(Girl,"She said \"when hell freezes over?\"")
                elif Other == LauraX:
                        call AnyLine(Girl,"She said to \"fuck off?\"")
                elif Other == JeanX:
                        call AnyLine(Girl,"She didn't seem to know who I was talking about.")
                elif Other == StormX:
                        call AnyLine(Girl,"She said \"I would rather not?\"")
                elif Other == JubesX:
                        call AnyLine(Girl,"She said to \"give it a rest?\"")
                call AnyLine(Girl,"I guess we can see if she comes around on the idea.")

        else:
                if Other == JeanX or Other.GirlLikeCheck(Girl) >= 800 or ApprovalCheck(Other, 1800) or (ApprovalCheck(Other, 1500) and Other.GirlLikeCheck(Girl) >= 500):
                        # if she likes the other girl a lot, or likes you a lot, or sort of likes you both. . .
                        $ Other.AddWord(1,0,0,"poly "+Girl.Tag,0) #adds "poly Kitty" to RogueX.Traits
                        #$ Other.AddWord(1,0,0,"dating?",0) #adds "dating" to KittyX.Traits

                        $ Other.Statup("Obed", 80, 10)
                        $ Other.Statup("Inbt", 80, 15)

                        $ BO = Player.Harem[:]
                        while BO:
                                $ BO[0].DrainWord("saw with "+Other.Tag,0,0,1)
                                $ BO.remove(BO[0])
                        if Girl.Event[5]:
                                # if you've already done her BF event before. . .
                                $ Player.Harem.append(Other)
                                #$ Other.AddWord(1,0,0,"dating",0)     #adds "dating" to traits
                        elif bg_current in PersonalRooms:
                                #if you're in a character room, launch their boyfriend speech
                                if Other.Tag+"Yes" not in Player.Traits:
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call expression Other.Tag + "_BF" #call Rogue_BF
                                $ renpy.pop_call() #skips return to ShareCheck
                                $ renpy.pop_call() #skips return to EventCalls
                        else:
                                # if not in a character room, ask later
                                if Other.Tag+"Yes" not in Player.Traits:
                                        $ Player.Traits.append(Other.Tag+"Yes")
                                call AskedMeet(Other,"bemused")
                else:
                        #If Girl refuses to share you
                        "[Girl.Name] sends you a text."
                        call AnyLine(Girl,"I talked to "+Other.Name+" about sharing you, and she said she wasn't into that sort of thing,")
                        if not ApprovalCheck(Other, 2000):
                                $ Other.Statup("Love", 200, -15)
                                $ Other.Statup("Obed", 50, -5)
                                $ Other.Statup("Inbt", 50, 5)
                                call AnyLine(Girl,"She's just not into you like that.")
                        else:
                                $ Other.Statup("Love", 200, -5)
                                call AnyLine(Girl,"She doesn't really like me that much. . .")

                        #means that she won't be available to ask again for another 7 days
                        $ Other.Break[0] = 7
        return

label Cheated(Girl=0,Other=0, Resolution = 0, B = 0): #rkeljsv
        # Called by EventCalls->CheatCheck if you got caught cheating
        #Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
        $ Girl.AddWord(1,0,"relationship",0,0)
        call Shift_Focus(Girl)

        $ Girl.FaceChange("angry")
        if Girl.Loc != bg_current and Girl not in Party:
                "Suddenly, [Girl.Name] shows up and says she needs to talk to you."
        $ Girl.Loc = bg_current

        $ Girl.DrainWord("asked meet",0,1) #removes "asked meet" from daily
        if "meet girl" in Player.DailyActions:
                $ Player.DailyActions.remove("meet girl")

        call Set_The_Scene
        call CleartheRoom(Girl)
        call Taboo_Level(1)

        if Girl.GirlLikeCheck(Other) >= 900:
                $ Resolution += 2
        elif Girl.GirlLikeCheck(Other) >= 800:
                $ Resolution += 1
        $ B = int((Girl.GirlLikeCheck(Other) - 500)/2)

        $ Resolution -= Girl.Cheated if Girl.Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating

        if Girl.Cheated:
                $ Girl.Statup("Love", 200, -50)
                $ Girl.Statup("Obed", 80, -20)
                $ Girl.Statup("Inbt", 50, -50)
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
                $ Girl.Statup("Love", 200, -100)
                $ Girl.Statup("Obed", 80, -30)
                $ Girl.Statup("Inbt", 50, -20)
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
                        $ Girl.Statup("Love", 90, 30)
                        $ Girl.Statup("Obed", 80, -10)
                        $ Line = "sorry"
                        $ Resolution += 1

                "What do you mean?":
                        $ Girl.Statup("Love", 200, -10)
                        $ Girl.Statup("Obed", 80, 15)
                        $ Girl.Statup("Inbt", 80, 5)
                        if Girl == StormX:
                                ch_s "I am talking about you and [Other.Name]. . ."
                        else:
                                call AnyLine(Girl,"I mean you screwing around with "+Other.Name+"!")
                        menu:
                                extend ""
                                "Oh! I'm sorry!":
                                    $ Girl.Statup("Love", 90, 20)
                                    $ Girl.Statup("Obed", 80, -10)
                                    $ Line = "sorry"
                                "Oh, that. Yeah.":
                                    $ Girl.Statup("Love", 200, -20)
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Line = "yeah"
                                    $ Resolution -= 1

                "You mean with [Other.Name]?":
                        $ Girl.Statup("Love", 200, -15)
                        $ Girl.Statup("Obed", 80, 20)
                        $ Girl.Statup("Inbt", 80, 10)
                        call AnyLine(Girl,"Yes, \"I mean with "+Other.Name+".\"")

                        if Girl == RogueX:
                                $ Line = "Y'all were screwing around behind my back!"
                        elif Girl == KittyX:
                                $ Line = "Why were you all over her like that?!"
                        elif Girl == EmmaX:
                                $ Line = "Or didn't you notice who you were fucking?"
                        elif Girl == LauraX:
                                $ Line = "I can smell her on you."
                        elif Girl == JeanX:
                                $ Line = "I played back her memories of it!"
                        elif Girl == StormX:
                                $ Line = "I know that the two of your were together."
                        elif Girl == JubesX:
                                ch_v "I have a sensitive nose. . ."

                        if Girl.Cheated:
                            $ Line = Line+" Again!"
                        call AnyLine(Girl,Line)
                        menu:
                                extend ""
                                "Oh! I'm sorry!":
                                    $ Girl.Statup("Love", 90, 15)
                                    $ Girl.Statup("Obed", 80, -10)
                                    $ Line = "sorry"
                                "Oh, yeah.":
                                    $ Girl.Statup("Love", 200, -20)
                                    $ Girl.Statup("Obed", 80, 10)
                                    $ Line = "yeah"
                                    $ Resolution -= 2

        if Line == "sorry":
                    $ Girl.FaceChange("sadside")
                    if Girl == RogueX:
                            ch_r "Well 'course you are, but that don't make it right."
                            ch_r "Screwing around with [Other.Name] like that. . ."
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
                    $ Girl.FaceChange("sad")
        else:
                    $ Girl.FaceChange("confused")
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
                    $ Girl.FaceChange("angry")

        menu:
                extend ""
                "I really hurt you, and I'm sorry.":
                        $ Girl.Statup("Love", 90, 25)
                        if Girl == JeanX:
                                $ Girl.Statup("Obed", 80, 10)
                                $ Resolution += 1
                                ch_j "Yes, we've established that, what else?"
                        else:
                                $ Girl.Statup("Obed", 80, -5)
                                call AnyLine(Girl,"Well at least you're owning up to it.")
                        $ Resolution += 2

                "We were just messing around, nothing serious.":
                        $ Girl.Statup("Obed", 80, 30)
                        $ Girl.Statup("Inbt", 80, 10)
                        if Girl == RogueX:
                                ch_r "\"Nothing serious?\" You did {i}not{/i} just tell me that."
                        elif Girl == KittyX:
                                ch_k "I'll \"nothing serious\" you!"
                        elif Girl == EmmaX:
                                ch_e "I'll be the judge of what is or is not \"serious.\""
                        elif Girl == LauraX:
                                if ApprovalCheck(Girl, 1500):
                                        ch_l "Ok, that's fair."
                                else:
                                        ch_l "Do you want to try that one again?"
                        elif Girl == JeanX:
                                $ Girl.Eyes = "side"
                                $ Girl.Statup("Love", 80, 10)
                                $ Resolution += 1
                                ch_j "Oh. . . well. . ."
                                $ Girl.FaceChange("angry",2)
                                ch_j "That's not the point!"
                                $ Girl.Blush = 1
                        elif Girl == StormX:
                                ch_s "Nothing serious to you, but what of me?"
                        elif Girl == JubesX:
                                ch_v "Oh, is that supposed to be an excuse?"
                        $ Girl.Statup("Love", 200, -25)

                        if not ApprovalCheck(Girl, 700, "O", Bonus = (B/3)):
                            $ Resolution -= 2

                "I think she's really hot.":
                    if B >= 100 or ApprovalCheck(Girl, 500, "I", Bonus = (B/3)):
                            # if Like trait is 700 or more. . .
                            $ Girl.FaceChange("confused",Eyes="side")
                            if Girl == StormX:
                                    ch_s "She is certainly beautiful, but I do not see why that would be an excuse."
                            elif Other == KittyX:
                                    call AnyLine(Girl,"Well. . . yeah, she is cute, but so what?")
                            else:
                                    call AnyLine(Girl,"Well. . . yeah, she is hot, but so what?")
                            $ Girl.Statup("Lust", 90, 5)
                            $ Line = "threeway"
                    else:
                            $ Girl.Statup("Love", 200, -20)
                            $ Girl.Statup("Obed", 80, 30)
                            if Girl == RogueX:
                                    ch_r "Well that don't mean shit, [Player.Name], you're with me!"
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
                    $ Girl.Statup("Obed", 80, 30)
                    if B >= 100 or ApprovalCheck(Girl,500,"I"):
                            # if Like trait is 700 or more. . .
                            $ Girl.FaceChange("confused",Eyes="side")
                            $ Girl.Statup("Inbt", 90, 25)
                            $ Girl.Statup("Lust", 90, 5)
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
                            $ Line = "threeway"
                    elif B >= 50 and Girl != JeanX:
                            # if Like trait is 600 or more. . .
                            $ Girl.FaceChange("confused")
                            $ Girl.Statup("Love", 200, -10)
                            if Girl == EmmaX and Other != StormX:
                                    ch_e "She's a good student, but that doesn't mean I'm interested in sharing."
                            elif Girl == StormX:
                                    ch_s "I like her well enough, but what difference does that make?"
                            else:
                                    call AnyLine(Girl,"We're friends, but so what?")
                    else:
                            $ Girl.Statup("Love", 200, -20)
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
                            $ Girl.Statup("Love", 90, 5)
                            call AnyLine(Girl,"Like the last time you told me that, you mean?")
                            $ Resolution -= 1
                    else:
                            $ Girl.Statup("Love", 90, 20)
                            $ Girl.FaceChange("angry")
                            $ Resolution += 2 if Resolution < 3 else 0
                            call AnyLine(Girl,"I'll hold you to that.")
                    $ Line = 0

                "I can't make any promises, she's pretty hot.":
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Love", 200, -40)
                            $ Girl.Statup("Obed", 90, 40)
                            $ Girl.Statup("Inbt", 90, 10)
                            call AnyLine(Girl,"Then I don't know what you tell you, I think we're through.")
                            $ Resolution -= 2
                            $ Line = 0

                "Have you considered maybe letting her join us?":
                        $ Girl.FaceChange("confused",Mouth="smile")
                        if ApprovalCheck(Girl, 2200, Bonus = B) or ApprovalCheck(Girl, 950, "L", Bonus = (B/3)):
                                $ Girl.Statup("Inbt", 90, 30)
                                $ Girl.Statup("Lust", 89, 10)
                                $ Resolution += 2
                        elif ApprovalCheck(Girl, 1500, Bonus = B) or Girl.GirlLikeCheck(Other) >= 700:
                                $ Girl.Statup("Inbt", 90, 10)
                                $ Girl.Statup("Lust", 90, 5)
                        else:
                                $ Resolution -= 3
                                $ Girl.Statup("Love", 200, -25)
                                $ Girl.Statup("Inbt", 90, 10)

                        $ Girl.Statup("Obed", 90, 40)
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
                        $ Line = "threeway"

        if Resolution >= 5 and Line == "threeway": #she agrees to a threeway
                        if Girl.Cheated:
                                $ Girl.Statup("Love", 90, 25)
                                $ Girl.Statup("Obed", 90, 30)
                                $ Girl.Statup("Inbt", 90, 60)
                        else:
                                $ Girl.Statup("Love", 90, 50)
                                $ Girl.Statup("Obed", 90, 40)
                                $ Girl.Statup("Inbt", 90, 40)
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
                        call AnyLine(Girl,"Maybe I could live with that, I'll talk to "+Other.Name+".")

                        $ Line = "poly"

        elif Resolution >= 5: #she suggests a threeway
                        if Girl.Cheated:
                                $ Girl.Statup("Love", 90, 20)
                                $ Girl.Statup("Obed", 90, 10)
                                $ Girl.Statup("Inbt", 90, 100)
                        else:
                                $ Girl.Statup("Love", 90, 40)
                                $ Girl.Statup("Obed", 90, 10)
                                $ Girl.Statup("Inbt", 90, 60)
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
                                call AnyLine(Girl,"Perhaps "+Other.Name+" and I could work something out.")
                        else:
                                call AnyLine(Girl,"Maybe me and "+Other.Name+" can work something out.")
                        $ Line = "poly"

        elif Resolution >= 2: #she agrees to forgive you
                    if Line == "threeway":
                            #you've asked for a threeway, but she knocked it down
                            $ Girl.Statup("Obed", 80, 10)
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
                    $ Girl.FaceChange("sadside")
                    if Girl.Cheated:
                            $ Girl.Statup("Obed", 80, 15)
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
                            $ Girl.Statup("Obed", 80, 30)
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
                    $ Girl.FaceChange("angry")
                    if Line == "threeway":
                        $ Girl.Statup("Obed", 80, 10)
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
                        $ Girl.Statup("Obed", 90, -50)
                        $ Girl.Statup("Inbt", 90, 20)
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
                        $ Girl.Statup("Obed", 90, -50)
                        $ Girl.Statup("Inbt", 90, 10)
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


        $ BO = TotalGirls[:]
        while BO:
                #removes "saw with Rogue" from traits
                $ Girl.DrainWord("saw with "+BO[0].Tag,0,0,1)
                $ BO.remove(BO[0])

        if Line == "poly":
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
                        $ Girl.FaceChange("sad")
                        if Resolution >= 3:
                                $ Girl.Statup("Love", 90, 10)
                                $ Girl.Statup("Obed", 90, 5)
                                if Girl == RogueX:
                                        ch_r "I am too, [RogueX.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Me too, [KittyX.Petname]. . ."
                        else:
                                $ Girl.Statup("Love", 90, 5)
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
                        if Girl.Obed + Girl.Inbt >= (1.5 * Girl.Love) or Girl.Lust >= 70:
                            #(Obed + Inbt) >= (1.5 * Love) or Lust >= 70
                            $ Girl.FaceChange("sly",Eyes="side")
                            $ Girl.Statup("Love", 90, 20)
                            $ Girl.Statup("Obed", 90, 10)
                            $ Girl.Statup("Inbt", 90, 10)
                            if Girl == StormX:
                                    ch_s "You are incorrigible, [StormX.Petname]."
                            else:
                                    call AnyLine(Girl,"Sure, whatever.")
                            call expression Girl.Tag + "_SMenu" #call Rogue_SexMenu
                        else:
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Love", 90, -10)
                            $ Girl.Statup("Obed", 90, -10)
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
                            $ Girl.FaceChange("sad")
                            $ Girl.Statup("Love", 90, 10)
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
                        if Girl.Obed + Girl.Inbt >= (1.5 * Girl.Love) or Girl.Lust >= 70:
                            #(Obed + Inbt) >= (1.5 * Love) or Lust >= 70
                            $ Girl.FaceChange("angry",Eyes="side")
                            $ Girl.Statup("Obed", 90, 10)
                            $ Girl.Statup("Inbt", 90, 10)
                            if Girl == StormX:
                                    ch_s "You are incorrigible, [StormX.Petname]."
                            else:
                                    call AnyLine(Girl,"Sure, whatever.")
                            $ Girl.DrainWord("angry",0,1)
                            call expression Girl.Tag + "_SMenu" #call Rogue_SMenu
                            $ Girl.AddWord(1,0,"angry",0,0) #adds "angry" to daily
                        else:
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Love", 90, -20)
                            $ Girl.Statup("Obed", 90, -10)
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
                            $ Girl.FaceChange("angry",Eyes="side")
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 90, 10)
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
                            $ Girl.FaceChange("confused")

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
                $ bg_current = "bg player"
                jump Misplaced
        else:
                call Remove_Girl(Girl)
        return

label NoFap(Girl=0,TabStore=Taboo,Cnt=0): #rkeljsv
        # called when you ask them not to fap from the romance menu
        # call NoFap(Girl)

        $ Taboo = 0
        ch_p "About when you masturbate on your own time. . ."

        if "askedfap" in Girl.DailyActions:
                #if it's not the first time you've asked today. . .
                if "nofap" in Girl.Traits:
                        call AnyLine(Girl,"I understand already.")
                else:
                        call AnyLine(Girl,"Stop bothering me with this.")

        elif "askedfap" in Girl.History:
                #if it's not the first time you asked. . .
                if not ApprovalCheck(Girl, 800):
                        #rude response
                        $ Girl.FaceChange("angry",2,Eyes="surprised")
                        $ Girl.Statup("Love", 80, -1)
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
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
                        $ Girl.FaceChange("angry",1)
                else:
                        #neutral response
                        $ Girl.Statup("Obed", 60, 2)
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Inbt", 60, 1)
                        $ Girl.Statup("Lust", 50, 1)
                        $ Girl.FaceChange("confused",1)
                        if Girl == EmmaX:
                                ch_e "Oh? This again?"
                        elif Girl == LauraX:
                                ch_l "Yeah?"
                        elif Girl == StormX:
                                ch_s "Oh, what is it, [StormX.Petname]?"
                        else: #Rogue, Kitty, Jean
                                $ Girl.FaceChange("confused",2)
                                call AnyLine(Girl,"Um, yeah, what about it?")

        else:
                #if this is the first time you've asked her. . .
                if not ApprovalCheck(Girl, 800):
                        #rude response
                        $ Girl.FaceChange("angry",2,Eyes="surprised")
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
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
                        $ Girl.FaceChange("angry",1)
                elif not ApprovalCheck(Girl, 500, "I"): # or RogueX.SEXP <= 30?
                        #shy response
                        $ Girl.Statup("Love", 90, -5)
                        $ Girl.Statup("Obed", 50, 3)
                        $ Girl.Statup("Obed", 80, 1)
                        $ Girl.Statup("Inbt", 30, -1)
                        $ Girl.Statup("Inbt", 30, 3, 1)
                        $ Girl.Statup("Lust", 50, 3)
                        if Girl == RogueX:
                                $ Girl.FaceChange("surprised",2)
                                ch_r "I. .  um. . I don't really do that. . ."
                        elif Girl == KittyX:
                                $ Girl.FaceChange("surprised",2)
                                ch_k "Oh, um, that's not really something I. . ."
                        elif Girl == EmmaX:
                                $ Girl.FaceChange("confused",1)
                                ch_e "I'm not sure why what I do in private is your business. . ."
                        elif Girl == LauraX:
                                $ Girl.FaceChange("surprised",2)
                                ch_l "Um. . . yeah?"
                        elif Girl == JeanX:
                                ch_j "Well, look. . . that's none of your business."
                        elif Girl == StormX:
                                ch_s ". . ."
                                ch_s "I am not really sure what business that is of yours, [StormX.Petname]."
                        elif Girl == JubesX:
                                ch_v "Do I. . ."
                                ch_v "What? Um. . . I don't wanna talk about it."
                elif ApprovalCheck(Girl, 500, "O"):
                        #submissive response
                        $ Girl.Statup("Obed", 90, 5)
                        $ Girl.Statup("Inbt", 50, 2)
                        $ Girl.Statup("Inbt", 80, 1)
                        $ Girl.Statup("Lust", 50, 5)
                        $ Girl.FaceChange("confused",1)
                        if Girl == EmmaX:
                                ch_e "What of it?"
                        else: #Rogue, Kitty, Laura
                                call AnyLine(Girl,"What about it?")
                else:
                        #neutral response
                        $ Girl.Statup("Obed", 90, 4)
                        $ Girl.Statup("Inbt", 90, 3)
                        $ Girl.Statup("Lust", 50, 3)
                        $ Girl.FaceChange("confused",1)
                        if Girl == EmmaX:
                                ch_e "Oh? What about it?"
                        elif Girl in (LauraX,JeanX):
                                call AnyLine(Girl,"Yeah?")
                        elif Girl == StormX:
                                ch_s ". . ."
                                ch_s "What did you want to know?"
                        else: #Rogue, Kitty
                                $ Girl.FaceChange("confused",2)
                                call AnyLine(Girl,"Um, yeah, what about it?")
        #end intro check. . .

        menu:
            extend ""
            "I'd rather you not do that." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Obed", 200, 2)
                            $ Girl.Statup("Inbt", 90, 1)
                    if ApprovalCheck(Girl, 1400, "LO"):
                            #loving response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 4)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("bemused",2)
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
                            $ Girl.FaceChange("bemused",1)
                    elif ApprovalCheck(Girl, 1600) and not ApprovalCheck(Girl, 500, "I") and Girl != JeanX:
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",2,Eyes="side")
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
                            $ Girl.FaceChange("bemused",1)
                    elif ApprovalCheck(Girl, 700, "O",Alt=[[JeanX],800]):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 70, 5)
                            $ Girl.FaceChange("sly",1)
                            call AnyLine(Girl,"Yes,"+Girl.Petname+".")
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 90, -3)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("angry",2)
                            if Girl == KittyX:
                                    ch_k "I- this whole conversation is inappropriate!"
                            elif Girl in (EmmaX,JeanX):
                                    call AnyLine(Girl,"I really don't care what \"you'd rather.\"")
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I am uninterested in your opinions on this, [StormX.Petname]."
                            else: #Rogue, Laura
                                    call AnyLine(Girl,"I'd rather you stay out my business.")
                            $ Girl.FaceChange("angry",1)
                            $ Cnt = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -1)
                                    $ Girl.Statup("Obed", 70, 2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("sly",1)
                            if Girl == RogueX:
                                    ch_r "'Fraid not, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Sorry, no. I try to keep busy."
                            elif Girl == EmmaX:
                                    ch_e "No, I think I shall. . . often."
                            elif Girl == LauraX:
                                    ch_l "Sorry, [LauraX.Petname], I've got needs."
                            elif Girl == JeanX:
                                    $ Girl.FaceChange("confused",1)
                                    ch_j "Um. . . no?"
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I would rather we not discuss this, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Um, that would be very inconvenient for me, so. . ."
                                    ch_v "No."
                            $ Cnt = 1
                    if not Cnt:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits
            # end "ask nicely"

            "Don't do that without permission." if "nofap" not in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Obed", 200, 3)
                    if ApprovalCheck(Girl, 600, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 3)
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Obed", 200, 4)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                                    $ Girl.Statup("Lust", 70, 5)
                            $ Girl.FaceChange("sly")
                            call AnyLine(Girl,"Yes,"+Girl.Petname+".")
                    elif ApprovalCheck(Girl, 1200, "LO"):
                            #positive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 4)
                                    $ Girl.Statup("Obed", 80, 3)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 3)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",1)
                            if Girl == RogueX:
                                    ch_r "I guess if it means so much to you. . ."
                            elif Girl == KittyX:
                                    ch_k "I guess I could do \"no fap no-\" what month even is this? . ."
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
                    elif not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Inbt", 90, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("bemused",2,Eyes="side")
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
                            $ Girl.FaceChange("normal",1)
                            $ Cnt = 1
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 70, -5)
                                    $ Girl.Statup("Love", 90, -5)
                                    $ Girl.Statup("Obed", 60, -3)
                                    $ Girl.Statup("Obed", 90, -3)
                                    $ Girl.Statup("Inbt", 90, 3)
                            $ Girl.FaceChange("angry",2)
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
                            $ Girl.FaceChange("angry",1)
                            $ Cnt = 1
                    else:
                            #no
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, -2)
                                    $ Girl.Statup("Obed", 70, -2)
                                    $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("bemused",2)
                            if Girl == RogueX:
                                    ch_r "'Fraid not, [RogueX.Petname]."
                            elif Girl == KittyX:
                                    ch_k "Sorry, no. I try to keep busy."
                            elif Girl == EmmaX:
                                    ch_e "No, I think I shall. . . often."
                            elif Girl == LauraX:
                                    ch_l "Sorry, [LauraX.Petname], I've got needs."
                            elif Girl == JeanX:
                                    $ Girl.FaceChange("confused",1)
                                    ch_j "Um. . . no?"
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I would rather we not discuss this, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "I'm gonna do. . . whatever."
                            $ Girl.FaceChange("bemused",1)
                            $ Cnt = 1
                    if not Cnt:
                            $ Girl.AddWord(1,0,0,"nofap")  #adds "nofap" tag to traits
            # end "obedience order"

            "You can do that if you need to." if "nofap" in Girl.Traits:
                    if "askedfap" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 90, 1)
                    if not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 60, 1)
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Inbt", 70, 5)
                                    $ Girl.Statup("Lust", 90, 10)
                            $ Girl.FaceChange("confused",2)
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
                            $ Girl.FaceChange("smile",1)
                    elif ApprovalCheck(Girl, 750, "O"):
                            #submissive response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 20)
                                    $ Girl.Statup("Obed", 200, 5)
                                    $ Girl.Statup("Obed", 90, 10)
                                    $ Girl.Statup("Inbt", 90, 10)
                                    $ Girl.Statup("Lust", 90, 10)
                            $ Girl.FaceChange("sly",1)
                            call AnyLine(Girl,"Yes,"+Girl.Petname+".")
                    else:
                            #positive response
                            if "okfap" not in Girl.History:
                                    $ Girl.Statup("Love", 90, 5)
                                    $ Girl.Statup("Obed", 60, 3)
                                    $ Girl.Statup("Inbt", 70, 3)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("surprised",2)
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
                            $ Girl.FaceChange("smile",1)
                    $ Girl.DrainWord("nofap",0,0,1) #removes "nofap" tag from traits
                    $ Girl.AddWord(1,0,0,0,"okfap")  #adds "okfap" tag to History

                    #fix add a potential for the girl to run out now. . .
            #end "return permission"

            "Nevermind":
                    if not ApprovalCheck(Girl, 500, "I"):
                            #shy response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 80, 10)
                                    $ Girl.Statup("Inbt", 50, 5)
                            $ Girl.FaceChange("bemused",1)
                            if Girl == EmmaX:
                                    ch_e "Back to more appropriate topics, I hope?"
                            elif Girl == LauraX:
                                    ch_l "Glad we're off this one. . ."
                            elif Girl == JeanX:
                                    $ Girl.FaceChange("confused",1)
                                    ch_j "Um. . .ok?"
                            elif Girl == StormX:
                                    ch_s ". . . Fine."
                            else: #Rogue, Kitty
                                    $ Girl.FaceChange("surprised",2)
                                    call AnyLine(Girl,"Right! What were we even talking about?")
                                    $ Girl.FaceChange("smile",1)
                    elif ApprovalCheck(Girl, 500, "O"):
                            #submissive response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 60, 5)
                                    $ Girl.Statup("Inbt", 80, 5)
                                    $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("sly",1)
                            if Girl in (EmmaX, StormX):
                                    call AnyLine(Girl,"Very Well. . .")
                            else:#Rogue, Kitty, Laura, Jean, Jubuilee
                                    call AnyLine(Girl,"Ok.")
                    elif not ApprovalCheck(Girl, 800):
                            #rude response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Love", 80, 5)
                                    $ Girl.Statup("Obed", 50, 5)
                            $ Girl.FaceChange("angry",2,Eyes="side")
                            if Girl == RogueX:
                                    ch_r "Damned straight, \"never mind.\""
                            elif Girl == EmmaX:
                                    ch_e "I should hope so . . ."
                            elif Girl == StormX:
                                    ch_s "Of course."
                            else: #Kitty, Laura, Jean
                                    call AnyLine(Girl,"Damned right, \"never mind.\"")
                            $ Girl.FaceChange("angry",1)
                    else:
                            #neutral response
                            if "askedfap" not in Girl.History:
                                    $ Girl.Statup("Obed", 50, 3)
                                    $ Girl.Statup("Inbt", 50, 2)
                            $ Girl.FaceChange("sly",1)
                            if Girl in (EmmaX,StormX):
                                    call AnyLine(Girl,"Very Well. . .")
                            else:#Rogue, Kitty, Laura, Jean
                                    call AnyLine(Girl,"Ok.")
            #end "nevermind"

        $ Girl.AddWord(1,0,"askedfap",0,"askedfap")  #adds "askedfap" tag to Daily and History
        $ Taboo = TabStore
        return

label girl_key(character):
    call Shift_Focus(character)
    call Set_The_Scene

    $ character.FaceChange("bemused")

    if character not in [LauraX, JeanX, JubesX]:
        $ character.ArmPose = 2

    if character == RogueX:
        ch_r "Hey, you've been sleeping over a lot, I figured you might want a key?"
    elif character == KittyX:
        ch_k "So you've[KittyX.like]been dropping by a lot lately, I figured you might want a key. . ."
    elif character == EmmaX:
        ch_e "You've been coming by fairly often. . ."
        ch_e ". . . you might want a key. . ."
    elif character == LauraX:
        ch_l "Hey, so. . . this isn't something I usually do but. . ."
        ch_l "Look, you've been sleeping over a lot and I was thinking. . ."
        ch_l "Just take it already."
        "She takes your hand and practically forces a key onto your palm before making your fingers close on it."
    elif character == JeanX:
        ch_j "Oh, here, just in case you wanted to drop by."
        "She tossed a key at you, which you manage to catch."
    elif character == StormX:
        ch_s "You have been coming up more often. . ."
        ch_s ". . . you might want a key. . ."
    elif character == JubesX:
        ch_v "Oh, um. . ."
        ch_v "We've been sleeping together for a bit and. . ."
        ch_v "Here."
        "She takes your hand and hands you her room key."

    ch_p "Thanks."

    if character not in [LauraX, JeanX, JubesX]:
        $ character.ArmPose = 1

    $ Keys.append(character)

    $ character.Event[0] = 1

    return

label girl_boyfriend(character):
    call Shift_Focus(character)

    $ Player.AddWord(1, "interruption")
    $ character.DrainWord("asked meet")

    if character.Loc != bg_current and character not in Party:
        $ character.Loc = bg_current

        if character == RogueX:
            "Suddenly, [character.Name] shows up and says she needs to talk to you."
        elif character == KittyX:
            "[character.Name] approaches you and asks if the two of you can talk."
        elif character == EmmaX:
            "[character.Name] approaches you and asks if the two of you can talk."
        elif character == LauraX:
            "[character.Name] approaches you and motions that she wants to speak to you alone."
        elif character == StormX:
            "[character.Name] approaches you and asks if the two of you can talk."
    elif character in Party:
        if character == RogueX:
            "[character.Name] turns towards you and asks if the two of you can talk."
        elif character  == KittyX:
            "[character.Name] turns towards you and asks if the two of you can talk."
        elif character == EmmaX:
            "[character.Name] turns towards you and asks if the two of you can talk."
        elif character == LauraX:
            "[character.Name] turns towards you and motions that she wants to speak to you alone."
        elif character == StormX:
            "[character.Name] turns towards you and asks if the two of you can talk."

    call Set_The_Scene(0)
    call Display_Girl(character)

    if character == KittyX:
        "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."
    elif character == EmmaX:
        "You can tell she's a bit uncomfortable about whatever she has to say."
    elif character == LauraX:
        "She looks a bit concerned and you can tell she's a bit anxious about whatever she has to say."

    call Taboo_Level
    call CleartheRoom(character)

    $ character.DailyActions.append("relationship")

    if character not in [LauraX, StormX]:
        $ character.FaceChange("bemused", 1)

        if character == RogueX:
            ch_r "So, [character.Petname], we've been hanging out for a while now."
            ch_r ". . ."
        elif character == KittyX:
            ch_k "So, [character.Petname], we've[character.like]been hanging for a while, right?"
            ch_k ". . ."
        elif character == EmmaX:
            ch_e "[EmmaX.Petname], we've been. . . enjoying ourselves for a while now."
            ch_e ". . ."

        $ character.Eyes = "sexy"

        $ line = None

        if character == RogueX:
            $ line = "Right?"
        elif character == KittyX:
            $ line = "Right?"
        elif character == EmmaX:
            $ line = "You have been enjoying yourself?"

        menu:
            character.voice "[line]"
            "Yeah, it's been great." if character in [RogueX]:
                $ character.Statup("Love", 200, 20)
            "Yeah. And it's been amazing." if character in [KittyX, EmmaX]:
                $ character.Statup("Love", 200, 20)
            "Yeah, I guess":
                $ character.Statup("Love", 200, 10)
            "Um, maybe?" if character in [RogueX]:
                $ character.Statup("Love", 200, -10)
                $ character.Statup("Obed", 200, 30)
            "Uhm. . . maybe?" if character in [KittyX, EmmaX]:
                $ character.Statup("Love", 200, -10)
                $ character.Statup("Obed", 200, 30)

        if character.SEXP >= 10:
            if character == RogueX:
                ch_r "I mean, we've done some stuff. . ."
            elif character == KittyX:
                ch_k "I mean, I've gone further with you than I've ever been with anybody before. . ."
            elif character == EmmaX:
                ch_e "I think we've been engaging in some rather inappropriate behavior. . ."
        if character.SEXP >= 15:
            if character == RogueX:
                ch_r "Like {i}sex{/i} stuff. . ."
            elif character == KittyX:
                ch_k "You know[character.like]. . .in the {i}bedroom{/i}. . ."
            elif character == EmmaX:
                ch_e "- for a student and teacher, at least. . ."

        if len(Player.Harem) >= 2:
            if character == RogueX:
                ch_r "I know you've been going with those other girls for a while now, but we got talking and . . ."
            elif character == KittyX:
                ch_k "I know you[KittyX.like]really get around and all. . ."
            elif character == EmmaX:
                ch_e "I understand that this isn't an exclusive deal for you. . ."
        elif character == KittyX and RogueX in Player.Harem:
            if "dating?" in KittyX.Traits:
                ch_k "I know you're kinda[character.like][RogueX.Name]'s boyfriend and all. . . but she and I were talking and[character.like]. . ."
            else:
                ch_k "I know you're kinda[character.like][RogueX.Name]'s boyfriend and all. . ."
        elif Player.Harem:
            if character == RogueX:
                ch_r "I know you've been going with [Player.Harem[0].Name] for a while now, but we got talking and . . ."
            elif character == KittyX:
                ch_k "I know you're kinda[KittyX.like]dating [Player.Harem[0].Name] and all. . ."
            elif character == EmmaX:
                ch_e "I understand that you've been dating [Player.Harem[0].Name]. . ."

        if not character.Event[5]:
            if character == RogueX:
                ch_r "Right, so I was thinking. . ."
                ch_r "I haven't really been able to have a stable relationship, since I couldn't touch anyone."
                ch_r "This is all very new to me, but I'm feeling my way through it as best I can."
                ch_r "Let's make it official, you want to be my boyfriend?"
            elif character == KittyX:
                ch_k "So, uhm. . ."
                ch_k "It’s not like I[KittyX.like]haven’t gone out with guys before."
                ch_k "I just[KittyX.like]..wow, this is so awkward.  I really like you a lot and. . ."
                ch_k "I mean. . . do you wanna[KittyX.like]be my boyfriend?"
                ch_k "[KittyX.Like]maybe we could make it official?"
            elif character == EmmaX:
                ch_e "So, that being the case. . ."
                ch_e "I was wondering if you'd like to make this a bit more official."
                ch_e "If I could perhaps consider you my. . ."
                ch_e "Boyfriend?"
                ch_e "- or something to that effect."
        elif character == KittyX and "dating?" in character.Traits:
            ch_k "[RogueX.Name] said it’d totally be cool if we were[character.like]dating, too."
        elif Player.Harem:
            if character == RogueX:
                ch_r "I'd still like to be your girlfriend too."
            elif character == KittyX:
                ch_k "If you were okay with it. . . I’d still like to be your girlfriend, too."
            elif character == EmmaX:
                ch_e ". . . but I would still like to also consider you my boyfriend as well."
        else:
            if character == RogueX:
                ch_r "You can be a real jerk sometimes, but still. . . I'm serious about this."
                ch_r "I think I want to be your girlfriend. . . officially"
            elif character == KittyX:
                ch_k "I wish you weren’t[character.like]such a jerk sometimes, but still. . . I’m totally serious about this."
                ch_k "I wanna be your girlfriend[character.like]officially."
            elif character == EmmaX:
                ch_e "I don't know why I put up with you, but I do still want to be your girlfriend."

        $ character.Event[5] += 1

        menu:
            extend ""
            "I'd love to!" if character in [RogueX]:
                $ character.Statup("Love", 200, 30)

                "[character.Name] leaps in and kisses you deeply."

                $ character.FaceChange("kiss")
                $ character.Kissed += 1
            "Are you kidding? I'd love to!" if character in [KittyX, EmmaX]:
                $ character.Statup("Love", 200, 30)

                "[character.Name] wraps her arms around you and starts kissing you passionately."

                $ character.FaceChange("kiss")

                call girl_kissing_launch(character, "kiss you")

                $ character.Kissed += 1
            "Um, ok." if character in [RogueX, EmmaX]:
                $ character.Brows = "confused"

                if character in [RogueX]:
                    "[character.Name] is a bit put off by your casual acceptence of reality, but takes it as a positive sign and hugs you."
                elif character in [EmmaX]:
                    "[character.Name] seems a little put off by how casually you’re taking all this."
            "Uhm[character.like]okay." if character in [KittyX]:
                $ character.Brows = "confused"

                "[character.Name] seems a little put off by how casually you’re taking all this."
                "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."
            "I'm with someone now." if Player.Harem:
                $ character.FaceChange("sad",1)

                if character == RogueX:
                    ch_r "I know, I know, I just thought maybe you could go out with me too?"
                elif character == KittyX:
                    ch_k "I know.  I just[character.like]. . . I thought maybe you could go out with me, too, maybe?"
                elif character == EmmaX:
                    ch_e "I understand.  I thought that perhaps you could go out with me as well?"

                menu:
                    extend ""
                    "Sure" if character in [RogueX]:
                        $ character.Statup("Love", 200, 30)

                        "[character.Name] leaps in and kisses you deeply."

                        $ character.FaceChange("kiss")
                        $ character.Kissed += 1
                    "Yes. Absolutely." if (character == KittyX and "KittyYes" in Player.Traits) or (character == EmmaX and "EmmaYes" in Player.Traits):
                        $ character.Statup("Love", 200, 30)

                        "[character.Name] wraps her arms around you and starts kissing you passionately."

                        $ character.FaceChange("kiss")

                        call girl_kissing_launch(character, "kiss you")

                        $ character.Kissed += 1
                    "She wouldn't understand." if len(Player.Harem) == 1:
                        $ Line = "no."
                    "They wouldn't be cool with that." if len(Player.Harem) > 1:
                        $ Line = "no."
                    "I'm sorry, but. . . no." if character.Event[5] != 20:
                        $ Line = "no."
                    "No way.":
                        call girl_boyfriend_jerk_ending(character)

                if Line == "no":
                    $ character.Statup("Love", 200, -10)

                    if character == RogueX:
                        ch_r "I get it. That's fine."
                    elif character == KittyX:
                        ch_k "Well. . . okay. I get it."
                    elif character == EmmaX:
                        ch_e "Well. . ."
                        ch_e "I suppose I understand."

                    $ character.Event[5] = 20

                    call Remove_Girl(character)

                    $ Line = 0

                    return
            "Not really.":
                call girl_boyfriend_jerk_ending(character)

        $ character.Petnames.append("boyfriend")
    elif character == LauraX:
        $ character.FaceChange("angry", 1, Eyes = "side")

        $ Line = 0

        ch_l "Hey. So. [character.Petname]. . ."

        $ character.FaceChange("confused",1,Mouth="lipbite")

        ch_l "I don't know- . . . you're pretty fun to hang out with, ya know?"

        menu:
            extend ""
            "I really love hanging out with you too!":
                $ character.FaceChange("surprised",2)

                ch_l "Right, so-"

                $ character.Statup("Obed", 50, -3)
                $ character.Statup("Inbt", 80, 1)

                ch_l ". . ."

                $ character.Statup("Love", 200, 5)
                $ character.FaceChange("bemused",1,Eyes="side")

                ch_l "\"Love\" is kind of a strong word, [character.Petname]."
            "Yeah, sure, it's a lot of fun.":
                $ character.Statup("Love", 200, 10)
                $ character.Statup("Inbt", 80, 2)
                $ character.FaceChange("smile",0)

                ch_l "Right?"
            "I mean, it beats math class. . .":
                $ character.Statup("Love", 200, 3)
                $ character.Statup("Obed", 80, 3)
                $ character.Statup("Inbt", 80, -3)
                $ character.FaceChange("angry",1)

                ch_l "Um, less enthusiasm than I was expecting. . ."
            "If you say so.":
                $ character.Statup("Obed", 80, 6)
                $ character.Statup("Inbt", 80, -8)
                $ character.FaceChange("confused",1)

                ch_l ". . ."

        ch_l "So like I was saying, I don't exactly have a ton of friends."
        $ character.FaceChange("sadside",1)
        ch_l "I kind of grew up in a rough place, and then spent a lot of time on the road."
        ch_l "I had a life before coming here."

        menu:
            extend ""
            "What was it like?":
                $ character.Statup("Love", 200, 7)
                $ character.Statup("Obed", 80, 2)
                $ character.Statup("Inbt", 80, 3)
                $ character.FaceChange("sad",1,Mouth="lipbite")
            "Yeah? I know.":
                $ character.Statup("Love", 200, 3)
                $ character.Statup("Obed", 80, 4)
                $ character.Statup("Inbt", 80, 1)
                $ character.FaceChange("confused",1,Mouth="lipbite")
            "I don't need a lot of backstory drama.":
                $ character.Statup("Love", 200, -5)
                $ character.Statup("Obed", 80, 10)
                $ character.Statup("Inbt", 80, -5)
                $ character.FaceChange("angry",1)

                $ Line = "bad"

                ch_l "Fine!"
                ch_l "\"Keep it simple\" it is then."
                ch_l "I don't hate hanging out with you, is all."

        if Line != "bad":
            $ character.FaceChange("normal",1,Eyes="side")
            ch_l "Well, you may have guessed I'm related to Wolverine."

            menu:
                extend ""
                "Kinda obvious, yeah.":
                    $ character.Statup("Love", 200, 4)
                "I had no idea!":
                    $ character.Statup("Love", 200, 3)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.FaceChange("confused",1)
                "Duh.":
                    $ character.Statup("Love", 200, 1)
                    $ character.Statup("Obed", 80, 2)
                    $ character.FaceChange("angry",1)

            ch_l "Well I'm actually his partial clone."

            $ character.FaceChange("angry",1,Eyes="side")

            ch_l "I was created to be some sort of biological weapon, an assassin."
            ch_l "I did a lot of work for them as a kid, until eventually I escaped."

            $ character.FaceChange("sadside",1)

            ch_l "After that, I had to do a lot of stuff. . . to stay alive."
            ch_l "Stuff I'm not proud of."

            $ character.FaceChange("sad",1)

            ch_l "But I don't know. . . being around you, I think it helps."

            $ character.FaceChange("sad",1,Mouth="smile")

            ch_l "I kind of feel. . . better."

        if character.SEXP >= 20:
            $ character.Statup("Obed", 80, 3)
            $ character.Statup("Inbt", 80, 2)
            $ character.Statup("Lust", 80, 5)
            $ character.FaceChange("sly",1)

            ch_l "You really are good in bed, after all."

        if len(Player.Harem) >= 2:
            ch_l "And I know that you have your share of other girls. . ."
            ch_l ". . . but I'd still like to be a part of your life."
        elif Player.Harem:
            ch_l "And I know you're with someone else. . ."
            ch_l ". . . but I'd still like to be a part of your life."
        else:
            ch_l "I'd just like to be a part of your life."

        $ character.FaceChange("sad",1,Mouth="smile")

        ch_l "That's it."

        $ character.Event[5] += 1

        menu:
            extend ""
            "Yeah! I really love you.":
                $ character.Statup("Love", 200, -3)
                $ character.Statup("Obed", 80, -3)
                $ character.Statup("Inbt", 80, 3)
                $ character.FaceChange("surprised",1)

                ch_l "Whoa!"

                $ character.FaceChange("perplexed")

                ch_l "Maybe cool your jets there, [character.Petname]."

                $ character.FaceChange("smile",Eyes="side")

                ch_l "I wasn't. . ."
                ch_l "I don't think we're there. . ."

                $ character.FaceChange("perplexed",1)

                ch_l "Right?"

                menu:
                    extend ""
                    "Maybe you aren't.":
                        $ character.Statup("Love", 200, 10)
                        $ character.Statup("Obed", 80, 5)
                        $ character.Statup("Inbt", 80, 5)
                        $ character.Statup("Lust", 80, 2)
                        $ character.FaceChange("smile",1,Eyes="side")

                        ch_l "Hehe. . . um."
                    "I guess, sure.":
                        $ character.Statup("Love", 200, 6)
                        $ character.Statup("Obed", 80, 3)
                        $ character.Statup("Inbt", 80, 2)
                        $ character.FaceChange("angry",1,Eyes="side",Mouth="lipbite")

                        ch_l "Right, so. . ."
            "Yeah, I think that'd be great.":
                $ character.Statup("Love", 200, 6)
                $ character.Statup("Obed", 80, 2)
                $ character.Statup("Inbt", 80, 3)
                $ character.FaceChange("smile",1,Eyes="side")

                ch_l "Cool."
            "Hmm? Ok.":
                $ character.Statup("Love", 80, 3)
                $ character.Statup("Obed", 80, 5)
                $ character.Statup("Inbt", 80, 3)
                $ character.FaceChange("confused",1,Eyes="side")

                ch_l "Yeah. . . cool."
            "I'm not really into that.":
                $ character.Statup("Love", 200, -5)
                $ character.Statup("Obed", 80, 5)
                $ character.Statup("Inbt", 80, -5)
                $ character.FaceChange("sad",1)

                if len(Player.Harem) >= 2:
                    ch_l "Is it because of [Player.Harem[0].Name] and the rest?"
                elif Player.Harem:
                    ch_l "Is it because of [Player.Harem[0].Name]?"
                else:
                    ch_l "Why not? What's the deal?"

                menu:
                    extend ""
                    "Yeah, I don't think she'd understand." if len(Player.Harem) == 1:
                        $ character.Statup("Love", 200, -5)
                        $ character.Statup("Obed", 80, 7)
                        $ character.FaceChange("angry",1,Eyes="side")
                        $ character.GLG(Player.Harem[0],800,-20,1)

                        ch_l "That bitch."
                    "They wouldn't be cool with that." if len(Player.Harem) > 1:
                        $ character.Statup("Love", 200, -5)
                        $ character.Statup("Obed", 80, 7)
                        $ character.FaceChange("angry",1,Eyes="side")

                        call HaremStatup(character,700,-20) #lowers like of all Harem girls by 10

                        ch_l "Bitches."
                    "It's. . . complicated.":
                        $ character.Statup("Love", 200, -20)
                        $ character.Statup("Obed", 80, 8)
                        $ character.Statup("Inbt", 80, -5)
                        $ character.FaceChange("angry",1)

                        ch_l "Complicated. Sure. Whatever."

                        $ character.FaceChange("angry",1,Eyes="side")

                        if len(Player.Harem) >= 2:
                            ch_l "Probably those bitches."

                            call HaremStatup(character,700,-10) #lowers like of all Harem girls by 10
                        elif Player.Harem:
                            ch_l "Probably because of her."

                            $ character.GLG(Player.Harem[0],800,-20,1)

                        $ Line = "no"
                    "I'm just not into you like that.":
                        $ character.Statup("Love", 200, -10)
                        $ character.FaceChange("surprised",1)

                        ch_l "Oh."

                        $ character.Statup("Obed", 80, 10)
                        $ character.Statup("Inbt", 80, 5)
                        $ character.FaceChange("sadside",1)

                        ch_l "Ok, I guess I can respect that."

                $ character.FaceChange("sad",1)

                if Line != "no":
                    ch_l "We're still cool though."

                ch_l "I should. . . leave."
                "[character.Name] wanders off in a bit of a daze."

                $ character.Event[5] = 20

                call Remove_Girl(character)
                $ Line = 0

                return

        if Player.Harem:
            if not ApprovalCheck(character, 1400):
                if len(Player.Harem) >= 2:
                    ch_l "So you'll break up with the others?"
                else:
                    ch_l "So you'll break up with [Player.Harem[0].Name]?"

                menu:
                    extend ""
                    "Yes, you're worth it.":
                        $ character.Statup("Love", 200, 20)
                        $ character.Statup("Obed", 80, 5)
                        $ character.Statup("Inbt", 80, 5)
                        $ character.FaceChange("surprised",2,Mouth="smile")

                        ch_l ". . ."

                        $ character.FaceChange("smile",1)

                        # fix, I need to add code here to initiate breakups with the rest. . .

                        $ character.Event[5] = 10
                    "I'd rather you join us.":
                        $ Line = 0
                        if ApprovalCheck(character, 1200):
                            $ BO = Player.Harem[:]

                            while BO and Line != "no":
                                if character.GirlLikeCheck(BO[0]) <= 500:
                                    $ Line = "no"

                                $ BO.remove(BO[0])
                        else:
                            $ Line = "no"

                        if Line == "no":
                            $ character.Statup("Love", 200, -10)
                            $ character.Statup("Obed", 80, 10)
                            $ character.FaceChange("angry",1)

                            call HaremStatup(character,700,-10)

                            ch_l "Eh, I'll pass."
                        else:
                            $ character.Statup("Love", 200,5)
                            $ character.Statup("Obed", 80, 15)
                            $ character.Statup("Inbt", 80, 10)
                            $ character.FaceChange("bemused",1)

                            ch_l "Well, I s'pose that wouldn't be so terrible."
                    "What? Of course not.":
                        $ character.Statup("Love", 200, -25)
                        $ character.Statup("Obed", 80, 5)

                        call HaremStatup(character,700,-20)

                        $ character.FaceChange("angry",1)

                        ch_l "Well, fine then."

                        $ Line = "no"
                if Line == "no":
                    $ character.Event[5] = 20

                    call Remove_Girl(character)
                    $ Line = 0

                    return

            if len(Player.Harem) >= 2:
                ch_l "And you don't think the others would mind?"
            else:
                ch_l "And you don't think [Player.Harem[0].Name] would mind?"
            menu:
                extend ""
                "No, actually they're fine with it." if "LauraYes" in Player.Traits:
                    $ character.Statup("Love", 200, 5)
                    $ character.Statup("Obed", 80, 10)
                    $ character.Statup("Inbt", 80, 5)
                    $ character.FaceChange("surprised",1)

                    ch_l "Oh, cool."
                "Actually. . . I guess we'll need to work on that one." if "LauraYes" not in Player.Traits:
                    $ character.Statup("Love", 200, 3)
                    $ character.Statup("Obed", 80, 3)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Lust", 80, 1)
                    $ character.FaceChange("confused",1)

                    ch_l "Hmm, get back to me, I guess?"

                    $ character.Event[5] = 20

                    call Remove_Girl(character)

                    $ Line = 0

                    return

            call HaremStatup(character,900,20)
    elif character == StormX:
        $ character.FaceChange("smile")

        ch_s "[character.Petname]. . . I was hoping that we could talk. . ."

        menu:
            extend ""
            "Yes?":
                pass
            "I'm kinda busy.":
                $ character.FaceChange("sadside")
                $ character.Statup("Love", 90, -5)
                $ character.Statup("Obed", 50, 2)

                ch_s "Then I won't take more of your time than is necessary."

                $ character.FaceChange("grimace")

        $ character.Event[5] = 20

        ch_s "I have been enjoying the time we've spent together."
        ch_s "I mean to say, I have been enjoying you."

        $ character.FaceChange("smile",Eyes="side")

        ch_s ". . ."

        $ character.FaceChange("smile")

        ch_s "May I tell you a story?"

        menu:
            extend ""
            "Sure.":
                pass
            "Can we not?":
                $ character.Statup("Love", 90, -5)
                $ character.Statup("Obed", 50, 3)
                $ character.Statup("Inbt", 70, -2)
                $ character.FaceChange("confused")

                ch_s "I think you will benefit from it."
            "Like I said, I'm really busy here.":
                $ character.FaceChange("sadside")
                $ character.Statup("Love", 90, -5)
                $ character.Statup("Obed", 60, 5)
                $ character.Statup("Inbt", 70, -2)

                ch_s "Then I won't take more of your time."
                ch_s "Let me know when your. . . schedule clears up."

                call Remove_Girl(character)

                $ Player.History.append("story")

                return

        $ character.FaceChange("smile")

        ch_s "When I was a child, I spent a lot of my time alone."
        ch_s "I was abandoned on the streets of Cairo, and had to fend for myself. . ."

        $ character.FaceChange("sadside")

        ch_s ". . . as a pickpocket."
        ch_s "Years later, I travelled south to Kenya, but for so much of my time, I had nobody that I could count on."

        $ character.FaceChange("smile")

        ch_s "Since I have come here, I have learned to value the strong bonds that I have with my teammates."

        if Player.Harem:
            if len(Player.Harem) >= 2:
                ch_s "And I know that you have been sharing your time with other girls,"
            else:
                ch_s "And I know that you have been sharing your time with [Player.Harem[0].Name],"

            if ApprovalCheck(character, 1500):
                $ character.Statup("Obed", 60, 2)
                $ character.Statup("Inbt", 70, 2)

                ch_s ". . . but I can accept that."
            else:
                ch_s ". . . and we can discuss that. . ."

        $ character.FaceChange("sly")

        ch_s "I just want to know that you are there for me too."

        menu:
            extend ""
            "Of course I am.":
                $ character.FaceChange("smile")
                $ character.Statup("Love", 90, 7)
                $ character.Statup("Obed", 60, 2)
                $ character.Statup("Inbt", 70, 2)

                ch_s "That is a relief to hear."
            "I'm not big on commitment. . .":
                $ character.FaceChange("sadside")
                $ character.Statup("Love", 90, -5)
                $ character.Statup("Obed", 60, 5)
                $ character.Statup("Inbt", 70, -2)

                ch_s ". . . that is unfortunate."

                $ character.FaceChange("sad")

                ch_s "Let me know if you should reconsider then."

                call Remove_Girl(character)

                $ Line = 0

                return
            "Well, I guess. . .":
                $ character.FaceChange("sadside")
                $ character.Statup("Love", 90, -3)
                $ character.Statup("Obed", 60, 1)
                $ character.Statup("Inbt", 70, -2)

                ch_s "That is. . . not exactly the answer I was looking for. . ."

        if Player.Harem:
            if ApprovalCheck(character, 1500):
                $ character.FaceChange("sly",Eyes="side")
                $ character.Statup("Obed", 80, 5)
                $ character.Statup("Inbt", 80, 5)

                ch_s "I would be happy to join your little \"harem.\""

                $ character.FaceChange("sly")

                ch_s "If you'll have me."
            else:
                ch_s "I would prefer to be your one and only. . ."
                menu:
                    extend ""
                    "I could break up with them. . ." if len(Player.Harem) >= 2:
                        $ character.FaceChange("smile")
                        $ character.Statup("Love", 90, 10)
                        $ character.Statup("Obed", 60, 5)
                        $ character.Statup("Inbt", 70, 5)

                        ch_s "Excellent!"
                        ch_s "Do let them down gently though. . ."

                        return
                    "I could break up with her. . ." if len(Player.Harem) == 1:
                        $ character.FaceChange("smile")
                        $ character.Statup("Love", 90, 10)
                        $ character.Statup("Obed", 60, 5)
                        $ character.Statup("Inbt", 70, 5)

                        ch_s "Excellent!"
                        ch_s "Do let her down gently though. . ."

                        return
                    "I can't do that.":
                        $ character.FaceChange("sadside")
                        $ character.Statup("Love", 90, -5)
                        $ character.Statup("Obed", 60, 5)
                        $ character.Statup("Obed", 80, 5)
                        $ character.Statup("Inbt", 70, -3)

                        ch_s ". . .oh."
                        ch_s "Well that is a disappointment."

                        if not ApprovalCheck(character, 1000):
                            ch_s "I suppose that will be all then."

                            $ character.Event[5] = 20

                            call Remove_Girl(character)

                            $ Line = 0

                            return
                        else:
                            $ character.Statup("Obed", 80, 5)
                            $ character.Statup("Inbt", 60, 3)
                            $ character.Statup("Inbt", 70, 2)

                            ch_s ". . . I suppose that I could accept this. . . arrangement."
            menu:
                extend ""
                "I would love that!" if "StormYes" in Player.Traits:
                    $ character.Statup("Love", 90, 20)
                    $ character.Statup("Inbt", 70, 5)

                    ch_s "Excellent!"
                "I would love that. . . but. . ." if "StormYes" not in Player.Traits:
                    $ character.FaceChange("confused")
                    $ character.Statup("Love", 90, 5)
                    $ character.Statup("Obed", 60, 5)

                    ch_s ". . . but?"

                    if len(Player.Harem) >= 2:
                        ch_p "The others weren't into that. . ."
                    else:
                        ch_p "[Player.Harem[0].Name] wasn't into that. . ."

                    $ character.FaceChange("sadside")

                    ch_s ". . .oh."
                    ch_s "Well that is a disappointment."
                    ch_s "Let me know if the situation. . . clears up."

                    $ character.Event[5] = 20

                    call Remove_Girl(character)

                    $ Line = 0

                    return
                "No thanks.":
                    $ character.FaceChange("sadside")
                    $ character.Statup("Love", 90, -25)
                    $ character.Statup("Obed", 60, 10)

                    ch_s ". . .oh."
                    ch_s "Very well then."
                    ch_s "I will take no more of your time."

                    call Remove_Girl(character)

                    $ Line = 0

                    return
        else:
            ch_s "So would you mind if I considered you my. . . \"boyfriend?\""
            menu:
                extend ""
                "I'd love that!":
                    $ character.Statup("Love", 90, 20)
                    $ character.Statup("Inbt", 70, 5)
                    $ character.FaceChange("smile")
                    ch_s "Excellent!"
                "I'd rather you didn't.":
                    $ character.Statup("Love", 90, -20)
                    $ character.Statup("Obed", 50, 5)
                    $ character.Statup("Obed", 70, 5)
                    $ character.FaceChange("sadside")

                    ch_s ". . .oh."
                    ch_s "Well that is a disappointment."

                    call Remove_Girl(character)

                    $ Line = 0

                    return
                "Suit yourself.":
                    $ character.Statup("Love", 90, -5)

                    if ApprovalCheck(character, 1000):
                        $ character.FaceChange("confused")
                        $ character.Statup("Obed", 50, 5)
                        $ character.Statup("Obed", 80, 5)

                        ch_s ". . .very well then. I shall do that. . ."
                    else:
                        $ character.FaceChange("sadside")
                        $ character.Statup("Obed", 60, 5)

                        ch_s ". . . that was not the reaction I had expected. . ."
                        ch_s "Perhaps I should give this further consideration. . ."

                        call Remove_Girl(character)

                        $ Line = 0

                        return

    if "Historia" not in Player.Traits:
        $ Player.Harem.append(character)

        if character == RogueX:
            if "RogueYes" in Player.Traits:
                $ Player.Traits.remove("RogueYes")
        elif character == KittyX:
            if "KittyYes" in Player.Traits:
                $ Player.Traits.remove("KittyYes")
        elif character == EmmaX:
            if "EmmaYes" in Player.Traits:
                $ Player.Traits.remove("EmmaYes")
        elif character == LauraX:
            if "LauraYes" in Player.Traits:
                $ Player.Traits.remove("LauraYes")
        elif character == StormX:
            if "StormYes" in Player.Traits:
                    $ Player.Traits.remove("StormYes")

        call Harem_Initiation

    $ character.FaceChange("sexy")

    if character == RogueX:
        ch_r "Now, . . . boyfriend. . . how would you like to celebrate?"
    elif character == KittyX:
        ch_k "Now. . . boyfriend. . . how about you and I[character.like]celebrate, huh?"
    elif character == EmmaX:
        ch_e "So then. . . how would you like to celebrate?"
    elif character == LauraX:
        $ character.Statup("Love", 200, 3)
        $ character.Statup("Obed", 80, 3)
        $ character.Statup("Inbt", 80, 1)
        $ character.Statup("Lust", 80, 1)
        $ character.FaceChange("sly",1)

        ch_l "So, did you have any plans for the next few minutes? . ."

    if "Historia" in Player.Traits:
        return 1

    $ temp_modifier = 10

    call girl_sex_menu(character)

    $ temp_modifier = 0

    return

label girl_boyfriend_jerk_ending(character):
    $ character.FaceChange("angry", 1)

    if character == RogueX:
        ch_r "Well fine!"

        $ Count = (20*character.Event[5])
    elif character == KittyX:
        ch_k "Fine![KittyX.Like]. . .be that way!"
    elif character == EmmaX:
        ch_e "Well! Suit yourself."

    $ character.Statup("Obed", 50, 40)

    if character.Event[5] != 20:
        $ character.Statup("Obed", 200, (20*character.Event[5]))
    if 20 > character.Event[5] >= 3:
        $ character.FaceChange("sad")

        if character == RogueX:
            ch_r "Hrmph. I don't care what you want, we're dating. Deal with it."
            ch_r "Now I need some alone time though."
        elif character == KittyX:
            ch_k "Yeah? Well. . .[character.like]I don’t care what you want! We’re dating! Deal."
            ch_k "I. . .uhm. . .think I need to[character.like]be alone for a little while."
        elif character == EmmaX:
            ch_e "You know, I'm tired of caring what you think about the matter."
            ch_e "I'm doing to consider us a couple whether you approve or not."
            ch_e "And with that, adieu."

        if "Historia" in Player.Traits:
            return 1

        $ character.Petnames.append("boyfriend")

        $ Achievements.append("I am not your Boyfriend!")

        $ bg_current = "bg player"

        call Remove_Girl(character)
        call Set_The_Scene
        $ renpy.pop_call()
        jump Player_Room

        return

    if character.Event[5] > 1:
        if character == RogueX:
            ch_r "I don't know why I keep asking, I should know you haven't changed."
        elif character == KittyX:
            ch_k "It was such a mistake asking you again.  You’re[KittyX.like]still such a jerk!"
        elif character == EmmaX:
            ch_e "It was such a mistake asking you again.  You still need to mature."

    if character.Event[5] != 20:
        $ character.Statup("Love", 200, -(50*character.Event[5]))
    else:
        $ character.Statup("Love", 200, -50)

    if bg_current == character.Home:
        if character == RogueX:
            ch_r "Jerk! Out!"
        elif character == KittyX:
            ch_k "Get out, you big jerk!"
        elif character == EmmaX:
            ch_e "Get away from me."

        $ bg_current = "bg player"
        call Remove_Girl(character)
        call Set_The_Scene
        $ renpy.pop_call()
        jump Player_Room
    else:
        "[character.Name] storms off."

        call Remove_Girl(character)
        call Set_The_Scene
        $ renpy.pop_call()

    if "Historia" in Player.Traits:
        return 1

label girl_daddy(character):
    $ character.DailyActions.append("relationship")

    if character != JeanX:
        $ character.DrainWord("asked meet")

    call Shift_Focus(character)
    call Set_The_Scene

    if character == RogueX:
        ch_r ". . ."
    elif character == KittyX:
        ch_k ". . ."
    elif character == EmmaX:
        ch_e ". . ."
    elif character == LauraX:
        ch_l ". . ."
    elif character == JeanX:
        ch_j ". . ."
    elif character == StormX:
        ch_s ". . ."

        $ Line = 0
        $ Options = TotalGirls[:]

        while Options:
            if "daddy" == Options[0].Petname:
                $ Line = 2
            elif "daddy" in Options[0].Petnames:
                $ Line = 1 if not Line else Line

            $ Options.remove(Options[0])
    elif character == JubesX:
        ch_v ". . ."

    if character in Player.Harem:
        if character == RogueX:
            ch_r "You know, even though we've been dating,"
        elif character == KittyX:
            ch_k "Hey, so[KittyX.like]we've been dating,"
        elif character == EmmaX:
            ch_e "We have been dating a while, [EmmaX.Petname],"
        elif character == LauraX:
            ch_l "So we've been dating a while yeah?"
        elif character == JeanX:
            ch_j "Ok, so I know we're dating. . ."
        elif character == StormX:
            ch_s "I have been talking with the other girls. . ."
        elif character == JubesX:
            ch_v "So we've been dating a while yeah?"
    else:
        if character == RogueX:
            ch_r "Even though we've been hanging out,"
        elif character == KittyX:
            ch_k "Hey, so[KittyX.like]we've been hanging out,"
        elif character == EmmaX:
            ch_e "We have been enjoying ourselves,"
        elif character == LauraX:
            ch_l "This thing we've got, pretty fun, right?"
        elif character == JeanX:
            ch_j "You. . . like me, right?"
        elif character == StormX:
            ch_s "I have heard something among the students. . ."
        elif character == JubesX:
            ch_v "This thing we've got, pretty fun, right?"

    if character != StormX:
        if character.Love > character.Obed and character.Love > character.Inbt:
            if character == RogueX:
                ch_r "and you're really sweet to me. . ."
            elif character == KittyX:
                ch_k "and you're so sweet. . ."
            elif character == EmmaX:
                ch_e "and you certainly are sweet. . ."
            elif character == LauraX:
                ch_l "and you've been really kind to me. . ."
            elif character == JeanX:
                ch_j "and I've really been warming up to this. . ."
            elif character == JubesX:
                ch_v "and you've been really kind to me. . ."
        elif character.Obed > character.Inbt:
            if character == RogueX:
                ch_r "and you know what I need. . ."
            elif character == KittyX:
                ch_k "and you give me what I need. . ."
            elif character == EmmaX:
                ch_e "and you know how to keep me interested. . ."
            elif character == LauraX:
                ch_l "and you've been a good influence. . ."
            elif character == JeanX:
                ch_j "I. . . \"respect\" you? . ."
            elif character == JubesX:
                ch_v "and you've been a good influence. . ."
        else:
            if character == RogueX:
                ch_r "and I've really been spreading my wings. . ."
            elif character == KittyX:
                ch_k "and I've been trying out new things. . ."
            elif character == EmmaX:
                ch_e "and I've been. . . exploring. . ."
            elif character == LauraX:
                ch_l "like, really fun. . ."
            elif character == JeanX:
                ch_j "and this is fun. . ."
            elif character == JubesX:
                ch_v "like, really fun. . ."

        if character == RogueX:
            ch_r "So I was thinking, could I call you \"daddy?\""
        elif character == KittyX:
            ch_k "So[KittyX.like]I was thinking, could I call you. . . \"daddy?\""
        elif character == EmmaX:
            ch_e "I was thinking, would you mind if I call you \"daddy?\""
        elif character == LauraX:
            ch_l "So I've been thinking, would you want to be called. . ."
            ch_l "\"daddy?\""
        elif character == JeanX:
            ch_j "I've been thinking, you know what would be totally hot? . ."
            ch_j "What if I called you. . . \"daddy?\""
        elif character == JubesX:
            ch_v "So I've been thinking, would you want to be called. . ."
            ch_v "\"daddy?\""

        menu:
            extend ""
            "Ok, go right ahead?":
                $ character.FaceChange("smile")
                $ character.Statup("Obed", 60, 10)
                $ character.Statup("Inbt", 80, 30)

                if character in [RogueX, EmmaX, LauraX, JeanX, JubesX]:
                    $ character.Statup("Love", 90, 20)
                elif character in [KittyX]:
                    $ character.Statup("Love", 90, 25)

                if character == RogueX:
                    ch_r "Squee!"
                elif character == KittyX:
                    ch_r "Great!"
                elif character == EmmaX:
                    ch_e "Excellent."
                elif character == LauraX:
                    ch_l "Cool."
                elif character == JeanX:
                    ch_j "Cool."
                elif character == JubesX:
                    ch_v "Cool."

                $ character.Petname = "daddy"
            "What do you mean by that?":
                $ character.FaceChange("bemused")

                if character == RogueX:
                    ch_r "I just sort of get turned on by it, you know, being your baby girl. . ."
                    ch_r "I'd like to call you that."
                elif character == KittyX:
                    ch_k "I don't know, it'd kinda be hot, being your baby girl. . ."
                    ch_k "Could'ya call me that?"
                elif character == EmmaX:
                    ch_e "I just find it to be a turn-on, being your baby girl. . ."
                    ch_e "I'd prefer to call you that sometimes."
                elif character == LauraX:
                    ch_l "I don't know, I've had some shitty father figures. . ."
                    ch_l "I just. . ."
                    if character.Love > character.Obed and character.Love > character.Inbt:
                        ch_l "I think you could do better. . ."
                    elif character.Obed > character.Inbt:
                        ch_l "you've really been assertive. . ."
                    else:
                        ch_l "wouldn't it be kinky?"
                elif character == JeanX:
                    ch_j "It's just kinda kinky, right. . ."
                    ch_j "\"Daddy?\""
                elif character == JubesX:
                    ch_v "I don't know, I've had some shitty father figures. . ."
                    ch_v "I just. . ."
                    if character.Love > character.Obed and character.Love > character.Inbt:
                        ch_v "I think you could do better. . ."
                    elif character.Obed > character.Inbt:
                        ch_v "you've really been assertive. . ."
                    else:
                        ch_v "wouldn't it be kinky?"

                menu:
                    extend ""
                    "Sounds interesting, fine by me.":
                        $ character.FaceChange("smile")
                        $ character.Statup("Obed", 60, 20)
                        $ character.Statup("Inbt", 80, 25)

                        if character != KittyX:
                            $ character.Statup("Love", 90, 15)

                        if character == RogueX:
                            ch_r "Great! . . daddy."
                        elif character == KittyX:
                            $ character.Statup("Love", 90, 17)

                            ch_k "Nice! . . daddy."
                        elif character == EmmaX:
                            ch_e "Great!"

                            $ character.FaceChange("sly",2)

                            ch_e " . . . daddy."

                            $ character.FaceChange("sly",1)
                        elif character == LauraX:
                            ch_l "Great!"

                            $ character.FaceChange("sly",2)

                            ch_l " . . . daddy."

                            $ character.FaceChange("sly",1)
                        elif character == JeanX:
                            ch_j "Nice."

                            $ character.FaceChange("sly",2)

                            ch_j " . . . daddy."

                            $ character.FaceChange("sly",1)
                        elif character == JubesX:
                            ch_v "Great!"

                            $ character.FaceChange("sly",2)

                            ch_v " . . . daddy."

                            $ character.FaceChange("sly",1)

                        $ character.Petname = "daddy"
                    "Could you not, please?":
                        $ character.Statup("Obed", 80, 40)
                        $ character.Statup("Inbt", 80, 20)

                        if character != JeanX:
                            $ character.FaceChange("sad")

                        if character != KittyX:
                            $ character.Statup("Love", 90, 5)

                        if character == RogueX:
                            ch_r "   . . .   "
                            ch_r "Well, ok."
                        elif character == KittyX:
                            ch_k "   . . .   "
                            ch_k "Huh. K."
                        elif character == EmmaX:
                            ch_e "   . . .   "
                            ch_e "Well, ok."
                        elif character == LauraX:
                            ch_l "   . . .   "
                            ch_l "Well, ok."
                        elif character == JeanX:
                            $ character.FaceChange("angry", 2)

                            ch_j "   . . .   "
                            ch_j "Fine, be that way!"

                            $ character.FaceChange("angry", 1, Eyes = "side")
                        elif character == JubesX:
                            ch_v "   . . .   "
                            ch_v "Well, ok."
                    "No, that creeps me out." if character in [RogueX, KittyX]:
                        $ character.Statup("Obed", 80, 45)
                        $ character.Statup("Inbt", 70, 5)
                        $ character.FaceChange("angry")

                        if character in [RogueX]:
                            $ character.Statup("Love", 90, -10)
                        elif character in [KittyX]:
                            $ character.Statup("Love", 90, -15)

                        if character == RogueX:
                            ch_r "Hrmph."
                        elif character == KittyX:
                            ch_r "Booo."
                    "You've got some real daddy issues, huh?" if character in [EmmaX, LauraX, JeanX, JubesX]:
                        $ character.Statup("Love", 90, -15)
                        $ character.Statup("Obed", 80, 45)
                        $ character.Statup("Inbt", 70, 5)

                        if character != JeanX:
                            $ character.FaceChange("angry")

                        if character == EmmaX:
                            ch_e "Let's not get into it."
                        elif character == LauraX:
                            ch_l "Yes. . . I said that."
                        elif character == JeanX:
                            $ character.FaceChange("angry",2)

                            ch_j "Oh, whatever, like you know!"

                            $ character.FaceChange("angry",1,Eyes="side")
                        elif character == JubesX:
                            ch_j "Yes. . . I said that."
            "No, that creeps me out." if character in [RogueX, KittyX]:
                $ character.Statup("Obed", 80, 40)
                $ character.Statup("Inbt", 70, 10)
                $ character.FaceChange("angry")

                if character == RogueX:
                    $ character.Statup("Love", 90, -5)

                    ch_r "Hrmph."
                elif character == KittyX:
                    $ character.Statup("Love", 90, -10)

                    ch_r "Hrmph."
            "Aren't you a bit old for that?" if character in [EmmaX]:
                $ character.Statup("Love", 90, -15)
                $ character.Statup("Obed", 80, 40)
                $ character.Statup("Inbt", 70, 10)
                $ character.FaceChange("angry")

                if character == EmmaX:
                    ch_e "Perhaps this was a bad idea."
            "You've got some real daddy issues, uh?" if character in [LauraX, JeanX, JubesX]:
                $ character.Statup("Love", 90, -15)
                $ character.Statup("Obed", 80, 45)
                $ character.Statup("Inbt", 70, 5)

                if character != JeanX:
                    $ character.FaceChange("angry")

                if character == LauraX:
                    ch_l ". . . Probably."
                    ch_l "Never mind."
                elif character == JeanX:
                    $ character.FaceChange("angry",2)

                    ch_j "Oh, whatever, like you know!"

                    $ character.FaceChange("angry",1,Eyes="side")
                elif character == JubesX:
                    ch_v ". . . Probably."
                    ch_v "Never mind."
    else:
        if Line:
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

        $ Line = 1

        while Line:
            menu:
                extend ""
                "Did you want me to call you that?" if "callyouthat" not in character.RecentActions:
                    $ character.Statup("Love", 70, 1)
                    $ character.Statup("Inbt", 90, 2)

                    ch_s ". . ."

                    $ character.Statup("Love", 95, 2)
                    $ character.Statup("Inbt", 70, 1)

                    ch_s "I suppose that I did. . ."

                    $ character.RecentActions.append("callyouthat")
                "I guess you could. . ." if "callyouthat" in character.RecentActions or "whycare" in character.RecentActions:
                    $ character.Statup("Love", 70, 2)
                    $ character.Statup("Obed", 200, 5)
                    $ character.Statup("Inbt", 70, 1)

                    ch_s ". . ."

                    $ character.Statup("Love", 200, 5)
                    $ character.Statup("Inbt", 90, 3)

                    ch_s "Certainly. . . Daddy."

                    $ Line = 0
                "Call me \"Daddy.\"":
                    $ character.Statup("Love", 90, 2)
                    $ character.Statup("Obed", 80, 3)

                    ch_s ". . ."

                    $ character.Statup("Obed", 200, 5)
                    $ character.Statup("Inbt", 90, 2)
                    $ character.Statup("Lust", 90, 3)

                    ch_s "Certainly. . . Daddy."

                    $ Line = 0
                "Why do you care?" if "whycare" not in character.RecentActions:
                    $ character.Statup("Love", 90, 2)
                    $ character.Statup("Obed", 80, -1)
                    $ character.Statup("Inbt", 90, -1)

                    ch_s "Oh, well, I was thinking that I could. . ."

                    $ character.RecentActions.append("whycare")
                "It's weird, right?":
                    $ character.Statup("Love", 90, -3)
                    $ character.Statup("Obed", 90, -5)
                    $ character.Statup("Inbt", 90, -15)

                    ch_s "Oh. . . "
                    ch_s ". . . I suppose that it is."
                    ch_s "Never mind. . ."

                    call Remove_Girl(character)

                    $ Line = 0
                "I'd rather not." if "callyouthat" in character.RecentActions or "whycare" in character.RecentActions:
                    $ character.Statup("Love", 90, -2)
                    $ character.Statup("Obed", 90, 3)
                    $ character.Statup("Inbt", 90, -5)

                    ch_s "Oh. . . "
                    ch_s ". . . I suppose that is fine."
                    ch_s "Never mind. . ."

                    call Remove_Girl(character)

                    $ Line = 0

    $ character.Petnames.append("daddy")

    return

label first_topless(character, silent = 0, temporary_line = 0): #rkeljsv
    if character.ChestNum() > 1 or character.OverNum() > 2 and not temporary_line:
        return

    if character.Loc != bg_current and "phonesex" not in Player.RecentActions:
        return

    $ character.RecentActions.append("topless")
    $ character.DailyActions.append("topless")
    $ character.DrainWord("no topless")
    $ character.SeenChest += 1

    if character.SeenChest > 1:
        return

    if character == RogueX:
        $ character.Statup("Inbt", 70, 20)
    elif character in [KittyX, EmmaX, LauraX, JeanX]:
        $ character.Statup("Inbt", 70, 15)

    if not silent:
        if character == RogueX:
            $ character.FaceChange("bemused", 1)

            "[character.Name] looks a bit shy, and slowly lowers her hands from her chest."
            character.voice "Well, [character.Petname]? Like what you see?"

            $ disappointed_line = "Well, they aren't that bad. . ."
        elif character == KittyX:
            $ character.FaceChange("bemused", 2)

            "[character.Name] looks a bit shy, and slowly lowers her hands from her chest."
            character.voice "[character.Like]what do you think?"

            $character.Blush = 1

            $ disapointed_line = "That's it?"
        elif character in [EmmaX, LauraX, JeanX, JubesX]:
            $ character.FaceChange("sly")

            "You get your first look at [character.Name]'s bare chest."

            if character == EmmaX:
                character.voice "Well, [character.Petname]? Is it everything you dreamed?"
            elif character == LauraX:
                ch_l "So? What are you looking at?"
            elif character == JeanX:
                ch_j "So, pretty spectacular, right?"
            elif character == JubesX:
                ch_v "So. . . um. . . like what you see?"

            $ character.Blush = 1

            $ disappointed_line = "Huh, not what I was expecting. . ."

        menu:
            extend ""
            "Nod" if character in [RogueX]:
                $ character.Statup("Love", 90, 20)
                $ character.Statup("Inbt", 70, 20)

                if character == RogueX:
                    $ character.FaceChange("smile")

                character.voice ". . ."

                $ character.Statup("Love", 40, 20)
            "Lovely." if character in [KittyX]:
                $ character.Statup("Love", 90, 20)
                $ character.Statup("Inbt", 70, 20)

                if character == KittyX:
                    $ character.FaceChange("smile", 2)

                character.voice ". . ."

                $ character.Statup("Love", 40, 20)

                if character == KittyX:
                    $ character.Blush = 1
            "Whatever." if character in [RogueX]:
                $ character.Statup("Love", 90, -30)
                $ character.Statup("Obed", 50, 20)
                $ character.Statup("Inbt", 70, -10)
                $ character.FaceChange("angry")

                if character == RogueX:
                    ch_r "Hmph!"

                $ character.Statup("Obed", 70, 20)
            "Definitely, and more." if character in [EmmaX]:
                $ character.Statup("Love", 90, 20)
                $ character.Statup("Inbt", 70, 20)
                $ character.FaceChange("smile",1)

                ch_e "I do aim to impress."

                $ character.Statup("Love", 40, 20)
                $ character.Blush = 0
            "Your tits? They look great." if character in [LauraX, JubesX]:
                $ character.Statup("Love", 90, 20)
                $ character.Statup("Inbt", 70, 20)

                if character == LauraX:
                    $ character.FaceChange("sexy",1,Eyes="down")

                    ch_l "Huh. I mean I guess so. . ."

                    $ character.FaceChange("smile",0)
                elif character == JubesX:
                    $ character.FaceChange("smile",2)

                    pause 0.5

                    $ character.FaceChange("sexy",1,Eyes="down")

                    ch_v "Ah! Um. . . yeah, I guess. . ."

                    $ character.FaceChange("smile")

                $ character.Statup("Love", 40, 20)
            "Yeah, they look amazing." if character in [JeanX]:
                $ JeanX.Statup("Love", 90, 10)
                $ JeanX.Statup("Inbt", 200, 20)
                $ JeanX.FaceChange("sexy",1,Eyes="down")

                ch_j "Yeah, they are pretty tight. . ."

                $ JeanX.FaceChange("smile",0)
                $ JeanX.Statup("Obed", 40, 20)
            ". . . [[stunned]]" if character in [EmmaX, LauraX, JeanX, JubesX]:
                if character == EmmaX:
                    $ character.Statup("Love", 90, 20)
                    $ character.Statup("Inbt", 70, 30)

                    ch_e "Yes, that would be the usual reaction."
                elif character in [LauraX, JubesX]:
                    $ character.Statup("Love", 90, 10)
                    $ character.Statup("Inbt", 70, 10)

                    if character == LauraX:
                        ch_l "Cat got your tongue?"
                    elif character == JubesX:
                        ch_v "Oh, that's a \"hit.\""
                elif character == JeanX:
                    $ character.Statup("Love", 90, 20)
                    $ character.Statup("Inbt", 200, 10)

                    ch_j "Stunning, I know."

                $ character.Statup("Love", 40, 10)
            "[disappointed_line]":
                if character != JeanX:
                    $ character.Statup("Love", 90, -30)
                    $ character.Statup("Obed", 60, 25)
                    $ character.Statup("Inbt", 70, -15)
                    $ character.FaceChange("confused", 2)

                    if character == RogueX:
                        character.voice "Say what now?"
                    elif character == KittyX:
                        character.voice "What?"
                    elif character == EmmaX:
                        character.voice "What?"
                    elif character == LauraX:
                        ch_l "Huh?"
                    elif character == JubesX:
                        ch_v "Wha?"
                else:
                    $ character.Statup("Love", 90, 10)
                    $ character.Statup("Obed", 40, 20)
                    $ character.Statup("Inbt", 200, 20)
                    $ character.FaceChange("smile",0)

                    ch_j "Exactl-{w=0.3}{nw}"

                    $ character.Statup("Love", 90, -40)
                    $ character.Statup("Obed", 60, 10)
                    $ character.Statup("Inbt", 200, -15)
                    $ character.FaceChange("confused",2)

                    ch_j "Exactl- wait, what?"

                    $ temporary_line = 0

                menu:
                    "They're even better than I imagined!" if character in [EmmaX]:
                        $ character.Statup("Love", 90, 20)
                        $ character.Statup("Obed", 60, -20)
                        $ character.Statup("Inbt", 70, 20)
                        $ character.FaceChange("perplexed",1)

                        ch_e "Well, I suppose you managed to salvage that one. . ."
                    "They're really perky!" if character in [LauraX, JeanX, JubesX]:
                        if character in [LauraX, JubesX]:
                            $ character.Statup("Love", 90, 20)
                            $ character.Statup("Obed", 60, -20)
                            $ character.Statup("Inbt", 70, 20)
                            $ character.FaceChange("perplexed",1)

                            character.voice "Oh. Right. . ."
                        elif character == JeanX:
                            $ character.Statup("Love", 90, 10)
                            $ character.Statup("Obed", 60, 10)
                            $ character.Statup("Inbt", 200, 20)
                            $ character.FaceChange("perplexed",1)

                            ch_j "Oh. Of course. . ."
                    "I, um, no, they're great!":
                        $ character.FaceChange("angry", 2, Mouth = "smile")

                        if character != JeanX:
                            $ character.Statup("Inbt", 70, 10)

                        if character == RogueX:
                            ch_r "Of couse they are!"
                        elif character == KittyX:
                            ch_k "Obviously!"
                        elif character == EmmaX:
                            ch_r "Of couse they are!"
                        elif character == LauraX:
                            ch_l "Why wouldn't they be?"
                        elif character == JeanX:
                            $ character.Statup("Obed", 80, 20)

                            ch_j "Of course they are!"
                        elif character == JubesX:
                            ch_v ". . ."
                            ch_v "I -know- that, that's why I was confused?"
                    "[EmmaX.Name]'s were a lot bigger, that's all." if character in [KittyX] and EmmaX.SeenChest:
                        $ temporary_line = EmmaX
                    "[StormX.Name]'s were a lot bigger, that's all." if character in [RogueX, KittyX, LauraX, JeanX, JubesX] and StormX.SeenChest:
                        $ temporary_line = StormX
                    "[RogueX.Name]'s were bigger, that's all." if character in [KittyX] and RogueX.SeenChest:
                        $ temporary_line = RogueX
                    "[EmmaX.Name]'s were bigger, that's all." if character in [RogueX, KittyX, LauraX, JeanX, JubesX] and EmmaX.SeenChest:
                        $ temporary_line = EmmaX
                    "[LauraX.Name]'s were bigger, that's all." if character in [KittyX] and LauraX.SeenChest:
                        $ temporary_line = LauraX
                    "[JeanX.Name]'s were bigger, that's all." if character in [KittyX] and JeanX.SeenChest:
                        $ temporary_line = JeanX
                    "[StormX.Name]'s were bigger, that's all." if character in [RogueX, KittyX, EmmaX, LauraX, JeanX, JubesX] and StormX.SeenChest:
                        $ temporary_line = StormX
                    "[RogueX.Name]'s were nicer, that's all." if character in [LauraX, JeanX, JubesX] and RogueX.SeenChest:
                        $ temporary_line = RogueX
                    "[LauraX.Name]'s were nicer, that's all." if character in [RogueX, JeanX, JubesX] and LauraX.SeenChest:
                        $ temporary_line = LauraX
                    "[JeanX.Name]'s were nicer, that's all." if character in [RogueX, LauraX, JubesX] and JeanX.SeenChest:
                        $ temporary_line = JeanX
                    "[RogueX.Name]'s were tighter, that's all." if character in [EmmaX, StormX] and RogueX.SeenChest:
                        $ temporary_line = RogueX
                    "[KittyX.Name]'s were tighter, that's all." if character in [RogueX, EmmaX, LauraX, JeanX, StormX, JubesX] and KittyX.SeenChest:
                        $ temporary_line = KittyX
                    "[EmmaX.Name]'s were tighter, that's all." if character in [StormX] and EmmaX.SeenChest:
                        $ temporary_line = EmmaX
                    "[LauraX.Name]'s were tighter, that's all." if character in [RogueX, EmmaX, StormX] and LauraX.SeenChest:
                        $ temporary_line = LauraX
                    "[JeanX.Name]'s were tighter, that's all." if character in [EmmaX, StormX] and JeanX.SeenChest:
                        $ temporary_line = JeanX

                if temporary_line:
                    $ character.FaceChange("angry")
                    $ character.Mouth = "surprised"

                    if character != JeanX:
                        $ character.Statup("Love", 90, -10)
                        $ character.Statup("Obed", 80, 30)
                        $ character.Statup("Inbt", 70, -25)
                    else:
                        $ character.Statup("Love", 50, -10)
                        $ character.Statup("Love", 90, -10)
                        $ character.Statup("Obed", 50, 10)
                        $ character.Statup("Obed", 80, 30)
                        $ character.Statup("Inbt", 200, -15)

                    character.voice ". . ."

                    $ character.Mouth = "sad"

                    if temporary_line in [EmmaX, StormX]:
                        if character.GirlLikeCheck(temporary_line) >= 800:
                            $ character.FaceChange("sly", 2, Eyes="side")
                            $ character.Statup("Obed", 80, 5)

                            if character == RogueX:
                                ch_r "Well, I mean they would be quite the handful. . ."
                            elif character == KittyX:
                                ch_k "Yeah, like you just wanna shove your head into there. . ."
                            elif character == EmmaX:
                                ch_e "They are lovely, but. . ."
                            elif character == LauraX:
                                ch_l "They are kinda huge. . ."
                            elif character == JeanX:
                                ch_j "Well, they are. . . heavy. . ."
                            elif character == JubesX:
                                ch_v "Well they are really ginormous. . ."

                            $ character.GirlLikeUp(temporary_line, 20) # +20
                        elif character.GirlLikeCheck(temporary_line) >= 700:
                            $ character.Eyes = "side"
                            $ character.Statup("Obed", 80, 5)

                            if character == RogueX:
                                ch_r "I mean, I guess, if you like that kind of thing. . ."
                            elif character == KittyX:
                                ch_k "I mean, I guess, if you like that kind of thing. . ."
                            elif character == EmmaX:
                                ch_e "I don't know about that. . ."
                            elif character == LauraX:
                                ch_l "I guess that's true. . ."
                            elif character == JeanX:
                                ch_j "If you have a thing for udders. . ."
                            elif character == JubesX:
                                ch_v "Oh. Well I can't compete there. . ."
                        else:
                            $ character.GirlLikeUp(temporary_line, -50) # +20

                            $ temporary_line = "bad"
                    elif temporary_line == KittyX:
                        if character.GirlLikeCheck(temporary_line) >= 800:
                            $ character.FaceChange("sly",2,Eyes="side")
                            $ character.Statup("Obed", 80, 5)

                            if character = RogueX:
                                ch_r "They are kind of adorable. . ."
                            elif character == EmmaX:
                                ch_e "They are rather . . . pert. . ."
                            elif character == LauraX:
                                ch_l "She is very. . . streamlined. . ."
                            elif character == JeanX:
                                ch_j "She is very. . . cute. . ."
                            elif character == JubesX:
                                ch_v ". . . I guess they are really cute. . ."

                            $ character.GirlLikeUp(temporary_line, 20)
                        elif character.GirlLikeCheck(temporary_line) >= 700:
                            $ character.Eyes = "side"
                            $ character.Statup("Obed", 80, 5)

                            if character == RogueX:
                                ch_r "I mean, yeah, I guess. . ."
                            elif character == EmmaX:
                                ch_e "Well, for a child. . ."
                            elif character == LauraX:
                                ch_l "They are kinda. . . pointy. . ."
                            elif character == JeanX:
                                ch_j "If you have a thing for surf boards. . ."
                            elif character == JubesX:
                                ch_v "Ok, into that, uh? . ."
                        else:
                            $ character.GirlLikeUp(temporary_line, -50)

                            $ temporary_line = "bad"

                    if temporary_line == "bad":
                        $ character.Statup("Love", 90, -20)

                        if character == RogueX:
                            ch_r "Yeah, that's enough outta you, [character.Petname]."
                        elif character == KittyX:
                            ch_k "Well you sure know how to ruin a mood."
                        elif character == EmmaX:
                            ch_e "I think you've seen enough for now, [EmmaX.Petname]."
                        elif character == LauraX:
                            ch_l "Still kinda rude though."
                        elif character == JeanX:
                            ch_j "Still, inappropriate on your part!"
                        elif character == JubesX:
                            ch_v "Still, you don't just -say- something like that!"

                        $ character.OutfitChange()

                        $ character.RecentActions.append("no topless")
                        $ character.DailyActions.append("no topless")
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")
    else:
        $ character.AddWord(1,0,0,0,"topless") #$ character.History.append("topless")

        if ApprovalCheck(character, 800) and not character.Forced:
            $ character.Statup("Inbt", 70, 5)

            if character in [RogueX, EmmaX]:
                $ character.Statup("Obed", 70, 5)
            elif character in [KittyX, LauraX, JubesX]:
                $ character.Statup("Obed", 70, 10)
            elif character == JeanX:
                $ character.Statup("Love", 70, 5)
                $ character.Statup("Obed", 70, 25)
                $ character.Statup("Inbt", 70, 15)
        else:
            if character == EmmaX:
                $ character.Statup("Love", 90, -5)

            $ character.Statup("Love", 90, -5)
            $ character.Statup("Inbt", 70, -5)
            $ character.FaceChange("angry")

            if character in [RogueX, EmmaX]:
                $ character.Statup("Obed", 70, 15)
            elif character in [KittyX, LauraX]:
                $ character.Statup("Obed", 70, 20)
            elif character == JeanX:
                $ character.Statup("Love", 90, -35)
                $ character.Statup("Inbt", 200, -15)
                $ character.Statup("Obed", 70, 40)
            elif character == JubesX:
                $ character.Statup("Obed", 70, 10)
    return

label Rogue_First_Bottomless(Silent = 0): #rkeljsv
    if RogueX.PantiesNum() > 1 or RogueX.PantsNum() > 2 or RogueX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if RogueX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ RogueX.RecentActions.append("bottomless")
    $ RogueX.DailyActions.append("bottomless")
    $ RogueX.DrainWord("no bottomless")
    $ RogueX.SeenPussy += 1
    if RogueX.SeenPussy > 1:
            #ends portion if you've already seen them
            return

    $ RogueX.Statup("Inbt", 80, 40)
    if not Silent:
        $ RogueX.FaceChange("bemused", 1)
        "[RogueX.Name] shyly moves her hands aside, revealing her pussy."
        menu Rogue_First_BMenu:
            ch_r "Well, [RogueX.Petname]? Was it worth the wait?"
            "Lovely. . .":
                    $ RogueX.Statup("Love", 90, 20)
                    $ RogueX.Statup("Inbt", 60, 30)
                    $ RogueX.FaceChange("smile")
                    ch_r ". . ."
                    $ RogueX.Statup("Love", 40, 20)
            "I suppose.":
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Obed", 50, 20)
                    $ RogueX.Statup("Inbt", 70, -20)
                    $ RogueX.FaceChange("angry")
                    ch_r ". . ."
                    $ RogueX.Statup("Obed", 70, 30)
    else:
            $ RogueX.AddWord(1,0,0,0,"bottomless") #$ RogueX.History.append("bottomless")
            if ApprovalCheck(RogueX, 500):
                    $ RogueX.Statup("Inbt", 60, 30)
            else:
                    $ RogueX.Statup("Love", 90, -5)
                    $ RogueX.Statup("Inbt", 70, -5)
                    $ RogueX.FaceChange("angry")
                    $ RogueX.Statup("Obed", 70, 15)
    return

label Kitty_First_Bottomless(Silent = 0):
    if KittyX.PantiesNum() > 1 or KittyX.PantsNum() > 2 or KittyX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if KittyX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ KittyX.RecentActions.append("bottomless")
    $ KittyX.DailyActions.append("bottomless")
    $ KittyX.DrainWord("no bottomless")
    $ KittyX.SeenPussy += 1
    if KittyX.SeenPussy > 1:
            return                  #ends portion if you've already seen them

    $ KittyX.Statup("Inbt", 80, 30)
    $ KittyX.Statup("Obed", 70, 10)
    if not Silent:
        $ KittyX.FaceChange("bemused", 1)
        "[KittyX.Name] shyly moves her hands aside, revealing her pussy."
        menu Kitty_First_BMenu:
            extend ""
            "Lovely. . .":
                    $ KittyX.Statup("Love", 90, 20)
                    $ KittyX.Statup("Inbt", 60, 25)
                    $ KittyX.FaceChange("smile")
                    ch_k ". . ."
                    $ KittyX.Statup("Love", 40, 20)
            "Now {i}that's{/i} the \"Kitty\" I wanted to see.":
                    $ KittyX.Statup("Love", 40, 25)
                    $ KittyX.Statup("Inbt", 60, 30)
                    $ KittyX.FaceChange("perplexed", 2)
                    ch_k "[[snort]"
                    $ KittyX.Statup("Love", 90, 25)
                    $ KittyX.Blush = 1
            "Pretty messy down there." if KittyX.Pubes:
                    $ KittyX.FaceChange("surprised",2)
                    ch_k "!"
                    if ApprovalCheck(KittyX, 800, "LO"):
                            $ KittyX.FaceChange("bemused",1)
                            $ KittyX.Statup("Obed", 50, 30)
                            $ KittyX.Statup("Inbt", 60, 25)
                            ch_k "I guess I could trim it up a bit. . ."
                            $ KittyX.Todo.append("shave")
                    else:
                            $ KittyX.FaceChange("angry",1)
                            $ KittyX.Statup("Love", 40, -20)
                            $ KittyX.Statup("Obed", 50, 25)
                            $ KittyX.Statup("Inbt", 60, -5)
                            ch_k "Well[KittyX.like]sorry I don't keep it baby soft!"
            "I've seen better.":
                    $ KittyX.Statup("Love", 90, -30)
                    $ KittyX.Statup("Obed", 50, 25)
                    $ KittyX.Statup("Inbt", 70, -30)
                    $ KittyX.FaceChange("angry")
                    ch_k ". . ."
                    $ KittyX.Statup("Obed", 70, 35)
    else:
            $ KittyX.AddWord(1,0,0,0,"bottomless") #$ KittyX.History.append("bottomless")
            if ApprovalCheck(KittyX, 800) and not KittyX.Forced:
                    $ KittyX.Statup("Inbt", 60, 15)
                    $ KittyX.Statup("Obed", 70, 10)
            else:
                    $ KittyX.Statup("Love", 90, -10)
                    $ KittyX.Statup("Inbt", 70, -5)
                    $ KittyX.FaceChange("angry")
                    $ KittyX.Statup("Obed", 70, 20)
    return

label Emma_First_Bottomless(Silent = 0):
    if EmmaX.PantiesNum() > 1 or EmmaX.PantsNum() > 2 or EmmaX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if EmmaX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ EmmaX.RecentActions.append("bottomless")
    $ EmmaX.DailyActions.append("bottomless")
    $ EmmaX.DrainWord("no bottomless")
    $ EmmaX.SeenPussy += 1
    if EmmaX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ EmmaX.Statup("Inbt", 80, 30)
    $ EmmaX.Statup("Obed", 70, 10)
    if not Silent:
        $ EmmaX.FaceChange("sly")
        "You find yourself staring at [EmmaX.Name]'s bare pussy."
        menu Emma_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ EmmaX.Statup("Love", 90, 20)
                    $ EmmaX.Statup("Inbt", 60, 25)
                    $ EmmaX.FaceChange("smile")
                    ch_e "I'm aware. . . "
                    $ EmmaX.Statup("Love", 40, 20)
            "I see you keep it smooth down there." if not EmmaX.Pubes:
                $ EmmaX.FaceChange("confused",1)
                ch_e "Yes?"
                if ApprovalCheck(EmmaX, 700, "LO"):
                        $ EmmaX.FaceChange("bemused")
                        menu:
                            ch_e "Do you prefer more fuzz?"
                            "Yes":
                                if ApprovalCheck(EmmaX, 900, "LO"):
                                        $ EmmaX.Statup("Obed", 50, 30)
                                        $ EmmaX.Statup("Inbt", 60, 25)
                                        ch_e "I suppose I could let it go. . ."
                                        $ EmmaX.Todo.append("pubes")
                                else:
                                        $ EmmaX.FaceChange("normal")
                                        ch_e "Well that's a pity."
                            "Up to you, I guess.":
                                        $ EmmaX.Statup("Love", 80, 10)
                                        ch_e "I'm glad you agree."
                            "No, leave it that way.":
                                        if ApprovalCheck(EmmaX, 900, "LO"):
                                                $ EmmaX.FaceChange("sly")
                                                $ EmmaX.Statup("Love", 80, 10)
                                        else:
                                                $ EmmaX.FaceChange("angry",Mouth="normal")
                                        $ EmmaX.Statup("Inbt", 60, 25)
                                        ch_e "I'm glad I have your. . . permission."
                                        $ EmmaX.Brows = "normal"
                else:
                        $ EmmaX.FaceChange("angry",1)
                        $ EmmaX.Statup("Love", 40, -20)
                        $ EmmaX.Statup("Obed", 50, 25)
                        $ EmmaX.Statup("Inbt", 60, -5)
                        ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":
                $ EmmaX.Statup("Love", 90, -30)
                $ EmmaX.Statup("Obed", 50, 25)
                $ EmmaX.Statup("Inbt", 70, -30)
                $ EmmaX.FaceChange("angry",2)
                if not EmmaX.Forced and not ApprovalCheck(EmmaX, 900, "LO"):
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")
                        $ EmmaX.Statup("Obed", 70, 25)
                ch_e "You will regret that remark. . ."
    else:

        $ EmmaX.AddWord(1,0,0,0,"bottomless") #$ EmmaX.History.append("bottomless")
        if ApprovalCheck(EmmaX, 800) and not EmmaX.Forced:
                $ EmmaX.Statup("Inbt", 60, 5)
                $ EmmaX.Statup("Obed", 70, 10)
        else:
                $ EmmaX.Statup("Love", 90, -10)
                $ EmmaX.Statup("Inbt", 70, -5)
                $ EmmaX.FaceChange("angry")
                $ EmmaX.Statup("Obed", 70, 15)
    return

label Laura_First_Bottomless(Silent = 0):
    if LauraX.PantiesNum() > 1 or LauraX.PantsNum() > 2 or LauraX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if LauraX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ LauraX.RecentActions.append("bottomless")
    $ LauraX.DailyActions.append("bottomless")
    $ LauraX.DrainWord("no bottomless")
    $ LauraX.SeenPussy += 1
    if LauraX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ LauraX.Statup("Inbt", 80, 30)
    $ LauraX.Statup("Obed", 70, 10)
    if not Silent:
        $ LauraX.FaceChange("sly")
        if LauraX.Pubes:
                "You find yourself staring at [LauraX.Name]'s furry pussy."
        else:
                "You find yourself staring at [LauraX.Name]'s bare pussy."
        menu Laura_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ LauraX.Statup("Love", 90, 20)
                    $ LauraX.Statup("Inbt", 60, 25)
                    $ LauraX.FaceChange("smile")
                    ch_l "You think?"
                    ch_l "Yeah, I like it too. . . "
                    $ LauraX.Statup("Love", 40, 20)
            "I see you keep it natural down there." if LauraX.Pubes:
                $ LauraX.FaceChange("confused",1)
                ch_l "Well. . . yeah."
                if ApprovalCheck(LauraX, 700, "LO"):
                    $ LauraX.FaceChange("bemused")
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if ApprovalCheck(LauraX, 900, "LO"):
                                    $ LauraX.Statup("Obed", 50, 30)
                                    $ LauraX.Statup("Inbt", 60, 25)
                                    ch_l "I guess I could. . ."
                                    $ LauraX.Todo.append("pubes")
                            else:
                                    $ LauraX.FaceChange("normal")
                                    ch_l "Seems like a waste of time."
                                    ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                                    $ LauraX.Statup("Love", 80, 10)
                                    ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":
                                    if ApprovalCheck(LauraX, 900, "LO"):
                                            $ LauraX.FaceChange("sly")
                                            $ LauraX.Statup("Love", 80, 10)
                                    else:
                                            $ LauraX.FaceChange("angry",Mouth="normal")
                                    $ LauraX.Statup("Inbt", 60, 25)
                                    ch_l "Right."
                                    $ LauraX.Brows = "normal"
                else:
                        $ LauraX.FaceChange("angry",1)
                        $ LauraX.Statup("Love", 40, -20)
                        $ LauraX.Statup("Obed", 50, 25)
                        $ LauraX.Statup("Inbt", 60, -5)
                        ch_l "I mean, what else would I do?"
            "What a mess.":
                    $ LauraX.Statup("Love", 90, -30)
                    $ LauraX.Statup("Obed", 50, 25)
                    $ LauraX.Statup("Inbt", 70, -30)
                    $ LauraX.FaceChange("angry",2)
                    if not LauraX.Forced and not ApprovalCheck(LauraX, 900, "LO"):
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")
                            $ LauraX.Statup("Obed", 70, 25)
                    ch_l "I'll make you a mess. . ."
    else:
        $ LauraX.AddWord(1,0,0,0,"bottomless") #$ LauraX.History.append("bottomless")
        if ApprovalCheck(LauraX, 800) and not LauraX.Forced:
                $ LauraX.Statup("Inbt", 60, 5)
                $ LauraX.Statup("Obed", 70, 10)
        else:
                $ LauraX.Statup("Love", 90, -5)
                $ LauraX.Statup("Inbt", 70, -5)
                $ LauraX.FaceChange("angry")
                $ LauraX.Statup("Obed", 70, 15)
    return

label Jean_First_Bottomless(Silent = 0):
    if JeanX.PantiesNum() > 1 or JeanX.PantsNum() > 2 or JeanX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if JeanX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ JeanX.RecentActions.append("bottomless")
    $ JeanX.DailyActions.append("bottomless")
    $ JeanX.DrainWord("no bottomless")
    $ JeanX.SeenPussy += 1
    if JeanX.SeenPussy > 1:
            return                  #ends portion if you've already seen them

    $ JeanX.Statup("Inbt", 200, 30)
    $ JeanX.Statup("Obed", 90, 10)
    if not Silent:
        $ JeanX.FaceChange("sly")
        if JeanX.Pubes:
                "You find yourself staring at [JeanX.Name]'s fuzzy pussy."
        else:
                "You find yourself staring at [JeanX.Name]'s bare pussy."
        menu Jean_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ JeanX.Statup("Love", 90, 20)
                    $ JeanX.Statup("Inbt", 200, 25)
                    $ JeanX.FaceChange("smile")
                    ch_j "Right?"
                    $ JeanX.Statup("Love", 40, 20)
            "I see you got a fire crotch down there." if JeanX.Pubes:
                $ JeanX.FaceChange("confused",1)
                ch_j "Well. . . yeah."
                if ApprovalCheck(JeanX, 700, "LO"):
                    $ JeanX.FaceChange("bemused")
                    menu:
                        ch_j "Do you prefer it smooth?"
                        "Yes":
                            if ApprovalCheck(JeanX, 900, "LO"):
                                    $ JeanX.Statup("Obed", 90, 30)
                                    $ JeanX.Statup("Inbt", 200, 25)
                                    ch_j "Hmm, I guess. . ."
                                    $ JeanX.Todo.append("pubes")
                            else:
                                    $ JeanX.FaceChange("normal")
                                    ch_j "Not worth the hassle."
                        "Up to you, I guess.":
                                    $ JeanX.Statup("Love", 80, 10)
                                    ch_j "Of course it is."
                        "No, leave it that way.":
                                    if ApprovalCheck(JeanX, 900, "LO"):
                                            $ JeanX.FaceChange("sly")
                                            $ JeanX.Statup("Love", 80, 10)
                                    else:
                                            $ JeanX.FaceChange("angry",Mouth="normal")
                                    $ JeanX.Statup("Inbt", 200, 25)
                                    ch_j "Of course."
                                    $ JeanX.Brows = "normal"
                else:
                        $ JeanX.FaceChange("angry",1)
                        $ JeanX.Statup("Love", 40, -20)
                        $ JeanX.Statup("Obed", 90, 25)
                        $ JeanX.Statup("Inbt", 200, -5)
                        ch_j "I didn't really feel like waxing it."
            "What a mess." if JeanX.Pubes:
                    $ JeanX.Statup("Love", 90, -30)
                    $ JeanX.Statup("Obed", 90, 25)
                    $ JeanX.Statup("Inbt", 200, -30)
                    $ JeanX.FaceChange("angry",2)
                    if not JeanX.Forced and not ApprovalCheck(JeanX, 900, "LO"):
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                            $ JeanX.Statup("Obed", 90, 25)
                    ch_j "Oh, so it's not baby-smooth like [EmmaX.Name]'s?"
            "Eh, I've seen better" if not JeanX.Pubes:
                    $ JeanX.Statup("Love", 90, -30)
                    $ JeanX.Statup("Obed", 90, 25)
                    $ JeanX.Statup("Inbt", 200, -30)
                    $ JeanX.FaceChange("angry",2)
                    if not JeanX.Forced and not ApprovalCheck(JeanX, 900, "LO"):
                            $ JeanX.RecentActions.append("angry")
                            $ JeanX.DailyActions.append("angry")
                            $ JeanX.Statup("Obed", 90, 25)
                    ch_j "Oh, so it's not saggy like [EmmaX.Name]'s?"
    else:
        $ JeanX.AddWord(1,0,0,0,"bottomless") #$ JeanX.History.append("bottomless")
        if ApprovalCheck(JeanX, 800) and not JeanX.Forced:
                $ JeanX.Statup("Inbt", 60, 5)
                $ JeanX.Statup("Obed", 90, 10)
        else:
                $ JeanX.Statup("Love", 90, -5)
                $ JeanX.Statup("Inbt", 200, -5)
                $ JeanX.FaceChange("angry")
                $ JeanX.Statup("Obed", 90, 15)
    return

label Jubes_First_Bottomless(Silent = 0):
    if JubesX.PantiesNum() > 1 or JubesX.PantsNum() > 2 or JubesX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return
    if JubesX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ JubesX.RecentActions.append("bottomless")
    $ JubesX.DailyActions.append("bottomless")
    $ JubesX.DrainWord("no bottomless")
    $ JubesX.SeenPussy += 1
    if JubesX.SeenPussy > 1:
            return                  #ends portion if you've already seen them


    $ JubesX.Statup("Inbt", 80, 30)
    $ JubesX.Statup("Obed", 70, 10)
    if not Silent:
        $ JubesX.FaceChange("sly")
        if JubesX.Pubes:
                "You find yourself staring at [JubesX.Name]'s furry pussy."
        else:
                "You find yourself staring at [JubesX.Name]'s bare pussy."
        menu Jubes_First_BMenu:
            extend ""
            "Niiice. . .":
                    $ JubesX.Statup("Love", 90, 20)
                    $ JubesX.Statup("Inbt", 60, 25)
                    $ JubesX.FaceChange("surprised",2)
                    ch_v "!!"
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Oh, um, yeah, I. . . also. . . "
                    $ JubesX.Statup("Love", 40, 20)
            "I see you keep it natural down there." if JubesX.Pubes:
                $ JubesX.FaceChange("confused",2)
                ch_v "Well. . . yeah."
                if ApprovalCheck(JubesX, 700, "LO"):
                    $ JubesX.FaceChange("bemused",1)
                    menu:
                        ch_v "Did you. . . prefer it shaved?"
                        "Yes":
                            if ApprovalCheck(JubesX, 900, "LO"):
                                    $ JubesX.Statup("Obed", 50, 30)
                                    $ JubesX.Statup("Inbt", 60, 25)
                                    ch_v "I guess I could. . ."
                                    $ JubesX.Todo.append("pubes")
                            else:
                                    $ JubesX.FaceChange("normal")
                                    ch_v "I dunno, seems like a lot of hassle."
                        "Up to you, I guess.":
                                    $ JubesX.Statup("Love", 80, 10)
                                    ch_v "Well, yeah, right? Of course."
                                    if ApprovalCheck(JubesX, 900, "LO"):
                                            $ JubesX.Statup("Inbt", 60, 10)
                                            $ JubesX.Todo.append("pubes")
                        "No, leave it that way.":
                                    if ApprovalCheck(JubesX, 900, "LO"):
                                            $ JubesX.FaceChange("sly")
                                            $ JubesX.Statup("Love", 80, 10)
                                    else:
                                            $ JubesX.FaceChange("angry",Mouth="normal")
                                    $ JubesX.Statup("Inbt", 60, 25)
                                    ch_v "Oh, I guess that's your call?"
                                    $ JubesX.Brows = "normal"
                else:
                        $ JubesX.FaceChange("angry",1)
                        $ JubesX.Statup("Love", 40, -20)
                        $ JubesX.Statup("Obed", 50, 25)
                        $ JubesX.Statup("Inbt", 60, -5)
                        ch_v "Well, of course!"
            "What a mess.":
                    $ JubesX.Statup("Love", 90, -30)
                    $ JubesX.Statup("Obed", 50, 25)
                    $ JubesX.Statup("Inbt", 70, -30)
                    $ JubesX.FaceChange("angry",2)
                    if not JubesX.Forced and not ApprovalCheck(JubesX, 900, "LO"):
                            $ JubesX.RecentActions.append("angry")
                            $ JubesX.DailyActions.append("angry")
                            $ JubesX.Statup("Obed", 70, 25)
                    ch_v "Oh, them's fighting words. . ."
    else:
        $ JubesX.AddWord(1,0,0,0,"bottomless") #$ JubesX.History.append("bottomless")
        if ApprovalCheck(JubesX, 800) and not JubesX.Forced:
                $ JubesX.Statup("Inbt", 60, 5)
                $ JubesX.Statup("Obed", 70, 10)
        else:
                $ JubesX.Statup("Love", 90, -5)
                $ JubesX.Statup("Inbt", 70, -5)
                $ JubesX.FaceChange("angry")
                $ JubesX.Statup("Obed", 70, 15)
    return
