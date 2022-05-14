
label AutoStrip(Girl=0):  #rkeljsv
        #this is called if they MUST strip to do a sex act, ie sex/anal
        $ Girl = GirlCheck(Girl)
        if (Girl.Panties and not Girl.PantiesDown) or Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6: #If she refuses to take off her pants but agreed to anal
            if Girl == RogueX:
                    ch_r "Well, I guess some things are necessary, [RogueX.Petname]."
            elif Girl == KittyX:
                    ch_k "We can't exactly do much like this, huh."
            elif Girl == EmmaX:
                    ch_e "I suppose we can't do much with all this on."
            elif Girl == LauraX:
                    ch_l "Huh. . ."
            elif Girl == JeanX:
                    ch_j "Huh. . ."
            elif Girl == StormX:
                    ch_s "I suppose our options are limited with these on."
            elif Girl == JubesX:
                    ch_v "Let's get these out of the way. . ."

            if (Girl.Panties and not Girl.PantiesDown) and (Girl.PantsNum() > 6 and not Girl.Upskirt):
                    "She quickly drops her pants and her [Girl.Panties]."
            elif (Girl.Panties and not Girl.PantiesDown) and (Girl.PantsNum() == 6 and not Girl.Upskirt):
                    "She quickly drops her shorts and her [Girl.Panties]."
            elif Girl.PantsNum() > 6 and not Girl.Upskirt:
                    "She tugs her pants down, exposing her bare pussy."
            elif Girl.PantsNum() == 6 and not Girl.Upskirt:
                    "She tugs her shorts down, exposing her bare pussy."
            elif Girl.HoseNum() >= 6 and (Girl.Panties and not Girl.PantiesDown):
                    "She tugs her [Girl.Hose] and [Girl.Panties] off."
            elif Girl.HoseNum() >= 6:
                    "She tugs her [Girl.Hose] off and drops them to the ground."
            elif (Girl.Panties and not Girl.PantiesDown):
                    "She tugs her [Girl.Panties] off and drops them to the ground."

        $ Girl.Upskirt = 1 if Girl.Legs else 0
        $ Girl.PantiesDown = 1 if Girl.Panties else 0
        $ Girl.Hose = 0 if Girl.HoseNum() >= 6 else Girl.Hose

        $ Girl.SeenPanties = 1
        call first_bottomless(Girl)
        return

label Girl_Undress(Girl=0,Region = "ask",CountStore=0): #rkeljsv
        #Called mostly from sex act menus when you want a girl to strip down
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        $ CountStore = temp_modifier
        if Partner == Girl:
                $ temp_modifier = 0
        call Shift_Focus(Girl)

        if Region == "auto":
                if Girl.Upskirt and Girl.PantiesDown:
                    return
                if Girl.PantsNum() > 5 and temp_modifier < 20:
                    $ temp_modifier = 20
                if Girl.Lust >= 90:
                    $ temp_modifier += 10
                elif Girl.Lust >= 80:
                    $ temp_modifier += 5
                $ Situation = "auto"
                call Bottoms_Off(Girl,0)

        if Region == "ask":
            menu:
                "Which parts?"
                "Her top" if Girl.Over or Girl.Chest or Girl.Arms or Girl.Acc:
                        $ Region = "top"
                "Her bottoms" if Girl.Legs or Girl.Panties or Girl.Hose or Girl.Acc:
                        $ Region = "bottom"
                "A little of both. . ." if Girl.Over or Girl.Chest or Girl.Legs or Girl.Panties or Girl.Hose or Girl.Acc:
                        $ Region = "both"
                "Never mind":
                        pass

        if Region == "top":
            if Girl.Over or Girl.Chest:
                call Top_Off(Girl,0)
        elif Region == "bottom":
            if Girl.Legs or Girl.Panties or Girl.Hose:
                call Bottoms_Off(Girl,0)
        elif Region == "both":
                if Girl.Over or Girl.Chest:
                        call Top_Off(Girl,0)

                if Partner == Girl:
                        $ temp_modifier = 0
                else:
                        $ temp_modifier = CountStore

                if "angry" in Girl.RecentActions:
                        pass
                elif not Girl.Legs and not Girl.Panties and not Girl.Hose:
                        pass
                elif "no topless" in Girl.RecentActions:
                        if Girl == RogueX:
                                ch_r "You might want to rethink your next question."
                        elif Girl == KittyX:
                                ch_k "Don't push it. . ."
                        elif Girl == EmmaX:
                                ch_e "Care to push your luck?"
                        elif Girl == LauraX:
                                ch_l "Know when to fold'em, [Girl.Petname]."
                        elif Girl == JeanX:
                                ch_j "Ha! Keep trying, [Girl.Petname]."
                        elif Girl == StormX:
                                ch_s "I do not see this going your way. . ."
                        elif Girl == JubesX:
                                ch_v "Well now you're pushing it. . ."
                        menu:
                            extend ""
                            "And now the bottoms?":
                                call Bottoms_Off(Girl,0)
                            "You're probably right, sorry.":
                                pass
                else:
                        ch_p "And now the bottoms?"
                        call Bottoms_Off(Girl,0)

        $ temp_modifier = CountStore
        return

