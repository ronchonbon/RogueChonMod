label meet_Jean:
    $ JeanX.name = "???"
    $ JeanX.location = "bg_shower"
    $ JeanX.change_face("sly")
    $ JeanX.Outfit.remove_Clothing(["pants", "skirt"])

    $ JeanX.player_petname = random_name(seed = False)
    $ JeanX.player_petnames.append(JeanX.player_petname)

    call set_the_scene(location = "bg_shower", fade = True)
    $ shift_focus(JeanX)

    "As you approach the showers, you notice someone getting dressed."
    ch_j "Hmm. . . I don't think I've seen you around before."
    ch_j "[JeanX.player_petname], right?"

    menu:
        ch_j "[JeanX.player_petname], right?"
        "No, it's [Player.name], actually.":
            $ JeanX.player_petname = random_name(seed = True)
            $ JeanX.player_petnames.append(JeanX.player_petname)

            call change_Girl_stat(JeanX, "love", -2)
            call change_Girl_stat(JeanX, "obedience", 2)

            ch_j "Right, [JeanX.player_petname], got it."
        "Yup, [JeanX.player_petname].":
            $ JeanX.change_face("sly", mouth = "smile")
            call change_Girl_stat(JeanX, "love", 5)

            ch_j "Thought you looked like a \"[JeanX.player_petname].\""
        "It's [Player.name], remember it.":
            $ JeanX.player_petname = random_name(seed = True)
            $ JeanX.player_petnames.append(JeanX.player_petname)

            $ JeanX.change_face("confused")
            call change_Girl_stat(JeanX, "love", -5)
            call change_Girl_stat(JeanX, "obedience", 5)

            ch_j "Right, [JeanX.player_petname], I heard you!"

    $ JeanX.change_face("sly")

    $ argued = False

    menu:
        extend ""
        "No, seriously, it's [Player.name]." if Player.name != JeanX.player_petname:
            $ JeanX.change_face("angry", blushing = 1)

            call change_Girl_stat(JeanX, "love", -5)
            call change_Girl_stat(JeanX, "obedience", 5)

            ch_j "I KNOW!!!"

            $ JeanX.change_face("bemused", blushing = 0, eyes = "side")

            ch_j "Seriously [JeanX.player_petname], you need to -relax.-"
        "No, it's. . . oh, that's right, [Player.name]." if Player.name == JeanX.player_petname:
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 2)

            ch_j "See? Brain like a steel trap."
        "Yup.":
            call change_Girl_stat(JeanX, "love", 5)
            call change_Girl_stat(JeanX, "obedience", 5)
        "Listen you stupid. . ." if Player.name != JeanX.player_petname:
            $ JeanX.change_face("confused")
            call change_Girl_stat(JeanX, "love", -10)
            call change_Girl_stat(JeanX, "obedience", 2)

            ch_j "I'm going to stop you right there, [JeanX.player_petname]."

            $ JeanX.change_face("angry", eyes = "psychic")

            ch_j "If I say your name is [JeanX.player_petname], it's [JeanX.player_petname]."

            $ JeanX.change_face("sly")

            ch_j "Right. . . [JeanX.player_petname]?"

            menu:
                extend ""
                "Oh, yeah. [JeanX.player_petname].":
                    $ JeanX.change_face("confused", blushing = 1, eyes = "side")
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "obedience", 5)

                    ch_j "Ok. . ."
                "Whatever.":
                    $ JeanX.change_face("confused", blushing = 1, eyes = "side")
                    call change_Girl_stat(JeanX, "obedience", 10)

                    ch_j ". . ."
                    ch_j "Right. . ."
                "No, it's [Player.name], pay attention!":
                    $ JeanX.change_face("confused", blushing = 1, eyes = "side")

                    call change_Girl_stat(JeanX, "love", -10)
                    call change_Girl_stat(JeanX, "obedience", 10)
                    call change_Girl_stat(JeanX, "inhibition", -10)

                    ch_j "Huh?"
                    ch_j "But I. . ."

                    $ JeanX.change_face("angry", blushing = 1, eyes = "psychic")

                    menu:
                        ch_j "Quack like a duck!"
                        "Quack [[sell it]":
                            $ JeanX.change_face("smile", blushing = 0)
                            call change_Girl_stat(JeanX, "love", 5)
                            call change_Girl_stat(JeanX, "obedience", -5)
                            call change_Girl_stat(JeanX, "inhibition", 10)

                            ch_j "Ah, ok, now we're getting somewhere."
                        "Quack [[sarcastically]":
                            $ JeanX.change_face("angry", blushing = 0, eyes = "squint")
                            call change_Girl_stat(JeanX, "love", -3)
                            call change_Girl_stat(JeanX, "obedience", 10)
                            call change_Girl_stat(JeanX, "inhibition", -5)

                            ch_j ". . ."

                            $ JeanX.change_face("sly")

                            ch_j "Good enough. . ."
                        "No.":
                            $ JeanX.change_face("confused", blushing = 1, eyes = "side")
                            call change_Girl_stat(JeanX, "love", -10)
                            call change_Girl_stat(JeanX, "obedience", 15)
                            call change_Girl_stat(JeanX, "inhibition", -5)

                            ch_j "This doesn't make sense. . ."

                            $ JeanX.change_face("angry", blushing = 1, eyes = "psychic")

                            ch_j "Could you be too dumb to mind-take? . . "

                            $ JeanX.change_face("confused", blushing = 1, eyes = "psychic")

                            ch_j "No, it worked on Logan. . ."

                            $ argued = True

    if not argued:
        $ JeanX.change_face("sly")

        ch_j "Anyway, I know what you were doing here. . ."
        ch_j "I bet you were hoping that you'd catch me naked or something, uh?"
        ch_j "Wanted to see these titties?"

        $ JeanX.arm_pose = 2
        $ JeanX.expose_breasts()

        pause 1.0

        call fix_clothing(JeanX)

        $ JeanX.change_face("sly", blushing = 0, eyes = "side")
        $ JeanX.arm_pose = 1

        menu:
            ch_j "Can't blame you, everyone does, the pervs."
            ". . . Thanks?":
                $ JeanX.change_face("bemused")
                call change_Girl_stat(JeanX, "love", 10)
                call change_Girl_stat(JeanX, "obedience", 5)

                ch_j "You're welcome, I don't mind being generous. . ."
            "Wow, those were great!":
                $ JeanX.change_face("smile")
                call change_Girl_stat(JeanX, "love", 15)
                call change_Girl_stat(JeanX, "obedience", 5)

                ch_j "I know, it's nice to put them on display from time to time. . ."
            "Pretty loose, aren't you?":
                $ JeanX.change_face("smile", brows = "confused")
                call change_Girl_stat(JeanX, "love", -3)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "inhibition", -5)

                ch_j "Well, only because I know how great they look. . ."

        # call Jean_First_Topless (0, 1)
        $ JeanX.change_face("bemused")

        ch_j ". . . not that you'll remember this in five minutes."

        $ JeanX.change_face("bemused", eyes = "psychic")

        ch_j "Now, what just happened?"

        $ JeanX.change_face("bemused")

        menu:
            extend ""
            "Nothing unusual.":
                call change_Girl_stat(JeanX, "love", 5)

                ch_j "Damned skippy, [JeanX.player_petname]."
            "I. . . don't know?":
                call change_Girl_stat(JeanX, "love", 5)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "inhibition", -5)

                ch_j "Right."

                $ JeanX.change_face("perplexed", blushing = 0)

                ch_j ". . ."
            "You just flashed me.":
                call change_Girl_stat(JeanX, "love", 5)

                ch_j "Exactl-{w=0.3}{nw}"

                $ JeanX.change_face("surprised", blushing = 2)

                call change_Girl_stat(JeanX, "love", -10)
                call change_Girl_stat(JeanX, "obedience", 10)
                call change_Girl_stat(JeanX, "inhibition", -5)

                $ JeanX.arm_pose = 2

                ch_j "Exactl- wait, what?"

                $ JeanX.change_face("surprised", blushing = 1)

                menu:
                    extend ""
                    "I mean, nothing unusual?":
                        $ JeanX.change_face("confused", blushing = 1)
                        call change_Girl_stat(JeanX, "love", 5)
                        call change_Girl_stat(JeanX, "obedience", 5)

                        ch_j ". . ."

                        $ JeanX.change_face("confused", blushing = 1, eyes = "side")

                        ch_j "Right. . ."
                    "You just flashed me.":
                        $ JeanX.change_face("confused", blushing = 2)
                        call change_Girl_stat(JeanX, "love", -5)
                        call change_Girl_stat(JeanX, "obedience", 10)

                        ch_j "How did you remember. . ."

                        $ JeanX.change_face("angry", blushing = 1)

                        ch_j "You should have forgotten that!"
                        ch_j "I mind took you!"

                        $ line = "power"
                    "You showed me your tits, you ditz!":
                        $ JeanX.change_face("angry", blushing = 2)
                        call change_Girl_stat(JeanX, "love", -20)
                        call change_Girl_stat(JeanX, "obedience", 20)

                        ch_j "Don't take that tone with me!"

                        $ JeanX.change_face("confused", blushing = 1)

                        ch_j "How did you remember. . ."

                        $ JeanX.change_face("angry", blushing = 1)

                        ch_j "You should have forgotten that!"
                        ch_j "I mind took you!"

                        $ line = "power"

                $ JeanX.arm_pose = 1

    if not line:
        ch_j "Now, looks like the mirror's all foggy. . ."

        $ JeanX.change_face("sly", eyes = "psychic")

        ch_j "I'll just use your eyes. . ."

        $ JeanX.change_face("confused", blushing = 1)

        ch_j ". . ."

        $ JeanX.change_face("angry", blushing = 1)
        call change_Girl_stat(JeanX, "love", -5)
        call change_Girl_stat(JeanX, "obedience", 5)
        call change_Girl_stat(JeanX, "inhibition", -5)

        ch_j "What's happening? Why can't I get inside your head?"

    menu:
        extend ""
        "I'm immune to mutant powers.":
            $ JeanX.change_face("confused", blushing = 1)
            call change_Girl_stat(JeanX, "love", -10)
            call change_Girl_stat(JeanX, "obedience", 10)

            ch_j "Huh?"
            ch_j "That's a thing?!"

            $ JeanX.change_face("angry", blushing = 1)

            ch_j "Why did nobody tell me that's a thing?!"
        "I'm already in your head.":
            $ JeanX.change_face("surprised", blushing = 2)
            call change_Girl_stat(JeanX, "love", -5)
            call change_Girl_stat(JeanX, "obedience", 30)

            ch_j "What?!"

            $ JeanX.change_face("confused", blushing = 1)

            ch_j "Wait . ."

            $ JeanX.change_face("angry", blushing = 1)
            call change_Girl_stat(JeanX, "love", -15)
            call change_Girl_stat(JeanX, "obedience", -10)

            ch_j "No you're not!"
            ch_j "You're just, like. . . immune to mind-taking or something!"
        "I'm a figment of your imagination.":
            $ JeanX.change_face("angry", blushing = 2)

            call change_Girl_stat(JeanX, "love", -5)
            call change_Girl_stat(JeanX, "obedience", 15)

            ch_j "Now you're just fucking with me."

            $ JeanX.change_face("angry", blushing = 1, mouth = "surprised")
            call change_Girl_stat(JeanX, "love", -5)

            ch_j "I do the fucking!"

            $ JeanX.change_face("angry", blushing = 1)

            ch_j "You're just, like. . . immune to mind-taking or something!"

    call change_Girl_stat(JeanX, "inhibition", -200)

    if JeanX.History["breasts_seen"]:
        $ JeanX.change_face("angry", blushing = 1)

        menu:
            ch_j "So you saw my. . ."
            "Yup.":
                call change_Girl_stat(JeanX, "obedience", 3)
                call change_Girl_stat(JeanX, "inhibition", -5)
            ". . .":
                call change_Girl_stat(JeanX, "obedience", 7)
            "What?":
                pass

        $ JeanX.change_face("angry", blushing = 2)

        menu:
            ch_j "And you remember? . ."
            "Yup.":
                call change_Girl_stat(JeanX, "love", -3)
                call change_Girl_stat(JeanX, "obedience", 10)
            ". . .":
                call change_Girl_stat(JeanX, "obedience", 10)
            "Of course I don't remember you flashing me.":
                $ JeanX.change_face("smile", blushing = 0)
                call change_Girl_stat(JeanX, "love", 10)
                call change_Girl_stat(JeanX, "inhibition", 50)

                ch_j "Ok, goo- {w=0.3}{nw}"

                $ JeanX.change_face("angry", blushing = 2)
                call change_Girl_stat(JeanX, "love", -20)
                call change_Girl_stat(JeanX, "obedience", 20)
                call change_Girl_stat(JeanX, "inhibition", -40)

                ch_j "Ok, goo- you're just bullshitting me again!"

    $ JeanX.change_face("angry", blushing = 1, eyes = "psychic")

    ch_j "Argh!"
    "You feel a slight breeze against your cheek."

    $ JeanX.change_face("angry", blushing = 1)
    call change_Girl_stat(JeanX, "love", -10)
    call change_Girl_stat(JeanX, "obedience", 10)
    call change_Girl_stat(JeanX, "inhibition", -20)

    menu:
        ch_j "And you're immune to my telekinesis too?!"
        "So long as I want to be, yeah.":
            pass
        "Yup.":
            call change_Girl_stat(JeanX, "love", -5)
            call change_Girl_stat(JeanX, "obedience", 10)
        ". . .":
            call change_Girl_stat(JeanX, "love", 3)

    $ JeanX.change_face("angry", blushing = 1, eyes = "psychic")
    call change_Girl_stat(JeanX, "obedience", 10)

    "A locker rips from the wall and heads your way."
    "With a pulse of your power, it loses momentum and falls over."

    $ JeanX.change_face("angry", blushing = 1, eyes = "side")
    call change_Girl_stat(JeanX, "obedience", 10)
    call change_Girl_stat(JeanX, "inhibition", -10)

    ch_j ". . ."
    ch_j "Well that's inconvenient."
    ch_j "I'm not sure what to do with you. . ."

    $ JeanX.change_face("angry", blushing = 1)

    ch_j "I'm not used to anyone being able to just. . ."

    $ JeanX.change_face("angry", blushing = 2, eyes = "side")

    ch_j ". . . ignore me like that. . ."
    ch_j "I'll need to give this some thought. . ."

    call remove_Girl(JeanX)

    "She collects her things and leaves the room."
    ch_p "Was that. . . ?"

    $ active_Girls.append(JeanX)

    $ JeanX.name = "Jean"
    $ JeanX.History.update("met")

    $ round -= 10

    return
