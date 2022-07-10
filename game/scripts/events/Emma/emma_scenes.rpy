label Emma_Caught_Classroom:
    show black_screen onlayer black

    $ EmmaX.teaching = True
    $ EmmaX.arm_pose = 1
    $ EmmaX.change_face("sexy", eyes = "closed")

    call set_the_scene(location = "bg_classroom")
    call clear_the_room(EmmaX, passive = True, silent = True)

    "As you walk down the halls, you hear some odd noises coming from the classroom."

    $ Player.add_word(1, "interruption")

    $ taboo = 0
    $ Count = 0

    hide black_screen onlayer black

    $ shift_focus(EmmaX)

    $ girl_secondary_Action = "fondle_pussy"
    $ second_girl_secondary_Action = "fondle_breasts"

    $ EmmaX.recent_history.append("classcaught")
    $ EmmaX.daily_history.append("unseen")
    $ EmmaX.recent_history.append("unseen")

    $ EmmaX.drain_word("no_masturbation")
    $ EmmaX.recent_history.append("masturbation")
    $ EmmaX.daily_history.append("masturbation")

    "You see [EmmaX.name] leaning back against her desk, her hands tracing slow paths across her body."

    if simulation:
        call after_masturbation(EmmaX, "interrupt")
    else:
        call masturbation_cycle(EmmaX)

    if "angry" in EmmaX.recent_history:
        return

    $ EmmaX.teaching = False
    $ EmmaX.eyes = "sexy"
    $ EmmaX.brows = "confused"
    $ EmmaX.mouth = "normal"
    $ EmmaX.arm_pose = 1

    call stop_all_Actions
    call set_the_scene

    if "classcaught" in EmmaX.history:
        ch_e "I notice you make a habit of dropping in."
    else:
        $ EmmaX.history.append("classcaught")

        if not simulation:
            $ approval_bonus = 25

        ch_e "Well."

        call stop_all_Actions

        $ EmmaX.location = "bg_classroom"

        call set_the_scene

        $ EmmaX.change_face("angry", eyes = "side")

        $ caught = False

        ch_e "It appears that you've caught me in a somewhat. . . compromising position. . ."

        menu:
            extend ""
            "Yup.":
                $ EmmaX.change_face("perplexed", mouth = "normal")
                call change_Girl_stat(EmmaX, "love", -1)
                call change_Girl_stat(EmmaX, "obedience", -2)
                call change_Girl_stat(EmmaX, "lust", -5)

                ch_e "Er, well. . ."
            "Are you supposed to be shlicking it in class?":
                $ EmmaX.change_face("angry", eyes = "side")
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "inhibition", 5)

                ch_e "Hrm."

                $ EmmaX.change_face("sly", brows = "angry")
                call change_Girl_stat(EmmaX, "lust", 3)

                ch_e "I imagine I shouldn't, but you know how it can be, "

                $ EmmaX.brows = "normal"
                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "-surrounded by attractive co-eds all day long. . ."

                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "yourself included. . ."
            "I think it was pretty hot.":
                $ EmmaX.change_face("sly")
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", 10)
                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "Hmm, well I suppose I can't blame you for that. . ."
            "What do you mean?":
                $ EmmaX.change_face("angry")
                call change_Girl_stat(EmmaX, "love", -10)
                call change_Girl_stat(EmmaX, "obedience", -5)

                ch_e "I mean how I was. . ."

                $ EmmaX.change_face("surprised")
                call change_Girl_stat(EmmaX, "love", 15)
                call change_Girl_stat(EmmaX, "obedience", 15)
                call change_Girl_stat(EmmaX, "inhibition", 5)

                ch_e "Oh!"

                $ EmmaX.change_face("perplexed")

                ch_e "Yes, obviously it was nothing, just getting some. . ."

                $ EmmaX.eyes = "side"
                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "paperwork done. . ."

                $ EmmaX.change_face("sly")

                $ caught = True

        ch_e "So how did you want to handle this. . . situation?"

        menu:
            extend ""
            "I think I can forget all about it.":
                $ EmmaX.change_face("smile")
                call change_Girl_stat(EmmaX, "love", 10)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", 15)

                ch_e "Thank you, [EmmaX.player_petname]. I appreciate your discretion."

                $ EmmaX.change_face("sly")

                ch_e "Are you {i}certain{/i} there's nothing I could do to thank you?"
            "What solution did you have in mind?":
                $ EmmaX.change_face("sly")
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 15)
                call change_Girl_stat(EmmaX, "inhibition", 15)
                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "Oh, I'm sure I could make it worth your while. . ."
            "What situation?":
                if not caught:
                    $ EmmaX.change_face("confused")
                    call change_Girl_stat(EmmaX, "love", -10)
                    call change_Girl_stat(EmmaX, "obedience", -5)

                    ch_e "I mean how I was. . ."

                    $ EmmaX.change_face("surprised")
                    call change_Girl_stat(EmmaX, "love", 15)
                    call change_Girl_stat(EmmaX, "obedience", 15)
                    call change_Girl_stat(EmmaX, "inhibition", 5)

                    ch_e "Oh!"

                    $ EmmaX.change_face("perplexed")

                    ch_e "Yes, obviously it was nothing, just getting some. . ."

                    $ EmmaX.eyes = "side"
                    call change_Girl_stat(EmmaX, "lust", 5)

                    ch_e "paperwork done. . ."

                    $ EmmaX.change_face("sly")
                else:
                    $ EmmaX.change_face("angry")
                    call change_Girl_stat(EmmaX, "love", -5)
                    call change_Girl_stat(EmmaX, "inhibition", 5)

                    ch_e "I do wonder if you're just being dense. . ."

                    $ EmmaX.change_face("sly")

                    ch_e "Still. . ."

        $ multi_action = False

        menu:
            extend ""
            "Could you strip?":
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", 15)

                ch_e "So you wanted a better view of the action?"

                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "I suppose I could accomodate that. . ."
                ch_e "to a point. . ."
                "[EmmaX.name] walks to the door and locks it behind her."

                $ taboo = 0
                $ EmmaX.taboo = 0

                if simulation:
                    return True

                call Group_Strip (EmmaX)
            "Could you just keep going?":
                call change_Girl_stat(EmmaX, "love", 10)
                call change_Girl_stat(EmmaX, "obedience", 15)
                call change_Girl_stat(EmmaX, "inhibition", 15)

                ch_e "Oh, you wanted to watch some more?"
                ch_e "I can't exactly blame you."

                $ EmmaX.eyes = "down"
                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "Were you going to put on a show as well?"

                menu:
                    "Yeah!":
                        call change_Girl_stat(EmmaX, "love", 5)
                        call change_Girl_stat(EmmaX, "inhibition", 10)
                        call change_Girl_stat(EmmaX, "lust", 5)

                        ch_e "Excellent."

                        if not simulation:
                            call Seen_First_Peen (EmmaX)

                        "You begin to stroke your cock."

                        $ Player.secondary_Action = "jerking_off"
                    "No, you go ahead.":
                        $ EmmaX.change_face("sad")
                        call change_Girl_stat(EmmaX, "love", -10)
                        call change_Girl_stat(EmmaX, "obedience", 5)
                        call change_Girl_stat(EmmaX, "inhibition", 5)

                        ch_e "Pity."

                $ EmmaX.change_face("sly")

                "[EmmaX.name] walks to the door and locks it behind her."

                $ taboo = 0
                $ EmmaX.taboo = 0

                $ Player.secondary_Action = "fondle_pussy"
                $ second_girl_secondary_Action = "fondle_breasts"

                "She leans back and runs her fingertips along her breasts."

                if simulation:
                    return True

                call masturbation_cycle(EmmaX)
                call after_masturbation(EmmaX, "stop")
            "Could I feel you up?":
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", 10)

                ch_e "Hmm, I could use some help . . .around the office. . . "

                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "Perhaps you have some suggestions?"
                "[EmmaX.name] walks to the door and locks it behind her."

                $ taboo = 0
                $ EmmaX.taboo = 0

                if simulation:
                    return True

                call before_action(EmmaX, "fondle_breasts")

                $ Player.primary_Action = "fondle_breasts"

                call Action_cycle(EmmaX, "fondle_breasts")
                call after_action(EmmaX, "fondle_breasts", "stop")
                call stop_all_Actions
            "Could you give me a hand? [[point to your cock]":
                call change_Girl_stat(EmmaX, "love", -5)
                call change_Girl_stat(EmmaX, "obedience", 5)
                $ EmmaX.brows = "surprised"

                ch_e "I appreciate boldness, [EmmaX.player_petname], but be a bit more realistic."

                $ EmmaX.brows = "normal"
                call change_Girl_stat(EmmaX, "love", 10)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "Perhaps instead I could just offer a little. . . token of my appreciation."
                "[EmmaX.name] walks to the door and locks it behind her."

                $ taboo = 0
                $ EmmaX.taboo = 0

                if simulation:
                    return True

                call Group_Strip (EmmaX)
            "I should just get going then.":
                $ EmmaX.change_face("surprised")
                call change_Girl_stat(EmmaX, "obedience", 5)

                ch_e "Oh."

                $ EmmaX.change_face("confused")
                call change_Girl_stat(EmmaX, "love", -5)
                call change_Girl_stat(EmmaX, "inhibition", -5)

                ch_e "Well, I suppose. . ."

                $ EmmaX.change_face("perplexed")
                call change_Girl_stat(EmmaX, "lust", 5)

                ch_e "I'll see you. . . in class then. . ."

        $ multi_action = True

        $ EmmaX.change_Outfit()

        "[EmmaX.name] collects her things and strides toward the door."
        "She turns back with her hand on the door."

        $ EmmaX.change_face("sly")

        ch_e "Oh, and [EmmaX.player_petname]?"
        ch_e "You can just call me \"Emma.\""

        $ EmmaX.name = "Emma"
        $ EmmaX.names.append("Emma")
        $ EmmaX.location = "bg_emma"

        call remove_Girl(EmmaX)

        $ round = 20 if round > 20 else round

    return