label Top_Off(Girl=0,Intro = 1, Line = 0, Cnt = 0): #rkeljsv
        # Will she take her top off? Modifiers
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if not Girl.Over and not Girl.Chest:
                # If she's already topless. Just skip back.
                $ temp_modifier = 0
                return

        if "angry" in Girl.RecentActions:
                if Girl == RogueX:
                        ch_r "I'm just too annoyed to deal with this right now."
                elif Girl == KittyX:
                        ch_k "No titties for you."
                elif Girl == EmmaX:
                        ch_e "I'm in no mood, [Girl.Petname]."
                elif Girl == LauraX:
                        ch_l "Don't push it, [Girl.Petname]."
                elif Girl == JeanX:
                        ch_j "No way, [Girl.Petname]."
                elif Girl == StormX:
                        ch_s "These are not for your enjoyment."
                elif Girl == JubesX:
                        ch_v "The top stays on. . ."
                return

        if Girl.SeenChest and ApprovalCheck(Girl, 500) and not Taboo:
                #You've seen her tits.
                $ temp_modifier += 20
        if "exhibitionist" in Girl.Traits:
                $ temp_modifier += (4*Taboo)
        if Girl in Player.Harem or "sex friend" in Girl.Petnames and not Taboo:
                $ temp_modifier += 10
        elif "ex" in Girl.Traits:
                $ temp_modifier -= 40
        if "no topless" in Girl.RecentActions:
                $ temp_modifier -= 10
        elif Girl == StormX and (not Taboo or Girl in Rules):
                #Storm is more up for it if in private or with Xavier cleared
                $ temp_modifier += 20


        if Intro and not Girl.Uptop:
                if Intro == 2:
                        #It was an addiction scene
                        if Girl == RogueX:
                                ch_r "I don't know, you'd have to touch them. . ."
                        elif Girl == KittyX:
                                ch_k "So, you'd have to be able to[KittyX.like]touch them, I guess. . ."
                        elif Girl == EmmaX:
                                ch_e "I would probably need to be bare-chested to get anything out of that. . ."
                        elif Girl == LauraX:
                                ch_l "I'd need to be topless to get anything from that. . ."
                        elif Girl == JeanX:
                                ch_j "I guess I'd have to go topless. . ."
                        elif Girl == StormX:
                                ch_s "If direct contact is necessary. . ."
                        elif Girl == JubesX:
                                ch_v "Well, I'd need to be topless for that to. . ."
                else:
                        if Girl.Over:
                                ch_p "This might be easier without your [Girl.Over] on."
                        elif Girl.Chest:
                                ch_p "This might be easier without your [Girl.Chest] on."


        $ Approval = ApprovalCheck(Girl, 1100, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen

        if Situation == "auto" and  (Girl.Over or Girl.Chest or (Girl == JubesX and Girl.Acc)) and not Girl.Uptop:
                $ Line = 0
                if ApprovalCheck(Girl, 1250, TabM = 1) or (Girl.SeenChest and ApprovalCheck(Girl, 500) and not Taboo):
                        #if she'd go topless
                        $ Girl.Statup("Inbt", 70, 1)
                        $ Girl.Uptop = 1
                        $ Line = Girl.Over if Girl.Over else Girl.Chest
                        "[Girl.Name] sighs in frustration, and pulls her [Line] up over her breasts."
                        if Girl == RogueX:
                                ch_r "I just wasn't getting much out of it that way."
                        elif Girl == KittyX:
                                ch_k "I[Girl.like]wasn't feeling it that way."
                        elif Girl == EmmaX:
                                ch_e "Sometimes only direct contact will do."
                        elif Girl == LauraX:
                                ch_l "That wasn't working out."
                        elif Girl == JeanX:
                                ch_j "Ok, try that now, [Girl.Petname]."
                        elif Girl == StormX:
                                ch_s "Does that work better?"
                        elif Girl == JubesX:
                                ch_v "Ok, that's more comfortable. . ."
                        if Taboo:
                            $ Girl.Statup("Inbt", 90, (int(Taboo/20)))
                        call first_topless(Girl, silent = 1)
                elif Girl.Over and Girl.Chest and ApprovalCheck(Girl, 800, TabM = 1):
                        #if she won't go topless, but has a bra on. . .
                        $ Girl.Statup("Inbt", 40, 1)
                        $ Line = Girl.Over
                        $ Girl.Over = 0
                        if Girl == KittyX:
                                "[Girl.Name] sighs in frustration, and her [Line] drops to the ground."
                        elif Girl == JubesX:
                                if Girl.Acc:
                                        $ Girl.Acc = 0
                                        "[Girl.Name] sighs in frustration, and shrugs off her Jacket, before pulling her [Line] over her head."
                                else:
                                        "[Girl.Name] sighs in frustration, and pulls her [Line] over her head, throwing it aside."
                        else:
                                "[Girl.Name] sighs in frustration, and pulls her [Line] over her head, throwing it aside."
                        if Girl == RogueX:
                                ch_r "I just wasn't getting much out of it that way."
                        elif Girl == KittyX:
                                ch_k "I[Girl.like]wasn't feeling it that way."
                        elif Girl == EmmaX:
                                ch_e "I just wasn't getting much out of it that way."
                        elif Girl == LauraX:
                                ch_l "That wasn't working out."
                        elif Girl == JeanX:
                                ch_j "Ok, try that now, [Girl.Petname]."
                        elif Girl == StormX:
                                ch_s "Does that work better?"
                        elif Girl == JubesX:
                                ch_v "Ok, that's a bit better. . ."


                $ Line = 0
                return

        if Approval >= 2: #(Girl.Love + Girl.Obed + Girl.Inbt + (2*temp_modifier) - (4*Taboo)) >= 1250:
            # Does she assume top off?
            if "no topless" in Girl.DailyActions:
                    if Girl == RogueX:
                            ch_r "Ok, fine, top off."
                    elif Girl == KittyX:
                            ch_k "Okay, okay!"
                    elif Girl == EmmaX:
                            ch_e "{i}Fine,{/i} if that will shut you up."
                    elif Girl == LauraX:
                            ch_l "{i}Fine,{/i} but don't think I'm getting soft on you."
                    elif Girl == JeanX:
                            ch_j "Oh, fine. . ."
                    elif Girl == StormX:
                            ch_s "Oh, if you insist. . ."
                    elif Girl == JubesX:
                            ch_v "Well if you insist. . ."
            $ Girl.FaceChange("sexy", 1)
            if Girl.Forced:
                    $ Girl.FaceChange("sad", 1)
                    $ Girl.Statup("Love", 20, -2, 1)
                    $ Girl.Statup("Love", 70, -3, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1)
            $ Girl.Statup("Inbt", 50, 3)
            $ Cnt = 1
            while (Girl.Chest or Girl.Over or (Girl == JubesX and Girl.Acc)) and Cnt:
                if Girl == RogueX:
                        ch_r "So, [Girl.Petname]. Did you want me to take my top off?"
                elif Girl == KittyX:
                        ch_k "So[Girl.like]how much did you want me to take off?"
                elif Girl == EmmaX:
                        ch_e "What was it you were interested in, [Girl.Petname]?"
                elif Girl == LauraX:
                        ch_l "What did you want to see, [Girl.Petname]?"
                elif Girl == JeanX:
                        ch_j "Oh, what were you looking to see, [Girl.Petname]."
                elif Girl == StormX:
                        ch_s "What should I remove?"
                elif Girl == JubesX:
                        ch_v "Ok then, so what did you want off?"
                menu:
                    #Menu All off?
                    extend ""

                    "Why don't you lose the jacket?" if Girl == JubesX and Girl.Acc:
                            $ Girl.Acc = 0
                            "[Girl.Name] shrugs her jacket off."

                    "Lose the [Girl.Over]." if Girl.Over:
                            $ Girl.FaceChange("bemused", 1)
                            $ Line = Girl.Over
                            $ Girl.Over = 0
                            if Girl == KittyX:
                                    "[Girl.Name] shrugs and her [Line] falls through to the ground."
                            else:
                                    "[Girl.Name] pulls her [Line] off and tosses it aside."

                    "Why don't you lose the [Girl.Neck]?" if Girl.Neck:
                            $ Line = Girl.Neck
                            $ Girl.Neck = 0
                            "[Girl.Name] pulls her [Line] off."

                    "Just lose the [Girl.Chest]." if Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)
                            $ Line = Girl.Chest
                            $ Girl.Chest = 0
                            if Girl == KittyX:
                                    "[Girl.Name] reaches through her top and pulls her [Line] free, dropping it to the ground."
                            else:
                                    "[Girl.Name] slowly removes her [Line] from under the [Girl.Over]."
                    "Lose the [Girl.Chest]." if not Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)
                            $ Line = Girl.Chest
                            $ Girl.Chest = 0
                            if Girl == KittyX:
                                    "[Girl.Name] shrugs and her [Line] falls through to the ground."
                            else:
                                    "[Girl.Name] throws off her [Line]."
                    "Just pull it up." if (Girl.Over or Girl.Chest) and not Girl.Uptop:
                            $ Girl.FaceChange("bemused", 1)
                            $ Girl.Uptop = 1
                            if Girl == EmmaX:
                                    "[Girl.Name] smiles and pulls out her tits. . ."
                            elif Girl.Over and Girl.Chest:
                                    "[Girl.Name] smiles and lifts up her tops. . ."
                            else:
                                    "[Girl.Name] smiles and lifts up her top. . ."
                    "Lose both tops." if Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)
                            if Girl == KittyX:
                                    $ Girl.Over = 0
                                    $ Girl.Chest = 0
                                    "[Girl.Name] shrugs and her tops fall through her body to the ground."
                            else:
                                    if Girl == JubesX and Girl.Acc:
                                            $ Girl.Acc = 0
                                            "[Girl.Name] pulls off her jacket. . ."
                                    $ Line = Girl.Over
                                    $ Girl.Over = 0
                                    "[Girl.Name] tosses the [Line] over her head. . ."
                                    $ Line = Girl.Chest
                                    $ Girl.Chest = 0
                                    ". . .and then the [Line] as well."
                    "Lose the [Girl.Arms]. . ." if Girl.Arms:
                            $ Girl.FaceChange("sexy")
                            $ Line = Girl.Arms
                            $ Girl.Arms = 0
                            "She pulls off her [Line]."

                    "Why don't you lose the suspenders?" if Girl.Acc == "suspenders" or Girl.Acc == "suspenders2":
                            $ Girl.Acc = 0
                            "[Girl.Name] pulls her suspenders off."

                    "Why don't you lose the hoops?" if Girl.Acc == "rings" or Girl.Acc == "rings":
                            $ Girl.Acc = 0
                            "[Girl.Name] pulls her hoops off."

                    "Why don't you lose the hat?" if Girl.Hair == "hat" or Girl.Hair == "hat wet":
                            $ Girl.Hair == "wet" if Girl.Hair == "hat wet" else "wave"
                            "[Girl.Name] tosses her hat aside."

                    "That's enough. [[exit]":
                            $ Girl.FaceChange("bemused", 1)
                            call AnyLine(Girl,"All right, "+Girl.Petname+".")
                            $ Cnt = 0
            if Girl.ChestNum() < 3 and Girl.OverNum() < 3:
                    #if her top's are off. . .
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    call first_topless(Girl)
            $ Girl.Statup("Lust", 80, 3)
            $ Girl.RecentActions.append("ask topless")
            $ Girl.DailyActions.append("ask topless")
            $ temp_modifier = 0
            return

        #Else, Doesn't automatically want to lose the top//////////////////////////////////

        $ Girl.FaceChange("bemused", 1)
        if Girl == RogueX:
                if Intro == "massage" and not Approval:
                    ch_r "I'm ok with a massage, but my top stays on."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_r "I just told you no, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_r "I'd like to leave something to the imagination. . ."
                elif not Girl.SeenChest:
                    ch_r "I'm not ready to show you those yet. . ."
                elif "no topless" in Girl.DailyActions:
                    ch_r "I wasn't into it earlier, [Girl.Petname], what's changed?"
                elif "ask topless" in Girl.RecentActions:
                    ch_r "Changed your mind, [Girl.Petname]?"
                elif Taboo:
                    ch_r "It's a bit exposed here. . ."
                elif Approval:
                    ch_r "Well, you've seen them before, but. . ."
                else:
                    ch_r "Not right now."
        elif Girl == KittyX:
                if Intro == "massage" and not Approval:
                    ch_k "A massage is fine, but I'm keeping my top on, ok?"
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_k "I[Girl.like]already told you, no way!"
                elif Approval and not Girl.SeenChest:
                    ch_k "I'm[Girl.like]not really comfortable with that."
                elif not Girl.SeenChest:
                    ch_k "I'd[Girl.like]really rather not, ok?"
                elif "no topless" in Girl.DailyActions:
                    ch_k "Do you[Girl.like]think something's changed since earlier?"
                elif "ask topless" in Girl.RecentActions:
                    ch_k "Did you[Girl.like]want something else off?"
                elif Taboo:
                    ch_k "I'm[Girl.like]not that comfortable out here. . ."
                elif Approval:
                    ch_k "Maybe not?"
                else:
                    ch_k "Nu-uh."
        elif Girl == EmmaX:
                if Intro == "massage" and not Approval:
                    ch_e "I welcome a massage, but I'm staying fully dressed."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_e "Learn from previous mistakes, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_e "I don't know if that would be appropriate."
                elif not Girl.SeenChest:
                    ch_e "I don't think you're ready for that."
                elif "no topless" in Girl.DailyActions:
                    ch_e "Are you still that obsessed?"
                elif "ask topless" in Girl.RecentActions:
                    ch_e "You want more?"
                elif Taboo:
                    ch_e "[Girl.Petname], not around prying eyes."
                elif Approval:
                    ch_e "Are you sure you're prepared?"
                else:
                    ch_e "No."
        elif Girl == LauraX:
                if Intro == "massage" and not Approval:
                    ch_l "I could use a massage, but I'm keeping my clothes on."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_l "Don't push it, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_l "I don't know, man."
                elif not Girl.SeenChest:
                    ch_l "I really don't think so."
                elif "no topless" in Girl.DailyActions:
                    ch_l "Dude, relax."
                elif "ask topless" in Girl.RecentActions:
                    ch_l "Again?"
                elif Taboo:
                    ch_l "[Girl.Petname], not around here, alright?"
                elif Approval:
                    ch_l "Are you sure?"
                else:
                    ch_l "No."
        elif Girl == JeanX:
                if Intro == "massage" and not Approval:
                    ch_j "Massage, yes, but top on."
                elif "no topless" in Girl.RecentActions:
                    $ JeanX.FaceChange("angry")
                    ch_j "Relax, [Girl.Petname]."
                #elif Approval and not Girl.SeenChest:
                    #ch_j "Hmm. . ."
                #elif not Girl.SeenChest:
                    #ch_j "Hm. . ."
                elif "no topless" in Girl.DailyActions:
                    ch_j "Not happening."
                elif "ask topless" in Girl.RecentActions:
                    ch_j "So soon?"
                elif Taboo:
                    ch_j "Hmm. . . not around here"
                elif Approval:
                    ch_j "Hmm. . ."
                else:
                    ch_j "No way."
        elif Girl == StormX:
                if Intro == "massage" and not Approval:
                    ch_s "I would enjoy a massage, but I'm staying fully clothed."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_s "I am not so pliable as that, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_s "I don't know if that would be appropriate."
                elif "no topless" in Girl.DailyActions:
                    ch_s "Do not ask again."
                elif "ask topless" in Girl.RecentActions:
                    ch_s "Oh, you'd like to see them again?"
                elif Taboo and Girl not in Rules:
                    ch_s "I'm afraid not in public, [Girl.Petname]."
                elif Approval:
                    ch_s "Are you Certain?"
                else:
                    ch_s "No."
        elif Girl == JubesX:
                if Intro == "massage" and not Approval:
                    ch_v "I could use a massage, but I'm keeping my clothes on."
                elif "no topless" in Girl.RecentActions:
                    $ Girl.FaceChange("angry")
                    ch_v "Don't push it, [Girl.Petname]."
                elif Approval and not Girl.SeenChest:
                    ch_v "I don't know, man."
                elif not Girl.SeenChest:
                    ch_v "I'm not cool with that."
                elif "no topless" in Girl.DailyActions:
                    ch_v "Dude, relax."
                elif "ask topless" in Girl.RecentActions:
                    ch_v "Again?"
                elif Taboo:
                    ch_v "[Girl.Petname], it's just public here?"
                elif Approval:
                    ch_v "I dunno, really?"
                else:
                    ch_v "Nah."
        menu:
            extend ""
            "Sorry, sorry." if "no topless" in Girl.RecentActions:
                $ Girl.FaceChange("bemused", 1)
                if Girl == RogueX:
                        ch_r "Ok, just. . . give it a rest, huh?"
                elif Girl == KittyX:
                        ch_k "It's cool, I get it, but[Girl.like]chill out, huh?"
                elif Girl == EmmaX:
                        ch_e "I can't blame you for your persistance, but learn from your errors."
                elif Girl == LauraX:
                        ch_l "Right, I get it, stay thirsty."
                elif Girl == JeanX:
                        ch_j "It's not like I can blame you, [Girl.Petname]."
                elif Girl == StormX:
                        ch_s "I cannot blame you."
                elif Girl == JubesX:
                        ch_v "Well, you can't win if the don't play, right?"

            "Ok, that's fine." if "no topless" not in Girl.RecentActions:
                if "ask topless" not in Girl.DailyActions:
                        $ Girl.Statup("Lust", 80, 3)
                        $ Girl.Statup("Love", 70, 1)
                        $ Girl.Statup("Love", 90, 1)
                        $ Girl.Statup("Inbt", 50, 3)
                if Girl.Forced:
                        $ Girl.Mouth = "grimace"
                        if Girl == RogueX:
                                ch_r "I really appreciate that."
                        elif Girl == KittyX:
                                ch_k "That's[Girl.like]really cool of you."
                        elif Girl == EmmaX:
                                ch_e "How. . . generous of you."
                        elif Girl == LauraX:
                                ch_l "Ok."
                        elif Girl == JeanX:
                                ch_j ". . ."
                        elif Girl == StormX:
                                ch_s "Good."
                        elif Girl == JubesX:
                                ch_v "Yeah, thanks. . ."
                        if "ask topless" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 20, 2)
                            $ Girl.Statup("Love", 70, 2)
                            $ Girl.Statup("Inbt", 60, 1)

            "How about just the jacket?" if Girl == JubesX and Girl.Acc:
                # asked to remove jacket
                if Girl.Over or Girl.Acc == "open jacket":
                        #if wearing a shirt
                        ch_v "Sure, I guess. . ."
                        $ Girl.Acc = 0
                        "[Girl.Name] shrugs off her Jacket."
                elif ApprovalCheck(Girl, 800, TabM = 2) and Girl.Chest: #80, 160 taboo
                        $ Girl.FaceChange("sexy")
                        ch_v "Well, I guess. . ."
                        $ Girl.FaceChange("bemused", 1)
                        $ Girl.Acc = 0
                        "[Girl.Name] shrugs off her Jacket."
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Inbt", 30, 2)
                elif not Girl.Chest:
                        $ Girl.Eyes = "surprised"
                        $ Girl.Blush = 2
                        ch_v "I kinda don't have anything under this. . ."
                        $ Girl.Statup("Inbt", 30, 1)
                        menu:
                            extend ""
                            "Ok, you can leave it on.":
                                    $ Girl.Mouth = "smile"
                                    $ Girl.Statup("Love", 70, 2)
                                    ch_v "Whew, thanks. . ."

                            "That doesn't bother me any.":
                                if ApprovalCheck(Girl, 500, "I", TabM=3) or ApprovalCheck(Girl, 1000, "LI", TabM=3):
                                    $ Girl.FaceChange("bemused", 1)
                                    ch_v "Whoa, spicy. . ."
                                    $ Girl.Statup("Obed", 20, 2)
                                    $ Girl.Statup("Obed", 60, 1)
                                    $ Girl.FaceChange("sexy")
                                    $ Girl.Acc = 0
                                    "[Girl.Name] shrugs off her Jacket."
                                    $ Girl.Over = 0
                                    $ Girl.Statup("Inbt", 30, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                                    call first_topless(Girl)
                                else:
                                    $ Girl.FaceChange("bemused")
                                    call Top_Off_Refused(Girl)

                            "I know, take it off.":
                                    call ToplessorNothing(Girl)
                        $ Girl.Blush = 1
                else:
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)
            #end "just the jacket?"
            "How about just the [Girl.Over]?" if Girl.Over:
                # asked to go shirtless.
                if ApprovalCheck(Girl, 800, TabM = 2) and Girl.Chest: #80, 160 taboo
                        $ Girl.FaceChange("sexy")
                        if Girl == RogueX:
                                ch_r "Well, that's no big deal I guess. . ."
                        elif Girl == KittyX:
                                ch_k "Um, I guess I could. . ."
                        elif Girl == EmmaX:
                                ch_e "Well, I suppose that would be fine. . ."
                        elif Girl == LauraX:
                                ch_l "I mean. . . I guess. . ."
                        elif Girl == JeanX:
                                ch_j "Sure, whatever."
                        elif Girl == StormX:
                                ch_s "I suppose so."
                        elif Girl == JubesX:
                                ch_v "Well, I guess. . ."
                        $ Girl.FaceChange("bemused", 1)
                        $ Line = Girl.Over
                        $ Girl.Over = 0
                        if Girl == KittyX:
                                "[Girl.Name] shrugs and her [Line] falls through to the ground."
                        elif Girl == JubesX:
                                if Girl.Acc:
                                        $ Girl.Acc = 0
                                        "[Girl.Name] shrugs off her Jacket, before pulling her [Line] over her head."
                                else:
                                        "[Girl.Name] pulls her [Line] over her head, throwing it aside."
                        else:
                                "[Girl.Name] tosses the [Line] over her head."
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Inbt", 30, 2)
                elif not Girl.Chest:
                        $ Girl.Eyes = "surprised"
                        $ Girl.Blush = 2
                        if Girl == RogueX:
                                ch_r "I'm not exactly decent under this, you know."
                        elif Girl == KittyX:
                                ch_k "I'd[Girl.like]be {i}totally{/i} exposed here."
                        elif Girl == EmmaX:
                                ch_e "I don't think you're prepared for what's under there."
                        elif Girl == LauraX:
                                ch_l "I don't really have anything on under here."
                        elif Girl == JeanX:
                                ch_j "I'm not wearing a bra at the moment."
                        elif Girl == StormX:
                                ch_s "I am naked under this, you know. . ."
                        elif Girl == JubesX:
                                ch_v "I kinda don't have anything under this. . ."
                        $ Girl.Statup("Inbt", 30, 1)
                        menu:
                            extend ""
                            "Ok, you can leave it on.":
                                    $ Girl.Mouth = "smile"
                                    $ Girl.Statup("Love", 70, 2)
                                    if Girl == RogueX:
                                            ch_r "Great!"
                                    elif Girl == KittyX:
                                            ch_k "Thanks!"
                                    elif Girl == EmmaX:
                                            ch_e "Good."
                                    elif Girl == LauraX:
                                            ch_l "Right."
                                    elif Girl == JeanX:
                                            ch_j "That's what I said."
                                    elif Girl == StormX:
                                            ch_s "Very well then."
                                    elif Girl == JubesX:
                                            ch_v "Whew, thanks. . ."

                            "That doesn't bother me any.":
                                if ApprovalCheck(Girl, 500, "I", TabM=3) or ApprovalCheck(Girl, 1000, "LI", TabM=3):
                                    $ Girl.FaceChange("bemused", 1)
                                    if Girl == RogueX:
                                            ch_r "Ooh, at least you know what you like"
                                    elif Girl == KittyX:
                                            ch_k "Why am I not surprised?"
                                    elif Girl == EmmaX:
                                            ch_e "Well, I suppose it couldn't hurt to try."
                                    elif Girl == LauraX:
                                            ch_l "Maybe it should. . ."
                                    elif Girl == JeanX:
                                            ch_j ". . ."
                                    elif Girl == StormX:
                                            ch_s "It doesn't bother me much either."
                                    elif Girl == JubesX:
                                            ch_v "Whoa, spicy. . ."
                                    $ Girl.Statup("Obed", 20, 2)
                                    $ Girl.Statup("Obed", 60, 1)
                                    $ Girl.FaceChange("sexy")
                                    $ Line = Girl.Over
                                    $ Girl.Over = 0
                                    if Girl == KittyX:
                                            "[Girl.Name] shrugs and her [Line] falls through to the ground."
                                    elif Girl == JubesX:
                                            if Girl.Acc:
                                                    $ Girl.Acc = 0
                                                    "[Girl.Name] shrugs off her Jacket, before pulling her [Line] over her head."
                                            else:
                                                    "[Girl.Name] and pulls her [Line] over her head, throwing it aside."
                                    else:
                                            "[Girl.Name] tosses the [Line] over her head."
                                    $ Girl.Over = 0
                                    $ Girl.Statup("Inbt", 30, 2)
                                    $ Girl.Statup("Inbt", 60, 1)
                                    call first_topless(Girl)
                                else:
                                    $ Girl.FaceChange("bemused")
                                    call Top_Off_Refused(Girl)

                            "I know, take it off.":
                                    call ToplessorNothing(Girl)
                        $ Girl.Blush = 1
                else:
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)
            #end "just the over?"

            "Come on, Please? [[take it all off]":
                # asked to go topless. 110, 270 Taboo
                if Approval and ApprovalCheck(Girl, 600, "L", TabM=1):
                        $ Girl.Statup("Obed", 40, 2)
                        $ Girl.FaceChange("sexy")
                        if Girl == RogueX:
                                if "no topless" in Girl.RecentActions:
                                    ch_r "You're pretty persistent, [Girl.Petname]. I guess this time it'll be rewarded. . ."
                                else:
                                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                        elif Girl == KittyX:
                                if "no topless" in Girl.RecentActions:
                                    ch_k "You just don't know when to quit. . . but you got lucky this time. . ."
                                else:
                                    ch_k "You[Girl.like]know how to ask nicely . . ."
                        elif Girl == EmmaX:
                                if "no topless" in Girl.RecentActions:
                                    ch_e "Fine, I can't take your constant begging."
                                else:
                                    ch_e "Well, I suppose if you ask nicely . . ."
                        elif Girl == LauraX:
                                    ch_l "Fine, you thirsty weirdo."
                        elif Girl == JeanX:
                                if "no topless" in Girl.RecentActions:
                                    ch_j "Oh, whatever."
                                else:
                                    ch_j "I guess. . ."
                        elif Girl == StormX:
                                    ch_s "Oh, very well."
                        elif Girl == JubesX:
                                    ch_v "Ok, fine, geeze."
                        $ Girl.Uptop = 1
                        "[Girl.Name] just pulls her top up over her tits."
                        $ Girl.Arms = 0
                        $ Girl.Statup("Inbt", 30, 2)
                        $ Girl.Statup("Inbt", 60, 1)
                        call first_topless(Girl)
                elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        if Girl == RogueX:
                                ch_r "Nuh uh, [Girl.Petname]."
                        elif Girl == KittyX:
                                ch_k "Noooope!"
                        elif Girl == EmmaX:
                                ch_e "Again, no."
                        elif Girl == LauraX:
                                ch_l "Still no."
                        elif Girl == JeanX:
                                ch_j "Still a \"no\" on that, [Girl.Petname]."
                        elif Girl == StormX:
                                ch_s "Not today, no."
                        elif Girl == JubesX:
                                ch_v "Nah. . ."
                        $ Girl.Statup("Love", 80, -5)
                        $ Girl.RecentActions.append("angry")
                        $ Girl.DailyActions.append("angry")
                else:
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)
            #end "all off?"

            "Lose the [Girl.Arms], at least. . ." if Girl.Arms:
                    $ Girl.FaceChange("sexy")
                    call AnyLine(Girl,"Oh, all right.")
                    $ Line = Girl.Arms
                    $ Girl.Arms = 0
                    "She pulls off her [Line]."
            "No, topless or nothing.":
                    #demanded topless 60, 260 taboo
                    call ToplessorNothing(Girl)

            "Never mind.":
                pass

        $ Girl.RecentActions.append("ask topless")
        $ Girl.DailyActions.append("ask topless")
        $ temp_modifier = 0
        return

