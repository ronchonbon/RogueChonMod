label meet_Storm_prelude:
    call set_the_scene(location = "bg_player", fade = True)

    "You hear a creaking noise from above you. You notice this happening more and more often lately."
    "Maybe next time you're in class, you can ask [EmmaX.name] about it."

    $ Player.add_word(1, 0, 0, 0, "noise")

    jump player_room

label meet_Storm_ask_Emma:
    $ EmmaX.teaching = False

    $ shift_focus(EmmaX)
    call set_the_scene(location = "bg_classroom", fade = True)

    "Before class, you approach [EmmaX.name]."
    ch_p "I've been hearing creaking noises above me, do you have any idea what that could be?"

    $ EmmaX.change_face("confused")

    ch_e "Oh. . ."

    $ EmmaX.change_face("sly")

    ch_e "That's just the resident ghost."

    menu:
        extend ""
        "Ghost?":
            pass
        "What?!":
            pass
        "Are you joking with me?":
            $ EmmaX.change_face("angry")

            ch_e "I don't joke."

            $ EmmaX.change_face("sly")

    ch_e "Yes, the ghost in the attic, [EmmaX.player_petname]."

    menu:
        extend ""
        "Is it dangerous?":
            pass
        "Oh, ok.":
            $ EmmaX.change_face("confused")

            ch_e "Ok?"

            $ EmmaX.change_face("angry", eyes = "side")

            ch_e ". . ."

            call change_Girl_stat(EmmaX, "love", -2)
            call change_Girl_stat(EmmaX, "obedience", 1)

            ch_e "I suppose I expected you would be a bit more concerned. . ."

    $ EmmaX.change_face("normal")

    ch_e "Well no, it probably isn't dangerous, but you might want to see for yourself. . ."

    menu:
        extend ""
        "Thanks for the heads up.":
            $ EmmaX.change_face("smile")
            call change_Girl_stat(EmmaX, "love", 3)
            call change_Girl_stat(EmmaX, "obedience", 1)

            ch_e "Glad to be of help."
        "Ok.":
            ch_e "Right. . ."

    ch_e "Ok, now sit down, the lesson is about to begin."

    $ EmmaX.teaching = True

    $ Player.add_word(1, 0, 0, 0, "attic")
    $ Player.history.remove("noise")

    call set_the_scene
    call take_class
    call tenth_round
    call set_Girls_locations
    call event_calls
    jump classroom

label meet_StormWater:
    call set_the_scene(location = "bg_player", fade = True)

    "As you enter your room, you notice that there is a puddle on the floor."
    "It appears to be dripping from a crack in the ceiling."
    "It seems like the ghost in the attic might be more trouble than [EmmaX.name] let on."

    menu:
        "Let's go bust some ghosts!":
            "Hell yeah."
        "Guh-guh-guh-ghosts?!":
            "Stop being a pussy."

    if len(Player.Party) > 1:
        Player.Party[1].voice "I think we'll sit this one out."

        call remove_Girl(Player.Party[1])

        Player.Party[0].voice "Have fun though."

        call remove_Girl(Player.Party[0])
    elif Player.Party:
        Player.Party[0].voice "I think I'll sit this one out."
        Player.Party[0].voice "Have fun though."

        call remove_Girl(Player.Party[0])

    "You head for the door marked \"Attic. . .\""

    $ Player.add_word(1, "water", 0, 0, 0)

    jump meet_Storm

label meet_Storm:
    if time_index > 2:
        if "noattic" in Player.daily_history:
            "No way, too spooky."
        else:
            "As you climb the stairs, a gust of chill wind rushes down them."
            "Oh, look at the time, maybe this is something that should wait for earlier in the day. . ."

        "You return to your room."

        $ Player.add_word(1, 0, "noattic", 0, 0)

        jump player_room

    call set_the_scene(location = "bg_storm", fade = True)

    $ Player.history.remove("attic")

    "You climb the stairs up to the attic. Once you reach the top, you hit a wave of humidity."
    "Greeting you at the top is what appears to be an indoor garden. Bright sunlight streams through the windows."

    $ StormX.location = "bg_storm"
    $ StormX.undress()
    $ StormX.change_face("normal", eyes = "side")

    call show_Girl(StormX, x_position = stage_center, color_transform = silhouette, transition = False)

    "Standing in the middle of the room appears to be a woman. . ."

    call get_color_transform
    $ color_transform = _return

    call show_Girl(StormX, color_transform = color_transform, transition = dissolve)
    $ shift_focus(StormX)

    "And she's naked."

    $ StormX.seen_breasts += 1
    $ StormX.seen_pussy += 1
    $ StormX.change_face("normal")

    ch_u "Oh, hello there."

    menu:
        extend ""
        "Um. . . hello?":
            call change_Girl_stat(StormX, "love", 2)
            ch_u "Yes, hello. Care to introduce yourself?"
        "Hey.":

            call change_Girl_stat(StormX, "obedience", 2)
            ch_u "Yes? . . Care to introduce yourself?"
        "Wow.":

            $ StormX.change_face("smile")
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "inhibition", 5)
            ch_u "I seem to have made an impression."
            ch_u "Care to introduce yourself?"
        ". . .":

            $ StormX.change_face("perplexed")
            ch_u "Yes?"
            $ StormX.change_face("normal")

    menu:
        extend ""
        "My name's [Player.name].":
            $ StormX.player_petname = Player.name
            $ StormX.change_face("smile")
            call change_Girl_stat(StormX, "love", 3)
            ch_u "A pleasure to meet you, [Player.name]."
        "It's \"Peter Parker.\"":
            $ StormX.player_petname = "Peter"
            $ StormX.change_face("smile")
            call change_Girl_stat(StormX, "love", 3)
            ch_u "A pleasure to meet you, Peter."
        "You first.":
            $ StormX.change_face("normal")
            call change_Girl_stat(StormX, "love", -2)
            call change_Girl_stat(StormX, "obedience", 5)
            ch_u "I suppose I can indulge you. . ."

    ch_u "My name is \"Ororo Munroe.\" You may call me \"Ororo.\""
    $ StormX.name = "Ororo"
    $ StormX.change_face("sly")
    ch_s "Or \"Ms. Munroe\" if you are nasty."
    $ StormX.names.append("Ms. Munroe")

    menu:
        extend ""
        "Pleased to meet you, Ororo.":
            $ StormX.change_face("smile")
            call change_Girl_stat(StormX, "love", 3)
        "Pleased to meet you, Ms. Munroe.":
            $ StormX.name = "Ms. Munroe"
            $ StormX.change_face("surprised", eyes = "closed", mouth = "sucking")
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 3)
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s "Ha ha ha!"
            $ StormX.change_face("smile")
            ch_s "Please indulge me the small joke."
            ch_s "\"Ororo\" is fine."
        "Don't I know you by another name?":

            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "obedience", 3)
        "Ok, cool.":
            call change_Girl_stat(StormX, "obedience", 2)
        ". . .":
            $ StormX.change_face("normal")
            ch_s "Um. . ."

    ch_s "I've also been known to go by the name \"Storm\"."
    $ StormX.names.append("Storm")

    ch_p "Well then I'll call you. . ."
    menu:
        extend ""
        "Ororo.":
            $ StormX.name = "Ororo"
        "Ms. Munroe.":
            if StormX.name != "Ms. Munroe":
                $ StormX.change_face("surprised", eyes = "closed", mouth = "sucking")
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 3)
                call change_Girl_stat(StormX, "inhibition", 2)
                ch_s "Hahaha!"
                $ StormX.change_face("smile")
                ch_s "I intended it only as a joke!"
            $ StormX.name = "Ms. Munroe"
            call change_Girl_stat(StormX, "love", 3)
            ch_s "Ha! Very well, it shall be our joke."
        "Storm.":
            $ StormX.name = "Storm"
            call change_Girl_stat(StormX, "obedience", 5)
            ch_s "Oh, so formal. Very well."

    if not StormX.player_petname:

        ch_p "My name is [Player.name]."
        $ StormX.player_petname = Player.name
        call change_Girl_stat(StormX, "love", 3)
        ch_s "A pleasure to meet you, [Player.name]."


    $ StormX.change_face("confused")
    ch_s "So did you come all the way up here for a reason?"
    $ StormX.change_face("normal")
    $ Count = 3
    while Count > 0:
        menu:
            extend ""
            "You're certainly naked." if "nudity" not in StormX.history:
                $ StormX.change_face("smile", eyes = "down")
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "obedience", 3)
                call change_Girl_stat(StormX, "inhibition", 5)
                ch_s "Yes, I suppose that I am. . ."
                $ StormX.change_face("normal")
                call Storm_Nudity
            "Don't you want to put something on?" if "nudity" not in StormX.history:
                $ StormX.change_face("confused", mouth = "sad")
                call change_Girl_stat(StormX, "love", -2)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", -3)
                ch_s "Not unless it would make you more comfortable."
                call Storm_Nudity
            "About why I came up":

                menu:
                    extend ""
                    "I heard a lot of noise up here." if "noise" not in StormX.recent_history:
                        $ StormX.change_face("surprised", 2)
                        call change_Girl_stat(StormX, "love", 2)
                        call change_Girl_stat(StormX, "obedience", 5)
                        ch_s "Have I been making too much noise?"
                        $ StormX.change_face("smile", 1, eyes = "down")
                        call change_Girl_stat(StormX, "obedience", 5)
                        ch_s "I suppose that I should be a better neighbor."
                        $ StormX.change_face("smile")
                        ch_s "Please accept my apology."
                        $ StormX.add_word(1, "noise", 0, 0, 0)
                        menu:
                            extend ""
                            "None needed.":
                                call change_Girl_stat(StormX, "love", 5)
                            "How will you make it up to me?":
                                $ StormX.change_face("smile", eyes = "leftside")
                                ch_s ". . ."
                                $ StormX.change_face("smile")
                                call change_Girl_stat(StormX, "obedience", 5)
                                ch_s "I suppose by being more careful in future?"
                            "Ok.":
                                pass
                    "So about the leak." if "water" in Player.recent_history:
                        $ Player.drain_word("water")
                        "You point to some puddles under some of her plants."
                        $ StormX.change_face("surprised", 2, eyes = "leftside")
                        call change_Girl_stat(StormX, "obedience", 5)
                        ch_s "Ah, yes. My apologies."
                        $ StormX.change_face("smile", 2, brows = "sad")
                        ch_s "I was watering my plants, and must have gotten a bit out of hand."
                        $ StormX.change_face("smile", 1)
                        ch_s "One moment. . ."
                        $ StormX.change_face("smile", eyes = "white")
                        "The wind picks up and swirls around the room, drying the puddles."
                        $ StormX.change_face("smile")

                    "You do have lovely plants." if "plants" not in StormX.recent_history:
                        $ StormX.change_face("smile")
                        call change_Girl_stat(StormX, "love", 7)
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s "Thank you."
                        $ StormX.change_face("smile", eyes = "leftside")
                        ch_s "I do my best to bring a bit of nature into this place."
                        $ StormX.change_face("smile")
                        $ StormX.add_word(1, "plants", 0, 0, 0)

                    "[EmmaX.name] said that you were a ghost." if "ghost" not in StormX.recent_history:
                        $ StormX.change_face("angry", eyes = "leftside")
                        ch_s "Oh, I expect she -would- say something like that. . ."
                        $ StormX.change_face("smile")
                        ch_s "Obviously I am as alive as you are."
                        ch_s "I've just recently returned from sabbatical, and was preparing to rejoin the teaching staff."
                        $ StormX.add_word(1, "ghost", 0, 0, 0)
                    "Never mind.":
                        pass

            "My name isn't -really- \"Peter.\"" if StormX.player_petname == "Peter":
                ch_p "It's [Player.name]."
                $ StormX.change_face("surprised", mouth = "smile")
                call change_Girl_stat(StormX, "love", 3)
                call change_Girl_stat(StormX, "obedience", 5)
                ch_s "Oh? A little joke then."
                $ StormX.change_face("smile")
                ch_s "No harm done, \"Peter.\""
                $ StormX.player_petname = Player.name
            "So what powers do you have?" if "powers" not in StormX.recent_history:
                $ StormX.change_face("smile")
                call change_Girl_stat(StormX, "love", 3)
                ch_s "I have the ability to influence the weather around me."
                $ StormX.change_face("smile", eyes = "white")
                call punch
                ch_s "I can summon the rain, call lightning, even glide on the winds."
                $ StormX.change_face("smile")
                ch_s "I very much enjoy the freedom my powers bring me, the connection to nature."
                $ StormX.add_word(1, "powers", 0, 0, 0)
            "That's a lovely accent." if "accent" not in StormX.recent_history:
                $ StormX.change_face("smile")
                call change_Girl_stat(StormX, "love", 5)
                ch_s "Thank you."
                ch_s "I am originally from the States, but spent much of my youth in Kenya."
                $ StormX.add_word(1, "accent", 0, 0, 0)
            "I suppose I should be going. . .":
                ch_s "Oh, I suppose so. . ."
                $ Count = 0



    $ StormX.change_face("smile")
    ch_s "Well, it was lovely meeting you then. . ."
    "She extends her hand to shake yours."
    menu:
        extend ""
        "Shake":
            $ StormX.change_face("surprised", 2)
            "You grab her hand in a firm shake, and a shudder passes through her."
            $ StormX.addiction_rate += 1
            call change_Girl_stat(StormX, "lust", 10)
            $ StormX.change_face("confused")
            ch_s "What was -that-?"
            $ StormX.change_face("surprised", brows = "sad")
            ch_s "I couldn't feel the winds around me!"
        "I probably shouldn't.":
            $ StormX.change_face("confused")
            ch_s "Oh, why not?"

    ch_p "My powers allow me to remove the powers of other mutants."
    ch_p "When I touch them, it seems to have a. . . strong impact."
    if StormX.addiction_rate:
        $ StormX.change_face("sadside", 1)
        call change_Girl_stat(StormX, "love", -15)
        call change_Girl_stat(StormX, "obedience", 20)
        ch_s "Oh. You could have told me that. . ."
    else:
        $ StormX.change_face("confused")
        call change_Girl_stat(StormX, "love", 15)
        ch_s "Oh. . . well thank you for letting me know then."
    $ StormX.change_face("normal")

    if "powers" not in StormX.recent_history:
        $ StormX.change_face("smile")
        ch_s "I suppose you should know, I normally have the ability to influence the weather around me."
        $ StormX.change_face("smile", eyes = "white")
        ch_s "I can summon the rain, call lightning, even glide on the winds."
        $ StormX.change_face("smile")
        ch_s "I very much enjoy the freedom my powers bring me, the connection to nature."

    if "ghost" not in StormX.recent_history:
        ch_s "I suppose you'll be seeing more of me as I join the teaching rotation."

    ch_s "In any case, it was nice meeting you. I suppose I'll see you in class, [StormX.player_petname]."
    if "naked" in Player.recent_history:
        call change_Girl_stat(StormX, "love", 5)
        call change_Girl_stat(StormX, "lust", 3)
        ch_s "Oh, [StormX.player_petname]. . ."
        ch_s ". . .aren't you forgetting something?"
        ch_p "Oh, yeah. . ."
        $ Player.drain_word("naked")
        $ Player.drain_word("cockout")
        "You put your clothes back on. and head back to your room."
    else:
        "You head back to your room."

    if StormX.player_petname == "Peter":
        $ StormX.history.append("Peter")

    $ StormX.petname = StormX.name
    $ StormX.history.append("met")

    $ active_Girls.append(StormX)

    $ EmmaX.weekly_schedule[1][0] = "bg_emma"
    $ EmmaX.weekly_schedule[1][1] = "bg_dangerroom"
    $ EmmaX.weekly_schedule[3][0] = "bg_emma"
    $ EmmaX.weekly_schedule[3][1] = "bg_dangerroom"

    call hide_all(fade = True)
    jump player_room

