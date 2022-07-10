label meet_Mystique:
    call set_the_scene(location = "bg_entrance", fade = True)

    "You reluctantly make your way to the school psychologist's office."
    "It's in a part of campus you haven't explored, and you get turned around more than once."
    "You finally find the right door.{p}Dr. Darkholme, PsyD{p}Sounds foreboding."
    "You knock."

    $ MystiqueX.name = "???"
    $ MystiqueX.location = "bg_office"
    $ MystiqueX.disguise = "Raven"

    ch_m "Come in."

    call set_the_scene(location = "bg_office", fade = True)

    ch_m "Hello, [Player.name] I presume?"

    $ note_lines = ["She reaches over to a pen and pad of paper and quickly jots something down.",
        "She writes something else down.",
        "She scribbles a note and underlines it.",
        "She underlines something on the page several times."]

    $ note_count = 0
    $ line = note_lines[note_count]

    menu:
        extend ""
        "That's me.":
            ch_m "Pleasure to meet you. Have a seat right there."
        "Yeah, listen, this seems like a total waste of time":
            $ MystiqueX.change_face("bemused")

            ch_m "Hmm, your report mentioned a complete disregard for social etiquette and authority."

            $ MystiqueX.change_face("normal")

            ch_m "Have a seat."
        ". . .":
            menu:
                ch_m "Yes?"
                "Sorry, I just wasn't expecting. . .":
                    $ MystiqueX.change_face("bemused", eyes = "side")

                    ch_m "Right. Please have a seat."
                "I get it, sexy therapist right?":
                    $ MystiqueX.change_face("bemused")

                    ch_m "Yes, your report mentioned a complete disregard for social etiquette and authority."

                    $ MystiqueX.change_face("normal")

                    ch_m "Please refrain from comments about my appearance. Have a seat."
                ". . .":
                    $ MystiqueX.change_face("bemused", eyes = "side")

                    "[line]"

                    $ note_count += 1
                    $ line = note_lines[note_count]

                    ch_m "Right. Please have a seat."

    ch_m "As I expect you realize, I am Dr. Darkholme."

    $ MystiqueX.name = "Dr. Darkholme"
    $ MystiqueX.names = ["Dr. Darkholme"]

    if day == 1:
        ch_m "As I also hope you realize, it is highly unusual and concerning for a new student to find themselves in my office after only [day] day here."
    else:
        ch_m "As I also hope you realize, it is highly unusual and concerning for a new student to find themselves in my office after only [day] days here."

    menu:
        ch_m "However, given your recent behavior, Charles has asked me to intervene."
        "I understand, I regret my actions.":
            ch_m "Mhm. What specifically do you regret?"
        "Sorry, I actually didn't hear a word you just said. What was that?":
            "[line]"

            $ note_count += 1
            $ line = note_lines[note_count]

            ch_m "I'm glad you are amused, [Player.name]. Let us hope you see the humor in my report to Charles."
            ch_m "Perhaps we should start with why you think you are here."
        ". . .":
            "[line]"

            $ note_count += 1
            $ line = note_lines[note_count]

            $ MystiqueX.change_face("bemused", eyes = "side")

            ch_m "This can be as easy or as difficult as you make it, [Player.name]."

            $ MystiqueX.change_face("normal")

            ch_m "Perhaps we should start with why you think you are here."

    menu:
        extend ""
        "I guess I just thought it would be fun to mess around a bit.":
            ch_m "I see."

            show black_screen onlayer black

            ch_m "And what exactly did you find so fun about. . .?"
        "Okay, okay. The truth is. . . I love pussy. Always have. The only thing I love as much as pussy is ass. Assholes, specifically. As long as I can remember, I've spent every waking minute thinking about eating ass, sucking on titties, going balls deep on every woman I see. And I do mean. Every. Woman.":
            ch_m "Your attempts to hide behind shock and offense reveals more about you than you know."

            show black_screen onlayer black

            ch_m "So please, do continue. . ."
        ". . .":
            "[line]"

            $ note_count += 1
            $ line = note_lines[note_count]

            if note_count > 2:
                $ MystiqueX.change_face("normal", brows = "confused")

                "You notice the faintest hint of contempt flash over her otherwise stony face."

            ch_m "I suppose you intend for me to decide for myself whether your behavior is defiance or a simple lack of capacity."

            show black_screen onlayer black

            ch_m "Very well, then. . ."

    $ round = 10

    jump meet_Mystique_end

label meet_Mystique_end:
    "An hour later. . ."

    hide black_screen onlayer black

    ch_m "Well, that was. . . enlightening."
    ch_m "I will be recommending to Charles that we meet on a regular basis. With any luck, we may just get to what's driving your behavior."
    ch_m "That will conclude this session, please close the door on your way out."

    call hide_all
    call set_the_scene(location = "bg_door")

    "You pull the door closed, but pause outside the office to check your phone."
    "After a few moments, you imagine you hear the sound of fabric shifting and falling to the floor."
    "Probably just wishful thinking from staring at Dr. Darkholme's thighs."

    $ active_Girls.append(MystiqueX)

    $ MystiqueX.History.update("met")

    jump campus
