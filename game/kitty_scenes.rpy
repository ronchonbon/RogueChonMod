


label KittyMeet:
    $ bg_current = "bg_campus"
    $ KittyX.OutfitDay = "casual1"
    $ KittyX.Outfit = "casual1"
    $ KittyX.change_outfit("casual1")
    call clear_the_room ("All", 0, 1)
    $ KittyX.location = "bg_kitty"
    $ KittyX.love = 400
    $ KittyX.obedience = 100
    $ KittyX.inhibition = 0
    call shift_focus (KittyX)
    call set_the_scene (0)
    $ KittyX.sprite_location = stage_center
    $ KittyX.player_petname = Player.name[:1]

    "As you rush to class, you see another student running straight at you."
    "You try to move aside, but aren't fast enough to get out of her way,"
    "She crashes into you at a full jog, and you both fall to the ground."
    "You scramble to your feet and offer the girl a hand up."
    show Kitty_Sprite at sprite_location(KittyX.sprite_location) with vpunch
    $ KittyX.location = "bg_campus"
    $ KittyX.change_stat("love", 90, -25)
    $ KittyX.change_face("surprised")
    $ KittyX.ArmPose = 1
    ch_u "Hey!"
    $ KittyX.brows = "angry"
    ch_u "What the hell was that?"
    $ counter = 1

    menu:
        extend ""
        "You crashed into me!":
            $ KittyX.change_face("confused", 2)
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 80, 20)
            ch_u "Wha! Well, yeah. . ."
            $ KittyX.blushing = 1
            $ counter = 0
        "Sorry about that.":
            $ KittyX.change_face("bemused", 1)
            $ KittyX.eyes = "side"
            $ KittyX.change_stat("love", 90, 25)
            ch_u "Well, I guess it[KittyX.like]wasn't entirely your fault. . ."
        "A meet-cute?":
            $ KittyX.change_face("surprised", 2)
            $ KittyX.change_stat("love", 90, 15)
            $ KittyX.change_stat("inhibition", 70, 10)
            ch_u " ! "
            $ KittyX.change_face("bemused", 1)
            ch_u "Hmm. . . maybe. . ."

    ch_p "My name's [Player.name], by the way."
    if counter:
        $ KittyX.change_face("smile", 1)
        ch_k "Mine's Kitty! Kitty Pryde. Nice to meet you!"
    else:
        $ KittyX.change_face("sadside", 1)
        ch_k "Um, mine's Kitty."
    $ KittyX.change_face("normal", 1)
    $ KittyX.mouth = "sad"
    ch_k "I just[KittyX.like]didn't expect to bounce off you like that. Normally I can phase through things."

    menu:
        extend ""
        "Losing your touch?":
            $ KittyX.change_face("confused", 0)
            $ KittyX.change_stat("obedience", 80, 5)
            ch_k "I don't {i}think{/i} that's it. . ."
            ch_p "Just kidding. . ."
            $ KittyX.change_stat("love", 90, 5)
        "Was I too distracting?":
            $ KittyX.change_face("angry", 1, Brows = "normal")
            $ KittyX.change_stat("love", 90, -2)
            $ KittyX.change_stat("obedience", 80, 8)
            $ KittyX.change_stat("inhibition", 70, 4)
            ch_k "Like, no."
            ch_p "Heh, I guess not."
        "It must be my powers.":
            $ KittyX.change_face("confused", 0)
            $ KittyX.change_stat("love", 90, 5)
            ch_k "Oh?"

    ch_p "I have the ability to negate mutant powers, so you can't phase through me."
    $ KittyX.change_face("perplexed", 0)
    ch_k "Oh! Wow, that's an interesting power. So if you grab me, I can't get away?"

    menu:
        extend ""
        "Want to give it a try?":
            $ KittyX.change_face("perplexed", 0)
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("inhibition", 70, 5)
            ch_k "I'm definitely curious."
        "I guess so.":
            $ KittyX.change_face("sadside", 0, Mouth = "lipbite")
            $ KittyX.change_stat("obedience", 80, 3)
            $ KittyX.change_stat("inhibition", 70, 7)
            ch_k "I'd like to give it a try."
        "Does that turn you on?":
            $ KittyX.change_face("surprised", 2)
            $ KittyX.change_stat("obedience", 80, 5)
            ch_k "What?! No! . ."
            $ KittyX.change_face("bemused", 1)
            $ KittyX.change_stat("inhibition", 70, 5)
            $ KittyX.eyes = "side"
            ch_k ". . . no."
            $ KittyX.eyes = "sexy"
            ch_k "But it is[KittyX.like]worth testing."

    ch_p "Ok, let's give it a shot."
    "You reach out and grab her wrist."
    $ KittyX.change_face("angry", 1, Eyes = "down")
    $ KittyX.addiction_rate += 2
    "She struggles for a few moments to shake you free, but you hold firm."
    $ counter = 0
    while counter < 3:
        menu:
            extend ""
            "Let her go.":
                if not counter:
                    $ KittyX.change_stat("love", 90, 7)
                    $ KittyX.change_stat("inhibition", 70, -2)
                elif counter == 1:
                    $ KittyX.change_stat("love", 90, 10)
                else:
                    $ KittyX.change_stat("love", 90, 5)
                "You release her arm and step back."
                $ counter = 4
            "Hold on.":
                "You continue to hold onto her arm and she fidgets uncomfortably."
                if not counter:
                    $ KittyX.eyes = "sexy"
                    ch_k "Are you[KittyX.like]going to let go of my arm any time soon?"
                elif counter == 2:
                    ch_k "Ok, that's enough!"
                    $ KittyX.eyes = "sexy"
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 80, -5)
                    $ KittyX.change_stat("inhibition", 70, 10)
                    "She reaches over and pries your hand loose."
                    $ counter = 4
                else:
                    $ KittyX.change_stat("love", 90, -1)
                    $ KittyX.change_stat("obedience", 80, 2)
                    "Um. . ."
                $ counter += 1
                $ KittyX.addiction_rate += 1
            "Pull her in for a hug.":

                $ KittyX.change_stat("love", 90, -5)
                $ KittyX.change_face("surprised", 2)
                ch_k "Hey! Like, not cool!"
                $ KittyX.change_face("angry", 1)
                show Kitty_Sprite at sprite_location(KittyX.sprite_location) with vpunch
                "She elbows you in the ribs and shoves herself back a few steps."
                $ KittyX.change_stat("inhibition", 70, 10)
                ch_k "My powers may not work on you, but I have[KittyX.like]a few years of combat experience on you."
                ch_k "And don't you forget it!"
                $ counter = 10

    if counter > 3:
        $ KittyX.eyes = "side"
        ch_k "Still though, that was an interesting experience. . ."
    else:
        $ KittyX.change_face("bemused", 1, Eyes = "side")
        ch_k "That was an interesting experience. . ."
    $ KittyX.eyes = "sexy"
    $ KittyX.mouth = "lipbite"
    ch_k "Kinda tingly. . ."

    $ counter = 0
    $ KittyX.change_face("surprised", Mouth = "kiss")
    ch_k "Oh! I[KittyX.like]totally forgot, I have to get to a briefing!"
    if counter < 5:
        $ KittyX.change_face("smile")
        ch_k "I'll see you later though! Like, bye!"
    else:
        $ KittyX.change_face("normal")
        ch_k "I'll see you around I guess. Like, bye!"

    $ KittyX.location = "bg_kitty"
    call set_the_scene

    "She jogs off down the path, and you continue on to class."
    $ KittyX.history.append("met")
    $ active_Girls.append(KittyX) if KittyX not in active_Girls else active_Girls
    $ bg_current = "bg_classroom"
    $ Round -= 10
    call shift_focus (RogueX)
    return







label Kitty_Key:
    call shift_focus (KittyX)
    call set_the_scene
    $ KittyX.change_face("bemused")
    $ KittyX.ArmPose = 2
    ch_k "So you've[KittyX.like]been dropping by a lot lately, I figured you might want a key. . ."
    ch_p "Thanks."
    $ KittyX.ArmPose = 1
    $ Keys.append(KittyX)
    $ KittyX.Event[0] = 1
    return





