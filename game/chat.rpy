label Chat(Girl=0):
    if not Girl:
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

                pass
    if Girl:
        if Girl.location == bg_current:
            if Girl == EmmaX and "classcaught" not in EmmaX.history:
                jump Emma_Chat_Minimal
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
                    $ Options = all_Girls[:]
                    while Options:
                        if Options[0] in Player.daily_history and "saw with " + Options[0].tag not in Girl.traits and Girl.GirlLikeCheck(Options[0]) <= 700:
                            $ Girl.traits.append("saw with " + Options[0].tag)
                        $ Options.remove(Options[0])
                $ Player.daily_history.remove("scent")

            if "les" in Girl.recent_history:

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
            call Chat_Menu

        elif Girl in Digits:
            if Girl.location == "hold":
                "She doesn't seem to be picking up."
            else:
                if Girl == EmmaX:
                    if EmmaX.location == "bg_teacher" and bg_current == "bg_classroom":
                        "She texts back, \"We can speak after class, [EmmaX.player_petname].\""
                        return
                    elif "classcaught" not in EmmaX.history:
                        call Emma_Chat_Minimal
                        return
                if Girl == StormX:
                    if StormX.location == "bg_teacher" and bg_current == "bg_classroom":
                        "She texts back, \"This can wait until after class, [StormX.player_petname].\""
                        return
                if Girl.location != bg_current:
                    show Cellphone at sprite_location(stage_left)
                else:
                    hide Cellphone
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
                call Chat_Menu
        else:
            "You don't know her number, you'll have to go to her."
    return

label Chat_Menu:

    $ Girl = GirlCheck(Girl)
    $ Girl.change_face()
    call shift_focus (Girl)
    if Girl.location != bg_current:
        show Cellphone at sprite_location(stage_left)
    else:
        hide Cellphone

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

    if time_index == 2 and "yesdate" in Player.daily_history:

        call Readytogo (Girl)










    menu:
        "Come on over." if Girl.location != bg_current:
            if Girl in Nearby and bg_current != "bg_showerrroom":
                call Swap_Nearby (Girl)
            elif Room_Full():
                "It's already pretty crowded here."
                call Dismissed
            else:
                call expression Girl.tag + "_Summon"
        "Ask [Girl.name] to leave" if Girl.location == bg_current:
            call Girl_Dismissed (Girl)
            return
        "Romance her":

            menu:
                "Flirt with her (locked)" if Girl.Chat[5]:
                    pass
                "Flirt with her" if not Girl.Chat[5]:
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
                        jump enter_main_sex_menu
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
                        jump enter_main_sex_menu
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
                    $ Line = 0
                    call expression Girl.tag + "_SexChat"

                "Date (locked)" if time_index > 2:
                    pass
                "Date" if time_index <= 2:
                    ch_p "Do you want to go on a date tonight?"
                    call Date_Ask (Girl)

                "Gifts (locked)" if Girl.location != bg_current:
                    pass
                "Gifts" if Girl.location == bg_current:
                    ch_p "I'd like to give you something."
                    call Gifts
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

                "Could I get your number?" if Girl not in Digits:
                    if Girl == EmmaX and approval_check(Girl, 800, "LI"):
                        ch_e "I don't see why not."
                        $ Digits.append(Girl)
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
                        $ Digits.append(Girl)
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
                        $ Digits.append(Girl)
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
            $ Options = Party[:]
            while Options:
                $ Party.remove(Options[0])
                call Girls_Schedule ([Options[0]], 0)
                if "leaving" in Options[0].recent_history:
                    $ Options[0].drain_word("leaving")
                if Options[0] == RogueX:
                    if Options[0].location == bg_current:
                        ch_r "Ok, I'll probably stick around for a bit anyway."
                    else:
                        ch_r "Ok, see you later then."
                elif Options[0] == KittyX:
                    if Options[0].location == bg_current:
                        ch_k "Good to know, but I'm[Options[0].like] fine here."
                    else:
                        ch_k "Cool, later."
                elif Options[0] == EmmaX:
                    if Options[0].location == bg_current:
                        ch_e "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                    elif Options[0].location == "bg_teacher" and bg_current == "bg_classroom":
                        ch_e "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                    else:
                        ch_e "If that's all then, I'll see you later."
                elif Options[0] == LauraX:
                    if Options[0].location == bg_current:
                        ch_l "I think I'm fine here."
                    else:
                        ch_l "Ok, see ya then."
                elif Options[0] == JeanX:



                    ch_j "Ok."
                elif Options[0] == StormX:
                    if Options[0].location == bg_current:
                        ch_s "I would rather stay, thank you."
                    elif Options[0].location == "bg_teacher" and bg_current == "bg_classroom":
                        ch_s "I do have a class to teach. I think that I'll stay."
                    else:
                        ch_s "Ah, fine, I'll see you later."
                elif Options[0] == JubesX:
                    if Options[0].location == bg_current:
                        ch_v "Ok, but I'll stick around."
                    else:
                        ch_v "Ok, ok. Laters."
                if Options[0].location != bg_current:
                    call set_the_scene
                $ Options.remove(Options[0])
            return
        "Switch to. . .":

            call Switch_Chat
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
    jump Chat_Menu

label Switch_Chat:

    if bg_current == "HW Party":
        "You'll have to go to the other girls if you want to talk to them."
        return
    $ Line = Girl
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
            $ Line = 0
            return

    if Girl.location != bg_current:
        if Girl in Digits:
            "You give [Girl.name] a call."
            if Girl == EmmaX and "classcaught" not in EmmaX.history:
                ch_e "I don't have time to talk to students right now."
                $ Girl = Line
        else:
            "You don't have her number."
            $ Girl = Line
    if Girl == EmmaX and "classcaught" not in EmmaX.history:
        ch_e "Surely we can discuss this later. . . alone perhaps."
        $ Girl = Line
        $ Line = 0
        return
    call shift_focus (Girl)
    if "_angry" not in Girl.recent_history and Girl != Line:
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
    $ Line = 0
    return

label Girl_Dismissed(Girl=0, Leaving=0):
    $ Girl = GirlCheck(Girl)
    if Girl in Party:
        $ Party.remove(Girl)
    call Girls_Schedule ([Girl], 0)

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

        call Remove_Girl (Girl, 1, 1)
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

