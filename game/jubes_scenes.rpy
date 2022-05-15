label Jubes_Meet:
        #jubilee's introduction scene
        #called from Sleepover if bg_current == "bg_player" and "met" in StormX.History and "met" not in JubesX.History:

        show blackscreen onlayer black
        $ JubesX.OutfitDay = "casual2"
        $ JubesX.Outfit = "casual2"
        $ JubesX.OutfitChange("casual2")
        call clear_the_room("all",0,1)
        $ JubesX.location = bg_current
        $ JubesX.love = 500
        $ JubesX.obedience = 50
        $ JubesX.inhibition = 50
        $ JubesX.sprite_location = StageCenter

        $ JubesX.names = []
        $ JubesX.name = "???"

        $ Player.AddWord(1,"interruption") #prevents interruption
        $ Player.Focus = 30
        ch_u "\"Slurp, slurp, slurp.\""

        $ Player.change_stat("Focus", 80, 5)
        $ JubesX.change_stat("lust", 80, 5)

        $ JubesX.change_face("sucking",1)

        "You feel a pleasant sensation. . ."
        ch_u "\"Slurp, slurp, slurp.\""
        $ Player.change_stat("Focus", 80, 5)
        $ JubesX.change_stat("lust", 80, 5)
        $ JubesX.Addictionrate += 1 #starts her addiction path

        "It's somewhere below your waist. . ."
        ch_u "\"Slurp, slurp, slurp.\""
        $ Player.change_stat("Focus", 80, 10)
        $ JubesX.change_stat("lust", 80, 5)

        "Wait. . . no it's not. . ."
        call shift_focus(JubesX)

        $ JubesX.ArmPose = 2
        show Jubes_Sprite at sprite_location(StageRight) zorder JubesX.Layer:
            ease 0.1 offset (100,50) zoom 2.5 alpha 1
            block:
                ease 1 yoffset 100
                pause .2
                ease 1 yoffset 50
                repeat

        "You open your eyes. . ."
        hide blackscreen onlayer black

        $ Count = 3
        $ line = 0
        "Someone seems to be giving you a hickey on your neck. . ."
        while Count > 0:
                #Looping portion
                $ Player.change_stat("Focus", 80, 10)
                $ JubesX.change_stat("lust", 80, 5)
                menu:
                    extend ""
                    "Stay Quiet":
                        $ JubesX.change_stat("inhibition", 90, 2)
                        $ JubesX.change_stat("lust", 80, 5)
                        $ JubesX.Addictionrate += 1
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
                            show blackscreen onlayer black
                            ". . ."
                            $ JubesX.change_stat("love", 90, 2)
                            $ JubesX.change_face("surprised",2)
                            show Jubes_Sprite:
                                ease 0.2 offset (100,50) zoom 2.5 alpha 1
                            ch_v "Whoa! Um. . . this is bad. . ."
                            ch_v "Wake up! Wake up! Sorry!!!!"
                            "You slowly pull yourself back. . ."
                            hide blackscreen onlayer black
                            ch_v "Sorry!"
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "I think I maybe drained a bit too much!"
                            $ JubesX.change_face("sadside",1)
                            ch_v "I was just. . . thirsty. . ."
                    "Um. . . lady? What're you doing?":
                            $ JubesX.change_stat("obedience", 90, 5)
                            $ JubesX.change_stat("inhibition", 90, -1)
                            $ JubesX.change_face("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Ah!"
                            $ JubesX.change_face("sadside",1,Mouth="normal")
                            ch_v "Oh, I guess I was. . ."
                            $ Count = 1
                    "That feels great, keep going. . .":
                            $ JubesX.change_stat("love", 90, 2)
                            $ JubesX.change_stat("inhibition", 90, 2)
                            $ JubesX.change_face("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Oh!"
                            $ JubesX.change_face("sadside",1,Mouth="smile")
                            ch_v "I, um. . . I wasn't expecting that reaction. . ."
                            $ JubesX.change_face("sad",1,Mouth="smile")
                            $ Count = 1
                    "Hey, quit that!":
                            $ JubesX.change_stat("obedience", 90, 10)
                            $ JubesX.change_stat("inhibition", 90, -3)
                            $ JubesX.change_face("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Ah!"
                            $ JubesX.change_face("sadside",1,Mouth="normal")
                            ch_v "Sorry!"
                            $ Count = 1
                $ Count -= 1
        $ JubesX.Blush = 1
        show Jubes_Sprite at sprite_location(JubesX.sprite_location,50)
        $ Count = 3
        while Count > 0:
            menu:
                extend ""
                "Who are you?" if "Jubilee" not in JubesX.names:
                        $ JubesX.change_stat("love", 90, 2)
                        $ JubesX.change_stat("obedience", 90, 1)
                        $ JubesX.change_face("smile",1)
                        ch_v "Oh, I guess I should introduce myself."
                        ch_v "The name's \"Jubilee.\""
                        $ JubesX.names.append("Jubilee")
                        $ JubesX.name = "Jubilee"
                        ch_v "Nice to ea- meet you."
                        menu:
                            extend ""
                            "Ok. . .":
                                    $ JubesX.change_face("confused",1)
                                    $ JubesX.change_stat("obedience", 90, 3)
                                    ch_v ". . ."
                            "My name's [Player.name]":
                                    $ JubesX.change_stat("love", 90, 3)
                                    $ JubesX.change_stat("obedience", 90, 2)
                                    ch_v "Oh, yeah, I know that."
                                    $ JubesX.change_stat("inhibition", 90, 2)
                                    ch_v "I've. . . heard about you."
                            "Huh.":
                                    $ JubesX.change_face("confused",1)
                                    ch_v ". . ."
                #end "who are you"


                "That's an interesting name." if "Jubilee" in JubesX.names and "Jubilation" not in JubesX.names:
                        #only plays after Jubilee but before this bit
                        $ JubesX.change_face("smile",1)
                        ch_v "Oh, yeah. Weird parents."
                        ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
                        ch_v "Guess I leaned into it?"
                        $ JubesX.names.append("Jubilation")
                        $ JubesX.names.append("Miss Lee")
                        $ JubesX.Pets.append("Miss Lee")
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
                                    $ JubesX.change_face("angry",1)
                                    $ JubesX.change_stat("love", 90, -3)
                                    $ JubesX.change_stat("obedience", 90, 3)
                                    $ JubesX.change_stat("inhibition", 90, 1)
                                    ch_v ". . ."
                                    $ JubesX.change_face("normal",1)
                #end "interesting name"


                "What are you doing in my room?!" if "thirst" not in JubesX.recent_history:
                        $ JubesX.change_stat("love", 90, -1)
                        $ JubesX.change_stat("obedience", 90, 7)
                        $ JubesX.change_stat("inhibition", 90, -2)
                        $ JubesX.change_face("startled",2)
                        ch_v "Oh, I was just. . . thirsty?"
                        $ JubesX.change_face("smile",1)
                        $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent

                #end "what are you in my room"
                "What were you doing?" if "thirst" not in JubesX.recent_history:
                        $ JubesX.change_stat("inhibition", 90, 1)
                        $ JubesX.change_face("startled",2)
                        ch_v "I was just. . . getting a drink?"
                        $ JubesX.change_face("smile",1)
                        $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent

                #end "what are you doing"


                "So you drink blood?" if "vamp" in JubesX.recent_history and "blood" not in JubesX.recent_history:
                        $ JubesX.change_stat("love", 90, 1)
                        $ JubesX.change_face("sadside",2)
                        ch_v "Yeah, I kinda have to. . ."
                        $ JubesX.change_face("sad",1)
                        ch_v "Sorry again. . ."
                        $ JubesX.AddWord(1,"blood",0,0,0) #adds "word" tag to Recent
                "Can you turn into a bat?" if "vamp" in JubesX.recent_history and "bat" not in JubesX.recent_history:
                        $ JubesX.change_stat("love", 90, 1)
                        $ JubesX.change_face("confused",1)
                        ch_v "Well, no. . ."
                        $ JubesX.change_face("sly",1)
                        ch_v "But I am strong and can turn into mist."
                        ch_v "Sometimes."
                        $ JubesX.AddWord(1,"bat",0,0,0) #adds "word" tag to Recent
                "Is it contagious?" if "vamp" in JubesX.recent_history and "contagious" not in JubesX.History:
                        $ JubesX.change_face("sadside",2)
                        ch_v "Infectious. . ."
                        $ JubesX.change_face("surprised",1,Mouth="sucking")
                        ch_v "- and no!"
                        $ JubesX.change_face("sadside",1)
                        ch_v "It was, but Dr. Strange was able to cast a spell or something."
                        ch_v "So you don't need to worry about it spreading to you or anything."
                        $ JubesX.change_face("sad",1)
                        $ JubesX.AddWord(1,0,0,0,"contagious") #adds "word" tag to History
                "Why me?" if "vamp" in JubesX.recent_history and "devamp" not in JubesX.recent_history:
                        $ JubesX.change_stat("love", 90, 1)
                        $ JubesX.change_face("sly",1,Eyes="side")
                        ch_v "Well. . ."
                        ch_v "I had a theory. . ."
                        ch_v "I sorta figured that if you could negate powers, then maybe. . ."
                        $ JubesX.change_face("smile",1)
                        ch_v "Maybe you could \"de-vampire\" me?"
                        $ JubesX.AddWord(1,"devamp",0,0,0) #adds "word" tag to Recent
                        menu:
                            extend ""
                            "You don't want to be a vampire":
                                    $ JubesX.change_stat("love", 90, 2)
                                    $ JubesX.change_stat("obedience", 90, 1)
                                    ch_v "Well, no. . ."
                            "I guess.":
                                    $ JubesX.change_face("confused",1)
                                    $ JubesX.change_stat("love", 90, -1)
                                    ch_v ". . ."
                        ch_v "The powers are cool and all, but I can't even go out during the daytime!"
                        ch_v "and the blood drinking, of course."
                        $ JubesX.change_face("normal",1)

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
                        $ JubesX.change_face("smile",1)
                        ch_v "Yeah! Of course I am!"
                        $ JubesX.change_face("smile",1,Eyes="side")
                        if "vamp" in JubesX.recent_history:
                                ch_v "You know, among other things. . ."
                        else:
                                ch_v ". . . among other things. . ."
                        $ JubesX.AddWord(1,"mutant",0,0,0) #adds "word" tag to Recent
                        menu:
                            extend ""
                            "So what's your power?":
                                    $ JubesX.change_stat("love", 90, 3)
                                    $ JubesX.change_stat("inhibition", 90, 1)
                                    ch_v ". . ."
                            "Oh, ok.":
                                    $ JubesX.change_stat("love", 90, -1)
                                    $ JubesX.change_stat("obedience", 90, 3)
                                    $ JubesX.change_face("confused",1)
                                    ch_v "Not even curious about what I can do?"
                        $ JubesX.change_face("smile",1)
                        ch_v "I can shoot fireworks."
                        $ JubesX.ArmPose = 1
                        show Fireworks onlayer black as Fire1:
                                pos (JubesX.sprite_location+300,350)#+160,270)
                        show Fireworks onlayer black as Fire2:
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
                                    $ JubesX.change_face("angry",1,Eyes="side")
                                    ch_v "Ok, so it's not \"negating mutant powers\" cool or anything. . ."
                                    ch_v "I can do other stuff. . ."
                                    $ JubesX.change_face("normal",1)
                            ". . .":
                                    $ JubesX.change_stat("obedience", 90, 2)
                                    ch_v ". . ."


                "Well, I guess I'm out of questions.":
                    $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent if she's missed it so far
                    $ Count = 0

            if "thirst" in JubesX.recent_history and "vamp" not in JubesX.recent_history:
                    "You feel a tickle on your neck and rub it, coming back with a trickle of blood on your fingers."
                    menu:
                        extend ""
                        "Oh. Blood. . .":
                                $ JubesX.change_stat("love", 90, 2)
                                $ JubesX.change_stat("obedience", 90, 3)
                                $ JubesX.change_stat("inhibition", 90, -2)
                                $ JubesX.change_face("angry",1,Eyes="squint",Mouth="kiss")
                                ch_v "You are -remarkably- chill about this."
                                $ JubesX.change_face("smile",1,Eyes="surprised", Brows = "sad")
                                ch_v "Maybe I took too much? . ."
                        "Why is my neck bleeding?":
                                $ JubesX.change_stat("love", 90, 4)
                                $ JubesX.change_stat("obedience", 90, 2)
                                $ JubesX.change_face("sadside",1)
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
                    $ JubesX.change_face("sadside",1)
                    ch_v "So. . . I'm. . . a vampire?"
                    $ JubesX.AddWord(1,"vamp",0,0,0) #adds "word" tag to Recent
                    menu:
                        extend ""
                        "This isn't a refreshment stand!":
                                $ JubesX.change_stat("love", 90, 1)
                                $ JubesX.change_stat("obedience", 90, 3)
                                $ JubesX.change_stat("inhibition", 90, 1)
                                $ JubesX.change_face("sly",1)
                                ch_v "Says you."
                        "A vampire. . .":
                                ch_v ". . . Yeah. . ."
                        "Oh. Gotcha.":
                                $ JubesX.change_stat("love", 90, 2)
                                $ JubesX.change_stat("obedience", 90, 2)
                                $ JubesX.change_stat("inhibition", 90, -1)
                                $ JubesX.change_face("perplexed",1)
                                ch_v "Maybe we should take you to the medbay. . ."
                    $ Count += 1

            #loops back into menu

        # End while loop

        if "Jubilee" not in JubesX.names:
                $ JubesX.change_stat("love", 90, -5)
                $ JubesX.change_stat("obedience", 90, 10)
                $ JubesX.change_face("angry",1)
                ch_v "Seriously? You don't even want to know my fucking name?"
                $ JubesX.change_face("sadside",1,Brows="angry")
                ch_v "How many girls do you have going through this place?"
                ch_v ". . ."
                $ JubesX.change_face("angry",1)
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
                            $ JubesX.change_face("smile",1)
                            ch_v "You catch on quick. . ."
                    "Most nights are, yeah.":
                            $ JubesX.change_face("confused",1)
                            ch_v "Wha. . . oh."
                            $ JubesX.change_stat("love", 90, 10)
                            $ JubesX.change_stat("obedience", 90, 5)
                            $ JubesX.change_stat("inhibition", 90, 15)
                            $ JubesX.change_face("smile",1)
                            ch_v "Heh."
                            ch_v "Ok, that's cool. No, I meant my -name- is Jubilee."
                            ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
                $ JubesX.name = "Jubilee"
                $ JubesX.names.append("Jubilation")
                $ JubesX.names.append("Miss Lee")
                $ JubesX.Pets.append("Miss Lee")
                ch_v "And I know your name's [Player.name], obviously."
        if "devamp" not in JubesX.recent_history:
                $ JubesX.change_face("sadside",1)
                ch_v "Anyway, I just figured that maybe your blood could reverse this \"vampire\" thing."
        menu:
            extend ""
            "So do you feel any different?":
                    $ JubesX.change_stat("love", 90, 5)
                    $ JubesX.change_stat("inhibition", 90, 2)
                    $ JubesX.change_face("smile",1)
            ". . .":
                $ JubesX.change_stat("love", 90, -2)
                $ JubesX.change_stat("obedience", 90, 2)
                $ JubesX.change_face("perplexed",1)
                ch_v "You don't even want to ask about the \"vampire\" thing?"
                menu:
                    extend ""
                    "Oh, yeah, how are you doing?":
                            $ JubesX.change_stat("love", 90, 1)
                            $ JubesX.change_stat("inhibition", 90, 1)
                            $ JubesX.change_face("smile",1)
                    "Not really.":
                            $ JubesX.change_stat("love", 90, -3)
                            $ JubesX.change_stat("obedience", 90, 3)
                            $ JubesX.change_face("angry",1)
                            ch_v "Well that's a bad start!"
                    "Oh, ok.":
                            $ JubesX.change_face("confused",1)
                            ch_v ". . ."

        ch_v "I guess. . . not that much different."
        ch_v "Still have the teeth, the. . . thirst."
        $ JubesX.change_face("sadside",1)
        ch_v "I guess I'm still a vampire."
        $ JubesX.change_face("normal",1)
        ch_v "But I do feel a bit better. . ."
        $ JubesX.change_face("sad",1)
        ch_v "I am sorry, I shouldn't have attacked you like that."
        ch_v "Not cool, I know."
        menu:
            extend ""
            "It's ok, I get it.":
                    $ JubesX.change_stat("love", 90, 5)
                    $ JubesX.change_stat("obedience", 90, -1)
                    $ JubesX.change_stat("inhibition", 90, 2)
                    $ JubesX.change_face("smile",1)
                    ch_v "Thanks."
                    ch_v "Is there any way I could make it up to you?"
            "Why not make it up to me?":
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_face("sexy",1)
                    ch_v "Oh?"
            "How dare you!":
                    $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.change_stat("inhibition", 90, -1)
                    $ JubesX.change_face("surprised",1)
                    ch_v "I know! I know!"
                    $ JubesX.change_face("smile",1)
                    ch_v "I can make it up to you!"
            ". . .":
                    $ JubesX.change_stat("inhibition", 90, 3)
                    $ JubesX.change_face("sly",1)
                    ch_v "So. . . I guess I could make it up to you?"
        menu:
            extend ""
            "That's not necessary.":
                    $ JubesX.change_stat("love", 90, 5)
                    $ JubesX.change_stat("inhibition", 90, 1)
                    $ JubesX.change_face("smile",1)
                    ch_v "That's sweet of you."
                    ch_v "Seriously though, I'll think of something. . ."
            "A kiss, maybe?":
                    $ JubesX.change_stat("love", 90, 3)
                    $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.change_stat("inhibition", 90, 2)
                    $ JubesX.change_face("sly",1)
                    ch_v "I heard you're a charmer."
                    ch_v "Well, I guess. . . one. . ."
                    $ JubesX.change_face("kiss")
                    show Jubes_Sprite:
                        ease 0.5 offset (0,0) zoom 2
                    pause 1
                    show Jubes_Sprite:
                        ease 0.5 offset (100,0) zoom 1.5
                    $ JubesX.change_face("sly",1)
                    ch_v ". . ."
            "You could flash me?":
                    $ JubesX.change_stat("obedience", 90, 3)
                    if Approvalcheck(JubesX, 620):
                            $ JubesX.change_stat("love", 90, 2)
                            $ JubesX.change_stat("inhibition", 90, 1)
                            $ JubesX.change_face("sly",1)
                            ch_v "I guess I could. . ."
                            $ JubesX.change_face("smile",1,Mouth="sucking")
                    else:
                            $ JubesX.change_stat("love", 90, -2)
                            $ JubesX.change_stat("obedience", 90, 1)
                            $ JubesX.change_face("angry",1,Mouth="sucking")
                    $ JubesX.ArmPose = 1
                    show Fireworks onlayer black as Fire1:
                            pos (JubesX.sprite_location+250,350)
                    show Fireworks onlayer black as Fire2:
                            pos (JubesX.sprite_location+250,350)
                    ch_v "As if."
                    $ JubesX.change_face("smile",1)

            "A blowjob?":
                    if Approvalcheck(JubesX, 620):
                            $ JubesX.change_stat("love", 90, 1)
                            $ JubesX.change_stat("obedience", 90, 5)
                            $ JubesX.change_stat("inhibition", 90, 1)
                            $ JubesX.change_face("smile",1,Mouth="sucking")
                    else:
                            $ JubesX.change_stat("love", 90, -5)
                            $ JubesX.change_stat("obedience", 90, 2)
                            $ JubesX.change_face("angry",1,Mouth="sucking")

                    ch_v "Hey, I may suck more than most, but even I'm not that easy!"
                    $ JubesX.change_face("smile",1)
        ch_v "Anyway, I should get going before dawn."
        ch_v "I might see you around sometime."
        ch_v "In the moonlight. . ."
        $ JubesX.AddWord(1,0,0,0,"met") #adds "word" tag to History
        $ active_Girls.append(JubesX) if JubesX not in active_Girls else active_Girls
        hide Jubes_Sprite with easeoutright
        call remove_girl(JubesX)
        "[JubesX.name] leaves the room, you might as well get some sleep. . ."
        return

label Jubes_Sunshine:
        #called from EventCalls if "sunshine" not in JubesX.History and "traveling" in Player.recent_history and bg_current in ("bg_classroom","bg_campus"):
        call shift_focus(JubesX)
        $ bg_current = "bg_campus"
        $ JubesX.location = "bg_campus"
        call clear_the_room(JubesX,0,1)
        call AltClothes(JubesX,1)
        call set_the_scene
        $ JubesX.change_face("smile")
        "On your way across the square, you see a shape charging toward you."
        call Punch
        "[JubesX.name] crashes into you."
        $ JubesX.change_face("smile",1,Mouth="sucking")
        ch_v "Hey, [Player.name]!"
        $ JubesX.change_face("smile",1)
        ch_v "check it out!"
        menu:
            extend ""
            "Oh, hey. . .":
                    $ JubesX.change_stat("love", 90, 2)
                    $ JubesX.change_face("smile",1,Mouth="sucking")
                    ch_v "Yes, \"hey,\" but I am -outside!-"
                    $ JubesX.change_stat("inhibition", 90, 2)
                    $ JubesX.change_face("smile",1)
                    ch_v "During the daytime!"
            "You're out during the day!":
                    $ JubesX.change_stat("love", 90, 5)
                    $ JubesX.change_stat("inhibition", 90, 2)
            "check what out?":
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("obedience", 90, 2)
                    ch_v "Look!"
                    ch_v "I'm -outside!-"
                    $ JubesX.change_stat("inhibition", 90, 2)
                    $ JubesX.change_face("smile",1,Mouth="sucking")
                    ch_v "During the -daytime!-"
                    $ JubesX.change_face("smile")
            "What the hell?":
                    $ JubesX.change_stat("love", 90, -3)
                    $ JubesX.change_stat("obedience", 90, 5)
                    $ JubesX.change_face("surprised",2,Mouth="sucking")
                    ch_v "Sorry! I was just so excited!"
                    $ JubesX.change_face("smile",1)
                    ch_v "I'm outside, during the daylight!"
        menu:
            extend ""
            "That's great!":
                    $ JubesX.change_stat("love", 90, 5)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("inhibition", 90, 1)
                    $ JubesX.change_face("surprised",1,Mouth="sucking")
                    ch_v "Right?!"
                    $ JubesX.change_face("smile",1)
            "So what? So am I.":
                    $ JubesX.change_stat("love", 90, -5)
                    $ JubesX.change_stat("obedience", 90, 5)
                    $ JubesX.change_face("confused",1)
                    ch_v "Yes. . ."
                    ch_v "But I am a -vampire,- remember?"
            "Ok.":
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("inhibition", 90, 2)
                    $ JubesX.change_face("confused",1)
                    ch_v ". . . I'm a -vampire?-"
        $ JubesX.change_face("surprised",1,Mouth="sucking")
        ch_v "I didn't used to be able to do this without catching fire!"
        $ JubesX.change_face("smile",1)
        menu:
            extend ""
            "So do you know why?":
                    $ JubesX.change_stat("love", 90, 1)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("inhibition", 90, 1)
            "Well it was never a problem for me.":
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("obedience", 90, 3)
                    $ JubesX.change_face("confused",1)
                    ch_v ". . ."
                    ch_v "No, I get that it wouldn't be. . ."
                    $ JubesX.change_face("normal",1)
            "Neat.":
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("inhibition", 90, 1)
                    $ JubesX.change_face("confused",1)
                    ch_v ". . ."
                    $ JubesX.change_face("normal",1)
            "Ok.":
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("inhibition", 90, 2)
                    $ JubesX.change_face("angry",1)
                    ch_v ". . ."
                    $ JubesX.change_face("normal",1)
        ch_v "I don't really know what caused it, but I guess it had to do with your blood. . ."
        $ JubesX.change_face("smile",1)
        ch_v "Anyway, I just wanted to say \"thank you,\" this is great!"
        $ JubesX.AddWord(1,0,0,0,"sunshine") #adds "word" tag to History
        hide Jubes_Sprite with easeoutright
        call remove_girl(JubesX)
        "[JubesX.name] dashes off, and you continue on your way. . ."
        return

label Jubes_Entry_check:
        #checks to see if she is trying to follow you and if she will.
        if JubesX not in Party:
                return
        call Jubes_Sunshock #checks to see if she has to stay
        if _return:
                #if she couldn't go with you
                menu:
                    "Ok then, we can stay here.":
                            if "stayed" in JubesX.recent_history:
                                    # you stay, but not for the first time recently
                                    $ Girl.change_stat("love", 80, -2)
                                    ch_v "Now I kind feel like you're jerking me around. . ."
                            elif Approvalcheck(JubesX, 1300) or Approvalcheck(JubesX, 400, "O"):
                                ch_v "That's really not necessary, don't let me hold you back."
                                menu:
                                    extend ""
                                    "I inist.":
                                        # you stay
                                        $ JubesX.change_face("smile",1)
                                        $ Girl.change_stat("love", 80, 2)
                                        $ JubesX.change_stat("inhibition", 60, 2)
                                        ch_v "Aw, thanks. That's sweet of you."
                                    "Ok, sorry about that.":
                                        # you go
                                        $ JubesX.change_stat("obedience", 90, 2)
                                        $ JubesX.change_face("sad",1)
                                        $ Party.remove(JubesX)
                                        "You leave her behind."
                                        return
                                    "Cool, later then.":
                                        # you go
                                        $ Girl.change_stat("love", 80, -2)
                                        $ JubesX.change_stat("obedience", 90, 2)
                                        $ JubesX.change_face("sad",1)
                                        $ Party.remove(JubesX)
                                        "You leave her behind."
                                        return
                            else:
                                        # you stay
                                        ch_v "Thanks, that's sweet of you."
                            $ JubesX.AddWord(1,"stayed",0,0,0) #adds "word" tag to recent
                            jump Misplaced
                    "Oh, too bad, you can stay here then.":
                            # you go
                            $ Party.remove(JubesX)
                            $ Girl.change_stat("love", 80, -2)
                            $ JubesX.change_stat("obedience", 70, 2)
                            if Approvalcheck(JubesX, 1300) or Approvalcheck(JubesX, 400, "O"):
                                    $ JubesX.change_stat("obedience", 90, 2)
                                    $ JubesX.change_face("sad",1)
                                    ch_v "I understand, later then. . ."
                            else:
                                    $ Girl.change_stat("love", 80, -4)
                                    $ JubesX.change_face("angry",1,Mouth="sucking")
                            "You leave her behind."
                            $ JubesX.change_face("sad",1)
        return

label Jubes_Sunshock:
        #this is called when Jubilee is asked to go out in the sublight with higher than 50% addiction
        #returns 1 if she doesn't go along with it.

        if JubesX.Addict <= 50 or time_index > 2:
                #if below the threshold or it's night time, ignore this
                return 0
        $ JubesX.change_face("sad",1)
        if "sunshock" in JubesX.recent_history:
                ch_v "Like I said, I'm not up for the sunshine."
                return 1
        $ JubesX.AddWord(1,"sunshock",0,0,0) #adds "word" tag to recent
        ch_v "Oh, wait, I'm kinda on a \"low charge\" at the moment, so I don't really want to go out in the sunlight?"
        menu:
            extend ""
            "Oh, sorry, that's fine.":
                    $ JubesX.change_stat("love", 90, 1)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_stat("inhibition", 90, 1)
                    $ JubesX.change_face("smile",1)
                    ch_v "Thanks for understanding. . ."
                    return 1

            "I could always. . . come get you?" if bg_current != JubesX.location and JubesX not in Party:
                    #if she's not local. . .
                    ch_v "Oh, that could be nice. I'll see you then."
                    return 1

            "I could always. . . top you off?" if bg_current == JubesX.location or JubesX in Party:
                    # only works if she is local to you
                    $ JubesX.change_stat("love", 80, 1)
                    $ JubesX.change_face("confused",1)
                    ch_v "Oh? What'd you have in mind?"
                    menu:
                        extend ""
                        "Nothing, just touch whatever you like.":
                            if Girl.Petname in ("master", "sir"):
                                    $ Girl.change_stat("lust", 80, 3)
                                    $ Girl.change_stat("love", 70, 1)
                                    $ Girl.change_stat("love", 95, 1)
                                    $ Girl.change_face("sexy")
                                    ch_v "Then I suppose I choose. . ."
                                    "She leans in for a kiss."
                                    call KissPrep(Girl)
                            elif Approvalcheck(Girl, 650, "LI"):
                                    $ Girl.change_stat("lust", 80, 3)
                                    $ Girl.change_stat("love", 80, 5)
                                    $ Girl.change_face("sexy")
                                    ch_v "Oh! Then how about I just try a simple touch. . ."
                                    "She leans in for a kiss."
                                    call KissPrep(Girl)
                            else:
                                    $ Girl.change_stat("lust", 80, 3)
                                    $ Girl.change_stat("love", 80, 6)
                                    $ Girl.change_face("smile")
                                    call Girl_Tag(Girl)
                            while Girl.Addict > 20 and Round > 10:
                                    #should remove addiction by 1 unit per round until either it stabilizes or time runs out.
                                    $ Girl.Addict -= 1
                                    $ Round -= 1
                                    if Round == 10:
                                            call Anyline(Girl,"I suppose we don't have time for any more than that.")
                        #end "Nothing, just touch whatever you like.":

                        "How about a kiss?":
                                if Girl.Kissed or Approvalcheck(Girl, 600, "LI") or Girl.Petname in ("master", "sir"):
                                        $ Girl.Forced = 0
                                        $ Girl.change_stat("lust", 80, 3)
                                        $ Girl.change_stat("love", 80, 6)
                                        $ Girl.change_face("sexy")
                                        ch_v "You've convinced me. . ."
                                        "She leans in for a kiss."
                                        call KissPrep(Girl)
                                        $ Girl.Addict = 20 if Girl.Addict > 20 else Girl.Addict
                                else:
                                        ch_v "I don't like you like that. . ."

                        "How about you let me touch you instead?":
                                ch_v "Oh, I don't know about that. . ."
                                menu:
                                    extend ""
                                    "How about you let me touch your breasts?":
                                            $ stored_count = temp_modifier
                                            call Top_Off(Girl,2)
                                            $ temp_modifier = stored_count
                                            call expression Girl.Tag + "_Fondle_Breasts"
                                            if "fondle_breasts" in Girl.recent_history:
                                                    $ Girl.change_stat("obedience", 80, 10)
                                                    $ Girl.change_stat("inhibition", 80, 10)
                                                    ch_v "So, fair trade?"

                                    "How about you just let me touch your thighs?":
                                            $ stored_count = temp_modifier
                                            call Bottoms_Off(Girl,2)
                                            $ temp_modifier = stored_count
                                            if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                                    ch_v "Well, we'll see. . ."
                                            call expression Girl.Tag + "_Fondle_Thighs"
                                            if "fondle_thighs" in Girl.recent_history:
                                                    $ Girl.change_stat("obedience", 50, 5)
                                                    $ Girl.change_stat("inhibition", 50, 5)
                                                    ch_v "So, fair trade?"
                                                    if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                                            call Girl_Tag(Girl)

                                    "How about you let me touch your pussy?":
                                            $ stored_count = temp_modifier
                                            call Bottoms_Off(Girl,0)
                                            $ temp_modifier = stored_count
                                            call expression Girl.Tag + "_Fondle_Pussy"
                                            if "fondle_pussy" in Girl.recent_history:
                                                    $ Girl.change_stat("obedience", 50, 10)
                                                    $ Girl.change_stat("obedience", 80, 5)
                                                    $ Girl.change_stat("inhibition", 50, 10)
                                                    $ Girl.change_stat("inhibition", 80, 5)
                                                    ch_v "That was plenty, right?"

                                    "Never mind then":
                                            $ JubesX.change_stat("love", 90, -3)
                                            $ JubesX.change_stat("obedience", 70, 1)
                                            $ JubesX.change_stat("obedience", 90, 2)
                                            $ JubesX.change_face("angry",1)
                        "Oh, never mind.":
                                $ JubesX.change_stat("love", 70, -2)
                                $ JubesX.change_stat("love", 90, -2)
                                $ JubesX.change_stat("obedience", 70, 1)
                                $ JubesX.change_stat("obedience", 90, 2)
                                $ JubesX.change_face("angry",1)

                        #end Sunshock treatment menu

                    if JubesX.Addict >= 70:
                            $ JubesX.change_stat("inhibition", 70, 1)
                            $ JubesX.change_stat("inhibition", 80, 1)
                            ch_v "Couldn't I just touch you real quick?"
                            menu:
                                extend ""
                                "Sure.":
                                        $ Girl.change_stat("lust", 80, 3)
                                        $ Girl.change_stat("love", 80, 6)
                                        $ Girl.change_face("smile")
                                        call Girl_Tag(Girl)
                                "Nope, sorry.":
                                        $ JubesX.change_stat("love", 80, -3)
                                        $ JubesX.change_stat("obedience", 70, 2)
                                        if Approvalcheck(JubesX, 1300) or Approvalcheck(JubesX, 400, "O"):
                                                $ JubesX.change_face("sad",1)
                                                ch_v "Oh."
                                        else:
                                                $ JubesX.change_stat("love", 90, -2)
                                                $ JubesX.change_stat("obedience", 90, 2)
                                                $ JubesX.change_face("angry",1)
                                                ch_v "Jerk."

                    if JubesX.Addict >= 70:
                            #this is too high, she will refuse outright.
                            if Approvalcheck(JubesX, 1300) or Approvalcheck(JubesX, 400, "O"):
                                    $ JubesX.change_face("sad",1)
                                    ch_v "I'm sorry, I just can't, it would be agonizing."
                            else:
                                    $ JubesX.change_face("angry",1)
                                    ch_v "You have to be kidding! I'd catch fire!"
                            return 1
                    elif Approvalcheck(JubesX, 1600) or Approvalcheck(JubesX, 500, "O"):
                            $ JubesX.change_stat("obedience", 90, 2)
                            $ JubesX.change_stat("inhibition", 80, 2)
                            ch_v "I guess I could manage it for a little bit. . ."
                    else:
                            ch_v "Grow up. . ."
                            return 1
            #end "I could always. . . top you off?":

            "Come on, don't be like that.":
                    $ JubesX.change_stat("love", 70, -2)
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_face("sad",1)
                    if JubesX.Addict >= 70:
                            #this is too high, she will refuse outright.
                            if Approvalcheck(JubesX, 1300) or Approvalcheck(JubesX, 400, "O"):
                                    $ JubesX.change_stat("obedience", 90, 2)
                                    ch_v "I'm sorry, I just can't, it would be agonizing."
                            else:
                                    $ JubesX.change_face("angry",1)
                                    ch_v "You have to be kidding! I'd catch fire!"
                            return 1
                    elif Approvalcheck(JubesX, 1600) or Approvalcheck(JubesX, 500, "O"):
                            $ JubesX.change_stat("obedience", 90, 2)
                            $ JubesX.change_stat("inhibition", 80, 2)
                            ch_v "I guess I could manage it for a little bit. . ."
                    else:
                            ch_v "Grow up. . ."
                            return 1
        return 0

label Jubes_Mall(Girls=[]):
        #this is called to introduce the mall element

        call shift_focus(JubesX)
        if JubesX.location == bg_current:
                "[JubesX.name] suddently freezes up, then turns to you."
        else:
                $ JubesX.location = bg_current
                "[JubesX.name] rushes into the room."
        call clear_the_room(JubesX,0,0) #she asks
        call set_the_scene
        $ Player.AddWord(1,0,0,0,"mall") #history

        $ JubesX.change_face("surprised",1,Mouth="sucking")
        ch_v "Hey, I just realized something!"
        $ JubesX.change_face("smile")
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
                    $ JubesX.change_face("angry",1,Mouth="sucking")
                    ch_v "This is serious!"
            ". . .":
                $ JubesX.change_stat("love", 90, -1)
                $ JubesX.change_face("confused")
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
                            $ JubesX.change_face("angry")
                            ch_v "Dick."
                    ". . .":
                            $ JubesX.change_stat("love", 90, -1)
                            $ JubesX.change_stat("obedience", 60, 1)
                            ch_v "Ooookaaay. . ."
        $ JubesX.change_face("surprised",1,Mouth="sucking")
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
                                $ JubesX.change_face("confused")
                                ch_v "Of course there's a mall! What town doesn't have a mall?!"
                        "Did you want to go?":
                                $ JubesX.change_stat("love", 80, 2)
                                $ JubesX.change_stat("love", 90, 1)
                                $ JubesX.change_stat("inhibition", 70, 1)
            "Oh, ok.":
                    $ JubesX.change_stat("love", 90, -1)
                    $ JubesX.change_stat("obedience", 90, 1)
                    $ JubesX.change_face("sad")
            "Wait, there's a mall?":
                    $ JubesX.change_stat("love", 80, 1)
                    $ JubesX.change_stat("inhibition", 70, 1)
                    $ JubesX.change_face("confused")
                    ch_v "Of course there's a mall! What town doesn't have a mall?!"
            "Ok, whatever.":
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("obedience", 50, 2)
                    $ JubesX.change_stat("obedience", 90, 2)
                    $ JubesX.change_stat("inhibition", 50, -1)
        $ JubesX.change_face("surprised",1,Mouth="sucking")
        ch_v "We've got to go there, right now!"
        $ JubesX.change_face("smile")
        $ Party = [JubesX]
        menu:
            "Ok, let's check it out.":
                    $ JubesX.change_stat("love", 80, 2)
                    $ JubesX.change_stat("love", 90, 1)
                    $ JubesX.change_stat("inhibition", 60, 1)
                    show blackscreen onlayer black with dissolve
                    "You both head out of the room."
            "You can go, I don't need anything.":
                    $ JubesX.change_stat("love", 80, 2)
                    $ JubesX.change_stat("obedience", 60, 1)
                    $ JubesX.change_stat("obedience", 80, 1)
                    ch_v "Come'on, you gotta go!"
                    ch_v "You don't know what you're missing!"
                    show blackscreen onlayer black with dissolve
                    "[JubesX.name] can be surprisingly forceful. . ."
            "Nah.":
                    $ JubesX.change_stat("love", 50, -2)
                    $ JubesX.change_stat("love", 90, -2)
                    $ JubesX.change_stat("inhibition", 50, 2)
                    $ JubesX.change_stat("inhibition", 60, 2)
                    $ JubesX.change_face("angry",1,Mouth="sucking")
                    ch_v "Stow the 'tude, we're going!"
                    $ JubesX.change_face("smile")
                    show blackscreen onlayer black with dissolve
                    "[JubesX.name] can be surprisngly forceful. . ."
            "Actually, I planned to-":
                    $ JubesX.change_stat("love", 50, -1)
                    $ JubesX.change_stat("love", 90, -1)
                    $ JubesX.change_stat("inhibition", 50, 1)
                    $ JubesX.change_stat("inhibition", 60, 1)
                    $ JubesX.change_face("surprised",1,Mouth="sucking")
                    ch_v "No time! We're going!"
                    $ JubesX.change_face("smile")
                    show blackscreen onlayer black with dissolve
                    "[JubesX.name] can be surprisngly forceful. . ."
        "You arrive at what appears to be a mid-sized suburban shopping complex, often referred to as a \"mall.\""

        $ bg_current = "bg_mall"
        $ JubesX.location = bg_current
        call clear_the_room(JubesX,0,1) #it's silent
        call set_the_scene

        $ JubesX.change_face("smile")
        ch_v "Welcome to the Salem Centre Mall!"
        ch_v "It's open dawn to dusk, which is why I wasn't able to get here for a while. . ."
        ch_v "It's got a -ton- of different shops, although I guess not all of them would be very interesting to you."
        $ line = 0
        $ Girls = all_Girls[:]
        while Girls and not line:
                if Girls[0].Date:
                        $ line = 1
                $ Girls.remove(Girls[0])
        if line:
                #if you've been on dates
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
                #if you haven't been on dates
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
        $ JubesX.change_face("confused",1)
        ch_v "Weird."
        ch_v "Anyway, I spent a -ton- of time at the mall when I was a kid."
        $ JubesX.change_face("sadside")
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
                    $ JubesX.change_face("confused",1)
                    ch_v ". . ."
            "Free food court, uh?":
                    $ JubesX.change_stat("love", 70, 1)
                    $ JubesX.change_stat("inhibition", 60, 1)
                    $ JubesX.change_face("smile",1,Eyes="side")
                    ch_v "When I could get into a restaurant, yeah. . ."
                    $ JubesX.change_stat("love", 70, -2)
                    $ JubesX.change_stat("love", 90, -1)
                    $ JubesX.change_stat("obedience", 80, 1)
                    $ JubesX.change_face("angry",1)
                    ch_v ". . ."

        ch_v "Yeah, but it was ok. . ."
        $ JubesX.change_face("smile",Eyes="side")
        ch_v "Anyway, then I bumped into some of the other Xavier's students and found my way to the school."
        $ JubesX.change_face("smile")
        ch_v "Xavier agreed to take me in there, and it's worked out much better."
        $ JubesX.change_face("sadside")
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
                    $ JubesX.change_face("angry")
                    ch_v ". . ."
        $ JubesX.change_face("smile")
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
                    $ JubesX.change_face("sad")
                    ch_v "Aw, ok. At least I can come here when I want now. . ."
                    $ JubesX.change_stat("obedience", 50, 3)
                    $ JubesX.change_stat("obedience", 90, 2)

        "You both head back to campus."
        $ bg_current = "bg_campus"
        $ JubesX.location = bg_current
        call clear_the_room(JubesX,0,1) #it's silent
        call set_the_scene
        ch_v "Anyway, it was nice to hang out with you."
        ch_v "I hope we can do it again some time!"
        jump Misplaced
        return

label Jubes_Cleanhouse:
        # this is triggered if you agree to break up the other girls, but then fail to within the time limit
        $ JubesX.DrainWord("asked meet")
        if "cleanhouse" in JubesX.Todo:
                        $ JubesX.Todo.remove("cleanhouse")
        if not Player.Harem or JubesX in Player.Harem:
                        $ JubesX.Event[5] = 2
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
        call clear_the_room(JubesX)
        call set_the_scene
        call Taboo_Level
        $ JubesX.daily_history.append("relationship")
        $ JubesX.change_stat("love", 200, -20)
        $ JubesX.change_face("angry",1)
        ch_v "What's the deal, [Player.Petname]?"
        ch_v "It's been a week already, and you're still dating [Player.Harem[0].name]!"
        if len(Player.Harem) >= 2:
                ch_v "Not to mention the rest of them!"
        menu:
            extend ""
            "Sorry about that, I'm sticking with them":
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 80, 5)
                    $ JubesX.change_stat("inhibition", 80, 5)
                    $ JubesX.change_face("angry",2)
                    ch_v "You asshole."
                    $ JubesX.change_face("sadside",1)
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
                    $ JubesX.Blush = 2
                    show Jubes_Sprite with vpunch
                    "She clocks you one."
                    "That was fair."
                    $ JubesX.Blush = 1

        ch_v "I can't believe you're putting me through this."
        ch_v "Making me choose between you and putting up with this whole arrangement."
        $ line = 0
        if Approvalcheck(JubesX, 1400) and Approvalcheck(JubesX, 600,"O"):
                #if she's very obedient. . .
                pass
        elif Approvalcheck(JubesX, 1200) and Approvalcheck(JubesX, 500,"O"):
                #second chance on if she likes you well enough. . .
                $ Girls = Player.Harem[:]
                while Girls and line != "no":
                    # Spits out a "no" if she doesn't like another girl
                    if JubesX.GirlLikecheck(Girls[0]) <= 400:
                            $ line = "no"
                    $ Girls.remove(Girls[0])
        else:
                $ line = "no"
        if line == "no":
                $ JubesX.change_stat("love", 200, -10)
                $ JubesX.change_stat("obedience", 80, 10)
                $ JubesX.change_face("angry",1)
                call Haremchange_stat(JubesX,700,-15) #lowers like of all Harem girls by 15
                ch_v "No, this is bullshit, never mind."
        else:
                $ JubesX.change_stat("love", 200, 5)
                $ JubesX.change_stat("obedience", 80, 20)
                $ JubesX.change_stat("inhibition", 80, 10)
                $ JubesX.change_face("angry",1,Eyes="side")
                ch_v "Ok, fine, whatever. I'm in too."
                if not simulation:
                        $ Player.Harem.append(JubesX)
                        if "JubesYes" in Player.Traits:
                                $ Player.Traits.remove("JubesYes")
                        $ JubesX.Petnames.append("boyfriend")
                        call Harem_Initiation
                        call Haremchange_stat(JubesX,900,20) #raises like of all Harem girls by 20
                        $ JubesX.Event[5] = 20
        return

label Jubes_love(Shipping=[],Shipshape=0,Topics=[],Girls=[]):
        # SHipping is used to track who else you're involved with
        # if JubesX.Event[6] = 5, then it cleared
        # if JubesX.Event[6] = 20, then it broke because you didn't love her
        # if JubesX.Event[6] = 23, then it broke because you pissed her off
        # if JubesX.Event[6] = 25, then it broke and you already went through the redux

        $ JubesX.DrainWord("asked meet")
        $ Girls = all_Girls[:]
        $ Girls.remove(JubesX)
        while Girls:
            if Approvalcheck(Girls[0], 1200, "LO"):
                    $ Shipping.append(Girls[0])
            $ Girls.remove(Girls[0])
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
        call clear_the_room(JubesX)
        call set_the_scene
        call Taboo_Level
        $ JubesX.daily_history.append("relationship")
        $ JubesX.change_face("sad",1)
        ch_v "Hey, so, I like what this is. . ."
        ch_v "-what we have. . ."
        $ JubesX.change_face("sadside",1)
        ch_v "It's been kind of hard for me to open up to people. . ."
        ch_v "I've been betrayed a lot out there."
        menu:
            extend ""
            "I would never betray you.":
                    $ JubesX.change_face("bemused",1)
                    $ JubesX.change_stat("love", 200, 10)
                    $ JubesX.change_stat("obedience", 70, 5)
                    $ JubesX.change_stat("inhibition", 60, 5)
                    ch_v "I. . . know that now."
            "I'm sorry to hear that.":
                    $ JubesX.change_face("sadside",1,Mouth="smile")
                    $ JubesX.change_stat("love", 200, 5)
                    $ JubesX.change_stat("obedience", 90, -5)
                    $ JubesX.change_stat("inhibition", 60, 10)
                    ch_v ". . ."
                    $ JubesX.change_face("smile",1)
                    ch_v "Thank you. . ."
            "That must be rough.":
                    $ JubesX.change_face("sadside",1,Mouth="normal")
                    $ JubesX.change_stat("love", 200, 5)
                    ch_v ". . ."
                    $ JubesX.change_face("smile",1)
                    ch_v "It was. . ."
            "Wow, that sucks.":
                    $ JubesX.change_face("confused",1)
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 90, 10)
                    $ JubesX.change_stat("inhibition", 90, -5)
                    ch_v ". . ."
                    $ JubesX.change_face("angry",1,Eyes="side")
                    ch_v "Right, so. . ."
        ch_v "I didn't always have it as easy as I've had it here."
        $ JubesX.Eyes = "normal"
        ch_v "I only thought it fair to tell you a little about that history."
        $ line = 0
        while len(Topics) < 9 and "exit" not in Topics:
                #lines are topics of current discussion. "Topics" catalogues things alrewady discussed

                if line == "facility":
                        menu:
                            extend ""
                            "How many people did you kill?" if "kills" not in Topics:
                                    $ JubesX.change_face("angry",0,Eyes="side")
                                    ch_v "Dozens. Maybe more. At least 13 primary targets."
                                    ch_v "Too many \"collaterals.\""
                                    $ Topics.append("kills")
                            "Did you ever fail a mission?" if "fail" not in Topics:
                                    $ JubesX.change_face("angry",0,Eyes="side",Brows="normal")
                                    ch_v "Once or twice."
                                    ch_v "Sometimes they managed to get away."
                                    ch_v "I'm not proud of who I was back then, but even then. . ."
                                    $ JubesX.Mouth = "smile"
                                    ch_v ". . . a part of me was happy when they did."
                                    $ Topics.append("fail")
                            "Did anyone take care of you?" if "mother" not in Topics:
                                    $ JubesX.change_face("smile",0)
                                    ch_v "My mother, Sarah Kinney."
                                    ch_v "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ JubesX.change_face("sadside",0)
                                    ch_v "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ line = "mother"
                            "How did you escape?" if "escape" not in Topics:
                                    $ JubesX.change_face("sadside",0)
                                    ch_v "Mother."
                                    ch_v "She got me out, found me an escape route."
                                    ch_v "It was the last thing she did."
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
                                    $ JubesX.change_face("smile",0)
                                    ch_v "Her name was Sarah Kinney."
                                    ch_v "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ JubesX.change_face("sadside",0)
                                    ch_v "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ line = "mother"
                            "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:
                                    $ JubesX.change_face("sad",0,Eyes="surprised")
                                    ch_v "I didn't want to, but the primary_action scent made me. . ."
                                    $ JubesX.change_face("sadside",0)
                                    if "trigger" in JubesX.History:
                                            ch_v "I've mentioned that to you before. . ."
                                    else:
                                            $ JubesX.History.append("trigger")
                                    ch_v ". . . it can make me kill, even if I don't want to."
                                    $ Topics.append("killed")
                            "It wasn't your fault." if "killed" in Topics:
                                    $ JubesX.change_stat("love", 200, 5)
                                    $ JubesX.change_stat("obedience", 70, 5)
                                    $ JubesX.change_stat("inhibition", 70, 5)
                                    $ JubesX.change_face("sad",0)
                                    ch_v "Not completely, no."
                                    $ JubesX.change_face("sadside",0)
                                    ch_v "But my hands aren't clean."
                                    $ line = "facility"
                            "That must have been horrible." if "killed" in Topics:
                                    $ JubesX.change_face("sadside",0)
                                    $ JubesX.change_stat("love", 200, 5)
                                    $ JubesX.change_stat("obedience", 90, 5)
                                    ch_v "It's taken me some time. . ."
                                    $ JubesX.change_face("normal",0)
                                    ch_v "but I think I'm ok with it now."
                                    $ line = "facility"
                            "Bummer." if "killed" in Topics:
                                    $ JubesX.change_face("angry",1)
                                    $ JubesX.change_stat("love", 200, -10)
                                    $ JubesX.change_stat("obedience", 90, 5)
                                    ch_v "Are you seriously making fun of my mother's death?!"
                                    $ Topics.append("exit")
                                    $ line = "angry"
                # end questions about mother

                if line == "NYX":
                        menu:
                            extend ""
                            "What did you do for a living?" if "living" not in Topics:
                                    $ JubesX.change_face("sadside",0)
                                    ch_v "There wasn't much I could do at the time, I mostly just scrounged for food."
                                    ch_v "You can get by on some pretty awful stuff if you have a healing factor."
                                    $ JubesX.change_face("bemused",1,Brows="sad")
                                    ch_v "I also did some. . . shady stuff."
                                    $ Topics.append("living")

                            "Was it sexual?" if "work" not in Topics and "living" in Topics:
                                    $ JubesX.change_face("sadside",2)
                                    $ JubesX.change_stat("obedience", 90, 5)
                                    $ JubesX.change_stat("inhibition", 90, 10)
                                    ch_v ". . ."
                                    $ JubesX.Blush = 1
                                    ch_v "A little."
                                    $ line = "work"
                                    $ Topics.append("work")

                            "Did you hurt people?" if "work" not in Topics and "living" in Topics:
                                    $ JubesX.change_face("surprised",0,Eyes="normal")
                                    ch_v "No, definitely not."
                                    ch_v "After the facility, I just couldn't take that sort of work anymore."
                                    $ JubesX.change_face("bemused",0)
                                    ch_v "I avoided hurting anyone."
                                    $ JubesX.change_face("sadside",2)
                                    ch_v "It tended to be more. . . sexual work."
                                    $ line = "work"
                                    $ Topics.append("work")

                            "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:
                                    $ JubesX.change_face("bemused",0)
                                    ch_v "Yeah, eventually."
                                    ch_v "I'd seen Wolverine on the news, and thought maybe he had some answers."
                                    ch_v "He's not around much though."
                                    $ Topics.append("xaviers")
                                    $ line = 0
                            "Good thing you made it here. [[exit]" if "xaviers" in Topics:
                                    $ JubesX.change_face("smile",0)
                                    ch_v "Yeah."
                                    $ line = 0

                if line == "work":
                        $ JubesX.change_face("sadside",0,Mouth="normal")
                        ch_v "It was mostly the rougher customers."
                        ch_v "The ones who couldn't control their tempers."
                        $ JubesX.change_face("angry",0,Mouth="smile")
                        ch_v "Better for the girl who can heal to take the hits, right?"
                        menu:
                                extend ""
                                "That's terrible. I wish I could have protected you.":
                                        $ JubesX.change_face("smile",1)
                                        $ JubesX.change_stat("love", 200, 5)
                                        $ JubesX.change_stat("obedience", 90, 5)
                                        $ JubesX.change_stat("inhibition", 90, -5)
                                        ch_v "Thanks, but I was ok."
                                        $ JubesX.change_face("sadside",0)
                                        ch_v "I didn't deserve it, but I felt like I did at the time."
                                "You're strong to have made it out of there.":
                                        $ JubesX.change_face("smile",0)
                                        $ JubesX.change_stat("love", 200, 5)
                                        $ JubesX.change_stat("obedience", 90, 10)
                                        $ JubesX.change_stat("inhibition", 90, 5)
                                        ch_v "Thanks."
                                        ch_v "I didn't really think of it like that. . ."
                                        $ JubesX.change_face("sadside",0)
                                        ch_v "I just felt like I'd deserved it."
                                        ch_v "But I realized how wrong that was."
                                "Yeah, that makes sense.":
                                        $ JubesX.change_face("confused",1)
                                        $ JubesX.change_stat("love", 200, -5)
                                        $ JubesX.change_stat("obedience", 90, 15)
                                        $ JubesX.change_stat("inhibition", 90, -5)
                                        ch_v "Don't think before you speak, do you?"
                                        $ JubesX.change_face("sadside",0)
                                        ch_v "It wasn't right, I just didn't realize it at the time."
                        ch_v "Eventually I got past it and decided to get out of there."
                        ch_v "Not like they could stop me."
                        $ line = "NYX"

                if not line:
                        # Primary menu, falls through to this
                        menu:
                            extend ""
                            "What did you do back at the facility?" if "facility" not in Topics:
                                    $ JubesX.change_face("sadside",0)
                                    ch_v "After they tested what I could do, they put me to work."
                                    ch_v "Mainly, I killed people for them."
                                    $ Topics.append("facility")
                                    $ line = "facility"
                            "More about that facility. . ." if "facility" in Topics:
                                    $ line = "facility"

                            "Where did you go after you escaped?" if "NYX" not in Topics:
                                    $ JubesX.change_face("sadside",0)
                                    ch_v "I wandered in the wilderness for weeks."
                                    ch_v "Eventually I found my way to New York."
                                    ch_v "I lived on the streets for a few years."
                                    $ Topics.append("NYX")
                                    $ line = "NYX"
                            "More about after the escape. . ." if "NYX" in Topics:
                                    $ line = "NYX"

                            "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:
                                    $ JubesX.change_face("smile",0)
                                    $ JubesX.change_stat("love", 200, 10)
                                    $ JubesX.change_stat("obedience", 90, 3)
                                    $ JubesX.change_stat("inhibition", 90, 3)
                                    ch_v "Thanks for listening to me ramble."
                                    $ Topics.append("exit")
                            "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:
                                    $ JubesX.change_face("sadside",0, Mouth="smile")
                                    $ JubesX.change_stat("obedience", 90, 10)
                                    ch_v "Yeah, you get the idea."
                                    $ Topics.append("exit")
                            "I don't really care about that. [[exit]":
                                    $ JubesX.change_face("angry",0)
                                    $ JubesX.change_stat("love", 200, -15)
                                    $ JubesX.change_stat("obedience", 50, 5)
                                    $ JubesX.change_stat("obedience", 90, 10)
                                    $ JubesX.change_stat("inhibition", 90, -5)
                                    ch_v "Oh, I'm sorry if I was boring you with my life story."
                                    $ line = "angry"
                                    $ Topics.append("exit")

        #end while loop

        if line == "angry":
                $ JubesX.change_face("angry",0)
                ch_v "And here I was thinking that I meant something to you."
                ch_v "Well forget that!"
                $ line = 0
                $ JubesX.Event[6] = 23
                $ JubesX.recent_history.append("angry")
                $ JubesX.daily_history.append("angry")
                hide Jubes_Sprite with easeoutright
                call remove_girl(JubesX)
                $ JubesX.location = "hold" #puts her off the board for the day
                return

        $ JubesX.change_face("bemused",0,Eyes="down")
        ch_v "I just thought you should know,"
        $ JubesX.change_face("smile",2)
        ch_v "I love you."
        menu:
                extend ""
                "I love you too!":
                    $ JubesX.change_face("smile",1)
                    $ JubesX.change_stat("love", 200, 20)
                    $ JubesX.change_stat("inhibition", 90, 5)
                    ch_v "For a second there you had me worried."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_love_End
                "I know.":
                    $ JubesX.change_face("smile",1)
                    $ JubesX.change_stat("love", 200, 10)
                    $ JubesX.change_stat("obedience", 90, 5)
                    $ JubesX.change_stat("inhibition", 90, 10)
                    $ JubesX.change_stat("lust", 90, 5)
                    ch_v "Smooth one. Seriously though, how about you?"
                "Neat?":
                    $ JubesX.change_face("confused",1)
                    $ JubesX.change_stat("obedience", 90, 5)
                    ch_v "I'm gonna need a bit more there, [JubesX.Petname]."
                "Huh.":
                    $ JubesX.change_face("confused",1)
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 90, 10)
                    ch_v "I'm not sure how to take that one."


        menu:
                extend ""
                "Oh, I love you too!":
                    $ JubesX.change_face("smile",1)
                    $ JubesX.change_stat("love", 200, 15)
                    $ JubesX.change_stat("obedience", 90, 5)
                    $ JubesX.change_stat("inhibition", 90, 5)
                    ch_v "For a second there you had me worried."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_love_End
                "I. . . love you back?":
                    $ JubesX.change_face("confused",1)
                    $ JubesX.change_stat("love", 200, 5)
                    $ JubesX.change_stat("obedience", 90, 10)
                    ch_v "Ok, I'll take it."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_love_End
                "I mean, that's cool and all. . .":
                    $ JubesX.change_face("sadside",1)
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 90, 10)
                    $ JubesX.change_stat("inhibition", 90, -5)
                    ch_v ". . . but you don't love me back. Got it."
                "That's. . . uncomfortable.":
                    $ JubesX.change_face("angry",1)
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
                        $ JubesX.change_face("sadside",1)
                        ch_v "Well, you do have your pick."
                "There's nobody else.":
                        $ JubesX.change_stat("love", 200, -15)
                        $ JubesX.change_stat("obedience", 90, 15)
                        $ JubesX.change_stat("inhibition", 90, 5)
                        $ JubesX.change_face("sad",1)
                        if Approvalcheck(JubesX, 1000, "OI"):
                            ch_v "I guess that's something."
                        else:
                            ch_v ". . ."
                "It's a \"you\" problem.":
                        $ JubesX.change_face("angry")
                        $ JubesX.change_stat("love", 200, -25)
                        $ JubesX.change_stat("obedience", 90, 15)
                        ch_v "You're seriously messing with me?"
                        $ JubesX.change_stat("love", 200, -10)
                        ch_v "You don't want to see me when I'm angry."
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.daily_history.append("angry")


        if line:
                #If you called out a girl,
                if JubesX.GirlLikecheck(line) >= 800:
                        $ JubesX.change_stat("love", 200, 5)
                        $ JubesX.change_stat("obedience", 90, 20)
                        $ JubesX.change_stat("inhibition", 90, 5)
                        $ JubesX.change_stat("lust", 90, 5)
                        $ JubesX.change_face("sadside",1)
                        ch_v "Yeah, I guess she's great."
                else:
                        $ JubesX.change_face("angry",Eyes="side")
                        $ JubesX.change_stat("love", 200, -5)
                        $ JubesX.change_stat("obedience", 90, 20)
                        ch_v "Bitch."
                        $ JubesX.recent_history.append("angry")
                        $ JubesX.GLG(line,800,-50,1)
        ch_v "Well, if that's the way you feel about it. . ."
        ch_v "I'll. . . see you later."
        ch_v "This. . . hurt."