label Kitty_BF:
    call shift_focus (KittyX)
    $ KittyX.DrainWord("asked meet")
    if KittyX.location != bg_current:
        $ KittyX.location = bg_current
        if KittyX not in Party:
            "[KittyX.name] approaches you and asks if the two of you can talk."
        else:
            "[KittyX.name] turns towards you and asks if the two of you can talk."

    call set_the_scene (0)
    call Display_Girl (KittyX)
    "A little blush on her cheeks, you can tell she's a bit anxious about whatever she has to say."
    call Taboo_Level
    call clear_the_room (KittyX)
    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("bemused", 1)

    ch_k "So, [KittyX.player_petname], we've[KittyX.like]been hanging for a while, right?"
    ch_k ". . ."
    $ KittyX.eyes = "sexy"
    menu:
        ch_k "Right?"
        "Yeah. And it's been amazing.":
            $ KittyX.change_stat("love", 200, 20)
        "Yeah, I guess":
            $ KittyX.change_stat("love", 200, 10)
        "Uhm. . .maybe?":
            $ KittyX.change_stat("love", 200, -10)
            $ KittyX.change_stat("obedience", 200, 30)
    if KittyX.SEXP >= 10:
        ch_k "I mean, I've gone further with you than I've ever been with anybody before. . ."
    if KittyX.SEXP >= 15:
        ch_k "You know[KittyX.like]. . .in the {i}bedroom{/i}. . ."
    if len(Player.Harem) >= 2:
        ch_k "I know you[KittyX.like]really get around and all. . ."
    elif RogueX in Player.Harem:
        if "dating?" in KittyX.Traits:
            ch_k "I know you're kinda[KittyX.like][RogueX.name]'s boyfriend and all. . . but she and I were talking and[KittyX.like]. . ."
        else:
            ch_k "I know you're kinda[KittyX.like][RogueX.name]'s boyfriend and all. . ."
    elif Player.Harem:
        ch_k "I know you're kinda[KittyX.like]dating [Player.Harem[0].name] and all. . ."

    if not KittyX.Event[5]:
        ch_k "So, uhm. . ."
        ch_k "It’s not like I[KittyX.like]haven’t gone out with guys before."
        ch_k "I just[KittyX.like].wow, this is so awkward. I really like you a lot and. . ."
        ch_k "I mean. . . do you wanna[KittyX.like]be my boyfriend?"
        ch_k "[KittyX.Like]maybe we could make it official?"
    elif "dating?" in KittyX.Traits:
        ch_k "[RogueX.name] said it’d totally be cool if we were[KittyX.like]dating, too."
    elif Player.Harem:
        ch_k "If you were okay with it. . . I’d still like to be your girlfriend, too."
    else:
        ch_k "I wish you weren’t[KittyX.like]such a jerk sometimes, but still. . . I’m totally serious about this."
        ch_k "I wanna be your girlfriend[KittyX.like]officially."
    $ KittyX.Event[5] += 1
    menu:
        extend ""
        "Are you kidding? I'd love to!":
            $ KittyX.change_stat("love", 200, 30)
            "[KittyX.name] wraps her arms around you and starts kissing you passionately."
            $ KittyX.change_face("kiss")
            call Kitty_Kissing_Launch ("kiss")
            $ KittyX.action_counter["kiss"] += 1
        "Uhm[KittyX.like]okay.":
            $ KittyX.brows = "confused"
            "[KittyX.name] seems a little put off by how casually you’re taking all this."
            "Still, she must think it’s a good first step, at least, because she leans into you and gives you a hug."
        "I'm with someone else now." if Player.Harem:
            $ KittyX.change_face("sad",1)
            ch_k "I know. I just[KittyX.like]. . . I thought maybe you could go out with me, too, maybe?"
            menu:
                extend ""
                "Yes. Absolutely." if "KittyYes" in Player.Traits:
                    $ KittyX.change_stat("love", 200, 30)
                    "[KittyX.name] wraps her arms around you and starts kissing you passionately."
                    $ KittyX.change_face("kiss")
                    call Kitty_Kissing_Launch ("kiss")
                    $ KittyX.action_counter["kiss"] += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                    $ Line = "no"
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ Line = "no"
                "I'm sorry, but. . . no." if KittyX.Event[5] != 20:
                    $ Line = "no"
                "No way.":
                    jump Kitty_BF_Jerk
            if Line == "no":
                $ KittyX.change_stat("love", 200, -10)
                ch_k "Well. . . okay. I get it."
                $ KittyX.Event[5] = 20
                call Remove_Girl (KittyX)
                $ Line = 0
                return
        "Not really.":
            jump Kitty_BF_Jerk

    if "Historia" not in Player.Traits:
        $ Player.Harem.append(KittyX)
        if "KittyYes" in Player.Traits:
            $ Player.Traits.remove("KittyYes")
    $ KittyX.player_petnames.append("boyfriend")
    $ KittyX.change_face("sexy")
    ch_k "Now. . . boyfriend. . . how about you and I[KittyX.like]celebrate, huh?"
    if "Historia" in Player.Traits:
        return 1
    $ approval_bonus = 10
    $ Player.AddWord(1,"interruption")
    call Kitty_SexMenu
    $ approval_bonus = 0
    return

label Kitty_BF_Jerk:
    $ KittyX.change_face("angry", 1)
    ch_k "Fine![KittyX.Like]. . .be that way!"
    $ KittyX.change_stat("obedience", 50, 40)
    if KittyX.Event[5] != 20:
        $ KittyX.change_stat("obedience", 200, (20* KittyX.Event[5]))
    if 20 > KittyX.Event[5] >= 3:
        $ KittyX.change_face("sad")
        ch_k "Yeah? Well. . .[KittyX.like]I don’t care what you want! We’re dating! Deal."
        ch_k "I. . .uhm. . .think I need to[KittyX.like]be alone for a little while."
        if "Historia" in Player.Traits:
            return 1
        $ KittyX.player_petnames.append("boyfriend")
        $ Achievements.append("I am not your Boyfriend!")
        $ bg_current = "bg_player"
        call Remove_Girl (KittyX)
        call set_the_scene
        $ renpy.pop_call()
        jump Player_Room
    if KittyX.Event[5] > 1:
        ch_k "It was such a mistake asking you again. You’re[KittyX.like]still such a jerk!"
    if KittyX.Event[5] != 20:
        $ KittyX.change_stat("love", 200, -(50* KittyX.Event[5]))
    else:
        $ KittyX.change_stat("love", 200, -50)
    ch_k "Get out, you big jerk!"
    if "Historia" in Player.Traits:
        return
    $ bg_current = "bg_player"
    call Remove_Girl (KittyX)
    $ renpy.pop_call()
    jump Player_Room




