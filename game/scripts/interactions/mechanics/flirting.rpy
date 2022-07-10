
label Flirt(Girl=0):

    $ Girl = check_girl(Girl)
    $ shift_focus (Girl)

    if Girl.location != Player.location:

        menu:
            "Compliment her":
                $ Girl.had_chat[5] = 1
                call Compliment (Girl)


            "Phone Sex" if Player.location == "bg_player":
                ch_p "Want to do some phone sex?"
                call set_Character_taboos
                if not approval_check(Girl, 900) or Girl.SEXP < 15:

                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                if Girl.taboo and approval_check(Girl, 1400):

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
                    if Girl in (EmmaX, StormX) and Girl.location == "bg_classroom" and time_index >= 2:
                        pass
                    else:
                        $ Girl.location = Girl.home
                elif approval_check(Girl, 1200):

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
                elif Girl.taboo:

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
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
                call set_Character_taboos
                call PhoneSex (Girl)
                call set_Character_taboos
                $ renpy.pop_call()
                return
            "Phone Sex [[not here] (locked)" if Player.location != "bg_player":
                pass
            "Never mind [[exit]":
                pass
    else:

        $ Girl.had_chat[5] = 1
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
                if approval_check(Girl, 650, "L", taboo_modifier = 1):
                    $ Girl.change_face("sexy", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
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
                        $ Girl.change_face("sexy", 1, eyes = "side")
                        ch_l "Huh."
                    elif Girl == JeanX:
                        ch_j "Huh."
                    elif Girl == StormX:
                        ch_s "Oh, hello there. . ."
                    elif Girl == JubesX:
                        ch_v "Oh, hey. . ."
                elif approval_check(Girl, 500, "L", taboo_modifier = 1):
                    $ Girl.change_face("surprised", 1)
                    call change_Girl_stat(Girl, "love", 2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
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
                elif approval_check(Girl, 300, "L", taboo_modifier = 1):
                    $ Girl.change_face("angry", 1)
                    call change_Girl_stat(Girl, "love", 2])
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
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
                    call change_Girl_stat(Girl, "love", 2])
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 3)
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

                if approval_check(Girl, 1000, taboo_modifier=2, Alt = [[RogueX],800]) or approval_check(Girl, 600, "L", taboo_modifier=2):
                    $ line = renpy.random.choice(["You lean over, put your hand against her cheek, and plant a kiss on her lips.",
                                                                    "You lean down, tilt her head back, and plant a kiss on her lips.",
                                                                    "You turn " + Girl.name + " around and plant a deep kiss on her."])
                    "[line]"
                elif approval_check(Girl, 1000, Alt = [[RogueX],800]) or approval_check(Girl, 600, "L"):
                    $ Girl.change_face("bemused", 1)
                    $ Girl.eyes = "side"
                    call change_Girl_stat(Girl, "obedience", 2])
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    call change_Girl_stat(Girl, "love", 2])
                    call change_Girl_stat(Girl, "obedience", 1])
                    call change_Girl_stat(Girl, "inhibition", 5)
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
                if Girl.permanent_History["kiss"]:

                    if approval_check(Girl, 750, "L", taboo_modifier = 1):
                        $ Girl.change_face("sexy", 1)
                        call change_Girl_stat(Girl, "love", 2)
                        call change_Girl_stat(Girl, "obedience", 2)
                        if Girl == RogueX:
                            ch_r "Hmm we should do that again, [Girl.player_petname]."
                        else:
                            Girl.voice "Mmmmmmm. . ."
                    elif approval_check(Girl, 650, "L", taboo_modifier = 1):
                        $ Girl.change_face("sexy", 1)
                        call change_Girl_stat(Girl, "love", 2)
                        call change_Girl_stat(Girl, "obedience", 2)
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
                    elif approval_check(Girl, 500, "L", taboo_modifier = 1):
                        $ Girl.change_face("surprised", 1)
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "obedience", 2)
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
                    elif approval_check(Girl, 300, "L", taboo_modifier = 1):
                        $ Girl.change_face("angry", 1)
                        call change_Girl_stat(Girl, "love", -1])
                        call change_Girl_stat(Girl, "obedience", 3)
                        call change_Girl_stat(Girl, "inhibition", 2)
                        if Girl == RogueX:
                            ch_r "That really wasn't appropriate, [Girl.player_petname]!"
                        elif Girl == KittyX:
                            ch_k "Dude!"
                        elif Girl == EmmaX:
                            ch_e "Highly inappropriate!"
                            $ Girl.change_face("bemused", eyes = "side")
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
                        call change_Girl_stat(Girl, "love", -3])
                        call change_Girl_stat(Girl, "obedience", 6)
                        call change_Girl_stat(Girl, "inhibition", 3)
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

                    if approval_check(Girl, 750, "L", taboo_modifier = 1):
                        $ Girl.change_face("surprised", 1)
                        call change_Girl_stat(Girl, "love", 45)
                        call change_Girl_stat(Girl, "obedience", 20)
                        call change_Girl_stat(Girl, "inhibition", 35)
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
                            $ Girl.change_face("normal", eyes = "side")
                            ch_l ". . ."
                            $ Girl.change_face("sexy", eyes = "side")
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
                    elif approval_check(Girl, 650, "L", taboo_modifier = 1):
                        $ Girl.change_face("surprised", 1)
                        call change_Girl_stat(Girl, "love", 30)
                        call change_Girl_stat(Girl, "obedience", 25)
                        call change_Girl_stat(Girl, "inhibition", 35)
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
                    elif approval_check(Girl, 500, "L", taboo_modifier = 1):
                        $ Girl.change_face("surprised", 1)
                        call change_Girl_stat(Girl, "obedience", 30)
                        call change_Girl_stat(Girl, "inhibition", 35)
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
                    elif approval_check(Girl, 700, taboo_modifier = 1):
                        $ Girl.change_face("angry", 1)
                        call change_Girl_stat(Girl, "love", -2])
                        call change_Girl_stat(Girl, "obedience", 40)
                        call change_Girl_stat(Girl, "inhibition", 40)
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
                        call change_Girl_stat(Girl, "love", -5])
                        call change_Girl_stat(Girl, "obedience", 50)
                        call change_Girl_stat(Girl, "inhibition", 40)
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

                $ Girl.permanent_History["kiss"] += 1
                $ Girl.addiction -= 1
                $ Girl.addiction_rate += 1
                $ Girl.addiction_rate = 3 if Girl.addiction_rate < 3 else Girl.addiction_rate

                if Girl.taboo and Girl == EmmaX:
                    if "threesome" not in EmmaX.history:
                        if not check_if_alone(EmmaX):

                            call Emma_ThreeCheck



                if approval_check(Girl, 650, taboo_modifier = 1):
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
                            call change_Girl_stat(Girl, "lust", 3)
                            call change_Girl_stat(Girl, "love", 1)
                            call change_Girl_stat(Girl, "love", 3)
                            call change_Girl_stat(Girl, "inhibition", 2)
                            if Player.location == "bg_halloween":
                                "She shrugs away from you and winks."
                                Girl.voice "Not now. . ."
                            else:
                                $ shift_focus(Girl)
                                $ Player.primary_Action = "kiss"
                                call stop_all_Actions (1)
                            return
                        "Just a taste [[no].":
                            $ Girl.change_face("bemused", 1)
                            call change_Girl_stat(Girl, "lust", 1)
                            call change_Girl_stat(Girl, "lust", 4)
                            call change_Girl_stat(Girl, "obedience", 2)
                            call change_Girl_stat(Girl, "inhibition", 2)
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
                            call change_Girl_stat(Girl, "love", -2)
                            call change_Girl_stat(Girl, "obedience", 3)
                            call change_Girl_stat(Girl, "inhibition", 1)
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


                if approval_check(Girl, 200, taboo_modifier = 1):
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
                    call change_Girl_stat(Girl, "lust", 3)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)
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
                elif approval_check(Girl, 600, "L", taboo_modifier = 1):
                    $ Girl.change_face("sexy")
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
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
                elif approval_check(Girl, 450, taboo_modifier = 1, Alt = [[JeanX], 500]):
                    $ Girl.change_face("surprised", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
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
                elif approval_check(Girl, 350, taboo_modifier = 1, Alt = [[JeanX],400]):
                    $ Girl.change_face("angry", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
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


                call slap_ass (Girl)
            "Pinch her ass":

                $ Girl.change_face("surprised", 1)
                if Girl.SEXP < 5 or not approval_check(Girl, 600, taboo_modifier = 1):
                    "You come up to [Girl.name] from behind and quickly pinch her butt."
                    $ Girl.change_face("angry")
                    call change_Girl_stat(Girl, "love", -4)
                    call change_Girl_stat(Girl, "love", -4)
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
                    call change_Girl_stat(Girl, "lust", 3)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 3)
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
                elif approval_check(Girl, 800, "L", taboo_modifier = 1):
                    $ Girl.change_face("sexy")
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                elif approval_check(Girl, 900, taboo_modifier = 1):
                    $ Girl.change_face("surprised")
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                elif approval_check(Girl, 800, taboo_modifier = 1):
                    $ Girl.change_face("angry")
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "inhibition", 3)
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


            "Flip her skirt up" if (Girl.Clothes["dress"] and not Girl.dress_upskirt) or (Girl.wearing_skirt and not Girl.upskirt):
                $ Girl.change_face("surprised", 1)

                if Girl.Clothes["dress"]:
                    $ Girl.dress_upskirt = True
                elif Girl.wearing_skirt:
                    $ Girl.upskirt = True

                pause 0.5

                "You sneak up on [Girl.name] from behind and flip her skirt up quickly!"

                if Girl.Clothes["dress"]:
                    $ Girl.dress_upskirt = False
                elif Girl.wearing_skirt:
                    $ Girl.upskirt = False

                if Girl.Clothes["underwear"] and not Girl.taboo:

                    if approval_check(Girl, 750, "L", taboo_modifier=2):
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
                        call change_Girl_stat(Girl, "love", 3)
                    elif approval_check(Girl, 650, "L", taboo_modifier=2):
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
                    elif approval_check(Girl, 300, "I", taboo_modifier = 1):
                        $ Girl.change_face("sexy", 1)
                        if Girl == KittyX:
                            ch_k "What's the deal?"
                        else:
                            Girl.voice "Hey, what do you think you're doing, [Girl.player_petname]?"
                    elif approval_check(Girl, 300, taboo_modifier = 1) or Girl == LauraX:
                        $ Girl.change_face("angry", 1)
                        call change_Girl_stat(Girl, "love", -3)
                        call change_Girl_stat(Girl, "obedience", 1)
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
                        call change_Girl_stat(Girl, "love", -5)
                        call change_Girl_stat(Girl, "obedience", 2)
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
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    $ Girl.seen_underwear = 1


                elif Girl.Clothes["underwear"]:

                    if approval_check(Girl, 750, "L") and approval_check(Girl, 1300, taboo_modifier=2):
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
                        call change_Girl_stat(Girl, "love", 3)
                    elif approval_check(Girl, 600, "L") and approval_check(Girl, 1200, taboo_modifier=2):
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
                    elif approval_check(Girl, 600, "L"):
                        $ Girl.change_face("angry", 1)
                        call change_Girl_stat(Girl, "love", -3)
                        call change_Girl_stat(Girl, "obedience", 3)
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
                    elif approval_check(Girl, 800, taboo_modifier=2):
                        $ Girl.change_face("angry", 1)
                        call change_Girl_stat(Girl, "love", -5)
                        call change_Girl_stat(Girl, "obedience", 2)
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
                        call change_Girl_stat(Girl, "love", -10)
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "inhibition", 1)
                        if Girl == EmmaX:
                            ch_e "Are you out of your mind, [Girl.player_petname]?"
                        elif Girl == LauraX:
                            ch_l "Dude!"
                        elif Girl == StormX:
                            ch_s ". . ."
                        else:
                            Girl.voice "What the fuck, [Girl.player_petname]!"
                        Girl.voice "Why would you even do that in public?"
                    call change_Girl_stat(Girl, "obedience", 7)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    $ Girl.seen_underwear = 1


                elif not Girl.taboo:

                    if approval_check(Girl, 850, "L"):
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
                    elif approval_check(Girl, 700, "L"):
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
                    elif approval_check(Girl, 600, "L"):
                        $ Girl.change_face("bemused", 1)
                        call change_Girl_stat(Girl, "love", -3)
                        call change_Girl_stat(Girl, "obedience", 3)
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
                    elif approval_check(Girl, 500):
                        $ Girl.change_face("angry", 1)
                        call change_Girl_stat(Girl, "love", -5)
                        call change_Girl_stat(Girl, "obedience", 2)
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
                        call change_Girl_stat(Girl, "love", -10)
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "inhibition", 1)
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
                    call change_Girl_stat(Girl, "obedience", 7)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    call expression Girl.tag + "_First_Bottomless"
                else:



                    if approval_check(Girl, 850, "L") and approval_check(Girl, 1500):
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
                    elif approval_check(Girl, 700, "L") and approval_check(Girl, 1500):
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
                    elif approval_check(Girl, 700):
                        $ Girl.change_face("bemused", 1)
                        call change_Girl_stat(Girl, "love", -3)
                        call change_Girl_stat(Girl, "obedience", 3)
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
                    elif approval_check(Girl, 1000):
                        $ Girl.change_face("angry", 1)
                        call change_Girl_stat(Girl, "love", -5)
                        call change_Girl_stat(Girl, "obedience", 2)
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
                        call change_Girl_stat(Girl, "love", -10)
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "inhibition", 1)
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
                    call change_Girl_stat(Girl, "obedience", 7)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    call change_Girl_stat(Girl, "inhibition", 4)
                    call expression Girl.tag + "_First_Bottomless"

                call change_Girl_stat(Girl, "lust", 1)
                if "exhibitionist" in Girl.traits:
                    call change_Girl_stat(Girl, "lust", 4)
            "Grab her tit":


                $ Girl.change_face("surprised", 1)
                "You come up to [Girl.name] and quickly honk her boob."
                if Girl.SEXP < 5 or not approval_check(Girl, 600, taboo_modifier=2):
                    "You come up to [Girl.name] and quickly honk her boob."
                    $ Girl.change_face("angry")
                    call change_Girl_stat(Girl, "love", -5)
                    call change_Girl_stat(Girl, "love", -5)
                    call punch
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
                        $ JubesX.arm_pose = 1
                        show Fireworks as Fire1 onlayer black:
                            pos (JubesX.sprite_location+160, 270)
                        show Fireworks as Fire2 onlayer black:
                            pos (JubesX.sprite_location+160, 270)
                        ch_v "Back it up. . ."
                    return
                if Girl.SEXP >= 40:
                    call change_Girl_stat(Girl, "lust", 5)
                    call change_Girl_stat(Girl, "love", 2)
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
                elif approval_check(Girl, 800, "L", taboo_modifier = 1):
                    $ Girl.change_face("sexy")
                    call change_Girl_stat(Girl, "lust", 2)
                    call change_Girl_stat(Girl, "love", 1)
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
                elif approval_check(Girl, 1000, taboo_modifier = 1):
                    $ Girl.change_face("perplexed")
                    call change_Girl_stat(Girl, "lust", 1)
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
                elif approval_check(Girl, 800, taboo_modifier = 1):
                    $ Girl.change_face("angry")
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "obedience", 4)
                    call change_Girl_stat(Girl, "inhibition", 3)
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
                    call change_Girl_stat(Girl, "love", -5)
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    if Girl == RogueX:
                        ch_r "Move it or lose it, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "You wanna lose that hand?"
                    elif Girl == EmmaX:
                        ch_e "Do you want to lose that hand?"
                    elif Girl == LauraX:
                        $ Girl.arm_pose = 2
                        $ LauraX.claws = 1
                        ch_l "You wanna lose that hand?"
                    elif Girl == JeanX:
                        ch_j "Excuse me?"
                    elif Girl == StormX:
                        ch_s "That is my breast. . . could you release it."
                    elif Girl == JubesX:
                        $ Girl.arm_pose = 1
                        ch_v "Do I need to spray you, [Girl.player_petname]?"
                    $ Count = 2
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "inhibition", 2)
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
                        call change_Girl_stat(Girl, "lust", 2)
                        call change_Girl_stat(Girl, "inhibition", 1)
                    elif Count == 3:
                        $ Girl.change_face("perplexed")
                        call change_Girl_stat(Girl, "lust", 1)
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
                        call change_Girl_stat(Girl, "love", -1)
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
                            $ JubesX.arm_pose = 1
                            ch_v "Ok, cut that out or you get the hose. . ."
                    elif Count == 1:
                        $ Girl.change_face("angry")
                        call change_Girl_stat(Girl, "love", -5)
                        if Girl == RogueX:
                            ch_r "Back the hell off, [Girl.player_petname]!"
                            call punch
                            "She slaps your hand away and smacks your face."
                            ch_r "What the fuck, [Girl.player_petname]?"
                        elif Girl == KittyX:
                            ch_k "Back it up, [Girl.player_petname]!"
                            call punch
                            "She elbows you in the ribs."
                            ch_k "WTF, [Girl.player_petname]?"
                        elif Girl == EmmaX:
                            ch_e "Time to stop, [Girl.player_petname]."
                            call punch
                            "She elbows you in the ribs."
                            ch_e "You should learn from social cues. . ."
                        elif Girl == LauraX:
                            ch_l "Take a step back, [Girl.player_petname]!"
                            call punch
                            "She gives you a quick shove."
                        elif Girl == JeanX:
                            $ JeanX.eyes = "psychic"
                            call punch
                            "You feel something slam the back of your head."
                            ch_j "Ok, that's good."
                            $ JeanX.eyes = "squint"
                        elif Girl == StormX:
                            ch_s "That is enough, [Girl.player_petname]."
                            call punch
                            "She elbows you in the ribs."
                            ch_s "Everything in moderation. . ."
                        elif Girl == JubesX:
                            $ JubesX.arm_pose = 1
                            show Fireworks as Fire1 onlayer black:
                                pos (JubesX.sprite_location+160, 270)
                            show Fireworks as Fire2 onlayer black:
                                pos (JubesX.sprite_location+160, 270)
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
                                    call change_Girl_stat(Girl, "lust", 2)
                                    call change_Girl_stat(Girl, "inhibition", 1)
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
                                    call change_Girl_stat(Girl, "lust", 4)
                                    call change_Girl_stat(Girl, "inhibition", 1)
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
                                call change_Girl_stat(Girl, "obedience", 3)
                                call change_Girl_stat(Girl, "inhibition", 2)
                                $ Count = 0
                            "Fondle it a little":

                                if Girl.permanent_History["fondle_breasts"]and approval_check(Girl, 1000, taboo_modifier=2):
                                    $ Girl.change_face("sexy", 1)
                                    $ Girl.eyes = "closed"
                                    call change_Girl_stat(Girl, "lust", 5)
                                else:
                                    $ Girl.change_face("perplexed")
                                    call change_Girl_stat(Girl, "lust", 2)
                                    $ Count -= 1
                                call change_Girl_stat(Girl, "obedience", 4)
                                call change_Girl_stat(Girl, "inhibition", 2)
                                if Girl == EmmaX:
                                    ch_e "Mmm. . ."
                                elif Girl == LauraX:
                                    ch_l "Hmm. . ."
                                else:
                                    Girl.voice "Umm. . ."
                            "Just leave it there.":

                                if Count == 5:
                                    $ Girl.change_face("perplexed")
                                    call change_Girl_stat(Girl, "lust", 3)
                                    if Girl == RogueX:
                                        ch_r "This is a bit odd."
                                    else:
                                        Girl.voice "Huh."
                                elif Count == 2:
                                    $ Girl.change_face("perplexed")
                                    call change_Girl_stat(Girl, "lust", 1)
                                    if Girl == EmmaX:
                                        ch_e "Um, [EmmaX.player_petname]."
                                    elif Girl == LauraX:
                                        ch_l "This is getting uncomfortable."
                                    else:
                                        Girl.voice "This is getting a little uncomfortable."
                                call change_Girl_stat(Girl, "obedience", 2)
                                call change_Girl_stat(Girl, "inhibition", 1)

                if Girl == LauraX:
                    $ LauraX.arm_pose = 1
                    $ LauraX.claws = 0
                if Girl == EmmaX and taboo and "taboo" not in EmmaX.history:
                    ch_e "Show some respect when in public, [EmmaX.player_petname]."
                elif Player.location == "bg_halloween":
                    "She shrugs away from you and winks."
                    Girl.voice "Not now. . ."
                elif Girl.permanent_History["fondle_breasts"]and approval_check(Girl, 1100, taboo_modifier = 3):
                    $ Girl.change_face("sexy", 1)
                    if Girl == RogueX:
                        ch_r "You know, maybe we could keep this party roll'in. . ."
                    elif Girl == KittyX:
                        ch_k "I wouldn't mind if we kept. . . you know. . ."
                    elif Girl == EmmaX:
                        if "threesome" not in EmmaX.history and not check_if_alone(EmmaX):

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
                            call change_Girl_stat(Girl, "lust", 5)
                            call change_Girl_stat(Girl, "love", 2)
                            call change_Girl_stat(Girl, "obedience", 3)
                            call change_Girl_stat(Girl, "inhibition", 3)
                            call before_action(Girl, "fondle_breasts")
                            call stop_all_Actions (1)
                            return
                        "Nah, that was enough.":
                            $ Girl.change_face("sad", 1)
                            call change_Girl_stat(Girl, "lust", 2)
                            call change_Girl_stat(Girl, "love", -1)
                            call change_Girl_stat(Girl, "obedience", 4)
                            call change_Girl_stat(Girl, "inhibition", 3)
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
                elif approval_check(Girl, 800, taboo_modifier = 3):
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
                elif approval_check(Girl, 800):
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
                    call change_Girl_stat(Girl, "lust", 3)
                    call change_Girl_stat(Girl, "love", 2)
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
                elif approval_check(Girl, 650, "L", Alt = [[RogueX], 600]):
                    $ Girl.change_face("sexy")
                    call change_Girl_stat(Girl, "lust", 1)
                    call change_Girl_stat(Girl, "love", 2)
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
                elif approval_check(Girl, 500, Alt = [[RogueX],450]):
                    $ Girl.change_face("surprised", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    if Girl == EmmaX:
                        ch_e "Well hello, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "Oh, hey there, [Girl.player_petname]."
                    elif Girl == StormX:
                        ch_s "Hello, [Girl.player_petname]."
                    else:
                        Girl.voice "Oh, hey, [Girl.player_petname]. What's up?"
                elif approval_check(Girl, 350):
                    $ Girl.change_face("angry", 1)
                    call change_Girl_stat(Girl, "love", -1)
                    if Girl == RogueX:
                        if Girl.taboo:
                            ch_r "Hey, um, ease up on the PDAs there, [Girl.player_petname]."
                        else:
                            ch_r "Whoa, um, give me some space here."
                    elif Girl == KittyX:
                        if Girl.taboo:
                            ch_k "Hey[Girl.like]maybe chill out, [Girl.player_petname]?"
                        else:
                            ch_k "Whoa, back it up."
                    elif Girl == EmmaX:
                        if Girl.taboo:
                            ch_e "Do I have to explain boundaries to you, [Girl.player_petname]?"
                        else:
                            ch_e "I'd rather you didn't. . ."
                    elif Girl == LauraX:
                        if Girl.taboo:
                            ch_l "Maybe take a step back, [Girl.player_petname]?"
                        else:
                            ch_l "Whoa, back it up."
                    elif Girl == JeanX:
                        if Girl.taboo:
                            ch_j "Not in public. . ."
                        else:
                            ch_j "Hey. . ."
                    elif Girl == StormX:
                        if Girl.taboo:
                            ch_s "Not while in public, [Girl.player_petname]?"
                        else:
                            ch_s "Could you not?"
                    elif Girl == JubesX:
                        if Girl.taboo:
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
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "inhibition", 2)
            "Ask for her_panties":


                call AskPanties (Girl)

            "Ask her to yoink some clothes" if Girl == KittyX:
                call Kitty_Yoink
            "Never mind [[exit]":

                $ Girl.had_chat[5] = 0
    return