label Emma_Teacher_Caught(Girl=0):


    if "noticed " + Girl.tag in EmmaX.recent_history:
        return
    if approval_check(EmmaX, 500, "I") and approval_check(EmmaX, 1500) and EmmaX.likes[Girl.tag] >= 500:
        "[EmmaX.name] notices the two of you, but just tilts her head in approval and continues on."
        $ EmmaX.check_if_likes(Girl,800,3, 1)
        $ Girl.check_if_likes(EmmaX,800,3, 1)
        $ EmmaX.recent_history.append("noticed " + Girl.tag)
        return

    ch_e "[Player.name]? [Girl.name]? Could you stop what you're doing immediately?"
    $ checkout()
    call reset_player

    $ Girl.change_face("bemused", 2, eyes = "side")
    call show_full_body(Girl)
    if approval_check(Girl, 700, "I"):
        $ Girl.change_face("bemused", 1)
        "[Girl.name] shrugs and returns to her seat."
        call Partner_Like (EmmaX, 2, -1, 500, Girl)
    else:
        "[Girl.name] jumps and dashes out of the room."
        call Partner_Like (EmmaX, -2, -3, 500, Girl)
        call remove_Girl(Girl)

    $ Girl.reputation -= 1
    call Partner_Like (Girl, 3, 2, 800, EmmaX)
    $ EmmaX.check_if_likes(Girl,800,3, 1)

    $ Player.reputation -= 1
    ch_e "Thank you."
    ch_e "And [Player.name], see me after class for detention. . ."

    $ renpy.pop_call()
    $ renpy.pop_call()
    $ Player.traits.append("detention")
    $ Player.daily_history.append("detention")
    jump classroom












label Emma_Detention:
    $ shift_focus (EmmaX)

    $ Player.location = "bg_classroom"

    call set_the_scene

    if True:
        "You enter the room and see [EmmaX.name] waiting for you at the back of the room."
    else:
        "After class, the students file out, and you wait a few minutes until they're all gone."
        "Once the last student leaves, [EmmaX.name] approaches you."

    show black_screen onlayer black

    $ EmmaX.change_Outfit()
    $ EmmaX.change_face("sly")
    $ EmmaX.arm_pose = 2

    call remove_all

    $ EmmaX.location = "bg_classroom"

    call set_the_scene

    $ Count = 0

    hide black_screen onlayer black

    $ line = 0
    if "detention" in Player.daily_history:
        ch_e "I'm glad you take your. . . education seriously."
    else:

        $ EmmaX.change_face("surprised")
        ch_e "Oh, [EmmaX.player_petname], you really shouldn't skip your detention like that. . ."
    $ Player.traits.remove("detention")
    $ EmmaX.recent_history.append("detention")
    $ EmmaX.daily_history.append("detention")
    $ EmmaX.change_face("sly")
    call change_Girl_stat(EmmaX, "lust", 3)
    ch_e "You've been such a naughty pupil. . ."
    $ EmmaX.arm_pose = 1
    $ EmmaX.change_face("sadside", brows = "normal")
    call change_Girl_stat(EmmaX, "lust", 5)
    ch_e "Chasing after those young girls. . ."
    $ EmmaX.change_face("sly")
    call change_Girl_stat(EmmaX, "lust", 3)
    if "detention" in EmmaX.history:
        ch_e "How will we deal with it this time?"
    else:

        ch_e "What am I to do with you. . ."
        $ EmmaX.history.append("detention")

    "[EmmaX.name] walks to the door and locks it behind her."
    $ taboo = 0
    $ EmmaX.taboo = 0
    $ Player.traits.append("locked")
    menu:
        extend ""
        "I guess I should focus on my studies.":
            if approval_check(EmmaX, 900) and "classcaught" in EmmaX.history:
                $ EmmaX.change_face("perplexed")
                call change_Girl_stat(EmmaX, "inhibition", -3)
                call change_Girl_stat(EmmaX, "lust", 5)
                ch_e "Oh. Really? I was thinking of a more. . . recreational punishment."
                menu:
                    extend ""
                    "Kidding, of course, what should we do? [[sex stuff]":
                        $ EmmaX.change_face("sly")
                        call change_Girl_stat(EmmaX, "love", 3)
                        call change_Girl_stat(EmmaX, "obedience", 5)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "Why do I put up with you?"
                        call enter_main_sex_menu(EmmaX)
                    "No, you're right, I take my education too lightly.":
                        call change_Girl_stat(EmmaX, "love", 1)
                        call change_Girl_stat(EmmaX, "inhibition", -2)
                        call change_Girl_stat(EmmaX, "lust", 5)
                        ch_e "Oh. Ok. Um. . ."
                        $ EmmaX.change_face("sad")
                        call change_Girl_stat(EmmaX, "obedience", 5)
                        call change_Girl_stat(EmmaX, "lust", 5)
                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                        call change_Girl_stat(EmmaX, "lust", 5)
                        $ Player.XP += 10
            else:

                $ EmmaX.change_face("sad", mouth = "normal")
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "lust", 5)
                ch_e "Yes. . . Exactly. . ."
                call change_Girl_stat(EmmaX, "inhibition", 5)
                call change_Girl_stat(EmmaX, "lust", 5)
                ch_e "I guess we could go over some of the topics from today's class then. . ."
                call change_Girl_stat(EmmaX, "inhibition", 5)
                call change_Girl_stat(EmmaX, "lust", 5)
                $ Player.XP += 10
        "I could think of a few things. . . [[sex stuff]":
            if approval_check(EmmaX, 900) and "classcaught" in EmmaX.history:
                $ EmmaX.change_face("sly")
                call change_Girl_stat(EmmaX, "lust", 5)
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                ch_e "I just bet you can. . ."
                call enter_main_sex_menu(EmmaX)
            else:

                $ EmmaX.change_face("sad", mouth = "smirk")
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "lust", 5)
                ch_e "I'm sure you could. . . but unfortunately this isn't the time for it."
                call change_Girl_stat(EmmaX, "inhibition", 5)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                call change_Girl_stat(EmmaX, "lust", 5)
                ch_e "We'll just have to settle for going over some of the topics from today's class. . ."
                call change_Girl_stat(EmmaX, "inhibition", 5)
                call change_Girl_stat(EmmaX, "lust", 5)
                $ Player.XP += 10
    $ round -= 20 if round > 20 else 0
    ch_e "Ok, I think that's plenty for now. . ."
    ch_e "You wouldn't want to make this a habit. . ."
    $ approval_bonus = 0
    $ EmmaX.change_Outfit()
    $ Player.drain_word("locked", 0, 0, 1)
    return








label Emma_Key:
    $ shift_focus (EmmaX)
    call set_the_scene
    $ EmmaX.change_face("bemused")
    $ EmmaX.arm_pose = 2
    ch_e "You've been coming by fairly often. . ."
    ch_e ". . . you might want a key. . ."
    ch_p "Thanks."
    $ EmmaX.arm_pose = 1
    $ Player.Keys.append(EmmaX)
    $ EmmaX.event_happened[0] = 1
    return






