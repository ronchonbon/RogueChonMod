
label AskDateOther:

    if Girl not in Player.Harem:
        return
    menu:
        "Have you considered letting me date. . ."
        "[RogueX.name]" if Girl != RogueX and RogueX not in Player.Harem:
            call Poly_Start (RogueX, 1, Girl)
        "[KittyX.name]" if Girl != KittyX and KittyX not in Player.Harem and "met" in KittyX.history:
            call Poly_Start (KittyX, 1, Girl)
        "[EmmaX.name]" if Girl != EmmaX and EmmaX not in Player.Harem and "met" in EmmaX.history:
            call Poly_Start (EmmaX, 1, Girl)
        "[LauraX.name]" if Girl != LauraX and LauraX not in Player.Harem and "met" in LauraX.history:
            call Poly_Start (LauraX, 1, Girl)
        "[JeanX.name]" if Girl != JeanX and JeanX not in Player.Harem and "met" in JeanX.history:
            call Poly_Start (JeanX, 1, Girl)
        "[StormX.name]" if Girl != StormX and StormX not in Player.Harem and "met" in StormX.history:
            call Poly_Start (StormX, 1, Girl)
        "[JubesX.name]" if Girl != JubesX and JubesX not in Player.Harem and "met" in JubesX.history:
            call Poly_Start (JubesX, 1, Girl)
        "Never mind":
            pass
    return


label Les_Interupted(Girl=0, temp_Girls=[]):
    $ Girl = check_girl(Girl)

    if "unseen" not in Girl.recent_history:
        if Girl.event_counter["orgasmed"]< 3 and Girl.remaining_actions:
            menu:
                "Did you want to stop them?"
                "Yeah.":
                    pass
                "No, let them keep going.":
                    $ Girl.remaining_actions -= 1 if Girl.remaining_actions > 0 else 0
                    jump Les_Cycle
        else:
            if Girl == LauraX:
                ch_l "Ahhh, that hit the spot. . ."
            else:
                Girl.voice "Ok, that's probably enough of that. . ."
        jump Les_After
    $ Girl.drain_word("unseen",1,0)
    $ Partner.drain_word("unseen",1,0)

    $ Girl.change_face("_surprised", 1)
    $ Partner.change_face("_surprised",2)

    "Suddenly, [Girl.name] jerks up from what she was doing with a start, and gives [Partner.name] a nudge."
    $ Girl.change_face("_bemused", 0)
    $ Partner.change_face("_perplexed",1)

    if Girl == RogueX:
        ch_r "Um, [Player.name], how long have you been watchin?"
    elif Girl == KittyX:
        ch_k "Eep! [Player.name], how long have you been there?!"
    elif Girl == EmmaX:
        ch_e "Hmm? [Girl.player_petname], enjoying the show?"
    elif Girl == LauraX:
        ch_l "Oh! Hey [Player.name], how long have you been there?"
    elif Girl == JeanX:
        ch_j "Oh, hey [Player.name], get a good look?"
    elif Girl == StormX:
        ch_s "Oh? Hello [Girl.player_petname]. Were you there long?"
    elif Girl == JubesX:
        ch_v "Oh? hey [Girl.player_petname]. What'd you see?"
    $ Girl.remaining_actions -= 1 if Girl.remaining_actions > 0 else 0
    call checkout(total = True)
    $ line = 0


    if Player.secondary_action == "jerking_off":
        $ Girl.eyes = "_down"
        if Girl == RogueX:
            ch_r "And why is your cock out like that?!"
        elif Girl == KittyX:
            ch_k "and why are you fapping?!"
        elif Girl == EmmaX:
            ch_e "and was. . . that. . really an appropriate reaction?"
        elif Girl == LauraX:
            ch_l "Looks like you're taking care of yourself."
        elif Girl == JeanX:
            ch_j "You seem to be enjoying yourself. . ."
        elif Girl == StormX:
            ch_s "It appears you kept yourself busy."
        elif Girl == JubesX:
            ch_v "Looks like it got your attention."
        menu:
            extend ""
            "Yeah, it was an excellent show.":
                $ Girl.change_face("_sexy")
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("obedience", 70, 2)
                "[Girl.name] glances over at [Partner.name]."
                if Girl == RogueX:
                    ch_r "Well, I imagine it was. . ."
                elif Girl == KittyX:
                    ch_k "I mean, I guess. . ."
                elif Girl == EmmaX:
                    ch_e "I suppose it was. . ."
                elif Girl == LauraX:
                    ch_l "I get that. . ."
                elif Girl == JeanX:
                    ch_j "Yeah, she's ok. . ."
                elif Girl == StormX:
                    ch_s "Yes, I suppose so."
                elif Girl == JubesX:
                    ch_v "Hear that? We're stars."
                if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                    $ approval_bonus += 10
                    $ Girl.change_stat("lust", 90, 5)
                    if Girl == RogueX:
                        ch_r "And the view from this angle ain't so bad either. . ."
                    elif Girl == KittyX:
                        ch_k "And[Girl.like]you're not so bad yourself. . ."
                    elif Girl == EmmaX:
                        ch_e "And at least you make good eye candy. . ."
                    elif Girl == LauraX:
                        ch_l "You're not so bad to look at either. . ."
                    elif Girl == JeanX:
                        ch_j "You're looking good too. . "
                    elif Girl == StormX:
                        ch_s "And you might make a fine addition. . ."
                    elif Girl == JubesX:
                        ch_v "Care to join us?"
            "I. . . just got here?":


                $ Girl.change_face("_angry")
                $ Girl.change_stat("love", 70, 2)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 70, 2)
                "She looks pointedly at your cock,"
                if Girl == RogueX:
                    ch_r "Suuure . . ."
                elif Girl == KittyX:
                    ch_k "Riiight. . ."
                elif Girl == EmmaX:
                    ch_e "I'm sure. . ."
                elif Girl == LauraX:
                    ch_l "Uh HUH. . ."
                elif Girl == JeanX:
                    ch_j "Sure. . ."
                elif Girl == StormX:
                    ch_s "I believe you."
                elif Girl == JubesX:
                    ch_v "Of course you did."
                if Girl.love >= 800 or Girl.obedience >= 500 or Girl.inhibition >= 500:
                    $ approval_bonus += 10
                    $ Girl.change_stat("lust", 90, 5)
                    $ Girl.change_face("_bemused", 1)
                    if Girl == RogueX:
                        ch_r "-but I guess we were pretty tempting. . ."
                    elif Girl == KittyX:
                        ch_k "-I can't exactly blame you though. . ."
                    elif Girl == EmmaX:
                        ch_e "not that I can blame you. . ."
                    elif Girl == LauraX:
                        ch_l "-can't blame you though."
                    elif Girl == JeanX:
                        ch_j "You missed some fun stuff. . ."
                    elif Girl == StormX:
                        ch_s ". . . but it's too bad you missed the fun."
                    elif Girl == JubesX:
                        ch_v "Too bad you missed the fun. . ."
                else:
                    $ approval_bonus -= 10
                    $ Girl.change_stat("lust", 200, -5)

        call Seen_First_Peen (Girl, Partner)
    else:


        menu:
            extend ""
            "Long enough.":
                $ Girl.change_face("_sexy", 1)
                $ Girl.change_stat("obedience", 50, 3)
                $ Girl.change_stat("obedience", 70, 2)
                if Girl == RogueX:
                    ch_r "Well I hope you got a good show out of it. . ."
                elif Girl == KittyX:
                    ch_k "I guess we[Girl.like]really put on a show, huh. . ."
                elif Girl == EmmaX:
                    ch_e "I supppose we did make a show of ourselves. . ."
                elif Girl == LauraX:
                    ch_l "Didn't intend to put on a show. . ."
                elif Girl == JeanX:
                    ch_j "I'll bet. . ."
                elif Girl == StormX:
                    ch_s "Yes, I suppose so."
                elif Girl == JubesX:
                    ch_v "Hate to think you missed it. . ."
            "I just got here.":
                $ Girl.change_face("_bemused", 1)
                $ Girl.change_stat("love", 70, 2)
                $ Girl.change_stat("love", 90, 1)
                if Girl == RogueX:
                    ch_r "A likely story . . ."
                elif Girl == KittyX:
                    ch_k "Uh HUH. . ."
                elif Girl == EmmaX:
                    ch_e "I'm sure. . ."
                elif Girl == LauraX:
                    ch_l "Uh HUH. . ."
                elif Girl == JeanX:
                    ch_j "Sure. . ."
                elif Girl == StormX:
                    ch_s "I believe you."
                elif Girl == JubesX:
                    ch_v "Of course you did."
                $ Girl.change_stat("obedience", 50, 2)
                $ Girl.change_stat("obedience", 70, 2)

    if not approval_check(Girl, 1350):

        $ Girl.change_stat("love", 200, -5)
        $ Girl.change_face("_angry")
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
        if Girl == RogueX:
            ch_r "You should get out of here right now, and maybe learn ta knock?"
        elif Girl == KittyX:
            ch_k "So maybe you could[Girl.like]leave us to it?"
        elif Girl == EmmaX:
            ch_e "So perhaps you could leave us to it?"
        elif Girl == LauraX:
            ch_l "So maybe just leave us to it?"
        elif Girl == JeanX:
            ch_j "Ok, so. . . we'd like to get back to it. . ."
        elif Girl == StormX:
            ch_s "If that will be all, I'd like you to leave."
        elif Girl == JubesX:
            ch_v "Ok, but, um, get going now."
        $ renpy.pop_call()
        $ renpy.pop_call()
        if bg_current == "bg_player":
            jump Campus_Map
        else:
            jump player_room

    if round <= 10:

        if Girl == RogueX:
            ch_r "It's getting too late to do much about it right now though."
        elif Girl == KittyX:
            ch_k "We were just about to take a break though."
        elif Girl == EmmaX:
            ch_e "I suppose it was time for a break. . ."
        elif Girl == LauraX:
            ch_l "I guess we could take a break though."
        elif Girl == JeanX:
            ch_j "We could use a break though. . ."
        elif Girl == StormX:
            ch_s "I believe we were just about to take a break though. . ."
        elif Girl == JubesX:
            ch_v "We need to take a minute though. . ."
        return
    $ action_context = "interrupted"