label Compliment(Girl=0, line0=0, line1=0, line2=0, Options = [], CountList = [], line=0, D20=0):




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

    $ CountList = [0, 1, 2,3,4, 5, 6, 7,8, 9]
    $ renpy.random.shuffle(CountList)

    $ line0 = Options[CountList[0]]
    $ line1 = Options[CountList[1]]
    $ line2 = Options[CountList[2]]
    menu:
        "[line0]":
            $ line = CountList[0]
        "[line1]":
            $ line = CountList[1]
        "[line2]":
            $ line = CountList[2]
        "These are all awful, I can do better. . .":
            ch_p "Um. . ."
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "obedience", -1)
            call Compliment (Girl)
            return
        "Never mind":
            $ Girl.had_chat[5] = 0
            return

    $ D20 = renpy.random.randint(5, 20)
    if Girl == JubesX:
        $ D20 += 3


    if line == 0:

        if approval_check(Girl, 1000):
            $ D20 += 5

        call change_Girl_stat(Girl, "love", 3)
        if Girl == LauraX:
            call change_Girl_stat(Girl, "love", 3)
            if D20 >= 10:
                $ Girl.change_face("smile")
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
                call change_Girl_stat(Girl, "lust", 2)
                ch_l "I know right? I think I nailed that one."
                ch_l "Those tin cans never stood a chance!"
            else:
                $ Girl.change_face("angry", 1, eyes = "side")
                call change_Girl_stat(Girl, "inhibition", 1)
                ch_l "Thanks. . ."
                ch_l "I don't know, I think I missed one of the Sentinels."
                ch_l "I have to be better than this."
                $ Girl.change_face("normal", 0)
        elif Girl == JeanX:
            call change_Girl_stat(Girl, "love", 3)
            call change_Girl_stat(Girl, "love", 2)
            $ D20 -= 5
            if D20 >= 10:
                $ Girl.change_face("smile")
                call change_Girl_stat(Girl, "obedience", 2)
                ch_j "Yeah, obviously."
            else:
                $ Girl.change_face("angry", 1, eyes = "side")
                call change_Girl_stat(Girl, "inhibition", 2)
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
                    call change_Girl_stat(Girl, "inhibition", 2)
                    ch_j "Yeah, I know, but you really sucked out there."
                    ch_j "It's almost like your power is useless against robots. . ."
                $ Girl.change_face("normal", 0)
        else:
            call change_Girl_stat(Girl, "obedience", 2)
            if D20 >= 15:
                $ Girl.change_face("smile")
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 1)
                if Girl == StormX:
                    ch_s "Yes, I do think that I did well at it."
                else:
                    Girl.voice "Yeah, I think I really nailed that one."
            elif D20 >= 10:
                $ Girl.change_face("bemused", 2)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                Girl.voice "I think there's room for improvement though."
            else:
                $ Girl.change_face("bemused", 1, eyes = "side")
                call change_Girl_stat(Girl, "love", 1)
                Girl.voice "I appreciate the support, but we both know I could have done better."
                $ Girl.change_face("smile")

    elif line == 1:

        if not approval_check(Girl, 700):
            $ D20 -= 5

        if D20 >= 10:
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "obedience", 1)
            if Girl == KittyX:
                $ Girl.change_face("smile")
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "inhibition", 1)
                ch_k "Thanks, [KittyX.player_petname]!"
                ch_k "The numbers really spoke to me."
            elif Girl == EmmaX or Girl == StormX:
                $ Girl.change_face("bemused")
                call change_Girl_stat(Girl, "love", 2)
                Girl.voice "I'm glad you were paying attention, [Girl.player_petname]."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 2)
                ch_j "Thanks, it wasn't hard."
            else:
                $ Girl.change_face("confused")
                Girl.voice "Thanks?"
        else:
            $ Girl.change_face("bemused")
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "inhibition", 50, 1)
            if Girl == KittyX:
                ch_k "Yeah, I definitely gave it my all there."
                $ D20 += 5
            elif Girl == EmmaX:
                ch_e "I'm surprised you were paying attention."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 2)
                ch_j "Thanks, it wasn't hard."
                call change_Girl_stat(Girl, "love", -1)
                call change_Girl_stat(Girl, "obedience", 2)
                $ Girl.change_face("confused", 1)
                ch_j "Wait . ."
            elif Girl == StormX:
                ch_s "So you -were- awake. I owe Emma a drink."
            else:
                Girl.voice "Yeah, it was ok. Got a little dull though."

    elif line == 2:

        if not approval_check(Girl, 900):
            $ D20 -= 10
        if Girl in (RogueX, KittyX, JeanX, JubesX):
            $ D20 += 5

        call change_Girl_stat(Girl, "inhibition", 2)
        if Girl == LauraX:
            $ Girl.change_face("confused", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 2)
            ch_l ". . ."
            ch_l "Ok?"
        elif D20 >= 10:
            $ Girl.change_face("bemused", 2)
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "love", 2)
            if Girl == RogueX:
                ch_r "Well aren't you full'a sugar."
            elif Girl == KittyX:
                ch_k "Aw, that's sweet of you to say."
            elif Girl == EmmaX:
                ch_e "I do make an effort. . ."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
                ch_j "Congratulations, you have eyes."
            elif Girl == StormX:
                ch_s "I do strive for \"extra.\""
            elif Girl == JubesX:
                ch_v "Aw, thanks!"
            $ Girl.change_face("bemused", 1)
        else:
            $ Girl.change_face("bemused", 1)
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "obedience", 2)
            if Girl == RogueX:
                ch_r "Well aren't you full'a crap. . ."
            elif Girl == KittyX:
                ch_k "Um, ok. . ."
            elif Girl == EmmaX:
                ch_e "So -just- today? . ."
            elif Girl == JeanX:
                $ Girl.change_face("confused", 1)
                call change_Girl_stat(Girl, "inhibition", 2)
                ch_j "Extra? So you don't think I'm -always- this beautiful?"
            elif Girl == StormX:
                ch_s "I don't think that my appearance should be your concern."
            elif Girl == JubesX:
                ch_v "Well, don't stare so much."

    elif line == 3:

        if not approval_check(Girl, 900):
            $ D20 -= 10
        if Girl in (KittyX, EmmaX, JeanX, JubesX):
            $ D20 += 5

        if Girl == LauraX:
            $ Girl.change_face("confused", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "inhibition", 1)
            ch_l "Um. . . hi?"
        elif D20 >= 10:
            $ Girl.change_face("smile", 2)
            call change_Girl_stat(Girl, "love", 2)
            if D20 >= 15:
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 1)
            if Girl == RogueX:
                ch_r "\"Hey there\" yourself."
            elif Girl == KittyX:
                ch_k "Oh, hehe, that's sweet of you. . ."
            elif Girl == EmmaX:
                ch_e "Yes. . . hello to you as well."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "obedience", 3)
                ch_j "Oh, hey."
            elif Girl == StormX:
                ch_s "And a \"hello gorgeous\" to you as well."
            elif Girl == JubesX:
                ch_v "That's sweet. . ."
            $ Girl.change_face("smile", 1)
        else:
            $ Girl.change_face("bemused", 1)
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 1)
            if Girl == RogueX:
                ch_r "\"Gorgeous\" yourself."
            elif Girl == KittyX:
                ch_k "Riight. . ."
            elif Girl == EmmaX:
                ch_e "Children these days. . ."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 1)
                ch_j "Whatever."
            elif Girl == StormX:
                ch_s "Oh, hello."
            elif Girl == JubesX:
                ch_v "Hey."

    elif line == 4:

        if approval_check(Girl, 900, "L") and Girl != EmmaX:
            pass
        elif not approval_check(Girl, 1000):
            $ D20 -= 10
        if Girl in (RogueX, KittyX):
            $ D20 += 10

        if Girl == LauraX:
            $ Girl.change_face("confused")
            ch_l "What?"
        elif D20 >= 10:
            $ Girl.change_face("bemused", 2)
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 1)
            if Girl == RogueX:
                ch_r "What a charmer."
            elif Girl == KittyX:
                $ Girl.change_face("bemused", 2, mouth = "smile")
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "lust", 2)
                ch_k "Heh. . . you don't say. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("bemused", 1)
                ch_e "A valiant effort. . ."
            elif Girl == JeanX:
                ch_j "Well. . . ok."
            elif Girl == StormX:
                ch_s "I am used to that."
            elif Girl == JubesX:
                ch_v "I have that effect on people."
            $ Girl.change_face("bemused", 1)
        else:
            $ Girl.change_face("angry", 1, eyes = "stunned")
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 1)
            if Girl == RogueX:
                ch_r "Maybe stay lost."
            elif Girl == KittyX:
                ch_k "Uh-huh. . ."
            elif Girl == EmmaX:
                ch_e "Perhaps you're laying it on a bit thick there. . ."
            elif Girl == JeanX:
                $ Girl.change_face("bemused", 1, eyes = "stunned")
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "inhibition", 1)
                ch_j "Don't be so basic."
            elif Girl == StormX:
                $ Girl.eyes = "white"
                ch_s "Better?"
            elif Girl == JubesX:
                ch_v "Sorry, I have that effect on people sometimes. . ."
            $ Girl.change_face("normal")

    elif line == 5:

        if not approval_check(Girl, 600):
            $ D20 -= 12
        elif not approval_check(Girl, 1200):
            $ D20 -= 8

        if Girl in (LauraX, StormX):
            $ D20 += 8

        if Girl == LauraX:
            $ Girl.change_face("bemused")
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "inhibition", 2)
            ch_l "Thanks? I've been trying something new."
        elif D20 >= 10:
            $ Girl.change_face("bemused", 1)
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 2)
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
            $ Girl.change_face("angry", 2)
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 1)
            if Girl == RogueX:
                ch_r "Maybe don't concern yourself with my \"tone.\""
            elif Girl == KittyX:
                ch_k "Are you being sarcastic?"
            elif Girl == EmmaX:
                ch_e "I don't think we should be discussing my body."
            elif Girl == JeanX:
                ch_j "You obviously meant that I -always- look toned."
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 2)
                $ Girl.change_face("bemused", 1)
                ch_j "But at least you're paying attention."
            elif Girl == StormX:
                ch_s "You pay too close attention to my body."
            elif Girl == JubesX:
                ch_v "Ok, weirdo. . ."

            if Girl.blushing == "_blush2":
                $ Girl.blushing = "_blush1"
            else:
                $ Girl.blushing = ""

            $ Girl.mouth = "normal"

    elif line == 6:

        if approval_check(Girl, 700, "I"):
            pass
        elif not approval_check(Girl, 900):
            $ D20 -= 15
        elif not approval_check(Girl, 1400):
            $ D20 -= 10

        if Girl in (KittyX, EmmaX):
            $ D20 += 5
        else:
            if D20 >= 10:
                $ Girl.change_face("bemused", 2)
            else:
                $ Girl.change_face("angry", 2)
        if D20 >= 10:
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 4)
            call change_Girl_stat(Girl, "inhibition", 3)
            call change_Girl_stat(Girl, "inhibition", 1)
            call change_Girl_stat(Girl, "lust", 3)
            if Girl == KittyX:
                $ Girl.change_face("bemused", 2, mouth = "smile")
                ch_k "Really? Thanks, I appreciate that. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("bemused", 1, mouth = "smile")
                ch_e "Marvelous, aren't they?"
            elif Girl == JeanX:
                $ Girl.change_face("bemused", 1, eyes = "down")
                ch_j ". . ."
                $ Girl.eyes = "squint"
                ch_j "Yeah. . . how observant."
            elif Girl == StormX:
                ch_s ". . . yes, I suppose so. . ."
        else:
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 3)
            if Girl == KittyX:
                if D20 <= 5:
                    $ Girl.change_face("angry", 2)
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "love", -1)
                    ch_k "Asshole!"
                else:
                    $ Girl.change_face("sadside", 2, mouth = "smile")
                    ch_k "I get where you're going with that, but. . ."
                $ Girl.change_face(5, 1)
            elif Girl == EmmaX:
                $ Girl.change_face("bemused", 1)
                ch_e "Perhaps keep your eyes up here?"
                if D20 >= 5:
                    $ Girl.change_face("angry", 1)
                    ch_e ". . ."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "love", 2)
                    call change_Girl_stat(Girl, "lust", 5)
                    ch_e "Higher!"
            elif Girl == JeanX:
                $ Girl.change_face("bemused", 1, eyes = "down")
                call change_Girl_stat(Girl, "love", 2)
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
            $ Girl.change_face("bemused", 1)

    elif line == 7:

        if approval_check(Girl, 700, "I"):
            pass
        elif not approval_check(Girl, 900):
            $ D20 -= 15
        elif not approval_check(Girl, 1300):
            $ D20 -= 10

        if Girl in (RogueX, EmmaX, StormX):
            $ D20 += 5

        if D20 >= 10:
            $ Girl.change_face("bemused", 2)
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "inhibition", 1)
            call change_Girl_stat(Girl, "lust", 2)
            if Girl == RogueX:
                ch_r "I don't know, my jeans have been getting a bit tight. . ."
            elif Girl == KittyX:
                ch_k "I guess so? I mean. . ."
            elif Girl == EmmaX:
                ch_e "My, you do have good taste. . ."
                $ Girl.change_face("confused", 1)
                ch_e "If perhaps poor manners. . ."
            elif Girl == LauraX:
                $ Girl.change_face("smile", 1)
                ch_l "Good to know."
            elif Girl == JeanX:
                ch_j "Want me to shake it a little?"
            elif Girl == StormX:
                ch_s "You think so? How amusing."
            elif Girl == JubesX:
                ch_v "Really?"
            $ Girl.change_face("bemused", 1)
        else:
            $ Girl.change_face("angry", 1)
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "love", -2)
            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "inhibition", 2)
            if Girl == EmmaX:
                ch_e "You shouldn't comment on a lady's figure."
            elif Girl == LauraX:
                $ Girl.change_face("confused", 1)
                ch_l "Right. . ."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 3)
                ch_j "Obviously."
            elif Girl == StormX:
                ch_s "[Girl.player_petname], please be serious."
            else:
                Girl.voice "Rude."
            $ Girl.change_face("normal", 1)

        if Girl == JubesX and Girl.Clothes["jacket"]:
            ch_v "How could you tell?"

    elif line == 8:

        if approval_check(Girl, 800, "L"):
            pass
        elif not approval_check(Girl, 1300):
            $ D20 -= 10
        if Girl in (EmmaX, LauraX, StormX):
            $ D20 += 15

        if D20 >= 10:
            $ Girl.change_face("bemused", 1, mouth = "smile")
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 3)
            call change_Girl_stat(Girl, "lust", 2)
            if Girl == RogueX:
                ch_r "Oh? Thank you, I guess?"
            elif Girl == KittyX:
                ch_k "Huh? . . I don't know, my usual shampoo, I guess. . ."
            elif Girl == EmmaX:
                ch_e "Thank you, I picked it up last time I was in Grasse."
            elif Girl == LauraX:
                ch_l "Probably blood, mostly. Ninjas."
            elif Girl == JeanX:
                $ line = renpy.random.choice([RogueX.name, KittyX.name,EmmaX.name])
                ch_j "Oh, just something I found in [line]'s room."
                $ line = 8
            elif Girl == StormX:
                ch_s "Ah, a heart-shaped flower I discovered in my travels. . ."
            elif Girl == JubesX:
                ch_v "Oh, it's probably sun tan lotion. . ."
        else:
            $ Girl.change_face("angry", 2, mouth = "smile")
            call change_Girl_stat(Girl, "love", -1)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 1)
            if Girl == RogueX:
                ch_r "Probably best not to talk about a woman's scent."
            elif Girl == KittyX:
                ch_k "Gross. . ."
            elif Girl == EmmaX:
                ch_e "You might want to back up a bit. . ."
            elif Girl == LauraX:
                $ Girl.change_face("confused", 1)
                call change_Girl_stat(Girl, "lust", 2)
                ch_l "I don't know, I'm kinda sweaty, I guess. . ."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 2)
                $ Girl.change_face("bemused", 1)
                ch_j "I don't know, something I found around. . ."
            elif Girl == StormX:
                ch_s ". . . you may be standing too close. . ."
            elif Girl == JubesX:
                ch_v "It's probably \"back the hell off.\""
            $ Girl.change_face("bemused", 1)

    elif line == 9:

        if approval_check(Girl, 900, "L"):
            pass
        elif not approval_check(Girl, 1100):
            $ D20 -= 10
        if Girl in (RogueX, LauraX, JeanX):
            $ D20 += 5

        if D20 >= 10:
            $ Girl.change_face("sly", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 3)
            call change_Girl_stat(Girl, "lust", 5)
            call change_Girl_stat(Girl, "lust", 5)
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
            call change_Girl_stat(Girl, "love", -2)
            call change_Girl_stat(Girl, "obedience", 1)
            call change_Girl_stat(Girl, "inhibition", 1)
            if Girl == EmmaX:
                $ Girl.change_face("angry", 1, mouth = "smirk")
                ch_e "That's not really appropriate."
            elif Girl == JeanX:
                $ Girl.change_face("sly", 1)
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "obedience", 1)
                ch_j "Control yourself. . ."
            else:
                $ Girl.change_face("bemused", 1)
                Girl.voice "Ok. . ."


    if D20 < 10:
        menu:
            "Sorry":
                if Girl not in (LauraX,JeanX):
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", -2)
                    call change_Girl_stat(Girl, "obedience", -1)
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
                    $ Girl.change_face("angry", eyes = "side")
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", -1)
                    ch_j ". . ."
                    if D20 < 7:
                        $ Girl.change_face("bemused")
                        call change_Girl_stat(Girl, "love", 1)
                        call change_Girl_stat(Girl, "obedience", 1)
                        ch_j "Ok, I can accept that."
                    if D20 < 5:
                        call change_Girl_stat(Girl, "love", 1)
                        call change_Girl_stat(Girl, "obedience", 2)
                        ch_j "Just don't let it happen again."
                elif Girl == StormX:
                    ch_s "Don't be sorry, be better."
                elif Girl == JubesX:
                    call change_Girl_stat(Girl, "love", 1)
                    ch_v "Yeah, ok. . ."
                $ Girl.change_face("normal")
            ". . .":
                pass
    elif Player.location == "date":

        if "compliment" not in Girl.recent_history:
            $ Girl.add_word(1, "compliment", 0, 0, 0)
            call Date_Bonus (Girl, 5)
    return

