


label meet_Laura(Topics=[], Loop=1):
    $ active_Girls.append(LauraX) if LauraX not in active_Girls else active_Girls
    $ LauraX.name = "???"
    $ LauraX.names.remove("Laura")
    $ LauraX.names.append("X-23")
    $ bg_current = "bg_dangerroom"
    call clear_the_room ("All", 0, 1)
    $ LauraX.location = "bg_dangerroom"
    $ LauraX.love = 400
    $ LauraX.obedience = 0
    $ LauraX.inhibition = 200
    $ LauraX.lust = 10
    call shift_focus (LauraX)
    $ LauraX.sprite_location = stage_center
    call set_the_scene (0)
    $ LauraX.player_petname = Player.name
    $ LauraX.today_outfit = "casual1"
    $ LauraX.outfit = "casual1"
    $ LauraX.change_outfit("casual1")

    "As you approach the Danger Room, you hear a ferocious clanging of metal."
    "Just as you pass through the door, a robotic arm smashes into your face."
    ". . ."
    $ LauraX.change_face("_normal", 0)
    show Laura_Sprite at sprite_location(LauraX.sprite_location)
    "When you come to, a girl pulls you up by your arm."
    $ LauraX.change_face("_surprised", 0, Eyes="_squint",Brows="_sad")
    ch_u "Oh, good, you don't look too damaged."
    $ LauraX.change_face("_smile", 0, Brows="_sad")
    ch_u "Sorry about that, I was getting a work-out in, and must have forgotten to lock the door."
    $ LauraX.change_face("_smile", 0)
    while Loop:
        menu:
            extend ""
            "Who are you?" if LauraX.name == "???":
                $ LauraX.change_face("_normal", 0)
                ch_l "I go by \"X-23\" in the field."
                $ LauraX.name = "X-23"
            "X-23? Is that your real name?" if LauraX.name == "X-23" and "X23" not in Topics:
                $ LauraX.change_face("_confused", 0)
                ch_l "It's the one I was born with."
                $ Topics.append("X23")
            "Is there anything else I could call you?" if "X23" in Topics and LauraX not in Topics:
                $ LauraX.change_stat("love", 70, 5)
                $ LauraX.change_face("_normal", 0)
                ch_l "I also go by Laura. Laura Kinney."
                $ LauraX.change_face("_confused", 0, Mouth="_normal")
                $ LauraX.name = "Laura"
                $ LauraX.names.append("Laura")
                $ Topics.append(LauraX)
                menu:
                    extend ""
                    "Nice to meet you Laura.":
                        $ LauraX.change_stat("love", 70, 5)
                        $ LauraX.change_face("_normal", 0)
                        ch_l "Yeah, ok."
                    "Hello Laura Laura Kinney.":
                        $ LauraX.change_face("_confused", 0,Mouth="_sucking")
                        ch_l "It's just-"
                        $ LauraX.change_face("_smile", 0,Brows="_surprised")
                        $ LauraX.change_stat("love", 70, 3)
                        $ LauraX.change_stat("inhibition", 70, 2)
                        ch_l "Oh, get it."
                    "Ok, how did you get that name?":
                        $ LauraX.change_face("_angry", 1,Eyes="_side")
                        $ LauraX.change_stat("love", 70, -2)
                        $ LauraX.change_stat("obedience", 70, 2)
                        ch_l "You're getting too personal."
            "I think I'd prefer calling you X-23." if LauraX.name == LauraX and LauraX in Topics:
                $ LauraX.change_stat("love", 70, -2)
                $ LauraX.change_stat("obedience", 70, 5)
                $ LauraX.change_face("_sadside", 0,Brows="_normal")
                ch_l "Suit yourself."
                $ LauraX.name = "X-23"
            "My name is [Player.name]" if LauraX.name != "???" and "player" not in Topics:
                $ LauraX.change_face("_normal", 0)
                ch_l "Ok."
                $ Topics.append("player")
                menu:
                    extend ""
                    ". . .and it's nice to meet you?":
                        $ LauraX.change_stat("love", 70, 1)
                        $ LauraX.change_face("_confused", 0,Mouth="_normal")
                        ch_l "Yeah, you too."
                    "So. . .[[moving on]":
                        $ LauraX.change_stat("love", 70, 3)
                        $ LauraX.change_stat("obedience", 70, 1)
                        $ LauraX.change_stat("inhibition", 70, 1)

            "What are you doing here?" if "Training" not in Topics:
                $ LauraX.change_stat("obedience", 70, -2)
                $ LauraX.change_face("_confused", 0)
                ch_l "Training. That's the point of this place."
                $ Topics.append("Training")
                menu:
                    extend ""
                    "I meant in the school, I haven't seen you around before.":
                        $ LauraX.change_stat("obedience", 70, 2)
                    "Ok, that's fair.":
                        $ LauraX.change_face("_normal", 0)
                        ch_p "But are you new to this school?"
                        $ LauraX.change_stat("love", 70, 3)
                        $ LauraX.change_stat("obedience", 70, 4)
                ch_l "I've been here since before your time."
                ch_l "Mostly out in the field though."
            "So you don't stay here long?" if "Training" in Topics and "Stay" not in Topics:
                $ LauraX.change_stat("love", 70, 2)
                $ LauraX.change_face("_normal", 0,Eyes="_side")
                ch_l "I'll be heading out again soon."
                $ LauraX.change_face("_normal", 0)
                ch_l "But I am planning to stick around after I get back from this mission."
                $ Topics.append("Stay")


            "What the hell was that?" if len(Topics) <= 1 and "WTF" not in Topics:
                $ LauraX.change_stat("love", 70, -2)
                $ LauraX.change_stat("obedience", 70, 8)
                $ LauraX.change_face("_confused", 0)
                ch_l "It was a robot arm."
                $ LauraX.change_face("_sad", 1,Eyes="leftside")
                ch_l "Like I said, sorry."
                $ LauraX.change_stat("obedience", 70, -3)
                $ LauraX.change_stat("inhibition", 70, 3)
                $ LauraX.change_face("_smile", 0,Brows="_confused")
                ch_l "You probably should have ducked though."
                $ Topics.append("WTF")

            "So what's your mutant power?" if LauraX.name != "???" and "claws" not in Topics:
                $ LauraX.change_stat("love", 70, 1)
                $ LauraX.change_stat("obedience", 70, 1)
                $ LauraX.change_face("_normal", 0)
                ch_l "I can heal fast."
                $ LauraX.ArmPose = 2
                ch_l "Also I have claws."
                $ LauraX.Claws = 1
                $ LauraX.change_face("_smile", 0,Brows="_confused")
                "snikt"
                $ Topics.append("claws")
                menu:
                    "Those claws look pretty sharp.":
                        $ LauraX.change_stat("inhibition", 70, 3)
                        ch_l "Yeah, indestructible too."
                    "Cool.":
                        $ LauraX.change_stat("love", 70, 3)
                        $ LauraX.change_stat("obedience", 70, 2)
                        $ LauraX.change_stat("inhibition", 70, 1)
                        $ LauraX.change_face("_smile", 0,Brows="_surprised")
                        ch_l "Yeah, indestructible too."
                    "Ouch.":
                        $ LauraX.Claws = 0
                        $ LauraX.change_face("_confused", 0)
                        $ LauraX.change_stat("love", 70, -2)
                        $ LauraX.change_stat("obedience", 70, -5)
                        ch_l "Don't worry, I won't stab you."
                        $ LauraX.change_face("_confused", 0,Mouth="_normal")
                        $ LauraX.change_stat("inhibition", 70, 7)
                        ch_l "Probably."
                $ LauraX.Claws = 0
                $ LauraX.ArmPose = 1

            "Don't you want to know my power?" if "claws" in Topics and "powers" not in Topics:
                if LauraX.love >= 405:
                    $ LauraX.change_face("_smile", 0,Brows="_confused")
                    ch_l "Yeah, I guess."
                else:
                    $ LauraX.change_face("_normal", 0)
                    ch_l "Not really."
                $ LauraX.change_stat("inhibition", 70, 3)
                $ Topics.append("powers")
                ch_p "I'm immune to mutant powers and can shut them off."
                $ LauraX.change_face("_smile", 0,Brows="_confused")
                $ LauraX.change_stat("love", 70, 3)
                $ LauraX.change_stat("obedience", 70, 3)
                ch_l "Huh. Interesting. So you can stop me from healing?"
                ch_p "Yeah. If I touch you, temporarily."
                $ LauraX.change_stat("obedience", 70, 2)
                $ LauraX.change_stat("lust", 70, 3)
                ch_l "Give it a try."
                "She holds out her arm, and you grab it."
                $ LauraX.change_stat("love", 70, 1)
                $ LauraX.change_stat("obedience", 70, 2)
                $ LauraX.change_stat("lust", 70, 5)
                $ LauraX.change_face("_confused", 0)
                ch_l "Huh."
                $ LauraX.change_face("_sexy", 1,Eyes="_closed")
                $ LauraX.addiction_rate += 1
                "You can feel her shudder a little."
                $ LauraX.change_face("_sexy", 1)
                $ LauraX.change_stat("love", 70, 1)
                $ LauraX.change_stat("obedience", 70, 3)
                $ LauraX.change_stat("lust", 70, 5)
                $ LauraX.addiction_rate += 1
                ch_l "That feels weird."
                $ LauraX.change_face("_sexy", 1,Eyes="leftside")
                $ LauraX.change_stat("obedience", 70, 1)
                $ LauraX.change_stat("lust", 70, 3)
                $ LauraX.addiction_rate += 1
                ch_l "-a little more \"alive\" than usual."
                $ LauraX.change_stat("inhibition", 70, 5)
                $ LauraX.change_stat("lust", 70, 5)
                $ LauraX.change_face("_sexy", 1,Brows="_confused")
                $ LauraX.addiction_rate += 1
                ch_l "Almost. . . dangerous."

            "Never mind that. . . [[moving on]" if LauraX.name != "???":
                $ Loop = 0

        if len(Topics) >= 3 and LauraX.name == "???":
            $ LauraX.change_stat("love", 70, -2)
            $ LauraX.change_stat("obedience", 70, 5)
            $ LauraX.change_stat("inhibition", 70, 5)
            ch_l "Oh, by the way, you can call me \"X-23\"."
            $ LauraX.name = "X-23"
        if len(Topics) >= 8:
            $ Loop = 0



    ch_l "Ok, I've got a plane to catch."
    if "player" in Topics:
        $ LauraX.change_stat("love", 70, 2)
        $ LauraX.change_stat("lust", 70, 1)
        $ LauraX.change_face("_smile",0)
        ch_l "Maybe I'll see you when I get back, [Player.name]."
    else:
        $ LauraX.change_face("_normal", 0)
        ch_l "Maybe I'll see you when I get back, stranger."
    if "powers" in Topics:
        $ LauraX.change_stat("obedience", 70, 2)
        $ LauraX.change_stat("inhibition", 70, 2)
        $ LauraX.change_stat("lust", 70, 3)
        $ LauraX.change_face("_smile", 1, Brows="_confused")
        ch_l "We should. . . spar."

    $ LauraX.location = "hold"
    call set_the_scene

    "She dashes out of the room, headed for the hangar."

    $ LauraX.pubes_counter = 3
    $ LauraX.to_do.append("mission")

    $ bg_current = "bg_dangerroom"
    $ round -= 10
    call shift_focus (RogueX)
    $ active_Girls.remove(LauraX) if LauraX in active_Girls else active_Girls

    return




label Laura_Key:
    call set_the_scene
    $ LauraX.change_face("_bemused")
    ch_l "Hey, so. . . this isn't something I usually do but. . ."
    ch_l "Look, you've been sleeping over a lot and I was thinking. . ."
    ch_l "Just take it already."
    "She takes your hand and practically forces a key onto your palm before making your fingers close on it."
    $ Keys.append(LauraX)
    $ LauraX.Event[0] = 1
    ch_p "Thanks."
    return






