label prologue:
    $ time_index = 2
    $ current_time = time_options[time_index]

    $ Player.location = "bg_entrance"

    scene background onlayer background
    scene

    show midground zorder 2
    show foreground zorder 4
    show cover zorder 7
    show Chibi_cock onlayer screens

    if simulation:
        show blue_screen onlayer black

    "You recently discovered that you were a mutant when a Sentinel attacked your home.\nYou were rescued by a squad of X-Men and given this address."
    "You've arrived in the early evening at the Xavier Institute, where you've been promised a new home."
    "Things have been tough for mutants in the years since Apocalypse's fall, but this sounds like it might be a good deal."

    call get_color_transform
    $ color_transform = _return

    show Xavier_sprite at sprite_location(stage_left), color_transform with easeinleft

    ch_x "Welcome to the Xavier Institute for Higher Learning. This is a home for all mutants to learn and grow."
    ch_x "My name is Charles Xavier, and I have dedicated my life to helping other mutants such as yourself."
    ch_x "I know that you've had a difficult time, but you will be safe here."
    ch_x "You'll have classes in the day to teach you the skills you'll need, and training in the Danger Room for self defense."
    ch_x "Since you're on your own, we'll provide a small stipend for your day-to-day needs."
    ch_x "Did you have any questions for me young man?"
    ch_p "Why did you even bring me here, I don't have any \"super powers.\""
    ch_x "Nonsense, my boy. You have an incredibly useful ability. . ."
    ch_x "the power to negate other powers, even including my own."

    $ RogueX.name = "???"
    $ RogueX.location = Player.location
    $ RogueX.change_face("surprised")

    call show_Girl(RogueX, x_position = stage_far_far_right, color_transform = color_transform, transition = easeinright)
    call shift_focus(RogueX)

    ch_r "What's that Prof? This new kid can negate mutant powers?"

    $ RogueX.mouth = "normal"

    call show_Girl(RogueX, x_position = stage_right, transition = ease)

    ch_r "Maybe even my own?"
    ch_x "That is correct, Rogue, though currently, his powers are weak and uncontrolled."

    $ RogueX.name = "Rogue"

    ch_x "One day, however, he may even be able to help you turn your powers off permanently."
    ch_r "! . . ."

    $ RogueX.change_face("smile")

    ch_x "Since you're here, why don't you show our new guest around the mansion?"
    ch_x "This young lady is named [RogueX.name], one of our veteran students."
    ch_x "And [RogueX.name], this young man goes by the name \"[Player.name]\"."

    hide Xavier_sprite with easeoutright

    call show_Girl(RogueX, x_position = stage_center, transition = ease)

    menu:
        ch_r "A pleasure ta meet ya, [RogueX.player_petname]. Let me give ya the lay of the place."
        "It's nice to meet you too.":
            call change_Girl_stat(RogueX, "love", 200, 20)
            $ RogueX.change_face("smile", 1)

            ch_r "Oh, a gentleman. I think we'll really get along."

            $ RogueX.blushing = ""

            ch_r "Ok, so let me show ya around. . ."
        "The \"lay\" of the place, eh?":
            call change_Girl_stat(RogueX, "love", 200, 10)
            $ RogueX.brows = "normal"
            $ RogueX.eyes = "surprised"
            $ RogueX.mouth = "smile"
            $ RogueX.blushing = "_blush1"

            ch_r "Wha- what? N, no, that's not what I meant! I'm just giving you the campus tour!"

            $ RogueX.change_face("bemused")
            call change_Girl_stat(RogueX, "inhibition", 200, 20)
            call change_Girl_stat(RogueX, "obedience", 200, 20)

            ch_r "Hmm. . ."

            call change_Girl_stat(RogueX, "lust", 90, 3)
            $ RogueX.change_face("normal")
            $ RogueX.eyes = "surprised"

            ch_r "Anyways, let's get this back on track. . ."

            $ RogueX.change_face("smile", 0)
        "Whatever.":
            call change_Girl_stat(RogueX, "obedience", 200, 20)
            $ RogueX.change_face("sad")
            $ RogueX.brows = "normal"

            ch_r "Tsk, well ok, let's get started."
        "Screw off.":
            call change_Girl_stat(RogueX, "love", 200, -30)
            call change_Girl_stat(RogueX, "obedience", 200, 30)
            $ RogueX.change_face("angry")

            call show_Girl(RogueX, transition = vpunch)

            ch_r "Well I never!"
            ch_r "Hmph, I have to give the tour anyways, so get mov'in. . ."

    call hide_Girl(RogueX)

label tour_start:
    $ Player.location = "bg_campus"

    call add_Girls(RogueX)

    ch_r "This is the campus square. It links up to all the major locations on campus and you'll probably pass through here a lot."

    call hide_Girl(RogueX)

    $ Player.location = "bg_player"

    call add_Girls(RogueX)

    ch_r "This will be your room, we each get private rooms now that the campus has been expanded."

    menu:
        ch_r "Pretty nice, right?"
        "It is with you in it.":
            $ RogueX.blushing = "_blush1"
            call change_Girl_stat(RogueX, "love", 200, 20)
            call change_Girl_stat(RogueX, "lust", 90, 5)
        "It'll do.":
            call change_Girl_stat(RogueX, "obedience", 200, 10)

    ch_p "And where do you live?"

    $ RogueX.blushing = ""

    ch_r "Oh, right down the hall, all the doors are labeled."

    if RogueX.love <= 500:
        ch_r "I wouldn't recommend bothering me though."
    else:
        ch_r "You can stop by sometime, but not after curfew."

    call hide_Girl(RogueX)

    $ Player.location = "bg_classroom"

    call add_Girls(RogueX)

    ch_r "And this is one of our state-of-the-art classrooms."
    ch_r "They're multi-purpose so they can teach almost anything in them."
    ch_r "This used to just be an after school training facility, but over the past few years it's grown into a full service university."

    call hide_Girl(RogueX)

    $ Player.location = "bg_dangerroom"

    call add_Girls(RogueX)

    ch_r "This is the Danger Room. It's been upgraded to a fully holographic experience, allowing realistic battlefield simulations."

    $ counter = 0

    while counter < 3:
        menu:
            extend ""
            "Why would you need battlefield simulations?" if counter != 1:
                ch_r "The world is a dangerous place, [RogueX.player_petname], especially for us mutants."
                ch_r "This place helps us train to use our powers. Coming here can help you to get a grasp on yours as well."

                $ counter = 3 if counter == 2 else 1
            "So can this place make some more. . . erotic simulations?" if counter != 2:
                $ RogueX.eyes = "side"
                $ RogueX.mouth = "lipbite"
                $ RogueX.blushing = "_blush1"
                call change_Girl_stat(RogueX, "inhibition", 200, 30)
                call change_Girl_stat(RogueX, "lust", 200, 5)

                ch_r "Well. . . I suppose it could. . . if one were into such things."

                $ RogueX.change_face(blushing = 0)

                $ counter = 3 if counter == 1 else 2
            "Ok, let's move on.":
                $ counter = 3

    ch_r "Moving on then. . ."

    call hide_Girl(RogueX)

