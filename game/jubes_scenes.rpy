label Jubes_Meet:
        #jubilee's introduction scene
        #called from Sleepover if bg_current == "bg player" and "met" in StormX.History and "met" not in JubesX.History:

        show blackscreen onlayer black
        $ JubesX.OutfitDay = "casual2"
        $ JubesX.Outfit = "casual2"
        $ JubesX.OutfitChange("casual2")
        call CleartheRoom("All",0,1)
        $ JubesX.Loc = bg_current
        $ JubesX.Love = 500
        $ JubesX.Obed = 50
        $ JubesX.Inbt = 50
        $ JubesX.sprite_location = StageCenter

        $ JubesX.Names = []
        $ JubesX.Name = "???"

        $ Player.AddWord(1,"interruption") #prevents interruption
        $ Player.Focus = 30
        ch_u "\"Slurp, slurp, slurp.\""

        $ Player.Statup("Focus", 80, 5)
        $ JubesX.Statup("Lust", 80, 5)

        $ JubesX.FaceChange("sucking",1)

        "You feel a pleasant sensation. . ."
        ch_u "\"Slurp, slurp, slurp.\""
        $ Player.Statup("Focus", 80, 5)
        $ JubesX.Statup("Lust", 80, 5)
        $ JubesX.Addictionrate += 1 #starts her addiction path

        "It's somewhere below your waist. . ."
        ch_u "\"Slurp, slurp, slurp.\""
        $ Player.Statup("Focus", 80, 10)
        $ JubesX.Statup("Lust", 80, 5)

        "Wait. . . no it's not. . ."
        call Shift_Focus(JubesX)

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
        $ Line = 0
        "Someone seems to be giving you a hickey on your neck. . ."
        while Count > 0:
                #Looping portion
                $ Player.Statup("Focus", 80, 10)
                $ JubesX.Statup("Lust", 80, 5)
                menu:
                    extend ""
                    "Stay Quiet":
                        $ JubesX.Statup("Inbt", 90, 2)
                        $ JubesX.Statup("Lust", 80, 5)
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
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.FaceChange("surprised",2)
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
                            $ JubesX.FaceChange("sadside",1)
                            ch_v "I was just. . . thirsty. . ."
                    "Um. . . lady? What're you doing?":
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, -1)
                            $ JubesX.FaceChange("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Ah!"
                            $ JubesX.FaceChange("sadside",1,Mouth="normal")
                            ch_v "Oh, I guess I was. . ."
                            $ Count = 1
                    "That feels great, keep going. . .":
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.Statup("Inbt", 90, 2)
                            $ JubesX.FaceChange("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Oh!"
                            $ JubesX.FaceChange("sadside",1,Mouth="smile")
                            ch_v "I, um. . . I wasn't expecting that reaction. . ."
                            $ JubesX.FaceChange("sad",1,Mouth="smile")
                            $ Count = 1
                    "Hey, quit that!":
                            $ JubesX.Statup("Obed", 90, 10)
                            $ JubesX.Statup("Inbt", 90, -3)
                            $ JubesX.FaceChange("surprised",2)
                            show Jubes_Sprite:
                                ease 0.5 offset (100,0) zoom 1.5 alpha 1
                            ch_v "Ah!"
                            $ JubesX.FaceChange("sadside",1,Mouth="normal")
                            ch_v "Sorry!"
                            $ Count = 1
                $ Count -= 1
        $ JubesX.Blush = 1
        show Jubes_Sprite at sprite_location(JubesX.sprite_location,50)
        $ Count = 3
        while Count > 0:
            menu:
                extend ""
                "Who are you?" if "Jubilee" not in JubesX.Names:
                        $ JubesX.Statup("Love", 90, 2)
                        $ JubesX.Statup("Obed", 90, 1)
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Oh, I guess I should introduce myself."
                        ch_v "The name's \"Jubilee.\""
                        $ JubesX.Names.append("Jubilee")
                        $ JubesX.Name = "Jubilee"
                        ch_v "Nice to ea- meet you."
                        menu:
                            extend ""
                            "Ok. . .":
                                    $ JubesX.FaceChange("confused",1)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    ch_v ". . ."
                            "My name's [Player.Name]":
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Obed", 90, 2)
                                    ch_v "Oh, yeah, I know that."
                                    $ JubesX.Statup("Inbt", 90, 2)
                                    ch_v "I've. . . heard about you."
                            "Huh.":
                                    $ JubesX.FaceChange("confused",1)
                                    ch_v ". . ."
                #end "who are you"


                "That's an interesting name." if "Jubilee" in JubesX.Names and "Jubilation" not in JubesX.Names:
                        #only plays after Jubilee but before this bit
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Oh, yeah. Weird parents."
                        ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
                        ch_v "Guess I leaned into it?"
                        $ JubesX.Names.append("Jubilation")
                        $ JubesX.Names.append("Miss Lee")
                        $ JubesX.Pets.append("Miss Lee")
                        menu:
                            extend ""
                            "Yeah, sure.":
                                    $ JubesX.Statup("Love", 90, 1)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    ch_v ". . ."
                            "It suits you.":
                                    $ JubesX.Statup("Love", 90, 5)
                                    $ JubesX.Statup("Inbt", 90, 2)
                                    ch_v ". . ."
                            "Weird.":
                                    $ JubesX.FaceChange("angry",1)
                                    $ JubesX.Statup("Love", 90, -3)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."
                                    $ JubesX.FaceChange("normal",1)
                #end "interesting name"


                "What are you doing in my room?!" if "thirst" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, -1)
                        $ JubesX.Statup("Obed", 90, 7)
                        $ JubesX.Statup("Inbt", 90, -2)
                        $ JubesX.FaceChange("startled",2)
                        ch_v "Oh, I was just. . . thirsty?"
                        $ JubesX.FaceChange("smile",1)
                        $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent

                #end "what are you in my room"
                "What were you doing?" if "thirst" not in JubesX.RecentActions:
                        $ JubesX.Statup("Inbt", 90, 1)
                        $ JubesX.FaceChange("startled",2)
                        ch_v "I was just. . . getting a drink?"
                        $ JubesX.FaceChange("smile",1)
                        $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent

                #end "what are you doing"


                "So you drink blood?" if "vamp" in JubesX.RecentActions and "blood" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 1)
                        $ JubesX.FaceChange("sadside",2)
                        ch_v "Yeah, I kinda have to. . ."
                        $ JubesX.FaceChange("sad",1)
                        ch_v "Sorry again. . ."
                        $ JubesX.AddWord(1,"blood",0,0,0) #adds "word" tag to Recent
                "Can you turn into a bat?" if "vamp" in JubesX.RecentActions and "bat" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 1)
                        $ JubesX.FaceChange("confused",1)
                        ch_v "Well, no. . ."
                        $ JubesX.FaceChange("sly",1)
                        ch_v "But I am strong and can turn into mist."
                        ch_v "Sometimes."
                        $ JubesX.AddWord(1,"bat",0,0,0) #adds "word" tag to Recent
                "Is it contagious?" if "vamp" in JubesX.RecentActions and "contagious" not in JubesX.History:
                        $ JubesX.FaceChange("sadside",2)
                        ch_v "Infectious. . ."
                        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
                        ch_v "- and no!"
                        $ JubesX.FaceChange("sadside",1)
                        ch_v "It was, but Dr. Strange was able to cast a spell or something."
                        ch_v "So you don't need to worry about it spreading to you or anything."
                        $ JubesX.FaceChange("sad",1)
                        $ JubesX.AddWord(1,0,0,0,"contagious") #adds "word" tag to History
                "Why me?" if "vamp" in JubesX.RecentActions and "devamp" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 1)
                        $ JubesX.FaceChange("sly",1,Eyes="side")
                        ch_v "Well. . ."
                        ch_v "I had a theory. . ."
                        ch_v "I sorta figured that if you could negate powers, then maybe. . ."
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Maybe you could \"de-vampire\" me?"
                        $ JubesX.AddWord(1,"devamp",0,0,0) #adds "word" tag to Recent
                        menu:
                            extend ""
                            "You don't want to be a vampire":
                                    $ JubesX.Statup("Love", 90, 2)
                                    $ JubesX.Statup("Obed", 90, 1)
                                    ch_v "Well, no. . ."
                            "I guess.":
                                    $ JubesX.FaceChange("confused",1)
                                    $ JubesX.Statup("Love", 90, -1)
                                    ch_v ". . ."
                        ch_v "The powers are cool and all, but I can't even go out during the daytime!"
                        ch_v "and the blood drinking, of course."
                        $ JubesX.FaceChange("normal",1)

                        menu:
                            extend ""
                            "Of course.":
                                    $ JubesX.Statup("Love", 90, 2)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."
                            "Yeah. . .":
                                    $ JubesX.Statup("Obed", 90, 1)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."


                "Are you a mutant?" if "mutant" not in JubesX.RecentActions:
                        $ JubesX.Statup("Love", 90, 2)
                        $ JubesX.FaceChange("smile",1)
                        ch_v "Yeah! Of course I am!"
                        $ JubesX.FaceChange("smile",1,Eyes="side")
                        if "vamp" in JubesX.RecentActions:
                                ch_v "You know, among other things. . ."
                        else:
                                ch_v ". . . among other things. . ."
                        $ JubesX.AddWord(1,"mutant",0,0,0) #adds "word" tag to Recent
                        menu:
                            extend ""
                            "So what's your power?":
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Inbt", 90, 1)
                                    ch_v ". . ."
                            "Oh, ok.":
                                    $ JubesX.Statup("Love", 90, -1)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    $ JubesX.FaceChange("confused",1)
                                    ch_v "Not even curious about what I can do?"
                        $ JubesX.FaceChange("smile",1)
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
                                    $ JubesX.Statup("Love", 90, 3)
                                    $ JubesX.Statup("Inbt", 90, 5)
                                    ch_v "Thanks!"
                            "K.":
                                    $ JubesX.Statup("Obed", 90, 2)
                                    $ JubesX.Statup("Inbt", 90, -1)
                                    $ JubesX.FaceChange("angry",1,Eyes="side")
                                    ch_v "Ok, so it's not \"negating mutant powers\" cool or anything. . ."
                                    ch_v "I can do other stuff. . ."
                                    $ JubesX.FaceChange("normal",1)
                            ". . .":
                                    $ JubesX.Statup("Obed", 90, 2)
                                    ch_v ". . ."


                "Well, I guess I'm out of questions.":
                    $ JubesX.AddWord(1,"thirst",0,0,0) #adds "word" tag to Recent if she's missed it so far
                    $ Count = 0

            if "thirst" in JubesX.RecentActions and "vamp" not in JubesX.RecentActions:
                    "You feel a tickle on your neck and rub it, coming back with a trickle of blood on your fingers."
                    menu:
                        extend ""
                        "Oh. Blood. . .":
                                $ JubesX.Statup("Love", 90, 2)
                                $ JubesX.Statup("Obed", 90, 3)
                                $ JubesX.Statup("Inbt", 90, -2)
                                $ JubesX.FaceChange("angry",1,Eyes="squint",Mouth="kiss")
                                ch_v "You are -remarkably- chill about this."
                                $ JubesX.FaceChange("smile",1,Eyes="surprised", Brows = "sad")
                                ch_v "Maybe I took too much? . ."
                        "Why is my neck bleeding?":
                                $ JubesX.Statup("Love", 90, 4)
                                $ JubesX.Statup("Obed", 90, 2)
                                $ JubesX.FaceChange("sadside",1)
                                ch_v "Yeah. . . about that. . ."
                                ch_v "Sorry."
                        "What the fuck?!":
                                $ JubesX.Statup("Love", 90, -2)
                                $ JubesX.Statup("Obed", 90, 10)
                                $ JubesX.Statup("Inbt", 90, -2)
                                $ JubesX.FaceChange("startled",2)
                                ch_v "Sorry! Sorry!"
                                $ JubesX.FaceChange("startled",1)
                                ch_v "Let me explain!"
                    $ JubesX.FaceChange("sadside",1)
                    ch_v "So. . . I'm. . . a vampire?"
                    $ JubesX.AddWord(1,"vamp",0,0,0) #adds "word" tag to Recent
                    menu:
                        extend ""
                        "This isn't a refreshment stand!":
                                $ JubesX.Statup("Love", 90, 1)
                                $ JubesX.Statup("Obed", 90, 3)
                                $ JubesX.Statup("Inbt", 90, 1)
                                $ JubesX.FaceChange("sly",1)
                                ch_v "Says you."
                        "A vampire. . .":
                                ch_v ". . . Yeah. . ."
                        "Oh. Gotcha.":
                                $ JubesX.Statup("Love", 90, 2)
                                $ JubesX.Statup("Obed", 90, 2)
                                $ JubesX.Statup("Inbt", 90, -1)
                                $ JubesX.FaceChange("perplexed",1)
                                ch_v "Maybe we should take you to the medbay. . ."
                    $ Count += 1

            #loops back into menu

        # End while loop

        if "Jubilee" not in JubesX.Names:
                $ JubesX.Statup("Love", 90, -5)
                $ JubesX.Statup("Obed", 90, 10)
                $ JubesX.FaceChange("angry",1)
                ch_v "Seriously? You don't even want to know my fucking name?"
                $ JubesX.FaceChange("sadside",1,Brows="angry")
                ch_v "How many girls do you have going through this place?"
                ch_v ". . ."
                $ JubesX.FaceChange("angry",1)
                ch_v "It's \"Jubilee,\" b-t-dubs."
                menu:
                    extend ""
                    "Where's a jubliee?":
                            $ JubesX.Statup("Obed", 90, 1)
                            $ JubesX.Statup("Inbt", 90, 1)
                            ch_v "My -name- is Jubilee, dumbass."
                    "Your name? Ok.":
                            $ JubesX.Statup("Love", 90, 3)
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, 15)
                            $ JubesX.FaceChange("smile",1)
                            ch_v "You catch on quick. . ."
                    "Most nights are, yeah.":
                            $ JubesX.FaceChange("confused",1)
                            ch_v "Wha. . . oh."
                            $ JubesX.Statup("Love", 90, 10)
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, 15)
                            $ JubesX.FaceChange("smile",1)
                            ch_v "Heh."
                            ch_v "Ok, that's cool. No, I meant my -name- is Jubilee."
                            ch_v "It's actually \"Jubilation Lee,\" but you know. . ."
                $ JubesX.Name = "Jubilee"
                $ JubesX.Names.append("Jubilation")
                $ JubesX.Names.append("Miss Lee")
                $ JubesX.Pets.append("Miss Lee")
                ch_v "And I know your name's [Player.Name], obviously."
        if "devamp" not in JubesX.RecentActions:
                $ JubesX.FaceChange("sadside",1)
                ch_v "Anyway, I just figured that maybe your blood could reverse this \"vampire\" thing."
        menu:
            extend ""
            "So do you feel any different?":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1)
            ". . .":
                $ JubesX.Statup("Love", 90, -2)
                $ JubesX.Statup("Obed", 90, 2)
                $ JubesX.FaceChange("perplexed",1)
                ch_v "You don't even want to ask about the \"vampire\" thing?"
                menu:
                    extend ""
                    "Oh, yeah, how are you doing?":
                            $ JubesX.Statup("Love", 90, 1)
                            $ JubesX.Statup("Inbt", 90, 1)
                            $ JubesX.FaceChange("smile",1)
                    "Not really.":
                            $ JubesX.Statup("Love", 90, -3)
                            $ JubesX.Statup("Obed", 90, 3)
                            $ JubesX.FaceChange("angry",1)
                            ch_v "Well that's a bad start!"
                    "Oh, ok.":
                            $ JubesX.FaceChange("confused",1)
                            ch_v ". . ."

        ch_v "I guess. . . not that much different."
        ch_v "Still have the teeth, the. . . thirst."
        $ JubesX.FaceChange("sadside",1)
        ch_v "I guess I'm still a vampire."
        $ JubesX.FaceChange("normal",1)
        ch_v "But I do feel a bit better. . ."
        $ JubesX.FaceChange("sad",1)
        ch_v "I am sorry, I shouldn't have attacked you like that."
        ch_v "Not cool, I know."
        menu:
            extend ""
            "It's ok, I get it.":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 90, -1)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Thanks."
                    ch_v "Is there any way I could make it up to you?"
            "Why not make it up to me?":
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.FaceChange("sexy",1)
                    ch_v "Oh?"
            "How dare you!":
                    $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.Statup("Inbt", 90, -1)
                    $ JubesX.FaceChange("surprised",1)
                    ch_v "I know! I know!"
                    $ JubesX.FaceChange("smile",1)
                    ch_v "I can make it up to you!"
            ". . .":
                    $ JubesX.Statup("Inbt", 90, 3)
                    $ JubesX.FaceChange("sly",1)
                    ch_v "So. . . I guess I could make it up to you?"
        menu:
            extend ""
            "That's not necessary.":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "That's sweet of you."
                    ch_v "Seriously though, I'll think of something. . ."
            "A kiss, maybe?":
                    $ JubesX.Statup("Love", 90, 3)
                    $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("sly",1)
                    ch_v "I heard you're a charmer."
                    ch_v "Well, I guess. . . one. . ."
                    $ JubesX.FaceChange("kiss")
                    show Jubes_Sprite:
                        ease 0.5 offset (0,0) zoom 2
                    pause 1
                    show Jubes_Sprite:
                        ease 0.5 offset (100,0) zoom 1.5
                    $ JubesX.FaceChange("sly",1)
                    ch_v ". . ."
            "You could flash me?":
                    $ JubesX.Statup("Obed", 90, 3)
                    if ApprovalCheck(JubesX, 620):
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.Statup("Inbt", 90, 1)
                            $ JubesX.FaceChange("sly",1)
                            ch_v "I guess I could. . ."
                            $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    else:
                            $ JubesX.Statup("Love", 90, -2)
                            $ JubesX.Statup("Obed", 90, 1)
                            $ JubesX.FaceChange("angry",1,Mouth="sucking")
                    $ JubesX.ArmPose = 1
                    show Fireworks onlayer black as Fire1:
                            pos (JubesX.sprite_location+250,350)
                    show Fireworks onlayer black as Fire2:
                            pos (JubesX.sprite_location+250,350)
                    ch_v "As if."
                    $ JubesX.FaceChange("smile",1)

            "A blowjob?":
                    if ApprovalCheck(JubesX, 620):
                            $ JubesX.Statup("Love", 90, 1)
                            $ JubesX.Statup("Obed", 90, 5)
                            $ JubesX.Statup("Inbt", 90, 1)
                            $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    else:
                            $ JubesX.Statup("Love", 90, -5)
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.FaceChange("angry",1,Mouth="sucking")

                    ch_v "Hey, I may suck more than most, but even I'm not that easy!"
                    $ JubesX.FaceChange("smile",1)
        ch_v "Anyway, I should get going before dawn."
        ch_v "I might see you around sometime."
        ch_v "In the moonlight. . ."
        $ JubesX.AddWord(1,0,0,0,"met") #adds "word" tag to History
        $ ActiveGirls.append(JubesX) if JubesX not in ActiveGirls else ActiveGirls
        hide Jubes_Sprite with easeoutright
        call Remove_Girl(JubesX)
        "[JubesX.Name] leaves the room, you might as well get some sleep. . ."
        return