label Laura_BF(temp_Girls=[]):
    call shift_focus (LauraX)
    if LauraX.location != bg_current:
        $ LauraX.location = bg_current
        if LauraX not in Party:
            "[LauraX.name] approaches you and motions that she wants to speak to you alone."
        else:
            "[LauraX.name] turns towards you and motions that she wants to speak to you alone."
    $ LauraX.drain_word("asked_to_meet")
    call set_the_scene (0)
    call show_girl (LauraX)
    "She looks a bit concerned and you can tell she's a bit anxious about whatever she has to say."
    call Taboo_Level
    call clear_the_room (LauraX)
    $ LauraX.daily_history.append("relationship")
    $ LauraX.change_face("_angry",1,Eyes="_side")
    $ Line = 0
    ch_l "Hey. So. [LauraX.player_petname]. . ."
    $ LauraX.change_face("_confused",1,Mouth="_lipbite")
    ch_l "I don't know- . . . you're pretty fun to hang out with, ya know?"
    menu:
        extend ""
        "I really love hanging out with you too!":
            $ LauraX.change_face("_surprised",2)
            ch_l "Right, so-"
            $ LauraX.change_stat("obedience", 50, -3)
            $ LauraX.change_stat("inhibition", 80, 1)
            ch_l ". . ."
            $ LauraX.change_stat("love", 200, 5)
            $ LauraX.change_face("_bemused",1,Eyes="_side")
            ch_l "\"Love\" is kind of a strong word, [LauraX.player_petname]."
        "Yeah, sure, it's a lot of fun.":
            $ LauraX.change_stat("love", 200, 10)
            $ LauraX.change_stat("inhibition", 80, 2)
            $ LauraX.change_face("_smile",0)
            ch_l "Right?"
        "I mean, it beats math class. . .":
            $ LauraX.change_stat("love", 200, 3)
            $ LauraX.change_stat("obedience", 80, 3)
            $ LauraX.change_stat("inhibition", 80, -3)
            $ LauraX.change_face("_angry",1)
            ch_l "Um, less enthusiasm than I was expecting. . ."
        "If you say so.":
            $ LauraX.change_stat("obedience", 80, 6)
            $ LauraX.change_stat("inhibition", 80, -8)
            $ LauraX.change_face("_confused",1)
            ch_l ". . ."

    ch_l "So like I was saying, I don't exactly have a ton of friends."
    $ LauraX.change_face("_sadside",1)
    ch_l "I kind of grew up in a rough place, and then spent a lot of time on the road."
    ch_l "I had a life before coming here."
    menu:
        extend ""
        "What was it like?":
            $ LauraX.change_stat("love", 200, 7)
            $ LauraX.change_stat("obedience", 80, 2)
            $ LauraX.change_stat("inhibition", 80, 3)
            $ LauraX.change_face("_sad",1,Mouth="_lipbite")
        "Yeah? I know.":
            $ LauraX.change_stat("love", 200, 3)
            $ LauraX.change_stat("obedience", 80, 4)
            $ LauraX.change_stat("inhibition", 80, 1)
            $ LauraX.change_face("_confused",1,Mouth="_lipbite")
        "I don't need a lot of backstory drama.":
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 80, 10)
            $ LauraX.change_stat("inhibition", 80, -5)
            $ LauraX.change_face("_angry",1)
            $ Line = "bad"
            ch_l "Fine!"
            ch_l "\"Keep it simple\" it is then."
            ch_l "I don't hate hanging out with you, is all."
    if Line != "bad":
        $ LauraX.change_face("_normal",1,Eyes="_side")
        ch_l "Well, you may have guessed I'm related to Wolverine."
        menu:
            extend ""
            "Kinda obvious, yeah.":
                $ LauraX.change_stat("love", 200, 4)
            "I had no idea!":
                $ LauraX.change_stat("love", 200, 3)
                $ LauraX.change_stat("inhibition", 80, 1)
                $ LauraX.change_face("_confused",1)
            "Duh.":
                $ LauraX.change_stat("love", 200, 1)
                $ LauraX.change_stat("obedience", 80, 2)
                $ LauraX.change_face("_angry",1)
        ch_l "Well I'm actually his partial clone."
        $ LauraX.change_face("_angry",1,Eyes="_side")
        ch_l "I was created to be some sort of biological weapon, an assassin."
        ch_l "I did a lot of work for them as a kid, until eventually I escaped."
        $ LauraX.change_face("_sadside",1)
        ch_l "After that, I had to do a lot of stuff. . . to stay alive."
        ch_l "Stuff I'm not proud of."
        $ LauraX.change_face("_sad",1)
        ch_l "But I don't know. . . being around you, I think it helps."
        $ LauraX.change_face("_sad",1,Mouth="_smile")
        ch_l "I kind of feel. . . better."
    if LauraX.SEXP >= 20:
        $ LauraX.change_stat("obedience", 80, 3)
        $ LauraX.change_stat("inhibition", 80, 2)
        $ LauraX.change_stat("lust", 80, 5)
        $ LauraX.change_face("_sly",1)
        ch_l "You really are good in bed, after all."
    if len(Player.Harem) >= 2:
        ch_l "And I know that you have your share of other girls. . ."
        ch_l ". . . but I'd still like to be a part of your life."
    elif Player.Harem:
        ch_l "And I know you're with someone else. . ."
        ch_l ". . . but I'd still like to be a part of your life."
    else:
        ch_l "I'd just like to be a part of your life."
    $ LauraX.change_face("_sad",1,Mouth="_smile")
    ch_l "That's it."
    $ LauraX.Event[5] += 1
    menu:
        extend ""
        "Yeah! I really love you.":
            $ LauraX.change_stat("love", 200, -3)
            $ LauraX.change_stat("obedience", 80, -3)
            $ LauraX.change_stat("inhibition", 80, 3)
            $ LauraX.change_face("_surprised",1)
            ch_l "Whoa!"
            $ LauraX.change_face("_perplexed")
            ch_l "Maybe cool your jets there, [LauraX.player_petname]."
            $ LauraX.change_face("_smile",Eyes="_side")
            ch_l "I wasn't. . ."
            ch_l "I don't think we're there. . ."
            $ LauraX.change_face("_perplexed",1)
            ch_l "Right?"
            menu:
                extend ""
                "Maybe you aren't.":
                    $ LauraX.change_stat("love", 200, 10)
                    $ LauraX.change_stat("obedience", 80, 5)
                    $ LauraX.change_stat("inhibition", 80, 5)
                    $ LauraX.change_stat("lust", 80, 2)
                    $ LauraX.change_face("_smile",1,Eyes="_side")
                    ch_l "Hehe. . . um."
                "I guess, sure.":
                    $ LauraX.change_stat("love", 200, 6)
                    $ LauraX.change_stat("obedience", 80, 3)
                    $ LauraX.change_stat("inhibition", 80, 2)
                    $ LauraX.change_face("_angry",1,Eyes="_side",Mouth="_lipbite")
                    ch_l "Right, so. . ."
        "Yeah, I think that'd be great.":

            $ LauraX.change_stat("love", 200, 6)
            $ LauraX.change_stat("obedience", 80, 2)
            $ LauraX.change_stat("inhibition", 80, 3)
            $ LauraX.change_face("_smile",1,Eyes="_side")
            ch_l "Cool."
        "Hmm? Ok.":
            $ LauraX.change_stat("love", 80, 3)
            $ LauraX.change_stat("obedience", 80, 5)
            $ LauraX.change_stat("inhibition", 80, 3)
            $ LauraX.change_face("_confused",1,Eyes="_side")
            ch_l "Yeah. . . cool."
        "I'm not really into that.":
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 80, 5)
            $ LauraX.change_stat("inhibition", 80, -5)
            $ LauraX.change_face("_sad",1)
            if len(Player.Harem) >= 2:
                ch_l "Is it because of [Player.Harem[0].name] and the rest?"
            elif Player.Harem:
                ch_l "Is it because of [Player.Harem[0].name]?"
            else:
                ch_l "Why not? What's the deal?"
            menu:
                extend ""
                "Yeah, I don't think she'd understand." if len(Player.Harem) == 1:
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 80, 7)
                    $ LauraX.change_face("_angry",1,Eyes="_side")
                    $ LauraX.GLG(Player.Harem[0],800,-20,1)
                    ch_l "That bitch."
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 80, 7)
                    $ LauraX.change_face("_angry",1,Eyes="_side")
                    call Haremchange_stat (LauraX, 700, -20)
                    ch_l "Bitches."
                "It's. . . complicated.":
                    $ LauraX.change_stat("love", 200, -20)
                    $ LauraX.change_stat("obedience", 80, 8)
                    $ LauraX.change_stat("inhibition", 80, -5)
                    $ LauraX.change_face("_angry",1)
                    ch_l "Complicated. Sure. Whatever."
                    $ LauraX.change_face("_angry",1,Eyes="_side")
                    if len(Player.Harem) >= 2:
                        ch_l "Probably those bitches."
                        call Haremchange_stat (LauraX, 700, -10)
                    elif Player.Harem:
                        ch_l "Probably because of her."
                        $ LauraX.GLG(Player.Harem[0],800,-20,1)
                    $ Line = "no"
                "I'm just not into you like that.":
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_face("_surprised",1)
                    ch_l "Oh."
                    $ LauraX.change_stat("obedience", 80, 10)
                    $ LauraX.change_stat("inhibition", 80, 5)
                    $ LauraX.change_face("_sadside",1)
                    ch_l "Ok, I guess I can respect that."


            $ LauraX.change_face("_sad",1)
            if Line != "no":
                ch_l "We're still cool though."
            ch_l "I should. . . leave."
            "[LauraX.name] wanders off in a bit of a daze."
            $ LauraX.Event[5] = 20
            call remove_girl (LauraX)
            $ Line = 0
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
                    $ LauraX.change_stat("love", 200, 20)
                    $ LauraX.change_stat("obedience", 80, 5)
                    $ LauraX.change_stat("inhibition", 80, 5)
                    $ LauraX.change_face("_surprised",2,Mouth="_smile")
                    ch_l ". . ."
                    $ LauraX.change_face("_smile",1)

                    $ LauraX.Event[5] = 10
                "I'd rather you join us.":
                    $ Line = 0
                    if approval_check(LauraX, 1200):

                        $ temp_Girls = Player.Harem[:]
                        while temp_Girls and Line != "no":

                            if LauraX.GirlLikeCheck(temp_Girls[0]) <= 500:
                                $ Line = "no"
                            $ temp_Girls.remove(temp_Girls[0])
                    else:
                        $ Line = "no"
                    if Line == "no":
                        $ LauraX.change_stat("love", 200, -10)
                        $ LauraX.change_stat("obedience", 80, 10)
                        $ LauraX.change_face("_angry",1)
                        call Haremchange_stat (LauraX, 700, -10)
                        ch_l "Eh, I'll pass."
                    else:
                        $ LauraX.change_stat("love", 200,5)
                        $ LauraX.change_stat("obedience", 80, 15)
                        $ LauraX.change_stat("inhibition", 80, 10)
                        $ LauraX.change_face("_bemused",1)
                        ch_l "Well, I s'pose that wouldn't be so terrible."
                "What? Of course not.":
                    $ LauraX.change_stat("love", 200, -25)
                    $ LauraX.change_stat("obedience", 80, 5)
                    call Haremchange_stat (LauraX, 700, -20)
                    $ LauraX.change_face("_angry",1)
                    ch_l "Well, fine then."
                    $ Line = "no"
            if Line == "no":
                $ LauraX.Event[5] = 20
                call remove_girl (LauraX)
                $ Line = 0
                return



        if len(Player.Harem) >= 2:
            ch_l "And you don't think the others would mind?"
        else:
            ch_l "And you don't think [Player.Harem[0].name] would mind?"
        menu:
            extend ""
            "No, actually they're fine with it." if "LauraYes" in Player.traits:
                $ LauraX.change_stat("love", 200, 5)
                $ LauraX.change_stat("obedience", 80, 10)
                $ LauraX.change_stat("inhibition", 80, 5)
                $ LauraX.change_face("_surprised",1)
                ch_l "Oh, cool."
            "Actually. . . I guess we'll need to work on that one." if "LauraYes" not in Player.traits:
                $ LauraX.change_stat("love", 200, 3)
                $ LauraX.change_stat("obedience", 80, 3)
                $ LauraX.change_stat("inhibition", 80, 1)
                $ LauraX.change_stat("lust", 80, 1)
                $ LauraX.change_face("_confused",1)
                ch_l "Hmm, get back to me, I guess?"
                $ LauraX.Event[5] = 20
                call remove_girl (LauraX)
                $ Line = 0
                return
        call Haremchange_stat (LauraX, 900, 20)


    if "Historia" not in Player.traits:
        $ Player.Harem.append(LauraX)
        if "LauraYes" in Player.traits:
            $ Player.traits.remove("LauraYes")
        $ LauraX.player_petnames.append("boyfriend")
        call Harem_Initiation
    $ LauraX.change_stat("love", 200, 3)
    $ LauraX.change_stat("obedience", 80, 3)
    $ LauraX.change_stat("inhibition", 80, 1)
    $ LauraX.change_stat("lust", 80, 1)
    $ LauraX.change_face("_sly",1)
    ch_l "So, did you have any plans for the next few minutes? . ."
    if "Historia" in Player.traits:
        return True
    $ approval_bonus = 10
    $ Player.add_word(1,"interruption")
    call Laura_SexMenu
    $ approval_bonus = 0

    return