label Love_You(Girl=0):



    ch_p "[Girl.name], I love you."
    if Player.location == "bg_halloween":
        Girl.voice ". . . we should talk after the party. . ."
        return

    if "lover" not in Girl.player_petnames:

        if "love" in Girl.history:

            if approval_check(Girl, 800, "L"):

                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 1)
                call change_Girl_stat(Girl, "lust", 5)
                $ Girl.change_face("bemused", 2, brows = "confused")

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

            elif approval_check(Girl, 600, "L"):

                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "inhibition", 1)
                $ Girl.change_face("bemused", 2)

                if Girl == RogueX:
                    ch_r "I don't know, love? . ."
                elif Girl == KittyX:
                    ch_k "I don't know if I think of you like that . ."
                elif Girl == EmmaX:
                    ch_e "This is incredibly inappropriate. . ."
                elif Girl == LauraX:
                    ch_l "I don't. . ."
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "love", 1)
                    ch_j "Right, but. . ."
                elif Girl == StormX:
                    ch_s "So you say, but. . ."
                elif Girl == JubesX:
                    ch_v "You're moving fast. . ."
            else:

                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "inhibition", 2)
                $ Girl.change_face("angry", 1)

                if Girl == RogueX:
                    ch_r "Bull."
                elif Girl == KittyX:
                    ch_k "Stop trolling me!"
                elif Girl == EmmaX:
                    ch_e "Oh forget this nonsense already. . ."
                elif Girl == LauraX:
                    ch_l "Fuck off with this. . ."
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "love", 2)
                    ch_j "Oh, keep it in your pants. . ."
                elif Girl == StormX:
                    ch_s "Oh, you child. . ."
                elif Girl == JubesX:
                    ch_v "Geeze, relax. . ."


        $ Girl.add_word(1, "love", "love", 0, "love")

        if Girl == RogueX:
            if not RogueX.event_happened[6]:

                $ line = "never"
            elif RogueX.event_happened[6] >= 20:

                ch_r "You're just giving me whiplash here, [RogueX.player_petname]."

        elif Girl == KittyX:
            if not KittyX.event_happened[6]:
                $ line = "never"
            elif KittyX.event_happened[6] >= 20:
                call Kitty_Love_Redux
        elif Girl == EmmaX:
            if not EmmaX.event_happened[6]:

                $ line = "never"
            elif EmmaX.event_happened[6] >= 20:
                call Emma_Love_Redux
        elif Girl == LauraX:
            if not LauraX.event_happened[6]:
                $ line = "never"
            elif LauraX.event_happened[6] >= 20:
                call Laura_Love_Redux
        elif Girl == JeanX:
            if not JeanX.event_happened[6]:
                $ line = "never"
            elif JeanX.event_happened[6] >= 20:
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "love", 40)
                ch_j "Nice to hear you admit it."
        elif Girl == StormX:
            if not StormX.event_happened[6]:

                $ line = "never"
            elif StormX.event_happened[6] >= 20:
                call Storm_Love_Redux
        elif Girl == JubesX:
            if not JubesX.event_happened[6]:

                $ line = "never"
            elif JubesX.event_happened[6] >= 20:
                call Jubes_Love_Redux

        if line == "never":

            if approval_check(Girl, 800, "L"):
                call change_Girl_stat(Girl, "love", 10)
                call change_Girl_stat(Girl, "lust", 5)
                $ Girl.change_face("smile", 2, eyes = "surprised")
            elif approval_check(Girl, 600, "L"):
                call change_Girl_stat(Girl, "love", 5)
                $ Girl.change_face("confused", 2, eyes = "surprised")
            else:
                $ Girl.change_face("angry", 1, brows = "confused")
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 5)
            call change_Girl_stat(Girl, "obedience", 5)
            call change_Girl_stat(Girl, "inhibition", 5)
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
            call remove_Girl(Girl)
            jump reset_location
        return


    if "love" in Girl.daily_history:

        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "inhibition", 1)
        call change_Girl_stat(Girl, "lust", 5)
        $ Girl.change_face("smile", 1)
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
            call change_Girl_stat(Girl, "love", -2)
            call change_Girl_stat(Girl, "obedience", -2)
            ch_j "You're getting a little repetitive. . ."
        elif Girl == StormX:
            ch_s "This isn't the first time today. . ."
            ch_s "Perhaps it should not be the last. . ."
        elif Girl == JubesX:
            ch_v "Seriously, give me time to think. . ."

    elif approval_check(Girl, 800, "L"):

        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)
        call change_Girl_stat(Girl, "lust", 5)
        $ Girl.change_face("smile", 1)
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
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", 1)
            ch_j "I love you too, ok?"
        elif Girl == StormX:
            ch_s "And I love you as well. . ."
        elif Girl == JubesX:
            ch_v "Aw, love you right back!"
    else:

        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "obedience", 3)
        $ Girl.change_face("sadside", 1)
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

    $ Girl.add_word(1, "love", "love", 0, "love")
    return

