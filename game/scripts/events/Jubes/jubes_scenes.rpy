
label Jubes_Sunshine:
    call set_the_scene(location = "bg_campus", fade = True)

    $ JubesX.location = Player.location
    $ JubesX.change_face("smile")

    "On your way across the square, you see a shape charging toward you."

    call get_color_transform
    $ color_transform = _return

    call show_Girl(JubesX, x_position = stage_center, color_transform = color_transform, transition = vpunch)

    "[JubesX.name] crashes into you."
    $ JubesX.change_face("smile", 1, mouth = "sucking")
    ch_v "Hey, [Player.name]!"
    $ JubesX.change_face("smile", 1)
    ch_v "Check it out!"
    menu:
        extend ""
        "Oh, hey. . .":
            call change_Girl_stat(JubesX, "love", 2)
            $ JubesX.change_face("smile", 1, mouth = "sucking")
            ch_v "Yes, \"hey,\" but I am -outside!-"
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("smile", 1)
            ch_v "During the daytime!"
        "You're out during the day!":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "inhibition", 2)
        "Check what out?":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "obedience", 2)
            ch_v "Look!"
            ch_v "I'm -outside!-"
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("smile", 1, mouth = "sucking")
            ch_v "During the -daytime!-"
            $ JubesX.change_face("smile")
        "What the hell?":
            call change_Girl_stat(JubesX, "love", -3)
            call change_Girl_stat(JubesX, "obedience", 5)
            $ JubesX.change_face("surprised", 2, mouth = "sucking")
            ch_v "Sorry! I was just so excited!"
            $ JubesX.change_face("smile", 1)
            ch_v "I'm outside, during the daylight!"
    menu:
        extend ""
        "That's great!":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("surprised", 1, mouth = "sucking")
            ch_v "Right?!"
            $ JubesX.change_face("smile", 1)
        "So what? So am I.":
            call change_Girl_stat(JubesX, "love", -5)
            call change_Girl_stat(JubesX, "obedience", 5)
            $ JubesX.change_face("confused", 1)
            ch_v "Yes. . ."
            ch_v "But I am a -vampire, - remember?"
        "Ok.":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("confused", 1)
            ch_v ". . . I'm a -vampire?-"
    $ JubesX.change_face("surprised", 1, mouth = "sucking")
    ch_v "I didn't used to be able to do this without catching fire!"
    $ JubesX.change_face("smile", 1)
    menu:
        extend ""
        "So do you know why?":
            call change_Girl_stat(JubesX, "love", 1)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
        "Well it was never a problem for me.":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "obedience", 3)
            $ JubesX.change_face("confused", 1)
            ch_v ". . ."
            ch_v "No, I get that it wouldn't be. . ."
            $ JubesX.change_face("normal", 1)
        "Neat.":
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("confused", 1)
            ch_v ". . ."
            $ JubesX.change_face("normal", 1)
        "Ok.":
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("angry", 1)
            ch_v ". . ."
            $ JubesX.change_face("normal", 1)
    ch_v "I don't really know what caused it, but I guess it had to do with your blood. . ."
    $ JubesX.change_face("smile", 1)
    ch_v "Anyway, I just wanted to say \"thank you,\" this is great!"
    $ JubesX.add_word(1, 0, 0, 0, "sunshine")

    call remove_Girl(JubesX)

    "[JubesX.name] dashes off, and you continue on your way. . ."

    return





label check_sunshock:
    if JubesX not in Player.Party:
        return

    call is_Jubes_sunshocked

    if _return:
        menu:
            "Ok then, we can stay here.":
                if "stayed" in JubesX.recent_history:
                    call change_Girl_stat(JubesX, "love", -2)

                    ch_v "Now I kind feel like you're jerking me around. . ."
                elif approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    ch_v "That's really not necessary, don't let me hold you back."

                    menu:
                        extend ""
                        "I insist.":
                            $ JubesX.change_face("smile", 1)
                            call change_Girl_stat(JubesX, "love", 2)
                            call change_Girl_stat(JubesX, "inhibition", 2)

                            ch_v "Aw, thanks. That's sweet of you."
                        "Ok, sorry about that.":
                            call change_Girl_stat(JubesX, "obedience", 2)
                            $ JubesX.change_face("sad", 1)

                            $ Player.Party.remove(JubesX)

                            "You leave her behind."

                            return
                        "Cool, later then.":
                            call change_Girl_stat(JubesX, "love", -2)
                            call change_Girl_stat(JubesX, "obedience", 2)
                            $ JubesX.change_face("sad", 1)

                            $ Player.Party.remove(JubesX)

                            "You leave her behind."

                            return
                else:
                    ch_v "Thanks, that's sweet of you."

                $ JubesX.add_word(1, "stayed", 0, 0, 0)

                jump reset_location
            "Oh, too bad, you can stay here then.":
                $ Player.Party.remove(JubesX)

                call change_Girl_stat(JubesX, "love", -2)
                call change_Girl_stat(JubesX, "obedience", 2)

                if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    call change_Girl_stat(JubesX, "obedience", 2)
                    $ JubesX.change_face("sad", 1)

                    ch_v "I understand, later then. . ."
                else:
                    call change_Girl_stat(JubesX, "love", -4)
                    $ JubesX.change_face("angry", 1, mouth = "sucking")

                "You leave her behind."

                $ JubesX.change_face("sad", 1)

    return

label is_Jubes_sunshocked:
    if JubesX.addiction <= 50 or time_index > 2:
        return False

    $ JubesX.change_face("sad", 1)

    if "sunshock" in JubesX.recent_history:
        ch_v "Like I said, I'm not up for the sunshine."

        return True

    $ JubesX.add_word(1, "sunshock", 0, 0, 0)

    ch_v "Oh, wait, I'm kinda on a \"low charge\" at the moment, so I don't really want to go out in the sunlight?"

    menu:
        extend ""
        "Oh, sorry, that's fine.":
            call change_Girl_stat(JubesX, "love", 1)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("smile", 1)

            ch_v "Thanks for understanding. . ."

            return True
        "I could always. . . come get you?" if Player.location != JubesX.location and JubesX not in Player.Party:
            ch_v "Oh, that could be nice. I'll see you then."

            return True
        "I could always. . . top you off?" if Player.location == JubesX.location or JubesX in Player.Party:
            call change_Girl_stat(JubesX, "love", 1)
            $ JubesX.change_face("confused", 1)

            ch_v "Oh? What'd you have in mind?"

            $ menu_context = "sunshock"

            call addiction_ultimatum_menu

            if JubesX.addiction >= 70:
                call change_Girl_stat(JubesX, "inhibition", 1)
                call change_Girl_stat(JubesX, "inhibition", 1)

                ch_v "Couldn't I just touch you real quick?"

                menu:
                    extend ""
                    "Sure.":
                        call change_Girl_stat(Girl, "lust", 3)
                        call change_Girl_stat(Girl, "love", 6)
                        $ Girl.change_face("smile")

                        call girl_touches_you (Girl)
                    "Nope, sorry.":
                        call change_Girl_stat(JubesX, "love", -3)
                        call change_Girl_stat(JubesX, "obedience", 2)

                        if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                            $ JubesX.change_face("sad", 1)

                            ch_v "Oh."
                        else:
                            call change_Girl_stat(JubesX, "love", -2)
                            call change_Girl_stat(JubesX, "obedience", 2)
                            $ JubesX.change_face("angry", 1)

                            ch_v "Jerk."

            if JubesX.addiction >= 70:
                if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    $ JubesX.change_face("sad", 1)

                    ch_v "I'm sorry, I just can't, it would be agonizing."
                else:
                    $ JubesX.change_face("angry", 1)

                    ch_v "You have to be kidding! I'd catch fire!"

                return True
            elif approval_check(JubesX, 1600) or approval_check(JubesX, 500, "O"):
                call change_Girl_stat(JubesX, "obedience", 2)
                call change_Girl_stat(JubesX, "inhibition", 2)

                ch_v "I guess I could manage it for a little bit. . ."
            else:
                ch_v "Grow up. . ."

                return True
        "Come on, don't be like that.":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "obedience", 2)
            $ JubesX.change_face("sad", 1)

            if JubesX.addiction >= 70:
                if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    call change_Girl_stat(JubesX, "obedience", 2)

                    ch_v "I'm sorry, I just can't, it would be agonizing."
                else:
                    $ JubesX.change_face("angry", 1)

                    ch_v "You have to be kidding! I'd catch fire!"

                return True
            elif approval_check(JubesX, 1600) or approval_check(JubesX, 500, "O"):
                call change_Girl_stat(JubesX, "obedience", 2)
                call change_Girl_stat(JubesX, "inhibition", 2)

                ch_v "I guess I could manage it for a little bit. . ."
            else:
                ch_v "Grow up. . ."

                return True

    return False


