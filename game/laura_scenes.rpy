label LauraMeet(Topics=[],Loop=1):
    $ ActiveGirls.append(LauraX) if LauraX not in ActiveGirls else ActiveGirls
    $ LauraX.Name = "???"
    $ LauraX.Names.remove("Laura")
    $ LauraX.Names.append("X-23")
    $ bg_current = "bg dangerroom"
    call CleartheRoom("All",0,1)
    $ LauraX.Loc = "bg dangerroom"
    $ LauraX.Love = 400
    $ LauraX.Obed = 0
    $ LauraX.Inbt = 200
    $ LauraX.Lust = 10
    call Shift_Focus(LauraX)
    $ LauraX.sprite_location = StageCenter
    call Set_The_Scene(0)
    $ LauraX.Petname = Player.Name
    $ LauraX.OutfitDay = "casual1"
    $ LauraX.Outfit = "casual1"
    $ LauraX.OutfitChange("casual1")

    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."
    ". . ."
    $ LauraX.FaceChange("normal", 0)
    show Laura_Sprite at sprite_location(LauraX.sprite_location)
    "When you come to, a girl pulls you up by your arm."
    $ LauraX.FaceChange("surprised", 0, Eyes="squint",Brows="sad")
    ch_u "Oh, good, you don't look too damaged."
    $ LauraX.FaceChange("smile", 0, Brows="sad")
    ch_u "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door."
    $ LauraX.FaceChange("smile", 0)
    while Loop:
        menu:
            extend ""
            "Who are you?" if LauraX.Name == "???":
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "I go by \"X-23\" in the field."
                    $ LauraX.Name = "X-23"
            "X-23? Is that your real name?" if LauraX.Name == "X-23" and "X23" not in Topics:
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "It's the one I was born with."
                    $ Topics.append("X23")
            "Is there anything else I could call you?" if "X23" in Topics and LauraX not in Topics:
                    $ LauraX.Statup("Love", 70, 5) # Love
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "I also go by Laura. Laura Kinney."
                    $ LauraX.FaceChange("confused", 0, Mouth="normal")
                    $ LauraX.Name = "Laura"
                    $ LauraX.Names.append("Laura")
                    $ Topics.append(LauraX)
                    menu:
                        extend ""
                        "Nice to meet you Laura.":
                            $ LauraX.Statup("Love", 70, 5) # Love
                            $ LauraX.FaceChange("normal", 0)
                            ch_l "Yeah, ok."
                        "Hello Laura Laura Kinney.":
                            $ LauraX.FaceChange("confused", 0,Mouth="sucking")
                            ch_l "It's just-"
                            $ LauraX.FaceChange("smile", 0,Brows="surprised")
                            $ LauraX.Statup("Love", 70, 3) # Love
                            $ LauraX.Statup("Inbt", 70, 2) # Inbt
                            ch_l "Oh, get it."
                        "Ok, how did you get that name?":
                            $ LauraX.FaceChange("angry", 1,Eyes="side")
                            $ LauraX.Statup("Love", 70, -2) # Love
                            $ LauraX.Statup("Obed", 70, 2) # Obed
                            ch_l "You're getting too personal."
            "I think I'd prefer calling you X-23." if LauraX.Name == LauraX and LauraX in Topics:
                            $ LauraX.Statup("Love", 70, -2) # Love
                            $ LauraX.Statup("Obed", 70, 5) # Obed
                            $ LauraX.FaceChange("sadside", 0,Brows="normal")
                            ch_l "Suit yourself."
                            $ LauraX.Name = "X-23"
            "My name is [Player.Name]" if LauraX.Name != "???" and "player" not in Topics:
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "Ok."
                    $ Topics.append("player")
                    menu:
                        extend ""
                        ". . .and it's nice to meet you?":
                            $ LauraX.Statup("Love", 70, 1) # Love
                            $ LauraX.FaceChange("confused", 0,Mouth="normal")
                            ch_l "Yeah, you too."
                        "So. . .[[moving on]":
                            $ LauraX.Statup("Love", 70, 3) # Love
                            $ LauraX.Statup("Obed", 70, 1) # Obed
                            $ LauraX.Statup("Inbt", 70, 1) # Inbt

            "What are you doing here?" if "Training" not in Topics:
                    $ LauraX.Statup("Obed", 70, -2) # Obed
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "Training. That's the point of this place."
                    $ Topics.append("Training")
                    menu:
                        extend ""
                        "I meant in the school, I haven't seen you around before.":
                                $ LauraX.Statup("Obed", 70, 2) # Obed
                        "Ok, that's fair.":
                                $ LauraX.FaceChange("normal", 0)
                                ch_p "But are you new to this school?"
                                $ LauraX.Statup("Love", 70, 3) # Love
                                $ LauraX.Statup("Obed", 70, 4) # Obed
                    ch_l "I've been here since before your time."
                    ch_l "Mostly out in the field though."
            "So you don't stay here long?" if "Training" in Topics and "Stay" not in Topics:
                    $ LauraX.Statup("Love", 70, 2) # Love
                    $ LauraX.FaceChange("normal", 0,Eyes="side")
                    ch_l "I'll be heading out again soon."
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "But I am planning to stick around after I get back from this mission."
                    $ Topics.append("Stay")


            "What the hell was that?" if len(Topics) <= 1 and "WTF" not in Topics:
                    $ LauraX.Statup("Love", 70, -2) # Love
                    $ LauraX.Statup("Obed", 70, 8) # Obed
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "It was a robot arm."
                    $ LauraX.FaceChange("sad", 1,Eyes="leftside")
                    ch_l "Like I said, sorry."
                    $ LauraX.Statup("Obed", 70, -3) # Obed
                    $ LauraX.Statup("Inbt", 70, 3) # Inbt
                    $ LauraX.FaceChange("smile", 0,Brows="confused")
                    ch_l "You probably should have ducked though."
                    $ Topics.append("WTF")

            "So what's your mutant power?" if LauraX.Name != "???" and "claws" not in Topics:
                    $ LauraX.Statup("Love", 70, 1) # Love
                    $ LauraX.Statup("Obed", 70, 1) # Obed
                    $ LauraX.FaceChange("normal", 0)
                    ch_l "I can heal fast."
                    $ LauraX.ArmPose = 2
                    ch_l "Also I have claws."
                    $ LauraX.Claws = 1
                    $ LauraX.FaceChange("smile", 0,Brows="confused")
                    "snikt"
                    $ Topics.append("claws")
                    menu:
                        "Those claws look pretty sharp.":
                                $ LauraX.Statup("Inbt", 70, 3) # Inbt
                                ch_l "Yeah, indestructible too."
                        "Cool.":
                                $ LauraX.Statup("Love", 70, 3) # Love
                                $ LauraX.Statup("Obed", 70, 2) # Obed
                                $ LauraX.Statup("Inbt", 70, 1) # Inbt
                                $ LauraX.FaceChange("smile", 0,Brows="surprised")
                                ch_l "Yeah, indestructible too."
                        "Ouch.":
                                $ LauraX.Claws = 0
                                $ LauraX.FaceChange("confused", 0)
                                $ LauraX.Statup("Love", 70, -2) # Love
                                $ LauraX.Statup("Obed", 70, -5) # Obed
                                ch_l "Don't worry, I won't stab you."
                                $ LauraX.FaceChange("confused", 0,Mouth="normal")
                                $ LauraX.Statup("Inbt", 70, 7) # Inbt
                                ch_l "Probably."
                    $ LauraX.Claws = 0
                    $ LauraX.ArmPose = 1

            "Don't you want to know my power?" if "claws" in Topics and "powers" not in Topics:
                    if LauraX.Love >= 405:
                            $ LauraX.FaceChange("smile", 0,Brows="confused")
                            ch_l "Yeah, I guess."
                    else:
                            $ LauraX.FaceChange("normal", 0)
                            ch_l "Not really."
                    $ LauraX.Statup("Inbt", 70, 3) # Inbt
                    $ Topics.append("powers")
                    ch_p "I'm immune to mutant powers and can shut them off."
                    $ LauraX.FaceChange("smile", 0,Brows="confused")
                    $ LauraX.Statup("Love", 70, 3) # Love
                    $ LauraX.Statup("Obed", 70, 3) # Obed
                    ch_l "Huh. Interesting. So you can stop me from healing?"
                    ch_p "Yeah. If I touch you, temporarily."
                    $ LauraX.Statup("Obed", 70, 2) # Obed
                    $ LauraX.Statup("Lust", 70, 3) # Lust
                    ch_l "Give it a try."
                    "She holds out her arm, and you grab it."
                    $ LauraX.Statup("Love", 70, 1) # Love
                    $ LauraX.Statup("Obed", 70, 2) # Obed
                    $ LauraX.Statup("Lust", 70, 5) # Lust
                    $ LauraX.FaceChange("confused", 0)
                    ch_l "Huh."
                    $ LauraX.FaceChange("sexy", 1,Eyes="closed")
                    $ LauraX.Addictionrate += 1
                    "You can feel her shudder a little."
                    $ LauraX.FaceChange("sexy", 1)
                    $ LauraX.Statup("Love", 70, 1) # Love
                    $ LauraX.Statup("Obed", 70, 3) # Obed
                    $ LauraX.Statup("Lust", 70, 5) # Lust
                    $ LauraX.Addictionrate += 1
                    ch_l "That feels weird."
                    $ LauraX.FaceChange("sexy", 1,Eyes="leftside")
                    $ LauraX.Statup("Obed", 70, 1) # Obed
                    $ LauraX.Statup("Lust", 70, 3) # Lust
                    $ LauraX.Addictionrate += 1
                    ch_l "-a little more \"alive\" than usual."
                    $ LauraX.Statup("Inbt", 70, 5) # Inbt
                    $ LauraX.Statup("Lust", 70, 5) # Lust
                    $ LauraX.FaceChange("sexy", 1,Brows="confused")
                    $ LauraX.Addictionrate += 1
                    ch_l "Almost. . . dangerous."

            "Never mind that. . . [[moving on]" if LauraX.Name != "???":
                    $ Loop = 0

        if len(Topics) >= 3 and LauraX.Name == "???":
                $ LauraX.Statup("Love", 70, -2) # Love
                $ LauraX.Statup("Obed", 70, 5) # Obed
                $ LauraX.Statup("Inbt", 70, 5) # Inbt
                ch_l "Oh, by the way, you can call me \"X-23\"."
                $ LauraX.Name = "X-23"
        if len(Topics) >= 8:
                $ Loop = 0


    #close while loop
    ch_l "Ok, I've got a plane to catch."
    if "player" in Topics:
            $ LauraX.Statup("Love", 70, 2) # Love
            $ LauraX.Statup("Lust", 70, 1) # Lust
            $ LauraX.FaceChange("smile",0)
            ch_l "Maybe I'll see you when I get back, [Player.Name]."
    else:
            $ LauraX.FaceChange("normal", 0)
            ch_l "Maybe I'll see you when I get back, stranger."
    if "powers" in Topics:
            $ LauraX.Statup("Obed", 70, 2) # Obed
            $ LauraX.Statup("Inbt", 70, 2) # Inbt
            $ LauraX.Statup("Lust", 70, 3) # Lust
            $ LauraX.FaceChange("smile", 1, Brows="confused")
            ch_l "We should. . . spar."

    $ LauraX.Loc = "hold"
    call Set_The_Scene

    "She dashes out of the room, headed for the hangar."

    $ LauraX.PubeC = 3
    $ LauraX.Todo.append("mission")

    $ bg_current = "bg dangerroom"
    $ Round -= 10
    call Shift_Focus(RogueX)
    $ ActiveGirls.remove(LauraX) if LauraX in ActiveGirls else ActiveGirls

    return

