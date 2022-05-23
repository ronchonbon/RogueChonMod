



























label StormMeetPrelude:
    "You hear a creaking noise from above you. You notice this happening more and more often lately."
    "Maybe next time you're in class, you can ask [EmmaX.name] about it."
    $ Player.add_word(1,0,0,0,"noise")
    return

label StormMeetAsk:
    $ bg_current = "bg_classroom"
    $ EmmaX.location = "bg_classroom"
    call clear_the_room (EmmaX, 0, 1)
    call shift_focus (EmmaX)
    call set_the_scene
    "Before class, you approach [EmmaX.name]."
    ch_p "I've been hearing creaking noises above me, do you have any idea what that could be?"
    $ EmmaX.change_face("_confused")
    ch_e "Oh. . ."
    $ EmmaX.change_face("_sly")
    ch_e "That's just the resident ghost."
    menu:
        ch_e "That's just the resident ghost."
        "Ghost?":
            pass
        "What?!":
            pass
        "Are you joking with me?":
            $ EmmaX.change_face("_angry")
            ch_e "I don't joke."
            $ EmmaX.change_face("_sly")
    ch_e "Yes, the ghost in the attic, [EmmaX.player_petname]."
    menu:
        extend ""
        "Is it dangerous?":
            pass
        "Oh, ok.":
            $ EmmaX.change_face("_confused")
            ch_e "Ok?"
            $ EmmaX.change_face("_angry",Eyes="_side")
            ch_e ". . ."
            $ EmmaX.change_stat("love", 70, -2)
            $ EmmaX.change_stat("obedience", 50, 1)
            ch_e "I suppose I expected you would be a bit more concerned. . ."
    $ EmmaX.change_face("_normal")
    ch_e "Well no, it probably isn't dangerous, but you might want to see for yourself. . ."
    menu:
        extend ""
        "Thanks for the heads up.":
            $ EmmaX.change_face("_smile")
            $ EmmaX.change_stat("love", 70, 3)
            $ EmmaX.change_stat("obedience", 50, 1)
            ch_e "Glad to be of help."
        "Ok.":
            ch_e "Right. . ."
    ch_e "Ok, now sit down, the lesson is about to begin."
    $ Player.add_word(1,0,0,0,"attic")
    $ StormX.broken_up[0] = 104
    $ Player.history.remove("noise")
    $ EmmaX.location = "bg_teacher"
    return

label StormMeetWater:

    "As you enter your room, you notice that there is a puddle on the floor."
    "It appears to be dripping from a crack in the ceiling."
    "It seems like the ghost in the attic might be more trouble than [EmmaX.name] let on."
    menu:
        "Let's go bust some ghosts!":
            "Hell yeah."
        "Guh-guh-guh-ghosts?!":
            "Stop being a pussy."
    if len(Party) > 1:
        Party[0].voice "I think we'll sit this one out."
        call remove_girl (Party[0])
        Party[0].voice "Have fun though."
        call remove_girl (Party[0])
    elif Party:
        Party[0].voice "I think I'll sit this one out."
        Party[0].voice "Have fun though."
        call remove_girl (Party[0])
    "You head for the door marked \"Attic. . .\""
    $ Player.add_word(1,"water",0,0,0)
    jump StormMeet


label StormMeet:
    if time_index > 2:
        if "noattic" in Player.daily_history:
            "No way, too spooky."
        else:
            "As you climb the stairs, a gust of chill wind rushes down them."
            "Oh, look at the time, maybe this is something that should wait for earlier in the day. . ."
        "You return to your room."
        $ bg_current = "bg_player"
        $ Player.add_word(1,0,"noattic",0,0)
        jump Misplaced

    $ Player.history.remove("attic")
    $ bg_current = "bg_storm"
    $ StormX.today_outfit = "casual1"
    $ StormX.outfit = "casual1"
    $ StormX.change_outfit("casual1")
    call clear_the_room ("All", 0, 1)
    $ StormX.broken_up[0] = 0
    $ StormX.location = 0
    $ StormX.love = 500
    $ StormX.obedience = 0
    $ StormX.inhibition = 100
    $ StormX.player_petname = 0
    $ StormX.names = ["Ororo"]
    "You climb the stairs up to the attic. Once you reach the top, you hit a wave of humidity."
    call shift_focus (StormX)
    call set_the_scene
    $ StormX.location = "bg_storm"
    $ StormX.sprite_location = stage_center
    "Greeting you at the top is what appears to be an indoor garden. Bright sunlight streams through the windows."


    $ StormX.change_outfit("nude")
    $ StormX.change_face("_normal",Eyes="_side")

    show Storm_Sprite at sprite_location(StormX.sprite_location)

    show expression AlphaMask("SilhouetteBase", At("Storm_Sprite", sprite_location(StormX.sprite_location))) as mask:
        offset (347,65)




    "Standing in the middle of the room appears to be a woman. . ."
    hide mask with fade


    "And she's naked."
    $ StormX.seen_breasts += 1
    $ StormX.seen_pussy += 1
    $ StormX.change_face("_normal")
    ch_u "Oh, hello there."
    menu:
        extend ""
        "Um. . . hello?":
            $ StormX.change_stat("love", 70, 2)
            ch_u "Yes, hello. Care to introduce yourself?"
        "Hey.":

            $ StormX.change_stat("obedience", 80, 2)
            ch_u "Yes? . . Care to introduce yourself?"
        "Wow.":

            $ StormX.change_face("_smile")
            $ StormX.change_stat("love", 70, 5)
            $ StormX.change_stat("inhibition", 200, 5)
            ch_u "I seem to have made an impression."
            ch_u "Care to introduce yourself?"
        ". . .":

            $ StormX.change_face("_perplexed")
            ch_u "Yes?"
            $ StormX.change_face("_normal")

    menu:
        extend ""
        "My name's [Player.name].":
            $ StormX.player_petname = Player.name
            $ StormX.change_face("_smile")
            $ StormX.change_stat("love", 70, 3)
            ch_u "A pleasure to meet you, [Player.name]."
        "It's \"Peter Parker.\"":
            $ StormX.player_petname = "Peter"
            $ StormX.change_face("_smile")
            $ StormX.change_stat("love", 70, 3)
            ch_u "A pleasure to meet you, Peter."
        "You first.":
            $ StormX.change_face("_normal")
            $ StormX.change_stat("love", 70, -2)
            $ StormX.change_stat("obedience", 80, 5)
            ch_u "I suppose I can indulge you. . ."

    ch_u "My name is \"Ororo Munroe.\" You may call me \"Ororo.\""
    $ StormX.name = "Ororo"
    $ StormX.change_face("_sly")
    ch_s "Or \"Ms. Munroe\" if you are nasty."
    $ StormX.names.append("Ms. Munroe")

    menu:
        extend ""
        "Pleased to meet you, Ororo.":
            $ StormX.change_face("_smile")
            $ StormX.change_stat("love", 70, 3)
        "Pleased to meet you, Ms. Munroe.":
            $ StormX.name = "Ms. Munroe"
            $ StormX.change_face("_surprised",Eyes="_closed",Mouth="_sucking")
            $ StormX.change_stat("love", 70, 5)
            $ StormX.change_stat("obedience", 80, 3)
            $ StormX.change_stat("inhibition", 200, 2)
            ch_s "Ha ha ha!"
            $ StormX.change_face("_smile")
            ch_s "Please indulge me the small joke."
            ch_s "\"Ororo\" is fine."
        "Don't I know you by another name?":

            $ StormX.change_stat("love", 70, 2)
            $ StormX.change_stat("obedience", 80, 3)
        "Ok, cool.":
            $ StormX.change_stat("obedience", 80, 2)
        ". . .":
            $ StormX.change_face("_normal")
            ch_s "Um. . ."

    ch_s "I've also been known to go by the name \"Storm\"."
    $ StormX.names.append("Storm")

    ch_p "Well then I'll call you. . ."
    menu:
        extend ""
        "Ororo.":
            $ StormX.name = "Ororo"
        "Ms. Munroe.":
            if StormX.name != "Ms. Munroe":
                $ StormX.change_face("_surprised",Eyes="_closed",Mouth="_sucking")
                $ StormX.change_stat("love", 70, 5)
                $ StormX.change_stat("obedience", 80, 3)
                $ StormX.change_stat("inhibition", 200, 2)
                ch_s "Hahaha!"
                $ StormX.change_face("_smile")
                ch_s "I intended it only as a joke!"
            $ StormX.name = "Ms. Munroe"
            $ StormX.change_stat("love", 70, 3)
            ch_s "Ha! Very well, it shall be our joke."
        "Storm.":
            $ StormX.name = "Storm"
            $ StormX.change_stat("obedience", 80, 5)
            ch_s "Oh, so formal. Very well."

    if not StormX.player_petname:

        ch_p "My name is [Player.name]."
        $ StormX.player_petname = Player.name
        $ StormX.change_stat("love", 70, 3)
        ch_s "A pleasure to meet you, [Player.name]."


    $ StormX.change_face("_confused")
    ch_s "So did you come all the way up here for a reason?"
    $ StormX.change_face("_normal")
    $ Count = 3
    while Count > 0:
        menu:
            extend ""
            "You're certainly naked." if "nudity" not in StormX.history:
                $ StormX.change_face("_smile",Eyes="_down")
                $ StormX.change_stat("love", 70, 2)
                $ StormX.change_stat("obedience", 80, 3)
                $ StormX.change_stat("inhibition", 200, 5)
                ch_s "Yes, I suppose that I am. . ."
                $ StormX.change_face("_normal")
                call Storm_Nudity
            "Don't you want to put something on?" if "nudity" not in StormX.history:
                $ StormX.change_face("_confused", Mouth="_sad")
                $ StormX.change_stat("love", 70, -2)
                $ StormX.change_stat("obedience", 80, 5)
                $ StormX.change_stat("inhibition", 200, -3)
                ch_s "Not unless it would make you more comfortable."
                call Storm_Nudity
            "About why I came up":

                menu:
                    extend ""
                    "I heard a lot of noise up here." if "noise" not in StormX.recent_history:
                        $ StormX.change_face("_surprised",2)
                        $ StormX.change_stat("love", 70, 2)
                        $ StormX.change_stat("obedience", 80, 5)
                        ch_s "Have I been making too much noise?"
                        $ StormX.change_face("_smile",1,Eyes="_down")
                        $ StormX.change_stat("obedience", 80, 5)
                        ch_s "I suppose that I should be a better neighbor."
                        $ StormX.change_face("_smile")
                        ch_s "Please accept my apology."
                        $ StormX.add_word(1,"noise",0,0,0)
                        menu:
                            extend ""
                            "None needed.":
                                $ StormX.change_stat("love", 70, 5)
                            "How will you make it up to me?":
                                $ StormX.change_face("_smile",Eyes="leftside")
                                ch_s ". . ."
                                $ StormX.change_face("_smile")
                                $ StormX.change_stat("obedience", 80, 5)
                                ch_s "I suppose by being more careful in future?"
                            "Ok.":
                                pass
                    "So about the leak." if "water" in Player.recent_history:
                        $ Player.drain_word("water")
                        "You point to some puddles under some of her plants."
                        $ StormX.change_face("_surprised",2,Eyes="leftside")
                        $ StormX.change_stat("obedience", 80, 5)
                        ch_s "Ah, yes. My apologies."
                        $ StormX.change_face("_smile",2,Brows="_sad")
                        ch_s "I was watering my plants, and must have gotten a bit out of hand."
                        $ StormX.change_face("_smile",1)
                        ch_s "One moment. . ."
                        $ StormX.change_face("_smile",Eyes="white")
                        "The wind picks up and swirls around the room, drying the puddles."
                        $ StormX.change_face("_smile")

                    "You do have lovely plants." if "plants" not in StormX.recent_history:
                        $ StormX.change_face("_smile")
                        $ StormX.change_stat("love", 70, 7)
                        $ StormX.change_stat("inhibition", 200, 5)
                        ch_s "Thank you."
                        $ StormX.change_face("_smile",Eyes="leftside")
                        ch_s "I do my best to bring a bit of nature into this place."
                        $ StormX.change_face("_smile")
                        $ StormX.add_word(1,"plants",0,0,0)

                    "[EmmaX.name] said that you were a ghost." if "ghost" not in StormX.recent_history:
                        $ StormX.change_face("_angry",Eyes="leftside")
                        ch_s "Oh, I expect she -would- say something like that. . ."
                        $ StormX.change_face("_smile")
                        ch_s "Obviously I am as alive as you are."
                        ch_s "I've just recently returned from sabbatical, and was preparing to rejoin the teaching staff."
                        $ StormX.add_word(1,"ghost",0,0,0)
                    "Never mind.":
                        pass

            "My name isn't -really- \"Peter.\"" if StormX.player_petname == "Peter":
                ch_p "It's [Player.name]."
                $ StormX.change_face("_surprised",Mouth="_smile")
                $ StormX.change_stat("love", 70, 3)
                $ StormX.change_stat("obedience", 80, 5)
                ch_s "Oh? A little joke then."
                $ StormX.change_face("_smile")
                ch_s "No harm done, \"Peter.\""
                $ StormX.player_petname = Player.name
            "So what powers do you have?" if "powers" not in StormX.recent_history:
                $ StormX.change_face("_smile")
                $ StormX.change_stat("love", 70, 3)
                ch_s "I have the ability to influence the weather around me."
                $ StormX.change_face("_smile", Eyes="white")
                call Punch
                ch_s "I can summon the rain, call lightning, even glide on the winds."
                $ StormX.change_face("_smile")
                ch_s "I very much enjoy the freedom my powers bring me, the connection to nature."
                $ StormX.add_word(1,"powers",0,0,0)
            "That's a lovely accent." if "accent" not in StormX.recent_history:
                $ StormX.change_face("_smile")
                $ StormX.change_stat("love", 70, 5)
                ch_s "Thank you."
                ch_s "I am originally from the States, but spent much of my youth in Kenya."
                $ StormX.add_word(1,"accent",0,0,0)
            "I suppose I should be going. . .":
                ch_s "Oh, I suppose so. . ."
                $ Count = 0



    $ StormX.change_face("_smile")
    ch_s "Well, it was lovely meeting you then. . ."
    "She extends her hand to shake yours."
    menu:
        extend ""
        "Shake":
            $ StormX.change_face("_surprised",2)
            "You grab her hand in a firm shake, and a shudder passes through her."
            $ StormX.addiction_rate += 1
            $ StormX.change_stat("lust", 70, 10)
            $ StormX.change_face("_confused")
            ch_s "What was -that-?"
            $ StormX.change_face("_surprised",Brows = "_sad")
            ch_s "I couldn't feel the winds around me!"
        "I probably shouldn't.":
            $ StormX.change_face("_confused")
            ch_s "Oh, why not?"

    ch_p "My powers allow me to remove the powers of other mutants."
    ch_p "When I touch them, it seems to have a. . . strong impact."
    if StormX.addiction_rate:
        $ StormX.change_face("_sadside",1)
        $ StormX.change_stat("love", 70, -15)
        $ StormX.change_stat("obedience", 80, 20)
        ch_s "Oh. You could have told me that. . ."
    else:
        $ StormX.change_face("_confused")
        $ StormX.change_stat("love", 70, 15)
        ch_s "Oh. . . well thank you for letting me know then."
    $ StormX.change_face("_normal")

    if "powers" not in StormX.recent_history:
        $ StormX.change_face("_smile")
        ch_s "I suppose you should know, I normally have the ability to influence the weather around me."
        $ StormX.change_face("_smile", Eyes="white")
        ch_s "I can summon the rain, call lightning, even glide on the winds."
        $ StormX.change_face("_smile")
        ch_s "I very much enjoy the freedom my powers bring me, the connection to nature."

    if "ghost" not in StormX.recent_history:
        ch_s "I suppose you'll be seeing more of me as I join the teaching rotation."

    ch_s "In any case, it was nice meeting you. I suppose I'll see you in class, [StormX.player_petname]."
    if "naked" in Player.recent_history:
        $ StormX.change_stat("love", 70, 5)
        $ StormX.change_stat("lust", 70, 3)
        ch_s "Oh, [StormX.player_petname]. . ."
        ch_s ". . .aren't you forgetting something?"
        ch_p "Oh, yeah. . ."
        $ Player.drain_word("naked")
        $ Player.drain_word("cockout")
        "You put your clothes back on. and head back to your room."
    else:
        "You head back to your room."
    if StormX.player_petname == "Peter":
        $ StormX.history.append("Peter")
    $ StormX.history.append("met")
    $ StormX.petname = StormX.name
    $ active_Girls.append(StormX) if StormX not in active_Girls else active_Girls
    $ EmmaX.weekly_schedule[1][0] = "bg_emma"
    $ EmmaX.weekly_schedule[1][1] = "bg_dangerroom"
    $ EmmaX.weekly_schedule[3][0] = "bg_emma"
    $ EmmaX.weekly_schedule[3][1] = "bg_dangerroom"

    $ round -= 20
    $ bg_current = "bg_player"
    jump Misplaced

    return

