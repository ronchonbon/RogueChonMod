label chat_menu(Girl):
    call shift_focus(Girl)

    menu:
        "Ask [Girl.name] to leave" if Girl.location == Player.location:
            call dismiss_Girl(Girl)

            return
        "Romance her":
            menu:
                "Sex Menu" if Girl.location == Player.location:
                    if Girl.love >= Girl.obedience:
                        ch_p "Did you want to fool around?"
                    else:
                        ch_p "I'd like to get naughty."

                    if approval_check(Girl, 600, "LI"):
                        $ Girl.change_face("sexy")

                        if Girl == RogueX:
                            ch_r "Heh, all right, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Mmmm, ok, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "Perhaps. . ."
                        elif Girl == LauraX:
                            ch_l "Cool."
                        elif Girl == JeanX:
                            ch_j "Yeah?"
                        elif Girl == StormX:
                            ch_s "Oh?"
                        elif Girl == JubesX:
                            ch_v "Yeah?"

                        call enter_main_sex_menu(Girl)

                        return
                    elif approval_check(Girl, 400, "OI"):
                        if Girl == RogueX:
                            ch_r "If that's what you want, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Yes, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "If that's what you want, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "Yes, [Girl.player_petname]."
                        elif Girl == JeanX:
                            ch_j "Whatever. . ."
                        elif Girl == StormX:
                            ch_s "Fine."
                        elif Girl == JubesX:
                            ch_v "What would you like, [Girl.player_petname]?"

                        call enter_main_sex_menu(Girl)

                        return
                    else:
                        if Girl == RogueX:
                            ch_r "I'm not really interested, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "No thanks, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "No thank you, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "No thanks, [Girl.player_petname]."
                        elif Girl == JeanX:
                            ch_j "Not interested."
                        elif Girl == StormX:
                            ch_s "I am uninterested."
                        elif Girl == JubesX:
                            ch_v "Nah, not into it."
                "Sex Menu (locked)" if Girl.location != Player.location:
                    pass
                "Back":
                    pass
        "Talk with her":
            menu:
                "Could I get your number?" if Girl not in Player.Phonebook:
                    if Girl == EmmaX and approval_check(Girl, 800, "LI"):
                        ch_e "I don't see why not."

                        $ Player.Phonebook.append(Girl)
                    elif Girl != EmmaX and(approval_check(Girl, 400, "L") or approval_check(Girl, 200, "I")):
                        if Girl == RogueX:
                            ch_r "Sure, I suppose."
                        elif Girl == KittyX:
                            ch_k "OMG[Girl.like]sure."
                        elif Girl == LauraX:
                            ch_l "Oh, sure."
                        elif Girl == JeanX:
                            ch_j "Huh? Ok."
                        elif Girl == StormX:
                            ch_s "Oh? Certainly."
                        elif Girl == JubesX:
                            ch_v "Sure, yeah."

                        $ Player.Phonebook.append(Girl)
                    elif approval_check(Girl, 200, "O", alternate_thresholds = {EmmaX: 500 - EmmaX.inhibition}):
                        if Girl == RogueX:
                            ch_r "If you want it, I guess."
                        elif Girl == KittyX:
                            ch_k "[Girl.Like]fine."
                        elif Girl == EmmaX:
                            ch_e "Hmm. . . fine, hand me your phone."
                        elif Girl == LauraX:
                            ch_l "I guess."
                        elif Girl == JeanX:
                            ch_j "Huh? Ok."
                        elif Girl == StormX:
                            ch_s "I don't see why not."
                        elif Girl == JubesX:
                            ch_v "I guess?"

                        $ Player.Phonebook.append(Girl)
                    else:
                        if Girl == RogueX:
                            ch_r "I don't really want you calling me."
                        elif Girl == KittyX:
                            ch_k "[Girl.Like]I'd rather not?"
                        elif Girl == EmmaX:
                            ch_e "I don't think it's appropriate to give my number out to a student like that."
                        elif Girl == LauraX:
                            ch_l "Um, probably not."
                        elif Girl == JeanX:
                            ch_j "I'd rather you didn't call me."
                        elif Girl == StormX:
                            ch_s "I would rather not."
                        elif Girl == JubesX:
                            ch_v "Nah, unlisted."
                "Back":
                    pass
        "Add her to party" if Girl not in Player.Party and Girl.location == Player.location:
            ch_p "Could you follow me for a bit?"

            if Girl == EmmaX and approval_check(Girl, 1250):
                $ Player.Party.append(Girl)

                ch_e "Lead away."

                return

            if approval_check(Girl, 600, alternate_thresholds = {EmmaX: 900, JeanX: 900}):
                $ Player.Party.append(Girl)

                if Girl == RogueX:
                    ch_r "Ok, Where did you want to go?"
                elif Girl == KittyX:
                    ch_k "[Girl.Like]where to?"
                elif Girl == EmmaX:
                    ch_e "You'd better not bore me."
                elif Girl == LauraX:
                    ch_l "Where to?"
                elif Girl == JeanX:
                    ch_j "Um, sure."
                elif Girl == StormX:
                    ch_s "Oh, certainly."
                elif Girl == JubesX:
                    ch_v "Sure, what's up?"

                return
            elif not approval_check(Girl, 400):
                if Girl == RogueX:
                    ch_r "Um, no thanks."
                elif Girl == KittyX:
                    ch_k "Ew, no."
                elif Girl == EmmaX:
                    ch_e "I can't imagine why I would."
                elif Girl == LauraX:
                    ch_l "No."
                elif Girl == JeanX:
                    ch_j "What? No."
                elif Girl == StormX:
                    ch_s "Hm, no thank you."
                elif Girl == JubesX:
                    ch_v "Nah, not into it."
            else:
                if Girl == RogueX:
                    ch_r "I'm fine here, thanks."
                elif Girl == KittyX:
                    ch_k "I think I'll stay here."
                elif Girl == EmmaX:
                    ch_e "I'd rather not."
                elif Girl == LauraX:
                    ch_l "I'd rather not."
                elif Girl == JeanX:
                    ch_j "What? No."
                elif Girl == StormX:
                    ch_s "I'm comfortable here."
                elif Girl == JubesX:
                    ch_v "Def not."
        "Disband party" if Girl in Player.Party:
            ch_p "Ok, you can leave if you prefer."

            python:
                for G in Player.Party:
                    Player.Party.remove(G)

            return
        "Never mind.":
            if Girl == RogueX:
                ch_r "Ok, later then."
            elif Girl == KittyX:
                ch_k "Ok, bye."
            elif Girl == EmmaX:
                ch_e "We'll talk later then."
            elif Girl == LauraX:
                ch_l "Ok."
            elif Girl == JeanX:
                ch_j "Ok?"
            elif Girl == StormX:
                ch_s "Very well then."
            elif Girl == JubesX:
                ch_v "K. . ."

            return

    jump chat_menu