label Laura_Cleanhouse:
        # this is triggered if you agree to break up the other girls, but then fail to within the time limit
        $ LauraX.DrainWord("asked meet")
        if "cleanhouse" in LauraX.Todo:
                        $ LauraX.Todo.remove("cleanhouse")
        if not Player.Harem or LauraX in Player.Harem:
                        $ LauraX.Event[5] = 2
                        return

        if LauraX.Loc == bg_current or LauraX in Party:
                "[LauraX.Name] glances over at you with a scowl."
        else:
                "[LauraX.Name] turns a corner and notices you."
        if bg_current != "bg laura" and bg_current != "bg player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg laura"
        $ LauraX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(LauraX)
        call Set_The_Scene
        call Taboo_Level
        $ LauraX.DailyActions.append("relationship")
        $ LauraX.Statup("Love", 200, -20)
        $ LauraX.FaceChange("angry",1)
        ch_l "What's the deal, [Player.Petname]?"
        ch_l "It's been a week already, and you're still dating [Player.Harem[0].Name]!"
        if len(Player.Harem) >= 2:
                ch_l "Not to mention the rest of them!"
        menu:
            extend ""
            "Sorry about that, I'm sticking with them":
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 80, 5)
                    $ LauraX.FaceChange("angry",2)
                    ch_l "You asshole."
                    $ LauraX.FaceChange("sadside",1)
                    ch_l "You could have at least been honest about it."
            "Must have slipped my mind":
                    $ LauraX.Statup("Love", 200, -10)
                    $ LauraX.Statup("Obed", 80, 10)
                    ch_l "!"
                    ch_l "Seriously dude? That's all you've got?"
            "[[shrug]":
                    $ LauraX.Statup("Love", 200, -20)
                    $ LauraX.Statup("Obed", 80, 10)
                    $ LauraX.Statup("Inbt", 80, 10)
                    $ LauraX.Blush = 2
                    show Laura_Sprite with vpunch
                    "She clocks you one."
                    "That was fair."
                    $ LauraX.Blush = 1

        ch_l "I can't believe you're putting me through this."
        ch_l "Making me choose between you and putting up with this whole arrangement."
        $ Line = 0
        if ApprovalCheck(LauraX, 1400) and ApprovalCheck(LauraX, 600,"O"):
                #if she's very obedient. . .
                pass
        elif ApprovalCheck(LauraX, 1200) and ApprovalCheck(LauraX, 500,"O"):
                #second chance on if she likes you well enough. . .
                $ BO = Player.Harem[:]
                while BO and Line != "no":
                    # Spits out a "no" if she doesn't like another girl
                    if LauraX.GirlLikeCheck(BO[0]) <= 400:
                            $ Line = "no"
                    $ BO.remove(BO[0])
        else:
                $ Line = "no"
        if Line == "no":
                $ LauraX.Statup("Love", 200, -10)
                $ LauraX.Statup("Obed", 80, 10)
                $ LauraX.FaceChange("angry",1)
                call HaremStatup(LauraX,700,-15) #lowers like of all Harem girls by 15
                ch_l "No, this is bullshit, never mind."
        else:
                $ LauraX.Statup("Love", 200, 5)
                $ LauraX.Statup("Obed", 80, 20)
                $ LauraX.Statup("Inbt", 80, 10)
                $ LauraX.FaceChange("angry",1,Eyes="side")
                ch_l "Ok, fine, whatever. I'm in too."
                if "Historia" not in Player.Traits:
                        $ Player.Harem.append(LauraX)
                        if "LauraYes" in Player.Traits:
                                $ Player.Traits.remove("LauraYes")
                        $ LauraX.Petnames.append("boyfriend")
                        call Harem_Initiation
                        call HaremStatup(LauraX,900,20) #raises like of all Harem girls by 20
                        $ LauraX.Event[5] = 20
        return

label Laura_Love(Shipping=[],Shipshape=0,Topics=[],BO=[]):
        # SHipping is used to track who else you're involved with
        # if LauraX.Event[6] = 5, then it cleared
        # if LauraX.Event[6] = 20, then it broke because you didn't love her
        # if LauraX.Event[6] = 23, then it broke because you pissed her off
        # if LauraX.Event[6] = 25, then it broke and you already went through the redux

        $ LauraX.DrainWord("asked meet")
        $ BO = TotalGirls[:]
        $ BO.remove(LauraX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        if LauraX.Loc == bg_current or LauraX in Party:
                "[LauraX.Name] glances over at you with a concerned look."
        else:
                "[LauraX.Name] turns a corner and notices you."
        if bg_current != "bg laura" and bg_current != "bg player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg laura"
        $ LauraX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(LauraX)
        call Set_The_Scene
        call Taboo_Level
        $ LauraX.DailyActions.append("relationship")
        $ LauraX.FaceChange("sad",1)
        ch_l "Hey, so, I like what this is. . ."
        ch_l "-what we have. . ."
        $ LauraX.FaceChange("sadside",1)
        ch_l "It's been kind of hard for me to open up to people. . ."
        ch_l "I've been betrayed a lot out there."
        menu:
            extend ""
            "I would never betray you.":
                    $ LauraX.FaceChange("bemused",1)
                    $ LauraX.Statup("Love", 200, 10)
                    $ LauraX.Statup("Obed", 70, 5)
                    $ LauraX.Statup("Inbt", 60, 5)
                    ch_l "I. . . know that now."
            "I'm sorry to hear that.":
                    $ LauraX.FaceChange("sadside",1,Mouth="smile")
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.Statup("Obed", 90, -5)
                    $ LauraX.Statup("Inbt", 60, 10)
                    ch_l ". . ."
                    $ LauraX.FaceChange("smile",1)
                    ch_l "Thank you. . ."
            "That must be rough.":
                    $ LauraX.FaceChange("sadside",1,Mouth="normal")
                    $ LauraX.Statup("Love", 200, 5)
                    ch_l ". . ."
                    $ LauraX.FaceChange("smile",1)
                    ch_l "It was. . ."
            "Wow, that sucks.":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 90, 10)
                    $ LauraX.Statup("Inbt", 90, -5)
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry",1,Eyes="side")
                    ch_l "Right, so. . ."
        ch_l "I didn't always have it as easy as I've had it here."
        $ LauraX.Eyes = "normal"
        ch_l "I only thought it fair to tell you a little about that history."
        $ Line = 0
        while len(Topics) < 9 and "exit" not in Topics:
                #Lines are topics of current discussion. "Topics" catalogues things alrewady discussed

                if Line == "facility":
                        menu:
                            extend ""
                            "How many people did you kill?" if "kills" not in Topics:
                                    $ LauraX.FaceChange("angry",0,Eyes="side")
                                    ch_l "Dozens. Maybe more. At least 13 primary targets."
                                    ch_l "Too many \"collaterals.\""
                                    $ Topics.append("kills")
                            "Did you ever fail a mission?" if "fail" not in Topics:
                                    $ LauraX.FaceChange("angry",0,Eyes="side",Brows="normal")
                                    ch_l "Once or twice."
                                    ch_l "Sometimes they managed to get away."
                                    ch_l "I'm not proud of who I was back then, but even then. . ."
                                    $ LauraX.Mouth = "smile"
                                    ch_l ". . . a part of me was happy when they did."
                                    $ Topics.append("fail")
                            "Did anyone take care of you?" if "mother" not in Topics:
                                    $ LauraX.FaceChange("smile",0)
                                    ch_l "My mother, Sarah Kinney."
                                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ Line = "mother"
                            "How did you escape?" if "escape" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "Mother."
                                    ch_l "She got me out, found me an escape route."
                                    ch_l "It was the last thing she did."
                                    $ Topics.append("escape")
                                    $ Line = "mother"
                            "I'd like to know more about what came after.":
                                    $ Line = "NYX"
                            "Enough about that though. . .":
                                    $ Line = 0

                # end facility questions

                if Line == "mother":
                        menu:
                            extend ""
                            "Who was your mother?" if "mother" not in Topics:
                                    $ LauraX.FaceChange("smile",0)
                                    ch_l "Her name was Sarah Kinney."
                                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ Line = "mother"
                            "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:
                                    $ LauraX.FaceChange("sad",0,Eyes="surprised")
                                    ch_l "I didn't want to, but the Trigger scent made me. . ."
                                    $ LauraX.FaceChange("sadside",0)
                                    if "trigger" in LauraX.History:
                                            ch_l "I've mentioned that to you before. . ."
                                    else:
                                            $ LauraX.History.append("trigger")
                                    ch_l ". . . it can make me kill, even if I don't want to."
                                    $ Topics.append("killed")
                            "It wasn't your fault." if "killed" in Topics:
                                    $ LauraX.Statup("Love", 200, 5)
                                    $ LauraX.Statup("Obed", 70, 5)
                                    $ LauraX.Statup("Inbt", 70, 5)
                                    $ LauraX.FaceChange("sad",0)
                                    ch_l "Not completely, no."
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "But my hands aren't clean."
                                    $ Line = "facility"
                            "That must have been horrible." if "killed" in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    $ LauraX.Statup("Love", 200, 5)
                                    $ LauraX.Statup("Obed", 90, 5)
                                    ch_l "It's taken me some time. . ."
                                    $ LauraX.FaceChange("normal",0)
                                    ch_l "but I think I'm ok with it now."
                                    $ Line = "facility"
                            "Bummer." if "killed" in Topics:
                                    $ LauraX.FaceChange("angry",1)
                                    $ LauraX.Statup("Love", 200, -10)
                                    $ LauraX.Statup("Obed", 90, 5)
                                    ch_l "Are you seriously making fun of my mother's death?!"
                                    $ Topics.append("exit")
                                    $ Line = "angry"
                # end questions about mother

                if Line == "NYX":
                        menu:
                            extend ""
                            "What did you do for a living?" if "living" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "There wasn't much I could do at the time, I mostly just scrounged for food."
                                    ch_l "You can get by on some pretty awful stuff if you have a healing factor."
                                    $ LauraX.FaceChange("bemused",1,Brows="sad")
                                    ch_l "I also did some. . . shady stuff."
                                    $ Topics.append("living")

                            "Was it sexual?" if "work" not in Topics and "living" in Topics:
                                    $ LauraX.FaceChange("sadside",2)
                                    $ LauraX.Statup("Obed", 90, 5)
                                    $ LauraX.Statup("Inbt", 90, 10)
                                    ch_l ". . ."
                                    $ LauraX.Blush = 1
                                    ch_l "A little."
                                    $ Line = "work"
                                    $ Topics.append("work")

                            "Did you hurt people?" if "work" not in Topics and "living" in Topics:
                                    $ LauraX.FaceChange("surprised",0,Eyes="normal")
                                    ch_l "No, definitely not."
                                    ch_l "After the facility, I just couldn't take that sort of work anymore."
                                    $ LauraX.FaceChange("bemused",0)
                                    ch_l "I avoided hurting anyone."
                                    $ LauraX.FaceChange("sadside",2)
                                    ch_l "It tended to be more. . . sexual work."
                                    $ Line = "work"
                                    $ Topics.append("work")

                            "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:
                                    $ LauraX.FaceChange("bemused",0)
                                    ch_l "Yeah, eventually."
                                    ch_l "I'd seen Wolverine on the news, and thought maybe he had some answers."
                                    ch_l "He's not around much though."
                                    $ Topics.append("xaviers")
                                    $ Line = 0
                            "Good thing you made it here. [[exit]" if "xaviers" in Topics:
                                    $ LauraX.FaceChange("smile",0)
                                    ch_l "Yeah."
                                    $ Line = 0

                if Line == "work":
                        $ LauraX.FaceChange("sadside",0,Mouth="normal")
                        ch_l "It was mostly the rougher customers."
                        ch_l "The ones who couldn't control their tempers."
                        $ LauraX.FaceChange("angry",0,Mouth="smile")
                        ch_l "Better for the girl who can heal to take the hits, right?"
                        menu:
                                extend ""
                                "That's terrible. I wish I could have protected you.":
                                        $ LauraX.FaceChange("smile",1)
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 90, 5)
                                        $ LauraX.Statup("Inbt", 90, -5)
                                        ch_l "Thanks, but I was ok."
                                        $ LauraX.FaceChange("sadside",0)
                                        ch_l "I didn't deserve it, but I felt like I did at the time."
                                "You're strong to have made it out of there.":
                                        $ LauraX.FaceChange("smile",0)
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 90, 10)
                                        $ LauraX.Statup("Inbt", 90, 5)
                                        ch_l "Thanks."
                                        ch_l "I didn't really think of it like that. . ."
                                        $ LauraX.FaceChange("sadside",0)
                                        ch_l "I just felt like I'd deserved it."
                                        ch_l "But I realized how wrong that was."
                                "Yeah, that makes sense.":
                                        $ LauraX.FaceChange("confused",1)
                                        $ LauraX.Statup("Love", 200, -5)
                                        $ LauraX.Statup("Obed", 90, 15)
                                        $ LauraX.Statup("Inbt", 90, -5)
                                        ch_l "Don't think before you speak, do you?"
                                        $ LauraX.FaceChange("sadside",0)
                                        ch_l "It wasn't right, I just didn't realize it at the time."
                        ch_l "Eventually I got past it and decided to get out of there."
                        ch_l "Not like they could stop me."
                        $ Line = "NYX"

                if not Line:
                        # Primary menu, falls through to this
                        menu:
                            extend ""
                            "What did you do back at the facility?" if "facility" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "After they tested what I could do, they put me to work."
                                    ch_l "Mainly, I killed people for them."
                                    $ Topics.append("facility")
                                    $ Line = "facility"
                            "More about that facility. . ." if "facility" in Topics:
                                    $ Line = "facility"

                            "Where did you go after you escaped?" if "NYX" not in Topics:
                                    $ LauraX.FaceChange("sadside",0)
                                    ch_l "I wandered in the wilderness for weeks."
                                    ch_l "Eventually I found my way to New York."
                                    ch_l "I lived on the streets for a few years."
                                    $ Topics.append("NYX")
                                    $ Line = "NYX"
                            "More about after the escape. . ." if "NYX" in Topics:
                                    $ Line = "NYX"

                            "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:
                                    $ LauraX.FaceChange("smile",0)
                                    $ LauraX.Statup("Love", 200, 10)
                                    $ LauraX.Statup("Obed", 90, 3)
                                    $ LauraX.Statup("Inbt", 90, 3)
                                    ch_l "Thanks for listening to me ramble."
                                    $ Topics.append("exit")
                            "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:
                                    $ LauraX.FaceChange("sadside",0, Mouth="smile")
                                    $ LauraX.Statup("Obed", 90, 10)
                                    ch_l "Yeah, you get the idea."
                                    $ Topics.append("exit")
                            "I don't really care about that. [[exit]":
                                    $ LauraX.FaceChange("angry",0)
                                    $ LauraX.Statup("Love", 200, -15)
                                    $ LauraX.Statup("Obed", 50, 5)
                                    $ LauraX.Statup("Obed", 90, 10)
                                    $ LauraX.Statup("Inbt", 90, -5)
                                    ch_l "Oh, I'm sorry if I was boring you with my life story."
                                    $ Line = "angry"
                                    $ Topics.append("exit")

        #end while loop

        if Line == "angry":
                $ LauraX.FaceChange("angry",0)
                ch_l "And here I was thinking that I meant something to you."
                ch_l "Well forget that!"
                $ Line = 0
                $ LauraX.Event[6] = 23
                $ LauraX.RecentActions.append("angry")
                $ LauraX.DailyActions.append("angry")
                hide Laura_Sprite with easeoutright
                call Remove_Girl(LauraX)
                $ LauraX.Loc = "hold" #puts her off the board for the day
                return

        $ LauraX.FaceChange("bemused",0,Eyes="down")
        ch_l "I just thought you should know,"
        $ LauraX.FaceChange("smile",2)
        ch_l "I love you."
        menu:
                extend ""
                "I love you too!":
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.Statup("Love", 200, 20)
                    $ LauraX.Statup("Inbt", 90, 5)
                    ch_l "For a second there you had me worried."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_Love_End
                "I know.":
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.Statup("Love", 200, 10)
                    $ LauraX.Statup("Obed", 90, 5)
                    $ LauraX.Statup("Inbt", 90, 10)
                    $ LauraX.Statup("Lust", 90, 5)
                    ch_l "Smooth one. Seriously though, how about you?"
                "Neat?":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Obed", 90, 5)
                    ch_l "I'm gonna need a bit more there, [LauraX.Petname]."
                "Huh.":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 90, 10)
                    ch_l "I'm not sure how to take that one."


        menu:
                extend ""
                "Oh, I love you too!":
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.Statup("Love", 200, 15)
                    $ LauraX.Statup("Obed", 90, 5)
                    $ LauraX.Statup("Inbt", 90, 5)
                    ch_l "For a second there you had me worried."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_Love_End
                "I. . . love you back?":
                    $ LauraX.FaceChange("confused",1)
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.Statup("Obed", 90, 10)
                    ch_l "Ok, I'll take it."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_Love_End
                "I mean, that's cool and all. . .":
                    $ LauraX.FaceChange("sadside",1)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 90, 10)
                    $ LauraX.Statup("Inbt", 90, -5)
                    ch_l ". . . but you don't love me back. Got it."
                "That's. . . uncomfortable.":
                    $ LauraX.FaceChange("angry",1)
                    $ LauraX.Statup("Love", 200, -10)
                    $ LauraX.Statup("Obed", 90, 15)
                    $ LauraX.Statup("Inbt", 90, -5)
                    ch_l "I don't like where this is heading."

        ch_l "What's your problem?"
        ch_l "Is it someone else?"
        $ Line = 0
        menu:
                extend ""
                "Yes, it's [RogueX.Name]." if RogueX in Shipping and Shipshape < 3:
                        $ Line = RogueX
                "Yes, it's [KittyX.Name]." if KittyX in Shipping and Shipshape < 3:
                        $ Line = KittyX
                "Yes, it's [EmmaX.Name]." if EmmaX in Shipping and Shipshape < 3:
                        $ Line = EmmaX
                "Yes, it's the others" if Shipshape > 1:
                        $ LauraX.Statup("Obed", 90, 15)
                        $ LauraX.Statup("Inbt", 90, 5)
                        $ LauraX.Statup("Lust", 90, 5)
                        $ LauraX.FaceChange("sadside",1)
                        ch_l "Well, you do have your pick."
                "There's nobody else.":
                        $ LauraX.Statup("Love", 200, -15)
                        $ LauraX.Statup("Obed", 90, 15)
                        $ LauraX.Statup("Inbt", 90, 5)
                        $ LauraX.FaceChange("sad",1)
                        if ApprovalCheck(LauraX, 1000, "OI"):
                            ch_l "I guess that's something."
                        else:
                            ch_l ". . ."
                "It's a \"you\" problem.":
                        $ LauraX.FaceChange("angry")
                        $ LauraX.Statup("Love", 200, -25)
                        $ LauraX.Statup("Obed", 90, 15)
                        ch_l "You're seriously messing with me?"
                        $ LauraX.Statup("Love", 200, -10)
                        ch_l "You don't want to see me when I'm angry."
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.DailyActions.append("angry")


        if Line:
                #If you called out a girl,
                if LauraX.GirlLikeCheck(Line) >= 800:
                        $ LauraX.Statup("Love", 200, 5)
                        $ LauraX.Statup("Obed", 90, 20)
                        $ LauraX.Statup("Inbt", 90, 5)
                        $ LauraX.Statup("Lust", 90, 5)
                        $ LauraX.FaceChange("sadside",1)
                        ch_l "Yeah, I guess she's great."
                else:
                        $ LauraX.FaceChange("angry",Eyes="side")
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 90, 20)
                        ch_l "Bitch."
                        $ LauraX.RecentActions.append("angry")
                        $ LauraX.GLG(Line,800,-50,1)
        ch_l "Well, if that's the way you feel about it. . ."
        ch_l "I'll. . . see you later."
        ch_l "This. . . hurt."

