label sleepover:
    $ Player.Party = []

    python:
        for G in all_Girls:
            if G.location == Player.location:
                Player.Party.append(G)

    if not Player.Party and Player.location == "bg_player":
        call remove_all

        "It's getting late, so you go to sleep."

        if "met" in StormX.history and "met" not in JubesX.history and day >= 1:
            call meet_Jubes

        call wait

        return

    while len(Player.Party) > 2:
        $ Player.Party.remove(Player.Party[2])

    if Player.Party:
        call shift_focus(Player.Party[0])

    if Player.location != "bg_player":
        $ temp_Girls = all_Girls[:]

        while temp_Girls:
            if temp_Girls[0].home == Player.location:
                if temp_Girls[0] not in Player.Party:
                    "[temp_Girls[0].name] probably wouldn't appreciate you staying over, you head back to your own room."

                    call remove_all

                    jump return_player_to_room

                if temp_Girls[0] != Player.Party[0]:
                    $ Player.Party.reverse()

                $ temp_Girls = [None]

            $ temp_Girls.remove(temp_Girls[0])

    if Player.location == "bg_player":
        if len(Player.Party) == 2:
            $ renpy.random.shuffle(Player.Party)

            if approval_check(Player.Party[0],Check=1) <= approval_check(Player.Party[1],Check=1):
                $ Player.Party.reverse()

        if not Player.Party:
            pass
        elif Player.Party[0].event_counter["sleepover"] >= 3 and approval_check(Player.Party[0], 800):
            pass
        elif Player.Party[0] == RogueX:
            ch_r "It's getting late and I'm getting a bit tired."
        elif Player.Party[0] == KittyX:
            ch_k "It's late, I'm thinking of heading out. . ."
        elif Player.Party[0] == EmmaX:
            ch_e "It's late, I should be going. . ."
        elif Player.Party[0] == LauraX:
            ch_l "I need some sleep. . ."
        elif Player.Party[0] == JeanX:
            ch_j "I'm turning in. . ."
        elif Player.Party[0] == StormX:
            ch_s "It is getting late, I should be going. . ."
        elif Player.Party[0] == JubesX:
            ch_v "Well, it's pretty late, you should be getting some sleep. . ."
    elif Player.Party and Player.location == Player.Party[0].home:
        if Player.Party[0] == RogueX:
            ch_r "It's getting late and I'm turning in."
        elif Player.Party[0] == KittyX:
            ch_k "I'm getting kinda tired. . ."
        elif Player.Party[0] == EmmaX:
            ch_e "It's getting late, [EmmaX.player_petname]. . ."
        elif Player.Party[0] == LauraX:
            ch_l "I'm tired. . ."
        elif Player.Party[0] == JeanX:
            ch_j "I'm turning in. . ."
        elif Player.Party[0] == StormX:
            ch_s "It is getting late, I would like to get ready for bed. . ."
        elif Player.Party[0] == JubesX:
            ch_v "Well, it's pretty late, you should be getting some sleep. . ."
    else:
        "Something went wrong."
        "Tell Oni \"[Player.Party] - [Player.location]\""


    if day <= 4:

        jump return_player_to_room

    if EmmaX in Player.Party:
        if "classcaught" not in EmmaX.history:
            if Player.location == EmmaX.home:
                ch_e "You should probably get going, we wouldn't want any rumors to spread."
                jump return_player_to_room
            else:
                ch_e "I should probably get going, we wouldn't want any rumors to spread."
                call remove_Girl(EmmaX)
        elif len(Player.Party) >= 2 and "threesome" not in EmmaX.history:

            if (Player.location == EmmaX.home or Player.location == "bg_player") and approval_check(EmmaX, 1100, "LI"):
                if Player.Party[0] != EmmaX:
                    $ Player.Party.reverse()
                ch_e "[Player.Party[1].name] dear, I need a moment with [Player.name], but you can leave."
                $ Player.Party[1].change_face("_confused", 1)
                Player.Party[1].voice "Oh, ok. . ."
                call remove_Girl(Player.Party[1])
                ch_e "Sorry about that, but I had to discuss something with you in private."
            else:

                ch_e "Yes, I really should be leaving, don't let me bother you two."
                call remove_Girl(EmmaX)
            if "sleeptime" not in EmmaX.history:
                $ EmmaX.history.append("sleeptime")
        if not Player.Party or (EmmaX not in Player.Party and Player.location == EmmaX.home):

            jump return_player_to_room

    $ Player.Party[0].change_face("_sexy", 1)

    $ line = 0
    if Player.Party[0].event_counter["sleepover"] >= 3 and approval_check(Player.Party[0], 800):

        if Player.Party[0].home == Player.location:
            Player.Party[0].voice "Are you staying over tonight?"
        else:
            Player.Party[0].voice "I'm staying over, right?"
        $ line = 1

    elif Player.Party[0].event_counter["sleepover"] < 3 and approval_check(Player.Party[0], 1100, "LI"):

        $ Player.Party[0].change_face("_bemused", 1)
        if Player.Party[0] == RogueX:
            if Player.location == Player.Party[0].home:
                ch_r "I was thinking. . . maybe you wanted to stay the night?"
            else:
                ch_r "I was thinking. . . maybe I could stay the night?"
        elif Player.Party[0] == KittyX:
            if Player.location == Player.Party[0].home:
                ch_k "So[KittyX.like]did you want to stay over?"
            else:
                ch_k "So[KittyX.like]could I stay over?"
        elif Player.Party[0] == EmmaX:
            if Player.location == Player.Party[0].home:
                ch_e "I was wondering, have you considered staying over?"
            else:
                ch_e "I was wondering, could I stay over?"
        elif Player.Party[0] == LauraX:
            if Player.location == Player.Party[0].home:
                ch_l "So, are you staying over?"
            else:
                ch_l "So, can I stay here tonight?"
        elif Player.Party[0] == JeanX:
            if Player.location == Player.Party[0].home:
                ch_j "Were you planning to stay over?"
            else:
                ch_j "I'm crashing here, ok?"
        elif Player.Party[0] == StormX:
            if Player.location == Player.Party[0].home:
                ch_s "Did you want to stay the night?"
            else:
                ch_s "Would you mind if I sleep here tonight?"
        elif Player.Party[0] == JubesX:
            if Player.location == Player.Party[0].home:
                ch_v "Would you maybe wanna sleep here?"
            else:
                ch_v "Would you maybe want me to sleep here?"
        $ line = 1


    if line:

        menu:
            extend ""
            "Sure.":
                if Player.Party[0].event_counter["sleepover"] <= 5:
                    $ Player.Party[0].change_stat("love", 70, 10)
                    $ Player.Party[0].change_stat("obedience", 80, 10)
                    $ Player.Party[0].change_stat("obedience", 50, 20)
                    $ Player.Party[0].change_stat("inhibition", 25, 20)
                $ Player.Party[0].change_stat("love", 70, 5)
                $ Player.Party[0].change_face("_smile")
            "No, sorry.":


                $ Player.Party[0].change_stat("obedience", 50, 2)
                $ Player.Party[0].change_stat("obedience", 30, 5)
                $ Player.Party[0].change_stat("inhibition", 40, 3)
                $ Player.Party[0].change_face("_sad")
                $ line = 0
                if Player.Party[0] == RogueX:
                    ch_r "Ok, see you tomorrow then. 'Night."
                elif Player.Party[0] == KittyX:
                    ch_k "Alright. . . see you tomorrow. . ."
                elif Player.Party[0] == EmmaX:
                    ch_e "Well, if you insist. See you tomorrow then."
                elif Player.Party[0] == LauraX:
                    ch_l "Ok."
                elif Player.Party[0] == JeanX:
                    ch_j "Huh. Ok, whatever."
                elif Player.Party[0] == StormX:
                    ch_s "Very well, I will see you tomorrow then."
                elif Player.Party[0] == JubesX:
                    ch_v "Ok, cool, cool. . . later then. . ."
    else:

        if Player.Party[0] == RogueX:
            if Player.location == Player.Party[0].home:
                ch_r "You should get going."
            else:
                ch_r "I'm heading out, see you tomorrow."
        elif Player.Party[0] == KittyX:
            if Player.location == Player.Party[0].home:
                ch_k "You should[KittyX.like]head out."
            else:
                ch_k "See ya tomorrow, [KittyX.player_petname]."
        elif Player.Party[0] == EmmaX:
            if Player.location == Player.Party[0].home:
                ch_e "Could you please clear the room?"
            else:
                ch_e "I should leave."
        elif Player.Party[0] == LauraX:
            if Player.location == Player.Party[0].home:
                ch_l "Clear out."
            else:
                ch_l "So, later."
        elif Player.Party[0] == JeanX:
            if Player.location == Player.Party[0].home:
                ch_j "So get going."


        elif Player.Party[0] == StormX:
            if Player.location == Player.Party[0].home:
                ch_s "Could you please leave me?"
            else:
                ch_s "I will see you tomorrow."
        elif Player.Party[0] == JubesX:
            if Player.location == Player.Party[0].home:
                ch_v "I've got some stuff to take care of, so I should get going."
            else:
                ch_v "I've got some stuff to take care of, so I guess you should get going."

        menu:
            extend ""
            "Ok, I'll head out. Good night." if Player.Party[0].home == Player.location:

                $ line = "leave"
            "Ok, see you later then. Good night." if Player.Party[0].home != Player.location:

                $ line = "leave"

            "Are you sure I can't stay the night? . ." if not Player.Party[0].event_counter["sleepover"] and Player.Party[0].home == Player.location:
                $ line = "please"
            "Are you sure you can't stay? . ." if not Player.Party[0].event_counter["sleepover"] and Player.Party[0].home != Player.location:
                $ line = "please"

            "That's not what you said the other night . ." if Player.Party[0].event_counter["sleepover"]:

                if approval_check(Player.Party[0],900)or approval_check(Player.Party[0],700,"L") or approval_check(Player.Party[0],500,"O"):
                    $ Player.Party[0].change_face("_bemused", 1)
                    $ line = 1
                    if Player.Party[0] == RogueX:
                        ch_r "Well. . . that didn't turn out so bad, I suppose. . ."
                    elif Player.Party[0] == KittyX:
                        ch_k "and that went pretty well. . ."
                    elif Player.Party[0] == EmmaX:
                        ch_e "It was a nice evening."
                    elif Player.Party[0] == LauraX:
                        ch_l "Yeah, it was."
                    elif Player.Party[0] == JeanX:
                        ch_j "I guess?"
                    elif Player.Party[0] == StormX:
                        ch_s "That was pleasant. . ."
                    elif Player.Party[0] == JubesX:
                        ch_v "Yeah, yeah. . ."
                else:
                    $ Player.Party[0].change_face("_smile", brows = "_confused")

                    if Player.Party[0] == RogueX:
                        ch_r "I'm afraid not this time, [RogueX.player_petname]. I'll see you later."
                    elif Player.Party[0] == KittyX:
                        ch_k "Um, no, 'fraid not. I'll see ya tomorrow."
                    elif Player.Party[0] == EmmaX:
                        ch_e "Well, not tonight, [EmmaX.player_petname]."
                    elif Player.Party[0] == LauraX:
                        ch_l "Yeah, but not this time."
                    elif Player.Party[0] == JeanX:
                        ch_j "So what?"
                    elif Player.Party[0] == StormX:
                        ch_s "Yes, but not tonight, unfortunately. . ."
                    elif Player.Party[0] == JubesX:
                        ch_v "Yeah, I know, but I've got stuff to do tonight. . ."
                    if Player.location != "bg_player":

                        ch_p "Ok, I'll be going then."


    if line == "leave":

        $ Player.Party[0].change_stat("love", 90, 3)
        $ Player.Party[0].change_stat("inhibition", 25, 2)
        $ Player.Party[0].change_face("_smile")
        $ line = 0
        if Player.Party[0] == RogueX:
            ch_r "Yeah, good night, [RogueX.player_petname]. . ."
        elif Player.Party[0] == KittyX:
            ch_k "Yeah, 'night, [KittyX.player_petname]. . ."
        elif Player.Party[0] == EmmaX:
            ch_e "Yes, good night, [EmmaX.player_petname]."
        elif Player.Party[0] == LauraX:
            ch_l "Ok, good night then."
        elif Player.Party[0] == JeanX:
            ch_j "Ok, 'night."
        elif Player.Party[0] == StormX:
            ch_s "Yes, good night."
        elif Player.Party[0] == JubesX:
            ch_v "Yup. . . later then. . ."

    if line == "please":

        if approval_check(Player.Party[0], 1000) or approval_check(Player.Party[0],700,"L") or approval_check(Player.Party[0],500,"O"):
            $ Player.Party[0].change_face("_bemused")
            $ line = 1
            if Player.Party[0] == RogueX:
                ch_r "Well. . . I suppose it would be alright."
            elif Player.Party[0] == KittyX:
                ch_k "Well, Maaaybeee. . ."
            elif Player.Party[0] == EmmaX:
                ch_e "I suppose we could make an exception. . ."
            elif Player.Party[0] == LauraX:
                ch_l "Suit yourself."
            elif Player.Party[0] == JeanX:
                ch_j "-Fine,- geeze."
            elif Player.Party[0] == StormX:
                ch_s "Oh, I suppose we could make do. . ."
            elif Player.Party[0] == JubesX:
                ch_v "Well. . . fine. . ."
        else:
            $ Player.Party[0].change_face("_smile", brows = "_confused")
            $ line = 0
            if Player.Party[0] == RogueX:
                ch_r "I'm afraid not, [RogueX.player_petname]. Head home, I'll see you later."
            elif Player.Party[0] == KittyX:
                ch_k "Ehhhh. . . no, not tonight, [KittyX.player_petname]. Sorry."
            elif Player.Party[0] == EmmaX:
                ch_e "I'm afraid not."
            elif Player.Party[0] == LauraX:
                ch_l "Don't push it."
            elif Player.Party[0] == JeanX:
                ch_j "Yeah, no."
            elif Player.Party[0] == StormX:
                ch_s "No, we cannot."
            elif Player.Party[0] == JubesX:
                ch_v "Nope."

    if not line:

        if Player.Party[0].home == Player.location:

            call clear_the_room (Player.Party[0], 1)
            jump return_player_to_room
        else:

            call remove_Girl(Player.Party[0])
            call sleepover
            return


    if len(Player.Party) >= 2:

        if Player.Party[0].likes[Player.Party[1].tag] >= 700 and approval_check(Player.Party[0], 1200):

            if Player.Party[0] == RogueX:
                ch_r "And you, [Player.Party[1].name]?"
            elif Player.Party[0] == KittyX:
                ch_k "How about you, [Player.Party[1].name]?"
            elif Player.Party[0] == EmmaX:
                ch_e "And what about you, [Player.Party[1].name]?"
            elif Player.Party[0] == LauraX:
                ch_l "And you, [Player.Party[1].name]?"
            elif Player.Party[0] == JeanX:
                ch_j ". . ."
                ch_j ". . . . . ."
                ch_j "And you, [Player.Party[1].name]?"
            elif Player.Party[0] == StormX:
                ch_s "And are you staying as well, [Player.Party[1].name]?"
            elif Player.Party[0] == JubesX:
                ch_v "What about you, [Player.Party[1].name]?"
        else:
            if Player.Party[0] == RogueX:
                ch_r "Are you leaving, [Player.Party[1].name]?"
            elif Player.Party[0] == KittyX:
                ch_k "You heading out, [Player.Party[1].name]?"
            elif Player.Party[0] == EmmaX:
                ch_e "I assume you're leaving, [Player.Party[1].name]?"
            elif Player.Party[0] == LauraX:
                ch_l "See you later, [Player.Party[1].name]."
            elif Player.Party[0] == JeanX:
                ch_j ". . ."
                ch_j ". . . . . ."
                ch_j "And you, [Player.Party[1].name]?"
            elif Player.Party[0] == StormX:
                ch_s "And I assume you will be leaving, [Player.Party[1].name]?"
            elif Player.Party[0] == JubesX:
                ch_v "You've gotta go though, -right- [Player.Party[1].name]?"

        if Player.Party[1].likes[Player.Party[0].tag] >= 500 and approval_check(Player.Party[1], 1200):

            $ Player.Party[1].change_face("_smile")
            if Player.Party[1] == RogueX:
                ch_r "I'd like to stay too."
            elif Player.Party[1] == KittyX:
                ch_k "Can I stay too?"
            elif Player.Party[1] == EmmaX:
                ch_e "I'd rather join the fun."
            elif Player.Party[1] == LauraX:
                ch_l "Me too, right?"
            elif Player.Party[1] == JeanX:
                ch_j "Sounds fun, I'm in."
            elif Player.Party[1] == StormX:
                ch_s "I would prefer to stay."
            elif Player.Party[1] == JubesX:
                ch_v "I can stay too, right?"
            $ line = 1
        else:
            $ Player.Party[0].change_face("_smile", 1)
            if Player.Party[1] == RogueX:
                ch_r "I guess I should be going."
            elif Player.Party[1] == KittyX:
                ch_k "I should go, right?"
            elif Player.Party[1] == EmmaX:
                ch_e "I suppose three is a crowd."
            elif Player.Party[1] == LauraX:
                ch_l "I should leave."
            elif Player.Party[1] == JeanX:
                ch_j "Sounds \"fun.\""
                ch_j "Later guys."
            elif Player.Party[1] == StormX:
                ch_s "Ah, I should be going then."
            elif Player.Party[1] == JubesX:
                ch_v "Um, yeah, I've got stuff to do, so. . ."
            $ line = 0
        menu:
            extend ""
            "You should stay, [Player.Party[1].name].":

                if Player.Party[1].likes[Player.Party[0].tag] >= 500 and approval_check(Player.Party[1], 1200):

                    if Player.Party[1] == RogueX:
                        ch_r "Oh, I'd love to."
                    elif Player.Party[1] == KittyX:
                        ch_k "Roomies!"
                    elif Player.Party[1] == EmmaX:
                        ch_e "I'd love to."
                    elif Player.Party[1] == LauraX:
                        ch_l "Great."
                    elif Player.Party[1] == JeanX:
                        ch_j "Oh, so glad I have permission. . ."
                    elif Player.Party[1] == StormX:
                        ch_s "Thank you, I would love to."
                    elif Player.Party[1] == JubesX:
                        ch_v "Oh! Thanks!"
                    $ line = 1
                    $ Player.Party[0].check_if_likes(Player.Party[1],800,3, 1)
                else:
                    $ Player.Party[1].change_face("_sadside", 1,mouth = "_smile")
                    if Player.Party[1] == RogueX:
                        ch_r "I don't want to be a bother."
                    elif Player.Party[1] == KittyX:
                        ch_k "No way."
                    elif Player.Party[1] == EmmaX:
                        ch_e "I couldn't."
                    elif Player.Party[1] == LauraX:
                        ch_l "Nah."
                    elif Player.Party[1] == JeanX:
                        $ Player.Party[1].change_face("_angry", 1,mouth = "_smile")
                        ch_j "Oh, so glad I have permission. . ."
                    elif Player.Party[1] == StormX:
                        ch_s "I would not want to intrude."
                    elif Player.Party[1] == JubesX:
                        ch_v ". . . nah, really. . . stuff to do."
                    $ line = 0
                    $ Player.Party[0].check_if_likes(Player.Party[1],700,-5, 1)


                if line:
                    if Player.Party[0].likes[Player.Party[1].tag] >= 700 and approval_check(Player.Party[0], 1200):

                        if Player.Party[0] == RogueX:
                            ch_r "Great!"
                        elif Player.Party[0] == KittyX:
                            ch_k "Roomies!"
                        elif Player.Party[0] == EmmaX:
                            ch_e "Lovely."
                        elif Player.Party[0] == LauraX:
                            ch_l "Ok."
                        elif Player.Party[0] == JeanX:
                            ch_j "Nice, threesome."
                        elif Player.Party[0] == StormX:
                            ch_s "Excellent, glad to have you."
                        elif Player.Party[0] == JubesX:
                            ch_v "Oh, cool!"
                        $ Player.Party[1].check_if_likes(Player.Party[0],800,5, 1)
                    elif Player.Party[0].likes[Player.Party[1].tag] >= 400 and approval_check(Player.Party[0], 1400):

                        $ Player.Party[0].change_face("_sadside", 1,mouth = "_smile")
                        if Player.Party[0] == RogueX:
                            ch_r "Sure, I guess."
                        elif Player.Party[0] == KittyX:
                            ch_k "Um, Ok."
                        elif Player.Party[0] == EmmaX:
                            ch_e "I suppose we could find room for one more."
                        elif Player.Party[0] == LauraX:
                            ch_l "Whatever."
                        elif Player.Party[0] == JeanX:
                            ch_j "Yeah, ok."
                        elif Player.Party[0] == StormX:
                            ch_s "Very well, make yourself at home. . ."
                        elif Player.Party[0] == JubesX:
                            ch_v "Oh, cool! Promise I won't bite."
                    else:
                        $ Player.Party[0].change_face("_angry", 1)
                        if Player.Party[0] == RogueX:
                            ch_r "I'm not cool with that."
                        elif Player.Party[0] == KittyX:
                            ch_k "No way."
                        elif Player.Party[0] == EmmaX:
                            ch_e "I don't think so."
                        elif Player.Party[0] == LauraX:
                            ch_l "Um, no."
                        elif Player.Party[0] == JeanX:
                            ch_j "Definitely not."
                        elif Player.Party[0] == StormX:
                            ch_s "No, I'm afraid not, [Player.Party[1].name]."
                        elif Player.Party[0] == JubesX:
                            ch_v "Oh. . . cool. Promise I won't bite."
                            ch_v "much. . ."
                        $ Player.Party[0].check_if_likes(Player.Party[1],700,-5, 1)
                        $ Player.Party[1].check_if_likes(Player.Party[0],700,-5, 1)
                        $ line = 0
            "You should get going, [Player.Party[1].name].":

                if Player.Party[1] == RogueX:
                    ch_r "Oh, ok."
                elif Player.Party[1] == KittyX:
                    ch_k "Yeah."
                elif Player.Party[1] == EmmaX:
                    ch_e "I assumed."
                elif Player.Party[1] == LauraX:
                    ch_l "Yeah."
                elif Player.Party[1] == JeanX:
                    ch_j "What? You're not kicking me out, I'm kicking me out!"
                elif Player.Party[1] == StormX:
                    ch_s "Ah, I understand."
                elif Player.Party[1] == JubesX:
                    ch_v "Oh, ok, yeah. . ."
                $ line = 0

    if line == 0:

        if len(Player.Party) >= 2:
            if Player.Party[0] == RogueX:
                ch_r "Later, [Player.Party[1].name]."
            elif Player.Party[0] == KittyX:
                ch_k "Night, [Player.Party[1].name]."
            elif Player.Party[0] == EmmaX:
                ch_e "Goodnight, [Player.Party[1].name]."
            elif Player.Party[0] == LauraX:
                ch_l "Night."
            elif Player.Party[0] == JeanX:
                ch_j "Later, [Player.Party[1].name]."
            elif Player.Party[0] == StormX:
                ch_s "Good night, [Player.Party[1].name]."
            elif Player.Party[0] == JubesX:
                ch_v "Night, [Player.Party[1].name]."

            if Player.Party[1] == RogueX:
                ch_r "Later guys."
            elif Player.Party[1] == KittyX:
                ch_k "Night."
            elif Player.Party[1] == EmmaX:
                ch_e "Goodnight."
            elif Player.Party[1] == LauraX:
                ch_l "Night."
            elif Player.Party[1] == JeanX:
                ch_j "Right, later."
            elif Player.Party[1] == StormX:
                ch_s "Good night."
            elif Player.Party[1] == JubesX:
                ch_v "Night!"
        if Player.Party:
            call clear_the_room (Player.Party[0], 1, 1)

    if not Player.Party:

        if Player.location != "bg_player":
            jump return_player_to_room
        call clear_the_room ("all", 1)

        "It's getting late, so you go to sleep."
        call wait
        return

    if Player.location != "bg_player" and Player.location != Player.Party[0].home:

        "You probably shouldn't sleep here, you head back to your own room."
        call remove_all
        $ renpy.pop_call()
        jump player_room

    jump sleepover_Morning


