
# Start Girl_Lesbian / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Les_Interupted(Girl=0,Girls=[]): #rkeljsv
        $ Girl = GirlCheck(Girl)
        # Called if you catch them fucking
        if "unseen" not in Girl.recent_history:
                if Girl.Org < 3 and Girl.Action:
                    menu:
                        "Did you want to stop them?"
                        "Yeah.":
                            pass
                        "No, let them keep going.":
                            $ Girl.Action -= 1 if Girl.Action > 0 else 0
                            jump Les_Cycle
                else:
                    if Girl == LauraX:
                            ch_l "Ahhh, that hit the spot. . ."
                    else:
                            call Anyline(Girl,"Ok, that's probably enough of that. . .")
                jump Les_After
        $ Girl.DrainWord("unseen",1,0) #She sees you, so remove unseens
        $ Partner.DrainWord("unseen",1,0) #She sees you, so remove unseens

        $ Girl.change_face("surprised", 1)
        $ Partner.change_face("surprised",2)

        "Suddenly, [Girl.name] jerks up from what she was doing with a start, and gives [Partner.name] a nudge."
        $ Girl.change_face("bemused", 0)
        $ Partner.change_face("perplexed",1)

        if Girl == RogueX:
                ch_r "Um, [Player.name], how long have you been watchin?"
        elif Girl == KittyX:
                ch_k "Eep! [Player.name], how long have you been there?!"
        elif Girl == EmmaX:
                ch_e "Hmm? [Girl.Petname], enjoying the show?"
        elif Girl == LauraX:
                ch_l "Oh! Hey [Player.name], how long have you been there?"
        elif Girl == JeanX:
                ch_j "Oh, hey [Player.name], get a good look?"
        elif Girl == StormX:
                ch_s "Oh? Hello [Girl.Petname]. Were you there long?"
        elif Girl == JubesX:
                ch_v "Oh? hey [Girl.Petname]. What'd you see?"
        $ Girl.Action -= 1 if Girl.Action > 0 else 0
        call Checkout(1)
        $ line = 0

        #If you've been jacking it
        if offhand_action == "jackin":
                $ Girl.Eyes = "down"
                if Girl == RogueX:
                        ch_r "And why is your cock out like that?!"
                elif Girl == KittyX:
                        ch_k "and why are you fapping?!"
                elif Girl == EmmaX:
                        ch_e "and was. . . that. .  really an appropriate reaction?"
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
                            $ Girl.change_face("sexy")
                            $ Girl.Statup("Obed", 50, 3)
                            $ Girl.Statup("Obed", 70, 2)
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
                            if Girl.Love >= 800 or Girl.Obed >= 500 or Girl.Inbt >= 500:
                                    $ temp_modifier += 10
                                    $ Girl.Statup("Lust", 90, 5)
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
                    #end "Yeah, it was an excellent show."

                    "I. . . just got here?":
                            $ Girl.change_face("angry")
                            $ Girl.Statup("Love", 70, 2)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 70, 2)
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
                            if Girl.Love >= 800 or Girl.Obed >= 500 or Girl.Inbt >= 500:
                                    $ temp_modifier += 10
                                    $ Girl.Statup("Lust", 90, 5)
                                    $ Girl.change_face("bemused", 1)
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
                                    $ temp_modifier -= 10
                                    $ Girl.Statup("Lust", 200, -5)
                    #end "I. . . just got here?"
                call Seen_First_Peen(Girl,Partner)
        #end "noticed you were jackin"
        else:
                #you haven't been jacking it
                menu:
                    extend ""
                    "Long enough.":
                            $ Girl.change_face("sexy", 1)
                            $ Girl.Statup("Obed", 50, 3)
                            $ Girl.Statup("Obed", 70, 2)
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
                            $ Girl.change_face("bemused", 1)
                            $ Girl.Statup("Love", 70, 2)
                            $ Girl.Statup("Love", 90, 1)
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
                            $ Girl.Statup("Obed", 50, 2)
                            $ Girl.Statup("Obed", 70, 2)

        if not ApprovalCheck(Girl, 1350):
                #If she doesn't like you enough to have you around. . .
                $ Girl.Statup("Love", 200, -5)
                $ Girl.change_face("angry")
                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
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
                        jump Player_Room

        if Round <= 10:
                #if there's no time, return
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