label tour_end:
    $ Player.location = "bg_campus"

    call add_Girls(RogueX)

    ch_r "Well, that's the nickel tour, now you know where everything is. . ."

    $ RogueX.mouth = "normal"
    $ RogueX.eyes = "normal"
    $ RogueX.brows = "confused"

    menu:
        ch_r "I was curious about your ability. Is it true that other mutant powers don't work on you?"
        "Sure.":
            ch_p "That's what they tell me, but to be honest, I don't know much about it."
        "What's it to you?":
            ch_p "What do you care?"

            $ RogueX.eyes = "sexy"

            ch_r ". . ."

            call change_Girl_stat(RogueX, "love", 200, -30)

    ch_r "Well, you see, my power is the ability to absorb the mutant powers and memories of those I touch."
    ch_r "Only, I still can't really control it. I can't touch people without hurting them, and I might even put them into a coma if I'm not careful."
    ch_r "So I was hoping that maybe with your power. . ."

    $ RogueX.change_face("sexy")
    $ RogueX.brows = "sad"

    menu:
        ch_r "So I was hoping that maybe with your power. . . I could touch you?"
        "Like, a kiss?":
            if RogueX.love >= 500:
                call change_Girl_stat(RogueX, "love", 200, 20)
                call change_Girl_stat(RogueX, "obedience", 200, 30)
                call change_Girl_stat(RogueX, "inhibition", 20, 20)
                $ RogueX.change_face("surprised", 1)

                ch_r "Well, aren't you fresh."

                $ RogueX.change_face("sexy")
                $ RogueX.mouth = "smile"

                ch_r "Just this once."

                call smooch(RogueX)

                "She gives you a little peck on the cheek."

                $ RogueX.change_face("smile")
            else:
                call change_Girl_stat(RogueX, "love", 200, 30)
                $ RogueX.change_face("bemused")

                ch_r "Heh, You'll have to earn that [RogueX.player_petname]."

                $ RogueX.change_out_of("gloves")
                $ RogueX.arm_pose = 2
                $ RogueX.change_face("sexy", brows = "sad")

                "She pulls off her glove and touches your face."
        "Ok, be my guest.":
            call change_Girl_stat(RogueX, "love", 200, 30)
            $ RogueX.change_face("smile")
            $ RogueX.change_out_of("gloves")
            $ RogueX.arm_pose = 2
            $ RogueX.change_face("sexy", brows = "sad")

            "She pulls off her glove and touches your face."
        "No, that's weird.":
            call change_Girl_stat(RogueX, "love", 200, -30)
            call change_Girl_stat(RogueX, "inhibition", 200, 30)
            $ RogueX.change_face("sad", brows = "normal")

            ch_r "Well I'm just too damned curious, sorry."

            $ RogueX.change_out_of("gloves")
            $ RogueX.arm_pose = 2

            "She pulls off her glove and touches your face."

    $ RogueX.change_face("surprised")

    ch_r "Wow."
    ch_r "This is amazing! With anyone else I would have drained their powers and they'd be out by now."

    $ RogueX.change_face("sexy")

    menu:
        ch_r "Do you know how long it's been since I've felt human contact without hurting them?"
        "Glad I could help.":
            call change_Girl_stat(RogueX, "love", 200, 10)
        "I'm guessing it's been quite a while.":
            call change_Girl_stat(RogueX, "lust", 200, 5)
            $ RogueX.change_face("bemused", 1)

            ch_r ". . ."

    $ RogueX.change_face("smile")

    ch_r "What a rush. I guess that's it then, I'm heading back to my room, you can head to yours."

    $ RogueX.blushing = ""

    if RogueX.love >= 500:
        ch_r "Maybe I'll see you around though. Here's my number, you can give me a call."

        if not simulation:
            $ Player.Phonebook.append(RogueX)

    $ RogueX.change_into("black gloves")
    $ RogueX.arm_pose = 1
    $ RogueX.addiction_rate = 5

label tour_parting:
    $ RogueX.emotion = "normal"
    $ RogueX.blushing = ""

    if not RogueX.action_counter["kiss"]:
        $ line = "Want to make out a little?"
    else:
        $ line = "Want to make out a little more?"

    menu:
        extend ""
        "Ok, see you later.":
            call remove_Girl(RogueX)

            "You head back to your room."
        "[line]":
            if RogueX.love >= 560:
                $ RogueX.change_face("bemused", 1)
                call change_Girl_stat(RogueX, "inhibition", 10, 20)
                call change_Girl_stat(RogueX, "inhibition", 50, 10)

                if simulation:
                    return True

                call start_action(RogueX, "kiss")

                if "angry" in RogueX.recent_history:
                    call change_Girl_stat(RogueX, "love", 200, -10)
                    call change_Girl_stat(RogueX, "obedience", 200, 30)

                    ch_r "What the hell, [Player.name]?!"
                    ch_r "Way to take advantage of a girl's feelings there!"

                    call remove_Girl(RogueX)

                    "[RogueX.name] tears off and you head back to your room."
                else:
                    $ RogueX.change_face("bemused", 1)

                    ch_r "That was real nice, [RogueX.player_petname]. I'll definitely be seeing you later."

                    call remove_Girl(RogueX)

                    "You head back to your room."
            else:
                if (RogueX.love >= 530 or RogueX.obedience > 50) and not RogueX.action_counter["kiss"]:
                    $ RogueX.addiction_rate += 1
                    call change_Girl_stat(RogueX, "lust", 200, 5)
                    call change_Girl_stat(RogueX, "love", 200, 10)
                    $ RogueX.action_counter["kiss"] += 1
                    $ RogueX.change_face("bemused", 1)

                    ch_r "Well, maybe one kiss."

                    $ RogueX.change_face("kiss")

                    "She gives you a quick kiss. No tongue."

                    jump tour_parting
                else:
                    $ RogueX.change_face("bemused")

                    ch_r "Nah, I think you've had enough for today, [RogueX.player_petname]."

                    call remove_Girl(RogueX)

                    "You head back to your room."

                    $ RogueX.emotion = "normal"

    if simulation:
        return False

    $ RogueX.location = "bg_rogue"
    $ RogueX.history.append("met")

    $ active_Girls.append(RogueX)

    $ round = 10

    jump player_room

label Rogue_first_kiss:
    $ RogueX.blushing = "_blush2"

    call kiss_launch(RogueX)

    $ RogueX.action_counter["kiss"] += 1

    "She leans in for a kiss."
    "You lean in and your lips meet [RogueX.name]'s."

    $ RogueX.eyes = "surprised"
    call change_Girl_stat(RogueX, "love", 90, 15)
    call change_Girl_stat(RogueX, "love", 60, 30)

    "A slight spark passes between you and her eyes widen with surprise."

    call change_Girl_stat(RogueX, "lust", 70, 5)

    ch_r "Wow, [RogueX.player_petname], that was really something. . ."

    $ RogueX.change_face("bemused", 1)

    ch_r "Not the kind of zap I'm used to."

    $ RogueX.addiction -= 5
    call change_Girl_stat(RogueX, "obedience", 30, 20)
    call change_Girl_stat(RogueX, "inhibition", 30, 30)

    call show_full_body(RogueX)

    return










label Rogue_Key:
    call shift_focus (RogueX)
    call set_the_scene
    $ RogueX.change_face("bemused")
    $ RogueX.arm_pose = 2
    ch_r "Hey, you've been sleeping over a lot, I figured you might want a key?"
    ch_p "Thanks."
    $ RogueX.arm_pose = 1
    $ Player.Keys.append(RogueX)
    $ RogueX.event_happened[0] = 1
    return