label return_player_to_room:
    $ del Player.Party[:]

    $ temp_Girls = all_Girls[:]

    $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        if Player.location != temp_Girls[0].home and temp_Girls[0].location == Player.location:
            "[temp_Girls[0].name] heads out."

            call remove_Girl(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    if Player.location != "bg_player":
        "You head back to your room."

    jump player_room




label sleepover_Morning:

    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == Player.location and temp_Girls[0] not in Player.Party:
            call remove_Girl(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])

    call shift_focus (Player.Party[0])

    if Player.Party[0] == StormX and not StormX.sleepwear["outfit_active"] and StormX.taboo < 20:

        $ Player.Party[0].change_outfit("nude")
    else:
        $ Player.Party[0].change_outfit("sleepwear")
    $ Player.Party[0].today_outfit_name == Player.Party[0].outfit
    if len(Player.Party) >= 2:

        if Player.Party[1] == StormX and not StormX.sleepwear["outfit_active"] and StormX.taboo < 20:

            $ Player.Party[1].change_outfit("nude")
        else:
            $ Player.Party[1].change_outfit("sleepwear")
        $ Player.Party[1].today_outfit_name == Player.Party[1].outfit
        "The girls change into their sleepwear."
    else:
        "[Player.Party[0].name] changes into her sleepwear."

    if Player.Party[0] == RogueX:
        ch_r "Hmm, that's a bit more comfortable."
    elif Player.Party[0] == KittyX:
        ch_k "Ah, that's better."
    elif Player.Party[0] == EmmaX:
        ch_e "Mmmm, that's better."
    elif Player.Party[0] == LauraX:
        ch_l ". . ."
    elif Player.Party[0] == JeanX:
        ch_j "Sexy, right?"
    elif Player.Party[0] == StormX:
        ch_s "Ah, much better."
    elif Player.Party[0] == JubesX:
        ch_v "Ah, that's better."




    if len(Player.Party) >= 2:
        if Player.Party[1] == RogueX:
            ch_r "Let's turn in."
        elif Player.Party[1] == KittyX:
            ch_k "Night, [KittyX.player_petname]"
        elif Player.Party[1] == EmmaX:
            ch_e "lights out."
        elif Player.Party[1] == LauraX:
            ch_l "Night."
        elif Player.Party[1] == JeanX:
            ch_j "Night."
        elif Player.Party[1] == StormX:
            ch_s "Good night."
        elif Player.Party[1] == JubesX:
            ch_v "Night."
    else:


        if Player.Party[0] == RogueX:
            ch_r "Let's turn in."
        elif Player.Party[0] == KittyX:
            ch_k "Night, [KittyX.player_petname]"
        elif Player.Party[0] == EmmaX:
            ch_e "Goodnight."
        elif Player.Party[0] == LauraX:
            ch_l "Night."
        elif Player.Party[0] == JeanX:
            ch_j "Night."
        elif Player.Party[0] == StormX:
            ch_s "Good night."
        elif Player.Party[0] == JubesX:
            ch_v "Night."

    show black_screen onlayer black
    pause 1






    $ time_index = 0
    $ current_time = time_options[(time_index)]
    $ day += 1

    if weekday < 6:
        $ weekday += 1
    else:
        $ weekday = 0



    $ day_of_week = week[weekday]

    $ Player.semen = Player.max_semen
    $ Player.spunk = 0
    $ round = 50

    $ temp_Girls = Player.Party[:]
    while temp_Girls:
        $ temp_Girls[0].remaining_actions = temp_Girls[0].max_actions
        $ temp_Girls.remove(temp_Girls[0])














    call Morningwood_Check

    $ Player.Party[0].change_face("_smile")
    if len(Player.Party) >= 2:
        $ Player.Party[1].change_face("_smile")

    hide black_screen onlayer black

    if "morningwood" in Player.daily_history:

        if Player.Party[0] == RogueX:
            ch_r "So, that aside, Sleep well?"
        elif Player.Party[0] == KittyX:
            ch_k "So anyway. . . G'morning . . ."
        elif Player.Party[0] == EmmaX:
            ch_e "Now that we've got that out of our system. . ."
            ch_e "Morning, [EmmaX.player_petname]."
        elif Player.Party[0] == LauraX:
            ch_l "Anyway, 'Morning."
        elif Player.Party[0] == JeanX:
            ch_j "So. . . 'Morning."
        elif Player.Party[0] == StormX:
            ch_s "Anyway, good morning, [StormX.player_petname]."
        elif Player.Party[0] == JubesX:
            ch_v "Anyways, 'morning, [Player.Party[0].player_petname]."
    else:
        if Player.Party[0] == RogueX:
            ch_r "'Morning [RogueX.player_petname]. Sleep well?"
        elif Player.Party[0] == KittyX:
            ch_k "G'morning . . ."
        elif Player.Party[0] == EmmaX:
            ch_e "Hrmph. . ."
            ch_e "Oh. You're here."
        elif Player.Party[0] == LauraX:
            ch_l "'Morning."
        elif Player.Party[0] == JeanX:
            ch_j "-Yawn-"
        elif Player.Party[0] == StormX:
            ch_s "Good morning, [StormX.player_petname]."
        elif Player.Party[0] == JubesX:
            ch_v "Hey. . . 'morning, [Player.Party[0].player_petname]."

    menu:
        extend ""
        "It's always nice sleeping with you." if Player.Party[0].event_counter["sleepover"]:
            if Player.Party[0].event_counter["sleepover"] < 5:
                $ Player.Party[0].change_stat("love", 90, 8)
                $ Player.Party[0].change_stat("obedience", 50, 10)
                $ Player.Party[0].change_stat("inhibition", 70, 8)
            $ Player.Party[0].blushing = "_blush1"

            if Player.Party[0] == RogueX:
                ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
                ch_r "We'll have to keep this regular."
            elif Player.Party[0] == KittyX:
                ch_k "And that's always nice to hear."
                ch_k "We'll have to keep this up."
            elif Player.Party[0] == EmmaX:
                ch_e "Well. . ."
                ch_e "We'll have to make a habit of it then."
            elif Player.Party[0] == LauraX:
                ch_l "Yeah. . ."
                ch_l "Warm. . ."
            elif Player.Party[0] == JeanX:
                ch_j "Of course it is."
                ch_j "I'm a princess."
            elif Player.Party[0] == StormX:
                ch_s "I enjoy it as well, [StormX.player_petname]."
                ch_s "You keep the bed quite warm. . ."
            elif Player.Party[0] == JubesX:
                ch_v "Yeah. . . it's nice having company. . ."
                ch_v "You keep it so cozy. . ."

        "I loved sleeping next to you." if not Player.Party[0].event_counter["sleepover"]:
            $ Player.Party[0].change_stat("love", 90, 15)
            $ Player.Party[0].change_stat("love", 70, 10)
            $ Player.Party[0].change_stat("obedience", 50, 12)
            $ Player.Party[0].change_stat("inhibition", 70, 12)
            $ line = "nice"
        "It was fun.":

            if not Player.Party[0].event_counter["sleepover"]:
                $ Player.Party[0].change_stat("love", 90, 10)
                $ Player.Party[0].change_stat("love", 70, 8)
                $ Player.Party[0].change_stat("obedience", 50, 15)
                $ Player.Party[0].change_stat("inhibition", 70, 15)
            elif Player.Party[0].event_counter["sleepover"] < 5:
                $ Player.Party[0].change_stat("love", 70, 8)
                $ Player.Party[0].change_stat("obedience", 80, 10)
                $ Player.Party[0].change_stat("inhibition", 35, 8)
            $ Player.Party[0].change_stat("obedience", 50, 8)
            if approval_check(Player.Party[0], 800, "L"):
                $ Player.Party[0].change_face("_bemused")
            else:
                $ Player.Party[0].change_face("_confused")

            $ line = "fun"
            if Player.Party[0] == RogueX:
                ch_r "Ok, well glad I wasn't {i}too{/i} much bother."
            elif Player.Party[0] == KittyX:
                ch_k "Yeah, I mean I guess it was. . ."
            elif Player.Party[0] == EmmaX:
                ch_e "\"Fun\" is certainly how I would describe it."
            elif Player.Party[0] == LauraX:
                ch_l "Yeah, I guess?"
            elif Player.Party[0] == JeanX:
                ch_j "Um, \"fun?\" . . Yeah."
            elif Player.Party[0] == StormX:
                ch_s ". . . Yes. . ."
                ch_s ". . . fun."
            elif Player.Party[0] == JubesX:
                ch_v "Yeah. . . it's nice having company. . ."
                $ line = "nice"
        "You were constantly tossing around.":

            $ Player.Party[0].blushing = "_blush1"
            if approval_check(Player.Party[0], 800, "L") or approval_check(Player.Party[0], 1200):
                $ Player.Party[0].change_face("_bemused")
                Player.Party[0].voice "Hmm?"
            else:
                $ Player.Party[0].change_face("_angry")
                Player.Party[0].voice "!!!"
            if Player.Party[0].event_counter["sleepover"] < 5:
                if Player.Party[0] == RogueX:
                    ch_r "It's not like I've had much experience sleeping next to someone. . ."
                elif Player.Party[0] == KittyX:
                    ch_k "I don't make a habit out of it. . ."
                elif Player.Party[0] == EmmaX:
                    ch_e "I haven't had a lot of practice lately."
                elif Player.Party[0] == LauraX:
                    ch_l "Deal with it."
                elif Player.Party[0] == JeanX:
                    ch_j "It's called \"grace.\""
                elif Player.Party[0] == StormX:
                    ch_s "Yes. . . well. . ."
                    ch_s "I do have a lot of energy. . ."
                elif Player.Party[0] == JubesX:
                    ch_v "I'm just not used to sleeping nights. . ."
                $ Player.Party[0].change_stat("love", 60, -8)
                $ Player.Party[0].change_stat("obedience", 50, 22)
                $ Player.Party[0].change_stat("inhibition", 50, 22)
            else:
                if Player.Party[0] == RogueX:
                    ch_r "Well you should probably be used to that by now."
                elif Player.Party[0] == KittyX:
                    ch_k "Yeah, well. . . you should be used to that!"
                elif Player.Party[0] == EmmaX:
                    ch_e "I don't plan on changing any time soon."
                elif Player.Party[0] == LauraX:
                    ch_l "Yeah, it'll be like that."
                elif Player.Party[0] == JeanX:
                    ch_j "Deal with it."
                elif Player.Party[0] == StormX:
                    ch_s "I suppose that I do."
                elif Player.Party[0] == JubesX:
                    ch_v "You don't need to harp on it. . ."
            $ line = "toss"
        "You need to learn to stick to your side.":

            if Player.Party[0].event_counter["sleepover"] < 5:
                $ Player.Party[0].change_stat("love", 80, -8)
                $ Player.Party[0].change_stat("obedience", 50, 40)
            if approval_check(Player.Party[0], 500, "O"):
                $ Player.Party[0].change_stat("love", 80, -2)
                $ Player.Party[0].change_stat("obedience", 90, 5)
                $ Player.Party[0].change_face("_normal")
                if Player.Party[0] == RogueX:
                    ch_r "Yes, [RogueX.player_petname], I'll try my best."
                elif Player.Party[0] == KittyX:
                    ch_k "Fine, whatever."
                elif Player.Party[0] == EmmaX:
                    ch_e "I do try."
                elif Player.Party[0] == LauraX:
                    ch_l "Ok."
                elif Player.Party[0] == JeanX:
                    ch_j "It's all my side."
                elif Player.Party[0] == StormX:
                    ch_s "I. . . can try. . ."
                elif Player.Party[0] == JubesX:
                    ch_v "I thought you wanted the attention. . ."
                if Player.Party[0].event_counter["sleepover"] < 5:
                    $ Player.Party[0].change_stat("obedience", 80, 8)
            else:
                $ Player.Party[0].change_face("_angry")
                $ Player.Party[0].change_stat("obedience", 90, 5)
                if Player.Party[0] == RogueX:
                    ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."
                elif Player.Party[0] == KittyX:
                    ch_k "That's not how you get me to come back."
                elif Player.Party[0] == EmmaX:
                    ch_e "I'll sleep how I please."
                elif Player.Party[0] == LauraX:
                    ch_l "Good luck with that."
                elif Player.Party[0] == JeanX:
                    ch_j "It's all my side."
                elif Player.Party[0] == StormX:
                    ch_s "That seems unlikely."
                elif Player.Party[0] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
                if Player.Party[0].event_counter["sleepover"] < 5:
                    $ Player.Party[0].change_stat("inhibition", 35, 20)
            $ line = "toss"

    if not Player.Party[0].event_counter["sleepover"] and line == "nice":
        if Player.Party[0] == RogueX:
            $ Player.Party[0].blushing = "_blush1"
            ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
            ch_r "Makes me want to do it again sometime."
        elif Player.Party[0] == KittyX:
            $ Player.Party[0].blushing = "_blush2"
            ch_k "Yeah, I. . [KittyX.like]I had fun too."
            $ Player.Party[0].blushing = "_blush1"
            ch_k "I wouldn't[KittyX.like]mind doing it again."
            $ Player.Party[0].blushing = "_blush2"
            ch_k "You know, some other time. . . "
            $ Player.Party[0].blushing = "_blush1"
        elif Player.Party[0] == EmmaX:
            $ Player.Party[0].change_face("_smile", 1)
            ch_e "You're a hopeless romantic, [EmmaX.player_petname]."
            $ Player.Party[0].change_face("_smile",2,eyes = "_side")
            ch_e "I suppose I can be a bit hopeless too. . ."
        elif Player.Party[0] == LauraX:
            $ Player.Party[0].change_face("_confused", 1)
            ch_l "Oh. . ."
            $ Player.Party[0].change_face("_surprised",2,brows = "_confused")
            ch_l "Yeah, so did I, now that you mention it. . ."
            $ Player.Party[0].change_face("_confused", 1)
            ch_l "Huh."
        elif Player.Party[0] == JeanX:
            $ Player.Party[0].change_face("_confused", 1)
            ch_j "Huh? . ."
            ch_j "Oh, yeah. . . it was great. . ."
            $ Player.Party[0].change_face("_smile", 1)
        elif Player.Party[0] == StormX:
            $ Player.Party[0].change_face("_smile", 1)
            ch_s "Well, yes, it was nice to sleep next to you as well, [StormX.player_petname]."
            $ Player.Party[0].change_face("_smile",2,eyes = "_leftside")
            ch_s "I think we should make a habit of this. . ."
            $ Player.Party[0].change_face("_smile", 1)
        elif Player.Party[0] == JubesX:
            $ Player.Party[0].change_face("_smile", 1)
            ch_v "Yeah, I enjoyed it too. . ."
            $ Player.Party[0].change_face("_sad", 1)
            ch_v "I haven't really been sleeping much since. . ."
            $ Player.Party[0].change_face("_sadside", 1)
            ch_v ". . . the change."
            $ Player.Party[0].change_face("_smile", 1)
            ch_v "It's nice having someone to stay with me. . ."

    $ Player.Party[0].blushing = ""

    if len(Player.Party) >= 2:

        if "morningwood" in Player.daily_history:
            if Player.Party[1] == RogueX:
                ch_r "And what about me?"
            elif Player.Party[1] == KittyX:
                ch_k "Me too?"
            elif Player.Party[1] == EmmaX:
                ch_e "And me?"
            elif Player.Party[1] == LauraX:
                ch_l "Ung, 'morning."
            elif Player.Party[1] == JeanX:
                ch_j "Yeah, yeah, 'morning."
            elif Player.Party[1] == StormX:
                ch_s "Ah, yes, good morning."
            elif Player.Party[1] == JubesX:
                ch_v "Yeah. . . 'morning."
        else:
            "[Player.Party[1].name] rolls over in bed."
            if Player.Party[1] == RogueX:
                ch_r "Mmm, yeah, 'Morning [RogueX.player_petname]."
            elif Player.Party[1] == KittyX:
                ch_k "Yeah, G'morning . . ."
            elif Player.Party[1] == EmmaX:
                ch_e "Hrmph. . ."
                ch_e "Oh. Not so loud, you two."
            elif Player.Party[1] == JeanX:
                ch_j "Yeah, yeah, 'morning."
            elif Player.Party[1] == StormX:
                ch_s "Ah, yes, good morning."
            elif Player.Party[1] == JubesX:
                ch_v "Oh, um, yeah. . . 'morning."

        menu:
            extend ""
            "I always love sleeping with you too, [Player.Party[1].name]." if Player.Party[1].event_counter["sleepover"]:
                if Player.Party[1].event_counter["sleepover"] < 5:
                    $ Player.Party[1].change_stat("love", 90, 8)
                    $ Player.Party[1].change_stat("obedience", 50, 10)
                    $ Player.Party[1].change_stat("inhibition", 70, 8)
                $ Player.Party[1].blushing = "_blush1"

                if Player.Party[1] == RogueX:
                    ch_r "That's sweet of ya to say, [RogueX.player_petname]."
                elif Player.Party[1] == KittyX:
                    ch_k "So cute!"
                elif Player.Party[1] == EmmaX:
                    ch_e "Mmmm. . . yes, lovely."
                elif Player.Party[1] == LauraX:
                    ch_l "Sure. . ."
                elif Player.Party[1] == JeanX:
                    ch_j "Ouch, you're giving me a toothache."
                elif Player.Party[1] == StormX:
                    ch_s "And I enjoy it as well, [StormX.player_petname]."
                elif Player.Party[1] == JubesX:
                    ch_v "Yeah. . . it's nice having company. . ."

            "And it was great sleeping with you as well, [Player.Party[1].name]." if not Player.Party[1].event_counter["sleepover"]:
                $ Player.Party[1].change_stat("love", 90, 15)
                $ Player.Party[1].change_stat("love", 70, 10)
                $ Player.Party[1].change_stat("obedience", 50, 12)
                $ Player.Party[1].change_stat("inhibition", 70, 12)
                $ line = "nice"
            "I had fun sleeping with you too, [Player.Party[1].name].":

                if not Player.Party[1].event_counter["sleepover"]:
                    $ Player.Party[1].change_stat("love", 90, 10)
                    $ Player.Party[1].change_stat("love", 70, 8)
                    $ Player.Party[1].change_stat("obedience", 50, 15)
                    $ Player.Party[1].change_stat("inhibition", 70, 15)
                elif Player.Party[1].event_counter["sleepover"] < 5:
                    $ Player.Party[1].change_stat("love", 70, 8)
                    $ Player.Party[1].change_stat("obedience", 80, 10)
                    $ Player.Party[1].change_stat("inhibition", 35, 8)
                $ Player.Party[1].change_stat("obedience", 50, 8)
                if approval_check(Player.Party[1], 800, "L"):
                    $ Player.Party[1].change_face("_bemused")
                else:
                    $ Player.Party[1].change_face("_confused")

                $ line = "fun"
                if Player.Party[1] == RogueX:
                    ch_r "Yeah, uh, fun."
                elif Player.Party[1] == KittyX:
                    ch_k "Yeah, I mean I guess it was. . ."
                elif Player.Party[1] == EmmaX:
                    ch_e "\"Fun\" is certainly how I would describe it."
                elif Player.Party[1] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Player.Party[1] == JeanX:
                    ch_j "Yeah you did."
                elif Player.Party[1] == StormX:
                    ch_s ". . . Yes. . ."
                    ch_s ". . . fun."
                elif Player.Party[1] == JubesX:
                    ch_v "Yeah. . . it's nice having company. . ."
                    $ line = "nice"

            "You were constantly tossing around, [Player.Party[1].name]." if line == "toss":
                $ line = "toss"
            "You were tossing around constantly too, [Player.Party[1].name]." if line != "toss":
                $ line = "toss"

            "You need to learn to stick to your side, [Player.Party[1].name]." if line == "toss":
                $ line = "turn"
            "And you need to learn to stick to your side too, [Player.Party[1].name]." if line != "toss":
                $ line = "turn"

        if not Player.Party[1].event_counter["sleepover"] and line == "nice":
            if Player.Party[1] == RogueX:
                $ Player.Party[1].blushing = "_blush1"
                ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
                ch_r "I think I'd want to do that again."
                ch_r "And, uh, you too, [Player.Party[0].name]."
            elif Player.Party[1] == KittyX:
                $ Player.Party[1].blushing = "_blush2"
                ch_k "Yeah, I. . [KittyX.like]I had fun too."
                $ Player.Party[1].blushing = "_blush1"
                ch_k "I wouldn't[KittyX.like]mind doing it again."
                $ Player.Party[1].blushing = "_blush2"
                ch_k "You know, some other time. . . "
                $ Player.Party[1].blushing = "_blush1"
                ch_k "And[KittyX.like]you too, [Player.Party[0].name]."
            elif Player.Party[1] == EmmaX:
                $ Player.Party[1].change_face("_smile", 1)
                ch_e "You're a hopeless romantic, [EmmaX.player_petname]."
                $ Player.Party[1].change_face("_smile",2,eyes = "_side")
                ch_e "I suppose I can be a bit hopeless too. . ."
                ch_e "You know what I'm talking about, [Player.Party[0].name]."
            elif Player.Party[1] == LauraX:
                $ LauraX.change_face("_confused", 1)
                ch_l "Oh. . ."
                $ Player.Party[1].change_face("_surprised",2,brows = "_confused")
                ch_l "Yeah, so did I, now that you mention it. . ."
                $ Player.Party[1].change_face("_confused", 1)
                ch_l "Huh."
                ch_l "Weird, right, [Player.Party[0].name]?"
            elif Player.Party[1] == JeanX:
                $ Player.Party[1].change_face("_confused", 1)
                ch_j "Huh? . ."
                ch_j "Oh, yeah. . . it was great. . ."
                $ Player.Party[0].change_face("_smile", 1)
            elif Player.Party[1] == StormX:
                $ Player.Party[1].change_face("_smile", 1)
                ch_s "Well, yes, it was nice to sleep next to you as well, [StormX.player_petname]."
                $ Player.Party[1].change_face("_smile",2,eyes = "_leftside")
                ch_s "I think we should make a habit of this. . ."
                $ Player.Party[1].change_face("_smile", 1)
            elif Player.Party[1] == JubesX:
                $ Player.Party[1].change_face("_smile", 1)
                ch_v "Yeah, I enjoyed it too. . ."
                $ Player.Party[1].change_face("_sad", 1)
                ch_v "I haven't really been sleeping much since. . ."
                $ Player.Party[1].change_face("_sadside", 1)
                ch_v ". . . the change."
                $ Player.Party[1].change_face("_smile", 1)
                ch_v "It's nice having someone to stay with me. . ."


        elif line == "toss":
            $ Player.Party[1].blushing = "_blush1"
            if approval_check(Player.Party[1], 800, "L") or approval_check(Player.Party[1], 1200):
                $ Player.Party[1].change_face("_bemused")
                Player.Party[1].voice "Hmm?"
            else:
                $ Player.Party[1].change_face("_angry")
                Player.Party[1].voice "!!!"
            if Player.Party[1].event_counter["sleepover"] < 5:
                if Player.Party[1] == RogueX:
                    ch_r "It's not like I've had much experience sleeping next to someone. . ."
                elif Player.Party[1] == KittyX:
                    ch_k "I don't make a habit out of it. . ."
                elif Player.Party[1] == EmmaX:
                    ch_e "I haven't had a lot of practice lately."
                elif Player.Party[1] == LauraX:
                    ch_l "Deal with it."
                elif Player.Party[1] == JeanX:
                    ch_j "It's called \"grace.\""
                elif Player.Party[1] == StormX:
                    ch_s "Yes. . . well. . ."
                    ch_s "I do have a lot of energy. . ."
                elif Player.Party[1] == JubesX:
                    ch_v "I'm just not used to sleeping nights. . ."
                $ Player.Party[1].change_stat("love", 60, -8)
                $ Player.Party[1].change_stat("obedience", 50, 22)
                $ Player.Party[1].change_stat("inhibition", 50, 22)
            else:
                if Player.Party[1] == RogueX:
                    ch_r "Well you should probably be used to that by now."
                elif Player.Party[1] == KittyX:
                    ch_k "Yeah, well. . . you should be used to that!"
                elif Player.Party[1] == EmmaX:
                    ch_e "I don't plan on changing any time soon."
                elif Player.Party[1] == LauraX:
                    ch_l "Yeah, it'll be like that."
                elif Player.Party[1] == JeanX:
                    ch_j "Deal with it."
                elif Player.Party[1] == StormX:
                    ch_s "I suppose that I do."
                elif Player.Party[1] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
        elif line == "turn":
            if Player.Party[1].event_counter["sleepover"] < 5:
                $ Player.Party[1].change_stat("love", 80, -8)
                $ Player.Party[1].change_stat("obedience", 50, 40)
            if approval_check(Player.Party[1], 500, "O"):
                $ Player.Party[1].change_stat("love", 80, -2)
                $ Player.Party[1].change_stat("obedience", 90, 5)
                $ Player.Party[1].change_face("_normal")
                if Player.Party[1] == RogueX:
                    ch_r "Yes, [RogueX.player_petname], I'll try my best."
                elif Player.Party[1] == KittyX:
                    ch_k "Fine, whatever."
                elif Player.Party[1] == EmmaX:
                    ch_e "I do try."
                elif Player.Party[1] == LauraX:
                    ch_l "Ok."
                elif Player.Party[1] == JeanX:
                    ch_j "It's all my side."
                elif Player.Party[1] == StormX:
                    ch_s "I. . . can try. . ."
                elif Player.Party[1] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
                if Player.Party[1].event_counter["sleepover"] < 5:
                    $ Player.Party[1].change_stat("obedience", 80, 8)
            else:
                $ Player.Party[1].change_face("_angry")
                $ Player.Party[1].change_stat("obedience", 90, 5)
                if Player.Party[1] == RogueX:
                    ch_r "Hmmph, you'll be sleeping alone, keep talk'in like that."
                elif Player.Party[1] == KittyX:
                    ch_k "That's not how you get me to come back."
                elif Player.Party[1] == EmmaX:
                    ch_e "I'll sleep how I please."
                elif Player.Party[1] == LauraX:
                    ch_l "Good luck with that."
                elif Player.Party[1] == JeanX:
                    ch_j "It's all my side."
                elif Player.Party[1] == StormX:
                    ch_s "That seems unlikely."
                elif Player.Party[1] == JubesX:
                    ch_v "I could just stay out of the bed entirely. . ."
                if Player.Party[1].event_counter["sleepover"] < 5:
                    $ Player.Party[1].change_stat("inhibition", 35, 20)

        $ Player.Party[1].blushing = ""



    if len(Player.Party) >= 2:
        $ Player.Party[1].event_counter["sleepover"] += 1


    $ Player.Party[0].event_counter["sleepover"] += 1




    $ time_index = 3
    $ current_time = time_options[(time_index)]
    $ day -= 1

    if weekday == 0:
        $ weekday = 6
    else:
        $ weekday -= 1

    $ day_of_week = week[weekday]

    call wait

    python:
        for G in all_Girls:
            if G.location == Player.location:
                Player.Party.append(G)

            if "morningwood" in G.traits:
                G.recent_history.append("blowjob")
                G.daily_history.append("blowjob")
                G.daily_history.append("morningwood")
                G.traits.remove("morningwood")



    if Player.Party:
        $ Player.Party[0].change_face("_normal")
        $ Player.Party[0].change_outfit("today")

        if len(Player.Party) >= 2:
            $ Player.Party[1].change_face("_normal")
            $ Player.Party[1].change_outfit("today")

            "The girls get changed for the day."
        else:
            "[Player.Party[0].name] gets changed for the day."

    $ Player.Party = []







    call girls_location
    return









