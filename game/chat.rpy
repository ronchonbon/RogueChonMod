
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

                if not ApprovalCheck(Girl, 1700) and not ApprovalCheck(Girl, 600,"O"):
                    $ Options = all_Girls[:]
                    while Options:
                        if Options[0] in Player.daily_history and "saw with " + Options[0].Tag not in Girl.Traits and Girl.GirlLikeCheck(Options[0]) <= 700:
                            $ Girl.Traits.append("saw with " + Options[0].Tag)
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

            if "angry" not in Girl.recent_history:
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

                if "angry" not in Girl.recent_history:
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

    if "angry" in Girl.recent_history:
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
                call expression Girl.Tag + "_Summon"
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
                    if "angry" in Girl.recent_history:
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
                    elif ApprovalCheck(Girl, 600, "LI"):
                        $ Girl.change_face("sexy")
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
                        shift_focus(Girl)
                        jump enter_main_sex_menu
                        return
                    elif ApprovalCheck(Girl, 400, "OI"):
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
                        shift_focus(Girl)
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
                    call expression Girl.Tag + "_SexChat"

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
                    call expression Girl.Tag + "_Chitchat"
                "Relationship status":
                    ch_p "Could we talk about us?"
                    if Girl.location == bg_current:
                        call expression Girl.Tag + "_Relationship"
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
                            call expression Girl.Tag + "_About" pass (RogueX)
                        "How do you feel about [KittyX.name]?" if Girl != KittyX and "met" in KittyX.history:
                            call expression Girl.Tag + "_About" pass (KittyX)
                        "How do you feel about [EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.history:
                            call expression Girl.Tag + "_About" pass (EmmaX)
                        "How do you feel about [LauraX.name]?" if Girl != LauraX and "met" in LauraX.history:
                            call expression Girl.Tag + "_About" pass (LauraX)
                        "How do you feel about [JeanX.name]?" if Girl != JeanX and "met" in JeanX.history:
                            call expression Girl.Tag + "_About" pass (JeanX)
                        "How do you feel about [StormX.name]?" if Girl != StormX and "met" in StormX.history:
                            call expression Girl.Tag + "_About" pass (StormX)
                        "How do you feel about [JubesX.name]?" if Girl != JubesX and "met" in JubesX.history:
                            call expression Girl.Tag + "_About" pass (JubesX)
                        "About hooking up with other girls. . .":
                            call expression Girl.Tag + "_Monogamy"
                        "Never mind.":
                            pass

                "Could I get your number?" if Girl not in Digits:
                    if Girl == EmmaX and ApprovalCheck(Girl, 800, "LI"):
                        ch_e "I don't see why not."
                        $ Digits.append(Girl)
                    elif Girl != EmmaX and (ApprovalCheck(Girl, 400, "L") or ApprovalCheck(Girl, 200, "I")):
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
                    elif ApprovalCheck(Girl, 200, "O",Alt=[[EmmaX],500-EmmaX.inhibition]):
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
            if Girl == EmmaX and ApprovalCheck(Girl, 1250):
                $ Party.append(Girl)
                ch_e "Lead away."
                return
            if ApprovalCheck(Girl, 600,Alt=[[EmmaX,JeanX],900]):
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
            elif not ApprovalCheck(Girl, 400):
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
                    $ Options[0].DrainWord("leaving")
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
    if "angry" not in Girl.recent_history and Girl != Line:
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
        $ Girl.DrainWord("leaving")
    menu:
        "You can leave if you like.":
            if Girl.location == bg_current and not ApprovalCheck(Girl, 700, "O"):
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

            if Girl.location == bg_current and not ApprovalCheck(Girl, 800, "LO"):
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
            elif not ApprovalCheck(Girl, 500, "LO"):
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

            if Girl.location == bg_current and not ApprovalCheck(Girl, 500, "O"):
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
            elif not ApprovalCheck(Girl, 300, "O"):
                $ Girl.change_face("confused")
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
                if Girl.location != bg_current and (ApprovalCheck(Girl, 1200, "LO") or ApprovalCheck(Girl, 500, "O")):

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
                elif Girl.location != bg_current and (ApprovalCheck(Girl, 1000, "LO") or ApprovalCheck(Girl, 300, "O")):

                    if "dismissed" not in Girl.daily_history:
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("love", 70, -5, 1)
                        $ Girl.change_stat("obedience", 50, 10)
                        $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_face("angry")
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
                    $ Girl.change_face("angry")
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
                elif ApprovalCheck(Girl, 1400, "LO") or ApprovalCheck(Girl, 400, "O"):

                    if "dismissed" not in Girl.daily_history:
                        $ Girl.change_stat("love", 50, -5, 1)
                        $ Girl.change_stat("obedience", 50, 10)
                        $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_face("sad")
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
                    $ Girl.change_face("sad")
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




