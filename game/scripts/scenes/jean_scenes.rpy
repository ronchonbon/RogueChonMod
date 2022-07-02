label meet_Jean:
    $ Present = [JeanX]

    $ JeanX.name = "???"
    $ JeanX.location = "bg_showerroom"

    $ JeanX.Outfit.remove_Clothing(["pants", "skirt"])

    $ JeanX.change_face("sly")

    $ JeanX.add_word(1,"showered", "showered", 0, 0)

    call Jeanname(1)
    call set_the_scene(location = "bg_showerroom", fade = True)
    call shift_focus(JeanX)

    "As you approach the showers, you notice someone getting dressed."
    ch_j "Hmm. . . I don't think I've seen you around before."
    ch_j "[JeanX.player_petname], right?"

    menu:
        ch_j "[JeanX.player_petname], right?"
        "No, it's [Player.name], actually.":
            call Jeanname

            call change_Girl_stat(JeanX, "love", 90, -2)
            call change_Girl_stat(JeanX, "obedience", 200, 2)

            ch_j "Right, [JeanX.player_petname], got it."
        "Yup, [JeanX.player_petname].":
            $ JeanX.change_face("sly", mouth = "smile")
            call change_Girl_stat(JeanX, "love", 90, 5)

            $ JeanX.IX -= 5

            ch_j "Thought you looked like a \"[JeanX.player_petname].\""
        "It's [Player.name], remember it.":
            call Jeanname

            $ JeanX.change_face("confused")
            call change_Girl_stat(JeanX, "love", 90, -5)
            call change_Girl_stat(JeanX, "obedience", 200, 5)

            ch_j "Right, [JeanX.player_petname], I heard you!"

    $ JeanX.change_face("sly")
    $ argued = False
    menu:
        extend ""
        "No, seriously, it's [Player.name]." if Player.name != JeanX.player_petname:
            $ JeanX.change_face("angry", 1)
            call change_Girl_stat(JeanX, "love", 90, -5)
            call change_Girl_stat(JeanX, "obedience", 200, 5)
            $ JeanX.IX -= 5
            ch_j "I KNOW!!!"
            $ JeanX.change_face("bemused", 0,eyes = "side")
            ch_j "Seriously [JeanX.player_petname], you need to -relax.-"
        "No, it's. . . oh, that's right, [Player.name]." if Player.name == JeanX.player_petname:
            call change_Girl_stat(JeanX, "love", 90, 5)
            call change_Girl_stat(JeanX, "obedience", 200, 2)
            $ JeanX.IX -= 5
            ch_j "See? Brain like a steel trap."
        "Yup.":
            call change_Girl_stat(JeanX, "love", 90, 5)
            call change_Girl_stat(JeanX, "obedience", 200, 5)
            $ JeanX.IX -= 5
        "Listen you stupid. . ." if Player.name != JeanX.player_petname:
            $ JeanX.change_face("confused")
            call change_Girl_stat(JeanX, "love", 90, -10)
            call change_Girl_stat(JeanX, "obedience", 200, 2)
            ch_j "I'm going to stop you right there, [JeanX.player_petname]."
            $ JeanX.change_face("angry", eyes = "psychic")
            ch_j "If I say your name is [JeanX.player_petname], it's [JeanX.player_petname]."
            $ JeanX.change_face("sly")
            ch_j "Right. . . [JeanX.player_petname]?"

            menu:
                extend ""
                "Oh, yeah. [JeanX.player_petname].":
                    $ JeanX.change_face("confused", 1,eyes = "side")
                    call change_Girl_stat(JeanX, "love", 90, 5)
                    call change_Girl_stat(JeanX, "obedience", 200, 5)
                    ch_j "Ok. . ."
                "Whatever.":
                    $ JeanX.change_face("confused", 1,eyes = "side")
                    call change_Girl_stat(JeanX, "obedience", 200, 10)
                    ch_j ". . ."
                    ch_j "Right. . ."
                "No, it's [Player.name], pay attention!":
                    $ JeanX.change_face("confused", 1,eyes = "side")
                    call change_Girl_stat(JeanX, "love", 90, -10)
                    call change_Girl_stat(JeanX, "obedience", 200, 10)
                    call change_Girl_stat(JeanX, "inhibition", 200, -10)
                    ch_j "Huh?"
                    ch_j "But I. . ."
                    $ JeanX.change_face("angry", 1,eyes = "psychic")
                    ch_j "Quack like a duck!"
                    menu:
                        extend ""
                        "Quack [[sell it]":
                            $ JeanX.change_face("smile", 0)
                            call change_Girl_stat(JeanX, "love", 90, 5)
                            call change_Girl_stat(JeanX, "obedience", 200, -5)
                            call change_Girl_stat(JeanX, "inhibition", 200, 10)
                            ch_j "Ah, ok, now we're getting somewhere."
                        "Quack [[sarcastically]":
                            $ JeanX.change_face("angry", 0,eyes = "squint")
                            call change_Girl_stat(JeanX, "love", 90, -3)
                            call change_Girl_stat(JeanX, "obedience", 200, 10)
                            call change_Girl_stat(JeanX, "inhibition", 200, -5)
                            ch_j ". . ."
                            $ JeanX.change_face("sly")
                            ch_j "Good enough. . ."
                        "No.":
                            $ JeanX.change_face("confused", 1,eyes = "side")
                            call change_Girl_stat(JeanX, "love", 90, -10)
                            call change_Girl_stat(JeanX, "obedience", 200, 15)
                            call change_Girl_stat(JeanX, "inhibition", 200, -5)
                            ch_j "This doesn't make sense. . ."
                            $ JeanX.change_face("angry", 1,eyes = "psychic")
                            ch_j "Could you be too dumb to mind-take? . . "
                            $ JeanX.change_face("confused", 1,eyes = "psychic")
                            ch_j "No, it worked on Logan. . ."
                            $ argued = True


    if not argued:

        $ JeanX.change_face("sly")
        ch_j "Anyway, I know what you were doing here. . ."
        ch_j "I bet you were hoping that you'd catch me naked or something, uh?"
        ch_j "Wanted to see these titties?"
        $ JeanX.arm_pose = 2

        call expose_breasts(JeanX)

        pause 1

        call fix_clothing(JeanX)

        $ JeanX.change_face("sly", 0,eyes = "side")
        $ JeanX.arm_pose = 1
        ch_j "Can't blame you, everyone does, the pervs."
        menu:
            extend ""
            ". . . Thanks?":
                $ JeanX.change_face("bemused")
                call change_Girl_stat(JeanX, "love", 90, 10)
                call change_Girl_stat(JeanX, "obedience", 200, 5)
                $ JeanX.IX -= 10
                ch_j "You're welcome, I don't mind being generous. . ."
            "Wow, those were great!":
                $ JeanX.change_face("smile")
                call change_Girl_stat(JeanX, "love", 90, 15)
                call change_Girl_stat(JeanX, "obedience", 200, 5)
                $ JeanX.IX -= 15
                ch_j "I know, it's nice to put them on display from time to time. . ."
            "Pretty loose, aren't you?":
                $ JeanX.change_face("smile", brows = "confused")
                call change_Girl_stat(JeanX, "love", 90, -3)
                call change_Girl_stat(JeanX, "obedience", 200, 10)
                call change_Girl_stat(JeanX, "inhibition", 200, -5)
                ch_j "Well, only because I know how great they look. . ."
        call Jean_First_Topless (0, 1)
        $ JeanX.change_face("bemused")
        ch_j ". . . not that you'll remember this in five minutes."
        $ JeanX.change_face("bemused", eyes = "psychic")
        ch_j "Now, what just happened?"
        $ JeanX.change_face("bemused")
        menu:
            extend ""
            "Nothing unusual.":
                call change_Girl_stat(JeanX, "love", 90, 5)
                ch_j "Damned skippy, [JeanX.player_petname]."
            "I. . . don't know?":
                call change_Girl_stat(JeanX, "love", 90, 5)
                call change_Girl_stat(JeanX, "obedience", 200, 10)
                call change_Girl_stat(JeanX, "inhibition", 200, -5)
                ch_j "Right."
                $ JeanX.change_face("perplexed", 0)
                ch_j ". . ."
            "You just flashed me.":
                call change_Girl_stat(JeanX, "love", 90, 5)
                ch_j "Exactl-{w=0.3}{nw}"
                $ JeanX.change_face("surprised", 2)
                call change_Girl_stat(JeanX, "love", 90, -10)
                call change_Girl_stat(JeanX, "obedience", 200, 10)
                call change_Girl_stat(JeanX, "inhibition", 200, -5)
                $ JeanX.arm_pose = 2
                ch_j "Exactl- wait, what?"
                $ JeanX.change_face("surprised", 1)
                menu:
                    extend ""
                    "I mean, nothing unusual?":
                        $ JeanX.change_face("confused", 1)
                        call change_Girl_stat(JeanX, "love", 90, 5)
                        call change_Girl_stat(JeanX, "obedience", 200, 5)
                        ch_j ". . ."
                        $ JeanX.change_face("confused", 1,eyes = "side")
                        ch_j "Right. . ."
                    "You just flashed me.":
                        $ JeanX.change_face("confused", 2)
                        call change_Girl_stat(JeanX, "love", 90,-5)
                        call change_Girl_stat(JeanX, "obedience", 200, 10)
                        ch_j "How did you remember. . ."
                        $ JeanX.change_face("angry", 1)
                        ch_j "You should have forgotten that!"
                        ch_j "I mind took you!"
                        $ line = "power"
                    "You showed me your tits, you ditz!":
                        $ JeanX.change_face("angry", 2)
                        call change_Girl_stat(JeanX, "love", 90, -20)
                        call change_Girl_stat(JeanX, "obedience", 200, 20)
                        ch_j "Don't take that tone with me!"
                        $ JeanX.change_face("confused", 1)
                        ch_j "How did you remember. . ."
                        $ JeanX.change_face("angry", 1)
                        ch_j "You should have forgotten that!"
                        ch_j "I mind took you!"
                        $ line = "power"
                $ JeanX.arm_pose = 1


    if not line:

        ch_j "Now, looks like the mirror's all foggy. . ."
        $ JeanX.change_face("sly", eyes = "psychic")
        ch_j "I'll just use your eyes. . ."
        $ JeanX.change_face("confused", 1)
        ch_j ". . ."
        $ JeanX.change_face("angry", 1)
        call change_Girl_stat(JeanX, "love", 90, -5)
        call change_Girl_stat(JeanX, "obedience", 200, 5)
        call change_Girl_stat(JeanX, "inhibition", 200, -5)
        ch_j "What's happening? Why can't I get inside your head?"


    menu:
        extend ""
        "I'm immune to mutant powers.":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "love", 90, -10)
            call change_Girl_stat(JeanX, "obedience", 200, 10)
            ch_j "Huh?"
            ch_j "That's a thing?!"
            $ JeanX.change_face("angry", 1)
            ch_j "Why did nobody tell me that's a thing?!"
        "I'm already in your head.":
            $ JeanX.change_face("surprised", 2)
            call change_Girl_stat(JeanX, "love", 90, -5)
            call change_Girl_stat(JeanX, "obedience", 200, 30)
            ch_j "What?!"
            $ JeanX.change_face("confused", 1)
            ch_j "Wait . ."
            $ JeanX.change_face("angry", 1)
            call change_Girl_stat(JeanX, "love", 90, -15)
            call change_Girl_stat(JeanX, "obedience", 200, -10)
            ch_j "No you're not!"
            ch_j "You're just, like. . . immune to mind-taking or something!"
        "I'm a figment of your imagination.":
            $ JeanX.change_face("angry", 2)
            call change_Girl_stat(JeanX, "love", 90, -5)
            call change_Girl_stat(JeanX, "obedience", 200, 15)
            ch_j "Now you're just fucking with me."
            $ JeanX.change_face("angry", 1,mouth = "surprised")
            call change_Girl_stat(JeanX, "love", 90, -5)
            ch_j "I do the fucking!"
            $ JeanX.change_face("angry", 1)
            ch_j "You're just, like. . . immune to mind-taking or something!"
    call change_Girl_stat(JeanX, "inhibition", 200, -200)
    if JeanX.seen_breasts:
        $ JeanX.change_face("angry", 1)
        ch_j "So you saw my. . ."
        menu:
            "Yup.":
                call change_Girl_stat(JeanX, "obedience", 200, 3)
                call change_Girl_stat(JeanX, "inhibition", 200, -5)
            ". . .":
                call change_Girl_stat(JeanX, "obedience", 200, 7)
            "What?":
                pass
        $ JeanX.change_face("angry", 2)
        ch_j "And you remember? . ."
        menu:
            "Yup.":
                call change_Girl_stat(JeanX, "love", 90, -3)
                call change_Girl_stat(JeanX, "obedience", 200, 10)
            ". . .":
                call change_Girl_stat(JeanX, "obedience", 200, 10)
            "Of course I don't remember you flashing me.":
                $ JeanX.change_face("smile", 0)
                call change_Girl_stat(JeanX, "love", 90, 10)
                call change_Girl_stat(JeanX, "inhibition", 200, 50)
                ch_j "Ok, goo- {w=0.3}{nw}"
                $ JeanX.change_face("angry", 2)
                call change_Girl_stat(JeanX, "love", 90, -20)
                call change_Girl_stat(JeanX, "obedience", 200, 20)
                call change_Girl_stat(JeanX, "inhibition", 200, -40)
                ch_j "Ok, goo- you're just bullshitting me again!"
    $ JeanX.change_face("angry", 1,eyes = "psychic")
    ch_j "Argh!"
    "You feel a slight breeze against your cheek."
    $ JeanX.change_face("angry", 1)
    call change_Girl_stat(JeanX, "love", 90, -10)
    call change_Girl_stat(JeanX, "obedience", 200, 10)
    call change_Girl_stat(JeanX, "inhibition", 200, -20)
    ch_j "And you're immune to my telekinesis too?!"
    menu:
        "So long as I want to be, yeah.":
            pass
        "Yup.":
            call change_Girl_stat(JeanX, "love", 90, -5)
            call change_Girl_stat(JeanX, "obedience", 200, 10)
        ". . .":
            call change_Girl_stat(JeanX, "love", 90, 3)
    call change_Girl_stat(JeanX, "obedience", 200, 10)
    $ JeanX.change_face("angry", 1,eyes = "psychic")
    "A locker rips from the wall and heads your way."
    "With a pulse of your power, it loses momentum and falls over."
    $ JeanX.change_face("angry", 1,eyes = "side")
    call change_Girl_stat(JeanX, "obedience", 200, 10)
    call change_Girl_stat(JeanX, "inhibition", 200, -10)
    ch_j ". . ."
    ch_j "Well that's inconvenient."
    ch_j "I'm not sure what to do with you. . ."
    $ JeanX.change_face("angry", 1)
    ch_j "I'm not used to anyone being able to just. . ."
    $ JeanX.change_face("angry", 2,eyes = "side")
    ch_j ". . . ignore me like that. . ."
    ch_j "I'll need to give this some thought. . ."

    call remove_Girl(JeanX)

    "She collects her things and leaves the room."

    $ JeanX.name = "Jean"
    $ JeanX.location = "bg_jean"
    $ JeanX.history.append("met")

    $ active_Girls.append(JeanX)

    ch_p "Who the hell was that? . ."

    call shift_focus(RogueX)

    $ round -= 10

    jump shower_room



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
    $ JeanX.change_face("sly", 1,eyes = "down")
    ". . .{w=0.5}{nw}"
    $ JeanX.change_face("sly", 1)
    "She looks at you appraisingly."

    ch_j "You know. . . you're more fun to hang out with than I expected."
    $ line = "Y"
    if JeanX.action_counter["massage"] >= 5:
        call change_Girl_stat(JeanX, "lust", 60, 5)
        ch_j "You give really good massages. . ."
        $ line = "and Y"
    if JeanX.event_counter["orgasmed"]>= 10:
        $ JeanX.change_face("sly", 1)
        call change_Girl_stat(JeanX, "lust", 70, 5)
        ch_j "[line]ou -really- know how to finish them. . ."
        $ line = "and Y"
        if JeanX.event_counter["orgasmed"]>= 30:
            call change_Girl_stat(JeanX, "lust", 80, 10)
            ch_j ". . . seriously. . ."
    if JeanX.seen_peen:
        $ JeanX.change_face("sly", 1)
        call change_Girl_stat(JeanX, "love", 200, 5)
        call change_Girl_stat(JeanX, "obedience", 90, 10)
        call change_Girl_stat(JeanX, "inhibition", 200, 5)
        call change_Girl_stat(JeanX, "lust", 85, 5)
        ch_j "[line]ou're certainly well hung too. . ."
    $ line = 0

    ch_j "I really couldn't have a better little sex toy."
    menu:
        extend ""
        "I love it too.":
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "love", 200, 10)
            call change_Girl_stat(JeanX, "obedience", 90, 5)
            call change_Girl_stat(JeanX, "inhibition", 200, 5)
            ch_j "Good boy. . ."
            ch_j "Keep this up and I might \"reward\" you more often."
        "What if I want something more?":
            $ JeanX.brows = "confused"
            call change_Girl_stat(JeanX, "obedience", 90, 10)
            ch_j "Oh?"
            $ line = "more"
        "I'm not your toy.":
            $ JeanX.brows = "confused"
            call change_Girl_stat(JeanX, "obedience", 90, 15)
            ch_j "Huh?"

    $ JeanX.history.append("sexfriend")
    if line == "more":
        $ JeanX.brows = "confused"
        ch_j "What more could you want?"
        menu:
            extend ""
            "Could you be my girlfriend?":
                $ JeanX.change_face("surprised", 2)
                call change_Girl_stat(JeanX, "love", 200, 5)
                call change_Girl_stat(JeanX, "obedience", 90, -5)
                ch_j "Ha! Girlfriend. . ."
                $ JeanX.change_face("bemused", 1,eyes = "side")
                ch_j "That's just precious!"

                $ JeanX.change_face("sly", 1)
                if JeanX.event_counter["orgasmed"]>= 10:
                    ch_j "Look, you're pretty hot and all, and you can get it. . ."
                else:
                    ch_j "Look, you're pretty hot and all. . ."
                ch_j "but I just don't see you as \"relationship\" material. . ."
            "Couldn't we be sex friends?":

                $ JeanX.change_face("bemused", 1,eyes = "side")
                call change_Girl_stat(JeanX, "love", 200, 5)
                call change_Girl_stat(JeanX, "obedience", 90, 10)
                call change_Girl_stat(JeanX, "inhibition", 80, 5)
                call change_Girl_stat(JeanX, "inhibition", 200, 5)
                call change_Girl_stat(JeanX, "lust", 85, 10)
                ch_j "Hmm. . ."
                ch_j "Friends with. . . benefits? . ."
                $ JeanX.change_face("bemused", 1)
                ch_j "I guess we could do that. . ."
                $ line = 0
            "Nothing, I guess. . .":
                $ JeanX.change_face("bemused", 1)
                call change_Girl_stat(JeanX, "love", 200, 5)
                ch_j "Exactly."
                $ line = 0
    if line:
        menu:
            extend ""
            "So what could I do to change your mind?":
                $ JeanX.change_face("surprised", 1)
                call change_Girl_stat(JeanX, "obedience", 90, -10)
                ch_j "How should I know?!"
                $ JeanX.change_face("bemused", 1,eyes = "side")
                ch_j "I guess give me some reason to respect you or something?"
                $ JeanX.change_face("sly", 1)
                ch_j "I mean, fucking around, that's fine, but let's keep this casual."
            "I guess that's fine.":
                $ JeanX.change_face("sly", 1)
                call change_Girl_stat(JeanX, "love", 200, 5)
                call change_Girl_stat(JeanX, "obedience", 90, -5)
                call change_Girl_stat(JeanX, "inhibition", 200, 5)
                ch_j "Glad we got that settled."
            "Bitch.":
                $ JeanX.change_face("sly", 1)
                call change_Girl_stat(JeanX, "obedience", 90, 5)
                call change_Girl_stat(JeanX, "inhibition", 200, 10)
                call change_Girl_stat(JeanX, "lust", 85, 2)
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
        call change_Girl_stat(JeanX, "lust", 70, 5)
        ch_j "I mean, you really know how to lay it down."
    if JeanX.obedience < 900:
        $ JeanX.change_face("sly", 1,eyes = "side")
        call change_Girl_stat(JeanX, "love", 200, 5)
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
            call change_Girl_stat(JeanX, "love", 90, 10)
            call change_Girl_stat(JeanX, "love", 200, 10)
            call change_Girl_stat(JeanX, "obedience", 90, 10)
            ch_j ". . ."
            call change_Girl_stat(JeanX, "inhibition", 200, 5)
            ch_j "That's what I was going to say!"
        ". . .":
            call change_Girl_stat(JeanX, "obedience", 90, 10)
            call change_Girl_stat(JeanX, "obedience", 200, 5)
            ch_j "I. . ."
        "You love me.":
            $ JeanX.change_face("surprised", 2)
            call change_Girl_stat(JeanX, "love", 200, 5)
            call change_Girl_stat(JeanX, "obedience", 90, 10)
            call change_Girl_stat(JeanX, "obedience", 200, 5)
            ch_j ". . ."
            call change_Girl_stat(JeanX, "inhibition", 200, 5)
            ch_j "Well. . . yeah."
    $ JeanX.change_face("sly", 1)
    ch_j "I love you. . ."
    if line != "love":
        menu JeanLove_Menu:
            extend ""
            "I love you too.":
                call change_Girl_stat(JeanX, "love", 90, 5)
                call change_Girl_stat(JeanX, "love", 200, 10)
                call change_Girl_stat(JeanX, "obedience", 90, 10)
                call change_Girl_stat(JeanX, "inhibition", 200, 5)
                $ JeanX.change_face("smile", 1)
                ch_j "Great!"
            ". . ." if not line:
                $ line = "repeat"
                $ JeanX.change_face("sad", 2)
                call change_Girl_stat(JeanX, "love", 200, -5)
                call change_Girl_stat(JeanX, "obedience", 90, 10)
                call change_Girl_stat(JeanX, "obedience", 200, 10)
                call change_Girl_stat(JeanX, "inhibition", 200, -5)
                ch_j "Well, say something. . ."
                jump JeanLove_Menu
            "Cool." if line != "cool":
                $ line = "cool"
                $ JeanX.change_face("angry", 1)
                call change_Girl_stat(JeanX, "love", 200, -5)
                call change_Girl_stat(JeanX, "obedience", 90, 10)
                call change_Girl_stat(JeanX, "inhibition", 200, -5)
                ch_j "I feel like maybe you aren't taking this seriously."
                jump JeanLove_Menu
            "Sorry, I mean \"that's cool.\"" if line == "cool":
                ch_j ". . ."
                call change_Girl_stat(JeanX, "love", 200, -3)
                call change_Girl_stat(JeanX, "inhibition", 200, -3)
                ch_j "That still doesn't seem. . ."
                call change_Girl_stat(JeanX, "love", 200, 5)
                ch_j "Adequate. . ."
            "I don't feel the same way.":
                $ JeanX.change_face("surprised", 2)
                call change_Girl_stat(JeanX, "love", 200, -5)
                call change_Girl_stat(JeanX, "obedience", 90, 10)
                call change_Girl_stat(JeanX, "obedience", 200, 5)
                call change_Girl_stat(JeanX, "inhibition", 200, -5)
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
            call change_Girl_stat(JeanX, "love", 200, 5)
            call change_Girl_stat(JeanX, "obedience", 90, 10)
            call change_Girl_stat(JeanX, "obedience", 200, 10)
            call change_Girl_stat(JeanX, "inhibition", 200, 5)
            $ Player.Harem.append(JeanX)
        "Sure, I'd love to." if not Player.Harem:
            call change_Girl_stat(JeanX, "love", 200, 5)
            call change_Girl_stat(JeanX, "obedience", 90, 10)
            call change_Girl_stat(JeanX, "obedience", 200, 10)
            call change_Girl_stat(JeanX, "inhibition", 200, 5)
            $ Player.Harem.append(JeanX)
        "I'm not interested.":
            $ JeanX.change_face("surprised", 2)
            call change_Girl_stat(JeanX, "love", 200, -5)
            call change_Girl_stat(JeanX, "obedience", 90, 5)
            call change_Girl_stat(JeanX, "inhibition", 200, -5)
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
                    $ JeanX.change_face("angry", 1,eyes = "side")
                    call change_Harem_stat (JeanX, 700, -5)
                    if len(Player.Harem) >= 2:
                        ch_j "Bitches."
                    elif Player.Harem:
                        ch_j "That bitch."
                "I just don't like you like that.":
                    $ JeanX.change_face("sad", 2,eyes = "surprised")
                    call change_Girl_stat(JeanX, "love", 90, -5)
                    call change_Girl_stat(JeanX, "love", 200, -5)
                    call change_Girl_stat(JeanX, "obedience", 90, 5)
                    call change_Girl_stat(JeanX, "obedience", 200, 10)
                    call change_Girl_stat(JeanX, "inhibition", 200, -5)
                    ch_j "Oh."
                    $ JeanX.change_face("sadside", 1)
                    ch_j "."
                    ch_j ". ."
                    ch_j ". . ."
            $ JeanX.change_face("smile", 1,brows = "angry")
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
                    call change_Girl_stat(JeanX, "love", 200, 5)
                    call change_Girl_stat(JeanX, "obedience", 80, 10)
                    call change_Girl_stat(JeanX, "inhibition", 80, 5)
                    $ JeanX.change_face("surprised", 1)
                    ch_j "Oh, good."
                "Actually. . . I guess we'll need to work on that one." if "JeanYes" not in Player.traits:
                    call change_Girl_stat(JeanX, "inhibition", 200, 5)
                    call change_Girl_stat(JeanX, "lust", 80, 3)
                    $ JeanX.change_face("confused", 1)
                    ch_j "I think I could bring them around. . ."
                    menu:
                        extend ""
                        "No! Don't do that!":
                            $ JeanX.change_face("sly", 1)
                            call change_Girl_stat(JeanX, "obedience", 80, 5)
                            ch_j "Right."
                            ch_j ". . ."
                            call change_Girl_stat(JeanX, "inhibition", 200, 5)
                            call change_Girl_stat(JeanX, "lust", 80, 2)
                            ch_j "-wink-"
                            menu:
                                extend ""
                                "No! No \"wink!\"":
                                    $ JeanX.change_face("sly", 1,eyes = "stunned")
                                    call change_Girl_stat(JeanX, "obedience", 50, 5)
                                    call change_Girl_stat(JeanX, "obedience", 90, 3)
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
                            call change_Girl_stat(JeanX, "love", 200, 3)
                            call change_Girl_stat(JeanX, "obedience", 80, 3)
                            call change_Girl_stat(JeanX, "inhibition", 80, 1)
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
    $ JeanX.change_face("sly", 1,eyes = "side")
    ch_j "Hey. . . [JeanX.player_petname]."
    $ JeanX.eyes = "squint"
    ch_j "We need to talk."
    $ JeanX.change_face("sadside", 1)
    ch_j ". . ."
    ch_j "When we first met. . . I was pretty rude."
    ch_j "I get that."
    $ JeanX.change_face("sly", 1,eyes = "leftside")
    ch_j "When you're practically perfect in every way, you can look down your lessers."
    $ JeanX.change_face("angry", 1,eyes = "leftside")
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
            call change_Girl_stat(JeanX, "love", 80, -3)
            call change_Girl_stat(JeanX, "obedience", 90, -3)
            call change_Girl_stat(JeanX, "inhibition", 80, 2)
            ch_j "Well. . . I didn't want to spell it out. . ."
        "You know it.":
            call change_Girl_stat(JeanX, "obedience", 80, 3)
            ch_j ". . ."
        "Oh? That's nice!":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "obedience", 80, -3)
            ch_j "Um, I think you're missing my point. . ."

    $ JeanX.history.append("sir")
    menu:
        extend ""
        "Tell me what you want.":
            $ JeanX.change_face("sly", 1,eyes = "side")
            call change_Girl_stat(JeanX, "love", 80, 5)
            call change_Girl_stat(JeanX, "obedience", 90, 2)
            ch_j "Well. . . just that. . ."
            call change_Girl_stat(JeanX, "obedience", 90, 2)
            call change_Girl_stat(JeanX, "inhibition", 200, 1)
            call change_Girl_stat(JeanX, "lust", 80, 5)
            ch_j "Could you. . ."
            call change_Girl_stat(JeanX, "obedience", 80, 2)
            call change_Girl_stat(JeanX, "inhibition", 200, 2)
            call change_Girl_stat(JeanX, "lust", 80, 5)
            ch_j "boss me around a little more?"
        "Call me your \"Master.\"":
            call change_Girl_stat(JeanX, "love", 200, 5)
            call change_Girl_stat(JeanX, "obedience", 90, 10)
            call change_Girl_stat(JeanX, "inhibition", 200, 5)
            call change_Girl_stat(JeanX, "lust", 85, 10)
            $ JeanX.change_face("surprised", 2)
            ch_j "!!!"
            $ JeanX.change_face("sly", 1,eyes = "side")
            call change_Girl_stat(JeanX, "obedience", 90, -5)
            ch_j "Well. . . I don't know about that!"
            ch_j "I mean. . . I could -maybe- call you. . ."
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "obedience", 90, 5)
            call change_Girl_stat(JeanX, "lust", 85, 5)
            ch_j "Sir?"
        "Ok?":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "love", 200, 3)
            ch_j ". . ."
            ch_j "You still seem kinda lost here. . ."
            ch_j "Maybe I'm still not being clear, but. . ."
            $ JeanX.change_face("angry", 1,eyes = "side")
            call change_Girl_stat(JeanX, "obedience", 80, -3)
            ch_j "If I have to spell it out for you, then maybe it's not worth it."
            menu:
                extend ""
                "You want me to tell you what to do.":
                    call change_Girl_stat(JeanX, "love", 200, 3)
                    call change_Girl_stat(JeanX, "obedience", 90, 5)
                    call change_Girl_stat(JeanX, "inhibition", 200, 2)
                    ch_j ". . ."
                    $ JeanX.change_face("sly", 1)
                    call change_Girl_stat(JeanX, "obedience", 80, 3)
                    call change_Girl_stat(JeanX, "lust", 80, 3)
                    ch_j "Yes. . ."
                    menu:
                        extend ""
                        "So what will you call me?":
                            $ JeanX.eyes = "side"
                            ch_j "How about. . ."
                            $ JeanX.change_face("sly", 1)
                            call change_Girl_stat(JeanX, "love", 200, 5)
                            call change_Girl_stat(JeanX, "obedience", 80, 10)
                            call change_Girl_stat(JeanX, "inhibition", 90, 3)
                            call change_Girl_stat(JeanX, "lust", 80, 3)
                            ch_j "\"Sir?\""
                        ". . .":
                            ch_j "How about I call you. . ."
                            call change_Girl_stat(JeanX, "obedience", 80, 10)
                            call change_Girl_stat(JeanX, "inhibition", 200, 10)
                            call change_Girl_stat(JeanX, "lust", 80, 3)
                            ch_j "\"Sir?\""
                        "Call me \"sir.\"":
                            call change_Girl_stat(JeanX, "love", 200, 10)
                            call change_Girl_stat(JeanX, "obedience", 90, 15)
                            call change_Girl_stat(JeanX, "lust", 85, 10)
                            ch_j ". . ."
                            call change_Girl_stat(JeanX, "obedience", 90, 5)
                            ch_j "Yes. . . sir."
                "Yeah, I guess. . .":


                    call change_Girl_stat(JeanX, "love", 200, -5)
                    call change_Girl_stat(JeanX, "obedience", 80, -10)
                    call change_Girl_stat(JeanX, "inhibition", 90, -10)
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
    $ JeanX.change_face("sly", 1,eyes = "side")
    ch_j "Hey. . . [JeanX.player_petname]."
    ch_j "Would you. . . want me to call you. . ."
    ch_j "\"Master?\""
    $ JeanX.history.append("master")
    menu:
        "Yeah, do that.":
            $ JeanX.change_face("sly", 1,eyes = "side")
            call change_Girl_stat(JeanX, "love", 200, 5)
            call change_Girl_stat(JeanX, "obedience", 200, 5)
            ch_j "Well. . . Ok then."
            $ JeanX.player_petname = "master"
        "What? Why?":
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "obedience", 200, 5)
            call change_Girl_stat(JeanX, "inhibition", 200, 10)
            call change_Girl_stat(JeanX, "lust", 80, 5)
            ch_j "Because it's -hot!-"
            ch_j "Duh."
        ". . .":
            call change_Girl_stat(JeanX, "love", 80, -3)
            call change_Girl_stat(JeanX, "obedience", 200, 10)
            call change_Girl_stat(JeanX, "inhibition", 80, -2)
            ch_j "Well. . ."
            ch_j ". . ."
            $ JeanX.change_face("sly", 1)
            call change_Girl_stat(JeanX, "inhibition", 80, 10)
            call change_Girl_stat(JeanX, "inhibition", 200, 5)
            ch_j "I'm going to anyway."
        "Not really.":
            call change_Girl_stat(JeanX, "love", 80, -3)
            call change_Girl_stat(JeanX, "obedience", 80, 3)
            call change_Girl_stat(JeanX, "inhibition", 80, -5)
            ch_j "Oh. . ."
            ch_j "Well, ok. . ."
            return
    call change_Girl_stat(JeanX, "obedience", 200, 5)
    call change_Girl_stat(JeanX, "inhibition", 200, 5)
    call change_Girl_stat(JeanX, "lust", 80, 5)
    $ JeanX.player_petnames.append("master")
    $ JeanX.change_face("sly", 1)
    ch_j "Master."
    menu:
        "Well. . . ok then.":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "inhibition", 80, -1)
            ch_j ". . . good?"
        "I don't think you understand how this works.":
            $ JeanX.change_face("confused", 1)
            call change_Girl_stat(JeanX, "love", 200, -2)
            call change_Girl_stat(JeanX, "obedience", 80, 1)
            ch_j "I don't follow."
            menu:
                "Never mind.":
                    $ JeanX.change_face("sly", 1)
                    call change_Girl_stat(JeanX, "love", 200, 5)
                    call change_Girl_stat(JeanX, "obedience", 200, 5)
                    call change_Girl_stat(JeanX, "inhibition", 200, 2)
                    ch_j "Right!"
                "Well you're supposed to do what I say. . .":
                    call change_Girl_stat(JeanX, "love", 200, 5)
                    call change_Girl_stat(JeanX, "obedience", 200, 10)
                    ch_j "Um, yeah."
                    $ JeanX.change_face("sly", 1)
                    ch_j "I can do that!"
        "Well, don't.":
            $ JeanX.change_face("sadside", 1)
            call change_Girl_stat(JeanX, "love", 80, -10)
            call change_Girl_stat(JeanX, "obedience", 80, -5)
            call change_Girl_stat(JeanX, "inhibition", 80, -10)
            ch_j "Oh. . ."
            ch_j "Bummer."
            return
    $ JeanX.change_face("sly", 1)
    $ JeanX.player_petname = "master"
    call change_Girl_stat(JeanX, "obedience", 90, 50)
    call change_Girl_stat(JeanX, "obedience", 200, 25)
    pause 0.1
    return








