

# Start Call to Fap / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label CalltoFap(Girl=0,Fap=0): #rkeljsv
        #called from EventCalls
        #The girl calls you for permission to fap, 1 is "yes," 2 is "i'll watch," 3 is "i'll visit."

        if "nofap" not in Girl.Traits:
                #if she's allowed to fap, she will
                $ Girl.DrainWord("wannafap",0,1) #removes "wannafap" tag from daily
                $ Girl.AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily
                return

        if Girl.location == bg_current:
                #if she's in the room with you, this won't come up.
                return

        #first girl to pass the above check. . .
        $ EGirls.remove(EGirls[0]) #remove her from the list
        while EGirls:
                #clears out remaining options, if applicable
                if "wannafap" in EGirls[0].daily_history and "nofap" not in EGirls[0].daily_history:
                        #if she's wants to fap and is allowed to, she will
                        $ EGirls[0].AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily
                $ EGirls.remove(EGirls[0])
                #any girls who are under "nofap" orders are out of luck this turn. . .

        $ Player.daily_history.append("fapcall")

        show Cellphone at sprite_location(StageLeft)

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
                ch_j "Hey [JeanX.Petname]. . ."
                ch_j "Remember how we agreed that I would hold off on. . ."
                ch_j ". . . on schlicking?"
                ch_j "Well I was just thinking. . ."
                ch_j "Maybe I could anyway?"
        elif Girl == StormX:
                ch_s "[StormX.Petname]. . ."
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
                                    ch_e "Oh, thank you, [EmmaX.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Nice."
                            elif Girl == JeanX:
                                    ch_j "Whew!"
                            elif Girl == StormX:
                                    ch_s ". . . Thank you, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Nice. . ."
                            $ Fap = 1
            "If you really have to. . .":
                    if (Girl.love + Girl.obedience) >= 2*Girl.inhibition:
                            #if she agrees to not do it (love+obedience >= double inhibition)
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("obedience", 60, 3)
                            $ Girl.change_stat("obedience", 80, 1)
                            $ Girl.change_stat("lust", 80, 5)
                            if Girl == RogueX:
                                    ch_r "Oh, well. . .."
                                    ch_r "I suppose I could restrain myself. . ."
                            elif Girl == KittyX:
                                    ch_k "Well, if it really bothers you. . ."
                            elif Girl == EmmaX:
                                    ch_e "I imagine I can find other distractions, [EmmaX.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Hmm. Yeah, whatever. Nevermind."
                            elif Girl == JeanX:
                                    ch_j "Well, I guess I could hold off. . ."
                                    ch_j "I do have -exceptional- self control. . ."
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "I suppose I can contain myself, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Well, I mean. . ."
                                    ch_v "I don't want to disappoint you. . ."
                            $ Girl.Thirst += 10

                    else:
                            #if she insists on doing it
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
                                    ch_s "That is appreciated, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Nice. . ."
                            $ Fap = 1
            "No, you may not.":
                    if Approvalcheck(Girl,600,"O") and (Girl.obedience >= Girl.inhibition):
                            #if she agrees to not do it (obedience >= inhibition)
                            $ Girl.change_stat("love", 50, -5)
                            $ Girl.change_stat("obedience", 60, 5)
                            $ Girl.change_stat("obedience", 200, 2)
                            $ Girl.change_stat("lust", 80, 5)
                            if Approvalcheck(Girl,800,"O"):
                                    $ Girl.change_stat("lust", 200, 5)
                            if Girl == RogueX:
                                    ch_r "Oh, well. . .."
                                    ch_r "I suppose I could restrain myself. . ."
                            elif Girl == KittyX:
                                    ch_k "Well, if it really bothers you. . ."
                            elif Girl == EmmaX:
                                    ch_e "I imagine I can find other distractions, [EmmaX.Petname]."
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
                    elif Approvalcheck(Girl,1000,"LO"):
                            #she is apologetic about it
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
                                    ch_s "I am afraid that I have my limits, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "I'm a little wired right now. . ."
                            $ Girl.Thirst += 10
                            $ Fap = 1
                    else:
                            #if she is mad at you
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
                                    call PsychicFlash(0)
                            elif Girl == StormX:
                                    ch_s ". . ."
                                    ch_s "Well, that is unfortunate, [StormX.Petname]."
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
                                    ch_e "I think you could at that, [EmmaX.Petname]."
                            elif Girl == LauraX:
                                    ch_l "Cool."
                            elif Girl == StormX:
                                    ch_s "I imagine that you could, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "That might be nice."
                            else: #Rogue, Kitty, Jean
                                    call Anyline(Girl,"Oh, you would, would you. . .")
                            $ Fap = 3
            "Only if I can watch." if Alonecheck(): #only works if you're alone
                    if Approvalcheck(Girl, 1200):
                            #She agrees
                            $ Girl.change_stat("love", 80, 4)
                            $ Girl.change_stat("obedience", 60, 2)
                            $ Girl.change_stat("obedience", 80, 2)
                            $ Girl.change_stat("inhibition", 50, 2)
                            $ Girl.change_stat("inhibition", 80, 3)
                            $ Girl.change_stat("lust", 80, 5)
                            if Girl == RogueX: #R_Mast
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
                                    ch_s "I would not mind that, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "Oh, well, I guess that'd be fine. . ."
                            $ Fap = 2
                    else:
                            #she's not into it.
                            $ Girl.change_stat("love", 60, -3)
                            $ Girl.change_stat("obedience", 60, -2)
                            $ Girl.change_stat("inhibition", 80, 3)
                            $ Girl.change_stat("lust", 50, 5)
                            if Girl == RogueX: #R_Mast
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
                                    ch_s "I am uncomfortable with that, [StormX.Petname]."
                            elif Girl == JubesX:
                                    ch_v "I'd uh, prefer you didn't. . ."
                            $ Girl.Thirst += 15

        $ Girl.DrainWord("wannafap",0,1) #removes "wannafap" tag from daily
        hide Cellphone

        if Fap == 3:
                #if you decide to come over. . .
                $ del Options[:]

                $ Girl.location = Girl.Home
                $ bg_current = Girl.Home
                call Taboo_Level(1)

                jump Misplaced

        elif Fap == 2:
                #if you agree to watch her. . .
                $ del Options[:]
                if Girl in (EmmaX,StormX) and Girl.location == "bg_classroom" and time_index >= 2:
                        pass             #if it's Emma and she's in class and it's a good time, stay
                else:
                        $ Girl.location = Girl.Home
                call Taboo_Level(0)
                call PhoneSex(Girl)
                $ renpy.pop_call() #skips past EventCall
        elif Fap:
                #if you agree at some point. . .
                $ Girl.AddWord(1,0,"gonnafap",0,0)  #adds "gonnafap" tag to daily

        $ Options = ["empty"] #sets token entry to prevent a removal failure. . .
        return

            #add history elements
            #add "if girl is watching, "join us." to basic sex menus
