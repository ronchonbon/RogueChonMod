label JeanMeet:
        call shift_focus(JeanX)

        $ JeanX.name = "???"
        $ JeanX.AddWord(1,"showered","showered",0,0)
        call remove_girl("all")
        call JeanName(1)


        $ JeanX.location = "bg showerroom"
        $ bg_current = "bg showerroom"
        $ active_Girls.append(JeanX) if JeanX not in active_Girls else active_Girls
        $ line = 0

        $ JeanX.OutfitChange("casual1")
        $ JeanX.Outfit = "casual1"
        $ JeanX.change_face("sly",0)
        call set_the_scene(0,1,0)
        "As you approach the showers, you notice someone getting dressed."
        call set_the_scene(1,0,0)

        ch_j "Hmm. . . I don't think I've seen you around before."
        ch_j "[JeanX.Petname], right?"
        ch_g "I bet someone named [JeanX.Petname] is really freaked out right now. . ."
        menu:
            ch_j "[JeanX.Petname], right?"
            "No, it's [Player.name], actually.":
                    call JeanName #sets new Petname
                    $ JeanX.change_stat("love", 90, -2)
                    $ JeanX.change_stat("obedience", 200, 2)
                    ch_j "Right, [JeanX.Petname], got it."
            "Yup, [JeanX.Petname].":
                    $ JeanX.change_face("sly",Mouth="smile")
                    $ JeanX.change_stat("love", 90, 5)
                    $ JeanX.IX -= 5
                    ch_j "Thought you looked like a \"[JeanX.Petname].\""
            "It's [Player.name], remember it.":
                    call JeanName #sets new Petname
                    $ JeanX.change_face("confused")
                    $ JeanX.change_stat("love", 90, -5)
                    $ JeanX.change_stat("obedience", 200, 5)
                    ch_j "Right, [JeanX.Petname], I heard you!"

        $ JeanX.change_face("sly")
        menu:
            extend ""
            "No, seriously, it's [Player.name]." if Player.name != JeanX.Petname:
                    $ JeanX.change_face("angry",1)
                    $ JeanX.change_stat("love", 90, -5)
                    $ JeanX.change_stat("obedience", 200, 5)
                    $ JeanX.IX -= 5
                    ch_j "I KNOW!!!"
                    $ JeanX.change_face("bemused",0,Eyes="side")
                    ch_j "Seriously [JeanX.Petname], you need to -relax.-"
            "No, it's. . . oh, that's right, [Player.name]." if Player.name == JeanX.Petname:
                    $ JeanX.change_stat("love", 90, 5)
                    $ JeanX.change_stat("obedience", 200, 2)
                    $ JeanX.IX -= 5
                    ch_j "See? Brain like a steel trap."
            "Yup.":
                    $ JeanX.change_stat("love", 90, 5)
                    $ JeanX.change_stat("obedience", 200, 5)
                    $ JeanX.IX -= 5
            "Listen you stupid. . ." if Player.name != JeanX.Petname:
                    $ JeanX.change_face("confused")
                    $ JeanX.change_stat("love", 90, -10)
                    $ JeanX.change_stat("obedience", 200, 2)
                    ch_j "I'm going to stop you right there, [JeanX.Petname]."
                    $ JeanX.change_face("angry",Eyes="psychic")
                    ch_j "If I say your name is [JeanX.Petname], it's [JeanX.Petname]."
                    $ JeanX.change_face("sly")
                    ch_j "Right. . . [JeanX.Petname]?"

                    menu:
                        extend ""
                        "Oh, yeah. [JeanX.Petname].":
                                $ JeanX.change_face("confused",1,Eyes="side")
                                $ JeanX.change_stat("love", 90, 5)
                                $ JeanX.change_stat("obedience", 200, 5)
                                ch_j "Ok. . ."
                        "Whatever.":
                                $ JeanX.change_face("confused",1,Eyes="side")
                                $ JeanX.change_stat("obedience", 200, 10)
                                ch_j ". . ."
                                ch_j "Right. . ."
                        "No, it's [Player.name], pay attention!":
                                $ JeanX.change_face("confused",1,Eyes="side")
                                $ JeanX.change_stat("love", 90, -10)
                                $ JeanX.change_stat("obedience", 200, 10)
                                $ JeanX.change_stat("inhibition", 200, -10)
                                ch_j "Huh?"
                                ch_j "But I. . ."
                                $ JeanX.change_face("angry",1,Eyes="psychic")
                                ch_j "Quack like a duck!"
                                menu:
                                    extend ""
                                    "Quack [[sell it]":
                                            $ JeanX.change_face("smile",0)
                                            $ JeanX.change_stat("love", 90, 5)
                                            $ JeanX.change_stat("obedience", 200, -5)
                                            $ JeanX.change_stat("inhibition", 200, 10)
                                            ch_j "Ah, ok, now we're getting somewhere."
                                    "Quack [[sarcastically]":
                                            $ JeanX.change_face("angry",0,Eyes="squint")
                                            $ JeanX.change_stat("love", 90, -3)
                                            $ JeanX.change_stat("obedience", 200, 10)
                                            $ JeanX.change_stat("inhibition", 200, -5)
                                            ch_j ". . ."
                                            $ JeanX.change_face("sly")
                                            ch_j "Good enough. . ."
                                    "No.":
                                            $ JeanX.change_face("confused",1,Eyes="side")
                                            $ JeanX.change_stat("love", 90, -10)
                                            $ JeanX.change_stat("obedience", 200, 15)
                                            $ JeanX.change_stat("inhibition", 200, -5)
                                            ch_j "This doesn't make sense. . ."
                                            $ JeanX.change_face("angry",1,Eyes="psychic")
                                            ch_j "Could you be too dumb to mind-take? . . "
                                            $ JeanX.change_face("confused",1,Eyes="psychic")
                                            ch_j "No, it worked on Logan. . ."
                                            $ line = "argued"
                    #end "you argue with her about the name thing"

        if not line:#line != "argued":
                #if you went along with her nickname
                $ JeanX.change_face("sly")
                ch_j "Anyway, I know what you were doing here. . ."
                ch_j "I bet you were hoping that you'd catch me naked or something, uh?"
                ch_j "Wanted to see these titties?"
                $ JeanX.ArmPose = 2
                $ JeanX.Uptop = 1 #Uptop up
                pause 1
                $ JeanX.Uptop = 0 #Uptop up
                $ JeanX.change_face("sly",0,Eyes="side")
                $ JeanX.ArmPose = 1
                ch_j "Can't blame you, everyone does, the pervs."
                menu:
                    extend ""
                    ". . . Thanks?":
                            $ JeanX.change_face("bemused")
                            $ JeanX.change_stat("love", 90, 10)
                            $ JeanX.change_stat("obedience", 200, 5)
                            $ JeanX.IX -= 10
                            ch_j "You're welcome, I don't mind being generous. . ."
                    "Wow, those were great!":
                            $ JeanX.change_face("smile")
                            $ JeanX.change_stat("love", 90, 15)
                            $ JeanX.change_stat("obedience", 200, 5)
                            $ JeanX.IX -= 15
                            ch_j "I know, it's nice to put them on display from time to time. . ."
                    "Pretty loose, aren't you?":
                            $ JeanX.change_face("smile",Brows="confused")
                            $ JeanX.change_stat("love", 90, -3)
                            $ JeanX.change_stat("obedience", 200, 10)
                            $ JeanX.change_stat("inhibition", 200, -5)
                            ch_j "Well, only because I know how great they look. . ."
                call first_topless(JeanX, silent = 0, temporary_line = 1)
                $ JeanX.change_face("bemused")
                ch_j ". . . not that you'll remember this in five minutes."
                $ JeanX.change_face("bemused",Eyes="psychic")
                ch_j "Now, what just happened?"
                $ JeanX.change_face("bemused")
                menu:
                    extend ""
                    "Nothing unusual.":
                            $ JeanX.change_stat("love", 90, 5)
                            ch_j "Damned skippy, [JeanX.Petname]."
                    "I. . . don't know?":
                            $ JeanX.change_stat("love", 90, 5)
                            $ JeanX.change_stat("obedience", 200, 10)
                            $ JeanX.change_stat("inhibition", 200, -5)
                            ch_j "Right."
                            $ JeanX.change_face("perplexed",0)
                            ch_j ". . ."
                    "You just flashed me.":
                            $ JeanX.change_stat("love", 90, 5)
                            ch_j "Exactl-{w=0.3}{nw}"
                            $ JeanX.change_face("surprised",2)
                            $ JeanX.change_stat("love", 90, -10)
                            $ JeanX.change_stat("obedience", 200, 10)
                            $ JeanX.change_stat("inhibition", 200, -5)
                            $ JeanX.ArmPose = 2
                            ch_j "Exactl- wait, what?"
                            $ JeanX.change_face("surprised",1)
                            menu:
                                extend ""
                                "I mean, nothing unusual?":
                                        $ JeanX.change_face("confused",1)
                                        $ JeanX.change_stat("love", 90, 5)
                                        $ JeanX.change_stat("obedience", 200, 5)
                                        ch_j ". . ."
                                        $ JeanX.change_face("confused",1,Eyes="side")
                                        ch_j "Right. . ."
                                "You just flashed me.":
                                        $ JeanX.change_face("confused",2)
                                        $ JeanX.change_stat("love", 90,-5)
                                        $ JeanX.change_stat("obedience", 200, 10)
                                        ch_j "How did you remember. . ."
                                        $ JeanX.change_face("angry",1)
                                        ch_j "You should have forgotten that!"
                                        ch_j "I mind took you!"
                                        $ line = "power"
                                "You showed me your tits, you ditz!":
                                        $ JeanX.change_face("angry",2)
                                        $ JeanX.change_stat("love", 90, -20)
                                        $ JeanX.change_stat("obedience", 200, 20)
                                        ch_j "Don't take that tone with me!"
                                        $ JeanX.change_face("confused",1)
                                        ch_j "How did you remember. . ."
                                        $ JeanX.change_face("angry",1)
                                        ch_j "You should have forgotten that!"
                                        ch_j "I mind took you!"
                                        $ line = "power"
                            $ JeanX.ArmPose = 1
        #end flashing sequence

        if not line:
                #if you've managed to not get outed yet. . .
                ch_j "Now, looks like the mirror's all foggy. . ."
                $ JeanX.change_face("sly",Eyes="psychic")
                ch_j "I'll just use your eyes. . ."
                $ JeanX.change_face("confused",1)
                ch_j ". . ."
                $ JeanX.change_face("angry",1)
                $ JeanX.change_stat("love", 90, -5)
                $ JeanX.change_stat("obedience", 200, 5)
                $ JeanX.change_stat("inhibition", 200, -5)
                ch_j "What's happening? Why can't I get inside your head?"
        # end "she tries to see through your eyes"

        menu:
            extend ""
            "I'm immune to mutant powers.":
                    $ JeanX.change_face("confused",1)
                    $ JeanX.change_stat("love", 90, -10)
                    $ JeanX.change_stat("obedience", 200, 10)
                    ch_j "Huh?"
                    ch_j "That's a thing?!"
                    $ JeanX.change_face("angry",1)
                    ch_j "Why did nobody tell me that's a thing?!"
            "I'm already in your head.":
                    $ JeanX.change_face("surprised",2)
                    $ JeanX.change_stat("love", 90, -5)
                    $ JeanX.change_stat("obedience", 200, 30)
                    ch_j "What?!"
                    $ JeanX.change_face("confused",1)
                    ch_j "Wait. . ."
                    $ JeanX.change_face("angry",1)
                    $ JeanX.change_stat("love", 90, -15)
                    $ JeanX.change_stat("obedience", 200, -10)
                    ch_j "No you're not!"
                    ch_j "You're just, like. . . immune to mind-taking or something!"
            "I'm a figment of your imagination.":
                    $ JeanX.change_face("angry",2)
                    $ JeanX.change_stat("love", 90, -5)
                    $ JeanX.change_stat("obedience", 200, 15)
                    ch_j "Now you're just fucking with me."
                    $ JeanX.change_face("angry",1,Mouth="surprised")
                    $ JeanX.change_stat("love", 90, -5)
                    ch_j "I do the fucking!"
                    $ JeanX.change_face("angry",1)
                    ch_j "You're just, like. . . immune to mind-taking or something!"
        $ JeanX.change_stat("inhibition", 200, -200)
        if JeanX.SeenChest:
                $ JeanX.change_face("angry",1)
                ch_j "So you saw my. . ."
                menu:
                    "Yup.":
                            $ JeanX.change_stat("obedience", 200, 3)
                            $ JeanX.change_stat("inhibition", 200, -5)
                    ". . .":
                            $ JeanX.change_stat("obedience", 200, 7)
                    "What?":
                            pass
                $ JeanX.change_face("angry",2)
                ch_j "And you remember? . ."
                menu:
                    "Yup.":
                            $ JeanX.change_stat("love", 90, -3)
                            $ JeanX.change_stat("obedience", 200, 10)
                    ". . .":
                            $ JeanX.change_stat("obedience", 200, 10)
                    "Of course I don't remember you flashing me":
                            $ JeanX.change_face("smile",0)
                            $ JeanX.change_stat("love", 90, 10)
                            $ JeanX.change_stat("inhibition", 200, 50)
                            ch_j "Ok, goo- {w=0.3}{nw}"
                            $ JeanX.change_face("angry",2)
                            $ JeanX.change_stat("love", 90, -20)
                            $ JeanX.change_stat("obedience", 200, 20)
                            $ JeanX.change_stat("inhibition", 200, -40)
                            ch_j "Ok, goo- you're just bullshitting me again!"
        $ JeanX.change_face("angry",1,Eyes="psychic")
        ch_j "Argh!"
        "You feel a slight breeze against your cheek."
        $ JeanX.change_face("angry",1)
        $ JeanX.change_stat("love", 90, -10)
        $ JeanX.change_stat("obedience", 200, 10)
        $ JeanX.change_stat("inhibition", 200, -20)
        ch_j "And you're immune to my telekinesis too?!"
        menu:
            "So long as I want to be, yeah.":
                    pass
            "Yup.":
                    $ JeanX.change_stat("love", 90, -5)
                    $ JeanX.change_stat("obedience", 200, 10)
            ". . .":
                    $ JeanX.change_stat("love", 90, 3)
        $ JeanX.change_stat("obedience", 200, 10)
        $ JeanX.change_face("angry",1,Eyes="psychic")
        "A locker rips from the wall and heads your way."
        "With a pulse of your power, it loses momentum and falls over."
        $ JeanX.change_face("angry",1,Eyes="side")
        $ JeanX.change_stat("obedience", 200, 10)
        $ JeanX.change_stat("inhibition", 200, -10)
        ch_j ". . ."
        ch_j "Well that's inconvenient."
        ch_j "I'm not sure what to do with you. . ."
        $ JeanX.change_face("angry",1)
        ch_j "I'm not used to anyone being able to just. . ."
        $ JeanX.change_face("angry",2,Eyes="side")
        ch_j ". . . ignore me like that. . ."
        ch_j "I'll need to give this some thought. . ."
        #end powers talk

        $ JeanX.History.append("met")
        $ bg_current = "bg showerroom"
        $ Round -= 10
        call shift_focus(RogueX)
        $ JeanX.location = "hold"
        call set_the_scene
        $ JeanX.Outfit = "casual1"
        $ JeanX.OutfitDay = "casual1"
        $ JeanX.OutfitChange("casual1")

        "She collects her things and leaves the room."
        ch_p "Who the hell was that? . ."
        $ EmmaX.OutfitChange("casual1")
        show JeanMFGrey zorder 150:
                pos (-200,100)
                rotate 0
                parallel:
                    ease .5 pos (350,100)
                parallel:
                    pause .4
                    ease .1 rotate 10
                    ease .1 rotate 0
                block:
                    ease .1 pos (350,105)
                    ease .1 pos (350,100)
                    repeat 4
        ". . ."
        hide JeanMFGrey with easeoutleft
        $ EmmaX.change_face("angry",1,Eyes="leftside")
        show Emma_Sprite at sprite_location(-100) zorder 25
        show Emma_Sprite at sprite_location(500) zorder 25 with easeinleft
        call shift_focus(EmmaX)
        ch_e "I mean, that was Jean mother fucking Grey."
        $ JeanX.name = "Jean"
        pause .1
        ch_e "She can be. . . a bit much."
        menu:
            "You said it.":
                    $ EmmaX.change_face("sly")
                    $ EmmaX.change_stat("love", 90, 5)
                    $ EmmaX.change_stat("obedience", 60, 3)
                    $ EmmaX.change_stat("inhibition", 60, 2)
            "I guess.":
                    $ EmmaX.change_face("sly")
                    $ EmmaX.change_stat("obedience", 70, 5)
            "Pretty hot though.":
                    $ EmmaX.change_face("angry",1)
                    $ EmmaX.change_stat("love", 90, -5)
                    $ EmmaX.change_stat("obedience", 40, 3)
                    $ EmmaX.change_stat("obedience", 80, 7)
                    ch_e "You're playing with fire, [EmmaX.Petname]."
        ch_e "Anyway, I was just passing through."
        $ EmmaX.change_face("angry",1,Eyes="side")
        ch_e "Do try to avoid that relentless black hole of drama. . ."
        show Emma_Sprite at sprite_location(-100) with easeinleft
        pause 0.2
        call remove_girl(EmmaX)
        call shift_focus(RogueX)
        call set_the_scene
        return

