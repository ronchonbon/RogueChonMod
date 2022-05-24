


label Jubes_Meet:



    show black_screen onlayer black
    $ JubesX.today_outfit = "casual2"
    $ JubesX.outfit = "casual2"
    $ JubesX.change_outfit("casual2")
    call clear_the_room ("all", 0, 1)
    $ JubesX.location = bg_current
    $ JubesX.love = 500
    $ JubesX.obedience = 50
    $ JubesX.inhibition = 50
    $ JubesX.sprite_location = stage_center

    $ JubesX.names = []
    $ JubesX.name = "???"

    $ Player.add_word(1,"interruption")
    $ Player.focus = 30
    ch_u "\"Slurp, slurp, slurp.\""

    $ Player.change_stat("focus", 80, 5)
    $ JubesX.change_stat("lust", 80, 5)




    $ JubesX.change_face("_sucking",1)

    "You feel a pleasant sensation. . ."
    ch_u "\"Slurp, slurp, slurp.\""
    $ Player.change_stat("focus", 80, 5)
    $ JubesX.change_stat("lust", 80, 5)
    $ JubesX.addiction_rate += 1

    "It's somewhere below your waist. . ."
    ch_u "\"Slurp, slurp, slurp.\""
    $ Player.change_stat("focus", 80, 10)
    $ JubesX.change_stat("lust", 80, 5)

    "Wait . . no it's not. . ."
    call shift_focus (JubesX)

    $ JubesX.arm_pose = 2
    show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(stage_right):
        ease 0.1 offset (100,50) zoom 2.5 alpha 1
        block:
            ease 1 yoffset 100
            pause .2
            ease 1 yoffset 50
            repeat

    "You open your eyes. . ."
    hide black_screen onlayer black

    $ Count = 3
    $ line = 0
    "Someone seems to be giving you a hickey on your neck. . ."
    while Count > 0:

        $ Player.change_stat("focus", 80, 10)
        $ JubesX.change_stat("lust", 80, 5)
        menu:
            extend ""
            "Stay Quiet":
                $ JubesX.change_stat("inhibition", 90, 2)
                $ JubesX.change_stat("lust", 80, 5)
                $ JubesX.addiction_rate += 1
                if Count > 2:
                    "You just let her do her thing and pretend to still be asleep."
                    ch_v "\"Slurp, slurp, slurp.\""
                    ". . ."
                elif Count > 1:
                    "It does feel nice. . ."
                    ch_v "\"Slurp, slurp, slurp.\""
                    ". . ."
                else:
                    "You wouldn't want to disturb her. . ."
                    ch_v "\"Slurp, slurp, slurp.\""
                    show black_screen onlayer black
                    ". . ."
                    $ JubesX.change_stat("love", 90, 2)
                    $ JubesX.change_face("_surprised",2)
                    show Jubes_Sprite:
                        ease 0.2 offset (100,50) zoom 2.5 alpha 1
                    ch_v "Whoa! Um. . . this is bad. . ."
                    ch_v "Wake up! Wake up! Sorry!!!!"
                    "You slowly pull yourself back. . ."
                    hide black_screen onlayer black
                    ch_v "Sorry!"
                    show Jubes_Sprite:
                        ease 0.5 offset (100,0) zoom 1.5 alpha 1
                    ch_v "I think I maybe drained a bit too much!"
                    $ JubesX.change_face("_sadside",1)
                    ch_v "I was just. . . thirsty. . ."
            "Um. . . lady? What're you doing?":
                $ JubesX.change_stat("obedience", 90, 5)
                $ JubesX.change_stat("inhibition", 90, -1)
                $ JubesX.change_face("_surprised",2)
                show Jubes_Sprite:
                    ease 0.5 offset (100,0) zoom 1.5 alpha 1
                ch_v "Ah!"
                $ JubesX.change_face("_sadside",1,Mouth="_normal")
                ch_v "Oh, I guess I was. . ."
                $ Count = 1
            "That feels great, keep going. . .":
                $ JubesX.change_stat("love", 90, 2)
                $ JubesX.change_stat("inhibition", 90, 2)
                $ JubesX.change_face("_surprised",2)
                show Jubes_Sprite:
                    ease 0.5 offset (100,0) zoom 1.5 alpha 1
                ch_v "Oh!"
                $ JubesX.change_face("_sadside",1,Mouth="_smile")
                ch_v "I, um. . . I wasn't expecting that reaction. . ."
                $ JubesX.change_face("_sad",1,Mouth="_smile")
                $ Count = 1
            "Hey, quit that!":
                $ JubesX.change_stat("obedience", 90, 10)
                $ JubesX.change_stat("inhibition", 90, -3)
                $ JubesX.change_face("_surprised",2)
                show Jubes_Sprite:
                    ease 0.5 offset (100,0) zoom 1.5 alpha 1
                ch_v "Ah!"
                $ JubesX.change_face("_sadside",1,Mouth="_normal")
                ch_v "Sorry!"
                $ Count = 1
        $ Count -= 1
    $ JubesX.blushing = "_blush1"
    show Jubes_Sprite at sprite_location(JubesX.sprite_location,50)
    $ Count = 3
    while Count > 0:
        menu:
            extend ""
            "Who are you?" if "Jubilee" not in JubesX.names:
                $ JubesX.change_stat("love", 90, 2)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_face("_smile",1)
                ch_v "Oh, I guess I should introduce myself."
                ch_v "The name's \"Jubilee.\""
                $ JubesX.names.append("Jubilee")
                $ JubesX.name = "Jubilee"
                ch_v "Nice to ea- meet you."
                menu:
                    extend ""
                    "Ok. . .":
                        $ JubesX.change_face("_confused",1)
                        $ JubesX.change_stat("obedience", 90, 3)
                        ch_v ". . ."
                    "My name's [Player.name]":
                        $ JubesX.change_stat("love", 90, 3)
                        $ JubesX.change_stat("obedience", 90, 2)
                        ch_v "Oh, yeah, I know that."
                        $ JubesX.change_stat("inhibition", 90, 2)
                        ch_v "I've. . . heard about you."
                    "Huh.":
                        $ JubesX.change_face("_confused",1)
                        ch_v ". . ."



            "That's an interesting name." if "Jubilee" in JubesX.names and "Jubilation" not in JubesX.names:

                $ JubesX.change_face("_smile",1)
                ch_v "Oh, yeah. Weird parents."
                ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
                ch_v "Guess I leaned into it?"
                $ JubesX.names.append("Jubilation")
                $ JubesX.names.append("Miss Lee")
                $ JubesX.petnames.append("Miss Lee")
                menu:
                    extend ""
                    "Yeah, sure.":
                        $ JubesX.change_stat("love", 90, 1)
                        $ JubesX.change_stat("obedience", 90, 3)
                        ch_v ". . ."
                    "It suits you.":
                        $ JubesX.change_stat("love", 90, 5)
                        $ JubesX.change_stat("inhibition", 90, 2)
                        ch_v ". . ."
                    "Weird.":
                        $ JubesX.change_face("_angry",1)
                        $ JubesX.change_stat("love", 90, -3)
                        $ JubesX.change_stat("obedience", 90, 3)
                        $ JubesX.change_stat("inhibition", 90, 1)
                        ch_v ". . ."
                        $ JubesX.change_face("_normal",1)



            "What are you doing in my room?!" if "thirst" not in JubesX.recent_history:
                $ JubesX.change_stat("love", 90, -1)
                $ JubesX.change_stat("obedience", 90, 7)
                $ JubesX.change_stat("inhibition", 90, -2)
                $ JubesX.change_face("startled",2)
                ch_v "Oh, I was just. . . thirsty?"
                $ JubesX.change_face("_smile",1)
                $ JubesX.add_word(1,"thirst",0,0,0)


            "What were you doing?" if "thirst" not in JubesX.recent_history:
                $ JubesX.change_stat("inhibition", 90, 1)
                $ JubesX.change_face("startled",2)
                ch_v "I was just. . . getting a drink?"
                $ JubesX.change_face("_smile",1)
                $ JubesX.add_word(1,"thirst",0,0,0)




            "So you drink blood?" if "vamp" in JubesX.recent_history and "blood" not in JubesX.recent_history:
                $ JubesX.change_stat("love", 90, 1)
                $ JubesX.change_face("_sadside",2)
                ch_v "Yeah, I kinda have to. . ."
                $ JubesX.change_face("_sad",1)
                ch_v "Sorry again. . ."
                $ JubesX.add_word(1,"blood",0,0,0)
            "Can you turn into a bat?" if "vamp" in JubesX.recent_history and "bat" not in JubesX.recent_history:
                $ JubesX.change_stat("love", 90, 1)
                $ JubesX.change_face("_confused",1)
                ch_v "Well, no. . ."
                $ JubesX.change_face("_sly",1)
                ch_v "But I am strong and can turn into mist."
                ch_v "Sometimes."
                $ JubesX.add_word(1,"bat",0,0,0)
            "Is it contagious?" if "vamp" in JubesX.recent_history and "contagious" not in JubesX.history:
                $ JubesX.change_face("_sadside",2)
                ch_v "Infectious. . ."
                $ JubesX.change_face("_surprised",1,Mouth="_sucking")
                ch_v "- and no!"
                $ JubesX.change_face("_sadside",1)
                ch_v "It was, but Dr. Strange was able to cast a spell or something."
                ch_v "So you don't need to worry about it spreading to you or anything."
                $ JubesX.change_face("_sad",1)
                $ JubesX.add_word(1,0,0,0,"contagious")
            "Why me?" if "vamp" in JubesX.recent_history and "devamp" not in JubesX.recent_history:
                $ JubesX.change_stat("love", 90, 1)
                $ JubesX.change_face("_sly",1,Eyes="_side")
                ch_v "Well. . ."
                ch_v "I had a theory. . ."
                ch_v "I sorta figured that if you could negate powers, then maybe. . ."
                $ JubesX.change_face("_smile",1)
                ch_v "Maybe you could \"de-vampire\" me?"
                $ JubesX.add_word(1,"devamp",0,0,0)
                menu:
                    extend ""
                    "You don't want to be a vampire":
                        $ JubesX.change_stat("love", 90, 2)
                        $ JubesX.change_stat("obedience", 90, 1)
                        ch_v "Well, no. . ."
                    "I guess.":
                        $ JubesX.change_face("_confused",1)
                        $ JubesX.change_stat("love", 90, -1)
                        ch_v ". . ."
                ch_v "The powers are cool and all, but I can't even go out during the daytime!"
                ch_v "and the blood drinking, of course."
                $ JubesX.change_face("_normal",1)

                menu:
                    extend ""
                    "Of course.":
                        $ JubesX.change_stat("love", 90, 2)
                        $ JubesX.change_stat("inhibition", 90, 1)
                        ch_v ". . ."
                    "Yeah. . .":
                        $ JubesX.change_stat("obedience", 90, 1)
                        $ JubesX.change_stat("inhibition", 90, 1)
                        ch_v ". . ."


            "Are you a mutant?" if "mutant" not in JubesX.recent_history:
                $ JubesX.change_stat("love", 90, 2)
                $ JubesX.change_face("_smile",1)
                ch_v "Yeah! Of course I am!"
                $ JubesX.change_face("_smile",1,Eyes="_side")
                if "vamp" in JubesX.recent_history:
                    ch_v "You know, among other things. . ."
                else:
                    ch_v ". . . among other things. . ."
                $ JubesX.add_word(1,"mutant",0,0,0)
                menu:
                    extend ""
                    "So what's your power?":
                        $ JubesX.change_stat("love", 90, 3)
                        $ JubesX.change_stat("inhibition", 90, 1)
                        ch_v ". . ."
                    "Oh, ok.":
                        $ JubesX.change_stat("love", 90, -1)
                        $ JubesX.change_stat("obedience", 90, 3)
                        $ JubesX.change_face("_confused",1)
                        ch_v "Not even curious about what I can do?"
                $ JubesX.change_face("_smile",1)
                ch_v "I can shoot fireworks."
                $ JubesX.arm_pose = 1
                show Fireworks as Fire1 onlayer black:
                    pos (JubesX.sprite_location+300,350)
                show Fireworks as Fire2 onlayer black:
                    pos (JubesX.sprite_location+300,350)
                ch_v "Pew pew!"
                menu:
                    extend ""
                    "Neat!":
                        $ JubesX.change_stat("love", 90, 3)
                        $ JubesX.change_stat("inhibition", 90, 5)
                        ch_v "Thanks!"
                    "K.":
                        $ JubesX.change_stat("obedience", 90, 2)
                        $ JubesX.change_stat("inhibition", 90, -1)
                        $ JubesX.change_face("_angry",1,Eyes="_side")
                        ch_v "Ok, so it's not \"negating mutant powers\" cool or anything. . ."
                        ch_v "I can do other stuff. . ."
                        $ JubesX.change_face("_normal",1)
                    ". . .":
                        $ JubesX.change_stat("obedience", 90, 2)
                        ch_v ". . ."
            "Well, I guess I'm out of questions.":


                $ JubesX.add_word(1,"thirst",0,0,0)
                $ Count = 0

        if "thirst" in JubesX.recent_history and "vamp" not in JubesX.recent_history:
            "You feel a tickle on your neck and rub it, coming back with a trickle of blood on your fingers."
            menu:
                extend ""
                "Oh. Blood. . .":
                    $ JubesX.change_stat("love", 90, 2)
                    $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.change_stat("inhibition", 90, -2)
                    $ JubesX.change_face("_angry",1,Eyes="_squint",Mouth = "_kiss")
                    ch_v "You are -remarkably- chill about this."
                    $ JubesX.change_face("_smile",1,Eyes="_surprised", Brows = "_sad")
                    ch_v "Maybe I took too much? . ."
                "Why is my neck bleeding?":
                    $ JubesX.change_stat("love", 90, 4)
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_face("_sadside",1)
                    ch_v "Yeah. . . about that. . ."
                    ch_v "Sorry."
                "What the fuck?!":
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("obedience", 90, 10)
                    $ JubesX.change_stat("inhibition", 90, -2)
                    $ JubesX.change_face("startled",2)
                    ch_v "Sorry! Sorry!"
                    $ JubesX.change_face("startled",1)
                    ch_v "Let me explain!"
            $ JubesX.change_face("_sadside",1)
            ch_v "So. . . I'm. . . a vampire?"
            $ JubesX.add_word(1,"vamp",0,0,0)
            menu:
                extend ""
                "This isn't a refreshment stand!":
                    $ JubesX.change_stat("love", 90, 1)
                    $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.change_stat("inhibition", 90, 1)
                    $ JubesX.change_face("_sly",1)
                    ch_v "Says you."
                "A vampire. . .":
                    ch_v ". . . Yeah. . ."
                "Oh. Gotcha.":
                    $ JubesX.change_stat("love", 90, 2)
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("inhibition", 90, -1)
                    $ JubesX.change_face("_perplexed",1)
                    ch_v "Maybe we should take you to the medbay. . ."
            $ Count += 1





    if "Jubilee" not in JubesX.names:
        $ JubesX.change_stat("love", 90, -5)
        $ JubesX.change_stat("obedience", 90, 10)
        $ JubesX.change_face("_angry",1)
        ch_v "Seriously? You don't even want to know my fucking name?"
        $ JubesX.change_face("_sadside",1,Brows="_angry")
        ch_v "How many girls do you have going through this place?"
        ch_v ". . ."
        $ JubesX.change_face("_angry",1)
        ch_v "It's \"Jubilee,\" b-t-dubs."
        menu:
            extend ""
            "Where's a jubliee?":
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_stat("inhibition", 90, 1)
                ch_v "My -name- is Jubilee, dumbass."
            "Your name? Ok.":
                $ JubesX.change_stat("love", 90, 3)
                $ JubesX.change_stat("obedience", 90, 5)
                $ JubesX.change_stat("inhibition", 90, 15)
                $ JubesX.change_face("_smile",1)
                ch_v "You catch on quick. . ."
            "Most nights are, yeah.":
                $ JubesX.change_face("_confused",1)
                ch_v "Wha. . . oh."
                $ JubesX.change_stat("love", 90, 10)
                $ JubesX.change_stat("obedience", 90, 5)
                $ JubesX.change_stat("inhibition", 90, 15)
                $ JubesX.change_face("_smile",1)
                ch_v "Heh."
                ch_v "Ok, that's cool. No, I meant my -name- is Jubilee."
                ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
        $ JubesX.name = "Jubilee"
        $ JubesX.names.append("Jubilation")
        $ JubesX.names.append("Miss Lee")
        $ JubesX.petnames.append("Miss Lee")
        ch_v "And I know your name's [Player.name], obviously."
    if "devamp" not in JubesX.recent_history:
        $ JubesX.change_face("_sadside",1)
        ch_v "Anyway, I just figured that maybe your blood could reverse this \"vampire\" thing."
    menu:
        extend ""
        "So do you feel any different?":
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("inhibition", 90, 2)
            $ JubesX.change_face("_smile",1)
        ". . .":
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("obedience", 90, 2)
            $ JubesX.change_face("_perplexed",1)
            ch_v "You don't even want to ask about the \"vampire\" thing?"
            menu:
                extend ""
                "Oh, yeah, how are you doing?":
                    $ JubesX.change_stat("love", 90, 1)
                    $ JubesX.change_stat("inhibition", 90, 1)
                    $ JubesX.change_face("_smile",1)
                "Not really.":
                    $ JubesX.change_stat("love", 90, -3)
                    $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.change_face("_angry",1)
                    ch_v "Well that's a bad start!"
                "Oh, ok.":
                    $ JubesX.change_face("_confused",1)
                    ch_v ". . ."

    ch_v "I guess. . . not that much different."
    ch_v "Still have the teeth, the. . . thirst."
    $ JubesX.change_face("_sadside",1)
    ch_v "I guess I'm still a vampire."
    $ JubesX.change_face("_normal",1)
    ch_v "But I do feel a bit better. . ."
    $ JubesX.change_face("_sad",1)
    ch_v "I am sorry, I shouldn't have attacked you like that."
    ch_v "Not cool, I know."
    menu:
        extend ""
        "It's ok, I get it.":
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 90, -1)
            $ JubesX.change_stat("inhibition", 90, 2)
            $ JubesX.change_face("_smile",1)
            ch_v "Thanks."
            ch_v "Is there any way I could make it up to you?"
        "Why not make it up to me?":
            $ JubesX.change_stat("obedience", 90, 2)
            $ JubesX.change_face("_sexy",1)
            ch_v "Oh?"
        "How dare you!":
            $ JubesX.change_stat("obedience", 90, 3)
            $ JubesX.change_stat("inhibition", 90, -1)
            $ JubesX.change_face("_surprised",1)
            ch_v "I know! I know!"
            $ JubesX.change_face("_smile",1)
            ch_v "I can make it up to you!"
        ". . .":
            $ JubesX.change_stat("inhibition", 90, 3)
            $ JubesX.change_face("_sly",1)
            ch_v "So. . . I guess I could make it up to you?"
    menu:
        extend ""
        "That's not necessary.":
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("inhibition", 90, 1)
            $ JubesX.change_face("_smile",1)
            ch_v "That's sweet of you."
            ch_v "Seriously though, I'll think of something. . ."
        "A kiss, maybe?":
            $ JubesX.change_stat("love", 90, 3)
            $ JubesX.change_stat("obedience", 90, 3)
            $ JubesX.change_stat("inhibition", 90, 2)
            $ JubesX.change_face("_sly",1)
            ch_v "I heard you're a charmer."
            ch_v "Well, I guess. . . one. . ."
            $ JubesX.change_face("_kiss")
            show Jubes_Sprite:
                ease 0.5 offset (0,0) zoom 2
            pause 1
            show Jubes_Sprite:
                ease 0.5 offset (100,0) zoom 1.5
            $ JubesX.change_face("_sly",1)
            ch_v ". . ."
        "You could flash me?":
            $ JubesX.change_stat("obedience", 90, 3)
            if approval_check(JubesX, 620):
                $ JubesX.change_stat("love", 90, 2)
                $ JubesX.change_stat("inhibition", 90, 1)
                $ JubesX.change_face("_sly",1)
                ch_v "I guess I could. . ."
                $ JubesX.change_face("_smile",1,Mouth="_sucking")
            else:
                $ JubesX.change_stat("love", 90, -2)
                $ JubesX.change_stat("obedience", 90, 1)
                $ JubesX.change_face("_angry",1,Mouth="_sucking")
            $ JubesX.arm_pose = 1
            show Fireworks as Fire1 onlayer black:
                pos (JubesX.sprite_location+250,350)
            show Fireworks as Fire2 onlayer black:
                pos (JubesX.sprite_location+250,350)
            ch_v "As if."
            $ JubesX.change_face("_smile",1)
        "A blowjob?":

            if approval_check(JubesX, 620):
                $ JubesX.change_stat("love", 90, 1)
                $ JubesX.change_stat("obedience", 90, 5)
                $ JubesX.change_stat("inhibition", 90, 1)
                $ JubesX.change_face("_smile",1,Mouth="_sucking")
            else:
                $ JubesX.change_stat("love", 90, -5)
                $ JubesX.change_stat("obedience", 90, 2)
                $ JubesX.change_face("_angry",1,Mouth="_sucking")

            ch_v "Hey, I may suck more than most, but even I'm not that easy!"
            $ JubesX.change_face("_smile",1)
    ch_v "Anyway, I should get going before dawn."
    ch_v "I might see you around sometime."
    ch_v "In the moonlight. . ."

    $ JubesX.add_word(1,0,0,0,"met")
    $ active_Girls.append(JubesX) if JubesX not in active_Girls else active_Girls
    hide Jubes_Sprite with easeoutright
    call remove_girl (JubesX)
    "[JubesX.name] leaves the room, you might as well get some sleep. . ."
    return





