



label Jean_Key:
    call set_the_scene
    $ JeanX.change_face("bemused")
    ch_j "Oh, here, just in case you wanted to drop by."
    "She tossed a key at you, which you manage to catch."
    $ Player.Keys.append(JeanX)
    $ JeanX.event_happened[0] = 1
    ch_p "Thanks."
    return




label Jean_Like:

    if JeanX.location != Player.location:
        "[JeanX.name] walks up to you."

    call clear_the_room(JeanX)

    $ JeanX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ JeanX.change_face("sly", 1, eyes = "down")
    ". . .{w=0.5}{nw}"
    $ JeanX.change_face("sly", 1)
    "She looks at you appraisingly."

    ch_j "You know. . . you're more fun to hang out with than I expected."
    $ line = "Y"
    if JeanX.permanent_History["massage"] >= 5:
        call change_Girl_stat(JeanX, "lust", 5)
        ch_j "You give really good massages. . ."
        $ line = "and Y"
    if JeanX.permanent_History["orgasmed"]>= 10:
        $ JeanX.change_face("sly", 1)
        call change_Girl_stat(JeanX, "lust", 5)
        ch_j "[line]ou -really- know how to finish them. . ."
        $ line = "and Y"
        if JeanX.permanent_History["orgasmed"]>= 30:
            call change_Girl_stat(JeanX, "lust", 10)
            ch_j ". . . seriously. . ."
    if JeanX.seen_peen:
        $ JeanX.change_face("sly", 1)
        call change_Girl_stat(JeanX, "love", 5)
        call change_Girl_stat(JeanX, "obedience", 10)
        call change_Girl_stat(JeanX, "inhibition", 5)
        call change_Girl_stat(JeanX, "lust", 5)
        ch_j "[line]ou're certainly well hung too. . ."
    $ line = 0

    ch_j "I really couldn't have a better little sex toy."
    menu:
        extend ""
        "I love it too.":
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "love", 10)
            call change_Girl_stat(JeanX, "obedience", 5)
            call change_Girl_stat(JeanX, "inhibition", 5)
            ch_j "Good boy. . ."
            ch_j "Keep this up and I might \"reward\" you more often."
        "What if I want something more?":
            $ JeanX.brows = "confused"
            call change_Girl_stat(JeanX, "obedience", 10)
            ch_j "Oh?"
            $ line = "more"
        "I'm not your toy.":
            $ JeanX.brows = "confused"
            call change_Girl_stat(JeanX, "obedience", 15)
            ch_j "Huh?"

    $ JeanX.history.append("sexfriend")
    if line == "more":
        $ JeanX.brows = "confused"
        ch_j "What more could you want?"
        menu:
            extend ""
            "Could you be my girlfriend?":
                $ JeanX.change_face("surprised", 2)
                call change_Girl_stat(JeanX, "love", 5)
                call change_Girl_stat(JeanX, "obedience", -5)
                ch_j "Ha! Girlfriend. . ."
                $ JeanX.change_face("bemused", 1, eyes = "side")
                ch_j "That's just precious!"

                $ JeanX.change_face("sly", 1)
                if JeanX.permanent_History["orgasmed"]>= 10:
                    ch_j "Look, you're pretty hot and all, and you can get it. . ."
                else:
                    ch_j "Look, you're pretty hot and all. . ."
                ch_j "but I just don't see you as \"relationship\" material. . ."
            "Couldn't we be sex friends?":

                $ JeanX.change_face("bemused", 1, eyes = "side")
                call change_Girl_stat(JeanX, "love", 5)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "inhibition", 5)
                call change_Girl_stat(JeanX, "inhibition", 5)
                call change_Girl_stat(JeanX, "lust", 10)
                ch_j "Hmm. . ."
                ch_j "Friends with. . . benefits? . ."
                $ JeanX.change_face("bemused", 1)
                ch_j "I guess we could do that. . ."
                $ line = 0
            "Nothing, I guess. . .":
                $ JeanX.change_face("bemused", 1)
                call change_Girl_stat(JeanX, "love", 5)
                ch_j "Exactly."
                $ line = 0
    if line:
        menu:
            extend ""
            "So what could I do to change your mind?":
                $ JeanX.change_face("surprised", 1)
                call change_Girl_stat(JeanX, "obedience", -10)
                ch_j "How should I know?!"
                $ JeanX.change_face("bemused", 1, eyes = "side")
                ch_j "I guess give me some reason to respect you or something?"
                $ JeanX.change_face("sly", 1)
                ch_j "I mean, fucking around, that's fine, but let's keep this casual."
            "I guess that's fine.":
                $ JeanX.change_face("sly", 1)
                call change_Girl_stat(JeanX, "love", 5)
                call change_Girl_stat(JeanX, "obedience", -5)
                call change_Girl_stat(JeanX, "inhibition", 5)
                ch_j "Glad we got that settled."
            "Bitch.":
                $ JeanX.change_face("sly", 1)
                call change_Girl_stat(JeanX, "obedience", 5)
                call change_Girl_stat(JeanX, "inhibition", 10)
                call change_Girl_stat(JeanX, "lust", 2)
                ch_j "Yeah, I know."
    $ JeanX.player_petname = "sexfriend"
    $ JeanX.player_petnames.append("sexfriend")
    return