label Jubes_Mall:
    $ shift_focus(JubesX)

    if JubesX.location == Player.location:
        "[JubesX.name] suddently freezes up, then turns to you."
    else:
        "[JubesX.name] rushes up to you."

    call clear_the_room (JubesX, 0, 0)
    call set_the_scene
    $ Player.add_word(1, 0, 0, 0, "mall")

    $ JubesX.change_face("surprised", 1, mouth = "sucking")
    ch_v "Hey, I just realized something!"
    $ JubesX.change_face("smile")
    menu:
        extend ""
        "Cool.":
            call change_Girl_stat(JubesX, "love", 1)
        "Oh, what?":
            call change_Girl_stat(JubesX, "love", 2)
            call change_Girl_stat(JubesX, "inhibition", 1)
        "Uh-huh.":
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", -1)
            $ JubesX.change_face("angry", 1, mouth = "sucking")
            ch_v "This is serious!"
        ". . .":
            call change_Girl_stat(JubesX, "love", -1)
            $ JubesX.change_face("confused")
            ch_v "Aren't you going to ask me \"what?\""
            menu:
                extend ""
                "Oh, sure, what?":
                    call change_Girl_stat(JubesX, "love", 2)
                    call change_Girl_stat(JubesX, "obedience", 1)
                    call change_Girl_stat(JubesX, "inhibition", 1)
                "No.":
                    call change_Girl_stat(JubesX, "love", -2)
                    call change_Girl_stat(JubesX, "obedience", 2)
                    call change_Girl_stat(JubesX, "inhibition", -1)
                    $ JubesX.change_face("angry")
                    ch_v "Dick."
                ". . .":
                    call change_Girl_stat(JubesX, "love", -1)
                    call change_Girl_stat(JubesX, "obedience", 1)
                    ch_v "Ooookaaay. . ."
    $ JubesX.change_face("surprised", 1, mouth = "sucking")
    ch_v "Now that I can go out during the daytime, I can go to the mall again!!"
    menu:
        extend ""
        "That's great!":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            ch_v "I know, right?"
            menu:
                extend ""
                "Wait, there's a mall?":
                    call change_Girl_stat(JubesX, "love", 1)
                    call change_Girl_stat(JubesX, "inhibition", 1)
                    $ JubesX.change_face("confused")
                    ch_v "Of course there's a mall! What town doesn't have a mall?!"
                "Did you want to go?":
                    call change_Girl_stat(JubesX, "love", 2)
                    call change_Girl_stat(JubesX, "love", 1)
                    call change_Girl_stat(JubesX, "inhibition", 1)
        "Oh, ok.":
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "obedience", 1)
            $ JubesX.change_face("sad")
        "Wait, there's a mall?":
            call change_Girl_stat(JubesX, "love", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("confused")
            ch_v "Of course there's a mall! What town doesn't have a mall?!"
        "Ok, whatever.":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "obedience", 2)
            call change_Girl_stat(JubesX, "obedience", 2)
            call change_Girl_stat(JubesX, "inhibition", -1)
    $ JubesX.change_face("surprised", 1, mouth = "sucking")
    ch_v "We've got to go there, right now!"
    $ JubesX.change_face("smile")
    $ Player.Party = [JubesX]
    menu:
        "Ok, let's check it out.":
            call change_Girl_stat(JubesX, "love", 2)
            call change_Girl_stat(JubesX, "love", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
        "You can go, I don't need anything.":
            call change_Girl_stat(JubesX, "love", 2)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "obedience", 1)
            ch_v "Come'on, you gotta go!"
            ch_v "You don't know what you're missing!"
            show black_screen onlayer black
            pause 1.0
            "[JubesX.name] can be surprisingly forceful. . ."
        "Nah.":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "inhibition", 2)
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("angry", 1, mouth = "sucking")
            ch_v "Stow the 'tude, we're going!"
            $ JubesX.change_face("smile")
            show black_screen onlayer black
            pause 1.0
            "[JubesX.name] can be surprisngly forceful. . ."
        "Actually, I planned to-":
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("surprised", 1, mouth = "sucking")
            ch_v "No time! We're going!"
            $ JubesX.change_face("smile")
            show black_screen onlayer black
            pause 1.0
            "[JubesX.name] can be surprisngly forceful. . ."

    call set_the_scene(location = "bg_mall", fade = True)

    "You arrive at what appears to be a mid-sized suburban shopping complex, often referred to as a \"mall.\""

    $ JubesX.change_face("smile")
    ch_v "Welcome to the Salem Centre Mall!"
    ch_v "It's open dawn to dusk, which is why I wasn't able to get here for a while. . ."
    ch_v "It's got a -ton- of different shops, although I guess not all of them would be very interesting to you."

    python:
        line = False

        for G in all_Girls:
            if G.went_on_date:
                line = True

                break

    if line:

        "You realize that the local movie theater is actually at one end of the mall."
        "And the restaurant you often go to is at the other end."
        "How did you not notice the mall in between before? . ."
        menu:
            "Selective amnesia":
                "Oh, yeah, probably."
            "I'm not very bright":
                "True, true."
            "Probably a retcon":
                "It happens."
    else:

        "You see a movie theater is at one end of the mall, and a nice looking restaurant is at the other end."
        "Maybe you should take people to these places. . ."
    ch_v "And you haven't been here before?"
    menu:
        extend ""
        "Apparently not.":
            pass
        "I think I've been close. . .":
            pass
        "Nope.":
            call change_Girl_stat(JubesX, "love", -1)
    $ JubesX.change_face("confused", 1)
    ch_v "Weird."
    ch_v "Anyway, I spent a -ton- of time at the mall when I was a kid."
    $ JubesX.change_face("sadside")
    ch_v "I'd run away from foster care, and just camped out in closed stores. . ."
    ch_v "It was better than being on the street, at least."
    menu:
        extend ""
        "That's rough.":
            call change_Girl_stat(JubesX, "love", 3)
            call change_Girl_stat(JubesX, "love", 1)
            call change_Girl_stat(JubesX, "obedience", 1)
        "That must have been hard for you.":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "love", 3)
            call change_Girl_stat(JubesX, "love", 1)
        "I guess.":
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("confused", 1)
            ch_v ". . ."
        "Free food court, uh?":
            call change_Girl_stat(JubesX, "love", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("smile", 1, eyes = "side")
            ch_v "When I could get into a restaurant, yeah. . ."
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "obedience", 1)
            $ JubesX.change_face("angry", 1)
            ch_v ". . ."

    ch_v "Yeah, but it was ok. . ."
    $ JubesX.change_face("smile", eyes = "side")
    ch_v "Anyway, then I bumped into some of the other Xavier's students and found my way to the school."
    $ JubesX.change_face("smile")
    ch_v "Xavier agreed to take me in there, and it's worked out much better."
    $ JubesX.change_face("sadside")
    ch_v "Until the whole \"vampire\" thing at least."
    menu:
        "Yeah, about that. . .":
            call change_Girl_stat(JubesX, "obedience", 1)
            call change_Girl_stat(JubesX, "obedience", 1)
        "Yeah, I bet.":
            call change_Girl_stat(JubesX, "love", 2)
        "Uh-huh.":
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "obedience", 1)
            $ JubesX.change_face("angry")
            ch_v ". . ."
    $ JubesX.change_face("smile")
    ch_v "So anyways. . . now that we're here, did you want to go shopping?"
    menu:
        "Sure, let's look around.":
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "love", 3)
            call change_Girl_stat(JubesX, "love", 1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            ch_v "Cool."
            jump mall
        "Nah, we can head back now.":
            call change_Girl_stat(JubesX, "love", -3)
            call change_Girl_stat(JubesX, "love", -2)
            call change_Girl_stat(JubesX, "love", -1)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("sad")
            ch_v "Aw, ok. At least I can come here when I want now. . ."
            call change_Girl_stat(JubesX, "obedience", 3)
            call change_Girl_stat(JubesX, "obedience", 2)

    "You both head back to campus."

    call set_the_scene(location = "bg_campus")

    ch_v "Anyway, it was nice to hang out with you."
    ch_v "I hope we can do it again some time!"

    $ Player.Party = []

    jump reset_location

    return



label Jubes_Key:
    call set_the_scene
    $ JubesX.change_face("bemused")
    ch_v "Oh, um. . ."
    ch_v "We've been sleeping together for a bit and. . ."
    ch_v "Here."
    "She takes your hand and hands you her room key."
    $ Player.Keys.append(JubesX)
    $ JubesX.event_happened[0] = 1
    ch_p "Thanks."
    return






label Jubes_BF(temp_Girls = []):
    $ shift_focus (JubesX)
    if JubesX.location != Player.location:
        if JubesX not in Player.Party:
            "[JubesX.name] approaches you and motions that she wants to speak to you alone."
        else:
            "[JubesX.name] turns towards you and motions that she wants to speak to you alone."

    $ JubesX.drain_word("asked_to_meet")

    call clear_the_room(JubesX, passive = True, silent = True)

    "She looks a bit concerned and you can tell she's a bit anxious about whatever she has to say."
    call set_Character_taboos
    call clear_the_room (JubesX)
    $ JubesX.daily_history.append("relationship")
    $ JubesX.change_face("angry", 1, eyes = "side")
    $ line = 0
    ch_v "Hey. So. [JubesX.player_petname]. . ."
    $ JubesX.change_face("confused", 1, mouth = "lipbite")
    ch_v "I don't know- . . . you're pretty fun to hang out with, ya know?"
    menu:
        extend ""
        "I really love hanging out with you too!":
            $ JubesX.change_face("surprised", 2)
            ch_v "Right, so-"
            call change_Girl_stat(JubesX, "obedience", -3)
            call change_Girl_stat(JubesX, "inhibition", 1)
            ch_v ". . ."
            call change_Girl_stat(JubesX, "love", 5)
            $ JubesX.change_face("bemused", 1, eyes = "side")
            ch_v "\"Love\" is kind of a strong word, [JubesX.player_petname]."
        "Yeah, sure, it's a lot of fun.":
            call change_Girl_stat(JubesX, "love", 10)
            call change_Girl_stat(JubesX, "inhibition", 2)
            $ JubesX.change_face("smile", 0)
            ch_v "Right?"
        "I mean, it beats math class. . .":
            call change_Girl_stat(JubesX, "love", 3)
            call change_Girl_stat(JubesX, "obedience", 3)
            call change_Girl_stat(JubesX, "inhibition", -3)
            $ JubesX.change_face("angry", 1)
            ch_v "Um, less enthusiasm than I was expecting. . ."
        "If you say so.":
            call change_Girl_stat(JubesX, "obedience", 6)
            call change_Girl_stat(JubesX, "inhibition", -8)
            $ JubesX.change_face("confused", 1)
            ch_v ". . ."

    ch_v "So like I was saying, I don't exactly have a ton of friends."
    $ JubesX.change_face("sadside", 1)
    ch_v "I kind of grew up in a rough place, and then spent a lot of time on the road."
    ch_v "I had a life before coming here."
    menu:
        extend ""
        "What was it like?":
            call change_Girl_stat(JubesX, "love", 7)
            call change_Girl_stat(JubesX, "obedience", 2)
            call change_Girl_stat(JubesX, "inhibition", 3)
            $ JubesX.change_face("sad", 1, mouth = "lipbite")
        "Yeah? I know.":
            call change_Girl_stat(JubesX, "love", 3)
            call change_Girl_stat(JubesX, "obedience", 4)
            call change_Girl_stat(JubesX, "inhibition", 1)
            $ JubesX.change_face("confused", 1, mouth = "lipbite")
        "I don't need a lot of backstory drama.":
            call change_Girl_stat(JubesX, "love", -5)
            call change_Girl_stat(JubesX, "obedience", 10)
            call change_Girl_stat(JubesX, "inhibition", -5)
            $ JubesX.change_face("angry", 1)
            $ line = "bad"
            ch_v "Fine!"
            ch_v "\"Keep it simple\" it is then."
            ch_v "I don't hate hanging out with you, is all."
    if line != "bad":
        $ JubesX.change_face("normal", 1, eyes = "side")
        ch_v "Well, you may have guessed I'm related to Wolverine."
        menu:
            extend ""
            "Kinda obvious, yeah.":
                call change_Girl_stat(JubesX, "love", 4)
            "I had no idea!":
                call change_Girl_stat(JubesX, "love", 3)
                call change_Girl_stat(JubesX, "inhibition", 1)
                $ JubesX.change_face("confused", 1)
            "Duh.":
                call change_Girl_stat(JubesX, "love", 1)
                call change_Girl_stat(JubesX, "obedience", 2)
                $ JubesX.change_face("angry", 1)
        ch_v "Well I'm actually his partial clone."
        $ JubesX.change_face("angry", 1, eyes = "side")
        ch_v "I was created to be some sort of biological weapon, an assassin."
        ch_v "I did a lot of work for them as a kid, until eventually I escaped."
        $ JubesX.change_face("sadside", 1)
        ch_v "After that, I had to do a lot of stuff. . . to stay alive."
        ch_v "Stuff I'm not proud of."
        $ JubesX.change_face("sad", 1)
        ch_v "But I don't know. . . being around you, I think it helps."
        $ JubesX.change_face("sad", 1, mouth = "smile")
        ch_v "I kind of feel. . . better."
    if JubesX.SEXP >= 20:
        call change_Girl_stat(JubesX, "obedience", 3)
        call change_Girl_stat(JubesX, "inhibition", 2)
        call change_Girl_stat(JubesX, "lust", 5)
        $ JubesX.change_face("sly", 1)
        ch_v "You really are good in bed, after all."
    if len(Player.Harem) >= 2:
        ch_v "And I know that you have your share of other girls. . ."
        ch_v ". . . but I'd still like to be a part of your life."
    elif Player.Harem:
        ch_v "And I know you're with someone else. . ."
        ch_v ". . . but I'd still like to be a part of your life."
    else:
        ch_v "I'd just like to be a part of your life."
    $ JubesX.change_face("sad", 1, mouth = "smile")
    ch_v "That's it."
    $ JubesX.event_happened[5] += 1
    menu:
        extend ""
        "Yeah! I really love you.":
            call change_Girl_stat(JubesX, "love", -3)
            call change_Girl_stat(JubesX, "obedience", -3)
            call change_Girl_stat(JubesX, "inhibition", 3)
            $ JubesX.change_face("surprised", 1)
            ch_v "Whoa!"
            $ JubesX.change_face("perplexed")
            ch_v "Maybe cool your jets there, [JubesX.player_petname]."
            $ JubesX.change_face("smile", eyes = "side")
            ch_v "I wasn't. . ."
            ch_v "I don't think we're there. . ."
            $ JubesX.change_face("perplexed", 1)
            ch_v "Right?"
            menu:
                extend ""
                "Maybe you aren't.":
                    call change_Girl_stat(JubesX, "love", 10)
                    call change_Girl_stat(JubesX, "obedience", 5)
                    call change_Girl_stat(JubesX, "inhibition", 5)
                    call change_Girl_stat(JubesX, "lust", 2)
                    $ JubesX.change_face("smile", 1, eyes = "side")
                    ch_v "Hehe. . . um."
                "I guess, sure.":
                    call change_Girl_stat(JubesX, "love", 6)
                    call change_Girl_stat(JubesX, "obedience", 3)
                    call change_Girl_stat(JubesX, "inhibition", 2)
                    $ JubesX.change_face("angry", 1, eyes = "side", mouth = "lipbite")
                    ch_v "Right, so. . ."
        "Yeah, I think that'd be great.":

            call change_Girl_stat(JubesX, "love", 6)
            call change_Girl_stat(JubesX, "obedience", 2)
            call change_Girl_stat(JubesX, "inhibition", 3)
            $ JubesX.change_face("smile", 1, eyes = "side")
            ch_v "Cool."
        "Hmm? Ok.":
            call change_Girl_stat(JubesX, "love", 3)
            call change_Girl_stat(JubesX, "obedience", 5)
            call change_Girl_stat(JubesX, "inhibition", 3)
            $ JubesX.change_face("confused", 1, eyes = "side")
            ch_v "Yeah. . . cool."
        "I'm not really into that.":
            call change_Girl_stat(JubesX, "love", -5)
            call change_Girl_stat(JubesX, "obedience", 5)
            call change_Girl_stat(JubesX, "inhibition", -5)
            $ JubesX.change_face("sad", 1)
            if len(Player.Harem) >= 2:
                ch_v "Is it because of [Player.Harem[0].name] and the rest?"
            elif Player.Harem:
                ch_v "Is it because of [Player.Harem[0].name]?"
            else:
                ch_v "Why not? What's the deal?"
            menu:
                extend ""
                "Yeah, I don't think she'd understand." if len(Player.Harem) == 1:
                    call change_Girl_stat(JubesX, "love", -5)
                    call change_Girl_stat(JubesX, "obedience", 7)
                    $ JubesX.change_face("angry", 1, eyes = "side")
                    $ JubesX.check_if_likes(Player.Harem[0],800, -20, 1)
                    ch_v "That bitch."
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    call change_Girl_stat(JubesX, "love", -5)
                    call change_Girl_stat(JubesX, "obedience", 7)
                    $ JubesX.change_face("angry", 1, eyes = "side")
                    call change_Harem_stat (JubesX, 700, -20)
                    ch_v "Bitches."
                "It's. . . complicated.":
                    call change_Girl_stat(JubesX, "love", -20)
                    call change_Girl_stat(JubesX, "obedience", 8)
                    call change_Girl_stat(JubesX, "inhibition", -5)
                    $ JubesX.change_face("angry", 1)
                    ch_v "Complicated. Sure. Whatever."
                    $ JubesX.change_face("angry", 1, eyes = "side")
                    if len(Player.Harem) >= 2:
                        ch_v "Probably those bitches."
                        call change_Harem_stat (JubesX, 700, -10)
                    elif Player.Harem:
                        ch_v "Probably because of her."
                        $ JubesX.check_if_likes(Player.Harem[0],800, -20, 1)
                    $ line = "no"
                "I'm just not into you like that.":
                    call change_Girl_stat(JubesX, "love", -10)
                    $ JubesX.change_face("surprised", 1)
                    ch_v "Oh."
                    call change_Girl_stat(JubesX, "obedience", 10)
                    call change_Girl_stat(JubesX, "inhibition", 5)
                    $ JubesX.change_face("sadside", 1)
                    ch_v "Ok, I guess I can respect that."


            $ JubesX.change_face("sad", 1)
            if line != "no":
                ch_v "We're still cool though."
            ch_v "I should. . . leave."
            "[JubesX.name] wanders off in a bit of a daze."
            $ JubesX.event_happened[5] = 20
            call remove_Girl(JubesX)
            $ line = 0
            return

    if Player.Harem:
        if not approval_check(JubesX, 1400):
            if len(Player.Harem) >= 2:
                ch_v "So you'll break up with the others?"
            else:
                ch_v "So you'll break up with [Player.Harem[0].name]?"
            menu:
                extend ""
                "Yes, you're worth it.":
                    call change_Girl_stat(JubesX, "love", 20)
                    call change_Girl_stat(JubesX, "obedience", 5)
                    call change_Girl_stat(JubesX, "inhibition", 5)
                    $ JubesX.change_face("surprised", 2, mouth = "smile")
                    ch_v ". . ."
                    $ JubesX.change_face("smile", 1)

                    $ JubesX.event_happened[5] = 10
                "I'd rather you join us.":
                    $ line = 0
                    if approval_check(JubesX, 1200):

                        $ temp_Girls = Player.Harem[:]
                        while temp_Girls and line != "no":

                            if JubesX.likes[temp_Girls[0].tag] <= 500:
                                $ line = "no"
                            $ temp_Girls.remove(temp_Girls[0])
                    else:
                        $ line = "no"
                    if line == "no":
                        call change_Girl_stat(JubesX, "love", -10)
                        call change_Girl_stat(JubesX, "obedience", 10)
                        $ JubesX.change_face("angry", 1)
                        call change_Harem_stat (JubesX, 700, -10)
                        ch_v "Eh, I'll pass."
                    else:
                        call change_Girl_stat(JubesX, "love", 200, 5)
                        call change_Girl_stat(JubesX, "obedience", 15)
                        call change_Girl_stat(JubesX, "inhibition", 10)
                        $ JubesX.change_face("bemused", 1)
                        ch_v "Well, I s'pose that wouldn't be so terrible."
                "What? Of course not.":
                    call change_Girl_stat(JubesX, "love", -25)
                    call change_Girl_stat(JubesX, "obedience", 5)
                    call change_Harem_stat (JubesX, 700, -20)
                    $ JubesX.change_face("angry", 1)
                    ch_v "Well, fine then."
                    $ line = "no"
            if line == "no":
                $ JubesX.event_happened[5] = 20
                call remove_Girl(JubesX)
                $ line = 0
                return



        if len(Player.Harem) >= 2:
            ch_v "And you don't think the others would mind?"
        else:
            ch_v "And you don't think [Player.Harem[0].name] would mind?"
        menu:
            extend ""
            "No, actually they're fine with it." if "JubesYes" in Player.traits:
                call change_Girl_stat(JubesX, "love", 5)
                call change_Girl_stat(JubesX, "obedience", 10)
                call change_Girl_stat(JubesX, "inhibition", 5)
                $ JubesX.change_face("surprised", 1)
                ch_v "Oh, cool."
            "Actually. . . I guess we'll need to work on that one." if "JubesYes" not in Player.traits:
                call change_Girl_stat(JubesX, "love", 3)
                call change_Girl_stat(JubesX, "obedience", 3)
                call change_Girl_stat(JubesX, "inhibition", 1)
                call change_Girl_stat(JubesX, "lust", 1)
                $ JubesX.change_face("confused", 1)
                ch_v "Hmm, get back to me, I guess?"
                $ JubesX.event_happened[5] = 20
                call remove_Girl(JubesX)
                $ line = 0
                return
        call change_Harem_stat (JubesX, 900, 20)


    if not simulation:
        $ Player.Harem.append(JubesX)
        if "JubesYes" in Player.traits:
            $ Player.traits.remove("JubesYes")
        $ JubesX.player_petnames.append("boyfriend")
        call Harem_Initiation
    call change_Girl_stat(JubesX, "love", 3)
    call change_Girl_stat(JubesX, "obedience", 3)
    call change_Girl_stat(JubesX, "inhibition", 1)
    call change_Girl_stat(JubesX, "lust", 1)
    $ JubesX.change_face("sly", 1)
    ch_v "So, did you have any plans for the next few minutes? . ."
    if simulation:
        return True
    $ approval_bonus = 10
    $ Player.add_word(1, "interruption")
    call enter_main_sex_menu(JubesX)
    $ approval_bonus = 0

    return

label Jubes_Cleanhouse:

    $ JubesX.drain_word("asked_to_meet")
    if "cleanhouse" in JubesX.to_do:
        $ JubesX.to_do.remove("cleanhouse")
    if not Player.Harem or JubesX in Player.Harem:
        $ JubesX.event_happened[5] = 2
        return

    if JubesX.location == Player.location or JubesX in Player.Party:
        "[JubesX.name] glances over at you with a scowl."
    else:
        "[JubesX.name] turns a corner and notices you."
    if Player.location != "bg_jubes" and Player.location != "bg_player":
        "With little word, she moves behind you and pushes you towards her room."
        $ Player.location = "bg_jubes"

    call set_the_scene
    call clear_the_room (JubesX)
    call set_the_scene
    call set_Character_taboos
    $ JubesX.daily_history.append("relationship")
    call change_Girl_stat(JubesX, "love", -20)
    $ JubesX.change_face("angry", 1)
    ch_v "What's the deal, [Player.player_petname]?"
    ch_v "It's been a week already, and you're still dating [Player.Harem[0].name]!"
    if len(Player.Harem) >= 2:
        ch_v "Not to mention the rest of them!"
    menu:
        extend ""
        "Sorry about that, I'm sticking with them":
            call change_Girl_stat(JubesX, "love", -5)
            call change_Girl_stat(JubesX, "obedience", 5)
            call change_Girl_stat(JubesX, "inhibition", 5)
            $ JubesX.change_face("angry", 2)
            ch_v "You asshole."
            $ JubesX.change_face("sadside", 1)
            ch_v "You could have at least been honest about it."
        "Must have slipped my mind":
            call change_Girl_stat(JubesX, "love", -10)
            call change_Girl_stat(JubesX, "obedience", 10)
            ch_v "!"
            ch_v "Seriously dude? That's all you've got?"
        "[[shrug]":
            call change_Girl_stat(JubesX, "love", -20)
            call change_Girl_stat(JubesX, "obedience", 10)
            call change_Girl_stat(JubesX, "inhibition", 10)
            $ JubesX.blushing = "_blush2"

            call show_Girl(JubesX, transition = vpunch)

            "She clocks you one."
            "That was fair."
            $ JubesX.blushing = "_blush1"

    ch_v "I can't believe you're putting me through this."
    ch_v "Making me choose between you and putting up with this whole arrangement."
    $ line = 0
    if approval_check(JubesX, 1400) and approval_check(JubesX, 600, "O"):

        pass
    elif approval_check(JubesX, 1200) and approval_check(JubesX, 500, "O"):

        $ temp_Girls = Player.Harem[:]
        while temp_Girls and line != "no":

            if JubesX.likes[temp_Girls[0].tag] <= 400:
                $ line = "no"
            $ temp_Girls.remove(temp_Girls[0])
    else:
        $ line = "no"
    if line == "no":
        call change_Girl_stat(JubesX, "love", -10)
        call change_Girl_stat(JubesX, "obedience", 10)
        $ JubesX.change_face("angry", 1)
        call change_Harem_stat (JubesX, 700, -15)
        ch_v "No, this is bullshit, never mind."
    else:
        call change_Girl_stat(JubesX, "love", 5)
        call change_Girl_stat(JubesX, "obedience", 20)
        call change_Girl_stat(JubesX, "inhibition", 10)
        $ JubesX.change_face("angry", 1, eyes = "side")
        ch_v "Ok, fine, whatever. I'm in too."
        if not simulation:
            $ Player.Harem.append(JubesX)
            if "JubesYes" in Player.traits:
                $ Player.traits.remove("JubesYes")
            $ JubesX.player_petnames.append("boyfriend")
            call Harem_Initiation
            call change_Harem_stat (JubesX, 900, 20)
            $ JubesX.event_happened[5] = 20
    return





label Jubes_Sub:
    $ JubesX.drain_word("asked_to_meet")
    $ shift_focus (JubesX)
    if JubesX.location != Player.location and JubesX not in Player.Party:
        "Suddenly, [JubesX.name] shows up and says she needs to talk to you."

    call clear_the_room (JubesX)

    $ JubesX.daily_history.append("relationship")
    $ JubesX.change_face("bemused", 1)

    $ line = 0
    ch_v "I've noticed something."
    ch_v "You've been trying to boss me around lately."
    menu:
        ch_v "I've noticed you trying to boss me around.{w=2.8}{nw}"
        "I guess. That's just kind of what comes naturally for me.":
            pass
        "Sorry. I didn't mean to come off like that.":
            pass
        "Yup. Deal with it.":
            pass
    "Before you can speak, she puts her hand over your mouth."
    $ JubesX.change_face("sly", 1, eyes = "side")
    ch_v "I don't know how I feel about that."
    if JubesX.event_happened[6]:
        $ JubesX.change_face("sadside", 1)
        ch_v "You know the past I've had, with the facility, with the. . . "
        ch_v ". . . work I had to do for them."
        $ JubesX.change_face("sad", 1)
        ch_v "I don't know if I want to let anyone tell me what to do like that again."
    menu Jubes_Sub_Question:
        extend ""
        "I guess I can be demanding.":
            $ JubesX.change_face("sly", 1)
            call change_Girl_stat(JubesX, "obedience", 10)
            call change_Girl_stat(JubesX, "inhibition", 5)
        "Sorry. I didn't mean to come off like that.":
            $ JubesX.change_face("sly", 1)
            call change_Girl_stat(JubesX, "love", 5)
            call change_Girl_stat(JubesX, "obedience", -5)
            call change_Girl_stat(JubesX, "inhibition", -5)
            ch_v "I get it, you're assertive. . ."
        "Remind me about the facility?" if JubesX.event_happened[6] and line != "facility":
            $ JubesX.change_face("sadside", 1)
            call change_Girl_stat(JubesX, "love", -10)
            call change_Girl_stat(JubesX, "inhibition", -5)
            ch_v "I told you, I was raised in an underground government lab."
            ch_v "They ordered me to kill people for them."
            $ JubesX.change_face("sly", 0, brows= "angry")
            ch_v ". . . until I got tired of taking orders."
            $ line = "facility"
            jump Jubes_Sub_Question
        "What bothers you about being told to do things?" if not JubesX.event_happened[6] and line != "facility":
            $ JubesX.change_face("sadside", 1)
            call change_Girl_stat(JubesX, "love", 5)
            ch_v "I've just had some rough experiences."
            ch_v "You don't need to know about them."
            ch_v ". . ."
            $ JubesX.change_face("sad", 0)
            ch_v "Let's just say I was ordered to do some things I regret."
            $ line = "facility"
            jump Jubes_Sub_Question
        "Get with the program.":
            if approval_check(JubesX, 1000, "LO"):
                $ JubesX.change_face("sly", 1)
                call change_Girl_stat(JubesX, "obedience", 20)
                call change_Girl_stat(JubesX, "inhibition", 10)
                ch_v "Hmmm. . ."
            else:
                call change_Girl_stat(JubesX, "love", -10)
                call change_Girl_stat(JubesX, "inhibition", -5)
                $ JubesX.change_face("angry", 0)
                ch_v "You're not off to a good start here. You might want to rethink your attitude."
                menu:
                    extend ""
                    "Sorry. I thought that's what you were into.":
                        $ JubesX.change_face("perplexed", 1, eyes = "side")
                        $ JubesX.eyes = "side"
                        call change_Girl_stat(JubesX, "love", 10)
                        call change_Girl_stat(JubesX, "obedience", 5)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        ch_v ". . . after I just said. . ."
                        $ JubesX.change_face("sly", 1)
                        ch_v "Ok, whatever."
                    "I don't care.":
                        call change_Girl_stat(JubesX, "love", -10)
                        ch_v "I guess not."
                        $ line = "rude"
    if line == "facility":
        $ line = 0

    if not line:

        $ JubesX.change_face("sly", 1)
        ch_v "Look, it's not like. . ."
        $ JubesX.change_face("sly", 2)
        ch_v ". . . it's not like I hate it."
        $ JubesX.change_face("smile", 1, eyes = "side")
        ch_v ". . . I actually think it might make me. . ."
        menu:
            extend ""
            "-excited?":
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", 5)
                ch_v ". . ."
                $ JubesX.change_face("sly", 1)
                call change_Girl_stat(JubesX, "lust", 10)
                ch_v "a little, yeah."
            "-digusted?":
                call change_Girl_stat(JubesX, "love", -5)
                call change_Girl_stat(JubesX, "obedience", -5)
                $ JubesX.change_face("sadside", 1)
                ch_v ". . . kind of, "
                $ JubesX.change_face("sly", 1)
                call change_Girl_stat(JubesX, "inhibition", 5)
                call change_Girl_stat(JubesX, "lust", 5)
                ch_v "but also kind of excited by it."
            "-hungry?":
                $ JubesX.change_face("confused", 1, eyes = "surprised", mouth = "smile")
                call change_Girl_stat(JubesX, "obedience", -5)
                call change_Girl_stat(JubesX, "inhibition", -5)
                ch_v "?!"
                $ JubesX.change_face("confused", 1, eyes = "normal", mouth = "smile")
                ch_v "Well. . . yeah? But not for-"
                $ JubesX.change_face("sly", 1)
                call change_Girl_stat(JubesX, "lust", 5)
                ch_v "I mean, it makes me kind of. . . excited."
            "-horny?":
                call change_Girl_stat(JubesX, "obedience", 10)
                call change_Girl_stat(JubesX, "inhibition", 5)
                $ JubesX.change_face("startled", 2, mouth = "lipbite")
                ch_v "!"
                $ JubesX.change_face("sly", 1, eyes = "side")
                call change_Girl_stat(JubesX, "inhibition", 5)
                call change_Girl_stat(JubesX, "lust", 10)
                call change_Girl_stat(JubesX, "lust", 5)
                ch_v "Yes."
        menu:
            extend ""
            "Good. If you wanna be with me, then you follow my orders.":
                if approval_check(JubesX, 1000, "LO"):
                    $ JubesX.change_face("sly", 1)
                    call change_Girl_stat(JubesX, "obedience", 15)
                    call change_Girl_stat(JubesX, "inhibition", 10)
                    ch_v "Hmmm. . ."
                else:
                    $ JubesX.change_face("sadside", 1, mouth = "normal")
                    call change_Girl_stat(JubesX, "love", -5)
                    call change_Girl_stat(JubesX, "obedience", 10)
                    ch_v "You might want to slow your roll there, [JubesX.player_petname]."
                    menu:
                        extend ""
                        "Whatever. That's how it is. Take it or leave it.":
                            $ JubesX.change_face("angry")
                            call change_Girl_stat(JubesX, "love", -10)
                            call change_Girl_stat(JubesX, "obedience", 5)
                            ch_v "I think you're pushing it too far there, [JubesX.player_petname]."
                            $ line = "rude"
                        "Ok, just a little.":
                            $ JubesX.change_face("bemused", 1)
                            call change_Girl_stat(JubesX, "love", 5)
                            call change_Girl_stat(JubesX, "inhibition", 5)
                            ch_v "-but not too much."
            "Yeah? You think it's sexy?":

                $ JubesX.change_face("bemused", 2, eyes = "side")
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", 10)
                ch_v ". . ."
                call change_Girl_stat(JubesX, "lust", 5)
                ch_v "Yeah."
            "You sure you don't want me to back off a little?":

                $ JubesX.change_face("startled", 1, eyes = "squint")
                call change_Girl_stat(JubesX, "obedience", -5)
                menu:
                    ch_v "Well if you have to ask. . ."
                    "Only if you're okay with it.":
                        $ JubesX.change_face("bemused", 1)
                        call change_Girl_stat(JubesX, "love", 10)
                        call change_Girl_stat(JubesX, "inhibition", 10)
                        $ line = 0
                    "Uhm. . .yeah. I think it's weird. Sorry.":
                        $ JubesX.change_face("sad", 1, eyes = "surprised")
                        call change_Girl_stat(JubesX, "love", -15)
                        call change_Girl_stat(JubesX, "obedience", -5)
                        call change_Girl_stat(JubesX, "inhibition", -10)
                        $ line = "embarrassed"
            "I couldn't care less.":

                call change_Girl_stat(JubesX, "love", -10)
                call change_Girl_stat(JubesX, "obedience", 15)
                $ JubesX.change_face("angry")
                ch_v "I think you're pushing it too far there, [JubesX.player_petname]."
                $ line = "rude"

    if not line:
        $ JubesX.change_face("bemused", 1, eyes = "down")
        ch_v "So, I'm willing to give this a shot."
        ch_v "Just a trial period, to see how it goes."
        ch_v "Just tell me what you want, and. . . I'll see about doing it."
        menu Jubes_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                call change_Girl_stat(JubesX, "obedience", 5)
                call change_Girl_stat(JubesX, "inhibition", 5)
                $ JubesX.change_face("sly", 1)
                $ line = 0
            "Don't you think that relationship's kinda. . .weird?":
                $ JubesX.change_face("sad", 1, eyes = "surprised")
                call change_Girl_stat(JubesX, "love", -5)
                call change_Girl_stat(JubesX, "inhibition", -15)
                $ line = "embarrassed"

    if not line:
        $ JubesX.change_face("smile", 1)
        ch_v "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                call change_Girl_stat(JubesX, "love", 5)
                call change_Girl_stat(JubesX, "obedience", 15)
                call change_Girl_stat(JubesX, "inhibition", 5)
                ch_v "Yes, sir."
                $ JubesX.player_petname = "sir"
            "That's kind of formal, isn't it?":
                $ JubesX.change_face("perplexed", 1)
                ch_v "Huh. ok, no problem"
                call change_Girl_stat(JubesX, "inhibition", -5)
                $ JubesX.change_face("sly", 1, eyes = "side")
                menu:
                    ch_v "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                        call change_Girl_stat(JubesX, "obedience", 10)
                        $ JubesX.change_face("smile", 1)
                        ch_v "Good."
                    "I don't feel comfortable with that. . .":
                        $ JubesX.change_face("sad", 1, eyes = "side")
                        call change_Girl_stat(JubesX, "love", -10)
                        call change_Girl_stat(JubesX, "obedience", -30)
                        call change_Girl_stat(JubesX, "inhibition", -15)
                        $ line = "embarrassed"


    $ JubesX.history.append("sir")
    if not line:
        $ JubesX.player_petnames.append("sir")

    elif line == "rude":
        call remove_Girl(JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] knocks her way past you and storms off."
    elif line == "embarrassed":
        $ JubesX.change_face("sadside", 2)
        ch_v "Huh, ok, if you're not interested. . ."

        call remove_Girl(JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] heads out of the room."
    return

label Jubes_Sub_Asked:
    $ line = 0
    $ JubesX.change_face("sadside", 1)
    ch_v "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in JubesX.player_petnames and approval_check(JubesX, 850, "O"):

                pass
            elif approval_check(JubesX, 550, "O"):

                pass
            else:
                $ JubesX.change_face("angry", 1)
                ch_v "It was a bad idea, don't worry about it."
                $ line = "rude"

            if line != "rude":
                call change_Girl_stat(JubesX, "love", 10)
                $ JubesX.change_face("sly", 1)
                ch_v "Well, it's not like you stopped ordering me around anyway."
                ch_v "Ok, let's give it a shot."
        "I know it's what you want. Do you want to try again, or not?":

            $ JubesX.change_face("bemused", 1)
            if "sir" in JubesX.player_petnames:
                if approval_check(JubesX, 850, "O"):
                    ch_v "Ok, fine."
                else:
                    ch_v "Nah, I'm good."
                    $ line = "rude"
            elif approval_check(JubesX, 600, "O"):

                $ JubesX.change_face("confused", 1)
                ch_v "Kinda wishy-washy there."
                $ JubesX.change_face("sly", 1)
                ch_v "but maybe you're right."
                ch_v "Are you sure you're into this?"
                menu:
                    extend ""
                    "Yes, I'm sorry I was mean about it.":
                        call change_Girl_stat(JubesX, "love", 15)
                        call change_Girl_stat(JubesX, "inhibition", 10)
                        $ JubesX.change_face("bemused", 1)
                        $ JubesX.eyes = "side"
                        ch_v "Ok then."
                    "You're damned right I am, bitch.":
                        if "sir" in JubesX.player_petnames and approval_check(JubesX, 900, "O"):
                            call change_Girl_stat(JubesX, "love", -5)
                            call change_Girl_stat(JubesX, "obedience", 10)
                            ch_v ". . ."
                        elif approval_check(JubesX, 700, "O"):
                            call change_Girl_stat(JubesX, "love", -5)
                            call change_Girl_stat(JubesX, "obedience", 10)
                            ch_v "Hmmm. . ."
                        else:
                            call change_Girl_stat(JubesX, "love", -10)
                            call change_Girl_stat(JubesX, "obedience", -10)
                            call change_Girl_stat(JubesX, "obedience", -10)
                            call change_Girl_stat(JubesX, "inhibition", -15)
                            $ JubesX.change_face("angry", 1)
                            ch_v "Wow, that's pushing it."
                            $ line = "rude"
                    "Ok, never mind then.":
                        $ JubesX.change_face("angry", 1)
                        call change_Girl_stat(JubesX, "love", -10)
                        call change_Girl_stat(JubesX, "obedience", -10)
                        call change_Girl_stat(JubesX, "obedience", -10)
                        call change_Girl_stat(JubesX, "inhibition", -15)
                        ch_v "I was thinking of taking orders from you, not mindgames."
                        ch_v "I should've known you'd be like this."
                        $ line = "rude"

    $ JubesX.recent_history.append("asked sub")
    $ JubesX.daily_history.append("asked sub")
    if line == "rude":


        call remove_Girl(JubesX)
        $ JubesX.recent_history.append("angry")
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] checks you as she stomps out of the room."
    elif "sir" in JubesX.player_petnames:

        call change_Girl_stat(JubesX, "obedience", 50)
        $ JubesX.player_petnames.append("master")
        $ JubesX.player_petname = "master"
        $ JubesX.eyes = "squint"
        ch_v ". . . master. . ."
    else:

        call change_Girl_stat(JubesX, "obedience", 30)
        $ JubesX.player_petnames.append("sir")
        $ JubesX.player_petname = "sir"
        $ JubesX.change_face("sly", 1)
        ch_v ". . . sir."
    return