label Kitty_Love:


    call shift_focus (KittyX)
    $ KittyX.DrainWord("asked meet")
    if KittyX.Event[6]:

        "[KittyX.name] seems kind of shy and shuffles up to you, as if working up her nerve."
    elif bg_current != "bg_kitty":
        if KittyX.location == bg_current or KittyX in Party:
            "Suddenly, [KittyX.name] says she wants to talk to you in her room and drags you over there."
        else:
            "[KittyX.name] shows up, hurridly says she wants to talk to you in her room and drags you over there."
        $ bg_current = "bg_kitty"
    else:
        "[KittyX.name] suddenly stares at you very intently."

    $ KittyX.location = bg_current
    call set_the_scene (0)
    call Display_Girl (KittyX)
    call clear_the_room (KittyX)
    call Taboo_Level
    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("bemused", 1)
    $ KittyX.eyes = "side"
    $ Line = 0
    $ KittyX.Event[6] += 1
    if KittyX.Event[6] == 1:
        if KittyX in Player.Harem:
            ch_k "We've[KittyX.like]been together for a while now, and I've been thinking. . ."
        else:
            ch_k "We've[KittyX.like]know each other for a while now, and I've been thinking. . ."
        ch_k "It's been[KittyX.like]kinda hard for me to really get invested in anyone. . ."
        $ KittyX.eyes = "down"
        ch_k ". . . to[KittyX.like]be comfortable with who they are and be myself. . ."
        $ KittyX.eyes = "sly"
        ch_k "I just feel like sometimes you. . ."
        $ KittyX.eyes = "side"
        ch_k "and me[KittyX.like] . ."
        $ KittyX.change_face("perplexed", 2)
        $ KittyX.eyes = "surprised"
        ch_k "Never mind!"
        "Kitty dashes off and phases through the nearest wall."
        hide Kitty_Sprite with easeoutright
        call Remove_Girl (KittyX)
        return
    if KittyX.Event[6] == 2:
        ch_k "Sorry about before, I don't think I was ready maybe. . ."
        ch_k ". . . but I was kind of thinking-"
    elif KittyX.Event[6] >= 5:
        ch_k "Um. . ."
        $ KittyX.eyes = "sly"
        ch_k "You know, it's time to stop running. I think I love you."
        $ KittyX.eyes = "side"
        ch_k "You don't have to say it back, but I do."
        $ KittyX.player_petnames.append("lover")
        ch_k "Um, that's all."
    else:
        ch_k "Um. . ."
    if "lover" not in KittyX.player_petnames:
        menu:
            "She turns and makes a break for the nearest wall."
            "Catch her":
                $ KittyX.change_face("perplexed", 2)
                $ KittyX.eyes = "surprised"
                $ KittyX.change_stat("love", 95, 10)
                $ KittyX.change_stat("obedience", 95, 15)
                "As she spins, you grab on to her wrist. She's slightly startled to have been caught."
            "Let her go":
                "She dashes through the nearest wall and vanishes from view."
                jump Kitty_Love_End
        $ KittyX.blushing = 1
        menu:
            extend ""
            "Pull her close":
                $ KittyX.change_face("smile", 1)
                $ KittyX.change_stat("love", 95, 20)
                "You draw her into an embrace, arms wrapped tightly around her waist."
                $ Line = "hug"
            "Stay like this":
                $ KittyX.eyes = "down"
                $ KittyX.change_stat("obedience", 95, 10)
                "You keep hold of her wrist."
                $ Line = "wrist"
            "Let her go":
                if 1 < KittyX.Event[6] < 4:
                    "You immediately release her wrist."
                    $ KittyX.eyes = "down"
                    "She dashes through the nearest wall and vanishes from view."
                    jump Kitty_Love_End
                else:
                    $ KittyX.change_stat("love", 95, 10)
                    $ KittyX.change_stat("obedience", 95, 20)
                    $ KittyX.change_stat("inhibition", 80, 20)
                    "You release her wrist and she takes a step back."

        ch_k "I'm. . . I'm sorry, I just kind of panicked."
    if "lover" not in KittyX.player_petnames:

        ch_k "I thought maybe if I let myself get too close. . ."
        ch_k "I'd fall. . ."
        menu:
            extend ""
            "I'll never let go." if Line:
                $ KittyX.change_stat("love", 95, 20)
                $ KittyX.change_stat("inhibition", 80, 10)
                "She melts into your arms."
            "I'd always catch you.":
                $ KittyX.change_face("smile")
                $ KittyX.change_stat("love", 95, 20)
                $ KittyX.change_stat("obedience", 80, 15)
                "She smiles and shifts a bit uncomfortably."
            "Yeah, you should watch out for that.":
                $ KittyX.change_face("angry", 1)
                $ KittyX.recent_history.append("angry")
                $ KittyX.change_stat("love", 200, -20)
                $ KittyX.change_stat("obedience", 80, 10)
                $ KittyX.change_stat("inhibition", 80, 10)
                "She shoves you away and then stomps through the nearest wall."
                jump Kitty_Love_End
            "So get going. [[Give her a shove]":

                $ KittyX.change_face("surprised", 1)
                $ KittyX.change_stat("love", 200, -50)
                $ KittyX.change_stat("obedience", 80, 10)
                $ KittyX.change_stat("inhibition", 80, 10)
                "You shove her through the nearest wall and then continue on you way."
                $ KittyX.recent_history.append("angry")
                hide Kitty_Sprite with easeoutbottom
                jump Kitty_Love_End

    if "lover" in KittyX.player_petnames:

        menu:
            extend ""
            "I love you too.":
                $ KittyX.change_stat("love", 200, 40)
                $ KittyX.change_stat("inhibition", 200, 50)
                $ KittyX.change_face("smile")
            "You love me?":
                $ KittyX.change_face("confused", 2)
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        $ KittyX.change_stat("love", 200, 30)
                        $ KittyX.change_stat("inhibition", 200, 60)
                        $ KittyX.change_face("smile")
                    "I mean, a little?":
                        $ KittyX.change_stat("obedience", 80, 20)
                        $ KittyX.change_stat("inhibition", 80, -10)
                        ch_k "That's not a \"yes.\" . ."
                        $ Line = "awkward"
                    "Not really.":
                        $ KittyX.change_stat("love", 200, -30)
                        $ KittyX.change_stat("obedience", 80, 30)
                        $ KittyX.change_stat("inhibition", 80, -30)
                        $ KittyX.change_face("angry", 2)
                        ch_k "Huh?!"
                        $ Line = "awkward"
            "Huh.":
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("obedience", 80, 10)
                $ KittyX.change_stat("inhibition", 80, -20)
                menu:
                    ch_k "Huh?!"
                    "I mean, I love you too!":
                        $ KittyX.change_stat("love", 200, 30)
                        $ KittyX.change_stat("inhibition", 80, 10)
                        $ KittyX.change_face("smile")
                        ch_k "Way to pull out a last minute save there. . ."
                    "Well that's awkward.":
                        $ KittyX.change_stat("love", 200, -20)
                        $ KittyX.change_stat("obedience", 80, 30)
                        $ KittyX.change_stat("inhibition", 80, -20)
                        $ KittyX.change_face("angry", 2)
                        $ Line = "awkward"
            "Well that's awkward.":
                $ KittyX.change_stat("love", 200, -30)
                $ KittyX.change_stat("obedience", 80, 40)
                $ KittyX.change_stat("inhibition", 80, -20)
                $ KittyX.change_face("perplexed", 2)
                $ Line = "awkward"
    else:
        menu:
            extend ""
            "I love you, [KittyX.name].":
                $ KittyX.change_stat("love", 200, 50)
                $ KittyX.change_stat("inhibition", 80, 30)
                $ KittyX.change_face("smile")
                $ Line = "love"
            "I think you're pretty great.":
                $ KittyX.change_face("confused")
                menu:
                    ch_k "But you don't love me?"
                    "Yeah, of course I do!":
                        $ KittyX.change_stat("love", 200, 30)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 80, 20)
                        $ KittyX.change_face("smile")
                    "I mean, a little?":
                        if ApprovalCheck(KittyX, 1200, "OI"):
                            $ KittyX.change_face("sad")
                            $ KittyX.change_stat("love", 200, -30)
                            $ KittyX.change_stat("obedience", 90, 20)
                            $ KittyX.change_stat("inhibition", 80, 10)
                            ch_k "But[KittyX.like]not \"nothing\". . ."
                        else:
                            $ Line = "awkward"
                    "Not really.":
                        $ KittyX.change_face("sad")
                        if ApprovalCheck(KittyX, 1500, "OI"):
                            $ KittyX.change_stat("love", 200, -30)
                            $ KittyX.change_stat("obedience", 50, 30)
                            ch_k "Ouch. . ."
                        else:
                            $ Line = "awkward"
            "I was thinking something more casual. . .":
                $ KittyX.change_face("sad")
                if ApprovalCheck(KittyX, 1200, "OI") or ApprovalCheck(KittyX, 700, "I"):
                    $ KittyX.change_stat("love", 200, -30)
                    $ KittyX.change_stat("obedience", 90, 20)
                    $ KittyX.change_stat("inhibition", 90, 30)
                    ch_k "Close enough."
                else:
                    $ Line = "awkward"

    if Line == "awkward":
        if ApprovalCheck(KittyX, 700, "O"):
            ch_k "Fine, this doesn't have to be love."
        elif ApprovalCheck(KittyX, 700, "I"):
            ch_k "Fine, just sex it is."
        elif ApprovalCheck(KittyX, 1200, "OI"):
            ch_k "Fine, I can work with that."
        else:
            $ KittyX.change_stat("love", 200, -50)
            $ KittyX.change_stat("obedience", 95, 50)
            $ KittyX.change_stat("inhibition", 80, -50)
            ch_k "Oh, well I mean if you don't love me-"
            ch_k "You don't have to love me, that's ok."
            ch_k "I'll, um. . . never mind."
            if "Historia" not in Player.Traits:
                $ KittyX.recent_history.append("angry")
        $ KittyX.Event[6] = 20
    else:
        if Line:

            "She squeezes you even tighter and makes a little whimper."
        else:
            "She dives into your arms with a little squeek."
        if "lover" not in KittyX.player_petnames:
            ch_k "I love you too. . ."
            ch_k "I think I have for a while now."
            $ KittyX.player_petnames.append("lover")