label Jean_Love:

    if JeanX.location != Player.location:
        "[JeanX.name] walks up to you."

    call clear_the_room(JeanX)

    $ JeanX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ JeanX.change_face("sly", 1)
    ch_j "So. . . [JeanX.player_petname]."
    ch_j "This has been going on a while, you and I."
    ch_j "I think my respect for you has grown a lot."
    if JeanX.SEXP >= 30:
        call change_Girl_stat(JeanX, "lust", 5)
        ch_j "I mean, you really know how to lay it down."
    if JeanX.obedience < 900:
        $ JeanX.change_face("sly", 1, eyes = "side")
        call change_Girl_stat(JeanX, "love", 5)
        ch_j "And you're so sweet to me. . ."
    ch_j "I kinda feel like. . ."
    $ line = 0
    menu:
        extend ""
        "I love you.":
            $ line = "love"
            $ JeanX.change_face("sly", 2)
            ch_j "I lo-"
            $ JeanX.change_face("surprised", 2)
            call change_Girl_stat(JeanX, "love", 10)
            call change_Girl_stat(JeanX, "love", 10)
            call change_Girl_stat(JeanX, "obedience", 10)
            ch_j ". . ."
            call change_Girl_stat(JeanX, "inhibition", 5)
            ch_j "That's what I was going to say!"
        ". . .":
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "obedience", 5)
            ch_j "I. . ."
        "You love me.":
            $ JeanX.change_face("surprised", 2)
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "obedience", 5)
            ch_j ". . ."
            call change_Girl_stat(JeanX, "inhibition", 5)
            ch_j "Well. . . yeah."
    $ JeanX.change_face("sly", 1)
    ch_j "I love you. . ."
    if line != "love":
        menu JeanLove_Menu:
            extend ""
            "I love you too.":
                call change_Girl_stat(JeanX, "love", 5)
                call change_Girl_stat(JeanX, "love", 10)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "inhibition", 5)
                $ JeanX.change_face("smile", 1)
                ch_j "Great!"
            ". . ." if not line:
                $ line = "repeat"
                $ JeanX.change_face("sad", 2)
                call change_Girl_stat(JeanX, "love", -5)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "inhibition", -5)
                ch_j "Well, say something. . ."
                jump JeanLove_Menu
            "Cool." if line != "cool":
                $ line = "cool"
                $ JeanX.change_face("angry", 1)
                call change_Girl_stat(JeanX, "love", -5)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "inhibition", -5)
                ch_j "I feel like maybe you aren't taking this seriously."
                jump JeanLove_Menu
            "Sorry, I mean \"that's cool.\"" if line == "cool":
                ch_j ". . ."
                call change_Girl_stat(JeanX, "love", -3)
                call change_Girl_stat(JeanX, "inhibition", -3)
                ch_j "That still doesn't seem. . ."
                call change_Girl_stat(JeanX, "love", 5)
                ch_j "Adequate. . ."
            "I don't feel the same way.":
                $ JeanX.change_face("surprised", 2)
                call change_Girl_stat(JeanX, "love", -5)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "obedience", 5)
                call change_Girl_stat(JeanX, "inhibition", -5)
                ch_j "Oh. . ."
                $ JeanX.change_face("sadside", 1)
                ch_j "I guess that's fine."
                ch_j "Whatever."
    ch_j "Anyway, I just wanted to put that out there."
    $ JeanX.event_happened[5] = 1
    $ JeanX.player_petname = "lover"
    $ JeanX.player_petnames.append("lover")
    if Player.Harem:
        ch_j "I figured if you wanted me to join your little lady-party, I'm in."
    else:
        ch_j "I figured maybe we could make it official, I could be your girlfriend. . ."
    menu:
        extend ""
        "Sure, the more the merrier." if Player.Harem:
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "inhibition", 5)
            $ Player.Harem.append(JeanX)
        "Sure, I'd love to." if not Player.Harem:
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "inhibition", 5)
            $ Player.Harem.append(JeanX)
        "I'm not interested.":
            $ JeanX.change_face("surprised", 2)
            call change_Girl_stat(JeanX, "love", -5)
            call change_Girl_stat(JeanX, "obedience", 5)
            call change_Girl_stat(JeanX, "inhibition", -5)
            ch_j "What?"
            $ JeanX.change_face("angry", 2)
            ch_j "Why not?!"
            if len(Player.Harem) >= 2:
                ch_j "Is it because of the others?"
            elif Player.Harem:
                ch_j "Is it because of [Player.Harem[0].name]?"
            menu:
                extend ""
                "Yeah" if Player.Harem:
                    $ JeanX.change_face("angry", 1, eyes = "side")
                    call change_Harem_stat (JeanX, 700, -5)
                    if len(Player.Harem) >= 2:
                        ch_j "Bitches."
                    elif Player.Harem:
                        ch_j "That bitch."
                "I just don't like you like that.":
                    $ JeanX.change_face("sad", 2, eyes = "surprised")
                    call change_Girl_stat(JeanX, "love", -5)
                    call change_Girl_stat(JeanX, "love", -5)
                    call change_Girl_stat(JeanX, "obedience", 5)
                    call change_Girl_stat(JeanX, "obedience", 10)
                    call change_Girl_stat(JeanX, "inhibition", -5)
                    ch_j "Oh."
                    $ JeanX.change_face("sadside", 1)
                    ch_j "."
                    ch_j ". ."
                    ch_j ". . ."
            $ JeanX.change_face("smile", 1, brows = "angry")
            ch_j "Well, you'll come around."
            ch_j "You don't find a catch like this every day."


    if JeanX in Player.Harem:
        $ JeanX.change_face("sly", 1)
        ch_j "Good."
        if len(Player.Harem) >= 2:

            if len(Player.Harem) >= 3:
                ch_j "And you don't think the others would mind?"
                $ line = "they're"
            else:
                ch_j "And you don't think [Player.Harem[0].name] would mind?"
                $ line = "she's"
            menu:
                extend ""
                "No, actually [line] fine with it." if "JeanYes" in Player.traits:
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "obedience", 10)
                    call change_Girl_stat(JeanX, "inhibition", 5)
                    $ JeanX.change_face("surprised", 1)
                    ch_j "Oh, good."
                "Actually. . . I guess we'll need to work on that one." if "JeanYes" not in Player.traits:
                    call change_Girl_stat(JeanX, "inhibition", 5)
                    call change_Girl_stat(JeanX, "lust", 3)
                    $ JeanX.change_face("confused", 1)
                    ch_j "I think I could bring them around. . ."
                    menu:
                        extend ""
                        "No! Don't do that!":
                            $ JeanX.change_face("sly", 1)
                            call change_Girl_stat(JeanX, "obedience", 5)
                            ch_j "Right."
                            ch_j ". . ."
                            call change_Girl_stat(JeanX, "inhibition", 5)
                            call change_Girl_stat(JeanX, "lust", 2)
                            ch_j "-wink-"
                            menu:
                                extend ""
                                "No! No \"wink!\"":
                                    $ JeanX.change_face("sly", 1, eyes = "stunned")
                                    call change_Girl_stat(JeanX, "obedience", 5)
                                    call change_Girl_stat(JeanX, "obedience", 3)
                                    pause 0.3
                                    $ JeanX.change_face("sly", 1)
                                    ch_j "Oh, FINE."
                                    ch_j "You sort things out on your end and get back to me."
                                    ch_j ". . . just don't take -too- long."
                                    $ Player.Harem.remove(JeanX)
                                    $ JeanX.event_happened[5] = 20
                                    return
                                "[[Might as well roll with it. . .]":
                                    ch_j "Heh."
                        "That would probably be a good idea. . .":
                            call change_Girl_stat(JeanX, "love", 3)
                            call change_Girl_stat(JeanX, "obedience", 3)
                            call change_Girl_stat(JeanX, "inhibition", 1)
                            $ JeanX.change_face("sly", 0)
                            ch_j "Right. On it."
        $ JeanX.player_petnames.append("boyfriend")

    $ line = 0
    return