label Jubes_Master:
    $ JubesX.drain_word("asked_to_meet")
    $ shift_focus (JubesX)
    if JubesX.location != Player.location and JubesX not in Player.Party:
        "Suddenly, [JubesX.name] shows up and says she needs to talk to you."

    call clear_the_room (JubesX)

    $ JubesX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ JubesX.change_face("sly", 1)
    ch_v "[JubesX.player_petname]. . ."
    ch_v ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            call change_Girl_stat(JubesX, "obedience", 5)
            call change_Girl_stat(JubesX, "inhibition", 5)
        "What?":
            ch_v "I was asking if I could talk to you about something. . ."
            $ JubesX.eyes = "side"
            ch_v ". . . personal."
            $ JubesX.eyes = "squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    call change_Girl_stat(JubesX, "love", 5)
                    call change_Girl_stat(JubesX, "obedience", 5)
                    ch_v "Right. . ."
                "Oh, then no.":
                    $ JubesX.change_face("sad", 1)
                    call change_Girl_stat(JubesX, "love", -5)
                    call change_Girl_stat(JubesX, "obedience", -10)
                    $ line = "embarrassed"
        "No.":
            $ JubesX.change_face("perplexed", 1, brows = "confused")
            call change_Girl_stat(JubesX, "love", -5)
            call change_Girl_stat(JubesX, "obedience", -5)
            call change_Girl_stat(JubesX, "inhibition", -5)
            ch_v "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ JubesX.change_face("confused", 1)
                    call change_Girl_stat(JubesX, "obedience", 10)
                    call change_Girl_stat(JubesX, "inhibition", 10)
                    ch_v "Right. . ."
                "Yes, not interested.":
                    $ JubesX.change_face("sad", 1)
                    call change_Girl_stat(JubesX, "love", -5)
                    call change_Girl_stat(JubesX, "inhibition", -10)
                    $ line = "embarrassed"


    if not line:
        $ JubesX.change_face("sly", 1)
        ch_v "I think I enjoy having you in charge."
        ch_v "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                $ JubesX.change_face("sly", 1)
                call change_Girl_stat(JubesX, "obedience", 5)
                ch_v "Good. Maybe we could take this a bit more seriously?"
                menu:
                    extend ""
                    "Nah. This is just about perfect.":
                        $ JubesX.change_face("sad", 1)
                        call change_Girl_stat(JubesX, "obedience", -15)
                        call change_Girl_stat(JubesX, "love", 10)
                        $ line = "fail"
                    "What'd you have in mind?":
                        $ JubesX.eyes = "side"
                        ch_v "I was thinking I could start calling you. . . {i}master{/i}?"
                        $ JubesX.eyes = "squint"
                        menu:
                            extend ""
                            "Oh, yeah. I'd like that.":
                                call change_Girl_stat(JubesX, "obedience", 5)
                                ch_v "Good. . ."
                            "Um. . .nah. That's too much.":
                                $ JubesX.change_face("sadside", 1)
                                call change_Girl_stat(JubesX, "obedience", -15)
                                call change_Girl_stat(JubesX, "inhibition", 5)
                                $ line = "fail"
                    "Actually, I'd prefer we stopped doing it. Too much pressure.":

                        $ JubesX.change_face("sad", 1)
                        call change_Girl_stat(JubesX, "love", -5)
                        call change_Girl_stat(JubesX, "obedience", -10)
                        call change_Girl_stat(JubesX, "inhibition", 15)
                        $ line = "fail"
                    "Actually, let's stop that. It's creeping me out.":

                        $ JubesX.change_face("angry", 2, eyes = "surprised")
                        call change_Girl_stat(JubesX, "love", -10)
                        call change_Girl_stat(JubesX, "obedience", -50)
                        call change_Girl_stat(JubesX, "inhibition", -15)
                        ch_v "Say no more, I wouldn't want to CREEP YOU OUT."
                        $ line = "embarrassed"
            "As if I care what you think, slut.":

                $ JubesX.change_face("angry", 1, mouth = "smile")
                call change_Girl_stat(JubesX, "love", -20)
                call change_Girl_stat(JubesX, "obedience", 10)
                call change_Girl_stat(JubesX, "inhibition", -10)
                ch_v ". . ."
                menu:
                    ch_v "Excuse me?"
                    "Sorry. I just don't care what you want.":
                        if approval_check(JubesX, 1400, "LO"):
                            call change_Girl_stat(JubesX, "obedience", 10)
                            ch_v ". . ."
                            $ JubesX.change_face("sly", 1)
                            call change_Girl_stat(JubesX, "love", 20)
                            call change_Girl_stat(JubesX, "inhibition", 15)
                            ch_v ". . .{i}go on. . .{/i}"
                        else:
                            call change_Girl_stat(JubesX, "love", -15)
                            call change_Girl_stat(JubesX, "obedience", -10)
                            call change_Girl_stat(JubesX, "inhibition", 5)
                            $ JubesX.change_face("angry", 1)
                            ch_v "!!!"
                            $ line = "rude"
                    "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                        call change_Girl_stat(JubesX, "love", 10)
                        call change_Girl_stat(JubesX, "obedience", 10)
                        call change_Girl_stat(JubesX, "inhibition", 5)
                        if approval_check(JubesX, 1400, "LO"):
                            call change_Girl_stat(JubesX, "obedience", 10)
                            ch_v ". . ."
                            $ JubesX.change_face("sly", 1)
                            call change_Girl_stat(JubesX, "love", 20)
                            call change_Girl_stat(JubesX, "inhibition", 15)
                            ch_v ". . .{i}no, about right. . .{/i}"
                        else:
                            call change_Girl_stat(JubesX, "love", 5)
                            call change_Girl_stat(JubesX, "obedience", -5)
                            call change_Girl_stat(JubesX, "inhibition", 5)
                            $ JubesX.change_face("angry", 1, eyes = "side")
                            ch_v ". . ."
                            ch_v "We'll work on it. . ."
            "I don't really like it. Too much pressure.":

                $ JubesX.change_face("sad", 2)
                call change_Girl_stat(JubesX, "love", -20)
                call change_Girl_stat(JubesX, "obedience", -20)
                call change_Girl_stat(JubesX, "inhibition", -10)
                $ line = "embarrassed"

    $ JubesX.history.append("master")
    if line == "rude":
        $ JubesX.recent_history.append("angry")

        call remove_Girl(JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] stomps out of the room."
    elif line == "embarrassed":
        ch_v "Ok, fine then."
        ch_v "And here I was, about to \"elevate your clearance.\""

        call remove_Girl(JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] brushes past you on her way out."
    elif line == "fail":
        ch_v "Oh. . ."
        ch_v "I guess that's fine."
    else:
        call change_Girl_stat(JubesX, "obedience", 50)
        $ JubesX.player_petnames.append("master")
        $ JubesX.player_petname = "master"
        ch_v ". . .master."
    return