label Jubes_Sunshine:

    call shift_focus (JubesX)
    $ bg_current = "bg_campus"
    $ JubesX.location = "bg_campus"
    call clear_the_room (JubesX, 0, 1)
    call alternate_clothes (JubesX, 1)
    call set_the_scene
    $ JubesX.change_face("_smile")
    "On your way across the square, you see a shape charging toward you."
    call Punch
    "[JubesX.name] crashes into you."
    $ JubesX.change_face("_smile",1,Mouth="_sucking")
    ch_v "Hey, [Player.name]!"
    $ JubesX.change_face("_smile",1)
    ch_v "Check it out!"
    menu:
        extend ""
        "Oh, hey. . .":
            $ JubesX.change_stat("love", 90, 2)
            $ JubesX.change_face("_smile",1,Mouth="_sucking")
            ch_v "Yes, \"hey,\" but I am -outside!-"
            $ JubesX.change_stat("inhibition", 90, 2)
            $ JubesX.change_face("_smile",1)
            ch_v "During the daytime!"
        "You're out during the day!":
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("inhibition", 90, 2)
        "Check what out?":
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("obedience", 90, 2)
            ch_v "Look!"
            ch_v "I'm -outside!-"
            $ JubesX.change_stat("inhibition", 90, 2)
            $ JubesX.change_face("_smile",1,Mouth="_sucking")
            ch_v "During the -daytime!-"
            $ JubesX.change_face("_smile")
        "What the hell?":
            $ JubesX.change_stat("love", 90, -3)
            $ JubesX.change_stat("obedience", 90, 5)
            $ JubesX.change_face("_surprised",2,Mouth="_sucking")
            ch_v "Sorry! I was just so excited!"
            $ JubesX.change_face("_smile",1)
            ch_v "I'm outside, during the daylight!"
    menu:
        extend ""
        "That's great!":
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 90, 1)
            $ JubesX.change_face("_surprised",1,Mouth="_sucking")
            ch_v "Right?!"
            $ JubesX.change_face("_smile",1)
        "So what? So am I.":
            $ JubesX.change_stat("love", 90, -5)
            $ JubesX.change_stat("obedience", 90, 5)
            $ JubesX.change_face("_confused",1)
            ch_v "Yes. . ."
            ch_v "But I am a -vampire,- remember?"
        "Ok.":
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("inhibition", 90, 2)
            $ JubesX.change_face("_confused",1)
            ch_v ". . . I'm a -vampire?-"
    $ JubesX.change_face("_surprised",1,Mouth="_sucking")
    ch_v "I didn't used to be able to do this without catching fire!"
    $ JubesX.change_face("_smile",1)
    menu:
        extend ""
        "So do you know why?":
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 90, 1)
        "Well it was never a problem for me.":
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("obedience", 90, 3)
            $ JubesX.change_face("_confused",1)
            ch_v ". . ."
            ch_v "No, I get that it wouldn't be. . ."
            $ JubesX.change_face("_normal",1)
        "Neat.":
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 90, 1)
            $ JubesX.change_face("_confused",1)
            ch_v ". . ."
            $ JubesX.change_face("_normal",1)
        "Ok.":
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 90, 2)
            $ JubesX.change_face("_angry",1)
            ch_v ". . ."
            $ JubesX.change_face("_normal",1)
    ch_v "I don't really know what caused it, but I guess it had to do with your blood. . ."
    $ JubesX.change_face("_smile",1)
    ch_v "Anyway, I just wanted to say \"thank you,\" this is great!"
    $ JubesX.add_word(1,0,0,0,"sunshine")
    hide Jubes_Sprite with easeoutright
    call remove_girl (JubesX)
    "[JubesX.name] dashes off, and you continue on your way. . ."
    return





label check_on_Jubes_sunshock:
    if JubesX not in Party:
        return

    call is_Jubes_sunshocked

    if _return:
        menu:
            "Ok then, we can stay here.":
                if "stayed" in JubesX.recent_history:
                    $ JubesX.change_stat("love", 80, -2)

                    ch_v "Now I kind feel like you're jerking me around. . ."
                elif approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    ch_v "That's really not necessary, don't let me hold you back."

                    menu:
                        extend ""
                        "I insist.":
                            $ JubesX.change_face("_smile",1)
                            $ JubesX.change_stat("love", 80, 2)
                            $ JubesX.change_stat("inhibition", 60, 2)

                            ch_v "Aw, thanks. That's sweet of you."
                        "Ok, sorry about that.":
                            $ JubesX.change_stat("obedience", 90, 2)
                            $ JubesX.change_face("_sad",1)

                            $ Party.remove(JubesX)

                            "You leave her behind."

                            return
                        "Cool, later then.":
                            $ JubesX.change_stat("love", 80, -2)
                            $ JubesX.change_stat("obedience", 90, 2)
                            $ JubesX.change_face("_sad",1)

                            $ Party.remove(JubesX)

                            "You leave her behind."

                            return
                else:
                    ch_v "Thanks, that's sweet of you."

                $ JubesX.add_word(1,"stayed",0,0,0)

                jump Misplaced
            "Oh, too bad, you can stay here then.":
                $ Party.remove(JubesX)

                $ JubesX.change_stat("love", 80, -2)
                $ JubesX.change_stat("obedience", 70, 2)

                if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_face("_sad",1)

                    ch_v "I understand, later then. . ."
                else:
                    $ JubesX.change_stat("love", 80, -4)
                    $ JubesX.change_face("_angry",1,Mouth="_sucking")

                "You leave her behind."

                $ JubesX.change_face("_sad",1)

    return

