label sleepover(line=0):
    $ Party = []

    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current:
            $ Party.append(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])


    if bg_current == "bg_player" and "met" in StormX.history and "met" not in JubesX.history:

        call clear_the_room ("all", 1, 0)
        "It's getting late, so you go to sleep."
        call Jubes_Meet
        call wait
        return

    if not Party and bg_current == "bg_player":

        call clear_the_room ("all", 1)

        "It's getting late, so you go to sleep."
        if "met" in StormX.history and "met" not in JubesX.history:
            call Jubes_Meet
        call wait
        return

    while len(Party) > 2:

        $ Party.remove(Party[2])

    if day <= 4:

        $ Party = []
    elif Party and Party[0]:
        call shift_focus (Party[0])

    if bg_current != "bg_player":

        $ temp_Girls = all_Girls[:]
        while temp_Girls:
            if temp_Girls[0].home == bg_current:
                if temp_Girls[0] not in Party:

                    "[temp_Girls[0].name] probably wouldn't appreciate you staying over, you head back to your own room."
                    call remove_girl ("all")
                    jump return_player_to_room
                if temp_Girls[0] != Party[0]:
                    $ Party.reverse()
                $ temp_Girls = [1]
            $ temp_Girls.remove(temp_Girls[0])


    if bg_current == "bg_player":
        if len(Party) == 2:
            $ renpy.random.shuffle(Party)
            if approval_check(Party[0],Check=1) <= approval_check(Party[1],Check=1):

                $ Party.reverse()
        if not Party:
            pass
        elif Party[0].event_counter["sleepover"] >= 3 and approval_check(Party[0], 800):
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


    if day <= 4:

        jump return_player_to_room

    if EmmaX in Party:
        if "classcaught" not in EmmaX.history:
            if bg_current == EmmaX.home:
                ch_e "You should probably get going, we wouldn't want any rumors to spread."
                jump return_player_to_room
            else:
                ch_e "I should probably get going, we wouldn't want any rumors to spread."
                call remove_girl (EmmaX)
        elif len(Party) >= 2 and "threesome" not in EmmaX.history:

            if (bg_current == EmmaX.home or bg_current == "bg_player") and approval_check(EmmaX, 1100, "LI"):
                if Party[0] != EmmaX:
                    $ Party.reverse()
                ch_e "[Party[1].name] dear, I need a moment with [Player.name], but you can leave."
                $ Party[1].change_face("_confused",1)
                Party[1].voice "Oh, ok. . ."
                call remove_girl (Party[1])
                ch_e "Sorry about that, but I had to discuss something with you in private."
            else:

                ch_e "Yes, I really should be leaving, don't let me bother you two."
                call remove_girl (EmmaX)
            if "sleeptime" not in EmmaX.history:
                $ EmmaX.history.append("sleeptime")
        if not Party or (EmmaX not in Party and bg_current == EmmaX.home):

            jump return_player_to_room

    $ Party[0].change_face("_sexy",1)

    $ line = 0
    if Party[0].event_counter["sleepover"] >= 3 and approval_check(Party[0], 800):

        if Party[0].home == bg_current:
            Party[0].voice "Are you staying over tonight?"
        else:
            Party[0].voice "I'm staying over, right?"
        $ line = 1

    elif Party[0].event_counter["sleepover"] < 3 and approval_check(Party[0], 1100, "LI"):

        $ Party[0].change_face("_bemused",1)
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
        $ line = 1


    if line:

        menu:
            extend ""
            "Sure.":
                if Party[0].event_counter["sleepover"] <= 5:
                    $ Party[0].change_stat("love", 70, 10)
                    $ Party[0].change_stat("obedience", 80, 10)
                    $ Party[0].change_stat("obedience", 50, 20)
                    $ Party[0].change_stat("inhibition", 25, 20)
                $ Party[0].change_stat("love", 70, 5)
                $ Party[0].change_face("_smile")
            "No, sorry.":


                $ Party[0].change_stat("obedience", 50, 2)
                $ Party[0].change_stat("obedience", 30, 5)
                $ Party[0].change_stat("inhibition", 40, 3)
                $ Party[0].change_face("_sad")
                $ line = 0
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

                $ line = "leave"
            "Ok, see you later then. Good night." if Party[0].home != bg_current:

                $ line = "leave"

            "Are you sure I can't stay the night? . ." if not Party[0].event_counter["sleepover"] and Party[0].home == bg_current:
                $ line = "please"
            "Are you sure you can't stay? . ." if not Party[0].event_counter["sleepover"] and Party[0].home != bg_current:
                $ line = "please"

            "That's not what you said the other night . ." if Party[0].event_counter["sleepover"]:

                if approval_check(Party[0],900)or approval_check(Party[0],700,"L") or approval_check(Party[0],500,"O"):
                    $ Party[0].change_face("_bemused",1)
                    $ line = 1
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
                    $ Party[0].change_face("_smile",brows="_confused")

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


    if line == "leave":

        $ Party[0].change_stat("love", 90, 3)
        $ Party[0].change_stat("inhibition", 25, 2)
        $ Party[0].change_face("_smile")
        $ line = 0
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

    if line == "please":

        if approval_check(Party[0],1000) or approval_check(Party[0],700,"L") or approval_check(Party[0],500,"O"):
            $ Party[0].change_face("_bemused")
            $ line = 1
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
            $ Party[0].change_face("_smile",brows="_confused")
            $ line = 0
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

    if not line:

        if Party[0].home == bg_current:

            call clear_the_room (Party[0], 1)
            jump return_player_to_room
        else:

            call remove_girl (Party[0])
            call sleepover
            return


    if len(Party) >= 2:

        if Party[0].likes[Party[1].tag] >= 700 and approval_check(Party[0], 1200):

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

        if Party[1].likes[Party[0].tag] >= 500 and approval_check(Party[1], 1200):

            $ Party[1].change_face("_smile")
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
            $ line = 1
        else:
            $ Party[0].change_face("_smile",1)
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
            $ line = 0
        menu:
            extend ""
            "You should stay, [Party[1].name].":

                if Party[1].likes[Party[0].tag] >= 500 and approval_check(Party[1], 1200):

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
                    $ line = 1
                    $ Party[0].check_if_likes(Party[1],800,3,1)
                else:
                    $ Party[1].change_face("_sadside",1,mouth="_smile")
                    if Party[1] == RogueX:
                        ch_r "I don't want to be a bother."
                    elif Party[1] == KittyX:
                        ch_k "No way."
                    elif Party[1] == EmmaX:
                        ch_e "I couldn't."
                    elif Party[1] == LauraX:
                        ch_l "Nah."
                    elif Party[1] == JeanX:
                        $ Party[1].change_face("_angry",1,mouth="_smile")
                        ch_j "Oh, so glad I have permission. . ."
                    elif Party[1] == StormX:
                        ch_s "I would not want to intrude."
                    elif Party[1] == JubesX:
                        ch_v ". . . nah, really. . . stuff to do."
                    $ line = 0
                    $ Party[0].check_if_likes(Party[1],700,-5,1)


                if line:
                    if Party[0].likes[Party[1].tag] >= 700 and approval_check(Party[0], 1200):

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
                        $ Party[1].check_if_likes(Party[0],800,5,1)
                    elif Party[0].likes[Party[1].tag] >= 400 and approval_check(Party[0], 1400):

                        $ Party[0].change_face("_sadside",1,mouth="_smile")
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
                        $ Party[0].change_face("_angry",1)
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
                        $ Party[0].check_if_likes(Party[1],700,-5,1)
                        $ Party[1].check_if_likes(Party[0],700,-5,1)
                        $ line = 0
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
                $ line = 0

    if line == 0:

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
            jump return_player_to_room
        call clear_the_room ("all", 1)

        "It's getting late, so you go to sleep."
        call wait
        return

    if bg_current != "bg_player" and bg_current != Party[0].home:

        "You probably shouldn't sleep here, you head back to your own room."
        call remove_girl ("all")
        $ renpy.pop_call()
        jump player_room

    jump sleepover_Morning