label Jubes_love_End:
        if "lover" not in JubesX.Petnames:
                $ JubesX.Event[6] = 20
                hide Jubes_Sprite with easeoutright
                call remove_girl(JubesX)
                $ JubesX.location = "hold" #puts her off the board for the day
                return

        $ JubesX.Event[6] = 5
        "[JubesX.name] grabs you in a crushing hug."
        $ JubesX.change_stat("love", 200, 25)
        $ JubesX.change_stat("lust", 90, 5)
        $ JubesX.change_face("sly",1)
        ch_v "So. . . now that we have some free time. . ."
        $ JubesX.change_stat("lust", 90, 10)

        if not JubesX.Sex:
            $ JubesX.change_face("bemused",2)
            ch_v "I think I'm ready. . ."
        else:
            ch_v "Would you like to have some fun?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Yeah, let's do this. . . [[have sex]":
                    $ JubesX.change_stat("inhibition", 30, 20)
                    $ JubesX.change_stat("obedience", 70, 10)
                    ch_v "Hmm. . ."
                    call Jubes_SexAct("sex")
                "I have something else in mind. . .[[choose another activity]":
                    $ JubesX.Brows = "confused"
                    $ JubesX.change_stat("obedience", 70, 25)
                    ch_v "Like what? . ."
                    $ temp_modifier = 20
                    call Jubes_SexMenu
        return