label Laura_Love_End:
        if "lover" not in LauraX.Petnames:
                $ LauraX.Event[6] = 20
                hide Laura_Sprite with easeoutright
                call Remove_Girl(LauraX)
                $ LauraX.Loc = "hold" #puts her off the board for the day
                return

        $ LauraX.Event[6] = 5
        "[LauraX.Name] grabs you in a crushing hug."
        $ LauraX.Statup("Love", 200, 25)
        $ LauraX.Statup("Lust", 90, 5)
        $ LauraX.FaceChange("sly",1)
        ch_l "So. . . now that we have some free time. . ."
        $ LauraX.Statup("Lust", 90, 10)

        if not LauraX.Sex:
            $ LauraX.FaceChange("bemused",2)
            ch_l "I think I'm ready. . ."
        else:
            ch_l "Would you like to have some fun?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Yeah, let's do this. . . [[have sex]":
                    $ LauraX.Statup("Inbt", 30, 20)
                    $ LauraX.Statup("Obed", 70, 10)
                    ch_l "Hmm. . ."
                    call Laura_SexAct("sex")
                "I have something else in mind. . .[[choose another activity]":
                    $ LauraX.Brows = "confused"
                    $ LauraX.Statup("Obed", 70, 25)
                    ch_l "Like what? . ."
                    $ temp_modifier = 20
                    call Laura_SexMenu
        return

label Laura_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ LauraX.DailyActions.append("relationship")

        if LauraX.Event[6] >= 25:
                #if this is the second time through
                ch_p "I hope you've forgiven me, I still love you."
                $ LauraX.Statup("Love", 95, 10)
                if ApprovalCheck(LauraX, 950, "L"):
                    $ Line = "love"
                else:
                    $ LauraX.FaceChange("angry")
                    ch_l "You're still working your way out of the hole, [LauraX.Petname]."
                    $ LauraX.Eyes="side"
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry",Mouth="lipbite")
                    ch_l "But let me hear your pitch."
        elif LauraX.Event[6] >= 23:
                #if you pissed her off the first time
                ch_p "I was rude when you opened up to me before."
                $ LauraX.Statup("Love", 95, 10)
                if ApprovalCheck(LauraX, 950, "L"):
                    ch_l "And. . ."
                else:
                    $ LauraX.FaceChange("angry")
                    ch_l "You're still working your way out of the hole, [LauraX.Petname]."
                    $ LauraX.Eyes="side"
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry",Mouth="lipbite")
                    ch_l "But let me hear your pitch."
        else:
                    ch_p "Remember when I told you that I didn't love you?"
                    $ LauraX.FaceChange("perplexed",1)
                    ch_l ". . ."
                    $ LauraX.FaceChange("angry", Eyes="side")
                    ch_l "How could I forget?"

        if Line != "love":
                menu:
                    extend ""
                    "I'm sorry, I didn't mean it.":
                        $ LauraX.Eyes = "surprised"
                        ch_l "Oh really?"
                        ch_l "That's awfully convenient."
                        ch_p "Yeah. I mean, yes, I love you, [LauraX.Name]."
                        $ LauraX.Statup("Love", 200, 10)
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ Line = "love"
                        else:
                            $ LauraX.FaceChange("sadside")
                            ch_l "Well, maybe I don't, anymore. . ."
                    "I've changed my mind, I do love you, so. . .":
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ Line = "love"
                            ch_l "Well that's great."
                        else:
                            $ LauraX.Mouth = "sad"
                            ch_l "Good for you."
                            $ LauraX.Statup("Inbt", 90, 10)
                            $ LauraX.FaceChange("sadside")
                            ch_l "I don't exactly have the same mind either. . ."
                    "Um, never mind.":
                            $ LauraX.Statup("Love", 200, -30)
                            $ LauraX.Statup("Obed", 50, 10)
                            $ LauraX.FaceChange("angry")
                            ch_l "Oh, fuck you."
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")
        if Line == "love":
                $ LauraX.Statup("Love", 200, 40)
                $ LauraX.Statup("Obed", 90, 10)
                $ LauraX.Statup("Inbt", 90, 10)
                $ LauraX.FaceChange("smile")
                ch_l "I'm glad you came around."
                ch_l "I love you too, [LauraX.Petname]!"
                if LauraX.Event[6] < 25:
                        $ LauraX.FaceChange("sly")
                        "She grabs the back of your head and pulls you close."
                        ch_l "Next time, don't keep me waiting."
                $ LauraX.Petnames.append("lover")
        $ LauraX.Event[6] = 25
        return

