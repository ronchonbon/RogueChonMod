label study_Explore:
    $ line = 0
    $ D20 = renpy.random.randint(1, 20)
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + counter:
                $ line = "book"
            else:
                "As you search the bookshelf, you accidentally knock one of the books off."
                "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if KittyX.location != Player.location and StormX.location != Player.location:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + counter:
                $ line = "left"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if KittyX.location != Player.location and StormX.location != Player.location:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + counter:
                $ line = "middle"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if KittyX.location != Player.location and StormX.location != Player.location:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + counter:
                $ line = "right"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]":
            jump study_room

    $ D20 = renpy.random.randint(1, 20)
    if not line:
        "Probably best to get out of here."
        "You slip out and head back to your room."

        $ Player.location = "bg_room"

        jump reset_location
    elif line == "book":
        if D20 >= 15 and "Well Studied" not in achievements:
            "As you check the books on the shelf, you notice that one of them is actually a disguised lockbox."
            if KittyX.location == Player.location:
                menu:
                    "Since [KittyX.name] is around, have her check inside?"
                    "Check in the box":
                        if approval_check(KittyX, 700, "I") or approval_check(KittyX, 1800):
                            if "Well Studied" not in achievements:
                                call change_Girl_stat(KittyX, "obedience", 10)
                                call change_Girl_stat(KittyX, "inhibition", 15)
                                ch_k "Sounds like a plan."
                                "[KittyX.name] swipes her hand through the box, and pulls out a stack of bills."
                                "Looks like Xavier was hiding a rainy day fund in here."
                                $ Player.cash += 500
                                "[[$500 acquired.]"
                                $ achievements.append("Well Studied")
                            else:
                                "Looks like this has been thoroughly looted."
                        else:
                            call change_Girl_stat(KittyX, "love", -3)
                            call change_Girl_stat(KittyX, "obedience", 1)
                            call change_Girl_stat(KittyX, "inhibition", 2)
                            ch_k "I really don't think we should do that."
                    "Put it back.":
                        "You place the box back on the shelf."
            elif StormX.location == Player.location:
                menu:
                    "Since [StormX.name] is around, have her check inside?"
                    "Check in the box":
                        if approval_check(StormX, 700, "I") or approval_check(StormX, 1800):
                            if "Well Studied" not in achievements:
                                call change_Girl_stat(StormX, "obedience", 10)
                                call change_Girl_stat(StormX, "inhibition", 15)
                                ch_s "I suppose I could. . ."
                                "[StormX.name] picks the lock on the box, and pulls out a stack of bills."
                                "Looks like Charles had some money set aside. . ."
                                $ Player.cash += 500
                                "[[$500 acquired.]"
                                $ achievements.append("Well Studied")
                            else:
                                "Looks like this has been thoroughly looted."
                        else:
                            call change_Girl_stat(StormX, "love", -3)
                            call change_Girl_stat(StormX, "obedience", 1)
                            call change_Girl_stat(StormX, "inhibition", 2)
                            ch_s "I really don't think we should do that."
                    "Put it back.":
                        "You place the box back on the shelf."
            else:
                "You can't think of any way to get it open, too bad you aren't a ghost or something."
                "You place the box back on the shelf."
        elif D20 >= 15:
            "There doesn't seem to be anything more of interest in here."
        else:
            "You search through the books for a few minutes, but don't find anything."
            "It would probably take a more thorough search."
    elif line == "left":
        if "Xavier's photo" not in Player.inventory:
            if D20 >= 10:
                "Buried under a pile of documents, you find a printed out photo."
                "It appears to be a selfie of Mystique making out with Xavier."
                "She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                if StormX.location == Player.location:
                    ch_s "You should probably put that back, it looks personal."
                else:
                    "[[Xavier's photo acquired.]"
                    $ Player.inventory.append("Xavier's photo")
                    if "kappa" in Player.history:
                        $ Player.history.remove("kappa")
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."
        else:
            "There doesn't seem to be anything more of interest in here."
    elif line == "middle":
        if "all" not in Player.Keys:
            "Under a few trinkets, you find a small keyring."
            "[[Keyring acquired.]"
            if "Xavier" not in Player.Keys:
                $ Player.Keys.append("Xavier")
            if RogueX not in Player.Keys:
                $ Player.Keys.append(RogueX)
            if KittyX not in Player.Keys:
                $ Player.Keys.append(KittyX)
            if EmmaX not in Player.Keys:
                $ Player.Keys.append(EmmaX)
            if LauraX not in Player.Keys:
                $ Player.Keys.append(LauraX)
            if JeanX not in Player.Keys:
                $ Player.Keys.append(JeanX)
            if StormX not in Player.Keys:
                $ Player.Keys.append(StormX)
            if JubesX not in Player.Keys:
                $ Player.Keys.append(JubesX)
            if "all" not in Player.Keys:
                $ Player.Keys.append("all")
        else:
            "There doesn't seem to be anything interesting in here."
    elif line == "right":
        "There doesn't seem to be anything more of interest in here, maybe later?"
        if "Xavier's files" not in Player.inventory:
            if D20 >= 10:
                "You search through some documents, but don't find anything."
                if StormX.location == Player.location:
                    ch_s "Hmm. . ."
                    "She reaches under some of the documents and finds a small notch."
                    "With a soft \"click\"a panel flips open in the drawer, revealing some file folders."
                    "Inside are some fairly. . . detailed reports on the girls at the school."
                    $ StormX.change_face("surprised", 2)
                    "These include body measurements, sexual histories. . . masturbation habits?"
                    call change_Girl_stat(StormX, "obedience", 5)
                    call change_Girl_stat(StormX, "inhibition", 5)
                    $ StormX.change_face("angry")
                    ch_s "Well, I don't think Charles should be holding information like this. . ."
                    $ StormX.change_face("normal", 1)
                    "[[Xavier's files acquired.]"
                    $ Player.inventory.append("Xavier's files")
                    if "rho" in Player.history:
                        $ Player.history.remove("rho")
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."
        else:
            "There doesn't seem to be anything more of interest in here."

    $ counter += 3
    jump study_Explore