label is_Jubes_sunshocked:
    if JubesX.addiction <= 50 or time_index > 2:
        return False

    $ JubesX.change_face("_sad",1)

    if "sunshock" in JubesX.recent_history:
        ch_v "Like I said, I'm not up for the sunshine."

        return True

    $ JubesX.add_word(1,"sunshock",0,0,0)

    ch_v "Oh, wait, I'm kinda on a \"low charge\" at the moment, so I don't really want to go out in the sunlight?"

    menu:
        extend ""
        "Oh, sorry, that's fine.":
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 90, 1)
            $ JubesX.change_face("_smile",1)

            ch_v "Thanks for understanding. . ."

            return True
        "I could always. . . come get you?" if bg_current != JubesX.location and JubesX not in Party:
            ch_v "Oh, that could be nice. I'll see you then."

            return True
        "I could always. . . top you off?" if bg_current == JubesX.location or JubesX in Party:
            $ JubesX.change_stat("love", 80, 1)
            $ JubesX.change_face("_confused",1)

            ch_v "Oh? What'd you have in mind?"

            $ menu_context = "sunshock"

            call addiction_ultimatum_menu

            if JubesX.addiction >= 70:
                $ JubesX.change_stat("inhibition", 70, 1)
                $ JubesX.change_stat("inhibition", 80, 1)

                ch_v "Couldn't I just touch you real quick?"

                menu:
                    extend ""
                    "Sure.":
                        $ Girl.change_stat("lust", 80, 3)
                        $ Girl.change_stat("love", 80, 6)
                        $ Girl.change_face("_smile")

                        call Girl_Tag (Girl)
                    "Nope, sorry.":
                        $ JubesX.change_stat("love", 80, -3)
                        $ JubesX.change_stat("obedience", 70, 2)

                        if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                            $ JubesX.change_face("_sad",1)

                            ch_v "Oh."
                        else:
                            $ JubesX.change_stat("love", 90, -2)
                            $ JubesX.change_stat("obedience", 90, 2)
                            $ JubesX.change_face("_angry",1)

                            ch_v "Jerk."

            if JubesX.addiction >= 70:
                if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    $ JubesX.change_face("_sad",1)

                    ch_v "I'm sorry, I just can't, it would be agonizing."
                else:
                    $ JubesX.change_face("_angry",1)

                    ch_v "You have to be kidding! I'd catch fire!"

                return True
            elif approval_check(JubesX, 1600) or approval_check(JubesX, 500, "O"):
                $ JubesX.change_stat("obedience", 90, 2)
                $ JubesX.change_stat("inhibition", 80, 2)

                ch_v "I guess I could manage it for a little bit. . ."
            else:
                ch_v "Grow up. . ."

                return True
        "Come on, don't be like that.":
            $ JubesX.change_stat("love", 70, -2)
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("obedience", 90, 2)
            $ JubesX.change_face("_sad",1)

            if JubesX.addiction >= 70:
                if approval_check(JubesX, 1300) or approval_check(JubesX, 400, "O"):
                    $ JubesX.change_stat("obedience", 90, 2)

                    ch_v "I'm sorry, I just can't, it would be agonizing."
                else:
                    $ JubesX.change_face("_angry",1)

                    ch_v "You have to be kidding! I'd catch fire!"

                return True
            elif approval_check(JubesX, 1600) or approval_check(JubesX, 500, "O"):
                $ JubesX.change_stat("obedience", 90, 2)
                $ JubesX.change_stat("inhibition", 80, 2)

                ch_v "I guess I could manage it for a little bit. . ."
            else:
                ch_v "Grow up. . ."

                return True

    return False