label Laura_Cleanhouse:

    $ LauraX.drain_word("asked_to_meet")
    if "cleanhouse" in LauraX.to_do:
        $ LauraX.to_do.remove("cleanhouse")
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
    call clear_the_room (LauraX)
    call set_the_scene
    call Taboo_Level
    $ LauraX.daily_history.append("relationship")
    $ LauraX.change_stat("love", 200, -20)
    $ LauraX.change_face("_angry",1)
    ch_l "What's the deal, [Player.player_petname]?"
    ch_l "It's been a week already, and you're still dating [Player.Harem[0].name]!"
    if len(Player.Harem) >= 2:
        ch_l "Not to mention the rest of them!"
    menu:
        extend ""
        "Sorry about that, I'm sticking with them":
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 80, 5)
            $ LauraX.change_stat("inhibition", 80, 5)
            $ LauraX.change_face("_angry",2)
            ch_l "You asshole."
            $ LauraX.change_face("_sadside",1)
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
            $ LauraX.blushing = "_blush2"
            show Laura_Sprite with vpunch
            "She clocks you one."
            "That was fair."
            $ LauraX.blushing = "_blush1"

    ch_l "I can't believe you're putting me through this."
    ch_l "Making me choose between you and putting up with this whole arrangement."
    $ Line = 0
    if approval_check(LauraX, 1400) and approval_check(LauraX, 600,"O"):

        pass
    elif approval_check(LauraX, 1200) and approval_check(LauraX, 500,"O"):

        $ temp_Girls = Player.Harem[:]
        while temp_Girls and Line != "no":

            if LauraX.GirlLikeCheck(temp_Girls[0]) <= 400:
                $ Line = "no"
            $ temp_Girls.remove(temp_Girls[0])
    else:
        $ Line = "no"
    if Line == "no":
        $ LauraX.change_stat("love", 200, -10)
        $ LauraX.change_stat("obedience", 80, 10)
        $ LauraX.change_face("_angry",1)
        call Haremchange_stat (LauraX, 700, -15)
        ch_l "No, this is bullshit, never mind."
    else:
        $ LauraX.change_stat("love", 200, 5)
        $ LauraX.change_stat("obedience", 80, 20)
        $ LauraX.change_stat("inhibition", 80, 10)
        $ LauraX.change_face("_angry",1,Eyes="_side")
        ch_l "Ok, fine, whatever. I'm in too."
        if "Historia" not in Player.traits:
            $ Player.Harem.append(LauraX)
            if "LauraYes" in Player.traits:
                $ Player.traits.remove("LauraYes")
            $ LauraX.player_petnames.append("boyfriend")
            call Harem_Initiation
            call Haremchange_stat (LauraX, 900, 20)
            $ LauraX.Event[5] = 20
    return


label Laura_Love(Shipping=[], Shipshape=0, Topics=[], temp_Girls=[]):






    $ LauraX.drain_word("asked_to_meet")
    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(LauraX)
    while temp_Girls:
        if approval_check(temp_Girls[0], 1200, "LO"):
            $ Shipping.append(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])
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
    call clear_the_room (LauraX)
    call set_the_scene
    call Taboo_Level
    $ LauraX.daily_history.append("relationship")
    $ LauraX.change_face("_sad",1)
    ch_l "Hey, so, I like what this is. . ."
    ch_l "-what we have. . ."
    $ LauraX.change_face("_sadside",1)
    ch_l "It's been kind of hard for me to open up to people. . ."
    ch_l "I've been betrayed a lot out there."
    menu:
        extend ""
        "I would never betray you.":
            $ LauraX.change_face("_bemused",1)
            $ LauraX.change_stat("love", 200, 10)
            $ LauraX.change_stat("obedience", 70, 5)
            $ LauraX.change_stat("inhibition", 60, 5)
            ch_l "I. . . know that now."
        "I'm sorry to hear that.":
            $ LauraX.change_face("_sadside",1,Mouth="_smile")
            $ LauraX.change_stat("love", 200, 5)
            $ LauraX.change_stat("obedience", 90, -5)
            $ LauraX.change_stat("inhibition", 60, 10)
            ch_l ". . ."
            $ LauraX.change_face("_smile",1)
            ch_l "Thank you. . ."
        "That must be rough.":
            $ LauraX.change_face("_sadside",1,Mouth="_normal")
            $ LauraX.change_stat("love", 200, 5)
            ch_l ". . ."
            $ LauraX.change_face("_smile",1)
            ch_l "It was. . ."
        "Wow, that sucks.":
            $ LauraX.change_face("_confused",1)
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 90, 10)
            $ LauraX.change_stat("inhibition", 90, -5)
            ch_l ". . ."
            $ LauraX.change_face("_angry",1,Eyes="_side")
            ch_l "Right, so. . ."
    ch_l "I didn't always have it as easy as I've had it here."
    $ LauraX.eyes = "_normal"
    ch_l "I only thought it fair to tell you a little about that history."
    $ Line = 0
    while len(Topics) < 9 and "exit" not in Topics:


        if Line == "facility":
            menu:
                extend ""
                "How many people did you kill?" if "kills" not in Topics:
                    $ LauraX.change_face("_angry",0,Eyes="_side")
                    ch_l "Dozens. Maybe more. At least 13 primary targets."
                    ch_l "Too many \"collaterals.\""
                    $ Topics.append("kills")
                "Did you ever fail a mission?" if "fail" not in Topics:
                    $ LauraX.change_face("_angry",0,Eyes="_side",Brows="_normal")
                    ch_l "Once or twice."
                    ch_l "Sometimes they managed to get away."
                    ch_l "I'm not proud of who I was back then, but even then. . ."
                    $ LauraX.mouth = "_smile"
                    ch_l ". . . a part of me was happy when they did."
                    $ Topics.append("fail")
                "Did anyone take care of you?" if "mother" not in Topics:
                    $ LauraX.change_face("_smile",0)
                    ch_l "My mother, Sarah Kinney."
                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                    $ LauraX.change_face("_sadside",0)
                    ch_l "She tried to help me, until I killed her."
                    $ Topics.append("mother")
                    $ Line = "mother"
                "How did you escape?" if "escape" not in Topics:
                    $ LauraX.change_face("_sadside",0)
                    ch_l "Mother."
                    ch_l "She got me out, found me an escape route."
                    ch_l "It was the last thing she did."
                    $ Topics.append("escape")
                    $ Line = "mother"
                "I'd like to know more about what came after.":
                    $ Line = "NYX"
                "Enough about that though. . .":
                    $ Line = 0



        if Line == "mother":
            menu:
                extend ""
                "Who was your mother?" if "mother" not in Topics:
                    $ LauraX.change_face("_smile",0)
                    ch_l "Her name was Sarah Kinney."
                    ch_l "She's the one who birthed me, and was also one of the scientists that helped create me."
                    $ LauraX.change_face("_sadside",0)
                    ch_l "She tried to help me, until I killed her."
                    $ Topics.append("mother")
                    $ Line = "mother"
                "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:
                    $ LauraX.change_face("_sad",0,Eyes="_surprised")
                    ch_l "I didn't want to, but the primary_action scent made me. . ."
                    $ LauraX.change_face("_sadside",0)
                    if "trigger" in LauraX.history:
                        ch_l "I've mentioned that to you before. . ."
                    else:
                        $ LauraX.history.append("trigger")
                    ch_l ". . . it can make me kill, even if I don't want to."
                    $ Topics.append("killed")
                "It wasn't your fault." if "killed" in Topics:
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_stat("obedience", 70, 5)
                    $ LauraX.change_stat("inhibition", 70, 5)
                    $ LauraX.change_face("_sad",0)
                    ch_l "Not completely, no."
                    $ LauraX.change_face("_sadside",0)
                    ch_l "But my hands aren't clean."
                    $ Line = "facility"
                "That must have been horrible." if "killed" in Topics:
                    $ LauraX.change_face("_sadside",0)
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_stat("obedience", 90, 5)
                    ch_l "It's taken me some time. . ."
                    $ LauraX.change_face("_normal",0)
                    ch_l "but I think I'm ok with it now."
                    $ Line = "facility"
                "Bummer." if "killed" in Topics:
                    $ LauraX.change_face("_angry",1)
                    $ LauraX.change_stat("love", 200, -10)
                    $ LauraX.change_stat("obedience", 90, 5)
                    ch_l "Are you seriously making fun of my mother's death?!"
                    $ Topics.append("exit")
                    $ Line = "_angry"


        if Line == "NYX":
            menu:
                extend ""
                "What did you do for a living?" if "living" not in Topics:
                    $ LauraX.change_face("_sadside",0)
                    ch_l "There wasn't much I could do at the time, I mostly just scrounged for food."
                    ch_l "You can get by on some pretty awful stuff if you have a healing factor."
                    $ LauraX.change_face("_bemused",1,Brows="_sad")
                    ch_l "I also did some. . . shady stuff."
                    $ Topics.append("living")

                "Was it sexual?" if "work" not in Topics and "living" in Topics:
                    $ LauraX.change_face("_sadside",2)
                    $ LauraX.change_stat("obedience", 90, 5)
                    $ LauraX.change_stat("inhibition", 90, 10)
                    ch_l ". . ."
                    $ LauraX.blushing = "_blush1"
                    ch_l "A little."
                    $ Line = "work"
                    $ Topics.append("work")

                "Did you hurt people?" if "work" not in Topics and "living" in Topics:
                    $ LauraX.change_face("_surprised",0,Eyes="_normal")
                    ch_l "No, definitely not."
                    ch_l "After the facility, I just couldn't take that sort of work anymore."
                    $ LauraX.change_face("_bemused",0)
                    ch_l "I avoided hurting anyone."
                    $ LauraX.change_face("_sadside",2)
                    ch_l "It tended to be more. . . sexual work."
                    $ Line = "work"
                    $ Topics.append("work")

                "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:
                    $ LauraX.change_face("_bemused",0)
                    ch_l "Yeah, eventually."
                    ch_l "I'd seen Wolverine on the news, and thought maybe he had some answers."
                    ch_l "He's not around much though."
                    $ Topics.append("xaviers")
                    $ Line = 0
                "Good thing you made it here. [[exit]" if "xaviers" in Topics:
                    $ LauraX.change_face("_smile",0)
                    ch_l "Yeah."
                    $ Line = 0

        if Line == "work":
            $ LauraX.change_face("_sadside",0,Mouth="_normal")
            ch_l "It was mostly the rougher customers."
            ch_l "The ones who couldn't control their tempers."
            $ LauraX.change_face("_angry",0,Mouth="_smile")
            ch_l "Better for the girl who can heal to take the hits, right?"
            menu:
                extend ""
                "That's terrible. I wish I could have protected you.":
                    $ LauraX.change_face("_smile",1)
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_stat("obedience", 90, 5)
                    $ LauraX.change_stat("inhibition", 90, -5)
                    ch_l "Thanks, but I was ok."
                    $ LauraX.change_face("_sadside",0)
                    ch_l "I didn't deserve it, but I felt like I did at the time."
                "You're strong to have made it out of there.":
                    $ LauraX.change_face("_smile",0)
                    $ LauraX.change_stat("love", 200, 5)
                    $ LauraX.change_stat("obedience", 90, 10)
                    $ LauraX.change_stat("inhibition", 90, 5)
                    ch_l "Thanks."
                    ch_l "I didn't really think of it like that. . ."
                    $ LauraX.change_face("_sadside",0)
                    ch_l "I just felt like I'd deserved it."
                    ch_l "But I realized how wrong that was."
                "Yeah, that makes sense.":
                    $ LauraX.change_face("_confused",1)
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 90, 15)
                    $ LauraX.change_stat("inhibition", 90, -5)
                    ch_l "Don't think before you speak, do you?"
                    $ LauraX.change_face("_sadside",0)
                    ch_l "It wasn't right, I just didn't realize it at the time."
            ch_l "Eventually I got past it and decided to get out of there."
            ch_l "Not like they could stop me."
            $ Line = "NYX"

        if not Line:

            menu:
                extend ""
                "What did you do back at the facility?" if "facility" not in Topics:
                    $ LauraX.change_face("_sadside",0)
                    ch_l "After they tested what I could do, they put me to work."
                    ch_l "Mainly, I killed people for them."
                    $ Topics.append("facility")
                    $ Line = "facility"
                "More about that facility. . ." if "facility" in Topics:
                    $ Line = "facility"

                "Where did you go after you escaped?" if "NYX" not in Topics:
                    $ LauraX.change_face("_sadside",0)
                    ch_l "I wandered in the wilderness for weeks."
                    ch_l "Eventually I found my way to New York."
                    ch_l "I lived on the streets for a few years."
                    $ Topics.append("NYX")
                    $ Line = "NYX"
                "More about after the escape. . ." if "NYX" in Topics:
                    $ Line = "NYX"

                "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:
                    $ LauraX.change_face("_smile",0)
                    $ LauraX.change_stat("love", 200, 10)
                    $ LauraX.change_stat("obedience", 90, 3)
                    $ LauraX.change_stat("inhibition", 90, 3)
                    ch_l "Thanks for listening to me ramble."
                    $ Topics.append("exit")
                "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:
                    $ LauraX.change_face("_sadside",0, Mouth="_smile")
                    $ LauraX.change_stat("obedience", 90, 10)
                    ch_l "Yeah, you get the idea."
                    $ Topics.append("exit")
                "I don't really care about that. [[exit]":
                    $ LauraX.change_face("_angry",0)
                    $ LauraX.change_stat("love", 200, -15)
                    $ LauraX.change_stat("obedience", 50, 5)
                    $ LauraX.change_stat("obedience", 90, 10)
                    $ LauraX.change_stat("inhibition", 90, -5)
                    ch_l "Oh, I'm sorry if I was boring you with my life story."
                    $ Line = "_angry"
                    $ Topics.append("exit")



    if Line == "_angry":
        $ LauraX.change_face("_angry",0)
        ch_l "And here I was thinking that I meant something to you."
        ch_l "Well forget that!"
        $ Line = 0
        $ LauraX.Event[6] = 23
        $ LauraX.recent_history.append("_angry")
        $ LauraX.daily_history.append("_angry")
        hide Laura_Sprite with easeoutright
        call remove_girl (LauraX)
        $ LauraX.location = "hold"
        return

    $ LauraX.change_face("_bemused",0,Eyes="_down")
    ch_l "I just thought you should know,"
    $ LauraX.change_face("_smile",2)
    ch_l "I love you."
    menu:
        extend ""
        "I love you too!":
            $ LauraX.change_face("_smile",1)
            $ LauraX.change_stat("love", 200, 20)
            $ LauraX.change_stat("inhibition", 90, 5)
            ch_l "For a second there you had me worried."
            $ LauraX.player_petnames.append("lover")
            jump Laura_Love_End
        "I know.":
            $ LauraX.change_face("_smile",1)
            $ LauraX.change_stat("love", 200, 10)
            $ LauraX.change_stat("obedience", 90, 5)
            $ LauraX.change_stat("inhibition", 90, 10)
            $ LauraX.change_stat("lust", 90, 5)
            ch_l "Smooth one. Seriously though, how about you?"
        "Neat?":
            $ LauraX.change_face("_confused",1)
            $ LauraX.change_stat("obedience", 90, 5)
            ch_l "I'm gonna need a bit more there, [LauraX.player_petname]."
        "Huh.":
            $ LauraX.change_face("_confused",1)
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 90, 10)
            ch_l "I'm not sure how to take that one."


    menu:
        extend ""
        "Oh, I love you too!":
            $ LauraX.change_face("_smile",1)
            $ LauraX.change_stat("love", 200, 15)
            $ LauraX.change_stat("obedience", 90, 5)
            $ LauraX.change_stat("inhibition", 90, 5)
            ch_l "For a second there you had me worried."
            $ LauraX.player_petnames.append("lover")
            jump Laura_Love_End
        "I. . . love you back?":
            $ LauraX.change_face("_confused",1)
            $ LauraX.change_stat("love", 200, 5)
            $ LauraX.change_stat("obedience", 90, 10)
            ch_l "Ok, I'll take it."
            $ LauraX.player_petnames.append("lover")
            jump Laura_Love_End
        "I mean, that's cool and all. . .":
            $ LauraX.change_face("_sadside",1)
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 90, 10)
            $ LauraX.change_stat("inhibition", 90, -5)
            ch_l ". . . but you don't love me back. Got it."
        "That's. . . uncomfortable.":
            $ LauraX.change_face("_angry",1)
            $ LauraX.change_stat("love", 200, -10)
            $ LauraX.change_stat("obedience", 90, 15)
            $ LauraX.change_stat("inhibition", 90, -5)
            ch_l "I don't like where this is heading."

    ch_l "What's your problem?"
    ch_l "Is it someone else?"
    $ Line = 0
    menu:
        extend ""
        "Yes, it's [RogueX.name]." if RogueX in Shipping and Shipshape < 3:
            $ Line = RogueX
        "Yes, it's [KittyX.name]." if KittyX in Shipping and Shipshape < 3:
            $ Line = KittyX
        "Yes, it's [EmmaX.name]." if EmmaX in Shipping and Shipshape < 3:
            $ Line = EmmaX
        "Yes, it's the others" if Shipshape > 1:
            $ LauraX.change_stat("obedience", 90, 15)
            $ LauraX.change_stat("inhibition", 90, 5)
            $ LauraX.change_stat("lust", 90, 5)
            $ LauraX.change_face("_sadside",1)
            ch_l "Well, you do have your pick."
        "There's nobody else.":
            $ LauraX.change_stat("love", 200, -15)
            $ LauraX.change_stat("obedience", 90, 15)
            $ LauraX.change_stat("inhibition", 90, 5)
            $ LauraX.change_face("_sad",1)
            if approval_check(LauraX, 1000, "OI"):
                ch_l "I guess that's something."
            else:
                ch_l ". . ."
        "It's a \"you\" problem.":
            $ LauraX.change_face("_angry")
            $ LauraX.change_stat("love", 200, -25)
            $ LauraX.change_stat("obedience", 90, 15)
            ch_l "You're seriously messing with me?"
            $ LauraX.change_stat("love", 200, -10)
            ch_l "You don't want to see me when I'm angry."
            $ LauraX.recent_history.append("_angry")
            $ LauraX.daily_history.append("_angry")


    if Line:

        if LauraX.GirlLikeCheck(Line) >= 800:
            $ LauraX.change_stat("love", 200, 5)
            $ LauraX.change_stat("obedience", 90, 20)
            $ LauraX.change_stat("inhibition", 90, 5)
            $ LauraX.change_stat("lust", 90, 5)
            $ LauraX.change_face("_sadside",1)
            ch_l "Yeah, I guess she's great."
        else:
            $ LauraX.change_face("_angry",Eyes="_side")
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 90, 20)
            ch_l "Bitch."
            $ LauraX.recent_history.append("_angry")
            $ LauraX.GLG(Line,800,-50,1)
    ch_l "Well, if that's the way you feel about it. . ."
    ch_l "I'll. . . see you later."
    ch_l "This. . . hurt."