label Flirt(Girl=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if Girl.location != bg_current:

        menu:
            "Compliment her":
                $ Girl.Chat[5] = 1
                call Compliment (Girl)


            "Phone Sex" if bg_current == "bg_player":
                ch_p "Want to do some phone sex?"
                call Taboo_Level (0)
                if not ApprovalCheck(Girl, 900) or Girl.SEXP < 15:

                    $ Girl.change_stat("love", 70, -2)
                    $ Girl.change_stat("love", 90, -2)
                    $ Girl.change_stat("obedience", 60, 2)
                    $ Girl.change_stat("inhibition", 40, 2)
                    if Girl == RogueX:
                        ch_r "You have -got- to be kid'n me. . ."
                    elif Girl == KittyX:
                        ch_k "Are you[Girl.like]serious?!"
                    elif Girl == EmmaX:
                        ch_e "That would be extremely inappropriate."
                    elif Girl == LauraX:
                        ch_l "What? No."
                    elif Girl == JeanX:
                        ch_j "Pretty sketch."
                    elif Girl == StormX:
                        ch_s "Definitely not."
                    elif Girl == JubesX:
                        ch_v "Def not. . ."
                    return
                if Girl.Taboo and ApprovalCheck(Girl, 1400):

                    if Girl == RogueX:
                        ch_r "Hmm. . . that sounds like fun. . ."
                        ch_r "I need to head home real quick. . ."
                    elif Girl == KittyX:
                        ch_k "Heh, you looking for a show? . ."
                        ch_k "Let me get back to my room. . ."
                    elif Girl == EmmaX:
                        ch_e "I think we could arrange that. . ."
                        ch_e "Give me a moment. . ."
                    elif Girl == LauraX:
                        ch_l "Yeah, I could do that, gimme a sec. . ."
                        ch_l "I need to head back to my room though. . ."
                    elif Girl == JeanX:
                        ch_j "Huh, I guess?"
                        ch_j "Gimme a minute to set up. . ."
                    elif Girl == StormX:
                        ch_s "That could be fun, give me one moment. . ."
                    elif Girl == JubesX:
                        ch_v "Oh. . . that might be fun. . ."
                        ch_v "Let me just find a place. . ."
                    if Girl in (EmmaX,StormX) and Girl.location == "bg_classroom" and time_index >= 2:
                        pass
                    else:
                        $ Girl.location = Girl.home
                elif ApprovalCheck(Girl, 1200):

                    if Girl == RogueX:
                        ch_r "Hmm. . . that sounds like fun. . ."
                    elif Girl == KittyX:
                        ch_k "Heh, you looking for a show? . ."
                    elif Girl == EmmaX:
                        ch_e "I think we could arrange that. . ."
                    elif Girl == LauraX:
                        ch_l "Yeah, I could do that, gimme a sec. . ."
                    elif Girl == JeanX:
                        ch_j "Yeah, sure. . ."
                    elif Girl == StormX:
                        ch_s "Sure, one moment. . ."
                    elif Girl == JubesX:
                        ch_v "Oh, sexy. . . sure, on sec. . ."
                elif Girl.Taboo:

                    if Girl == RogueX:
                        ch_r "I'm not home right now, so I can't."
                    elif Girl == KittyX:
                        ch_k "Heh, sorry, I'm out at right now."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid I'm a bit occupied at the moment. . ."
                    elif Girl == LauraX:
                        ch_l "I'm a little exposed here, right now, maybe later. . ."
                    elif Girl == JeanX:
                        ch_j "It's kinda public here, you know. . ."
                    elif Girl == StormX:
                        ch_s "I'm afraid it's a bit public here. . ."
                    elif Girl == JubesX:
                        ch_v "I'm kinda tied up here. . ."
                    return
                else:

                    if Girl == RogueX:
                        ch_r "I, um, I don't know about that. . ."
                    elif Girl == KittyX:
                        ch_k "Heh, heh, um, I don't think I could. . ."
                    elif Girl == EmmaX:
                        ch_e "I'd rather avoid putting on a show like that. . ."
                    elif Girl == LauraX:
                        ch_l "Nah, had enough of surveillance . . ."
                    elif Girl == JeanX:
                        ch_j "Rather not."
                    elif Girl == StormX:
                        ch_s "I don't think so."
                    elif Girl == JubesX:
                        ch_v "Nah, not into it. . ."
                    return
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("inhibition", 80, 2)
                call Taboo_Level (0)
                call PhoneSex (Girl)
                call Taboo_Level (0)
                $ renpy.pop_call()
                return
            "Phone Sex [[not here] (locked)" if bg_current != "bg_player":
                pass
            "Never mind [[exit]":
                pass
    else:

        $ Girl.Chat[5] = 1
        menu:
            "Compliment her":
                call Compliment (Girl)
            "Say you love her":

                call Love_You (Girl)
            "Touch her cheek":

                call TouchCheek (Girl)
            "Hold hands":

                call Hold_Hands (Girl)
            "Pat her head":

                call Girl_Headpat (Girl)
            "Kiss her cheek":

                "You lean over, brush her hair aside and kiss her on the cheek."
                if ApprovalCheck(Girl, 650, "L", TabM=1):
                    $ Girl.change_face("sexy", 1)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 40, 2)
                    if Girl == RogueX:
                        ch_r "That was real sweet, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k ". . ."
                        ch_k "Wow. Hey."
                    elif Girl == EmmaX:
                        ch_e ". . ."
                        ch_e "Hello. . ."
                    elif Girl == LauraX:
                        ch_l ". . ."
                        $ Girl.change_face("sexy", 1, Eyes="side")
                        ch_l "Huh."
                    elif Girl == JeanX:
                        ch_j "Huh."
                    elif Girl == StormX:
                        ch_s "Oh, hello there. . ."
                    elif Girl == JubesX:
                        ch_v "Oh, hey. . ."
                elif ApprovalCheck(Girl, 500, "L", TabM=1):
                    $ Girl.change_face("surprised", 1)
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("obedience", 40, 2)
                    $ Girl.change_stat("inhibition", 20, 1)
                    if Girl == RogueX:
                        ch_r "What was that for, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k ". . . hey! What's the deal?"
                    elif Girl == EmmaX:
                        ch_e ". . . to what do I owe the pleasure?"
                    elif Girl == LauraX:
                        ch_l ". . . hey!"
                        ch_l "What's that about?"
                    elif Girl == JeanX:
                        ch_j "Um. . ."
                    elif Girl == StormX:
                        ch_s "Oh?"
                    elif Girl == JubesX:
                        ch_v "Oh, hey. . ."
                elif ApprovalCheck(Girl, 300, "L", TabM=1):
                    $ Girl.change_face("angry", 1)
                    $ Girl.change_stat("love", 90, -1,Alt=[[JeanX],500,2])
                    $ Girl.change_stat("obedience", 60, 2)
                    $ Girl.change_stat("inhibition", 40, 1)
                    if Girl == RogueX:
                        ch_r "Hey, keep your distance, [Girl.player_petname]!"
                    elif Girl == KittyX:
                        ch_k "I don't[Girl.like]like you like that?"
                    elif Girl == EmmaX:
                        ch_e "That's highly inappropriate, [Girl.player_petname]"
                        ch_e "[[mumbles] -in public, at least. . ."
                    elif Girl == LauraX:
                        ch_l "That's a bit forward."
                    elif Girl == JeanX:
                        $ Girl.brows = "confused"
                        ch_j "Hey, what's that about?"
                    elif Girl == StormX:
                        ch_s "That's quite inappropriate. . ."
                    elif Girl == JubesX:
                        ch_v "What was that? . ."
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.change_stat("love", 90, -5,Alt=[[JeanX],500,2])
                    $ Girl.change_stat("obedience", 90, 5)
                    $ Girl.change_stat("inhibition", 40, 3)
                    if Girl == RogueX:
                        ch_r "Hey, back off!"
                    elif Girl == KittyX:
                        ch_k "Keep off me!"
                    elif Girl == EmmaX:
                        ch_e "Stop that at once."
                    elif Girl == LauraX:
                        ch_l "Keep back!"
                    elif Girl == JeanX:
                        $ Girl.eyes = "psychic"
                        ch_j "Back!"
                        $ Girl.eyes = "sexy"
                    elif Girl == StormX:
                        $ Girl.eyes = "white"
                        ch_s "What are you doing?!"
                        $ Girl.eyes = "sexy"
                    elif Girl == JubesX:
                        ch_v "Hey!"
                $ Girl.addiction -= 1
                $ Girl.addiction_rate += 1
                $ Girl.addiction_rate = 3 if Girl.addiction_rate < 3 else Girl.addiction_rate
            "Kiss her lips":

                if ApprovalCheck(Girl, 1000, TabM=2,Alt=[[RogueX],800]) or ApprovalCheck(Girl, 600, "L", TabM=2):
                    $ Line = renpy.random.choice(["You lean over, put your hand against her cheek, and plant a kiss on her lips.",
                                                                    "You lean down, tilt her head back, and plant a kiss on her lips.",
                                                                    "You turn "+Girl.name+" around and plant a deep kiss on her."])
                    "[Line]"
                elif ApprovalCheck(Girl, 1000,Alt=[[RogueX],800]) or ApprovalCheck(Girl, 600, "L"):
                    $ Girl.change_face("bemused", 1)
                    $ Girl.eyes = "side"
                    $ Girl.change_stat("obedience", 50, -1,Alt=[[JeanX],500,2])
                    $ Girl.change_stat("inhibition", 40, 2)
                    if Girl == RogueX:
                        "You lean close for a kiss, but [Girl.name] plants a hand on your face and pushes you back."
                        ch_r "Isn't this a bit public, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_k "Not in public, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        "You lean close for a kiss, but [Girl.name] plants a hand on your face and pushes you back."
                        ch_e "Not in public, [Girl.player_petname]."
                    elif Girl == LauraX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_l "Not here, [Girl.player_petname]."
                    elif Girl == JeanX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_j "Um, not here, [Girl.player_petname]."
                    elif Girl == StormX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_s "Not in public, [Girl.player_petname]."
                    elif Girl == JubesX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_v "No, not in public. . ."
                    return
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.change_stat("love", 90, -5,Alt=[[JeanX],500,2])
                    $ Girl.change_stat("obedience", 50, -1,Alt=[[JeanX],500,1])
                    $ Girl.change_stat("inhibition", 40, 5)
                    if Girl == RogueX:
                        "You lean close for a kiss, but [Girl.name] plants a hand on your face and pushes you back."
                        ch_r "What the hell, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_k "Keep your distance, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        "You lean close for a kiss, but [Girl.name] plants a hand on your face and pushes you back."
                        ch_e "No."
                    elif Girl == LauraX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_l "Keep to yourself, [Girl.player_petname]."
                    elif Girl == JeanX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_j "Back it up, [Girl.player_petname]."
                    elif Girl == StormX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_s "Oh, no thank you, [Girl.player_petname]"
                    elif Girl == JubesX:
                        "You lean close for a kiss, but [Girl.name] gently elbows your ribs."
                        ch_v "Oh, um, no thanks. . ."
                    return
                if Girl.action_counter["kiss"]:

                    if ApprovalCheck(Girl, 750, "L", TabM=1):
                        $ Girl.change_face("sexy", 1)
                        $ Girl.change_stat("love", 90, 2)
                        $ Girl.change_stat("obedience", 50, 2)
                        if Girl == RogueX:
                            ch_r "Hmm we should do that again, [Girl.player_petname]."
                        else:
                            Girl.voice "Mmmmmmm. . ."
                    elif ApprovalCheck(Girl, 650, "L", TabM=1):
                        $ Girl.change_face("sexy", 1)
                        $ Girl.change_stat("love", 90, 2)
                        $ Girl.change_stat("obedience", 50, 2)
                        if Girl == RogueX:
                            ch_r "Hmm, that was a nice surprise, [Girl.player_petname]?"
                        elif Girl == KittyX:
                            ch_k "Hmm, \"hello\" to you too, [Girl.player_petname]?"
                        elif Girl == EmmaX:
                            ch_e "Hmm, hello [Girl.player_petname]. . ."
                        elif Girl == LauraX:
                            ch_l "Hmm, that's nice. . ."
                        elif Girl == JeanX:
                            ch_j "Hmm. . ."
                        elif Girl == StormX:
                            ch_s "Hmm. . ."
                        elif Girl == JubesX:
                            ch_v "Mmmmm. . ."
                    elif ApprovalCheck(Girl, 500, "L", TabM=1):
                        $ Girl.change_face("surprised", 1)
                        $ Girl.change_stat("love", 70, 3)
                        $ Girl.change_stat("obedience", 50, 2)
                        if Girl == RogueX:
                            ch_r "Hey, what do you think you're doing, [Girl.player_petname]?"
                        elif Girl == KittyX:
                            ch_k "That's[Girl.like]a bit forward?"
                        elif Girl == EmmaX:
                            ch_e "You're incorrigible."
                        elif Girl == LauraX:
                            ch_l "I don't know about that."
                        elif Girl == JeanX:
                            ch_j "Hey!"
                        elif Girl == StormX:
                            ch_s "Hey. . ."
                        elif Girl == JubesX:
                            ch_v "Hey, that's not cool. . ."
                    elif ApprovalCheck(Girl, 300, "L", TabM=1):
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -3,Alt=[[JeanX],500,-1])
                        $ Girl.change_stat("obedience", 60, 3)
                        $ Girl.change_stat("inhibition", 40, 2)
                        if Girl == RogueX:
                            ch_r "That really wasn't appropriate, [Girl.player_petname]!"
                        elif Girl == KittyX:
                            ch_k "Dude!"
                        elif Girl == EmmaX:
                            ch_e "Highly inappropriate!"
                            $ Girl.change_face("bemused", Eyes="side")
                            ch_e "-at least while in public. . ."
                        elif Girl == LauraX:
                            ch_l "Back it off, [Girl.player_petname]."
                        elif Girl == JeanX:
                            ch_j "Back off!"
                        elif Girl == StormX:
                            ch_s "Keep your distance."
                        elif Girl == JubesX:
                            ch_v "Back off."
                    else:
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -8,Alt=[[JeanX],500,-3])
                        $ Girl.change_stat("obedience", 90, 6)
                        $ Girl.change_stat("inhibition", 40, 3)
                        if Girl == RogueX:
                            ch_r "Not cool, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Back off, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "Down boy."
                        elif Girl == LauraX:
                            ch_l "Fuck off."
                        elif Girl == JeanX:
                            ch_j "Hey!"
                        elif Girl == StormX:
                            ch_s "[Player.name]!"
                        elif Girl == JubesX:
                            ch_v "Nope."
                else:

                    if ApprovalCheck(Girl, 750, "L", TabM=1):
                        $ Girl.change_face("surprised", 1)
                        $ Girl.change_stat("love", 70, 45)
                        $ Girl.change_stat("obedience", 50, 20)
                        $ Girl.change_stat("inhibition", 50, 35)
                        if Girl == RogueX:
                            ch_r "Hmmm, that was a pleasant suprise. . ."
                            $ Girl.change_face("sexy")
                            ch_r "Maybe we should do that again, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k ". . ."
                            ch_k "Hmmm, that was nice. . ."
                            $ Girl.change_face("sexy")
                            ch_k "Let me know if you want to do that again, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e ". . ."
                            ch_e "Hmmm, that was a pleasant surprise. . ."
                            $ Girl.change_face("sexy")
                            ch_e "I could always use some more, [Girl.player_petname]."
                        elif Girl == LauraX:
                            $ Girl.change_face("normal",Eyes="side")
                            ch_l ". . ."
                            $ Girl.change_face("sexy",Eyes="side")
                            ch_l "Hmmm, that was nice. . ."
                            $ Girl.change_face("sexy")
                        elif Girl == JeanX:
                            ch_j "Oh. . ."
                        elif Girl == StormX:
                            ch_s ". . ."
                            ch_s "Hmmm, what was that, [Girl.player_petname]. . ."
                            $ Girl.change_face("sexy")
                            ch_s "I could do that again. . ."
                        elif Girl == JubesX:
                            ch_v "Mmmmm. . ."
                            ch_v "Oh, wait. . . what was that about?"
                    elif ApprovalCheck(Girl, 650, "L", TabM=1):
                        $ Girl.change_face("surprised", 1)
                        $ Girl.change_stat("love", 80, 30)
                        $ Girl.change_stat("obedience", 50, 25)
                        $ Girl.change_stat("inhibition", 50, 35)
                        if Girl == RogueX:
                            ch_r "Wha, what was that, [Girl.player_petname]?"
                            ch_r "Hmm, not that it was entirely unpleasant. . ."
                        elif Girl == KittyX:
                            ch_k "Huh?"
                            ch_k "I, um[Girl.like]don't know what to do with that. . ."
                        elif Girl == EmmaX:
                            ch_e "Hmm?"
                            ch_e "So we're there now, are we? . ."
                        elif Girl == LauraX:
                            ch_l " ! "
                            ch_l "I'm not sure what to do with that. . ."
                        elif Girl == JeanX:
                            ch_j "Huh."
                        elif Girl == StormX:
                            ch_s "Oh!"
                        elif Girl == JubesX:
                            ch_v "Mmmmm. . .wait, what?"
                            ch_v "What was that for?"
                    elif ApprovalCheck(Girl, 500, "L", TabM=1):
                        $ Girl.change_face("surprised", 1)
                        $ Girl.change_stat("obedience", 70, 30)
                        $ Girl.change_stat("inhibition", 70, 35)
                        if Girl == RogueX:
                            ch_r "Hey, what do you think you're doing, [Girl.player_petname]?"
                        elif Girl == KittyX:
                            ch_k "What's the deal, [Girl.player_petname]?!"
                        elif Girl == EmmaX:
                            ch_e "I don't think that's really appropriate, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "What are you thinking, [Girl.player_petname]?!"
                        elif Girl == JeanX:
                            ch_j "What was that? . ."
                        elif Girl == StormX:
                            ch_s "That isn't appropriate."
                        elif Girl == JubesX:
                            ch_v "That was. . . give a girl some warning. . ."
                    elif ApprovalCheck(Girl, 700, TabM=1):
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 60, -5,Alt=[[JeanX],500,-2])
                        $ Girl.change_stat("obedience", 70, 40)
                        $ Girl.change_stat("inhibition", 70, 40)
                        if Girl == RogueX:
                            ch_r "Wha, what the hell was that about?!"
                        elif Girl == KittyX:
                            ch_k "the hell, [Girl.player_petname]?!"
                        elif Girl == EmmaX:
                            ch_e "We can't be seen doing that, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "What the hell, [Girl.player_petname]?!"
                        elif Girl == JeanX:
                            ch_j "Hey!"
                        elif Girl == StormX:
                            ch_s "[Player.name]!"
                        elif Girl == JubesX:
                            ch_v "Hey!"
                    else:
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 60, -15,Alt=[[JeanX],500,-5])
                        $ Girl.change_stat("obedience", 70, 50)
                        $ Girl.change_stat("inhibition", 70, 40)
                        if Girl == RogueX:
                            ch_r "Not cool, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "[Girl.Like]WTF?!"
                        elif Girl == EmmaX:
                            ch_e "How dare you?"
                        elif Girl == LauraX:
                            ch_l "Fuck off."
                        elif Girl == JeanX:
                            ch_j "What the hell was that?!"
                        elif Girl == StormX:
                            ch_s "Keep your distance!"
                        elif Girl == JubesX:
                            ch_v "Back off, creep!"

                $ Girl.action_counter["kiss"] += 1
                $ Girl.addiction -= 1
                $ Girl.addiction_rate += 1
                $ Girl.addiction_rate = 3 if Girl.addiction_rate < 3 else Girl.addiction_rate

                if Girl.Taboo and Girl == EmmaX:
                    if "three" not in EmmaX.history:
                        if not AloneCheck(EmmaX):

                            call Emma_ThreeCheck



                if ApprovalCheck(Girl, 650, TabM=1):
                    if Girl.love > Girl.obedience and Girl.love > Girl.inhibition:
                        if Girl == RogueX:
                            ch_r "Gimme some more sugar, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "More smooches, [Girl.player_petname]!"
                        elif Girl == EmmaX:
                            ch_e "I hope there's more where that came from. . ."
                        elif Girl == LauraX:
                            ch_l "I think I'd like some more."
                        elif Girl == JeanX:
                            ch_j "You're kinda sweet. . ."
                        elif Girl == StormX:
                            ch_s "Your lips are sweet, my [Girl.player_petname]."
                        elif Girl == JubesX:
                            ch_v "Well I could use another taste. . ."
                    elif Girl.obedience > Girl.inhibition:
                        if Girl == RogueX:
                            ch_r "Did you want to follow up on that?"
                        elif Girl == KittyX:
                            ch_k "I'd be open to more if you are."
                        elif Girl == EmmaX:
                            ch_e "I wouldn't mind some more of that. . ."
                        elif Girl == LauraX:
                            ch_l "Did you want to continue?"
                        elif Girl == JeanX:
                            ch_j "Did you want something more?"
                        elif Girl == StormX:
                            ch_s "Was that all you wanted?"
                        elif Girl == JubesX:
                            ch_v "Did you want some more? . ."
                    else:
                        if Girl == RogueX:
                            ch_r "You'd best have a follow-up to that, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "We could keep going, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "Get over here. . ."
                        elif Girl == LauraX:
                            ch_l "We could keep going, [Girl.player_petname]."
                        elif Girl == JeanX:
                            ch_j "Well that was fun. . ."
                        elif Girl == StormX:
                            ch_s "Hey. . ."
                        elif Girl == JubesX:
                            ch_v "Well? . ."
                    menu:
                        "Keep kissing?"
                        "You know it.":
                            $ Girl.change_stat("lust", 60, 3)
                            $ Girl.change_stat("love", 90, 1)
                            $ Girl.change_stat("love", 60, 3)
                            $ Girl.change_stat("inhibition", 50, 2)
                            if bg_current == "HW Party":
                                "She shrugs away from you and winks."
                                Girl.voice "Not now. . ."
                            else:
                                call expression Girl.Tag + "_SexAct" pass ("kissing")
                                call Trig_Reset (1)
                            return
                        "Just a taste [[no].":
                            $ Girl.change_face("bemused", 1)
                            $ Girl.change_stat("lust", 40, 1)
                            $ Girl.change_stat("lust", 60, 4)
                            $ Girl.change_stat("obedience", 70, 2)
                            $ Girl.change_stat("inhibition", 50, 2)
                            if Girl == RogueX:
                                ch_r "At some point I'm gonna need the whole mouthful, [Girl.player_petname]."
                            elif Girl == KittyX:
                                ch_k "Oh, way to[Girl.like]tease a girl!"
                            elif Girl == EmmaX:
                                ch_e "Tease. . ."
                            elif Girl == LauraX:
                                ch_l "Ah, you were kidding."
                            elif Girl == JeanX:
                                ch_j "Oh, ok. . ."
                            elif Girl == StormX:
                                ch_s "You tease me."
                            elif Girl == JubesX:
                                ch_v "Oh, you'll pay for that one later. . ."
                        "Nope.":
                            $ Girl.change_face("angry", 1)
                            $ Girl.change_stat("love", 80, -2)
                            $ Girl.change_stat("obedience", 70, 3)
                            $ Girl.change_stat("inhibition", 50, 1)
                            if Girl == RogueX:
                                ch_r "You're writing checks you can't cash, [Girl.player_petname]."
                            elif Girl == KittyX:
                                ch_k "Don't string me along here, [Girl.player_petname]."
                            elif Girl == EmmaX:
                                ch_e "I don't appreciate games, [Girl.player_petname]."
                            elif Girl == LauraX:
                                ch_l "Ah, you were kidding."
                            elif Girl == JeanX:
                                ch_j "Ooookay. . ."
                            elif Girl == StormX:
                                ch_s "Do not play with my heart."
                            elif Girl == JubesX:
                                ch_v "Aw. . ."
                else:
                    if Girl == RogueX:
                        ch_r "Don't just plant one on a girl without ask'in first."
                    elif Girl == KittyX:
                        ch_k "Well[Girl.like]don't do it again."
                    elif Girl == EmmaX:
                        ch_e "Don't try that again."
                    elif Girl == LauraX:
                        ch_l "Don't push me."
                    elif Girl == JeanX:
                        ch_j "Keep it to yourself."
                    elif Girl == StormX:
                        ch_s "Do not do that again."
                    elif Girl == JubesX:
                        ch_v "Well, you should definitely warn me first. . ."
            "Hug her":


                if ApprovalCheck(Girl, 200, TabM=1):
                    "You lean over and wrap [Girl.name] in a warm hug."
                else:
                    $ Girl.change_face("angry", 1)
                    "You lean in with your arms wide, but [Girl.name] grabs your shoulders and shoves you back."
                    if Girl == RogueX:
                        ch_r "Hey, what're you doing, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "What's the deal, [Girl.player_petname]?"
                    elif Girl == EmmaX:
                        ch_e "What exactly is that about, [Girl.player_petname]?"
                    elif Girl == LauraX:
                        ch_l "What's was that, [Girl.player_petname]?"
                    elif Girl == JeanX:
                        ch_j "Hey, back it up."
                    elif Girl == StormX:
                        ch_s "Take a step back."
                    elif Girl == JubesX:
                        ch_v "Hey, back off. . ."
                    return
                if Girl.SEXP >= 30:
                    $ Girl.change_stat("lust", 60, 3)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 90, 3)
                    $ Girl.change_stat("inhibition", 90, 3)
                    $ Girl.change_face("sexy")
                    if Girl == RogueX:
                        ch_r "Hmm, are you hinting at something there, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "You're warming me up, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "Hmmm, what did you have in mind, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "I think you're flipping my switch, [Girl.player_petname]."
                    elif Girl == JeanX:
                        ch_j "What, are you thinking sexy time?"
                    elif Girl == StormX:
                        ch_s "Hmm, what did you have in mind?"
                    elif Girl == JubesX:
                        ch_v "Oh, what was that for. . ."
                elif ApprovalCheck(Girl, 600, "L", TabM=1):
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 40, 2)
                    $ Girl.change_stat("inhibition", 30, 1)
                    if Girl == RogueX:
                        ch_r "Hmm, nice to see you too, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Hmm, warm huggies."
                    elif Girl == EmmaX:
                        ch_e "Hmm, I do enjoy this. . ."
                    elif Girl == LauraX:
                        ch_l "Hmmmmm. . ."
                    elif Girl == JeanX:
                        ch_j "Um, geeze!"
                    elif Girl == StormX:
                        ch_s "Hmmm."
                    elif Girl == JubesX:
                        ch_v "Oh, hey. . ."
                elif ApprovalCheck(Girl, 450, TabM=1,Alt=[[JeanX],500]):
                    $ Girl.change_face("surprised", 1)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("obedience", 40, 2)
                    $ Girl.change_stat("inhibition", 30, 1)
                    if Girl == RogueX:
                        ch_r "Hey, [Girl.player_petname]. What's up?"
                    elif Girl == KittyX:
                        ch_k "Hey[Girl.like]what is this about?"
                    elif Girl == EmmaX:
                        ch_e "Hm? What was it you wanted?"
                    elif Girl == LauraX:
                        ch_l "Um, [Girl.player_petname]? What is this?"
                    elif Girl == JeanX:
                        ch_j "Um, what are you doing?"
                    elif Girl == StormX:
                        ch_s "Oh, hello there."
                    elif Girl == JubesX:
                        ch_v "Hello. . ."
                elif ApprovalCheck(Girl, 350, TabM=1,Alt=[[JeanX],400]):
                    $ Girl.change_face("angry", 1)
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("obedience", 50, 3)
                    $ Girl.change_stat("inhibition", 30, 2)
                    if Girl == RogueX:
                        ch_r "I don't really know you that well."
                    elif Girl == KittyX:
                        ch_k "I'm not comfortable with this. . ."
                    elif Girl == EmmaX:
                        ch_e "We can't be seen like this. . ."
                    elif Girl == LauraX:
                        ch_l "This is making me uncomfortable. . ."
                    elif Girl == JeanX:
                        ch_j "This. . . is weird."
                    elif Girl == StormX:
                        ch_s "Um, you can release me now."
                    elif Girl == JubesX:
                        ch_v "Ok, that's good for now. . ."
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.change_stat("love", 10, -1)
                    $ Girl.change_stat("love", 40, -1)
                    $ Girl.change_stat("obedience", 20, 2)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 30, 2)
                    if Girl == RogueX:
                        ch_r "Had enough, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "What was that about, [Girl.player_petname]?"
                    elif Girl == EmmaX:
                        ch_e "What was that about, [Girl.player_petname]?"
                    elif Girl == LauraX:
                        ch_l "Hey, back off."
                    elif Girl == JeanX:
                        ch_j "What's your deal?"
                    elif Girl == StormX:
                        ch_s "What was that?"
                    elif Girl == JubesX:
                        ch_v "Well, you should definitely warn me first. . ."
            "Slap her ass":


                call Slap_Ass (Girl)
            "Pinch her ass":

                $ Girl.change_face("surprised", 1)
                if Girl.SEXP < 5 or not ApprovalCheck(Girl, 600, TabM=1):
                    "You come up to [Girl.name] from behind and quickly pinch her butt."
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 90, -4)
                    $ Girl.change_stat("love", 60, -4)
                    "She slaps your hand away and rounds on you."
                    if Girl == RogueX:
                        ch_r "Hey, what're you doing, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Hey! Bad touch!"
                    elif Girl == EmmaX:
                        ch_e "Down boy!"
                    elif Girl == LauraX:
                        ch_l "What are you thinking?"
                    elif Girl == JeanX:
                        ch_j "Hey!"
                    elif Girl == StormX:
                        ch_s "Excuse me!"
                    elif Girl == JubesX:
                        ch_v "Ow, hey!"
                    return
                if Girl.SEXP >= 30:
                    $ Girl.change_stat("lust", 60, 3)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 60, 2)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("inhibition", 50, 3)
                    $ Girl.change_face("sexy")
                    if Girl == RogueX:
                        ch_r "Ooh! Are you hinting at something there, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Purrrr, Kitty like."
                    elif Girl == EmmaX:
                        ch_e "Mmm, what was that for?"
                    elif Girl == LauraX:
                        ch_l "Oooh! Getting rough?"
                    elif Girl == JeanX:
                        ch_j "Oo!"
                    elif Girl == StormX:
                        ch_s "Oh!"
                    elif Girl == JubesX:
                        ch_v "Ooo!"
                elif ApprovalCheck(Girl, 800, "L", TabM=1):
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 60, 2)
                    $ Girl.change_stat("obedience", 90, 1)
                    $ Girl.change_stat("inhibition", 50, 2)
                    if Girl == RogueX:
                        ch_r "Hmm, nice to see you too, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Hmm, you know it, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "Oooh!"
                    elif Girl == LauraX:
                        ch_l "You like the way that feels, [Girl.player_petname]?"
                    elif Girl == JeanX:
                        ch_j "Oh, um, hey."
                    elif Girl == StormX:
                        ch_s "Hello. . ."
                    elif Girl == JubesX:
                        ch_v "Ooo. . . hey there. . ."
                elif ApprovalCheck(Girl, 900, TabM=1):
                    $ Girl.change_face("surprised")
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 60, 3)
                    $ Girl.change_stat("obedience", 90, 2)
                    $ Girl.change_stat("inhibition", 50, 2)
                    if Girl == RogueX:
                        ch_r "Ooh! What's up?"
                    elif Girl == KittyX:
                        ch_k "Ooh! Hey!"
                    elif Girl == EmmaX:
                        ch_e "Mmm, watch it."
                    elif Girl == LauraX:
                        ch_l "Wha?!"
                    elif Girl == JeanX:
                        ch_j "What's the deal?"
                    elif Girl == StormX:
                        ch_s "What was that?"
                    elif Girl == JubesX:
                        ch_v "What're you up to?"
                elif ApprovalCheck(Girl, 800, TabM=1):
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 60, -3)
                    $ Girl.change_stat("love", 90, -1)
                    $ Girl.change_stat("obedience", 60, 4)
                    $ Girl.change_stat("obedience", 90, 3)
                    $ Girl.change_stat("inhibition", 50, 2)
                    if Girl == RogueX:
                        ch_r "Hey, not cool."
                    elif Girl == KittyX:
                        ch_k "Dude!"
                    elif Girl == EmmaX:
                        ch_e "That is not something you can do in public."
                    elif Girl == LauraX:
                        ch_l "Hey!"
                    elif Girl == JeanX:
                        ch_j "What's your damage?"
                    elif Girl == StormX:
                        ch_s "Keep your distance."
                    elif Girl == JubesX:
                        ch_v "Back it up."
                else:
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 60, -3)
                    $ Girl.change_stat("love", 90, -3)
                    $ Girl.change_stat("obedience", 60, 5)
                    $ Girl.change_stat("obedience", 90, 4)
                    $ Girl.change_stat("inhibition", 50, 3)
                    if Girl == RogueX:
                        ch_r "Ow! Lay off."
                    elif Girl == KittyX:
                        ch_k "Ow! That hurt!"
                    elif Girl == EmmaX:
                        ch_e "Would you like me to break those fingers?"
                    elif Girl == LauraX:
                        ch_l "Ouch! What the fuck?!"
                    elif Girl == JeanX:
                        ch_j "What the fuck?"
                    elif Girl == StormX:
                        ch_s "[Player.name]!"
                    elif Girl == JubesX:
                        ch_v "Fuck off!"


            "Flip her skirt up" if Girl.PantsNum() == 5 and not Girl.Upskirt:
                $ Girl.change_face("surprised", 1)
                $ Girl.Upskirt = 1
                pause 0.5
                $ Girl.Upskirt = 0
                "You sneak up on [Girl.name] from behind and flip her skirt up quickly!"
                $ Girl.Upskirt = 0
                if Girl.underwear and not Girl.Taboo:

                    if ApprovalCheck(Girl, 750, "L", TabM=2):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "Oh, naughty, [Girl.player_petname]!"
                            ch_r "You could have just asked, you know. . ."
                        elif Girl == KittyX:
                            ch_k "Cute!"
                            ch_k "You couldn't[Girl.like]ask? . ."
                        elif Girl == EmmaX:
                            ch_e "Cheeky. . ."
                            ch_e "You could have asked for a look."
                        elif Girl == LauraX:
                            ch_l "Hey!"
                            ch_l "You wanted to see my underwear?"
                        elif Girl == JeanX:
                            ch_j "You could have asked."
                        elif Girl == StormX:
                            ch_s "Cheeky monkey."
                        elif Girl == JubesX:
                            ch_v "Heh, hey there!"
                        $ Girl.change_stat("love", 90, 3)
                    elif ApprovalCheck(Girl, 650, "L", TabM=2):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "Naughty naughty, [Girl.player_petname]!"
                        elif Girl == KittyX:
                            ch_k "Real cute, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "Cheeky."
                        elif Girl == LauraX:
                            ch_l "What's the deal, [Girl.player_petname]?"
                        elif Girl == JeanX:
                            ch_j "What?"
                        elif Girl == StormX:
                            ch_s "Cheeky monkey."
                        elif Girl == JubesX:
                            ch_v "Heh, hey there!"
                    elif ApprovalCheck(Girl, 300, "I", TabM=1):
                        $ Girl.change_face("sexy", 1)
                        if Girl == KittyX:
                            ch_k "What's the deal?"
                        else:
                            Girl.voice "Hey, what do you think you're doing, [Girl.player_petname]?"
                    elif ApprovalCheck(Girl, 300, TabM=1) or Girl == LauraX:
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -3)
                        $ Girl.change_stat("obedience", 80, 1)
                        if Girl == EmmaX:
                            ch_e "Totally inappropriate, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "Huh?"
                        elif Girl == StormX:
                            ch_s "Inappropriate behavior."
                        else:
                            Girl.voice "Not cool, [Girl.player_petname]."
                    else:
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -5)
                        $ Girl.change_stat("obedience", 80, 2)
                        if Girl == RogueX:
                            ch_r "What the fuck, [Girl.player_petname]!"
                            ch_r "That is not how you treat a lady!"
                        elif Girl == KittyX:
                            ch_k "What the fuck?"
                        elif Girl == EmmaX:
                            ch_e "Completely inappropriate!"
                            ch_e "I may have to consider your future at this school."
                        elif Girl == LauraX:
                            ch_l "HEY!"
                        elif Girl == JeanX:
                            ch_j "What the hell?!"
                        elif Girl == StormX:
                            ch_s "[Player.name]!"
                        elif Girl == JubesX:
                            ch_v "-the hell?"
                    $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_stat("inhibition", 30, 2)
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.SeenPanties = 1


                elif Girl.underwear:

                    if ApprovalCheck(Girl, 750, "L") and ApprovalCheck(Girl, 1300, TabM=2):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "Oh, naughty, [Girl.player_petname]!"
                            ch_r "You could have just asked, you know. . ."
                        elif Girl == KittyX:
                            ch_k "Cute!"
                            ch_e "You couldn't[Girl.like]ask? . ."
                        elif Girl == EmmaX:
                            ch_e "Cheeky. . ."
                            ch_e "You could have asked for a look."
                        elif Girl == LauraX:
                            ch_l "Hey!"
                            ch_l "You wanted to see my underwear?"
                        elif Girl == JeanX:
                            ch_j "You could have asked."
                        elif Girl == StormX:
                            ch_s "Cheeky monkey."
                        elif Girl == JubesX:
                            ch_v "Heh, hey there!"
                        $ Girl.change_stat("love", 90, 3)
                    elif ApprovalCheck(Girl, 600, "L") and ApprovalCheck(Girl, 1200, TabM=2):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname]! A little warning!"
                        elif Girl == KittyX:
                            ch_k "[Girl.player_petname]! A head's up wouldn't hurt."
                        elif Girl == EmmaX:
                            ch_e "[Girl.player_petname]!"
                            ch_e "Oh don't give me that look."
                        elif Girl == LauraX:
                            ch_l "Hey, it's kinda public for that."
                        elif Girl == JeanX:
                            ch_j "You could have asked."
                        elif Girl == StormX:
                            ch_s "Cheeky monkey."
                        elif Girl == JubesX:
                            ch_v "Heh, maybe not here!"
                    elif ApprovalCheck(Girl, 600, "L"):
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -3)
                        $ Girl.change_stat("obedience", 80, 3)
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname]! This isn't the time or place for this!"
                        elif Girl == KittyX:
                            ch_k "[Girl.player_petname]! Not in public!"
                        elif Girl == EmmaX:
                            ch_e "[Girl.player_petname]! I do have a reputation to maintain."
                        elif Girl == LauraX:
                            ch_l "Hey, chill it."
                        elif Girl == JeanX:
                            ch_j "Cut that out."
                        elif Girl == StormX:
                            ch_s "What are you doing?"
                        elif Girl == JubesX:
                            ch_v "-the hell?"
                    elif ApprovalCheck(Girl, 800, TabM=2):
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -5)
                        $ Girl.change_stat("obedience", 80, 2)
                        if Girl == EmmaX:
                            ch_e "Are you out of your mind, [Girl.player_petname]?"
                        elif Girl == LauraX:
                            ch_l "Hey!"
                        elif Girl == StormX:
                            ch_s "What was that?"
                        else:
                            Girl.voice "Wha! [Girl.player_petname]!"
                    else:
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -10)
                        $ Girl.change_stat("obedience", 80, 2)
                        $ Girl.change_stat("inhibition", 80, 1)
                        if Girl == EmmaX:
                            ch_e "Are you out of your mind, [Girl.player_petname]?"
                        elif Girl == LauraX:
                            ch_l "Dude!"
                        elif Girl == StormX:
                            ch_s ". . ."
                        else:
                            Girl.voice "What the fuck, [Girl.player_petname]!"
                        Girl.voice "Why would you even do that in public?"
                    $ Girl.change_stat("obedience", 80, 7)
                    $ Girl.change_stat("inhibition", 30, 3)
                    $ Girl.change_stat("inhibition", 80, 3)
                    $ Girl.SeenPanties = 1


                elif not Girl.Taboo:

                    if ApprovalCheck(Girl, 850, "L"):
                        if Girl == RogueX:
                            ch_r "Oh, naughty, [Girl.player_petname]!"
                            ch_r "You could have just asked, you know. . ."
                        elif Girl == KittyX:
                            ch_k "Cute!"
                            ch_e "You couldn't[Girl.like]ask? . ."
                        elif Girl == EmmaX:
                            ch_e "Cheeky. . ."
                            ch_e "You could have asked for a look."
                        elif Girl == LauraX:
                            ch_l "Hey!"
                            ch_l "Like what you see?"
                        elif Girl == JeanX:
                            ch_j "Caught me."
                        elif Girl == StormX:
                            ch_s "Cheeky monkey."
                        elif Girl == JubesX:
                            ch_v "Heh, hey there!"
                    elif ApprovalCheck(Girl, 700, "L"):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname]! A little warning!"
                        elif Girl == KittyX:
                            ch_k "[Girl.player_petname]! A head's up wouldn't hurt."
                        elif Girl == EmmaX:
                            ch_e "[Girl.player_petname]!"
                            ch_e "Oh don't give me that look."
                        elif Girl == LauraX:
                            ch_l "Hey, what's up?"
                        elif Girl == JeanX:
                            ch_j "Caught me."
                        elif Girl == StormX:
                            ch_s "Cheeky monkey."
                        elif Girl == JubesX:
                            ch_v "Heh, hey there!"
                    elif ApprovalCheck(Girl, 600, "L"):
                        $ Girl.change_face("bemused", 1)
                        $ Girl.change_stat("love", 90, -3)
                        $ Girl.change_stat("obedience", 80, 3)
                        if Girl == RogueX:
                            ch_r "Wha?! [Girl.player_petname]? . . I don't usually. . ."
                        elif Girl == KittyX:
                            ch_k "Wha?! [Girl.player_petname]? . ."
                            ch_k "It's not like I usually. . ."
                        elif Girl == EmmaX:
                            ch_e "Wha?! [Girl.player_petname]?"
                            ch_e "You were expecting something else?"
                        elif Girl == LauraX:
                            ch_l "Wha?! [Girl.player_petname]?"
                        elif Girl == JeanX:
                            ch_j "Hey!"
                        elif Girl == StormX:
                            ch_s "Surprised?"
                        elif Girl == JubesX:
                            ch_v "Um, surprised?"
                    elif ApprovalCheck(Girl, 500):
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -5)
                        $ Girl.change_stat("obedience", 80, 2)
                        if Girl == EmmaX:
                            ch_e "Are you out of your mind, [Girl.player_petname]?"
                        elif Girl == LauraX:
                            ch_l "Hey!"
                        elif Girl == StormX:
                            ch_s ". . ."
                        else:
                            Girl.voice "Wha! [Girl.player_petname]!"
                    else:
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -10)
                        $ Girl.change_stat("obedience", 80, 2)
                        $ Girl.change_stat("inhibition", 80, 1)
                        if Girl == EmmaX:
                            ch_e "Are you out of your mind, [Girl.player_petname]?"
                            ch_e "Even if I had been wearing panties. . ."
                        elif Girl == LauraX:
                            ch_l "Dude!"
                        elif Girl == JeanX:
                            ch_j "Hey! Privacy much?"
                        elif Girl == StormX:
                            ch_s "That really isn't appropriate."
                        else:
                            Girl.voice "What the fuck, [Girl.player_petname]!"
                            Girl.voice "I- I don't usually, you know. . ."
                    $ Girl.change_stat("obedience", 80, 7)
                    $ Girl.change_stat("inhibition", 30, 3)
                    $ Girl.change_stat("inhibition", 80, 4)
                    call expression Girl.Tag + "_First_Bottomless"
                else:



                    if ApprovalCheck(Girl, 850, "L") and ApprovalCheck(Girl, 1500):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "Oh, naughty, [Girl.player_petname]!"
                            ch_r "You could have just asked, you know. . ."
                        elif Girl == KittyX:
                            ch_k "Cute!"
                            ch_e "You couldn't[Girl.like]ask? . ."
                        elif Girl == EmmaX:
                            ch_e "Cheeky. . ."
                            ch_e "You could have asked for a look."
                        elif Girl == LauraX:
                            ch_l "Hey!"
                            ch_l "Like what you see?"
                        elif Girl == JeanX:
                            ch_j "Caught me."
                        elif Girl == StormX:
                            ch_s "Cheeky monkey."
                        elif Girl == JubesX:
                            ch_v "Heh, hey there!"
                    elif ApprovalCheck(Girl, 700, "L") and ApprovalCheck(Girl, 1500):
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname]! A little warning!"
                        elif Girl == KittyX:
                            ch_k "[Girl.player_petname]! A head's up wouldn't hurt."
                        elif Girl == EmmaX:
                            ch_e "[Girl.player_petname]!"
                            ch_e "Oh don't give me that look."
                        elif Girl == LauraX:
                            ch_l "Hey, what's up?"
                        elif Girl == JeanX:
                            ch_j "Hey, um, not here, right?"
                        elif Girl == StormX:
                            ch_s "Best not in public."
                        elif Girl == JubesX:
                            ch_v "Heh, hey not there!"
                    elif ApprovalCheck(Girl, 700):
                        $ Girl.change_face("bemused", 1)
                        $ Girl.change_stat("love", 90, -3)
                        $ Girl.change_stat("obedience", 80, 3)
                        if Girl == RogueX:
                            ch_r "[Girl.player_petname]! This isn't the time or place for this!"
                        elif Girl == KittyX:
                            ch_k "[Girl.player_petname]! Not in public!"
                        elif Girl == EmmaX:
                            ch_e "[Girl.player_petname]! I do have a reputation to maintain."
                        elif Girl == LauraX:
                            ch_l "Hey, chill it."
                        elif Girl == JeanX:
                            ch_j "Hey! Um. . . not here, right?"
                        elif Girl == StormX:
                            ch_s "Best not in public."
                        elif Girl == JubesX:
                            ch_v "Probably not here?"
                    elif ApprovalCheck(Girl, 1000):
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -5)
                        $ Girl.change_stat("obedience", 80, 2)
                        if Girl == EmmaX:
                            ch_e "Are you out of your mind, [Girl.player_petname]?"
                        elif Girl == LauraX:
                            ch_l "Hey!"
                        elif Girl == JeanX:
                            ch_j "Hey! I'd rather not. . . here."
                        elif Girl == StormX:
                            ch_s "Not here."
                        else:
                            Girl.voice "Wha! [Girl.player_petname]!"
                    else:
                        $ Girl.change_face("angry", 1)
                        $ Girl.change_stat("love", 90, -10)
                        $ Girl.change_stat("obedience", 80, 2)
                        $ Girl.change_stat("inhibition", 80, 1)
                        if Girl == EmmaX:
                            ch_e "Are you out of your mind, [Girl.player_petname]?"
                            ch_e "Even if I had been wearing panties. . ."
                        elif Girl == LauraX:
                            ch_l "Dude!"
                        elif Girl == JeanX:
                            ch_j "Hey! Um. . ."
                        elif Girl == StormX:
                            ch_s "Best that you not. . ."
                        else:
                            Girl.voice "What the fuck, [Girl.player_petname]!"
                            Girl.voice "I- I don't usually, you know. . ."
                    $ Girl.change_stat("obedience", 80, 7)
                    $ Girl.change_stat("inhibition", 30, 4)
                    $ Girl.change_stat("inhibition", 80, 4)
                    call expression Girl.Tag + "_First_Bottomless"

                $ Girl.change_stat("lust", 60, 1)
                if "exhibitionist" in Girl.Traits:
                    $ Girl.change_stat("lust", 200, 4)
            "Grab her tit":


                $ Girl.change_face("surprised", 1)
                "You come up to [Girl.name] and quickly honk her boob."
                if Girl.SEXP < 5 or not ApprovalCheck(Girl, 600, TabM=2):
                    "You come up to [Girl.name] and quickly honk her boob."
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("love", 60, -5)
                    call Punch
                    if Girl == RogueX:
                        "She slaps your hand away and smacks your face."
                        ch_r "What the fuck, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        "She slaps your hand away and elbows you in the ribs."
                        ch_k "[Girl.Like]WTF, [Girl.player_petname]?"
                    elif Girl == EmmaX:
                        "She slaps your hand away and elbows you in the ribs."
                        ch_e "You must learn to resist temptations, [Girl.player_petname]."
                    elif Girl == LauraX:
                        "She flips you onto your back."
                        ch_l "What the fuck?!"
                    elif Girl == JeanX:
                        $ JeanX.eyes = "psychic"
                        "You feel something slam the back of your head."
                        ch_j "Hands!"
                        $ JeanX.eyes = "squint"
                    elif Girl == StormX:
                        "She flips you onto your back."
                        ch_s "Can I help you?"
                    elif Girl == JubesX:
                        $ JubesX.ArmPose = 1
                        show Fireworks as Fire1 onlayer black:
                            pos (JubesX.sprite_location+160,270)
                        show Fireworks as Fire2 onlayer black:
                            pos (JubesX.sprite_location+160,270)
                        ch_v "Back it up. . ."
                    return
                if Girl.SEXP >= 40:
                    $ Girl.change_stat("lust", 60, 5)
                    $ Girl.change_stat("love", 90, 2)
                    $ Girl.change_face("sexy")
                    if Girl == RogueX:
                        ch_r "Ooh! Are you hinting at something there, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Hmm, I'm glad I can't phase right now, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "I do enjoy this, [Girl.player_petname]. . ."
                    elif Girl == LauraX:
                        ch_l "Hmm, that's pleasant."
                    elif Girl == JeanX:
                        ch_j "Hmm. . ."
                    elif Girl == StormX:
                        ch_s "Hello there. . ."
                    elif Girl == JubesX:
                        ch_v "Oh, hello. . ."
                    $ Count = 10
                elif ApprovalCheck(Girl, 800, "L", TabM=1):
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("lust", 60, 2)
                    $ Girl.change_stat("love", 90, 1)
                    if Girl == RogueX:
                        ch_r "Hmm, hand to my heart, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Hmm, keep it there, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "Mmmmmm. . ."
                    elif Girl == LauraX:
                        ch_l "Hmm, are you enjoying that as much as I am?"
                    elif Girl == JeanX:
                        ch_j "Well hello there."
                    elif Girl == StormX:
                        ch_s "Hello there. . ."
                    elif Girl == JubesX:
                        ch_v "Oh, hello. . ."
                    $ Count = 7
                elif ApprovalCheck(Girl, 1000, TabM=1):
                    $ Girl.change_face("perplexed")
                    $ Girl.change_stat("lust", 60, 1)
                    if Girl == RogueX:
                        ch_r "Oh! A little handsy, eh [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Kinda forward, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "Rather forward of you, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "That's a bit inappropriate, [Girl.player_petname]."
                    elif Girl == JeanX:
                        ch_j "Hey, that's a bit. . ."
                    elif Girl == StormX:
                        ch_s "That is my breast. . .Hmmm. . ."
                    elif Girl == JubesX:
                        ch_v "Little handsy there, [Girl.player_petname]. . ."
                    $ Count = 5
                elif ApprovalCheck(Girl, 800, TabM=1):
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 90, -3)
                    $ Girl.change_stat("obedience", 90, 4)
                    $ Girl.change_stat("inhibition", 90, 3)
                    if Girl == RogueX:
                        ch_r "You seem to have misplaced something. . ."
                    elif Girl == KittyX:
                        ch_k "You might want to move that?"
                    elif Girl == EmmaX:
                        ch_e "You should move that, immediately."
                    elif Girl == LauraX:
                        ch_l "Are you going to move that hand or will I have to?"
                    elif Girl == JeanX:
                        ch_j "Ehem, you going to move that?"
                    elif Girl == StormX:
                        ch_s "That is my breast. . ."
                    elif Girl == JubesX:
                        ch_v "Couldja watch the hands there, [Girl.player_petname]. . ."
                    $ Count = 3
                else:
                    $ Girl.change_face("angry")
                    $ Girl.change_stat("love", 90, -5)
                    $ Girl.change_stat("obedience", 90, 5)
                    $ Girl.change_stat("inhibition", 90, 3)
                    if Girl == RogueX:
                        ch_r "Move it or lose it, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "You wanna lose that hand?"
                    elif Girl == EmmaX:
                        ch_e "Do you want to lose that hand?"
                    elif Girl == LauraX:
                        $ Girl.ArmPose = 2
                        $ LauraX.Claws = 1
                        ch_l "You wanna lose that hand?"
                    elif Girl == JeanX:
                        ch_j "Excuse me?"
                    elif Girl == StormX:
                        ch_s "That is my breast. . . could you release it."
                    elif Girl == JubesX:
                        $ Girl.ArmPose = 1
                        ch_v "Do I need to spray you, [Girl.player_petname]?"
                    $ Count = 2
                $ Girl.change_stat("obedience", 70, 3)
                $ Girl.change_stat("inhibition", 70, 2)
                if Girl == RogueX:
                    ch_r "Um, are you going to let go?"
                elif Girl == KittyX:
                    ch_k "Um, are you done yet?"
                elif Girl == EmmaX:
                    ch_e "Had enough?"
                elif Girl == LauraX:
                    ch_l "Are you satisfied?"
                elif Girl == JeanX:
                    ch_j "That it?"
                elif Girl == StormX:
                    ch_s "Did you enjoy that?"
                elif Girl == JubesX:
                    ch_v "So, having fun?"
                while Count > 0:
                    if Count == 6:
                        $ Girl.change_face("sexy", 1)
                        if Girl == RogueX:
                            ch_r "Hmmm, maybe do keep at it. . ."
                        elif Girl == KittyX:
                            ch_k "Mmmmm, I do kinda like it. . ."
                        elif Girl == EmmaX:
                            ch_e "Mmmmm, I do enjoy that. . ."
                        elif Girl == LauraX:
                            ch_l "That's pretty comforting. . ."
                        elif Girl == JeanX:
                            ch_j "Ok, go ahead with that. . ."
                        elif Girl == StormX:
                            ch_s "Hmmm. . . more, perhaps. . ."
                        elif Girl == JubesX:
                            ch_v "Do go on. . ."
                        $ Girl.change_stat("lust", 90, 2)
                        $ Girl.change_stat("inhibition", 70, 1)
                    elif Count == 3:
                        $ Girl.change_face("perplexed")
                        $ Girl.change_stat("lust", 90, 1)
                        if Girl == RogueX:
                            ch_r "That's nice [Girl.player_petname], but maybe cut it out?"
                        elif Girl == KittyX:
                            ch_k "Not that it's not nice, [Girl.player_petname], but maybe stop?"
                        elif Girl == EmmaX:
                            ch_e "Not that I don't enjoy that, [Girl.player_petname]. . ."
                        elif Girl == LauraX:
                            ch_l "I like it, but maybe stop for now?"
                        elif Girl == JeanX:
                            ch_j "Ok, that's probably enough. . ."
                        elif Girl == StormX:
                            ch_s "Or, maybe not. . ."
                        elif Girl == JubesX:
                            ch_v "Um, probably cut that out. . ."
                    elif Count == 2:
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 90, -1)
                        if Girl == RogueX:
                            ch_r "Ok, stop it right now."
                        elif Girl == KittyX:
                            ch_k "Ok, give it a rest."
                        elif Girl == EmmaX:
                            ch_e "Ok, enough of that. . ."
                        elif Girl == LauraX:
                            ch_l "Ok, that's enough now."
                        elif Girl == JeanX:
                            ch_j "Maybe stop? . ."
                        elif Girl == StormX:
                            ch_s "Ok, that is plenty. . ."
                        elif Girl == JubesX:
                            $ JubesX.ArmPose = 1
                            ch_v "Ok, cut that out or you get the hose. . ."
                    elif Count == 1:
                        $ Girl.change_face("angry")
                        $ Girl.change_stat("love", 90, -5)
                        if Girl == RogueX:
                            ch_r "Back the hell off, [Girl.player_petname]!"
                            call Punch
                            "She slaps your hand away and smacks your face."
                            ch_r "What the fuck, [Girl.player_petname]?"
                        elif Girl == KittyX:
                            ch_k "Back it up, [Girl.player_petname]!"
                            call Punch
                            "She elbows you in the ribs."
                            ch_k "WTF, [Girl.player_petname]?"
                        elif Girl == EmmaX:
                            ch_e "Time to stop, [Girl.player_petname]."
                            call Punch
                            "She elbows you in the ribs."
                            ch_e "You should learn from social cues. . ."
                        elif Girl == LauraX:
                            ch_l "Take a step back, [Girl.player_petname]!"
                            call Punch
                            "She gives you a quick shove."
                        elif Girl == JeanX:
                            $ JeanX.eyes = "psychic"
                            call Punch
                            "You feel something slam the back of your head."
                            ch_j "Ok, that's good."
                            $ JeanX.eyes = "squint"
                        elif Girl == StormX:
                            ch_s "That is enough, [Girl.player_petname]."
                            call Punch
                            "She elbows you in the ribs."
                            ch_s "Everything in moderation. . ."
                        elif Girl == JubesX:
                            $ JubesX.ArmPose = 1
                            show Fireworks as Fire1 onlayer black:
                                pos (JubesX.sprite_location+160,270)
                            show Fireworks as Fire2 onlayer black:
                                pos (JubesX.sprite_location+160,270)
                            ch_v "Seriously, [Girl.player_petname]. . ."
                        $ Count = 1
                    $ Count -= 1 if Count >= 0 else 0

                    if Count > 0:
                        menu:
                            "Your hand is still on her chest."
                            "Let go immediately":
                                if Count >= 7:
                                    if Girl == RogueX:
                                        ch_r "Aw, can't say I'm not a {i}little{/i} disappointed. . ."
                                    elif Girl == KittyX:
                                        ch_k "That wasn't[Girl.like]{i}so{/i} bad. . ."
                                    elif Girl == EmmaX:
                                        ch_e "It's not that I really minded. . ."
                                    elif Girl == LauraX:
                                        ch_l "I didn't really mind it. . ."
                                    elif Girl == JeanX:
                                        ch_j "Aw, too bad. . ."
                                    elif Girl == StormX:
                                        ch_s "Ah, it was good while it lasted. . ."
                                    elif Girl == JubesX:
                                        ch_v "Maybe later though. . ."
                                    $ Girl.change_stat("lust", 60, 2)
                                    $ Girl.change_stat("inhibition", 70, 1)
                                elif Count <= 4:
                                    if Girl == RogueX:
                                        ch_r "Smart move."
                                    elif Girl == KittyX:
                                        ch_k "Probably for the best."
                                    elif Girl == EmmaX:
                                        ch_e "I suppose it's for the best."
                                    elif Girl == LauraX:
                                        ch_l "Probably for the best."
                                    elif Girl == JeanX:
                                        ch_j "Yeah. . ."
                                    elif Girl == StormX:
                                        ch_s "Ok, that is plenty. . ."
                                    elif Girl == JubesX:
                                        ch_v "Yeah. . ."
                                $ Count = 0
                            "Honk it again and let go":

                                if Count >= 7:
                                    if Girl == RogueX:
                                        ch_r "Heh, can't say I'm not a {i}little{/i} disappointed. . ."
                                    elif Girl == KittyX:
                                        ch_k "That wasn't[Girl.like]{i}so{/i} bad. . ."
                                    elif Girl == EmmaX:
                                        ch_e "Hmm, so amusing."
                                    elif Girl == LauraX:
                                        ch_l "I didn't mind it so much. . ."
                                    elif Girl == JeanX:
                                        ch_j "Aw, too bad. . ."
                                    elif Girl == StormX:
                                        ch_s "Hmmm. . ."
                                    elif Girl == JubesX:
                                        ch_v "Tsk. . ."
                                    $ Girl.change_stat("lust", 60, 4)
                                    $ Girl.change_stat("inhibition", 70, 1)
                                elif Count >= 4:
                                    if Girl == RogueX:
                                        ch_r "Classy, [Girl.player_petname]."
                                    elif Girl == KittyX:
                                        ch_k "A real joker, [Girl.player_petname]."
                                    elif Girl == EmmaX:
                                        ch_e "How droll."
                                    elif Girl == LauraX:
                                        ch_l "Heh."
                                    elif Girl == JeanX:
                                        ch_j "Hmmmm. . ."
                                    elif Girl == StormX:
                                        ch_s "Hmmm. . ."
                                    elif Girl == JubesX:
                                        ch_v "Hm. . ."
                                else:
                                    $ Girl.change_face("angry")
                                    if Girl == RogueX:
                                        ch_r "Dick move."
                                    elif Girl == KittyX:
                                        ch_k "Douche."
                                    elif Girl == EmmaX:
                                        ch_e "You'd better take more care."
                                    elif Girl == LauraX:
                                        ch_l "Asshole."
                                    elif Girl == JeanX:
                                        ch_j "Dick. . ."
                                    elif Girl == StormX:
                                        ch_s "Cute. . ."
                                    elif Girl == JubesX:
                                        ch_v "Joker. . ."
                                $ Girl.change_stat("obedience", 70, 3)
                                $ Girl.change_stat("inhibition", 70, 2)
                                $ Count = 0
                            "Fondle it a little":

                                if Girl.action_counter["fondle_breasts"]and ApprovalCheck(Girl, 1000, TabM=2):
                                    $ Girl.change_face("sexy",1)
                                    $ Girl.eyes = "closed"
                                    $ Girl.change_stat("lust", 90, 5)
                                else:
                                    $ Girl.change_face("perplexed")
                                    $ Girl.change_stat("lust", 90, 2)
                                    $ Count -= 1
                                $ Girl.change_stat("obedience", 70, 4)
                                $ Girl.change_stat("inhibition", 70, 2)
                                if Girl == EmmaX:
                                    ch_e "Mmm. . ."
                                elif Girl == LauraX:
                                    ch_l "Hmm. . ."
                                else:
                                    Girl.voice "Umm. . ."
                            "Just leave it there.":

                                if Count == 5:
                                    $ Girl.change_face("perplexed")
                                    $ Girl.change_stat("lust", 90, 3)
                                    if Girl == RogueX:
                                        ch_r "This is a bit odd."
                                    else:
                                        Girl.voice "Huh."
                                elif Count == 2:
                                    $ Girl.change_face("perplexed")
                                    $ Girl.change_stat("lust", 90, 1)
                                    if Girl == EmmaX:
                                        ch_e "Um, [EmmaX.player_petname]."
                                    elif Girl == LauraX:
                                        ch_l "This is getting uncomfortable."
                                    else:
                                        Girl.voice "This is getting a little uncomfortable."
                                $ Girl.change_stat("obedience", 70, 2)
                                $ Girl.change_stat("inhibition", 70, 1)

                if Girl == LauraX:
                    $ LauraX.ArmPose = 1
                    $ LauraX.Claws = 0
                if Girl == EmmaX and Taboo and "taboo" not in EmmaX.history:
                    ch_e "Show some respect when in public, [EmmaX.player_petname]."
                elif bg_current == "HW Party":
                    "She shrugs away from you and winks."
                    Girl.voice "Not now. . ."
                elif Girl.action_counter["fondle_breasts"]and ApprovalCheck(Girl, 1100, TabM = 3):
                    $ Girl.change_face("sexy", 1)
                    if Girl == RogueX:
                        ch_r "You know, maybe we could keep this party roll'in. . ."
                    elif Girl == KittyX:
                        ch_k "I wouldn't mind if we kept. . . you know. . ."
                    elif Girl == EmmaX:
                        if "three" not in EmmaX.history and not AloneCheck(EmmaX):

                            call Emma_ThreeCheck
                        ch_e "Were you just sampling, or did you want to continue?"
                    elif Girl == LauraX:
                        ch_l "We could keep going. . ."
                    elif Girl == JeanX:
                        ch_j "Did you have anything more in mind? . ."
                    elif Girl == StormX:
                        ch_s "Did you wish to continue?"
                    elif Girl == JubesX:
                        ch_v "What'er you thinking? More?"
                    menu:
                        extend ""
                        "Yeah!":
                            $ Girl.change_stat("lust", 60, 5)
                            $ Girl.change_stat("love", 90, 2)
                            $ Girl.change_stat("obedience", 60, 3)
                            $ Girl.change_stat("inhibition", 60, 3)
                            call expression Girl.Tag + "_SexAct" pass ("breasts")
                            call Trig_Reset (1)
                            return
                        "Nah, that was enough.":
                            $ Girl.change_face("sad", 1)
                            $ Girl.change_stat("lust", 60, 2)
                            $ Girl.change_stat("love", 90, -1)
                            $ Girl.change_stat("obedience", 60, 4)
                            $ Girl.change_stat("inhibition", 60, 3)
                            if Girl == RogueX:
                                ch_r "Whatever."
                            elif Girl == KittyX:
                                ch_k "Whatevs."
                            elif Girl == EmmaX:
                                ch_e "Oh. Pity."
                            elif Girl == LauraX:
                                ch_l "Fine."
                            elif Girl == JeanX:
                                ch_j "Aw, too bad. . ."
                            elif Girl == StormX:
                                ch_s "That is unfortunate."
                            elif Girl == JubesX:
                                ch_v "Aw. . ."
                elif ApprovalCheck(Girl, 800, TabM = 3):
                    $ Girl.brows = "confused"
                    $ Girl.eyes = "sexy"
                    $ Girl.mouth = "smile"
                    if Girl == RogueX:
                        ch_r "Was that fun for you?"
                    elif Girl == KittyX:
                        ch_k "You enjoy that?"
                    elif Girl == EmmaX:
                        ch_e "Did you enjoy that?"
                    elif Girl == LauraX:
                        ch_l "You enjoyed that?"
                    elif Girl == JeanX:
                        ch_j "Nice, right?"
                    elif Girl == StormX:
                        ch_s "I'm sure you were impressed."
                    elif Girl == JubesX:
                        ch_v "Well, if you were thinking more. . ."
                elif ApprovalCheck(Girl, 800):
                    $ Girl.change_face("angry", 1)
                    if Girl == RogueX:
                        ch_r "I can't believe you'd do that in public!"
                    elif Girl == KittyX:
                        ch_k "How could you do that in public?"
                    elif Girl == EmmaX:
                        ch_e "I can't believe you would do that in public."
                    elif Girl == LauraX:
                        ch_l "You do that in public?"
                    elif Girl == JeanX:
                        ch_j "Don't draw attention. . ."
                    elif Girl == StormX:
                        ch_s "Not in public."
                    elif Girl == JubesX:
                        ch_v "Not really the place for it. . ."
                else:
                    $ Girl.change_face("angry", 1)
                    if Girl == RogueX:
                        ch_r "Just, don't do that sort of thing again!"
                    elif Girl == KittyX:
                        ch_k "[Girl.like]keep your hands to yourself!"
                    elif Girl == EmmaX:
                        ch_e "Just keep your hands to yourself."
                    elif Girl == LauraX:
                        ch_l "Keep your hands to yourself!"
                    elif Girl == JeanX:
                        ch_j "Look, don't touch."
                    elif Girl == StormX:
                        ch_s "I didn't offer you permission to touch me like that."
                    elif Girl == JubesX:
                        ch_v "Ask first, ya'know? . ."
            "Rub her shoulders":


                "You come up to [Girl.name] from behind and gently rub her shoulders."
                if Girl.SEXP >= 30:
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("lust", 60, 3)
                    $ Girl.change_stat("love", 90, 2)
                    "She leans back into your hands"
                    if Girl == RogueX:
                        ch_r "Hmm, are you hinting at something there, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Hmm, getting frisky, [Girl.player_petname]?"
                    elif Girl == EmmaX:
                        ch_e "Hmm, to what do I owe the pleasure, [Girl.player_petname]?"
                    elif Girl == LauraX:
                        ch_l "Hmm, are you thinking what I'm thinking, [Girl.player_petname]?"
                    elif Girl == JeanX:
                        ch_j "Oooh, right there. . ."
                    elif Girl == StormX:
                        ch_s "Hmmm. . ."
                    elif Girl == JubesX:
                        ch_v "Ohhh. . . hay there. . ."
                elif ApprovalCheck(Girl, 650, "L",Alt=[[RogueX],600]):
                    $ Girl.change_face("sexy")
                    $ Girl.change_stat("lust", 60, 1)
                    $ Girl.change_stat("love", 90, 2)
                    if Girl == RogueX:
                        ch_r "Hmm, that feels nice, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Purr, that's nice, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "Well that's lovely, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "Hmmm, that's nice, [Girl.player_petname]."
                    elif Girl == JeanX:
                        ch_j "Hey, that's nice. . ."
                    elif Girl == StormX:
                        ch_s "That's lovely, [Girl.player_petname]."
                    elif Girl == JubesX:
                        ch_v "Ohhh. . . hay there. . ."
                elif ApprovalCheck(Girl, 500,Alt=[[RogueX],450]):
                    $ Girl.change_face("surprised", 1)
                    $ Girl.change_stat("love", 90, 1)
                    if Girl == EmmaX:
                        ch_e "Well hello, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "Oh, hey there, [Girl.player_petname]."
                    elif Girl == StormX:
                        ch_s "Hello, [Girl.player_petname]."
                    else:
                        Girl.voice "Oh, hey, [Girl.player_petname]. What's up?"
                elif ApprovalCheck(Girl, 350):
                    $ Girl.change_face("angry", 1)
                    $ Girl.change_stat("love", 90, -1)
                    if Girl == RogueX:
                        if Girl.Taboo:
                            ch_r "Hey, um, ease up on the PDAs there, [Girl.player_petname]."
                        else:
                            ch_r "Whoa, um, give me some space here."
                    elif Girl == KittyX:
                        if Girl.Taboo:
                            ch_k "Hey[Girl.like]maybe chill out, [Girl.player_petname]?"
                        else:
                            ch_k "Whoa, back it up."
                    elif Girl == EmmaX:
                        if Girl.Taboo:
                            ch_e "Do I have to explain boundaries to you, [Girl.player_petname]?"
                        else:
                            ch_e "I'd rather you didn't. . ."
                    elif Girl == LauraX:
                        if Girl.Taboo:
                            ch_l "Maybe take a step back, [Girl.player_petname]?"
                        else:
                            ch_l "Whoa, back it up."
                    elif Girl == JeanX:
                        if Girl.Taboo:
                            ch_j "Not in public. . ."
                        else:
                            ch_j "Hey. . ."
                    elif Girl == StormX:
                        if Girl.Taboo:
                            ch_s "Not while in public, [Girl.player_petname]?"
                        else:
                            ch_s "Could you not?"
                    elif Girl == JubesX:
                        if Girl.Taboo:
                            ch_v "Not here, right, [Girl.player_petname]?"
                        else:
                            ch_v "Not into it, [Girl.player_petname]."
                else:
                    $ Girl.change_face("angry", 1)
                    "She slaps your hands away."
                    if Girl == RogueX:
                        ch_r "Not really the time or place, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "No touchy!"
                    elif Girl == EmmaX:
                        ch_e "That will be enough of that."
                    elif Girl == LauraX:
                        ch_l "No hands or you lose them."
                    elif Girl == JeanX:
                        ch_j "Cut that out."
                    elif Girl == StormX:
                        ch_s "Cease that."
                    elif Girl == JubesX:
                        ch_v "Cut it out, geeze. . ."
                $ Girl.change_stat("obedience", 30, 3)
                $ Girl.change_stat("inhibition", 30, 2)
            "Ask for her_panties":


                call AskPanties (Girl)

            "Ask her to yoink some clothes" if Girl == KittyX:
                call Kitty_Yoink
            "Never mind [[exit]":

                $ Girl.Chat[5] = 0
    return





