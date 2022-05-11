label prologue:
    $ bg_current = "bg study"
    $ Time_Count = 2
    $ Current_Time = "Evening"
    call display_background

    if "Historia" in Player.Traits:
        show BlueScreen onlayer black

    "You recently discovered that you were a mutant when a Sentinel attacked your home.\nYou were rescued by a squad of X-Men and given this address."
    "You've arrived in the early evening at the Xavier Institute, where you've been promised a new home."
    "Things have been tough for mutants in the years since Apocalypse's fall, but this sounds like it might be a good deal."

    if "Historia" not in Player.Traits:
        python:
            Player.Name = renpy.input("What is your name?", default="Zero", length = 10)
            Player.Name = Player.Name .strip()

            if not Player.Name :
                Player.Name  = "Zero"

            if Player.Name in ("master", "sir", "lover", "boyfriend", "sex friend", "fuck buddy"):
                Line = "Nice try, smartass."
                Player.Name  = "Zero"

        if Line:
            "[Line]"
        menu:
            "What is your skin color?"
            "Green":
                $ Player.Color = "green"
            "White":
                $ Player.Color = "pink"
            "Black":
                $ Player.Color = "brown"

    show Professor at sprite_location(StageLeft) with dissolve

    ch_x "Welcome to the Xavier Institute for Higher Learning. This is a home for all mutants to learn and grow."
    ch_x "My name is Charles Xavier, and I have dedicated my life to helping other mutants such as yourself."
    ch_x "I know that you've had a difficult time, but you will be safe here."
    ch_x "You'll have classes in the day to teach you the skills you'll need, and training in the danger room for self defense."
    ch_x "Since you're on your own, we'll provide a small stipend for your day-to-day needs."
    ch_x "Did you have any questions for me young man?"
    ch_p "Why did you even bring me here, I don't have any \"super powers.\""
    ch_x "Nonsense, my boy. You have an incredibly useful ability. . ."
    ch_x "the power to negate other powers, even including my own."

    $ RogueX.Loc = bg_current
    $ RogueX.FaceChange("surprised")
    $ RogueX.sprite_location = StageFarRight

    show Rogue_Sprite at sprite_location(RogueX.sprite_location) with easeinright

    ch_r "What's that Prof? This new kid can negate mutant powers?"

    $ RogueX.Mouth = "normal"
    $ RogueX.sprite_location = StageRight

    show Rogue_Sprite at sprite_location(RogueX.sprite_location) with ease

    ch_r "Maybe even my own?"
    ch_x "That is correct, [RogueX.Name], though currently, his powers are weak and uncontrolled."
    ch_x "One day, however, he may even be able to help you turn your powers off permanently."
    ch_r "! . . ."

    $ RogueX.FaceChange("smile")

    ch_x "Since you're here, why don't you show our new guest around the mansion?"

    ch_x "This young lady is named [RogueX.Name], one of our veteran students."
    ch_x "And [RogueX.Name], this young man goes by the name \"[Player.Name]\"."

    hide Professor with easeoutright

    $ RogueX.sprite_location = StageCenter

    show Rogue_Sprite at sprite_location(RogueX.sprite_location) with ease

    $ ActiveGirls.append(RogueX) if RogueX not in ActiveGirls else ActiveGirls

    menu:
        ch_r "A pleasure ta meet ya, [RogueX.Petname]. Let me give ya the lay of the place."
        "It's nice to meet you too.":
            $ RogueX.Statup("Love", 200, 20)
            $ RogueX.FaceChange("smile", 1)

            ch_r "Oh, a gentleman. I think we'll really get along."

            $ RogueX.Blush = 0

            ch_r "Ok, so let me show ya around. . ."
        "The \"lay\" of the place, eh?":
            $ RogueX.Statup("Love", 200, 10)
            $ RogueX.Brows = "normal"
            $ RogueX.Eyes = "surprised"
            $ RogueX.Mouth = "smile"
            $ RogueX.Blush = 1

            ch_r "Wha- what? N, no, that's not what I meant! I'm just giving you the campus tour!"

            $ RogueX.FaceChange("bemused")
            $ RogueX.Statup("Inbt", 200, 20)
            $ RogueX.Statup("Obed", 200, 20)

            ch_r "Hmm. . ."

            $ RogueX.Statup("Lust", 90, 3)
            $ RogueX.FaceChange("normal")
            $ RogueX.Eyes = "surprised"

            ch_r "Anyways, let's get this back on track. . ."

            $ RogueX.FaceChange("smile", 0)
        "Whatever.":
            $ RogueX.Statup("Obed", 200, 20)
            $ RogueX.FaceChange("sad")
            $ RogueX.Brows = "normal"

            ch_r "Tsk, well ok, let's get started."
        "Screw off.":
            $ RogueX.Statup("Love", 200, -30)
            $ RogueX.Statup("Obed", 200, 30)
            $ RogueX.FaceChange("angry")

            show Rogue_Sprite at sprite_location(RogueX.sprite_location) with vpunch

            ch_r "Well I never!"
            ch_r "Hmph, I have to give the tour anyways, so get mov'in. . ."