label Emma_taboo_Talk:


    if "taboo" in EmmaX.history:
        return

    $ EmmaX.change_face("sly")
    if "taboocheck" not in EmmaX.history:
        ch_e "[EmmaX.player_petname], I know that we've had some. . . fun, "
        $ EmmaX.change_face("sly", eyes = "side")
        ch_e "but that was between us, in private."
        $ EmmaX.change_face("sly")
        ch_e "I can't have our trysts become. . . public knowledge."
        ch_e "I am a teacher here, you understand."
        ch_e "You're a student."
        $ EmmaX.change_face("sadside")
        ch_e "It's complicated."
        ch_e "So I'm afraid that we can only. . ."
        $ EmmaX.change_face("sad")
        ch_e ". . .interact, when we're alone."
        ch_e "Do you understand?"
    else:
        ch_e "I believe I made clear why I couldn't do anything like that in public. . ."

    $ line = 1
    while line >= 1:
        menu:
            extend ""
            "Yeah, I suppose.":
                $ EmmaX.change_face("smile")
                if "taboocheck" in EmmaX.history:
                    pass
                elif line != 4:

                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "obedience", 5)
                    call change_Girl_stat(EmmaX, "inhibition", 5)
                else:
                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "love", 10)

                ch_e "Thank you for your discretion."
                $ EmmaX.change_face("sly")
                if approval_check(EmmaX, 2000) and "taboocheck" in EmmaX.history:
                    ch_e "Although. . . I suppose we could make an exception. . ."
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    $ line = -1
                else:
                    ch_e "I do hope that we can still find some time to meet up."
                    $ line = 0

            "I don't care who sees us." if line != 2 and line != 4:
                if "taboocheck" in EmmaX.history:
                    ch_e "I'm aware. . ."
                    if approval_check(EmmaX, 500, "I"):
                        $ EmmaX.change_face("sly")
                        ch_e "Frankly, I don't either."
                        $ EmmaX.change_face("angry", eyes = "side")
                        ch_e "It's not about that though, if we get caught, I get fired."
                        $ EmmaX.change_face("angry")
                        ch_e "If I get fired, then I can't stay here."
                        $ EmmaX.change_face("sly")
                        ch_e "So that really isn't an option."
                    else:
                        $ EmmaX.change_face("confused", 1)
                        ch_e "You might not, but I have a reputation to maintain."
                elif approval_check(EmmaX, 500, "I"):
                    call change_Girl_stat(EmmaX, "lust", 5)
                    call change_Girl_stat(EmmaX, "inhibition", 5)
                    $ EmmaX.change_face("sly")
                    ch_e "Frankly, I don't either."
                    $ EmmaX.change_face("angry", eyes = "side")
                    ch_e "It's not about that though, if we get caught, I get fired."
                    $ EmmaX.change_face("angry")
                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "obedience", 10)
                    ch_e "If I get fired, then I can't stay here."
                    $ EmmaX.change_face("sly")
                    ch_e "So that really isn't an option."
                else:
                    call change_Girl_stat(EmmaX, "lust", 5)
                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "obedience", 10)
                    $ EmmaX.change_face("confused", 1)
                    ch_e "Well you might not, but I have a reputation to maintain."
                $ EmmaX.change_face("sly")
                ch_e "So can you understand why we must be discrete?"
                $ line = 4 if line != 1 else 2

            "Couldn't you just mindwipe anyone who sees?" if line != 3 and line != 4:
                if "taboocheck" in EmmaX.history:
                    ch_e "Yes, we've been over why that wouldn't exactly be an option."
                else:
                    if approval_check(EmmaX, 500, "I"):
                        $ EmmaX.change_face("sly")
                        call change_Girl_stat(EmmaX, "lust", 5)
                        call change_Girl_stat(EmmaX, "love", 5)
                        call change_Girl_stat(EmmaX, "obedience", 5)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "You must have read my mind."
                    elif approval_check(EmmaX, 800, "LO"):
                        $ EmmaX.change_face("sly", 1)
                        call change_Girl_stat(EmmaX, "lust", 5)
                        call change_Girl_stat(EmmaX, "love", 10)
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "Oh, you naughty boy."
                    else:
                        $ EmmaX.change_face("surprised", 1)
                        call change_Girl_stat(EmmaX, "lust", 5)
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        call change_Girl_stat(EmmaX, "inhibition", 15)
                        call change_Girl_stat(EmmaX, "inhibition", 10)
                        ch_e "What? I would never!"
                    $ EmmaX.change_face("angry", eyes = "side")
                    ch_e "Either way though, that's not really an option either."
                ch_e "I can't muck about with the students' minds too much without Charles catching on."
                ch_e "Casually mindwiping students certainly wouldn't pass unnoticed."
                if EmmaX in Rules:

                    ch_p "But Xavier is off the board now. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "I suppose that's true. . ."
                    ch_e "A little helpful editing might not hurt. . ."
                    $ line = -1
                else:
                    $ EmmaX.change_face("confused", mouth = "normal")
                    ch_e "So are we on the same page here?"
                    $ line = 4 if line != 1 else 3

            "I don't care, let's do it." if line == 4:
                $ line = 0
                if approval_check(EmmaX, 2000):
                    $ EmmaX.change_face("surprised", eyes = "side")
                    call change_Girl_stat(EmmaX, "lust", 5)
                    call change_Girl_stat(EmmaX, "inhibition", 15)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    ch_e "Oh, I will get in so much trouble for this. . ."
                    call change_Girl_stat(EmmaX, "love", 5)
                    call change_Girl_stat(EmmaX, "obedience", 15)
                    $ EmmaX.change_face("sly")
                    ch_e "but you're worth it."
                    $ line = -1
                elif approval_check(EmmaX, 800, "I"):
                    $ EmmaX.change_face("surprised", eyes = "side")
                    call change_Girl_stat(EmmaX, "lust", 5)
                    call change_Girl_stat(EmmaX, "obedience", 15)
                    ch_e "Oh, I will get in so much trouble for this. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "but it will be so much fun."
                    $ line = -1
                elif "taboocheck" in EmmaX.history:
                    $ EmmaX.change_face("angry")
                    call change_Girl_stat(EmmaX, "love", -5)
                    call change_Girl_stat(EmmaX, "obedience", -5)
                    ch_e "You're going to have to respect my boundaries on this one."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ renpy.pop_call()
                else:
                    $ EmmaX.change_face("angry")
                    call change_Girl_stat(EmmaX, "love", -5)
                    call change_Girl_stat(EmmaX, "obedience", -5)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    ch_e "Well that's just too bad."
                    ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ renpy.pop_call()


    if "taboocheck" not in EmmaX.history:
        $ EmmaX.history.append("taboocheck")
    if line == -1:

        $ EmmaX.history.append("taboo")
        $ EmmaX.history.remove("taboocheck")
    $ line = 0
    return





label Emma_ThreeCheck(Pass = 3, Quest = [], Girl=0, temp_Girls = []):

    if EmmaX.SEXP <= 30:
        $ EmmaX.change_face("confused")
        ch_e "[EmmaX.player_petname], I barely put up with you, don't try to bring other girls into this."
        return
    if "threesome" in EmmaX.history:
        return

    $ line = 0
    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(EmmaX)
    while temp_Girls:
        if "saw with " + temp_Girls[0].tag in EmmaX.traits:
            $ line = "I saw you with " + temp_Girls[0].tag
        if temp_Girls[0].location == Player.location:
            $ Girl = temp_Girls[0]
            $ temp_Girls = [1]
        $ temp_Girls.remove(temp_Girls[0])

    if not Girl or Girl not in all_Girls:
        $ Quest.append(2)
        if line:
            $ EmmaX.change_face("angry", eyes = "side")
            if line:
                ch_e "[line] earlier. I'm not sure how I feel about that."
            $ line = 0
            if "sleeptime" in EmmaX.history:

                ch_e "I saw you considering having me sleep over with that. . . girl. . ."
                $ EmmaX.history.remove("sleeptime")

    if "threecheck" not in EmmaX.history:
        $ EmmaX.change_face("bemused", eyes = "side")
        "[EmmaX.name] moves close to you and whispers. . ."
        if approval_check(EmmaX, 900, "L"):
            ch_e "[EmmaX.player_petname], I really do. . . care for you. . ."
        elif approval_check(EmmaX, 800, "L"):
            ch_e "[EmmaX.player_petname], I do think you're. . . interesting. . ."
        elif approval_check(EmmaX, 500, "O"):
            ch_e "[EmmaX.player_petname], there is something. . . compelling about you. . ."
        elif approval_check(EmmaX, 500, "I"):
            ch_e "[EmmaX.player_petname], you know that I'm. . . flexible, "
        else:
            ch_e "[EmmaX.player_petname], I don't know what this even is yet, but. . ."
        ch_e "I'm a teacher at this school, and I can't exactly be caught forming some sort of. . ."
        ch_e "harem with the students."
        ch_e "Just you and I would be scandalous, but multiple students?"
        ch_e "That could be a disaster."
    else:
        ch_e "I already explained why I couldn't do this around other girls."
    while Pass > 0:
        menu:
            extend ""
            "Yeah, I suppose.":
                $ EmmaX.change_face("smile")
                if "threecheck" not in EmmaX.history:
                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "love", 10)

                ch_e "Thank you for not insisting."
                $ EmmaX.change_face("sly")
                if Pass == 1 and approval_check(EmmaX, 2000):
                    ch_e "though I suppose. . . perhaps I could make an exception. . ."
                    $ Pass = 0
                else:
                    ch_e "I do hope that we can still find some. . . personal time?"
                    $ Pass = -1

            "But she's cool with it." if 2 not in Quest:


                $ Quest.append(2)
                if Girl.location == Player.location:
                    $ Pass -= 1
                    if "poly Emma" in Girl.traits:

                        if Girl == RogueX:
                            ch_r "Yeah, like I said, ready when you are."
                        elif Girl == KittyX:
                            ch_k "Yup, sounds fun."
                        elif Girl == LauraX:
                            ch_l "Yeah, I'm in."
                    else:
                        $ Girl.traits.append("poly Emma")
                        if approval_check(Girl, 1500) and Girl.likes[EmmaX.tag] >= 800:
                            if Girl == RogueX:
                                ch_r "I really am."
                            elif Girl == KittyX:
                                ch_k "Yeah, you bet."
                            elif Girl == LauraX:
                                ch_l "Sure."
                        elif approval_check(Girl, 1500) and Girl.likes[EmmaX.tag] >= 600:
                            if Girl == RogueX:
                                ch_r "Yeah, you'll do."
                            elif Girl == KittyX:
                                ch_k "Yeah, you're ok."
                            elif Girl == LauraX:
                                ch_l "Yeah, it's cool."
                        elif approval_check(Girl, 2000):
                            if Girl == RogueX:
                                ch_r "You and I get along like cats and bitches. . ."
                                ch_r "but I do want to make him happy."
                            elif Girl == KittyX:
                                ch_k "I don't like you much, but I do want him to be happy."
                            elif Girl == LauraX:
                                ch_l "Ugh, yeah. . ."
                                ch_l "I mean this guy seems to like you."
                        elif approval_check(Girl, 500) and Girl.likes[EmmaX.tag] >= 800:
                            if Girl == RogueX:
                                ch_r "This guy I could take or leave, but you clean up real nice."
                            elif Girl == KittyX:
                                ch_k "Well, I don't know about this guy, but. . . you're pretty."
                            elif Girl == LauraX:
                                ch_l "Hey, even without [Player.name] here, you're a catch."
                        else:
                            if Girl == RogueX:
                                ch_r "I said no such thing!"
                            elif Girl == KittyX:
                                ch_k "I didn't say anything like that!"
                            elif Girl == LauraX:
                                ch_l "Say what now?"
                            $ Girl.traits.remove("poly Emma")
                            $ Pass += 1
                if EmmaX.likes[Girl.tag] >= 700:
                    ch_e "And you're quite fetching yourself dear. . ."
                    $ Pass -= 1 if Pass > 0 else 0
                elif EmmaX.likes[Girl.tag] >= 500:
                    ch_e "And you're. . . acceptable. . ."
                else:
                    ch_e "And that's just lovely, really. . ."
                    $ Pass += 1
                ch_e "But I'm afraid that any sort of dalliance would be an issue."


            "Xavier doesn't care." if taboo and EmmaX in Rules and 3 not in Quest:
                $ Quest.append(3)
                ch_e "Well, that may be, but it could still get out."
                $ Pass -= 1

            "Xavier won't find out here." if not taboo and 3 not in Quest:
                $ Quest.append(3)
                ch_e "Well, that may be, but it could still get out."
                $ Pass -= 1

            "I don't care, let's do this." if Quest:
                if approval_check(EmmaX, 2000) and Pass <= 2:
                    $ EmmaX.change_face("surprised", eyes = "side")
                    call change_Girl_stat(EmmaX, "lust", 5)
                    call change_Girl_stat(EmmaX, "inhibition", 15)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    call change_Girl_stat(EmmaX, "love", 5)
                    call change_Girl_stat(EmmaX, "obedience", 15)
                    ch_e "Oh, I could get in so much trouble for this. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "but you're worth it."
                    $ Pass = 0
                elif approval_check(EmmaX, 800, "I") and Pass <= 2:
                    $ EmmaX.change_face("surprised", eyes = "side")
                    call change_Girl_stat(EmmaX, "lust", 5)
                    call change_Girl_stat(EmmaX, "obedience", 15)
                    ch_e "Oh, I could get in so much trouble for this. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "but it will be so much fun."
                    $ Pass = 0
                elif "threecheck" not in EmmaX.history:
                    $ EmmaX.change_face("angry")
                    call change_Girl_stat(EmmaX, "love", -5)
                    call change_Girl_stat(EmmaX, "obedience", -5)
                    ch_e "You're going to have to learn to take \"no\" for an answer on this one."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ Pass = -1
                else:
                    $ EmmaX.change_face("angry")
                    call change_Girl_stat(EmmaX, "love", -5)
                    call change_Girl_stat(EmmaX, "obedience", -5)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    ch_e "Well that's just too bad."
                    ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ Pass = -1

    if "threecheck" not in EmmaX.history:
        $ EmmaX.history.append("threecheck")
    if Pass == -1:

        $ renpy.pop_call()
    else:

        $ EmmaX.history.append("threesome")
        $ EmmaX.history.remove("threecheck")
        if Girl in all_Girls:
            if "poly " + Girl.tag not in EmmaX.traits:
                $ EmmaX.traits.append("poly " + Girl.tag)
            $ EmmaX.recent_history.append("noticed " + Girl.tag)
            $ Girl.recent_history.append("noticed Emma")
    return