label Jubes_Mall(temp_Girls=[]):


    call shift_focus (JubesX)
    if JubesX.location == bg_current:
        "[JubesX.name] suddently freezes up, then turns to you."
    else:
        $ JubesX.location = bg_current
        "[JubesX.name] rushes into the room."
    call clear_the_room (JubesX, 0, 0)
    call set_the_scene
    $ Player.add_word(1,0,0,0,"mall")

    $ JubesX.change_face("_surprised",1,Mouth="_sucking")
    ch_v "Hey, I just realized something!"
    $ JubesX.change_face("_smile")
    menu:
        extend ""
        "Cool.":
            $ JubesX.change_stat("love", 80, 1)
        "Oh, what?":
            $ JubesX.change_stat("love", 90, 2)
            $ JubesX.change_stat("inhibition", 60, 1)
        "Uh-huh.":
            $ JubesX.change_stat("love", 80, -1)
            $ JubesX.change_stat("obedience", 50, 1)
            $ JubesX.change_stat("obedience", 60,1)
            $ JubesX.change_stat("inhibition", 50, -1)
            $ JubesX.change_face("_angry",1,Mouth="_sucking")
            ch_v "This is serious!"
        ". . .":
            $ JubesX.change_stat("love", 90, -1)
            $ JubesX.change_face("_confused")
            ch_v "Aren't you going to ask me \"what?\""
            menu:
                extend ""
                "Oh, sure, what?":
                    $ JubesX.change_stat("love", 90, 2)
                    $ JubesX.change_stat("obedience", 50, 1)
                    $ JubesX.change_stat("inhibition", 50, 1)
                "No.":
                    $ JubesX.change_stat("love", 80, -2)
                    $ JubesX.change_stat("obedience", 70, 2)
                    $ JubesX.change_stat("inhibition", 30, -1)
                    $ JubesX.change_face("_angry")
                    ch_v "Dick."
                ". . .":
                    $ JubesX.change_stat("love", 90, -1)
                    $ JubesX.change_stat("obedience", 60, 1)
                    ch_v "Ooookaaay. . ."
    $ JubesX.change_face("_surprised",1,Mouth="_sucking")
    ch_v "Now that I can go out during the daytime, I can go to the mall again!!"
    menu:
        extend ""
        "That's great!":
            $ JubesX.change_stat("love", 90, 5)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_stat("inhibition", 90, 1)
            ch_v "I know, right?"
            menu:
                extend ""
                "Wait, there's a mall?":
                    $ JubesX.change_stat("love", 80, 1)
                    $ JubesX.change_stat("inhibition", 70, 1)
                    $ JubesX.change_face("_confused")
                    ch_v "Of course there's a mall! What town doesn't have a mall?!"
                "Did you want to go?":
                    $ JubesX.change_stat("love", 80, 2)
                    $ JubesX.change_stat("love", 90, 1)
                    $ JubesX.change_stat("inhibition", 70, 1)
        "Oh, ok.":
            $ JubesX.change_stat("love", 90, -1)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_face("_sad")
        "Wait, there's a mall?":
            $ JubesX.change_stat("love", 80, 1)
            $ JubesX.change_stat("inhibition", 70, 1)
            $ JubesX.change_face("_confused")
            ch_v "Of course there's a mall! What town doesn't have a mall?!"
        "Ok, whatever.":
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("obedience", 50, 2)
            $ JubesX.change_stat("obedience", 90, 2)
            $ JubesX.change_stat("inhibition", 50, -1)
    $ JubesX.change_face("_surprised",1,Mouth="_sucking")
    ch_v "We've got to go there, right now!"
    $ JubesX.change_face("_smile")
    $ Party = [JubesX]
    menu:
        "Ok, let's check it out.":
            $ JubesX.change_stat("love", 80, 2)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            show black_screen onlayer black with dissolve
            "You both head out of the room."
        "You can go, I don't need anything.":
            $ JubesX.change_stat("love", 80, 2)
            $ JubesX.change_stat("obedience", 60, 1)
            $ JubesX.change_stat("obedience", 80, 1)
            ch_v "Come'on, you gotta go!"
            ch_v "You don't know what you're missing!"
            show black_screen onlayer black with dissolve
            "[JubesX.name] can be surprisingly forceful. . ."
        "Nah.":
            $ JubesX.change_stat("love", 50, -2)
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("inhibition", 50, 2)
            $ JubesX.change_stat("inhibition", 60, 2)
            $ JubesX.change_face("_angry",1,Mouth="_sucking")
            ch_v "Stow the 'tude, we're going!"
            $ JubesX.change_face("_smile")
            show black_screen onlayer black with dissolve
            "[JubesX.name] can be surprisngly forceful. . ."
        "Actually, I planned to-":
            $ JubesX.change_stat("love", 50, -1)
            $ JubesX.change_stat("love", 90, -1)
            $ JubesX.change_stat("inhibition", 50, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            $ JubesX.change_face("_surprised",1,Mouth="_sucking")
            ch_v "No time! We're going!"
            $ JubesX.change_face("_smile")
            show black_screen onlayer black with dissolve
            "[JubesX.name] can be surprisngly forceful. . ."
    "You arrive at what appears to be a mid-sized suburban shopping complex, often referred to as a \"mall.\""

    $ bg_current = "bg_mall"
    $ JubesX.location = bg_current
    call clear_the_room (JubesX, 0, 1)
    call set_the_scene

    $ JubesX.change_face("_smile")
    ch_v "Welcome to the Salem Centre Mall!"
    ch_v "It's open dawn to dusk, which is why I wasn't able to get here for a while. . ."
    ch_v "It's got a -ton- of different shops, although I guess not all of them would be very interesting to you."
    $ line = 0
    $ temp_Girls = all_Girls[:]
    while temp_Girls and not line:
        if temp_Girls[0].went_on_date:
            $ line = 1
        $ temp_Girls.remove(temp_Girls[0])
    if line:

        "You realize that the local movie theater is actually at one end of the mall."
        "And the restaurant you often go to is at the other end."
        "How did you not notice the mall in between before? . ."
        menu:
            "Selective amnesia":
                "Oh, yeah, probably."
            "I'm not very bright":
                "True, true."
            "Probably a retcon":
                "It happens."
    else:

        "You see a movie theater is at one end of the mall, and a nice looking restaurant is at the other end."
        "Maybe you should take people to these places. . ."
    ch_v "And you haven't been here before?"
    menu:
        extend ""
        "Apparently not.":
            pass
        "I think I've been close. . .":
            pass
        "Nope.":
            $ JubesX.change_stat("love", 70, -1)
    $ JubesX.change_face("_confused",1)
    ch_v "Weird."
    ch_v "Anyway, I spent a -ton- of time at the mall when I was a kid."
    $ JubesX.change_face("_sadside")
    ch_v "I'd run away from foster care, and just camped out in closed stores. . ."
    ch_v "It was better than being on the street, at least."
    menu:
        extend ""
        "That's rough.":
            $ JubesX.change_stat("love", 80, 3)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("obedience", 50, 1)
        "That must have been hard for you.":
            $ JubesX.change_stat("love", 60, 5)
            $ JubesX.change_stat("love", 80, 3)
            $ JubesX.change_stat("love", 90, 1)
        "I guess.":
            $ JubesX.change_stat("love", 70, -1)
            $ JubesX.change_stat("love", 90, -1)
            $ JubesX.change_stat("obedience", 50, 1)
            $ JubesX.change_stat("inhibition", 50, 1)
            $ JubesX.change_face("_confused",1)
            ch_v ". . ."
        "Free food court, uh?":
            $ JubesX.change_stat("love", 70, 1)
            $ JubesX.change_stat("inhibition", 60, 1)
            $ JubesX.change_face("_smile",1,Eyes="_side")
            ch_v "When I could get into a restaurant, yeah. . ."
            $ JubesX.change_stat("love", 70, -2)
            $ JubesX.change_stat("love", 90, -1)
            $ JubesX.change_stat("obedience", 80, 1)
            $ JubesX.change_face("_angry",1)
            ch_v ". . ."

    ch_v "Yeah, but it was ok. . ."
    $ JubesX.change_face("_smile",Eyes="_side")
    ch_v "Anyway, then I bumped into some of the other Xavier's students and found my way to the school."
    $ JubesX.change_face("_smile")
    ch_v "Xavier agreed to take me in there, and it's worked out much better."
    $ JubesX.change_face("_sadside")
    ch_v "Until the whole \"vampire\" thing at least."
    menu:
        "Yeah, about that. . .":
            $ JubesX.change_stat("obedience", 30, 1)
            $ JubesX.change_stat("obedience", 60, 1)
        "Yeah, I bet.":
            $ JubesX.change_stat("love", 80, 2)
        "Uh-huh.":
            $ JubesX.change_stat("love", 90, -2)
            $ JubesX.change_stat("obedience", 90, 1)
            $ JubesX.change_face("_angry")
            ch_v ". . ."
    $ JubesX.change_face("_smile")
    ch_v "So anyways. . . now that we're here, did you want to go shopping?"
    menu:
        "Sure, let's look around.":
            $ JubesX.change_stat("love", 60, 5)
            $ JubesX.change_stat("love", 80, 3)
            $ JubesX.change_stat("love", 90, 1)
            $ JubesX.change_stat("inhibition", 50, 1)
            ch_v "Cool."
            call Shopping_Mall
        "Nah, we can head back now.":
            $ JubesX.change_stat("love", 60, -3)
            $ JubesX.change_stat("love", 80, -2)
            $ JubesX.change_stat("love", 90, -1)
            $ JubesX.change_stat("inhibition", 90, 1)
            $ JubesX.change_face("_sad")
            ch_v "Aw, ok. At least I can come here when I want now. . ."
            $ JubesX.change_stat("obedience", 50, 3)
            $ JubesX.change_stat("obedience", 90, 2)

    "You both head back to campus."
    $ bg_current = "bg_campus"
    $ JubesX.location = bg_current
    call clear_the_room (JubesX, 0, 1)
    call set_the_scene
    ch_v "Anyway, it was nice to hang out with you."
    ch_v "I hope we can do it again some time!"
    jump Misplaced
    return



label Jubes_Key:
    call set_the_scene
    $ JubesX.change_face("_bemused")
    ch_v "Oh, um. . ."
    ch_v "We've been sleeping together for a bit and. . ."
    ch_v "Here."
    "She takes your hand and hands you her room key."
    $ keys.append(JubesX)
    $ JubesX.event_happened[0] = 1
    ch_p "Thanks."
    return






label Jubes_BF(temp_Girls=[]):
    call shift_focus (JubesX)
    if JubesX.location != bg_current:
        $ JubesX.location = bg_current
        if JubesX not in Party:
            "[JubesX.name] approaches you and motions that she wants to speak to you alone."
        else:
            "[JubesX.name] turns towards you and motions that she wants to speak to you alone."
    $ JubesX.drain_word("asked_to_meet")
    call set_the_scene (0)
    call display_girl (JubesX)
    "She looks a bit concerned and you can tell she's a bit anxious about whatever she has to say."
    call taboo_level
    call clear_the_room (JubesX)
    $ JubesX.daily_history.append("relationship")
    $ JubesX.change_face("_angry",1,Eyes="_side")
    $ line = 0
    ch_v "Hey. So. [JubesX.player_petname]. . ."
    $ JubesX.change_face("_confused",1,Mouth="_lipbite")
    ch_v "I don't know- . . . you're pretty fun to hang out with, ya know?"
    menu:
        extend ""
        "I really love hanging out with you too!":
            $ JubesX.change_face("_surprised",2)
            ch_v "Right, so-"
            $ JubesX.change_stat("obedience", 50, -3)
            $ JubesX.change_stat("inhibition", 80, 1)
            ch_v ". . ."
            $ JubesX.change_stat("love", 200, 5)
            $ JubesX.change_face("_bemused",1,Eyes="_side")
            ch_v "\"Love\" is kind of a strong word, [JubesX.player_petname]."
        "Yeah, sure, it's a lot of fun.":
            $ JubesX.change_stat("love", 200, 10)
            $ JubesX.change_stat("inhibition", 80, 2)
            $ JubesX.change_face("_smile",0)
            ch_v "Right?"
        "I mean, it beats math class. . .":
            $ JubesX.change_stat("love", 200, 3)
            $ JubesX.change_stat("obedience", 80, 3)
            $ JubesX.change_stat("inhibition", 80, -3)
            $ JubesX.change_face("_angry",1)
            ch_v "Um, less enthusiasm than I was expecting. . ."
        "If you say so.":
            $ JubesX.change_stat("obedience", 80, 6)
            $ JubesX.change_stat("inhibition", 80, -8)
            $ JubesX.change_face("_confused",1)
            ch_v ". . ."

    ch_v "So like I was saying, I don't exactly have a ton of friends."
    $ JubesX.change_face("_sadside",1)
    ch_v "I kind of grew up in a rough place, and then spent a lot of time on the road."
    ch_v "I had a life before coming here."
    menu:
        extend ""
        "What was it like?":
            $ JubesX.change_stat("love", 200, 7)
            $ JubesX.change_stat("obedience", 80, 2)
            $ JubesX.change_stat("inhibition", 80, 3)
            $ JubesX.change_face("_sad",1,Mouth="_lipbite")
        "Yeah? I know.":
            $ JubesX.change_stat("love", 200, 3)
            $ JubesX.change_stat("obedience", 80, 4)
            $ JubesX.change_stat("inhibition", 80, 1)
            $ JubesX.change_face("_confused",1,Mouth="_lipbite")
        "I don't need a lot of backstory drama.":
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 80, 10)
            $ JubesX.change_stat("inhibition", 80, -5)
            $ JubesX.change_face("_angry",1)
            $ line = "bad"
            ch_v "Fine!"
            ch_v "\"Keep it simple\" it is then."
            ch_v "I don't hate hanging out with you, is all."
    if line != "bad":
        $ JubesX.change_face("_normal",1,Eyes="_side")
        ch_v "Well, you may have guessed I'm related to Wolverine."
        menu:
            extend ""
            "Kinda obvious, yeah.":
                $ JubesX.change_stat("love", 200, 4)
            "I had no idea!":
                $ JubesX.change_stat("love", 200, 3)
                $ JubesX.change_stat("inhibition", 80, 1)
                $ JubesX.change_face("_confused",1)
            "Duh.":
                $ JubesX.change_stat("love", 200, 1)
                $ JubesX.change_stat("obedience", 80, 2)
                $ JubesX.change_face("_angry",1)
        ch_v "Well I'm actually his partial clone."
        $ JubesX.change_face("_angry",1,Eyes="_side")
        ch_v "I was created to be some sort of biological weapon, an assassin."
        ch_v "I did a lot of work for them as a kid, until eventually I escaped."
        $ JubesX.change_face("_sadside",1)
        ch_v "After that, I had to do a lot of stuff. . . to stay alive."
        ch_v "Stuff I'm not proud of."
        $ JubesX.change_face("_sad",1)
        ch_v "But I don't know. . . being around you, I think it helps."
        $ JubesX.change_face("_sad",1,Mouth="_smile")
        ch_v "I kind of feel. . . better."
    if JubesX.SEXP >= 20:
        $ JubesX.change_stat("obedience", 80, 3)
        $ JubesX.change_stat("inhibition", 80, 2)
        $ JubesX.change_stat("lust", 80, 5)
        $ JubesX.change_face("_sly",1)
        ch_v "You really are good in bed, after all."
    if len(Player.Harem) >= 2:
        ch_v "And I know that you have your share of other girls. . ."
        ch_v ". . . but I'd still like to be a part of your life."
    elif Player.Harem:
        ch_v "And I know you're with someone else. . ."
        ch_v ". . . but I'd still like to be a part of your life."
    else:
        ch_v "I'd just like to be a part of your life."
    $ JubesX.change_face("_sad",1,Mouth="_smile")
    ch_v "That's it."
    $ JubesX.event_happened[5] += 1
    menu:
        extend ""
        "Yeah! I really love you.":
            $ JubesX.change_stat("love", 200, -3)
            $ JubesX.change_stat("obedience", 80, -3)
            $ JubesX.change_stat("inhibition", 80, 3)
            $ JubesX.change_face("_surprised",1)
            ch_v "Whoa!"
            $ JubesX.change_face("_perplexed")
            ch_v "Maybe cool your jets there, [JubesX.player_petname]."
            $ JubesX.change_face("_smile",Eyes="_side")
            ch_v "I wasn't. . ."
            ch_v "I don't think we're there. . ."
            $ JubesX.change_face("_perplexed",1)
            ch_v "Right?"
            menu:
                extend ""
                "Maybe you aren't.":
                    $ JubesX.change_stat("love", 200, 10)
                    $ JubesX.change_stat("obedience", 80, 5)
                    $ JubesX.change_stat("inhibition", 80, 5)
                    $ JubesX.change_stat("lust", 80, 2)
                    $ JubesX.change_face("_smile",1,Eyes="_side")
                    ch_v "Hehe. . . um."
                "I guess, sure.":
                    $ JubesX.change_stat("love", 200, 6)
                    $ JubesX.change_stat("obedience", 80, 3)
                    $ JubesX.change_stat("inhibition", 80, 2)
                    $ JubesX.change_face("_angry",1,Eyes="_side",Mouth="_lipbite")
                    ch_v "Right, so. . ."
        "Yeah, I think that'd be great.":

            $ JubesX.change_stat("love", 200, 6)
            $ JubesX.change_stat("obedience", 80, 2)
            $ JubesX.change_stat("inhibition", 80, 3)
            $ JubesX.change_face("_smile",1,Eyes="_side")
            ch_v "Cool."
        "Hmm? Ok.":
            $ JubesX.change_stat("love", 80, 3)
            $ JubesX.change_stat("obedience", 80, 5)
            $ JubesX.change_stat("inhibition", 80, 3)
            $ JubesX.change_face("_confused",1,Eyes="_side")
            ch_v "Yeah. . . cool."
        "I'm not really into that.":
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 80, 5)
            $ JubesX.change_stat("inhibition", 80, -5)
            $ JubesX.change_face("_sad",1)
            if len(Player.Harem) >= 2:
                ch_v "Is it because of [Player.Harem[0].name] and the rest?"
            elif Player.Harem:
                ch_v "Is it because of [Player.Harem[0].name]?"
            else:
                ch_v "Why not? What's the deal?"
            menu:
                extend ""
                "Yeah, I don't think she'd understand." if len(Player.Harem) == 1:
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 80, 7)
                    $ JubesX.change_face("_angry",1,Eyes="_side")
                    $ JubesX.check_if_likes(Player.Harem[0],800,-20,1)
                    ch_v "That bitch."
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 80, 7)
                    $ JubesX.change_face("_angry",1,Eyes="_side")
                    call Haremchange_stat (JubesX, 700, -20)
                    ch_v "Bitches."
                "It's. . . complicated.":
                    $ JubesX.change_stat("love", 200, -20)
                    $ JubesX.change_stat("obedience", 80, 8)
                    $ JubesX.change_stat("inhibition", 80, -5)
                    $ JubesX.change_face("_angry",1)
                    ch_v "Complicated. Sure. Whatever."
                    $ JubesX.change_face("_angry",1,Eyes="_side")
                    if len(Player.Harem) >= 2:
                        ch_v "Probably those bitches."
                        call Haremchange_stat (JubesX, 700, -10)
                    elif Player.Harem:
                        ch_v "Probably because of her."
                        $ JubesX.check_if_likes(Player.Harem[0],800,-20,1)
                    $ line = "no"
                "I'm just not into you like that.":
                    $ JubesX.change_stat("love", 200, -10)
                    $ JubesX.change_face("_surprised",1)
                    ch_v "Oh."
                    $ JubesX.change_stat("obedience", 80, 10)
                    $ JubesX.change_stat("inhibition", 80, 5)
                    $ JubesX.change_face("_sadside",1)
                    ch_v "Ok, I guess I can respect that."


            $ JubesX.change_face("_sad",1)
            if line != "no":
                ch_v "We're still cool though."
            ch_v "I should. . . leave."
            "[JubesX.name] wanders off in a bit of a daze."
            $ JubesX.event_happened[5] = 20
            call remove_girl (JubesX)
            $ line = 0
            return

    if Player.Harem:
        if not approval_check(JubesX, 1400):
            if len(Player.Harem) >= 2:
                ch_v "So you'll break up with the others?"
            else:
                ch_v "So you'll break up with [Player.Harem[0].name]?"
            menu:
                extend ""
                "Yes, you're worth it.":
                    $ JubesX.change_stat("love", 200, 20)
                    $ JubesX.change_stat("obedience", 80, 5)
                    $ JubesX.change_stat("inhibition", 80, 5)
                    $ JubesX.change_face("_surprised",2,Mouth="_smile")
                    ch_v ". . ."
                    $ JubesX.change_face("_smile",1)

                    $ JubesX.event_happened[5] = 10
                "I'd rather you join us.":
                    $ line = 0
                    if approval_check(JubesX, 1200):

                        $ temp_Girls = Player.Harem[:]
                        while temp_Girls and line != "no":

                            if JubesX.likes[temp_Girls[0].tag] <= 500:
                                $ line = "no"
                            $ temp_Girls.remove(temp_Girls[0])
                    else:
                        $ line = "no"
                    if line == "no":
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.change_stat("obedience", 80, 10)
                        $ JubesX.change_face("_angry",1)
                        call Haremchange_stat (JubesX, 700, -10)
                        ch_v "Eh, I'll pass."
                    else:
                        $ JubesX.change_stat("love", 200,5)
                        $ JubesX.change_stat("obedience", 80, 15)
                        $ JubesX.change_stat("inhibition", 80, 10)
                        $ JubesX.change_face("_bemused",1)
                        ch_v "Well, I s'pose that wouldn't be so terrible."
                "What? Of course not.":
                    $ JubesX.change_stat("love", 200, -25)
                    $ JubesX.change_stat("obedience", 80, 5)
                    call Haremchange_stat (JubesX, 700, -20)
                    $ JubesX.change_face("_angry",1)
                    ch_v "Well, fine then."
                    $ line = "no"
            if line == "no":
                $ JubesX.event_happened[5] = 20
                call remove_girl (JubesX)
                $ line = 0
                return



        if len(Player.Harem) >= 2:
            ch_v "And you don't think the others would mind?"
        else:
            ch_v "And you don't think [Player.Harem[0].name] would mind?"
        menu:
            extend ""
            "No, actually they're fine with it." if "JubesYes" in Player.traits:
                $ JubesX.change_stat("love", 200, 5)
                $ JubesX.change_stat("obedience", 80, 10)
                $ JubesX.change_stat("inhibition", 80, 5)
                $ JubesX.change_face("_surprised",1)
                ch_v "Oh, cool."
            "Actually. . . I guess we'll need to work on that one." if "JubesYes" not in Player.traits:
                $ JubesX.change_stat("love", 200, 3)
                $ JubesX.change_stat("obedience", 80, 3)
                $ JubesX.change_stat("inhibition", 80, 1)
                $ JubesX.change_stat("lust", 80, 1)
                $ JubesX.change_face("_confused",1)
                ch_v "Hmm, get back to me, I guess?"
                $ JubesX.event_happened[5] = 20
                call remove_girl (JubesX)
                $ line = 0
                return
        call Haremchange_stat (JubesX, 900, 20)


    if not simulation:
        $ Player.Harem.append(JubesX)
        if "JubesYes" in Player.traits:
            $ Player.traits.remove("JubesYes")
        $ JubesX.player_petnames.append("boyfriend")
        call Harem_Initiation
    $ JubesX.change_stat("love", 200, 3)
    $ JubesX.change_stat("obedience", 80, 3)
    $ JubesX.change_stat("inhibition", 80, 1)
    $ JubesX.change_stat("lust", 80, 1)
    $ JubesX.change_face("_sly",1)
    ch_v "So, did you have any plans for the next few minutes? . ."
    if simulation:
        return True
    $ approval_bonus = 10
    $ Player.add_word(1,"interruption")
    call Jubes_SexMenu
    $ approval_bonus = 0

    return