label Storm_Nudity:

    ch_s "I am not bothered. I do not value modesty so highly."
    ch_s "This is my body and I am unashamed to show it."
    $ StormX.change_face("normal")
    $ StormX.history.append("nudity")
    while True:
        menu:
            extend ""
            "So you don't mind me looking?" if "looking" not in StormX.recent_history:
                $ StormX.add_word(1, "looking", 0, 0, 0)
                $ StormX.change_face("surprised")
                call change_Girl_stat(StormX, "love", 3)
                call change_Girl_stat(StormX, "obedience", 2)
                ch_s "How could I? It's only natural."
                $ StormX.change_face("normal", eyes = "side")
                ch_s ". . ."
                $ StormX.change_face("sly")
                call change_Girl_stat(StormX, "inhibition", 10)
                call change_Girl_stat(StormX, "lust", 2)
                ch_s "Just try not to get too enthusiastic about it. . ."
                $ StormX.change_face("normal")
                ch_s "Was there something else about my body?"
            "Well you're very beautiful." if "hot" not in StormX.recent_history:
                $ StormX.add_word(1, "hot", 0, 0, 0)
                $ StormX.change_face("smile")
                call change_Girl_stat(StormX, "love", 10)
                call change_Girl_stat(StormX, "obedience", 2)
                call change_Girl_stat(StormX, "inhibition", 10)
                ch_s "Thank you. . ."
                ch_s "Was there something else about my body?"
            "Well you're really hot." if "hot" not in StormX.recent_history:
                $ StormX.add_word(1, "hot", 0, 0, 0)
                $ StormX.change_face("sly", brows = "confused")
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "inhibition", 10)
                call change_Girl_stat(StormX, "lust", 2)
                ch_s ". . . Thank you. . ."
                $ StormX.change_face("sly")
                ch_s "Was there something else about my body?"
            "You have a fantastic rack." if "tits" not in StormX.recent_history:
                $ StormX.add_word(1, "tits", 0, 0, 0)
                $ StormX.change_face("surprised", 2)
                ch_s ". . ."
                $ StormX.change_face("sly", 1, brows = "angry", eyes = "down")
                call change_Girl_stat(StormX, "obedience", 15)
                call change_Girl_stat(StormX, "inhibition", 15)
                call change_Girl_stat(StormX, "lust", 2)
                ch_s "Yes, I suppose that I do. . ."
                ch_s ". . ."
                $ StormX.change_face("sly", brows = "confused")
                ch_s "You are aware that this is a bit inappropriate?"
                menu:
                    extend ""
                    "Sorry.":
                        $ StormX.change_face("smile", eyes = "stunned")
                        call change_Girl_stat(StormX, "love", 5)
                        call change_Girl_stat(StormX, "obedience", -2)
                        ch_s "It's not a problem."
                        $ StormX.change_face("smile")
                    "They're just so much nicer than [EmmaX.name]'s.":
                        $ StormX.change_face("perplexed", 2)
                        ch_s ". . ."
                        call change_Girl_stat(StormX, "love", 2)
                        call change_Girl_stat(StormX, "obedience", 2)
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s "Thank you?"
                        $ StormX.change_face("smile", 1)
                        ch_s "I really don't see them as that much better. . ."
                    "They're just so much bigger than [KittyX.name]'s.":
                        $ StormX.change_face("perplexed", 2)
                        ch_s ". . ."
                        call change_Girl_stat(StormX, "love", 3)
                        call change_Girl_stat(StormX, "obedience", 2)
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s "Thank you?"
                        $ StormX.change_face("smile", 1, eyes = "side")
                        ch_s "Kitty's do have their own charm, certainly. . ."
                        $ StormX.change_face("smile")
                    "Yeah.":
                        ch_s ". . ."
                        $ StormX.change_face("smile")
                        call change_Girl_stat(StormX, "obedience", 5)
                        ch_s "Well, so long as you are aware."
                ch_s "Was there something else about my body?"

            "Could I get a feel?" if "touching" not in StormX.recent_history:
                $ StormX.change_face("angry", 2, eyes = "surprised")
                call change_Girl_stat(StormX, "love", -10)
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "lust", 2)
                ch_s ". . ."
                call Storm_Touching
            "So what about sex, is that on the table?" if "touching" not in StormX.recent_history:
                $ StormX.change_face("angry", 2, eyes = "surprised")
                call change_Girl_stat(StormX, "love", -3)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "lust", 2)
                ch_s ". . ."
                call Storm_Touching

            "You've certainly got a jungle going on down there." if "pubes" not in StormX.recent_history:
                $ StormX.add_word(1, "pubes", 0, 0, 0)
                $ StormX.change_face("angry", 2, eyes = "surprised")
                call change_Girl_stat(StormX, "love", -10)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", -5)
                ch_s "I don't believe that's really an appropriate topic of conversation."
                menu:
                    extend ""
                    "I really like it, actually.":
                        call change_Girl_stat(StormX, "love", 10)
                        call change_Girl_stat(StormX, "inhibition", 15)
                        call change_Girl_stat(StormX, "lust", 5)
                    ". . .":
                        pass
                $ StormX.change_face("angry", 2, eyes = "down")
                ch_s "I just don't see the point in \"gardening\" down there. . ."
                $ StormX.change_face("angry", 1)

            "So could you put some clothes on?" if "nudity" in StormX.history and not StormX.Clothes["top"]:
                $ StormX.change_face("sly")
                call change_Girl_stat(StormX, "love", -2)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", -3)
                ch_s "If it would make you more comforable, then I would not mind it."
                $ StormX.today_outfit_name = "default"
                $ StormX.outfit_name = "default"
                $ StormX.change_Outfit()

            "Should I get naked too?" if "naked" not in Player.recent_history:
                $ StormX.change_face("surprised", mouth = "sucking")
                call change_Girl_stat(StormX, "love", 3)
                call change_Girl_stat(StormX, "obedience", 2)
                call change_Girl_stat(StormX, "inhibition", 10)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "Haha!"
                $ StormX.change_face("smile")
                ch_s "If that would make you more comfortable, I do not mind."
                call Girl_First_Peen (StormX, 0, 1)
                $ StormX.change_face("smile")
            "No, I suppose not. . . [[return]":
                return

    return