label Kitty_Love_End:
    if Line == "awkward" or "lover" not in KittyX.player_petnames:
        hide Kitty_Sprite with easeoutright
        call Remove_Girl (KittyX)
        return
    ch_k "So I was thinking. . . did you want to . . ."
    if bg_current != "bg_player" and bg_current != "bg_kitty":
        ch_k "Wait, let's take this someplace more private. . ."
        $ bg_current = "bg_kitty"
        $ KittyX.location = bg_current
        call set_the_scene
        call clear_the_room (KittyX)
        call Taboo_Level
        ch_k "Ok, so like I was saying. . ."
    $ KittyX.change_stat("obedience", 70, 10)
    $ Player.AddWord(1,"interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            $ KittyX.change_stat("inhibition", 30, 30)
            ch_k "Hmm. . ."
            if "Historia" in Player.Traits:
                return 1
            call Kitty_SexAct ("sex")
        "I have something else in mind. . .[[choose another activity]":
            $ KittyX.brows = "confused"
            $ KittyX.change_stat("obedience", 70, 20)
            ch_k "Something like. . ."
            if "Historia" in Player.Traits:
                return 1
            $ approval_bonus = 20
            call Kitty_SexMenu
    return

label Kitty_Love_Redux:

    $ Line = 0
    $ KittyX.daily_history.append("relationship")
    if KittyX.Event[6] >= 25:

        ch_p "I hope you've forgiven me, I still love you."
        $ KittyX.change_stat("love", 95, 10)
        if ApprovalCheck(KittyX, 950, "L"):
            $ Line = "love"
        else:
            $ KittyX.change_face("sad")
            ch_k "You've dug too deep a hole, [KittyX.player_petname]."
            ch_k "Keep trying though."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ KittyX.change_face("perplexed",1)
        ch_k "Um, YEAH?!"
        menu:
            "I'm sorry, I didn't mean it.":
                $ KittyX.eyes = "surprised"
                ch_k "Well, if you. . . so wait, you {i}do{/i} love me?"
                ch_p "Yeah. I mean, yes, I love you, Kitty."
                $ KittyX.change_stat("love", 200, 10)
                if ApprovalCheck(KittyX, 950, "L"):
                    $ Line = "love"
                else:
                    $ KittyX.change_face("sadside")
                    ch_k "Well, I don't know how I feel at this point. . ."
            "I've changed my mind, so. . .":
                if ApprovalCheck(KittyX, 950, "L"):
                    $ Line = "love"
                    $ KittyX.eyes = "surprised"
                    ch_k "Really?!"
                else:
                    $ KittyX.mouth = "sad"
                    ch_k "Oh, you've changed your mind. Wonderful."
                    $ KittyX.change_stat("inhibition", 90, 10)
                    $ KittyX.change_face("sadside")
                    ch_k "Maybe I have too. . ."
            "Um, never mind.":
                $ KittyX.change_stat("love", 200, -30)
                $ KittyX.change_stat("obedience", 50, 10)
                $ KittyX.change_face("angry")
                ch_k "Seriously?"
                $ KittyX.recent_history.append("angry")
    if Line == "love":
        $ KittyX.change_stat("love", 200, 40)
        $ KittyX.change_stat("obedience", 90, 10)
        $ KittyX.change_stat("inhibition", 90, 10)
        $ KittyX.change_face("smile")
        ch_k "I[KittyX.like]love you too!"
        if KittyX.Event[6] < 25:
            $ KittyX.change_face("sly")
            "She slugs you in the arm"
            ch_k "Took you long enough."
        $ KittyX.player_petnames.append("lover")
    $ KittyX.Event[6] = 25
    return





label Kitty_Sub:
    call shift_focus (KittyX)
    $ KittyX.DrainWord("asked meet")
    if KittyX.location != bg_current and KittyX not in Party:
        "Suddenly, [KittyX.name] shows up and says she needs to talk to you."

    $ KittyX.location = bg_current
    call set_the_scene (0)
    call Display_Girl (KittyX)
    call clear_the_room (KittyX)
    call Taboo_Level
    $ KittyX.daily_history.append("relationship")
    $ KittyX.change_face("bemused", 1)

    $ Line = 0
    ch_k "So, uhm. . .you've really kinda[KittyX.like]taken control in our relationship lately."
    menu:
        extend ""
        "I guess. That's just kind of what comes naturally for me.":
            $ KittyX.change_stat("obedience", 200, 10)
            $ KittyX.change_stat("inhibition", 50, 5)
        "Sorry. I didn't mean to come off like that.":
            $ KittyX.change_face("startled", 2)
            $ KittyX.change_stat("love", 80, 5)
            $ KittyX.change_stat("obedience", 200, -5)
            $ KittyX.change_stat("inhibition", 50, -5)
            ch_k "No! Don't get the wrong idea! I just. . ."
        "Yup. Deal with it.":
            if ApprovalCheck(KittyX, 1000, "LO"):
                $ KittyX.change_stat("obedience", 200, 20)
                $ KittyX.change_stat("inhibition", 50, 10)
                ch_k "Um, yeah. . ."
            else:
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("obedience", 200, 10)
                $ KittyX.change_stat("inhibition", 50, 5)
                $ KittyX.change_face("angry")
                ch_k "I {i}was{/i} going to tell you I kinda liked it. But I didn't think you'd be[KittyX.like]a {i}jerk{/i} about it!"
                menu:
                    extend ""
                    "Guess you don't know me so well, huh?":
                        ch_k "I guess not."
                        $ Line = "rude"
                    "Sorry. I kind of thought you were getting into me being like that.":
                        $ KittyX.change_face("sexy", 2)
                        $ KittyX.eyes = "side"
                        $ KittyX.change_stat("love", 95, 5)
                        $ KittyX.change_stat("obedience", 200, 5)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        ch_k ". . ."

    $ KittyX.blushing = 1
    if not Line:

        ch_k "Well, I've, uhm. . . never had a guy be like that with me before. . ."
        $ KittyX.change_face("sly", 2)
        ch_k "I think I kinda like it."
        $ KittyX.change_face("smile", 1)
        menu:
            extend ""
            "Good. If you wanna be with me, that's how it'll be.":
                if ApprovalCheck(KittyX, 1000, "LO"):
                    $ KittyX.change_stat("obedience", 200, 15)
                    $ KittyX.change_stat("inhibition", 50, 10)
                    ch_k "I guess I walked into that one. . ."
                else:
                    $ KittyX.change_face("sadside", 1)
                    $ KittyX.change_stat("love", 200, -5)
                    $ KittyX.change_stat("obedience", 200, 10)
                    ch_k "You don't have to do it[KittyX.like]{i}all{/i} the time. You could still be nice once in a while."
                    menu:
                        extend ""
                        "Whatever. That's how it is. Take it or leave it.":
                            $ KittyX.change_face("angry")
                            $ KittyX.change_stat("love", 200, -10)
                            $ KittyX.change_stat("obedience", 200, 5)
                            ch_k "Y'know, you're such a jerk, [Player.name]!"
                            $ Line = "rude"
                        "I think I could maybe do that.":
                            $ KittyX.change_face("bemused", 2)
                            $ KittyX.eyes = "side"
                            $ KittyX.change_stat("love", 95, 5)
                            $ KittyX.change_stat("obedience", 200, 3)
                            $ KittyX.change_stat("inhibition", 50, 5)
                            ch_k "Uhm. . .yeah. It's[KittyX.like]. . kinda hot."
            "Yeah? You think it's sexy?":

                $ KittyX.change_face("bemused", 2)
                $ KittyX.eyes = "side"
                $ KittyX.change_stat("obedience", 200, 5)
                $ KittyX.change_stat("inhibition", 50, 10)
                ch_k "Uhm. . .yeah. It's[KittyX.like]. . kinda hot."
            "You sure you don't want me to back off a little?":

                $ KittyX.change_face("startled", 1)
                $ KittyX.change_stat("obedience", 200, -5)
                menu:
                    ch_k "Only if you think it might be[KittyX.like]weird. But I think it's kinda hot."
                    "Only if you're okay with it.":
                        $ KittyX.change_face("bemused", 2)
                        $ KittyX.change_stat("love", 95, 10)
                        $ KittyX.change_stat("inhibition", 50, 10)
                        $ Line = 0
                    "Uhm. . .yeah. I {i}do{/i} think it's weird. Sorry.":
                        $ KittyX.change_stat("love", 200, -15)
                        $ KittyX.change_stat("obedience", 200, -5)
                        $ KittyX.change_stat("inhibition", 50, -10)
                        $ Line = "embarrassed"
            "I don't really care what you like. I do what I want.":

                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("obedience", 200, 15)
                $ KittyX.change_face("angry")
                ch_k "Y'know, you're such a jerk, [Player.name]!"
                $ Line = "rude"

    if not Line:
        $ KittyX.change_face("bemused", 1)
        $ KittyX.eyes = "down"
        ch_k "Cool. So. . .just so you know. . .I don't mind[KittyX.like]you being in control."
        if "256 Shades of Grey" in KittyX.Inventory:
            ch_k "Like in that '256 Shades of Grey' book."
        menu Kitty_Sub_Choice:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                $ KittyX.change_stat("love", 200, -5)
                $ KittyX.change_stat("inhibition", 50, -15)
                $ Line = "embarrassed"
            "I think I could get used to that kinda thing.":
                $ KittyX.change_stat("obedience", 200, 5)
                $ KittyX.change_stat("inhibition", 50, 5)
                $ KittyX.change_face("smile", 1)
                $ Line = 0
            "You actually {i}read{/i} that?" if "256 Shades of Grey" in KittyX.Inventory and Line != "grey":
                $ KittyX.change_stat("love", 95, 5)
                $ KittyX.change_face("sly", 1)
                ch_k "You think I wouldn't read something you bought me? I think you {i}maybe{/i} don't realize how much I like you."
                $ KittyX.change_stat("inhibition", 50, 5)
                ch_k "Well, I {i}did{/i} read it. And. . .it turns out it kinda[KittyX.like]. . {i}really{/i} turned me on."
                ch_k "So. . .what d'you think? Think[KittyX.like]maybe you'd like that?"
                $ Line = "grey"
                jump Kitty_Sub_Choice

    if not Line:
        $ KittyX.change_face("smile", 1)
        ch_k "Awesome. So. . .if you wanted me to, I could[KittyX.like]call you {i}sir{/i} or something."
        $ KittyX.change_face("sly", 2)
        ch_k "Think you'd like that?"
        $ KittyX.blushing = 1
        menu:
            extend ""
            "That has a nice ring to it.":
                $ KittyX.change_stat("love", 95, 5)
                $ KittyX.change_stat("obedience", 200, 15)
                $ KittyX.change_stat("inhibition", 50, 5)
                ch_k "Okay, then. . .{i}sir{/i}."
                $ KittyX.player_petname = "sir"
            "I think I'd rather stick with what we've got going.":
                $ KittyX.change_face("startled", 2)
                ch_k "Oh!"
                $ KittyX.change_stat("inhibition", 50, -5)
                $ KittyX.change_face("sadside", 1)
                menu:
                    ch_k ". . . Well. . . maybe you can still kinda[KittyX.like]be in control, anyway?"
                    "I like that idea.":
                        $ KittyX.change_stat("obedience", 200, 10)
                        $ KittyX.change_face("smile", 1)
                        ch_k "You're so awesome, [KittyX.player_petname]."
                    "This is getting really weird.":
                        $ KittyX.change_stat("love", 200, -10)
                        $ KittyX.change_stat("obedience", 200, -50)
                        $ KittyX.change_stat("inhibition", 50, -15)
                        $ Line = "embarrassed"


    $ KittyX.history.append("sir")
    if not Line:
        $ KittyX.blushing = 1
        $ KittyX.player_petnames.append("sir")

    elif Line == "rude":
        hide Kitty_Sprite with easeoutbottom
        call Remove_Girl (KittyX)
        if "Historia" not in Player.Traits:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor in a huff, leaving you alone."
    elif Line == "embarrassed":
        $ KittyX.change_face("sadside", 2)
        ch_k "Oh! Uhm, yeah! [KittyX.Like]I mean. . ."
        $ KittyX.mouth = "smile"
        ch_k "I was just kidding. I[KittyX.like]. . yeah. That's kinda weird."
        ch_k "I should go. I think I hear Professor Xavier calling me."
        $ KittyX.blushing = 1
        hide Kitty_Sprite with easeoutbottom
        call Remove_Girl (KittyX)
        if "Historia" not in Player.Traits:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor, leaving you alone. It didn't look like she could get away fast enough."
    return

label Kitty_Sub_Asked:
    $ Line = 0
    $ KittyX.change_face("sadside", 1)
    ch_k "Yeah. And I also[KittyX.like]remember what a {i}jerk{/i} you were to me about it."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in KittyX.player_petnames and ApprovalCheck(KittyX, 850, "O"):

                pass
            elif ApprovalCheck(KittyX, 550, "O"):

                pass
            else:
                ch_k "Well maybe {i}I'm{/i}[KittyX.like]over that. . ."
                $ Line = "rude"

            if Line != "rude":
                $ KittyX.change_stat("love", 90, 10)
                $ KittyX.change_face("sly", 1)
                ch_k "Well. . .okay. I {i}did{/i} think that was pretty hot. Also, you're super-cute when you apologize."
                call Kitty_Kissing_Smooch
                ch_k "Okay. We can[KittyX.like]try again."
        "Listen. . . I know it's what you want. Do you want to try again, or not?":

            $ KittyX.change_face("bemused", 1)
            if "sir" in KittyX.player_petnames:
                if ApprovalCheck(KittyX, 850, "O"):
                    ch_k "Ok, fine."
                else:
                    ch_k "Um, not really."
                    $ Line = "rude"
            elif ApprovalCheck(KittyX, 600, "O"):

                $ KittyX.change_face("sadside", 1)
                ch_k "You're[KittyX.like]totally impossible."
                $ KittyX.eyes = "squint"
                ch_k "Maybe you're right."
                ch_k "But I still think you should[KittyX.like] apologize for being a jerk to me."
                menu:
                    extend ""
                    "Okay, I'm sorry I was mean about it.":
                        $ KittyX.change_stat("love", 90, 15)
                        $ KittyX.change_stat("inhibition", 50, 10)
                        $ KittyX.change_face("bemused", 1)
                        $ KittyX.eyes = "side"
                        ch_k "That's all you had to say."
                    "Not gonna happen.":
                        if "sir" in KittyX.player_petnames and ApprovalCheck(KittyX, 900, "O"):
                            $ KittyX.change_stat("love", 200, -5)
                            $ KittyX.change_stat("obedience", 200, 10)
                            ch_k ". . ."
                        elif ApprovalCheck(KittyX,650, "O"):
                            $ KittyX.change_stat("love", 200, -5)
                            $ KittyX.change_stat("obedience", 200, 10)
                            ch_k "I, um. . ."
                        else:
                            $ KittyX.change_stat("love", 200, -10)
                            $ KittyX.change_stat("obedience", 90, -10)
                            $ KittyX.change_stat("obedience", 200, -10)
                            $ KittyX.change_stat("inhibition", 50, -15)
                            "Kitty sighs and rolls her eyes."
                            $ KittyX.change_face("angry", 1)
                            $ KittyX.eyes = "side"
                            ch_k "You really don't learn, do you?"
                            $ Line = "rude"
                    "Ok, never mind then.":
                        $ KittyX.change_face("angry", 1)
                        $ KittyX.change_stat("love", 200, -10)
                        $ KittyX.change_stat("obedience", 90, -10)
                        $ KittyX.change_stat("obedience", 200, -10)
                        $ KittyX.change_stat("inhibition", 50, -15)
                        ch_k "Y'know, if you're gonna throw that in my face, forget it."
                        ch_k "I should've[KittyX.like]expected you'd be like that."
                        $ Line = "rude"

    $ KittyX.recent_history.append("asked sub")
    $ KittyX.daily_history.append("asked sub")
    if Line == "rude":

        hide Kitty_Sprite with easeoutbottom
        call Remove_Girl (KittyX)
        $ KittyX.recent_history.append("angry")
        if "Historia" not in Player.Traits:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor, leaving you alone. She looked pretty upset."
    elif "sir" in KittyX.player_petnames:

        $ KittyX.change_stat("obedience", 200, 50)
        $ KittyX.player_petnames.append("master")
        $ KittyX.player_petname = "master"
        $ KittyX.eyes = "sly"
        ch_k ". . . master. . ."
    else:

        $ KittyX.change_stat("obedience", 200, 30)
        $ KittyX.player_petnames.append("sir")
        $ KittyX.player_petname = "sir"
        $ KittyX.eyes = "sly"
        ch_k ". . . sir."
    return






label Kitty_Master:
    call shift_focus (KittyX)
    $ KittyX.DrainWord("asked meet")
    if KittyX.location != bg_current and KittyX not in Party:
        "Suddenly, [KittyX.name] shows up and says she needs to talk to you."

    $ KittyX.location = bg_current
    call set_the_scene (0)
    call Display_Girl (KittyX)
    call clear_the_room (KittyX)
    $ KittyX.daily_history.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ KittyX.change_face("bemused", 1)
    ch_k "[KittyX.player_petname], if you don't mind me saying so. . ."
    ch_k "I think having you be[KittyX.like]in control of our relationship is working out pretty awesome."
    menu:
        extend ""
        "I like it too.":
            $ KittyX.change_face("sly", 1)
            ch_k "Cool. Maybe we could[KittyX.like]kick it up a notch?"
            menu:
                extend ""
                "Nah. This is just about perfect.":
                    $ KittyX.change_face("sad", 1)
                    $ KittyX.change_stat("obedience", 200, -15)
                    $ KittyX.change_stat("inhibition", 50, 10)
                    ch_k "Oh. Well, okay, I guess."
                    $ Line = "fail"
                "What'd you have in mind?":
                    $ KittyX.eyes = "side"
                    ch_k "I dunno. I was thinking[KittyX.like]maybe I could start calling you. . . {i}master{/i}?"
                    $ KittyX.eyes = "squint"
                    ch_k "Would you like that? I think that'd be kinda[KittyX.like]hot."
                    menu:
                        extend ""
                        "Oh, yeah. I'd like that.":
                            ch_k "Cool. . ."
                        "Uhm. . .nah. That's too much.":
                            $ KittyX.change_face("sad", 1)
                            $ KittyX.change_stat("obedience", 200, -15)
                            $ KittyX.change_stat("inhibition", 50, 5)
                            ch_k "Oh. Well, okay, I guess."
                            $ Line = "fail"
                "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":

                    $ KittyX.change_face("sly", 1)
                    $ KittyX.change_stat("love", 200, 15)
                    $ KittyX.change_stat("obedience", 200, -10)
                    $ KittyX.change_stat("inhibition", 50, 10)
                    ch_k "Aw, I guess I can't get mad about that. . ."
                    $ Line = "fail"
                "Actually, let's stop that. It's creeping me out.":

                    $ KittyX.change_face("perplexed", 2)
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.change_stat("obedience", 200, -50)
                    $ KittyX.change_stat("inhibition", 50, -15)
                    ch_k "Oh. Sorry. I guess I got[KittyX.like]carried away with it."
                    $ KittyX.blushing = 1
                    $ Line = "embarrassed"
        "As if I care what you think, slut.":

            $ KittyX.change_face("sad", 1)
            $ KittyX.change_stat("love", 200, -20)
            $ KittyX.change_stat("obedience", 200, 10)
            $ KittyX.change_stat("inhibition", 50, -10)
            menu:
                ch_k "Excuse me?"
                "Sorry. I just don't care what you want.":
                    if ApprovalCheck(KittyX, 1400, "LO"):
                        $ KittyX.change_stat("obedience", 200, 10)
                        ch_k "That's so. . ."
                        $ KittyX.change_face("sly", 1)
                        $ KittyX.change_stat("love", 200, 20)
                        $ KittyX.change_stat("inhibition", 50, 15)
                        ch_k ". . .{i}mean!{/i}"
                    else:
                        $ KittyX.change_stat("love", 200, -15)
                        $ KittyX.change_stat("obedience", 200, -10)
                        $ KittyX.change_stat("inhibition", 50, 5)
                        $ KittyX.change_face("angry", 1)
                        ch_k "!!!"
                        $ Line = "rude"
                "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                    $ KittyX.change_stat("love", 200, 10)
                    $ KittyX.change_stat("obedience", 200, 10)
                    $ KittyX.change_stat("inhibition", 50, 5)
                    ch_k "Oh, okay. Just. . .try not to be so[KittyX.like]mean about it, 'kay?"
        "Not me. It's kind of creepy.":

            $ KittyX.change_face("sad", 2)
            $ KittyX.change_stat("love", 200, -10)
            $ KittyX.change_stat("obedience", 200, -20)
            $ KittyX.change_stat("inhibition", 50, -25)
            ch_k "Oh. Uhm. . .never mind, then."
            $ Line = "embarrassed"

    $ KittyX.history.append("master")
    if Line == "rude":
        $ KittyX.recent_history.append("angry")
        hide Kitty_Sprite with easeoutbottom
        call Remove_Girl (KittyX)
        if "Historia" not in Player.Traits:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor in a huff. She might have been crying."
    elif Line == "embarrassed":
        hide Kitty_Sprite with easeoutbottom
        call Remove_Girl (KittyX)
        if "Historia" not in Player.Traits:
            $ renpy.pop_call()
        "[KittyX.name] phases through the floor, leaving you alone. She looked really embarrassed."
    elif Line != "fail":
        $ KittyX.change_stat("obedience", 200, 50)
        $ KittyX.player_petnames.append("master")
        $ KittyX.player_petname = "master"
        ch_k ". . .master."
    return






label Kitty_Sexfriend:
    $ KittyX.location = bg_current
    call set_the_scene (0)
    call Display_Girl (KittyX)
    call clear_the_room (KittyX)
    $ KittyX.daily_history.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ KittyX.change_face("bemused", 1)
    ch_k "So, [KittyX.player_petname]. . .you[KittyX.like]got a second?"
    menu:
        extend ""
        "Not really.":
            $ KittyX.change_face("angry", 1)
            ch_k "You're such a jerk, [Player.name]!"
            $ KittyX.change_stat("love", 200, -20)
            $ KittyX.change_stat("obedience", 50, 3)
            $ Line = "rude"
        "This doesn't sound good.":

            $ KittyX.change_face("perplexed", 1)
            ch_k "I promise. It's nothing[KittyX.like]bad."
        "Yeah. What's up?":

            pass

    if not Line:
        if ApprovalCheck(KittyX, 850, "L"):
            $ KittyX.change_face("bemused", 1)
            ch_k "Well. . . I really like you. You know that, right?"
            menu:
                extend ""
                "I was kinda hoping.":
                    $ KittyX.change_face("sexy", 1)
                    $ KittyX.change_stat("love", 90, 10)
                    $ KittyX.change_stat("inhibition", 80, 5)
                    ch_k "I was {i}really{/i} hoping you'd say that [KittyX.player_petname]."
                "Really?":

                    ch_k "Uhm. . . [KittyX.like]yeah. I really do."
                "Ugh. Gross":

                    $ KittyX.change_face("angry", 1)
                    $ KittyX.change_stat("love", 200, -10)
                    $ KittyX.change_stat("obedience", 50, 5)
                    $ KittyX.change_stat("inhibition", 80, -5)
                    ch_k "Y'know, you're such an ass, [Player.name]!"
                    $ Line = "rude"

        elif ApprovalCheck(KittyX, 1000, "LI"):
            $ KittyX.change_face("sexy", 1)
            ch_k "I just wanted to tell you. . .I think you're[KittyX.like]kinda cute."
            menu:
                extend ""
                "That's really nice of you to say.":
                    $ KittyX.change_stat("love", 80, 5)
                    $ KittyX.change_stat("inhibition", 80, 5)
                    ch_k "Well, I really mean it."
                "Me? You really think so?":

                    ch_k "Yeah. I {i}really{/i} do."
                "Are you going somewhere with this?":

                    $ KittyX.change_face("angry")
                    ch_k "Well not anymore, I'm not!"
                    $ Line = "rude"
        else:

            $ KittyX.mouth = "smile"
            $ KittyX.brows = "sad"
            $ KittyX.eyes = "side"
            ch_k "This is gonna sound[KittyX.like]really weird."
            menu:
                extend ""
                "Well, you've got me intrigued. Now you {i}have{/i} to tell me.":
                    ch_k "Promise you won't think[KittyX.like]{i}badly{/i}of me?"
                    menu:
                        extend ""
                        "[KittyX.name]. . . I really like you. I promise.":
                            $ KittyX.change_face("smile")
                            $ KittyX.change_stat("love", 80, 10)
                            $ KittyX.change_stat("inhibition", 80, 5)
                            ch_k "Well. . . okay."
                        "Uhm. . . okay?":

                            ch_k "Well. . ."
                        "No promises.":

                            $ KittyX.change_face("perplexed",2)
                            $ KittyX.change_stat("inhibition", 80, -5)
                            ch_k "Uhm. . . never mind, then."
                            $ Line = "embarrassed"
                "Uhm, I think I've had my fill of {i}weird{/i}, thanks":

                    $ KittyX.change_face("angry",1)
                    ch_k "Fine. [KittyX.like]whatever."
                    $ Line = "rude"
    if KittyX in Player.Harem:
        $ Line = "harem"
    if not Line:
        ch_k "Anyway. . . I was[KittyX.like]kinda thinking. . . we get along pretty well, right?"
        menu:
            extend ""
            "Right. . . ":
                pass
            "Okay. Just stop. You're creeping me out.":
                $ KittyX.change_face("perplexed",2)
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("inhibition", 80, -10)
                ch_k "Sorry. I knew this was a mistake."
                $ Line = "embarrassed"

    if not Line:
        ch_k "And we've[KittyX.like]known each other for a little while, right?"
        menu:
            extend ""
            "Right. . . ":
                pass
            "Okay. Just stop. You're creeping me out.":
                $ KittyX.change_face("perplexed",2)
                $ KittyX.change_stat("love", 200, -10)
                $ KittyX.change_stat("inhibition", 80, -10)
                ch_k "Sorry. I knew this was a mistake."
                $ Line = "embarrassed"
    if not Line:
        ch_k "Well. . . I was just kinda thinking. . . "
        ch_k "[KittyX.like]we could take our relationship a little further, if you wanted to."
        menu:
            extend ""
            "You mean. . . like, being {i}friends with benefits{/i}?":
                ch_k "Kinda, yeah. Whaddya think?"
                menu:
                    extend ""
                    "Sounds amazing! Count me in.":
                        $ KittyX.change_face("smile",1)
                        $ KittyX.change_stat("love", 80, 10)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 200, 50)
                        $ KittyX.change_stat("lust", 200, 5)
                        "Kitty leans in and gives you a gentle kiss on the cheek."
                        ch_k "I can't wait to get started, [KittyX.player_petname]."
                    "That may be the sluttiest thing I've ever heard in my life.":

                        $ KittyX.change_face("angry",1)
                        $ KittyX.change_stat("love", 200, -30)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 80, -40)
                        ch_k "You're the biggest asshole[KittyX.like]ever, [KittyX.player_petname]!"
                        $ Line = "rude"
            "Uhm, to be honest, I'd rather not.":

                $ KittyX.change_face("sadside",2)
                $ KittyX.change_stat("obedience", 50, 15)
                $ KittyX.change_stat("inhibition", 80, -15)
                ch_k "Oh. Okay."
                ch_k "I[KittyX.like]think I should go now. I've got[KittyX.like]stuff to do."
                $ Line = "sad"
    if Line == "harem":
        ch_k "I am -totally- addicted to this dick. . ."
        $ Line = 0
    if Line == "rude":
        $ KittyX.change_face("angry",1)
        $ KittyX.recent_history.append("angry")
        $ KittyX.change_stat("love", 200, -20)
        $ KittyX.change_stat("obedience", 50, 5)
        $ KittyX.change_stat("inhibition", 80, -10)
        hide Kitty_Sprite with easeoutleft
        $ KittyX.recent_history.append("angry")
        "[KittyX.name] storms off in a huff. She seemed pretty mad at you."
    elif Line == "embarrassed":
        $ KittyX.change_face("perplexed",1)
        $ KittyX.change_stat("love", 200, -10)
        $ KittyX.change_stat("obedience", 50, 5)
        $ KittyX.change_stat("inhibition", 80, -20)
        hide Kitty_Sprite with easeoutbottom
        "[KittyX.name] phases through the floor leaving you alone. That was very strange."
    elif Line == "sad":
        hide Kitty_Sprite with easeoutbottom
        "[KittyX.name] phases through the floor leaving you alone. You think you may have hurt her feelings."
    else:
        $ KittyX.player_petnames.append("sex friend")
        $ KittyX.change_face("sly",2)
        $ KittyX.change_stat("inhibition", 80, 10)
        $ KittyX.change_stat("lust", 80, 10)
        "[KittyX.name] leans in and passes her hand across your body."
        "As she does so, she phases her hand through your jeans, so her fingers slide along your bare skin."
        $ KittyX.blushing = 1
        ch_k "I'll definitely be seeing {i}you{/i} later, [KittyX.player_petname]."
        hide Kitty_Sprite with easeoutright
        "She passes through a nearby wall. "
    call Remove_Girl (KittyX)
    return








