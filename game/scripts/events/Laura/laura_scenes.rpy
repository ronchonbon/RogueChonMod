




label Laura_Key:
    call set_the_scene
    $ LauraX.change_face("bemused")
    ch_l "Hey, so. . . this isn't something I usually do but. . ."
    ch_l "Look, you've been sleeping over a lot and I was thinking. . ."
    ch_l "Just take it already."
    "She takes your hand and practically forces a key onto your palm before making your fingers close on it."
    $ Player.Keys.append(LauraX)
    $ LauraX.event_happened[0] = 1
    ch_p "Thanks."
    return






label Laura_BF(temp_Girls = []):
    $ shift_focus (LauraX)
    if LauraX.location != Player.location:
        $ LauraX.location = Player.location
        if LauraX not in Player.Party:
            "[LauraX.name] approaches you and motions that she wants to speak to you alone."
        else:
            "[LauraX.name] turns towards you and motions that she wants to speak to you alone."
    $ LauraX.drain_word("asked_to_meet")
    call set_the_scene
    call show_Girl (LauraX)
    "She looks a bit concerned and you can tell she's a bit anxious about whatever she has to say."
    call set_Character_taboos
    call clear_the_room (LauraX)
    $ LauraX.daily_history.append("relationship")
    $ LauraX.change_face("angry", 1, eyes = "side")
    $ line = 0
    ch_l "Hey. So. [LauraX.player_petname]. . ."
    $ LauraX.change_face("confused", 1, mouth = "lipbite")
    ch_l "I don't know- . . . you're pretty fun to hang out with, ya know?"
    menu:
        extend ""
        "I really love hanging out with you too!":
            $ LauraX.change_face("surprised", 2)
            ch_l "Right, so-"
            call change_Girl_stat(LauraX, "obedience", -3)
            call change_Girl_stat(LauraX, "inhibition", 1)
            ch_l ". . ."
            call change_Girl_stat(LauraX, "love", 5)
            $ LauraX.change_face("bemused", 1, eyes = "side")
            ch_l "\"Love\" is kind of a strong word, [LauraX.player_petname]."
        "Yeah, sure, it's a lot of fun.":
            call change_Girl_stat(LauraX, "love", 10)
            call change_Girl_stat(LauraX, "inhibition", 2)
            $ LauraX.change_face("smile", 0)
            ch_l "Right?"
        "I mean, it beats math class. . .":
            call change_Girl_stat(LauraX, "love", 3)
            call change_Girl_stat(LauraX, "obedience", 3)
            call change_Girl_stat(LauraX, "inhibition", -3)
            $ LauraX.change_face("angry", 1)
            ch_l "Um, less enthusiasm than I was expecting. . ."
        "If you say so.":
            call change_Girl_stat(LauraX, "obedience", 6)
            call change_Girl_stat(LauraX, "inhibition", -8)
            $ LauraX.change_face("confused", 1)
            ch_l ". . ."

    ch_l "So like I was saying, I don't exactly have a ton of friends."
    $ LauraX.change_face("sadside", 1)
    ch_l "I kind of grew up in a rough place, and then spent a lot of time on the road."
    ch_l "I had a life before coming here."
    menu:
        extend ""
        "What was it like?":
            call change_Girl_stat(LauraX, "love", 7)
            call change_Girl_stat(LauraX, "obedience", 2)
            call change_Girl_stat(LauraX, "inhibition", 3)
            $ LauraX.change_face("sad", 1, mouth = "lipbite")
        "Yeah? I know.":
            call change_Girl_stat(LauraX, "love", 3)
            call change_Girl_stat(LauraX, "obedience", 4)
            call change_Girl_stat(LauraX, "inhibition", 1)
            $ LauraX.change_face("confused", 1, mouth = "lipbite")
        "I don't need a lot of backstory drama.":
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 10)
            call change_Girl_stat(LauraX, "inhibition", -5)
            $ LauraX.change_face("angry", 1)
            $ line = "bad"
            ch_l "Fine!"
            ch_l "\"Keep it simple\" it is then."
            ch_l "I don't hate hanging out with you, is all."
    if line != "bad":
        $ LauraX.change_face("normal", 1, eyes = "side")
        ch_l "Well, you may have guessed I'm related to Wolverine."
        menu:
            extend ""
            "Kinda obvious, yeah.":
                call change_Girl_stat(LauraX, "love", 4)
            "I had no idea!":
                call change_Girl_stat(LauraX, "love", 3)
                call change_Girl_stat(LauraX, "inhibition", 1)
                $ LauraX.change_face("confused", 1)
            "Duh.":
                call change_Girl_stat(LauraX, "love", 1)
                call change_Girl_stat(LauraX, "obedience", 2)
                $ LauraX.change_face("angry", 1)
        ch_l "Well I'm actually his partial clone."
        $ LauraX.change_face("angry", 1, eyes = "side")
        ch_l "I was created to be some sort of biological weapon, an assassin."
        ch_l "I did a lot of work for them as a kid, until eventually I escaped."
        $ LauraX.change_face("sadside", 1)
        ch_l "After that, I had to do a lot of stuff. . . to stay alive."
        ch_l "Stuff I'm not proud of."
        $ LauraX.change_face("sad", 1)
        ch_l "But I don't know. . . being around you, I think it helps."
        $ LauraX.change_face("sad", 1, mouth = "smile")
        ch_l "I kind of feel. . . better."
    if LauraX.SEXP >= 20:
        call change_Girl_stat(LauraX, "obedience", 3)
        call change_Girl_stat(LauraX, "inhibition", 2)
        call change_Girl_stat(LauraX, "lust", 5)
        $ LauraX.change_face("sly", 1)
        ch_l "You really are good in bed, after all."
    if len(Player.Harem) >= 2:
        ch_l "And I know that you have your share of other girls. . ."
        ch_l ". . . but I'd still like to be a part of your life."
    elif Player.Harem:
        ch_l "And I know you're with someone else. . ."
        ch_l ". . . but I'd still like to be a part of your life."
    else:
        ch_l "I'd just like to be a part of your life."
    $ LauraX.change_face("sad", 1, mouth = "smile")
    ch_l "That's it."
    $ LauraX.event_happened[5] += 1
    menu:
        extend ""
        "Yeah! I really love you.":
            call change_Girl_stat(LauraX, "love", -3)
            call change_Girl_stat(LauraX, "obedience", -3)
            call change_Girl_stat(LauraX, "inhibition", 3)
            $ LauraX.change_face("surprised", 1)
            ch_l "Whoa!"
            $ LauraX.change_face("perplexed")
            ch_l "Maybe cool your jets there, [LauraX.player_petname]."
            $ LauraX.change_face("smile", eyes = "side")
            ch_l "I wasn't. . ."
            ch_l "I don't think we're there. . ."
            $ LauraX.change_face("perplexed", 1)
            ch_l "Right?"
            menu:
                extend ""
                "Maybe you aren't.":
                    call change_Girl_stat(LauraX, "love", 10)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Girl_stat(LauraX, "inhibition", 5)
                    call change_Girl_stat(LauraX, "lust", 2)
                    $ LauraX.change_face("smile", 1, eyes = "side")
                    ch_l "Hehe. . . um."
                "I guess, sure.":
                    call change_Girl_stat(LauraX, "love", 6)
                    call change_Girl_stat(LauraX, "obedience", 3)
                    call change_Girl_stat(LauraX, "inhibition", 2)
                    $ LauraX.change_face("angry", 1, eyes = "side", mouth = "lipbite")
                    ch_l "Right, so. . ."
        "Yeah, I think that'd be great.":

            call change_Girl_stat(LauraX, "love", 6)
            call change_Girl_stat(LauraX, "obedience", 2)
            call change_Girl_stat(LauraX, "inhibition", 3)
            $ LauraX.change_face("smile", 1, eyes = "side")
            ch_l "Cool."
        "Hmm? Ok.":
            call change_Girl_stat(LauraX, "love", 3)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 3)
            $ LauraX.change_face("confused", 1, eyes = "side")
            ch_l "Yeah. . . cool."
        "I'm not really into that.":
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", -5)
            $ LauraX.change_face("sad", 1)
            if len(Player.Harem) >= 2:
                ch_l "Is it because of [Player.Harem[0].name] and the rest?"
            elif Player.Harem:
                ch_l "Is it because of [Player.Harem[0].name]?"
            else:
                ch_l "Why not? What's the deal?"
            menu:
                extend ""
                "Yeah, I don't think she'd understand." if len(Player.Harem) == 1:
                    call change_Girl_stat(LauraX, "love", -5)
                    call change_Girl_stat(LauraX, "obedience", 7)
                    $ LauraX.change_face("angry", 1, eyes = "side")
                    $ LauraX.check_if_likes(Player.Harem[0],800, -20, 1)
                    ch_l "That bitch."
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    call change_Girl_stat(LauraX, "love", -5)
                    call change_Girl_stat(LauraX, "obedience", 7)
                    $ LauraX.change_face("angry", 1, eyes = "side")
                    call change_Harem_stat (LauraX, 700, -20)
                    ch_l "Bitches."
                "It's. . . complicated.":
                    call change_Girl_stat(LauraX, "love", -20)
                    call change_Girl_stat(LauraX, "obedience", 8)
                    call change_Girl_stat(LauraX, "inhibition", -5)
                    $ LauraX.change_face("angry", 1)
                    ch_l "Complicated. Sure. Whatever."
                    $ LauraX.change_face("angry", 1, eyes = "side")
                    if len(Player.Harem) >= 2:
                        ch_l "Probably those bitches."
                        call change_Harem_stat (LauraX, 700, -10)
                    elif Player.Harem:
                        ch_l "Probably because of her."
                        $ LauraX.check_if_likes(Player.Harem[0],800, -20, 1)
                    $ line = "no"
                "I'm just not into you like that.":
                    call change_Girl_stat(LauraX, "love", -10)
                    $ LauraX.change_face("surprised", 1)
                    ch_l "Oh."
                    call change_Girl_stat(LauraX, "obedience", 10)
                    call change_Girl_stat(LauraX, "inhibition", 5)
                    $ LauraX.change_face("sadside", 1)
                    ch_l "Ok, I guess I can respect that."


            $ LauraX.change_face("sad", 1)
            if line != "no":
                ch_l "We're still cool though."
            ch_l "I should. . . leave."
            "[LauraX.name] wanders off in a bit of a daze."
            $ LauraX.event_happened[5] = 20
            call remove_Girl(LauraX)
            $ line = 0
            return

    if Player.Harem:
        if not approval_check(LauraX, 1400):
            if len(Player.Harem) >= 2:
                ch_l "So you'll break up with the others?"
            else:
                ch_l "So you'll break up with [Player.Harem[0].name]?"
            menu:
                extend ""
                "Yes, you're worth it.":
                    call change_Girl_stat(LauraX, "love", 20)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Girl_stat(LauraX, "inhibition", 5)
                    $ LauraX.change_face("surprised", 2, mouth = "smile")
                    ch_l ". . ."
                    $ LauraX.change_face("smile", 1)

                    $ LauraX.event_happened[5] = 10
                "I'd rather you join us.":
                    $ line = 0
                    if approval_check(LauraX, 1200):

                        $ temp_Girls = Player.Harem[:]
                        while temp_Girls and line != "no":

                            if LauraX.likes[temp_Girls[0].tag] <= 500:
                                $ line = "no"
                            $ temp_Girls.remove(temp_Girls[0])
                    else:
                        $ line = "no"
                    if line == "no":
                        call change_Girl_stat(LauraX, "love", -10)
                        call change_Girl_stat(LauraX, "obedience", 10)
                        $ LauraX.change_face("angry", 1)
                        call change_Harem_stat (LauraX, 700, -10)
                        ch_l "Eh, I'll pass."
                    else:
                        call change_Girl_stat(LauraX, "love", 200, 5)
                        call change_Girl_stat(LauraX, "obedience", 15)
                        call change_Girl_stat(LauraX, "inhibition", 10)
                        $ LauraX.change_face("bemused", 1)
                        ch_l "Well, I s'pose that wouldn't be so terrible."
                "What? Of course not.":
                    call change_Girl_stat(LauraX, "love", -25)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Harem_stat (LauraX, 700, -20)
                    $ LauraX.change_face("angry", 1)
                    ch_l "Well, fine then."
                    $ line = "no"
            if line == "no":
                $ LauraX.event_happened[5] = 20
                call remove_Girl(LauraX)
                $ line = 0
                return



        if len(Player.Harem) >= 2:
            ch_l "And you don't think the others would mind?"
        else:
            ch_l "And you don't think [Player.Harem[0].name] would mind?"
        menu:
            extend ""
            "No, actually they're fine with it." if "LauraYes" in Player.traits:
                call change_Girl_stat(LauraX, "love", 5)
                call change_Girl_stat(LauraX, "obedience", 10)
                call change_Girl_stat(LauraX, "inhibition", 5)
                $ LauraX.change_face("surprised", 1)
                ch_l "Oh, cool."
            "Actually. . . I guess we'll need to work on that one." if "LauraYes" not in Player.traits:
                call change_Girl_stat(LauraX, "love", 3)
                call change_Girl_stat(LauraX, "obedience", 3)
                call change_Girl_stat(LauraX, "inhibition", 1)
                call change_Girl_stat(LauraX, "lust", 1)
                $ LauraX.change_face("confused", 1)
                ch_l "Hmm, get back to me, I guess?"
                $ LauraX.event_happened[5] = 20
                call remove_Girl(LauraX)
                $ line = 0
                return
        call change_Harem_stat (LauraX, 900, 20)


    if not simulation:
        $ Player.Harem.append(LauraX)
        if "LauraYes" in Player.traits:
            $ Player.traits.remove("LauraYes")
        $ LauraX.player_petnames.append("boyfriend")
        call Harem_Initiation
    call change_Girl_stat(LauraX, "love", 3)
    call change_Girl_stat(LauraX, "obedience", 3)
    call change_Girl_stat(LauraX, "inhibition", 1)
    call change_Girl_stat(LauraX, "lust", 1)
    $ LauraX.change_face("sly", 1)
    ch_l "So, did you have any plans for the next few minutes? . ."
    if simulation:
        return True
    $ approval_bonus = 10
    $ Player.add_word(1, "interruption")
    call enter_main_sex_menu(LauraX)
    $ approval_bonus = 0

    return