label Storm_Nudity:

    ch_s "I am not bothered. I do not value modesty so highly."
    ch_s "This is my body and I am unashamed to show it."
    $ StormX.change_face("_normal")
    $ StormX.history.append("nudity")
    while True:
        menu:
            extend ""
            "So you don't mind me looking?" if "looking" not in StormX.recent_history:
                $ StormX.add_word(1,"looking",0,0,0)
                $ StormX.change_face("_surprised")
                $ StormX.change_stat("love", 70, 3)
                $ StormX.change_stat("obedience", 80, 2)
                ch_s "How could I? It's only natural."
                $ StormX.change_face("_normal",Eyes="_side")
                ch_s ". . ."
                $ StormX.change_face("_sly")
                $ StormX.change_stat("inhibition", 200, 10)
                $ StormX.change_stat("lust", 50, 2)
                ch_s "Just try not to get too enthusiastic about it. . ."
                $ StormX.change_face("_normal")
                ch_s "Was there something else about my body?"
            "Well you're very beautiful." if "hot" not in StormX.recent_history:
                $ StormX.add_word(1,"hot",0,0,0)
                $ StormX.change_face("_smile")
                $ StormX.change_stat("love", 70, 10)
                $ StormX.change_stat("obedience", 80, 2)
                $ StormX.change_stat("inhibition", 200, 10)
                ch_s "Thank you. . ."
                ch_s "Was there something else about my body?"
            "Well you're really hot." if "hot" not in StormX.recent_history:
                $ StormX.add_word(1,"hot",0,0,0)
                $ StormX.change_face("_sly",Brows="_confused")
                $ StormX.change_stat("love", 70, 5)
                $ StormX.change_stat("obedience", 80, 10)
                $ StormX.change_stat("inhibition", 200, 10)
                $ StormX.change_stat("lust", 50, 2)
                ch_s ". . . Thank you. . ."
                $ StormX.change_face("_sly")
                ch_s "Was there something else about my body?"
            "You have a fantastic rack." if "tits" not in StormX.recent_history:
                $ StormX.add_word(1,"tits",0,0,0)
                $ StormX.change_face("_surprised",2)
                ch_s ". . ."
                $ StormX.change_face("_sly",1,Brows="_angry",Eyes="_down")
                $ StormX.change_stat("obedience", 80, 15)
                $ StormX.change_stat("inhibition", 200, 15)
                $ StormX.change_stat("lust", 50, 2)
                ch_s "Yes, I suppose that I do. . ."
                ch_s ". . ."
                $ StormX.change_face("_sly",Brows="_confused")
                ch_s "You are aware that this is a bit inappropriate?"
                menu:
                    extend ""
                    "Sorry.":
                        $ StormX.change_face("_smile",Eyes="_stunned")
                        $ StormX.change_stat("love", 70, 5)
                        $ StormX.change_stat("obedience", 80, -2)
                        ch_s "It's not a problem."
                        $ StormX.change_face("_smile")
                    "They're just so much nicer than [EmmaX.name]'s.":
                        $ StormX.change_face("_perplexed",2)
                        ch_s ". . ."
                        $ StormX.change_stat("love", 70, 2)
                        $ StormX.change_stat("obedience", 80, 2)
                        $ StormX.change_stat("inhibition", 200, 5)
                        ch_s "Thank you?"
                        $ StormX.change_face("_smile",1)
                        ch_s "I really don't see them as that much better. . ."
                    "They're just so much bigger than [KittyX.name]'s.":
                        $ StormX.change_face("_perplexed",2)
                        ch_s ". . ."
                        $ StormX.change_stat("love", 70, 3)
                        $ StormX.change_stat("obedience", 80, 2)
                        $ StormX.change_stat("inhibition", 200, 5)
                        ch_s "Thank you?"
                        $ StormX.change_face("_smile",1,Eyes="_side")
                        ch_s "Kitty's do have their own charm, certainly. . ."
                        $ StormX.change_face("_smile")
                    "Yeah.":
                        ch_s ". . ."
                        $ StormX.change_face("_smile")
                        $ StormX.change_stat("obedience", 80, 5)
                        ch_s "Well, so long as you are aware."
                ch_s "Was there something else about my body?"

            "Could I get a feel?" if "touching" not in StormX.recent_history:
                $ StormX.change_face("_angry",2,Eyes="_surprised")
                $ StormX.change_stat("love", 70, -10)
                $ StormX.change_stat("obedience", 80, 10)
                $ StormX.change_stat("lust", 50, 2)
                ch_s ". . ."
                call Storm_Touching
            "So what about sex, is that on the table?" if "touching" not in StormX.recent_history:
                $ StormX.change_face("_angry",2,Eyes="_surprised")
                $ StormX.change_stat("love", 70, -3)
                $ StormX.change_stat("obedience", 80, 5)
                $ StormX.change_stat("lust", 50, 2)
                ch_s ". . ."
                call Storm_Touching

            "You've certainly got a jungle going on down there." if "pubes" not in StormX.recent_history:
                $ StormX.add_word(1,"pubes",0,0,0)
                $ StormX.change_face("_angry",2,Eyes="_surprised")
                $ StormX.change_stat("love", 70, -10)
                $ StormX.change_stat("obedience", 80, 5)
                $ StormX.change_stat("inhibition", 200, -5)
                ch_s "I don't believe that's really an appropriate topic of conversation."
                menu:
                    extend ""
                    "I really like it, actually.":
                        $ StormX.change_stat("love", 70, 10)
                        $ StormX.change_stat("inhibition", 200, 15)
                        $ StormX.change_stat("lust", 50, 5)
                    ". . .":
                        pass
                $ StormX.change_face("_angry",2,Eyes="_down")
                ch_s "I just don't see the point in \"gardening\" down there. . ."
                $ StormX.change_face("_angry",1)

            "So could you put some clothes on?" if "nudity" in StormX.history and not StormX.top:
                $ StormX.change_face("_sly")
                $ StormX.change_stat("love", 70, -2)
                $ StormX.change_stat("obedience", 80, 5)
                $ StormX.change_stat("inhibition", 200, -3)
                ch_s "If it would make you more comforable, then I would not mind it."
                $ StormX.today_outfit = "casual1"
                $ StormX.outfit = "casual1"
                $ StormX.change_outfit("casual1")

            "Should I get naked too?" if "naked" not in Player.recent_history:
                $ StormX.change_face("_surprised",Mouth="_sucking")
                $ StormX.change_stat("love", 70, 3)
                $ StormX.change_stat("obedience", 80, 2)
                $ StormX.change_stat("inhibition", 200, 10)
                $ StormX.change_stat("lust", 50, 5)
                ch_s "Haha!"
                $ StormX.change_face("_smile")
                ch_s "If that would make you more comfortable, I do not mind."
                call Girl_First_Peen (StormX, 0, 1)
                $ StormX.change_face("_smile")
            "No, I suppose not. . . [[return]":
                return

    return