label Morningwood_Check(Girls=[0,-3], D20=0):



    $ D20 = renpy.random.randint(0,3)
    $ line = 0

    if len(Player.Party) >= 2:

        if Player.Party[0].likes[Player.Party[1].tag] >= 900:

            $ Girls[0] = 2
        elif Player.Party[0].likes[Player.Party[1].tag] >= 750:

            $ Girls[0] = 0
        elif Player.Party[0].likes[Player.Party[1].tag] <= 400:

            $ Girls[0] = 2
        else:
            $ Girls[0] = 0

        if Player.Party[1].likes[Player.Party[0].tag] >= 900:

            $ Girls[1] = 2
        elif Player.Party[1].likes[Player.Party[0].tag] >= 750:

            $ Girls[1] = 0
        elif Player.Party[1].likes[Player.Party[0].tag] <= 400:

            $ Girls[1] = -5
        else:
            $ Girls[1] = -3
    else:
        $ Girls[0] -= 2


    if "chill" in Player.Party[0].traits:

        $ Girls[0] = 0
    else:
        if Player.Party[0].action_counter["blowjob"] >= 5 or approval_check(Player.Party[0], 900, "I"):
            $ Girls[0] += 3
        elif Player.Party[0].action_counter["blowjob"] and approval_check(Player.Party[0], 900):
            $ Girls[0] += 2
        elif approval_check(Player.Party[0], 1400):
            $ Girls[0] += 2
        elif Player.Party[0].action_counter["blowjob"] or approval_check(Player.Party[0], 900):
            $ Girls[0] += 1

        if "hungry" in Player.Party[0].traits and D20 >= 2:

            $ Girls[0] += 2
        if Player.Party[0].thirst >= 60:

            $ Girls[0] += 2
        elif Player.Party[0].thirst >= 30:

            $ Girls[0] += 1
        if Player.Party[0].lust >= 50:

            $ Girls[0] += 1
        if Player.Party[0].SEXP <= 15:

            $ Girls[0] -= 1


        if Girls[1] >= 0:

            $ Girls[0] += 1


    if JubesX in Player.Party:

        if len(Player.Party) >= 2:
            $ line = "no"
        else:
            return
    elif Girls[0] >= D20:
        $ line = "yes"




    if len(Player.Party) >= 2:
        if Player.Party[1].action_counter["blowjob"] >= 5 or approval_check(Player.Party[1], 900, "I"):
            $ Girls[1] += 3
        elif Player.Party[1].action_counter["blowjob"] and approval_check(Player.Party[1], 900):
            $ Girls[1] += 2
        elif approval_check(Player.Party[1], 1400):
            $ Girls[1] += 2
        elif Player.Party[1].action_counter["blowjob"] or approval_check(Player.Party[1], 900):
            $ Girls[1] += 1

        if "hungry" in Player.Party[1].traits and D20 >= 2:

            $ Girls[1] += 2
        if Player.Party[1].thirst >= 60:

            $ Girls[1] += 2
        elif Player.Party[1].thirst >= 30:

            $ Girls[1] += 1
        if Player.Party[1].lust >= 50:

            $ Girls[1] += 1
        if Player.Party[1].SEXP <= 15:

            $ Girls[1] -= 1


        if Girls[0] >= 0:

            $ Girls[1] += 1


        if Player.Party[1] == JubesX:

            if Girls[1] >= (D20 + 1):
                $ line = "other"
            elif Girls[1] <= -1:
                $ line = "no"
        elif Girls[1] >= (D20 + 1):
            if line == "yes":
                $ line = "double"
            else:
                $ line = "other"
        elif Girls[1] <= -1:
            $ line = "no"


        if line == "other" and Player.Party[0].likes[Player.Party[1].tag] >= 500 and "chill" not in Player.Party[1].traits:

            $ Player.Party.reverse()
            $ Girls[0] = "yes"
            $ Girls[1] = 0



    if line:

        if line == "no":

            "You hear a little commotion as you start to wake up."
            if Player.Party[1] == RogueX:
                ch_r "You get'cher head out of there, [Player.Party[0].name]!"
            elif Player.Party[1] == KittyX:
                "You hear a thump and feel a small woosh as something heavy drops under the bed."
                Player.Party[0].voice "Ow!"
                ch_k "Serves you right, [Player.Party[0].name]."
            elif Player.Party[1] == EmmaX:
                ch_e "Step away from [Player.name], [Player.Party[0].name]."
            elif Player.Party[1] == LauraX:
                ch_l "Back it up, [Player.Party[0].name]."
            elif Player.Party[1] == JeanX:
                ch_j "Back it off, [Player.Party[0].name]."
            elif Player.Party[1] == StormX:
                ch_s "[Player.Party[0].name], some of us are trying to sleep. . ."
            elif Player.Party[1] == JubesX:
                ch_v "He's trying to sleep over there, cut it out. . ."

            if Player.Party[0] == RogueX:
                ch_r "I didn't mean no harm, [Player.Party[1].name]."
            elif Player.Party[0] == KittyX:
                "You hear a thump and feel a small woosh as something drops under the bed."
                Player.Party[0].voice "Ow!"
                ch_k "Spoilsport."
            elif Player.Party[0] == EmmaX:
                ch_e "Don't be a bore, dear."
            elif Player.Party[0] == LauraX:
                ch_l "Fine, whatever."
            elif Player.Party[0] == JeanX:
                ch_j "You back it off. . ."
                "-Zap-"
            elif Player.Party[0] == StormX:
                ch_s "I didn't intend to wake you. . ."
            elif Player.Party[0] == JubesX:
                ch_v "Oh, fine. . ."
            if Player.Party[0] != JeanX:
                return
        elif line == "double":

            $ second_girl_main_action = "blowjob"
            $ Player.Party[1].recent_history.append("blowjob")
            $ Player.Party[1].daily_history.append("blowjob")
            $ Player.Party[1].daily_history.append("morningwood")
            $ Player.Party[1].traits.append("morningwood")

        $ Player.primary_action = "blowjob"
        $ Player.Party[0].recent_history.append("blowjob")
        $ Player.Party[0].daily_history.append("blowjob")
        $ Player.Party[0].daily_history.append("morningwood")
        $ Player.Party[0].traits.append("morningwood")
        call sleepover_MorningWood

        call sex_over(put_clothes_on = False)
    else:



        pass

    return