label Rogue_BF:
    call shift_focus (RogueX)

    $ Player.add_word(1, "interruption")
    $ RogueX.drain_word("asked_to_meet")
    if RogueX.location != Player.location and RogueX not in Player.Party:
        "Suddenly, [RogueX.name] shows up and says she needs to talk to you."


    call set_the_scene

    call clear_the_room (RogueX)
    call set_Character_taboos
    $ RogueX.daily_history.append("relationship")
    $ RogueX.change_face("bemused", 1)
    ch_r "So, [RogueX.player_petname], we've been hanging out for a while now."
    ch_r ". . ."
    $ RogueX.eyes = "sexy"
    menu:
        ch_r "Right?"
        "Yeah, it's been great.":
            call change_Girl_stat(RogueX, "love", 200, 20)
        "Yeah, I guess":
            call change_Girl_stat(RogueX, "love", 200, 10)
        "Um, maybe?":
            call change_Girl_stat(RogueX, "love", 200, -10)
            call change_Girl_stat(RogueX, "obedience", 200, 30)
    if RogueX.SEXP >= 10:
        ch_r "I mean, we've done some stuff. . ."
    if RogueX.SEXP >= 15:
        ch_r "Like {i}sex{/i} stuff. . ."

    if len(Player.Harem) >= 2:
        ch_r "I know you've been going with those other girls for a while now, but we got talking and . . ."
    elif Player.Harem:
        ch_r "I know you've been going with [Player.Harem[0].name] for a while now, but we got talking and . . ."

    if not RogueX.event_happened[5]:
        ch_r "Right, so I was thinking. . ."
        ch_r "I haven't really been able to have a stable relationship, since I couldn't touch anyone."
        ch_r "This is all very new to me, but I'm feeling my way through it as best I can."
        ch_r "Let's make it official, you want to be my boyfriend?"
    elif Player.Harem:
        ch_r "I'd still like to be your girlfriend too."
    else:
        ch_r "You can be a real jerk sometimes, but still. . . I'm serious about this."
        ch_r "I think I want to be your girlfriend. . . officially"
    $ RogueX.event_happened[5] += 1
    menu:
        extend ""
        "I'd love to!":
            call change_Girl_stat(RogueX, "love", 200, 30)
            "Rogue leaps in and kisses you deeply."
            $ RogueX.change_face("kiss")
            $ RogueX.action_counter["kiss"] += 1
        "Um, ok.":
            $ RogueX.brows = "confused"
            "[RogueX.name] is a bit put off by your casual acceptence of reality, but takes it as a positive sign and hugs you."

        "I'm with someone now." if Player.Harem:
            $ RogueX.change_face("sad", 1)
            ch_r "I know, I know, I just thought maybe you could go out with me too?"
            menu:
                extend ""
                "Sure":
                    call change_Girl_stat(RogueX, "love", 200, 30)
                    "Rogue leaps in and kisses you deeply."
                    $ RogueX.change_face("kiss")
                    $ RogueX.action_counter["kiss"] += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                    $ line = "no."
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ line = "no."
                "I'm sorry, but. . . no." if RogueX.event_happened[5] != 20:
                    $ line = "no."
                "No way.":
                    jump Rogue_BF_Jerk
            if line == "no":
                call change_Girl_stat(RogueX, "love", 200, -10)
                ch_r "I get it. That's fine."
                $ RogueX.event_happened[5] = 20
                call remove_Girl(RogueX)
                $ line = 0
                return
        "Not really.":
            jump Rogue_BF_Jerk
    $ RogueX.player_petnames.append("boyfriend")
    if not simulation:
        $ Player.Harem.append(RogueX)
        if "RogueYes" in Player.traits:
            $ Player.traits.remove("RogueYes")
    $ RogueX.change_face("sexy")
    ch_r "Now, . . . boyfriend. . . how would you like to celebrate?"
    if simulation:
        return True
    $ approval_bonus = 10
    call enter_main_sex_menu(RogueX)
    $ approval_bonus = 0
    return

label Rogue_BF_Jerk:
    $ RogueX.change_face("angry", 1)
    ch_r "Well fine!"
    $ Count = (20* RogueX.event_happened[5])
    call change_Girl_stat(RogueX, "obedience", 50, 40)
    if RogueX.event_happened[5] != 20:
        call change_Girl_stat(RogueX, "obedience", 200, (20* RogueX.event_happened[5]))
    if 20 > RogueX.event_happened[5] >= 3:
        $ RogueX.change_face("sad")
        ch_r "Hrmph. I don't care what you want, we're dating. Deal with it."
        ch_r "Now I need some alone time though."
        if simulation:
            return True
        $ RogueX.player_petnames.append("boyfriend")
        $ achievements.append("I am not your Boyfriend!")
        $ Player.location = "bg_player"
        call remove_Girl(RogueX)
        call set_the_scene
        return
    if 1 <  RogueX.event_happened[5] < 20:
        ch_r "I don't know why I keep asking, I should know you haven't changed."
        call change_Girl_stat(RogueX, "love", 200, -(50* RogueX.event_happened[5]))
    else:
        call change_Girl_stat(RogueX, "love", 200, -50)

    if Player.location == RogueX.home:
        ch_r "Jerk! Out!"
    else:
        "[RogueX.name] storms off."
    if simulation:
        return True
    $ RogueX.location = "bg_rogue"
    $ Player.location = "bg_player"
    call remove_Girl(RogueX)
    call set_the_scene
    jump reset_location




label Rogue_Love:
    call shift_focus (RogueX)
    $ RogueX.drain_word("asked_to_meet")

    if Player.location != "bg_rogue":
        if RogueX.location == Player.location or RogueX in Player.Party:
            "Suddenly, [RogueX.name] says she wants to talk to you in her room and drags you over there."
        else:
            "[RogueX.name] shows up, hurriedly says she wants to talk to you in her room and drags you over there."
    else:
        "[RogueX.name] suddenly stares at you very intently."

    $ Player.add_word(1, "interruption")
    $ Player.location = "bg_rogue"

    call set_the_scene

    call clear_the_room (RogueX)
    call set_Character_taboos
    $ RogueX.daily_history.append("relationship")
    $ RogueX.change_face("bemused", 1)
    if RogueX in Player.Harem:
        ch_r "We've been dating for a while now, and I'm really feeling close to you."
    else:
        ch_r "We've been hanging out for a while now, and I'm really feeling close to you."
    ch_r ". . ."
    $ RogueX.eyes = "sexy"
    menu:
        ch_r "Right?"
        "I love you, [RogueX.name].":
            call change_Girl_stat(RogueX, "love", 200, 50)
            $ RogueX.event_happened[6] = 10
        "Yeah, it's been great.":
            call change_Girl_stat(RogueX, "love", 200, 20)
        "Yeah, I guess":
            call change_Girl_stat(RogueX, "love", 200, 10)
        "Um, maybe?":
            call change_Girl_stat(RogueX, "love", 200, -10)
            call change_Girl_stat(RogueX, "obedience", 200, 30)
    if not RogueX.event_happened[6]:
        ch_r "Right, so I was thinking. . ."
        ch_r "I love you."
    elif RogueX.event_happened[6] == 10:
        $ RogueX.change_face("confused")
        ch_r "So. . . wait, what?"
        $ RogueX.change_face("smile", 2)
        $ RogueX.brows = "surprised"
        ch_r "I love you too!"
        $ RogueX.change_face("kiss")
        "Rogue leaps into your arms and gives you a kiss."
        $ RogueX.change_face("sexy", 1)
        $ RogueX.action_counter["kiss"] += 1
    else:
        ch_r "Even though we've had our rough patches from time to time. . ."
        ch_r "I still love you."
    $ RogueX.event_happened[6] += 1
    if RogueX.event_happened[6] < 10:
        menu:
            extend ""
            "I love you too.":
                call change_Girl_stat(RogueX, "love", 200, 50)
                "[RogueX.name] collapses into your arms."
            "That's great!":
                $ RogueX.brows = "confused"
                "[RogueX.name] seems a bit perplexed, but takes it as a positive sign and hugs you."
            "I know.":
                $ RogueX.change_face("smile")
                $ RogueX.brows = "confused"
                "[RogueX.name] punches you in the arm and then gives you a huge hug."
            "So?":
                jump Rogue_Love_Jerk
            "Well I don't think of you like that.":
                call change_Girl_stat(RogueX, "love", 200, -50)
                call change_Girl_stat(RogueX, "obedience", 200, 50)
                jump Rogue_Love_Jerk
    $ RogueX.change_face("bemused", 1,eyes = "side")
    $ RogueX.player_petnames.append("lover")
    call Rogue_AnnaMarie
    ch_r "Anyway, I am glad I've been able to share this with you."
    $ RogueX.change_face("sly")
    ch_r "I'm hoping to share a lot more with you if I can. . ."
    if not RogueX.action_counter["sex"]:
        call change_Girl_stat(RogueX, "obedience", 70, 10)
        ch_r "So. . . did you want to . . . consumate this?"
        menu:
            extend ""
            "Yeah. . . [[have sex]":
                call change_Girl_stat(RogueX, "inhibition", 30, 30)
                ch_r "Hmm. . ."
                if simulation:
                    return True

                call start_action(RogueX, "sex")

                return
            "I have something else in mind. . .[[choose another activity]":
                $ RogueX.brows = "confused"
                call change_Girl_stat(RogueX, "obedience", 70, 20)
                ch_r "Well now you've got me curious. . ."
                pass
            "Ew. [[do nothing]":
                call change_Girl_stat(RogueX, "love", 200, -10)
                call change_Girl_stat(RogueX, "obedience", 70, 40)
                $ RogueX.change_face("perplexed", 1)
                ch_r "Um, ok?"
                ch_r "{size=-5}What the fuck was that?{/size}"
                return
    else:
        ch_r "Now, lover. . . was there anything else you felt like doing to celebrate?"
    if simulation:
        return True
    if "stockings_and_garterbelt" not in RogueX.inventory:
        $ RogueX.inventory.append("stockings_and_garterbelt")
    $ approval_bonus = 20
    call enter_main_sex_menu(RogueX)
    $ approval_bonus = 0

    $ Player.location = "bg_rogue"

    jump reset_location