label Storm_Touching:

    $ StormX.change_face("_angry",1)
    ch_s "Do not confuse my words."
    ch_s "I am not ashamed of my body, but nor is it available for common use."
    menu:
        extend ""
        "Sorry, no offense intended.":
            $ StormX.change_face("_angry",Eyes="_side")
            $ StormX.change_stat("love", 70, 5)
            $ StormX.change_stat("obedience", 80, -2)
            $ StormX.change_stat("inhibition", 200, 5)
            ch_s "It is fine. I really cannot blame you for asking."
            $ StormX.change_face("_normal")
            ch_s "Children these days are so impulsive."
        "Who said I was \"common?\"":
            $ StormX.change_face("surpised",2,Mouth="_sucking")
            $ StormX.change_stat("love", 70, 5)
            $ StormX.change_stat("obedience", 80, 10)
            ch_s "Ha! You do have an excellent sense of humor."
            $ StormX.change_face("_sly",1)
            $ StormX.change_stat("love", 70, 3)
            ch_s "Certainly, you are \"uncommon.\""
            $ StormX.change_stat("inhibition", 200, 10)
            $ StormX.change_stat("lust", 50, 5)
            ch_s "-but I am afraid it will take more than that."
        "So. . . never?":
            $ StormX.change_face("_perplexed")
            $ StormX.change_stat("love", 70, 5)
            $ StormX.change_stat("obedience", 80, 10)
            ch_s ". . ."
            $ StormX.change_face("_sly",Eyes="_side")
            $ StormX.change_stat("inhibition", 200, 10)
            $ StormX.change_stat("lust", 50, 5)
            ch_s "I cannot say that it would be -impossible-. . ."
            $ StormX.change_face("_sly")
        "Ok.":
            $ StormX.change_face("_normal")
            $ StormX.change_stat("love", 70, 2)
            $ StormX.change_stat("obedience", 80, -2)
            ch_s "Glad to know that we have an understanding."
    $ StormX.add_word(1,"touching",0,0,0)

    ch_s "Now, was there something else about my body?"
    return

label Storm_Peter:

    $ StormX.history.remove("Peter")
    if Player.name == "Peter Parker":
        return
    $ bg_current = "bg_classroom"
    call clear_the_room (StormX, 0, 1)
    "Before class begins, [StormX.name] rushes up to you."
    $ StormX.location = "bg_classroom"
    call shift_focus (StormX)
    call set_the_scene
    $ StormX.change_face("_angry",2,Eyes="_surprised")
    ch_s "[Player.name]!"
    $ StormX.change_face("_angry")
    ch_s "Yes, I know your name is not \"Peter Parker.\""
    ch_s "Emma told me when I could not find your name on the roster."
    $ StormX.change_stat("love", 50, -5)
    $ StormX.change_stat("love", 60, -20)
    ch_s "I cannot believe you would make a fool of me like that."
    $ StormX.change_stat("love", 80, -50)
    $ StormX.change_stat("obedience", 80, 5)
    ch_s "I will not forget that."
    $ StormX.player_petname = Player.name
    $ bg_current = "bg_teacher"
    call set_the_scene
    return








label Storm_Teacher_Caught(Girl=0):


    if "noticed " + Girl.tag in StormX.recent_history:
        return
    if approval_check(StormX, 500, "I") and approval_check(StormX, 1500) and StormX.GirlLikeCheck(Girl) >= 500:
        "[StormX.name] notices the two of you, but just nods in approval and continues on."
        $ StormX.GLG(Girl,800,3,1)
        $ Girl.GLG(StormX,800,3,1)
        $ StormX.recent_history.append("noticed " + Girl.tag)
        return

    ch_s "[Player.name]? [Girl.name]? Could you please stop what you are doing there?"
    call checkout (1)

    $ Girl.change_face("_bemused", 2, Eyes="_side")
    call AllReset (Girl)
    if approval_check(Girl, 700, "I"):
        $ Girl.change_face("_bemused", 1)
        "[Girl.name] shrugs and returns to her seat."
        call Partner_Like (StormX, 2, -1, 500, Girl)
    else:
        "[Girl.name] jumps and dashes out of the room."
        call Partner_Like (StormX, -2, -3, 500, Girl)
        call remove_girl (Girl)

    $ Girl.reputation -= 1
    call Partner_Like (Girl, 3, 2, 800, StormX)
    $ StormX.GLG(Girl,800,3,1)

    $ Player.reputation -= 1
    ch_s "Thank you."

    jump Misplaced



label Storm_Hairtalk:

    call shift_focus (StormX)
    $ bg_current = "bg_classroom"
    $ StormX.location = "bg_classroom"
    call clear_the_room (StormX, 0, 1)
    call set_the_scene
    call AltClothes (StormX, 8)
    $ StormX.change_face("_normal")
    "When class ends, [StormX.name] calls you to her desk."
    ch_s "[StormX.player_petname], I was noticing that you seemed. . . distracted in class lately."
    ch_s "Was there anything I could do to help you remain attentive?"
    menu:
        extend ""
        "No, I'll try to pay better attention.":
            $ StormX.change_stat("love", 50, 2)
            $ StormX.change_stat("love", 70, 2)
            ch_s ". . ."
            ch_s "Very well then. . ."
        "You're just too beautiful.":
            $ StormX.change_stat("love", 60, 3)
            $ StormX.change_stat("love", 80, 2)
            $ StormX.change_face("_surprised")
            ch_s ". . ."
            $ StormX.change_face("_smile",Eyes="_side")
            $ StormX.change_stat("obedience", 80, 1)
            $ StormX.change_stat("inhibition", 80, 2)
            ch_s "That is sweet."
            $ StormX.change_face("_bemused")
            ch_s "But I would not wish to be to blame for your failing in class."
        "I can't help staring at your tits.":
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_stat("inhibition", 80, 2)
            $ StormX.change_face("_surprised")
            ch_s ". . ."
            if approval_check(StormX, 700):
                $ StormX.change_face("_confused",Eyes="_side")
                $ StormX.change_stat("love", 70, 2)
                ch_s "That is. . . sweet."
            else:
                $ StormX.change_face("_angry")
                $ StormX.change_stat("love", 70, -2)
                ch_s "That is completely inapprorpiate."
            $ StormX.change_face("_bemused")
            ch_s "But I would not wish to be to blame for your failing in class."
        "I don't know.":
            $ StormX.change_stat("love", 50, -1)
            $ StormX.change_stat("obedience", 80, -2)
            $ StormX.change_face("_confused")
            ch_s ". . ."
            $ StormX.change_face("_bemused")
            $ StormX.change_stat("inhibition", 80, 2)
            ch_s "Well, perhaps we could think of something?"
    ch_s "I was thinking that perhaps I could reward your performance. . somehow."
    $ StormX.add_word(1,"uninterrupted",0,0,0)
    $ Player.add_word(1,"interruption")
    menu:
        extend ""
        "That's fine, don't worry about it.":
            $ StormX.change_stat("love", 70, 1)
            $ StormX.change_stat("obedience", 80, -1)
            $ StormX.change_face("_confused")
            ch_s ". . ."
            $ StormX.change_face("_sad")
            ch_s ". . . If you are certain. . ."
        "Maybe you could flash me?":
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_face("_bemused", 1,Eyes="_side")
            pause 0.4
            $ StormX.eyes = "leftside"
            pause 0.4
            $ StormX.eyes = "_squint"
            if approval_check(StormX, 700):
                $ StormX.change_stat("love", 70, 2)
                $ StormX.change_stat("inhibition", 60, 1)
                ch_s "I. . . suppose that I might accomodate that. . ."
                $ StormX.change_stat("inhibition", 80, 2)
                $ StormX.top_pulled_up = 1
                $ StormX.upskirt = 1
                pause 1      
                $ StormX.top_pulled_up = 0
                $ StormX.upskirt = 0
                ch_s ". . ."
            else:
                $ StormX.change_stat("love", 70, -2)
                $ StormX.change_stat("inhibition", 80, 1)
                ch_s "I may be comfortable with my body, but that is an inappropriate request."
        "Maybe take some clothes off?":
            $ StormX.change_stat("obedience", 50, 2)
            $ StormX.change_stat("obedience", 80, 1)
            $ StormX.change_face("_bemused", 1,Eyes="_side")
            pause 0.4
            $ StormX.eyes = "leftside"
            pause 0.4
            $ StormX.eyes = "_squint"
            if approval_check(StormX, 800):
                $ StormX.change_stat("inhibition", 50, 1)
                $ StormX.change_stat("inhibition", 80, 2)
                $ taboo = 0
                $ StormX.taboo = 0
                ch_s "I. . . suppose that I might accomodate that. . ."
                call Girl_Undress (StormX)
                $ taboo = 40
                $ StormX.taboo = 40
            else:
                $ StormX.change_stat("love", 70, -2)
                $ StormX.change_stat("inhibition", 200, 5)
                ch_s "I may be comfortable with my body, but that is an inappropriate request."
        "Maybe a kiss?":
            $ StormX.change_stat("love", 70, 1)
            $ StormX.change_face("_bemused")
            if approval_check(StormX, 700) or StormX.Kiss:
                $ StormX.change_stat("love", 80, 3)
                $ StormX.change_stat("obedience", 80, 1)
                $ StormX.change_stat("inhibition", 80, 1)
                ch_s "I. . . suppose that I might accomodate that. . ."
                call Storm_SexAct ("kiss")
            else:
                $ StormX.change_stat("obedience", 80, -1)
                ch_s "I do not think that I should do that. . ."
        "Maybe some fondling?":
            $ StormX.change_stat("obedience", 80, 2)
            if approval_check(StormX, 900) or ((StormX.action_counter["fondle_breasts"]+ StormX.action_counter["fondle_pussy"] + StormX.action_counter["fondle_ass"]) > 0):
                $ StormX.change_face("_bemused", 1,Eyes="_side")
                pause 0.4
                $ StormX.eyes = "leftside"
                pause 0.4
                $ StormX.eyes = "_squint"
                $ StormX.change_stat("inhibition", 80, 2)
                ch_s "I. . . suppose that I might accomodate that. . ."
                $ StormX.change_stat("obedience", 50, 2)
                $ StormX.change_stat("obedience", 80, 1)
                call Storm_FB_Prep
            else:
                $ StormX.change_face("_angry", 2)
                ch_s "[StormX.player_petname]!"
                $ StormX.change_face("_angry", 1)
                $ StormX.change_stat("love", 70, -3)
                $ StormX.change_stat("obedience", 50, -1)
                ch_s "That would be highly inappropriate!"

    $ StormX.drain_word("uninterrupted")
    ch_s "Ok, I think that will be enough for now."
    "As you turn to leave, you notice a photo on the desk"
    show Storm_Photo zorder 150 with easeinbottom
    $ StormX.change_face("_bemused")
    ch_s "Oh, that was me during an earlier, more rebellious phase."
    hide Storm_Photo with easeoutbottom
    $ StormX.history.append("_mohawk")
    menu:
        extend ""
        "You look great like that.":
            $ StormX.change_stat("love", 70, 2)
            $ StormX.change_face("_smile")
            ch_s "Oh, should I try it again?"
            menu:
                extend ""
                "Sure, go for it.":
                    $ StormX.change_stat("love", 50, 1)
                    $ StormX.change_stat("love", 70, 1)
                    $ StormX.change_stat("obedience", 80, 2)
                    if approval_check(StormX, 700):
                        ch_s "I think that I shall."
                        $ StormX.to_do.append("hair")
                    else:
                        ch_s "I may consider it in future. . ."
                "Not really, you look great this way too.":
                    $ StormX.change_stat("love", 50, 1)
                    $ StormX.change_stat("love", 70, 2)
                    $ StormX.change_stat("inhibition", 80, 2)
                    ch_s "Thank you, I appreciate that. . ."
                "No.":
                    $ StormX.change_stat("love", 70, -1)
                    $ StormX.change_face("_sadside")
                    ch_s ". . ."
                    $ StormX.change_stat("obedience", 50, 2)
                    $ StormX.change_stat("obedience", 80, 1)
                    ch_s "I suppose I can understand that. . ."
                    $ StormX.change_face("_bemused")
                    ch_s "I do enjoy my current style. . ."
        "I don't think that look works for you.":
            $ StormX.change_stat("love", 50, -2)
            $ StormX.change_face("_sadside")
            ch_s ". . ."
            $ StormX.change_stat("obedience", 50, 1)
            $ StormX.change_stat("obedience", 80, 2)
            ch_s "I suppose I can understand that. . ."
            $ StormX.change_face("_bemused")
            ch_s "I do enjoy my current style. . ."
        "Ok.":
            $ StormX.change_stat("obedience", 50, 2)
    ch_s "I suppose that is all I needed to tell you. . ."
    return