label TouchCheek(Girl=0):
    if Girl not in all_Girls:
        return
    $ shift_focus (Girl)
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
        call change_Girl_stat(Girl, "love", -2)
        return
    else:
        "You reach out and brush [Girl.name]'s face with your hand, a shiver runs through her."
    call change_Girl_stat(Girl, "obedience", 1)

    if Girl == RogueX or "addictive" in Player.traits:
        $ Girl.addiction -= 2
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0
        $ Girl.addiction_rate = 3 if Girl.addiction_rate < 3 else Girl.addiction_rate
        call change_Girl_stat(Girl, "lust", 5)
    else:
        $ Girl.addiction -= 2
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0
        call change_Girl_stat(Girl, "lust", 5)

    if approval_check(Girl, 1000):
        $ Girl.change_face("sexy", 1)
        if Girl == RogueX:
            ch_r "A promise of things to come, [Girl.player_petname]?"
        elif Girl == EmmaX:
            ch_e "That's sweet, what was it for, [Girl.player_petname]?"
        elif Girl == JeanX:
            ch_j "Oh, um. . . hey."
        else:
            Girl.voice "Hmmm, what were you thinking, [Girl.player_petname]?"
        call change_Girl_stat(Girl, "love", 1)
    elif approval_check(Girl, 800, Alt = [[RogueX], 500]) or approval_check(Girl, 700, "L"):
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
        call change_Girl_stat(Girl, "love", -2)
        $ Girl.daily_history.append("no_cheek")
    elif approval_check(Girl, 250):
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
        call change_Girl_stat(Girl, "love", -3)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)

    if "no_cheek" in Girl.daily_history:
        menu:
            "Sorry, sorry, won't happen again.":
                if approval_check(Girl, 300):
                    $ Girl.change_face("sexy", 1)
                    if Girl == RogueX:
                        ch_r "Well, ok, just cut it out though."
                    elif Girl == EmmaX:
                        ch_e "See that it doesn't."
                    elif Girl == StormX:
                        ch_s "So long as you understand. . ."
                    else:
                        Girl.voice "Ok. . ."
                    call change_Girl_stat(Girl, "love", 2)
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
                    call change_Girl_stat(Girl, "obedience", 1)
            "You know you wanted it.":


                if approval_check(Girl, 400, "OI", Alt = [[RogueX],300]) or approval_check(Girl, 800, Alt = [[RogueX,LauraX], 1500]):
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
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    $ Girl.blushing = "_blush1"
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
    else:

        menu:
            "Sorry, you looked so cute there.":
                if approval_check(Girl, 850, "LI"):
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
                    call change_Girl_stat(Girl, "love", 2)
                elif approval_check(Girl, 500, "LI"):
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
                    call change_Girl_stat(Girl, "love", 2)
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
                    call change_Girl_stat(Girl, "obedience", 1)
            "You had a fly on you.":


                if approval_check(Girl, 850, "LI"):
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
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "inhibition", 1)
                elif approval_check(Girl, 600):
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
                    call change_Girl_stat(Girl, "obedience", 2)
            "Are you sure you didn't enjoy that?":


                if approval_check(Girl, 650, "LI") or approval_check(Girl, 1000):
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
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 1)
                elif approval_check(Girl, 500, "OI"):
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
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)


    $ Girl.recent_history.append("cheek")
    $ Girl.daily_history.append("cheek")
    return