label Storm_Touching:

    $ StormX.change_face("angry", 1)
    ch_s "Do not confuse my words."
    ch_s "I am not ashamed of my body, but nor is it available for common use."
    menu:
        extend ""
        "Sorry, no offense intended.":
            $ StormX.change_face("angry", eyes = "side")
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", -2)
            call change_Girl_stat(StormX, "inhibition", 5)
            ch_s "It is fine. I really cannot blame you for asking."
            $ StormX.change_face("normal")
            ch_s "Children these days are so impulsive."
        "Who said I was \"common?\"":
            $ StormX.change_face("surpised", 2, mouth = "sucking")
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 10)
            ch_s "Ha! You do have an excellent sense of humor."
            $ StormX.change_face("sly", 1)
            call change_Girl_stat(StormX, "love", 3)
            ch_s "Certainly, you are \"uncommon.\""
            call change_Girl_stat(StormX, "inhibition", 10)
            call change_Girl_stat(StormX, "lust", 5)
            ch_s "-but I am afraid it will take more than that."
        "So. . . never?":
            $ StormX.change_face("perplexed")
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 10)
            ch_s ". . ."
            $ StormX.change_face("sly", eyes = "side")
            call change_Girl_stat(StormX, "inhibition", 10)
            call change_Girl_stat(StormX, "lust", 5)
            ch_s "I cannot say that it would be -impossible-. . ."
            $ StormX.change_face("sly")
        "Ok.":
            $ StormX.change_face("normal")
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "obedience", -2)
            ch_s "Glad to know that we have an understanding."
    $ StormX.add_word(1, "touching", 0, 0, 0)

    ch_s "Now, was there something else about my body?"
    return

label Storm_Peter:
    $ StormX.history.remove("Peter")

    if Player.name == "Peter Parker":
        return

    $ Player.location = "bg_classroom"

    call clear_the_room (StormX, 0, 1)

    "Before class begins, [StormX.name] rushes up to you."

    $ StormX.location = "bg_classroom"

    $ shift_focus (StormX)
    call set_the_scene

    $ StormX.change_face("angry", 2, eyes = "surprised")
    ch_s "[Player.name]!"
    $ StormX.change_face("angry")
    ch_s "Yes, I know your name is not \"Peter Parker.\""
    ch_s "Emma told me when I could not find your name on the roster."
    call change_Girl_stat(StormX, "love", -5)
    call change_Girl_stat(StormX, "love", -20)
    ch_s "I cannot believe you would make a fool of me like that."
    call change_Girl_stat(StormX, "love", -50)
    call change_Girl_stat(StormX, "obedience", 5)
    ch_s "I will not forget that."
    $ StormX.player_petname = Player.name
    $ Player.location = "bg_classroom"
    call set_the_scene
    return








label Storm_Teacher_Caught(Girl=0):


    if "noticed " + Girl.tag in StormX.recent_history:
        return
    if approval_check(StormX, 500, "I") and approval_check(StormX, 1500) and StormX.likes[Girl.tag] >= 500:
        "[StormX.name] notices the two of you, but just nods in approval and continues on."
        $ StormX.check_if_likes(Girl,800,3, 1)
        $ Girl.check_if_likes(StormX,800,3, 1)
        $ StormX.recent_history.append("noticed " + Girl.tag)
        return

    ch_s "[Player.name]? [Girl.name]? Could you please stop what you are doing there?"
    $ checkout()
    call reset_player

    $ Girl.change_face("bemused", 2, eyes = "side")

    call show_full_body(Girl)

    if approval_check(Girl, 700, "I"):
        $ Girl.change_face("bemused", 1)
        "[Girl.name] shrugs and returns to her seat."
        call Partner_Like (StormX, 2, -1, 500, Girl)
    else:
        "[Girl.name] jumps and dashes out of the room."
        call Partner_Like (StormX, -2, -3, 500, Girl)
        call remove_Girl(Girl)

    $ Girl.reputation -= 1
    call Partner_Like (Girl, 3, 2, 800, StormX)
    $ StormX.check_if_likes(Girl,800,3, 1)

    $ Player.reputation -= 1
    ch_s "Thank you."

    jump reset_location



label Storm_Hairtalk:

    $ shift_focus (StormX)
    $ Player.location = "bg_classroom"

    call clear_the_room (StormX, 0, 1)
    call set_the_scene
    call alternate_clothes (StormX, 8)
    $ StormX.change_face("normal")
    "When class ends, [StormX.name] calls you to her desk."
    ch_s "[StormX.player_petname], I was noticing that you seemed. . . distracted in class lately."
    ch_s "Was there anything I could do to help you remain attentive?"
    menu:
        extend ""
        "No, I'll try to pay better attention.":
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "love", 2)
            ch_s ". . ."
            ch_s "Very well then. . ."
        "You're just too beautiful.":
            call change_Girl_stat(StormX, "love", 3)
            call change_Girl_stat(StormX, "love", 2)
            $ StormX.change_face("surprised")
            ch_s ". . ."
            $ StormX.change_face("smile", eyes = "side")
            call change_Girl_stat(StormX, "obedience", 1)
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s "That is sweet."
            $ StormX.change_face("bemused")
            ch_s "But I would not wish to be to blame for your failing in class."
        "I can't help staring at your tits.":
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            $ StormX.change_face("surprised")
            ch_s ". . ."
            if approval_check(StormX, 700):
                $ StormX.change_face("confused", eyes = "side")
                call change_Girl_stat(StormX, "love", 2)
                ch_s "That is. . . sweet."
            else:
                $ StormX.change_face("angry")
                call change_Girl_stat(StormX, "love", -2)
                ch_s "That is completely inapprorpiate."
            $ StormX.change_face("bemused")
            ch_s "But I would not wish to be to blame for your failing in class."
        "I don't know.":
            call change_Girl_stat(StormX, "love", -1)
            call change_Girl_stat(StormX, "obedience", -2)
            $ StormX.change_face("confused")
            ch_s ". . ."
            $ StormX.change_face("bemused")
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s "Well, perhaps we could think of something?"
    ch_s "I was thinking that perhaps I could reward your performance. . somehow."
    $ StormX.add_word(1, "uninterrupted", 0, 0, 0)
    $ Player.add_word(1, "interruption")
    menu:
        extend ""
        "That's fine, don't worry about it.":
            call change_Girl_stat(StormX, "love", 1)
            call change_Girl_stat(StormX, "obedience", -1)
            $ StormX.change_face("confused")
            ch_s ". . ."
            $ StormX.change_face("sad")
            ch_s ". . . If you are certain. . ."
        "Maybe you could flash me?":
            call change_Girl_stat(StormX, "obedience", 2)
            $ StormX.change_face("bemused", 1, eyes = "side")
            pause 0.4
            $ StormX.eyes = "leftside"
            pause 0.4
            $ StormX.eyes = "squint"
            if approval_check(StormX, 700):
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "inhibition", 1)
                ch_s "I. . . suppose that I might accomodate that. . ."
                call change_Girl_stat(StormX, "inhibition", 2)
                $ StormX.top_pulled_up = True
                $ StormX.upskirt = True
                pause 1
                $ StormX.top_pulled_up = False
                $ StormX.upskirt = False
                ch_s ". . ."
            else:
                call change_Girl_stat(StormX, "love", -2)
                call change_Girl_stat(StormX, "inhibition", 1)
                ch_s "I may be comfortable with my body, but that is an inappropriate request."
        "Maybe take some clothes off?":
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "obedience", 1)
            $ StormX.change_face("bemused", 1, eyes = "side")
            pause 0.4
            $ StormX.eyes = "leftside"
            pause 0.4
            $ StormX.eyes = "squint"
            if approval_check(StormX, 800):
                call change_Girl_stat(StormX, "inhibition", 1)
                call change_Girl_stat(StormX, "inhibition", 2)
                $ taboo = 0
                $ StormX.taboo = 0
                ch_s "I. . . suppose that I might accomodate that. . ."
                call undress_Girl (StormX)
                $ taboo = 40
                $ StormX.taboo = 40
            else:
                call change_Girl_stat(StormX, "love", -2)
                call change_Girl_stat(StormX, "inhibition", 5)
                ch_s "I may be comfortable with my body, but that is an inappropriate request."
        "Maybe a kiss?":
            call change_Girl_stat(StormX, "love", 1)
            $ StormX.change_face("bemused")
            if approval_check(StormX, 700) or StormX.Kiss:
                call change_Girl_stat(StormX, "love", 3)
                call change_Girl_stat(StormX, "obedience", 1)
                call change_Girl_stat(StormX, "inhibition", 1)
                ch_s "I. . . suppose that I might accomodate that. . ."

                call before_action(StormX, "kiss")
            else:
                call change_Girl_stat(StormX, "obedience", -1)
                ch_s "I do not think that I should do that. . ."
        "Maybe some fondling?":
            call change_Girl_stat(StormX, "obedience", 2)
            if approval_check(StormX, 900) or ((StormX.permanent_History["fondle_breasts"]+ StormX.permanent_History["fondle_pussy"] + StormX.permanent_History["fondle_ass"]) > 0):
                $ StormX.change_face("bemused", 1, eyes = "side")
                pause 0.4
                $ StormX.eyes = "leftside"
                pause 0.4
                $ StormX.eyes = "squint"
                call change_Girl_stat(StormX, "inhibition", 2)
                ch_s "I. . . suppose that I might accomodate that. . ."
                call change_Girl_stat(StormX, "obedience", 2)
                call change_Girl_stat(StormX, "obedience", 1)

                call before_action(StormX, "fondle_breasts")
            else:
                $ StormX.change_face("angry", 2)
                ch_s "[StormX.player_petname]!"
                $ StormX.change_face("angry", 1)
                call change_Girl_stat(StormX, "love", -3)
                call change_Girl_stat(StormX, "obedience", -1)
                ch_s "That would be highly inappropriate!"

    $ StormX.drain_word("uninterrupted")
    ch_s "Ok, I think that will be enough for now."
    "As you turn to leave, you notice a photo on the desk"
    show Storm_Photo zorder 150 with easeinbottom
    $ StormX.change_face("bemused")
    ch_s "Oh, that was me during an earlier, more rebellious phase."
    hide Storm_Photo with easeoutbottom
    $ StormX.history.append("mohawk")
    menu:
        extend ""
        "You look great like that.":
            call change_Girl_stat(StormX, "love", 2)
            $ StormX.change_face("smile")
            ch_s "Oh, should I try it again?"
            menu:
                extend ""
                "Sure, go for it.":
                    call change_Girl_stat(StormX, "love", 1)
                    call change_Girl_stat(StormX, "love", 1)
                    call change_Girl_stat(StormX, "obedience", 2)
                    if approval_check(StormX, 700):
                        ch_s "I think that I shall."
                        $ StormX.to_do.append("hair")
                    else:
                        ch_s "I may consider it in future. . ."
                "Not really, you look great this way too.":
                    call change_Girl_stat(StormX, "love", 1)
                    call change_Girl_stat(StormX, "love", 2)
                    call change_Girl_stat(StormX, "inhibition", 2)
                    ch_s "Thank you, I appreciate that. . ."
                "No.":
                    call change_Girl_stat(StormX, "love", -1)
                    $ StormX.change_face("sadside")
                    ch_s ". . ."
                    call change_Girl_stat(StormX, "obedience", 2)
                    call change_Girl_stat(StormX, "obedience", 1)
                    ch_s "I suppose I can understand that. . ."
                    $ StormX.change_face("bemused")
                    ch_s "I do enjoy my current style. . ."
        "I don't think that look works for you.":
            call change_Girl_stat(StormX, "love", -2)
            $ StormX.change_face("sadside")
            ch_s ". . ."
            call change_Girl_stat(StormX, "obedience", 1)
            call change_Girl_stat(StormX, "obedience", 2)
            ch_s "I suppose I can understand that. . ."
            $ StormX.change_face("bemused")
            ch_s "I do enjoy my current style. . ."
        "Ok.":
            call change_Girl_stat(StormX, "obedience", 2)
    ch_s "I suppose that is all I needed to tell you. . ."
    return



