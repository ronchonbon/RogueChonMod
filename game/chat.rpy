label Chat(Girl=0):  #rkeljsv
        if not Girl:
                menu:
                    "Chat with [RogueX.name]" if RogueX.Loc == bg_current:
                            $ Girl = RogueX
                    "Text [RogueX.name]" if RogueX.Loc != bg_current:
                            $ Girl = RogueX

                    "Chat with [KittyX.name]" if KittyX.Loc == bg_current:
                            $ Girl = KittyX
                    "Text [KittyX.name]" if KittyX.Loc != bg_current and "met" in KittyX.History:
                            $ Girl = KittyX

                    "Chat with [EmmaX.name]" if EmmaX.Loc == bg_current:
                            $ Girl = EmmaX
                    "Text [EmmaX.name]" if EmmaX.Loc != bg_current and "met" in EmmaX.History:
                            $ Girl = EmmaX

                    "Chat with [LauraX.name]" if LauraX.Loc == bg_current:
                            $ Girl = LauraX
                    "Text [LauraX.name]" if LauraX.Loc != bg_current and "met" in LauraX.History:
                            $ Girl = LauraX

                    "Chat with [JeanX.name]" if JeanX.Loc == bg_current:
                            $ Girl = JeanX
                    "Text [JeanX.name]" if JeanX.Loc != bg_current and "met" in JeanX.History:
                            $ Girl = JeanX

                    "Chat with [StormX.name]" if StormX.Loc == bg_current:
                            $ Girl = StormX
                    "Text [StormX.name]" if StormX.Loc != bg_current and "met" in StormX.History:
                            $ Girl = StormX

                    "Chat with [JubesX.name]" if JubesX.Loc == bg_current:
                            $ Girl = JubesX
                    "Text [JubesX.name]" if JubesX.Loc != bg_current and "met" in JubesX.History:
                            $ Girl = JubesX

                    "Never Mind":
                        pass
        if Girl:
                if Girl.Loc == bg_current:
                        if Girl == EmmaX and "classcaught" not in EmmaX.History:
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
                        if Girl == LauraX and Girl.Loc == bg_current and "scent" in Player.daily_history:
                                #if you've fucked another girl, and not showered, Laura will know.
                                if not ApprovalCheck(Girl, 1700) and not ApprovalCheck(Girl, 600,"O"):
                                        $ Options = all_Girls[:]
                                        while Options:
                                                if Options[0] in Player.daily_history and "saw with " + Options[0].Tag not in Girl.Traits and Girl.GirlLikeCheck(Options[0]) <= 700:
                                                        $ Girl.Traits.append("saw with " + Options[0].Tag)
                                                $ Options.remove(Options[0])
                                $ Player.daily_history.remove("scent")

                        if "les" in Girl.recent_history:
                                #if she's with a girl. . .
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
                                        ch_e "One moment, [Girl.Petname]. . ."
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
                                        ch_s "One moment, [Girl.Petname]. . ."
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
                                        ch_r "So what did you want to talk about, [Girl.Petname]?"
                                elif Girl == KittyX:
                                        ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
                                elif Girl == EmmaX:
                                        ch_e "What was it you wanted to discuss, [Girl.Petname]?"
                                elif Girl == LauraX:
                                        ch_l "Yeah?"
                                elif Girl == JeanX:
                                        ch_j "What is it?"
                                elif Girl == StormX:
                                        ch_s "What can I do for you, [Girl.Petname]?"
                                elif Girl == JubesX:
                                        ch_v "Hey, what can I do for ya, [Girl.Petname]?"
                        call Chat_Menu
                        #call expression Girl.Tag + "_Chat_Set" pass ("chat")
                elif Girl in Digits:
                    if Girl.Loc == "hold":
                        "She doesn't seem to be picking up."
                    else:
                        if Girl == EmmaX:
                                    if EmmaX.Loc == "bg_teacher" and bg_current == "bg_classroom":
                                            "She texts back, \"We can speak after class, [EmmaX.Petname].\""
                                            return
                                    elif "classcaught" not in EmmaX.History:
                                            call Emma_Chat_Minimal
                                            return
                        if Girl == StormX:
                                    if StormX.Loc == "bg_teacher" and bg_current == "bg_classroom":
                                            "She texts back, \"This can wait until after class, [StormX.Petname].\""
                                            return
                        if Girl.Loc != bg_current:
                                    show Cellphone at sprite_location(StageLeft)
                        else:
                                    hide Cellphone
                        "You send [Girl.name] a text."
                        #intro dialog
                        if "angry" not in Girl.recent_history:
                                if Girl == RogueX:
                                        ch_r "So what did you want to talk about, [Girl.Petname]?"
                                elif Girl == KittyX:
                                        ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
                                elif Girl == EmmaX:
                                        ch_e "What was it you wanted to discuss, [Girl.Petname]?"
                                elif Girl == LauraX:
                                        ch_l "Yeah?"
                                elif Girl == JeanX:
                                        ch_j "What is it?"
                                elif Girl == StormX:
                                        ch_s "What can I do for you, [Girl.Petname]?"
                                elif Girl == JubesX:
                                        ch_v "Hey, what can I do for ya, [Girl.Petname]?"
                        call Chat_Menu
                else:
                        "You don't know her number, you'll have to go to her."
        return

label Chat_Menu: #rkeljsv
        #Primary chat menu, called by "Chat", carries over "Girl"
        $ Girl = GirlCheck(Girl)
        $ Girl.change_face()
        call Shift_Focus(Girl)
        if Girl.Loc != bg_current:
                    show Cellphone at sprite_location(StageLeft)
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
                            ch_v "Not in the mood, [Girl.Petname]."
                    return

        if time_index == 2 and "yesdate" in Player.daily_history:
                #checks to see if you want to go on a date
                call Readytogo(Girl)

        menu:
            "Come on over." if Girl.Loc != bg_current:
                        if Girl in Nearby and bg_current != "bg_showerrroom":
                                call Swap_Nearby(Girl)
                        elif Room_Full():
                                "It's already pretty crowded here."
                                call Dismissed
                        else:
                                call summon(Girl)
            "Ask [Girl.name] to leave" if Girl.Loc == bg_current:
                                call Girl_Dismissed(Girl)
                                return

            "Romance her":
                    menu:
                        "Flirt with her (locked)" if Girl.Chat[5]:
                                    pass
                        "Flirt with her" if not Girl.Chat[5]:
                                    call Flirt(Girl)

                        "Sex Menu (locked)" if Girl.Loc != bg_current:
                                    pass
                        "Sex Menu" if Girl.Loc == bg_current:
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
                                                    ch_v "Not in the mood, [Girl.Petname]?"
                                    elif ApprovalCheck(Girl, 600, "LI"):
                                            $ Girl.change_face("sexy")
                                            if Girl == RogueX:
                                                    ch_r "Heh, all right, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "Mmmm, ok, [Girl.Petname]."
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
                                            call enter_main_sex_menu
                                            return
                                    elif ApprovalCheck(Girl, 400, "OI"):
                                            if Girl == RogueX:
                                                    ch_r "If that's what you want, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "Yes, [Girl.Petname]."
                                            elif Girl == EmmaX:
                                                    ch_e "If that's what you want, [Girl.Petname]."
                                            elif Girl == LauraX:
                                                    ch_l "Yes, [Girl.Petname]."
                                            elif Girl == JeanX:
                                                    ch_j "Whatever. . ."
                                            elif Girl == StormX:
                                                    ch_s "Fine."
                                            elif Girl == JubesX:
                                                    ch_v "What would you like, [Girl.Petname]?"
                                            call enter_main_sex_menu
                                            return
                                    else:
                                            if Girl == RogueX:
                                                    ch_r "I'm not really interested, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "No thanks, [Girl.Petname]."
                                            elif Girl == EmmaX:
                                                    ch_e "No thank you, [Girl.Petname]."
                                            elif Girl == LauraX:
                                                    ch_l "No thanks, [Girl.Petname]."
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
                                        $ line = 0
                                        call expression Girl.Tag + "_SexChat" #call Rogu_SexChat

                        "Date (locked)" if time_index > 2:
                                        pass
                        "Date"  if time_index <= 2:
                                        ch_p "Do you want to go on a date tonight?"
                                        call Date_Ask(Girl)

                        "Gifts (locked)" if Girl.Loc != bg_current:
                                        pass
                        "Gifts" if Girl.Loc == bg_current:
                                        ch_p "I'd like to give you something."
                                        call Gifts #(Girl)
                        "Back":
                                        pass

            "Talk with her":
                    menu:
                        "I just wanted to talk. . .":
                                    call expression Girl.Tag + "_Chitchat" #call Rogue_Chitchat
                        "Relationship status":
                                    ch_p "Could we talk about us?"
                                    if Girl.Loc == bg_current:
                                        call expression Girl.Tag + "_Relationship" #call Rogue_Relationship
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
                                        "How do you feel about [KittyX.name]?" if Girl != KittyX and "met" in KittyX.History:
                                                call expression Girl.Tag + "_About" pass (KittyX)
                                        "How do you feel about [EmmaX.name]?" if Girl != EmmaX and "met" in EmmaX.History:
                                                call expression Girl.Tag + "_About" pass (EmmaX)
                                        "How do you feel about [LauraX.name]?" if Girl != LauraX and "met" in LauraX.History:
                                                call expression Girl.Tag + "_About" pass (LauraX)
                                        "How do you feel about [JeanX.name]?" if Girl != JeanX and "met" in JeanX.History:
                                                call expression Girl.Tag + "_About" pass (JeanX)
                                        "How do you feel about [StormX.name]?" if Girl != StormX and "met" in StormX.History:
                                                call expression Girl.Tag + "_About" pass (StormX)
                                        "How do you feel about [JubesX.name]?" if Girl != JubesX and "met" in JubesX.History:
                                                call expression Girl.Tag + "_About" pass (JubesX)
                                        "About hooking up with other girls. . .":
                                                call expression Girl.Tag + "_Monogamy" #call Rogue_Monogamy
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

            "Add her to party" if Girl not in Party and Girl.Loc == bg_current:
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
                                call Girls_Schedule([Options[0]],0)
                                if "leaving" in Options[0].recent_history:
                                        $ Options[0].DrainWord("leaving")
                                if Options[0] == RogueX:
                                        if Options[0].Loc == bg_current:
                                                ch_r "Ok, I'll probably stick around for a bit anyway."
                                        else:
                                                ch_r "Ok, see you later then."
                                elif Options[0] == KittyX:
                                        if Options[0].Loc == bg_current:
                                                ch_k "Good to know, but I'm[Options[0].like] fine here."
                                        else:
                                                ch_k "Cool, later."
                                elif Options[0] == EmmaX:
                                        if Options[0].Loc == bg_current:
                                                ch_e "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                                        elif Options[0].Loc == "bg_teacher" and bg_current == "bg_classroom":
                                                ch_e "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                                        else:
                                                ch_e "If that's all then, I'll see you later."
                                elif Options[0] == LauraX:
                                        if Options[0].Loc == bg_current:
                                                ch_l "I think I'm fine here."
                                        else:
                                                ch_l "Ok, see ya then."
                                elif Options[0] == JeanX:
                                        #if Options[0].Loc == bg_current:
                                                #ch_j "Ok."
                                        #else:
                                                ch_j "Ok."
                                elif Options[0] == StormX:
                                        if Options[0].Loc == bg_current:
                                                ch_s "I would rather stay, thank you."
                                        elif Options[0].Loc == "bg_teacher" and bg_current == "bg_classroom":
                                                ch_s "I do have a class to teach. I think that I'll stay."
                                        else:
                                                ch_s "Ah, fine, I'll see you later."
                                elif Options[0] == JubesX:
                                        if Options[0].Loc == bg_current:
                                                ch_v "Ok, but I'll stick around."
                                        else:
                                                ch_v "Ok, ok. Laters."
                                if Options[0].Loc != bg_current:
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