image JeanMFGrey:
        "images/JeanSprite/JeanMF.png"
        #pos (500,700)

label Jean_Like:
        #if Jean's love value hits 500
        if JeanX.location != bg_current:
                $ JeanX.location = bg_current
                "[JeanX.name] walks up to you."
        call set_the_scene(0)
        call Display_Girl(JeanX)
        call clear_the_room(JeanX)
        call set_the_scene
        $ JeanX.daily_history.append("relationship")
        call Taboo_Level
        $ line = 0
        $ JeanX.change_face("sly",1,Eyes="down")
        ". . .{w=0.5}{nw}"
        $ JeanX.change_face("sly",1)
        "She looks at you appraisingly."

        ch_j "You know. . . you're more fun to hang out with than I expected."
        $ line = "Y"
        if JeanX.Massage >= 5:
                $ JeanX.change_stat("lust", 60, 5)
                ch_j "You give really good massages. . ."
                $ line = "and Y"
        if JeanX.event_counter["orgasm"] >= 10:
                $ JeanX.change_face("sly",1)
                $ JeanX.change_stat("lust", 70, 5)
                ch_j "[line]ou -really- know how to finish them. . ."
                $ line = "and Y"
                if JeanX.event_counter["orgasm"] >= 30:
                        $ JeanX.change_stat("lust", 80, 10)
                        ch_j ". . . seriously. . ."
        if JeanX.SeenPeen:
                $ JeanX.change_face("sly",1)
                $ JeanX.change_stat("love", 200, 5)
                $ JeanX.change_stat("obedience", 90, 10)
                $ JeanX.change_stat("inhibition", 200, 5)
                $ JeanX.change_stat("lust", 85, 5)
                ch_j "[line]ou're certainly well hung too. . ."
        $ line = 0

        ch_j "I really couldn't have a better little sex toy."
        menu:
                    extend ""
                    "I love it too.":
                            $ JeanX.change_face("sly",1)
                            $ JeanX.change_stat("love", 200, 10)
                            $ JeanX.change_stat("obedience", 90, 5)
                            $ JeanX.change_stat("inhibition", 200, 5)
                            ch_j "Good boy. . ."
                            ch_j "Keep this up and I might \"reward\" you more often."
                    "What if I want something more?":
                            $ JeanX.Brows = "confused"
                            $ JeanX.change_stat("obedience", 90, 10)
                            ch_j "Oh?"
                            $ line = "more"
                    "I'm not your toy.":
                            $ JeanX.Brows = "confused"
                            $ JeanX.change_stat("obedience", 90, 15)
                            ch_j "Huh?"

        $ JeanX.History.append("sexfriend")
        if line == "more":
                $ JeanX.Brows = "confused"
                ch_j "What more could you want?"
                menu:
                    extend ""
                    "Could you be my girlfriend?":
                            $ JeanX.change_face("surprised",2)
                            $ JeanX.change_stat("love", 200, 5)
                            $ JeanX.change_stat("obedience", 90, -5)
                            ch_j "Ha! Girlfriend. . ."
                            $ JeanX.change_face("bemused",1,Eyes="side")
                            ch_j "That's just precious!"

                            $ JeanX.change_face("sly",1)
                            if JeanX.event_counter["orgasm"] >= 10:
                                    ch_j "Look, you're pretty hot and all, and you can get it. . ."
                            else:
                                    ch_j "Look, you're pretty hot and all. . ."
                            ch_j "but I just don't see you as \"relationship\" material. . ."

                    "Couldn't we be sex friends?":
                            $ JeanX.change_face("bemused",1,Eyes="side")
                            $ JeanX.change_stat("love", 200, 5)
                            $ JeanX.change_stat("obedience", 90, 10)
                            $ JeanX.change_stat("inhibition", 80, 5)
                            $ JeanX.change_stat("inhibition", 200, 5)
                            $ JeanX.change_stat("lust", 85, 10)
                            ch_j "Hmm. . ."
                            ch_j "Friends with. . . benefits? . ."
                            $ JeanX.change_face("bemused",1)
                            ch_j "I guess we could do that. . ."
                            $ line = 0
                    "Nothing, I guess. . .":
                            $ JeanX.change_face("bemused",1)
                            $ JeanX.change_stat("love", 200, 5)
                            ch_j "Exactly."
                            $ line = 0
        if line:
                menu:
                    extend ""
                    "So what could I do to change your mind?":
                            $ JeanX.change_face("surprised",1)
                            $ JeanX.change_stat("obedience", 90, -10)
                            ch_j "How should I know?!"
                            $ JeanX.change_face("bemused",1,Eyes="side")
                            ch_j "I guess give me some reason to respect you or something?"
                            $ JeanX.change_face("sly",1)
                            ch_j "I mean, fucking around, that's fine, but let's keep this casual."
                    "I guess that's fine.":
                            $ JeanX.change_face("sly",1)
                            $ JeanX.change_stat("love", 200, 5)
                            $ JeanX.change_stat("obedience", 90, -5)
                            $ JeanX.change_stat("inhibition", 200, 5)
                            ch_j "Glad we got that settled."
                    "Bitch.":
                            $ JeanX.change_face("sly",1)
                            $ JeanX.change_stat("obedience", 90, 5)
                            $ JeanX.change_stat("inhibition", 200, 10)
                            $ JeanX.change_stat("lust", 85, 2)
                            ch_j "Yeah, I know."
        $ JeanX.Petname = "sexfriend"
        $ JeanX.Petnames.append("sexfriend")
        return