label Storm_Detention:

    call shift_focus (StormX)
    call clear_the_room (StormX, 0, 1)
    if "traveling" in Player.recent_history:
        "You enter the room and see [StormX.name] waiting for you at the back of the room."
    else:
        "After class, the students file out, and you wait a few minutes until they're all gone."
        "Once the last student leaves, [StormX.name] approaches you."
    show blackscreen onlayer black
    $ bg_current = "bg_classroom"
    $ StormX.location = "bg_classroom"
    $ StormX.change_outfit()
    call set_the_scene
    $ StormX.change_face("_sly")
    $ StormX.arm_pose = 2
    $ Count = 0
    call clear_the_room (StormX, 0, 1)
    hide blackscreen onlayer black
    $ Line = 0
    if "detention" in Player.daily_history:
        ch_s "I'm glad you take your. . . education seriously."
    else:

        $ StormX.change_face("_surprised")
        ch_s "Oh, [StormX.player_petname], you really shouldn't skip your detention like that. . ."
    $ Player.traits.remove("detention")
    $ StormX.recent_history.append("detention")
    $ StormX.daily_history.append("detention")
    $ StormX.change_face("_sly")
    $ StormX.change_stat("lust", 80, 3)
    ch_s "You've been such a naughty pupil. . ."
    $ StormX.arm_pose = 1
    $ StormX.change_face("_sadside", Brows="_normal")
    $ StormX.change_stat("lust", 80, 5)
    ch_s "Chasing after those young girls. . ."
    $ StormX.change_face("_sly")
    $ StormX.change_stat("lust", 80, 3)
    if "detention" in StormX.history:
        ch_s "How will we deal with it this time?"
    else:

        ch_s "What am I to do with you. . ."
        $ StormX.history.append("detention")

    "[StormX.name] walks to the door and locks it behind her."
    $ taboo = 0
    $ StormX.taboo = 0
    $ Player.traits.append("locked")
    menu:
        extend ""
        "I guess I should focus on my studies.":
            if approval_check(StormX, 900) and "classcaught" in StormX.history:
                $ StormX.change_face("_perplexed")
                $ StormX.change_stat("inhibition", 70, -3)
                $ StormX.change_stat("lust", 80, 5)
                ch_s "Oh. Really? I was thinking of a more. . . recreational punishment."
                menu:
                    extend ""
                    "Kidding, of course, what should we do? [[sex stuff]":
                        $ StormX.change_face("_sly")
                        $ StormX.change_stat("love", 90, 3)
                        $ StormX.change_stat("obedience", 60, 5)
                        $ StormX.change_stat("inhibition", 70, 5)
                        ch_s "Why do I put up with you?"
                        call Storm_SexMenu
                    "No, you're right, I take my education too lightly.":
                        $ StormX.change_stat("love", 80, 1)
                        $ StormX.change_stat("inhibition", 70, -2)
                        $ StormX.change_stat("lust", 80, 5)
                        ch_s "Oh. Ok. Um. . ."
                        $ StormX.change_face("_sad")
                        $ StormX.change_stat("obedience", 60, 5)
                        $ StormX.change_stat("lust", 80, 5)
                        ch_s "I guess we could go over some of the topics from today's class then. . ."
                        $ StormX.change_stat("lust", 80, 5)
                        $ Player.XP += 10
            else:

                $ StormX.change_face("_sad", Mouth="_normal")
                $ StormX.change_stat("love", 50, 5)
                $ StormX.change_stat("love", 80, 5)
                $ StormX.change_stat("obedience", 60, 5)
                $ StormX.change_stat("lust", 80, 5)
                ch_s "Yes. . . Exactly. . ."
                $ StormX.change_stat("inhibition", 50, 5)
                $ StormX.change_stat("lust", 80, 5)
                ch_s "I guess we could go over some of the topics from today's class then. . ."
                $ StormX.change_stat("inhibition", 70, 5)
                $ StormX.change_stat("lust", 80, 5)
                $ Player.XP += 10
        "I could think of a few things. . . [[sex stuff]":
            if approval_check(StormX, 900) and "classcaught" in StormX.history:
                $ StormX.change_face("_sly")
                $ StormX.change_stat("lust", 80, 5)
                $ StormX.change_stat("love", 90, 5)
                $ StormX.change_stat("obedience", 60, 5)
                $ StormX.change_stat("inhibition", 70, 5)
                ch_s "I just bet you can. . ."
                call Storm_SexMenu
            else:

                $ StormX.change_face("_sad", Mouth="_smirk")
                $ StormX.change_stat("love", 80, 5)
                $ StormX.change_stat("obedience", 60, 5)
                $ StormX.change_stat("lust", 80, 5)
                ch_s "I'm sure you could. . . but unfortunately this isn't the time for it."
                $ StormX.change_stat("inhibition", 50, 5)
                $ StormX.change_stat("inhibition", 70, 5)
                $ StormX.change_stat("lust", 80, 5)
                ch_s "We'll just have to settle for going over some of the topics from today's class. . ."
                $ StormX.change_stat("inhibition", 50, 5)
                $ StormX.change_stat("lust", 80, 5)
                $ Player.XP += 10
    $ round = 20 if round > 20 else round
    ch_s "Ok, I think that's plenty for now. . ."
    ch_s "You wouldn't want to make this a habit. . ."
    $ approval_bonus = 0
    $ StormX.change_outfit()
    $ Player.drain_word("locked",0,0,1)
    return








label Storm_Key:
    call shift_focus (StormX)
    call set_the_scene
    $ StormX.change_face("_bemused")
    $ StormX.arm_pose = 2
    ch_s "You have been coming up more often. . ."
    ch_s ". . . you might want a key. . ."
    ch_p "Thanks."
    $ StormX.arm_pose = 1
    $ keys.append(StormX)
    $ StormX.event_happened[0] = 1
    return






label Storm_BF:
    call shift_focus (StormX)
    if StormX.location != bg_current:
        $ StormX.location = bg_current
        if StormX not in Party:
            "[StormX.name] approaches you and asks if the two of you can talk."
        else:
            "[StormX.name] turns towards you and asks if the two of you can talk."
    $ StormX.drain_word("asked_to_meet")

    call set_the_scene (0)
    call show_girl (StormX)
    call taboo_Level
    call clear_the_room (StormX)
    $ StormX.daily_history.append("relationship")

    $ StormX.change_face("_smile")
    ch_s "[StormX.player_petname]. . . I was hoping that we could talk. . ."
    menu:
        extend ""
        "Yes?":
            pass
        "I'm kinda busy.":
            $ StormX.change_face("_sadside")
            $ StormX.change_stat("love", 90, -5)
            $ StormX.change_stat("obedience", 50, 2)
            ch_s "Then I won't take more of your time than is necessary."
            $ StormX.change_face("_grimace")

    $ StormX.event_happened[5] = 20

    ch_s "I have been enjoying the time we've spent together."
    ch_s "I mean to say, I have been enjoying you."
    $ StormX.change_face("_smile",Eyes="_side")
    ch_s ". . ."
    $ StormX.change_face("_smile")
    ch_s "May I tell you a story?"
    menu:
        extend ""
        "Sure.":
            pass
        "Can we not?":
            $ StormX.change_stat("love", 90, -5)
            $ StormX.change_stat("obedience", 50, 3)
            $ StormX.change_stat("inhibition", 70, -2)
            $ StormX.change_face("_confused")
            ch_s "I think you will benefit from it."
        "Like I said, I'm really busy here.":
            $ StormX.change_face("_sadside")
            $ StormX.change_stat("love", 90, -5)
            $ StormX.change_stat("obedience", 60, 5)
            $ StormX.change_stat("inhibition", 70, -2)
            ch_s "Then I won't take more of your time."
            ch_s "Let me know when your. . . schedule clears up."
            call remove_girl (StormX)
            $ Player.history.append("story")
            return

label Storm_BF_Story:
    $ StormX.change_face("_smile")
    ch_s "When I was a child, I spent a lot of my time alone."
    ch_s "I was abandoned on the streets of Cairo, and had to fend for myself. . ."
    $ StormX.change_face("_sadside")
    ch_s ". . . as a pickpocket."
    ch_s "Years later, I travelled south to Kenya, but for so much of my time, I had nobody that I could count on."
    $ StormX.change_face("_smile")
    ch_s "Since I have come here, I have learned to value the strong bonds that I have with my teammates."
    if Player.Harem:
        if len(Player.Harem) >= 2:
            ch_s "And I know that you have been sharing your time with other girls,"
        else:
            ch_s "And I know that you have been sharing your time with [Player.Harem[0].name],"
        if approval_check(StormX, 1500):
            $ StormX.change_stat("obedience", 60, 2)
            $ StormX.change_stat("inhibition", 70, 2)
            ch_s ". . . but I can accept that."
        else:
            ch_s ". . . and we can discuss that. . ."
    $ StormX.change_face("_sly")
    ch_s "I just want to know that you are there for me too."
    menu:
        extend ""
        "Of course I am.":
            $ StormX.change_face("_smile")
            $ StormX.change_stat("love", 90, 7)
            $ StormX.change_stat("obedience", 60, 2)
            $ StormX.change_stat("inhibition", 70, 2)
            ch_s "That is a relief to hear."
        "I'm not big on commitment. . .":
            $ StormX.change_face("_sadside")
            $ StormX.change_stat("love", 90, -5)
            $ StormX.change_stat("obedience", 60, 5)
            $ StormX.change_stat("inhibition", 70, -2)
            ch_s ". . . that is unfortunate."
            $ StormX.change_face("_sad")
            ch_s "Let me know if you should reconsider then."
            return
        "Well, I guess. . .":
            $ StormX.change_face("_sadside")
            $ StormX.change_stat("love", 90, -3)
            $ StormX.change_stat("obedience", 60, 1)
            $ StormX.change_stat("inhibition", 70, -2)
            ch_s "That is. . . not exactly the answer I was looking for. . ."

    if Player.Harem:
        if approval_check(StormX, 1500):

            $ StormX.change_face("_sly",Eyes="_side")
            $ StormX.change_stat("obedience", 80, 5)
            $ StormX.change_stat("inhibition", 80, 5)
            ch_s "I would be happy to join your little \"harem.\""
            $ StormX.change_face("_sly")
            ch_s "If you'll have me."
        else:

            ch_s "I would prefer to be your one and only. . ."
            menu:
                extend ""
                "I could break up with them. . ." if len(Player.Harem) >= 2:
                    $ StormX.change_face("_smile")
                    $ StormX.change_stat("love", 90, 10)
                    $ StormX.change_stat("obedience", 60, 5)
                    $ StormX.change_stat("inhibition", 70, 5)
                    ch_s "Excellent!"
                    ch_s "Do let them down gently though. . ."
                    return
                "I could break up with her. . ." if len(Player.Harem) == 1:
                    $ StormX.change_face("_smile")
                    $ StormX.change_stat("love", 90, 10)
                    $ StormX.change_stat("obedience", 60, 5)
                    $ StormX.change_stat("inhibition", 70, 5)
                    ch_s "Excellent!"
                    ch_s "Do let her down gently though. . ."
                    return
                "I can't do that.":
                    $ StormX.change_face("_sadside")
                    $ StormX.change_stat("love", 90, -5)
                    $ StormX.change_stat("obedience", 60, 5)
                    $ StormX.change_stat("obedience", 80, 5)
                    $ StormX.change_stat("inhibition", 70, -3)
                    ch_s ". . .oh."
                    ch_s "Well that is a disappointment."
                    if not approval_check(StormX, 1000):
                        ch_s "I suppose that will be all then."
                        call remove_girl (StormX)
                        return
                    else:
                        $ StormX.change_stat("obedience", 80, 5)
                        $ StormX.change_stat("inhibition", 60, 3)
                        $ StormX.change_stat("inhibition", 70, 2)
                        ch_s ". . . I suppose that I could accept this. . . arrangement."
        menu:
            extend ""
            "I would love that!" if "StormYes" in Player.traits:
                $ StormX.change_stat("love", 90, 20)
                $ StormX.change_stat("inhibition", 70, 5)
                ch_s "Excellent!"
                jump Storm_BF_End
            "I would love that. . . but. . ." if "StormYes" not in Player.traits:
                $ StormX.change_face("_confused")
                $ StormX.change_stat("love", 90, 5)
                $ StormX.change_stat("obedience", 60, 5)
                ch_s ". . . but?"
                if len(Player.Harem) >= 2:
                    ch_p "The others weren't into that. . ."
                else:
                    ch_p "[Player.Harem[0].name] wasn't into that. . ."
                $ StormX.change_face("_sadside")
                ch_s ". . .oh."
                ch_s "Well that is a disappointment."
                ch_s "Let me know if the situation. . . clears up."
            "No thanks.":
                $ StormX.change_face("_sadside")
                $ StormX.change_stat("love", 90, -25)
                $ StormX.change_stat("obedience", 60, 10)
                ch_s ". . .oh."
                ch_s "Very well then."
                ch_s "I will take no more of your time."
    else:


        ch_s "So would you mind if I considered you my. . . \"boyfriend?\""
        menu:
            extend ""
            "I'd love that!":
                $ StormX.change_stat("love", 90, 20)
                $ StormX.change_stat("inhibition", 70, 5)
                $ StormX.change_face("_smile")
                ch_s "Excellent!"
                jump Storm_BF_End
            "I'd rather you didn't.":
                $ StormX.change_stat("love", 90, -20)
                $ StormX.change_stat("obedience", 50, 5)
                $ StormX.change_stat("obedience", 70, 5)
                $ StormX.change_face("_sadside")
                ch_s ". . .oh."
                ch_s "Well that is a disappointment."
            "Suit yourself.":
                $ StormX.change_stat("love", 90, -5)
                if approval_check(StormX, 1000):
                    $ StormX.change_face("_confused")
                    $ StormX.change_stat("obedience", 50, 5)
                    $ StormX.change_stat("obedience", 80, 5)
                    ch_s ". . .very well then. I shall do that. . ."
                    jump Storm_BF_End
                else:
                    $ StormX.change_face("_sadside")
                    $ StormX.change_stat("obedience", 60, 5)
                    ch_s ". . . that was not the reaction I had expected. . ."
                    ch_s "Perhaps I should give this further consideration. . ."

    return