# End Call to Fap / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Phone Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label PhoneSex(Girl=0): #rkeljsv
        # called by Eventcalls->CalltoFap
        # make sure to adjust orgasm options to work when you aren't in the room.
        if bg_current != "bg_player":
                "You rush back to your room."
                $ bg_current = "bg_player"
                call Taboo_Level
                call set_the_scene
        if Girl in (EmmaX,JeanX):
                #telepathic sex?
                call MindFuck

        $ Player.AddWord(1,"phonesex","phonesex",0,"phonesex") #Recent and History
        #display the phone sex graphics

        call shift_focus(Girl)
        show PhoneSex zorder 150

        $ Girl.AddWord(1,"phonesex","phonesex",0,"phonesex")  #adds "phonesex" tag to recent and daily actions, and history
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
                ch_k "Mmmmm. . . call any time, [KittyX.Petname]."
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
                ch_s "I believe I've got the camera set up, [StormX.Petname]. . ."
                call Storm_M_Prep
                ch_s "I enjoyed that, thank you. . ."
        elif Girl == JubesX:
                ch_v "Ok, loaded up. . .."
                ch_v "Looking good?"
                call Jubes_M_Prep
                ch_v "Mmmmm. . . call again, [JubesX.Petname]."
                ch_v "I'll be waiting. . ."
        #hide the phone sex graphics

        hide PhoneSex

        call Get_Dressed
        $ Girl.OutfitChange(5) #resets her clothes
        call checkout(1)
        $ Player.recent_history.remove("phonesex")
        return