label Laura_Love_End:
    if "lover" not in LauraX.player_petnames:
        $ LauraX.Event[6] = 20
        hide Laura_Sprite with easeoutright
        call remove_girl (LauraX)
        $ LauraX.location = "hold"
        return

    $ LauraX.Event[6] = 5
    "[LauraX.name] grabs you in a crushing hug."
    $ LauraX.change_stat("love", 200, 25)
    $ LauraX.change_stat("lust", 90, 5)
    $ LauraX.change_face("_sly",1)
    ch_l "So. . . now that we have some free time. . ."
    $ LauraX.change_stat("lust", 90, 10)

    if not LauraX.action_counter["sex"]:
        $ LauraX.change_face("_bemused",2)
        ch_l "I think I'm ready. . ."
    else:
        ch_l "Would you like to have some fun?"
    $ Player.add_word(1,"interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            $ LauraX.change_stat("inhibition", 30, 20)
            $ LauraX.change_stat("obedience", 70, 10)
            ch_l "Hmm. . ."
            call Laura_SexAct ("sex")
        "I have something else in mind. . .[[choose another activity]":
            $ LauraX.brows = "_confused"
            $ LauraX.change_stat("obedience", 70, 25)
            ch_l "Like what? . ."
            $ approval_bonus = 20
            call Laura_SexMenu
    return

label Laura_Love_Redux:

    $ Line = 0
    $ LauraX.daily_history.append("relationship")

    if LauraX.Event[6] >= 25:

        ch_p "I hope you've forgiven me, I still love you."
        $ LauraX.change_stat("love", 95, 10)
        if approval_check(LauraX, 950, "L"):
            $ Line = "love"
        else:
            $ LauraX.change_face("_angry")
            ch_l "You're still working your way out of the hole, [LauraX.player_petname]."
            $ LauraX.eyes="_side"
            ch_l ". . ."
            $ LauraX.change_face("_angry",Mouth="_lipbite")
            ch_l "But let me hear your pitch."
    elif LauraX.Event[6] >= 23:

        ch_p "I was rude when you opened up to me before."
        $ LauraX.change_stat("love", 95, 10)
        if approval_check(LauraX, 950, "L"):
            ch_l "And. . ."
        else:
            $ LauraX.change_face("_angry")
            ch_l "You're still working your way out of the hole, [LauraX.player_petname]."
            $ LauraX.eyes="_side"
            ch_l ". . ."
            $ LauraX.change_face("_angry",Mouth="_lipbite")
            ch_l "But let me hear your pitch."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ LauraX.change_face("_perplexed",1)
        ch_l ". . ."
        $ LauraX.change_face("_angry", Eyes="_side")
        ch_l "How could I forget?"

    if Line != "love":
        menu:
            extend ""
            "I'm sorry, I didn't mean it.":
                $ LauraX.eyes = "_surprised"
                ch_l "Oh really?"
                ch_l "That's awfully convenient."
                ch_p "Yeah. I mean, yes, I love you, [LauraX.name]."
                $ LauraX.change_stat("love", 200, 10)
                if approval_check(LauraX, 950, "L"):
                    $ Line = "love"
                else:
                    $ LauraX.change_face("_sadside")
                    ch_l "Well, maybe I don't, anymore. . ."
            "I've changed my mind, I do love you, so. . .":
                if approval_check(LauraX, 950, "L"):
                    $ Line = "love"
                    ch_l "Well that's great."
                else:
                    $ LauraX.mouth = "_sad"
                    ch_l "Good for you."
                    $ LauraX.change_stat("inhibition", 90, 10)
                    $ LauraX.change_face("_sadside")
                    ch_l "I don't exactly have the same mind either. . ."
            "Um, never mind.":
                $ LauraX.change_stat("love", 200, -30)
                $ LauraX.change_stat("obedience", 50, 10)
                $ LauraX.change_face("_angry")
                ch_l "Oh, fuck you."
                $ LauraX.recent_history.append("_angry")
                $ LauraX.daily_history.append("_angry")
    if Line == "love":
        $ LauraX.change_stat("love", 200, 40)
        $ LauraX.change_stat("obedience", 90, 10)
        $ LauraX.change_stat("inhibition", 90, 10)
        $ LauraX.change_face("_smile")
        ch_l "I'm glad you came around."
        ch_l "I love you too, [LauraX.player_petname]!"
        if LauraX.Event[6] < 25:
            $ LauraX.change_face("_sly")
            "She grabs the back of your head and pulls you close."
            ch_l "Next time, don't keep me waiting."
        $ LauraX.player_petnames.append("lover")
    $ LauraX.Event[6] = 25
    return






label Laura_Sub:
    $ LauraX.drain_word("asked_to_meet")
    call shift_focus (LauraX)
    if LauraX.location != bg_current and LauraX not in Party:
        "Suddenly, [LauraX.name] shows up and says she needs to talk to you."

    $ LauraX.location = bg_current
    call set_the_scene (0)
    call show_girl (LauraX)
    call clear_the_room (LauraX)
    call set_the_scene
    call Taboo_Level
    $ LauraX.daily_history.append("relationship")
    $ LauraX.change_face("_bemused", 1)

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
    $ LauraX.change_face("_sly", 1,Eyes="_side")
    ch_l "I don't know how I feel about that."
    if LauraX.Event[6]:
        $ LauraX.change_face("_sadside", 1)
        ch_l "You know the past I've had, with the facility, with the. . . "
        ch_l ". . . work I had to do for them."
        $ LauraX.change_face("_sad", 1)
        ch_l "I don't know if I want to let anyone tell me what to do like that again."
    menu Laura_Sub_Question:
        extend ""
        "I guess I can be demanding.":
            $ LauraX.change_face("_sly", 1)
            $ LauraX.change_stat("obedience", 200, 10)
            $ LauraX.change_stat("inhibition", 50, 5)
        "Sorry. I didn't mean to come off like that.":
            $ LauraX.change_face("_sly", 1)
            $ LauraX.change_stat("love", 80, 5)
            $ LauraX.change_stat("obedience", 200, -5)
            $ LauraX.change_stat("inhibition", 50, -5)
            ch_l "I get it, you're assertive. . ."
        "Remind me about the facility?" if LauraX.Event[6] and Line != "facility":
            $ LauraX.change_face("_sadside", 1)
            $ LauraX.change_stat("love", 99, -10)
            $ LauraX.change_stat("inhibition", 50, -5)
            ch_l "I told you, I was raised in an underground government lab."
            ch_l "They ordered me to kill people for them."
            $ LauraX.change_face("_sly", 0, Brows= "_angry")
            ch_l ". . . until I got tired of taking orders."
            $ Line = "facility"
            jump Laura_Sub_Question
        "What bothers you about being told to do things?" if not LauraX.Event[6] and Line != "facility":
            $ LauraX.change_face("_sadside", 1)
            $ LauraX.change_stat("love", 80, 5)
            ch_l "I've just had some rough experiences."
            ch_l "You don't need to know about them."
            ch_l ". . ."
            $ LauraX.change_face("_sad", 0)
            ch_l "Let's just say I was ordered to do some things I regret."
            $ Line = "facility"
            jump Laura_Sub_Question
        "Get with the program.":
            if approval_check(LauraX, 1000, "LO"):
                $ LauraX.change_face("_sly", 1)
                $ LauraX.change_stat("obedience", 200, 20)
                $ LauraX.change_stat("inhibition", 50, 10)
                ch_l "Hmmm. . ."
            else:
                $ LauraX.change_stat("love", 200, -10)
                $ LauraX.change_stat("inhibition", 50, -5)
                $ LauraX.change_face("_angry",0)
                ch_l "You're not off to a good start here. You might want to rethink your attitude."
                menu:
                    extend ""
                    "Sorry. I thought that's what you were into.":
                        $ LauraX.change_face("_perplexed", 1,Eyes="_side")
                        $ LauraX.eyes = "_side"
                        $ LauraX.change_stat("love", 75, 10)
                        $ LauraX.change_stat("obedience", 200, 5)
                        $ LauraX.change_stat("inhibition", 50, 5)
                        ch_l ". . . after I just said. . ."
                        $ LauraX.change_face("_sly", 1)
                        ch_l "Ok, whatever."
                    "I don't care.":
                        $ LauraX.change_stat("love", 95, -10)
                        ch_l "I guess not."
                        $ Line = "rude"
    if Line == "facility":
        $ Line = 0

    if not Line:

        $ LauraX.change_face("_sly", 1)
        ch_l "Look, it's not like. . ."
        $ LauraX.change_face("_sly", 2)
        ch_l ". . . it's not like I hate it."
        $ LauraX.change_face("_smile", 1, Eyes="_side")
        ch_l ". . . I actually think it might make me. . ."
        menu:
            extend ""
            "-excited?":
                $ LauraX.change_stat("obedience", 200, 5)
                $ LauraX.change_stat("inhibition", 50, 5)
                ch_l ". . ."
                $ LauraX.change_face("_sly", 1)
                $ LauraX.change_stat("lust", 50, 10)
                ch_l "a little, yeah."
            "-digusted?":
                $ LauraX.change_stat("love", 75, -5)
                $ LauraX.change_stat("obedience", 200, -5)
                $ LauraX.change_face("_sadside", 1)
                ch_l ". . . kind of,"
                $ LauraX.change_face("_sly", 1)
                $ LauraX.change_stat("inhibition", 70, 5)
                $ LauraX.change_stat("lust", 50, 5)
                ch_l "but also kind of excited by it."
            "-hungry?":
                $ LauraX.change_face("_confused", 1,Eyes="_surprised",Mouth="_smile")
                $ LauraX.change_stat("obedience", 200, -5)
                $ LauraX.change_stat("inhibition", 50, -5)
                ch_l "?!"
                $ LauraX.change_face("_confused", 1,Eyes="_normal",Mouth="_smile")
                ch_l "Well. . . yeah? But not for-"
                $ LauraX.change_face("_sly", 1)
                $ LauraX.change_stat("lust", 50, 5)
                ch_l "I mean, it makes me kind of. . . excited."
            "-horny?":
                $ LauraX.change_stat("obedience", 200, 10)
                $ LauraX.change_stat("inhibition", 50, 5)
                $ LauraX.change_face("startled", 2,Mouth="_lipbite")
                ch_l "!"
                $ LauraX.change_face("_sly", 1, Eyes="_side")
                $ LauraX.change_stat("inhibition", 50, 5)
                $ LauraX.change_stat("lust", 50, 10)
                $ LauraX.change_stat("lust", 70, 5)
                ch_l "Yes."
        menu:
            extend ""
            "Good. If you wanna be with me, then you follow my orders.":
                if approval_check(LauraX, 1000, "LO"):
                    $ LauraX.change_face("_sly", 1)
                    $ LauraX.change_stat("obedience", 200, 15)
                    $ LauraX.change_stat("inhibition", 50, 10)
                    ch_l "Hmmm. . ."
                else:
                    $ LauraX.change_face("_sadside", 1,Mouth="_normal")
                    $ LauraX.change_stat("love", 200, -5)
                    $ LauraX.change_stat("obedience", 200, 10)
                    ch_l "You might want to slow your roll there, [LauraX.player_petname]."
                    menu:
                        extend ""
                        "Whatever. That's how it is. Take it or leave it.":
                            $ LauraX.change_face("_angry")
                            $ LauraX.change_stat("love", 200, -10)
                            $ LauraX.change_stat("obedience", 200, 5)
                            ch_l "I think you're pushing it too far there, [LauraX.player_petname]."
                            $ Line = "rude"
                        "Ok, just a little.":
                            $ LauraX.change_face("_bemused", 1)
                            $ LauraX.change_stat("love", 95, 5)
                            $ LauraX.change_stat("inhibition", 50, 5)
                            ch_l "-but not too much."
            "Yeah? You think it's sexy?":

                $ LauraX.change_face("_bemused", 2,Eyes="_side")
                $ LauraX.change_stat("obedience", 200, 5)
                $ LauraX.change_stat("inhibition", 50, 10)
                ch_l ". . ."
                $ LauraX.change_stat("lust", 50, 5)
                ch_l "Yeah."
            "You sure you don't want me to back off a little?":

                $ LauraX.change_face("startled", 1,Eyes="_squint")
                $ LauraX.change_stat("obedience", 200, -5)
                menu:
                    ch_l "Well if you have to ask. . ."
                    "Only if you're okay with it.":
                        $ LauraX.change_face("_bemused", 1)
                        $ LauraX.change_stat("love", 95, 10)
                        $ LauraX.change_stat("inhibition", 50, 10)
                        $ Line = 0
                    "Uhm. . .yeah. I think it's weird. Sorry.":
                        $ LauraX.change_face("_sad", 1, Eyes="_surprised")
                        $ LauraX.change_stat("love", 200, -15)
                        $ LauraX.change_stat("obedience", 200, -5)
                        $ LauraX.change_stat("inhibition", 50, -10)
                        $ Line = "embarrassed"
            "I couldn't care less.":

                $ LauraX.change_stat("love", 200, -10)
                $ LauraX.change_stat("obedience", 200, 15)
                $ LauraX.change_face("_angry")
                ch_l "I think you're pushing it too far there, [LauraX.player_petname]."
                $ Line = "rude"

    if not Line:
        $ LauraX.change_face("_bemused", 1,Eyes = "_down")
        ch_l "So, I'm willing to give this a shot."
        ch_l "Just a trial period, to see how it goes."
        ch_l "Just tell me what you want, and. . . I'll see about doing it."
        menu Laura_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                $ LauraX.change_stat("obedience", 200, 5)
                $ LauraX.change_stat("inhibition", 50, 5)
                $ LauraX.change_face("_sly", 1)
                $ Line = 0
            "Don't you think that relationship's kinda. . .weird?":
                $ LauraX.change_face("_sad", 1, Eyes="_surprised")
                $ LauraX.change_stat("love", 200, -5)
                $ LauraX.change_stat("inhibition", 50, -15)
                $ Line = "embarrassed"

    if not Line:
        $ LauraX.change_face("_smile", 1)
        ch_l "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                $ LauraX.change_stat("love", 95, 5)
                $ LauraX.change_stat("obedience", 200, 15)
                $ LauraX.change_stat("inhibition", 50, 5)
                ch_l "Yes, sir."
                $ LauraX.player_petname = "sir"
            "That's kind of formal, isn't it?":
                $ LauraX.change_face("_perplexed", 1)
                ch_l "Huh. ok, no problem"
                $ LauraX.change_stat("inhibition", 50, -5)
                $ LauraX.change_face("_sly", 1,Eyes="_side")
                menu:
                    ch_l "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                        $ LauraX.change_stat("obedience", 200, 10)
                        $ LauraX.change_face("_smile", 1)
                        ch_l "Good."
                    "I don't feel comfortable with that. . .":
                        $ LauraX.change_face("_sad", 1, Eyes="_side")
                        $ LauraX.change_stat("love", 200, -10)
                        $ LauraX.change_stat("obedience", 200, -30)
                        $ LauraX.change_stat("inhibition", 50, -15)
                        $ Line = "embarrassed"


    $ LauraX.history.append("sir")
    if not Line:
        $ LauraX.player_petnames.append("sir")

    elif Line == "rude":
        call remove_girl (LauraX)
        if "Historia" not in Player.traits:
            $ renpy.pop_call()
        "[LauraX.name] knocks her way past you and storms off."
    elif Line == "embarrassed":
        $ LauraX.change_face("_sadside", 2)
        ch_l "Huh, ok, if you're not interested. . ."
        hide Laura_Sprite with easeoutright
        call remove_girl (LauraX)
        if "Historia" not in Player.traits:
            $ renpy.pop_call()
        "[LauraX.name] heads out of the room."
    return

label Laura_Sub_Asked:
    $ Line = 0
    $ LauraX.change_face("_sadside", 1)
    ch_l "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in LauraX.player_petnames and approval_check(LauraX, 850, "O"):

                pass
            elif approval_check(LauraX, 550, "O"):

                pass
            else:
                $ LauraX.change_face("_angry", 1)
                ch_l "It was a bad idea, don't worry about it."
                $ Line = "rude"

            if Line != "rude":
                $ LauraX.change_stat("love", 90, 10)
                $ LauraX.change_face("_sly", 1)
                ch_l "Well, it's not like you stopped ordering me around anyway."
                ch_l "Ok, let's give it a shot."
        "I know it's what you want. Do you want to try again, or not?":

            $ LauraX.change_face("_bemused", 1)
            if "sir" in LauraX.player_petnames:
                if approval_check(LauraX, 850, "O"):
                    ch_l "Ok, fine."
                else:
                    ch_l "Nah, I'm good."
                    $ Line = "rude"
            elif approval_check(LauraX, 600, "O"):

                $ LauraX.change_face("_confused", 1)
                ch_l "Kinda wishy-washy there."
                $ LauraX.change_face("_sly", 1)
                ch_l "but maybe you're right."
                ch_l "Are you sure you're into this?"
                menu:
                    extend ""
                    "Yes, I'm sorry I was mean about it.":
                        $ LauraX.change_stat("love", 90, 15)
                        $ LauraX.change_stat("inhibition", 50, 10)
                        $ LauraX.change_face("_bemused", 1)
                        $ LauraX.eyes = "_side"
                        ch_l "Ok then."
                    "You're damned right I am, bitch.":
                        if "sir" in LauraX.player_petnames and approval_check(LauraX, 900, "O"):
                            $ LauraX.change_stat("love", 200, -5)
                            $ LauraX.change_stat("obedience", 200, 10)
                            ch_l ". . ."
                        elif approval_check(LauraX,700, "O"):
                            $ LauraX.change_stat("love", 200, -5)
                            $ LauraX.change_stat("obedience", 200, 10)
                            ch_l "Hmmm. . ."
                        else:
                            $ LauraX.change_stat("love", 200, -10)
                            $ LauraX.change_stat("obedience", 90, -10)
                            $ LauraX.change_stat("obedience", 200, -10)
                            $ LauraX.change_stat("inhibition", 50, -15)
                            $ LauraX.change_face("_angry", 1)
                            ch_l "Wow, that's pushing it."
                            $ Line = "rude"
                    "Ok, never mind then.":
                        $ LauraX.change_face("_angry", 1)
                        $ LauraX.change_stat("love", 200, -10)
                        $ LauraX.change_stat("obedience", 90, -10)
                        $ LauraX.change_stat("obedience", 200, -10)
                        $ LauraX.change_stat("inhibition", 50, -15)
                        ch_l "I was thinking of taking orders from you, not mindgames."
                        ch_l "I should've known you'd be like this."
                        $ Line = "rude"

    $ LauraX.recent_history.append("asked sub")
    $ LauraX.daily_history.append("asked sub")
    if Line == "rude":

        hide Laura_Sprite with easeoutright
        call remove_girl (LauraX)
        $ LauraX.recent_history.append("_angry")
        if "Historia" not in Player.traits:
            $ renpy.pop_call()
        "[LauraX.name] checks you as she stomps out of the room."
    elif "sir" in LauraX.player_petnames:

        $ LauraX.change_stat("obedience", 200, 50)
        $ LauraX.player_petnames.append("master")
        $ LauraX.player_petname = "master"
        $ LauraX.eyes = "_sly"
        ch_l ". . . master. . ."
    else:

        $ LauraX.change_stat("obedience", 200, 30)
        $ LauraX.player_petnames.append("sir")
        $ LauraX.player_petname = "sir"
        $ LauraX.change_face("_sly", 1)
        ch_l ". . . sir."
    return






label Laura_Master:
    $ LauraX.drain_word("asked_to_meet")
    call shift_focus (LauraX)
    if LauraX.location != bg_current and LauraX not in Party:
        "Suddenly, [LauraX.name] shows up and says she needs to talk to you."

    $ LauraX.location = bg_current
    call set_the_scene (0)
    call show_girl (LauraX)
    call clear_the_room (LauraX)
    call set_the_scene
    $ LauraX.daily_history.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ LauraX.change_face("_sly", 1)
    ch_l "[LauraX.player_petname]. . ."
    ch_l ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            $ LauraX.change_stat("obedience", 200, 5)
            $ LauraX.change_stat("inhibition", 50, 5)
        "What?":
            ch_l "I was asking if I could talk to you about something. . ."
            $ LauraX.eyes = "_side"
            ch_l ". . . personal."
            $ LauraX.eyes = "_squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ LauraX.change_stat("love", 80, 5)
                    $ LauraX.change_stat("obedience", 200, 5)
                    ch_l "Right. . ."
                "Oh, then no.":
                    $ LauraX.change_face("_sad", 1)
                    $ LauraX.change_stat("love", 80, -5)
                    $ LauraX.change_stat("obedience", 200, -10)
                    $ Line = "embarrassed"
        "No.":
            $ LauraX.change_face("_perplexed", 1,Brows="_confused")
            $ LauraX.change_stat("love", 80, -5)
            $ LauraX.change_stat("obedience", 200, -5)
            $ LauraX.change_stat("inhibition", 50, -5)
            ch_l "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ LauraX.change_face("_confused", 1)
                    $ LauraX.change_stat("obedience", 200, 10)
                    $ LauraX.change_stat("inhibition", 60, 10)
                    ch_l "Right. . ."
                "Yes, not interested.":
                    $ LauraX.change_face("_sad", 1)
                    $ LauraX.change_stat("love", 80, -5)
                    $ LauraX.change_stat("inhibition", 50, -10)
                    $ Line = "embarrassed"


    if not Line:
        $ LauraX.change_face("_sly", 1)
        ch_l "I think I enjoy having you in charge."
        ch_l "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                $ LauraX.change_face("_sly", 1)
                $ LauraX.change_stat("obedience", 200, 5)
                ch_l "Good. Maybe we could take this a bit more seriously?"
                menu:
                    extend ""
                    "Nah. This is just about perfect.":
                        $ LauraX.change_face("_sad", 1)
                        $ LauraX.change_stat("obedience", 200, -15)
                        $ LauraX.change_stat("love", 80, 10)
                        $ Line = "fail"
                    "What'd you have in mind?":
                        $ LauraX.eyes = "_side"
                        ch_l "I was thinking I could start calling you. . . {i}master{/i}?"
                        $ LauraX.eyes = "_squint"
                        menu:
                            extend ""
                            "Oh, yeah. I'd like that.":
                                $ LauraX.change_stat("obedience", 200, 5)
                                ch_l "Good. . ."
                            "Um. . .nah. That's too much.":
                                $ LauraX.change_face("_sadside", 1)
                                $ LauraX.change_stat("obedience", 200, -15)
                                $ LauraX.change_stat("inhibition", 50, 5)
                                $ Line = "fail"
                    "Actually, I'd prefer we stopped doing it. Too much pressure.":

                        $ LauraX.change_face("_sad", 1)
                        $ LauraX.change_stat("love", 200, -5)
                        $ LauraX.change_stat("obedience", 200, -10)
                        $ LauraX.change_stat("inhibition", 50, 15)
                        $ Line = "fail"
                    "Actually, let's stop that. It's creeping me out.":

                        $ LauraX.change_face("_angry", 2, Eyes="_surprised")
                        $ LauraX.change_stat("love", 200, -10)
                        $ LauraX.change_stat("obedience", 200, -50)
                        $ LauraX.change_stat("inhibition", 50, -15)
                        ch_l "Say no more, I wouldn't want to CREEP YOU OUT."
                        $ Line = "embarrassed"
            "As if I care what you think, slut.":

                $ LauraX.change_face("_angry", 1, Mouth="_smile")
                $ LauraX.change_stat("love", 90, -20)
                $ LauraX.change_stat("obedience", 200, 10)
                $ LauraX.change_stat("inhibition", 50, -10)
                ch_l ". . ."
                menu:
                    ch_l "Excuse me?"
                    "Sorry. I just don't care what you want.":
                        if approval_check(LauraX, 1400, "LO"):
                            $ LauraX.change_stat("obedience", 200, 10)
                            ch_l ". . ."
                            $ LauraX.change_face("_sly", 1)
                            $ LauraX.change_stat("love", 200, 20)
                            $ LauraX.change_stat("inhibition", 50, 15)
                            ch_l ". . .{i}go on. . .{/i}"
                        else:
                            $ LauraX.change_stat("love", 200, -15)
                            $ LauraX.change_stat("obedience", 200, -10)
                            $ LauraX.change_stat("inhibition", 50, 5)
                            $ LauraX.change_face("_angry", 1)
                            ch_l "!!!"
                            $ Line = "rude"
                    "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                        $ LauraX.change_stat("love", 200, 10)
                        $ LauraX.change_stat("obedience", 200, 10)
                        $ LauraX.change_stat("inhibition", 50, 5)
                        if approval_check(LauraX, 1400, "LO"):
                            $ LauraX.change_stat("obedience", 200, 10)
                            ch_l ". . ."
                            $ LauraX.change_face("_sly", 1)
                            $ LauraX.change_stat("love", 200, 20)
                            $ LauraX.change_stat("inhibition", 50, 15)
                            ch_l ". . .{i}no, about right. . .{/i}"
                        else:
                            $ LauraX.change_stat("love", 200, 5)
                            $ LauraX.change_stat("obedience", 200, -5)
                            $ LauraX.change_stat("inhibition", 50, 5)
                            $ LauraX.change_face("_angry", 1, Eyes="_side")
                            ch_l ". . ."
                            ch_l "We'll work on it. . ."
            "I don't really like it. Too much pressure.":

                $ LauraX.change_face("_sad", 2)
                $ LauraX.change_stat("love", 200, -20)
                $ LauraX.change_stat("obedience", 200, -20)
                $ LauraX.change_stat("inhibition", 50, -10)
                $ Line = "embarrassed"

    $ LauraX.history.append("master")
    if Line == "rude":
        $ LauraX.recent_history.append("_angry")
        hide Laura_Sprite with easeoutright
        call remove_girl (LauraX)
        if "Historia" not in Player.traits:
            $ renpy.pop_call()
        "[LauraX.name] stomps out of the room."
    elif Line == "embarrassed":
        ch_l "Ok, fine then."
        ch_l "And here I was, about to \"elevate your clearance.\""
        hide Laura_Sprite with easeoutright
        call remove_girl (LauraX)
        if "Historia" not in Player.traits:
            $ renpy.pop_call()
        "[LauraX.name] brushes past you on her way out."
    elif Line == "fail":
        ch_l "Oh. . ."
        ch_l "I guess that's fine."
    else:
        $ LauraX.change_stat("obedience", 200, 50)
        $ LauraX.player_petnames.append("master")
        $ LauraX.player_petname = "master"
        ch_l ". . .master."
    return







label Laura_Sexfriend:

    $ LauraX.lust = 70
    $ LauraX.location = bg_current
    $ LauraX.drain_word("asked_to_meet")
    call set_the_scene
    $ LauraX.daily_history.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ LauraX.change_face("_sly",2,Eyes="_side")
    "[LauraX.name] approaches you and pulls you aside. She seems to be shivering a little bit."
    "She seems to be squirming around and rubbing her thighs together."
    $ LauraX.player_petnames.append("sex friend")
    $ LauraX.change_face("_sly",2)
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
                $ LauraX.change_face("_sly",2,Mouth="_smile")
                $ Line = "yes"
            "No thanks":
                $ LauraX.change_face("_confused",2)
                $ Line = "no"
            ". . .":
                $ LauraX.change_stat("obedience", 90, 5)
                $ LauraX.change_face("_confused",2)

        if not Line:
            ch_l "Now, if at all possible. . ."
            menu:
                extend ""
                "Sure":
                    $ LauraX.change_face("_sly",2,Mouth="_smile")
                    $ Line = "yes"
                "No thanks":
                    $ LauraX.change_face("_confused",2)
                    $ Line = "no"

        if Line == "no":
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 80, 5)
            ch_l "What? Why not?"
            menu:
                extend ""
                "Ok, fine":
                    $ LauraX.change_face("_confused",2,Mouth="_smile")
                    ch_l "Love the enthusiasm."
                    $ Line = "yes"
                "Not interested":
                    $ LauraX.change_face("_confused",2)
                "There's someone else":

                    $ LauraX.change_stat("love", 95, -5)
                    $ LauraX.change_stat("obedience", 90, 5)
                    if Player.Harem:
                        $ LauraX.change_face("_surprised",2)
                        ch_l "Oh, [Player.Harem[0].name]?"
                        $ LauraX.GLG(Player.Harem[0],600,-25,1)
                    $ LauraX.change_face("_sly",2)
                    ch_l "Well, she doesn't need to know about it. . ."
                    menu:
                        extend ""
                        "Ok, fine":
                            ch_l "Love the enthusiasm."
                            $ Line = "yes"
                        "Still no":
                            pass

    if Line == "no":
        $ LauraX.change_stat("love", 200, -10)
        $ LauraX.change_stat("obedience", 90, 15)
        $ LauraX.change_stat("inhibition", 90, 10)
        $ LauraX.change_face("_sad",2)
        ch_l "Really?"
        ch_l "Bummer."
        ch_l "Well let me know if you change your mind."
        $ LauraX.change_face("_sadside",2,Mouth="_lipbite",Brows="_angry")
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
        $ LauraX.change_face("_sly",1,Mouth="_smile")
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
                    call clear_the_room (LauraX)
                    call set_the_scene
                    $ Taboo = 0
                    $ LauraX.Taboo = 0
                "No, let's do it here.":

                    $ LauraX.change_stat("obedience", 80, 5)
                    $ LauraX.change_stat("inhibition", 90, 15)
                    ch_l "Kinky."

        $ action_context = LauraX
        $ Player.add_word(1,"interruption")
        call Laura_SexPrep
        call Laura_SexMenu


    return






