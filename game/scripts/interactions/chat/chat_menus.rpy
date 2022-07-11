label chat_menu(Girl):
    hide screen Girl_picker

    $ shift_focus(Girl)

    $ chatting = True

    while chatting:
        menu:
            "Ask [Girl.name] to leave" if Girl.location == Player.location:
                call dismiss(Girl)

                $ chatting = False
            "Romance her":
                menu:
                    "Sex Menu" if Girl.location == Player.location:
                        if Girl.love >= Girl.obedience:
                            Player.voice "Did you want to fool around?"
                        else:
                            Player.voice "I'd like to get naughty."

                        if approval_check(Girl, 600, "LI"):
                            $ Girl.change_face("sexy")

                            if Girl == RogueX:
                                Girl.voice "Heh, all right, [Girl.player_petname]."
                            elif Girl == KittyX:
                                Girl.voice "Mmmm, ok, [Girl.player_petname]."
                            elif Girl == EmmaX:
                                Girl.voice "Perhaps. . ."
                            elif Girl == LauraX:
                                Girl.voice "Cool."
                            elif Girl == JeanX:
                                Girl.voice "Yeah?"
                            elif Girl == StormX:
                                Girl.voice "Oh?"
                            elif Girl == JubesX:
                                Girl.voice "Yeah?"
                            elif Girl == MystiqueX:
                                Girl.voice "Mhm. . . ?"

                            call enter_main_sex_menu(Girl)
                        elif approval_check(Girl, 400, "OI"):
                            if Girl == RogueX:
                                Girl.voice "If that's what you want, [Girl.player_petname]."
                            elif Girl == KittyX:
                                Girl.voice "Yes, [Girl.player_petname]."
                            elif Girl == EmmaX:
                                Girl.voice "If that's what you want, [Girl.player_petname]."
                            elif Girl == LauraX:
                                Girl.voice "Yes, [Girl.player_petname]."
                            elif Girl == JeanX:
                                Girl.voice "Whatever. . ."
                            elif Girl == StormX:
                                Girl.voice "Fine."
                            elif Girl == JubesX:
                                Girl.voice "What would you like, [Girl.player_petname]?"
                            elif Girl == MystiqueX:
                                Girl.voice "What would you like, [Girl.player_petname]?"

                            call enter_main_sex_menu(Girl)
                        else:
                            if Girl == RogueX:
                                Girl.voice "I'm not really interested, [Girl.player_petname]."
                            elif Girl == KittyX:
                                Girl.voice "No thanks, [Girl.player_petname]."
                            elif Girl == EmmaX:
                                Girl.voice "No thank you, [Girl.player_petname]."
                            elif Girl == LauraX:
                                Girl.voice "No thanks, [Girl.player_petname]."
                            elif Girl == JeanX:
                                Girl.voice "Not interested."
                            elif Girl == StormX:
                                Girl.voice "I am uninterested."
                            elif Girl == JubesX:
                                Girl.voice "Nah, not into it."
                            elif Girl == MystiqueX:
                                Girl.voice "No."
                    "Sex Menu (locked)" if Girl.location != Player.location:
                        pass
                    "Back":
                        pass
            "Talk with her":
                menu:
                    "Could I get your number?" if Girl not in Player.Phonebook:
                        if Girl == EmmaX and approval_check(Girl, 800, "LI"):
                            Girl.voice "I don't see why not."

                            $ Player.Phonebook.append(Girl)
                        elif Girl != EmmaX and(approval_check(Girl, 400, "L") or approval_check(Girl, 200, "I")):
                            if Girl == RogueX:
                                Girl.voice "Sure, I suppose."
                            elif Girl == KittyX:
                                Girl.voice "OMG[Girl.like]sure."
                            elif Girl == LauraX:
                                Girl.voice "Oh, sure."
                            elif Girl == JeanX:
                                Girl.voice "Huh? Ok."
                            elif Girl == StormX:
                                Girl.voice "Oh? Certainly."
                            elif Girl == JubesX:
                                Girl.voice "Sure, yeah."
                            elif Girl == MystiqueX:
                                Girl.voice "You may."

                            $ Player.Phonebook.append(Girl)
                        elif approval_check(Girl, 200, "O", alternate_thresholds = {EmmaX: 500 - Girl.inhibition}):
                            if Girl == RogueX:
                                Girl.voice "If you want it, I guess."
                            elif Girl == KittyX:
                                Girl.voice "[Girl.Like]fine."
                            elif Girl == EmmaX:
                                Girl.voice "Hmm. . . fine, hand me your phone."
                            elif Girl == LauraX:
                                Girl.voice "I guess."
                            elif Girl == JeanX:
                                Girl.voice "Huh? Ok."
                            elif Girl == StormX:
                                Girl.voice "I don't see why not."
                            elif Girl == JubesX:
                                Girl.voice "I guess?"
                            elif Girl == MystiqueX:
                                Girl.voice "Hmm. . . ok."

                            $ Player.Phonebook.append(Girl)
                        else:
                            if Girl == RogueX:
                                Girl.voice "I don't really want you calling me."
                            elif Girl == KittyX:
                                Girl.voice "[Girl.Like]I'd rather not?"
                            elif Girl == EmmaX:
                                Girl.voice "I don't think it's appropriate to give my number out to a student like that."
                            elif Girl == LauraX:
                                Girl.voice "Um, probably not."
                            elif Girl == JeanX:
                                Girl.voice "I'd rather you didn't call me."
                            elif Girl == StormX:
                                Girl.voice "I would rather not."
                            elif Girl == JubesX:
                                Girl.voice "Nah, unlisted."
                            elif Girl == MystiqueX:
                                Girl.voice "Not likely."
                    "Back":
                        pass
            "Add her to party" if Girl not in Player.Party and Girl.location == Player.location:
                Player.voice "Could you follow me for a bit?"

                if Girl == EmmaX and approval_check(Girl, 1250):
                    $ Player.Party.append(Girl)

                    Girl.voice "Lead away."

                if approval_check(Girl, 600, alternate_thresholds = {EmmaX: 900, JeanX: 900, MystiqueX: 1000}):
                    $ Player.Party.append(Girl)

                    if Girl == RogueX:
                        Girl.voice "Ok, Where did you want to go?"
                    elif Girl == KittyX:
                        Girl.voice "[Girl.Like]where to?"
                    elif Girl == EmmaX:
                        Girl.voice "You'd better not bore me."
                    elif Girl == LauraX:
                        Girl.voice "Where to?"
                    elif Girl == JeanX:
                        Girl.voice "Um, sure."
                    elif Girl == StormX:
                        Girl.voice "Oh, certainly."
                    elif Girl == JubesX:
                        Girl.voice "Sure, what's up?"
                    elif Girl == MystiqueX:
                        Girl.voice "Where to, [Girl.player_petname]?"
                elif not approval_check(Girl, 400):
                    if Girl == RogueX:
                        Girl.voice "Um, no thanks."
                    elif Girl == KittyX:
                        Girl.voice "Ew, no."
                    elif Girl == EmmaX:
                        Girl.voice "I can't imagine why I would."
                    elif Girl == LauraX:
                        Girl.voice "No."
                    elif Girl == JeanX:
                        Girl.voice "What? No."
                    elif Girl == StormX:
                        Girl.voice "Hm, no thank you."
                    elif Girl == JubesX:
                        Girl.voice "Nah, not into it."
                    elif Girl == MystiqueX:
                        Girl.voice "Ah, no."
                else:
                    if Girl == RogueX:
                        Girl.voice "I'm fine here, thanks."
                    elif Girl == KittyX:
                        Girl.voice "I think I'll stay here."
                    elif Girl == EmmaX:
                        Girl.voice "I'd rather not."
                    elif Girl == LauraX:
                        Girl.voice "I'd rather not."
                    elif Girl == JeanX:
                        Girl.voice "What? No."
                    elif Girl == StormX:
                        Girl.voice "I'm comfortable here."
                    elif Girl == JubesX:
                        Girl.voice "Def not."
                    elif Girl == MystiqueX:
                        Girl.voice "Not this time."
            "Disband party" if Girl in Player.Party:
                Player.voice "Ok, you can leave if you prefer."

                python:
                    for G in Player.Party:
                        Player.Party.remove(G)
            "Never mind.":
                if Girl == RogueX:
                    Girl.voice "Ok, later then."
                elif Girl == KittyX:
                    Girl.voice "Ok, bye."
                elif Girl == EmmaX:
                    Girl.voice "We'll talk later then."
                elif Girl == LauraX:
                    Girl.voice "Ok."
                elif Girl == JeanX:
                    Girl.voice "Ok?"
                elif Girl == StormX:
                    Girl.voice "Very well then."
                elif Girl == JubesX:
                    Girl.voice "K."
                elif Girl == MystiqueX:
                    Girl.voice "Very well."

                $ chatting = False

    return