#add option for girl to strip herself. . .
# End Phone Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#start Call_For_Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Call_For_Les(Girl=0,Girl2=0,Girls=[]): #rkeljsv
        #called by Jumpercheck if girls are lesing and Girl approves

        if Girl not in active_Girls:
                $ Girls = active_Girls[:]
                while Girls and Girl not in active_Girls:
                        if Girls[0] not in Party and Girls[0].location != bg_current and "les" in Girls[0].recent_history:
                                # if this girl is not already the focal girl, is at the current location but not in a party,
                                # and was queued for a les action, set her up as girl 1.
                                $ Girl = Girls[0]
                                $ Girls = [1]
                        $ Girls.remove(Girls[0])
        if Girl in active_Girls and not Girl2:
                #if a Girl was either offered or produced by first loop. . .
                $ Girls = active_Girls[:]
                $ Girls.remove(Girl)
                while Girls:
                        if Girls[0] not in Party and Girls[0].location != bg_current and "les" in Girls[0].recent_history:
                                # if this girl is not already the focal girl, is at the current location but not in a party,
                                # and was queued for a les action, set her up as girl 2.
                                if Approvalcheck(Girls[0], 1600 - Girls[0].SEXP, TabM=0):
                                        $ Girl2 = Girls[0]
                                        $ Girls = [1]
                                else:
                                        return 0
                        $ Girls.remove(Girls[0])
        if Girl not in active_Girls or Girl2 not in active_Girls:
                #if either girl refuses, continue with Jumper check
                return 0

        show Cellphone at sprite_location(StageLeft)

        $ line = 0
        "You get a call from [Girl.name]."
        if Girl == RogueX:
                ch_r "Hey, [Player.name]. . . I was just over here with [Girl2.name] and. . ."
                ch_r "One thing lead to another, you know how that goes. . . and we were just wondering,"
                ch_r "Would you like to come over and join us?"
        elif Girl == KittyX:
                ch_k "Oh, hi, [Girl.Petname]. . . I was just hanging out with [Girl2.name] and. . ."
                ch_k "we got to thinking[Girl.like]"
                ch_k "Did you wanna come over and join us?"
        elif Girl == EmmaX:
                ch_e "[Girl.Petname]. . . I was just here entertaining [Girl2.name]. . ."
                ch_e "One thing lead to another, I'm sure you get the picture. . . and we were just wondering,"
                ch_e "Would you like to come lend us a hand?"
                ch_e "Or other bits. . ."
        elif Girl == LauraX:
                ch_l "Hey, [Player.name]. . . I was with [Girl2.name] here, and. . ."
                ch_l "You know, feeling each other up-"
                call Anyline(Girl2,"Hey!{w=0.3}{nw}")
                ch_l ". . . so . . ."
                ch_l "Want in on this action?"
        elif Girl == JeanX:
                ch_j "Oh, [Girl.Petname]. . . I was hanging out with [Girl2.name]. . ."
                ch_j "Did you want to swing by and pound some sense into her?"
                call Anyline(Girl2,"Hey!{w=0.3}{nw}")
                ch_j ". . ."
        elif Girl == StormX:
                ch_s "Hello, [Girl.Petname]? . . I was having a. . . chat with [Girl2.name]. . ."
                ch_s "We were having a good time, and were wondering if perhaps you wanted to join us?"
        elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.Petname]. . . [Girl2.name]'s over here and. . ."
                ch_v "we were having some fun, and. . ."
                ch_v "Did you want to join us?"
        while not line and line != "what":
                menu:
                    extend ""
                    "Sure, I'll be right there!":
                            $ Girl.change_stat("love", 95, 5)
                            $ Girl.change_stat("obedience", 95, 3)
                            $ Girl.change_stat("inhibition", 95, 2)
                            if Girl in (EmmaX,StormX):
                                ch_e "lovely, see you in a bit."
                            else:
                                call Anyline(Girl,"Cool. See you here.")
                            $ Girl2.change_stat("love", 95, 5)
                            $ Girl2.change_stat("obedience", 95, 3)
                            $ Girl2.change_stat("inhibition", 95, 2)
                            $ line = "yes"
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
                    "What, are you watching a movie?" if line != "what" and Girl != JeanX:
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
                                    ch_r "We're bumpin uglies, [Girl2.Petname]."
                                    ch_r "Thought you might want in."
                            elif Girl2 == KittyX:
                                    $ Girl2.change_stat("inhibition", 80, 2)
                                    ch_k "It's, um. . . sex."
                                    ch_k "We're having sex."
                                    ch_k "-thought you might wanna join us?"
                            elif Girl2 == EmmaX:
                                    ch_e "We're having -intercourse-, [Girl2.Petname]."
                                    ch_e "Did - you - want - to - join - us?"
                            elif Girl2 == LauraX:
                                    ch_l "Sex, dumbass."
                                    ch_l "We're shucking clams over here and wanted someone to bring the meat."
                                    ch_l "You packing, or what?"
                            elif Girl2 == StormX:
                                    ch_s "What she is trying to say is that we were enjoying each other's bodies."
                                    ch_s "Sex, [Girl2.Petname]. We wanted you to join us for sex."
                            elif Girl2 == JubesX:
                                    ch_v "I was eating her out, basically."
                                    ch_v "Did you want in on this?"
                            $ line = "what"
                            #loops back through. . .

        hide Cellphone
        #if you decide to come over. . .
        if bg_current == Girl.Home:
                #swaps girls if for some reason you're in the other one's room
                $ line = Girl
                $ Girl = Girl2
                $ Girl2 = line
        $ Girl.location = Girl.Home
        $ Girl2.location = Girl.Home
        $ bg_current = Girl.Home
        $ Taboo= 0
        $ Girl.Taboo = 0
        $ Girl2.Taboo = 0
        $ line = 0

        $ Girl.DrainWord("les",1,0) #removes general "les" tag from recent actions
        $ Girl2.DrainWord("les",1,0) #removes general "les" tag from recent actions

        $ Girl.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl2.AddWord(0,"lesbian","lesbian")  #adds "lesbian" tag to recent and daily actions
        $ Girl.AddWord(1,0,0,0,"les "+Girl2.Tag)  #adds "les Rogue" tag to recent actions
        $ Girl2.AddWord(1,0,0,0,"les "+Girl.Tag)  #adds "les Kitty" tag to recent actions

        call set_the_scene(0,1,0,0)
        "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
        while line < 2:
            menu:
                extend ""
                "Knock politely":
                        if Girl == RogueX:
                                ch_r "Come on in, [RogueX.Petname]!"
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
                        $ line = 2
                "Peek inside" if line != 1:
                        call set_the_scene
                        $ Girl.change_face("kiss",1,Eyes = "closed")
                        $ Girl2.change_face("kiss",1,Eyes = "closed")
                        $ primary_action = "lesbian"
                        $ primary_action3 = "fondle_pussy"
                        $ primary_action4 = "fondle_pussy"
                        "You see [Girl.name] and [Girl2.name], eyes closed and stroking each other vigorously."
                        $ line = 1
                "Enter quietly":
                        $ line = 2
                "Leave quietly":
                        "You leave the girls to their business and slip out."
                        $ Girl.Thirst -= 30
                        $ Girl.lust = 20
                        $ Girl2.Thirst -= 30
                        $ Girl2.lust = 20
                        $ Girl.change_stat("love", 90, -3)
                        $ Girl2.change_stat("love", 90, -3)
                        $ renpy.pop_call()
                        $ bg_current = "bg_campus"
                        $ line = 0
                        jump Misplaced

        $ line = 0
        $ Girl.change_face("sly",1)
        $ Girl2.change_face("sly",1)
        call set_the_scene(1,0,0,0)  #no clothes or trigger resets
        if Girl == RogueX:
                ch_r "Sorry we got started without you."
        elif Girl == KittyX:
                ch_k "Oh, hey, [KittyX.Petname], we. . . got a little bored."
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
        $ primary_action3 = "fondle_pussy"
        $ primary_action4 = "fondle_pussy"
        $ Partner = Girl2
        call expression Girl.Tag + "_SexAct" pass ("lesbian") #call Rogue_SexAct("lesbian")
        jump Misplaced
        return

#end Call_For_Les / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