label Laura_Fuckbuddy:
    $ LauraX.daily_history.append("relationship")
    $ LauraX.lust = 80
    $ LauraX.drain_word("asked_to_meet")

    "You hear a knock on the door, and go to answer it."

    $ LauraX.location = bg_current
    call shift_focus (LauraX)
    call set_the_scene (0)
    $ LauraX.outfit = "casual1"
    $ LauraX.today_outfit = "casual1"
    $ LauraX.change_outfit("casual1")
    call show_girl (LauraX)
    call Taboo_Level
    $ primary_action = "masturbation"
    $ girl_offhand_action = "fondle_pussy"
    $ LauraX.change_face("_sly",2,Mouth="_lipbite")
    "[LauraX.name] is standing in the doorway, with her hand down her pants."
    "You can tell she's been masturbating furiously, her scent is overpowering."
    $ primary_action = 0
    $ girl_offhand_action = 0
    $ LauraX.ArmPose = 1
    "She looks you up and down hungrily, and pulls her hand out of her pants."
    "She reaches up to caress your face, smearing her juices along it."
    ch_l "Mine."
    $ LauraX.player_petnames.append("fuck buddy")
    $ LauraX.Event[10] += 1

    $ action_context = LauraX
    $ Player.add_word(1,"interruption")
    call Laura_SexPrep
    call Laura_SexMenu
    return






