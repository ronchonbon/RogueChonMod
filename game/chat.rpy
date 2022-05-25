label chat:
    menu:
        "Chat with [RogueX.name]" if RogueX.location == bg_current:
            $ Girl = RogueX
        "Text [RogueX.name]" if RogueX.location != bg_current:
            $ Girl = RogueX
        "Chat with [KittyX.name]" if KittyX.location == bg_current:
            $ Girl = KittyX
        "Text [KittyX.name]" if KittyX.location != bg_current and "met" in KittyX.history:
            $ Girl = KittyX
        "Chat with [EmmaX.name]" if EmmaX.location == bg_current:
            $ Girl = EmmaX
        "Text [EmmaX.name]" if EmmaX.location != bg_current and "met" in EmmaX.history:
            $ Girl = EmmaX
        "Chat with [LauraX.name]" if LauraX.location == bg_current:
            $ Girl = LauraX
        "Text [LauraX.name]" if LauraX.location != bg_current and "met" in LauraX.history:
            $ Girl = LauraX
        "Chat with [JeanX.name]" if JeanX.location == bg_current:
            $ Girl = JeanX
        "Text [JeanX.name]" if JeanX.location != bg_current and "met" in JeanX.history:
            $ Girl = JeanX
        "Chat with [StormX.name]" if StormX.location == bg_current:
            $ Girl = StormX
        "Text [StormX.name]" if StormX.location != bg_current and "met" in StormX.history:
            $ Girl = StormX
        "Chat with [JubesX.name]" if JubesX.location == bg_current:
            $ Girl = JubesX
        "Text [JubesX.name]" if JubesX.location != bg_current and "met" in JubesX.history:
            $ Girl = JubesX
        "Never Mind":
            return

    if Girl:
        if Girl.location == bg_current:
            if Girl == EmmaX and "classcaught" not in EmmaX.history:
                jump Emma_chat_Minimal

            if "caught" in Girl.daily_history:
                if Girl == RogueX:
                    ch_r "We should probably keep our distance for now."
                elif Girl == KittyX:
                    ch_k "I'm[Girl.like]going to keep my distance 'til this blows over."
                elif Girl == EmmaX:
                    ch_e "I don't think we should be seen together, if you don't mind."
                elif Girl == LauraX:
                    ch_l "I think we should lie low for a bit."
                elif Girl == JeanX:
                    ch_j "You got me in trouble."
                elif Girl == StormX:
                    ch_s "We should probably keep our distance. . ."
                elif Girl == JubesX:
                    ch_v "I want to keep my distance for now. . ."

                return

            if Girl == LauraX and Girl.location == bg_current and "scent" in Player.daily_history:
                if not approval_check(Girl, 1700) and not approval_check(Girl, 600,"O"):
                    python:
                        for G in all_Girls:
                            if G in Player.daily_history and "saw with " + G.tag not in Girl.traits and Girl.likes[G.tag] <= 700:
                                Girl.traits.append("saw with " + G.tag)

                $ Player.daily_history.remove("scent")

            if "lesbian" in Girl.recent_history:
                if Girl == RogueX:
                    ch_r "Ooof. . . gimme a minute. . ."
                    "You hear some shifting around. . ."
                    ch_r "Ok, just um, never mind. . ."
                    "You hear some muffled giggles in the background."
                elif Girl == KittyX:
                    ch_k "Ah! One minute. . ."
                    "You hear some shifting around. . ."
                    ch_k "Ok, (\"quit it!\") what did you. . .)"
                    "You hear some muffled giggles in the background."
                    ch_k "So. . ."
                elif Girl == EmmaX:
                    ch_e "One moment, [Girl.player_petname]. . ."
                    "You hear some shifting around. . ."
                    ch_e "Ok, so. . ."
                    "You hear some muffled giggles in the background."
                elif Girl == LauraX:
                    ch_l "Just a minute. . ."
                    "You hear some shifting around. . ."
                    ch_l "Yeah, um. . . what was it you wanted?"
                    "You hear some muffled giggles in the background."
                    ch_l "So. . ."
                elif Girl == JeanX:
                    ch_j "One minute. . ."
                    "You hear some shifting around. . ."
                    ch_j "Ok, that should. . . what is it?"
                    "You hear some muffled giggles in the background."
                elif Girl == StormX:
                    ch_s "One moment, [Girl.player_petname]. . ."
                    "You hear some shifting around. . ."
                    ch_s "What was it that you wanted?"
                    "You hear some muffled giggles in the background."
                elif Girl == JubesX:
                    ch_v "Oh, hey! One sec. . ."
                    "You hear some shifting around. . ."
                    ch_v "Hey, hey, (stop!) What did you want? . .)"
                    "You hear some muffled giggles in the background."
                    ch_v "Um. . . anyway."

            if "_angry" not in Girl.recent_history:
                if Girl == RogueX:
                    ch_r "So what did you want to talk about, [Girl.player_petname]?"
                elif Girl == KittyX:
                    ch_k "So[Girl.like]what did you want to talk about, [Girl.player_petname]?"
                elif Girl == EmmaX:
                    ch_e "What was it you wanted to discuss, [Girl.player_petname]?"
                elif Girl == LauraX:
                    ch_l "Yeah?"
                elif Girl == JeanX:
                    ch_j "What is it?"
                elif Girl == StormX:
                    ch_s "What can I do for you, [Girl.player_petname]?"
                elif Girl == JubesX:
                    ch_v "Hey, what can I do for ya, [Girl.player_petname]?"

            call chat_menu
        elif Girl in phonebook:
            if Girl.location == "hold":
                "She doesn't seem to be picking up."
            else:
                if Girl == EmmaX:
                    if EmmaX.location == "bg_teacher" and bg_current == "bg_classroom":
                        "She texts back, \"We can speak after class, [EmmaX.player_petname].\""

                        return
                    elif "classcaught" not in EmmaX.history:
                        jump Emma_chat_Minimal

                if Girl == StormX:
                    if StormX.location == "bg_teacher" and bg_current == "bg_classroom":
                        "She texts back, \"This can wait until after class, [StormX.player_petname].\""

                        return

                if Girl.location != bg_current:
                    show cellphone at sprite_location(stage_left)
                else:
                    hide cellphone

                "You send [Girl.name] a text."

                if "_angry" not in Girl.recent_history:
                    if Girl == RogueX:
                        ch_r "So what did you want to talk about, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "So[Girl.like]what did you want to talk about, [Girl.player_petname]?"
                    elif Girl == EmmaX:
                        ch_e "What was it you wanted to discuss, [Girl.player_petname]?"
                    elif Girl == LauraX:
                        ch_l "Yeah?"
                    elif Girl == JeanX:
                        ch_j "What is it?"
                    elif Girl == StormX:
                        ch_s "What can I do for you, [Girl.player_petname]?"
                    elif Girl == JubesX:
                        ch_v "Hey, what can I do for ya, [Girl.player_petname]?"

                call chat_menu
        else:
            "You don't know her number, you'll have to go to her."

    return