label Jean_Daddy:
    $ JeanX.daily_history.append("relationship")
    call shift_focus (JeanX)
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
            call change_Girl_stat(JeanX, "love", 90, 20)
            call change_Girl_stat(JeanX, "obedience", 60, 10)
            call change_Girl_stat(JeanX, "inhibition", 80, 30)
            ch_j "Cool."
        "What do you mean by that?":
            $ JeanX.change_face("bemused")
            ch_j "It's just kinda kinky, right. . ."
            ch_j "\"Daddy?\""

            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ JeanX.change_face("smile")
                    call change_Girl_stat(JeanX, "love", 90, 15)
                    call change_Girl_stat(JeanX, "obedience", 60, 20)
                    call change_Girl_stat(JeanX, "inhibition", 80, 25)
                    ch_j "Nice."
                    $ JeanX.change_face("sly", 2)
                    ch_j " . . . daddy."
                    $ JeanX.change_face("sly", 1)
                    $ JeanX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(JeanX, "love", 90, 5)
                    call change_Girl_stat(JeanX, "obedience", 80, 40)
                    call change_Girl_stat(JeanX, "inhibition", 80, 20)
                    $ JeanX.change_face("angry", 2)
                    ch_j " . . . "
                    ch_j "Fine, be that way!"
                    $ JeanX.change_face("angry", 1,eyes = "side")
                "You've got some real daddy issues, uh?":
                    call change_Girl_stat(JeanX, "love", 90, -15)
                    call change_Girl_stat(JeanX, "obedience", 80, 45)
                    call change_Girl_stat(JeanX, "inhibition", 70, 5)
                    $ JeanX.change_face("angry", 2)
                    ch_j "Oh, whatever, like you know!"
                    $ JeanX.change_face("angry", 1,eyes = "side")
        "You've got some real daddy issues, uh?":
            call change_Girl_stat(JeanX, "love", 90, -15)
            call change_Girl_stat(JeanX, "obedience", 80, 45)
            call change_Girl_stat(JeanX, "inhibition", 70, 5)
            $ JeanX.change_face("angry", 2)
            ch_j "Oh, whatever, like you know!"
            $ JeanX.change_face("angry", 1,eyes = "side")
    $ JeanX.player_petnames.append("daddy")
    return