label Laura_Daddy:
    $ LauraX.daily_history.append("relationship")
    $ LauraX.drain_word("asked_to_meet")
    call shift_focus (LauraX)
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
            $ LauraX.change_face("_smile")
            $ LauraX.change_stat("love", 90, 20)
            $ LauraX.change_stat("obedience", 60, 10)
            $ LauraX.change_stat("inhibition", 80, 30)
            ch_l "Cool."
        "What do you mean by that?":
            $ LauraX.change_face("_bemused")
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
                    $ LauraX.change_face("_smile")
                    $ LauraX.change_stat("love", 90, 15)
                    $ LauraX.change_stat("obedience", 60, 20)
                    $ LauraX.change_stat("inhibition", 80, 25)
                    ch_l "Great!"
                    $ LauraX.change_face("_sly",2)
                    ch_l " . . . daddy."
                    $ LauraX.change_face("_sly",1)
                    $ LauraX.player_petname = "daddy"
                "Could you not, please?":
                    $ LauraX.change_stat("love", 90, 5)
                    $ LauraX.change_stat("obedience", 80, 40)
                    $ LauraX.change_stat("inhibition", 80, 20)
                    $ LauraX.change_face("_sad")
                    ch_l " . . . "
                    ch_l "Well, ok."
                "You've got some real daddy issues, uh?":
                    $ LauraX.change_stat("love", 90, -15)
                    $ LauraX.change_stat("obedience", 80, 45)
                    $ LauraX.change_stat("inhibition", 70, 5)
                    $ LauraX.change_face("_angry")
                    ch_l "Yes. . . I said that."
        "You've got some real daddy issues, uh?":
            $ LauraX.change_stat("love", 90, -15)
            $ LauraX.change_stat("obedience", 80, 45)
            $ LauraX.change_stat("inhibition", 70, 5)
            $ LauraX.change_face("_angry")
            ch_l ". . . Probably."
            ch_l "Never mind."
    $ LauraX.player_petnames.append("daddy")
    return