label Laura_Cleanhouse:

    $ LauraX.drain_word("asked_to_meet")
    if "cleanhouse" in LauraX.to_do:
        $ LauraX.to_do.remove("cleanhouse")
    if not Player.Harem or LauraX in Player.Harem:
        $ LauraX.event_happened[5] = 2
        return

    if LauraX.location == Player.location or LauraX in Player.Party:
        "[LauraX.name] glances over at you with a scowl."
    else:
        "[LauraX.name] turns a corner and notices you."
    if Player.location != "bg_laura" and Player.location != "bg_player":
        "With little word, she moves behind you and pushes you towards her room."
        $ Player.location = "bg_laura"

    call set_the_scene
    call clear_the_room (LauraX)
    call set_the_scene
    call set_Character_taboos
    $ LauraX.daily_history.append("relationship")
    call change_Girl_stat(LauraX, "love", -20)
    $ LauraX.change_face("angry", 1)
    ch_l "What's the deal, [Player.player_petname]?"
    ch_l "It's been a week already, and you're still dating [Player.Harem[0].name]!"
    if len(Player.Harem) >= 2:
        ch_l "Not to mention the rest of them!"
    menu:
        extend ""
        "Sorry about that, I'm sticking with them":
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 5)
            $ LauraX.change_face("angry", 2)
            ch_l "You asshole."
            $ LauraX.change_face("sadside", 1)
            ch_l "You could have at least been honest about it."
        "Must have slipped my mind":
            call change_Girl_stat(LauraX, "love", -10)
            call change_Girl_stat(LauraX, "obedience", 10)
            ch_l "!"
            ch_l "Seriously dude? That's all you've got?"
        "[[shrug]":
            call change_Girl_stat(LauraX, "love", -20)
            call change_Girl_stat(LauraX, "obedience", 10)
            call change_Girl_stat(LauraX, "inhibition", 10)
            $ LauraX.blushing = "_blush2"

            call show_Girl(LauraX, transition = vpunch)

            "She clocks you one."
            "That was fair."
            $ LauraX.blushing = "_blush1"

    ch_l "I can't believe you're putting me through this."
    ch_l "Making me choose between you and putting up with this whole arrangement."
    $ line = 0
    if approval_check(LauraX, 1400) and approval_check(LauraX, 600, "O"):

        pass
    elif approval_check(LauraX, 1200) and approval_check(LauraX, 500, "O"):

        $ temp_Girls = Player.Harem[:]
        while temp_Girls and line != "no":

            if LauraX.likes[temp_Girls[0].tag] <= 400:
                $ line = "no"
            $ temp_Girls.remove(temp_Girls[0])
    else:
        $ line = "no"
    if line == "no":
        call change_Girl_stat(LauraX, "love", -10)
        call change_Girl_stat(LauraX, "obedience", 10)
        $ LauraX.change_face("angry", 1)
        call change_Harem_stat (LauraX, 700, -15)
        ch_l "No, this is bullshit, never mind."
    else:
        call change_Girl_stat(LauraX, "love", 5)
        call change_Girl_stat(LauraX, "obedience", 20)
        call change_Girl_stat(LauraX, "inhibition", 10)
        $ LauraX.change_face("angry", 1, eyes = "side")
        ch_l "Ok, fine, whatever. I'm in too."
        if not simulation:
            $ Player.Harem.append(LauraX)
            if "LauraYes" in Player.traits:
                $ Player.traits.remove("LauraYes")
            $ LauraX.player_petnames.append("boyfriend")
            call Harem_Initiation
            call change_Harem_stat (LauraX, 900, 20)
            $ LauraX.event_happened[5] = 20
    return