label tour_start:
    $ bg_current = "bg campus"

    $ RogueX.Loc = bg_current

    call Set_The_Scene(0)

    show Rogue_Sprite at sprite_location(RogueX.sprite_location)

    ch_r "This is the campus square. It links up to all the major locations on campus and you'll probably pass through here a lot."

    $ bg_current = "bg player"

    $ RogueX.Loc = bg_current

    call Set_The_Scene(0)

    show Rogue_Sprite at sprite_location(RogueX.sprite_location)

    ch_r "This will be your room, we each get private rooms now that the campus has been expanded."

    menu:
        ch_r "Pretty nice, right?"
        "It is with you in it.":
            $ RogueX.Blush = 1
            $ RogueX.Statup("Love", 200, 20)
            $ RogueX.Statup("Lust", 90, 5)
        "It'll do.":
            $ RogueX.Statup("Obed", 200, 10)

    ch_p "And where do you live?"

    $ RogueX.Blush = 0

    ch_r "Oh, right down the hall, all the doors are labeled."

    if RogueX.Love <= 500:
        ch_r "I wouldn't recommend bothering me though."
    else:
        ch_r "You can stop by sometime, but not after curfew."

    $ bg_current = "bg classroom"

    $ RogueX.Loc = bg_current

    call CleartheRoom("All",0,1)
    call Set_The_Scene(0)

    show Rogue_Sprite at sprite_location(RogueX.sprite_location)

    ch_r "And this is one of our state-of-the-art classrooms."
    ch_r "They're multi-purpose so they can teach almost anything in them."
    ch_r "This used to just be an after school training facility, but over the past few years it's grown into a full service university."

    $ bg_current = "bg dangerroom"

    $ RogueX.Loc = bg_current

    call Set_The_Scene(0)

    show Rogue_Sprite at sprite_location(RogueX.sprite_location)

    ch_r "And this is the Danger Room. It's been upgraded to a fully holographic experience, allowing realistic battlefield simulations."

    $ Count = 0
    while Count < 3:
        menu:
            extend ""
            "Why would you need battlefield simulations?" if Count != 1:
                    ch_r "The world is a dangerous place, [RogueX.Petname], especially for us mutants."
                    ch_r "This place helps us train to use our powers. Coming here can help you to get a grasp on yours as well."

                    $ Count = 3 if Count == 2 else 1
            "So can this place make some more. . . erotic simulations?" if Count != 2:
                    $ RogueX.Eyes = "side"
                    $ RogueX.Mouth = "lipbite"
                    $ RogueX.Blush = 1
                    $ RogueX.Statup("Inbt", 200, 30)
                    $ RogueX.Statup("Lust", 200, 5)

                    ch_r "Well. . . I suppose it could. . . if one were into such things."

                    $ RogueX.FaceChange(B=0)

                    $ Count = 3 if Count == 1 else 2
            "Ok, let's move on.":
                    $ Count = 3
    $ Count = 0

    ch_r "Moving on then. . ."