label Jubes_Sunshine:
        #called from EventCalls if "sunshine" not in JubesX.History and "traveling" in Player.RecentActions and bg_current in ("bg classroom","bg campus"):
        call Shift_Focus(JubesX)
        $ bg_current = "bg campus"
        $ JubesX.Loc = "bg campus"
        call CleartheRoom(JubesX,0,1)
        call AltClothes(JubesX,1)
        call Set_The_Scene
        $ JubesX.FaceChange("smile")
        "On your way across the square, you see a shape charging toward you."
        call Punch
        "[JubesX.Name] crashes into you."
        $ JubesX.FaceChange("smile",1,Mouth="sucking")
        ch_v "Hey, [Player.Name]!"
        $ JubesX.FaceChange("smile",1)
        ch_v "Check it out!"
        menu:
            extend ""
            "Oh, hey. . .":
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    ch_v "Yes, \"hey,\" but I am -outside!-"
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "During the daytime!"
            "You're out during the day!":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 2)
            "Check what out?":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 2)
                    ch_v "Look!"
                    ch_v "I'm -outside!-"
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("smile",1,Mouth="sucking")
                    ch_v "During the -daytime!-"
                    $ JubesX.FaceChange("smile")
            "What the hell?":
                    $ JubesX.Statup("Love", 90, -3)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.FaceChange("surprised",2,Mouth="sucking")
                    ch_v "Sorry! I was just so excited!"
                    $ JubesX.FaceChange("smile",1)
                    ch_v "I'm outside, during the daylight!"
        menu:
            extend ""
            "That's great!":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("surprised",1,Mouth="sucking")
                    ch_v "Right?!"
                    $ JubesX.FaceChange("smile",1)
            "So what? So am I.":
                    $ JubesX.Statup("Love", 90, -5)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.FaceChange("confused",1)
                    ch_v "Yes. . ."
                    ch_v "But I am a -vampire,- remember?"
            "Ok.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . . I'm a -vampire?-"
        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "I didn't used to be able to do this without catching fire!"
        $ JubesX.FaceChange("smile",1)
        menu:
            extend ""
            "So do you know why?":
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
            "Well it was never a problem for me.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 3)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . ."
                    ch_v "No, I get that it wouldn't be. . ."
                    $ JubesX.FaceChange("normal",1)
            "Neat.":
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . ."
                    $ JubesX.FaceChange("normal",1)
            "Ok.":
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 2)
                    $ JubesX.FaceChange("angry",1)
                    ch_v ". . ."
                    $ JubesX.FaceChange("normal",1)
        ch_v "I don't really know what caused it, but I guess it had to do with your blood. . ."
        $ JubesX.FaceChange("smile",1)
        ch_v "Anyway, I just wanted to say \"thank you,\" this is great!"
        $ JubesX.AddWord(1,0,0,0,"sunshine") #adds "word" tag to History
        hide Jubes_Sprite with easeoutright
        call Remove_Girl(JubesX)
        "[JubesX.Name] dashes off, and you continue on your way. . ."
        return

label Jubes_Entry_Check:
        #checks to see if she is trying to follow you and if she will.
        if JubesX not in Party:
                return
        call Jubes_Sunshock #checks to see if she has to stay
        if _return:
                #if she couldn't go with you
                menu:
                    "Ok then, we can stay here.":
                            if "stayed" in JubesX.RecentActions:
                                    # you stay, but not for the first time recently
                                    $ Girl.Statup("Love", 80, -2)
                                    ch_v "Now I kind feel like you're jerking me around. . ."
                            elif ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                ch_v "That's really not necessary, don't let me hold you back."
                                menu:
                                    extend ""
                                    "I inist.":
                                        # you stay
                                        $ JubesX.FaceChange("smile",1)
                                        $ Girl.Statup("Love", 80, 2)
                                        $ JubesX.Statup("Inbt", 60, 2)
                                        ch_v "Aw, thanks. That's sweet of you."
                                    "Ok, sorry about that.":
                                        # you go
                                        $ JubesX.Statup("Obed", 90, 2)
                                        $ JubesX.FaceChange("sad",1)
                                        $ Party.remove(JubesX)
                                        "You leave her behind."
                                        return
                                    "Cool, later then.":
                                        # you go
                                        $ Girl.Statup("Love", 80, -2)
                                        $ JubesX.Statup("Obed", 90, 2)
                                        $ JubesX.FaceChange("sad",1)
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
                            $ Girl.Statup("Love", 80, -2)
                            $ JubesX.Statup("Obed", 70, 2)
                            if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                    $ JubesX.Statup("Obed", 90, 2)
                                    $ JubesX.FaceChange("sad",1)
                                    ch_v "I understand, later then. . ."
                            else:
                                    $ Girl.Statup("Love", 80, -4)
                                    $ JubesX.FaceChange("angry",1,Mouth="sucking")
                            "You leave her behind."
                            $ JubesX.FaceChange("sad",1)
        return