label dismiss_Girl(Girl):
    if Girl in Player.Party:
        $ Player.Party.remove(Girl)

    $ leaving = False

    menu:
        "You can leave if you like.":
            if Girl.location == Player.location and not approval_check(Girl, 700, "O"):
                if Girl == RogueX:
                    ch_r "Thanks, but I think I'll stick around."
                elif Girl == KittyX:
                    ch_k "Well, I think I'll stay."
                elif Girl == EmmaX:
                    ch_e "Be that as it may, I'll stick around for a bit."
                elif Girl == LauraX:
                    ch_l "Ok. [[she does not seem to be moving. . .]"
                elif Girl == JeanX:
                    ch_j "Ok. [[she does not seem to be moving. . .]"
                elif Girl == StormX:
                    ch_s "You have been heard. [[she does not seem to be moving. . .]"
                elif Girl == JubesX:
                    ch_v "K. . . [[she does not seem to be moving. . .]"
            else:
                if Girl == RogueX:
                    ch_r "Sure, ok. See you later."
                elif Girl == KittyX:
                    ch_k "Ok, later!"
                elif Girl == EmmaX:
                    ch_e "Very well, [Girl.player_petname]"
                elif Girl == LauraX:
                    ch_l "Ok."
                elif Girl == JeanX:
                    ch_j "Ok."
                elif Girl == StormX:
                    ch_s "Ok then."
                elif Girl == JubesX:
                    ch_v "K. . ."

                $ leaving = True
        "Could you give me the room please?":
            if Girl.location == Player.location and not approval_check(Girl, 800, "LO"):
                if Girl == RogueX:
                    ch_r "I'd rather stick around."
                elif Girl == KittyX:
                    ch_k "I've got nowhere better to be."
                elif Girl == EmmaX:
                    ch_e "As it happens, I don't have any other plans."
                elif Girl == LauraX:
                    ch_l "Nobody's kicking you out [[She doesn't move]."
                elif Girl == JeanX:
                    ch_j "What? No."
                elif Girl == StormX:
                    ch_s "I'd rather stay."
                elif Girl == JubesX:
                    ch_v "Nah, I'm good here."
            elif not approval_check(Girl, 500, "LO"):
                if Girl == RogueX:
                    ch_r "I think I should probably stick around."
                elif Girl == KittyX:
                    ch_k "Yeah, no."
                elif Girl == EmmaX:
                    ch_e "I don't think that I can."
                elif Girl == LauraX:
                    ch_l "Nope."
                elif Girl == JeanX:
                    ch_j "What? No."
                elif Girl == StormX:
                    ch_s "No, thank you."
                elif Girl == JubesX:
                    ch_v "Nah, I'm good here."
            else:
                if "dismissed" not in Girl.daily_history:
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "obedience", 5)

                if Girl == RogueX:
                    ch_r "Not a problem, see you later then."
                elif Girl == KittyX:
                    ch_k "Sure, ok."
                elif Girl == EmmaX:
                    ch_e "Very well. . ."
                elif Girl == LauraX:
                    ch_l "Sure, ok."
                elif Girl == JeanX:
                    ch_j "Whatever."
                elif Girl == StormX:
                    ch_s "Ok then."
                elif Girl == JubesX:
                    ch_v "Fine. . ."

                $ leaving = True
        "You can go now.":
            if Girl.location == Player.location and not approval_check(Girl, 500, "O"):
                if Girl == RogueX:
                    ch_r "I think I'll stay."
                elif Girl == KittyX:
                    ch_k "Um, no."
                elif Girl == EmmaX:
                    ch_e "No, I don't believe that I can."
                elif Girl == LauraX:
                    ch_l "But I won't."
                elif Girl == JeanX:
                    ch_j "Right. [[she's not moving]"
                elif Girl == StormX:
                    ch_s "But I would rather stay."
                elif Girl == JubesX:
                    ch_v "Yeah, but I'm not."
            elif not approval_check(Girl, 300, "O"):
                $ Girl.change_face("confused")

                if Girl == RogueX:
                    ch_r "Well if you want me to go, then maybe I should stick around."
                elif Girl == KittyX:
                    ch_k "Not when you've got me curious."
                elif Girl == EmmaX:
                    ch_e "Now I am intrigued."
                elif Girl == LauraX:
                    ch_l "Why?"
                elif Girl == JeanX:
                    ch_j "Uh-huh. [[she's not moving]"
                elif Girl == StormX:
                    ch_s "Oh?"
                elif Girl == JubesX:
                    ch_v "Why's that?"
            else:
                if Girl == RogueX:
                    ch_r "If you wish."
                elif Girl == KittyX:
                    ch_k "Um, ok."
                elif Girl == EmmaX:
                    ch_e "Very well. . ."
                elif Girl == LauraX:
                    ch_l "Ok."
                elif Girl == JeanX:
                    ch_j "Whatever."
                elif Girl == StormX:
                    ch_s "Ok then."
                elif Girl == JubesX:
                    ch_v "Oh, ok. . ."

                $ leaving = True
        "Never mind.":
            return

    if leaving:
        call remove_Girl(Girl)
    elif not leaving:
        menu:
            extend ""
            "I insist, get going.":
                if approval_check(Girl, 1200, "LO") or approval_check(Girl, 500, "O"):
                    if Girl == RogueX:
                        ch_r "Ok, if you insist."
                    elif Girl == KittyX:
                        ch_k "Um, ok."
                    elif Girl == EmmaX:
                        ch_e "Very well. . ."
                    elif Girl == LauraX:
                        ch_l "Ok, fine."
                    elif Girl == JeanX:
                        ch_j ". . ."
                        ch_j "Fine."
                    elif Girl == StormX:
                        ch_s ". . . Fine."
                    elif Girl == JubesX:
                        ch_v "Ok, fine. . ."

                    $ leaving = True
                elif approval_check(Girl, 1000, "LO") or approval_check(Girl, 300, "O"):
                    $ Girl.change_face("angry")

                    if Girl == RogueX:
                        ch_r "Fine, if you're going to be a dick about it."
                    elif Girl == KittyX:
                        ch_k "Fine, jerk!"
                    elif Girl == EmmaX:
                        ch_e "I'll leave, but do not test me, [Girl.player_petname]"
                    elif Girl == LauraX:
                        ch_l "I've got stuff to do anyway."
                    elif Girl == JeanX:
                        ch_j ". . ."
                        ch_j "Oh, I forgot to mention, I needed to go do. . . something."
                    elif Girl == StormX:
                        ch_s "Well, I did have some errands to run."
                    elif Girl == JubesX:
                        ch_v "Whatever. . ."

                    $ leaving = True
                else:
                    $ Girl.change_face("angry")

                    if Girl == RogueX:
                        ch_r "Like hell I will."
                    elif Girl == KittyX:
                        ch_k "Noooope."
                    elif Girl == EmmaX:
                        ch_e "Well now I'm definitely not."
                    elif Girl == LauraX:
                        ch_l "Not until I see what you have planned here."
                    elif Girl == JeanX:
                        ch_j "Well that doesn't sound fun."
                    elif Girl == StormX:
                        ch_s "I would definitely prefer to stay now."
                    elif Girl == JubesX:
                        ch_v "Well now I'm -definitely- sticking around. . ."
            "Ok, never mind.":
                pass

    if leaving:
        call remove_Girl(Girl)

    return