label Compliment(Girl=0, Line0=0, Line1=0, Line2=0, Options=[], CountList=[], Line=0, D20=0):




    $ Options = ["You really nailed that Danger Room exercise",
                "Great job in class the other day",
                "You're looking extra beautiful today",
                "Hey there, gorgeous",
                "I'm sorry, I got lost in your eyes",
                "You're looking really toned lately",
                "You have some really nice tits",
                "Your ass looks really great",
                "Oh, what's that fragrance? It suits you",
                "I'm so into you"]

    $ CountList = [0,1,2,3,4,5,6,7,8,9]
    $ renpy.random.shuffle(CountList)

    $ Line0 = Options[CountList[0]]
    $ Line1 = Options[CountList[1]]
    $ Line2 = Options[CountList[2]]
    menu:
        "[Line0]":
            $ Line = CountList[0]
        "[Line1]":
            $ Line = CountList[1]
        "[Line2]":
            $ Line = CountList[2]
        "These are all awful, I can do better. . .":
            ch_p "Um. . ."
            $ Girl.change_stat("love", 50, -1)
            $ Girl.change_stat("obedience", 40, -1)
            call Compliment (Girl)
            return
        "Never mind":
            $ Girl.Chat[5] = 0
            return

    $ D20 = renpy.random.randint(5, 20)
    if Girl == JubesX:
        $ D20 += 3


    if Line == 0:

        if ApprovalCheck(Girl, 1000):
            $ D20 += 5

        $ Girl.change_stat("love", 60, 3)
        if Girl == LauraX:
            $ Girl.change_stat("love", 40, 3)
            if D20 >= 10:
                $ Girl.change_face("smile")
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_stat("lust", 50, 2)
                ch_l "I know right? I think I nailed that one."
                ch_l "Those tin cans never stood a chance!"
            else:
                $ Girl.change_face("angry",1,Eyes="side")
                $ Girl.change_stat("inhibition", 50, 1)
                ch_l "Thanks. . ."
                ch_l "I don't know, I think I missed one of the Sentinels."
                ch_l "I have to be better than this."
                $ Girl.change_face("normal",0)
        elif Girl == JeanX:
            $ Girl.change_stat("love", 40, 3)
            $ Girl.change_stat("love", 80, 2)
            $ D20 -= 5
            if D20 >= 10:
                $ Girl.change_face("smile")
                $ Girl.change_stat("obedience", 60, 2)
                ch_j "Yeah, obviously."
            else:
                $ Girl.change_face("angry",1,Eyes="side")
                $ Girl.change_stat("inhibition", 80, 2)
                if D20 >= 9:
                    ch_j "Yeah, I know, but I think [EmmaX.name] did very poorly."
                    ch_j "I bet she wished she had TK too. . ."
                elif D20 >= 8:
                    ch_j "Yeah, I know, but I think [KittyX.name] really dropped the ball."
                    ch_j "I mean, she was phasing, but still. . ."
                elif D20 >= 7:
                    ch_j "Yeah, I know, but [RogueX.name] bumped into me and nearly sucked me dry."
                    ch_j "Usually she just sucks. . ."
                elif D20 >= 6:
                    ch_j "Yeah, I know, but [LauraX.name] almost took my head off."
                    ch_j "That's one of my best features!"
                else:
                    $ Girl.change_stat("inhibition", 90, 2)
                    ch_j "Yeah, I know, but you really sucked out there."
                    ch_j "It's almost like your power is useless against robots. . ."
                $ Girl.change_face("normal",0)
        else:
            $ Girl.change_stat("obedience", 60, 2)
            if D20 >= 15:
                $ Girl.change_face("smile")
                $ Girl.change_stat("love", 60, 1)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                if Girl == StormX:
                    ch_s "Yes, I do think that I did well at it."
                else:
                    Girl.voice "Yeah, I think I really nailed that one."
            elif D20 >= 10:
                $ Girl.change_face("bemused",2)
                $ Girl.change_stat("love", 60, 1)
                $ Girl.change_stat("obedience", 60, 1)
                Girl.voice "I think there's room for improvement though."
            else:
                $ Girl.change_face("bemused",1,Eyes="side")
                $ Girl.change_stat("love", 80, 1)
                Girl.voice "I appreciate the support, but we both know I could have done better."
                $ Girl.change_face("smile")

    elif Line == 1:

        if not ApprovalCheck(Girl, 700):
            $ D20 -= 5

        if D20 >= 10:
            $ Girl.change_stat("love", 70, 2)
            $ Girl.change_stat("obedience", 60, 1)
            if Girl == KittyX:
                $ Girl.change_face("smile")
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("inhibition", 50, 1)
                ch_k "Thanks, [KittyX.player_petname]!"
                ch_k "The numbers really spoke to me."
            elif Girl == EmmaX or Girl == StormX:
                $ Girl.change_face("bemused")
                $ Girl.change_stat("love", 80, 2)
                Girl.voice "I'm glad you were paying attention, [Girl.player_petname]."
            elif Girl == JeanX:
                $ Girl.change_stat("love", 80, 2)
                ch_j "Thanks, it wasn't hard."
            else:
                $ Girl.change_face("confused")
                Girl.voice "Thanks?"
        else:
            $ Girl.change_face("bemused")
            $ Girl.change_stat("love", 60, 1)
            $ Girl.change_stat("inhibition",50, 1)
            if Girl == KittyX:
                ch_k "Yeah, I definitely gave it my all there."
                $ D20 += 5
            elif Girl == EmmaX:
                ch_e "I'm surprised you were paying attention."
            elif Girl == JeanX:
                $ Girl.change_stat("love", 80, 2)
                ch_j "Thanks, it wasn't hard."
                $ Girl.change_stat("love", 80, -1)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_face("confused",1)
                ch_j "Wait. . ."
            elif Girl == StormX:
                ch_s "So you -were- awake. I owe Emma a drink."
            else:
                Girl.voice "Yeah, it was ok. Got a little dull though."

    elif Line == 2:

        if not ApprovalCheck(Girl, 900):
            $ D20 -= 10
        if Girl in (RogueX, KittyX, JeanX, JubesX):
            $ D20 += 5

        $ Girl.change_stat("inhibition", 50, 2)
        if Girl == LauraX:
            $ Girl.change_face("confused",1)
            $ Girl.change_stat("love", 80, 1, 1)
            $ Girl.change_stat("obedience", 60, 2)
            ch_l ". . ."
            ch_l "Ok?"
        elif D20 >= 10:
            $ Girl.change_face("bemused",2)
            $ Girl.change_stat("love", 70, 2)
            $ Girl.change_stat("love", 90, 2)
            if Girl == RogueX:
                ch_r "Well aren't you full'a sugar."
            elif Girl == KittyX:
                ch_k "Aw, that's sweet of you to say."
            elif Girl == EmmaX:
                ch_e "I do make an effort. . ."
            elif Girl == JeanX:
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 90, 2)
                ch_j "Congratulations, you have eyes."
            elif Girl == StormX:
                ch_s "I do strive for \"extra.\""
            elif Girl == JubesX:
                ch_v "Aw, thanks!"
            $ Girl.change_face("bemused",1)
        else:
            $ Girl.change_face("bemused",1)
            $ Girl.change_stat("love", 50, -1)
            $ Girl.change_stat("love", 70, -1)
            $ Girl.change_stat("obedience", 50, 2)
            if Girl == RogueX:
                ch_r "Well aren't you full'a crap. . ."
            elif Girl == KittyX:
                ch_k "Um, ok. . ."
            elif Girl == EmmaX:
                ch_e "So -just- today? . ."
            elif Girl == JeanX:
                $ Girl.change_face("confused",1)
                $ Girl.change_stat("inhibition", 90, 2)
                ch_j "Extra? So you don't think I'm -always- this beautiful?"
            elif Girl == StormX:
                ch_s "I don't think that my appearance should be your concern."
            elif Girl == JubesX:
                ch_v "Well, don't stare so much."

    elif Line == 3:

        if not ApprovalCheck(Girl, 900):
            $ D20 -= 10
        if Girl in (KittyX, EmmaX, JeanX, JubesX):
            $ D20 += 5

        if Girl == LauraX:
            $ Girl.change_face("confused",1)
            $ Girl.change_stat("love", 70, 2, 1)
            $ Girl.change_stat("inhibition", 50, 1)
            ch_l "Um. . . hi?"
        elif D20 >= 10:
            $ Girl.change_face("smile",2)
            $ Girl.change_stat("love", 60, 2)
            if D20 >= 15:
                $ Girl.change_stat("love", 200, 1)
                $ Girl.change_stat("obedience", 60, 1)
                $ Girl.change_stat("inhibition", 80, 1)
            if Girl == RogueX:
                ch_r "\"Hey there\" yourself."
            elif Girl == KittyX:
                ch_k "Oh, hehe, that's sweet of you. . ."
            elif Girl == EmmaX:
                ch_e "Yes. . . hello to you as well."
            elif Girl == JeanX:
                $ Girl.change_stat("obedience", 60, 3)
                ch_j "Oh, hey."
            elif Girl == StormX:
                ch_s "And a \"hello gorgeous\" to you as well."
            elif Girl == JubesX:
                ch_v "That's sweet. . ."
            $ Girl.change_face("smile",1)
        else:
            $ Girl.change_face("bemused",1)
            $ Girl.change_stat("love", 60, -1)
            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("inhibition", 50, 1)
            if Girl == RogueX:
                ch_r "\"Gorgeous\" yourself."
            elif Girl == KittyX:
                ch_k "Riight. . ."
            elif Girl == EmmaX:
                ch_e "Children these days. . ."
            elif Girl == JeanX:
                $ Girl.change_stat("love", 80, 1)
                ch_j "Whatever."
            elif Girl == StormX:
                ch_s "Oh, hello."
            elif Girl == JubesX:
                ch_v "Hey."

    elif Line == 4:

        if ApprovalCheck(Girl, 900, "L") and Girl != EmmaX:
            pass
        elif not ApprovalCheck(Girl, 1000):
            $ D20 -= 10
        if Girl in (RogueX, KittyX):
            $ D20 += 10

        if Girl == LauraX:
            $ Girl.change_face("confused")
            ch_l "What?"
        elif D20 >= 10:
            $ Girl.change_face("bemused",2)
            $ Girl.change_stat("love", 90, 2)
            $ Girl.change_stat("obedience", 50, 2)
            $ Girl.change_stat("inhibition", 30, 1)
            if Girl == RogueX:
                ch_r "What a charmer."
            elif Girl == KittyX:
                $ Girl.change_face("bemused",2,Mouth="smile")
                $ Girl.change_stat("love", 200, 1)
                $ Girl.change_stat("lust", 50, 2)
                ch_k "Heh. . . you don't say. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("bemused",1)
                ch_e "A valiant effort. . ."
            elif Girl == JeanX:
                ch_j "Well. . . ok."
            elif Girl == StormX:
                ch_s "I am used to that."
            elif Girl == JubesX:
                ch_v "I have that effect on people."
            $ Girl.change_face("bemused",1)
        else:
            $ Girl.change_face("angry",1,Eyes="up")
            $ Girl.change_stat("love", 60, 1)
            $ Girl.change_stat("obedience", 50, 1)
            if Girl == RogueX:
                ch_r "Maybe stay lost."
            elif Girl == KittyX:
                ch_k "Uh-huh. . ."
            elif Girl == EmmaX:
                ch_e "Perhaps you're laying it on a bit thick there. . ."
            elif Girl == JeanX:
                $ Girl.change_face("bemused",1,Eyes="up")
                $ Girl.change_stat("love", 60, 1)
                $ Girl.change_stat("obedience", 80, 1)
                $ Girl.change_stat("inhibition", 80, 1)
                ch_j "Don't be so basic."
            elif Girl == StormX:
                $ Girl.eyes = "white"
                ch_s "Better?"
            elif Girl == JubesX:
                ch_v "Sorry, I have that effect on people sometimes. . ."
            $ Girl.change_face("normal")

    elif Line == 5:

        if not ApprovalCheck(Girl, 600):
            $ D20 -= 12
        elif not ApprovalCheck(Girl, 1200):
            $ D20 -= 8

        if Girl in (LauraX,StormX):
            $ D20 += 8

        if Girl == LauraX:
            $ Girl.change_face("bemused")
            $ Girl.change_stat("love", 80, 2)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 50, 2)
            ch_l "Thanks? I've been trying something new."
        elif D20 >= 10:
            $ Girl.change_face("bemused",1)
            $ Girl.change_stat("love", 60, 2)
            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("inhibition", 60, 2)
            if Girl == RogueX:
                ch_r "Well. . . that's sweet of ya. . ."
            elif Girl == KittyX:
                ch_k "Oh. . . ok, um, thank you?"
            elif Girl == EmmaX:
                ch_e "Hmm, maybe a bit too lean? Perhaps I should take a break."
            elif Girl == JeanX:
                ch_j "I know you meant -\"always.\""
            elif Girl == StormX:
                ch_s "I have been trying a new routine."
            elif Girl == JubesX:
                ch_v "I have been working out. . ."
        else:
            $ Girl.change_face("angry",2)
            $ Girl.change_stat("love", 50, -1)
            $ Girl.change_stat("love", 70, -1)
            $ Girl.change_stat("obedience", 50, 2)
            $ Girl.change_stat("inhibition", 50, 1)
            if Girl == RogueX:
                ch_r "Maybe don't concern yourself with my \"tone.\""
            elif Girl == KittyX:
                ch_k "Are you being sarcastic?"
            elif Girl == EmmaX:
                ch_e "I don't think we should be discussing my body."
            elif Girl == JeanX:
                ch_j "You obviously meant that I -always- look toned."
                $ Girl.change_stat("love", 80, 2)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_stat("inhibition", 90, 2)
                $ Girl.change_face("bemused",1)
                ch_j "But at least you're paying attention."
            elif Girl == StormX:
                ch_s "You pay too close attention to my body."
            elif Girl == JubesX:
                ch_v "Ok, weirdo. . ."
            $ Girl.blushing -= 1
            $ Girl.mouth = "normal"

    elif Line == 6:

        if ApprovalCheck(Girl, 700, "I"):
            pass
        elif not ApprovalCheck(Girl, 900):
            $ D20 -= 15
        elif not ApprovalCheck(Girl, 1400):
            $ D20 -= 10

        if Girl in (KittyX, EmmaX):
            $ D20 += 5
        else:
            if D20 >= 10:
                $ Girl.change_face("bemused",2)
            else:
                $ Girl.change_face("angry",2)
        if D20 >= 10:
            $ Girl.change_stat("love", 90, 2)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 80, 4)
            $ Girl.change_stat("inhibition", 80, 3)
            $ Girl.change_stat("inhibition", 200, 1)
            $ Girl.change_stat("lust", 50, 3)
            if Girl == KittyX:
                $ Girl.change_face("bemused",2,Mouth="smile")
                ch_k "Really? Thanks, I appreciate that. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("bemused",1,Mouth="smile")
                ch_e "Marvelous, aren't they?"
            elif Girl == JeanX:
                $ Girl.change_face("bemused",1,Eyes="down")
                ch_j ". . ."
                $ Girl.eyes = "squint"
                ch_j "Yeah. . . how observant."
            elif Girl == StormX:
                ch_s ". . . yes, I suppose so. . ."
        else:
            $ Girl.change_stat("love", 70, -1)
            $ Girl.change_stat("obedience", 60, 3)
            $ Girl.change_stat("obedience", 80, 2)
            $ Girl.change_stat("inhibition", 80, 3)
            if Girl == KittyX:
                if D20 <= 5:
                    $ Girl.change_face("angry",2)
                    $ Girl.change_stat("love", 60, -3)
                    $ Girl.change_stat("love", 90, -1)
                    ch_k "Asshole!"
                else:
                    $ Girl.change_face("sadside",2,Mouth="smile")
                    ch_k "I get where you're going with that, but. . ."
                $ Girl.change_face(5,1)
            elif Girl == EmmaX:
                $ Girl.change_face("bemused",1)
                ch_e "Perhaps keep your eyes up here?"
                if D20 >= 5:
                    $ Girl.change_face("angry",1)
                    ch_e ". . ."
                    $ Girl.change_face("bemused",1)
                    $ Girl.change_stat("love", 90, 2)
                    $ Girl.change_stat("lust", 70, 5)
                    ch_e "Higher!"
            elif Girl == JeanX:
                $ Girl.change_face("bemused",1,Eyes="down")
                $ Girl.change_stat("love", 90, 2)
                ch_j "I know I should be offended, but you do have a point."
            elif Girl == StormX:
                ch_s "[Girl.player_petname]! Please restrain your libido."
        if Girl == RogueX:
            ch_r "Well bless your heart. I appreciate the effort."
        elif Girl == LauraX:
            ch_l "I guess so?"
        elif Girl == JubesX:
            ch_v "I mean. . . ok?"
        if Girl != KittyX:
            $ Girl.change_face("bemused",1)

    elif Line == 7:

        if ApprovalCheck(Girl, 700, "I"):
            pass
        elif not ApprovalCheck(Girl, 900):
            $ D20 -= 15
        elif not ApprovalCheck(Girl, 1300):
            $ D20 -= 10

        if Girl in (RogueX, EmmaX, StormX):
            $ D20 += 5

        if D20 >= 10:
            $ Girl.change_face("bemused",2)
            $ Girl.change_stat("love", 80, 2)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 60, 1)
            $ Girl.change_stat("lust", 30, 2)
            if Girl == RogueX:
                ch_r "I don't know, my jeans have been getting a bit tight. . ."
            elif Girl == KittyX:
                ch_k "I guess so? I mean. . ."
            elif Girl == EmmaX:
                ch_e "My, you do have good taste. . ."
                $ Girl.change_face("confused",1)
                ch_e "If perhaps poor manners. . ."
            elif Girl == LauraX:
                $ Girl.change_face("smile",1)
                ch_l "Good to know."
            elif Girl == JeanX:
                ch_j "Want me to shake it a little?"
            elif Girl == StormX:
                ch_s "You think so? How amusing."
            elif Girl == JubesX:
                ch_v "Really?"
            $ Girl.change_face("bemused",1)
        else:
            $ Girl.change_face("angry",1)
            $ Girl.change_stat("love", 60, -1)
            $ Girl.change_stat("love", 70, -2)
            $ Girl.change_stat("obedience", 60, 3)
            $ Girl.change_stat("inhibition", 50, 2)
            if Girl == EmmaX:
                ch_e "You shouldn't comment on a lady's figure."
            elif Girl == LauraX:
                $ Girl.change_face("confused",1)
                ch_l "Right. . ."
            elif Girl == JeanX:
                $ Girl.change_stat("love", 60, 3)
                ch_j "Obviously."
            elif Girl == StormX:
                ch_s "[Girl.player_petname], please be serious."
            else:
                Girl.voice "Rude."
            $ Girl.change_face("normal",1)

        if Girl == JubesX and Girl.accessory:
            ch_v "How could you tell?"

    elif Line == 8:

        if ApprovalCheck(Girl, 800, "L"):
            pass
        elif not ApprovalCheck(Girl, 1300):
            $ D20 -= 10
        if Girl in (EmmaX, LauraX, StormX):
            $ D20 += 15

        if D20 >= 10:
            $ Girl.change_face("bemused",1,Mouth="smile")
            $ Girl.change_stat("love", 90, 2)
            $ Girl.change_stat("love", 200, 1)
            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("inhibition", 80, 3)
            $ Girl.change_stat("lust", 50, 2)
            if Girl == RogueX:
                ch_r "Oh? Thank you, I guess?"
            elif Girl == KittyX:
                ch_k "Huh? . . I don't know, my usual shampoo, I guess. . ."
            elif Girl == EmmaX:
                ch_e "Thank you, I picked it up last time I was in Grasse."
            elif Girl == LauraX:
                ch_l "Probably blood, mostly. Ninjas."
            elif Girl == JeanX:
                $ Line = renpy.random.choice([RogueX.name,KittyX.name,EmmaX.name])
                ch_j "Oh, just something I found in [Line]'s room."
                $ Line = 8
            elif Girl == StormX:
                ch_s "Ah, a heart-shaped flower I discovered in my travels. . ."
            elif Girl == JubesX:
                ch_v "Oh, it's probably sun tan lotion. . ."
        else:
            $ Girl.change_face("angry",2,Mouth="grimace")
            $ Girl.change_stat("love", 60, -1)
            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("inhibition", 50, 1)
            if Girl == RogueX:
                ch_r "Probably best not to talk about a woman's scent."
            elif Girl == KittyX:
                ch_k "Gross. . ."
            elif Girl == EmmaX:
                ch_e "You might want to back up a bit. . ."
            elif Girl == LauraX:
                $ Girl.change_face("confused",1)
                $ Girl.change_stat("lust", 50, 2)
                ch_l "I don't know, I'm kinda sweaty, I guess. . ."
            elif Girl == JeanX:
                $ Girl.change_stat("love", 60, 1)
                $ Girl.change_stat("love", 80, 1)
                $ Girl.change_stat("obedience", 60, 2)
                $ Girl.change_face("bemused",1)
                ch_j "I don't know, something I found around. . ."
            elif Girl == StormX:
                ch_s ". . . you may be standing too close. . ."
            elif Girl == JubesX:
                ch_v "It's probably \"back the hell off.\""
            $ Girl.change_face("bemused",1)

    elif Line == 9:

        if ApprovalCheck(Girl, 900, "L"):
            pass
        elif not ApprovalCheck(Girl, 1100):
            $ D20 -= 10
        if Girl in (RogueX, LauraX, JeanX):
            $ D20 += 5

        if D20 >= 10:
            $ Girl.change_face("sly",1)
            $ Girl.change_stat("love", 80, 1)
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("obedience", 70, 2)
            $ Girl.change_stat("inhibition", 80, 3)
            $ Girl.change_stat("lust", 30, 5)
            $ Girl.change_stat("lust", 60, 5)
            if Girl == RogueX:
                ch_r "I'm glad for that. . ."
            elif Girl == KittyX:
                ch_k "You aren't yet. . ."
                ch_k "but you could be. . ."
            elif Girl == EmmaX:
                ch_e "Hmm, yes. . . I can see that."
            elif Girl == LauraX:
                ch_l "Not yet, you aren't."
            elif Girl == JeanX:
                ch_j "Of course you are. . ."
            elif Girl == StormX:
                ch_s "Oh, how nice. . ."
            elif Girl == JubesX:
                ch_v "You will be. Oh yes, you will be. . ."
        else:
            $ Girl.change_stat("love", 60, -2)
            $ Girl.change_stat("obedience", 60, 1)
            $ Girl.change_stat("inhibition", 50, 1)
            if Girl == EmmaX:
                $ Girl.change_face("angry",1,Mouth="smirk")
                ch_e "That's not really appropriate."
            elif Girl == JeanX:
                $ Girl.change_face("sly",1)
                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("obedience", 60, 1)
                ch_j "Control yourself. . ."
            else:
                $ Girl.change_face("bemused",1)
                Girl.voice "Ok. . ."


    if D20 < 10:
        menu:
            "Sorry":
                if Girl not in (LauraX,JeanX):
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("obedience", 40, -2)
                    $ Girl.change_stat("obedience", 70, -1)
                    $ Girl.change_face("sadside")
                if Girl == RogueX:
                    ch_r "Well, thanks for that. . ."
                elif Girl == KittyX:
                    ch_k "I guess I won't hold it against you. . ."
                elif Girl == EmmaX:
                    ch_e "Fine, I can accept that."
                elif Girl == LauraX:
                    $ Girl.change_face("normal")
                    ch_l "Whatever."
                elif Girl == JeanX:
                    $ Girl.change_face("angry",Eyes="side")
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("obedience", 70, -1)
                    ch_j ". . ."
                    if D20 < 7:
                        $ Girl.change_face("bemused")
                        $ Girl.change_stat("love", 60, 1)
                        $ Girl.change_stat("obedience", 50, 1)
                        ch_j "Ok, I can accept that."
                    if D20 < 5:
                        $ Girl.change_stat("love", 90, 1)
                        $ Girl.change_stat("obedience", 40, 2)
                        ch_j "Just don't let it happen again."
                elif Girl == StormX:
                    ch_s "Don't be sorry, be better."
                elif Girl == JubesX:
                    $ Girl.change_stat("love", 70, 1)
                    ch_v "Yeah, ok. . ."
                $ Girl.change_face("normal")
            ". . .":
                pass
    elif bg_current == "date":

        if "compliment" not in Girl.recent_history:
            $ Girl.AddWord(1,"compliment",0,0,0)
            call Date_Bonus (Girl, 5)
    return