label Storm_Detention:

    $ shift_focus (StormX)
    call clear_the_room (StormX, 0, 1)
    if True:
        "You enter the room and see [StormX.name] waiting for you at the back of the room."
    else:
        "After class, the students file out, and you wait a few minutes until they're all gone."
        "Once the last student leaves, [StormX.name] approaches you."
    show black_screen onlayer black
    $ Player.location = "bg_classroom"
    $ StormX.location = "bg_classroom"
    $ StormX.change_Outfit()
    call set_the_scene
    $ StormX.change_face("sly")
    $ StormX.arm_pose = 2
    $ Count = 0
    call clear_the_room (StormX, 0, 1)
    hide black_screen onlayer black
    $ line = 0
    if "detention" in Player.daily_history:
        ch_s "I'm glad you take your. . . education seriously."
    else:

        $ StormX.change_face("surprised")
        ch_s "Oh, [StormX.player_petname], you really shouldn't skip your detention like that. . ."
    $ Player.traits.remove("detention")
    $ StormX.recent_history.append("detention")
    $ StormX.daily_history.append("detention")
    $ StormX.change_face("sly")
    call change_Girl_stat(StormX, "lust", 3)
    ch_s "You've been such a naughty pupil. . ."
    $ StormX.arm_pose = 1
    $ StormX.change_face("sadside", brows = "normal")
    call change_Girl_stat(StormX, "lust", 5)
    ch_s "Chasing after those young girls. . ."
    $ StormX.change_face("sly")
    call change_Girl_stat(StormX, "lust", 3)
    if "detention" in StormX.history:
        ch_s "How will we deal with it this time?"
    else:

        ch_s "What am I to do with you. . ."
        $ StormX.history.append("detention")

    "[StormX.name] walks to the door and locks it behind her."
    $ taboo = 0
    $ StormX.taboo = 0
    $ Player.traits.append("locked")
    menu:
        extend ""
        "I guess I should focus on my studies.":
            if approval_check(StormX, 900) and "classcaught" in StormX.history:
                $ StormX.change_face("perplexed")
                call change_Girl_stat(StormX, "inhibition", -3)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "Oh. Really? I was thinking of a more. . . recreational punishment."
                menu:
                    extend ""
                    "Kidding, of course, what should we do? [[sex stuff]":
                        $ StormX.change_face("sly")
                        call change_Girl_stat(StormX, "love", 3)
                        call change_Girl_stat(StormX, "obedience", 5)
                        call change_Girl_stat(StormX, "inhibition", 5)
                        ch_s "Why do I put up with you?"
                        call enter_main_sex_menu(StormX)
                    "No, you're right, I take my education too lightly.":
                        call change_Girl_stat(StormX, "love", 1)
                        call change_Girl_stat(StormX, "inhibition", -2)
                        call change_Girl_stat(StormX, "lust", 5)
                        ch_s "Oh. Ok. Um. . ."
                        $ StormX.change_face("sad")
                        call change_Girl_stat(StormX, "obedience", 5)
                        call change_Girl_stat(StormX, "lust", 5)
                        ch_s "I guess we could go over some of the topics from today's class then. . ."
                        call change_Girl_stat(StormX, "lust", 5)
                        $ Player.XP += 10
            else:

                $ StormX.change_face("sad", mouth = "normal")
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "Yes. . . Exactly. . ."
                call change_Girl_stat(StormX, "inhibition", 5)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "I guess we could go over some of the topics from today's class then. . ."
                call change_Girl_stat(StormX, "inhibition", 5)
                call change_Girl_stat(StormX, "lust", 5)
                $ Player.XP += 10
        "I could think of a few things. . . [[sex stuff]":
            if approval_check(StormX, 900) and "classcaught" in StormX.history:
                $ StormX.change_face("sly")
                call change_Girl_stat(StormX, "lust", 5)
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", 5)
                ch_s "I just bet you can. . ."
                call enter_main_sex_menu(StormX)

            else:

                $ StormX.change_face("sad", mouth = "smirk")
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "I'm sure you could. . . but unfortunately this isn't the time for it."
                call change_Girl_stat(StormX, "inhibition", 5)
                call change_Girl_stat(StormX, "inhibition", 5)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "We'll just have to settle for going over some of the topics from today's class. . ."
                call change_Girl_stat(StormX, "inhibition", 5)
                call change_Girl_stat(StormX, "lust", 5)
                $ Player.XP += 10
    $ round = 20 if round > 20 else round
    ch_s "Ok, I think that's plenty for now. . ."
    ch_s "You wouldn't want to make this a habit. . ."
    $ approval_bonus = 0
    $ StormX.change_Outfit()
    $ Player.drain_word("locked", 0, 0, 1)
    return








label Storm_Key:
    $ shift_focus (StormX)
    call set_the_scene
    $ StormX.change_face("bemused")
    $ StormX.arm_pose = 2
    ch_s "You have been coming up more often. . ."
    ch_s ". . . you might want a key. . ."
    ch_p "Thanks."
    $ StormX.arm_pose = 1
    $ Player.Keys.append(StormX)
    $ StormX.event_happened[0] = 1
    return






label Storm_BF:
    $ shift_focus (StormX)
    if StormX.location != Player.location:

        if StormX not in Player.Party:
            "[StormX.name] approaches you and asks if the two of you can talk."
        else:
            "[StormX.name] turns towards you and asks if the two of you can talk."
    $ StormX.drain_word("asked_to_meet")

    call set_the_scene

    call set_Character_taboos
    call clear_the_room (StormX)
    $ StormX.daily_history.append("relationship")

    $ StormX.change_face("smile")
    ch_s "[StormX.player_petname]. . . I was hoping that we could talk. . ."
    menu:
        extend ""
        "Yes?":
            pass
        "I'm kinda busy.":
            $ StormX.change_face("sadside")
            call change_Girl_stat(StormX, "love", -5)
            call change_Girl_stat(StormX, "obedience", 2)
            ch_s "Then I won't take more of your time than is necessary."
            $ StormX.change_face("smile")

    $ StormX.event_happened[5] = 20

    ch_s "I have been enjoying the time we've spent together."
    ch_s "I mean to say, I have been enjoying you."
    $ StormX.change_face("smile", eyes = "side")
    ch_s ". . ."
    $ StormX.change_face("smile")
    ch_s "May I tell you a story?"
    menu:
        extend ""
        "Sure.":
            pass
        "Can we not?":
            call change_Girl_stat(StormX, "love", -5)
            call change_Girl_stat(StormX, "obedience", 3)
            call change_Girl_stat(StormX, "inhibition", -2)
            $ StormX.change_face("confused")
            ch_s "I think you will benefit from it."
        "Like I said, I'm really busy here.":
            $ StormX.change_face("sadside")
            call change_Girl_stat(StormX, "love", -5)
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", -2)
            ch_s "Then I won't take more of your time."
            ch_s "Let me know when your. . . schedule clears up."
            call remove_Girl(StormX)
            $ Player.history.append("story")
            return

label Storm_BF_Story:
    $ StormX.change_face("smile")
    ch_s "When I was a child, I spent a lot of my time alone."
    ch_s "I was abandoned on the streets of Cairo, and had to fend for myself. . ."
    $ StormX.change_face("sadside")
    ch_s ". . . as a pickpocket."
    ch_s "Years later, I travelled south to Kenya, but for so much of my time, I had nobody that I could count on."
    $ StormX.change_face("smile")
    ch_s "Since I have come here, I have learned to value the strong bonds that I have with my teammates."
    if Player.Harem:
        if len(Player.Harem) >= 2:
            ch_s "And I know that you have been sharing your time with other girls, "
        else:
            ch_s "And I know that you have been sharing your time with [Player.Harem[0].name], "
        if approval_check(StormX, 1500):
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s ". . . but I can accept that."
        else:
            ch_s ". . . and we can discuss that. . ."
    $ StormX.change_face("sly")
    ch_s "I just want to know that you are there for me too."
    menu:
        extend ""
        "Of course I am.":
            $ StormX.change_face("smile")
            call change_Girl_stat(StormX, "love", 7)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s "That is a relief to hear."
        "I'm not big on commitment. . .":
            $ StormX.change_face("sadside")
            call change_Girl_stat(StormX, "love", -5)
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", -2)
            ch_s ". . . that is unfortunate."
            $ StormX.change_face("sad")
            ch_s "Let me know if you should reconsider then."
            return
        "Well, I guess. . .":
            $ StormX.change_face("sadside")
            call change_Girl_stat(StormX, "love", -3)
            call change_Girl_stat(StormX, "obedience", 1)
            call change_Girl_stat(StormX, "inhibition", -2)
            ch_s "That is. . . not exactly the answer I was looking for. . ."

    if Player.Harem:
        if approval_check(StormX, 1500):

            $ StormX.change_face("sly", eyes = "side")
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", 5)
            ch_s "I would be happy to join your little \"harem.\""
            $ StormX.change_face("sly")
            ch_s "If you'll have me."
        else:

            ch_s "I would prefer to be your one and only. . ."
            menu:
                extend ""
                "I could break up with them. . ." if len(Player.Harem) >= 2:
                    $ StormX.change_face("smile")
                    call change_Girl_stat(StormX, "love", 10)
                    call change_Girl_stat(StormX, "obedience", 5)
                    call change_Girl_stat(StormX, "inhibition", 5)
                    ch_s "Excellent!"
                    ch_s "Do let them down gently though. . ."
                    return
                "I could break up with her. . ." if len(Player.Harem) == 1:
                    $ StormX.change_face("smile")
                    call change_Girl_stat(StormX, "love", 10)
                    call change_Girl_stat(StormX, "obedience", 5)
                    call change_Girl_stat(StormX, "inhibition", 5)
                    ch_s "Excellent!"
                    ch_s "Do let her down gently though. . ."
                    return
                "I can't do that.":
                    $ StormX.change_face("sadside")
                    call change_Girl_stat(StormX, "love", -5)
                    call change_Girl_stat(StormX, "obedience", 5)
                    call change_Girl_stat(StormX, "obedience", 5)
                    call change_Girl_stat(StormX, "inhibition", -3)
                    ch_s ". . .oh."
                    ch_s "Well that is a disappointment."
                    if not approval_check(StormX, 1000):
                        ch_s "I suppose that will be all then."
                        call remove_Girl(StormX)
                        return
                    else:
                        call change_Girl_stat(StormX, "obedience", 5)
                        call change_Girl_stat(StormX, "inhibition", 3)
                        call change_Girl_stat(StormX, "inhibition", 2)
                        ch_s ". . . I suppose that I could accept this. . . arrangement."
        menu:
            extend ""
            "I would love that!" if "StormYes" in Player.traits:
                call change_Girl_stat(StormX, "love", 20)
                call change_Girl_stat(StormX, "inhibition", 5)
                ch_s "Excellent!"
                jump Storm_BF_End
            "I would love that. . . but. . ." if "StormYes" not in Player.traits:
                $ StormX.change_face("confused")
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 5)
                ch_s ". . . but?"
                if len(Player.Harem) >= 2:
                    ch_p "The others weren't into that. . ."
                else:
                    ch_p "[Player.Harem[0].name] wasn't into that. . ."
                $ StormX.change_face("sadside")
                ch_s ". . .oh."
                ch_s "Well that is a disappointment."
                ch_s "Let me know if the situation. . . clears up."
            "No thanks.":
                $ StormX.change_face("sadside")
                call change_Girl_stat(StormX, "love", -25)
                call change_Girl_stat(StormX, "obedience", 10)
                ch_s ". . .oh."
                ch_s "Very well then."
                ch_s "I will take no more of your time."
    else:


        ch_s "So would you mind if I considered you my. . . \"boyfriend?\""
        menu:
            extend ""
            "I'd love that!":
                call change_Girl_stat(StormX, "love", 20)
                call change_Girl_stat(StormX, "inhibition", 5)
                $ StormX.change_face("smile")
                ch_s "Excellent!"
                jump Storm_BF_End
            "I'd rather you didn't.":
                call change_Girl_stat(StormX, "love", -20)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "obedience", 5)
                $ StormX.change_face("sadside")
                ch_s ". . .oh."
                ch_s "Well that is a disappointment."
            "Suit yourself.":
                call change_Girl_stat(StormX, "love", -5)
                if approval_check(StormX, 1000):
                    $ StormX.change_face("confused")
                    call change_Girl_stat(StormX, "obedience", 5)
                    call change_Girl_stat(StormX, "obedience", 5)
                    ch_s ". . .very well then. I shall do that. . ."
                    jump Storm_BF_End
                else:
                    $ StormX.change_face("sadside")
                    call change_Girl_stat(StormX, "obedience", 5)
                    ch_s ". . . that was not the reaction I had expected. . ."
                    ch_s "Perhaps I should give this further consideration. . ."

    return