label tour_end:
    $ bg_current = "bg campus"
    $ RogueX.Loc = bg_current

    call Set_The_Scene(0)

    show Rogue_Sprite at sprite_location(RogueX.sprite_location)

    ch_r "Well, that's the nickel tour, now you know where everything is. . ."

    $ RogueX.Mouth = "normal"
    $ RogueX.Eyes = "normal"
    $ RogueX.Brows = "confused"

    menu:
        ch_r "I was curious about your ability. Is it true that other mutant powers don't work on you?"
        "Sure.":
            ch_p "That's what they tell me, but to be honest, I don't know much about it."
        "What's it to you?":
            ch_p "What do you care?"

            $ RogueX.Eyes = "sexy"

            ch_r ". . ."

            $ RogueX.Statup("Love", 200, -30)

    ch_r "Well, you see, my power is the ability to absorb the mutant powers and memories of those I touch."

    $ Head = 0

    ch_r "Only, I still can't really control it. I can't touch people without hurting them, and I might even put them into a coma if I'm not careful."
    ch_r "So I was hoping that maybe with your power. . ."

    $ RogueX.FaceChange("sexy")
    $ RogueX.Brows = "sad"

    menu:
        ch_r "So I was hoping that maybe with your power. . . I could touch you?"
        "Like, a kiss?":
            if RogueX.Love >= 500:
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Obed", 200, 30)
                $ RogueX.Statup("Inbt", 20, 20)
                $ RogueX.FaceChange("surprised", 1)

                ch_r "Well, aren't you fresh."

                $ RogueX.FaceChange("sexy")
                $ RogueX.Mouth = "smile"

                ch_r "Just this once."

                $ RogueX.FaceChange("kiss")
                call girl_kissing_smooch(RogueX)

                "She gives you a little peck on the cheek."

                $ RogueX.FaceChange("smile")
            else:
                $ RogueX.Statup("Love", 200, 30)
                $ RogueX.FaceChange("bemused")

                ch_r "Heh, You'll have to earn that [RogueX.Petname]."

                $ RogueX.Arms = 0
                $ RogueX.ArmPose = 2
                $ RogueX.FaceChange("sexy")
                $ RogueX.Brows = "sad"

                "She pulls off her glove and touches your face."
        "Ok, be my guest.":
            $ RogueX.Statup("Love", 200, 30)
            $ RogueX.FaceChange("smile")
            $ RogueX.Arms = 0
            $ RogueX.ArmPose = 2
            $ RogueX.FaceChange("sexy")
            $ RogueX.Brows = "sad"

            "She pulls off her glove and touches your face."
        "No, that's weird.":
            $ RogueX.Statup("Love", 200, -30)
            $ RogueX.Statup("Inbt", 200, 30)
            $ RogueX.FaceChange("sad")
            $ RogueX.Brows = "normal"

            ch_r "Well I'm just too damned curious, sorry."

            $ RogueX.Arms = 0
            $ RogueX.ArmPose = 2

            "She pulls off her glove and touches your face."

    $ RogueX.FaceChange("surprised")

    ch_r "Wow."
    ch_r "This is amazing! With anyone else I would have drained their powers and they'd be out by now."

    $ RogueX.FaceChange("sexy")

    menu:
        ch_r "Do you know how long it's been since I've felt human contact without hurting them?"
        "Glad I could help.":
            $ RogueX.Statup("Love", 200, 10)
        "I'm guessing it's been quite a while.":
            $ RogueX.Statup("Lust", 200, 5)
            $ RogueX.FaceChange("bemused", 1)

            ch_r ". . ."

    $ RogueX.FaceChange("smile")

    ch_r "What a rush. I guess that's it then, I'm heading back to my room, you can head to yours."

    $ RogueX.Blush = 0

    if RogueX.Love >= 500:
        ch_r "Maybe I'll see you around though. Here's my number, you can give me a call."

        if "Historia" not in Player.Traits:
            $ Digits.append(RogueX)

    $ RogueX.Arms = "gloves"
    $ RogueX.ArmPose = 1
    $ RogueX.Addictionrate = 5

label tour_parting:
    $ RogueX.Emote = "normal"
    $ RogueX.Blush = 0

    if not RogueX.Kissed:
        $ Line = "Want to make out a little?"
    else:
        $ Line = "Want to make out a little more?"

    menu:
        extend ""
        "Ok, See you later.":
            "You head back to your room."
        "[Line]":
            if RogueX.Love >= 560:
                $ RogueX.FaceChange("bemused", 1)
                $ RogueX.Statup("Inbt", 10, 20)
                $ RogueX.Statup("Inbt", 50, 10)

                if "Historia" in Player.Traits:
                    return 1

                call Makeout(RogueX)
                if "angry" in RogueX.RecentActions:
                    $ RogueX.Statup("Love", 200, -10)
                    $ RogueX.Statup("Obed", 200, 30)

                    ch_r "What the hell, [Player.Name]?!"
                    ch_r "Way to take advantage of a girl's feelings there!"

                    hide Rogue_Sprite with easeoutright

                    "[RogueX.Name] tears off and you head back to your room."
                else:
                    $ RogueX.FaceChange("bemused", 1)

                    ch_r "That was real nice, [RogueX.Petname]. I'll definitely be seeing you later."

                    hide Rogue_Sprite with easeoutright

                    "You head back to your room."

                    $ RogueX.Emote = "normal"
            else:
                if (RogueX.Love >= 530 or RogueX.Obed > 50) and not RogueX.Kissed:
                    $ RogueX.Addictionrate += 1
                    $ RogueX.Statup("Lust", 200, 5)
                    $ RogueX.Statup("Love", 200, 10)
                    $ RogueX.Kissed += 1
                    $ RogueX.FaceChange("bemused", 1)

                    ch_r "Well, maybe one kiss."

                    $ RogueX.FaceChange("kiss")

                    "She gives you a quick kiss. No tongue."

                    jump tour_parting
                else:
                    $ RogueX.FaceChange("bemused")

                    ch_r "Nah, I think you've had enough for today, [RogueX.Petname]."
                    "You head back to your room."

                    hide Rogue_Sprite

                    $ RogueX.Emote = "normal"

    $ RogueX.Loc = "bg rogue"

    if "Historia" in Player.Traits:
        return 0

    $ bg_current = "bg player"
    call Wait

    $ bg_current = "bg player"
    call Set_The_Scene

    "This is a short tutorial on the game's features. Feel free to skip it, you can always view it later in this room."

    call Tutorial
    jump player_room

    return