label Jubes_Cleanhouse:

    $ JubesX.drain_word("asked_to_meet")
    if "cleanhouse" in JubesX.to_do:
        $ JubesX.to_do.remove("cleanhouse")
    if not Player.Harem or JubesX in Player.Harem:
        $ JubesX.event_happened[5] = 2
        return

    if JubesX.location == bg_current or JubesX in Party:
        "[JubesX.name] glances over at you with a scowl."
    else:
        "[JubesX.name] turns a corner and notices you."
    if bg_current != "bg_jubes" and bg_current != "bg_player":
        "With little word, she moves behind you and pushes you towards her room."
        $ bg_current = "bg_jubes"
    $ JubesX.location = bg_current
    call set_the_scene
    call clear_the_room (JubesX)
    call set_the_scene
    call taboo_level
    $ JubesX.daily_history.append("relationship")
    $ JubesX.change_stat("love", 200, -20)
    $ JubesX.change_face("_angry",1)
    ch_v "What's the deal, [Player.player_petname]?"
    ch_v "It's been a week already, and you're still dating [Player.Harem[0].name]!"
    if len(Player.Harem) >= 2:
        ch_v "Not to mention the rest of them!"
    menu:
        extend ""
        "Sorry about that, I'm sticking with them":
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 80, 5)
            $ JubesX.change_stat("inhibition", 80, 5)
            $ JubesX.change_face("_angry",2)
            ch_v "You asshole."
            $ JubesX.change_face("_sadside",1)
            ch_v "You could have at least been honest about it."
        "Must have slipped my mind":
            $ JubesX.change_stat("love", 200, -10)
            $ JubesX.change_stat("obedience", 80, 10)
            ch_v "!"
            ch_v "Seriously dude? That's all you've got?"
        "[[shrug]":
            $ JubesX.change_stat("love", 200, -20)
            $ JubesX.change_stat("obedience", 80, 10)
            $ JubesX.change_stat("inhibition", 80, 10)
            $ JubesX.blushing = "_blush2"
            show Jubes_Sprite with vpunch
            "She clocks you one."
            "That was fair."
            $ JubesX.blushing = "_blush1"

    ch_v "I can't believe you're putting me through this."
    ch_v "Making me choose between you and putting up with this whole arrangement."
    $ line = 0
    if approval_check(JubesX, 1400) and approval_check(JubesX, 600,"O"):

        pass
    elif approval_check(JubesX, 1200) and approval_check(JubesX, 500,"O"):

        $ temp_Girls = Player.Harem[:]
        while temp_Girls and line != "no":

            if JubesX.likes[temp_Girls[0].tag] <= 400:
                $ line = "no"
            $ temp_Girls.remove(temp_Girls[0])
    else:
        $ line = "no"
    if line == "no":
        $ JubesX.change_stat("love", 200, -10)
        $ JubesX.change_stat("obedience", 80, 10)
        $ JubesX.change_face("_angry",1)
        call Haremchange_stat (JubesX, 700, -15)
        ch_v "No, this is bullshit, never mind."
    else:
        $ JubesX.change_stat("love", 200, 5)
        $ JubesX.change_stat("obedience", 80, 20)
        $ JubesX.change_stat("inhibition", 80, 10)
        $ JubesX.change_face("_angry",1,Eyes="_side")
        ch_v "Ok, fine, whatever. I'm in too."
        if not simulation:
            $ Player.Harem.append(JubesX)
            if "JubesYes" in Player.traits:
                $ Player.traits.remove("JubesYes")
            $ JubesX.player_petnames.append("boyfriend")
            call Harem_Initiation
            call Haremchange_stat (JubesX, 900, 20)
            $ JubesX.event_happened[5] = 20
    return


label Jubes_Love(Shipping=[], Shipshape=0, Topics=[], temp_Girls=[]):






    $ JubesX.drain_word("asked_to_meet")
    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(JubesX)
    while temp_Girls:
        if approval_check(temp_Girls[0], 1200, "LO"):
            $ Shipping.append(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])
    $ Shipshape = len(Shipping)

    if JubesX.location == bg_current or JubesX in Party:
        "[JubesX.name] glances over at you with a concerned look."
    else:
        "[JubesX.name] turns a corner and notices you."
    if bg_current != "bg_jubes" and bg_current != "bg_player":
        "With little word, she moves behind you and pushes you towards her room."
        $ bg_current = "bg_jubes"
    $ JubesX.location = bg_current
    call set_the_scene
    call clear_the_room (JubesX)
    call set_the_scene
    call taboo_level
    $ JubesX.daily_history.append("relationship")
    $ JubesX.change_face("_sad",1)
    ch_v "Hey, so, I like what this is. . ."
    ch_v "-what we have. . ."
    $ JubesX.change_face("_sadside",1)
    ch_v "It's been kind of hard for me to open up to people. . ."
    ch_v "I've been betrayed a lot out there."
    menu:
        extend ""
        "I would never betray you.":
            $ JubesX.change_face("_bemused",1)
            $ JubesX.change_stat("love", 200, 10)
            $ JubesX.change_stat("obedience", 70, 5)
            $ JubesX.change_stat("inhibition", 60, 5)
            ch_v "I. . . know that now."
        "I'm sorry to hear that.":
            $ JubesX.change_face("_sadside",1,Mouth="_smile")
            $ JubesX.change_stat("love", 200, 5)
            $ JubesX.change_stat("obedience", 90, -5)
            $ JubesX.change_stat("inhibition", 60, 10)
            ch_v ". . ."
            $ JubesX.change_face("_smile",1)
            ch_v "Thank you. . ."
        "That must be rough.":
            $ JubesX.change_face("_sadside",1,Mouth="_normal")
            $ JubesX.change_stat("love", 200, 5)
            ch_v ". . ."
            $ JubesX.change_face("_smile",1)
            ch_v "It was. . ."
        "Wow, that sucks.":
            $ JubesX.change_face("_confused",1)
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 90, 10)
            $ JubesX.change_stat("inhibition", 90, -5)
            ch_v ". . ."
            $ JubesX.change_face("_angry",1,Eyes="_side")
            ch_v "Right, so. . ."
    ch_v "I didn't always have it as easy as I've had it here."
    $ JubesX.eyes = "_normal"
    ch_v "I only thought it fair to tell you a little about that history."
    $ line = 0
    while len(Topics) < 9 and "exit" not in Topics:


        if line == "facility":
            menu:
                extend ""
                "How many people did you kill?" if "kills" not in Topics:
                    $ JubesX.change_face("_angry",0,Eyes="_side")
                    ch_v "Dozens. Maybe more. At least 13 primary targets."
                    ch_v "Too many \"collaterals.\""
                    $ Topics.append("kills")
                "Did you ever fail a mission?" if "fail" not in Topics:
                    $ JubesX.change_face("_angry",0,Eyes="_side",Brows="_normal")
                    ch_v "Once or twice."
                    ch_v "Sometimes they managed to get away."
                    ch_v "I'm not proud of who I was back then, but even then. . ."
                    $ JubesX.mouth = "_smile"
                    ch_v ". . . a part of me was happy when they did."
                    $ Topics.append("fail")
                "Did anyone take care of you?" if "mother" not in Topics:
                    $ JubesX.change_face("_smile",0)
                    ch_v "My mother, Sarah Kinney."
                    ch_v "She's the one who birthed me, and was also one of the scientists that helped create me."
                    $ JubesX.change_face("_sadside",0)
                    ch_v "She tried to help me, until I killed her."
                    $ Topics.append("mother")
                    $ line = "mother"
                "How did you escape?" if "escape" not in Topics:
                    $ JubesX.change_face("_sadside",0)
                    ch_v "Mother."
                    ch_v "She got me out, found me an escape route."
                    ch_v "It was the last thing she did."
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
                    $ JubesX.change_face("_smile",0)
                    ch_v "Her name was Sarah Kinney."
                    ch_v "She's the one who birthed me, and was also one of the scientists that helped create me."
                    $ JubesX.change_face("_sadside",0)
                    ch_v "She tried to help me, until I killed her."
                    $ Topics.append("mother")
                    $ line = "mother"
                "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:
                    $ JubesX.change_face("_sad",0,Eyes="_surprised")
                    ch_v "I didn't want to, but the primary_action scent made me. . ."
                    $ JubesX.change_face("_sadside",0)
                    if "trigger" in JubesX.history:
                        ch_v "I've mentioned that to you before. . ."
                    else:
                        $ JubesX.history.append("trigger")
                    ch_v ". . . it can make me kill, even if I don't want to."
                    $ Topics.append("killed")
                "It wasn't your fault." if "killed" in Topics:
                    $ JubesX.change_stat("love", 200, 5)
                    $ JubesX.change_stat("obedience", 70, 5)
                    $ JubesX.change_stat("inhibition", 70, 5)
                    $ JubesX.change_face("_sad",0)
                    ch_v "Not completely, no."
                    $ JubesX.change_face("_sadside",0)
                    ch_v "But my hands aren't clean."
                    $ line = "facility"
                "That must have been horrible." if "killed" in Topics:
                    $ JubesX.change_face("_sadside",0)
                    $ JubesX.change_stat("love", 200, 5)
                    $ JubesX.change_stat("obedience", 90, 5)
                    ch_v "It's taken me some time. . ."
                    $ JubesX.change_face("_normal",0)
                    ch_v "but I think I'm ok with it now."
                    $ line = "facility"
                "Bummer." if "killed" in Topics:
                    $ JubesX.change_face("_angry",1)
                    $ JubesX.change_stat("love", 200, -10)
                    $ JubesX.change_stat("obedience", 90, 5)
                    ch_v "Are you seriously making fun of my mother's death?!"
                    $ Topics.append("exit")
                    $ line = "_angry"


        if line == "NYX":
            menu:
                extend ""
                "What did you do for a living?" if "living" not in Topics:
                    $ JubesX.change_face("_sadside",0)
                    ch_v "There wasn't much I could do at the time, I mostly just scrounged for food."
                    ch_v "You can get by on some pretty awful stuff if you have a healing factor."
                    $ JubesX.change_face("_bemused",1,Brows="_sad")
                    ch_v "I also did some. . . shady stuff."
                    $ Topics.append("living")

                "Was it sexual?" if "work" not in Topics and "living" in Topics:
                    $ JubesX.change_face("_sadside",2)
                    $ JubesX.change_stat("obedience", 90, 5)
                    $ JubesX.change_stat("inhibition", 90, 10)
                    ch_v ". . ."
                    $ JubesX.blushing = "_blush1"
                    ch_v "A little."
                    $ line = "work"
                    $ Topics.append("work")

                "Did you hurt people?" if "work" not in Topics and "living" in Topics:
                    $ JubesX.change_face("_surprised",0,Eyes="_normal")
                    ch_v "No, definitely not."
                    ch_v "After the facility, I just couldn't take that sort of work anymore."
                    $ JubesX.change_face("_bemused",0)
                    ch_v "I avoided hurting anyone."
                    $ JubesX.change_face("_sadside",2)
                    ch_v "It tended to be more. . . sexual work."
                    $ line = "work"
                    $ Topics.append("work")

                "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:
                    $ JubesX.change_face("_bemused",0)
                    ch_v "Yeah, eventually."
                    ch_v "I'd seen Wolverine on the news, and thought maybe he had some answers."
                    ch_v "He's not around much though."
                    $ Topics.append("xaviers")
                    $ line = 0
                "Good thing you made it here. [[exit]" if "xaviers" in Topics:
                    $ JubesX.change_face("_smile",0)
                    ch_v "Yeah."
                    $ line = 0

        if line == "work":
            $ JubesX.change_face("_sadside",0,Mouth="_normal")
            ch_v "It was mostly the rougher customers."
            ch_v "The ones who couldn't control their tempers."
            $ JubesX.change_face("_angry",0,Mouth="_smile")
            ch_v "Better for the girl who can heal to take the hits, right?"
            menu:
                extend ""
                "That's terrible. I wish I could have protected you.":
                    $ JubesX.change_face("_smile",1)
                    $ JubesX.change_stat("love", 200, 5)
                    $ JubesX.change_stat("obedience", 90, 5)
                    $ JubesX.change_stat("inhibition", 90, -5)
                    ch_v "Thanks, but I was ok."
                    $ JubesX.change_face("_sadside",0)
                    ch_v "I didn't deserve it, but I felt like I did at the time."
                "You're strong to have made it out of there.":
                    $ JubesX.change_face("_smile",0)
                    $ JubesX.change_stat("love", 200, 5)
                    $ JubesX.change_stat("obedience", 90, 10)
                    $ JubesX.change_stat("inhibition", 90, 5)
                    ch_v "Thanks."
                    ch_v "I didn't really think of it like that. . ."
                    $ JubesX.change_face("_sadside",0)
                    ch_v "I just felt like I'd deserved it."
                    ch_v "But I realized how wrong that was."
                "Yeah, that makes sense.":
                    $ JubesX.change_face("_confused",1)
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 90, 15)
                    $ JubesX.change_stat("inhibition", 90, -5)
                    ch_v "Don't think before you speak, do you?"
                    $ JubesX.change_face("_sadside",0)
                    ch_v "It wasn't right, I just didn't realize it at the time."
            ch_v "Eventually I got past it and decided to get out of there."
            ch_v "Not like they could stop me."
            $ line = "NYX"

        if not line:

            menu:
                extend ""
                "What did you do back at the facility?" if "facility" not in Topics:
                    $ JubesX.change_face("_sadside",0)
                    ch_v "After they tested what I could do, they put me to work."
                    ch_v "Mainly, I killed people for them."
                    $ Topics.append("facility")
                    $ line = "facility"
                "More about that facility. . ." if "facility" in Topics:
                    $ line = "facility"

                "Where did you go after you escaped?" if "NYX" not in Topics:
                    $ JubesX.change_face("_sadside",0)
                    ch_v "I wandered in the wilderness for weeks."
                    ch_v "Eventually I found my way to New York."
                    ch_v "I lived on the streets for a few years."
                    $ Topics.append("NYX")
                    $ line = "NYX"
                "More about after the escape. . ." if "NYX" in Topics:
                    $ line = "NYX"

                "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:
                    $ JubesX.change_face("_smile",0)
                    $ JubesX.change_stat("love", 200, 10)
                    $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.change_stat("inhibition", 90, 3)
                    ch_v "Thanks for listening to me ramble."
                    $ Topics.append("exit")
                "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:
                    $ JubesX.change_face("_sadside",0, Mouth="_smile")
                    $ JubesX.change_stat("obedience", 90, 10)
                    ch_v "Yeah, you get the idea."
                    $ Topics.append("exit")
                "I don't really care about that. [[exit]":
                    $ JubesX.change_face("_angry",0)
                    $ JubesX.change_stat("love", 200, -15)
                    $ JubesX.change_stat("obedience", 50, 5)
                    $ JubesX.change_stat("obedience", 90, 10)
                    $ JubesX.change_stat("inhibition", 90, -5)
                    ch_v "Oh, I'm sorry if I was boring you with my life story."
                    $ line = "_angry"
                    $ Topics.append("exit")



    if line == "_angry":
        $ JubesX.change_face("_angry",0)
        ch_v "And here I was thinking that I meant something to you."
        ch_v "Well forget that!"
        $ line = 0
        $ JubesX.event_happened[6] = 23
        $ JubesX.recent_history.append("_angry")
        $ JubesX.daily_history.append("_angry")
        hide Jubes_Sprite with easeoutright
        call remove_girl (JubesX)
        $ JubesX.location = "hold"
        return

    $ JubesX.change_face("_bemused",0,Eyes="_down")
    ch_v "I just thought you should know,"
    $ JubesX.change_face("_smile",2)
    ch_v "I love you."
    menu:
        extend ""
        "I love you too!":
            $ JubesX.change_face("_smile",1)
            $ JubesX.change_stat("love", 200, 20)
            $ JubesX.change_stat("inhibition", 90, 5)
            ch_v "For a second there you had me worried."
            $ JubesX.player_petnames.append("lover")
            jump Jubes_Love_End
        "I know.":
            $ JubesX.change_face("_smile",1)
            $ JubesX.change_stat("love", 200, 10)
            $ JubesX.change_stat("obedience", 90, 5)
            $ JubesX.change_stat("inhibition", 90, 10)
            $ JubesX.change_stat("lust", 90, 5)
            ch_v "Smooth one. Seriously though, how about you?"
        "Neat?":
            $ JubesX.change_face("_confused",1)
            $ JubesX.change_stat("obedience", 90, 5)
            ch_v "I'm gonna need a bit more there, [JubesX.player_petname]."
        "Huh.":
            $ JubesX.change_face("_confused",1)
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 90, 10)
            ch_v "I'm not sure how to take that one."


    menu:
        extend ""
        "Oh, I love you too!":
            $ JubesX.change_face("_smile",1)
            $ JubesX.change_stat("love", 200, 15)
            $ JubesX.change_stat("obedience", 90, 5)
            $ JubesX.change_stat("inhibition", 90, 5)
            ch_v "For a second there you had me worried."
            $ JubesX.player_petnames.append("lover")
            jump Jubes_Love_End
        "I. . . love you back?":
            $ JubesX.change_face("_confused",1)
            $ JubesX.change_stat("love", 200, 5)
            $ JubesX.change_stat("obedience", 90, 10)
            ch_v "Ok, I'll take it."
            $ JubesX.player_petnames.append("lover")
            jump Jubes_Love_End
        "I mean, that's cool and all. . .":
            $ JubesX.change_face("_sadside",1)
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 90, 10)
            $ JubesX.change_stat("inhibition", 90, -5)
            ch_v ". . . but you don't love me back. Got it."
        "That's. . . uncomfortable.":
            $ JubesX.change_face("_angry",1)
            $ JubesX.change_stat("love", 200, -10)
            $ JubesX.change_stat("obedience", 90, 15)
            $ JubesX.change_stat("inhibition", 90, -5)
            ch_v "I don't like where this is heading."

    ch_v "What's your problem?"
    ch_v "Is it someone else?"
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
            $ JubesX.change_stat("obedience", 90, 15)
            $ JubesX.change_stat("inhibition", 90, 5)
            $ JubesX.change_stat("lust", 90, 5)
            $ JubesX.change_face("_sadside",1)
            ch_v "Well, you do have your pick."
        "There's nobody else.":
            $ JubesX.change_stat("love", 200, -15)
            $ JubesX.change_stat("obedience", 90, 15)
            $ JubesX.change_stat("inhibition", 90, 5)
            $ JubesX.change_face("_sad",1)
            if approval_check(JubesX, 1000, "OI"):
                ch_v "I guess that's something."
            else:
                ch_v ". . ."
        "It's a \"you\" problem.":
            $ JubesX.change_face("_angry")
            $ JubesX.change_stat("love", 200, -25)
            $ JubesX.change_stat("obedience", 90, 15)
            ch_v "You're seriously messing with me?"
            $ JubesX.change_stat("love", 200, -10)
            ch_v "You don't want to see me when I'm angry."
            $ JubesX.recent_history.append("_angry")
            $ JubesX.daily_history.append("_angry")


    if line:

        if JubesX.likes[line.tag] >= 800:
            $ JubesX.change_stat("love", 200, 5)
            $ JubesX.change_stat("obedience", 90, 20)
            $ JubesX.change_stat("inhibition", 90, 5)
            $ JubesX.change_stat("lust", 90, 5)
            $ JubesX.change_face("_sadside",1)
            ch_v "Yeah, I guess she's great."
        else:
            $ JubesX.change_face("_angry",Eyes="_side")
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 90, 20)
            ch_v "Bitch."
            $ JubesX.recent_history.append("_angry")
            $ JubesX.check_if_likes(line,800,-50,1)
    ch_v "Well, if that's the way you feel about it. . ."
    ch_v "I'll. . . see you later."
    ch_v "This. . . hurt."