label Jubes_love_Redux:
         #this is for if you rejected her but want a second chance
        $ line = 0
        $ JubesX.daily_history.append("relationship")

        if JubesX.Event[6] >= 25:
                #if this is the second time through
                ch_p "I hope you've forgiven me, I still love you."
                $ JubesX.change_stat("love", 95, 10)
                if Approvalcheck(JubesX, 950, "L"):
                    $ line = "love"
                else:
                    $ JubesX.change_face("angry")
                    ch_v "You're still working your way out of the hole, [JubesX.Petname]."
                    $ JubesX.Eyes="side"
                    ch_v ". . ."
                    $ JubesX.change_face("angry",Mouth="lipbite")
                    ch_v "But let me hear your pitch."
        elif JubesX.Event[6] >= 23:
                #if you pissed her off the first time
                ch_p "I was rude when you opened up to me before."
                $ JubesX.change_stat("love", 95, 10)
                if Approvalcheck(JubesX, 950, "L"):
                    ch_v "And. . ."
                else:
                    $ JubesX.change_face("angry")
                    ch_v "You're still working your way out of the hole, [JubesX.Petname]."
                    $ JubesX.Eyes="side"
                    ch_v ". . ."
                    $ JubesX.change_face("angry",Mouth="lipbite")
                    ch_v "But let me hear your pitch."
        else:
                    ch_p "Remember when I told you that I didn't love you?"
                    $ JubesX.change_face("perplexed",1)
                    ch_v ". . ."
                    $ JubesX.change_face("angry", Eyes="side")
                    ch_v "How could I forget?"

        if line != "love":
                menu:
                    extend ""
                    "I'm sorry, I didn't mean it.":
                        $ JubesX.Eyes = "surprised"
                        ch_v "Oh really?"
                        ch_v "That's awfully convenient."
                        ch_p "Yeah. I mean, yes, I love you, [JubesX.name]."
                        $ JubesX.change_stat("love", 200, 10)
                        if Approvalcheck(JubesX, 950, "L"):
                            $ line = "love"
                        else:
                            $ JubesX.change_face("sadside")
                            ch_v "Well, maybe I don't, anymore. . ."
                    "I've changed my mind, I do love you, so. . .":
                        if Approvalcheck(JubesX, 950, "L"):
                            $ line = "love"
                            ch_v "Well that's great."
                        else:
                            $ JubesX.Mouth = "sad"
                            ch_v "Good for you."
                            $ JubesX.change_stat("inhibition", 90, 10)
                            $ JubesX.change_face("sadside")
                            ch_v "I don't exactly have the same mind either. . ."
                    "Um, never mind.":
                            $ JubesX.change_stat("love", 200, -30)
                            $ JubesX.change_stat("obedience", 50, 10)
                            $ JubesX.change_face("angry")
                            ch_v "Oh, fuck you."
                            $ JubesX.recent_history.append("angry")
                            $ JubesX.daily_history.append("angry")
        if line == "love":
                $ JubesX.change_stat("love", 200, 40)
                $ JubesX.change_stat("obedience", 90, 10)
                $ JubesX.change_stat("inhibition", 90, 10)
                $ JubesX.change_face("smile")
                ch_v "I'm glad you came around."
                ch_v "I love you too, [JubesX.Petname]!"
                if JubesX.Event[6] < 25:
                        $ JubesX.change_face("sly")
                        "She grabs the back of your head and pulls you close."
                        ch_v "Next time, don't keep me waiting."
                $ JubesX.Petnames.append("lover")
        $ JubesX.Event[6] = 25
        return