label Favorite_Actions(Chr=0, Quick=0, Temp=0, ATemp=0, PTemp=0, BTemp=0, TTemp=0, HTemp=0, FTemp=0, D20F=0, BOptions=0):




    if Chr:
        $ BOptions = [Chr]
    else:
        $ BOptions = active_Girls[:]


    while BOptions:
        $ Chr = BOptions[0]

        $ ATemp = Chr.action_counter["anal"] + Chr.action_counter["dildo_ass"] + Chr.action_counter["fondle_ass"] + Chr.action_counter["finger_ass"] + Chr.action_counter["eat_ass"]
        $ PTemp = Chr.action_counter["sex"] + Chr.action_counter["dildo_pussy"] + Chr.action_counter["fondle_pussy"] + Chr.action_counter["finger_pussy"] + Chr.action_counter["eat_pussy"]
        $ BTemp = Chr.action_counter["blowjob"]
        $ TTemp = Chr.action_counter["titjob"]
        $ XTemp = Chr.action_counter["footjob"]
        $ HTemp = Chr.action_counter["handjob"]
        $ FTemp = Chr.action_counter["fondle_breasts"]+ Chr.action_counter["fondle_thighs"]+ Chr.action_counter["suck_breasts"] + Chr.action_counter["hotdog"]


        if Chr.player_favorite_action and approval_check(Chr, 1500):
            if Chr.player_favorite_action == "anal":
                $ ATemp += 20
            elif Chr.player_favorite_action == "sex":
                $ PTemp += 20
            elif Chr.player_favorite_action == "blowjob":
                $ BTemp += 20
            elif Chr.player_favorite_action == "titjob":
                $ TTemp += 20
            elif Chr.player_favorite_action == "footjob":
                $ XTemp += 20
            elif Chr.player_favorite_action == "handjob":
                $ HTemp += 20
            else:
                $ FTemp += 20
        elif Chr.player_favorite_action and approval_check(Chr, 800):
            if Chr.player_favorite_action == "anal":
                $ ATemp += 5
            elif Chr.player_favorite_action == "sex":
                $ PTemp += 5
            elif Chr.player_favorite_action == "blowjob":
                $ BTemp += 5
            elif Chr.player_favorite_action == "titjob":
                $ TTemp += 5
            elif Chr.player_favorite_action == "footjob":
                $ XTemp += 5
            elif Chr.player_favorite_action == "handjob":
                $ HTemp += 5
            else:
                $ FTemp += 5


        $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + XTemp + FTemp + Chr.action_counter["kiss"]
        if Total <= 0:
            $ D20F = 999
        else:
            $ D20F = renpy.random.randint(1, Total)


        if D20F <= ATemp:

            if Chr.action_counter["anal"] >= 5:
                $ Temp = "anal"
            elif Chr.action_counter["eat_ass"] >= 5:
                $ Temp = "eat_ass"
            else:
                $ Temp = "finger_ass"
        elif D20F <= ATemp + PTemp:

            if Chr.action_counter["sex"] >= 5:
                $ Temp = "sex"
            elif Chr.action_counter["eat_pussy"] >= 5:
                $ Temp = "eat_pussy"
            else:
                $ Temp = "fondle_pussy"
        elif D20F <= ATemp + PTemp + BTemp:
            $ Temp = "blowjob"
        elif D20F <= ATemp + PTemp + BTemp + TTemp:
            $ Temp = "titjob"
        elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
            $ Temp = "footjob"
        elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
            $ Temp = "handjob"
        elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp + FTemp:

            $ D20F = renpy.random.randint(1, 20)
            if D20F >= 15 and Chr.action_counter["hotdog"]:
                $ Temp = "hotdog"
            elif D20F >= 10 and Chr.action_counter["suck_breasts"]:
                $ Temp = "suck_breasts"
            elif D20F >= 5 and Chr.action_counter["fondle_breasts"]:
                $ Temp = "fondle_breasts"
            else:
                $ Temp = "fondle_thighs"
        else:
            $ Temp = "kiss"

        if not Quick:
            $ Chr.favorite_action = Temp
        else:
            return Temp
        $ BOptions.remove(BOptions[0])
    return