label Rogue_Love_Jerk:
    if not simulation:
        $ renpy.pop_call()
    $ RogueX.change_face("angry", 1)
    ch_r "Well fine!"
    $ Count = (20* RogueX.event_happened[6])
    call change_Girl_stat(RogueX, "obedience", 50, 40)
    call change_Girl_stat(RogueX, "obedience", 200, Count)
    if RogueX.event_happened[6] == 3:
        $ RogueX.change_face("sad")
        ch_r "I. . . I don't care, I love you too much anyways."
        ch_r "I need some time to myself though."
        if simulation:
            return True
        $ RogueX.player_petnames.append("lover")
        $ achievements.append("One Sided Love")
        $ RogueX.location = "bg_rogue"
        $ Player.location = "bg_player"
        call remove_Girl(RogueX)
        jump player_room
    if RogueX.event_happened[6] > 1:
        ch_r "Fool me once, shame on you. . . I thought you'd grown."
    ch_r "If that's how you want to be, you can get the hell out of here!"
    $ Count = (100* RogueX.event_happened[6])
    call change_Girl_stat(RogueX, "love", 200, -Count)
    if simulation:
        return False
    $ RogueX.location = "bg_rogue"
    $ Player.location = "bg_player"
    call remove_Girl(RogueX)
    jump player_room

label Rogue_AnnaMarie:
    ch_r "I should probably tell you, I wasn't exactly born with the name \"Rogue.\""
    ch_r ". . ."
    $ RogueX.change_face("bemused", 1)
    ch_r "Grow'in up, I went by \"Anna-Marie.\""
    $ RogueX.names.append("Anna-Marie")
    $ RogueX.names.append("Anna")
    $ RogueX.names.append("Marie")
    menu:
        extend ""
        "That's a lovely name.":
            call change_Girl_stat(RogueX, "love", 200, 10)
            call change_Girl_stat(RogueX, "obedience", 50, 5)
            call change_Girl_stat(RogueX, "inhibition", 70, 5)
            $ RogueX.change_face("smile", 2)
            ch_r "Oh, thank you so much for say'in. . ."
        "Huh, ok.":
            call change_Girl_stat(RogueX, "obedience", 80, 5)
            $ RogueX.change_face("confused", 1)
            ch_r "Um. . . yeah."
        "Don't like it.":
            call change_Girl_stat(RogueX, "love", 200, -5)
            call change_Girl_stat(RogueX, "obedience", 200, 10)
            call change_Girl_stat(RogueX, "inhibition", 200, -5)
            $ RogueX.change_face("angry", 1)
            ch_r "Oh. . . Ok. . ."
    menu:
        extend ""
        "I think \"Rogue\" suits you though.":
            $ RogueX.name = "Rogue"
            $ RogueX.change_face("smile")
            ch_r "Yeah, I'm used to it by this point."
        "I liked the sound of \"Anna-Marie.\"":
            $ RogueX.name = "Anna-Marie"
            $ RogueX.change_face("smile")
            ch_r "It might be fun to go back like that again. . ."
        "\"Marie\" would be a cute name for you.":
            $ RogueX.name = "Marie"
            $ RogueX.change_face("smile")
            ch_r "You think? I suppose. . ."
        "\"Anna\" sounds nice.":
            $ RogueX.name = "Anna"
            $ RogueX.change_face("smile")
            ch_r "I suppose it does. . ."
    return




label Rogue_Sub:
    call shift_focus (RogueX)
    $ RogueX.drain_word("asked_to_meet")
    if RogueX.location != Player.location and RogueX not in Player.Party:
        "Suddenly, [RogueX.name] shows up and says she needs to talk to you."

    $ Player.add_word(1, "interruption")

    call set_the_scene

    call clear_the_room (RogueX)
    call set_Character_taboos
    $ RogueX.daily_history.append("relationship")
    $ RogueX.change_face("bemused", 1)
    ch_r ". . ."
    if RogueX in Player.Harem:
        ch_r "We've been dating for a bit now."
    else:
        ch_r "We've been hanging out for a while now."
    if RogueX.action_counter["fondle_breasts"]or RogueX.action_counter["fondle_pussy"] or RogueX.action_counter["fondle_ass"]:
        ch_r "I've let you touch me. . ."
    if RogueX.action_counter["handjob"] or RogueX.action_counter["blowjob"]:
        ch_r "I've touched you. . ."
    if RogueX.love >= 900 and (RogueX in Player.Harem):
        ch_r "I love you so much. . ."
    elif RogueX.love >= 800:
        ch_r "I really care about you."
    elif RogueX.love >= 500:
        ch_r "We don't exactly get along, but. . . we work, right?"
    else:
        $ RogueX.brows = "angry"
        ch_r "I really don't like you much, but something about you just. . ."
        ch_r "works for me."
    menu:
        extend ""
        "Yeah, it's been great.":
            call change_Girl_stat(RogueX, "love", 200, 20)
        "Yeah, I guess":
            call change_Girl_stat(RogueX, "love", 200, 10)
        "Um, maybe?":
            call change_Girl_stat(RogueX, "love", 200, -10)
            call change_Girl_stat(RogueX, "obedience", 200, 30)
    if not RogueX.event_happened[7]:
        ch_r "Right, so I was thinking. . ."
        $ RogueX.eyes = "sexy"
        ch_r "I'd like you to provide some . . .structure to my life."
    else:
        ch_r "I'd like you to reconsider the offer I made. . ."
        ch_r "the one about giving me some . . .structure."
    $ RogueX.event_happened[7] += 1
    menu:
        extend ""
        "Sounds interesting, yes.":
            call change_Girl_stat(RogueX, "obedience", 200, 100)
            $ RogueX.player_petnames.append("sir")
            "[RogueX.name] nods obediently."
        "What do you mean by that?":
            $ RogueX.change_face("bemused")
            ch_r "When you. . . encourage me to try new things, it really turns me on."
            ch_r "I'd like you to continue to. . . encourage me."
            menu:
                ch_r "I mean that I would like you to give me orders, and I will follow them as best I can."
                "Sounds interesting, ok.":
                    call change_Girl_stat(RogueX, "obedience", 200, 100)
                    "[RogueX.name] nods obediently."
                "Oh, ok, sure.":
                    "[RogueX.name] seems a bit put out, but takes it as a positive sign and nods."
                "Oh, no thanks. Take care of things yourself.":
                    jump Rogue_Sub_Jerk
            $ RogueX.player_petnames.append("sir")
        "Nah, you can handle things yourself.":
            jump Rogue_Sub_Jerk
    $ RogueX.change_face("sexy")
    ch_r "Now, sir. . . was there anything else you wished me to do to celebrate?"
    if simulation:
        return True
    if "stockings_and_garterbelt" not in RogueX.inventory:
        $ RogueX.inventory.append("stockings_and_garterbelt")
    $ approval_bonus = 10
    call enter_main_sex_menu(RogueX)
    $ approval_bonus = 0
    return