label LesScene(Girl=0,Bonus = 0,Girls=[]): #rkeljsv
        $ Girl = GirlCheck(Girl)
        call shift_focus(Girl)

        if not Girl.Action:
                #this is often called by the sex menu, and reverts if she's worn out.
                call Sex_Basic_Dialog(Girl,"tired")
                return

        if Girl.LesWatch:
                $ temp_modifier += 10
        elif Girl.Les:
                $ temp_modifier += 5
        if Girl.SEXP >= 50:
                $ temp_modifier += 25
        elif Girl.SEXP >= 30:
                $ temp_modifier += 15
        elif Girl.SEXP >= 15:
                $ temp_modifier += 5

        if Girl.Lust >= 90:
                $ temp_modifier += 5
        elif Girl.Lust >= 75:
                $ temp_modifier += 5

        elif Girl.Inbt >= 750:
                $ temp_modifier += 5

        if "exhibitionist" in Girl.Traits:
                $ temp_modifier += (3*Taboo)

        if Girl in Player.Harem or "sex friend" in Girl.Petnames:
                $ temp_modifier += 10
        elif "ex" in Girl.Traits:
                $ temp_modifier -= 40

        if Partner not in all_Girls:
                $ Partner = 0
                $ Girls = all_Girls[:]
                $ Girls.remove(Girl)
                while Girls:
                        if Girls[0].location == bg_current:
                                $ Partner = Girls[0]
                                $ Girls = [1]
                        $ Girls.remove(Girls[0])

        if Girl == JeanX:
                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                call Girl_Whammy(Partner)
        elif Partner == JeanX:
                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                call Girl_Whammy(Girl)

        $ line = Girl.GirlLikeCheck(Partner)
        if line >= 900:
                $ Bonus += 150
        elif line >= 800 or "poly "+Partner.Tag in Girl.Traits:
                $ Bonus += 100
        elif line >= 700:
                $ Bonus += 50
        elif line <= 200:
                $ Bonus -= 200
        elif line <= 500:
                $ Bonus -= 100
        $ Partner.DrainWord("unseen",1,0) #She sees you, so remove unseens
        $ line = 0

        $ Girl.AddWord(1,"noticed "+Partner.Tag,"noticed "+Partner.Tag) #ie $ Girl.recent_history.append("noticed Partner")
        $ Partner.AddWord(1,"noticed "+Girl.Tag,"noticed "+Girl.Tag) #ie $ Partner.recent_history.append("noticed Girl")

        if bg_current in PersonalRooms:
                $ Taboo = 0
                $ Girl.Taboo = 0
                $ Partner.Taboo = 0
        if Girl.ForcedCount and not Girl.Forced:
                $ temp_modifier -= 5 * Girl.ForcedCount

        $ Approval = ApprovalCheck(Girl, 1350, TabM = 2, Bonus = Bonus) # 1350, 1500, 1650, Taboo -800

        $ Girl.DrainWord("unseen",1,0) #She sees you, so remove unseens

        if action_context == "interrupted":
            menu:
                extend ""
                "I guess I should probably get going then. . .":
                        $ Girl.Statup("Love", 80, 3)
                        if Approval >= 2:
                                # if lead girl is very much in
                                if Girl == RogueX:
                                        ch_r "Well, I didn't say you had to leave. . ."
                                elif Girl == KittyX:
                                        ch_k "Hmmmm, I don't know about that. . ."
                                elif Girl == EmmaX:
                                        ch_e "Well, if [Partner.Tag]'s game. . ."
                                elif Girl == LauraX:
                                        ch_l "Hmmmm, I don't know about that. . ."
                                elif Girl == JeanX:
                                        ch_j "Well, you don't -have- to. . ."
                                elif Girl == StormX:
                                        ch_s "That really won't be necessary."
                                elif Girl == JubesX:
                                        ch_v "Orrr. . . you could join us?"
                                call Les_Response(Partner,Girl,3,B2=Bonus)
                                if not _return:
                                        return
                        else:
                                # If lead girl is only so/so, but Partner is on board, she tries to convince lead girl
                                call Les_Response(Partner,Girl,1,B2=Bonus)
                                if not _return:
                                        #this is the default reaction if Partner is not into it either
                                        if Approval:
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
                                                        ch_s "I am sorry, [Girl.Petname]. Perhaps some other time."
                                                elif Girl == JubesX:
                                                        ch_v "Oh, bummer, well see you later then."
                                                $ renpy.pop_call()
                                                $ renpy.pop_call()
                                                if bg_current == "bg_player":
                                                        jump Campus_Map
                                                else:
                                                        jump Player_Room
                                elif not Approval:
                                        #if Partner is in, but not lead girl
                                        if Girl == RogueX:
                                                ch_r "I'm sorry [Girl.Petname], I just am not interested in putting on a show."
                                        elif Girl == KittyX:
                                                ch_k "Sorry [Girl.Petname], I guess we'd like to keep this private."
                                        elif Girl == EmmaX:
                                                ch_e "So sorry [Girl.Petname], I suppose we'd like to keep this private."
                                        elif Girl == LauraX:
                                                ch_l "Sorry [Girl.Petname], maybe come back later."
                                        elif Girl == JeanX:
                                                ch_j "Hope you enjoyed the show, but we're a little busy. . ."
                                        elif Girl == StormX:
                                                ch_s "Well I'm afraid that I would rather you didn't stay."
                                        elif Girl == JubesX:
                                                ch_v "Sorry, not interested."
                                        return
                                elif not Girl.Action:
                                        #if she's tired out. . .
                                        if Girl == RogueX:
                                                ch_r "I'm sorry [Girl.Petname], I'm just too tuckered out right now. . ."
                                        elif Girl == KittyX:
                                                ch_k "Sorry [Girl.Petname], I'm kinda worn out already. . ."
                                        elif Girl == EmmaX:
                                                ch_e "So sorry [Girl.Petname], I needed a break. . ."
                                        elif Girl == LauraX:
                                                ch_l "Sorry [Girl.Petname], looks like we're taking a break. . ."
                                        elif Girl == JeanX:
                                                ch_j "I could use a break though. . ."
                                        elif Girl == StormX:
                                                ch_s "I did need to take a brief rest, however."
                                        elif Girl == JubesX:
                                                ch_v "I'm kinda worn out though."
                                        return
                                else:
                                        #if it all worked out. . .
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
                        #if it passed the hurdles. . .
                        $ focused_Girl = Girl
                        jump Les_Prep

                "So maybe I could join you girls?" if Player.Semen and Girl.Action:
                        $ Girl.change_face("sexy")
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
                        return                      #returns to sexmenu=
                "So maybe I could watch a bit longer?":
                        $ Girl.change_face("bemused", 1)
            #End "Interrupted" content.

        #first time
        if not Girl.LesWatch:
                $ Girl.change_face("surprised", 1,Mouth="kiss")
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
                if Girl.Forced:
                        $ Girl.change_face("sad")
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
        #end if first time. . .

        if Approval and (Partner == RogueX or Girl == RogueX) and "touch" not in RogueX.Traits:
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
        #end "can Rogue touch" check

        if not Girl.LesWatch and Approval:
                #First time dialog
                if Girl.Forced:
                        $ Girl.change_face("sad")
                        $ Girl.Statup("Love", 70, -3, 1)
                        $ Girl.Statup("Love", 20, -2, 1)
                elif Bonus >= 100:
                        $ Girl.change_face("sly", Eyes="side")
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
                elif Girl.Love >= (Girl.Obed + Girl.Inbt):
                        $ Girl.change_face("sexy")
                        $ Girl.Brows = "sad"
                        $ Girl.Mouth = "smile"
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
                elif Girl.Obed >= Girl.Inbt:
                        $ Girl.change_face("normal")
                        if Girl == RogueX:
                                ch_r "If that's what you want, [Girl.Petname]. . ."
                        elif Girl == KittyX:
                                ch_k "If that's what you want, [Girl.Petname]. . ."
                        elif Girl == EmmaX:
                                ch_e "If this is what gets you off, [Girl.Petname]. . ."
                        elif Girl == LauraX:
                                ch_l "I'm ok with that, [Girl.Petname]. . ."
                        elif Girl == JeanX:
                                ch_j "Ok, sure. . ."
                        elif Girl == StormX:
                                ch_s "I could be convinced. . ."
                        elif Girl == JubesX:
                                ch_v "If you like that. . ."
                else: # Uninhibited
                        $ Girl.change_face("sad")
                        $ Girl.Mouth = "smile"
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
                #End first time with approval dialogs

        elif Approval:
                    #Second time+ initial dialog
                    if Girl.Forced:
                            $ Girl.change_face("sad")
                            $ Girl.Statup("Love", 70, -3, 1)
                            $ Girl.Statup("Love", 20, -2, 1)
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
                    elif Approval and "lesbian" in Girl.recent_history:
                            $ Girl.change_face("sexy", 1)
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
                            $ focused_Girl = Girl
                            jump Les_Prep
                    elif Approval and "lesbian" in Girl.daily_history:
                            $ Girl.change_face("sexy", 1)
                            $ line = renpy.random.choice(["Enjoyed the show?",
                                    "Didn't get enough earlier?",
                                    "I don't mind having an audience. . ."])
                            call Anyline(Girl,line)
                    elif Girl.Les < 3:
                            $ Girl.change_face("sexy", 1)
                            $ Girl.Brows = "confused"
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
                            $ Girl.change_face("sexy", 1)
                            $ Girl.ArmPose = 2
                            $ line = renpy.random.choice(["You do like to watch.",
                                    "So you'd like us to go again?",
                                    "You want to watch some more?",
                                    "You want me to get it on with "+Partner.Tag+"?"])
                            call Anyline(Girl,line)
                    $ line = 0
                    #End second time+ initial dialog

        if Approval >= 2:
                    #If she's into it. . .
                    if Girl.Forced:
                            $ Girl.change_face("sad")
                            $ Girl.Statup("Obed", 90, 1)
                            $ Girl.Statup("Inbt", 60, 1)
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
                            $ Girl.change_face("sexy", 1)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Inbt", 50, 3)
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
                                            call Anyline(Girl,line)
                                    $ line = 0
                    $ Girl.Statup("Obed", 20, 1)
                    $ Girl.Statup("Obed", 60, 1)
                    $ Girl.Statup("Inbt", 70, 2)
                    jump Les_Partner
                    #end instant approval
        else:
            #If she's not into it, but maybe. . .
            if Girl == RogueX:
                    ch_r "I'm not sure about that though, [Girl.Petname]."
            elif Girl == KittyX:
                    ch_k "I don't know about that, [Girl.Petname]."
            elif Girl == EmmaX:
                    ch_e "I'm not sure about that, [Girl.Petname]."
            elif Girl == LauraX:
                    ch_l "I don't know, [Girl.Petname]."
            elif Girl == JeanX:
                    ch_j "Hmm. . . I don't know. . ."
            elif Girl == StormX:
                    ch_s "I am unsure. . ."
            elif Girl == JubesX:
                    ch_v "Well, but. . ."
            menu:
                "Maybe later?":
                        $ Girl.change_face("sexy", 1)
                        if Bonus >= 100:
                                $ Girl.Statup("Inbt", 90, 5)
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
                                $ Girl.GLG(Partner,800,3,1)
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
                                $ Girl.change_face("angry", 1, Eyes="side")
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
                        $ Girl.change_face("smile", 1)
                        $ Girl.Statup("Love", 80, 2)
                        $ Girl.Statup("Inbt", 70, 5)
                        call Taboo_Level
                        return
                        # end "Maybe later?"

                "You look like you might be into it. . .":
                        if Approval:
                                $ Girl.change_face("sexy")
                                $ Girl.Statup("Obed", 90, 4)
                                $ Girl.Statup("Obed", 50, 5)
                                $ Girl.Statup("Inbt", 70, 4)
                                $ Girl.Statup("Inbt", 40, 4)
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
                                        call Anyline(Girl,line)
                                call Anyline(Girl,line)
                                $ line = 0
                                jump Les_Partner

                "Just get at it already.":
                        # Pressured into it
                        $ Approval = ApprovalCheck(Girl, 550, "OI", TabM = 2) # 55, 70, 85
                        if Approval > 1 or (Approval and Girl.Forced):
                                $ Girl.change_face("sad")
                                $ Girl.Statup("Love", 70, -5, 1)
                                $ Girl.Statup("Love", 200, -5)
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
                                $ Girl.Statup("Obed", 80, 4)
                                $ Girl.Statup("Inbt", 80, 1)
                                $ Girl.Statup("Inbt", 60, 3)
                                $ Girl.Forced = 1
                                jump Les_Partner
                        else:
                                $ Girl.Statup("Love", 200, -20)
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
        # end of asking her to do it

        call Les_Response(Partner,Girl,1,B2=Bonus)
        if _return:
                #if the other girl convinces her
                $ Girl.change_face("smile", 1)
                if Girl == RogueX:
                        ch_r "Ok, fine! You've talked me into it."
                        ch_r "Get over here. . ."
                elif Girl == KittyX:
                        ch_k "Ok, if {i}you{/i} want to."
                        ch_k "Commere. . ."
                elif Girl == EmmaX:
                        ch_e "Well, if you insist, dear."
                        $ Girl.change_face("sly", 1)
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
                $ focused_Girl = Girl
                jump Les_Prep


        #She refused all offers.
        $ Girl.ArmPose = 1
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
        elif Girl.Forced:
                $ Girl.change_face("angry", 1)
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
                $ Girl.Statup("Lust", 90, 5)
                if Girl.Love > 300:
                        $ Girl.Statup("Love", 70, -2)
                $ Girl.Statup("Obed", 50, -2)
                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
        elif Girl.Taboo > 20:
                # she refuses and this is too public a place for her
                $ Girl.change_face("angry", 1)
                $ Girl.daily_history.append("tabno")
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
                $ Girl.Statup("Lust", 90, 5)
                $ Girl.Statup("Obed", 50, -3)
        elif Girl.Les:
                $ Girl.change_face("sad")
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
                $ Girl.change_face("normal", 1)
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
        $ temp_modifier = 0
        call Taboo_Level
        return