label execute_plan(Girl):
    if "Xavier" in Player.daily_history:
        "The Professor seems pretty out of it."
        "You don't think you'll be able to get anything more out of him today."
        "You leave him to it."

        $ Player.location = "bg_player"

        jump reset_location

    $ shift_focus(Girl)

    $ Girl.change_face("sly")

    "As you say this, a sly grin crosses [Girl.name]'s face."
    "You quickly approach Xavier and place your hands on his head."

    $ Xavier.change_face("psychic")

    ch_x ". . ."

    $ Xavier.change_face("shocked")

    "Xavier realizes with a shock that with your powers, his telepathy is useless."

    if Partner:
        $ first_time = False

        if Partner == RogueX and "Omega" not in Player.traits:
            $ first_time = True
        elif Partner == KittyX and "Kappa" not in Player.traits:
            $ first_time = True
        elif Partner == EmmaX and "Psi" not in Player.traits:
            $ first_time = True
        elif Partner == LauraX and "Chi" not in Player.traits:
            $ first_time = True
        elif Partner == JeanX and "Alpha" not in Player.traits:
            $ first_time = True
        elif Partner == StormX and "Rho" not in Player.traits:
            $ first_time = True
        elif Partner == JubesX and "Zeta" not in Player.traits:
            $ first_time = True

        if first_time:
            if approval_check(Partner, 1000) or Partner == JeanX:
                $ Partner.change_face("surprised")

                "[Partner.name] looks a bit caught off guard, but goes along with the idea."

                $ Partner.change_face("sly")
            else:
                $ Partner.change_face("surprised")

                "[Partner.name] looks a bit uncomfortable with what's happening and takes off."

                call remove_Girl(Partner)
        else:
            $ Partner.change_face("sly")

            "[Partner.name] understands what's going on here."

    $ Xavier.change_face("angry")

    if Girl == RogueX:
        $ RogueX.take_off("gloves")
        $ RogueX.arm_pose = 2

        call show_Girl(RogueX, x_position = stage_left + 0.1, y_position = 0.1, sprite_layer = 1, transition = ease)

        "[RogueX.name] moves in and also grabs his head, duplicating his powers as he watches helplessly."
        "Now that she posesses his full power, while his are negated, he has no defenses."

        $ Xavier.change_face("hypno")

        if "Omega" in Player.traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"

            call change_Girl_stat(RogueX, "obedience", 3)
            call change_Girl_stat(RogueX, "inhibition", 1)
        else:
            call change_Girl_stat(RogueX, "obedience", 40)
            call change_Girl_stat(RogueX, "inhibition", 20)

        ch_r "Well, [RogueX.player_petname], what would you like to do with this opportunity?"
        ch_r "I think we'll only get three tries at this. . ."
    elif Girl == KittyX:
        $ KittyX.arm_pose = 2

        call show_Girl(KittyX, x_position = stage_left + 0.1, y_position = 0.2, transition = ease)

        $ KittyX.sprite_location = stage_center

        "[KittyX.name] moves in and sits on his lap, pinning his arms to the chair."

        if "Kappa" in Player.traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"

            call change_Girl_stat(KittyX, "obedience", 3)
            call change_Girl_stat(KittyX, "inhibition", 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            "You pull out the photo you found earlier in his study."

            call change_Girl_stat(KittyX, "obedience", 40)
            call change_Girl_stat(KittyX, "inhibition", 30)

            ch_p "I have here a rather. . . compromising photo of you and Mystique."
            ch_p "I was thinking maybe you could cut me a little slack around here."
            ch_x "And if I do not?"
            ch_p "[KittyX.name] here's set it to distribute to every computer in school, every day."
            ch_p "And only I know the password."
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ."

            call change_Girl_stat(KittyX, "obedience", 30)
            call change_Girl_stat(KittyX, "inhibition", 10)

        ch_k "Well, [KittyX.player_petname], what should we ask for?"
    elif Girl in [EmmaX, JeanX]:
        call show_Girl(Girl, x_position = stage_left + 0.1, y_position = 0.1, sprite_layer = 1, transition = ease)

        "[Girl.name] moves behind Xavier and activates her own telepathy."

        $ Xavier.change_face("angry")

        if (Girl == EmmaX and "Psi" in Player.traits) or (Girl == JeanX and "Alpha" in Player.traits):
            ch_x "Oh, not again. . ."

            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "inhibition", 1)
        else:
            call change_Girl_stat(Girl, "obedience", 40)
            call change_Girl_stat(Girl, "inhibition", 30)
            call change_Girl_stat(Girl, "obedience", 30)
            call change_Girl_stat(Girl, "inhibition", 10)

        Girl.voice "Well, [Girl.player_petname], what should we ask for?"
    elif Girl == LauraX:
        $ LauraX.arm_pose = 2

        if "Chi" in Player.traits:
            ch_x "Oh, not again."

            $ LauraX.claws = 1

            ch_x "What is it you want this time?"

            call change_Girl_stat(LauraX, "obedience", 3)
            call change_Girl_stat(LauraX, "inhibition", 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            ch_p "[LauraX.name] and I were talking, and it seems like neither of us appreciates you bothering us."
            ch_x "And if I continue?"
            ch_p "My little [LauraX.petname] here has a very particular set of skills, you know. . ."

            $ LauraX.name_check()
            $ LauraX.claws = 1
            $ LauraX.change_face("sly")

            ch_p "She could cause a lot of trouble if she keeps getting called down here. . ."
            "[LauraX.name] draws her claws along the arm of the Professor's chair, tracing fine lines into the metal."
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ."

            call change_Girl_stat(LauraX, "obedience", 40)
            call change_Girl_stat(LauraX, "inhibition", 30)
            call change_Girl_stat(LauraX, "obedience", 30)
            call change_Girl_stat(LauraX, "inhibition", 10)

        ch_l "Well, [LauraX.player_petname], what should we ask for?"
    elif Girl == StormX:
        $ StormX.arm_pose = 1

        call show_Girl(StormX, x_position = stage_left + 0.1, y_position = 0.2, transition = ease)

        $ StormX.sprite_location = stage_center

        "[StormX.name] moves in and sits on his lap, pinning his arms to the chair."

        if "Rho" in Player.traits:
            ch_x "Oh, not this again."
            ch_x "What is it you want this time?"

            call change_Girl_stat(StormX, "obedience", 3)
            call change_Girl_stat(StormX, "inhibition", 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"
            "You pull out the files you found earlier in his study."

            call change_Girl_stat(StormX, "obedience", 40)
            call change_Girl_stat(StormX, "inhibition", 30)

            ch_p "I have here some rather. . . questionable \"medical\" files."
            ch_p "I was thinking maybe you could cut me a little slack around here."
            ch_x "And if I do not?"
            ch_p "We've made sure that -all- the girls in these files will find out."
            ch_x "Very well. . . I'll forget about your punishment."
            ch_p "Oh, I think we can do a bit better than that. . ."

            call change_Girl_stat(StormX, "obedience", 30)
            call change_Girl_stat(StormX, "inhibition", 10)

        ch_s "Well, [StormX.player_petname], what should we ask for?"
    elif Girl == JubesX:
        $ JubesX.arm_pose = 2

        call show_Girl(KittyX, x_position = stage_left + 0.1, y_position = 0.2, transition = ease)

        $ JubesX.sprite_location = stage_center

        "[JubesX.name] moves in and sits on his lap, pinning his arms to the chair."
        "She turns to look at him."

        if "Zeta" in Player.traits:
            ch_x "Oh, not again."
            ch_x "What is it you want this time?"

            call change_Girl_stat(JubesX, "obedience", 3)
            call change_Girl_stat(JubesX, "inhibition", 1)
        else:
            ch_x "What is the meaning of this? Unhand me!"

            call change_Girl_stat(JubesX, "inhibition", 30)

            ch_v "Look into my eyes. . ."

            call change_Girl_stat(JubesX, "obedience", 40)
            call change_Girl_stat(JubesX, "inhibition", 10)

            ch_v "See the sparks dancing around them? . . ."

            call change_Girl_stat(JubesX, "obedience", 30)

            "She slowly mesmerizes him into a trance, using a combination of her vampiric abilties and fireworks. . ."

        ch_v "Well, [JubesX.player_petname], what should we ask for?"

    $ count = 3
    $ Player.being_punished = 0

    while count > 0:
        $ count -= 1

        menu:
            ch_x "What do you want?"
            "Don't bother us anymore when we're having fun." if Girl not in Rules:
                ch_x "Very well. . . I could offer you some. . . discretion. . ."

                $ Rules.append(Girl)
            "You know, it's kinda fun dodging you, catch us if you can." if Girl in Rules:
                ch_x "If you. . . want me to, I suppose. . ."

                $ Rules.remove(Girl)
            "You know, [JeanX.name] should be able to \"whammy\" people again." if "nowhammy" in JeanX.traits:
                ch_x "I could remove her mind-wiping ban. . ."

                $ JeanX.traits.remove("nowhammy")
                $ JeanX.traits.append("whammy")

                if JeanX.location == Player.location:
                    call change_Girl_stat(JeanX, "obedience", 5)
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "love", 5)
                    call change_Girl_stat(JeanX, "love", 5)
                    $ Girl.change_face("sly", 1)

                    ch_j "Nice. . ."
            "You know, I did like it when [JeanX.name] couldn't use her \"whammy.\"" if "whammy" in JeanX.traits:
                ch_x "I could reinstate her mind-wiping ban. . ."

                $ JeanX.traits.append("nowhammy")
                $ JeanX.traits.remove("whammy")

                if JeanX.location == Player.location:
                    call change_Girl_stat(JeanX, "obedience", 5)
                    call change_Girl_stat(JeanX, "obedience", 5)
                    call change_Girl_stat(JeanX, "love", -5)
                    call change_Girl_stat(JeanX, "love", -5)
                    $ JeanX.change_face("angry", 1, mouth = "surprised")

                    ch_j "Hey!"

                    $ JeanX.change_face("angry", 1)
            "Raise my stipend." if Player.income < 30:
                if Girl == RogueX and "Omega" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."

                    $ Player.income += 2
                elif Girl == KittyX and "Kappa" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."

                    $ Player.income += 2
                elif Girl == EmmaX and "Psi" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."

                    $ Player.income += 2
                elif Girl == LauraX and "Chi" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."

                    $ Player.income += 2
                elif Girl == JeanX and "Alpha" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."

                    $ Player.income += 2
                elif Girl == StormX and "Rho" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."

                    $ Player.income += 2
                elif Girl == JubesX and "Zeta" not in Player.traits:
                    ch_x "Very well. . . but I can only raise it by so much. . ."

                    $ Player.income += 2
                else:
                    ch_x "I'm afraid I can't manage any more than I have. . ."

                    $ count += 1
            "Raise my stipend. [[Used](locked)" if Player.income >= 30:
                pass
            "I was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Player.Keys:
                        ch_x "Fine, take it. . ."

                        $ Player.Keys.append("Xavier")
                    "Give me the key to your study. [[Owned] (locked)" if "Xavier" in Player.Keys:
                        pass
                    "Give me the key to [Girl.name]'s room." if Girl not in Player.Keys:
                        ch_x "I. . . suppose I could do that. . ."

                        $ Player.Keys.append(Girl)
                    "Give me the key to [Girl.name]'s room.[[Owned] (locked)" if Girl in Player.Keys:
                        pass
                    "Never mind.":
                        $ count += 1
            "That should do it.":
                $ count = 0

    ch_x "Very well, that should conclude our business. Please leave."

    if Girl == RogueX:
        if "Omega" not in Player.traits:
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "love", 30)
            call change_Girl_stat(Girl, "love", 20)

            $ Player.traits.append("Omega")

        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."

        $ Girl.Clothes["gloves"] = "gloves"
        $ Girl.arm_pose = 1
    elif Girl == KittyX:
        if "Kappa" not in Player.traits:
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 10)
            call change_Girl_stat(Girl, "love", 10)
            call change_Girl_stat(Girl, "love", 20)

            $ Player.traits.append("Kappa")

        $ Girl.arm_pose = 1
    elif Girl == EmmaX:
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."

        if "Psi" not in Player.traits:
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 10)
            call change_Girl_stat(Girl, "love", 10)
            call change_Girl_stat(Girl, "love", 20)

            $ Player.traits.append("Psi")
    elif Girl == LauraX:
        if "Chi" not in Player.traits:
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 10)
            call change_Girl_stat(Girl, "love", 10)
            call change_Girl_stat(Girl, "love", 20)

            $ Player.traits.append("Chi")

        $ Girl.arm_pose = 1
        $ Girl.claws = 0
    elif Girl == JeanX:
        ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here."

        if "Alpha" not in Player.traits:
            call change_Girl_stat(Girl, "lust", 20)
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 10)
            call change_Girl_stat(Girl, "obedience", 10)
            call change_Girl_stat(Girl, "obedience", 20)
            call change_Girl_stat(Girl, "love", 10)
            call change_Girl_stat(Girl, "love", 20)

            $ Player.traits.append("Alpha")
    elif Girl == StormX:
        if "Rho" not in Player.traits:
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 10)
            call change_Girl_stat(Girl, "love", 10)
            call change_Girl_stat(Girl, "love", 20)

            $ Player.traits.append("Rho")
    elif Girl == JubesX:
        if "Zeta" not in Player.traits:
            call change_Girl_stat(Girl, "lust", 10)
            call change_Girl_stat(Girl, "inhibition", 10)
            call change_Girl_stat(Girl, "love", 10)
            call change_Girl_stat(Girl, "love", 20)

            $ Player.traits.append("Zeta")

        $ Girl.arm_pose = 1

    $ Player.daily_history.append("Xavier")

    jump reset_location