label return_player_to_room:
    $ del Party[:]

    $ temp_Girls = all_Girls[:]

    $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        if bg_current != temp_Girls[0].home and temp_Girls[0].location == bg_current:
            "[temp_Girls[0].name] heads out."

            $ temp_Girls[0].location = temp_Girls[0].home

        $ temp_Girls.remove(temp_Girls[0])

    if bg_current != "bg_player":
        "You head back to your room."

    jump player_room




label sleepover_Morning:

    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current and temp_Girls[0] not in Party:
            call remove_girl (temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])

    call shift_focus (Party[0])

    if Party[0] == StormX and not StormX.sleepwear["outfit_active"] and StormX.taboo < 20:

        $ Party[0].change_outfit("nude")
    else:
        $ Party[0].change_outfit("sleepwear")
    $ Party[0].today_outfit_name == Party[0].outfit
    if len(Party) >= 2:

        if Party[1] == StormX and not StormX.sleepwear["outfit_active"] and StormX.taboo < 20:

            $ Party[1].change_outfit("nude")
        else:
            $ Party[1].change_outfit("sleepwear")
        $ Party[1].today_outfit_name == Party[1].outfit
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
            ch_e "lights out."
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
    hide night_mask onlayer nightmask
    $ Player.semen = Player.max_semen
    $ Player.spunk = 0
    $ round = 50

    $ temp_Girls = Party[:]
    while temp_Girls:
        $ temp_Girls[0].remaining_actions = temp_Girls[0].max_actions
        $ temp_Girls.remove(temp_Girls[0])














    call Morningwood_Check

    $ Party[0].change_face("_smile")
    if len(Party) >= 2:
        $ Party[1].change_face("_smile")
    hide night_mask onlayer nightmask
    hide black_screen onlayer black

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
            $ Party[0].blushing = "_blush1"

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
            $ line = "nice"
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
            if approval_check(Party[0], 800, "L"):
                $ Party[0].change_face("_bemused")
            else:
                $ Party[0].change_face("_confused")

            $ line = "fun"
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
                $ line = "nice"
        "You were constantly tossing around.":

            $ Party[0].blushing = "_blush1"
            if approval_check(Party[0], 800, "L") or approval_check(Party[0], 1200):
                $ Party[0].change_face("_bemused")
                Party[0].voice "Hmm?"
            else:
                $ Party[0].change_face("_angry")
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
            $ line = "toss"
        "You need to learn to stick to your side.":

            if Party[0].event_counter["sleepover"] < 5:
                $ Party[0].change_stat("love", 80, -8)
                $ Party[0].change_stat("obedience", 50, 40)
            if approval_check(Party[0], 500, "O"):
                $ Party[0].change_stat("love", 80, -2)
                $ Party[0].change_stat("obedience", 90, 5)
                $ Party[0].change_face("_normal")
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
                $ Party[0].change_face("_angry")
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
            $ line = "toss"

    if not Party[0].event_counter["sleepover"] and line == "nice":
        if Party[0] == RogueX:
            $ Party[0].blushing = "_blush1"
            ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
            ch_r "Makes me want to do it again sometime."
        elif Party[0] == KittyX:
            $ Party[0].blushing = "_blush2"
            ch_k "Yeah, I. . [KittyX.like]I had fun too."
            $ Party[0].blushing = "_blush1"
            ch_k "I wouldn't[KittyX.like]mind doing it again."
            $ Party[0].blushing = "_blush2"
            ch_k "You know, some other time. . . "
            $ Party[0].blushing = "_blush1"
        elif Party[0] == EmmaX:
            $ Party[0].change_face("_smile",1)
            ch_e "You're a hopeless romantic, [EmmaX.player_petname]."
            $ Party[0].change_face("_smile",2,eyes="_side")
            ch_e "I suppose I can be a bit hopeless too. . ."
        elif Party[0] == LauraX:
            $ Party[0].change_face("_confused",1)
            ch_l "Oh. . ."
            $ Party[0].change_face("_surprised",2,brows="_confused")
            ch_l "Yeah, so did I, now that you mention it. . ."
            $ Party[0].change_face("_confused",1)
            ch_l "Huh."
        elif Party[0] == JeanX:
            $ Party[0].change_face("_confused",1)
            ch_j "Huh? . ."
            ch_j "Oh, yeah. . . it was great. . ."
            $ Party[0].change_face("_smile",1)
        elif Party[0] == StormX:
            $ Party[0].change_face("_smile",1)
            ch_s "Well, yes, it was nice to sleep next to you as well, [StormX.player_petname]."
            $ Party[0].change_face("_smile",2,eyes="_leftside")
            ch_s "I think we should make a habit of this. . ."
            $ Party[0].change_face("_smile",1)
        elif Party[0] == JubesX:
            $ Party[0].change_face("_smile",1)
            ch_v "Yeah, I enjoyed it too. . ."
            $ Party[0].change_face("_sad",1)
            ch_v "I haven't really been sleeping much since. . ."
            $ Party[0].change_face("_sadside",1)
            ch_v ". . . the change."
            $ Party[0].change_face("_smile",1)
            ch_v "It's nice having someone to stay with me. . ."

    $ Party[0].blushing = ""

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
                $ Party[1].blushing = "_blush1"

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
                $ line = "nice"
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
                if approval_check(Party[1], 800, "L"):
                    $ Party[1].change_face("_bemused")
                else:
                    $ Party[1].change_face("_confused")

                $ line = "fun"
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
                    $ line = "nice"

            "You were constantly tossing around, [Party[1].name]." if line == "toss":
                $ line = "toss"
            "You were tossing around constantly too, [Party[1].name]." if line != "toss":
                $ line = "toss"

            "You need to learn to stick to your side, [Party[1].name]." if line == "toss":
                $ line = "turn"
            "And you need to learn to stick to your side too, [Party[1].name]." if line != "toss":
                $ line = "turn"

        if not Party[1].event_counter["sleepover"] and line == "nice":
            if Party[1] == RogueX:
                $ Party[1].blushing = "_blush1"
                ch_r "Aw, that's right sweet of ya, [RogueX.player_petname]."
                ch_r "I think I'd want to do that again."
                ch_r "And, uh, you too, [Party[0].name]."
            elif Party[1] == KittyX:
                $ Party[1].blushing = "_blush2"
                ch_k "Yeah, I. . [KittyX.like]I had fun too."
                $ Party[1].blushing = "_blush1"
                ch_k "I wouldn't[KittyX.like]mind doing it again."
                $ Party[1].blushing = "_blush2"
                ch_k "You know, some other time. . . "
                $ Party[1].blushing = "_blush1"
                ch_k "And[KittyX.like]you too, [Party[0].name]."
            elif Party[1] == EmmaX:
                $ Party[1].change_face("_smile",1)
                ch_e "You're a hopeless romantic, [EmmaX.player_petname]."
                $ Party[1].change_face("_smile",2,eyes="_side")
                ch_e "I suppose I can be a bit hopeless too. . ."
                ch_e "You know what I'm talking about, [Party[0].name]."
            elif Party[1] == LauraX:
                $ LauraX.change_face("_confused",1)
                ch_l "Oh. . ."
                $ Party[1].change_face("_surprised",2,brows="_confused")
                ch_l "Yeah, so did I, now that you mention it. . ."
                $ Party[1].change_face("_confused",1)
                ch_l "Huh."
                ch_l "Weird, right, [Party[0].name]?"
            elif Party[1] == JeanX:
                $ Party[1].change_face("_confused",1)
                ch_j "Huh? . ."
                ch_j "Oh, yeah. . . it was great. . ."
                $ Party[0].change_face("_smile",1)
            elif Party[1] == StormX:
                $ Party[1].change_face("_smile",1)
                ch_s "Well, yes, it was nice to sleep next to you as well, [StormX.player_petname]."
                $ Party[1].change_face("_smile",2,eyes="_leftside")
                ch_s "I think we should make a habit of this. . ."
                $ Party[1].change_face("_smile",1)
            elif Party[1] == JubesX:
                $ Party[1].change_face("_smile",1)
                ch_v "Yeah, I enjoyed it too. . ."
                $ Party[1].change_face("_sad",1)
                ch_v "I haven't really been sleeping much since. . ."
                $ Party[1].change_face("_sadside",1)
                ch_v ". . . the change."
                $ Party[1].change_face("_smile",1)
                ch_v "It's nice having someone to stay with me. . ."


        elif line == "toss":
            $ Party[1].blushing = "_blush1"
            if approval_check(Party[1], 800, "L") or approval_check(Party[1], 1200):
                $ Party[1].change_face("_bemused")
                Party[1].voice "Hmm?"
            else:
                $ Party[1].change_face("_angry")
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
        elif line == "turn":
            if Party[1].event_counter["sleepover"] < 5:
                $ Party[1].change_stat("love", 80, -8)
                $ Party[1].change_stat("obedience", 50, 40)
            if approval_check(Party[1], 500, "O"):
                $ Party[1].change_stat("love", 80, -2)
                $ Party[1].change_stat("obedience", 90, 5)
                $ Party[1].change_face("_normal")
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
                $ Party[1].change_face("_angry")
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

        $ Party[1].blushing = ""



    if len(Party) >= 2:
        $ Party[1].event_counter["sleepover"] += 1


    $ Party[0].event_counter["sleepover"] += 1




    $ time_index = 3
    $ current_time = time_options[(time_index)]
    $ day -= 1

    if weekday == 0:
        $ weekday = 6
    else:
        $ weekday -= 1

    $ day_of_week = week[weekday]

    call wait

    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if "leaving" in temp_Girls[0].recent_history or temp_Girls[0].location == bg_current:


            $ Party.append(temp_Girls[0])
            $ temp_Girls[0].location = bg_current
            if "leaving" in temp_Girls[0].recent_history:
                $ temp_Girls[0].recent_history.remove("leaving")
        if "morningwood" in temp_Girls[0].traits:

            $ temp_Girls[0].recent_history.append("blowjob")
            $ temp_Girls[0].daily_history.append("blowjob")
            $ temp_Girls[0].daily_history.append("morningwood")
            $ temp_Girls[0].traits.remove("morningwood")
        $ temp_Girls.remove(temp_Girls[0])



    if Party:
        $ Party[0].change_face("_normal")
        $ Party[0].change_outfit(6, outfit_changed = True)

        if len(Party) >= 2:
            $ Party[1].change_face("_normal")
            $ Party[1].change_outfit(6, outfit_changed = True)

            "The girls get changed for the day."
        else:
            "[Party[0].name] gets changed for the day."

    $ Party = []







    call girls_location
    return