label Rogue_Sub_Jerk:
    $ RogueX.change_face("sad", 1)
    ch_r "Hrmph!"
    $ Count = (20* RogueX.event_happened[7])
    call change_Girl_stat(RogueX, "inhibition", 50, 30)
    call change_Girl_stat(RogueX, "inhibition", 200, Count)
    if not simulation:
        $ renpy.pop_call()
    if RogueX.event_happened[7] == 2:
        $ RogueX.change_face("sad")
        ch_r "I need some time to myself though."
        if simulation:
            return
        $ RogueX.player_petnames.append("sir")
        $ achievements.append("Nosiree")
        $ Player.location = "bg_player"
        $ RogueX.location = "bg_rogue"
        call remove_Girl(RogueX)
        jump player_room
    if RogueX.event_happened[7] > 1:
        ch_r "I thought you may have learned to respect my needs by now."
    ch_r "If that's how it is, I would appreciate some time alone."
    $ Count = (20* RogueX.event_happened[7])
    call change_Girl_stat(RogueX, "obedience", 200, -Count)
    if simulation:
        return
    $ RogueX.location = "bg_rogue"
    $ Player.location = "bg_player"
    call remove_Girl(RogueX)
    jump player_room





label Rogue_Master:
    call shift_focus (RogueX)
    $ RogueX.drain_word("asked_to_meet")
    if RogueX.location != Player.location and RogueX not in Player.Party:
        "Suddenly, [RogueX.name] shows up and says she needs to talk to you."

    $ Player.add_word(1, "interruption")

    call set_the_scene

    call clear_the_room (RogueX)
    call set_Character_taboos
    $ RogueX.daily_history.append("relationship")
    $ RogueX.change_face("bemused", 1)
    ch_r ". . ."

    if RogueX in Player.Harem:
        ch_r "This situation we have has really added some . . . spice to our relationship."
    else:
        ch_r "This situation we have has been very. . . interesting."
    if RogueX.action_counter["anal"] or RogueX.action_counter["dildo_ass"]:
        ch_r "We've even done some butt stuff."
    if RogueX.love >= 900 and (RogueX in Player.Harem):
        ch_r "I'm devoted to you. . ."
    elif RogueX.love >= 800:
        ch_r "I really care about you."
    elif RogueX.love >= 500:
        ch_r "I can't be without you."
    else:
        $ RogueX.brows = "angry"
        ch_r "I can't stand being with you, but can't stand being without you either."
    menu:
        ch_r "Have I been pleasing you, [RogueX.player_petname]?"
        "Certainly.":
            call change_Girl_stat(RogueX, "love", 200, 20)
            call change_Girl_stat(RogueX, "obedience", 200, 20)
        "Yeah, I guess.":
            call change_Girl_stat(RogueX, "love", 200, 10)
            call change_Girl_stat(RogueX, "obedience", 200, 20)
        "Not especially.":
            call change_Girl_stat(RogueX, "love", 200, -10)
            call change_Girl_stat(RogueX, "obedience", 200, 30)
    if not RogueX.event_happened[8]:
        ch_r "Yes, well, given that. . ."
        ch_r "I think that I would like you to be my master, formally."
    else:
        ch_r "I'd like you to reconsider the offer I made. . ."
        ch_r "please be my master."
    $ RogueX.event_happened[8] += 1
    menu:
        extend ""
        "Very well.":
            call change_Girl_stat(RogueX, "obedience", 200, 100)
            $ RogueX.player_petnames.append("master")
            "[RogueX.name] bows obediently."
        "What do you mean by that?":
            $ RogueX.brows = "confused"
            ch_r "Well, when you tell me what to do. . ."
            $ RogueX.change_face("bemused", 1)
            ch_r "I get really horny."
            ch_r "I just really need for you to tell me what to do."
            menu:
                ch_r "I mean that I would follow your orders to the letter, so long as I am able."
                "Oh, ok, sure.":
                    "[RogueX.name] seems a bit put out, but takes it as a positive sign and nods."
                    $ RogueX.player_petnames.append("master")
                "You should do your own thing, you don't need me telling you what to do.":
                    $ RogueX.brows = "confused"
                    ch_r "Ok, if that's what you want. . ."
                    call change_Girl_stat(RogueX, "inhibition", 50, 100)
                    call change_Girl_stat(RogueX, "inhibition", 90, 50)
                    ch_r "For now at least. . ."
                    call change_Girl_stat(RogueX, "obedience", 200, -200)
                    $ RogueX.event_happened[8] = 3
                "Oh, no, sounds like too much work.":
                    jump Rogue_Obed_Jerk
        "Nah, take care of yourself.":
            jump Rogue_Obed_Jerk
    $ RogueX.change_face("sexy")
    ch_r "Now, master. . . was there anything else you wished me to do to celebrate?"
    if simulation:
        return True
    $ approval_bonus = 20
    call enter_main_sex_menu(RogueX)
    $ approval_bonus = 0
    return

label Rogue_Obed_Jerk:
    $ RogueX.change_face("sad", 1)
    ch_r "Well fine!"
    $ Count = (20* RogueX.event_happened[8])
    call change_Girl_stat(RogueX, "inhibition", 50, 30)
    call change_Girl_stat(RogueX, "inhibition", 200, Count)
    if not simulation:
        $ renpy.pop_call()
    if RogueX.event_happened[8] == 2:
        $ RogueX.change_face("sad")
        ch_r "I don't care what you say, this is something I need. MASTER."
        ch_r "I need some time to myself though."
        if simulation:
            return
        $ RogueX.player_petnames.append("master")
        $ achievements.append("Heavy is the Head")
        $ Player.location = "bg_player"
        $ RogueX.location = "bg_rogue"
        call remove_Girl(RogueX)
        jump player_room
    if RogueX.event_happened[8] > 1:
        ch_r "I thought you may have learned to respect my needs by now."
    ch_r "If that's how it is, I would appreciate some time alone."
    $ Count = (50* RogueX.event_happened[8])
    call change_Girl_stat(RogueX, "obedience", 200, -Count)
    if simulation:
        return
    $ RogueX.location = "bg_rogue"
    $ Player.location = "bg_player"
    call remove_Girl(RogueX)
    jump player_room