label Jean_Sub:

    if JeanX.location != Player.location:
        "[JeanX.name] walks up to you."

    call clear_the_room(JeanX)

    $ JeanX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ JeanX.change_face("sly", 1, eyes = "side")
    ch_j "Hey. . . [JeanX.player_petname]."
    $ JeanX.eyes = "squint"
    ch_j "We need to talk."
    $ JeanX.change_face("sadside", 1)
    ch_j ". . ."
    ch_j "When we first met. . . I was pretty rude."
    ch_j "I get that."
    $ JeanX.change_face("sly", 1, eyes = "leftside")
    ch_j "When you're practically perfect in every way, you can look down your lessers."
    $ JeanX.change_face("angry", 1, eyes = "leftside")
    ch_j ". . ."
    ch_j "Maybe that came out wrong."
    $ JeanX.change_face("sly", 1)
    ch_j "What I mean is, you've really shown me something lately."
    ch_j "You know how to push my buttons. . ."
    ch_j "-get me to do things I never expected. . ."
    ch_j ". . . -feel- things I never expected. . ."
    menu:
        extend ""
        "So what do you want from me?":
            call change_Girl_stat(JeanX, "love", -3)
            call change_Girl_stat(JeanX, "obedience", -3)
            call change_Girl_stat(JeanX, "inhibition", 2)
            ch_j "Well. . . I didn't want to spell it out. . ."
        "You know it.":
            call change_Girl_stat(JeanX, "obedience", 3)
            ch_j ". . ."
        "Oh? That's nice!":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "obedience", -3)
            ch_j "Um, I think you're missing my point. . ."

    $ JeanX.history.append("sir")
    menu:
        extend ""
        "Tell me what you want.":
            $ JeanX.change_face("sly", 1, eyes = "side")
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 2)
            ch_j "Well. . . just that. . ."
            call change_Girl_stat(JeanX, "obedience", 2)
            call change_Girl_stat(JeanX, "inhibition", 1)
            call change_Girl_stat(JeanX, "lust", 5)
            ch_j "Could you. . ."
            call change_Girl_stat(JeanX, "obedience", 2)
            call change_Girl_stat(JeanX, "inhibition", 2)
            call change_Girl_stat(JeanX, "lust", 5)
            ch_j "boss me around a little more?"
        "Call me your \"Master.\"":
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "inhibition", 5)
            call change_Girl_stat(JeanX, "lust", 10)
            $ JeanX.change_face("surprised", 2)
            ch_j "!!!"
            $ JeanX.change_face("sly", 1, eyes = "side")
            call change_Girl_stat(JeanX, "obedience", -5)
            ch_j "Well. . . I don't know about that!"
            ch_j "I mean. . . I could -maybe- call you. . ."
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "obedience", 5)
            call change_Girl_stat(JeanX, "lust", 5)
            ch_j "Sir?"
        "Ok?":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "love", 3)
            ch_j ". . ."
            ch_j "You still seem kinda lost here. . ."
            ch_j "Maybe I'm still not being clear, but. . ."
            $ JeanX.change_face("angry", 1, eyes = "side")
            call change_Girl_stat(JeanX, "obedience", -3)
            ch_j "If I have to spell it out for you, then maybe it's not worth it."
            menu:
                extend ""
                "You want me to tell you what to do.":
                    call change_Girl_stat(JeanX, "love", 3)
                    call change_Girl_stat(JeanX, "obedience", 5)
                    call change_Girl_stat(JeanX, "inhibition", 2)
                    ch_j ". . ."
                    $ JeanX.change_face("sly", 1)
                    call change_Girl_stat(JeanX, "obedience", 3)
                    call change_Girl_stat(JeanX, "lust", 3)
                    ch_j "Yes. . ."
                    menu:
                        extend ""
                        "So what will you call me?":
                            $ JeanX.eyes = "side"
                            ch_j "How about. . ."
                            $ JeanX.change_face("sly", 1)
                            call change_Girl_stat(JeanX, "love", 5)
                            call change_Girl_stat(JeanX, "obedience", 10)
                            call change_Girl_stat(JeanX, "inhibition", 3)
                            call change_Girl_stat(JeanX, "lust", 3)
                            ch_j "\"Sir?\""
                        ". . .":
                            ch_j "How about I call you. . ."
                            call change_Girl_stat(JeanX, "obedience", 10)
                            call change_Girl_stat(JeanX, "inhibition", 10)
                            call change_Girl_stat(JeanX, "lust", 3)
                            ch_j "\"Sir?\""
                        "Call me \"sir.\"":
                            call change_Girl_stat(JeanX, "love", 10)
                            call change_Girl_stat(JeanX, "obedience", 15)
                            call change_Girl_stat(JeanX, "lust", 10)
                            ch_j ". . ."
                            call change_Girl_stat(JeanX, "obedience", 5)
                            ch_j "Yes. . . sir."
                "Yeah, I guess. . .":


                    call change_Girl_stat(JeanX, "love", -5)
                    call change_Girl_stat(JeanX, "obedience", -10)
                    call change_Girl_stat(JeanX, "inhibition", -10)
                    ch_j "Hmm. . . maybe so. . ."
                    return

    $ JeanX.player_petname = "sir"
    $ JeanX.player_petnames.append("sir")
    $ JeanX.recent_history.append("asked sub")
    $ JeanX.daily_history.append("asked sub")
    return