label Jubes_Love_End:
    if "lover" not in JubesX.player_petnames:
        $ JubesX.event_happened[6] = 20
        hide Jubes_Sprite with easeoutright
        call remove_girl (JubesX)
        $ JubesX.location = "hold"
        return

    $ JubesX.event_happened[6] = 5
    "[JubesX.name] grabs you in a crushing hug."
    $ JubesX.change_stat("love", 200, 25)
    $ JubesX.change_stat("lust", 90, 5)
    $ JubesX.change_face("_sly",1)
    ch_v "So. . . now that we have some free time. . ."
    $ JubesX.change_stat("lust", 90, 10)

    if not JubesX.action_counter["sex"]:
        $ JubesX.change_face("_bemused",2)
        ch_v "I think I'm ready. . ."
    else:
        ch_v "Would you like to have some fun?"
    $ Player.add_word(1,"interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            $ JubesX.change_stat("inhibition", 30, 20)
            $ JubesX.change_stat("obedience", 70, 10)
            ch_v "Hmm. . ."
            call Jubes_SexAct ("sex")
        "I have something else in mind. . .[[choose another activity]":
            $ JubesX.brows = "_confused"
            $ JubesX.change_stat("obedience", 70, 25)
            ch_v "Like what? . ."
            $ approval_bonus = 20
            call Jubes_SexMenu
    return

label Jubes_Love_Redux:

    $ line = 0
    $ JubesX.daily_history.append("relationship")

    if JubesX.event_happened[6] >= 25:

        ch_p "I hope you've forgiven me, I still love you."
        $ JubesX.change_stat("love", 95, 10)
        if approval_check(JubesX, 950, "L"):
            $ line = "love"
        else:
            $ JubesX.change_face("_angry")
            ch_v "You're still working your way out of the hole, [JubesX.player_petname]."
            $ JubesX.eyes="_side"
            ch_v ". . ."
            $ JubesX.change_face("_angry",Mouth="_lipbite")
            ch_v "But let me hear your pitch."
    elif JubesX.event_happened[6] >= 23:

        ch_p "I was rude when you opened up to me before."
        $ JubesX.change_stat("love", 95, 10)
        if approval_check(JubesX, 950, "L"):
            ch_v "And. . ."
        else:
            $ JubesX.change_face("_angry")
            ch_v "You're still working your way out of the hole, [JubesX.player_petname]."
            $ JubesX.eyes="_side"
            ch_v ". . ."
            $ JubesX.change_face("_angry",Mouth="_lipbite")
            ch_v "But let me hear your pitch."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ JubesX.change_face("_perplexed",1)
        ch_v ". . ."
        $ JubesX.change_face("_angry", Eyes="_side")
        ch_v "How could I forget?"

    if line != "love":
        menu:
            extend ""
            "I'm sorry, I didn't mean it.":
                $ JubesX.eyes = "_surprised"
                ch_v "Oh really?"
                ch_v "That's awfully convenient."
                ch_p "Yeah. I mean, yes, I love you, [JubesX.name]."
                $ JubesX.change_stat("love", 200, 10)
                if approval_check(JubesX, 950, "L"):
                    $ line = "love"
                else:
                    $ JubesX.change_face("_sadside")
                    ch_v "Well, maybe I don't, anymore. . ."
            "I've changed my mind, I do love you, so. . .":
                if approval_check(JubesX, 950, "L"):
                    $ line = "love"
                    ch_v "Well that's great."
                else:
                    $ JubesX.mouth = "_sad"
                    ch_v "Good for you."
                    $ JubesX.change_stat("inhibition", 90, 10)
                    $ JubesX.change_face("_sadside")
                    ch_v "I don't exactly have the same mind either. . ."
            "Um, never mind.":
                $ JubesX.change_stat("love", 200, -30)
                $ JubesX.change_stat("obedience", 50, 10)
                $ JubesX.change_face("_angry")
                ch_v "Oh, fuck you."
                $ JubesX.recent_history.append("_angry")
                $ JubesX.daily_history.append("_angry")
    if line == "love":
        $ JubesX.change_stat("love", 200, 40)
        $ JubesX.change_stat("obedience", 90, 10)
        $ JubesX.change_stat("inhibition", 90, 10)
        $ JubesX.change_face("_smile")
        ch_v "I'm glad you came around."
        ch_v "I love you too, [JubesX.player_petname]!"
        if JubesX.event_happened[6] < 25:
            $ JubesX.change_face("_sly")
            "She grabs the back of your head and pulls you close."
            ch_v "Next time, don't keep me waiting."
        $ JubesX.player_petnames.append("lover")
    $ JubesX.event_happened[6] = 25
    return






label Jubes_Sub:
    $ JubesX.drain_word("asked_to_meet")
    call shift_focus (JubesX)
    if JubesX.location != bg_current and JubesX not in Party:
        "Suddenly, [JubesX.name] shows up and says she needs to talk to you."

    $ JubesX.location = bg_current
    call set_the_scene (0)
    call display_girl (JubesX)
    call clear_the_room (JubesX)
    call set_the_scene
    call taboo_level
    $ JubesX.daily_history.append("relationship")
    $ JubesX.change_face("_bemused", 1)

    $ line = 0
    ch_v "I've noticed something."
    ch_v "You've been trying to boss me around lately."
    menu:
        ch_v "I've noticed you trying to boss me around.{w=2.8}{nw}"
        "I guess. That's just kind of what comes naturally for me.":
            pass
        "Sorry. I didn't mean to come off like that.":
            pass
        "Yup. Deal with it.":
            pass
    "Before you can speak, she puts her hand over your mouth."
    $ JubesX.change_face("_sly", 1,Eyes="_side")
    ch_v "I don't know how I feel about that."
    if JubesX.event_happened[6]:
        $ JubesX.change_face("_sadside", 1)
        ch_v "You know the past I've had, with the facility, with the. . . "
        ch_v ". . . work I had to do for them."
        $ JubesX.change_face("_sad", 1)
        ch_v "I don't know if I want to let anyone tell me what to do like that again."
    menu Jubes_Sub_Question:
        extend ""
        "I guess I can be demanding.":
            $ JubesX.change_face("_sly", 1)
            $ JubesX.change_stat("obedience", 200, 10)
            $ JubesX.change_stat("inhibition", 50, 5)
        "Sorry. I didn't mean to come off like that.":
            $ JubesX.change_face("_sly", 1)
            $ JubesX.change_stat("love", 80, 5)
            $ JubesX.change_stat("obedience", 200, -5)
            $ JubesX.change_stat("inhibition", 50, -5)
            ch_v "I get it, you're assertive. . ."
        "Remind me about the facility?" if JubesX.event_happened[6] and line != "facility":
            $ JubesX.change_face("_sadside", 1)
            $ JubesX.change_stat("love", 99, -10)
            $ JubesX.change_stat("inhibition", 50, -5)
            ch_v "I told you, I was raised in an underground government lab."
            ch_v "They ordered me to kill people for them."
            $ JubesX.change_face("_sly", 0, Brows= "_angry")
            ch_v ". . . until I got tired of taking orders."
            $ line = "facility"
            jump Jubes_Sub_Question
        "What bothers you about being told to do things?" if not JubesX.event_happened[6] and line != "facility":
            $ JubesX.change_face("_sadside", 1)
            $ JubesX.change_stat("love", 80, 5)
            ch_v "I've just had some rough experiences."
            ch_v "You don't need to know about them."
            ch_v ". . ."
            $ JubesX.change_face("_sad", 0)
            ch_v "Let's just say I was ordered to do some things I regret."
            $ line = "facility"
            jump Jubes_Sub_Question
        "Get with the program.":
            if approval_check(JubesX, 1000, "LO"):
                $ JubesX.change_face("_sly", 1)
                $ JubesX.change_stat("obedience", 200, 20)
                $ JubesX.change_stat("inhibition", 50, 10)
                ch_v "Hmmm. . ."
            else:
                $ JubesX.change_stat("love", 200, -10)
                $ JubesX.change_stat("inhibition", 50, -5)
                $ JubesX.change_face("_angry",0)
                ch_v "You're not off to a good start here. You might want to rethink your attitude."
                menu:
                    extend ""
                    "Sorry. I thought that's what you were into.":
                        $ JubesX.change_face("_perplexed", 1,Eyes="_side")
                        $ JubesX.eyes = "_side"
                        $ JubesX.change_stat("love", 75, 10)
                        $ JubesX.change_stat("obedience", 200, 5)
                        $ JubesX.change_stat("inhibition", 50, 5)
                        ch_v ". . . after I just said. . ."
                        $ JubesX.change_face("_sly", 1)
                        ch_v "Ok, whatever."
                    "I don't care.":
                        $ JubesX.change_stat("love", 95, -10)
                        ch_v "I guess not."
                        $ line = "rude"
    if line == "facility":
        $ line = 0

    if not line:

        $ JubesX.change_face("_sly", 1)
        ch_v "Look, it's not like. . ."
        $ JubesX.change_face("_sly", 2)
        ch_v ". . . it's not like I hate it."
        $ JubesX.change_face("_smile", 1, Eyes="_side")
        ch_v ". . . I actually think it might make me. . ."
        menu:
            extend ""
            "-excited?":
                $ JubesX.change_stat("obedience", 200, 5)
                $ JubesX.change_stat("inhibition", 50, 5)
                ch_v ". . ."
                $ JubesX.change_face("_sly", 1)
                $ JubesX.change_stat("lust", 50, 10)
                ch_v "a little, yeah."
            "-digusted?":
                $ JubesX.change_stat("love", 75, -5)
                $ JubesX.change_stat("obedience", 200, -5)
                $ JubesX.change_face("_sadside", 1)
                ch_v ". . . kind of,"
                $ JubesX.change_face("_sly", 1)
                $ JubesX.change_stat("inhibition", 70, 5)
                $ JubesX.change_stat("lust", 50, 5)
                ch_v "but also kind of excited by it."
            "-hungry?":
                $ JubesX.change_face("_confused", 1,Eyes="_surprised",Mouth="_smile")
                $ JubesX.change_stat("obedience", 200, -5)
                $ JubesX.change_stat("inhibition", 50, -5)
                ch_v "?!"
                $ JubesX.change_face("_confused", 1,Eyes="_normal",Mouth="_smile")
                ch_v "Well. . . yeah? But not for-"
                $ JubesX.change_face("_sly", 1)
                $ JubesX.change_stat("lust", 50, 5)
                ch_v "I mean, it makes me kind of. . . excited."
            "-horny?":
                $ JubesX.change_stat("obedience", 200, 10)
                $ JubesX.change_stat("inhibition", 50, 5)
                $ JubesX.change_face("startled", 2,Mouth="_lipbite")
                ch_v "!"
                $ JubesX.change_face("_sly", 1, Eyes="_side")
                $ JubesX.change_stat("inhibition", 50, 5)
                $ JubesX.change_stat("lust", 50, 10)
                $ JubesX.change_stat("lust", 70, 5)
                ch_v "Yes."
        menu:
            extend ""
            "Good. If you wanna be with me, then you follow my orders.":
                if approval_check(JubesX, 1000, "LO"):
                    $ JubesX.change_face("_sly", 1)
                    $ JubesX.change_stat("obedience", 200, 15)
                    $ JubesX.change_stat("inhibition", 50, 10)
                    ch_v "Hmmm. . ."
                else:
                    $ JubesX.change_face("_sadside", 1,Mouth="_normal")
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 200, 10)
                    ch_v "You might want to slow your roll there, [JubesX.player_petname]."
                    menu:
                        extend ""
                        "Whatever. That's how it is. Take it or leave it.":
                            $ JubesX.change_face("_angry")
                            $ JubesX.change_stat("love", 200, -10)
                            $ JubesX.change_stat("obedience", 200, 5)
                            ch_v "I think you're pushing it too far there, [JubesX.player_petname]."
                            $ line = "rude"
                        "Ok, just a little.":
                            $ JubesX.change_face("_bemused", 1)
                            $ JubesX.change_stat("love", 95, 5)
                            $ JubesX.change_stat("inhibition", 50, 5)
                            ch_v "-but not too much."
            "Yeah? You think it's sexy?":

                $ JubesX.change_face("_bemused", 2,Eyes="_side")
                $ JubesX.change_stat("obedience", 200, 5)
                $ JubesX.change_stat("inhibition", 50, 10)
                ch_v ". . ."
                $ JubesX.change_stat("lust", 50, 5)
                ch_v "Yeah."
            "You sure you don't want me to back off a little?":

                $ JubesX.change_face("startled", 1,Eyes="_squint")
                $ JubesX.change_stat("obedience", 200, -5)
                menu:
                    ch_v "Well if you have to ask. . ."
                    "Only if you're okay with it.":
                        $ JubesX.change_face("_bemused", 1)
                        $ JubesX.change_stat("love", 95, 10)
                        $ JubesX.change_stat("inhibition", 50, 10)
                        $ line = 0
                    "Uhm. . .yeah. I think it's weird. Sorry.":
                        $ JubesX.change_face("_sad", 1, Eyes="_surprised")
                        $ JubesX.change_stat("love", 200, -15)
                        $ JubesX.change_stat("obedience", 200, -5)
                        $ JubesX.change_stat("inhibition", 50, -10)
                        $ line = "embarrassed"
            "I couldn't care less.":

                $ JubesX.change_stat("love", 200, -10)
                $ JubesX.change_stat("obedience", 200, 15)
                $ JubesX.change_face("_angry")
                ch_v "I think you're pushing it too far there, [JubesX.player_petname]."
                $ line = "rude"

    if not line:
        $ JubesX.change_face("_bemused", 1,Eyes = "_down")
        ch_v "So, I'm willing to give this a shot."
        ch_v "Just a trial period, to see how it goes."
        ch_v "Just tell me what you want, and. . . I'll see about doing it."
        menu Jubes_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                $ JubesX.change_stat("obedience", 200, 5)
                $ JubesX.change_stat("inhibition", 50, 5)
                $ JubesX.change_face("_sly", 1)
                $ line = 0
            "Don't you think that relationship's kinda. . .weird?":
                $ JubesX.change_face("_sad", 1, Eyes="_surprised")
                $ JubesX.change_stat("love", 200, -5)
                $ JubesX.change_stat("inhibition", 50, -15)
                $ line = "embarrassed"

    if not line:
        $ JubesX.change_face("_smile", 1)
        ch_v "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                $ JubesX.change_stat("love", 95, 5)
                $ JubesX.change_stat("obedience", 200, 15)
                $ JubesX.change_stat("inhibition", 50, 5)
                ch_v "Yes, sir."
                $ JubesX.player_petname = "sir"
            "That's kind of formal, isn't it?":
                $ JubesX.change_face("_perplexed", 1)
                ch_v "Huh. ok, no problem"
                $ JubesX.change_stat("inhibition", 50, -5)
                $ JubesX.change_face("_sly", 1,Eyes="_side")
                menu:
                    ch_v "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                        $ JubesX.change_stat("obedience", 200, 10)
                        $ JubesX.change_face("_smile", 1)
                        ch_v "Good."
                    "I don't feel comfortable with that. . .":
                        $ JubesX.change_face("_sad", 1, Eyes="_side")
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.change_stat("obedience", 200, -30)
                        $ JubesX.change_stat("inhibition", 50, -15)
                        $ line = "embarrassed"


    $ JubesX.history.append("sir")
    if not line:
        $ JubesX.player_petnames.append("sir")

    elif line == "rude":
        call remove_girl (JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] knocks her way past you and storms off."
    elif line == "embarrassed":
        $ JubesX.change_face("_sadside", 2)
        ch_v "Huh, ok, if you're not interested. . ."
        hide Jubes_Sprite with easeoutright
        call remove_girl (JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] heads out of the room."
    return