label Jean_love:
        #if her love hits 800 and obedience over 600
        if JeanX.location != bg_current:
                $ JeanX.location = bg_current
                "[JeanX.name] walks up to you."
        call set_the_scene(0)
        call Display_Girl(JeanX)
        call clear_the_room(JeanX)
        call set_the_scene
        $ JeanX.daily_history.append("relationship")
        call Taboo_Level
        $ line = 0
        $ JeanX.change_face("sly",1)
        ch_j "So. . . [JeanX.Petname]."
        ch_j "This has been going on a while, you and I."
        ch_j "I think my respect for you has grown a lot."
        if JeanX.SEXP >= 30:
                $ JeanX.change_stat("lust", 70, 5)
                ch_j "I mean, you really know how to lay it down."
        if JeanX.obedience < 900:
                $ JeanX.change_face("sly",1,Eyes="side")
                $ JeanX.change_stat("love", 200, 5)
                ch_j "And you're so sweet to me. . ."
        ch_j "I kinda feel like. . ."
        $ line = 0
        menu:
            extend ""
            "I love you.":
                    $ line = "love"
                    $ JeanX.change_face("sly",2)
                    ch_j "I lo-"
                    $ JeanX.change_face("surprised",2)
                    $ JeanX.change_stat("love", 90, 10)
                    $ JeanX.change_stat("love", 200, 10)
                    $ JeanX.change_stat("obedience", 90, 10)
                    ch_j ". . ."
                    $ JeanX.change_stat("inhibition", 200, 5)
                    ch_j "That's what I was going to say!"
            ". . .":
                    $ JeanX.change_stat("obedience", 90, 10)
                    $ JeanX.change_stat("obedience", 200, 5)
                    ch_j "I. . ."
            "You love me.":
                    $ JeanX.change_face("surprised",2)
                    $ JeanX.change_stat("love", 200, 5)
                    $ JeanX.change_stat("obedience", 90, 10)
                    $ JeanX.change_stat("obedience", 200, 5)
                    ch_j ". . ."
                    $ JeanX.change_stat("inhibition", 200, 5)
                    ch_j "Well. . . yeah."
        $ JeanX.change_face("sly",1)
        ch_j "I love you. . ."
        if line != "love":
                menu Jeanlove_Menu:
                    extend ""
                    "I love you too.":
                            $ JeanX.change_stat("love", 90, 5)
                            $ JeanX.change_stat("love", 200, 10)
                            $ JeanX.change_stat("obedience", 90, 10)
                            $ JeanX.change_stat("inhibition", 200, 5)
                            $ JeanX.change_face("smile",1)
                            ch_j "Great!"
                    ". . ." if not line:
                            $ line = "repeat"
                            $ JeanX.change_face("sad",2)
                            $ JeanX.change_stat("love", 200, -5)
                            $ JeanX.change_stat("obedience", 90, 10)
                            $ JeanX.change_stat("obedience", 200, 10)
                            $ JeanX.change_stat("inhibition", 200, -5)
                            ch_j "Well, say something. . ."
                            jump Jeanlove_Menu
                    "Cool." if line != "cool":
                            $ line = "cool"
                            $ JeanX.change_face("angry",1)
                            $ JeanX.change_stat("love", 200, -5)
                            $ JeanX.change_stat("obedience", 90, 10)
                            $ JeanX.change_stat("inhibition", 200, -5)
                            ch_j "I feel like maybe you aren't taking this seriously."
                            jump Jeanlove_Menu
                    "Sorry, I mean \"that's cool.\"" if line == "cool":
                            ch_j ". . ."
                            $ JeanX.change_stat("love", 200, -3)
                            $ JeanX.change_stat("inhibition", 200, -3)
                            ch_j "That still doesn't seem. . ."
                            $ JeanX.change_stat("love", 200, 5)
                            ch_j "Adequate. . ."
                    "I don't feel the same way.":
                            $ JeanX.change_face("surprised",2)
                            $ JeanX.change_stat("love", 200, -5)
                            $ JeanX.change_stat("obedience", 90, 10)
                            $ JeanX.change_stat("obedience", 200, 5)
                            $ JeanX.change_stat("inhibition", 200, -5)
                            ch_j "Oh. . ."
                            $ JeanX.change_face("sadside",1)
                            ch_j "I guess that's fine."
                            ch_j "Whatever."
        ch_j "Anyway, I just wanted to put that out there."
        $ JeanX.Event[5] = 1
        $ JeanX.Petname = "lover"
        $ JeanX.Petnames.append("lover")
        if Player.Harem:
                ch_j "I figured if you wanted me to join your little lady-party, I'm in."
        else:
                ch_j "I figured maybe we could make it official, I could be your girlfriend. . ."
        menu:
            extend ""
            "Sure, the more the merrier." if Player.Harem:
                    $ JeanX.change_stat("love", 200, 5)
                    $ JeanX.change_stat("obedience", 90, 10)
                    $ JeanX.change_stat("obedience", 200, 10)
                    $ JeanX.change_stat("inhibition", 200, 5)
                    $ Player.Harem.append(JeanX)
            "Sure, I'd love to." if not Player.Harem:
                    $ JeanX.change_stat("love", 200, 5)
                    $ JeanX.change_stat("obedience", 90, 10)
                    $ JeanX.change_stat("obedience", 200, 10)
                    $ JeanX.change_stat("inhibition", 200, 5)
                    $ Player.Harem.append(JeanX)
            "I'm not interested.":
                    $ JeanX.change_face("surprised",2)
                    $ JeanX.change_stat("love", 200, -5)
                    $ JeanX.change_stat("obedience", 90, 5)
                    $ JeanX.change_stat("inhibition", 200, -5)
                    ch_j "What?"
                    $ JeanX.change_face("angry",2)
                    ch_j "Why not?!"
                    if len(Player.Harem) >= 2:
                        ch_j "Is it because of the others?"
                    elif Player.Harem:
                        ch_j "Is it because of [Player.Harem[0].name]?"
                    menu:
                        extend ""
                        "Yeah" if Player.Harem:
                                $ JeanX.change_face("angry",1,Eyes="side")
                                call Haremchange_stat(JeanX,700,-5) #lowers like of all Harem girls by 5
                                if len(Player.Harem) >= 2:
                                        ch_j "Bitches."
                                elif Player.Harem:
                                        ch_j "That bitch."
                        "I just don't like you like that.":
                                $ JeanX.change_face("sad",2,Eyes="surprised")
                                $ JeanX.change_stat("love", 90, -5)
                                $ JeanX.change_stat("love", 200, -5)
                                $ JeanX.change_stat("obedience", 90, 5)
                                $ JeanX.change_stat("obedience", 200, 10)
                                $ JeanX.change_stat("inhibition", 200, -5)
                                ch_j "Oh."
                                $ JeanX.change_face("sadside",1)
                                ch_j "."
                                ch_j ". ."
                                ch_j ". . ."
                    $ JeanX.change_face("smile",1,Brows="angry")
                    ch_j "Well, you'll come around."
                    ch_j "You don't find a catch like this every day."
            #not interested

        if JeanX in Player.Harem:
            $ JeanX.change_face("sly",1)
            ch_j "Good."
            if len(Player.Harem) >= 2:
                #if there are other girls in it
                if len(Player.Harem) >= 3:
                    ch_j "And you don't think the others would mind?"
                    $ line = "they're"
                else:
                    ch_j "And you don't think [Player.Harem[0].name] would mind?"
                    $ line = "she's"
                menu:
                    extend ""
                    "No, actually [line] fine with it." if "JeanYes" in Player.Traits:
                            $ JeanX.change_stat("love", 200, 5)
                            $ JeanX.change_stat("obedience", 80, 10)
                            $ JeanX.change_stat("inhibition", 80, 5)
                            $ JeanX.change_face("surprised",1)
                            ch_j "Oh, good."
                    "Actually. . . I guess we'll need to work on that one." if "JeanYes" not in Player.Traits:
                            $ JeanX.change_stat("inhibition", 200, 5)
                            $ JeanX.change_stat("lust", 80, 3)
                            $ JeanX.change_face("confused",1)
                            ch_j "I think I could bring them around. . ."
                            menu:
                                extend ""
                                "No! Don't do that!":
                                        $ JeanX.change_face("sly",1)
                                        $ JeanX.change_stat("obedience", 80, 5)
                                        ch_j "Right."
                                        ch_j ". . ."
                                        $ JeanX.change_stat("inhibition", 200, 5)
                                        $ JeanX.change_stat("lust", 80, 2)
                                        ch_j "-wink-"
                                        menu:
                                            extend ""
                                            "No! No \"wink!\"":
                                                    $ JeanX.change_face("sly",1,Eyes="stunned")
                                                    $ JeanX.change_stat("obedience", 50, 5)
                                                    $ JeanX.change_stat("obedience", 90, 3)
                                                    pause 0.3
                                                    $ JeanX.change_face("sly",1)
                                                    ch_j "Oh, FINE."
                                                    ch_j "You sort things out on your end and get back to me."
                                                    ch_j ". . . just don't take -too- long."
                                                    $ Player.Harem.remove(JeanX)
                                                    $ JeanX.Event[5] = 20
                                                    return
                                            "[[Might as well roll with it. . .]":
                                                    ch_j "Heh."
                                "That would probably be a good idea. . .":
                                                    $ JeanX.change_stat("love", 200, 3)
                                                    $ JeanX.change_stat("obedience", 80, 3)
                                                    $ JeanX.change_stat("inhibition", 80, 1)
                                                    $ JeanX.change_face("sly",0)
                                                    ch_j "Right. On it."
            $ JeanX.Petnames.append("boyfriend")
        #end if Player Harem
        $ line = 0
        return