label Emma_BF:
    $ EmmaX.drain_word("asked_to_meet")
    $ shift_focus (EmmaX)

    if EmmaX not in Player.Party:
        "[EmmaX.name] approaches you and asks if the two of you can talk."

        call add_Girls(EmmaX)
    else:
        "[EmmaX.name] turns towards you and asks if the two of you can talk."

    "You can tell she's a bit uncomfortable about whatever she has to say."
    call set_Character_taboos
    call clear_the_room(EmmaX)
    $ EmmaX.daily_history.append("relationship")
    $ EmmaX.change_face("bemused", 1)

    ch_e "[EmmaX.player_petname], we've been. . . enjoying ourselves for a while now."
    ch_e ". . ."
    $ EmmaX.eyes = "sexy"
    menu:
        ch_e "You have been enjoying yourself?"
        "Yeah. And it's been amazing.":
            call change_Girl_stat(EmmaX, "love", 20)
        "Yeah, I guess":
            call change_Girl_stat(EmmaX, "love", 10)
        "Uhm. . .maybe?":
            call change_Girl_stat(EmmaX, "love", -10)
            call change_Girl_stat(EmmaX, "obedience", 30)
    if EmmaX.SEXP >= 10:
        ch_e "I think we've been engaging in some rather inappropriate behavior. . ."
    if EmmaX.SEXP >= 15:
        ch_e "-for a student and teacher, at least. . ."
    if len(Player.Harem) >= 2:
        ch_e "I understand that this isn't an exclusive deal for you. . ."
    elif Player.Harem:
        ch_e "I understand that you've been dating [Player.Harem[0].name]. . ."

    if not EmmaX.event_happened[5]:
        ch_e "So, that being the case. . ."
        ch_e "I was wondering if you'd like to make this a bit more official."
        ch_e "If I could perhaps consider you my. . ."
        ch_e "Boyfriend?"
        ch_e "-or something to that effect."
    elif Player.Harem:
        ch_e ". . . but I would still like to also consider you my boyfriend as well."
    else:
        ch_e "I don't know why I put up with you, but I do still want to be your girlfriend."
    $ EmmaX.event_happened[5] += 1
    menu:
        extend ""
        "Are you kidding? I'd love to!":
            call change_Girl_stat(EmmaX, "love", 25)
            call kiss_launch(EmmaX)
            "[EmmaX.name] wraps her arms around you and starts kissing you passionately."
            $ EmmaX.permanent_History["kiss"] += 1
        "Uhm, okay.":
            $ EmmaX.brows = "confused"
            "[EmmaX.name] seems a little put off by how casually you’re taking all this."
        "I'm with someone else now." if Player.Harem:
            $ EmmaX.change_face("sad", 1)
            ch_e "I understand. I thought that perhaps you could go out with me as well?"
            menu:
                extend ""
                "Yes. Absolutely." if "EmmaYes" in Player.traits:
                    call change_Girl_stat(EmmaX, "love", 30)
                    "[EmmaX.name] wraps her arms around you and starts kissing you passionately."
                    call kiss_launch(EmmaX)
                    $ EmmaX.permanent_History["kiss"] += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                    $ line = "no"
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ line = "no"
                "I'm sorry, but. . . no." if EmmaX.event_happened[5] != 20:
                    $ line = "no"
                "No way.":
                    jump Emma_BF_Jerk
            if line == "no":
                call change_Girl_stat(EmmaX, "love", -10)
                ch_e "Well. . ."
                ch_e "I suppose I understand."
                $ EmmaX.event_happened[5] = 20
                call remove_Girl(EmmaX)
                $ line = 0
                return
        "Not really.":
            jump Emma_BF_Jerk

    if not simulation:
        $ Player.Harem.append(EmmaX)
        if "EmmaYes" in Player.traits:
            $ Player.traits.remove("EmmaYes")
    $ EmmaX.player_petnames.append("boyfriend")
    $ EmmaX.change_face("sexy")
    ch_e "So then. . . how would you like to celebrate?"
    if simulation:
        return True
    $ approval_bonus = 10
    $ Player.add_word(1, "interruption")
    call enter_main_sex_menu(EmmaX)
    $ approval_bonus = 0
    return

label Emma_BF_Jerk:
    $ EmmaX.change_face("angry", 1)
    ch_e "Well! Suit yourself."
    call change_Girl_stat(EmmaX, "obedience", 40)
    if EmmaX.event_happened[5] != 20:
        call change_Girl_stat(EmmaX, "obedience", (20* EmmaX.event_happened[5]))
    if 20 > EmmaX.event_happened[5] >= 3:
        $ EmmaX.change_face("sad")
        ch_e "You know, I'm tired of caring what you think about the matter."
        ch_e "I'm doing to consider us a couple whether you approve or not."
        ch_e "And with that, adieu."
        if simulation:
            return True
        $ EmmaX.player_petnames.append("boyfriend")
        $ achievements.append("I am not your Boyfriend!")
        $ Player.location = "bg_player"
        call remove_Girl(EmmaX)
        call set_the_scene
        $ renpy.pop_call()
        jump player_room
    if EmmaX.event_happened[5] > 1:
        ch_e "It was such a mistake asking you again. You still need to mature."
    if EmmaX.event_happened[5] != 20:
        call change_Girl_stat(EmmaX, "love", -(50* EmmaX.event_happened[5]))
    else:
        call change_Girl_stat(EmmaX, "love", -50)
    ch_e "Get away from me."
    if simulation:
        return
    $ Player.location = "bg_player"
    call remove_Girl(EmmaX)
    $ renpy.pop_call()
    jump player_room