label Switch_Chat: #rkeljsv
    #called from Main Chat, Settings, or Wardrobe
    if bg_current == "HW Party":
            "You'll have to go to the other girls if you want to talk to them."
            return
    $ line = Girl
    menu:
        "[RogueX.name]" if Girl != RogueX:
                $ Girl = RogueX
        "[KittyX.name]" if Girl != KittyX and "met" in KittyX.History:
                $ Girl = KittyX
        "[EmmaX.name]" if Girl != EmmaX and "met" in EmmaX.History:
                $ Girl = EmmaX
        "[LauraX.name]" if Girl != LauraX and "met" in LauraX.History:
                $ Girl = LauraX
        "[JeanX.name]" if Girl != JeanX and "met" in JeanX.History:
                $ Girl = JeanX
        "[StormX.name]" if Girl != StormX and "met" in StormX.History:
                $ Girl = StormX
        "[JubesX.name]" if Girl != JubesX and "met" in JubesX.History:
                $ Girl = JubesX
        "Never mind":
                $ line = 0
                return

    if Girl.Loc != bg_current:
        if Girl in Digits:
                "You give [Girl.name] a call."
                if Girl == EmmaX and "classcaught" not in EmmaX.History:
                    ch_e "I don't have time to talk to students right now."
                    $ Girl = line
        else:
                    "You don't have her number."
                    $ Girl = line
    if Girl == EmmaX and "classcaught" not in EmmaX.History:
            ch_e "Surely we can discuss this later. . . alone perhaps."
            $ Girl = line
            $ line = 0
            return
    call Shift_Focus(Girl)
    if "angry" not in Girl.recent_history and Girl != line:
            if Girl == RogueX:
                    ch_r "So what did you want to talk about, [Girl.Petname]?"
            elif Girl == KittyX:
                    ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
            elif Girl == EmmaX:
                    ch_e "What was it you wanted to discuss, [Girl.Petname]?"
            elif Girl == LauraX:
                    ch_l "Yeah?"
            elif Girl == JeanX:
                    ch_j "What is it?"
            elif Girl == StormX:
                    ch_s "What can I do for you, [Girl.Petname]?"
            elif Girl == JubesX:
                    ch_v "Hey, what can I do for ya, [Girl.Petname]?"
    $ line = 0
    return

label Girl_Dismissed(Girl=0,Leaving = 0): #rkeljsv
    $ Girl = GirlCheck(Girl)
    if Girl in Party:
            $ Party.remove(Girl)
    call Girls_Schedule([Girl],0)
    #if Girl.Loc == bg_current then it means she wants to stay here
    if "leaving" in Girl.recent_history:
                $ Girl.DrainWord("leaving")
    menu:
        "You can leave if you like.":
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 700, "O"):
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
                                ch_e "Very well, [Girl.Petname]"
                        elif Girl == LauraX:
                                ch_l "Ok."
                        elif Girl == JeanX:
                                ch_j "Ok."
                        elif Girl == StormX:
                                ch_s "Ok then."
                        elif Girl == JubesX:
                                ch_v "K. . ."
                        $ Leaving = 1
                # End "You can leave if you like."
        "Could you give me the room please?":
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 800, "LO"):
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
                #end "Could you give me the room please?"
        "You can go now.":
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 500, "O"):
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
                #end "You can go now."
        "Nevermind.":
                        return

    if not Leaving and bg_current in ("bg_campus","bg_classroom","bg_dangerroom"):
            #if there is space nearby. . .
            call Remove_Girl(Girl,1,1)
    elif not Leaving:
            #if she's refused to leave yet. . .
            menu:
                extend ""
                "I insist, get going.":
                        if Girl.Loc != bg_current and (ApprovalCheck(Girl, 1200, "LO") or ApprovalCheck(Girl, 500, "O")):
                                #If she has someplace to be and is obedient
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
                        elif Girl.Loc != bg_current and (ApprovalCheck(Girl, 1000, "LO") or ApprovalCheck(Girl, 300, "O")):
                                #If she has someplace to be and is less obedient
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
                                        ch_e "I'll leave, but do not test me, [Girl.Petname]"
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
                        elif Girl.Loc != bg_current:
                                #If she has someplace to be but is not obedient
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
                                #If she has nowhere to be to be but is obedient
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
                                #If she has nowhere to be to be and is not obedient
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
                        #end "I insist, get going."
                "Ok, nevermind.":
                                pass

    if "dismissed" not in Girl.daily_history:
            $ Girl.daily_history.append("dismissed")
    if Girl in Nearby:
            "You shift a bit away from [Girl.name]"
    elif Leaving == 0:
            # Stay
            $ Girl.Loc = bg_current
    else:
            # Go
            if Girl.Loc != bg_current: #it stays the same
                pass
            elif bg_current == Girl.Home:
                $ Girl.Loc = "bg_campus"
            else:
                $ Girl.Loc = Girl.Home
            call AllReset(Girl)
            "[Girl.name] heads out."
    return
    #end "you can leave"

label Favorite_Actions(Girl=0, Quick=0, Temp=0, ATemp=0, PTemp=0, BTemp=0, TTemp=0, HTemp=0, FTemp=0, D20F=0, Girlsptions=0):
    # Character is the selected girl
    # if there's no selected Girl, it does it for all girls
    # if Quick is True, it just returns a string of the action as a value, otherwise it sets it as a lasting variable.

    if Girl:
            $ Girlsptions = [Girl]
    else:
            $ Girlsptions = active_Girls[:]
            #cycles through each girl possible

    while Girlsptions:
            $ Girl = Girlsptions[0]
            #ass, pussy, blow, tits, hand, fondling, kiss
            $ ATemp = Girl.Anal + Girl.DildoA + Girl.FondleA + Girl.InsertA + Girl.LickA
            $ PTemp = Girl.Sex + Girl.DildoP + Girl.FondleP + Girl.InsertP + Girl.LickP
            $ BTemp = Girl.Blow
            $ TTemp = Girl.Tit
            $ XTemp = Girl.Foot
            $ HTemp = Girl.Hand
            $ FTemp = Girl.FondleB + Girl.FondleT + Girl.SuckB + Girl.Hotdog

            #This portion sets a bonus based on the player's favorite activity with her.
            if Girl.PlayerFav and ApprovalCheck(Girl, 1500):
                    if Girl.PlayerFav == "anal":
                        $ ATemp += 20
                    elif Girl.PlayerFav == "sex":
                        $ PTemp += 20
                    elif Girl.PlayerFav == "blow":
                        $ BTemp += 20
                    elif Girl.PlayerFav == "tit":
                        $ TTemp += 20
                    elif Girl.PlayerFav == "foot":
                        $ XTemp += 20
                    elif Girl.PlayerFav == "hand":
                        $ HTemp += 20
                    else:
                        $ FTemp += 20
            elif Girl.PlayerFav and ApprovalCheck(Girl, 800):
                    if Girl.PlayerFav == "anal":
                        $ ATemp += 5
                    elif Girl.PlayerFav == "sex":
                        $ PTemp += 5
                    elif Girl.PlayerFav == "blow":
                        $ BTemp += 5
                    elif Girl.PlayerFav == "tit":
                        $ TTemp += 5
                    elif Girl.PlayerFav == "foot":
                        $ XTemp += 5
                    elif Girl.PlayerFav == "hand":
                        $ HTemp += 5
                    else:
                        $ FTemp += 5

            #This adds the numbers together to make a large number, then generates a random number between 1 and that total
            $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + XTemp + FTemp + Girl.Kissed
            if Total <= 0:
                $ D20F = 999
            else:
                $ D20F = renpy.random.randint(1, Total)

            # This selects a favorite activity based on which number is picked.
            if D20F <= ATemp:
                        #if the result is someplace under the "anal" category. . .
                        if Girl.Anal >= 5:
                            $ Temp = "anal"
                        elif Girl.LickA >= 5:
                            $ Temp = "lick ass"
                        else:
                            $ Temp = "insert ass"
            elif D20F <= ATemp + PTemp:
                        #if the result is someplace under the "sex" category. . .
                        if Girl.Sex >= 5:
                            $ Temp = "sex"
                        elif Girl.LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
            elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
            elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
                            $ Temp = "foot"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
                            $ Temp = "hand"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp + FTemp:
                        #if the result failed the higher tier categories. . .
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and Girl.Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and Girl.SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and Girl.FondleB:
                            $ Temp = "fondle_breasts"
                        else:
                            $ Temp = "fondle_thighs"
            else:
                            $ Temp = "kiss_you"

            if not Quick:
                $ Girl.Favorite = Temp
            else:
                return Temp
            $ Girlsptions.remove(Girlsptions[0])
    return