label Rogue_Love:
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")

    if bg_current != "bg rogue":
        if RogueX.Loc == bg_current or RogueX in Party:
            "Suddenly, [RogueX.Name] says she wants to talk to you in her room and drags you over there."
        else:
            "[RogueX.Name] shows up, hurridly says she wants to talk to you in her room and drags you over there."
    else:
        "[RogueX.Name] suddenly stares at you very intently."

    $ Player.AddWord(1,"interruption") #adds to Recent
    $ bg_current = "bg rogue"
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    if RogueX in Player.Harem:
            ch_r "We've been dating for a while now, and I'm really feeling close to you."
    else:
            ch_r "We've been hanging out for a while now, and I'm really feeling close to you."
    ch_r ". . ."
    $ RogueX.Eyes = "sexy"
    menu:
        ch_r "Right?"
        "I love you, [RogueX.Name].":
                $ RogueX.Statup("Love", 200, 50)
                $ RogueX.Event[6] = 10
        "Yeah, it's been great.":
                $ RogueX.Statup("Love", 200, 20)
        "Yeah, I guess":
                $ RogueX.Statup("Love", 200, 10)
        "Um, maybe?":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[6]:
            ch_r "Right, so I was thinking. . ."
            ch_r "I love you."
    elif RogueX.Event[6] == 10:
            $ RogueX.FaceChange("confused")
            ch_r "So. . . wait, what?"
            $ RogueX.FaceChange("smile",2)
            $RogueX.Brows = "surprised"
            ch_r "I love you too!"
            $ RogueX.FaceChange("kiss")
            "Rogue leaps into your arms and gives you a kiss."
            $ RogueX.FaceChange("sexy",1)
            $ RogueX.Kissed += 1
    else:
            ch_r "Even though we've had our rough patches from time to time. . ."
            ch_r "I still love you."
    $ RogueX.Event[6] += 1
    if RogueX.Event[6] < 10:
        menu:
            extend ""
            "I love you too.":
                    $ RogueX.Statup("Love", 200, 50)
                    "[RogueX.Name] collapses into your arms."
            "That's great!":
                    $ RogueX.Brows = "confused"
                    "[RogueX.Name] seems a bit perplexed, but takes it as a positive sign and hugs you."
            "I know.":
                    $ RogueX.FaceChange("smile")
                    $ RogueX.Brows = "confused"
                    "[RogueX.Name] punches you in the arm and then gives you a huge hug."
            "So?":
                    jump Rogue_Love_Jerk
            "Well I don't think of you like that.":
                    $ RogueX.Statup("Love", 200, -50)
                    $ RogueX.Statup("Obed", 200, 50)
                    jump Rogue_Love_Jerk
    $ RogueX.FaceChange("bemused",1,Eyes="side")
    $ RogueX.Petnames.append("lover")
    call Rogue_AnnaMarie        #plays new name dialog
    ch_r "Anyway, I am glad I've been able to share this with you."
    $ RogueX.FaceChange("sly")
    ch_r "I'm hoping to share a lot more with you if I can. . ."
    if not RogueX.Sex:
        $ RogueX.Statup("Obed", 70, 10)
        ch_r "So. . . did you want to . . . consumate this?"
        menu:
            extend ""
            "Yeah. . . [[have sex]":
                    $ RogueX.Statup("Inbt", 30, 30)
                    ch_r "Hmm. . ."
                    if "Historia" in Player.Traits:
                        return 1
                    call Rogue_SexAct("sex")
                    return
            "I have something else in mind. . .[[choose another activity]":
                    $ RogueX.Brows = "confused"
                    $ RogueX.Statup("Obed", 70, 20)
                    ch_r "Well now you've got me curious. . ."
                    pass
            "Ew. [[do nothing]":
                    $ RogueX.Statup("Love", 200, -10)
                    $ RogueX.Statup("Obed", 70, 40)
                    $ RogueX.FaceChange("perplexed",1)
                    ch_r "Um, ok?"
                    ch_r "{size=-5}What the fuck was that?{/size}"          #fix test this
                    return
    else:
            ch_r "Now, lover. . . was there anything else you felt like doing to celebrate?"
    if "Historia" in Player.Traits:
            return 1
    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ temp_modifier = 20
    call Rogue_SexMenu
    $ temp_modifier = 0
    return