label Les_Partner:
        # This checks to see if the other girl is into it.
        # Girl and Girls are passed from previous label

        $ Girls = all_Girls[:]
        $ Girls.remove(Girl)
        while Girls:
                if Girls[0].location == bg_current:
                        call Les_Response(Girls[0],Girl,2)
                        if not _return:
                                # If she refused
                                return
                $ Girls.remove(Girls[0])
        #if nobody refuses, it passes through to the next label

label Les_Prep(Girl=focused_Girl,Girls=[]):
        #sets the scene up
        $ line = 0
        if Girl not in all_Girls or Girl == Partner:
                $ Girl = focused_Girl
                if Girl == Partner:
                    $ Partner = 0
                    $ line = 1

        if Partner not in all_Girls:
                $ Partner = 0
                $ Girls = all_Girls[:]
                $ Girls.remove(Girl)
                while Girls:
                        if Girls[0].location == bg_current:
                                $ Partner = Girls[0]
                                $ Girls = [1]
                        $ Girls.remove(Girls[0])

        if line:
                #if for some reason the Partner and lead were jumbled, swap them.
                call shift_focus(Partner)

        $ line = 0

        $ Girl.AddWord(1,"noticed "+Partner.Tag,"noticed "+Partner.Tag) #ie $ Girl.recent_history.append("noticed Partner")
        $ Partner.AddWord(1,"noticed "+Girl.Tag,"noticed "+Girl.Tag) #ie $ Partner.recent_history.append("noticed Girl")

        if "unseen" not in Girl.recent_history:
                #if she knows you're there. . .
                $ Girl.change_face("sexy")
                $ Girl.ArmPose = 2
                "[Girl.name] move's closer to [Partner.name] and wraps her arms around her neck."
                if not Girl.LesWatch:
                        #First time
                        if Girl.Forced:
                            $ Girl.Statup("Love", 90, -20)
                            $ Girl.Statup("Obed", 70, 55)
                            $ Girl.Statup("Inbt", 80, 55)
                        else:
                            $ Girl.Statup("Love", 90, 5)
                            $ Girl.Statup("Obed", 70, 20)
                            $ Girl.Statup("Inbt", 80, 60)
                call Les_FirstKiss
                $ girl_offhand_action == "kiss girl"
                $ Partner_primary_action == "kiss girl"

        $ primary_action = "lesbian"
        if action_context:
            $ renpy.pop_call()
            $ action_context = 0
        $ line = 0
        if Girl.Taboo:
            $ Girl.DrainWord("tabno")
        $ Girl.DrainWord("no_lesbian")
        $ Girl.AddWord(0,"lesbian","lesbian") #adds "lesbian" to daily and recent
        $ Partner.AddWord(0,"lesbian","lesbian") #adds "lesbian" to daily and recent