label Hold_Hands(Girl=0, Gloves=0):

    if Girl.Clothes["gloves"] == "gloves":
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
                $ Girl.take_off("gloves")
    "You reach down and grab [Girl.name]'s hand in yours."
    if approval_check(Girl, 800, "L"):
        $ Girl.change_face("smile", 1, eyes = "closed")
        "She squeezes your hand back and leans her shoulder against yours."
        $ Count = 10
    elif approval_check(Girl, 1200):
        $ Girl.change_face("bemused", 1, brows = "confused")
        "She gives your hand a light squeeze in return."
        $ Count = 4
    elif approval_check(Girl, 800):
        $ Girl.change_face("bemused", 2, brows = "confused")
        "She stiffens a bit, but leaves her hand in yours."
        $ Girl.change_face("bemused", 1, eyes = "down")
        $ Count = 2
    else:

        $ Girl.change_face("angry", 1)
        call change_Girl_stat(Girl, "love", -1)
        call change_Girl_stat(Girl, "love", -1)
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)
        if not Girl.Clothes["gloves"] and Girl.resistance:
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "lust", 5)
            $ Girl.addiction -= 2
            $ Girl.addiction_rate += 1 if RogueX.addiction_rate < 5 else 0
        if Gloves == "gloves":
            $ Girl.Clothes["gloves"] = "gloves"
            "She slaps your hand away, putting her gloves back on."
        else:
            "She slaps your hand away."
        Girl.voice "Don't get too familiar."
        return

    if Girl.Clothes["gloves"] != "gloves":
        $ Girl.addiction_rate += 1 if Girl.addiction_rate < 5 else 0

    while Count:
        $ round -= 5
        if approval_check(Girl, 800, "L"):
            if Count >= 8:
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "lust", 2)
        elif approval_check(Girl, 1200):
            if Count >= 3:
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "lust", 1)
        elif approval_check(Girl, 800):
            call change_Girl_stat(Girl, "love", 2)
            call change_Girl_stat(Girl, "obedience", 2)
        if Girl.Clothes["gloves"] != "gloves" and Girl.addiction_rate >= 3 and Girl.addiction >= 5:
            call change_Girl_stat(Girl, "lust", 3)
            $ Girl.addiction -= 2
            $ Count += 1 if Count <= 1 else 0
            if Girl.lust >= 30:
                $ Girl.change_face("sly", 2)

        menu:
            "Keep holding hands.":
                pass
            "Stop holding hands.":
                $ Count = 0
                $ Girl.change_face("bemused", 1)
                return
        $ Count -= 1
        $ Count = 0 if round <= 10 else Count



    $ Girl.add_word(1, "holdhands", "holdhands")

    if not approval_check(Girl, 800, "L") and not approval_check(Girl, 1200):

        $ Girl.change_face("sadside", 1, brows = "confused")
        call change_Girl_stat(Girl, "love", -2)
        call change_Girl_stat(Girl, "obedience", -2)
        call change_Girl_stat(Girl, "inhibition", 3)
        call change_Girl_stat(Girl, "lust", -5)
    else:
        $ Girl.change_face("smile", 1)
    if Gloves == "gloves":
        $ Girl.Clothes["gloves"] = "gloves"
    $ Gloves = 0
    Girl.voice "Ok, that's enough of that. . ."
    return

