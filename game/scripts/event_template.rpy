label event_template:

    # a tasteful fade-to-black while we change scenery
    show black_screen onlayer black

    # sets the location you want the event to take place in
    $ Player.location = "bg_classroom"

    hide black_screen onlayer black

    "This is narration."
    "You enter the classroom and have a seat."
    "The bell to class rings, but Professor McCoy seems to be late."
    "A strange woman enters the room and heads to the podium with a regal stride."

    # this shows Emma's normal standing sprite
    show Emma_sprite standing

    # if you wanted her to appear and then turn to diamond, you could do this
    show Emma_sprite standing diamond with Emma_harden

    # this changes the Girl's face. preset emotion's include:
    # _normal, _angry, _bemused, _closed, _confused, _kiss, _sad, _sadside, _sexy, _sly, _smile, _surprised, _oh, _startled, _down, _perplexed, _sucking, _tongue, _manic
    $ EmmaX.change_face("_normal")
    $ EmmaX.arm_pose = 1

    # lines that begin with ch_ are voiced by a character: ch_e is Emma, ch_p is Zero, and so on
    ch_u "Hello students. My name is Emma Frost, and I have been invited to conduct this class."

    # notice that this character went from being unknown (ch_u) to Emma (ch_e) once she introduced herself
    ch_e "I hope that over my tenure here you will demonstrate talents and hard work worthy of my respect."
    "She scans her eyes over the room, passing over each student."

    # you can also specify a preset emotion with modifications: for example, blushing (from 0 - 2), as well as specific mouth, brows, and eyes
    $ EmmaX.change_face("_surprised", blushing = 1)

    pause 1

    # see?
    $ EmmaX.change_face("_sly", mouth = "_sad")

    # this is the command to raise or lower stats. the first argument is the stat to raise and the third argument is the amount to raise by
    call change_Girl_stat(EmmaX, "love", 90, -10)

    # you can also directly raise a stat, but this will not be accompanied by a notification
    $ EmmaX.lust += 5

    "As her eyes pass over you, they briefly widen and then narrow."

    $ EmmaX.change_face("_sly")

    ch_e "Very well, let us begin, class."

    $ EmmaX.change_face("_normal")

    "The class is pretty basic today, mostly a lecture on her areas of expertise, psychology and literature."

    $ EmmaX.lust += 5

    "She asks a lot of questions of the students, and singles you out more than once. You notice her glancing in your direction as other students answer."

    $ EmmaX.lust += 5

    # this is one way to indicate for me that you want some time to pass
    call wait

    ch_e "All right students, class dismissed."

    # note that you can put variables in []s and Ren'Py will interpolate the correct string to place
    ch_e "[EmmaX.player_petname], could you wait a moment, I have something to discuss with you."

    # this is a menu. the first item here indicates that the title of the menu should be the last line said; each subsequent item is a menu option
    menu:
        extend ""
        "Yes?":

            # this indicates what should happen if this menu option is chosen
            call change_Girl_stat(EmmaX, "love", 70, 10)
            $ EmmaX.change_face("_normal")
        "I've got places to be.":
            call change_Girl_stat(EmmaX, "love", 70, -15)
            call change_Girl_stat(EmmaX, "obedience", 80, 10)
            $ EmmaX.change_face("_angry")

            ch_e "[Player.name], do not take that attitude with me."
            "She places herself in the doorway, preventing you from leaving."
        "For such a sexy teacher? I've got some time.":
            call change_Girl_stat(EmmaX, "love", 70, -5)
            call change_Girl_stat(EmmaX, "obedience", 80, 5)
            $ EmmaX.change_face("_angry", 1, mouth = "_smirk")

            ch_e "That's rather. . . inappropriate."

            $ EmmaX.change_face("_bemused", mouth = "_smile")
            call change_Girl_stat(EmmaX, "love", 70, 20)
            call change_Girl_stat(EmmaX, "lust", 50, 5)
            call change_Girl_stat(EmmaX, "inhibition", 25, 15)

            ch_e "But also obvious, so I can't criticize you too harshly."

    ch_e "I've heard about you from Professor Xavier and. . . others."

    # these are conditional statements that select options based on the indicated criteria
    if Player.reputation <= 200:

        # this only happens if Zero's reputation is less than or equal to 200, for example
        call change_Girl_stat(EmmaX, "obedience", 80, 10)
        call change_Girl_stat(EmmaX, "inhibition", 90, 15)
        call change_Girl_stat(EmmaX, "lust", 50, 5)
        $ EmmaX.change_face("_angry", brows = "_confused")

        ch_e "You seem to be a bit of a scoundrel. . ."
    elif Player.reputation < 600:
        call change_Girl_stat(EmmaX, "obedience", 80, 5)
        call change_Girl_stat(EmmaX, "inhibition", 90, 5)
        call change_Girl_stat(EmmaX, "lust", 50, 5)
        $ EmmaX.change_face("_sly")

        ch_e "You have quite a reputation around campus. . ."
    else:
        $ EmmaX.change_face("_smile")

        ch_e "You have managed a reasonable reputation. . ."

    if total_SEXP >= 110 or (len(Player.Harem) >= 2 and not simulation):
        call change_Girl_stat(EmmaX, "love", 70, 5)
        call change_Girl_stat(EmmaX, "obedience", 80, 10)
        call change_Girl_stat(EmmaX, "inhibition", 200, 10)
        call change_Girl_stat(EmmaX, "lust", 50, 5)
        $ EmmaX.change_face("_sly")

        ch_e ". . . and a number of conquests to your name. . ."
    elif total_SEXP >= 60:
        call change_Girl_stat(EmmaX, "love", 70, 5)
        call change_Girl_stat(EmmaX, "obedience", 80, 5)
        call change_Girl_stat(EmmaX, "inhibition", 200, 5)
        call change_Girl_stat(EmmaX, "lust", 50, 2)
        $ EmmaX.change_face("_smile")

        ch_e ". . . and are not without some romantic entanglements. . ."
    else:
        $ EmmaX.change_face("_smile", brows = "_confused")

        ch_e ". . .though I haven't heard of much of a romantic life. . ."

    if Player.level >= 3:
        call change_Girl_stat(EmmaX, "love", 70, 5)
        call change_Girl_stat(EmmaX, "obedience", 80, 5)
        $ EmmaX.change_face("_smile")

        ch_e "But your grades have been excellent."
    elif Player.level >= 2:
        $ EmmaX.change_face("_normal", brows = "_confused")

        ch_e "But your grades have been marginal at best."
    else:
        call change_Girl_stat(EmmaX, "love", 70, -5)
        call change_Girl_stat(EmmaX, "lust", 10, -5, 1)
        $ EmmaX.change_face("_normal", brows = "_sad")

        ch_e "But you haven't been living up to your potential in class."

    $ EmmaX.change_face("_normal", eyes = "_side")

    ch_e "My particular interest in this case, however. . ."

    $ EmmaX.change_face("_sly")

    ch_e "is that I cannot get a \"read\" on you."

    $ EmmaX.change_face("_sly", mouth = "_normal")

    ch_e "My mutant power is telepathy, the same as Professor Xavier's."
    ch_e "I've grown accustomed to knowing what those around me are thinking."

    $ EmmaX.change_face("_bemused", eyes = "_side")

    ch_e "With you. . . I cannot do that, which presents an interesting. . ."

    $ EmmaX.change_face("_sly")

    ch_e ". . . challenge. . ."

    menu:
        extend ""
        "I imagine it would.":
            call change_Girl_stat(EmmaX, "love", 70, 5)
            call change_Girl_stat(EmmaX, "inhibition", 200, 5)
            $ EmmaX.change_face("_normal")

            ch_e "Hmm, yes."
        "Huh.":
            call change_Girl_stat(EmmaX, "love", 70, -1)
            call change_Girl_stat(EmmaX, "obedience", 80, -1)
            $ EmmaX.change_face("_confused", mouth = "_normal")

            ch_e ". . . yes."

            $ EmmaX.change_face("_normal")
        "So you can't see what I'm picturing right now?":
            call change_Girl_stat(EmmaX, "obedience", 80, 5)
            $ EmmaX.change_face("_bemused")

            # you can have little mini-animations by setting the sprite to do something, pausing, and then changing the sprite
            pause 0.5

            $ EmmaX.change_face("_bemused", eyes = "_down")

            "She glances downward."

            $ EmmaX.change_face("_sly")
            call change_Girl_stat(EmmaX, "love", 70, 10)
            call change_Girl_stat(EmmaX, "inhibition", 200, 10)
            call change_Girl_stat(EmmaX, "lust", 50, 15)

            ch_e "I can't read your mind, but I'm not blind, [EmmaX.player_petname]."

    ch_e "In any case, I think we should set aside some time to talk."
    ch_e "I'd like to make you a personal project, so I can see how you tick."

    menu:
        extend ""
        "I'd be ok with that.":
            call change_Girl_stat(EmmaX, "love", 70, 5)
            call change_Girl_stat(EmmaX, "inhibition", 200, 5)
            $ EmmaX.change_face("_smile")

            ch_e "Excellent, I look forward to it."
        "I don't know if you should experiment on your students.":
            call change_Girl_stat(EmmaX, "love", 70, -5)
            $ EmmaX.change_face("_normal", mouth = "_sad")

            ch_e "There's nothing for you to worry about."

            $ EmmaX.change_face("_sly")

            ch_e "I'll be. . . gentle."
        "If it means spending more time with you. . .":
            if approval_check(EmmaX, 295, "L"):
                call change_Girl_stat(EmmaX, "inhibition", 200, 5)
                call change_Girl_stat(EmmaX, "lust", 50, 5)
                $ EmmaX.change_face("_sly")

                ch_e "Oh, I believe we'll be spending a good deal of time together. . ."
            else:
                $ EmmaX.change_face("_angry")

                ch_e "Much as it may pain me, it would. . ."

                $ EmmaX.change_face("_normal")
        "What do I get out of it?":
            if not approval_check(EmmaX, 290, "L"):
                call change_Girl_stat(EmmaX, "love", 70, -5)
                call change_Girl_stat(EmmaX, "obedience", 80, 5)
                call change_Girl_stat(EmmaX, "inhibition", 200, 5)
                $ EmmaX.change_face("_angry")

                ch_e "You'll stand some chance of passing this class, [EmmaX.player_petname]."

                $ EmmaX.change_face("_normal")
            else:
                if EmmaX.obedience > 0:
                    $ EmmaX.change_face("_confused", mouth = "_smirk")

                    ch_e "What would you {i}like{/i} to \"get out of it?\""

                    menu:
                        extend ""
                        "I guess if it helps your \"research.\" . .":
                            call change_Girl_stat(EmmaX, "love", 70, 10)
                            call change_Girl_stat(EmmaX, "obedience", 80, -5)
                            $ EmmaX.change_face("_smile")

                            ch_e "I'm glad to see that you can be reasonable."
                        "Spending more time with you would be plenty. . .":
                            call change_Girl_stat(EmmaX, "love", 70, 5)
                            call change_Girl_stat(EmmaX, "obedience", 80, 5)
                            call change_Girl_stat(EmmaX, "lust", 20, 5)
                            $ EmmaX.change_face("_sly")

                            ch_e "It certainly should be."
                        "A kiss?":
                            call change_Girl_stat(EmmaX, "love", 70, -5)
                            call change_Girl_stat(EmmaX, "obedience", 80, 10)
                            $ EmmaX.change_face("_surprised", 1, mouth = "_surprised")

                            ch_e "[EmmaX.player_petname], that is incredibly inappropriate!"

                            $ EmmaX.change_face("_sadside", 0, brows = "_angry")

                            ch_e "I would {i}never{/i} consider such a thing with a student."

                            if approval_check(EmmaX, 220, "I"):
                                $ EmmaX.change_face("_sly", 1)
                                call change_Girl_stat(EmmaX, "love", 70, 5)
                                call change_Girl_stat(EmmaX, "obedience", 80, 5)
                                call change_Girl_stat(EmmaX, "inhibition", 200, 5)
                                call change_Girl_stat(EmmaX, "lust", 50, 5)

                                ch_e ". . .never. . ."
                        "I think you know what I'd want. . .":
                            call change_Girl_stat(EmmaX, "obedience", 80, 5)
                            call change_Girl_stat(EmmaX, "lust", 50, 5)
                            $ EmmaX.change_face("_sly", brows = "_angry")

                            ch_e "Yes, I imagine that I do. . ."

                            if approval_check(EmmaX, 220, "I"):
                                $ EmmaX.change_face("_sly", 1)
                                call change_Girl_stat(EmmaX, "love", 70, 5)
                                call change_Girl_stat(EmmaX, "obedience", 80, 5)
                                call change_Girl_stat(EmmaX, "inhibition", 200, 10)
                                call change_Girl_stat(EmmaX, "lust", 50, 5)

                                ch_e "And we may be able to come to some sort of \"mutually beneficial\" arrangement."
                            else:
                                $ EmmaX.change_face("_bemused", 0)
                                call change_Girl_stat(EmmaX, "love", 70, -5)

                                ch_e "But figuring out whether I'm correct is the entire point here."
                else:
                    $ EmmaX.change_face("_normal")

                    ch_e "The satisfaction of helping my. . . studies."

                    if approval_check(EmmaX, 300, "L"):
                        $ EmmaX.change_face("_sly")
                        call change_Girl_stat(EmmaX, "obedience", 80, 5)
                        call change_Girl_stat(EmmaX, "inhibition", 200, 5)
                        call change_Girl_stat(EmmaX, "lust", 50, 5)

                        ch_e "-and maybe if you're good. . ."
                    else:
                        ch_e "-and nothing more."

    $ EmmaX.change_face("_normal", 0)

    ch_e "That said, class is finished for the day and I have some paperwork to attend to, so I'll see you. . ."
    ch_e ". . . later. . ."

    # when a character leaves, you hide the sprite
    hide Emma_sprite

    "She strides out of the room and down the hall."

    # and that's it. I will fill in the blanks with necessary function calls

    return