label Girl_Settings: #rkeljsv
    if Girl not in all_Girls:
        $ Girl == focused_Girl
    call Shift_Focus(Girl)
    while True:
        menu:
            ch_p "Let's talk about you."
            "Wardrobe":
                        ch_p "I wanted to talk about your style."
                        if bg_current == "HW Party":
                                call Anyline(Girl,"Not at the party. . .")
                        else:
                                call Taboo_Level
                                call expression Girl.Tag + "_Clothes" #call Rogue_Clothes

            "Shift her Personality" if ApprovalCheck(Girl, 900, "L", TabM=0) or ApprovalCheck(Girl, 900, "O", TabM=0)or ApprovalCheck(Girl, 900, "I", TabM=0):
                        ch_p "Could we talk about us?"
                        call expression Girl.Tag + "_Personality" #call Rogue_Personality

            "Your Petname":
                        ch_p "Could we talk about my pet name?"
                        call expression Girl.Tag + "_Names"  #call Rogue_Names

            "[Girl.name]'s Petname":
                        ch_p "I've got a pet name for you, you know?"
                        call expression Girl.Tag + "_Pet" #call Rogue_Pet

            "[Girl.name]'s name" if len(Girl.names) > 1:
                        ch_p "You know how you told me you went by a different name?"
                        call expression Girl.Tag + "_Rename" #call Rogue_Rename

            "Follow options" if "follow" in Girl.Traits:
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
                        else: #Kitty, Laura, Jubilee
                                call Anyline(Girl,"Yeah?")
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
                                    $ line = "free"

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
                                    $ line = "ask"

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
                                    $ line = "lock"
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

                        if line:
                                    $ Girl.daily_history.append("follow")
                                    if "freetravels" in Girl.Traits:
                                        $ Girl.Traits.remove("freetravels")
                                    if "asktravels" in Girl.Traits:
                                        $ Girl.Traits.remove("asktravels")
                                    if "lockedtravels" in Girl.Traits:
                                        $ Girl.Traits.remove("lockedtravels")

                                    if line == "free":
                                        $ Girl.Traits.append("freetravels")
                                    elif line == "ask":
                                        $ Girl.Traits.append("asktravels")
                                    elif line == "lock":
                                        $ Girl.Traits.append("lockedtravels")
                                    $ line = 0

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
    #end loop

label AskDateOther: #rkeljsv
        #called if you ask a girlfriend about dating a different girl. "Girl" is passed from the prior chat.
        if Girl not in Player.Harem:
            return
        menu:
            "Have you considered letting me date. . ."
            "[RogueX.name]" if Girl != RogueX and RogueX not in Player.Harem:
                    call Poly_Start(RogueX,1,Girl)
            "[KittyX.name]" if Girl != KittyX and KittyX not in Player.Harem and "met" in KittyX.History:
                    call Poly_Start(KittyX,1,Girl)
            "[EmmaX.name]" if Girl != EmmaX and EmmaX not in Player.Harem and "met" in EmmaX.History:
                    call Poly_Start(EmmaX,1,Girl)
            "[LauraX.name]" if Girl != LauraX and LauraX not in Player.Harem and "met" in LauraX.History:
                    call Poly_Start(LauraX,1,Girl)
            "[JeanX.name]" if Girl != JeanX and JeanX not in Player.Harem and "met" in JeanX.History:
                    call Poly_Start(JeanX,1,Girl)
            "[StormX.name]" if Girl != StormX and StormX not in Player.Harem and "met" in StormX.History:
                    call Poly_Start(StormX,1,Girl)
            "[JubesX.name]" if Girl != JubesX and JubesX not in Player.Harem and "met" in JubesX.History:
                    call Poly_Start(JubesX,1,Girl)
            "Never mind":
                    pass
        return