label Jean_Sub:
        # if her obedience hits 500
        if JeanX.location != bg_current:
                $ JeanX.location = bg_current
                "[JeanX.name] walks up to you."
        call set_the_scene(0)
        call Display_Girl(JeanX)
        call clear_the_room(JeanX)
        call set_the_scene
        $ JeanX.daily_history.append("relationship")
        call Taboo_Level
        $ line = 0
        $ JeanX.change_face("sly",1,Eyes="side")
        ch_j "Hey. . . [JeanX.Petname]."
        $ JeanX.Eyes="squint"
        ch_j "We need to talk."
        $ JeanX.change_face("sadside",1)
        ch_j ". . ."
        ch_j "When we first met. . . I was pretty rude."
        ch_j "I get that."
        $ JeanX.change_face("sly",1,Eyes="leftside")
        ch_j "When you're practically perfect in every way, you can look down your lessers."
        $ JeanX.change_face("angry",1,Eyes="leftside")
        ch_j ". . ."
        ch_j "Maybe that came out wrong."
        $ JeanX.change_face("sly",1)
        ch_j "What I mean is, you've really shown me something lately."
        ch_j "You know how to push my buttons. . ."
        ch_j "-get me to do things I never expected. . ."
        ch_j ". . . -feel- things I never expected. . ."
        menu:
            extend ""
            "So what do you want from me?":
                    $ JeanX.change_stat("love", 80, -3)
                    $ JeanX.change_stat("obedience", 90, -3)
                    $ JeanX.change_stat("inhibition", 80, 2)
                    ch_j "Well. . . I didn't want to spell it out. . ."
            "You know it.":
                    $ JeanX.change_stat("obedience", 80, 3)
                    ch_j ". . ."
            "Oh? That's nice!":
                    $ JeanX.change_face("confused",1)
                    $ JeanX.change_stat("obedience", 80, -3)
                    ch_j "Um, I think you're missing my point. . ."

        $ JeanX.History.append("sir")
        menu:
            extend ""
            "Tell me what you want.":
                    $ JeanX.change_face("sly",1,Eyes="side")
                    $ JeanX.change_stat("love", 80, 5)
                    $ JeanX.change_stat("obedience", 90, 2)
                    ch_j "Well. . . just that. . ."
                    $ JeanX.change_stat("obedience", 90, 2)
                    $ JeanX.change_stat("inhibition", 200, 1)
                    $ JeanX.change_stat("lust", 80, 5)
                    ch_j "Could you. . ."
                    $ JeanX.change_stat("obedience", 80, 2)
                    $ JeanX.change_stat("inhibition", 200, 2)
                    $ JeanX.change_stat("lust", 80, 5)
                    ch_j "boss me around a little more?"
            "Call me your \"Master.\"":
                    $ JeanX.change_stat("love", 200, 5)
                    $ JeanX.change_stat("obedience", 90, 10)
                    $ JeanX.change_stat("inhibition", 200, 5)
                    $ JeanX.change_stat("lust", 85, 10)
                    $ JeanX.change_face("surprised",2)
                    ch_j "!!!"
                    $ JeanX.change_face("sly",1,Eyes="side")
                    $ JeanX.change_stat("obedience", 90, -5)
                    ch_j "Well. . . I don't know about that!"
                    ch_j "I mean. . . I could -maybe- call you. . ."
                    $ JeanX.change_face("sly",1)
                    $ JeanX.change_stat("obedience", 90, 5)
                    $ JeanX.change_stat("lust", 85, 5)
                    ch_j "Sir?"
            "Ok?":
                    $ JeanX.change_face("confused",1)
                    $ JeanX.change_stat("love", 200, 3)
                    ch_j ". . ."
                    ch_j "You still seem kinda lost here. . ."
                    ch_j "Maybe I'm still not being clear, but. . ."
                    $ JeanX.change_face("angry",1,Eyes="side")
                    $ JeanX.change_stat("obedience", 80, -3)
                    ch_j "If I have to spell it out for you, then maybe it's not worth it."
                    menu:
                        extend ""
                        "You want me to tell you what to do.":
                                $ JeanX.change_stat("love", 200, 3)
                                $ JeanX.change_stat("obedience", 90, 5)
                                $ JeanX.change_stat("inhibition", 200, 2)
                                ch_j ". . ."
                                $ JeanX.change_face("sly",1)
                                $ JeanX.change_stat("obedience", 80, 3)
                                $ JeanX.change_stat("lust", 80, 3)
                                ch_j "Yes. . ."
                                menu:
                                    extend ""
                                    "So what will you call me?":
                                            $ JeanX.Eyes="side"
                                            ch_j "How about. . ."
                                            $ JeanX.change_face("sly",1)
                                            $ JeanX.change_stat("love", 200, 5)
                                            $ JeanX.change_stat("obedience", 80, 10)
                                            $ JeanX.change_stat("inhibition", 90, 3)
                                            $ JeanX.change_stat("lust", 80, 3)
                                            ch_j "\"Sir?\""
                                    ". . .":
                                            ch_j "How about I call you. . ."
                                            $ JeanX.change_stat("obedience", 80, 10)
                                            $ JeanX.change_stat("inhibition", 200, 10)
                                            $ JeanX.change_stat("lust", 80, 3)
                                            ch_j "\"Sir?\""
                                    "Call me \"sir.\"":
                                            $ JeanX.change_stat("love", 200, 10)
                                            $ JeanX.change_stat("obedience", 90, 15)
                                            $ JeanX.change_stat("lust", 85, 10)
                                            ch_j ". . ."
                                            $ JeanX.change_stat("obedience", 90, 5)
                                            ch_j "Yes. . . sir."
                                # end "You want me to tell you what to do."

                        "Yeah, I guess. . .":
                                $ JeanX.change_stat("love", 200, -5)
                                $ JeanX.change_stat("obedience", 80, -10)
                                $ JeanX.change_stat("inhibition", 90, -10)
                                ch_j "Hmm. . . maybe so. . ."
                                return
                    #end "ok?"
        $ JeanX.Petname = "sir"
        $ JeanX.Petnames.append("sir")
        $ JeanX.recent_history.append("asked sub")
        $ JeanX.daily_history.append("asked sub")
        return