label Gifts:

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)
    while True:
        if not Player.inventory:
            "You don't have anything to give her."
            return
        menu:
            "What would you like to give her?"
            "Toys and Books":
                menu:
                    "Give her a dildo." if "_dildo" in Player.inventory:

                        if "_dildo" not in Girl.inventory:
                            "You give [Girl.name] the dildo."
                            $ Girl.blushing = "_blush1"
                            $ Girl.ArmPose = 2
                            $ Girl.held_item = "_dildo"
                            if approval_check(Girl, 800):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove("_dildo")
                                $ Girl.inventory.append("_dildo")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 30)
                                if Girl == RogueX:
                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                elif Girl == LauraX:
                                    ch_l "Oh, cool, I've wanted one of these. . ."
                                else:
                                    Girl.voice "I'm sure I can find some place to store it. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 500):
                                $ Girl.change_face("_confused")
                                $ Player.inventory.remove("_dildo")
                                $ Girl.inventory.append("_dildo")
                                if Girl != EmmaX:
                                    $ Girl.change_stat("love", 200, 10)
                                    $ Girl.change_stat("obedience", 200, 10)
                                    $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == RogueX:
                                    ch_r "Huh, well I guess I can find a place for it. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")
                                    ch_r "I- I mean. . . I'll just put it away."
                                elif Girl == KittyX:
                                    ch_k "I don't know what. . ."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")
                                    ch_k "Oh!"
                                    ch_k "Oh. . . I'll just[Girl.like]put it away."
                                elif Girl == EmmaX:
                                    ch_e "This is not an appropriate gift from a student. . ."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sadside",1)
                                    ch_e "Hm. . ."
                                    $ Girl.change_stat("love", 200, 10)
                                    $ Girl.change_stat("obedience", 200, 10)
                                    $ Girl.change_stat("inhibition", 200, 10)
                                    $ Girl.change_face("_sly")
                                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh, you're a weird gift giver."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_smile")
                                    ch_l "It's very thoughtful though."
                                elif Girl == JeanX:
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    ch_j "Well we know where your mind it at."
                                    $ Girl.change_face("_smile")
                                    ch_j "I guess I should be flattered. . ."
                                elif Girl == StormX:
                                    if StormX not in Rules:
                                        $ Girl.change_face("_sadside",1)
                                        ch_s "I don't know that I should accept this from a student. . ."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    ch_s "Hm. . ."
                                    $ Girl.change_face("_sly")
                                    ch_s "Thank you for the thought. . ."
                                elif Girl == JubesX:
                                    ch_v "I guess I have some use for it. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")
                                    ch_v "I- I mean. . . decorative."
                                $ Girl.change_face("_bemused")
                            elif "offered gift" in Girl.daily_history:
                                $ Girl.change_face("_angry")
                                "She hands it back to you."
                                if Girl == RogueX:
                                    ch_r "Look, maybe you should just rethink your gift-giving choices?"
                                elif Girl == KittyX:
                                    ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                                elif Girl == EmmaX:
                                    ch_e "I think I have made myself clear about inappropriate gifts?"
                                elif Girl == LauraX:
                                    ch_l "I said I can't take something like this."
                                elif Girl == JeanX:
                                    ch_j "I really don't need this."
                                elif Girl == StormX:
                                    ch_s "I repeat, this is not something I need."
                                elif Girl == JubesX:
                                    ch_v "This really isn't something I need. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)
                                if Girl == RogueX:
                                    ch_r "That's a pretty forward gift to be giving a lady. . ."
                                elif Girl == KittyX:
                                    ch_k "I- you shouldn't be giving girls stuff like this!"
                                elif Girl == EmmaX:
                                    ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                                elif Girl == LauraX:
                                    ch_l "I don't think you should just be handing these out to random chicks."
                                elif Girl == JeanX:
                                    ch_j "So you just go around handing out sex toys?"
                                elif Girl == StormX:
                                    ch_s "I do not appreciate the implication here."
                                elif Girl == JubesX:
                                    ch_v "This is an odd design for a. . . wait."
                                $ Girl.change_stat("lust", 89, 5)
                                "She hands it back to you."
                                $ Girl.daily_history.append("offered gift")
                        elif Girl.inventory.count("_dildo") == 1:
                            $ Player.inventory.remove("_dildo")
                            $ Girl.inventory.append("_dildo")
                            if Girl == RogueX:
                                ch_r "Well, I suppose I could always use another. . ."
                            elif Girl == KittyX:
                                ch_k "Why stop with one. . ."
                            elif Girl == EmmaX:
                                ch_e "I suppose I always have room for one more. . ."
                            elif Girl == LauraX:
                                ch_l "I don't know if I need another. . ."
                            elif Girl == JeanX:
                                ch_j "Oh look, another rubber cock. . ."
                            elif Girl == StormX:
                                ch_s "Oh, another one. . ."
                            elif Girl == JubesX:
                                ch_v "I don't need more. . ."
                        else:
                            if Girl == RogueX:
                                ch_r "Honestly, [Girl.player_petname], I already have enough of those."
                            elif Girl == KittyX:
                                ch_k "I only have so many places to store these."
                            elif Girl == EmmaX:
                                ch_e "How many places do you think I could put these?"
                            elif Girl == LauraX:
                                ch_l "I'm running out of space at this point."
                            elif Girl == JeanX:
                                ch_j "How many holes do you think a girl has?"
                            elif Girl == StormX:
                                ch_s "I doubt I can find a place for this one."
                            elif Girl == JubesX:
                                ch_v "This is way too many. . ."
                        $ Girl.held_item = 0
                        $ Girl.ArmPose = 2

                    "Give her the vibrator." if "_vibrator" in Player.inventory:

                        if "_vibrator" not in Girl.inventory:
                            "You give [Girl.name] the Shocker Vibrator."
                            $ Girl.blushing = "_blush1"
                            $ Girl.ArmPose = 2
                            $ Girl.held_item = "_vibrator"
                            if approval_check(Girl, 700):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove("_vibrator")
                                $ Girl.inventory.append("_vibrator")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 30)
                                if Girl == RogueX:
                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                elif Girl == KittyX:
                                    ch_k "Well this is. . . [[bzzzt]- "
                                    ch_k "-interesting. . ."
                                elif Girl == EmmaX:
                                    ch_e "How very thoughtful of you. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sly")
                                    ch_e "I'm sure I can put this to good use. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sly")
                                    ch_l "-some kind of sex thing, huh. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, nifty."
                                elif Girl == StormX:
                                    ch_s "Oh!. . . oooohhh."
                                elif Girl == JubesX:
                                    ch_v "Oh, this could be nice. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 400):
                                $ Girl.change_face("_confused")
                                $ Player.inventory.remove("_vibrator")
                                $ Girl.inventory.append("_vibrator")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == RogueX:
                                    ch_r "I guess I can use this to work the kinks out. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")
                                    ch_r "Muscle knots, I mean!"
                                elif Girl == KittyX:
                                    ch_k "I've heard these are very relaxing. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_surprised")
                                    ch_k "-for my back!"
                                elif Girl == EmmaX:
                                    ch_e "How very thoughtful of you. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("_sly")
                                    ch_e "A back massager, I assume. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "
                                    $ Girl.change_face("_sly")
                                    $ Girl.change_stat("lust", 89, 10)
                                    ch_l "-oooh. . ."
                                elif Girl == JeanX:
                                    ch_j "Huh. Ok."
                                elif Girl == StormX:
                                    ch_s "Oh, something for exercise purposes. . ."
                                elif Girl == JubesX:
                                    ch_v "Thanks, my, uh, back's been killing me. . ."
                                $ Girl.change_face("_bemused", 1)
                            elif "offered gift" in Girl.daily_history:
                                $ Girl.change_face("_angry")
                                "She hands it back to you."
                                if Girl == RogueX:
                                    ch_r "Look, maybe you should just rethink your gift-giving choices?"
                                elif Girl == KittyX:
                                    ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"
                                elif Girl == EmmaX:
                                    ch_e "I think I have made myself clear about inappropriate gifts?"
                                elif Girl == LauraX:
                                    ch_l "I don't want it."
                                elif Girl == JeanX:
                                    ch_j "I really don't need this."
                                elif Girl == StormX:
                                    ch_s "I repeat, this is not something I need."
                                elif Girl == JubesX:
                                    ch_v "I don't need this. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)
                                if Girl == RogueX:
                                    ch_r "I don't think I have much use for that."
                                elif Girl == KittyX:
                                    ch_k "I can't really see the point."
                                elif Girl == EmmaX:
                                    ch_e "[Girl.player_petname], I don't believe this is an appropriate gift from a student."
                                elif Girl == LauraX:
                                    ch_l "I don't need it."
                                elif Girl == JeanX:
                                    ch_j "Huh. No, I don't need this."
                                elif Girl == StormX:
                                    ch_s "I have no use for this."
                                elif Girl == JubesX:
                                    ch_v "Put that away. . ."
                                $ Girl.change_stat("lust", 89, 5)
                                "She hands it back to you."
                                $ Girl.daily_history.append("offered gift")
                        else:
                            if Girl == RogueX:
                                ch_r "[Girl.player_petname], I only need the one."
                            elif Girl == EmmaX:
                                ch_e "I already have plenty."
                            else:
                                Girl.voice "I already have one of these."
                        $ Girl.held_item = 0
                        $ Girl.ArmPose = 2

                    "Give her a butt plug." if "buttplug" in Player.inventory:
                        if "buttplug" not in Girl.inventory:
                            "You give [Girl.name] the butt plug."
                            $ Player.inventory.remove("buttplug")
                            $ Girl.inventory.append("buttplug")
                        else:
                            "She already has enough of those."

                    "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in Player.inventory:

                        if "Dazzler and Longshot" not in Girl.inventory:
                            "You give [Girl.name] the book."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 600, "L"):
                                $ Girl.change_face("_smile")
                                if Girl == RogueX:
                                    ch_r "Oh, I've heard of this one, very romantic!"
                                elif Girl == KittyX:
                                    ch_k "Oh, this one's so sweet!"
                                elif Girl == EmmaX:
                                    $ Girl.change_face("_angry")
                                    ch_e "Is this the type of thing you expect from me. . ."
                                    $ Girl.change_face("_sadside", Mouth="_lipbite")
                                    ch_e "we'll have to see. . ."
                                elif Girl == LauraX:
                                    ch_l "A love story?"
                                elif Girl == JeanX:
                                    ch_j "Oh. . . a romance. . ."
                                elif Girl == StormX:
                                    ch_s "You have a taste for romances?"
                                elif Girl == JubesX:
                                    ch_v "You know, me and Dazzler have a lot in common. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("_confused")
                                if Girl == RogueX:
                                    ch_r "Hmph, well I guess i've heard good things about it, I'll give it a shot."
                                elif Girl == KittyX:
                                    ch_k "Hm, worth the read I guess."
                                elif Girl == EmmaX:
                                    $ Girl.change_face("_angry")
                                    ch_e "I don't exactly read this dime store trash. . ."
                                    $ Girl.change_face("_sadside", Mouth="_lipbite")
                                    ch_e "but I will take it. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh. Is there a movie?"
                                elif Girl == JeanX:
                                    ch_j "What are you implying?"
                                elif Girl == StormX:
                                    ch_s "I did enjoy the film. . ."
                                elif Girl == JubesX:
                                    ch_v "Are you saying I look like her?"
                                $ Girl.change_face("_bemused")
                            $ Player.inventory.remove("Dazzler and Longshot")
                            $ Girl.inventory.append("Dazzler and Longshot")
                            $ Girl.change_stat("love", 200, 50)
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."

                    "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in Player.inventory:

                        if "256 Shades of Grey" not in Girl.inventory:
                            "You give [Girl.name] the book."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 500, "O"):
                                $ Girl.change_face("_bemused")
                                if Girl == RogueX:
                                    ch_r "I'll research it thoroughly."
                                elif Girl == KittyX:
                                    ch_k "I'll give it a good look."
                                elif Girl == EmmaX:
                                    ch_e "I expect it might be somewhat entertaining."
                                elif Girl == LauraX:
                                    ch_l "Looks dirty."
                                elif Girl == JeanX:
                                    ch_j "Ha!"
                                    ch_j "Oh, man, what a weekend that was. . ."
                                    $ Girl.change_stat("love", 50, 5)
                                    $ Girl.change_stat("love", 90, 3)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    ch_j "Did you want to try some of this stuff?"
                                elif Girl == StormX:
                                    ch_s "Oh, you're serious about this?"
                                elif Girl == JubesX:
                                    ch_v "Kinky. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("_confused")
                                if Girl == RogueX:
                                    ch_r "Hmm, I have heard some good things about this one. I'll give it a quick read."
                                elif Girl == KittyX:
                                    ch_k "Hmm, I guess I could read a few chapters."
                                elif Girl == EmmaX:
                                    ch_e "I've heard of that one."
                                elif Girl == LauraX:
                                    ch_l "I'll give it a look."
                                elif Girl == JeanX:
                                    ch_j "Ha!"
                                    ch_j "Oh, man, what a weekend that was. . ."
                                    $ Girl.change_stat("love", 50, -5)
                                    $ Girl.change_stat("obedience", 200, 5)
                                    $ Girl.change_stat("inhibition", 200, -5)
                                    ch_j "Wait, did -you- read this?"
                                elif Girl == StormX:
                                    ch_s "I do think I need to speak to that girl. . ."
                                elif Girl == JubesX:
                                    ch_v "This is a little dark for me. . ."
                                $ Girl.change_face("_bemused")
                            $ Player.inventory.remove("256 Shades of Grey")
                            $ Girl.inventory.append("256 Shades of Grey")
                            $ Girl.change_stat("obedience", 200, 50,Alt=[[JeanX],200,10])
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."

                    "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in Player.inventory:

                        if "Avengers Tower Penthouse" not in Girl.inventory:
                            "You give [Girl.name] the book."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 500, "I"):
                                $ Girl.change_face("_bemused")
                                if Girl == RogueX:
                                    ch_r "Oh. . . I think I can work with this. . ."
                                elif Girl == KittyX:
                                    ch_k "This should be fun. . ."
                                elif Girl == EmmaX:
                                    ch_e "Perhaps don't visit unannounced. . ."
                                elif Girl == LauraX:
                                    ch_l "This is pretty hot. . ."
                                elif Girl == JeanX:
                                    ch_j "Hello Mr. Rogers. . ."
                                elif Girl == StormX:
                                    ch_s "Oh, this is. . . explicit. . ."
                                elif Girl == JubesX:
                                    ch_v "Wow, how did she. . . wow. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("_confused")
                                if Girl == RogueX:
                                    ch_r "Well. . . this is a bit. . . I think I'll keep this for research."
                                elif Girl == KittyX:
                                    ch_k "Well. . . this is a bit. . . I could maybe learn a few things."
                                elif Girl == EmmaX:
                                    ch_e "I normally confiscate such things. . . I'll just do that now. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh. . . ok."
                                elif Girl == JeanX:
                                    ch_j "Ooh, kinky stuff. . ."
                                elif Girl == StormX:
                                    ch_s "Oh. . . my. . ."
                                elif Girl == JubesX:
                                    ch_v "Um, this is kinda. . . a lot. . ."
                                $ Girl.change_face("_bemused")
                            $ Player.inventory.remove("Avengers Tower Penthouse")
                            $ Girl.inventory.append("Avengers Tower Penthouse")
                            $ Girl.change_stat("inhibition", 200, 50)
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."
                    "Never mind":

                        pass
            "Clothing":


                menu:
                    "Give her the green nighty." if Girl.tag + " nighty" in Player.inventory:

                        if "nighty" not in Girl.inventory:
                            "You give [Girl.name] the nighty."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 600):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " nighty")
                                $ Girl.inventory.append("nighty")
                                $ Girl.change_stat("love", 200, 40)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 30)
                                ch_r "I bet I'd look good in this. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("_confused")
                                $ Player.inventory.remove(Girl.tag + " nighty")
                                $ Girl.inventory.append("nighty")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)
                                ch_r "Well, it's a little revealing, but still pretty cute."
                                $ Girl.change_face("_bemused")
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the corset." if Girl.tag + " corset" in Player.inventory:

                        if "_corset" not in Girl.inventory:
                            "You give [Girl.name] the corset."
                            if approval_check(Girl, 1000):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " corset")
                                $ Girl.inventory.append("_corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == LauraX:
                                    ch_l "I'd look good in this, right?"
                                elif Girl == JeanX:
                                    ch_j "Ok, I can get into this one. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 700) or Girl == JeanX:
                                $ Girl.change_face("_confused",1)
                                $ Player.inventory.remove(Girl.tag + " corset")
                                $ Girl.inventory.append("_corset")
                                $ Girl.change_stat("love", 200, 15)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == LauraX:
                                    ch_l "This is. . . kinda cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Thanks?"
                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 600):
                                $ Girl.change_face("_confused",2)
                                $ Player.inventory.remove(Girl.tag + " corset")
                                $ Girl.inventory.append("_corset")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 15)
                                $ Girl.change_stat("inhibition", 200, 15)
                                if Girl == LauraX:
                                    ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)
                                if Girl == LauraX:
                                    ch_l "I just told you no."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -10)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)
                                if "no_gift_panties" in Girl.daily_history:
                                    if Girl == LauraX:
                                        ch_l "I don't want this either."
                                else:
                                    if Girl == LauraX:
                                        ch_l "You have too much time on your hands."
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.blushing = "_blush1"
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the lace corset." if Girl.tag + " lace corset" in Player.inventory:

                        if "lace corset" not in Girl.inventory:
                            "You give [Girl.name] the lace corset."
                            if approval_check(Girl, 1200):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " lace corset")
                                $ Girl.inventory.append("lace corset")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 20)
                                ch_l "You think this'd look good on me?"
                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 1000):
                                $ Girl.change_face("_confused",1)
                                $ Player.inventory.remove(Girl.tag + " lace corset")
                                $ Girl.inventory.append("lace corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 15)
                                ch_l "This is. . . kinda flimsy. . ."
                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 800):
                                $ Girl.change_face("_confused",2)
                                $ Player.inventory.remove(Girl.tag + " lace corset")
                                $ Girl.inventory.append("lace corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 25)
                                ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)
                                ch_l "I just told you no."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -10)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)
                                if "no_gift_panties" in Girl.daily_history:
                                    ch_l "I don't want this either."
                                else:
                                    ch_l "You have too much time on your hands."
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.blushing = "_blush1"
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the lace bra." if Girl.tag + " lace_bra" in Player.inventory:

                        if "lace_bra" not in Girl.inventory:
                            "You give [Girl.name] the lace bra."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 1000) or Girl == JeanX:
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " lace_bra")
                                $ Girl.inventory.append("lace_bra")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 30)
                                if Girl == RogueX:
                                    ch_r "Hmm, this really shows off the assets. . ."
                                elif Girl == KittyX:
                                    ch_k "At least you appreciate what I've got."
                                elif Girl == EmmaX:
                                    ch_e "I'm impressed, you got the size correct. . ."
                                elif Girl == JeanX:
                                    ch_j "Good tastes. . ."
                                elif Girl == StormX:
                                    ch_s "Do you think this would suit me?"
                                elif Girl == JubesX:
                                    ch_v "You like how this would look on me. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 700,Alt=[[EmmaX],600]):
                                $ Girl.change_face("_confused")
                                $ Player.inventory.remove(Girl.tag + " lace_bra")
                                $ Girl.inventory.append("lace_bra")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)
                                if Girl == RogueX:
                                    ch_r "I don't know that I'd wear this out, but maybe in private."
                                elif Girl == KittyX:
                                    ch_k "This is. . . see-through. . ."
                                    ch_k "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                elif Girl == EmmaX:
                                    if approval_check(Girl, 700):
                                        ch_e "I'm not exactly running low on this sort of thing. . ."
                                    else:
                                        ch_e "This is an . . . unusual gift from a student. . ."
                                elif Girl == StormX:
                                    ch_s "It is not that I do not appreciate it, but. . ."
                                elif Girl == JubesX:
                                    ch_v "It's not my usual style. . ."
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)
                                if Girl == RogueX:
                                    ch_r "You can't even give me 24 hours?!"
                                elif Girl == KittyX:
                                    ch_k "I haven't changed my mind, stop bothering me!"
                                elif Girl == EmmaX:
                                    ch_e "This still isn't an appropriate gift from a student."
                                elif Girl == StormX:
                                    ch_s "I still do not need this."
                                elif Girl == JubesX:
                                    ch_v "Seriously, this is a bit much. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)
                                if Girl == RogueX:
                                    if "no_gift_panties" in Girl.daily_history:
                                        ch_r "I don't want these neither!"
                                    else:
                                        ch_r "I don't know why you would focus on my rack, [Girl.player_petname]"
                                elif Girl == KittyX:
                                    if "no_gift_panties" in Girl.daily_history:
                                        ch_k "I don't want these either!"
                                    else:
                                        ch_k "You just- just don't be thinking about my breasts!"
                                elif Girl == EmmaX:
                                    if "no_gift_panties" in Girl.daily_history:
                                        ch_e "This isn't any better than the last."
                                    else:
                                        ch_e "I don't think it's appropriate for you to be so focused on my breasts."
                                elif Girl == StormX:
                                    ch_s "My current one is plenty."
                                elif Girl == JubesX:
                                    ch_v "I definitely don't want this. . ."
                                $ Girl.change_stat("lust", 89, 5)
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                            $ Girl.change_face("_bemused")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the lace panties." if Girl.tag + " lace_panties" in Player.inventory:

                        if "_lace_panties" not in Girl.inventory:
                            "You give [Girl.name] the lace panties."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 1100) or Girl == JeanX:
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " lace_panties")
                                $ Girl.inventory.append("_lace_panties")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 30)
                                if Girl == RogueX:
                                    ch_r "Hmm, these really put the goods on display. . ."
                                elif Girl == KittyX:
                                    ch_k "These don't leave much to the imagination. . ."
                                elif Girl == EmmaX:
                                    ch_e "Not entirely out of place in my wardrobe. . ."
                                elif Girl == LauraX:
                                    ch_l "These are pretty hot. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, these are nice. . ."
                                elif Girl == StormX:
                                    ch_s "So you think I would look good in these?"
                                elif Girl == JubesX:
                                    ch_v "You think I'd look good in frills?"
                                $ Girl.change_stat("lust", 89, 10)
                            elif approval_check(Girl, 800):
                                $ Girl.change_face("_confused")
                                $ Player.inventory.remove(Girl.tag + " lace_panties")
                                $ Girl.inventory.append("_lace_panties")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)
                                if Girl == RogueX:
                                    ch_r "These are a bit flimsy. . ."
                                elif Girl == KittyX:
                                    ch_k "I- I wouldn't wear something like these. . ."
                                    $ KittyX.change_face("_bemused",1)
                                    ch_k "But I'll hold on to them. . ."
                                elif Girl == EmmaX:
                                    ch_e "This is an. . . unsual gift."
                                    $ EmmaX.change_face("_sly",1)
                                    ch_e "But I'll hold on to them. . ."
                                elif Girl == LauraX:
                                    ch_l "I don't think I'd wear these. . ."
                                    $ Girl.change_face("_bemused",1)
                                    ch_l "But I might need to do laundry. . ."
                                elif Girl == StormX:
                                    ch_s "I suppose I could always use another pair. . ."
                                elif Girl == JubesX:
                                    ch_v "A little. . . intimate. . ."
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)
                                if Girl == RogueX:
                                    ch_r "Not today, [Girl.player_petname]!"
                                elif Girl == KittyX:
                                    ch_k "Look, my answer's still no, stop asking!"
                                elif Girl == EmmaX:
                                    ch_e "I don't recommend trying again any time soon."
                                elif Girl == LauraX:
                                    ch_l "My answer's still no, stop asking!"
                                elif Girl == StormX:
                                    ch_s "I truly am satisfied with my undergarments."
                                elif Girl == JubesX:
                                    ch_v "Seriously, cut it out. . ."
                            else:
                                $ Girl.change_face("_angry")
                                $ Girl.change_stat("love", 50, -20)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)
                                if Girl == RogueX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_r "I don't want these neither!"
                                    else:
                                        ch_r "I think I'll pick out my own unmentionables, thank you."
                                elif Girl == KittyX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_k "I don't want these either!"
                                    elif Girl.SeenPanties:
                                        ch_k "Just because you've seen my panties doesn't mean you get to pick them out."
                                    else:
                                        ch_k "Oh, don't you worry what I've got on down there."
                                elif Girl == EmmaX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_e "These aren't appropriate either."
                                    elif Girl.SeenPanties:
                                        ch_e "Just because you've seen my panties doesn't mean you get to pick them out."
                                    else:
                                        ch_e "I don't believe these are appropriate thoughts for you to be having."
                                elif Girl == LauraX:
                                    if "no_gift_bra" in Girl.daily_history:
                                        ch_l "I don't want these either!"
                                    elif Girl.SeenPanties:
                                        ch_l "Did you not like the ones I had?"
                                    else:
                                        ch_l "You don't need to worry about my underwear."
                                elif Girl == StormX:
                                    ch_s "I do have plenty of underwear, [Girl.player_petname]."
                                elif Girl == JubesX:
                                    ch_v "I'm a bit uncomfortable with this. . ."
                                $ Girl.change_stat("lust", 89, 5)
                                "She hands them back to you."
                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_panties")
                            $ Girl.change_face("_bemused")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the stockings and garterbelt." if "_stockings_and_garterbelt" in Player.inventory:

                        if "_stockings_and_garterbelt" not in Girl.inventory:
                            "You give [Girl.name] the stockings."
                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("_bemused")
                            $ Player.inventory.remove("_stockings_and_garterbelt")
                            $ Girl.inventory.append("_stockings_and_garterbelt")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)
                            if Girl == EmmaX:
                                ch_e "These are lovely. . ."
                            elif Girl == StormX:
                                ch_s "You think I could pull these off?"
                            else:
                                Girl.voice "These are pretty nice. . ."
                            $ Girl.change_stat("lust", 89, 5)
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the pantyhose." if Girl.tag + "_pantyhose" in Player.inventory:

                        if "pantyhose" not in Girl.inventory:
                            "You give [Girl.name] the pantyhose."
                            $ Girl.change_face("_bemused")
                            $ Player.inventory.remove(Girl.tag + "_pantyhose")
                            $ Girl.inventory.append("pantyhose")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)
                            Girl.voice "These are lovely. . ."
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the knee stockings." if "knee" in Player.inventory and Girl == KittyX:

                        if "knee" not in Girl.inventory:
                            "You give [Girl.name] the knee stockings."
                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("_bemused")
                            $ Player.inventory.remove("knee")
                            $ Girl.inventory.append("knee")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)
                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the high socks." if "socks" in Player.inventory and Girl == JubesX:

                        if "sock" not in Girl.inventory:
                            "You give [Girl.name] the high socks."
                            $ Girl.blushing = "_blush1"
                            $ Girl.change_face("_bemused")
                            $ Player.inventory.remove("sock")
                            $ Girl.inventory.append("sock")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)
                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the bikini top." if Girl.tag + " bikini_top" in Player.inventory:

                        if "_bikini_top" not in Girl.inventory:
                            "You give [Girl.name] the bikini top."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 1200):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " bikini_top")
                                $ Girl.inventory.append("_bikini_top")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == RogueX:
                                    ch_r "This is a nice color. . ."
                                elif Girl == KittyX:
                                    ch_k "This is pretty cute. . ."
                                elif Girl == EmmaX:
                                    ch_e "This does show off my assets, doesn't it. . ."
                                elif Girl == LauraX:
                                    ch_l "\"X\", cute. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, very nice style. . ."
                                elif Girl == StormX:
                                    ch_s "Oh! I think that I recognize this one."
                                elif Girl == JubesX:
                                    ch_v "Ooo, so Cal. . ."
                            elif approval_check(Girl, 900) or Girl == JeanX:
                                $ Girl.change_face("_confused",1)
                                $ Player.inventory.remove(Girl.tag + " bikini_top")
                                $ Girl.inventory.append("_bikini_top")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)
                                if Girl == RogueX:
                                    ch_r "A little skimpy. . ."
                                elif Girl == KittyX:
                                    ch_k "Kinda visible, maybe. . ."
                                elif Girl == EmmaX:
                                    ch_e "This is my style. . ."
                                elif Girl == LauraX:
                                    ch_l "Ok, cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Yeah, this'll work. . ."
                                elif Girl == StormX:
                                    ch_s "I think I can recognize the design. . ."
                                elif Girl == JubesX:
                                    ch_v "Not a bad choice. . ."
                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 700):
                                $ Girl.change_face("_confused",2)
                                $ Player.inventory.remove(Girl.tag + " bikini_top")
                                $ Girl.inventory.append("_bikini_top")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 5)
                                $ Girl.change_stat("inhibition", 200, 5)
                                if Girl == RogueX:
                                    ch_r "I was thinking about a tan. . ."
                                elif Girl == KittyX:
                                    ch_k "Aw, a cute Kitty. . . hole. . ."
                                elif Girl == EmmaX:
                                    ch_e "An interesting. . . gift. . ."
                                elif Girl == LauraX:
                                    ch_l "I could use one of these. . ."
                                elif Girl == StormX:
                                    ch_s "I suppose that I could use a new suit."
                                elif Girl == JubesX:
                                    ch_v "I guess that works for me. . ."
                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)
                                if Girl == RogueX:
                                    ch_r "My answer's still no, stop asking!"
                                elif Girl == KittyX:
                                    ch_k "Look, my answer's still no, stop asking!"
                                elif Girl == EmmaX:
                                    ch_e "I don't recommend trying again any time soon."
                                elif Girl == LauraX:
                                    ch_l "My answer's still no, stop asking!"
                                elif Girl == StormX:
                                    ch_s "I do not need fashion advice, thank you."
                                elif Girl == JubesX:
                                    ch_v "This really doesn't work for me. . ."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -5)
                                $ Girl.change_stat("obedience", 20, 5)
                                $ Girl.change_stat("inhibition", 20, 10)
                                if "no_gift_panties" in Girl.daily_history:
                                    Girl.voice "I don't want these either!"
                                else:
                                    if Girl == RogueX:
                                        ch_r "Don't you worry what I've got on there."
                                    elif Girl == KittyX:
                                        ch_k "Oh, don't you worry what I've got on there."
                                    elif Girl == EmmaX:
                                        ch_e "I don't think my swimwear is any concern of yours."
                                    elif Girl == LauraX:
                                        ch_l "Don't worry about what I wear."
                                    elif Girl == StormX:
                                        ch_s "No, thank you."
                                    elif Girl == JubesX:
                                        ch_v "Nah, I don't think it works for me. . ."
                                $ Girl.blushing = "_blush1"
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                            if "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"
                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "_blue_skirt" in Girl.inventory:
                                        $ Girl.Swim[0] = 1
                                else:
                                    $ Girl.Swim[0] = 1
                        else:
                            Girl.voice "I already have one of those."



                    "Give her the bikini bottoms." if Girl.tag + " bikini_bottoms" in Player.inventory:

                        if "_bikini_bottoms" not in Girl.inventory:
                            "You give [Girl.name] the bikini bottoms."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 1200):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " bikini_bottoms")
                                $ Girl.inventory.append("_bikini_bottoms")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == RogueX:
                                    ch_r "These are pretty nice. . ."
                                elif Girl == KittyX:
                                    ch_k "These are pretty cute. . ."
                                elif Girl == EmmaX:
                                    ch_e "These are quite stylish. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh, nice cut. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, sexy style. . ."
                                elif Girl == StormX:
                                    ch_s "Lovely, but where have I seen this cut before. . ."
                                elif Girl == JubesX:
                                    ch_v "Wow, super sexy. . ."
                            elif approval_check(Girl, 900) or Girl == JeanX:
                                $ Girl.change_face("_confused",1)
                                $ Player.inventory.remove(Girl.tag + " bikini_bottoms")
                                $ Girl.inventory.append("_bikini_bottoms")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)
                                if Girl == RogueX:
                                    ch_r "Kinda tiny, aren't they. . ."
                                elif Girl == KittyX:
                                    ch_k "A little snug, maybe. . ."
                                elif Girl == EmmaX:
                                    ch_e "Rather daring. . ."
                                elif Girl == LauraX:
                                    ch_l "Ok, cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Ooo, these are nice. . ."
                                elif Girl == StormX:
                                    ch_s "Where have I seen this cut before. . ."
                                elif Girl == JubesX:
                                    ch_v "Maybe a little small. . ."
                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 700):
                                $ Girl.change_face("_confused",2)
                                $ Player.inventory.remove(Girl.tag + " bikini_bottoms")
                                $ Girl.inventory.append("_bikini_bottoms")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 5)
                                $ Girl.change_stat("inhibition", 200, 5)
                                if Girl == RogueX:
                                    ch_r "I was thinking about a tan. . ."
                                elif Girl == KittyX:
                                    ch_k "Well, it is bikini weather. . ."
                                elif Girl == EmmaX:
                                    ch_e "I don't know that a student should be buying me swimwear. . ."
                                elif Girl == LauraX:
                                    ch_l "Weird gift, but is it warm out. . ."
                                elif Girl == StormX:
                                    ch_s "What an unusual design."
                                elif Girl == JubesX:
                                    ch_v "I'm not sure I can wear these. . ."
                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)
                                if Girl == RogueX:
                                    ch_r "My answer's still no, stop asking!"
                                elif Girl == KittyX:
                                    ch_k "Look, my answer's still no, stop asking!"
                                elif Girl == EmmaX:
                                    ch_e "I don't recommend trying again any time soon."
                                elif Girl == LauraX:
                                    ch_l "My answer's still no, stop asking!"
                                elif Girl == StormX:
                                    ch_s "Again, no."
                                elif Girl == JubesX:
                                    ch_v "Definitely not."
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -5)
                                $ Girl.change_stat("obedience", 20, 5)
                                $ Girl.change_stat("inhibition", 20, 10)
                                if "no_gift_bra" in Girl.daily_history:
                                    Girl.voice "I don't want these either!"
                                else:
                                    if Girl == RogueX:
                                        ch_r "Don't you worry what I've got on down there."
                                    elif Girl == KittyX:
                                        ch_k "Oh, don't you worry what I've got on down there."
                                    elif Girl == EmmaX:
                                        ch_e "I don't think my swimwear is any concern of yours."
                                    elif Girl == LauraX:
                                        ch_l "Don't worry about what I wear."
                                    elif Girl == StormX:
                                        ch_s "No, thank you."
                                    elif Girl == JubesX:
                                        ch_v "Oh no. . ."
                                $ Girl.blushing = "_blush1"
                                "She hands them back to you."
                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_panties")
                            if "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"
                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "_blue_skirt" in Girl.inventory:
                                        $ Girl.Swim[0] = 1
                                else:
                                    $ Girl.Swim[0] = 1
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the blue skirt." if Girl.tag + " blue_skirt" in Player.inventory:

                        if "_blue_skirt" not in Girl.inventory:
                            "You give [Girl.name] the blue skirt."
                            $ Girl.blushing = "_blush1"
                            if approval_check(Girl, 1000):
                                $ Girl.change_face("_bemused")
                                $ Player.inventory.remove(Girl.tag + " blue_skirt")
                                $ Girl.inventory.append("_blue_skirt")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                ch_k "This is a cute skirt. . ."
                            elif approval_check(Girl, 800):
                                $ Girl.change_face("_confused",1)
                                $ Player.inventory.remove(Girl.tag + " blue_skirt")
                                $ Girl.inventory.append("_blue_skirt")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)
                                ch_k "This is kinda daring. . ."
                                $ Girl.change_face("_bemused",1)
                            elif approval_check(Girl, 600):
                                $ Girl.change_face("_confused",2)
                                $ Player.inventory.remove(Girl.tag + " blue_skirt")
                                $ Girl.inventory.append("_blue_skirt")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 5)
                                $ Girl.change_stat("inhibition", 200, 5)
                                ch_k "It'd go well with a swimsuit. . ."
                                $ Girl.change_face("_bemused",1)
                            elif "no_gift_skirt" in Girl.recent_history:
                                $ Girl.change_face("_angry",2)
                                ch_k "I just don't want that."
                            elif "no_gift_skirt" in Girl.daily_history:
                                $ Girl.change_face("_angry",2)
                                ch_k "Look, my answer's still no, stop asking!"
                            else:
                                $ Girl.change_face("_angry",2)
                                $ Girl.change_stat("love", 50, -5)
                                $ Girl.change_stat("obedience", 20, 5)
                                $ Girl.change_stat("inhibition", 20, 10)
                                ch_k "Oh, don't you worry what I'm wearing."
                                $ Girl.blushing = "_blush1"
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_skirt")
                                $ Girl.daily_history.append("no_gift_skirt")
                            if Girl == KittyX and "_bikini_top" in Girl.inventory and "_bikini_bottoms" in Girl.inventory:
                                $ Girl.Swim[0] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Never mind":


                        pass
            "Wardrobe":


                ch_p "I wanted to talk about your style."
                call Taboo_Level
                $ Line = "Giftstore"
                call expression Girl.tag + "_Clothes"
            "Switch to. . .":

                call Switch_Chat
                ch_p "I'd like to give you something."
                if Girl.location != bg_current:
                    Girl.voice "I don't see how, if I'm not there."
                    return
                jump Gifts
            "Exit":
                return
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
                    call Taboo_Level
                    call expression Girl.tag + "_Clothes"

            "Shift her Personality" if approval_check(Girl, 900, "L", TabM=0) or approval_check(Girl, 900, "O", TabM=0)or approval_check(Girl, 900, "I", TabM=0):
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
                $ Line = 0
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
                        $ Line = "free"

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
                        $ Line = "ask"

                    "Don't ever leave when I'm around." if "lockedtravels" not in Girl.traits or "freetravels" in Girl.traits:
                        if approval_check(Girl, 500, "O",Alt=[[EmmaX,JeanX],600]) or approval_check(Girl, 900, "L"):
                            $ Girl.change_face("_sexy")
                            if Girl == RogueX:
                                ch_r "Oh, Ok."
                            elif Girl == KittyX:
                                ch_k "Aw, you miss me when I'm not around!"
                            elif Girl == EmmaX:
                                $ Girl.change_face("_angry", Eyes="_side")
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
                            $ Line = "lock"
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

                if Line:
                    $ Girl.daily_history.append("follow")
                    if "freetravels" in Girl.traits:
                        $ Girl.traits.remove("freetravels")
                    if "asktravels" in Girl.traits:
                        $ Girl.traits.remove("asktravels")
                    if "lockedtravels" in Girl.traits:
                        $ Girl.traits.remove("lockedtravels")

                    if Line == "free":
                        $ Girl.traits.append("freetravels")
                    elif Line == "ask":
                        $ Girl.traits.append("asktravels")
                    elif Line == "lock":
                        $ Girl.traits.append("lockedtravels")
                    $ Line = 0

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
                call Switch_Chat
            "Never mind.":

                return