label chat_menu:
    $ Girl.change_face()

    call shift_focus(Girl)

    if Girl.location != bg_current:
        show cellphone at sprite_location(stage_left)
    else:
        hide cellphone

    if "_angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I really don't want to talk to you right now."
        elif Girl == KittyX:
            ch_k "I'm[Girl.like]so mad at you right now!"
        elif Girl == EmmaX:
            ch_e "I would not press my luck if I were you."
        elif Girl == LauraX:
            ch_l "You don't want to be around me right now."
        elif Girl == JeanX:
            ch_j "Get away from me."
        elif Girl == StormX:
            ch_s "You do not want to tangle with me right now."
        elif Girl == JubesX:
            ch_v "Not in the mood, [Girl.player_petname]."

        return

    if time_index == 2 and "going_on_date" in Player.daily_history:
        call Readytogo (Girl)

    menu:
        "Come on over." if Girl.location != bg_current:
            if Girl in Nearby and bg_current != "bg_showerrroom":
                call Swap_Nearby(Girl)
            elif Room_Full():
                "It's already pretty crowded here."

                call dismiss_menu
            else:
                call expression Girl.tag + "_Summon"
        "Ask [Girl.name] to leave" if Girl.location == bg_current:
            call dismiss_girl (Girl)

            return
        "Romance her":
            menu:
                "Flirt with her (locked)" if Girl.had_chat[5]:
                    pass
                "Flirt with her" if not Girl.had_chat[5]:
                    call Flirt (Girl)
                "Sex Menu (locked)" if Girl.location != bg_current:
                    pass
                "Sex Menu" if Girl.location == bg_current:
                    if Girl.love >= Girl.obedience:
                        ch_p "Did you want to fool around?"
                    else:
                        ch_p "I'd like to get naughty."

                    if "_angry" in Girl.recent_history:
                        if Girl == RogueX:
                            ch_r "I don't want to deal with you right now."
                        elif Girl == KittyX:
                            ch_k "Not even!"
                        elif Girl == EmmaX:
                            ch_e "You should know better than that."
                        elif Girl == LauraX:
                            ch_l "Bad idea right now."
                        elif Girl == JeanX:
                            ch_j "-So- not interested."
                        elif Girl == StormX:
                            ch_s "I am uninterested."
                        elif Girl == JubesX:
                            ch_v "Not in the mood, [Girl.player_petname]?"
                    elif approval_check(Girl, 600, "LI"):
                        $ Girl.change_face("_sexy")

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

                        call shift_focus(Girl)
                        call enter_main_sex_menu

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

                        call shift_focus(Girl)
                        call enter_main_sex_menu

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
                "Dirty Talk (locked)" if Girl.SEXP < 10:
                    pass
                "Dirty Talk" if Girl.SEXP >= 10:
                    ch_p "About when we get together. . ."

                    call expression Girl.tag + "_Sexchat"
                "Date (locked)" if time_index > 2:
                    pass
                "Date" if time_index <= 2:
                    ch_p "Do you want to go on a date tonight?"

                    call Date_Ask (Girl)
                "gifts (locked)" if Girl.location != bg_current:
                    pass
                "gifts" if Girl.location == bg_current:
                    ch_p "I'd like to give you something."

                    call gifts
                "Back":
                    pass
        "Talk with her":
            menu:
                "I just wanted to talk. . .":
                    call expression Girl.tag + "_Chitchat"
                "Relationship status":
                    ch_p "Could we talk about us?"

                    if Girl.location == bg_current:
                        call expression Girl.tag + "_Relationship"
                    else:
                        if Girl == RogueX:
                            ch_r "That sounds like it might be a little heavy to do over the phone."
                            ch_r "Maybe later?"
                        elif Girl == KittyX:
                            ch_k "That seems like something we'd want to do face to face."
                            ch_k "Maybe later?"
                        elif Girl == EmmaX:
                            ch_e "This seems a bit serious to discuss over the phone."
                            ch_e "Later, perhaps."
                        elif Girl == LauraX:
                            ch_l "Sounds heavy."
                            ch_l "Maybe later when we're face to face?"
                        elif Girl == JeanX:
                            ch_j "That sounds like a conversation to have in person, yeah?"
                        elif Girl == StormX:
                            ch_s "That seems like a conversation that we should have face to face."
                            ch_s "Perhaps at a later date."
                        elif Girl == JubesX:
                            ch_v "Well that sounds ominous."
                            ch_v "Maybe see me in person?"
                "Other girls":
                    menu:
                        "How do you feel about [RogueX.name]?" if Girl != RogueX:
                            call expression Girl.tag + "_About" pass (RogueX)
                        "How do you feel about [KittyX.name]?" if Girl != KittyX and "met" in KittyX.history:
                            call expression Girl.tag + "_About" pass (KittyX)
                        "How do you feel about [EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.history:
                            call expression Girl.tag + "_About" pass (EmmaX)
                        "How do you feel about [LauraX.name]?" if Girl != LauraX and "met" in LauraX.history:
                            call expression Girl.tag + "_About" pass (LauraX)
                        "How do you feel about [JeanX.name]?" if Girl != JeanX and "met" in JeanX.history:
                            call expression Girl.tag + "_About" pass (JeanX)
                        "How do you feel about [StormX.name]?" if Girl != StormX and "met" in StormX.history:
                            call expression Girl.tag + "_About" pass (StormX)
                        "How do you feel about [JubesX.name]?" if Girl != JubesX and "met" in JubesX.history:
                            call expression Girl.tag + "_About" pass (JubesX)
                        "About hooking up with other girls. . .":
                            call expression Girl.tag + "_Monogamy"
                        "Never mind.":
                            pass
                "Could I get your number?" if Girl not in phonebook:
                    if Girl == EmmaX and approval_check(Girl, 800, "LI"):
                        ch_e "I don't see why not."

                        $ phonebook.append(Girl)
                    elif Girl != EmmaX and (approval_check(Girl, 400, "L") or approval_check(Girl, 200, "I")):
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

                        $ phonebook.append(Girl)
                    elif approval_check(Girl, 200, "O",Alt=[[EmmaX],500-EmmaX.inhibition]):
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

                        $ phonebook.append(Girl)
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
        "Change her":
            call Girl_Settings
        "Add her to party" if Girl not in Party and Girl.location == bg_current:
            ch_p "Could you follow me for a bit?"

            if Girl == EmmaX and approval_check(Girl, 1250):
                $ Party.append(Girl)

                ch_e "Lead away."

                return

            if approval_check(Girl, 600,Alt=[[EmmaX,JeanX],900]):
                $ Party.append(Girl)

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
        "Disband party" if Girl in Party:
            ch_p "Ok, you can leave if you prefer."

            $ temp_Girls = Party[:]

            while temp_Girls:
                $ Party.remove(temp_Girls[0])

                call change_into_scheduled_outfit([temp_Girls[0]], 0)

                if "leaving" in temp_Girls[0].recent_history:
                    $ temp_Girls[0].drain_word("leaving")
                if temp_Girls[0] == RogueX:
                    if temp_Girls[0].location == bg_current:
                        ch_r "Ok, I'll probably stick around for a bit anyway."
                    else:
                        ch_r "Ok, see you later then."
                elif temp_Girls[0] == KittyX:
                    if temp_Girls[0].location == bg_current:
                        ch_k "Good to know, but I'm[temp_Girls[0].like] fine here."
                    else:
                        ch_k "Cool, later."
                elif temp_Girls[0] == EmmaX:
                    if temp_Girls[0].location == bg_current:
                        ch_e "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                    elif temp_Girls[0].location == "bg_teacher" and bg_current == "bg_classroom":
                        ch_e "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                    else:
                        ch_e "If that's all then, I'll see you later."
                elif temp_Girls[0] == LauraX:
                    if temp_Girls[0].location == bg_current:
                        ch_l "I think I'm fine here."
                    else:
                        ch_l "Ok, see ya then."
                elif temp_Girls[0] == JeanX:
                    ch_j "Ok."
                elif temp_Girls[0] == StormX:
                    if temp_Girls[0].location == bg_current:
                        ch_s "I would rather stay, thank you."
                    elif temp_Girls[0].location == "bg_teacher" and bg_current == "bg_classroom":
                        ch_s "I do have a class to teach. I think that I'll stay."
                    else:
                        ch_s "Ah, fine, I'll see you later."
                elif temp_Girls[0] == JubesX:
                    if temp_Girls[0].location == bg_current:
                        ch_v "Ok, but I'll stick around."
                    else:
                        ch_v "Ok, ok. Laters."

                if temp_Girls[0].location != bg_current:
                    call set_the_scene

                $ temp_Girls.remove(temp_Girls[0])

            return
        "Switch to. . .":
            call switch_chat
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