label Jubes_Sunshock:
        #this is called when Jubilee is asked to go out in the sublight with higher than 50% addiction
        #returns 1 if she doesn't go along with it.

        if JubesX.Addict <= 50 or Time_Count > 2:
                #if below the threshold or it's night time, ignore this
                return 0
        $ JubesX.FaceChange("sad",1)
        if "sunshock" in JubesX.RecentActions:
                ch_v "Like I said, I'm not up for the sunshine."
                return 1
        $ JubesX.AddWord(1,"sunshock",0,0,0) #adds "word" tag to recent
        ch_v "Oh, wait, I'm kinda on a \"low charge\" at the moment, so I don't really want to go out in the sunlight?"
        menu:
            extend ""
            "Oh, sorry, that's fine.":
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Thanks for understanding. . ."
                    return 1

            "I could always. . . come get you?" if bg_current != JubesX.Loc and JubesX not in Party:
                    #if she's not local. . .
                    ch_v "Oh, that could be nice. I'll see you then."
                    return 1

            "I could always. . . top you off?" if bg_current == JubesX.Loc or JubesX in Party:
                    # only works if she is local to you
                    $ JubesX.Statup("Love", 80, 1)
                    $ JubesX.FaceChange("confused",1)
                    ch_v "Oh? What'd you have in mind?"
                    menu:
                        extend ""
                        "Nothing, just touch whatever you like.":
                            if Girl.Petname in ("master", "sir"):
                                    $ Girl.Statup("Lust", 80, 3)
                                    $ Girl.Statup("Love", 70, 1)
                                    $ Girl.Statup("Love", 95, 1)
                                    $ Girl.FaceChange("sexy")
                                    ch_v "Then I suppose I choose. . ."
                                    "She leans in for a kiss."
                                    call KissPrep(Girl)
                            elif ApprovalCheck(Girl, 650, "LI"):
                                    $ Girl.Statup("Lust", 80, 3)
                                    $ Girl.Statup("Love", 80, 5)
                                    $ Girl.FaceChange("sexy")
                                    ch_v "Oh! Then how about I just try a simple touch. . ."
                                    "She leans in for a kiss."
                                    call KissPrep(Girl)
                            else:
                                    $ Girl.Statup("Lust", 80, 3)
                                    $ Girl.Statup("Love", 80, 6)
                                    $ Girl.FaceChange("smile")
                                    call Girl_Tag(Girl)
                            while Girl.Addict > 20 and Round > 10:
                                    #should remove addiction by 1 unit per round until either it stabilizes or time runs out.
                                    $ Girl.Addict -= 1
                                    $ Round -= 1
                                    if Round == 10:
                                            call AnyLine(Girl,"I suppose we don't have time for any more than that.")
                        #end "Nothing, just touch whatever you like.":

                        "How about a kiss?":
                                if Girl.Kissed or ApprovalCheck(Girl, 600, "LI") or Girl.Petname in ("master", "sir"):
                                        $ Girl.Forced = 0
                                        $ Girl.Statup("Lust", 80, 3)
                                        $ Girl.Statup("Love", 80, 6)
                                        $ Girl.FaceChange("sexy")
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
                                            $ CountStore = temp_modifier
                                            call Top_Off(Girl,2)
                                            $ temp_modifier = CountStore
                                            call expression Girl.Tag + "_Fondle_Breasts"
                                            if "fondle breasts" in Girl.RecentActions:
                                                    $ Girl.Statup("Obed", 80, 10)
                                                    $ Girl.Statup("Inbt", 80, 10)
                                                    ch_v "So, fair trade?"

                                    "How about you just let me touch your thighs?":
                                            $ CountStore = temp_modifier
                                            call Bottoms_Off(Girl,2)
                                            $ temp_modifier = CountStore
                                            if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                                    ch_v "Well, we'll see. . ."
                                            call expression Girl.Tag + "_Fondle_Thighs"
                                            if "fondle thighs" in Girl.RecentActions:
                                                    $ Girl.Statup("Obed", 50, 5)
                                                    $ Girl.Statup("Inbt", 50, 5)
                                                    ch_v "So, fair trade?"
                                                    if Girl.PantsNum() > 6 or Girl.HoseNum() >= 5:
                                                            call Girl_Tag(Girl)

                                    "How about you let me touch your pussy?":
                                            $ CountStore = temp_modifier
                                            call Bottoms_Off(Girl,0)
                                            $ temp_modifier = CountStore
                                            call expression Girl.Tag + "_Fondle_Pussy"
                                            if "fondle pussy" in Girl.RecentActions:
                                                    $ Girl.Statup("Obed", 50, 10)
                                                    $ Girl.Statup("Obed", 80, 5)
                                                    $ Girl.Statup("Inbt", 50, 10)
                                                    $ Girl.Statup("Inbt", 80, 5)
                                                    ch_v "That was plenty, right?"

                                    "Never mind then":
                                            $ JubesX.Statup("Love", 90, -3)
                                            $ JubesX.Statup("Obed", 70, 1)
                                            $ JubesX.Statup("Obed", 90, 2)
                                            $ JubesX.FaceChange("angry",1)
                        "Oh, never mind.":
                                $ JubesX.Statup("Love", 70, -2)
                                $ JubesX.Statup("Love", 90, -2)
                                $ JubesX.Statup("Obed", 70, 1)
                                $ JubesX.Statup("Obed", 90, 2)
                                $ JubesX.FaceChange("angry",1)

                        #end Sunshock treatment menu

                    if JubesX.Addict >= 70:
                            $ JubesX.Statup("Inbt", 70, 1)
                            $ JubesX.Statup("Inbt", 80, 1)
                            ch_v "Couldn't I just touch you real quick?"
                            menu:
                                extend ""
                                "Sure.":
                                        $ Girl.Statup("Lust", 80, 3)
                                        $ Girl.Statup("Love", 80, 6)
                                        $ Girl.FaceChange("smile")
                                        call Girl_Tag(Girl)
                                "Nope, sorry.":
                                        $ JubesX.Statup("Love", 80, -3)
                                        $ JubesX.Statup("Obed", 70, 2)
                                        if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                                $ JubesX.FaceChange("sad",1)
                                                ch_v "Oh."
                                        else:
                                                $ JubesX.Statup("Love", 90, -2)
                                                $ JubesX.Statup("Obed", 90, 2)
                                                $ JubesX.FaceChange("angry",1)
                                                ch_v "Jerk."

                    if JubesX.Addict >= 70:
                            #this is too high, she will refuse outright.
                            if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                    $ JubesX.FaceChange("sad",1)
                                    ch_v "I'm sorry, I just can't, it would be agonizing."
                            else:
                                    $ JubesX.FaceChange("angry",1)
                                    ch_v "You have to be kidding! I'd catch fire!"
                            return 1
                    elif ApprovalCheck(JubesX, 1600) or ApprovalCheck(JubesX, 500, "O"):
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.Statup("Inbt", 80, 2)
                            ch_v "I guess I could manage it for a little bit. . ."
                    else:
                            ch_v "Grow up. . ."
                            return 1
            #end "I could always. . . top you off?":

            "Come on, don't be like that.":
                    $ JubesX.Statup("Love", 70, -2)
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.FaceChange("sad",1)
                    if JubesX.Addict >= 70:
                            #this is too high, she will refuse outright.
                            if ApprovalCheck(JubesX, 1300) or ApprovalCheck(JubesX, 400, "O"):
                                    $ JubesX.Statup("Obed", 90, 2)
                                    ch_v "I'm sorry, I just can't, it would be agonizing."
                            else:
                                    $ JubesX.FaceChange("angry",1)
                                    ch_v "You have to be kidding! I'd catch fire!"
                            return 1
                    elif ApprovalCheck(JubesX, 1600) or ApprovalCheck(JubesX, 500, "O"):
                            $ JubesX.Statup("Obed", 90, 2)
                            $ JubesX.Statup("Inbt", 80, 2)
                            ch_v "I guess I could manage it for a little bit. . ."
                    else:
                            ch_v "Grow up. . ."
                            return 1
        return 0

