label LauraMeet(Topics=[],Loop=1):
    $ active_Girls.append(LauraX) if LauraX not in active_Girls else active_Girls
    $ LauraX.name = "???"
    $ LauraX.names.remove("Laura")
    $ LauraX.names.append("X-23")
    $ bg_current = "bg_dangerroom"
    call clear_the_room("all",0,1)
    $ LauraX.location = "bg_dangerroom"
    $ LauraX.love = 400
    $ LauraX.obedience = 0
    $ LauraX.inhibition = 200
    $ LauraX.lust = 10
    call shift_focus(LauraX)
    $ LauraX.sprite_location = StageCenter
    call set_the_scene(0)
    $ LauraX.Petname = Player.name
    $ LauraX.OutfitDay = "casual1"
    $ LauraX.Outfit = "casual1"
    $ LauraX.OutfitChange("casual1")

    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."
    ". . ."
    $ LauraX.change_face("normal", 0)
    show Laura_Sprite at sprite_location(LauraX.sprite_location)
    "When you come to, a girl pulls you up by your arm."
    $ LauraX.change_face("surprised", 0, Eyes="squint",Brows="sad")
    ch_u "Oh, good, you don't look too damaged."
    $ LauraX.change_face("smile", 0, Brows="sad")
    ch_u "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door."
    $ LauraX.change_face("smile", 0)
    while Loop:
        menu:
            extend ""
            "Who are you?" if LauraX.name == "???":
                    $ LauraX.change_face("normal", 0)
                    ch_l "I go by \"X-23\" in the field."
                    $ LauraX.name = "X-23"
            "X-23? Is that your real name?" if LauraX.name == "X-23" and "X23" not in Topics:
                    $ LauraX.change_face("confused", 0)
                    ch_l "It's the one I was born with."
                    $ Topics.append("X23")
            "Is there anything else I could call you?" if "X23" in Topics and LauraX not in Topics:
                    $ LauraX.change_stat("love", 70, 5) # love
                    $ LauraX.change_face("normal", 0)
                    ch_l "I also go by Laura. Laura Kinney."
                    $ LauraX.change_face("confused", 0, Mouth="normal")
                    $ LauraX.name = "Laura"
                    $ LauraX.names.append("Laura")
                    $ Topics.append(LauraX)
                    menu:
                        extend ""
                        "Nice to meet you Laura.":
                            $ LauraX.change_stat("love", 70, 5) # love
                            $ LauraX.change_face("normal", 0)
                            ch_l "Yeah, ok."
                        "Hello Laura Laura Kinney.":
                            $ LauraX.change_face("confused", 0,Mouth="sucking")
                            ch_l "It's just-"
                            $ LauraX.change_face("smile", 0,Brows="surprised")
                            $ LauraX.change_stat("love", 70, 3) # love
                            $ LauraX.change_stat("inhibition", 70, 2) # inhibition
                            ch_l "Oh, get it."
                        "Ok, how did you get that name?":
                            $ LauraX.change_face("angry", 1,Eyes="side")
                            $ LauraX.change_stat("love", 70, -2) # love
                            $ LauraX.change_stat("obedience", 70, 2) # obedience
                            ch_l "You're getting too personal."
            "I think I'd prefer calling you X-23." if LauraX.name == LauraX and LauraX in Topics:
                            $ LauraX.change_stat("love", 70, -2) # love
                            $ LauraX.change_stat("obedience", 70, 5) # obedience
                            $ LauraX.change_face("sadside", 0,Brows="normal")
                            ch_l "Suit yourself."
                            $ LauraX.name = "X-23"
            "My name is [Player.name]" if LauraX.name != "???" and "player" not in Topics:
                    $ LauraX.change_face("normal", 0)
                    ch_l "Ok."
                    $ Topics.append("player")
                    menu:
                        extend ""
                        ". . .and it's nice to meet you?":
                            $ LauraX.change_stat("love", 70, 1) # love
                            $ LauraX.change_face("confused", 0,Mouth="normal")
                            ch_l "Yeah, you too."
                        "So. . .[[moving on]":
                            $ LauraX.change_stat("love", 70, 3) # love
                            $ LauraX.change_stat("obedience", 70, 1) # obedience
                            $ LauraX.change_stat("inhibition", 70, 1) # inhibition

            "What are you doing here?" if "Training" not in Topics:
                    $ LauraX.change_stat("obedience", 70, -2) # obedience
                    $ LauraX.change_face("confused", 0)
                    ch_l "Training. That's the point of this place."
                    $ Topics.append("Training")
                    menu:
                        extend ""
                        "I meant in the school, I haven't seen you around before.":
                                $ LauraX.change_stat("obedience", 70, 2) # obedience
                        "Ok, that's fair.":
                                $ LauraX.change_face("normal", 0)
                                ch_p "But are you new to this school?"
                                $ LauraX.change_stat("love", 70, 3) # love
                                $ LauraX.change_stat("obedience", 70, 4) # obedience
                    ch_l "I've been here since before your time."
                    ch_l "Mostly out in the field though."
            "So you don't stay here long?" if "Training" in Topics and "Stay" not in Topics:
                    $ LauraX.change_stat("love", 70, 2) # love
                    $ LauraX.change_face("normal", 0,Eyes="side")
                    ch_l "I'll be heading out again soon."
                    $ LauraX.change_face("normal", 0)
                    ch_l "But I am planning to stick around after I get back from this mission."
                    $ Topics.append("Stay")


            "What the hell was that?" if len(Topics) <= 1 and "WTF" not in Topics:
                    $ LauraX.change_stat("love", 70, -2) # love
                    $ LauraX.change_stat("obedience", 70, 8) # obedience
                    $ LauraX.change_face("confused", 0)
                    ch_l "It was a robot arm."
                    $ LauraX.change_face("sad", 1,Eyes="leftside")
                    ch_l "Like I said, sorry."
                    $ LauraX.change_stat("obedience", 70, -3) # obedience
                    $ LauraX.change_stat("inhibition", 70, 3) # inhibition
                    $ LauraX.change_face("smile", 0,Brows="confused")
                    ch_l "You probably should have ducked though."
                    $ Topics.append("WTF")

            "So what's your mutant power?" if LauraX.name != "???" and "claws" not in Topics:
                    $ LauraX.change_stat("love", 70, 1) # love
                    $ LauraX.change_stat("obedience", 70, 1) # obedience
                    $ LauraX.change_face("normal", 0)
                    ch_l "I can heal fast."
                    $ LauraX.ArmPose = 2
                    ch_l "Also I have claws."
                    $ LauraX.Claws = 1
                    $ LauraX.change_face("smile", 0,Brows="confused")
                    "snikt"
                    $ Topics.append("claws")
                    menu:
                        "Those claws look pretty sharp.":
                                $ LauraX.change_stat("inhibition", 70, 3) # inhibition
                                ch_l "Yeah, indestructible too."
                        "Cool.":
                                $ LauraX.change_stat("love", 70, 3) # love
                                $ LauraX.change_stat("obedience", 70, 2) # obedience
                                $ LauraX.change_stat("inhibition", 70, 1) # inhibition
                                $ LauraX.change_face("smile", 0,Brows="surprised")
                                ch_l "Yeah, indestructible too."
                        "Ouch.":
                                $ LauraX.Claws = 0
                                $ LauraX.change_face("confused", 0)
                                $ LauraX.change_stat("love", 70, -2) # love
                                $ LauraX.change_stat("obedience", 70, -5) # obedience
                                ch_l "Don't worry, I won't stab you."
                                $ LauraX.change_face("confused", 0,Mouth="normal")
                                $ LauraX.change_stat("inhibition", 70, 7) # inhibition
                                ch_l "Probably."
                    $ LauraX.Claws = 0
                    $ LauraX.ArmPose = 1

            "Don't you want to know my power?" if "claws" in Topics and "powers" not in Topics:
                    if LauraX.love >= 405:
                            $ LauraX.change_face("smile", 0,Brows="confused")
                            ch_l "Yeah, I guess."
                    else:
                            $ LauraX.change_face("normal", 0)
                            ch_l "Not really."
                    $ LauraX.change_stat("inhibition", 70, 3) # inhibition
                    $ Topics.append("powers")
                    ch_p "I'm immune to mutant powers and can shut them off."
                    $ LauraX.change_face("smile", 0,Brows="confused")
                    $ LauraX.change_stat("love", 70, 3) # love
                    $ LauraX.change_stat("obedience", 70, 3) # obedience
                    ch_l "Huh. Interesting. So you can stop me from healing?"
                    ch_p "Yeah. If I touch you, temporarily."
                    $ LauraX.change_stat("obedience", 70, 2) # obedience
                    $ LauraX.change_stat("lust", 70, 3) # lust
                    ch_l "Give it a try."
                    "She holds out her arm, and you grab it."
                    $ LauraX.change_stat("love", 70, 1) # love
                    $ LauraX.change_stat("obedience", 70, 2) # obedience
                    $ LauraX.change_stat("lust", 70, 5) # lust
                    $ LauraX.change_face("confused", 0)
                    ch_l "Huh."
                    $ LauraX.change_face("sexy", 1,Eyes="closed")
                    $ LauraX.Addictionrate += 1
                    "You can feel her shudder a little."
                    $ LauraX.change_face("sexy", 1)
                    $ LauraX.change_stat("love", 70, 1) # love
                    $ LauraX.change_stat("obedience", 70, 3) # obedience
                    $ LauraX.change_stat("lust", 70, 5) # lust
                    $ LauraX.Addictionrate += 1
                    ch_l "That feels weird."
                    $ LauraX.change_face("sexy", 1,Eyes="leftside")
                    $ LauraX.change_stat("obedience", 70, 1) # obedience
                    $ LauraX.change_stat("lust", 70, 3) # lust
                    $ LauraX.Addictionrate += 1
                    ch_l "-a little more \"alive\" than usual."
                    $ LauraX.change_stat("inhibition", 70, 5) # inhibition
                    $ LauraX.change_stat("lust", 70, 5) # lust
                    $ LauraX.change_face("sexy", 1,Brows="confused")
                    $ LauraX.Addictionrate += 1
                    ch_l "Almost. . . dangerous."

            "Never mind that. . . [[moving on]" if LauraX.name != "???":
                    $ Loop = 0

        if len(Topics) >= 3 and LauraX.name == "???":
                $ LauraX.change_stat("love", 70, -2) # love
                $ LauraX.change_stat("obedience", 70, 5) # obedience
                $ LauraX.change_stat("inhibition", 70, 5) # inhibition
                ch_l "Oh, by the way, you can call me \"X-23\"."
                $ LauraX.name = "X-23"
        if len(Topics) >= 8:
                $ Loop = 0


    #close while loop
    ch_l "Ok, I've got a plane to catch."
    if "player" in Topics:
            $ LauraX.change_stat("love", 70, 2) # love
            $ LauraX.change_stat("lust", 70, 1) # lust
            $ LauraX.change_face("smile",0)
            ch_l "Maybe I'll see you when I get back, [Player.name]."
    else:
            $ LauraX.change_face("normal", 0)
            ch_l "Maybe I'll see you when I get back, stranger."
    if "powers" in Topics:
            $ LauraX.change_stat("obedience", 70, 2) # obedience
            $ LauraX.change_stat("inhibition", 70, 2) # inhibition
            $ LauraX.change_stat("lust", 70, 3) # lust
            $ LauraX.change_face("smile", 1, Brows="confused")
            ch_l "We should. . . spar."

    $ LauraX.location = "hold"
    call set_the_scene

    "She dashes out of the room, headed for the hangar."

    $ LauraX.PubeC = 3
    $ LauraX.Todo.append("mission")

    $ bg_current = "bg_dangerroom"
    $ Round -= 10
    call shift_focus(RogueX)
    $ active_Girls.remove(LauraX) if LauraX in active_Girls else active_Girls

    return