label Kitty_Fuckbuddy:
    $ KittyX.daily_history.append("relationship")
    $ KittyX.DrainWord("asked meet")
    "Out of nowhere, you feel a hand stroking across your cock."
    "Even though you're fully dressed, it definitely feels like soft skin touching your own."
    "You glance down and see a slender arm snaked around your waist, before vanishing into your pants."
    "As you try to control your rising erection, a voice whispers into your ear,"
    ch_k "Any time, just let me know. . ."
    "-and suddenly the pressure is gone."
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on [KittyX.name] later. . ."
    $ KittyX.player_petnames.append("fuck buddy")
    $ KittyX.Event[10] += 1
    return






label Kitty_Daddy:
    $ KittyX.daily_history.append("relationship")
    $ KittyX.DrainWord("asked meet")
    call shift_focus (KittyX)
    call set_the_scene
    ch_k ". . ."
    if KittyX in Player.Harem:
        ch_k "Hey, so[KittyX.like]we've been dating,"
    else:
        ch_k "Hey, so[KittyX.like]we've been hanging out,"
    if KittyX.love > KittyX.obedience and KittyX.love > KittyX.inhibition:
        ch_k "and you're so sweet. . ."
    elif KittyX.obedience > KittyX.inhibition:
        ch_k "and you give me what I need. . ."
    else:
        ch_k "and I've been trying out new things. . ."
    ch_k "So[KittyX.like]I was thinking, could I call you. . . \"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ KittyX.change_face("smile")
            $ KittyX.change_stat("love", 90, 25)
            $ KittyX.change_stat("obedience", 60, 10)
            $ KittyX.change_stat("inhibition", 80, 30)
            ch_k "Great!"
        "What do you mean by that?":
            $ KittyX.change_face("bemused")
            ch_k "I don't know, it'd kinda be hot, being your baby girl. . ."
            ch_k "Could'ya call me that?"
            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ KittyX.change_face("smile")
                    $ KittyX.change_stat("love", 90, 17)
                    $ KittyX.change_stat("obedience", 60, 20)
                    $ KittyX.change_stat("inhibition", 80, 25)
                    ch_k "Nice! . . daddy."
                    $ KittyX.player_petname = "daddy"
                "Could you not, please?":
                    $ KittyX.change_stat("obedience", 80, 40)
                    $ KittyX.change_stat("inhibition", 80, 20)
                    $ KittyX.change_face("sad")
                    ch_k " . . . "
                    ch_k "Huh. K."
                "No, that creeps me out.":
                    $ KittyX.change_stat("love", 90, -15)
                    $ KittyX.change_stat("obedience", 80, 45)
                    $ KittyX.change_stat("inhibition", 70, 5)
                    $ KittyX.change_face("angry")
                    ch_k "Booo."
        "No, that creeps me out.":
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("obedience", 80, 40)
            $ KittyX.change_stat("inhibition", 70, 10)
            $ KittyX.change_face("angry")
            ch_k "Hrmph."
    $ KittyX.player_petnames.append("daddy")
    return



























































































































































































































































































































