label Jubes_Mall(BO=[]):
        #this is called to introduce the mall element

        call Shift_Focus(JubesX)
        if JubesX.Loc == bg_current:
                "[JubesX.Name] suddently freezes up, then turns to you."
        else:
                $ JubesX.Loc = bg_current
                "[JubesX.Name] rushes into the room."
        call CleartheRoom(JubesX,0,0) #she asks
        call Set_The_Scene
        $ Player.AddWord(1,0,0,0,"mall") #history

        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "Hey, I just realized something!"
        $ JubesX.FaceChange("smile")
        menu:
            extend ""
            "Cool.":
                    $ JubesX.Statup("Love", 80, 1)
            "Oh, what?":
                    $ JubesX.Statup("Love", 90, 2)
                    $ JubesX.Statup("Inbt", 60, 1)
            "Uh-huh.":
                    $ JubesX.Statup("Love", 80, -1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Obed", 60,1)
                    $ JubesX.Statup("Inbt", 50, -1)
                    $ JubesX.FaceChange("angry",1,Mouth="sucking")
                    ch_v "This is serious!"
            ". . .":
                $ JubesX.Statup("Love", 90, -1)
                $ JubesX.FaceChange("confused")
                ch_v "Aren't you going to ask me \"what?\""
                menu:
                    extend ""
                    "Oh, sure, what?":
                            $ JubesX.Statup("Love", 90, 2)
                            $ JubesX.Statup("Obed", 50, 1)
                            $ JubesX.Statup("Inbt", 50, 1)
                    "No.":
                            $ JubesX.Statup("Love", 80, -2)
                            $ JubesX.Statup("Obed", 70, 2)
                            $ JubesX.Statup("Inbt", 30, -1)
                            $ JubesX.FaceChange("angry")
                            ch_v "Dick."
                    ". . .":
                            $ JubesX.Statup("Love", 90, -1)
                            $ JubesX.Statup("Obed", 60, 1)
                            ch_v "Ooookaaay. . ."
        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "Now that I can go out during the daytime, I can go to the mall again!!"
        menu:
            extend ""
            "That's great!":
                    $ JubesX.Statup("Love", 90, 5)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    ch_v "I know, right?"
                    menu:
                        extend ""
                        "Wait, there's a mall?":
                                $ JubesX.Statup("Love", 80, 1)
                                $ JubesX.Statup("Inbt", 70, 1)
                                $ JubesX.FaceChange("confused")
                                ch_v "Of course there's a mall! What town doesn't have a mall?!"
                        "Did you want to go?":
                                $ JubesX.Statup("Love", 80, 2)
                                $ JubesX.Statup("Love", 90, 1)
                                $ JubesX.Statup("Inbt", 70, 1)
            "Oh, ok.":
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.FaceChange("sad")
            "Wait, there's a mall?":
                    $ JubesX.Statup("Love", 80, 1)
                    $ JubesX.Statup("Inbt", 70, 1)
                    $ JubesX.FaceChange("confused")
                    ch_v "Of course there's a mall! What town doesn't have a mall?!"
            "Ok, whatever.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 50, 2)
                    $ JubesX.Statup("Obed", 90, 2)
                    $ JubesX.Statup("Inbt", 50, -1)
        $ JubesX.FaceChange("surprised",1,Mouth="sucking")
        ch_v "We've got to go there, right now!"
        $ JubesX.FaceChange("smile")
        $ Party = [JubesX]
        menu:
            "Ok, let's check it out.":
                    $ JubesX.Statup("Love", 80, 2)
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Inbt", 60, 1)
                    show blackscreen onlayer black with dissolve
                    "You both head out of the room."
            "You can go, I don't need anything.":
                    $ JubesX.Statup("Love", 80, 2)
                    $ JubesX.Statup("Obed", 60, 1)
                    $ JubesX.Statup("Obed", 80, 1)
                    ch_v "Come'on, you gotta go!"
                    ch_v "You don't know what you're missing!"
                    show blackscreen onlayer black with dissolve
                    "[JubesX.Name] can be surprisingly forceful. . ."
            "Nah.":
                    $ JubesX.Statup("Love", 50, -2)
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Inbt", 50, 2)
                    $ JubesX.Statup("Inbt", 60, 2)
                    $ JubesX.FaceChange("angry",1,Mouth="sucking")
                    ch_v "Stow the 'tude, we're going!"
                    $ JubesX.FaceChange("smile")
                    show blackscreen onlayer black with dissolve
                    "[JubesX.Name] can be surprisngly forceful. . ."
            "Actually, I planned to-":
                    $ JubesX.Statup("Love", 50, -1)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.Statup("Inbt", 60, 1)
                    $ JubesX.FaceChange("surprised",1,Mouth="sucking")
                    ch_v "No time! We're going!"
                    $ JubesX.FaceChange("smile")
                    show blackscreen onlayer black with dissolve
                    "[JubesX.Name] can be surprisngly forceful. . ."
        "You arrive at what appears to be a mid-sized suburban shopping complex, often referred to as a \"mall.\""

        $ bg_current = "bg mall"
        $ JubesX.Loc = bg_current
        call CleartheRoom(JubesX,0,1) #it's silent
        call Set_The_Scene

        $ JubesX.FaceChange("smile")
        ch_v "Welcome to the Salem Centre Mall!"
        ch_v "It's open dawn to dusk, which is why I wasn't able to get here for a while. . ."
        ch_v "It's got a -ton- of different shops, although I guess not all of them would be very interesting to you."
        $ Line = 0
        $ BO = TotalGirls[:]
        while BO and not Line:
                if BO[0].Date:
                        $ Line = 1
                $ BO.remove(BO[0])
        if Line:
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
                    $ JubesX.Statup("Love", 70, -1)
        $ JubesX.FaceChange("confused",1)
        ch_v "Weird."
        ch_v "Anyway, I spent a -ton- of time at the mall when I was a kid."
        $ JubesX.FaceChange("sadside")
        ch_v "I'd run away from foster care, and just camped out in closed stores. . ."
        ch_v "It was better than being on the street, at least."
        menu:
            extend ""
            "That's rough.":
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Obed", 50, 1)
            "That must have been hard for you.":
                    $ JubesX.Statup("Love", 60, 5)
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 90, 1)
            "I guess.":
                    $ JubesX.Statup("Love", 70, -1)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Obed", 50, 1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    $ JubesX.FaceChange("confused",1)
                    ch_v ". . ."
            "Free food court, uh?":
                    $ JubesX.Statup("Love", 70, 1)
                    $ JubesX.Statup("Inbt", 60, 1)
                    $ JubesX.FaceChange("smile",1,Eyes="side")
                    ch_v "When I could get into a restaurant, yeah. . ."
                    $ JubesX.Statup("Love", 70, -2)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Obed", 80, 1)
                    $ JubesX.FaceChange("angry",1)
                    ch_v ". . ."

        ch_v "Yeah, but it was ok. . ."
        $ JubesX.FaceChange("smile",Eyes="side")
        ch_v "Anyway, then I bumped into some of the other Xavier's students and found my way to the school."
        $ JubesX.FaceChange("smile")
        ch_v "Xavier agreed to take me in there, and it's worked out much better."
        $ JubesX.FaceChange("sadside")
        ch_v "Until the whole \"vampire\" thing at least."
        menu:
            "Yeah, about that. . .":
                    $ JubesX.Statup("Obed", 30, 1)
                    $ JubesX.Statup("Obed", 60, 1)
            "Yeah, I bet.":
                    $ JubesX.Statup("Love", 80, 2)
            "Uh-huh.":
                    $ JubesX.Statup("Love", 90, -2)
                    $ JubesX.Statup("Obed", 90, 1)
                    $ JubesX.FaceChange("angry")
                    ch_v ". . ."
        $ JubesX.FaceChange("smile")
        ch_v "So anyways. . . now that we're here, did you want to go shopping?"
        menu:
            "Sure, let's look around.":
                    $ JubesX.Statup("Love", 60, 5)
                    $ JubesX.Statup("Love", 80, 3)
                    $ JubesX.Statup("Love", 90, 1)
                    $ JubesX.Statup("Inbt", 50, 1)
                    ch_v "Cool."
                    call Shopping_Mall
            "Nah, we can head back now.":
                    $ JubesX.Statup("Love", 60, -3)
                    $ JubesX.Statup("Love", 80, -2)
                    $ JubesX.Statup("Love", 90, -1)
                    $ JubesX.Statup("Inbt", 90, 1)
                    $ JubesX.FaceChange("sad")
                    ch_v "Aw, ok. At least I can come here when I want now. . ."
                    $ JubesX.Statup("Obed", 50, 3)
                    $ JubesX.Statup("Obed", 90, 2)

        "You both head back to campus."
        $ bg_current = "bg campus"
        $ JubesX.Loc = bg_current
        call CleartheRoom(JubesX,0,1) #it's silent
        call Set_The_Scene
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

        if JubesX.Loc == bg_current or JubesX in Party:
                "[JubesX.Name] glances over at you with a scowl."
        else:
                "[JubesX.Name] turns a corner and notices you."
        if bg_current != "bg jubes" and bg_current != "bg player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg jubes"
        $ JubesX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(JubesX)
        call Set_The_Scene
        call Taboo_Level
        $ JubesX.DailyActions.append("relationship")
        $ JubesX.Statup("Love", 200, -20)
        $ JubesX.FaceChange("angry",1)
        ch_v "What's the deal, [Player.Petname]?"
        ch_v "It's been a week already, and you're still dating [Player.Harem[0].Name]!"
        if len(Player.Harem) >= 2:
                ch_v "Not to mention the rest of them!"
        menu:
            extend ""
            "Sorry about that, I'm sticking with them":
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 80, 5)
                    $ JubesX.Statup("Inbt", 80, 5)
                    $ JubesX.FaceChange("angry",2)
                    ch_v "You asshole."
                    $ JubesX.FaceChange("sadside",1)
                    ch_v "You could have at least been honest about it."
            "Must have slipped my mind":
                    $ JubesX.Statup("Love", 200, -10)
                    $ JubesX.Statup("Obed", 80, 10)
                    ch_v "!"
                    ch_v "Seriously dude? That's all you've got?"
            "[[shrug]":
                    $ JubesX.Statup("Love", 200, -20)
                    $ JubesX.Statup("Obed", 80, 10)
                    $ JubesX.Statup("Inbt", 80, 10)
                    $ JubesX.Blush = 2
                    show Jubes_Sprite with vpunch
                    "She clocks you one."
                    "That was fair."
                    $ JubesX.Blush = 1

        ch_v "I can't believe you're putting me through this."
        ch_v "Making me choose between you and putting up with this whole arrangement."
        $ Line = 0
        if ApprovalCheck(JubesX, 1400) and ApprovalCheck(JubesX, 600,"O"):
                #if she's very obedient. . .
                pass
        elif ApprovalCheck(JubesX, 1200) and ApprovalCheck(JubesX, 500,"O"):
                #second chance on if she likes you well enough. . .
                $ BO = Player.Harem[:]
                while BO and Line != "no":
                    # Spits out a "no" if she doesn't like another girl
                    if JubesX.GirlLikeCheck(BO[0]) <= 400:
                            $ Line = "no"
                    $ BO.remove(BO[0])
        else:
                $ Line = "no"
        if Line == "no":
                $ JubesX.Statup("Love", 200, -10)
                $ JubesX.Statup("Obed", 80, 10)
                $ JubesX.FaceChange("angry",1)
                call HaremStatup(JubesX,700,-15) #lowers like of all Harem girls by 15
                ch_v "No, this is bullshit, never mind."
        else:
                $ JubesX.Statup("Love", 200, 5)
                $ JubesX.Statup("Obed", 80, 20)
                $ JubesX.Statup("Inbt", 80, 10)
                $ JubesX.FaceChange("angry",1,Eyes="side")
                ch_v "Ok, fine, whatever. I'm in too."
                if "Historia" not in Player.Traits:
                        $ Player.Harem.append(JubesX)
                        if "JubesYes" in Player.Traits:
                                $ Player.Traits.remove("JubesYes")
                        $ JubesX.Petnames.append("boyfriend")
                        call Harem_Initiation
                        call HaremStatup(JubesX,900,20) #raises like of all Harem girls by 20
                        $ JubesX.Event[5] = 20
        return