label Top_Off_Refused(Girl=0): #rkeljsv
        #Called form Top_Off when you insist but she refuses
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        $ Girl.FaceChange("angry")
        if Girl == RogueX:
                if "no topless" in Girl.RecentActions:
                        ch_r "Get a clue, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:
                        ch_r "Give it a rest, [Girl.Petname]."
                else:
                        $ Girl.FaceChange("sad")
                        ch_r "I'm afraid not this time, [Girl.Petname]. Sure we can't have some fun anyway?"
        elif Girl == KittyX:
                if "no topless" in Girl.RecentActions:
                        ch_k "[Girl.Like]back off."
                elif "no topless" in Girl.DailyActions:
                        ch_k "Not today, maybe not ever, [Girl.Petname]."
                else:
                        $ KittyX.FaceChange("sad")
                        ch_k "[Girl.Like], no way, but I don't want to go. . ."
        elif Girl == EmmaX:
                if "no topless" in Girl.RecentActions:
                        ch_e "You should probably back off now."
                elif "no topless" in Girl.DailyActions:
                        ch_e "I'm tired of this, [Girl.Petname]."
                else:
                        ch_e "Is this a dealbreaker for you?"
        elif Girl == LauraX:
                if "no topless" in Girl.RecentActions:
                        ch_l "You're getting real close to the line, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:
                        ch_l "You keep coming back with this, [Girl.Petname]."
                else:
                        ch_l "Let it go?"
        elif Girl == JeanX:
                if "no topless" in Girl.RecentActions:
                        ch_j "Step carefully, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:
                        ch_j "Still on about that?"
                else:
                        ch_j "Careful. . ."
        elif Girl == StormX:
                if "no topless" in Girl.RecentActions:
                        ch_s "I will not move on this."
                elif "no topless" in Girl.DailyActions:
                        ch_s "Find your joy elsewhere, [Girl.Petname]."
                else:
                        ch_s "Do you insist on this path?"
        elif Girl == JubesX:
                if "no topless" in Girl.RecentActions:
                        ch_v "I thought I was clear. . ."
                elif "no topless" in Girl.DailyActions:
                        ch_v "Look, cut it out, [Girl.Petname]."
                else:
                        ch_v "Whoa, slow your roll there. . ."
        menu:
            extend ""
            "Sure, never mind." if "no topless" not in Girl.RecentActions:
                    $ Girl.FaceChange("sexy")
                    $ Girl.Statup("Love", 70, 2)
                    if Girl == RogueX or Girl == KittyX:
                            call AnyLine(Girl,"Great!")
                    else:
                            call AnyLine(Girl,"Good.")
            "Sorry, I'll drop it." if "no topless" in Girl.RecentActions:
                    if Girl == RogueX:
                            ch_r "Fine. . ."
                    elif Girl == KittyX:
                            ch_k "Good!"
                    else:
                            call AnyLine(Girl,"Good.")
            "No, I insist. . .":
                    $ Girl.Brows = "angry"
                    if Girl == RogueX:
                            $ Girl.Brows = "confused"
                            ch_r "Ok [Girl.Petname], your loss."
                    elif Girl == KittyX:
                            ch_k "Fine then!"
                    elif Girl == EmmaX:
                            ch_e "Very well."
                    elif Girl == LauraX:
                            ch_l "Your funeral."
                    elif Girl == JeanX:
                            $ Girl.FaceChange("smile")
                            ch_j "Well that was at least good for a laugh."
                    elif Girl == StormX:
                            ch_s "So be it."
                    elif Girl == JubesX:
                            ch_v "Too bad then. . ."
                    $ Girl.Statup("Lust", 50, 5)
                    $ Girl.Statup("Love", 70, -2, 1)
                    if "no topless" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 60, 4)
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")
        $ Girl.RecentActions.append("no topless")
        $ Girl.DailyActions.append("no topless")
        return