label Storm_BF_End:
    $ StormX.player_petnames.append("boyfriend")

    if not simulation:
        $ Player.Harem.append(StormX)
        if "StormYes" in Player.traits:
            $ Player.traits.remove("StormYes")
    return






label Storm_Love:

    $ StormX.drain_word("asked_to_meet")
    if StormX.location == bg_current or StormX in Party:
        "[StormX.name] glances over at you with an apprising look on her face."
    else:
        "[StormX.name] turns a corner and notices you."
    if bg_current != "bg_storm" and bg_current != "bg_player":
        "With little word, she takes your hand and pulls you up to her room."
        $ bg_current = "bg_storm"
    $ StormX.location = bg_current
    call set_the_scene
    call clear_the_room (StormX)
    call taboo_Level
    $ StormX.daily_history.append("relationship")

    $ StormX.change_face("_sadside",1)
    ch_s "[StormX.player_petname]. . . I have a bit of a problem. . ."
    menu:
        extend ""
        "What is it?":
            $ StormX.change_stat("love", 200, 2)
            $ StormX.change_stat("inhibition", 80, 1)
            $ StormX.change_face("_smile")
        "Can I help?":
            $ StormX.change_stat("love", 200, 2)
            $ StormX.change_stat("obedience", 50, 2)
            $ StormX.change_face("_smile")
            ch_s "Perhaps. . ."
        "That sucks.":
            $ StormX.change_stat("love", 200, -5)
            $ StormX.change_stat("inhibition", 90, 2)
            $ StormX.event_happened[6] += 1
            $ StormX.change_face("_angry",2)
            ch_s ". . ."
            $ StormX.change_face("_normal",1)
        "Ok.":
            $ StormX.change_stat("love", 200, -3)
            $ StormX.change_face("_confused",1)
            if not approval_check(StormX, 800, "OI"):
                $ StormX.event_happened[6] += 1
                $ StormX.change_stat("love", 200, -2)
            ch_s ". . ."
    if len(Player.Harem) >= 2:
        ch_s "I know that you have to divide yourself among multiple women. . ."
    elif StormX in Player.Harem:
        ch_s "We make a pretty cute couple so far. . ."
    $ StormX.change_face("_sad",1)
    ch_s "I have been considering my feelings for you. . ."
    $ StormX.change_face("_sadside",1)
    ch_s "I have reached an uncomfortable conclusion."
    ch_s "I feel that I am somewhat \"bound\" you to. . ."
    menu:
        extend ""
        "What do you mean?":
            $ StormX.change_stat("love", 200, 2)
            $ StormX.change_stat("inhibition", 80, 1)
            $ StormX.change_face("_normal",1)
            ch_s "Allow me to explain. . ."
        "Is it something I did?":
            $ StormX.change_stat("love", 200, -1)
            $ StormX.change_stat("inhibition", 60, -2)
            $ StormX.change_face("_surprised",1)
            ch_s "Oh, no, not intentionally, at least. . ."
            $ StormX.change_face("_normal",1)
        "Kinky.":
            $ StormX.change_stat("obedience", 90, 3)
            $ StormX.change_stat("inhibition", 80, 5)
            $ StormX.change_face("_confused",1)
            if not approval_check(StormX, 600, "OI"):
                $ StormX.change_stat("love", 200, -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("_sly",1)
            ch_s ". . . that is. . . not the reaction I intended. . ."
            $ StormX.change_face("_normal",1)
        "Ok":
            $ StormX.change_stat("obedience", 70, 2)
            $ StormX.change_face("_confused",1)
            if not approval_check(StormX, 800, "OI"):
                $ StormX.change_stat("love", 200, -2)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("_angry",1)
            ch_s ". . ."
    ch_s "My concern leads back to my childhood."
    $ StormX.change_face("_sadside",1)
    ch_s "When I was very young, a building I was in was hit by a terrorist attack."
    ch_s "It fell around me, trapping me under the rubble."
    $ StormX.eyes = "_closed"
    ch_s "For days I was surrounded by the earth, barely able to move."
    ch_s ". . . barely able to breathe."
    menu:
        extend ""
        "How awful!":
            $ StormX.change_stat("love", 200, 4)
            $ StormX.change_face("_normal",1)
            ch_s "Yes, but I managed."
        "That must have been difficult.":
            $ StormX.change_stat("love", 200, 5)
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_stat("inhibition", 80, 2)
            $ StormX.change_face("_smile",1,Eyes="_side")
            ch_s "Thank you, yes, but I managed."
        "Wow.":
            $ StormX.change_stat("obedience", 90, 2)
            $ StormX.change_face("_confused",1)
            if not approval_check(StormX, 600, "OI"):
                $ StormX.change_stat("love", 200, -3)
                $ StormX.change_stat("inhibition", 80, -2)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("_angry",1)
            ch_s ". . ."
            ch_s "Yes. \"Wow.\""
        "Cool!":
            $ StormX.change_stat("love", 200, -5)
            $ StormX.event_happened[6] += 1
            $ StormX.change_face("_surprised",2)
            ch_s ". . ."
            $ StormX.change_face("_angry",1)
            ch_s "Perhaps try not to sound so excited?"
        "Ok.":
            $ StormX.change_stat("love", 200, -2)
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_stat("inhibition", 80, 1)
            $ StormX.change_face("_sadside",1)
            if not approval_check(StormX, 800, "OI"):
                $ StormX.change_stat("love", 200, -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("_angry",1)
            ch_s ". . ."
            ch_s "I did expect a bit more \"engagement\" here. . ."
    ch_s "At the end of the third day, the concrete above me shifted, and a hand reached down."
    $ StormX.change_face("_smile",1)
    ch_s "Workers had managed to find me and dig their way to me."
    $ StormX.change_face("_sadside",1)
    ch_s "Even after I'd recovered from the physical trauma of the event, I wasn't competely healed."
    ch_s " I found that I had lasting mental scars from the experience. . ."
    menu:
        extend ""
        "I can understand that.":
            $ StormX.change_stat("love", 200, 5)
            $ StormX.change_stat("obedience", 80, 1)
            $ StormX.change_face("_smile",1)
            ch_s "I love that about you. . ."
        "What kind?":
            $ StormX.change_stat("love", 200, 4)
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_stat("inhibition", 80, 2)
            $ StormX.change_face("_normal",1)
        "Yeah, I bet.":
            $ StormX.change_stat("love", 200, -2)
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_face("_angry",1,Brows="_confused")
            ch_s ". . ."
        "So you're crazy then?":
            $ StormX.change_stat("love", 200, -5)
            $ StormX.change_stat("obedience", 80, 5)
            $ StormX.change_stat("inhibition", 80, -5)
            $ StormX.event_happened[6] += 2
            $ StormX.change_face("_angry",2)
            ch_s "Of course not!"
            ch_s "That is an inapporpriate way to discuss such things."
            $ StormX.blushing = "_blush1"
        "Ok.":
            $ StormX.change_stat("love", 200, -5)
            $ StormX.event_happened[6] += 1
            $ StormX.change_face("_angry",1,Eyes="_side")
            ch_s "Why do I feel like you are not engaged in this conversation?"

    ch_s "The experience left me with fairly strong \"claustrophobia.\" a fear of confinement."
    ch_s "It made me seek out open spaces, places from which I always felt like I could flee."
    $ StormX.change_face("_bemused",1)
    ch_s "So I expect that you understand what a difficulty you've caused me. . ."
    $ Line = 1
    while Line > 0:
        $ Line -= 1
        menu:
            extend ""
            "Yeah, I understand." if "iknow" not in StormX.recent_history:
                $ StormX.change_stat("love", 200, 2)
                $ StormX.change_stat("obedience", 80, 2)
                $ StormX.add_word(1,"iknow",0,0,0)
                $ StormX.change_face("_smile",1,Brows = "_confused")
                $ Line += 1
                ch_s "Oh?"
            "I'm afraid I don't. . .":
                if "iknow" in StormX.recent_history and "strong" not in StormX.recent_history:

                    $ StormX.change_stat("love", 200, -2)
                    $ StormX.change_stat("obedience", 80, -5)
                    $ StormX.change_stat("inhibition", 80, 2)
                    ch_s ". . ."
                    $ StormX.change_face("_sadside",1)
                    ch_s "You seemed so confident. . ."
                else:
                    $ StormX.change_stat("love", 200, 5)
                    $ StormX.change_stat("obedience", 80, -2)
                    $ StormX.change_stat("inhibition", 80, 5)
                    $ StormX.change_face("_smile",1)
                    ch_s "That is fair. . ."
            "You feel like I trap you.":
                $ StormX.change_stat("love", 200, 7)
                $ StormX.change_stat("obedience", 80, 2)
                $ StormX.change_face("_sad",1)
                ch_s "Yes. . . I'm afraid so. . ."
            "You think I'm too strong." if "strong" not in StormX.recent_history:
                $ StormX.change_face("_confused",1)
                ch_s "What?"
                menu:
                    extend ""
                    "Nothing! Never mind.":
                        $ StormX.change_stat("obedience", 80, -2)
                        ch_s "Ok. . ."
                    "Like, I can hold you and you can't get away.":
                        $ StormX.change_stat("love", 200, -3)
                        $ StormX.change_stat("obedience", 80, -1)
                        $ StormX.change_face("_surprised",1)
                        ch_p "Because I'm strong."
                        $ StormX.change_stat("obedience", 80, -1)
                        $ StormX.change_stat("inhibition", 80, -2)
                        $ StormX.change_face("_angry",1)
                        ch_s ". . ."
                        ch_s "No."
                $ StormX.add_word(1,"strong",0,0,0)
                $ Line +=1
            "Nope.":
                $ StormX.change_stat("love", 200, -5)
                $ StormX.change_stat("obedience", 80, -2)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("_angry",1)
                ch_s ". . ."
                $ StormX.eyes = "_side"
                ch_s "I suppose that should not surprise me. . ."
            "Lady problems,\" right?":
                $ StormX.change_stat("love", 200, -10)
                $ StormX.event_happened[6] += 2
                $ StormX.change_face("_surprised",2)
                ch_s ". . ."
                $ StormX.change_stat("obedience", 80, -2)
                $ StormX.change_stat("inhibition", 80, -2)
                $ StormX.change_face("_angry",2)
                ch_s ". . .No."
                $ StormX.blushing = "_blush1"
                ch_s "It is not. . . \"lady problems.\""
            "[[shrug]":
                $ StormX.change_stat("love", 200, -3)
                if not approval_check(StormX, 800, "OI"):
                    $ StormX.change_stat("love", 200, -2)
                    $ StormX.event_happened[6] += 2
                $ StormX.change_face("_angry",1)
                ch_s ". . ."
    if StormX.event_happened[6] >= 5:

        jump Storm_Love_Badend

label Storm_Love_Redux:

    ch_s "The closer we get to each other, the less able I feel I am to. . ."
    $ StormX.change_face("_sadside",1)
    ch_s ". . . to pull myself -free- from you."
    menu:
        extend ""
        "Is that what you want?":
            $ StormX.change_stat("love", 200, 1)
            $ StormX.change_face("_surprised",2)
            ch_s "No!"
            $ StormX.change_stat("love", 200, 2)
            $ StormX.change_face("_smile",1,Eyes="_side")
            ch_s ". . . no. . ."
            $ StormX.change_stat("love", 200, 3)
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_stat("inhibition", 80, 2)
            $ StormX.change_face("_smile",1)
            ch_s "I suppose that I do not. . ."
        "Can I do anything?":
            $ StormX.change_stat("love", 200, 5)
            $ StormX.change_stat("inhibition", 80, 4)
            $ StormX.change_face("_smile",1)
            ch_s "I do not believe anything -needs- to be done here."
            ch_s "I am content with this. . ."
        "Yeah, I have that effect on women.":
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_stat("inhibition", 90, 3)
            $ StormX.change_face("_sly",1)
            if not approval_check(StormX, 600, "OI"):
                $ StormX.change_stat("love", 200, -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("_angry",1,Mouth="_smile")
            ch_s "Try to avoid a swelled head, [StormX.player_petname]"
        "Cool!":
            $ StormX.change_stat("love", 200, -5)
            $ StormX.event_happened[6] += 2
            $ StormX.change_face("_angry",1)
            ch_s "I am glad you are enjoying my struggles."
        "Ok.":
            $ StormX.change_stat("love", 200, -2)
            $ StormX.change_face("_bemused",1)
            if not approval_check(StormX, 800, "OI"):
                $ StormX.change_stat("love", 200, -3)
                $ StormX.event_happened[6] += 1
                $ StormX.change_face("_angry",2)
                ch_s "Is that really the best you can offer here?"
                $ StormX.blushing = ""
            ch_s "Why do I put up with you?"

    if StormX.event_happened[6] >= 5:

        jump Storm_Love_Badend

    ch_s "I suppose I just need to accept the truth. . ."
    $ StormX.change_face("_smile",1)
    ch_s "I love you, beloved."
    $ StormX.player_petnames.append("lover")
    menu:
        extend ""
        "I love you too!":
            $ StormX.change_stat("love", 200, 10)
            $ StormX.eyes = "_surprised"
            pause .2                    
            $ StormX.eyes = "_normal"
            ch_s "I am glad to hear that."
        "Cool.":
            $ StormX.change_stat("obedience", 80, 2)
            $ StormX.change_stat("inhibition", 80, -2)
            $ StormX.change_face("_confused",1)
            if not approval_check(StormX, 1200):
                $ StormX.change_stat("love", 200, -5)
                $ StormX.event_happened[6] += 1
            ch_s "You have nothing more to add than that?"
        "I wouldn't go that far.":
            $ StormX.change_stat("love", 200, -10)
            $ StormX.change_stat("obedience", 90, 5)
            $ StormX.change_stat("inhibition", 90, -5)
            $ StormX.event_happened[6] += 2
            $ StormX.change_face("_angry",1,Eyes="_side")
            ch_s "No, I suppose you would not."
        "I guess I do too. . .":
            $ StormX.change_stat("obedience", 90, 5)
            $ StormX.change_stat("inhibition", 80, -2)
            $ StormX.change_face("_bemused",1)
            if not approval_check(StormX, 1200):
                $ StormX.change_face("_angry",1)
                $ StormX.event_happened[6] += 1
            ch_s "Please, do not overwhelm me with your affections. . ."
        "Ok.":
            if not approval_check(StormX, 800, "OI"):
                $ StormX.change_face("_angry",1)
                $ StormX.change_stat("love", 200, -2)
                $ StormX.event_happened[6] += 1
            ch_s ". . ."

    if StormX.event_happened[6] >= 6:

        jump Storm_Love_Badend

    if len(Player.Harem) >= 2:
        ch_s "I do not expect to keep you for myself. . ."
        $ StormX.change_face("_smile",1,Eyes="_side")
        ch_s "The others also love you so much. . ."
        ch_s ". . . but the part of you that entraps me is mine."
    $ StormX.change_face("_smile",1)
    ch_s "I am so glad that I found you, beloved."
    menu:
        extend ""
        "I'm glad I found you too.":
            $ StormX.change_stat("love", 200, 5)
            $ StormX.change_stat("obedience", 90, 5)
            $ StormX.change_stat("inhibition", 80, 5)
            $ StormX.player_petname = "beloved"
        "I am too, but about that name. . .":
            $ StormX.change_stat("love", 200, 5)
            $ StormX.change_stat("obedience", 90, 7)
            $ StormX.change_stat("inhibition", 80, 3)
            ch_p "Could you just keep calling me \"[StormX.player_petname]?\""
            ch_s "I suppose that I could. . ."
        "I don't like that name.":
            $ StormX.change_stat("love", 200, 3)
            $ StormX.change_stat("obedience", 80, 10)
            $ StormX.change_stat("inhibition", 80, -2)
            $ StormX.change_face("_bemused",1)
            ch_s "Well, I suppose [StormX.player_petname] does suit you better. . ."
        "Ok.":
            $ StormX.change_stat("obedience", 80, 5)
            $ StormX.change_stat("inhibition", 80, 2)
            $ StormX.change_face("_confused",1)
            ch_s ". . ."
            if not approval_check(StormX, 900, "L"):
                $ StormX.change_stat("love", 200, (901-StormX.love))
            $ StormX.change_face("_smile",1,Eyes="_side")
            ch_s "Ok."
            $ StormX.player_petname = "beloved"

    return

label Storm_Love_Badend:

    $ StormX.change_face("_angry",1)
    ch_s "You know, I do not think you're ready to have this conversation."
    $ StormX.recent_history.append("_angry")
    $ StormX.daily_history.append("_angry")
    call remove_girl (StormX)
    return




label Storm_Sub:
    call shift_focus (StormX)
    $ StormX.drain_word("asked_to_meet")

    $ StormX.location = bg_current
    call set_the_scene
    if StormX.location != bg_current and StormX not in Party:
        "[StormX.name] shows up and says she needs to talk to you."
    else:
        "[StormX.name] approaches you, looking to talk."
    call clear_the_room (StormX)
    call taboo_Level
    $ StormX.daily_history.append("relationship")

    $ StormX.change_face("_sly")
    $ Line = 0
    ch_s "[StormX.player_petname]. . . I have noticed that when we are together. . ."
    ch_s ". . . you tend to. . . assert yourself. . ."
    menu:
        extend ""
        "Do I?":
            $ StormX.change_face("_confused")
            $ StormX.change_stat("obedience", 90, -2)
            ch_s "Yes. . ."
        "Yes, I do.":
            $ StormX.change_stat("obedience", 90, 10)
            $ StormX.change_stat("inhibition", 90, 3)
            $ StormX.change_stat("lust", 70, 5)
            ch_s "I am glad you noticed it too. . ."
        "Ok?":
            $ StormX.change_face("_confused")
            $ StormX.change_stat("obedience", 90, -1)
            ch_s ". . ."
            ch_s ". . . yes, well. . ."
    ch_s "I hope that you have also noticed. . ."
    $ StormX.change_face("_sly")
    ch_s ". . . what effect it has on me when you do. . ."
    menu:
        extend ""
        "You. . . enjoy it?":
            $ StormX.change_stat("obedience", 90, 3)
            $ Line = ". . . yes, I suppose that I do."
        "Does it turn you on?":
            $ StormX.change_face("_bemused",Eyes="_side")
            $ StormX.change_stat("obedience", 90, 2)
            ch_s ". . ."
            $ StormX.change_stat("obedience", 90, 3)
            $ StormX.change_stat("inhibition", 90, 5)
            $ StormX.change_stat("lust", 90, 5)
            $ Line = ". . . yes."
        "Sorry?":
            $ StormX.change_face("_perplexed",2)
            $ StormX.change_stat("obedience", 90, -5)
            $ StormX.change_stat("inhibition", 90, -5)
            ch_s "Oh, you don't need to-"
            ch_s "That is not what I intended. . ."
        "It makes you wet.":
            $ StormX.change_face("_surprised",2)
            $ StormX.change_stat("obedience", 90, 3)
            $ StormX.change_stat("lust", 90, 5)
            $ StormX.change_stat("lust", 60, 5)
            ch_s ". . ."
            $ StormX.change_stat("inhibition", 90, 7)
            $ StormX.change_stat("lust", 70, 5)
            $ StormX.change_face("_bemused",2,Eyes="_side")
            $ Line = ". . .sometimes. . ."
    while Line:
        menu:
            ch_s "[Line]"
            "Cool.":
                $ StormX.change_face("_perplexed",1)
                $ Line = 0
            "Say it again.":
                $ StormX.change_face("_perplexed",Eyes="_side")
                ch_s ". . ."
                if "repeat" not in StormX.recent_history:
                    $ StormX.change_stat("obedience", 90, 5)
                    $ StormX.change_stat("lust", 60, 5)
                    $ StormX.add_word(1,"repeat",0,0,0)
                    $ StormX.change_face("_bemused",2,Eyes="_side")
                else:
                    $ StormX.change_face("_bemused")
                    $ StormX.change_stat("love", 80, 2)
                    $ StormX.change_stat("obedience", 90, -2)
                    ch_s ". . . I think perhaps that is enough for now. . ."
                    menu:
                        "Ok.":
                            $ StormX.change_stat("love", 70, 2)
                            $ StormX.change_stat("obedience", 90, 2)
                        "I'll tell you when it's enough.":
                            $ StormX.change_face("_angry",1)
                            $ StormX.change_stat("love", 90, -5)
                            $ StormX.change_stat("obedience", 90, 2)
                            ch_s "Perhaps you are taking things a bit too far."
                        "Fine, for now.":
                            $ StormX.change_stat("love", 90, 3)
                            $ StormX.change_stat("obedience", 90, 3)
                            $ StormX.change_stat("inhibition", 90, 2)
                            ch_s "Thank you."
                    $ Line = 0
                    $ StormX.change_face("_sly",1)
            "I'm glad.":
                $ Line = 0
                $ StormX.change_face("_bemused",1)
                $ StormX.change_stat("love", 90, 3)
                $ StormX.change_stat("inhibition", 90, 2)
            "It turns me on too.":
                $ Line = 0
                $ StormX.change_face("_sly",1,Mouth="_smile")
                $ StormX.change_stat("love", 90, 2)
                $ StormX.change_stat("obedience", 90, 5)
                $ StormX.change_stat("inhibition", 90, 3)
                $ StormX.change_stat("lust", 90, 5)
    ch_s "In any case. . ."
    ch_s "I was hoping that you might continue to. . . assert yourself in future. . ."
    menu:
        extend ""
        "I guess I could. . .":
            $ StormX.change_face("_sly",1)
            $ StormX.change_stat("love", 90, 2)
            $ StormX.change_stat("obedience", 90, 2)
        "I could do that.":
            $ StormX.change_face("_sly",1)
            $ StormX.change_stat("obedience", 90, 5)
        "I'd don't want to.":
            $ StormX.change_face("_perplexed",1)
            $ StormX.change_stat("love", 80, -5)
            $ StormX.change_stat("obedience", 90, -5)
            $ StormX.change_stat("inhibition", 90, -5)
            ch_s "Oh?"
            $ StormX.change_face("_sadside",1)
            $ StormX.change_stat("obedience", 90, -5)
            ch_s ". . .fine."
            $ StormX.change_stat("obedience", 90, -10)
            ch_s "Perhaps some other time. . ."
            call remove_girl (StormX)
            $ StormX.change_face("_normal",1)
            $ StormX.history.append("sir")
            return
        "Of course.":
            $ StormX.change_face("_sly",1)
            $ StormX.change_stat("obedience", 90, 10)
            $ StormX.change_stat("inhibition", 60, 5)
        "Ok.":
            $ StormX.change_face("_perplexed",1)
            $ StormX.change_stat("obedience", 90, -3)
            ch_s ". . . fine."

    ch_s "and perhaps I could refer to you as. . . sir?"
    $ StormX.player_petnames.append("sir")
    menu:
        extend ""
        "If you want?":
            $ StormX.change_face("_perplexed",1,Eyes="_side")
            $ StormX.change_stat("love", 80, 3)
            ch_s ". . . right. . ."
            $ StormX.change_stat("inhibition", 90, -2)
            ch_s ". . ."
            $ StormX.change_stat("obedience", 90, -5)
            ch_s "I am unsure you got the correct message here. . ."
            ch_s ". . ."
            $ StormX.change_face("_normal",1)
            ch_s "Whatever. . ."
            $ StormX.player_petname = "sir"
        "You may.":
            $ StormX.change_face("_sly",1)
            $ StormX.player_petname = "sir"
            $ StormX.change_stat("love", 90, 5)
            $ StormX.change_stat("obedience", 90, 10)
            $ StormX.change_stat("inhibition", 90, 5)
        "I'd rather you keep calling me [StormX.player_petname].":
            $ StormX.change_face("_sly",1)
            $ StormX.change_stat("obedience", 90, 15)
            $ StormX.change_stat("inhibition", 90, 3)
            ch_s "Very well. . ."
        "I'd rather you call me [Player.name]." if StormX.player_petname != Player.name:
            $ StormX.change_face("_sly",1)
            $ StormX.change_stat("obedience", 90, 15)
            $ StormX.change_stat("inhibition", 90, 3)
            ch_s "Very well. . ."
        "Ok.":
            $ StormX.change_face("_confused",1)
            $ StormX.change_stat("obedience", 90, 5)
            ch_s ". . . right. . ."
            $ StormX.change_face("_normal",1)
            $ StormX.player_petname = "sir"
    ch_s "This should be fun, [StormX.player_petname]. . ."
    return


label Storm_Sub_Asked:
    $ Line = 0
    $ StormX.change_face("_sadside", 1)
    ch_s "I do recall something like that. . ."
    ch_s "You indicated that you were uninterested. . ."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in StormX.player_petnames and approval_check(StormX, 850, "O"):

                pass
            elif approval_check(StormX, 550, "O"):

                pass
            else:
                ch_s "I have changed my mind. . . at least for the time being. . ."
                $ Line = "rude"

            if Line != "rude":
                $ StormX.change_stat("love", 90, 10)
                $ StormX.change_face("_sly", 1)
                ch_s "I appreciate that. . ."
                ch_s "Fine, we can give it another try."
        "I get it now.":
            if "sir" in StormX.player_petnames and approval_check(StormX, 850, "O"):

                pass
            elif approval_check(StormX, 550, "O"):

                pass
            else:
                ch_s "Well. . ."
                ch_s "I have changed my mind. . . at least for the time being. . ."
                $ Line = "rude"

            if Line != "rude":
                $ StormX.change_stat("obedience", 200, 10)
                ch_s ". . ."
                $ StormX.change_face("_sly",1)
                ch_s "We will see."
        "You know you want it.":
            if "sir" in StormX.player_petnames and approval_check(StormX, 850, "O"):

                pass
            elif approval_check(StormX, 550, "O"):

                pass
            else:
                $ StormX.change_face("_sly",1)
                $ StormX.change_stat("love", 200, 5)
                $ StormX.change_stat("obedience", 90, 5)
                ch_s ". . . ye-"
                $ StormX.change_face("_angry",1,Eyes="_side")
                $ StormX.change_stat("obedience", 90, -3)
                $ StormX.change_stat("inhibition", 90, 5)
                ch_s "-no. . ."
                ch_s "I have changed my mind. . . at least for the time being. . ."
                $ Line = "rude"

            if Line != "rude":
                $ StormX.change_stat("love", 200, 5)
                $ StormX.change_stat("obedience", 200, 10)
                $ StormX.change_stat("inhibition", 90, 5)
                $ StormX.change_stat("lust", 90, 5)
                ch_s ". . ."
                $ StormX.change_face("_sly",1)
                ch_s ". . . yes. I do want it."

    $ StormX.recent_history.append("asked sub")
    $ StormX.daily_history.append("asked sub")
    if Line == "rude":

        hide Storm_Sprite with easeoutright
        call remove_girl (StormX)
        $ StormX.recent_history.append("_angry")
        $ renpy.pop_call()
        "[StormX.name] marches out the door, leaving you alone. She looked pretty upset."
    elif "sir" in StormX.player_petnames:

        $ StormX.change_stat("obedience", 200, 30)
        $ StormX.player_petnames.append("master")
        $ StormX.player_petname = "master"
        $ StormX.eyes = "_sly"
        ch_s ". . . master. . ."
    else:

        $ StormX.change_stat("obedience", 200, 30)
        $ StormX.player_petnames.append("sir")
        $ StormX.player_petname = "sir"
        $ StormX.eyes = "_sly"
        ch_s ". . . sir."
    return






label Storm_Master:
    $ StormX.drain_word("asked_to_meet")
    call shift_focus (StormX)
    $ StormX.location = bg_current
    call set_the_scene
    if StormX.location != bg_current and StormX not in Party:
        "[StormX.name] shows up and says she needs to talk to you."
    else:
        "[StormX.name] approaches you, looking to talk."
    call clear_the_room (StormX)
    $ StormX.daily_history.append("relationship")
    call taboo_Level
    $ Line = 0
    $ Options = all_Girls[:]
    while Options:

        if "master" == Options[0].player_petname:
            $ Line = 2
        elif "master" in Options[0].player_petnames:
            $ Line = 1 if not Line else Line
        $ Options.remove(Options[0])
    $ StormX.change_face("_bemused", 1)
    if Line:

        ch_s "I have heard some talk among the other girls. . ."
        if Line == 2:

            ch_s "Apparently you have been having some of them calling you. . . "
            $ StormX.change_face("_sly", 1)
            ch_s "\"Master?\""
        else:

            ch_s "Apparently some have considered calling you. . . "
            $ StormX.change_face("_sly", 1)
            ch_s "\"Master?\""
    else:

        ch_s "I have been thinking lately. . ."
        ch_s "Do you enjoy. . . dominating those around you?"
        ch_s "Do you enjoy hearing a woman call you. . ."
        $ StormX.change_face("_sly", 1)
        ch_s "\"Master?\""
    menu:
        extend ""
        "I don't know, it can be fun.":
            $ StormX.change_stat("obedience", 200, 2)
            $ StormX.change_stat("inhibition", 90, 2)
            ch_s ". . ."
            $ StormX.change_face("_bemused", 1)
            ch_s "I can imagine. . ."
        "I don't really encourage it.":
            $ StormX.change_face("_confused", 1)
            $ StormX.change_stat("obedience", 200, -2)
            $ StormX.change_stat("inhibition", 90, -2)
            if Line == 2:
                ch_s "Really? . ."
                $ StormX.change_face("_sly", 1)
                $ StormX.change_stat("love", 90, -5)
                ch_s "That is not what I have heard. . ."
            else:
                ch_s "Hmmm. . . that is not the answer I was expecting. . ."
        "Yes. I like it.":

            $ StormX.change_face("_sly", 1)
            $ StormX.change_stat("love", 90, 2)
            $ StormX.change_stat("obedience", 200, 5)
            $ StormX.change_stat("inhibition", 90, 3)
            ch_s "I expected that you might. . ."
        "What about you?":
            $ StormX.change_face("_sly", 1,Eyes="_side")
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("obedience", 200, 2)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 90, 2)
            ch_s "I do not know. . ."
            $ StormX.add_word(1,"aboutyou",0,0,0)
        "Nope.":
            $ StormX.change_face("_confused", 1)
            $ StormX.change_stat("obedience", 200, -5)
            $ StormX.change_stat("inhibition", 90, -2)
            if Line:
                $ StormX.change_stat("love", 90, -5)
                ch_s "You don't need to hide such things from me. . ."
            else:
                ch_s "Hmmm. . . that is not the answer I was expecting. . ."


    menu:
        extend ""
        "So you -would- enjoy it.":
            $ StormX.change_face("_bemused", 1)
            $ StormX.change_stat("love", 90, 3)
            $ StormX.change_stat("obedience", 200, 5)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 90, 2)
        "Would you enjoy that?" if "aboutyou" not in StormX.recent_history:
            $ StormX.change_face("_sly", 1,Eyes="_side")
            $ StormX.change_stat("love", 90, 1)
            $ StormX.change_stat("obedience", 200, 2)
            $ StormX.change_stat("inhibition", 70, 3)
            $ StormX.change_stat("inhibition", 90, 2)
            ch_s "I do not know. . ."
        "You wouldn't enjoy it, would you?":
            $ StormX.change_face("_surprised", 1)
            $ StormX.change_stat("love", 90, -2)
            $ StormX.change_stat("obedience", 200, -2)
            ch_s "Oh, you wound me. . ."
            $ StormX.change_face("_sly", 1,Eyes="_side")
            ch_s "Perhaps you assume too much. . ."
        "You want to call me \"Master,\" don't you.":
            $ StormX.change_face("_sly", 1,Eyes="_side")
            $ StormX.change_stat("obedience", 200, 5)
            $ StormX.change_stat("inhibition", 90, 2)
            $ StormX.change_stat("lust", 80, 5)
            ch_s "Well. . ."
        "Yeah?":
            $ StormX.change_face("_sly", 1,Eyes="_side")
            $ StormX.change_stat("love", 90, -3)
            $ StormX.change_stat("obedience", 200, -3)
            ch_s "Hmm. . ."
            ch_s "Perhaps you should ask me. . ."
    $ StormX.change_face("_sly", 1)
    ch_s "I might. . ."
    $ Line = 1
    while Line:
        menu:
            extend ""
            "Call me \"Master.\"" if "master" not in StormX.player_petnames:
                $ StormX.change_face("_surprised", 2)
                $ StormX.change_stat("obedience", 200, 10)
                $ StormX.change_stat("lust", 70, 5)
                ch_s "Oh. . ."
                $ StormX.change_face("_sly", 1)
                $ StormX.change_stat("obedience", 200, 5)
                ch_s "I can do that. . ."
                $ StormX.change_stat("obedience", 200, 10)
                $ StormX.change_stat("inhibition", 90, 3)
                $ StormX.change_stat("lust", 90, 5)
                ch_s "Master."
                $ StormX.player_petnames.append("master")
            "What do you want to call me?" if "master" not in StormX.player_petnames:
                $ StormX.change_face("_sly", 1,Eyes="_side")
                $ StormX.change_stat("love", 90, 3)
                $ StormX.change_stat("obedience", 200, 7)
                $ StormX.change_stat("lust", 70, 5)
                ch_s "Hmmm. . ."
                $ StormX.change_stat("obedience", 200, 3)
                ch_s "I was considering calling you. . ."
                $ StormX.change_face("_sly", 1)
                $ StormX.change_stat("obedience", 200, 10)
                $ StormX.change_stat("inhibition", 90, 5)
                $ StormX.change_stat("lust", 90, 5)
                ch_s ". . . Master."
                $ StormX.player_petnames.append("master")
            "Say it." if "master" not in StormX.player_petnames:
                $ StormX.change_stat("obedience", 200, 12)
                $ StormX.change_stat("lust", 90, 5)
                ch_s ". . ."
                $ StormX.change_face("_sly", 1,Eyes="_side")
                $ StormX.change_stat("obedience", 200, 7)
                $ StormX.change_stat("lust", 94, 5)
                ch_s ". . ."
                $ StormX.change_face("_sly", 1)
                $ StormX.change_stat("obedience", 200, 10)
                $ StormX.change_stat("inhibition", 90, 3)
                $ StormX.change_stat("lust", 200, 5)
                ch_s "Master."
                $ StormX.player_petnames.append("master")
            "Say it again." if "master" in StormX.player_petnames and Line < 3:
                if Line < 2:
                    $ StormX.change_stat("obedience", 200, 2)
                    $ StormX.change_stat("inhibition", 80, 2)
                    $ StormX.change_face("_sly", 2,Eyes="_side")
                    ch_s ". . ."
                    $ StormX.change_stat("lust", 200, 5)
                else:
                    $ StormX.change_face("_smile", 1)
                    $ StormX.change_stat("love", 90, 3)
                    $ StormX.change_stat("inhibition", 80, 3)
                    ch_s "Alright, that is perhaps a bit much. . ."
                $ StormX.change_face("_sly", 2,Eyes="_side")
                ch_s "Master."
                $ Line += 1
            "Yes, call me that from now on." if "master" in StormX.player_petnames:
                $ StormX.change_face("_sly", 1)
                $ StormX.change_stat("obedience", 200, 5)
                $ StormX.change_stat("inhibition", 90, 2)
                ch_s "Of course. . . Master"
                $ StormX.player_petname = "master"
                $ Line = 0
            "But I'd prefer you stick to [StormX.player_petname]." if "master" in StormX.player_petnames:
                $ StormX.change_face("_sad", 1)
                $ StormX.change_stat("love", 90, 3)
                $ StormX.change_stat("obedience", 200, 3)
                ch_s "I suppose that I can. . . [StormX.player_petname]"
                $ Line = 0
            "I don't know if I would be comfortable with that. . ." if "context" not in StormX.recent_history and "master" not in StormX.player_petnames:
                $ StormX.change_stat("love", 90, 2)
                $ StormX.change_stat("obedience", 200, -3)
                $ StormX.change_stat("inhibition", 90, -2)
                $ Line = "context"
            "I can't ask you to call me that." if "context" not in StormX.recent_history and "master" not in StormX.player_petnames:
                $ StormX.change_stat("obedience", 200, -5)
                $ StormX.change_stat("inhibition", 90, -3)
                $ Line = "context"
            "I still would rather not have you call me that." if "context" in StormX.recent_history and "master" not in StormX.player_petnames:
                $ StormX.change_face("_sad", 1,Mouth="_smile")
                $ StormX.change_stat("love", 90, 5)
                $ StormX.change_stat("obedience", 200, 5)
                ch_s "I can understand that."
                $ StormX.change_face("_smile", 1)
                ch_s "Consider it forgotten."
                ch_s ". . ."
                $ StormX.change_face("_sly", 1)
                ch_s "Though if you change your mind. . ."
                $ Line = 0


        if Line == "context":

            $ StormX.change_face("_surprised", 2)
            ch_s "Oh."
            $ StormX.change_face("_sad", 1)
            ch_s "I am of course aware that there is some. . ."
            $ StormX.change_face("_sadside", 1)
            ch_s ". . . historical baggage associated with that term."
            ch_s "I cannot say that I am entirely immune to the concept. . ."
            ch_s "But I do not think that it would bother me."
            $ StormX.change_stat("obedience", 200, 2)
            $ StormX.change_stat("inhibition", 90, 2)
            $ StormX.change_stat("lust", 90, 2)
            ch_s ". . . if it were you. . ."
            $ StormX.change_face("_sly", 1)
            $ StormX.add_word(1,"context",0,0,0)
            $ Line = 1

    $ StormX.change_face("_sly", 1)
    $ StormX.history.append("master")
    $ Line = 0
    return






label Storm_Sexfriend:
    "You get a text from [StormX.name]."
    "Drop by the pool tonight. . ."
    $ Player.add_word(1,0,0,0,"poolnight")
    $ StormX.daily_history.append("relationship")
    $ StormX.event_happened[9] = 1
    return


label Storm_Poolnight:
    call shift_focus (StormX)
    call set_the_scene
    call clear_the_room (StormX, 1, 1)
    $ StormX.location = "bg_pool"
    call ShowPool ([StormX])
    $ taboo = 0
    $ StormX.taboo = 0
    $ StormX.change_face("_sly", 1)
    $ StormX.change_outfit("nude")
    $ StormX.recent_history.append("poolnight")
    if "sexfriend" not in StormX.player_petnames:

        show Storm_Sprite:
            yoffset 200
        "As you enter the pool area, it seems fairly empty, aside from a small ripple across the pool's surface."
        show Storm_Sprite:
            ease 1 yoffset 0
        pause 1
        show Storm_Sprite zorder 50 at Pool_Bob(500)
        "Storm rises from the pool."
        ch_s "Ah, I was hoping you would join me, [StormX.player_petname]. . ."
        if StormX not in Player.Harem and StormX.player_petname not in ("sir","master"):
            ch_s "I know that this is a no-strings attached situation. . ."
            ch_s "That is fine with me."
            $ StormX.change_stat("inhibition", 200, 25)
            ch_s "We can just continue on as. . . sex friends. . ."
            $ StormX.player_petnames.append("sex friend")
    else:
        ch_s "Oh, hello there, [StormX.player_petname]."
    ch_s "Care to join me?"
    menu:
        extend ""
        "Sure":
            $ StormX.change_stat("love", 200, 2)
            $ StormX.change_stat("inhibition", 200, 2)
            "You join her in the pool and swim about for a bit."
            $ StormX.change_stat("lust", 90, 3)
            "You weave closer and closer to each other. . ."
            $ round -= 10 if round >= 10 else round
            "Finally, she pulls you close and whispers in your ear. . ."
            $ StormX.change_stat("lust", 90, 5)
            ch_s "Would you like to get out of the water, and get me soaking wet?"
            "You both climb out of the pool to the sidelines."
        "Couldn't you just come to me?":
            $ StormX.change_stat("obedience", 70, 1)
            $ StormX.change_stat("obedience", 90, 2)
            $ StormX.change_stat("inhibition", 200, 2)
            $ StormX.change_stat("lust", 90, 3)
            ch_s "I could manage that. . ."
            "She climbs out of the pool."
        "Maybe later. [[leave]":
            $ StormX.change_face("_sad", 1)
            $ StormX.change_stat("obedience", 90, 3)
            ch_s "Oh, that is a pity. . ."
            ch_s "Have fun then. . ."
            "You head back to your room."
            $ bg_current = "bg_player"
            jump Misplaced
    hide Storm_Sprite
    hide FullPool
    call set_the_scene (Dress=0)
    $ StormX.change_face("_sly", 1,Eyes="leftside")
    ch_s "Now that you have me, [StormX.player_petname]. . ."
    $ StormX.change_face("_sly", 1)
    ch_s "What do you intend to do with me. . ."
    call Storm_SexMenu
    return







label Storm_Fuckbuddy:
    $ StormX.daily_history.append("relationship")
    $ StormX.location = "bg_classroom"
    $ bg_current = "bg_classroom"
    call clear_the_room (StormX, 1, 1)
    call set_the_scene (Dress=0)
    $ Player.traits.append("locked")
    $ Nearby = []
    call taboo_Level
    $ StormX.change_face("_sly", 1,Eyes="_side")
    $ StormX.change_stat("inhibition", 200, 5)
    "After class, [StormX.name] walks past you, and places a hand on your chest as you head out."
    $ StormX.change_stat("inhibition", 200, 5)
    "She leans back and locks the door."
    $ StormX.change_face("_sly", 1,Eyes="_down")
    $ StormX.change_stat("inhibition", 200, 10)
    ch_s "I do have needs, you know."
    $ StormX.player_petnames.append("fuck buddy")
    $ StormX.event_happened[10] += 1
    $ StormX.change_face("_sly", 1)
    $ StormX.change_stat("inhibition", 200, 10)
    ch_s "Couldn't you help me with that? . . "
    call Storm_SexMenu
    return




label Storm_Daddy:
    $ StormX.daily_history.append("relationship")
    call shift_focus (StormX)
    call set_the_scene
    ch_s ". . ."
    $ Line = 0
    $ Options = all_Girls[:]
    while Options:

        if "daddy" == Options[0].player_petname:
            $ Line = 2
        elif "daddy" in Options[0].player_petnames:
            $ Line = 1 if not Line else Line
        $ Options.remove(Options[0])


    if StormX in Player.Harem:
        ch_s "I have been talking with the other girls. . ."
    else:
        ch_s "I have heard something among the students. . ."
    if Line:
        ch_s "Apparently you have some of them call you. . . \"daddy?\""
    else:
        ch_s "Apparently sometimes the woman in a relationship. . ."
        ch_s ". . . calls her partner. . . \"daddy?\""
    menu:
        extend ""
        "Yes?":
            ch_s "I thought as much. . ."
        "I don't know what you're talking about.":
            ch_s "I think it is just a term of endearment. . ."
            ch_s "Affectionate, but. . . submissive?"
        "Not really.":
            ch_s "Oh. Perhaps I misunderstood."
    $ Line = 1
    $ StormX.player_petnames.append("daddy")
    while Line:
        menu:
            extend ""
            "Did you want me to call you that?" if "callyouthat" not in StormX.recent_history:
                $ StormX.change_stat("love", 70, 1)
                $ StormX.change_stat("inhibition", 90, 2)
                ch_s ". . ."
                $ StormX.change_stat("love", 95, 2)
                $ StormX.change_stat("inhibition", 70, 1)
                ch_s "I suppose that I did. . ."
                $ StormX.recent_history.append("callyouthat")
            "I guess you could. . ." if "callyouthat" in StormX.recent_history or "whycare" in StormX.recent_history:
                $ StormX.change_stat("love", 70, 2)
                $ StormX.change_stat("obedience", 200, 5)
                $ StormX.change_stat("inhibition", 70, 1)
                ch_s ". . ."
                $ StormX.change_stat("love", 200, 5)
                $ StormX.change_stat("inhibition", 90, 3)
                ch_s "Certainly. . . Daddy."
                $ Line = 0
            "Call me \"Daddy.\"":
                $ StormX.change_stat("love", 90, 2)
                $ StormX.change_stat("obedience", 80, 3)
                ch_s ". . ."
                $ StormX.change_stat("obedience", 200, 5)
                $ StormX.change_stat("inhibition", 90, 2)
                $ StormX.change_stat("lust", 90, 3)
                ch_s "Certainly. . . Daddy."
                $ Line = 0
            "Why do you care?" if "whycare" not in StormX.recent_history:
                $ StormX.change_stat("love", 90, 2)
                $ StormX.change_stat("obedience", 80, -1)
                $ StormX.change_stat("inhibition", 90, -1)
                ch_s "Oh, well, I was thinking that I could. . ."
                $ StormX.recent_history.append("whycare")
            "It's weird, right?":
                $ StormX.change_stat("love", 90, -3)
                $ StormX.change_stat("obedience", 90, -5)
                $ StormX.change_stat("inhibition", 90, -15)
                ch_s "Oh. . . "
                ch_s ". . . I suppose that it is."
                ch_s "Never mind. . ."
                call remove_girl (StormX)
                $ Line = 0
            "I'd rather not." if "callyouthat" in StormX.recent_history or "whycare" in StormX.recent_history:
                $ StormX.change_stat("love", 90, -2)
                $ StormX.change_stat("obedience", 90, 3)
                $ StormX.change_stat("inhibition", 90, -5)
                ch_s "Oh. . . "
                ch_s ". . . I suppose that it fine."
                ch_s "Never mind. . ."
                call remove_girl (StormX)
                $ Line = 0
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