label Les_Cycle(Girl=focused_Girl):
        $ Girl = GirlCheck(Girl)
        while Round > 0:
            call shift_focus(Girl)
            call Les_Launch(Girl)
            $ Girl.LustFace()

            if  Player.Focus < 100:
                        #Player Command menu
                        menu:
                            "Keep watching. . .":
                                        pass

                            "\"Ahem. . .\"" if "unseen" in Girl.recent_history:
                                        jump Les_Interupted

                            "Start jack'in it." if offhand_action != "jackin":
                                        call Jackin(Girl)
                            "Stop jack'in it." if offhand_action == "jackin":
                                        $ offhand_action = 0

                            "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                        pass
                            "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                        "You concentrate on not burning out too quickly."
                                        $ Player.FocusX = 1
                            "Release your focus." if Player.FocusX:
                                        "You release your concentration. . ."
                                        $ Player.FocusX = 0

                            "Other options":
                                    menu:
                                        "Offhand action":
                                                if Girl.Action and MultiAction:
                                                        call Offhand_Set
                                                        if offhand_action:
                                                             $ Girl.Action -= 1
                                                else:
                                                        call Sex_Basic_Dialog(Girl,"tired")  # "I'm actually getting a little tired,"

                                        "Threesome actions":
                                            menu:
                                                "Ask [Girl.name] to do something else with [Partner.name]":
                                                        if "unseen" in Girl.recent_history:
                                                                ch_p "Oh yeah, why don't you. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Les_Change(Girl)
                                                "Ask [Partner.name] to do something else":
                                                        if "unseen" in Girl.recent_history:
                                                                ch_p "Oh yeah, why don't you. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Three_Change(Girl)

                                                "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                                            $ position_change_timer = 0
                                                "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                                        if "unseen" in Girl.recent_history:
                                                                ch_p "Oh, that's good. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                $ position_change_timer = 0

                                                #"Swap to [Partner.name]":
                                                            #call primary_action_Swap(Girl)
                                                "Undress [Partner.name]":
                                                        if "unseen" in Girl.recent_history:
                                                                ch_p "Oh, yeah, take it off. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Girl_Undress(Partner)
                                                                call shift_focus(Partner)
                                                                jump Les_Cycle
                                                "Clean up Partner":
                                                        if "unseen" in Girl.recent_history:
                                                                ch_p "You've got a little something. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Girl_Cleanup(Partner,"ask")
                                                                #call shift_focus(Partner)
                                                                jump Les_Cycle
                                                "Never mind":
                                                                jump Les_Cycle
                                        "undress [Girl.name]":
                                                        if "unseen" in Girl.recent_history:
                                                                ch_p "Oh yeah, why don't you. . ."
                                                                jump Les_Interupted
                                                        else:
                                                                call Girl_Undress(Girl)
                                        "Clean up [Girl.name] (locked)" if not Girl.Spunk:
                                                                pass
                                        "Clean up [Girl.name]" if Girl.Spunk:
                                                if "unseen" in Girl.recent_history:
                                                                ch_p "You've got a little something. . ."
                                                                jump Les_Interupted
                                                else:
                                                                call Girl_Cleanup(Girl,"ask")
                                        "Never mind":
                                                                jump Les_Cycle

                            "Back to Sex Menu" if MultiAction:
                                        ch_p "Let's try something else."
                                        $ action_context = "shift"
                                        $ line = 0
                                        jump Les_After
                            "End Scene" if not MultiAction:
                                        ch_p "Let's stop for now."
                                        $ line = 0
                                        jump Les_After
            #End menu (if line)

            call shift_focus(Girl)
            call Sex_Dialog(Girl,Partner)

            $ counter += 1
            $ Round -= 1

            $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

            if Player.Focus >= 100 or Girl.Lust >= 100:
                        #If either of you can cum:
                        if Player.Focus >= 100:
                                #If you can cum:
                                if "unseen" not in Girl.recent_history: #if she knows you're there
                                        call Player_Cumming(Girl)
                                        if "angry" in Girl.recent_history:
                                                call expression Girl.Tag + "_Pos_Reset"
                                                call expression Partner.Tag + "_Pos_Reset"
                                                return
                                        $ Girl.Statup("Lust", 200, 5)
                                        if 100 > Girl.Lust >= 70 and Girl.OCount < 2:
                                                $ Girl.recent_history.append("unsatisfied")
                                                $ Girl.daily_history.append("unsatisfied")
                                        $ line = "came"
                                else: #If she wasn't aware you were there
                                        "You grunt and try to hold it in."
                                        $ Player.Focus = 95
                                        jump Les_Interupted

                        if Girl.Lust >= 100:
                                        #If the lead Girl can cum
                                        call Girl_Cumming(Girl)
                                        jump Les_Interupted

                        if line == "came":
                                        $ line = 0
                                        if not Player.Semen:
                                                "You're emptied out, you should probably take a break."
            if Partner and Partner.Lust >= 100:
                    #Checks if partner could orgasm
                    call Girl_Cumming(Partner)

            #End orgasm

            $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

            if "unseen" in Girl.recent_history:
                    if Round == 10:
                            "It's getting a bit late, [Girl.name] and [Partner.name] will probably be wrapping up soon."
                    elif Round == 5:
                            "They're definitely going to stop soon."
            else:
                    if Round == 10:
                            call Sex_Basic_Dialog(Girl,10) #"You might want to wrap this up, it's getting late."
                    elif Round == 5:
                            call Sex_Basic_Dialog(Girl,5)   #"Seriously, it'll be time to stop soon."
        #Round = 0 loop breaks
        $ Girl.change_face("bemused", 0)
        $ line = 0
        if "unseen" not in Girl.recent_history:
                call Sex_Basic_Dialog(Girl,"done")   #"Ok, [Girl.Petname], that's enough of that for now."