label LesScene(Girl=0, Bonus=0, temp_Girls=[]):
    $ Girl = check_girl(Girl)
    call shift_focus (Girl)

    if not Girl.remaining_actions:

        call Sex_Basic_Dialog (Girl, "tired")
        return

    if Girl.event_counter["seen_with_girl"]:
        $ approval_bonus += 10
    elif Girl.event_counter["been_with_girl"]:
        $ approval_bonus += 5
    if Girl.SEXP >= 50:
        $ approval_bonus += 25
    elif Girl.SEXP >= 30:
        $ approval_bonus += 15
    elif Girl.SEXP >= 15:
        $ approval_bonus += 5

    if Girl.lust >= 90:
        $ approval_bonus += 5
    elif Girl.lust >= 75:
        $ approval_bonus += 5

    elif Girl.inhibition >= 750:
        $ approval_bonus += 5

    if "exhibitionist" in Girl.traits:
        $ approval_bonus += (3*taboo)

    if Girl in Player.Harem or "sex friend" in Girl.player_petnames:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40

    if Partner not in all_Girls:
        $ Partner = 0
        $ temp_Girls = all_Girls[:]
        $ temp_Girls.remove(Girl)
        while temp_Girls:
            if temp_Girls[0].location == bg_current:
                $ Partner = temp_Girls[0]
                $ temp_Girls = [1]
            $ temp_Girls.remove(temp_Girls[0])

    if Girl == JeanX:

        call Girl_Whammy (Partner)
    elif Partner == JeanX:

        call Girl_Whammy (Girl)

    $ line = Girl.likes[Partner.tag]
    if line >= 900:
        $ Bonus += 150
    elif line >= 800 or "poly "+Partner.tag in Girl.traits:
        $ Bonus += 100
    elif line >= 700:
        $ Bonus += 50
    elif line <= 200:
        $ Bonus -= 200
    elif line <= 500:
        $ Bonus -= 100
    $ Partner.drain_word("unseen",1,0)
    $ line = 0

    $ Girl.add_word(1,"noticed "+Partner.tag,"noticed "+Partner.tag)
    $ Partner.add_word(1,"noticed "+Girl.tag,"noticed "+Girl.tag)

    if bg_current in personal_rooms:
        $ taboo = 0
        $ Girl.taboo = 0
        $ Partner.taboo = 0
    if Girl.event_counter["forced"] and not Girl.forced:
        $ approval_bonus -= 5*Girl.event_counter["forced"]

    $ approval = approval_check(Girl, 1350, taboo_modifier = 2, Bonus = Bonus)

    $ Girl.drain_word("unseen",1,0)

    if action_context == "interrupted":
        menu:
            extend ""
            "I guess I should probably get going then. . .":
                $ Girl.change_stat("love", 80, 3)
                if approval >= 2:

                    if Girl == RogueX:
                        ch_r "Well, I didn't say you had to leave. . ."
                    elif Girl == KittyX:
                        ch_k "Hmmmm, I don't know about that. . ."
                    elif Girl == EmmaX:
                        ch_e "Well, if [Partner.tag]'s game. . ."
                    elif Girl == LauraX:
                        ch_l "Hmmmm, I don't know about that. . ."
                    elif Girl == JeanX:
                        ch_j "Well, you don't -have- to. . ."
                    elif Girl == StormX:
                        ch_s "That really won't be necessary."
                    elif Girl == JubesX:
                        ch_v "Orrr. . . you could join us?"
                    call Les_Response (Partner, Girl, 3, B2=Bonus)
                    if not _return:
                        return
                else:

                    call Les_Response (Partner, Girl, 1, B2=Bonus)
                    if not _return:

                        if approval:
                            if Girl == RogueX:
                                ch_r "I mean, you can hang out. . ."
                            elif Girl == KittyX:
                                ch_k "You could at least stick around. . ."
                            elif Girl == EmmaX:
                                ch_e "Well, you could at least stay for a bit. . ."
                            elif Girl == LauraX:
                                ch_l "You could chill here."
                            elif Girl == JeanX:
                                ch_j "Well, you can still stick around. . ."
                            elif Girl == StormX:
                                ch_s "Then you could at least stay and chat for a bit."
                            elif Girl == JubesX:
                                ch_v "Well then, just hang out for a bit."
                            return
                        else:
                            if Girl == RogueX:
                                ch_r "Yeah, that's probably a good idea. . ."
                            elif Girl == KittyX:
                                ch_k "I guess so. . ."
                            elif Girl == EmmaX:
                                ch_e "I suppose. . ."
                            elif Girl == LauraX:
                                ch_l "Yeah. . ."
                            elif Girl == JeanX:
                                ch_j "Oh, fine. . ."
                            elif Girl == StormX:
                                ch_s "I am sorry, [Girl.player_petname]. Perhaps some other time."
                            elif Girl == JubesX:
                                ch_v "Oh, bummer, well see you later then."
                            $ renpy.pop_call()
                            $ renpy.pop_call()
                            if bg_current == "bg_player":
                                jump Campus_Map
                            else:
                                jump player_room
                    elif not approval:

                        if Girl == RogueX:
                            ch_r "I'm sorry [Girl.player_petname], I just am not interested in putting on a show."
                        elif Girl == KittyX:
                            ch_k "Sorry [Girl.player_petname], I guess we'd like to keep this private."
                        elif Girl == EmmaX:
                            ch_e "So sorry [Girl.player_petname], I suppose we'd like to keep this private."
                        elif Girl == LauraX:
                            ch_l "Sorry [Girl.player_petname], maybe come back later."
                        elif Girl == JeanX:
                            ch_j "Hope you enjoyed the show, but we're a little busy. . ."
                        elif Girl == StormX:
                            ch_s "Well I'm afraid that I would rather you didn't stay."
                        elif Girl == JubesX:
                            ch_v "Sorry, not interested."
                        return
                    elif not Girl.remaining_actions:

                        if Girl == RogueX:
                            ch_r "I'm sorry [Girl.player_petname], I'm just too tuckered out right now. . ."
                        elif Girl == KittyX:
                            ch_k "Sorry [Girl.player_petname], I'm kinda worn out already. . ."
                        elif Girl == EmmaX:
                            ch_e "So sorry [Girl.player_petname], I needed a break. . ."
                        elif Girl == LauraX:
                            ch_l "Sorry [Girl.player_petname], looks like we're taking a break. . ."
                        elif Girl == JeanX:
                            ch_j "I could use a break though. . ."
                        elif Girl == StormX:
                            ch_s "I did need to take a brief rest, however."
                        elif Girl == JubesX:
                            ch_v "I'm kinda worn out though."
                        return
                    else:

                        if Girl == RogueX:
                            ch_r "Ok, fine."
                        elif Girl == KittyX:
                            ch_k "Sure."
                        elif Girl == EmmaX:
                            ch_e "Very well."
                        elif Girl == LauraX:
                            ch_l "Sure."
                        elif Girl == JeanX:
                            ch_j "Nice."
                        elif Girl == StormX:
                            ch_s "Oh, excellent."
                        elif Girl == JubesX:
                            ch_v "Nice."

                call shift_focus(Girl)
                jump Les_Prep

            "So maybe I could join you girls?" if Player.semen and Girl.remaining_actions:
                $ Girl.change_face("_sexy")
                if Girl == RogueX:
                    ch_r "Well what did you have in mind?"
                elif Girl == KittyX:
                    ch_k "Mmmm, what would you like?"
                elif Girl == EmmaX:
                    ch_e "Oh? What do you bring to the table?"
                elif Girl == LauraX:
                    ch_l "Oh, you have something to add here?"
                elif Girl == JeanX:
                    ch_j "Oh? Do tell. . ."
                elif Girl == StormX:
                    ch_s "I think that you might. . ."
                elif Girl == JubesX:
                    ch_v "Well, I think we could work with that. . ."
                $ action_context = "join"
                return
            "So maybe I could watch a bit longer?":
                $ Girl.change_face("_bemused", 1)



    if not Girl.event_counter["seen_with_girl"]:
        $ Girl.change_face("_surprised", 1,mouth = "_kiss")
        if Girl == RogueX:
            ch_r "You want me and [Partner.name] to hook up, while you watch?"
        elif Girl == KittyX:
            ch_k "You wanna watch me and [Partner.name] hook up?"
        elif Girl == EmmaX:
            ch_e "You wanna watch me and [Partner.name] \"engaged?\""
        elif Girl == LauraX:
            ch_l "You want to watch me and [Partner.name] hook up?"
        elif Girl == JeanX:
            ch_j "Oh, you'd like to watch me and [Partner.name]?. . ."
        elif Girl == StormX:
            ch_s "Oh, so you would like to see the two of us together?"
        elif Girl == JubesX:
            ch_v "Oh, me and her? Together?"
        if Girl.forced:
            $ Girl.change_face("_sad")
            if Girl == RogueX:
                ch_r "And {i}just{/i} watch?"
            elif Girl == KittyX:
                ch_k "but {i}just{/i} watch, right?"
            elif Girl == EmmaX:
                ch_e "nothing more than that though?"
            elif Girl == LauraX:
                ch_l "{i}Just{/i} watching, right?"
            elif Girl == JeanX:
                ch_j "-Just- watching. . ."
            elif Girl == StormX:
                ch_s "Nothing more than to watch?"
            elif Girl == JubesX:
                ch_v "But just watching though?"


    if approval and (Partner == RogueX or Girl == RogueX) and "touch" not in RogueX.traits:
        if Girl == RogueX:
            ch_r "I don't know, isn't my touch. . . dangerous?"
            ch_p "Don't worry, I can keep it turned off."
            ch_r "I suppose you can. . ."
        elif Girl == KittyX:
            ch_k "I don't know, isn't it kinda. . . dangerous to touch [RogueX.name]?"
            ch_p "Don't worry, I can keep it turned off."
            ch_k "Oh, well I guess. . ."
        elif Girl == EmmaX:
            ch_e "I'm not sure, [RogueX.name]'s touch can be. . . disruptive?"
            ch_p "Don't worry, I can keep it turned off."
            ch_e "Oh, I suppose you can at that. . ."
        elif Girl == LauraX:
            ch_l "I don't know, [RogueX.name]'s touch can be. . . intense. . ."
            ch_p "Don't worry, I can keep it turned off."
            ch_l "Oh, well I guess. . ."
        elif Girl == JeanX:
            ch_j "I guess I can use my TK to avoid direct contact. . ."
        elif Girl == StormX:
            ch_s "I'm unsure, [RogueX.name]'s touch can be a bit of an issue."
            ch_p "Don't worry, I can keep it turned off."
            ch_s "That is true. . ."
        elif Girl == JubesX:
            ch_v "I wouldn't want any trouble with [RogueX.name]'s. . . condition."
            ch_p "Don't worry, I can keep it turned off."
            ch_v "Oh, that'll work."


    if not Girl.event_counter["seen_with_girl"] and approval:

        if Girl.forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
        elif Bonus >= 100:
            $ Girl.change_face("_sly", eyes="_side")
            if Girl == RogueX:
                ch_r "Hmm, actually I might enjoy this more than you think. . ."
            elif Girl == KittyX:
                ch_k "Heh, you don't know what you're asking for. . ."
            elif Girl == EmmaX:
                ch_e "This won't be my first time. . ."
            elif Girl == LauraX:
                ch_l "Well you'd be in for a treat. . ."
            elif Girl == JeanX:
                ch_j "I won't turn down a round with her. . ."
            elif Girl == StormX:
                ch_s "I am certainly more than open to the idea."
            elif Girl == JubesX:
                ch_v "Oh, yeah, no prob."
        elif Girl.love >= (Girl.obedience + Girl.inhibition):
            $ Girl.change_face("_sexy")
            $ Girl.brows = "_sad"
            $ Girl.mouth = "_smile"
            if Girl == RogueX:
                ch_r "I haven't really given much thought to being with other people lately. . ."
            elif Girl == KittyX:
                ch_k "I hadn't really considered putting on a show like this. . ."
            elif Girl == EmmaX:
                ch_e "I hadn't considered this as one of your kinks. . ."
            elif Girl == LauraX:
                ch_l "I hadn't really considered putting on a show like this. . ."
            elif Girl == JeanX:
                ch_j "I don't make a habit of this. . ."
            elif Girl == StormX:
                ch_s "I might if that sort of thing interests you. . ."
            elif Girl == JubesX:
                ch_v "I guess I could be into it."
        elif Girl.obedience >= Girl.inhibition:
            $ Girl.change_face("_normal")
            if Girl == RogueX:
                ch_r "If that's what you want, [Girl.player_petname]. . ."
            elif Girl == KittyX:
                ch_k "If that's what you want, [Girl.player_petname]. . ."
            elif Girl == EmmaX:
                ch_e "If this is what gets you off, [Girl.player_petname]. . ."
            elif Girl == LauraX:
                ch_l "I'm ok with that, [Girl.player_petname]. . ."
            elif Girl == JeanX:
                ch_j "Ok, sure. . ."
            elif Girl == StormX:
                ch_s "I could be convinced. . ."
            elif Girl == JubesX:
                ch_v "If you like that. . ."
        else:
            $ Girl.change_face("_sad")
            $ Girl.mouth = "_smile"
            if Girl == RogueX:
                ch_r "I guess it could be fun with you watching. . ."
            elif Girl == KittyX:
                ch_k "I guess it could be fun with you watching. . ."
            elif Girl == EmmaX:
                ch_e "I do enjoy an audience. . ."
            elif Girl == LauraX:
                ch_l "Not that I mind. . ."
            elif Girl == JeanX:
                ch_j "I wouldn't mind an audience. . ."
            elif Girl == StormX:
                ch_s "I am open to the idea."
            elif Girl == JubesX:
                ch_v "Sure, I guess. . ."


    elif approval:

        if Girl.forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("love", 20, -2, 1)
            if Girl == RogueX:
                ch_r "So you want to watch me with a girl again?"
            elif Girl == KittyX:
                ch_k "You really like this girl-on-girl stuff, huh?"
            elif Girl == EmmaX:
                ch_e "You enjoyed the last show?"
            elif Girl == LauraX:
                ch_l "This is what gets you off?"
            elif Girl == JeanX:
                ch_j "Enjoy the show, uh? . ."
            elif Girl == StormX:
                ch_s "So you enjoy these little plays?"
            elif Girl == JubesX:
                ch_v "This is the kind of thing you like?"
        elif approval and "lesbian" in Girl.recent_history:
            $ Girl.change_face("_sexy", 1)
            if Girl == RogueX:
                ch_r "I guess we could get a little closer. . ."
            elif Girl == KittyX:
                ch_k "A little more wouldn't hurt. . ."
            elif Girl == EmmaX:
                ch_e "Hmm, back for more?"
            elif Girl == LauraX:
                ch_l "I wouldn't mind a little more. . ."
            elif Girl == JeanX:
                ch_j "Ok then, back to it. . ."
            elif Girl == StormX:
                ch_s "Very well. . ."
            elif Girl == JubesX:
                ch_v "I guess we can do that for you. . ."
            call shift_focus(Girl)
            jump Les_Prep
        elif approval and "lesbian" in Girl.daily_history:
            $ Girl.change_face("_sexy", 1)
            $ line = renpy.random.choice(["Enjoyed the show?",
                                    "Didn't get enough earlier?",
                                    "I don't mind having an audience. . ."])
            Girl.voice "[line]"
        elif Girl.event_counter["been_with_girl"] < 3:
            $ Girl.change_face("_sexy", 1)
            $ Girl.brows = "_confused"
            if Girl == RogueX:
                ch_r "You like to watch, huh?"
            elif Girl == KittyX:
                ch_k "You really do like to watch."
            elif Girl == EmmaX:
                ch_e "You do like to watch."
            elif Girl == LauraX:
                ch_l "You do like to watch."
            elif Girl == JeanX:
                ch_j "Can't get enough of me. . ."
            elif Girl == StormX:
                ch_s "So you enjoy these little plays?"
            elif Girl == JubesX:
                ch_v "I don't know. . ."
        else:
            $ Girl.change_face("_sexy", 1)
            $ Girl.arm_pose = 2
            $ line = renpy.random.choice(["You do like to watch.",
                                    "So you'd like us to go again?",
                                    "You want to watch some more?",
                                    "You want me to get it on with "+Partner.tag+"?"])
            Girl.voice "[line]"
        $ line = 0


    if approval >= 2:

        if Girl.forced:
            $ Girl.change_face("_sad")
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            if Girl == RogueX:
                ch_r "Fine, I'm ok with it if she is. . ."
            elif Girl == KittyX:
                ch_k "Well, I guess if she's fine with it. . ."
            elif Girl == EmmaX:
                ch_e "So long as she finds it acceptable. . ."
            elif Girl == LauraX:
                ch_l "Not the worst way to spend some time. . ."
            elif Girl == JeanX:
                ch_j "Well, could be worse. . ."
            elif Girl == StormX:
                ch_s "I suppose a show would not hurt."
            elif Girl == JubesX:
                ch_v "Could be worse. . ."
        else:
            $ Girl.change_face("_sexy", 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            if action_context == "interrupted":
                if Girl == RogueX:
                    ch_r "Well I could do some more. . ."
                elif Girl == KittyX:
                    ch_k "Well I guess we could get back to it. . ."
                elif Girl == EmmaX:
                    ch_e "Well I suppose we could continue. . ."
                elif Girl == LauraX:
                    ch_l "Well I could get back in there. . ."
                elif Girl == JeanX:
                    ch_j "I did want to try a few things. . ."
                elif Girl == StormX:
                    ch_s "Come here then, [Partner.name]."
                elif Girl == JubesX:
                    ch_v "Back to it then?"
            else:
                $ line = renpy.random.choice(["Well. . . ok.",
                                        "I don't mind getting with her. . .",
                                        "A",
                                        "Sure.",
                                        "I guess. . .",
                                        "Heh, ok, fine."])
                if line == "A":
                    if Girl == RogueX:
                        ch_r "I may have needed this anyway. . ."
                    elif Girl == KittyX:
                        ch_k "I kinda needed this anyways. . ."
                    elif Girl == EmmaX:
                        ch_e "I don't mind getting intimate with her. . ."
                    elif Girl == LauraX:
                        ch_l "I kinda needed to blow off some steam. . ."
                    elif Girl == JeanX:
                        ch_j "You haven't seen this one trick she has. . ."
                    elif Girl == StormX:
                        ch_s "You will enjoy this one."
                    elif Girl == JubesX:
                        ch_v "I still needed some attention anyway."
                else:
                    Girl.voice "[line]"
                $ line = 0
        $ Girl.change_stat("obedience", 20, 1)
        $ Girl.change_stat("obedience", 60, 1)
        $ Girl.change_stat("inhibition", 70, 2)
        jump Les_Partner
    else:


        if Girl == RogueX:
            ch_r "I'm not sure about that though, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "I don't know about that, [Girl.player_petname]."
        elif Girl == EmmaX:
            ch_e "I'm not sure about that, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "I don't know, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "Hmm. . . I don't know. . ."
        elif Girl == StormX:
            ch_s "I am unsure. . ."
        elif Girl == JubesX:
            ch_v "Well, but. . ."
        menu:
            "Maybe later?":
                $ Girl.change_face("_sexy", 1)
                if Bonus >= 100:
                    $ Girl.change_stat("inhibition", 90, 5)
                    if Girl == RogueX:
                        ch_r "Well. . . definitely at some point. . ."
                    elif Girl == KittyX:
                        ch_k "I mean, eventually. . ."
                    elif Girl == EmmaX:
                        ch_e "Eventually. . ."
                    elif Girl == LauraX:
                        ch_l "Maybe some other time. . ."
                    elif Girl == JeanX:
                        ch_j "Sure, maybe. . ."
                    elif Girl == StormX:
                        ch_s "Yes, some other time, perhaps."
                    elif Girl == JubesX:
                        ch_v "Sure, maybe."
                elif Bonus >= 0:
                    $ Girl.check_if_likes(Partner,800,3,1)
                    if Girl == RogueX:
                        ch_r "Um, I don't know. . . maybe?"
                    elif Girl == KittyX:
                        ch_k "Um, I don't know. . . maybe?"
                    elif Girl == EmmaX:
                        ch_e "One never knows. . ."
                    elif Girl == LauraX:
                        ch_l "Eh, I don't know. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . maybe. . ."
                    elif Girl == StormX:
                        ch_s "That may be better."
                    elif Girl == JubesX:
                        ch_v "Sure maybe."
                else:
                    $ Girl.change_face("_angry", 1, eyes="_side")
                    if Girl == RogueX:
                        ch_r "Yeah, I really don't see that happening. . ."
                    elif Girl == KittyX:
                        ch_k "Not likely."
                    elif Girl == EmmaX:
                        ch_e "Unlikely."
                    elif Girl == LauraX:
                        ch_l "Probably not."
                    elif Girl == JeanX:
                        ch_j "Not likely. . ."
                    elif Girl == StormX:
                        ch_s "Doubtful."
                    elif Girl == JubesX:
                        ch_v "Doubtful."
                if Girl == RogueX:
                    ch_r "But thanks for being ok with that."
                elif Girl == KittyX:
                    ch_k "Thanks for being cool though. . ."
                elif Girl == EmmaX:
                    ch_e "I do appreciate your restraint."
                elif Girl == StormX:
                    ch_s "I am sorry about that."
                elif Girl == JubesX:
                    ch_v "Sorry."
                $ Girl.change_face("_smile", 1)
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 70, 5)
                call taboo_Level
                return
            "You look like you might be into it. . .":


                if approval:
                    $ Girl.change_face("_sexy")
                    $ Girl.change_stat("obedience", 90, 4)
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("inhibition", 70, 4)
                    $ Girl.change_stat("inhibition", 40, 4)
                    $ line = renpy.random.choice(["Well. . . ok.",
                                        "I don't mind getting with her. . .",
                                        "A",
                                        "Sure.",
                                        "I guess. . .",
                                        "Heh, ok, fine."])
                    if line == "A":
                        if Girl == RogueX:
                            ch_r "I may have needed this anyway. . ."
                        elif Girl == KittyX:
                            ch_k "I kinda needed this anyways. . ."
                        elif Girl == EmmaX:
                            ch_e "I don't mind getting intimate with her. . ."
                        elif Girl == LauraX:
                            ch_l "I kinda needed to blow off some steam. . ."
                        elif Girl == JeanX:
                            ch_j "You haven't seen this one trick she has. . ."
                        elif Girl == StormX:
                            ch_s "You will enjoy this one."
                        elif Girl == JubesX:
                            ch_v "I mean, maybe."
                    else:
                        Girl.voice "[line]"
                    Girl.voice "[line]"
                    $ line = 0
                    jump Les_Partner
            "Just get at it already.":


                $ approval = approval_check(Girl, 550, "OI", taboo_modifier = 2)
                if approval > 1 or (approval and Girl.forced):
                    $ Girl.change_face("_sad")
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("love", 200, -5)
                    if Girl == RogueX:
                        ch_r "Ok, fine. I'll give it a try."
                    elif Girl == KittyX:
                        ch_k "Ok, whatever."
                    elif Girl == EmmaX:
                        ch_e "Oh, fine."
                    elif Girl == LauraX:
                        ch_l "Ok, if you insist."
                    elif Girl == JeanX:
                        ch_j "Oh, fine. . ."
                    elif Girl == StormX:
                        ch_s ". . ."
                    elif Girl == JubesX:
                        ch_v "Fine."
                    $ Girl.change_stat("obedience", 80, 4)
                    $ Girl.change_stat("inhibition", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.forced = 1
                    jump Les_Partner
                else:
                    $ Girl.change_stat("love", 200, -20)
                    $ Girl.recent_history.append("_angry")
                    $ Girl.daily_history.append("_angry")


    call Les_Response (Partner, Girl, 1, B2=Bonus)
    if _return:

        $ Girl.change_face("_smile", 1)
        if Girl == RogueX:
            ch_r "Ok, fine! You've talked me into it."
            ch_r "Get over here. . ."
        elif Girl == KittyX:
            ch_k "Ok, if {i}you{/i} want to."
            ch_k "Commere. . ."
        elif Girl == EmmaX:
            ch_e "Well, if you insist, dear."
            $ Girl.change_face("_sly", 1)
            ch_e "Get over here. . ."
        elif Girl == LauraX:
            ch_l "Ok, if {i}you're{/i} into it."
            ch_l "Get over here. . ."
        elif Girl == JeanX:
            ch_j "Well, you're certainly enthusiastic. . ."
            ch_j "Ok, fine."
        elif Girl == StormX:
            ch_s "Well how could I refuse you, [Partner.name]?"
            ch_s "Very well, get over here. . ."
        elif Girl == JubesX:
            ch_v "Ok, fine, if you're into it."
            ch_v "Come on over here."
        call shift_focus(Girl)
        jump Les_Prep



    $ Girl.arm_pose = 1
    if not Partner:
        if Girl == RogueX:
            ch_r "It would take two to tango, so. . ."
        elif Girl == KittyX:
            ch_k "Seems like she wasn't into it. . ."
        elif Girl == EmmaX:
            ch_e "Well, I can't exactly do this alone. . ."
        elif Girl == LauraX:
            ch_l "I don't know if I should feel insulted. . ."
        elif Girl == JeanX:
            ch_j "We will have -words- later. . ."
        elif Girl == StormX:
            ch_s "I'm afraid that settles that."
        elif Girl == JubesX:
            ch_v "Well, doesn't look like it's happening. . ."
    elif Girl.forced:
        $ Girl.change_face("_angry", 1)
        if Girl == RogueX:
            ch_r "Look, that's just not on the table."
        elif Girl == KittyX:
            ch_k "I'm just not into that."
        elif Girl == EmmaX:
            ch_e "I'm just not into that."
        elif Girl == LauraX:
            ch_l "I'm not into that."
        elif Girl == JeanX:
            ch_j "Seems kinda sketch. . ."
        elif Girl == StormX:
            ch_s "I would prefer something else."
        elif Girl == JubesX:
            ch_v "Just not into it."
        $ Girl.change_stat("lust", 90, 5)
        if Girl.love > 300:
            $ Girl.change_stat("love", 70, -2)
        $ Girl.change_stat("obedience", 50, -2)
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
    elif Girl.taboo > 20:

        $ Girl.change_face("_angry", 1)
        $ Girl.daily_history.append("no_taboo")
        if Girl == RogueX:
            ch_r "Definitely not around here."
        elif Girl == KittyX:
            ch_k "Totally not around here."
        elif Girl == EmmaX:
            ch_e "Totally not around here."
        elif Girl == LauraX:
            ch_l "Not someplace so public."
        elif Girl == JeanX:
            ch_j "I don't think this is the place for it?"
        elif Girl == StormX:
            ch_s "This area may be too public."
        elif Girl == JubesX:
            ch_v "It's too public here."
        $ Girl.change_stat("lust", 90, 5)
        $ Girl.change_stat("obedience", 50, -3)
    elif Girl.event_counter["been_with_girl"]:
        $ Girl.change_face("_sad")
        if Girl == RogueX:
            if Bonus >= 100:
                ch_r "I just don't think I'm ready for that sort of thing."
            else:
                ch_r "I just don't think I'm into that sort of thing."
        elif Girl == KittyX:
            if Bonus >= 100:
                ch_k "I'm not really comfortable with that."
            else:
                ch_k "I don't think I'm ready for an audience."
        elif Girl == EmmaX:
            if Bonus >= 100:
                ch_e "I'm not really comfortable with that."
            else:
                ch_e "I don't think I'm ready for an audience."
        elif Girl == LauraX:
            if Bonus >= 100:
                ch_l "I'm not up for that."
            else:
                ch_l "Not with an audience."
        elif Girl == JeanX:
            if Bonus >= 100:
                ch_j "I'm not cool with that."
            else:
                ch_j "I'd rather you didn't watch."
        elif Girl == StormX:
            if Bonus >= 100:
                ch_s "That's not really something I would want to do."
            else:
                ch_s "I don't think an audience would be appropriate."
        elif Girl == JubesX:
            if Bonus >= 100:
                ch_v "Just not into it."
            else:
                ch_v "I'd rather you weren't involved."
    else:
        $ Girl.change_face("_normal", 1)
        if Girl == RogueX:
            ch_r "Heh, noway, I am {i}not{/i} doing that."
        elif Girl == KittyX:
            ch_k "No way."
        elif Girl == EmmaX:
            ch_e "No way."
        elif Girl == LauraX:
            ch_l "Nope."
        elif Girl == JeanX:
            ch_j "No way. . ."
        elif Girl == StormX:
            ch_s "I'm afraid not."
        elif Girl == JubesX:
            ch_v "Nope."
    $ Girl.recent_history.append("no_lesbian")
    $ Girl.daily_history.append("no_lesbian")
    $ approval_bonus = 0
    call taboo_Level
    return

label Les_Partner:



    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(Girl)
    while temp_Girls:
        if temp_Girls[0].location == bg_current:
            call Les_Response (temp_Girls[0], Girl, 2)
            if not _return:

                return
        $ temp_Girls.remove(temp_Girls[0])


label Les_Prep(Girl=focused_Girl, temp_Girls=[]):

    $ line = 0
    if Girl not in all_Girls or Girl == Partner:
        $ Girl = focused_Girl
        if Girl == Partner:
            $ Partner = 0
            $ line = 1

    if Partner not in all_Girls:
        $ Partner = 0
        $ temp_Girls = all_Girls[:]
        $ temp_Girls.remove(Girl)
        while temp_Girls:
            if temp_Girls[0].location == bg_current:
                $ Partner = temp_Girls[0]
                $ temp_Girls = [1]
            $ temp_Girls.remove(temp_Girls[0])

    if line:

        call shift_focus (Partner)

    $ line = 0

    $ Girl.add_word(1,"noticed "+Partner.tag,"noticed "+Partner.tag)
    $ Partner.add_word(1,"noticed "+Girl.tag,"noticed "+Girl.tag)

    if "unseen" not in Girl.recent_history:

        $ Girl.change_face("_sexy")
        $ Girl.arm_pose = 2
        "[Girl.name] move's closer to [Partner.name] and wraps her arms around her neck."
        if not Girl.event_counter["seen_with_girl"]:

            if Girl.forced:
                $ Girl.change_stat("love", 90, -20)
                $ Girl.change_stat("obedience", 70, 55)
                $ Girl.change_stat("inhibition", 80, 55)
            else:
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_stat("obedience", 70, 20)
                $ Girl.change_stat("inhibition", 80, 60)
        call Les_FirstKiss
        $ girl_secondary_action == "kiss girl"
        $ second_girl_main_action == "kiss girl"

    $ Player.primary_action = "lesbian"
    if action_context:
        $ renpy.pop_call()
        $ action_context = None
    $ line = 0
    if Girl.taboo:
        $ Girl.drain_word("no_taboo")
    $ Girl.drain_word("no_lesbian")
    $ Girl.add_word(0,"lesbian","lesbian")
    $ Partner.add_word(0,"lesbian","lesbian")

label Les_Cycle(Girl=focused_Girl):
    $ Girl = check_girl(Girl)
    while round > 0:
        call shift_focus (Girl)
        call lesbian_launch(Girl)
        $ Girl.lust_face()

        if Player.focus < 100:

            menu:
                "Keep watching. . .":
                    pass

                "\"Ahem. . .\"" if "unseen" in Girl.recent_history:
                    jump Les_Interupted

                "Start jack'in it." if Player.secondary_action != "jerking_off":
                    call jerking_off (Girl)
                "Stop jack'in it." if Player.secondary_action == "jerking_off":
                    $ Player.secondary_action = None

                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.traits:
                    pass
                "Focus to last longer." if not Player.focusing and "focus" in Player.traits:
                    "You concentrate on not burning out too quickly."
                    $ Player.focusing = 1
                "Release your focus." if Player.focusing:
                    "You release your concentration. . ."
                    $ Player.focusing = 0
                "Other options":

                    menu:
                        "Offhand action":
                            if Girl.remaining_actions and multi_action:
                                call set_secondary_action
                                if Player.secondary_action:
                                    $ Girl.remaining_actions -= 1
                            else:
                                call Sex_Basic_Dialog (Girl, "tired")
                        "Threesome actions":

                            menu:
                                "Ask [Girl.name] to do something else with [Partner.name]":
                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh yeah, why don't you. . ."
                                        jump Les_Interupted
                                    else:
                                        call Les_Change (Girl)
                                "Ask [Partner.name] to do something else":
                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh yeah, why don't you. . ."
                                        jump Les_Interupted
                                    else:
                                        call Three_Change (Girl)

                                "Don't stop what you're doing. . .(locked)" if not position_timer or not second_girl_main_action:
                                    $ position_timer = 0
                                "Don't stop what you're doing. . ." if position_timer and second_girl_main_action:
                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh, that's good. . ."
                                        jump Les_Interupted
                                    else:
                                        $ position_timer = 0
                                "Undress [Partner.name]":



                                    if "unseen" in Girl.recent_history:
                                        ch_p "Oh, yeah, take it off. . ."
                                        jump Les_Interupted
                                    else:
                                        call Girl_Undress (Partner)
                                        call shift_focus (Partner)
                                        jump Les_Cycle
                                "Clean up Partner":
                                    if "unseen" in Girl.recent_history:
                                        ch_p "You've got a little something. . ."
                                        jump Les_Interupted
                                    else:
                                        call Girl_Cleanup (Partner, "ask")

                                        jump Les_Cycle
                                "Never mind":
                                    jump Les_Cycle
                        "undress [Girl.name]":
                            if "unseen" in Girl.recent_history:
                                ch_p "Oh yeah, why don't you. . ."
                                jump Les_Interupted
                            else:
                                call Girl_Undress (Girl)
                        "Clean up [Girl.name] (locked)" if not Girl.spunk:
                            pass
                        "Clean up [Girl.name]" if Girl.spunk:
                            if "unseen" in Girl.recent_history:
                                ch_p "You've got a little something. . ."
                                jump Les_Interupted
                            else:
                                call Girl_Cleanup (Girl, "ask")
                        "Never mind":
                            jump Les_Cycle

                "Back to Sex Menu" if multi_action:
                    ch_p "Let's try something else."
                    $ action_context = "shift"
                    $ line = 0
                    jump Les_After
                "End Scene" if not multi_action:
                    ch_p "Let's stop for now."
                    $ line = 0
                    jump Les_After


        call shift_focus (Girl)
        call Sex_Dialog (Girl, Partner)

        $ counter += 1
        $ round -= 1

        $ Player.focus = 50 if not Player.semen and Player.focus >= 50 else Player.focus

        if Player.focus >= 100 or Girl.lust >= 100:

            if Player.focus >= 100:

                if "unseen" not in Girl.recent_history:
                    call Player_Cumming (Girl)
                    if "_angry" in Girl.recent_history:
                        call reset_position(Girl)
                        call reset_position(Partner)
                        return
                    $ Girl.change_stat("lust", 200, 5)
                    if 100 > Girl.lust >= 70 and Girl.session_orgasms < 2:
                        $ Girl.recent_history.append("unsatisfied")
                        $ Girl.daily_history.append("unsatisfied")
                    $ line = "came"
                else:
                    "You grunt and try to hold it in."
                    $ Player.focus = 95
                    jump Les_Interupted

            if Girl.lust >= 100:

                call Girl_Cumming (Girl)
                jump Les_Interupted

            if line == "came":
                $ line = 0
                if not Player.semen:
                    "You're emptied out, you should probably take a break."
        if Partner and Partner.lust >= 100:

            call Girl_Cumming (Partner)



        $ Player.focus -= 12 if Player.focusing and Player.focus > 50 else 0

        if "unseen" in Girl.recent_history:
            if round == 10:
                "It's getting a bit late, [Girl.name] and [Partner.name] will probably be wrapping up soon."
            elif round == 5:
                "They're definitely going to stop soon."
        else:
            if round == 10:
                call Sex_Basic_Dialog (Girl, 10)
            elif round == 5:
                call Sex_Basic_Dialog (Girl, 5)

    $ Girl.change_face("_bemused", 0)
    $ line = 0
    if "unseen" not in Girl.recent_history:
        call Sex_Basic_Dialog (Girl, "done")


label Les_After:
    call reset_position(Girl)
    if not Partner:
        $ approval_bonus = 0
        call checkout
        return
    call reset_position(Partner)
    $ Girl.change_face("_sexy")
    if Partner == EmmaX:
        call Partner_Like (Girl, 4)
    else:
        call Partner_Like (Girl, 3)

    $ Girl.event_counter["seen_with_girl"] += 1
    $ Partner.event_counter["seen_with_girl"] += 1
    if Girl.event_counter["seen_with_girl"] == 1:
        $ Girl.SEXP += 15
        if Girl.love >= 500 and Girl.Org:
            if Girl == RogueX:
                ch_r "I have to say, I really enjoyed that one. . ."
            elif Girl == KittyX:
                ch_k "Hmm, that's kinda fun with an audience. . ."
            elif Girl == EmmaX:
                ch_e "I do enjoy an audience. . ."
                $ Girl.change_face("_sly",1)
                ch_e "something to keep in mind?"
            elif Girl == LauraX:
                ch_l "I enjoyed the audience. . ."
            elif Girl == JeanX:
                ch_j "Nice having an audience there. . ."
            elif Girl == StormX:
                ch_s "I did enjoy being watched. . ."
            elif Girl == JubesX:
                ch_v "It was cool to have an audience. . ."
    if Partner.event_counter["seen_with_girl"] == 1:
        $ Partner.SEXP += 15
        if Partner.love >= 500 and Partner.Org:
            if Partner == RogueX:
                ch_r "I have to say, I really enjoyed that one. . ."
            elif Partner == KittyX:
                ch_k "Hmm, that's kinda fun with an audience. . ."
            elif Partner == EmmaX:
                ch_e "I do enjoy an audience. . ."
                $ Partner.change_face("_sly",1)
                ch_e "something to keep in mind?"
            elif Partner == LauraX:
                ch_l "I enjoyed the audience. . ."
            elif Partner == JeanX:
                ch_j "Nice having an audience there. . ."
            elif Girl == StormX:
                ch_s "I did enjoy being watched. . ."
            elif Girl == JubesX:
                ch_v "It was cool to have an audience. . ."
    if not action_context:
        call Post_Les_Dialog
    $ Girl.add_word(1,0,0,0,"les "+Partner.tag)
    $ Partner.add_word(1,0,0,0,"les "+Girl.tag)
    $ approval_bonus = 0
    call checkout
    return



label Post_Les_Dialog:

    if Girl == RogueX:
        ch_r "That was nice. . ."
    elif Girl == KittyX:
        ch_k "That was fun. . ."
    elif Girl == EmmaX:
        ch_e "That was enjoyable. . ."
    elif Girl == LauraX:
        ch_l "That was fun. . ."
    elif Girl == JeanX:
        ch_j "Hey, that was fun. . ."
    elif Girl == StormX:
        ch_s "That was. . . quite enjoyable."
    elif Girl == JubesX:
        ch_v "That was a blast. . ."

    if "les "+Partner.tag in Girl.history:

        if Partner == RogueX:
            ch_r "Mmmm yeah. . ."
        elif Partner == KittyX:
            ch_k "Mmmm yeah that was good. . ."
        elif Partner == EmmaX:
            ch_e "Certainly. . ."
        elif Partner == LauraX:
            ch_l "Yup. . ."
        elif Partner == JeanX:
            ch_j "Yeah, I guess it was. . ."
        elif Partner == StormX:
            ch_s "It certainly was. . ."
        elif Girl == JubesX:
            ch_v "Totally. . ."
    else:


        if Girl.likes[Partner.tag] >= 600:

            if Girl == RogueX:
                ch_r "You. . . really know what you're doing down there. . ."
            elif Girl == KittyX:
                ch_k "You're really good at that!"
            elif Girl == EmmaX:
                ch_e "You were delightful dear!"
            elif Girl == LauraX:
                ch_l "I liked that thing with the mouth work."
            elif Girl == JeanX:
                ch_j "You seemed. . . experienced. . ."
            elif Girl == StormX:
                ch_s "You certainly have a talent for this. . ."
            elif Girl == JubesX:
                ch_v "You're really great at this. . ."
        else:

            if Girl == RogueX:
                ch_r "That. . . wasn't awful. . ."
            elif Girl == KittyX:
                ch_k "That was. . . interesting. . ."
            elif Girl == EmmaX:
                ch_e "At least you could keep up. . ."
            elif Girl == LauraX:
                ch_l "That was ok. . ."
            elif Girl == JeanX:
                ch_j "Yeah, ok. . ."
            elif Girl == StormX:
                ch_s "That was. . . fine."
            elif Girl == JubesX:
                ch_v "You. . . tried. . ."


        if Partner.likes[Girl.tag] >= 600:

            if Partner == RogueX:
                ch_r "Um, yeah, you too. . ."
            elif Partner == KittyX:
                ch_k "Yeah, that was really hot. . ."
            elif Partner == EmmaX:
                ch_e "Practice, dear. . ."
            elif Partner == LauraX:
                ch_l "I can read a map."
            elif Partner == JeanX:
                ch_j "Well, I -can- read minds. . ."
            elif Partner == StormX:
                ch_s "Yes, you as well."
            elif Partner == JubesX:
                ch_v "Yeah, you were great. . ."
        else:

            if Partner == RogueX:
                ch_r "I guess. . ."
            elif Partner == KittyX:
                ch_k "I guess. . ."
            elif Partner == EmmaX:
                ch_e "You could certainly do with more practice. . ."
            elif Partner == LauraX:
                ch_l "Uh-huh."
            elif Partner == JeanX:
                ch_j "Sure, whatever. . ."
            elif Partner == StormX:
                ch_s "Yes. . ."
            elif Partner == JubesX:
                ch_v "I guess you tried. . ."
    return



label Les_Response(Speaker=0, Subject=0, Step=1, B=0, B2=0, approval_bonus=0, Result=0, approval=0):




    if Speaker not in all_Girls:
        $ Speaker = Partner
    if Subject not in all_Girls:
        $ Subject = focused_Girl
    if Speaker == EmmaX:

        if "threesome" not in EmmaX.history or "classcaught" not in EmmaX.history or (taboo > 20 and "taboo" not in EmmaX.history):
            $ EmmaX.recent_history.append("no_lesbian")
            $ EmmaX.daily_history.append("no_lesbian")
            $ EmmaX.change_stat("obedience", 70, 5)
            $ EmmaX.change_stat("inhibition", 80, 5)
            $ EmmaX.change_stat("lust", 50, 10)
            $ Speaker.change_face("_sadside", 1)
            "[EmmaX.name] looks around furtively."
            if Subject == StormX:
                ch_e "Just to be clear, Ororo, I do -not- engage in sexual activities with students like [Player.name] here."
                ch_e "I suppose I should excuse myself."
                $ Subject.change_face("_bemused", 1)
                ch_s "Oh, yes, Ms. Frost. We would not wish to give the wrong impression."
            else:
                ch_e "I can't imagine why you would think I would engage in such behavior with a student!"
            call remove_girl (EmmaX)
            "She quickly leaves the room."
            return False

    if not Speaker.remaining_actions:

        if Speaker == RogueX:
            ch_r "I'm sorry, I'm just worn out"
        elif Speaker == KittyX:
            ch_k "I'm too tired for this. . ."
        elif Speaker == EmmaX:
            ch_e "I'm exhausted, not now. . ."
        elif Speaker == LauraX:
            ch_l "I've got other things to be doing. . ."
        elif Speaker == JeanX:
            ch_j "I'm tired of this. . ."
        elif Speaker == StormX:
            ch_s "I cannot right now, I am sorry."
        elif Speaker == JubesX:
            ch_v "Sorry, I'm just worn out. . ."
        return False

    if Speaker.event_counter["been_with_girl"]:
        $ approval_bonus += 10
    if Speaker.SEXP >= 50:
        $ approval_bonus += 25
    elif Speaker.SEXP >= 30:
        $ approval_bonus += 15
    elif Speaker.SEXP >= 15:
        $ approval_bonus += 5

    elif Speaker.inhibition >= 750:
        $ approval_bonus += 5

    if "exhibitionist" in Speaker.traits:
        $ approval_bonus += (3*taboo)

    if Speaker in Player.Harem or "sex friend" in Speaker.player_petnames:
        $ approval_bonus += 10
    elif "ex" in Speaker.traits:
        $ approval_bonus -= 40


    if Speaker.likes[Subject.tag] >= 900:
        $ B += 150
    elif Speaker.likes[Subject.tag] >= 800 or "poly " + Subject.tag in Speaker.traits:
        $ B += 100
    elif Speaker.likes[Subject.tag] >= 700:
        $ B += 50
    elif Speaker.likes[Subject.tag] <= 200:
        $ B -= 200
    elif Speaker.likes[Subject.tag] <= 500:
        $ B -= 100

    if Speaker == JeanX:
        $ B += 100

    $ approval = approval_check(Speaker, 1300, taboo_modifier = 2, Bonus = B)

    if not approval:

        pass
    elif Step == 1:

        if approval >= 2 or B >= 150:
            $ Speaker.change_face("_sexy", 1)
            if Speaker == RogueX:
                ch_r "You sure [Subject.tag]? Could be a lot of fun?"
            elif Speaker == KittyX:
                ch_k "Come on [Subject.tag], it could be kinda fun."
            elif Speaker == EmmaX:
                ch_e "Oh come on [Subject.tag], I could show you a few things."
            elif Speaker == LauraX:
                ch_l "It's really not bad, give it a shot."
            elif Speaker == JeanX:
                ch_j "Come on. . . [Subject.tag], it could be fun."
                $ B2 += 50
            elif Speaker == StormX:
                ch_s "Now [Subject.tag], it would not be so bad, would it?"
            elif Speaker == JubesX:
                ch_v "Come on, you in, [Subject.tag]? . ."
            if B2 >= 100:
                $ Result = 1
                $ Speaker.change_likes(Subject,(int(B/10)))
                $ Subject.change_likes(Speaker,(int(B2/10)))
        else:
            return Result

    elif Step == 2:

        if approval >= 2:
            $ Speaker.change_face("_smile", 1)
            if Speaker == RogueX:
                ch_r "'Course!"
            elif Speaker == KittyX:
                ch_k "'Course!"
            elif Speaker == EmmaX:
                ch_e "Of course, [Speaker.player_petname]."
            elif Speaker == LauraX:
                ch_l "I'm in."
            elif Speaker == JeanX:
                ch_j "Sure, why not."
            elif Speaker == StormX:
                ch_s "Sounds fun."
            elif Speaker == JubesX:
                ch_v "Sure, sounds fun."
            $ Result = 1
            return Result

        $ Speaker.change_face("_sly", 2)
        if Speaker == RogueX:
            if B >= 100:
                ch_r "I don't know, maybe. . ."
            if B >= 0:
                ch_r "I'm not sure about her though. . ."
        elif Speaker == KittyX:
            if B >= 100:
                ch_k "Yeah, I mean I guess. . ."
            if B >= 0:
                ch_k "No offense [Subject.tag], but. . ."
        elif Speaker == EmmaX:
            if B >= 100:
                ch_e "Mmmmm, certainly. . ."
            if B >= 0:
                ch_e "[Subject.tag], dear, I don't really think so. . ."
        elif Speaker == LauraX:
            if B >= 100:
                ch_l "You're cute and all. . ."
            if B >= 0:
                ch_l "I don't know, [Subject.tag]. . ."
        elif Speaker == JeanX:
            if B >= 100:
                ch_j "She's not bad. . ."
            if B >= 0:
                ch_j "With her? . ."
        elif Speaker == StormX:
            if B >= 100:
                ch_s "Oh, yes. . ."
            if B >= 0:
                ch_s "I am unsure. . ."
        elif Speaker == JubesX:
            if B >= 100:
                ch_v "Definitely. . ."
            if B >= 0:
                ch_v "I dunno. . ."
        $ Speaker.blushing = "_blush1"
        menu:
            extend ""
            "Ok, that's fine. . .":
                if B >= 100:
                    if Speaker == RogueX:
                        ch_r "Never mind, I'm in."
                    elif Speaker == KittyX:
                        ch_k "No, no, let's do this."
                    elif Speaker == EmmaX:
                        ch_e "Oh, don't back out now. . ."
                    elif Speaker == LauraX:
                        ch_l "Oh, no, I'm in."
                    elif Speaker == JeanX:
                        ch_j "Oh, don't get me wrong, I'm on board."
                    elif Speaker == StormX:
                        ch_s "No, no, I -am- interested. . ."
                    elif Speaker == JubesX:
                        ch_v "Oh, wait, I'm in!"
                    $ Result = 1
                else:
                    $ Speaker.change_face("_smile")
                    if Speaker == RogueX:
                        ch_r "Thanks, I appreciate it."
                    elif Speaker == KittyX:
                        ch_k "Thanks, I appreciate it."
                    elif Speaker == EmmaX:
                        ch_e "I appreciate your restraint."
                    elif Speaker == LauraX:
                        ch_l "Yeah. . ."
                    elif Speaker == JeanX:
                        ch_j "Right. . ."
                    elif Speaker == StormX:
                        ch_s "I appreciate that, thank you."
                    elif Speaker == JubesX:
                        ch_v "Yeah, thanks."
            "Come on, you might enjoy it. . .":
                if B >= 50:
                    if Speaker == RogueX:
                        ch_r "Well, I suppose."
                    elif Speaker == KittyX:
                        ch_k "I mean, maybe?"
                    elif Speaker == EmmaX:
                        ch_e "I'm sure I would. . ."
                    elif Speaker == LauraX:
                        ch_l "Maybe. . "
                    elif Speaker == JeanX:
                        ch_j "Yeah, I guess. . ."
                    elif Speaker == StormX:
                        ch_s "I suppose that I might. . ."
                    elif Speaker == JubesX:
                        ch_v "I guess. . ."
                    $ Result = 1
                else:
                    $ Speaker.change_face("_sad", 2)
                    if Speaker == RogueX:
                        ch_r "I don't think so."
                    elif Speaker == KittyX:
                        ch_k "Probably not."
                    elif Speaker == EmmaX:
                        ch_e "Probably not."
                    elif Speaker == LauraX:
                        ch_l "I doubt it."
                    elif Speaker == JeanX:
                        ch_j "Doubt it."
                    elif Speaker == StormX:
                        ch_s "Not at the moment though."
                    elif Speaker == JubesX:
                        ch_v "I don't know, I don't think so. . ."
            "Get in there, now.":
                if approval_check(Speaker, 550, "OI", taboo_modifier = 2):
                    $ Speaker.change_face("_sadside", 1)
                    if Speaker == RogueX:
                        ch_r "Fine, whatever."
                    elif Speaker == KittyX:
                        ch_k "Fiiine."
                    elif Speaker == EmmaX:
                        ch_e "Oh, fine."
                    elif Speaker == LauraX:
                        ch_l "Fine."
                    elif Speaker == JeanX:
                        ch_j "Oh, whatever."
                    elif Speaker == StormX:
                        ch_s "Fine."
                    elif Speaker == JubesX:
                        ch_v "Oh, whatever."
                    $ Result = 1
                else:
                    $ Speaker.change_face("_angry")
                    if Speaker == RogueX:
                        ch_r "Who do you think you're talk'in to?"
                    elif Speaker == KittyX:
                        ch_k "You're not the boss of me!"
                    elif Speaker == EmmaX:
                        ch_e "Don't forget who's in charge here, [Speaker.player_petname]"
                    elif Speaker == LauraX:
                        ch_l "Don't push me."
                    elif Speaker == JeanX:
                        ch_j "Don't you tell me what to \"get into.\""
                    elif Speaker == StormX:
                        ch_s "This is not how one asks a favor."
                    elif Speaker == JubesX:
                        ch_v "No way!"
                    $ Speaker.add_word(1,"_angry","_angry")
            "[Subject.name], what do you think?":
                $ Subject.change_face("_sexy", 1)
                $ Speaker.change_likes(Subject,(int(B/10)))
                if B >= 50:
                    $ Subject.change_likes(Speaker,5)
                if Subject == RogueX:
                    if Speaker == KittyX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_r "You know that we work well together."
                        else:
                            ch_r "It could be a lot of fun."
                    elif Speaker == EmmaX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_r "You could do that thing from last time. . ."
                        else:
                            ch_r "I was hoping you could give me some after class lessons. . ."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_r "Oh, it's not that bad."
                        else:
                            ch_r "It could be a lot of fun."
                elif Subject == KittyX:
                    if Speaker == RogueX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_k "Come on [Speaker.tag], you know we have fun."
                        else:
                            ch_k "Come on [Speaker.tag], could be fun."
                    elif Speaker in (EmmaX,StormX):
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_k "I mean, it might be nice to show [Subject.player_petname] what you've taught me. . ."
                        else:
                            ch_k "I've seen you watching me in class. . ."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_k "We have so much fun together though."
                        else:
                            ch_k "It could be fun!"
                elif Subject == EmmaX:
                    if Speaker == StormX:
                        ch_e "I really think we have a few things we could teach [EmmaX.player_petname] here. . ."
                    elif Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                        ch_e "What's the matter [Speaker.name], too shy around [Player.name]?"
                    else:
                        ch_e "What's the matter [Speaker.name], I've seen how you look at me. . ."
                elif Subject == LauraX:
                    if Speaker == EmmaX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_l "Wow, you aren't this shy when [Subject.player_petname]'s not around."
                        else:
                            ch_l "Come on, you look really squishy."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_l "What, you don't want to fuck with [Player.name] around?"
                        else:
                            ch_l "Come on, you look like you have it in you."
                elif Subject == JeanX:
                    if Speaker == EmmaX:
                        ch_j "Come on, we both know you're into this shit."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_j "What, -now- you're getting shy?"
                        else:
                            ch_j "Come on, I bet you really get around."
                elif Subject == StormX:
                    if Speaker == KittyX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_s "Now [Speaker.tag], this certainly wouldn't be your first lesson. . ."
                        else:
                            ch_s "Now [Speaker.tag], haven't you taken -any- interest in me?"
                    elif Speaker == EmmaX:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_s "Now [Subject.player_petname], that isn't what you've said in the past. . ."
                        else:
                            ch_s "Oh? You want to pass up the opportunity to teach [StormX.player_petname] a few things. . ."
                    else:
                        if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                            ch_s "You haven't enjoyed our time together?"
                        else:
                            ch_s "I can promise you would enjoy yourself. . ."
                elif Subject == JubesX:
                    if Subject.event_counter["been_with_girl"] and Speaker.event_counter["been_with_girl"]:
                        ch_v "I mean, it's not like this is our -first time- or anything. . ."
                    else:
                        ch_v "I think I can carry my weight over here. . ."


                if B >= 50:

                    $ Speaker.change_face("_smile", 1)
                    if Speaker == RogueX:
                        ch_r "You know, I can't argue with that, [Subject.tag]."
                    elif Speaker == KittyX:
                        ch_k "Heh, I guess so, [Subject.tag]."
                    elif Speaker == EmmaX:
                        ch_e "If we must, [Subject.tag]."
                    elif Speaker == LauraX:
                        ch_l "I guess so."
                    elif Speaker == JeanX:
                        ch_j "Fair point. . ."
                    elif Speaker == StormX:
                        ch_s "Well you do make a compelling case. . ."
                    elif Speaker == JubesX:
                        ch_v "Well, that's true. . ."
                    $ Result = 1
                else:

                    $ Speaker.change_face("_angry", 1, eyes="_side")
                    if Speaker == RogueX:
                        ch_r "Sorry [Subject.tag], nothin personal."
                    elif Speaker == KittyX:
                        ch_k "Sorry [Subject.tag], I don't mean anything personal."
                    elif Speaker == EmmaX:
                        ch_e "I'm sorry [Subject.tag], it's really not you."
                    elif Speaker == LauraX:
                        ch_l "Sorry [Subject.tag], it's not about you."
                    elif Speaker == JeanX:
                        ch_j "Yeah, I'm really not interested."
                    elif Speaker == StormX:
                        ch_s "I'm afraid not, [Subject.tag]."
                    elif Speaker == JubesX:
                        ch_v "No way, nothing personal, [Subject.tag]."

    if Step == 3:

        if approval:
            $ Speaker.change_face("_smile", 1)
            if Speaker == RogueX:
                ch_r "I mean, I guess so. . ."
            elif Speaker == KittyX:
                ch_k "I mean, I guess. . ."
            elif Speaker == EmmaX:
                ch_e "How could I back out now?"
            elif Speaker == LauraX:
                ch_l "Yeah. . ."
            elif Speaker == JeanX:
                ch_j "Well, I guess."
            elif Speaker == StormX:
                ch_s "I suppose we could continue. . ."
            elif Speaker == JubesX:
                ch_v "Well, I guess if you're into it. . ."
            $ Result = 1
        else:
            $ Speaker.change_face("_sadside", 1)
            if Speaker == RogueX:
                ch_r "I'm really not into that right now. . ."
            elif Speaker == KittyX:
                ch_k "I'm really not into it atm. . ."
            elif Speaker == EmmaX:
                ch_e "I'm afraid not. . ."
            elif Speaker == LauraX:
                ch_l "Not right now. . ."
            elif Speaker == JeanX:
                ch_j "Not into it."
            elif Speaker == StormX:
                ch_s "I would rather not."
            elif Speaker == JubesX:
                ch_v "Nah, not into it."
    if not Result:

        $ Speaker.recent_history.append("no_lesbian")
        $ Speaker.daily_history.append("no_lesbian")
        $ Speaker.change_face("_sadside", 1)
        $ Partner = 0
        if Speaker == RogueX:
            if B <= 0:
                ch_r "Sorry, [Speaker.player_petname], it's just not like that with her."
            if Speaker.taboo > 20:
                ch_r "Sorry, [Speaker.player_petname], this isn't a good place for it."
            if B >= 100:
                ch_r "Sorry, [Speaker.player_petname], maybe if you weren't around. . ."
            else:
                ch_r "Sorry, [Speaker.player_petname], I'm just not interested."
        elif Speaker == KittyX:
            if B <= 0:
                ch_k "Sorry, [Speaker.player_petname], I'm just not into her."
            if Speaker.taboo > 20:
                ch_k "Sorry, [Speaker.player_petname], this isn't exactly the right place for that."
            if B >= 100:
                ch_k "Sorry, [Speaker.player_petname], not with you watching. . ."
            else:
                ch_k "Sorry, [Speaker.player_petname], I'm just not into it."
        elif Speaker == EmmaX:
            if B <= 0:
                ch_e "I'm sorry, [Speaker.player_petname], she's just not my type."
            if Speaker.taboo > 20:
                ch_e "I'm sorry, [Speaker.player_petname], this would cause a scandal."
            if B >= 100:
                ch_e "I'm sorry, [Speaker.player_petname], not with an audience. . ."
            else:
                ch_e "I'm sorry, [Speaker.player_petname], I'm just not interested in that."
        elif Speaker == LauraX:
            if B <= 0:
                ch_l "Sorry, [Speaker.player_petname], she's not my type."
            if Speaker.taboo > 20:
                ch_l "Sorry, [Speaker.player_petname], this area's a bit exposed."
            if B >= 100:
                ch_l "Sorry, [Speaker.player_petname], I don't want an audience. . ."
            else:
                ch_l "Sorry, [Speaker.player_petname], I'm just not into that."
        elif Speaker == JeanX:
            if B <= 0:
                ch_l "Sorry, [Speaker.player_petname], I know I can do better than her."
            if Speaker.taboo > 20:
                ch_l "Sorry, [Speaker.player_petname]. . . not in public."
            if B >= 100:
                ch_l "Sorry, [Speaker.player_petname], you'll have to earn that . ."
            else:
                ch_l "Sorry, [Speaker.player_petname], not right now."
        elif Speaker == StormX:
            if B <= 0:
                ch_s "Apologies, [Speaker.player_petname], I could not, with her."
            if Speaker.taboo > 20:
                ch_s "Apologies, [Speaker.player_petname], this is not the place for it."
            if B >= 100:
                ch_s "Apologies, [Speaker.player_petname], this is a private affair. . ."
            else:
                ch_s "Apologies, [Speaker.player_petname], I am just uninterested."
        elif Speaker == JubesX:
            if B <= 0:
                ch_v "Sorry, [Speaker.player_petname], she's not my type."
            if Speaker.taboo > 20:
                ch_v "Sorry, [Speaker.player_petname], not here, at least."
            if B >= 100:
                ch_v "Sorry, [Speaker.player_petname], I don't want an audience. . ."
            else:
                ch_v "Sorry, [Speaker.player_petname], I'm not into it."


    return Result



label Les_FirstKiss:

    if "les " + Partner.tag in Girl.history:

        $ line = "experienced"
    elif Girl.event_counter["been_with_girl"] and Partner.event_counter["been_with_girl"]:

        $ line = "first both"
    elif Girl.event_counter["been_with_girl"]:

        $ line = "first girl"
    elif Partner.event_counter["been_with_girl"]:

        $ line = "first partner"

    if line == "experienced":
        "[Girl.name] and [Partner.name] move together in a passionate kiss."
        "[Girl.name]'s arms firmly grasp [Partner.name]'s neck and pull her close."
    else:
        if line in ("first both", "first girl"):

            "[Girl.name] slowly moves in and gives [Partner.name] a soft kiss."
        else:

            "[Girl.name] casually places a hand on the back of [Partner.name]'s head and draws their lips together."
        if line == "first partner":

            "[Partner.name] pulls back a bit, but slowly leans into the enbrace."
        else:

            "[Partner.name]'s lips curl up into a smile and she draws [Girl.name] even closer."
        "After a few seconds, it begins to grow more passionate."
    return





label Girl_Whammy(Other):

    if "nowhammy" not in JeanX.traits and Other.likes[JeanX.tag] < 800:

        $ Player.add_word(1,0,0,0,"whammied")
        if Other == EmmaX and EmmaX.level >= JeanX.level:
            ch_e "Oh, don't even try that nonsense with me, Ms. Grey."
            return
        if Other == JubesX and JubesX.level >= JeanX.level:
            ch_v "Vampire whammy beats mutant whammy!"
            return

        $ Other.likes[JeanX.tag] += 500 if Other.likes[JeanX.tag] <= 900 else Other.likes[JeanX.tag]
        $ Other.likes[JeanX.tag] = 900 if Other.likes[JeanX.tag] >= 900 else Other.likes[JeanX.tag]
    return




label Les_Change(Primary=0, Secondary=Partner, D20S=0, PrimaryLust=0, SecondaryLust=0):



    if Primary not in all_Girls:
        return
    $ line = 0
    menu:
        "Hey [Primary.name]. . ."
        "why don't you kiss her?" if second_girl_secondary_action != "kiss girl" and second_girl_secondary_action != "kiss both":
            call Threeway_Set (Primary, "kiss girl", "lesbian", girl_secondary_action, Secondary)
        "why don't you grab her tits?" if girl_secondary_action != "fondle_breasts":
            call Threeway_Set (Primary, "fondle_breasts", "lesbian", girl_secondary_action, Secondary)
        "why don't you suck her breasts?" if girl_secondary_action != "suck_breasts":
            call Threeway_Set (Primary, "suck_breasts", "lesbian", girl_secondary_action, Secondary)
        "why don't you finger her?" if girl_secondary_action != "fondle_pussy":
            call Threeway_Set (Primary, "fondle_pussy", "lesbian", girl_secondary_action, Secondary)
        "why don't you go down on her?" if girl_secondary_action != "eat_pussy":
            call Threeway_Set (Primary, "eat_pussy", "lesbian", girl_secondary_action, Secondary)
        "why don't you grab her ass?" if girl_secondary_action != "fondle_ass":
            call Threeway_Set (Primary, "fondle_ass", "lesbian", girl_secondary_action, Secondary)
        "why don't you lick her ass?" if girl_secondary_action != "eat_ass":
            call Threeway_Set (Primary, "eat_ass", "lesbian", girl_secondary_action, Secondary)
        "never mind.":
            pass
    if not line:
        $ line = "You return to what you were doing."
    else:
        $ action_context = "skip"
    "[line]"
    return





label Poly_Start(Newbie=0, round2=0, Asked=0):




    $ line = 0

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
        if round2 and Asked:
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
        call Harem_Start (Newbie, round2)
        return


    $ Party = [Player.Harem[0]]
    call shift_focus (Player.Harem[0])
    call set_the_scene
    call clear_the_room (Player.Harem[0])


    if round2:
        "You pull [Party[0].name] aside for a moment."
        ch_p "Hey, have you changed your mind about [Newbie.name] lately?"
    else:
        $ Party[0].change_face("_bemused")
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



    if Party[0].likes[Newbie.tag] >= 800:
        $ Party[0].change_face("_sly")
    elif Party[0].likes[Newbie.tag] >= 600:
        pass
    else:

        $ Party[0].change_face("_angry",mouth="_normal")


    if Party[0] == RogueX:
        if Party[0].likes[Newbie.tag] >= 800:

            ch_r "She is pretty sexy, I guess."
        elif Party[0].likes[Newbie.tag] >= 600:

            ch_r "I like her just fine, I was just wondering where it was headed."
        else:

            ch_r "I'm not really a fan'a hers."
    elif Party[0] == KittyX:
        if Party[0].likes[Newbie.tag] >= 800:

            ch_k "She's kinda hot, I get that. . ."
        elif Party[0].likes[Newbie.tag] >= 600:

            ch_k "She's ok, sure, but I'm not sure. . ."
        else:

            ch_k "I don't really like her much."
    elif Party[0] == EmmaX:
        if Party[0].likes[Newbie.tag] >= 800:

            ch_e "I think she's quite the catch."
        elif Party[0].likes[Newbie.tag] >= 600:

            ch_e "I do like her, but have some concerns."
        else:

            ch_e "I don't really approve."
    elif Party[0] == LauraX:
        if Party[0].likes[Newbie.tag] >= 800:

            ch_l "She's pretty hot, I get it."
        elif Party[0].likes[Newbie.tag] >= 600:

            ch_l "She's ok, I guess."
        else:

            ch_l "I don't like her."
    elif Party[0] == JeanX:
        if Party[0].likes[Newbie.tag] >= 800:

            ch_j "I get it, she's hot enough."
        elif Party[0].likes[Newbie.tag] >= 600:

            ch_j "She's. . . fine."
        else:

            ch_j "You probably shouldn't be seen around her."
    elif Party[0] == StormX:
        if Party[0].likes[Newbie.tag] >= 800:

            ch_s "She is very beautiful, certainly."
        elif Party[0].likes[Newbie.tag] >= 600:

            ch_s "She is a good girl, certainly. . ."
        else:

            ch_s "I do not think I like her much."
    elif Party[0] == JubesX:
        if Party[0].likes[Newbie.tag] >= 800:

            ch_v "Ok, she's totally hot, but. . ."
        elif Party[0].likes[Newbie.tag] >= 600:

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
            $ line = "y"
        "Maybe, what do you think?":
            $ line = "m"
        "No, not really.":
            $ line = "n"

    if line == "y":
        if Party[0].likes[Newbie.tag] >= 800:

            $ line = "yy"
            $ Party[0].change_stat("love", 90, 5)
            $ Party[0].change_stat("obedience", 50, 5)
            $ Party[0].change_stat("inhibition", 90, 10)
        elif approval_check(Party[0], 1800):

            $ line = "ym"
            $ Party[0].change_stat("obedience", 50, 5)
        elif approval_check(Party[0], 1500) and Party[0].likes[Newbie.tag] >= 500:

            $ line = "ym"
        else:

            $ line = "yn"
            $ Party[0].change_stat("love", 90, -10)

    if line == "m":
        if Party[0].likes[Newbie.tag] >= 800:

            $ line = "my"
            $ Party[0].change_stat("inhibition", 90, 5)
        elif approval_check(Party[0], 1800):

            $ line = "mm"
        elif approval_check(Party[0], 1500) and Party[0].likes[Newbie.tag] >= 600:

            $ line = "mm"
        else:

            $ line = "mn"

    if line == "n":
        if Party[0].likes[Newbie.tag] >= 800:

            $ line = "ny"
            $ Party[0].change_stat("inhibition", 90, 10)
        elif approval_check(Party[0], 1700):

            $ line = "nm"
            $ Party[0].change_stat("inhibition", 90, 5)
        elif approval_check(Party[0], 1300) and Party[0].likes[Newbie.tag] >= 500:

            $ line = "nm"
            $ Party[0].change_stat("love", 90, 5)
        else:

            $ line = "nn"
            $ Party[0].change_stat("love", 90, 10)





    if line == "yn" or line == "mn" or line == "nn":
        $ Party[0].change_face("_angry")
    elif line == "yy" or line == "ny" or line == "my":
        $ Party[0].change_face("_sexy")
    else:
        $ Party[0].change_face("_bemused")


    if Party[0] == RogueX:
        if line == "yy":

            ch_r "Great, sounds fun."
        elif line == "my":

            ch_r "Oh, don't let me stop you."
        elif line == "ny":

            ch_r "Oh. Well maybe you should!"

        elif line == "ym" or line == "mm":

            ch_r "Yeah, I guess I can live with that."
        elif line == "nm":

            ch_r "Hmm, not that I would have minded."

        elif line == "yn" or line == "mn":

            ch_r "I don't think I'm really cool with that."
        elif line == "nn":

            ch_r "Good to hear."

    elif Party[0] == KittyX:
        if line == "yy":

            ch_k "Cool, sounds fun."
        elif line == "my":

            ch_k "Oh, seriously, it's fine with me!"
        elif line == "ny":

            ch_k "You might want to, she's hot!"

        elif line == "ym" or line == "mm":

            ch_k "Yeah, I can[KittyX.like]live with that."
        elif line == "nm":

            ch_k "Ok, I would have been ok with it though."

        elif line == "yn" or line == "mn":

            ch_k "That's not really cool with me."
        elif line == "nn":

            ch_k "Good, that wouldn't have been cool."

    elif Party[0] == EmmaX:
        if line == "yy":

            ch_e "Lovely. . ."
        elif line == "my":

            ch_e "Oh, please do, she's lovely."
        elif line == "ny":

            ch_e "Pity, I rather like her."

        elif line == "ym" or line == "mm":

            ch_e "I suppose I can make do then."
        elif line == "nm":

            ch_e "You could do a lot worse."

        elif line == "yn" or line == "mn":

            ch_e "I don't think that will be acceptable."
        elif line == "nn":

            ch_e "Probably for the best."

    elif Party[0] == LauraX:
        if line == "yy":

            ch_l "Nice."
        elif line == "my":

            ch_l "Come on, she's pretty great."
        elif line == "ny":

            ch_l "You sure? She's hot."

        elif line == "ym" or line == "mm":

            ch_l "Fine, I can work with that."
        elif line == "nm":

            ch_l "Ok. I'm cool with it if you do though."

        elif line == "yn" or line == "mn":

            ch_l "Nope."
        elif line == "nn":

            ch_l "Good."

    elif Party[0] == JeanX:
        if line == "yy":

            ch_j "Well, ok, sure."
        elif line == "my":

            ch_j "Well. . . she could be fun. . ."
        elif line == "ny":

            ch_j "Really? I mean, she could be fun."

        elif line == "ym" or line == "mm":

            ch_j "Well, ok, fine. . ."
        elif line == "nm":

            ch_j "Ok. I could think about it though."

        elif line == "yn" or line == "mn":

            ch_j "Well, cut it out."
        elif line == "nn":

            ch_j "Yeah."

    elif Party[0] == StormX:
        if line == "yy":

            ch_s "Oh, that will be nice. . ."
        elif line == "my":

            ch_s "Oh, you definitely should!"
        elif line == "ny":

            ch_s "That is too bad. You would go well together."

        elif line == "ym" or line == "mm":

            ch_s "Well, that should be fine."
        elif line == "nm":

            ch_s "You might want to reconsider. . ."

        elif line == "yn" or line == "mn":

            ch_s "I do not think I could deal with her."
        elif line == "nn":

            ch_s "Yes, I would agree with that."

    elif Party[0] == JubesX:
        if line == "yy":

            ch_v "Ok, cool."
        elif line == "my":

            ch_v "Yeah, sure, I'm down with it."
        elif line == "ny":

            ch_v "Ok, but you might be missing out!"

        elif line == "ym" or line == "mm":

            ch_v "Ok, yeah, I can deal."
        elif line == "nm":

            ch_v "Ok, your call, I guess."

        elif line == "yn" or line == "mn":

            ch_v "Well. . . I might have some feelings."
        elif line == "nn":

            ch_v "Glad we're on the same page here."



    if line != "yy" and line != "nn":

        menu:
            extend ""
            "Ok, then I guess I will ask her to join us." if line in ("my","ny","ym","mm","nm"):

                $ line = "yy"
                $ Party[0].change_face("_smile")
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

            "Well then, I guess I'll stop." if line in ("mn","yn","ym","mm","nm"):

                $ line = "nn"
                $ Party[0].change_face("_smile")
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

                pass

            "Well, I'm going to pass anyway." if line in ("nm","ny","mm"):

                $ line = "nn"
                $ Party[0].change_face("_sad")
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



    if line == "mn" or line == "yn":


        if approval_check(Party[0], 1600) and Party[0].likes[Newbie.tag] >= 500:
            $ Party[0].change_face("_sadside")
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
            $ line = "yy"
        else:
            $ Party[0].change_face("_angry",eyes="_side")
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
            $ Party[0].traits.append("ex")
            $ Party[0].broken_up[0] = 5 + Party[0].broken_up[1] + Party[0].cheated_on
            $ Player.Harem.remove(Party[0])
            call remove_girl (Party[0])


    $ Party = []
    if line == "yy":
        if Newbie.tag + "No" in Player.traits:
            $ Player.traits.remove(Newbie.tag + "No")
        $ Player.drain_word(Newbie.tag + "No",0,0,1)
        $ Player.traits.append(Newbie.tag + "Yes")
        "You should give [Newbie.name] a call."
    else:
        $ Player.traits.append(Newbie.tag + "No")
    return






label Harem_Start(Newbie=0, round2=0):




    $ line = 0

    if len(Player.Harem) < 2:

        return

    $ Party = [Player.Harem[0],Player.Harem[1]]

    call check_who_is_present
    $ Party = [Player.Harem[0],Player.Harem[1]]
    call shift_focus (Player.Harem[0])
    call set_the_scene

    $ Party[0].change_face("_bemused")
    $ Party[1].change_face("_bemused")
    if round2:
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




    if Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:
        pass
    elif Party[0].likes[Newbie.tag] >= 700:

        $ Party[1].change_face("_angry",mouth="_normal")
    elif Party[1].likes[Newbie.tag] >= 700:

        $ Party[0].change_face("_angry",mouth="_normal")
    else:

        $ Party[0].change_face("_angry",mouth="_normal")
        $ Party[1].change_face("_angry",mouth="_normal")

    if Party[0] == RogueX:
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            ch_r "Now we like her just fine, and we can't say we don't like the idea much."
        elif Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:

            ch_r "Now we like her just fine, but we don't know about share'in."
        elif Party[0].likes[Newbie.tag] >= 700:

            ch_r "Now I like her just fine, but [Party[1].name] ain't so sure."
        elif Party[1].likes[Newbie.tag] >= 700:

            ch_r "Now [Party[1].name] seems to like her, but I'm not so sure."
        else:

            ch_r "Neither'a us is really cool with that."
    elif Party[0] == KittyX:
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            ch_k "She's kinda hot, we get that. . ."
        elif Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:

            ch_k "She's ok, sure, but we're not sure. . ."
        elif Party[0].likes[Newbie.tag] >= 700:

            ch_k "I like her, but I don't know about [Party[1].name]."
        elif Party[1].likes[Newbie.tag] >= 700:

            ch_k "[Party[1].name] likes her, but I don't know."
        else:

            ch_k "We don't really like her much."
    elif Party[0] == EmmaX:
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            ch_e "I think we agree that she's a nice catch."
        elif Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:

            ch_e "We do like her, but we have some concerns."
        elif Party[0].likes[Newbie.tag] >= 700:

            ch_e "[Party[1].name] doesn't really approve."
        elif Party[1].likes[Newbie.tag] >= 700:

            ch_e "[Party[1].name] seems to think she's acceptable."
        else:

            ch_e "We don't really approve."
    elif Party[0] == LauraX:
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            ch_l "She's pretty hot, we get it."
        elif Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:

            ch_l "She's ok, I guess."
        elif Party[0].likes[Newbie.tag] >= 700:

            ch_l "She's fine, but [Party[1].name] doesn't like her."
        elif Party[1].likes[Newbie.tag] >= 700:

            ch_l "[Party[1].name] likes her. I don't."
        else:

            ch_l "We don't like her."
    elif Party[0] == JeanX:
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            ch_j "I get it, she's hot enough."
        elif Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:

            ch_j "She's. . . fine."
        elif Party[0].likes[Newbie.tag] >= 700:

            ch_j "I think she's fine, but [Party[1].name] doesn't like her."
            ch_j "For whatever that's worth. . ."
        elif Party[1].likes[Newbie.tag] >= 700:

            ch_j "[Party[1].name] likes her. I don't."
            ch_j "So I think you know the right answer to this one. . ."
        else:

            ch_j "You probably shouldn't be seen around her."
    elif Party[0] == StormX:
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            ch_s "We agree that she is very beautiful. . ."
        elif Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:

            ch_s "She is a good girl, but we do have some concerns. . ."
        elif Party[0].likes[Newbie.tag] >= 700:

            ch_s "I like her, but [Party[1].name] does not approve."
        elif Party[1].likes[Newbie.tag] >= 700:

            ch_s "[Party[1].name] appears to like her, I am unsure."
        else:

            ch_s "We do not like her very much."

    elif Party[0] == JubesX:
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            ch_v "Ok, she's totally hot, but. . ."
        elif Party[0].likes[Newbie.tag] >= 600 and Party[1].likes[Newbie.tag] >= 600:

            ch_v "She's. . . fine, but. . ."
        elif Party[0].likes[Newbie.tag] >= 700:

            ch_v "She's. . . fine, but, [Party[1].name]. . ."
        elif Party[1].likes[Newbie.tag] >= 700:

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
            $ line = "y"
        "Maybe, what do you think?":
            $ line = "m"
        "No, not really.":
            $ line = "n"

    if line == "y":
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            $ line = "yy"
            $ Party[0].change_stat("love", 90, 5)
            $ Party[0].change_stat("obedience", 50, 5)
            $ Party[0].change_stat("inhibition", 90, 10)
            $ Party[1].change_stat("love", 90, 5)
            $ Party[1].change_stat("obedience", 50, 5)
            $ Party[1].change_stat("inhibition", 90, 10)
        elif approval_check(Party[0], 1800) and approval_check(Party[1], 1800):

            $ line = "ym"
            $ Party[0].change_stat("obedience", 50, 10)
            $ Party[1].change_stat("obedience", 50, 10)
        elif approval_check(Party[0], 1500) and approval_check(Party[1], 1500):
            if Party[0].likes[Newbie.tag] >= 500 and Party[1].likes[Newbie.tag] >= 500:

                $ line = "ym"
                $ Party[0].change_stat("obedience", 80, 15)
                $ Party[1].change_stat("obedience", 80, 15)
            else:

                $ line = "yn"
                $ Party[0].change_stat("love", 90, -5)
                $ Party[0].change_stat("obedience", 50, -5)
                $ Party[1].change_stat("love", 90, -5)
                $ Party[1].change_stat("obedience", 50, -5)
        else:

            $ line = "yn"
            $ Party[0].change_stat("love", 90, -10)
            $ Party[0].change_stat("obedience", 50, -5)
            $ Party[1].change_stat("love", 90, -10)
            $ Party[1].change_stat("obedience", 50, -5)

    if line == "m":
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            $ line = "my"
            $ Party[0].change_stat("inhibition", 90, 5)
            $ Party[1].change_stat("inhibition", 90, 5)
        elif approval_check(Party[0], 1800) and approval_check(Party[1], 1800):

            $ line = "mm"
        elif approval_check(Party[0], 1500) and approval_check(Party[1], 1500):
            if Party[0].likes[Newbie.tag] >= 600 or Party[1].likes[Newbie.tag] >= 600:

                $ line = "mm"
            else:

                $ line = "mn"
        else:

            $ line = "mn"

    if line == "n":
        if Party[0].likes[Newbie.tag] >= 800 and Party[1].likes[Newbie.tag] >= 800:

            $ line = "ny"
            $ Party[0].change_stat("inhibition", 90, 10)
            $ Party[1].change_stat("inhibition", 90, 10)
        elif approval_check(Party[0], 1700) and approval_check(Party[1], 1700):

            $ line = "nm"
            $ Party[0].change_stat("inhibition", 90, 5)
        elif approval_check(Party[0], 1300) and approval_check(Party[1], 1300):
            if Party[0].likes[Newbie.tag] >= 500 and Party[1].likes[Newbie.tag] >= 500:

                $ line = "nm"
            else:

                $ line = "nn"
                $ Party[0].change_stat("love", 90, 5)
                $ Party[0].change_stat("inhibition", 90, 5)
                $ Party[1].change_stat("love", 90, 5)
                $ Party[1].change_stat("inhibition", 90, 5)
        else:

            $ line = "nn"
            $ Party[0].change_stat("love", 90, 5)
            $ Party[0].change_stat("inhibition", 90, 5)
            $ Party[1].change_stat("love", 90, 5)
            $ Party[1].change_stat("inhibition", 90, 5)





    if line == "yn" or line == "mn" or line == "nn":
        $ Party[0].change_face("_angry")
        $ Party[1].change_face("_angry")
    elif line == "yy" or line == "ny" or line == "my":
        $ Party[0].change_face("_sexy")
        $ Party[1].change_face("_sexy")
    else:
        $ Party[0].change_face("_bemused")
        $ Party[1].change_face("_bemused")


    if Party[0] == RogueX:
        if line == "yy":

            ch_r "Great, sounds fun."
        elif line == "my":

            ch_r "Oh, don't let me stop you."
        elif line == "ny":

            ch_r "Oh. Well maybe you should!"

        elif line == "ym" or line == "mm":

            ch_r "Yeah, I guess we can live with that."
        elif line == "nm":

            ch_r "Hmm, not that we would have minded."

        elif line == "yn" or line == "mn":

            ch_r "I don't think we're really cool with that."
        elif line == "nn":

            ch_r "Good to hear."

    elif Party[0] == KittyX:
        if line == "yy":

            ch_k "Cool, sounds fun."
        elif line == "my":

            ch_k "Oh, seriously, it's fine with us!"
        elif line == "ny":

            ch_k "You might want to, she's hot!"

        elif line == "ym" or line == "mm":

            ch_k "Yeah, we can[KittyX.like]live with that."
        elif line == "nm":

            ch_k "Ok, we would have been ok with it though."

        elif line == "yn" or line == "mn":

            ch_k "That's not really cool with us."
        elif line == "nn":

            ch_k "Good, that wouldn't have been cool."

    elif Party[0] == EmmaX:
        if line == "yy":

            ch_e "Lovely. . ."
        elif line == "my":

            ch_e "Oh, please do, she's lovely."
        elif line == "ny":

            ch_e "Pity, I rather like her."

        elif line == "ym" or line == "mm":

            ch_e "I suppose we can make do then."
        elif line == "nm":

            ch_e "You could do a lot worse."

        elif line == "yn" or line == "mn":

            ch_e "I don't think that will be acceptable."
        elif line == "nn":

            ch_e "Probably for the best."

    elif Party[0] == LauraX:
        if line == "yy":

            ch_l "Nice."
        elif line == "my":

            ch_l "Come on, she's pretty great."
        elif line == "ny":

            ch_l "You sure? She's hot."

        elif line == "ym" or line == "mm":

            ch_l "Fine, we can work with that."
        elif line == "nm":

            ch_l "Ok. We're cool with it if you do though."

        elif line == "yn" or line == "mn":

            ch_l "Nope."
        elif line == "nn":

            ch_l "Good."

    elif Party[0] == JeanX:
        if line == "yy":

            ch_j "Well, ok, sure."
        elif line == "my":

            ch_j "Well. . . she could be fun. . ."
        elif line == "ny":

            ch_j "Really? I mean, she could be fun."

        elif line == "ym" or line == "mm":

            ch_j "Well, ok, fine. . ."
        elif line == "nm":

            ch_j "Ok. I could think about it though."

        elif line == "yn" or line == "mn":

            ch_j "Well, cut it out."
        elif line == "nn":

            ch_j "Yeah."

    elif Party[0] == StormX:
        if line == "yy":

            ch_s "Oh, that will be nice. . ."
        elif line == "my":

            ch_s "Oh, you definitely should!"
        elif line == "ny":

            ch_s "That is too bad. You would go well together."

        elif line == "ym" or line == "mm":

            ch_s "Well, that should be fine."
        elif line == "nm":

            ch_s "You might want to reconsider. . ."

        elif line == "yn" or line == "mn":

            ch_s "I do not think we could deal with her."
        elif line == "nn":

            ch_s "Yes, we could agree with that."

    elif Party[0] == JubesX:
        if line == "yy":

            ch_v "Ok, cool."
        elif line == "my":

            ch_v "Yeah, sure, I guess we're down with that down with it."
        elif line == "ny":

            ch_v "Ok, but you might be missing out!"

        elif line == "ym" or line == "mm":

            ch_v "Ok, yeah, we can deal."
        elif line == "nm":

            ch_v "Ok, your call, I guess."

        elif line == "yn" or line == "mn":

            ch_v "Well. . . we might have some feelings."
        elif line == "nn":

            ch_v "Glad we're on the same page here."



    if line != "yy" and line != "nn":

        menu:
            extend ""
            "Ok, then I guess I will ask her to join us." if line in ("my","ny","ym","mm","nm"):

                $ line = "yy"
                $ Party[0].change_face("_smile")
                $ Party[1].change_face("_smile")
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
            "Well then, I guess I'll stop." if line in ("mn","yn"):

                $ line = "nn"
                $ Party[0].change_face("_normal")
                $ Party[1].change_face("_normal")
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

                pass

            "Well, I'm going to pass anyway." if line in ("ym","my","nm","ny","mm"):

                $ line = "nn"
                $ Party[0].change_face("_sad")
                $ Party[1].change_face("_sad")
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


        if line == "yy" or line == "nn":
            pass
        elif len(Player.Harem) >= 3:
            $ Party[0].change_face("_smile",eyes="_side")
            $ Party[1].change_face("_smile",eyes="_side")
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

            $ Count = 0
            while Count < 2:
                if approval_check(Party[Count], 1600) and Party[Count].likes[Newbie.tag] >= 500:

                    $ Party[Count].change_face("_sadside")
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

                    $ Party[Count].change_face("_angry",eyes="_side")
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
                    $ Party[Count].traits.append("ex")
                    $ Party[Count].broken_up[0] = 5 + Party[Count].broken_up[1] + Party[Count].cheated_on

                    $ Player.Harem.remove(Party[Count])
                    call remove_girl (Party[Count])
                $ Count += 1



    if line == "yy":
        if Newbie.tag + "No" in Player.traits:
            $ Player.traits.remove(Newbie.tag + "No")
        $ Player.drain_word(Newbie.tag + "No",0,0,1)
        $ Player.traits.append(Newbie.tag + "Yes")
        $ Count = len(Player.Harem)
        while Count:
            $ Count -= 1
            $ Player.Harem[Count].drain_word("saw with "+Newbie.tag,0,0,1)
        "You should give [Newbie.name] a call."
    else:
        $ Player.traits.append(Newbie.tag + "No")

    $ Party = []
    $ Count = 0
    return

label Harem_Initiation(temp_Girls=[], temp_Girls2=[]):


    $ temp_Girls = Player.Harem[:]
    while temp_Girls:
        $ temp_Girls2 = Player.Harem[:]
        while temp_Girls2:
            if temp_Girls[0] != temp_Girls2[0] and "poly " + temp_Girls2[0].tag not in temp_Girls[0].traits:
                $ temp_Girls[0].traits.append("poly " + temp_Girls2[0].tag)
            if temp_Girls[0] != temp_Girls2[0] and "saw with " + temp_Girls2[0].tag in temp_Girls[0].traits:
                $ temp_Girls[0].drain_word("saw with " + temp_Girls2[0].tag,0,0,1)
            $ temp_Girls2.remove(temp_Girls2[0])
        $ temp_Girls.remove(temp_Girls[0])
    return




label Call_For_Les(Girl=0, Girl2=0, temp_Girls=[]):


    if Girl not in active_Girls:
        $ temp_Girls = active_Girls[:]
        while temp_Girls and Girl not in active_Girls:
            if temp_Girls[0] not in Party and temp_Girls[0].location != bg_current and "lesbian" in temp_Girls[0].recent_history:


                $ Girl = temp_Girls[0]
                $ temp_Girls = [1]
            $ temp_Girls.remove(temp_Girls[0])
    if Girl in active_Girls and not Girl2:

        $ temp_Girls = active_Girls[:]
        $ temp_Girls.remove(Girl)
        while temp_Girls:
            if temp_Girls[0] not in Party and temp_Girls[0].location != bg_current and "lesbian" in temp_Girls[0].recent_history:


                if approval_check(temp_Girls[0], 1600 - temp_Girls[0].SEXP, taboo_modifier=0):
                    $ Girl2 = temp_Girls[0]
                    $ temp_Girls = [1]
                else:
                    return False
            $ temp_Girls.remove(temp_Girls[0])
    if Girl not in active_Girls or Girl2 not in active_Girls:

        return False

    show cellphone at sprite_location(stage_left)

    $ line = 0
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
    while not line and line != "what":
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
                hide cellphone
                jump reset_location
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
                $ line = "what"


    hide cellphone

    if bg_current == Girl.home:

        $ line = Girl
        $ Girl = Girl2
        $ Girl2 = line
    $ Girl.location = Girl.home
    $ Girl2.location = Girl.home
    $ bg_current = Girl.home
    $ taboo= 0
    $ Girl.taboo = 0
    $ Girl2.taboo = 0
    $ line = 0

    $ Girl.drain_word("lesbian",1,0)
    $ Girl2.drain_word("lesbian",1,0)

    $ Girl.add_word(0,"lesbian","lesbian")
    $ Girl2.add_word(0,"lesbian","lesbian")
    $ Girl.add_word(1,0,0,0,"les "+Girl2.tag)
    $ Girl2.add_word(1,0,0,0,"les "+Girl.tag)

    call set_the_scene (0, 1, 0, 0)
    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
    while line < 2:
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
                $ line = 2
            "Peek inside" if line != 1:
                call set_the_scene
                $ Girl.change_face("_kiss",1,eyes = "_closed")
                $ Girl2.change_face("_kiss",1,eyes = "_closed")
                $ Player.primary_action = "lesbian"
                $ girl_secondary_action = "fondle_pussy"
                $ second_girl_main_action = "fondle_pussy"
                "You see [Girl.name] and [Girl2.name], eyes closed and stroking each other vigorously."
                $ line = 1
            "Enter quietly":
                $ line = 2
            "Leave quietly":
                "You leave the girls to their business and slip out."
                $ Girl.thirst -= 30
                $ Girl.lust = 20
                $ Girl2.thirst -= 30
                $ Girl2lust = 20
                $ Girl.change_stat("love", 90, -3)
                $ Girl2.change_stat("love", 90, -3)
                $ renpy.pop_call()
                $ bg_current = "bg_campus"
                $ line = 0
                jump reset_location

    $ line = 0
    $ Girl.change_face("_sly",1)
    $ Girl2.change_face("_sly",1)
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

    $ Player.primary_action = "lesbian"
    $ girl_secondary_action = "fondle_pussy"
    $ second_girl_main_action = "fondle_pussy"
    $ Partner = Girl2
    call shift_focus(Girl)
    call Les_Prep(Girl)
    jump reset_location
    return

label Share(Girl=0, Other=0):



    $ Girl.drain_word("ask "+Other.tag,0,0,1)

    if Girl.broken_up[0]:

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

        if Other == JeanX or Other.likes[Girl.tag] >= 800 or approval_check(Other, 1800) or (approval_check(Other, 1500) and Other.likes[Girl.tag] >= 500):

            $ Other.add_word(1,0,0,"poly "+Girl.tag,0)


            $ Other.change_stat("obedience", 80, 10)
            $ Other.change_stat("inhibition", 80, 15)

            $ temp_Girls = Player.Harem[:]
            while temp_Girls:
                $ temp_Girls[0].drain_word("saw with "+Other.tag,0,0,1)
                $ temp_Girls.remove(temp_Girls[0])
            if Girl.event_happened[5]:

                $ Player.Harem.append(Other)

            elif bg_current in personal_rooms:

                if Other.tag+"Yes" not in Player.traits:
                    $ Player.traits.append(Other.tag+"Yes")
                call expression Other.tag + "_BF"
                $ renpy.pop_call()
                $ renpy.pop_call()
            else:

                if Other.tag+"Yes" not in Player.traits:
                    $ Player.traits.append(Other.tag+"Yes")
                call ask_to_meet(Other, "_bemused")
        else:

            "[Girl.name] sends you a text."
            Girl.voice "I talked to [Other.name] about sharing you, and she said she wasn't into that sort of thing,"
            if not approval_check(Other, 2000):
                $ Other.change_stat("love", 200, -15)
                $ Other.change_stat("obedience", 50, -5)
                $ Other.change_stat("inhibition", 50, 5)
                Girl.voice "She's just not into you like that."
            else:
                $ Other.change_stat("love", 200, -5)
                Girl.voice "She doesn't really like me that much. . ."


            $ Other.broken_up[0] = 7
    return