label Laura_Cleanhouse:
        # this is triggered if you agree to break up the other girls, but then fail to within the time limit
        $ LauraX.DrainWord("asked meet")
        if "cleanhouse" in LauraX.Todo:
                        $ LauraX.Todo.remove("cleanhouse")
        if not Player.Harem or LauraX in Player.Harem:
                        $ LauraX.Event[5] = 2
                        return

        if LauraX.location == bg_current or LauraX in Party:
                "[LauraX.name] glances over at you with a scowl."
        else:
                "[LauraX.name] turns a corner and notices you."
        if bg_current != "bg_laura" and bg_current != "bg_player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg_laura"
        $ LauraX.location = bg_current
        call set_the_scene
        call clear_the_room(LauraX)
        call set_the_scene
        call Taboo_Level
        $ LauraX.daily_history.append("relationship")
        $ LauraX.change_stat("love", 200, -20)
        $ LauraX.change_face("angry",1)
        ch_l "What's the deal, [Player.Petname]?"
        ch_l "It's been a week already, and you're still dating [Player.Harem[0].name]!"
        if len(Player.Harem) >= 2:
                ch_l "Not to mention the rest of them!"
        menu:
            extend ""
            "Sorry about that, I'm sticking with them":
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 80, 5)
                    $ LauraX.change_stat("inhibition", 80, 5)
                    $ LauraX.change_face("angry",2)
                    ch_l "You asshole."
                    $ LauraX.change_face("sadside",1)
                    ch_l "You could have at least been honest about it."
            "Must have slipped my mind":
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_stat("obedience", 80, 10)
                    ch_l "!"
                    ch_l "Seriously dude? That's all you've got?"
            "[[shrug]":
                    $ LauraX.change_stat("love", 200, -20)
                    $ LauraX.change_stat("obedience", 80, 10)
                    $ LauraX.change_stat("inhibition", 80, 10)
                    $ LauraX.Blush = 2
                    show Laura_Sprite with vpunch
                    "She clocks you one."
                    "That was fair."
                    $ LauraX.Blush = 1

        ch_l "I can't believe you're putting me through this."
        ch_l "Making me choose between you and putting up with this whole arrangement."
        $ line = 0
        if ApprovalCheck(LauraX, 1400) and ApprovalCheck(LauraX, 600,"O"):
                #if she's very obedient. . .
                pass
        elif ApprovalCheck(LauraX, 1200) and ApprovalCheck(LauraX, 500,"O"):
                #second chance on if she likes you well enough. . .
                $ Girls = Player.Harem[:]
                while Girls and line != "no":
                    # Spits out a "no" if she doesn't like another girl
                    if LauraX.GirlLikeCheck(Girls[0]) <= 400:
                            $ line = "no"
                    $ Girls.remove(Girls[0])
        else:
                $ line = "no"
        if line == "no":
                $ LauraX.change_stat("love", 200, -10)
                $ LauraX.change_stat("obedience", 80, 10)
                $ LauraX.change_face("angry",1)
                call Haremchange_stat(LauraX,700,-15) #lowers like of all Harem girls by 15
                ch_l "No, this is bullshit, never mind."
        else:
                $ LauraX.change_stat("love", 200, 5)
                $ LauraX.change_stat("obedience", 80, 20)
                $ LauraX.change_stat("inhibition", 80, 10)
                $ LauraX.change_face("angry",1,Eyes="side")
                ch_l "Ok, fine, whatever. I'm in too."
                if not simulation:
                        $ Player.Harem.append(LauraX)
                        if "LauraYes" in Player.Traits:
                                $ Player.Traits.remove("LauraYes")
                        $ LauraX.Petnames.append("boyfriend")
                        call Harem_Initiation
                        call Haremchange_stat(LauraX,900,20) #raises like of all Harem girls by 20
                        $ LauraX.Event[5] = 20
        return