label text_menu(Girl):
    hide screen Girl_picker
    nvl clear

    $ shift_focus(Girl)

    Player.text "Hey."

    if Girl == RogueX:
        $ line = "hey " + Girl.player_petname + "."
    elif Girl == KittyX:
        $ line = "oh hey " + Girl.player_petname + "."
    elif Girl == EmmaX:
        $ line = "Yes?"
    elif Girl == LauraX:
        $ line = "Watsup?"
    elif Girl == JeanX:
        $ line = "hi"
    elif Girl == StormX:
        $ line = "Hello."
    elif Girl == JubesX:
        $ line = "hey!"
    elif Girl == MystiqueX:
        $ line = "Yes, " + Girl.player_petname + "?"

    menu(nvl = True):
        Girl.text "[line]"
        "Want to come over?":
            Player.text "Want to come over?"

            call summon(Girl)
        "Never mind.":
            Player.text "Never mind."

            if Girl == RogueX:
                Girl.text "ok. . ."
            elif Girl == KittyX:
                Girl.text "???"
            elif Girl == EmmaX:
                Girl.text "Try not to waste my time."
            elif Girl == LauraX:
                Girl.text "Huh?"
            elif Girl == StormX:
                Girl.text "Ok."
            elif Girl == JubesX:
                Girl.text "uh"

    return