label Gwentro:
    $ Player.add_word(1,"interruption")
    if Taboo > 5 or RogueX.location == bg_current or KittyX.location == bg_current or EmmaX.location == bg_current:

        return
    $ LauraX.history.append("Gwentro")
    $ Gwenname = "???"
    ch_g "Where is the exit to this place?!"
    call GwenFace ("_angry")
    show Gwen_Sprite zorder 25 at sprite_location(1500):
        xzoom -1
    show Gwen_Sprite zorder 25 at sprite_location(100) with easeinright
    pause .1
    call GwenFace ("_surprised")
    $ action_speed = 0
    $ LauraX.change_face("_surprised",2,Eyes="_side")
    show Gwen_Sprite zorder 25 at sprite_location(200) with vpunch
    ch_g "Ouch!"
    call GwenFace ("_angry")
    ch_g "Ok, that's a wall. . . apparently."
    call GwenFace ("_surprised")
    ch_g "Oh, hey you tw-"
    call GwenFace ("_surprised", 1, Mouth = "_kiss")
    ch_g "Um. . ."
    call GwenFace ("shocked", 1)
    ch_g "Sorry! My bad, I was just. . ."
    $ LauraX.change_face("_confused",2,Eyes="_side")
    call GwenFace ("_surprised", 1, Mouth = "_kiss")
    extend "\n looking for an exit. . ."
    call GwenFace ("_smile", 1)
    extend "\n but you two. . . seem to be working on something. . ."
    call GwenFace ("_sad", 1)
    extend "\n and now I can't see because of this stupid word balloon. . ."
    show Gwen_Sprite:
        ease 1 ypos 150
    call GwenFace ("_smile", 1)
    extend ""
    ch_g "Better. . ."
    show Gwen_Sprite:
        ease 1 ypos 50
    ch_g "So now that we've got that taken care of, what's your name?"
    $ LauraX.change_face("_angry",1,Eyes="_side")
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
    call GwenFace ("_surprised")
    ch_g "Sorry, it's just that menu popping up caught me by surprise."
    call GwenFace ("_smile")
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
            $ Gwenname = "Gwen"
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
    if Gwenname != "Gwen":
        $ Gwenname = "Gwen"
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
    $ LauraX.change_face("_angry",Eyes="leftside")
    ch_g "Sorry, I should have said hello earlier, hey Laura!"
    $ LauraX.change_face("_confused",Eyes="leftside")
    ch_l "How do you know my name!"
    ch_g "I've read all about you! Or do you prefer \"X-23?\""
    ch_g "Or \"Wolverine?\""
    call GwenFace ("_surprised", Mouth = "_kiss")
    ch_g "God, it's not \"Talon,\" is it?"
    call GwenFace ("_smile")
    ch_l "[LauraX.name] - is - fine."
    call GwenFace ("_smile", Mouth = "_kiss")
    ch_g "Cool, so. . ."
    menu:
        "What are you doing here?":
            ch_p "What are you doing here?"
            ch_g "I had a feeling you would ask that."
        "Some other irrelvant option.":
            ch_p "What are you doing here?"
            ch_g "Man, determinism, am I right?"
    $ LauraX.change_face("_confused",Eyes="leftside")
    ch_g "Why are any of us here, really?"
    ch_g "Oh! You mean \"why am I {i}here{/i}\" in this game?"
    call GwenFace ("_sad")
    ch_g "Honestly? No idea. One minute I had an ongoing, then I was on a team book, guess that's cancelled now?"
    call GwenFace ("_smile")
    ch_g "Yeah, your guess is as good as mine. Maybe whoever made it's a fan?"
    call GwenFace ("_smile", 1)
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
    call GwenFace ("_angry", 1)
    ch_g "Huh."
    ch_g "Apparently I can't get my clothes off here."
    call GwenFace ("_sad", 1)
    ch_g "That's unfortunate."
    call GwenFace ("_angry", 1, Mouth="_smile")
    ch_g "I could just stay and watch for a bit. . ."
    $ LauraX.change_face("_angry",Eyes="leftside")
    call GwenFace ("_surprised", 1)
    ch_l "NO!"
    ch_g "Right, right. Don't poke the wolverine. . ."
    call GwenFace ("_smile", 1)
    ch_g "Except you, of course -wink-."
    call GwenFace ("_sad", 0)
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
    call GwenFace ("_sad", 1, Eyes="_surprised")
    ch_g "Maybe never, we won't know."
    show Gwen_Sprite:
        ease .2 xpos 1500
    call GwenFace ("_surprised")
    ch_l "Get out!"
    ch_g "Right! I'm gone, sorry!"
    hide Gwen_Sprite
    $ LauraX.change_face("_bemused",Eyes="_sexy")
    ch_l "Now, what were were doing. . ."

    return


label Laura_Dressup:


    $ active_Girls.append(LauraX) if LauraX not in active_Girls else active_Girls
    call shift_focus (LauraX)
    $ bg_current = "bg_campus"
    call remove_girl ("All")
    $ LauraX.location = bg_current
    call set_the_scene (0)

    $ LauraX.outfit = "casual1"
    $ LauraX.change_outfit("casual1")
    show Laura_Sprite at sprite_location(LauraX.sprite_location) with vpunch
    $ round -= 10 if round >= 11 else round
    $ LauraX.history.remove("dress0")
    $ LauraX.history.append("dress1")
    $ LauraX.history.append("met")
    "As you're heading across the square, you bump into [LauraX.name]."
    $ LauraX.change_face("_normal")
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
            $ LauraX.change_face("_confused")
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
            $ LauraX.change_face("_bemused")
            ch_l "Not really."

    hide Laura_Sprite with easeoutright
    call remove_girl (LauraX)
    "[LauraX.name] walks away, and as you watch her go you feel a tap on your shoulder."

    call shift_focus (KittyX)
    $ KittyX.location = bg_current
    call set_the_scene (0)
    $ KittyX.outfit = KittyX.today_outfit
    $ KittyX.change_outfit()
    call show_girl (KittyX)

    $ KittyX.change_face("_smile")
    ch_k "Hey, [KittyX.player_petname], what're you staring at?"


    menu:
        extend ""
        "Hey, [KittyX.name]. I was just talking to [LauraX.name].":
            ch_k "Oh, she's back?"
        "Oh, nothing.":
            ch_k "Oh, I see, [LauraX.name]."
            ch_k "She's back?"
        "I was checking out that fine piece over there.":
            if approval_check(KittyX,1200,"LO") or KittyX.event_counter["been_with_girl"] >= 10:
                $ KittyX.change_stat("obedience", 80, 5)
                $ KittyX.change_stat("inhibition", 80, 5)
                $ KittyX.change_face("_bemused",1)
                ch_k "I guess I can't blame you. . ."
            else:
                $ KittyX.change_stat("love", 70, -5)
                $ KittyX.change_stat("obedience", 80, 10)
                $ KittyX.change_stat("inhibition", 80, 5)
                $ KittyX.change_face("_angry")
                ch_k "Rude much?"

    $ KittyX.change_face("_smile",Eyes="_side")
    ch_k "She's never around very much, you know."
    ch_k "Must get it from Logan."

    menu:
        extend ""
        "Oh, they're related?":
            ch_k "Yeah, she's his daughter or something? I'm not too sure."
        "She's his clone, right?":
            ch_k "I guess? I'm not too sure."
    "She shrugs, but then grins mischieviously."

    $ KittyX.change_face("_sly")
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


    ch_k "Well, she doesn't really have much of a wardrobe, so we were going to get her some new clothes."

    menu:
        extend ""
        "You're really stylish, so you'll probably pick out something great.":
            $ KittyX.change_stat("love", 80, 5)
            $ KittyX.change_stat("inhibition", 40, 3)
            $ KittyX.change_face("_smile",1)
            ch_k "Sweet talker."
        "That sounds good.":
            $ KittyX.change_stat("love", 60, 2)
        "With your fashion sense? That'll end well.":
            $ KittyX.change_stat("love", 70, -5)
            $ KittyX.change_stat("obedience", 80, 5)
            $ KittyX.change_stat("inhibition", 80, -3)
            $ KittyX.change_face("_angry")
    ch_k "Anyway, we were thinking around $10 each."

    menu:
        extend ""
        "Here you go." if Player.cash >= 10:
            $ KittyX.change_stat("love", 70, 1)
            $ KittyX.change_stat("obedience", 40, 2)
            ch_k "Nice."
            $ Player.cash -= 10
            $ LauraX.history.append("dress2")
        "I don't have enough. . ." if Player.cash < 10:
            $ KittyX.change_stat("love", 70, 1)
            $ KittyX.change_stat("obedience", 40, 2)
            $ KittyX.change_face("_normal",1,Brows="_surprised",Mouth="_sad")
            ch_k "Oh."
            ch_k "We aren't in a rush or anything. If you still want to, just hit me up."
        "You know what, never mind.":
            $ KittyX.change_stat("love", 70, -2)
            $ KittyX.change_stat("obedience", 40, -1)
            $ KittyX.change_face("_normal",1,Brows="_surprised",Mouth="_sad")
            ch_k "Oh, ok."
    return

label Laura_Dressup2:

    ch_p "Hey, remember that gift you wanted to give [LauraX.name] earlier?"
    $ KittyX.change_face("_smile")
    ch_k "Yeah?"
    menu:
        extend ""
        "Here you go, $10.":
            $ KittyX.change_stat("love", 70, 1)
            $ KittyX.change_stat("obedience", 40, 2)
            ch_k "Cool."
            $ LauraX.history.append("dress2")
        "Never mind.":
            ch_k "Oh, ok."
    return


label Laura_Dressup3:


    $ LauraX.history.remove("dress1")
    $ LauraX.history.remove("dress2")
    $ LauraX.history.append("dress3")
    $ LauraX.inventory.append("wolvie_top")
    $ LauraX.inventory.append("wolvie_panties")

    "You're walking past [KittyX.name]'s door when you hear her laughing at something."
    "You hear someone else's voice, there's clearly someone else in her room with her."

    ch_l "[KittyX.name], you shouldn't have."
    ch_l "No, seriously. . ."
    ch_l "you shouldn't have."
    ch_k "Aww, c'mon. You look great."

    "You remember [KittyX.name] talking about getting [LauraX.name] some new clothes. She must've gotten [LauraX.name] to try them on."
    "You can't help but feel curious. . ."

    $ KittyX.outfit = KittyX.today_outfit
    $ KittyX.change_outfit()
    $ LauraX.change_outfit("nude")
    $ LauraX.bra = "wolvie_top"
    $ LauraX.underwear = "wolvie_panties"
    menu:
        extend ""
        "Sneak a peek [[no key] (locked)" if KittyX not in Keys:
            pass
        "Sneak a peek" if KittyX in Keys:
            "You use your key and unlock the door, opening it and sticking your head in."
            ch_p "Hey, [KittyX.name], what's going on?"
            ch_k "Hey, [KittyX.player_petname]! Come on in!"

            call clear_the_room ("All", 0, 1)
            call shift_focus (LauraX)
            $ KittyX.location = "bg_kitty"
            $ LauraX.location = "bg_kitty"
            call set_the_scene (Dress=0)

            $ LauraX.change_face("_sad",2,Eyes="_squint",Brows="_confused")
            "[LauraX.name] stares at you, her eyes narrowed. She's clearly on edge."
            $ LauraX.change_face("_sad",2,Brows="_confused",Eyes="leftside")
            ch_l "Didn't you lock the door?"
            if KittyX.event_counter["sleepover"] < 5:
                $ KittyX.change_face("_smile",Eyes="_side")
                ch_k "Yeah, but I gave him a key."
                $ LauraX.change_face("_sad",1,Brows="_confused",Eyes="leftside")
                ch_l "You. . . gave him a key?"
            else:

                $ KittyX.change_face("_confused",Eyes="_side")
                ch_k "Yeah, I'm not really sure how he got a key. . ."
                if not approval_check(KittyX,1200):

                    $ KittyX.change_face("_angry",1)
                    ch_k "Ok, that's enough, out, out!"
                    "You head back out."
                    return
                $ KittyX.change_face("_smile")
                ch_k "I guess it's fine though. . ."
                $ LauraX.change_face("_sad",1,Brows="_confused",Eyes="leftside")
                ch_l "It's fine that he got a mystery key?"
            $ KittyX.change_face("_smile",1)
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

            call clear_the_room ("All", 0, 1)
            call shift_focus (LauraX)
            $ KittyX.location = "bg_kitty"
            $ LauraX.location = "bg_kitty"
            call set_the_scene (Dress=0)

            $ LauraX.change_face("_sad",2,Brows="_surprised")
            "[LauraX.name] stares at you, as if she's not sure what she's seeing."
            $ LauraX.change_face("_sad",2,Brows="_confused",Eyes="leftside")
            ch_l "So you just let him come into your room whenever?"
            $ KittyX.change_face("_smile",1)
            ch_k "Uh-huh. I mean, he's my [KittyX.player_petname]."
            ch_l "Your. . . [KittyX.player_petname]."
        "Walk away":

            "Nah, I should let them have their girl time."
            return
    $ LauraX.SeenPanties = 1
    $ LauraX.change_face("_angry",1,Eyes="_closed")
    "She shakes her head, trying to absorb all this new information."
    "She mutters to herself."
    ch_l "I've been gone longer than I thought. . ."
    $ LauraX.change_face("_sad",1,Brows="_confused",Eyes="leftside")
    ch_l "So why's he here?"
    $ KittyX.change_face("_smile",Eyes="_side")
    ch_k "Well, he kind of pitched in to get you this stuff, so why not see what he thinks?"
    "[KittyX.name] walks over and poses like she's presenting [LauraX.name] as a model."
    $ KittyX.ArmPose = 2
    $ KittyX.change_face("_smile")
    ch_k "So, what do you think?"

    menu:
        extend ""
        "Her outfit looks familiar. . .":
            ch_k "I call it the Logan Look."
            $ LauraX.change_face("_sad",2,Eyes="_stunned")
            $ LauraX.change_stat("inhibition", 40, -2)
            ch_l "Please don't call it that."
        "Looking good, [LauraX.name]!":
            $ LauraX.change_stat("love", 70, 5)
            $ LauraX.change_stat("obedience", 40, 3)
            $ LauraX.change_stat("inhibition", 40, 5)
            $ LauraX.GLG(KittyX,700,5,1)
            $ LauraX.change_face("_sadside",1)
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
            $ LauraX.change_face("_bemused",1)
            $ LauraX.GLG(KittyX,700,3,1)
            ch_l "Yeah, I guess she does. . ."
        "Can I get a refund?":
            $ KittyX.change_stat("love", 70, -5)
            $ KittyX.change_stat("obedience", 40, -3)
            $ KittyX.change_face("_angry")
            ch_k "Way to bring down the mood."
            $ LauraX.change_stat("love", 70, -5)
            $ LauraX.change_stat("obedience", 40, 5)
            $ LauraX.change_stat("inhibition", 40, -5)
            $ LauraX.change_face("_angry")
            ch_l "Seriously."

    $ LauraX.change_face("_smile",0,Eyes="leftside")
    $ LauraX.GLG(KittyX,700,5,1)
    $ KittyX.GLG(LauraX,700,5,1)
    ch_l "But really, [KittyX.name], thanks for this."
    $ KittyX.change_face("_smile",Eyes="_side")
    ch_k "No problem! Like, what're friends for?"
    ch_l "Pretty sure friends don't normally use their friends as dressup dolls."
    ch_k "Oh, [LauraX.name], you have sooooo much to learn."
    $ LauraX.change_face("_smile",Eyes="_down")
    "[LauraX.name] smiles just a little bit and looks down at herself."
    ch_l "I think wearing the whole outfit is a bit much."
    $ LauraX.change_face("_smile",Eyes="leftside")
    ch_l "You know that Logan's going to have a few words if he sees me like this."
    $ KittyX.change_face("_smile",Eyes="_side")
    ch_k "Hey, it's your outfit now. Mix-and-match, girl!"
    ch_l "Yeah. Yeah, I think I'll do that."
    $ LauraX.names.append("Wolverine")

    $ KittyX.change_face("_smile")
    $ LauraX.change_face("_sly",1)
    "[LauraX.name] fixes you with a steely gaze."

    ch_l "So. . . I'd like to change now."

    menu:
        extend ""
        "Go right ahead!":
            $ LauraX.change_stat("obedience", 40, 3)
            $ LauraX.change_stat("inhibition", 40, 3)
            if (not LauraX.SeenChest or not LauraX.SeenPussy) and not approval_check(LauraX,1400):
                $ LauraX.change_stat("love", 70, -5)
                $ LauraX.change_face("_angry",1)
                ch_l "I don't think so."
                ch_k "Yeah, I think you'd better get going, [KittyX.player_petname]. . ."
                ch_k ". . .Before she does to you what Logan does to people who make him mad."
                "[KittyX.name] firmly escorts you to the door."
            else:
                if LauraX.SeenChest and LauraX.SeenPussy:
                    ch_l "Fair enough. . ."
                elif approval_check(LauraX,1400):
                    ch_l "Bold choice. . ."
                $ KittyX.change_face("_surprised",2,Eyes="_side")
                $ LauraX.bra = ""
                "[LauraX.name] starts stripping out of the new clothes. . ."
                if approval_check(KittyX,1200):
                    $ KittyX.change_face("_sly",1)
                else:
                    $ KittyX.change_face("_angry",1,Eyes="_side")

                $ LauraX.underwear = ""
                call Laura_First_Topless
                call Laura_First_Bottomless (1)
                pause 1
                $ LauraX.change_outfit(LauraX.today_outfit,Changed=1)
                "And then puts on her usual outfit."

                if approval_check(KittyX,1200):
                    $ KittyX.change_face("_sly",1)
                else:
                    $ KittyX.change_face("_angry",1)
                ch_k "Well, I guess you got your show for the day."
                ch_k "Now give us some girl time."
                "[KittyX.name] shoos you out of the room and you head to the Campus square."
        "Message received. See you girls later!":

            ch_k "Later, [KittyX.player_petname]!"
            ch_l "See ya."

    $ round -= 20 if round >= 21 else round
    return





