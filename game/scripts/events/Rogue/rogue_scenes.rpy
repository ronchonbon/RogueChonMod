

label Rogue_boyfriend:
    if RogueX.location != Player.location:
        "Suddenly, [RogueX.name] shows up and says she needs to talk to you."

        $ RogueX.location = Player.location

    call clear_the_room(RogueX)

    $ RogueX.change_face("bemused", blushing = 1)

    ch_r "So, [RogueX.player_petname], we've been hanging out for a while now."
    ch_r ". . ."

    $ RogueX.eyes = "sexy"

    menu:
        ch_r "Right?"
        "Yeah, it's been great.":
            call change_Girl_stat(RogueX, "love", 20)
        "Yeah, I guess":
            call change_Girl_stat(RogueX, "love", 10)
        "Um, maybe?":
            call change_Girl_stat(RogueX, "love", -10)
            call change_Girl_stat(RogueX, "obedience", 30)

    if RogueX.SEXP >= 10:
        ch_r "I mean, we've done some stuff. . ."

    if RogueX.SEXP >= 15:
        ch_r "Like {i}sex{/i} stuff. . ."

    if len(Player.Harem) > 1:
        ch_r "I know you've been going with those other girls, but we got talking and . . ."
    elif Player.Harem:
        ch_r "I know you've been going with [Player.Harem[0].name], but we got talking and . . ."

    if not Player.Harem and approval_check(RogueX, 750, "L"):
        ch_r "Right, so I was thinking. . ."
        ch_r "I haven't really been able to have a stable relationship, since I couldn't touch anyone."
        ch_r "This is all very new to me, but I'm feeling my way through it as best I can."
        ch_r "Let's make it official, you want to be my boyfriend?"
    elif Player.Harem:
        ch_r "I'd still like to be your girlfriend too."
    else:
        ch_r "You can be a real jerk sometimes, but still. . . I'm serious about this."
        ch_r "I think I want to be your girlfriend. . . officially."

    menu:
        extend ""
        "I'd love to!":
            call change_Girl_stat(RogueX, "love", 30)

            "Rogue leaps in and kisses you deeply."

            call kiss_launch(RogueX)

            $ RogueX.permanent_History["kiss"] += 1
        "Um, ok.":
            $ RogueX.brows = "confused"

            "[RogueX.name] is a bit put off by your casual acceptance of reality, but takes it as a positive sign and hugs you."
        "I'm with someone now." if Player.Harem:
            $ RogueX.change_face("sad", blushing = 1)

            menu:
                ch_r "I know, I know, I just thought maybe you could go out with me too?"
                "Sure.":
                    call change_Girl_stat(RogueX, "love", 30)

                    "Rogue leaps in and kisses you deeply."

                    call kiss_launch(RogueX)

                    $ RogueX.permanent_History["kiss"] += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                    $ line = "no."
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ line = "no."
                "I'm sorry, but. . . no.":
                    $ line = "no."
                "No way.":
                    jump Rogue_boyfriend_bad_ending

            if line == "no":
                call change_Girl_stat(RogueX, "love", -10)

                ch_r "I get it. That's fine."

                call remove_Girl(RogueX)

                return
        "Not really.":
            jump Rogue_boyfriend_bad_ending

    $ Player.Harem.append(RogueX)

    $ RogueX.change_face("sexy")
    $ RogueX.player_petnames.append("boyfriend")

    ch_r "Now, . . . boyfriend. . . how would you like to celebrate?"

    call enter_main_sex_menu(RogueX)

    return

label Rogue_boyfriend_bad_ending:
    $ RogueX.change_face("angry", blushing = 1)

    ch_r "Well fine!"

    call change_Girl_stat(RogueX, "love", -50)
    call change_Girl_stat(RogueX, "obedience", 40)

    if Player.location == RogueX.home:
        ch_r "Jerk! Out!"

        $ Player.traveling = True

        jump player_room
    else:
        call remove_Girl(RogueX)

        "[RogueX.name] storms off."

        $ RogueX.location = "bg_rogue"

    return

label Rogue_key:
    $ shift_focus(RogueX)
    call set_the_scene

    $ RogueX.change_face("bemused")
    $ RogueX.arm_pose = 2

    ch_r "Hey, you've been sleeping over a lot, I figured you might want a key?"
    ch_p "Thanks."

    $ RogueX.arm_pose = 1
    $ Player.Keys.append(RogueX)

    return








