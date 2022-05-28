
label Girls_Caught(Girl=0, TotalCaught=0, Shame=0, Count=0, T_Pet=0, temp_Girls=[]):
    call shift_focus (Girl)
    call checkout
    Girl.voice "!!!"
    $ line = primary_action
    call Trig_Reset
    $ Girl.change_outfit()
    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current:
            $ temp_Girls[0].location = "bg_study"
        $ TotalCaught += temp_Girls[0].event_counter["caught"]
        $ temp_Girls.remove(temp_Girls[0])
    $ bg_current = "bg_study"
    call set_the_scene (0)
    show Xavier_sprite at sprite_location(stage_left)

    if Girl == RogueX:
        show Rogue_sprite at sprite_location(stage_right) with ease
    elif Girl == KittyX:
        show Kitty_sprite at sprite_location(stage_right) with ease
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
    call outfitShame (Girl, 20)

    $ Count = Girl.event_counter["caught"]

    if Partner == RogueX:
        show Rogue_sprite at sprite_location(stage_far_right) with ease
    elif Partner == KittyX:
        show Kitty_sprite at sprite_location(stage_far_right) with ease
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

    call change_Xavier_face ("_shocked")
    $ Girl.change_face("_sad")
    if (Girl == EmmaX or Partner == EmmaX) and (Girl == StormX or Partner == StormX):
        ch_x "I'm very disappointed in the both of you!."
        ch_x "You should temp_GirlsTH know better than this!"
    elif Girl == StormX or Partner == StormX:
        ch_x "I'm very disappointed in your behavior, particularly yours, Ororo."
    elif Girl == EmmaX or Partner == EmmaX:
        ch_x "I'm very disappointed in your behavior, particularly yours, Emma."
    else:
        ch_x "I'm very disappointed in your behavior, the both of you."

    if line == "fondle_thighs" or line == "fondle_breasts" or line == "fondle_pussy" or line == "hotdog" or line == "handjob":
        ch_x "The two of you, feeling each other up like animals!"
    elif line == "dildo_pussy" or line == "dildo_anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif line == "eat_pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif line == "blowjob":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"

    if Girl.outfit["shame"] >= 40:
        ch_x "[Girl.name], my dear, you're practically naked! At least throw a towel on!"
        "He throws [Girl.name] the towel."
        show black_screen onlayer black
        $ temp_Girls = all_Girls[:]
        while temp_Girls:
            if temp_Girls[0].location == bg_current and (not temp_Girls[0].outfit["top"] and not temp_Girls[0].outfit["bra"]):
                $ temp_Girls[0].outfit["top"] = "_towel"
            $ temp_Girls.remove(temp_Girls[0])
        hide black_screen onlayer black
        if (Girl == StormX or Partner == StormX) and StormX.outfit["top"] == "_towel":
            ch_x ". . ."
            ch_x "Ororo, for Christ's sake. . ."
            ch_x "Put on some actual clothes!"
            show black_screen onlayer black
            $ StormX.outfit["top"] = "_white_shirt"
            $ StormX.outfit["bottom"] = "_skirt"
            hide black_screen onlayer black
            ch_x ". . . fine."

    elif Girl.outfit["shame"] >= 20:
        ch_x "[Girl.name], my dear, that attire is positively scandalous."

    if Girl.event_counter["caught"]:

        "And this isn't even the first time this has happened!"

    if Partner:
        $ Partner.change_face("_surprised",2)
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
        $ Partner.change_face("_bemused",1, eyes="_side")

    if EmmaX.location == bg_current and EmmaX not in Rules:
        if not EmmaX.event_counter["caught"]:
            ch_x "Emma, you are entrusted as a teacher here, I can't have you fraternizing with the students."
            ch_x "This is especially true in the school's public spaces!"
            ch_x "What sort of message does that send?"
            ch_x "How appropriate would it be if I were to just wander the halls with Miss Grey on my lap?"
            call change_Xavier_face ("_hypno")
            ch_x "Just. . . running my hands along her firm little body without a care in the world. . ."
            call change_Xavier_face ("_happy")
            if JeanX.location == bg_current:
                "You glance over at [JeanX.name], she shrugs."
            ch_x ". . ."
            call change_Xavier_face ("_shocked")
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
            call change_Xavier_face ("_hypno")
            ch_x "Just. . . rolling down the halls with my balls flowing freely in the wind. . ."
            call change_Xavier_face ("_happy")
            ch_x ". . ."
            call change_Xavier_face ("_shocked")
            ch_x "Do not distract me! . ."
        else:
            if EmmaX.location == bg_current and EmmaX not in Rules:
                ch_x "And Ororo! We've also been over this before."
            else:
                ch_x "Ororo, I don't believe this is the first time we've had this talk."
            ch_x "I should hope it will be the last."

    $ line = 0
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

            call change_Xavier_face ("_happy")
            if Girl.event_counter["caught"]:
                ch_x "But you know you've done this before. . . at least [Girl.event_counter['caught']] times. . ."
            elif Girl == EmmaX and TotalCaught:
                ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ."
                $ Girl.change_face("_sexy",brows="_confused")
            elif Girl == StormX and TotalCaught:
                ch_x "Not with Ms. Munroe, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ."
                $ Girl.change_face("_sexy",brows="_confused")
            elif TotalCaught:
                ch_x "Not with this young lady, perhaps, but you know you've done this before. . ."
                ch_x "at least [TotalCaught] times. . ."
            else:
                ch_x "Very well, just don't let it happen again. "
            $ Count += 5
            if being_punished:
                ch_x "I'm extending your punishment by [Count] days."
            else:
                ch_x "I'm halving your daily stipend for [Count] days."
            ch_x "Now return to your rooms and reflect on what you've done."
        "Just having a little fun, right [Girl.petname]?":


            $ Girl.name_check()
            $ Girl.change_face("_bemused")
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

            call change_Xavier_face ("_angry")
            $ Count += 10
            ch_x "If that's your attitude, harsher methods might be necessary."
            if being_punished:
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


        "Just this. . . Plan Omega, [RogueX.name]." if Girl == RogueX and Player.level >= 5:
            $ line = "Omega"
        "Just this. . . Plan Kappa, [KittyX.name]!" if Girl == KittyX and Player.level >= 5:
            $ line = "Kappa"
        "Just this. . . Plan Psi, [EmmaX.name]!" if Girl == EmmaX and Player.level >= 5:
            $ line = "Psi"
        "Just this. . . Plan Chi, [LauraX.name]!" if Girl == LauraX and Player.level >= 5:
            $ line = "Chi"
        "Just this. . . Plan Alpha, [JeanX.name]!" if Girl == JeanX and Player.level >= 5:
            $ line = "Alpha"
        "Just this. . . Plan Rho, [StormX.name]!" if Girl == StormX and Player.level >= 5:
            $ line = "Rho"
        "Just this. . . Plan Zeta, [JubesX.name]!" if Girl == JubesX and Player.level >= 5:
            $ line = "Zeta"
        "You can suck it, old man.":



            $ Girl.change_face("_surprised")
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

            call change_Xavier_face ("_angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if being_punished:
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


    if line:
        if line == "Omega":
            if approval_check(RogueX, 1500, taboo_modifier=1, Loc="No"):
                call Xavier_Plan (RogueX)
                return
            elif approval_check(RogueX, 1000, taboo_modifier=1, Loc="No"):
                $ Girl.change_face("_perplexed",brows = "_sad")
                ch_r "I'm not comfortable with something that extreme, [RogueX.player_petname]. . ."
                menu:
                    "Dammit [RogueX.name]. . .":
                        $ Girl.change_face("_angry")
                        $ RogueX.change_stat("obedience", 50, 5)
                        $ RogueX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("_bemused")
            else:
                $ Girl.change_face("_confused")
                ch_r "What nonsense are you talking now?"
                ch_p "Plan {i}Omega!{/i} . . you know. . ."
                ch_r "Sounds like gibberish."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("_bemused")

        elif line == "Kappa":
            if "Xavier's photo" in Player.inventory and approval_check(KittyX, 1500, taboo_modifier=1, Loc="No"):
                call Xavier_Plan (KittyX)
                return
            elif approval_check(KittyX, 1000, taboo_modifier=1, Loc="No"):
                $ Girl.change_face("_perplexed",brows = "_sad")
                if "Xavier's photo" in Player.inventory:
                    ch_k "You know. . . I really don't think that's a good idea. . ."
                elif "kappa" in Player.history:
                    ch_k "Maybe if we came back later we could find something. . ."
                else:
                    ch_k "We don't really have any way to pull that off atm. . ."
                    $ Player.history.append("kappa")
                menu:
                    "Dammit [KittyX.name]. . .":
                        $ Girl.change_face("_angry")
                        $ KittyX.change_stat("obedience", 50, 5)
                        $ KittyX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("_bemused")
                        $ KittyX.change_stat("love", 90, 5)
            else:
                $ Girl.change_face("_confused")
                ch_k "Wait, Plan what??"
                ch_p "Plan {i}Kappa!{/i} . . you know. . ."
                ch_k "I have no {i}idea{/i} what you're talking about."
                ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("_bemused")

        elif line == "Psi":
            if approval_check(EmmaX, 1500, taboo_modifier=1, Loc="No"):
                call Xavier_Plan (EmmaX)
                return
            elif approval_check(EmmaX, 1000, taboo_modifier=1, Loc="No"):
                $ Girl.change_face("_perplexed",brows = "_sad")
                ch_e "Um, I don't believe we're quite at that point yet, [EmmaX.player_petname]. . ."
                menu:
                    "Dammit [EmmaX.name]. . .":
                        $ Girl.change_face("_angry")
                        $ EmmaX.change_stat("obedience", 50, 5)
                        $ EmmaX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("_bemused")
            else:
                $ Girl.change_face("_confused")
                ch_e "Lord child, what are you talking about now?"
                ch_p "Plan {i}Psi!{/i} . . you know. . ."
                ch_e "I wish that I did."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("_bemused")

        elif line == "Chi":
            if LauraX.level >= 2 and approval_check(LauraX, 1500, taboo_modifier=1, Loc="No") and approval_check(LauraX, 750, "I"):
                call Xavier_Plan (LauraX)
                return
            elif approval_check(LauraX, 1000, taboo_modifier=1, Loc="No"):
                $ Girl.change_face("_angry",eyes="_side",brows = "_angry")
                ch_l "I told you that was a stupid idea. . ."
                menu:
                    "Dammit [LauraX.name]. . .":
                        $ Girl.change_face("_angry")
                        $ LauraX.change_stat("obedience", 50, 5)
                        $ LauraX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("_bemused")
                        $ LauraX.change_stat("love", 90, 5)
            else:
                $ Girl.change_face("_confused")
                ch_l "Yeah!"
                ch_l ". . ."
                ch_l "Wait, plan \"key,\" what??"
                ch_p "Plan {i}Chi!{/i} . . you know. . ."
                ch_l "Um. No?"
                ch_p "oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("_bemused")

        elif line == "Alpha":
            if approval_check(JeanX, 1500, taboo_modifier=1, Loc="No"):
                call Xavier_Plan (JeanX)
                return
            elif approval_check(JeanX, 1000, taboo_modifier=1, Loc="No"):
                $ Girl.change_face("_perplexed",brows = "_sad")
                ch_j "Look, this is your mess, I'm not going to clean it up, [JeanX.player_petname]. . ."
                menu:
                    "Dammit [JeanX.name]. . .":
                        $ Girl.change_face("_angry")
                        $ JeanX.change_stat("obedience", 50, 5)
                        $ JeanX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("_bemused")
            else:
                $ Girl.change_face("_confused")
                ch_j "Huh? What are you talking about?"
                ch_p "Plan {i}Alpha!{/i} . . you know. . ."
                ch_j "Drawing a blank here. . ."
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("_bemused")

        elif line == "Rho":
            if "Xavier's files" in Player.inventory and approval_check(StormX, 1500, taboo_modifier=1, Loc="No"):
                call Xavier_Plan (StormX)
                return
            elif approval_check(StormX, 1000, taboo_modifier=1, Loc="No"):
                $ Girl.change_face("_perplexed",brows = "_sad")
                if "Xavier's files" in Player.inventory:
                    ch_s "I really doubt that we should attempt that. . ."
                elif "rho" in Player.history:
                    ch_s "Perhaps if we had some leverage on the situation. . ."
                else:
                    ch_s "I'm not sure what you think we could do here. . ."
                    $ Player.history.append("rho")
                menu:
                    "Dammit [StormX.name]. . .":
                        $ Girl.change_face("_angry")
                        $ StormX.change_stat("obedience", 50, 5)
                        $ StormX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("_bemused")
            else:
                $ Girl.change_face("_confused")
                ch_s "'Ro? You were speaking to me?"
                ch_p "Yes! Plan {i}Rho!{/i} . . you know. . ."
                ch_s "Yes, this is 'Ro. What plan?"
                ch_p "What's on second! I don't know!"
                $ Girl.change_face("_smile")
                ch_s "Ah! \"Third base!\""
                $ Girl.change_face("_bemused")

        elif line == "Zeta":
            if approval_check(JubesX, 1500, taboo_modifier=1, Loc="No"):
                call Xavier_Plan (JubesX)
                return
            elif approval_check(JubesX, 1000, taboo_modifier=1, Loc="No"):
                $ Girl.change_face("_perplexed",brows = "_sad")
                ch_v "What?! Um, no, let's not."
                menu:
                    "Dammit [JubesX.name]. . .":
                        $ Girl.change_face("_angry")
                        $ JubesX.change_stat("obedience", 50, 5)
                        $ JubesX.change_stat("love", 90, -5)
                    "Yeah, I guess you're right. . .":
                        $ Girl.change_face("_bemused")
            else:
                $ Girl.change_face("_confused")
                ch_v "Huh?"
                ch_p "Plan {i}Zeta!{/i} . . you know. . ."
                ch_v "Is this a \"Gundam\" thing?"
                ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                $ Girl.change_face("_bemused")



        call change_Xavier_face ("_angry")
        $ Count += 10
        ch_x "I have no idea what that was about, but it sounds like you haven't learned."
        if being_punished:
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


    $ being_punished += Count

    $ Girl.event_counter["caught"] += 1
    if Partner in all_Girls:
        $ Partner.event_counter["caught"] += 1
    $ Girl.add_word(0,"caught","caught")

    if Girl == KittyX and KittyX not in Rules and "Xavier's photo" not in Player.inventory:
        "It would probably be a good idea to find some way to get Xavier to leave you alone."
        if KittyX.event_counter["caught"] > 1:
            "Maybe I should try searching the office when he's not around."
        if KittyX.event_counter["caught"] > 2:
            "I bet [KittyX.name] could help me get in."
        if KittyX.event_counter["caught"] > 3:
            "I bet there's something in that lefthand drawer. . ."
    elif Girl == JeanX and "nowhammy" not in JeanX.traits and JeanX.event_counter["caught"] > 1:
        ch_x "Oh, and Jean, dear, I'd like a word?"
        $ Girl.change_face("_bemused")
        ch_j "What is it?"
        ch_x "I understand that you've been using your abilities to. . ."
        ch_x "cover up for some of your. . . transgressions."
        $ Girl.change_face("_bemused",eyes="up")
        ch_j "Oh, you mean how I mindwipe the \"NPCs\" that get too nosy?"
        call change_Xavier_face ("_angry")
        ch_x "If by \"NPCs\" you mean your fellow students. . ."
        ch_x ". . . and by \"get too nosy,\" you mean \"notice you having sex in public\". . ."
        ch_x ". . . then yes, that is exactly what I mean."
        $ Girl.change_face("_bemused",eyes="_side")
        ch_j "Ok, yeah."
        ch_x "I would like you to cease this activity at once!"
        ch_x "It is a total abuse of your abilities and of those students' autonomy!"
        $ Girl.change_face("_angry",1)
        ch_j "Who cares."
        call change_Xavier_face ("_shocked")
        ch_x "!!!"
        ch_x "I do!"
        call change_Xavier_face ("_angry")
        ch_x "That is it, young lady. Until further notice, you're forbidden from. . . whammying your fellow students!"
        $ Girl.change_face("_angry",1,mouth="_surprised")
        ch_j "Bullshit!"
        $ Girl.change_face("_angry",0,eyes="_psychic")
        ch_x "Ugh. . ."
        call change_Xavier_face ("_psychic")
        ch_x "[Player.name]. . . this may take a while. . ."
        ch_x "You may as well leave. . ."
        $ JeanX.traits.append("nowhammy")
        $ Girl.change_face("_normal")

    if EmmaX.location == bg_current and EmmaX not in Rules:
        ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
        if EmmaX.event_counter["caught"]:
            $ EmmaX.change_stat("love", 90, -5)
            $ Girl.change_face("_angry",eyes="_closed")
            ch_e "Not again. . ."
    if StormX.location == bg_current and StormX not in Rules:
        if EmmaX.location == bg_current and EmmaX not in Rules:
            ch_x "And Ororo, I'm afraid we will have to have words as well. . ."
        else:
            ch_x "Ororo, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
        if StormX.event_counter["caught"]:
            $ StormX.change_stat("love", 90, -5)
            $ Girl.change_face("_angry",eyes="_closed")
            ch_s "Again? . ."
        if StormX not in Rules and "Xavier's files" not in Player.inventory:
            "It would probably be a good idea to find some way to get Xavier to leave you alone."
            if StormX.event_counter["caught"] > 1:
                "Maybe I should try searching the office when he's not around."
            if StormX.event_counter["caught"] > 2:
                "I bet [StormX.name] could help me get in."
            if StormX.event_counter["caught"] > 3:
                "I bet there's something in that righthand drawer. . ."

    call remove_girl ("all")
    "You return to your room"
    hide Xavier_sprite
    jump player_room



label Xavier_Plan(GirlX=0):
    if "Xavier" in Player.daily_history:
        "The Professor seems pretty out of it."
        "You don't think you'll be able to get anything more out of him today."
        "You leave him to it."
        jump player_room


    call shift_focus (GirlX)
    $ GirlX.change_face("_sly")
    "As you say this, a sly grin crosses [GirlX.name]'s face."
    "You quickly approach Xavier and place your hands on his head."
    call change_Xavier_face ("_psychic")
    ch_x ". . ."
    call change_Xavier_face ("_shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."

    if Partner:
        if Partner == RogueX and "Omega" not in Player.traits:
            $ line = "first"
        elif Partner == KittyX and "Kappa" not in Player.traits:
            $ line = "first"
        elif Partner == EmmaX and "Psi" not in Player.traits:
            $ line = "first"
        elif Partner == LauraX and "Chi" not in Player.traits:
            $ line = "first"
        elif Partner == JeanX and "Alpha" not in Player.traits:
            $ line = "first"
        elif Partner == StormX and "Rho" not in Player.traits:
            $ line = "first"
        elif Partner == JubesX and "Zeta" not in Player.traits:
            $ line = "first"

        if line == "first":

            if approval_check(Partner, 1000) or Partner == JeanX:

                $ Partner.change_face("_surprised")
                "[Partner.name] looks a bit caught off guard, but goes along with the idea."
                $ Partner.change_face("_sly")
            else:
                $ Partner.change_face("_surprised")
                "[Partner.name] looks a bit uncomfortable with what's happening and takes off."
                call remove_girl (Partner)
        else:

            $ Partner.change_face("_sly")
            "[Partner.name] understands what's going on here."


    call change_Xavier_face ("_angry")
    if GirlX == RogueX:
        $ RogueX.outfit["gloves"] = ""
        $ RogueX.arm_pose = 2
        show Rogue_sprite zorder 24 at sprite_location(stage_left+100,85) with ease
        "[RogueX.name] moves in and also grabs his head, duplicating his powers as he watches helplessly."
        "Now that she posesses his full power, while his are negated, he has no defenses."
        call change_Xavier_face ("_hypno")
        if "Omega" in Player.traits:
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
        $ KittyX.arm_pose = 2
        show Kitty_sprite at sprite_location(stage_left+100,150) with ease
        $ KittyX.sprite_location = stage_center
        "[KittyX.name] moves in sits on his lap, pinning his arms to the chair."
        if "Kappa" in Player.traits:
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
        call change_Xavier_face ("_angry")
        if (GirlX == EmmaX and "Psi" in Player.traits) or (GirlX == JeanX and "Alpha" in Player.traits):
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
        $ LauraX.arm_pose = 2
        if "Chi" in Player.traits:
            ch_x "Oh, not again."
            $ LauraX.claws = 1
            ch_x "What is it you want this time?"
            $ LauraX.change_stat("obedience", 80, 3)
            $ LauraX.change_stat("inhibition", 80, 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            ch_p "[LauraX.name] and I were talking, and it seems like neither of us appreciates you bothering us."
            ch_x "And if I continue?"
            ch_p "My little [LauraX.petname] here has a very particular set of skills, you know. . ."
            $ GirlX.name_check()
            $ LauraX.claws = 1
            $ GirlX.change_face("_sly")
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
        $ StormX.arm_pose = 1
        show Storm_Sprite at sprite_location(stage_left+100,150) with ease
        $ StormX.sprite_location = stage_center
        "[StormX.name] moves in sits on his lap, pinning his arms to the chair."
        if "Rho" in Player.traits:
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
        $ JubesX.arm_pose = 2
        show Jubes_Sprite at sprite_location(stage_left+100,150) with ease
        $ JubesX.sprite_location = stage_center
        "[JubesX.name] moves in and sits on his lap, pinning his arms to the chair."
        "She turns to look at him."
        if "Zeta" in Player.traits:
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
    $ being_punished = 0
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

            "You know, [JeanX.name] should be able to \"whammy\" people again." if JeanX in all_Girls and "nowhammy" in JeanX.traits:
                ch_x "I could remove her mind-wiping ban. . ."
                $ JeanX.traits.remove("nowhammy")
                $ JeanX.traits.append("whammy")
                if JeanX.location == bg_current:
                    $ JeanX.change_stat("obedience", 50, 5)
                    $ JeanX.change_stat("love", 50, 5)
                    $ JeanX.change_stat("love", 70, 5)
                    $ JeanX.change_stat("love", 90, 5)
                    $ GirlX.change_face("_sly",1)
                    ch_j "Nice. . ."
            "You know, I did like it when [JeanX.name] couldn't use her \"whammy.\"" if JeanX in all_Girls and "whammy" in JeanX.traits:
                ch_x "I could reinstate her mind-wiping ban. . ."
                $ JeanX.traits.append("nowhammy")
                $ JeanX.traits.remove("whammy")
                if JeanX.location == bg_current:
                    $ JeanX.change_stat("obedience", 50, 5)
                    $ JeanX.change_stat("obedience", 80, 5)
                    $ JeanX.change_stat("love", 70, -5)
                    $ JeanX.change_stat("love", 90, -5)
                    $ GirlX.change_face("_angry",1,mouth="_surprised")
                    ch_j "Hey!"
                    $ GirlX.change_face("_angry",1)

            "Raise my stipend." if Player.income < 30:
                if GirlX == RogueX and "Omega" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.income += 2
                elif GirlX == KittyX and "Kappa" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.income += 2
                elif GirlX == EmmaX and "Psi" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.income += 2
                elif GirlX == LauraX and "Chi" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.income += 2
                elif GirlX == JeanX and "Alpha" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.income += 2
                elif GirlX == StormX and "Rho" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.income += 2
                elif GirlX == JubesX and "Zeta" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."
                    $ Player.income += 2
                else:
                    ch_x "I'm afraid I can't manage any more than I have. . ."
                    $ Count += 1
            "Raise my stipend. [[Used](locked)" if Player.income >= 30:
                pass
            "There's this girl that's been bothering me. . .":

                "This will send a girl away, temporarily removing her from the game."
                "You can always ask to bring her back later."
                $ line = 0
                menu:
                    ch_p "Could you get rid of. . ."
                    "[RogueX.name]" if RogueX in active_Girls:
                        $ line = RogueX
                    "[KittyX.name]" if KittyX in active_Girls and "met" in KittyX.history:
                        $ line = KittyX
                    "[EmmaX.name]" if EmmaX in active_Girls and "met" in EmmaX.history:
                        $ line = EmmaX
                    "[LauraX.name]" if LauraX in active_Girls and "met" in LauraX.history and "dress0" not in LauraX.history:
                        $ line = LauraX
                    "[JeanX.name]" if JeanX in active_Girls and "met" in JeanX.history:
                        $ line = JeanX
                    "[StormX.name]" if StormX in active_Girls and "met" in StormX.history:
                        $ line = StormX
                    "[JubesX.name]" if JubesX in active_Girls and "met" in JubesX.history:
                        $ line = JubesX
                    "Never mind. . .":
                        $ Count += 1
                if line:

                    ch_x "Very well, I suppose I can keep her occupied with various tasks around the campus. . ."
                    ch_x "She should be out of your hair for the time being."
                    if line.location == bg_current:

                        $ line.change_stat("love", 90, -10)
                        $ line.change_stat("obedience", 50, 3)
                        if line == RogueX:
                            ch_r "What do you mean, I'm \"bothering\" you?"
                        elif line == KittyX:
                            ch_k "Hey, what gives?!"
                        elif line == EmmaX:
                            ch_e "Excuse me? I must not have heard that right."
                        elif line == LauraX:
                            ch_l "Explain."
                        elif line == JeanX:
                            ch_j "Are you kidding me?!"
                        elif line == StormX:
                            ch_s "I do not understand this."
                        elif line == JubesX:
                            ch_v "Seriously?!"
                        menu:
                            extend ""
                            "Oh, sorry, never mind.":
                                $ line = 0
                                if approval_check(line, 2000):

                                    $ line.change_face("_confused")
                                    $ line.change_stat("love", 90, 3)
                                    $ line.change_stat("obedience", 50, 2)
                                    if line == RogueX:
                                        ch_r "Right. . ."
                                    elif line == KittyX:
                                        ch_k "Uh-huh?"
                                    elif line == EmmaX:
                                        ch_e ". . . right. . ."
                                    elif line == LauraX:
                                        ch_l "If you say so."
                                    elif line == JeanX:
                                        ch_j "We will have words. . ."
                                    elif line == StormX:
                                        ch_s "I will remember this. . ."
                                    elif line == JubesX:
                                        ch_v "Riiight."
                                else:

                                    $ line.change_face("_angry")
                                    $ line.change_stat("obedience", 50, -2)
                                    $ line.change_stat("inhibition", 60, 3)
                                    if line == RogueX:
                                        ch_r "Damned right you are."
                                    elif line == KittyX:
                                        ch_k "Yeah, right."
                                    elif line == EmmaX:
                                        ch_e "I don't know what you were thinking."
                                    elif line == LauraX:
                                        ch_l "Uh. . . huh."
                                    elif line == JeanX:
                                        ch_j "We will have words. . ."
                                    elif line == StormX:
                                        ch_s "I will remember this. . ."
                                    elif line == JubesX:
                                        ch_v "We will have words."
                            "Sorry, but I just need some \"me\" time.":
                                $ active_Girls.remove(line)
                                $ line.change_stat("obedience", 50, 5)
                                $ line.change_stat("obedience", 90, 2)
                                $ line.change_stat("inhibition", 60, 2)
                                if approval_check(line, 900, "L") or approval_check(line, 2000):

                                    $ line.change_face("_sadside")
                                    if line == RogueX:
                                        ch_r "I suppose if you do, I can give you some space."
                                    elif line == KittyX:
                                        ch_k "I guess we both could. . ."
                                    elif line == EmmaX:
                                        ch_e "I wouldn't want to be a bother. . ."
                                    elif line == LauraX:
                                        ch_l "I can make myself scarce. . ."
                                    elif line == JeanX:
                                        ch_j "Well, I guess I could find someone else to occupy my time with. . ."
                                    elif line == StormX:
                                        ch_s ". . . fine, I can understand that. . ."
                                    elif line == JubesX:
                                        ch_v "Ok, whatever, I have things to do."
                                else:

                                    $ line.change_stat("love", 90, -5)
                                    $ line.change_face("_angry")
                                    $ line.add_word(1,"_angry","_angry")
                                    if line == RogueX:
                                        ch_r "Oh, I think you'll be getting it."
                                    elif line == KittyX:
                                        ch_k "Yeah, \"me\" too, I guess!"
                                    elif line == EmmaX:
                                        ch_e "I do have other things with which to occupy myself."
                                    elif line == LauraX:
                                        ch_l "I'm busy too."
                                    elif line == StormX:
                                        ch_s "Oh, you shall get it. . ."
                                    elif line == JubesX:
                                        ch_v "We will have words."
                            "You heard me.":
                                $ active_Girls.remove(line)
                                $ line.change_stat("love", 80, -5)
                                $ line.change_stat("love", 90, -5)
                                $ line.change_stat("obedience", 80, 5)
                                if approval_check(line, 850, "O") or approval_check(line, 1500, "LO"):

                                    $ line.change_face("_sadside")
                                    $ line.change_stat("obedience", 200, 10)
                                else:

                                    $ line.change_face("_angry")
                                    $ line.change_stat("love", 90, -5)
                                    $ line.change_stat("inhibition", 60, 5)
                                    $ line.add_word(1,"_angry","_angry")
                                if line == RogueX:
                                    ch_r "Loud and clear."
                                elif line == KittyX:
                                    ch_k ". . ."
                                elif line == EmmaX:
                                    ch_e "I suppose I did."
                                elif line == LauraX:
                                    ch_l "If you say so."
                                elif line == JeanX:
                                    ch_j "Noted. . ."
                                elif line == StormX:
                                    ch_s "Like thunder. . ."
                                elif line == JubesX:
                                    ch_v "We will have words."
                    else:


                        $ active_Girls.remove(line)
                if line == GirlX:
                    GirlX.voice "Did you forget that I'm your escape plan?"
                    menu:
                        "Oh. . .":
                            ch_x "I'll forget you asked."
                            $ Count = 0
                $ line = 0


            "I wanted to bring a girl back in. . ." if len(all_Girls) > len (active_Girls):
                "This will bring the girl back into active play."
                "You can always ask to send her away again later."
                $ line = 0
                menu:
                    ch_p "Could you bring back. . ."
                    "[RogueX.name]" if RogueX not in active_Girls and RogueX in TotalGirl:
                        $ line = RogueX
                    "[KittyX.name]" if KittyX not in active_Girls and KittyX in all_Girls and "met" in KittyX.history:
                        $ line = KittyX
                    "[EmmaX.name]" if EmmaX not in active_Girls and EmmaX in all_Girls and "met" in EmmaX.history:
                        $ line = EmmaX
                    "[LauraX.name]" if LauraX not in active_Girls and LauraX in all_Girls and "met" in LauraX.history and "dress0" not in LauraX.history:

                        $ line = LauraX
                    "[JeanX.name]" if JeanX not in active_Girls and JeanX in all_Girls and "met" in JeanX.history:
                        $ line = JeanX
                    "[StormX.name]" if StormX not in active_Girls and StormX in all_Girls and "met" in StormX.history:
                        $ line = StormX
                    "[JubesX.name]" if JubesX not in active_Girls and JubesX in all_Girls and "met" in JubesX.history:
                        $ line = JubesX
                    "Never mind. . .":
                        $ Count += 1
                if line:

                    ch_x "Certainly. I've kept her busy, but I can let her off the hook. . ."
                    ch_x "She should have more free time now. . ."
                    $ active_Girls.append(line)
                $ line = 0
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in keys:
                        ch_x "Fine, take it. . ."
                        $ keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in keys:
                        pass

                    "Give me the key to [GirlX.name]'s room." if GirlX not in keys:
                        ch_x "I. . . suppose I could do that. . ."
                        $ keys.append(GirlX)
                    "Give me the key to [GirlX.name]'s room.[[Owned] (locked)" if GirlX in keys:
                        pass
                    "Never mind the keys.":

                        $ Count += 1
            "That should do it.":
                $ Count = 0

    ch_x "Very well, that should conclude our business. Please leave."
    if GirlX == RogueX:
        if "Omega" not in Player.traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("love", 70, 30)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.traits.append("Omega")
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
        $ GirlX.outfit["gloves"] = "_gloves"
        $ GirlX.arm_pose = 1
    elif GirlX == KittyX:
        if "Kappa" not in Player.traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.traits.append("Kappa")
        $ GirlX.arm_pose = 0
    elif GirlX == EmmaX:
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
        if "Psi" not in Player.traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.traits.append("Psi")
    elif GirlX == LauraX:
        if "Chi" not in Player.traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.traits.append("Chi")
        $ GirlX.arm_pose = 1
        $ GirlX.claws = 0
    elif GirlX == JeanX:
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."
        if "Alpha" not in Player.traits:
            $ GirlX.change_stat("lust", 70, 20)
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("obedience", 70, 10)
            $ GirlX.change_stat("obedience", 200, 20)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.traits.append("Alpha")
    elif GirlX == StormX:
        if "Rho" not in Player.traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.traits.append("Rho")
    elif GirlX == JubesX:
        if "Zeta" not in Player.traits:
            $ GirlX.change_stat("lust", 90, 10)
            $ GirlX.change_stat("inhibition", 80, 10)
            $ GirlX.change_stat("love", 70, 10)
            $ GirlX.change_stat("love", 200, 20)
            $ Player.traits.append("Zeta")
        $ GirlX.arm_pose = 0

    $ Player.daily_history.append("Xavier")
    call remove_girl ("all")
    hide Xavier_sprite
    call set_the_scene
    "You return to your room"
    jump player_room







label Girl_Caught_Changing(Girl=0):
    if Girl not in all_Girls:
        return
    call shift_focus (Girl)
    $ D20 = renpy.random.randint(1, 20)

    $ Girl.change_face("_surprised", 1,mouth = "_kiss")
    call remove_girl ("all")

    if D20 > 17:

        $ Girl.change_outfit("nude")
    else:

        $ Girl.change_outfit(6)
        if D20 >15:

            $ Girl.outfit["bottom"] = ""
            $ Girl.outfit["hose"] = ""
            $ Girl.outfit["underwear"] = ""
        elif D20 >14:

            $ Girl.outfit["bra"] = ""
            $ Girl.outfit["top"] = ""
        elif D20 >10:

            $ Girl.outfit["top"] = ""
            $ Girl.outfit["bottom"] = ""
        elif D20 >5:

            $ Girl.outfit["top"] = ""

    $ Girl.location = bg_current
    call set_the_scene(check_if_dressed = False)
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
    elif approval_check(Girl, 1400):
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
            if not approval_check(Girl, (D20 *70)) and (not Girl.seen_pussy or not Girl.seen_breasts):

                $ Girl.change_face("_surprised",brows="_angry")
                $ Girl.change_stat("love", 80, -50)

                if not Girl.top_number() or (Girl.top_number()+Girl.bra_number() <5) or (Girl.bottom_number() < 5 and Girl.hose_number() < 10):


                    call expression Girl.tag + "_First_Bottomless" pass (1)
                    call expression Girl.tag + "_First_Topless" pass (1)
                    $ Girl.outfit["top"] = "_towel"
                    "She grabs a towel and covers up."
            else:

                $ Girl.change_face("_surprised", 1,brows = "_confused")
                if "exhibitionist" in Girl.traits:
                    $ Girl.change_stat("lust", 200, (2*D20))
                else:
                    $ Girl.change_stat("lust", 200, D20)
                if D20 > 17:
                    call expression Girl.tag + "_First_Bottomless"
                    call expression Girl.tag + "_First_Topless" pass (1)
                elif D20 > 15:
                    call expression Girl.tag + "_First_Bottomless"
                elif D20 > 14:
                    call expression Girl.tag + "_First_Topless"
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


            if not approval_check(Girl, 800) and (not Girl.seen_pussy or not Girl.seen_breasts):
                $ Girl.change_face("_angry",brows="_confused")
                $ Girl.change_stat("love", 80, -5)
            else:
                $ Girl.change_face("_sexy",brows="_confused")
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
        $ Girl.change_face("_sexy")
        if approval_check(Girl, 1000):

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

            $ Girl.top_pulled_up = 1
            $ Girl.upskirt = 1
            pause 1
            call expression Girl.tag + "_First_Topless" pass (1)
            call expression Girl.tag + "_First_Bottomless" pass (1)
            $ Girl.top_pulled_up = 0
            $ Girl.upskirt = 0
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

            $ Girl.change_outfit(6,outfit_changed=0)
            $ renpy.pop_call()
            call world_map

    if Girl == StormX and D20 >5:

        ch_s "Ok, then let me finish getting dressed. . ."
        menu:
            "Ok.":
                "She finishes getting changed."
                $ Girl.change_outfit(6,outfit_changed=0)
            "Actually, you could leave them off.":
                if approval_check(Girl, 350+(10*D20)):
                    $ Girl.change_stat("love", 70, 3)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_face("_sexy")
                    ch_s "I suppose that could not hurt. . ."
                    $ Girl.set_temp_outfit()
                else:
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_face("_smile")
                    ch_s "Ha! I would not want to be too much of a distraction."
                    $ Girl.change_outfit(6,outfit_changed=0)
            "Why not lose the rest too?":
                $ Girl.change_face("_sexy")
                if approval_check(Girl, 700):
                    $ Girl.change_stat("love", 50, 1)
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_s "Oh, you are a naughty one. . ."
                    $ Girl.change_outfit("nude")
                    $ Girl.set_temp_outfit()
                elif approval_check(Girl, 350+(10*D20)):
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 70, 2)
                    ch_s "I could at least. . . pause for a moment?"
                    $ Girl.set_temp_outfit()
                else:
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 70, 1)
                    ch_s "You are joking, [Girl.player_petname]."
                    $ Girl.change_outfit(6,outfit_changed=0)
            "Don't, stay like that.":
                $ Girl.change_stat("obedience", 80, 2)
                if approval_check(Girl,1100):
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
                    $ Girl.change_face("_sexy")
                    ch_s "If you want. . ."
                    $ Girl.set_temp_outfit()
                elif approval_check(Girl, 350+(10*D20)) and approval_check(Girl, 400, "O"):
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("love", 80, -1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_face("_sexy",eyes="_side")
                    ch_s ". . . Very well."
                    $ Girl.set_temp_outfit()
                else:
                    $ Girl.change_stat("love", 80, -2)
                    $ Girl.change_stat("obedience", 50, -1)
                    $ Girl.change_face("_angry")
                    ch_s "You do not decide that, [Girl.player_petname]."
                    $ Girl.change_outfit(6,outfit_changed=0)
            "Lose the rest of it.":
                $ Girl.change_stat("obedience", 80, 2)
                if approval_check(Girl,1300):
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
                    $ Girl.change_face("_sexy")
                    ch_s "Fine. . ."
                    $ Girl.change_outfit("nude")
                    $ Girl.set_temp_outfit()
                elif approval_check(Girl,800) and approval_check(Girl, 500, "O"):
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("love", 80, -2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_face("_sexy",eyes="_side")
                    ch_s ". . . Fine."
                    $ Girl.change_outfit("nude")
                    $ Girl.set_temp_outfit()
                else:
                    $ Girl.change_stat("love", 50, -2)
                    $ Girl.change_stat("love", 80, -2)
                    $ Girl.change_stat("obedience", 50, -2)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_face("_angry")
                    ch_s "I do not think that I will, [Girl.player_petname]."
                    $ Girl.change_outfit(6,outfit_changed=0)
    return



label caught_masturbating(Girl=0):

    if Girl not in all_Girls:
        return
    $ Girl.drain_word("will_masturbate")
    call remove_girl ("all")
    $ Girl.location = bg_current
    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
    menu:
        extend ""
        "Knock politely":
            $ line = "knock"
        "Peek inside":
            call set_the_scene
            $ Girl.change_face("_kiss",1,eyes = "_closed")
            $ primary_action = "masturbation"
            $ girl_offhand_action = "fondle_pussy"
            "You see [Girl.name], eyes closed and stroking herself vigorously."
            menu:
                extend ""
                "Enter Quietly":
                    $ line = "enter"
                "Pull back and knock":
                    $ line = "knock"
                "Leave quietly":
                    $ line = "leave"
        "Enter quietly":
            $ line = "enter"
            "You hear some odd noises coming from [Girl.name]'s room as you enter."
        "Leave quietly":
            $ line = "leave"

    if line == "leave":
        $ Girl.change_stat("lust", 80, 20)
        "You leave [Girl.name] to her business and slip out."
        $ renpy.pop_call()
        jump campus_Map
    elif line == "knock":
        "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
        "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."
        $ Girl.change_face("_confused",1,eyes = "_surprised",mouth = "_smile")
        $ primary_action = None
        $ girl_offhand_action = None
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
    elif line == "enter":
        call shift_focus (Girl)
        show black_screen onlayer black
        $ Girl.upskirt = 1
        $ Girl.underwear_pulled_down = 1
        $ Girl.location = bg_current

        call set_the_scene
        $ Girl.change_face("_sexy")
        $ Girl.eyes = "_closed"
        $ Girl.arm_pose = 2
        $ Count = 0
        $ primary_action = "masturbation"
        hide black_screen onlayer black
        $ Girl.daily_history.append("unseen")
        $ Girl.recent_history.append("unseen")
        call expression Girl.tag + "_SexAct" pass ("masturbation")
        if "_angry" in Girl.recent_history:
            return


        $ Girl.change_face("_sexy",brows="_confused")
        if Girl.action_counter["masturbation"] == 1:
            if Girl == RogueX:
                ch_r "Well that was a bit unexpected. . ."
                $ Girl.change_face("_bemused",eyes="_side")
                ch_r "but not exactly unpleasant. . ."
                $ Girl.change_face("_sexy")
                ch_r "Maybe next time I'll give you a heads up first."
            elif Girl == KittyX:
                ch_k "So[KittyX.like]I wasn't expecting company. . ."
                $ Girl.change_face("_bemused",eyes="_side")
                ch_k "but I didn't exactly mind it either. . ."
                $ Girl.change_face("_sexy")
                ch_k "Maybe knock next time?"
            elif Girl == EmmaX:
                ch_e "I wasn't expecting visitors. . ."
                $ Girl.change_face("_bemused",eyes="_side")
                ch_e "although for you I could make an exception. . ."
                $ Girl.change_face("_sexy")
                ch_e "Perhaps next time you could knock?"
            elif Girl == LauraX:
                ch_l "So what are you doing here? . ."
                $ Girl.change_face("_bemused",eyes="_side")
                ch_l "not that I mind the company. . ."
                $ Girl.change_face("_sexy")
                ch_l "But you know, give me a heads up first."
            elif Girl == JeanX:
                $ Girl.change_face("_bemused",eyes="_side")
                ch_j "Well that was fun. . ."
                $ Girl.change_face("_sexy")
                ch_j "So what brings you here? . ."
            elif Girl == StormX:
                ch_s "That was an interesting experience. . ."
                $ Girl.change_face("_bemused",eyes="_side")
                ch_s "I certainly didn't mnd the attention. . ."
                $ Girl.change_face("_sexy")
                ch_s "You might want to knock in future though."
            elif Girl == JubesX:
                ch_v "I don't usually get unexpected visitors . ."
                $ Girl.change_face("_bemused",eyes="_side")
                ch_v "but I didn't mind the company. . ."
                $ Girl.change_face("_sexy")
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

        $ Girl.arm_pose = 1
        $ Girl.change_outfit(outfit_changed=0)

    return



label Girls_Caught_Lesing(Girl=0, Girl2=0, temp_Girls=[]):


    $ temp_Girls = active_Girls[:]
    if Girl in all_Girls:
        $ temp_Girls.remove(Girl)
    while temp_Girls and not Girl:
        if temp_Girls[0] not in Party and temp_Girls[0].location == bg_current and "lesbian" in temp_Girls[0].recent_history:


            $ Girl = temp_Girls[0]
            $ temp_Girls = [1]
        $ temp_Girls.remove(temp_Girls[0])
    if Girl and not Girl2:

        $ temp_Girls = active_Girls[:]
        $ temp_Girls.remove(Girl)
        while temp_Girls:
            if temp_Girls[0] not in Party and temp_Girls[0].location == bg_current and "lesbian" in temp_Girls[0].recent_history:


                $ Girl2 = temp_Girls[0]
                $ temp_Girls = [1]
            $ temp_Girls.remove(temp_Girls[0])

    if not Girl or not Girl2:
        return True

    $ Girl.drain_word("lesbian",1,0)
    $ Girl2.drain_word("lesbian",1,0)

    $ Girl.add_word(0,"lesbian","lesbian")
    $ Girl2.add_word(0,"lesbian","lesbian")
    $ Girl.add_word(1,0,0,0,"les "+Girl2.tag)
    $ Girl2.add_word(1,0,0,0,"les "+Girl.tag)

    "As you approach her room, you hear soft moans from inside, and notice that the door is slightly ajar."
    $ line = 0
    while not line:
        menu:
            extend ""
            "Knock politely":
                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."
                $ Girl.change_face("_confused",2,eyes = "_surprised",mouth = "_smile")
                $ Girl2.change_face("_confused",2,eyes = "_surprised",mouth = "_smile")
                $ primary_action = None
                $ girl_offhand_action = None
                $ second_girl_primary_action = None
                $ second_girl_offhand_action = None
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
                $ Girl.change_face("_smile",1)
                $ Girl2.change_face("_smile",1)
                $ approval_bonus += 10
                $ line = 1
            "Peek inside":
                call set_the_scene
                $ Girl.change_face("_kiss",1,eyes = "_closed")
                $ Girl2.change_face("_kiss",1,eyes = "_closed")
                $ primary_action = "lesbian"
                $ girl_offhand_action = "fondle_pussy"
                $ second_girl_primary_action = "fondle_pussy"
                "You see [Girl.name] and [Girl2.name], eyes closed and stroking each other vigorously."
            "Enter quietly":
                call set_the_scene (silent = True)
                $ Girl.change_face("_kiss",1,eyes = "_closed")
                $ Girl2.change_face("_kiss",1,eyes = "_closed")
                $ primary_action = "lesbian"
                $ girl_offhand_action = "fondle_pussy"
                $ second_girl_primary_action = "fondle_pussy"
                $ Girl.add_word(1,"unseen","unseen")
                $ Girl2.add_word(1,"unseen","unseen")
                $ Partner = Girl2
                $ line = 0
                call expression Girl.tag + "_SexAct" pass ("lesbian")
            "Leave quietly":
                "You leave the girls to their business and slip out."
                $ Girl.thirst -= 30
                $ Girl.lust = 20
                $ Girl2.thirst -= 30
                $ Girl2lust = 20
                $ renpy.pop_call()
                jump campus_Map
    $ line = 0
    return





label caught_showering(Girl):
    call shift_focus (Girl)

    $ Options = []

    $ Girl.add_word(1,"showered","showered",0,0)

    call remove_girl("all")

    $ Girl.change_outfit("nude")
    $ Girl.change_face("_smile",1)

    $ Girl.location = "bg_showerroom"
    $ Girl.wet = 1
    $ Girl.grool = 2

    if "will_masturbate" in Girl.daily_history:
        "As you approach the showers, you hear some shallow moans from inside."
    else:
        "As you approach the showers, you hear some humming noises from inside."

    menu:
        "What do you do?"
        "Enter":
            $ knock = False
        "Knock":
            $ knock = True
        "Come back later":
            call remove_girl (Girl)

            $ Girl.change_outfit(6)
            $ Girl.drain_word("will_masturbate",0,1)
            $ Girl.lust = 25
            $ Girl.thirst -= int(Girl.thirst/2) if Girl.thirst >= 50 else int(Girl.thirst/4)

            jump campus

    if knock:
        "You knock on the door. You hear some shuffling inside"

        $ Girl.outfit["top"] = "_towel"

        if "will_masturbate" in Girl.daily_history:
            "You hear a sharp shuffling sound and the water gets cut off."
            "After several seconds and some more shuffling, [Girl.name] comes to the door."

            $ bg_current = "bg_showerroom"

            $ Girl.change_face("_perplexed",2,mouth="_normal")

            call set_the_scene(check_if_dressed = False)

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

            $ bg_current = "bg_showerroom"

            call set_the_scene(check_if_dressed = False)

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
        $ bg_current = "bg_showerroom"

        if "will_masturbate" in Girl.daily_history:
            $ Girl.drain_word("will_masturbate",0,1)
            $ Girl.change_face("_sexy",eyes="_closed")
            $ Girl.add_word(1,"unseen","unseen",0,0)

            call set_the_scene(check_if_dressed = False)

            $ Count = 0
            $ primary_action = "masturbation"
            $ girl_offhand_action = "fondle_pussy"

            "You see [Girl.name] under the shower, feeling herself up."

            call expression Girl.tag + "_SexAct" pass ("masturbation")

            $ renpy.pop_call()
            jump shower_room
        elif D20 >= 15:
            call set_the_scene(check_if_dressed = False)

            $ Girl.change_face("_surprised", 1)

            "As you enter the showers, you see [Girl.name] washing up."

            call expression Girl.tag + "_First_Bottomless" pass (1)
            call expression Girl.tag + "_First_Topless" pass (1)

            if not approval_check(Girl, 1200) or not Girl.seen_pussy or not Girl.seen_breasts:
                $ Girl.brows="_angry"
                $ Girl.outfit["top"] = "_towel"

                "She grabs a towel and covers up."

                $ Girl.change_face("_angry", 1)
                $ Girl.change_stat("love", 80, -5)
            else:
                if "exhibitionist" in Girl.traits:
                    $ Girl.change_stat("lust", 90, (2*D20))
                else:
                    $ Girl.change_stat("lust", 80, D20)

                $ Girl.brows="_confused"

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
                    if not approval_check(Girl, 500,"I"):
                        $ Girl.change_stat("love", 50, -3)
                        $ Girl.change_stat("obedience", 50, 2)

                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                "It's not as if you're leaving that much to the imagination. . ." if Girl == EmmaX:
                    $ EmmaX.change_stat("obedience", 50, 2)
                    $ EmmaX.change_stat("obedience", 80, 2)
                    $ EmmaX.change_stat("inhibition", 60, 2)
        else:
            $ Girl.outfit["top"] = "_towel"

            call set_the_scene(check_if_dressed = False)

            "As you enter the showers, you see [Girl.name] putting on a towel."

            if not approval_check(Girl, 1100) and (not Girl.seen_pussy or not Girl.seen_breasts):
                $ Girl.change_face("_angry",brows="_confused")
                $ Girl.change_stat("love", 80, -5)
            else:
                $ Girl.change_face("_sexy",brows="_confused")

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
                    if approval_check(Girl, 500,"I"):
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

        $ Girl.change_face("_sexy")

        if Girl == StormX:
            ch_s "Oh, that's fine, [Girl.player_petname]."
            ch_s "You might want to be careful with the other girls though."
        elif not approval_check(Girl, 1000) or not Girl.seen_pussy or not Girl.seen_breasts:
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
        elif not approval_check(Girl, 1300):
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

            if Girl.outfit["top"] == "_towel":
                $ Girl.outfit["top"] = ""

                pause 0.5

                $ Girl.outfit["top"] = "_towel"

                "She flashes you real quick."

                call expression Girl.tag + "_First_Bottomless" pass (1)
                call expression Girl.tag + "_First_Topless" pass (1)

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
            call remove_girl (Girl)
        "Actually, could you stick around a minute?":
            if approval_check(Girl, 900) or Girl == StormX:
                if Girl == RogueX:
                    ch_r "Sure, what's up?"
                elif Girl == KittyX:
                    ch_k "Yeah?"
                elif Girl == EmmaX:
                    ch_e "Very well, what did you need?"
                elif Girl == LauraX:
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

                call remove_girl(Girl)

    return False

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
                call AskedMeet (Other, "_bemused")
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