label Jubes_Sexfriend:

    $ JubesX.lust = 70
    $ JubesX.location = Player.location
    $ JubesX.drain_word("asked_to_meet")
    call set_the_scene
    $ JubesX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ JubesX.change_face("sly", 2, eyes = "side")
    "[JubesX.name] approaches you and pulls you aside. She seems to be shivering a little bit."
    "She seems to be squirming around and rubbing her thighs together."
    $ JubesX.player_petnames.append("sex friend")
    $ JubesX.change_face("sly", 2)
    if JubesX in Player.Harem:
        ch_v "Hey."
        ch_v "I need some alone time with you."
    elif "lover" in JubesX.player_petnames or "master" in JubesX.player_petnames or "lover" in JubesX.player_petnames or "sir" in JubesX.player_petnames:

        ch_v "Hey."
        ch_v "I need some alone time with you."
    else:

        ch_v "Hey, so. . . "
        if JubesX.SEXP >= 50:
            ch_v "I know we're kind of casual and all. . ."
        else:
            ch_v "Maybe this seems a bit out of the blue, but. . ."
        ch_v "I'd really just like to have some sex."
        ch_v "Like lots of sex."
        ch_v "With you."
        menu:
            extend ""
            "Sure":
                $ JubesX.change_face("sly", 2, mouth = "smile")
                $ line = "yes"
            "No thanks":
                $ JubesX.change_face("confused", 2)
                $ line = "no"
            ". . .":
                call change_Girl_stat(JubesX, "obedience", 5)
                $ JubesX.change_face("confused", 2)

        if not line:
            ch_v "Now, if at all possible. . ."
            menu:
                extend ""
                "Sure":
                    $ JubesX.change_face("sly", 2, mouth = "smile")
                    $ line = "yes"
                "No thanks":
                    $ JubesX.change_face("confused", 2)
                    $ line = "no"

        if line == "no":
            call change_Girl_stat(JubesX, "love", -5)
            call change_Girl_stat(JubesX, "obedience", 5)
            ch_v "What? Why not?"
            menu:
                extend ""
                "Ok, fine":
                    $ JubesX.change_face("confused", 2, mouth = "smile")
                    ch_v "Love the enthusiasm."
                    $ line = "yes"
                "Not interested":
                    $ JubesX.change_face("confused", 2)
                "There's someone else":

                    call change_Girl_stat(JubesX, "love", -5)
                    call change_Girl_stat(JubesX, "obedience", 5)
                    if Player.Harem:
                        $ JubesX.change_face("surprised", 2)
                        ch_v "Oh, [Player.Harem[0].name]?"
                        $ JubesX.check_if_likes(Player.Harem[0], 600, -25, 1)
                    $ JubesX.change_face("sly", 2)
                    ch_v "Well, she doesn't need to know about it. . ."
                    menu:
                        extend ""
                        "Ok, fine":
                            ch_v "Love the enthusiasm."
                            $ line = "yes"
                        "Still no":
                            pass

    if line == "no":
        call change_Girl_stat(JubesX, "love", -10)
        call change_Girl_stat(JubesX, "obedience", 15)
        call change_Girl_stat(JubesX, "inhibition", 10)
        $ JubesX.change_face("sad", 2)
        ch_v "Really?"
        ch_v "Bummer."
        ch_v "Well let me know if you change your mind."
        $ JubesX.change_face("sadside", 2, mouth = "lipbite", brows = "angry")
        if Player.Harem:
            ch_v "Wonder if [Player.Harem[0].name]'s busy. . ."
            $ JubesX.check_if_likes(Player.Harem[0], 500, 25, 1)
        else:
            ch_v "Wonder if Kitty's busy. . ."
            $ JubesX.check_if_likes("Kitty", 500, 25, 1)
    else:
        call change_Girl_stat(JubesX, "love", 10)
        call change_Girl_stat(JubesX, "obedience", 5)
        call change_Girl_stat(JubesX, "inhibition", 15)
        $ JubesX.change_face("sly", 1, mouth = "smile")
        if taboo:
            ch_v "Wanna take this party someplace else?"
            menu:
                extend ""
                "Yeah":
                    ch_v "Sure, let's go."
                    if Player.location == "bg_player":
                        $ Player.location = "bg_jubes"
                    else:
                        $ Player.location = "bg_player"

                    call clear_the_room (JubesX)
                    call set_the_scene
                    $ taboo = 0
                    $ JubesX.taboo = 0
                "No, let's do it here.":

                    call change_Girl_stat(JubesX, "obedience", 5)
                    call change_Girl_stat(JubesX, "inhibition", 15)
                    ch_v "Kinky."

        $ Player.add_word(1, "interruption")
        call before_action(JubesX, "sex", JubesX)
        call enter_main_sex_menu(JubesX)



    return