label Jean_Master:
    if JeanX.location != Player.location:
        "[JeanX.name] walks up to you."

    call clear_the_room(JeanX)

    $ JeanX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ JeanX.change_face("sly", 1, eyes = "side")
    ch_j "Hey. . . [JeanX.player_petname]."
    ch_j "Would you. . . want me to call you. . ."
    ch_j "\"Master?\""
    $ JeanX.history.append("master")
    menu:
        "Yeah, do that.":
            $ JeanX.change_face("sly", 1, eyes = "side")
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 5)
            ch_j "Well. . . Ok then."
            $ JeanX.player_petname = "master"
        "What? Why?":
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "obedience", 5)
            call change_Girl_stat(JeanX, "inhibition", 10)
            call change_Girl_stat(JeanX, "lust", 5)
            ch_j "Because it's -hot!-"
            ch_j "Duh."
        ". . .":
            call change_Girl_stat(JeanX, "love", -3)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "inhibition", -2)
            ch_j "Well. . ."
            ch_j ". . ."
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "inhibition", 10)
            call change_Girl_stat(JeanX, "inhibition", 5)
            ch_j "I'm going to anyway."
        "Not really.":
            call change_Girl_stat(JeanX, "love", -3)
            call change_Girl_stat(JeanX, "obedience", 3)
            call change_Girl_stat(JeanX, "inhibition", -5)
            ch_j "Oh. . ."
            ch_j "Well, ok. . ."
            return
    call change_Girl_stat(JeanX, "obedience", 5)
    call change_Girl_stat(JeanX, "inhibition", 5)
    call change_Girl_stat(JeanX, "lust", 5)
    $ JeanX.player_petnames.append("master")
    $ JeanX.change_face("sly", 1)
    ch_j "Master."
    menu:
        "Well. . . ok then.":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "inhibition", -1)
            ch_j ". . . good?"
        "I don't think you understand how this works.":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "love", -2)
            call change_Girl_stat(JeanX, "obedience", 1)
            ch_j "I don't follow."
            menu:
                "Never mind.":
                    $ JeanX.change_face("sly", 1)
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "obedience", 5)
                    call change_Girl_stat(JeanX, "inhibition", 2)
                    ch_j "Right!"
                "Well you're supposed to do what I say. . .":
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "obedience", 10)
                    ch_j "Um, yeah."
                    $ JeanX.change_face("sly", 1)
                    ch_j "I can do that!"
        "Well, don't.":
            $ JeanX.change_face("sadside", 1)
            call change_Girl_stat(JeanX, "love", -10)
            call change_Girl_stat(JeanX, "obedience", -5)
            call change_Girl_stat(JeanX, "inhibition", -10)
            ch_j "Oh. . ."
            ch_j "Bummer."
            return
    $ JeanX.change_face("sly", 1)
    $ JeanX.player_petname = "master"
    call change_Girl_stat(JeanX, "obedience", 50)
    call change_Girl_stat(JeanX, "obedience", 25)
    pause 0.1
    return