label ToplessorNothing(Girl=0): #rkeljsv
        #Called from Top_Off if you insist she go topless after she's declined.
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        $ Girl.FaceChange("angry")
        if ApprovalCheck(Girl, 800, "OI", TabM = 4) and ApprovalCheck(Girl, 400, "O", TabM = 3):
            $ Girl.Statup("Love", 20, -2, 1)
            $ Girl.Statup("Love", 70, -5, 1)
            $ Girl.Statup("Inbt", 60, 3)
            $ Girl.FaceChange("sad")
            if Girl == RogueX:
                    if "no topless" in Girl.RecentActions:
                        ch_r "Ok, ok, whatever."
                    else:
                        ch_r "Fine, if that's what you want."
            elif Girl == KittyX:
                    if "no topless" in Girl.RecentActions:
                        ch_k "Ok, fine. This time."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_k "Whatever."
            elif Girl == EmmaX:
                    if "no topless" in Girl.RecentActions:
                        ch_e "Oh, very well. . ."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_e "Fine."
            elif Girl == LauraX:
                    if "no topless" in Girl.RecentActions:
                        ch_l "Hrmph, whatever. . ."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_l "Ugh, whatever."
            elif Girl == JeanX:
                    if "no topless" in Girl.RecentActions:
                        ch_j "Ok, fine. . ."
                    else:
                        $ Girl.FaceChange("sad")
                        ch_j "Fine! . . whatever."
            elif Girl == StormX:
                    $ Girl.FaceChange("sad")
                    if "no topless" in Girl.RecentActions:
                        ch_s "I suppose sometimes I must. . ."
                    else:
                        ch_s "Fine."
            elif Girl == JubesX:
                    if "no topless" in Girl.RecentActions:
                        ch_v "Ok, fine, just quit asking."
                    else:
                        ch_v "Ok, fine, whatever."
            $ Girl.Statup("Obed", 60, 4)
            $ Girl.Statup("Obed", 90, 2)
            $ Girl.Uptop = 1
            "[Girl.Name] slowly pulls her top up over her tits."
            call first_topless(Girl)
        else:
            $ Girl.Statup("Love", 200, -10)
            $ Girl.Statup("Obed", 40, -1, 1)
            if Girl == RogueX:
                    if "no topless" in Girl.RecentActions:
                        ch_r "Seriously, cut this shit out."
                    else:
                        $Girl.Brows = "confused"
                        ch_r "\"Nothing\" it is then."
            elif Girl == KittyX:
                    if "no topless" in Girl.RecentActions:
                        ch_k "It[Girl.like]wasn't cute the first time."
                    else:
                        $ Girl.Brows = "angry"
                        ch_k "[Girl.Like]no way!"
            elif Girl == EmmaX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_e "Learn to take \"no\" for an answer."
                    else:
                        ch_e "I'm afraid not."
            elif Girl == LauraX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_l "You have got to chill."
                    else:
                        ch_l "Nope."
            elif Girl == JeanX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_j "Keep it under control."
                    else:
                        ch_j "Oh, no."
            elif Girl == StormX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_s "I say again, \"no.\"."
                    else:
                        ch_s "Then that would be a \"no.\"."
            elif Girl == JubesX:
                    if "no topless" in Girl.RecentActions:
                        $ Girl.Brows = "angry"
                        ch_v "Look, I told you, \"no.\"."
                    else:
                        ch_v "Sorry, no go."
            $ Girl.RecentActions.append("no topless")
            $ Girl.DailyActions.append("no topless")
            $ Girl.RecentActions.append("angry")
            $ Girl.DailyActions.append("angry")
        return