label Rogue_Love_Jerk:
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    $ RogueX.FaceChange("angry", 1)
    ch_r "Well fine!"
    $ Count = (20* RogueX.Event[6])
    $ RogueX.Statup("Obed", 50, 40)
    $ RogueX.Statup("Obed", 200, Count)
    if RogueX.Event[6] == 3:
            $ RogueX.FaceChange("sad")
            ch_r "I. . . I don't care, I love you too much anyways."
            ch_r "I need some time to myself though."
            if "Historia" in Player.Traits:
                    return 1
            $ RogueX.Petnames.append("lover")
            $ Achievements.append("One Sided Love")
            $ RogueX.Loc = "bg rogue"
            $ bg_current = "bg player"
            call Remove_Girl(RogueX)
            jump player_room
    if RogueX.Event[6] > 1:
            ch_r "Fool me once, shame on you. . . I thought you'd grown."
    ch_r "If that's how you want to be, you can get the hell out of here!"
    $ Count = (100* RogueX.Event[6])
    $ RogueX.Statup("Love", 200, -Count)
    if "Historia" in Player.Traits:
            return 0
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump player_room

label Rogue_AnnaMarie:
    ch_r "I should probably tell you, I wasn't exactly born with the name \"Rogue.\""
    ch_r ". . ."
    $ RogueX.FaceChange("bemused",1)
    ch_r "Grow'in up, I went by \"Anna-Marie.\""
    $ RogueX.Names.append("Anna-Marie")
    $ RogueX.Names.append("Anna")
    $ RogueX.Names.append("Marie")
    menu:
        extend ""
        "That's a lovely name.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 50, 5)
                $ RogueX.Statup("Inbt", 70, 5)
                $ RogueX.FaceChange("smile",2)
                ch_r "Oh, thank you so much for say'in. . ."
        "Huh, ok.":
                $ RogueX.Statup("Obed", 80, 5)
                $ RogueX.FaceChange("confused",1)
                ch_r "Um. . . yeah."
        "Don't like it.":
                $ RogueX.Statup("Love", 200, -5)
                $ RogueX.Statup("Obed", 200, 10)
                $ RogueX.Statup("Inbt", 200, -5)
                $ RogueX.FaceChange("angry",1)
                ch_r "Oh. . . Ok. . ."
    menu:
        extend ""
        "I think \"Rogue\" suits you though.":
                $ RogueX.Name = "Rogue"
                $ RogueX.FaceChange("smile")
                ch_r "Yeah, I'm used to it by this point."
        "I liked the sound of \"Anna-Marie.\"":
                $ RogueX.Name = "Anna-Marie"
                $ RogueX.FaceChange("smile")
                ch_r "It might be fun to go back like that again. . ."
        "\"Marie\" would be a cute name for you.":
                $ RogueX.Name = "Marie"
                $ RogueX.FaceChange("smile")
                ch_r "You think? I suppose. . ."
        "\"Anna\" sounds nice.":
                $ RogueX.Name = "Anna"
                $ RogueX.FaceChange("smile")
                ch_r "I suppose it does. . ."
    return

label Rogue_Sub:
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    if RogueX.Loc != bg_current and RogueX not in Party:
            "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."

    $ Player.AddWord(1,"interruption") #adds to Recent
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."
    if RogueX in Player.Harem:
            ch_r "We've been dating for a bit now."
    else:
            ch_r "We've been hanging out for a while now."
    if RogueX.FondleB or RogueX.FondleP or RogueX.FondleA:
            ch_r "I've let you touch me. . ."
    if RogueX.Hand or RogueX.Blow:
            ch_r "I've touched you. . ."
    if RogueX.Love >= 900 and (RogueX in Player.Harem):
            ch_r "I love you so much. . ."
    elif RogueX.Love >= 800:
            ch_r "I really care about you."
    elif RogueX.Love >= 500:
            ch_r "We don't exactly get along, but. . . we work, right?"
    else:
            $ RogueX.Brows = "angry"
            ch_r "I really don't like you much, but something about you just. . ."
            ch_r "works for me."
    menu:
        extend ""
        "Yeah, it's been great.":
                $ RogueX.Statup("Love", 200, 20)
        "Yeah, I guess":
                $ RogueX.Statup("Love", 200, 10)
        "Um, maybe?":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[7]:
            ch_r "Right, so I was thinking. . ."
            $ RogueX.Eyes = "sexy"
            ch_r "I'd like you to provide some . . .structure to my life."
    else:
            ch_r "I'd like you to reconsider the offer I made. . ."
            ch_r "the one about giving me some . . .structure."
    $ RogueX.Event[7] += 1
    menu:
        extend ""
        "Sounds interesting, yes.":
                $ RogueX.Statup("Obed", 200, 100)
                $ RogueX.Petnames.append("sir")
                "[RogueX.Name] nods obediently."
        "What do you mean by that?":
                $ RogueX.FaceChange("bemused")
                ch_r "When you. . . encourage me to try new things, it really turns me on."
                ch_r "I'd like you to continue to. . . encourage me."
                menu:
                    ch_r "I mean that I would like you to give me orders, and I will follow them as best I can."
                    "Sounds interesting, ok.":
                            $ RogueX.Statup("Obed", 200, 100)
                            "[RogueX.Name] nods obediently."
                    "Oh, ok, sure.":
                            "[RogueX.Name] seems a bit put out, but takes it as a positive sign and nods."
                    "Oh, no thanks. Take care of things yourself.":
                            jump Rogue_Sub_Jerk
                $ RogueX.Petnames.append("sir")
        "Nah, you can handle things yourself.":
                jump Rogue_Sub_Jerk
    $ RogueX.FaceChange("sexy")
    ch_r "Now, sir. . . was there anything else you wished me to do to celebrate?"
    if "Historia" in Player.Traits:
            return 1
    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ temp_modifier = 10
    call Rogue_SexMenu
    $ temp_modifier = 0
    return