label Jubes_Sub:
    $ JubesX.DrainWord("asked meet")
    call shift_focus(JubesX)
    if JubesX.location != bg_current and JubesX not in Party:
        "Suddenly, [JubesX.name] shows up and says she needs to talk to you."

    $ JubesX.location = bg_current
    call set_the_scene(0)
    call Display_Girl(JubesX)
    call clear_the_room(JubesX)
    call set_the_scene
    call Taboo_Level
    $ JubesX.daily_history.append("relationship")
    $ JubesX.change_face("bemused", 1)

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
    $ JubesX.change_face("sly", 1,Eyes="side")
    ch_v "I don't know how I feel about that."
    if JubesX.Event[6]: #if you've done the love route
            $ JubesX.change_face("sadside", 1)
            ch_v "You know the past I've had, with the facility, with the. . . "
            ch_v ". . . work I had to do for them."
            $ JubesX.change_face("sad", 1)
            ch_v "I don't know if I want to let anyone tell me what to do like that again."
    menu Jubes_Sub_Question:
        extend ""
        "I guess I can be demanding.":
                $ JubesX.change_face("sly", 1)
                $ JubesX.change_stat("obedience", 200, 10)
                $ JubesX.change_stat("inhibition", 50, 5)
        "Sorry. I didn't mean to come off like that.":
                $ JubesX.change_face("sly", 1)
                $ JubesX.change_stat("love", 80, 5)
                $ JubesX.change_stat("obedience", 200, -5)
                $ JubesX.change_stat("inhibition", 50, -5)
                ch_v "I get it, you're assertive. . ."
        "Remind me about the facility?" if JubesX.Event[6] and line != "facility":
                $ JubesX.change_face("sadside", 1)
                $ JubesX.change_stat("love", 99, -10)
                $ JubesX.change_stat("inhibition", 50, -5)
                ch_v "I told you, I was raised in an underground government lab."
                ch_v "They ordered me to kill people for them."
                $ JubesX.change_face("sly", 0, Brows= "angry")
                ch_v ". . . until I got tired of taking orders."
                $ line = "facility"
                jump Jubes_Sub_Question
        "What bothers you about being told to do things?" if not JubesX.Event[6] and line != "facility":
                $ JubesX.change_face("sadside", 1)
                $ JubesX.change_stat("love", 80, 5)
                ch_v "I've just had some rough experiences."
                ch_v "You don't need to know about them."
                ch_v ". . ."
                $ JubesX.change_face("sad", 0)
                ch_v "Let's just say I was ordered to do some things I regret."
                $ line = "facility"
                jump Jubes_Sub_Question
        "Get with the program.":
                if Approvalcheck(JubesX, 1000, "LO"):
                        $ JubesX.change_face("sly", 1)
                        $ JubesX.change_stat("obedience", 200, 20)
                        $ JubesX.change_stat("inhibition", 50, 10)
                        ch_v "Hmmm. . ."
                else:
                        $ JubesX.change_stat("love", 200, -10)
                        $ JubesX.change_stat("inhibition", 50, -5)
                        $ JubesX.change_face("angry",0)
                        ch_v "You're not off to a good start here. You might want to rethink your attitude."
                        menu:
                            extend ""
                            "Sorry.  I thought that's what you were into.":
                                    $ JubesX.change_face("perplexed", 1,Eyes="side")
                                    $ JubesX.Eyes = "side"
                                    $ JubesX.change_stat("love", 75, 10)
                                    $ JubesX.change_stat("obedience", 200, 5)
                                    $ JubesX.change_stat("inhibition", 50, 5)
                                    ch_v ". . . after I just said. . ."
                                    $ JubesX.change_face("sly", 1)
                                    ch_v "Ok, whatever."
                            "I don't care.":
                                    $ JubesX.change_stat("love", 95, -10)
                                    ch_v "I guess not."
                                    $ line = "rude"
    if line == "facility":
            $ line = 0

    if not line:
            # She's advancing to the next stage
            $ JubesX.change_face("sly", 1)
            ch_v "Look, it's not like. . ."
            $ JubesX.change_face("sly", 2)
            ch_v ". . . it's not like I hate it."
            $ JubesX.change_face("smile", 1, Eyes="side")
            ch_v ". . . I actually think it might make me. . ."
            menu:
                extend ""
                "-excited?":
                    $ JubesX.change_stat("obedience", 200, 5)
                    $ JubesX.change_stat("inhibition", 50, 5)
                    ch_v ". . ."
                    $ JubesX.change_face("sly", 1)
                    $ JubesX.change_stat("lust", 50, 10)
                    ch_v "a little, yeah."
                "-digusted?":
                    $ JubesX.change_stat("love", 75, -5)
                    $ JubesX.change_stat("obedience", 200, -5)
                    $ JubesX.change_face("sadside", 1)
                    ch_v ". . . kind of,"
                    $ JubesX.change_face("sly", 1)
                    $ JubesX.change_stat("inhibition", 70, 5)
                    $ JubesX.change_stat("lust", 50, 5)
                    ch_v "but also kind of excited by it."
                "-hungry?":
                    $ JubesX.change_face("confused", 1,Eyes="surprised",Mouth="smile")
                    $ JubesX.change_stat("obedience", 200, -5)
                    $ JubesX.change_stat("inhibition", 50, -5)
                    ch_v "?!"
                    $ JubesX.change_face("confused", 1,Eyes="normal",Mouth="smile")
                    ch_v "Well. . . yeah? But not for-"
                    $ JubesX.change_face("sly", 1)
                    $ JubesX.change_stat("lust", 50, 5)
                    ch_v "I mean, it makes me kind of. . . excited."
                "-horny?":
                    $ JubesX.change_stat("obedience", 200, 10)
                    $ JubesX.change_stat("inhibition", 50, 5)
                    $ JubesX.change_face("startled", 2,Mouth="lipbite")
                    ch_v "!"
                    $ JubesX.change_face("sly", 1, Eyes="side")
                    $ JubesX.change_stat("inhibition", 50, 5)
                    $ JubesX.change_stat("lust", 50, 10)
                    $ JubesX.change_stat("lust", 70, 5)
                    ch_v "Yes."
            menu:
                extend ""
                "Good. If you wanna be with me, then you follow my orders.":
                        if Approvalcheck(JubesX, 1000, "LO"):
                            $ JubesX.change_face("sly", 1)
                            $ JubesX.change_stat("obedience", 200, 15)
                            $ JubesX.change_stat("inhibition", 50, 10)
                            ch_v "Hmmm. . ."
                        else:
                            $ JubesX.change_face("sadside", 1,Mouth="normal")
                            $ JubesX.change_stat("love", 200, -5)
                            $ JubesX.change_stat("obedience", 200, 10)
                            ch_v "You might want to slow your roll there, [JubesX.Petname]."
                            menu:
                                extend ""
                                "Whatever. That's how it is. Take it or leave it.":
                                        $ JubesX.change_face("angry")
                                        $ JubesX.change_stat("love", 200, -10)
                                        $ JubesX.change_stat("obedience", 200, 5)
                                        ch_v "I think you're pushing it too far there, [JubesX.Petname]."
                                        $ line = "rude"
                                "Ok, just a little." :
                                        $ JubesX.change_face("bemused", 1)
                                        $ JubesX.change_stat("love", 95, 5)
                                        $ JubesX.change_stat("inhibition", 50, 5)
                                        ch_v "-but not too much."

                "Yeah? You think it's sexy?":
                                        $ JubesX.change_face("bemused", 2,Eyes="side")
                                        $ JubesX.change_stat("obedience", 200, 5)
                                        $ JubesX.change_stat("inhibition", 50, 10)
                                        ch_v ". . ."
                                        $ JubesX.change_stat("lust", 50, 5)
                                        ch_v "Yeah."

                "You sure you don't want me to back off a little?":
                        $ JubesX.change_face("startled", 1,Eyes="squint")
                        $ JubesX.change_stat("obedience", 200, -5)
                        menu:
                            ch_v "Well if you have to ask. . ."
                            "Only if you're okay with it.":
                                $ JubesX.change_face("bemused", 1)
                                $ JubesX.change_stat("love", 95, 10)
                                $ JubesX.change_stat("inhibition", 50, 10)
                                $ line = 0
                            "Uhm. . .yeah. I think it's weird.  Sorry.":
                                $ JubesX.change_face("sad", 1, Eyes="surprised")
                                $ JubesX.change_stat("love", 200, -15)
                                $ JubesX.change_stat("obedience", 200, -5)
                                $ JubesX.change_stat("inhibition", 50, -10)
                                $ line = "embarrassed"

                "I couldn't care less.":
                                $ JubesX.change_stat("love", 200, -10)
                                $ JubesX.change_stat("obedience", 200, 15)
                                $ JubesX.change_face("angry")
                                ch_v "I think you're pushing it too far there, [JubesX.Petname]."
                                $ line = "rude"

    if not line:
        $ JubesX.change_face("bemused", 1,Eyes = "down")
        ch_v "So, I'm willing to give this a shot."
        ch_v "Just a trial period, to see how it goes."
        ch_v "Just tell me what you want, and. . . I'll see about doing it."
        menu Jubes_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                    $ JubesX.change_stat("obedience", 200, 5)
                    $ JubesX.change_stat("inhibition", 50, 5)
                    $ JubesX.change_face("sly", 1)
                    $ line = 0
            "Don't you think that relationship's kinda. . .weird?":
                    $ JubesX.change_face("sad", 1, Eyes="surprised")
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("inhibition", 50, -15)
                    $ line = "embarrassed"

    if not line:
        $ JubesX.change_face("smile", 1)
        ch_v "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ JubesX.change_stat("love", 95, 5)
                    $ JubesX.change_stat("obedience", 200, 15)
                    $ JubesX.change_stat("inhibition", 50, 5)
                    ch_v "Yes, sir."
                    $ JubesX.Petname = "sir"
            "That's kind of formal, isn't it?":
                $ JubesX.change_face("perplexed", 1)
                ch_v "Huh. ok, no problem"
                $ JubesX.change_stat("inhibition", 50, -5)
                $ JubesX.change_face("sly", 1,Eyes="side")
                menu:
                    ch_v "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                            $ JubesX.change_stat("obedience", 200, 10)
                            $ JubesX.change_face("smile", 1)
                            ch_v "Good."
                    "I don't feel comfortable with that. . .":
                            $ JubesX.change_face("sad", 1, Eyes="side")
                            $ JubesX.change_stat("love", 200, -10)
                            $ JubesX.change_stat("obedience", 200, -30)
                            $ JubesX.change_stat("inhibition", 50, -15)
                            $line = "embarrassed"

    $ JubesX.History.append("sir")
    if not line:
            $ JubesX.Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif line == "rude":
            call remove_girl(JubesX)
            if not simulation:
                    $ renpy.pop_call()
            "[JubesX.name] knocks her way past you and storms off."
    elif line == "embarrassed":
            $ JubesX.change_face("sadside", 2)
            ch_v "Huh, ok, if you're not interested. . .."
            hide Jubes_Sprite with easeoutright
            call remove_girl(JubesX)
            if not simulation:
                    $ renpy.pop_call()
            "[JubesX.name] heads out of the room."
    return