label Laura_Love(Shipping = [], Shipshape=0, Topics = [], temp_Girls = []):






    $ LauraX.drain_word("asked_to_meet")
    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(LauraX)
    while temp_Girls:
        if approval_check(temp_Girls[0], 1200, "LO"):
            $ Shipping.append(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])
    $ Shipshape = len(Shipping)

    if LauraX.location == Player.location or LauraX in Player.Party:
        "[LauraX.name] glances over at you with a concerned look."
    else:
        "[LauraX.name] turns a corner and notices you."
    if Player.location != "bg_laura" and Player.location != "bg_player":
        "With little word, she moves behind you and pushes you towards her room."
        $ Player.location = "bg_laura"

    call set_the_scene
    call clear_the_room (LauraX)
    call set_the_scene
    call set_Character_taboos
    $ LauraX.daily_history.append("relationship")
    $ LauraX.change_face("sad", 1)
    ch_l "Hey, so, I like what this is. . ."
    ch_l "-what we have. . ."
    $ LauraX.change_face("sadside", 1)
    ch_l "It's been kind of hard for me to open up to people. . ."
    ch_l "I've been betrayed a lot out there."
    menu:
        extend ""
        "I would never betray you.":
            $ LauraX.change_face("bemused", 1)
            call change_Girl_stat(LauraX, "love", 10)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 5)
            ch_l "I. . . know that now."
        "I'm sorry to hear that.":
            $ LauraX.change_face("sadside", 1, mouth = "smile")
            call change_Girl_stat(LauraX, "love", 5)
            call change_Girl_stat(LauraX, "obedience", -5)
            call change_Girl_stat(LauraX, "inhibition", 10)
            ch_l ". . ."
            $ LauraX.change_face("smile", 1)
            ch_l "Thank you. . ."
        "That must be rough.":
            $ LauraX.change_face("sadside", 1, mouth = "normal")
            call change_Girl_stat(LauraX, "love", 5)
            ch_l ". . ."
            $ LauraX.change_face("smile", 1)
            ch_l "It was. . ."
        "Wow, that sucks.":
            $ LauraX.change_face("confused", 1)
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 10)
            call change_Girl_stat(LauraX, "inhibition", -5)
            ch_l ". . ."
            $ LauraX.change_face("angry", 1, eyes = "side")
            ch_l "Right, so. . ."
    ch_l "I didn't always have it as easy as I've had it here."
    $ LauraX.eyes = "normal"
    ch_l "I only thought it fair to tell you a little about that history."
    $ line = 0
    while len(Topics) < 9 and "exit" not in Topics:


        if line == "facility":
            menu:
                extend ""
                "How many people did you kill?" if "kills" not in Topics:
                    $ LauraX.change_face("angry", 0, eyes = "side")
                    ch_l "Dozens. Maybe more. At least 13 primary targets."
                    ch_l "Too many \"collaterals.\""
                    $ Topics.append("kills")
                "Did you ever fail a mission?" if "fail" not in Topics:
                    $ LauraX.change_face("angry", 0, eyes = "side", brows = "normal")
                    ch_l "Once or twice."
                    ch_l "Sometimes they managed to get away."
                    ch_l "I'm not proud of who I was back then, but even then. . ."
                    $ LauraX.mouth = "smile"
                    ch_l ". . . a part of me was happy when they did."
                    $ Topics.append("fail")
                "Did anyone take care of you?" if "mother" not in Topics:
                    $ LauraX.change_face("smile", 0)
                    ch_l "My mother, Sarah Kinney."
                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                    $ LauraX.change_face("sadside", 0)
                    ch_l "She tried to help me, until I killed her."
                    $ Topics.append("mother")
                    $ line = "mother"
                "How did you escape?" if "escape" not in Topics:
                    $ LauraX.change_face("sadside", 0)
                    ch_l "Mother."
                    ch_l "She got me out, found me an escape route."
                    ch_l "It was the last thing she did."
                    $ Topics.append("escape")
                    $ line = "mother"
                "I'd like to know more about what came after.":
                    $ line = "NYX"
                "Enough about that though. . .":
                    $ line = 0



        if line == "mother":
            menu:
                extend ""
                "Who was your mother?" if "mother" not in Topics:
                    $ LauraX.change_face("smile", 0)
                    ch_l "Her name was Sarah Kinney."
                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                    $ LauraX.change_face("sadside", 0)
                    ch_l "She tried to help me, until I killed her."
                    $ Topics.append("mother")
                    $ line = "mother"
                "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:
                    $ LauraX.change_face("sad", 0, eyes = "surprised")
                    ch_l "I didn't want to, but the trigger scent made me. . ."
                    $ LauraX.change_face("sadside", 0)
                    if "trigger" in LauraX.history:
                        ch_l "I've mentioned that to you before. . ."
                    else:
                        $ LauraX.history.append("trigger")
                    ch_l ". . . it can make me kill, even if I don't want to."
                    $ Topics.append("killed")
                "It wasn't your fault." if "killed" in Topics:
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Girl_stat(LauraX, "inhibition", 5)
                    $ LauraX.change_face("sad", 0)
                    ch_l "Not completely, no."
                    $ LauraX.change_face("sadside", 0)
                    ch_l "But my hands aren't clean."
                    $ line = "facility"
                "That must have been horrible." if "killed" in Topics:
                    $ LauraX.change_face("sadside", 0)
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    ch_l "It's taken me some time. . ."
                    $ LauraX.change_face("normal", 0)
                    ch_l "but I think I'm ok with it now."
                    $ line = "facility"
                "Bummer." if "killed" in Topics:
                    $ LauraX.change_face("angry", 1)
                    call change_Girl_stat(LauraX, "love", -10)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    ch_l "Are you seriously making fun of my mother's death?!"
                    $ Topics.append("exit")
                    $ line = "angry"


        if line == "NYX":
            menu:
                extend ""
                "What did you do for a living?" if "living" not in Topics:
                    $ LauraX.change_face("sadside", 0)
                    ch_l "There wasn't much I could do at the time, I mostly just scrounged for food."
                    ch_l "You can get by on some pretty awful stuff if you have a healing factor."
                    $ LauraX.change_face("bemused", 1, brows = "sad")
                    ch_l "I also did some. . . shady stuff."
                    $ Topics.append("living")

                "Was it sexual?" if "work" not in Topics and "living" in Topics:
                    $ LauraX.change_face("sadside", 2)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Girl_stat(LauraX, "inhibition", 10)
                    ch_l ". . ."
                    $ LauraX.blushing = "_blush1"
                    ch_l "A little."
                    $ line = "work"
                    $ Topics.append("work")

                "Did you hurt people?" if "work" not in Topics and "living" in Topics:
                    $ LauraX.change_face("surprised", 0, eyes = "normal")
                    ch_l "No, definitely not."
                    ch_l "After the facility, I just couldn't take that sort of work anymore."
                    $ LauraX.change_face("bemused", 0)
                    ch_l "I avoided hurting anyone."
                    $ LauraX.change_face("sadside", 2)
                    ch_l "It tended to be more. . . sexual work."
                    $ line = "work"
                    $ Topics.append("work")

                "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:
                    $ LauraX.change_face("bemused", 0)
                    ch_l "Yeah, eventually."
                    ch_l "I'd seen Wolverine on the news, and thought maybe he had some answers."
                    ch_l "He's not around much though."
                    $ Topics.append("xaviers")
                    $ line = 0
                "Good thing you made it here. [[exit]" if "xaviers" in Topics:
                    $ LauraX.change_face("smile", 0)
                    ch_l "Yeah."
                    $ line = 0

        if line == "work":
            $ LauraX.change_face("sadside", 0, mouth = "normal")
            ch_l "It was mostly the rougher customers."
            ch_l "The ones who couldn't control their tempers."
            $ LauraX.change_face("angry", 0, mouth = "smile")
            ch_l "Better for the girl who can heal to take the hits, right?"
            menu:
                extend ""
                "That's terrible. I wish I could have protected you.":
                    $ LauraX.change_face("smile", 1)
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Girl_stat(LauraX, "inhibition", -5)
                    ch_l "Thanks, but I was ok."
                    $ LauraX.change_face("sadside", 0)
                    ch_l "I didn't deserve it, but I felt like I did at the time."
                "You're strong to have made it out of there.":
                    $ LauraX.change_face("smile", 0)
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "obedience", 10)
                    call change_Girl_stat(LauraX, "inhibition", 5)
                    ch_l "Thanks."
                    ch_l "I didn't really think of it like that. . ."
                    $ LauraX.change_face("sadside", 0)
                    ch_l "I just felt like I'd deserved it."
                    ch_l "But I realized how wrong that was."
                "Yeah, that makes sense.":
                    $ LauraX.change_face("confused", 1)
                    call change_Girl_stat(LauraX, "love", -5)
                    call change_Girl_stat(LauraX, "obedience", 15)
                    call change_Girl_stat(LauraX, "inhibition", -5)
                    ch_l "Don't think before you speak, do you?"
                    $ LauraX.change_face("sadside", 0)
                    ch_l "It wasn't right, I just didn't realize it at the time."
            ch_l "Eventually I got past it and decided to get out of there."
            ch_l "Not like they could stop me."
            $ line = "NYX"

        if not line:

            menu:
                extend ""
                "What did you do back at the facility?" if "facility" not in Topics:
                    $ LauraX.change_face("sadside", 0)
                    ch_l "After they tested what I could do, they put me to work."
                    ch_l "Mainly, I killed people for them."
                    $ Topics.append("facility")
                    $ line = "facility"
                "More about that facility. . ." if "facility" in Topics:
                    $ line = "facility"

                "Where did you go after you escaped?" if "NYX" not in Topics:
                    $ LauraX.change_face("sadside", 0)
                    ch_l "I wandered in the wilderness for weeks."
                    ch_l "Eventually I found my way to New York."
                    ch_l "I lived on the streets for a few years."
                    $ Topics.append("NYX")
                    $ line = "NYX"
                "More about after the escape. . ." if "NYX" in Topics:
                    $ line = "NYX"

                "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:
                    $ LauraX.change_face("smile", 0)
                    call change_Girl_stat(LauraX, "love", 10)
                    call change_Girl_stat(LauraX, "obedience", 3)
                    call change_Girl_stat(LauraX, "inhibition", 3)
                    ch_l "Thanks for listening to me ramble."
                    $ Topics.append("exit")
                "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:
                    $ LauraX.change_face("sadside", 0, mouth = "smile")
                    call change_Girl_stat(LauraX, "obedience", 10)
                    ch_l "Yeah, you get the idea."
                    $ Topics.append("exit")
                "I don't really care about that. [[exit]":
                    $ LauraX.change_face("angry", 0)
                    call change_Girl_stat(LauraX, "love", -15)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Girl_stat(LauraX, "obedience", 10)
                    call change_Girl_stat(LauraX, "inhibition", -5)
                    ch_l "Oh, I'm sorry if I was boring you with my life story."
                    $ line = "angry"
                    $ Topics.append("exit")



    if line == "angry":
        $ LauraX.change_face("angry", 0)
        ch_l "And here I was thinking that I meant something to you."
        ch_l "Well forget that!"
        $ line = 0
        $ LauraX.event_happened[6] = 23
        $ LauraX.recent_history.append("angry")
        $ LauraX.daily_history.append("angry")
        hide Laura_sprite with easeoutright
        call remove_Girl(LauraX)
        $ LauraX.location = "hold"
        return

    $ LauraX.change_face("bemused", 0, eyes = "down")
    ch_l "I just thought you should know, "
    $ LauraX.change_face("smile", 2)
    ch_l "I love you."
    menu:
        extend ""
        "I love you too!":
            $ LauraX.change_face("smile", 1)
            call change_Girl_stat(LauraX, "love", 20)
            call change_Girl_stat(LauraX, "inhibition", 5)
            ch_l "For a second there you had me worried."
            $ LauraX.player_petnames.append("lover")
            jump Laura_Love_End
        "I know.":
            $ LauraX.change_face("smile", 1)
            call change_Girl_stat(LauraX, "love", 10)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 10)
            call change_Girl_stat(LauraX, "lust", 5)
            ch_l "Smooth one. Seriously though, how about you?"
        "Neat?":
            $ LauraX.change_face("confused", 1)
            call change_Girl_stat(LauraX, "obedience", 5)
            ch_l "I'm gonna need a bit more there, [LauraX.player_petname]."
        "Huh.":
            $ LauraX.change_face("confused", 1)
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 10)
            ch_l "I'm not sure how to take that one."


    menu:
        extend ""
        "Oh, I love you too!":
            $ LauraX.change_face("smile", 1)
            call change_Girl_stat(LauraX, "love", 15)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 5)
            ch_l "For a second there you had me worried."
            $ LauraX.player_petnames.append("lover")
            jump Laura_Love_End
        "I. . . love you back?":
            $ LauraX.change_face("confused", 1)
            call change_Girl_stat(LauraX, "love", 5)
            call change_Girl_stat(LauraX, "obedience", 10)
            ch_l "Ok, I'll take it."
            $ LauraX.player_petnames.append("lover")
            jump Laura_Love_End
        "I mean, that's cool and all. . .":
            $ LauraX.change_face("sadside", 1)
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 10)
            call change_Girl_stat(LauraX, "inhibition", -5)
            ch_l ". . . but you don't love me back. Got it."
        "That's. . . uncomfortable.":
            $ LauraX.change_face("angry", 1)
            call change_Girl_stat(LauraX, "love", -10)
            call change_Girl_stat(LauraX, "obedience", 15)
            call change_Girl_stat(LauraX, "inhibition", -5)
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
            call change_Girl_stat(LauraX, "obedience", 15)
            call change_Girl_stat(LauraX, "inhibition", 5)
            call change_Girl_stat(LauraX, "lust", 5)
            $ LauraX.change_face("sadside", 1)
            ch_l "Well, you do have your pick."
        "There's nobody else.":
            call change_Girl_stat(LauraX, "love", -15)
            call change_Girl_stat(LauraX, "obedience", 15)
            call change_Girl_stat(LauraX, "inhibition", 5)
            $ LauraX.change_face("sad", 1)
            if approval_check(LauraX, 1000, "OI"):
                ch_l "I guess that's something."
            else:
                ch_l ". . ."
        "It's a \"you\" problem.":
            $ LauraX.change_face("angry")
            call change_Girl_stat(LauraX, "love", -25)
            call change_Girl_stat(LauraX, "obedience", 15)
            ch_l "You're seriously messing with me?"
            call change_Girl_stat(LauraX, "love", -10)
            ch_l "You don't want to see me when I'm angry."
            $ LauraX.recent_history.append("angry")
            $ LauraX.daily_history.append("angry")


    if line:

        if LauraX.likes[line.tag] >= 800:
            call change_Girl_stat(LauraX, "love", 5)
            call change_Girl_stat(LauraX, "obedience", 20)
            call change_Girl_stat(LauraX, "inhibition", 5)
            call change_Girl_stat(LauraX, "lust", 5)
            $ LauraX.change_face("sadside", 1)
            ch_l "Yeah, I guess she's great."
        else:
            $ LauraX.change_face("angry", eyes = "side")
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 20)
            ch_l "Bitch."
            $ LauraX.recent_history.append("angry")
            $ LauraX.check_if_likes(line,800, -50, 1)
    ch_l "Well, if that's the way you feel about it. . ."
    ch_l "I'll. . . see you later."
    ch_l "This. . . hurt."