label Jean_Master:
        if JeanX.location != bg_current:
                $ JeanX.location = bg_current
                "[JeanX.name] walks up to you."
        call set_the_scene(0)
        call Display_Girl(JeanX)
        call clear_the_room(JeanX)
        call set_the_scene
        $ JeanX.daily_history.append("relationship")
        call Taboo_Level
        $ line = 0
        $ JeanX.change_face("sly",1,Eyes="side")
        ch_j "Hey. . . [JeanX.Petname]."
        ch_j "Would you. . . want me to call you. . ."
        ch_j "\"Master?\""
        $ JeanX.History.append("master")
        menu:
            "Yeah, do that.":
                    $ JeanX.change_face("sly",1,Eyes="side")
                    $ JeanX.change_stat("love", 200, 5)
                    $ JeanX.change_stat("obedience", 200, 5)
                    ch_j "Well. . . Ok then."
                    $ JeanX.Petname = "master"
            "What? Why?":
                    $ JeanX.change_face("sly",1)
                    $ JeanX.change_stat("obedience", 200, 5)
                    $ JeanX.change_stat("inhibition", 200, 10)
                    $ JeanX.change_stat("lust", 80, 5)
                    ch_j "Because it's -hot!-"
                    ch_j "Duh."
            ". . .":
                    $ JeanX.change_stat("love", 80, -3)
                    $ JeanX.change_stat("obedience", 200, 10)
                    $ JeanX.change_stat("inhibition", 80, -2)
                    ch_j "Well. . ."
                    ch_j ". . ."
                    $ JeanX.change_face("sly",1)
                    $ JeanX.change_stat("inhibition", 80, 10)
                    $ JeanX.change_stat("inhibition", 200, 5)
                    ch_j "I'm going to anyway."
            "Not really.":
                    $ JeanX.change_stat("love", 80, -3)
                    $ JeanX.change_stat("obedience", 80, 3)
                    $ JeanX.change_stat("inhibition", 80, -5)
                    ch_j "Oh. . ."
                    ch_j "Well, ok. . ."
                    return
        $ JeanX.change_stat("obedience", 200, 5)
        $ JeanX.change_stat("inhibition", 200, 5)
        $ JeanX.change_stat("lust", 80, 5)
        $ JeanX.Petnames.append("master")
        $ JeanX.change_face("sly",1)
        ch_j "Master."
        menu:
            "Well. . . ok then.":
                    $ JeanX.change_face("confused",1)
                    $ JeanX.change_stat("inhibition", 80, -1)
                    ch_j ". . . good?"
            "I don't think you understand how this works.":
                    $ JeanX.change_face("confused",1)
                    $ JeanX.change_stat("love", 200, -2)
                    $ JeanX.change_stat("obedience", 80, 1)
                    ch_j "I don't follow."
                    menu:
                        "Never mind.":
                                $ JeanX.change_face("sly",1)
                                $ JeanX.change_stat("love", 200, 5)
                                $ JeanX.change_stat("obedience", 200, 5)
                                $ JeanX.change_stat("inhibition", 200, 2)
                                ch_j "Right!"
                        "Well you're supposed to do what I say. . .":
                                $ JeanX.change_stat("love", 200, 5)
                                $ JeanX.change_stat("obedience", 200, 10)
                                ch_j "Um, yeah."
                                $ JeanX.change_face("sly",1)
                                ch_j "I can do that!"
            "Well, don't.":
                    $ JeanX.change_face("sadside",1)
                    $ JeanX.change_stat("love", 80, -10)
                    $ JeanX.change_stat("obedience", 80, -5)
                    $ JeanX.change_stat("inhibition", 80, -10)
                    ch_j "Oh. . ."
                    ch_j "Bummer."
                    return
        $ JeanX.change_face("sly",1)
        $ JeanX.Petname = "master"
        $ JeanX.change_stat("obedience", 90, 50)
        $ JeanX.change_stat("obedience", 200, 25)
        pause 0.1
        return