label Rogue_Sub_Jerk:
    $ RogueX.FaceChange("sad", 1)
    ch_r "Hrmph!"
    $ Count = (20* RogueX.Event[7])
    $ RogueX.Statup("Inbt", 50, 30)
    $ RogueX.Statup("Inbt", 200, Count)
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    if RogueX.Event[7] == 2:
            $ RogueX.FaceChange("sad")
            ch_r "I need some time to myself though."
            if "Historia" in Player.Traits:
                    return
            $ RogueX.Petnames.append("sir")
            $ Achievements.append("Nosiree")
            $ bg_current = "bg player"
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump player_room
    if RogueX.Event[7] > 1:
            ch_r "I thought you may have learned to respect my needs by now."
    ch_r "If that's how it is, I would appreciate some time alone."
    $ Count = (20* RogueX.Event[7])
    $ RogueX.Statup("Obed", 200, -Count)
    if "Historia" in Player.Traits:
            return
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump player_room

label Rogue_Master:
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    if RogueX.Loc != bg_current and RogueX not in Party:
            "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."

    $ Player.AddWord(1,"interruption") #adds to Recent
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.DailyActions.append("relationship")
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."

    if RogueX in Player.Harem:
            ch_r "This situation we have has really added some . . . spice to our relationship."
    else:
            ch_r "This situation we have has been very. . . interesting."
    if RogueX.Anal or RogueX.DildoA:
            ch_r "We've even done some butt stuff."
    if RogueX.Love >= 900 and (RogueX in Player.Harem):
            ch_r "I'm devoted to you. . ."
    elif RogueX.Love >= 800:
            ch_r "I really care about you."
    elif RogueX.Love >= 500:
            ch_r "I can't be without you."
    else:
            $ RogueX.Brows = "angry"
            ch_r "I can't stand being with you, but can't stand being without you either."
    menu:
        ch_r "Have I been pleasing you, [RogueX.Petname]?"
        "Certainly.":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Obed", 200, 20)
        "Yeah, I guess.":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 200, 20)
        "Not especially.":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if not RogueX.Event[8]:
                ch_r "Yes, well, given that. . ."
                ch_r "I think that I would like you to be my master, formally."
    else:
                ch_r "I'd like you to reconsider the offer I made. . ."
                ch_r "please be my master."
    $ RogueX.Event[8] += 1
    menu:
        extend ""
        "Very well.":
                $ RogueX.Statup("Obed", 200, 100)
                $ RogueX.Petnames.append("master")
                "[RogueX.Name] bows obediently."
        "What do you mean by that?":
                $RogueX.Brows = "confused"
                ch_r "Well, when you tell me what to do. . ."
                $ RogueX.FaceChange("bemused", 1)
                ch_r "I get really horny."
                ch_r "I just really need for you to tell me what to do."
                menu:
                    ch_r "I mean that I would follow your orders to the letter, so long as I am able."
                    "Oh, ok, sure.":
                            "[RogueX.Name] seems a bit put out, but takes it as a positive sign and nods."
                            $ RogueX.Petnames.append("master")
                    "You should do your own thing, you don't need me telling you what to do.":
                            $RogueX.Brows = "confused"
                            ch_r "Ok, if that's what you want. . ."
                            $ RogueX.Statup("Inbt", 50, 100)
                            $ RogueX.Statup("Inbt", 90, 50)
                            ch_r "For now at least. . ."
                            $ RogueX.Statup("Obed", 200, -200)
                            $ RogueX.Event[8] = 3
                    "Oh, no, sounds like too much work.":
                            jump Rogue_Obed_Jerk
        "Nah, take care of yourself.":
                jump Rogue_Obed_Jerk
    $ RogueX.FaceChange("sexy")
    ch_r "Now, master. . . was there anything else you wished me to do to celebrate?"
    if "Historia" in Player.Traits:
            return 1
    $ temp_modifier = 20
    call Rogue_SexMenu
    $ temp_modifier = 0
    return