label Girl_Headpat(Girl=0):
    $ Girl = check_girl(Girl)
    $ shift_focus (Girl)
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
        call change_Girl_stat(Girl, "love", -2)
        return
    else:
        "You reach out and pat [Girl.name] on the head."
    call change_Girl_stat(Girl, "obedience", 2)

    if approval_check(Girl, 1200, Alt = [[LauraX], 1000]):
        $ Girl.change_face("sexy", 1)
        if Girl == EmmaX:
            ch_e "Hmmmm?"
        else:
            Girl.voice "Mmmmm. . ."
        call change_Girl_stat(Girl, "love", 1)
    elif approval_check(Girl, 800, Alt = [[EmmaX], 1200]) or approval_check(Girl, 750, "L", Alt = [[LauraX], 600]):
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
        call change_Girl_stat(Girl, "love", -2)
        $ Girl.daily_history.append("no_headpat")
    elif approval_check(Girl, 400, Alt = [[EmmaX], 600]):
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
        call change_Girl_stat(Girl, "love", -3)
        call change_Girl_stat(Girl, "obedience", 1)
        call change_Girl_stat(Girl, "inhibition", 1)

    if "no_headpat" in Girl.daily_history:
        menu:
            "Sorry, sorry, won't happen again.":
                if approval_check(Girl, 300):
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
                    call change_Girl_stat(Girl, "love", 2)
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
                    call change_Girl_stat(Girl, "obedience", 1)
            "You know you wanted it.":

                if approval_check(Girl, 400, "OI", Alt = [[EmmaX], 600]) or approval_check(Girl, 800, Alt = [[EmmaX], 900]):
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
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    $ Girl.blushing = "_blush1"
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
    else:


        menu:
            "Sorry, you looked so cute there.":
                if approval_check(Girl, 850, "LI", Alt = [[EmmaX], 1050]):
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
                    call change_Girl_stat(Girl, "love", 2)
                elif approval_check(Girl, 500, "LI", Alt = [[EmmaX], 700]):
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
                    call change_Girl_stat(Girl, "love", 2)
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
                    call change_Girl_stat(Girl, "obedience", 1)
                    $ Count = 1
            "You had a loose hair going on.":

                if approval_check(Girl, 700, "LI", Alt = [[EmmaX,JeanX],850]):
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
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "inhibition", 1)
                elif approval_check(Girl, 700):
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
                    call change_Girl_stat(Girl, "obedience", 2)
                    $ Count = 1
            "Are you sure you didn't enjoy that?":

                if approval_check(Girl, 850, Alt = [[EmmaX,JeanX], 1000]):
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
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    $ Count = 4
                elif approval_check(Girl, 500, "OI"):
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
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    call change_Girl_stat(Girl, "love", -3)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    $ Count = 1
        while Count > 0 and round >= 10:
            $ Count -= 1 if Count != 4 else 0
            $ round -= 1
            menu:
                "Continue?"
                "Yes":
                    "You continue to hold your hand on top of [Girl.name]'s head, rubbing it softly."
                    if Count <= 0:

                        if approval_check(Girl, 800):
                            $ Girl.change_face("bemused", 2)
                            call change_Girl_stat(Girl, "love", 2)
                            call change_Girl_stat(Girl, "inhibition", 2)
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
                            call change_Girl_stat(Girl, "love", -5)
                            call change_Girl_stat(Girl, "inhibition", 3)
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

                        if approval_check(Girl, 800, Alt = [[EmmaX], 900]):
                            $ Girl.change_face("bemused", 1)
                            call change_Girl_stat(Girl, "love", 1)
                            call change_Girl_stat(Girl, "obedience", 2)
                            call change_Girl_stat(Girl, "inhibition", 2)
                            if Girl == RogueX:
                                ch_r "Um, you might wanna. . ."
                            elif Girl == KittyX:
                                ch_k "We should probably do something else. . ."
                            elif Girl == EmmaX:
                                if taboo > 20:

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
                            call change_Girl_stat(Girl, "love", -2)
                            call change_Girl_stat(Girl, "obedience", 2)
                            call change_Girl_stat(Girl, "obedience", 2)
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

                        if approval_check(Girl, 800, Alt = [[EmmaX], 900]):
                            $ Girl.change_face("bemused", 2, eyes = "closed")
                            if Count > 5:
                                call change_Girl_stat(Girl, "love", 1)
                                call change_Girl_stat(Girl, "love", 1)
                                call change_Girl_stat(Girl, "obedience", 1)
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
                            call change_Girl_stat(Girl, "love", -1)
                            call change_Girl_stat(Girl, "obedience", 2)
                            call change_Girl_stat(Girl, "obedience", 2)
                            call change_Girl_stat(Girl, "inhibition", 2)
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
    $ line = 0
    if not Girl.Clothes["underwear"] or Girl.Clothes["underwear"] == "shorts":
        if approval_check(Girl, 900):
            $ Girl.change_face("sexy", 1)
            call change_Girl_stat(Girl, "lust", 5)
            call change_Girl_stat(Girl, "lust", 5)
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 5)
            call change_Girl_stat(Girl, "inhibition", 10)
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
        elif Girl.Clothes["top"] == "towel" or not Girl.Clothes["bottom"]:
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
            $ Girl.change_face("bemused", 2, eyes = "side")
            call change_Girl_stat(Girl, "lust", 5)
            call change_Girl_stat(Girl, "lust", 5)
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 5)
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

        if Girl.seen_pussy and approval_check(Girl, 500):

            $ approval_bonus += 15
        elif Girl.seen_underwear and approval_check(Girl, 500):

            $ approval_bonus += 5
        if "exhibitionist" in Girl.traits:
            $ approval_bonus += (Girl.taboo*5)
        if Girl in Player.Harem or ("sex friend" in Girl.player_petnames and not taboo):
            $ approval_bonus += 10
        if "no_bottomless" in Girl.recent_history:
            $ approval_bonus -= 20

        $ line = 0
        if Girl.wearing_pants or Girl.Clothes["hose"] == "tights":

            if approval_check(Girl, 1000, "OI", taboo_modifier = 5) or "exhibitionist" in Girl.traits:
                $ line = "here"
            elif approval_check(Girl, 900, taboo_modifier = 5):
                $ line = "change"
        elif Girl.wearing_skirt:

            if approval_check(Girl, 600, "OI", taboo_modifier = 5) or "exhibitionist" in Girl.traits:
                $ line = "here"
            elif approval_check(Girl, 1100, taboo_modifier = 5):
                $ line = "change"
        else:
            if approval_check(Girl, 1200, taboo_modifier = 5) or "exhibitionist" in Girl.traits:
                $ line = "here"

        if Girl == StormX and line == "change":

            if not taboo or StormX in Rules:
                $ line = "here"

        if Girl == KittyX and line:

            call change_Girl_stat(Girl, "lust", 2)
            call change_Girl_stat(Girl, "obedience", 4)
            call change_Girl_stat(Girl, "inhibition", 4)
            call Remove_Panties (Girl)
            if Girl.wearing_pants or Girl.Clothes["hose"] == "tights":
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "inhibition", 5)
            elif Girl.wearing_skirt:
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "obedience", 4)
                call change_Girl_stat(Girl, "inhibition", 4)
            else:
                call change_Girl_stat(Girl, "lust", 7)
                call change_Girl_stat(Girl, "obedience", 6)
                call change_Girl_stat(Girl, "inhibition", 8)
            $ approval_bonus = Store
            $ line = 0
            return

        if line == "here":

            $ Girl.change_face("sly")
            if Girl.wearing_skirt:

                call change_Girl_stat(Girl, "obedience", 4)
                call change_Girl_stat(Girl, "inhibition", 4)
            else:
                call change_Girl_stat(Girl, "obedience", 6)
                call change_Girl_stat(Girl, "inhibition", 6)

            call change_Girl_stat(Girl, "lust", 5)
            call Remove_Panties (Girl)

            if Girl.taboo:
                call change_Girl_stat(Girl, "lust", 5)
                if "exhibitionist" in Girl.traits:
                    call change_Girl_stat(Girl, "lust", 5)
                    call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "obedience", 10)
                call change_Girl_stat(Girl, "inhibition", 10)

        elif line:

            if not taboo and Girl != StormX:

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
                        call change_Girl_stat(Girl, "love", 5)
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
                        call change_Girl_stat(Girl, "lust", 2)
                        call change_Girl_stat(Girl, "obedience", 4)
                        call change_Girl_stat(Girl, "inhibition", 4)
                        show black_screen onlayer black
                        "You exit the room for a minute"
                        hide black_screen onlayer black
                        $ Girl.daily_history.append("commando")
                        $ Girl.change_Outfit()
                        call outfitShame (Girl, 20)
                        "When you return, she quietly hands you her balled up panties."
                        $ line = 0
                    "And miss the show?":

                        if approval_check(Girl, 1000, "LI"):
                            call change_Girl_stat(Girl, "lust", 5)
                            call change_Girl_stat(Girl, "obedience", 5)
                            call change_Girl_stat(Girl, "inhibition", 5)
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
                            call change_Girl_stat(Girl, "love", -5)
                            call change_Girl_stat(Girl, "obedience", -3)
                            call change_Girl_stat(Girl, "inhibition", 5)
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
                            $ line = 0
                    "Nope, I'm staying.":

                        if approval_check(Girl, 600, "OI"):
                            $ Girl.change_face("perplexed", 1)
                            call change_Girl_stat(Girl, "lust", 5)
                            call change_Girl_stat(Girl, "obedience", 10)
                            call change_Girl_stat(Girl, "inhibition", 5)
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
                            call change_Girl_stat(Girl, "love", -10)
                            call change_Girl_stat(Girl, "obedience", -5)
                            call change_Girl_stat(Girl, "inhibition", 5)
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
                            $ line = 0
                if line:

                    $ Girl.change_face("sly", 1)
                    if Girl.wearing_pants or Girl.Clothes["hose"] == "tights":
                        call change_Girl_stat(Girl, "lust", 5)
                        call change_Girl_stat(Girl, "obedience", 5)
                        call change_Girl_stat(Girl, "inhibition", 5)
                    elif Girl.wearing_skirt:
                        call change_Girl_stat(Girl, "lust", 5)
                        call change_Girl_stat(Girl, "obedience", 4)
                        call change_Girl_stat(Girl, "inhibition", 4)
                    call Remove_Panties (Girl)
            else:


                $ Girl.change_face("sly", 1)
                call change_Girl_stat(Girl, "lust", 2)
                call change_Girl_stat(Girl, "obedience", 4)
                call change_Girl_stat(Girl, "inhibition", 4)
                $ Girl.location = "hold"
                call set_the_scene
                "[Girl.name] nods and leaves for a minute."
                $ Girl.daily_history.append("commando")
                $ Girl.change_Outfit()
                call outfitShame (Girl, 20)
                $ Girl.location = Player.location
                call set_the_scene
                "She returns and quietly hands you her balled up panties."
        else:

            $ Girl.change_face("angry", 2)
            if not approval_check(Girl, 500):
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "love", -10)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "inhibition", 3)
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
            elif not approval_check(Girl, 500, taboo_modifier = 5):
                call change_Girl_stat(Girl, "lust", 5)
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "inhibition", 5)
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
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "inhibition", 1)
                if Girl.taboo:
                    call change_Girl_stat(Girl, "inhibition", 2)
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
                    call change_Girl_stat(Girl, "obedience", -2)
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
            $ Girl.blushing = "_blush1"
    $ approval_bonus = Store
    $ line = 0
    return