label Jean_Daddy:
    $ JeanX.daily_history.append("relationship")
    $ shift_focus (JeanX)
    call set_the_scene
    ch_j ". . ."
    if JeanX in Player.Harem:
        ch_j "Ok, so I know we're dating. . ."
    else:
        ch_j "You. . . like me, right?"
    if JeanX.love > JeanX.obedience and JeanX.love > JeanX.inhibition:
        ch_j "and I've really been warming up to this. . ."
    elif JeanX.obedience > JeanX.inhibition:
        ch_j "I. . . \"respect\" you? . ."
    else:
        ch_j "and this is fun. . ."
    ch_j "I've been thinking, you know what would be totally hot? . ."
    ch_j "What if I called you. . . \"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ JeanX.change_face("smile")
            call change_Girl_stat(JeanX, "love", 20)
            call change_Girl_stat(JeanX, "obedience", 10)
            call change_Girl_stat(JeanX, "inhibition", 30)
            ch_j "Cool."
        "What do you mean by that?":
            $ JeanX.change_face("bemused")
            ch_j "It's just kinda kinky, right. . ."
            ch_j "\"Daddy?\""

            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ JeanX.change_face("smile")
                    call change_Girl_stat(JeanX, "love", 15)
                    call change_Girl_stat(JeanX, "obedience", 20)
                    call change_Girl_stat(JeanX, "inhibition", 25)
                    ch_j "Nice."
                    $ JeanX.change_face("sly", 2)
                    ch_j " . . . daddy."
                    $ JeanX.change_face("sly", 1)
                    $ JeanX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "obedience", 40)
                    call change_Girl_stat(JeanX, "inhibition", 20)
                    $ JeanX.change_face("angry", 2)
                    ch_j " . . . "
                    ch_j "Fine, be that way!"
                    $ JeanX.change_face("angry", 1, eyes = "side")
                "You've got some real daddy issues, uh?":
                    call change_Girl_stat(JeanX, "love", -15)
                    call change_Girl_stat(JeanX, "obedience", 45)
                    call change_Girl_stat(JeanX, "inhibition", 5)
                    $ JeanX.change_face("angry", 2)
                    ch_j "Oh, whatever, like you know!"
                    $ JeanX.change_face("angry", 1, eyes = "side")
        "You've got some real daddy issues, uh?":
            call change_Girl_stat(JeanX, "love", -15)
            call change_Girl_stat(JeanX, "obedience", 45)
            call change_Girl_stat(JeanX, "inhibition", 5)
            $ JeanX.change_face("angry", 2)
            ch_j "Oh, whatever, like you know!"
            $ JeanX.change_face("angry", 1, eyes = "side")
    $ JeanX.player_petnames.append("daddy")
    return