label Laura_Love_End:
    if "lover" not in LauraX.player_petnames:
        $ LauraX.event_happened[6] = 20
        hide Laura_sprite with easeoutright
        call remove_Girl(LauraX)
        $ LauraX.location = "hold"
        return

    $ LauraX.event_happened[6] = 5
    "[LauraX.name] grabs you in a crushing hug."
    call change_Girl_stat(LauraX, "love", 25)
    call change_Girl_stat(LauraX, "lust", 5)
    $ LauraX.change_face("sly", 1)
    ch_l "So. . . now that we have some free time. . ."
    call change_Girl_stat(LauraX, "lust", 10)

    if not LauraX.permanent_History["sex"]:
        $ LauraX.change_face("bemused", 2)
        ch_l "I think I'm ready. . ."
    else:
        ch_l "Would you like to have some fun?"
    $ Player.add_word(1, "interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            call change_Girl_stat(LauraX, "inhibition", 20)
            call change_Girl_stat(LauraX, "obedience", 10)
            ch_l "Hmm. . ."
            call before_action(LauraX, "sex")
        "I have something else in mind. . .[[choose another activity]":
            $ LauraX.brows = "confused"
            call change_Girl_stat(LauraX, "obedience", 25)
            ch_l "Like what? . ."
            $ approval_bonus = 20
            call enter_main_sex_menu(LauraX)

    return

label Laura_Love_Redux:

    $ line = 0
    $ LauraX.daily_history.append("relationship")

    if LauraX.event_happened[6] >= 25:

        ch_p "I hope you've forgiven me, I still love you."
        call change_Girl_stat(LauraX, "love", 10)
        if approval_check(LauraX, 950, "L"):
            $ line = "love"
        else:
            $ LauraX.change_face("angry")
            ch_l "You're still working your way out of the hole, [LauraX.player_petname]."
            $ LauraX.eyes = "side"
            ch_l ". . ."
            $ LauraX.change_face("angry", mouth = "lipbite")
            ch_l "But let me hear your pitch."
    elif LauraX.event_happened[6] >= 23:

        ch_p "I was rude when you opened up to me before."
        call change_Girl_stat(LauraX, "love", 10)
        if approval_check(LauraX, 950, "L"):
            ch_l "And. . ."
        else:
            $ LauraX.change_face("angry")
            ch_l "You're still working your way out of the hole, [LauraX.player_petname]."
            $ LauraX.eyes = "side"
            ch_l ". . ."
            $ LauraX.change_face("angry", mouth = "lipbite")
            ch_l "But let me hear your pitch."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ LauraX.change_face("perplexed", 1)
        ch_l ". . ."
        $ LauraX.change_face("angry", eyes = "side")
        ch_l "How could I forget?"

    if line != "love":
        menu:
            extend ""
            "I'm sorry, I didn't mean it.":
                $ LauraX.eyes = "surprised"
                ch_l "Oh really?"
                ch_l "That's awfully convenient."
                ch_p "Yeah. I mean, yes, I love you, [LauraX.name]."
                call change_Girl_stat(LauraX, "love", 10)
                if approval_check(LauraX, 950, "L"):
                    $ line = "love"
                else:
                    $ LauraX.change_face("sadside")
                    ch_l "Well, maybe I don't, anymore. . ."
            "I've changed my mind, I do love you, so. . .":
                if approval_check(LauraX, 950, "L"):
                    $ line = "love"
                    ch_l "Well that's great."
                else:
                    $ LauraX.mouth = "sad"
                    ch_l "Good for you."
                    call change_Girl_stat(LauraX, "inhibition", 10)
                    $ LauraX.change_face("sadside")
                    ch_l "I don't exactly have the same mind either. . ."
            "Um, never mind.":
                call change_Girl_stat(LauraX, "love", -30)
                call change_Girl_stat(LauraX, "obedience", 10)
                $ LauraX.change_face("angry")
                ch_l "Oh, fuck you."
                $ LauraX.recent_history.append("angry")
                $ LauraX.daily_history.append("angry")
    if line == "love":
        call change_Girl_stat(LauraX, "love", 40)
        call change_Girl_stat(LauraX, "obedience", 10)
        call change_Girl_stat(LauraX, "inhibition", 10)
        $ LauraX.change_face("smile")
        ch_l "I'm glad you came around."
        ch_l "I love you too, [LauraX.player_petname]!"
        if LauraX.event_happened[6] < 25:
            $ LauraX.change_face("sly")
            "She grabs the back of your head and pulls you close."
            ch_l "Next time, don't keep me waiting."
        $ LauraX.player_petnames.append("lover")
    $ LauraX.event_happened[6] = 25
    return






label Laura_Sub:
    $ LauraX.drain_word("asked_to_meet")
    $ shift_focus (LauraX)
    if LauraX.location != Player.location and LauraX not in Player.Party:
        "Suddenly, [LauraX.name] shows up and says she needs to talk to you."


    call set_the_scene
    call show_Girl (LauraX)
    call clear_the_room (LauraX)
    call set_the_scene
    call set_Character_taboos
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
    $ LauraX.change_face("sly", 1, eyes = "side")
    ch_l "I don't know how I feel about that."
    if LauraX.event_happened[6]:
        $ LauraX.change_face("sadside", 1)
        ch_l "You know the past I've had, with the facility, with the. . . "
        ch_l ". . . work I had to do for them."
        $ LauraX.change_face("sad", 1)
        ch_l "I don't know if I want to let anyone tell me what to do like that again."
    menu Laura_Sub_Question:
        extend ""
        "I guess I can be demanding.":
            $ LauraX.change_face("sly", 1)
            call change_Girl_stat(LauraX, "obedience", 10)
            call change_Girl_stat(LauraX, "inhibition", 5)
        "Sorry. I didn't mean to come off like that.":
            $ LauraX.change_face("sly", 1)
            call change_Girl_stat(LauraX, "love", 5)
            call change_Girl_stat(LauraX, "obedience", -5)
            call change_Girl_stat(LauraX, "inhibition", -5)
            ch_l "I get it, you're assertive. . ."
        "Remind me about the facility?" if LauraX.event_happened[6] and line != "facility":
            $ LauraX.change_face("sadside", 1)
            call change_Girl_stat(LauraX, "love", -10)
            call change_Girl_stat(LauraX, "inhibition", -5)
            ch_l "I told you, I was raised in an underground government lab."
            ch_l "They ordered me to kill people for them."
            $ LauraX.change_face("sly", 0, brows= "angry")
            ch_l ". . . until I got tired of taking orders."
            $ line = "facility"
            jump Laura_Sub_Question
        "What bothers you about being told to do things?" if not LauraX.event_happened[6] and line != "facility":
            $ LauraX.change_face("sadside", 1)
            call change_Girl_stat(LauraX, "love", 5)
            ch_l "I've just had some rough experiences."
            ch_l "You don't need to know about them."
            ch_l ". . ."
            $ LauraX.change_face("sad", 0)
            ch_l "Let's just say I was ordered to do some things I regret."
            $ line = "facility"
            jump Laura_Sub_Question
        "Get with the program.":
            if approval_check(LauraX, 1000, "LO"):
                $ LauraX.change_face("sly", 1)
                call change_Girl_stat(LauraX, "obedience", 20)
                call change_Girl_stat(LauraX, "inhibition", 10)
                ch_l "Hmmm. . ."
            else:
                call change_Girl_stat(LauraX, "love", -10)
                call change_Girl_stat(LauraX, "inhibition", -5)
                $ LauraX.change_face("angry", 0)
                ch_l "You're not off to a good start here. You might want to rethink your attitude."
                menu:
                    extend ""
                    "Sorry. I thought that's what you were into.":
                        $ LauraX.change_face("perplexed", 1, eyes = "side")
                        $ LauraX.eyes = "side"
                        call change_Girl_stat(LauraX, "love", 10)
                        call change_Girl_stat(LauraX, "obedience", 5)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        ch_l ". . . after I just said. . ."
                        $ LauraX.change_face("sly", 1)
                        ch_l "Ok, whatever."
                    "I don't care.":
                        call change_Girl_stat(LauraX, "love", -10)
                        ch_l "I guess not."
                        $ line = "rude"
    if line == "facility":
        $ line = 0

    if not line:

        $ LauraX.change_face("sly", 1)
        ch_l "Look, it's not like. . ."
        $ LauraX.change_face("sly", 2)
        ch_l ". . . it's not like I hate it."
        $ LauraX.change_face("smile", 1, eyes = "side")
        ch_l ". . . I actually think it might make me. . ."
        menu:
            extend ""
            "-excited?":
                call change_Girl_stat(LauraX, "obedience", 5)
                call change_Girl_stat(LauraX, "inhibition", 5)
                ch_l ". . ."
                $ LauraX.change_face("sly", 1)
                call change_Girl_stat(LauraX, "lust", 10)
                ch_l "a little, yeah."
            "-digusted?":
                call change_Girl_stat(LauraX, "love", -5)
                call change_Girl_stat(LauraX, "obedience", -5)
                $ LauraX.change_face("sadside", 1)
                ch_l ". . . kind of, "
                $ LauraX.change_face("sly", 1)
                call change_Girl_stat(LauraX, "inhibition", 5)
                call change_Girl_stat(LauraX, "lust", 5)
                ch_l "but also kind of excited by it."
            "-hungry?":
                $ LauraX.change_face("confused", 1, eyes = "surprised", mouth = "smile")
                call change_Girl_stat(LauraX, "obedience", -5)
                call change_Girl_stat(LauraX, "inhibition", -5)
                ch_l "?!"
                $ LauraX.change_face("confused", 1, eyes = "normal", mouth = "smile")
                ch_l "Well. . . yeah? But not for-"
                $ LauraX.change_face("sly", 1)
                call change_Girl_stat(LauraX, "lust", 5)
                ch_l "I mean, it makes me kind of. . . excited."
            "-horny?":
                call change_Girl_stat(LauraX, "obedience", 10)
                call change_Girl_stat(LauraX, "inhibition", 5)
                $ LauraX.change_face("startled", 2, mouth = "lipbite")
                ch_l "!"
                $ LauraX.change_face("sly", 1, eyes = "side")
                call change_Girl_stat(LauraX, "inhibition", 5)
                call change_Girl_stat(LauraX, "lust", 10)
                call change_Girl_stat(LauraX, "lust", 5)
                ch_l "Yes."
        menu:
            extend ""
            "Good. If you wanna be with me, then you follow my orders.":
                if approval_check(LauraX, 1000, "LO"):
                    $ LauraX.change_face("sly", 1)
                    call change_Girl_stat(LauraX, "obedience", 15)
                    call change_Girl_stat(LauraX, "inhibition", 10)
                    ch_l "Hmmm. . ."
                else:
                    $ LauraX.change_face("sadside", 1, mouth = "normal")
                    call change_Girl_stat(LauraX, "love", -5)
                    call change_Girl_stat(LauraX, "obedience", 10)
                    ch_l "You might want to slow your roll there, [LauraX.player_petname]."
                    menu:
                        extend ""
                        "Whatever. That's how it is. Take it or leave it.":
                            $ LauraX.change_face("angry")
                            call change_Girl_stat(LauraX, "love", -10)
                            call change_Girl_stat(LauraX, "obedience", 5)
                            ch_l "I think you're pushing it too far there, [LauraX.player_petname]."
                            $ line = "rude"
                        "Ok, just a little.":
                            $ LauraX.change_face("bemused", 1)
                            call change_Girl_stat(LauraX, "love", 5)
                            call change_Girl_stat(LauraX, "inhibition", 5)
                            ch_l "-but not too much."
            "Yeah? You think it's sexy?":

                $ LauraX.change_face("bemused", 2, eyes = "side")
                call change_Girl_stat(LauraX, "obedience", 5)
                call change_Girl_stat(LauraX, "inhibition", 10)
                ch_l ". . ."
                call change_Girl_stat(LauraX, "lust", 5)
                ch_l "Yeah."
            "You sure you don't want me to back off a little?":

                $ LauraX.change_face("startled", 1, eyes = "squint")
                call change_Girl_stat(LauraX, "obedience", -5)
                menu:
                    ch_l "Well if you have to ask. . ."
                    "Only if you're okay with it.":
                        $ LauraX.change_face("bemused", 1)
                        call change_Girl_stat(LauraX, "love", 10)
                        call change_Girl_stat(LauraX, "inhibition", 10)
                        $ line = 0
                    "Uhm. . .yeah. I think it's weird. Sorry.":
                        $ LauraX.change_face("sad", 1, eyes = "surprised")
                        call change_Girl_stat(LauraX, "love", -15)
                        call change_Girl_stat(LauraX, "obedience", -5)
                        call change_Girl_stat(LauraX, "inhibition", -10)
                        $ line = "embarrassed"
            "I couldn't care less.":

                call change_Girl_stat(LauraX, "love", -10)
                call change_Girl_stat(LauraX, "obedience", 15)
                $ LauraX.change_face("angry")
                ch_l "I think you're pushing it too far there, [LauraX.player_petname]."
                $ line = "rude"

    if not line:
        $ LauraX.change_face("bemused", 1, eyes = "down")
        ch_l "So, I'm willing to give this a shot."
        ch_l "Just a trial period, to see how it goes."
        ch_l "Just tell me what you want, and. . . I'll see about doing it."
        menu Laura_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                call change_Girl_stat(LauraX, "obedience", 5)
                call change_Girl_stat(LauraX, "inhibition", 5)
                $ LauraX.change_face("sly", 1)
                $ line = 0
            "Don't you think that relationship's kinda. . .weird?":
                $ LauraX.change_face("sad", 1, eyes = "surprised")
                call change_Girl_stat(LauraX, "love", -5)
                call change_Girl_stat(LauraX, "inhibition", -15)
                $ line = "embarrassed"

    if not line:
        $ LauraX.change_face("smile", 1)
        ch_l "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                call change_Girl_stat(LauraX, "love", 5)
                call change_Girl_stat(LauraX, "obedience", 15)
                call change_Girl_stat(LauraX, "inhibition", 5)
                ch_l "Yes, sir."
                $ LauraX.player_petname = "sir"
            "That's kind of formal, isn't it?":
                $ LauraX.change_face("perplexed", 1)
                ch_l "Huh. ok, no problem"
                call change_Girl_stat(LauraX, "inhibition", -5)
                $ LauraX.change_face("sly", 1, eyes = "side")
                menu:
                    ch_l "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                        call change_Girl_stat(LauraX, "obedience", 10)
                        $ LauraX.change_face("smile", 1)
                        ch_l "Good."
                    "I don't feel comfortable with that. . .":
                        $ LauraX.change_face("sad", 1, eyes = "side")
                        call change_Girl_stat(LauraX, "love", -10)
                        call change_Girl_stat(LauraX, "obedience", -30)
                        call change_Girl_stat(LauraX, "inhibition", -15)
                        $ line = "embarrassed"


    $ LauraX.history.append("sir")
    if not line:
        $ LauraX.player_petnames.append("sir")

    elif line == "rude":
        call remove_Girl(LauraX)
        if not simulation:
            $ renpy.pop_call()
        "[LauraX.name] knocks her way past you and storms off."
    elif line == "embarrassed":
        $ LauraX.change_face("sadside", 2)
        ch_l "Huh, ok, if you're not interested. . ."
        hide Laura_sprite with easeoutright
        call remove_Girl(LauraX)
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
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in LauraX.player_petnames and approval_check(LauraX, 850, "O"):

                pass
            elif approval_check(LauraX, 550, "O"):

                pass
            else:
                $ LauraX.change_face("angry", 1)
                ch_l "It was a bad idea, don't worry about it."
                $ line = "rude"

            if line != "rude":
                call change_Girl_stat(LauraX, "love", 10)
                $ LauraX.change_face("sly", 1)
                ch_l "Well, it's not like you stopped ordering me around anyway."
                ch_l "Ok, let's give it a shot."
        "I know it's what you want. Do you want to try again, or not?":

            $ LauraX.change_face("bemused", 1)
            if "sir" in LauraX.player_petnames:
                if approval_check(LauraX, 850, "O"):
                    ch_l "Ok, fine."
                else:
                    ch_l "Nah, I'm good."
                    $ line = "rude"
            elif approval_check(LauraX, 600, "O"):

                $ LauraX.change_face("confused", 1)
                ch_l "Kinda wishy-washy there."
                $ LauraX.change_face("sly", 1)
                ch_l "but maybe you're right."
                ch_l "Are you sure you're into this?"
                menu:
                    extend ""
                    "Yes, I'm sorry I was mean about it.":
                        call change_Girl_stat(LauraX, "love", 15)
                        call change_Girl_stat(LauraX, "inhibition", 10)
                        $ LauraX.change_face("bemused", 1)
                        $ LauraX.eyes = "side"
                        ch_l "Ok then."
                    "You're damned right I am, bitch.":
                        if "sir" in LauraX.player_petnames and approval_check(LauraX, 900, "O"):
                            call change_Girl_stat(LauraX, "love", -5)
                            call change_Girl_stat(LauraX, "obedience", 10)
                            ch_l ". . ."
                        elif approval_check(LauraX, 700, "O"):
                            call change_Girl_stat(LauraX, "love", -5)
                            call change_Girl_stat(LauraX, "obedience", 10)
                            ch_l "Hmmm. . ."
                        else:
                            call change_Girl_stat(LauraX, "love", -10)
                            call change_Girl_stat(LauraX, "obedience", -10)
                            call change_Girl_stat(LauraX, "obedience", -10)
                            call change_Girl_stat(LauraX, "inhibition", -15)
                            $ LauraX.change_face("angry", 1)
                            ch_l "Wow, that's pushing it."
                            $ line = "rude"
                    "Ok, never mind then.":
                        $ LauraX.change_face("angry", 1)
                        call change_Girl_stat(LauraX, "love", -10)
                        call change_Girl_stat(LauraX, "obedience", -10)
                        call change_Girl_stat(LauraX, "obedience", -10)
                        call change_Girl_stat(LauraX, "inhibition", -15)
                        ch_l "I was thinking of taking orders from you, not mindgames."
                        ch_l "I should've known you'd be like this."
                        $ line = "rude"

    $ LauraX.recent_history.append("asked sub")
    $ LauraX.daily_history.append("asked sub")
    if line == "rude":

        hide Laura_sprite with easeoutright
        call remove_Girl(LauraX)
        $ LauraX.recent_history.append("angry")
        if not simulation:
            $ renpy.pop_call()
        "[LauraX.name] checks you as she stomps out of the room."
    elif "sir" in LauraX.player_petnames:

        call change_Girl_stat(LauraX, "obedience", 50)
        $ LauraX.player_petnames.append("master")
        $ LauraX.player_petname = "master"
        $ LauraX.eyes = "squint"
        ch_l ". . . master. . ."
    else:

        call change_Girl_stat(LauraX, "obedience", 30)
        $ LauraX.player_petnames.append("sir")
        $ LauraX.player_petname = "sir"
        $ LauraX.change_face("sly", 1)
        ch_l ". . . sir."
    return






label Laura_Master:
    $ LauraX.drain_word("asked_to_meet")
    $ shift_focus (LauraX)
    if LauraX.location != Player.location and LauraX not in Player.Party:
        "Suddenly, [LauraX.name] shows up and says she needs to talk to you."


    call set_the_scene
    call show_Girl (LauraX)
    call clear_the_room (LauraX)
    call set_the_scene
    $ LauraX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ LauraX.change_face("sly", 1)
    ch_l "[LauraX.player_petname]. . ."
    ch_l ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 5)
        "What?":
            ch_l "I was asking if I could talk to you about something. . ."
            $ LauraX.eyes = "side"
            ch_l ". . . personal."
            $ LauraX.eyes = "squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    ch_l "Right. . ."
                "Oh, then no.":
                    $ LauraX.change_face("sad", 1)
                    call change_Girl_stat(LauraX, "love", -5)
                    call change_Girl_stat(LauraX, "obedience", -10)
                    $ line = "embarrassed"
        "No.":
            $ LauraX.change_face("perplexed", 1, brows = "confused")
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", -5)
            call change_Girl_stat(LauraX, "inhibition", -5)
            ch_l "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ LauraX.change_face("confused", 1)
                    call change_Girl_stat(LauraX, "obedience", 10)
                    call change_Girl_stat(LauraX, "inhibition", 10)
                    ch_l "Right. . ."
                "Yes, not interested.":
                    $ LauraX.change_face("sad", 1)
                    call change_Girl_stat(LauraX, "love", -5)
                    call change_Girl_stat(LauraX, "inhibition", -10)
                    $ line = "embarrassed"


    if not line:
        $ LauraX.change_face("sly", 1)
        ch_l "I think I enjoy having you in charge."
        ch_l "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                $ LauraX.change_face("sly", 1)
                call change_Girl_stat(LauraX, "obedience", 5)
                ch_l "Good. Maybe we could take this a bit more seriously?"
                menu:
                    extend ""
                    "Nah. This is just about perfect.":
                        $ LauraX.change_face("sad", 1)
                        call change_Girl_stat(LauraX, "obedience", -15)
                        call change_Girl_stat(LauraX, "love", 10)
                        $ line = "fail"
                    "What'd you have in mind?":
                        $ LauraX.eyes = "side"
                        ch_l "I was thinking I could start calling you. . . {i}master{/i}?"
                        $ LauraX.eyes = "squint"
                        menu:
                            extend ""
                            "Oh, yeah. I'd like that.":
                                call change_Girl_stat(LauraX, "obedience", 5)
                                ch_l "Good. . ."
                            "Um. . .nah. That's too much.":
                                $ LauraX.change_face("sadside", 1)
                                call change_Girl_stat(LauraX, "obedience", -15)
                                call change_Girl_stat(LauraX, "inhibition", 5)
                                $ line = "fail"
                    "Actually, I'd prefer we stopped doing it. Too much pressure.":

                        $ LauraX.change_face("sad", 1)
                        call change_Girl_stat(LauraX, "love", -5)
                        call change_Girl_stat(LauraX, "obedience", -10)
                        call change_Girl_stat(LauraX, "inhibition", 15)
                        $ line = "fail"
                    "Actually, let's stop that. It's creeping me out.":

                        $ LauraX.change_face("angry", 2, eyes = "surprised")
                        call change_Girl_stat(LauraX, "love", -10)
                        call change_Girl_stat(LauraX, "obedience", -50)
                        call change_Girl_stat(LauraX, "inhibition", -15)
                        ch_l "Say no more, I wouldn't want to CREEP YOU OUT."
                        $ line = "embarrassed"
            "As if I care what you think, slut.":

                $ LauraX.change_face("angry", 1, mouth = "smile")
                call change_Girl_stat(LauraX, "love", -20)
                call change_Girl_stat(LauraX, "obedience", 10)
                call change_Girl_stat(LauraX, "inhibition", -10)
                ch_l ". . ."
                menu:
                    ch_l "Excuse me?"
                    "Sorry. I just don't care what you want.":
                        if approval_check(LauraX, 1400, "LO"):
                            call change_Girl_stat(LauraX, "obedience", 10)
                            ch_l ". . ."
                            $ LauraX.change_face("sly", 1)
                            call change_Girl_stat(LauraX, "love", 20)
                            call change_Girl_stat(LauraX, "inhibition", 15)
                            ch_l ". . .{i}go on. . .{/i}"
                        else:
                            call change_Girl_stat(LauraX, "love", -15)
                            call change_Girl_stat(LauraX, "obedience", -10)
                            call change_Girl_stat(LauraX, "inhibition", 5)
                            $ LauraX.change_face("angry", 1)
                            ch_l "!!!"
                            $ line = "rude"
                    "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                        call change_Girl_stat(LauraX, "love", 10)
                        call change_Girl_stat(LauraX, "obedience", 10)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        if approval_check(LauraX, 1400, "LO"):
                            call change_Girl_stat(LauraX, "obedience", 10)
                            ch_l ". . ."
                            $ LauraX.change_face("sly", 1)
                            call change_Girl_stat(LauraX, "love", 20)
                            call change_Girl_stat(LauraX, "inhibition", 15)
                            ch_l ". . .{i}no, about right. . .{/i}"
                        else:
                            call change_Girl_stat(LauraX, "love", 5)
                            call change_Girl_stat(LauraX, "obedience", -5)
                            call change_Girl_stat(LauraX, "inhibition", 5)
                            $ LauraX.change_face("angry", 1, eyes = "side")
                            ch_l ". . ."
                            ch_l "We'll work on it. . ."
            "I don't really like it. Too much pressure.":

                $ LauraX.change_face("sad", 2)
                call change_Girl_stat(LauraX, "love", -20)
                call change_Girl_stat(LauraX, "obedience", -20)
                call change_Girl_stat(LauraX, "inhibition", -10)
                $ line = "embarrassed"

    $ LauraX.history.append("master")
    if line == "rude":
        $ LauraX.recent_history.append("angry")
        hide Laura_sprite with easeoutright
        call remove_Girl(LauraX)
        if not simulation:
            $ renpy.pop_call()
        "[LauraX.name] stomps out of the room."
    elif line == "embarrassed":
        ch_l "Ok, fine then."
        ch_l "And here I was, about to \"elevate your clearance.\""
        hide Laura_sprite with easeoutright
        call remove_Girl(LauraX)
        if not simulation:
            $ renpy.pop_call()
        "[LauraX.name] brushes past you on her way out."
    elif line == "fail":
        ch_l "Oh. . ."
        ch_l "I guess that's fine."
    else:
        call change_Girl_stat(LauraX, "obedience", 50)
        $ LauraX.player_petnames.append("master")
        $ LauraX.player_petname = "master"
        ch_l ". . .master."
    return