label Emma_Love:
    $ EmmaX.drain_word("asked_to_meet")

    $ Shipping = []

    python:
        for G in all_Girls:
            if G != EmmaX and approval_check(G, 1200, "LO"):
                Shipping.append(G)

    $ Shipshape = len(Shipping)

    if EmmaX.location == Player.location or EmmaX in Player.Party:
        "[EmmaX.name] glances over at you with an apprising look on her face."
    else:
        "[EmmaX.name] turns a corner and notices you."
    if Player.location != "bg_emma" and Player.location != "bg_player":
        "With little word, she takes your hand and pulls you back to her room."
        $ Player.location = "bg_emma"
    $ EmmaX.location = Player.location
    call set_the_scene
    call clear_the_room(EmmaX)
    call set_Character_taboos
    $ EmmaX.daily_history.append("relationship")

    $ EmmaX.change_face("sexy", eyes = "side")
    ch_e "As you are aware, this. . . situation has been going for a while now."
    ch_e "It's been very. . . comfortable for me."
    $ EmmaX.change_face("sexy")
    ch_e "I have enjoyed your company. . . is what I'm trying to say."
    menu:
        extend ""
        "It's more than just company, we're together in this.":
            $ EmmaX.change_face("smile", 1)
            call change_Girl_stat(EmmaX, "love", 10)
            call change_Girl_stat(EmmaX, "inhibition", 5)
            ch_e "Yes!"
            ch_e "Yes, we certainly are more than that."
            $ EmmaX.change_face("sly")
            ch_e "You must have read my mind."
        "I've enjoyed it a lot too.":
            $ EmmaX.change_face("sly")
            call change_Girl_stat(EmmaX, "love", 5)
            call change_Girl_stat(EmmaX, "obedience", 2)
            ch_e "Yes, I imagine you have."
            ch_e "Perhaps it was more than that though. . ."
        "Yeah, it's been fun.":
            $ EmmaX.change_face("confused")
            call change_Girl_stat(EmmaX, "obedience", 5)
            ch_e "Yes, \"fun.\""
            $ EmmaX.change_face("angry", eyes = "side")
            ch_e "It is fun, but I was thinking. . ."
            $ EmmaX.change_face("sly")
        "Oh, ok.":
            $ EmmaX.change_face("confused", eyes = "side")
            ch_e "Um, yes. . ."
            ch_e ". . ."
            $ EmmaX.change_face("confused")
            ch_e "I'm not sure I was clear. . ."
        "Yeah, you're a good ride.":
            $ EmmaX.change_face("angry")
            if not approval_check(EmmaX, 1600):
                call change_Girl_stat(EmmaX, "obedience", -5)
                call change_Girl_stat(EmmaX, "inhibition", -5)
                $ EmmaX.eyes = "side"
                ch_e "Never mind, this was a bad idea."
                jump Emma_Love_End
            ch_e "Such impertinence!"
            if approval_check(EmmaX, 1000, "OI"):
                $ EmmaX.change_face("sly", 2)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                call change_Girl_stat(EmmaX, "lust", 5)
                ch_e "I am though, yes."
                $ EmmaX.blushing = "_blush1"
            else:
                $ EmmaX.change_face("sexy")
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                ch_e "I suppose that's part of your charm though."

    ch_e "I certainly do care for you. . ."
    ch_e "Perhaps more than I have for anyone else in a long time."
    if approval_check(EmmaX, 1600):
        $ EmmaX.change_face("sexy", eyes = "side")
        ch_e "Perhaps more than I ever have."
    ch_e ". . ."
    ch_e "What I'm trying to say is. . ."
    $ EmmaX.change_face("sexy", brows = "sad")
    ch_e "I love you."
    menu:
        extend ""
        "I love you too, [EmmaX.petname]!":
            $ EmmaX.change_face("smile", 2)
            call change_Girl_stat(EmmaX, "love", 20)
            call change_Girl_stat(EmmaX, "inhibition", 10)
            ch_e "I dearly hoped that you did!"
            $ EmmaX.player_petnames.append("lover")
            jump Emma_Love_End
        "Wow! That's cool.":
            $ EmmaX.change_face("confused")
            call change_Girl_stat(EmmaX, "love", 5)
            ch_e "Cool?"
            ch_e "Don't you have anything else you'd like to say to me?"
            $ EmmaX.change_face("sadside", 2)
        "Oh, ok.":
            $ EmmaX.change_face("confused", 2)
            call change_Girl_stat(EmmaX, "obedience", 5)
            call change_Girl_stat(EmmaX, "inhibition", -5)
            ch_e "Ok?"
            $ EmmaX.change_face("angry")
            ch_e "Is that all the response you have for me?"
        "Ha!":
            $ EmmaX.change_face("surprised", 2)
            call change_Girl_stat(EmmaX, "love", -5)
            call change_Girl_stat(EmmaX, "obedience", 10)
            call change_Girl_stat(EmmaX, "inhibition", -5)
            ch_e "!"
            $ EmmaX.change_face("angry", 2)
            ch_e "Well that's hardly the response I expected."
    ch_e "I would hope that you also love me. . ."
    menu:
        extend ""
        "Oh! Yes, of course I love you, [EmmaX.petname]!":
            $ EmmaX.name_check()
            $ EmmaX.change_face("smile", 2)
            call change_Girl_stat(EmmaX, "love", 15)
            call change_Girl_stat(EmmaX, "obedience", 2)
            ch_e "I dearly hoped that you did!"
            $ EmmaX.player_petnames.append("lover")
            jump Emma_Love_End
        "Oh. Oooooh! Yeah, sure.":
            if approval_check(EmmaX, 1200, "OI"):
                $ EmmaX.change_face("sly", 1)
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 10)
            if approval_check(EmmaX, 1200, "OI"):
                $ EmmaX.change_face("sly", 1, brows = "angry")
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "inhibition", -5)
            ch_e "I'm glad to see that you caught up with the situation."
        "Oh. That's awkward.":
            $ EmmaX.change_face("angry", 2)
            call change_Girl_stat(EmmaX, "love", -15)
            call change_Girl_stat(EmmaX, "obedience", 15)
            call change_Girl_stat(EmmaX, "inhibition", -10)
            ch_e "Awkward?!"
            ch_e "This situation is about to become considerably more \"awkward.\""
            $ EmmaX.blushing = "_blush1"
            $ line = "angry"

    ch_e "I'm giving you one last chance here."
    ch_e "This is not a time for fooling around."
    ch_e "Do you love me, or not?"
    menu:
        extend ""
        "Yes, of course I love you, [EmmaX.petname]!":
            $ EmmaX.name_check()
            $ EmmaX.change_face("sly", 2)
            call change_Girl_stat(EmmaX, "love", 5)
            call change_Girl_stat(EmmaX, "obedience", 15)
            call change_Girl_stat(EmmaX, "inhibition", 5)
            ch_e "Took you long enough to get there."
            $ EmmaX.player_petnames.append("lover")
            jump Emma_Love_End
        "I can't really say yet.":
            if line != "angry" or approval_check(EmmaX, 800, "OI"):
                $ EmmaX.change_face("sadside")
                call change_Girl_stat(EmmaX, "obedience", 5)
            else:
                $ EmmaX.change_face("angry")
                call change_Girl_stat(EmmaX, "love", -5)
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "inhibition", -5)
            ch_e "Oh."
        "No.":
            if line == "angry" or not approval_check(EmmaX, 800, "OI"):
                $ EmmaX.change_face("angry")
                call change_Girl_stat(EmmaX, "love", -10)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", -5)
            else:
                $ EmmaX.change_face("sadside")
                call change_Girl_stat(EmmaX, "love", -10)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", -5)
            ch_e "Oh."

    ch_e "Is it because of someone else?"
    $ line = 0
    menu:
        extend ""
        "Yes, it's [RogueX.name]." if RogueX in Shipping and Shipshape < 3:
            $ line = RogueX
        "Yes, it's [KittyX.name]." if KittyX in Shipping and Shipshape < 3:
            $ line = KittyX
        "Yes, it's [LauraX.name]." if LauraX in Shipping and Shipshape < 3:
            $ line = LauraX
        "Yes, it's the others" if Shipshape > 1:
            call change_Girl_stat(EmmaX, "obedience", 15)
            call change_Girl_stat(EmmaX, "inhibition", 5)
            call change_Girl_stat(EmmaX, "lust", 5)
            ch_e "I suppose I can't blame you there."
        "There's nobody else.":
            $ EmmaX.change_face("sadside")
            call change_Girl_stat(EmmaX, "love", -15)
            call change_Girl_stat(EmmaX, "obedience", 15)
            call change_Girl_stat(EmmaX, "inhibition", 5)
            if approval_check(EmmaX, 1000, "OI"):
                ch_e "Hmmm. . . well I suppose I can take solace in that."
            else:
                ch_e "I see."
        "It's a \"you\" problem.":
            $ EmmaX.change_face("angry")
            call change_Girl_stat(EmmaX, "love", -25)
            call change_Girl_stat(EmmaX, "obedience", 15)
            ch_e "Oh is it now?"
            call change_Girl_stat(EmmaX, "love", -10)
            ch_e "I can think of a great many ways to make this a \"you\" problem."
            $ EmmaX.recent_history.append("angry")
            $ EmmaX.daily_history.append("angry")
    if line:

        if EmmaX.likes[line.tag] >= 800:
            call change_Girl_stat(EmmaX, "love", 5)
            call change_Girl_stat(EmmaX, "obedience", 20)
            call change_Girl_stat(EmmaX, "inhibition", 5)
            call change_Girl_stat(EmmaX, "lust", 5)
            ch_e "Yes, she is lovely."
        else:
            $ EmmaX.change_face("angry", eyes = "side")
            call change_Girl_stat(EmmaX, "love", -5)
            call change_Girl_stat(EmmaX, "obedience", 20)
            ch_e "That cow!"
            $ EmmaX.recent_history.append("angry")
            $ EmmaX.check_if_likes(line,800, -50, 1)
    ch_e "I suppose I'll just have to let this go."
    ch_e "I'll. . . see you in a bit."
    ch_e "I need some time to consider this."