label Morningwood_Check(Girls=[0,-3], D20=0):



    $ D20 = renpy.random.randint(0,3)
    $ line = 0

    if len(Party) >= 2:

        if Party[0].likes[Party[1].tag] >= 900:

            $ Girls[0] = 2
        elif Party[0].likes[Party[1].tag] >= 750:

            $ Girls[0] = 0
        elif Party[0].likes[Party[1].tag] <= 400:

            $ Girls[0] = 2
        else:
            $ Girls[0] = 0

        if Party[1].likes[Party[0].tag] >= 900:

            $ Girls[1] = 2
        elif Party[1].likes[Party[0].tag] >= 750:

            $ Girls[1] = 0
        elif Party[1].likes[Party[0].tag] <= 400:

            $ Girls[1] = -5
        else:
            $ Girls[1] = -3
    else:
        $ Girls[0] -= 2


    if "chill" in Party[0].traits:

        $ Girls[0] = 0
    else:
        if Party[0].action_counter["blowjob"] >= 5 or approval_check(Party[0], 900, "I"):
            $ Girls[0] += 3
        elif Party[0].action_counter["blowjob"] and approval_check(Party[0], 900):
            $ Girls[0] += 2
        elif approval_check(Party[0], 1400):
            $ Girls[0] += 2
        elif Party[0].action_counter["blowjob"] or approval_check(Party[0], 900):
            $ Girls[0] += 1

        if "hungry" in Party[0].traits and D20 >= 2:

            $ Girls[0] += 2
        if Party[0].thirst >= 60:

            $ Girls[0] += 2
        elif Party[0].thirst >= 30:

            $ Girls[0] += 1
        if Party[0].lust >= 50:

            $ Girls[0] += 1
        if Party[0].SEXP <= 15:

            $ Girls[0] -= 1


        if Girls[1] >= 0:

            $ Girls[0] += 1


    if JubesX in Party:

        if len(Party) >= 2:
            $ line = "no"
        else:
            return
    elif Girls[0] >= D20:
        $ line = "yes"




    if len(Party) >= 2:
        if Party[1].action_counter["blowjob"] >= 5 or approval_check(Party[1], 900, "I"):
            $ Girls[1] += 3
        elif Party[1].action_counter["blowjob"] and approval_check(Party[1], 900):
            $ Girls[1] += 2
        elif approval_check(Party[1], 1400):
            $ Girls[1] += 2
        elif Party[1].action_counter["blowjob"] or approval_check(Party[1], 900):
            $ Girls[1] += 1

        if "hungry" in Party[1].traits and D20 >= 2:

            $ Girls[1] += 2
        if Party[1].thirst >= 60:

            $ Girls[1] += 2
        elif Party[1].thirst >= 30:

            $ Girls[1] += 1
        if Party[1].lust >= 50:

            $ Girls[1] += 1
        if Party[1].SEXP <= 15:

            $ Girls[1] -= 1


        if Girls[0] >= 0:

            $ Girls[1] += 1


        if Party[1] == JubesX:

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


        if line == "other" and Party[0].likes[Party[1].tag] >= 500 and "chill" not in Party[1].traits:

            $ Party.reverse()
            $ Girls[0] = "yes"
            $ Girls[1] = 0



    if line:

        if line == "no":

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
        elif line == "double":

            $ second_girl_primary_action = "blowjob"
            $ Party[1].recent_history.append("blowjob")
            $ Party[1].daily_history.append("blowjob")
            $ Party[1].daily_history.append("morningwood")
            $ Party[1].traits.append("morningwood")

        $ primary_action = "blowjob"
        $ Party[0].recent_history.append("blowjob")
        $ Party[0].daily_history.append("blowjob")
        $ Party[0].daily_history.append("morningwood")
        $ Party[0].traits.append("morningwood")
        call sleepover_MorningWood

        call Sex_Over (0)
    else:



        pass

    return