label summon(Girl, temp_modifier = temp_modifier):
    $ Girl.OutfitChange()

    if "no summon" in Girl.recent_history:
        if "angry" in Girl.recent_history:
            call already_said_no_dialog(Girl)
        elif Girl.recent_history.count("no summon") > 1:
            call already_said_no_dialog(Girl)

            $ Girl.recent_history.append("angry")
        elif time_index >= 3: #night time
            if Girl == RogueX:
                ch_r "I told you it was too late for that tonight."
            elif Girl == KittyX:
                ch_k "Like I said, it's too late for that."
            elif Girl == EmmaX:
                ch_e "It's past your bedtime."
        else:
            if Girl == RogueX:
                ch_r "I told you I was busy."
            elif Girl == KittyX:
                ch_k "Like I told you, I'm busy."
            elif Girl == EmmaX:
                ch_e "As I said, I've got things to do."
            elif Girl == LauraX:
                ch_l "Like I said, I'm busy."
            elif Girl == JeanX:
                ch_j "I told you I'm busy!"
            elif Girl == StormX:
                ch_s "As I said, I am occupied."
            elif Girl == JubesX:
                ch_v "Like I said, I'm busy."

        $ Girl.recent_history.append("no summon")

        return

    $ D20 = renpy.random.randint(1, 20)
    $ line = 0

    if Girl.Loc == "bg_classroom": #fix change these if changed function
        if Girl != StormX:
            $ temp_modifier = -10
        else:
            $ temp_modifier = -30
    elif Girl.Loc == "bg_dangerroom":
        if Girl == EmmaX:
            $ temp_modifier = -20
        else:
            $ temp_modifier = -10
    elif Girl in [JeanX] and Girl.Loc == Girl.Home:
        $ temp_modifier = -10
    elif Girl.Loc == "bg_showerroom":
        if Girl in [EmmaX, StormX, JubesX]:
            $ temp_modifier = -30
        else:
            $ temp_modifier = -40
    elif Girl in [EmmaX, StormX] and Girl.Loc == "bg_teacher":
        $ temp_modifier = -30

    if D20 <= 3:
        $ line = "no"
    elif "les" in Girl.recent_history:
        if ApprovalCheck(Girl, 2000):
            if Girl == RogueX:
                ch_r "I'm enjoying some company right now, [Girl.Petname], care to join us?"
            elif Girl == KittyX:
                ch_k "I'm sorta with someone right now, [KittyX.Petname], wanna join us?"
            elif Girl == EmmaX:
                ch_e "I'm. . . entertaining at the moment, [EmmaX.Petname], care to join us?"
            elif Girl == LauraX:
                ch_l "I'm kinda with a girl right now? Wanna come over?"
            elif Girl == JeanX:
                ch_j "I'm getting off with one of the girls. Wanna come over?"
            elif Girl == StormX:
                ch_s "I am preoccupied with one of the girls. Care to join us?"
            elif Girl == JubesX:
                ch_v "I have another guest here right now, but I guess you can drop by. . ."

            menu:
                extend ""
                "Sure.":
                    $ line = "go to"
                "No thanks.":
                    if Girl == RogueX:
                        ch_r "Suit yourself."
                    elif Girl == KittyX:
                        ch_k "K' then."
                    elif Girl == EmmaX:
                        ch_e "Your loss."
                    elif Girl == LauraX:
                        ch_l "Heh, your call."
                    elif Girl == JeanX:
                        ch_j "Heh, ok. . ."
                    elif Girl == StormX:
                        ch_s "Goodbye then."
                    elif Girl == JubesX:
                        ch_v "Heh, your call."

                    return
        else:
            if Girl == RogueX:
                ch_r "What? Um, no, um, not right now."
                ch_r "Maybe we could touch base later."
            elif Girl == KittyX:
                ch_k "Um, no, everything's fine here, we're all good here."
                ch_k "Maybe I could see you in a bit?"
            elif Girl == EmmaX:
                ch_e "Oh. . . that might be an issue, we're- I'm. . ."
                ch_e "Indisposed. . ."
                ch_e "Perhaps we could meet later."
            elif Girl == LauraX:
                ch_l "Oh, um, kinda busy here."
                ch_l "I'll see you later, eh?"
            elif Girl == JeanX:
                ch_j "I'm a little. . . tied up at the moment."
                ch_j "We can talk later."
            elif Girl == StormX:
                ch_s "I am a bit preoccupied."
                ch_s "Perhaps we could talk later?"
            elif Girl == JubesX:
                ch_v "Oh, um, I kinda have a guest."
                ch_v "I'll see you later, though?"

            $ Girl.recent_history.append("no summon")

            return
    elif time_index >= 3:
        if ApprovalCheck(Girl, 700, "L", Alt = [[StormX], 500]) or ApprovalCheck(Girl, 300, "O", Alt = [[StormX], 400]):
            if Girl == RogueX:
                ch_r "Ok, it's getting late but I can hang out for a bit."
            elif Girl == KittyX:
                ch_k "It's[KittyX.like]getting kinda late, but we can hang out for a bit."
            elif Girl == EmmaX:
                ch_e "It's getting late, but fine, what did you want?"
            elif Girl == LauraX:
                ch_l "You're up too? Sure, we can hang."
            elif Girl == JeanX:
                ch_j "You're up too? Yeah, that's fine."
            elif Girl == StormX:
                ch_s "You are awake? I can join you."
            elif Girl == JubesX:
                ch_v "You're up too? Sure, we can hang."

            $ Girl.Loc = bg_current

            call set_the_scene
        else:
            if Girl == RogueX:
                ch_r "It's a bit late, [Girl.Petname], maybe tomorrow."
            elif Girl == KittyX:
                ch_k "It's kinda late? Maybe tomorrow."
            elif Girl == EmmaX:
                ch_e "It's late, [EmmaX.Petname], tell me tomorrow."
            elif Girl == LauraX:
                ch_l "Nah."
            elif Girl == JeanX:
                ch_j "I'd rather not. . ."
            elif Girl == StormX:
                ch_s "It is too late, I need to sleep."
            elif Girl == JubesX:
                ch_v "Nah."

            $ Girl.recent_history.append("no summon")
        return
    elif not ApprovalCheck(Girl, 700, "L") or not ApprovalCheck(Girl, 600, "O"):
        if not ApprovalCheck(Girl, 300):
            if Girl == RogueX:
                ch_r "Not really interested, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "I'm kinda busy, [KittyX.Petname]."
            elif Girl == EmmaX:
                ch_e "I don't really feel up to that, [EmmaX.Petname]."
            elif Girl == LauraX:
                ch_l "I'm busy, [LauraX.Petname]."
            elif Girl == JeanX:
                ch_j "I'm busy, [JeanX.Petname]."
            elif Girl == StormX:
                ch_s "I am busy, [StormX.Petname]."
            elif Girl == JubesX:
                ch_v "I'm kinda busy, [JubesX.Petname]."

            $ Girl.recent_history.append("no summon")

            return

        if "summoned" in Girl.recent_history:
            pass
        elif "goto" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "You were just over here and then you took off. Why not just head back?"
            elif Girl == KittyX:
                ch_k "You {i}just{/i} left here, why not come back?"
            elif Girl == EmmaX:
                ch_e "You only just left, why not return?"
            elif Girl == LauraX:
                ch_l "You were just over here."
            elif Girl == JeanX:
                ch_j "You just left. . ."
            elif Girl == StormX:
                ch_s "You were just over here."
            elif Girl == JubesX:
                ch_v "You just left!"
        elif Girl.Loc == "bg_classroom" or Girl.Loc == "bg_teacher":
            if Girl == RogueX:
                ch_r "I'm kinda in class right now, [Girl.Petname], you could join me."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]in class right now, [KittyX.Petname], you up for it?"
            elif Girl == EmmaX:
                ch_e "You can find me in the classroom, [EmmaX.Petname]."
            elif Girl == LauraX:
                ch_l "I'm in class, did you want to come too?"
            elif Girl == JeanX:
                ch_j "I'm in class right now."
            elif Girl == StormX:
                ch_s "You can find me in the classroom."
            elif Girl == JubesX:
                ch_v "I'm in class, did you want to come too?"
        elif Girl.Loc == "bg_dangerroom":
            if Girl == RogueX:
                ch_r "I'm training at the moment, [Girl.Petname], care to join me?"
            elif Girl == KittyX:
                ch_k "I'm in the Danger Room, [KittyX.Petname], want in?"
            elif Girl == EmmaX:
                ch_e "I'm getting some training in, [EmmaX.Petname], care to join me?"
            elif Girl == LauraX:
                ch_l "I'm in the Danger Room, [LauraX.Petname], want in?"
            elif Girl == JeanX:
                ch_j "I'm in the Danger Room, [JeanX.Petname]."
            elif Girl == StormX:
                ch_s "I am in the Danger Room, [StormX.Petname], care to join me?"
            elif Girl == JubesX:
                ch_v "I'm in the Danger Room, [JubesX.Petname], want in?"
        elif Girl.Loc == "bg_campus":
            if Girl == RogueX:
                ch_r "I'm hanging out on campus, [Girl.Petname], want to hang with me?"
            elif Girl == KittyX:
                ch_k "I'm chillin in the quad, [KittyX.Petname], want to come?"
            elif Girl == EmmaX:
                ch_e "I'm relaxing in the square, if you'd care to join me."
            elif Girl == LauraX:
                ch_l "I'm napping under a tree here, want to come?"
            elif Girl == JeanX:
                ch_j "I'm relaxing in the quad right now."
            elif Girl == StormX:
                ch_s "I am relaxing in the courtyard, care to join me?"
            elif Girl == JubesX:
                ch_v "I'm just enjoying the sun, want to come?"
        elif Girl.Loc == Girl.Home:
            if Girl == RogueX:
                ch_r "I'm in my room, [Girl.Petname], want to swing by?"
            elif Girl == KittyX:
                ch_k "I'm in my room, [KittyX.Petname], want to hang?"
            elif Girl == EmmaX:
                ch_e "I'm in my room, [EmmaX.Petname]."
            elif Girl == LauraX:
                ch_l "I'm in my room, [LauraX.Petname], want to hang?"
            elif Girl == JeanX:
                ch_j "I'm in my room, [JeanX.Petname]."
            elif Girl == StormX:
                ch_s "I am in my room, [StormX.Petname], care to join me?"
            elif Girl == JubesX:
                ch_v "I'm in my room, [JubesX.Petname], did you wanna drop by?"
        elif Girl.Loc == "bg_player":
            if Girl == RogueX:
                ch_r "I happen to be in your room, [Girl.Petname], I'm waiting for you. . ."
            elif Girl == KittyX:
                ch_k "I'm in your room, [KittyX.Petname], come home. . ."
            elif Girl == EmmaX:
                ch_e "I'm waiting in your room, [EmmaX.Petname]. . ."
            elif Girl == LauraX:
                ch_l "I'm in your room, [LauraX.Petname], why aren't you?"
            elif Girl == JeanX:
                ch_j "I'm in your room, [JeanX.Petname], where are you?"
            elif Girl == StormX:
                ch_s "I am in your room, [StormX.Petname], coming home soon?"
            elif Girl == JubesX:
                ch_v "I'm in your room, [JubesX.Petname], are you coming back?"
        elif Girl.Loc == "bg_showerroom":
            if ApprovalCheck(Girl, 1600):
                if Girl == RogueX:
                    ch_r "I'm kinda in the shower right now, [Girl.Petname], care to join me?"
                elif Girl == KittyX:
                    ch_k "I'm[KittyX.like]in the shower right now, [KittyX.Petname], want to get wet?"
                elif Girl == EmmaX:
                    ch_e "I'm in the shower right now, [EmmaX.Petname], do you need an invitation?"
                elif Girl == LauraX:
                    ch_l "I'm in the shower right now. Join me?"
                elif Girl == JeanX:
                    ch_j "I'm in the shower right now."
                elif Girl == StormX:
                    ch_s "I am in the shower right now. Care to join me?"
                elif Girl == JubesX:
                    ch_v "I'm in the shower right now. Join me?"
            else:
                if Girl == RogueX:
                    ch_r "I'm kinda in the shower right now, [Girl.Petname], maybe we could touch base later."
                elif Girl == KittyX:
                    ch_k "I'm[KittyX.like]in the shower right now, [KittyX.Petname], maybe we could touch base later."
                elif Girl == EmmaX:
                    ch_e "I'm in the shower right now, [EmmaX.Petname], perhaps I'll see you later."
                elif Girl == LauraX:
                    ch_l "I'm in the shower right now, [LauraX.Petname]. We can connect later."
                elif Girl == JeanX:
                    ch_j "I'm in the shower right now, [JeanX.Petname]."
                    ch_j "Don't come knocking."
                elif Girl == StormX:
                    ch_s "I am in the shower right now, [StormX.Petname]. We can connect later."
                elif Girl == JubesX:
                    ch_v "I'm in the shower right now, [JubesX.Petname]. We can hang later."

                $ Girl.recent_history.append("no summon")

                return
        elif Girl.Loc == "hold":
            if Girl == RogueX:
                ch_r "I'm not really around right now, see you later?"
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]kinda off the grid right now. Sorry?"
            elif Girl == EmmaX:
                ch_e "I'm off campus for a bit, I'll be back later."
            elif Girl == LauraX:
                ch_l "I'm on task right now. Sorry?"
            elif Girl == JeanX:
                ch_j "I'm busy at the moment."
            elif Girl == StormX:
                ch_s "I am occupied right now. I am sorry."
            elif Girl == JubesX:
                ch_v "I'm a little busy right now. Sorry?"

            $ Girl.recent_history.append("no summon")

            return
        else:
            if Girl == RogueX:
                ch_r "Why don't you come over here, [Girl.Petname]?"
            elif Girl == KittyX:
                ch_k "Why don't you come over here, [KittyX.Petname]?"
            elif Girl == EmmaX:
                ch_e "You could always come over here, [EmmaX.Petname]."
            elif Girl == LauraX:
                ch_l "Why don't you come to me?"
            elif Girl == JeanX:
                ch_j "Why don't you come to me?"
            elif Girl == StormX:
                ch_s "Perhaps you could come to me?"
            elif Girl == JubesX:
                ch_v "Why don't you come to me?"

        if "summoned" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Ok, fine, but why are you leading me on a merry chase?"
            elif Girl == KittyX:
                ch_k "Ok, fiiiiine, but why are you dragging me all over?"
            elif Girl == EmmaX:
                ch_e "Again? Very well."
            elif Girl == LauraX:
                ch_l "Again? Ok, fine."
            elif Girl == JeanX:
                ch_j "Again? Ok, fine."
            elif Girl == StormX:
                ch_s "Again? Very well. . ."
            elif Girl == JubesX:
                ch_v "Oh, you want me back so soon?"

            $ line = "yes"
        elif "goto" in Girl.recent_history:
            menu:
                extend ""
                "You're right, be right back.":
                    if Girl == RogueX:
                        ch_r "See you then!"
                    elif Girl == KittyX:
                        ch_k "KK, Cya!"
                    elif Girl == EmmaX:
                        ch_e "I'll be waiting."
                    elif Girl == LauraX:
                        ch_l "See you when you get here."
                    elif Girl == JeanX:
                        ch_j "Ok then."
                    elif Girl == StormX:
                        ch_s "I will see you soon then."
                    elif Girl == JubesX:
                        ch_v "Cool, see you then."

                    $ line = "go to"
                "Nah, it's better here.":
                    if Girl == RogueX:
                        ch_r "Fine by me."
                    elif Girl == KittyX:
                        ch_k "OK."
                    elif Girl == EmmaX:
                        ch_e "Very well."
                    elif Girl == LauraX:
                        ch_l "If you say so."
                    elif Girl == JeanX:
                        ch_j "Ok then."
                    elif Girl == StormX:
                        ch_s "If you insist."
                    elif Girl == JubesX:
                        ch_v "Ok, later then."
                "But I'd {i}really{/i} like to see you over here.":
                    if ApprovalCheck(Girl, 600, "L") or ApprovalCheck(Girl, 1400):
                        $ line = "lonely"
                    else:
                        $ line = "no"
                "I said come over here.":
                    if ApprovalCheck(Girl, 600, "O"):
                        $ line = "command"
                    elif D20 >= 7 and ApprovalCheck(Girl, 1400):
                        if Girl == RogueX:
                            ch_r "I suppose I can, [Girl.Petname]."
                        elif Girl == KittyX:
                            ch_k "Ok, fine."
                        elif Girl == EmmaX:
                            ch_e "Hmm, very well."
                        elif Girl == LauraX:
                            ch_l "Hmph."
                        elif Girl == JeanX:
                            ch_j "Well. . ."
                        elif Girl == StormX:
                            ch_s ". . ."
                        elif Girl == JubesX:
                            ch_v "Fine."

                        $ line = "yes"
                    elif ApprovalCheck(Girl, 200, "O"):
                        if Girl == RogueX:
                            ch_r "I don't think so."
                            ch_r "If you want to see me, you know where to find me."
                        elif Girl == KittyX:
                            ch_k "Whatever."
                            ch_k "Here I am if you want me."
                        elif Girl == EmmaX:
                            ch_e "If you're lucky, I'll still be here when you arrive."
                        elif Girl == LauraX:
                            ch_l "Whatever."
                            ch_l "I'll be here if you change your mind."
                        elif Girl == JeanX:
                            ch_j "Whatever."
                        elif Girl == StormX:
                            ch_s "I will be here if you change your mind."
                        elif Girl == JubesX:
                            ch_v "Whatever."
                            ch_v "I'll be here if you change your mind."
                    else:
                        $ line = "no"
        else:
            menu:
                extend ""
                "Sure, I'll be right there.":
                    $ Girl.change_stat("love", 55, 1)
                    $ Girl.change_stat("inhibition", 30, 1)

                    if Girl == RogueX:
                        ch_r "See you then!"
                    elif Girl == KittyX:
                        ch_k "See ya!"
                    elif Girl == EmmaX:
                        ch_e "I'll be waiting."
                    elif Girl == LauraX:
                        ch_l "See you when you get here."
                    elif Girl == JeanX:
                        ch_j "Good."
                    elif Girl == StormX:
                        ch_s "I will see you soon then."
                    elif Girl == JubesX:
                        ch_v "Cool, see you then."

                    $ line = "go to"
                "Nah, we can talk later.":
                    $ Girl.change_stat("obedience", 50, 1)
                    $ Girl.change_stat("obedience", 30, 2)

                    if Girl == RogueX:
                        ch_r "Oh, ok. Talk to you later then."
                    elif Girl == KittyX:
                        ch_k "Oh, ok. Later then."
                    elif Girl == EmmaX:
                        ch_e "Very well."
                    elif Girl == LauraX:
                        ch_l "Ok. Later then."
                    elif Girl == JeanX:
                        ch_j "Ok."
                    elif Girl == StormX:
                        ch_s "Fine. Later then."
                    elif Girl == JubesX:
                        ch_v "Ok. Later then."
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck(Girl, 600, "L") or ApprovalCheck(Girl, 1400):
                        $ Girl.change_stat("love", 70, 1)
                        $ Girl.change_stat("obedience", 50, 1)

                        $ line = "lonely"
                    else:
                        $ Girl.change_stat("inhibition", 30, 1)

                        $ line = "no"

                        if Girl == JeanX:
                            ch_j "Needy much?"
                        elif Girl == StormX:
                            ch_s "Well we cannot have that. . ."
                        elif Girl == JubesX:
                            ch_v "Aw, how could I say \"no\"?"
                "Come on, it'll be fun." if Girl in [LauraX, JeanX, StormX, JubesX]:
                    if ApprovalCheck(Girl, 400, "L") and ApprovalCheck(Girl, 800):
                        $ Girl.change_stat("love", 70, 1)
                        $ Girl.change_stat("obedience", 50, 1)

                        $ line = "fun"
                    else:
                        $ Girl.change_stat("inhibition", 30, 1)

                        $ line = "no"
                "I said come over here.":
                    if ApprovalCheck(Girl, 600, "O"):
                        $ Girl.change_stat("love", 50, 1, 1)
                        $ Girl.change_stat("love", 40, -1)
                        $ Girl.change_stat("obedience", 90, 1)

                        $ line = "command"
                    elif D20 >= 7 and ApprovalCheck(Girl, 1400):
                        $ Girl.change_stat("love", 70, -2)
                        $ Girl.change_stat("love", 90, -1)
                        $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("obedience", 90, 1)

                        if Girl == RogueX:
                            ch_r "I suppose I can, [Girl.Petname]."
                        elif Girl == KittyX:
                            ch_k "Ok, fine, [KittyX.Petname]."
                        elif Girl == EmmaX:
                            ch_e "Ok, fine, [EmmaX.Petname]."
                        elif Girl == LauraX:
                            ch_l "Ok, fine."
                        elif Girl == JeanX:
                            ch_j "Ok, fine."
                        elif Girl == StormX:
                            ch_s "Fine."
                        elif Girl == JubesX:
                            ch_v "Ok, fine."

                        $ line = "yes"
                    elif ApprovalCheck(Girl, 200, "O"):
                        $ Girl.change_stat("love", 70, -4)
                        $ Girl.change_stat("love", 90, -2)

                        if Girl == RogueX:
                            ch_r "I don't know who you think you are, boss'in me around like that."
                        elif Girl == KittyX:
                            ch_k "You're not my supervisor!"
                        elif Girl == EmmaX:
                            ch_e "Who do you think is in charge here?!"
                        elif Girl == LauraX:
                            ch_l "Don't even try it."
                        elif Girl == JeanX:
                            ch_j "And I said \"no.\""
                        elif Girl == StormX:
                            ch_s "And I refused."
                        elif Girl == JubesX:
                            ch_v "No way."

                        $ Girl.change_stat("inhibition", 40, 2)
                        $ Girl.change_stat("inhibition", 60, 1)
                        $ Girl.change_stat("obedience", 70, -2)

                        if Girl == RogueX:
                            ch_r "If you want to see me, you know where to find me."
                        elif Girl == KittyX:
                            ch_k "You know where to find me."
                        elif Girl == EmmaX:
                            ch_e "You'd better hope you don't find me here."
                        elif Girl == LauraX:
                            ch_l "I'm staying put."
                        elif Girl == JeanX:
                            ch_j "I'm staying here."
                        elif Girl == StormX:
                            ch_s "I would rather stay."
                        elif Girl == JubesX:
                            ch_v "I'm staying here."
                    else:
                        $ Girl.change_stat("inhibition", 30, 1)
                        $ Girl.change_stat("inhibition", 50, 1)
                        $ Girl.change_stat("love", 50, -1, 1)
                        $ Girl.change_stat("obedience", 70, -1)

                        $ line = "no"
    else:
        if Girl.love > Girl.obedience:
            if Girl == RogueX:
                ch_r "I'd love to, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "Sure!"
            elif Girl == EmmaX:
                ch_e "I'd love to."
            elif Girl == LauraX:
                ch_l "Sure!"
            elif Girl == JeanX:
                ch_j "Ok, fine."
            elif Girl == StormX:
                ch_s "On my way."
            elif Girl == JubesX:
                ch_v "Sure!"
        else:
            if Girl == RogueX:
                ch_r "Ok, I'll be right over, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "Ok, be there in a jiff, [KittyX.Petname]."
            elif Girl == EmmaX:
                ch_e "I'll be right there, [EmmaX.Petname]."
            elif Girl == LauraX:
                ch_l "Ok, I'm in route."
            elif Girl == JeanX:
                ch_j "Ok, if you insist. . ."
            elif Girl == StormX:
                ch_s "Very well."
            elif Girl == JubesX:
                ch_v "Cool, on my way."

        $ line = "yes"

    $ temp_modifier = 0

    if not line:
        $ Girl.recent_history.append("no summon")

        return
    elif line == "no":
        if Girl.Loc == "bg_classroom":
            if Girl == RogueX:
                ch_r "I seriously can't, [Girl.Petname], big test coming up."
            elif Girl == KittyX:
                ch_k "I[KittyX.like]really need to study, [KittyX.Petname]."
            elif Girl == EmmaX:
                ch_e "I have a lot of paperwork, [EmmaX.Petname]."
            elif Girl == LauraX:
                ch_l "I can't skip this lecture."
            elif Girl == JeanX:
                ch_j "Sorry, [JeanX.Petname], I'm kinda busy."
            elif Girl == StormX:
                ch_s "I cannot leave class like this."
            elif Girl == JubesX:
                ch_v "I can't skip this lecture."
        elif Girl.Loc == "bg_dangerroom":
            if Girl == RogueX:
                ch_r "Wish I could, [Girl.Petname], but I need to get some hours in."
            elif Girl == KittyX:
                ch_k "I'm just getting a workout in."
            elif Girl == EmmaX:
                ch_e "I'm just getting warmed up here."
            elif Girl == LauraX:
                ch_l "I'm just getting warmed up though!"
            elif Girl == JeanX:
                ch_j "Sorry, [JeanX.Petname], I'm kinda busy."
            elif Girl == StormX:
                ch_s "I have work to put in here."
            elif Girl == JubesX:
                ch_v "I'm just getting into it."
        elif Girl in [EmmaX, StormX] and Girl.Loc == "bg_teacher":
            if Girl == EmmaX:
                ch_e "I can't exactly leave class, [EmmaX.Petname]."
            elif Girl == StormX:
                ch_s "I cannot leave class like this."
        else:
            if Girl == RogueX:
                ch_r "I'm sorry, [Girl.Petname], but I'm kinda busy right now."
            elif Girl == KittyX:
                ch_k "I'm sorry, [KittyX.Petname], but I'm kinda busy."
            elif Girl == EmmaX:
                ch_e "I have a lot to finish up here."
            elif Girl == LauraX:
                ch_l "Sorry, [LauraX.Petname], I'm kinda busy."
            elif Girl == JeanX:
                ch_j "Sorry, [JeanX.Petname], I'm kinda busy."
            elif Girl == StormX:
                ch_s "I am sorry, [StormX.Petname], I am occupied."
            elif Girl == JubesX:
                ch_v "Sorry, [JubesX.Petname], I'm kinda busy."

        $ Girl.recent_history.append("no summon")

        return
    elif line == "go to":
        $ temp_modifier = 0
        $ line = 0

        $ Girl.recent_history.append("goto")
        $ Player.recent_history.append("goto")

        if Girl.Loc == "bg_classroom" or Girl.Loc == "bg_teacher":
            if Girl == RogueX:
                ch_r "See you then!"
            elif Girl == KittyX:
                ch_k "I'll hold a seat for you!"
            elif Girl == EmmaX:
                ch_e "You don't want to miss too much."
            elif Girl == LauraX:
                ch_l "K, there's room next to me."
            elif Girl == JeanX:
                ch_j "Ok then."
            elif Girl == StormX:
                ch_s "I will see you soon then."
            elif Girl == JubesX:
                ch_v "K, there's room next to me."

            jump Class_Room
        elif Girl.Loc == "bg_dangerroom":
            if Girl == RogueX:
                ch_r "I'll be warming up!"
            elif Girl == KittyX:
                ch_k "I'll be warming up!"
            elif Girl == EmmaX:
                ch_e "I'll try to save some for you."
            elif Girl == LauraX:
                ch_l "I'll try to leave some bots for 'ya."
            elif Girl == JeanX:
                ch_j "I'll try not to finish the exercise myself."
            elif Girl == StormX:
                ch_s "I will see you soon then."
            elif Girl == JubesX:
                ch_v "Don't be long. . ."

            jump Danger_Room
        elif Girl.Loc == Girl.Home:
            if Girl == RogueX:
                ch_r "I'll get tidied up."
            elif Girl == KittyX:
                ch_k "I'll clean up a few things."
            elif Girl == EmmaX:
                ch_e "I'll tidy up a few things."
            elif Girl == LauraX:
                ch_l "I'll. . . make some space."
            elif Girl == JeanX:
                ch_j "Don't keep me waiting."
            elif Girl == StormX:
                ch_s "I will see you soon then."
            elif Girl == JubesX:
                ch_v "I'll. . . get ready."

            call girls_room(Girl)

            return
        elif Girl.Loc == "bg_player":
            if Girl == RogueX:
                ch_r "I'll be waiting."
            elif Girl == KittyX:
                ch_k "I'll be here for you."
            elif Girl == EmmaX:
                ch_e "I'll be waiting for you."
            elif Girl == LauraX:
                ch_l "I'll be waiting."
            elif Girl == JeanX:
                ch_j "Don't keep me waiting."
            elif Girl == StormX:
                ch_s "I will be waiting."
            elif Girl == JubesX:
                ch_v "I'll be waiting."

            jump player_room
        elif Girl.Loc == "bg_showerroom":
            if Girl == RogueX:
                ch_r "I guess I'll be here."
            elif Girl == KittyX:
                ch_k "I guess I'll be lathering up."
            elif Girl == EmmaX:
                ch_e "Don't keep me waiting. . ."
            elif Girl == LauraX:
                ch_l "I'll leave you some hot water."
            elif Girl == JeanX:
                ch_j "I'll see you then."
            elif Girl == StormX:
                ch_s "I will leave you some hot water."
            elif Girl == JubesX:
                ch_v "I'll leave you some hot water."

            jump Shower_Room
        elif Girl.Loc == "bg_campus":
            if Girl == RogueX:
                ch_r "I'll keep an eye out for you."
            elif Girl == KittyX:
                ch_k "I've got a nice spot in the shade."
            elif Girl == EmmaX:
                ch_e "I've got a nice location picked out."
            elif Girl == LauraX:
                ch_l "Look for the biggest tree."
            elif Girl == JeanX:
                ch_j "Ok."
            elif Girl == StormX:
                ch_s "I will keep an eye out for you."
            elif Girl == JubesX:
                ch_v "I'm still in the shade a bit. . ."

            jump Campus
        elif Girl.Loc in PersonalRooms:
            if Girl == RogueX:
                ch_r "I'll see you there."
            elif Girl == KittyX:
                ch_k "See ya' in a bit. . ."
            elif Girl == EmmaX:
                ch_e "I'll try to keep occupied."
            elif Girl == LauraX:
                ch_l "Yeah, see you."
            elif Girl == JeanX:
                ch_j "Yeah, see you."
            elif Girl == StormX:
                ch_s "I will see you then."
            elif Girl == JubesX:
                ch_v "Yeah, see you."

            $ bg_current = Girl.Loc

            jump Misplaced
        else:
            if Girl == RogueX:
                ch_r "You know, I'll just meet you in my room."
            elif Girl == KittyX:
                ch_k "You know, I'll just meet you in my room."
            elif Girl == EmmaX:
                ch_e "You know, I'll just meet you in my room."
            elif Girl == LauraX:
                ch_l "Um, I'll just meet you in my room."
            elif Girl == JeanX:
                ch_j "Um, I'll just meet you in my room."
            elif Girl == StormX:
                ch_s "I will just meet you in my room."
            elif Girl == JubesX:
                ch_v "Um, I'll just meet you in my room."

            $ Girl.Loc = Girl.Home

            call girls_room(Girl)

            return
    elif line == "lonely":
        if Girl == RogueX:
            ch_r "Oh, how could I say \"no\" to you, [Girl.Petname]?"
        elif Girl == KittyX:
            ch_k "Awwww, how sweet!"
        elif Girl == EmmaX:
            ch_e "Well, we can't have that now."
        elif Girl == LauraX:
            ch_l "You are such a dork!"
        elif Girl == JeanX:
            ch_j "Oh. . . fine. . ."
        elif Girl == StormX:
            ch_s "Why must you be so adorable?"
        elif Girl == JubesX:
            ch_v "Aw, well I can help with that!"
    elif line == "command":
        if Girl == RogueX:
            ch_r "Fine, if you insist, [Girl.Petname]."
        elif Girl == KittyX:
            ch_k "Very well, [KittyX.Petname]."
        elif Girl == EmmaX:
            ch_e "If I must. . ."
        elif Girl == LauraX:
            ch_l "Yes, [LauraX.Petname]."
        elif Girl == JeanX:
            ch_j "Fine, [JeanX.Petname]."
        elif Girl == StormX:
            ch_s "Yes, [StormX.Petname]."
        elif Girl == JubesX:
            ch_v "Ok, [JubesX.Petname]."

    $ Girl.recent_history.append("summoned")

    $ line = 0

    if "locked" in Player.Traits:
        call Locked_Door(Girl)

        return

    call Taboo_Level(0)

    $ Girl.OutfitChange()
    $ Girl.Loc = bg_current

    call set_the_scene

    return