label Les_After: #rkeljsv
        call expression Girl.Tag + "_Pos_Reset"
        if not Partner:
                $ temp_modifier = 0
                call Checkout
                return
        call expression Partner.Tag + "_Pos_Reset"
        $ Girl.change_face("sexy")
        if Partner == EmmaX:
                call Partner_Like(Girl,4)
        else:
                call Partner_Like(Girl,3)

        $ Girl.LesWatch += 1
        $ Partner.LesWatch += 1
        if Girl.LesWatch == 1:
                $ Girl.SEXP += 15
                if Girl.Love >= 500 and Girl.Org:
                        if Girl == RogueX:
                                ch_r "I have to say, I really enjoyed that one. . ."
                        elif Girl == KittyX:
                                ch_k "Hmm, that's kinda fun with an audience. . ."
                        elif Girl == EmmaX:
                                ch_e "I do enjoy an audience. . ."
                                $ Girl.change_face("sly",1)
                                ch_e "something to keep in mind?"
                        elif Girl == LauraX:
                                ch_l "I enjoyed the audience. . ."
                        elif Girl == JeanX:
                                ch_j "Nice having an audience there. . ."
                        elif Girl == StormX:
                                ch_s "I did enjoy being watched. . ."
                        elif Girl == JubesX:
                                ch_v "It was cool to have an audience. . ."
        if Partner.LesWatch == 1:
                $ Partner.SEXP += 15
                if Partner.Love >= 500 and Partner.Org:
                        if Partner == RogueX:
                                ch_r "I have to say, I really enjoyed that one. . ."
                        elif Partner == KittyX:
                                ch_k "Hmm, that's kinda fun with an audience. . ."
                        elif Partner == EmmaX:
                                ch_e "I do enjoy an audience. . ."
                                $ Partner.change_face("sly",1)
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
        $ Girl.AddWord(1,0,0,0,"les "+Partner.Tag) #ie $ Girl.recent_history.append("noticed Partner")
        $ Partner.AddWord(1,0,0,0,"les "+Girl.Tag) #ie $ Partner.recent_history.append("noticed Girl")
        $ temp_modifier = 0
        call Checkout
        return
    # End LesScene


label Post_Les_Dialog: #rkeljsv
        # called from Les_After if they have dialog for each other.
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

        if "les "+Partner.Tag in Girl.History:
                #if this wasn't the first time. . .
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
                # If this is the first time they've done this. . .
                # "les Kitty" not in RogueX.History. . .
                if Girl.GirlLikeCheck(Partner) >= 600:
                        #if the Lead girl likes the Partner. . .
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
                        #if the Lead girl doesn't like the Partner. . .
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

                #second girl response. . .
                if Partner.GirlLikeCheck(Girl) >= 600:
                        #if the Partner girl likes the Lead. . .
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
                        #if the Partner girl doesn't like the Lead. . .
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