label Laura_love(Shipping=[],Shipshape=0,Topics=[],Girls=[]):
        # SHipping is used to track who else you're involved with
        # if LauraX.Event[6] = 5, then it cleared
        # if LauraX.Event[6] = 20, then it broke because you didn't love her
        # if LauraX.Event[6] = 23, then it broke because you pissed her off
        # if LauraX.Event[6] = 25, then it broke and you already went through the redux

        $ LauraX.DrainWord("asked meet")
        $ Girls = all_Girls[:]
        $ Girls.remove(LauraX)
        while Girls:
            if ApprovalCheck(Girls[0], 1200, "LO"):
                    $ Shipping.append(Girls[0])
            $ Girls.remove(Girls[0])
        $ Shipshape = len(Shipping)

        if LauraX.location == bg_current or LauraX in Party:
                "[LauraX.name] glances over at you with a concerned look."
        else:
                "[LauraX.name] turns a corner and notices you."
        if bg_current != "bg_laura" and bg_current != "bg_player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg_laura"
        $ LauraX.location = bg_current
        call set_the_scene
        call clear_the_room(LauraX)
        call set_the_scene
        call Taboo_Level
        $ LauraX.daily_history.append("relationship")
        $ LauraX.change_face("sad",1)
        ch_l "Hey, so, I like what this is. . ."
        ch_l "-what we have. . ."
        $ LauraX.change_face("sadside",1)
        ch_l "It's been kind of hard for me to open up to people. . ."
        ch_l "I've been betrayed a lot out there."
        menu:
            extend ""
            "I would never betray you.":
                    $ LauraX.change_face("bemused",1)
                    $ LauraX.change_stat("love", 200, 10)
                    $ LauraX.change_stat("obedience", 70, 5)
                    $ LauraX.change_stat("inhibition", 60, 5)
                    ch_l "I. . . know that now."
            "I'm sorry to hear that.":
                    $ LauraX.change_face("sadside",1,Mouth="smile")
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_stat("obedience", 90, -5)
                    $ LauraX.change_stat("inhibition", 60, 10)
                    ch_l ". . ."
                    $ LauraX.change_face("smile",1)
                    ch_l "Thank you. . ."
            "That must be rough.":
                    $ LauraX.change_face("sadside",1,Mouth="normal")
                    $ LauraX.change_stat("love", 200, 5)
                    ch_l ". . ."
                    $ LauraX.change_face("smile",1)
                    ch_l "It was. . ."
            "Wow, that sucks.":
                    $ LauraX.change_face("confused",1)
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 90, 10)
                    $ LauraX.change_stat("inhibition", 90, -5)
                    ch_l ". . ."
                    $ LauraX.change_face("angry",1,Eyes="side")
                    ch_l "Right, so. . ."
        ch_l "I didn't always have it as easy as I've had it here."
        $ LauraX.Eyes = "normal"
        ch_l "I only thought it fair to tell you a little about that history."
        $ line = 0
        while len(Topics) < 9 and "exit" not in Topics:
                #lines are topics of current discussion. "Topics" catalogues things alrewady discussed

                if line == "facility":
                        menu:
                            extend ""
                            "How many people did you kill?" if "kills" not in Topics:
                                    $ LauraX.change_face("angry",0,Eyes="side")
                                    ch_l "Dozens. Maybe more. At least 13 primary targets."
                                    ch_l "Too many \"collaterals.\""
                                    $ Topics.append("kills")
                            "Did you ever fail a mission?" if "fail" not in Topics:
                                    $ LauraX.change_face("angry",0,Eyes="side",Brows="normal")
                                    ch_l "Once or twice."
                                    ch_l "Sometimes they managed to get away."
                                    ch_l "I'm not proud of who I was back then, but even then. . ."
                                    $ LauraX.Mouth = "smile"
                                    ch_l ". . . a part of me was happy when they did."
                                    $ Topics.append("fail")
                            "Did anyone take care of you?" if "mother" not in Topics:
                                    $ LauraX.change_face("smile",0)
                                    ch_l "My mother, Sarah Kinney."
                                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ LauraX.change_face("sadside",0)
                                    ch_l "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ line = "mother"
                            "How did you escape?" if "escape" not in Topics:
                                    $ LauraX.change_face("sadside",0)
                                    ch_l "Mother."
                                    ch_l "She got me out, found me an escape route."
                                    ch_l "It was the last thing she did."
                                    $ Topics.append("escape")
                                    $ line = "mother"
                            "I'd like to know more about what came after.":
                                    $ line = "NYX"
                            "Enough about that though. . .":
                                    $ line = 0

                # end facility questions

                if line == "mother":
                        menu:
                            extend ""
                            "Who was your mother?" if "mother" not in Topics:
                                    $ LauraX.change_face("smile",0)
                                    ch_l "Her name was Sarah Kinney."
                                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ LauraX.change_face("sadside",0)
                                    ch_l "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ line = "mother"
                            "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:
                                    $ LauraX.change_face("sad",0,Eyes="surprised")
                                    ch_l "I didn't want to, but the primary_action scent made me. . ."
                                    $ LauraX.change_face("sadside",0)
                                    if "trigger" in LauraX.History:
                                            ch_l "I've mentioned that to you before. . ."
                                    else:
                                            $ LauraX.History.append("trigger")
                                    ch_l ". . . it can make me kill, even if I don't want to."
                                    $ Topics.append("killed")
                            "It wasn't your fault." if "killed" in Topics:
                                    $ LauraX.change_stat("love", 200, 5)
                                    $ LauraX.change_stat("obedience", 70, 5)
                                    $ LauraX.change_stat("inhibition", 70, 5)
                                    $ LauraX.change_face("sad",0)
                                    ch_l "Not completely, no."
                                    $ LauraX.change_face("sadside",0)
                                    ch_l "But my hands aren't clean."
                                    $ line = "facility"
                            "That must have been horrible." if "killed" in Topics:
                                    $ LauraX.change_face("sadside",0)
                                    $ LauraX.change_stat("love", 200, 5)
                                    $ LauraX.change_stat("obedience", 90, 5)
                                    ch_l "It's taken me some time. . ."
                                    $ LauraX.change_face("normal",0)
                                    ch_l "but I think I'm ok with it now."
                                    $ line = "facility"
                            "Bummer." if "killed" in Topics:
                                    $ LauraX.change_face("angry",1)
                                    $ LauraX.change_stat("love", 200, -10)
                                    $ LauraX.change_stat("obedience", 90, 5)
                                    ch_l "Are you seriously making fun of my mother's death?!"
                                    $ Topics.append("exit")
                                    $ line = "angry"
                # end questions about mother

                if line == "NYX":
                        menu:
                            extend ""
                            "What did you do for a living?" if "living" not in Topics:
                                    $ LauraX.change_face("sadside",0)
                                    ch_l "There wasn't much I could do at the time, I mostly just scrounged for food."
                                    ch_l "You can get by on some pretty awful stuff if you have a healing factor."
                                    $ LauraX.change_face("bemused",1,Brows="sad")
                                    ch_l "I also did some. . . shady stuff."
                                    $ Topics.append("living")

                            "Was it sexual?" if "work" not in Topics and "living" in Topics:
                                    $ LauraX.change_face("sadside",2)
                                    $ LauraX.change_stat("obedience", 90, 5)
                                    $ LauraX.change_stat("inhibition", 90, 10)
                                    ch_l ". . ."
                                    $ LauraX.Blush = 1
                                    ch_l "A little."
                                    $ line = "work"
                                    $ Topics.append("work")

                            "Did you hurt people?" if "work" not in Topics and "living" in Topics:
                                    $ LauraX.change_face("surprised",0,Eyes="normal")
                                    ch_l "No, definitely not."
                                    ch_l "After the facility, I just couldn't take that sort of work anymore."
                                    $ LauraX.change_face("bemused",0)
                                    ch_l "I avoided hurting anyone."
                                    $ LauraX.change_face("sadside",2)
                                    ch_l "It tended to be more. . . sexual work."
                                    $ line = "work"
                                    $ Topics.append("work")

                            "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:
                                    $ LauraX.change_face("bemused",0)
                                    ch_l "Yeah, eventually."
                                    ch_l "I'd seen Wolverine on the news, and thought maybe he had some answers."
                                    ch_l "He's not around much though."
                                    $ Topics.append("xaviers")
                                    $ line = 0
                            "Good thing you made it here. [[exit]" if "xaviers" in Topics:
                                    $ LauraX.change_face("smile",0)
                                    ch_l "Yeah."
                                    $ line = 0

                if line == "work":
                        $ LauraX.change_face("sadside",0,Mouth="normal")
                        ch_l "It was mostly the rougher customers."
                        ch_l "The ones who couldn't control their tempers."
                        $ LauraX.change_face("angry",0,Mouth="smile")
                        ch_l "Better for the girl who can heal to take the hits, right?"
                        menu:
                                extend ""
                                "That's terrible. I wish I could have protected you.":
                                        $ LauraX.change_face("smile",1)
                                        $ LauraX.change_stat("love", 200, 5)
                                        $ LauraX.change_stat("obedience", 90, 5)
                                        $ LauraX.change_stat("inhibition", 90, -5)
                                        ch_l "Thanks, but I was ok."
                                        $ LauraX.change_face("sadside",0)
                                        ch_l "I didn't deserve it, but I felt like I did at the time."
                                "You're strong to have made it out of there.":
                                        $ LauraX.change_face("smile",0)
                                        $ LauraX.change_stat("love", 200, 5)
                                        $ LauraX.change_stat("obedience", 90, 10)
                                        $ LauraX.change_stat("inhibition", 90, 5)
                                        ch_l "Thanks."
                                        ch_l "I didn't really think of it like that. . ."
                                        $ LauraX.change_face("sadside",0)
                                        ch_l "I just felt like I'd deserved it."
                                        ch_l "But I realized how wrong that was."
                                "Yeah, that makes sense.":
                                        $ LauraX.change_face("confused",1)
                                        $ LauraX.change_stat("love", 200, -5)
                                        $ LauraX.change_stat("obedience", 90, 15)
                                        $ LauraX.change_stat("inhibition", 90, -5)
                                        ch_l "Don't think before you speak, do you?"
                                        $ LauraX.change_face("sadside",0)
                                        ch_l "It wasn't right, I just didn't realize it at the time."
                        ch_l "Eventually I got past it and decided to get out of there."
                        ch_l "Not like they could stop me."
                        $ line = "NYX"

                if not line:
                        # Primary menu, falls through to this
                        menu:
                            extend ""
                            "What did you do back at the facility?" if "facility" not in Topics:
                                    $ LauraX.change_face("sadside",0)
                                    ch_l "After they tested what I could do, they put me to work."
                                    ch_l "Mainly, I killed people for them."
                                    $ Topics.append("facility")
                                    $ line = "facility"
                            "More about that facility. . ." if "facility" in Topics:
                                    $ line = "facility"

                            "Where did you go after you escaped?" if "NYX" not in Topics:
                                    $ LauraX.change_face("sadside",0)
                                    ch_l "I wandered in the wilderness for weeks."
                                    ch_l "Eventually I found my way to New York."
                                    ch_l "I lived on the streets for a few years."
                                    $ Topics.append("NYX")
                                    $ line = "NYX"
                            "More about after the escape. . ." if "NYX" in Topics:
                                    $ line = "NYX"

                            "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:
                                    $ LauraX.change_face("smile",0)
                                    $ LauraX.change_stat("love", 200, 10)
                                    $ LauraX.change_stat("obedience", 90, 3)
                                    $ LauraX.change_stat("inhibition", 90, 3)
                                    ch_l "Thanks for listening to me ramble."
                                    $ Topics.append("exit")
                            "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:
                                    $ LauraX.change_face("sadside",0, Mouth="smile")
                                    $ LauraX.change_stat("obedience", 90, 10)
                                    ch_l "Yeah, you get the idea."
                                    $ Topics.append("exit")
                            "I don't really care about that. [[exit]":
                                    $ LauraX.change_face("angry",0)
                                    $ LauraX.change_stat("love", 200, -15)
                                    $ LauraX.change_stat("obedience", 50, 5)
                                    $ LauraX.change_stat("obedience", 90, 10)
                                    $ LauraX.change_stat("inhibition", 90, -5)
                                    ch_l "Oh, I'm sorry if I was boring you with my life story."
                                    $ line = "angry"
                                    $ Topics.append("exit")

        #end while loop

        if line == "angry":
                $ LauraX.change_face("angry",0)
                ch_l "And here I was thinking that I meant something to you."
                ch_l "Well forget that!"
                $ line = 0
                $ LauraX.Event[6] = 23
                $ LauraX.recent_history.append("angry")
                $ LauraX.daily_history.append("angry")
                hide Laura_Sprite with easeoutright
                call remove_girl(LauraX)
                $ LauraX.location = "hold" #puts her off the board for the day
                return

        $ LauraX.change_face("bemused",0,Eyes="down")
        ch_l "I just thought you should know,"
        $ LauraX.change_face("smile",2)
        ch_l "I love you."
        menu:
                extend ""
                "I love you too!":
                    $ LauraX.change_face("smile",1)
                    $ LauraX.change_stat("love", 200, 20)
                    $ LauraX.change_stat("inhibition", 90, 5)
                    ch_l "For a second there you had me worried."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_love_End
                "I know.":
                    $ LauraX.change_face("smile",1)
                    $ LauraX.change_stat("love", 200, 10)
                    $ LauraX.change_stat("obedience", 90, 5)
                    $ LauraX.change_stat("inhibition", 90, 10)
                    $ LauraX.change_stat("lust", 90, 5)
                    ch_l "Smooth one. Seriously though, how about you?"
                "Neat?":
                    $ LauraX.change_face("confused",1)
                    $ LauraX.change_stat("obedience", 90, 5)
                    ch_l "I'm gonna need a bit more there, [LauraX.Petname]."
                "Huh.":
                    $ LauraX.change_face("confused",1)
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 90, 10)
                    ch_l "I'm not sure how to take that one."


        menu:
                extend ""
                "Oh, I love you too!":
                    $ LauraX.change_face("smile",1)
                    $ LauraX.change_stat("love", 200, 15)
                    $ LauraX.change_stat("obedience", 90, 5)
                    $ LauraX.change_stat("inhibition", 90, 5)
                    ch_l "For a second there you had me worried."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_love_End
                "I. . . love you back?":
                    $ LauraX.change_face("confused",1)
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_stat("obedience", 90, 10)
                    ch_l "Ok, I'll take it."
                    $ LauraX.Petnames.append("lover")
                    jump Laura_love_End
                "I mean, that's cool and all. . .":
                    $ LauraX.change_face("sadside",1)
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 90, 10)
                    $ LauraX.change_stat("inhibition", 90, -5)
                    ch_l ". . . but you don't love me back. Got it."
                "That's. . . uncomfortable.":
                    $ LauraX.change_face("angry",1)
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_stat("obedience", 90, 15)
                    $ LauraX.change_stat("inhibition", 90, -5)
                    ch_l "I don't like where this is heading."

        ch_l "What's your problem?"
        ch_l "Is it someone else?"
        $ line = 0
        menu:
                extend ""
                "Yes, it's [RogueX.name]." if RogueX in Shipping and Shipshape < 3:
                        $ line = RogueX
                "Yes, it's [KittyX.name]." if KittyX in Shipping and Shipshape < 3:
                        $ line = KittyX
                "Yes, it's [EmmaX.name]." if EmmaX in Shipping and Shipshape < 3:
                        $ line = EmmaX
                "Yes, it's the others" if Shipshape > 1:
                        $ LauraX.change_stat("obedience", 90, 15)
                        $ LauraX.change_stat("inhibition", 90, 5)
                        $ LauraX.change_stat("lust", 90, 5)
                        $ LauraX.change_face("sadside",1)
                        ch_l "Well, you do have your pick."
                "There's nobody else.":
                        $ LauraX.change_stat("love", 200, -15)
                        $ LauraX.change_stat("obedience", 90, 15)
                        $ LauraX.change_stat("inhibition", 90, 5)
                        $ LauraX.change_face("sad",1)
                        if ApprovalCheck(LauraX, 1000, "OI"):
                            ch_l "I guess that's something."
                        else:
                            ch_l ". . ."
                "It's a \"you\" problem.":
                        $ LauraX.change_face("angry")
                        $ LauraX.change_stat("love", 200, -25)
                        $ LauraX.change_stat("obedience", 90, 15)
                        ch_l "You're seriously messing with me?"
                        $ LauraX.change_stat("love", 200, -10)
                        ch_l "You don't want to see me when I'm angry."
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.daily_history.append("angry")


        if line:
                #If you called out a girl,
                if LauraX.GirlLikeCheck(line) >= 800:
                        $ LauraX.change_stat("love", 200, 5)
                        $ LauraX.change_stat("obedience", 90, 20)
                        $ LauraX.change_stat("inhibition", 90, 5)
                        $ LauraX.change_stat("lust", 90, 5)
                        $ LauraX.change_face("sadside",1)
                        ch_l "Yeah, I guess she's great."
                else:
                        $ LauraX.change_face("angry",Eyes="side")
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 90, 20)
                        ch_l "Bitch."
                        $ LauraX.recent_history.append("angry")
                        $ LauraX.GLG(line,800,-50,1)
        ch_l "Well, if that's the way you feel about it. . ."
        ch_l "I'll. . . see you later."
        ch_l "This. . . hurt."

label Laura_love_End:
        if "lover" not in LauraX.Petnames:
                $ LauraX.Event[6] = 20
                hide Laura_Sprite with easeoutright
                call remove_girl(LauraX)
                $ LauraX.location = "hold" #puts her off the board for the day
                return

        $ LauraX.Event[6] = 5
        "[LauraX.name] grabs you in a crushing hug."
        $ LauraX.change_stat("love", 200, 25)
        $ LauraX.change_stat("lust", 90, 5)
        $ LauraX.change_face("sly",1)
        ch_l "So. . . now that we have some free time. . ."
        $ LauraX.change_stat("lust", 90, 10)

        if not LauraX.Sex:
            $ LauraX.change_face("bemused",2)
            ch_l "I think I'm ready. . ."
        else:
            ch_l "Would you like to have some fun?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Yeah, let's do this. . . [[have sex]":
                    $ LauraX.change_stat("inhibition", 30, 20)
                    $ LauraX.change_stat("obedience", 70, 10)
                    ch_l "Hmm. . ."
                    call Laura_SexAct("sex")
                "I have something else in mind. . .[[choose another activity]":
                    $ LauraX.Brows = "confused"
                    $ LauraX.change_stat("obedience", 70, 25)
                    ch_l "Like what? . ."
                    $ temp_modifier = 20
                    call Laura_SexMenu
        return