label switch_chat:
    if bg_current == "HW Party":
        "You'll have to go to the other girls if you want to talk to them."

        return

    $ line = Girl
    menu:
        "[RogueX.name]" if Girl != RogueX:
            $ Girl = RogueX
        "[KittyX.name]" if Girl != KittyX and "met" in KittyX.history:
            $ Girl = KittyX
        "[EmmaX.name]" if Girl != EmmaX and "met" in EmmaX.history:
            $ Girl = EmmaX
        "[LauraX.name]" if Girl != LauraX and "met" in LauraX.history:
            $ Girl = LauraX
        "[JeanX.name]" if Girl != JeanX and "met" in JeanX.history:
            $ Girl = JeanX
        "[StormX.name]" if Girl != StormX and "met" in StormX.history:
            $ Girl = StormX
        "[JubesX.name]" if Girl != JubesX and "met" in JubesX.history:
            $ Girl = JubesX
        "Never mind":
            $ line = 0

            return

    if Girl.location != bg_current:
        if Girl in phonebook:
            "You give [Girl.name] a call."
            if Girl == EmmaX and "classcaught" not in EmmaX.history:
                ch_e "I don't have time to talk to students right now."

                $ Girl = line
        else:
            "You don't have her number."

            $ Girl = line

    if Girl == EmmaX and "classcaught" not in EmmaX.history:
        ch_e "Surely we can discuss this later. . . alone perhaps."

        $ Girl = line

        $ line = 0

        return

    call shift_focus (Girl)

    if "_angry" not in Girl.recent_history and Girl != line:
        if Girl == RogueX:
            ch_r "So what did you want to talk about, [Girl.player_petname]?"
        elif Girl == KittyX:
            ch_k "So[Girl.like]what did you want to talk about, [Girl.player_petname]?"
        elif Girl == EmmaX:
            ch_e "What was it you wanted to discuss, [Girl.player_petname]?"
        elif Girl == LauraX:
            ch_l "Yeah?"
        elif Girl == JeanX:
            ch_j "What is it?"
        elif Girl == StormX:
            ch_s "What can I do for you, [Girl.player_petname]?"
        elif Girl == JubesX:
            ch_v "Hey, what can I do for ya, [Girl.player_petname]?"

    $ line = 0

    return