label Jeanname(Base=0, JNNum=0, Alpha=0, Jeannames={}):
    if Base == 1:
        $ Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        $ JNNum = renpy.random.randint(0, 25)
        $ Base = str(Alpha[JNNum])
    elif Base:
        pass
    else:
        $ Base = Player.name[:1]

    $ Jeannames = { "A":"Abe",
                    "B":"Barry",
                    "C":"Carl",
                    "D":"Dennis",
                    "E":"Erik",
                    "F":"Foggy",
                    "G":"Gil",
                    "H":"Hunk",
                    "I":"Ike",
                    "J":"Jeff",
                    "K":"Kirk",
                    "L":"Lance",
                    "M":"Mitch",
                    "N":"Norm",
                    "O":"Ollie",
                    "P":"Pete",
                    "Q":"Quince",
                    "R":"Rory",
                    "S":"Sonny",
                    "T":"Todd",
                    "U":"Uri",
                    "V":"Vince",
                    "W":"Wally",
                    "X":"Ray",
                    "Y":"Yuri",
                    "Z":"Zoro"}

    $ Base = Base.upper()
    if Base in Jeannames and Jeannames[Base] != Player.name:
        $ JeanX.player_petname = Jeannames[Base]
    else:

        $ Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        $ JNNum = renpy.random.randint(0, 25)
        $ Base = str(Alpha[JNNum])
        $ JeanX.player_petname = Jeannames[Base]

    return