label Laura_love_Redux:
         #this is for if you rejected her but want a second chance
        $ line = 0
        $ LauraX.daily_history.append("relationship")

        if LauraX.Event[6] >= 25:
                #if this is the second time through
                ch_p "I hope you've forgiven me, I still love you."
                $ LauraX.change_stat("love", 95, 10)
                if ApprovalCheck(LauraX, 950, "L"):
                    $ line = "love"
                else:
                    $ LauraX.change_face("angry")
                    ch_l "You're still working your way out of the hole, [LauraX.Petname]."
                    $ LauraX.Eyes="side"
                    ch_l ". . ."
                    $ LauraX.change_face("angry",Mouth="lipbite")
                    ch_l "But let me hear your pitch."
        elif LauraX.Event[6] >= 23:
                #if you pissed her off the first time
                ch_p "I was rude when you opened up to me before."
                $ LauraX.change_stat("love", 95, 10)
                if ApprovalCheck(LauraX, 950, "L"):
                    ch_l "And. . ."
                else:
                    $ LauraX.change_face("angry")
                    ch_l "You're still working your way out of the hole, [LauraX.Petname]."
                    $ LauraX.Eyes="side"
                    ch_l ". . ."
                    $ LauraX.change_face("angry",Mouth="lipbite")
                    ch_l "But let me hear your pitch."
        else:
                    ch_p "Remember when I told you that I didn't love you?"
                    $ LauraX.change_face("perplexed",1)
                    ch_l ". . ."
                    $ LauraX.change_face("angry", Eyes="side")
                    ch_l "How could I forget?"

        if line != "love":
                menu:
                    extend ""
                    "I'm sorry, I didn't mean it.":
                        $ LauraX.Eyes = "surprised"
                        ch_l "Oh really?"
                        ch_l "That's awfully convenient."
                        ch_p "Yeah. I mean, yes, I love you, [LauraX.name]."
                        $ LauraX.change_stat("love", 200, 10)
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ line = "love"
                        else:
                            $ LauraX.change_face("sadside")
                            ch_l "Well, maybe I don't, anymore. . ."
                    "I've changed my mind, I do love you, so. . .":
                        if ApprovalCheck(LauraX, 950, "L"):
                            $ line = "love"
                            ch_l "Well that's great."
                        else:
                            $ LauraX.Mouth = "sad"
                            ch_l "Good for you."
                            $ LauraX.change_stat("inhibition", 90, 10)
                            $ LauraX.change_face("sadside")
                            ch_l "I don't exactly have the same mind either. . ."
                    "Um, never mind.":
                            $ LauraX.change_stat("love", 200, -30)
                            $ LauraX.change_stat("obedience", 50, 10)
                            $ LauraX.change_face("angry")
                            ch_l "Oh, fuck you."
                            $ LauraX.recent_history.append("angry")
                            $ LauraX.daily_history.append("angry")
        if line == "love":
                $ LauraX.change_stat("love", 200, 40)
                $ LauraX.change_stat("obedience", 90, 10)
                $ LauraX.change_stat("inhibition", 90, 10)
                $ LauraX.change_face("smile")
                ch_l "I'm glad you came around."
                ch_l "I love you too, [LauraX.Petname]!"
                if LauraX.Event[6] < 25:
                        $ LauraX.change_face("sly")
                        "She grabs the back of your head and pulls you close."
                        ch_l "Next time, don't keep me waiting."
                $ LauraX.Petnames.append("lover")
        $ LauraX.Event[6] = 25
        return

label Laura_Sub:
    $ LauraX.DrainWord("asked meet")
    call shift_focus(LauraX)
    if LauraX.location != bg_current and LauraX not in Party:
        "Suddenly, [LauraX.name] shows up and says she needs to talk to you."

    $ LauraX.location = bg_current
    call set_the_scene(0)
    call Display_Girl(LauraX)
    call clear_the_room(LauraX)
    call set_the_scene
    call Taboo_Level
    $ LauraX.daily_history.append("relationship")
    $ LauraX.change_face("bemused", 1)

    $ line = 0
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
    $ LauraX.change_face("sly", 1,Eyes="side")
    ch_l "I don't know how I feel about that."
    if LauraX.Event[6]: #if you've done the love route
            $ LauraX.change_face("sadside", 1)
            ch_l "You know the past I've had, with the facility, with the. . . "
            ch_l ". . . work I had to do for them."
            $ LauraX.change_face("sad", 1)
            ch_l "I don't know if I want to let anyone tell me what to do like that again."
    menu Laura_Sub_Question:
        extend ""
        "I guess I can be demanding.":
                $ LauraX.change_face("sly", 1)
                $ LauraX.change_stat("obedience", 200, 10)
                $ LauraX.change_stat("inhibition", 50, 5)
        "Sorry. I didn't mean to come off like that.":
                $ LauraX.change_face("sly", 1)
                $ LauraX.change_stat("love", 80, 5)
                $ LauraX.change_stat("obedience", 200, -5)
                $ LauraX.change_stat("inhibition", 50, -5)
                ch_l "I get it, you're assertive. . ."
        "Remind me about the facility?" if LauraX.Event[6] and line != "facility":
                $ LauraX.change_face("sadside", 1)
                $ LauraX.change_stat("love", 99, -10)
                $ LauraX.change_stat("inhibition", 50, -5)
                ch_l "I told you, I was raised in an underground government lab."
                ch_l "They ordered me to kill people for them."
                $ LauraX.change_face("sly", 0, Brows= "angry")
                ch_l ". . . until I got tired of taking orders."
                $ line = "facility"
                jump Laura_Sub_Question
        "What bothers you about being told to do things?" if not LauraX.Event[6] and line != "facility":
                $ LauraX.change_face("sadside", 1)
                $ LauraX.change_stat("love", 80, 5)
                ch_l "I've just had some rough experiences."
                ch_l "You don't need to know about them."
                ch_l ". . ."
                $ LauraX.change_face("sad", 0)
                ch_l "Let's just say I was ordered to do some things I regret."
                $ line = "facility"
                jump Laura_Sub_Question
        "Get with the program.":
                if ApprovalCheck(LauraX, 1000, "LO"):
                        $ LauraX.change_face("sly", 1)
                        $ LauraX.change_stat("obedience", 200, 20)
                        $ LauraX.change_stat("inhibition", 50, 10)
                        ch_l "Hmmm. . ."
                else:
                        $ LauraX.change_stat("love", 200, -10)
                        $ LauraX.change_stat("inhibition", 50, -5)
                        $ LauraX.change_face("angry",0)
                        ch_l "You're not off to a good start here. You might want to rethink your attitude."
                        menu:
                            extend ""
                            "Sorry.  I thought that's what you were into.":
                                    $ LauraX.change_face("perplexed", 1,Eyes="side")
                                    $ LauraX.Eyes = "side"
                                    $ LauraX.change_stat("love", 75, 10)
                                    $ LauraX.change_stat("obedience", 200, 5)
                                    $ LauraX.change_stat("inhibition", 50, 5)
                                    ch_l ". . . after I just said. . ."
                                    $ LauraX.change_face("sly", 1)
                                    ch_l "Ok, whatever."
                            "I don't care.":
                                    $ LauraX.change_stat("love", 95, -10)
                                    ch_l "I guess not."
                                    $ line = "rude"
    if line == "facility":
            $ line = 0

    if not line:
            # She's advancing to the next stage
            $ LauraX.change_face("sly", 1)
            ch_l "Look, it's not like. . ."
            $ LauraX.change_face("sly", 2)
            ch_l ". . . it's not like I hate it."
            $ LauraX.change_face("smile", 1, Eyes="side")
            ch_l ". . . I actually think it might make me. . ."
            menu:
                extend ""
                "-excited?":
                    $ LauraX.change_stat("obedience", 200, 5)
                    $ LauraX.change_stat("inhibition", 50, 5)
                    ch_l ". . ."
                    $ LauraX.change_face("sly", 1)
                    $ LauraX.change_stat("lust", 50, 10)
                    ch_l "a little, yeah."
                "-digusted?":
                    $ LauraX.change_stat("love", 75, -5)
                    $ LauraX.change_stat("obedience", 200, -5)
                    $ LauraX.change_face("sadside", 1)
                    ch_l ". . . kind of,"
                    $ LauraX.change_face("sly", 1)
                    $ LauraX.change_stat("inhibition", 70, 5)
                    $ LauraX.change_stat("lust", 50, 5)
                    ch_l "but also kind of excited by it."
                "-hungry?":
                    $ LauraX.change_face("confused", 1,Eyes="surprised",Mouth="smile")
                    $ LauraX.change_stat("obedience", 200, -5)
                    $ LauraX.change_stat("inhibition", 50, -5)
                    ch_l "?!"
                    $ LauraX.change_face("confused", 1,Eyes="normal",Mouth="smile")
                    ch_l "Well. . . yeah? But not for-"
                    $ LauraX.change_face("sly", 1)
                    $ LauraX.change_stat("lust", 50, 5)
                    ch_l "I mean, it makes me kind of. . . excited."
                "-horny?":
                    $ LauraX.change_stat("obedience", 200, 10)
                    $ LauraX.change_stat("inhibition", 50, 5)
                    $ LauraX.change_face("startled", 2,Mouth="lipbite")
                    ch_l "!"
                    $ LauraX.change_face("sly", 1, Eyes="side")
                    $ LauraX.change_stat("inhibition", 50, 5)
                    $ LauraX.change_stat("lust", 50, 10)
                    $ LauraX.change_stat("lust", 70, 5)
                    ch_l "Yes."
            menu:
                extend ""
                "Good. If you wanna be with me, then you follow my orders.":
                        if ApprovalCheck(LauraX, 1000, "LO"):
                            $ LauraX.change_face("sly", 1)
                            $ LauraX.change_stat("obedience", 200, 15)
                            $ LauraX.change_stat("inhibition", 50, 10)
                            ch_l "Hmmm. . ."
                        else:
                            $ LauraX.change_face("sadside", 1,Mouth="normal")
                            $ LauraX.change_stat("love", 200, -5)
                            $ LauraX.change_stat("obedience", 200, 10)
                            ch_l "You might want to slow your roll there, [LauraX.Petname]."
                            menu:
                                extend ""
                                "Whatever. That's how it is. Take it or leave it.":
                                        $ LauraX.change_face("angry")
                                        $ LauraX.change_stat("love", 200, -10)
                                        $ LauraX.change_stat("obedience", 200, 5)
                                        ch_l "I think you're pushing it too far there, [LauraX.Petname]."
                                        $ line = "rude"
                                "Ok, just a little." :
                                        $ LauraX.change_face("bemused", 1)
                                        $ LauraX.change_stat("love", 95, 5)
                                        $ LauraX.change_stat("inhibition", 50, 5)
                                        ch_l "-but not too much."

                "Yeah? You think it's sexy?":
                                        $ LauraX.change_face("bemused", 2,Eyes="side")
                                        $ LauraX.change_stat("obedience", 200, 5)
                                        $ LauraX.change_stat("inhibition", 50, 10)
                                        ch_l ". . ."
                                        $ LauraX.change_stat("lust", 50, 5)
                                        ch_l "Yeah."

                "You sure you don't want me to back off a little?":
                        $ LauraX.change_face("startled", 1,Eyes="squint")
                        $ LauraX.change_stat("obedience", 200, -5)
                        menu:
                            ch_l "Well if you have to ask. . ."
                            "Only if you're okay with it.":
                                $ LauraX.change_face("bemused", 1)
                                $ LauraX.change_stat("love", 95, 10)
                                $ LauraX.change_stat("inhibition", 50, 10)
                                $ line = 0
                            "Uhm. . .yeah. I think it's weird.  Sorry.":
                                $ LauraX.change_face("sad", 1, Eyes="surprised")
                                $ LauraX.change_stat("love", 200, -15)
                                $ LauraX.change_stat("obedience", 200, -5)
                                $ LauraX.change_stat("inhibition", 50, -10)
                                $ line = "embarrassed"

                "I couldn't care less.":
                                $ LauraX.change_stat("love", 200, -10)
                                $ LauraX.change_stat("obedience", 200, 15)
                                $ LauraX.change_face("angry")
                                ch_l "I think you're pushing it too far there, [LauraX.Petname]."
                                $ line = "rude"

    if not line:
        $ LauraX.change_face("bemused", 1,Eyes = "down")
        ch_l "So, I'm willing to give this a shot."
        ch_l "Just a trial period, to see how it goes."
        ch_l "Just tell me what you want, and. . . I'll see about doing it."
        menu Laura_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                    $ LauraX.change_stat("obedience", 200, 5)
                    $ LauraX.change_stat("inhibition", 50, 5)
                    $ LauraX.change_face("sly", 1)
                    $ line = 0
            "Don't you think that relationship's kinda. . .weird?":
                    $ LauraX.change_face("sad", 1, Eyes="surprised")
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("inhibition", 50, -15)
                    $ line = "embarrassed"

    if not line:
        $ LauraX.change_face("smile", 1)
        ch_l "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ LauraX.change_stat("love", 95, 5)
                    $ LauraX.change_stat("obedience", 200, 15)
                    $ LauraX.change_stat("inhibition", 50, 5)
                    ch_l "Yes, sir."
                    $ LauraX.Petname = "sir"
            "That's kind of formal, isn't it?":
                $ LauraX.change_face("perplexed", 1)
                ch_l "Huh. ok, no problem"
                $ LauraX.change_stat("inhibition", 50, -5)
                $ LauraX.change_face("sly", 1,Eyes="side")
                menu:
                    ch_l "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                            $ LauraX.change_stat("obedience", 200, 10)
                            $ LauraX.change_face("smile", 1)
                            ch_l "Good."
                    "I don't feel comfortable with that. . .":
                            $ LauraX.change_face("sad", 1, Eyes="side")
                            $ LauraX.change_stat("love", 200, -10)
                            $ LauraX.change_stat("obedience", 200, -30)
                            $ LauraX.change_stat("inhibition", 50, -15)
                            $line = "embarrassed"

    $ LauraX.History.append("sir")
    if not line:
            $ LauraX.Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif line == "rude":
            call remove_girl(LauraX)
            if not simulation:
                    $ renpy.pop_call()
            "[LauraX.name] knocks her way past you and storms off."
    elif line == "embarrassed":
            $ LauraX.change_face("sadside", 2)
            ch_l "Huh, ok, if you're not interested. . .."
            hide Laura_Sprite with easeoutright
            call remove_girl(LauraX)
            if not simulation:
                    $ renpy.pop_call()
            "[LauraX.name] heads out of the room."
    return