label Jubes_Sub_Asked:
    $ line = 0
    $ JubesX.change_face("_sadside", 1)
    ch_v "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in JubesX.player_petnames and approval_check(JubesX, 850, "O"):

                pass
            elif approval_check(JubesX, 550, "O"):

                pass
            else:
                $ JubesX.change_face("_angry", 1)
                ch_v "It was a bad idea, don't worry about it."
                $ line = "rude"

            if line != "rude":
                $ JubesX.change_stat("love", 90, 10)
                $ JubesX.change_face("_sly", 1)
                ch_v "Well, it's not like you stopped ordering me around anyway."
                ch_v "Ok, let's give it a shot."
        "I know it's what you want. Do you want to try again, or not?":

            $ JubesX.change_face("_bemused", 1)
            if "sir" in JubesX.player_petnames:
                if approval_check(JubesX, 850, "O"):
                    ch_v "Ok, fine."
                else:
                    ch_v "Nah, I'm good."
                    $ line = "rude"
            elif approval_check(JubesX, 600, "O"):

                $ JubesX.change_face("_confused", 1)
                ch_v "Kinda wishy-washy there."
                $ JubesX.change_face("_sly", 1)
                ch_v "but maybe you're right."
                ch_v "Are you sure you're into this?"
                menu:
                    extend ""
                    "Yes, I'm sorry I was mean about it.":
                        $ JubesX.change_stat("love", 90, 15)
                        $ JubesX.change_stat("inhibition", 50, 10)
                        $ JubesX.change_face("_bemused", 1)
                        $ JubesX.eyes = "_side"
                        ch_v "Ok then."
                    "You're damned right I am, bitch.":
                        if "sir" in JubesX.player_petnames and approval_check(JubesX, 900, "O"):
                            $ JubesX.change_stat("love", 200, -5)
                            $ JubesX.change_stat("obedience", 200, 10)
                            ch_v ". . ."
                        elif approval_check(JubesX,700, "O"):
                            $ JubesX.change_stat("love", 200, -5)
                            $ JubesX.change_stat("obedience", 200, 10)
                            ch_v "Hmmm. . ."
                        else:
                            $ JubesX.change_stat("love", 200, -10)
                            $ JubesX.change_stat("obedience", 90, -10)
                            $ JubesX.change_stat("obedience", 200, -10)
                            $ JubesX.change_stat("inhibition", 50, -15)
                            $ JubesX.change_face("_angry", 1)
                            ch_v "Wow, that's pushing it."
                            $ line = "rude"
                    "Ok, never mind then.":
                        $ JubesX.change_face("_angry", 1)
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.change_stat("obedience", 90, -10)
                        $ JubesX.change_stat("obedience", 200, -10)
                        $ JubesX.change_stat("inhibition", 50, -15)
                        ch_v "I was thinking of taking orders from you, not mindgames."
                        ch_v "I should've known you'd be like this."
                        $ line = "rude"

    $ JubesX.recent_history.append("asked sub")
    $ JubesX.daily_history.append("asked sub")
    if line == "rude":

        hide Jubes_Sprite with easeoutright
        call remove_girl (JubesX)
        $ JubesX.recent_history.append("_angry")
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] checks you as she stomps out of the room."
    elif "sir" in JubesX.player_petnames:

        $ JubesX.change_stat("obedience", 200, 50)
        $ JubesX.player_petnames.append("master")
        $ JubesX.player_petname = "master"
        $ JubesX.eyes = "_sly"
        ch_v ". . . master. . ."
    else:

        $ JubesX.change_stat("obedience", 200, 30)
        $ JubesX.player_petnames.append("sir")
        $ JubesX.player_petname = "sir"
        $ JubesX.change_face("_sly", 1)
        ch_v ". . . sir."
    return