label Love_You(Girl=0):



    ch_p "[Girl.name], I love you."
    if bg_current == "HW Party":
        Girl.voice ". . . we should talk after the party. . ."
        return

    if "lover" not in Girl.player_petnames:

        if "love" in Girl.history:

            if ApprovalCheck(Girl, 800,"L"):

                $ Girl.change_stat("love", 90, 2)
                $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_stat("lust", 30, 5)
                $ Girl.change_face("bemused",2,Brows="confused")

                if Girl == RogueX:
                    ch_r "Don't push it. . ."
                elif Girl == KittyX:
                    ch_k "I can't even . ."
                elif Girl == EmmaX:
                    ch_e "Just don't. . ."
                elif Girl == LauraX:
                    ch_l "I don't want to. . ."
                elif Girl == JeanX:
                    ch_j "Well, I don't know what to do with that. . ."
                elif Girl == StormX:
                    ch_s "Don't toy with me. . ."
                elif Girl == JubesX:
                    ch_v "I don't know. . ."

            elif ApprovalCheck(Girl, 600,"L"):

                $ Girl.change_stat("love", 95, 2)
                $ Girl.change_stat("obedience", 80, 3)
                $ Girl.change_stat("inhibition", 60, 1)
                $ Girl.change_face("bemused",2)

                if Girl == RogueX:
                    ch_r "I don't know, love? . ."
                elif Girl == KittyX:
                    ch_k "I don't know if I think of you like that . ."
                elif Girl == EmmaX:
                    ch_e "This is incredibly inappropriate. . ."
                elif Girl == LauraX:
                    ch_l "I don't. . ."
                elif Girl == JeanX:
                    $ Girl.change_stat("love", 50, 1)
                    ch_j "Right, but. . ."
                elif Girl == StormX:
                    ch_s "So you say, but. . ."
                elif Girl == JubesX:
                    ch_v "You're moving fast. . ."
            else:

                $ Girl.change_stat("love", 95, -5)
                $ Girl.change_stat("obedience", 90, 5)
                $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_face("angry",1)

                if Girl == RogueX:
                    ch_r "Bull."
                elif Girl == KittyX:
                    ch_k "Stop trolling me!"
                elif Girl == EmmaX:
                    ch_e "Oh forget this nonsense already. . ."
                elif Girl == LauraX:
                    ch_l "Fuck off with this. . ."
                elif Girl == JeanX:
                    $ Girl.change_stat("love", 60, 2)
                    ch_j "Oh, keep it in your pants. . ."
                elif Girl == StormX:
                    ch_s "Oh, you child. . ."
                elif Girl == JubesX:
                    ch_v "Geeze, relax. . ."


        $ Girl.AddWord(1,"love","love",0,"love")

        if Girl == RogueX:
            if not RogueX.Event[6]:

                $ Line = "never"
            elif RogueX.Event[6] >= 20:

                ch_r "You're just giving me whiplash here, [RogueX.player_petname]."

        elif Girl == KittyX:
            if not KittyX.Event[6]:
                $ Line = "never"
            elif KittyX.Event[6] >= 20:
                call Kitty_Love_Redux
        elif Girl == EmmaX:
            if not EmmaX.Event[6]:

                $ Line = "never"
            elif EmmaX.Event[6] >= 20:
                call Emma_Love_Redux
        elif Girl == LauraX:
            if not LauraX.Event[6]:
                $ Line = "never"
            elif LauraX.Event[6] >= 20:
                call Laura_Love_Redux
        elif Girl == JeanX:
            if not JeanX.Event[6]:
                $ Line = "never"
            elif JeanX.Event[6] >= 20:
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("love", 200, 40)
                ch_j "Nice to hear you admit it."
        elif Girl == StormX:
            if not StormX.Event[6]:

                $ Line = "never"
            elif StormX.Event[6] >= 20:
                call Storm_Love_Redux
        elif Girl == JubesX:
            if not JubesX.Event[6]:

                $ Line = "never"
            elif JubesX.Event[6] >= 20:
                call Jubes_Love_Redux

        if Line == "never":

            if ApprovalCheck(Girl, 800,"L"):
                $ Girl.change_stat("love", 90, 10)
                $ Girl.change_stat("lust", 50, 5)
                $ Girl.change_face("smile",2,Eyes="surprised")
            elif ApprovalCheck(Girl, 600,"L"):
                $ Girl.change_stat("love", 90, 5)
                $ Girl.change_face("confused",2,Eyes="surprised")
            else:
                $ Girl.change_face("angry",1,Brows="confused")
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 90, 5)
            $ Girl.change_stat("obedience", 70, 5)
            $ Girl.change_stat("inhibition", 60, 5)
            if Girl == RogueX:
                ch_r "Whaaa? . ."
                ch_r "Is this some kind of joke?"
            elif Girl == KittyX:
                ch_k "What was that? . ."
                ch_k ". . . Um, I gotta go!"
            elif Girl == EmmaX:
                ch_e "What? I. . . I don't know what to say about that."
                ch_e "I. . . I'll get back to you."
            elif Girl == LauraX:
                ch_l "Huh? You-"
                ch_l "Um. . ."
                ch_l "Bye."
            elif Girl == JeanX:
                ch_j "Hmm, food for thought. . ."
            elif Girl == StormX:
                ch_s "Let me consider this. . ."
            elif Girl == JubesX:
                ch_v "I. . . not now. . ."

            "[Girl.name] leaves the room."
            call Remove_Girl (Girl)
            jump Misplaced
        return


    if "love" in Girl.daily_history:

        $ Girl.change_stat("love", 95, 5)
        $ Girl.change_stat("obedience", 70, 2)
        $ Girl.change_stat("inhibition", 60, 1)
        $ Girl.change_stat("lust", 50, 5)
        $ Girl.change_face("smile",1)
        if Girl == RogueX:
            ch_r "I think you told me that earlier. . ."
            ch_r "but don't stop on my account, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "Didn't you already say that? . ."
            ch_k ". . . say it again."
        elif Girl == EmmaX:
            ch_e "So you've told me. . ."
            ch_e "but I don't tire of it, [EmmaX.player_petname]."
        elif Girl == LauraX:
            ch_l "Yeah, I know. . ."
            ch_l "but you can keep saying it, [LauraX.player_petname]."
        elif Girl == JeanX:
            $ Girl.change_stat("love", 80, -2)
            $ Girl.change_stat("obedience", 70, -2)
            ch_j "You're getting a little repetitive. . ."
        elif Girl == StormX:
            ch_s "This isn't the first time today. . ."
            ch_s "Perhaps it should not be the last. . ."
        elif Girl == JubesX:
            ch_v "Seriously, give me time to think. . ."

    elif ApprovalCheck(Girl, 800,"L"):

        $ Girl.change_stat("love", 90, 5)
        $ Girl.change_stat("love", 200, 5)
        $ Girl.change_stat("obedience", 70, 1)
        $ Girl.change_stat("inhibition", 60, 1)
        $ Girl.change_stat("lust", 30, 5)
        $ Girl.change_face("smile",1)
        if Girl == RogueX:
            ch_r "I love you too, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "Awwww! I love you too, [KittyX.player_petname]."
        elif Girl == EmmaX:
            ch_e "And I love you too, [EmmaX.player_petname]."
        elif Girl == LauraX:
            ch_l "Yeah, love you too."
        elif Girl == JeanX:
            ch_j ". . ."
            $ Girl.change_stat("obedience", 90, 2)
            $ Girl.change_stat("inhibition", 80, 1)
            ch_j "I love you too, ok?"
        elif Girl == StormX:
            ch_s "And I love you as well. . ."
        elif Girl == JubesX:
            ch_v "Aw, love you right back!"
    else:

        $ Girl.change_stat("love", 90, 5)
        $ Girl.change_stat("love", 50, -10, 1)
        $ Girl.change_stat("obedience", 70, 3)
        $ Girl.change_face("sadside",1)
        if Girl == RogueX:
            ch_r "It's too late for that."
        elif Girl == KittyX:
            ch_k "As if. Jerk."
        elif Girl == EmmaX:
            ch_e "I dearly wish that I could believe that."
        elif Girl == LauraX:
            ch_l "You blew it."
        elif Girl == JeanX:
            ch_j "Yeah, bullshit. . ."
        elif Girl == StormX:
            ch_s "If only that were so. . ."
        elif Girl == JubesX:
            ch_v "Talk is cheap. . ."

    $ Girl.AddWord(1,"love","love",0,"love")
    return