label Laura_Sub:
    $ LauraX.DrainWord("asked meet")
    call Shift_Focus(LauraX)
    if LauraX.Loc != bg_current and LauraX not in Party:
        "Suddenly, [LauraX.Name] shows up and says she needs to talk to you."

    $ LauraX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(LauraX)
    call CleartheRoom(LauraX)
    call Set_The_Scene
    call Taboo_Level
    $ LauraX.DailyActions.append("relationship")
    $ LauraX.FaceChange("bemused", 1)

    $ Line = 0
    ch_l "I've noticed something."
    ch_l "You've been trying to boss me around lately."
    menu:
        ch_l "I've noticed you trying to boss me around.{w=2.8}{nw}"
        "I guess. That's just kind of what comes naturally for me.":
                pass
        "Sorry. I didn't mean to come off like that.":
                pass
        "Yup. Deal with it.":
                pass
    "Before you can speak, she puts her hand over your mouth."
    $ LauraX.FaceChange("sly", 1,Eyes="side")
    ch_l "I don't know how I feel about that."
    if LauraX.Event[6]: #if you've done the Love route
            $ LauraX.FaceChange("sadside", 1)
            ch_l "You know the past I've had, with the facility, with the. . . "
            ch_l ". . . work I had to do for them."
            $ LauraX.FaceChange("sad", 1)
            ch_l "I don't know if I want to let anyone tell me what to do like that again."
    menu Laura_Sub_Question:
        extend ""
        "I guess I can be demanding.":
                $ LauraX.FaceChange("sly", 1)
                $ LauraX.Statup("Obed", 200, 10)
                $ LauraX.Statup("Inbt", 50, 5)
        "Sorry. I didn't mean to come off like that.":
                $ LauraX.FaceChange("sly", 1)
                $ LauraX.Statup("Love", 80, 5)
                $ LauraX.Statup("Obed", 200, -5)
                $ LauraX.Statup("Inbt", 50, -5)
                ch_l "I get it, you're assertive. . ."
        "Remind me about the facility?" if LauraX.Event[6] and Line != "facility":
                $ LauraX.FaceChange("sadside", 1)
                $ LauraX.Statup("Love", 99, -10)
                $ LauraX.Statup("Inbt", 50, -5)
                ch_l "I told you, I was raised in an underground government lab."
                ch_l "They ordered me to kill people for them."
                $ LauraX.FaceChange("sly", 0, Brows= "angry")
                ch_l ". . . until I got tired of taking orders."
                $ Line = "facility"
                jump Laura_Sub_Question
        "What bothers you about being told to do things?" if not LauraX.Event[6] and Line != "facility":
                $ LauraX.FaceChange("sadside", 1)
                $ LauraX.Statup("Love", 80, 5)
                ch_l "I've just had some rough experiences."
                ch_l "You don't need to know about them."
                ch_l ". . ."
                $ LauraX.FaceChange("sad", 0)
                ch_l "Let's just say I was ordered to do some things I regret."
                $ Line = "facility"
                jump Laura_Sub_Question
        "Get with the program.":
                if ApprovalCheck(LauraX, 1000, "LO"):
                        $ LauraX.FaceChange("sly", 1)
                        $ LauraX.Statup("Obed", 200, 20)
                        $ LauraX.Statup("Inbt", 50, 10)
                        ch_l "Hmmm. . ."
                else:
                        $ LauraX.Statup("Love", 200, -10)
                        $ LauraX.Statup("Inbt", 50, -5)
                        $ LauraX.FaceChange("angry",0)
                        ch_l "You're not off to a good start here. You might want to rethink your attitude."
                        menu:
                            extend ""
                            "Sorry.  I thought that's what you were into.":
                                    $ LauraX.FaceChange("perplexed", 1,Eyes="side")
                                    $ LauraX.Eyes = "side"
                                    $ LauraX.Statup("Love", 75, 10)
                                    $ LauraX.Statup("Obed", 200, 5)
                                    $ LauraX.Statup("Inbt", 50, 5)
                                    ch_l ". . . after I just said. . ."
                                    $ LauraX.FaceChange("sly", 1)
                                    ch_l "Ok, whatever."
                            "I don't care.":
                                    $ LauraX.Statup("Love", 95, -10)
                                    ch_l "I guess not."
                                    $ Line = "rude"
    if Line == "facility":
            $ Line = 0

    if not Line:
            # She's advancing to the next stage
            $ LauraX.FaceChange("sly", 1)
            ch_l "Look, it's not like. . ."
            $ LauraX.FaceChange("sly", 2)
            ch_l ". . . it's not like I hate it."
            $ LauraX.FaceChange("smile", 1, Eyes="side")
            ch_l ". . . I actually think it might make me. . ."
            menu:
                extend ""
                "-excited?":
                    $ LauraX.Statup("Obed", 200, 5)
                    $ LauraX.Statup("Inbt", 50, 5)
                    ch_l ". . ."
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Lust", 50, 10)
                    ch_l "a little, yeah."
                "-digusted?":
                    $ LauraX.Statup("Love", 75, -5)
                    $ LauraX.Statup("Obed", 200, -5)
                    $ LauraX.FaceChange("sadside", 1)
                    ch_l ". . . kind of,"
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Inbt", 70, 5)
                    $ LauraX.Statup("Lust", 50, 5)
                    ch_l "but also kind of excited by it."
                "-hungry?":
                    $ LauraX.FaceChange("confused", 1,Eyes="surprised",Mouth="smile")
                    $ LauraX.Statup("Obed", 200, -5)
                    $ LauraX.Statup("Inbt", 50, -5)
                    ch_l "?!"
                    $ LauraX.FaceChange("confused", 1,Eyes="normal",Mouth="smile")
                    ch_l "Well. . . yeah? But not for-"
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Lust", 50, 5)
                    ch_l "I mean, it makes me kind of. . . excited."
                "-horny?":
                    $ LauraX.Statup("Obed", 200, 10)
                    $ LauraX.Statup("Inbt", 50, 5)
                    $ LauraX.FaceChange("startled", 2,Mouth="lipbite")
                    ch_l "!"
                    $ LauraX.FaceChange("sly", 1, Eyes="side")
                    $ LauraX.Statup("Inbt", 50, 5)
                    $ LauraX.Statup("Lust", 50, 10)
                    $ LauraX.Statup("Lust", 70, 5)
                    ch_l "Yes."
            menu:
                extend ""
                "Good. If you wanna be with me, then you follow my orders.":
                        if ApprovalCheck(LauraX, 1000, "LO"):
                            $ LauraX.FaceChange("sly", 1)
                            $ LauraX.Statup("Obed", 200, 15)
                            $ LauraX.Statup("Inbt", 50, 10)
                            ch_l "Hmmm. . ."
                        else:
                            $ LauraX.FaceChange("sadside", 1,Mouth="normal")
                            $ LauraX.Statup("Love", 200, -5)
                            $ LauraX.Statup("Obed", 200, 10)
                            ch_l "You might want to slow your roll there, [LauraX.Petname]."
                            menu:
                                extend ""
                                "Whatever. That's how it is. Take it or leave it.":
                                        $ LauraX.FaceChange("angry")
                                        $ LauraX.Statup("Love", 200, -10)
                                        $ LauraX.Statup("Obed", 200, 5)
                                        ch_l "I think you're pushing it too far there, [LauraX.Petname]."
                                        $ Line = "rude"
                                "Ok, just a little." :
                                        $ LauraX.FaceChange("bemused", 1)
                                        $ LauraX.Statup("Love", 95, 5)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        ch_l "-but not too much."

                "Yeah? You think it's sexy?":
                                        $ LauraX.FaceChange("bemused", 2,Eyes="side")
                                        $ LauraX.Statup("Obed", 200, 5)
                                        $ LauraX.Statup("Inbt", 50, 10)
                                        ch_l ". . ."
                                        $ LauraX.Statup("Lust", 50, 5)
                                        ch_l "Yeah."

                "You sure you don't want me to back off a little?":
                        $ LauraX.FaceChange("startled", 1,Eyes="squint")
                        $ LauraX.Statup("Obed", 200, -5)
                        menu:
                            ch_l "Well if you have to ask. . ."
                            "Only if you're okay with it.":
                                $ LauraX.FaceChange("bemused", 1)
                                $ LauraX.Statup("Love", 95, 10)
                                $ LauraX.Statup("Inbt", 50, 10)
                                $ Line = 0
                            "Uhm. . .yeah. I think it's weird.  Sorry.":
                                $ LauraX.FaceChange("sad", 1, Eyes="surprised")
                                $ LauraX.Statup("Love", 200, -15)
                                $ LauraX.Statup("Obed", 200, -5)
                                $ LauraX.Statup("Inbt", 50, -10)
                                $ Line = "embarrassed"

                "I couldn't care less.":
                                $ LauraX.Statup("Love", 200, -10)
                                $ LauraX.Statup("Obed", 200, 15)
                                $ LauraX.FaceChange("angry")
                                ch_l "I think you're pushing it too far there, [LauraX.Petname]."
                                $ Line = "rude"

    if not Line:
        $ LauraX.FaceChange("bemused", 1,Eyes = "down")
        ch_l "So, I'm willing to give this a shot."
        ch_l "Just a trial period, to see how it goes."
        ch_l "Just tell me what you want, and. . . I'll see about doing it."
        menu Laura_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                    $ LauraX.Statup("Obed", 200, 5)
                    $ LauraX.Statup("Inbt", 50, 5)
                    $ LauraX.FaceChange("sly", 1)
                    $ Line = 0
            "Don't you think that relationship's kinda. . .weird?":
                    $ LauraX.FaceChange("sad", 1, Eyes="surprised")
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Inbt", 50, -15)
                    $ Line = "embarrassed"

    if not Line:
        $ LauraX.FaceChange("smile", 1)
        ch_l "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ LauraX.Statup("Love", 95, 5)
                    $ LauraX.Statup("Obed", 200, 15)
                    $ LauraX.Statup("Inbt", 50, 5)
                    ch_l "Yes, sir."
                    $ LauraX.Petname = "sir"
            "That's kind of formal, isn't it?":
                $ LauraX.FaceChange("perplexed", 1)
                ch_l "Huh. ok, no problem"
                $ LauraX.Statup("Inbt", 50, -5)
                $ LauraX.FaceChange("sly", 1,Eyes="side")
                menu:
                    ch_l "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                            $ LauraX.Statup("Obed", 200, 10)
                            $ LauraX.FaceChange("smile", 1)
                            ch_l "Good."
                    "I don't feel comfortable with that. . .":
                            $ LauraX.FaceChange("sad", 1, Eyes="side")
                            $ LauraX.Statup("Love", 200, -10)
                            $ LauraX.Statup("Obed", 200, -30)
                            $ LauraX.Statup("Inbt", 50, -15)
                            $Line = "embarrassed"

    $ LauraX.History.append("sir")
    if not Line:
            $ LauraX.Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] knocks her way past you and storms off."
    elif Line == "embarrassed":
            $ LauraX.FaceChange("sadside", 2)
            ch_l "Huh, ok, if you're not interested. . .."
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] heads out of the room."
    return