label Jubes_Sub_Asked:
    $ line = 0
    $ JubesX.change_face("sadside", 1)
    ch_v "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in JubesX.Petnames and Approvalcheck(JubesX, 850, "O"):
                        #if this is asking about the "master" name, and her obedience is higher than 700
                        pass
                elif Approvalcheck(JubesX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        $ JubesX.change_face("angry", 1)
                        ch_v "It was a bad idea, don't worry about it." #Failed again. :(
                        $ line = "rude"

                if line != "rude":
                        $ JubesX.change_stat("love", 90, 10)
                        $ JubesX.change_face("sly", 1)
                        ch_v "Well, it's not like you stopped ordering me around anyway."
                        ch_v "Ok, let's give it a shot."

        "I know it's what you want. Do you want to try again, or not?":
                $ JubesX.change_face("bemused", 1)
                if "sir" in JubesX.Petnames:
                    if Approvalcheck(JubesX, 850, "O"):
                        ch_v "Ok, fine."
                    else:
                        ch_v "Nah, I'm good."
                        $ line = "rude"
                elif Approvalcheck(JubesX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ JubesX.change_face("confused", 1)
                        ch_v "Kinda wishy-washy there."
                        $ JubesX.change_face("sly", 1)
                        ch_v "but maybe you're right."
                        ch_v "Are you sure you're into this?"
                        menu:
                            extend ""
                            "Yes, I'm sorry I was mean about it.":
                                            $ JubesX.change_stat("love", 90, 15)
                                            $ JubesX.change_stat("inhibition", 50, 10)
                                            $ JubesX.change_face("bemused", 1)
                                            $ JubesX.Eyes = "side"
                                            ch_v "Ok then."
                            "You're damned right I am, bitch.":
                                    if "sir" in JubesX.Petnames and Approvalcheck(JubesX, 900, "O"):
                                            $ JubesX.change_stat("love", 200, -5)
                                            $ JubesX.change_stat("obedience", 200, 10)
                                            ch_v ". . ."
                                    elif Approvalcheck(JubesX,700, "O"):
                                            $ JubesX.change_stat("love", 200, -5)
                                            $ JubesX.change_stat("obedience", 200, 10)
                                            ch_v "Hmmm. . ."
                                    else: #if it failed both those things,
                                            $ JubesX.change_stat("love", 200, -10)
                                            $ JubesX.change_stat("obedience", 90, -10)
                                            $ JubesX.change_stat("obedience", 200, -10)
                                            $ JubesX.change_stat("inhibition", 50, -15)
                                            $ JubesX.change_face("angry", 1)
                                            ch_v "Wow, that's pushing it."
                                            $ line = "rude"
                            "Ok, never mind then.":
                                            $ JubesX.change_face("angry", 1)
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
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Jubes_Sprite with easeoutright
            call remove_girl(JubesX)
            $ JubesX.recent_history.append("angry")
            if not simulation:
                    $ renpy.pop_call()
            "[JubesX.name] checks you as she stomps out of the room."
    elif "sir" in JubesX.Petnames:
            #it didn't fail and "sir" was covered
            $ JubesX.change_stat("obedience", 200, 50)
            $ JubesX.Petnames.append("master")
            $ JubesX.Petname = "master"
            $ JubesX.Eyes = "sly"
            ch_v ". . . master. . ."
    else:
            #it didn't fail
            $ JubesX.change_stat("obedience", 200, 30)
            $ JubesX.Petnames.append("sir")
            $ JubesX.Petname = "sir"
            $ JubesX.change_face("sly", 1)
            ch_v ". . . sir."
    return

label Jubes_Master:
    $ JubesX.DrainWord("asked meet")
    call shift_focus(JubesX)
    if JubesX.location != bg_current and JubesX not in Party:
        "Suddenly, [JubesX.name] shows up and says she needs to talk to you."

    $ JubesX.location = bg_current
    call set_the_scene(0)
    call Display_Girl(JubesX)
    call clear_the_room(JubesX)
    call set_the_scene
    $ JubesX.daily_history.append("relationship")
    call Taboo_Level
    $ line = 0
    $ JubesX.change_face("sly", 1)
    ch_v "[JubesX.Petname]. . ."
    ch_v ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            $ JubesX.change_stat("obedience", 200, 5)
            $ JubesX.change_stat("inhibition", 50, 5)
        "What?":
            ch_v "I was asking if I could talk to you about something. . ."
            $ JubesX.Eyes = "side"
            ch_v ". . . personal."
            $ JubesX.Eyes = "squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ JubesX.change_stat("love", 80, 5)
                    $ JubesX.change_stat("obedience", 200, 5)
                    ch_v "Right. . ."
                "Oh, then no.":
                    $ JubesX.change_face("sad", 1)
                    $ JubesX.change_stat("love", 80, -5)
                    $ JubesX.change_stat("obedience", 200, -10)
                    $ line = "embarrassed"
        "No.":
            $ JubesX.change_face("perplexed", 1,Brows="confused")
            $ JubesX.change_stat("love", 80, -5)
            $ JubesX.change_stat("obedience", 200, -5)
            $ JubesX.change_stat("inhibition", 50, -5)
            ch_v "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ JubesX.change_face("confused", 1)
                    $ JubesX.change_stat("obedience", 200, 10)
                    $ JubesX.change_stat("inhibition", 60, 10)
                    ch_v "Right. . ."
                "Yes, not interested.":
                    $ JubesX.change_face("sad", 1)
                    $ JubesX.change_stat("love", 80, -5)
                    $ JubesX.change_stat("inhibition", 50, -10)
                    $ line = "embarrassed"


    if not line:
        $ JubesX.change_face("sly", 1)
        ch_v "I think I enjoy having you in charge."
        ch_v "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                    $ JubesX.change_face("sly", 1)
                    $ JubesX.change_stat("obedience", 200, 5)
                    ch_v "Good. Maybe we could take this a bit more seriously?"
                    menu:
                        extend ""
                        "Nah. This is just about perfect.":
                                $ JubesX.change_face("sad", 1)
                                $ JubesX.change_stat("obedience", 200, -15)
                                $ JubesX.change_stat("love", 80, 10)
                                $ line = "fail"
                        "What'd you have in mind?":
                                $ JubesX.Eyes = "side"
                                ch_v "I was thinking I could start calling you. . . {i}master{/i}?"
                                $ JubesX.Eyes = "squint"
                                menu:
                                    extend ""
                                    "Oh, yeah.  I'd like that.":
                                            $ JubesX.change_stat("obedience", 200, 5)
                                            ch_v "Good. . ."
                                    "Um. . .nah.  That's too much.":
                                            $ JubesX.change_face("sadside", 1)
                                            $ JubesX.change_stat("obedience", 200, -15)
                                            $ JubesX.change_stat("inhibition", 50, 5)
                                            $ line = "fail"

                        "Actually, I'd prefer we stopped doing it. Too much pressure.":
                                $ JubesX.change_face("sad", 1)
                                $ JubesX.change_stat("love", 200, -5)
                                $ JubesX.change_stat("obedience", 200, -10)
                                $ JubesX.change_stat("inhibition", 50, 15)
                                $ line = "fail"

                        "Actually, let's stop that. It's creeping me out.":
                                $ JubesX.change_face("angry", 2, Eyes="surprised")
                                $ JubesX.change_stat("love", 200, -10)
                                $ JubesX.change_stat("obedience", 200, -50)
                                $ JubesX.change_stat("inhibition", 50, -15)
                                ch_v "Say no more, I wouldn't want to CREEP YOU OUT."
                                $ line = "embarrassed"

            "As if I care what you think, slut.":
                    $ JubesX.change_face("angry", 1, Mouth="smile")
                    $ JubesX.change_stat("love", 90, -20)
                    $ JubesX.change_stat("obedience", 200, 10)
                    $ JubesX.change_stat("inhibition", 50, -10)
                    ch_v ". . ."
                    menu:
                        ch_v "Excuse me?"
                        "Sorry. I just don't care what you want.":
                                if Approvalcheck(JubesX, 1400, "LO"):
                                        $ JubesX.change_stat("obedience", 200, 10)
                                        ch_v ". . ."
                                        $ JubesX.change_face("sly", 1)
                                        $ JubesX.change_stat("love", 200, 20)
                                        $ JubesX.change_stat("inhibition", 50, 15)
                                        ch_v ". . .{i}go on. . .{/i}"
                                else:
                                        $ JubesX.change_stat("love", 200, -15)
                                        $ JubesX.change_stat("obedience", 200, -10)
                                        $ JubesX.change_stat("inhibition", 50, 5)
                                        $ JubesX.change_face("angry", 1)
                                        ch_v "!!!"
                                        $ line = "rude"

                        "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                                $ JubesX.change_stat("love", 200, 10)
                                $ JubesX.change_stat("obedience", 200, 10)
                                $ JubesX.change_stat("inhibition", 50, 5)
                                if Approvalcheck(JubesX, 1400, "LO"):
                                        $ JubesX.change_stat("obedience", 200, 10)
                                        ch_v ". . ."
                                        $ JubesX.change_face("sly", 1)
                                        $ JubesX.change_stat("love", 200, 20)
                                        $ JubesX.change_stat("inhibition", 50, 15)
                                        ch_v ". . .{i}no, about right. . .{/i}"
                                else:
                                        $ JubesX.change_stat("love", 200, 5)
                                        $ JubesX.change_stat("obedience", 200, -5)
                                        $ JubesX.change_stat("inhibition", 50, 5)
                                        $ JubesX.change_face("angry", 1, Eyes="side")
                                        ch_v ". . ."
                                        ch_v "We'll work on it. . ."

            "I don't really like it. Too much pressure.":
                                $ JubesX.change_face("sad", 2)
                                $ JubesX.change_stat("love", 200, -20)
                                $ JubesX.change_stat("obedience", 200, -20)
                                $ JubesX.change_stat("inhibition", 50, -10)
                                $ line = "embarrassed"

    $ JubesX.History.append("master")
    if line == "rude":
            $ JubesX.recent_history.append("angry")
            hide Jubes_Sprite with easeoutright
            call remove_girl(JubesX)
            if not simulation:
                    $ renpy.pop_call()
            "[JubesX.name] stomps out of the room."
    elif line == "embarrassed":
            ch_v "Ok, fine then."
            ch_v "And here I was, about to \"elevate your clearance.\""
            hide Jubes_Sprite with easeoutright
            call remove_girl(JubesX)
            if not simulation:
                    $ renpy.pop_call()
            "[JubesX.name] brushes past you on her way out."
    elif line == "fail":
            ch_v "Oh. . ."
            ch_v "I guess that's fine."
    else:
            $ JubesX.change_stat("obedience", 200, 50)
            $ JubesX.Petnames.append("master")
            $ JubesX.Petname = "master"
            ch_v ". . .master."
    return

label Jubes_Sexfriend:   #Jubes_Update
        #set this to occur after class
        $ JubesX.lust = 70
        $ JubesX.location = bg_current
        $ JubesX.DrainWord("asked meet")
        call set_the_scene
        $ JubesX.daily_history.append("relationship")
        call Taboo_Level
        $ line = 0
        $ JubesX.change_face("sly",2,Eyes="side")
        "[JubesX.name] approaches you and pulls you aside. She seems to be shivering a little bit."
        "She seems to be squirming around and rubbing her thighs together."
        $ JubesX.Petnames.append("sex friend")
        $ JubesX.change_face("sly",2)
        if JubesX in Player.Harem:
                ch_v "Hey."
                ch_v "I need some alone time with you."
        elif "lover" in JubesX.Petnames or "master" in JubesX.Petnames or "lover" in JubesX.Petnames or "sir" in JubesX.Petnames:
                #if you have done the lover thing
                ch_v "Hey."
                ch_v "I need some alone time with you."
        else:
                #if you've done no relationship stuff yet. . .
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
                        $ JubesX.change_face("sly",2,Mouth="smile")
                        $line = "yes"
                    "No thanks":
                        $ JubesX.change_face("confused",2)
                        $line = "no"
                    ". . .":
                        $ JubesX.change_stat("obedience", 90, 5)
                        $ JubesX.change_face("confused",2)

                if not line:
                        ch_v "Now, if at all possible. . ."
                        menu:
                            extend ""
                            "Sure":
                                $ JubesX.change_face("sly",2,Mouth="smile")
                                $line = "yes"
                            "No thanks":
                                $ JubesX.change_face("confused",2)
                                $line = "no"

                if line == "no":
                    $ JubesX.change_stat("love", 200, -5)
                    $ JubesX.change_stat("obedience", 80, 5)
                    ch_v "What? Why not?"
                    menu:
                        extend ""
                        "Ok, fine":
                            $ JubesX.change_face("confused",2,Mouth="smile")
                            ch_v "love the enthusiasm."
                            $line = "yes"
                        "Not interested":
                            $ JubesX.change_face("confused",2)

                        "There's someone else":
                            $ JubesX.change_stat("love", 95, -5)
                            $ JubesX.change_stat("obedience", 90, 5)
                            if Player.Harem:
                                    $ JubesX.change_face("surprised",2)
                                    ch_v "Oh, [Player.Harem[0].name]?"
                                    $ JubesX.GLG(Player.Harem[0],600,-25,1)
                            $ JubesX.change_face("sly",2)
                            ch_v "Well, she doesn't need to know about it. . ."
                            menu:
                                extend ""
                                "Ok, fine":
                                        ch_v "love the enthusiasm."
                                        $ line = "yes"
                                "Still no":
                                        pass

        if line == "no":
                    $ JubesX.change_stat("love", 200, -10)
                    $ JubesX.change_stat("obedience", 90, 15)
                    $ JubesX.change_stat("inhibition", 90, 10)
                    $ JubesX.change_face("sad",2)
                    ch_v "Really?"
                    ch_v "Bummer."
                    ch_v "Well let me know if you change your mind."
                    $ JubesX.change_face("sadside",2,Mouth="lipbite",Brows="angry")
                    if Player.Harem:
                            ch_v "Wonder if [Player.Harem[0].name]'s busy. . ."
                            $ JubesX.GLG(Player.Harem[0],500,25,1)
                    else:
                            ch_v "Wonder if Kitty's busy. . ."
                            $ JubesX.GLG("Kitty",500,25,1)
        else:
                $ JubesX.change_stat("love", 90, 10)
                $ JubesX.change_stat("obedience", 90, 5)
                $ JubesX.change_stat("inhibition", 90, 15)
                $ JubesX.change_face("sly",1,Mouth="smile")
                if Taboo:
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
                                call clear_the_room(JubesX)
                                call set_the_scene
                                $ Taboo = 0
                                $ JubesX.Taboo = 0

                        "No, let's do it here.":
                                $ JubesX.change_stat("obedience", 80, 5)
                                $ JubesX.change_stat("inhibition", 90, 15)
                                ch_v "Kinky."

                $ action_context = JubesX
                $ Player.AddWord(1,"interruption") #adds to Recent
                call Jubes_SexPrep              #she offers sex
                call Jubes_SexMenu

                #end "if no relationship"
        return

label Jubes_Fuckbuddy:
        $ JubesX.daily_history.append("relationship")
        $ JubesX.lust = 80
        $ JubesX.DrainWord("asked meet")
        # Conditions, in your room, jubes not there.
        "You hear a knock on the door, and go to answer it."
        #change jubes's outfit to default
        $ JubesX.location = bg_current
        call shift_focus(JubesX)
        call set_the_scene(0)
        $ JubesX.Outfit = "casual1"
        $ JubesX.OutfitDay = "casual1"
        $ JubesX.OutfitChange("casual1")
        call Display_Girl(JubesX)
        call Taboo_Level
        $ primary_action = "masturbation"
        $ primary_action3 = "fondle_pussy"
        $ JubesX.change_face("sly",2,Mouth="lipbite")
        "[JubesX.name] is standing in the doorway, with her hand down her pants."
        "You can tell she's been masturbating furiously, her scent is overpowering."
        $ primary_action = 0
        $ primary_action3 = 0
        $ JubesX.ArmPose = 1
        "She looks you up and down hungrily, and pulls her hand out of her pants."
        "She reaches up to caress your face, smearing her juices along it."
        ch_v "Mine."
        $ JubesX.Petnames.append("fuck buddy")
        $ JubesX.Event[10] += 1

        $ action_context = JubesX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call Jubes_SexPrep              #she offers sex
        call Jubes_SexMenu
        return