label Remove_Panties(Girl=0, Type=0, Store=0, Store2=0):
    if Girl not in all_Girls:
        return
    if Girl == KittyX:
        $ Girl.take_off("underwear")
        $ Girl.change_face("bemused")
        if Girl.wearing_pants:
            "[Girl.name] looks around, reaches into her pocket, and tugs her panties out."
        elif Girl.wearing_skirt:
            "[Girl.name] looks around, reaches into her skirt, and pulls her panties out."
        elif Girl.Clothes["hose"] in ["tights", "pantyhose"]:
            "[Girl.name] looks around, reaches through her [Girl.Clothes[hose].name], and pulls her panties out."
        else:
            "[Girl.name] looks around and pulls her panties off."

        $ Girl.change_face("sexy")
        "She hands them to you with a smirk."

        if not Girl.Clothes["bottom"] :
            call expression Girl.tag + "_First_Bottomless"

        $ Girl.daily_history.append("commando")
        $ Girl.change_Outfit()
        call outfitShame (Girl, 20)
        return
    elif Girl == JeanX and Girl.wearing_skirt and not approval_check(Girl, 400, "L"):
        $ Girl.take_off("underwear")
        $ Girl.change_face("bemused", eyes = "psychic")
        "You notice some movement as her panties shoot down her legs and she quickly steps out of them."
        "They scoot along near the ground and then up to your hand."
        $ Girl.change_face("sexy")

        if not Girl.Clothes["bottom"] :
            call expression Girl.tag + "_First_Bottomless"

        $ Girl.daily_history.append("commando")
        $ Girl.change_Outfit()
        call outfitShame (Girl, 20)
        return

    $ Store = Girl.Clothes["bottom"]
    $ Store2 = Girl.Clothes["hose"]
    if Girl.wearing_skirt:
        $ Girl.dress_upskirt = True

        $ Type = 2

    if Girl.wearing_pants:
        $ Girl.Outfit.remove_Clothing(["pants", "skirt"])

        $ Type = 1
    elif Girl.wearing_skirt:
        $ Girl.upskirt = True

        $ Type = 2

    if Girl.Clothes["hose"] in ["tights", "pantyhose"]:
        $ Girl.take_off("hose")
        $ Type = 3 if Type == 2 else 4

    $ Girl.take_off("underwear")

    if Girl.taboo:
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

    $ Girl.Clothes["bottom"] = Store
    $ Girl.Clothes["hose"] = Store2
    if Girl.wearing_pants:
        "She hands you the panties and then pulls her pants back on."
    elif Girl.wearing_shorts:
        "She hands you the panties and then pulls her shorts back up."

        $ Girl.Clothes["pants"].state = False
    elif Girl.wearing_skirt and Girl.Clothes["hose"] in ["tights", "pantyhose"]:
        "She hands you the panties and then pulls her [Girl.Clothes[hose].name] back on and her skirt back down."

        $ Girl.upskirt = False
    elif Girl.wearing_skirt:
        "She hands you the panties and then pulls her skirt back down."

        $ Girl.upskirt = False
    elif Girl.Clothes["hose"] in ["tights", "pantyhose"]:
        "She hands you the panties and then pulls her [Girl.Clothes[hose].name] back on."
    else:
        "[Girl.name] hands them to you in a ball."

    call expression Girl.tag + "_First_Bottomless" pass (1)

    $ Girl.daily_history.append("commando")
    $ Girl.change_Outfit()
    call outfitShame (Girl, 20)
    return