label Rogue_Love:
    $ shift_focus (RogueX)
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
            call change_Girl_stat(RogueX, "love", 50)
            $ RogueX.event_happened[6] = 10
        "Yeah, it's been great.":
            call change_Girl_stat(RogueX, "love", 20)
        "Yeah, I guess":
            call change_Girl_stat(RogueX, "love", 10)
        "Um, maybe?":
            call change_Girl_stat(RogueX, "love", -10)
            call change_Girl_stat(RogueX, "obedience", 30)
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
        $ RogueX.permanent_History["kiss"] += 1
    else:
        ch_r "Even though we've had our rough patches from time to time. . ."
        ch_r "I still love you."
    $ RogueX.event_happened[6] += 1
    if RogueX.event_happened[6] < 10:
        menu:
            extend ""
            "I love you too.":
                call change_Girl_stat(RogueX, "love", 50)
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
                call change_Girl_stat(RogueX, "love", -50)
                call change_Girl_stat(RogueX, "obedience", 50)
                jump Rogue_Love_Jerk
    $ RogueX.change_face("bemused", 1, eyes = "side")
    $ RogueX.player_petnames.append("lover")
    call Rogue_AnnaMarie
    ch_r "Anyway, I am glad I've been able to share this with you."
    $ RogueX.change_face("sly")
    ch_r "I'm hoping to share a lot more with you if I can. . ."
    if not RogueX.permanent_History["sex"]:
        call change_Girl_stat(RogueX, "obedience", 10)
        ch_r "So. . . did you want to . . . consumate this?"
        menu:
            extend ""
            "Yeah. . . [[have sex]":
                call change_Girl_stat(RogueX, "inhibition", 30)
                ch_r "Hmm. . ."
                if simulation:
                    return True

                call start_Action(RogueX, "sex")

                return
            "I have something else in mind. . .[[choose another activity]":
                $ RogueX.brows = "confused"
                call change_Girl_stat(RogueX, "obedience", 20)
                ch_r "Well now you've got me curious. . ."
                pass
            "Ew. [[do nothing]":
                call change_Girl_stat(RogueX, "love", -10)
                call change_Girl_stat(RogueX, "obedience", 40)
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
    call change_Girl_stat(RogueX, "obedience", 40)
    call change_Girl_stat(RogueX, "obedience", Count)
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
    call change_Girl_stat(RogueX, "love", -Count)
    if simulation:
        return False
    $ RogueX.location = "bg_rogue"
    $ Player.location = "bg_player"
    call remove_Girl(RogueX)
    jump player_room

label Rogue_AnnaMarie:
    ch_r "I should probably tell you, I wasn't exactly born with the name \"Rogue.\""
    ch_r ". . ."

    $ RogueX.change_face("bemused", blushing = 1)

    ch_r "Grow'in up, I went by \"Anna-Marie.\""

    $ RogueX.names.append("Anna-Marie")
    $ RogueX.names.append("Anna")
    $ RogueX.names.append("Marie")

    menu:
        extend ""
        "That's a lovely name.":
            $ RogueX.change_face("smile", blushing = 2)
            call change_Girl_stat(RogueX, "love", 10)
            call change_Girl_stat(RogueX, "obedience", 5)
            call change_Girl_stat(RogueX, "inhibition", 5)

            ch_r "Oh, thank you so much for say'in. . ."
        "Huh, ok.":
            $ RogueX.change_face("confused", blushing = 1)
            call change_Girl_stat(RogueX, "obedience", 5)

            ch_r "Um. . . yeah."
        "Don't like it.":
            $ RogueX.change_face("angry", blushing = 1)
            call change_Girl_stat(RogueX, "love", -5)
            call change_Girl_stat(RogueX, "obedience", 10)
            call change_Girl_stat(RogueX, "inhibition", -5)

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
    $ shift_focus (RogueX)
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
    if RogueX.permanent_History["fondle_breasts"]or RogueX.permanent_History["fondle_pussy"] or RogueX.permanent_History["fondle_ass"]:
        ch_r "I've let you touch me. . ."
    if RogueX.permanent_History["handjob"] or RogueX.permanent_History["blowjob"]:
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
            call change_Girl_stat(RogueX, "love", 20)
        "Yeah, I guess":
            call change_Girl_stat(RogueX, "love", 10)
        "Um, maybe?":
            call change_Girl_stat(RogueX, "love", -10)
            call change_Girl_stat(RogueX, "obedience", 30)
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
            call change_Girl_stat(RogueX, "obedience", 100)
            $ RogueX.player_petnames.append("sir")
            "[RogueX.name] nods obediently."
        "What do you mean by that?":
            $ RogueX.change_face("bemused")
            ch_r "When you. . . encourage me to try new things, it really turns me on."
            ch_r "I'd like you to continue to. . . encourage me."
            menu:
                ch_r "I mean that I would like you to give me orders, and I will follow them as best I can."
                "Sounds interesting, ok.":
                    call change_Girl_stat(RogueX, "obedience", 100)
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
    call change_Girl_stat(RogueX, "inhibition", 30)
    call change_Girl_stat(RogueX, "inhibition", Count)
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
    call change_Girl_stat(RogueX, "obedience", -Count)
    if simulation:
        return
    $ RogueX.location = "bg_rogue"
    $ Player.location = "bg_player"
    call remove_Girl(RogueX)
    jump player_room