label JeanName(Base=0,JNNum=0,Alpha=0,JeanNames={}):
        if Base == 1:
                $ Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                $ JNNum = renpy.random.randint(0,25)
                $ Base = str(Alpha[JNNum]) #peels off random number from alphabet
        elif Base:
                pass
        else:
                $ Base = Player.name[:1] #takes first letter of player's name
        $ JeanNames = { "A":"Abe",
                        "B":"Barry",
                        "C":"Carl",
                        "D":"Dennis",
                        "E":"Erik",
                        "F":"Foggy",
                        "G":"Gil",
                        "H":"Hunk",
                        "I":"Ike",
                        "J":"Jeff",
                        "K":"Kirk",
                        "L":"Lance",
                        "M":"Mitch",
                        "N":"Norm",
                        "O":"Ollie",
                        "P":"Pete",
                        "Q":"Quince",
                        "R":"Rory",
                        "S":"Sonny",
                        "T":"Todd",
                        "U":"Uri",
                        "V":"Vince",
                        "W":"Wally",
                        "X":"Ray",
                        "Y":"Yuri",
                        "Z":"Zoro"
                        }
        $ Base = Base.upper() #should return the upper case version of a lowercase letter?
        if Base in JeanNames and JeanNames[Base] != Player.name:
                $ JeanX.Petname = JeanNames[Base]
        else:
                #If the name is a dupe or not a valid name, pick a random letter
                $ Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                $ JNNum = renpy.random.randint(0,25)
                $ Base = str(Alpha[JNNum]) #peels off random number from alphabet
                $ JeanX.Petname = JeanNames[Base]

        return