label Laura_Sub_Asked:
    $ line = 0
    $ LauraX.change_face("sadside", 1)
    ch_l "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in LauraX.Petnames and ApprovalCheck(LauraX, 850, "O"):
                        #if this is asking about the "master" name, and her obedienceience is higher than 700
                        pass
                elif ApprovalCheck(LauraX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        $ LauraX.change_face("angry", 1)
                        ch_l "It was a bad idea, don't worry about it." #Failed again. :(
                        $ line = "rude"

                if line != "rude":
                        $ LauraX.change_stat("love", 90, 10)
                        $ LauraX.change_face("sly", 1)
                        ch_l "Well, it's not like you stopped ordering me around anyway."
                        ch_l "Ok, let's give it a shot."

        "I know it's what you want. Do you want to try again, or not?":
                $ LauraX.change_face("bemused", 1)
                if "sir" in LauraX.Petnames:
                    if ApprovalCheck(LauraX, 850, "O"):
                        ch_l "Ok, fine."
                    else:
                        ch_l "Nah, I'm good."
                        $ line = "rude"
                elif ApprovalCheck(LauraX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ LauraX.change_face("confused", 1)
                        ch_l "Kinda wishy-washy there."
                        $ LauraX.change_face("sly", 1)
                        ch_l "but maybe you're right."
                        ch_l "Are you sure you're into this?"
                        menu:
                            extend ""
                            "Yes, I'm sorry I was mean about it.":
                                            $ LauraX.change_stat("love", 90, 15)
                                            $ LauraX.change_stat("inhibition", 50, 10)
                                            $ LauraX.change_face("bemused", 1)
                                            $ LauraX.Eyes = "side"
                                            ch_l "Ok then."
                            "You're damned right I am, bitch.":
                                    if "sir" in LauraX.Petnames and ApprovalCheck(LauraX, 900, "O"):
                                            $ LauraX.change_stat("love", 200, -5)
                                            $ LauraX.change_stat("obedience", 200, 10)
                                            ch_l ". . ."
                                    elif ApprovalCheck(LauraX,700, "O"):
                                            $ LauraX.change_stat("love", 200, -5)
                                            $ LauraX.change_stat("obedience", 200, 10)
                                            ch_l "Hmmm. . ."
                                    else: #if it failed both those things,
                                            $ LauraX.change_stat("love", 200, -10)
                                            $ LauraX.change_stat("obedience", 90, -10)
                                            $ LauraX.change_stat("obedience", 200, -10)
                                            $ LauraX.change_stat("inhibition", 50, -15)
                                            $ LauraX.change_face("angry", 1)
                                            ch_l "Wow, that's pushing it."
                                            $ line = "rude"
                            "Ok, never mind then.":
                                            $ LauraX.change_face("angry", 1)
                                            $ LauraX.change_stat("love", 200, -10)
                                            $ LauraX.change_stat("obedience", 90, -10)
                                            $ LauraX.change_stat("obedience", 200, -10)
                                            $ LauraX.change_stat("inhibition", 50, -15)
                                            ch_l "I was thinking of taking orders from you, not mindgames."
                                            ch_l "I should've known you'd be like this."
                                            $ line = "rude"

    $ LauraX.recent_history.append("asked sub")
    $ LauraX.daily_history.append("asked sub")
    if line == "rude":
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Laura_Sprite with easeoutright
            call remove_girl(LauraX)
            $ LauraX.recent_history.append("angry")
            if not simulation:
                    $ renpy.pop_call()
            "[LauraX.name] checks you as she stomps out of the room."
    elif "sir" in LauraX.Petnames:
            #it didn't fail and "sir" was covered
            $ LauraX.change_stat("obedience", 200, 50)
            $ LauraX.Petnames.append("master")
            $ LauraX.Petname = "master"
            $ LauraX.Eyes = "sly"
            ch_l ". . . master. . ."
    else:
            #it didn't fail
            $ LauraX.change_stat("obedience", 200, 30)
            $ LauraX.Petnames.append("sir")
            $ LauraX.Petname = "sir"
            $ LauraX.change_face("sly", 1)
            ch_l ". . . sir."
    return

label Laura_Master:
    $ LauraX.DrainWord("asked meet")
    call shift_focus(LauraX)
    if LauraX.location != bg_current and LauraX not in Party:
        "Suddenly, [LauraX.name] shows up and says she needs to talk to you."

    $ LauraX.location = bg_current
    call set_the_scene(0)
    call Display_Girl(LauraX)
    call clear_the_room(LauraX)
    call set_the_scene
    $ LauraX.daily_history.append("relationship")
    call Taboo_Level
    $ line = 0
    $ LauraX.change_face("sly", 1)
    ch_l "[LauraX.Petname]. . ."
    ch_l ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            $ LauraX.change_stat("obedience", 200, 5)
            $ LauraX.change_stat("inhibition", 50, 5)
        "What?":
            ch_l "I was asking if I could talk to you about something. . ."
            $ LauraX.Eyes = "side"
            ch_l ". . . personal."
            $ LauraX.Eyes = "squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ LauraX.change_stat("love", 80, 5)
                    $ LauraX.change_stat("obedience", 200, 5)
                    ch_l "Right. . ."
                "Oh, then no.":
                    $ LauraX.change_face("sad", 1)
                    $ LauraX.change_stat("love", 80, -5)
                    $ LauraX.change_stat("obedience", 200, -10)
                    $ line = "embarrassed"
        "No.":
            $ LauraX.change_face("perplexed", 1,Brows="confused")
            $ LauraX.change_stat("love", 80, -5)
            $ LauraX.change_stat("obedience", 200, -5)
            $ LauraX.change_stat("inhibition", 50, -5)
            ch_l "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ LauraX.change_face("confused", 1)
                    $ LauraX.change_stat("obedience", 200, 10)
                    $ LauraX.change_stat("inhibition", 60, 10)
                    ch_l "Right. . ."
                "Yes, not interested.":
                    $ LauraX.change_face("sad", 1)
                    $ LauraX.change_stat("love", 80, -5)
                    $ LauraX.change_stat("inhibition", 50, -10)
                    $ line = "embarrassed"


    if not line:
        $ LauraX.change_face("sly", 1)
        ch_l "I think I enjoy having you in charge."
        ch_l "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                    $ LauraX.change_face("sly", 1)
                    $ LauraX.change_stat("obedience", 200, 5)
                    ch_l "Good. Maybe we could take this a bit more seriously?"
                    menu:
                        extend ""
                        "Nah. This is just about perfect.":
                                $ LauraX.change_face("sad", 1)
                                $ LauraX.change_stat("obedience", 200, -15)
                                $ LauraX.change_stat("love", 80, 10)
                                $ line = "fail"
                        "What'd you have in mind?":
                                $ LauraX.Eyes = "side"
                                ch_l "I was thinking I could start calling you. . . {i}master{/i}?"
                                $ LauraX.Eyes = "squint"
                                menu:
                                    extend ""
                                    "Oh, yeah.  I'd like that.":
                                            $ LauraX.change_stat("obedience", 200, 5)
                                            ch_l "Good. . ."
                                    "Um. . .nah.  That's too much.":
                                            $ LauraX.change_face("sadside", 1)
                                            $ LauraX.change_stat("obedience", 200, -15)
                                            $ LauraX.change_stat("inhibition", 50, 5)
                                            $ line = "fail"

                        "Actually, I'd prefer we stopped doing it. Too much pressure.":
                                $ LauraX.change_face("sad", 1)
                                $ LauraX.change_stat("love", 200, -5)
                                $ LauraX.change_stat("obedience", 200, -10)
                                $ LauraX.change_stat("inhibition", 50, 15)
                                $ line = "fail"

                        "Actually, let's stop that. It's creeping me out.":
                                $ LauraX.change_face("angry", 2, Eyes="surprised")
                                $ LauraX.change_stat("love", 200, -10)
                                $ LauraX.change_stat("obedience", 200, -50)
                                $ LauraX.change_stat("inhibition", 50, -15)
                                ch_l "Say no more, I wouldn't want to CREEP YOU OUT."
                                $ line = "embarrassed"

            "As if I care what you think, slut.":
                    $ LauraX.change_face("angry", 1, Mouth="smile")
                    $ LauraX.change_stat("love", 90, -20)
                    $ LauraX.change_stat("obedience", 200, 10)
                    $ LauraX.change_stat("inhibition", 50, -10)
                    ch_l ". . ."
                    menu:
                        ch_l "Excuse me?"
                        "Sorry. I just don't care what you want.":
                                if ApprovalCheck(LauraX, 1400, "LO"):
                                        $ LauraX.change_stat("obedience", 200, 10)
                                        ch_l ". . ."
                                        $ LauraX.change_face("sly", 1)
                                        $ LauraX.change_stat("love", 200, 20)
                                        $ LauraX.change_stat("inhibition", 50, 15)
                                        ch_l ". . .{i}go on. . .{/i}"
                                else:
                                        $ LauraX.change_stat("love", 200, -15)
                                        $ LauraX.change_stat("obedience", 200, -10)
                                        $ LauraX.change_stat("inhibition", 50, 5)
                                        $ LauraX.change_face("angry", 1)
                                        ch_l "!!!"
                                        $ line = "rude"

                        "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                                $ LauraX.change_stat("love", 200, 10)
                                $ LauraX.change_stat("obedience", 200, 10)
                                $ LauraX.change_stat("inhibition", 50, 5)
                                if ApprovalCheck(LauraX, 1400, "LO"):
                                        $ LauraX.change_stat("obedience", 200, 10)
                                        ch_l ". . ."
                                        $ LauraX.change_face("sly", 1)
                                        $ LauraX.change_stat("love", 200, 20)
                                        $ LauraX.change_stat("inhibition", 50, 15)
                                        ch_l ". . .{i}no, about right. . .{/i}"
                                else:
                                        $ LauraX.change_stat("love", 200, 5)
                                        $ LauraX.change_stat("obedience", 200, -5)
                                        $ LauraX.change_stat("inhibition", 50, 5)
                                        $ LauraX.change_face("angry", 1, Eyes="side")
                                        ch_l ". . ."
                                        ch_l "We'll work on it. . ."

            "I don't really like it. Too much pressure.":
                                $ LauraX.change_face("sad", 2)
                                $ LauraX.change_stat("love", 200, -20)
                                $ LauraX.change_stat("obedience", 200, -20)
                                $ LauraX.change_stat("inhibition", 50, -10)
                                $ line = "embarrassed"

    $ LauraX.History.append("master")
    if line == "rude":
            $ LauraX.recent_history.append("angry")
            hide Laura_Sprite with easeoutright
            call remove_girl(LauraX)
            if not simulation:
                    $ renpy.pop_call()
            "[LauraX.name] stomps out of the room."
    elif line == "embarrassed":
            ch_l "Ok, fine then."
            ch_l "And here I was, about to \"elevate your clearance.\""
            hide Laura_Sprite with easeoutright
            call remove_girl(LauraX)
            if not simulation:
                    $ renpy.pop_call()
            "[LauraX.name] brushes past you on her way out."
    elif line == "fail":
            ch_l "Oh. . ."
            ch_l "I guess that's fine."
    else:
            $ LauraX.change_stat("obedience", 200, 50)
            $ LauraX.Petnames.append("master")
            $ LauraX.Petname = "master"
            ch_l ". . .master."
    return

label Laura_Sexfriend:   #Laura_Update
        #set this to occur after class
        $ LauraX.lust = 70
        $ LauraX.location = bg_current
        $ LauraX.DrainWord("asked meet")
        call set_the_scene
        $ LauraX.daily_history.append("relationship")
        call Taboo_Level
        $ line = 0
        $ LauraX.change_face("sly",2,Eyes="side")
        "[LauraX.name] approaches you and pulls you aside. She seems to be shivering a little bit."
        "She seems to be squirming around and rubbing her thighs together."
        $ LauraX.Petnames.append("sex friend")
        $ LauraX.change_face("sly",2)
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
                        $ LauraX.change_face("sly",2,Mouth="smile")
                        $line = "yes"
                    "No thanks":
                        $ LauraX.change_face("confused",2)
                        $line = "no"
                    ". . .":
                        $ LauraX.change_stat("obedience", 90, 5)
                        $ LauraX.change_face("confused",2)

                if not line:
                        ch_l "Now, if at all possible. . ."
                        menu:
                            extend ""
                            "Sure":
                                $ LauraX.change_face("sly",2,Mouth="smile")
                                $line = "yes"
                            "No thanks":
                                $ LauraX.change_face("confused",2)
                                $line = "no"

                if line == "no":
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 80, 5)
                    ch_l "What? Why not?"
                    menu:
                        extend ""
                        "Ok, fine":
                            $ LauraX.change_face("confused",2,Mouth="smile")
                            ch_l "love the enthusiasm."
                            $line = "yes"
                        "Not interested":
                            $ LauraX.change_face("confused",2)

                        "There's someone else":
                            $ LauraX.change_stat("love", 95, -5)
                            $ LauraX.change_stat("obedience", 90, 5)
                            if Player.Harem:
                                    $ LauraX.change_face("surprised",2)
                                    ch_l "Oh, [Player.Harem[0].name]?"
                                    $ LauraX.GLG(Player.Harem[0],600,-25,1)
                            $ LauraX.change_face("sly",2)
                            ch_l "Well, she doesn't need to know about it. . ."
                            menu:
                                extend ""
                                "Ok, fine":
                                        ch_l "love the enthusiasm."
                                        $ line = "yes"
                                "Still no":
                                        pass

        if line == "no":
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_stat("obedience", 90, 15)
                    $ LauraX.change_stat("inhibition", 90, 10)
                    $ LauraX.change_face("sad",2)
                    ch_l "Really?"
                    ch_l "Bummer."
                    ch_l "Well let me know if you change your mind."
                    $ LauraX.change_face("sadside",2,Mouth="lipbite",Brows="angry")
                    if Player.Harem:
                            ch_l "Wonder if [Player.Harem[0].name]'s busy. . ."
                            $ LauraX.GLG(Player.Harem[0],500,25,1)
                    else:
                            ch_l "Wonder if Kitty's busy. . ."
                            $ LauraX.GLG("Kitty",500,25,1)
        else:
                $ LauraX.change_stat("love", 90, 10)
                $ LauraX.change_stat("obedience", 90, 5)
                $ LauraX.change_stat("inhibition", 90, 15)
                $ LauraX.change_face("sly",1,Mouth="smile")
                if Taboo:
                    ch_l "Wanna take this party someplace else?"
                    menu:
                        extend ""
                        "Yeah":
                                ch_l "Sure, let's go."
                                if bg_current == "bg_player":
                                        $ bg_current = "bg_laura"
                                else:
                                        $ bg_current = "bg_player"
                                $ LauraX.location = bg_current
                                call clear_the_room(LauraX)
                                call set_the_scene
                                $ Taboo = 0
                                $ LauraX.Taboo = 0

                        "No, let's do it here.":
                                $ LauraX.change_stat("obedience", 80, 5)
                                $ LauraX.change_stat("inhibition", 90, 15)
                                ch_l "Kinky."

                $ action_context = LauraX
                $ Player.AddWord(1,"interruption") #adds to Recent
                call Laura_SexPrep              #she offers sex
                call Laura_SexMenu

                #end "if no relationship"
        return

label Laura_Fuckbuddy:
        $ LauraX.daily_history.append("relationship")
        $ LauraX.lust = 80
        $ LauraX.DrainWord("asked meet")
        # Conditions, in your room, laura not there.
        "You hear a knock on the door, and go to answer it."
        #change laura's outfit to default
        $ LauraX.location = bg_current
        call shift_focus(LauraX)
        call set_the_scene(0)
        $ LauraX.Outfit = "casual1"
        $ LauraX.OutfitDay = "casual1"
        $ LauraX.OutfitChange("casual1")
        call Display_Girl(LauraX)
        call Taboo_Level
        $ primary_action = "masturbation"
        $ primary_action3 = "fondle_pussy"
        $ LauraX.change_face("sly",2,Mouth="lipbite")
        "[LauraX.name] is standing in the doorway, with her hand down her pants."
        "You can tell she's been masturbating furiously, her scent is overpowering."
        $ primary_action = 0
        $ primary_action3 = 0
        $ LauraX.ArmPose = 1
        "She looks you up and down hungrily, and pulls her hand out of her pants."
        "She reaches up to caress your face, smearing her juices along it."
        ch_l "Mine."
        $ LauraX.Petnames.append("fuck buddy")
        $ LauraX.Event[10] += 1

        $ action_context = LauraX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call Laura_SexPrep              #she offers sex
        call Laura_SexMenu
        return

label Gwentro:
        $ Player.AddWord(1,"interruption") #adds to Recent
        if Taboo > 5 or RogueX.location == bg_current or KittyX.location == bg_current or EmmaX.location == bg_current:
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
        $ action_speed = 0
        $ LauraX.change_face("surprised",2,Eyes="side")
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
        $ LauraX.change_face("confused",2,Eyes="side")
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
        $ LauraX.change_face("angry",1,Eyes="side")
        show Gwen_Sprite:
            ypos 50
        ch_g "So now that we've got that taken care of, what's your name?{w=0.2}{nw}"
        call GwenFace("shocked",0)
        menu:
            ch_g "So now that we've got that taken care of, what's your name?{nw}"
            "[Player.name]":
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
            "[Player.name]":
                ch_p "It's [Player.name]."
                ch_g "Hi, [Player.name], my name's Gwen!"
                $ GwenName = "Gwen"
            "None of your buisiness":
                ch_p "It's none of your business."
                ch_g "Well, it looks like your name is [Player.name]."
                ch_g "I could tell from the menu."
                ch_g "Mine's Gwen, b-t-dubs."
            "Who are you?":
                ch_p "Never mind me, who are you?!"
                ch_g "Oh! That's fair, I'm new around here. My name's Gwen!"
                ch_g "And it looks like your name is [Player.name]."
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
        $ LauraX.change_face("angry",Eyes="leftside")
        ch_g "Sorry, I should have said hello earlier, hey Laura!"
        $ LauraX.change_face("confused",Eyes="leftside")
        ch_l "How do you know my name!"
        ch_g "I've read all about you! Or do you prefer \"X-23?\""
        ch_g "Or \"Wolverine?\""
        call GwenFace("surprised",Mouth="kiss")
        ch_g "God, it's not \"Talon,\" is it?"
        call GwenFace("smile")
        ch_l "[LauraX.name] - is - fine."
        call GwenFace("smile",Mouth="kiss")
        ch_g "Cool, so. . ."
        menu:
            "What are you doing here?":
                ch_p "What are you doing here?"
                ch_g "I had a feeling you would ask that."
            "Some other irrelvant option.":
                ch_p "What are you doing here?"
                ch_g "Man, determinism, am I right?"
        $ LauraX.change_face("confused",Eyes="leftside")
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
        $ LauraX.change_face("angry",Eyes="leftside")
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
        $ LauraX.change_face("bemused",Eyes="sexy")
        ch_l "Now, what were were doing. . ."

        return

label Laura_Dressup:
        #(Condition: X23 has returned to school)
        #(location: campus square)
        $ active_Girls.append(LauraX) if LauraX not in active_Girls else active_Girls
        call shift_focus(LauraX)
        $ bg_current = "bg_campus"
        call remove_girl("all")
        $ LauraX.location = bg_current
        call set_the_scene(0)

        $ LauraX.Outfit = "casual1"
        $ LauraX.OutfitChange("casual1")
        show Laura_Sprite at sprite_location(LauraX.sprite_location) with vpunch
        $ Round -= 10 if Round >= 11 else Round
        $ LauraX.History.remove("dress0")
        $ LauraX.History.append("dress1")
        $ LauraX.History.append("met")
        "As you're heading across the square, you bump into [LauraX.name]."
        $ LauraX.change_face("normal")
        ch_l "Oh, hey."
        menu:
            extend ""
            "Ah, [LauraX.name]. You're back!":
                    $ LauraX.change_stat("love", 50, 3)
                    $ LauraX.change_stat("obedience", 50, 1)
                    ch_l "Yeah, just got back."
            "Hey.":
                    ch_l "Yeah, just got back."
            "Who are you again?":
                    $ LauraX.change_stat("love", 70, -3)
                    $ LauraX.change_stat("obedience", 80, 5)
                    $ LauraX.change_face("confused")
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
                    $ LauraX.change_stat("love", 70, -1)
                    $ LauraX.change_stat("obedience", 80, 5)
                    $ LauraX.change_stat("inhibition", 80, 5)
                    $ LauraX.change_face("bemused")
                    ch_l "Not really."

        hide Laura_Sprite with easeoutright
        call remove_girl(LauraX)
        "[LauraX.name] walks away, and as you watch her go you feel a tap on your shoulder."

        call shift_focus(KittyX)
        $ KittyX.location = bg_current
        call set_the_scene(0)
        $ KittyX.Outfit = KittyX.OutfitDay
        $ KittyX.OutfitChange()
        call Display_Girl(KittyX)

        $ KittyX.change_face("smile")
        ch_k "Hey, [KittyX.Petname], what're you staring at?"
        #add Kitty arrving here

        menu:
            extend ""
            "Hey, [KittyX.name]. I was just talking to [LauraX.name].":
                    ch_k "Oh, she's back?"
            "Oh, nothing.":
                    ch_k "Oh, I see, [LauraX.name]."
                    ch_k "She's back?"
            "I was checking out that fine piece over there.":
                if ApprovalCheck(KittyX,1200,"LO") or KittyX.Les >= 10:
                        $ KittyX.change_stat("obedience", 80, 5)
                        $ KittyX.change_stat("inhibition", 80, 5)
                        $ KittyX.change_face("bemused",1)
                        ch_k "I guess I can't blame you. . ."
                else:
                        $ KittyX.change_stat("love", 70, -5)
                        $ KittyX.change_stat("obedience", 80, 10)
                        $ KittyX.change_stat("inhibition", 80, 5)
                        $ KittyX.change_face("angry")
                        ch_k "Rude much?"

        $ KittyX.change_face("smile",Eyes="side")
        ch_k "She's never around very much, you know."
        ch_k "Must get it from Logan."

        menu:
            extend ""
            "Oh, they're related?":
                    ch_k "Yeah, she's his daughter or something? I'm not too sure."
            "She's his clone, right?":
                    ch_k "I guess? I'm not too sure."
        "She shrugs, but then grins mischieviously."

        $ KittyX.change_face("sly")
        ch_k "Actually, we were thinking of giving her a \"welcome home\" present."
        ch_k "You wanna chip in?"

        menu:
            extend ""
            "Sure, why not?":
                    $ KittyX.change_stat("love", 50, 5)
                    $ KittyX.change_stat("obedience", 40, 5)
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
                    $ KittyX.change_stat("love", 80, 5)
                    $ KittyX.change_stat("inhibition", 40, 3)
                    $ KittyX.change_face("smile",1)
                    ch_k "Sweet talker."
            "That sounds good.":
                    $ KittyX.change_stat("love", 60, 2)
            "With your fashion sense? That'll end well.":
                    $ KittyX.change_stat("love", 70, -5)
                    $ KittyX.change_stat("obedience", 80, 5)
                    $ KittyX.change_stat("inhibition", 80, -3)
                    $ KittyX.change_face("angry")
        ch_k "Anyway, we were thinking around $10 each."

        menu:
            extend ""
            "Here you go." if Player.Cash >= 10:
                    $ KittyX.change_stat("love", 70, 1)
                    $ KittyX.change_stat("obedience", 40, 2)
                    ch_k "Nice."
                    $ Player.Cash -= 10
                    $ LauraX.History.append("dress2")
            "I don't have enough. . ." if Player.Cash < 10:
                    $ KittyX.change_stat("love", 70, 1)
                    $ KittyX.change_stat("obedience", 40, 2)
                    $ KittyX.change_face("normal",1,Brows="surprised",Mouth="sad")
                    ch_k "Oh."
                    ch_k "We aren't in a rush or anything. If you still want to, just hit me up."
            "You know what, never mind.":
                    $ KittyX.change_stat("love", 70, -2)
                    $ KittyX.change_stat("obedience", 40, -1)
                    $ KittyX.change_face("normal",1,Brows="surprised",Mouth="sad")
                    ch_k "Oh, ok."
        return

label Laura_Dressup2:
        ch_p "Hey, remember that gift you wanted to give [LauraX.name] earlier?"
        $ KittyX.change_face("smile")
        ch_k "Yeah?"
        menu:
            extend ""
            "Here you go, $10.":
                    $ KittyX.change_stat("love", 70, 1)
                    $ KittyX.change_stat("obedience", 40, 2)
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

        "You're walking past [KittyX.name]'s door when you hear her laughing at something."
        "You hear someone else's voice, there's clearly someone else in her room with her."

        ch_l "[KittyX.name], you shouldn't have."
        ch_l "No, seriously. . ."
        ch_l "you shouldn't have."
        ch_k "Aww, c'mon. You look great."

        "You remember [KittyX.name] talking about getting [LauraX.name] some new clothes. She must've gotten [LauraX.name] to try them on."
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
                    ch_p "Hey, [KittyX.name], what's going on?"
                    ch_k "Hey, [KittyX.Petname]! Come on in!"

                    call clear_the_room("all",0,1)
                    call shift_focus(LauraX)
                    $ KittyX.location = "bg_kitty"
                    $ LauraX.location = "bg_kitty"
                    call set_the_scene(Dress=0)

                    $ LauraX.change_face("sad",2,Eyes="squint",Brows="confused")
                    "[LauraX.name] stares at you, her eyes narrowed. She's clearly on edge."
                    $ LauraX.change_face("sad",2,Brows="confused",Eyes="leftside")
                    ch_l "Didn't you lock the door?"
                    if KittyX.Sleep < 5:
                            $ KittyX.change_face("smile",Eyes="side")
                            ch_k "Yeah, but I gave him a key."
                            $ LauraX.change_face("sad",1,Brows="confused",Eyes="leftside")
                            ch_l "You. . . gave him a key?"
                    else:
                            # you probably stole it from Xavier
                            $ KittyX.change_face("confused",Eyes="side")
                            ch_k "Yeah, I'm not really sure how he got a key. . ."
                            if not ApprovalCheck(KittyX,1200):
                                    #if she doesn't like you a lot yet. . .
                                    $ KittyX.change_face("angry",1)
                                    ch_k "Ok, that's enough, out, out!"
                                    "You head back out."
                                    return
                            $ KittyX.change_face("smile")
                            ch_k "I guess it's fine though. . ."
                            $ LauraX.change_face("sad",1,Brows="confused",Eyes="leftside")
                            ch_l "It's fine that he got a mystery key?"
                    $ KittyX.change_face("smile",1)
                    ch_k "Uh-huh. I mean, he's my [KittyX.Petname]."
                    ch_l "Your. . . [KittyX.Petname]."
            "Knock":
                    "You knock on the door."
                    ch_k "Who is it?"
                    ch_p "It's [Player.name], mind if I come in?"
                    if not ApprovalCheck(KittyX, 1000):
                            ch_k "Um, sorry [KittyX.Petname], we're a little busy in here."
                            ch_k "[KittyX.Like]maybe check back later?"
                            ch_p "Sure, no problem."
                            "You head back out."
                            return
                    ch_k "Sure, [KittyX.Petname]! Gimme a sec!"
                    "[KittyX.name] unlocks the door and it swings open."

                    call clear_the_room("all",0,1)
                    call shift_focus(LauraX)
                    $ KittyX.location = "bg_kitty"
                    $ LauraX.location = "bg_kitty"
                    call set_the_scene(Dress=0)

                    $ LauraX.change_face("sad",2,Brows="surprised")
                    "[LauraX.name] stares at you, as if she's not sure what she's seeing."
                    $ LauraX.change_face("sad",2,Brows="confused",Eyes="leftside")
                    ch_l "So you just let him come into your room whenever?"
                    $ KittyX.change_face("smile",1)
                    ch_k "Uh-huh. I mean, he's my [KittyX.Petname]."
                    ch_l "Your. . . [KittyX.Petname]."

            "Walk away":
                "Nah, I should let them have their girl time."
                return
        $ LauraX.SeenPanties = 1
        $ LauraX.change_face("angry",1,Eyes="closed")
        "She shakes her head, trying to absorb all this new information."
        "She mutters to herself."
        ch_l "I've been gone longer than I thought. . ."
        $ LauraX.change_face("sad",1,Brows="confused",Eyes="leftside")
        ch_l "So why's he here?"
        $ KittyX.change_face("smile",Eyes="side")
        ch_k "Well, he kind of pitched in to get you this stuff, so why not see what he thinks?"
        "[KittyX.name] walks over and poses like she's presenting [LauraX.name] as a model."
        $ KittyX.ArmPose = 2
        $ KittyX.change_face("smile")
        ch_k "So, what do you think?"

        menu:
            extend ""
            "Her outfit looks familiar. . .":
                    ch_k "I call it the Logan Look."
                    $ LauraX.change_face("sad",2,Eyes="stunned")
                    $ LauraX.change_stat("inhibition", 40, -2)
                    ch_l "Please don't call it that."
            "Looking good, [LauraX.name]!":
                    $ LauraX.change_stat("love", 70, 5)
                    $ LauraX.change_stat("obedience", 40, 3)
                    $ LauraX.change_stat("inhibition", 40, 5)
                    $ LauraX.GLG(KittyX,700,5,1)
                    $ LauraX.change_face("sadside",1)
                    ch_l "Yeah, well. . . [KittyX.name] knows her stuff."
                    $ KittyX.change_stat("love", 70, 1)
                    $ KittyX.change_stat("obedience", 40, 3)
                    $ KittyX.GLG(LauraX,700,3,1)
                    ch_k "Heh, thanks."
            "Great ensemble, [KittyX.name]! It looks great on her!":
                    $ KittyX.change_stat("love", 70, 5)
                    $ KittyX.change_stat("obedience", 40, 3)
                    ch_k "Hey, I know my stuff, y'know?"
                    $ LauraX.change_stat("love", 70, 3)
                    $ LauraX.change_stat("obedience", 40, 2)
                    $ LauraX.change_stat("inhibition", 40, 5)
                    $ LauraX.change_face("bemused",1)
                    $ LauraX.GLG(KittyX,700,3,1)
                    ch_l "Yeah, I guess she does. . ."
            "Can I get a refund?":
                    $ KittyX.change_stat("love", 70, -5)
                    $ KittyX.change_stat("obedience", 40, -3)
                    $ KittyX.change_face("angry")
                    ch_k "Way to bring down the mood."
                    $ LauraX.change_stat("love", 70, -5)
                    $ LauraX.change_stat("obedience", 40, 5)
                    $ LauraX.change_stat("inhibition", 40, -5)
                    $ LauraX.change_face("angry")
                    ch_l "Seriously."

        $ LauraX.change_face("smile",0,Eyes="leftside")
        $ LauraX.GLG(KittyX,700,5,1)
        $ KittyX.GLG(LauraX,700,5,1)
        ch_l "But really, [KittyX.name], thanks for this."
        $ KittyX.change_face("smile",Eyes="side")
        ch_k "No problem! Like, what're friends for?"
        ch_l "Pretty sure friends don't normally use their friends as dressup dolls."
        ch_k "Oh, [LauraX.name], you have sooooo much to learn."
        $ LauraX.change_face("smile",Eyes="down")
        "[LauraX.name] smiles just a little bit and looks down at herself."
        ch_l "I think wearing the whole outfit is a bit much."
        $ LauraX.change_face("smile",Eyes="leftside")
        ch_l "You know that Logan's going to have a few words if he sees me like this."
        $ KittyX.change_face("smile",Eyes="side")
        ch_k "Hey, it's your outfit now. Mix-and-match, girl!"
        ch_l "Yeah. Yeah, I think I'll do that."
        $ LauraX.names.append("Wolverine")

        $ KittyX.change_face("smile")
        $ LauraX.change_face("sly",1)
        "[LauraX.name] fixes you with a steely gaze."

        ch_l "So. . . I'd like to change now."

        menu:
            extend ""
            "Go right ahead!":
                    $ LauraX.change_stat("obedience", 40, 3)
                    $ LauraX.change_stat("inhibition", 40, 3)
                    if (not LauraX.SeenChest or not LauraX.SeenPussy) and not ApprovalCheck(LauraX,1400):
                            $ LauraX.change_stat("love", 70, -5)
                            $ LauraX.change_face("angry",1)
                            ch_l "I don't think so."
                            ch_k "Yeah, I think you'd better get going, [KittyX.Petname]. . ."
                            ch_k ". . .Before she does to you what Logan does to people who make him mad."
                            "[KittyX.name] firmly escorts you to the door."
                    else:
                        if LauraX.SeenChest and LauraX.SeenPussy:
                                ch_l "Fair enough. . ."
                        elif ApprovalCheck(LauraX,1400):
                                ch_l "Bold choice. . ."
                        $ KittyX.change_face("surprised",2,Eyes="side")
                        $ LauraX.Chest = 0
                        "[LauraX.name] starts stripping out of the new clothes. . ."
                        if ApprovalCheck(KittyX,1200):
                                $ KittyX.change_face("sly",1)
                        else:
                                $ KittyX.change_face("angry",1,Eyes="side")

                        $ LauraX.Panties = 0
                        call Laura_First_Topless
                        call Laura_First_Bottomless(1)
                        pause 1
                        $ LauraX.OutfitChange(LauraX.OutfitDay,Changed=1)
                        "And then puts on her usual outfit."

                        if ApprovalCheck(KittyX,1200):
                                $ KittyX.change_face("sly",1)
                        else:
                                $ KittyX.change_face("angry",1)
                        ch_k "Well, I guess you got your show for the day."
                        ch_k "Now give us some girl time."
                        "[KittyX.name] shoos you out of the room and you head to the Campus square."

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
        $ LauraX.change_face("sad",1)
        if LauraX.location == bg_current or LauraX in Party:
                "[LauraX.name] glances over at you with a distressed look."
        else:
                "[LauraX.name] turns a corner and notices you."
        if bg_current != "bg_laura" and bg_current != "bg_player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg_laura"
        $ LauraX.location = bg_current
        call set_the_scene
        call clear_the_room(LauraX)
        call set_the_scene
        call Taboo_Level
        ch_l "Hey. . ."
        ch_l "[LauraX.Petname]. . ."
        ch_l "About that time at the party. . ."
        menu:
            extend ""
            "What time at the party?":
                    $ LauraX.change_stat("love", 90, -2)
                    $ LauraX.change_stat("obedience", 80, 2)
                    $ LauraX.change_stat("inhibition", 60, 1)
                    $ LauraX.change_face("confused",2)
            "Oh, yeah. I'm sorry about that.":
                    $ LauraX.change_stat("love", 80, 5)
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_face("surprised",2)
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                    $ LauraX.change_face("smile",1)
            "Yeah?":
                    $ LauraX.change_stat("obedience", 50, 1)
                    $ LauraX.change_stat("inhibition", 60, 1)
                    $ LauraX.change_face("sad",1)
            ". . .":
                    $ LauraX.change_stat("love", 80, -1)
                    $ LauraX.change_stat("obedience", 50, 2)
                    $ LauraX.change_face("sad",1)

        if "sorry" not in LauraX.recent_history:
                    #if you didn't apologize in first response
                    $ LauraX.change_face("sadside",1)
                    ch_l "We were at the Halloween Party. . ."
                    $ LauraX.change_face("sad",1)
                    ch_l "And you said something about my costume. . ."
                    menu:
                        extend ""
                        "I don't remember, what did I say?":
                                $ LauraX.change_stat("love", 99, -3)
                                $ LauraX.change_face("surprised",1)
                        "Oh, yeah. I'm sorry about that.":
                                $ LauraX.change_face("smile",1)
                                $ LauraX.change_stat("love", 80, 5)
                                $ LauraX.change_stat("love", 200, 5)
                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                        "Did I?":
                                $ LauraX.change_face("surprised",1)
                                ch_l ". . ."
                                $ LauraX.change_stat("love", 99, -5)
                                $ LauraX.change_stat("obedience", 70, 3)
                                $ LauraX.change_stat("obedience", 90, 2)
                                $ LauraX.change_face("angry",1)
                        ". . .":
                                $ LauraX.change_stat("love", 99, -1)
                                $ LauraX.change_face("angry",1)

        if "sorry" not in LauraX.recent_history:
                    #if you didn't apologize in second response
                    ch_l "You said that it looked like a. . ."
                    ch_l "A prostitute."
                    menu:
                        extend ""
                        "Oooh. Ouch. Yeah.":
                                $ LauraX.change_face("sly",1)
                                $ LauraX.change_stat("love", 80, 2)
                                $ LauraX.change_stat("love", 200, 2)
                                $ LauraX.change_stat("inhibition", 60, 2)
                        "Oh, yeah. I'm sorry about that.":
                                $ LauraX.change_face("smile",1)
                                $ LauraX.change_stat("love", 80, 2)
                                $ LauraX.change_stat("love", 200, 5)
                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                        "Is that a problem?":
                                $ LauraX.change_face("surprised",1)
                                pause 0.5
                                $ LauraX.change_face("angry",1)
                                $ LauraX.change_stat("love", 80, -5)
                                $ LauraX.change_stat("love", 200, -5)
                                $ LauraX.change_stat("obedience", 70, 5)
                                ch_l "Of -course- it's a -problem-. . ."
                        "Huh.":
                                $ LauraX.change_stat("love", 99, -3)
                                $ LauraX.change_stat("obedience", 70, 5)
                                $ LauraX.change_face("surprised",1)
                        ". . .":
                                $ LauraX.change_stat("love", 80, -2)
                                $ LauraX.change_stat("love", 200, -2)
                                $ LauraX.change_face("angry",1)

        if "lover" in LauraX.Petnames:
                ch_l "You understand why this would... bother me. . ."
                menu:
                    extend ""
                    "Oh. . . yeah.":
                            $ LauraX.change_face("normal",1,Eyes="side")
                            $ LauraX.change_stat("love", 90, 1)
                            $ LauraX.change_stat("inhibition", 60, 2)
                            $ LauraX.AddWord(1,"nyx",0,0,0) #adds "nyx" to Recent
                    "I'm sorry, I must have missed it.":
                            $ LauraX.change_face("confused",2)
                            $ LauraX.change_stat("love", 200, -3)
                            ch_l "Seriously?"
                            $ LauraX.change_face("angry",1)
                    "What? Why?":
                            $ LauraX.change_face("confused",2)
                            $ LauraX.change_stat("love", 200, -5)
                            ch_l "Seriously?"
                            $ LauraX.change_face("angry",1)

        if "nyx" not in LauraX.recent_history:
                ch_l "Maybe you don't understand why this cuts deep. . ."
                ch_l ". . ."
                $ LauraX.change_face("sadside",1)
                ch_l "When I was younger, on my own. . ."
                $ LauraX.change_stat("inhibition", 60, 1)
                ch_l "I had to do some things. . ."
                $ LauraX.Blush = 2
                $ LauraX.change_stat("inhibition", 60, 1)
                ch_l "On the streets."
                $ LauraX.change_face("sad",1)
                ch_l "So I don't want to be called. . . that."

        menu:
            extend ""
            "Oh, I'm so sorry.":
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_face("smile",1,Eyes="side")
                    ch_l "Thanks. . ."
                    $ LauraX.change_face("smile",1)
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
            "Yeah, I get it.":
                    $ LauraX.change_stat("love", 80, 2)
                    $ LauraX.change_stat("love", 200, 3)
                    $ LauraX.change_stat("obedience", 80, 1)
                    $ LauraX.change_stat("inhibition", 60, 1)
                    $ LauraX.change_face("smile",1)
                    ch_l "Thanks."
                    $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
            "Oh, ok.":
                    if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 400, "O"):
                        $ LauraX.change_stat("obedience", 60, 3)
                        $ LauraX.change_stat("obedience", 90, 2)
                        $ LauraX.change_stat("inhibition", 60, 3)
                        $ LauraX.change_face("sly",1)
                    else:
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 90, 5)
                        $ LauraX.change_face("angry",1)
                    ch_l ". . ."
            "Ha! Get over it.":
                    $ LauraX.change_face("angry",1)
                    $ LauraX.change_stat("love", 80, -5)
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 80, 5)
                    $ LauraX.change_stat("inhibition", 60, 5)
                    ch_l "Asshole."
                    $ LauraX.DrainWord("sorry",1,0,0)
        menu:
            extend ""
            "Won't happen again.":
                    if "sorry" not in LauraX.recent_history:
                            $ LauraX.change_face("confused",1)
                            ch_l "So you're sorry then?"
                            menu:
                                "Yeah, of course!":
                                        $ LauraX.change_face("smile",1)
                                        $ LauraX.change_stat("love", 200, 3)
                                        ch_l "Good."
                                        $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                                "Eh, I guess?":
                                        ch_l ". . ."
                                        if ApprovalCheck(LauraX, 1200) or ApprovalCheck(LauraX, 400, "O"):
                                                $ LauraX.change_face("normal",1)
                                                $ LauraX.change_stat("love", 80, 2)
                                                $ LauraX.change_stat("love", 200, 2)
                                                $ LauraX.change_stat("obedience", 90, 2)
                                                $ LauraX.change_stat("inhibition", 60, 1)
                                                ch_l "Good enough."
                                                $ LauraX.AddWord(1,"sorry",0,0,0) #adds "sorry" to Recent
                                        else:
                                                $ LauraX.change_stat("love", 90, -5)
                                                $ LauraX.change_stat("obedience", 90, 3)
                                                $ LauraX.change_stat("inhibition", 60, 1)
                                                $ LauraX.change_face("angry",1)
                                                ch_l "Not good enough."
                                "For what?":
                                        $ LauraX.change_face("angry",1)
                                        $ LauraX.change_stat("love", 80, -5)
                                        $ LauraX.change_stat("love", 99, -5)
                                        $ LauraX.change_stat("obedience", 90, 5)
                                        $ LauraX.change_stat("inhibition", 50, 5)
                                        $ LauraX.change_stat("inhibition", 70, 5)
                                        ch_l "Grrrrrr."
                    else:
                            $ LauraX.change_face("angry",1,Mouth="smile")
                            $ LauraX.change_stat("obedience", 80, 2)
                            $ LauraX.change_stat("inhibition", 60, 3)
                            ch_l "It'd better not."

            "That all?":
                    $ LauraX.change_face("angry",1)
                    $ LauraX.change_stat("love", 80, -5)
                    $ LauraX.change_stat("love", 99, -5)
                    $ LauraX.change_stat("inhibition", 60, 10)
                    ch_l "Seriously?!"

        if "sorry" in LauraX.recent_history:
                $ LauraX.change_face("smile",1)
                ch_l "I'm glad that you care, at least."
        else:
                $ LauraX.change_face("angry",1)
                $ LauraX.AddWord(1,"angry","angry",0,0) #adds "angry" to Recent/Daily
                ch_l "Well if that's how you feel about it, you can fuck right off!"
        return