label dismiss_girl(Girl=0, Leaving=0):
    $ Girl = check_girl(Girl)
    if Girl in Party:
        $ Party.remove(Girl)
    call change_into_scheduled_outfit ([Girl], 0)

    if "leaving" in Girl.recent_history:
        $ Girl.drain_word("leaving")
    menu:
        "You can leave if you like.":
            if Girl.location == bg_current and not approval_check(Girl, 700, "O"):
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
                $ Leaving = 1
        "Could you give me the room please?":

            if Girl.location == bg_current and not approval_check(Girl, 800, "LO"):
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
                    $ Girl.change_stat("obedience", 30, 5)
                    $ Girl.change_stat("obedience", 50, 5)
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
                $ Leaving = 1
        "You can go now.":

            if Girl.location == bg_current and not approval_check(Girl, 500, "O"):
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
                $ Girl.change_face("_confused")
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
                if "dismissed" not in Girl.daily_history:
                    $ Girl.change_stat("obedience", 40, 10)
                    $ Girl.change_stat("obedience", 60, 5)
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
                $ Leaving = 1
        "Nevermind.":

            return

    if not Leaving and bg_current in ("bg_campus","bg_classroom","bg_dangerroom"):

        call remove_girl (Girl, 1, 1)
    elif not Leaving:

        menu:
            extend ""
            "I insist, get going.":
                if Girl.location != bg_current and (approval_check(Girl, 1200, "LO") or approval_check(Girl, 500, "O")):

                    if "dismissed" not in Girl.daily_history:
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("obedience", 50, 10)
                        $ Girl.change_stat("obedience", 80, 5)
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
                    $ Leaving = 1
                elif Girl.location != bg_current and (approval_check(Girl, 1000, "LO") or approval_check(Girl, 300, "O")):

                    if "dismissed" not in Girl.daily_history:
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("obedience", 50, 10)
                        $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_face("_angry")
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
                    $ Leaving = 1
                elif Girl.location != bg_current:

                    if "dismissed" not in Girl.daily_history:
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("love", 70, -10, 1)
                        $ Girl.change_stat("obedience", 50, -5)
                        $ Girl.change_stat("inhibition", 50, 5)
                        $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.change_face("_angry")
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
                elif approval_check(Girl, 1400, "LO") or approval_check(Girl, 400, "O"):

                    if "dismissed" not in Girl.daily_history:
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("obedience", 50, 10)
                        $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_face("_sad")
                    if Girl == RogueX:
                        ch_r "Ok, if that's what you want."
                    elif Girl == KittyX:
                        ch_k "Um, sure, fine."
                    elif Girl == EmmaX:
                        ch_e "I suppose I could get out of your way."
                    elif Girl == LauraX:
                        ch_l "Ok."
                    elif Girl == JeanX:
                        ch_j "Whatever."
                    elif Girl == StormX:
                        ch_s "Fine."
                    elif Girl == JubesX:
                        ch_v "Ok, fine. . ."
                    $ Leaving = 1
                else:

                    if "dismissed" not in Girl.daily_history:
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("love", 70, -10, 1)
                        $ Girl.change_stat("obedience", 50, -5)
                        $ Girl.change_stat("inhibition", 50, 3)
                        $ Girl.change_stat("inhibition", 80, 2)
                    $ Girl.change_face("_sad")
                    if Girl == RogueX:
                        ch_r "You wish."
                    elif Girl == KittyX:
                        ch_k "Yeah right."
                    elif Girl == EmmaX:
                        ch_e "That doesn't look like it'll be happening."
                    elif Girl == LauraX:
                        ch_l "Nope."
                    elif Girl == JeanX:
                        ch_j "What? No"
                    elif Girl == StormX:
                        ch_s "Oh, certainly not."
                    elif Girl == JubesX:
                        ch_v "Def not. . ."
            "Ok, nevermind.":

                pass

    if "dismissed" not in Girl.daily_history:
        $ Girl.daily_history.append("dismissed")
    if Girl in Nearby:
        "You shift a bit away from [Girl.name]"
    elif Leaving == 0:

        $ Girl.location = bg_current
    else:

        if Girl.location != bg_current:
            pass
        elif bg_current == Girl.home:
            $ Girl.location = "bg_campus"
        else:
            $ Girl.location = Girl.home
        call AllReset (Girl)
        "[Girl.name] heads out."
    return