label Laura_Sexfriend:

    $ LauraX.lust = 70
    $ LauraX.location = Player.location
    $ LauraX.drain_word("asked_to_meet")
    call set_the_scene
    $ LauraX.daily_history.append("relationship")
    call set_Character_taboos
    $ line = 0
    $ LauraX.change_face("sly", 2, eyes = "side")
    "[LauraX.name] approaches you and pulls you aside. She seems to be shivering a little bit."
    "She seems to be squirming around and rubbing her thighs together."
    $ LauraX.player_petnames.append("sex friend")
    $ LauraX.change_face("sly", 2)
    if LauraX in Player.Harem:
        ch_l "Hey."
        ch_l "I need some alone time with you."
    elif "lover" in LauraX.player_petnames or "master" in LauraX.player_petnames or "lover" in LauraX.player_petnames or "sir" in LauraX.player_petnames:

        ch_l "Hey."
        ch_l "I need some alone time with you."
    else:

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
                $ LauraX.change_face("sly", 2, mouth = "smile")
                $ line = "yes"
            "No thanks":
                $ LauraX.change_face("confused", 2)
                $ line = "no"
            ". . .":
                call change_Girl_stat(LauraX, "obedience", 5)
                $ LauraX.change_face("confused", 2)

        if not line:
            ch_l "Now, if at all possible. . ."
            menu:
                extend ""
                "Sure":
                    $ LauraX.change_face("sly", 2, mouth = "smile")
                    $ line = "yes"
                "No thanks":
                    $ LauraX.change_face("confused", 2)
                    $ line = "no"

        if line == "no":
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 5)
            ch_l "What? Why not?"
            menu:
                extend ""
                "Ok, fine":
                    $ LauraX.change_face("confused", 2, mouth = "smile")
                    ch_l "Love the enthusiasm."
                    $ line = "yes"
                "Not interested":
                    $ LauraX.change_face("confused", 2)
                "There's someone else":

                    call change_Girl_stat(LauraX, "love", -5)
                    call change_Girl_stat(LauraX, "obedience", 5)
                    if Player.Harem:
                        $ LauraX.change_face("surprised", 2)
                        ch_l "Oh, [Player.Harem[0].name]?"
                        $ LauraX.check_if_likes(Player.Harem[0], 600, -25, 1)
                    $ LauraX.change_face("sly", 2)
                    ch_l "Well, she doesn't need to know about it. . ."
                    menu:
                        extend ""
                        "Ok, fine":
                            ch_l "Love the enthusiasm."
                            $ line = "yes"
                        "Still no":
                            pass

    if line == "no":
        call change_Girl_stat(LauraX, "love", -10)
        call change_Girl_stat(LauraX, "obedience", 15)
        call change_Girl_stat(LauraX, "inhibition", 10)
        $ LauraX.change_face("sad", 2)
        ch_l "Really?"
        ch_l "Bummer."
        ch_l "Well let me know if you change your mind."
        $ LauraX.change_face("sadside", 2, mouth = "lipbite", brows = "angry")
        if Player.Harem:
            ch_l "Wonder if [Player.Harem[0].name]'s busy. . ."
            $ LauraX.check_if_likes(Player.Harem[0], 500, 25, 1)
        else:
            ch_l "Wonder if Kitty's busy. . ."
            $ LauraX.check_if_likes("Kitty", 500, 25, 1)
    else:
        call change_Girl_stat(LauraX, "love", 10)
        call change_Girl_stat(LauraX, "obedience", 5)
        call change_Girl_stat(LauraX, "inhibition", 15)
        $ LauraX.change_face("sly", 1, mouth = "smile")
        if taboo:
            ch_l "Wanna take this party someplace else?"
            menu:
                extend ""
                "Yeah":
                    ch_l "Sure, let's go."
                    if Player.location == "bg_player":
                        $ Player.location = "bg_laura"
                    else:
                        $ Player.location = "bg_player"

                    call clear_the_room (LauraX)
                    call set_the_scene
                    $ taboo = 0
                    $ LauraX.taboo = 0
                "No, let's do it here.":

                    call change_Girl_stat(LauraX, "obedience", 5)
                    call change_Girl_stat(LauraX, "inhibition", 15)
                    ch_l "Kinky."

        $ Player.add_word(1, "interruption")
        call before_action(LauraX, "sex", context = LauraX)
        call enter_main_sex_menu(LauraX)



    return