#Start Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >
label Les_Response(Speaker=0,Subject=0, Step=1, B=0, B2=0, temp_modifier=0, Result=0, Approval = 0): #rkeljsv
        #Dialog for responses to Lesbian scenes, Subject is the lead, Speaker is typically Partner to the lead girl. Step is the phase of the conversation
        # B is the bonus of how much Speaker is into this, B2 is a bonus for how much Subject is into it
        # call Les_Response(RogueX,1)
        # call Les_Response(KittyX,RogueX,1)
        if Speaker not in all_Girls:
                $ Speaker = Partner
        if Subject not in all_Girls:
                $ Subject = focused_Girl
        if Speaker == EmmaX:
                #if Emma's not open to public sex yet, bailout
                if "three" not in EmmaX.History or "classcaught" not in EmmaX.History or (Taboo > 20 and "taboo" not in EmmaX.History):
                    $ EmmaX.recent_history.append("no_lesbian")
                    $ EmmaX.daily_history.append("no_lesbian")
                    $ EmmaX.Statup("Obed", 70, 5)
                    $ EmmaX.Statup("Inbt", 80, 5)
                    $ EmmaX.Statup("Lust", 50, 10)
                    $ Speaker.change_face("sadside", 1)
                    "[EmmaX.name] looks around furtively."
                    if Subject == StormX:
                            ch_e "Just to be clear, Ororo, I do -not- engage in sexual activities with students like [Player.name] here."
                            ch_e "I suppose I should excuse myself."
                            $ Subject.change_face("bemused", 1)
                            ch_s "Oh, yes, Ms. Frost. We would not wish to give the wrong impression."
                    else:
                            ch_e "I can't imagine why you would think I would engage in such behavior with a student!"
                    call remove_girl(EmmaX)
                    "She quickly leaves the room."
                    return 0

        if not Speaker.Action:
                #this is often called by the sex menu, and reverts if she's worn out.
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
                return 0

        if Speaker.Les:
                $ temp_modifier += 10
        if Speaker.SEXP >= 50:
                $ temp_modifier += 25
        elif Speaker.SEXP >= 30:
                $ temp_modifier += 15
        elif Speaker.SEXP >= 15:
                $ temp_modifier += 5

        elif Speaker.Inbt >= 750:
                $ temp_modifier += 5

        if "exhibitionist" in Speaker.Traits:
                $ temp_modifier += (3*Taboo)

        if Speaker in Player.Harem or "sex friend" in Speaker.Petnames:
                $ temp_modifier += 10
        elif "ex" in Speaker.Traits:
                $ temp_modifier -= 40

        # Provides a bonus based on how much the speaker likes the subject girl
        if Speaker.GirlLikeCheck(Subject) >= 900:
                $ B += 150
        elif Speaker.GirlLikeCheck(Subject) >= 800 or "poly " + Subject.Tag in Speaker.Traits:
                $ B += 100
        elif Speaker.GirlLikeCheck(Subject) >= 700:
                $ B += 50
        elif Speaker.GirlLikeCheck(Subject) <= 200:
                $ B -= 200
        elif Speaker.GirlLikeCheck(Subject) <= 500:
                $ B -= 100

        if Speaker == JeanX:
                $ B += 100

        $ Approval = ApprovalCheck(Speaker, 1300, TabM = 2, Bonus = B) # 1300, 1450, 1600, Taboo -800

        if not Approval:
                #if there's no chance, skip to the end
                pass
        elif Step == 1:
                #this is if the first girl's check failed, but the speaking girl likes her.
                if Approval >= 2 or B >= 150:
                        $ Speaker.change_face("sexy", 1)
                        if Speaker == RogueX:
                                ch_r "You sure [Subject.Tag]? Could be a lot of fun?"
                        elif Speaker == KittyX:
                                ch_k "Come on [Subject.Tag], it could be kinda fun."
                        elif Speaker == EmmaX:
                                ch_e "Oh come on [Subject.Tag], I could show you a few things."
                        elif Speaker == LauraX:
                                ch_l "It's really not bad, give it a shot."
                        elif Speaker == JeanX:
                                ch_j "Come on. . . [Subject.Tag], it could be fun."
                                $ B2 += 50
                        elif Speaker == StormX:
                                ch_s "Now [Subject.Tag], it would not be so bad, would it?"
                        elif Speaker == JubesX:
                                ch_v "Come on, you in, [Subject.Tag]? . ."
                        if B2 >= 100:
                                $ Result = 1
                                $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                                $ Subject.GirlLikeUp(Speaker,(int(B2/10))) #B2 sent by the call. . .
                else:
                        return Result

        elif Step == 2:
            #this is the second step, usually in the Prep phase
            if Approval >= 2:
                    $ Speaker.change_face("smile", 1)
                    if Speaker == RogueX:
                            ch_r "'Course!"
                    elif Speaker == KittyX:
                            ch_k "'Course!"
                    elif Speaker == EmmaX:
                            ch_e "Of course, [Speaker.Petname]."
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
            #if Approval, but not 2
            $ Speaker.change_face("sly", 2)
            if Speaker == RogueX:
                    if B >= 100:
                            ch_r "I don't know, maybe. . ."
                    if B >= 0:
                            ch_r "I'm not sure about her though. . ."
            elif Speaker == KittyX:
                    if B >= 100:
                            ch_k "Yeah, I mean I guess. . ."
                    if B >= 0:
                            ch_k "No offense [Subject.Tag], but. . ."
            elif Speaker == EmmaX:
                    if B >= 100:
                            ch_e "Mmmmm, certainly. . ."
                    if B >= 0:
                            ch_e "[Subject.Tag], dear, I don't really think so. . ."
            elif Speaker == LauraX:
                    if B >= 100:
                            ch_l "You're cute and all. . ."
                    if B >= 0:
                            ch_l "I don't know, [Subject.Tag]. . ."
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
            $ Speaker.Blush = 1
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
                                $ Speaker.change_face("smile")
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
                                        ch_l "Maybe. .. "
                                elif Speaker == JeanX:
                                        ch_j "Yeah, I guess. . ."
                                elif Speaker == StormX:
                                        ch_s "I suppose that I might. . ."
                                elif Speaker == JubesX:
                                        ch_v "I guess. . ."
                                $ Result = 1
                        else:
                                $ Speaker.change_face("sad", 2)
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
                        if ApprovalCheck(Speaker, 550, "OI", TabM = 2):
                                $ Speaker.change_face("sadside", 1)
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
                                $ Speaker.change_face("angry")
                                if Speaker == RogueX:
                                        ch_r "Who do you think you're talk'in to?"
                                elif Speaker == KittyX:
                                        ch_k "You're not the boss of me!"
                                elif Speaker == EmmaX:
                                        ch_e "Don't forget who's in charge here, [Speaker.Petname]"
                                elif Speaker == LauraX:
                                        ch_l "Don't push me."
                                elif Speaker == JeanX:
                                        ch_j "Don't you tell me what to \"get into.\""
                                elif Speaker == StormX:
                                        ch_s "This is not how one asks a favor."
                                elif Speaker == JubesX:
                                        ch_v "No way!"
                                $ Speaker.AddWord(1,"angry","angry") # adds to daily and recent
                "[Subject.name], what do you think?":
                        $ Subject.change_face("sexy", 1)
                        $ Speaker.GirlLikeUp(Subject,(int(B/10)))
                        if B >= 50:
                                $ Subject.GirlLikeUp(Speaker,5)
                        if Subject == RogueX:
                                if Speaker == KittyX:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "You know that we work well together."
                                    else:
                                            ch_r "It could be a lot of fun."
                                elif Speaker == EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "You could do that thing from last time. . ."
                                    else:
                                            ch_r "I was hoping you could give me some after class lessons. . ."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_r "Oh, it's not that bad."
                                    else:
                                            ch_r "It could be a lot of fun."
                        elif Subject == KittyX:
                                if Speaker == RogueX:
                                    if Subject.Les and Speaker.Les:
                                            ch_k "Come on [Speaker.Tag], you know we have fun."
                                    else:
                                            ch_k "Come on [Speaker.Tag], could be fun."
                                elif Speaker in (EmmaX,StormX):
                                    if Subject.Les and Speaker.Les:
                                            ch_k "I mean, it might be nice to show [Subject.Petname] what you've taught me. . ."
                                    else:
                                            ch_k "I've seen you watching me in class. . ."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_k "We have so much fun together though."
                                    else:
                                            ch_k "It could be fun!"
                        elif Subject == EmmaX:
                                if Speaker == StormX:
                                    ch_e "I really think we have a few things we could teach [EmmaX.Petname] here. . ."
                                elif Subject.Les and Speaker.Les:
                                    ch_e "What's the matter [Speaker.name], too shy around [Player.name]?"
                                else:
                                    ch_e "What's the matter [Speaker.name], I've seen how you look at me. . ."
                        elif Subject == LauraX:
                                if Speaker == EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_l "Wow, you aren't this shy when [Subject.Petname]'s not around."
                                    else:
                                            ch_l "Come on, you look really squishy."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_l "What, you don't want to fuck with [Player.name] around?"
                                    else:
                                            ch_l "Come on, you look like you have it in you."
                        elif Subject == JeanX:
                                if Speaker == EmmaX:
                                    ch_j "Come on, we both know you're into this shit."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_j "What, -now- you're getting shy?"
                                    else:
                                            ch_j "Come on, I bet you really get around."
                        elif Subject == StormX:
                                if Speaker == KittyX:
                                    if Subject.Les and Speaker.Les:
                                            ch_s "Now [Speaker.Tag], this certainly wouldn't be your first lesson. . ."
                                    else:
                                            ch_s "Now [Speaker.Tag], haven't you taken -any- interest in me?"
                                elif Speaker == EmmaX:
                                    if Subject.Les and Speaker.Les:
                                            ch_s "Now [Subject.Petname], that isn't what you've said in the past. . ."
                                    else:
                                            ch_s "Oh? You want to pass up the opportunity to teach [StormX.Petname] a few things. . ."
                                else:
                                    if Subject.Les and Speaker.Les:
                                            ch_s "You haven't enjoyed our time together?"
                                    else:
                                            ch_s "I can promise you would enjoy yourself. . ."
                        elif Subject == JubesX:
                                    if Subject.Les and Speaker.Les:
                                            ch_v "I mean, it's not like this is our -first time- or anything. . ."
                                    else:
                                            ch_v "I think I can carry my weight over here. . ."
                        #end dialogs from if you asked the other girl waht she thought. . .
                        #then the speaker responds. . .
                        if B >= 50:
                                #Yes
                                $ Speaker.change_face("smile", 1)
                                if Speaker == RogueX:
                                        ch_r "You know, I can't argue with that, [Subject.Tag]."
                                elif Speaker == KittyX:
                                        ch_k "Heh, I guess so, [Subject.Tag]."
                                elif Speaker == EmmaX:
                                        ch_e "If we must, [Subject.Tag]."
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
                                #No
                                $ Speaker.change_face("angry", 1, Eyes="side")
                                if Speaker == RogueX:
                                        ch_r "Sorry [Subject.Tag], nothin personal."
                                elif Speaker == KittyX:
                                        ch_k "Sorry [Subject.Tag], I don't mean anything personal."
                                elif Speaker == EmmaX:
                                        ch_e "I'm sorry [Subject.Tag], it's really not you."
                                elif Speaker == LauraX:
                                        ch_l "Sorry [Subject.Tag], it's not about you."
                                elif Speaker == JeanX:
                                        ch_j "Yeah, I'm really not interested."
                                elif Speaker == StormX:
                                        ch_s "I'm afraid not, [Subject.Tag]."
                                elif Speaker == JubesX:
                                        ch_v "No way, nothing personal, [Subject.Tag]."
                #end dialogs from if you asked the other girl waht she thought. . .
        if Step == 3:
                #This is a check if you interrupted them and Primary wants to do it, does Secondary?
                if Approval:
                        $ Speaker.change_face("smile", 1)
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
                        $ Speaker.change_face("sadside", 1)
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
                #response if all falls through and it fails. . .
                $ Speaker.recent_history.append("no_lesbian")
                $ Speaker.daily_history.append("no_lesbian")
                $ Speaker.change_face("sadside", 1)
                $ Partner = 0
                if Speaker == RogueX:
                        if B <= 0:
                                ch_r "Sorry, [Speaker.Petname], it's just not like that with her."
                        if Speaker.Taboo > 20:
                                ch_r "Sorry, [Speaker.Petname], this isn't a good place for it."
                        if B >= 100:
                                ch_r "Sorry, [Speaker.Petname], maybe if you weren't around. . ."
                        else:
                                ch_r "Sorry, [Speaker.Petname], I'm just not interested."
                elif Speaker == KittyX:
                        if B <= 0:
                                ch_k "Sorry, [Speaker.Petname], I'm just not into her."
                        if Speaker.Taboo > 20:
                                ch_k "Sorry, [Speaker.Petname], this isn't exactly the right place for that."
                        if B >= 100:
                                ch_k "Sorry, [Speaker.Petname], not with you watching. . ."
                        else:
                                ch_k "Sorry, [Speaker.Petname], I'm just not into it."
                elif Speaker == EmmaX:
                        if B <= 0:
                                ch_e "I'm sorry, [Speaker.Petname], she's just not my type."
                        if Speaker.Taboo > 20:
                                ch_e "I'm sorry, [Speaker.Petname], this would cause a scandal."
                        if B >= 100:
                                ch_e "I'm sorry, [Speaker.Petname], not with an audience. . ."
                        else:
                                ch_e "I'm sorry, [Speaker.Petname], I'm just not interested in that."
                elif Speaker == LauraX:
                        if B <= 0:
                                ch_l "Sorry, [Speaker.Petname], she's not my type."
                        if Speaker.Taboo > 20:
                                ch_l "Sorry, [Speaker.Petname], this area's a bit exposed."
                        if B >= 100:
                                ch_l "Sorry, [Speaker.Petname], I don't want an audience. . ."
                        else:
                                ch_l "Sorry, [Speaker.Petname], I'm just not into that."
                elif Speaker == JeanX:
                        if B <= 0:
                                ch_l "Sorry, [Speaker.Petname], I know I can do better than her."
                        if Speaker.Taboo > 20:
                                ch_l "Sorry, [Speaker.Petname]. . . not in public."
                        if B >= 100:
                                ch_l "Sorry, [Speaker.Petname], you'll have to earn that . ."
                        else:
                                ch_l "Sorry, [Speaker.Petname], not right now."
                elif Speaker == StormX:
                        if B <= 0:
                                ch_s "Apologies, [Speaker.Petname], I could not, with her."
                        if Speaker.Taboo > 20:
                                ch_s "Apologies, [Speaker.Petname], this is not the place for it."
                        if B >= 100:
                                ch_s "Apologies, [Speaker.Petname], this is a private affair. . ."
                        else:
                                ch_s "Apologies, [Speaker.Petname], I am just uninterested."
                elif Speaker == JubesX:
                        if B <= 0:
                                ch_v "Sorry, [Speaker.Petname], she's not my type."
                        if Speaker.Taboo > 20:
                                ch_v "Sorry, [Speaker.Petname], not here, at least."
                        if B >= 100:
                                ch_v "Sorry, [Speaker.Petname], I don't want an audience. . ."
                        else:
                                ch_v "Sorry, [Speaker.Petname], I'm not into it."
        # end failure text

        return Result