label TouchCheek(Girl=0):
    if Girl not in all_Girls:
        return
    call shift_focus (Girl)
    $ Girl.change_face("surprised", 1)
    if "no_cheek" in Girl.daily_history:
        "You reach out to brush [Girl.name]'s face with your hand, but she slaps it away."
        $ Girl.change_face("angry")
        if Girl == RogueX:
            ch_r "Back off, asshole."
        elif Girl == EmmaX:
            ch_e "What are you doing, [Girl.player_petname]?"
        elif Girl == JeanX:
            $ Girl.eyes = "psychic"
            ch_j "I told you to keep your distance."
            $ Girl.eyes = "squint"
        elif Girl == StormX:
            ch_s "Do not."
        else:
            Girl.voice "Hands off, dickbag."
        $ Girl.change_stat("love", 50, -2)
        return
    else:
        "You reach out and brush [Girl.name]'s face with your hand, a shiver runs through her."
    $ Girl.change_stat("obedience", 50, 1)

    if Girl == RogueX or "addictive" in Player.Traits:
        $ Girl.addiction -= 2
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0
        $ Girl.addiction_rate = 3 if Girl.addiction_rate < 3 else Girl.addiction_rate
        $ Girl.change_stat("lust", 70, 5)
    else:
        $ Girl.addiction -= 2
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0
        $ Girl.change_stat("lust", 40, 5)

    if ApprovalCheck(Girl, 1000):
        $ Girl.change_face("sexy", 1)
        if Girl == RogueX:
            ch_r "A promise of things to come, [Girl.player_petname]?"
        elif Girl == EmmaX:
            ch_e "That's sweet, what was it for, [Girl.player_petname]?"
        elif Girl == JeanX:
            ch_j "Oh, um. . . hey."
        else:
            Girl.voice "Hmmm, what were you thinking, [Girl.player_petname]?"
        $ Girl.change_stat("love", 80, 1)
    elif ApprovalCheck(Girl, 800,Alt=[[RogueX],500]) or ApprovalCheck(Girl, 700,"L"):
        $ Girl.change_face("smile", 1)
        if Girl == RogueX:
            ch_r "That was. . . nice."
        elif Girl == EmmaX:
            ch_e "Mmmmm. . ."
        elif Girl == JeanX:
            ch_j "Oh, hey. . ."
        else:
            Girl.voice "Sweet. . ."
    elif "cheek" in Girl.daily_history:
        $ Girl.change_face("angry", 1)
        if Girl == RogueX:
            ch_r "Hey, I told you to cut that out already."
        elif Girl == EmmaX:
            ch_e "I won't warn you again, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "I warned you to keep your distance. . ."
        else:
            Girl.voice "Hey, I warned you, [Girl.player_petname]."
        $ Girl.change_stat("love", 50, -2)
        $ Girl.daily_history.append("no_cheek")
    elif ApprovalCheck(Girl, 250):
        $ Girl.mouth = "smile"
        $ Girl.brows = "normal"
        if Girl == RogueX:
            ch_r "A. . . little warning maybe next time?"
        elif Girl == EmmaX:
            ch_e "Hmm, perhaps we need to discuss \"boundaries.\""
        elif Girl == JeanX:
            ch_j "Hey! don't touch me."
        elif Girl == StormX:
            ch_s "Keep your distance. . ."
        elif Girl == JubesX:
            ch_v "Back it up!"
        else:
            Girl.voice "Um, that was weird."
    else:
        $ Girl.change_face("angry", 1)
        if Girl == RogueX:
            ch_r "Don't. . . don't do that."
        elif Girl == EmmaX:
            ch_e "That's inappropriate behavior, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "I don't think that is appropriate. . ."
        else:
            Girl.voice "Back off, weirdo."
        $ Girl.change_stat("love", 50, -3)
        $ Girl.change_stat("obedience", 50, 1)
        $ Girl.change_stat("inhibition", 30, 1)

    if "no_cheek" in Girl.daily_history:
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck(Girl, 300):
                    $ Girl.change_face("sexy", 1)
                    if Girl == RogueX:
                        ch_r "Well, ok, just cut it out though."
                    elif Girl == EmmaX:
                        ch_e "See that it doesn't."
                    elif Girl == StormX:
                        ch_s "So long as you understand. . ."
                    else:
                        Girl.voice "Ok. . ."
                    $ Girl.change_stat("love", 80, 2)
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.eyes = "side"
                    if Girl == RogueX:
                        ch_r "A likely story. . ."
                    elif Girl == EmmaX:
                        ch_e "I'm sure."
                    elif Girl == StormX:
                        ch_s "Very well. . ."
                    else:
                        Girl.voice "Uh-huh."
                    $ Girl.change_stat("obedience", 20, 1)
            "You know you wanted it.":


                if ApprovalCheck(Girl, 400, "OI",Alt=[[RogueX],300]) or ApprovalCheck(Girl, 800,Alt=[[RogueX,LauraX],1500]):
                    $ Girl.change_face("normal", 1)
                    $ Girl.eyes = "squint"
                    if Girl == RogueX:
                        ch_r "Well. . . I guess, maybe. . ."
                    elif Girl == JeanX:
                        ch_j "What? No. . ."
                    elif Girl == JubesX:
                        ch_v "We'll see how far that gets'ya!"
                    else:
                        Girl.voice "Don't make promises you can't keep."
                    $ Girl.change_stat("love", 60, -1)
                    $ Girl.change_stat("obedience", 30, 2)
                    $ Girl.change_stat("inhibition", 40, 2)
                else:
                    $ Girl.change_face("angry", 2)
                    $ Girl.eyes = "squint"
                    if Girl == RogueX:
                        ch_r "Like hell I did."
                    elif Girl == EmmaX:
                        ch_e "You {i}must{/i} be daydreaming."
                    elif Girl == StormX:
                        ch_s "Unlikely. . ."
                    else:
                        Girl.voice "You wish."
                    $ Girl.blushing = 1
                    $ Girl.change_stat("love", 60, -3)
                    $ Girl.change_stat("obedience", 30, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
    else:

        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck(Girl, 850, "LI"):
                    $ Girl.change_face("sexy", 1)
                    if Girl == RogueX:
                        ch_r "I'll make sure to collect on that later."
                    elif Girl == KittyX:
                        ch_k "Yeah,[KittyX.like]stop being weird."
                    elif Girl == EmmaX:
                        ch_e "Don't make promises you can't keep."
                    elif Girl == LauraX:
                        ch_l "There better be more where that came from."
                    elif Girl == JeanX:
                        ch_j "Of course I did!"
                        ch_j "But you'll have to do better than that. . ."
                    elif Girl == StormX:
                        ch_s "You have a strange sense of humor. . ."
                    elif Girl == JubesX:
                        ch_v "Aw."
                    $ Girl.change_stat("love", 80, 2)
                elif ApprovalCheck(Girl, 500, "LI"):
                    $ Girl.change_face("smile", 1)
                    if Girl == RogueX:
                        ch_r "Aw, you're sweet."
                    elif Girl == KittyX:
                        ch_k "I'm not the only one looking cute, [LauraX.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "You don't look so bad yourself, [EmmaX.player_petname]."
                    elif Girl == LauraX:
                        ch_l "Uh, yeah. . . you too?"
                    elif Girl == JeanX:
                        ch_j "Of course I did!"
                        ch_j "Still. . ."
                    elif Girl == StormX:
                        ch_s "Hmmm, you flatterer. . ."
                    elif Girl == JubesX:
                        ch_v "Aw, you know it."
                    $ Girl.change_stat("love", 80, 2)
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.eyes = "side"
                    if Girl == RogueX:
                        ch_r "Don't you \"cute\" me, just cut it out. . ."
                    elif Girl == KittyX:
                        ch_k "Too cute for you."
                    elif Girl == EmmaX:
                        ch_e "Obviously."
                    elif Girl == LauraX:
                        ch_l "I don't do \"cute.\""
                    elif Girl == JeanX:
                        ch_j "Of course I did!"
                        ch_j "That doesn't mean you can just touch me. . ."
                    elif Girl == StormX:
                        ch_s "You joke. . ."
                    elif Girl == JubesX:
                        ch_v "Still. . ."
                    $ Girl.change_stat("obedience", 20, 1)
            "You had a fly on you.":


                if ApprovalCheck(Girl, 850, "LI"):
                    $ Girl.change_face("sexy", 1)
                    if Girl == RogueX:
                        ch_r "Oh? Was that all. . ."
                    elif Girl == EmmaX:
                        ch_e "Oh? I'm {i}sure{/i} that was it. . ."
                    elif Girl == JeanX:
                        ch_j "Flies know better than to land on me."
                    elif Girl == StormX:
                        ch_s "I doubt that. . ."
                        "A gust of wind swirls around her."
                    elif Girl == JubesX:
                        ch_v "Doubtful."
                    else:
                        Girl.voice "Oh? Sorry. . ."
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("inhibition", 40, 1)
                elif ApprovalCheck(Girl, 600):
                    $ Girl.change_face("normal")
                    Girl.voice "A fly, right. . ."
                else:
                    $ Girl.change_face("angry", 1)
                    if Girl == RogueX:
                        ch_r "A likely story, look, just don't touch me."
                    elif Girl == EmmaX:
                        ch_e "That's no excuse."
                    elif Girl == JeanX:
                        ch_j "Flies know better than to land on me."
                    elif Girl == StormX:
                        ch_s "They know to keep their distance. . ."
                        "A gust of wind swirls around her."
                    elif Girl == JubesX:
                        ch_v "Don't get many of those anymore. . ."
                    else:
                        Girl.voice "Riiiight, just don't touch me."
                    $ Girl.change_stat("obedience", 50, 2)
            "Are you sure you didn't enjoy that?":


                if ApprovalCheck(Girl, 650, "LI") or ApprovalCheck(Girl, 1000):
                    $ Girl.change_face("sexy", 1)
                    $ Girl.eyes = "side"
                    if Girl == RogueX:
                        ch_r "I suppose I did, at that."
                    elif Girl == EmmaX:
                        ch_e "I'd need to try again to be sure. . ."
                    elif Girl == JeanX:
                        ch_j ". . ."
                        ch_j "I guess. . ."
                    elif Girl == StormX:
                        ch_s "Perhaps. . ."
                    elif Girl == JubesX:
                        ch_v "Well, find out. . ."
                    else:
                        Girl.voice "Maybe if there were more to it. . ."
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 30, 1)
                    $ Girl.change_stat("inhibition", 40, 1)
                elif ApprovalCheck(Girl, 500, "OI"):
                    $ Girl.change_face("normal", 1)
                    if Girl == EmmaX:
                        ch_e "Don't push it. . . too far."
                    elif Girl == JeanX:
                        ch_j ". . ."
                        ch_j "I guess. . ."
                    elif Girl == StormX:
                        ch_s "I. . . no. . ."
                    elif Girl == JubesX:
                        ch_v "Not really. . ."
                    else:
                        Girl.voice "Well. . . I guess, maybe. . . no, quit it."
                    $ Girl.change_stat("love", 60, -1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 30, 2)
                    $ Girl.change_stat("inhibition", 40, 2)
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.eyes = "side"
                    if Girl == KittyX:
                        ch_k "Not interested."
                    elif Girl == EmmaX:
                        ch_e "Positive."
                    elif Girl == JeanX:
                        ch_j "Definately."
                    elif Girl == StormX:
                        ch_s "Certain."
                    else:
                        Girl.voice "Grrrr. . ."
                    $ Girl.change_stat("love", 60, -3)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 30, 3)
                    $ Girl.change_stat("inhibition", 40, 2)


    $ Girl.recent_history.append("cheek")
    $ Girl.daily_history.append("cheek")
    return