label Rogue_Obed_Jerk:
    $ RogueX.FaceChange("sad", 1)
    ch_r "Well fine!"
    $ Count = (20* RogueX.Event[8])
    $ RogueX.Statup("Inbt", 50, 30)
    $ RogueX.Statup("Inbt", 200, Count)
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    if RogueX.Event[8] == 2:
            $ RogueX.FaceChange("sad")
            ch_r "I don't care what you say, this is something I need. MASTER."
            ch_r "I need some time to myself though."
            if "Historia" in Player.Traits:
                    return
            $ RogueX.Petnames.append("master")
            $ Achievements.append("Heavy is the Head")
            $ bg_current = "bg player"
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump player_room
    if RogueX.Event[8] > 1:
            ch_r "I thought you may have learned to respect my needs by now."
    ch_r "If that's how it is, I would appreciate some time alone."
    $ Count = (50* RogueX.Event[8])
    $ RogueX.Statup("Obed", 200, -Count)
    if "Historia" in Player.Traits:
        return
    $ RogueX.Loc = "bg rogue"
    $ bg_current = "bg player"
    call Remove_Girl(RogueX)
    jump player_room

label Rogue_Sexfriend:
    call Shift_Focus(RogueX)
    $ RogueX.DailyActions.append("relationship")
    if RogueX in Player.Harem:
            if RogueX.Loc != bg_current and RogueX not in Party:
                    return
            $ RogueX.DrainWord("asked meet")
            if "stockings and garterbelt" not in RogueX.Inventory:
                    $ RogueX.Inventory.append("stockings and garterbelt")
            $ RogueX.Petnames.append("sex friend")
            $ RogueX.Statup("Inbt", 200, 50)
            "[RogueX.Name] suddenly gives your butt a little squeeze."
            return

    $ RogueX.DrainWord("asked meet")
    if RogueX.Loc != bg_current and RogueX not in Party:
        "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."

    if "stockings and garterbelt" not in RogueX.Inventory:
            $ RogueX.Inventory.append("stockings and garterbelt")
    $ RogueX.Petnames.append("sex friend")
    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.FaceChange("smile", 1)
    ch_r ". . ."
    ch_r "We've been having fun, right?"
    if RogueX.SEXP >= 40:
            ch_r "I mean, we've been getting up to some pretty wild stuff."
    if "ex" in RogueX.Traits:
            ch_r "And we were actually dating for a while. . ."
    else:
            ch_r "And I know we're not \"dating\" dating, but you know. . ."
    menu:
        ch_r "Haven't I been fun to have around?"
        "Yeah, you've been great.":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Inbt", 200, 20)
        "Hmmm. . . yes?":
                $ RogueX.Statup("Inbt", 200, 20)
        "Maybe. . .":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    if RogueX in Player.Harem:
        ch_r "I'd like to have a -lot- more sex. . ."
    if not RogueX.Event[9]:
        ch_r "Ok, so since we've been having so much fun. . ."
        if "ex" in RogueX.Traits:
                ch_r "I think that even though we aren't dating, I still want to be sex friends."
        else:
                ch_r "I think I'm ready to accept just being casual sex friends."
    else:
        ch_r "I'd like you to reconsider my generous offer. . ."
        ch_r "come on, sex friend? Eh?"
    $ RogueX.Event[9] += 1
    if RogueX not in Player.Harem:
            menu:
                extend ""
                "Sounds fun!":
                        $ RogueX.Statup("Inbt", 200, 100)
                        $ RogueX.Petnames.append("sex friend")
                        "[RogueX.Name] nods obediently."
                "What do you mean by that?":
                        $RogueX.Brows = "confused"
                        ch_r "You know, casual sex, no real strings, for now at least."
                        menu:
                            ch_r "Well?"
                            "Oh, ok, sure.":
                                    "[RogueX.Name] is a bit put off, but grabs you in a big hug anyway."
                            "Oh, no thanks. Not interested.":
                                    jump Rogue_Sexfriend_Jerk
                "Nah, you're on your own.":
                        jump Rogue_Sexfriend_Jerk
            $ RogueX.FaceChange("sexy")
            ch_r "Now, sex friend. . . how would you like to celebrate?"
            if "Historia" in Player.Traits:
                    return 1
    $ Player.AddWord(1,"interruption") #adds to Recent
    $ temp_modifier = 25
    call Rogue_SexMenu
    $ temp_modifier = 0
    return

label Rogue_Sexfriend_Jerk:
    $ RogueX.FaceChange("sad", 1)
    $ RogueX.DailyActions.append("relationship")
    ch_r "Your loss."
    $ RogueX.Statup("Obed", 50, 30)
    if "Historia" not in Player.Traits:
            $ renpy.pop_call()
    if RogueX.Event[9] == 3:
            ch_r "Well, it's not really up to you anyways."
            ch_r "Just let me know if you want a roll in the hay."
            ch_r "I need some alone time though."
            if "Historia" in Player.Traits:
                    return
            $ RogueX.Petnames.append("sex friend")
            $ Achievements.append("Man of Virtue")
            $ bg_current = "bg player"
            $ RogueX.Loc = "bg rogue"
            call Remove_Girl(RogueX)
            jump player_room
    $ Count = (10 * RogueX.Event[9])
    $ RogueX.Statup("Inbt", 200, -Count)
    if bg_current == "bg rogue":
            ch_r "Ok, you can go now."
            $ bg_current = "bg player"
    else:
            ch_r "Ok, I'm out."
            $ RogueX.Loc = "bg rogue"
    if "Historia" in Player.Traits:
            return
    call Remove_Girl(RogueX)
    jump player_room