label Bottoms_Off(Girl=0,Intro = 1, Line = 0, Cnt = 0): #rkeljsv
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if not Girl.Legs and not Girl.Panties and not Girl.Hose:
                # If she's already bottomless. Just skip back.
                $ temp_modifier = 0
                return

        if "angry" in Girl.RecentActions:
                if Girl == RogueX:
                        ch_r "I'm just too annoyed to deal with this right now."
                elif Girl == KittyX:
                        ch_k "The only \"kitty\" you're getting is up here."
                elif Girl == EmmaX:
                        ch_e "I would give up on that."
                elif Girl == LauraX:
                        ch_l "You're barking up the wrong tree."
                elif Girl == JeanX:
                        ch_j "Definitely not, [Girl.Petname]."
                elif Girl == StormX:
                        ch_s "That is certainly optimistic."
                        ch_s "No."
                elif Girl == JubesX:
                        ch_v "Definitely not."
                return

        # Will she take her bottoms off Modifiers
        if Girl.SeenPussy and ApprovalCheck(Girl, 700): #You've seen her Pussy.
                $ temp_modifier += 20
        elif not Girl.Panties:
                $ temp_modifier -= 20
        elif Girl.SeenPanties and ApprovalCheck(Girl, 500): #You've seen her panties.
                $ temp_modifier += 5
        if Intro == "dildo":
                $ temp_modifier += 20
        if "exhibitionist" in Girl.Traits:
                $ temp_modifier += (Taboo * 5)
        if (Girl in Player.Harem or "sex friend" in Girl.Petnames) and not Taboo:
                $ temp_modifier += 10
        elif "ex" in Girl.Traits:
                $ temp_modifier -= 40
        if "no bottomless" in Girl.RecentActions:
                $ temp_modifier -= 20
        elif Girl == StormX and (not Taboo or Girl in Rules):
                #Storm is more up for it if in private or with Xavier cleared
                $ temp_modifier += 20

        if Intro:
                if Intro == 2 and Girl.PantsNum() > 5:
                        #It was an addiction scene
                        if Girl == RogueX:
                                ch_r "I don't know, I might need my knickers off for that. . ."
                        elif Girl == KittyX:
                                ch_k "So, you'd have to be able to[KittyX.like]touch down there, I guess. . ."
                        elif Girl == EmmaX:
                                ch_e "I would probably need to lose these to get anything out of that. . ."
                        elif Girl == LauraX:
                                ch_l "I'd need to be pantsless to get anything from that. . ."
                        elif Girl == JeanX:
                                ch_j "I guess I'd have to go bottomless. . ."
                        elif Girl == StormX:
                                ch_s "I will remove these then. . ."
                        elif Girl == JubesX:
                                ch_v "I guess these would get in the way. . ."
                else:
                        if Girl.Legs and not Girl.Upskirt: #fix jube
                                ch_p "This might be easier without your [Girl.Legs] on."
                        elif Girl.Panties and not Girl.PantiesDown:
                                ch_p "This might be easier without your [Girl.Panties] on."

        $ Approval = ApprovalCheck(Girl, 1200, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen

        if Situation == "auto":
            $ Cnt = 0

            if not Girl.Upskirt and not Girl.PantiesDown:
                if Girl.PantsNum() == 5:
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (Girl.SeenPussy and not Taboo): #fix jube
                            $ Girl.Statup("Inbt", 60, 1)
                            if Taboo:
                                    $ Girl.Statup("Inbt", 90, (int(Taboo/20)))
                            $ Girl.Upskirt = 1
                            "She slides her skirt up."
                            $ Cnt = 1

                if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                    if Girl.Panties:
                        #she has pants and panties on
                        if not Approval or (not Girl.SeenPanties and Taboo):
                            return
                    elif Approval < 2 or (not Girl.SeenPussy and Taboo):
                        return
                    elif Girl.Upskirt:
                        return
                    $ Girl.Statup("Inbt", 60, 1)
                    if Girl.HoseNum() >= 6:
                            $ Line = Girl.Hose
                            $ Girl.Hose = 0
                    $ Girl.Upskirt = 1

                    if Girl == KittyX:
                            if Girl.PantsNum(0) >= 6:
                                "[Girl.Name] grumbles to herself, and then allows her [Girl.Legs] to drop down her legs."
                            else:
                                "[Girl.Name] grumbles to herself, and then allows her [Line] to drop down her legs."
                            if Girl.Panties:
                                    $ Girl.SeenPanties = 1
                    elif Girl.Panties:
                            if Girl.PantsNum(0) >= 6:
                                "[Girl.Name] grumbles to herself, and then unzips her [Girl.Legs], sliding them down her legs."
                            else:
                                "[Girl.Name] grumbles to herself, and then pulls her [Line] down her legs."
                            $ Girl.SeenPanties = 1
                    else:
                            if Girl.PantsNum(0) >= 6:
                                "[Girl.Name] grumbles to herself, and then unzips her [Girl.Legs], sliding them off her bare ass."
                            else:
                                "[Girl.Name] grumbles to herself, and then pulls her [Line] down her bare ass."
                    call first_bottomless(Girl, 1)
                    if Taboo:
                        $ Girl.Statup("Inbt", 90, (int(Taboo/10)))
                    $ Cnt = 1

            if Girl.Panties and not Girl.PantiesDown:
                # Just wearing panties, lose them?
                if Approval >= 2 or (Girl.SeenPussy and not Taboo):
                    $ Girl.Statup("Inbt", 70, 2)
                    if Taboo:
                            $ Girl.Statup("Inbt", 90, (int(Taboo/10)))
                    $ Girl.PantiesDown = 1
                    if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                            $ Girl.Upskirt = 1 #fix jube
                    if Girl == KittyX:
                            if Cnt:
                                "With a second thought, [Girl.Name] lets her [Girl.Panties] drop too."
                            else:
                                "[Girl.Name] tsks in irritation, and her [Girl.Panties] slide off to the ground."
                    else:
                            if Cnt:
                                "[Girl.Name] tsks in irritation, and pulls down her [Girl.Panties] too."
                            else:
                                "[Girl.Name] tsks in irritation, and pulls down her [Girl.Panties]."
                    call first_bottomless(Girl, 1)
                    if Girl == RogueX:
                            ch_r "I wasn't getting anything out of it with those on. Give it another go."
                    elif Girl == KittyX:
                            ch_k "It's super annoying not being able to phase you through these."
                    elif Girl == EmmaX:
                            ch_e "That was just in the way."
                    elif Girl == LauraX:
                            ch_l "I guess all that was in the way."
                    elif Girl == JeanX:
                            ch_j "Ok, see if you can make that work, [Girl.Petname]."
                    elif Girl == StormX:
                            ch_s "That should simplify things. . ."
                    elif Girl == JubesX:
                            ch_v "Ok, that's a bit more comfortable. . ."
            return


        if Approval >= 2:
            #will she volunteer to strip to underwear?
            $ Girl.FaceChange("sexy", 1)
            if Girl.Forced:
                    $ Girl.FaceChange("sad", 1)
                    $ Girl.Statup("Love", 20, -2, 1)
                    $ Girl.Statup("Love", 70, -3, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1)
            if Girl == RogueX:
                    if Approval >= 3:
                        $ Line = "Hmmm, what do you want to see? . ."
                    else:
                        $ Line = "Well, ok. I'd kinda like to keep {i}some{/i} modesty though. . ."
            elif Girl == KittyX:
                    if Approval >= 3:
                        $ Line = "Heh, what would you like to see? . ."
                    else:
                        $ Line = "Ok, maybe, but don't push it. . ."
            elif Girl == EmmaX:
                    if Approval >= 3:
                        $ Line = "Mmmm, what would you like?"
                    else:
                        $ Line = "What would you have me take off?"
            elif Girl == LauraX:
                    if Approval >= 3:
                        $ Line = "What did you want off?"
                    else:
                        $ Line = "Hm, what did you want me to lose?"
            elif Girl == JeanX:
                    if Approval >= 3:
                        $ Line = "What did you want off?"
                    else:
                        $ Line = "Like. . . what? . ."
            elif Girl == StormX:
                        $ Line = "What would you have me remove?"
            elif Girl == JubesX:
                        $ Line =  "Well like what did you have in mind here?"
            call Bottoms_Off_Legs(Girl)

            if not Girl.Panties and Girl.RecentActions.count("bottomless") < 2:
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 50, 3)
                    $ Girl.Statup("Lust", 80, 3)

        elif Girl.Legs or Girl.Panties or Girl.Hose:
            # She'd rather not strip but might
            $ Girl.FaceChange("bemused", 1)
            if Girl == RogueX:
                    if "no bottomless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_r "What did I just tell you, [Girl.Petname]?"
                    elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        ch_r "I doubt your odds will be better here, [Girl.Petname]. . ."
                    elif Approval and not Girl.SeenPussy:
                        ch_r "Not everything, right?"
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_r "I'm not ready to show you that either."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_r "Have you forgot what I said earlier, [Girl.Petname]?"
                    elif Taboo:
                        ch_r "I don't know about doing it here. . ."
                    elif Approval:
                        ch_r "I don't know if I want to take my bottoms off. . ."
                    elif Girl.SeenPussy:
                        ch_r "Well, you've seen it before, but. . ."
                    else:
                        ch_r "I'm not taking my bottoms off."
            elif Girl == KittyX:
                    if "no bottomless" in Girl.RecentActions:
                        $ KittyX.FaceChange("angry")
                        ch_k "Last warning, [Girl.Petname]. No."
                    elif "no topless" in Girl.RecentActions:
                        $ KittyX.FaceChange("angry")
                        ch_k "Not learning from your mistakes here, [Girl.Petname]. . ."
                    elif Approval and not Girl.SeenPussy:
                        ch_k "I'm not sure about that. . ."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_k "That's a bit too far."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_k "Short memory, [Girl.Petname]?"
                    elif Taboo:
                        ch_k "This is[Girl.like]kinda public. . ."
                    elif Approval:
                        ch_k "I'm[Girl.like]not sure about this. . ."
                    elif Girl.SeenPussy:
                        ch_k "Well, you've seen[Girl.like]it before . . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_k "I'm keeping my pants on."
                    elif Girl.PantsNum(0) > 5:
                        ch_k "I'm keeping my shorts on."
                    else:
                        ch_k "I'm keeping my panties on."
            elif Girl == EmmaX:
                    if "no bottomless" in Girl.RecentActions:
                        $ EmmaX.FaceChange("angry")
                        ch_e "Stop asking, you're embarrassing yourself."
                    elif "no topless" in Girl.RecentActions:
                        $ EmmaX.FaceChange("angry")
                        ch_e "Do you really think that's likely?"
                    elif Approval and not Girl.SeenPussy:
                        ch_e "I don't know if you're ready for that."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_e "Be careful how far you push it. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_e "Don't you learn anything, [Girl.Petname]?"
                    elif Taboo:
                        ch_e "Not with so many eyes around, [Girl.Petname]. . ."
                    elif Approval:
                        ch_e "Probably not. . ."
                    elif Girl.SeenPussy:
                        ch_e "I think you've seen enough . . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_e "I'm keeping my pants on."
                    elif Girl.PantsNum(0) == 5:
                        ch_e "I'm keeping my skirt on."
                    elif Girl.PantsNum(0) == 6:
                        ch_e "I'm keeping my shorts on."
                    else:
                        ch_e "I'm keeping my panties on."
            elif Girl == LauraX:
                    if "no bottomless" in Girl.RecentActions:
                        $ LauraX.FaceChange("angry")
                        ch_l "Now you're just embarrassing yourself."
                    elif "no topless" in Girl.RecentActions:
                        $ LauraX.FaceChange("angry")
                        ch_l "This is really pushing it."
                    elif Approval and not Girl.SeenPussy:
                        ch_l "I don't know if you're earned that yet."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_l "Kinda pushing it, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_l "So thirsty. . ."
                    elif Taboo:
                        ch_l "This is pretty exposed, [Girl.Petname]. . ."
                    elif Approval:
                        ch_l "Probably not. . ."
                    elif Girl.SeenPussy:
                        ch_l "You've probably seen enough . . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_l "Well, I'm keeping my pants on."
                    elif Girl.PantsNum(0) == 5:
                        ch_l "Well, I'm keeping my skirt on."
                    elif Girl.PantsNum(0) == 6:
                        ch_l "Well, I'm keeping my shorts on."
                    else:
                        ch_l "Well, I'm keeping my panties on."
            elif Girl == JeanX:
                    if "no bottomless" in Girl.RecentActions:
                        $ JeanX.FaceChange("angry")
                        ch_j "Look, it's just not happening."
                    elif "no topless" in Girl.RecentActions:
                        $ JeanX.FaceChange("angry")
                        ch_j "Why did you think that would be different?"
                    elif Approval and not Girl.SeenPussy:
                        ch_j "Hmm. . . have your earned that. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_j "Again with this?"
                    elif Taboo:
                        ch_j "Not here, [Girl.Petname]. . ."
                    elif Approval:
                        ch_j "Hmm. . ."
                    elif Girl.SeenPussy:
                        ch_j "Hmm. . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_j "I'm keeping my pants on though."
                    elif Girl.PantsNum(0) == 5:
                        ch_j "I'm keeping my skirt on though."
                    elif Girl.PantsNum(0) == 6:
                        ch_j "I'm keeping my shorts on though."
                    else:
                        ch_j "I'm keeping my panties on though."
            elif Girl == StormX:
                    if "no bottomless" in Girl.RecentActions:
                        $ StormX.FaceChange("angry")
                        ch_s "You need to stop asking about that."
                    elif Taboo and Girl not in Rules:
                        ch_s "I cannot in public, [Girl.Petname]. . ."
                    elif Approval:
                        ch_s "I am unsure. . ."
                    elif Girl.PantsNum(0) > 6:
                        ch_s "I will be keeping my pants on."
                    elif Girl.PantsNum(0) == 5:
                        ch_s "I will be keeping my skirt on."
                    elif Girl.PantsNum(0) == 6:
                        ch_s "I will be keeping my shorts on."
                    else:
                        ch_s "I will be keeping my panties on."
            elif Girl == JubesX:
                    if "no bottomless" in Girl.RecentActions:
                        $ JubesX.FaceChange("angry")
                        ch_v "Don't have a cow, dude."
                    elif "no topless" in Girl.RecentActions:
                        $ JubesX.FaceChange("angry")
                        ch_v "Don't push it, [Girl.Petname]."
                    elif Approval and not Girl.SeenPussy:
                        ch_v "I don't know, man."
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_v "Kinda pushing it, [Girl.Petname]. . ."
                    elif "no bottomless" in Girl.DailyActions:
                        ch_v "So thirsty. . ."
                    elif Taboo:
                        ch_v "[Girl.Petname], it's just public here?"
                    elif Approval:
                        ch_v "Doubtful. . ."
                    elif Girl.SeenPussy:
                        ch_v "Need another look?"
                    elif Girl.PantsNum(0) > 6:
                        ch_v "Well, I'm keeping my pants on."
                    elif Girl.PantsNum(0) == 6:
                        ch_v "Well, I'm keeping my shorts on."
                    else:
                        ch_v "Well, I'm keeping my panties on."
            menu:
                extend ""
                "Ok, never mind." if "no bottomless" not in Girl.RecentActions:
                    if "ask bottomless" not in Girl.DailyActions:
                            $ Girl.Statup("Lust", 80, 2)
                            $ Girl.Statup("Love", 70, 1)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Inbt", 50, 3)
                    if Girl.Forced:
                            $ Girl.Mouth = "smile"
                            if Girl == RogueX:
                                    ch_r "I really appreciate that."
                            elif Girl == KittyX:
                                    ch_k ". . . thank you."
                            elif Girl == EmmaX:
                                    ch_e "Very. . . generous."
                            elif Girl == LauraX:
                                    ch_l "Right."
                            elif Girl == JeanX:
                                    ch_j ". . ."
                            elif Girl == StormX:
                                    ch_s "Thank you. . ."
                            elif Girl == JubesX:
                                    ch_v "Thanks. . ."
                            if "ask bottomless" not in Girl.DailyActions:
                                    $ Girl.Statup("Love", 20, 3)
                                    $ Girl.Statup("Love", 70, 4)
                                    $ Girl.Statup("Inbt", 60, 2)

                "Sorry, sorry." if "no bottomless" in Girl.RecentActions:
                            if Girl == RogueX:
                                    ch_r "Ok, fine, just chill out about it."
                            elif Girl == KittyX:
                                    ch_k "[Girl.Like], fine, whatever."
                            else:
                                    call AnyLine(Girl,"Good.")

                "Come on, Please?":
                        if "no bottomless" in Girl.DailyActions:
                                $ Girl.FaceChange("angry", 1)
                                if Girl == RogueX:
                                        ch_r "Listen up when I tell you \"no.\""
                                elif Girl == KittyX:
                                        ch_k "I already told you \"no.\""
                                elif Girl == EmmaX:
                                        ch_e "I believe you've heard my answer on that."
                                elif Girl == LauraX:
                                        ch_l "You heard me."
                                elif Girl == JeanX:
                                        ch_j "Are you deaf, or stupid?"
                                elif Girl == StormX:
                                        ch_s "I have spoken on the matter."
                                elif Girl == JubesX:
                                        ch_v "No."
                        else:
                            if Approval and ApprovalCheck(Girl, 600, "L", TabM=1):
                                $ Girl.FaceChange("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                $ Approval += 1 if D20 == 3 else 0
                                if Girl == RogueX:
                                        $ Line = "Well, what were you thinking then. . ."
                                elif Girl == KittyX:
                                        $ Line = "I guess. . ."
                                elif Girl == EmmaX:
                                        $ Line = "Perhaps. . ."
                                elif Girl == LauraX:
                                        $ Line = "Maybe. . ."
                                elif Girl == JeanX:
                                        $ Line = "-sigh-. . . like what?"
                                elif Girl == StormX:
                                        ch_s ". . ."
                                        $ Line = "What did you want? . ."
                                elif Girl == JubesX:
                                        $ Line =  "I mean, maaaybe. . ."
                                call Bottoms_Off_Legs(Girl)
                            else:
                                $ Girl.FaceChange("sexy")
                                call Bottoms_Off_Refused(Girl)

                "It doesn't have to be everything. . ." if Girl.Legs or Girl.HoseNum() >= 10 or Girl.Panties == "shorts":
                    if Approval and "no bottomless" not in Girl.DailyActions:
                            $ Girl.FaceChange("bemused", 1)
                            $ Line = "Well what did you have in mind then?"
                            call Bottoms_Off_Legs(Girl)
                    else:
                            # She refuses your request. . .
                            $ Girl.FaceChange("sexy")
                            call Bottoms_Off_Refused(Girl)
                "It doesn't have to be everything. . . (locked)" if not Girl.Legs and Girl.HoseNum() < 10 and Girl.Panties != "shorts":
                            pass

                "No, lose 'em.":            #85 and -200 taboo
                    if (Approval and Girl.Obed >= 250) or (ApprovalCheck(Girl, 850, "OI", TabM = 5) and ApprovalCheck(Girl, 400, "O")):
                                $ Girl.Statup("Love", 20, -1, 1)
                                $ Girl.Statup("Love", 70, -5, 1)
                                $ Girl.Statup("Obed", 50, 4)
                                $ Girl.Statup("Inbt", 60, 3)
                                if Girl == RogueX:
                                        $ Line =  "Fine, if that's what you want. What do you want to see?"
                                elif Girl == KittyX:
                                        $ Line =  "Like geez, you're serious. . ."
                                elif Girl == EmmaX:
                                        $ Line =  "Don't test me. . ."
                                elif Girl == LauraX:
                                        $ Line =  "Don't push me. . ."
                                elif Girl == JeanX:
                                        $ Line = "Think very carefully. . ."
                                elif Girl == StormX:
                                        ch_s ". . ."
                                        $ Line = "What did you want? . ."
                                elif Girl == JubesX:
                                        $ Line =  "Tone. . ."
                                $ Approval = 1 if Approval < 1 else Approval
                                $ Girl.Forced = 1
                                call Bottoms_Off_Legs(Girl)
                    else:
                        $ Girl.Statup("Love", 200, -10)
                        if ApprovalCheck(Girl, 400, "O"):
                                if Girl == RogueX:
                                        ch_r "I. . . I really can't."
                                elif Girl == KittyX:
                                        ch_k "Sorry[Girl.like]no way."
                                elif Girl == EmmaX:
                                        ch_e "Definitely not."
                                elif Girl == LauraX:
                                        ch_l "No way."
                                elif Girl == JeanX:
                                        ch_j "Ha! No."
                                elif Girl == StormX:
                                        ch_s "I am sorry, no."
                                elif Girl == JubesX:
                                        ch_v "Definitely not."
                        else:
                                $ Girl.FaceChange("angry")
                                if Girl == RogueX:
                                        ch_r "Well fuck off then!"
                                elif Girl == KittyX:
                                        ch_k "GTFO."
                                elif Girl == EmmaX:
                                        ch_e "Out of my sight, [Girl.Petname]."
                                elif Girl == LauraX:
                                        ch_l "Fuck off."
                                elif Girl == JeanX:
                                        ch_j "Not even."
                                elif Girl == StormX:
                                        ch_s "No."
                                elif Girl == JubesX:
                                        ch_v "Nah. . ."
                                $ Girl.RecentActions.append("angry")
                                $ Girl.DailyActions.append("angry")
                        $ Girl.RecentActions.append("no bottomless")
                        $ Girl.DailyActions.append("no bottomless")

        $ temp_modifier = 0
        $ Girl.RecentActions.append("ask bottomless")
        $ Girl.DailyActions.append("ask bottomless")
        return

label Bottoms_Off_Legs(Girl=0):  #rkeljsv
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if Girl.Forced:
            $ Girl.FaceChange("sad", 1)
        elif ApprovalCheck(Girl, 1100, "OI", TabM = 3):
            $ Girl.FaceChange("sly")
        elif ApprovalCheck(Girl, 1400, TabM = 3):
            $ Girl.FaceChange("sexy", 1)
        else:
            $ Girl.FaceChange("bemused", 1)

        $ Line = "Well what did you want off?" if not Line else Line
        $ Cnt = 1
        while Cnt and (Girl.Legs or Girl.Panties or Girl.Hose):
            call AnyLine(Girl,Line)
            menu:
                # She's asking what you'd like to see.
                extend ""
                "Take it all off" if Line != "Well what did you have in mind then?":
                        #approval a given
                        if not Girl.Panties and Girl.HoseNum() < 10:
                                call NoPantiesOn(Girl)

                        if Girl.Legs:
                                $ Line = Girl.Legs
                                $ Girl.Legs = 0
                                if not Girl.SeenPanties:
                                    if Girl == RogueX:
                                            "[Girl.Name] shyly removes her [Line]."
                                    elif Girl == KittyX:
                                            "[Girl.Name] shyly tugs her [Line] off of her legs."
                                    else:
                                            "[Girl.Name] pulls off her [Line]."
                                    $ Girl.SeenPanties = 1
                                else:
                                    "[Girl.Name] pulls her [Line] off."

                        if Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                                call NoPantiesOn(Girl)

                        if Girl == JubesX and JubesX.Acc != "shut jacket":
                                #if it's an ordinary jacket, leave it on
                                pass
                        elif Girl == JubesX and JubesX.Acc == "shut jacket":
                                $ Girl.Acc = 0
                                "She pulls her [Girl.Acc] off."
                                call first_bottomless(Girl)
                        elif Girl.Acc: #boots, mostly
                                $ Girl.Acc = 0
                                "She pulls her [Girl.Acc] off."

                        if Girl.Hose:
                                $ Line = Girl.Hose #HoseName
                                $ Girl.Hose = 0
                                if Girl == KittyX:
                                        "Her [Line] drop to the ground in a heap."
                                else:
                                        "She pulls her [Line] down."

                        if Approval < 2:
                                call NoPantiesOn(Girl)

                        if Girl.Panties:
                                $ Line = Girl.Panties
                                $ Girl.Panties = 0
                                if Girl == KittyX:
                                        "She glances up at you as her [Line] fall clear of her."
                                else:
                                        "She glances up at you as she removes her [Line]."
                        call first_bottomless(Girl)


                "Lose the [Girl.Legs]." if Girl.Legs:
                        if Girl.Panties and Approval >= 2:
                            $ Girl.FaceChange("sexy")
                            if Girl == RogueX:
                                    ch_r "I guess I could do that. . ."
                            elif Girl == KittyX:
                                    ch_k "That's. . . doable. . ."
                            elif Girl == EmmaX:
                                    ch_e "I can manage that. . ."
                            elif Girl == LauraX:
                                    ch_l "I guess I could. . ."
                            elif Girl == JeanX:
                                    ch_j ". . .I guess. . ."
                            elif Girl == StormX:
                                    ch_s "I could do that. . ."
                            elif Girl == JubesX:
                                    ch_v "Well, I could do that. . ."
                        elif Approval:
                                $ Girl.FaceChange("sexy", 1)
                                if Approval < 2 and not Girl.Panties and Girl.HoseNum() < 10:
                                    call NoPantiesOn(Girl)
                        else:
                                $ Girl.FaceChange("sexy")
                                call Bottoms_Off_Refused(Girl)
                                return

                        $ Line = Girl.Legs
                        $ Girl.Legs = 0
                        if not Girl.Panties and Girl.HoseNum() < 10:
                                $ Girl.FaceChange("sly", 2)
                                if Girl == KittyX:
                                        "She blushes and looks at you as her [Line] drops at her feet."
                                elif Girl == RogueX:
                                        "She blushes and looks at you slyly before removing her [Line]."
                                else:
                                        "She glaces at you slyly before removing her [Line]."
                                call first_bottomless(Girl)
                        elif not Girl.SeenPanties:
                                if Girl == KittyX:
                                        "She blushes and looks at you as her [Line] drops at her feet."
                                elif Girl == RogueX:
                                        "She blushes and looks at you slyly before removing her [Line]."
                                else:
                                        "She glaces at you slyly before removing her [Line]."
                                $ Girl.SeenPanties = 1
                        else:
                                "[Girl.Name] pulls her [Line] off."
                        $ Girl.FaceChange("bemused", 1)

                "Lose the [Girl.Panties]." if Girl.Panties:
                        if Approval < 2:
                                if Girl == RogueX:
                                        ch_r "No thanks, [Girl.Petname]."
                                elif Girl == KittyX:
                                        ch_k "Sorry, no."
                                elif Girl == EmmaX:
                                        ch_e "I'm afraid not."
                                elif Girl == LauraX:
                                        ch_l "No way."
                                elif Girl == JeanX:
                                        ch_j "Ha! No way."
                                elif Girl == StormX:
                                        ch_s "I would rather not."
                                elif Girl == JubesX:
                                        ch_v "Um, no thanks. . ."
                                $ Girl.RecentActions.append("no bottomless")
                                $ Girl.DailyActions.append("no bottomless")
                                return
                        elif Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                            if Girl == RogueX:
                                    ch_r "A little backwards, but sure. . ."
                            elif Girl == KittyX:
                                    ch_k "[Girl.Like]I guess. . ."
                            elif Girl == EmmaX:
                                    ch_e "I suppose that I could. . ."
                            elif Girl == LauraX:
                                    ch_l "Huh, ok. . ."
                            elif Girl == JeanX:
                                    ch_j "Hmm. . . I guess. . ."
                            elif Girl == StormX:
                                    ch_s "I could do that. . ."
                            elif Girl == JubesX:
                                    ch_v "Well, I could do that. . ."
                        else:
                            if Girl == EmmaX:
                                    ch_e "Of course."
                            elif Girl == LauraX:
                                    ch_l "Huh, ok. . ."
                            elif Girl == StormX:
                                    ch_s "Fine."
                            else:
                                    call AnyLine(Girl,"Ok, sure, "+Girl.Petname+".")
                        $ Line = Girl.Panties
                        $ Girl.Panties = 0
                        if Girl == KittyX:
                            if Girl.PantsNum() >= 5:
                                "She reaches a hand into her [Girl.Legs] and pulls her [Line] out through the pocket."
                                "She gives a little wink as she drops them to the ground."
                            elif Girl.HoseNum() >= 5:
                                "She reaches a hand into her [Girl.Hose] and pulls her [Line] out through the pocket."
                                "She gives a little wink as she drops them to the ground."
                            else:
                                "With a little shimmy, her [Line] drop to the ground."
                        elif Girl.PantsNum() >= 6:
                                "She pulls her [Girl.Legs] off, then removes her [Line], before putting them back on."
                        elif Girl.HoseNum() >= 6:
                                "She pulls her [Girl.Hose] off, then removes her [Line], before putting them back on."
                        elif Girl == JubesX and JubesX.Acc == "shut jacket":
                                "She reaches under her jacket and pulls her [Line] down."
                        elif Girl.Legs:
                                "She reaches under her [Girl.Legs] and pulls her [Line] down."
                        else:
                                "She glances up at you as she removes her [Line]."
                        call first_bottomless(Girl)

                "Just give me a clear view. . ." if (Girl.Panties and not Girl.PantiesDown) or (Girl.Legs and not Girl.Upskirt):
                        if Approval >= 2:
                                if Girl == LauraX:
                                        ch_l "Whatever."
                                else:
                                        call AnyLine(Girl,"Fine.")
                                $ Girl.PantiesDown = 1 if Girl.Panties else 0
                                $ Girl.Upskirt = 1 if Girl.Legs else 0
                                if Girl.Legs:
                                        "She shifts her [Girl.Legs] out of the way."
                                else:
                                        "She shifts her [Girl.Panties] out of the way."
                        elif Approval >= 1 and Girl.Legs and Girl.Panties and not Girl.PantiesDown:
                                if Girl == RogueX:
                                        ch_r "I'll show you a little bit. . ."
                                elif Girl == KittyX:
                                        ch_k "I guess I could show you something. . ."
                                elif Girl == EmmaX:
                                        ch_e "I'll give at least give a little view. . ."
                                elif Girl == LauraX:
                                        ch_l "Make do with this. . ."
                                elif Girl == JeanX:
                                        ch_j "This should be plenty, [Girl.Petname]."
                                elif Girl == StormX:
                                        ch_s "I have taken off enough. . ."
                                elif Girl == JubesX:
                                        ch_v "I guess. . . how 'bout this. . ."
                                $ Girl.Upskirt = 1
                        else:
                                call AnyLine(Girl,"No.")
                                $ Girl.RecentActions.append("no bottomless")
                                $ Girl.DailyActions.append("no bottomless")
                                return
                        call first_bottomless(Girl)

                "Lose the [Girl.Hose]." if Girl.Hose:
                        $ Girl.FaceChange("bemused", 1)
                        if Girl.Legs:
                            call AnyLine(Girl,"All right, fine.")
                        elif Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                            call NoPantiesOn(Girl)
                        elif not Approval and Girl.HoseNum() >= 6:
                            if Girl == RogueX:
                                    ch_r "No thanks, [Girl.Petname]."
                            else:
                                    call AnyLine(Girl,"Sorry, no, "+Girl.Petname+".")
                            return
                        else:
                            if Girl == RogueX:
                                    ch_r "Ok, sure, [Girl.Petname]."
                            else:
                                    call AnyLine(Girl,"Fine, "+Girl.Petname+".")
                        $ Line = Girl.Hose
                        $ Girl.Hose = 0
                        if Girl == KittyX:
                            if Girl.PantsNum() >= 5:
                                "She reaches a hand into her [Girl.Legs] and pulls her [Line] right through her legs."
                                "She makes a little flourish and drops them to the ground."
                            else:
                                "She gives a little shake and her [Line] drop to the ground."
                        elif Girl.PantsNum() >= 6:
                                "She pulls off her [Girl.Legs] and pulls her [Line] off, then puts them back on."
                        elif Girl.Legs:
                                "She reaches under her [Girl.Legs] and pulls her [Line] down."
                        elif Girl.HoseNum() < 10:
                                "[Girl.Name] pulls her [Line] off."
                        elif not Girl.Panties:
                                $ Girl.FaceChange("sly", 2)
                                "She blushes and looks at you slyly before removing her [Line]."
                                $ Girl.Blush = 1
                                call first_bottomless(Girl)
                        elif not Girl.SeenPanties:
                                "[Girl.Name] shyly removes her [Line]."
                                $ Girl.SeenPanties = 1
                        else:
                                "[Girl.Name] pulls her [Line] off."

                "Rip the [Girl.Hose]." if Girl.Hose == "pantyhose" or Girl.Hose == "tights":
                        $ Girl.FaceChange("bemused", 1)
                        if Girl.Legs:
                            call AnyLine(Girl,"All right, fine.")
                        elif Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                            call NoPantiesOn(Girl)
                        elif not Approval and Girl.HoseNum() >= 6:
                            if Girl == RogueX:
                                    ch_r "I'd rather you didn't, [Girl.Petname]."
                            else:
                                    call AnyLine(Girl,"Sorry, no, "+Girl.Petname+".")
                            return

                        $ Line = Girl.Hose
                        if Girl.Hose == "tights":
                                $ Girl.Hose = "ripped tights"
                        elif Girl.Hose == "pantyhose":
                                $ Girl.Hose = "ripped pantyhose"
                        if Girl.Hose not in Girl.Inventory:
                                $ Girl.Inventory.append(Girl.Hose)
                        $ Girl.AddWord(1,"ripped","ripped")
                        "You tear holes in her [Line]."
                        if not ApprovalCheck(Girl, 1200, TabM=0):
                                $ Girl.FaceChange("angry", 1,Eyes="down")
                                if Girl == RogueX:
                                        ch_r "Dammit, [Girl.Petname], those are gettin expensive!"
                                elif Girl == KittyX:
                                        ch_k "Hey, I was using those!"
                                elif Girl == EmmaX:
                                        ch_e "I hope you're paying for those."
                                elif Girl == LauraX:
                                        ch_l "Hey. Not cool."
                                elif Girl == JeanX:
                                        ch_j "Oh, whatever."
                                elif Girl == StormX:
                                        ch_s "Those do not grow on trees. . ."
                                elif Girl == JubesX:
                                        ch_v "Hey! You'd better replace those. . ."
                                $ Girl.FaceChange("bemused", 1)

                "Why don't you lose the sweater?" if Girl.Acc == "sweater":
                            $ Girl.Acc = 0
                            "[Girl.Name] tosses her sweater off."

                "Keep it all on for now." if Cnt == 1:
                    $ Cnt = 0

                "Ok, that's enough for now." if Cnt == 2:
                    $ Cnt = 0

            $ Cnt = 2 if Cnt else Cnt
            $ Line = "Anything else?"
        return

label NoPantiesOn(Girl=0):  #rkeljsv
        #called when asked to remove pants with nothing on under
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if not Girl.Panties:
            return

        if Girl == RogueX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_r "Well, I'm not exactly decent under here, you know. . ."
                else:
                        ch_r "This is the last bit. . ."
        elif Girl == KittyX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_k "[Girl.Like]I'm not wearing any panties. . ."
                else:
                        ch_k "Not much else on. . ."
        elif Girl == EmmaX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_e "I don't have anything on under this. . ."
                else:
                        ch_e "This is all I have on. . ."
        elif Girl == LauraX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_l "I don't have anything on under this. . ."
                else:
                        ch_l "These are all I have on. . ."
        elif Girl == JeanX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_j "I don't have panties on right now. . ."
                else:
                        ch_j ". . ."
        elif Girl == StormX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_s "I am naked under this. . ."
                else:
                        ch_s "This is all I have on. . ."
        elif Girl == JubesX:
                if Girl.PantsNum() >= 5 or Girl.HoseNum() >= 10:
                        ch_v "I don't have anything on under this. . ."
                else:
                        ch_v "This is all I've got on. . ."
        menu:
            extend ""
            "Could you do it anyway?":
                if ApprovalCheck(Girl, 1000, "LI", TabM=1):
                        if Girl == RogueX:
                                ch_r "Well, if you're gonna ask so nicely. . . "
                        elif Girl == KittyX:
                                ch_k "I[Girl.like]guess so. . . "
                        elif Girl == EmmaX:
                                ch_e "I suppose. . . "
                        elif Girl == LauraX:
                                ch_l "I guess. . . "
                        elif Girl == JeanX:
                                ch_j "Oh, why not. . ."
                        elif Girl == StormX:
                                ch_s "I suppose I could. . ."
                        elif Girl == JubesX:
                                ch_v "Well, guess. . ."
                else:
                        if Girl == RogueX:
                                ch_r "Sorry, I don't think so."
                        elif Girl == KittyX:
                                ch_k "No thanks."
                        elif Girl == EmmaX:
                                ch_e "I'm afraid not."
                        elif Girl == LauraX:
                                ch_l "Nah, not right now."
                        elif Girl == JeanX:
                                ch_j "Ha! Keep trying, [Girl.Petname]."
                        elif Girl == StormX:
                                ch_s "I do not think so, right now."
                        elif Girl == JubesX:
                                ch_v "Nah. . ."
                        call Bottoms_Off_Refused(Girl)
                        $ renpy.pop_call()
            "Don't care, lose'em.":
                if ApprovalCheck(Girl, 800, "OI", TabM=1):
                        if Girl == RogueX:
                                ch_r "Fine, whatever."
                        elif Girl == KittyX:
                                ch_k "Whatev."
                        elif Girl == EmmaX:
                                ch_e "If you insist."
                        elif Girl == LauraX:
                                ch_l "Fine."
                        elif Girl == JeanX:
                                ch_j ". . ."
                        elif Girl == StormX:
                                ch_s ". . ."
                        elif Girl == JubesX:
                                ch_v "Fine. . ."
                else:
                        call Bottoms_Off_Refused(Girl)
                        $ renpy.pop_call()

            "Ok, you can leave it on.":
                $ renpy.pop_call()
        return

label Bottoms_Off_Refused(Girl=0):  #rkeljsv
        $ Girl = GirlCheck(Girl)
        call Shift_Focus(Girl)

        if Girl == RogueX:
                if "no bottomless" in Girl.RecentActions:
                        ch_r "What part of \"no\" escapes you, [Girl.Petname]?"
                elif "no bottomless" in Girl.DailyActions:
                        ch_r "If you keep this up, not ever, [Girl.Petname]."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_r "That's enough, [Girl.Petname]. Sure we can't have some fun anyway?"
                    else:
                        ch_r "I'm afraid not this time, [Girl.Petname]. Sure we can't have some fun anyway?"
        elif Girl == KittyX:
                if "no bottomless" in Girl.RecentActions:
                        ch_k "You're[Girl.like]on my last nerve here."
                elif "no bottomless" in Girl.DailyActions:
                        ch_k "Give it a rest."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_k "What you see is what you get, but[Girl.like]can't we still have some fun?"
                    else:
                        ch_k "The answer's \"no,\" but[Girl.like]can't we still have some fun?"
        elif Girl == EmmaX:
                if "no bottomless" in Girl.RecentActions:
                        ch_e "Try to control your impulses."
                elif "no bottomless" in Girl.DailyActions:
                        ch_e "Not today."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_e "That's all I'm willing to do, is that a deal-breaker?"
                    else:
                        ch_e "I'm afraid not, is that a deal-breaker?"
        elif Girl == LauraX:
                if "no bottomless" in Girl.RecentActions:
                        ch_l "Reign it in."
                elif "no bottomless" in Girl.DailyActions:
                        ch_l "No, not today."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_l "No more, is that going to be a problem?"
                    else:
                        ch_l "Nope, is that going to be a problem?"
        elif Girl == JeanX:
                if "no bottomless" in Girl.RecentActions:
                        ch_j "Take a breath, [Girl.Petname]."
                elif "no bottomless" in Girl.DailyActions:
                        ch_j "I made myself clear."
                else:
                    $ Girl.FaceChange("sad")
                    #if Cnt == 2:
                        #ch_j "Do we have a problem?"
                    #else:
                    ch_j "Do we have a problem?"
        elif Girl == StormX:
                if "no bottomless" in Girl.RecentActions:
                        ch_s "Show some restraint."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:
                        ch_s "This is all, can we continue without it?"
                    else:
                        ch_s "I would rather not, can we continue without it?"
        elif Girl == JubesX:
                if "no bottomless" in Girl.DailyActions:
                        ch_v "Like I said, nope."
                else:
                    $ Girl.FaceChange("sad")
                    ch_v "This is it, ok?"
        menu:
            extend ""
            "Sure, never mind." if "no bottomless" not in Girl.RecentActions:
                    $ Girl.Mouth = "smile"
                    $ Girl.Statup("Love", 70, 2)
                    $ Girl.Statup("Obed", 60, 2)
                    if Girl == RogueX:
                            ch_r "Great."
                    elif Girl == KittyX:
                            ch_k "Great!"
                    elif Girl == EmmaX:
                            ch_e "Excellent."
                    elif Girl == LauraX:
                            ch_l "Right."
                    elif Girl == JeanX:
                            ch_j "Good. . ."
                    elif Girl == StormX:
                            ch_s "Good. . ."
                    elif Girl == JubesX:
                            ch_v "Cool."

            "Sorry, I'll drop it." if "no bottomless" in Girl.RecentActions:
                    if Girl == EmmaX:
                            ch_e "Good."
                    elif Girl == LauraX:
                            ch_l "Cool."
                    else:
                            call AnyLine(Girl,"Fine. . .")

            "No, let's do something else.":
                    $ Girl.Brows = "confused"
                    if Girl == RogueX:
                            ch_r "Ok [Girl.Petname], your loss."
                    elif Girl == KittyX:
                            ch_k "Ok[Girl.like]whatever."
                    elif Girl == StormX:
                            ch_s "So be it. . ."
                    elif Girl == JubesX:
                            ch_v "Whatever. . ."
                    else:
                            call AnyLine(Girl,"Your loss.")
                    $ Girl.Statup("Lust", 50, 5)
                    $ Girl.Statup("Love", 70, -2, 1)
                    if "no bottomless" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 60, 4)
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")

        $ Girl.RecentActions.append("no bottomless")
        $ Girl.DailyActions.append("no bottomless")
        $ temp_modifier = 0
        return