label Hold_Hands(Girl=0, Gloves=0):

    if Girl.arms == "gloves":
        menu:
            "Gloves or no Gloves?"
            "Gloves":
                pass
            "No Gloves":
                ch_p "Hey, could you lose the gloves for a second?"
                if Girl == RogueX:
                    ch_r "Ok, [Girl.player_petname]. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, fine, [Girl.player_petname]. . ."
                $ Gloves = "gloves"
                $ Girl.arms = 0
    "You reach down and grab [Girl.name]'s hand in yours."
    if ApprovalCheck(Girl, 800,"L"):
        $ Girl.change_face("smile",1,Eyes="closed")
        "She squeezes your hand back and leans her shoulder against yours."
        $ Count = 10
    elif ApprovalCheck(Girl, 1200):
        $ Girl.change_face("bemused",1,Brows="confused")
        "She gives your hand a light squeeze in return."
        $ Count = 4
    elif ApprovalCheck(Girl, 800):
        $ Girl.change_face("bemused",2,Brows="confused")
        "She stiffens a bit, but leaves her hand in yours."
        $ Girl.change_face("bemused",1,Eyes="down")
        $ Count = 2
    else:

        $ Girl.change_face("angry",1)
        $ Girl.change_stat("love", 40, -1)
        $ Girl.change_stat("love", 60, -1)
        $ Girl.change_stat("obedience", 60, 2)
        $ Girl.change_stat("obedience", 80, 1)
        $ Girl.change_stat("inhibition", 50, 1)
        if not Girl.arms and Girl.resistance:
            $ Girl.change_stat("obedience", 60, 2)
            $ Girl.change_stat("lust", 30, 5)
            $ Girl.addiction -= 2
            $ Girl.addiction_rate += 1 if RogueX.addiction_rate < 5 else 0
        if Gloves == "gloves":
            $ Girl.arms = "gloves"
            "She slaps your hand away, putting her gloves back on."
        else:
            "She slaps your hand away."
        Girl.voice "Don't get too familiar."
        return

    if Girl.arms != "gloves":
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0

    while Count:
        $ Round -= 5
        if ApprovalCheck(Girl, 800,"L"):
            if Count >= 8:
                $ Girl.change_stat("love", 90, 2)
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("lust", 30, 2)
        elif ApprovalCheck(Girl, 1200):
            if Count >= 3:
                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("obedience", 70, 2)
                $ Girl.change_stat("lust", 30, 1)
        elif ApprovalCheck(Girl, 800):
            $ Girl.change_stat("love", 70, 2)
            $ Girl.change_stat("obedience", 50, 2)
        if Girl.arms != "gloves" and Girl.addiction_rate >= 3 and Girl.addiction >= 5:
            $ Girl.change_stat("lust", 50, 3)
            $ Girl.addiction -= 2
            $ Count += 1 if Count <= 1 else 0
            if Girl.lust >= 30:
                $ Girl.change_face("sly",2)

        menu:
            "Keep holding hands.":
                pass
            "Stop holding hands.":
                $ Count = 0
                $ Girl.change_face("bemused",1)
                return
        $ Count -= 1
        $ Count = 0 if Round <= 10 else Count



    $ Girl.AddWord(1,"holdhands","holdhands")

    if not ApprovalCheck(Girl, 800,"L") and not ApprovalCheck(Girl, 1200):

        $ Girl.change_face("sadside",1,Brows="confused")
        $ Girl.change_stat("love", 60, -2)
        $ Girl.change_stat("obedience", 60, -2)
        $ Girl.change_stat("inhibition", 50, 3)
        $ Girl.change_stat("lust", 60, -5)
    else:
        $ Girl.change_face("smile",1)
    if Gloves == "gloves":
        $ Girl.arms = "gloves"
    $ Gloves = 0
    Girl.voice "Ok, that's enough of that. . ."
    return




label Girl_Headpat(Girl=0):
    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)
    $ Girl.change_face("surprised", 1)
    if "no_headpat" in Girl.daily_history:
        "You reach out to pat [Girl.name] on the head, but she slaps it away."
        $ Girl.change_face("angry")
        if Girl == RogueX:
            ch_r "Hands ta yourself, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "I told you, weird."
            ch_k "Weirdo."
        elif Girl == EmmaX:
            ch_e "What have we said about this \"head pats\" obsession?"
        elif Girl == LauraX:
            ch_l "Seriously, hands off."
        elif Girl == JeanX:
            $ Girl.eyes = "psychic"
            ch_j "I told you to keep your distance."
            $ Girl.eyes = "squint"
        elif Girl == StormX:
            ch_s "Stay away from the hair."
        elif Girl == JubesX:
            ch_v "Hey, watch the 'doo!"
        $ Girl.change_stat("love", 50, -2)
        return
    else:
        "You reach out and pat [Girl.name] on the head."
    $ Girl.change_stat("obedience", 50, 2)

    if ApprovalCheck(Girl, 1200,Alt=[[LauraX],1000]):
        $ Girl.change_face("sexy", 1)
        if Girl == EmmaX:
            ch_e "Hmmmm?"
        else:
            Girl.voice "Mmmmm. . ."
        $ Girl.change_stat("love", 85, 1)
    elif ApprovalCheck(Girl, 800,Alt=[[EmmaX],1200]) or ApprovalCheck(Girl, 750, "L",Alt=[[LauraX],600]):
        $ Girl.change_face("smile", 1)
        Girl.voice "Mmmmm. . ."
    elif "headpat" in Girl.daily_history:
        $ Girl.change_face("angry", 1)
        if Girl == RogueX:
            ch_r "Hands ta yourself, [Girl.player_petname]."
        elif Girl == KittyX:
            ch_k "Hey, cut it out."
        elif Girl == EmmaX:
            ch_e "Do I look like a child or pet to you?"
        elif Girl == LauraX:
            ch_l "I warned you not to do that."
        elif Girl == JeanX:
            ch_j "Hey! Watch the hair!"
        elif Girl == StormX:
            ch_s "Back up. Now."
        elif Girl == JubesX:
            ch_v "What'd I tell you?"
        $ Girl.change_stat("love", 50, -2)
        $ Girl.daily_history.append("no_headpat")
    elif ApprovalCheck(Girl, 400,Alt=[[EmmaX],600]):
        $ Girl.mouth = "smile"
        $ Girl.brows = "normal"
        if Girl == RogueX:
            ch_r "This is. . . weird."
        elif Girl == KittyX:
            ch_k "Um, okay.."
        elif Girl == EmmaX:
            ch_e "Hmph. You have some odd interests."
        elif Girl == LauraX:
            ch_l "Um, that was weird."
        elif Girl == JeanX:
            ch_j "'the hell?"
        elif Girl == StormX:
            ch_s "What is that about?"
        elif Girl == JubesX:
            ch_v "Weirdo."
    else:
        $ Girl.change_face("angry", 1)
        if Girl == RogueX:
            "She slaps your hand aside and glares at you."
            ch_r "Quit it!"
        elif Girl == KittyX:
            "She slaps your hand aside and glares at you."
            ch_k "Knock it off!"
        elif Girl == EmmaX:
            "She grabs your wrist and pulls it away from her hair."
            ch_e "I will warn you once. Stop that."
        elif Girl == LauraX:
            "She flails her arms around, knocking your hand away."
            ch_l "Get away from me."
        elif Girl == JeanX:
            $ Girl.eyes = "psychic"
            ch_j "Quit it!."
            $ Girl.eyes = "squint"
        elif Girl == StormX:
            ch_s "Stop."
        elif Girl == JubesX:
            ch_v "Hey. . ."
        $ Girl.change_stat("love", 50, -3)
        $ Girl.change_stat("obedience", 50, 1)
        $ Girl.change_stat("inhibition", 30, 1)

    if "no_headpat" in Girl.daily_history:
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck(Girl, 300):
                    $ Girl.change_face("sexy", 1)
                    if Girl == RogueX:
                        ch_r "Heard that before. . ."
                    elif Girl == KittyX:
                        ch_k "Uh-huh."
                    elif Girl == EmmaX:
                        ch_e "I should hope not."
                    elif Girl == LauraX:
                        ch_l "Yeah, stop being weird."
                    elif Girl == JeanX:
                        ch_j "Ok then. . ."
                    elif Girl == StormX:
                        ch_s "Very well. . ."
                    elif Girl == JubesX:
                        ch_v "Well, cut it out."
                    $ Girl.change_stat("love", 80, 2)
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.eyes = "side"
                    if Girl == RogueX:
                        ch_r "Damned right. . ."
                    elif Girl == KittyX:
                        ch_k "It'd better not."
                    elif Girl == EmmaX:
                        "[EmmaX.name] silently glares at you."
                    elif Girl == LauraX:
                        ch_l "Uh-huh."
                    elif Girl == JeanX:
                        ch_j "You'd better not."
                    elif Girl == StormX:
                        ch_s "I should hope not. . ."
                    elif Girl == JubesX:
                        ch_v "Sure. . ."
                    $ Girl.change_stat("obedience", 20, 1)
            "You know you wanted it.":

                if ApprovalCheck(Girl, 400, "OI",Alt=[[EmmaX],600]) or ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                    $ Girl.change_face("normal", 1)
                    $ Girl.eyes = "squint"
                    if Girl == RogueX:
                        ch_r "I. . . maybe?"
                    elif Girl == KittyX:
                        ch_k "Maaaaybe.."
                    elif Girl == EmmaX:
                        ch_e "Hmph. . ."
                    elif Girl == LauraX:
                        ch_l "Um. . ."
                    elif Girl == JeanX:
                        ch_j "Um. . . ok. . ."
                    elif Girl == StormX:
                        ch_s "Well. . ."
                    elif Girl == JubesX:
                        ch_v "Hmm. . ."
                    $ Girl.change_stat("love", 60, -1)
                    $ Girl.change_stat("obedience", 30, 2)
                    $ Girl.change_stat("inhibition", 40, 2)
                else:
                    $ Girl.change_face("angry", 2)
                    $ Girl.eyes = "squint"
                    if Girl == RogueX:
                        ch_r "Wouldn't count on it."
                    elif Girl == KittyX:
                        ch_k "Um. . ."
                    elif Girl == EmmaX:
                        ch_e "What nonsense. . ."
                    elif Girl == LauraX:
                        ch_l "Did not!"
                    elif Girl == JeanX:
                        ch_j "You don't know me."
                    elif Girl == StormX:
                        ch_s "Then you do not know me."
                    elif Girl == JubesX:
                        ch_v "You wanna find out?"
                    $ Girl.blushing = 1
                    $ Girl.change_stat("love", 60, -3)
                    $ Girl.change_stat("obedience", 30, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
    else:


        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck(Girl, 850, "LI",Alt=[[EmmaX],1050]):
                    $ Girl.change_face("sexy", 1)
                    $ Count = 7
                    if Girl == RogueX:
                        "She tilts her head a bit."
                        ch_r "Mmmmm. . ."
                    elif Girl == KittyX:
                        "She leans into it."
                        ch_k "Purrrrr. . ."
                    elif Girl == EmmaX:
                        "She hesitates, but then slowly closes her eyes."
                        ch_e "Be grateful. I wouldn't let just anyone do this."
                        $ Count -= 2
                    elif Girl == LauraX:
                        "She leans into it."
                        ch_l "Mmmmm. . ."
                    elif Girl == JeanX:
                        ch_j "I always look cute. . ."
                    elif Girl == StormX:
                        ch_s "I suppose I did. . ."
                    elif Girl == JubesX:
                        ch_v "Always. . ."
                    $ Girl.change_stat("love", 80, 2)
                elif ApprovalCheck(Girl, 500, "LI",Alt=[[EmmaX],700]):
                    $ Girl.change_face("smile", 1)
                    $ Count = 5
                    if Girl == RogueX:
                        ch_r "Well, do go on. . ."
                    elif Girl == KittyX:
                        ch_k "Tell me something I don't know."
                    elif Girl == EmmaX:
                        ch_e "Just cute? I must be slipping."
                        $ Count -= 1
                    elif Girl == LauraX:
                        ch_l "I'm not cute."
                        ch_l "But continue."
                    elif Girl == JeanX:
                        ch_j "I always look cute. . ."
                    elif Girl == StormX:
                        ch_s "I suppose I did. . ."
                    elif Girl == JubesX:
                        ch_v "Sure. . ."
                    $ Girl.change_stat("love", 80, 2)
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.eyes = "side"
                    if Girl == RogueX:
                        ch_r "You're up ta somethin. . ."
                    elif Girl == KittyX:
                        ch_k "Yeah, right. Pull the other one."
                    elif Girl == EmmaX:
                        ch_e "You'll have to do better than that, [Girl.player_petname]. Much better."
                    elif Girl == LauraX:
                        ch_l "This cutie might bite your hand off."
                    elif Girl == JeanX:
                        ch_j "I always look cute. Look, don't touch."
                    elif Girl == StormX:
                        ch_s "I'm not sure about that. . ."
                    elif Girl == JubesX:
                        ch_v "Yeah, right."
                    $ Girl.change_stat("obedience", 20, 1)
                    $ Count = 1
            "You had a loose hair going on.":

                if ApprovalCheck(Girl, 700, "LI",Alt=[[EmmaX,JeanX],850]):
                    $ Girl.change_face("sexy", 1)
                    $ Count = 4
                    if Girl == RogueX:
                        ch_r "Oh? You'd best put it back then. . ."
                    elif Girl == KittyX:
                        ch_k "Loose hair? Me?"
                    elif Girl == EmmaX:
                        ch_e "A loose hair, you say? Perhaps you can help get it back under control."
                        $ Count += 1
                    elif Girl == LauraX:
                        ch_l "Oh? Whatever. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . ."
                    elif Girl == StormX:
                        ch_s "Oh? . ."
                    elif Girl == JubesX:
                        ch_v "Not with this style."
                    $ Girl.change_stat("love", 60, 1)
                    $ Girl.change_stat("inhibition", 40, 1)
                elif ApprovalCheck(Girl, 700):
                    $ Girl.change_face("normal")
                    $ Count = 3
                    if Girl == RogueX:
                        ch_r "Something's loose here. . ."
                    elif Girl == KittyX:
                        ch_k "A hair, right. . ."
                    elif Girl == EmmaX:
                        ch_e "A loose hair? Oh, [Girl.player_petname]. I would hope you'd be more original than that."
                    elif Girl == LauraX:
                        ch_l "A hair, right. . ."
                    elif Girl == JeanX:
                        ch_j "Seems fishy. . ."
                    elif Girl == StormX:
                        ch_s "Oh? . ."
                    elif Girl == JubesX:
                        ch_v "Not with this style."
                else:
                    $ Girl.change_face("angry", 1)
                    if Girl == RogueX:
                        ch_r "Ain't no reason to go messin with it."
                    elif Girl == KittyX:
                        ch_k "Uhuh, just.. just watch it, okay?"
                    elif Girl == EmmaX:
                        ch_e "I can handle something like that easily enough on my own."
                    elif Girl == LauraX:
                        ch_l "Uhuh, just don't touch me."
                    elif Girl == JeanX:
                        ch_j "That's not possible."
                    elif Girl == StormX:
                        ch_s "A likely tale . ."
                    elif Girl == JubesX:
                        ch_v "Not with this style."
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Count = 1
            "Are you sure you didn't enjoy that?":

                if ApprovalCheck(Girl, 850,Alt=[[EmmaX,JeanX],1000]):
                    $ Girl.change_face("sexy", 1)
                    $ Girl.eyes = "side"
                    if Girl == RogueX:
                        ch_r "Well, I suppose. . ."
                    elif Girl == KittyX:
                        ch_k "Hmmm.. maybe, maybe not."
                    elif Girl == EmmaX:
                        ch_e "I'll admit that much, at least."
                    elif Girl == LauraX:
                        ch_l "Well. . . yeah. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . ."
                    elif Girl == StormX:
                        ch_s "Hmm. . ."
                    elif Girl == JubesX:
                        ch_v "Well. . ."
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 30, 1)
                    $ Girl.change_stat("inhibition", 40, 1)
                    $ Count = 4
                elif ApprovalCheck(Girl, 500, "OI"):
                    $ Girl.change_face("normal", 1)
                    $ Count = 2
                    if Girl == RogueX:
                        ch_r "Not. . . really?"
                    elif Girl == KittyX:
                        ch_k "Well. . . I guess, maybe. . . nah, nope."
                    elif Girl == EmmaX:
                        ch_e "Ah. . . no, no. A lady must have some secrets."
                        $ Count += 1
                    elif Girl == LauraX:
                        ch_l "Well. . . I guess, maybe. . . no, quit it."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . nope."
                    elif Girl == StormX:
                        ch_s "I don't believe so. . ."
                    elif Girl == JubesX:
                        ch_v "Not so much."
                    $ Girl.change_stat("love", 60, -1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 30, 2)
                    $ Girl.change_stat("inhibition", 40, 2)
                else:
                    $ Girl.change_face("angry", 1)
                    $ Girl.eyes = "side"
                    if Girl == RogueX:
                        ch_r "Oh, I'm sure."
                    elif Girl == KittyX:
                        ch_k "Grrrr. . ."
                    elif Girl == EmmaX:
                        ch_e "If you'd tried that a few years ago.."
                    elif Girl == LauraX:
                        ch_l "Grrrr. . ."
                    elif Girl == JeanX:
                        ch_j "I'm pretty sure I didn't."
                    elif Girl == StormX:
                        ch_s "Definitely not."
                    elif Girl == JubesX:
                        ch_v "Nope."
                    $ Girl.change_stat("love", 60, -3)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 30, 3)
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ Count = 1
        while Count > 0 and Round >= 10:
            $ Count -= 1 if Count != 4 else 0
            $ Round -= 1
            menu:
                "Continue?"
                "Yes":
                    "You continue to hold your hand on top of [Girl.name]'s head, rubbing it softly."
                    if Count <= 0:

                        if ApprovalCheck(Girl, 800):
                            $ Girl.change_face("bemused", 2)
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("inhibition", 40, 2)
                            if Girl == RogueX:
                                ch_r "Hey, ok, that'll be fine. . ."
                            elif Girl == KittyX:
                                ch_k "Hey, okay, I think that's enough. . ."
                            elif Girl == EmmaX:
                                ch_e "I think. . . that will do."
                            elif Girl == LauraX:
                                ch_l "Ok, that's enough of that for now. . ."
                            elif Girl == JeanX:
                                ch_j "Ok, ok, enough of that."
                            elif Girl == StormX:
                                ch_s "Ok, you can stop now."
                            elif Girl == JubesX:
                                ch_v "Ok, that's good."
                            "She ducks out from under your hand."
                            $ Girl.change_face("bemused", 1)
                        else:
                            $ Girl.change_face("angry", 2)
                            $ Girl.change_stat("love", 60, -5)
                            $ Girl.change_stat("inhibition", 40, 3)
                            if Girl == RogueX:
                                ch_r "Enough's enough there."
                            elif Girl == KittyX:
                                ch_k "Ok, I think that's enough now. . ."
                            elif Girl == EmmaX:
                                ch_e "I think you've had your fun. . ."
                            elif Girl == LauraX:
                                ch_l "Ok, enough, enough. . ."
                            elif Girl == JeanX:
                                ch_j "Cut it out now."
                            elif Girl == StormX:
                                ch_s "Stop. Now."
                            elif Girl == JubesX:
                                ch_v "Ok, cut it out."
                            "She knocks your hand away."
                            $ Girl.change_face("angry", 1)
                    elif Count == 1:

                        if ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                            $ Girl.change_face("bemused", 1)
                            $ Girl.change_stat("love", 80, 1)
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("inhibition", 40, 2)
                            if Girl == RogueX:
                                ch_r "Um, you might wanna. . ."
                            elif Girl == KittyX:
                                ch_k "We should probably do something else. . ."
                            elif Girl == EmmaX:
                                if Taboo > 20:

                                    ch_e "We really shouldn't do this in public. . . I do have an image."
                                else:
                                    ch_e "Just be careful not to do that in public. . . I do have an image."
                            elif Girl == LauraX:
                                ch_l "We should probably do something else. . ."
                            elif Girl == JeanX:
                                ch_j "You should probably stop that."
                            elif Girl == StormX:
                                ch_s "Are you going to. . . ok then. . ."
                            elif Girl == JubesX:
                                ch_v "Maybe give it a rest."
                        else:
                            $ Girl.change_face("angry", 2)
                            $ Girl.change_stat("love", 60, -2)
                            $ Girl.change_stat("obedience", 60, 2)
                            $ Girl.change_stat("obedience", 30, 2)
                            if Girl == RogueX:
                                ch_r "You'd best cut that out. . ."
                            elif Girl == KittyX:
                                ch_k "This [Girl.name] has claws, you know."
                            elif Girl == EmmaX:
                                ch_e "Don't push your luck too far."
                            elif Girl == LauraX:
                                ch_l "You aiming to lose that hand?"
                            elif Girl == JeanX:
                                ch_j "You should probably stop that."
                            elif Girl == StormX:
                                ch_s "That is enough."
                            elif Girl == JubesX:
                                ch_v "Ok, cut it out."
                    else:

                        if ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                            $ Girl.change_face("bemused", 2,Eyes="closed")
                            if Count > 5:
                                $ Girl.change_stat("love", 90, 1)
                                $ Girl.change_stat("love", 70, 1)
                                $ Girl.change_stat("obedience", 50, 1)
                            if Girl == RogueX:
                                ch_r "Uhuhh. . ."
                            elif Girl == KittyX:
                                ch_k "Mmmmm. . ."
                                "She's practically purring."
                            elif Girl == EmmaX:
                                ch_e "Mmmmm. . . you really shouldn't. . ."
                                "She does seem to be leaning into it. . ."
                            elif Girl == JeanX:
                                ch_j "Hmmm. . ."
                            else:
                                Girl.voice "Mmmmm. . ."
                        else:
                            $ Girl.change_face("angry", 1)
                            $ Girl.change_stat("love", 60, -1)
                            $ Girl.change_stat("obedience", 50, 2)
                            $ Girl.change_stat("obedience", 30, 2)
                            $ Girl.change_stat("inhibition", 40, 2)
                            if Girl == EmmaX:
                                ch_e "Er. . ."
                            else:
                                Girl.voice "Um. . ."
                            $ Count -= 1 if Count > 2 else 0
                "No":
                    $ Count = 0
    $ Count = 0
    $ Girl.recent_history.append("headpat")
    $ Girl.daily_history.append("headpat")
    return