label Jubes_Fuckbuddy:
    $ JubesX.daily_history.append("relationship")
    $ JubesX.lust = 80
    $ JubesX.drain_word("asked_to_meet")

    "You hear a knock on the door, and go to answer it."

    $ JubesX.location = Player.location
    $ shift_focus (JubesX)
    call set_the_scene
    $ JubesX.outfit_name = "default"
    $ JubesX.today_outfit_name = "default"
    $ JubesX.change_Outfit()
    call show_Girl (JubesX)
    call set_Character_taboos
    $ Player.primary_Action = "masturbation"
    $ girl_secondary_Action = "fondle_pussy"
    $ JubesX.change_face("sly", 2, mouth = "lipbite")
    "[JubesX.name] is standing in the doorway, with her hand down her pants."
    "You can tell she's been masturbating furiously, her scent is overpowering."
    $ Player.primary_Action = None
    $ girl_secondary_Action = None
    $ JubesX.arm_pose = 1
    "She looks you up and down hungrily, and pulls her hand out of her pants."
    "She reaches up to caress your face, smearing her juices along it."
    ch_v "Mine."
    $ JubesX.player_petnames.append("fuck buddy")
    $ JubesX.event_happened[10] += 1

    $ Player.add_word(1, "interruption")
    call before_action(JubesX, "sex", JubesX)
    call enter_main_sex_menu(JubesX)

    return