label Laura_Fuckbuddy:
    $ LauraX.daily_history.append("relationship")
    $ LauraX.lust = 80
    $ LauraX.drain_word("asked_to_meet")

    "You hear a knock on the door, and go to answer it."

    $ LauraX.location = Player.location
    $ shift_focus (LauraX)
    call set_the_scene
    $ LauraX.outfit_name = "default"
    $ LauraX.today_outfit_name = "default"
    $ LauraX.change_Outfit()
    call show_Girl (LauraX)
    call set_Character_taboos
    $ Player.primary_Action = "masturbation"
    $ girl_secondary_Action = "fondle_pussy"
    $ LauraX.change_face("sly", 2, mouth = "lipbite")
    "[LauraX.name] is standing in the doorway, with her hand down her pants."
    "You can tell she's been masturbating furiously, her scent is overpowering."
    $ Player.primary_Action = None
    $ girl_secondary_Action = None
    $ LauraX.arm_pose = 1
    "She looks you up and down hungrily, and pulls her hand out of her pants."
    "She reaches up to caress your face, smearing her juices along it."
    ch_l "Mine."
    $ LauraX.player_petnames.append("fuck buddy")
    $ LauraX.event_happened[10] += 1

    $ Player.add_word(1, "interruption")
    call before_action(LauraX, "sex", LauraX)
    call enter_main_sex_menu(LauraX)

    return






label Laura_Daddy:
    $ LauraX.daily_history.append("relationship")
    $ LauraX.drain_word("asked_to_meet")
    $ shift_focus (LauraX)
    call set_the_scene
    ch_l ". . ."
    if LauraX in Player.Harem:
        ch_l "So we've been dating a while yeah?"
    else:
        ch_l "This thing we've got, pretty fun, right?"
    if LauraX.love > LauraX.obedience and LauraX.love > LauraX.inhibition:
        ch_l "and you've been really kind to me. . ."
    elif LauraX.obedience > LauraX.inhibition:
        ch_l "and you've been a good influence. . ."
    else:
        ch_l "like, really fun. . ."
    ch_l "So I've been thinking, would you want to be called. . ."
    ch_l "\"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ LauraX.change_face("smile")
            call change_Girl_stat(LauraX, "love", 20)
            call change_Girl_stat(LauraX, "obedience", 10)
            call change_Girl_stat(LauraX, "inhibition", 30)
            ch_l "Cool."
        "What do you mean by that?":
            $ LauraX.change_face("bemused")
            ch_l "I don't know, I've had some shitty father figures. . ."
            ch_l "I just. . ."
            if LauraX.love > LauraX.obedience and LauraX.love > LauraX.inhibition:
                ch_l "I think you could do better. . ."
            elif LauraX.obedience > LauraX.inhibition:
                ch_l "you've really been assertive. . ."
            else:
                ch_l "wouldn't it be kinky?"

            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ LauraX.change_face("smile")
                    call change_Girl_stat(LauraX, "love", 15)
                    call change_Girl_stat(LauraX, "obedience", 20)
                    call change_Girl_stat(LauraX, "inhibition", 25)
                    ch_l "Great!"
                    $ LauraX.change_face("sly", 2)
                    ch_l " . . . daddy."
                    $ LauraX.change_face("sly", 1)
                    $ LauraX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(LauraX, "love", 5)
                    call change_Girl_stat(LauraX, "obedience", 40)
                    call change_Girl_stat(LauraX, "inhibition", 20)
                    $ LauraX.change_face("sad")
                    ch_l " . . . "
                    ch_l "Well, ok."
                "You've got some real daddy issues, uh?":
                    call change_Girl_stat(LauraX, "love", -15)
                    call change_Girl_stat(LauraX, "obedience", 45)
                    call change_Girl_stat(LauraX, "inhibition", 5)
                    $ LauraX.change_face("angry")
                    ch_l "Yes. . . I said that."
        "You've got some real daddy issues, uh?":
            call change_Girl_stat(LauraX, "love", -15)
            call change_Girl_stat(LauraX, "obedience", 45)
            call change_Girl_stat(LauraX, "inhibition", 5)
            $ LauraX.change_face("angry")
            ch_l ". . . Probably."
            ch_l "Never mind."
    $ LauraX.player_petnames.append("daddy")
    return






label Gwentro:
    $ Player.add_word(1, "interruption")
    if taboo > 5 or RogueX.location == Player.location or KittyX.location == Player.location or EmmaX.location == Player.location:

        return
    $ LauraX.history.append("Gwentro")
    $ Gwen_name = "???"
    ch_g "Where is the exit to this place?!"
    call GwenFace ("angry")
    show Gwen_Sprite zorder 45 at sprite_location(1500):
        xzoom -1
    show Gwen_Sprite zorder 45 at sprite_location(100) with easeinright
    pause .1
    call GwenFace ("surprised")
    $ action_speed = 0
    $ LauraX.change_face("surprised", 2, eyes = "side")
    show Gwen_Sprite zorder 45 at sprite_location(200) with vpunch
    ch_g "Ouch!"
    call GwenFace ("angry")
    ch_g "Ok, that's a wall. . . apparently."
    call GwenFace ("surprised")
    ch_g "Oh, hey you tw-"
    call GwenFace ("surprised", 1, mouth = "kiss")
    ch_g "Um. . ."
    call GwenFace ("shocked", 1)
    ch_g "Sorry! My bad, I was just. . ."
    $ LauraX.change_face("confused", 2, eyes = "side")
    call GwenFace ("surprised", 1, mouth = "kiss")
    extend "\n looking for an exit. . ."
    call GwenFace ("smile", 1)
    extend "\n but you two. . . seem to be working on something. . ."
    call GwenFace ("sad", 1)
    extend "\n and now I can't see because of this stupid word balloon. . ."
    show Gwen_Sprite:
        ease 1 ypos 150
    call GwenFace ("smile", 1)
    extend ""
    ch_g "Better. . ."
    show Gwen_Sprite:
        ease 1 ypos 50
    ch_g "So now that we've got that taken care of, what's your name?"
    $ LauraX.change_face("angry", 1, eyes = "side")
    show Gwen_Sprite:
        ypos 50
    ch_g "So now that we've got that taken care of, what's your name?{w=0.2}{nw}"
    call GwenFace ("shocked", 0)
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
    call GwenFace ("surprised")
    ch_g "Sorry, it's just that menu popping up caught me by surprise."
    call GwenFace ("smile")
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
            $ Gwen_name = "Gwen"
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
    if Gwen_name != "Gwen":
        $ Gwen_name = "Gwen"
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
    $ LauraX.change_face("angry", eyes = "leftside")
    ch_g "Sorry, I should have said hello earlier, hey Laura!"
    $ LauraX.change_face("confused", eyes = "leftside")
    ch_l "How do you know my name!"
    ch_g "I've read all about you! Or do you prefer \"X-23?\""
    ch_g "Or \"Wolverine?\""
    call GwenFace ("surprised", mouth = "kiss")
    ch_g "God, it's not \"Talon,\" is it?"
    call GwenFace ("smile")
    ch_l "[LauraX.name] - is - fine."
    call GwenFace ("smile", mouth = "kiss")
    ch_g "Cool, so. . ."
    menu:
        "What are you doing here?":
            ch_p "What are you doing here?"
            ch_g "I had a feeling you would ask that."
        "Some other irrelvant option.":
            ch_p "What are you doing here?"
            ch_g "Man, determinism, am I right?"
    $ LauraX.change_face("confused", eyes = "leftside")
    ch_g "Why are any of us here, really?"
    ch_g "Oh! You mean \"why am I {i}here{/i}\" in this game?"
    call GwenFace ("sad")
    ch_g "Honestly? No idea. One minute I had an ongoing, then I was on a team book, guess that's cancelled now?"
    call GwenFace ("smile")
    ch_g "Yeah, your guess is as good as mine. Maybe whoever made it's a fan?"
    call GwenFace ("smile", 1)
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
    ch_g "Well, \"When in Rome. . .\"{w = 1.8}{nw}"
    call GwenFace ("angry", 1)
    ch_g "Huh."
    ch_g "Apparently I can't get my clothes off here."
    call GwenFace ("sad", 1)
    ch_g "That's unfortunate."
    call GwenFace ("angry", 1, mouth = "smile")
    ch_g "I could just stay and watch for a bit. . ."
    $ LauraX.change_face("angry", eyes = "leftside")
    call GwenFace ("surprised", 1)
    ch_l "NO!"
    ch_g "Right, right. Don't poke the wolverine. . ."
    call GwenFace ("smile", 1)
    ch_g "Except you, of course -wink-."
    call GwenFace ("sad", 0)
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
    call GwenFace ("sad", 1, eyes = "surprised")
    ch_g "Maybe never, we won't know."
    show Gwen_Sprite:
        ease .2 xpos 1500
    call GwenFace ("surprised")
    ch_l "Get out!"
    ch_g "Right! I'm gone, sorry!"
    hide Gwen_Sprite
    $ LauraX.change_face("bemused", eyes = "sexy")
    ch_l "Now, what were were doing. . ."

    return