label Rogue_Master:
    $ shift_focus (RogueX)
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
    if RogueX.permanent_History["anal"] or RogueX.permanent_History["dildo_ass"]:
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
            call change_Girl_stat(RogueX, "love", 20)
            call change_Girl_stat(RogueX, "obedience", 20)
        "Yeah, I guess.":
            call change_Girl_stat(RogueX, "love", 10)
            call change_Girl_stat(RogueX, "obedience", 20)
        "Not especially.":
            call change_Girl_stat(RogueX, "love", -10)
            call change_Girl_stat(RogueX, "obedience", 30)
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
            call change_Girl_stat(RogueX, "obedience", 100)
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
                    call change_Girl_stat(RogueX, "inhibition", 100)
                    call change_Girl_stat(RogueX, "inhibition", 50)
                    ch_r "For now at least. . ."
                    call change_Girl_stat(RogueX, "obedience", -200)
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
    call change_Girl_stat(RogueX, "inhibition", 30)
    call change_Girl_stat(RogueX, "inhibition", Count)
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
    call change_Girl_stat(RogueX, "obedience", -Count)
    if simulation:
        return
    $ RogueX.location = "bg_rogue"
    $ Player.location = "bg_player"
    call remove_Girl(RogueX)
    jump player_room





label Rogue_Sexfriend:
    $ shift_focus (RogueX)
    $ RogueX.daily_history.append("relationship")
    if RogueX in Player.Harem:
        if RogueX.location != Player.location and RogueX not in Player.Party:
            return
        $ RogueX.drain_word("asked_to_meet")
        if "stockings_and_garterbelt" not in RogueX.inventory:
            $ RogueX.inventory.append("stockings_and_garterbelt")
        $ RogueX.player_petnames.append("sex friend")
        call change_Girl_stat(RogueX, "inhibition", 50)
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
            call change_Girl_stat(RogueX, "love", 20)
            call change_Girl_stat(RogueX, "inhibition", 20)
        "Hmmm. . . yes?":
            call change_Girl_stat(RogueX, "inhibition", 20)
        "Maybe. . .":
            call change_Girl_stat(RogueX, "love", -10)
            call change_Girl_stat(RogueX, "obedience", 30)
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
                call change_Girl_stat(RogueX, "inhibition", 100)
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
    call change_Girl_stat(RogueX, "obedience", 30)
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
    call change_Girl_stat(RogueX, "inhibition", -Count)
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
    $ shift_focus (RogueX)
    $ RogueX.drain_word("asked_to_meet")
    if RogueX in Player.Harem:
        if RogueX.location != Player.location and RogueX not in Player.Party:
            return
        $ RogueX.player_petnames.append("fuck buddy")
        call change_Girl_stat(RogueX, "inhibition", 50)
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
            call change_Girl_stat(RogueX, "love", 20)
            call change_Girl_stat(RogueX, "obedience", 20)
            call change_Girl_stat(RogueX, "inhibition", 30)
        "Yeah?":
            call change_Girl_stat(RogueX, "love", 10)
            call change_Girl_stat(RogueX, "obedience", 20)
        "Whatever.":
            call change_Girl_stat(RogueX, "love", -10)
            call change_Girl_stat(RogueX, "obedience", 30)
    ch_r "So, since it's worked so far. . ."
    $ RogueX.event_happened[10] += 1
    $ RogueX.player_petnames.append("fuck buddy")
    if RogueX not in Player.Harem:
        ch_r "I'd like to be full on casual fuck buddies."
        menu:
            extend ""
            "Heh, ok, fuck buddy.":
                call change_Girl_stat(RogueX, "inhibition", 100)
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
    call change_Girl_stat(RogueX, "obedience", 30)
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
    call change_Girl_stat(RogueX, "inhibition", -Count)
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
    $ shift_focus (RogueX)
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
            call change_Girl_stat(RogueX, "love", 20)
            call change_Girl_stat(RogueX, "obedience", 10)
            call change_Girl_stat(RogueX, "inhibition", 30)
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
                    call change_Girl_stat(RogueX, "love", 15)
                    call change_Girl_stat(RogueX, "obedience", 20)
                    call change_Girl_stat(RogueX, "inhibition", 25)
                    ch_r "Great! . . daddy."
                    $ RogueX.player_petname = "daddy"
                "Could you not, please?":
                    call change_Girl_stat(RogueX, "love", 5)
                    call change_Girl_stat(RogueX, "obedience", 40)
                    call change_Girl_stat(RogueX, "inhibition", 20)
                    $ RogueX.change_face("sad")
                    ch_r " . . . "
                    ch_r "Well, ok."
                "No, that creeps me out.":
                    call change_Girl_stat(RogueX, "love", -10)
                    call change_Girl_stat(RogueX, "obedience", 45)
                    call change_Girl_stat(RogueX, "inhibition", 5)
                    $ RogueX.change_face("angry")
                    ch_r "Hrmph."
        "No, that creeps me out.":
            call change_Girl_stat(RogueX, "love", -5)
            call change_Girl_stat(RogueX, "obedience", 40)
            call change_Girl_stat(RogueX, "inhibition", 10)
            $ RogueX.change_face("angry")
            ch_r "Hrmph."
    $ RogueX.player_petnames.append("daddy")
    return