label Jubes_Love(Shipping=[],Shipshape=0,Topics=[],BO=[]):
        # SHipping is used to track who else you're involved with
        # if JubesX.Event[6] = 5, then it cleared
        # if JubesX.Event[6] = 20, then it broke because you didn't love her
        # if JubesX.Event[6] = 23, then it broke because you pissed her off
        # if JubesX.Event[6] = 25, then it broke and you already went through the redux

        $ JubesX.DrainWord("asked meet")
        $ BO = TotalGirls[:]
        $ BO.remove(JubesX)
        while BO:
            if ApprovalCheck(BO[0], 1200, "LO"):
                    $ Shipping.append(BO[0])
            $ BO.remove(BO[0])
        $ Shipshape = len(Shipping)

        if JubesX.Loc == bg_current or JubesX in Party:
                "[JubesX.Name] glances over at you with a concerned look."
        else:
                "[JubesX.Name] turns a corner and notices you."
        if bg_current != "bg jubes" and bg_current != "bg player":
                "With little word, she moves behind you and pushes you towards her room."
                $ bg_current = "bg jubes"
        $ JubesX.Loc = bg_current
        call Set_The_Scene
        call CleartheRoom(JubesX)
        call Set_The_Scene
        call Taboo_Level
        $ JubesX.DailyActions.append("relationship")
        $ JubesX.FaceChange("sad",1)
        ch_v "Hey, so, I like what this is. . ."
        ch_v "-what we have. . ."
        $ JubesX.FaceChange("sadside",1)
        ch_v "It's been kind of hard for me to open up to people. . ."
        ch_v "I've been betrayed a lot out there."
        menu:
            extend ""
            "I would never betray you.":
                    $ JubesX.FaceChange("bemused",1)
                    $ JubesX.Statup("Love", 200, 10)
                    $ JubesX.Statup("Obed", 70, 5)
                    $ JubesX.Statup("Inbt", 60, 5)
                    ch_v "I. . . know that now."
            "I'm sorry to hear that.":
                    $ JubesX.FaceChange("sadside",1,Mouth="smile")
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Obed", 90, -5)
                    $ JubesX.Statup("Inbt", 60, 10)
                    ch_v ". . ."
                    $ JubesX.FaceChange("smile",1)
                    ch_v "Thank you. . ."
            "That must be rough.":
                    $ JubesX.FaceChange("sadside",1,Mouth="normal")
                    $ JubesX.Statup("Love", 200, 5)
                    ch_v ". . ."
                    $ JubesX.FaceChange("smile",1)
                    ch_v "It was. . ."
            "Wow, that sucks.":
                    $ JubesX.FaceChange("confused",1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 10)
                    $ JubesX.Statup("Inbt", 90, -5)
                    ch_v ". . ."
                    $ JubesX.FaceChange("angry",1,Eyes="side")
                    ch_v "Right, so. . ."
        ch_v "I didn't always have it as easy as I've had it here."
        $ JubesX.Eyes = "normal"
        ch_v "I only thought it fair to tell you a little about that history."
        $ Line = 0
        while len(Topics) < 9 and "exit" not in Topics:
                #Lines are topics of current discussion. "Topics" catalogues things alrewady discussed

                if Line == "facility":
                        menu:
                            extend ""
                            "How many people did you kill?" if "kills" not in Topics:
                                    $ JubesX.FaceChange("angry",0,Eyes="side")
                                    ch_v "Dozens. Maybe more. At least 13 primary targets."
                                    ch_v "Too many \"collaterals.\""
                                    $ Topics.append("kills")
                            "Did you ever fail a mission?" if "fail" not in Topics:
                                    $ JubesX.FaceChange("angry",0,Eyes="side",Brows="normal")
                                    ch_v "Once or twice."
                                    ch_v "Sometimes they managed to get away."
                                    ch_v "I'm not proud of who I was back then, but even then. . ."
                                    $ JubesX.Mouth = "smile"
                                    ch_v ". . . a part of me was happy when they did."
                                    $ Topics.append("fail")
                            "Did anyone take care of you?" if "mother" not in Topics:
                                    $ JubesX.FaceChange("smile",0)
                                    ch_v "My mother, Sarah Kinney."
                                    ch_v "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ JubesX.FaceChange("sadside",0)
                                    ch_v "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ Line = "mother"
                            "How did you escape?" if "escape" not in Topics:
                                    $ JubesX.FaceChange("sadside",0)
                                    ch_v "Mother."
                                    ch_v "She got me out, found me an escape route."
                                    ch_v "It was the last thing she did."
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
                                    $ JubesX.FaceChange("smile",0)
                                    ch_v "Her name was Sarah Kinney."
                                    ch_v "She's the one who birthed me, and was also one of the scientists that helped create me."
                                    $ JubesX.FaceChange("sadside",0)
                                    ch_v "She tried to help me, until I killed her."
                                    $ Topics.append("mother")
                                    $ Line = "mother"
                            "Why would you kill her?" if "killed" not in Topics and "mother" in Topics:
                                    $ JubesX.FaceChange("sad",0,Eyes="surprised")
                                    ch_v "I didn't want to, but the Trigger scent made me. . ."
                                    $ JubesX.FaceChange("sadside",0)
                                    if "trigger" in JubesX.History:
                                            ch_v "I've mentioned that to you before. . ."
                                    else:
                                            $ JubesX.History.append("trigger")
                                    ch_v ". . . it can make me kill, even if I don't want to."
                                    $ Topics.append("killed")
                            "It wasn't your fault." if "killed" in Topics:
                                    $ JubesX.Statup("Love", 200, 5)
                                    $ JubesX.Statup("Obed", 70, 5)
                                    $ JubesX.Statup("Inbt", 70, 5)
                                    $ JubesX.FaceChange("sad",0)
                                    ch_v "Not completely, no."
                                    $ JubesX.FaceChange("sadside",0)
                                    ch_v "But my hands aren't clean."
                                    $ Line = "facility"
                            "That must have been horrible." if "killed" in Topics:
                                    $ JubesX.FaceChange("sadside",0)
                                    $ JubesX.Statup("Love", 200, 5)
                                    $ JubesX.Statup("Obed", 90, 5)
                                    ch_v "It's taken me some time. . ."
                                    $ JubesX.FaceChange("normal",0)
                                    ch_v "but I think I'm ok with it now."
                                    $ Line = "facility"
                            "Bummer." if "killed" in Topics:
                                    $ JubesX.FaceChange("angry",1)
                                    $ JubesX.Statup("Love", 200, -10)
                                    $ JubesX.Statup("Obed", 90, 5)
                                    ch_v "Are you seriously making fun of my mother's death?!"
                                    $ Topics.append("exit")
                                    $ Line = "angry"
                # end questions about mother

                if Line == "NYX":
                        menu:
                            extend ""
                            "What did you do for a living?" if "living" not in Topics:
                                    $ JubesX.FaceChange("sadside",0)
                                    ch_v "There wasn't much I could do at the time, I mostly just scrounged for food."
                                    ch_v "You can get by on some pretty awful stuff if you have a healing factor."
                                    $ JubesX.FaceChange("bemused",1,Brows="sad")
                                    ch_v "I also did some. . . shady stuff."
                                    $ Topics.append("living")

                            "Was it sexual?" if "work" not in Topics and "living" in Topics:
                                    $ JubesX.FaceChange("sadside",2)
                                    $ JubesX.Statup("Obed", 90, 5)
                                    $ JubesX.Statup("Inbt", 90, 10)
                                    ch_v ". . ."
                                    $ JubesX.Blush = 1
                                    ch_v "A little."
                                    $ Line = "work"
                                    $ Topics.append("work")

                            "Did you hurt people?" if "work" not in Topics and "living" in Topics:
                                    $ JubesX.FaceChange("surprised",0,Eyes="normal")
                                    ch_v "No, definitely not."
                                    ch_v "After the facility, I just couldn't take that sort of work anymore."
                                    $ JubesX.FaceChange("bemused",0)
                                    ch_v "I avoided hurting anyone."
                                    $ JubesX.FaceChange("sadside",2)
                                    ch_v "It tended to be more. . . sexual work."
                                    $ Line = "work"
                                    $ Topics.append("work")

                            "And then you eventually made it here? [[exit]" if "xaviers" not in Topics:
                                    $ JubesX.FaceChange("bemused",0)
                                    ch_v "Yeah, eventually."
                                    ch_v "I'd seen Wolverine on the news, and thought maybe he had some answers."
                                    ch_v "He's not around much though."
                                    $ Topics.append("xaviers")
                                    $ Line = 0
                            "Good thing you made it here. [[exit]" if "xaviers" in Topics:
                                    $ JubesX.FaceChange("smile",0)
                                    ch_v "Yeah."
                                    $ Line = 0

                if Line == "work":
                        $ JubesX.FaceChange("sadside",0,Mouth="normal")
                        ch_v "It was mostly the rougher customers."
                        ch_v "The ones who couldn't control their tempers."
                        $ JubesX.FaceChange("angry",0,Mouth="smile")
                        ch_v "Better for the girl who can heal to take the hits, right?"
                        menu:
                                extend ""
                                "That's terrible. I wish I could have protected you.":
                                        $ JubesX.FaceChange("smile",1)
                                        $ JubesX.Statup("Love", 200, 5)
                                        $ JubesX.Statup("Obed", 90, 5)
                                        $ JubesX.Statup("Inbt", 90, -5)
                                        ch_v "Thanks, but I was ok."
                                        $ JubesX.FaceChange("sadside",0)
                                        ch_v "I didn't deserve it, but I felt like I did at the time."
                                "You're strong to have made it out of there.":
                                        $ JubesX.FaceChange("smile",0)
                                        $ JubesX.Statup("Love", 200, 5)
                                        $ JubesX.Statup("Obed", 90, 10)
                                        $ JubesX.Statup("Inbt", 90, 5)
                                        ch_v "Thanks."
                                        ch_v "I didn't really think of it like that. . ."
                                        $ JubesX.FaceChange("sadside",0)
                                        ch_v "I just felt like I'd deserved it."
                                        ch_v "But I realized how wrong that was."
                                "Yeah, that makes sense.":
                                        $ JubesX.FaceChange("confused",1)
                                        $ JubesX.Statup("Love", 200, -5)
                                        $ JubesX.Statup("Obed", 90, 15)
                                        $ JubesX.Statup("Inbt", 90, -5)
                                        ch_v "Don't think before you speak, do you?"
                                        $ JubesX.FaceChange("sadside",0)
                                        ch_v "It wasn't right, I just didn't realize it at the time."
                        ch_v "Eventually I got past it and decided to get out of there."
                        ch_v "Not like they could stop me."
                        $ Line = "NYX"

                if not Line:
                        # Primary menu, falls through to this
                        menu:
                            extend ""
                            "What did you do back at the facility?" if "facility" not in Topics:
                                    $ JubesX.FaceChange("sadside",0)
                                    ch_v "After they tested what I could do, they put me to work."
                                    ch_v "Mainly, I killed people for them."
                                    $ Topics.append("facility")
                                    $ Line = "facility"
                            "More about that facility. . ." if "facility" in Topics:
                                    $ Line = "facility"

                            "Where did you go after you escaped?" if "NYX" not in Topics:
                                    $ JubesX.FaceChange("sadside",0)
                                    ch_v "I wandered in the wilderness for weeks."
                                    ch_v "Eventually I found my way to New York."
                                    ch_v "I lived on the streets for a few years."
                                    $ Topics.append("NYX")
                                    $ Line = "NYX"
                            "More about after the escape. . ." if "NYX" in Topics:
                                    $ Line = "NYX"

                            "I'm glad you shared that with me. [[exit]" if len(Topics) >= 5:
                                    $ JubesX.FaceChange("smile",0)
                                    $ JubesX.Statup("Love", 200, 10)
                                    $ JubesX.Statup("Obed", 90, 3)
                                    $ JubesX.Statup("Inbt", 90, 3)
                                    ch_v "Thanks for listening to me ramble."
                                    $ Topics.append("exit")
                            "I think that's probably enough. [[exit]" if "facility" in Topics and "NYX" in Topics:
                                    $ JubesX.FaceChange("sadside",0, Mouth="smile")
                                    $ JubesX.Statup("Obed", 90, 10)
                                    ch_v "Yeah, you get the idea."
                                    $ Topics.append("exit")
                            "I don't really care about that. [[exit]":
                                    $ JubesX.FaceChange("angry",0)
                                    $ JubesX.Statup("Love", 200, -15)
                                    $ JubesX.Statup("Obed", 50, 5)
                                    $ JubesX.Statup("Obed", 90, 10)
                                    $ JubesX.Statup("Inbt", 90, -5)
                                    ch_v "Oh, I'm sorry if I was boring you with my life story."
                                    $ Line = "angry"
                                    $ Topics.append("exit")

        #end while loop

        if Line == "angry":
                $ JubesX.FaceChange("angry",0)
                ch_v "And here I was thinking that I meant something to you."
                ch_v "Well forget that!"
                $ Line = 0
                $ JubesX.Event[6] = 23
                $ JubesX.RecentActions.append("angry")
                $ JubesX.DailyActions.append("angry")
                hide Jubes_Sprite with easeoutright
                call Remove_Girl(JubesX)
                $ JubesX.Loc = "hold" #puts her off the board for the day
                return

        $ JubesX.FaceChange("bemused",0,Eyes="down")
        ch_v "I just thought you should know,"
        $ JubesX.FaceChange("smile",2)
        ch_v "I love you."
        menu:
                extend ""
                "I love you too!":
                    $ JubesX.FaceChange("smile",1)
                    $ JubesX.Statup("Love", 200, 20)
                    $ JubesX.Statup("Inbt", 90, 5)
                    ch_v "For a second there you had me worried."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_Love_End
                "I know.":
                    $ JubesX.FaceChange("smile",1)
                    $ JubesX.Statup("Love", 200, 10)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 10)
                    $ JubesX.Statup("Lust", 90, 5)
                    ch_v "Smooth one. Seriously though, how about you?"
                "Neat?":
                    $ JubesX.FaceChange("confused",1)
                    $ JubesX.Statup("Obed", 90, 5)
                    ch_v "I'm gonna need a bit more there, [JubesX.Petname]."
                "Huh.":
                    $ JubesX.FaceChange("confused",1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 10)
                    ch_v "I'm not sure how to take that one."


        menu:
                extend ""
                "Oh, I love you too!":
                    $ JubesX.FaceChange("smile",1)
                    $ JubesX.Statup("Love", 200, 15)
                    $ JubesX.Statup("Obed", 90, 5)
                    $ JubesX.Statup("Inbt", 90, 5)
                    ch_v "For a second there you had me worried."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_Love_End
                "I. . . love you back?":
                    $ JubesX.FaceChange("confused",1)
                    $ JubesX.Statup("Love", 200, 5)
                    $ JubesX.Statup("Obed", 90, 10)
                    ch_v "Ok, I'll take it."
                    $ JubesX.Petnames.append("lover")
                    jump Jubes_Love_End
                "I mean, that's cool and all. . .":
                    $ JubesX.FaceChange("sadside",1)
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 90, 10)
                    $ JubesX.Statup("Inbt", 90, -5)
                    ch_v ". . . but you don't love me back. Got it."
                "That's. . . uncomfortable.":
                    $ JubesX.FaceChange("angry",1)
                    $ JubesX.Statup("Love", 200, -10)
                    $ JubesX.Statup("Obed", 90, 15)
                    $ JubesX.Statup("Inbt", 90, -5)
                    ch_v "I don't like where this is heading."

        ch_v "What's your problem?"
        ch_v "Is it someone else?"
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
                        $ JubesX.Statup("Obed", 90, 15)
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.Statup("Lust", 90, 5)
                        $ JubesX.FaceChange("sadside",1)
                        ch_v "Well, you do have your pick."
                "There's nobody else.":
                        $ JubesX.Statup("Love", 200, -15)
                        $ JubesX.Statup("Obed", 90, 15)
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.FaceChange("sad",1)
                        if ApprovalCheck(JubesX, 1000, "OI"):
                            ch_v "I guess that's something."
                        else:
                            ch_v ". . ."
                "It's a \"you\" problem.":
                        $ JubesX.FaceChange("angry")
                        $ JubesX.Statup("Love", 200, -25)
                        $ JubesX.Statup("Obed", 90, 15)
                        ch_v "You're seriously messing with me?"
                        $ JubesX.Statup("Love", 200, -10)
                        ch_v "You don't want to see me when I'm angry."
                        $ JubesX.RecentActions.append("angry")
                        $ JubesX.DailyActions.append("angry")


        if Line:
                #If you called out a girl,
                if JubesX.GirlLikeCheck(Line) >= 800:
                        $ JubesX.Statup("Love", 200, 5)
                        $ JubesX.Statup("Obed", 90, 20)
                        $ JubesX.Statup("Inbt", 90, 5)
                        $ JubesX.Statup("Lust", 90, 5)
                        $ JubesX.FaceChange("sadside",1)
                        ch_v "Yeah, I guess she's great."
                else:
                        $ JubesX.FaceChange("angry",Eyes="side")
                        $ JubesX.Statup("Love", 200, -5)
                        $ JubesX.Statup("Obed", 90, 20)
                        ch_v "Bitch."
                        $ JubesX.RecentActions.append("angry")
                        $ JubesX.GLG(Line,800,-50,1)
        ch_v "Well, if that's the way you feel about it. . ."
        ch_v "I'll. . . see you later."
        ch_v "This. . . hurt."