label Storm_BF_End:
    $ StormX.player_petnames.append("boyfriend")

    if not simulation:
        $ Player.Harem.append(StormX)
        if "StormYes" in Player.traits:
            $ Player.traits.remove("StormYes")
    return






label Storm_Love:

    $ StormX.drain_word("asked_to_meet")
    if StormX.location == Player.location or StormX in Player.Party:
        "[StormX.name] glances over at you with an apprising look on her face."
    else:
        "[StormX.name] turns a corner and notices you."
    if Player.location != "bg_storm" and Player.location != "bg_player":
        "With little word, she takes your hand and pulls you up to her room."
        $ Player.location = "bg_storm"

    call set_the_scene
    call clear_the_room (StormX)
    call set_Character_taboos
    $ StormX.daily_history.append("relationship")

    $ StormX.change_face("sadside", 1)
    ch_s "[StormX.player_petname]. . . I have a bit of a problem. . ."
    menu:
        extend ""
        "What is it?":
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "inhibition", 1)
            $ StormX.change_face("smile")
        "Can I help?":
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "obedience", 2)
            $ StormX.change_face("smile")
            ch_s "Perhaps. . ."
        "That sucks.":
            call change_Girl_stat(StormX, "love", -5)
            call change_Girl_stat(StormX, "inhibition", 2)
            $ StormX.event_happened[6] += 1
            $ StormX.change_face("angry", 2)
            ch_s ". . ."
            $ StormX.change_face("normal", 1)
        "Ok.":
            call change_Girl_stat(StormX, "love", -3)
            $ StormX.change_face("confused", 1)
            if not approval_check(StormX, 800, "OI"):
                $ StormX.event_happened[6] += 1
                call change_Girl_stat(StormX, "love", -2)
            ch_s ". . ."
    if len(Player.Harem) >= 2:
        ch_s "I know that you have to divide yourself among multiple women. . ."
    elif StormX in Player.Harem:
        ch_s "We make a pretty cute couple so far. . ."
    $ StormX.change_face("sad", 1)
    ch_s "I have been considering my feelings for you. . ."
    $ StormX.change_face("sadside", 1)
    ch_s "I have reached an uncomfortable conclusion."
    ch_s "I feel that I am somewhat \"bound\" you to. . ."
    menu:
        extend ""
        "What do you mean?":
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "inhibition", 1)
            $ StormX.change_face("normal", 1)
            ch_s "Allow me to explain. . ."
        "Is it something I did?":
            call change_Girl_stat(StormX, "love", -1)
            call change_Girl_stat(StormX, "inhibition", -2)
            $ StormX.change_face("surprised", 1)
            ch_s "Oh, no, not intentionally, at least. . ."
            $ StormX.change_face("normal", 1)
        "Kinky.":
            call change_Girl_stat(StormX, "obedience", 3)
            call change_Girl_stat(StormX, "inhibition", 5)
            $ StormX.change_face("confused", 1)
            if not approval_check(StormX, 600, "OI"):
                call change_Girl_stat(StormX, "love", -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("sly", 1)
            ch_s ". . . that is. . . not the reaction I intended. . ."
            $ StormX.change_face("normal", 1)
        "Ok":
            call change_Girl_stat(StormX, "obedience", 2)
            $ StormX.change_face("confused", 1)
            if not approval_check(StormX, 800, "OI"):
                call change_Girl_stat(StormX, "love", -2)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("angry", 1)
            ch_s ". . ."
    ch_s "My concern leads back to my childhood."
    $ StormX.change_face("sadside", 1)
    ch_s "When I was very young, a building I was in was hit by a terrorist attack."
    ch_s "It fell around me, trapping me under the rubble."
    $ StormX.eyes = "closed"
    ch_s "For days I was surrounded by the earth, barely able to move."
    ch_s ". . . barely able to breathe."
    menu:
        extend ""
        "How awful!":
            call change_Girl_stat(StormX, "love", 4)
            $ StormX.change_face("normal", 1)
            ch_s "Yes, but I managed."
        "That must have been difficult.":
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            $ StormX.change_face("smile", 1, eyes = "side")
            ch_s "Thank you, yes, but I managed."
        "Wow.":
            call change_Girl_stat(StormX, "obedience", 2)
            $ StormX.change_face("confused", 1)
            if not approval_check(StormX, 600, "OI"):
                call change_Girl_stat(StormX, "love", -3)
                call change_Girl_stat(StormX, "inhibition", -2)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("angry", 1)
            ch_s ". . ."
            ch_s "Yes. \"Wow.\""
        "Cool!":
            call change_Girl_stat(StormX, "love", -5)
            $ StormX.event_happened[6] += 1
            $ StormX.change_face("surprised", 2)
            ch_s ". . ."
            $ StormX.change_face("angry", 1)
            ch_s "Perhaps try not to sound so excited?"
        "Ok.":
            call change_Girl_stat(StormX, "love", -2)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 1)
            $ StormX.change_face("sadside", 1)
            if not approval_check(StormX, 800, "OI"):
                call change_Girl_stat(StormX, "love", -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("angry", 1)
            ch_s ". . ."
            ch_s "I did expect a bit more \"engagement\" here. . ."
    ch_s "At the end of the third day, the concrete above me shifted, and a hand reached down."
    $ StormX.change_face("smile", 1)
    ch_s "Workers had managed to find me and dig their way to me."
    $ StormX.change_face("sadside", 1)
    ch_s "Even after I'd recovered from the physical trauma of the event, I wasn't competely healed."
    ch_s " I found that I had lasting mental scars from the experience. . ."
    menu:
        extend ""
        "I can understand that.":
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 1)
            $ StormX.change_face("smile", 1)
            ch_s "I love that about you. . ."
        "What kind?":
            call change_Girl_stat(StormX, "love", 4)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            $ StormX.change_face("normal", 1)
        "Yeah, I bet.":
            call change_Girl_stat(StormX, "love", -2)
            call change_Girl_stat(StormX, "obedience", 2)
            $ StormX.change_face("angry", 1, brows = "confused")
            ch_s ". . ."
        "So you're crazy then?":
            call change_Girl_stat(StormX, "love", -5)
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", -5)
            $ StormX.event_happened[6] += 2
            $ StormX.change_face("angry", 2)
            ch_s "Of course not!"
            ch_s "That is an inapporpriate way to discuss such things."
            $ StormX.blushing = "_blush1"
        "Ok.":
            call change_Girl_stat(StormX, "love", -5)
            $ StormX.event_happened[6] += 1
            $ StormX.change_face("angry", 1, eyes = "side")
            ch_s "Why do I feel like you are not engaged in this conversation?"

    ch_s "The experience left me with fairly strong \"claustrophobia.\" a fear of confinement."
    ch_s "It made me seek out open spaces, places from which I always felt like I could flee."
    $ StormX.change_face("bemused", 1)
    ch_s "So I expect that you understand what a difficulty you've caused me. . ."
    $ line = 1
    while line > 0:
        $ line -= 1
        menu:
            extend ""
            "Yeah, I understand." if "iknow" not in StormX.recent_history:
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "obedience", 2)
                $ StormX.add_word(1, "iknow", 0, 0, 0)
                $ StormX.change_face("smile", 1, brows = "confused")
                $ line += 1
                ch_s "Oh?"
            "I'm afraid I don't. . .":
                if "iknow" in StormX.recent_history and "strong" not in StormX.recent_history:

                    call change_Girl_stat(StormX, "love", -2)
                    call change_Girl_stat(StormX, "obedience", -5)
                    call change_Girl_stat(StormX, "inhibition", 2)
                    ch_s ". . ."
                    $ StormX.change_face("sadside", 1)
                    ch_s "You seemed so confident. . ."
                else:
                    call change_Girl_stat(StormX, "love", 5)
                    call change_Girl_stat(StormX, "obedience", -2)
                    call change_Girl_stat(StormX, "inhibition", 5)
                    $ StormX.change_face("smile", 1)
                    ch_s "That is fair. . ."
            "You feel like I trap you.":
                call change_Girl_stat(StormX, "love", 7)
                call change_Girl_stat(StormX, "obedience", 2)
                $ StormX.change_face("sad", 1)
                ch_s "Yes. . . I'm afraid so. . ."
            "You think I'm too strong." if "strong" not in StormX.recent_history:
                $ StormX.change_face("confused", 1)
                ch_s "What?"
                menu:
                    extend ""
                    "Nothing! Never mind.":
                        call change_Girl_stat(StormX, "obedience", -2)
                        ch_s "Ok. . ."
                    "Like, I can hold you and you can't get away.":
                        call change_Girl_stat(StormX, "love", -3)
                        call change_Girl_stat(StormX, "obedience", -1)
                        $ StormX.change_face("surprised", 1)
                        ch_p "Because I'm strong."
                        call change_Girl_stat(StormX, "obedience", -1)
                        call change_Girl_stat(StormX, "inhibition", -2)
                        $ StormX.change_face("angry", 1)
                        ch_s ". . ."
                        ch_s "No."
                $ StormX.add_word(1, "strong", 0, 0, 0)
                $ line += 1
            "Nope.":
                call change_Girl_stat(StormX, "love", -5)
                call change_Girl_stat(StormX, "obedience", -2)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("angry", 1)
                ch_s ". . ."
                $ StormX.eyes = "side"
                ch_s "I suppose that should not surprise me. . ."
            "Lady problems,\" right?":
                call change_Girl_stat(StormX, "love", -10)
                $ StormX.event_happened[6] += 2
                $ StormX.change_face("surprised", 2)
                ch_s ". . ."
                call change_Girl_stat(StormX, "obedience", -2)
                call change_Girl_stat(StormX, "inhibition", -2)
                $ StormX.change_face("angry", 2)
                ch_s ". . .No."
                $ StormX.blushing = "_blush1"
                ch_s "It is not. . . \"lady problems.\""
            "[[shrug]":
                call change_Girl_stat(StormX, "love", -3)
                if not approval_check(StormX, 800, "OI"):
                    call change_Girl_stat(StormX, "love", -2)
                    $ StormX.event_happened[6] += 2
                $ StormX.change_face("angry", 1)
                ch_s ". . ."
    if StormX.event_happened[6] >= 5:

        jump Storm_Love_Badend