label Jubes_Daddy:
    $ JubesX.daily_history.append("relationship")
    $ JubesX.drain_word("asked_to_meet")
    $ shift_focus (JubesX)
    call set_the_scene
    ch_v ". . ."
    if JubesX in Player.Harem:
        ch_v "So we've been dating a while yeah?"
    else:
        ch_v "This thing we've got, pretty fun, right?"
    if JubesX.love > JubesX.obedience and JubesX.love > JubesX.inhibition:
        ch_v "and you've been really kind to me. . ."
    elif JubesX.obedience > JubesX.inhibition:
        ch_v "and you've been a good influence. . ."
    else:
        ch_v "like, really fun. . ."
    ch_v "So I've been thinking, would you want to be called. . ."
    ch_v "\"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ JubesX.change_face("smile")
            call change_Girl_stat(JubesX, "love", 20)
            call change_Girl_stat(JubesX, "obedience", 10)
            call change_Girl_stat(JubesX, "inhibition", 30)
            ch_v "Cool."
        "What do you mean by that?":
            $ JubesX.change_face("bemused")
            ch_v "I don't know, I've had some shitty father figures. . ."
            ch_v "I just. . ."
            if JubesX.love > JubesX.obedience and JubesX.love > JubesX.inhibition:
                ch_v "I think you could do better. . ."
            elif JubesX.obedience > JubesX.inhibition:
                ch_v "you've really been assertive. . ."
            else:
                ch_v "wouldn't it be kinky?"

            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ JubesX.change_face("smile")
                    call change_Girl_stat(JubesX, "love", 15)
                    call change_Girl_stat(JubesX, "obedience", 20)
                    call change_Girl_stat(JubesX, "inhibition", 25)
                    ch_v "Great!"
                    $ JubesX.change_face("sly", 2)
                    ch_v " . . . daddy."
                    $ JubesX.change_face("sly", 1)
                    $ JubesX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(JubesX, "love", 5)
                    call change_Girl_stat(JubesX, "obedience", 40)
                    call change_Girl_stat(JubesX, "inhibition", 20)
                    $ JubesX.change_face("sad")
                    ch_v " . . . "
                    ch_v "Well, ok."
                "You've got some real daddy issues, uh?":
                    call change_Girl_stat(JubesX, "love", -15)
                    call change_Girl_stat(JubesX, "obedience", 45)
                    call change_Girl_stat(JubesX, "inhibition", 5)
                    $ JubesX.change_face("angry")
                    ch_v "Yes. . . I said that."
        "You've got some real daddy issues, uh?":
            call change_Girl_stat(JubesX, "love", -15)
            call change_Girl_stat(JubesX, "obedience", 45)
            call change_Girl_stat(JubesX, "inhibition", 5)
            $ JubesX.change_face("angry")
            ch_v ". . . Probably."
            ch_v "Never mind."
    $ JubesX.player_petnames.append("daddy")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