label Jubes_Love_End:
        if "lover" not in JubesX.Petnames:
                $ JubesX.Event[6] = 20
                hide Jubes_Sprite with easeoutright
                call Remove_Girl(JubesX)
                $ JubesX.Loc = "hold" #puts her off the board for the day
                return

        $ JubesX.Event[6] = 5
        "[JubesX.Name] grabs you in a crushing hug."
        $ JubesX.Statup("Love", 200, 25)
        $ JubesX.Statup("Lust", 90, 5)
        $ JubesX.FaceChange("sly",1)
        ch_v "So. . . now that we have some free time. . ."
        $ JubesX.Statup("Lust", 90, 10)

        if not JubesX.Sex:
            $ JubesX.FaceChange("bemused",2)
            ch_v "I think I'm ready. . ."
        else:
            ch_v "Would you like to have some fun?"
        $ Player.AddWord(1,"interruption") #adds to Recent
        menu:
                extend ""
                "Yeah, let's do this. . . [[have sex]":
                    $ JubesX.Statup("Inbt", 30, 20)
                    $ JubesX.Statup("Obed", 70, 10)
                    ch_v "Hmm. . ."
                    call Jubes_SexAct("sex")
                "I have something else in mind. . .[[choose another activity]":
                    $ JubesX.Brows = "confused"
                    $ JubesX.Statup("Obed", 70, 25)
                    ch_v "Like what? . ."
                    $ temp_modifier = 20
                    call Jubes_SexMenu
        return

label Jubes_Love_Redux:
         #this is for if you rejected her but want a second chance
        $ Line = 0
        $ JubesX.DailyActions.append("relationship")

        if JubesX.Event[6] >= 25:
                #if this is the second time through
                ch_p "I hope you've forgiven me, I still love you."
                $ JubesX.Statup("Love", 95, 10)
                if ApprovalCheck(JubesX, 950, "L"):
                    $ Line = "love"
                else:
                    $ JubesX.FaceChange("angry")
                    ch_v "You're still working your way out of the hole, [JubesX.Petname]."
                    $ JubesX.Eyes="side"
                    ch_v ". . ."
                    $ JubesX.FaceChange("angry",Mouth="lipbite")
                    ch_v "But let me hear your pitch."
        elif JubesX.Event[6] >= 23:
                #if you pissed her off the first time
                ch_p "I was rude when you opened up to me before."
                $ JubesX.Statup("Love", 95, 10)
                if ApprovalCheck(JubesX, 950, "L"):
                    ch_v "And. . ."
                else:
                    $ JubesX.FaceChange("angry")
                    ch_v "You're still working your way out of the hole, [JubesX.Petname]."
                    $ JubesX.Eyes="side"
                    ch_v ". . ."
                    $ JubesX.FaceChange("angry",Mouth="lipbite")
                    ch_v "But let me hear your pitch."
        else:
                    ch_p "Remember when I told you that I didn't love you?"
                    $ JubesX.FaceChange("perplexed",1)
                    ch_v ". . ."
                    $ JubesX.FaceChange("angry", Eyes="side")
                    ch_v "How could I forget?"

        if Line != "love":
                menu:
                    extend ""
                    "I'm sorry, I didn't mean it.":
                        $ JubesX.Eyes = "surprised"
                        ch_v "Oh really?"
                        ch_v "That's awfully convenient."
                        ch_p "Yeah. I mean, yes, I love you, [JubesX.Name]."
                        $ JubesX.Statup("Love", 200, 10)
                        if ApprovalCheck(JubesX, 950, "L"):
                            $ Line = "love"
                        else:
                            $ JubesX.FaceChange("sadside")
                            ch_v "Well, maybe I don't, anymore. . ."
                    "I've changed my mind, I do love you, so. . .":
                        if ApprovalCheck(JubesX, 950, "L"):
                            $ Line = "love"
                            ch_v "Well that's great."
                        else:
                            $ JubesX.Mouth = "sad"
                            ch_v "Good for you."
                            $ JubesX.Statup("Inbt", 90, 10)
                            $ JubesX.FaceChange("sadside")
                            ch_v "I don't exactly have the same mind either. . ."
                    "Um, never mind.":
                            $ JubesX.Statup("Love", 200, -30)
                            $ JubesX.Statup("Obed", 50, 10)
                            $ JubesX.FaceChange("angry")
                            ch_v "Oh, fuck you."
                            $ JubesX.RecentActions.append("angry")
                            $ JubesX.DailyActions.append("angry")
        if Line == "love":
                $ JubesX.Statup("Love", 200, 40)
                $ JubesX.Statup("Obed", 90, 10)
                $ JubesX.Statup("Inbt", 90, 10)
                $ JubesX.FaceChange("smile")
                ch_v "I'm glad you came around."
                ch_v "I love you too, [JubesX.Petname]!"
                if JubesX.Event[6] < 25:
                        $ JubesX.FaceChange("sly")
                        "She grabs the back of your head and pulls you close."
                        ch_v "Next time, don't keep me waiting."
                $ JubesX.Petnames.append("lover")
        $ JubesX.Event[6] = 25
        return