label Emma_Love_End:
    if "lover" not in EmmaX.player_petnames:
        call remove_Girl(EmmaX)
        $ EmmaX.location = "hold"
        return

    "[EmmaX.name] pulls closer to you and snuggles into your arms."
    call change_Girl_stat(EmmaX, "love", 25)
    call change_Girl_stat(EmmaX, "lust", 5)
    ch_e "So. . . now that we have some time together. . ."
    call change_Girl_stat(EmmaX, "lust", 10)

    if not EmmaX.permanent_History["sex"]:
        ch_e "I think we've certainly waited long enough. . ."
    else:
        ch_e "Whatever do you intend to do about it?"
    $ Player.add_word(1, "interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            call change_Girl_stat(EmmaX, "inhibition", 20)
            call change_Girl_stat(EmmaX, "obedience", 10)
            ch_e "Hmm. . ."

            call before_action(EmmaX, "sex")
        "I have something else in mind. . .[[choose another activity]":
            $ EmmaX.brows = "confused"
            call change_Girl_stat(EmmaX, "obedience", 25)
            ch_e "Something like. . ."
            $ approval_bonus = 20
            call enter_main_sex_menu(EmmaX)
    return

label Emma_Love_Redux:

    $ line = 0
    $ EmmaX.daily_history.append("relationship")
    if EmmaX.event_happened[6] >= 25:

        ch_p "I hope you've forgiven me, I still love you."
        call change_Girl_stat(EmmaX, "love", 10)
        if approval_check(EmmaX, 950, "L"):
            $ line = "love"
        else:
            $ EmmaX.change_face("angry")
            ch_e "I don't believe you're sufficiently contrite, [EmmaX.player_petname]."
            $ EmmaX.eyes = "side"
            ch_e ". . ."
            $ EmmaX.change_face("angry", mouth = "lipbite")
            ch_e "I didn't tell you to stop."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ EmmaX.change_face("perplexed", 1)
        ch_e ". . ."
        $ EmmaX.change_face("angry", eyes = "side")
        ch_e "I believe I do remember something to that effect, yes."
    if line != "love":
        menu:
            extend ""
            "I'm sorry, I didn't mean it.":
                $ EmmaX.eyes = "surprised"
                ch_e "Oh? So you do love me?"
                ch_p "Yeah. I mean, yes, I love you, [EmmaX.name]."
                call change_Girl_stat(EmmaX, "love", 10)
                if approval_check(EmmaX, 950, "L"):
                    $ line = "love"
                else:
                    $ EmmaX.change_face("sadside")
                    ch_e "I'm not sure that I still do. . ."
            "I've changed my mind, so. . .":
                if approval_check(EmmaX, 950, "L"):
                    $ line = "love"
                    $ EmmaX.eyes = "surprised"
                    ch_e "Oh?"
                else:
                    $ EmmaX.mouth = "sad"
                    ch_e "Oh, you've changed your mind. Lovely."
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    $ EmmaX.change_face("sadside")
                    ch_e "Perhaps I have too. . ."
            "Um, never mind.":
                call change_Girl_stat(EmmaX, "love", -30)
                call change_Girl_stat(EmmaX, "obedience", 10)
                $ EmmaX.change_face("angry")
                ch_e "Don't you dare."
                $ EmmaX.recent_history.append("angry")
    if line == "love":
        call change_Girl_stat(EmmaX, "love", 40)
        call change_Girl_stat(EmmaX, "obedience", 10)
        call change_Girl_stat(EmmaX, "inhibition", 10)
        $ EmmaX.change_face("smile")
        ch_e "I couldn't be happier!"
        ch_e "I love you too, [EmmaX.player_petname]!"
        if EmmaX.event_happened[6] < 25:
            $ EmmaX.change_face("sly")
            "She grabs the back of your head and pulls you close."
            ch_e "You shouldn't have kept me waiting."
        $ EmmaX.player_petnames.append("lover")
    $ EmmaX.event_happened[6] = 25
    return



label Emma_Sub:
    $ EmmaX.drain_word("asked_to_meet")
    $ shift_focus (EmmaX)

    if EmmaX.location != Player.location and EmmaX not in Player.Party:
        "[EmmaX.name] shows up and says she needs to talk to you."
    else:
        "[EmmaX.name] approaches you, looking to talk."
    $ EmmaX.location = Player.location
    call set_the_scene
    call clear_the_room (EmmaX)
    call set_Character_taboos
    $ EmmaX.daily_history.append("relationship")
    $ EmmaX.change_face("bemused", 1)

    $ line = 0
    ch_e "I've been noticing, you have a sort of"
    ch_e ". . . commanding air about you, [EmmaX.player_petname]."
    menu:
        extend ""
        "I guess. That's just kind of what comes naturally for me.":
            call change_Girl_stat(EmmaX, "obedience", 10)
            call change_Girl_stat(EmmaX, "inhibition", 5)
        "Sorry. I didn't mean to come off like that.":
            $ EmmaX.change_face("startled", 2)
            call change_Girl_stat(EmmaX, "love", 5)
            call change_Girl_stat(EmmaX, "obedience", -5)
            call change_Girl_stat(EmmaX, "inhibition", -5)
            ch_e "Oh, don't apologize. . ."
        "Yup. Deal with it.":
            if approval_check(EmmaX, 1000, "LO"):
                call change_Girl_stat(EmmaX, "obedience", 20)
                call change_Girl_stat(EmmaX, "inhibition", 10)
                ch_e "Ehem. . ."
            else:
                call change_Girl_stat(EmmaX, "love", -10)
                call change_Girl_stat(EmmaX, "obedience", 10)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                $ EmmaX.change_face("angry")
                ch_e "Well, that wasn't exactly what I had in mind."
                menu:
                    extend ""
                    "Guess you don't know me so well, huh?":
                        ch_e "I suppose that I don't."
                        $ line = "rude"
                    "Sorry. I kind of thought you were getting into me being like that.":
                        $ EmmaX.change_face("sexy", 2)
                        $ EmmaX.eyes = "side"
                        call change_Girl_stat(EmmaX, "love", 5)
                        call change_Girl_stat(EmmaX, "obedience", 5)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "Not. . . quite like that, no. . ."

    if not line:

        ch_e "What I was getting at, is that I think that I tend to. . ."
        $ EmmaX.change_face("sly", 2)
        ch_e "-enjoy when you take a firm hand with me."
        $ EmmaX.change_face("smile", 1)
        menu:
            extend ""
            "Good. If you wanna be with me, that's how it'll be.":
                if approval_check(EmmaX, 1000, "LO"):
                    call change_Girl_stat(EmmaX, "obedience", 15)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                else:
                    $ EmmaX.change_face("sadside", 1)
                    call change_Girl_stat(EmmaX, "love", -5)
                    call change_Girl_stat(EmmaX, "obedience", 10)
                ch_e "Perhaps with a touch more class, [EmmaX.player_petname]. . ."
                menu:
                    extend ""
                    "Whatever. That's how it is. Take it or leave it.":
                        $ EmmaX.change_face("angry")
                        call change_Girl_stat(EmmaX, "love", -10)
                        call change_Girl_stat(EmmaX, "obedience", 5)
                        ch_e "I suppose you could use a bit more maturity first."
                        $ line = "rude"
                    "I think I could maybe do that.":
                        $ EmmaX.change_face("bemused", 2)
                        $ EmmaX.eyes = "side"
                        call change_Girl_stat(EmmaX, "love", 5)
                        call change_Girl_stat(EmmaX, "obedience", 3)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        ch_e "That's good to hear."
            "Yeah? You think it's sexy?":

                $ EmmaX.change_face("bemused", 2)
                $ EmmaX.eyes = "side"
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "inhibition", 10)
            "You sure you don't want me to back off a little?":


                $ EmmaX.change_face("startled", 1)
                call change_Girl_stat(EmmaX, "obedience", -5)
                menu:
                    ch_e "I wouldn't want to make you. . . uncomfortable."
                    "Only if you're okay with it.":
                        $ EmmaX.change_face("bemused", 2)
                        call change_Girl_stat(EmmaX, "love", 10)
                        call change_Girl_stat(EmmaX, "inhibition", 10)
                        $ line = 0
                    "Uhm. . .yeah. I {i}do{/i} think it's weird. Sorry.":
                        call change_Girl_stat(EmmaX, "love", -15)
                        call change_Girl_stat(EmmaX, "obedience", -5)
                        call change_Girl_stat(EmmaX, "inhibition", -10)
                        $ line = "embarrassed"
            "I don't really care what you like. I do what I want.":

                call change_Girl_stat(EmmaX, "love", -10)
                call change_Girl_stat(EmmaX, "obedience", 15)
                $ EmmaX.change_face("angry")
                ch_e "Ugh. I think I may have misjudged you."
                $ line = "rude"

    if not line:
        $ EmmaX.change_face("bemused", 1, eyes = "side")
        ch_e "I'm more used to being in charge of the situation."
        ch_e "When you take control of things. . ."
        ch_e "I find it quite. . . exciting."
        menu:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                call change_Girl_stat(EmmaX, "love", -5)
                call change_Girl_stat(EmmaX, "inhibition", -15)
                ch_e "Not at all, just perhaps a bit. . . unconventional."
            "I think I could get used to that kinda thing.":
                call change_Girl_stat(EmmaX, "obedience", 5)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                $ EmmaX.change_face("smile", 1)

    if not line:
        $ EmmaX.change_face("smile", 1)
        ch_e "That sounds delightful. If you don't mind, could I refer to you as. . . sir?"
        $ EmmaX.change_face("sly", 2)
        ch_e "Would you enjoy that?"
        $ EmmaX.blushing = "_blush1"
        menu:
            extend ""
            "That has a nice ring to it.":
                call change_Girl_stat(EmmaX, "love", 5)
                call change_Girl_stat(EmmaX, "obedience", 15)
                call change_Girl_stat(EmmaX, "inhibition", 5)
                ch_e "Very well then. . .{i}sir{/i}."
                $ EmmaX.player_petname = "sir"
            "I think I'd rather stick with what we've got going.":
                $ EmmaX.change_face("confused", 2)
                ch_e "Hmm."
                call change_Girl_stat(EmmaX, "inhibition", -5)
                $ EmmaX.change_face("sadside", 1)
                menu:
                    ch_e ". . . could you perhaps still take the lead in things?"
                    "I like that idea.":
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        $ EmmaX.change_face("smile", 1)
                        ch_e "That should do then, [EmmaX.player_petname]."
                    "This is getting really awkward.":
                        call change_Girl_stat(EmmaX, "love", -10)
                        call change_Girl_stat(EmmaX, "obedience", -50)
                        call change_Girl_stat(EmmaX, "inhibition", -15)
                        $ line = "embarrassed"


    $ EmmaX.history.append("sir")
    if not line:
        $ EmmaX.blushing = "_blush1"
        $ EmmaX.player_petnames.append("sir")

    elif line == "rude":
        call remove_Girl(EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] marches out the door in a huff, leaving you alone."
    elif line == "embarrassed":
        $ EmmaX.change_face("sad", 2)
        ch_e "Well, I. . . um. . ."
        $ EmmaX.change_face("sly", 1)
        ch_e "I was testing you. Obviously. That would be unprofessional."
        $ EmmaX.change_face("sadside", 2)
        ch_e "I should go. I think I see a student over there in need."
        $ EmmaX.blushing = "_blush1"
        call remove_Girl(EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] dashes out the door, leaving you alone. It didn't look like she could get away fast enough."
    return