label sleepover_MorningWood:

    $ Player.add_word(1,"interruption")
    call shift_focus (Player.Party[0])
    $ Player.focus = 30
    if Player.primary_action == "blowjob":
        ch_u "\"Slurp, slurp, slurp.\""
    else:
        ch_u "\"Squish, squish, squish.\""

    $ Player.change_stat("focus", 80, 5)
    $ Player.Party[0].change_stat("lust", 80, 5)
    $ Player.daily_history.append("morningwood")

    $ Partner = Player.Party[1] if len(Player.Party) >= 2 else 0


    $ Player.recent_history.append("cockout")

    if Partner:
        call show_Girl(Partner, x_position = 0.85, y_position = 0.33)

        $ Partner.recent_history.append("threesome")

    $ Player.Party[0].recent_history.append("blanket")
    call show_blowjob(Player.Party[0])

    $ Player.Party[0].change_face("_closed", 1)
    if Partner:
        $ Partner.change_face("_closed", 1,mouth = "_tongue")

    "You feel a pleasant sensation. . ."
    if Player.primary_action == "blowjob":
        if second_girl_main_action:
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
    else:
        if second_girl_main_action:
            ch_u "\"Squish, squish, squish.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Squish, squish, squish.\""
    $ Player.change_stat("focus", 80, 5)
    $ Player.Party[0].change_stat("lust", 80, 5)

    "It's somewhere below your waist. . ."
    if Player.primary_action == "blowjob":
        if second_girl_main_action:
            ch_u "\"Slurp, slurp, slurp.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Slurp, slurp, slurp.\""
    else:
        if second_girl_main_action:
            ch_u "\"Squish, squish, squish.\" \n \ \"Slurp, slurp, slurp.\""
        else:
            ch_u "\"Squish, squish, squish.\""
    $ Player.change_stat("focus", 80, 10)
    $ Player.Party[0].change_stat("lust", 80, 5)

    "You open your eyes. . ."

    hide black_screen onlayer black

    $ action_speed = 3
    $ Count = 3
    $ line = 0
    call Seen_First_Peen (Player.Party[0], Partner, 1, 1, 1)
    while Count > 0:

        $ Player.change_stat("focus", 80, 10)
        $ Player.Party[0].change_stat("lust", 80, 5)
        if Partner:
            $ Partner.change_stat("lust", 80, 5)
        menu:
            "Stay Quiet":
                if Count >2:
                    if second_girl_main_action:
                        "You just let them do their thing and pretend to still be asleep."
                    else:
                        "You just let her do her thing and pretend to still be asleep."
                elif Count>1:
                    "It does feel nice. . ."
                else:
                    if second_girl_main_action:
                        "You wouldn't want to disturb them. . ."
                    else:
                        "You wouldn't want to disturb her. . ."
                if Player.primary_action == "blowjob":
                    Player.Party[0].voice "\"Slurp, slurp, slurp.\""
                else:
                    Player.Party[0].voice "\"Squish, squish, squish.\""
                if second_girl_main_action:
                    Player.Party[1].voice "\"Slurp, slurp, slurp.\""
                ". . ."
            "Um. . . [Player.Party[0].petname], what're you doing?":
                $ line = "question"
                $ Count = 1
            "That feels great, keep going. . .":
                $ line = "praise"
                $ Count = 1
            "Hey, quit that!":
                $ line = "no"
                $ Count = 1
        $ Count -= 1
    $ action_speed = 1
    $ Player.Party[0].blushing = "_blush1"
    if second_girl_main_action:
        "[Player.Party[0].name] pulls back with a pop and [Player.Party[1].name] sits back."
        $ second_girl_main_action = None
    else:
        "[Player.Party[0].name] pulls back with a pop."
    if line == "question":
        $ Player.Party[0].change_face("_smile", 1)
        if Player.Party[0] == RogueX:
            ch_r "Well I ain't whistlin Dixie, [RogueX.player_petname]."
        elif Player.Party[0] == KittyX:
            ch_k "I wasn't[KittyX.like]being subtle about it, [KittyX.player_petname]."
        elif Player.Party[0] == EmmaX:
            ch_e "Surely your education hasn't been that poor, [EmmaX.player_petname]."
        elif Player.Party[0] == LauraX:
            ch_l "Guess."
        elif Player.Party[0] == JeanX:
            $ Player.Party[0].change_face("_confused", 1)
            $ action_speed = 2
            ch_j ". . ."
            ch_j "I 'ave orr dick, in ey 'outh. . ."
            ch_j "Are u 'rain 'amaged?"
            $ action_speed = 1
            if Partner:
                $ Player.Party[0].eyes = "_leftside"
                ch_j "Is he brain damaged?"
            $ Player.Party[0].change_face("_sly", 1)
        elif Player.Party[0] == StormX:
            ch_s "I didn't intend to wake you. . ."
        elif Player.Party[0] == JubesX:
            ch_v "Sorry, I. . . hadn't had breakfast. . ."
    elif line == "praise":
        $ Player.Party[0].change_face("_smile", 1)
        $ Player.Party[0].change_stat("love", 90, 5)
        $ Player.Party[0].change_stat("obedience", 50, 2)
        $ Player.Party[0].change_stat("inhibition", 60, 2)
        if Player.Party[0] == RogueX:
            ch_r "Mmm, you know it, [RogueX.player_petname]."
        elif Player.Party[0] == KittyX:
            ch_k "Mmm, hehe."
        elif Player.Party[0] == EmmaX:
            ch_e "Practice, [EmmaX.player_petname]."
        elif Player.Party[0] == LauraX:
            ch_l "Yeah, I guess?"
        elif Player.Party[0] == JeanX:
            ch_j "Heh."
        elif Player.Party[0] == StormX:
            ch_s "Certainly. . ."
        elif Player.Party[0] == JubesX:
            ch_v "I do enjoy it. . ."
    elif line == "no":
        $ Player.Party[0].change_stat("love", 90, -3)
        $ Player.Party[0].change_stat("obedience", 50, 2)
        $ Player.Party[0].change_stat("inhibition", 60, -2)
        $ action_speed = 0
        $ Player.Party[0].change_face("_angry", 1,brows = "_confused")
        if Player.Party[0] == RogueX:
            ch_r "Well that's a fine \"how d'ya do,\" when a girl goes to all this trouble!"
        elif Player.Party[0] == KittyX:
            ch_k "{i}That's{/i} the thanks I get?!"
        elif Player.Party[0] == EmmaX:
            ch_e "A little \"gratitude\" wouldn't be uncalled for. . ."
        elif Player.Party[0] == LauraX:
            ch_l "Huh?"
        elif Player.Party[0] == JeanX:
            ch_j "Seriously? No \"thank you?\""
        elif Player.Party[0] == StormX:
            ch_s "Oh, I'm sorry if I was presumptuous. . ."
        elif Player.Party[0] == JubesX:
            ch_v "Sorry, sorry! I was a little hungry. . ."
    else:
        if Player.Party[0] == RogueX:
            ch_r "Heh, I can tell you're awake, [RogueX.player_petname]. . ."
            ch_r "You've been. . . more responsive."
        elif Player.Party[0] == KittyX:
            ch_k "You can stop faking it, [KittyX.player_petname]. . ."
            ch_k "This guy's telling me you're awake now."
        elif Player.Party[0] == EmmaX:
            ch_e "I don't know who you think you're fooling."
            ch_e "You've been awake for a while, [EmmaX.player_petname]. . ."
        elif Player.Party[0] == LauraX:
            ch_l "You can stop playing dead, [LauraX.player_petname]. . ."
            ch_l "Oldest trick in the book."
        elif Player.Party[0] == JeanX:
            ch_j "You can stop pretending to be asleep. . ."
            ch_j "I can't read your mind, but I can read your dick. . ."
        elif Player.Party[0] == StormX:
            ch_s "I didn't intend to wake you, but it seems I have."
        elif Player.Party[0] == JubesX:
            ch_v "Oh, g'morning sleepyhead. . ."


    if Partner:

        if line == "question":
            $ Player.Party[1].change_face("_smile", 1)
        elif line == "praise":
            $ Player.Party[1].change_stat("love", 90, 3)
            $ Player.Party[1].change_stat("obedience", 50, 2)
            $ Player.Party[1].change_stat("inhibition", 60, -2)
            $ Player.Party[1].change_face("_smile", 1)
        elif line == "no":
            $ Player.Party[1].change_stat("love", 90, -3)
            $ Player.Party[1].change_stat("obedience", 50, 2)
            $ Player.Party[1].change_stat("inhibition", 60, -2)
            $ Player.Party[1].change_face("_angry", 1,brows = "_confused")

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
            if line != "no":

                $ Player.Party[0].change_face("_smile", 1)
                if Player.Party[0] == RogueX:
                    ch_r "My pleasure."
                elif Player.Party[0] == KittyX:
                    ch_k "Hehe, mmmm. . ."
                elif Player.Party[0] == EmmaX:
                    ch_e "If you insist. . ."
                elif Player.Party[0] == LauraX:
                    ch_l "That's the plan. . ."
                elif Player.Party[0] == JeanX:
                    ch_j "Sure."
                elif Player.Party[0] == StormX:
                    ch_s "I would love to. . ."
                elif Player.Party[0] == JubesX:
                    ch_v "Sure would."
            elif line == "no" and approval_check(Player.Party[0], 1750):

                $ Player.Party[0].change_stat("obedience", 80, 3)
                $ Player.Party[0].change_stat("inhibition", 60, 2)
                $ Player.Party[0].change_face("_bemused")
                if Player.Party[0] == RogueX:
                    ch_r "You're lucky I'm so into you. . ."
                elif Player.Party[0] == KittyX:
                    ch_k "Wha? Well. . . I guess. . ."
                elif Player.Party[0] == EmmaX:
                    ch_e "Do try not to be a prat this time. . ."
                elif Player.Party[0] == LauraX:
                    ch_l "Fine. . ."
                elif Player.Party[0] == JeanX:
                    $ Player.Party[0].change_stat("obedience", 90, 3)
                    ch_j "Whatever."
                elif Player.Party[0] == StormX:
                    ch_s ". . ."
                    ch_s "I suppose I should finish what I start."
                elif Player.Party[0] == JubesX:
                    ch_v "Do you need to ask?"
                $ line = "maybe"
            else:

                $ Player.Party[0].change_face("_angry", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Player.Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Player.Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Player.Party[0] == LauraX:
                    ch_l "No."
                elif Player.Party[0] == JeanX:
                    ch_j "Ha! No."
                elif Player.Party[0] == StormX:
                    ch_s "Well now I am not so motivated. . ."
                elif Player.Party[0] == JubesX:
                    ch_v "No, I think I got enough. . ."
        "Were you more interested in something else?":
            if line != "no":

                $ Player.Party[0].change_face("_sexy", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Ooh, what did you have in mind?"
                elif Player.Party[0] == KittyX:
                    ch_k "Maaaybee. . . like what?"
                elif Player.Party[0] == EmmaX:
                    ch_e "Perhaps. . . What did you have in mind?"
                elif Player.Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Player.Party[0] == JeanX:
                    ch_j "You read my mind. . ."
                elif Player.Party[0] == StormX:
                    ch_s "I would love to. . ."
                elif Player.Party[0] == JubesX:
                    ch_v "Sure, I guess. . ."
                $ line = "sex"
            elif line == "no" and approval_check(Player.Party[0], 1650):

                $ Player.Party[0].change_stat("obedience", 80, 3)
                $ Player.Party[0].change_stat("inhibition", 60, 3)
                $ Player.Party[0].change_face("_bemused", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Well, you're a jerk, but you're a cute jerk."
                    ch_r "What were you thinking?"
                elif Player.Party[0] == KittyX:
                    ch_k "Oh, so you had something {i}else{/i} in mind. . ."
                    ch_k "Like what?"
                elif Player.Party[0] == EmmaX:
                    ch_e "Hmm, second chance [EmmaX.player_petname], what were you considering?"
                elif Player.Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Player.Party[0] == JeanX:
                    ch_j "Oh? Trying to make it up to me?"
                elif Player.Party[0] == StormX:
                    ch_s "Well, I suppose if you were interested. . ."
                elif Player.Party[0] == JubesX:
                    ch_v "I guess?"
                $ line = "sex"
            else:

                $ Player.Party[0].change_face("_angry", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Player.Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Player.Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Player.Party[0] == LauraX:
                    ch_l "No."
                elif Player.Party[0] == JeanX:
                    ch_j "Well I -was,- but then you had to be a dickbag about it."
                elif Player.Party[0] == StormX:
                    ch_s "I am no longer in the mood."
                elif Player.Party[0] == JubesX:
                    ch_v "Lol, no. . ."
        "Sorry, sorry, please continue." if line == "no":
            if approval_check(Player.Party[0], 1450):

                $ Player.Party[0].change_stat("love", 90, 3)
                $ Player.Party[0].change_stat("obedience", 80, 2)
                $ Player.Party[0].change_stat("inhibition", 60, 4)
                $ Player.Party[0].change_face("_bemused", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Well, since you asked so nice. . ."
                elif Player.Party[0] == KittyX:
                    ch_k "I guess I can forgive you. . ."
                elif Player.Party[0] == EmmaX:
                    ch_e "Ok, I'll give you another chance here."
                elif Player.Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Player.Party[0] == JeanX:
                    ch_j ". . . fine."
                elif Player.Party[0] == StormX:
                    ch_s "Fine."
                elif Player.Party[0] == JubesX:
                    ch_v "Yeah, sure."
                $ line = "maybe"
            else:

                $ Player.Party[0].change_stat("love", 90, 2)
                $ Player.Party[0].change_face("_angry", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Player.Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Player.Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Player.Party[0] == LauraX:
                    ch_l "No."
                elif Player.Party[0] == JeanX:
                    ch_j "Nice try."
                elif Player.Party[0] == StormX:
                    ch_s "I am no longer in the mood."
                elif Player.Party[0] == JubesX:
                    ch_v "Nah, I got enough. . ."
        "Sorry, but we could do something else." if line == "no":
            if approval_check(Player.Party[0], 1350):

                $ Player.Party[0].change_stat("love", 90, 3)
                $ Player.Party[0].change_face("_sexy", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Well, since you asked so nice. . ."
                    ch_r "What did you have in mind?"
                elif Player.Party[0] == KittyX:
                    ch_k "I guess, maybe. . ."
                    ch_k "Like what?"
                elif Player.Party[0] == EmmaX:
                    ch_e "Mmm, I'll consider it. . ."
                elif Player.Party[0] == LauraX:
                    ch_l "Yeah, I guess?"
                elif Player.Party[0] == JeanX:
                    ch_j ". . . fine."
                elif Player.Party[0] == StormX:
                    ch_s "I. . . suppose so."
                elif Player.Party[0] == JubesX:
                    ch_v "Sure, I guess. . ."
                $ line = "sex"
            else:

                $ Player.Party[0].change_stat("love", 90, 2)
                $ Player.Party[0].change_face("_angry", 1)
                if Player.Party[0] == RogueX:
                    ch_r "Well not when you're rude to me."
                    ch_r "You can polish yourself off."
                elif Player.Party[0] == KittyX:
                    ch_k "You can't walk that one back!"
                    ch_k "You can take care of that yourself."
                elif Player.Party[0] == EmmaX:
                    ch_e "Not with your attitude."
                    ch_e "I think you can manage to finish this yourself."
                elif Player.Party[0] == LauraX:
                    ch_l "No."
                elif Player.Party[0] == JeanX:
                    ch_j "Nope, too late."
                elif Player.Party[0] == StormX:
                    ch_s "No, I am no longer in the mood."
                elif Player.Party[0] == JubesX:
                    ch_v "Nah. . ."
        "Not when I'm just waking up.":
            $ Player.Party[0].change_face("_angry", 1)
            if Player.Party[0] == RogueX:
                ch_r "Fine, whatever!"
                $ RogueX.eyes = "_side"
                ch_r "[[mumbles] Girl tries to do a favor. . ."
            elif Player.Party[0] == KittyX:
                ch_k "Aw. . ."
                $ KittyX.eyes = "_side"
                ch_k "Last time I do you a favor. . ."
            elif Player.Party[0] == EmmaX:
                ch_e "Hmph. . ."
                $ EmmaX.eyes = "_side"
                ch_e "It's not as though that was for my benefit. . ."
            elif Player.Party[0] == LauraX:
                ch_l "Tsk. . ."
                $ LauraX.eyes = "_side"
                ch_l "\"No free blowjobs,\" got it. . ."
            elif Player.Party[0] == JeanX:
                $ Player.Party[0].change_stat("love", 90, -5)
                $ Player.Party[0].change_stat("obedience", 90, 2)
                ch_j "Seriously? . ."
                $ JeanX.eyes = "_side"
                ch_j "\"Rules, rules, rules\" around here. . ."
            elif Player.Party[0] == StormX:
                ch_s "I can understand."
            elif Player.Party[0] == JubesX:
                ch_v "Ok, ok. . ."
            $ line = "no"



    if line == "no" or line == "sex":
        if Partner:
            $ Partner.change_face("_sexy")
        $ Player.Party[0].recent_history.remove("blanket")
        call show_full_body(Player.Party[0])

        if len(Player.Party) >= 2:
            call move_Girl(Player.Party[1], x_position = 0.7, transition = ease)

        if line == "no":
            if Player.location == "bg_player":
                if Partner:
                    Partner.voice "I'm out of here."
                Player.Party[0].voice "Yeah, me too."
            else:
                Player.Party[0].voice "Oh, get out of here already."




            $ Player.Party = []
            $ Partner = 0


            $ time_index = 3
            $ current_time = time_options[(time_index)]
            $ day -= 1

            if weekday == 0:
                $ weekday = 6
            else:
                $ weekday -= 1

            $ day_of_week = week[weekday]
            call wait

            jump return_player_to_room

        elif line == "sex":
            call shift_focus(Player.Party[0])
            call enter_main_sex_menu(Player.Party[0])
    else:

        $ line = 0
        $ action_speed = 1
        if Partner:
            $ second_girl_main_action = "blowjob"
        call Morning_Partner

        call start_action(Player.Party[0], "blowjob")

    return



label Morning_Partner:

    if not Partner:
        return
    $ Partner.change_face("_sexy")
    call move_Girl(Partner, x_position = 0.7, transition = ease)

    return