label Kitty_Yoink(Girl=0, TempBonus=0, Shy=0):






    if "yoink" in KittyX.daily_history:
        ch_k "We've had enough fun with that."
        return

    if RogueX.location == bg_current:
        $ Girl = RogueX
    elif EmmaX.location == bg_current:
        $ Girl = EmmaX
    elif LauraX.location == bg_current:
        $ Girl = LauraX
    elif JeanX.location == bg_current:
        $ Girl = JeanX
    elif StormX.location == bg_current:
        $ Girl = StormX
    elif JubesX.location == bg_current:
        $ Girl = JubesX

    if (EmmaX.location == "bg_teacher" or StormX.location == "bg_teacher") and bg_current == "bg_classroom":

        menu:
            "About who?"
            "[Girl.name]?" if Girl:
                pass
            "[EmmaX.name]" if EmmaX.location == "bg_teacher":
                $ Girl = EmmaX
            "[StormX.name]" if StormX.location == "bg_teacher":
                $ Girl = StormX
            "Never mind":
                return
    elif not Girl:
        "I don't know who you think you could yoink from."
        return


    if KittyX.GirlLikeCheck(Girl) <= 200:
        $ TempBonus = 400
    elif KittyX.GirlLikeCheck(Girl) <= 400:
        $ TempBonus = 200
    elif KittyX.GirlLikeCheck(Girl) >= 800 or ApprovalCheck(Girl, 500, "I", TabM=3):

        $ TempBonus = 0
    else:

        $ TempBonus = -400

    menu:
        "Hey [KittyX.name], why don't you snag [Girl.name]'s. . ."
        ". . . [Girl.top]?" if Girl.top:
            if Girl.bra:

                $ Shy = 2
                if ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):


                    $ Line = "over"
                elif ApprovalCheck(KittyX, 600, TabM=2, Bonus=TempBonus):

                    $ Line = "no"
                else:

                    $ Line = "noway"
            else:

                $ Shy = 3
                if ApprovalCheck(KittyX, 800, TabM=2.5, Bonus=(TempBonus*1.5)):
                    $ Line = "over"
                elif ApprovalCheck(KittyX, 600, TabM=1.5, Bonus=TempBonus):
                    $ Line = "no"
                else:
                    $ Line = "noway"

        ". . . [Girl.bra]?" if Girl.bra:
            if Girl.top:

                $ Shy = 1
                if ApprovalCheck(KittyX, 1200, TabM=1, Bonus=TempBonus):


                    $ Line = "chest"
                elif ApprovalCheck(KittyX, 600, TabM=0.5, Bonus=TempBonus):

                    $ Line = "no"
                else:

                    $ Line = "noway"
            else:

                $ Shy = 3
                if ApprovalCheck(KittyX, 800, TabM=2.5, Bonus=(TempBonus*1.5)):
                    $ Line = "chest"
                elif ApprovalCheck(KittyX, 600, TabM=1.5, Bonus=TempBonus):
                    $ Line = "no"
                else:
                    $ Line = "noway"

        ". . . [Girl.legs]?" if Girl.legs:
            if Girl.underwear or Girl.HoseNum() >= 10:

                $ Shy = 2
                if ApprovalCheck(KittyX, 1000, TabM=2, Bonus=TempBonus):


                    $ Line = "legs"
                elif ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):

                    $ Line = "no"
                else:

                    $ Line = "noway"
            else:

                $ Shy = 3
                if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                    $ Line = "legs"
                elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                    $ Line = "no"
                else:
                    $ Line = "noway"

        ". . . [Girl.underwear]?" if Girl.underwear:
            if Girl.legs or Girl.HoseNum() >= 10:

                $ Shy = 1
                if ApprovalCheck(KittyX, 1000, TabM=1, Bonus=TempBonus):


                    $ Line = "panties"
                elif ApprovalCheck(KittyX, 800, TabM=0.5, Bonus=TempBonus):

                    $ Line = "no"
                else:

                    $ Line = "noway"
            else:

                $ Shy = 3
                if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                    $ Line = "panties"
                elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                    $ Line = "no"
                else:
                    $ Line = "noway"

        ". . . [Girl.hose]?" if Girl.hose:
            if Girl.legs:

                $ Shy = 1
                if ApprovalCheck(KittyX, 800, TabM=1, Bonus=TempBonus):


                    $ Line = "hose"
                elif ApprovalCheck(KittyX, 800, TabM=0.5, Bonus=TempBonus):

                    $ Line = "no"
                else:

                    $ Line = "noway"
            elif Girl.underwear or Girl.HoseNum() < 10:

                $ Shy = 2
                if ApprovalCheck(KittyX, 1000, TabM=2, Bonus=TempBonus):


                    $ Line = "hose"
                elif ApprovalCheck(KittyX, 800, TabM=2, Bonus=TempBonus):

                    $ Line = "no"
                else:

                    $ Line = "noway"
            else:

                $ Shy = 3
                if ApprovalCheck(KittyX, 1000, TabM=2.5, Bonus=(TempBonus*1.5)):
                    $ Line = "hose"
                elif ApprovalCheck(KittyX, 800, TabM=1.5, Bonus=TempBonus):
                    $ Line = "no"
                else:
                    $ Line = "noway"
        "Never mind.":

            return

    if Line == "no":
        $ KittyX.change_face("sadside",1)
        $ KittyX.change_stat("love", 90, -(Shy))
        ch_k "I really couldn't do that to her."
        return
    if Line == "noway":
        $ KittyX.change_face("angry",1)
        $ KittyX.change_stat("love", 90, -(2*Shy))
        $ KittyX.change_stat("obedience", 60, -(Shy))
        ch_k "How could you[KittyX.like]even {i}consider{/i} something like that?"
        return


    $ KittyX.change_stat("obedience", 70, Shy)
    $ KittyX.change_stat("inhibition", 80, Shy)
    "[KittyX.name] sneaks up behind [Girl.name]. . ."

    $ Girl.change_face("surprised",2)
    if Line == "over":
        $ Line = Girl.top
        $ Girl.top = 0
        call expression Girl.Tag + "_First_Topless" pass (1)
        "She reaches out and snags [Girl.name]'s [Line], tugging it through her body."

    elif Line == "chest":
        $ Line = Girl.bra
        $ Girl.bra = 0
        call expression Girl.Tag + "_First_Topless" pass (1)
        if Girl.top:
            "She reaches through [Girl.name]'s [Girl.top] and snags her [Line]."
        else:
            "She reaches out and snags [Girl.name]'s [Line], tugging it free."

    elif Line == "legs":
        $ Line = Girl.legs
        $ Girl.legs = 0
        call expression Girl.Tag + "_First_Bottomless" pass (1)
        "She reaches down and snags [Girl.name]'s [Line], tugging them through her body."

    elif Line == "panties":
        $ Line = Girl.underwear
        $ Girl.underwear = 0
        call expression Girl.Tag + "_First_Bottomless" pass (1)
        if Girl.legs:
            "She reaches down through [Girl.name]'s [Girl.legs] and snags her [Line]."
        elif Girl.hose:
            "She reaches down through [Girl.name]'s [Girl.hose] and snags her [Line]."
        else:
            "She reaches out and snags [Girl.name]'s [Line], tugging them free."
    elif Line == "hose":
        $ Line = Girl.hose
        $ Girl.hose = 0
        call expression Girl.Tag + "_First_Bottomless" pass (1)
        if Girl.legs:
            "She reaches down through [Girl.name]'s [Girl.legs] and snags her [Line]."
        else:
            "She reaches out and snags [Girl.name]'s [Line], tugging them free."

    "She then dashes back a few steps, slipping the [Line] behind her back."

    call Activity_Check (Girl, KittyX, 1, 0, 2)
    $ Approval = _return

    $ KittyX.daily_history.append("yoink")
    if "yoink" not in KittyX.history:
        $ KittyX.history.append("yoink")

    if "exhibitionist" in Girl.Traits:
        $ Approval = 2
    $ Girl.daily_history.append("yoink")

    if Shy <= 1:

        if Approval >= 2:

            $ Girl.change_face("sly")
            $ Girl.change_stat("inhibition", 80, Shy)
            $ Girl.change_stat("lust", 80, 2)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
        elif Approval:

            $ Girl.change_face("angry",1)
            $ Girl.change_stat("love", 90, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
        else:
            $ Girl.change_face("angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She storms away in disgust."

    elif Shy <= 2:

        if Approval >= 2:

            $ Girl.change_face("sly")
            $ Girl.change_stat("inhibition", 80, Shy)
            $ Girl.change_stat("lust", 80, Shy)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
            "She then just leans back, unconcerned."
        elif Approval or Girl == JeanX:

            $ Girl.change_face("angry",1)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            $ Girl.change_stat("lust", 80, Shy)
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            if Girl != JeanX:
                $ Girl.change_face("sadside",2)
                "She settles back down with a little embarassment."
        else:
            $ Girl.change_face("angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She dashes away in embarassment."
    else:

        if Approval >= 2:

            $ Girl.change_face("sly")
            $ Girl.change_stat("love", 90, 1)
            $ Girl.change_stat("inhibition", 80, Shy)
            $ Girl.change_stat("lust", 80, 2*Shy)
            "[Girl.name] glances back in surprise, but then breaks into a quick smile."
            "She looks around, daring anyone to comment."
        elif Approval or Girl == JeanX:

            $ Girl.change_face("angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            if Girl != JeanX:
                "She seems really mortified, but stands her ground."
        else:
            $ Girl.change_face("angry",2)
            $ Girl.change_stat("love", 90, -(Shy))
            $ Girl.change_stat("inhibition", 80, -(Shy))
            "[Girl.name] glances back in surprise, and then glances over at you with a glare."
            "She dashes away in embarassment."



    if Approval:
        $ Girl.GLG(KittyX,900,(2*Shy),1)
        $ KittyX.GLG(Girl,900,(2*Shy),1)
        $ Girl.AddWord(1,"yoinked")
    else:
        call Remove_Girl (Girl)
        $ Girl.GLG(KittyX,900,-(2*Shy),1)

    if Girl == JeanX and Approval < 2:
        "With a quick nod, her clothes come flying back to her."
        $ Girl.DrainWord("yoinked")
        $ Girl.change_outfit()
        "[KittyX.name]'s left a little dazed."
    elif TempBonus > 0:
        if Approval < 2:

            $ KittyX.change_face("sly")
            $ KittyX.change_stat("love", 80, 1)
            "[KittyX.name] smiles triumphantly."
        else:

            $ KittyX.change_face("angry",Eyes="side")
            "[KittyX.name] seems a bit annoyed at [Girl.name]'s attitude."

    elif not Approval:

        $ KittyX.change_face("sly")
        $ KittyX.change_stat("lust", 80, Shy)
        "[KittyX.name] seems a bit uncertain about the whole thing."
    else:

        $ KittyX.change_face("sly")
        $ KittyX.change_stat("love", 80, 1)
        $ KittyX.change_stat("lust", 80, Shy)
        "[KittyX.name] laughs under her breath and waggles the [Line] at you."
    return




label Kitty_Kate:
    $ KittyX.location = bg_current
    call set_the_scene (0)
    call Display_Girl (KittyX)
    call Taboo_Level
    $ Line = 0
    $ KittyX.change_face("bemused", 1)
    ch_k "Hey, [KittyX.player_petname]. . .you[KittyX.like]got a second?"
    menu:
        extend ""
        "Not really.":
            $ KittyX.change_face("angry", 1)
            ch_k "You're such a jerk, [Player.name]!"
            $ KittyX.change_stat("love", 200, -10)
            $ KittyX.change_stat("obedience", 50, 3)
        "Yeah. What's up?":

            pass
    $ KittyX.names.append("Kate")
    ch_k "I just wanted to let you know, I'm going by \"Kate\" now!"
    $ KittyX.name = "Kate"
    menu:
        extend ""
        "Oh no you aren't.":
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("obedience", 50, 10)
            $ KittyX.change_stat("inhibition", 80, -10)
            $ KittyX.change_face("angry", 2)
            ch_k "!!!"
            if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "O"):
                $ KittyX.name = "Kitty"
                $ KittyX.change_face("sadside", 1)
                $ KittyX.change_stat("obedience", 90, 10)
                $ KittyX.change_stat("inhibition", 80, -5)
                ch_k "Well. . . ok. . ."
            else:
                ch_k "You're not my supervisor!"
        "That's a good fit for you.":
            $ KittyX.change_face("smile", 1)
            $ KittyX.change_stat("love", 60, 5)
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("inhibition", 60, 5)
            ch_k "Thanks!"
        "I always thought \"Kitty\" sounded pretty.":
            $ KittyX.name = "Kitty"
            $ KittyX.change_stat("love", 90, 5)
            $ KittyX.change_stat("obedience", 70, 5)
            $ KittyX.change_stat("inhibition", 50, 5)
            ch_k "Oh, well I guess if you really like \"Kitty,\" I can understand that. . ."
        "Why?":
            $ KittyX.names.append("Katherine")
            ch_k "Well, my full name is \"Katherine Pryde\", and I thought \"Kate\" sounded more grown-up."
            menu:
                extend ""
                "Oh, ok then.":
                    $ KittyX.change_face("smile", 1)
                    $ KittyX.change_stat("love", 60, 5)
                    $ KittyX.change_stat("love", 90, 5)
                    $ KittyX.change_stat("inhibition", 60, 5)
                    ch_k ". . ."
                "No, it sounds silly.":
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 50, 10)
                    $ KittyX.change_stat("inhibition", 80, -10)
                    $ KittyX.change_face("angry", 2)
                    ch_k "!!!"
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "O"):
                        $ KittyX.name = "Kitty"
                        $ KittyX.change_face("sadside", 1)
                        $ KittyX.change_stat("obedience", 90, 10)
                        $ KittyX.change_stat("inhibition", 80, -5)
                        ch_k "Well. . . ok. . ."
                    else:
                        ch_k "You're not my supervisor!"
                "I suppose, but \"Kitty\" is such a pretty name.":
                    $ KittyX.change_stat("love", 90, 5)
                    $ KittyX.change_stat("inhibition", 50, 5)
                    if ApprovalCheck(KittyX, 800, "LO"):
                        $ KittyX.name = "Kitty"
                        $ KittyX.change_stat("obedience", 70, 5)
                        ch_k "Well, I guess if you prefer it. . ."
                    else:
                        ch_k "Well. . . too bad."
                "Why not \"Katherine\" then?":
                    $ KittyX.change_stat("obedience", 70, 5)
                    if ApprovalCheck(KittyX, 1200, "LO") or ApprovalCheck(KittyX, 500, "0"):
                        $ KittyX.name = "Katherine"
                        $ KittyX.change_stat("obedience", 90, 5)
                        ch_k "I suppose I could. . ."
                    else:
                        ch_k "I don't really like it that much. . ."
                        menu:
                            extend ""
                            "Ok, \"Kate\" it is then.":
                                $ KittyX.name = "Kate"
                                $ KittyX.change_face("smile", 1)
                                $ KittyX.change_stat("love", 60, 5)
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("inhibition", 60, 5)
                                ch_k ". . ."
                            "Ok, then back to \"Kitty?\"":
                                $ KittyX.change_stat("love", 90, 5)
                                $ KittyX.change_stat("inhibition", 50, 5)
                                if ApprovalCheck(KittyX, 800, "LO"):
                                    $ KittyX.name = "Kitty"
                                    $ KittyX.change_stat("obedience", 70, 5)
                                    ch_k "I suppose, if you prefer it that way. . ."
                                else:
                                    ch_k "Well. . . too bad."



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