label Laura_Dressup:


    $ active_Girls.append(LauraX) if LauraX not in active_Girls else active_Girls
    $ shift_focus (LauraX)
    $ Player.location = "bg_campus"
    call remove_all
    $ LauraX.location = Player.location
    call set_the_scene

    $ LauraX.outfit_name = "default"
    $ LauraX.change_Outfit()

    call show_Girl(LauraX, transition = vpunch)

    $ round -= 10 if round >= 11 else round
    $ LauraX.history.remove("dress0")
    $ LauraX.history.append("dress1")
    $ LauraX.history.append("met")
    "As you're heading across the square, you bump into [LauraX.name]."
    $ LauraX.change_face("normal")
    ch_l "Oh, hey."
    menu:
        extend ""
        "Ah, [LauraX.name]. You're back!":
            call change_Girl_stat(LauraX, "love", 3)
            call change_Girl_stat(LauraX, "obedience", 1)
            ch_l "Yeah, just got back."
        "Hey.":
            ch_l "Yeah, just got back."
        "Who are you again?":
            call change_Girl_stat(LauraX, "love", -3)
            call change_Girl_stat(LauraX, "obedience", 5)
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
            call change_Girl_stat(LauraX, "love", -1)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 5)
            $ LauraX.change_face("bemused")
            ch_l "Not really."

    hide Laura_sprite with easeoutright
    call remove_Girl(LauraX)
    "[LauraX.name] walks away, and as you watch her go you feel a tap on your shoulder."

    $ shift_focus (KittyX)
    $ KittyX.location = Player.location
    call set_the_scene
    $ KittyX.outfit_name = KittyX.today_outfit_name
    $ KittyX.change_Outfit()
    call show_Girl (KittyX)

    $ KittyX.change_face("smile")
    ch_k "Hey, [KittyX.player_petname], what're you staring at?"


    menu:
        extend ""
        "Hey, [KittyX.name]. I was just talking to [LauraX.name].":
            ch_k "Oh, she's back?"
        "Oh, nothing.":
            ch_k "Oh, I see, [LauraX.name]."
            ch_k "She's back?"
        "I was checking out that fine piece over there.":
            if approval_check(KittyX, 1200, "LO") or KittyX.permanent_History["been_with_girl"] >= 10:
                call change_Girl_stat(KittyX, "obedience", 5)
                call change_Girl_stat(KittyX, "inhibition", 5)
                $ KittyX.change_face("bemused", 1)
                ch_k "I guess I can't blame you. . ."
            else:
                call change_Girl_stat(KittyX, "love", -5)
                call change_Girl_stat(KittyX, "obedience", 10)
                call change_Girl_stat(KittyX, "inhibition", 5)
                $ KittyX.change_face("angry")
                ch_k "Rude much?"

    $ KittyX.change_face("smile", eyes = "side")
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
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "obedience", 5)
            ch_p "Here you go. What're you planning to get her?"
        "Nah, I don't really know her.":
            ch_k "Yeah, maybe you've got a point. She's kinda prickly sometimes."
            return
        "That could be kind creepy.":
            ch_k "Yeah, maybe you've got a point. She's kinda prickly sometimes."
            return


    ch_k "Well, she doesn't really have much of a wardrobe, so we were going to get her some new clothes."

    menu:
        extend ""
        "You're really stylish, so you'll probably pick out something great.":
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "inhibition", 3)
            $ KittyX.change_face("smile", 1)
            ch_k "Sweet talker."
        "That sounds good.":
            call change_Girl_stat(KittyX, "love", 2)
        "With your fashion sense? That'll end well.":
            call change_Girl_stat(KittyX, "love", -5)
            call change_Girl_stat(KittyX, "obedience", 5)
            call change_Girl_stat(KittyX, "inhibition", -3)
            $ KittyX.change_face("angry")
    ch_k "Anyway, we were thinking around $10 each."

    menu:
        extend ""
        "Here you go." if Player.cash >= 10:
            call change_Girl_stat(KittyX, "love", 1)
            call change_Girl_stat(KittyX, "obedience", 2)
            ch_k "Nice."
            $ Player.cash -= 10
            $ LauraX.history.append("dress2")
        "I don't have enough. . ." if Player.cash < 10:
            call change_Girl_stat(KittyX, "love", 1)
            call change_Girl_stat(KittyX, "obedience", 2)
            $ KittyX.change_face("normal", 1, brows = "surprised", mouth = "sad")
            ch_k "Oh."
            ch_k "We aren't in a rush or anything. If you still want to, just hit me up."
        "You know what, never mind.":
            call change_Girl_stat(KittyX, "love", -2)
            call change_Girl_stat(KittyX, "obedience", -1)
            $ KittyX.change_face("normal", 1, brows = "surprised", mouth = "sad")
            ch_k "Oh, ok."
    return

label Laura_Dressup2:

    ch_p "Hey, remember that gift you wanted to give [LauraX.name] earlier?"
    $ KittyX.change_face("smile")
    ch_k "Yeah?"
    menu:
        extend ""
        "Here you go, $10.":
            call change_Girl_stat(KittyX, "love", 1)
            call change_Girl_stat(KittyX, "obedience", 2)
            ch_k "Cool."
            $ LauraX.history.append("dress2")
        "Never mind.":
            ch_k "Oh, ok."
    return


label Laura_Dressup3:


    $ LauraX.history.remove("dress1")
    $ LauraX.history.remove("dress2")
    $ LauraX.history.append("dress3")
    $ LauraX.inventory.append("wolvie_bra")
    $ LauraX.inventory.append("wolvie_panties")

    "You're walking past [KittyX.name]'s door when you hear her laughing at something."
    "You hear someone else's voice, there's clearly someone else in her room with her."

    ch_l "[KittyX.name], you shouldn't have."
    ch_l "No, seriously. . ."
    ch_l "you shouldn't have."
    ch_k "Aww, c'mon. You look great."

    "You remember [KittyX.name] talking about getting [LauraX.name] some new clothes. She must've gotten [LauraX.name] to try them on."
    "You can't help but feel curious. . ."

    $ KittyX.outfit_name = KittyX.today_outfit_name
    $ KittyX.change_Outfit()
    $ LauraX.undress()
    $ LauraX.Clothes["bra"] = "wolvie_bra"
    $ LauraX.Clothes["underwear"] = "wolvie_panties"
    menu:
        extend ""
        "Sneak a peek [[no key] (locked)" if KittyX not in Player.Keys:
            pass
        "Sneak a peek" if KittyX in Player.Keys:
            "You use your key and unlock the door, opening it and sticking your head in."
            ch_p "Hey, [KittyX.name], what's going on?"
            ch_k "Hey, [KittyX.player_petname]! Come on in!"

            $ Player.location = "bg_kitty"

            call clear_the_room ("all", 0, 1)
            $ shift_focus (LauraX)
            $ KittyX.location = "bg_kitty"
            $ LauraX.location = "bg_kitty"
            call set_the_scene

            $ LauraX.change_face("sad", 2, eyes = "squint", brows = "confused")
            "[LauraX.name] stares at you, her eyes narrowed. She's clearly on edge."
            $ LauraX.change_face("sad", 2, brows = "confused", eyes = "leftside")
            ch_l "Didn't you lock the door?"
            if KittyX.permanent_History["sleepover"] < 5:
                $ KittyX.change_face("smile", eyes = "side")
                ch_k "Yeah, but I gave him a key."
                $ LauraX.change_face("sad", 1, brows = "confused", eyes = "leftside")
                ch_l "You. . . gave him a key?"
            else:

                $ KittyX.change_face("confused", eyes = "side")
                ch_k "Yeah, I'm not really sure how he got a key. . ."
                if not approval_check(KittyX, 1200):

                    $ KittyX.change_face("angry", 1)
                    ch_k "Ok, that's enough, out, out!"
                    "You head back out."
                    return
                $ KittyX.change_face("smile")
                ch_k "I guess it's fine though. . ."
                $ LauraX.change_face("sad", 1, brows = "confused", eyes = "leftside")
                ch_l "It's fine that he got a mystery key?"
            $ KittyX.change_face("smile", 1)
            ch_k "Uh-huh. I mean, he's my [KittyX.player_petname]."
            ch_l "Your. . . [KittyX.player_petname]."
        "Knock":
            "You knock on the door."
            ch_k "Who is it?"
            ch_p "It's [Player.name], mind if I come in?"
            if not approval_check(KittyX, 1000):
                ch_k "Um, sorry [KittyX.player_petname], we're a little busy in here."
                ch_k "[KittyX.Like]maybe check back later?"
                ch_p "Sure, no problem."
                "You head back out."
                return
            ch_k "Sure, [KittyX.player_petname]! Gimme a sec!"
            "[KittyX.name] unlocks the door and it swings open."

            $ Player.location = "bg_kitty"

            call clear_the_room ("all", 0, 1)
            $ shift_focus (LauraX)
            $ KittyX.location = "bg_kitty"
            $ LauraX.location = "bg_kitty"
            call set_the_scene

            $ LauraX.change_face("sad", 2, brows = "surprised")
            "[LauraX.name] stares at you, as if she's not sure what she's seeing."
            $ LauraX.change_face("sad", 2, brows = "confused", eyes = "leftside")
            ch_l "So you just let him come into your room whenever?"
            $ KittyX.change_face("smile", 1)
            ch_k "Uh-huh. I mean, he's my [KittyX.player_petname]."
            ch_l "Your. . . [KittyX.player_petname]."
        "Walk away":

            "Nah, I should let them have their girl time."
            return
    $ LauraX.seen_underwear = 1
    $ LauraX.change_face("angry", 1, eyes = "closed")
    "She shakes her head, trying to absorb all this new information."
    "She mutters to herself."
    ch_l "I've been gone longer than I thought. . ."
    $ LauraX.change_face("sad", 1, brows = "confused", eyes = "leftside")
    ch_l "So why's he here?"
    $ KittyX.change_face("smile", eyes = "side")
    ch_k "Well, he kind of pitched in to get you this stuff, so why not see what he thinks?"
    "[KittyX.name] walks over and poses like she's presenting [LauraX.name] as a model."
    $ KittyX.arm_pose = 2
    $ KittyX.change_face("smile")
    ch_k "So, what do you think?"

    menu:
        extend ""
        "Her outfit looks familiar. . .":
            ch_k "I call it the Logan Look."
            $ LauraX.change_face("sad", 2, eyes = "stunned")
            call change_Girl_stat(LauraX, "inhibition", -2)
            ch_l "Please don't call it that."
        "Looking good, [LauraX.name]!":
            call change_Girl_stat(LauraX, "love", 5)
            call change_Girl_stat(LauraX, "obedience", 3)
            call change_Girl_stat(LauraX, "inhibition", 5)
            $ LauraX.check_if_likes(KittyX, 700, 5, 1)
            $ LauraX.change_face("sadside", 1)
            ch_l "Yeah, well. . . [KittyX.name] knows her stuff."
            call change_Girl_stat(KittyX, "love", 1)
            call change_Girl_stat(KittyX, "obedience", 3)
            $ KittyX.check_if_likes(LauraX, 700,3, 1)
            ch_k "Heh, thanks."
        "Great ensemble, [KittyX.name]! It looks great on her!":
            call change_Girl_stat(KittyX, "love", 5)
            call change_Girl_stat(KittyX, "obedience", 3)
            ch_k "Hey, I know my stuff, y'know?"
            call change_Girl_stat(LauraX, "love", 3)
            call change_Girl_stat(LauraX, "obedience", 2)
            call change_Girl_stat(LauraX, "inhibition", 5)
            $ LauraX.change_face("bemused", 1)
            $ LauraX.check_if_likes(KittyX, 700,3, 1)
            ch_l "Yeah, I guess she does. . ."
        "Can I get a refund?":
            call change_Girl_stat(KittyX, "love", -5)
            call change_Girl_stat(KittyX, "obedience", -3)
            $ KittyX.change_face("angry")
            ch_k "Way to bring down the mood."
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", -5)
            $ LauraX.change_face("angry")
            ch_l "Seriously."

    $ LauraX.change_face("smile", 0, eyes = "leftside")
    $ LauraX.check_if_likes(KittyX, 700, 5, 1)
    $ KittyX.check_if_likes(LauraX, 700, 5, 1)
    ch_l "But really, [KittyX.name], thanks for this."
    $ KittyX.change_face("smile", eyes = "side")
    ch_k "No problem! Like, what're friends for?"
    ch_l "Pretty sure friends don't normally use their friends as dressup dolls."
    ch_k "Oh, [LauraX.name], you have sooooo much to learn."
    $ LauraX.change_face("smile", eyes = "down")
    "[LauraX.name] smiles just a little bit and looks down at herself."
    ch_l "I think wearing the whole outfit is a bit much."
    $ LauraX.change_face("smile", eyes = "leftside")
    ch_l "You know that Logan's going to have a few words if he sees me like this."
    $ KittyX.change_face("smile", eyes = "side")
    ch_k "Hey, it's your outfit now. Mix-and-match, girl!"
    ch_l "Yeah. Yeah, I think I'll do that."
    $ LauraX.names.append("Wolverine")

    $ KittyX.change_face("smile")
    $ LauraX.change_face("sly", 1)
    "[LauraX.name] fixes you with a steely gaze."

    ch_l "So. . . I'd like to change now."

    menu:
        extend ""
        "Go right ahead!":
            call change_Girl_stat(LauraX, "obedience", 3)
            call change_Girl_stat(LauraX, "inhibition", 3)
            if (not LauraX.seen_breasts or not LauraX.seen_pussy) and not approval_check(LauraX, 1400):
                call change_Girl_stat(LauraX, "love", -5)
                $ LauraX.change_face("angry", 1)
                ch_l "I don't think so."
                ch_k "Yeah, I think you'd better get going, [KittyX.player_petname]. . ."
                ch_k ". . .Before she does to you what Logan does to people who make him mad."
                "[KittyX.name] firmly escorts you to the door."
            else:
                if LauraX.seen_breasts and LauraX.seen_pussy:
                    ch_l "Fair enough. . ."
                elif approval_check(LauraX, 1400):
                    ch_l "Bold choice. . ."
                $ KittyX.change_face("surprised", 2, eyes = "side")
                $ LauraX.take_off("bra")
                "[LauraX.name] starts stripping out of the new clothes. . ."
                if approval_check(KittyX, 1200):
                    $ KittyX.change_face("sly", 1)
                else:
                    $ KittyX.change_face("angry", 1, eyes = "side")

                $ LauraX.take_off("underwear")
                call Laura_First_Topless
                call Laura_First_Bottomless (1)
                pause 1
                $ LauraX.change_Outfit(LauraX.today_outfit_name,)
                "And then puts on her usual outfit."

                if approval_check(KittyX, 1200):
                    $ KittyX.change_face("sly", 1)
                else:
                    $ KittyX.change_face("angry", 1)
                ch_k "Well, I guess you got your show for the day."
                ch_k "Now give us some girl time."
                "[KittyX.name] shoos you out of the room and you head to the campus square."
        "Message received. See you girls later!":

            ch_k "Later, [KittyX.player_petname]!"
            ch_l "See ya."

    $ round -= 20 if round >= 21 else round

    $ Player.location = "bg_campus"

    jump reset_location
    return