label Girl_Settings:
    if Girl not in all_Girls:
        $ Girl == focused_Girl
    call shift_focus (Girl)
    while True:
        menu:
            ch_p "Let's talk about you."
            "Wardrobe":
                ch_p "I wanted to talk about your style."
                if bg_current == "HW Party":
                    Girl.voice "Not at the party. . ."
                else:
                    call taboo_level
                    call expression Girl.tag + "_Clothes"

            "Shift her Personality" if approval_check(Girl, 900, "L", taboo_modifier=0) or approval_check(Girl, 900, "O", taboo_modifier=0)or approval_check(Girl, 900, "I", taboo_modifier=0):
                ch_p "Could we talk about us?"
                call expression Girl.tag + "_Personality"
            "Your Petname":

                ch_p "Could we talk about my pet name?"
                call expression Girl.tag + "_names"
            "[Girl.name]'s Petname":

                ch_p "I've got a pet name for you, you know?"
                call expression Girl.tag + "_Pet"

            "[Girl.name]'s name" if len(Girl.names) > 1:
                ch_p "You know how you told me you went by a different name?"
                call expression Girl.tag + "_Rename"

            "Follow options" if "follow" in Girl.traits:
                ch_p "You know how you ask if I want to follow you sometimes?"
                $ line = 0
                if Girl == RogueX:
                    ch_r "Yes?"
                elif Girl == EmmaX:
                    ch_e "Yes?"
                elif Girl == JeanX:
                    ch_j "Not really, but go on?"
                elif Girl == StormX:
                    ch_s "Yes?"
                else:
                    Girl.voice "Yeah?"
                menu:
                    extend ""
                    "You can go where you want, I'll catch up later." if "freetravels" not in Girl.traits:
                        $ Girl.change_face("_perplexed")
                        if Girl == RogueX:
                            ch_r "Oh, ok, not a problem."
                        elif Girl == KittyX:
                            ch_k "Um[Girl.like]okay."
                        elif Girl == EmmaX:
                            ch_e "Fine, I'll leave some mystery."
                        elif Girl == LauraX:
                            ch_l "Oh. . . okay."
                        elif Girl == JeanX:
                            ch_j "Ooookay?"
                        elif Girl == StormX:
                            ch_s "Very well?"
                        elif Girl == JubesX:
                            ch_v "Oh, sure, ok. . ."
                        if "follow" not in Girl.daily_history:
                            $ Girl.change_stat("love", 90, -2)
                            $ Girl.change_stat("obedience", 30, 5)
                        $ line = "free"

                    "You can ask if I want to follow you." if "asktravels" not in Girl.traits or "freetravels" in Girl.traits:
                        $ Girl.change_face("_perplexed")
                        if Girl == RogueX:
                            ch_r "Oh, ok, not a problem."
                        elif Girl == KittyX:
                            ch_k "Um[Girl.like]okay."
                        elif Girl == EmmaX:
                            ch_e "Don't want to be left behind?"
                        elif Girl == LauraX:
                            ch_l "Right. . ."
                        elif Girl == JeanX:
                            ch_j "Noted?"
                        elif Girl == StormX:
                            ch_s "Very well?"
                        elif Girl == JubesX:
                            ch_v "Ok, yeah, wouldn't want you falling behind. . ."
                        if "follow" not in Girl.daily_history:
                            $ Girl.change_stat("love", 70, 2)
                            $ Girl.change_stat("inhibition", 60, 2)
                        $ line = "ask"

                    "Don't ever leave when I'm around." if "lockedtravels" not in Girl.traits or "freetravels" in Girl.traits:
                        if approval_check(Girl, 500, "O",Alt=[[EmmaX,JeanX],600]) or approval_check(Girl, 900, "L"):
                            $ Girl.change_face("_sexy")
                            if Girl == RogueX:
                                ch_r "Oh, Ok."
                            elif Girl == KittyX:
                                ch_k "Aw, you miss me when I'm not around!"
                            elif Girl == EmmaX:
                                $ Girl.change_face("_angry", eyes="_side")
                                ch_e "I don't know why I put up with your nonsense."
                                $ Girl.change_face("_sexy",1)
                                ch_e "But {i}fine.{/i}"
                            elif Girl == LauraX:
                                ch_l "That's sweet."
                            elif Girl == JeanX:
                                ch_j ". . ."
                                ch_j "We'll see. . ."
                            elif Girl == StormX:
                                ch_s "I suppose. . ."
                            elif Girl == JubesX:
                                ch_v "Oh, ok. . ."
                            if "follow" not in Girl.daily_history:
                                if Girl.love > 90:
                                    $ Girl.change_stat("love", 99, 2)
                                $ Girl.change_stat("obedience", 60, 5)
                            $ Girl.change_stat("inhibition", 50, -5, 1)
                            $ line = "lock"
                        else:
                            $ Girl.change_face("_angry")
                            if Girl == RogueX:
                                ch_r "Well, I don't really care what you think on the matter."
                            elif Girl == KittyX:
                                ch_k "Well, who cares what you think?"
                            elif Girl == EmmaX:
                                ch_e "Where I go is my own business."
                            elif Girl == LauraX:
                                ch_l "Well, who cares what you think?"
                            elif Girl == JeanX:
                                ch_j "Right, that sounds like something I'd do. . ."
                            elif Girl == StormX:
                                ch_s "Do not presume to control me."
                            elif Girl == JubesX:
                                ch_v "Well, we'll see. . ."
                    "Never mind.":

                        if Girl == RogueX:
                            ch_r "Oh, ok."
                        elif Girl == KittyX:
                            ch_k "Ooookay."
                        elif Girl == EmmaX:
                            ch_e "Whatever."
                        elif Girl == LauraX:
                            ch_l "Right. . ."
                        elif Girl == JeanX:
                            ch_j "OK?"
                        elif Girl == StormX:
                            ch_s "Very Well."
                        elif Girl == JubesX:
                            ch_v "Right. . ."

                if line:
                    $ Girl.daily_history.append("follow")
                    if "freetravels" in Girl.traits:
                        $ Girl.traits.remove("freetravels")
                    if "asktravels" in Girl.traits:
                        $ Girl.traits.remove("asktravels")
                    if "lockedtravels" in Girl.traits:
                        $ Girl.traits.remove("lockedtravels")

                    if line == "free":
                        $ Girl.traits.append("freetravels")
                    elif line == "ask":
                        $ Girl.traits.append("asktravels")
                    elif line == "lock":
                        $ Girl.traits.append("lockedtravels")
                    $ line = 0

            "\"Like\" options" if Girl == KittyX:
                ch_p "So you[Girl.like]say \"[Girl.like]\" a lot. . ."
                if approval_check(Girl, 800):
                    call KittyLike
                else:
                    ch_k "[Girl.Like]what's it to you?"
            "Boundaries":

                menu:
                    "Should she come by unannounced?"
                    "Yes [[default]":
                        ch_p "You can come over whenever you feel like it."
                        $ Girl.change_face("_smile")
                        if Girl == RogueX:
                            ch_r "Will do."
                        elif Girl == KittyX:
                            ch_k "Um[Girl.like]cool."
                        elif Girl == EmmaX:
                            ch_e "Fine, I might."
                        elif Girl == LauraX:
                            ch_l "Oh. . . okay."
                        elif Girl == JeanX:
                            ch_j "Whatever."
                        elif Girl == StormX:
                            ch_s "I'd like that."
                        elif Girl == JubesX:
                            ch_v "Ok, I'll see you sometime then. . ."
                        $ Girl.drain_word("lockedout",0,0,1)
                    "No":
                        ch_p "Could you please not just drop by unannounced?"
                        $ Girl.change_face("_perplexed")
                        if Girl == RogueX:
                            ch_r "Oh, ok, not a problem."
                        elif Girl == KittyX:
                            ch_k "Um[Girl.like]okay."
                        elif Girl == EmmaX:
                            ch_e "Fine, I'll contact you first."
                        elif Girl == LauraX:
                            ch_l "Oh. . . okay."
                        elif Girl == JeanX:
                            ch_j "Whatever."
                        elif Girl == StormX:
                            ch_s "I can respect that."
                        elif Girl == JubesX:
                            ch_v "Sure, I can give you space. . ."
                        $ Girl.change_face("_smile")
                        $ Girl.add_word(1,0,0,"lockedout")
            "Switch to. . .":
                call switch_chat
            "Never mind.":

                return