label AskPanties(Girl=0, Store=0):

    if Girl not in all_Girls:
        return
    $ Store = approval_bonus
    $ Line = 0
    if not Girl.underwear or Girl.underwear == "shorts":
        if ApprovalCheck(Girl, 900):
            $ Girl.change_face("sexy", 1)
            $ Girl.change_stat("lust", 80, 5)
            $ Girl.change_stat("lust", 60, 5)
            $ Girl.change_stat("lust", 40, 10)
            $ Girl.change_stat("inhibition", 60, 5)
            $ Girl.change_stat("inhibition", 30, 10)
            if Girl == RogueX:
                ch_r "I'm not wearing any."
            elif Girl == KittyX:
                ch_k "I might. . . if I had any. . ."
            elif Girl == EmmaX:
                ch_e "That. . . isn't exactly an option."
            elif Girl == LauraX:
                ch_l "I'm not wearing any."
            elif Girl == JeanX:
                ch_j "Well I don't have any on."
            elif Girl == StormX:
                ch_s "I'm not wearing any at the moment."
            elif Girl == JubesX:
                ch_v "I might, if I were weaing any."
        elif Girl.top == "towel" or not Girl.legs:
            $ Girl.change_face("bemused", 2)
            if Girl == RogueX:
                ch_r "I think you can see I can't."
            elif Girl == KittyX:
                ch_k "How do you expect I could do that?"
            elif Girl == EmmaX:
                ch_e "I think you can see that I don't have any. . ."
            elif Girl == LauraX:
                ch_l "Did you think I was wearing any?"
            elif Girl == JeanX:
                ch_j "Why would I have those on?"
            elif Girl == StormX:
                ch_s "Why would you think I was wearing any?"
            elif Girl == JubesX:
                ch_v "Where would I find any?"
        else:
            $ Girl.change_face("bemused", 2, Eyes="side")
            $ Girl.change_stat("lust", 80, 5)
            $ Girl.change_stat("lust", 60, 5)
            $ Girl.change_stat("lust", 40, 10)
            $ Girl.change_stat("inhibition", 60, 5)
            if Girl == RogueX:
                ch_r "I definitely have some on, but you can't have them."
            elif Girl == KittyX:
                ch_k "Um, no. Not right now. For. . . reasons."
            elif Girl == EmmaX:
                ch_e "Hrm, I'm afraid not."
            elif Girl == LauraX:
                ch_l "I'm not wearing any at the moment."
            elif Girl == JeanX:
                ch_j "Um, no. . ."
            elif Girl == StormX:
                ch_s "I'm not wearing any at the moment."
            elif Girl == JubesX:
                ch_v "I, um, can't right now."
    else:

        if Girl.SeenPussy and ApprovalCheck(Girl, 500):

            $ approval_bonus += 15
        elif Girl.SeenPanties and ApprovalCheck(Girl, 500):

            $ approval_bonus += 5
        if "exhibitionist" in Girl.Traits:
            $ approval_bonus += (Girl.Taboo*5)
        if Girl in Player.Harem or ("sex friend" in Girl.player_petnames and not Taboo):
            $ approval_bonus += 10
        if "no_bottomless" in Girl.recent_history:
            $ approval_bonus -= 20

        $ Line = 0
        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:

            if ApprovalCheck(Girl, 1000, "OI", TabM = 5) or "exhibitionist" in Girl.Traits:
                $ Line = "here"
            elif ApprovalCheck(Girl, 900, TabM = 5):
                $ Line = "change"
        elif Girl.PantsNum() == 5:

            if ApprovalCheck(Girl, 600, "OI", TabM = 5) or "exhibitionist" in Girl.Traits:
                $ Line = "here"
            elif ApprovalCheck(Girl, 1100, TabM = 5):
                $ Line = "change"
        else:
            if ApprovalCheck(Girl, 1200, TabM = 5) or "exhibitionist" in Girl.Traits:
                $ Line = "here"

        if Girl == StormX and Line == "change":

            if not Taboo or StormX in Rules:
                $ Line = "here"

        if Girl == KittyX and Line:

            $ Girl.change_stat("lust", 60, 2)
            $ Girl.change_stat("obedience", 60, 4)
            $ Girl.change_stat("inhibition", 60, 4)
            call Remove_Panties (Girl)
            if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 60, 5)
                $ Girl.change_stat("inhibition", 60, 5)
            elif Girl.PantsNum() == 5:
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("obedience", 60, 4)
                $ Girl.change_stat("inhibition", 60, 4)
            else:
                $ Girl.change_stat("lust", 60, 7)
                $ Girl.change_stat("obedience", 60, 6)
                $ Girl.change_stat("inhibition", 60, 8)
            $ approval_bonus = Store
            $ Line = 0
            return

        if Line == "here":

            $ Girl.change_face("sly")
            if Girl.PantsNum() == 5:

                $ Girl.change_stat("obedience", 60, 4)
                $ Girl.change_stat("inhibition", 60, 4)
            else:
                $ Girl.change_stat("obedience", 60, 6)
                $ Girl.change_stat("inhibition", 60, 6)

            $ Girl.change_stat("lust", 60, 5)
            call Remove_Panties (Girl)

            if Girl.Taboo:
                $ Girl.change_stat("lust", 60, 5)
                if "exhibitionist" in Girl.Traits:
                    $ Girl.change_stat("lust", 80, 5)
                    $ Girl.change_stat("lust", 200, 5)
                $ Girl.change_stat("obedience", 80, 10)
                $ Girl.change_stat("inhibition", 80, 10)

        elif Line:

            if not Taboo and Girl != StormX:

                $ Girl.change_face("bemused", 1)
                if Girl == RogueX:
                    ch_r "Could you head out for a 'sec while I change?"
                elif Girl == KittyX:
                    ch_k "Could you turn around?"
                elif Girl == EmmaX:
                    ch_e "I would appreciate some privacy while I change."
                elif Girl == LauraX:
                    ch_l "Could you turn around?"
                elif Girl == JeanX:
                    ch_j "Hey, a little privacy?"
                elif Girl == JubesX:
                    ch_v "Um, turn around or something."
                menu:
                    extend ""
                    "OK.":
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_face("smile", 1)
                        if Girl == RogueX:
                            ch_r "I 'preciate it, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Thanks, [Girl.player_petname]."
                        elif Girl == EmmaX:
                            ch_e "Thank you, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "Thanks."
                        elif Girl == JeanX:
                            ch_j "Cool."
                        elif Girl == JubesX:
                            ch_v "K."
                        $ Girl.change_face("sly", 1)
                        $ Girl.change_stat("lust", 60, 2)
                        $ Girl.change_stat("obedience", 60, 4)
                        $ Girl.change_stat("inhibition", 60, 4)
                        show blackscreen onlayer black
                        "You exit the room for a minute"
                        hide blackscreen onlayer black
                        $ Girl.daily_history.append("pantyless")
                        $ Girl.change_outfit()
                        call OutfitShame (Girl, 20)
                        "When you return, she quietly hands you her balled up panties."
                        $ Line = 0
                    "And miss the show?":

                        if ApprovalCheck(Girl, 1000, "LI"):
                            $ Girl.change_stat("lust", 70, 5)
                            $ Girl.change_stat("obedience", 60, 5)
                            $ Girl.change_stat("inhibition", 60, 5)
                            $ Girl.change_face("sly", 1)
                            if Girl == RogueX:
                                ch_r "Ok, fine."
                            elif Girl == KittyX:
                                ch_k "Oh, you think there's a show?"
                            elif Girl == EmmaX:
                                ch_e "How precious."
                            elif Girl == LauraX:
                                ch_l "Oh, you'd like to watch?"
                            elif Girl == JeanX:
                                ch_j "Oh, here for a show. . ."
                            elif Girl == JubesX:
                                ch_v "Well. . ."
                        else:
                            $ Girl.change_face("angry", 1)
                            $ Girl.change_stat("love", 90, -5)
                            $ Girl.change_stat("obedience", 60, -3)
                            $ Girl.change_stat("inhibition", 60, 5)
                            if Girl == RogueX:
                                ch_r "Then I guess there'll be no show to see, [Girl.player_petname]."
                            elif Girl == KittyX:
                                ch_k "Apparently so."
                            elif Girl == EmmaX:
                                ch_e "What show would that be, [Player.name]?"
                            elif Girl == LauraX:
                                ch_l "Yes."
                            elif Girl == JeanX:
                                ch_j "There isn't any show here."
                            elif Girl == JubesX:
                                ch_v "Nope."
                            $ Line = 0
                    "Nope, I'm staying.":

                        if ApprovalCheck(Girl, 600, "OI"):
                            $ Girl.change_face("perplexed", 1)
                            $ Girl.change_stat("lust", 70, 5)
                            $ Girl.change_stat("obedience", 60, 10)
                            $ Girl.change_stat("inhibition", 60, 5)
                            if Girl == RogueX:
                                ch_r "If you insist."
                            elif Girl == KittyX:
                                ch_k "Ok."
                            elif Girl == EmmaX:
                                ch_e "If you must."
                            elif Girl == LauraX:
                                ch_l "Ok."
                            elif Girl == JeanX:
                                ch_j "Ok, fine."
                            elif Girl == JubesX:
                                ch_v ". . . K."
                            $ Girl.change_face("normal")
                        else:
                            $ Girl.change_face("angry", 1)
                            $ Girl.change_stat("love", 90, -10)
                            $ Girl.change_stat("obedience", 60, -5)
                            $ Girl.change_stat("inhibition", 60, 5)
                            if Girl == RogueX:
                                ch_r "Then I guess I'm not doing anything."
                            elif Girl == KittyX:
                                ch_k "Huh, maybe[Girl.like]have a little respect?"
                            elif Girl == EmmaX:
                                ch_e "Then I suppose we're done here."
                            elif Girl == LauraX:
                                ch_l "I think that's rude under the circumstances."
                            elif Girl == JeanX:
                                ch_j "Fine, you get nothing."
                            elif Girl == JubesX:
                                ch_v "Then forget it."
                            $ Line = 0
                if Line:

                    $ Girl.change_face("sly", 1)
                    if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:
                        $ Girl.change_stat("lust", 60, 5)
                        $ Girl.change_stat("obedience", 60, 5)
                        $ Girl.change_stat("inhibition", 60, 5)
                    elif Girl.PantsNum() == 5:
                        $ Girl.change_stat("lust", 60, 5)
                        $ Girl.change_stat("obedience", 60, 4)
                        $ Girl.change_stat("inhibition", 60, 4)
                    call Remove_Panties (Girl)
            else:


                $ Girl.change_face("sly", 1)
                $ Girl.change_stat("lust", 60, 2)
                $ Girl.change_stat("obedience", 60, 4)
                $ Girl.change_stat("inhibition", 60, 4)
                $ Girl.location = "hold"
                call set_the_scene
                "[Girl.name] nods and leaves for a minute."
                $ Girl.daily_history.append("pantyless")
                $ Girl.change_outfit()
                call OutfitShame (Girl, 20)
                $ Girl.location = bg_current
                call set_the_scene
                "She returns and quietly hands you her balled up panties."
        else:

            $ Girl.change_face("angry", 2)
            if not ApprovalCheck(Girl, 500):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("love", 90, -10)
                $ Girl.change_stat("obedience", 60, 3)
                $ Girl.change_stat("inhibition", 60, 3)
                if Girl == RogueX:
                    ch_r "I can't believe you would even ask me something like that!"
                elif Girl == KittyX:
                    ch_k "You think I'd do that?"
                elif Girl == EmmaX:
                    ch_e "Out of the question."
                elif Girl == LauraX:
                    ch_l "Why do you think I would?"
                elif Girl == JeanX:
                    ch_j "I think I'll keep them on, thanks."
                elif Girl == StormX:
                    ch_s "I'm wearing them for a reason."
                elif Girl == JubesX:
                    ch_v "No thanks."
                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            elif not ApprovalCheck(Girl, 500, TabM = 5):
                $ Girl.change_stat("lust", 60, 5)
                $ Girl.change_stat("love", 90, -5)
                $ Girl.change_stat("obedience", 60, 5)
                $ Girl.change_stat("inhibition", 60, 5)
                if Girl == RogueX:
                    ch_r "I can't believe you would even ask me that here!"
                elif Girl == KittyX:
                    ch_k "I mean, here?"
                elif Girl == EmmaX:
                    ch_e "Look around you and have some sense."
                elif Girl == LauraX:
                    ch_l "In public?"
                elif Girl == JeanX:
                    ch_j "I can't. . . here."
                elif Girl == StormX:
                    ch_s "I don't think that would be appropriate here."
                elif Girl == JubesX:
                    ch_v "Um, not out here."
                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
            else:
                $ Girl.change_face("bemused", 2)
                $ Girl.change_stat("lust", 60, 3)
                $ Girl.change_stat("inhibition", 60, 1)
                if Girl.Taboo:
                    $ Girl.change_stat("inhibition", 60, 2)
                    if Girl == RogueX:
                        ch_r "I'm sorry, [Girl.player_petname], I'm not ready yet."
                    elif Girl == KittyX:
                        ch_k "Maybe you'll earn that, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "You know I would, [Girl.player_petname], but not here."
                    elif Girl == LauraX:
                        ch_l "Maybe someday, [Girl.player_petname]."
                    elif Girl == JeanX:
                        ch_j "Not around here."
                    elif Girl == StormX:
                        ch_s "I don't think that would be appropriate here."
                    elif Girl == JubesX:
                        ch_v "Um, not out here."
                else:
                    $ Girl.change_face("perplexed")
                    $ Girl.change_stat("obedience", 60, -2)
                    if Girl == RogueX:
                        ch_r "Nah, not around you, at least."
                    elif Girl == KittyX:
                        ch_k "You're nasty, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "You'll have to work up to that, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "Why would you want that?"
                    elif Girl == JeanX:
                        ch_j "Gross."
                    elif Girl == StormX:
                        ch_s "Of what interest are they to you?"
                    elif Girl == JubesX:
                        ch_v "I don't wanna."
            $ Girl.blushing = 1
    $ approval_bonus = Store
    $ Line = 0
    return