label Laura_Foul:
    $ LauraX.history.remove("partyfoul")
    if "partysolved" in LauraX.history:
        $ LauraX.history.remove("partysolved")
    $ LauraX.add_word(1, 0, 0, 0, "partyfix")
    $ LauraX.change_face("sad", 1)
    if LauraX.location == Player.location or LauraX in Player.Party:
        "[LauraX.name] glances over at you with a distressed look."
    else:
        "[LauraX.name] turns a corner and notices you."
    if Player.location != "bg_laura" and Player.location != "bg_player":
        "With little word, she moves behind you and pushes you towards her room."
        $ Player.location = "bg_laura"

    call set_the_scene
    call clear_the_room (LauraX)
    call set_the_scene
    call set_Character_taboos
    ch_l "Hey. . ."
    ch_l "[LauraX.player_petname]. . ."
    ch_l "About that time at the party. . ."
    menu:
        extend ""
        "What time at the party?":
            call change_Girl_stat(LauraX, "love", -2)
            call change_Girl_stat(LauraX, "obedience", 2)
            call change_Girl_stat(LauraX, "inhibition", 1)
            $ LauraX.change_face("confused", 2)
        "Oh, yeah. I'm sorry about that.":
            call change_Girl_stat(LauraX, "love", 5)
            call change_Girl_stat(LauraX, "love", 5)
            $ LauraX.change_face("surprised", 2)
            $ LauraX.add_word(1, "sorry", 0, 0, 0)
            $ LauraX.change_face("smile", 1)
        "Yeah?":
            call change_Girl_stat(LauraX, "obedience", 1)
            call change_Girl_stat(LauraX, "inhibition", 1)
            $ LauraX.change_face("sad", 1)
        ". . .":
            call change_Girl_stat(LauraX, "love", -1)
            call change_Girl_stat(LauraX, "obedience", 2)
            $ LauraX.change_face("sad", 1)

    if "sorry" not in LauraX.recent_history:

        $ LauraX.change_face("sadside", 1)
        ch_l "We were at the Halloween Player.Party. . ."
        $ LauraX.change_face("sad", 1)
        ch_l "And you said something about my costume. . ."
        menu:
            extend ""
            "I don't remember, what did I say?":
                call change_Girl_stat(LauraX, "love", -3)
                $ LauraX.change_face("surprised", 1)
            "Oh, yeah. I'm sorry about that.":
                $ LauraX.change_face("smile", 1)
                call change_Girl_stat(LauraX, "love", 5)
                call change_Girl_stat(LauraX, "love", 5)
                $ LauraX.add_word(1, "sorry", 0, 0, 0)
            "Did I?":
                $ LauraX.change_face("surprised", 1)
                ch_l ". . ."
                call change_Girl_stat(LauraX, "love", -5)
                call change_Girl_stat(LauraX, "obedience", 3)
                call change_Girl_stat(LauraX, "obedience", 2)
                $ LauraX.change_face("angry", 1)
            ". . .":
                call change_Girl_stat(LauraX, "love", -1)
                $ LauraX.change_face("angry", 1)

    if "sorry" not in LauraX.recent_history:

        ch_l "You said that it looked like a. . ."
        ch_l "A prostitute."
        menu:
            extend ""
            "Oooh. Ouch. Yeah.":
                $ LauraX.change_face("sly", 1)
                call change_Girl_stat(LauraX, "love", 2)
                call change_Girl_stat(LauraX, "love", 2)
                call change_Girl_stat(LauraX, "inhibition", 2)
            "Oh, yeah. I'm sorry about that.":
                $ LauraX.change_face("smile", 1)
                call change_Girl_stat(LauraX, "love", 2)
                call change_Girl_stat(LauraX, "love", 5)
                $ LauraX.add_word(1, "sorry", 0, 0, 0)
            "Is that a problem?":
                $ LauraX.change_face("surprised", 1)
                pause 0.5
                $ LauraX.change_face("angry", 1)
                call change_Girl_stat(LauraX, "love", -5)
                call change_Girl_stat(LauraX, "love", -5)
                call change_Girl_stat(LauraX, "obedience", 5)
                ch_l "Of -course- it's a -problem-. . ."
            "Huh.":
                call change_Girl_stat(LauraX, "love", -3)
                call change_Girl_stat(LauraX, "obedience", 5)
                $ LauraX.change_face("surprised", 1)
            ". . .":
                call change_Girl_stat(LauraX, "love", -2)
                call change_Girl_stat(LauraX, "love", -2)
                $ LauraX.change_face("angry", 1)

    if "lover" in LauraX.player_petnames:
        ch_l "You understand why this would.. bother me. . ."
        menu:
            extend ""
            "Oh. . . yeah.":
                $ LauraX.change_face("normal", 1, eyes = "side")
                call change_Girl_stat(LauraX, "love", 1)
                call change_Girl_stat(LauraX, "inhibition", 2)
                $ LauraX.add_word(1, "nyx", 0, 0, 0)
            "I'm sorry, I must have missed it.":
                $ LauraX.change_face("confused", 2)
                call change_Girl_stat(LauraX, "love", -3)
                ch_l "Seriously?"
                $ LauraX.change_face("angry", 1)
            "What? Why?":
                $ LauraX.change_face("confused", 2)
                call change_Girl_stat(LauraX, "love", -5)
                ch_l "Seriously?"
                $ LauraX.change_face("angry", 1)

    if "nyx" not in LauraX.recent_history:
        ch_l "Maybe you don't understand why this cuts deep. . ."
        ch_l ". . ."
        $ LauraX.change_face("sadside", 1)
        ch_l "When I was younger, on my own. . ."
        call change_Girl_stat(LauraX, "inhibition", 1)
        ch_l "I had to do some things. . ."
        $ LauraX.blushing = "_blush2"
        call change_Girl_stat(LauraX, "inhibition", 1)
        ch_l "On the streets."
        $ LauraX.change_face("sad", 1)
        ch_l "So I don't want to be called. . . that."

    menu:
        extend ""
        "Oh, I'm so sorry.":
            call change_Girl_stat(LauraX, "love", 5)
            $ LauraX.change_face("smile", 1, eyes = "side")
            ch_l "Thanks. . ."
            $ LauraX.change_face("smile", 1)
            $ LauraX.add_word(1, "sorry", 0, 0, 0)
        "Yeah, I get it.":
            call change_Girl_stat(LauraX, "love", 2)
            call change_Girl_stat(LauraX, "love", 3)
            call change_Girl_stat(LauraX, "obedience", 1)
            call change_Girl_stat(LauraX, "inhibition", 1)
            $ LauraX.change_face("smile", 1)
            ch_l "Thanks."
            $ LauraX.add_word(1, "sorry", 0, 0, 0)
        "Oh, ok.":
            if approval_check(LauraX, 1200) or approval_check(LauraX, 400, "O"):
                call change_Girl_stat(LauraX, "obedience", 3)
                call change_Girl_stat(LauraX, "obedience", 2)
                call change_Girl_stat(LauraX, "inhibition", 3)
                $ LauraX.change_face("sly", 1)
            else:
                call change_Girl_stat(LauraX, "love", -5)
                call change_Girl_stat(LauraX, "obedience", 5)
                $ LauraX.change_face("angry", 1)
            ch_l ". . ."
        "Ha! Get over it.":
            $ LauraX.change_face("angry", 1)
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "obedience", 5)
            call change_Girl_stat(LauraX, "inhibition", 5)
            ch_l "Asshole."
            $ LauraX.drain_word("sorry", 1, 0, 0)
    menu:
        extend ""
        "Won't happen again.":
            if "sorry" not in LauraX.recent_history:
                $ LauraX.change_face("confused", 1)
                ch_l "So you're sorry then?"
                menu:
                    "Yeah, of course!":
                        $ LauraX.change_face("smile", 1)
                        call change_Girl_stat(LauraX, "love", 3)
                        ch_l "Good."
                        $ LauraX.add_word(1, "sorry", 0, 0, 0)
                    "Eh, I guess?":
                        ch_l ". . ."
                        if approval_check(LauraX, 1200) or approval_check(LauraX, 400, "O"):
                            $ LauraX.change_face("normal", 1)
                            call change_Girl_stat(LauraX, "love", 2)
                            call change_Girl_stat(LauraX, "love", 2)
                            call change_Girl_stat(LauraX, "obedience", 2)
                            call change_Girl_stat(LauraX, "inhibition", 1)
                            ch_l "Good enough."
                            $ LauraX.add_word(1, "sorry", 0, 0, 0)
                        else:
                            call change_Girl_stat(LauraX, "love", -5)
                            call change_Girl_stat(LauraX, "obedience", 3)
                            call change_Girl_stat(LauraX, "inhibition", 1)
                            $ LauraX.change_face("angry", 1)
                            ch_l "Not good enough."
                    "For what?":
                        $ LauraX.change_face("angry", 1)
                        call change_Girl_stat(LauraX, "love", -5)
                        call change_Girl_stat(LauraX, "love", -5)
                        call change_Girl_stat(LauraX, "obedience", 5)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        call change_Girl_stat(LauraX, "inhibition", 5)
                        ch_l "Grrrrrr."
            else:
                $ LauraX.change_face("angry", 1, mouth = "smile")
                call change_Girl_stat(LauraX, "obedience", 2)
                call change_Girl_stat(LauraX, "inhibition", 3)
                ch_l "It'd better not."
        "That all?":

            $ LauraX.change_face("angry", 1)
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "love", -5)
            call change_Girl_stat(LauraX, "inhibition", 10)
            ch_l "Seriously?!"

    if "sorry" in LauraX.recent_history:
        $ LauraX.change_face("smile", 1)
        ch_l "I'm glad that you care, at least."
    else:
        $ LauraX.change_face("angry", 1)
        $ LauraX.add_word(1, "angry", "angry", 0, 0)
        ch_l "Well if that's how you feel about it, you can fuck right off!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