label leave(Girl, temp_modifier = temp_modifier, number_of_Girls = 0):
    if "leaving" in Girl.recent_history:
        $ Girl.DrainWord("leaving")
    else:
        return

    if bg_current == "bg_dangerroom":
        call Gym_Exit([Girl])

    if Girl.Loc == "hold":
        if Girl == RogueX:
            ch_r "I'm heading out for a while, see you later."
        elif Girl == KittyX:
            ch_k "I'm[KittyX.like]going off the grid, see you later."
        elif Girl == EmmaX:
            ch_e "Sorry, I have some business to attend to."
        elif Girl == LauraX:
            ch_l "I'm taking off for a bit, later."
        elif Girl == JeanX:
            ch_j "Ok, I've got work to do, apparently."
        elif Girl == StormX:
            ch_s "I've got some business to take care of."
        elif Girl == JubesX:
            ch_v "Ok, peace out."

        return

    if Girl in Party or "lockedtravels" in Girl.Traits:
        $ Girl.Loc = bg_current

        return

    elif "freetravels" in Girl.Traits or not ApprovalCheck(Girl, 700):
        $ Girl.OutfitChange()

        if number_of_Girls:
            if Girl == KittyX:
                ch_k "Yeah, I'm headed out too."
            elif Girl == EmmaX:
                ch_e "I have to head out as well."
            elif Girl == LauraX:
                ch_l "Yeah, I'm leaving too."
            elif Girl == JeanX:
                ch_j "I'm leaving too."
            elif Girl == StormX:
                ch_s "Yes, I'm leaving too."
            elif Girl == JubesX:
                ch_v "Yes, I'm leaving too."

        if not ApprovalCheck(Girl, 600, "LO"):
            if Girl == RogueX:
                ch_r "I'm headed out, see you later."
        elif Girl in [EmmaX, StormX] in Girl.Loc == "bg_teacher":
            if Girl == EmmaX:
                ch_e "I have a class to teach."
            elif Girl == StormX:
                ch_s "I've got class to teach."
        elif Girl.Loc == "bg_classroom":
            if Girl == RogueX:
                ch_r "I'm headed to class right now, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]headed to class right now."
            elif Girl == EmmaX:
                ch_e "I have some paperwork to take care of."
            elif Girl == LauraX:
                ch_l "I've got class."
            elif Girl == JeanX:
                ch_j "I've got class."
            elif Girl == StormX:
                ch_s "I've got class to teach."
            elif Girl == JubesX:
                ch_v "I've got class."
        elif Girl.Loc == "bg_dangerroom":
            if Girl == RogueX:
                ch_r "I'm hitting the danger room, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]hitting the danger room."
            elif Girl == EmmaX:
                ch_e "I have a workout scheduled."
            elif Girl == LauraX:
                ch_l "I'm hitting the Danger Room."
            elif Girl == JeanX:
                ch_j "I'm getting some exercise."
            elif Girl == StormX:
                ch_s "I am heading for the Danger Room."
            elif Girl == JubesX:
                ch_v "I'm hitting the Danger Room."
        elif Girl.Loc == "bg_campus":
            if Girl == RogueX:
                ch_r "I'm going to hang out on campus, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]going to hang out on campus."
            elif Girl == EmmaX:
                ch_e "I'm going to take in some sun."
            elif Girl == LauraX:
                ch_l "I'm taking a nap in the quad."
            elif Girl == JeanX:
                ch_j "I'm taking a break in the quad."
            elif Girl == StormX:
                ch_s "I am going to relax in the courtyard."
            elif Girl == JubesX:
                ch_v "I'm gonna get some sun."
        elif Girl.Loc == Girl.Home:
            if Girl == RogueX:
                ch_r "I'm heading back to my room, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]heading back to my room."
            elif Girl == EmmaX:
                ch_e "I'm heading back to my room."
            elif Girl == LauraX:
                ch_l "I'm headed back to my room."
            elif Girl == JeanX:
                ch_j "I'm going back to my room."
            elif Girl == StormX:
                ch_s "I am returning to my room."
            elif Girl == JubesX:
                ch_v "I'm headed back to my room."
        elif Girl.Loc == "bg_player":
            if Girl == RogueX:
                ch_r "I'll be heading to your room, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "I'll[KittyX.like]be heading to your room."
            elif Girl == EmmaX:
                ch_e "I'll be heading to your room."
            elif Girl == LauraX:
                ch_l "I'm gonna hang out in your room for a bit."
            elif Girl == JeanX:
                ch_j "I'm hanging out in your room for a bit."
            elif Girl == StormX:
                ch_s "I am planning to relax in your room."
            elif Girl == JubesX:
                ch_v "I'm gonna hang out in your room for a bit."
        elif Girl.Loc == "bg_pool":
            if Girl == RogueX:
                ch_r "I'm headed for the pool."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]hitting up the pool."
            elif Girl == EmmaX:
                ch_e "I was heading for a swim."
            elif Girl == LauraX:
                ch_l "I was hitting the pool."
            elif Girl == JeanX:
                ch_j "I going to hit the pool."
            elif Girl == StormX:
                ch_s "I was going to take a swim."
            elif Girl == JubesX:
                ch_v "I was hitting the pool."
        elif Girl.Loc == "bg_showerroom":
            if ApprovalCheck(Girl, 1400):
                if Girl == RogueX:
                    ch_r "I'm hitting the showers, later."
                elif Girl == KittyX:
                    ch_k "I'm catching a shower, later!"
                elif Girl == EmmaX:
                    ch_e "I'm going to take a quick shower."
                elif Girl == LauraX:
                    ch_l "I'm hitting the showers, later."
                elif Girl == JeanX:
                    ch_j "I'm hitting the showers."
                elif Girl == StormX:
                    ch_s "I am hitting the showers, I will see you later."
                elif Girl == JubesX:
                    ch_v "I'm hitting the showers, later."
            else:
                if Girl == RogueX:
                    ch_r "I'm. . . headed out, see you later."
                elif Girl == KittyX:
                    ch_k "I'm outta here, later!"
                elif Girl == LauraX:
                    ch_l "I'm headed out."
                elif Girl == JeanX:
                    ch_j "I'm headed out."
                elif Girl == StormX:
                    ch_s "I will see you later."
                elif Girl == JubesX:
                    ch_v "I'm headed out."
        else:
            if Girl == RogueX:
                ch_r "I'm headed out, see you later."
            elif Girl == KittyX:
                ch_k "I'm headed out, see you later."
            elif Girl == EmmaX:
                ch_e "I'll see you later."
            elif Girl == LauraX:
                ch_l "I'm headed out, later."
            elif Girl == JeanX:
                ch_j "I'm headed out."
            elif Girl == StormX:
                ch_s "I will see you later."
            elif Girl == JubesX:
                ch_v "I'm headed out, later."

        hide expression Girl.Tag + "_Sprite"

        return

    if bg_current == "bg_dangerroom":
        call Gym_Exit([Girl])

    $ Girl.OutfitChange()

    if "follow" not in Girl.Traits:
        $ Girl.Traits.append("follow")

    $ D20 = renpy.random.randint(1, 20)
    $ line = 0

    if Girl.Loc == "bg_classroom": #fix change these if changed function
        $ temp_modifier = 10
    elif Girl.Loc == "bg_dangerroom":
        $ temp_modifier = 20
    elif Girl.Loc == "bg_showerroom":
        if Girl in [EmmaX, StormX, JubesX]:
            $ temp_modifier = 40
        else:
            $ temp_modifier = 20
    elif Girl in [EmmaX, StormX] and Girl.Loc == "bg_teacher":
        $ temp_modifier = -40

    if number_of_Girls:
        if Girl == KittyX:
            ch_k "Yeah, I'm headed out too."
        elif Girl == EmmaX:
            ch_e "I'm leaving as well."
        elif Girl == LauraX:
            ch_l "Yeah, I'm headed out too."
        elif Girl == JeanX:
            ch_j "Yeah, I'm headed out too."
        elif Girl == StormX:
            ch_s "Yeah, I'm headed out too."
        elif Girl == JubesX:
            ch_v "Yeah, I'm headed out too."

    if Girl.Loc == "bg_classroom":
        if Girl == RogueX:
            ch_r "I'm headed to class right now, [Girl.Petname], you could join me."
        elif Girl == KittyX:
            ch_k "I'm headed to class right now, you could[KittyX.like]join me."
        elif Girl == EmmaX:
            ch_e "I have some paperwork to take care of, but you could keep me company."
        elif Girl == LauraX:
            ch_l "I've got class, want in?"
        elif Girl == JeanX:
            ch_j "I've got class."
        elif Girl == StormX:
            ch_s "I've got class to teach, are you attending?"
        elif Girl == JubesX:
            ch_v "I've got class, you interested?"
    elif Girl in [EmmaX, StormX] and Girl.Loc == "bg_teacher":
        if Girl == EmmaX:
            ch_e "I've got a class to teach, but you could probably learn a thing or two from it."
        elif Girl == StormX:
            ch_s "I've got class to teach, are you attending?"
    elif Girl.Loc == "bg_dangerroom":
        if Girl == RogueX:
            ch_r "I'm hitting the danger room, [Girl.Petname], care to join me?"
        elif Girl == KittyX:
            ch_k "I'm hitting the danger room, care to[KittyX.like]join me?"
        elif Girl == EmmaX:
            ch_e "I have a workout planned, but there's room for one more."
        elif Girl == LauraX:
            ch_l "I've got some Danger Room time, want in?"
        elif Girl == JeanX:
            ch_j "I've got some Danger Room time scheduled."
        elif Girl == StormX:
            ch_s "I am heading for the Danger Room, care to join me?"
        elif Girl == JubesX:
            ch_v "I've got some Danger Room time, you interested?"
    elif Girl.Loc == "bg_campus":
        if Girl == RogueX:
            ch_r "I'm going to hang out on campus, [Girl.Petname], want to hang with me?"
        elif Girl == KittyX:
            ch_k "I'm going to[KittyX.like]hang out on campus, want to chill with me?"
        elif Girl == EmmaX:
            ch_e "I'm planning to get some sunning in, care to join me?"
        elif Girl == LauraX:
            ch_l "I'm taking a nap on the quad, you want in?"
        elif Girl == JeanX:
            ch_j "I'm hanging out on the quad."
        elif Girl == StormX:
            ch_s "I am going to relax in the courtyard, care to join me?"
        elif Girl == JubesX:
            ch_v "I'm gonna get some sun on the quad, you interested?"
    elif Girl.Loc == Girl.Home:
        if Girl == RogueX:
            ch_r "I'm heading back to my room, [Girl.Petname], want to swing by?"
        elif Girl == KittyX:
            ch_k "I'm heading back to my room, want to[KittyX.like]hang out?"
        elif Girl == EmmaX:
            ch_e "I'm heading back to my room, but you can walk me back."
        elif Girl == LauraX:
            ch_l "I'm headed back to my room, you want in?"
        elif Girl == JeanX:
            ch_j "I'm headed back to my room."
        elif Girl == StormX:
            ch_s "I am returning to my room, care to join me?"
        elif Girl == JubesX:
            ch_v "I'm headed back to my room, you interested?"
    elif Girl.Loc == "bg_player":
        if Girl == RogueX:
            ch_r "I'll be heading to your room, [Girl.Petname]."
        elif Girl == KittyX:
            ch_k "I'll[KittyX.like]be heading to your room."
        elif Girl == EmmaX:
            ch_e "I'm actually heading to your room, [EmmaX.Petname]."
        elif Girl == LauraX:
            ch_l "I'm going to hang out in your room for a bit, you coming?"
        elif Girl == JeanX:
            ch_j "I'm going to hang out in your room for a bit."
        elif Girl == StormX:
            ch_s "I am planning to relax in your room, care to join me?"
        elif Girl == JubesX:
            ch_v "I'm going to hang out in your room for a bit, you interested?"
    elif Girl.Loc == "bg_showerroom":
        if ApprovalCheck(Girl, 1600):
            if Girl == RogueX:
                ch_r "I'm hitting the showers, [Girl.Petname], care to join me?"
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]hitting the showers, want to join me?"
            elif Girl == EmmaX:
                ch_e "I'm catching a quick shower, care to join me?"
            elif Girl == LauraX:
                ch_l "I'm hitting the showers, you could use one too."
            elif Girl == JeanX:
                ch_j "I'm hitting the showers."
            elif Girl == StormX:
                ch_s "I am hitting the showers, care to join me?"
            elif Girl == JubesX:
                ch_v "I'm hitting the showers, you should join me."
        else:
            if Girl == RogueX:
                ch_r "I'm hitting the showers, [Girl.Petname], maybe we could touch base later."
            elif Girl == KittyX:
                ch_k "I'm hitting the showers, maybe we could[KittyX.like]touch base later."
            elif Girl == EmmaX:
                ch_e "I'm headed for the showers, make sure to keep your distance."
            elif Girl == LauraX:
                ch_l "I'm hitting the showers, see you later."
            elif Girl == JeanX:
                ch_j "I'm hitting the showers, maybe hang back for a bit."
            elif Girl == StormX:
                ch_s "I will see you later."
            elif Girl == JubesX:
                ch_v "I'm hitting the showers, laters."

            return
    elif Girl.Loc == "bg_pool":
        if Girl == RogueX:
            ch_r "I'm headed for the pool. Wanna come?"
        elif Girl == KittyX:
            ch_k "I'm[KittyX.like]hitting up the pool. You coming?"
        elif Girl == EmmaX:
            ch_e "I was heading for a swim. Care to join me?"
        elif Girl == LauraX:
            ch_l "I was hitting the pool. Wanna come?"
        elif Girl == JeanX:
            ch_j "I was hitting the pool."
        elif Girl == StormX:
            ch_s "I was going to take a swim, care to join me?"
        elif Girl == JubesX:
            ch_v "I was hitting the pool. Wanna come?"
    else: #Location unknown
        if Girl == RogueX:
            ch_r "Why don't you come with me, [Girl.Petname]?"
        elif Girl == KittyX:
            ch_k "Wanna[KittyX.like]come with me, [KittyX.Petname]?"
        elif Girl == EmmaX:
            ch_e "Would you care to come with me?"
        elif Girl == LauraX:
            ch_l "Wanna join me?"
        elif Girl == JeanX:
            ch_j "Are you coming with?"
        elif Girl == StormX:
            ch_s "Care to join me?"
        elif Girl == JubesX:
            ch_v "Wanna join me?"

    menu:
        extend ""
        "Sure, I'll catch up.":
            if "followed" not in Girl.recent_history:
                $ Girl.change_stat("love", 55, 1)
                $ Girl.change_stat("inhibition", 30, 1)

            $ line = "go to"
        "Nah, we can talk later.":
            if "followed" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("obedience", 30, 2)

            if Girl == RogueX:
                ch_r "Oh, ok. Talk to you later then."
            elif Girl == KittyX:
                ch_k "Ok, cool. Talk to you later then."
            elif Girl == EmmaX:
                ch_e "Very well, I'll talk to you later."
            elif Girl == LauraX:
                ch_l "Sure, whatever."
            elif Girl == JeanX:
                ch_j "Fine, whatever."
            elif Girl == StormX:
                ch_s "Very well."
            elif Girl == JubesX:
                ch_v "Sure, whatever."
        "Could you please stay with me? I'll get lonely.":
            if ApprovalCheck(Girl, 600, "L", Alt = [[JubesX], 650]) or ApprovalCheck(Girl, 1400, Alt = [[JubesX], 1500]):
                if "followed" not in Girl.recent_history:
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("obedience", 50, 1)

                $ line = "lonely"
            else:
                if "followed" not in Girl.recent_history:
                    $ Girl.change_stat("inhibition", 30, 1)

                $ line = "no"

                if Girl == JeanX:
                    ch_j "Needy much?"
                elif Girl == StormX:
                    ch_s "Well we cannot have that. . ."
                elif Girl == JubesX:
                    ch_v "Aw, how could I say \"no\"?"
        "Come on, it'll be fun." if Girl in [LauraX, JeanX, StormX, JubesX]:
            if ApprovalCheck(Girl, 400, "L") and ApprovalCheck(Girl, 800):
                $ Girl.change_stat("love", 70, 1)
                $ Girl.change_stat("obedience", 50, 1)

                $ line = "fun"
            else:
                $ Girl.change_stat("inhibition", 30, 1)

                $ line = "no"
        "No, stay here.":
            if ApprovalCheck(Girl, 600, "O"):
                if "followed" not in Girl.recent_history:
                    $ Girl.change_stat("love", 50, 1, 1)
                    $ Girl.change_stat("love", 40, -1)
                    $ Girl.change_stat("obedience", 90, 1)

                $ line = "command"
            elif D20 >= 7 and ApprovalCheck(Girl, 1400):
                if "followed" not in Girl.recent_history:
                    $ Girl.change_stat("love", 70, -2)
                    $ Girl.change_stat("love", 90, -1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("obedience", 90, 1)

                if Girl == RogueX:
                    ch_r "I suppose I can, [Girl.Petname]."
                elif Girl == KittyX:
                    ch_k "Uh, sure, I guess."
                elif Girl == EmmaX:
                    ch_e "I guess it wasn't that important. . ."
                elif Girl == LauraX:
                    ch_l "I guess if you need me here."
                elif Girl == JeanX:
                    ch_j ". . . Fine."
                elif Girl == StormX:
                    ch_s "Fine."
                elif Girl == JubesX:
                    ch_v "I guess I could. . ."

                $ line = "yes"
            elif ApprovalCheck(Girl, 200, "O"):
                if "followed" not in Girl.recent_history:
                    $ Girl.change_stat("love", 70, -4)
                    $ Girl.change_stat("love", 90, -2)

                if Girl == RogueX:
                    ch_r "I don't know who you think you are, boss'in me around like that."
                elif Girl == KittyX:
                    ch_k "[KittyX.Like]in your dreams, [KittyX.Petname]."
                elif Girl == EmmaX:
                    ch_e "Does that work with your little strumpets?"
                elif Girl == LauraX:
                    h_l "Don't tell me what to do."
                elif Girl == JeanX:
                    ch_j "You're not the boss of me."
                elif Girl == StormX:
                    ch_s "And I refused."
                elif Girl == JubesX:
                    ch_v "No way."

                if "followed" not in Girl.recent_history:
                    $ Girl.change_stat("inhibition", 40, 2)
                    $ Girl.change_stat("inhibition", 60, 1)
                    $ Girl.change_stat("obedience", 70, -2)

                if Girl == RogueX:
                    ch_r "If you want to see me, you know where to find me."
                elif Girl == KittyX:
                    ch_k "I'm gone."
                elif Girl == LauraX:
                    ch_l "I'm out of here."
                elif Girl == JeanX:
                    ch_j "Ha!"
                elif Girl == JubesX:
                    ch_v "I'm out of here."
            else:
                if "followed" not in Girl.recent_history:
                    $ Girl.change_stat("inhibition", 30, 1)
                    $ Girl.change_stat("inhibition", 50, 1)
                    $ Girl.change_stat("love", 50, -1, 1)
                    $ Girl.change_stat("obedience", 70, -1)

                $ line = "no"

    $ Girl.recent_history.append("followed")

    if not line:
        hide expression Girl.Tag + "_Sprite"

        call Gym_Clothes_Off([Girl])

        return

    if line == "no":
        if Girl.Loc == "bg_classroom":
            if Girl == RogueX:
                ch_r "I seriously can't, [Girl.Petname], big test coming up."
            elif Girl == KittyX:
                ch_k "Totally can't, [KittyX.Petname], Gotta study for the test."
            elif Girl == EmmaX:
                ch_e "I'm afraid not, [EmmaX.Petname], I need to get this work done."
            elif Girl == LauraX:
                ch_l "I really can't miss this one."
            elif Girl == JeanX:
                ch_j "I'd rather not."
            elif Girl == StormX:
                ch_s "I cannot skip class like this."
            elif Girl == JubesX:
                ch_v "I really can't miss this one."
        elif Girl in [EmmaX, StormX] and Girl.Loc == "bg_teacher":
            if Girl == EmmaX:
                ch_e "I'm not \"cutting class,\" [EmmaX.Petname]."
            elif Girl == StormX:
                ch_s "I cannot skip class like this."
        elif Girl.Loc == "bg_dangerroom":
            if Girl == RogueX:
                ch_r "Wish I could, [Girl.Petname], but I need to get some hours in."
            elif Girl == KittyX:
                ch_k "Sorry [KittyX.Petname], but I[KittyX.like]need the practice?"
            elif Girl == EmmaX:
                ch_e "I'm sorry, but how do you think I keep this figure?"
            elif Girl == LauraX:
                ch_l "Sorry [LauraX.Petname], but I'm going a little stir crazy."
            elif Girl == JeanX:
                ch_j "I'd rather not."
            elif Girl == StormX:
                ch_s "I have work to put in here."
            elif Girl == JubesX:
                ch_v "Sorry [JubesX.Petname], I need the exercise."
        else:
            if Girl == RogueX:
                ch_r "I'm sorry, [Girl.Petname], but I'm kinda busy right now."
            elif Girl == KittyX:
                ch_k "I'm[KittyX.like]sorry, [KittyX.Petname], I've got things to do."
            elif Girl == EmmaX:
                ch_e "I'm sorry, I'm just much too busy at the moment."
            elif Girl == LauraX:
                ch_l "Sorry, I have stuff to do."
            elif Girl == JeanX:
                ch_j "I'd rather not."
            elif Girl == StormX:
                ch_s "I am sorry, [StormX.Petname], I am occupied."
            elif Girl == JubesX:
                ch_v "Sorry, I'm kinda busy."

        hide expression Girl.Tag + "_Sprite"

        call Gym_Clothes_Off([Girl])

        return
    elif line == "go to":
        $ temp_modifier = 0
        $ line = 0

        call DrainAll("leaving")
        call DrainAll("arriving")

        $ Girl.recent_history.append("goto")

        $ Player.recent_history.append("goto")

        hide expression Girl.Tag + "_Sprite"

        call Gym_Clothes_Off([Girl])

        if Girl.Loc == "bg_classroom":
            if Girl == RogueX:
                ch_r "See you then!"
            elif Girl == KittyX:
                ch_k "Cool, study buddy!"
            elif Girl == EmmaX:
                ch_e "Excellent, that should pass the time."
            elif Girl == LauraX:
                ch_l "Ok, get a move on then."
            elif Girl == JeanX:
                ch_j "Ok."
            elif Girl == StormX:
                ch_s "I will see you soon then."
            elif Girl == JubesX:
                ch_v "Ok, get a move on then."

            jump Class_Room_Entry
        elif Girl in [EmmaX, StormX] and Girl.Loc == "bg_teacher":
            if Girl == EmmaX:
                ch_e "I'll see you there."
            elif Girl == StormX:
                ch_s "I will see you soon then."
        elif Girl.Loc == "bg_dangerroom":
            if Girl == RogueX:
                ch_r "I'll be warming up!"
            elif Girl == KittyX:
                ch_k "I'll be ready and waiting!"
            elif Girl == EmmaX:
                ch_e "I'll try to leave some for you."
            elif Girl == LauraX:
                ch_l "I'll get warmed up."
            elif Girl == JeanX:
                ch_j "I'll get warmed up."
            elif Girl == StormX:
                ch_s "I will see you soon then."
            elif Girl == JubesX:
                ch_v "I'll get warmed up."

            jump Danger_Room_Entry
        elif Girl.Loc == Girl.Home:
            if Girl == RogueX:
                ch_r "I'll meet you there."
            elif Girl == KittyX:
                ch_k "I'll meet you there."
            elif Girl == EmmaX:
                ch_e "I'll be waiting."
            elif Girl == LauraX:
                ch_l "Ok."
            elif Girl == JeanX:
                ch_j "Ok."
            elif Girl == StormX:
                ch_s "I will see you soon then."
            elif Girl == JubesX:
                ch_v "Ok."

            call girls_room(Girl)

            return
        elif Girl.Loc == "bg_player":
            if Girl == RogueX:
                ch_r "I'll be waiting."
            elif Girl == KittyX:
                ch_k "I'll be waiting."
            elif Girl == EmmaX:
                ch_e "I'll be waiting."
            elif Girl == LauraX:
                ch_l "Good."
            elif Girl == JeanX:
                ch_j "Good."
            elif Girl == StormX:
                ch_s "I will be waiting."
            elif Girl == JubesX:
                ch_v "Good."

            jump player_room
        elif Girl.Loc == "bg_showerroom":
            if Girl == RogueX:
                ch_r "I guess I'll see you there."
            elif Girl == KittyX:
                ch_k "I guess I'll see you there."
            elif Girl == EmmaX:
                ch_e "I'll get started."
            elif Girl == LauraX:
                ch_l "Ok, nice."
            elif Girl == JeanX:
                ch_j "Ok, nice."
            elif Girl == StormX:
                ch_s "I will leave you some hot water."
            elif Girl == JubesX:
                ch_v "Ok, nice."

            jump Shower_Room_Entry
        elif Girl.Loc == "bg_campus":
            if Girl == RogueX:
                ch_r "Let's head over there."
            elif Girl == KittyX:
                ch_k "Let's head over there."
            elif Girl == EmmaX:
                ch_e "Ok, let's."
            elif Girl == LauraX:
                ch_l "Ok, nice."
            elif Girl == JeanX:
                ch_j "Ok."
            elif Girl == StormX:
                ch_s "I will keep an eye out for you."
            elif Girl == JubesX:
                ch_v "Ok, nice."

            jump Campus_Entry
        elif Girl.Loc == "bg_pool":
            if Girl == RogueX:
                ch_r "Let's head over there."
            elif Girl == KittyX:
                ch_k "Ok, let's go."
            elif Girl == EmmaX:
                ch_e "Ok, let's."
            elif Girl == LauraX:
                ch_l "Cool."
            elif Girl == JeanX:
                ch_j "Cool."
            elif Girl == StormX:
                ch_s "Excellent."
            elif Girl == JubesX:
                ch_v "Cool."

            jump Pool_Entry
        else:
            if Girl in [RogueX, KittyX, EmmaX]:
                ch_r "You know, I'll just meet you in my room."

                $ Girl.Loc = Girl.Home

                call girls_room(Girl)

                return
            elif Girl in [LauraX, JeanX, StormX, JubesX]:
                ch_l "I'll just meet you in your room."

                $ Girl.Loc = "bg_player"

                jump player_room
    elif line == "lonely":
        if Girl == RogueX:
            ch_r "Oh, how could I say \"no\" to you, [Girl.Petname]?"
        elif Girl == KittyX:
            ch_k "I guess[KittyX.like]I couldn't leave you lonely. . ."
        elif Girl == EmmaX:
            ch_e "Well we wouldn't want that. . ."
        elif Girl == LauraX:
            ch_l "Well, I guess you should never go alone. . ."
        elif Girl == JeanX:
            ch_j "Well, I guess. . ."
        elif Girl == StormX:
            ch_s "Why must you be so adorable?"
        elif Girl == JubesX:
            ch_v "Aw, well I can help with that!"
    elif line == "command":
        if Girl == RogueX:
            ch_r "Fine, if you insist, [Girl.Petname]."
        elif Girl == KittyX:
            ch_k "Humph, ok."
        elif Girl == EmmaX:
            ch_e "If you insist."
        elif Girl == LauraX:
            ch_l "Yes [LauraX.Petname]."
        elif Girl == JeanX:
            ch_j "Fine, [JeanX.Petname]. . ."
        elif Girl == StormX:
            ch_s "Yes, [StormX.Petname]."
        elif Girl == JubesX:
            ch_v "Ok, [JubesX.Petname]."

    $ line = 0

    if Girl == RogueX:
        ch_r "I can stay for a bit."
    elif Girl == KittyX:
        ch_k "I guess I can stick around."
    elif Girl == EmmaX:
        ch_e "I suppose I can stay for a while."
    elif Girl == LauraX:
        ch_l "I'll stick around."
    elif Girl == JeanX:
        ch_j "I'll stick around."
    elif Girl == StormX:
        ch_s "I'll stick around."
    elif Girl == JubesX:
        ch_v "I'll stay here."

    $ Girl.Loc = bg_current

    call Taboo_Level(0)

    return