label Rogue_Sexfriend:
    call shift_focus (RogueX)
    $ RogueX.daily_history.append("relationship")
    if RogueX in Player.Harem:
        if RogueX.location != Player.location and RogueX not in Player.Party:
            return
        $ RogueX.drain_word("asked_to_meet")
        if "stockings_and_garterbelt" not in RogueX.inventory:
            $ RogueX.inventory.append("stockings_and_garterbelt")
        $ RogueX.player_petnames.append("sex friend")
        call change_Girl_stat(RogueX, "inhibition", 200, 50)
        "[RogueX.name] suddenly gives your butt a little squeeze."
        return

    $ RogueX.drain_word("asked_to_meet")
    if RogueX.location != Player.location and RogueX not in Player.Party:
        "Suddenly, [RogueX.name] shows up and says she needs to talk to you."

    if "stockings_and_garterbelt" not in RogueX.inventory:
        $ RogueX.inventory.append("stockings_and_garterbelt")
    $ RogueX.player_petnames.append("sex friend")

    call set_the_scene

    call clear_the_room (RogueX)
    call set_Character_taboos
    $ RogueX.change_face("smile", 1)
    ch_r ". . ."
    ch_r "We've been having fun, right?"
    if RogueX.SEXP >= 40:
        ch_r "I mean, we've been getting up to some pretty wild stuff."
    if "ex" in RogueX.traits:
        ch_r "And we were actually dating for a while. . ."
    else:
        ch_r "And I know we're not \"dating\" dating, but you know. . ."
    menu:
        ch_r "Haven't I been fun to have around?"
        "Yeah, you've been great.":
            call change_Girl_stat(RogueX, "love", 200, 20)
            call change_Girl_stat(RogueX, "inhibition", 200, 20)
        "Hmmm. . . yes?":
            call change_Girl_stat(RogueX, "inhibition", 200, 20)
        "Maybe. . .":
            call change_Girl_stat(RogueX, "love", 200, -10)
            call change_Girl_stat(RogueX, "obedience", 200, 30)
    if RogueX in Player.Harem:
        ch_r "I'd like to have a -lot- more sex. . ."
    if not RogueX.event_happened[9]:
        ch_r "Ok, so since we've been having so much fun. . ."
        if "ex" in RogueX.traits:
            ch_r "I think that even though we aren't dating, I still want to be sex friends."
        else:
            ch_r "I think I'm ready to accept just being casual sex friends."
    else:
        ch_r "I'd like you to reconsider my generous offer. . ."
        ch_r "come on, sex friend? Eh?"
    $ RogueX.event_happened[9] += 1
    if RogueX not in Player.Harem:
        menu:
            extend ""
            "Sounds fun!":
                call change_Girl_stat(RogueX, "inhibition", 200, 100)
                $ RogueX.player_petnames.append("sex friend")
                "[RogueX.name] nods obediently."
            "What do you mean by that?":
                $ RogueX.brows = "confused"
                ch_r "You know, casual sex, no real strings, for now at least."
                menu:
                    ch_r "Well?"
                    "Oh, ok, sure.":
                        "[RogueX.name] is a bit put off, but grabs you in a big hug anyway."
                    "Oh, no thanks. Not interested.":
                        jump Rogue_Sexfriend_Jerk
            "Nah, you're on your own.":
                jump Rogue_Sexfriend_Jerk
        $ RogueX.change_face("sexy")
        ch_r "Now, sex friend. . . how would you like to celebrate?"
        if simulation:
            return True
    $ Player.add_word(1, "interruption")
    $ approval_bonus = 25
    call enter_main_sex_menu(RogueX)
    $ approval_bonus = 0
    return

label Rogue_Sexfriend_Jerk:
    $ RogueX.change_face("sad", 1)
    $ RogueX.daily_history.append("relationship")
    ch_r "Your loss."
    call change_Girl_stat(RogueX, "obedience", 50, 30)
    if not simulation:
        $ renpy.pop_call()
    if RogueX.event_happened[9] == 3:
        ch_r "Well, it's not really up to you anyways."
        ch_r "Just let me know if you want a roll in the hay."
        ch_r "I need some alone time though."
        if simulation:
            return
        $ RogueX.player_petnames.append("sex friend")
        $ achievements.append("Man of Virtue")
        $ Player.location = "bg_player"
        $ RogueX.location = "bg_rogue"
        call remove_Girl(RogueX)
        jump player_room
    $ Count = (10*RogueX.event_happened[9])
    call change_Girl_stat(RogueX, "inhibition", 200, -Count)
    if Player.location == "bg_rogue":
        ch_r "Ok, you can go now."
        $ Player.location = "bg_player"
    else:
        ch_r "Ok, I'm out."
        $ RogueX.location = "bg_rogue"
    if simulation:
        return
    call remove_Girl(RogueX)
    jump player_room





label Rogue_Fuckbuddy:
    call shift_focus (RogueX)
    $ RogueX.drain_word("asked_to_meet")
    if RogueX in Player.Harem:
        if RogueX.location != Player.location and RogueX not in Player.Party:
            return
        $ RogueX.player_petnames.append("fuck buddy")
        call change_Girl_stat(RogueX, "inhibition", 200, 50)
        "[RogueX.name] suddenly reaches down and gives your package a little squeeze."
        return

    if RogueX.location != Player.location and RogueX not in Player.Party:
        "Suddenly, [RogueX.name] shows up and says she needs to talk to you."


    call set_the_scene

    call clear_the_room (RogueX)
    call set_Character_taboos
    $ RogueX.change_face("bemused", 1)
    ch_r ". . ."
    ch_r "I've been having a lot of fun with this \"sex friend\" thing."
    if "exhibitionist" in RogueX.traits:
        ch_r "And I've really been getting off on all the stuff we've been doing."
    menu:
        extend ""
        "You bet!":
            call change_Girl_stat(RogueX, "love", 200, 20)
            call change_Girl_stat(RogueX, "obedience", 200, 20)
            call change_Girl_stat(RogueX, "inhibition", 200, 30)
        "Yeah?":
            call change_Girl_stat(RogueX, "love", 200, 10)
            call change_Girl_stat(RogueX, "obedience", 200, 20)
        "Whatever.":
            call change_Girl_stat(RogueX, "love", 200, -10)
            call change_Girl_stat(RogueX, "obedience", 200, 30)
    ch_r "So, since it's worked so far. . ."
    $ RogueX.event_happened[10] += 1
    $ RogueX.player_petnames.append("fuck buddy")
    if RogueX not in Player.Harem:
        ch_r "I'd like to be full on casual fuck buddies."
        menu:
            extend ""
            "Heh, ok, fuck buddy.":
                call change_Girl_stat(RogueX, "inhibition", 200, 100)
                $ RogueX.player_petnames.append("fuck buddy")
                $ RogueX.arm_pose = 2
                ch_r "Whoo hoo!"
                $ RogueX.Clothes["top"] = 0
                $ RogueX.Clothes["bra"] = 0
                if simulation:
                    return True
                call Rogue_First_Topless (1)
                call breasts_launch(RogueX)
                "Rogue, throws her top off, grabs you and shoves your head into her cleavage."
                call show_full_body(RogueX)
            "What do you mean by that?":
                $ RogueX.brows = "confused"
                menu:
                    ch_r "I mean, you know, we'd fuck. And be buddies. Both of those."
                    "Oh, ok, sure.":
                        call kiss_launch(RogueX)
                        "Rogue laughs and tackles you into a hug."
                        call show_full_body(RogueX)
                    "Oh, no, not my style.":
                        jump Rogue_Fuckbuddy_Jerk
            "No thanks.":
                jump Rogue_Fuckbuddy_Jerk
        $ RogueX.change_face("sexy")
        ch_r "Now, -heh-, fuck buddy. . . let's make this official!"
    if simulation:
        return True
    $ approval_bonus = 30
    $ Player.add_word(1, "interruption")
    call enter_main_sex_menu(RogueX)
    $ approval_bonus = 0
    return

label Rogue_Fuckbuddy_Jerk:
    call change_Girl_stat(RogueX, "obedience", 50, 30)
    $ RogueX.change_face("bemused", 1)
    if RogueX.event_happened[10] > 1:
        $ RogueX.arm_pose = 2
        $ RogueX.Clothes["top"] = 0
        $ RogueX.Clothes["bra"] = 0
        ch_r "I offer these things on a silver platter, and nothing!"
        $ RogueX.change_Outfit()
        ch_r "Look, I don't care what you call it. Just let me know if you want a tumble."
        if simulation:
            return True
        call Rogue_First_Topless (1)
        $ RogueX.player_petnames.append("fuck buddy")
        $ achievements.append("Stalwart as the mount")
        return
    else:
        ch_r "Too bad."
    if simulation:
        return
    $ renpy.pop_call()
    $ Count = (10*RogueX.event_happened[10])
    call change_Girl_stat(RogueX, "inhibition", 200, -Count)
    if Player.location == "bg_rogue":
        ch_r "Ok, you can go now."
        $ Player.location = "bg_player"
    else:
        ch_r "Ok, I'm out."
        $ RogueX.location = "bg_rogue"
    call remove_Girl(RogueX)
    jump player_room