label Remove_Panties(Girl=0, Type=0, Store=0, Store2=0):
    if Girl not in all_Girls:
        return
    if Girl == KittyX:
        $ Girl.underwear = 0
        $ Girl.change_face("bemused")
        if Girl.PantsNum() >= 6:
            "[Girl.name] looks around, reaches into her pocket, and tugs her panties out."
        elif Girl.PantsNum() == 5:
            "[Girl.name] looks around, reaches into her skirt, and pulls her panties out."
        elif Girl.HoseNum() >= 5:
            "[Girl.name] looks around, reaches through her [Girl.hose], and pulls her panties out."
        else:
            "[Girl.name] looks around and pulls her panties off."

        $ Girl.change_face("sexy")
        "She hands them to you with a smirk."

        if not Girl.legs and Girl.HoseNum() <= 10:
            call expression Girl.Tag + "_First_Bottomless"

        $ Girl.daily_history.append("pantyless")
        $ Girl.change_outfit()
        call OutfitShame (Girl, 20)
        return
    elif Girl == JeanX and Girl.PantsNum() == 5 and not ApprovalCheck(Girl, 400, "L"):
        $ Girl.underwear = 0
        $ Girl.change_face("bemused",Eyes="psychic")
        "You notice some movement as her panties shoot down her legs and she quickly steps out of them."
        "They scoot along near the ground and then up to your hand."
        $ Girl.change_face("sexy")

        if not Girl.legs and Girl.HoseNum() <= 10:
            call expression Girl.Tag + "_First_Bottomless"

        $ Girl.daily_history.append("pantyless")
        $ Girl.change_outfit()
        call OutfitShame (Girl, 20)
        return

    $ Store = Girl.legs
    $ Store2 = Girl.hose
    if Girl.PantsNum() >= 6:

        $ Girl.legs = 0
        $ Type = 1
    elif Girl.PantsNum() == 5:

        $ Girl.Upskirt = 1
        $ Type = 2
    if Girl.HoseNum() >= 5:
        $ Girl.hose = 0
        $ Type = 3 if Type == 2 else 4

    $ Girl.underwear = 0

    if Girl.Taboo:
        if Type == 1:
            "[Girl.name] looks around, but pulls her pants clean off and her panties with them."
        elif Type == 3:
            "[Girl.name] looks around, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
        elif Type == 2:
            "[Girl.name] looks around, reaches under her skirt, and pulls her panties down."
        elif Type == 4:
            "[Girl.name] looks around, but pulls her [Store2] clean off and her panties with them."
        else:
            "[Girl.name] looks around, and pulls her panties down."
    else:
        if Type == 1:
            "[Girl.name] glances at you and pulls her pants clean off and her panties with them."
        elif Type == 3:
            "[Girl.name] glances at you, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
        elif Type == 2:
            "[Girl.name] glances at you, reaches under her skirt, and pulls her panties down."
        elif Type == 4:
            "[Girl.name] glances at you and pulls her [Store2] clean off and her panties with them."
        else:
            "[Girl.name] glances at you and pulls her panties off."

    $ Girl.legs = Store
    $ Girl.hose = Store2
    if Girl.PantsNum() > 6:

        "She hands you the panties and then pulls her pants back on."
    elif Girl.PantsNum() == 6 or Girl.underwear == "shorts":

        "She hands you the panties and then pulls her shorts back up."
        $ Girl.Upskirt = 0
    elif Girl.PantsNum() == 5 and Girl.HoseNum() >= 5:

        "She hands you the panties and then pulls her [Girl.hose] back on and her skirt back down."
        $ Girl.Upskirt = 0
    elif Girl.PantsNum() == 5:

        "She hands you the panties and then pulls her skirt back down."
        $ Girl.Upskirt = 0
    elif Girl.HoseNum() >= 5:

        "She hands you the panties and then pulls her [Girl.hose] back on."
    else:
        "[Girl.name] hands them to you in a ball."
    call expression Girl.Tag + "_First_Bottomless" pass (1)

    $ Girl.daily_history.append("pantyless")
    $ Girl.change_outfit()
    call OutfitShame (Girl, 20)
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


        if Chr.player_favorite_action and ApprovalCheck(Chr, 1500):
            if Chr.player_favorite_action == "anal":
                $ ATemp += 20
            elif Chr.player_favorite_action == "sex":
                $ PTemp += 20
            elif Chr.player_favorite_action == "blowjob":
                $ BTemp += 20
            elif Chr.player_favorite_action == "titjob":
                $ TTemp += 20
            elif Chr.player_favorite_action == "foot":
                $ XTemp += 20
            elif Chr.player_favorite_action == "handjob":
                $ HTemp += 20
            else:
                $ FTemp += 20
        elif Chr.player_favorite_action and ApprovalCheck(Chr, 800):
            if Chr.player_favorite_action == "anal":
                $ ATemp += 5
            elif Chr.player_favorite_action == "sex":
                $ PTemp += 5
            elif Chr.player_favorite_action == "blowjob":
                $ BTemp += 5
            elif Chr.player_favorite_action == "titjob":
                $ TTemp += 5
            elif Chr.player_favorite_action == "foot":
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
            $ Temp = "foot"
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
        if not Player.Inventory:
            "You don't have anything to give her."
            return
        menu:
            "What would you like to give her?"
            "Toys and Books":
                menu:
                    "Give her a dildo." if "dildo" in Player.Inventory:

                        if "dildo" not in Girl.Inventory:
                            "You give [Girl.name] the dildo."
                            $ Girl.blushing = 1
                            $ Girl.ArmPose = 2
                            $ Girl.held_item = "dildo"
                            if ApprovalCheck(Girl, 800):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove("dildo")
                                $ Girl.Inventory.append("dildo")
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
                            elif ApprovalCheck(Girl, 500):
                                $ Girl.change_face("confused")
                                $ Player.Inventory.remove("dildo")
                                $ Girl.Inventory.append("dildo")
                                if Girl != EmmaX:
                                    $ Girl.change_stat("love", 200, 10)
                                    $ Girl.change_stat("obedience", 200, 10)
                                    $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == RogueX:
                                    ch_r "Huh, well I guess I can find a place for it. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("surprised")
                                    ch_r "I- I mean. . . I'll just put it away."
                                elif Girl == KittyX:
                                    ch_k "I don't know what. . ."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("surprised")
                                    ch_k "Oh!"
                                    ch_k "Oh. . . I'll just[Girl.like]put it away."
                                elif Girl == EmmaX:
                                    ch_e "This is not an appropriate gift from a student. . ."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("sadside",1)
                                    ch_e "Hm. . ."
                                    $ Girl.change_stat("love", 200, 10)
                                    $ Girl.change_stat("obedience", 200, 10)
                                    $ Girl.change_stat("inhibition", 200, 10)
                                    $ Girl.change_face("sly")
                                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh, you're a weird gift giver."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("smile")
                                    ch_l "It's very thoughtful though."
                                elif Girl == JeanX:
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    ch_j "Well we know where your mind it at."
                                    $ Girl.change_face("smile")
                                    ch_j "I guess I should be flattered. . ."
                                elif Girl == StormX:
                                    if StormX not in Rules:
                                        $ Girl.change_face("sadside",1)
                                        ch_s "I don't know that I should accept this from a student. . ."
                                    $ Girl.change_stat("lust", 89, 5)
                                    $ Girl.change_stat("lust", 89, 10)
                                    ch_s "Hm. . ."
                                    $ Girl.change_face("sly")
                                    ch_s "Thank you for the thought. . ."
                                elif Girl == JubesX:
                                    ch_v "I guess I have some use for it. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("surprised")
                                    ch_v "I- I mean. . . decorative."
                                $ Girl.change_face("bemused")
                            elif "offered gift" in Girl.daily_history:
                                $ Girl.change_face("angry")
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
                                $ Girl.change_face("angry")
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
                        elif Girl.Inventory.count("dildo") == 1:
                            $ Player.Inventory.remove("dildo")
                            $ Girl.Inventory.append("dildo")
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

                    "Give her the vibrator." if "vibrator" in Player.Inventory:

                        if "vibrator" not in Girl.Inventory:
                            "You give [Girl.name] the Shocker Vibrator."
                            $ Girl.blushing = 1
                            $ Girl.ArmPose = 2
                            $ Girl.held_item = "vibrator"
                            if ApprovalCheck(Girl, 700):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove("vibrator")
                                $ Girl.Inventory.append("vibrator")
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
                                    $ Girl.change_face("sly")
                                    ch_e "I'm sure I can put this to good use. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("sly")
                                    ch_l "-some kind of sex thing, huh. . ."
                                elif Girl == JeanX:
                                    ch_j "Oh, nifty."
                                elif Girl == StormX:
                                    ch_s "Oh!. . . oooohhh."
                                elif Girl == JubesX:
                                    ch_v "Oh, this could be nice. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            elif ApprovalCheck(Girl, 400):
                                $ Girl.change_face("confused")
                                $ Player.Inventory.remove("vibrator")
                                $ Girl.Inventory.append("vibrator")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == RogueX:
                                    ch_r "I guess I can use this to work the kinks out. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("surprised")
                                    ch_r "Muscle knots, I mean!"
                                elif Girl == KittyX:
                                    ch_k "I've heard these are very relaxing. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("surprised")
                                    ch_k "-for my back!"
                                elif Girl == EmmaX:
                                    ch_e "How very thoughtful of you. . ."
                                    $ Girl.change_stat("lust", 89, 10)
                                    $ Girl.change_face("sly")
                                    ch_e "A back massager, I assume. . ."
                                elif Girl == LauraX:
                                    ch_l "This is. . . [[bzzzt]- "
                                    $ Girl.change_face("sly")
                                    $ Girl.change_stat("lust", 89, 10)
                                    ch_l "-oooh. . ."
                                elif Girl == JeanX:
                                    ch_j "Huh. Ok."
                                elif Girl == StormX:
                                    ch_s "Oh, something for exercise purposes. . ."
                                elif Girl == JubesX:
                                    ch_v "Thanks, my, uh, back's been killing me. . ."
                                $ Girl.change_face("bemused", 1)
                            elif "offered gift" in Girl.daily_history:
                                $ Girl.change_face("angry")
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
                                $ Girl.change_face("angry")
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

                    "Give her a butt plug." if "buttplug" in Player.Inventory:
                        if "buttplug" not in Girl.Inventory:
                            "You give [Girl.name] the butt plug."
                            $ Player.Inventory.remove("buttplug")
                            $ Girl.Inventory.append("buttplug")
                        else:
                            "She already has enough of those."

                    "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in Player.Inventory:

                        if "Dazzler and Longshot" not in Girl.Inventory:
                            "You give [Girl.name] the book."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 600, "L"):
                                $ Girl.change_face("smile")
                                if Girl == RogueX:
                                    ch_r "Oh, I've heard of this one, very romantic!"
                                elif Girl == KittyX:
                                    ch_k "Oh, this one's so sweet!"
                                elif Girl == EmmaX:
                                    $ Girl.change_face("angry")
                                    ch_e "Is this the type of thing you expect from me. . ."
                                    $ Girl.change_face("sadside", Mouth="lipbite")
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
                                $ Girl.change_face("confused")
                                if Girl == RogueX:
                                    ch_r "Hmph, well I guess i've heard good things about it, I'll give it a shot."
                                elif Girl == KittyX:
                                    ch_k "Hm, worth the read I guess."
                                elif Girl == EmmaX:
                                    $ Girl.change_face("angry")
                                    ch_e "I don't exactly read this dime store trash. . ."
                                    $ Girl.change_face("sadside", Mouth="lipbite")
                                    ch_e "but I will take it. . ."
                                elif Girl == LauraX:
                                    ch_l "Huh. Is there a movie?"
                                elif Girl == JeanX:
                                    ch_j "What are you implying?"
                                elif Girl == StormX:
                                    ch_s "I did enjoy the film. . ."
                                elif Girl == JubesX:
                                    ch_v "Are you saying I look like her?"
                                $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("Dazzler and Longshot")
                            $ Girl.Inventory.append("Dazzler and Longshot")
                            $ Girl.change_stat("love", 200, 50)
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."

                    "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in Player.Inventory:

                        if "256 Shades of Grey" not in Girl.Inventory:
                            "You give [Girl.name] the book."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 500, "O"):
                                $ Girl.change_face("bemused")
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
                                $ Girl.change_face("confused")
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
                                $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("256 Shades of Grey")
                            $ Girl.Inventory.append("256 Shades of Grey")
                            $ Girl.change_stat("obedience", 200, 50,Alt=[[JeanX],200,10])
                        else:
                            if Girl == EmmaX:
                                ch_e "You're repeating yourself."
                            else:
                                Girl.voice "I already have one of those."

                    "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in Player.Inventory:

                        if "Avengers Tower Penthouse" not in Girl.Inventory:
                            "You give [Girl.name] the book."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 500, "I"):
                                $ Girl.change_face("bemused")
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
                                $ Girl.change_face("confused")
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
                                $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("Avengers Tower Penthouse")
                            $ Girl.Inventory.append("Avengers Tower Penthouse")
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
                    "Give her the green nighty." if Girl.Tag + " nighty" in Player.Inventory:

                        if "nighty" not in Girl.Inventory:
                            "You give [Girl.name] the nighty."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 600):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " nighty")
                                $ Girl.Inventory.append("nighty")
                                $ Girl.change_stat("love", 200, 40)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 30)
                                ch_r "I bet I'd look good in this. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            else:
                                $ Girl.change_face("confused")
                                $ Player.Inventory.remove(Girl.Tag + " nighty")
                                $ Girl.Inventory.append("nighty")
                                $ Girl.change_stat("love", 200, 30)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)
                                ch_r "Well, it's a little revealing, but still pretty cute."
                                $ Girl.change_face("bemused")
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the corset." if Girl.Tag + " corset" in Player.Inventory:

                        if "corset" not in Girl.Inventory:
                            "You give [Girl.name] the corset."
                            if ApprovalCheck(Girl, 1000):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " corset")
                                $ Girl.Inventory.append("corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == LauraX:
                                    ch_l "I'd look good in this, right?"
                                elif Girl == JeanX:
                                    ch_j "Ok, I can get into this one. . ."
                                $ Girl.change_stat("lust", 89, 10)
                            elif ApprovalCheck(Girl, 700) or Girl == JeanX:
                                $ Girl.change_face("confused",1)
                                $ Player.Inventory.remove(Girl.Tag + " corset")
                                $ Girl.Inventory.append("corset")
                                $ Girl.change_stat("love", 200, 15)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 10)
                                if Girl == LauraX:
                                    ch_l "This is. . . kinda cool. . ."
                                elif Girl == JeanX:
                                    ch_j "Thanks?"
                                $ Girl.change_face("bemused",1)
                            elif ApprovalCheck(Girl, 600):
                                $ Girl.change_face("confused",2)
                                $ Player.Inventory.remove(Girl.Tag + " corset")
                                $ Girl.Inventory.append("corset")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 15)
                                $ Girl.change_stat("inhibition", 200, 15)
                                if Girl == LauraX:
                                    ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                $ Girl.change_face("bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("angry",2)
                                if Girl == LauraX:
                                    ch_l "I just told you no."
                            else:
                                $ Girl.change_face("angry",2)
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
                                $ Girl.blushing = 1
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the lace corset." if Girl.Tag + " lace corset" in Player.Inventory:

                        if "lace corset" not in Girl.Inventory:
                            "You give [Girl.name] the lace corset."
                            if ApprovalCheck(Girl, 1200):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                $ Girl.Inventory.append("lace corset")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 20)
                                ch_l "You think this'd look good on me?"
                                $ Girl.change_stat("lust", 89, 10)
                            elif ApprovalCheck(Girl, 1000):
                                $ Girl.change_face("confused",1)
                                $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                $ Girl.Inventory.append("lace corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 30)
                                $ Girl.change_stat("inhibition", 200, 15)
                                ch_l "This is. . . kinda flimsy. . ."
                                $ Girl.change_face("bemused",1)
                            elif ApprovalCheck(Girl, 800):
                                $ Girl.change_face("confused",2)
                                $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                $ Girl.Inventory.append("lace corset")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 25)
                                ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                $ Girl.change_face("bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("angry",2)
                                ch_l "I just told you no."
                            else:
                                $ Girl.change_face("angry",2)
                                $ Girl.change_stat("love", 50, -10)
                                $ Girl.change_stat("obedience", 20, 10)
                                $ Girl.change_stat("inhibition", 20, 20)
                                if "no_gift_panties" in Girl.daily_history:
                                    ch_l "I don't want this either."
                                else:
                                    ch_l "You have too much time on your hands."
                                $ Girl.change_stat("lust", 89, 5)
                                $ Girl.blushing = 1
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the lace bra." if Girl.Tag + " lace_bra" in Player.Inventory:

                        if "lace_bra" not in Girl.Inventory:
                            "You give [Girl.name] the lace bra."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 1000) or Girl == JeanX:
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " lace_bra")
                                $ Girl.Inventory.append("lace_bra")
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
                            elif ApprovalCheck(Girl, 700,Alt=[[EmmaX],600]):
                                $ Girl.change_face("confused")
                                $ Player.Inventory.remove(Girl.Tag + " lace_bra")
                                $ Girl.Inventory.append("lace_bra")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)
                                if Girl == RogueX:
                                    ch_r "I don't know that I'd wear this out, but maybe in private."
                                elif Girl == KittyX:
                                    ch_k "This is. . . see-through. . ."
                                    ch_k "I don't know why you'd give me this, it's not like I'd wear it. . ."
                                elif Girl == EmmaX:
                                    if ApprovalCheck(Girl, 700):
                                        ch_e "I'm not exactly running low on this sort of thing. . ."
                                    else:
                                        ch_e "This is an . . . unusual gift from a student. . ."
                                elif Girl == StormX:
                                    ch_s "It is not that I do not appreciate it, but. . ."
                                elif Girl == JubesX:
                                    ch_v "It's not my usual style. . ."
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("angry",2)
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
                                $ Girl.change_face("angry")
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
                            $ Girl.change_face("bemused")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the lace panties." if Girl.Tag + " lace_panties" in Player.Inventory:

                        if "lace_panties" not in Girl.Inventory:
                            "You give [Girl.name] the lace panties."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 1100) or Girl == JeanX:
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " lace_panties")
                                $ Girl.Inventory.append("lace_panties")
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
                            elif ApprovalCheck(Girl, 800):
                                $ Girl.change_face("confused")
                                $ Player.Inventory.remove(Girl.Tag + " lace_panties")
                                $ Girl.Inventory.append("lace_panties")
                                $ Girl.change_stat("love", 200, 25)
                                $ Girl.change_stat("obedience", 200, 20)
                                $ Girl.change_stat("inhibition", 200, 20)
                                if Girl == RogueX:
                                    ch_r "These are a bit flimsy. . ."
                                elif Girl == KittyX:
                                    ch_k "I- I wouldn't wear something like these. . ."
                                    $ KittyX.change_face("bemused",1)
                                    ch_k "But I'll hold on to them. . ."
                                elif Girl == EmmaX:
                                    ch_e "This is an. . . unsual gift."
                                    $ EmmaX.change_face("sly",1)
                                    ch_e "But I'll hold on to them. . ."
                                elif Girl == LauraX:
                                    ch_l "I don't think I'd wear these. . ."
                                    $ Girl.change_face("bemused",1)
                                    ch_l "But I might need to do laundry. . ."
                                elif Girl == StormX:
                                    ch_s "I suppose I could always use another pair. . ."
                                elif Girl == JubesX:
                                    ch_v "A little. . . intimate. . ."
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("angry",2)
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
                                $ Girl.change_face("angry")
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
                            $ Girl.change_face("bemused")
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the stockings and garterbelt." if "stockings_and_garterbelt" in Player.Inventory:

                        if "stockings_and_garterbelt" not in Girl.Inventory:
                            "You give [Girl.name] the stockings."
                            $ Girl.blushing = 1
                            $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("stockings_and_garterbelt")
                            $ Girl.Inventory.append("stockings_and_garterbelt")
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

                    "Give her the pantyhose." if Girl.Tag + "_pantyhose" in Player.Inventory:

                        if "pantyhose" not in Girl.Inventory:
                            "You give [Girl.name] the pantyhose."
                            $ Girl.change_face("bemused")
                            $ Player.Inventory.remove(Girl.Tag + "_pantyhose")
                            $ Girl.Inventory.append("pantyhose")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)
                            Girl.voice "These are lovely. . ."
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the knee stockings." if "knee" in Player.Inventory and Girl == KittyX:

                        if "knee" not in Girl.Inventory:
                            "You give [Girl.name] the knee stockings."
                            $ Girl.blushing = 1
                            $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("knee")
                            $ Girl.Inventory.append("knee")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)
                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the high socks." if "socks" in Player.Inventory and Girl == JubesX:

                        if "sock" not in Girl.Inventory:
                            "You give [Girl.name] the high socks."
                            $ Girl.blushing = 1
                            $ Girl.change_face("bemused")
                            $ Player.Inventory.remove("sock")
                            $ Girl.Inventory.append("sock")
                            $ Girl.change_stat("love", 200, 5)
                            $ Girl.change_stat("obedience", 200, 5)
                            $ Girl.change_stat("inhibition", 200, 5)
                            Girl.voice "These are pretty nice. . ."
                        else:
                            Girl.voice "I already have one of those."

                    "Give her the bikini top." if Girl.Tag + " bikini_top" in Player.Inventory:

                        if "bikini_top" not in Girl.Inventory:
                            "You give [Girl.name] the bikini top."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 1200):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " bikini_top")
                                $ Girl.Inventory.append("bikini_top")
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
                            elif ApprovalCheck(Girl, 900) or Girl == JeanX:
                                $ Girl.change_face("confused",1)
                                $ Player.Inventory.remove(Girl.Tag + " bikini_top")
                                $ Girl.Inventory.append("bikini_top")
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
                                $ Girl.change_face("bemused",1)
                            elif ApprovalCheck(Girl, 700):
                                $ Girl.change_face("confused",2)
                                $ Player.Inventory.remove(Girl.Tag + " bikini_top")
                                $ Girl.Inventory.append("bikini_top")
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
                                $ Girl.change_face("bemused",1)
                            elif "no_gift_bra" in Girl.daily_history:
                                $ Girl.change_face("angry",2)
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
                                $ Girl.change_face("angry",2)
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
                                $ Girl.blushing = 1
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_bra")
                                $ Girl.daily_history.append("no_gift_bra")
                            if "bikini_top" in Girl.Inventory and "bikini_bottoms" in Girl.Inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"
                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "blue_skirt" in Girl.Inventory:
                                        $ Girl.Swim[0] = 1
                                else:
                                    $ Girl.Swim[0] = 1
                        else:
                            Girl.voice "I already have one of those."



                    "Give her the bikini bottoms." if Girl.Tag + " bikini_bottoms" in Player.Inventory:

                        if "bikini_bottoms" not in Girl.Inventory:
                            "You give [Girl.name] the bikini bottoms."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 1200):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " bikini_bottoms")
                                $ Girl.Inventory.append("bikini_bottoms")
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
                            elif ApprovalCheck(Girl, 900) or Girl == JeanX:
                                $ Girl.change_face("confused",1)
                                $ Player.Inventory.remove(Girl.Tag + " bikini_bottoms")
                                $ Girl.Inventory.append("bikini_bottoms")
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
                                $ Girl.change_face("bemused",1)
                            elif ApprovalCheck(Girl, 700):
                                $ Girl.change_face("confused",2)
                                $ Player.Inventory.remove(Girl.Tag + " bikini_bottoms")
                                $ Girl.Inventory.append("bikini_bottoms")
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
                                $ Girl.change_face("bemused",1)
                            elif "no_gift_panties" in Girl.daily_history:
                                $ Girl.change_face("angry",2)
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
                                $ Girl.change_face("angry",2)
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
                                $ Girl.blushing = 1
                                "She hands them back to you."
                                $ Girl.recent_history.append("no_gift_panties")
                                $ Girl.daily_history.append("no_gift_panties")
                            if "bikini_top" in Girl.Inventory and "bikini_bottoms" in Girl.Inventory:
                                if Girl == StormX:
                                    ch_s "Oh! I understand the purpose of the flap now!"
                                if Girl == KittyX:
                                    if Girl.inhibition >= 400 or "blue_skirt" in Girl.Inventory:
                                        $ Girl.Swim[0] = 1
                                else:
                                    $ Girl.Swim[0] = 1
                        else:
                            Girl.voice "I already have one of those."


                    "Give her the blue skirt." if Girl.Tag + " blue_skirt" in Player.Inventory:

                        if "blue_skirt" not in Girl.Inventory:
                            "You give [Girl.name] the blue skirt."
                            $ Girl.blushing = 1
                            if ApprovalCheck(Girl, 1000):
                                $ Girl.change_face("bemused")
                                $ Player.Inventory.remove(Girl.Tag + " blue_skirt")
                                $ Girl.Inventory.append("blue_skirt")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 10)
                                ch_k "This is a cute skirt. . ."
                            elif ApprovalCheck(Girl, 800):
                                $ Girl.change_face("confused",1)
                                $ Player.Inventory.remove(Girl.Tag + " blue_skirt")
                                $ Girl.Inventory.append("blue_skirt")
                                $ Girl.change_stat("love", 200, 20)
                                $ Girl.change_stat("obedience", 200, 10)
                                $ Girl.change_stat("inhibition", 200, 5)
                                ch_k "This is kinda daring. . ."
                                $ Girl.change_face("bemused",1)
                            elif ApprovalCheck(Girl, 600):
                                $ Girl.change_face("confused",2)
                                $ Player.Inventory.remove(Girl.Tag + " blue_skirt")
                                $ Girl.Inventory.append("blue_skirt")
                                $ Girl.change_stat("love", 200, 10)
                                $ Girl.change_stat("obedience", 200, 5)
                                $ Girl.change_stat("inhibition", 200, 5)
                                ch_k "It'd go well with a swimsuit. . ."
                                $ Girl.change_face("bemused",1)
                            elif "no_gift_skirt" in Girl.recent_history:
                                $ Girl.change_face("angry",2)
                                ch_k "I just don't want that."
                            elif "no_gift_skirt" in Girl.daily_history:
                                $ Girl.change_face("angry",2)
                                ch_k "Look, my answer's still no, stop asking!"
                            else:
                                $ Girl.change_face("angry",2)
                                $ Girl.change_stat("love", 50, -5)
                                $ Girl.change_stat("obedience", 20, 5)
                                $ Girl.change_stat("inhibition", 20, 10)
                                ch_k "Oh, don't you worry what I'm wearing."
                                $ Girl.blushing = 1
                                "She hands it back to you."
                                $ Girl.recent_history.append("no_gift_skirt")
                                $ Girl.daily_history.append("no_gift_skirt")
                            if Girl == KittyX and "bikini_top" in Girl.Inventory and "bikini_bottoms" in Girl.Inventory:
                                $ Girl.Swim[0] = 1
                        else:
                            Girl.voice "I already have one of those."
                    "Never mind":


                        pass
            "Wardrobe":


                ch_p "I wanted to talk about your style."
                call Taboo_Level
                $ Line = "Giftstore"
                call expression Girl.Tag + "_Clothes"
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
                    call expression Girl.Tag + "_Clothes"

            "Shift her Personality" if ApprovalCheck(Girl, 900, "L", TabM=0) or ApprovalCheck(Girl, 900, "O", TabM=0)or ApprovalCheck(Girl, 900, "I", TabM=0):
                ch_p "Could we talk about us?"
                call expression Girl.Tag + "_Personality"
            "Your Petname":

                ch_p "Could we talk about my pet name?"
                call expression Girl.Tag + "_names"
            "[Girl.name]'s Petname":

                ch_p "I've got a pet name for you, you know?"
                call expression Girl.Tag + "_Pet"

            "[Girl.name]'s name" if len(Girl.names) > 1:
                ch_p "You know how you told me you went by a different name?"
                call expression Girl.Tag + "_Rename"

            "Follow options" if "follow" in Girl.Traits:
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
                    "You can go where you want, I'll catch up later." if "freetravels" not in Girl.Traits:
                        $ Girl.change_face("perplexed")
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

                    "You can ask if I want to follow you." if "asktravels" not in Girl.Traits or "freetravels" in Girl.Traits:
                        $ Girl.change_face("perplexed")
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

                    "Don't ever leave when I'm around." if "lockedtravels" not in Girl.Traits or "freetravels" in Girl.Traits:
                        if ApprovalCheck(Girl, 500, "O",Alt=[[EmmaX,JeanX],600]) or ApprovalCheck(Girl, 900, "L"):
                            $ Girl.change_face("sexy")
                            if Girl == RogueX:
                                ch_r "Oh, Ok."
                            elif Girl == KittyX:
                                ch_k "Aw, you miss me when I'm not around!"
                            elif Girl == EmmaX:
                                $ Girl.change_face("angry", Eyes="side")
                                ch_e "I don't know why I put up with your nonsense."
                                $ Girl.change_face("sexy",1)
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
                            $ Girl.change_face("angry")
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
                    if "freetravels" in Girl.Traits:
                        $ Girl.Traits.remove("freetravels")
                    if "asktravels" in Girl.Traits:
                        $ Girl.Traits.remove("asktravels")
                    if "lockedtravels" in Girl.Traits:
                        $ Girl.Traits.remove("lockedtravels")

                    if Line == "free":
                        $ Girl.Traits.append("freetravels")
                    elif Line == "ask":
                        $ Girl.Traits.append("asktravels")
                    elif Line == "lock":
                        $ Girl.Traits.append("lockedtravels")
                    $ Line = 0

            "\"Like\" options" if Girl == KittyX:
                ch_p "So you[Girl.like]say \"[Girl.like]\" a lot. . ."
                if ApprovalCheck(Girl, 800):
                    call KittyLike
                else:
                    ch_k "[Girl.Like]what's it to you?"
            "Boundaries":

                menu:
                    "Should she come by unannounced?"
                    "Yes [[default]":
                        ch_p "You can come over whenever you feel like it."
                        $ Girl.change_face("smile")
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
                        $ Girl.DrainWord("lockedout",0,0,1)
                    "No":
                        ch_p "Could you please not just drop by unannounced?"
                        $ Girl.change_face("perplexed")
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
                        $ Girl.change_face("smile")
                        $ Girl.AddWord(1,0,0,"lockedout")
            "Switch to. . .":
                call Switch_Chat
            "Never mind.":

                return






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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