label Jubes_Master:
    $ JubesX.drain_word("asked_to_meet")
    call shift_focus (JubesX)
    if JubesX.location != bg_current and JubesX not in Party:
        "Suddenly, [JubesX.name] shows up and says she needs to talk to you."

    $ JubesX.location = bg_current
    call set_the_scene (0)
    call display_girl (JubesX)
    call clear_the_room (JubesX)
    call set_the_scene
    $ JubesX.daily_history.append("relationship")
    call taboo_level
    $ line = 0
    $ JubesX.change_face("_sly", 1)
    ch_v "[JubesX.player_petname]. . ."
    ch_v ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            $ JubesX.change_stat("obedience", 200, 5)
            $ JubesX.change_stat("inhibition", 50, 5)
        "What?":
            ch_v "I was asking if I could talk to you about something. . ."
            $ JubesX.eyes = "_side"
            ch_v ". . . personal."
            $ JubesX.eyes = "_squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ JubesX.change_stat("love", 80, 5)
                    $ JubesX.change_stat("obedience", 200, 5)
                    ch_v "Right. . ."
                "Oh, then no.":
                    $ JubesX.change_face("_sad", 1)
                    $ JubesX.change_stat("love", 80, -5)
                    $ JubesX.change_stat("obedience", 200, -10)
                    $ line = "embarrassed"
        "No.":
            $ JubesX.change_face("_perplexed", 1,Brows="_confused")
            $ JubesX.change_stat("love", 80, -5)
            $ JubesX.change_stat("obedience", 200, -5)
            $ JubesX.change_stat("inhibition", 50, -5)
            ch_v "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ JubesX.change_face("_confused", 1)
                    $ JubesX.change_stat("obedience", 200, 10)
                    $ JubesX.change_stat("inhibition", 60, 10)
                    ch_v "Right. . ."
                "Yes, not interested.":
                    $ JubesX.change_face("_sad", 1)
                    $ JubesX.change_stat("love", 80, -5)
                    $ JubesX.change_stat("inhibition", 50, -10)
                    $ line = "embarrassed"


    if not line:
        $ JubesX.change_face("_sly", 1)
        ch_v "I think I enjoy having you in charge."
        ch_v "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                $ JubesX.change_face("_sly", 1)
                $ JubesX.change_stat("obedience", 200, 5)
                ch_v "Good. Maybe we could take this a bit more seriously?"
                menu:
                    extend ""
                    "Nah. This is just about perfect.":
                        $ JubesX.change_face("_sad", 1)
                        $ JubesX.change_stat("obedience", 200, -15)
                        $ JubesX.change_stat("love", 80, 10)
                        $ line = "fail"
                    "What'd you have in mind?":
                        $ JubesX.eyes = "_side"
                        ch_v "I was thinking I could start calling you. . . {i}master{/i}?"
                        $ JubesX.eyes = "_squint"
                        menu:
                            extend ""
                            "Oh, yeah. I'd like that.":
                                $ JubesX.change_stat("obedience", 200, 5)
                                ch_v "Good. . ."
                            "Um. . .nah. That's too much.":
                                $ JubesX.change_face("_sadside", 1)
                                $ JubesX.change_stat("obedience", 200, -15)
                                $ JubesX.change_stat("inhibition", 50, 5)
                                $ line = "fail"
                    "Actually, I'd prefer we stopped doing it. Too much pressure.":

                        $ JubesX.change_face("_sad", 1)
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 200, -10)
                        $ JubesX.change_stat("inhibition", 50, 15)
                        $ line = "fail"
                    "Actually, let's stop that. It's creeping me out.":

                        $ JubesX.change_face("_angry", 2, Eyes="_surprised")
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.change_stat("obedience", 200, -50)
                        $ JubesX.change_stat("inhibition", 50, -15)
                        ch_v "Say no more, I wouldn't want to CREEP YOU OUT."
                        $ line = "embarrassed"
            "As if I care what you think, slut.":

                $ JubesX.change_face("_angry", 1, Mouth="_smile")
                $ JubesX.change_stat("love", 90, -20)
                $ JubesX.change_stat("obedience", 200, 10)
                $ JubesX.change_stat("inhibition", 50, -10)
                ch_v ". . ."
                menu:
                    ch_v "Excuse me?"
                    "Sorry. I just don't care what you want.":
                        if approval_check(JubesX, 1400, "LO"):
                            $ JubesX.change_stat("obedience", 200, 10)
                            ch_v ". . ."
                            $ JubesX.change_face("_sly", 1)
                            $ JubesX.change_stat("love", 200, 20)
                            $ JubesX.change_stat("inhibition", 50, 15)
                            ch_v ". . .{i}go on. . .{/i}"
                        else:
                            $ JubesX.change_stat("love", 200, -15)
                            $ JubesX.change_stat("obedience", 200, -10)
                            $ JubesX.change_stat("inhibition", 50, 5)
                            $ JubesX.change_face("_angry", 1)
                            ch_v "!!!"
                            $ line = "rude"
                    "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                        $ JubesX.change_stat("love", 200, 10)
                        $ JubesX.change_stat("obedience", 200, 10)
                        $ JubesX.change_stat("inhibition", 50, 5)
                        if approval_check(JubesX, 1400, "LO"):
                            $ JubesX.change_stat("obedience", 200, 10)
                            ch_v ". . ."
                            $ JubesX.change_face("_sly", 1)
                            $ JubesX.change_stat("love", 200, 20)
                            $ JubesX.change_stat("inhibition", 50, 15)
                            ch_v ". . .{i}no, about right. . .{/i}"
                        else:
                            $ JubesX.change_stat("love", 200, 5)
                            $ JubesX.change_stat("obedience", 200, -5)
                            $ JubesX.change_stat("inhibition", 50, 5)
                            $ JubesX.change_face("_angry", 1, Eyes="_side")
                            ch_v ". . ."
                            ch_v "We'll work on it. . ."
            "I don't really like it. Too much pressure.":

                $ JubesX.change_face("_sad", 2)
                $ JubesX.change_stat("love", 200, -20)
                $ JubesX.change_stat("obedience", 200, -20)
                $ JubesX.change_stat("inhibition", 50, -10)
                $ line = "embarrassed"

    $ JubesX.history.append("master")
    if line == "rude":
        $ JubesX.recent_history.append("_angry")
        hide Jubes_Sprite with easeoutright
        call remove_girl (JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] stomps out of the room."
    elif line == "embarrassed":
        ch_v "Ok, fine then."
        ch_v "And here I was, about to \"elevate your clearance.\""
        hide Jubes_Sprite with easeoutright
        call remove_girl (JubesX)
        if not simulation:
            $ renpy.pop_call()
        "[JubesX.name] brushes past you on her way out."
    elif line == "fail":
        ch_v "Oh. . ."
        ch_v "I guess that's fine."
    else:
        $ JubesX.change_stat("obedience", 200, 50)
        $ JubesX.player_petnames.append("master")
        $ JubesX.player_petname = "master"
        ch_v ". . .master."
    return







label Jubes_Sexfriend:

    $ JubesX.lust = 70
    $ JubesX.location = bg_current
    $ JubesX.drain_word("asked_to_meet")
    call set_the_scene
    $ JubesX.daily_history.append("relationship")
    call taboo_level
    $ line = 0
    $ JubesX.change_face("_sly",2,Eyes="_side")
    "[JubesX.name] approaches you and pulls you aside. She seems to be shivering a little bit."
    "She seems to be squirming around and rubbing her thighs together."
    $ JubesX.player_petnames.append("sex friend")
    $ JubesX.change_face("_sly",2)
    if JubesX in Player.Harem:
        ch_v "Hey."
        ch_v "I need some alone time with you."
    elif "lover" in JubesX.player_petnames or "master" in JubesX.player_petnames or "lover" in JubesX.player_petnames or "sir" in JubesX.player_petnames:

        ch_v "Hey."
        ch_v "I need some alone time with you."
    else:

        ch_v "Hey, so. . . "
        if JubesX.SEXP >= 50:
            ch_v "I know we're kind of casual and all. . ."
        else:
            ch_v "Maybe this seems a bit out of the blue, but. . ."
        ch_v "I'd really just like to have some sex."
        ch_v "Like lots of sex."
        ch_v "With you."
        menu:
            extend ""
            "Sure":
                $ JubesX.change_face("_sly",2,Mouth="_smile")
                $ line = "yes"
            "No thanks":
                $ JubesX.change_face("_confused",2)
                $ line = "no"
            ". . .":
                $ JubesX.change_stat("obedience", 90, 5)
                $ JubesX.change_face("_confused",2)

        if not line:
            ch_v "Now, if at all possible. . ."
            menu:
                extend ""
                "Sure":
                    $ JubesX.change_face("_sly",2,Mouth="_smile")
                    $ line = "yes"
                "No thanks":
                    $ JubesX.change_face("_confused",2)
                    $ line = "no"

        if line == "no":
            $ JubesX.change_stat("love", 200, -5)
            $ JubesX.change_stat("obedience", 80, 5)
            ch_v "What? Why not?"
            menu:
                extend ""
                "Ok, fine":
                    $ JubesX.change_face("_confused",2,Mouth="_smile")
                    ch_v "Love the enthusiasm."
                    $ line = "yes"
                "Not interested":
                    $ JubesX.change_face("_confused",2)
                "There's someone else":

                    $ JubesX.change_stat("love", 95, -5)
                    $ JubesX.change_stat("obedience", 90, 5)
                    if Player.Harem:
                        $ JubesX.change_face("_surprised",2)
                        ch_v "Oh, [Player.Harem[0].name]?"
                        $ JubesX.check_if_likes(Player.Harem[0],600,-25,1)
                    $ JubesX.change_face("_sly",2)
                    ch_v "Well, she doesn't need to know about it. . ."
                    menu:
                        extend ""
                        "Ok, fine":
                            ch_v "Love the enthusiasm."
                            $ line = "yes"
                        "Still no":
                            pass

    if line == "no":
        $ JubesX.change_stat("love", 200, -10)
        $ JubesX.change_stat("obedience", 90, 15)
        $ JubesX.change_stat("inhibition", 90, 10)
        $ JubesX.change_face("_sad",2)
        ch_v "Really?"
        ch_v "Bummer."
        ch_v "Well let me know if you change your mind."
        $ JubesX.change_face("_sadside",2,Mouth="_lipbite",Brows="_angry")
        if Player.Harem:
            ch_v "Wonder if [Player.Harem[0].name]'s busy. . ."
            $ JubesX.check_if_likes(Player.Harem[0],500,25,1)
        else:
            ch_v "Wonder if Kitty's busy. . ."
            $ JubesX.check_if_likes("Kitty",500,25,1)
    else:
        $ JubesX.change_stat("love", 90, 10)
        $ JubesX.change_stat("obedience", 90, 5)
        $ JubesX.change_stat("inhibition", 90, 15)
        $ JubesX.change_face("_sly",1,Mouth="_smile")
        if taboo:
            ch_v "Wanna take this party someplace else?"
            menu:
                extend ""
                "Yeah":
                    ch_v "Sure, let's go."
                    if bg_current == "bg_player":
                        $ bg_current = "bg_jubes"
                    else:
                        $ bg_current = "bg_player"
                    $ JubesX.location = bg_current
                    call clear_the_room (JubesX)
                    call set_the_scene
                    $ taboo = 0
                    $ JubesX.taboo = 0
                "No, let's do it here.":

                    $ JubesX.change_stat("obedience", 80, 5)
                    $ JubesX.change_stat("inhibition", 90, 15)
                    ch_v "Kinky."

        $ action_context = JubesX
        $ Player.add_word(1,"interruption")
        call Jubes_SexPrep
        call Jubes_SexMenu


    return






label Jubes_Fuckbuddy:
    $ JubesX.daily_history.append("relationship")
    $ JubesX.lust = 80
    $ JubesX.drain_word("asked_to_meet")

    "You hear a knock on the door, and go to answer it."

    $ JubesX.location = bg_current
    call shift_focus (JubesX)
    call set_the_scene (0)
    $ JubesX.outfit = "casual1"
    $ JubesX.today_outfit = "casual1"
    $ JubesX.change_outfit("casual1")
    call display_girl (JubesX)
    call taboo_level
    $ primary_action = "masturbation"
    $ girl_offhand_action = "fondle_pussy"
    $ JubesX.change_face("_sly",2,Mouth="_lipbite")
    "[JubesX.name] is standing in the doorway, with her hand down her pants."
    "You can tell she's been masturbating furiously, her scent is overpowering."
    $ primary_action = None
    $ girl_offhand_action = None
    $ JubesX.arm_pose = 1
    "She looks you up and down hungrily, and pulls her hand out of her pants."
    "She reaches up to caress your face, smearing her juices along it."
    ch_v "Mine."
    $ JubesX.player_petnames.append("fuck buddy")
    $ JubesX.event_happened[10] += 1

    $ action_context = JubesX
    $ Player.add_word(1,"interruption")
    call Jubes_SexPrep
    call Jubes_SexMenu
    return






label Jubes_Daddy:
    $ JubesX.daily_history.append("relationship")
    $ JubesX.drain_word("asked_to_meet")
    call shift_focus (JubesX)
    call set_the_scene
    ch_v ". . ."
    if JubesX in Player.Harem:
        ch_v "So we've been dating a while yeah?"
    else:
        ch_v "This thing we've got, pretty fun, right?"
    if JubesX.love > JubesX.obedience and JubesX.love > JubesX.inhibition:
        ch_v "and you've been really kind to me. . ."
    elif JubesX.obedience > JubesX.inhibition:
        ch_v "and you've been a good influence. . ."
    else:
        ch_v "like, really fun. . ."
    ch_v "So I've been thinking, would you want to be called. . ."
    ch_v "\"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ JubesX.change_face("_smile")
            $ JubesX.change_stat("love", 90, 20)
            $ JubesX.change_stat("obedience", 60, 10)
            $ JubesX.change_stat("inhibition", 80, 30)
            ch_v "Cool."
        "What do you mean by that?":
            $ JubesX.change_face("_bemused")
            ch_v "I don't know, I've had some shitty father figures. . ."
            ch_v "I just. . ."
            if JubesX.love > JubesX.obedience and JubesX.love > JubesX.inhibition:
                ch_v "I think you could do better. . ."
            elif JubesX.obedience > JubesX.inhibition:
                ch_v "you've really been assertive. . ."
            else:
                ch_v "wouldn't it be kinky?"

            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ JubesX.change_face("_smile")
                    $ JubesX.change_stat("love", 90, 15)
                    $ JubesX.change_stat("obedience", 60, 20)
                    $ JubesX.change_stat("inhibition", 80, 25)
                    ch_v "Great!"
                    $ JubesX.change_face("_sly",2)
                    ch_v " . . . daddy."
                    $ JubesX.change_face("_sly",1)
                    $ JubesX.player_petname = "daddy"
                "Could you not, please?":
                    $ JubesX.change_stat("love", 90, 5)
                    $ JubesX.change_stat("obedience", 80, 40)
                    $ JubesX.change_stat("inhibition", 80, 20)
                    $ JubesX.change_face("_sad")
                    ch_v " . . . "
                    ch_v "Well, ok."
                "You've got some real daddy issues, uh?":
                    $ JubesX.change_stat("love", 90, -15)
                    $ JubesX.change_stat("obedience", 80, 45)
                    $ JubesX.change_stat("inhibition", 70, 5)
                    $ JubesX.change_face("_angry")
                    ch_v "Yes. . . I said that."
        "You've got some real daddy issues, uh?":
            $ JubesX.change_stat("love", 90, -15)
            $ JubesX.change_stat("obedience", 80, 45)
            $ JubesX.change_stat("inhibition", 70, 5)
            $ JubesX.change_face("_angry")
            ch_v ". . . Probably."
            ch_v "Never mind."
    $ JubesX.player_petnames.append("daddy")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