label Laura_Sub_Asked:
    $ Line = 0
    $ LauraX.FaceChange("sadside", 1)
    ch_l "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in LauraX.Petnames and ApprovalCheck(LauraX, 850, "O"):
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck(LauraX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        $ LauraX.FaceChange("angry", 1)
                        ch_l "It was a bad idea, don't worry about it." #Failed again. :(
                        $ Line = "rude"

                if Line != "rude":
                        $ LauraX.Statup("Love", 90, 10)
                        $ LauraX.FaceChange("sly", 1)
                        ch_l "Well, it's not like you stopped ordering me around anyway."
                        ch_l "Ok, let's give it a shot."

        "I know it's what you want. Do you want to try again, or not?":
                $ LauraX.FaceChange("bemused", 1)
                if "sir" in LauraX.Petnames:
                    if ApprovalCheck(LauraX, 850, "O"):
                        ch_l "Ok, fine."
                    else:
                        ch_l "Nah, I'm good."
                        $ Line = "rude"
                elif ApprovalCheck(LauraX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ LauraX.FaceChange("confused", 1)
                        ch_l "Kinda wishy-washy there."
                        $ LauraX.FaceChange("sly", 1)
                        ch_l "but maybe you're right."
                        ch_l "Are you sure you're into this?"
                        menu:
                            extend ""
                            "Yes, I'm sorry I was mean about it.":
                                            $ LauraX.Statup("Love", 90, 15)
                                            $ LauraX.Statup("Inbt", 50, 10)
                                            $ LauraX.FaceChange("bemused", 1)
                                            $ LauraX.Eyes = "side"
                                            ch_l "Ok then."
                            "You're damned right I am, bitch.":
                                    if "sir" in LauraX.Petnames and ApprovalCheck(LauraX, 900, "O"):
                                            $ LauraX.Statup("Love", 200, -5)
                                            $ LauraX.Statup("Obed", 200, 10)
                                            ch_l ". . ."
                                    elif ApprovalCheck(LauraX,700, "O"):
                                            $ LauraX.Statup("Love", 200, -5)
                                            $ LauraX.Statup("Obed", 200, 10)
                                            ch_l "Hmmm. . ."
                                    else: #if it failed both those things,
                                            $ LauraX.Statup("Love", 200, -10)
                                            $ LauraX.Statup("Obed", 90, -10)
                                            $ LauraX.Statup("Obed", 200, -10)
                                            $ LauraX.Statup("Inbt", 50, -15)
                                            $ LauraX.FaceChange("angry", 1)
                                            ch_l "Wow, that's pushing it."
                                            $ Line = "rude"
                            "Ok, never mind then.":
                                            $ LauraX.FaceChange("angry", 1)
                                            $ LauraX.Statup("Love", 200, -10)
                                            $ LauraX.Statup("Obed", 90, -10)
                                            $ LauraX.Statup("Obed", 200, -10)
                                            $ LauraX.Statup("Inbt", 50, -15)
                                            ch_l "I was thinking of taking orders from you, not mindgames."
                                            ch_l "I should've known you'd be like this."
                                            $ Line = "rude"

    $ LauraX.RecentActions.append("asked sub")
    $ LauraX.DailyActions.append("asked sub")
    if Line == "rude":
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            $ LauraX.RecentActions.append("angry")
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] checks you as she stomps out of the room."
    elif "sir" in LauraX.Petnames:
            #it didn't fail and "sir" was covered
            $ LauraX.Statup("Obed", 200, 50)
            $ LauraX.Petnames.append("master")
            $ LauraX.Petname = "master"
            $ LauraX.Eyes = "sly"
            ch_l ". . . master. . ."
    else:
            #it didn't fail
            $ LauraX.Statup("Obed", 200, 30)
            $ LauraX.Petnames.append("sir")
            $ LauraX.Petname = "sir"
            $ LauraX.FaceChange("sly", 1)
            ch_l ". . . sir."
    return

label Laura_Master:
    $ LauraX.DrainWord("asked meet")
    call Shift_Focus(LauraX)
    if LauraX.Loc != bg_current and LauraX not in Party:
        "Suddenly, [LauraX.Name] shows up and says she needs to talk to you."

    $ LauraX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(LauraX)
    call CleartheRoom(LauraX)
    call Set_The_Scene
    $ LauraX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ LauraX.FaceChange("sly", 1)
    ch_l "[LauraX.Petname]. . ."
    ch_l ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            $ LauraX.Statup("Obed", 200, 5)
            $ LauraX.Statup("Inbt", 50, 5)
        "What?":
            ch_l "I was asking if I could talk to you about something. . ."
            $ LauraX.Eyes = "side"
            ch_l ". . . personal."
            $ LauraX.Eyes = "squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ LauraX.Statup("Love", 80, 5)
                    $ LauraX.Statup("Obed", 200, 5)
                    ch_l "Right. . ."
                "Oh, then no.":
                    $ LauraX.FaceChange("sad", 1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Obed", 200, -10)
                    $ Line = "embarrassed"
        "No.":
            $ LauraX.FaceChange("perplexed", 1,Brows="confused")
            $ LauraX.Statup("Love", 80, -5)
            $ LauraX.Statup("Obed", 200, -5)
            $ LauraX.Statup("Inbt", 50, -5)
            ch_l "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ LauraX.FaceChange("confused", 1)
                    $ LauraX.Statup("Obed", 200, 10)
                    $ LauraX.Statup("Inbt", 60, 10)
                    ch_l "Right. . ."
                "Yes, not interested.":
                    $ LauraX.FaceChange("sad", 1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Inbt", 50, -10)
                    $ Line = "embarrassed"


    if not Line:
        $ LauraX.FaceChange("sly", 1)
        ch_l "I think I enjoy having you in charge."
        ch_l "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                    $ LauraX.FaceChange("sly", 1)
                    $ LauraX.Statup("Obed", 200, 5)
                    ch_l "Good. Maybe we could take this a bit more seriously?"
                    menu:
                        extend ""
                        "Nah. This is just about perfect.":
                                $ LauraX.FaceChange("sad", 1)
                                $ LauraX.Statup("Obed", 200, -15)
                                $ LauraX.Statup("Love", 80, 10)
                                $ Line = "fail"
                        "What'd you have in mind?":
                                $ LauraX.Eyes = "side"
                                ch_l "I was thinking I could start calling you. . . {i}master{/i}?"
                                $ LauraX.Eyes = "squint"
                                menu:
                                    extend ""
                                    "Oh, yeah.  I'd like that.":
                                            $ LauraX.Statup("Obed", 200, 5)
                                            ch_l "Good. . ."
                                    "Um. . .nah.  That's too much.":
                                            $ LauraX.FaceChange("sadside", 1)
                                            $ LauraX.Statup("Obed", 200, -15)
                                            $ LauraX.Statup("Inbt", 50, 5)
                                            $ Line = "fail"

                        "Actually, I'd prefer we stopped doing it. Too much pressure.":
                                $ LauraX.FaceChange("sad", 1)
                                $ LauraX.Statup("Love", 200, -5)
                                $ LauraX.Statup("Obed", 200, -10)
                                $ LauraX.Statup("Inbt", 50, 15)
                                $ Line = "fail"

                        "Actually, let's stop that. It's creeping me out.":
                                $ LauraX.FaceChange("angry", 2, Eyes="surprised")
                                $ LauraX.Statup("Love", 200, -10)
                                $ LauraX.Statup("Obed", 200, -50)
                                $ LauraX.Statup("Inbt", 50, -15)
                                ch_l "Say no more, I wouldn't want to CREEP YOU OUT."
                                $ Line = "embarrassed"

            "As if I care what you think, slut.":
                    $ LauraX.FaceChange("angry", 1, Mouth="smile")
                    $ LauraX.Statup("Love", 90, -20)
                    $ LauraX.Statup("Obed", 200, 10)
                    $ LauraX.Statup("Inbt", 50, -10)
                    ch_l ". . ."
                    menu:
                        ch_l "Excuse me?"
                        "Sorry. I just don't care what you want.":
                                if ApprovalCheck(LauraX, 1400, "LO"):
                                        $ LauraX.Statup("Obed", 200, 10)
                                        ch_l ". . ."
                                        $ LauraX.FaceChange("sly", 1)
                                        $ LauraX.Statup("Love", 200, 20)
                                        $ LauraX.Statup("Inbt", 50, 15)
                                        ch_l ". . .{i}go on. . .{/i}"
                                else:
                                        $ LauraX.Statup("Love", 200, -15)
                                        $ LauraX.Statup("Obed", 200, -10)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        $ LauraX.FaceChange("angry", 1)
                                        ch_l "!!!"
                                        $ Line = "rude"

                        "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                                $ LauraX.Statup("Love", 200, 10)
                                $ LauraX.Statup("Obed", 200, 10)
                                $ LauraX.Statup("Inbt", 50, 5)
                                if ApprovalCheck(LauraX, 1400, "LO"):
                                        $ LauraX.Statup("Obed", 200, 10)
                                        ch_l ". . ."
                                        $ LauraX.FaceChange("sly", 1)
                                        $ LauraX.Statup("Love", 200, 20)
                                        $ LauraX.Statup("Inbt", 50, 15)
                                        ch_l ". . .{i}no, about right. . .{/i}"
                                else:
                                        $ LauraX.Statup("Love", 200, 5)
                                        $ LauraX.Statup("Obed", 200, -5)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        $ LauraX.FaceChange("angry", 1, Eyes="side")
                                        ch_l ". . ."
                                        ch_l "We'll work on it. . ."

            "I don't really like it. Too much pressure.":
                                $ LauraX.FaceChange("sad", 2)
                                $ LauraX.Statup("Love", 200, -20)
                                $ LauraX.Statup("Obed", 200, -20)
                                $ LauraX.Statup("Inbt", 50, -10)
                                $ Line = "embarrassed"

    $ LauraX.History.append("master")
    if Line == "rude":
            $ LauraX.RecentActions.append("angry")
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] stomps out of the room."
    elif Line == "embarrassed":
            ch_l "Ok, fine then."
            ch_l "And here I was, about to \"elevate your clearance.\""
            hide Laura_Sprite with easeoutright
            call Remove_Girl(LauraX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[LauraX.Name] brushes past you on her way out."
    elif Line == "fail":
            ch_l "Oh. . ."
            ch_l "I guess that's fine."
    else:
            $ LauraX.Statup("Obed", 200, 50)
            $ LauraX.Petnames.append("master")
            $ LauraX.Petname = "master"
            ch_l ". . .master."
    return

label Laura_Sexfriend:   #Laura_Update
        #set this to occur after class
        $ LauraX.Lust = 70
        $ LauraX.Loc = bg_current
        $ LauraX.DrainWord("asked meet")
        call Set_The_Scene
        $ LauraX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ LauraX.FaceChange("sly",2,Eyes="side")
        "[LauraX.Name] approaches you and pulls you aside. She seems to be shivering a little bit."
        "She seems to be squirming around and rubbing her thighs together."
        $ LauraX.Petnames.append("sex friend")
        $ LauraX.FaceChange("sly",2)
        if LauraX in Player.Harem:
                ch_l "Hey."
                ch_l "I need some alone time with you."
        elif "lover" in LauraX.Petnames or "master" in LauraX.Petnames or "lover" in LauraX.Petnames or "sir" in LauraX.Petnames:
                #if you have done the lover thing
                ch_l "Hey."
                ch_l "I need some alone time with you."
        else:
                #if you've done no relationship stuff yet. . .
                ch_l "Hey, so. . . "
                if LauraX.SEXP >= 50:
                    ch_l "I know we're kind of casual and all. . ."
                else:
                    ch_l "Maybe this seems a bit out of the blue, but. . ."
                ch_l "I'd really just like to have some sex."
                ch_l "Like lots of sex."
                ch_l "With you."
                menu:
                    extend ""
                    "Sure":
                        $ LauraX.FaceChange("sly",2,Mouth="smile")
                        $Line = "yes"
                    "No thanks":
                        $ LauraX.FaceChange("confused",2)
                        $Line = "no"
                    ". . .":
                        $ LauraX.Statup("Obed", 90, 5)
                        $ LauraX.FaceChange("confused",2)

                if not Line:
                        ch_l "Now, if at all possible. . ."
                        menu:
                            extend ""
                            "Sure":
                                $ LauraX.FaceChange("sly",2,Mouth="smile")
                                $Line = "yes"
                            "No thanks":
                                $ LauraX.FaceChange("confused",2)
                                $Line = "no"

                if Line == "no":
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 80, 5)
                    ch_l "What? Why not?"
                    menu:
                        extend ""
                        "Ok, fine":
                            $ LauraX.FaceChange("confused",2,Mouth="smile")
                            ch_l "Love the enthusiasm."
                            $Line = "yes"
                        "Not interested":
                            $ LauraX.FaceChange("confused",2)

                        "There's someone else":
                            $ LauraX.Statup("Love", 95, -5)
                            $ LauraX.Statup("Obed", 90, 5)
                            if Player.Harem:
                                    $ LauraX.FaceChange("surprised",2)
                                    ch_l "Oh, [Player.Harem[0].Name]?"
                                    $ LauraX.GLG(Player.Harem[0],600,-25,1)
                            $ LauraX.FaceChange("sly",2)
                            ch_l "Well, she doesn't need to know about it. . ."
                            menu:
                                extend ""
                                "Ok, fine":
                                        ch_l "Love the enthusiasm."
                                        $ Line = "yes"
                                "Still no":
                                        pass

        if Line == "no":
                    $ LauraX.Statup("Love", 200, -10)
                    $ LauraX.Statup("Obed", 90, 15)
                    $ LauraX.Statup("Inbt", 90, 10)
                    $ LauraX.FaceChange("sad",2)
                    ch_l "Really?"
                    ch_l "Bummer."
                    ch_l "Well let me know if you change your mind."
                    $ LauraX.FaceChange("sadside",2,Mouth="lipbite",Brows="angry")
                    if Player.Harem:
                            ch_l "Wonder if [Player.Harem[0].Name]'s busy. . ."
                            $ LauraX.GLG(Player.Harem[0],500,25,1)
                    else:
                            ch_l "Wonder if Kitty's busy. . ."
                            $ LauraX.GLG("Kitty",500,25,1)
        else:
                $ LauraX.Statup("Love", 90, 10)
                $ LauraX.Statup("Obed", 90, 5)
                $ LauraX.Statup("Inbt", 90, 15)
                $ LauraX.FaceChange("sly",1,Mouth="smile")
                if Taboo:
                    ch_l "Wanna take this party someplace else?"
                    menu:
                        extend ""
                        "Yeah":
                                ch_l "Sure, let's go."
                                if bg_current == "bg player":
                                        $ bg_current = "bg laura"
                                else:
                                        $ bg_current = "bg player"
                                $ LauraX.Loc = bg_current
                                call CleartheRoom(LauraX)
                                call Set_The_Scene
                                $ Taboo = 0
                                $ LauraX.Taboo = 0

                        "No, let's do it here.":
                                $ LauraX.Statup("Obed", 80, 5)
                                $ LauraX.Statup("Inbt", 90, 15)
                                ch_l "Kinky."

                $ Situation = LauraX
                $ Player.AddWord(1,"interruption") #adds to Recent
                call Laura_SexPrep              #she offers sex
                call Laura_SexMenu

                #end "if no relationship"
        return

label Laura_Fuckbuddy:
        $ LauraX.DailyActions.append("relationship")
        $ LauraX.Lust = 80
        $ LauraX.DrainWord("asked meet")
        # Conditions, in your room, laura not there.
        "You hear a knock on the door, and go to answer it."
        #change laura's outfit to default
        $ LauraX.Loc = bg_current
        call Shift_Focus(LauraX)
        call Set_The_Scene(0)
        $ LauraX.Outfit = "casual1"
        $ LauraX.OutfitDay = "casual1"
        $ LauraX.OutfitChange("casual1")
        call Display_Girl(LauraX)
        call Taboo_Level
        $ Trigger = "masturbation"
        $ Trigger3 = "fondle pussy"
        $ LauraX.FaceChange("sly",2,Mouth="lipbite")
        "[LauraX.Name] is standing in the doorway, with her hand down her pants."
        "You can tell she's been masturbating furiously, her scent is overpowering."
        $ Trigger = 0
        $ Trigger3 = 0
        $ LauraX.ArmPose = 1
        "She looks you up and down hungrily, and pulls her hand out of her pants."
        "She reaches up to caress your face, smearing her juices along it."
        ch_l "Mine."
        $ LauraX.Petnames.append("fuck buddy")
        $ LauraX.Event[10] += 1

        $ Situation = LauraX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call Laura_SexPrep              #she offers sex
        call Laura_SexMenu
        return

label Gwentro:
        $ Player.AddWord(1,"interruption") #adds to Recent
        if Taboo > 5 or RogueX.Loc == bg_current or KittyX.Loc == bg_current or EmmaX.Loc == bg_current:
            #returns if other girls are present, this is a one on one thing.
            return
        $ LauraX.History.append("Gwentro")
        $ GwenName = "???"
        ch_g "Where is the exit to this place?!"
        call GwenFace("angry")
        show Gwen_Sprite at sprite_location(1500) zorder 25:
                xzoom -1
        show Gwen_Sprite at sprite_location(100) zorder 25 with easeinright #call Display_Gwen
        pause .1
        call GwenFace("surprised")
        $ Speed = 0
        $ LauraX.FaceChange("surprised",2,Eyes="side")
        show Gwen_Sprite at sprite_location(200) zorder 25 with vpunch #call Display_Gwen
        ch_g "Ouch!"
        call GwenFace("angry")
        ch_g "Ok, that's a wall. . . apparently."
        call GwenFace("surprised")
        ch_g "Oh, hey you tw-"
        call GwenFace("surprised",1,Mouth="kiss")
        ch_g "Um. . ."
        call GwenFace("shocked",1)
        ch_g "Sorry! My bad, I was just. . ."
        $ LauraX.FaceChange("confused",2,Eyes="side")
        call GwenFace("surprised",1,Mouth="kiss")
        extend "\n looking for an exit. . ."
        call GwenFace("smile",1)
        extend "\n but you two. . . seem to be working on something. . ."
        call GwenFace("sad",1)
        extend "\n and now I can't see because of this stupid word balloon. . ."
        show Gwen_Sprite:
            ease 1 ypos 150
        call GwenFace("smile",1)
        extend ""
        ch_g "Better. . ."
        show Gwen_Sprite:
            ease 1 ypos 50
        ch_g "So now that we've got that taken care of, what's your name?"
        $ LauraX.FaceChange("angry",1,Eyes="side")
        show Gwen_Sprite:
            ypos 50
        ch_g "So now that we've got that taken care of, what's your name?{w=0.2}{nw}"
        call GwenFace("shocked",0)
        menu:
            ch_g "So now that we've got that taken care of, what's your name?{nw}"
            "[Player.Name]":
                pass
            "Zero":
                pass
            "None of your buisiness":
                pass
            "Who are you?":
                pass
        ch_g "Whoa!" with vpunch
        menu:
            ch_g "Whoa!"
            "What?":
                pass
        call GwenFace("surprised")
        ch_g "Sorry, it's just that menu popping up caught me by surprise."
        call GwenFace("smile")
        ch_g "That's how you talk around here? Menus?"
        menu:
            extend ""
            "Yes?":
                    ch_g "That's ok, no judgement. . ."
                    ch_g "I guess that's not the most important thing at the moment. . ."
            "What are you talking about?":
                    ch_g "The floating blocks from earlier? I guess you can't see those. . ."
                    ch_g "Unless you're roleplaying right now."
        ch_g "Anyway, back to you, what's your name?"
        menu:
            extend ""
            "[Player.Name]":
                ch_p "It's [Player.Name]."
                ch_g "Hi, [Player.Name], my name's Gwen!"
                $ GwenName = "Gwen"
            "None of your buisiness":
                ch_p "It's none of your business."
                ch_g "Well, it looks like your name is [Player.Name]."
                ch_g "I could tell from the menu."
                ch_g "Mine's Gwen, b-t-dubs."
            "Who are you?":
                ch_p "Never mind me, who are you?!"
                ch_g "Oh! That's fair, I'm new around here. My name's Gwen!"
                ch_g "And it looks like your name is [Player.Name]."
                ch_g "I could tell from the menu."
        if GwenName != "Gwen":
            $ GwenName = "Gwen"
            menu:
                extend ""
                "What menu?!":
                    ch_g "Don't worry about it."
                "Riiiight. . .":
                    pass
        ch_g "It is kinda crowded over here though, so if you don't mind. . ."
        show Gwen_Sprite:
            easeout 1 xpos 300
            xzoom 1
            easein .5 xpos 900
        ch_g "Ah, yes, room to breathe!"
        $ LauraX.FaceChange("angry",Eyes="leftside")
        ch_g "Sorry, I should have said hello earlier, hey Laura!"
        $ LauraX.FaceChange("confused",Eyes="leftside")
        ch_l "How do you know my name!"
        ch_g "I've read all about you! Or do you prefer \"X-23?\""
        ch_g "Or \"Wolverine?\""
        call GwenFace("surprised",Mouth="kiss")
        ch_g "God, it's not \"Talon,\" is it?"
        call GwenFace("smile")
        ch_l "[LauraX.Name] - is - fine."
        call GwenFace("smile",Mouth="kiss")
        ch_g "Cool, so. . ."
        menu:
            "What are you doing here?":
                ch_p "What are you doing here?"
                ch_g "I had a feeling you would ask that."
            "Some other irrelvant option.":
                ch_p "What are you doing here?"
                ch_g "Man, determinism, am I right?"
        $ LauraX.FaceChange("confused",Eyes="leftside")
        ch_g "Why are any of us here, really?"
        ch_g "Oh! You mean \"why am I {i}here{/i}\" in this game?"
        call GwenFace("sad")
        ch_g "Honestly? No idea. One minute I had an ongoing, then I was on a team book, guess that's cancelled now?"
        call GwenFace("smile")
        ch_g "Yeah, your guess is as good as mine. Maybe whoever made it's a fan?"
        call GwenFace("smile",1)
        ch_g "Judging by what you two have cooking over there, looks like some kind of hentai game."
        ch_g "Well, \"When in Rome. . .\""
        show Gwen_Sprite:
            easeout .2 xpos 890
            easeout .2 xpos 900
            pause .5
            easeout .15 xpos 880
            easeout .15 xpos 910
            easeout .15 xpos 880
            easeout .15 xpos 900
        ch_g "Well, \"When in Rome. . .\"{w=1.8}{nw}"
        call GwenFace("angry",1)
        ch_g "Huh."
        ch_g "Apparently I can't get my clothes off here."
        call GwenFace("sad",1)
        ch_g "That's unfortunate."
        call GwenFace("angry",1,Mouth="smile")
        ch_g "I could just stay and watch for a bit. . ."
        $ LauraX.FaceChange("angry",Eyes="leftside")
        call GwenFace("surprised",1)
        ch_l "NO!"
        ch_g "Right, right. Don't poke the wolverine. . ."
        call GwenFace("smile",1)
        ch_g "Except you, of course -wink-."
        call GwenFace("sad",0)
        show Gwen_Sprite:
            ease .5 xpos 950
        ch_g "I should probably get going then. . ."
        show Gwen_Sprite:
            ease .5 xpos 1050
        ch_g "Don't know when I'll be back. . ."
        show Gwen_Sprite:
            ease .5 xpos 1200
        ch_g "If ever. . ."
        show Gwen_Sprite:
            ease .5 xpos 1000
        call GwenFace("sad",1,Eyes="surprised")
        ch_g "Maybe never, we won't know."
        show Gwen_Sprite:
            ease .2 xpos 1500
        call GwenFace("surprised")
        ch_l "Get out!"
        ch_g "Right! I'm gone, sorry!"
        hide Gwen_Sprite
        $ LauraX.FaceChange("bemused",Eyes="sexy")
        ch_l "Now, what were were doing. . ."

        return

label Laura_Dressup:
        #(Condition: X23 has returned to school)
        #(location: campus square)
        $ ActiveGirls.append(LauraX) if LauraX not in ActiveGirls else ActiveGirls
        call Shift_Focus(LauraX)
        $ bg_current = "bg campus"
        call Remove_Girl("All")
        $ LauraX.Loc = bg_current
        call Set_The_Scene(0)

        $ LauraX.Outfit = "casual1"
        $ LauraX.OutfitChange("casual1")
        show Laura_Sprite at sprite_location(LauraX.sprite_location) with vpunch
        $ Round -= 10 if Round >= 11 else Round
        $ LauraX.History.remove("dress0")
        $ LauraX.History.append("dress1")
        $ LauraX.History.append("met")
        "As you're heading across the square, you bump into [LauraX.Name]."
        $ LauraX.FaceChange("normal")
        ch_l "Oh, hey."
        menu:
            extend ""
            "Ah, [LauraX.Name]. You're back!":
                    $ LauraX.Statup("Love", 50, 3)
                    $ LauraX.Statup("Obed", 50, 1)
                    ch_l "Yeah, just got back."
            "Hey.":
                    ch_l "Yeah, just got back."
            "Who are you again?":
                    $ LauraX.Statup("Love", 70, -3)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.FaceChange("confused")
                    ch_l "Laura."
                    ch_l "We met a while back."

        "She stretches and pops her neck."
        ch_l "I'll be sticking around for a while this time."
        ch_l "I'll see you around, I could use a hot shower."

        menu:
            extend ""
            "Sure, no problem. See you later!":
                    pass
            "Ok, later.":
                    pass
            "Want some company?":
                    $ LauraX.Statup("Love", 70, -1)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 80, 5)
                    $ LauraX.FaceChange("bemused")
                    ch_l "Not really."

        hide Laura_Sprite with easeoutright
        call Remove_Girl(LauraX)
        "[LauraX.Name] walks away, and as you watch her go you feel a tap on your shoulder."

        call Shift_Focus(KittyX)
        $ KittyX.Loc = bg_current
        call Set_The_Scene(0)
        $ KittyX.Outfit = KittyX.OutfitDay
        $ KittyX.OutfitChange()
        call Display_Girl(KittyX)

        $ KittyX.FaceChange("smile")
        ch_k "Hey, [KittyX.Petname], what're you staring at?"
        #add Kitty arrving here

        menu:
            extend ""
            "Hey, [KittyX.Name]. I was just talking to [LauraX.Name].":
                    ch_k "Oh, she's back?"
            "Oh, nothing.":
                    ch_k "Oh, I see, [LauraX.Name]."
                    ch_k "She's back?"
            "I was checking out that fine piece over there.":
                if ApprovalCheck(KittyX,1200,"LO") or KittyX.Les >= 10:
                        $ KittyX.Statup("Obed", 80, 5)
                        $ KittyX.Statup("Inbt", 80, 5)
                        $ KittyX.FaceChange("bemused",1)
                        ch_k "I guess I can't blame you. . ."
                else:
                        $ KittyX.Statup("Love", 70, -5)
                        $ KittyX.Statup("Obed", 80, 10)
                        $ KittyX.Statup("Inbt", 80, 5)
                        $ KittyX.FaceChange("angry")
                        ch_k "Rude much?"

        $ KittyX.FaceChange("smile",Eyes="side")
        ch_k "She's never around very much, you know."
        ch_k "Must get it from Logan."

        menu:
            extend ""
            "Oh, they're related?":
                    ch_k "Yeah, she's his daughter or something? I'm not too sure."
            "She's his clone, right?":
                    ch_k "I guess? I'm not too sure."
        "She shrugs, but then grins mischieviously."

        $ KittyX.FaceChange("sly")
        ch_k "Actually, we were thinking of giving her a \"welcome home\" present."
        ch_k "You wanna chip in?"

        menu:
            extend ""
            "Sure, why not?":
                    $ KittyX.Statup("Love", 50, 5)
                    $ KittyX.Statup("Obed", 40, 5)
                    ch_p "Here you go. What're you planning to get her?"
            "Nah, I don't really know her.":
                    ch_k "Yeah, maybe you've got a point. She's kinda prickly sometimes."
                    return
            "That could be kind creepy.":
                    ch_k "Yeah, maybe you've got a point. She's kinda prickly sometimes."
                    return

        #"Kitty grins."
        ch_k "Well, she doesn't really have much of a wardrobe, so we were going to get her some new clothes."

        menu:
            extend ""
            "You're really stylish, so you'll probably pick out something great.":
                    $ KittyX.Statup("Love", 80, 5)
                    $ KittyX.Statup("Inbt", 40, 3)
                    $ KittyX.FaceChange("smile",1)
                    ch_k "Sweet talker."
            "That sounds good.":
                    $ KittyX.Statup("Love", 60, 2)
            "With your fashion sense? That'll end well.":
                    $ KittyX.Statup("Love", 70, -5)
                    $ KittyX.Statup("Obed", 80, 5)
                    $ KittyX.Statup("Inbt", 80, -3)
                    $ KittyX.FaceChange("angry")
        ch_k "Anyway, we were thinking around $10 each."

        menu:
            extend ""
            "Here you go." if Player.Cash >= 10:
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 2)
                    ch_k "Nice."
                    $ Player.Cash -= 10
                    $ LauraX.History.append("dress2")
            "I don't have enough. . ." if Player.Cash < 10:
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 2)
                    $ KittyX.FaceChange("normal",1,Brows="surprised",Mouth="sad")
                    ch_k "Oh."
                    ch_k "We aren't in a rush or anything. If you still want to, just hit me up."
            "You know what, never mind.":
                    $ KittyX.Statup("Love", 70, -2)
                    $ KittyX.Statup("Obed", 40, -1)
                    $ KittyX.FaceChange("normal",1,Brows="surprised",Mouth="sad")
                    ch_k "Oh, ok."
        return