label sleepover_MorningWood:

    $ Player.add_word(1,"interruption")
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
            show Rogue_sprite standing:
                pos (900,250)
        elif Partner == KittyX:
            show Kitty_sprite standing:
                pos (900,250)
        elif Partner == EmmaX:
            show Emma_sprite standing:
                pos (900,250)
        elif Partner == LauraX:
            show Laura_sprite standing:
                pos (900,250)
        elif Partner == JeanX:
            show Jean_sprite standing:
                pos (900,250)
        elif Partner == StormX:
            show Storm_sprite standing:
                pos (900,250)
        elif Partner == JubesX:
            show Jubes_sprite standing:
                pos (900,250)
        $ Partner.recent_history.append("threesome")

    $ Party[0].recent_history.append("blanket")
    call blowjob_launch(Party[0])

    $ Party[0].change_face("_closed",1)
    if Partner:
        $ Partner.change_face("_closed",1,mouth="_tongue")

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

    hide night_mask onlayer nightmask
    hide black_screen onlayer black

    $ action_speed = 3
    $ Count = 3
    $ line = 0
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
    $ Party[0].blushing = "_blush1"
    if second_girl_primary_action:
        "[Party[0].name] pulls back with a pop and [Party[1].name] sits back."
        $ second_girl_primary_action = None
    else:
        "[Party[0].name] pulls back with a pop."
    if line == "question":
        $ Party[0].change_face("_smile",1)
        if Party[0] == RogueX:
            ch_r "Well I ain't whistlin Dixie, [RogueX.player_petname]."
        elif Party[0] == KittyX:
            ch_k "I wasn't[KittyX.like]being subtle about it, [KittyX.player_petname]."
        elif Party[0] == EmmaX:
            ch_e "Surely your education hasn't been that poor, [EmmaX.player_petname]."
        elif Party[0] == LauraX:
            ch_l "Guess."
        elif Party[0] == JeanX:
            $ Party[0].change_face("_confused",1)
            $ action_speed = 2
            ch_j ". . ."
            ch_j "I 'ave orr dick, in ey 'outh. . ."
            ch_j "Are u 'rain 'amaged?"
            $ action_speed = 1
            if Partner:
                $ Party[0].eyes = "_leftside"
                ch_j "Is he brain damaged?"
            $ Party[0].change_face("_sly",1)
        elif Party[0] == StormX:
            ch_s "I didn't intend to wake you. . ."
        elif Party[0] == JubesX:
            ch_v "Sorry, I. . . hadn't had breakfast. . ."
    elif line == "praise":
        $ Party[0].change_face("_smile",1)
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
    elif line == "no":
        $ Party[0].change_stat("love", 90, -3)
        $ Party[0].change_stat("obedience", 50, 2)
        $ Party[0].change_stat("inhibition", 60, -2)
        $ action_speed = 0
        $ Party[0].change_face("_angry",1,brows="_confused")
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

        if line == "question":
            $ Party[1].change_face("_smile",1)
        elif line == "praise":
            $ Party[1].change_stat("love", 90, 3)
            $ Party[1].change_stat("obedience", 50, 2)
            $ Party[1].change_stat("inhibition", 60, -2)
            $ Party[1].change_face("_smile",1)
        elif line == "no":
            $ Party[1].change_stat("love", 90, -3)
            $ Party[1].change_stat("obedience", 50, 2)
            $ Party[1].change_stat("inhibition", 60, -2)
            $ Party[1].change_face("_angry",1,brows="_confused")

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

                $ Party[0].change_face("_smile",1)
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
            elif line == "no" and approval_check(Party[0], 1750):

                $ Party[0].change_stat("obedience", 80, 3)
                $ Party[0].change_stat("inhibition", 60, 2)
                $ Party[0].change_face("_bemused")
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
                $ line = "maybe"
            else:

                $ Party[0].change_face("_angry",1)
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
            if line != "no":

                $ Party[0].change_face("_sexy",1)
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
                $ line = "sex"
            elif line == "no" and approval_check(Party[0], 1650):

                $ Party[0].change_stat("obedience", 80, 3)
                $ Party[0].change_stat("inhibition", 60, 3)
                $ Party[0].change_face("_bemused",1)
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
                $ line = "sex"
            else:

                $ Party[0].change_face("_angry",1)
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
        "Sorry, sorry, please continue." if line == "no":
            if approval_check(Party[0], 1450):

                $ Party[0].change_stat("love", 90, 3)
                $ Party[0].change_stat("obedience", 80, 2)
                $ Party[0].change_stat("inhibition", 60, 4)
                $ Party[0].change_face("_bemused",1)
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
                $ line = "maybe"
            else:

                $ Party[0].change_stat("love", 90, 2)
                $ Party[0].change_face("_angry",1)
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
        "Sorry, but we could do something else." if line == "no":
            if approval_check(Party[0], 1350):

                $ Party[0].change_stat("love", 90, 3)
                $ Party[0].change_face("_sexy",1)
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
                $ line = "sex"
            else:

                $ Party[0].change_stat("love", 90, 2)
                $ Party[0].change_face("_angry",1)
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
            $ Party[0].change_face("_angry",1)
            if Party[0] == RogueX:
                ch_r "Fine, whatever!"
                $ RogueX.eyes = "_side"
                ch_r "[[mumbles] Girl tries to do a favor. . ."
            elif Party[0] == KittyX:
                ch_k "Aw. . ."
                $ KittyX.eyes = "_side"
                ch_k "Last time I do you a favor. . ."
            elif Party[0] == EmmaX:
                ch_e "Hmph. . ."
                $ EmmaX.eyes = "_side"
                ch_e "It's not as though that was for my benefit. . ."
            elif Party[0] == LauraX:
                ch_l "Tsk. . ."
                $ LauraX.eyes = "_side"
                ch_l "\"No free blowjobs,\" got it. . ."
            elif Party[0] == JeanX:
                $ Party[0].change_stat("love", 90, -5)
                $ Party[0].change_stat("obedience", 90, 2)
                ch_j "Seriously? . ."
                $ JeanX.eyes = "_side"
                ch_j "\"Rules, rules, rules\" around here. . ."
            elif Party[0] == StormX:
                ch_s "I can understand."
            elif Party[0] == JubesX:
                ch_v "Ok, ok. . ."
            $ line = "no"



    if line == "no" or line == "sex":
        if Partner:
            $ Partner.change_face("_sexy")
        $ Party[0].recent_history.remove("blanket")
        call reset_position(Party[0])

        if len(Party) >= 2:
            if Party[1] == RogueX:
                show Rogue_sprite standing:
                    ease 1 pos (700,50)
                show Rogue_sprite standing:
                    pos (700,50)
            elif Party[1] == KittyX:
                show Kitty_sprite standing:
                    ease 1 pos (700,50)
                show Kitty_sprite standing:
                    pos (700,50)
            elif Party[1] == EmmaX:
                show Emma_sprite standing:
                    ease 1 pos (700,50)
                show Emma_sprite standing:
                    pos (700,50)
            elif Party[1] == LauraX:
                show Laura_sprite standing:
                    ease 1 pos (700,50)
                show Laura_sprite standing:
                    pos (700,50)
            elif Party[1] == JeanX:
                show Jean_sprite standing:
                    ease 1 pos (700,50)
                show Jean_sprite standing:
                    pos (700,50)
            elif Party[1] == StormX:
                show Storm_sprite standing:
                    ease 1 pos (700,50)
                show Storm_sprite standing:
                    pos (700,50)
            elif Party[1] == JubesX:
                show Jubes_sprite standing:
                    ease 1 pos (700,50)
                show Jubes_sprite standing:
                    pos (700,50)

        if line == "no":
            if bg_current == "bg_player":
                if Partner:
                    Partner.voice "I'm out of here."
                Party[0].voice "Yeah, me too."
            else:
                Party[0].voice "Oh, get out of here already."




            $ Party = []
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
            call shift_focus(Party[0])
            jump enter_main_sex_menu
    else:

        $ line = 0
        $ action_speed = 1
        $ action_context = None
        if Partner:
            $ second_girl_primary_action = "blowjob"
        call Morning_Partner

        $ Girl = Party[0]
        $ primary_action = "blowjob"

        call action

    return



label Morning_Partner:

    if not Partner:
        return
    $ Partner.change_face("_sexy")
    if Partner == RogueX:
        show Rogue_sprite standing:
            ease 1 pos (700,50)
        show Rogue_sprite standing:
            pos (700,50)
    elif Partner == EmmaX:
        show Emma_sprite standing:
            ease 1 pos (700,50)
        show Emma_sprite standing:
            pos (700,50)
    elif Partner == KittyX:
        show Kitty_sprite standing:
            ease 1 pos (700,50)
        show Kitty_sprite standing:
            pos (700,50)
    elif Partner == LauraX:
        show Laura_sprite standing:
            ease 1 pos (700,50)
        show Laura_sprite standing:
            pos (700,50)
    elif Partner == JeanX:
        show Jean_sprite standing:
            ease 1 pos (700,50)
        show Jean_sprite standing:
            pos (700,50)
    elif Partner == StormX:
        show Storm_sprite standing:
            ease 1 pos (700,50)
        show Storm_sprite standing:
            pos (700,50)
    elif Partner == JubesX:
        show Jubes_sprite standing:
            ease 1 pos (700,50)
        show Jubes_sprite standing:
            pos (700,50)
    return