#End Girl.Les_Response >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >  >

label Les_FirstKiss:
        # called when there is a first kiss situation between two girls
        if "les " + Partner.Tag in Girl.History:
                #if they've been together before
                $ line = "experienced"
        elif Girl.Les and Partner.Les:
                #if both have kissed girls before
                $ line = "first both"
        elif Girl.Les:
                # Girl's had experience
                $ line = "first girl"
        elif Partner.Les:
                #Partner's had experience
                $ line = "first partner"

        if line == "experienced":
                "[Girl.name] and [Partner.name] move together in a passionate kiss."
                "[Girl.name]'s arms firmly grasp [Partner.name]'s neck and pull her close."
        else:
                if line in ("first both", "first girl"):
                        # Girl's first time
                        "[Girl.name] slowly moves in and gives [Partner.name] a soft kiss."
                else:
                        #not Girl's first time
                        "[Girl.name] casually places a hand on the back of [Partner.name]'s head and draws their lips together."
                if line == "first partner":
                        #other girl's first time
                        "[Partner.name] pulls back a bit, but slowly leans into the enbrace."
                else:
                        #not other girl's first time
                        "[Partner.name]'s lips curl up into a smile and she draws [Girl.name] even closer."
                "After a few seconds, it begins to grow more passionate."
        return