label Emma_Sub_Asked:
    $ line = 0
    $ EmmaX.change_face("sadside", 1)
    ch_e "I might."
    ch_e "If I did, I would also remember that you seemed unprepared for the role."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in EmmaX.player_petnames and approval_check(EmmaX, 850, "O"):

                pass
            elif approval_check(EmmaX, 550, "O"):

                pass
            else:
                ch_e "Perhaps when you've done a bit more soul-searching. . ."
                $ line = "rude"

            if line != "rude":
                call change_Girl_stat(EmmaX, "love", 10)
                $ EmmaX.change_face("sly", 1)
                ch_e "I suppose I could give you another chance."
                ch_e "I appreciate that you recognize you made an error."
                ch_e "Fine, we can give it another try."
        "Listen. . .I know it's what you want. Do you want to try again, or not?":

            $ EmmaX.change_face("bemused", 1)
            if "sir" in EmmaX.player_petnames and approval_check(EmmaX, 850, "O"):
                ch_e "Ok, fine."
            elif not approval_check(EmmaX, 600, "O"):
                ch_e "Not at the moment, no."
                $ line = "rude"
            else:

                $ EmmaX.change_face("sadside", 1)
                ch_e "You do tend to push your luck."
                $ EmmaX.eyes = "squint"
                ch_e "Perhaps you are right, but I do think an apology is still in order."
                menu:
                    extend ""
                    "Okay, I'm sorry I was so rude about it.":
                        call change_Girl_stat(EmmaX, "love", 15)
                        call change_Girl_stat(EmmaX, "inhibition", 10)
                        $ EmmaX.change_face("bemused", 1, eyes = "side")
                        ch_e "Apology accepted. . ."
                    "Not gonna happen.":
                        if "sir" in EmmaX.player_petnames and approval_check(EmmaX, 900, "O"):
                            call change_Girl_stat(EmmaX, "love", -5)
                            call change_Girl_stat(EmmaX, "obedience", 10)
                            ch_e ". . ."
                        elif approval_check(EmmaX, 650, "O"):
                            call change_Girl_stat(EmmaX, "love", -5)
                            call change_Girl_stat(EmmaX, "obedience", 10)
                            ch_e "I- um. . .hmmm. . ."
                        else:
                            call change_Girl_stat(EmmaX, "love", -10)
                            call change_Girl_stat(EmmaX, "obedience", -10)
                            call change_Girl_stat(EmmaX, "obedience", -10)
                            call change_Girl_stat(EmmaX, "inhibition", -15)
                            "[EmmaX.name] sighs and rolls her eyes."
                            $ EmmaX.change_face("angry", 1, eyes = "side")
                            ch_e "You really don't learn, do you?"
                            $ line = "rude"
                    "Ok, never mind then.":
                        $ EmmaX.change_face("angry", 1)
                        call change_Girl_stat(EmmaX, "love", -10)
                        call change_Girl_stat(EmmaX, "obedience", -10)
                        call change_Girl_stat(EmmaX, "obedience", -10)
                        call change_Girl_stat(EmmaX, "inhibition", -15)
                        ch_e "I don't know what I saw in you."
                        $ line = "rude"

    $ EmmaX.recent_history.append("asked sub")
    $ EmmaX.daily_history.append("asked sub")
    if line == "rude":

        call remove_Girl(EmmaX)
        $ EmmaX.recent_history.append("angry")
        $ renpy.pop_call()
        "[EmmaX.name] marches out the door, leaving you alone. She looked pretty upset."
    elif "sir" in EmmaX.player_petnames:

        call change_Girl_stat(EmmaX, "obedience", 50)
        $ EmmaX.player_petnames.append("master")
        $ EmmaX.player_petname = "master"
        $ EmmaX.eyes = "squint"
        ch_e ". . . master. . ."
    else:

        call change_Girl_stat(EmmaX, "obedience", 30)
        $ EmmaX.player_petnames.append("sir")
        $ EmmaX.player_petname = "sir"
        $ EmmaX.eyes = "squint"
        ch_e ". . . sir."
    return






label Emma_Master:
    $ EmmaX.drain_word("asked_to_meet")
    $ shift_focus (EmmaX)
    $ EmmaX.location = Player.location
    call set_the_scene
    if EmmaX.location != Player.location and EmmaX not in Player.Party:
        "[EmmaX.name] shows up and says she needs to talk to you."
    else:
        "[EmmaX.name] approaches you, looking to talk."
    call clear_the_room (EmmaX)
    $ EmmaX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ EmmaX.change_face("bemused", 1)
    ch_e "[EmmaX.player_petname], if you don't mind my saying so. . ."
    ch_e "I do think that your more. . . assertive direction has been quite. . ."
    ch_e ". . . exhilarating."
    menu:
        extend ""
        "I like it too.":
            $ EmmaX.change_face("sly", 1)
            ch_e "Good, good. . ."
            ch_e "That being the case, perhaps we would be able to. . ."
            ch_e "Go a bit deeper?"
            menu:
                extend ""
                "Nah. This is just about perfect.":
                    $ EmmaX.change_face("sad", 1)
                    call change_Girl_stat(EmmaX, "obedience", -15)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    ch_e "Oh? I suppose. . ."
                    $ line = "fail"
                "What'd you have in mind?":
                    $ EmmaX.eyes = "side"
                    ch_e "Hmm, well I was just considering, perhaps I could refer to you as. . ."
                    ch_e ". . . {i}master{/i}?"
                    $ EmmaX.eyes = "squint"
                    ch_e "Would you like that? Would that appeal to you?"
                    menu:
                        extend ""
                        "Oh, yeah. I'd like that.":
                            ch_e "Lovely. . ."
                        "Uhm. . .nah. That's too much.":
                            $ EmmaX.change_face("sad", 1)
                            call change_Girl_stat(EmmaX, "obedience", -15)
                            call change_Girl_stat(EmmaX, "inhibition", 5)
                            ch_e "Oh. Very well then, forget I said anything about it."
                            ch_e "Forget. . . forget. . . "
                            ch_e "Oh, never mind, I forgot that doesn't actually work on you."
                            ch_e "Just, be discreet."
                            $ line = "fail"
                "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":

                    $ EmmaX.change_face("sly", 1)
                    call change_Girl_stat(EmmaX, "love", 15)
                    call change_Girl_stat(EmmaX, "obedience", -10)
                    call change_Girl_stat(EmmaX, "inhibition", 10)
                    ch_e "Well, I suppose you must be true to your nature. . ."
                    $ line = "fail"
                "Actually, let's stop that. It's creeping me out.":

                    $ EmmaX.change_face("perplexed", 2)
                    call change_Girl_stat(EmmaX, "love", -10)
                    call change_Girl_stat(EmmaX, "obedience", -50)
                    call change_Girl_stat(EmmaX, "inhibition", -15)
                    ch_e "Well. We wouldn't want that now."
                    $ EmmaX.blushing = "_blush1"
                    $ line = "embarrassed"
        "As if I care what you think, slut.":

            $ EmmaX.change_face("angry", 1)
            call change_Girl_stat(EmmaX, "love", -20)
            call change_Girl_stat(EmmaX, "obedience", 10)
            call change_Girl_stat(EmmaX, "inhibition", -10)
            menu:
                ch_e "What was that?"
                "Sorry. I just don't care what you want.":
                    if approval_check(EmmaX, 1400, "LO"):
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        ch_e "That's. . ."
                        $ EmmaX.change_face("sly", 1)
                        call change_Girl_stat(EmmaX, "love", 20)
                        call change_Girl_stat(EmmaX, "inhibition", 15)
                        ch_e ". . .not entirely off the mark."
                    else:
                        call change_Girl_stat(EmmaX, "love", -15)
                        call change_Girl_stat(EmmaX, "obedience", -10)
                        call change_Girl_stat(EmmaX, "inhibition", 5)
                        $ EmmaX.change_face("angry", 1)
                        ch_e "!!!"
                        $ line = "rude"
                "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "obedience", 10)
                    call change_Girl_stat(EmmaX, "inhibition", 5)
                    ch_e "You. . . may have a bit of work to do on that."
        "Not me. It's kind of creepy.":

            $ EmmaX.change_face("sad", 2)
            call change_Girl_stat(EmmaX, "love", -10)
            call change_Girl_stat(EmmaX, "obedience", -20)
            call change_Girl_stat(EmmaX, "inhibition", -25)
            ch_e "Oh. Well we wouldn't want that. . ."
            $ line = "embarrassed"

    $ EmmaX.history.append("master")
    if line == "rude":
        $ EmmaX.recent_history.append("angry")
        call remove_Girl(EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] storms out the door in a huff."
    elif line == "embarrassed":
        call remove_Girl(EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] dashed out of the room, leaving you alone. She looked really embarrassed."
    elif line != "fail":
        call change_Girl_stat(EmmaX, "obedience", 50)
        $ EmmaX.player_petnames.append("master")
        $ EmmaX.player_petname = "master"
        ch_e ". . .master."
    return






