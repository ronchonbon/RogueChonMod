label Sleepover(Line=0, BO=[]):




    $ Party = []

    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current:
            $ Party.append(BO[0])
        $ BO.remove(BO[0])


    if bg_current == "bg_player" and "met" in StormX.history and "met" not in JubesX.history:

        call clear_the_room ("All", 1, 0)
        "It's getting late, so you go to sleep."
        call Jubes_Meet
        call Wait
        return

    if not Party and bg_current == "bg_player":

        call clear_the_room ("All", 1)

        "It's getting late, so you go to sleep."
        if "met" in StormX.history and "met" not in JubesX.history:
            call Jubes_Meet
        call Wait
        return

    while len(Party) > 2:

        $ Party.remove(Party[2])

    if Day <= 4:

        $ Party = []
    elif Party and Party[0]:
        call shift_focus (Party[0])

    if bg_current != "bg_player":

        $ BO = all_Girls[:]
        while BO:
            if BO[0].home == bg_current:
                if BO[0] not in Party:

                    "[BO[0].name] probably wouldn't appreciate you staying over, you head back to your own room."
                    call Remove_Girl ("All")
                    jump Return_Player
                if BO[0] != Party[0]:
                    $ Party.reverse()
                $ BO = [1]
            $ BO.remove(BO[0])


    if bg_current == "bg_player":
        if len(Party) == 2:
            $ renpy.random.shuffle(Party)
            if ApprovalCheck(Party[0],Check=1) <= ApprovalCheck(Party[1],Check=1):

                $ Party.reverse()
        if not Party:
            pass
        elif Party[0].event_counter["sleepover"] >= 3 and ApprovalCheck(Party[0], 800):
            pass
        elif Party[0] == RogueX:
            ch_r "It's getting late and I'm getting a bit tired."
        elif Party[0] == KittyX:
            ch_k "It's late, I'm thinking of heading out. . ."
        elif Party[0] == EmmaX:
            ch_e "It's late, I should be going. . ."
        elif Party[0] == LauraX:
            ch_l "I need some sleep. . ."
        elif Party[0] == JeanX:
            ch_j "I'm turning in. . ."
        elif Party[0] == StormX:
            ch_s "It is getting late, I should be going. . ."
        elif Party[0] == JubesX:
            ch_v "Well, it's pretty late, you should be getting some sleep. . ."
    elif Party and bg_current == Party[0].home:
        if Party[0] == RogueX:
            ch_r "It's getting late and I'm turning in."
        elif Party[0] == KittyX:
            ch_k "I'm getting kinda tired. . ."
        elif Party[0] == EmmaX:
            ch_e "It's getting late, [EmmaX.player_petname]. . ."
        elif Party[0] == LauraX:
            ch_l "I'm tired. . ."
        elif Party[0] == JeanX:
            ch_j "I'm turning in. . ."
        elif Party[0] == StormX:
            ch_s "It is getting late, I would like to get ready for bed. . ."
        elif Party[0] == JubesX:
            ch_v "Well, it's pretty late, you should be getting some sleep. . ."
    else:
        "Something went wrong."
        "Tell Oni \"[Party] - [bg_current]\""


    if Day <= 4:

        jump Return_Player

    if EmmaX in Party:
        if "classcaught" not in EmmaX.history:
            if bg_current == EmmaX.home:
                ch_e "You should probably get going, we wouldn't want any rumors to spread."
                jump Return_Player
            else:
                ch_e "I should probably get going, we wouldn't want any rumors to spread."
                call Remove_Girl (EmmaX)
        elif len(Party) >= 2 and "three" not in EmmaX.history:

            if (bg_current == EmmaX.home or bg_current == "bg_player") and ApprovalCheck(EmmaX, 1100, "LI"):
                if Party[0] != EmmaX:
                    $ Party.reverse()
                ch_e "[Party[1].name] dear, I need a moment with [Player.name], but you can leave."
                $ Party[1].change_face("confused",1)
                Party[1].voice "Oh, ok. . ."
                call Remove_Girl (Party[1])
                ch_e "Sorry about that, but I had to discuss something with you in private."
            else:

                ch_e "Yes, I really should be leaving, don't let me bother you two."
                call Remove_Girl (EmmaX)
            if "sleeptime" not in EmmaX.history:
                $ EmmaX.history.append("sleeptime")
        if not Party or (EmmaX not in Party and bg_current == EmmaX.home):

            jump Return_Player

    $ Party[0].change_face("sexy",1)

    $ Line = 0
    if Party[0].event_counter["sleepover"] >= 3 and ApprovalCheck(Party[0], 800):

        if Party[0].home == bg_current:
            Party[0].voice "Are you staying over tonight?"
        else:
            Party[0].voice "I'm staying over, right?"
        $ Line = 1

    elif Party[0].event_counter["sleepover"] < 3 and ApprovalCheck(Party[0], 1100, "LI"):

        $ Party[0].change_face("bemused",1)
        if Party[0] == RogueX:
            if bg_current == Party[0].home:
                ch_r "I was thinking. . . maybe you wanted to stay the night?"
            else:
                ch_r "I was thinking. . . maybe I could stay the night?"
        elif Party[0] == KittyX:
            if bg_current == Party[0].home:
                ch_k "So[KittyX.like]did you want to stay over?"
            else:
                ch_k "So[KittyX.like]could I stay over?"
        elif Party[0] == EmmaX:
            if bg_current == Party[0].home:
                ch_e "I was wondering, have you considered staying over?"
            else:
                ch_e "I was wondering, could I stay over?"
        elif Party[0] == LauraX:
            if bg_current == Party[0].home:
                ch_l "So, are you staying over?"
            else:
                ch_l "So, can I stay here tonight?"
        elif Party[0] == JeanX:
            if bg_current == Party[0].home:
                ch_j "Were you planning to stay over?"
            else:
                ch_j "I'm crashing here, ok?"
        elif Party[0] == StormX:
            if bg_current == Party[0].home:
                ch_s "Did you want to stay the night?"
            else:
                ch_s "Would you mind if I sleep here tonight?"
        elif Party[0] == JubesX:
            if bg_current == Party[0].home:
                ch_v "Would you maybe wanna sleep here?"
            else:
                ch_v "Would you maybe want me to sleep here?"
        $ Line = 1


    if Line:

        menu:
            extend ""
            "Sure.":
                if Party[0].event_counter["sleepover"] <= 5:
                    $ Party[0].change_stat("love", 70, 10)
                    $ Party[0].change_stat("obedience", 80, 10)
                    $ Party[0].change_stat("obedience", 50, 20)
                    $ Party[0].change_stat("inhibition", 25, 20)
                $ Party[0].change_stat("love", 70, 5)
                $ Party[0].change_face("smile")
            "No, sorry.":


                $ Party[0].change_stat("obedience", 50, 2)
                $ Party[0].change_stat("obedience", 30, 5)
                $ Party[0].change_stat("inhibition", 40, 3)
                $ Party[0].change_face("sad")
                $ Line = 0
                if Party[0] == RogueX:
                    ch_r "Ok, see you tomorrow then. 'Night."
                elif Party[0] == KittyX:
                    ch_k "Alright. . . see you tomorrow. . ."
                elif Party[0] == EmmaX:
                    ch_e "Well, if you insist. See you tomorrow then."
                elif Party[0] == LauraX:
                    ch_l "Ok."
                elif Party[0] == JeanX:
                    ch_j "Huh. Ok, whatever."
                elif Party[0] == StormX:
                    ch_s "Very well, I will see you tomorrow then."
                elif Party[0] == JubesX:
                    ch_v "Ok, cool, cool. . . later then. . ."
    else:

        if Party[0] == RogueX:
            if bg_current == Party[0].home:
                ch_r "You should get going."
            else:
                ch_r "I'm heading out, see you tomorrow."
        elif Party[0] == KittyX:
            if bg_current == Party[0].home:
                ch_k "You should[KittyX.like]head out."
            else:
                ch_k "See ya tomorrow, [KittyX.player_petname]."
        elif Party[0] == EmmaX:
            if bg_current == Party[0].home:
                ch_e "Could you please clear the room?"
            else:
                ch_e "I should leave."
        elif Party[0] == LauraX:
            if bg_current == Party[0].home:
                ch_l "Clear out."
            else:
                ch_l "So, later."
        elif Party[0] == JeanX:
            if bg_current == Party[0].home:
                ch_j "So get going."


        elif Party[0] == StormX:
            if bg_current == Party[0].home:
                ch_s "Could you please leave me?"
            else:
                ch_s "I will see you tomorrow."
        elif Party[0] == JubesX:
            if bg_current == Party[0].home:
                ch_v "I've got some stuff to take care of, so I should get going."
            else:
                ch_v "I've got some stuff to take care of, so I guess you should get going."

        menu:
            extend ""
            "Ok, I'll head out. Good night." if Party[0].home == bg_current:

                $ Line = "leave"
            "Ok, see you later then. Good night." if Party[0].home != bg_current:

                $ Line = "leave"

            "Are you sure I can't stay the night? . ." if not Party[0].event_counter["sleepover"] and Party[0].home == bg_current:
                $ Line = "please"
            "Are you sure you can't stay? . ." if not Party[0].event_counter["sleepover"] and Party[0].home != bg_current:
                $ Line = "please"

            "That's not what you said the other night . ." if Party[0].event_counter["sleepover"]:

                if ApprovalCheck(Party[0],900)or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
                    $ Party[0].change_face("bemused",1)
                    $ Line = 1
                    if Party[0] == RogueX:
                        ch_r "Well. . . that didn't turn out so bad, I suppose. . ."
                    elif Party[0] == KittyX:
                        ch_k "and that went pretty well. . ."
                    elif Party[0] == EmmaX:
                        ch_e "It was a nice evening."
                    elif Party[0] == LauraX:
                        ch_l "Yeah, it was."
                    elif Party[0] == JeanX:
                        ch_j "I guess?"
                    elif Party[0] == StormX:
                        ch_s "That was pleasant. . ."
                    elif Party[0] == JubesX:
                        ch_v "Yeah, yeah. . ."
                else:
                    $ Party[0].change_face("smile",Brows="confused")

                    if Party[0] == RogueX:
                        ch_r "I'm afraid not this time, [RogueX.player_petname]. I'll see you later."
                    elif Party[0] == KittyX:
                        ch_k "Um, no, 'fraid not. I'll see ya tomorrow."
                    elif Party[0] == EmmaX:
                        ch_e "Well, not tonight, [EmmaX.player_petname]."
                    elif Party[0] == LauraX:
                        ch_l "Yeah, but not this time."
                    elif Party[0] == JeanX:
                        ch_j "So what?"
                    elif Party[0] == StormX:
                        ch_s "Yes, but not tonight, unfortunately. . ."
                    elif Party[0] == JubesX:
                        ch_v "Yeah, I know, but I've got stuff to do tonight. . ."
                    if bg_current != "bg_player":

                        ch_p "Ok, I'll be going then."


    if Line == "leave":

        $ Party[0].change_stat("love", 90, 3)
        $ Party[0].change_stat("inhibition", 25, 2)
        $ Party[0].change_face("smile")
        $ Line = 0
        if Party[0] == RogueX:
            ch_r "Yeah, good night, [RogueX.player_petname]. . ."
        elif Party[0] == KittyX:
            ch_k "Yeah, 'night, [KittyX.player_petname]. . ."
        elif Party[0] == EmmaX:
            ch_e "Yes, good night, [EmmaX.player_petname]."
        elif Party[0] == LauraX:
            ch_l "Ok, good night then."
        elif Party[0] == JeanX:
            ch_j "Ok, 'night."
        elif Party[0] == StormX:
            ch_s "Yes, good night."
        elif Party[0] == JubesX:
            ch_v "Yup. . . later then. . ."

    if Line == "please":

        if ApprovalCheck(Party[0],1000) or ApprovalCheck(Party[0],700,"L") or ApprovalCheck(Party[0],500,"O"):
            $ Party[0].change_face("bemused")
            $ Line = 1
            if Party[0] == RogueX:
                ch_r "Well. . . I suppose it would be alright."
            elif Party[0] == KittyX:
                ch_k "Well, Maaaybeee. . ."
            elif Party[0] == EmmaX:
                ch_e "I suppose we could make an exception. . ."
            elif Party[0] == LauraX:
                ch_l "Suit yourself."
            elif Party[0] == JeanX:
                ch_j "-Fine,- geeze."
            elif Party[0] == StormX:
                ch_s "Oh, I suppose we could make do. . ."
            elif Party[0] == JubesX:
                ch_v "Well. . . fine. . ."
        else:
            $ Party[0].change_face("smile",Brows="confused")
            $ Line = 0
            if Party[0] == RogueX:
                ch_r "I'm afraid not, [RogueX.player_petname]. Head home, I'll see you later."
            elif Party[0] == KittyX:
                ch_k "Ehhhh. . . no, not tonight, [KittyX.player_petname]. Sorry."
            elif Party[0] == EmmaX:
                ch_e "I'm afraid not."
            elif Party[0] == LauraX:
                ch_l "Don't push it."
            elif Party[0] == JeanX:
                ch_j "Yeah, no."
            elif Party[0] == StormX:
                ch_s "No, we cannot."
            elif Party[0] == JubesX:
                ch_v "Nope."

    if not Line:

        if Party[0].home == bg_current:

            call clear_the_room (Party[0], 1)
            jump Return_Player
        else:

            call Remove_Girl (Party[0])
            call Sleepover
            return


    if len(Party) >= 2:

        if Party[0].GirlLikeCheck(Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):

            if Party[0] == RogueX:
                ch_r "And you, [Party[1].name]?"
            elif Party[0] == KittyX:
                ch_k "How about you, [Party[1].name]?"
            elif Party[0] == EmmaX:
                ch_e "And what about you, [Party[1].name]?"
            elif Party[0] == LauraX:
                ch_l "And you, [Party[1].name]?"
            elif Party[0] == JeanX:
                ch_j ". . ."
                ch_j ". . . . . ."
                ch_j "And you, [Party[1].name]?"
            elif Party[0] == StormX:
                ch_s "And are you staying as well, [Party[1].name]?"
            elif Party[0] == JubesX:
                ch_v "What about you, [Party[1].name]?"
        else:
            if Party[0] == RogueX:
                ch_r "Are you leaving, [Party[1].name]?"
            elif Party[0] == KittyX:
                ch_k "You heading out, [Party[1].name]?"
            elif Party[0] == EmmaX:
                ch_e "I assume you're leaving, [Party[1].name]?"
            elif Party[0] == LauraX:
                ch_l "See you later, [Party[1].name]."
            elif Party[0] == JeanX:
                ch_j ". . ."
                ch_j ". . . . . ."
                ch_j "And you, [Party[1].name]?"
            elif Party[0] == StormX:
                ch_s "And I assume you will be leaving, [Party[1].name]?"
            elif Party[0] == JubesX:
                ch_v "You've gotta go though, -right- [Party[1].name]?"

        if Party[1].GirlLikeCheck(Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):

            $ Party[1].change_face("smile")
            if Party[1] == RogueX:
                ch_r "I'd like to stay too."
            elif Party[1] == KittyX:
                ch_k "Can I stay too?"
            elif Party[1] == EmmaX:
                ch_e "I'd rather join the fun."
            elif Party[1] == LauraX:
                ch_l "Me too, right?"
            elif Party[1] == JeanX:
                ch_j "Sounds fun, I'm in."
            elif Party[1] == StormX:
                ch_s "I would prefer to stay."
            elif Party[1] == JubesX:
                ch_v "I can stay too, right?"
            $ Line = 1
        else:
            $ Party[0].change_face("smile",1)
            if Party[1] == RogueX:
                ch_r "I guess I should be going."
            elif Party[1] == KittyX:
                ch_k "I should go, right?"
            elif Party[1] == EmmaX:
                ch_e "I suppose three is a crowd."
            elif Party[1] == LauraX:
                ch_l "I should leave."
            elif Party[1] == JeanX:
                ch_j "Sounds \"fun.\""
                ch_j "Later guys."
            elif Party[1] == StormX:
                ch_s "Ah, I should be going then."
            elif Party[1] == JubesX:
                ch_v "Um, yeah, I've got stuff to do, so. . ."
            $ Line = 0
        menu:
            extend ""
            "You should stay, [Party[1].name].":

                if Party[1].GirlLikeCheck(Party[0]) >= 500 and ApprovalCheck(Party[1], 1200):

                    if Party[1] == RogueX:
                        ch_r "Oh, I'd love to."
                    elif Party[1] == KittyX:
                        ch_k "Roomies!"
                    elif Party[1] == EmmaX:
                        ch_e "I'd love to."
                    elif Party[1] == LauraX:
                        ch_l "Great."
                    elif Party[1] == JeanX:
                        ch_j "Oh, so glad I have permission. . ."
                    elif Party[1] == StormX:
                        ch_s "Thank you, I would love to."
                    elif Party[1] == JubesX:
                        ch_v "Oh! Thanks!"
                    $ Line = 1
                    $ Party[0].GLG(Party[1],800,3,1)
                else:
                    $ Party[1].change_face("sadside",1,Mouth="smile")
                    if Party[1] == RogueX:
                        ch_r "I don't want to be a bother."
                    elif Party[1] == KittyX:
                        ch_k "No way."
                    elif Party[1] == EmmaX:
                        ch_e "I couldn't."
                    elif Party[1] == LauraX:
                        ch_l "Nah."
                    elif Party[1] == JeanX:
                        $ Party[1].change_face("angry",1,Mouth="smile")
                        ch_j "Oh, so glad I have permission. . ."
                    elif Party[1] == StormX:
                        ch_s "I would not want to intrude."
                    elif Party[1] == JubesX:
                        ch_v ". . . nah, really. . . stuff to do."
                    $ Line = 0
                    $ Party[0].GLG(Party[1],700,-5,1)


                if Line:
                    if Party[0].GirlLikeCheck(Party[1]) >= 700 and ApprovalCheck(Party[0], 1200):

                        if Party[0] == RogueX:
                            ch_r "Great!"
                        elif Party[0] == KittyX:
                            ch_k "Roomies!"
                        elif Party[0] == EmmaX:
                            ch_e "Lovely."
                        elif Party[0] == LauraX:
                            ch_l "Ok."
                        elif Party[0] == JeanX:
                            ch_j "Nice, threesome."
                        elif Party[0] == StormX:
                            ch_s "Excellent, glad to have you."
                        elif Party[0] == JubesX:
                            ch_v "Oh, cool!"
                        $ Party[1].GLG(Party[0],800,5,1)
                    elif Party[0].GirlLikeCheck(Party[1]) >= 400 and ApprovalCheck(Party[0], 1400):

                        $ Party[0].change_face("sadside",1,Mouth="smile")
                        if Party[0] == RogueX:
                            ch_r "Sure, I guess."
                        elif Party[0] == KittyX:
                            ch_k "Um, Ok."
                        elif Party[0] == EmmaX:
                            ch_e "I suppose we could find room for one more."
                        elif Party[0] == LauraX:
                            ch_l "Whatever."
                        elif Party[0] == JeanX:
                            ch_j "Yeah, ok."
                        elif Party[0] == StormX:
                            ch_s "Very well, make yourself at home. . ."
                        elif Party[0] == JubesX:
                            ch_v "Oh, cool! Promise I won't bite."
                    else:
                        $ Party[0].change_face("angry",1)
                        if Party[0] == RogueX:
                            ch_r "I'm not cool with that."
                        elif Party[0] == KittyX:
                            ch_k "No way."
                        elif Party[0] == EmmaX:
                            ch_e "I don't think so."
                        elif Party[0] == LauraX:
                            ch_l "Um, no."
                        elif Party[0] == JeanX:
                            ch_j "Definitely not."
                        elif Party[0] == StormX:
                            ch_s "No, I'm afraid not, [Party[1].name]."
                        elif Party[0] == JubesX:
                            ch_v "Oh. . . cool. Promise I won't bite."
                            ch_v "much. . ."
                        $ Party[0].GLG(Party[1],700,-5,1)
                        $ Party[1].GLG(Party[0],700,-5,1)
                        $ Line = 0
            "You should get going, [Party[1].name].":

                if Party[1] == RogueX:
                    ch_r "Oh, ok."
                elif Party[1] == KittyX:
                    ch_k "Yeah."
                elif Party[1] == EmmaX:
                    ch_e "I assumed."
                elif Party[1] == LauraX:
                    ch_l "Yeah."
                elif Party[1] == JeanX:
                    ch_j "What? You're not kicking me out, I'm kicking me out!"
                elif Party[1] == StormX:
                    ch_s "Ah, I understand."
                elif Party[1] == JubesX:
                    ch_v "Oh, ok, yeah. . ."
                $ Line = 0

    if Line == 0:

        if len(Party) >= 2:
            if Party[0] == RogueX:
                ch_r "Later, [Party[1].name]."
            elif Party[0] == KittyX:
                ch_k "Night, [Party[1].name]."
            elif Party[0] == EmmaX:
                ch_e "Goodnight, [Party[1].name]."
            elif Party[0] == LauraX:
                ch_l "Night."
            elif Party[0] == JeanX:
                ch_j "Later, [Party[1].name]."
            elif Party[0] == StormX:
                ch_s "Good night, [Party[1].name]."
            elif Party[0] == JubesX:
                ch_v "Night, [Party[1].name]."

            if Party[1] == RogueX:
                ch_r "Later guys."
            elif Party[1] == KittyX:
                ch_k "Night."
            elif Party[1] == EmmaX:
                ch_e "Goodnight."
            elif Party[1] == LauraX:
                ch_l "Night."
            elif Party[1] == JeanX:
                ch_j "Right, later."
            elif Party[1] == StormX:
                ch_s "Good night."
            elif Party[1] == JubesX:
                ch_v "Night!"
        if Party:
            call clear_the_room (Party[0], 1, 1)

    if not Party:

        if bg_current != "bg_player":
            jump Return_Player
        call clear_the_room ("All", 1)

        "It's getting late, so you go to sleep."
        call Wait
        return

    if bg_current != "bg_player" and bg_current != Party[0].home:

        "You probably shouldn't sleep here, you head back to your own room."
        call Remove_Girl ("All")
        $ renpy.pop_call()
        jump Player_Room

    jump Sleepover_Morning


label Return_Player:

    $ del Party[:]
    $ BO = all_Girls[:]
    $ renpy.random.shuffle(BO)
    while BO:
        if bg_current != BO[0].home and BO[0].location == bg_current:
            "[BO[0].name] heads out."
            $ BO[0].location = BO[0].home
        $ BO.remove(BO[0])
    if bg_current != "bg_player":
        "You head back to your room."
    $ bg_current = "bg_player"
    jump Misplaced




label Sleepover_Morning:

    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current and BO[0] not in Party:
            call Remove_Girl (BO[0])
        $ BO.remove(BO[0])

    call shift_focus (Party[0])

    if Party[0] == StormX and not StormX.sleepwear[0] and StormX.Taboo < 20:

        $ Party[0].change_outfit("nude")
    else:
        $ Party[0].change_outfit("sleep")
    $ Party[0].OutfitDay == Party[0].Outfit
    if len(Party) >= 2:

        if Party[1] == StormX and not StormX.sleepwear[0] and StormX.Taboo < 20:

            $ Party[1].change_outfit("nude")
        else:
            $ Party[1].change_outfit("sleep")
        $ Party[1].OutfitDay == Party[1].Outfit
        "The girls change into their sleepwear."
    else:
        "[Party[0].name] changes into her sleepwear."

    if Party[0] == RogueX:
        ch_r "Hmm, that's a bit more comfortable."
    elif Party[0] == KittyX:
        ch_k "Ah, that's better."
    elif Party[0] == EmmaX:
        ch_e "Mmmm, that's better."
    elif Party[0] == LauraX:
        ch_l ". . ."
    elif Party[0] == JeanX:
        ch_j "Sexy, right?"
    elif Party[0] == StormX:
        ch_s "Ah, much better."
    elif Party[0] == JubesX:
        ch_v "Ah, that's better."




    if len(Party) >= 2:
        if Party[1] == RogueX:
            ch_r "Let's turn in."
        elif Party[1] == KittyX:
            ch_k "Night, [KittyX.player_petname]"
        elif Party[1] == EmmaX:
            ch_e "Lights out."
        elif Party[1] == LauraX:
            ch_l "Night."
        elif Party[1] == JeanX:
            ch_j "Night."
        elif Party[1] == StormX:
            ch_s "Good night."
        elif Party[1] == JubesX:
            ch_v "Night."
    else:


        if Party[0] == RogueX:
            ch_r "Let's turn in."
        elif Party[0] == KittyX:
            ch_k "Night, [KittyX.player_petname]"
        elif Party[0] == EmmaX:
            ch_e "Goodnight."
        elif Party[0] == LauraX:
            ch_l "Night."
        elif Party[0] == JeanX:
            ch_j "Night."
        elif Party[0] == StormX:
            ch_s "Good night."
        elif Party[0] == JubesX:
            ch_v "Night."

    show blackscreen onlayer black
    pause 1






    $ time_index = 0
    $ Current_Time = Time_Options[(time_index)]
    $ Day += 1

    if Weekday < 6:
        $ Weekday += 1
    else:
        $ Weekday = 0



    $ DayofWeek = Week[Weekday]
    hide NightMask onlayer nightmask
    $ Player.semen = Player.max_semen
    $ Player.Spunk = 0
    $ Round = 50

    $ BO = Party[:]
    while BO:
        $ BO[0].remaining_actions = BO[0].max_actions
        $ BO.remove(BO[0])














    call Morningwood_Check

    $ Party[0].change_face("smile")
    if len(Party) >= 2:
        $ Party[1].change_face("smile")
    hide NightMask onlayer nightmask
    hide blackscreen onlayer black

    if "morningwood" in Player.daily_history:

        if Party[0] == RogueX:
            ch_r "So, that aside, Sleep well?"
        elif Party[0] == KittyX:
            ch_k "So anyway. . . G'morning . . ."
        elif Party[0] == EmmaX:
            ch_e "Now that we've got that out of our system. . ."
            ch_e "Morning, [EmmaX.player_petname]."
        elif Party[0] == LauraX:
            ch_l "Anyway, 'Morning."
        elif Party[0] == JeanX:
            ch_j "So. . . 'Morning."
        elif Party[0] == StormX:
            ch_s "Anyway, good morning, [StormX.player_petname]."
        elif Party[0] == JubesX:
            ch_v "Anyways, 'morning, [Party[0].player_petname]."
    else:
        if Party[0] == RogueX:
            ch_r "'Morning [RogueX.player_petname]. Sleep well?"
        elif Party[0] == KittyX:
            ch_k "G'morning . . ."
        elif Party[0] == EmmaX:
            ch_e "Hrmph. . ."
            ch_e "Oh. You're here."
        elif Party[0] == LauraX:
            ch_l "'Morning."
        elif Party[0] == JeanX:
            ch_j "-Yawn-"
        elif Party[0] == StormX:
            ch_s "Good morning, [StormX.player_petname]."
        elif Party[0] == JubesX:
            ch_v "Hey. . . 'morning, [Party[0].player_petname]."

    menu:
        extend ""
        "It's always nice sleeping with you." if Party[0].event_counter["sleepover"]:
            if Party[0].event_counter["sleepover"] < 5:
                $ Party[0].change_stat("love", 90, 8)
                $ Party[0].change_stat("obedience", 50, 10)
                $ Party[0].change_stat("inhibition", 70, 8)
            $ Party[0].blushing = 1

            if Party[0] == RogueX:
                ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
                ch_r "We'll have to keep this regular."
            elif Party[0] == KittyX:
                ch_k "And that's always nice to hear."
                ch_k "We'll have to keep this up."
            elif Party[0] == EmmaX:
                ch_e "Well. . ."
                ch_e "We'll have to make a habit of it then."
            elif Party[0] == LauraX:
                ch_l "Yeah. . ."
                ch_l "Warm. . ."
            elif Party[0] == JeanX:
                ch_j "Of course it is."
                ch_j "I'm a princess."
            elif Party[0] == StormX:
                ch_s "I enjoy it as well, [StormX.player_petname]."
                ch_s "You keep the bed quite warm. . ."
            elif Party[0] == JubesX:
                ch_v "Yeah. . . it's nice having company. . ."
                ch_v "You keep it so cozy. . ."

        "I loved sleeping next to you." if not Party[0].event_counter["sleepover"]:
            $ Party[0].change_stat("love", 90, 15)
            $ Party[0].change_stat("love", 70, 10)
            $ Party[0].change_stat("obedience", 50, 12)
            $ Party[0].change_stat("inhibition", 70, 12)
            $ Line = "nice"
        "It was fun.":

            if not Party[0].event_counter["sleepover"]:
                $ Party[0].change_stat("love", 90, 10)
                $ Party[0].change_stat("love", 70, 8)
                $ Party[0].change_stat("obedience", 50, 15)
                $ Party[0].change_stat("inhibition", 70, 15)
            elif Party[0].event_counter["sleepover"] < 5:
                $ Party[0].change_stat("love", 70, 8)
                $ Party[0].change_stat("obedience", 80, 10)
                $ Party[0].change_stat("inhibition", 35, 8)
            $ Party[0].change_stat("obedience", 50, 8)
            if ApprovalCheck(Party[0], 800, "L"):
                $ Party[0].change_face("bemused")
            else:
                $ Party[0].change_face("confused")

            $ Line = "fun"
            if Party[0] == RogueX:
                ch_r "Ok, well glad I wasn't {i}too{/i} much bother."
            elif Party[0] == KittyX:
                ch_k "Yeah, I mean I guess it was. . ."
            elif Party[0] == EmmaX:
                ch_e "\"Fun\" is certainly how I would describe it."
            elif Party[0] == LauraX:
                ch_l "Yeah, I guess?"
            elif Party[0] == JeanX:
                ch_j "Um, \"fun?\" . . Yeah."
            elif Party[0] == StormX:
                ch_s ". . . Yes. . ."
                ch_s ". . . fun."
            elif Party[0] == JubesX:
                ch_v "Yeah. . . it's nice having company. . ."
                $ Line = "nice"
        "You were constantly tossing around.":

            $ Party[0].blushing = 1
            if ApprovalCheck(Party[0], 800, "L") or ApprovalCheck(Party[0], 1200):
                $ Party[0].change_face("bemused")
                Party[0].voice "Hmm?"
            else:
                $ Party[0].change_face("angry")
                Party[0].voice "!!!"
            if Party[0].event_counter["sleepover"] < 5:
                if Party[0] == RogueX:
                    ch_r "It's not like I've had much experience sleeping next to someone. . ."
                elif Party[0] == KittyX:
                    ch_k "I don't make a habit out of it. . ."
                elif Party[0] == EmmaX:
                    ch_e "I haven't had a lot of practice lately."
                elif Party[0] == LauraX:
                    ch_l "Deal with it."
                elif Party[0] == JeanX:
                    ch_j "It's called \"grace.\""
                elif Party[0] == StormX:
                    ch_s "Yes. . . well. . ."
                    ch_s "I do have a lot of energy. . ."
                elif Party[0] == JubesX:
                    ch_v "I'm just not used to sleeping nights. . ."
                $ Party[0].change_stat("love", 60, -8)
                $ Party[0].change_stat("obedience", 50, 22)
                $ Party[0].change_stat("inhibition", 50, 22)
            else:
                if Party[0] == RogueX:
                    ch_r "Well you should probably be used to that by now."
                elif Party[0] == KittyX:
                    ch_k "Yeah, well. . . you should be used to that!"
                elif Party[0] == EmmaX:
                    ch_e "I don't plan on changing any time soon."
                elif Party[0] == LauraX:
                    ch_l "Yeah, it'll be like that."
                elif Party[0] == JeanX:
                    ch_j "Deal with it."
                elif Party[0] == StormX:
                    ch_s "I suppose that I do."
                elif Party[0] == JubesX:
                    ch_v "You don't need to harp on it. . ."
            $ Line = "toss"
        "You need to learn to stick to your side.":

            if Party[0].event_counter["sleepover"] < 5:
                $ Party[0].change_stat("love", 80, -8)
                $ Party[0].change_stat("obedience", 50, 40)
            if ApprovalCheck(Party[0], 500, "O"):
                $ Party[0].change_stat("love", 80, -2)
                $ Party[0].change_stat("obedience", 90, 5)
                $ Party[0].change_face("normal")
                if Party[0] == RogueX:
                    ch_r "Yes, [RogueX.player_petname], I'll try my best."
                elif Party[0] == KittyX:
                    ch_k "Fine, whatever."
                elif Party[0] == EmmaX:
                    ch_e "I do try."
                elif Party[0] == LauraX:
                    ch_l "Ok."
                elif Party[0] == JeanX:
                    ch_j "It's all my side."
                elif Party[0] == StormX:
                    ch_s "I. . . can try. . ."
                elif Party[0] == JubesX:
                    ch_v "I thought you wanted the attention. . ."
                if Party[0].event_counter["sleepover"] < 5:
                    $ Party[0].change_stat("obedience", 80, 8)
            else:
                $ Party[0].change_face("angry")
                $ Party[0].change_stat("obedience", 90, 5)
                if Party[0] == RogueX:
                    ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."
                elif Party[0] == KittyX:
                    ch_k "That's not how you get me to come back."
                elif Party[0] == EmmaX:
                    ch_e "I'll sleep how I please."
                elif Party[0] == LauraX:
                    ch_l "Good luck with that."
                elif Party[0] == JeanX:
                    ch_j "It's all my side."
                elif Party[0] == StormX:
                    ch_s "That seems unlikely."
                elif Party[0] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
                if Party[0].event_counter["sleepover"] < 5:
                    $ Party[0].change_stat("inhibition", 35, 20)
            $ Line = "toss"

    if not Party[0].event_counter["sleepover"] and Line == "nice":
        if Party[0] == RogueX:
            $ Party[0].blushing = 1
            ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
            ch_r "Makes me want to do it again sometime."
        elif Party[0] == KittyX:
            $ Party[0].blushing = 2
            ch_k "Yeah, I. . [KittyX.like]I had fun too."
            $ Party[0].blushing = 1
            ch_k "I wouldn't[KittyX.like]mind doing it again."
            $ Party[0].blushing = 2
            ch_k "You know, some other time. . . "
            $ Party[0].blushing = 1
        elif Party[0] == EmmaX:
            $ Party[0].change_face("smile",1)
            ch_e "You're a hopeless romantic, [EmmaX.player_petname]."
            $ Party[0].change_face("smile",2,Eyes="side")
            ch_e "I suppose I can be a bit hopeless too. . ."
        elif Party[0] == LauraX:
            $ Party[0].change_face("confused",1)
            ch_l "Oh. . ."
            $ Party[0].change_face("surprised",2,Brows="confused")
            ch_l "Yeah, so did I, now that you mention it. . ."
            $ Party[0].change_face("confused",1)
            ch_l "Huh."
        elif Party[0] == JeanX:
            $ Party[0].change_face("confused",1)
            ch_j "Huh? . ."
            ch_j "Oh, yeah. . . it was great. . ."
            $ Party[0].change_face("smile",1)
        elif Party[0] == StormX:
            $ Party[0].change_face("smile",1)
            ch_s "Well, yes, it was nice to sleep next to you as well, [StormX.player_petname]."
            $ Party[0].change_face("smile",2,Eyes="leftside")
            ch_s "I think we should make a habit of this. . ."
            $ Party[0].change_face("smile",1)
        elif Party[0] == JubesX:
            $ Party[0].change_face("smile",1)
            ch_v "Yeah, I enjoyed it too. . ."
            $ Party[0].change_face("sad",1)
            ch_v "I haven't really been sleeping much since. . ."
            $ Party[0].change_face("sadside",1)
            ch_v ". . . the change."
            $ Party[0].change_face("smile",1)
            ch_v "It's nice having someone to stay with me. . ."

    $ Party[0].blushing = 0

    if len(Party) >= 2:

        if "morningwood" in Player.daily_history:
            if Party[1] == RogueX:
                ch_r "And what about me?"
            elif Party[1] == KittyX:
                ch_k "Me too?"
            elif Party[1] == EmmaX:
                ch_e "And me?"
            elif Party[1] == LauraX:
                ch_l "Ung, 'morning."
            elif Party[1] == JeanX:
                ch_j "Yeah, yeah, 'morning."
            elif Party[1] == StormX:
                ch_s "Ah, yes, good morning."
            elif Party[1] == JubesX:
                ch_v "Yeah. . . 'morning."
        else:
            "[Party[1].name] rolls over in bed."
            if Party[1] == RogueX:
                ch_r "Mmm, yeah, 'Morning [RogueX.player_petname]."
            elif Party[1] == KittyX:
                ch_k "Yeah, G'morning . . ."
            elif Party[1] == EmmaX:
                ch_e "Hrmph. . ."
                ch_e "Oh. Not so loud, you two."
            elif Party[1] == JeanX:
                ch_j "Yeah, yeah, 'morning."
            elif Party[1] == StormX:
                ch_s "Ah, yes, good morning."
            elif Party[1] == JubesX:
                ch_v "Oh, um, yeah. . . 'morning."

        menu:
            extend ""
            "I always love sleeping with you too, [Party[1].name]." if Party[1].event_counter["sleepover"]:
                if Party[1].event_counter["sleepover"] < 5:
                    $ Party[1].change_stat("love", 90, 8)
                    $ Party[1].change_stat("obedience", 50, 10)
                    $ Party[1].change_stat("inhibition", 70, 8)
                $ Party[1].blushing = 1

                if Party[1] == RogueX:
                    ch_r "That's sweet of ya to say, [RogueX.player_petname]."
                elif Party[1] == KittyX:
                    ch_k "So cute!"
                elif Party[1] == EmmaX:
                    ch_e "Mmmm. . . yes, lovely."
                elif Party[1] == LauraX:
                    ch_l "Sure. . ."
                elif Party[1] == JeanX:
                    ch_j "Ouch, you're giving me a toothache."
                elif Party[1] == StormX:
                    ch_s "And I enjoy it as well, [StormX.player_petname]."
                elif Party[1] == JubesX:
                    ch_v "Yeah. . . it's nice having company. . ."

            "And it was great sleeping with you as well, [Party[1].name]." if not Party[1].event_counter["sleepover"]:
                $ Party[1].change_stat("love", 90, 15)
                $ Party[1].change_stat("love", 70, 10)
                $ Party[1].change_stat("obedience", 50, 12)
                $ Party[1].change_stat("inhibition", 70, 12)
                $ Line = "nice"
            "I had fun sleeping with you too, [Party[1].name].":

                if not Party[1].event_counter["sleepover"]:
                    $ Party[1].change_stat("love", 90, 10)
                    $ Party[1].change_stat("love", 70, 8)
                    $ Party[1].change_stat("obedience", 50, 15)
                    $ Party[1].change_stat("inhibition", 70, 15)
                elif Party[1].event_counter["sleepover"] < 5:
                    $ Party[1].change_stat("love", 70, 8)
                    $ Party[1].change_stat("obedience", 80, 10)
                    $ Party[1].change_stat("inhibition", 35, 8)
                $ Party[1].change_stat("obedience", 50, 8)
                if ApprovalCheck(Party[1], 800, "L"):
                    $ Party[1].change_face("bemused")
                else:
                    $ Party[1].change_face("confused")

                $ Line = "fun"
                if Party[1] == RogueX:
                    ch_r "Yeah, uh, fun."
                elif Party[1] == KittyX:
                    ch_k "Yeah, I mean I guess it was. . ."
                elif Party[1] == EmmaX:
                    ch_e "\"Fun\" is certainly how I would describe it."
                elif Party[1] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Party[1] == JeanX:
                    ch_j "Yeah you did."
                elif Party[1] == StormX:
                    ch_s ". . . Yes. . ."
                    ch_s ". . . fun."
                elif Party[1] == JubesX:
                    ch_v "Yeah. . . it's nice having company. . ."
                    $ Line = "nice"

            "You were constantly tossing around, [Party[1].name]." if Line == "toss":
                $ Line = "toss"
            "You were tossing around constantly too, [Party[1].name]." if Line != "toss":
                $ Line = "toss"

            "You need to learn to stick to your side, [Party[1].name]." if Line == "toss":
                $ Line = "turn"
            "And you need to learn to stick to your side too, [Party[1].name]." if Line != "toss":
                $ Line = "turn"

        if not Party[1].event_counter["sleepover"] and Line == "nice":
            if Party[1] == RogueX:
                $ Party[1].blushing = 1
                ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
                ch_r "I think I'd want to do that again."
                ch_r "And, uh, you too, [Party[0].name]."
            elif Party[1] == KittyX:
                $ Party[1].blushing = 2
                ch_k "Yeah, I. . [KittyX.like]I had fun too."
                $ Party[1].blushing = 1
                ch_k "I wouldn't[KittyX.like]mind doing it again."
                $ Party[1].blushing = 2
                ch_k "You know, some other time. . . "
                $ Party[1].blushing = 1
                ch_k "And[KittyX.like]you too, [Party[0].name]."
            elif Party[1] == EmmaX:
                $ Party[1].change_face("smile",1)
                ch_e "You're a hopeless romantic, [EmmaX.player_petname]."
                $ Party[1].change_face("smile",2,Eyes="side")
                ch_e "I suppose I can be a bit hopeless too. . ."
                ch_e "You know what I'm talking about, [Party[0].name]."
            elif Party[1] == LauraX:
                $ LauraX.change_face("confused",1)
                ch_l "Oh. . ."
                $ Party[1].change_face("surprised",2,Brows="confused")
                ch_l "Yeah, so did I, now that you mention it. . ."
                $ Party[1].change_face("confused",1)
                ch_l "Huh."
                ch_l "Weird, right, [Party[0].name]?"
            elif Party[1] == JeanX:
                $ Party[1].change_face("confused",1)
                ch_j "Huh? . ."
                ch_j "Oh, yeah. . . it was great. . ."
                $ Party[0].change_face("smile",1)
            elif Party[1] == StormX:
                $ Party[1].change_face("smile",1)
                ch_s "Well, yes, it was nice to sleep next to you as well, [StormX.player_petname]."
                $ Party[1].change_face("smile",2,Eyes="leftside")
                ch_s "I think we should make a habit of this. . ."
                $ Party[1].change_face("smile",1)
            elif Party[1] == JubesX:
                $ Party[1].change_face("smile",1)
                ch_v "Yeah, I enjoyed it too. . ."
                $ Party[1].change_face("sad",1)
                ch_v "I haven't really been sleeping much since. . ."
                $ Party[1].change_face("sadside",1)
                ch_v ". . . the change."
                $ Party[1].change_face("smile",1)
                ch_v "It's nice having someone to stay with me. . ."


        elif Line == "toss":
            $ Party[1].blushing = 1
            if ApprovalCheck(Party[1], 800, "L") or ApprovalCheck(Party[1], 1200):
                $ Party[1].change_face("bemused")
                Party[1].voice "Hmm?"
            else:
                $ Party[1].change_face("angry")
                Party[1].voice "!!!"
            if Party[1].event_counter["sleepover"] < 5:
                if Party[1] == RogueX:
                    ch_r "It's not like I've had much experience sleeping next to someone. . ."
                elif Party[1] == KittyX:
                    ch_k "I don't make a habit out of it. . ."
                elif Party[1] == EmmaX:
                    ch_e "I haven't had a lot of practice lately."
                elif Party[1] == LauraX:
                    ch_l "Deal with it."
                elif Party[1] == JeanX:
                    ch_j "It's called \"grace.\""
                elif Party[1] == StormX:
                    ch_s "Yes. . . well. . ."
                    ch_s "I do have a lot of energy. . ."
                elif Party[1] == JubesX:
                    ch_v "I'm just not used to sleeping nights. . ."
                $ Party[1].change_stat("love", 60, -8)
                $ Party[1].change_stat("obedience", 50, 22)
                $ Party[1].change_stat("inhibition", 50, 22)
            else:
                if Party[1] == RogueX:
                    ch_r "Well you should probably be used to that by now."
                elif Party[1] == KittyX:
                    ch_k "Yeah, well. . . you should be used to that!"
                elif Party[1] == EmmaX:
                    ch_e "I don't plan on changing any time soon."
                elif Party[1] == LauraX:
                    ch_l "Yeah, it'll be like that."
                elif Party[1] == JeanX:
                    ch_j "Deal with it."
                elif Party[1] == StormX:
                    ch_s "I suppose that I do."
                elif Party[1] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
        elif Line == "turn":
            if Party[1].event_counter["sleepover"] < 5:
                $ Party[1].change_stat("love", 80, -8)
                $ Party[1].change_stat("obedience", 50, 40)
            if ApprovalCheck(Party[1], 500, "O"):
                $ Party[1].change_stat("love", 80, -2)
                $ Party[1].change_stat("obedience", 90, 5)
                $ Party[1].change_face("normal")
                if Party[1] == RogueX:
                    ch_r "Yes, [RogueX.player_petname], I'll try my best."
                elif Party[1] == KittyX:
                    ch_k "Fine, whatever."
                elif Party[1] == EmmaX:
                    ch_e "I do try."
                elif Party[1] == LauraX:
                    ch_l "Ok."
                elif Party[1] == JeanX:
                    ch_j "It's all my side."
                elif Party[1] == StormX:
                    ch_s "I. . . can try. . ."
                elif Party[1] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
                if Party[1].event_counter["sleepover"] < 5:
                    $ Party[1].change_stat("obedience", 80, 8)
            else:
                $ Party[1].change_face("angry")
                $ Party[1].change_stat("obedience", 90, 5)
                if Party[1] == RogueX:
                    ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."
                elif Party[1] == KittyX:
                    ch_k "That's not how you get me to come back."
                elif Party[1] == EmmaX:
                    ch_e "I'll sleep how I please."
                elif Party[1] == LauraX:
                    ch_l "Good luck with that."
                elif Party[1] == JeanX:
                    ch_j "It's all my side."
                elif Party[1] == StormX:
                    ch_s "That seems unlikely."
                elif Party[1] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
                if Party[1].event_counter["sleepover"] < 5:
                    $ Party[1].change_stat("inhibition", 35, 20)

        $ Party[1].blushing = 0



    if len(Party) >= 2:
        $ Party[1].event_counter["sleepover"] += 1


    $ Party[0].event_counter["sleepover"] += 1




    $ time_index = 3
    $ Current_Time = Time_Options[(time_index)]
    $ Day -= 1

    if Weekday == 0:
        $ Weekday = 6
    else:
        $ Weekday -= 1

    $ DayofWeek = Week[Weekday]

    call Wait

    $ BO = all_Girls[:]
    while BO:
        if "leaving" in BO[0].recent_history or BO[0].location == bg_current:


            $ Party.append(BO[0])
            $ BO[0].location = bg_current
            if "leaving" in BO[0].recent_history:
                $ BO[0].recent_history.remove("leaving")
        if "morningwood" in BO[0].Traits:

            $ BO[0].recent_history.append("blowjob")
            $ BO[0].daily_history.append("blowjob")
            $ BO[0].daily_history.append("morningwood")
            $ BO[0].Traits.remove("morningwood")
        $ BO.remove(BO[0])



    if Party:
        $ Party[0].change_face("normal")
        $ Party[0].change_outfit(6,Changed = 1)

        if len(Party) >= 2:
            $ Party[1].change_face("normal")
            $ Party[1].change_outfit(6,Changed = 1)
            "The girls get changed for the day."
        else:
            "[Party[0].name] gets changed for the day."
    $ Party = []







    call Girls_Location
    return









label Morningwood_Check(Girls=[0,-3], D20=0):



    $ D20 = renpy.random.randint(0,3)
    $ Line = 0

    if len(Party) >= 2:

        if Party[0].GirlLikeCheck(Party[1]) >= 900:

            $ Girls[0] = 2
        elif Party[0].GirlLikeCheck(Party[1]) >= 750:

            $ Girls[0] = 0
        elif Party[0].GirlLikeCheck(Party[1]) <= 400:

            $ Girls[0] = 2
        else:
            $ Girls[0] = 0

        if Party[1].GirlLikeCheck(Party[0]) >= 900:

            $ Girls[1] = 2
        elif Party[1].GirlLikeCheck(Party[0]) >= 750:

            $ Girls[1] = 0
        elif Party[1].GirlLikeCheck(Party[0]) <= 400:

            $ Girls[1] = -5
        else:
            $ Girls[1] = -3
    else:
        $ Girls[0] -= 2


    if "chill" in Party[0].Traits:

        $ Girls[0] = 0
    else:
        if Party[0].action_counter["blowjob"] >= 5 or ApprovalCheck(Party[0], 900, "I"):
            $ Girls[0] += 3
        elif Party[0].action_counter["blowjob"] and ApprovalCheck(Party[0], 900):
            $ Girls[0] += 2
        elif ApprovalCheck(Party[0], 1400):
            $ Girls[0] += 2
        elif Party[0].action_counter["blowjob"] or ApprovalCheck(Party[0], 900):
            $ Girls[0] += 1

        if "hungry" in Party[0].Traits and D20 >= 2:

            $ Girls[0] += 2
        if Party[0].Thirst >= 60:

            $ Girls[0] += 2
        elif Party[0].Thirst >= 30:

            $ Girls[0] += 1
        if Party[0].lust >= 50:

            $ Girls[0] += 1
        if Party[0].SEXP <= 15:

            $ Girls[0] -= 1


        if Girls[1] >= 0:

            $ Girls[0] += 1


    if JubesX in Party:

        if len(Party) >= 2:
            $ Line = "no"
        else:
            return
    elif Girls[0] >= D20:
        $ Line = "yes"




    if len(Party) >= 2:
        if Party[1].action_counter["blowjob"] >= 5 or ApprovalCheck(Party[1], 900, "I"):
            $ Girls[1] += 3
        elif Party[1].action_counter["blowjob"] and ApprovalCheck(Party[1], 900):
            $ Girls[1] += 2
        elif ApprovalCheck(Party[1], 1400):
            $ Girls[1] += 2
        elif Party[1].action_counter["blowjob"] or ApprovalCheck(Party[1], 900):
            $ Girls[1] += 1

        if "hungry" in Party[1].Traits and D20 >= 2:

            $ Girls[1] += 2
        if Party[1].Thirst >= 60:

            $ Girls[1] += 2
        elif Party[1].Thirst >= 30:

            $ Girls[1] += 1
        if Party[1].lust >= 50:

            $ Girls[1] += 1
        if Party[1].SEXP <= 15:

            $ Girls[1] -= 1


        if Girls[0] >= 0:

            $ Girls[1] += 1


        if Party[1] == JubesX:

            if Girls[1] >= (D20 + 1):
                $ Line = "other"
            elif Girls[1] <= -1:
                $ Line = "no"
        elif Girls[1] >= (D20 + 1):
            if Line == "yes":
                $ Line = "double"
            else:
                $ Line = "other"
        elif Girls[1] <= -1:
            $ Line = "no"


        if Line == "other" and Party[0].GirlLikeCheck(Party[1]) >= 500 and "chill" not in Party[1].Traits:

            $ Party.reverse()
            $ Girls[0] = "yes"
            $ Girls[1] = 0



    if Line:

        if Line == "no":

            "You hear a little commotion as you start to wake up."
            if Party[1] == RogueX:
                ch_r "You get'cher head out of there, [Party[0].name]!"
            elif Party[1] == KittyX:
                "You hear a thump and feel a small woosh as something heavy drops under the bed."
                Party[0].voice "Ow!"
                ch_k "Serves you right, [Party[0].name]."
            elif Party[1] == EmmaX:
                ch_e "Step away from [Player.name], [Party[0].name]."
            elif Party[1] == LauraX:
                ch_l "Back it up, [Party[0].name]."
            elif Party[1] == JeanX:
                ch_j "Back it off, [Party[0].name]."
            elif Party[1] == StormX:
                ch_s "[Party[0].name], some of us are trying to sleep. . ."
            elif Party[1] == JubesX:
                ch_v "He's trying to sleep over there, cut it out. . ."

            if Party[0] == RogueX:
                ch_r "I didn't mean no harm, [Party[1].name]."
            elif Party[0] == KittyX:
                "You hear a thump and feel a small woosh as something drops under the bed."
                Party[0].voice "Ow!"
                ch_k "Spoilsport."
            elif Party[0] == EmmaX:
                ch_e "Don't be a bore, dear."
            elif Party[0] == LauraX:
                ch_l "Fine, whatever."
            elif Party[0] == JeanX:
                ch_j "You back it off. . ."
                "-Zap-"
            elif Party[0] == StormX:
                ch_s "I didn't intend to wake you. . ."
            elif Party[0] == JubesX:
                ch_v "Oh, fine. . ."
            if Party[0] != JeanX:
                return
        elif Line == "double":

            $ second_girl_primary_action = "blowjob"
            $ Party[1].recent_history.append("blowjob")
            $ Party[1].daily_history.append("blowjob")
            $ Party[1].daily_history.append("morningwood")
            $ Party[1].Traits.append("morningwood")

        $ primary_action = "blowjob"
        $ Party[0].recent_history.append("blowjob")
        $ Party[0].daily_history.append("blowjob")
        $ Party[0].daily_history.append("morningwood")
        $ Party[0].Traits.append("morningwood")
        call Sleepover_MorningWood

        call Sex_Over (0)
    else:



        pass

    return






label Sleepover_MorningWood:

    $ Player.AddWord(1,"interruption")
    call shift_focus (Party[0])
    $ Player.focus = 30
    if primary_action == "blowjob":
        ch_u "\"Slurp, slurp, slurp.\""
    else:
        ch_u "\"Squish, squish, squish.\""

    $ Player.change_stat("focus", 80, 5)
    $ Party[0].change_stat("lust", 80, 5)
    $ Player.daily_history.append("morningwood")

    $ Partner = Party[1] if len(Party) >= 2 else 0


    $ Player.recent_history.append("cockout")

    if Partner:
        if Partner == RogueX:
            show Rogue_Sprite:
                pos (900,250)
        elif Partner == KittyX:
            show Kitty_Sprite:
                pos (900,250)
        elif Partner == EmmaX:
            show Emma_Sprite:
                pos (900,250)
        elif Partner == LauraX:
            show Laura_Sprite:
                pos (900,250)
        elif Partner == JeanX:
            show Jean_Sprite:
                pos (900,250)
        elif Partner == StormX:
            show Storm_Sprite:
                pos (900,250)
        elif Partner == JubesX:
            show Jubes_Sprite:
                pos (900,250)
        $ Partner.recent_history.append("threesome")

    $ Party[0].recent_history.append("blanket")
    call expression Party[0].Tag + "_BJ_Launch"

    $ Party[0].change_face("closed",1)
    if Partner:
        $ Partner.change_face("closed",1,Mouth="tongue")

    "You feel a pleasant sensation. . ."
    if primary_action == "blowjob":
        if second_girl_primary_action:
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
    else:
        if second_girl_primary_action:
            ch_u "\"Squish, squish, squish.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Squish, squish, squish.\""
    $ Player.change_stat("focus", 80, 5)
    $ Party[0].change_stat("lust", 80, 5)

    "It's somewhere below your waist. . ."
    if primary_action == "blowjob":
        if second_girl_primary_action:
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
    else:
        if second_girl_primary_action:
            ch_u "\"Squish, squish, squish.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Squish, squish, squish.\""
    $ Player.change_stat("focus", 80, 10)
    $ Party[0].change_stat("lust", 80, 5)

    "You open your eyes. . ."

    hide NightMask onlayer nightmask
    hide blackscreen onlayer black

    $ action_speed = 3
    $ Count = 3
    $ Line = 0
    call Seen_First_Peen (Party[0], Partner, 1, 1, 1)
    while Count > 0:

        $ Player.change_stat("focus", 80, 10)
        $ Party[0].change_stat("lust", 80, 5)
        if Partner:
            $ Partner.change_stat("lust", 80, 5)
        menu:
            "Stay Quiet":
                if Count >2:
                    if second_girl_primary_action:
                        "You just let them do their thing and pretend to still be asleep."
                    else:
                        "You just let her do her thing and pretend to still be asleep."
                elif Count>1:
                    "It does feel nice. . ."
                else:
                    if second_girl_primary_action:
                        "You wouldn't want to disturb them. . ."
                    else:
                        "You wouldn't want to disturb her. . ."
                if primary_action == "blowjob":
                    Party[0].voice "\"Slurp, slurp, slurp.\""
                else:
                    Party[0].voice "\"Squish, squish, squish.\""
                if second_girl_primary_action:
                    Party[1].voice "\"Slurp, slurp, slurp.\""
                ". . ."
            "Um. . . [Party[0].petname], what're you doing?":
                $ Line = "question"
                $ Count = 1
            "That feels great, keep going. . .":
                $ Line = "praise"
                $ Count = 1
            "Hey, quit that!":
                $ Line = "no"
                $ Count = 1
        $ Count -= 1
    $ action_speed = 1
    $ Party[0].blushing = 1
    if second_girl_primary_action:
        "[Party[0].name] pulls back with a pop and [Party[1].name] sits back."
        $ second_girl_primary_action = 0
    else:
        "[Party[0].name] pulls back with a pop."
    if Line == "question":
        $ Party[0].change_face("smile",1)
        if Party[0] == RogueX:
            ch_r "Well I ain't whistlin Dixie, [RogueX.player_petname]."
        elif Party[0] == KittyX:
            ch_k "I wasn't[KittyX.like]being subtle about it, [KittyX.player_petname]."
        elif Party[0] == EmmaX:
            ch_e "Surely your education hasn't been that poor, [EmmaX.player_petname]."
        elif Party[0] == LauraX:
            ch_l "Guess."
        elif Party[0] == JeanX:
            $ Party[0].change_face("confused",1)
            $ action_speed = 2
            ch_j ". . ."
            ch_j "I 'ave orr dick, in ey 'outh. . ."
            ch_j "Are u 'rain 'amaged?"
            $ action_speed = 1
            if Partner:
                $ Party[0].eyes = "leftside"
                ch_j "Is he brain damaged?"
            $ Party[0].change_face("sly",1)
        elif Party[0] == StormX:
            ch_s "I didn't intend to wake you. . ."
        elif Party[0] == JubesX:
            ch_v "Sorry, I. . . hadn't had breakfast. . ."
    elif Line == "praise":
        $ Party[0].change_face("smile",1)
        $ Party[0].change_stat("love", 90, 5)
        $ Party[0].change_stat("obedience", 50, 2)
        $ Party[0].change_stat("inhibition", 60, 2)
        if Party[0] == RogueX:
            ch_r "Mmm, you know it, [RogueX.player_petname]."
        elif Party[0] == KittyX:
            ch_k "Mmm, hehe."
        elif Party[0] == EmmaX:
            ch_e "Practice, [EmmaX.player_petname]."
        elif Party[0] == LauraX:
            ch_l "Yeah, I guess?"
        elif Party[0] == JeanX:
            ch_j "Heh."
        elif Party[0] == StormX:
            ch_s "Certainly. . ."
        elif Party[0] == JubesX:
            ch_v "I do enjoy it. . ."
    elif Line == "no":
        $ Party[0].change_stat("love", 90, -3)
        $ Party[0].change_stat("obedience", 50, 2)
        $ Party[0].change_stat("inhibition", 60, -2)
        $ action_speed = 0
        $ Party[0].change_face("angry",1,Brows="confused")
        if Party[0] == RogueX:
            ch_r "Well that's a fine \"how d'ya do,\" when a girl goes to all this trouble!"
        elif Party[0] == KittyX:
            ch_k "{i}That's{/i} the thanks I get?!"
        elif Party[0] == EmmaX:
            ch_e "A little \"gratitude\" wouldn't be uncalled for. . ."
        elif Party[0] == LauraX:
            ch_l "Huh?"
        elif Party[0] == JeanX:
            ch_j "Seriously? No \"thank you?\""
        elif Party[0] == StormX:
            ch_s "Oh, I'm sorry if I was presumptuous. . ."
        elif Party[0] == JubesX:
            ch_v "Sorry, sorry! I was a little hungry. . ."
    else:
        if Party[0] == RogueX:
            ch_r "Heh, I can tell you're awake, [RogueX.player_petname]. . ."
            ch_r "You've been. . . more responsive."
        elif Party[0] == KittyX:
            ch_k "You can stop faking it, [KittyX.player_petname]. . ."
            ch_k "This guy's telling me you're awake now."
        elif Party[0] == EmmaX:
            ch_e "I don't know who you think you're fooling."
            ch_e "You've been awake for a while, [EmmaX.player_petname]. . ."
        elif Party[0] == LauraX:
            ch_l "You can stop playing dead, [LauraX.player_petname]. . ."
            ch_l "Oldest trick in the book."
        elif Party[0] == JeanX:
            ch_j "You can stop pretending to be asleep. . ."
            ch_j "I can't read your mind, but I can read your dick. . ."
        elif Party[0] == StormX:
            ch_s "I didn't intend to wake you, but it seems I have."
        elif Party[0] == JubesX:
            ch_v "Oh, g'morning sleepyhead. . ."


    if Partner:

        if Line == "question":
            $ Party[1].change_face("smile",1)
        elif Line == "praise":
            $ Party[1].change_stat("love", 90, 3)
            $ Party[1].change_stat("obedience", 50, 2)
            $ Party[1].change_stat("inhibition", 60, -2)
            $ Party[1].change_face("smile",1)
        elif Line == "no":
            $ Party[1].change_stat("love", 90, -3)
            $ Party[1].change_stat("obedience", 50, 2)
            $ Party[1].change_stat("inhibition", 60, -2)
            $ Party[1].change_face("angry",1,Brows="confused")

        if Partner == RogueX:
            if "blowjob" in RogueX.recent_history:
                ch_r "I don't know 'bout that, [RogueX.player_petname]."
            else:
                "[RogueX.name] rolls over in bed."
                ch_r "Don't stop on my account, [RogueX.player_petname]."
        elif Partner == KittyX:
            if "blowjob" in KittyX.recent_history:
                ch_k "Huh. . ."
            else:
                "[KittyX.name] rolls over in bed."
                ch_k "Looked like you were having some fun there . . ."
        elif Partner == EmmaX:
            if "blowjob" in EmmaX.recent_history:
                ch_e "Well. . ."
            else:
                "[EmmaX.name] rolls over in bed."
                ch_e "Oh, don't let me stop you two."
        elif Partner == LauraX:
            if "blowjob" in LauraX.recent_history:
                ch_l "Hmm. . ."
            else:
                "[LauraX.name] rolls over in bed and stares at you both."
        elif Partner == JeanX:
            if "blowjob" in JeanX.recent_history:
                ch_j "Hmm. . ."
            else:
                "[JeanX.name] rolls over in bed and puts a pillow over her head."
        elif Partner == StormX:
            if "blowjob" in StormX.recent_history:
                ch_s "Hm?"
            else:
                "[StormX.name] rolls over in bed."
                ch_s "Ah."
                ch_s "Go on then. . ."
        elif Partner == JubesX:
            if "blowjob" in JubesX.recent_history:
                ch_v "Mmmm. . ."
            else:
                "[JubesX.name] rolls over in bed."
                ch_v "I just thought it looked like fun. . ."


    menu:
        "So, um, you want to get back to it?":
            if Line != "no":

                $ Party[0].change_face("smile",1)
                if Party[0] == RogueX:
                    ch_r "My pleasure."
                elif Party[0] == KittyX:
                    ch_k "Hehe, mmmm. . ."
                elif Party[0] == EmmaX:
                    ch_e "If you insist. . ."
                elif Party[0] == LauraX:
                    ch_l "That's the plan. . ."
                elif Party[0] == JeanX:
                    ch_j "Sure."
                elif Party[0] == StormX:
                    ch_s "I would love to. . ."
                elif Party[0] == JubesX:
                    ch_v "Sure would."
            elif Line == "no" and ApprovalCheck(Party[0], 1750):

                $ Party[0].change_stat("obedience", 80, 3)
                $ Party[0].change_stat("inhibition", 60, 2)
                $ Party[0].change_face("bemused")
                if Party[0] == RogueX:
                    ch_r "You're lucky I'm so into you. . ."
                elif Party[0] == KittyX:
                    ch_k "Wha? Well. . . I guess. . ."
                elif Party[0] == EmmaX:
                    ch_e "Do try not to be a prat this time. . ."
                elif Party[0] == LauraX:
                    ch_l "Fine. . ."
                elif Party[0] == JeanX:
                    $ Party[0].change_stat("obedience", 90, 3)
                    ch_j "Whatever."
                elif Party[0] == StormX:
                    ch_s ". . ."
                    ch_s "I suppose I should finish what I start."
                elif Party[0] == JubesX:
                    ch_v "Do you need to ask?"
                $ Line = "maybe"
            else:

                $ Party[0].change_face("angry",1)
                if Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Party[0] == LauraX:
                    ch_l "No."
                elif Party[0] == JeanX:
                    ch_j "Ha! No."
                elif Party[0] == StormX:
                    ch_s "Well now I am not so motivated. . ."
                elif Party[0] == JubesX:
                    ch_v "No, I think I got enough. . ."
        "Were you more interested in something else?":
            if Line != "no":

                $ Party[0].change_face("sexy",1)
                if Party[0] == RogueX:
                    ch_r "Ooh, what did you have in mind?"
                elif Party[0] == KittyX:
                    ch_k "Maaaybee. . . like what?"
                elif Party[0] == EmmaX:
                    ch_e "Perhaps. . . What did you have in mind?"
                elif Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Party[0] == JeanX:
                    ch_j "You read my mind. . ."
                elif Party[0] == StormX:
                    ch_s "I would love to. . ."
                elif Party[0] == JubesX:
                    ch_v "Sure, I guess. . ."
                $ Line = "sex"
            elif Line == "no" and ApprovalCheck(Party[0], 1650):

                $ Party[0].change_stat("obedience", 80, 3)
                $ Party[0].change_stat("inhibition", 60, 3)
                $ Party[0].change_face("bemused",1)
                if Party[0] == RogueX:
                    ch_r "Well, you're a jerk, but you're a cute jerk."
                    ch_r "What were you thinking?"
                elif Party[0] == KittyX:
                    ch_k "Oh, so you had something {i}else{/i} in mind. . ."
                    ch_k "Like what?"
                elif Party[0] == EmmaX:
                    ch_e "Hmm, second chance [EmmaX.player_petname], what were you considering?"
                elif Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Party[0] == JeanX:
                    ch_j "Oh? Trying to make it up to me?"
                elif Party[0] == StormX:
                    ch_s "Well, I suppose if you were interested. . ."
                elif Party[0] == JubesX:
                    ch_v "I guess?"
                $ Line = "sex"
            else:

                $ Party[0].change_face("angry",1)
                if Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Party[0] == LauraX:
                    ch_l "No."
                elif Party[0] == JeanX:
                    ch_j "Well I -was,- but then you had to be a dickbag about it."
                elif Party[0] == StormX:
                    ch_s "I am no longer in the mood."
                elif Party[0] == JubesX:
                    ch_v "Lol, no. . ."
        "Sorry, sorry, please continue." if Line == "no":
            if ApprovalCheck(Party[0], 1450):

                $ Party[0].change_stat("love", 90, 3)
                $ Party[0].change_stat("obedience", 80, 2)
                $ Party[0].change_stat("inhibition", 60, 4)
                $ Party[0].change_face("bemused",1)
                if Party[0] == RogueX:
                    ch_r "Well, since you asked so nice. . ."
                elif Party[0] == KittyX:
                    ch_k "I guess I can forgive you. . ."
                elif Party[0] == EmmaX:
                    ch_e "Ok, I'll give you another chance here."
                elif Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Party[0] == JeanX:
                    ch_j ". . . fine."
                elif Party[0] == StormX:
                    ch_s "Fine."
                elif Party[0] == JubesX:
                    ch_v "Yeah, sure."
                $ Line = "maybe"
            else:

                $ Party[0].change_stat("love", 90, 2)
                $ Party[0].change_face("angry",1)
                if Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Party[0] == LauraX:
                    ch_l "No."
                elif Party[0] == JeanX:
                    ch_j "Nice try."
                elif Party[0] == StormX:
                    ch_s "I am no longer in the mood."
                elif Party[0] == JubesX:
                    ch_v "Nah, I got enough. . ."
        "Sorry, but we could do something else." if Line == "no":
            if ApprovalCheck(Party[0], 1350):

                $ Party[0].change_stat("love", 90, 3)
                $ Party[0].change_face("sexy",1)
                if Party[0] == RogueX:
                    ch_r "Well, since you asked so nice. . ."
                    ch_r "What did you have in mind?"
                elif Party[0] == KittyX:
                    ch_k "I guess, maybe. . ."
                    ch_k "Like what?"
                elif Party[0] == EmmaX:
                    ch_e "Mmm, I'll consider it. . ."
                elif Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Party[0] == JeanX:
                    ch_j ". . . fine."
                elif Party[0] == StormX:
                    ch_s "I. . . suppose so."
                elif Party[0] == JubesX:
                    ch_v "Sure, I guess. . ."
                $ Line = "sex"
            else:

                $ Party[0].change_stat("love", 90, 2)
                $ Party[0].change_face("angry",1)
                if Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Party[0] == LauraX:
                    ch_l "No."
                elif Party[0] == JeanX:
                    ch_j "Nope, too late."
                elif Party[0] == StormX:
                    ch_s "No, I am no longer in the mood."
                elif Party[0] == JubesX:
                    ch_v "Nah. . ."
        "Not when I'm just waking up.":
            $ Party[0].change_face("angry",1)
            if Party[0] == RogueX:
                ch_r "Fine, whatever!"
                $ RogueX.eyes = "side"
                ch_r "[[mumbles] Girl tries to do a favor. . ."
            elif Party[0] == KittyX:
                ch_k "Aw. . ."
                $ KittyX.eyes = "side"
                ch_k "Last time I do you a favor. . ."
            elif Party[0] == EmmaX:
                ch_e "Hmph. . ."
                $ EmmaX.eyes = "side"
                ch_e "It's not as though that was for my benefit. . ."
            elif Party[0] == LauraX:
                ch_l "Tsk. . ."
                $ LauraX.eyes = "side"
                ch_l "\"No free blowjobs,\" got it. . ."
            elif Party[0] == JeanX:
                $ Party[0].change_stat("love", 90, -5)
                $ Party[0].change_stat("obedience", 90, 2)
                ch_j "Seriously? . ."
                $ JeanX.eyes = "side"
                ch_j "\"Rules, rules, rules\" around here. . ."
            elif Party[0] == StormX:
                ch_s "I can understand."
            elif Party[0] == JubesX:
                ch_v "Ok, ok. . ."
            $ Line = "no"



    if Line == "no" or Line == "sex":
        if Partner:
            $ Partner.change_face("sexy")
        $ Party[0].recent_history.remove("blanket")
        call expression Party[0].Tag + "_BJ_Reset"

        if len(Party) >= 2:
            if Party[1] == RogueX:
                show Rogue_Sprite:
                    ease 1 pos (700,50)
                show Rogue_Sprite:
                    pos (700,50)
            elif Party[1] == KittyX:
                show Kitty_Sprite:
                    ease 1 pos (700,50)
                show Kitty_Sprite:
                    pos (700,50)
            elif Party[1] == EmmaX:
                show Emma_Sprite:
                    ease 1 pos (700,50)
                show Emma_Sprite:
                    pos (700,50)
            elif Party[1] == LauraX:
                show Laura_Sprite:
                    ease 1 pos (700,50)
                show Laura_Sprite:
                    pos (700,50)
            elif Party[1] == JeanX:
                show Jean_Sprite:
                    ease 1 pos (700,50)
                show Jean_Sprite:
                    pos (700,50)
            elif Party[1] == StormX:
                show Storm_Sprite:
                    ease 1 pos (700,50)
                show Storm_Sprite:
                    pos (700,50)
            elif Party[1] == JubesX:
                show Jubes_Sprite:
                    ease 1 pos (700,50)
                show Jubes_Sprite:
                    pos (700,50)

        if Line == "no":
            if bg_current == "bg_player":
                if Partner:
                    Partner.voice "I'm out of here."
                Party[0].voice "Yeah, me too."
            else:
                Party[0].voice "Oh, get out of here already."




            $ Party = []
            $ Partner = 0


            $ time_index = 3
            $ Current_Time = Time_Options[(time_index)]
            $ Day -= 1

            if Weekday == 0:
                $ Weekday = 6
            else:
                $ Weekday -= 1

            $ DayofWeek = Week[Weekday]
            call Wait

            jump Return_Player

        elif Line == "sex":

            call expression Party[0].Tag + "_SexMenu"
    else:

        $ Line = 0
        $ action_speed = 1
        $ action_context = 0
        if Partner:
            $ second_girl_primary_action = "blowjob"
        call Morning_Partner
        call expression Party[0].Tag + "_SexAct" pass ("blowjob")
    return



label Morning_Partner:

    if not Partner:
        return
    $ Partner.change_face("sexy")
    if Partner == RogueX:
        show Rogue_Sprite:
            ease 1 pos (700,50)
        show Rogue_Sprite:
            pos (700,50)
    elif Partner == EmmaX:
        show Emma_Sprite:
            ease 1 pos (700,50)
        show Emma_Sprite:
            pos (700,50)
    elif Partner == KittyX:
        show Kitty_Sprite:
            ease 1 pos (700,50)
        show Kitty_Sprite:
            pos (700,50)
    elif Partner == LauraX:
        show Laura_Sprite:
            ease 1 pos (700,50)
        show Laura_Sprite:
            pos (700,50)
    elif Partner == JeanX:
        show Jean_Sprite:
            ease 1 pos (700,50)
        show Jean_Sprite:
            pos (700,50)
    elif Partner == StormX:
        show Storm_Sprite:
            ease 1 pos (700,50)
        show Storm_Sprite:
            pos (700,50)
    elif Partner == JubesX:
        show Jubes_Sprite:
            ease 1 pos (700,50)
        show Jubes_Sprite:
            pos (700,50)
    return










label Poly_Start(Newbie=0, Round2=0, Asked=0):




    $ Line = 0

    if Newbie in Player.Harem:
        return

    if not Player.Harem:
        return

    if Asked in all_Girls:
        if Asked in Player.Harem and Player.Harem[0] != Asked:

            $ Player.Harem.remove(Asked)
            if Player.Harem:
                $ Player.Harem.insert(0,Asked)
            else:
                $ Player.Harem.append(Asked)

    if "polystart" in Player.daily_history:
        if Round2 and Asked:
            "You pull [Player.Harem[0].name] aside for a moment."
            ch_p "Hey, have you changed your mind about [Newbie.name] lately?"
            if Player.Harem[0] == RogueX:
                ch_r "Getting a little greedy, aren't you."
            elif Player.Harem[0] == KittyX:
                ch_k "Wow, um, chill for a bit."
            elif Player.Harem[0] == EmmaX:
                ch_e "Take a breather, [Player.Harem[0].player_petname]."
            elif Player.Harem[0] == LauraX:
                ch_l "Cool your jets."
            elif Player.Harem[0] == JeanX:
                ch_j "Not really, no."
            elif Player.Harem[0] == StormX:
                ch_s "I am weighing my options, give me time."
            elif Player.Harem[0] == JubesX:
                ch_v "Look. . . I have feelings. . ."
            Asked.voice "Ask me some time later."
        return

    $ Player.daily_history.append("polystart")

    if len(Player.Harem) >= 2:
        call Harem_Start (Newbie, Round2)
        return


    $ Party = [Player.Harem[0]]
    call shift_focus (Player.Harem[0])
    call set_the_scene
    call clear_the_room (Player.Harem[0])


    if Round2:
        "You pull [Party[0].name] aside for a moment."
        ch_p "Hey, have you changed your mind about [Newbie.name] lately?"
    else:
        $ Party[0].change_face("bemused")
        "[Party[0].name] pulls you aside and wants to talk about something."


        if Party[0] == RogueX:
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



    if Party[0].GirlLikeCheck(Newbie) >= 800:
        $ Party[0].change_face("sly")
    elif Party[0].GirlLikeCheck(Newbie) >= 600:
        pass
    else:

        $ Party[0].change_face("angry",Mouth="normal")


    if Party[0] == RogueX:
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            ch_r "She is pretty sexy, I guess."
        elif Party[0].GirlLikeCheck(Newbie) >= 600:

            ch_r "I like her just fine, I was just wondering where it was headed."
        else:

            ch_r "I'm not really a fan'a hers."
    elif Party[0] == KittyX:
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            ch_k "She's kinda hot, I get that. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 600:

            ch_k "She's ok, sure, but I'm not sure. . ."
        else:

            ch_k "I don't really like her much."
    elif Party[0] == EmmaX:
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            ch_e "I think she's quite the catch."
        elif Party[0].GirlLikeCheck(Newbie) >= 600:

            ch_e "I do like her, but have some concerns."
        else:

            ch_e "I don't really approve."
    elif Party[0] == LauraX:
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            ch_l "She's pretty hot, I get it."
        elif Party[0].GirlLikeCheck(Newbie) >= 600:

            ch_l "She's ok, I guess."
        else:

            ch_l "I don't like her."
    elif Party[0] == JeanX:
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            ch_j "I get it, she's hot enough."
        elif Party[0].GirlLikeCheck(Newbie) >= 600:

            ch_j "She's. . . fine."
        else:

            ch_j "You probably shouldn't be seen around her."
    elif Party[0] == StormX:
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            ch_s "She is very beautiful, certainly."
        elif Party[0].GirlLikeCheck(Newbie) >= 600:

            ch_s "She is a good girl, certainly. . ."
        else:

            ch_s "I do not think I like her much."
    elif Party[0] == JubesX:
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            ch_v "Ok, she's totally hot, but. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 600:

            ch_v "She's. . . fine, but. . ."
        else:

            ch_v "I'm not there for it."




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

            $ Line = "yy"
            $ Party[0].change_stat("love", 90, 5)
            $ Party[0].change_stat("obedience", 50, 5)
            $ Party[0].change_stat("inhibition", 90, 10)
        elif ApprovalCheck(Party[0], 1800):

            $ Line = "ym"
            $ Party[0].change_stat("obedience", 50, 5)
        elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 500:

            $ Line = "ym"
        else:

            $ Line = "yn"
            $ Party[0].change_stat("love", 90, -10)

    if Line == "m":
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            $ Line = "my"
            $ Party[0].change_stat("inhibition", 90, 5)
        elif ApprovalCheck(Party[0], 1800):

            $ Line = "mm"
        elif ApprovalCheck(Party[0], 1500) and Party[0].GirlLikeCheck(Newbie) >= 600:

            $ Line = "mm"
        else:

            $ Line = "mn"

    if Line == "n":
        if Party[0].GirlLikeCheck(Newbie) >= 800:

            $ Line = "ny"
            $ Party[0].change_stat("inhibition", 90, 10)
        elif ApprovalCheck(Party[0], 1700):

            $ Line = "nm"
            $ Party[0].change_stat("inhibition", 90, 5)
        elif ApprovalCheck(Party[0], 1300) and Party[0].GirlLikeCheck(Newbie) >= 500:

            $ Line = "nm"
            $ Party[0].change_stat("love", 90, 5)
        else:

            $ Line = "nn"
            $ Party[0].change_stat("love", 90, 10)





    if Line == "yn" or Line == "mn" or Line == "nn":
        $ Party[0].change_face("angry")
    elif Line == "yy" or Line == "ny" or Line == "my":
        $ Party[0].change_face("sexy")
    else:
        $ Party[0].change_face("bemused")


    if Party[0] == RogueX:
        if Line == "yy":

            ch_r "Great, sounds fun."
        elif Line == "my":

            ch_r "Oh, don't let me stop you."
        elif Line == "ny":

            ch_r "Oh. Well maybe you should!"

        elif Line == "ym" or Line == "mm":

            ch_r "Yeah, I guess I can live with that."
        elif Line == "nm":

            ch_r "Hmm, not that I would have minded."

        elif Line == "yn" or Line == "mn":

            ch_r "I don't think I'm really cool with that."
        elif Line == "nn":

            ch_r "Good to hear."

    elif Party[0] == KittyX:
        if Line == "yy":

            ch_k "Cool, sounds fun."
        elif Line == "my":

            ch_k "Oh, seriously, it's fine with me!"
        elif Line == "ny":

            ch_k "You might want to, she's hot!"

        elif Line == "ym" or Line == "mm":

            ch_k "Yeah, I can[KittyX.like]live with that."
        elif Line == "nm":

            ch_k "Ok, I would have been ok with it though."

        elif Line == "yn" or Line == "mn":

            ch_k "That's not really cool with me."
        elif Line == "nn":

            ch_k "Good, that wouldn't have been cool."

    elif Party[0] == EmmaX:
        if Line == "yy":

            ch_e "Lovely. . ."
        elif Line == "my":

            ch_e "Oh, please do, she's lovely."
        elif Line == "ny":

            ch_e "Pity, I rather like her."

        elif Line == "ym" or Line == "mm":

            ch_e "I suppose I can make do then."
        elif Line == "nm":

            ch_e "You could do a lot worse."

        elif Line == "yn" or Line == "mn":

            ch_e "I don't think that will be acceptable."
        elif Line == "nn":

            ch_e "Probably for the best."

    elif Party[0] == LauraX:
        if Line == "yy":

            ch_l "Nice."
        elif Line == "my":

            ch_l "Come on, she's pretty great."
        elif Line == "ny":

            ch_l "You sure? She's hot."

        elif Line == "ym" or Line == "mm":

            ch_l "Fine, I can work with that."
        elif Line == "nm":

            ch_l "Ok. I'm cool with it if you do though."

        elif Line == "yn" or Line == "mn":

            ch_l "Nope."
        elif Line == "nn":

            ch_l "Good."

    elif Party[0] == JeanX:
        if Line == "yy":

            ch_j "Well, ok, sure."
        elif Line == "my":

            ch_j "Well. . . she could be fun. . ."
        elif Line == "ny":

            ch_j "Really? I mean, she could be fun."

        elif Line == "ym" or Line == "mm":

            ch_j "Well, ok, fine. . ."
        elif Line == "nm":

            ch_j "Ok. I could think about it though."

        elif Line == "yn" or Line == "mn":

            ch_j "Well, cut it out."
        elif Line == "nn":

            ch_j "Yeah."

    elif Party[0] == StormX:
        if Line == "yy":

            ch_s "Oh, that will be nice. . ."
        elif Line == "my":

            ch_s "Oh, you definitely should!"
        elif Line == "ny":

            ch_s "That is too bad. You would go well together."

        elif Line == "ym" or Line == "mm":

            ch_s "Well, that should be fine."
        elif Line == "nm":

            ch_s "You might want to reconsider. . ."

        elif Line == "yn" or Line == "mn":

            ch_s "I do not think I could deal with her."
        elif Line == "nn":

            ch_s "Yes, I would agree with that."

    elif Party[0] == JubesX:
        if Line == "yy":

            ch_v "Ok, cool."
        elif Line == "my":

            ch_v "Yeah, sure, I'm down with it."
        elif Line == "ny":

            ch_v "Ok, but you might be missing out!"

        elif Line == "ym" or Line == "mm":

            ch_v "Ok, yeah, I can deal."
        elif Line == "nm":

            ch_v "Ok, your call, I guess."

        elif Line == "yn" or Line == "mn":

            ch_v "Well. . . I might have some feelings."
        elif Line == "nn":

            ch_v "Glad we're on the same page here."



    if Line != "yy" and Line != "nn":

        menu:
            extend ""
            "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):

                $ Line = "yy"
                $ Party[0].change_face("smile")
                $ Party[0].change_stat("love", 90, 10)
                $ Party[0].change_stat("obedience", 50, 10)
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

                $ Line = "nn"
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

            "I'm asking her in anyway." if Line in ("mn","yn"):

                pass

            "Well, I'm going to pass anyway." if Line in ("nm","ny","mm"):

                $ Line = "nn"
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



    if Line == "mn" or Line == "yn":


        if ApprovalCheck(Party[0], 1600) and Party[0].GirlLikeCheck(Newbie) >= 500:
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
                ch_j "But this counts as your Christmas present."
            elif Party[0] == StormX:
                ch_s ". . ."
                ch_s "I can accept that."
            elif Party[0] == JubesX:
                ch_v "Whatever. Fine."
            $ Line = "yy"
        else:
            $ Party[0].change_face("angry",Eyes="side")
            $ Party[0].change_stat("love", 90, -25)
            $ Party[0].change_stat("inhibition", 90, 10)
            if Party[0] == RogueX:
                ch_r "I just don't like you that much, [RogueX.player_petname]."
                ch_r "I'm out."
            elif Party[0] == KittyX:
                ch_k "You aren't that cute, [KittyX.player_petname]."
                ch_k "I'm done."
            elif Party[0] == EmmaX:
                ch_e "Don't overestimate yourself, [EmmaX.player_petname]."
                ch_e "We're done."
            elif Party[0] == LauraX:
                ch_l "Too far, [LauraX.player_petname]."
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
            call Remove_Girl (Party[0])


    $ Party = []
    if Line == "yy":
        if Newbie.Tag + "No" in Player.Traits:
            $ Player.Traits.remove(Newbie.Tag + "No")
        $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
        $ Player.Traits.append(Newbie.Tag + "Yes")
        "You should give [Newbie.name] a call."
    else:
        $ Player.Traits.append(Newbie.Tag + "No")
    return






label Harem_Start(Newbie=0, Round2=0):




    $ Line = 0

    if len(Player.Harem) < 2:

        return

    $ Party = [Player.Harem[0],Player.Harem[1]]

    call Present_Check
    $ Party = [Player.Harem[0],Player.Harem[1]]
    call shift_focus (Player.Harem[0])
    call set_the_scene

    $ Party[0].change_face("bemused")
    $ Party[1].change_face("bemused")
    if Round2:
        "You call [Party[0].name] and [Party[1].name] over."
        ch_p "I was wondering if you'd changed your mind about [Newbie.name]."
    else:
        "[Party[0].name] pulls you aside and wants to talk about something."


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




    if Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:
        pass
    elif Party[0].GirlLikeCheck(Newbie) >= 700:

        $ Party[1].change_face("angry",Mouth="normal")
    elif Party[1].GirlLikeCheck(Newbie) >= 700:

        $ Party[0].change_face("angry",Mouth="normal")
    else:

        $ Party[0].change_face("angry",Mouth="normal")
        $ Party[1].change_face("angry",Mouth="normal")

    if Party[0] == RogueX:
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            ch_r "Now we like her just fine, and we can't say we don't like the idea much."
        elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:

            ch_r "Now we like her just fine, but we don't know about share'in."
        elif Party[0].GirlLikeCheck(Newbie) >= 700:

            ch_r "Now I like her just fine, but [Party[1].name] ain't so sure."
        elif Party[1].GirlLikeCheck(Newbie) >= 700:

            ch_r "Now [Party[1].name] seems to like her, but I'm not so sure."
        else:

            ch_r "Neither'a us is really cool with that."
    elif Party[0] == KittyX:
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            ch_k "She's kinda hot, we get that. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:

            ch_k "She's ok, sure, but we're not sure. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 700:

            ch_k "I like her, but I don't know about [Party[1].name]."
        elif Party[1].GirlLikeCheck(Newbie) >= 700:

            ch_k "[Party[1].name] likes her, but I don't know."
        else:

            ch_k "We don't really like her much."
    elif Party[0] == EmmaX:
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            ch_e "I think we agree that she's a nice catch."
        elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:

            ch_e "We do like her, but we have some concerns."
        elif Party[0].GirlLikeCheck(Newbie) >= 700:

            ch_e "[Party[1].name] doesn't really approve."
        elif Party[1].GirlLikeCheck(Newbie) >= 700:

            ch_e "[Party[1].name] seems to think she's acceptable."
        else:

            ch_e "We don't really approve."
    elif Party[0] == LauraX:
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            ch_l "She's pretty hot, we get it."
        elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:

            ch_l "She's ok, I guess."
        elif Party[0].GirlLikeCheck(Newbie) >= 700:

            ch_l "She's fine, but [Party[1].name] doesn't like her."
        elif Party[1].GirlLikeCheck(Newbie) >= 700:

            ch_l "[Party[1].name] likes her. I don't."
        else:

            ch_l "We don't like her."
    elif Party[0] == JeanX:
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            ch_j "I get it, she's hot enough."
        elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:

            ch_j "She's. . . fine."
        elif Party[0].GirlLikeCheck(Newbie) >= 700:

            ch_j "I think she's fine, but [Party[1].name] doesn't like her."
            ch_j "For whatever that's worth. . ."
        elif Party[1].GirlLikeCheck(Newbie) >= 700:

            ch_j "[Party[1].name] likes her. I don't."
            ch_j "So I think you know the right answer to this one. . ."
        else:

            ch_j "You probably shouldn't be seen around her."
    elif Party[0] == StormX:
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            ch_s "We agree that she is very beautiful. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:

            ch_s "She is a good girl, but we do have some concerns. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 700:

            ch_s "I like her, but [Party[1].name] does not approve."
        elif Party[1].GirlLikeCheck(Newbie) >= 700:

            ch_s "[Party[1].name] appears to like her, I am unsure."
        else:

            ch_s "We do not like her very much."

    elif Party[0] == JubesX:
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            ch_v "Ok, she's totally hot, but. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 600 and Party[1].GirlLikeCheck(Newbie) >= 600:

            ch_v "She's. . . fine, but. . ."
        elif Party[0].GirlLikeCheck(Newbie) >= 700:

            ch_v "She's. . . fine, but, [Party[1].name]. . ."
        elif Party[1].GirlLikeCheck(Newbie) >= 700:

            ch_v "[Party[1].name] likes her, but I don't know."
        else:

            ch_v "We're not there for it."




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

            $ Line = "yy"
            $ Party[0].change_stat("love", 90, 5)
            $ Party[0].change_stat("obedience", 50, 5)
            $ Party[0].change_stat("inhibition", 90, 10)
            $ Party[1].change_stat("love", 90, 5)
            $ Party[1].change_stat("obedience", 50, 5)
            $ Party[1].change_stat("inhibition", 90, 10)
        elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):

            $ Line = "ym"
            $ Party[0].change_stat("obedience", 50, 10)
            $ Party[1].change_stat("obedience", 50, 10)
        elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
            if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:

                $ Line = "ym"
                $ Party[0].change_stat("obedience", 80, 15)
                $ Party[1].change_stat("obedience", 80, 15)
            else:

                $ Line = "yn"
                $ Party[0].change_stat("love", 90, -5)
                $ Party[0].change_stat("obedience", 50, -5)
                $ Party[1].change_stat("love", 90, -5)
                $ Party[1].change_stat("obedience", 50, -5)
        else:

            $ Line = "yn"
            $ Party[0].change_stat("love", 90, -10)
            $ Party[0].change_stat("obedience", 50, -5)
            $ Party[1].change_stat("love", 90, -10)
            $ Party[1].change_stat("obedience", 50, -5)

    if Line == "m":
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            $ Line = "my"
            $ Party[0].change_stat("inhibition", 90, 5)
            $ Party[1].change_stat("inhibition", 90, 5)
        elif ApprovalCheck(Party[0], 1800) and ApprovalCheck(Party[1], 1800):

            $ Line = "mm"
        elif ApprovalCheck(Party[0], 1500) and ApprovalCheck(Party[1], 1500):
            if Party[0].GirlLikeCheck(Newbie) >= 600 or Party[1].GirlLikeCheck(Newbie) >= 600:

                $ Line = "mm"
            else:

                $ Line = "mn"
        else:

            $ Line = "mn"

    if Line == "n":
        if Party[0].GirlLikeCheck(Newbie) >= 800 and Party[1].GirlLikeCheck(Newbie) >= 800:

            $ Line = "ny"
            $ Party[0].change_stat("inhibition", 90, 10)
            $ Party[1].change_stat("inhibition", 90, 10)
        elif ApprovalCheck(Party[0], 1700) and ApprovalCheck(Party[1], 1700):

            $ Line = "nm"
            $ Party[0].change_stat("inhibition", 90, 5)
        elif ApprovalCheck(Party[0], 1300) and ApprovalCheck(Party[1], 1300):
            if Party[0].GirlLikeCheck(Newbie) >= 500 and Party[1].GirlLikeCheck(Newbie) >= 500:

                $ Line = "nm"
            else:

                $ Line = "nn"
                $ Party[0].change_stat("love", 90, 5)
                $ Party[0].change_stat("inhibition", 90, 5)
                $ Party[1].change_stat("love", 90, 5)
                $ Party[1].change_stat("inhibition", 90, 5)
        else:

            $ Line = "nn"
            $ Party[0].change_stat("love", 90, 5)
            $ Party[0].change_stat("inhibition", 90, 5)
            $ Party[1].change_stat("love", 90, 5)
            $ Party[1].change_stat("inhibition", 90, 5)





    if Line == "yn" or Line == "mn" or Line == "nn":
        $ Party[0].change_face("angry")
        $ Party[1].change_face("angry")
    elif Line == "yy" or Line == "ny" or Line == "my":
        $ Party[0].change_face("sexy")
        $ Party[1].change_face("sexy")
    else:
        $ Party[0].change_face("bemused")
        $ Party[1].change_face("bemused")


    if Party[0] == RogueX:
        if Line == "yy":

            ch_r "Great, sounds fun."
        elif Line == "my":

            ch_r "Oh, don't let me stop you."
        elif Line == "ny":

            ch_r "Oh. Well maybe you should!"

        elif Line == "ym" or Line == "mm":

            ch_r "Yeah, I guess we can live with that."
        elif Line == "nm":

            ch_r "Hmm, not that we would have minded."

        elif Line == "yn" or Line == "mn":

            ch_r "I don't think we're really cool with that."
        elif Line == "nn":

            ch_r "Good to hear."

    elif Party[0] == KittyX:
        if Line == "yy":

            ch_k "Cool, sounds fun."
        elif Line == "my":

            ch_k "Oh, seriously, it's fine with us!"
        elif Line == "ny":

            ch_k "You might want to, she's hot!"

        elif Line == "ym" or Line == "mm":

            ch_k "Yeah, we can[KittyX.like]live with that."
        elif Line == "nm":

            ch_k "Ok, we would have been ok with it though."

        elif Line == "yn" or Line == "mn":

            ch_k "That's not really cool with us."
        elif Line == "nn":

            ch_k "Good, that wouldn't have been cool."

    elif Party[0] == EmmaX:
        if Line == "yy":

            ch_e "Lovely. . ."
        elif Line == "my":

            ch_e "Oh, please do, she's lovely."
        elif Line == "ny":

            ch_e "Pity, I rather like her."

        elif Line == "ym" or Line == "mm":

            ch_e "I suppose we can make do then."
        elif Line == "nm":

            ch_e "You could do a lot worse."

        elif Line == "yn" or Line == "mn":

            ch_e "I don't think that will be acceptable."
        elif Line == "nn":

            ch_e "Probably for the best."

    elif Party[0] == LauraX:
        if Line == "yy":

            ch_l "Nice."
        elif Line == "my":

            ch_l "Come on, she's pretty great."
        elif Line == "ny":

            ch_l "You sure? She's hot."

        elif Line == "ym" or Line == "mm":

            ch_l "Fine, we can work with that."
        elif Line == "nm":

            ch_l "Ok. We're cool with it if you do though."

        elif Line == "yn" or Line == "mn":

            ch_l "Nope."
        elif Line == "nn":

            ch_l "Good."

    elif Party[0] == JeanX:
        if Line == "yy":

            ch_j "Well, ok, sure."
        elif Line == "my":

            ch_j "Well. . . she could be fun. . ."
        elif Line == "ny":

            ch_j "Really? I mean, she could be fun."

        elif Line == "ym" or Line == "mm":

            ch_j "Well, ok, fine. . ."
        elif Line == "nm":

            ch_j "Ok. I could think about it though."

        elif Line == "yn" or Line == "mn":

            ch_j "Well, cut it out."
        elif Line == "nn":

            ch_j "Yeah."

    elif Party[0] == StormX:
        if Line == "yy":

            ch_s "Oh, that will be nice. . ."
        elif Line == "my":

            ch_s "Oh, you definitely should!"
        elif Line == "ny":

            ch_s "That is too bad. You would go well together."

        elif Line == "ym" or Line == "mm":

            ch_s "Well, that should be fine."
        elif Line == "nm":

            ch_s "You might want to reconsider. . ."

        elif Line == "yn" or Line == "mn":

            ch_s "I do not think we could deal with her."
        elif Line == "nn":

            ch_s "Yes, we could agree with that."

    elif Party[0] == JubesX:
        if Line == "yy":

            ch_v "Ok, cool."
        elif Line == "my":

            ch_v "Yeah, sure, I guess we're down with that down with it."
        elif Line == "ny":

            ch_v "Ok, but you might be missing out!"

        elif Line == "ym" or Line == "mm":

            ch_v "Ok, yeah, we can deal."
        elif Line == "nm":

            ch_v "Ok, your call, I guess."

        elif Line == "yn" or Line == "mn":

            ch_v "Well. . . we might have some feelings."
        elif Line == "nn":

            ch_v "Glad we're on the same page here."



    if Line != "yy" and Line != "nn":

        menu:
            extend ""
            "Ok, then I guess I will ask her to join us." if Line in ("my","ny","ym","mm","nm"):

                $ Line = "yy"
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

                $ Line = "nn"
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
            "I'm asking her in anyway." if Line in ("mn","yn"):

                pass

            "Well, I'm going to pass anyway." if Line in ("ym","my","nm","ny","mm"):

                $ Line = "nn"
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


        if Line == "yy" or Line == "nn":
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
            $ Line = "yy"
        elif Line == "mn" or Line == "yn":

            $ Count = 0
            while Count < 2:
                if ApprovalCheck(Party[Count], 1600) and Party[Count].GirlLikeCheck(Newbie) >= 500:

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
                    $ Line = "yy"
                else:

                    $ Party[Count].change_face("angry",Eyes="side")
                    $ Party[Count].change_stat("love", 90, -25)
                    $ Party[Count].change_stat("inhibition", 90, 10)
                    if Party[Count] == RogueX:
                        ch_r "I just don't like you that much, [RogueX.player_petname]."
                        ch_r "I'm out."
                    elif Party[Count] == KittyX:
                        ch_k "You aren't that cute, [KittyX.player_petname]."
                        ch_k "I'm done."
                    elif Party[Count] == EmmaX:
                        ch_e "Don't overestimate yourself, [EmmaX.player_petname]."
                        ch_e "We're done."
                    elif Party[Count] == LauraX:
                        ch_l "Too far, [LauraX.player_petname]."
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
                    call Remove_Girl (Party[Count])
                $ Count += 1



    if Line == "yy":
        if Newbie.Tag + "No" in Player.Traits:
            $ Player.Traits.remove(Newbie.Tag + "No")
        $ Player.DrainWord(Newbie.Tag + "No",0,0,1)
        $ Player.Traits.append(Newbie.Tag + "Yes")
        $ Count = len(Player.Harem)
        while Count:
            $ Count -= 1
            $ Player.Harem[Count].DrainWord("saw with "+Newbie.Tag,0,0,1)
        "You should give [Newbie.name] a call."
    else:
        $ Player.Traits.append(Newbie.Tag + "No")

    $ Party = []
    $ Count = 0
    return

label Harem_Initiation(BO=[], BO2=[]):


    $ BO = Player.Harem[:]
    while BO:
        $ BO2 = Player.Harem[:]
        while BO2:
            if BO[0] != BO2[0] and "poly " + BO2[0].Tag not in BO[0].Traits:
                $ BO[0].Traits.append("poly " + BO2[0].Tag)
            if BO[0] != BO2[0] and "saw with " + BO2[0].Tag in BO[0].Traits:
                $ BO[0].DrainWord("saw with " + BO2[0].Tag,0,0,1)
            $ BO2.remove(BO2[0])
        $ BO.remove(BO[0])
    return





label Study_Session(BO=[]):

    $ Party = []

    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current:
            $ Party.append(BO[0])
        $ BO.remove(BO[0])

    if not Party:
        "There's nobody here to study with."
        menu:
            "Study anyway?"
            "Yes":
                $ Player.XP += 5
                $ Round -= 30 if Round >= 30 else Round
            "Never mind.":
                pass
        return

    $ renpy.random.shuffle(Party)

    if time_index >= 3:
        if Party[0] == JubesX and len(Party) < 2:

            pass
        else:
            if EmmaX in Party:
                ch_e "It's a little late for a study session, maybe tomorrow."
            elif Party[0] == RogueX:
                ch_r "It's a little late for studying, maybe tomorrow."
            elif Party[0] == KittyX:
                ch_k "It's kinda late for studying. . . Tomorrow?"
            elif Party[0] == LauraX:
                ch_l "It's late. Maybe tomorrow."
            elif Party[0] == JeanX:
                ch_j "-Yawn- Maybe tomorrow. . ."
            elif Party[0] == StormX:
                ch_s "It is getting a bit late for study."
            elif Party[0] == JubesX:
                ch_v "Well, it is getting kinda late. . ."
                ch_v "I don't think it'd be good for you guys. . ."
            $ Party = []
            return

    if Round <= 30:
        if EmmaX in Party:
            ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
        elif Party[0] == RogueX:
            ch_r "I don't know that there's time for that, maybe if we wait a bit. . ."
        elif Party[0] == KittyX:
            ch_k "I don't know that there's time for that, maybe if we wait a bit. . ."
        elif Party[0] == LauraX:
            ch_l "I was about to take a break, maybe wait a bit."
        elif Party[0] == JeanX:
            ch_j "I need a break, gimme a minute. . ."
        elif Party[0] == StormX:
            ch_s "I need a quick break, perhaps in a few minutes."
        elif Party[0] == JubesX:
            ch_v "We could maybe get some snacks first. . ."
        $ Party = []
        return

    elif EmmaX in Party and len(Party) >= 2:
        ch_e "I suppose you could both use some work."
    else:
        if EmmaX in Party:
            ch_e "Very well."
        elif Party[0] == RogueX:
            ch_r "Sure."
        elif Party[0] == KittyX:
            ch_k "Sure."
        elif Party[0] == LauraX:
            ch_l "Fine."
        elif Party[0] == JeanX:
            ch_j "I guess."
        elif Party[0] == StormX:
            ch_s "I suppose we could go over a few things. . ."
        elif Party[0] == JubesX:
            ch_v "I guess we could study. . ."


    $ Player.recent_history.append("study")
    $ Player.XP += 5
    $ primary_action = 0
    $ Line = renpy.random.choice(["you run you through some basic routines, it's fairly uneventful.",
                    "You study up for the mutant biology test.",
                    "You study for the math quiz.",
                    "You get bored and discuss student gossip instead.",
                    "You study for a few hours, that was fun.",
                    "You spend the next few hours studying the lit test.",
                    "You study for the game design course."])
    "[Line]"
    $ Line = 0

    $ Party[0].change_stat("love", 80, 2)
    $ Party[0].XP += 5
    if len(Party) >= 2:
        $ Party[1].change_stat("love", 80, 2)
        $ Party[0].GLG(Party[1],700,5,1)
        $ Party[1].GLG(Party[0],700,5,1)
        $ Party[1].XP += 5


    $ D20 = renpy.random.randint(1, 20)


    if len(Party) >= 2 and EmmaX in Party and "three" not in EmmaX.history:
        $ Line = "no"

    if Line != "no" and D20 >= 10:
        call Frisky_Study
    else:

        if EmmaX in Party:
            ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
        elif Party[0] == RogueX:
            ch_r "It's getting a bit late, we should wrap this up. . ."
        elif Party[0] == KittyX:
            ch_k "It's kinda late, we should probably stop. . ."
        elif Party[0] == LauraX:
            ch_l "I'm bored now."
        elif Party[0] == JeanX:
            ch_j "Ok, that's enough of that. . ."
        elif Party[0] == StormX:
            ch_s "I think that will be enough for now."
        elif Party[0] == JubesX:
            ch_v "Ugh, my head hurts!"
        $ Player.XP += 5
    $ Line = 0
    $ Party = []
    if time_index >= 3:
        $ Round = 10
        return
    call Wait
    call Girls_Location
    return




label Frisky_Study(Prime_Bonus=0, Second=0, Line=0, Second_Bonus=0):




    call shift_focus (Party[0])

    if len(Party) >= 2:
        $ Second = Party[1]

    if Party[0] == EmmaX and "classcaught" not in EmmaX.history:

        "[EmmaX.name] leans close to you for a moment, but then catches herself and pulls back."
    elif Party[0] == EmmaX and Second and ("three" not in EmmaX.history or "taboo" not in EmmaX.history):

        "[EmmaX.name] starts to lean close to you, but then notices [Second.name]."
        $ Party[0].change_face("sly",1,Eyes="side")
        "She stops immediately and looks a bit embarrassed."
    elif D20 > 17 and ApprovalCheck(Party[0], 1000) and Party[0].action_counter["blowjob"] > 5:
        $ Line = "blowjob"
    elif D20 > 14 and Party[0] == JubesX and ApprovalCheck(Party[0], 1000) and Party[0].action_counter["blowjob"] > 5:
        $ Line = "blowjob"
    elif D20 > 14 and ApprovalCheck(Party[0], 1000) and Party[0].action_counter["handjob"] >= 5:
        $ Line = "handjob"
    elif D20 > 10 and (ApprovalCheck(Party[0], 1300) or (Party[0].action_counter["masturbation"] and ApprovalCheck(Party[0], 1000))) and Party[0].lust >= 70:
        $ Line = "masturbate"
    elif D20 > 10 and ApprovalCheck(Party[0], 1200) and Party[0].lust >= 30:
        $ Line = "strip"
    elif ApprovalCheck(Party[0], 700) and Party[0].action_counter["kiss"] > 1:
        $ Line = "kissing"
    elif ApprovalCheck(Party[0], 500):
        $ Line = "snuggle"
        if Party[0] != JeanX or ApprovalCheck(Party[0], 700,"L"):
            $ Line = "snuggle"
        else:
            "[Party[0].name] briefly rests against your shoulder, but then shakes herself and pulls back."
            $ Line = 0


    if not Line and len(Party) >= 2 and not Prime_Bonus:


        $ Party.reverse()
        call Frisky_Study (1)
        return
    elif not Line or Line == "strip":
        pass
    elif Line == "blowjob":
        $ Party[0].change_face("sly")
        if Party[0] == KittyX:
            "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
            "She unzips you pants and pulls your dick out, stroking it slowly."
            "She then dives her head under the book, and starts to lick it."
        else:
            "[Party[0].name] get predatory grin, and begins to unzip your pants."
            "She pulls your dick out and pops it into her mouth."
    elif Line == "handjob":
        $ Party[0].change_face("sly")
        if Party[0] == KittyX:
            "[KittyX.name] reaches her hand through your textbook and you can feel it in your lap."
            "She runs her finger along your erection, her hand passing through the jeans to touch your bare skin."
            "She unzips you pants and pulls your dick out, stroking it slowly."
        elif Party[0] == JeanX and D20 > 15:
            "As you study, you feel something stirring along your cock, a slight hint of pressure."
            menu:
                "Go with it":
                    "After a moment, you can feel a tugging on your zipper as it releases."
                    "You cock floats free of your pants, lifted half under its own power and half due to. . ."
                    $ Party[0].change_face("sly",Eyes="leftside")
                    "You glance over at [JeanX.name] and she smiles mischieviously as the pressure builds."
                    "You can feel a strong rubbing sensation along the length of the shaft, up and down."
                    "It feels similar to a hand or mouth wrapped around itpassing from root to tip and back."
                    "[JeanX.name] throws an arm over your shoulders and leans against you as this pressure continues. . ."
                "Flex your power to shut it down":
                    $ Party[0].change_face("sad")
                    $ Party[0].change_stat("love", 80, -2)
                    $ Party[0].change_stat("obedience", 50, 3)
                    $ Party[0].change_stat("obedience", 80, 5)
                    $ Party[0].change_stat("inhibition", 90, -2)
                    ch_j "Aw. . ."
                    $ Line = 0
        else:
            "[Party[0].name] get predatory grin, and begins to unzip your pants."
            "She pulls your dick out and begins to slowly stroke it."
    elif Line == "masturbate":
        $ Party[0].change_face("sly", Eyes="side")
        "[Party[0].name] leans back a bit and starts to rub herself."
        $ primary_action = "masturbation"
    elif Line == "kissing":
        "[Party[0].name] leans close to you, and leans in for a kiss."
    elif Line == "snuggle":
        "[Party[0].name] leans close to you and you spend the rest of the study session nuzzled close."


    if Line == "strip":
        if Party[0] != EmmaX and EmmaX in Party and ApprovalCheck(EmmaX, 1200) and EmmaX.lust >= 30:
            $ Party.reverse()

        if StormX in Party and renpy.random.randint(1,2) > 1:
            $ Party.reverse()


        call Group_Strip_Study
    elif Line and len(Party) < 2:

        call expression Party[0].Tag + "_SexAct" pass (Line)
    elif Line:

        if Line == "snuggle":
            call Date_Sex_Break (Party[0], Second, 2)
            if _return == 3:
                $ Second.change_face("angry")
                "[Second.name] glowers at you a bit."
                $ Party[0].GLG(Second,700,5,1)
                $ Second.GLG(Party[0],700,5,1)
        else:
            call Date_Sex_Break (Party[0], Second)

        if _return == 4:
            if Line == "blowjob":
                "[Party[0].name] lets your dick fall out of her mouth."
                "You zip your pants back up."
            elif Line == "handjob":
                "[Party[0].name] lets your dick drop into your lap."
                "You zip your pants back up."
            else:
                "[Party[0].name] stops what she's doing."

            $ Party[0].change_face("sad")
            if Party[0] == RogueX:
                ch_r "Buzzkill."
            elif Party[0] == KittyX:
                ch_k "Booo."
            elif Party[0] == EmmaX:
                ch_e "Oh, very well."
            elif Party[0] == LauraX:
                ch_l "Be that way."
            elif Party[0] == JeanX:
                ch_j "Aw. . ."
            elif Party[0] == StormX:
                ch_s "How unfortunate."
            elif Party[0] == JubesX:
                ch_v "Jerk!"
        elif Line != "snuggle":


            if _return == 3:

                if Party[0] == RogueX:
                    ch_r "Mind if I continue?"
                elif Party[0] == KittyX:
                    ch_k "I can keep going?"
                elif Party[0] == EmmaX:
                    ch_e "You don't mind if I continue?"
                elif Party[0] == LauraX:
                    ch_l "Keep going?"
                elif Party[0] == JeanX:
                    ch_j "Ok, back to it. . ."
                elif Party[0] == StormX:
                    ch_s "Well, would you like me to stop?"
                elif Party[0] == JubesX:
                    ch_v "Not interested?"
                menu:
                    extend ""
                    "Go ahead.":
                        $ Party[0].change_face("sly")
                        if Party[0] == RogueX:
                            ch_r "Nice."
                        elif Party[0] == KittyX:
                            ch_k "Cool."
                        elif Party[0] == EmmaX:
                            ch_e "Lovely."
                        elif Party[0] == LauraX:
                            ch_l "Un."
                        elif Party[0] == JeanX:
                            ch_j "Mmm. . ."
                        elif Party[0] == StormX:
                            ch_s "That is what I'd hoped. . ."
                        elif Party[0] == JubesX:
                            ch_v "Sweet!"
                    "We should stop.":
                        $ Party[0].change_face("sad")
                        if Party[0] == RogueX:
                            ch_r "Hmph."
                        elif Party[0] == KittyX:
                            ch_k "Lame."
                        elif Party[0] == EmmaX:
                            ch_e "Spoil sport."
                        elif Party[0] == LauraX:
                            ch_l "Grr."
                        elif Party[0] == JeanX:
                            ch_j "Aw. . ."
                        elif Party[0] == StormX:
                            ch_s "Pity."
                        elif Party[0] == JubesX:
                            ch_v "Aw!"
                        $ Party[0].change_face("normal")
                        return

            call expression Party[0].Tag + "_SexAct" pass (Line)
        if len(Party) >= 2:
            $ Party[0].GLG(Party[1],900,10,1)
            $ Party[1].GLG(Party[0],900,10,1)
    else:


        return
    if Party:
        $ Party[0].AddWord(1,0,0,0,"frisky")
    if len(Party) >= 2:
        $ Party[1].AddWord(1,0,0,0,"frisky")

    "Well that was certainly a productive use of your study time. . ."
    return




label Girls_Caught(Girl=0, TotalCaught=0, Shame=0, Count=0, T_Pet=0, BO=[]):
    call shift_focus (Girl)
    call Checkout
    Girl.voice "!!!"
    $ Line = primary_action
    call Trig_Reset
    $ Girl.change_outfit()
    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current:
            $ BO[0].location = "bg_study"
        $ TotalCaught += BO[0].event_counter["caught"]
        $ BO.remove(BO[0])
    $ bg_current = "bg_study"
    call set_the_scene (0)
    show Professor at sprite_location(stage_left)

    if Girl == RogueX:
        show Rogue_Sprite at sprite_location(stage_right) with ease
    elif Girl == KittyX:
        show Kitty_Sprite at sprite_location(stage_right) with ease
    elif Girl == EmmaX:
        show Emma_Sprite at sprite_location(stage_right) with ease
    elif Girl == LauraX:
        show Laura_Sprite at sprite_location(stage_right) with ease
    elif Girl == JeanX:
        show Jean_Sprite at sprite_location(stage_right) with ease
    elif Girl == StormX:
        show Storm_Sprite at sprite_location(stage_right) with ease
    elif Girl == JubesX:
        show Jubes_Sprite at sprite_location(stage_right) with ease
    call OutfitShame (Girl, 20)

    $ Count = Girl.event_counter["caught"]

    if Partner == RogueX:
        show Rogue_Sprite at sprite_location(stage_far_right) with ease
    elif Partner == KittyX:
        show Kitty_Sprite at sprite_location(stage_far_right) with ease
    elif Partner == EmmaX:
        show Emma_Sprite at sprite_location(stage_far_right) with ease
    elif Partner == LauraX:
        show Laura_Sprite at sprite_location(stage_far_right) with ease
    elif Partner == JeanX:
        show Jean_Sprite at sprite_location(stage_far_right) with ease
    elif Partner == StormX:
        show Storm_Sprite at sprite_location(stage_far_right) with ease
    elif Partner == JubesX:
        show Jubes_Sprite at sprite_location(stage_far_right) with ease

    call XavierFace ("shocked")
    $ Girl.change_face("sad")
    if (Girl == EmmaX or Partner == EmmaX) and (Girl == StormX or Partner == StormX):
        ch_x "I'm very disappointed in the both of you!."
        ch_x "You should BOTH know better than this!"
    elif Girl == StormX or Partner == StormX:
        ch_x "I'm very disappointed in your behavior, particularly yours, Ororo."
    elif Girl == EmmaX or Partner == EmmaX:
        ch_x "I'm very disappointed in your behavior, particularly yours, Emma."
    else:
        ch_x "I'm very disappointed in your behavior, the both of you."

    if Line == "fondle_thighs" or Line == "fondle_breasts" or Line == "fondle_pussy" or Line == "hotdog" or Line == "handjob":
        ch_x "The two of you, feeling each other up like animals!"
    elif Line == "dildo_pussy" or Line == "dildo_anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Line == "eat_pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Line == "blowjob":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"

    if Girl.Shame >= 40:
        ch_x "[Girl.name], my dear, you're practically naked! At least throw a towel on!"
        "He throws [Girl.name] the towel."
        show blackscreen onlayer black
        $ BO = all_Girls[:]
        while BO:
            if BO[0].location == bg_current and (not BO[0].top and not BO[0].bra):
                $ BO[0].top = "towel"
            $ BO.remove(BO[0])
        hide blackscreen onlayer black
        if (Girl == StormX or Partner == StormX) and StormX.top == "towel":
            ch_x ". . ."
            ch_x "Ororo, for Christ's sake. . ."
            ch_x "Put on some actual clothes!"
            show blackscreen onlayer black
            $ StormX.top = "white_shirt"
            $ StormX.legs = "skirt"
            hide blackscreen onlayer black
            ch_x ". . . fine."

    elif Girl.Shame >= 20:
        ch_x "[Girl.name], my dear, that attire is positively scandalous."

    if Girl.event_counter["caught"]:

        "And this isn't even the first time this has happened!"

    if Partner:
        $ Partner.change_face("surprised",2)
        if Partner in Rules:
            if Partner == KittyX:
                "Xavier glances over at [KittyX.name], who just waggles her phone. . ."
            elif Partner == LauraX:
                $ Laura_Arms = 2
                "Xavier glances over at [LauraX.name], who raises her fist and shakes it. . ."
                $ Laura_Arms = 1
            ch_x "And. . .hm, I could have sworn there was someone else. . ."
        else:
            ch_x "And [Partner.name], you were just watching this occur!"
        $ Partner.change_face("bemused",1, Eyes="side")

    if EmmaX.location == bg_current and EmmaX not in Rules:
        if not EmmaX.event_counter["caught"]:
            ch_x "Emma, you are entrusted as a teacher here, I can't have you fraternizing with the students."
            ch_x "This is especially true in the school's public spaces!"
            ch_x "What sort of message does that send?"
            ch_x "How appropriate would it be if I were to just wander the halls with Miss Grey on my lap?"
            call XavierFace ("hypno")
            ch_x "Just. . . running my hands along her firm little body without a care in the world. . ."
            call XavierFace ("happy")
            if JeanX.location == bg_current:
                "You glance over at [JeanX.name], she shrugs."
            ch_x ". . ."
            call XavierFace ("shocked")
            ch_x "Yes, well, as I was saying! . ."
        else:
            ch_x "Emma, I don't believe this is the first time we've had this talk."
            ch_x "I should hope it will be the last."
    if StormX.location == bg_current and StormX not in Rules:
        if not StormX.event_counter["caught"]:
            if EmmaX.location == bg_current and EmmaX not in Rules:
                ch_x "And Ororo! You also know better than to be fraternizing with the students!"
            else:
                ch_x "Ororo, you are entrusted as a teacher here, I can't have you fraternizing with the students."
            ch_x "I'm well aware of your Bohemian tendencies in private, but you must comport yourself while in public."
            ch_x "What sort of message does that send?"
            ch_x "Do you think it would be appropriate for me to engage in such escapades?"
            call XavierFace ("hypno")
            ch_x "Just. . . rolling down the halls with my balls flowing freely in the wind. . ."
            call XavierFace ("happy")
            ch_x ". . ."
            call XavierFace ("shocked")
            ch_x "Do not distract me! . ."
        else:
            if EmmaX.location == bg_current and EmmaX not in Rules:
                ch_x "And Ororo! We've also been over this before."
            else:
                ch_x "Ororo, I don't believe this is the first time we've had this talk."
            ch_x "I should hope it will be the last."

    $ Line = 0
    menu:
        ch_x "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
            if RogueX.location == bg_current and RogueX.event_counter["caught"] < 3:
                $ RogueX.change_stat("love", 70, 20)
                $ RogueX.change_stat("inhibition", 50, -15)
                $ RogueX.change_stat("love", 90, 5)
            if KittyX.location == bg_current and KittyX.event_counter["caught"] < 3:
                $ KittyX.change_stat("love", 70, 10)
                $ KittyX.change_stat("inhibition", 30, -25)
                $ KittyX.change_stat("inhibition", 50, -10)
            if EmmaX.location == bg_current and EmmaX.event_counter["caught"] < 3:
                $ EmmaX.change_stat("love", 70, 5)
                $ EmmaX.change_stat("inhibition", 30, -15)
            if LauraX.location == bg_current and LauraX.event_counter["caught"] < 3:
                $ LauraX.change_stat("inhibition", 30, -20)
                $ LauraX.change_stat("inhibition", 50, -10)
            if JeanX.location == bg_current and JeanX.event_counter["caught"] < 3:
                $ JeanX.change_stat("obedience", 30, -20)
                $ JeanX.change_stat("obedience", 50, -10)
            if StormX.location == bg_current and StormX.event_counter["caught"] < 3:
                $ StormX.change_stat("love", 70, 5)
                $ StormX.change_stat("inhibition", 30, -5)
            if JubesX.location == bg_current and JubesX.event_counter["caught"] < 3:
                $ JubesX.change_stat("love", 70, 10)
                $ JubesX.change_stat("obedience", 70, 5)
                $ JubesX.change_stat("inhibition", 30, -10)
                $ JubesX.change_stat("inhibition", 50, -5)
            $ Girl.change_stat("obedience", 50, -5)

            call XavierFace ("happy")
            if Girl.event_counter["caught"]:
                ch_x "But you know you've done this before. . . at least [Girl.event_counter['caught']] times. . ."
            elif Girl == EmmaX and TotalCaught:
                ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ."
                $ Girl.change_face("sexy",Brows="confused")
            elif Girl == StormX and TotalCaught:
                ch_x "Not with Ms. Munroe, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ."
                $ Girl.change_face("sexy",Brows="confused")
            elif TotalCaught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ."
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
        "Just having a little fun, right [Girl.petname]?":


            $ Girl.nameCheck()
            $ Girl.change_face("bemused")
            $ Girl.change_stat("lust", 90, 5)
            if RogueX.location == bg_current and RogueX.event_counter["caught"] < 5:
                $ RogueX.change_stat("love", 70, 20)
                $ RogueX.change_stat("love", 90, 10)
            if KittyX.location == bg_current and KittyX.event_counter["caught"] < 5:
                $ KittyX.change_stat("inhibition", 90, 10)
                $ KittyX.change_stat("love", 90, 10)
            if EmmaX.location == bg_current and EmmaX.event_counter["caught"] < 5:
                $ EmmaX.change_stat("inhibition", 90, 10)
                $ EmmaX.change_stat("love", 90, 10)
            if LauraX.location == bg_current and LauraX.event_counter["caught"] < 5:
                $ LauraX.change_stat("inhibition", 90, 10)
                $ LauraX.change_stat("obedience", 90, 5)
                $ LauraX.change_stat("love", 90, 5)
            if JeanX.location == bg_current and JeanX.event_counter["caught"] < 5:
                $ JeanX.change_stat("inhibition", 200, 10)
                $ JeanX.change_stat("obedience", 50, 5)
                $ JeanX.change_stat("obedience", 90, 5)
                $ JeanX.change_stat("love", 90, 5)
            if StormX.location == bg_current and StormX.event_counter["caught"] < 5:
                $ StormX.change_stat("inhibition", 90, 15)
                $ StormX.change_stat("obedience", 50, 5)
                $ StormX.change_stat("love", 90, 5)
            if JubesX.location == bg_current and JubesX.event_counter["caught"] < 5:
                $ JubesX.change_stat("inhibition", 90, 5)
                $ JubesX.change_stat("obedience", 80, 5)
                $ JubesX.change_stat("love", 90, 10)

            call XavierFace ("angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."

            if RogueX.location == bg_current and RogueX.event_counter["caught"] < 3:
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("obedience", 90, 20)
                $ RogueX.change_stat("inhibition", 30, -20)
                $ RogueX.change_stat("inhibition", 50, -10)
            if KittyX.location == bg_current and KittyX.event_counter["caught"] < 3:
                $ KittyX.change_stat("obedience", 50, 20)
                $ KittyX.change_stat("obedience", 90, 20)
                $ KittyX.change_stat("inhibition", 30, -20)
            if EmmaX.location == bg_current and EmmaX.event_counter["caught"] < 3:
                $ EmmaX.change_stat("obedience", 50, 20)
                $ EmmaX.change_stat("obedience", 90, 20)
                $ EmmaX.change_stat("inhibition", 30, -20)
            if LauraX.location == bg_current and LauraX.event_counter["caught"] < 3:
                $ LauraX.change_stat("obedience", 50, 20)
                $ LauraX.change_stat("obedience", 90, 20)
                $ LauraX.change_stat("inhibition", 30, -20)
            if JeanX.location == bg_current and JeanX.event_counter["caught"] < 3:
                $ JeanX.change_stat("obedience", 50, 20)
                $ JeanX.change_stat("obedience", 90, 20)
            if StormX.location == bg_current and StormX.event_counter["caught"] < 3:
                $ StormX.change_stat("obedience", 50, 20)
                $ StormX.change_stat("inhibition", 30, -10)
            if JubesX.location == bg_current and JubesX.event_counter["caught"] < 3:
                $ JubesX.change_stat("obedience", 70, 10)
                $ JubesX.change_stat("inhibition", 30, -10)

            ch_x "I've had enough of you, begone."


        "Just this. . . Plan Omega, [RogueX.name]." if Girl == RogueX and Player.Lvl >= 5:
            $ Line = "Omega"
        "Just this. . . Plan Kappa, [KittyX.name]!" if Girl == KittyX and Player.Lvl >= 5:
            $ Line = "Kappa"
        "Just this. . . Plan Psi, [EmmaX.name]!" if Girl == EmmaX and Player.Lvl >= 5:
            $ Line = "Psi"
        "Just this. . . Plan Chi, [LauraX.name]!" if Girl == LauraX and Player.Lvl >= 5:
            $ Line = "Chi"
        "Just this. . . Plan Alpha, [JeanX.name]!" if Girl == JeanX and Player.Lvl >= 5:
            $ Line = "Alpha"
        "Just this. . . Plan Rho, [StormX.name]!" if Girl == StormX and Player.Lvl >= 5:
            $ Line = "Rho"
        "Just this. . . Plan Zeta, [JubesX.name]!" if Girl == JubesX and Player.Lvl >= 5:
            $ Line = "Zeta"
        "You can suck it, old man.":



            $ Girl.change_face("surprised")
            $ Girl.change_stat("lust", 90, 10)
            if RogueX.location == bg_current and RogueX.event_counter["caught"] < 3:
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("obedience", 90, 40)
            if KittyX.location == bg_current and KittyX.event_counter["caught"] < 3:
                $ KittyX.change_stat("obedience", 50, 25)
                $ KittyX.change_stat("obedience", 90, 40)
            if EmmaX.location == bg_current and EmmaX.event_counter["caught"] < 3:
                $ EmmaX.change_stat("love", 90, 5)
                $ EmmaX.change_stat("obedience", 50, 20)
                $ EmmaX.change_stat("obedience", 90, 30)
            if LauraX.location == bg_current and LauraX.event_counter["caught"] < 3:
                $ LauraX.change_stat("love", 90, 5)
                $ LauraX.change_stat("obedience", 50, 25)
                $ LauraX.change_stat("obedience", 90, 30)
            if JeanX.location == bg_current and JeanX.event_counter["caught"] < 3:
                $ JeanX.change_stat("love", 50, 5)
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("obedience", 50, 25)
                $ JeanX.change_stat("obedience", 90, 30)
            if StormX.location == bg_current and StormX.event_counter["caught"] < 3:
                $ StormX.change_stat("love", 90, -5)
                $ StormX.change_stat("obedience", 50, 20)
                $ StormX.change_stat("obedience", 90, 30)
            if JubesX.location == bg_current and JubesX.event_counter["caught"] < 3:
                $ JubesX.change_stat("love", 80, 10)
                $ JubesX.change_stat("obedience", 50, 25)
                $ JubesX.change_stat("obedience", 90, 30)

            call XavierFace ("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!"

            if RogueX.location == bg_current and RogueX.event_counter["caught"] < 3:
                if RogueX.inhibition > 500:
                    $ RogueX.change_stat("inhibition", 90, 15)
                $ RogueX.change_stat("inhibition", 30, -20)
                $ RogueX.change_stat("inhibition", 50, -10)
            if KittyX.location == bg_current and KittyX.event_counter["caught"] < 3:
                if KittyX.inhibition > 500:
                    $ KittyX.change_stat("inhibition", 90, 15)
                $ KittyX.change_stat("inhibition", 30, -20)
                $ KittyX.change_stat("inhibition", 50, -10)
            if EmmaX.location == bg_current and EmmaX.event_counter["caught"] < 3:
                if EmmaX.inhibition > 500:
                    $ EmmaX.change_stat("inhibition", 90, 15)
                $ EmmaX.change_stat("inhibition", 30, -20)
                $ EmmaX.change_stat("inhibition", 50, -10)
            if LauraX.location == bg_current and LauraX.event_counter["caught"] < 3:
                if LauraX.inhibition > 500:
                    $ LauraX.change_stat("inhibition", 90, 15)
                $ LauraX.change_stat("inhibition", 30, -15)
                $ LauraX.change_stat("inhibition", 50, -10)
            if JeanX.location == bg_current and JeanX.event_counter["caught"] < 3:
                $ JeanX.change_stat("inhibition", 90, 15)
            if StormX.location == bg_current and StormX.event_counter["caught"] < 3:
                if StormX.inhibition > 500:
                    $ StormX.change_stat("inhibition", 90, 5)
                $ StormX.change_stat("inhibition", 30, -10)
                $ StormX.change_stat("inhibition", 50, -5)
            if JubesX.location == bg_current and JubesX.event_counter["caught"] < 3:
                if JubesX.inhibition > 500:
                    $ JubesX.change_stat("inhibition", 90, 15)
                $ JubesX.change_stat("inhibition", 30, -15)
                $ JubesX.change_stat("inhibition", 50, -10)

            ch_x "Now get out of my sight."


    if Line:
        if Line == "Omega":
            if ApprovalCheck(RogueX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (RogueX)
                return
            elif ApprovalCheck(RogueX, 1000, TabM=1, Loc="No"):
                $ Girl.change_face("perplexed",Brows = "sad")
                ch_r "I'm not comfortable with something that extreme, [RogueX.player_petname]. . ."
                menu:
                    "Dammit [RogueX.name]. . .":
                        $ Girl.change_face("angry")
                        $ RogueX.change_stat("obedience", 50, 5)
                        $ RogueX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("bemused")
            else:
                $ Girl.change_face("confused")
                ch_r "What nonsense are you talking now?"
                ch_p "Plan {i}Omega!{/i} . . you know. . ."
                ch_r "Sounds like gibberish."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("bemused")

        elif Line == "Kappa":
            if "Xavier's photo" in Player.Inventory and ApprovalCheck(KittyX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (KittyX)
                return
            elif ApprovalCheck(KittyX, 1000, TabM=1, Loc="No"):
                $ Girl.change_face("perplexed",Brows = "sad")
                if "Xavier's photo" in Player.Inventory:
                    ch_k "You know. . . I really don't think that's a good idea. . ."
                elif "kappa" in Player.history:
                    ch_k "Maybe if we came back later we could find something. . ."
                else:
                    ch_k "We don't really have any way to pull that off atm. . ."
                    $ Player.history.append("kappa")
                menu:
                    "Dammit [KittyX.name]. . .":
                        $ Girl.change_face("angry")
                        $ KittyX.change_stat("obedience", 50, 5)
                        $ KittyX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("bemused")
                        $ KittyX.change_stat("love", 90, 5)
            else:
                $ Girl.change_face("confused")
                ch_k "Wait, Plan what??"
                ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                ch_k "I have no {i}idea{/i} what you're talking about."
                ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("bemused")

        elif Line == "Psi":
            if ApprovalCheck(EmmaX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (EmmaX)
                return
            elif ApprovalCheck(EmmaX, 1000, TabM=1, Loc="No"):
                $ Girl.change_face("perplexed",Brows = "sad")
                ch_e "Um, I don't believe we're quite at that point yet, [EmmaX.player_petname]. . ."
                menu:
                    "Dammit [EmmaX.name]. . .":
                        $ Girl.change_face("angry")
                        $ EmmaX.change_stat("obedience", 50, 5)
                        $ EmmaX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("bemused")
            else:
                $ Girl.change_face("confused")
                ch_e "Lord child, what are you talking about now?"
                ch_p "Plan {i}Psi!{/i} . . you know. . ."
                ch_e "I wish that I did."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("bemused")

        elif Line == "Chi":
            if LauraX.Lvl >= 2 and ApprovalCheck(LauraX, 1500, TabM=1, Loc="No") and ApprovalCheck(LauraX, 750, "I"):
                call Xavier_Plan (LauraX)
                return
            elif ApprovalCheck(LauraX, 1000, TabM=1, Loc="No"):
                $ Girl.change_face("angry",Eyes="side",Brows = "angry")
                ch_l "I told you that was a stupid idea. . ."
                menu:
                    "Dammit [LauraX.name]. . .":
                        $ Girl.change_face("angry")
                        $ LauraX.change_stat("obedience", 50, 5)
                        $ LauraX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("bemused")
                        $ LauraX.change_stat("love", 90, 5)
            else:
                $ Girl.change_face("confused")
                ch_l "Yeah!"
                ch_l ". . ."
                ch_l "Wait, plan \"key,\" what??"
                ch_p "Plan {i}Chi!{/i} . . you know. . ."
                ch_l "Um. No?"
                ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("bemused")

        elif Line == "Alpha":
            if ApprovalCheck(JeanX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (JeanX)
                return
            elif ApprovalCheck(JeanX, 1000, TabM=1, Loc="No"):
                $ Girl.change_face("perplexed",Brows = "sad")
                ch_j "Look, this is your mess, I'm not going to clean it up, [JeanX.player_petname]. . ."
                menu:
                    "Dammit [JeanX.name]. . .":
                        $ Girl.change_face("angry")
                        $ JeanX.change_stat("obedience", 50, 5)
                        $ JeanX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("bemused")
            else:
                $ Girl.change_face("confused")
                ch_j "Huh? What are you talking about?"
                ch_p "Plan {i}Alpha!{/i} . . you know. . ."
                ch_j "Drawing a blank here. . ."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("bemused")

        elif Line == "Rho":
            if "Xavier's files" in Player.Inventory and ApprovalCheck(StormX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (StormX)
                return
            elif ApprovalCheck(StormX, 1000, TabM=1, Loc="No"):
                $ Girl.change_face("perplexed",Brows = "sad")
                if "Xavier's files" in Player.Inventory:
                    ch_s "I really doubt that we should attempt that. . ."
                elif "rho" in Player.history:
                    ch_s "Perhaps if we had some leverage on the situation. . ."
                else:
                    ch_s "I'm not sure what you think we could do here. . ."
                    $ Player.history.append("rho")
                menu:
                    "Dammit [StormX.name]. . .":
                        $ Girl.change_face("angry")
                        $ StormX.change_stat("obedience", 50, 5)
                        $ StormX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("bemused")
            else:
                $ Girl.change_face("confused")
                ch_s "'Ro? You were speaking to me?"
                ch_p "Yes! Plan {i}Rho!{/i} . . you know. . ."
                ch_s "Yes, this is 'Ro. What plan?"
                ch_p "What's on second! I don't know!"
                $ Girl.change_face("smile")
                ch_s "Ah! \"Third base!\""
                $ Girl.change_face("bemused")

        elif Line == "Zeta":
            if ApprovalCheck(JubesX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (JubesX)
                return
            elif ApprovalCheck(JubesX, 1000, TabM=1, Loc="No"):
                $ Girl.change_face("perplexed",Brows = "sad")
                ch_v "What?! Um, no, let's not."
                menu:
                    "Dammit [JubesX.name]. . .":
                        $ Girl.change_face("angry")
                        $ JubesX.change_stat("obedience", 50, 5)
                        $ JubesX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("bemused")
            else:
                $ Girl.change_face("confused")
                ch_v "Huh?"
                ch_p "Plan {i}Zeta!{/i} . . you know. . ."
                ch_v "Is this a \"Gundam\" thing?"
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("bemused")



        call XavierFace ("angry")
        $ Count += 10
        ch_x "I have no idea what that was about, but it sounds like you haven't learned."
        if PunishmentX:
            ch_x "I'm extending your punishment by [Count] days."
        else:
            ch_x "I'm halving your daily stipend for [Count] days."

            if RogueX.location == bg_current and RogueX.event_counter["caught"] < 3:
                $ RogueX.change_stat("obedience", 50, 10)
                $ RogueX.change_stat("obedience", 90, 10)
                $ RogueX.change_stat("inhibition", 30, -10)
                $ RogueX.change_stat("inhibition", 50, -5)
            if KittyX.location == bg_current and KittyX.event_counter["caught"] < 3:
                $ KittyX.change_stat("obedience", 50, 10)
                $ KittyX.change_stat("obedience", 90, 10)
                $ KittyX.change_stat("inhibition", 30, -10)
                $ KittyX.change_stat("inhibition", 50, -5)
            if EmmaX.location == bg_current and EmmaX.event_counter["caught"] < 3:
                $ EmmaX.change_stat("obedience", 50, 10)
                $ EmmaX.change_stat("inhibition", 50, -5)
            if LauraX.location == bg_current and LauraX.event_counter["caught"] < 3:
                $ LauraX.change_stat("obedience", 50, 10)
                $ LauraX.change_stat("obedience", 90, 10)
                $ LauraX.change_stat("inhibition", 30, -10)
                $ LauraX.change_stat("inhibition", 50, -5)
            if JeanX.location == bg_current and JeanX.event_counter["caught"] < 3:
                $ JeanX.change_stat("obedience", 50, -10)
            if StormX.location == bg_current and StormX.event_counter["caught"] < 3:
                $ StormX.change_stat("obedience", 50, 10)
                $ StormX.change_stat("inhibition", 50, -5)
            if JubesX.location == bg_current and JubesX.event_counter["caught"] < 3:
                $ JubesX.change_stat("obedience", 50, 5)
                $ JubesX.change_stat("obedience", 90, 5)
                $ JubesX.change_stat("inhibition", 30, -8)
                $ JubesX.change_stat("inhibition", 50, -2)
        ch_x "I've had enough of you, begone."


    $ PunishmentX += Count

    $ Girl.event_counter["caught"] += 1
    if Partner in all_Girls:
        $ Partner.event_counter["caught"] += 1
    $ Girl.AddWord(0,"caught","caught")

    if Girl == KittyX and KittyX not in Rules and "Xavier's photo" not in Player.Inventory:
        "It would probably be a good idea to find some way to get Xavier to leave you alone."
        if KittyX.event_counter["caught"] > 1:
            "Maybe I should try searching the office when he's not around."
        if KittyX.event_counter["caught"] > 2:
            "I bet [KittyX.name] could help me get in."
        if KittyX.event_counter["caught"] > 3:
            "I bet there's something in that lefthand drawer. . ."
    elif Girl == JeanX and "nowhammy" not in JeanX.Traits and JeanX.event_counter["caught"] > 1:
        ch_x "Oh, and Jean, dear, I'd like a word?"
        $ Girl.change_face("bemused")
        ch_j "What is it?"
        ch_x "I understand that you've been using your abilities to. . ."
        ch_x "cover up for some of your. . . transgressions."
        $ Girl.change_face("bemused",Eyes="up")
        ch_j "Oh, you mean how I mindwipe the \"NPCs\" that get too nosy?"
        call XavierFace ("angry")
        ch_x "If by \"NPCs\" you mean your fellow students. . ."
        ch_x ". . . and by \"get too nosy,\" you mean \"notice you having sex in public\". . ."
        ch_x ". . . then yes, that is exactly what I mean."
        $ Girl.change_face("bemused",Eyes="side")
        ch_j "Ok, yeah."
        ch_x "I would like you to cease this activity at once!"
        ch_x "It is a total abuse of your abilities and of those students' autonomy!"
        $ Girl.change_face("angry",1)
        ch_j "Who cares."
        call XavierFace ("shocked")
        ch_x "!!!"
        ch_x "I do!"
        call XavierFace ("angry")
        ch_x "That is it, young lady. Until further notice, you're forbidden from. . . whammying your fellow students!"
        $ Girl.change_face("angry",1,Mouth="surprised")
        ch_j "Bullshit!"
        $ Girl.change_face("angry",0,Eyes="psychic")
        ch_x "Ugh. . ."
        call XavierFace ("psychic")
        ch_x "[Player.name]. . . this may take a while. . ."
        ch_x "You may as well leave. . ."
        $ JeanX.Traits.append("nowhammy")
        $ Girl.change_face("normal")

    if EmmaX.location == bg_current and EmmaX not in Rules:
        ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
        if EmmaX.event_counter["caught"]:
            $ EmmaX.change_stat("love", 90, -5)
            $ Girl.change_face("angry",Eyes="closed")
            ch_e "Not again. . ."
    if StormX.location == bg_current and StormX not in Rules:
        if EmmaX.location == bg_current and EmmaX not in Rules:
            ch_x "And Ororo, I'm afraid we will have to have words as well. . ."
        else:
            ch_x "Ororo, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
        if StormX.event_counter["caught"]:
            $ StormX.change_stat("love", 90, -5)
            $ Girl.change_face("angry",Eyes="closed")
            ch_s "Again? . ."
        if StormX not in Rules and "Xavier's files" not in Player.Inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            if StormX.event_counter["caught"] > 1:
                "Maybe I should try searching the office when he's not around."
            if StormX.event_counter["caught"] > 2:
                "I bet [StormX.name] could help me get in."
            if StormX.event_counter["caught"] > 3:
                "I bet there's something in that righthand drawer. . ."

    call Remove_Girl ("All")
    "You return to your room"
    hide Professor
    $ bg_current = "bg_player"
    jump Misplaced



label Xavier_Plan(GirlX=0):
    if "Xavier" in Player.daily_history:
        "The Professor seems pretty out of it."
        "You don't think you'll be able to get anything more out of him today."
        "You leave him to it."
        $ bg_current = "bg_player"
        jump Misplaced


    call shift_focus (GirlX)
    $ GirlX.change_face("sly")
    "As you say this, a sly grin crosses [GirlX.name]'s face."
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace ("psychic")
    ch_x ". . ."
    call XavierFace ("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."

    if Partner:
        if Partner == RogueX and "Omega" not in Player.Traits:
            $ Line = "first"
        elif Partner == KittyX and "Kappa" not in Player.Traits:
            $ Line = "first"
        elif Partner == EmmaX and "Psi" not in Player.Traits:
            $ Line = "first"
        elif Partner == LauraX and "Chi" not in Player.Traits:
            $ Line = "first"
        elif Partner == JeanX and "Alpha" not in Player.Traits:
            $ Line = "first"
        elif Partner == StormX and "Rho" not in Player.Traits:
            $ Line = "first"
        elif Partner == JubesX and "Zeta" not in Player.Traits:
            $ Line = "first"

        if Line == "first":

            if ApprovalCheck(Partner, 1000) or Partner == JeanX:

                $ Partner.change_face("surprised")
                "[Partner.name] looks a bit caught off guard, but goes along with the idea."
                $ Partner.change_face("sly")
            else:
                $ Partner.change_face("surprised")
                "[Partner.name] looks a bit uncomfortable with what's happening and takes off."
                call Remove_Girl (Partner)
        else:

            $ Partner.change_face("sly")
            "[Partner.name] understands what's going on here."


    call XavierFace ("angry")
    if GirlX == RogueX:
        $ RogueX.arms = 0
        $ RogueX.ArmPose = 2
        show Rogue_Sprite zorder 24 at sprite_location(stage_left+100,85) with ease
        "[RogueX.name] moves in and also grabs his head, duplicating his powers as he watches helplessly."
        "Now that she posesses his full power, while his are negated, he has no defenses."
        call XavierFace ("hypno")
        if "Omega" in Player.Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
            $ RogueX.change_stat("obedience", 80, 3)
            $ RogueX.change_stat("inhibition", 70, 1)
        else:
            $ RogueX.change_stat("obedience", 50, 40)
            $ RogueX.change_stat("inhibition", 70, 20)
        ch_r "Well, [RogueX.player_petname], what would you like to do with this opportunity?"
        ch_r "I think we'll only get three tries at this. . ."
    elif GirlX == KittyX:
        $ KittyX.ArmPose = 2
        show Kitty_Sprite at sprite_location(stage_left+100,150) with ease
        $ KittyX.sprite_location = stage_center
        "[KittyX.name] moves in sits on his lap, pinning his arms to the chair."
        if "Kappa" in Player.Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
            $ KittyX.change_stat("obedience", 80, 3)
            $ KittyX.change_stat("inhibition", 70, 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            "You pull out the photo you found earlier in his study."
            $ KittyX.change_stat("obedience", 50, 40)
            $ KittyX.change_stat("inhibition", 70, 30)
            ch_p "I have here a rather. . . compromising photo of you and Mystique."
            ch_p "I was thinking maybe you could cut me a little slack around here."
            ch_x "And if I do not?"
            ch_p "[KittyX.name] here's set it to distribute to every computer in school, every day."
            ch_p "And only I know the password."
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ."
            $ KittyX.change_stat("obedience", 200, 30)
            $ KittyX.change_stat("inhibition", 200, 10)
        ch_k "Well, [KittyX.player_petname], what should we ask for?"
    elif GirlX == EmmaX or GirlX == JeanX:
        if GirlX == EmmaX:
            show Emma_Sprite zorder 24 at sprite_location(stage_left+100,85) with ease
        elif GirlX == JeanX:
            show Jean_Sprite zorder 24 at sprite_location(stage_left+100,85) with ease
        "[GirlX.name] moves behind Xavier and activates her own telepathy."
        call XavierFace ("angry")
        if (GirlX == EmmaX and "Psi" in Player.Traits) or (GirlX == JeanX and "Alpha" in Player.Traits):
            ch_x "Oh, not again. . ."
            $ GirlX.change_stat("obedience", 80, 3)
            $ GirlX.change_stat("inhibition", 80, 1)
        else:
            $ GirlX.change_stat("obedience", 50, 40)
            $ GirlX.change_stat("inhibition", 70, 30)
            $ GirlX.change_stat("obedience", 200, 30)
            $ GirlX.change_stat("inhibition", 200, 10)
        GirlX.voice "Well, [GirlX.player_petname], what should we ask for?"
    elif GirlX == LauraX:
        $ LauraX.ArmPose = 2
        if "Chi" in Player.Traits:
            ch_x "Oh, not again."
            $ LauraX.Claws = 1
            ch_x "What is it you want this time?"
            $ LauraX.change_stat("obedience", 80, 3)
            $ LauraX.change_stat("inhibition", 80, 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            ch_p "[LauraX.name] and I were talking, and it seems like neither of us appreciates you bothering us."
            ch_x "And if I continue?"
            ch_p "My little [LauraX.petname] here has a very particular set of skills, you know. . ."
            $ GirlX.nameCheck()
            $ LauraX.Claws = 1
            $ GirlX.change_face("sly")
            ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
            "[LauraX.name] draws her claws along the arm of the Professor's chair, tracing fine lines into the metal."
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ."
            $ LauraX.change_stat("obedience", 50, 40)
            $ LauraX.change_stat("inhibition", 80, 30)
            $ LauraX.change_stat("obedience", 200, 30)
            $ LauraX.change_stat("inhibition", 200, 10)
        ch_l "Well, [LauraX.player_petname], what should we ask for?"
    elif GirlX == StormX:
        $ StormX.ArmPose = 1
        show Storm_Sprite at sprite_location(stage_left+100,150) with ease
        $ StormX.sprite_location = stage_center
        "[StormX.name] moves in sits on his lap, pinning his arms to the chair."
        if "Rho" in Player.Traits:
            ch_x "Oh, not this again."
            ch_x "What is it you want this time?"
            $ StormX.change_stat("obedience", 80, 3)
            $ StormX.change_stat("inhibition", 70, 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            "You pull out the files you found earlier in his study."
            $ StormX.change_stat("obedience", 50, 40)
            $ StormX.change_stat("inhibition", 70, 30)
            ch_p "I have here some rather. . . questionable \"medical\" files."
            ch_p "I was thinking maybe you could cut me a little slack around here."
            ch_x "And if I do not?"
            ch_p "We've made sure that -all- the girls in these files will find out."
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ."
            $ StormX.change_stat("obedience", 200, 30)
            $ StormX.change_stat("inhibition", 200, 10)
        ch_s "Well, [StormX.player_petname], what should we ask for?"
    elif GirlX == JubesX:
        $ JubesX.ArmPose = 2
        show Jubes_Sprite at sprite_location(stage_left+100,150) with ease
        $ JubesX.sprite_location = stage_center
        "[JubesX.name] moves in and sits on his lap, pinning his arms to the chair."
        "She turns to look at him."
        if "Zeta" in Player.Traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"
            $ JubesX.change_stat("obedience", 80, 3)
            $ JubesX.change_stat("inhibition", 70, 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            $ JubesX.change_stat("inhibition", 70, 30)
            ch_v "Look into my eyes. . ."
            $ JubesX.change_stat("obedience", 50, 40)
            $ JubesX.change_stat("inhibition", 200, 10)
            ch_v "see the sparks dancing around them? . . ."
            $ JubesX.change_stat("obedience", 200, 30)
            "She slowly mesmerizes him into a trance, using a combination of her vampiric abilties and fireworks. . ."
        ch_v "Well, [JubesX.player_petname], what should we ask for?"

    $ Count = 3
    $ PunishmentX = 0
    while Count > 0:
        $ Count -= 1
        menu:
            ch_x "What do you want?"
            "Don't bother us anymore when we're having fun." if GirlX not in Rules:
                ch_x "Very well. . . I could offer you some. . . discretion. . ."
                $ Rules.append(GirlX)
            "You know, it's kinda fun dodging you, catch us if you can." if GirlX in Rules:
                ch_x "If you. . . want me to, I suppose. . ."
                $ Rules.remove(GirlX)

            "You know, [JeanX.name] should be able to \"whammy\" people again." if JeanX in all_Girls and "nowhammy" in JeanX.Traits:
                ch_x "I could remove her mind-wiping ban. . ."
                $ JeanX.Traits.remove("nowhammy")
                $ JeanX.Traits.append("whammy")
                if JeanX.location == bg_current:
                    $ JeanX.change_stat("obedience", 50, 5)
                    $ JeanX.change_stat("love", 50, 5)
                    $ JeanX.change_stat("love", 70, 5)
                    $ JeanX.change_stat("love", 90, 5)
                    $ GirlX.change_face("sly",1)
                    ch_j "Nice. . ."
            "You know, I did like it when [JeanX.name] couldn't use her \"whammy.\"" if JeanX in all_Girls and "whammy" in JeanX.Traits:
                ch_x "I could reinstate her mind-wiping ban. . ."
                $ JeanX.Traits.append("nowhammy")
                $ JeanX.Traits.remove("whammy")
                if JeanX.location == bg_current:
                    $ JeanX.change_stat("obedience", 50, 5)
                    $ JeanX.change_stat("obedience", 80, 5)
                    $ JeanX.change_stat("love", 70, -5)
                    $ JeanX.change_stat("love", 90, -5)
                    $ GirlX.change_face("angry",1,Mouth="surprised")
                    ch_j "Hey!"
                    $ GirlX.change_face("angry",1)

            "Raise my stipend." if Player.Income < 30:
                if GirlX == RogueX and "Omega" not in Player.Traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.Income += 2
                elif GirlX == KittyX and "Kappa" not in Player.Traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.Income += 2
                elif GirlX == EmmaX and "Psi" not in Player.Traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.Income += 2
                elif GirlX == LauraX and "Chi" not in Player.Traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.Income += 2
                elif GirlX == JeanX and "Alpha" not in Player.Traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.Income += 2
                elif GirlX == StormX and "Rho" not in Player.Traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.Income += 2
                elif GirlX == JubesX and "Zeta" not in Player.Traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.Income += 2
                else:
                    ch_x "I'm afraid I can't manage any more than I have. . ."
                    $ Count += 1
            "Raise my stipend. [[Used](locked)" if Player.Income >= 30:
                pass
            "There's this girl that's been bothering me. . .":

                "This will send a girl away, temporarily removing her from the game."
                "You can always ask to bring her back later."
                $ Line = 0
                menu:
                    ch_p "Could you get rid of. . ."
                    "[RogueX.name]" if RogueX in active_Girls:
                        $ Line = RogueX
                    "[KittyX.name]" if KittyX in active_Girls and "met" in KittyX.history:
                        $ Line = KittyX
                    "[EmmaX.name]" if EmmaX in active_Girls and "met" in EmmaX.history:
                        $ Line = EmmaX
                    "[LauraX.name]" if LauraX in active_Girls and "met" in LauraX.history and "dress0" not in LauraX.history:
                        $ Line = LauraX
                    "[JeanX.name]" if JeanX in active_Girls and "met" in JeanX.history:
                        $ Line = JeanX
                    "[StormX.name]" if StormX in active_Girls and "met" in StormX.history:
                        $ Line = StormX
                    "[JubesX.name]" if JubesX in active_Girls and "met" in JubesX.history:
                        $ Line = JubesX
                    "Never mind. . .":
                        $ Count += 1
                if Line:

                    ch_x "Very well, I suppose I can keep her occupied with various tasks around the campus. . ."
                    ch_x "She should be out of your hair for the time being."
                    if Line.location == bg_current:

                        $ Line.change_stat("love", 90, -10)
                        $ Line.change_stat("obedience", 50, 3)
                        if Line == RogueX:
                            ch_r "What do you mean, I'm \"bothering\" you?"
                        elif Line == KittyX:
                            ch_k "Hey, what gives?!"
                        elif Line == EmmaX:
                            ch_e "Excuse me? I must not have heard that right."
                        elif Line == LauraX:
                            ch_l "Explain."
                        elif Line == JeanX:
                            ch_j "Are you kidding me?!"
                        elif Line == StormX:
                            ch_s "I do not understand this."
                        elif Line == JubesX:
                            ch_v "Seriously?!"
                        menu:
                            extend ""
                            "Oh, sorry, never mind.":
                                $ Line = 0
                                if ApprovalCheck(Line, 2000):

                                    $ Line.change_face("confused")
                                    $ Line.change_stat("love", 90, 3)
                                    $ Line.change_stat("obedience", 50, 2)
                                    if Line == RogueX:
                                        ch_r "Right. . ."
                                    elif Line == KittyX:
                                        ch_k "Uh-huh?"
                                    elif Line == EmmaX:
                                        ch_e ". . . right. . ."
                                    elif Line == LauraX:
                                        ch_l "If you say so."
                                    elif Line == JeanX:
                                        ch_j "We will have words. . ."
                                    elif Line == StormX:
                                        ch_s "I will remember this. . ."
                                    elif Line == JubesX:
                                        ch_v "Riiight."
                                else:

                                    $ Line.change_face("angry")
                                    $ Line.change_stat("obedience", 50, -2)
                                    $ Line.change_stat("inhibition", 60, 3)
                                    if Line == RogueX:
                                        ch_r "Damned right you are."
                                    elif Line == KittyX:
                                        ch_k "Yeah, right."
                                    elif Line == EmmaX:
                                        ch_e "I don't know what you were thinking."
                                    elif Line == LauraX:
                                        ch_l "Uh. . . huh."
                                    elif Line == JeanX:
                                        ch_j "We will have words. . ."
                                    elif Line == StormX:
                                        ch_s "I will remember this. . ."
                                    elif Line == JubesX:
                                        ch_v "We will have words."
                            "Sorry, but I just need some \"me\" time.":
                                $ active_Girls.remove(Line)
                                $ Line.change_stat("obedience", 50, 5)
                                $ Line.change_stat("obedience", 90, 2)
                                $ Line.change_stat("inhibition", 60, 2)
                                if ApprovalCheck(Line, 900, "L") or ApprovalCheck(Line, 2000):

                                    $ Line.change_face("sadside")
                                    if Line == RogueX:
                                        ch_r "I suppose if you do, I can give you some space."
                                    elif Line == KittyX:
                                        ch_k "I guess we both could. . ."
                                    elif Line == EmmaX:
                                        ch_e "I wouldn't want to be a bother. . ."
                                    elif Line == LauraX:
                                        ch_l "I can make myself scarce. . ."
                                    elif Line == JeanX:
                                        ch_j "Well, I guess I could find someone else to occupy my time with. . ."
                                    elif Line == StormX:
                                        ch_s ". . . fine, I can understand that. . ."
                                    elif Line == JubesX:
                                        ch_v "Ok, whatever, I have things to do."
                                else:

                                    $ Line.change_stat("love", 90, -5)
                                    $ Line.change_face("angry")
                                    $ Line.AddWord(1,"angry","angry")
                                    if Line == RogueX:
                                        ch_r "Oh, I think you'll be getting it."
                                    elif Line == KittyX:
                                        ch_k "Yeah, \"me\" too, I guess!"
                                    elif Line == EmmaX:
                                        ch_e "I do have other things with which to occupy myself."
                                    elif Line == LauraX:
                                        ch_l "I'm busy too."
                                    elif Line == StormX:
                                        ch_s "Oh, you shall get it. . ."
                                    elif Line == JubesX:
                                        ch_v "We will have words."
                            "You heard me.":
                                $ active_Girls.remove(Line)
                                $ Line.change_stat("love", 80, -5)
                                $ Line.change_stat("love", 90, -5)
                                $ Line.change_stat("obedience", 80, 5)
                                if ApprovalCheck(Line, 850, "O") or ApprovalCheck(Line, 1500, "LO"):

                                    $ Line.change_face("sadside")
                                    $ Line.change_stat("obedience", 200, 10)
                                else:

                                    $ Line.change_face("angry")
                                    $ Line.change_stat("love", 90, -5)
                                    $ Line.change_stat("inhibition", 60, 5)
                                    $ Line.AddWord(1,"angry","angry")
                                if Line == RogueX:
                                    ch_r "Loud and clear."
                                elif Line == KittyX:
                                    ch_k ". . ."
                                elif Line == EmmaX:
                                    ch_e "I suppose I did."
                                elif Line == LauraX:
                                    ch_l "If you say so."
                                elif Line == JeanX:
                                    ch_j "Noted. . ."
                                elif Line == StormX:
                                    ch_s "Like thunder. . ."
                                elif Line == JubesX:
                                    ch_v "We will have words."
                    else:


                        $ active_Girls.remove(Line)
                if Line == GirlX:
                    GirlX.voice "Did you forget that I'm your escape plan?"
                    menu:
                        "Oh. . .":
                            ch_x "I'll forget you asked."
                            $ Count = 0
                $ Line = 0


            "I wanted to bring a girl back in. . ." if len(all_Girls) > len (active_Girls):
                "This will bring the girl back into active play."
                "You can always ask to send her away again later."
                $ Line = 0
                menu:
                    ch_p "Could you bring back. . ."
                    "[RogueX.name]" if RogueX not in active_Girls and RogueX in TotalGirl:
                        $ Line = RogueX
                    "[KittyX.name]" if KittyX not in active_Girls and KittyX in all_Girls and "met" in KittyX.history:
                        $ Line = KittyX
                    "[EmmaX.name]" if EmmaX not in active_Girls and EmmaX in all_Girls and "met" in EmmaX.history:
                        $ Line = EmmaX
                    "[LauraX.name]" if LauraX not in active_Girls and LauraX in all_Girls and "met" in LauraX.history and "dress0" not in LauraX.history:

                        $ Line = LauraX
                    "[JeanX.name]" if JeanX not in active_Girls and JeanX in all_Girls and "met" in JeanX.history:
                        $ Line = JeanX
                    "[StormX.name]" if StormX not in active_Girls and StormX in all_Girls and "met" in StormX.history:
                        $ Line = StormX
                    "[JubesX.name]" if JubesX not in active_Girls and JubesX in all_Girls and "met" in JubesX.history:
                        $ Line = JubesX
                    "Never mind. . .":
                        $ Count += 1
                if Line:

                    ch_x "Certainly. I've kept her busy, but I can let her off the hook. . ."
                    ch_x "She should have more free time now. . ."
                    $ active_Girls.append(Line)
                $ Line = 0
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:
                        ch_x "Fine, take it. . ."
                        $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:
                        pass

                    "Give me the key to [GirlX.name]'s room." if GirlX not in Keys:
                        ch_x "I. . . suppose I could do that. . ."
                        $ Keys.append(GirlX)
                    "Give me the key to [GirlX.name]'s room.[[Owned] (locked)" if GirlX in Keys:
                        pass
                    "Never mind the keys.":

                        $ Count += 1
            "That should do it.":
                $ Count = 0

    ch_x "Very well, that should conclude our business. Please leave."
    if GirlX == RogueX:
        if "Omega" not in Player.Traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("love", 70, 30)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.Traits.append("Omega")
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
        $ GirlX.arms = "gloves"
        $ GirlX.ArmPose = 1
    elif GirlX == KittyX:
        if "Kappa" not in Player.Traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.Traits.append("Kappa")
        $ GirlX.ArmPose = 0
    elif GirlX == EmmaX:
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
        if "Psi" not in Player.Traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.Traits.append("Psi")
    elif GirlX == LauraX:
        if "Chi" not in Player.Traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.Traits.append("Chi")
        $ GirlX.ArmPose = 1
        $ GirlX.Claws = 0
    elif GirlX == JeanX:
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
        if "Alpha" not in Player.Traits:
            $ GirlX.change_stat("lust", 70, 20)
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("obedience", 70, 10)
            $ GirlX.change_stat("obedience", 200, 20)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.Traits.append("Alpha")
    elif GirlX == StormX:
        if "Rho" not in Player.Traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.Traits.append("Rho")
    elif GirlX == JubesX:
        if "Zeta" not in Player.Traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.Traits.append("Zeta")
        $ GirlX.ArmPose = 0

    $ Player.daily_history.append("Xavier")
    call Remove_Girl ("All")
    hide Professor
    $ bg_current = "bg_player"
    call set_the_scene
    "You return to your room"
    jump Misplaced







label Girl_Caught_Changing(Girl=0):
    if Girl not in all_Girls:
        return
    call shift_focus (Girl)
    $ D20 = renpy.random.randint(1, 20)

    $ Girl.change_face("surprised", 1,Mouth="kiss")
    call Remove_Girl ("All")

    if D20 > 17:

        $ Girl.change_outfit("nude")
    else:

        $ Girl.change_outfit(6)
        if D20 >15:

            $ Girl.legs = 0
            $ Girl.hose = 0
            $ Girl.underwear = 0
        elif D20 >14:

            $ Girl.bra = 0
            $ Girl.top = 0
        elif D20 >10:

            $ Girl.top = 0
            $ Girl.legs = 0
        elif D20 >5:

            $ Girl.top = 0

    $ Girl.location = bg_current
    call set_the_scene (Dress=0)
    if D20 > 17:

        "As you enter the room, you see [Girl.name] is naked, and seems to be getting dressed."
    elif D20 >14:

        "As you enter the room, you see [Girl.name] is practically naked, and seems to be getting dressed."
    elif D20 >10:

        "As you enter the room, you see [Girl.name] is in her underwear, and seems to be getting dressed."
    elif D20 >5:

        "As you enter the room, you see [Girl.name] has her top off, and seems to be getting dressed."
    else:

        "As you enter the room, you see [Girl.name] has just pulled her top on, and seems to have been getting dressed."

    if Girl == StormX:
        ch_s "Oh, hello, [Girl.player_petname]."
    elif ApprovalCheck(Girl, 1400):
        if Girl == RogueX:
            ch_r "Oh, hey."
        elif Girl == KittyX:
            ch_k "Hey, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "Oh, here for the view?"
        elif Girl == LauraX:
            ch_l "Hey."
        elif Girl == JeanX:
            ch_j "Oh, [Girl.player_petname]?"
        elif Girl == JubesX:
            ch_v "Yo."
    else:
        if D20 > 5:
            if not ApprovalCheck(Girl, (D20 *70)) and (not Girl.SeenPussy or not Girl.SeenChest):

                $ Girl.change_face("surprised",Brows="angry")
                $ Girl.change_stat("love", 80, -50)

                if not Girl.OverNum() or (Girl.OverNum()+Girl.ChestNum() <5) or (Girl.PantsNum() < 5 and Girl.HoseNum() < 10):


                    call expression Girl.Tag + "_First_Bottomless" pass (1)
                    call expression Girl.Tag + "_First_Topless" pass (1)
                    $ Girl.top = "towel"
                    "She grabs a towel and covers up."
            else:

                $ Girl.change_face("surprised", 1,Brows = "confused")
                if "exhibitionist" in Girl.Traits:
                    $ Girl.change_stat("lust", 200, (2*D20))
                else:
                    $ Girl.change_stat("lust", 200, D20)
                if D20 > 17:
                    call expression Girl.Tag + "_First_Bottomless"
                    call expression Girl.Tag + "_First_Topless" pass (1)
                elif D20 > 15:
                    call expression Girl.Tag + "_First_Bottomless"
                elif D20 > 14:
                    call expression Girl.Tag + "_First_Topless"
            $ Girl.change_stat("inhibition", 70, 20)


            if Girl == RogueX:
                ch_r "Hey! Learn to knock maybe?!"
            elif Girl == KittyX:
                ch_k "Why didn't you knock?!"
            elif Girl == EmmaX:
                ch_e "Did you consider knocking?"
            elif Girl == LauraX:
                ch_l "Didn't think about knocking?"
            elif Girl == JeanX:
                ch_j "Forget to knock, [JeanX.player_petname]?"
            elif Girl == JubesX:
                ch_v "Hey, knock maybe?"
            menu:
                extend ""
                "Sorry, I should have knocked.":
                    $ Girl.change_stat("love", 50, 2)
                    $ Girl.change_stat("love", 80, 4)
                "And miss the view?":
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
        else:


            if not ApprovalCheck(Girl, 800) and (not Girl.SeenPussy or not Girl.SeenChest):
                $ Girl.change_face("angry",Brows="confused")
                $ Girl.change_stat("love", 80, -5)
            else:
                $ Girl.change_face("sexy",Brows="confused")
            $ Girl.change_stat("inhibition", 50, 3)

            if Girl == RogueX:
                ch_r "Well hello there, [Girl.player_petname]. Hoping to see something more?"
            elif Girl == KittyX:
                ch_k "Hey, [Girl.player_petname]. . . {i}you{/i} were hoping I'd be naaaked."
            elif Girl == EmmaX:
                ch_e "Were you hoping to catch me in a compromising position?."
            elif Girl == LauraX:
                ch_l "Hey, [Girl.player_petname]. Trying to catch a peek?"
            elif Girl == JeanX:
                ch_j "Oh, [Girl.player_petname]. Hoping to catch me dressing again?"
            elif Girl == JubesX:
                ch_v "Hey, [Girl.player_petname]. Hoping to catch me naked again?"

            menu:
                extend ""
                "Sorry, I should have knocked.":
                    $ Girl.change_stat("love", 50, 2)
                    $ Girl.change_stat("love", 80, 2)
                "Well, to be honest. . .":
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
        $ Girl.change_face("sexy")
        if ApprovalCheck(Girl, 1000):

            if Girl == RogueX:
                ch_r "You could have just asked, [RogueX.player_petname]."
            elif Girl == KittyX:
                ch_k "I didn't say that I {i}minded{/i}. . ."
            elif Girl == EmmaX:
                ch_e "That does show initiative. . ."
            elif Girl == LauraX:
                ch_l "I don't mind."
            elif Girl == JeanX:
                ch_j "Well, give the audience what it wants. . ."
            elif Girl == JubesX:
                ch_v "You just have to ask. . ."

            $ Girl.Uptop = 1
            $ Girl.Upskirt = 1
            pause 1
            call expression Girl.Tag + "_First_Topless" pass (1)
            call expression Girl.Tag + "_First_Bottomless" pass (1)
            $ Girl.Uptop = 0
            $ Girl.Upskirt = 0
            "She flashes you real quick."
        else:

            if Girl == RogueX:
                ch_r "Well, it happens, just be careful next time."
            elif Girl == KittyX:
                ch_k "Yeah. . . we wouldn't want any accidents. . ."
            elif Girl == EmmaX:
                ch_e "Hmm, show a bit more care next time. . ."
            elif Girl == LauraX:
                ch_l "Uh-huh . . ."
            elif Girl == JeanX:
                ch_j "Sure, perv."
            elif Girl == JubesX:
                ch_v "Don't be sneaking around."

    if Girl == RogueX:
        ch_r "Well, are you planning to stick around?"
    elif Girl == KittyX:
        ch_k "So were you planning on staying?"
    elif Girl == EmmaX:
        ch_e "Did you have business with me?"
    elif Girl == LauraX:
        ch_l "So did you plan to stay?"
    elif Girl == JeanX:
        ch_j "So, what did you want?"
    elif Girl == StormX:
        ch_s "Was there something I could help you with?"
    elif Girl == JubesX:
        ch_v "Did you want something?"
    menu:
        extend ""
        "Sure, for a bit.":
            pass
        "Actually, I should get going. . .":

            $ Girl.change_outfit(6,Changed=0)
            $ renpy.pop_call()
            call Worldmap

    if Girl == StormX and D20 >5:

        ch_s "Ok, then let me finish getting dressed. . ."
        menu:
            "Ok.":
                "She finishes getting changed."
                $ Girl.change_outfit(6,Changed=0)
            "Actually, you could leave them off.":
                if ApprovalCheck(Girl, 350+(10*D20)):
                    $ Girl.change_stat("love", 70, 3)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_face("sexy")
                    ch_s "I suppose that could not hurt. . ."
                    $ Girl.Set_Temp_Outfit()
                else:
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_face("smile")
                    ch_s "Ha! I would not want to be too much of a distraction."
                    $ Girl.change_outfit(6,Changed=0)
            "Why not lose the rest too?":
                $ Girl.change_face("sexy")
                if ApprovalCheck(Girl, 700):
                    $ Girl.change_stat("love", 50, 1)
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_s "Oh, you are a naughty one. . ."
                    $ Girl.change_outfit("nude")
                    $ Girl.Set_Temp_Outfit()
                elif ApprovalCheck(Girl, 350+(10*D20)):
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 70, 2)
                    ch_s "I could at least. . . pause for a moment?"
                    $ Girl.Set_Temp_Outfit()
                else:
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_s "You are joking, [Girl.player_petname]."
                    $ Girl.change_outfit(6,Changed=0)
            "Don't, stay like that.":
                $ Girl.change_stat("obedience", 80, 2)
                if ApprovalCheck(Girl,1100):
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
                    $ Girl.change_face("sexy")
                    ch_s "If you want. . ."
                    $ Girl.Set_Temp_Outfit()
                elif ApprovalCheck(Girl, 350+(10*D20)) and ApprovalCheck(Girl, 400, "O"):
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("love", 80, -1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_face("sexy",Eyes="side")
                    ch_s ". . . Very well."
                    $ Girl.Set_Temp_Outfit()
                else:
                    $ Girl.change_stat("love", 80, -2)
                    $ Girl.change_stat("obedience", 50, -1)
                    $ Girl.change_face("angry")
                    ch_s "You do not decide that, [Girl.player_petname]."
                    $ Girl.change_outfit(6,Changed=0)
            "Lose the rest of it.":
                $ Girl.change_stat("obedience", 80, 2)
                if ApprovalCheck(Girl,1300):
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
                    $ Girl.change_face("sexy")
                    ch_s "Fine. . ."
                    $ Girl.change_outfit("nude")
                    $ Girl.Set_Temp_Outfit()
                elif ApprovalCheck(Girl,800) and ApprovalCheck(Girl, 500, "O"):
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("love", 80, -2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_face("sexy",Eyes="side")
                    ch_s ". . . Fine."
                    $ Girl.change_outfit("nude")
                    $ Girl.Set_Temp_Outfit()
                else:
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("love", 80, -2)
                    $ Girl.change_stat("obedience", 50, -2)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_face("angry")
                    ch_s "I do not think that I will, [Girl.player_petname]."
                    $ Girl.change_outfit(6,Changed=0)
    return



label Girl_Caught_Mastubating(Girl=0):

    if Girl not in all_Girls:
        return
    $ Girl.DrainWord("gonnafap")
    call Remove_Girl ("All")
    $ Girl.location = bg_current
    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
    menu:
        extend ""
        "Knock politely":
            $ Line = "knock"
        "Peek inside":
            call set_the_scene
            $ Girl.change_face("kiss",1,Eyes = "closed")
            $ primary_action = "masturbation"
            $ girl_offhand_action = "fondle_pussy"
            "You see [Girl.name], eyes closed and stroking herself vigorously."
            menu:
                extend ""
                "Enter Quietly":
                    $ Line = "enter"
                "Pull back and knock":
                    $ Line = "knock"
                "Leave quietly":
                    $ Line = "leave"
        "Enter quietly":
            $ Line = "enter"
            "You hear some odd noises coming from [Girl.name]'s room as you enter."
        "Leave quietly":
            $ Line = "leave"

    if Line == "leave":
        $ Girl.change_stat("lust", 80, 20)
        "You leave [Girl.name] to her business and slip out."
        $ renpy.pop_call()
        jump Campus_Map
    elif Line == "knock":
        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
        "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."
        $ Girl.change_face("confused",1,Eyes = "surprised",Mouth = "smile")
        $ primary_action = 0
        $ girl_offhand_action = 0
        call set_the_scene
        if Girl == RogueX:
            ch_r "Sorry about that [RogueX.player_petname], I was. . . working out."
        elif Girl == KittyX:
            ch_k "Oh, hey, [KittyX.player_petname], I was. . . never mind."
        elif Girl == EmmaX:
            ch_e "Well, I suppose you could tell I was a bit. . . occupied."
        elif Girl == LauraX:
            ch_l "Um, hey [LauraX.player_petname], just working off some stress."
        elif Girl == JeanX:
            ch_j "Oh, [JeanX.player_petname]. I was. . . never mind."
        elif Girl == StormX:
            ch_s "Oh, um, [StormX.player_petname]. I was just. . . stretching."
        elif Girl == JubesX:
            ch_v "Oh, hey, [Girl.player_petname]. . . I was. . ."
        $ approval_bonus += 10
    elif Line == "enter":
        call shift_focus (Girl)
        show blackscreen onlayer black
        $ Girl.Upskirt = 1
        $ Girl.underwearDown = 1
        $ Girl.location = bg_current

        call set_the_scene
        $ Girl.change_face("sexy")
        $ Girl.eyes = "closed"
        $ Girl.ArmPose = 2
        $ Count = 0
        $ primary_action = "masturbation"
        hide blackscreen onlayer black
        $ Girl.daily_history.append("unseen")
        $ Girl.recent_history.append("unseen")
        call expression Girl.Tag + "_SexAct" pass ("masturbate")
        if "angry" in Girl.recent_history:
            return


        $ Girl.change_face("sexy",Brows="confused")
        if Girl.action_counter["masturbation"] == 1:
            if Girl == RogueX:
                ch_r "Well that was a bit unexpected. . ."
                $ Girl.change_face("bemused",Eyes="side")
                ch_r "but not exactly unpleasant. . ."
                $ Girl.change_face("sexy")
                ch_r "Maybe next time I'll give you a heads up first."
            elif Girl == KittyX:
                ch_k "So[KittyX.like]I wasn't expecting company. . ."
                $ Girl.change_face("bemused",Eyes="side")
                ch_k "but I didn't exactly mind it either. . ."
                $ Girl.change_face("sexy")
                ch_k "Maybe knock next time?"
            elif Girl == EmmaX:
                ch_e "I wasn't expecting visitors. . ."
                $ Girl.change_face("bemused",Eyes="side")
                ch_e "although for you I could make an exception. . ."
                $ Girl.change_face("sexy")
                ch_e "Perhaps next time you could knock?"
            elif Girl == LauraX:
                ch_l "So what are you doing here? . ."
                $ Girl.change_face("bemused",Eyes="side")
                ch_l "not that I mind the company. . ."
                $ Girl.change_face("sexy")
                ch_l "But you know, give me a heads up first."
            elif Girl == JeanX:
                $ Girl.change_face("bemused",Eyes="side")
                ch_j "Well that was fun. . ."
                $ Girl.change_face("sexy")
                ch_j "So what brings you here? . ."
            elif Girl == StormX:
                ch_s "That was an interesting experience. . ."
                $ Girl.change_face("bemused",Eyes="side")
                ch_s "I certainly didn't mnd the attention. . ."
                $ Girl.change_face("sexy")
                ch_s "You might want to knock in future though."
            elif Girl == JubesX:
                ch_v "I don't usually get unexpected visitors . ."
                $ Girl.change_face("bemused",Eyes="side")
                ch_v "but I didn't mind the company. . ."
                $ Girl.change_face("sexy")
                ch_v "Maybe knock next time?"
        else:
            if Girl == RogueX:
                ch_r "Fancy seeing you here again, [Girl.player_petname]. Almost like it was intentional. . ."
            elif Girl == KittyX:
                ch_k "You seem to be making a habit of dropping in."
            elif Girl == EmmaX:
                ch_e "I notice you make a habit of dropping in."
            elif Girl == LauraX:
                ch_l "You're around a lot. . ."
            elif Girl == JeanX:
                ch_j "You have a habit of dropping by. . ."
            elif Girl == StormX:
                ch_s "You come up here fairly often. . ."
            elif Girl == JubesX:
                ch_v "You stop by alot. . ."

        $ Girl.ArmPose = 1
        $ Girl.change_outfit(Changed=0)

    return





label Call_For_Les(Girl=0, Girl2=0, BO=[]):


    if Girl not in active_Girls:
        $ BO = active_Girls[:]
        while BO and Girl not in active_Girls:
            if BO[0] not in Party and BO[0].location != bg_current and "les" in BO[0].recent_history:


                $ Girl = BO[0]
                $ BO = [1]
            $ BO.remove(BO[0])
    if Girl in active_Girls and not Girl2:

        $ BO = active_Girls[:]
        $ BO.remove(Girl)
        while BO:
            if BO[0] not in Party and BO[0].location != bg_current and "les" in BO[0].recent_history:


                if ApprovalCheck(BO[0], 1600 - BO[0].SEXP, TabM=0):
                    $ Girl2 = BO[0]
                    $ BO = [1]
                else:
                    return 0
            $ BO.remove(BO[0])
    if Girl not in active_Girls or Girl2 not in active_Girls:

        return 0

    show Cellphone at sprite_location(stage_left)

    $ Line = 0
    "You get a call from [Girl.name]."
    if Girl == RogueX:
        ch_r "Hey, [Player.name]. . . I was just over here with [Girl2.name] and. . ."
        ch_r "One thing lead to another, you know how that goes. . . and we were just wondering,"
        ch_r "Would you like to come over and join us?"
    elif Girl == KittyX:
        ch_k "Oh, hi, [Girl.player_petname]. . . I was just hanging out with [Girl2.name] and. . ."
        ch_k "we got to thinking[Girl.like]"
        ch_k "Did you wanna come over and join us?"
    elif Girl == EmmaX:
        ch_e "[Girl.player_petname]. . . I was just here entertaining [Girl2.name]. . ."
        ch_e "One thing lead to another, I'm sure you get the picture. . . and we were just wondering,"
        ch_e "Would you like to come lend us a hand?"
        ch_e "Or other bits. . ."
    elif Girl == LauraX:
        ch_l "Hey, [Player.name]. . . I was with [Girl2.name] here, and. . ."
        ch_l "You know, feeling each other up-"
        Girl2.voice "Hey!{w=0.3}{nw}"
        ch_l ". . . so . . ."
        ch_l "Want in on this action?"
    elif Girl == JeanX:
        ch_j "Oh, [Girl.player_petname]. . . I was hanging out with [Girl2.name]. . ."
        ch_j "Did you want to swing by and pound some sense into her?"
        Girl2.voice "Hey!{w=0.3}{nw}"
        ch_j ". . ."
    elif Girl == StormX:
        ch_s "Hello, [Girl.player_petname]? . . I was having a. . . chat with [Girl2.name]. . ."
        ch_s "We were having a good time, and were wondering if perhaps you wanted to join us?"
    elif Girl == JubesX:
        ch_v "Oh, hey, [Girl.player_petname]. . . [Girl2.name]'s over here and. . ."
        ch_v "we were having some fun, and. . ."
        ch_v "Did you want to join us?"
    while not Line and Line != "what":
        menu:
            extend ""
            "Sure, I'll be right there!":
                $ Girl.change_stat("love", 95, 5)
                $ Girl.change_stat("obedience", 95, 3)
                $ Girl.change_stat("inhibition", 95, 2)
                if Girl in (EmmaX,StormX):
                    ch_e "Lovely, see you in a bit."
                else:
                    Girl.voice "Cool. See you here."
                $ Girl2.change_stat("love", 95, 5)
                $ Girl2.change_stat("obedience", 95, 3)
                $ Girl2.change_stat("inhibition", 95, 2)
                $ Line = "yes"
            "Nah, have fun though.":
                $ Girl.change_stat("love", 90, -4)
                $ Girl.change_stat("obedience", 95, 2)
                $ Girl.change_stat("inhibition", 90, -2)
                if Girl == RogueX:
                    ch_r "Oh. Ok then. . ."
                elif Girl == KittyX:
                    ch_k "Wow, ok, I guess."
                elif Girl == EmmaX:
                    ch_e "I admire your restraint. . ."
                    $ Girl.change_stat("obedience", 95, 2)
                    ch_e "If not your wisdom. . ."
                elif Girl == LauraX:
                    ch_l "Huh. Ok."
                elif Girl == JeanX:
                    ch_j "Ok, just thought I'd ask."
                    ch_j "Later then."
                elif Girl == StormX:
                    ch_s "That is unfortunate. . ."
                elif Girl == JubesX:
                    ch_v "Ok, but you're missing out!"
                $ Girl2.change_stat("love", 90, -4)
                $ Girl2.change_stat("obedience", 95, 2)
                $ Girl2.change_stat("inhibition", 90, -2)
                $ Player.recent_history.append("no_les")
                "She hangs up."
                hide Cellphone
                jump Misplaced
            "What, are you watching a movie?" if Line != "what" and Girl != JeanX:
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 80, 2)
                if Girl == RogueX:
                    ch_r "Oh, we're putting on quite the show, but no."
                elif Girl == KittyX:
                    $ Girl.change_stat("inhibition", 80, 2)
                    ch_k "Um. . . no. . .we're, um. . ."
                elif Girl == EmmaX:
                    $ Girl.change_stat("love", 80, 1)
                    ch_e "Oh, that's adorable. No, of course not."
                elif Girl == LauraX:
                    ch_l "You hit your head or something?"
                elif Girl == StormX:
                    ch_s "A movie? . . no. Not a movie."
                elif Girl == JubesX:
                    ch_v "Heh, no! We aren't. . . it's more fun than that. . ."

                $ Girl2.change_stat("love", 80, 2)
                $ Girl2.change_stat("inhibition", 80, 2)
                if Girl2 == RogueX:
                    ch_r "We're bumpin uglies, [Girl2.player_petname]."
                    ch_r "Thought you might want in."
                elif Girl2 == KittyX:
                    $ Girl2.change_stat("inhibition", 80, 2)
                    ch_k "It's, um. . . sex."
                    ch_k "We're having sex."
                    ch_k "-thought you might wanna join us?"
                elif Girl2 == EmmaX:
                    ch_e "We're having -intercourse-, [Girl2.player_petname]."
                    ch_e "Did - you - want - to - join - us?"
                elif Girl2 == LauraX:
                    ch_l "Sex, dumbass."
                    ch_l "We're shucking clams over here and wanted someone to bring the meat."
                    ch_l "You packing, or what?"
                elif Girl2 == StormX:
                    ch_s "What she is trying to say is that we were enjoying each other's bodies."
                    ch_s "Sex, [Girl2.player_petname]. We wanted you to join us for sex."
                elif Girl2 == JubesX:
                    ch_v "I was eating her out, basically."
                    ch_v "Did you want in on this?"
                $ Line = "what"


    hide Cellphone

    if bg_current == Girl.home:

        $ Line = Girl
        $ Girl = Girl2
        $ Girl2 = Line
    $ Girl.location = Girl.home
    $ Girl2.location = Girl.home
    $ bg_current = Girl.home
    $ Taboo= 0
    $ Girl.Taboo = 0
    $ Girl2.Taboo = 0
    $ Line = 0

    $ Girl.DrainWord("les",1,0)
    $ Girl2.DrainWord("les",1,0)

    $ Girl.AddWord(0,"lesbian","lesbian")
    $ Girl2.AddWord(0,"lesbian","lesbian")
    $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)
    $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)

    call set_the_scene (0, 1, 0, 0)
    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
    while Line < 2:
        menu:
            extend ""
            "Knock politely":
                if Girl == RogueX:
                    ch_r "Come on in, [RogueX.player_petname]!"
                elif Girl == KittyX:
                    ch_k "Oh! Come in!"
                elif Girl == EmmaX:
                    ch_e "No need to wait on our account. . ."
                elif Girl == LauraX:
                    ch_l "Come in!"
                elif Girl == JeanX:
                    ch_j "Enter!"
                elif Girl == StormX:
                    ch_s "Come in!"
                elif Girl == JubesX:
                    ch_v "You may enter!"
                $ Line = 2
            "Peek inside" if Line != 1:
                call set_the_scene
                $ Girl.change_face("kiss",1,Eyes = "closed")
                $ Girl2.change_face("kiss",1,Eyes = "closed")
                $ primary_action = "lesbian"
                $ girl_offhand_action = "fondle_pussy"
                $ second_girl_primary_action = "fondle_pussy"
                "You see [Girl.name] and [Girl2.name], eyes closed and stroking each other vigorously."
                $ Line = 1
            "Enter quietly":
                $ Line = 2
            "Leave quietly":
                "You leave the girls to their business and slip out."
                $ Girl.Thirst -= 30
                $ Girl.lust = 20
                $ Girl2.Thirst -= 30
                $ Girl2lust = 20
                $ Girl.change_stat("love", 90, -3)
                $ Girl2.change_stat("love", 90, -3)
                $ renpy.pop_call()
                $ bg_current = "bg_campus"
                $ Line = 0
                jump Misplaced

    $ Line = 0
    $ Girl.change_face("sly",1)
    $ Girl2.change_face("sly",1)
    call set_the_scene (1, 0, 0, 0)
    if Girl == RogueX:
        ch_r "Sorry we got started without you."
    elif Girl == KittyX:
        ch_k "Oh, hey, [KittyX.player_petname], we. . . got a little bored."
    elif Girl == EmmaX:
        ch_e "We certainly didn't."
    elif Girl == LauraX:
        ch_l "So you waiting for another invitation?"
    elif Girl == JeanX:
        ch_j "So you getting in here?"
    elif Girl == StormX:
        ch_s "Well? Are you joining us?"
    elif Girl == JubesX:
        ch_v "Get over here."

    $ primary_action = "lesbian"
    $ girl_offhand_action = "fondle_pussy"
    $ second_girl_primary_action = "fondle_pussy"
    $ Partner = Girl2
    call expression Girl.Tag + "_SexAct" pass ("lesbian")
    jump Misplaced
    return






label Girls_Caught_Lesing(Girl=0, Girl2=0, BO=[]):


    $ BO = active_Girls[:]
    if Girl in all_Girls:
        $ BO.remove(Girl)
    while BO and not Girl:
        if BO[0] not in Party and BO[0].location == bg_current and "les" in BO[0].recent_history:


            $ Girl = BO[0]
            $ BO = [1]
        $ BO.remove(BO[0])
    if Girl and not Girl2:

        $ BO = active_Girls[:]
        $ BO.remove(Girl)
        while BO:
            if BO[0] not in Party and BO[0].location == bg_current and "les" in BO[0].recent_history:


                $ Girl2 = BO[0]
                $ BO = [1]
            $ BO.remove(BO[0])

    if not Girl or not Girl2:
        return 1

    $ Girl.DrainWord("les",1,0)
    $ Girl2.DrainWord("les",1,0)

    $ Girl.AddWord(0,"lesbian","lesbian")
    $ Girl2.AddWord(0,"lesbian","lesbian")
    $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)
    $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)

    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
    $ Line = 0
    while not Line:
        menu:
            extend ""
            "Knock politely":
                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."
                $ Girl.change_face("confused",2,Eyes = "surprised",Mouth = "smile")
                $ Girl2.change_face("confused",2,Eyes = "surprised",Mouth = "smile")
                $ primary_action = 0
                $ girl_offhand_action = 0
                $ second_girl_primary_action = 0
                $ second_girl_offhand_action = 0
                call set_the_scene
                if Girl == RogueX:
                    ch_r "Sorry about that [Girl.player_petname], we were, um. . . working out."
                elif Girl == KittyX:
                    ch_k "Oh, hey, [Girl.player_petname], hi, we were. . . never mind."
                elif Girl == EmmaX:
                    ch_e "Well, I hope you have a good reason for interrupting us."
                    ch_e "I was. . . teaching her a few things. . ."
                elif Girl == LauraX:
                    ch_l "Um, hey [Girl.player_petname], we were a bit busy."
                elif Girl == JeanX:
                    ch_j "Hey [Girl.player_petname], we were just giving [Girl2.name]'s tongue a workout."
                elif Girl == StormX:
                    ch_s "Ah, hello, [Girl.player_petname] . . I was having a. . . chat with [Girl2.name]. . ."
                elif Girl == JubesX:
                    ch_v "Oh, hey. . . me and [Girl2.name] were just. . . having some fun."
                $ Girl.change_face("smile",1)
                $ Girl2.change_face("smile",1)
                $ approval_bonus += 10
                $ Line = 1
            "Peek inside":
                call set_the_scene
                $ Girl.change_face("kiss",1,Eyes = "closed")
                $ Girl2.change_face("kiss",1,Eyes = "closed")
                $ primary_action = "lesbian"
                $ girl_offhand_action = "fondle_pussy"
                $ second_girl_primary_action = "fondle_pussy"
                "You see [Girl.name] and [Girl2.name], eyes closed and stroking each other vigorously."
            "Enter quietly":
                call set_the_scene (Quiet=1)
                $ Girl.change_face("kiss",1,Eyes = "closed")
                $ Girl2.change_face("kiss",1,Eyes = "closed")
                $ primary_action = "lesbian"
                $ girl_offhand_action = "fondle_pussy"
                $ second_girl_primary_action = "fondle_pussy"
                $ Girl.AddWord(1,"unseen","unseen")
                $ Girl2.AddWord(1,"unseen","unseen")
                $ Partner = Girl2
                $ Line = 0
                call expression Girl.Tag + "_SexAct" pass ("lesbian")
            "Leave quietly":
                "You leave the girls to their business and slip out."
                $ Girl.Thirst -= 30
                $ Girl.lust = 20
                $ Girl2.Thirst -= 30
                $ Girl2lust = 20
                $ renpy.pop_call()
                jump Campus_Map
    $ Line = 0
    return





label Girl_Caught_Shower(Girl=0):
    if Girl not in all_Girls:
        return
    call shift_focus (Girl)

    $ Options = []
    $ Girl.AddWord(1,"showered","showered",0,0)
    call Remove_Girl ("All")

    $ Girl.change_outfit("nude")
    $ Girl.change_face("smile",1)

    $ Girl.location = "bg_showerroom"
    $ Girl.Water = 1
    $ Girl.Wet = 2

    if "gonnafap" in Girl.daily_history:
        "As you approach the showers, you hear some shallow moans from inside."
    else:
        "As you approach the showers, you hear some humming noises from inside."
    menu:
        "What do you do?"
        "Enter":
            pass
        "Knock":
            $ Line = "knock"
        "Come back later":
            call Remove_Girl (Girl)
            $ Girl.change_outfit(6)
            $ Girl.DrainWord("gonnafap",0,1)
            $ Girl.lust = 25
            $ Girl.Thirst -= int(Girl.Thirst/2) if Girl.Thirst >= 50 else int(Girl.Thirst/4)
            $ bg_current = "bg_campus"
            jump Misplaced

    if Line == "knock":

        "You knock on the door. You hear some shuffling inside"
        $ Girl.top = "towel"
        if "gonnafap" in Girl.daily_history:

            "You hear a sharp shuffling sound and the water gets cut off."
            "After several seconds and some more shuffling, [Girl.name] comes to the door."
            $ Girl.change_face("perplexed",2,Mouth="normal")
            call set_the_scene (Dress=0)
            if Girl == RogueX:
                ch_r "Sorry about that [Girl.player_petname], I was. . . just wrapping up my shower."
            elif Girl == KittyX:
                ch_k "Oh, hey, [Girl.player_petname]. I was just. . . showering. Yeah."
            elif Girl == EmmaX:
                ch_e "Oh, hello [Girl.player_petname]. I was. . . taking care of some personal business."
            elif Girl == LauraX:
                ch_l "Oh, hey [Girl.player_petname]. I was just. . . working off some stress."
            elif Girl == JeanX:
                ch_j "Oh, [Girl.player_petname]. I was. . . never mind."
            elif Girl == StormX:
                ch_s "Ah, hello, [Girl.player_petname]. . . I was. . . cleaning myself."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.player_petname]. . . I was. . . what did you hear?"
            $ Girl.change_stat("lust", 90, 5)
            $ approval_bonus += 10
        else:

            "You hear the rustling of a towel and some knocking around, but after a few seconds [Girl.name] comes to the door."
            call set_the_scene (Dress=0)
            if Girl == RogueX:
                ch_r "Sorry about that [Girl.player_petname], I was just wrapping up my shower."
            elif Girl == KittyX:
                ch_k "Oh, hey, [Girl.player_petname]. I was just[KittyX.like]showering."
            elif Girl == EmmaX:
                ch_e "Oh, hello [Girl.player_petname]. I was just finishing my shower."
            elif Girl == LauraX:
                ch_l "Oh, hey [Girl.player_petname]. I was just finishing up."
            elif Girl == JeanX:
                ch_j "Oh, [Girl.player_petname]. I'm about done here."
            elif Girl == StormX:
                ch_s "Ah, hello, [Girl.player_petname] . . I am about finished here if you want some water. . ."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.player_petname]. I was wrapping up here. . ."
    else:


        if "gonnafap" in Girl.daily_history:

            $ Girl.DrainWord("gonnafap",0,1)
            $ Girl.change_face("sexy",Eyes="closed")
            $ Girl.AddWord(1,"unseen","unseen",0,0)
            call set_the_scene (Dress=0)
            $ Count = 0
            $ primary_action = "masturbation"
            $ girl_offhand_action = "fondle_pussy"
            "You see [Girl.name] under the shower, feeling herself up."
            call expression Girl.Tag + "_SexAct" pass ("masturbate")
            $ bg_current = "bg_showerroom"
            jump Misplaced

        elif D20 >= 15:

            call set_the_scene (Dress=0)
            $ Girl.change_face("surprised", 1)
            "As you enter the showers, you see [Girl.name] washing up."
            call expression Girl.Tag + "_First_Bottomless" pass (1)
            call expression Girl.Tag + "_First_Topless" pass (1)
            if not ApprovalCheck(Girl, 1200) or not Girl.SeenPussy or not Girl.SeenChest:
                $ Girl.brows="angry"
                $ Girl.top = "towel"
                "She grabs a towel and covers up."
                $ Girl.change_face("angry", 1)
                $ Girl.change_stat("love", 80, -5)
            else:
                if "exhibitionist" in Girl.Traits:
                    $ Girl.change_stat("lust", 90, (2*D20))
                else:
                    $ Girl.change_stat("lust", 80, D20)
                $ Girl.brows="confused"






            $ Girl.change_stat("inhibition", 70, 3)
            if Girl == RogueX:
                ch_r "Hey! Learn to knock maybe?!"
            elif Girl == KittyX:
                ch_k "Did you[KittyX.like]get a good look?"
            elif Girl == EmmaX:
                ch_e "Hello. Haven't you learned to knock before entering?"
            elif Girl == LauraX:
                ch_l "Um, hey? Don't knock much?"
            elif Girl == JeanX:
                ch_j "Forget to knock, [JeanX.player_petname]?"
            elif Girl == StormX:
                ch_s "Oh, hello, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Hey, knock maybe?"
            menu:
                extend ""
                "Sorry, I should have knocked.":
                    $ Girl.change_stat("love", 50, 2)
                    if Girl != StormX:
                        $ Girl.change_stat("love", 80, 4)
                "And miss the view?":
                    $ Girl.change_stat("obedience", 50, 2)
                    if Girl != StormX:
                        $ Girl.change_stat("obedience", 80, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                "Why, would it have made a difference?":
                    if not ApprovalCheck(Girl, 500,"I"):
                        $ Girl.change_stat("love", 50, -3)
                        $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("obedience", 80, 2)
                    $ EmmaX.change_stat("inhibition", 60, 2)
        else:



            $ Girl.top = "towel"
            call set_the_scene (Dress=0)
            "As you enter the showers, you see [Girl.name] putting on a towel."
            if not ApprovalCheck(Girl, 1100) and (not Girl.SeenPussy or not Girl.SeenChest):
                $ Girl.change_face("angry",Brows="confused")
                $ Girl.change_stat("love", 80, -5)
            else:
                $ Girl.change_face("sexy",Brows="confused")
            $ Girl.change_stat("inhibition", 50, 3)
            if Girl == RogueX:
                ch_r "Well hello there, [RogueX.player_petname]. Hoping to see something more?"
            elif Girl == KittyX:
                ch_k "Oh, hey. Were you hoping I'd be naaaaaked?"
            elif Girl == EmmaX:
                ch_e "Oh, hello, [EmmaX.player_petname]. Sorry you didn't get here sooner?"
            elif Girl == LauraX:
                ch_l "Oh, hey [LauraX.player_petname]. Trying to slip in unnoticed?"
            elif Girl == JeanX:
                ch_j "Oh, [JeanX.player_petname], just sneaking in?"
            elif Girl == StormX:
                ch_s "Oh, hello, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Well you're being sneaky. . ."
            menu:
                extend ""
                "Sorry, I should have knocked.":
                    $ Girl.change_stat("love", 50, 2)
                    if Girl != StormX:
                        $ Girl.change_stat("love", 80, 2)
                "Well, to be honest. . .":
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("obedience", 50, 2)
                    if Girl != StormX:
                        $ Girl.change_stat("obedience", 80, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                "I still like the view. . ." if Girl != EmmaX:
                    if ApprovalCheck(Girl, 500,"I"):
                        $ Girl.change_stat("love", 80, 1)
                    else:
                        $ Girl.change_stat("love", 50, -1)
                        $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 3)
                "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("obedience", 80, 2)
                    $ EmmaX.change_stat("inhibition", 60, 2)


        $ Girl.change_face("sexy")
        if Girl == StormX:
            ch_s "Oh, that's fine, [Girl.player_petname]."
            ch_s "You might want to be careful with the other girls though."
        elif not ApprovalCheck(Girl, 1000) or not Girl.SeenPussy or not Girl.SeenChest:
            if Girl == RogueX:
                ch_r "Well, it happens, just be careful next time."
            elif Girl == KittyX:
                ch_k "Well, it's not like I totally mind. . ."
            elif Girl == EmmaX:
                ch_e "Hmm. Yes, a likely excuse."
            elif Girl == LauraX:
                ch_l "Well, just keep an eye on your own bits."
                ch_l "Wouldn't want them going missing."
            elif Girl == JeanX:
                ch_j "Well, just. . . be more careful."
            elif Girl == JubesX:
                ch_v "Gimme some warning next time."
        elif not ApprovalCheck(Girl, 1300):
            if Girl == RogueX:
                ch_r "Well, it happens, just be careful next time."
            elif Girl == KittyX:
                ch_k "Well too bad."
            elif Girl == EmmaX:
                ch_e "Hmm. Yes, a likely excuse."
            elif Girl == LauraX:
                ch_l "Uh-huh."
            elif Girl == JeanX:
                ch_j "Sure. . ."
            elif Girl == JubesX:
                ch_v "Uh-huh. . ."
        else:
            if Girl == RogueX:
                ch_r "You could have just asked, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Well, it's not like it's totally off the table. . ."
            elif Girl == EmmaX:
                ch_e "Well, it's not that I mind. . ."
            elif Girl == LauraX:
                ch_l "Nah, I don't mind much. . ."
            elif Girl == JeanX:
                ch_j "How could I resist an audience?"
            elif Girl == JubesX:
                ch_v "Gimme some warning next time."
            elif Girl == JubesX:
                ch_v "You just have to ask. . ."

            if Girl.top == "towel":

                $ Girl.top = 0
                pause 0.5
                $ Girl.top = "towel"
                "She flashes you real quick."
                $ Girl.top = "towel"
                call expression Girl.Tag + "_First_Bottomless" pass (1)
                call expression Girl.Tag + "_First_Topless" pass (1)

                if Girl == LauraX:
                    ch_l "Heh!"



    if Girl == RogueX:
        ch_r "Well, I should probably get going. . ."
    elif Girl == KittyX:
        ch_k "I'm done here, see you later?"
    elif Girl == EmmaX:
        ch_e "I should probably be leaving. . ."
    elif Girl == LauraX:
        ch_l "I should get going. . ."
    elif Girl == JeanX:
        ch_j "Ok, I'm headed out."
    elif Girl == StormX:
        ch_s "Ok, I am finished here, [Girl.player_petname]."
    elif Girl == JubesX:
        ch_v "Well, I'm done here. . ."
    menu:
        extend ""
        "Sure, see you later then.":
            call Remove_Girl (Girl)
        "Actually, could you stick around a minute?":
            if ApprovalCheck(Girl, 900) or Girl == StormX:
                if Girl == RogueX:
                    ch_r "Sure, what's up?"
                elif Girl == KittyX:
                    ch_k "Yeah?"
                elif Girl == EmmaX:
                    ch_e "Very well, what did you need?"
                elif Girl == LauraX:
                    $ LauraX.location = "bg_showerroom"
                    ch_l "Huh? Ok, what's up?"
                elif Girl == JeanX:
                    ch_j "What? Why?"
                elif Girl == StormX:
                    ch_s "I suppose so, what did you need?"
                elif Girl == JubesX:
                    ch_v "Oh? Why?"
            else:

                if Girl == RogueX:
                    ch_r "Um, actually, I'm not really comfortable being so. . . exposed?"
                    ch_r "I'll just see you around later."
                elif Girl == KittyX:
                    ch_k "I'm[KittyX.like]totally exposed here?"
                    ch_k "I'm just going to head out."
                elif Girl == EmmaX:
                    ch_e "I really shouldn't be \"hanging out\" in such a state."
                    ch_e "We can talk later."
                elif Girl == LauraX:
                    ch_l "I probably shouldn't hang out like this."
                    ch_l "We'll talk later."
                elif Girl == JeanX:
                    ch_j "I'd rather not."
                elif Girl == JubesX:
                    ch_v "Um. . . nah. . ."
                call Remove_Girl (Girl)

    if Line == "leaving":
        $ Girl.change_outfit(6)
    $ Line = 0
    return 0






label Pool_Sunbathe(Girl=0, Type=0, Mod=0):




    menu:
        "With who?"
        "[RogueX.name]" if bg_current == RogueX.location:
            $ Girl = RogueX
        "[KittyX.name]" if bg_current == KittyX.location:
            $ Girl = KittyX
        "[EmmaX.name]" if bg_current == EmmaX.location:
            $ Girl = EmmaX
        "[LauraX.name]" if bg_current == LauraX.location:
            $ Girl = LauraX
        "[JeanX.name]" if bg_current == JeanX.location:
            $ Girl = JeanX
        "[StormX.name]" if bg_current == StormX.location:
            $ Girl = StormX
        "[JubesX.name]" if bg_current == JubesX.location:
            $ Girl = JubesX
        "Never mind.":
            return

    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
        ch_p "Hey, [Girl.name], why don't you just relax over here?"
        ch_p "You don't want to get tanlines, why don't you. . ."
        ch_p ". . . take off a few layers?"
    else:
        ch_p "Are you sure you don't want to. . ."

    if time_index >= 2:
        $ Girl.change_face("confused")
        Girl.voice "A bit late in the day for that. . ."
        $ Girl.change_face("normal")
        return
    if not Girl.ClothingCheck():

        $ Girl.change_face("sly")
        Girl.voice "Little late for that."
        return
    if "no_tan" in Girl.recent_history:
        $ Girl.change_face("angry")
        Girl.voice "I just told you \"no.\""
        $ Girl.AddWord(1,"angry","angry")
        return
    elif "no_tan" in Girl.daily_history:
        $ Girl.change_face("angry")
        Girl.voice "Not today."
        $ Girl.AddWord(1,"angry","angry")
        return

    if Girl == EmmaX:
        if "classcaught" not in EmmaX.history:
            $ Girl.change_face("angry",2)
            ch_e "That would be entirely inappropriate."
            return
        if "taboo" not in EmmaX.history:
            $ Girl.change_face("bemused",2)
            ch_e "[EmmaX.player_petname], we can't be seen like that in public. . ."
            return
        if "three" not in EmmaX.history:
            if not AloneCheck(EmmaX):
                $ Girl.change_face("bemused",2)
                ch_e "Not with this sort of company. . ."
                return

    if not Girl.top and not Girl.bra and not Girl.legs and not Girl.underwear and (not Girl.accessory or Girl != JubesX):

        $ Girl.change_face("sly")
        if Girl == RogueX:
            ch_r "I don't think that'll be a problem, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "Beat you to it."
        elif Girl == EmmaX:
            ch_e "I plan ahead."
        elif Girl == LauraX:
            ch_l "Yup."
        elif Girl == JeanX:
            ch_j "Seems that's taken care of. . ."
        elif Girl == StormX:
            ch_s "I cannot get much more naked. . ."
        elif Girl == JubesX:
            ch_v "I'm already pretty naked here. . ."
        $ Girl.AddWord(1,"tan","tan")
        return

    $ Line = 0
    while True:

        if not Line:

            menu:
                extend ""
                "take it all off?" if (Girl.top or Girl.bra) and (Girl.legs or Girl.underwear or Girl.hose):
                    if Girl.top == "towel" and not Girl.legs and not Girl.hose and not Girl.underwear:
                        $ Type = "no_panties"
                    elif (Girl.legs or Girl.hose) and not Girl.underwear:
                        $ Type = "no_panties"
                    elif Girl.top and not Girl.bra:
                        $ Type = "no_bra"
                    else:
                        $ Type = "both"
                    $ Mod = 200

                "lose the top?" if Girl.bra and not Girl.top:
                    $ Type = "bra"

                "maybe just lose the jacket?" if Girl.accessory and Girl == JubesX:
                    if Girl.accessory == "shut_jacket" and not Girl.legs and not Girl.hose and not Girl.underwear:
                        $ Type = "no_panties"
                    elif Girl.accessory == "shut_jacket" and not Girl.top and not Girl.bra:
                        $ Type = "no_bra"
                    else:
                        $ Type = "jacket"

                "maybe just lose the [Girl.top]?" if Girl.top:
                    if Girl.top == "towel" and not Girl.legs and not Girl.hose and not Girl.underwear:
                        $ Type = "no_panties"
                    elif not Girl.bra:
                        $ Type = "no_bra"
                    else:
                        $ Type = "over"

                "maybe just lose the [Girl.legs]?" if Girl.legs:
                    if not Girl.underwear:
                        $ Type = "no_panties"
                    else:
                        $ Type = "legs"

                "maybe just lose the [Girl.hose]?" if Girl.hose and not Girl.legs:
                    if not Girl.underwear:
                        $ Type = "no_panties"
                    else:
                        $ Type = "legs"

                "maybe just lose the [Girl.underwear]?" if Girl.underwear:
                    $ Type = "panties"
                    $ Mod = 200
                "never mind.":

                    return


        if Type == "no_panties":
            $ Mod = 200
            $ Girl.change_face("bemused",1)
            Girl.voice "I don't have bottoms on under this. . ."
        elif Type == "no_bra":
            $ Girl.change_face("bemused",1)
            Girl.voice "I don't have a top on under this. . ."

        if (Girl.SeenPussy and Girl.SeenChest) and AloneCheck():
            $ Mod -= 100


        if "exhibitionist" in Girl.Traits:

            $ Line = "sure"
        elif ApprovalCheck(Girl, 700+Mod, "I"):

            $ Line = "sure"
        elif ApprovalCheck(Girl, 1400+Mod) or (Girl == StormX and StormX in Rules):

            $ Line = "sure"
        elif ApprovalCheck(Girl, 900):

            $ Line = "sorry"
        else:

            $ Line = "no"

        if Type == "no_bra" or Type == "no_panties":

            menu:
                extend ""
                "And?":
                    if Line == "sure":
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("inhibition", 70, 1)

                        $ Girl.change_face("sly",1)
                        if Girl == RogueX:
                            ch_r "Hmm, good point. . ."
                        elif Girl == KittyX:
                            ch_k "\"And\". . . I don't know. . ."
                        elif Girl == EmmaX:
                            ch_e "\"And\". . . you're lucky you're so cute. . ."
                        elif Girl == LauraX:
                            ch_l "I don't know. . ."
                        elif Girl == JeanX:
                            ch_j "Good point."
                        elif Girl == StormX:
                            ch_s "Just giving you fair warning. . ."
                        elif Girl == JubesX:
                            ch_v "Well. . . ok. . ."
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 70, -1)
                            $ Girl.change_stat("obedience", 80, 1)

                        $ Girl.change_face("angry",2)
                        if Girl == RogueX:
                            ch_r "\"And\" that's all you're getting. . . for now. . ."
                        elif Girl == KittyX:
                            ch_k "\"And\". . . AND!"
                        elif Girl == EmmaX:
                            ch_e "\"And\". . . you shouldn't push your luck. . ."
                        elif Girl == LauraX:
                            ch_l "\"And\" that's all you get."
                        elif Girl == JeanX:
                            $ Girl.change_face("bemused",1)
                            ch_j "\"And\" I'd rather not."
                        elif Girl == StormX:
                            ch_s "\"And\" I would prefer to keep it on."
                        elif Girl == JubesX:
                            ch_v "Well, I'm keeping it on."
                "Take it off anyway.":
                    if Line == "sure" or (Line == "sorry" and Girl != StormX and ApprovalCheck(Girl, 600+Mod, "O")):
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("obedience", 80, 2)
                        if Line != "sure":
                            $ Girl.change_face("sad",2)
                        else:
                            $ Girl.change_face("normal",1)
                        if Girl == RogueX:
                            ch_r "Oh, ok. . ."
                        elif Girl == KittyX:
                            ch_k "Yeah, ok. . ."
                        elif Girl == EmmaX:
                            ch_e "If you insist. . ."
                        elif Girl == LauraX:
                            ch_l "Affirmative."
                        elif Girl == JeanX:
                            ch_j ". . . ok."
                        elif Girl == StormX:
                            $ Girl.change_stat("love", 80, -2)
                            ch_s ". . . fine. . ."
                        elif Girl == JubesX:
                            ch_v "Whatever. . ."

                        $ Line = "sure"
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, -2)
                            $ Girl.change_stat("obedience", 80, -1)
                            $ Girl.change_stat("inhibition", 60, 1)

                        $ Girl.change_face("angry",1)
                        if Girl == RogueX:
                            ch_r "I don't like that tone on you. . ."
                        elif Girl == KittyX:
                            ch_k "How about \"no\". . ."
                        elif Girl == EmmaX:
                            ch_e "Not with that tone. . ."
                        elif Girl == LauraX:
                            ch_l "Don't push me."
                        elif Girl == JeanX:
                            $ Girl.change_face("bemused",1)
                            ch_j "Ha! no."
                        elif Girl == StormX:
                            $ Girl.change_stat("love", 80, -2)
                            ch_s "You presume too much."
                        elif Girl == JubesX:
                            ch_v "Nope."

                        $ Girl.AddWord(1,"no_tan","no_tan")
                        return
                "Hot.":
                    if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                        $ Girl.change_stat("love", 80, 1)
                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                        $ Girl.change_stat("inhibition", 80, 1)

                    $ Girl.change_face("sly",1)
                    if Girl == RogueX:
                        ch_r "Heh, you're a sweetie. . ."
                    elif Girl == KittyX:
                        ch_k "Hehe. . ."
                    elif Girl == EmmaX:
                        ch_e "How sweet. . ."
                    elif Girl == LauraX:
                        ch_l "True."
                    elif Girl == JeanX:
                        ch_j "You know it."
                    elif Girl == StormX:
                        ch_s ". . . I suppose so."
                    elif Girl == JubesX:
                        ch_v "Hehe. . ."
                "Ok, that's fine.":

                    if Line == "sure":
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 80, 1)
                            $ Girl.change_stat("inhibition", 60, 1)
                            $ Girl.change_stat("inhibition", 80, 1)

                        $ Girl.change_face("sly",1)
                        if Girl == RogueX:
                            ch_r "Ready for a nice surprise? . ."
                        elif Girl == KittyX:
                            ch_k "Oh, you bet it is. . ."
                        elif Girl == EmmaX:
                            ch_e "More than you know. . ."
                        elif Girl == LauraX:
                            ch_l "But I can be generous. . ."
                        elif Girl == JeanX:
                            ch_j "But. . . I guess I can make an exception. . ."
                        elif Girl == StormX:
                            ch_s "But you are right about the value in an even tan. . ."
                        elif Girl == JubesX:
                            ch_v "You bet. . ."
                    else:
                        if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                            $ Girl.change_stat("love", 50, 1)
                            $ Girl.change_stat("love", 80, 1)
                            $ Girl.change_stat("inhibition", 60, 1)

                        $ Girl.change_face("smile")
                        if Girl == RogueX:
                            ch_r "Thanks, [RogueX.player_petname]. . ."
                        elif Girl == KittyX:
                            ch_k "Thanks. . ."
                        elif Girl == EmmaX:
                            ch_e "Good. . ."
                        elif Girl == LauraX:
                            ch_l "Right."
                        elif Girl == JeanX:
                            ch_j "Good. . ."
                        elif Girl == StormX:
                            ch_s "I am sorry to disappoint."
                        elif Girl == JubesX:
                            ch_v "Thanks. . ."

            if Line == "sure":

                $ Girl.top = 0
                call expression Girl.Tag + "_First_Topless"
                if Type == "no_panties":
                    $ Girl.legs = 0
                    $ Girl.hose = 0
                    call expression Girl.Tag + "_First_Bottomless"
                $ Girl.AddWord(1,"tan","tan")
            else:
                $ Girl.AddWord(1,"no_tan","no_tan")

            $ Line = 0


        if Line == "sure":

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 70, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            $ Girl.change_face("sly",1)
            if Girl == RogueX:
                ch_r "I suppose I could. . ."
            elif Girl == KittyX:
                ch_k "I guess. . ."
            elif Girl == EmmaX:
                ch_e "Hmmm. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Yeah, ok."
            elif Girl == StormX:
                ch_s "I suppose I could."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            if Type == "jacket" or Type == "both":
                if Girl == JubesX:
                    $ Girl.accessory = 0
            if Type == "over" or Type == "both":
                $ Girl.top = 0
            if Type == "bra" or Type == "both":
                $ Girl.bra = 0
            call expression Girl.Tag + "_First_Topless"

            if Type == "legs" or Type == "both":
                $ Girl.legs = 0
                $ Girl.hose = 0
            if Type == "panties" or Type == "both":
                $ Girl.underwear = 0
            call expression Girl.Tag + "_First_Bottomless"

            $ Girl.AddWord(1,"tan","tan")

        elif Line == "sorry" and (Type == "over" or Type == "legs" or Type == "jacket"):

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("obedience", 80, 1)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_face("bemused",1)
            if Girl == RogueX:
                ch_r "I suppose I could. . ."
            elif Girl == KittyX:
                ch_k "I guess. . ."
            elif Girl == EmmaX:
                ch_e "Hmmm. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Sure, I guess."
            elif Girl == StormX:
                ch_s "I suppose I could."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            if Type == "jacket":
                $ Girl.accessory = 0
            if Type == "over":
                $ Girl.top = 0
            if Type == "legs":
                $ Girl.legs = 0
                $ Girl.hose = 0
            $ Girl.AddWord(1,"tan","tan")

        elif Line == "sorry":

            if "tan" not in Girl.recent_history and "no_tan" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 90, 2)
            $ Girl.change_face("sadside",1)
            if Girl == RogueX:
                ch_r "Sorry, I think I can live with the tan lines. . ."
            elif Girl == KittyX:
                ch_k "I just can't. . ."
            elif Girl == EmmaX:
                ch_e "That just wouldn't be appropriate. . ."
            elif Girl == LauraX:
                ch_l "Nah. . ."
            elif Girl == JeanX:
                ch_j "I. . . wouldn't be comfortable with that. . ."
            elif Girl == StormX:
                ch_s "I am sorry to disappoint you."
            elif Girl == JubesX:
                ch_v "Sorry. . ."
            $ Girl.AddWord(1,"no_tan","no_tan")

        elif Line == "no":

            $ Girl.change_stat("love", 50, -5)
            $ Girl.change_stat("obedience", 50, 2)
            $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_face("angry",1)
            if Girl == RogueX:
                ch_r "Not interested, [RogueX.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "Not even."
            elif Girl == EmmaX:
                ch_e "You must be dreaming. . ."
            elif Girl == LauraX:
                ch_l "Nope. . ."
            elif Girl == JeanX:
                ch_j "Ha!"
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Sure. . ."

            $ Girl.AddWord(1,"no_tan","no_tan")
            return
        if not Girl.bra and not Girl.top and not Girl.underwear and not Girl.legs and Girl.HoseNum() < 10:
            $ Girl.change_outfit("nude")
        $ Mod = 0
        $ Line = 0
        if Girl.ClothingCheck():
            "Anything else?"
        else:
            return
    return






label Pool_Skinnydip(Girl=0, Line=0, Type=0, Mod=0):




    menu:
        "With who?"
        "[RogueX.name]" if bg_current == RogueX.location:
            $ Girl = RogueX
        "[KittyX.name]" if bg_current == KittyX.location:
            $ Girl = KittyX
        "[EmmaX.name]" if bg_current == EmmaX.location:
            $ Girl = EmmaX
        "[LauraX.name]" if bg_current == LauraX.location:
            $ Girl = LauraX
        "[JeanX.name]" if bg_current == JeanX.location:
            $ Girl = JeanX
        "[StormX.name]" if bg_current == StormX.location:
            $ Girl = StormX
        "[JubesX.name]" if bg_current == JubesX.location:
            $ Girl = JubesX
        "Never mind.":
            return

    ch_p "Hey, [Girl.name], why don't we skinny dip?"

    if Round <= 10:
        $ Girl.change_face("sad")
        Girl.voice "No time for that."
        return
    elif "no_dip" in Girl.recent_history:
        $ Girl.change_face("angry")
        Girl.voice "I just told you \"no.\""
        $ Girl.AddWord(1,"angry","angry")
        return
    elif "no_dip" in Girl.daily_history:
        $ Girl.change_face("angry")
        Girl.voice "Not today."
        $ Girl.AddWord(1,"angry","angry")
        return
    elif "dip" in Girl.recent_history:
        $ Girl.change_face("confused")
        Girl.voice "We already did that."
        return

    if Girl == EmmaX:
        if "classcaught" not in EmmaX.history:
            $ Girl.change_face("angry",2)
            ch_e "That would be entirely inappropriate."
            return
        if "taboo" not in EmmaX.history:
            $ Girl.change_face("bemused",2)
            ch_e "[EmmaX.player_petname], I couldn't risk us getting caught. . ."
            return
        if "three" not in EmmaX.history:
            if not AloneCheck(EmmaX):
                $ Girl.change_face("bemused",2)
                ch_e "Not with this sort of company. . ."
                return

    if not Girl.ClothingCheck():

        $ Girl.change_face("sly")
        if Girl == RogueX:
            ch_r "Sure, let's get wet."
        elif Girl == KittyX:
            ch_k "Cannonball!"
        elif Girl == EmmaX:
            ch_e "Lovely."
        elif Girl == LauraX:
            ch_l "I'm in."
        elif Girl == JeanX:
            ch_j "Heh, sure."
        elif Girl == StormX:
            ch_s "I would love to."
        elif Girl == JubesX:
            ch_v "Sure!"

        $ Girl.AddWord(1,"dip","dip")
    else:

        if Girl.SeenPussy and Girl.SeenChest:
            $ Mod += 100

        if "exhibitionist" in Girl.Traits:

            $ Line = "sure"
        elif ApprovalCheck(Girl, 700-Mod, "I"):

            $ Line = "sure"
        elif ApprovalCheck(Girl, 1200-Mod) or (Girl == StormX and StormX in Rules):

            $ Line = "sure"
        elif ApprovalCheck(Girl, 800):

            $ Line = "sorry"
        else:

            $ Line = "no"

        if Line == "sure":

            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 70, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            $ Girl.change_face("sly",1)
            if Girl == RogueX:
                ch_r "Sounds fun. . ."
            elif Girl == KittyX:
                ch_k "Oooh, naughty. . ."
            elif Girl == EmmaX:
                ch_e "How daring. . ."
            elif Girl == LauraX:
                ch_l "Sure."
            elif Girl == JeanX:
                ch_j "Yeah, ok."
            elif Girl == StormX:
                ch_s "I would love to."
            elif Girl == JubesX:
                ch_v "Sure!"


            $ Girl.top = 0
            $ Girl.bra = 0
            call expression Girl.Tag + "_First_Topless"

            $ Girl.legs = 0
            $ Girl.hose = 0
            $ Girl.underwear = 0
            call expression Girl.Tag + "_First_Bottomless"
            $ Girl.change_outfit("nude")
            $ Girl.AddWord(1,"dip","dip")

        elif Line == "sorry":

            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("inhibition", 90, 2)
            $ Girl.change_face("sadside",1)
            if Girl == RogueX:
                ch_r "Couldn't we just take a normal swim?"
            elif Girl == KittyX:
                ch_k "I don't think so. . ."
            elif Girl == EmmaX:
                ch_e "Perhaps in a tub. . ."
            elif Girl == LauraX:
                ch_l "Nah. . ."
            elif Girl == JeanX:
                ch_j "Um, no, not right now."
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Yeah, not right now."
            menu:
                extend ""
                "Ok, we can just use swimsuits.":
                    if Girl.Swim[0]:

                        if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 60, 2)
                        $ Girl.change_face("smile")
                        if Girl == RogueX:
                            ch_r "Thanks, [RogueX.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Cool."
                        elif Girl == EmmaX:
                            ch_e "That would be nice."
                        elif Girl == LauraX:
                            ch_l "Whatever."
                        elif Girl == JeanX:
                            ch_j "Yeah, ok."
                        elif Girl == StormX:
                            ch_s "Yes, that would be fine."
                        elif Girl == JubesX:
                            ch_v "Sure!"

                        show blackscreen onlayer black
                        "She goes and changes into her suit. . ."
                        $ Girl.change_outfit("swimwear")
                        hide blackscreen onlayer black
                        $ Girl.AddWord(1,"no_dip","no_dip")
                        $ Count = 1
                    else:
                        if not Girl.change_outfit("swimwear"):
                            $ Count = 0
                    if not Count:

                        menu:
                            extend ""
                            "Then what about your undies?":
                                if Girl.ChestNum() > 2 and Girl.PantiesNum() > 2 and ApprovalCheck(Girl, 1000):

                                    pass
                                elif Girl.ChestNum() > 1 and Girl.PantiesNum() > 1 and ApprovalCheck(Girl, 1200):

                                    pass
                                else:
                                    $ Girl.change_face("sly",1)
                                    Girl.voice "That's not going to work either."
                                    $ Girl.AddWord(1,"no_dip","no_dip")
                                    return
                                $ Girl.change_face("smile",1)
                                if Girl == RogueX:
                                    ch_r "Ok, fine. . ."
                                elif Girl == KittyX:
                                    ch_k "Fine, geez."
                                elif Girl == EmmaX:
                                    ch_e "I suppose. . ."
                                elif Girl == LauraX:
                                    ch_l "Sure, whatever. . ."
                                elif Girl == JeanX:
                                    ch_j ". . . I guess."
                                elif Girl == StormX:
                                    ch_s "Oh, I suppose so. . ."
                                elif Girl == JubesX:
                                    ch_v "I guess so. . ."
                            "Ok then, never mind.":
                                Girl.voice "Thanks."
                                $ Girl.AddWord(1,"no_dip","no_dip")
                                return
                        $ Girl.top = 0
                        "She starts to strip down."
                        $ Girl.legs = 0
                        $ Girl.hose = 0
                        "And ends up in her underwear."
                        $ Girl.SeenPanties = 1
                "Never mind then.":


                    $ Girl.change_stat("love", 80, -1)
                    if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                    if Girl == RogueX:
                        ch_r "Hmph."
                    elif Girl == KittyX:
                        ch_k "Bummer."
                    elif Girl == EmmaX:
                        ch_e "Disappointing."
                    elif Girl == LauraX:
                        ch_l "K."
                    elif Girl == StormX:
                        ch_s "Thank you, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Ok."
                    $ Girl.AddWord(1,"no_dip","no_dip")
                    return

        elif Line == "no":

            $ Girl.change_stat("love", 50, -5)
            if "dip" not in Girl.recent_history and "no_dip" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_face("angry",1)
            if Girl == RogueX:
                ch_r "Not interested, [RogueX.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "Not even."
            elif Girl == EmmaX:
                ch_e "You must be dreaming. . ."
            elif Girl == LauraX:
                ch_l "Nope. . ."
            elif Girl == JeanX:
                $ Girl.change_face("bemused",1)
                ch_j "Ha!"
            elif Girl == StormX:
                ch_s "I am afraid not, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "Sorry. . ."

            $ Girl.AddWord(1,"no_dip","no_dip")
            return

    call ShowPool ([Girl])
    $ Girl.Water = 1
    $ Round -= 20 if Round >= 20 else Round
    "You both swim around for a bit."
    hide FullPool
    call set_the_scene (1, 0, 0)

    return





label Pool_Topless(Girl=focused_Girl, BO=[]):

    if Girl.location != bg_current:

        $ BO = all_Girls[:]
        $ renpy.random.shuffle(BO)
        while BO:
            if BO[0].location == bg_current:
                call shift_focus (BO[0])
                $ BO = [1]
            $ BO.remove(BO[0])

    $ focused_Girl = Girl
    if (Girl.ChestNum() <= 1 and Girl.OverNum() <= 1) or Girl.location != bg_current:

        $ D20 = renpy.random.randint(1, 14)
        return
    $ Girl.Uptop = 1
    "[Girl.name] dives into the pool"
    menu:
        "It appears she's had a wardrobe malfunction."
        "Hey, [Girl.name]. . .":
            ch_p "Looks like you might be missing something there. . ."
            $ Girl.change_face("confused")
            if Girl != StormX:
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 50, -2)
                Girl.voice ". . ."
                $ Girl.change_face("surprised",2,Eyes="down")
            $ Girl.change_stat("love", 80, 3)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("lust", 50, 2)
            $ Count = 100
        "Say nothing":
            $ Girl.change_face("surprised",2,Eyes="down")
            "After a few moments, [Girl.name] seems to notice that her top rode up."
            if ApprovalCheck(Girl, 1200):
                $ Count = 0
            else:
                $ Count = -100

    if ApprovalCheck(Girl, 800-Count,"I") or ApprovalCheck(Girl, 1600-Count) or (Girl == StormX and StormX in Rules):
        $ Girl.change_face("sly")
        $ Girl.bra = 0
        $ Girl.top = 0
        $ Girl.change_stat("obedience", 60, 2)
        $ Girl.change_stat("inhibition", 50, 4)
        $ Girl.change_stat("inhibition", 90, 2)
        $ Girl.change_stat("lust", 50, 5)
        "She smiles and tosses her top over her head."
        call expression Girl.Tag + "_First_Topless"
    elif ApprovalCheck(Girl, 500-Count,"I") or ApprovalCheck(Girl, 1200-Count):
        $ Girl.change_face("sly",1)
        $ Girl.change_stat("obedience", 60, 2)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("inhibition", 80, 2)
        $ Girl.change_stat("lust", 50, 3)
        "She smiles, and leaves the top how it is."
        call expression Girl.Tag + "_First_Topless"
    else:
        if ApprovalCheck(Girl, 800-Count) or (Girl == StormX):

            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("inhibition", 70, 2)
            $ Girl.change_stat("lust", 50, 1)
            $ Girl.change_face("bemused",2)
        else:

            $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_face("angry",2)
        call expression Girl.Tag + "_First_Topless" pass (1)
        $ Girl.Uptop = 0
        "She tugs her top back into place."
        if Count <= 0:
            $ Girl.change_stat("love", 70, -5)
            $ Girl.change_stat("obedience", 60, -2)
            $ Girl.change_stat("inhibition", 60, 2)
            Girl.voice "You could have told me."

    $ Count = 0
    return





label Breakup(Girl=0, Other=0, Anger=0, BO=[]):



    $ Girl.AddWord(1,"breakup talk","breakup talk",0,0)

    if Girl.Break[1] > 3:
        $ Girl.change_face("angry")
        $ Girl.change_stat("love", 50, -5, 1)
        $ Girl.change_stat("love", 80, -10, 1)
        $ Girl.change_stat("obedience", 30, -5, 1)
        $ Girl.change_stat("obedience", 50, -10, 1)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("inhibition", 80, 1)
        Girl.voice "This is getting old."
        $ Anger -= 1
    elif Girl.Break[1]:
        $ Girl.change_face("surprised")
        $ Girl.change_stat("love", 50, -5, 1)
        $ Girl.change_stat("obedience", 30, -5, 1)
        $ Girl.change_stat("inhibition", 80, 1)
        Girl.voice "What, again?"
        $ Girl.change_face("angry")
        $ Anger += 1
    else:
        $ Girl.change_face("surprised")
        Girl.voice "What?! Why?"

    $ Line = 0
    menu:
        "It's not you, it's me.":
            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_stat("obedience", 80, -5)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("inhibition", 70, 1)
            $ Girl.change_face("confused")
        "I just think we need a break.":

            $ Girl.change_stat("love", 200, -5)
            $ Girl.change_face("sad")
        "I've found someone else.":

            $ Anger += 1
            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 3)
            $ Girl.change_stat("inhibition", 50, -5)
            $ Girl.change_face("angry")
            Girl.voice "Who is it?"
            menu:
                extend ""
                "[RogueX.name]" if Girl != RogueX:
                    $ Other = RogueX
                "[KittyX.name]" if Girl != KittyX and "met" in KittyX.history:
                    $ Other = KittyX
                "[EmmaX.name]" if Girl != EmmaX and "met" in EmmaX.history:
                    $ Other = EmmaX
                "[LauraX.name]" if Girl != LauraX and "met" in LauraX.history:
                    $ Other = LauraX
                "[JeanX.name]" if Girl != JeanX and "met" in JeanX.history:
                    $ Other = JeanX
                "[StormX.name]" if Girl != StormX and "met" in StormX.history:
                    $ Other = StormX
                "[JubesX.name]" if Girl != JubesX and "met" in JubesX.history:
                    $ Other = JubesX
                "I won't say.":
                    $ Girl.change_stat("love", 200, -5)
                    $ BO = active_Girls[:]
                    $ BO.remove(Girl)
                    $ Count = 0
                    while BO:
                        if BO[0].SEXP > Count:

                            $ Other = BO[0]
                            $ Count = BO[0].SEXP
                        $ BO.remove(BO[0])
                    $ Count = 0
                    if not Other:
                        Girl.voice "Well it's got to be someone. . ."
                    else:
                        Girl.voice "It's [Other.name], isn't it."
                "I was kidding.":
                    $ Girl.change_stat("love", 200, -5)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_face("angry")
                    if Girl == RogueX:
                        ch_r "That was a pretty rude way to deflect there."
                    elif Girl == KittyX:
                        ch_k "I'll[KittyX.like]kid you!"
                    elif Girl == EmmaX:
                        ch_e "Oh, you do *not* want to \"kid\" me about that."
                    elif Girl == LauraX:
                        ch_l ". . ."
                    elif Girl == JeanX:
                        ch_j "The last time I heard a joke like that, someone lost a 7th birthday."
                    elif Girl == StormX:
                        ch_s "You should not \"kid\" about such things, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Right. . ."
                    $ Girl.change_face("normal")
                    $ Anger += 1
        "I'm just done with you.":

            $ Girl.change_face("angry")
            $ Girl.change_stat("love", 50, 3)
            $ Girl.change_stat("love", 200, -15)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 80, 5)
            $ Girl.change_stat("obedience", 200,5)
            $ Girl.change_stat("inhibition", 50, -5)
            $ Anger += 1


    if not Other:

        $ Girl.change_face("sad")
        if ApprovalCheck(Girl, 900, "O"):

            Girl.voice "If that's really what you want. . ."
        elif ApprovalCheck(Girl, 900, "L"):

            Girl.voice "But I love you so much!"
        elif ApprovalCheck(Girl, 900, "I") or Girl == JeanX:

            Girl.voice "If that's how you feel. . ."
        elif ApprovalCheck(Girl, 1500):

            Girl.voice "But we mean so much to each other!"
        else:

            Girl.voice "Are you sure this is what you want?"
        $ Line = "bargaining"
    else:



        $ counter = int((Girl.GirlLikeCheck(Other) - 500)/2)

        if Girl.GirlLikeCheck(Other) >= 800:
            $ Girl.change_stat("lust", 70, 5)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 200, 5)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_stat("inhibition", 200, 5)
            $ Girl.change_face(5,2)
            Girl.voice "Well, you have good tastes, at least."
            $ Girl.change_face(5,1)
        elif Girl.GirlLikeCheck(Other) >= 600:
            $ Girl.change_stat("love", 50, -5, 1)
            $ Girl.change_stat("love", 80, -10, 1)
            $ Girl.change_stat("obedience", 50, 5)
            $ Girl.change_stat("obedience", 200, 3)
            if Other == EmmaX and Girl != StormX:
                Girl.voice "With our teacher?!"
            if Other == StormX and Girl != EmmaX:
                Girl.voice "With our teacher?!"
            elif Girl == EmmaX and Other != StormX:
                ch_e "And I always did like her in class. . ."
            elif Girl == StormX and Other == EmmaX:
                ch_s "And she seemed so respectable. . ."
            elif Girl in (EmmaX,StormX) and Other in (EmmaX,StormX):
                Girl.voice "You have a thing for teachers?"
            elif Girl == LauraX:
                ch_l "I do kinda like her."
            elif Girl == JeanX:
                ch_j "Well, she's not a complete bitch."
            else:
                Girl.voice "With one of my friends?!"
            $ Girl.change_face("normal")
            $ Anger += 1
        elif Girl.GirlLikeCheck(Other) >= 400:
            $ Girl.change_stat("love", 50, -3, 1)
            $ Girl.change_stat("love", 80, -5, 1)
            $ Girl.change_stat("obedience", 80, 5)
            $ Girl.change_stat("inhibition", 50, 1)
            $ Girl.change_stat("inhibition", 80, 3)
            Girl.voice "You know you can do better."
        else:
            $ Girl.change_stat("love", 50, -5, 1)
            $ Girl.change_stat("obedience", 80, 3)
            $ Girl.change_stat("inhibition", 50, 2)
            $ Girl.change_stat("inhibition", 80, 5)
            $ Girl.change_face("angry")
            Girl.voice "With that skank?!"
            $ Anger += 2

        if ApprovalCheck(Girl, 2000, Bonus = counter):
            $ Girl.change_stat("lust", 70, 5)
            $ Girl.change_face("sexy")
            Girl.voice "Why not both of us?"
            $ Line = "threeway"
        else:
            $ Girl.change_face("sad")
            Girl.voice "You would rather be with her than with me?"
            menu:
                extend ""
                "Yes, I would.":
                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("love", 80, -5, 1)
                    $ Girl.change_stat("obedience", 30, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Anger += 1
                    $ Line = "bargaining"
                    if Girl == RogueX:
                        ch_r "Well then I don't think I can help you."
                    elif Girl == KittyX:
                        ch_k "!!!"
                    elif Girl == EmmaX:
                        ch_e "I suppose you've made your choice then."
                    elif Girl == LauraX:
                        ch_l "Your loss."
                    elif Girl == JeanX:
                        ch_j "Nonsense."
                    elif Girl == StormX:
                        ch_s "Then I understand."
                        $ Line = "threeway"
                    elif Girl == JubesX:
                        ch_v "Rough. . ."
                "I'd rather be with both of you.":

                    $ Line = "threeway"
                "No, I'm sorry, never mind that.":

                    $ Girl.change_stat("love", 50, -3, 1)
                    $ Girl.change_stat("obedience", 80, -5)
                    Girl.voice "Not doing yourself any favors there. . ."
                    $ Line = "bargaining"


    if Line == "threeway" and Anger < 4:
        if Girl == StormX:
            ch_s "So would she be fine with you dating us both?"
        else:
            Girl.voice "Date us both at once? What does she think about that?"
        menu Breakup_Threeway_Offer:
            extend ""
            "She said it would be ok with her." if "poly "+ Girl.Tag in Other.Traits or Girl.Tag+"Yes" in Player.Traits:

                if ApprovalCheck(Girl, 1800, Bonus = counter):
                    $ Girl.change_face("smile", 1)
                    $ Girl.change_stat("lust", 70, 5)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_stat("inhibition", 80, 1)
                    if Girl.GirlLikeCheck(Other) < 400:
                        $ Girl.change_face("angry")
                        if Girl == RogueX:
                            ch_r "I can't stand that bitch, but for you I'll put up with her."
                        elif Girl == KittyX:
                            ch_k "That bitch! Fine, I'll put up with her."
                        elif Girl == EmmaX:
                            ch_e "I suppose I can be the better woman here. . ."
                            ch_e "Not that it's hard to accomplish."
                        elif Girl == LauraX:
                            ch_l "I can keep my claws in. . . for you."
                        elif Girl == JeanX:
                            ch_j "Well. . I guess I can find -some- use for her."
                        elif Girl == StormX:
                            ch_s "I dislike her, but I will put up with her."
                        elif Girl == JubesX:
                            ch_v "Well, this is not cool. . . but I can deal. . ."
                    elif Girl == StormX:
                        ch_s "Then that is all I need to know."
                    elif Girl.GirlLikeCheck(Other) >= 700 or Girl == JeanX:
                        $ Girl.change_face("sexy")
                        Girl.voice "I have to say I've kind of been thinking about it myself."
                    elif Girl.love >= Girl.obedience:
                        $ Girl.change_face("sad")
                        Girl.voice "Just so long as we can be together, I can share."
                    else:

                        Girl.voice "If she's in, I am."

                    $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0)
                else:
                    $ Anger += 2
                    $ Girl.change_stat("love", 50, -10, 1)
                    $ Girl.change_stat("love", 80, -15, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 50, 5)
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_face("angry", 1)
                    Girl.voice "Well maybe she did, but I don't want to share."
                    $ Line = "bargaining"
                    if Girl == StormX:
                        $ Line = "breakup"
            "I have no idea.":


                $ Line = "ask " + Other.Tag
            "She's not into it.":

                if Girl.GirlLikeCheck(Other) >= 700:
                    $ Girl.change_stat("love", 200, -5)
                elif Girl.GirlLikeCheck(Other) <= 400:
                    $ Girl.change_stat("love", 90, 5)
                Girl.voice "Well then why even bring it up?"
            "Well, even if she doesn't agree. . .":


                $ Line = "ask " + Other.Tag
                if Girl.GirlLikeCheck(Other) >= 700:
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 200, -5)
                elif Girl.GirlLikeCheck(Other) <= 400:
                    $ Girl.change_stat("love", 90, 5)

        if Line == "ask " + Other.Tag and Girl.GirlLikeCheck(Other) >= 700:

            Girl.voice "You want me to ask her for you?"
            menu:
                extend ""
                "Yes, that'd be a good idea.":
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("obedience", 70, 1)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_face("sexy")
                    Girl.voice "I guess I could."
                    $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0)
                    $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0)
                "No, let's just keep it under cover.":
                    $ Girl.change_stat("love", 50, -5, 1)
                    $ Girl.change_stat("love", 80, -5, 1)
                    $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_stat("inhibition", 50, 3)
                    Girl.voice "I don't know. . ."

        if Line == "breakup":
            pass
        elif Line != "bargaining" and "poly "+ Other.Tag not in Girl.Traits:


            if "ask "+ Other.Tag not in Girl.Traits and not ApprovalCheck(Girl, 1800, Bonus = -(int((Girl.GirlLikeCheck(Other) - 600)/2))):


                $ Girl.change_stat("love", 50, -5, 1)
                $ Girl.change_stat("obedience", 80, -10, 1)
                $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_face("angry", 1)
                if not ApprovalCheck(Girl, 1800):
                    Girl.voice "Maybe I don't like you that much either."
                else:
                    $ Girl.change_stat("love", 80, -10, 1)
                    $ Girl.change_stat("obedience", 50, -5, 1)
                    if Girl == EmmaX and Other != StormX:
                        ch_e "I'd rather not be dallying with another teacher's boyfriend. . ."
                    elif Girl == EmmaX:
                        ch_e "I'd rather not be dallying with a student's boyfriend. . ."
                    elif Girl == StormX:
                        ch_s "I would rather not creep around like that."
                    elif Girl == JeanX:
                        ch_j "I don't know, shes a little boring. . ."
                    elif Other == EmmaX:
                        Girl.voice "I don't want to get caught with the teacher's boyfriend!"
                    else:
                        Girl.voice "I'm not really cool with that, [Other.name]'s a friend of mine."
                $ Anger += 1
                if Girl != StormX:
                    $ Line = "bargaining"
            else:

                $ Girl.change_stat("obedience", 30, 5)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("inhibition", 50, 5)
                $ Girl.change_stat("inhibition", 80, 1)
                $ Girl.change_face("sad")
                if Girl.GirlLikeCheck(Other) < 400:
                    $ Girl.change_face("angry")
                    if Girl == RogueX:
                        ch_r "I can't stand that bitch, but for you I'll put up with her."
                    elif Girl == KittyX:
                        ch_k "That bitch! Fine, I'll put up with her."
                    elif Girl == EmmaX:
                        ch_e "I suppose I can be the better woman here. . ."
                        ch_e "Not that it's hard to accomplish."
                    elif Girl == LauraX:
                        ch_l "I can keep my claws in. . . for you."
                    elif Girl == JeanX:
                        ch_j "Well. . I guess I can find -some- use for her."
                    elif Girl == StormX:
                        ch_s "I dislike her, but I will put up with her."
                    elif Girl == JubesX:
                        ch_v "Well, this is not cool. . . but I can deal. . ."
                elif Girl.GirlLikeCheck(Other) >= 700:
                    $ Girl.change_face("sexy")
                    Girl.voice "I have to say I've kind of been thinking about it myself."
                elif Girl.love >= Girl.obedience:

                    $ Girl.change_face("sad")
                    Girl.voice "Just so long as we can be together, I can share."
                else:

                    Girl.voice "If she's in, I am."
                $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0)
                if "ask "+ Other.Tag in Girl.Traits:

                    Girl.voice "I'll talk to [Other.name] about it."
                else:
                    $ Girl.change_face("sad")
                    $ Girl.AddWord(1,0,0,"downlow",0)
                    if Girl == RogueX:
                        ch_r "I guess we can keep this on the downlow, for now at least."
                    elif Girl == KittyX:
                        ch_k "Oooh, our little secret. . ."
                    elif Girl == EmmaX:
                        ch_e "I suppose I can be discreet."
                    elif Girl == LauraX:
                        ch_l "I can keep a secret."
                    elif Girl == JeanX:
                        ch_j "Sure, that works."
                    elif Girl == StormX:
                        ch_s "I can keep my secrets."
                    elif Girl == JubesX:
                        ch_v "I can keep to myself. . ."

                    if Girl.GirlLikeCheck(Other) >= 800 and Girl != JeanX:
                        Girl.voice "Please talk to [Other.name] about sharing you openly though."
                    elif Girl.GirlLikeCheck(Other) >= 500 and Girl != JeanX:
                        Girl.voice "I really don't like going behind [Other.name]'s back though."
                    else:
                        Girl.voice "Might be fun, sneaking around behind her back."


    if Line == "bargaining" and Anger < 4:
        $ Girl.change_face("sad")
        Girl.voice "You're sure there's no way I could convince you to stay?"
        menu Breakup_Bargaining:
            extend ""
            "Sorry, I've changed my mind.":
                $ Girl.change_stat("obedience", 80, 5)
                if ApprovalCheck(Girl, 1500):
                    $ Line = "makeup"
                    $ Girl.change_stat("love", 80, 5)
                    if Girl == RogueX:
                        ch_r "That's wonderful!"
                    elif Girl == KittyX:
                        ch_k "Ok!"
                    elif Girl == EmmaX:
                        ch_e "I can accept that as an apology. . ."
                    elif Girl == LauraX:
                        ch_l "Huh? Ok. . ."
                    elif Girl == JeanX:
                        ch_j "Finally, you've come to your senses."
                    elif Girl == StormX:
                        ch_s "Then you can stay."
                    elif Girl == JubesX:
                        ch_v "Cool. . ."
                else:
                    $ Line = "breakup"
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 80, -5)
                    $ Girl.change_stat("inhibition", 80, 10)
                    if Girl == RogueX:
                        ch_r "You know what? Save it. We're done."
                    elif Girl == KittyX:
                        ch_k "Too little, too late. . ."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid it's too late for apologies."
                    elif Girl == LauraX:
                        ch_l "Uh-huh. Too late for that."
                    elif Girl == JeanX:
                        ch_j "You know what? Too late."
                    elif Girl == StormX:
                        ch_s "I am not interested in your games."
                    elif Girl == JubesX:
                        ch_v "Too late. . ."
            "My mind's made up.":
                $ Girl.change_stat("obedience", 80, 5)
                $ Line = "breakup"
            "Well, you could do something for me. . .[[sex menu]":
                $ Girl.AddWord(1,"bargainsex",0,0,0)
                $ Girl.change_stat("obedience", 80, 3)
                $ approval_bonus = 50
                $ multi_action = 0
                call expression Girl.Tag + "_SMenu"
                $ multi_action = 1
                menu:
                    "Ok, I guess we can give it another shot.":
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 80, 5)
                        $ Line = "makeup"
                        $ Girl.change_face("smile")
                    "That was nice, but we're still over.":

                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("love", 80, -10, 1)
                        $ Girl.change_stat("obedience", 50, 15)
                        $ Girl.change_stat("obedience", 80, 10)
                        $ Line = "breakup"
                        $ Anger += 4

            "Maybe if we brought someone else into this relationship?" if not Other and "bargainthreeway" not in Girl.recent_history:

                $ Girl.AddWord(1,"bargainthreeway",0,0,0)
                Girl.voice "Who?"
                menu:
                    extend ""
                    "[RogueX.name]?" if Girl != RogueX:
                        $ Other = RogueX
                    "[KittyX.name]?" if Girl != KittyX and "met" in KittyX.history:
                        $ Other = KittyX
                    "[EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.history:
                        $ Other = EmmaX
                    "[LauraX.name]?" if Girl != LauraX and "met" in LauraX.history:
                        $ Other = LauraX
                    "[JeanX.name]?" if Girl != JeanX and "met" in JeanX.history:
                        $ Other = JeanX
                    "[StormX.name]?" if Girl != StormX and "met" in StormX.history:
                        $ Other = StormX
                    "[JubesX.name]?" if Girl != JubesX and "met" in JubesX.history:
                        $ Other = JubesX
                    "Up to you?":

                        $ Girl.change_face("confused")

                        $ BO = active_Girls[:]
                        $ BO.remove(Girl)
                        $ Count = 0
                        while BO:
                            if Girl.GirlLikeCheck(BO[0]) > Count:

                                $ Other = BO[0]
                                $ Count = Girl.GirlLikeCheck(BO[0])
                            $ BO.remove(BO[0])
                        $ Count = 0
                        Girl.voice "[Other.name]?"
                    "Never mind, silly question.":

                        $ Girl.change_stat("love", 200, -10)
                        $ Girl.change_stat("obedience", 50, -10, 1)
                        $ Anger += 1
                        $ Girl.change_face("angry")
                        jump Breakup_Bargaining

                if Other:
                    $ Girl.change_face("confused")
                    jump Breakup_Threeway_Offer

        if Anger < 3 and Line != "breakup" and Line != "makeup":

            if Girl == StormX:
                $ Line = "breakup"
            else:
                jump Breakup_Bargaining




    if Line == "breakup" or Anger >= 4:
        if Anger >= 4:

            $ Girl.change_face("angry")
            $ Girl.change_stat("love", 60, -10, 1)
            $ Girl.change_stat("obedience", 50, -5)
            $ Girl.change_stat("inhibition", 70, 5)
            if Girl == RogueX:
                ch_r "Well fuck you then!"
            elif Girl == KittyX:
                ch_k "Jerk!!"
            elif Girl == EmmaX:
                ch_e "Scum."
            elif Girl == LauraX:
                ch_l "You're gonna want to back up a few steps."
            elif Girl == JeanX:
                ch_j "Ok, that's it, I'm pulling the plug on this one!"
            elif Girl == StormX:
                ch_s "I am afraid that you have overstayed your welcome."
            elif Girl == JubesX:
                ch_v "Fuck off then!"
        else:

            $ Girl.change_stat("inhibition", 70, 5)
            $ Girl.change_face("sad")

            if Girl.love >= Girl.obedience:

                if Girl == RogueX:
                    ch_r "I'll really miss you."
                elif Girl == KittyX:
                    ch_k "I was[KittyX.like]totally all-in on this!"
                elif Girl == EmmaX:
                    ch_e "I'll be devastated."
                    ch_e "For at least five minutes."
                elif Girl == LauraX:
                    ch_l ". . ."
                elif Girl == JeanX:
                    ch_j "You know what. . . forget it."
                elif Girl == StormX:
                    ch_s "I will miss you."
                elif Girl == JubesX:
                    ch_v "I'll miss you. . ."
                $ Girl.AddWord(1,0,0,"ex",0)
            elif Girl.obedience >= Girl.inhibition:

                $ Girl.change_stat("obedience", 200, -10)
                if Girl == RogueX:
                    ch_r "You're abandoning me."
                elif Girl == KittyX:
                    ch_k "I'm[KittyX.like]not sure what to do next."
                elif Girl == EmmaX:
                    ch_e "I suppose I'll have to make do."
                elif Girl == LauraX:
                    ch_l "I'll need some new options."
                elif Girl == JeanX:
                    ch_j "Ok, never mind then."
                elif Girl == StormX:
                    ch_s "I am sorry it has come to this."
                elif Girl == JubesX:
                    ch_v "I needed this. . ."
                $ Girl.AddWord(1,0,0,"ex",0)
            else:

                if Girl == RogueX:
                    ch_r "Now who'll I fuck?"
                elif Girl == KittyX:
                    ch_k "I guess I'll[KittyX.like]have to find someone else to bang?"
                elif Girl == EmmaX:
                    ch_e "I suppose I'll have other options."
                elif Girl == LauraX:
                    ch_l "Ok, later."
                elif Girl == JeanX:
                    ch_j "Ok, that's cool."
                elif Girl == StormX:
                    ch_s "Well, I will find a way to move on."
                elif Girl == JubesX:
                    ch_v "This was fun. . ."


        if Girl in Player.Harem:
            $ Player.Harem.remove(Girl)

        $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
        $ Girl.Break[1] += 1
    else:



        $ Girl.change_face("smile")
        Girl.voice "I'm glad we could work things out. . ."
        if Girl.love >= Girl.obedience:

            $ Girl.change_stat("love", 200, 3)
            if Girl == RogueX:
                ch_r "I'd really miss you."
            elif Girl == KittyX:
                ch_k "I'd[KittyX.like]totes miss you!"
            elif Girl == EmmaX:
                ch_e "I'm in too deep, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "I. . . care about you."
            elif Girl == JeanX:
                ch_j "You've really grown on me."
                $ Girl.change_face("sly")
                ch_j "Like a one of those teacup pigs. . ."
            elif Girl == StormX:
                ch_s "I would miss you very much."
            elif Girl == JubesX:
                ch_v "I woulda missed you. . ."
        elif Girl.obedience >= Girl.inhibition:

            if Girl == RogueX:
                ch_r "I need you with me."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]totally all-in on this."
            elif Girl == EmmaX:
                ch_e "I don't think I could do without you."
            elif Girl == LauraX:
                ch_l "I need you too much."
            elif Girl == JeanX:
                ch_j "I was really starting to enjoy this. . ."
            elif Girl == StormX:
                ch_s "I would miss you very much."
            elif Girl == JubesX:
                ch_v "I need this. . ."
        else:

            if Girl == RogueX:
                ch_r "We have fun together. Let's keep it at that."
            elif Girl == KittyX:
                ch_k "You[KittyX.like]really dodged a bullet on that one."
            elif Girl == EmmaX:
                ch_e "It's too much trouble finding another toy."
            elif Girl == LauraX:
                ch_l "Ok, fine."
            elif Girl == JeanX:
                ch_j "Yeah. . . ok."
            elif Girl == StormX:
                ch_s "I suppose so."
            elif Girl == JubesX:
                ch_v "This is fun, right?"
    $ Line = 0
    return






label CheatCheck(BO=[], BO2=[]):







    $ BO = all_Girls[:]
    $ renpy.random.shuffle(BO)
    while BO:
        if "locked" in Player.Traits and BO[0].location != bg_current:

            pass
        else:
            $ BO2 = all_Girls[:]
            while BO2:
                if "meet girl" in Player.daily_history:

                    return
                elif BO[0] in Player.Harem:

                    if "saw with " + BO2[0].Tag in BO[0].Traits:

                        if BO[0] in Player.Harem and BO2[0] in Player.Harem:

                            $ BO[0].DrainWord("saw with "+BO2[0].Tag,0,0,1)
                        elif BO[0] in Player.Harem and BO2[0].Tag + "Yes" in Player.Traits:
                            $ BO[0].DrainWord("saw with "+BO2[0].Tag,0,0,1)
                        elif bg_current == "bg_player" or bg_current == BO[0].home:
                            call Cheated (BO[0], BO2[0])
                            $ renpy.pop_call()
                            return
                $ BO2.remove(BO2[0])
        $ BO.remove(BO[0])
    return

label ShareCheck(BO=[], BO2=[]):





    $ BO = all_Girls[:]
    $ BO.remove(StormX)
    while BO:
        if BO[0] in Player.Harem:

            $ BO2 = all_Girls[:]
            $ BO2.remove(StormX)
            while BO2:
                if "ask " + BO2[0].Tag in BO[0].Traits:

                    if BO[0] in Player.Harem and BO2[0] in Player.Harem:

                        $ BO[0].DrainWord("ask "+BO2[0].Tag,0,0,1)
                    else:
                        call Share (BO[0], BO2[0])
                        $ renpy.pop_call()
                        return
                $ BO2.remove(BO2[0])
        $ BO.remove(BO[0])
    return

label AddictCheck(BO=[]):


    $ BO = active_Girls[:]
    $ renpy.random.shuffle(BO)
    if JubesX in BO and JubesX.addiction >= 40 and BO[0].resistance:
        $ BO.remove(JubesX)
        if "sunshine" not in JubesX.history or "addiction" in JubesX.daily_history:
            pass
        elif bg_current == JubesX.home or bg_current == "bg_player":
            if not JubesX.resistance:

                call First_Addicted (JubesX)
            else:
                call Addiction_Fix (JubesX)
        else:
            if "asked meet" in JubesX.daily_history:
                pass
            elif "asked meet" in JubesX.daily_history and JubesX.addiction >= 60:
                "[JubesX.name] texts you. . ."
                JubesX.voice "I know I asked to meet you in your room earlier, but I really need a fix."
                $ Player.AddWord(1,"asked fix",0,0,0)
                $ JubesX.AddWord(1,"asked meet","asked meet",0,0)
                call ReturnToRoom
                return
            else:
                "[JubesX.name] texts and asks if you could get her a fix later."
                $ JubesX.AddWord(1,"asked meet","asked meet",0,0)
                call ReturnToRoom
                return
    while BO:
        if "locked" in Player.Traits and BO[0].location != bg_current:

            pass
        elif "asked fix" in Player.daily_history and "asked meet" not in BO[0].daily_history:

            pass
        elif BO[0].Event[3]:

            pass
        elif "angry" not in BO[0].recent_history and "addiction" not in BO[0].daily_history and BO[0].remaining_actions >= 1:

            if (BO[0].addiction >= 60 or (BO[0].addiction >= 40 and BO[0] == JubesX)) and BO[0].resistance:

                if bg_current == BO[0].home or bg_current == "bg_player":
                    call Addiction_Fix (BO[0])
                else:
                    if "asked meet" in BO[0].recent_history:
                        pass
                    elif "asked meet" in BO[0].daily_history and BO[0].addiction >= 80:
                        "[BO[0].name] texts you. . ."
                        BO[0].voice "I know I asked to meet you in your room earlier, but I'm serious, this is important."
                        $ Player.AddWord(1,"asked fix",0,0,0)
                        $ BO[0].AddWord(1,"asked meet","asked meet",0,0)
                        call ReturnToRoom
                        return
                    else:
                        "[BO[0].name] texts and asks if you could meet her in your room later."
                        $ BO[0].AddWord(1,"asked meet","asked meet",0,0)
                        call ReturnToRoom
                        return

            elif BO[0].resistance:
                pass

            elif BO[0] == JubesX and BO[0].addiction < 50:
                pass
            elif BO[0].addiction >= 35 and not BO[0].Event[1]:

                call First_Addicted (BO[0])
            elif BO[0].addiction >= 60 and BO[0].Event[1] <= 2:

                call First_Addicted (BO[0])
            elif BO[0].addiction >= 90:

                call First_Addicted (BO[0])
        $ BO.remove(BO[0])
    return


label Share(Girl=0, Other=0):



    $ Girl.DrainWord("ask "+Other.Tag,0,0,1)

    if Girl.Break[0]:

        "[Girl.name] sends you a text."
        $ Other.change_stat("love", 90, -10)
        $ Other.change_stat("obedience", 80, 10)
        $ Other.change_stat("inhibition", 80, 5)

        if Other == RogueX:
            Girl.voice "She said to \"stop bother'in her?\""
        elif Other == KittyX:
            Girl.voice "She said to \"give it a rest?\""
        elif Other == EmmaX:
            Girl.voice "She said \"when hell freezes over?\""
        elif Other == LauraX:
            Girl.voice "She said to \"fuck off?\""
        elif Other == JeanX:
            Girl.voice "She didn't seem to know who I was talking about."
        elif Other == StormX:
            Girl.voice "She said \"I would rather not?\""
        elif Other == JubesX:
            Girl.voice "She said to \"give it a rest?\""
        Girl.voice "I guess we can see if she comes around on the idea."
    else:

        if Other == JeanX or Other.GirlLikeCheck(Girl) >= 800 or ApprovalCheck(Other, 1800) or (ApprovalCheck(Other, 1500) and Other.GirlLikeCheck(Girl) >= 500):

            $ Other.AddWord(1,0,0,"poly "+Girl.Tag,0)


            $ Other.change_stat("obedience", 80, 10)
            $ Other.change_stat("inhibition", 80, 15)

            $ BO = Player.Harem[:]
            while BO:
                $ BO[0].DrainWord("saw with "+Other.Tag,0,0,1)
                $ BO.remove(BO[0])
            if Girl.Event[5]:

                $ Player.Harem.append(Other)

            elif bg_current in PersonalRooms:

                if Other.Tag+"Yes" not in Player.Traits:
                    $ Player.Traits.append(Other.Tag+"Yes")
                call expression Other.Tag + "_BF"
                $ renpy.pop_call()
                $ renpy.pop_call()
            else:

                if Other.Tag+"Yes" not in Player.Traits:
                    $ Player.Traits.append(Other.Tag+"Yes")
                call AskedMeet (Other, "bemused")
        else:

            "[Girl.name] sends you a text."
            Girl.voice "I talked to [Other.name] about sharing you, and she said she wasn't into that sort of thing,"
            if not ApprovalCheck(Other, 2000):
                $ Other.change_stat("love", 200, -15)
                $ Other.change_stat("obedience", 50, -5)
                $ Other.change_stat("inhibition", 50, 5)
                Girl.voice "She's just not into you like that."
            else:
                $ Other.change_stat("love", 200, -5)
                Girl.voice "She doesn't really like me that much. . ."


            $ Other.Break[0] = 7
    return



label Cheated(Girl=0, Other=0, Resolution=0, B=0):


    $ Girl.AddWord(1,0,"relationship",0,0)
    call shift_focus (Girl)

    $ Girl.change_face("angry")
    if Girl.location != bg_current and Girl not in Party:
        "Suddenly, [Girl.name] shows up and says she needs to talk to you."
    $ Girl.location = bg_current

    $ Girl.DrainWord("asked meet",0,1)
    if "meet girl" in Player.daily_history:
        $ Player.daily_history.remove("meet girl")

    call set_the_scene
    call clear_the_room (Girl)
    call Taboo_Level (1)

    if Girl.GirlLikeCheck(Other) >= 900:
        $ Resolution += 2
    elif Girl.GirlLikeCheck(Other) >= 800:
        $ Resolution += 1
    $ B = int((Girl.GirlLikeCheck(Other) - 500)/2)

    $ Resolution -= Girl.Cheated if Girl.Cheated <= 3 else 3

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
            $ Line = "sorry"
            $ Resolution += 1
        "What do you mean?":

            $ Girl.change_stat("love", 200, -10)
            $ Girl.change_stat("obedience", 80, 15)
            $ Girl.change_stat("inhibition", 80, 5)
            if Girl == StormX:
                ch_s "I am talking about you and [Other.name]. . ."
            else:
                Girl.voice "I mean you screwing around with [Other.name]!"
            menu:
                extend ""
                "Oh! I'm sorry!":
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("obedience", 80, -10)
                    $ Line = "sorry"
                "Oh, that. Yeah.":
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.change_stat("obedience", 80, 10)
                    $ Line = "yeah"
                    $ Resolution -= 1
        "You mean with [Other.name]?":

            $ Girl.change_stat("love", 200, -15)
            $ Girl.change_stat("obedience", 80, 20)
            $ Girl.change_stat("inhibition", 80, 10)
            Girl.voice "Yes, \"I mean with [Other.name].\""

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
            Girl.voice "[Line]"
            menu:
                extend ""
                "Oh! I'm sorry!":
                    $ Girl.change_stat("love", 90, 15)
                    $ Girl.change_stat("obedience", 80, -10)
                    $ Line = "sorry"
                "Oh, yeah.":
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.change_stat("obedience", 80, 10)
                    $ Line = "yeah"
                    $ Resolution -= 2

    if Line == "sorry":
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
                Girl.voice "Well at least you're owning up to it."
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
                if ApprovalCheck(Girl, 1500):
                    ch_l "Ok, that's fair."
                else:
                    ch_l "Do you want to try that one again?"
            elif Girl == JeanX:
                $ Girl.eyes = "side"
                $ Girl.change_stat("love", 80, 10)
                $ Resolution += 1
                ch_j "Oh. . . well. . ."
                $ Girl.change_face("angry",2)
                ch_j "That's not the point!"
                $ Girl.blushing = 1
            elif Girl == StormX:
                ch_s "Nothing serious to you, but what of me?"
            elif Girl == JubesX:
                ch_v "Oh, is that supposed to be an excuse?"
            $ Girl.change_stat("love", 200, -25)

            if not ApprovalCheck(Girl, 700, "O", Bonus = (B/3)):
                $ Resolution -= 2
        "I think she's really hot.":

            if B >= 100 or ApprovalCheck(Girl, 500, "I", Bonus = (B/3)):

                $ Girl.change_face("confused",Eyes="side")
                if Girl == StormX:
                    ch_s "She is certainly beautiful, but I do not see why that would be an excuse."
                elif Other == KittyX:
                    Girl.voice "Well. . . yeah, she is cute, but so what?"
                else:
                    Girl.voice "Well. . . yeah, she is hot, but so what?"
                $ Girl.change_stat("lust", 90, 5)
                $ Line = "threeway"
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
            if B >= 100 or ApprovalCheck(Girl,500,"I"):

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
                $ Line = "threeway"
            elif B >= 50 and Girl != JeanX:

                $ Girl.change_face("confused")
                $ Girl.change_stat("love", 200, -10)
                if Girl == EmmaX and Other != StormX:
                    ch_e "She's a good student, but that doesn't mean I'm interested in sharing."
                elif Girl == StormX:
                    ch_s "I like her well enough, but what difference does that make?"
                else:
                    Girl.voice "We're friends, but so what?"
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
                Girl.voice "Like the last time you told me that, you mean?"
                $ Resolution -= 1
            else:
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_face("angry")
                $ Resolution += 2 if Resolution < 3 else 0
                Girl.voice "I'll hold you to that."
            $ Line = 0
        "I can't make any promises, she's pretty hot.":

            $ Girl.change_face("angry")
            $ Girl.change_stat("love", 200, -40)
            $ Girl.change_stat("obedience", 90, 40)
            $ Girl.change_stat("inhibition", 90, 10)
            Girl.voice "Then I don't know what you tell you, I think we're through."
            $ Resolution -= 2
            $ Line = 0
        "Have you considered maybe letting her join us?":

            $ Girl.change_face("confused",Mouth="smile")
            if ApprovalCheck(Girl, 2200, Bonus = B) or ApprovalCheck(Girl, 950, "L", Bonus = (B/3)):
                $ Girl.change_stat("inhibition", 90, 30)
                $ Girl.change_stat("lust", 89, 10)
                $ Resolution += 2
            elif ApprovalCheck(Girl, 1500, Bonus = B) or Girl.GirlLikeCheck(Other) >= 700:
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
            $ Line = "threeway"

    if Resolution >= 5 and Line == "threeway":
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
        Girl.voice "Maybe I could live with that, I'll talk to [Other.name]."

        $ Line = "poly"

    elif Resolution >= 5:
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
            Girl.voice "Perhaps [Other.name] and I could work something out."
        else:
            Girl.voice "Maybe me and [Other.name] can work something out."
        $ Line = "poly"

    elif Resolution >= 2:
        if Line == "threeway":

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
                ch_k "Too many times, [KittyX.player_petname]. . ."
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
                ch_r "You betrayed my trust, [RogueX.player_petname]."
                ch_r "Don't let it happen again."
            elif Girl == KittyX:
                ch_k "You hurt me here, [KittyX.player_petname]. . ."
                ch_k "Don't hurt me like this again."
            elif Girl == EmmaX:
                ch_e "I'll let you off with a warning this time, but don't let it happen again."
            elif Girl == LauraX:
                ch_l "You're on thin ice, bub."
            elif Girl == JeanX:
                ch_j "I'll let you off this time, but don't push it."
            elif Girl == StormX:
                ch_s "You have betrayed my trust, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "I don't like these games. . ."
    else:


        $ Girl.change_face("angry")
        if Line == "threeway":
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
                ch_r "Sorry, [RogueX.player_petname], this is the end."
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
                ch_r "I just don't think I can trust you anymore, [RogueX.player_petname]."
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
                ch_s "You have betrayed my trust, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "I don't like these games!"

        $ Girl.AddWord(1,0,0,"ex",0)
        if Girl in Player.Harem:
            $ Player.Harem.remove(Girl)
        $ Girl.AddWord(1,0,"angry",0,0)



    $ BO = all_Girls[:]
    while BO:

        $ Girl.DrainWord("saw with "+BO[0].Tag,0,0,1)
        $ BO.remove(BO[0])

    if Line == "poly":
        $ Girl.AddWord(1,0,0,"poly "+Other.Tag,0)
        $ Girl.AddWord(1,0,0,"ask "+Other.Tag,0)
    else:
        $ Girl.GLG(Other,1000,-50,1)

    if "ex" in Girl.Traits:
        $ Girl.Break[0] = 5 + Girl.Break[1] + Girl.Cheated
    $ Girl.Cheated += 1


    menu:
        "I'm glad we could work this out." if Girl in Player.Harem:
            $ Girl.change_face("sad")
            if Resolution >= 3:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("obedience", 90, 5)
                if Girl == RogueX:
                    ch_r "I am too, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Me too, [KittyX.player_petname]. . ."
            else:
                $ Girl.change_stat("love", 90, 5)
                if Girl == RogueX:
                    ch_r "Yeah, we'll see, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sure, [KittyX.player_petname]. . ."
            if Girl == EmmaX:
                ch_e "Yes, delightful."
            elif Girl == LauraX:
                ch_l "Yeah, sure."
            elif Girl == JeanX:
                ch_j "Right, sure."
            elif Girl == StormX:
                ch_s "We shall see if I made the correct decision, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Yeah, maybe. . ."

        "Want to fool around a bit?" if Girl in Player.Harem and not Taboo:
            if Girl.obedience + Girl.inhibition >= (1.5*Girl.love) or Girl.lust >= 70:

                $ Girl.change_face("sly",Eyes="side")
                $ Girl.change_stat("love", 90, 20)
                $ Girl.change_stat("obedience", 90, 10)
                $ Girl.change_stat("inhibition", 90, 10)
                if Girl == StormX:
                    ch_s "You are incorrigible, [StormX.player_petname]."
                else:
                    Girl.voice "Sure, whatever."
                call expression Girl.Tag + "_SMenu"
            else:
                $ Girl.change_face("sad")
                $ Girl.change_stat("love", 90, -10)
                $ Girl.change_stat("obedience", 90, -10)
                if Girl == RogueX:
                    ch_r "It's still too raw, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Don't even, [KittyX.player_petname]. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, this is rich."
                elif Girl == LauraX:
                    ch_l "Yeah, not now."
                elif Girl == JeanX:
                    ch_j "Maybe later."
                elif Girl == StormX:
                    ch_s "Take some time to reflect on your actions, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Don't even with me right now. . ."

        "I'm sorry it didn't work out." if Girl not in Player.Harem:
            $ Girl.change_face("sad")
            $ Girl.change_stat("love", 90, 10)
            if Girl == RogueX:
                ch_r "I am too, [RogueX.player_petname]."
            elif Girl == KittyX:
                ch_k "Yeah, me too, [KittyX.player_petname]. . ."
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
            if Girl.obedience + Girl.inhibition >= (1.5*Girl.love) or Girl.lust >= 70:

                $ Girl.change_face("angry",Eyes="side")
                $ Girl.change_stat("obedience", 90, 10)
                $ Girl.change_stat("inhibition", 90, 10)
                if Girl == StormX:
                    ch_s "You are incorrigible, [StormX.player_petname]."
                else:
                    Girl.voice "Sure, whatever."
                $ Girl.DrainWord("angry",0,1)
                call expression Girl.Tag + "_SMenu"
                $ Girl.AddWord(1,0,"angry",0,0)
            else:
                $ Girl.change_face("angry")
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 90, -10)
                if Girl == RogueX:
                    ch_r "You have got to be kidding me."
                elif Girl == KittyX:
                    ch_k "Don't even, [KittyX.player_petname]. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, this is rich."
                elif Girl == LauraX:
                    ch_l "Yeah, not now."
                elif Girl == JeanX:
                    ch_j "Maybe later."
                elif Girl == StormX:
                    ch_s "Take some time to reflect on your actions, [StormX.player_petname]."
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
                ch_s "I am sure that I will, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Sure, whatever. . ."
        "Ok, see you later then.":

            $ Girl.change_face("confused")

    if Girl == RogueX:
        ch_r "I need some time alone, [RogueX.player_petname]. I'll see you later."
    elif Girl == KittyX:
        ch_k "I need some \"me\" time, I'll see you around."
    elif Girl == EmmaX:
        ch_e "Now, I need to be alone for a bit."
    elif Girl == LauraX:
        ch_l "Ok, well, bye."
    elif Girl == StormX:
        ch_s "I'm sure that I will see you later, [StormX.player_petname]."
    elif Girl == JubesX:
        ch_v "I'm gonna. . . get out of here. . ."

    $ Round -= 10 if Round > 10 else Round

    if bg_current == Girl.home:

        $ bg_current = "bg_player"
        jump Misplaced
    else:
        call Remove_Girl (Girl)
    return







label NoFap(Girl=0, TabStore=Taboo, counter=0):



    $ Taboo = 0
    ch_p "About when you masturbate on your own time. . ."

    if "askedfap" in Girl.daily_history:

        if "nofap" in Girl.Traits:
            Girl.voice "I understand already."
        else:
            Girl.voice "Stop bothering me with this."

    elif "askedfap" in Girl.history:

        if not ApprovalCheck(Girl, 800):

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
                ch_s "This really is none of your business, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "You, um, need to stop asking. . ."
            $ Girl.change_face("angry",1)
        else:

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
                ch_s "Oh, what is it, [StormX.player_petname]?"
            else:
                $ Girl.change_face("confused",2)
                Girl.voice "Um, yeah, what about it?"
    else:


        if not ApprovalCheck(Girl, 800):

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
                ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Do I. . ."
                ch_v "What? What business is that of yours?!"
            $ Girl.change_face("angry",1)
        elif not ApprovalCheck(Girl, 500, "I"):

            $ Girl.change_stat("love", 90, -5)
            $ Girl.change_stat("obedience", 50, 3)
            $ Girl.change_stat("obedience", 80, 1)
            $ Girl.change_stat("inhibition", 30, -1)
            $ Girl.change_stat("inhibition", 30, 3, 1)
            $ Girl.change_stat("lust", 50, 3)
            if Girl == RogueX:
                $ Girl.change_face("surprised",2)
                ch_r "I. . um. . I don't really do that. . ."
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
                ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Do I. . ."
                ch_v "What? Um. . . I don't wanna talk about it."
        elif ApprovalCheck(Girl, 500, "O"):

            $ Girl.change_stat("obedience", 90, 5)
            $ Girl.change_stat("inhibition", 50, 2)
            $ Girl.change_stat("inhibition", 80, 1)
            $ Girl.change_stat("lust", 50, 5)
            $ Girl.change_face("confused",1)
            if Girl == EmmaX:
                ch_e "What of it?"
            else:
                Girl.voice "What about it?"
        else:

            $ Girl.change_stat("obedience", 90, 4)
            $ Girl.change_stat("inhibition", 90, 3)
            $ Girl.change_stat("lust", 50, 3)
            $ Girl.change_face("confused",1)
            if Girl == EmmaX:
                ch_e "Oh? What about it?"
            elif Girl in (LauraX,JeanX):
                Girl.voice "Yeah?"
            elif Girl == StormX:
                ch_s ". . ."
                ch_s "What did you want to know?"
            else:
                $ Girl.change_face("confused",2)
                Girl.voice "Um, yeah, what about it?"


    menu:
        extend ""
        "I'd rather you not do that." if "nofap" not in Girl.Traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("obedience", 200, 2)
                $ Girl.change_stat("inhibition", 90, 1)
            if ApprovalCheck(Girl, 1400, "LO"):

                if "askedfap" not in Girl.history:
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
                    ch_e "[EmmaX.player_petname], the idea of it really bothers you?"
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
                    ch_s "If you truly believe you can take over my needs, [StormX.player_petname]. . ."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I do have needs. . ."
                    ch_v "You would need to make sure they get. . . taken care of."
                $ Girl.change_face("bemused",1)
            elif ApprovalCheck(Girl, 1600) and not ApprovalCheck(Girl, 500, "I") and Girl != JeanX:

                if "askedfap" not in Girl.history:
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
                    ch_s "I am not really sure what business that is of yours, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I don't really. . ."
                    ch_v "Ok, we'll see. . ."
                $ Girl.change_face("bemused",1)
            elif ApprovalCheck(Girl, 700, "O",Alt=[[JeanX],800]):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 70, 5)
                $ Girl.change_face("sly",1)
                Girl.voice "Yes,[Girl.player_petname]."
            elif not ApprovalCheck(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 90, -3)
                    $ Girl.change_stat("inhibition", 90, 3)
                $ Girl.change_face("angry",2)
                if Girl == KittyX:
                    ch_k "I- this whole conversation is inappropriate!"
                elif Girl in (EmmaX,JeanX):
                    Girl.voice "I really don't care what \"you'd rather.\""
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am uninterested in your opinions on this, [StormX.player_petname]."
                else:
                    Girl.voice "I'd rather you stay out my business."
                $ Girl.change_face("angry",1)
                $ counter = 1
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -1)
                    $ Girl.change_stat("obedience", 70, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_face("sly",1)
                if Girl == RogueX:
                    ch_r "'Fraid not, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sorry, no. I try to keep busy."
                elif Girl == EmmaX:
                    ch_e "No, I think I shall. . . often."
                elif Girl == LauraX:
                    ch_l "Sorry, [LauraX.player_petname], I've got needs."
                elif Girl == JeanX:
                    $ Girl.change_face("confused",1)
                    ch_j "Um. . . no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Um, that would be very inconvenient for me, so. . ."
                    ch_v "No."
                $ counter = 1
            if not counter:
                $ Girl.AddWord(1,0,0,"nofap")


        "Don't do that without permission." if "nofap" not in Girl.Traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("obedience", 200, 3)
            if ApprovalCheck(Girl, 600, "O"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("obedience", 200, 4)
                    $ Girl.change_stat("inhibition", 90, 5)
                    $ Girl.change_stat("lust", 50, 5)
                    $ Girl.change_stat("lust", 70, 5)
                $ Girl.change_face("sly")
                Girl.voice "Yes,[Girl.player_petname]."
            elif ApprovalCheck(Girl, 1200, "LO"):

                if "askedfap" not in Girl.history:
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
                    ch_s "Well, I could give that a try, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I do have needs. . ."
                    ch_v "You would need to make sure they get. . . taken care of."
            elif not ApprovalCheck(Girl, 500, "I"):

                if "askedfap" not in Girl.history:
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
                    ch_s "Do not take this tone with me, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Um, I don't know about that. . ."
                $ Girl.change_face("normal",1)
                $ counter = 1
            elif not ApprovalCheck(Girl, 800):

                if "askedfap" not in Girl.history:
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
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Rude. . ."
                $ Girl.change_face("angry",1)
                $ counter = 1
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, -2)
                    $ Girl.change_stat("obedience", 70, -2)
                    $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_face("bemused",2)
                if Girl == RogueX:
                    ch_r "'Fraid not, [RogueX.player_petname]."
                elif Girl == KittyX:
                    ch_k "Sorry, no. I try to keep busy."
                elif Girl == EmmaX:
                    ch_e "No, I think I shall. . . often."
                elif Girl == LauraX:
                    ch_l "Sorry, [LauraX.player_petname], I've got needs."
                elif Girl == JeanX:
                    $ Girl.change_face("confused",1)
                    ch_j "Um. . . no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would rather we not discuss this, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'm gonna do. . . whatever."
                $ Girl.change_face("bemused",1)
                $ counter = 1
            if not counter:
                $ Girl.AddWord(1,0,0,"nofap")


        "You can do that if you need to." if "nofap" in Girl.Traits:
            if "askedfap" not in Girl.daily_history:
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("obedience", 90, 1)
                $ Girl.change_stat("inhibition", 90, 1)
            if not ApprovalCheck(Girl, 500, "I"):

                if "okfap" not in Girl.history:
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
            elif ApprovalCheck(Girl, 750, "O"):

                if "okfap" not in Girl.history:
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("obedience", 200, 5)
                    $ Girl.change_stat("obedience", 90, 10)
                    $ Girl.change_stat("inhibition", 90, 10)
                    $ Girl.change_stat("lust", 90, 10)
                $ Girl.change_face("sly",1)
                Girl.voice "Yes,[Girl.player_petname]."
            else:

                if "okfap" not in Girl.history:
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
                    ch_s "That would be fantastic, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Oh. . . oh! Nice!"
                $ Girl.change_face("smile",1)
            $ Girl.DrainWord("nofap",0,0,1)
            $ Girl.AddWord(1,0,0,0,"okfap")
        "Nevermind":




            if not ApprovalCheck(Girl, 500, "I"):

                if "askedfap" not in Girl.history:
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
                else:
                    $ Girl.change_face("surprised",2)
                    Girl.voice "Right! What were we even talking about?"
                    $ Girl.change_face("smile",1)
            elif ApprovalCheck(Girl, 500, "O"):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 60, 5)
                    $ Girl.change_stat("inhibition", 80, 5)
                    $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("sly",1)
                if Girl in (EmmaX, StormX):
                    Girl.voice "Very Well. . ."
                else:
                    Girl.voice "Ok."
            elif not ApprovalCheck(Girl, 800):

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("love", 80, 5)
                    $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_face("angry",2,Eyes="side")
                if Girl == RogueX:
                    ch_r "Damned straight, \"never mind.\""
                elif Girl == EmmaX:
                    ch_e "I should hope so . . ."
                elif Girl == StormX:
                    ch_s "Of course."
                else:
                    Girl.voice "Damned right, \"never mind.\""
                $ Girl.change_face("angry",1)
            else:

                if "askedfap" not in Girl.history:
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_face("sly",1)
                if Girl in (EmmaX,StormX):
                    Girl.voice "Very Well. . ."
                else:
                    Girl.voice "Ok."


    $ Girl.AddWord(1,0,"askedfap",0,"askedfap")
    $ Taboo = TabStore
    return






label CalltoFap(Girl=0, Fap=0):



    if "nofap" not in Girl.Traits:

        $ Girl.DrainWord("wannafap",0,1)
        $ Girl.AddWord(1,0,"gonnafap",0,0)
        return

    if Girl.location == bg_current:

        return


    $ EGirls.remove(EGirls[0])
    while EGirls:

        if "wannafap" in EGirls[0].daily_history and "nofap" not in EGirls[0].daily_history:

            $ EGirls[0].AddWord(1,0,"gonnafap",0,0)
        $ EGirls.remove(EGirls[0])


    $ Player.daily_history.append("fapcall")


    show Cellphone at sprite_location(stage_left)

    "[Girl.name] calls you up. . ."
    if Girl == RogueX:
        ch_r "So. . . I was wondering. . ."
        ch_r "I know you didn't want me to. . . um. . . "
        ch_r "take care of my needs?"
        ch_r ". . ."
        ch_r ". . .but would you mind if I were to do that?"
        ch_r "Right now?"
    elif Girl == KittyX:
        ch_k "Hey, so[KittyX.like]I know you were all like. . ."
        ch_k "\"don't touch yourself, Kitty,\" and[KittyX.like],"
        ch_k "I know I agreed and all, but. . ."
        ch_k "Would you mind if[KittyX.like]maybe I did anyway?"
    elif Girl == EmmaX:
        ch_e "I'm aware that we had something of an arrangement going on. . ."
        ch_e "One relating to me. . . gratifying myself. . ."
        ch_e "or the lack thereof. . ."
        ch_e "And I was just curious, would you mind if we perhaps suspended that rule. . ."
        ch_e "Just for tonight, perhaps?"
    elif Girl == LauraX:
        ch_l "Hey, remember when you told me I couldn't schlick off?"
        ch_l "I want to schlick off."
        ch_l ". . ."
        ch_l "That cool? or. . ."
    elif Girl == JeanX:
        ch_j "Hey [JeanX.player_petname]. . ."
        ch_j "Remember how we agreed that I would hold off on. . ."
        ch_j ". . . on schlicking?"
        ch_j "Well I was just thinking. . ."
        ch_j "Maybe I could anyway?"
    elif Girl == StormX:
        ch_s "[StormX.player_petname]. . ."
        ch_s "I find myself in need of some. . . relief."
        ch_s "Would you mind if I were to satisfy myself?"
    elif Girl == JubesX:
        ch_v "Hey, remember how you told me I couldn't. . ."
        ch_v ". . . \"take care of my own needs?\""
        ch_v "Well. . . I have needs."
        ch_v "A whole lotta needs. . ."
        ch_v "So I was kinda hoping. . ."

    menu:
        "Sure, no problem.":
            $ Girl.change_stat("love", 90, 5)
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 80, 2)
            $ Girl.change_stat("inhibition", 80, 3)
            $ Girl.change_stat("lust", 50, 5)
            if Girl == RogueX:
                ch_r "Thanks, I really appreciate that."
            elif Girl == KittyX:
                ch_k "Cool!"
            elif Girl == EmmaX:
                ch_e "Oh, thank you, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "Nice."
            elif Girl == JeanX:
                ch_j "Whew!"
            elif Girl == StormX:
                ch_s ". . . Thank you, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "Nice. . ."
            $ Fap = 1
        "If you really have to. . .":
            if (Girl.love + Girl.obedience) >= 2*Girl.inhibition:

                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("obedience", 60, 3)
                $ Girl.change_stat("obedience", 80, 1)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Oh, well. . ."
                    ch_r "I suppose I could restrain myself. . ."
                elif Girl == KittyX:
                    ch_k "Well, if it really bothers you. . ."
                elif Girl == EmmaX:
                    ch_e "I imagine I can find other distractions, [EmmaX.player_petname]."
                elif Girl == LauraX:
                    ch_l "Hmm. Yeah, whatever. Nevermind."
                elif Girl == JeanX:
                    ch_j "Well, I guess I could hold off. . ."
                    ch_j "I do have -exceptional- self control. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I suppose I can contain myself, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Well, I mean. . ."
                    ch_v "I don't want to disappoint you. . ."
                $ Girl.Thirst += 10
            else:


                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("love", 200, 1)
                $ Girl.change_stat("obedience", 50, -4)
                $ Girl.change_stat("obedience", 90, -1)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_stat("inhibition", 80, 5)
                $ Girl.change_stat("lust", 50, 5)
                if Girl == RogueX:
                    ch_r "I would REALLY appreciate that."
                    ch_r "Thank you."
                elif Girl == KittyX:
                    ch_k "I kinda. . . yeah."
                elif Girl == EmmaX:
                    ch_e "It would really just take the edge off of a long day."
                elif Girl == LauraX:
                    ch_l "Yeah, I probably do."
                elif Girl == JeanX:
                    ch_j "K', thanks!"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "That is appreciated, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Nice. . ."
                $ Fap = 1
        "No, you may not.":
            if ApprovalCheck(Girl,600,"O") and (Girl.obedience >= Girl.inhibition):

                $ Girl.change_stat("love", 50, -5)
                $ Girl.change_stat("obedience", 60, 5)
                $ Girl.change_stat("obedience", 200, 2)
                $ Girl.change_stat("lust", 80, 5)
                if ApprovalCheck(Girl,800,"O"):
                    $ Girl.change_stat("lust", 200, 5)
                if Girl == RogueX:
                    ch_r "Oh, well. . ."
                    ch_r "I suppose I could restrain myself. . ."
                elif Girl == KittyX:
                    ch_k "Well, if it really bothers you. . ."
                elif Girl == EmmaX:
                    ch_e "I imagine I can find other distractions, [EmmaX.player_petname]."
                elif Girl == LauraX:
                    ch_l "Hmm. Yeah, whatever. Nevermind."
                elif Girl == JeanX:
                    ch_j ". . ."
                    ch_j ". . . . . ."
                    ch_j "Ok."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Fine."
                elif Girl == JubesX:
                    ch_v "Well. . . Ok. . ."
                $ Girl.Thirst += 10
            elif ApprovalCheck(Girl,1000,"LO"):

                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 50, -3)
                $ Girl.change_stat("obedience", 80, -2)
                $ Girl.change_stat("inhibition", 50, 3)
                $ Girl.change_stat("inhibition", 80, 2)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Well, I mean, I kind of started. . ."
                elif Girl == KittyX:
                    ch_k "Um, sorry, but I[KittyX.like]have to?"
                elif Girl == EmmaX:
                    ch_e "I think I'll just have to do it anyway. . ."
                elif Girl == LauraX:
                    ch_l "Um, sure, I will -NOT- be doing just that. . ."
                elif Girl == JeanX:
                    ch_j "Well. . . as it turns out. . ."
                    ch_j "\"Ask for forgiveness,\" you know?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am afraid that I have my limits, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'm a little wired right now. . ."
                $ Girl.Thirst += 10
                $ Fap = 1
            else:

                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 80, -5)
                $ Girl.change_stat("inhibition", 50, 4)
                $ Girl.change_stat("inhibition", 80, 3)
                if Girl == RogueX:
                    ch_r "You know what? Screw it, and screw you!"
                elif Girl == KittyX:
                    ch_k "Well. . . I'm doing it anyway!"
                elif Girl == EmmaX:
                    ch_e "I think I can be the judge of that."
                elif Girl == LauraX:
                    ch_l "Sure, keep thinking I care."
                elif Girl == JeanX:
                    ch_j "Fine!"
                    ch_j "You can just imagine what I'm *not* doing right now."
                    $ Girl.change_face("angry",Mouth="smirk")
                    call PsychicFlash (0)
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "Well, that is unfortunate, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I kinda need some release here though. . ."
                $ Girl.Thirst += 10
                $ Fap = 1
        "I could come over and take care of that. . .":
            $ Girl.change_stat("love", 80, 4)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 80, 2)
            $ Girl.change_stat("inhibition", 80, 2)
            $ Girl.change_stat("lust", 80, 5)
            if Girl == EmmaX:
                ch_e "I think you could at that, [EmmaX.player_petname]."
            elif Girl == LauraX:
                ch_l "Cool."
            elif Girl == StormX:
                ch_s "I imagine that you could, [StormX.player_petname]."
            elif Girl == JubesX:
                ch_v "That might be nice."
            else:
                Girl.voice "Oh, you would, would you. . ."
            $ Fap = 3
        "Only if I can watch." if AloneCheck():
            if ApprovalCheck(Girl, 1200):

                $ Girl.change_stat("love", 80, 4)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 50, 2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_stat("lust", 80, 5)
                if Girl == RogueX:
                    ch_r "Hmm. . . that sounds like fun. . ."
                elif Girl == KittyX:
                    ch_k "Heh, you looking for a show? . ."
                elif Girl == EmmaX:
                    ch_e "I think we could arrange that. . ."
                elif Girl == LauraX:
                    ch_l "Yeah, I could do that, gimme a sec. . ."
                elif Girl == JeanX:
                    ch_j "Ok, fair. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I would not mind that, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "Oh, well, I guess that'd be fine. . ."
                $ Fap = 2
            else:

                $ Girl.change_stat("love", 60, -3)
                $ Girl.change_stat("obedience", 60, -2)
                $ Girl.change_stat("inhibition", 80, 3)
                $ Girl.change_stat("lust", 50, 5)
                if Girl == RogueX:
                    ch_r "I, um, I don't know about that. . ."
                elif Girl == KittyX:
                    ch_k "Heh, heh, um, I don't think I could. . ."
                elif Girl == EmmaX:
                    ch_e "I'd rather avoid putting on a show like that. . ."
                elif Girl == LauraX:
                    ch_l "Nah, had enough of surveillance . . ."
                elif Girl == JeanX:
                    ch_j "Um, no?"
                elif Girl == StormX:
                    ch_s ". . ."
                    ch_s "I am uncomfortable with that, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "I'd uh, prefer you didn't. . ."
                $ Girl.Thirst += 15

    $ Girl.DrainWord("wannafap",0,1)
    hide Cellphone

    if Fap == 3:

        $ del Options[:]

        $ Girl.location = Girl.home
        $ bg_current = Girl.home
        call Taboo_Level (1)

        jump Misplaced

    elif Fap == 2:

        $ del Options[:]
        if Girl in (EmmaX,StormX) and Girl.location == "bg_classroom" and time_index >= 2:
            pass
        else:
            $ Girl.location = Girl.home
        call Taboo_Level (0)
        call PhoneSex (Girl)
        $ renpy.pop_call()
    elif Fap:

        $ Girl.AddWord(1,0,"gonnafap",0,0)

    $ Options = ["empty"]
    return







label PhoneSex(Girl=0):


    if bg_current != "bg_player":
        "You rush back to your room."
        $ bg_current = "bg_player"
        call Taboo_Level
        call set_the_scene
    if Girl in (EmmaX,JeanX):

        call MindFuck

    $ Player.AddWord(1,"phonesex","phonesex",0,"phonesex")


    call shift_focus (Girl)
    show PhoneSex zorder 150

    $ Girl.AddWord(1,"phonesex","phonesex",0,"phonesex")
    $ primary_action = 1
    if Girl == RogueX:
        ch_r "Ok, I think that should get the video running, right?"
        call Rogue_M_Prep
        ch_r "Hmm, that was a satisfying phone call. . ."
        ch_r "I gotta go."
    elif Girl == KittyX:
        ch_k "Ok, that's got it up."
        ch_k "[KittyX.Like]how do I look?"
        call Kitty_M_Prep
        ch_k "Mmmmm. . . call any time, [KittyX.player_petname]."
        ch_k "[KittyX.Like]ANY time."
    elif Girl == EmmaX:
        ch_e "Now, set it up like so. . ."
        ch_e "There, you should have video up."
        call Emma_M_Prep
        ch_e "I do enjoy these little chats. . ."
        ch_e "I need to be going though."
    elif Girl == LauraX:
        ch_l "Ok, video up. . ."
        call Laura_M_Prep
        ch_l "That was fun. Call you later?"
    elif Girl == JeanX:
        ch_j "Ooookay. . . There, video on. . ."
        call Jean_M_Prep
        ch_j "Ok, later."
    elif Girl == StormX:
        ch_s ". . ."
        ch_s "I believe I've got the camera set up, [StormX.player_petname]. . ."
        call Storm_M_Prep
        ch_s "I enjoyed that, thank you. . ."
    elif Girl == JubesX:
        ch_v "Ok, loaded up. . ."
        ch_v "Looking good?"
        call Jubes_M_Prep
        ch_v "Mmmmm. . . call again, [JubesX.player_petname]."
        ch_v "I'll be waiting. . ."


    hide PhoneSex

    call Get_Dressed
    $ Girl.change_outfit(5)
    call Checkout (1)
    $ Player.recent_history.remove("phonesex")
    return




label MindFuck_Screen:

    if bg_current in PersonalRooms:
        call RoomMask




















    elif bg_current == "bg_classroom":
        show bg_classmask onlayer black:
            alpha .2
    elif bg_current == "bg_dangerroom":
        show bg_danger onlayer black:
            alpha .2
    elif bg_current == "bg_showerroom":
        show bg_shower onlayer black:
            alpha .2
    elif bg_current == "bg_study":
        show bg_study onlayer black:
            alpha .2
    elif bg_current == "bg_movies":
        show bg_movies onlayer black:
            alpha .2
    elif bg_current == "bg_restaurant":
        show bg_rest onlayer black:
            alpha .2
    elif bg_current == "bg_pool":
        show bg_pool onlayer black:
            alpha .2
    else:
        show bg_campus onlayer black:
            alpha .2
    return

label PsychicFlash(Face="sly", TempLoc=0):
    call MindFuck_Screen
    $ Line = Girl.location
    $ Girl.location = bg_current
    call set_the_scene (1, 0, 0, 0, 1)
    if Face:
        $ Girl.change_face(Face)
    $ Girl.ArmPose = 2
    $ Girl.Uptop = 1
    $ Girl.Upskirt = 1
    $ Girl.underwearDown = 1
    ". . . {w=0.3}{nw}"
    if Girl == EmmaX:
        hide Emma_Sprite with fade
    elif Girl == JeanX:
        hide Jean_Sprite with fade
    $ Girl.change_outfit(6,Changed=1)
    scene onlayer black
    $ Girl.ArmPose = 1
    $ Line = 0
    Girl.voice ". . ."


label MindFuck(TempLoc=0):

    if Girl == EmmaX:
        ch_e "Would you prefer to have some telepathic sex?"
    elif Girl == JeanX:
        ch_j "Wouldn't telepathic sex be more fun?"
    menu MindFuck_Menu:
        "Sure":
            if Girl == EmmaX:
                ch_e "Lovely. . ."
                ch_e "Just let me prepare us. . ."
            elif Girl == JeanX:
                ch_j "Great!"
                ch_j "Ok, looping you in. . ."

            call MindFuck_Screen
            $ TempLoc = Girl.location
            $ Girl.location = bg_current
            $ Girl.change_face("sly")

            call set_the_scene (1, 0, 0, 0, 1)
            Girl.voice "There. . ."

            $ Player.AddWord(1,"MindFuck","MindFuck",0,"MindFuck")
            call expression Girl.Tag + "_SexMenu"

            $ Girl.location = TempLoc
            if Girl == EmmaX:
                ch_e "That'll be all for now. . ."
                ch_e "I'll see you in your dreams. . ."
            elif Girl == JeanX:
                ch_j "Ok, that'll do it. . ."
                ch_j "Be thinking about me. . ."

            $ Girl.change_outfit(6,Changed=1)
            $ Girl.Spunk = []
            if Girl == EmmaX:
                hide Emma_Sprite with fade
            elif Girl == JeanX:
                hide Jean_Sprite with fade
            scene onlayer black
            jump Misplaced
        "What is that?" if "mfuck?" not in Player.recent_history and "MindFuck" not in Player.history:
            if Girl == EmmaX:
                ch_e "Well, if you open your mind a bit, I could project into it."
                ch_e "Then we could have. . . all sorts of fun. . ."
            elif Girl == JeanX:
                ch_j "You know, like if you let your guards down a little. . ."
                ch_j "I could work my way in there and we could have some fun. . ."
            $ Player.AddWord(1,"mfuck?")
            jump MindFuck_Menu
        "Nah, over the phone is fine.":
            if Girl == EmmaX:
                ch_e "Fine, be boring. . ."
            elif Girl == JeanX:
                ch_j "Lame. . ."
            return
    return



label Frisky_Class(Girl=0, Teacher=0, LineB=0, BO=[]):
    if Girl not in all_Girls:
        return
    $ Partner = 0
    $ Line = 0

    if len(Present) >= 2:
        $ Present[1].sprite_location = stage_left
        $ Present[1].eyes = "side"
    $ Present[0].sprite_location = stage_right

    $ BO = active_Girls[:]

    while BO:

        if renpy.showing(BO[0].Tag+"_Sprite"):
            if BO[0] == RogueX:
                show Rogue_Sprite at sprite_location(RogueX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == KittyX:
                show Kitty_Sprite at sprite_location(KittyX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == LauraX:
                show Laura_Sprite at sprite_location(LauraX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == JeanX:
                show Jean_Sprite at sprite_location(JeanX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == JubesX:
                show Jubes_Sprite at sprite_location(JubesX.sprite_location,50):
                    ease .5 ypos 250
        $ BO.remove(BO[0])

    call shift_focus (Girl)
    if EmmaX.location == "bg_teacher":
        "[EmmaX.name] is giving a lecture on mutant relations. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."
        $ Teacher = EmmaX
    elif StormX.location == "bg_teacher":
        "[StormX.name] is giving a lecture on geography and politics. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."
        $ Teacher = StormX
    else:
        "Professor McCoy is giving a lecture on the X-Gene. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."
    "Occasionally, you catch her glancing over your way."

    "[Girl.name] opens her notebook and begins scratching out a note."
    "She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
    "She watches you as you unfold the note."
    if "friskyclass" in Girl.history:
        "It reads \"Did you want to fool around again? Y[[] N[[]\""
        menu:
            "Y":
                $ Girl.change_face("sly",1)
                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("inhibition", 60, 3)
                "She smiles suggestively."
                $ D20 = renpy.random.randint(1, 15)
                jump Frisky_Class_Loop
            "N":
                $ Girl.change_stat("love", 80, -10)
                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)
                $ Line = "rejected"
                $ Girl.change_face("angry")
                $ Girl.daily_history.append("angry")
                jump Frisky_Class_End
    if Girl == RogueX:
        "In looping penstrokes, it reads: \"You like biology?\""
    elif Girl == KittyX:
        "In girly penstrokes, it reads: \"biology?\""
    elif Girl == LauraX:
        "In roughly formed penstrokes, it reads: \"Boring, right?\""
    elif Girl == JeanX:
        "In sloppy penstrokes, it reads: \"kinda dull\"."
    elif Girl == JubesX:
        "In flashy penstrokes, it reads: \"Totally boring?\""
    if Girl in (RogueX,KittyX):
        $ Girl.change_face("smile",2)
        "You look back and see that she's blushing slightly."
        "She slides her pen over to you so you can reply."
        $ Girl.change_face("smile",1)
    else:
        $ Girl.change_face("sly",1)
        "You look back and see that she's staring at you suggestively."
        "She slides her pen over to you so you can reply."

    menu:
        "You reply. . ."
        "What are you talking about?":
            jump Frisky_Class_End
        "Naah. Not so much.":

            $ Girl.change_stat("love", 80, -3)
            $ Girl.change_stat("inhibition", 60, -3)
            $ Girl.change_face("confused")
            jump Frisky_Class_End

        "It's my favorite subject." if Girl in (RogueX,KittyX):
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_face("smile")
            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could study together tonight?\"."
            $ Line = "continue"

        "Yeah, pretty lame." if Girl not in (RogueX,KittyX):
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_face("smile")
            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could 'study' together tonight?\"."
            $ Line = "continue"

        "I do when it's about you." if Girl in (RogueX,KittyX):
            $ Line = "her"

        "I was too busy thinking about you." if Girl not in (RogueX,KittyX):
            $ Line = "her"



    if Line == "her":
        if ApprovalCheck(Girl, 500, "I") or Girl.SEXP >= 30:
            $ Girl.change_face("sly")
            "[Girl.name] reads your note and smiles at you suggestively."
            $ Line = "flirt"
        elif ApprovalCheck(Girl, 900):
            if Girl in (RogueX,KittyX):
                $ Girl.change_face("confused",2)
                "[Girl.name] reads your note and blushes furiously, looking down at her notes."
            else:
                $ Girl.change_face("sly",1)
                "[Girl.name] reads your note and gets a sly smile, looking down at her notes."
            $ Girl.change_face("bemused",1)
            $ Line = "flirt"
        else:

            if Girl in (RogueX,KittyX):
                $ Girl.change_face("perplexed",2)
                "[Girl.name] reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could study tonight?\"."
            else:
                $ Girl.change_face("sly",1)
                "[Girl.name] reads your note and gets a sly smile. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could 'study' tonight?\"."
            $ Girl.change_face("bemused",1)
            $ Line = "continue"


    if Line == "continue":
        "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."
        menu:
            "You respond. . ."
            "Maybe later.":
                $ Girl.change_stat("love", 80, -3)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)
                $ Girl.change_face("confused")
                $ Line = 0
                jump Frisky_Class_End
            "Naah. I've got better things to do.":
                $ Girl.change_stat("love", 80, -10)
                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)
                $ Line = "rejected"
                $ Girl.change_face("angry")
                $ Girl.daily_history.append("angry")
                jump Frisky_Class_End
            "Count on it.":
                $ Girl.change_face("smile")
                "She smiles when she reads your reply, and throws you a wink."
                $ Girl.daily_history.append("studydate")
                "The rest of class is uneventful."
                return
            "We could get some \"studying\" done right now.":
                if ApprovalCheck(Girl, 1000):
                    $ Girl.change_face("sly",1)
                    $ Girl.change_stat("love", 80, 3)
                    $ Girl.change_stat("inhibition", 60, 3)
                    "[Girl.name] gets a mischevious grin on her face and leans towards you."
                    $ Line = "flirt"
                elif ApprovalCheck(Girl, 700):
                    $ Girl.change_face("smile",1)
                    $ Girl.change_stat("inhibition", 60, 2)
                    if Girl in (RogueX,KittyX):
                        "[Girl.name] blushes and smiles your way."
                    else:
                        "[Girl.name] startles a bit and smiles your way."
                    $ Line = "flirt"
                else:
                    $ Girl.change_face("confused",1)
                    "[Girl.name] looks a bit surprised, then scowls at you."
                    jump Frisky_Class_End




    if Line == "flirt":
        $ Round -= 20
        $ D20 = renpy.random.randint(1, 15)
        $ Girl.change_face("sly")
        "You notice one of [Girl.name]'s shoes slip from her foot beneath the desk. She tosses you a sly grin."
        if Girl.hose:
            "You feel the smooth texture of her stockinged foot begin to slowly slide back and forth along the length of your calf."
        else:
            "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."

        while D20 <= 21 or "go on" in Player.recent_history:
            menu Frisky_Class_Loop:
                "Pull away from her.":
                    if Line == "fondle_pussy":
                        "You slowly slide your hand from her lap and start taking notes again."
                        $ Line = "tease"
                    elif Line == "fondle_breast":
                        "With a final squeeze, you move your hand back to the desktop."
                        $ Line = "tease"
                    elif Girl.session_orgasms and Girl.lust < 90:
                        "That'll probably do for now. . ."
                        $ Line = "tease"
                    else:
                        $ Line = "rejected"
                        $ Girl.change_stat("love", 200, -15)
                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 60, -2)
                    jump Frisky_Class_End

                "Look into her eyes and smile slightly." if Line == "flirt":
                    $ Girl.change_face("smile")
                    $ Girl.change_stat("love", 200, 5)
                    "[Girl.name] smiles back."
                    "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."
                    $ Line = "handholding"
                    jump Frisky_Class_Loop
                "Grasp her hand gently, stroking the top of it." if Line == "handholding":
                    $ Girl.change_stat("love", 200, 5)
                    $ Girl.change_stat("lust", 50, 5)
                    $ Girl.change_face("smile")
                    "[Girl.name] sighs contentedly and holds your hand for the remainder of class."
                    jump Frisky_Class_End


                "Try and slip your hand to her lap." if Line != "fondle_pussy":
                    $ Line = "fondle_pussy"
                    if ApprovalCheck(Girl, 1200) and Girl.action_counter["fondle_pussy"] and Girl.SEXP >= 40:
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 5)
                        "[Girl.name] gets a mischievous grin and places her hand on your arm."
                    elif ApprovalCheck(Girl, 1400) and Girl.action_counter["fondle_pussy"]:
                        $ Girl.change_face("smile")
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                    elif ApprovalCheck(Girl, 1500):
                        $ Girl.change_face("perplexed",2)
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] glances at you in alarm, but then slowly calms down."
                        $ Girl.change_face("smile",1)
                        $ D20 += 2
                    else:
                        $ Line = "too far"

                    if Line == "fondle_pussy":
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("lust", 94, 5)
                        if Girl.PantsNum() == 5:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak under the hem of her skirt, slowly tracing the soft contours of her mound."
                        elif Girl.PantsNum() >= 7:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak down her pants, slowly tracing the soft contours of her mound."
                        else:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound."

                        $ Girl.change_stat("lust", 94, 5)
                        if Girl.underwear == "shorts":
                            "You think her shorts are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.underwear:
                            "You think her panties are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.pubes:
                            "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        else:
                            "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        $ primary_action = "fondle_pussy"
                        $ D20 += 5

                "Keep fondling her pussy." if Line == "fondle_pussy":
                    $ Girl.change_stat("obedience", 70, 5)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_stat("lust", 89, 5)
                    $ Girl.change_stat("lust", 94, 5)
                    $ LineB = renpy.random.choice(["As the class drones on, you continue to slowly massage her warm delta.",
                                        "As the class continues, you continue to slowly massage her moist pussy.",
                                        "As the lecture drones on, you continue to slowly stroke her clit.",
                                        "As the class continues, you continue to slowly caress her labia."])
                    "[LineB]"

                    $ D20 += 5


                "Start fondling her tits." if Line != "fondle_breasts":
                    $ Line = "fondle_breasts"
                    if ApprovalCheck(Girl, 1100) and Girl.action_counter["fondle_breasts"]and Girl.SEXP >= 40:
                        $ Girl.change_stat("love", 80, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("sly")
                        "[Girl.name] closes her eyes and caresses your arm."
                    elif ApprovalCheck(Girl, 1300) and Girl.action_counter["fondle_breasts"]:
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("smile",1)
                        "[Girl.name] flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                    elif ApprovalCheck(Girl, 1400):
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("perplexed",2)
                        "[Girl.name] glances at you in alarm, but then slowly calms down."
                        $ Girl.change_face("smile",2)
                        $ D20 += 5
                    else:
                        $ Line = "too far"

                    if Line == "fondle_breasts":
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("lust", 94, 5)
                        "[Girl.name]'s sly eyes spakle as your hand cups her breast, giving it a casual caress."
                        "her nipples begin to firm up and she lets out a small moan of pleasure."
                        $ D20 += 7
                        $ primary_action = "fondle_breasts"
                "Keep fondling her tits." if Line == "fondle_breasts":
                    $ Girl.change_stat("obedience", 70, 5)
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_stat("lust", 95, 3)
                    "Barely paying attention to the lecture, you continue to pulse her breast in your palm."
                    $ D20 += 7


                "Try and pull her hand toward your lap." if not offhand_action and Player.semen:
                    if "handjob" in Girl.recent_history:
                        "[Girl.name] grins and her hand grasps your cock again."
                    elif ApprovalCheck(Girl, 1200) and Girl.action_counter["handjob"] and Girl.SEXP >= 40:
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 5)
                        "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."
                    elif ApprovalCheck(Girl, 1400) and Girl.action_counter["fondle_pussy"]:
                        $ Girl.change_face("smile")
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] starts slightly as your move her hand up your thigh, but then she lets out a slight grin."
                    elif ApprovalCheck(Girl, 1500):
                        $ Girl.change_face("perplexed",2)
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)
                        "[Girl.name] glances at you in alarm, but then slowly calms down."
                        $ Girl.change_face("smile",1)
                        $ D20 += 2
                    else:
                        $ Line = "too far"

                    if Line != "too far":

                        $ Girl.change_face("sly")
                        $ Girl.change_stat("lust", 94, 5)
                        if "cockout" not in Player.recent_history:
                            "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."
                            $ Player.AddWord(1,"cockout")
                            call Seen_First_Peen (Girl, Partner)
                            $ Girl.change_stat("lust", 94, 5)
                        $ offhand_action = "handjob"
                        $ Girl.recent_history.append("handjob")
                        $ Girl.daily_history.append("handjob")
                        "She begins to gently stroke it. . ."
                        if "handjob" not in Girl.recent_history:
                            $ Girl.action_counter["handjob"] += 1
                        $ D20 += 5


                "Stop her handjob." if offhand_action:
                    "You put a hand on her wrist and nudge her hand away."
                    if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.love+Girl.obedience) >= (2*Girl.inhibition):

                        $ Girl.change_face("sad")
                        $ Girl.change_stat("love", 90, -1)
                        $ Girl.change_stat("obedience", 60, 2)
                        $ Girl.change_stat("obedience", 80, 3)
                        "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."
                        $ Girl.change_face("sly")
                        $ offhand_action = 0
                    else:
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 80, -3)
                        $ Girl.change_stat("love", 90, -1)
                        $ Girl.change_stat("obedience", 70, -2)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_stat("inhibition", 80, 2)
                        "[Girl.name] grasps your cock tightly, then continues to stroke it when you let go."
                        $ Girl.change_face("sly")
                        $ D20 += 2





            if not offhand_action and Player.semen and "stophand" not in Girl.recent_history:
                if ApprovalCheck(Girl, 1200) and ApprovalCheck(Girl, 400, "I") and Girl.action_counter["handjob"] and Girl.SEXP >= 40:
                    $ Girl.change_face("sly")
                    "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."
                    menu:
                        "What do you do?"
                        "Let her":
                            "You smile and nod a little."
                            $ Girl.change_face("sly")
                            $ Girl.change_stat("love", 80, 1)
                            $ Girl.change_stat("inhibition", 70, 3)
                            $ Girl.change_stat("inhibition", 90, 2)
                            $ Girl.change_stat("lust", 94, 5)
                            if "cockout" not in Player.recent_history:
                                "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."
                                $ Player.AddWord(1,"cockout")
                                call Seen_First_Peen (Girl, Partner)
                                $ Girl.change_stat("lust", 94, 5)
                            $ offhand_action = "handjob"
                            $ Girl.recent_history.append("handjob")
                            $ Girl.daily_history.append("handjob")
                            "She begins to gently stroke it. . ."
                            if "handjob" not in Girl.recent_history:
                                $ Girl.action_counter["handjob"] += 1
                            $ D20 += 10
                        "Stop her":
                            "You put a hand on her wrist and nudge her hand away."
                            $ Girl.recent_history.append("stophand")
                            if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.love+Girl.obedience) >= (2*Girl.inhibition):

                                $ Girl.change_face("sad")
                                $ Girl.change_stat("love", 90, -1)
                                $ Girl.change_stat("obedience", 60, 2)
                                $ Girl.change_stat("obedience", 80, 3)
                                "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."
                                $ Girl.change_face("sly")
                                $ offhand_action = 0
                            else:
                                $ Girl.change_face("angry")
                                $ Girl.change_stat("love", 80, -3)
                                $ Girl.change_stat("love", 90, -1)
                                $ Girl.change_stat("obedience", 70, -2)
                                $ Girl.change_stat("inhibition", 60, 3)
                                $ Girl.change_stat("inhibition", 80, 2)
                                "[Girl.name] stops, but looks really annoyed."
                                $ D20 += 10


            if offhand_action:

                "[Girl.name]'s hand continues to caress your cock. . ."
                $ Player.focus += 15 if Player.focus < 60 else 10
                if Player.focus >= 100:

                    "As you start to reach your limits, [Girl.name] places a hand over your cock."
                    "You jiz all over her hand."
                    $ Player.semen -= 1
                    if (Girl.action_counter["blowjob"] and ApprovalCheck(Girl, 1200)) or Girl == JubesX:
                        "She quickly licks it all up."
                        $ Girl.addiction -= 20
                        $ Girl.event_counter["swallowed"] += 1
                        $ Girl.recent_history.append("swallow")
                        $ Girl.daily_history.append("swallow")
                    else:
                        "She quickly wipes her hand off under the desk."
                    $ Girl.change_stat("lust", 200, 5)
                    $ D20 += 10
                    if not Player.semen:
                        "She continues to lightly stroke you, but you don't seem up to it for now. . ."
                        $ offhand_action = 0
                $ D20 += 5



            if Girl.lust >= 95:
                $ LineB = Line
                call Girl_Cumming (Girl, 1)
                $ Line = LineB
                $ LineB = renpy.random.choice([Girl.name+" collapses over her desk.",
                                    Girl.name+" mumbles something unintelligible.",
                                    Girl.name+" bites her lip as she struggles to stay upright.",
                                    Girl.name+" seems a bit flushed."])
                "[LineB]"
                $ D20 += 15



            $ Round -= 7
            if Round <= 15:
                "Unfortunately it seems like class is wrapping up. You'll have to save this for later. . ."
                $ Line = "tease"
                jump Frisky_Class_End
            if Line == "too far":

                $ Girl.change_face("surprised",2)
                $ Girl.change_stat("love", 80, -5)
                $ Girl.change_stat("obedience", 70, 7)
                $ Girl.change_stat("inhibition", 50, -3)
                "[Girl.name] sits up straight in her seat and makes a little yelping noise."
                $ Girl.change_face("angry",1)
                "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."
                $ D20 += 20
                if "go on" in Player.recent_history:
                    jump Frisky_Class_End
                    $ Line = "caught"
            else:
                if len(Present) >= 2 and D20 >= 15:

                    if Partner:

                        $ Partner.GirlLikeUp(Girl,2)
                        $ Girl.GirlLikeUp(Partner,2)
                        $ Partner.change_stat("lust", 95, 3)
                        $ LineB = renpy.random.choice([0,
                                            0,
                                            0,
                                            Partner.name+" seems into it. . .",
                                            Partner.name+"'s hand moves a bit faster.",
                                            Partner.name+" bites her lip as her hand continues to move.",
                                            Partner.name+"'s hand slows down a bit."])
                        if LineB:
                            "[LineB]"
                        if Partner.lust >= 95:
                            $ LineB = Line
                            call Girl_Cumming (Partner, 1)
                            $ Line = LineB
                            $ LineB = renpy.random.choice([Partner.name+" collapses over her desk.",
                                                    Partner.name+" mumbles something unintelligible.",
                                                    Partner.name+" bites her lip as she struggles to stay upright.",
                                                    Partner.name+" seems a bit flushed."])
                            "[LineB]"
                            $ D20 += 15

                    elif "saw with "+ Girl.Tag in Present[1].Traits:
                        Present[1].voice "Well!"
                        $ Present[1].GirlLikeUp(Girl,-4)
                        $ Girl.GirlLikeUp(Present[1],-2)
                        call Remove_Girl (Present[1])
                    elif ApprovalCheck(Present[1], 1500) and Present[1].GirlLikeCheck(Girl) >= 600:

                        $ Present[1].eyes = "leftside"
                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."
                        $ Present[1].change_face("sly",1)
                        "She seems to be kinda into it. . ."
                        if ApprovalCheck(Present[1], 800, "I") or "exhibitionist" in Present[1].Traits:
                            $ Girl.change_stat("inhibition", 90, 3)
                            $ Present[1].GirlLikeUp(Girl,3)
                            $ Girl.GirlLikeUp(Present[1],5)
                            $ Present[1].change_stat("lust", 89, 7)
                            "You notice that [Present[1].name]'s begun feeling herself up as well."
                            $ Present[1].AddWord(1,"frisky","frisky",0,0)
                            $ Partner = Present[1]
                    else:


                        $ Present[1].eyes = "leftside"
                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."
                        $ Present[1].AddWord(1,0,0,"saw with " + Girl.Tag)
                        $ Present[1].change_face("angry",1)
                        if Present[1] == RogueX:
                            ch_r "How dare you! Hussy."
                        elif Present[1] == KittyX:
                            ch_k "Hey! . . . HEY!"
                        elif Present[1] == LauraX:
                            ch_l "Cool off, you two."
                        elif Present[1] == JeanX:
                            ch_j "Hey, cut it out."
                        $ Present[1].GirlLikeUp(Girl,-2)
                        $ Girl.GirlLikeUp(Present[1],-3)
                        $ D20 += 15
                        if "go on" in Player.recent_history:
                            $ Line = "caught"
                            jump Frisky_Class_End


                if Teacher and "frisky" in Teacher.recent_history:

                    $ Teacher.GirlLikeUp(Girl,2)
                    $ Girl.GirlLikeUp(Teacher,2)
                    $ Teacher.change_stat("lust", 95, 3)
                    $ LineB = renpy.random.choice([0,
                                    0,
                                    0,
                                    Teacher.name+" stumbles a bit over the delivery of the next portion of her lecture.",
                                    Teacher.name+"'s hand moves a bit faster.",
                                    Teacher.name+" bites her lip as her hand continues to move.",
                                    Teacher.name+"'s hand slows down a bit."])
                    if LineB:
                        "[LineB]"
                    if Teacherlust >= 95:
                        $ LineB = Line
                        call Girl_Cumming (Teacher, 1)
                        $ Line = LineB
                        $ LineB = renpy.random.choice([Teacher.name+" stumbles a bit over the delivery of the next portion of her lecture.",
                                            Teacher.name+" mumbles something unintelligible but continues the lecture.",
                                            Teacher.name+" bites her lip as she struggles to continue talking.",
                                            Teacher.name+" seems a bit under the weather.",
                                            Teacher.name+" seems a bit flushed."])
                        "[LineB]"
                        $ D20 += 15

                if D20 > 30:

                    if D20 >= 50:
                        $ LineB = renpy.random.choice([0,
                                        0,
                                        0,
                                        "The class isn't paying attention to the lecture anymore.",
                                        "The class definitely seems into the show she's putting on.",
                                        "The class is hooting and hollering.",
                                        "The students seem to be watching you intently."])
                    else:
                        $ LineB = renpy.random.choice([0,
                                        0,
                                        0,
                                        "The class seems a little confused as to what she's talking about.",
                                        "The class seems a little confused as to what she's doing back there.",
                                        "The class is shifting strange looks your way.",
                                        "A bunch of students seem to be watching you intently."])
                    if LineB:
                        "[LineB]"



        if "exhibitionist" not in Girl.Traits and not ApprovalCheck(Girl, 700,"I"):

            $ Line = "too far"
        if Line not in ("rejected", "handholding", "tease"):
            $ Girl.change_face("surprised")
            if Teacher:
                $ Teacher.change_face("surprised",1)
                "[Teacher.name] stops her lecture in mid-sentence when she notices what you and [Girl.name] are up to."
                if ApprovalCheck(Teacher, 1500) and Teacher.GirlLikeCheck(Girl) >= 600:

                    $ Teacher.change_face("sly",1)
                    if Line == "too far":

                        $ Girl.mouth = "sad"
                        if Teacher == EmmaX:
                            "She looks over at you and shrugs as she continues her lecture, but the moment has past."
                        elif Teacher == StormX:
                            "She looks over at you and smiles consolingly as she continues her lecture, but the moment has past."
                        jump Frisky_Class_End
                    "She gets a sly smile on her face and continues her lecture."
                    $ Girl.change_face("sly",1)
                    if ApprovalCheck(Teacher, 800, "I") or "exhibitionist" in Teacher.Traits:
                        $ Teacher.change_stat("inhibition", 90, 3)
                        $ Teacher.GirlLikeUp(Girl,3)
                        $ Girl.GirlLikeUp(Teacher,5)
                        $ Teacher.change_stat("lust", 89, 7)
                        "You notice that [Teacher.name]'s hand has snaked down beneath the podium and begun to move."
                        $ Teacher.AddWord(1,"frisky","frisky",0,0)
                        $ Player.AddWord(1,"go on","go on",0,0)
                    "[Girl.name] looks around and shrugs. . ."
                    jump Frisky_Class_Loop
                else:
                    $ Teacher.change_face("angry",1)
                    $ Girl.mouth = "sad"
                    if Teacher == EmmaX:
                        ch_e "[EmmaX.player_petname], [Girl.Tag], if you could perhaps pay more attention to the lecture, and less to each other's bodies?"
                        ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
                    elif Teacher == StormX:
                        ch_s "[StormX.player_petname], [Girl.Tag], I can appreciate your enthusaism, but perhaps not on my time?"
                        ch_s "I think perhaps you should visit Charles and cool off?"
            else:
                "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and [Girl.name]."
                ch_b "Oh, my stars and garters!"
                ch_b "[Player.name]!?! {b}WHAT ARE YOU DOING? BOTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"
            $ Girl.AddWord(1,0,0,0,"friskyclass")
            $ Line = 0
            $ Girl.change_stat("love", 80, -10)
            $ Girl.change_stat("obedience", 70, -5)
            $ Girl.change_stat("inhibition", 50, -10)
            $ primary_action = 0
            if Girl not in Rules:
                call Girls_Caught (Girl)
            else:
                "Since Xavier isn't concerned with your activities, you both head back to your room instead."
                $ Girl.location = "bg_player"
                call clear_the_room (Girl, 0, 1)
                jump Player_Room



label Frisky_Class_End:
    $ primary_action = 0
    $ Partner = 0
    if Teacher:
        $ Teacher.DrainWord("frisky",1,0)
    if not Line:

        $ Girl.change_face("confused")
        "She unfolds the note and quickly reads it over."
        $ Girl.change_face("sad")
        "As she does, you immediately see disappointment come over her features."
        "She scratches out a reply and slides it back in front of you."
        "When you open it up, it reads: {i}Never mind.{/i}"
    elif Line == "tease":

        if Girl.lust >= 80:
            $ Girl.change_face("surprised",2)
            "[Girl.name] startles briefly."
            $ Girl.change_face("sad",2)
            "[Girl.name] she looks over at you a bit upset that you ended things so abruptly."
        $ Girl.AddWord(1,0,0,0,"friskyclass")
        $ Girl.change_face("sly",1)
        "[Girl.name] takes in a deep breath and exhales it in a sigh, leaning in to whisper."
        if Girl == RogueX:
            ch_r "Tonight's \"study session\" just got a whole lot more interesting."
        elif Girl == KittyX:
            ch_k "I think we'll have[KittyX.like]a -lot- more fun tonight. . ."
        elif Girl == LauraX:
            ch_l "Tonight we can. . . finish this."
        elif Girl == JeanX:
            ch_j "I guess it can wait until later. . ."
        elif Girl == JubesX:
            ch_v "I'm looking forward to picking this up later. . ."
    elif Line == "rejected":

        if Girl in (RogueX,KittyX):
            $ Girl.change_face("sadside")
            "[Girl.name] looks surprised and hurt. For the rest of the class, she says nothing."
        else:
            $ Girl.change_face("angry")
            "[Girl.name] looks surprised and hurt. For the rest of the class, she stares daggers at you."
        "It seems like she has a hard time looking you in the eye."
    elif Line == "caught":
        "You quickly separate and go back to trying to study. . ."

    "Eventually, [Girl.name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."
    $ Line = 0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