label Jubes_Sub:
    $ JubesX.DrainWord("asked meet")
    call Shift_Focus(JubesX)
    if JubesX.Loc != bg_current and JubesX not in Party:
        "Suddenly, [JubesX.Name] shows up and says she needs to talk to you."

    $ JubesX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(JubesX)
    call CleartheRoom(JubesX)
    call Set_The_Scene
    call Taboo_Level
    $ JubesX.DailyActions.append("relationship")
    $ JubesX.FaceChange("bemused", 1)

    $ Line = 0
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
    $ JubesX.FaceChange("sly", 1,Eyes="side")
    ch_v "I don't know how I feel about that."
    if JubesX.Event[6]: #if you've done the Love route
            $ JubesX.FaceChange("sadside", 1)
            ch_v "You know the past I've had, with the facility, with the. . . "
            ch_v ". . . work I had to do for them."
            $ JubesX.FaceChange("sad", 1)
            ch_v "I don't know if I want to let anyone tell me what to do like that again."
    menu Jubes_Sub_Question:
        extend ""
        "I guess I can be demanding.":
                $ JubesX.FaceChange("sly", 1)
                $ JubesX.Statup("Obed", 200, 10)
                $ JubesX.Statup("Inbt", 50, 5)
        "Sorry. I didn't mean to come off like that.":
                $ JubesX.FaceChange("sly", 1)
                $ JubesX.Statup("Love", 80, 5)
                $ JubesX.Statup("Obed", 200, -5)
                $ JubesX.Statup("Inbt", 50, -5)
                ch_v "I get it, you're assertive. . ."
        "Remind me about the facility?" if JubesX.Event[6] and Line != "facility":
                $ JubesX.FaceChange("sadside", 1)
                $ JubesX.Statup("Love", 99, -10)
                $ JubesX.Statup("Inbt", 50, -5)
                ch_v "I told you, I was raised in an underground government lab."
                ch_v "They ordered me to kill people for them."
                $ JubesX.FaceChange("sly", 0, Brows= "angry")
                ch_v ". . . until I got tired of taking orders."
                $ Line = "facility"
                jump Jubes_Sub_Question
        "What bothers you about being told to do things?" if not JubesX.Event[6] and Line != "facility":
                $ JubesX.FaceChange("sadside", 1)
                $ JubesX.Statup("Love", 80, 5)
                ch_v "I've just had some rough experiences."
                ch_v "You don't need to know about them."
                ch_v ". . ."
                $ JubesX.FaceChange("sad", 0)
                ch_v "Let's just say I was ordered to do some things I regret."
                $ Line = "facility"
                jump Jubes_Sub_Question
        "Get with the program.":
                if ApprovalCheck(JubesX, 1000, "LO"):
                        $ JubesX.FaceChange("sly", 1)
                        $ JubesX.Statup("Obed", 200, 20)
                        $ JubesX.Statup("Inbt", 50, 10)
                        ch_v "Hmmm. . ."
                else:
                        $ JubesX.Statup("Love", 200, -10)
                        $ JubesX.Statup("Inbt", 50, -5)
                        $ JubesX.FaceChange("angry",0)
                        ch_v "You're not off to a good start here. You might want to rethink your attitude."
                        menu:
                            extend ""
                            "Sorry.  I thought that's what you were into.":
                                    $ JubesX.FaceChange("perplexed", 1,Eyes="side")
                                    $ JubesX.Eyes = "side"
                                    $ JubesX.Statup("Love", 75, 10)
                                    $ JubesX.Statup("Obed", 200, 5)
                                    $ JubesX.Statup("Inbt", 50, 5)
                                    ch_v ". . . after I just said. . ."
                                    $ JubesX.FaceChange("sly", 1)
                                    ch_v "Ok, whatever."
                            "I don't care.":
                                    $ JubesX.Statup("Love", 95, -10)
                                    ch_v "I guess not."
                                    $ Line = "rude"
    if Line == "facility":
            $ Line = 0

    if not Line:
            # She's advancing to the next stage
            $ JubesX.FaceChange("sly", 1)
            ch_v "Look, it's not like. . ."
            $ JubesX.FaceChange("sly", 2)
            ch_v ". . . it's not like I hate it."
            $ JubesX.FaceChange("smile", 1, Eyes="side")
            ch_v ". . . I actually think it might make me. . ."
            menu:
                extend ""
                "-excited?":
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.Statup("Inbt", 50, 5)
                    ch_v ". . ."
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Lust", 50, 10)
                    ch_v "a little, yeah."
                "-digusted?":
                    $ JubesX.Statup("Love", 75, -5)
                    $ JubesX.Statup("Obed", 200, -5)
                    $ JubesX.FaceChange("sadside", 1)
                    ch_v ". . . kind of,"
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Inbt", 70, 5)
                    $ JubesX.Statup("Lust", 50, 5)
                    ch_v "but also kind of excited by it."
                "-hungry?":
                    $ JubesX.FaceChange("confused", 1,Eyes="surprised",Mouth="smile")
                    $ JubesX.Statup("Obed", 200, -5)
                    $ JubesX.Statup("Inbt", 50, -5)
                    ch_v "?!"
                    $ JubesX.FaceChange("confused", 1,Eyes="normal",Mouth="smile")
                    ch_v "Well. . . yeah? But not for-"
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Lust", 50, 5)
                    ch_v "I mean, it makes me kind of. . . excited."
                "-horny?":
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.Statup("Inbt", 50, 5)
                    $ JubesX.FaceChange("startled", 2,Mouth="lipbite")
                    ch_v "!"
                    $ JubesX.FaceChange("sly", 1, Eyes="side")
                    $ JubesX.Statup("Inbt", 50, 5)
                    $ JubesX.Statup("Lust", 50, 10)
                    $ JubesX.Statup("Lust", 70, 5)
                    ch_v "Yes."
            menu:
                extend ""
                "Good. If you wanna be with me, then you follow my orders.":
                        if ApprovalCheck(JubesX, 1000, "LO"):
                            $ JubesX.FaceChange("sly", 1)
                            $ JubesX.Statup("Obed", 200, 15)
                            $ JubesX.Statup("Inbt", 50, 10)
                            ch_v "Hmmm. . ."
                        else:
                            $ JubesX.FaceChange("sadside", 1,Mouth="normal")
                            $ JubesX.Statup("Love", 200, -5)
                            $ JubesX.Statup("Obed", 200, 10)
                            ch_v "You might want to slow your roll there, [JubesX.Petname]."
                            menu:
                                extend ""
                                "Whatever. That's how it is. Take it or leave it.":
                                        $ JubesX.FaceChange("angry")
                                        $ JubesX.Statup("Love", 200, -10)
                                        $ JubesX.Statup("Obed", 200, 5)
                                        ch_v "I think you're pushing it too far there, [JubesX.Petname]."
                                        $ Line = "rude"
                                "Ok, just a little." :
                                        $ JubesX.FaceChange("bemused", 1)
                                        $ JubesX.Statup("Love", 95, 5)
                                        $ JubesX.Statup("Inbt", 50, 5)
                                        ch_v "-but not too much."

                "Yeah? You think it's sexy?":
                                        $ JubesX.FaceChange("bemused", 2,Eyes="side")
                                        $ JubesX.Statup("Obed", 200, 5)
                                        $ JubesX.Statup("Inbt", 50, 10)
                                        ch_v ". . ."
                                        $ JubesX.Statup("Lust", 50, 5)
                                        ch_v "Yeah."

                "You sure you don't want me to back off a little?":
                        $ JubesX.FaceChange("startled", 1,Eyes="squint")
                        $ JubesX.Statup("Obed", 200, -5)
                        menu:
                            ch_v "Well if you have to ask. . ."
                            "Only if you're okay with it.":
                                $ JubesX.FaceChange("bemused", 1)
                                $ JubesX.Statup("Love", 95, 10)
                                $ JubesX.Statup("Inbt", 50, 10)
                                $ Line = 0
                            "Uhm. . .yeah. I think it's weird.  Sorry.":
                                $ JubesX.FaceChange("sad", 1, Eyes="surprised")
                                $ JubesX.Statup("Love", 200, -15)
                                $ JubesX.Statup("Obed", 200, -5)
                                $ JubesX.Statup("Inbt", 50, -10)
                                $ Line = "embarrassed"

                "I couldn't care less.":
                                $ JubesX.Statup("Love", 200, -10)
                                $ JubesX.Statup("Obed", 200, 15)
                                $ JubesX.FaceChange("angry")
                                ch_v "I think you're pushing it too far there, [JubesX.Petname]."
                                $ Line = "rude"

    if not Line:
        $ JubesX.FaceChange("bemused", 1,Eyes = "down")
        ch_v "So, I'm willing to give this a shot."
        ch_v "Just a trial period, to see how it goes."
        ch_v "Just tell me what you want, and. . . I'll see about doing it."
        menu Jubes_Sub_Choice:
            extend ""
            "I think I could get used to that kinda thing.":
                    $ JubesX.Statup("Obed", 200, 5)
                    $ JubesX.Statup("Inbt", 50, 5)
                    $ JubesX.FaceChange("sly", 1)
                    $ Line = 0
            "Don't you think that relationship's kinda. . .weird?":
                    $ JubesX.FaceChange("sad", 1, Eyes="surprised")
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Inbt", 50, -15)
                    $ Line = "embarrassed"

    if not Line:
        $ JubesX.FaceChange("smile", 1)
        ch_v "Cool. so is there anything you need. . . sir?"
        menu:
            extend ""
            "That has a nice ring to it.":
                    $ JubesX.Statup("Love", 95, 5)
                    $ JubesX.Statup("Obed", 200, 15)
                    $ JubesX.Statup("Inbt", 50, 5)
                    ch_v "Yes, sir."
                    $ JubesX.Petname = "sir"
            "That's kind of formal, isn't it?":
                $ JubesX.FaceChange("perplexed", 1)
                ch_v "Huh. ok, no problem"
                $ JubesX.Statup("Inbt", 50, -5)
                $ JubesX.FaceChange("sly", 1,Eyes="side")
                menu:
                    ch_v "You'll still give me some orders, right?"
                    "Yeah, no problem.":
                            $ JubesX.Statup("Obed", 200, 10)
                            $ JubesX.FaceChange("smile", 1)
                            ch_v "Good."
                    "I don't feel comfortable with that. . .":
                            $ JubesX.FaceChange("sad", 1, Eyes="side")
                            $ JubesX.Statup("Love", 200, -10)
                            $ JubesX.Statup("Obed", 200, -30)
                            $ JubesX.Statup("Inbt", 50, -15)
                            $Line = "embarrassed"

    $ JubesX.History.append("sir")
    if not Line:
            $ JubesX.Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":
            call Remove_Girl(JubesX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[JubesX.Name] knocks her way past you and storms off."
    elif Line == "embarrassed":
            $ JubesX.FaceChange("sadside", 2)
            ch_v "Huh, ok, if you're not interested. . .."
            hide Jubes_Sprite with easeoutright
            call Remove_Girl(JubesX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[JubesX.Name] heads out of the room."
    return

label Jubes_Sub_Asked:
    $ Line = 0
    $ JubesX.FaceChange("sadside", 1)
    ch_v "Yeah. You didn't seem into the idea."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in JubesX.Petnames and ApprovalCheck(JubesX, 850, "O"):
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck(JubesX, 550, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        pass
                else: #if it failed both those things,
                        $ JubesX.FaceChange("angry", 1)
                        ch_v "It was a bad idea, don't worry about it." #Failed again. :(
                        $ Line = "rude"

                if Line != "rude":
                        $ JubesX.Statup("Love", 90, 10)
                        $ JubesX.FaceChange("sly", 1)
                        ch_v "Well, it's not like you stopped ordering me around anyway."
                        ch_v "Ok, let's give it a shot."

        "I know it's what you want. Do you want to try again, or not?":
                $ JubesX.FaceChange("bemused", 1)
                if "sir" in JubesX.Petnames:
                    if ApprovalCheck(JubesX, 850, "O"):
                        ch_v "Ok, fine."
                    else:
                        ch_v "Nah, I'm good."
                        $ Line = "rude"
                elif ApprovalCheck(JubesX, 600, "O"):
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        $ JubesX.FaceChange("confused", 1)
                        ch_v "Kinda wishy-washy there."
                        $ JubesX.FaceChange("sly", 1)
                        ch_v "but maybe you're right."
                        ch_v "Are you sure you're into this?"
                        menu:
                            extend ""
                            "Yes, I'm sorry I was mean about it.":
                                            $ JubesX.Statup("Love", 90, 15)
                                            $ JubesX.Statup("Inbt", 50, 10)
                                            $ JubesX.FaceChange("bemused", 1)
                                            $ JubesX.Eyes = "side"
                                            ch_v "Ok then."
                            "You're damned right I am, bitch.":
                                    if "sir" in JubesX.Petnames and ApprovalCheck(JubesX, 900, "O"):
                                            $ JubesX.Statup("Love", 200, -5)
                                            $ JubesX.Statup("Obed", 200, 10)
                                            ch_v ". . ."
                                    elif ApprovalCheck(JubesX,700, "O"):
                                            $ JubesX.Statup("Love", 200, -5)
                                            $ JubesX.Statup("Obed", 200, 10)
                                            ch_v "Hmmm. . ."
                                    else: #if it failed both those things,
                                            $ JubesX.Statup("Love", 200, -10)
                                            $ JubesX.Statup("Obed", 90, -10)
                                            $ JubesX.Statup("Obed", 200, -10)
                                            $ JubesX.Statup("Inbt", 50, -15)
                                            $ JubesX.FaceChange("angry", 1)
                                            ch_v "Wow, that's pushing it."
                                            $ Line = "rude"
                            "Ok, never mind then.":
                                            $ JubesX.FaceChange("angry", 1)
                                            $ JubesX.Statup("Love", 200, -10)
                                            $ JubesX.Statup("Obed", 90, -10)
                                            $ JubesX.Statup("Obed", 200, -10)
                                            $ JubesX.Statup("Inbt", 50, -15)
                                            ch_v "I was thinking of taking orders from you, not mindgames."
                                            ch_v "I should've known you'd be like this."
                                            $ Line = "rude"

    $ JubesX.RecentActions.append("asked sub")
    $ JubesX.DailyActions.append("asked sub")
    if Line == "rude":
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Jubes_Sprite with easeoutright
            call Remove_Girl(JubesX)
            $ JubesX.RecentActions.append("angry")
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[JubesX.Name] checks you as she stomps out of the room."
    elif "sir" in JubesX.Petnames:
            #it didn't fail and "sir" was covered
            $ JubesX.Statup("Obed", 200, 50)
            $ JubesX.Petnames.append("master")
            $ JubesX.Petname = "master"
            $ JubesX.Eyes = "sly"
            ch_v ". . . master. . ."
    else:
            #it didn't fail
            $ JubesX.Statup("Obed", 200, 30)
            $ JubesX.Petnames.append("sir")
            $ JubesX.Petname = "sir"
            $ JubesX.FaceChange("sly", 1)
            ch_v ". . . sir."
    return

label Jubes_Master:
    $ JubesX.DrainWord("asked meet")
    call Shift_Focus(JubesX)
    if JubesX.Loc != bg_current and JubesX not in Party:
        "Suddenly, [JubesX.Name] shows up and says she needs to talk to you."

    $ JubesX.Loc = bg_current
    call Set_The_Scene(0)
    call Display_Girl(JubesX)
    call CleartheRoom(JubesX)
    call Set_The_Scene
    $ JubesX.DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ JubesX.FaceChange("sly", 1)
    ch_v "[JubesX.Petname]. . ."
    ch_v ". . . permission to speak freely. . ."
    menu:
        extend ""
        "Granted.":
            $ JubesX.Statup("Obed", 200, 5)
            $ JubesX.Statup("Inbt", 50, 5)
        "What?":
            ch_v "I was asking if I could talk to you about something. . ."
            $ JubesX.Eyes = "side"
            ch_v ". . . personal."
            $ JubesX.Eyes = "squint"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ JubesX.Statup("Love", 80, 5)
                    $ JubesX.Statup("Obed", 200, 5)
                    ch_v "Right. . ."
                "Oh, then no.":
                    $ JubesX.FaceChange("sad", 1)
                    $ JubesX.Statup("Love", 80, -5)
                    $ JubesX.Statup("Obed", 200, -10)
                    $ Line = "embarrassed"
        "No.":
            $ JubesX.FaceChange("perplexed", 1,Brows="confused")
            $ JubesX.Statup("Love", 80, -5)
            $ JubesX.Statup("Obed", 200, -5)
            $ JubesX.Statup("Inbt", 50, -5)
            ch_v "- are you sure about that?"
            menu:
                extend ""
                "Oh, go ahead.":
                    $ JubesX.FaceChange("confused", 1)
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.Statup("Inbt", 60, 10)
                    ch_v "Right. . ."
                "Yes, not interested.":
                    $ JubesX.FaceChange("sad", 1)
                    $ JubesX.Statup("Love", 80, -5)
                    $ JubesX.Statup("Inbt", 50, -10)
                    $ Line = "embarrassed"


    if not Line:
        $ JubesX.FaceChange("sly", 1)
        ch_v "I think I enjoy having you in charge."
        ch_v "It gives me. . . structure. . ."
        menu:
            extend ""
            "I like it too.":
                    $ JubesX.FaceChange("sly", 1)
                    $ JubesX.Statup("Obed", 200, 5)
                    ch_v "Good. Maybe we could take this a bit more seriously?"
                    menu:
                        extend ""
                        "Nah. This is just about perfect.":
                                $ JubesX.FaceChange("sad", 1)
                                $ JubesX.Statup("Obed", 200, -15)
                                $ JubesX.Statup("Love", 80, 10)
                                $ Line = "fail"
                        "What'd you have in mind?":
                                $ JubesX.Eyes = "side"
                                ch_v "I was thinking I could start calling you. . . {i}master{/i}?"
                                $ JubesX.Eyes = "squint"
                                menu:
                                    extend ""
                                    "Oh, yeah.  I'd like that.":
                                            $ JubesX.Statup("Obed", 200, 5)
                                            ch_v "Good. . ."
                                    "Um. . .nah.  That's too much.":
                                            $ JubesX.FaceChange("sadside", 1)
                                            $ JubesX.Statup("Obed", 200, -15)
                                            $ JubesX.Statup("Inbt", 50, 5)
                                            $ Line = "fail"

                        "Actually, I'd prefer we stopped doing it. Too much pressure.":
                                $ JubesX.FaceChange("sad", 1)
                                $ JubesX.Statup("Love", 200, -5)
                                $ JubesX.Statup("Obed", 200, -10)
                                $ JubesX.Statup("Inbt", 50, 15)
                                $ Line = "fail"

                        "Actually, let's stop that. It's creeping me out.":
                                $ JubesX.FaceChange("angry", 2, Eyes="surprised")
                                $ JubesX.Statup("Love", 200, -10)
                                $ JubesX.Statup("Obed", 200, -50)
                                $ JubesX.Statup("Inbt", 50, -15)
                                ch_v "Say no more, I wouldn't want to CREEP YOU OUT."
                                $ Line = "embarrassed"

            "As if I care what you think, slut.":
                    $ JubesX.FaceChange("angry", 1, Mouth="smile")
                    $ JubesX.Statup("Love", 90, -20)
                    $ JubesX.Statup("Obed", 200, 10)
                    $ JubesX.Statup("Inbt", 50, -10)
                    ch_v ". . ."
                    menu:
                        ch_v "Excuse me?"
                        "Sorry. I just don't care what you want.":
                                if ApprovalCheck(JubesX, 1400, "LO"):
                                        $ JubesX.Statup("Obed", 200, 10)
                                        ch_v ". . ."
                                        $ JubesX.FaceChange("sly", 1)
                                        $ JubesX.Statup("Love", 200, 20)
                                        $ JubesX.Statup("Inbt", 50, 15)
                                        ch_v ". . .{i}go on. . .{/i}"
                                else:
                                        $ JubesX.Statup("Love", 200, -15)
                                        $ JubesX.Statup("Obed", 200, -10)
                                        $ JubesX.Statup("Inbt", 50, 5)
                                        $ JubesX.FaceChange("angry", 1)
                                        ch_v "!!!"
                                        $ Line = "rude"

                        "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                                $ JubesX.Statup("Love", 200, 10)
                                $ JubesX.Statup("Obed", 200, 10)
                                $ JubesX.Statup("Inbt", 50, 5)
                                if ApprovalCheck(JubesX, 1400, "LO"):
                                        $ JubesX.Statup("Obed", 200, 10)
                                        ch_v ". . ."
                                        $ JubesX.FaceChange("sly", 1)
                                        $ JubesX.Statup("Love", 200, 20)
                                        $ JubesX.Statup("Inbt", 50, 15)
                                        ch_v ". . .{i}no, about right. . .{/i}"
                                else:
                                        $ JubesX.Statup("Love", 200, 5)
                                        $ JubesX.Statup("Obed", 200, -5)
                                        $ JubesX.Statup("Inbt", 50, 5)
                                        $ JubesX.FaceChange("angry", 1, Eyes="side")
                                        ch_v ". . ."
                                        ch_v "We'll work on it. . ."

            "I don't really like it. Too much pressure.":
                                $ JubesX.FaceChange("sad", 2)
                                $ JubesX.Statup("Love", 200, -20)
                                $ JubesX.Statup("Obed", 200, -20)
                                $ JubesX.Statup("Inbt", 50, -10)
                                $ Line = "embarrassed"

    $ JubesX.History.append("master")
    if Line == "rude":
            $ JubesX.RecentActions.append("angry")
            hide Jubes_Sprite with easeoutright
            call Remove_Girl(JubesX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[JubesX.Name] stomps out of the room."
    elif Line == "embarrassed":
            ch_v "Ok, fine then."
            ch_v "And here I was, about to \"elevate your clearance.\""
            hide Jubes_Sprite with easeoutright
            call Remove_Girl(JubesX)
            if "Historia" not in Player.Traits:
                    $ renpy.pop_call()
            "[JubesX.Name] brushes past you on her way out."
    elif Line == "fail":
            ch_v "Oh. . ."
            ch_v "I guess that's fine."
    else:
            $ JubesX.Statup("Obed", 200, 50)
            $ JubesX.Petnames.append("master")
            $ JubesX.Petname = "master"
            ch_v ". . .master."
    return

label Jubes_Sexfriend:   #Jubes_Update
        #set this to occur after class
        $ JubesX.Lust = 70
        $ JubesX.Loc = bg_current
        $ JubesX.DrainWord("asked meet")
        call Set_The_Scene
        $ JubesX.DailyActions.append("relationship")
        call Taboo_Level
        $ Line = 0
        $ JubesX.FaceChange("sly",2,Eyes="side")
        "[JubesX.Name] approaches you and pulls you aside. She seems to be shivering a little bit."
        "She seems to be squirming around and rubbing her thighs together."
        $ JubesX.Petnames.append("sex friend")
        $ JubesX.FaceChange("sly",2)
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
                        $ JubesX.FaceChange("sly",2,Mouth="smile")
                        $Line = "yes"
                    "No thanks":
                        $ JubesX.FaceChange("confused",2)
                        $Line = "no"
                    ". . .":
                        $ JubesX.Statup("Obed", 90, 5)
                        $ JubesX.FaceChange("confused",2)

                if not Line:
                        ch_v "Now, if at all possible. . ."
                        menu:
                            extend ""
                            "Sure":
                                $ JubesX.FaceChange("sly",2,Mouth="smile")
                                $Line = "yes"
                            "No thanks":
                                $ JubesX.FaceChange("confused",2)
                                $Line = "no"

                if Line == "no":
                    $ JubesX.Statup("Love", 200, -5)
                    $ JubesX.Statup("Obed", 80, 5)
                    ch_v "What? Why not?"
                    menu:
                        extend ""
                        "Ok, fine":
                            $ JubesX.FaceChange("confused",2,Mouth="smile")
                            ch_v "Love the enthusiasm."
                            $Line = "yes"
                        "Not interested":
                            $ JubesX.FaceChange("confused",2)

                        "There's someone else":
                            $ JubesX.Statup("Love", 95, -5)
                            $ JubesX.Statup("Obed", 90, 5)
                            if Player.Harem:
                                    $ JubesX.FaceChange("surprised",2)
                                    ch_v "Oh, [Player.Harem[0].Name]?"
                                    $ JubesX.GLG(Player.Harem[0],600,-25,1)
                            $ JubesX.FaceChange("sly",2)
                            ch_v "Well, she doesn't need to know about it. . ."
                            menu:
                                extend ""
                                "Ok, fine":
                                        ch_v "Love the enthusiasm."
                                        $ Line = "yes"
                                "Still no":
                                        pass

        if Line == "no":
                    $ JubesX.Statup("Love", 200, -10)
                    $ JubesX.Statup("Obed", 90, 15)
                    $ JubesX.Statup("Inbt", 90, 10)
                    $ JubesX.FaceChange("sad",2)
                    ch_v "Really?"
                    ch_v "Bummer."
                    ch_v "Well let me know if you change your mind."
                    $ JubesX.FaceChange("sadside",2,Mouth="lipbite",Brows="angry")
                    if Player.Harem:
                            ch_v "Wonder if [Player.Harem[0].Name]'s busy. . ."
                            $ JubesX.GLG(Player.Harem[0],500,25,1)
                    else:
                            ch_v "Wonder if Kitty's busy. . ."
                            $ JubesX.GLG("Kitty",500,25,1)
        else:
                $ JubesX.Statup("Love", 90, 10)
                $ JubesX.Statup("Obed", 90, 5)
                $ JubesX.Statup("Inbt", 90, 15)
                $ JubesX.FaceChange("sly",1,Mouth="smile")
                if Taboo:
                    ch_v "Wanna take this party someplace else?"
                    menu:
                        extend ""
                        "Yeah":
                                ch_v "Sure, let's go."
                                if bg_current == "bg player":
                                        $ bg_current = "bg jubes"
                                else:
                                        $ bg_current = "bg player"
                                $ JubesX.Loc = bg_current
                                call CleartheRoom(JubesX)
                                call Set_The_Scene
                                $ Taboo = 0
                                $ JubesX.Taboo = 0

                        "No, let's do it here.":
                                $ JubesX.Statup("Obed", 80, 5)
                                $ JubesX.Statup("Inbt", 90, 15)
                                ch_v "Kinky."

                $ Situation = JubesX
                $ Player.AddWord(1,"interruption") #adds to Recent
                call Jubes_SexPrep              #she offers sex
                call Jubes_SexMenu

                #end "if no relationship"
        return

label Jubes_Fuckbuddy:
        $ JubesX.DailyActions.append("relationship")
        $ JubesX.Lust = 80
        $ JubesX.DrainWord("asked meet")
        # Conditions, in your room, jubes not there.
        "You hear a knock on the door, and go to answer it."
        #change jubes's outfit to default
        $ JubesX.Loc = bg_current
        call Shift_Focus(JubesX)
        call Set_The_Scene(0)
        $ JubesX.Outfit = "casual1"
        $ JubesX.OutfitDay = "casual1"
        $ JubesX.OutfitChange("casual1")
        call Display_Girl(JubesX)
        call Taboo_Level
        $ Trigger = "masturbation"
        $ Trigger3 = "fondle pussy"
        $ JubesX.FaceChange("sly",2,Mouth="lipbite")
        "[JubesX.Name] is standing in the doorway, with her hand down her pants."
        "You can tell she's been masturbating furiously, her scent is overpowering."
        $ Trigger = 0
        $ Trigger3 = 0
        $ JubesX.ArmPose = 1
        "She looks you up and down hungrily, and pulls her hand out of her pants."
        "She reaches up to caress your face, smearing her juices along it."
        ch_v "Mine."
        $ JubesX.Petnames.append("fuck buddy")
        $ JubesX.Event[10] += 1

        $ Situation = JubesX
        $ Player.AddWord(1,"interruption") #adds to Recent
        call Jubes_SexPrep              #she offers sex
        call Jubes_SexMenu
        return