label Storm_Love_Redux:

    ch_s "The closer we get to each other, the less able I feel I am to. . ."
    $ StormX.change_face("sadside", 1)
    ch_s ". . . to pull myself -free- from you."
    menu:
        extend ""
        "Is that what you want?":
            call change_Girl_stat(StormX, "love", 1)
            $ StormX.change_face("surprised", 2)
            ch_s "No!"
            call change_Girl_stat(StormX, "love", 2)
            $ StormX.change_face("smile", 1, eyes = "side")
            ch_s ". . . no. . ."
            call change_Girl_stat(StormX, "love", 3)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            $ StormX.change_face("smile", 1)
            ch_s "I suppose that I do not. . ."
        "Can I do anything?":
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "inhibition", 4)
            $ StormX.change_face("smile", 1)
            ch_s "I do not believe anything -needs- to be done here."
            ch_s "I am content with this. . ."
        "Yeah, I have that effect on women.":
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 3)
            $ StormX.change_face("sly", 1)
            if not approval_check(StormX, 600, "OI"):
                call change_Girl_stat(StormX, "love", -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("angry", 1, mouth = "smile")
            ch_s "Try to avoid a swelled head, [StormX.player_petname]"
        "Cool!":
            call change_Girl_stat(StormX, "love", -5)
            $ StormX.event_happened[6] += 2
            $ StormX.change_face("angry", 1)
            ch_s "I am glad you are enjoying my struggles."
        "Ok.":
            call change_Girl_stat(StormX, "love", -2)
            $ StormX.change_face("bemused", 1)
            if not approval_check(StormX, 800, "OI"):
                call change_Girl_stat(StormX, "love", -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("angry", 2)
                ch_s "Is that really the best you can offer here?"
                $ StormX.blushing = ""
            ch_s "Why do I put up with you?"

    if StormX.event_happened[6] >= 5:

        jump Storm_Love_Badend

    ch_s "I suppose I just need to accept the truth. . ."
    $ StormX.change_face("smile", 1)
    ch_s "I love you, beloved."
    $ StormX.player_petnames.append("lover")
    menu:
        extend ""
        "I love you too!":
            call change_Girl_stat(StormX, "love", 10)
            $ StormX.eyes = "surprised"
            pause .2
            $ StormX.eyes = "normal"
            ch_s "I am glad to hear that."
        "Cool.":
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", -2)
            $ StormX.change_face("confused", 1)
            if not approval_check(StormX, 1200):
                call change_Girl_stat(StormX, "love", -5)
                $ StormX.event_happened[6] += 1
            ch_s "You have nothing more to add than that?"
        "I wouldn't go that far.":
            call change_Girl_stat(StormX, "love", -10)
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", -5)
            $ StormX.event_happened[6] += 2
            $ StormX.change_face("angry", 1, eyes = "side")
            ch_s "No, I suppose you would not."
        "I guess I do too. . .":
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", -2)
            $ StormX.change_face("bemused", 1)
            if not approval_check(StormX, 1200):
                $ StormX.change_face("angry", 1)
                $ StormX.event_happened[6] += 1
            ch_s "Please, do not overwhelm me with your affections. . ."
        "Ok.":
            if not approval_check(StormX, 800, "OI"):
                $ StormX.change_face("angry", 1)
                call change_Girl_stat(StormX, "love", -2)
                $ StormX.event_happened[6] += 1
            ch_s ". . ."

    if StormX.event_happened[6] >= 6:

        jump Storm_Love_Badend

    if len(Player.Harem) >= 2:
        ch_s "I do not expect to keep you for myself. . ."
        $ StormX.change_face("smile", 1, eyes = "side")
        ch_s "The others also love you so much. . ."
        ch_s ". . . but the part of you that entraps me is mine."
    $ StormX.change_face("smile", 1)
    ch_s "I am so glad that I found you, beloved."
    menu:
        extend ""
        "I'm glad I found you too.":
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", 5)
            $ StormX.player_petname = "beloved"
        "I am too, but about that name. . .":
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 7)
            call change_Girl_stat(StormX, "inhibition", 3)
            ch_p "Could you just keep calling me \"[StormX.player_petname]?\""
            ch_s "I suppose that I could. . ."
        "I don't like that name.":
            call change_Girl_stat(StormX, "love", 3)
            call change_Girl_stat(StormX, "obedience", 10)
            call change_Girl_stat(StormX, "inhibition", -2)
            $ StormX.change_face("bemused", 1)
            ch_s "Well, I suppose [StormX.player_petname] does suit you better. . ."
        "Ok.":
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", 2)
            $ StormX.change_face("confused", 1)
            ch_s ". . ."
            if not approval_check(StormX, 900, "L"):
                call change_Girl_stat(StormX, "love", (901-StormX.love))
            $ StormX.change_face("smile", 1, eyes = "side")
            ch_s "Ok."
            $ StormX.player_petname = "beloved"

    return

label Storm_Love_Badend:

    $ StormX.change_face("angry", 1)
    ch_s "You know, I do not think you're ready to have this conversation."
    $ StormX.recent_history.append("angry")
    $ StormX.daily_history.append("angry")
    call remove_Girl(StormX)
    return




label Storm_Sub:
    $ shift_focus (StormX)
    $ StormX.drain_word("asked_to_meet")


    call set_the_scene
    if StormX.location != Player.location and StormX not in Player.Party:
        "[StormX.name] shows up and says she needs to talk to you."
    else:
        "[StormX.name] approaches you, looking to talk."
    call clear_the_room (StormX)
    call set_Character_taboos
    $ StormX.daily_history.append("relationship")

    $ StormX.change_face("sly")
    $ line = 0
    ch_s "[StormX.player_petname]. . . I have noticed that when we are together. . ."
    ch_s ". . . you tend to. . . assert yourself. . ."
    menu:
        extend ""
        "Do I?":
            $ StormX.change_face("confused")
            call change_Girl_stat(StormX, "obedience", -2)
            ch_s "Yes. . ."
        "Yes, I do.":
            call change_Girl_stat(StormX, "obedience", 10)
            call change_Girl_stat(StormX, "inhibition", 3)
            call change_Girl_stat(StormX, "lust", 5)
            ch_s "I am glad you noticed it too. . ."
        "Ok?":
            $ StormX.change_face("confused")
            call change_Girl_stat(StormX, "obedience", -1)
            ch_s ". . ."
            ch_s ". . . yes, well. . ."
    ch_s "I hope that you have also noticed. . ."
    $ StormX.change_face("sly")
    ch_s ". . . what effect it has on me when you do. . ."
    menu:
        extend ""
        "You. . . enjoy it?":
            call change_Girl_stat(StormX, "obedience", 3)
            $ line = ". . . yes, I suppose that I do."
        "Does it turn you on?":
            $ StormX.change_face("bemused", eyes = "side")
            call change_Girl_stat(StormX, "obedience", 2)
            ch_s ". . ."
            call change_Girl_stat(StormX, "obedience", 3)
            call change_Girl_stat(StormX, "inhibition", 5)
            call change_Girl_stat(StormX, "lust", 5)
            $ line = ". . . yes."
        "Sorry?":
            $ StormX.change_face("perplexed", 2)
            call change_Girl_stat(StormX, "obedience", -5)
            call change_Girl_stat(StormX, "inhibition", -5)
            ch_s "Oh, you don't need to-"
            ch_s "That is not what I intended. . ."
        "It makes you wet.":
            $ StormX.change_face("surprised", 2)
            call change_Girl_stat(StormX, "obedience", 3)
            call change_Girl_stat(StormX, "lust", 5)
            call change_Girl_stat(StormX, "lust", 5)
            ch_s ". . ."
            call change_Girl_stat(StormX, "inhibition", 7)
            call change_Girl_stat(StormX, "lust", 5)
            $ StormX.change_face("bemused", 2, eyes = "side")
            $ line = ". . .sometimes. . ."
    while line:
        menu:
            ch_s "[line]"
            "Cool.":
                $ StormX.change_face("perplexed", 1)
                $ line = 0
            "Say it again.":
                $ StormX.change_face("perplexed", eyes = "side")
                ch_s ". . ."
                if "repeat" not in StormX.recent_history:
                    call change_Girl_stat(StormX, "obedience", 5)
                    call change_Girl_stat(StormX, "lust", 5)
                    $ StormX.add_word(1, "repeat", 0, 0, 0)
                    $ StormX.change_face("bemused", 2, eyes = "side")
                else:
                    $ StormX.change_face("bemused")
                    call change_Girl_stat(StormX, "love", 2)
                    call change_Girl_stat(StormX, "obedience", -2)
                    ch_s ". . . I think perhaps that is enough for now. . ."
                    menu:
                        "Ok.":
                            call change_Girl_stat(StormX, "love", 2)
                            call change_Girl_stat(StormX, "obedience", 2)
                        "I'll tell you when it's enough.":
                            $ StormX.change_face("angry", 1)
                            call change_Girl_stat(StormX, "love", -5)
                            call change_Girl_stat(StormX, "obedience", 2)
                            ch_s "Perhaps you are taking things a bit too far."
                        "Fine, for now.":
                            call change_Girl_stat(StormX, "love", 3)
                            call change_Girl_stat(StormX, "obedience", 3)
                            call change_Girl_stat(StormX, "inhibition", 2)
                            ch_s "Thank you."
                    $ line = 0
                    $ StormX.change_face("sly", 1)
            "I'm glad.":
                $ line = 0
                $ StormX.change_face("bemused", 1)
                call change_Girl_stat(StormX, "love", 3)
                call change_Girl_stat(StormX, "inhibition", 2)
            "It turns me on too.":
                $ line = 0
                $ StormX.change_face("sly", 1, mouth = "smile")
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", 3)
                call change_Girl_stat(StormX, "lust", 5)
    ch_s "In any case. . ."
    ch_s "I was hoping that you might continue to. . . assert yourself in future. . ."
    menu:
        extend ""
        "I guess I could. . .":
            $ StormX.change_face("sly", 1)
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "obedience", 2)
        "I could do that.":
            $ StormX.change_face("sly", 1)
            call change_Girl_stat(StormX, "obedience", 5)
        "I'd don't want to.":
            $ StormX.change_face("perplexed", 1)
            call change_Girl_stat(StormX, "love", -5)
            call change_Girl_stat(StormX, "obedience", -5)
            call change_Girl_stat(StormX, "inhibition", -5)
            ch_s "Oh?"
            $ StormX.change_face("sadside", 1)
            call change_Girl_stat(StormX, "obedience", -5)
            ch_s ". . .fine."
            call change_Girl_stat(StormX, "obedience", -10)
            ch_s "Perhaps some other time. . ."
            call remove_Girl(StormX)
            $ StormX.change_face("normal", 1)
            $ StormX.history.append("sir")
            return
        "Of course.":
            $ StormX.change_face("sly", 1)
            call change_Girl_stat(StormX, "obedience", 10)
            call change_Girl_stat(StormX, "inhibition", 5)
        "Ok.":
            $ StormX.change_face("perplexed", 1)
            call change_Girl_stat(StormX, "obedience", -3)
            ch_s ". . . fine."

    ch_s "and perhaps I could refer to you as. . . sir?"
    $ StormX.player_petnames.append("sir")
    menu:
        extend ""
        "If you want?":
            $ StormX.change_face("perplexed", 1, eyes = "side")
            call change_Girl_stat(StormX, "love", 3)
            ch_s ". . . right. . ."
            call change_Girl_stat(StormX, "inhibition", -2)
            ch_s ". . ."
            call change_Girl_stat(StormX, "obedience", -5)
            ch_s "I am unsure you got the correct message here. . ."
            ch_s ". . ."
            $ StormX.change_face("normal", 1)
            ch_s "Whatever. . ."
            $ StormX.player_petname = "sir"
        "You may.":
            $ StormX.change_face("sly", 1)
            $ StormX.player_petname = "sir"
            call change_Girl_stat(StormX, "love", 5)
            call change_Girl_stat(StormX, "obedience", 10)
            call change_Girl_stat(StormX, "inhibition", 5)
        "I'd rather you keep calling me [StormX.player_petname].":
            $ StormX.change_face("sly", 1)
            call change_Girl_stat(StormX, "obedience", 15)
            call change_Girl_stat(StormX, "inhibition", 3)
            ch_s "Very well. . ."
        "I'd rather you call me [Player.name]." if StormX.player_petname != Player.name:
            $ StormX.change_face("sly", 1)
            call change_Girl_stat(StormX, "obedience", 15)
            call change_Girl_stat(StormX, "inhibition", 3)
            ch_s "Very well. . ."
        "Ok.":
            $ StormX.change_face("confused", 1)
            call change_Girl_stat(StormX, "obedience", 5)
            ch_s ". . . right. . ."
            $ StormX.change_face("normal", 1)
            $ StormX.player_petname = "sir"
    ch_s "This should be fun, [StormX.player_petname]. . ."
    return