label Rogue_Fuckbuddy:
    call Shift_Focus(RogueX)
    $ RogueX.DrainWord("asked meet")
    if RogueX in Player.Harem:
            if RogueX.Loc != bg_current and RogueX not in Party:
                    return
            $ RogueX.Petnames.append("fuck buddy")
            $ RogueX.Statup("Inbt", 200, 50)
            "[RogueX.Name] suddenly reaches down and gives your package a little squeeze."
            return

    if RogueX.Loc != bg_current and RogueX not in Party:
            "Suddenly, [RogueX.Name] shows up and says she needs to talk to you."

    $ RogueX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(RogueX)
    call CleartheRoom(RogueX)
    call Taboo_Level
    $ RogueX.FaceChange("bemused", 1)
    ch_r ". . ."
    ch_r "I've been having a lot of fun with this \"sex friend\" thing."
    if "exhibitionist" in RogueX.Traits:
            ch_r "And I've really been getting off on all the stuff we've been doing."
    menu:
        extend ""
        "You bet!":
                $ RogueX.Statup("Love", 200, 20)
                $ RogueX.Statup("Obed", 200, 20)
                $ RogueX.Statup("Inbt", 200, 30)
        "Yeah?":
                $ RogueX.Statup("Love", 200, 10)
                $ RogueX.Statup("Obed", 200, 20)
        "Whatever.":
                $ RogueX.Statup("Love", 200, -10)
                $ RogueX.Statup("Obed", 200, 30)
    ch_r "So, since it's worked so far. . ."
    $ RogueX.Event[10] += 1
    $ RogueX.Petnames.append("fuck buddy")
    if RogueX not in Player.Harem:
            ch_r "I'd like to be full on casual fuck buddies."
            menu:
                extend ""
                "Heh, ok, fuck buddy.":
                        $ RogueX.Statup("Inbt", 200, 100)
                        $ RogueX.Petnames.append("fuck buddy")
                        $ RogueX.ArmPose = 2
                        ch_r "Whoo hoo!"
                        $ RogueX.Over = 0
                        $ RogueX.Chest = 0
                        if "Historia" in Player.Traits:
                                    return 1
                        call first_topless(RogueX, silent = 1)
                        call Rogue_Breasts_Launch
                        "Rogue, throws her top off, grabs you and shoves your head into her cleavage."
                        call Rogue_Pos_Reset
                "What do you mean by that?":
                    $RogueX.Brows = "confused"
                    menu:
                        ch_r "I mean, you know, we'd fuck. And be buddies. Both of those."
                        "Oh, ok, sure.":
                                call Rogue_Kissing_Launch
                                "Rogue laughs and tackles you into a hug."
                                call Rogue_Pos_Reset
                        "Oh, no, not my style.":
                                jump Rogue_Fuckbuddy_Jerk
                "No thanks.":
                    jump Rogue_Fuckbuddy_Jerk
            $ RogueX.FaceChange("sexy")
            ch_r "Now, -heh-, fuck buddy. . . let's make this official!"
    if "Historia" in Player.Traits:
            return 1
    $ temp_modifier = 30
    $ Player.AddWord(1,"interruption") #adds to Recent
    call Rogue_SexMenu
    $ temp_modifier = 0
    return

label Rogue_Fuckbuddy_Jerk:
    $ RogueX.Statup("Obed", 50, 30)
    $ RogueX.FaceChange("bemused", 1)
    if RogueX.Event[10] > 1:
            $ RogueX.ArmPose = 2
            $ RogueX.Over = 0
            $ RogueX.Chest = 0
            ch_r "I offer these things on a silver platter, and nothing!"
            $ RogueX.OutfitChange()
            ch_r "Look, I don't care what you call it. Just let me know if you want a tumble."
            if "Historia" in Player.Traits:
                    return 1
            call first_topless(RogueX, silent = 1)
            $ RogueX.Petnames.append("fuck buddy")
            $ Achievements.append("Stalwart as the mount")
            return
    else:
            ch_r "Too bad."
    if "Historia" in Player.Traits:
            return
    $ renpy.pop_call()
    $ Count = (10*RogueX.Event[10])
    $ RogueX.Statup("Inbt", 200, -Count)
    if bg_current == "bg rogue":
            ch_r "Ok, you can go now."
            $ bg_current = "bg player"
    else:
            ch_r "Ok, I'm out."
            $ RogueX.Loc = "bg rogue"
    call Remove_Girl(RogueX)
    jump player_room