#End Girl.Les_Response / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl Whammy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Girl_Whammy(Other):
    #called when Jean is involved in a threesome, makes her whammy the other girl
    if "nowhammy" not in JeanX.Traits and Other.LikeJean < 800:
            #this raises a girl's like-Jean stat if Jean wants to sleep with her
            $ Player.AddWord(1,0,0,0,"whammied") #adds a whammied marker to the player's history for chat options
            if Other == EmmaX and EmmaX.Lvl >= JeanX.Lvl:
                    ch_e "Oh, don't even try that nonsense with me, Ms. Grey."
                    return
            if Other == JubesX and JubesX.Lvl >= JeanX.Lvl:
                    ch_v "Vampire whammy beats mutant whammy!"
                    return
            if "Jeaned" not in Other.Traits:
                    $ Other.Traits.append("Jeaned") #got whammied tag
                    $ setattr(JeanX,"LikeS"+Other.Tag,Other.LikeJean)     #$ JeanX.LikeSRogue = RogueX.LikeJean
            $ Other.LikeJean += 500 if Other.LikeJean <= 900 else Other.LikeJean
            $ Other.LikeJean = 900 if Other.LikeJean >= 900 else Other.LikeJean
    return
# End Girl Whammy / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Les activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Les_Change(Primary = 0, Secondary=Partner, D20S=0, PrimaryLust=0, SecondaryLust=0): #nee (D20S=0, Secondary=Partner, Primary = "Rogue", PrimaryLust=0, SecondaryLust=0):
        # for Lesbian primary activity: Threeway_Set(Primary,"preset", "lesbian", girl_offhand_action, ActiveGirl)
        #this is called when the player wants to change over a lesbian T3 behavior.
        # call Les_Change(RogueX)
        if Primary not in all_Girls:
                return
        $ line = 0
        menu:
            "Hey [Primary.name]. . ."
            "why don't you kiss her?" if Partner_offhand_action != "kiss girl" and Partner_offhand_action != "kiss both":
                        call Threeway_Set(Primary,"kiss girl", "lesbian", girl_offhand_action,Secondary)
            "why don't you grab her tits?" if girl_offhand_action != "fondle_breasts":
                        call Threeway_Set(Primary,"fondle_breasts", "lesbian", girl_offhand_action,Secondary)
            "why don't you suck her breasts?" if girl_offhand_action != "suck_breasts":
                        call Threeway_Set(Primary,"suck_breasts", "lesbian", girl_offhand_action,Secondary)
            "why don't you finger her?" if girl_offhand_action != "fondle_pussy":
                        call Threeway_Set(Primary,"fondle_pussy", "lesbian", girl_offhand_action,Secondary)
            "why don't you go down on her?" if girl_offhand_action != "eat_pussy":
                        call Threeway_Set(Primary,"eat_pussy", "lesbian", girl_offhand_action,Secondary)
            "why don't you grab her ass?" if girl_offhand_action != "fondle_ass":
                        call Threeway_Set(Primary,"fondle_ass", "lesbian", girl_offhand_action,Secondary)
            "why don't you lick her ass?" if girl_offhand_action != "eat_ass":
                        call Threeway_Set(Primary,"eat_ass", "lesbian", girl_offhand_action,Secondary)
            "never mind.":
                pass
        if not line:
            $ line = "You return to what you were doing."
        else:
            $ action_context = "skip"
        "[line]"
        return
# End Les activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