label Storm_Sub_Asked:
    $ line = 0
    $ StormX.change_face("sadside", 1)
    ch_s "I do recall something like that. . ."
    ch_s "You indicated that you were uninterested. . ."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in StormX.player_petnames and approval_check(StormX, 850, "O"):

                pass
            elif approval_check(StormX, 550, "O"):

                pass
            else:
                ch_s "I have changed my mind. . . at least for the time being. . ."
                $ line = "rude"

            if line != "rude":
                call change_Girl_stat(StormX, "love", 10)
                $ StormX.change_face("sly", 1)
                ch_s "I appreciate that. . ."
                ch_s "Fine, we can give it another try."
        "I get it now.":
            if "sir" in StormX.player_petnames and approval_check(StormX, 850, "O"):

                pass
            elif approval_check(StormX, 550, "O"):

                pass
            else:
                ch_s "Well. . ."
                ch_s "I have changed my mind. . . at least for the time being. . ."
                $ line = "rude"

            if line != "rude":
                call change_Girl_stat(StormX, "obedience", 10)
                ch_s ". . ."
                $ StormX.change_face("sly", 1)
                ch_s "We will see."
        "You know you want it.":
            if "sir" in StormX.player_petnames and approval_check(StormX, 850, "O"):

                pass
            elif approval_check(StormX, 550, "O"):

                pass
            else:
                $ StormX.change_face("sly", 1)
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 5)
                ch_s ". . . ye-"
                $ StormX.change_face("angry", 1, eyes = "side")
                call change_Girl_stat(StormX, "obedience", -3)
                call change_Girl_stat(StormX, "inhibition", 5)
                ch_s "-no. . ."
                ch_s "I have changed my mind. . . at least for the time being. . ."
                $ line = "rude"

            if line != "rude":
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "inhibition", 5)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s ". . ."
                $ StormX.change_face("sly", 1)
                ch_s ". . . yes. I do want it."

    $ StormX.recent_history.append("asked sub")
    $ StormX.daily_history.append("asked sub")
    if line == "rude":
        call remove_Girl(StormX)
        $ StormX.recent_history.append("angry")
        $ renpy.pop_call()
        "[StormX.name] marches out the door, leaving you alone. She looked pretty upset."
    elif "sir" in StormX.player_petnames:

        call change_Girl_stat(StormX, "obedience", 30)
        $ StormX.player_petnames.append("master")
        $ StormX.player_petname = "master"
        $ StormX.eyes = "squint"
        ch_s ". . . master. . ."
    else:

        call change_Girl_stat(StormX, "obedience", 30)
        $ StormX.player_petnames.append("sir")
        $ StormX.player_petname = "sir"
        $ StormX.eyes = "squint"
        ch_s ". . . sir."
    return






label Storm_Master:
    $ StormX.drain_word("asked_to_meet")
    $ shift_focus (StormX)

    call set_the_scene
    if StormX.location != Player.location and StormX not in Player.Party:
        "[StormX.name] shows up and says she needs to talk to you."
    else:
        "[StormX.name] approaches you, looking to talk."
    call clear_the_room (StormX)
    $ StormX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ Options = all_Girls[:]
    while Options:

        if "master" == Options[0].player_petname:
            $ line = 2
        elif "master" in Options[0].player_petnames:
            $ line = 1 if not line else line
        $ Options.remove(Options[0])
    $ StormX.change_face("bemused", 1)
    if line:

        ch_s "I have heard some talk among the other girls. . ."
        if line == 2:

            ch_s "Apparently you have been having some of them calling you. . . "
            $ StormX.change_face("sly", 1)
            ch_s "\"Master?\""
        else:

            ch_s "Apparently some have considered calling you. . . "
            $ StormX.change_face("sly", 1)
            ch_s "\"Master?\""
    else:

        ch_s "I have been thinking lately. . ."
        ch_s "Do you enjoy. . . dominating those around you?"
        ch_s "Do you enjoy hearing a woman call you. . ."
        $ StormX.change_face("sly", 1)
        ch_s "\"Master?\""
    menu:
        extend ""
        "I don't know, it can be fun.":
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s ". . ."
            $ StormX.change_face("bemused", 1)
            ch_s "I can imagine. . ."
        "I don't really encourage it.":
            $ StormX.change_face("confused", 1)
            call change_Girl_stat(StormX, "obedience", -2)
            call change_Girl_stat(StormX, "inhibition", -2)
            if line == 2:
                ch_s "Really? . ."
                $ StormX.change_face("sly", 1)
                call change_Girl_stat(StormX, "love", -5)
                ch_s "That is not what I have heard. . ."
            else:
                ch_s "Hmmm. . . that is not the answer I was expecting. . ."
        "Yes. I like it.":

            $ StormX.change_face("sly", 1)
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", 3)
            ch_s "I expected that you might. . ."
        "What about you?":
            $ StormX.change_face("sly", 1, eyes = "side")
            call change_Girl_stat(StormX, "love", 1)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 3)
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s "I do not know. . ."
            $ StormX.add_word(1, "aboutyou", 0, 0, 0)
        "Nope.":
            $ StormX.change_face("confused", 1)
            call change_Girl_stat(StormX, "obedience", -5)
            call change_Girl_stat(StormX, "inhibition", -2)
            if line:
                call change_Girl_stat(StormX, "love", -5)
                ch_s "You don't need to hide such things from me. . ."
            else:
                ch_s "Hmmm. . . that is not the answer I was expecting. . ."


    menu:
        extend ""
        "So you -would- enjoy it.":
            $ StormX.change_face("bemused", 1)
            call change_Girl_stat(StormX, "love", 3)
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", 3)
            call change_Girl_stat(StormX, "inhibition", 2)
        "Would you enjoy that?" if "aboutyou" not in StormX.recent_history:
            $ StormX.change_face("sly", 1, eyes = "side")
            call change_Girl_stat(StormX, "love", 1)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 3)
            call change_Girl_stat(StormX, "inhibition", 2)
            ch_s "I do not know. . ."
        "You wouldn't enjoy it, would you?":
            $ StormX.change_face("surprised", 1)
            call change_Girl_stat(StormX, "love", -2)
            call change_Girl_stat(StormX, "obedience", -2)
            ch_s "Oh, you wound me. . ."
            $ StormX.change_face("sly", 1, eyes = "side")
            ch_s "Perhaps you assume too much. . ."
        "You want to call me \"Master,\" don't you.":
            $ StormX.change_face("sly", 1, eyes = "side")
            call change_Girl_stat(StormX, "obedience", 5)
            call change_Girl_stat(StormX, "inhibition", 2)
            call change_Girl_stat(StormX, "lust", 5)
            ch_s "Well. . ."
        "Yeah?":
            $ StormX.change_face("sly", 1, eyes = "side")
            call change_Girl_stat(StormX, "love", -3)
            call change_Girl_stat(StormX, "obedience", -3)
            ch_s "Hmm. . ."
            ch_s "Perhaps you should ask me. . ."
    $ StormX.change_face("sly", 1)
    ch_s "I might. . ."
    $ line = 1
    while line:
        menu:
            extend ""
            "Call me \"Master.\"" if "master" not in StormX.player_petnames:
                $ StormX.change_face("surprised", 2)
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "Oh. . ."
                $ StormX.change_face("sly", 1)
                call change_Girl_stat(StormX, "obedience", 5)
                ch_s "I can do that. . ."
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "inhibition", 3)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "Master."
                $ StormX.player_petnames.append("master")
            "What do you want to call me?" if "master" not in StormX.player_petnames:
                $ StormX.change_face("sly", 1, eyes = "side")
                call change_Girl_stat(StormX, "love", 3)
                call change_Girl_stat(StormX, "obedience", 7)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "Hmmm. . ."
                call change_Girl_stat(StormX, "obedience", 3)
                ch_s "I was considering calling you. . ."
                $ StormX.change_face("sly", 1)
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "inhibition", 5)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s ". . . Master."
                $ StormX.player_petnames.append("master")
            "Say it." if "master" not in StormX.player_petnames:
                call change_Girl_stat(StormX, "obedience", 12)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s ". . ."
                $ StormX.change_face("sly", 1, eyes = "side")
                call change_Girl_stat(StormX, "obedience", 7)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s ". . ."
                $ StormX.change_face("sly", 1)
                call change_Girl_stat(StormX, "obedience", 10)
                call change_Girl_stat(StormX, "inhibition", 3)
                call change_Girl_stat(StormX, "lust", 5)
                ch_s "Master."
                $ StormX.player_petnames.append("master")
            "Say it again." if "master" in StormX.player_petnames and line < 3:
                if line < 2:
                    call change_Girl_stat(StormX, "obedience", 2)
                    call change_Girl_stat(StormX, "inhibition", 2)
                    $ StormX.change_face("sly", 2, eyes = "side")
                    ch_s ". . ."
                    call change_Girl_stat(StormX, "lust", 5)
                else:
                    $ StormX.change_face("smile", 1)
                    call change_Girl_stat(StormX, "love", 3)
                    call change_Girl_stat(StormX, "inhibition", 3)
                    ch_s "Alright, that is perhaps a bit much. . ."
                $ StormX.change_face("sly", 2, eyes = "side")
                ch_s "Master."
                $ line += 1
            "Yes, call me that from now on." if "master" in StormX.player_petnames:
                $ StormX.change_face("sly", 1)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", 2)
                ch_s "Of course. . . Master"
                $ StormX.player_petname = "master"
                $ line = 0
            "But I'd prefer you stick to [StormX.player_petname]." if "master" in StormX.player_petnames:
                $ StormX.change_face("sad", 1)
                call change_Girl_stat(StormX, "love", 3)
                call change_Girl_stat(StormX, "obedience", 3)
                ch_s "I suppose that I can. . . [StormX.player_petname]"
                $ line = 0
            "I don't know if I would be comfortable with that. . ." if "context" not in StormX.recent_history and "master" not in StormX.player_petnames:
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "obedience", -3)
                call change_Girl_stat(StormX, "inhibition", -2)
                $ line = "context"
            "I can't ask you to call me that." if "context" not in StormX.recent_history and "master" not in StormX.player_petnames:
                call change_Girl_stat(StormX, "obedience", -5)
                call change_Girl_stat(StormX, "inhibition", -3)
                $ line = "context"
            "I still would rather not have you call me that." if "context" in StormX.recent_history and "master" not in StormX.player_petnames:
                $ StormX.change_face("sad", 1, mouth = "smile")
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "obedience", 5)
                ch_s "I can understand that."
                $ StormX.change_face("smile", 1)
                ch_s "Consider it forgotten."
                ch_s ". . ."
                $ StormX.change_face("sly", 1)
                ch_s "Though if you change your mind. . ."
                $ line = 0


        if line == "context":

            $ StormX.change_face("surprised", 2)
            ch_s "Oh."
            $ StormX.change_face("sad", 1)
            ch_s "I am of course aware that there is some. . ."
            $ StormX.change_face("sadside", 1)
            ch_s ". . . historical baggage associated with that term."
            ch_s "I cannot say that I am entirely immune to the concept. . ."
            ch_s "But I do not think that it would bother me."
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            call change_Girl_stat(StormX, "lust", 2)
            ch_s ". . . if it were you. . ."
            $ StormX.change_face("sly", 1)
            $ StormX.add_word(1, "context", 0, 0, 0)
            $ line = 1

    $ StormX.change_face("sly", 1)
    $ StormX.history.append("master")
    $ line = 0
    return