label Rogue_Daddy:
    $ RogueX.daily_history.append("relationship")
    $ RogueX.drain_word("asked_to_meet")
    call shift_focus (RogueX)
    call set_the_scene
    ch_r ". . ."
    if RogueX in Player.Harem:
        ch_r "You know, even though we've been dating, "
    else:
        ch_r "Even though we've been hanging out, "
    if RogueX.love > RogueX.obedience and RogueX.love > RogueX.inhibition:
        ch_r "and you're really sweet to me. . ."
    elif RogueX.obedience > RogueX.inhibition:
        ch_r "and you know what I need. . ."
    else:
        ch_r "and I've really been spreading my wings. . ."
    ch_r "So I was thinking, could I call you \"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ RogueX.change_face("smile")
            call change_Girl_stat(RogueX, "love", 90, 20)
            call change_Girl_stat(RogueX, "obedience", 60, 10)
            call change_Girl_stat(RogueX, "inhibition", 80, 30)
            ch_r "Squee!"
            $ RogueX.player_petname = "daddy"
        "What do you mean by that?":
            $ RogueX.change_face("bemused")
            ch_r "I just sort of get turned on by it, you know, being your baby girl. . ."
            ch_r "I'd like to call you that."
            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ RogueX.change_face("smile")
                    call change_Girl_stat(RogueX, "love", 90, 15)
                    call change_Girl_stat(RogueX, "obedience", 60, 20)
                    call change_Girl_stat(RogueX, "inhibition", 80, 25)
                    ch_r "Great! . . daddy."
                    $ RogueX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(RogueX, "love", 90, 5)
                    call change_Girl_stat(RogueX, "obedience", 80, 40)
                    call change_Girl_stat(RogueX, "inhibition", 80, 20)
                    $ RogueX.change_face("sad")
                    ch_r " . . . "
                    ch_r "Well, ok."
                "No, that creeps me out.":
                    call change_Girl_stat(RogueX, "love", 90, -10)
                    call change_Girl_stat(RogueX, "obedience", 80, 45)
                    call change_Girl_stat(RogueX, "inhibition", 70, 5)
                    $ RogueX.change_face("angry")
                    ch_r "Hrmph."
        "No, that creeps me out.":
            call change_Girl_stat(RogueX, "love", 90, -5)
            call change_Girl_stat(RogueX, "obedience", 80, 40)
            call change_Girl_stat(RogueX, "inhibition", 70, 10)
            $ RogueX.change_face("angry")
            ch_r "Hrmph."
    $ RogueX.player_petnames.append("daddy")
    return