label Laura_Dressup2:
        ch_p "Hey, remember that gift you wanted to give [LauraX.Name] earlier?"
        $ KittyX.FaceChange("smile")
        ch_k "Yeah?"
        menu:
            extend ""
            "Here you go, $10.":
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 2)
                    ch_k "Cool."
                    $ LauraX.History.append("dress2")
            "Never mind.":
                    ch_k "Oh, ok."
        return

label Laura_Dressup3:
        #(Condition: Laura_Dressup has already played), State should be "dress2"
        #(location: Kitty's room door)
        $ LauraX.History.remove("dress1")
        $ LauraX.History.remove("dress2")
        $ LauraX.History.append("dress3")
        $ LauraX.Inventory.append("wolvie top")
        $ LauraX.Inventory.append("wolvie panties")

        "You're walking past [KittyX.Name]'s door when you hear her laughing at something."
        "You hear someone else's voice, there's clearly someone else in her room with her."

        ch_l "[KittyX.Name], you shouldn't have."
        ch_l "No, seriously. . ."
        ch_l "you shouldn't have."
        ch_k "Aww, c'mon. You look great."

        "You remember [KittyX.Name] talking about getting [LauraX.Name] some new clothes. She must've gotten [LauraX.Name] to try them on."
        "You can't help but feel curious. . ."

        $ KittyX.Outfit = KittyX.OutfitDay
        $ KittyX.OutfitChange()
        $ LauraX.OutfitChange("nude")
        $ LauraX.Chest = "wolvie top"
        $ LauraX.Panties = "wolvie panties"
        menu:
            extend ""
            "Sneak a peek [[no key] (locked)" if KittyX not in Keys:
                    pass
            "Sneak a peek" if KittyX in Keys:
                    "You use your key and unlock the door, opening it and sticking your head in."
                    ch_p "Hey, [KittyX.Name], what's going on?"
                    ch_k "Hey, [KittyX.Petname]! Come on in!"

                    call CleartheRoom("All",0,1)
                    call Shift_Focus(LauraX)
                    $ KittyX.Loc = "bg kitty"
                    $ LauraX.Loc = "bg kitty"
                    call Set_The_Scene(Dress=0)

                    $ LauraX.FaceChange("sad",2,Eyes="squint",Brows="confused")
                    "[LauraX.Name] stares at you, her eyes narrowed. She's clearly on edge."
                    $ LauraX.FaceChange("sad",2,Brows="confused",Eyes="leftside")
                    ch_l "Didn't you lock the door?"
                    if KittyX.Sleep < 5:
                            $ KittyX.FaceChange("smile",Eyes="side")
                            ch_k "Yeah, but I gave him a key."
                            $ LauraX.FaceChange("sad",1,Brows="confused",Eyes="leftside")
                            ch_l "You. . . gave him a key?"
                    else:
                            # you probably stole it from Xavier
                            $ KittyX.FaceChange("confused",Eyes="side")
                            ch_k "Yeah, I'm not really sure how he got a key. . ."
                            if not ApprovalCheck(KittyX,1200):
                                    #if she doesn't like you a lot yet. . .
                                    $ KittyX.FaceChange("angry",1)
                                    ch_k "Ok, that's enough, out, out!"
                                    "You head back out."
                                    return
                            $ KittyX.FaceChange("smile")
                            ch_k "I guess it's fine though. . ."
                            $ LauraX.FaceChange("sad",1,Brows="confused",Eyes="leftside")
                            ch_l "It's fine that he got a mystery key?"
                    $ KittyX.FaceChange("smile",1)
                    ch_k "Uh-huh. I mean, he's my [KittyX.Petname]."
                    ch_l "Your. . . [KittyX.Petname]."
            "Knock":
                    "You knock on the door."
                    ch_k "Who is it?"
                    ch_p "It's [Player.Name], mind if I come in?"
                    if not ApprovalCheck(KittyX, 1000):
                            ch_k "Um, sorry [KittyX.Petname], we're a little busy in here."
                            ch_k "[KittyX.Like]maybe check back later?"
                            ch_p "Sure, no problem."
                            "You head back out."
                            return
                    ch_k "Sure, [KittyX.Petname]! Gimme a sec!"
                    "[KittyX.Name] unlocks the door and it swings open."

                    call CleartheRoom("All",0,1)
                    call Shift_Focus(LauraX)
                    $ KittyX.Loc = "bg kitty"
                    $ LauraX.Loc = "bg kitty"
                    call Set_The_Scene(Dress=0)

                    $ LauraX.FaceChange("sad",2,Brows="surprised")
                    "[LauraX.Name] stares at you, as if she's not sure what she's seeing."
                    $ LauraX.FaceChange("sad",2,Brows="confused",Eyes="leftside")
                    ch_l "So you just let him come into your room whenever?"
                    $ KittyX.FaceChange("smile",1)
                    ch_k "Uh-huh. I mean, he's my [KittyX.Petname]."
                    ch_l "Your. . . [KittyX.Petname]."

            "Walk away":
                "Nah, I should let them have their girl time."
                return
        $ LauraX.SeenPanties = 1
        $ LauraX.FaceChange("angry",1,Eyes="closed")
        "She shakes her head, trying to absorb all this new information."
        "She mutters to herself."
        ch_l "I've been gone longer than I thought. . ."
        $ LauraX.FaceChange("sad",1,Brows="confused",Eyes="leftside")
        ch_l "So why's he here?"
        $ KittyX.FaceChange("smile",Eyes="side")
        ch_k "Well, he kind of pitched in to get you this stuff, so why not see what he thinks?"
        "[KittyX.Name] walks over and poses like she's presenting [LauraX.Name] as a model."
        $ KittyX.ArmPose = 2
        $ KittyX.FaceChange("smile")
        ch_k "So, what do you think?"

        menu:
            extend ""
            "Her outfit looks familiar. . .":
                    ch_k "I call it the Logan Look."
                    $ LauraX.FaceChange("sad",2,Eyes="stunned")
                    $ LauraX.Statup("Inbt", 40, -2)
                    ch_l "Please don't call it that."
            "Looking good, [LauraX.Name]!":
                    $ LauraX.Statup("Love", 70, 5)
                    $ LauraX.Statup("Obed", 40, 3)
                    $ LauraX.Statup("Inbt", 40, 5)
                    $ LauraX.GLG(KittyX,700,5,1)
                    $ LauraX.FaceChange("sadside",1)
                    ch_l "Yeah, well. . . [KittyX.Name] knows her stuff."
                    $ KittyX.Statup("Love", 70, 1)
                    $ KittyX.Statup("Obed", 40, 3)
                    $ KittyX.GLG(LauraX,700,3,1)
                    ch_k "Heh, thanks."
            "Great ensemble, [KittyX.Name]! It looks great on her!":
                    $ KittyX.Statup("Love", 70, 5)
                    $ KittyX.Statup("Obed", 40, 3)
                    ch_k "Hey, I know my stuff, y'know?"
                    $ LauraX.Statup("Love", 70, 3)
                    $ LauraX.Statup("Obed", 40, 2)
                    $ LauraX.Statup("Inbt", 40, 5)
                    $ LauraX.FaceChange("bemused",1)
                    $ LauraX.GLG(KittyX,700,3,1)
                    ch_l "Yeah, I guess she does. . ."
            "Can I get a refund?":
                    $ KittyX.Statup("Love", 70, -5)
                    $ KittyX.Statup("Obed", 40, -3)
                    $ KittyX.FaceChange("angry")
                    ch_k "Way to bring down the mood."
                    $ LauraX.Statup("Love", 70, -5)
                    $ LauraX.Statup("Obed", 40, 5)
                    $ LauraX.Statup("Inbt", 40, -5)
                    $ LauraX.FaceChange("angry")
                    ch_l "Seriously."

        $ LauraX.FaceChange("smile",0,Eyes="leftside")
        $ LauraX.GLG(KittyX,700,5,1)
        $ KittyX.GLG(LauraX,700,5,1)
        ch_l "But really, [KittyX.Name], thanks for this."
        $ KittyX.FaceChange("smile",Eyes="side")
        ch_k "No problem! Like, what're friends for?"
        ch_l "Pretty sure friends don't normally use their friends as dressup dolls."
        ch_k "Oh, [LauraX.Name], you have sooooo much to learn."
        $ LauraX.FaceChange("smile",Eyes="down")
        "[LauraX.Name] smiles just a little bit and looks down at herself."
        ch_l "I think wearing the whole outfit is a bit much."
        $ LauraX.FaceChange("smile",Eyes="leftside")
        ch_l "You know that Logan's going to have a few words if he sees me like this."
        $ KittyX.FaceChange("smile",Eyes="side")
        ch_k "Hey, it's your outfit now. Mix-and-match, girl!"
        ch_l "Yeah. Yeah, I think I'll do that."
        $ LauraX.Names.append("Wolverine")

        $ KittyX.FaceChange("smile")
        $ LauraX.FaceChange("sly",1)
        "[LauraX.Name] fixes you with a steely gaze."

        ch_l "So. . . I'd like to change now."

        menu:
            extend ""
            "Go right ahead!":
                    $ LauraX.Statup("Obed", 40, 3)
                    $ LauraX.Statup("Inbt", 40, 3)
                    if (not LauraX.SeenChest or not LauraX.SeenPussy) and not ApprovalCheck(LauraX,1400):
                            $ LauraX.Statup("Love", 70, -5)
                            $ LauraX.FaceChange("angry",1)
                            ch_l "I don't think so."
                            ch_k "Yeah, I think you'd better get going, [KittyX.Petname]. . ."
                            ch_k ". . .Before she does to you what Logan does to people who make him mad."
                            "[KittyX.Name] firmly escorts you to the door."
                    else:
                        if LauraX.SeenChest and LauraX.SeenPussy:
                                ch_l "Fair enough. . ."
                        elif ApprovalCheck(LauraX,1400):
                                ch_l "Bold choice. . ."
                        $ KittyX.FaceChange("surprised",2,Eyes="side")
                        $ LauraX.Chest = 0
                        "[LauraX.Name] starts stripping out of the new clothes. . ."
                        if ApprovalCheck(KittyX,1200):
                                $ KittyX.FaceChange("sly",1)
                        else:
                                $ KittyX.FaceChange("angry",1,Eyes="side")

                        $ LauraX.Panties = 0
                        call Laura_First_Topless
                        call Laura_First_Bottomless(1)
                        pause 1
                        $ LauraX.OutfitChange(LauraX.OutfitDay,Changed=1)
                        "And then puts on her usual outfit."

                        if ApprovalCheck(KittyX,1200):
                                $ KittyX.FaceChange("sly",1)
                        else:
                                $ KittyX.FaceChange("angry",1)
                        ch_k "Well, I guess you got your show for the day."
                        ch_k "Now give us some girl time."
                        "[KittyX.Name] shoos you out of the room and you head to the Campus square."

            "Message received. See you girls later!":
                        ch_k "Later, [KittyX.Petname]!"
                        ch_l "See ya."

        $ Round -= 20 if Round >= 21 else Round
        return
        #End scene