label Storm_Sexfriend:
    "You get a text from [StormX.name]."
    "Drop by the pool tonight. . ."
    $ Player.add_word(1, 0, 0, 0, "poolnight")
    $ StormX.daily_history.append("relationship")
    $ StormX.event_happened[9] = 1
    return


label Storm_Poolnight:
    $ shift_focus (StormX)
    call set_the_scene
    call clear_the_room (StormX, 1, 1)
    $ StormX.location = "bg_pool"
    call ShowPool ([StormX])
    $ taboo = 0
    $ StormX.taboo = 0
    $ StormX.change_face("sly", 1)
    $ StormX.undress()
    $ StormX.recent_history.append("poolnight")
    if "sexfriend" not in StormX.player_petnames:
        call show_Girl(StormX, x_position = 0.5, y_position = 0.6, sprite_layer = 1, color_transform = night, transition = easebottom)

        "As you enter the pool area, it seems fairly empty, aside from a small ripple across the pool's surface."

        call show_Girl(StormX, y_position = 0.4, color_transform = night, transition = ease)

        pause 1.0

        show Storm_sprite standing zorder 1 at sprite_location(StormX.sprite_location, 0.4), night, swimming(0.5)

        "Storm rises from the pool."
        ch_s "Ah, I was hoping you would join me, [StormX.player_petname]. . ."
        if StormX not in Player.Harem and StormX.player_petname not in ("sir", "master"):
            ch_s "I know that this is a no-strings attached situation. . ."
            ch_s "That is fine with me."
            call change_Girl_stat(StormX, "inhibition", 25)
            ch_s "We can just continue on as. . . sex friends. . ."
            $ StormX.player_petnames.append("sex friend")
    else:
        ch_s "Oh, hello there, [StormX.player_petname]."
    ch_s "Care to join me?"
    menu:
        extend ""
        "Sure":
            call change_Girl_stat(StormX, "love", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            "You join her in the pool and swim about for a bit."
            call change_Girl_stat(StormX, "lust", 3)
            "You weave closer and closer to each other. . ."
            $ round -= 10 if round >= 10 else round
            "Finally, she pulls you close and whispers in your ear. . ."
            call change_Girl_stat(StormX, "lust", 5)
            ch_s "Would you like to get out of the water, and get me soaking wet?"
            "You both climb out of the pool to the sidelines."
        "Couldn't you just come to me?":
            call change_Girl_stat(StormX, "obedience", 1)
            call change_Girl_stat(StormX, "obedience", 2)
            call change_Girl_stat(StormX, "inhibition", 2)
            call change_Girl_stat(StormX, "lust", 3)
            ch_s "I could manage that. . ."
            "She climbs out of the pool."
        "Maybe later. [[leave]":
            $ StormX.change_face("sad", 1)
            call change_Girl_stat(StormX, "obedience", 3)
            ch_s "Oh, that is a pity. . ."
            ch_s "Have fun then. . ."
            "You head back to your room."
            $ Player.location = "bg_player"
            jump reset_location
    hide Storm_sprite
    call set_the_scene
    $ StormX.change_face("sly", 1, eyes = "leftside")
    ch_s "Now that you have me, [StormX.player_petname]. . ."
    $ StormX.change_face("sly", 1)
    ch_s "What do you intend to do with me. . ."
    call enter_main_sex_menu(StormX)

    return







label Storm_Fuckbuddy:
    $ StormX.daily_history.append("relationship")
    $ StormX.location = "bg_classroom"
    $ Player.location = "bg_classroom"
    call clear_the_room (StormX, 1, 1)
    call set_the_scene
    $ Player.traits.append("locked")
    $ Nearby = []
    call set_Character_taboos
    $ StormX.change_face("sly", 1, eyes = "side")
    call change_Girl_stat(StormX, "inhibition", 5)
    "After class, [StormX.name] walks past you, and places a hand on your chest as you head out."
    call change_Girl_stat(StormX, "inhibition", 5)
    "She leans back and locks the door."
    $ StormX.change_face("sly", 1, eyes = "down")
    call change_Girl_stat(StormX, "inhibition", 10)
    ch_s "I do have needs, you know."
    $ StormX.player_petnames.append("fuck buddy")
    $ StormX.event_happened[10] += 1
    $ StormX.change_face("sly", 1)
    call change_Girl_stat(StormX, "inhibition", 10)
    ch_s "Couldn't you help me with that? . . "
    call enter_main_sex_menu(StormX)

    return




label Storm_Daddy:
    $ StormX.daily_history.append("relationship")
    $ shift_focus (StormX)
    call set_the_scene
    ch_s ". . ."
    $ line = 0
    $ Options = all_Girls[:]
    while Options:

        if "daddy" == Options[0].player_petname:
            $ line = 2
        elif "daddy" in Options[0].player_petnames:
            $ line = 1 if not line else line
        $ Options.remove(Options[0])


    if StormX in Player.Harem:
        ch_s "I have been talking with the other girls. . ."
    else:
        ch_s "I have heard something among the students. . ."
    if line:
        ch_s "Apparently you have some of them call you. . . \"daddy?\""
    else:
        ch_s "Apparently sometimes the woman in a relationship. . ."
        ch_s ". . . calls her partner. . . \"daddy?\""
    menu:
        extend ""
        "Yes?":
            ch_s "I thought as much. . ."
        "I don't know what you're talking about.":
            ch_s "I think it is just a term of endearment. . ."
            ch_s "Affectionate, but. . . submissive?"
        "Not really.":
            ch_s "Oh. Perhaps I misunderstood."
    $ line = 1
    $ StormX.player_petnames.append("daddy")
    while line:
        menu:
            extend ""
            "Did you want me to call you that?" if "callyouthat" not in StormX.recent_history:
                call change_Girl_stat(StormX, "love", 1)
                call change_Girl_stat(StormX, "inhibition", 2)
                ch_s ". . ."
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "inhibition", 1)
                ch_s "I suppose that I did. . ."
                $ StormX.recent_history.append("callyouthat")
            "I guess you could. . ." if "callyouthat" in StormX.recent_history or "whycare" in StormX.recent_history:
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", 1)
                ch_s ". . ."
                call change_Girl_stat(StormX, "love", 5)
                call change_Girl_stat(StormX, "inhibition", 3)
                ch_s "Certainly. . . Daddy."
                $ line = 0
            "Call me \"Daddy.\"":
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "obedience", 3)
                ch_s ". . ."
                call change_Girl_stat(StormX, "obedience", 5)
                call change_Girl_stat(StormX, "inhibition", 2)
                call change_Girl_stat(StormX, "lust", 3)
                ch_s "Certainly. . . Daddy."
                $ line = 0
            "Why do you care?" if "whycare" not in StormX.recent_history:
                call change_Girl_stat(StormX, "love", 2)
                call change_Girl_stat(StormX, "obedience", -1)
                call change_Girl_stat(StormX, "inhibition", -1)
                ch_s "Oh, well, I was thinking that I could. . ."
                $ StormX.recent_history.append("whycare")
            "It's weird, right?":
                call change_Girl_stat(StormX, "love", -3)
                call change_Girl_stat(StormX, "obedience", -5)
                call change_Girl_stat(StormX, "inhibition", -15)
                ch_s "Oh. . . "
                ch_s ". . . I suppose that it is."
                ch_s "Never mind. . ."
                call remove_Girl(StormX)
                $ line = 0
            "I'd rather not." if "callyouthat" in StormX.recent_history or "whycare" in StormX.recent_history:
                call change_Girl_stat(StormX, "love", -2)
                call change_Girl_stat(StormX, "obedience", 3)
                call change_Girl_stat(StormX, "inhibition", -5)
                ch_s "Oh. . . "
                ch_s ". . . I suppose that it fine."
                ch_s "Never mind. . ."
                call remove_Girl(StormX)
                $ line = 0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