label Rogue_Frisky_Class:
    $ line = 0
    if EmmaX.teaching:
        "[EmmaX.name] is giving a lecture on mutant relations. In her seat next to you, you notice [RogueX.name] shifting uncomfortably in her seat."
    elif StormX.teaching:
        "[StormX.name] is giving a lecture on geography and politics. In her seat next to you, you notice [RogueX.name] shifting uncomfortably in her seat."
    else:
        "Professor McCoy is giving a lecture on the X-Gene. In her seat next to you, you notice [RogueX.name] shifting uncomfortably in her seat."
    "Occasionally, you catch her glancing over your way."
    if not approval_check(RogueX, 600):
        jump Rogue_Frisky_Class_End

    "[RogueX.name] opens her notebook and begins scratching out a note. She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
    "She watches you as you unfold the note. In looping penstrokes, it reads: {i}You like biology?{/i}"
    "You look back and see that she's blushing slightly. She slides her pen over to you so you can reply."
    menu:
        "You reply. . ."
        "What are you talking about?":
            pass
        "Naah. Not so much.":

            call change_Girl_stat(RogueX, "love", 80, -3)
            call change_Girl_stat(RogueX, "inhibition", 60, -3)
            $ RogueX.change_face("confused")
        "It's my favorite subject.":

            call change_Girl_stat(RogueX, "love", 80, 5)
            $ RogueX.change_face("smile")
            "[RogueX.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. {i}\"Then maybe we could study together tonight?\"{/i}."
            $ line = "continue"
        "I do when it's about you.":

            if approval_check(RogueX, 500, "I") or RogueX.SEXP >= 30:
                $ RogueX.change_face("sly")
                "[RogueX.name] reads your note and smiles at you suggestively."
                $ line = "flirt"
            elif approval_check(RogueX, 900):
                $ RogueX.change_face("confused", 2)
                "[RogueX.name] reads your note and blushes furiously, looking down at her notes."
                $ RogueX.blushing = "_blush1"
                $ line = "flirt"
            else:
                $ RogueX.change_face("perplexed", 2)
                "[RogueX.name] reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. {i}\"I meant the class! Maybe we could study tonight?\"{/i}."
                $ RogueX.blushing = "_blush1"
                $ line = "continue"


    if line == "continue":
        "[RogueX.name]'s drawn a little heart as the period at the bottom of the question mark."
        "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."
        menu:
            "You respond. . ."
            "Maybe later.":
                call change_Girl_stat(RogueX, "love", 80, -3)
                call change_Girl_stat(RogueX, "obedience", 70, 5)
                call change_Girl_stat(RogueX, "inhibition", 60, -3)
                $ RogueX.change_face("confused")
                $ line = 0
            "Naah. I've got better things to do.":
                call change_Girl_stat(RogueX, "love", 200, -15)
                call change_Girl_stat(RogueX, "obedience", 70, 5)
                call change_Girl_stat(RogueX, "inhibition", 60, -3)
                $ line = 0
                $ RogueX.change_face("angry")
                $ RogueX.daily_history.append("angry")
            "Count on it.":
                "She smiles when she reads your reply, and throws you a wink."
                $ RogueX.daily_history.append("studydate")
                $ RogueX.change_face("smile")
                jump Rogue_Frisky_Class_End
            "We could get some \"studying\" done right now.":
                if approval_check(RogueX, 1200):
                    $ RogueX.change_face("sly", 1)
                    call change_Girl_stat(RogueX, "love", 80, 3)
                    call change_Girl_stat(RogueX, "inhibition", 60, 3)
                    "[RogueX.name] gets a mischevious grin on her face and leans towards you."
                    $ line = "flirt"
                elif approval_check(RogueX, 700):
                    $ RogueX.change_face("smile", 1)
                    call change_Girl_stat(RogueX, "inhibition", 60, 2)
                    "[RogueX.name] blushes and smiles your way."
                    $ line = "flirt"
                else:
                    $ RogueX.change_face("confused", 1)
                    "[RogueX.name] looks a bit surprised, then scowls at you."
                    jump Rogue_Frisky_Class_End



    if line == "flirt":
        $ Player.add_word(1, "interruption")
        $ D20 = renpy.random.randint(1, 20)
        $ RogueX.change_face("sly")
        "You notice one of [RogueX.name]'s shoes slip from her foot beneath the desk. She tosses you a sly grin."
        if RogueX.Clothes["hose"]:
            "You feel the smooth texture of her stockinged foot begin to slowly slide back and forth along the length of your calf."
        else:
            "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."

        while D20 <= 21:
            menu:
                extend ""
                "Pull away from her.":
                    if line == "fondle_pussy":
                        "You slowly slide your hand from her lap and start taking notes again."
                        $ line = "tease"
                    elif line == "fondle_breast":
                        "With a final squeeze, you move your hand back to the desktop."
                        $ line = "tease"
                    else:
                        $ line = "rejected"
                        call change_Girl_stat(RogueX, "love", 200, -15)
                        call change_Girl_stat(RogueX, "obedience", 70, 2)
                        call change_Girl_stat(RogueX, "inhibition", 60, -2)
                    jump Rogue_Frisky_Class_End

                "Look into her eyes and smile slightly." if line == "flirt":
                    $ RogueX.change_face("smile")
                    call change_Girl_stat(RogueX, "love", 200, 5)
                    "[RogueX.name] smiles back."
                    "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."
                    $ line = "handholding"
                "Grasp her hand gently, stroking the top of it." if line == "handholding":
                    call change_Girl_stat(RogueX, "love", 200, 5)
                    $ RogueX.change_face("smile")
                    "[RogueX.name] sighs contentedly and holds your hand for the remainder of class."
                    jump Rogue_Frisky_Class_End

                "Try and slip your hand to her lap." if line != "fondle_pussy":
                    $ line = "fondle_pussy"
                    if approval_check(RogueX, 1500) and RogueX.action_counter["fondle_pussy"] and RogueX.SEXP >= 40:
                        $ RogueX.change_face("sly")
                        call change_Girl_stat(RogueX, "love", 90, 5)
                        call change_Girl_stat(RogueX, "obedience", 70, 5)
                        call change_Girl_stat(RogueX, "inhibition", 60, 5)
                        "[RogueX.name] gets a mischievous grin and places her hand on your arm."
                    elif approval_check(RogueX, 1800) and RogueX.action_counter["fondle_pussy"]:
                        $ RogueX.change_face("smile")
                        call change_Girl_stat(RogueX, "love", 80, 3)
                        call change_Girl_stat(RogueX, "obedience", 70, 7)
                        call change_Girl_stat(RogueX, "inhibition", 60, 3)
                        "[RogueX.name] starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                    elif approval_check(RogueX, 2000):
                        $ RogueX.change_face("perplexed", 2)
                        call change_Girl_stat(RogueX, "obedience", 70, 10)
                        call change_Girl_stat(RogueX, "inhibition", 60, 3)
                        "[RogueX.name] glances at you in alarm, but then slowly calms down."
                        $ RogueX.change_face("smile", 1)
                        $ D20 += 2
                    else:
                        $ line = "too far"

                    if line == "fondle_pussy":
                        $ RogueX.change_face("sly")
                        if RogueX.Clothes["bottom"] == "skirt":
                            "[RogueX.name]'s sly smile turns sultry as she feels your fingers sneak under the hem of her skirt, slowly tracing the soft contours of her mound."
                        elif RogueX.Clothes["bottom"] == "pants":
                            "[RogueX.name]'s sly smile turns sultry as she feels your fingers sneak down her pants, slowly tracing the soft contours of her mound."
                        else:
                            "[RogueX.name]'s sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound."

                        if RogueX.Clothes["underwear"] == "shorts":
                            "You think her shorts are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif RogueX.Clothes["underwear"]:
                            "You think her panties are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif RogueX.pubes:
                            "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        else:
                            "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        $ D20 += 5

                "Keep fondling her pussy." if line == "fondle_pussy":
                    call change_Girl_stat(RogueX, "obedience", 70, 5)
                    call change_Girl_stat(RogueX, "inhibition", 60, 3)
                    "As the class drones on, you continue to slowly massage her warm delta."
                    $ D20 += 5

                "Start fondling her tits." if line != "fondle_breasts":
                    $ line = "fondle_breasts"
                    if approval_check(RogueX, 1500) and RogueX.action_counter["fondle_breasts"]and RogueX.SEXP >= 40:
                        call change_Girl_stat(RogueX, "love", 80, 5)
                        call change_Girl_stat(RogueX, "obedience", 70, 5)
                        call change_Girl_stat(RogueX, "inhibition", 60, 3)
                        $ RogueX.change_face("sly")
                        "[RogueX.name] closes her eyes and caresses your arm."
                    elif approval_check(RogueX, 1800) and RogueX.action_counter["fondle_breasts"]:
                        call change_Girl_stat(RogueX, "love", 80, 3)
                        call change_Girl_stat(RogueX, "obedience", 70, 7)
                        call change_Girl_stat(RogueX, "inhibition", 60, 3)
                        $ RogueX.change_face("smile", 1)
                        "[RogueX.name] flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                    elif approval_check(RogueX, 2000):
                        call change_Girl_stat(RogueX, "obedience", 70, 10)
                        call change_Girl_stat(RogueX, "inhibition", 60, 3)
                        $ RogueX.change_face("perplexed", 2)
                        "[RogueX.name] glances at you in alarm, but then slowly calms down."
                        $ RogueX.change_face("smile", 2)
                        $ D20 += 5
                    else:
                        $ line = "too far"

                    if line == "fondle_breasts":
                        $ RogueX.change_face("sly")
                        "[RogueX.name]'s sly eyes spakle as your hand cups her breast, giving it a casual caress."
                        "her nipples begin to firm up and she lets out a small moan of pleasure."
                        $ D20 += 7
                "Keep fondling her tits." if line == "fondle_breasts":
                    call change_Girl_stat(RogueX, "obedience", 70, 5)
                    call change_Girl_stat(RogueX, "inhibition", 60, 2)
                    "Barely paying attention to the lecture, you continue to pulse her breast in your palm."
                    $ D20 += 7

            if line == "too far":
                $ RogueX.change_face("surprised", 2)
                call change_Girl_stat(RogueX, "love", 80, -5)
                call change_Girl_stat(RogueX, "obedience", 70, 7)
                call change_Girl_stat(RogueX, "inhibition", 50, -3)
                "[RogueX.name] sits up straight in her seat and makes a little yelping noise."
                $ RogueX.change_face("angry", 1)
                "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."
                $ D20 += 10


        if line not in ("rejected", "handholding", "tease"):
            call change_Girl_stat(RogueX, "love", 80, -10)
            call change_Girl_stat(RogueX, "obedience", 70, -5)
            call change_Girl_stat(RogueX, "inhibition", 50, -10)
            $ RogueX.change_face("surprised")
            if EmmaX.teaching:
                "[EmmaX.name] stops her lecture in mid-sentence when she notices that the whole class is looking at you and [RogueX.name]."
                ch_e "[EmmaX.player_petname], [RogueX.name], if you could perhaps pay more attention to the lecture, and less to each other's bodies?"
                ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
            elif StormX.teaching:
                "[StormX.name] stops her lecture in mid-sentence when she notices that the whole class is looking at you and [RogueX.name]."
                ch_s "[StormX.player_petname], [RogueX.name], I can appreciate your enthusaism, but perhaps not on my time?"
                ch_s "I think perhaps you should visit Charles and cool off?"
            else:
                "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and [RogueX.name]."
                ch_b "Oh, my stars and garters!"
                ch_b "[Player.name]!?! {b}WHAT ARE YOU DOING? BOTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"
            if RogueX not in Rules:
                call caught_having_sex(RogueX)
            else:
                "Since Xavier isn't concerned with your activities, you both head back to your room instead."

                $ Player.location = "bg_player"

                call clear_the_room (RogueX, 0, 1)

                jump player_room



label Rogue_Frisky_Class_End:
    if not line:
        $ RogueX.change_face("confused")
        "She unfolds the note and quickly reads it over."
        $ RogueX.change_face("sad")
        "As she does, you immediately see disappointment come over her features."
        "She scratches out a reply and slides it back in front of you."
        "When you open it up, it reads: {i}Never mind.{/i}"
    elif line == "tease":
        $ RogueX.change_face("sly", 1)
        "[RogueX.name] takes in a deep breath and exhales it in a sigh, leaning in to whisper."
        ch_r "Tonight's \"study session\" just got a whole lot more interesting."
    elif line == "rejected":
        $ RogueX.change_face("sadside")
        "[RogueX.name] looks surprised and hurt. For the rest of the class, she says nothing."
        "It seems like she has a hard time looking you in the eye."

    "Eventually, [RogueX.name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