label Laura_Foul:
        $ LauraX.History.remove("partyfoul")
        if "partysolved" in LauraX.History:
                $ LauraX.History.remove("partysolved")
        $ LauraX.AddWord(1,0,0,0,"partyfix") #adds "partysolved" to History
        $ LauraX.FaceChange("sad",1)
        if LauraX.Loc == bg_current or LauraX in Party:
                "[LauraX.Name] glances over at you with a distressed look."
        else:
                "[LauraX.Name] turns a corner and notices you."
        if bg_current != "bg laura" and bg_current != "bg player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg laura"
        $ LauraX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(LauraX)
        call Set_The_Scene
        call Taboo_Level
        ch_l "Hey. . ."
        ch_l "[LauraX.Petname]. . ."
        ch_l "About that time at the party. . ."
        menu:
            extend ""
            "What time at the party?":
                    $ LauraX.Statup("Love", 90, -2)
                    $ LauraX.Statup("Obed", 80, 2)
                    $ LauraX.Statup("Inbt", 60, 1)
                    $ LauraX.FaceChange("confused",2)
            "Oh, yeah. I'm sorry about that.":
                    $ LauraX.Statup("Love", 80, 5)
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.FaceChange("surprised",2)
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                    $ LauraX.FaceChange("smile",1)
            "Yeah?":
                    $ LauraX.Statup("Obed", 50, 1)
                    $ LauraX.Statup("Inbt", 60, 1)
                    $ LauraX.FaceChange("sad",1)
            ". . .":
                    $ LauraX.Statup("Love", 80, -1)
                    $ LauraX.Statup("Obed", 50, 2)
                    $ LauraX.FaceChange("sad",1)

        if "sorry" not in LauraX.RecentActions:
                    #if you didn't apologize in first response
                    $ LauraX.FaceChange("sadside",1)
                    ch_l "We were at the Halloween Party. . ."
                    $ LauraX.FaceChange("sad",1)
                    ch_l "And you said something about my costume. . ."
                    menu:
                        extend ""
                        "I don't remember, what did I say?":
                                $ LauraX.Statup("Love", 99, -3)
                                $ LauraX.FaceChange("surprised",1)
                        "Oh, yeah. I'm sorry about that.":
                                $ LauraX.FaceChange("smile",1)
                                $ LauraX.Statup("Love", 80, 5)
                                $ LauraX.Statup("Love", 200, 5)
                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                        "Did I?":
                                $ LauraX.FaceChange("surprised",1)
                                ch_l ". . ."
                                $ LauraX.Statup("Love", 99, -5)
                                $ LauraX.Statup("Obed", 70, 3)
                                $ LauraX.Statup("Obed", 90, 2)
                                $ LauraX.FaceChange("angry",1)
                        ". . .":
                                $ LauraX.Statup("Love", 99, -1)
                                $ LauraX.FaceChange("angry",1)

        if "sorry" not in LauraX.RecentActions:
                    #if you didn't apologize in second response
                    ch_l "You said that it looked like a. . ."
                    ch_l "A prostitute."
                    menu:
                        extend ""
                        "Oooh. Ouch. Yeah.":
                                $ LauraX.FaceChange("sly",1)
                                $ LauraX.Statup("Love", 80, 2)
                                $ LauraX.Statup("Love", 200, 2)
                                $ LauraX.Statup("Inbt", 60, 2)
                        "Oh, yeah. I'm sorry about that.":
                                $ LauraX.FaceChange("smile",1)
                                $ LauraX.Statup("Love", 80, 2)
                                $ LauraX.Statup("Love", 200, 5)
                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                        "Is that a problem?":
                                $ LauraX.FaceChange("surprised",1)
                                pause 0.5
                                $ LauraX.FaceChange("angry",1)
                                $ LauraX.Statup("Love", 80, -5)
                                $ LauraX.Statup("Love", 200, -5)
                                $ LauraX.Statup("Obed", 70, 5)
                                ch_l "Of -course- it's a -problem-. . ."
                        "Huh.":
                                $ LauraX.Statup("Love", 99, -3)
                                $ LauraX.Statup("Obed", 70, 5)
                                $ LauraX.FaceChange("surprised",1)
                        ". . .":
                                $ LauraX.Statup("Love", 80, -2)
                                $ LauraX.Statup("Love", 200, -2)
                                $ LauraX.FaceChange("angry",1)

        if "lover" in LauraX.Petnames:
                ch_l "You understand why this would... bother me. . ."
                menu:
                    extend ""
                    "Oh. . . yeah.":
                            $ LauraX.FaceChange("normal",1,Eyes="side")
                            $ LauraX.Statup("Love", 90, 1)
                            $ LauraX.Statup("Inbt", 60, 2)
                            $ LauraX.AddWord(1,"nyx",0,0,0) #adds "nyx" to Recent
                    "I'm sorry, I must have missed it.":
                            $ LauraX.FaceChange("confused",2)
                            $ LauraX.Statup("Love", 200, -3)
                            ch_l "Seriously?"
                            $ LauraX.FaceChange("angry",1)
                    "What? Why?":
                            $ LauraX.FaceChange("confused",2)
                            $ LauraX.Statup("Love", 200, -5)
                            ch_l "Seriously?"
                            $ LauraX.FaceChange("angry",1)

        if "nyx" not in LauraX.RecentActions:
                ch_l "Maybe you don't understand why this cuts deep. . ."
                ch_l ". . ."
                $ LauraX.FaceChange("sadside",1)
                ch_l "When I was younger, on my own. . ."
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "I had to do some things. . ."
                $ LauraX.Blush = 2
                $ LauraX.Statup("Inbt", 60, 1)
                ch_l "On the streets."
                $ LauraX.FaceChange("sad",1)
                ch_l "So I don't want to be called. . . that."

        menu:
            extend ""
            "Oh, I'm so sorry.":
                    $ LauraX.Statup("Love", 200, 5)
                    $ LauraX.FaceChange("smile",1,Eyes="side")
                    ch_l "Thanks. . ."
                    $ LauraX.FaceChange("smile",1)
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
            "Yeah, I get it.":
                    $ LauraX.Statup("Love", 80, 2)
                    $ LauraX.Statup("Love", 200, 3)
                    $ LauraX.Statup("Obed", 80, 1)
                    $ LauraX.Statup("Inbt", 60, 1)
                    $ LauraX.FaceChange("smile",1)
                    ch_l "Thanks."
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
            "Oh, ok.":
                    if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 400, "O"):
                        $ LauraX.Statup("Obed", 60, 3)
                        $ LauraX.Statup("Obed", 90, 2)
                        $ LauraX.Statup("Inbt", 60, 3)
                        $ LauraX.FaceChange("sly",1)
                    else:
                        $ LauraX.Statup("Love", 200, -5)
                        $ LauraX.Statup("Obed", 90, 5)
                        $ LauraX.FaceChange("angry",1)
                    ch_l ". . ."
            "Ha! Get over it.":
                    $ LauraX.FaceChange("angry",1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Love", 200, -5)
                    $ LauraX.Statup("Obed", 80, 5)
                    $ LauraX.Statup("Inbt", 60, 5)
                    ch_l "Asshole."
                    $ LauraX.DrainWord("sorry",1,0,0)
        menu:
            extend ""
            "Won't happen again.":
                    if "sorry" not in LauraX.RecentActions:
                            $ LauraX.FaceChange("confused",1)
                            ch_l "So you're sorry then?"
                            menu:
                                "Yeah, of course!":
                                        $ LauraX.FaceChange("smile",1)
                                        $ LauraX.Statup("Love", 200, 3)
                                        ch_l "Good."
                                        $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                                "Eh, I guess?":
                                        ch_l ". . ."
                                        if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 400, "O"):
                                                $ LauraX.FaceChange("normal",1)
                                                $ LauraX.Statup("Love", 80, 2)
                                                $ LauraX.Statup("Love", 200, 2)
                                                $ LauraX.Statup("Obed", 90, 2)
                                                $ LauraX.Statup("Inbt", 60, 1)
                                                ch_l "Good enough."
                                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                                        else:
                                                $ LauraX.Statup("Love", 90, -5)
                                                $ LauraX.Statup("Obed", 90, 3)
                                                $ LauraX.Statup("Inbt", 60, 1)
                                                $ LauraX.FaceChange("angry",1)
                                                ch_l "Not good enough."
                                "For what?":
                                        $ LauraX.FaceChange("angry",1)
                                        $ LauraX.Statup("Love", 80, -5)
                                        $ LauraX.Statup("Love", 99, -5)
                                        $ LauraX.Statup("Obed", 90, 5)
                                        $ LauraX.Statup("Inbt", 50, 5)
                                        $ LauraX.Statup("Inbt", 70, 5)
                                        ch_l "Grrrrrr."
                    else:
                            $ LauraX.FaceChange("angry",1,Mouth="smile")
                            $ LauraX.Statup("Obed", 80, 2)
                            $ LauraX.Statup("Inbt", 60, 3)
                            ch_l "It'd better not."

            "That all?":
                    $ LauraX.FaceChange("angry",1)
                    $ LauraX.Statup("Love", 80, -5)
                    $ LauraX.Statup("Love", 99, -5)
                    $ LauraX.Statup("Inbt", 60, 10)
                    ch_l "Seriously?!"

        if "sorry" in LauraX.RecentActions:
                $ LauraX.FaceChange("smile",1)
                ch_l "I'm glad that you care, at least."
        else:
                $ LauraX.FaceChange("angry",1)
                $ LauraX.AddWord(1,"angry","angry",0,0) #adds "angry" to Recent/Daily
                ch_l "Well if that's how you feel about it, you can fuck right off!"
        return