label Laura_Foul:
    $ LauraX.history.remove("partyfoul")
    if "partysolved" in LauraX.history:
        $ LauraX.history.remove("partysolved")
    $ LauraX.add_word(1,0,0,0,"partyfix")
    $ LauraX.change_face("_sad",1)
    if LauraX.location == bg_current or LauraX in Party:
        "[LauraX.name] glances over at you with a distressed look."
    else:
        "[LauraX.name] turns a corner and notices you."
    if bg_current != "bg_laura" and bg_current != "bg_player":
        "With little word, she moves behind you and pushes you towards her room."
        $ bg_current = "bg_laura"
    $ LauraX.location = bg_current
    call set_the_scene
    call clear_the_room (LauraX)
    call set_the_scene
    call Taboo_Level
    ch_l "Hey. . ."
    ch_l "[LauraX.player_petname]. . ."
    ch_l "About that time at the party. . ."
    menu:
        extend ""
        "What time at the party?":
            $ LauraX.change_stat("love", 90, -2)
            $ LauraX.change_stat("obedience", 80, 2)
            $ LauraX.change_stat("inhibition", 60, 1)
            $ LauraX.change_face("_confused",2)
        "Oh, yeah. I'm sorry about that.":
            $ LauraX.change_stat("love", 80, 5)
            $ LauraX.change_stat("love", 200, 5)
            $ LauraX.change_face("_surprised",2)
            $ LauraX.add_word(1,"sorry",0,0,0)
            $ LauraX.change_face("_smile",1)
        "Yeah?":
            $ LauraX.change_stat("obedience", 50, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            $ LauraX.change_face("_sad",1)
        ". . .":
            $ LauraX.change_stat("love", 80, -1)
            $ LauraX.change_stat("obedience", 50, 2)
            $ LauraX.change_face("_sad",1)

    if "sorry" not in LauraX.recent_history:

        $ LauraX.change_face("_sadside",1)
        ch_l "We were at the Halloween Party. . ."
        $ LauraX.change_face("_sad",1)
        ch_l "And you said something about my costume. . ."
        menu:
            extend ""
            "I don't remember, what did I say?":
                $ LauraX.change_stat("love", 99, -3)
                $ LauraX.change_face("_surprised",1)
            "Oh, yeah. I'm sorry about that.":
                $ LauraX.change_face("_smile",1)
                $ LauraX.change_stat("love", 80, 5)
                $ LauraX.change_stat("love", 200, 5)
                $ LauraX.add_word(1,"sorry",0,0,0)
            "Did I?":
                $ LauraX.change_face("_surprised",1)
                ch_l ". . ."
                $ LauraX.change_stat("love", 99, -5)
                $ LauraX.change_stat("obedience", 70, 3)
                $ LauraX.change_stat("obedience", 90, 2)
                $ LauraX.change_face("_angry",1)
            ". . .":
                $ LauraX.change_stat("love", 99, -1)
                $ LauraX.change_face("_angry",1)

    if "sorry" not in LauraX.recent_history:

        ch_l "You said that it looked like a. . ."
        ch_l "A prostitute."
        menu:
            extend ""
            "Oooh. Ouch. Yeah.":
                $ LauraX.change_face("_sly",1)
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("love", 200, 2)
                $ LauraX.change_stat("inhibition", 60, 2)
            "Oh, yeah. I'm sorry about that.":
                $ LauraX.change_face("_smile",1)
                $ LauraX.change_stat("love", 80, 2)
                $ LauraX.change_stat("love", 200, 5)
                $ LauraX.add_word(1,"sorry",0,0,0)
            "Is that a problem?":
                $ LauraX.change_face("_surprised",1)
                pause 0.5
                $ LauraX.change_face("_angry",1)
                $ LauraX.change_stat("love", 80, -5)
                $ LauraX.change_stat("love", 200, -5)
                $ LauraX.change_stat("obedience", 70, 5)
                ch_l "Of -course- it's a -problem-. . ."
            "Huh.":
                $ LauraX.change_stat("love", 99, -3)
                $ LauraX.change_stat("obedience", 70, 5)
                $ LauraX.change_face("_surprised",1)
            ". . .":
                $ LauraX.change_stat("love", 80, -2)
                $ LauraX.change_stat("love", 200, -2)
                $ LauraX.change_face("_angry",1)

    if "lover" in LauraX.player_petnames:
        ch_l "You understand why this would.. bother me. . ."
        menu:
            extend ""
            "Oh. . . yeah.":
                $ LauraX.change_face("_normal",1,Eyes="_side")
                $ LauraX.change_stat("love", 90, 1)
                $ LauraX.change_stat("inhibition", 60, 2)
                $ LauraX.add_word(1,"nyx",0,0,0)
            "I'm sorry, I must have missed it.":
                $ LauraX.change_face("_confused",2)
                $ LauraX.change_stat("love", 200, -3)
                ch_l "Seriously?"
                $ LauraX.change_face("_angry",1)
            "What? Why?":
                $ LauraX.change_face("_confused",2)
                $ LauraX.change_stat("love", 200, -5)
                ch_l "Seriously?"
                $ LauraX.change_face("_angry",1)

    if "nyx" not in LauraX.recent_history:
        ch_l "Maybe you don't understand why this cuts deep. . ."
        ch_l ". . ."
        $ LauraX.change_face("_sadside",1)
        ch_l "When I was younger, on my own. . ."
        $ LauraX.change_stat("inhibition", 60, 1)
        ch_l "I had to do some things. . ."
        $ LauraX.blushing = "_blush2"
        $ LauraX.change_stat("inhibition", 60, 1)
        ch_l "On the streets."
        $ LauraX.change_face("_sad",1)
        ch_l "So I don't want to be called. . . that."

    menu:
        extend ""
        "Oh, I'm so sorry.":
            $ LauraX.change_stat("love", 200, 5)
            $ LauraX.change_face("_smile",1,Eyes="_side")
            ch_l "Thanks. . ."
            $ LauraX.change_face("_smile",1)
            $ LauraX.add_word(1,"sorry",0,0,0)
        "Yeah, I get it.":
            $ LauraX.change_stat("love", 80, 2)
            $ LauraX.change_stat("love", 200, 3)
            $ LauraX.change_stat("obedience", 80, 1)
            $ LauraX.change_stat("inhibition", 60, 1)
            $ LauraX.change_face("_smile",1)
            ch_l "Thanks."
            $ LauraX.add_word(1,"sorry",0,0,0)
        "Oh, ok.":
            if approval_check(LauraX, 1200) or approval_check(LauraX, 400, "O"):
                $ LauraX.change_stat("obedience", 60, 3)
                $ LauraX.change_stat("obedience", 90, 2)
                $ LauraX.change_stat("inhibition", 60, 3)
                $ LauraX.change_face("_sly",1)
            else:
                $ LauraX.change_stat("love", 200, -5)
                $ LauraX.change_stat("obedience", 90, 5)
                $ LauraX.change_face("_angry",1)
            ch_l ". . ."
        "Ha! Get over it.":
            $ LauraX.change_face("_angry",1)
            $ LauraX.change_stat("love", 80, -5)
            $ LauraX.change_stat("love", 200, -5)
            $ LauraX.change_stat("obedience", 80, 5)
            $ LauraX.change_stat("inhibition", 60, 5)
            ch_l "Asshole."
            $ LauraX.drain_word("sorry",1,0,0)
    menu:
        extend ""
        "Won't happen again.":
            if "sorry" not in LauraX.recent_history:
                $ LauraX.change_face("_confused",1)
                ch_l "So you're sorry then?"
                menu:
                    "Yeah, of course!":
                        $ LauraX.change_face("_smile",1)
                        $ LauraX.change_stat("love", 200, 3)
                        ch_l "Good."
                        $ LauraX.add_word(1,"sorry",0,0,0)
                    "Eh, I guess?":
                        ch_l ". . ."
                        if approval_check(LauraX, 1200) or approval_check(LauraX, 400, "O"):
                            $ LauraX.change_face("_normal",1)
                            $ LauraX.change_stat("love", 80, 2)
                            $ LauraX.change_stat("love", 200, 2)
                            $ LauraX.change_stat("obedience", 90, 2)
                            $ LauraX.change_stat("inhibition", 60, 1)
                            ch_l "Good enough."
                            $ LauraX.add_word(1,"sorry",0,0,0)
                        else:
                            $ LauraX.change_stat("love", 90, -5)
                            $ LauraX.change_stat("obedience", 90, 3)
                            $ LauraX.change_stat("inhibition", 60, 1)
                            $ LauraX.change_face("_angry",1)
                            ch_l "Not good enough."
                    "For what?":
                        $ LauraX.change_face("_angry",1)
                        $ LauraX.change_stat("love", 80, -5)
                        $ LauraX.change_stat("love", 99, -5)
                        $ LauraX.change_stat("obedience", 90, 5)
                        $ LauraX.change_stat("inhibition", 50, 5)
                        $ LauraX.change_stat("inhibition", 70, 5)
                        ch_l "Grrrrrr."
            else:
                $ LauraX.change_face("_angry",1,Mouth="_smile")
                $ LauraX.change_stat("obedience", 80, 2)
                $ LauraX.change_stat("inhibition", 60, 3)
                ch_l "It'd better not."
        "That all?":

            $ LauraX.change_face("_angry",1)
            $ LauraX.change_stat("love", 80, -5)
            $ LauraX.change_stat("love", 99, -5)
            $ LauraX.change_stat("inhibition", 60, 10)
            ch_l "Seriously?!"

    if "sorry" in LauraX.recent_history:
        $ LauraX.change_face("_smile",1)
        ch_l "I'm glad that you care, at least."
    else:
        $ LauraX.change_face("_angry",1)
        $ LauraX.add_word(1,"_angry","_angry",0,0)
        ch_l "Well if that's how you feel about it, you can fuck right off!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