label Emma_Sexfriend:
    $ EmmaX.drain_word("asked_to_meet")

    if EmmaX in Player.Harem:
        $ EmmaX.player_petnames.append("sex friend")
        return
    $ EmmaX.location = Player.location
    call set_the_scene
    call clear_the_room (EmmaX, 1, 1)
    $ EmmaX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    "After class, the students file out of the room."
    $ EmmaX.change_face("bemused", 1)
    ch_e "[Player.name], could I have a word with you?"
    menu:
        extend ""
        "I'm in a hurry.":
            $ EmmaX.change_face("angry", 1)
            ch_e "That's. . . not an appropriate response."
            call change_Girl_stat(EmmaX, "love", -20)
            call change_Girl_stat(EmmaX, "obedience", 3)
            $ line = "rude"
        "This doesn't sound good.":

            $ EmmaX.change_face("sly", 1)
            ch_e "Settle down, it's nothing. . . unpleasant."
        "Yeah. What's up?":

            pass

    if not line:
        if approval_check(EmmaX, 850, "L"):
            $ EmmaX.change_face("sly", 1)
            ch_e "I just, enjoy spending time with you, as you're aware?"
            menu:
                extend ""
                "I thought so.":
                    $ EmmaX.change_face("sexy", 1)
                    call change_Girl_stat(EmmaX, "love", 10)
                    call change_Girl_stat(EmmaX, "inhibition", 5)
                    ch_e "I {i}was{/i} hoping you'd be aware, [EmmaX.player_petname]."
                "Really?":
                    $ EmmaX.change_face("perplexed", 1)
                    ch_e "Um, yes."
                "Don't complicate things.":

                    $ EmmaX.change_face("angry", 1)
                    call change_Girl_stat(EmmaX, "love", -10)
                    call change_Girl_stat(EmmaX, "obedience", 5)
                    call change_Girl_stat(EmmaX, "inhibition", -5)
                    ch_e "I'm sorry if you find this discussion too \"complicated.\""
                    $ line = "rude"
        elif approval_check(EmmaX, 1000, "LI"):
            $ EmmaX.change_face("sexy", 1)
            ch_e "I just thought you should know how. . . intriguing I find you."
            menu:
                extend ""
                "That's really nice of you to say.":
                    call change_Girl_stat(EmmaX, "love", 5)
                    call change_Girl_stat(EmmaX, "inhibition", 5)
                    ch_e "Certainly."
                "Me? You really think so?":
                    ch_e "Don't be overly modest, [EmmaX.player_petname]."
                "Are you going somewhere with this?":
                    $ EmmaX.change_face("angry")
                    ch_e "Perhaps not."
                    $ line = "rude"
        else:
            $ EmmaX.mouth = "smile"
            $ EmmaX.brows = "sad"
            $ EmmaX.eyes = "side"
            ch_e "This may sound a bit. . . unconventional."
            menu:
                extend ""
                "Well, you've got me intrigued. Now you {i}have{/i} to tell me.":
                    ch_e "You'll keep this between the two of us?"
                    menu:
                        extend ""
                        "[EmmaX.name]. . . I really like you. I promise.":
                            $ EmmaX.change_face("smile")
                            call change_Girl_stat(EmmaX, "love", 10)
                            call change_Girl_stat(EmmaX, "inhibition", 5)
                            ch_e "Very well. . ."
                        "Uhm. . . okay?":
                            ch_e "Well. . ."
                        "No promises.":
                            $ EmmaX.change_face("perplexed", 2)
                            call change_Girl_stat(EmmaX, "inhibition", -5)
                            ch_e "Hmm. . . never mind, then."
                            $ line = "embarrassed"
                "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                    $ EmmaX.change_face("angry", 1)
                    ch_e "Live in suspense then."
                    $ line = "rude"

    if not line:
        ch_e "I was considering. . . "
        ch_e "Perhaps we could take our relationship a little further, if you wanted to."
        menu:
            extend ""
            "You mean. . . like, being {i}friends with benefits{/i}?":
                ch_e "I suppose you could put it that way."
                ch_e "What do you think?"
                menu:
                    extend ""
                    "Sounds amazing! Count me in.":
                        $ EmmaX.change_face("smile", 1)
                        call change_Girl_stat(EmmaX, "love", 10)
                        call change_Girl_stat(EmmaX, "obedience", 10)
                        call change_Girl_stat(EmmaX, "inhibition", 50)
                        call change_Girl_stat(EmmaX, "lust", 5)
                        "[EmmaX.name] leans in and gives you a passionate kiss."
                        $ EmmaX.permanent_History["kiss"] += 1
                        ch_e "I can't wait to get started, [EmmaX.player_petname]."
                    "That's pretty slutty, [EmmaX.name].":
                        if approval_check(EmmaX, 2000):
                            $ EmmaX.change_face("angry", 1, brows = "confused")
                            call change_Girl_stat(EmmaX, "love", -10)
                            call change_Girl_stat(EmmaX, "obedience", 15)
                            ch_e "I suppose you're not wrong."
                        else:
                            $ EmmaX.change_face("angry", 1)
                            call change_Girl_stat(EmmaX, "love", -30)
                            call change_Girl_stat(EmmaX, "obedience", 10)
                            call change_Girl_stat(EmmaX, "inhibition", -20)
                            ch_e "Then I suppose I'll have to take care of that elsewhere!"
                            $ line = "rude"
            "Uhm, to be honest, I'd rather not.":
                $ EmmaX.change_face("sadside", 2)
                call change_Girl_stat(EmmaX, "obedience", 15)
                call change_Girl_stat(EmmaX, "inhibition", -15)
                ch_e "Oh. Suit yourself, I suppose."
                ch_e "I should be leaving."
                $ line = "sad"

    if line == "rude":
        $ EmmaX.change_face("angry", 1)
        $ EmmaX.recent_history.append("angry")
        call change_Girl_stat(EmmaX, "love", -20)
        call change_Girl_stat(EmmaX, "obedience", 5)
        call change_Girl_stat(EmmaX, "inhibition", -10)
        call remove_Girl(EmmaX)
        $ EmmaX.recent_history.append("angry")
        "[EmmaX.name] storms off in a huff. She seemed pretty mad at you."
    elif line == "embarrassed":
        $ EmmaX.change_face("perplexed", 1)
        call change_Girl_stat(EmmaX, "love", -10)
        call change_Girl_stat(EmmaX, "obedience", 5)
        call change_Girl_stat(EmmaX, "inhibition", -20)
        call remove_Girl(EmmaX)
        "[EmmaX.name] dashes out of the room, leaving you alone. That was very strange."
    elif line == "sad":
        call remove_Girl(EmmaX)
        "[EmmaX.name] wanders into the hall, leaving you alone. You think you may have hurt her feelings."
    else:
        $ EmmaX.player_petnames.append("sex friend")
        $ EmmaX.change_face("sly", 2)
        call change_Girl_stat(EmmaX, "inhibition", 10)
        call change_Girl_stat(EmmaX, "lust", 10)
        "[EmmaX.name] leans in and caresses your body."
        "As she does so, you feel a tickle as if her mouth is surrounding your cock."
        "You look back at her and she winks."
        ch_e "I do have a few tricks up my sleeves, [EmmaX.player_petname]."
        ch_e "I'll see you later, I hope."
        call remove_Girl(EmmaX)
        "She leaves the room, and the phantom \"lips\" give you one final kiss. "
    call remove_Girl(EmmaX)
    return






label Emma_Fuckbuddy:
    $ EmmaX.drain_word("asked_to_meet")
    $ EmmaX.daily_history.append("relationship")
    "Out of nowhere, you feel a tongue sliding across your cock."
    "Even though you're fully dressed, it definitely feels like a mouth has enveloped your cock."
    "You look down, but can't see any movement, although your cock has become diamond hard."
    "As you try to control your obvious erection, a voice tickles the back of your mind, "
    ch_e "To me, my X-Man. . ."
    "-and suddenly the pressure is gone."
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on [EmmaX.name] later. . ."
    $ EmmaX.player_petnames.append("fuck buddy")
    $ EmmaX.event_happened[10] += 1
    return




label Emma_Daddy:
    $ EmmaX.drain_word("asked_to_meet")
    $ EmmaX.daily_history.append("relationship")
    $ shift_focus (EmmaX)
    call set_the_scene
    ch_e ". . ."
    if EmmaX in Player.Harem:
        ch_e "We have been dating a while, [EmmaX.player_petname], "
    else:
        ch_e "We have been enjoying ourselves, "
    if EmmaX.love > EmmaX.obedience and EmmaX.love > EmmaX.inhibition:
        ch_e "and you certainly are sweet. . ."
    elif EmmaX.obedience > EmmaX.inhibition:
        ch_e "and you know how to keep me interested. . ."
    else:
        ch_e "and I've been. . . exploring. . ."
    ch_e "I was thinking, would you mind if I call you \"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ EmmaX.change_face("smile")
            call change_Girl_stat(EmmaX, "love", 20)
            call change_Girl_stat(EmmaX, "obedience", 10)
            call change_Girl_stat(EmmaX, "inhibition", 30)
            ch_e "Excellent."
        "What do you mean by that?":
            $ EmmaX.change_face("bemused")
            ch_e "I just find it to be a turn-on, being your baby girl. . ."
            ch_e "I'd prefer to call you that sometimes."
            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ EmmaX.change_face("smile")
                    call change_Girl_stat(EmmaX, "love", 15)
                    call change_Girl_stat(EmmaX, "obedience", 20)
                    call change_Girl_stat(EmmaX, "inhibition", 25)
                    ch_e "Great!"
                    $ EmmaX.change_face("sly", 2)
                    ch_e " . . . daddy."
                    $ EmmaX.change_face("sly", 1)
                    $ EmmaX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(EmmaX, "love", 5)
                    call change_Girl_stat(EmmaX, "obedience", 40)
                    call change_Girl_stat(EmmaX, "inhibition", 20)
                    $ EmmaX.change_face("sad")
                    ch_e " . . . "
                    ch_e "Well, ok."
                "You've got some real daddy issues, uh?":
                    call change_Girl_stat(EmmaX, "love", -15)
                    call change_Girl_stat(EmmaX, "obedience", 45)
                    call change_Girl_stat(EmmaX, "inhibition", 5)
                    $ EmmaX.change_face("angry")
                    ch_e "Let's not get into it."
        "Aren't you a bit old for that?":
            call change_Girl_stat(EmmaX, "love", -15)
            call change_Girl_stat(EmmaX, "obedience", 40)
            call change_Girl_stat(EmmaX, "inhibition", 10)
            $ EmmaX.change_face("angry")
            ch_e "Perhaps this was a bad idea."
    $ EmmaX.player_petnames.append("daddy")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
